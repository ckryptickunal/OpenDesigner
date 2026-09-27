#!/usr/bin/env python3
"""Find living documents whose facts have changed since they were last updated.

    python3 tools/living_docs.py            report drift; exit 1 if any fact changed or a check failed
    python3 tools/living_docs.py --accept   store the current facts, after the documents are updated

Some documents state facts that change on their own: star counts, whether CI runs, the state of issues they
cite, package versions in benchmarks, the open pull requests. This tool reads those facts live (GitHub via the
`gh` CLI, npm over HTTPS) and compares them with `_coordination/living-docs.json`. For every changed fact it
names the documents to revisit. Update the documents first, then run --accept. Never accept without updating.
Standard library plus `gh`. Tools may use the network; skills may not.
"""
import argparse, json, re, subprocess, sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT = ROOT / "_coordination" / "living-docs.json"
REPO = "ckryptickunal/OpenDesigner"
PLAN, SKILL = "docs/FIELD-PLAN.md", ".claude/skills/od-pr-review/SKILL.md"
LOG, MATRIX, SETTINGS = "_coordination/PR-RESOLUTION-LOG.md", "benchmarks/L09-benchmark-matrix.md", "docs/GITHUB-SETTINGS.md"


def gh(*args):
    r = subprocess.run(["gh", *args], capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(r.stderr.strip() or "gh failed")
    return r.stdout.strip()


def npm(pkg):
    with urllib.request.urlopen(f"https://registry.npmjs.org/{pkg}", timeout=20) as r:
        d = json.load(r)
    latest = d["dist-tags"]["latest"]
    return {"latest": latest, "deprecated": bool(d["versions"][latest].get("deprecated"))}


def facts():
    """Yield (fact id, documents that depend on it, function returning the live value)."""
    yield "repo.stars", [PLAN, SETTINGS], lambda: int(gh("api", f"repos/{REPO}", "-q", ".stargazers_count"))
    yield "repo.ci_has_runs", [PLAN, SKILL, SETTINGS], lambda: gh("run", "list", "-R", REPO, "-L", "1", "--json", "databaseId", "-q", "length") != "0"
    yield "repo.open_prs", [LOG], lambda: sorted(int(n) for n in gh("pr", "list", "-R", REPO, "--state", "open", "--json", "number", "-q", ".[].number").split())
    plan = (ROOT / PLAN).read_text(encoding="utf-8") if (ROOT / PLAN).exists() else ""
    for owner, repo, kind, num in sorted(set(re.findall(r"github\.com/([\w.-]+)/([\w.-]+)/(issues|discussions)/(\d+)", plan))):
        if kind == "issues":
            get = lambda o=owner, r=repo, n=num: gh("api", f"repos/{o}/{r}/issues/{n}", "-q", ".state")
        else:
            q = f'query{{repository(owner:"{owner}",name:"{repo}"){{discussion(number:{num}){{closed}}}}}}'
            get = lambda q=q: "closed" if gh("api", "graphql", "-f", f"query={q}", "-q", ".data.repository.discussion.closed") == "true" else "open"
        yield f"{owner}/{repo}#{num}", [PLAN], get
    matrix = (ROOT / MATRIX).read_text(encoding="utf-8")
    ext = matrix.split("### Extended systems", 1)[1].split("\n## ", 1)[0] if "### Extended systems" in matrix else ""
    for pkg, version in re.findall(r"`(@[\w.-]+/[\w.-]+)` (\d[\w.-]*)", ext):
        yield f"npm:{pkg}", [MATRIX, f"benchmarks/systems/ (the {pkg} teardown, snapshot {version})"], lambda p=pkg: npm(p)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--accept", action="store_true", help="store current facts as the new baseline")
    args = ap.parse_args()
    old = json.loads(SNAPSHOT.read_text()) if SNAPSHOT.exists() else {}
    new, drift, failed = {}, [], []
    for fid, docs, get in facts():
        try:
            new[fid] = get()
        except Exception as e:  # report and keep going; one dead source should not hide the rest
            failed.append(f"{fid}: {e}")
            if fid in old:
                new[fid] = old[fid]
            continue
        if fid in old and old[fid] != new[fid]:
            drift.append((fid, old[fid], new[fid], docs))
        elif fid not in old and old:
            drift.append((fid, None, new[fid], docs))
    for fid, was, now, docs in drift:
        print(f"CHANGED {fid}: {was} -> {now}\n        revisit: {', '.join(docs)}")
    for f in failed:
        print(f"FAILED  {f}")
    if args.accept:
        SNAPSHOT.write_text(json.dumps(new, indent=2, sort_keys=True) + "\n")
        print(f"stored {len(new)} facts in {SNAPSHOT.relative_to(ROOT)}")
        return
    print(f"{len(new)} facts checked, {len(drift)} changed, {len(failed)} failed")
    sys.exit(1 if drift or failed else 0)


if __name__ == "__main__":
    main()
