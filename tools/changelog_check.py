#!/usr/bin/env python3
"""Check that CHANGELOG.md stays short and dated, the way the website's changelog page reads it.

Every top-level entry must look like
    - **Short title** (2026-11-01). One to three plain sentences.
with a title of at most 70 characters, the date it landed on main, and at most 400 characters after the title.
Sub-points are allowed but discouraged: at most 3 per entry, each at most 200 characters.

    python3 tools/changelog_check.py            report problems, exit 1 if any
    python3 tools/changelog_check.py --latest   also check that the newest commit's day on main has an entry

Standard library only, no network.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TITLE_MAX, BODY_MAX, SUB_MAX, SUBS_MAX = 70, 400, 200, 3
ENTRY = re.compile(r"^- \*\*(.+?)\*\* \((\d{4}-\d{2}-\d{2})\)\. (.+)$")


def check(text):
    problems, entries, subs, current = [], [], 0, None
    for n, line in enumerate(text.splitlines(), 1):
        if line.startswith("- "):
            subs, m = 0, ENTRY.match(line)
            if not m:
                problems.append(f"line {n}: write it as `- **Title** (YYYY-MM-DD). Sentences.`: {line[:80]}")
                current = None
                continue
            title, day, body = m.groups()
            current = title
            entries.append(day)
            if len(title) > TITLE_MAX:
                problems.append(f"line {n}: title is {len(title)} characters (at most {TITLE_MAX}): {title}")
            if len(body) > BODY_MAX:
                problems.append(f"line {n}: \"{title}\" is {len(body)} characters (at most {BODY_MAX}); put the detail in the commit or PR")
        elif re.match(r"^\s+- ", line) and current:
            subs += 1
            if subs > SUBS_MAX:
                problems.append(f"line {n}: \"{current}\" has more than {SUBS_MAX} sub-points; fold them into one or two sentences")
            if len(line.strip()) > SUB_MAX:
                problems.append(f"line {n}: sub-point is {len(line.strip())} characters (at most {SUB_MAX})")
    return problems, entries


def main():
    problems, days = check((ROOT / "CHANGELOG.md").read_text(encoding="utf-8"))
    if "--latest" in sys.argv[1:]:
        r = subprocess.run(["git", "log", "-1", "--first-parent", "--format=%cs", "HEAD"], cwd=ROOT, capture_output=True, text=True)
        latest = r.stdout.strip()
        if latest and latest not in days:
            problems.append(f"no entry dated {latest}, the day of the newest commit; add one per change that day")
    for p in problems:
        print(p)
    print(f"CHANGELOG.md: {len(days)} entries, {len(problems)} problem{'s' if len(problems) != 1 else ''}")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
