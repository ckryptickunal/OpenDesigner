#!/usr/bin/env python3
"""Navigate the design-system research with Jev (TypeSafe's System One model).

  python3 tools/jev_nav.py status            lane progress, Decision Cards, sources
  python3 tools/jev_nav.py find "question"   gathers candidate cards, then Jev ranks them for the question
  python3 tools/jev_nav.py html              writes navigator.html, a visual map of the research
  python3 tools/jev_nav.py export            writes synthesis/cards.json, every Decision Card split into its fields
  python3 tools/jev_nav.py graph             writes synthesis/decision-graph.json from the cards' depends/affects links
  python3 tools/jev_nav.py check             flags cited source ids missing from traces and unknown card ids

`find` needs JEV_API_KEY (or TYPESAFE_API_KEY) in the environment or in the project's .env;
without it, it falls back to keyword ranking.
"""
import argparse, html, json, os, re, sys, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API = "https://api.typesafe.ai/v1/systemone"
CARDS_PER_REQUEST = 20
KEYWORD_CANDIDATES = 40


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


def keyword_rank(query, pool):
    terms = set(re.findall(r"\w{3,}", query.lower()))
    return sorted(pool, key=lambda c: -sum((c["title"] + " " + c["text"]).lower().count(t) for t in terms))


def find(args):
    query, research = args.query, [l for l in lanes() if l["id"].startswith("L")]
    everything = [c for l in research for f in lane_files(l["id"]) for c in cards(f)]
    if not api_key():
        print("No JEV_API_KEY or TYPESAFE_API_KEY found: using keyword ranking instead of Jev.\n", file=sys.stderr)
        return show(keyword_rank(query, everything)[: args.top], None)

    # 1. Candidates: code retrieves, Jev judges. Keyword matches across all lanes, plus every card
    #    in the lane Jev picks (catches questions that share no words with the right card).
    lane = jev({"question": query}, {"lane": {
        "type": "choice",
        "instructions": "Which research lane of a design-system research project is most likely to answer `question`?",
        "criteria": {l["id"]: l["scope"] for l in research}}})["lane"]["choice"]
    pool = {(c["file"], c["line"]): c for c in keyword_rank(query, everything)[:KEYWORD_CANDIDATES]}
    pool |= {(c["file"], c["line"]): c for f in lane_files(lane) for c in cards(f)}
    pool = list(pool.values())

    # 2. Judge: one Noul per card over shared state; batches run in parallel.
    def judge(batch):
        state = {"question": query, "cards": [{"title": c["title"], "text": c["text"][:900]} for c in batch]}
        qs = {f"c{j}": {"type": "noul", "instructions": f"Does the Decision Card `cards[{j}]` directly help answer `question`?",
                        "criteria": {"true": "The card addresses the question's subject and gives usable guidance",
                                     "false": "The card is about something else or only mentions it in passing"}}
              for j in range(len(batch))}
        answers = jev(state, qs)
        return [(answers[f"c{j}"]["noul"], c) for j, c in enumerate(batch)]

    batches = [pool[i:i + CARDS_PER_REQUEST] for i in range(0, len(pool), CARDS_PER_REQUEST)]
    with ThreadPoolExecutor(max_workers=4) as ex:
        scored = sorted((s for b in ex.map(judge, batches) for s in b), key=lambda t: -t[0])
    top = scored[: args.top]
    print(f"Judged {len(pool)} candidate cards (Jev's lane pick: {lane}); answers from " +
          ", ".join(sorted({c['id'].split('-')[1] for s, c in top if s >= 0.5})) + "\n")
    show([c for _, c in top], [s for s, _ in top])


def show(ranked, scores):
    for i, c in enumerate(ranked):
        tag = f"{scores[i]:.2f}  " if scores else ""
        print(f"{tag}{c['id']}: {c['title']}\n      {c['file']}:{c['line']}")


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
    """Citation integrity: every S-id cited must be logged in a trace; every DC id referenced must exist."""
    sid, dcid = re.compile(r"S-L\d+-\d+"), re.compile(r"DC-L\d+-\d+")
    defined = {s for p in (ROOT / "traces").glob("*-trace.md") for s in sid.findall(p.read_text(errors="replace"))}
    cards_known = {c["id"] for l in lanes() for f in lane_files(l["id"]) for c in cards(f)}
    docs = [p for d in ("research", "benchmarks", "benchmarks/systems", "synthesis", "sources") for p in sorted((ROOT / d).glob("*.md"))]
    bad = 0
    for p in docs:
        text = p.read_text(errors="replace")
        missing_s = sorted(set(sid.findall(text)) - defined)
        missing_dc = sorted(set(dcid.findall(text)) - cards_known)
        if missing_s or missing_dc:
            bad += 1
            print(f"{p.relative_to(ROOT)}: {len(missing_s)} source ids not in any trace {missing_s[:6]}"
                  f"{'; ' + str(len(missing_dc)) + ' unknown card ids ' + str(missing_dc[:6]) if missing_dc else ''}")
    print(f"\n{len(docs)} files checked, {len(defined)} source ids logged, {len(cards_known)} cards; {bad} files with dangling references")


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
