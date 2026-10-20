#!/usr/bin/env python3
"""Agent evals: run OpenDesigner's skills on small tasks with `claude plugin eval`, with and without the plugin.

    python3 tools/agent_evals.py                       every case, 3 runs per arm (the default; costs model usage)
    python3 tools/agent_evals.py --case 'contrast*' --runs 1     one case, one run per arm, while writing a case
    python3 tools/agent_evals.py --tag smoke           the quick set
    python3 tools/agent_evals.py --save                also write the summary to evals/agent/results/<date>.json and latest.json
    python3 tools/agent_evals.py --ref 9dcd6ba --case 'no-identity*' --ablation none    the skills as they were at a commit
                                                       (before and after a change: same cases, same graders, older skills)

The cases live in evals/<case>/ (prompt.md, graders/, and fixtures beside them). `claude plugin eval` refuses a plugin folder
with more than 20,000 entries, and this repo is bigger than that, so the script first assembles the plugin exactly as a
person installs it (the manifest and skills/) plus the cases into dist/eval-plugin/ (git-ignored), and runs it there.

Every run is a real Claude Code session on your own account and counts against your plan or API bill. Each case runs twice
per round: once with OpenDesigner loaded and once without it, so the report shows what the plugin adds (the Δ column).
The cases' scaffold scripts (they copy a fixture into the workspace) run with --scaffold. Defaults: Sonnet for the agent and Haiku for the judge, pinned so scores compare over time; a $15 ceiling. Raw runs and the
HTML report stay in dist/eval-plugin/evals/results/; only the summary below is committed.
"""
import argparse
import datetime
import json
import pathlib
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
STAGE = ROOT / "dist" / "eval-plugin"
OUT = ROOT / "evals" / "agent"
SKIP = {"results", "design", "checkers", "agent"}


def stage(ref=None):
    if STAGE.exists():
        shutil.rmtree(STAGE)
    STAGE.mkdir(parents=True)
    if ref:  # the plugin as it was at that commit; the cases and graders stay today's, so only the skills differ
        archive = subprocess.run(["git", "archive", ref, ".claude-plugin", "skills"], cwd=ROOT, capture_output=True, check=True).stdout
        subprocess.run(["tar", "-x", "-C", str(STAGE)], input=archive, check=True)
    else:
        shutil.copytree(ROOT / ".claude-plugin", STAGE / ".claude-plugin")
        shutil.copytree(ROOT / "skills", STAGE / "skills", ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "node_modules", ".DS_Store"))
    (STAGE / "evals").mkdir()
    for d in sorted((ROOT / "evals").iterdir()):
        if d.is_dir() and d.name not in SKIP and (d / "prompt.md").exists():
            shutil.copytree(d, STAGE / "evals" / d.name)
    return sum(1 for _ in STAGE.rglob("*"))


def summary(agg, args):
    cases = []
    for c in agg.get("cases", []):
        a = c.get("aggregates", {})
        arms = c.get("arms", {})
        with_runs, without = arms.get("with", []), arms.get("without", [])
        def mean(runs):
            s = [r.get("score") for r in runs if isinstance(r.get("score"), (int, float))]
            return round(sum(s) / len(s), 3) if s else None
        cases.append({"name": c.get("name"), "score": a.get("score"), "without": mean(without), "delta": a.get("delta"),
                      "runs": len(with_runs), "errors": [r.get("error") for r in with_runs + without if r.get("error")]})
    g = agg.get("aggregates", {})
    return {"kind": "agent", "date": datetime.date.today().isoformat(),
            "commit": subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip(),
            "skillsRef": args.ref or "working tree", "label": args.label, "model": args.model, "judgeModel": args.judge_model, "runsPerArm": args.runs, "claudeVersion": agg.get("claudeVersion"),
            "overallScore": g.get("overallScore"), "meanDelta": g.get("meanDelta"), "casesPassed": g.get("casesPassed"),
            "casesTotal": g.get("casesTotal"), "costUsd": agg.get("costUsd"), "durationSeconds": agg.get("durationSeconds"),
            "partial": agg.get("partial", False), "cases": cases}


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--case", help="case name glob")
    ap.add_argument("--tag", help="only cases with this tag")
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--model", default="sonnet")
    ap.add_argument("--judge-model", default="haiku")
    ap.add_argument("--ablation", default="with-without", choices=["with-without", "none"])
    ap.add_argument("--max-cost-usd", default="15")
    ap.add_argument("-j", "--concurrency", default="2")
    ap.add_argument("--save", action="store_true", help="write the summary into evals/agent/")
    ap.add_argument("--ref", help="stage the skills from this git commit instead of the working tree")
    ap.add_argument("--label", help="a name for this run in the saved summary, such as before or after")
    a = ap.parse_args()
    n = stage(a.ref)
    print(f"staged the plugin and {len(list((STAGE / 'evals').iterdir()))} cases in {STAGE.relative_to(ROOT)} ({n} entries)")
    res = STAGE / "evals" / "results" / "last.json"
    cmd = ["claude", "plugin", "eval", str(STAGE), "--trust-plugin", "--scaffold", "--no-publish", "--allow-tools", "Bash", "Write", "Edit",
           "--model", a.model, "--judge-model", a.judge_model, "--runs", str(a.runs), "--ablation", a.ablation,
           "--max-cost-usd", a.max_cost_usd, "-j", a.concurrency, "--threshold", "0", "--json", str(res)]
    if a.case:
        cmd += ["--case", a.case]
    if a.tag:
        cmd += ["--tag", a.tag]
    p = subprocess.run(cmd)
    if not res.exists():
        sys.exit(p.returncode or 1)
    s = summary(json.loads(res.read_text()), a)
    for c in s["cases"]:
        d = c["delta"]
        print(f"{c['name']:24} with {c['score']}  without {c['without']}  Δ {d if d is not None else '-'}" + (f"  errors: {c['errors']}" if c["errors"] else ""))
    print(f"overall {s['overallScore']}  mean Δ {s['meanDelta']}  cost ${s['costUsd']}")
    if a.save:
        (OUT / "results").mkdir(parents=True, exist_ok=True)
        name = f"{s['date']}-{a.label}.json" if a.label else f"{s['date']}.json"
        (OUT / "results" / name).write_text(json.dumps(s, indent=2) + "\n")
        if not a.case and not a.tag and not a.ref:  # only a full run of today's skills becomes the published result
            (OUT / "latest.json").write_text(json.dumps(s, indent=2) + "\n")
    sys.exit(p.returncode)


if __name__ == "__main__":
    main()
