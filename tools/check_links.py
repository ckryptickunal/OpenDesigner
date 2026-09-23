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
SKIP_DIRS = {".git", "node_modules", "__pycache__", "last30days-raw"}
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


def main(args):
    broken, checked = [], 0
    for p in md_files(args):
        for n, target in links(p):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I) or target.startswith("#"):
                continue
            rel = target.split("#", 1)[0].split("?", 1)[0]
            if not rel:
                continue
            dest = (ROOT / rel.lstrip("/")) if rel.startswith("/") else (p.parent / rel)
            checked += 1
            if not dest.exists():
                broken.append(f"{p.relative_to(ROOT)}:{n}: {target}")
    print("\n".join(broken))
    print(f"{checked} relative links checked, {len(broken)} broken")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
