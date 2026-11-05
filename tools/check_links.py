#!/usr/bin/env python3
"""Offline Markdown link check: every relative link in a .md file must point to a file or folder that exists.

  python3 tools/check_links.py            check every Markdown file in the repo
  python3 tools/check_links.py docs *.md  check only these files or folders

Web links (http, https, mailto) are skipped, so it needs no network. Anchors (#section) are ignored.
A link that starts with / in site/docs/*.md is an address on the website, not a file: it must be a page site/build.py
makes (site/build.py page_paths), that page's Markdown copy (index.md) or a file the build writes at the root. A link to an
old address that only redirects is reported too, with the address to use.
Exits 1 if any link is broken.
"""
import importlib.util, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "node_modules", "__pycache__", "last30days-raw", "dist"}  # dist: build output, git-ignored
SITE_DOCS = ROOT / "site" / "docs"
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


_SITE = {}


def site():
    """The website's addresses, read from site/build.py: (routes, redirects). Loaded once, offline."""
    if not _SITE:
        spec = importlib.util.spec_from_file_location("od_site_build", ROOT / "site" / "build.py")
        build = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(build)
        pages = build.page_paths(build.load_docs())
        files = set()
        for src in ("build.py", "library_page.py", "tour_page.py"):  # what the build writes at the root: DIST / "llms.txt" ...
            files |= {"/" + f for f in re.findall(r'DIST / "([^"{}]+)"', (ROOT / "site" / src).read_text())
                      if re.fullmatch(r"[\w/-]+\.\w+", f)}
        _SITE.update(routes=set(pages) | {p + "index.md" for p in pages} | files, redirects=dict(build.REDIRECTS))
    return _SITE["routes"], _SITE["redirects"]


def site_link(rel):
    """None when the website serves this address as a page or file; otherwise what is wrong."""
    routes, redirects = site()
    if rel in routes:
        return None
    if rel in redirects:
        return f"redirects to {redirects[rel]}; link there"
    if rel + "/" in routes:
        return f"missing its trailing slash: {rel}/"
    return "no page or file on the website at this address (site/build.py makes none)"


def main(args):
    broken, checked = [], 0
    for p in md_files(args):
        for n, target in links(p):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I) or target.startswith("#"):
                continue
            rel = target.split("#", 1)[0].split("?", 1)[0]
            if not rel:
                continue
            checked += 1
            if rel.startswith("/") and p.is_relative_to(SITE_DOCS):
                why = site_link(rel)
                if why:
                    broken.append(f"{p.relative_to(ROOT)}:{n}: {target} ({why})")
                continue
            dest = (ROOT / rel.lstrip("/")) if rel.startswith("/") else (p.parent / rel)
            if not dest.exists():
                broken.append(f"{p.relative_to(ROOT)}:{n}: {target}")
    print("\n".join(broken))
    print(f"{checked} relative links checked, {len(broken)} broken")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
