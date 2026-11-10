#!/usr/bin/env python3
"""Zip each skill for upload to claude.ai (Customize > Skills) or the Claude API, into dist/, and the ChatGPT Project
files into one download.

    python3 tools/build_dist.py            validate frontmatter, then write dist/<skill>.zip and dist/opendesigner-chatgpt.zip
    python3 tools/build_dist.py --check    validate only (exit 1 on errors); writes nothing

Each zip holds the skill folder at its root (opendesigner.zip -> opendesigner/SKILL.md), the layout the
Claude Help Center asks for. Frontmatter is checked against the portable Agent Skills fields: name
(1-64, a-z 0-9 and hyphens, matches the folder, no "anthropic" or "claude"), description (1-1024;
warn above 200 because the claude.ai Help Center states a 200-character limit), and only license,
compatibility, metadata and allowed-tools besides. It also checks that the release the engine stamps into each system
(OPENDESIGNER_VERSION in skills/opendesigner/scripts/engine.py) equals the version in plugin.json and
.claude-plugin/plugin.json. dist/ is git-ignored. Standard library only.

opendesigner-chatgpt.zip is not a skill. It holds what a ChatGPT Project needs, so nobody fetches six files by hand: the
files of chatgpt-project/knowledge/, instructions.txt (only the part of chatgpt-project/instructions.md below its "---"
line, the text people paste) and a README.txt with the three steps.
"""
import argparse, json, re, sys, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC, DIST = ROOT / "skills", ROOT / "dist"
GPT, GPT_ZIP = ROOT / "chatgpt-project", "opendesigner-chatgpt"
ALLOWED = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
IGNORE = {"__pycache__", ".DS_Store", "node_modules", "out", ".vite"}  # the painting engine must ship without installs or renders
# claude.ai installs each uploaded skill on its own, so the sub-skills' zips carry the engine and the data it
# reads (spec 8.2). In the repo and in plugin installs they use the sibling opendesigner skill instead.
BUNDLE = {p: p for p in ("scripts/engine.py", "scripts/journey.py", "references/levers.json", "references/hooks.json",
                          "references/graph.json", "references/questions.json", "references/pacing.json",
                          "references/report.schema.json", "references/rules.md", "references/zoom.md",
                          "references/improve.md", "references/making.md", "references/audit.md", "assets/picker.js",
                          "assets/output/PROTOCOL.md")}  # engine.py imports journey.py, which reads pacing and the report schema; review.py compare inlines picker.js


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


def check_version():
    """Errors when the engine's OPENDESIGNER_VERSION differs from a manifest's version (a skill zip carries only the engine)."""
    src = (SRC / "opendesigner" / "scripts" / "engine.py").read_text(encoding="utf-8")
    m = re.search(r'^OPENDESIGNER_VERSION = "([^"]+)"$', src, re.M)
    if not m:
        return ["skills/opendesigner/scripts/engine.py has no OPENDESIGNER_VERSION line"]
    errs = []
    for manifest in ("plugin.json", ".claude-plugin/plugin.json"):
        v = json.loads((ROOT / manifest).read_text(encoding="utf-8")).get("version")
        if v != m.group(1):
            errs.append(f"{manifest} says version {v}, but engine.py stamps systems with OPENDESIGNER_VERSION {m.group(1)}. "
                        "Set both to the same release")
    return errs


def chatgpt_parts():
    """(errors, the paste text, the knowledge files) for the ChatGPT bundle. The paste text is everything below the
    first "---" line of chatgpt-project/instructions.md; the lines above it are notes for people reading the repository."""
    _notes, line, paste = (GPT / "instructions.md").read_text(encoding="utf-8").partition("\n---\n")
    files = sorted(f for f in (GPT / "knowledge").iterdir() if f.is_file() and f.name not in IGNORE)
    errs = []
    if not line or not paste.strip():
        errs.append('chatgpt-project/instructions.md has no "---" line with the text to paste below it')
    if not files:
        errs.append("chatgpt-project/knowledge/ holds no files (python3 tools/build_data.py writes them)")
    return errs, paste.strip() + "\n", files


def chatgpt_readme(files):
    return f"""OpenDesigner for ChatGPT

1. Unzip this file.
2. In ChatGPT, create a Project. Copy everything in instructions.txt and paste it into the Project's instructions.
3. Upload the {len(files)} files in the knowledge folder as Project files:
   {", ".join(f.name for f in files)}

Then start a chat in the Project and say: "Create a design system for my app."

Help with each step: https://opendesigner.dev/docs/install/
Source (MIT): https://github.com/ckryptickunal/OpenDesigner
"""


def write_chatgpt(paste, files):
    """dist/opendesigner-chatgpt.zip: one folder with README.txt, instructions.txt and knowledge/."""
    out = DIST / f"{GPT_ZIP}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(f"{GPT_ZIP}/README.txt", chatgpt_readme(files))
        z.writestr(f"{GPT_ZIP}/instructions.txt", paste)
        for f in files:
            z.write(f, Path(GPT_ZIP) / "knowledge" / f.name)
    return out


def shown(out):
    try:
        return out.relative_to(ROOT)
    except ValueError:
        return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    skills = sorted(p for p in SRC.iterdir() if (p / "SKILL.md").exists())
    version_errs = check_version()
    for e in version_errs:
        print(f"error version: {e}")
    failed = bool(version_errs)
    for s in skills:
        errs, warns = check(s)
        for w in warns:
            print(f"warn  {s.name}: {w}")
        for e in errs:
            print(f"error {s.name}: {e}")
        failed |= bool(errs)
        if errs or args.check or version_errs:
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
                # The bundled engine's `show` command reads templates relative to its skill root.
                # Sub-skill zips include the engine, so they need its templates as well.
                for template in sorted((SRC / "opendesigner" / "assets" / "templates").glob("*.html")):
                    dst = Path("assets/templates") / template.name
                    if not (s / dst).exists():
                        z.write(template, Path(s.name) / dst)
        print(f"wrote {shown(out)} ({out.stat().st_size // 1024} KB)")
    gpt_errs, paste, files = chatgpt_parts()
    for e in gpt_errs:
        print(f"error chatgpt: {e}")
    failed |= bool(gpt_errs)
    if not (gpt_errs or args.check or version_errs):
        DIST.mkdir(exist_ok=True)
        out = write_chatgpt(paste, files)
        print(f"wrote {shown(out)} ({out.stat().st_size // 1024} KB)")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
