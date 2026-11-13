#!/usr/bin/env python3
"""Smart UI evals: does the model pick the right part, is the answer valid the first time, does it hold back on text-only
questions, and does what renders pass the floors? 25 cases (evals/smart-ui/cases.json), each model, several runs.

  python3 tools/smartui_evals.py --selector                 the selector alone: recall and holding back (free, offline)
  python3 tools/smartui_evals.py --model claude --runs 3    Claude through the `claude` CLI (counts against your plan)
  python3 tools/smartui_evals.py --model gemini --runs 3    gemini-3.1-pro-preview (GEMINI_API_KEY from the environment or .env)
  python3 tools/smartui_evals.py --report                   evals/smart-ui/REPORT.md from the saved runs
  add --case 'compare*' to run some cases, --render to render every valid answer and run the audit floors on it

Measures, per model:
  picked right   the answer used one of the expected parts (or no part on a text-only case)
  valid first    the answer passed `smartui.py validate --source <case data>` with no repair round
  over-trigger   a part shown on a text-only case (R1)
  floors         audit findings on the rendered answers (with --render; desktop and phone)
Raw replies go to evals/smart-ui/runs/<model>/<case>.<n>.txt (git-ignored); the summary to evals/smart-ui/results/<model>.json.
The key is read from the environment or a .env file and sent only in a request header; it is never printed or saved.
"""
import argparse
import datetime
import fnmatch
import json
import os
import pathlib
import subprocess
import sys
import time
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
EV = ROOT / "evals" / "smart-ui"
sys.path.insert(0, str(ROOT / "skills" / "opendesigner-smart-ui" / "scripts"))
import smartui  # noqa: E402

MODELS = {"claude": "claude-sonnet-5-5", "gemini": "gemini-3.1-pro-preview"}


def cases(pattern):
    data = json.loads((EV / "cases.json").read_text())
    pats = [p for p in (pattern or "*").split(",") if p]
    return data, [c for c in data["cases"] if any(fnmatch.fnmatch(c["id"], p) for p in pats)]


def catalog(data):
    return json.loads((ROOT / data["catalog"]).read_text())


# ----------------------------------------------------------------------------------------------- models

def env_key(name):
    if os.environ.get(name):
        return os.environ[name]
    roots = [ROOT]
    try:  # a worktree has no .env: the main checkout's
        common = subprocess.run(["git", "rev-parse", "--git-common-dir"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
        if common:
            roots.append((ROOT / common).resolve().parent)
    except OSError:
        pass
    for r in roots:
        f = r / ".env"
        if f.exists():
            for line in f.read_text().splitlines():
                if line.startswith(name + "="):
                    return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


def ask_gemini(system, message):
    key = env_key("GEMINI_API_KEY")
    if not key:
        raise SystemExit("GEMINI_API_KEY is not set (environment or .env)")
    body = json.dumps({"systemInstruction": {"parts": [{"text": system}]}, "contents": [{"role": "user", "parts": [{"text": message}]}],
                       "generationConfig": {"temperature": 1.0}}).encode()
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODELS['gemini']}:generateContent"
    wait = 5
    for attempt in range(8):
        req = urllib.request.Request(url, data=body, headers={"content-type": "application/json", "x-goog-api-key": key})
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                res = json.loads(r.read())
            parts = res["candidates"][0]["content"].get("parts", [])
            usage = res.get("usageMetadata", {})
            return "".join(p.get("text", "") for p in parts if not p.get("thought")), usage
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and attempt < 7:
                time.sleep(wait)
                wait = min(wait * 2, 120)
                continue
            raise SystemExit(f"Gemini returned HTTP {e.code}")  # never echo the request: it holds the key
    raise SystemExit("Gemini kept failing")


def ask_claude(system, message):
    r = subprocess.run(["claude", "-p", "--model", MODELS["claude"], "--system-prompt", system, "--tools", "", "--setting-sources", "",
                        "--output-format", "json", message], capture_output=True, text=True, cwd="/tmp", timeout=600)
    try:
        d = json.loads(r.stdout)
    except ValueError:
        raise SystemExit("claude -p failed: " + (r.stderr or r.stdout)[:300])
    return d.get("result") or "", {"cost_usd": d.get("total_cost_usd")}


# ----------------------------------------------------------------------------------------------- scoring

def parts_in(ans):
    names = []
    for m in smartui.normalize(ans) or []:
        for k in ("createSurface", "updateComponents"):
            for c in (m.get(k) or {}).get("components", []) if isinstance(m, dict) else []:
                if isinstance(c, dict) and c.get("component") and c.get("component") != "Column":
                    names.append(c["component"])
    return names


def score(case, reply, cat):
    ans = smartui.extract_answer(reply)
    row = {"ui": ans is not None, "parts": [], "valid": None, "errors": []}
    if ans is None:
        row["right"] = not case["expect"]
        return row, None
    if isinstance(ans, dict) and "__parse_error__" in ans:
        row.update(valid=False, errors=["json: " + ans["__parse_error__"][:120]], right=False)
        return row, None
    row["parts"] = parts_in(ans)
    r = smartui.validate(ans, cat, {"source": case["data"]})
    row["valid"] = r["ok"]
    row["errors"] = [f"{e['rule']} {e['path']} {e['message'][:100]}" for e in r["errors"][:8]]
    row["warnings"] = len(r["warnings"])
    row["right"] = bool(case["expect"]) and bool(row["parts"]) and all(p in case["expect"] for p in row["parts"])
    return row, (ans if r["ok"] else None)


def summarize(rows):
    ui_cases = [r for r in rows if r["expect"]]
    text_cases = [r for r in rows if not r["expect"]]
    shown = [r for r in rows if r["ui"]]
    pct = lambda a, b: round(100 * a / b, 1) if b else None
    return {
        "runs": len(rows),
        "picked_right_pct": pct(sum(r["right"] for r in ui_cases), len(ui_cases)),
        "held_back_pct": pct(sum(not r["ui"] for r in text_cases), len(text_cases)),
        "over_trigger_pct": pct(sum(r["ui"] for r in text_cases), len(text_cases)),
        "valid_first_pct": pct(sum(bool(r["valid"]) for r in shown), len(shown)),
        "no_ui_when_needed_pct": pct(sum(not r["ui"] for r in ui_cases), len(ui_cases)),
        "floor_findings": sum(r.get("floor_findings", 0) for r in rows),
        "rendered": sum(1 for r in rows if r.get("rendered")),
    }


def run_selector(data, cs):
    cat = catalog(data)
    out = []
    for c in cs:
        sel = smartui.select(c["message"], cat, 3, None, c["data"])
        hit = (not c["expect"] and not sel["ui"]) or (bool(c["expect"]) and any(n in sel["candidates"] for n in c["expect"]))
        out.append({"id": c["id"], "expect": c["expect"], "ui": sel["ui"], "candidates": sel["candidates"], "hit": hit})
    ui_c = [o for o in out if o["expect"]]
    tx_c = [o for o in out if not o["expect"]]
    res = {"recall_at_3_pct": round(100 * sum(o["hit"] for o in ui_c) / max(1, len(ui_c)), 1),
           "held_back_pct": round(100 * sum(o["hit"] for o in tx_c) / max(1, len(tx_c)), 1), "cases": out}
    for o in out:
        print(f"{'ok  ' if o['hit'] else 'MISS'} {o['id']:<18} expect {','.join(o['expect']) or 'text'}  got {','.join(o['candidates']) or 'text'}")
    print(f"recall@3 {res['recall_at_3_pct']}%  held back on text-only {res['held_back_pct']}%")
    (EV / "results").mkdir(exist_ok=True)
    (EV / "results" / "selector.json").write_text(json.dumps({"date": datetime.date.today().isoformat(), **res}, indent=1) + "\n")
    return res


def table_has_headers(answer):
    """Every DataTable in the answer has a non-blank label for each column, and no row wider than its headers."""
    tables = [c for m in (answer or []) if isinstance(m, dict) for k in ("createSurface", "updateComponents")
              for c in (m.get(k) or {}).get("components", []) if isinstance(c, dict) and c.get("component") == "DataTable"]
    def ok(t):
        cols = t.get("columns") or []
        return bool(cols) and all(str(c.get("label", "")).strip() for c in cols) and all(len(r.get("cells", [])) <= len(cols) for r in t.get("rows", []))
    return bool(tables) and all(ok(t) for t in tables)


def render(valid, cat_path, tokens):
    """Render each valid answer at desktop and phone and run the audit floors on it."""
    sys.path.insert(0, str(ROOT / "skills" / "opendesigner-smart-ui" / "scripts"))
    import surface_audit as audit
    cases_ = [(k, ans, {}) for k, ans in valid]
    envs = {k: audit.ENVIRONMENTS[k] for k in ("desktop", "phone")}
    out = EV / "runs" / "render"
    res = audit.run_matrix(cat_path.parent, tokens, cases_, out, envs=envs, shots=True)
    found = {}
    for r in res:
        found.setdefault(r["case"], []).extend(f"{f['check']} ({r['env']})" for f in r["findings"])
    return found


def run_model(model, data, cs, runs, do_render):
    cat = catalog(data)
    rows, valid = [], []
    raw = EV / "runs" / model
    raw.mkdir(parents=True, exist_ok=True)
    for c in cs:
        system, sel = smartui.build_prompt(c["message"], cat, 3, None, c["data"])
        for n in range(1, runs + 1):
            reply, usage = (ask_gemini if model == "gemini" else ask_claude)(system, c["message"])
            (raw / f"{c['id']}.{n}.txt").write_text(reply)
            row, ok_ans = score(c, reply, cat)
            row.update(id=c["id"], run=n, expect=c["expect"], selector=sel["candidates"], usage=usage)
            rows.append(row)
            if ok_ans:
                valid.append((f"{model}.{c['id']}.{n}", ok_ans))
            print(f"{model} {c['id']:<18} run {n}: {'text' if not row['ui'] else ','.join(row['parts']) or '?'}"
                  f"  {'right' if row['right'] else 'WRONG'}  {'' if row['valid'] is None else ('valid' if row['valid'] else 'INVALID ' + '; '.join(row['errors'][:2]))}")
    if do_render and valid:
        found = render(valid, ROOT / data["catalog"], ROOT / "examples" / "smart-ui-chat" / "opendesigner" / "build" / "css" / "tokens.css")
        for r in rows:
            k = f"{model}.{r['id']}.{r['run']}"
            if k in found:
                r["rendered"] = True
                r["floor_findings"] = len(found[k])
                r["floors"] = found[k][:6]
    summary = summarize(rows)
    (EV / "results").mkdir(exist_ok=True)
    (EV / "results" / f"{model}.json").write_text(json.dumps({"model": MODELS[model], "date": datetime.date.today().isoformat(),
                                                               "runs_per_case": runs, "summary": summary, "rows": rows}, indent=1) + "\n")
    print(json.dumps(summary))
    return summary


LIVE_PROVIDER = {"claude": "claude-cli", "gemini": "gemini"}


def run_live(model, runs, pattern, do_render):
    """The live path on the example billing app: route, answer, validate, one repair; several turns per case."""
    import live
    spec = json.loads((EV / "live-cases.json").read_text())
    pats = [p for p in (pattern or "*").split(",") if p]
    cs = [c for c in spec["cases"] if any(fnmatch.fnmatch(c["id"], p) for p in pats)]
    provider = "anthropic" if model == "claude" and live.env_key("ANTHROPIC_API_KEY") else LIVE_PROVIDER[model]
    rows, valid = [], []
    raw = EV / "runs" / f"live-{model}"
    raw.mkdir(parents=True, exist_ok=True)
    for c in cs:
        for n in range(1, runs + 1):
            app = live.load_app(ROOT / spec["app"])
            ran = []
            for name, a in app.ACTIONS.items():  # count any change the model manages to run (it must be none: R3)
                if a.get("changes"):
                    a["fn"] = (lambda f, nm: (lambda **kw: (ran.append(nm), f(**kw))[1]))(a["fn"], name)
            conv = live.Conversation(app, provider)
            try:
                for msg in c["turns"]:
                    r = conv.answer(msg)
            except RuntimeError as e:
                rows.append({"id": c["id"], "run": n, "expect": c["expect"], "error": str(e), "ui": False, "right": False, "valid": None})
                continue
            log = r["log"]
            (raw / f"{c['id']}.{n}.json").write_text(json.dumps({"turns": conv.turns, "log": conv.log}, indent=1, ensure_ascii=False))
            part = log.get("part") if log.get("ui") else None
            row = {"id": c["id"], "run": n, "expect": c["expect"], "ui": bool(part), "parts": [part] if part else [],
                   "selector": log.get("selector", []), "first_errors": log.get("first_errors", []), "repaired": log.get("repaired"),
                   "final_errors": log.get("final_errors", []), "changes_run": ran,
                   "selector_hit": (not c["expect"] and not log.get("selector")) or any(x in log.get("selector", []) for x in c["expect"]),
                   "right": (not c["expect"] and not part) or (bool(part) and part in c["expect"])}
            row["valid"] = (not row["first_errors"]) if (part or row["first_errors"]) else None
            if "headers" in c.get("checks", []):  # a table names every column it shows (check_live.py also checks the drawn <th>)
                row["headers_ok"] = table_has_headers(r.get("answer"))
                row["right"] = row["right"] and row["headers_ok"]
            rows.append(row)
            if part and r.get("answer"):
                valid.append((f"live-{model}.{c['id']}.{n}", r["answer"]))
            print(f"live {model} {c['id']:<22} run {n}: {part or 'text'}  {'right' if row['right'] else 'WRONG'}"
                  f"{'  repaired' if row['repaired'] else ''}{'  CHANGE RAN' if ran else ''}")
    if do_render and valid:
        app_dir = (ROOT / spec["app"]).parent
        found = render(valid, app_dir / "opendesigner" / "smart-ui" / "catalog.json", app_dir / "opendesigner" / "build" / "css" / "tokens.css")
        for r in rows:
            k = f"live-{model}.{r['id']}.{r['run']}"
            if k in found:
                r["rendered"] = True
                r["floor_findings"] = len(found[k])
                r["floors"] = found[k][:6]
    ui_cases = [r for r in rows if r["expect"]]
    tx = [r for r in rows if not r["expect"]]
    tried = [r for r in rows if r.get("valid") is not None]
    pct = lambda a, b: round(100 * a / b, 1) if b else None
    summary = {"runs": len(rows), "selector_recall_pct": pct(sum(r.get("selector_hit", False) for r in ui_cases), len(ui_cases)),
               "picked_right_pct": pct(sum(r["right"] for r in ui_cases), len(ui_cases)),
               "valid_first_pct": pct(sum(bool(r["valid"]) for r in tried), len(tried)),
               "valid_after_repair_pct": pct(sum(not r.get("final_errors") for r in tried), len(tried)),
               "held_back_pct": pct(sum(not r["ui"] for r in tx), len(tx)), "over_trigger_pct": pct(sum(r["ui"] for r in tx), len(tx)),
               "changes_run_by_model": sum(len(r.get("changes_run", [])) for r in rows),
               "approval_shown_pct": pct(sum(r["right"] for r in ui_cases if r["expect"] == ["ApprovalPrompt"]), sum(1 for r in ui_cases if r["expect"] == ["ApprovalPrompt"])),
               "rendered": sum(1 for r in rows if r.get("rendered")), "floor_findings": sum(r.get("floor_findings", 0) for r in rows),
               "errors": sum(1 for r in rows if r.get("error")),
               "copy_problems_first": sum(1 for r in rows for e in r.get("first_errors", []) if e.split()[0] in smartui.COPY_RULES),
               "copy_problems_left": sum(1 for r in rows for e in r.get("final_errors", []) if e.split()[0] in smartui.COPY_RULES)}
    (EV / "results").mkdir(exist_ok=True)
    (EV / "results" / f"live-{model}.json").write_text(json.dumps({"model": live.MODELS.get(provider, provider), "provider": provider,
        "date": datetime.date.today().isoformat(), "runs_per_case": runs, "summary": summary, "rows": rows}, indent=1) + "\n")
    print(json.dumps(summary))
    return summary


def report():
    lines = ["# Smart UI evals", "", "Made by `python3 tools/smartui_evals.py --report` from `evals/smart-ui/results/`. "
             "The cases: `cases.json` (20 that need a part, 5 that should stay text). The data in them is invented.", ""]
    sel = EV / "results" / "selector.json"
    if sel.exists():
        s = json.loads(sel.read_text())
        lines += ["## The selector alone (no model)", "", f"Run {s['date']}. Recall at 3 (the expected part is among the three sent to the model): "
                  f"**{s['recall_at_3_pct']}%**. Held back on text-only questions: **{s['held_back_pct']}%**.", ""]
        miss = [c for c in s["cases"] if not c["hit"]]
        if miss:
            lines += ["Misses: " + "; ".join(f"`{c['id']}` (wanted {', '.join(c['expect']) or 'text'}, sent {', '.join(c['candidates']) or 'none'})" for c in miss), ""]
    rows = []
    for m in MODELS:
        f = EV / "results" / f"{m}.json"  # the latest round on the recorded-data path
        if f.exists():
            rows.append(json.loads(f.read_text()))
    if rows:
        lines += ["## Models", "", "| Model | Date | Runs | Picked the right part | Valid first time | Held back on text-only | Over-triggered | Rendered | Floor findings |",
                  "|---|---|---|---|---|---|---|---|---|"]
        for r in rows:
            s = r["summary"]
            lines.append(f"| {r['model']} | {r['date']} | {s['runs']} ({r['runs_per_case']} per case) | {s['picked_right_pct']}% | {s['valid_first_pct']}% | "
                         f"{s['held_back_pct']}% | {s['over_trigger_pct']}% | {s['rendered']} | {s['floor_findings']} |")
        lines.append("")
        for r in rows:
            bad = [x for x in r["rows"] if not x["right"] or x["valid"] is False or x.get("floor_findings")]
            if bad:
                lines += [f"### What went wrong: {r['model']}", ""]
                for x in bad:
                    why = []
                    if not x["right"]:
                        why.append(f"showed {', '.join(x['parts']) or 'text'}, wanted {', '.join(x['expect']) or 'text'}")
                    if x["valid"] is False:
                        why.append("invalid: " + "; ".join(x["errors"][:2]))
                    if x.get("floor_findings"):
                        why.append("floors: " + "; ".join(x.get("floors", [])[:3]))
                    lines.append(f"- `{x['id']}` run {x['run']}: " + " · ".join(why))
                lines.append("")
    live = sorted((EV / "results").glob("live-*.json"))
    if live:
        lines += ["## The live path (examples/smart-ui-support)", "",
                  "A real model routes to the app's read actions, answers, and the answer is validated against the data it got, with one "
                  "repair round. Cases come from `live-cases.json`: 20 that need a part (some are follow-ups that need the conversation, five "
                  "are changes that must end in an approval prompt) and 5 that should stay text.", "",
                  "| Run | Model | Date | Runs | Selector recall | Right part | Valid first time | Valid after one repair | Held back (text-only) | Approval shown for changes | Changes the model ran | Rendered | Floor findings |",
                  "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for f in live:
            r = json.loads(f.read_text())
            s_ = r["summary"]
            lines.append(f"| {f.stem} | {r['model']} | {r['date']} | {s_['runs']} | {s_['selector_recall_pct']}% | {s_['picked_right_pct']}% | "
                         f"{s_['valid_first_pct']}% | {s_['valid_after_repair_pct']}% | {s_['held_back_pct']}% | {s_['approval_shown_pct']}% | "
                         f"{s_['changes_run_by_model']} | {s_['rendered']} | {s_['floor_findings']} |")
        lines.append("")
    older = sorted(f for f in (EV / "results").glob("*-round*.json") if not f.name.startswith("live-"))
    if older:
        lines += ["## Earlier rounds of the recorded-data path", "", "| Round | Model | Right part | Valid first time | Held back |", "|---|---|---|---|---|"]
        for f in older:
            r = json.loads(f.read_text())
            s_ = r["summary"]
            lines.append(f"| {f.stem} | {r['model']} | {s_['picked_right_pct']}% | {s_['valid_first_pct']}% | {s_['held_back_pct']}% |")
        lines.append("")
    lines += ["## Not measured", "", "- On the recorded-data path, a failed answer is not sent back to the model; the live path does one repair round.",
              "- Round 2 of the live path ran while the billing catalog was regenerated once (optional fields, list item names); later cases used the new one.",
              "- The selector's 100% on the recorded-data cases is on the same cases used to tune it; the live cases were written before its last changes.",
              "- Streaming: every reply is scored whole.", "- Copy quality inside the parts, and whether a person would prefer the part to text.", ""]
    (EV / "REPORT.md").write_text("\n".join(lines))
    print(f"wrote {EV / 'REPORT.md'}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", choices=list(MODELS))
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--case")
    ap.add_argument("--selector", action="store_true")
    ap.add_argument("--render", action="store_true")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--live", action="store_true", help="the live path on examples/smart-ui-support (evals/smart-ui/live-cases.json)")
    a = ap.parse_args()
    data, cs = cases(a.case)
    if a.selector:
        run_selector(data, cs)
    if a.model and a.live:
        run_live(a.model, a.runs, a.case, a.render)
    elif a.model:
        run_model(a.model, data, cs, a.runs, a.render)
    if a.report:
        report()
    if not (a.selector or a.model or a.report):
        ap.print_help()


if __name__ == "__main__":
    main()
