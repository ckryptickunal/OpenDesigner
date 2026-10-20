"""The evals page's live sections. A docs page writes {{evals:<name>}} on its own line; site/build.py swaps in the block below,
built from the committed result files, so the page always shows the last real run and never a number typed by hand:

    evals/agent/latest.json      tools/agent_evals.py --save   (claude plugin eval, with and without the plugin)
    evals/design/latest.json     tools/design_evals.py         (the engine on fixed briefs, no AI)
    evals/checkers/latest.json   tools/checker_evals.py        (our checkers on pages with planted mistakes)
    brand/showcase/audit/*.json  the showcase audits: round 4 blind test, then each rebuilt piece's round 4 or 5 record

A file that does not exist yet shows a plain "not run yet" line instead of a number.
"""
import html
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
esc = html.escape
GH = "https://github.com/ckryptickunal/OpenDesigner"


def _load(rel):
    p = ROOT / rel
    return json.loads(p.read_text()) if p.exists() else None


def _pct(x):
    return f"{round(x * 100)}%" if isinstance(x, (int, float)) else "–"


def _meta(parts):
    return '<p class="ev-meta">' + " · ".join(esc(str(p)) for p in parts if p) + "</p>"


def _table(head, rows, cls=""):
    th = "".join(f"<th>{esc(h)}</th>" for h in head)
    num = lambda c: bool(re.fullmatch(r"[\d.,%+–\- ]*(of [\d,]+|pts|%)?|<code>.*</code>.*", str(c)))
    body = "".join("<tr>" + "".join(f'<td class="n">{c}</td>' if num(c) else f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table class="ev-table {cls}"><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'


LABELS = {"builds": "builds", "no-errors": "no validation errors", "text-contrast": "text contrast 4.5:1", "ui-contrast": "borders and focus 3:1",
          "targets": "target sizes", "brand-kept": "brand color kept exactly", "exports": "every export written", "design-md": "DESIGN.md written",
          "same-twice": "same result twice", "type-steps": "type sizes 10% apart", "button-visible": "primary button stands out 3:1",
          "says-so": "the engine warns about each miss"}


def _case_description(name):
    p = ROOT / "evals" / name / "prompt.md"
    if not p.exists():
        return ""
    m = re.search(r"^description:\s*(.+)$", p.read_text(), re.M)
    return m.group(1).strip() if m else ""


def showcase_numbers():
    """Round 4 started with a blind test of the gallery as it stood: 37 pairs against shipped screens (AUDIT-ROUND4.md).
    After it, every rebuilt piece carries its own round 4 or 5 record with the fresh reviewer's score."""
    rebuilt, passed, held = 0, 0, 0
    for f in sorted((ROOT / "brand/showcase/audit").glob("*.json")):
        j = json.loads(f.read_text())
        latest = j.get("round5") or j.get("round4")
        if not latest:
            continue
        rebuilt += 1
        score = latest.get("score") or 0
        if score >= 4:
            passed += 1
        elif (j.get("owner") or {}).get("verdict") == "hold":
            held += 1
    return {"before_pairs": 37, "before_lost": 30, "rebuilt": rebuilt, "passed": passed, "held": held}


def block(name):
    if name == "summary":
        ag, de, ch, sc = _load("evals/agent/latest.json"), _load("evals/design/latest.json"), _load("evals/checkers/latest.json"), showcase_numbers()
        tiles = []
        if ag:
            tiles.append(("Agent evals", f"{_pct(ag.get('overallScore'))} with OpenDesigner",
                          f"{_pct((ag.get('overallScore') or 0) - (ag.get('meanDelta') or 0))} without it, on the same {ag.get('casesTotal')} tasks"))
        if de:
            tiles.append(("Design evals", f"{de['passed']} of {de['checks']} required checks",
                          f"{de['briefs']} briefs; {de.get('qualityPassed')} of {de.get('qualityChecks')} stricter quality checks"))
        if ch and ch.get("checkers"):
            cs = ch["checkers"].values()
            planted, caught, alarms = sum(c.get("planted", 0) for c in cs), sum(c.get("caught", 0) for c in cs), sum(c.get("falseAlarms", 0) for c in cs)
            tiles.append(("Checker evals", f"{caught} of {planted} planted mistakes caught",
                          f"{len(ch['checkers'])} checkers; {alarms} false alarms on clean pages"))
        tiles.append(("Showcase audit", f"{sc['passed']} of {sc['rebuilt']} rebuilt pieces pass",
                      f"before: ours lost {sc['before_lost']} of {sc['before_pairs']} blind pairs"))
        return f'<div class="ev-stats" data-n="{len(tiles)}">' + "".join(f'<div class="ev-stat"><p class="kicker">{esc(k)}</p><p class="ev-big">{esc(v)}</p><p class="ev-sub">{esc(s)}</p></div>'
                                                for k, v, s in tiles) + "</div>"
    if name == "agent":
        ag = _load("evals/agent/latest.json")
        if not ag:
            return '<p class="ev-meta">Not run yet.</p>'
        rows = []
        for c in ag["cases"]:
            d = c.get("delta")
            rows.append([f'<strong>{esc(c["name"])}</strong><br><span class="ev-desc">{esc(_case_description(c["name"]))}</span>', _pct(c.get("score")),
                         _pct(c.get("without")) if c.get("without") is not None else "–",
                         (("+" if d > 0 else "") + f"{round(d * 100)}" + " pts") if isinstance(d, (int, float)) else "–"])
        return _table(["Task", "With OpenDesigner", "Without", "Difference"], rows) + _meta([
            f"Run {ag['date']}", f"commit {ag.get('commit')}", f"agent model: {ag.get('model')}", f"judge: {ag.get('judgeModel')}",
            f"{ag.get('runsPerArm')} runs per task per arm", f"Claude Code {ag.get('claudeVersion')}",
            f"about ${ag.get('costUsd'):.2f}" if isinstance(ag.get("costUsd"), (int, float)) else ""])
    if name == "agent-changes":
        ch = _load("evals/agent/changes.json") or {"changes": []}
        rows = []
        for c in ch["changes"]:
            before, after = _load(f"evals/agent/results/{c['date']}-{c['id']}-before.json"), _load(f"evals/agent/results/{c['date']}-{c['id']}-after.json")
            if not (before and after):
                continue
            b, a = before["cases"][0], after["cases"][0]
            rows.append([f'<strong>{esc(c["case"])}</strong><br><span class="ev-desc">{esc(c["what"])}</span>', _pct(b.get("score")), _pct(a.get("score")),
                         f'<code>{esc(before.get("skillsRef", ""))}</code> → ' + (f'<code>{esc(c["fixCommit"])}</code>' if c.get("fixCommit") else "the fix")])
        if not rows:
            return '<p class="ev-meta">No before-and-after runs yet.</p>'
        return _table(["Fix", "Before", "After", "Skills"], rows) + _meta(["same cases and graders; only the skills differ", "3 runs each, with the plugin"])
    if name == "design":
        de = _load("evals/design/latest.json")
        if not de:
            return '<p class="ev-meta">Not run yet.</p>'
        rows = []
        for r in de["rows"]:
            miss = [LABELS.get(k, k) for k, ok in r["checks"].items() if not ok] + [LABELS.get(k, k) + " (quality)" for k, ok in r.get("quality", {}).items() if not ok]
            rows.append([f'<strong>{esc(r["id"])}</strong><br><span class="ev-desc">{esc(r["why"])}</span>', f'{r["passed"]} of {r["of"]}',
                         f'{sum(r.get("quality", {}).values())} of {len(r.get("quality", {}))}', esc(", ".join(miss)) or "none"])
        return _table(["Brief", "Required", "Quality", "Missed"], rows) + _meta([f"Run {de['date']}", f"commit {de.get('commit')}",
                                                                                 "no AI involved; the same answers give the same files"])
    if name == "checkers":
        ch = _load("evals/checkers/latest.json")
        if not ch:
            return '<p class="ev-meta">Not run yet.</p>'
        rows = [[f'<strong>{esc(k)}</strong>', f'{v.get("caught")} of {v.get("planted")}', _pct(v.get("precision")), str(v.get("falseAlarms", 0))]
                for k, v in ch.get("checkers", {}).items()]
        out = _table(["Checker", "Planted mistakes caught", "Precision", "False alarms (clean pages)"], rows)
        hist = ch.get("history") or []
        if hist:
            out += _table(["Layout checker version", "Date", "Caught", "What changed"],
                          [[f'<code>{esc(h.get("commit", ""))}</code>', esc(h.get("date", "")), f'{h.get("caught")} of {h.get("planted")}', esc(h.get("note", ""))] for h in hist])
        return out + _meta([f"Run {ch.get('date')}", f"commit {ch.get('commit')}", "deterministic: two runs give the same result"])
    if name == "checker-changes":
        ch, chg = _load("evals/checkers/latest.json"), _load("evals/checkers/changes.json")
        before = _load("evals/checkers/" + chg["before"]) if chg else None
        if not (ch and chg and before):
            return '<p class="ev-meta">No checker fixes recorded yet.</p>'
        rows = []
        for f in chg["fixes"]:
            b, a = before["checkers"].get(f["checker"], {}), ch["checkers"].get(f["checker"], {})
            fmt = lambda c: f'{c.get("caught")} of {c.get("planted")} caught, {_pct(c.get("precision"))} precise, {c.get("falseAlarms", 0)} false alarms'
            rows.append([f'<strong>{esc(f["checker"])}</strong><br><span class="ev-desc">{esc(f["what"])}</span>', esc(fmt(b)), esc(fmt(a))])
        return _table(["Bug the evals found", "Before the fix", "After"], rows) + _meta(["same test pages, same scoring; only the checker changed"])
    if name == "showcase":
        sc = showcase_numbers()
        rows = [["Before (round 4 audit, 15 Oct 2026)", f"In {sc['before_pairs']} blind pairs against shipped products, ours lost {sc['before_lost']}.",
                 f'<a href="{GH}/blob/main/brand/showcase/AUDIT-ROUND4.md">AUDIT-ROUND4.md</a>'],
                ["After (rebuilt pieces, rounds 4 and 5)", f"{sc['rebuilt']} pieces rebuilt. {sc['passed']} reached 4 of 5 with a fresh reviewer after a blind test; "
                 f"{sc['held']} stay hidden until they do.", f'<a href="{GH}/tree/main/brand/showcase/audit">audit records</a>']]
        return _table(["", "Result", "Evidence"], rows)
    raise SystemExit(f"unknown evals block: {name}")
