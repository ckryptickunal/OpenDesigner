#!/usr/bin/env python3
"""Write the repo's GitHub numbers as four JSON files for the growth dashboard.

  python3 tools/gh_snapshot.py --out <folder>

Writes gh_repo.json (totals), gh_stars.json (new and total stars per day since the repo opened),
gh_traffic.json (views, unique visitors and clones per day; GitHub keeps 14 days) and gh_referrers.json.
Each file is {"rows": [...]}. Needs the GitHub CLI, signed in with push access (traffic needs it).
"""
import argparse
import datetime as dt
import json
import pathlib
import subprocess

REPO = "ckryptickunal/OpenDesigner"


def gh(path, accept=None, paginate=False):
    cmd = ["gh", "api"] + (["-H", f"Accept: {accept}"] if accept else []) + (["--paginate", "--slurp"] if paginate else []) + [path]
    out = json.loads(subprocess.run(cmd, capture_output=True, text=True, check=True).stdout)
    return [x for page in out for x in page] if paginate else out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True)
    out = pathlib.Path(ap.parse_args().out)
    out.mkdir(parents=True, exist_ok=True)
    taken = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    repo = gh(f"repos/{REPO}")
    per_day = {}
    for s in gh(f"repos/{REPO}/stargazers?per_page=100", "application/vnd.github.star+json", paginate=True):
        per_day[s["starred_at"][:10]] = per_day.get(s["starred_at"][:10], 0) + 1
    rows, total, day = [], 0, dt.date.fromisoformat(repo["created_at"][:10])
    while day <= dt.datetime.now(dt.timezone.utc).date():
        n = per_day.get(day.isoformat(), 0)
        total += n
        rows.append({"day": day.isoformat(), "new_stars": n, "total_stars": total})
        day += dt.timedelta(days=1)

    views = gh(f"repos/{REPO}/traffic/views")["views"]
    clones = {c["timestamp"][:10]: c for c in gh(f"repos/{REPO}/traffic/clones")["clones"]}
    traffic = [{"day": v["timestamp"][:10], "views": v["count"], "unique_visitors": v["uniques"],
                "clones": clones.get(v["timestamp"][:10], {}).get("count", 0),
                "unique_cloners": clones.get(v["timestamp"][:10], {}).get("uniques", 0)} for v in views]
    referrers = [{"referrer": r["referrer"], "views": r["count"], "unique_visitors": r["uniques"]}
                 for r in gh(f"repos/{REPO}/traffic/popular/referrers")]
    count = lambda q: gh(f"search/issues?q=repo:{REPO}+{q}")["total_count"]
    totals = {"stars": repo["stargazers_count"], "forks": repo["forks_count"], "watchers": repo["subscribers_count"],
              "open_issues": count("is:issue+is:open"), "open_prs": count("is:pr+is:open"), "merged_prs": count("is:pr+is:merged"),
              "contributors": len(gh(f"repos/{REPO}/contributors?per_page=100")), "created": repo["created_at"][:10],
              "last_push": repo["pushed_at"][:10], "taken_at": taken}

    for name, data in (("gh_repo", [totals]), ("gh_stars", rows), ("gh_traffic", traffic), ("gh_referrers", referrers)):
        (out / f"{name}.json").write_text(json.dumps({"rows": data}))
    print(f"{taken}: {totals['stars']} stars, {len(traffic)} traffic days, {len(referrers)} referrers -> {out}")


if __name__ == "__main__":
    main()
