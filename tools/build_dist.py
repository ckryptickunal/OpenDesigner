#!/usr/bin/env python3
"""Zip each skill for upload to claude.ai (Customize > Skills) or the Claude API, into dist/.

    python3 tools/build_dist.py            validate frontmatter, then write dist/<skill>.zip
    python3 tools/build_dist.py --check    validate only (exit 1 on errors)

Each zip holds the skill folder at its root (opendesigner.zip -> opendesigner/SKILL.md), the layout the
Claude Help Center asks for. Frontmatter is checked against the portable Agent Skills fields: name
(1-64, a-z 0-9 and hyphens, matches the folder, no "anthropic" or "claude"), description (1-1024;
warn above 200 because the claude.ai Help Center states a 200-character limit), and only license,
compatibility, metadata and allowed-tools besides. dist/ is git-ignored. Standard library only.
"""
import argparse, re, sys, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC, DIST = ROOT / "skills", ROOT / "dist"
ALLOWED = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
IGNORE = {"__pycache__", ".DS_Store"}
# claude.ai installs each uploaded skill on its own, so the sub-skills' zips carry the engine and the data it
# reads (spec 8.2). In the repo and in plugin installs they use the sibling opendesigner skill instead.
BUNDLE = {"scripts/engine.py": "scripts/engine.py", "references/levers.json": "references/levers.json",
          "references/hooks.json": "references/hooks.json", "references/graph.json": "references/graph.json"}


def check(skill):
    errs, warns = [], []
    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return ["no YAML frontmatter"], warns
    fm = m.group(1)
    keys = set(re.findall(r"^([A-Za-z_-]+):", fm, re.M))
    if keys - ALLOWED:
        errs.append(f"non-portable keys {sorted(keys - ALLOWED)} fail claude.ai upload")
    name = (re.search(r"^name:\s*(.+)$", fm, re.M) or [None, ""])[1].strip()
    desc = (re.search(r"^description:\s*(.+)$", fm, re.M) or [None, ""])[1].strip()
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
        errs.append(f"bad name {name!r}")
    if name != skill.name:
        errs.append(f"name {name!r} does not match folder {skill.name!r}")
    if "anthropic" in name or "claude" in name:
        errs.append("name may not contain 'anthropic' or 'claude'")
    if not 1 <= len(desc) <= 1024:
        errs.append(f"description length {len(desc)} (1-1024)")
    elif len(desc) > 200:
        warns.append(f"description is {len(desc)} chars; claude.ai may reject over 200")
    if re.search(r"<[a-zA-Z/]", name + desc):
        errs.append("XML-like tags in name or description")
    lines = text.count("\n")
    if lines > 500:
        warns.append(f"SKILL.md is {lines} lines (guidance: under 500)")
    return errs, warns


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    skills = sorted(p for p in SRC.iterdir() if (p / "SKILL.md").exists())
    failed = False
    for s in skills:
        errs, warns = check(s)
        for w in warns:
            print(f"warn  {s.name}: {w}")
        for e in errs:
            print(f"error {s.name}: {e}")
        failed |= bool(errs)
        if errs or args.check:
            continue
        DIST.mkdir(exist_ok=True)
        out = DIST / f"{s.name}.zip"
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(s.rglob("*")):
                rel = f.relative_to(s)
                if f.is_file() and not (set(rel.parts) & IGNORE) and f.suffix != ".pyc":
                    z.write(f, Path(s.name) / rel)
            if s.name != "opendesigner":
                for src, dst in BUNDLE.items():
                    if (SRC / "opendesigner" / src).exists() and not (s / dst).exists():
                        z.write(SRC / "opendesigner" / src, Path(s.name) / dst)
        print(f"wrote {out.relative_to(ROOT)} ({out.stat().st_size // 1024} KB)")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
