#!/usr/bin/env python3
"""Navigate the design-system research with Jev (TypeSafe's System One model).

  python3 tools/jev_nav.py status            lane progress, Decision Cards, sources
  python3 tools/jev_nav.py find "question"   gathers candidate cards and house standards, then Jev ranks them for the question
  python3 tools/jev_nav.py html              writes navigator.html, a visual map of the research
  python3 tools/jev_nav.py export            writes synthesis/cards.json, every Decision Card split into its fields
  python3 tools/jev_nav.py graph             writes synthesis/decision-graph.json from the cards' depends/affects links
  python3 tools/jev_nav.py check             flags cited source ids missing from traces, unknown card ids and unknown standard ids,
                                             and quotes in the standards' conflicts that the file they name no longer contains

`find` needs JEV_API_KEY (or TYPESAFE_API_KEY) in the environment or in the project's .env;
without it, it falls back to keyword (BM25) ranking.
"""
import argparse, html, json, math, os, re, sys, urllib.error, urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API = "https://api.typesafe.ai/v1/systemone"
CARDS_PER_REQUEST = 20
KEYWORD_CANDIDATES = 60  # 40 left the right cards out of the pool for broad questions (persona triage R34)
CONFIDENT = 0.6  # below this best score, find says it has no confident answer
CITING_OF_TOP = 20  # L19 cards pooled because they cite one of the 20 keyword-top older cards
STANDARD_CANDIDATES = 18  # keyword-top house standards always judged, whatever lane Jev picks (doubled for the STD lane)
DCID = re.compile(r"DC-L\d+-\d+")
STDID = re.compile(r"STD-[a-z]+(?:-[a-z]+)*-\d+")


def lanes():
    """Rows of the BOARD.md lane table: id, scope, output path, status."""
    rows = []
    for line in (ROOT / "_coordination/BOARD.md").read_text().splitlines():
        m = re.match(r"\| (L\d+|S\d|V\d) \| (.+?) \| `?([^|`]+?)`?(?:, .*?)? \| (.+?) \|$", line)
        if m:
            rows.append(dict(id=m[1], scope=m[2], output=m[3].strip(), status=m[4]))
    return rows


def lane_files(lane_id):
    files = sorted((ROOT / "research").glob(f"{lane_id}-*.md")) + sorted((ROOT / "benchmarks").glob(f"{lane_id}-*.md"))
    if lane_id == "L09":
        files += sorted((ROOT / "benchmarks/systems").glob("*.md"))
    return files


def cards(path):
    """Decision Cards in a file: `### DC-...` heading up to the next ### or ## heading."""
    out, cur = [], None
    for n, line in enumerate(path.read_text(errors="replace").splitlines(), 1):
        if line.startswith("### DC-"):
            cur = dict(id=line[4:].split(":")[0], title=line.split(":", 1)[-1].strip(), file=str(path.relative_to(ROOT)), line=n, text=[])
            out.append(cur)
        elif line.startswith(("## ", "### ")):
            cur = None
        elif cur is not None:
            cur["text"].append(line)
    for c in out:
        c["text"] = "\n".join(c["text"]).strip()
    return out


def trace_rows(lane_id):
    p = ROOT / "traces" / f"{lane_id}-trace.md"
    if not p.exists():
        return 0
    return sum(1 for l in p.read_text(errors="replace").splitlines() if re.match(r"\|\s*[^|-]", l) and "S-" in l)


def status(_):
    print(f"{'lane':5} {'cards':>5} {'sources':>7} {'inferred':>8}  status")
    for ln in lanes():
        fs = lane_files(ln["id"])
        cs = [c for f in fs for c in cards(f)]
        inferred = sum(f.read_text(errors="replace").count("[inferred]") for f in fs)
        print(f"{ln['id']:5} {len(cs):>5} {trace_rows(ln['id']):>7} {inferred:>8}  {ln['status'][:70]}")


def api_key():
    """TYPESAFE_API_KEY or JEV_API_KEY from the environment, else JEV_API_KEY from the project's .env."""
    for name in ("TYPESAFE_API_KEY", "JEV_API_KEY"):
        if os.environ.get(name):
            return os.environ[name]
    env = ROOT / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            if line.startswith(("JEV_API_KEY=", "TYPESAFE_API_KEY=")):
                return line.split("=", 1)[1].strip().strip("\"'")
    return None


def jev(state, questions):
    req = urllib.request.Request(API, method="POST", data=json.dumps({"state": state, "model": "jev-latest", "questions": questions}).encode(),
                                 headers={"Authorization": f"Bearer {api_key()}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)["answers"]


def standards_doc():
    p = ROOT / "synthesis/standards.json"
    return json.loads(p.read_text()) if p.exists() else {}


def standards_as_cards(doc):
    """House standards (synthesis/standards.json, lane L19) join the pool, so `find` answers "what is the rule for X?" too."""
    return [dict(id=s["id"], title=s["title"], file="synthesis/standards.json", line=0, theme=s.get("theme", ""), std=s,
                 text=f"House standard ({s['strength']}): {s['rule']} Why: {s['why']} Values: "
                      + "; ".join(f"{k}: {v}" for k, v in (s.get("values") or {}).items()))
            for s in doc.get("standards", [])]


STOPWORDS = set("""a about all an and any are as at be been but by can could did do does for from get had has have
how i if in into is it its just me more most my need no not of on or our should so some than that the their them
then there these they this those to up use using was we were what when where which who why will with would you your""".split())
# Words that fill broad questions ("make my app look good") and appear on hundreds of cards in a design-system corpus:
# counted, they rank cards on "design" and "user" instead of the question's subject. Compared after stemming, so
# "makes", "looking" and "users" go too.
DOMAIN_STOPWORDS = set("ui ux make look design good app user".split())


def stem(word):
    """Crude suffix stripping, so "closes", "closing" and "close" meet, as do "dragged" and "drag"."""
    if word.endswith("ies") and len(word) > 4:
        word = word[:-3] + "y"
    elif word.endswith("sses"):
        word = word[:-2]
    elif word.endswith("es") and len(word) > 4 and not word.endswith(("ses", "ues")):
        word = word[:-2]
    elif word.endswith("s") and len(word) > 3 and not word.endswith(("ss", "us", "is")):
        word = word[:-1]
    for suffix, repl in (("ation", "at"), ("ing", ""), ("ed", ""), ("ly", "")):
        if word.endswith(suffix) and len(word) - len(suffix) >= 3:
            word = word[: -len(suffix)] + repl
            if suffix in ("ing", "ed") and word[-1] == word[-2] and word[-1] not in "lsz":
                word = word[:-1]  # dragg -> drag, sett -> set
            break
    return word[:-1] if word.endswith("e") and len(word) > 3 else word


DOMAIN_STEMS = {stem(w) for w in DOMAIN_STOPWORDS}


def terms(text):
    stems = (stem(w) for w in re.findall(r"[a-z0-9]+", text.lower()) if len(w) > 1 and w not in STOPWORDS)
    return [s for s in stems if s not in DOMAIN_STEMS]


def keyword_rank(query, pool, k1=1.2, b=0.75, title_weight=3):
    """BM25 (the BM25F form: title and text are length-normalised separately, and a title match counts
    `title_weight` times). Rare words count more, and a match in a long card counts less than the same match
    in a short one. Returns only the cards that match at least one term, best first."""
    docs = [(Counter(terms(c["title"])), Counter(terms(c["text"]))) for c in pool]
    lengths = [(sum(t.values()), sum(x.values())) for t, x in docs]
    avg_title = sum(l[0] for l in lengths) / max(len(docs), 1) or 1
    avg_text = sum(l[1] for l in lengths) / max(len(docs), 1) or 1
    q = set(terms(query))
    idf = {}
    for t in q:
        n = sum(1 for title, text in docs if t in title or t in text)
        idf[t] = math.log(1 + (len(docs) - n + 0.5) / (n + 0.5))
    def score(i):
        (title, text), (lt, lx) = docs[i], lengths[i]
        s = 0.0
        for t in q:
            tf = title_weight * title[t] / (1 - b + b * lt / avg_title) + text[t] / (1 - b + b * lx / avg_text)
            s += idf[t] * tf * (k1 + 1) / (tf + k1) if tf else 0
        return s
    scored = sorted(((score(i), i) for i in range(len(pool))), key=lambda t: -t[0])
    return [pool[i] for s, i in scored if s > 0]


def named_standards(card):
    """Standard ids on an L19 card's `Standards:` line."""
    return STDID.findall(fields(card).get("standards", ""))


def house_overrides(all_cards, doc):
    """Older card id -> ids of the L19 cards ("differs from DC-..." on their Default line) and the standards ("supersedes")
    that the house prefers. A standard's "conflicts" only records where OpenDesigner differs today; a card named there is
    not replaced unless the standard lists it under "supersedes" (a card the house keeps, such as DC-L08-18, stays)."""
    out = {}
    for c in all_cards:
        if not c["id"].startswith("DC-L19-"):
            continue
        # Only the card's recommended default overrides an older card; a "differs" note on an option the house did not
        # adopt does not. Both wordings occur: "differs from DC-..." and "Differs: DC-...".
        default = fields(c).get("default") or ""
        for m in re.finditer(r"differs(?:\s+from)?\s*:?", default, re.I):
            clause = re.split(r"[.;]\**(?=\s|$)", default[m.end():], maxsplit=1)[0]
            for old in DCID.findall(clause):
                if not old.startswith("DC-L19-"):
                    out.setdefault(old, set()).add(c["id"])
    for s in doc.get("standards", []):
        for old in s.get("supersedes") or []:
            if DCID.fullmatch(old):
                out.setdefault(old, set()).add(s["id"])
    return out


def options_digest(text, per_option=160, limit=900):
    """A card's Options field, shortened for the judge: each option's first words, so a card whose default is about one
    thing but whose options cover the question (a list of color mistakes, say) is still recognised."""
    rows = [re.sub(r"\*\*", "", l.strip().lstrip("-").strip()) for l in text.splitlines() if l.strip()]
    rows = [r if len(r) <= per_option else r[:per_option].rsplit(" ", 1)[0] + "…" for r in rows]
    out = " | ".join(rows)
    return out if len(out) <= limit else out[:limit].rsplit(" ", 1)[0] + "…"


def judge_text(c):
    """What the judge reads: a standard's rule and values; a card's Questions, Options (shortened), Default and Standards lines."""
    if "std" in c:
        s = c["std"]
        return (f"House standard ({s['strength']}): {s['rule']} Values: "
                + "; ".join(f"{k}: {v}" for k, v in (s.get("values") or {}).items()))
    f = fields(c)
    clean = lambda v: re.sub(r'^[(][^)]*[)] ', '', v)
    parts = [f"{label}: {options_digest(clean(f[key])) if key == 'options' else clean(f[key])}"
             for key, label in (("questions", "Questions"), ("options", "Options"), ("default", "Default"), ("standards", "Standards"))
             if f.get(key)]
    return "\n".join(parts) if parts else c["text"][:900]


def with_overriders(rows, overrides, by_id, order, score=lambda _id: None, relevant=lambda _id: True):
    """rows [(score, card)] -> rows plus, for each overridden card none of whose overriders is listed, its best overrider
    (order: id -> sort key, best first), so a card shown as superseded has what supersedes it on screen. An overrider the
    judge found off the question (relevant false) is not pulled in: the card then keeps its "house differs" note."""
    listed = {c["id"] for _, c in rows}
    out = list(rows)
    for _, c in rows:
        by = overrides.get(c["id"])
        if not by or by & listed:
            continue
        pick = min((b for b in by if b in by_id and relevant(b)), key=order, default=None)
        if pick:
            out.append((score(pick), by_id[pick]))
            listed.add(pick)
    return out


def find(args):
    query, research = args.query, [l for l in lanes() if l["id"].startswith("L")]
    doc = standards_doc()
    std = standards_as_cards(doc)
    everything = [c for l in research for f in lane_files(l["id"]) for c in cards(f)] + std
    overrides = house_overrides(everything, doc)
    ranked = keyword_rank(query, everything)
    by_id = {}
    for c in everything:
        by_id.setdefault(c["id"], c)
    kw_pos = {}
    for n, c in enumerate(ranked):
        kw_pos.setdefault(c["id"], n)
    kw_order = lambda i: kw_pos.get(i, len(ranked))
    if not api_key():
        print("No JEV_API_KEY or TYPESAFE_API_KEY found: using keyword ranking instead of Jev.\n", file=sys.stderr)
        return show(with_overriders([(None, c) for c in ranked[: args.top]], overrides, by_id, kw_order), overrides)

    # 1. Candidates: code retrieves, Jev judges. The keyword-top (BM25) cards across all lanes, the keyword-top
    #    house standards, every card in the research lane Jev picks (catches questions that share no words
    #    with the right card), the L19 cards that cite that lane's cards or the keyword-top older cards (the
    #    newer research on the same decisions), and the standards named on the pooled L19 cards' `Standards:` lines.
    themes = "; ".join(f"{t['title']} ({t['summary']})" for t in doc.get("themes", []))
    lane = jev({"question": query}, {"lane": {
        "type": "choice",
        "instructions": "Which research lane of a design-system research project is most likely to answer `question`?",
        "criteria": {l["id"]: l["scope"] for l in research}
                    | ({"STD": f"House standards, the non-negotiable rules. Themes: {themes}"} if std else {})}})["lane"]["choice"]
    key = lambda c: (c["file"], c["line"], c["id"])
    pool = {}
    def add(cs):
        for c in cs:
            pool.setdefault(key(c), c)
    add([c for c in ranked if "std" not in c][:KEYWORD_CANDIDATES])
    add([c for c in ranked if "std" in c][: STANDARD_CANDIDATES * (2 if lane == "STD" else 1)])
    # L19 cards are the newer research on older decisions: pool the ones that cite the chosen lane's cards, and up to
    # CITING_OF_TOP that cite the keyword-top older cards (a card on the same decision that shares few words with the question).
    l19_cite = lambda ids: sorted((c for c in everything if c["id"].startswith("DC-L19-") and ids & set(DCID.findall(c["text"]))),
                                  key=lambda c: kw_order(c["id"]))
    older_top = set([c["id"] for c in ranked if c["id"].startswith("DC-") and not c["id"].startswith("DC-L19-")][:20])
    citing = l19_cite(older_top)[:CITING_OF_TOP]
    if lane != "STD":
        lane_cards = [c for f in lane_files(lane) for c in cards(f)]
        add(lane_cards)
        if lane != "L19":
            citing += [c for c in l19_cite({c["id"] for c in lane_cards}) if c not in citing]
    add(citing)
    # Standards named on pooled L19 cards, in keyword order; capped so that picking the L19 lane (164 cards)
    # does not pull in nearly every standard.
    std_by_id = {c["id"]: c for c in std}
    l19 = [c for c in ranked if c["id"].startswith("DC-L19-") and key(c) in pool][:KEYWORD_CANDIDATES]
    l19 += [c for c in citing if c not in l19]
    add(std_by_id[s] for c in l19 for s in named_standards(c) if s in std_by_id)
    pool = list(pool.values())

    # 2. Judge: one Noul per card over shared state; batches run in parallel.
    def judge(batch):
        state = {"question": query, "cards": [{"title": c["title"], "text": judge_text(c)} for c in batch]}
        qs = {f"c{j}": {"type": "noul", "instructions": f"Does the Decision Card or house standard `cards[{j}]` directly help answer `question`?",
                        "criteria": {"true": "It gives usable guidance specific to the question's component, property or situation "
                                             "(it names it, or a category that plainly includes it)",
                                     "false": "It is about something else or only mentions the subject in passing; or it is a general "
                                              "process, workflow or review rule (how to build, check or review work) that does not name "
                                              "the question's component or property"}}
              for j in range(len(batch))}
        answers = jev(state, qs)
        return [(answers[f"c{j}"]["noul"], c) for j, c in enumerate(batch)]

    batches = [pool[i:i + CARDS_PER_REQUEST] for i in range(0, len(pool), CARDS_PER_REQUEST)]
    with ThreadPoolExecutor(max_workers=4) as ex:
        scored = sorted((s for b in ex.map(judge, batches) for s in b), key=lambda t: -t[0])
    top = scored[: args.top]
    good = [c for s, c in top if s >= 0.5]
    lanes_hit = sorted({c["id"].split("-")[1] for c in good if c["id"].startswith("DC-")})
    themes_hit = sorted({c.get("theme") or c["id"].split("-")[1] for c in good if not c["id"].startswith("DC-")})
    n_std = sum(1 for c in pool if "std" in c)
    print(f"Judged {len(pool) - n_std} cards and {n_std} house standards (Jev's lane pick: {lane}); answers from "
          + (", ".join(lanes_hit + ([f"STD ({', '.join(themes_hit)})"] if themes_hit else [])) or "nothing above 0.5") + "\n")
    if not top or top[0][0] < CONFIDENT:
        print(f"No confident answer: the best card scores {top[0][0] if top else 0:.2f}, under {CONFIDENT}. "
              "The closest cards follow; treat them as leads, not answers.\n")
    judged = {}
    for s, c in scored:
        judged.setdefault(c["id"], s)
    show(with_overriders(top, overrides, by_id, lambda i: (-judged.get(i, -1.0), kw_order(i)), judged.get,
                         lambda i: judged.get(i, 1.0) >= 0.5), overrides)


def show(rows, overrides=None):
    """Print the results, rows [(score or None, card)]. A card the house differs from is marked. When the card or standard
    that supersedes it is in the list too, the card moves just below it and is labelled superseded (its score then sits
    out of order on purpose)."""
    overrides = overrides or {}
    rows = list(rows)
    for _ in range(len(rows)):
        moved = False
        for i, (_, c) in enumerate(rows):
            later = [j for j in range(i + 1, len(rows)) if rows[j][1]["id"] in overrides.get(c["id"], ())]
            if later:
                rows.insert(later[-1], rows.pop(i))
                moved = True
                break
        if not moved:
            break
    listed = {c["id"] for _, c in rows}
    short = lambda ids: ", ".join(ids[:3]) + (f" +{len(ids) - 3}" if len(ids) > 3 else "")
    scored = any(s is not None for s, _ in rows)
    for s, c in rows:
        tag = f"{s:.2f}  " if s is not None else ("  -   " if scored else "")
        by = sorted(overrides.get(c["id"], ()))
        shown = [b for b in by if b in listed]
        note = (f"  (superseded by {short(shown)})" if shown
                else f"  (house differs: {short(by)})" if by else "")
        where = f"{c['file']}:{c['line']}" if c["line"] else f"{c['file']} ({c['id']}; readable in skills/opendesigner/references/standards/)"
        print(f"{tag}{c['id']}: {c['title']}{note}\n      {where}")


FIELD = re.compile(r"^- \*\*(.+?):\*\*\s*(.*)$")


CANONICAL = ["block path", "questions", "options", "visual effect", "depends on", "affects", "token encoding",
             "platform notes", "accessibility constraints", "default", "evidence"]


def fields(card):
    """Split a card body into its `- **Field:** value` entries (values may continue on following lines).
    Variant labels such as "Options (real values)" fold into the canonical field, keeping the qualifier."""
    out, key = {}, None
    for line in card["text"].splitlines():
        m = FIELD.match(line)
        if m:
            label = m[1].strip().lower()
            key = next((c for c in CANONICAL if label.startswith(c)), label)
            value = m[2].strip() if key == label or label.split(" (")[0] == key else f"({label}) {m[2].strip()}"
            out[key] = (out[key] + "\n" + value) if key in out else value
        elif key and line.strip():
            out[key] += "\n" + line.strip()
    return out


def export(_):
    rows = []
    for ln in lanes():
        for f in lane_files(ln["id"]):
            for c in cards(f):
                rows.append(dict(id=c["id"], lane=ln["id"], title=c["title"], file=c["file"], line=c["line"], **fields(c)))
    out = ROOT / "synthesis/cards.json"
    out.write_text(json.dumps(rows, indent=1, ensure_ascii=False))
    keys = {}
    for r in rows:
        for k in r:
            keys[k] = keys.get(k, 0) + 1
    print(f"{len(rows)} cards -> {out}")
    print("field coverage: " + ", ".join(f"{k} {v}" for k, v in sorted(keys.items(), key=lambda kv: -kv[1])))


def graph(_):
    """Decision graph from the cards' depends/affects fields: edges point from a decision to what it constrains.
    Question order = topological order of the condensed graph (cycles collapse into one step)."""
    rows = json.loads((ROOT / "synthesis/cards.json").read_text())
    ids = {r["id"] for r in rows}
    ref = re.compile(r"DC-L\d+-\d+")
    edges = set()
    for r in rows:
        edges |= {(d, r["id"]) for d in ref.findall(r.get("depends on", "")) if d in ids and d != r["id"]}
        edges |= {(r["id"], a) for a in ref.findall(r.get("affects", "")) if a in ids and a != r["id"]}
    overrides = ROOT / "synthesis/graph-overrides.json"
    if overrides.exists():
        o = json.loads(overrides.read_text())
        edges |= {(a, b) for a, b, _ in o.get("add", []) if a in ids and b in ids}
        edges -= {(a, b) for a, b, _ in o.get("remove", [])}
    succ = {i: set() for i in ids}
    for a, b in edges:
        succ[a].add(b)

    # Tarjan's strongly connected components, then Kahn's topological sort over the components.
    index, low, stack, on, comps, counter = {}, {}, [], set(), [], [0]
    def strong(v):
        index[v] = low[v] = counter[0]; counter[0] += 1; stack.append(v); on.add(v)
        for w in succ[v]:
            if w not in index:
                strong(w); low[v] = min(low[v], low[w])
            elif w in on:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            comp = []
            while True:
                w = stack.pop(); on.discard(w); comp.append(w)
                if w == v:
                    break
            comps.append(sorted(comp))
    sys.setrecursionlimit(10000)
    for v in sorted(ids):
        if v not in index:
            strong(v)
    comp_of = {v: i for i, c in enumerate(comps) for v in c}
    csucc = {i: set() for i in range(len(comps))}
    indeg = {i: 0 for i in range(len(comps))}
    for a, b in edges:
        if comp_of[a] != comp_of[b] and comp_of[b] not in csucc[comp_of[a]]:
            csucc[comp_of[a]].add(comp_of[b]); indeg[comp_of[b]] += 1
    level, frontier, order = {}, sorted(i for i in indeg if indeg[i] == 0), []
    for i in frontier:
        level[i] = 0
    while frontier:
        nxt = []
        for i in frontier:
            order.append(i)
            for j in csucc[i]:
                level[j] = max(level.get(j, 0), level[i] + 1); indeg[j] -= 1
                if indeg[j] == 0:
                    nxt.append(j)
        frontier = sorted(nxt)
    title = {r["id"]: r["title"] for r in rows}
    out = dict(
        nodes=[dict(id=r["id"], lane=r["lane"], title=r["title"], block=r.get("block path", ""),
                    step=level[comp_of[r["id"]]], fan_out=len(succ[r["id"]])) for r in rows],
        edges=[dict(source=a, target=b) for a, b in sorted(edges)],
        cycles=[c for c in comps if len(c) > 1])
    (ROOT / "synthesis/decision-graph.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
    steps = max(level.values()) + 1
    print(f"{len(rows)} decisions, {len(edges)} edges, {steps} dependency steps, {len(out['cycles'])} cycles -> synthesis/decision-graph.json")
    print("Most influential (decisions that constrain the most others):")
    for n in sorted(out["nodes"], key=lambda n: -n["fan_out"])[:12]:
        print(f"  {n['fan_out']:>3}  step {n['step']}  {n['id']}: {n['title']}")
    for c in out["cycles"]:
        print("  cycle: " + " <-> ".join(f"{i} ({title[i][:30]})" for i in c[:6]))


def check(_):
    """Citation integrity: every S-id cited must be logged in a trace; every DC id referenced must exist;
    every STD id cited must be a standard (active or retired) in synthesis/standards.json."""
    sid = re.compile(r"S-[A-Z]+\d*[a-z]?-\d+")
    defined = {s for p in (ROOT / "traces").glob("*-trace.md") for s in sid.findall(p.read_text(errors="replace"))}
    cards_known = {c["id"] for l in lanes() for f in lane_files(l["id"]) for c in cards(f)}
    doc = standards_doc()
    std_known = {s["id"] for s in doc.get("standards", [])} | {r["id"] for r in doc.get("retired", [])}
    docs = [p for d in ("research", "benchmarks", "benchmarks/systems", "synthesis", "sources") for p in sorted((ROOT / d).glob("*.md"))]
    std_docs = (sorted((ROOT / "research").glob("*.md")) + sorted((ROOT / "synthesis").glob("*.md"))
                + [p for p in sorted((ROOT / "synthesis").glob("*.json")) if p.name != "standards.json"]
                + sorted((ROOT / "learn/wiki/synthesis").glob("*.md")))
    bad = 0
    for p in sorted(set(docs) | set(std_docs)):
        text = p.read_text(errors="replace")
        missing_s = sorted(set(sid.findall(text)) - defined) if p in docs else []
        missing_dc = sorted(set(DCID.findall(text)) - cards_known) if p in docs else []
        missing_std = sorted(set(STDID.findall(text)) - std_known) if p in std_docs else []
        if missing_s or missing_dc or missing_std:
            bad += 1
            problems = [f"{len(ids)} {what} {ids[:6]}" for ids, what in ((missing_s, "source ids not in any trace"),
                        (missing_dc, "unknown card ids"), (missing_std, "unknown standard ids")) if ids]
            print(f"{p.relative_to(ROOT)}: " + "; ".join(problems))
    stale = stale_conflict_quotes(doc)
    for sid, files, quote in stale:
        print(f"synthesis/standards.json {sid} conflicts: '{quote}' is no longer in {' or '.join(files)}")
    print(f"\n{len(set(docs) | set(std_docs))} files checked, {len(defined)} source ids logged, {len(cards_known)} cards, "
          f"{len(std_known)} standards; {bad} files with dangling references; {len(stale)} standards' conflict quotes "
          "no longer in the file they name")


STAGES = "skills/opendesigner/references/stages"
PATH_REF = re.compile(r"(?<![\w.-])((?:skills|synthesis|research|learn|tools|docs|benchmarks)/[\w./-]*?\w\.(?:py|md|json|html|js))(?![\w-])")
STAGE_REF = re.compile(r"(?<![\w.-])(\d\d-[a-z0-9-]+?)(?:\.detailed)?\.md\b")
ROOT_DOC = re.compile(r"(?<![\w./-])((?:AGENTS|README|CLAUDE|CHANGELOG)\.md)\b")
QUOTE = re.compile(r"(?<![\w'])'([^'\n]{12,}?)'(?![\w'])")


def stale_conflict_quotes(doc):
    """(standard id, files, quote) for each quoted fragment in a standard's "conflicts" that no file the entry names still
    contains, so a conflict about text that has since changed is caught (R32). Cheap by design: exact text after folding
    case, spaces, backticks and escapes; fragments with <placeholders>, an ellipsis or no readable file are skipped."""
    cache = {}
    def text(rel):
        if rel not in cache:
            p = ROOT / rel
            raw = p.read_text(errors="replace") if p.is_file() else None
            cache[rel] = fold(raw.replace('\\"', '"').replace("\\'", "'")) if raw is not None else None
        return cache[rel]
    fold = lambda s: re.sub(r"\s+", " ", s.replace("`", "").replace("’", "'").replace("“", '"').replace("”", '"')).lower()
    out = []
    for s in doc.get("standards", []):
        for entry in s.get("conflicts") or []:
            files = set(PATH_REF.findall(entry))
            files |= {"skills/opendesigner/scripts/engine.py"} if re.search(r"(?<![\w/.-])engine\.py\b", entry) else set()
            for stem_ in STAGE_REF.findall(entry):  # a stage file named bare or by its folder, with its detailed twin
                files |= {f"{STAGES}/{stem_}.md", f"{STAGES}/{stem_}.detailed.md"}
            files |= set(ROOT_DOC.findall(entry))
            for lane in {m.split("-")[1] for m in DCID.findall(entry)}:  # a quote from a card the entry names
                files |= {str(p.relative_to(ROOT)) for p in lane_files(lane)}
            files = sorted(f for f in files if text(f) is not None)
            if not files:
                continue
            for quote in QUOTE.findall(entry):
                if re.search(r"<[a-z][\w.-]*>|\.\.\.|…", quote):
                    continue
                if not any(fold(quote) in text(f) for f in files):
                    out.append((s["id"], files, quote))
    return out


def build_html(_):
    blocks = []
    for ln in lanes():
        fs = lane_files(ln["id"])
        cs = [c for f in fs for c in cards(f)]
        done = ln["status"].startswith("done")
        items = "".join(f'<li><a href="{html.escape(c["file"])}">{html.escape(c["id"])}</a> {html.escape(c["title"])}</li>' for c in cs)
        files = " ".join(f'<a href="{html.escape(str(f.relative_to(ROOT)))}">{html.escape(f.name)}</a>' for f in fs) or "<span class=muted>no file yet</span>"
        blocks.append(f"""<section class="lane{' done' if done else ''}"><header><b>{ln['id']}</b><span class="pill">{html.escape(ln['status'][:48])}</span></header>
<p>{html.escape(ln['scope'])}</p><div class="stats"><span>{len(cs)} cards</span><span>{trace_rows(ln['id'])} sources</span></div>
<div class="files">{files}</div>{f'<details><summary>Decision Cards</summary><ol>{items}</ol></details>' if cs else ''}</section>""")
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Research Navigator</title><style>
:root{{--bg:#f7f6f3;--card:#fff;--ink:#1d1c1a;--muted:#6b6862;--line:#e4e1da;--accent:#3d5afe;--ok:#1f8a4c}}
@media (prefers-color-scheme:dark){{:root{{--bg:#131312;--card:#1c1c1a;--ink:#eceae4;--muted:#9c9890;--line:#2e2d2a;--accent:#8c9eff;--ok:#5fd08f}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 ui-sans-serif,system-ui,-apple-system,sans-serif}}
main{{max-width:1200px;margin:0 auto;padding:32px 16px}}h1{{font-size:28px;margin:0 0 4px}}.muted,p{{color:var(--muted)}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px;margin-top:24px}}
.lane{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px}}.lane.done{{border-color:var(--ok)}}
header{{display:flex;justify-content:space-between;gap:8px;align-items:center}}.pill{{font-size:12px;color:var(--muted);border:1px solid var(--line);border-radius:99px;padding:2px 8px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:70%}}
.stats{{display:flex;gap:12px;font-size:13px;font-weight:600}}.files{{font-size:13px;margin-top:8px;overflow-wrap:anywhere}}a{{color:var(--accent)}}
details{{margin-top:8px;font-size:13px}}ol{{padding-left:20px;max-height:280px;overflow:auto}}</style></head>
<body><main><h1>Design-system research</h1><p>Lanes, Decision Cards and sources. Regenerate with <code>python3 tools/jev_nav.py html</code>; ask questions with <code>python3 tools/jev_nav.py find "…"</code>.</p>
<div class="grid">{''.join(blocks)}</div></main></body></html>"""
    (ROOT / "navigator.html").write_text(page)
    print(ROOT / "navigator.html")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status").set_defaults(fn=status)
    f = sub.add_parser("find"); f.add_argument("query"); f.add_argument("--top", type=int, default=10); f.set_defaults(fn=find)
    sub.add_parser("html").set_defaults(fn=build_html)
    sub.add_parser("export").set_defaults(fn=export)
    sub.add_parser("graph").set_defaults(fn=graph)
    sub.add_parser("check").set_defaults(fn=check)
    a = ap.parse_args()
    try:
        a.fn(a)
    except urllib.error.HTTPError as e:
        sys.exit(f"TypeSafe API error {e.code}: {e.read().decode()[:300]}")
