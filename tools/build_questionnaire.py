#!/usr/bin/env python3
"""Build synthesis/questionnaire.json from synthesis/QUESTIONNAIRE.md and validate the flow.

  python3 tools/build_questionnaire.py          validate, refresh time weights and the merge table, write JSON
  python3 tools/build_questionnaire.py --check  validate only

Checks: every DC id exists in cards.json; every S id appears in traces/; every Q id referenced exists;
no question is asked before a question it depends on (decision-graph.json edges, including overrides);
each graph cycle sits on one stage.
"""
import json, re, sys, glob, collections
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SYN = ROOT / "synthesis"
MD = SYN / "QUESTIONNAIRE.md"
OUT = SYN / "questionnaire.json"

cards = {c["id"]: c for c in json.load(open(SYN / "cards.json"))}
graph = json.load(open(SYN / "decision-graph.json"))
fan = {n["id"]: n["fan_out"] for n in graph["nodes"]}
step = {n["id"]: n["step"] for n in graph["nodes"]}
trace_ids = set()
for f in glob.glob(str(ROOT / "traces" / "*.md")) + glob.glob(str(ROOT / "research" / "*.md")) + [str(ROOT / "benchmarks" / "L09-benchmark-matrix.md")]:
    trace_ids |= set(re.findall(r"S-L\d\d-\d{3}", open(f, errors="ignore").read()))

DC = re.compile(r"DC-L\d\d-\d\d")
SID = re.compile(r"S-L\d\d-\d{3}")
QID = re.compile(r"\bQ-[a-z]+-\d\d\b")
MODES = {"Quick": ["quick", "standard", "expert"], "Standard": ["standard", "expert"],
         "Expert": ["expert"], "Any": ["quick", "standard", "expert"]}
FIELD = re.compile(r"^- \*\*(.+?):\*\* ?(.*)$")
# Block class per question, applying L17's scheme (DC-L17-01); the mapping is this file's judgment [inferred]. Default G.
CLASS_NAMES = {"G": "generatable", "E": "extractable", "D": "designer-owned", "T": "tool-assisted", "I": "owner input"}
CLASS = {}
for c, ids in {
    "I": "scope-01 scope-02 scope-03 scope-04 scope-05 scope-06 aud-01 aud-02 aud-03 aud-04 brand-01 brand-02 brand-05 brand-07 "
         "plat-01 plat-02 plat-03 plat-04 plat-05 plat-07 plat-08 plat-09 tool-01 tool-02 tool-03 theme-03 type-04 "
         "voice-06 comp-02 color-19 ai-01 pattern-05 pattern-06 gov-01 gov-02 gov-03 gov-04 gov-05 gov-06 pref-01 pref-02 pref-03",
    "E": "ref-01 color-01",
    "D": "brand-03 brand-08 icon-06 img-01 img-04 img-06 img-07 motion-08 shape-05",
    "T": "icon-01 type-01 type-02 voice-01 tool-04 token-07 token-08 dist-01 dist-02 dist-03 viz-01 comp-01 gov-07 motion-09 color-06 depth-04 icon-07",
}.items():
    for i in ids.split():
        CLASS["Q-" + i] = c


def parse(text):
    stages, qs, cur_stage, cur_q, in_opts = [], [], None, None, False
    for line in text.split("\n"):
        m = re.match(r"^## Stage (\d\d) · (.+)$", line)
        if m:
            cur_stage = {"id": f"S{m.group(1)}", "n": int(m.group(1)), "title": m.group(2), "screen": "", "questions": []}
            stages.append(cur_stage); cur_q = None; continue
        if line.startswith("## "):
            cur_stage = None; cur_q = None; continue
        if cur_stage and line.startswith("> ") and not cur_stage["screen"]:
            cur_stage["screen"] = line[2:].strip(); continue
        m = re.match(r"^### (Q-[a-z]+-\d\d) · (.+) · (Quick|Standard|Expert|Any)$", line)
        if m and cur_stage:
            cur_q = {"id": m.group(1), "stage": cur_stage["id"], "question": m.group(2), "mode": m.group(3),
                     "modes": MODES[m.group(3)], "fields": collections.OrderedDict(), "options": []}
            qs.append(cur_q); cur_stage["questions"].append(cur_q["id"]); in_opts = False; continue
        if not cur_q:
            continue
        m = FIELD.match(line)
        if m:
            label, val = m.group(1), m.group(2).strip()
            in_opts = label == "Options"
            if not in_opts:
                cur_q["fields"][label] = val
            continue
        if in_opts and line.startswith("  - "):
            o = line[4:].strip()
            vals = re.match(r"^((?:`[^`]+`(?: / )?)+)\s*(.*)$", o)
            values = re.findall(r"`([^`]+)`", vals.group(1)) if vals else []
            rest = vals.group(2) if vals else o
            label, _, effect = rest.partition(": ")
            cur_q["options"].append({"value": values[0] if len(values) == 1 else values, "label": label.strip(),
                                     "effect": effect.strip(), "refs": sorted(set(DC.findall(o) + SID.findall(o)))})
    return stages, qs


def finish(q):
    f = q.pop("fields")
    d = f.get("Default", "")
    default, _, src = d.partition("*Source:*")
    dec = f.get("Decides", "")
    decides = [] if dec.lower().startswith("none") else DC.findall(dec)
    ch = f.get("Changes", "")
    ch_cards, _, blocks = ch.partition(" · blocks: ")
    hook = f.get("Hook")
    h = None
    if hook:
        acc, _, ifno = hook.partition("If no:")
        h = {"accepts": acc.replace("Accepts", "", 1).strip(" :."), "if_no": ifno.strip()}
    ev = f.get("Evidence", "")
    fo = max([fan.get(c, 0) for c in decides] or [0])
    q.update({
        "ask": f.get("Ask", "").strip('"'), "example": f.get("Example", ""), "why": f.get("Why", ""),
        "control": f.get("Control", ""), "show_if": f.get("Show if"),
        "default": default.strip(" ."), "default_source": src.strip(),
        "decides": decides, "graph_step": max([step.get(c, 0) for c in decides] or [0]), "fan_out": fo,
        "changes": sorted(set(DC.findall(ch_cards))), "blocks": [b.strip() for b in blocks.split(";") if b.strip()],
        "preview": f.get("Preview", ""), "use_avoid": f.get("Use / avoid"), "hook": h, "dials": f.get("Dials"),
        "pre_answers": QID.findall(f.get("Pre-answers", "")) or None,
        "skip": f.get("Skip", ""), "evidence": {"cards": sorted(set(DC.findall(ev))), "sources": sorted(set(SID.findall(ev)))},
        "merges": re.findall(r"\b([KBPD]\d+(?:\.\d+)?)\b", f.get("Merges", "")),
    })
    st = f.get("Status", "")
    q["status"] = "planned" if st.lower().startswith("planned") else "active"
    if q["status"] == "planned":
        q["planned_note"] = st.split(".", 1)[1].strip() if "." in st else ""
    kind = "hook" if h else ("reference" if q["mode"] == "Any" else ("input" if not decides else "decision"))
    q["kind"] = kind
    q["block_class"] = CLASS.get(q["id"], "G")
    if fo >= 5 or q["mode"] == "Quick":
        tw = "high"
    elif fo >= 2 or kind in ("hook", "input", "reference") or q["block_class"] == "I":
        tw = "medium"
    else:
        tw = "low"
    q["time_weight"] = tw
    return q


def table_section(text, title):
    m = re.search(r"^## " + re.escape(title) + r".*?\n(.*?)(?=\n## |\Z)", text, re.S | re.M)
    rows = []
    if not m:
        return rows
    lines = [l for l in m.group(1).split("\n") if l.startswith("|")]
    if len(lines) < 3:
        return rows
    head = [h.strip().lower() for h in lines[0].strip("|").split("|")]
    for l in lines[2:]:
        cells = [c.strip() for c in l.strip("|").split("|")]
        rows.append(dict(zip(head, cells)))
    return rows


def main():
    text = MD.read_text()
    stages, qs = parse(text)
    qs = [finish(q) for q in qs]
    byid = {q["id"]: q for q in qs}
    problems = []
    # ids
    for dc in set(DC.findall(text)) - set(cards):
        problems.append(f"unknown card {dc}")
    for sid in sorted(set(SID.findall(text)) - trace_ids):
        problems.append(f"source id not found in traces/research: {sid}")
    for qid in sorted(set(QID.findall(text)) - set(byid)):
        problems.append(f"unknown question id referenced: {qid}")
    dup = [k for k, v in collections.Counter(q["id"] for q in qs).items() if v > 1]
    problems += [f"duplicate question id {d}" for d in dup]
    # ordering
    pos = {}
    for si, st in enumerate(stages):
        for qi, qid in enumerate(st["questions"]):
            for c in byid[qid]["decides"]:
                pos.setdefault(c, (st["n"], qi, qid))
    viol = []
    cyc_of = {c: i for i, cyc in enumerate(graph["cycles"]) for c in cyc}
    for e in graph["edges"]:
        a, b = pos.get(e["source"]), pos.get(e["target"])
        same_cycle = e["source"] in cyc_of and cyc_of.get(e["source"]) == cyc_of.get(e["target"])
        if a and b and a[2] != b[2] and not (same_cycle and a[0] == b[0]) and (a[0], a[1]) > (b[0], b[1]):
            viol.append(f"{e['source']} ({a[2]}) must precede {e['target']} ({b[2]})")
    for cyc in graph["cycles"]:
        st = {pos[c][0] for c in cyc if c in pos}
        if len(st) > 1:
            viol.append(f"cycle split across stages: {cyc}")
    decided = set(pos)
    auto = set(DC.findall(" ".join(r.get("card", "") for r in table_section(text, "Auto-applied rules"))))
    notasked = set(DC.findall(" ".join(r.get("card", "") for r in table_section(text, "Not asked"))))
    missing = sorted(set(cards) - decided - auto - notasked)
    problems += [f"card not covered: {c}" for c in missing]
    problems += viol
    print(f"{len(stages)} stages, {len(qs)} questions; quick {sum(q['mode']=='Quick' for q in qs)}, "
          f"standard {sum(q['mode'] in ('Quick','Standard') for q in qs)}, expert {sum(q['mode']!='Any' for q in qs)}, "
          f"any-mode panel {sum(q['mode']=='Any' for q in qs)}; "
          f"covered cards: asked {len(decided)}, auto {len(auto)}, not asked {len(notasked)}, missing {len(missing)}")
    print(f"graph: {len(graph['nodes'])} nodes, {len(graph['edges'])} edges, {len(graph['cycles'])} cycles; ordering violations {len(viol)}")
    for p in problems:
        print("PROBLEM:", p)
    if "--check" in sys.argv:
        return
    # refresh time-weight lines in the markdown
    out, cur = [], None
    for line in text.split("\n"):
        m = re.match(r"^### (Q-[a-z]+-\d\d) · ", line)
        if m:
            cur = byid.get(m.group(1))
        if (line.startswith("- **Time weight:**") or line.startswith("- **Block class:**")) and cur and "high, medium or low" not in line and "G, E, D, T or I" not in line:
            continue
        if line.startswith("- **Evidence:**") and cur:
            out.append(f"- **Block class:** {cur['block_class']} ({CLASS_NAMES[cur['block_class']]})")
            out.append(f"- **Time weight:** {cur['time_weight']} (fan-out {cur['fan_out']})")
        out.append(line)
    text = "\n".join(out)
    # merge table
    K = []
    for h, n in [(0, 5), (1, 6), (2, 8), (3, 6), (4, 5), (5, 5), (6, 5), (7, 6), (8, 5), (9, 7), (10, 5), (11, 6), (12, 4), (13, 4)]:
        K += [f"K{h}.{i}" for i in range(1, n + 1)]
    groups = [("L11 kickoff (K, 77)", K), ("L06 brand (B, 15)", [f"B{i}" for i in range(1, 16)]),
              ("L10 platform (P, 26)", [f"P{i}" for i in range(1, 27)]), ("L14 device extract (D, 7)", [f"D{i}" for i in range(1, 8)])]
    where = collections.defaultdict(list)
    for q in qs:
        for c in q["merges"]:
            if q["id"] not in where[c]:
                where[c].append(q["id"])
    rows = ["| Source | Where each question went |", "|---|---|"]
    for name, codes in groups:
        rows.append(f"| {name} | " + "; ".join(f"{c} {', '.join(where.get(c, ['(none)']))}" for c in codes) + " |")
    unplaced = [c for _, codes in groups for c in codes if c not in where]
    text = re.sub(r"<!-- MERGE_TABLE -->|\| Source \| Where each question went \|.*?(?=\n\n)", "\n".join(rows), text, count=1, flags=re.S)
    MD.write_text(text)
    merge_log = [{"source": c, "questions": where.get(c, [])} for _, codes in groups for c in codes]
    doc = {
        "meta": {
            "title": "Guided decision flow (questionnaire)", "file": "synthesis/QUESTIONNAIRE.md", "built_by": "tools/build_questionnaire.py",
            "graph": {"nodes": len(graph["nodes"]), "edges": len(graph["edges"]), "cycles": len(graph["cycles"]), "ordering_violations": len(viol)},
            "counts": {"stages": len(stages), "sequential_screens": len(stages) - 1, "questions": len(qs),
                       "quick": sum(q["mode"] == "Quick" for q in qs),
                       "standard": sum(q["mode"] in ("Quick", "Standard") for q in qs),
                       "expert": sum(q["mode"] != "Any" for q in qs), "any_mode_panel": sum(q["mode"] == "Any" for q in qs),
                       "planned": sum(q["status"] == "planned" for q in qs)},
            "planned": [q["id"] for q in qs if q["status"] == "planned"],
            "modes": {"quick": "Quick questions only; everything else takes its default",
                      "standard": "Quick + Standard questions", "expert": "every question",
                      "any": "reference panel, available on every screen, never required"},
            "quick_order": [q["id"] for q in qs if q["mode"] == "Quick"],
            "time_weight_rule": "high: a decided card has fan-out 5+ or the question is Quick; medium: fan-out 2-4, or an asset hook, input question, the reference panel, or block class I; low: otherwise",
            "block_classes": CLASS_NAMES,
            "quick_mode_assumed_owner_inputs": [q["id"] for q in qs if q["block_class"] == "I" and q["mode"] != "Quick"
                                                and q["status"] != "planned"],
            "unplaced_source_questions": unplaced,
        },
        "interview_protocol": [
            "Start at zoom 0 (sketch): the five questions in references/zoom.md, then build. Nobody picks a mode. After each level, offer to stop or to zoom into one area (pacing.json areas, with rough minutes). Offer the reference panel (Q-ref-01) and keep it open.",
            "Walk the chosen area's stages in order. Open each with one sentence on what it decides; render its preview if the host can show visuals, else describe the example in words.",
            "Ask each question at or below the zoom level being worked (questions.json zoom) whose show_if holds, using its ask line. Skip questions with status planned: the feature is not built yet, so ask nothing and record nothing.",
            "time_weight high: explain why, show 2-3 options with effect and a real system, recommend the default with its source, state what it changes. medium: ask with the default and main alternatives. low: state the default in one line and confirm.",
            "Asset hooks (kind=hook): ask whether the person has the asset, accept hook.accepts formats, otherwise offer hook.if_no paths with their caveats.",
            "Record {question id, option value, set_by: chosen|confirmed_default|auto_default|reference}. Questions above the zoom level reached take their default and stay editable.",
            "If an answer conflicts with an earlier one in the same cycle, show the conflict and settle it with the ranked principles (Q-brand-07). Do not average silently.",
            "After each stage, summarize decisions in plain sentences and append them to the decision log for later sessions and teammates.",
            "Only offer listed option values; record anything else as a custom value with the person's reason.",
            "Show on the best surface the host supports (MCP view, canvas or artifact, Figma or Paper via MCP, local HTML, host question tool, plain text); say which is in use; never block on a visual (DC-L18-06).",
            "One question per turn: recommended option plus 2-3 closest alternatives with a visual each, 'other' allowed, one line on what it changes; one high-weight question per turn, up to three low-weight ones grouped; a single form is fine on cycle screens (DC-L18-08, DC-L18-09).",
            "Gates: approve after scope stages 01-05 (with the block map tagged by block_class), after direction stages 06-08, and after the asset checklist; finish with a coverage check. At zoom 0 and 1 keep only the direction gate (DC-L17-12, DC-L17-09).",
            "Never invent owner-input (block_class I) answers: below zoom 2, record meta.quick_mode_assumed_owner_inputs as assumed and list them for confirmation at the end (DC-L17-08).",
            "Write durable outputs to the user's repo: DTCG tokens (canonical), DESIGN.md, an ADR-style decision log, a state file with answers, statuses and coverage, an AGENTS.md pointer, and exported lint rules (DC-L18-10, DC-L18-11).",
        ],
        "stages": stages,
        "questions": qs,
        "auto_applied": table_section(text, "Auto-applied rules"),
        "not_asked": table_section(text, "Not asked"),
        "merge_log": merge_log,
        "disagreements": table_section(text, "Where lanes or systems disagree"),
    }
    # one stage or question per line: small on disk, easy for a model to read step by step
    parts, keys = [], list(doc)
    for i, k in enumerate(keys):
        v, comma = doc[k], "," if i < len(keys) - 1 else ""
        if isinstance(v, list):
            body = ",\n".join(json.dumps(x, ensure_ascii=False, separators=(",", ":")) for x in v)
            parts.append(f"{json.dumps(k)}:[\n{body}\n]{comma}")
        else:
            parts.append(f"{json.dumps(k)}:{json.dumps(v, ensure_ascii=False, indent=1)}{comma}")
    text_out = "{\n" + "\n".join(parts) + "\n}\n"
    json.loads(text_out)
    OUT.write_text(text_out)
    print(f"wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
