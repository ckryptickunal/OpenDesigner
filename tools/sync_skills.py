#!/usr/bin/env python3
"""Copy skills/ (the source of truth) into the folders each agent host scans.

    python3 tools/sync_skills.py           write .agents/skills/ and .claude/skills/
    python3 tools/sync_skills.py --check   exit 1 if either copy has drifted (for CI)

Why copies and not symlinks: symlinks break on Windows checkouts, in zip downloads and in web uploads,
and Claude Code reads only .claude/skills/ while Codex, Cursor, Copilot and Gemini CLI read
.agents/skills/ (research/L18 DC-L18-02). Only folders that exist in skills/ are managed; other skills
a contributor keeps in those folders are left alone. Standard library only.
"""
import argparse, filecmp, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "skills"
TARGETS = [ROOT / ".agents" / "skills", ROOT / ".claude" / "skills"]
IGNORE = {"__pycache__", ".DS_Store"}


def files(base):
    return {p.relative_to(base) for p in base.rglob("*")
            if p.is_file() and not (set(p.relative_to(base).parts) & IGNORE) and p.suffix != ".pyc"}


def drift(src, dst):
    a, b = files(src), files(dst) if dst.exists() else set()
    changed = [f for f in a & b if not filecmp.cmp(src / f, dst / f, shallow=False)]
    return sorted(a - b), sorted(b - a), sorted(changed)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="report drift and exit 1 if any")
    args = ap.parse_args()
    skills = sorted(p for p in SRC.iterdir() if p.is_dir() and (p / "SKILL.md").exists())
    names = {p.name for p in skills}
    bad = 0
    for target in TARGETS:
        rel = target.relative_to(ROOT)
        stale = [p for p in target.iterdir() if p.is_dir() and p.name.startswith("opendesigner")
                 and p.name not in names] if target.exists() else []
        for s in skills:
            missing, extra, changed = drift(s, target / s.name)
            if not (missing or extra or changed):
                continue
            bad += 1
            if args.check:
                for tag, lst in (("missing", missing), ("extra", extra), ("changed", changed)):
                    for f in lst:
                        print(f"{tag}: {rel}/{s.name}/{f}")
            else:
                shutil.rmtree(target / s.name, ignore_errors=True)
                shutil.copytree(s, target / s.name, ignore=shutil.ignore_patterns(*IGNORE, "*.pyc"))
                print(f"synced {rel}/{s.name}")
        for p in stale:
            bad += 1
            if args.check:
                print(f"stale: {rel}/{p.name}")
            else:
                shutil.rmtree(p)
                print(f"removed {rel}/{p.name}")
    if args.check:
        print("in sync" if not bad else f"{bad} skill copies out of date: run python3 tools/sync_skills.py")
        sys.exit(1 if bad else 0)
    if not bad:
        print("already in sync")


if __name__ == "__main__":
    main()
