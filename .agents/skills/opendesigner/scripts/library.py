#!/usr/bin/env python3
"""The optional OpenDesigner component library: list, suggest, add and check components.

  python3 library.py list [--type data] [--style dense] [--industry finance] [--json]
  python3 library.py suggest --industry finance [--style dense] [--type data]   one recommended pick, with its reason
  python3 library.py add <slug> [--into components/odl] [--tokens opendesigner/build/css/tokens.css]
  python3 library.py add <slug> --from https://opendesigner.dev                    fetch one component from the website instead
  python3 library.py catalog [--check]                                           write assets/library/library.json (the machine catalog)
  python3 library.py check                                                       the rules in assets/library/README.md, and the catalog

Components live in ../assets/library/components/<slug>/ (component.html and meta.json). They use only the --ds-* variables
the engine writes, so in a project with an OpenDesigner system they work with no edits. Standard library only; the network
is used only by add --from, for the one file asked for.
"""
import argparse
import json
import pathlib
import re
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
LIB = HERE.parent / "assets" / "library" / "components"
CATALOG = LIB.parent / "library.json"
ENGINE = HERE / "engine.py"
TYPES = ["data", "chart", "form", "feedback", "navigation", "overlay", "ai", "commerce", "content"]
STYLES = ["quiet", "dense", "technical", "friendly", "editorial"]
INDUSTRIES = ["finance", "saas", "devtools", "security", "crm", "logistics", "health", "education", "retail", "productivity",
              "social", "media", "travel", "food", "fitness", "events", "home", "money", "games", "any"]  # money: personal finance (finance is B2B)
WIDTHS = ["narrow", "medium", "wide"]
CONSUMER = {"retail", "health", "education", "social", "media", "travel", "food", "fitness", "events", "home", "money", "games"}  # site/library_page.py
EDGE = ["empty", "loading", "error", "disabled", "overflow", "long_text"]
EDGE_STATUS = ["shown", "handled", "not_built"]
SLOTS = ["text", "rich", "number", "media", "list", "action", "input", "none"]
FORMAT = "opendesigner.library/1"
FIELDS = ["name", "summary", "use", "type", "style", "industries", "tags", "states", "source", "a11y", "width"]
# Every CSS named colour (transparent, currentColor and inherit are fine).
NAMED = r"(?<![-\w])(" + "|".join(sorted("""aliceblue antiquewhite aqua aquamarine azure beige bisque black blanchedalmond blue blueviolet brown burlywood cadetblue chartreuse chocolate coral cornflowerblue cornsilk crimson cyan darkblue darkcyan darkgoldenrod darkgray darkgreen darkgrey darkkhaki darkmagenta darkolivegreen darkorange darkorchid darkred darksalmon darkseagreen darkslateblue darkslategray darkslategrey darkturquoise darkviolet deeppink deepskyblue dimgray dimgrey dodgerblue firebrick floralwhite forestgreen fuchsia gainsboro ghostwhite gold goldenrod gray green greenyellow grey honeydew hotpink indianred indigo ivory khaki lavender lavenderblush lawngreen lemonchiffon lightblue lightcoral lightcyan lightgoldenrodyellow lightgray lightgreen lightgrey lightpink lightsalmon lightseagreen lightskyblue lightslategray lightslategrey lightsteelblue lightyellow lime limegreen linen magenta maroon mediumaquamarine mediumblue mediumorchid mediumpurple mediumseagreen mediumslateblue mediumspringgreen mediumturquoise mediumvioletred midnightblue mintcream mistyrose moccasin navajowhite navy oldlace olive olivedrab orange orangered orchid palegoldenrod palegreen paleturquoise palevioletred papayawhip peachpuff peru pink plum powderblue purple rebeccapurple red rosybrown royalblue saddlebrown salmon sandybrown seagreen seashell sienna silver skyblue slateblue slategray slategrey snow springgreen steelblue tan teal thistle tomato turquoise violet wheat white whitesmoke yellow yellowgreen""".split(), key=len, reverse=True)) + r")(?![-\w])"
SPACING = r"^(padding|margin|gap|row-gap|column-gap|inset)(-[a-z-]+)?$"  # spacing in raw px is not a token
# attributes the OpenDesigner website's own scripts look for across the whole page: a part that used one would be rewritten
# by the site (a review's data-stars once became the GitHub star count). Keep parts off them.
RESERVED_ATTRS = ["stars", "forks", "issues", "pushed", "copy", "copy-text", "tabs", "slides", "au", "gallery", "kit-add", "look", "q", "rm", "thumb", "aisle", "goto-aisle"]
SCRIPT_BANNED = r"scrollIntoView|\bfetch\(|XMLHttpRequest|WebSocket|sendBeacon|localStorage|sessionStorage|document\.cookie|document\.(body|documentElement)|\beval\(|new Function|\bimport\(|window\.open|innerHTML|outerHTML|insertAdjacentHTML"
TOKEN_ONLY = ["font-size", "font-family", "font-weight", "border-radius", "box-shadow", "transition-duration", "animation-duration", "font"]


def components():
    out = []
    for d in sorted(p for p in LIB.iterdir() if p.is_dir()) if LIB.exists() else []:
        if not ((d / "meta.json").exists() and (d / "component.html").exists()):
            print(f"{d.name}: skipped, needs both component.html and meta.json", file=sys.stderr)
            continue
        meta = json.loads((d / "meta.json").read_text())
        out.append({"slug": d.name, **meta})
    return out


def matches(c, a):
    return ((not a.type or c["type"] == a.type) and (not a.style or c["style"] == a.style)
            and (not a.industry or a.industry in c["industries"] or "any" in c["industries"]))


def cmd_list(a):
    rows = [c for c in components() if matches(c, a)]
    if a.json:
        print(json.dumps(rows, indent=2))
        return 0
    for c in rows:
        print(f'{c["slug"]:<22} {c["type"]:<10} {c["style"]:<10} {",".join(c["industries"]):<22} {c["summary"]}')
    print(f"{len(rows)} of {len(components())} components")
    return 0


def cmd_suggest(a):
    """One pick for a person who should not have to browse: the best fit by industry, then style, then type."""
    def score(c):
        return ((3 if a.industry and a.industry in c["industries"] else 1 if "any" in c["industries"] else 0)
                + (2 if a.style and c["style"] == a.style else 0) + (2 if a.type and c["type"] == a.type else 0))
    pool = [c for c in components() if not a.type or c["type"] == a.type]  # what they asked for comes first
    ranked = sorted(pool, key=lambda c: -score(c))
    if not ranked or score(ranked[0]) == 0:
        print("No component fits this project well. Don't offer the library now.")
        return 0
    c = ranked[0]
    why = [w for w, ok in ((f"made for {a.industry}", a.industry in c["industries"]), (f"{c['style']} like the rest of the product", a.style == c["style"]),
                           (f"a {c['type']} part", a.type == c["type"])) if ok] or ["fits any product"]
    print(f'{c["slug"]}: {c["name"]}. {c["summary"]} Why: {", ".join(why)}.')
    return 0


def engine_vars():
    """The --ds-* names every system writes: the intersection over three different sketches (dense, regular and large
    audiences), because some roles exist only in some systems (a compact scale has no headline-md)."""
    sketches = [["--audience", "dense", "--platforms", "web", "--feel", "precise,calm", "--brand", "#15803D"],
                ["--audience", "regular", "--platforms", "ios,web", "--feel", "friendly,playful", "--brand", "#E0457B"],
                ["--audience", "large", "--platforms", "web", "--feel", "calm,trustworthy", "--brand", "#1E3A8A"]]
    sets = []
    for sk in sketches:
        with tempfile.TemporaryDirectory() as t:
            d = pathlib.Path(t) / "opendesigner"
            for args in (["sketch", "--name", "Check", *sk], ["build", "--force"]):
                subprocess.run([sys.executable, str(ENGINE), "--dir", str(d), *args], check=True, capture_output=True)
            sets.append(set(re.findall(r"(--ds-[a-z0-9-]+)\s*:", (d / "build/css/tokens.css").read_text())))
    return set.intersection(*sets)


def used_vars(text):
    return set(re.findall(r"var\((--ds-[a-z0-9-]+)", text))


def fetch(base, slug):
    """One component file from the website: https only (or a loopback address while testing a local build)."""
    import urllib.parse
    import urllib.request
    u = urllib.parse.urlparse(base.rstrip("/"))
    if u.scheme != "https" and u.hostname not in ("localhost", "127.0.0.1", "::1"):
        raise ValueError(f"--from must be an https address (got {base})")
    url = f"{base.rstrip('/')}/library/{slug}.html"
    req = urllib.request.Request(url, headers={"User-Agent": "opendesigner-library"})
    with urllib.request.urlopen(req, timeout=20) as r:
        body = r.read(512 * 1024 + 1)
    if len(body) > 512 * 1024 or f'class="odl-{slug}'.encode() not in body:
        raise ValueError(f"{url} is not an OpenDesigner component file")
    return body.decode()


def cmd_add(a):
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", a.slug):
        print(f"'{a.slug}' is not a component name. Run: library.py list")
        return 1
    if a.base:
        try:
            text = fetch(a.base, a.slug)
        except Exception as e:  # a missing page, no network or a wrong address: say which, change nothing
            print(f"Could not fetch {a.slug} from {a.base}: {e}")
            return 1
    else:
        src = LIB / a.slug / "component.html"
        if not src.exists():
            print(f"No component '{a.slug}'. Run: library.py list")
            return 1
        text = src.read_text()
    into = pathlib.Path(a.into)
    into.mkdir(parents=True, exist_ok=True)
    dest = into / f"{a.slug}.html"
    if dest.exists() and not a.force:
        print(f"{dest} already exists. Add --force to replace it.")
        return 1
    dest.write_text(text)
    print(f"Copied {a.slug} to {dest}")
    tok = pathlib.Path(a.tokens)
    if tok.exists():
        have = set(re.findall(r"(--ds-[a-z0-9-]+)\s*:", tok.read_text()))
        missing = sorted(used_vars(text) - have)
        print("Every variable it uses is in your tokens." if not missing else
              f"Your tokens lack {len(missing)} variable(s); map each to one of yours or run engine.py build: " + ", ".join(missing))
    else:
        print(f"No {tok}: map its --ds-* variables to your own tokens ({len(used_vars(text))} used).")
    return 0


def reserved_attrs(src):
    return sorted({m.group(1) for m in re.finditer(r"\sdata-([a-z-]+)(?=[\s=>])", src) if m.group(1) in RESERVED_ATTRS})


def check_one(c, known):
    errs, slug = [], c["slug"]
    for f in FIELDS:
        if f not in c:
            errs.append(f"meta.json lacks {f}")
    if c.get("type") not in TYPES:
        errs.append(f"type {c.get('type')!r} is not one of {TYPES}")
    if c.get("style") not in STYLES:
        errs.append(f"style {c.get('style')!r} is not one of {STYLES}")
    if c.get("width") not in WIDTHS:
        errs.append(f"width {c.get('width')!r} is not one of {WIDTHS}")
    for i in c.get("industries", []):
        if i not in INDUSTRIES:
            errs.append(f"industry {i!r} is not one of {INDUSTRIES}")
    if not 3 <= len(c.get("tags", [])) <= 6:
        errs.append("give 3 to 6 tags")
    if c.get("source") and not (LIB.parents[4] / c["source"]).exists() and (LIB.parents[4] / "brand").exists():
        errs.append(f"source {c['source']} does not exist")
    html_ = (LIB / slug / "component.html").read_text()
    styles = re.findall(r"<style>(.*?)</style>", html_, re.S)
    if len(styles) != 1:
        errs.append("needs exactly one <style> block")
    css = "".join(styles)
    rest = re.sub(r"<style>.*?</style>|<script>.*?</script>", "", html_, flags=re.S)
    scripts = re.findall(r"<script>(.*?)</script>", html_, re.S)
    if len(scripts) > 1:
        errs.append("at most one <script>")
    if re.search(r"<(link|iframe)\b|<script\s+src|@import|url\(", html_):
        errs.append("loads something external (link, iframe, script src, @import or url())")
    # photos: only free Unsplash photos, hotlinked from images.unsplash.com in an <img> with alt, size and lazy loading, each
    # credited in meta.json "photos" (CRAFT.md section 5; owner, 2026-10-23: "wherever there is an image placeholder, use
    # sample images from Unsplash")
    credited = {ph.get("img") for ph in c.get("photos", []) if isinstance(ph, dict)}
    for tag in re.findall(r"<img\b[^>]*>", html_):
        src = (re.search(r'\ssrc="([^"]*)"', tag) or [None, ""])[1]
        m = re.match(r"https://images\.unsplash\.com/(photo-[A-Za-z0-9-]+)\?", src)
        if not m:
            errs.append(f"<img> may only load a free Unsplash photo from images.unsplash.com (got {src[:60]!r})")
            continue
        for a in ("alt", "width", "height"):
            if not re.search(rf'\s{a}="', tag):
                errs.append(f"<img> {m.group(1)} needs {a}")
        if 'loading="lazy"' not in tag:
            errs.append(f'<img> {m.group(1)} needs loading="lazy"')
        if m.group(1) not in credited:
            errs.append(f'photo {m.group(1)} is not listed in meta.json "photos" with its author')
    for a in reserved_attrs(html_):
        errs.append(f"uses data-{a}, which the website's own scripts read across the page: rename it (data-{a}-value, or a word of your own)")
    body = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    decls, stack, start = [], [], 0
    for m in re.finditer(r"[{}]", body):
        if m.group(0) == "{":
            prelude = body[start:m.start()].strip().split(";")[-1].strip()
            if prelude.startswith("@"):
                stack.append("keyframes" if prelude.startswith("@keyframes") else "group")
            else:
                stack.append("rule")
                if "keyframes" not in stack[:-1]:
                    for part in prelude.split(","):
                        p = part.strip()
                        if p and not p.startswith(f".odl-{slug}"):
                            errs.append(f"selector not scoped to .odl-{slug}: {p}")
        else:
            if stack and stack[-1] == "rule":
                decls += re.findall(r"([a-z-]+)\s*:\s*([^;]+)", body[start:m.start()])
            if stack:
                stack.pop()
        start = m.end()
    for where, text in (("CSS", body), ("markup", " ".join(re.findall(r'(?:style|fill|stroke|color)="([^"]*)"', rest)))):
        for m in re.finditer(r"#[0-9a-fA-F]{3,8}\b|\b(?:rgba?|hsla?|oklch|oklab|lab|lch|color-mix)\(", text):
            errs.append(f"colour literal in {where}: {m.group(0)}")
        for m in re.finditer(NAMED, re.sub(r"--[a-z0-9-]+|@keyframes\s+[\w-]+|animation(-name)?\s*:[^;]+", "", text)):
            errs.append(f"named colour in {where}: {m.group(0)}")
    moves = False
    for prop, val in decls:
        v = val.strip()
        if prop in ("transition", "animation") and v != "none" or prop.startswith(("transition-", "animation-")):
            moves = True
        if prop in TOKEN_ONLY and v not in ("inherit", "0", "none", "normal") and "var(--ds-" not in v:
            errs.append(f"{prop} is not a token: {v}")
        if prop in ("transition", "animation") and re.search(r"(?<![\w-])\d*\.?\d+m?s\b", re.sub(r"var\([^)]*\)", "", v)):
            errs.append(f"{prop} has a raw duration: {v}")
        if re.match(SPACING, prop) and re.search(r"(?<![\w-])\d*\.?\d+(px|rem|em)\b", re.sub(r"var\([^)]*\)", "", v)):
            errs.append(f"{prop} has a raw length (use a space token): {v}")
    # a text highlight is a plain fill: no underline stroke along its bottom edge (owner, 2026-10-21: it curves at the line
    # ends). Any bottom inset shadow or bottom border on an inline or highlighted element is caught; a field's straight focus
    # line (a search box) is fine.
    for sel, decl in re.findall(r"(?:^|(?<=[{};]))\s*([^{}@;]+?)\s*\{([^{}]*)\}", body):
        if re.search(r"search|input|field|:has\(", sel):
            continue
        if re.search(r"box-shadow:\s*inset 0 (calc\(-|-)", decl) or (re.search(r"border-(bottom|block-end)(-[a-z]+)?\s*:", decl) and re.search(r"(mark|target|highlight|\bhl\b|ins|del)\b", sel)):
            errs.append(f"underline stroke on {sel.strip()[:60]}: a highlight or text gets a plain fill, never a bottom stroke")
    # nor a hard ledge under a box (a shadow pushed down with no blur, the "3D button" lip): the owner reads it as the same
    # curved bottom stroke (2026-10-22, quiz answers and a lesson path)
    for sel, decl in re.findall(r"(?:^|(?<=[{};]))\s*([^{}@;]+?)\s*\{([^{}]*)\}", body):
        if re.search(r"box-shadow:[^;]*?(?<![\w-])0 (var\(--ds-space-[^)]+\)|calc\([^)]*\)|[1-9][\d.]*px) 0 (var\(--ds-color|var\(--[a-z]|#|rgb)", decl):
            errs.append(f"hard bottom ledge on {sel.strip()[:60]}: a shadow pushed down with no blur reads as a bottom stroke; use a fill or a soft elevation token")
    # a list row is sized by the row or control tokens; the touch-target floor is a minimum, not a size (a sidebar with 24 px
    # rows read as cramped: Michael Filipiuk's sidebar clean-up, 2026-10-23)
    for sel, decl in re.findall(r"(?:^|(?<=[{};]))\s*([^{}@;]+?)\s*\{([^{}]*)\}", body):
        if re.search(r"\.odl-(item|row|opt|option|entry)\b|\[role=\"?(menuitem|option)|\bli\b", sel) and re.search(r"(?<![\w-])min-block-size:\s*var\(--ds-size-target-min\)", decl):
            errs.append(f"row {sel.strip()[:60]} is sized by the target floor: use max(var(--ds-size-control-md), var(--ds-size-target-min)) or a --ds-size-row-* token")
    if moves and "prefers-reduced-motion" not in body:
        errs.append("it animates: add a @media (prefers-reduced-motion: reduce) block that turns its motion off")
    if not re.search(r":focus-visible", body) and re.search(r"<(button|input|a|select|textarea|summary)\b", rest):
        errs.append("interactive parts need a :focus-visible style")
    for js in scripts:
        for m in re.finditer(SCRIPT_BANNED, js):
            errs.append(f"script uses {m.group(0)}: a component script only wires its own root")
        # the website shows each part several times (cards, previews) with ids and aria references stripped; a script that
        # finds elements by id breaks there (trip-search and itinerary threw on load, 2026-10-23)
        if re.search(r"getElementById|querySelector(All)?\(\s*[\"'`]#|[\"'`]#[\"'`]\s*\+|\[aria-(labelledby|controls|describedby)=", js):
            errs.append("script finds elements by id or aria reference: copies of the part have no ids; find them by class, data attribute or order")
        if f'querySelectorAll(".odl-{slug}")' not in js:
            errs.append(f'script must start from document.querySelectorAll(".odl-{slug}")')
    for v in sorted(used_vars(html_) - known):
        errs.append(f"{v} is not a variable every engine system writes")
    if f'class="odl-{slug}' not in rest:
        errs.append(f"the root element needs class odl-{slug}")
    return errs


# ---- the machine catalog (library.json): what each component is, holds and does, for agents, the MCP server and smart UI.
# Derived fields come from component.html, so they cannot drift; authored ones come from meta.json "spec". Format: README.md.
IMPLICIT = {"nav": "navigation", "ol": "list", "ul": "list", "table": "table", "form": "form", "dialog": "dialog", "article": "article",
            "aside": "complementary", "header": "banner", "footer": "contentinfo", "progress": "progressbar", "meter": "meter"}
CONTROLS = {"button": r"<button\b", "input": r"<input\b(?![^>]*type=\"hidden\")", "link": r"<a\b[^>]*\shref=", "select": r"<select\b",
            "textarea": r"<textarea\b", "summary": r"<summary\b"}


def markup(src):
    return re.sub(r"<style>.*?</style>|<script>.*?</script>", "", src, flags=re.S)


def audience(industries):
    if "any" in industries:
        return "any"
    kinds = {"consumer" if i in CONSUMER else "work" for i in industries}
    return kinds.pop() if len(kinds) == 1 else "any"


def roles(src):
    m = markup(src)
    out = set(re.findall(r'\srole="([a-z]+)"', m))
    out |= {r for tag, r in IMPLICIT.items() if re.search(rf"<{tag}\b", m)}
    if re.search(r"<section\b[^>]*\saria-label(ledby)?=", m):
        out.add("region")
    return sorted(out - {"presentation", "none"})


def entry(c):
    src = (LIB / c["slug"] / "component.html").read_text()
    css = "".join(re.findall(r"<style>(.*?)</style>", src, re.S))
    m, sp = markup(src), c.get("spec", {})
    use = [c["use"]] + [u for u in sp.get("use_when", []) if u != c["use"]]
    return {
        "id": c["slug"], "name": c["name"], "purpose": c["summary"], "use_when": use, "avoid_when": sp.get("avoid_when", []),
        "type": c["type"], "style": c["style"], "width": c["width"],
        "tags": {"audience": audience(c["industries"]), "industries": c["industries"], "keywords": c["tags"]},
        "root": f".odl-{c['slug']}", "parts": sp.get("parts", []), "data": sp.get("data", {}),
        "states": {"shown": c["states"], "edge": {k: sp.get("edge", {}).get(k) for k in EDGE}},
        "tokens": sorted(used_vars(src)),
        "a11y": {"summary": c["a11y"], "roles": roles(src), "keyboard": sp.get("keyboard", []),
                 "controls": {k: len(re.findall(rx, m)) for k, rx in CONTROLS.items()},
                 "focus_visible": ":focus-visible" in css, "reduced_motion": "prefers-reduced-motion" in css,
                 "min_target": "--ds-size-target-min" in css},
        "files": {"html": f"components/{c['slug']}/component.html", "bytes": len(src.encode()), "script": "<script>" in src},
        "source": c.get("source"), "photos": len(c.get("photos", [])),
    }


def version():
    m = re.search(r'^OPENDESIGNER_VERSION = "([^"]+)"', ENGINE.read_text(), re.M)
    return m.group(1) if m else "unknown"


def catalog():
    return {"format": FORMAT, "version": version(), "count": len(components()),
            "vocab": {"types": TYPES, "styles": STYLES, "industries": INDUSTRIES, "audiences": ["work", "consumer", "any"],
                      "widths": WIDTHS, "slots": SLOTS, "edge_states": EDGE, "edge_status": EDGE_STATUS},
            "components": [entry(c) for c in components()]}


def catalog_text():
    return json.dumps(catalog(), indent=1, ensure_ascii=False) + "\n"


def cmd_catalog(a):
    text = catalog_text()
    if a.check:
        ok = CATALOG.exists() and CATALOG.read_text() == text
        print(f"{CATALOG.name} is current" if ok else f"{CATALOG.name} is out of date: run library.py catalog")
        return 0 if ok else 1
    CATALOG.write_text(text)
    print(f"Wrote {CATALOG} ({len(components())} components)")
    return 0


def selector_found(sel, m):
    """Each class and element a selector names exists in the markup (attribute and pseudo parts are not checked)."""
    s = re.sub(r"\[[^\]]*\]|::?[a-z-]+(\([^)]*\))?", "", sel)
    for cls in re.findall(r"\.([A-Za-z][\w-]*)", s):
        if not re.search(rf'class="[^"]*(?<![\w-]){re.escape(cls)}(?![\w-])', m):
            return f"class {cls}"
    for tag in re.findall(r"(?:^|[\s>+~,])([a-z][a-z0-9]*)(?=[\s.>+~#:,\[]|$)", s):
        if not re.search(rf"<{tag}\b", m):
            return f"element {tag}"
    return None


def schema_errors(node, where, parts):
    errs = []
    if not isinstance(node, dict):
        return [f"{where} is not an object"]
    if "part" in node and node["part"] not in parts:
        errs.append(f"{where} names part {node['part']!r}, which is not in spec.parts")
    t = node.get("type")
    if "enum" in node or "const" in node:
        return errs
    if t == "string":
        if "maxLength" not in node:
            errs.append(f"{where} is a string without maxLength")
    elif t == "array":
        if "maxItems" not in node:
            errs.append(f"{where} is a list without maxItems")
        errs += schema_errors(node.get("items", {}), f"{where}[]", parts) if "items" in node else [f"{where} has no items"]
    elif t == "object":
        props = node.get("properties", {})
        for r in node.get("required", []):
            if r not in props:
                errs.append(f"{where} requires {r!r}, which is not a property")
        for k, v in props.items():
            errs += schema_errors(v, f"{where}.{k}", parts)
    elif t not in ("number", "integer", "boolean"):
        errs.append(f"{where} has type {t!r}")
    return errs


def spec_errors(c):
    """The authored half of the catalog: present, and true to the file."""
    sp, errs = c.get("spec"), []
    if not isinstance(sp, dict):
        return ["meta.json lacks spec (see README.md, library.json)"]
    src = (LIB / c["slug"] / "component.html").read_text()
    m = markup(src)
    for k in ("avoid_when", "parts", "keyboard"):
        if not isinstance(sp.get(k), list):
            errs.append(f"spec.{k} must be a list")
    if not sp.get("avoid_when"):
        errs.append("spec.avoid_when needs at least one case")
    names = set()
    for p in sp.get("parts", []):
        if not {"name", "selector", "what", "slot"} <= set(p):
            errs.append(f"spec.parts item {p.get('name')!r} needs name, selector, what and slot")
            continue
        names.add(p["name"])
        if p["slot"] not in SLOTS:
            errs.append(f"part {p['name']}: slot {p['slot']!r} is not one of {SLOTS}")
        miss = selector_found(p["selector"], m)
        if miss:
            errs.append(f"part {p['name']}: selector {p['selector']!r} names {miss}, which is not in the file")
    if not sp.get("parts"):
        errs.append("spec.parts is empty")
    data = sp.get("data")
    if not isinstance(data, dict) or data.get("type") != "object":
        errs.append("spec.data must be a JSON Schema object")
    else:
        errs += schema_errors(data, "data", names)
    edge = sp.get("edge", {})
    for k in EDGE:
        e = edge.get(k)
        if not isinstance(e, dict) or e.get("status") not in EDGE_STATUS:
            errs.append(f"spec.edge.{k} needs a status: one of {EDGE_STATUS}")
            continue
        if not e.get("how"):
            errs.append(f"spec.edge.{k} needs how")
        if e["status"] != "not_built" and (not e.get("evidence") or e["evidence"] not in src):
            errs.append(f"spec.edge.{k} is {e['status']}: its evidence {e.get('evidence')!r} must be a string found in component.html")
    for k in set(edge) - set(EDGE):
        errs.append(f"spec.edge.{k} is not one of {EDGE}")
    if any(re.search(rx, m) for rx in CONTROLS.values()) and not sp.get("keyboard"):
        errs.append("spec.keyboard is empty, but the file has controls")
    return errs


def cmd_check(_a):
    known = engine_vars()
    cs, bad = components(), 0
    for c in cs:
        errs = check_one(c, known) + spec_errors(c)
        bad += bool(errs)
        print(f"{c['slug']}: " + ("ok" if not errs else "\n  " + "\n  ".join(errs)))
    print(f"{len(cs)} components, {bad} with problems")
    stale = not CATALOG.exists() or CATALOG.read_text() != catalog_text()
    if stale:
        print(f"{CATALOG.name} is out of date: run library.py catalog")
    return 1 if bad or not cs or stale else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("list", "suggest"):
        p = sub.add_parser(name)
        p.add_argument("--type", choices=TYPES)
        p.add_argument("--style", choices=STYLES)
        p.add_argument("--industry", choices=INDUSTRIES)
        if name == "list":
            p.add_argument("--json", action="store_true")
    p = sub.add_parser("add")
    p.add_argument("slug")
    p.add_argument("--into", default="components/odl")
    p.add_argument("--tokens", default="opendesigner/build/css/tokens.css")
    p.add_argument("--force", action="store_true", help="replace a file that is already there")
    p.add_argument("--from", dest="base", metavar="URL", help="fetch the component from this website (https://opendesigner.dev) instead of this copy")
    p = sub.add_parser("catalog")
    p.add_argument("--check", action="store_true", help="only say whether library.json is current")
    sub.add_parser("check")
    a = ap.parse_args()
    return {"list": cmd_list, "suggest": cmd_suggest, "add": cmd_add, "catalog": cmd_catalog, "check": cmd_check}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
