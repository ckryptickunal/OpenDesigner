#!/usr/bin/env python3
"""Find weekdays that don't match their dates in a page's text ("Tue 14 Oct", "Saturday, October 17", "Ends Sat Oct 18").

  python3 brand/tools/check_dates.py <file or folder> ... [--year 2026]

Builders keep writing weekdays from the wrong year's calendar; the showcase audit found six. The year comes from a four-digit
year next to the date, within the next 60 characters or the last one in the 400 before, else from --year (default: this year). Reads .html and .md files; prints each mismatch and exits 1 if any. The year is a guess when
the page names several years, so treat each line as a candidate to check, not a verdict.
"""
import datetime as dt
import html
import pathlib
import re
import sys

DAYS = {d: i for i, d in enumerate(["mon", "tue", "wed", "thu", "fri", "sat", "sun"])}
MONTHS = {m: i + 1 for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])}
DAY = r"(?P<wd>mon|tue|wed|thu|fri|sat|sun)[a-z]*\.?,?"
MON = r"(?P<mon>jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?"
NUM = r"(?P<d>\d{1,2})(?:st|nd|rd|th)?"
YEAR = r"(?:,?\s+(?P<y>(?:19|20)\d\d))?"
PATTERNS = [re.compile(rf"\b{DAY}\s+{NUM}\s+{MON}{YEAR}", re.I),   # Tue 14 Oct 2026
            re.compile(rf"\b{DAY}\s+{MON}\s+{NUM}{YEAR}", re.I)]   # Saturday, October 17, 2026


def text_of(path):
    s = path.read_text(errors="replace")
    if path.suffix == ".html":
        s = re.sub(r"<(script|style)\b.*?</\1>", " ", s, flags=re.S | re.I)
        s = html.unescape(re.sub(r"<[^>]+>", " ", s))
    return re.sub(r"\s+", " ", s)


def check(path, year):
    found = []
    text = text_of(path)
    for pat in PATTERNS:
        for m in pat.finditer(text):
            after = re.search(r"\b((?:19|20)\d\d)\b", text[m.end():m.end() + 60])
            before = re.findall(r"\b((?:19|20)\d\d)\b", text[max(0, m.start() - 400):m.start()])
            y = int(m.group("y") or (after.group(1) if after else (before[-1] if before else year)))
            try:
                date = dt.date(y, MONTHS[m.group("mon")[:3].lower()], int(m.group("d")))
            except ValueError:
                found.append(f"{path}: \"{m.group(0)}\" is not a date")
                continue
            if date.weekday() != DAYS[m.group("wd")[:3].lower()]:
                found.append(f"{path}: \"{m.group(0).strip()}\" is a {date.strftime('%A')} in {y}")
    return found


def main(argv):
    year = dt.date.today().year
    if "--year" in argv:
        i = argv.index("--year"); year = int(argv[i + 1]); argv = argv[:i] + argv[i + 2:]
    files = []
    for a in argv or ["."]:
        p = pathlib.Path(a)
        files += [p] if p.is_file() else [f for f in p.rglob("*") if f.suffix in (".html", ".md") and "/opendesigner/" not in str(f)]
    problems = [x for f in sorted(set(files)) for x in check(f, year)]
    print("\n".join(problems) if problems else f"{len(files)} files: every weekday matches its date")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
