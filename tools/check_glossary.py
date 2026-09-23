#!/usr/bin/env python3
"""Check and build the three-voice glossary (plain, designer, engineer).

  python3 tools/check_glossary.py synthesis/glossary/shard-a.json   check one shard while writing it
  python3 tools/check_glossary.py --build                          merge shards, check coverage, write
                                                                   synthesis/glossary.json and docs/GLOSSARY.md
Exit code 1 when any error is found.
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
G = ROOT / "synthesis/glossary"
LIMITS = {"plain": 20, "designer": 30, "engineer": 30, "example": 15, "designer_says": 8, "code_name": 8}
MAX_GRADE = 9          # per-entry ceiling for the plain voice (Flesch-Kincaid grade)
MAX_MEAN_GRADE = 6.0   # the plain voice as a whole reads at grade 6 or lower (U1 spec)
# Words a school student would not know. The plain voice explains the idea instead of naming it.
JARGON = {"token", "tokens", "primitive", "semantic", "alias", "schema", "variable", "variables", "chroma", "hue",
          "kerning", "tracking", "affordance", "heuristic", "heuristics", "parameter", "parameters", "metadata",
          "ontology", "taxonomy", "hierarchy", "modular", "ratio", "algorithm", "syntax", "render", "rendered",
          "responsive", "viewport", "breakpoint", "breakpoints", "opacity", "elevation", "gestalt", "cognitive"}
ACRONYM_OK = {"OK", "TV", "AI", "UI"}
LAYER_ORDER = ["core", "use", "dials", "ctx", "prin", "found", "tok", "comp", "pat", "guard", "deliver", "gov", "builder"]
LAYER_NAMES = {"core": "Everyday terms", "use": "Using OpenDesigner", "dials": "The eight dials", "ctx": "Context and inputs", "prin": "Principles",
               "found": "Foundations", "tok": "Tokens", "comp": "Components", "pat": "Patterns and templates",
               "guard": "Guardrails and validation", "deliver": "Delivery and tooling",
               "gov": "Governance, docs and adoption", "builder": "How OpenDesigner works"}


def words(text):
    return re.findall(r"[A-Za-z][A-Za-z'-]*|\d+(?:[.,]\d+)?", text)


def syllables(word):
    w = word.lower().strip("'")
    if w.isdigit():
        return 1
    groups = re.findall(r"[aeiouy]+", w)
    n = len(groups) - (1 if w.endswith("e") and not w.endswith(("le", "ee")) and len(groups) > 1 else 0)
    return max(1, n)


def grade(text):
    ws = words(text)
    sentences = max(1, len(re.findall(r"[.!?](\s|$)", text)))
    if not ws:
        return 0.0
    return 0.39 * len(ws) / sentences + 11.8 * sum(syllables(w) for w in ws) / len(ws) - 15.59


def check_entries(entries, label):
    errors, warnings, grades = [], [], []
    seen = set()
    for e in entries:
        tag = f"{label}:{e.get('id', '?')}"
        for field in ("id", "term", "plain", "designer", "engineer", "source"):
            if not e.get(field):
                errors.append(f"{tag} missing {field}")
        if e.get("id") in seen:
            errors.append(f"{tag} duplicate id")
        seen.add(e.get("id"))
        for field, limit in LIMITS.items():
            n = len(words(e.get(field, "")))
            if n > limit:
                errors.append(f"{tag} {field} has {n} words (limit {limit})")
        plain = e.get("plain", "")
        acr = sorted({a for a in re.findall(r"\b[A-Z]{2,}\b", plain) if a not in ACRONYM_OK})
        if acr:
            errors.append(f"{tag} plain voice uses acronyms {acr}")
        jar = sorted({w.lower() for w in words(plain)} & JARGON)
        if jar:
            errors.append(f"{tag} plain voice uses jargon {jar}")
        if plain and (plain == e.get("designer") or plain == e.get("engineer")):
            errors.append(f"{tag} voices must differ")
        if plain:
            g = grade(plain)
            grades.append(g)
            if g > MAX_GRADE:
                errors.append(f"{tag} plain voice reads at grade {g:.1f} (max {MAX_GRADE})")
    if grades and sum(grades) / len(grades) > MAX_MEAN_GRADE:
        errors.append(f"{label}: plain voice averages grade {sum(grades)/len(grades):.1f} (max {MAX_MEAN_GRADE})")
    return errors, warnings, grades


def build():
    inputs = json.loads((G / "terms-input.json").read_text())
    merged = {}
    for shard in sorted(G.glob("shard-*.json")):
        for e in json.loads(shard.read_text()):
            merged[e["id"]] = e
    missing = [t["id"] for t in inputs if t["id"] not in merged]
    extra = [i for i in merged if i not in {t["id"] for t in inputs}]
    layer = {t["id"]: t["layer"] for t in inputs}
    ordered = sorted(merged.values(), key=lambda e: (LAYER_ORDER.index(layer.get(e["id"], "builder")), e["id"]))
    for e in ordered:
        e["layer"] = layer.get(e["id"], "builder")
        if "aka" in e:  # writers may use either name; ship one
            e["aliases"] = e.pop("aka")
    errors, _, grades = check_entries(ordered, "glossary")
    errors += [f"missing term {m}" for m in missing] + [f"term not in terms-input.json {x}" for x in extra]
    (ROOT / "synthesis/glossary.json").write_text(json.dumps(ordered, indent=1, ensure_ascii=False) + "\n")
    write_markdown(ordered)
    mean = sum(grades) / len(grades) if grades else 0
    print(f"{len(ordered)} terms, {len(missing)} missing, plain voice mean grade {mean:.1f}")
    return errors


def write_markdown(entries):
    out = ["# Glossary", "",
           "Every term OpenDesigner uses, said three ways. Read the one that fits you.", "",
           "- **Plain**: anyone can follow it, no design or coding background needed.",
           "- **Designer**: the words designers use, and what it does to the look and feel.",
           "- **Engineer**: how it is built: token names, formats, code.", "",
           "Generated from `synthesis/glossary.json` by `python3 tools/check_glossary.py --build`. Edit the JSON, not this file.", ""]
    present = [l for l in LAYER_ORDER if any(e["layer"] == l for e in entries)]
    out += ["**Sections:** " + " · ".join(f"[{LAYER_NAMES[l]}](#{LAYER_NAMES[l].lower().replace(',', '').replace(' ', '-')})" for l in present), ""]
    for l in present:
        out += [f"## {LAYER_NAMES[l]}", ""]
        for e in (e for e in entries if e["layer"] == l):
            short = " · ".join(x for x in (f"Designers: {e['designer_says']}" if e.get("designer_says") else "",
                                             f"Code: `{e['code_name']}`" if e.get("code_name") else "") if x)
            out += [f"### {e['term']}", "", e["plain"] + (f"  \n{short}" if short else ""), "",
                    f"<details><summary>Designer and engineer</summary>", "",
                    f"**Designer:** {e['designer']}", "", f"**Engineer:** {e['engineer']}", "",
                    *( [f"**Example:** {e['example']}", ""] if e.get("example") else [] ),
                    *( [f"**Also called:** {', '.join(e.get('aliases') or e.get('aka'))}", ""] if (e.get('aliases') or e.get('aka')) else [] ),
                    "</details>", ""]
    (ROOT / "docs").mkdir(exist_ok=True)
    (ROOT / "docs/GLOSSARY.md").write_text("\n".join(out))


if __name__ == "__main__":
    if sys.argv[1:] == ["--build"]:
        errs = build()
    else:
        errs = []
        for path in sys.argv[1:]:
            e, _, g = check_entries(json.loads(Path(path).read_text()), Path(path).stem)
            errs += e
            if g:
                print(f"{path}: {len(g)} entries, plain voice mean grade {sum(g)/len(g):.1f}")
    for e in errs:
        print("ERROR", e)
    print(f"{len(errs)} errors")
    sys.exit(1 if errs else 0)
