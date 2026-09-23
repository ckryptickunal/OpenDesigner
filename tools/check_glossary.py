#!/usr/bin/env python3
"""Check and build the three-voice glossary (plain, designer, engineer).

  python3 tools/check_glossary.py synthesis/glossary/shard-a.json   check one shard while writing it
  python3 tools/check_glossary.py --build                          merge shards, check coverage, write
                                                                   synthesis/glossary.json and docs/GLOSSARY.md
  python3 tools/check_glossary.py --refresh-tokens                 regenerate engine-token-paths.txt from the engine
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


TOKENS_FILE = G / "engine-token-paths.txt"
TRUTH_FILE = G / "engine-truth.json"   # state keys, $extensions paths, resolver modifiers, engine commands and flags
ENGINE = ROOT / "skills/opendesigner/scripts/engine.py"
# Dotted names starting with these roots are treated as token paths and must match what the engine generates.
TOKEN_ROOTS = ("color", "space", "radius", "font", "text", "motion", "elevation", "size", "opacity", "border", "focus",
               "icon", "layer", "shadow", "chart", "avatar", "nav", "input", "button", "illustration", "haptic", "z")
TOKEN_RE = re.compile(r"\b(?:%s)(?:\.[A-Za-z0-9*]+(?:-[A-Za-z0-9*]+)*)+" % "|".join(TOKEN_ROOTS))


def refresh_tokens():
    """Union of every token path the engine generates across the shipped examples, the default system,
    and each dial at 0 and 100, so tokens that appear only under some settings count as real."""
    import subprocess, tempfile
    dials = [d["id"] for d in json.loads((ROOT / "synthesis/levers.json").read_text())["dials"]]
    runs = [[]] + [[["set", f"dials.{d}", str(v), "--no-doc"]] for d in dials for v in (0, 100)]
    paths = set()

    def walk(node, prefix):
        if isinstance(node, dict):
            if "$value" in node:
                paths.add(".".join(prefix))
                return
            for k, v in node.items():
                if not k.startswith("$"):
                    walk(v, prefix + [k])

    def collect(tokens_dir):
        for f in Path(tokens_dir).rglob("*.json"):
            walk(json.loads(f.read_text()), [])

    state_keys, ext, modifiers = set(), set(), set()

    def state_walk(node, prefix):
        if isinstance(node, dict):
            for k, v in node.items():
                state_keys.add(".".join(prefix + [k]))
                if k != "answers":
                    state_walk(v, prefix + [k])

    def ext_walk(node, prefix):
        if isinstance(node, dict):
            for k, v in node.items():
                ext.add(".".join(prefix + [k]))
                ext_walk(v, prefix + [k])

    def meta(folder):
        folder = Path(folder)
        if (folder / "state.json").exists():
            state_walk(json.loads((folder / "state.json").read_text()), [])
        for f in (folder / "tokens").rglob("*.json"):
            data = json.loads(f.read_text())
            if "modifiers" in data:
                for name, m in data["modifiers"].items():
                    modifiers.add(name)
                    modifiers.update(m.get("contexts", {}))
            stack = [data]
            while stack:
                n = stack.pop()
                if isinstance(n, dict):
                    for k, v in n.items():
                        if k == "$extensions" and isinstance(v, dict):
                            ext_walk(v, ["$extensions"])
                        else:
                            stack.append(v)

    for example in sorted((ROOT / "examples").glob("*/tokens")):
        collect(example)
        meta(example.parent)
    with tempfile.TemporaryDirectory() as tmp:
        for i, steps in enumerate(runs):
            d = Path(tmp) / f"run{i}" / "opendesigner"
            for args in (["init", "--name", "Glossary check"], *steps, ["generate"]):
                subprocess.run([sys.executable, str(ENGINE), "--dir", str(d), *args], check=True, capture_output=True)
            collect(d / "tokens")
            meta(d)
    help_out = subprocess.run([sys.executable, str(ENGINE), "--help"], capture_output=True, text=True).stdout
    commands = sorted(set(re.search(r"\{([a-z,-]+)\}", help_out).group(1).split(",")))
    flags = set(re.findall(r"(--[a-z][a-z-]+)", help_out))
    for c in commands:
        flags |= set(re.findall(r"(--[a-z][a-z-]+)", subprocess.run([sys.executable, str(ENGINE), c, "--help"],
                                                                        capture_output=True, text=True).stdout))
    TRUTH_FILE.write_text(json.dumps(dict(state_keys=sorted(state_keys), extensions=sorted(ext), modifiers=sorted(modifiers),
                                          commands=commands, flags=sorted(flags)), indent=1) + "\n")
    TOKENS_FILE.write_text("\n".join(sorted(paths)) + "\n")
    print(f"{len(paths)} token paths from {len(runs)} generated systems and the examples -> {TOKENS_FILE.relative_to(ROOT)}")


def unknown_tokens(e, real):
    """Token-like names in the engineer voice or code_name that the engine does not generate and are not marked (proposed)."""
    prefixes = {".".join(p.split(".")[:i]) for p in real for i in range(1, p.count(".") + 1)}
    bad = []
    for field in ("engineer", "code_name"):
        text = e.get(field, "")
        for m in TOKEN_RE.finditer(text):
            name = m.group(0).rstrip(".")
            if ".tokens" in name or re.search(r"\.(json|py|svg|html|css|txt|png)$", name) or \
                    (name.endswith(".md") and (re.search(r"[A-Z]", name) or name.count(".") == 1)):  # file names
                continue
            base = name[:-2] if name.endswith(".*") else name
            if name in real or base in prefixes or base in real:
                continue
            if "(proposed)" in text[m.end():m.end() + 14]:
                continue
            bad.append(f"{field}: {name}")
    return bad


STATE_RE = re.compile(r"\b(?:raw|dials|answers|hooks|context|profile|zoom|locks|overrides|principles|components|references|"
                      r"taste|macros|preset|system|exports|blocks|summary)(?:\.[A-Za-z0-9_*-]+)+")
EXT_RE = re.compile(r"\$extensions(?:\.[A-Za-z0-9_*]+)+")
CMD_RE = re.compile(r"engine\.py\s+([a-z][a-z-]*)")
FLAG_RE = re.compile(r"(?<![\w-])(--[a-z][a-z-]+)")


def unknown_config(e, truth):
    """State keys, $extensions paths, engine commands and flags that do not exist, unless marked (proposed) or planned."""
    bad = []
    keys, ext = set(truth["state_keys"]), set(truth["extensions"])
    key_prefixes = {".".join(k.split(".")[:i]) for k in keys for i in range(1, k.count(".") + 2)}
    for field in ("engineer", "code_name", "designer"):
        text = e.get(field, "")
        def excused(m):
            around = text[max(0, m.start() - 40):m.end() + 14].lower()
            return "(proposed)" in around or "planned" in around or "not generated" in around
        for m in STATE_RE.finditer(text):
            name = m.group(0).rstrip(".*").rstrip(".")
            if name.startswith("answers.") or name in key_prefixes or excused(m) or re.search(r"\.(json|md|py)$", name):
                continue
            bad.append(f"{field}: state key {name}")
        for m in EXT_RE.finditer(text):
            name = m.group(0).rstrip(".*").rstrip(".")
            if name in ext or excused(m):
                continue
            bad.append(f"{field}: {name}")
        for m in CMD_RE.finditer(text):
            if m.group(1) not in truth["commands"] and not excused(m):
                bad.append(f"{field}: engine command {m.group(1)}")
        for m in FLAG_RE.finditer(text):
            if m.group(1) not in truth["flags"] and "engine" in text and not excused(m):
                bad.append(f"{field}: flag {m.group(1)}")
    return bad


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
    real = set(TOKENS_FILE.read_text().split()) if TOKENS_FILE.exists() else set()
    truth = json.loads(TRUTH_FILE.read_text()) if TRUTH_FILE.exists() else None
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
        if real:
            for u in unknown_tokens(e, real):
                errors.append(f"{tag} names a token the engine does not generate ({u}); use the real name or add (proposed)")
        if truth:
            for u in unknown_config(e, truth):
                errors.append(f"{tag} names something the engine does not have ({u}); use the real name or mark it (proposed)/planned")
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
    if sys.argv[1:] == ["--refresh-tokens"]:
        refresh_tokens()
        sys.exit(0)
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
