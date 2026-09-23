#!/usr/bin/env python3
"""Reading level of OpenDesigner's user-facing text (for the plain-language pass, lane U4).

  python3 tools/readability.py                 report every user-facing file
  python3 tools/readability.py --json out.json also save the numbers (for before/after comparison)
  python3 tools/readability.py README.md ...   report specific files

Measures prose only: code blocks, inline code, tables, links' URLs, HTML tags and front matter are skipped.
Grade is the Flesch-Kincaid estimate from tools/check_glossary.py.
"""
import json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_glossary import grade, words  # same formula as the glossary checker

ROOT = Path(__file__).resolve().parent.parent
USER_FACING = ["README.md", "AGENTS.md", "docs/*.md", "skills/*/SKILL.md", "skills/opendesigner/references/*.md",
               "skills/opendesigner/references/stages/*.md", "skills/opendesigner/assets/output/*.md",
               "skills/opendesigner/assets/templates/*.html", "chatgpt-project/*.md"]
SKIP = {"docs/GLOSSARY.md"}  # generated, checked by check_glossary.py
LONG = 25  # words; sentences longer than this are hard to follow
MIN_SENTENCES = 5  # fewer than this is too little text for a meaningful grade


def prose(text):
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)       # front matter
    text = re.sub(r"```.*?```", " ", text, flags=re.S)              # code blocks
    text = re.sub(r"<script.*?</script>|<style.*?</style>", " ", text, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)                             # HTML tags
    text = re.sub(r"`[^`]*`", " ", text)                             # inline code
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)             # keep link text
    lines = [l for l in text.splitlines() if not l.strip().startswith("|") and not l.strip().startswith("#")]
    return "\n".join(lines)


def sentences(text):
    parts = re.split(r"(?<=[.!?])\s+|\n\s*[-*]\s+|\n{2,}", text)
    return [p.strip() for p in parts if len(words(p)) >= 3]


def measure(path):
    ss = sentences(prose(path.read_text(errors="replace")))
    if not ss:
        return None
    grades = [grade(s) for s in ss]
    lengths = [len(words(s)) for s in ss]
    return dict(file=str(path.relative_to(ROOT)), sentences=len(ss), words=sum(lengths),
                grade=round(sum(grades) / len(grades), 1), avg_words=round(sum(lengths) / len(lengths), 1),
                long=sum(1 for n in lengths if n > LONG))


def main(argv):
    save = None
    if "--json" in argv:
        i = argv.index("--json"); save = argv[i + 1]; argv = argv[:i] + argv[i + 2:]
    paths = [ROOT / a for a in argv] if argv else sorted({p for g in USER_FACING for p in ROOT.glob(g)})
    measured = [r for p in paths if str(p.relative_to(ROOT)) not in SKIP and (r := measure(p))]
    rows = [r for r in measured if r["sentences"] >= MIN_SENTENCES]
    tiny = [r["file"] for r in measured if r["sentences"] < MIN_SENTENCES]
    print(f"{'grade':>5} {'avg words':>9} {'long':>5} {'sentences':>9}  file")
    for r in sorted(rows, key=lambda r: -r["grade"]):
        print(f"{r['grade']:>5} {r['avg_words']:>9} {r['long']:>5} {r['sentences']:>9}  {r['file']}")
    total = sum(r["sentences"] for r in rows) or 1
    mean = sum(r["grade"] * r["sentences"] for r in rows) / total
    print(f"\n{len(rows)} files, {total} sentences, weighted mean grade {mean:.1f}, "
          f"{sum(r['long'] for r in rows)} sentences over {LONG} words")
    if tiny:
        print(f"Too little prose to grade ({len(tiny)}): " + ", ".join(tiny))
    if save:
        Path(save).write_text(json.dumps(rows, indent=1))


if __name__ == "__main__":
    main(sys.argv[1:])
