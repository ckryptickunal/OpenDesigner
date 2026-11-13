#!/usr/bin/env python3
"""Smart UI: an assistant's answer arrives as the right piece of interface, built only from the person's own system.

  python3 smartui.py scope [--project .] [--json]          read the repo: product, chat surface, framework, tokens,
                                                            actions; propose intents and components (writes nothing
                                                            unless --write)
  python3 smartui.py catalog [--tokens T] [--out D]        A2UI v1.0 catalog + the component bundle for the renderer
  python3 smartui.py prompt --for "<message>" [--k 3]      pick the few components that fit and print the prompt
  python3 smartui.py validate <answer.json> [--source data.json] [--partial] [--a2ui]
  python3 smartui.py view [--answer A]                     one self-contained HTML file (the MCP Apps view)
  python3 smartui.py text <answer.json>                    the text-only fallback for a host that renders no UI
  python3 smartui.py audit [--fixtures] [--answer F]       render in headless Chromium and run the floors and the
                                                            craft checks (needs Playwright for Python; never installs it)

Files go in ./opendesigner/smart-ui/ (catalog.json, od-components.js, scope.json, audit/). Standard library only,
no network. The rules (R1 to R7) are in ../references/rules.md.
"""
import argparse
import datetime
import html as htmllib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
SKILL = HERE.parent
SKILLS = SKILL.parent
CORE = SKILLS / "opendesigner"
LIB = CORE / "assets" / "library" / "components"
SET = SKILL / "assets" / "set.json"
sys.path.insert(0, str(CORE / "scripts"))
import slots  # noqa: E402  (the shared mark reader in the core skill)

A2UI_VERSION = "1.0"
CATALOG_VERSION = 1
VISUAL = {"tone", "emphasis", "size", "density"}       # enums that pick a look: their values must be token families
EVENT = {"type": "object", "additionalProperties": False, "required": ["name"],
         "properties": {"name": {"type": "string", "pattern": "^[a-z][a-z0-9_]*$", "maxLength": 40},
                        "context": {"type": "object", "maxProperties": 8,
                                    "additionalProperties": {"type": ["string", "number", "boolean"], "maxLength": 200}}}}
MEDIA = {"type": "object", "additionalProperties": False, "required": ["src", "alt"],
         "properties": {"src": {"type": "string", "format": "uri", "maxLength": 2048, "x-od-url": "image"},
                        "alt": {"type": "string", "minLength": 1, "maxLength": 200}}}
LIMITS = {"components": 8, "depth": 3, "leaves": 1}
HANDLER = re.compile(r"^on[A-Z_]|^on(click|dblclick|load|error|abort|mouse\w*|key\w*|focus\w*|blur|change|input|submit|pointer\w*|touch\w*|wheel|scroll|drag\w*|drop|animation\w*|transition\w*)$", re.I)
BANNED_KEYS = {"style", "class", "classname", "css", "theme", "html", "innerhtml", "outerhtml", "dangerouslysetinnerhtml", "srcdoc"}
HTML = re.compile(r"<\s*/?\s*[a-zA-Z!][^>]*>|<\s*[a-zA-Z]")
WHOLE_STYLE = re.compile(r"^\s*(#(?:[0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})|-?\d*\.?\d+(px|rem|em|vh|vw|pt)|(rgba?|hsla?|oklch|oklab|lab|lch|color-mix|var|calc|url|expression)\(.*)\s*$", re.I)
NUM = re.compile(r"(?<![\w.])-?\d[\d,]*(?:\.\d+)?")


# ----------------------------------------------------------------------------------------------- the set and the library

def od(obj):
    """Our extra facts on a catalog or a component, kept where A2UI allows them: metadata.extensions.opendesigner."""
    return ((obj or {}).get("metadata") or {}).get("extensions", {}).get("opendesigner", {})


def ext(facts):
    return {"extensions": {"opendesigner": facts}}


def load_set():
    return json.loads(SET.read_text())


def component(slug):
    d = LIB / slug
    src = (d / "component.html").read_text()
    meta = json.loads((d / "meta.json").read_text())
    return src, meta


def token_names(path):
    p = pathlib.Path(path)
    return set(re.findall(r"(--ds-[a-z0-9-]+)\s*:", p.read_text())) if p.exists() else set()


def token_backed(value, tokens):
    """A visual enum value is allowed only when the system has a colour family by that name."""
    if not tokens:
        return True
    return any(t.startswith(f"--ds-color-{p}-{value}") for t in tokens for p in ("text", "bg", "border", "icon")) or \
        any(t.startswith(f"--ds-color-{value}-") for t in tokens)


# ----------------------------------------------------------------------------------------------- catalog

def _clean(prop):
    return {k: v for k, v in prop.items() if k not in ("part",)}


def props_for(nodes, spec, css, tokens, where=""):
    """JSON Schema properties for one scope of marks, merged with the component's authored spec.data."""
    sprops = (spec or {}).get("properties", {})
    props, names_text = {}, []
    for n in nodes:
        k, name = n["kind"], n["name"]
        s = _clean(sprops.get(name, {}))
        if k == "text":
            names_text.append(name)
            t = s.get("type")
            p = s if (set(t) if isinstance(t, list) else {t}) & {"string", "number", "integer"} or "enum" in s else {"type": "string", "maxLength": 120}
            if p.get("type") == "string" and "maxLength" not in p:
                p["maxLength"] = 120
            props.setdefault(name, p)
        elif k == "input":
            props.setdefault(name, {"type": "string", "pattern": "^[a-z][a-z0-9_]*$", "maxLength": 40})
            for extra, ps in (("value", {"type": ["string", "number", "boolean"], "maxLength": 200}), ("required", {"type": "boolean"}),
                              ("min", {"type": "number"}), ("max", {"type": "number"})):
                if extra in sprops or extra in ("value", "required"):
                    props.setdefault(extra, {**ps, **{x: y for x, y in _clean(sprops.get(extra, {})).items() if x in ("maxLength", "minimum", "maximum")}})
            if "options" in sprops:
                props.setdefault("options", {"type": "array", "maxItems": sprops["options"].get("maxItems", 20), "items": {
                    "type": "object", "additionalProperties": False, "required": ["label", "value"],
                    "properties": {"label": {"type": "string", "maxLength": 60}, "value": {"type": "string", "maxLength": 60}}}})
        elif k == "label":
            props.setdefault(name, {"type": "string", "maxLength": 120, **{x: y for x, y in s.items() if x in ("maxLength", "description")}})
        elif k == "measure":
            if name in props and props[name].get("type") == "string":
                props[name] = {"type": s.get("type") if s.get("type") in (["number", "null"], ["null", "number"]) else "number", **{x: y for x, y in s.items() if x in ("minimum", "maximum", "description")}}
            else:
                props.setdefault(name, {"type": s.get("type") if isinstance(s.get("type"), list) else "number", **{x: y for x, y in s.items() if x in ("minimum", "maximum", "description")}})
            props[name]["x-od-measure"] = True
        elif k in ("var", "when"):
            vals = slots.css_values(css, name) if k == "var" else n.get("values", [])
            if "enum" in s:
                vals = [v for v in s["enum"] if v in vals] or s["enum"] if k == "var" else s["enum"]
            if name in VISUAL:
                vals = [v for v in vals if token_backed(v, tokens)]
            old = props.get(name, {}).get("enum", [])
            props[name] = {"type": "string", "enum": sorted(set(old) | set(vals)) if k == "when" else vals}
            if name in VISUAL:
                props[name]["x-od-token"] = True
        elif k == "media":
            props[name] = json.loads(json.dumps(MEDIA))
        elif k == "action":
            kids = props_for([c for c in n.get("children", []) if c["name"] != "label"], s, css, tokens, where + name + ".")
            props[name] = {"type": "object", "additionalProperties": False, "required": ["label", "event"],
                           "properties": {"label": {"type": "string", "minLength": 1, "maxLength": 40},
                                          "a11y_label": {"type": "string", "maxLength": 120},
                                          "event": {"$ref": "#/$defs/Event"}, **kids["properties"]},
                           "x-od-effect": n.get("effect", "none")}
        elif k == "list":
            items = s.get("items", {})
            inner = props_for(n.get("children", []), items, css, tokens, where + name + "[].")
            arr = {"type": "array", "minItems": s.get("minItems", 0), "maxItems": s.get("maxItems", 12),
                   "items": {"type": "object", "additionalProperties": False, "properties": inner["properties"],
                             "required": inner["required"]}}
            if inner["name_from"]:
                arr["items"]["x-od-name-from"] = inner["name_from"]
            props[name] = arr
    req = [r for r in (spec or {}).get("required", []) if r in props] if spec and "required" in spec else \
        [n["name"] for n in nodes if n["kind"] == "text" and not n.get("optional")]
    for n in nodes:  # actions and media are required unless the authored spec says otherwise
        if n["kind"] in ("action",) and not spec and n["name"] not in req:
            req.append(n["name"])
    return {"properties": props, "required": sorted(set(req), key=list(props).index),
            "name_from": next((t for t in names_text if props.get(t, {}).get("type") == "string"), None)}


def pascal(slug):
    return "".join(w.capitalize() for w in slug.split("-"))


def build_catalog(tokens_path=None, system="system", allow_images=(), allow_links=(), only=None, library=False):
    """library=True adds every other marked library part (group "library"), for audits of the whole library."""
    tokens = token_names(tokens_path) if tokens_path else set()
    cset = load_set()
    comps, x_od, bundle = {}, {}, {}
    entries = list(cset["components"])
    if library:
        have = {c["slug"] for c in entries}
        entries += [{"slug": d.name, "as": pascal(d.name), "group": "library", "intents": []}
                    for d in sorted(LIB.iterdir()) if d.is_dir() and d.name not in have]
    for c in entries:
        if only and c["slug"] not in only:
            continue
        if not ((LIB / c["slug"] / "component.html").exists() and (LIB / c["slug"] / "meta.json").exists()):
            print(f"{c['slug']}: not in the library yet, left out", file=sys.stderr)
            continue
        src, meta = component(c["slug"])
        marks = slots.read_marks(src)
        if not marks:
            if c["group"] != "library":
                print(f"{c['slug']}: has no slot marks yet, left out", file=sys.stderr)
            continue
        css = "".join(re.findall(r"<style>(.*?)</style>", src, re.S))
        spec = meta.get("spec", {})
        built = props_for(marks, spec.get("data"), css, tokens)
        schema = {"type": "object", "description": meta.get("summary", ""), "additionalProperties": False,
                  "properties": {"component": {"const": c["as"]}, "id": {"type": "string", "maxLength": 64},
                                 "@accessibility": {"$ref": "#/$defs/Accessibility"}, "@metadata": {"$ref": "#/$defs/Metadata"},
                                 **built["properties"]},
                  "required": ["component", "id", *built["required"]]}
        schema["metadata"] = ext({"slug": c["slug"], "group": c["group"], "name": meta.get("name"), "use": meta.get("use"),
                          "use_when": spec.get("use_when", []), "avoid_when": spec.get("avoid_when", []),
                          "tags": meta.get("tags", []), "intents": c.get("intents", []), "width": meta.get("width"),
                          "name_from": built["name_from"]})
        comps[c["as"]] = schema
        bundle[c["as"]] = {"slug": c["slug"], "src": src}
    comps["Column"] = {"type": "object", "description": "Two to four parts one under the other, only when the person asked for more than one.",
                       "additionalProperties": False, "required": ["component", "id", "children"],
                       "properties": {"component": {"const": "Column"}, "id": {"type": "string", "maxLength": 64},
                                      "children": {"type": "array", "minItems": 2, "maxItems": 4, "items": {"type": "string", "maxLength": 64}},
                                      "gap": {"type": "string", "enum": ["sm", "md", "lg"]}, "@accessibility": {"$ref": "#/$defs/Accessibility"}},
                       "metadata": ext({"slug": None, "group": "layout", "container": True})}
    cid = f"https://opendesigner.dev/catalogs/{re.sub(r'[^a-z0-9-]+', '-', system.lower()).strip('-') or 'system'}/v{CATALOG_VERSION}/catalog.json"
    catalog = {
        "$schema": "https://json-schema.org/draft/2020-12/schema", "$id": cid, "catalogId": cid, "protocolVersion": A2UI_VERSION,
        "title": f"{system}: Smart UI catalog",
        "description": "Components an assistant may answer with, built only from this system's tokens. Generated by OpenDesigner smartui.py catalog; do not edit.",
        "instructions": INSTRUCTIONS,
        "components": comps, "functions": {},
        "$defs": {"anyComponent": {"oneOf": [{"$ref": f"#/components/{k}"} for k in comps]}, "anyFunction": {"not": {}},
                  "Event": EVENT,
                  "Accessibility": {"type": "object", "additionalProperties": False,
                                    "properties": {"label": {"type": "string", "maxLength": 120}, "description": {"type": "string", "maxLength": 240},
                                                   "live": {"type": "string", "enum": ["off", "polite"]}, "hidden": {"type": "boolean"}}},
                  "Metadata": {"type": "object", "additionalProperties": False,
                               "properties": {"stale_since": {"type": "string", "maxLength": 40}, "permission": {"type": "string", "enum": ["granted", "denied"]},
                                              "permission_note": {"type": "string", "maxLength": 160}}}},
        "metadata": ext({"system": system, "set_version": cset["version"], "made": datetime.date.today().isoformat(),
                         "allow": {"images": sorted(allow_images), "links": sorted(allow_links)}, "limits": LIMITS}),
    }
    return catalog, bundle


INSTRUCTIONS = (
    "Answer in plain text first. Show a component only when it does a job text cannot: a list to pick from, numbers to compare, "
    "a form to fill, a step to approve. A short factual answer stays text (R1). One component per answer unless the person asked "
    "for more (R2). Actions that change data (book, pay, send, delete) are buttons the person presses; never claim they happened (R3). "
    "Use only the components and properties in this catalog; there are no colour, size, style, class or URL-of-your-choice properties (R4). "
    "Every number must come from the data you were given; leave a value out when you do not have it (R6). Text is plain: no HTML or markdown.")


def bundle_js(bundle):
    """od-components.js: each component's own template (trusted library markup) and its wiring script, for <od-surface>."""
    out = ["/* Generated by OpenDesigner smartui.py catalog. Library components (MIT); icons Lucide (ISC). Do not edit. */",
           "(function (g) { var R = (g.ODSmartUI = g.ODSmartUI || {}); R.components = R.components || {};"]
    for name, b in bundle.items():
        src = b["src"]
        style = "".join(re.findall(r"<style>(.*?)</style>", src, re.S))
        script = "".join(re.findall(r"<script>(.*?)</script>", src, re.S))
        markup = re.sub(r"<style>.*?</style>|<script>.*?</script>|<!--.*?-->", "", src, flags=re.S).strip()
        wire = f"function () {{ {script} }}" if script.strip() else "null"
        out.append(f"R.components[{json.dumps(name)}] = {{ slug: {json.dumps(b['slug'])}, css: {json.dumps(style)}, html: {json.dumps(markup)}, wire: {wire} }};")
    out.append("})(typeof window !== 'undefined' ? window : globalThis);")
    return "\n".join(out) + "\n"


def classic_js():
    """od-validate.js and od-surface.js as one plain script (no modules), for a single-file view."""
    out = []
    for f in ("od-validate.js", "od-surface.js"):
        js = (SKILL / "assets" / f).read_text()
        js = re.sub(r"^import .*?;\s*$", "", js, flags=re.M)
        js = re.sub(r"^export default .*?;\s*$", "", js, flags=re.M)
        js = re.sub(r"^export (?=(function|class|const|let|async))", "", js, flags=re.M)
        out.append(js)
    return "(function () {\n" + "\n".join(out) + "\n})();\n"


VIEW_BRIDGE = r"""
(function () {
  // MCP Apps bridge (2026-01-26): JSON-RPC 2.0 over postMessage. The view shows the answer the show_ui tool checked.
  var s = document.getElementById("s"), cat = JSON.parse(document.getElementById("od-catalog").textContent);
  s.catalog = cat;
  var id = 0, waiting = {};
  function send(m) { if (window.parent !== window) window.parent.postMessage(m, "*"); }
  function request(method, params) { var i = ++id; send({ jsonrpc: "2.0", id: i, method: method, params: params });
    return new Promise(function (ok) { waiting[i] = ok; setTimeout(function () { if (waiting[i]) { delete waiting[i]; ok(null); } }, 4000); }); }
  var hostLook = false, hostVars = null;
  function applyHost(ctx) {
    if (!ctx) return;
    if (ctx.theme) document.documentElement.setAttribute("data-theme", ctx.theme);
    if (ctx.styles && ctx.styles.variables) hostVars = ctx.styles.variables;
    if (hostLook && hostVars) { // R7: the host's look only when the owner opted in
      var map = { "--color-background-primary": "--ds-color-surface-raised", "--color-background-secondary": "--ds-color-bg-neutral-subtle",
        "--color-text-primary": "--ds-color-text-primary", "--color-text-secondary": "--ds-color-text-secondary",
        "--color-border-primary": "--ds-color-border-subtle", "--font-sans": "--ds-font-family-body", "--border-radius-md": "--ds-radius-container" };
      Object.keys(map).forEach(function (k) { if (hostVars[k]) document.documentElement.style.setProperty(map[k], hostVars[k]); });
    }
  }
  function size() { send({ jsonrpc: "2.0", method: "ui/notifications/size-changed", params: { width: document.documentElement.scrollWidth, height: document.documentElement.scrollHeight } }); }
  function show(sc) {
    if (!sc || !sc.answer) return;
    hostLook = !!sc.host_look; applyHost({});
    s.reset(); s.process(sc.answer); setTimeout(size, 50);
  }
  s.addEventListener("od-action", function (e) {
    var a = e.detail.action;
    request("ui/message", { role: "user", content: [{ type: "text", text: "OD:action " + a.name + " " + JSON.stringify(a.context) }] });
  });
  window.addEventListener("message", function (ev) {
    var m = ev.data; if (!m || m.jsonrpc !== "2.0") return;
    if (m.id && waiting[m.id]) { var ok = waiting[m.id]; delete waiting[m.id]; ok(m.result || null); return; }
    if (m.method === "ui/notifications/tool-result") show((m.params || {}).structuredContent);
    else if (m.method === "ui/notifications/host-context-changed") applyHost(m.params);
    else if (m.method === "ui/resource-teardown" && m.id) send({ jsonrpc: "2.0", id: m.id, result: {} });
  });
  new ResizeObserver(size).observe(document.body);
  request("ui/initialize", { protocolVersion: "2026-01-26", appInfo: { name: "opendesigner-smart-ui", version: "1" },
    appCapabilities: { availableDisplayModes: ["inline"] } }).then(function (r) {
    applyHost(r && r.hostContext);
    send({ jsonrpc: "2.0", method: "ui/notifications/initialized", params: {} });
  });
  var pre = document.getElementById("od-answer");   // a standalone file opened with an answer in it
  if (pre && pre.textContent.trim()) show(JSON.parse(pre.textContent));
})();
"""


def view_html(catalog, components_js, tokens_css, answer=None):
    """One self-contained HTML page: tokens, the renderer, the parts and the catalog. The MCP Apps view, or a file to open."""
    esc = lambda t: t.replace("</", "<\\/")
    return ("<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
            f"<title>{htmllib.escape(od(catalog).get('system') or 'Smart UI')}</title>"
            f"<style>{esc(tokens_css)}\n{esc((SKILL / 'assets' / 'od-surface.css').read_text())}\n"
            "body{margin:0;padding:var(--ds-space-inset-md);background:transparent;color:var(--ds-color-text-primary)}</style></head><body>"
            "<od-surface id=\"s\"></od-surface>"
            f"<script type=\"application/json\" id=\"od-catalog\">{esc(json.dumps(catalog))}</script>"
            f"<script type=\"application/json\" id=\"od-answer\">{esc(json.dumps({'answer': answer})) if answer else ''}</script>"
            f"<script>{esc(components_js)}</script><script>{esc(classic_js())}</script><script>{esc(VIEW_BRIDGE)}</script></body></html>\n")


def cmd_view(a):
    out = pathlib.Path(a.out)
    cat = _load_catalog(out / "catalog.json")
    comps = (out / "od-components.js").read_text()
    tokens = pathlib.Path(a.tokens).read_text()
    ans = smartui_answer(a.answer, cat) if a.answer else None
    dest = pathlib.Path(a.write or (out / "surface.html"))
    dest.write_text(view_html(cat, comps, tokens, ans))
    print(f"Wrote {dest}: one file with your tokens, the renderer and {len(cat['components']) - 1} parts" + (", showing the answer" if ans else ""))
    return 0


def smartui_answer(path, cat):
    ans = extract_answer(pathlib.Path(path).read_text())
    r = validate(ans, cat)
    if not r["ok"]:
        sys.exit("The answer does not pass the validator: " + "; ".join(e["rule"] + " " + e["path"] for e in r["errors"][:5]))
    return ans


def cmd_catalog(a):
    out = pathlib.Path(a.out)
    tokens = a.tokens
    catalog, bundle = build_catalog(tokens, a.system or _system_name(), a.allow_images or [], a.allow_links or [],
                                    _chosen(a) if not (a.all or a.library) else None, library=a.library)
    out.mkdir(parents=True, exist_ok=True)
    (out / "catalog.json").write_text(json.dumps(catalog, indent=1) + "\n")
    (out / "od-components.js").write_text(bundle_js(bundle))
    n = len(catalog["components"]) - 1
    print(f"Wrote {out}/catalog.json ({n} components, catalogId {catalog['catalogId']}) and od-components.js")
    if not token_names(tokens):
        print(f"No tokens at {tokens}: visual enums are not checked against your system. Pass --tokens <your tokens.css>.")
    return 0


def _system_name():
    st = pathlib.Path("opendesigner/state.json")
    try:
        return json.loads(st.read_text()).get("name") or "system"
    except (OSError, ValueError):
        return "system"


def _chosen(a):
    p = pathlib.Path(a.out) / "scope.json"
    try:
        s = json.loads(p.read_text())
        return set(s.get("components_confirmed") or []) or None
    except (OSError, ValueError):
        return None


def components_md():
    """references/components.md: the set by job, from set.json and each part's meta.json (smartui.py components --write)."""
    cset = load_set()
    lines = ["# The parts, by job", "",
             "Generated by `smartui.py components --write` from `assets/set.json` and each part's `meta.json` in the library. "
             "Every part is a library component with slot marks; the catalog lists only the ones a project confirmed.", ""]
    for g, what in cset["groups"].items():
        rows = [c for c in cset["components"] if c["group"] == g]
        if not rows:
            continue
        lines += [f"## {what} ({g})", "", "| Part | Library component | What it shows |", "|---|---|---|"]
        for c in rows:
            try:
                meta = json.loads((LIB / c["slug"] / "meta.json").read_text())
            except OSError:
                meta = {"summary": "not in the library yet"}
            lines.append(f"| `{c['as']}` | `{c['slug']}` | {meta.get('summary', '').replace('|', '/')} |")
        lines.append("")
    lines += ["Every part handles the states in `states.md`; its fixture is `fixture.json` beside the part in the library.", ""]
    return "\n".join(lines)


def cmd_components(a):
    text = components_md()
    dest = SKILL / "references" / "components.md"
    if a.check:
        ok = dest.exists() and dest.read_text() == text
        print("components.md is current" if ok else "components.md is out of date: smartui.py components --write")
        return 0 if ok else 1
    if a.write:
        dest.write_text(text)
        print(f"wrote {dest}")
    else:
        print(text)
    return 0


# ----------------------------------------------------------------------------------------------- selector and prompt

STOP = set("a an the of to in on for and or with my me i is are be it this that what how do does can you your our we at by from show tell give please about".split())
UI_CUES = re.compile(r"\b(compare|vs\.?|versus|options|list|table|chart|graph|trend|breakdown|break down|split|book|schedule|pick|choose|form|fill|steps|"
                     r"show me|find|search|status|track|receipt|confirm|approve|pay|send|delete|cancel|upload|download|file|code|snippet|where is|"
                     r"map|photo|picture|each month|per month|by month|over time|changed|moved|how much|spend|spent|update|change|details|"
                     r"explain|define|meaning|go through|went through|times?|slots?|available|invoice|refund|year)\b", re.I)
CONTRACT = [(r"\bwhere's\b", "where is"), (r"\bwhat's\b", "what is"), (r"\bhow's\b", "how is"), (r"\bwhen's\b", "when is"),
            (r"\bit's\b", "it is"), (r"\bthat's\b", "that is"), (r"\bi'm\b", "i am"), (r"\bdidn't\b", "did not")]


def norm(t):
    t = t.lower()
    for a, b in CONTRACT:
        t = re.sub(a, b, t)
    return t


def stem(w):
    for suf in ("ings", "ing", "ies", "ied", "es", "ed", "s"):
        if len(w) > len(suf) + 2 and w.endswith(suf):
            return w[: -len(suf)] + ("y" if suf in ("ies", "ied") else "")
    return w


def words(t):
    return [stem(w) for w in re.findall(r"[a-z0-9']+", norm(t)) if w not in STOP]


def score(msg, comp):
    """How well one part fits a message: whole intent phrases, then shared words with its intents, tags and use."""
    m, xs, s = norm(msg), od(comp), 0.0
    mw = set(words(msg))
    for phrase in xs.get("intents", []):
        pw = set(words(phrase))
        if norm(phrase) in m:
            s += 3 + len(phrase.split()) * 0.5
        elif pw and len(pw & mw) == len(pw) and len(pw) > 1:
            s += 2.5
        elif pw & mw:
            s += 0.8 * len(pw & mw) / len(pw)
    bag = set(words(" ".join(xs.get("tags", []) + xs.get("use_when", []) + [xs.get("use") or "", xs.get("name") or ""])))
    s += 0.4 * len(bag & mw)
    return s


def data_signals(data):
    """What the data itself says: an error to report, or a search that found nothing."""
    out = {}
    def walk(v, key=""):
        if isinstance(v, dict):
            if any(k in v for k in ("error", "errors")) or (key.endswith("error") and v):
                out["ErrorRetry"] = 4
            for k, x in v.items():
                walk(x, k)
        elif isinstance(v, list) and not v and key:
            out["EmptyState"] = 4
    walk(data)
    return out


def select(msg, catalog, k=3, scope=None, data=None):
    """The top-k components for one message, and whether the message gives a reason for UI at all (R1)."""
    ranked = []
    sig = data_signals(data) if data is not None else {}
    for name, c in catalog["components"].items():
        if od(c).get("container"):
            continue
        s = score(msg, c) + sig.get(name, 0)
        for it in (scope or {}).get("intents", []):
            if name in it.get("components", []) and any(norm(p) in norm(msg) for p in it.get("phrases", [])):
                s += 4
        ranked.append((s, name))
    ranked.sort(key=lambda x: (-x[0], x[1]))
    top = [n for s, n in ranked[:k] if s >= 0.8]
    best = ranked[0][0] if ranked else 0
    cue = bool(UI_CUES.search(norm(msg)))
    reason = cue or best >= 3
    short_fact = (len(words(msg)) <= 6 and re.match(r"^\s*(what|when|who|how many|is|are|does|did|can|do)\b", norm(msg))
                  and not cue and best < 3)
    ui = bool(top) and reason and not short_fact
    return {"ui": ui, "candidates": top if ui else [], "scores": {n: round(s, 2) for s, n in ranked[:k + 2]},
            "why": ("a cue for UI and a part that fits" if ui else "no reason for UI: answer in text (R1)")}


def compact(schema):
    """A short, model-readable form of one component's properties (no x-od, no refs)."""
    def one(p):
        if "$ref" in p:
            return "{name, context?}" if p["$ref"].endswith("Event") else "object"
        t = p.get("type")
        if "enum" in p:
            return "|".join(map(str, p["enum"]))
        if t == "array":
            return f"[{one(p['items'])}] ({p.get('minItems', 0)}-{p.get('maxItems', '')})"
        if t == "object":
            req = set(p.get("required", []))
            return "{" + ", ".join(f"{k}{'' if k in req else '?'}: {one(v)}" for k, v in p.get("properties", {}).items()) + "}"
        if t == "string":
            return f"text<={p.get('maxLength', '')}" if "format" not in p else "url"
        return str(t)
    req = set(schema.get("required", []))
    return ", ".join(f"{k}{'' if k in req else '?'}: {one(v)}" for k, v in schema["properties"].items()
                     if k not in ("component", "id", "@accessibility", "@metadata"))


def build_prompt(msg, catalog, k=3, scope=None, data=None):
    sel = select(msg, catalog, k, scope, data)
    lines = [
        "You can answer with interface parts from the person's own design system (OpenDesigner Smart UI).",
        catalog["instructions"],
        "",
        "Output: your text answer. If a part helps, add ONE fenced block marked a2ui holding a JSON array of A2UI v1.0 messages:",
        '```a2ui\n[{"version":"1.0","createSurface":{"surfaceId":"s1","catalogId":"' + catalog["catalogId"] + '",'
        '"components":[{"id":"root","component":"<Name>", ...properties}]}}]\n```',
        "Button and link actions are {label, event: {name, context?}}; event names are lower_snake_case. Images only from: "
        + (", ".join(od(catalog)["allow"]["images"]) or "nowhere (no images allowed)") + ".",
        "",
    ]
    if sel["ui"]:
        lines.append("Parts that may fit this message (use at most one, or none):")
        for n in sel["candidates"]:
            c = catalog["components"][n]
            lines.append(f"- {n}: {c['description']} When: {'; '.join(od(c).get('use_when', [])[:2]) or od(c).get('use')}. "
                         f"Properties: {compact(c)}")
    else:
        lines.append("No part fits a reason to show interface here: answer in text only.")
    if data is not None:
        lines += ["", "Data you may use (every number you show must come from here):", json.dumps(data, ensure_ascii=False)[:6000]]
    return "\n".join(lines), sel


def cmd_prompt(a):
    catalog = _load_catalog(a.catalog)
    scope = _load_json(pathlib.Path(a.catalog).parent / "scope.json")
    data = _load_json(a.data) if a.data else None
    text, sel = build_prompt(a.for_, catalog, a.k, scope, data)
    print(json.dumps(sel) if a.json else text)
    return 0


# ----------------------------------------------------------------------------------------------- validator

def _err(errs, rule, path, msg, sid, fix=None):
    e = {"code": "VALIDATION_FAILED", "rule": rule, "path": path, "message": msg, "surfaceId": sid}
    if fix:
        e["fix"] = fix
    errs.append(e)


def _host(url):
    m = re.match(r"^https://([^/?#:]+)(:\d+)?([/?#]|$)", url)
    return m.group(1).lower() if m else None


def host_allowed(host, allow):
    return any(host == h or (h.startswith("*.") and host.endswith(h[1:])) for h in allow)


def resolve(value, data, path, errs, sid, partial, ctx):
    """This catalog takes values, not A2UI data bindings: a {"@path": ...} is refused, so what renders is what was checked."""
    if isinstance(value, dict) and "@path" in value:
        _err(errs, "binding", path, "this catalog takes values, not @path bindings", sid, "put the value itself here")
        return None
    return value


def check_value(v, schema, path, errs, sid, cat, opts, ctx):
    """One value against the schema subset the catalog uses. Returns the value with @path bindings resolved."""
    if "$ref" in schema:
        schema = cat["$defs"][schema["$ref"].rsplit("/", 1)[1]]
    t = schema.get("type")
    types = t if isinstance(t, list) else [t] if t else []
    if v is None:
        if "null" not in types and types:
            _err(errs, "type", path, f"expected {' or '.join(types)}, got null; leave it out, or the part must allow a missing value", sid)
        return None
    v = resolve(v, ctx["data"], path, errs, sid, opts.get("partial"), ctx)
    if v is None:
        return None
    pyt = {"string": str, "number": (int, float), "integer": int, "boolean": bool, "array": list, "object": dict, "null": type(None)}
    if types and not any(isinstance(v, pyt[x]) and not (x in ("number", "integer") and isinstance(v, bool)) for x in types):
        _err(errs, "type", path, f"expected {' or '.join(types)}, got {type(v).__name__}", sid)
        return v
    if "const" in schema and v != schema["const"]:
        _err(errs, "type", path, f"must be {schema['const']!r}", sid)
    if "enum" in schema and v not in schema["enum"]:
        rule = "R4-token" if schema.get("x-od-token") else "enum"
        _err(errs, rule, path, f"{v!r} is not one of {schema['enum']}", sid, f"use one of: {', '.join(map(str, schema['enum']))}")
        return v
    if isinstance(v, str):
        if len(v) > schema.get("maxLength", 10 ** 9):
            _err(errs, "length", path, f"text is {len(v)} characters, the most is {schema['maxLength']}", sid, "shorten it")
        if len(v) < schema.get("minLength", 0):
            _err(errs, "empty", path, "must not be empty", sid)
        if "pattern" in schema and not re.fullmatch(schema["pattern"], v):
            _err(errs, "pattern", path, f"{v!r} does not match {schema['pattern']}", sid)
        if schema.get("format") == "uri":
            kind = schema.get("x-od-url", "link")
            host = _host(v)
            if not host:
                _err(errs, "R4-url", path, "only https URLs are allowed", sid)
            elif not host_allowed(host, od(cat)["allow"]["images" if kind == "image" else "links"]):
                _err(errs, "R4-url", path, f"{host} is not on the allow-list for {kind}s", sid, "leave it out, or ask the owner to add the domain")
        elif not schema.get("x-od-code"):
            if HTML.search(v):
                _err(errs, "R4-html", path, "text holds HTML; text is plain only", sid, "write the words without tags")
            elif WHOLE_STYLE.match(v):
                _err(errs, "R4-style", path, f"{v!r} is a style value (colour, size or CSS); there are no style properties", sid)
        if ctx.get("numbers") is not None and not schema.get("x-od-code"):
            for n in NUM.findall(v):
                if _num(n) not in ctx["numbers"]:
                    ctx["warnings"].append({"rule": "R6-text", "path": path, "message": f"{n} in the text is not in the data you were given"})
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        if "minimum" in schema and v < schema["minimum"] or "maximum" in schema and v > schema["maximum"]:
            _err(errs, "range", path, f"{v} is outside {schema.get('minimum', '-inf')} to {schema.get('maximum', 'inf')}", sid)
        if ctx.get("numbers") is not None and float(v) not in ctx["numbers"]:
            _err(errs, "R6-number", path, f"{v} is not in the data you were given", sid, "use the value from the data, or leave it out and show it as missing")
    if isinstance(v, list):
        if len(v) > schema.get("maxItems", 10 ** 9):
            _err(errs, "items", path, f"{len(v)} items, the most is {schema['maxItems']}", sid, "show fewer, or say how many more there are")
        if len(v) < schema.get("minItems", 0) and not opts.get("partial") and not opts.get("allow_empty"):
            _err(errs, "items", path, f"{len(v)} items, the fewest is {schema['minItems']}", sid)
        it = schema.get("items", {})
        return [check_value(x, it, f"{path}/{i}", errs, sid, cat, opts, ctx) for i, x in enumerate(v)]
    if isinstance(v, dict):
        props = schema.get("properties", {})
        addl = schema.get("additionalProperties", True)
        if len(v) > schema.get("maxProperties", 10 ** 9):
            _err(errs, "items", path, f"{len(v)} keys, the most is {schema['maxProperties']}", sid)
        out = {}
        for k, x in v.items():
            if k.lower() in BANNED_KEYS or HANDLER.match(k):
                _err(errs, "R4-key", f"{path}/{k}", f"{k!r} is not allowed: no style, class, theme, HTML or event-handler keys", sid, "remove it")
                continue
            if k in props:
                out[k] = check_value(x, props[k], f"{path}/{k}", errs, sid, cat, opts, ctx)
            elif isinstance(addl, dict):
                out[k] = check_value(x, addl, f"{path}/{k}", errs, sid, cat, opts, ctx)
            elif addl is False:
                _err(errs, "unknown-property", f"{path}/{k}", f"unknown property {k!r}", sid, f"use only: {', '.join(p for p in props if not p.startswith('@'))}")
            else:
                out[k] = x
        if not opts.get("partial"):
            for r in schema.get("required", []):
                if r not in v:
                    _err(errs, "required", f"{path}/{r}", f"{r} is required", sid)
        if schema.get("x-od-effect") == "change" and isinstance(v.get("event"), dict) and "approved" in (v["event"].get("context") or {}):
            _err(errs, "R3-approval", f"{path}/event/context/approved", "an action that changes data is approved by the person, never in the answer", sid, "remove approved")
        return out
    return v


def _num(s):
    try:
        return float(str(s).replace(",", ""))
    except ValueError:
        return None


def numbers_in(obj, out=None):
    out = set() if out is None else out
    if isinstance(obj, bool):
        return out
    if isinstance(obj, (int, float)):
        out.add(float(obj))
    elif isinstance(obj, str):
        out.update(x for x in (_num(n) for n in NUM.findall(obj)) if x is not None)
    elif isinstance(obj, dict):
        for v in obj.values():
            numbers_in(v, out)
    elif isinstance(obj, list):
        for v in obj:
            numbers_in(v, out)
    return out


def normalize(answer):
    """Accept a list of A2UI messages, one message, or {"messages": [...]}."""
    if isinstance(answer, dict) and "messages" in answer:
        answer = answer["messages"]
    if isinstance(answer, dict):
        answer = [answer]
    return answer if isinstance(answer, list) else None


def accessible_names(comp, schema, cat, base, out):
    """Each action's name as a screen reader hears it (label, plus the item's name in a list), for the repeat check."""
    def walk(v, s, path, item_name):
        if "$ref" in s:
            return
        if isinstance(v, dict) and s.get("type") == "object":
            for k, x in v.items():
                ps = s.get("properties", {}).get(k)
                if not ps:
                    continue
                if ps.get("x-od-effect") is not None and isinstance(x, dict):
                    name = x.get("a11y_label") or (x.get("label", "") + (f", {item_name}" if item_name else ""))
                    out.append((name.strip().lower(), f"{path}/{k}"))
                else:
                    walk(x, ps, f"{path}/{k}", item_name)
        elif isinstance(v, list) and s.get("type") == "array":
            it = s.get("items", {})
            nf = it.get("x-od-name-from")
            for i, x in enumerate(v):
                walk(x, it, f"{path}/{i}", (x.get(nf) if isinstance(x, dict) and nf and isinstance(x.get(nf), str) else item_name))
    walk(comp, schema, base, None)


def validate(answer, cat, opts=None):
    """Errors (A2UI error objects plus the rule and a fix) and warnings for one answer. Same rules as od-validate.js."""
    opts = opts or {}
    errs, warns = [], []
    msgs = normalize(answer)
    if msgs is None:
        _err(errs, "shape", "", "an answer is a list of A2UI messages", "")
        return {"ok": False, "errors": errs, "warnings": warns, "surfaces": {}}
    surfaces = {}
    numbers = numbers_in(opts["source"]) if opts.get("source") is not None else None
    for i, m in enumerate(msgs):
        base = f"/{i}"
        if not isinstance(m, dict):
            _err(errs, "shape", base, "each message is an object", "")
            continue
        if m.get("version") != A2UI_VERSION:
            _err(errs, "version", f"{base}/version", f'version must be "{A2UI_VERSION}"', "", 'add "version": "1.0"')
        kinds = [k for k in ("createSurface", "updateComponents", "updateDataModel", "deleteSurface") if k in m]
        extra = [k for k in m if k not in ("version", "createSurface", "updateComponents", "updateDataModel", "deleteSurface")]
        if len(kinds) != 1 or extra:
            _err(errs, "shape", base, "each message has exactly one of createSurface, updateComponents, updateDataModel, deleteSurface", "")
            continue
        kind = kinds[0]
        body = m[kind]
        sid = body.get("surfaceId") if isinstance(body, dict) else None
        if not isinstance(sid, str) or not sid:
            _err(errs, "shape", f"{base}/{kind}/surfaceId", "surfaceId is required", "")
            continue
        if kind == "createSurface":
            if sid in surfaces:
                errs.append({"code": "INTEGRITY_ERROR", "rule": "integrity", "path": f"{base}/{kind}/surfaceId", "message": f"surface {sid} already exists", "surfaceId": sid})
            if "theme" in body:
                _err(errs, "R4-key", f"{base}/{kind}/theme", "A2UI v1.0 has no theme; the system's tokens style the surface", sid, "remove theme")
            if body.get("catalogId") not in (None, cat["catalogId"]):
                _err(errs, "catalog", f"{base}/{kind}/catalogId", f"this renderer supports only {cat['catalogId']}", sid)
            for k in body:
                if k not in ("surfaceId", "catalogId", "components", "dataModel", "sendDataModel", "metadata", "theme"):
                    _err(errs, "unknown-property", f"{base}/{kind}/{k}", f"unknown key {k!r}", sid)
            surfaces[sid] = {"components": {}, "data": body.get("dataModel") if isinstance(body.get("dataModel"), dict) else {}}
            comps = body.get("components", [])
        elif sid not in surfaces:
            errs.append({"code": "INTEGRITY_ERROR", "rule": "integrity", "path": f"{base}/{kind}/surfaceId", "message": f"no surface {sid}; createSurface comes first", "surfaceId": sid})
            continue
        elif kind == "updateComponents":
            comps = body.get("components", [])
        elif kind == "updateDataModel":
            path = body.get("path", "/")
            val = body.get("value")
            if path in ("/", ""):
                surfaces[sid]["data"] = val if isinstance(val, dict) else {}
            else:
                cur = surfaces[sid]["data"]
                parts = [p.replace("~1", "/").replace("~0", "~") for p in path.split("/")[1:]]
                for p in parts[:-1]:
                    cur = cur.setdefault(p, {}) if isinstance(cur, dict) else {}
                if isinstance(cur, dict):
                    if val is None:
                        cur.pop(parts[-1], None)
                    else:
                        cur[parts[-1]] = val
            continue
        else:
            surfaces.pop(sid, None)
            continue
        if not isinstance(comps, list):
            _err(errs, "shape", f"{base}/{kind}/components", "components is a list", sid)
            continue
        for j, c in enumerate(comps):
            cpath = f"{base}/{kind}/components/{j}"
            if not isinstance(c, dict):
                _err(errs, "shape", cpath, "a component is an object", sid)
                continue
            name = c.get("component")
            schema = cat["components"].get(name)
            if schema is None:
                _err(errs, "unknown-component", f"{cpath}/component", f"unknown component {name!r}", sid,
                     "use one of: " + ", ".join(k for k in cat["components"]))
                continue
            ctx = {"data": surfaces[sid]["data"], "numbers": numbers, "warnings": warns}
            checked = check_value(c, schema, cpath, errs, sid, cat, opts, ctx)
            acc = c.get("@accessibility") or {}
            if isinstance(acc, dict) and acc.get("live") == "assertive":
                pass  # the schema already refuses it (R5: polite only)
            if isinstance(c.get("id"), str):
                surfaces[sid]["components"][c["id"]] = {"c": checked if isinstance(checked, dict) else c, "path": cpath, "schema": schema}
    for sid, s in surfaces.items():
        structure(sid, s, cat, opts, errs)
    return {"ok": not errs, "errors": errs, "warnings": warns,
            "surfaces": {sid: {"data": s["data"], "components": {k: v["c"] for k, v in s["components"].items()}} for sid, s in surfaces.items()}}


def structure(sid, s, cat, opts, errs):
    comps = s["components"]
    limits = {**od(cat).get("limits", LIMITS), **{k: v for k, v in (opts.get("limits") or {}).items() if v}}
    if not comps:
        return
    if len(comps) > limits["components"]:
        _err(errs, "R2-size", "", f"{len(comps)} components on one surface; the most is {limits['components']}", sid)
    if "root" not in comps:
        if not opts.get("partial"):
            _err(errs, "root", "", 'one component needs id "root"', sid)
        return
    seen, leaves = set(), []

    def walk(cid, depth, trail):
        if cid in trail:
            errs.append({"code": "INTEGRITY_ERROR", "rule": "cycle", "path": comps[cid]["path"], "message": f"{cid} contains itself", "surfaceId": sid})
            return
        if cid not in comps:
            if not opts.get("partial"):
                _err(errs, "children", "", f"child {cid!r} does not exist", sid)
            return
        seen.add(cid)
        if depth > limits["depth"]:
            _err(errs, "depth", comps[cid]["path"], f"nested {depth} deep; the most is {limits['depth']}", sid)
            return
        c = comps[cid]["c"]
        if od(comps[cid]["schema"]).get("container"):
            for ch in c.get("children", []) if isinstance(c.get("children"), list) else []:
                walk(ch, depth + 1, trail | {cid})
        else:
            leaves.append(cid)
    walk("root", 1, frozenset())
    for cid, v in comps.items():
        if cid not in seen and not opts.get("partial"):
            _err(errs, "orphan", v["path"], f"{cid} is not reached from root", sid, "add it to a Column's children or remove it")
    if len(leaves) > limits["leaves"]:
        _err(errs, "R2-one", "", f"{len(leaves)} parts in one answer; show one unless the person asked for more", sid, "keep the one that answers the question")
    names = []
    for cid in leaves:
        accessible_names(comps[cid]["c"], comps[cid]["schema"], cat, comps[cid]["path"], names)
    count = {}
    for n, p in names:
        count.setdefault(n, []).append(p)
    for n, ps in count.items():
        if not n:
            _err(errs, "R5-name", ps[0], "an action has no name", sid, "give it a label")
        elif len(ps) > 1:
            _err(errs, "R5-repeat", ps[1], f"{len(ps)} actions are all called {n!r}", sid, "give each a11y_label that says which one, for example \"Book the 08:40 flight\"")


def _load_json(p):
    try:
        return json.loads(pathlib.Path(p).read_text())
    except (OSError, ValueError, TypeError):
        return None


def _load_catalog(p):
    c = _load_json(p)
    if not c:
        sys.exit(f"No catalog at {p}. Run: smartui.py catalog")
    return c


def extract_answer(text):
    """The A2UI messages in a model's reply (a fenced a2ui block, or JSON on its own), or None for a text-only answer."""
    m = re.search(r"```a2ui\s*(.*?)```", text, re.S)
    if m:
        body = m.group(1)
    else:
        s = text.strip()
        if not s.startswith(("[", "{")):
            return None
        body = s
    try:
        return json.loads(body)
    except ValueError as e:
        return {"__parse_error__": str(e)}


def cmd_validate(a):
    cat = _load_catalog(a.catalog)
    raw = sys.stdin.read() if a.answer == "-" else pathlib.Path(a.answer).read_text()
    ans = extract_answer(raw)
    if ans is None:
        print(json.dumps({"ok": True, "ui": False, "errors": [], "warnings": []}) if a.json else "Text only: nothing to validate.")
        return 0
    if isinstance(ans, dict) and "__parse_error__" in ans:
        r = {"ok": False, "errors": [{"code": "VALIDATION_FAILED", "rule": "json", "path": "", "message": "not JSON: " + ans["__parse_error__"], "surfaceId": ""}], "warnings": []}
    else:
        r = validate(ans, cat, {"partial": a.partial, "source": _load_json(a.source) if a.source else None,
                                "limits": {"leaves": a.max_parts}})
    if a.a2ui:
        for e in r["errors"]:
            print(json.dumps({"version": A2UI_VERSION, "error": {k: e[k] for k in ("code", "path", "message", "surfaceId")}}))
    elif a.json:
        print(json.dumps({k: r[k] for k in ("ok", "errors", "warnings")}, indent=1))
    else:
        for e in r["errors"]:
            print(f"{e['rule']:<18} {e['path'] or '/'}  {e['message']}" + (f"  Fix: {e['fix']}" if e.get("fix") else ""))
        for w in r["warnings"]:
            print(f"warning {w['rule']:<10} {w['path']}  {w['message']}")
        print("ok" if r["ok"] else f"{len(r['errors'])} error(s)")
    return 0 if r["ok"] else 1


# ----------------------------------------------------------------------------------------------- text fallback

def to_text(surfaces, cat):
    """Plain text for a host that renders no UI. The same walk as ODSmartUI.toText in od-surface.js."""
    out = []

    def val(v, s, indent):
        if isinstance(v, dict):
            if "label" in v and "event" in v:
                return []
            if "src" in v and "alt" in v:
                return [indent + f"[Image: {v['alt']}]"]
            parts, nested = [], []
            for k, x in v.items():
                if k.startswith("@") or k in ("component", "id", "children"):
                    continue
                ps = (s.get("properties") or {}).get(k, {})
                if isinstance(x, (str, int, float)) and not isinstance(x, bool) and not ps.get("x-od-token") and "enum" not in ps:
                    parts.append(str(x))
                elif isinstance(x, (list, dict)):
                    nested += val(x, ps, indent + ("  " if parts else ""))
            return ([indent + " · ".join(parts)] if parts else []) + nested
        if isinstance(v, list):
            lines = []
            for x in v:
                sub = val(x, s.get("items", {}), "")
                if sub:
                    lines.append(indent + "- " + sub[0].strip())
                    lines += [indent + "  " + y.strip() for y in sub[1:]]
            return lines
        return [indent + str(v)]

    for sid, s in surfaces.items():
        comps = s["components"]

        def walk(cid):
            c = comps.get(cid)
            if not c:
                return
            schema = cat["components"].get(c.get("component"), {})
            if od(schema).get("container"):
                for ch in c.get("children", []):
                    walk(ch)
            else:
                out.extend(val(c, schema, ""))
                out.append("")
        walk("root")
    return "\n".join(out).strip() + "\n"


def cmd_text(a):
    cat = _load_catalog(a.catalog)
    ans = extract_answer(pathlib.Path(a.answer).read_text())
    if ans is None:
        print(pathlib.Path(a.answer).read_text())
        return 0
    r = validate(ans, cat, {"partial": True})
    print(to_text(r["surfaces"], cat), end="")
    return 0


# ----------------------------------------------------------------------------------------------- scope

FRAMEWORKS = [("next", "Next.js"), ("react", "React"), ("vue", "Vue"), ("svelte", "Svelte"), ("@angular/core", "Angular"),
              ("solid-js", "Solid"), ("astro", "Astro"), ("lit", "Lit"), ("react-native", "React Native")]
CHAT_HINTS = re.compile(r"(chat|assistant|copilot|conversation|ai[-_ ]?(panel|bar|sidebar))", re.I)
AI_SDKS = [("ai", "Vercel AI SDK"), ("@ai-sdk/react", "Vercel AI SDK"), ("@copilotkit/react-core", "CopilotKit"), ("@assistant-ui/react", "assistant-ui"),
           ("openai", "OpenAI SDK"), ("@anthropic-ai/sdk", "Anthropic SDK"), ("@google/genai", "Google Gen AI SDK"), ("langchain", "LangChain"),
           ("@modelcontextprotocol/sdk", "MCP SDK"), ("@a2ui/lit", "A2UI"), ("anthropic", "Anthropic SDK (Python)"), ("openai", "OpenAI SDK (Python)")]
SKIP_DIRS = {"node_modules", ".git", "dist", "build", ".next", ".venv", "venv", "__pycache__", "opendesigner", ".worktrees", "coverage"}
# product types the scope step knows how to propose intents for; anything else gets "not known" and the person says
PRODUCT_INTENTS = json.loads((SKILL / "assets" / "intents.json").read_text()) if (SKILL / "assets" / "intents.json").exists() else {}


def _files(root, exts, limit=4000):
    n = 0
    for p in root.rglob("*"):
        if any(part in SKIP_DIRS or part.startswith(".") and part not in (".",) for part in p.relative_to(root).parts[:-1]):
            continue
        if p.is_file() and p.suffix in exts:
            yield p
            n += 1
            if n >= limit:
                return


def scope(root):
    root = pathlib.Path(root).resolve()
    found = {"project": str(root), "read": [], "not_known": []}
    # product and users: DESIGN.md / PRODUCT.md / the system's state
    st = _load_json(root / "opendesigner" / "state.json") or {}
    raw = st.get("raw", {}) if isinstance(st, dict) else {}
    answers = st.get("answers", {}) if isinstance(st, dict) else {}
    def ans(q):
        v = answers.get(q)
        return v.get("value") if isinstance(v, dict) else v
    product = ans("Q-scope-01")
    product = " ".join(product) if isinstance(product, list) else product
    audience = ans("Q-aud-01")
    for f in ("PRODUCT.md", "DESIGN.md"):
        if (root / f).exists():
            found["read"].append(f)
            t = (root / f).read_text(errors="ignore")
            if not product:
                m = re.search(r"(?im)^#+\s*product\s*\n+\s*([^\n#].+)$", t) or re.search(r"(?im)^\W*(?:product(?: type)?|what it is)\s*[:|]\s*(.+)$", t)
                if m and not re.match(r"(?i)not (recorded|enough)", m.group(1).strip()):
                    product = m.group(1).strip()[:160]
    product = product or raw.get("productType") or None
    found["product_type"] = raw.get("productType")
    if st:
        found["read"].append("opendesigner/state.json")
    found["product"] = product
    found["audience"] = audience
    found["system"] = st.get("name") if st else None
    # framework and AI SDKs: package.json, pyproject, requirements
    deps = {}
    for pj in [root / "package.json", *list(root.glob("*/package.json"))[:8]]:
        d = _load_json(pj)
        if isinstance(d, dict):
            found["read"].append(str(pj.relative_to(root)))
            for k in ("dependencies", "devDependencies"):
                deps.update(d.get(k) or {})
    pytext = ""
    for f in ("pyproject.toml", "requirements.txt"):
        if (root / f).exists():
            found["read"].append(f)
            pytext += (root / f).read_text(errors="ignore").lower()
    found["framework"] = next((label for key, label in FRAMEWORKS if key in deps), None) or \
        next((label for key, label in (("django", "Django"), ("flask", "Flask"), ("fastapi", "FastAPI"), ("rails", "Rails")) if key in pytext), None) or \
        ("plain HTML" if list(root.glob("*.html")) else None)
    found["ai_sdks"] = sorted({label for key, label in AI_SDKS if key in deps or (label.endswith("(Python)") and re.search(rf"^{key}\b", pytext, re.M))})
    # tokens
    toks = [p for p in (root / "opendesigner/build/css/tokens.css", root / "build/css/tokens.css") if p.exists()]
    if toks:
        found["tokens"] = {"file": str(toks[0].relative_to(root)), "kind": "opendesigner", "count": len(token_names(toks[0]))}
    else:
        css_vars = 0
        for p in _files(root, {".css", ".scss"}, 400):
            css_vars += len(re.findall(r"--[a-z][a-z0-9-]*\s*:", p.read_text(errors="ignore")))
        found["tokens"] = {"file": None, "kind": "own CSS variables" if css_vars else None, "count": css_vars}
        found["not_known"].append("an OpenDesigner system: run the opendesigner skill first, or map --ds-* to your variables (token-map.css)")
    # chat surface and actions
    chats, actions = [], []
    for p in _files(root, {".tsx", ".jsx", ".ts", ".js", ".vue", ".svelte", ".py", ".html", ".astro"}):
        rel = str(p.relative_to(root))
        if CHAT_HINTS.search(rel):
            chats.append(rel)
        try:
            t = p.read_text(errors="ignore")
        except OSError:
            continue
        for m in re.finditer(r"""(?:app|router|api|bp)\.(get|post|put|patch|delete)\(\s*["'`]([^"'`]+)""", t):
            actions.append({"kind": "route", "method": m.group(1).upper(), "path": m.group(2), "file": rel})
        for m in re.finditer(r"""@(?:app|router|bp)\.(get|post|put|patch|delete|route)\(\s*["']([^"']+)""", t):
            actions.append({"kind": "route", "method": m.group(1).upper(), "path": m.group(2), "file": rel})
        for m in re.finditer(r"""\btool\(\s*\{[^}]*?description|\bname:\s*["'`]([a-z][a-z0-9_]+)["'`],\s*description""", t):
            if m.group(1):
                actions.append({"kind": "tool", "name": m.group(1), "file": rel})
        if re.search(r"export\s+(async\s+)?function\s+(GET|POST|PUT|PATCH|DELETE)\b", t) and "/api/" in "/" + rel:
            for meth in re.findall(r"export\s+(?:async\s+)?function\s+(GET|POST|PUT|PATCH|DELETE)\b", t):
                actions.append({"kind": "route", "method": meth, "path": "/" + rel.split("app/", 1)[-1].rsplit("/route.", 1)[0], "file": rel})
    found["chat_surface"] = sorted(set(chats))[:10]
    if not chats:
        found["not_known"].append("where the assistant lives (no chat or assistant file found)")
    found["actions"] = actions[:60]
    for a in found["actions"]:
        a["changes_data"] = a.get("method") in ("POST", "PUT", "PATCH", "DELETE")
    if not product:
        found["not_known"].append("the product type (no PRODUCT.md, DESIGN.md or system state says it)")
    if not audience:
        found["not_known"].append("who uses it (Q-aud-01 is not answered)")
    found["intents"] = propose_intents(product, found["actions"])
    found["components_proposed"] = sorted({c for it in found["intents"] for c in it["components"]})
    found["components_confirmed"] = []
    return found


def propose_intents(product, actions):
    """Intents from the product type (assets/intents.json), plus one per action the assistant could take."""
    key = None
    p = (product or "").lower()
    for k, v in PRODUCT_INTENTS.items():
        if k == p or any(w in p for w in v.get("match", [])):
            key = k
            break
    out = []
    for it in (PRODUCT_INTENTS.get(key, {}).get("intents", []) if key else []):
        out.append({**it, "from": f"product type {key}"})
    for a in actions:
        if a.get("kind") == "route" and a.get("changes_data"):
            out.append({"intent": f"{a['method']} {a['path']}", "phrases": [], "components": ["ApprovalPrompt", "Receipt", "ErrorRetry"],
                        "from": f"route in {a['file']}"})
        elif a.get("kind") == "tool":
            out.append({"intent": f"tool {a['name']}", "phrases": [], "components": [], "from": f"tool in {a['file']}"})
    if not key:
        out.insert(0, {"intent": "not known", "phrases": [], "components": [], "from": "the product type is not known: ask what the assistant must answer"})
    return out


def cmd_scope(a):
    s = scope(a.project)
    if a.write:
        out = pathlib.Path(a.project) / "opendesigner" / "smart-ui"
        out.mkdir(parents=True, exist_ok=True)
        old = _load_json(out / "scope.json") or {}
        s["components_confirmed"] = old.get("components_confirmed", [])
        (out / "scope.json").write_text(json.dumps(s, indent=1) + "\n")
    if a.json:
        print(json.dumps(s, indent=1))
        return 0
    print(f"Product: {s['product'] or 'not known'} · users: {s['audience'] or 'not known'} · framework: {s['framework'] or 'not known'}")
    print(f"AI in the code: {', '.join(s['ai_sdks']) or 'none found'} · chat surface: {', '.join(s['chat_surface'][:3]) or 'not found'}")
    t = s["tokens"]
    print(f"Tokens: {t['file'] or t['kind'] or 'none found'} ({t['count']} variables)")
    print(f"Actions found: {len(s['actions'])} ({sum(x.get('changes_data', False) for x in s['actions'])} change data)")
    print("Proposed intents:")
    for it in s["intents"]:
        print(f"  - {it['intent']}: {', '.join(it['components']) or '(choose)'}   [{it['from']}]")
    for n in s["not_known"]:
        print(f"Not known: {n}")
    print("Confirm the components with: smartui.py confirm <Name,Name,...>" if a.write else "Add --write to save this as opendesigner/smart-ui/scope.json")
    return 0


def cmd_confirm(a):
    p = pathlib.Path(a.project) / "opendesigner" / "smart-ui" / "scope.json"
    s = _load_json(p)
    if not s:
        print("No scope.json yet. Run: smartui.py scope --write")
        return 1
    names = [n.strip() for n in a.names.split(",") if n.strip()]
    known = {c["as"]: c["slug"] for c in load_set()["components"]}
    bad = [n for n in names if n not in known and n not in known.values()]
    if bad:
        print("Not in the Smart UI set: " + ", ".join(bad) + ". Known: " + ", ".join(known))
        return 1
    s["components_confirmed"] = sorted({known.get(n, n) for n in names})
    s["confirmed_on"] = datetime.date.today().isoformat()
    p.write_text(json.dumps(s, indent=1) + "\n")
    print(f"Confirmed {len(s['components_confirmed'])} components. Next: smartui.py catalog")
    return 0


# ----------------------------------------------------------------------------------------------- audit

def cmd_audit(a):
    try:
        import surface_audit as audit  # noqa: F401  (scripts/surface_audit.py: the Playwright driver)
    except ImportError as e:
        print(f"Audit needs scripts/surface_audit.py and Playwright for Python ({e}). Install Playwright yourself if you want this; the skill never installs it.")
        return 2
    return audit.run(a)


# ----------------------------------------------------------------------------------------------- main

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    dflt = "opendesigner/smart-ui"
    p = sub.add_parser("scope")
    p.add_argument("--project", default=".")
    p.add_argument("--json", action="store_true")
    p.add_argument("--write", action="store_true", help="save opendesigner/smart-ui/scope.json")
    p = sub.add_parser("confirm", help="record the components the person confirmed")
    p.add_argument("names")
    p.add_argument("--project", default=".")
    p = sub.add_parser("catalog")
    p.add_argument("--tokens", default="opendesigner/build/css/tokens.css")
    p.add_argument("--out", default=dflt)
    p.add_argument("--system")
    p.add_argument("--allow-images", nargs="*", help="image hosts, for example images.example.com or *.cdn.example")
    p.add_argument("--allow-links", nargs="*")
    p.add_argument("--all", action="store_true", help="every component in the set, not only the confirmed ones")
    p.add_argument("--library", action="store_true", help="also every other marked library part (for auditing the library)")
    p = sub.add_parser("view", help="one self-contained HTML file: tokens, renderer, parts, catalog (the MCP Apps view)")
    p.add_argument("--out", default=dflt)
    p.add_argument("--tokens", default="opendesigner/build/css/tokens.css")
    p.add_argument("--answer", help="an answer to show in it")
    p.add_argument("--write", help="where to write it (default <out>/surface.html)")
    p = sub.add_parser("components", help="the parts by job (references/components.md)")
    p.add_argument("--write", action="store_true")
    p.add_argument("--check", action="store_true")
    p = sub.add_parser("prompt")
    p.add_argument("--for", dest="for_", required=True)
    p.add_argument("--catalog", default=f"{dflt}/catalog.json")
    p.add_argument("--data")
    p.add_argument("--k", type=int, default=3)
    p.add_argument("--json", action="store_true", help="only the selection")
    p = sub.add_parser("validate")
    p.add_argument("answer", help="a file with the model's reply or A2UI JSON, or - for stdin")
    p.add_argument("--catalog", default=f"{dflt}/catalog.json")
    p.add_argument("--source", help="the data the model was given: every number must come from it (R6)")
    p.add_argument("--partial", action="store_true", help="a streamed answer that is not finished")
    p.add_argument("--max-parts", type=int, help="more than one part, when the person asked for more (R2)")
    p.add_argument("--a2ui", action="store_true", help="print A2UI error messages for the agent")
    p.add_argument("--json", action="store_true")
    p = sub.add_parser("text")
    p.add_argument("answer")
    p.add_argument("--catalog", default=f"{dflt}/catalog.json")
    p = sub.add_parser("audit")
    p.add_argument("--catalog", default=f"{dflt}/catalog.json")
    p.add_argument("--tokens", default="opendesigner/build/css/tokens.css")
    p.add_argument("--answer", action="append", help="an answer file to render (repeatable)")
    p.add_argument("--fixtures", action="store_true", help="every component's state fixtures")
    p.add_argument("--only")
    p.add_argument("--out", default=f"{dflt}/audit")
    p.add_argument("--envs", help="some of: " + "desktop,phone,phone-320,text-200,dark,dark-phone,rtl,reduced-motion")
    p.add_argument("--no-shots", action="store_true", help="no screenshots (saves disk)")
    p.add_argument("--ledger", action="store_true", help="record each failure with engine.py ledger (asks nothing; read the report first)")
    a = ap.parse_args(argv)
    return {"scope": cmd_scope, "confirm": cmd_confirm, "catalog": cmd_catalog, "prompt": cmd_prompt, "validate": cmd_validate,
            "text": cmd_text, "audit": cmd_audit, "view": cmd_view, "components": cmd_components}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
