#!/usr/bin/env python3
"""Offline Markdown link check: every relative link in a .md file must point to a file or folder that exists.

  python3 tools/check_links.py            check every Markdown file in the repo
  python3 tools/check_links.py docs *.md  check only these files or folders

Web links (http, https, mailto) are skipped, so it needs no network. Anchors (#section) are ignored.
Exits 1 if any link is broken.
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "node_modules", "__pycache__", "last30days-raw", "dist"}  # dist: build output, git-ignored
SITE_DOCS = ROOT / "site" / "docs"
SITE_ROUTES = {"/", "/showcase/", "/llms.txt", "/llms-full.txt", "/sitemap.xml", "/robots.txt"}  # made by site/build.py
LINK = re.compile(r"(?<!\!)\[[^\]\n]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)|!\[[^\]\n]*\]\(([^)\s]+)\)")
FENCE = re.compile(r"^\s*(```|~~~)")


def md_files(args):
    targets = [ROOT / a for a in args] or [ROOT]
    for t in targets:
        if t.is_file() and t.suffix == ".md":
            yield t
        elif t.is_dir():
            for p in sorted(t.rglob("*.md")):
                if not SKIP_DIRS & set(p.relative_to(ROOT).parts):
                    yield p


def links(path):
    in_fence = False
    for n, line in enumerate(path.read_text(errors="replace").splitlines(), 1):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        line = re.sub(r"`[^`]*`", "", line)  # ignore inline code
        for m in LINK.finditer(line):
            yield n, m.group(1) or m.group(2)


def site_route(rel):
    """The website's docs link by address: /docs/<page>/ is site/docs/<page>.md, and /docs/ is index.md."""
    if rel in SITE_ROUTES:
        return ROOT / "site" / "build.py"
    m = re.fullmatch(r"/docs/(?:([a-z0-9-]+)/)?", rel)
    return SITE_DOCS / f"{m.group(1) or 'index'}.md" if m else ROOT / "site" / "missing"


def main(args):
    broken, checked = [], 0
    for p in md_files(args):
        for n, target in links(p):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I) or target.startswith("#"):
                continue
            rel = target.split("#", 1)[0].split("?", 1)[0]
            if not rel:
                continue
            if rel.startswith("/") and p.is_relative_to(SITE_DOCS):
                dest = site_route(rel)
            else:
                dest = (ROOT / rel.lstrip("/")) if rel.startswith("/") else (p.parent / rel)
            checked += 1
            if not dest.exists():
                broken.append(f"{p.relative_to(ROOT)}:{n}: {target}")
    print("\n".join(broken))
    print(f"{checked} relative links checked, {len(broken)} broken")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
