#!/usr/bin/env python3
"""Check and build the three-voice glossary (plain, designer, engineer).

synthesis/glossary.json is the glossary: add and edit terms there. Each term has an id, a layer (one of LAYER_ORDER), the
three voices and a source. Lane U1 first wrote the terms in shards under synthesis/glossary/; they were merged into
glossary.json and retired on 2026-10-21 (git history has them).

  python3 tools/check_glossary.py --build            re-read the engine, check every term, sort glossary.json by layer and
                                                     write docs/GLOSSARY.md; then run tools/build_data.py
  python3 tools/check_glossary.py --check            the same checks against the engine as it is now, writing nothing; fails
                                                     if a term breaks a rule or docs/GLOSSARY.md is out of date (CI runs it)
  python3 tools/check_glossary.py draft.json         check a draft array of terms before adding it to glossary.json
  python3 tools/check_glossary.py --refresh-tokens   re-read the engine only: the token paths, state keys, commands and flags
                                                     the checks accept (synthesis/glossary/engine-token-paths.txt, engine-truth.json)
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


# State maps keyed by data (a question id, a token path, a standard id): their own key is real, and anything under it is accepted.
RECORD_MAPS = ("answers", "overrides", "standards.records", "standards.types", "standards.snapshots")


def engine_lists():
    """What the engine has today: the union of every token path it generates across the shipped examples, the default
    system and each dial at 0 and 100 (so tokens that appear only under some settings count as real), plus its state keys,
    $extensions paths, resolver modifiers, commands and flags."""
    import subprocess, tempfile
    dials = [d["id"] for d in json.loads((ROOT / "synthesis/levers.json").read_text())["dials"]]
    runs = [[]] + [[["set", f"dials.{d}", str(v), "--no-doc"]] for d in dials for v in (0, 100)]
    runs.append([["set", "taste.brief", "a quiet library at night", "--no-doc"], ["set", "taste.never", '["gradients"]', "--no-doc"]])  # set only by the person
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
                if ".".join(prefix + [k]) not in RECORD_MAPS:
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
    truth = dict(state_keys=sorted(state_keys), record_maps=list(RECORD_MAPS), extensions=sorted(ext), modifiers=sorted(modifiers),
                 commands=commands, flags=sorted(flags))
    return paths, truth, len(runs)


def refresh_tokens():
    paths, truth, runs = engine_lists()
    TRUTH_FILE.write_text(json.dumps(truth, indent=1) + "\n")
    TOKENS_FILE.write_text("\n".join(sorted(paths)) + "\n")
    print(f"{len(paths)} token paths from {runs} generated systems and the examples -> {TOKENS_FILE.relative_to(ROOT)}")
    return paths, truth


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
            under_record = any(name.startswith(r + ".") for r in truth.get("record_maps", ["answers"]))
            if under_record or name in key_prefixes or excused(m) or re.search(r"\.(json|md|py)$", name):
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


def check_entries(entries, label, real=None, truth=None):
    """Every rule in synthesis/THREE-VOICES.md that a script can check. real and truth are the engine lists; by default the
    committed copies (fast, for drafts), which --check and --build replace with a fresh read of the engine."""
    errors, warnings, grades = [], [], []
    seen = set()
    if real is None:
        real = set(TOKENS_FILE.read_text().split()) if TOKENS_FILE.exists() else set()
    if truth is None:
        truth = json.loads(TRUTH_FILE.read_text()) if TRUTH_FILE.exists() else None
    for e in entries:
        tag = f"{label}:{e.get('id', '?')}"
        for field in ("id", "term", "plain", "designer", "engineer", "source"):
            if not e.get(field):
                errors.append(f"{tag} missing {field}")
        if e.get("layer") not in LAYER_ORDER:
            errors.append(f"{tag} layer {e.get('layer')!r} is not one of {', '.join(LAYER_ORDER)}")
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


GLOSSARY = ROOT / "synthesis/glossary.json"
DOC = ROOT / "docs/GLOSSARY.md"


def load_sorted():
    entries = json.loads(GLOSSARY.read_text())
    for e in entries:
        if "aka" in e:  # writers may use either name; ship one
            e["aliases"] = e.pop("aka")
    return sorted(entries, key=lambda e: (LAYER_ORDER.index(e["layer"]) if e.get("layer") in LAYER_ORDER else len(LAYER_ORDER), e.get("id", "")))


def build(write):
    """Check glossary.json against the engine as it is now. With write: also refresh the engine lists, sort glossary.json and
    write docs/GLOSSARY.md. Without: report what --build would change."""
    paths, truth = refresh_tokens() if write else engine_lists()[:2]
    entries = load_sorted()
    errors, _, grades = check_entries(entries, "glossary", set(paths), truth)
    text, doc = json.dumps(entries, indent=1, ensure_ascii=False) + "\n", markdown(entries)
    if write:
        GLOSSARY.write_text(text)
        DOC.parent.mkdir(exist_ok=True)
        DOC.write_text(doc)
    else:
        if not DOC.exists() or DOC.read_text() != doc:
            errors.append("docs/GLOSSARY.md is out of date: run python3 tools/check_glossary.py --build")
        if GLOSSARY.read_text() != text:
            errors.append("synthesis/glossary.json is not in build order: run python3 tools/check_glossary.py --build")
    mean = sum(grades) / len(grades) if grades else 0
    print(f"{len(entries)} terms, plain voice mean grade {mean:.1f}")
    return errors


def markdown(entries):
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
    return "\n".join(out)


if __name__ == "__main__":
    if sys.argv[1:] == ["--refresh-tokens"]:
        refresh_tokens()
        sys.exit(0)
    if sys.argv[1:] in (["--build"], ["--check"]):
        errs = build(write=sys.argv[1] == "--build")
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
