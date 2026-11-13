#!/usr/bin/env python3
"""The automatic half of the release growth routine (docs/GROWTH-ROUTINE.md).

Checks the built website and the README, read-only and offline:
  1. search.py audit on site/dist (robots, sitemap, canonicals, titles, h1, JSON-LD, llms.txt against the pages)
  2. robots.txt lets every search and answer engine in (training bots are the owner's choice and are only listed)
  3. the sitemap and the built pages match, both ways
  4. llms.txt and llms-full.txt exist, every docs page is in llms-full.txt, and the questions section is there
  5. README facts match the repo: the version, the number of library parts and the number of skills
Then it prints the steps that need a person: the answer-engine probe and its trend row, and the live checks.

  python3 tools/growth_check.py            check the existing build in site/dist
  python3 tools/growth_check.py --build    build the site first (about a minute)

Exit code 1 when a check fails. Warnings never fail it.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SEARCH = ROOT / "skills/opendesigner-search/scripts/search.py"
# Bots that put the site in search results or answers. Blocking one of them hides the site from that engine.
MUST_ALLOW = ["Googlebot", "Bingbot", "OAI-SearchBot", "ChatGPT-User", "PerplexityBot", "Perplexity-User",
              "Claude-SearchBot", "Claude-User", "Applebot"]
NUMBER_WORDS = {w: i for i, w in enumerate("zero one two three four five six seven eight nine ten eleven twelve".split())}


def robots_blocked(robots_text):
    """The must-allow bots that robots.txt shuts out of the whole site, by the group that names them (or '*')."""
    groups, agents, rules = {}, [], []
    for raw in robots_text.splitlines() + ["user-agent: __end__"]:
        line = raw.split("#", 1)[0].strip()
        if not line or ":" not in line:
            continue
        key, val = (x.strip() for x in line.split(":", 1))
        key = key.lower()
        if key == "user-agent":
            if rules:
                for a in agents:
                    groups[a.lower()] = rules
                agents, rules = [], []
            agents.append(val)
        elif key in ("allow", "disallow"):
            rules.append((key, val))
    blocked = []
    for bot in MUST_ALLOW:
        rs = groups.get(bot.lower(), groups.get("*", []))
        if ("disallow", "/") in rs and ("allow", "/") not in rs:
            blocked.append(bot)
    return blocked


def built_pages(dist):
    """Paths of indexable built pages: an HTML document (not a fragment) without a noindex robots meta."""
    out = set()
    for f in dist.rglob("index.html"):
        html = f.read_text(errors="ignore")
        if "<html" not in html[:2000].lower() or re.search(r'<meta[^>]+name="robots"[^>]+noindex', html):
            continue
        rel = f.parent.relative_to(dist).as_posix()
        out.add("/" if rel == "." else f"/{rel}/")
    return out


def sitemap_paths(dist, base):
    xml = (dist / "sitemap.xml").read_text()
    return {u.replace(base.rstrip("/"), "", 1) or "/" for u in re.findall(r"<loc>([^<]+)</loc>", xml)}


def readme_facts(readme, version, parts, skills):
    """Each README fact that disagrees with the repo, as a sentence."""
    bad = []
    for v in re.findall(r"Version (\d+\.\d+\.\d+)", readme):
        if v != version:
            bad.append(f"README says version {v}; the engine says {version}")
    for n in re.findall(r"(\d+) ready-made parts", readme):
        if int(n) != parts:
            bad.append(f"README says {n} ready-made parts; the library has {parts}")
    for w in re.findall(r"\bthe (\w+) skill folders", readme):
        n = NUMBER_WORDS.get(w.lower(), int(w) if w.isdigit() else None)
        if n is not None and n != skills:
            bad.append(f"README says the {w} skill folders; the repo has {skills} skills")
    for w in re.findall(r"lists the other (\w+)", readme):
        n = NUMBER_WORDS.get(w.lower(), int(w) if w.isdigit() else None)
        if n is not None and n != skills - 3:   # the README names three skill zips before "the other N"
            bad.append(f"README says 'the other {w}' skills; with {skills} skills and three named, it is {skills - 3}")
    return bad


def readme_opening_words(readme, words=("design system", "Claude Code", "Cursor", "design tokens")):
    """Category words missing from the README's first 2,000 characters of visible text: answer engines quote a repo's
    opening when they answer 'which open-source tool' questions (probe, 2026-11-13)."""
    text = re.sub(r"<[^>]+>|!\[[^\]]*\]\([^)]*\)", " ", readme)
    text = re.sub(r'alt="[^"]*"', " ", text)[:2000].lower()
    return [w for w in words if w.lower() not in text]


def run(dist, base, readme_path):
    fails, warns = [], []
    res = subprocess.run([sys.executable, str(SEARCH), "audit", str(dist), "--base", base], capture_output=True, text=True)
    head = res.stdout.splitlines()[0] if res.stdout else res.stderr.strip()
    print(f"1. search.py audit: {head}")
    m = re.search(r"(\d+) errors?, (\d+) warnings?", head)
    if not m:
        fails.append("search.py audit did not run: " + head)
    else:
        if int(m.group(1)):
            fails.append(f"search.py audit: {m.group(1)} errors (run it to see them)")
        if int(m.group(2)):
            warns.append(f"search.py audit: {m.group(2)} warnings (run it to see them)")

    blocked = robots_blocked((dist / "robots.txt").read_text()) if (dist / "robots.txt").exists() else MUST_ALLOW
    print(f"2. robots.txt: {'every search and answer bot allowed' if not blocked else 'blocks ' + ', '.join(blocked)}")
    fails += [f"robots.txt blocks {b}" for b in blocked]

    pages, mapped = built_pages(dist), sitemap_paths(dist, base) if (dist / "sitemap.xml").exists() else set()
    missing, gone = sorted(pages - mapped), sorted(mapped - pages)
    print(f"3. sitemap: {len(mapped)} addresses, {len(pages)} indexable pages; {len(missing)} not listed, {len(gone)} listed but not built")
    fails += [f"sitemap leaves out {p}" for p in missing[:10]] + [f"sitemap lists {p}, which is not built" for p in gone[:10]]

    llms, full = dist / "llms.txt", dist / "llms-full.txt"
    if not llms.exists() or not full.exists():
        fails.append("llms.txt or llms-full.txt is missing")
    else:
        lt, ft = llms.read_text(), full.read_text()
        if "## Questions people ask" not in lt:
            fails.append("llms.txt has no 'Questions people ask' section (LLMS_QUESTIONS in site/build.py)")
        absent = [p for p in sorted(pages) if p.startswith("/docs/") and p != "/docs/" and p not in ft]
        print(f"4. llms.txt {len(lt):,} characters, llms-full.txt {len(ft):,}; docs pages missing from llms-full.txt: {len(absent)}")
        fails += [f"llms-full.txt leaves out {p}" for p in absent[:10]]

    readme = readme_path.read_text()
    version = re.search(r'^OPENDESIGNER_VERSION = "([^"]+)"', (ROOT / "skills/opendesigner/scripts/engine.py").read_text(), re.M).group(1)
    parts = len([d for d in (ROOT / "skills/opendesigner/assets/library/components").iterdir() if (d / "component.html").exists()])
    skills = len([d for d in (ROOT / "skills").iterdir() if (d / "SKILL.md").exists()])
    bad = readme_facts(readme, version, parts, skills)
    print(f"5. README facts (version {version}, {parts} parts, {skills} skills): {'match' if not bad else str(len(bad)) + ' wrong'}")
    fails += bad
    warns += [f"README opening never says '{w}'; engines quote a repo's first lines" for w in readme_opening_words(readme)]
    return fails, warns


MANUAL = """
By hand (docs/GROWTH-ROUTINE.md):
  - Answer-engine probe: ask the fixed questions in ChatGPT and Perplexity, logged out; raw notes in _coordination/plans/<date>-answer-engine-probe.md; one trend row per engine in docs/GROWTH-ROUTINE.md.
  - For each question that missed us, pick the fix in skills/opendesigner-search/references/fixes.md: a title, an FAQ answer or an LLMS_QUESTIONS line.
  - Live site, one fetch per page at most: /robots.txt, /llms.txt and /sitemap.xml return 200; opendesigner.vercel.app redirects to opendesigner.dev.
  - Ask Kunal for Search Console and Bing Webmaster numbers (clicks, impressions, pages indexed) for the trend table.
  - Off-site listings and posts: proposals only, one yes from Kunal each."""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--build", action="store_true", help="run site/build.py first")
    ap.add_argument("--dist", default=str(ROOT / "site/dist"))
    a = ap.parse_args()
    if a.build:
        subprocess.run([sys.executable, str(ROOT / "site/build.py")], check=True)
    dist = Path(a.dist)
    if not (dist / "index.html").exists():
        sys.exit(f"No build in {dist}: run python3 site/build.py first, or pass --build")
    base = (ROOT / "site/site-url.txt").read_text().strip()
    fails, warns = run(dist, base, ROOT / "README.md")
    for w in warns:
        print(f"WARN  {w}")
    for f in fails:
        print(f"FAIL  {f}")
    print(MANUAL)
    print(f"\ngrowth check: {len(fails)} failed, {len(warns)} warnings")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
