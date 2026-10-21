#!/usr/bin/env python3
"""Run every automatic check of the post-change audit (skills/opendesigner/references/post-change-audit.md, section A) and
print one table: passed or failed, with the line that says why. Then walk section B by eye.

  python3 site/post_change_audit.py [--base http://localhost:4173] [--dist site/dist] [--quick]

Builds nothing: build first (python3 site/build.py, or with SITE_DIST) and serve the build at --base. --quick checks only the
library pages, the home page and one docs page instead of every page. Needs Playwright and Chrome. Exits 1 if any check fails.
"""
import argparse
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def run(name, cmd, ok):
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip().splitlines()
    last = next((l for l in reversed(out) if l.strip()), "")
    passed = ok(r.returncode, "\n".join(out))
    note = ""
    if not passed:  # keep the whole report of a failed check, so nobody has to run it again to read it
        log = ROOT / "site/.cache/audit" / (re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") + ".txt")
        log.parent.mkdir(parents=True, exist_ok=True); log.write_text("\n".join(out) + "\n")
        note = f"  (full report: {log.relative_to(ROOT)})"
    print(f"{'PASS' if passed else 'FAIL'}  {name:<34} {last[:110]}{note}")
    return passed


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", default="http://localhost:4173")
    ap.add_argument("--dist", default=str(ROOT / "site/dist"))
    ap.add_argument("--quick", action="store_true")
    a = ap.parse_args()
    py = sys.executable
    pages = sorted({re.sub(r"^https?://[^/]+", "", u) for u in re.findall(r"<loc>([^<]+)</loc>", (pathlib.Path(a.dist) / "sitemap.xml").read_text())})
    if a.quick:
        pages = [p for p in pages if p.startswith("/library/")][:8] + ["/", "/docs/install/", "/library/"]
    zero = lambda code, out: code == 0
    results = [
        run("links, titles, structured data", [py, "site/check.py", a.dist], lambda c, o: "no problems" in o),
        run("same header and footer everywhere", [py, "site/check_chrome.py", "--base", a.base, "--dist", a.dist, "--widths", "390,768,1024,1440"], zero),
        run("layout at 13 widths (incl. corners)", [py, "site/check_layout.py", "--base", a.base, "--pages", ",".join(pages), "--errors-only"], zero),
        run("library components (rules)", [py, "skills/opendesigner/scripts/library.py", "check"], zero),
        run("library components unscaled", [py, "site/library_layout.py", "--errors-only"], zero),
        run("skill copies in sync", [py, "tools/sync_skills.py", "--check"], zero),
        run("generated knowledge current", [py, "tools/build_data.py", "--check"], zero),
    ]
    n = sum(results)
    print(f"\n{n} of {len(results)} automatic checks passed. Now walk section B of skills/opendesigner/references/post-change-audit.md by eye.")
    return 0 if n == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
