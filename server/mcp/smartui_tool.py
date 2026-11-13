"""Smart UI for the OpenDesigner MCP server: the show_ui tool and the ui://opendesigner/surface view (MCP Apps).

show_ui takes an answer as A2UI v1.0 messages, checks it with the Smart UI validator against the project's own
catalog, and returns it as structuredContent for the view to draw, with the plain-text version as content (what a
host without views shows, and what the model reads). It stays read-only: data in, view out. An action the person
presses in the view comes back to the chat as an "OD:action <name> <context>" message; nothing runs in the server.

The project: OD_PROJECT (or the server's working folder) with opendesigner/smart-ui/catalog.json and
od-components.js (smartui.py catalog) and opendesigner/build/css/tokens.css. server.py registers TOOL and VIEW.
"""
import html
import json
import os
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
SMART = pathlib.Path(os.environ.get("OD_SMARTUI_DIR") or HERE.parent.parent / "skills" / "opendesigner-smart-ui").resolve()
sys.path.insert(0, str(SMART / "scripts"))
import smartui  # noqa: E402

SURFACE_URI = "ui://opendesigner/surface"


class NoCatalog(Exception):
    pass


def project():
    return pathlib.Path(os.environ.get("OD_PROJECT") or os.getcwd()).resolve()


def load():
    d = project() / "opendesigner" / "smart-ui"
    cat_f, comp_f, tok_f = d / "catalog.json", d / "od-components.js", project() / "opendesigner" / "build" / "css" / "tokens.css"
    if not (cat_f.exists() and comp_f.exists() and tok_f.exists()):
        raise NoCatalog(f"No Smart UI catalog in {project()}. Run there: python3 {SMART}/scripts/smartui.py catalog "
                        "(it needs opendesigner/build/css/tokens.css from the opendesigner skill).")
    return json.loads(cat_f.read_text()), comp_f.read_text(), tok_f.read_text()


def csp():
    try:
        cat = load()[0]
    except NoCatalog:
        return {"connectDomains": [], "resourceDomains": [], "frameDomains": []}
    hosts = smartui.od(cat).get("allow", {}).get("images", [])
    return {"connectDomains": [], "resourceDomains": ["https://" + h for h in hosts], "frameDomains": []}


def view_text():
    try:
        cat, comps, tokens = load()
    except NoCatalog as e:
        return f"<!doctype html><meta charset=utf-8><p style='font:14px system-ui'>{html.escape(str(e))}</p>"
    return smartui.view_html(cat, comps, tokens)


def show_ui(args, tool_error):
    """fn for server.py: (structuredContent, text), or tool_error(message) for the model to repair."""
    try:
        cat = load()[0]
    except NoCatalog as e:
        raise tool_error(str(e))
    answer = args.get("answer")
    r = smartui.validate(answer, cat, {"source": args.get("source"), "limits": {"leaves": args.get("max_parts")}})
    if not r["ok"]:
        lines = [json.dumps({"version": "1.0", "error": {k: e[k] for k in ("code", "path", "message", "surfaceId")}}) + (f"  fix: {e['fix']}" if e.get("fix") else "")
                 for e in r["errors"][:12]]
        raise tool_error("The answer was not shown: it does not pass the Smart UI checks. Fix these and call show_ui again, "
                         "or answer in text:\n" + "\n".join(lines))
    text = smartui.to_text(r["surfaces"], cat).strip() or "(shown)"
    # R7: the host's look only when the owner turned it on (smartui.py catalog --host-look); the model can't
    return {"answer": answer, "catalogId": cat["catalogId"], "host_look": bool(smartui.od(cat).get("host_look"))}, text


TOOL = {
    "name": "show_ui",
    "title": "Show an answer as interface",
    "description": "Show one part of the person's own design system (a table, a comparison, a form, a booking step) filled with "
                   "your answer's data. Pass A2UI v1.0 messages built from the project's Smart UI catalog "
                   "(resource od://smart-ui/catalog). Use it only when a part does a job text cannot; a short answer stays text. "
                   "It checks the answer first and returns errors you can fix. Buttons the person presses come back as "
                   "'OD:action <name> <context>' messages; nothing happens on its own.",
    "inputSchema": {"type": "object", "additionalProperties": False, "required": ["answer"], "properties": {
        "answer": {"type": "array", "minItems": 1, "maxItems": 8, "description": "A2UI v1.0 messages: createSurface (and updateComponents)"},
        "source": {"type": "object", "description": "the data you were given; every number shown must come from it (the server can only check against what you pass)"},
        "max_parts": {"type": "integer", "minimum": 1, "maximum": 4, "description": "more than one part, only when the person asked for more"},
        }},
    "ui": SURFACE_URI,
}

VIEW = {"uri": SURFACE_URI, "name": "smart-ui-surface", "title": "Smart UI answer",
        "description": "Draws a show_ui answer with the project's own tokens and library parts.", "render": view_text, "csp": csp}


def catalog_resource():
    return {"uri": "od://smart-ui/catalog", "name": "smart-ui-catalog", "title": "Smart UI catalog (A2UI v1.0)", "mimeType": "application/json",
            "description": "The parts show_ui accepts, with their properties: the project's opendesigner/smart-ui/catalog.json."}


def catalog_text():
    try:
        return json.dumps(load()[0], ensure_ascii=False)
    except NoCatalog as e:
        return json.dumps({"error": str(e)})
