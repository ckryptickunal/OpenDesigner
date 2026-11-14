#!/usr/bin/env python3
"""Bring each library part's meta.json spec in step with its slot marks.

  python3 tools/sync_spec_states.py           write the changes
  python3 tools/sync_spec_states.py --check   report what is out of step; exit 1 if anything is

For every component with slot marks:
  - spec.data gets each marked property it lacks: text up to 80 characters, a number for a bar or meter, a photo as
    {src, alt}, a list of up to 12 items, an enum of the values the CSS styles. Authored properties are never changed.
  - spec.edge.missing_image: "none" when the file has no <img>; "handled" when its photos are data-od-media (the Smart UI
    renderer swaps a photo that fails for a block of the same size with its alt text); otherwise "not_built".
  - spec.edge.loading, and spec.edge.empty when the part has a list, are "handled" when they were "not_built": the Smart
    UI renderer draws loading rows from the marks and one plain line in an empty list. The "how" says so; the static file
    still shows neither.
Standard library only.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
LIB = ROOT / "skills" / "opendesigner" / "assets" / "library" / "components"
sys.path.insert(0, str(ROOT / "skills" / "opendesigner" / "scripts"))
import slots  # noqa: E402


def prop_for(n, css):
    k = n["kind"]
    if k == "text":
        return {"type": "string", "maxLength": 80}
    if k == "label":
        return {"type": "string", "maxLength": 120}
    if k == "measure":
        return {"type": "number"}
    if k == "media":
        return {"type": "object", "required": ["src", "alt"],
                "properties": {"src": {"type": "string", "maxLength": 2048}, "alt": {"type": "string", "maxLength": 200}}}
    if k == "var":
        vals = slots.css_values(css, n["name"])
        return {"enum": vals} if vals else None
    if k == "when":
        return {"enum": n.get("values", [])} if n.get("values") else None
    if k == "input":
        return {"type": "string", "maxLength": 40}
    if k == "list":
        return {"type": "array", "minItems": 0, "maxItems": 12, "items": {"type": "object", "properties": {}}}
    return None


def sync_data(nodes, schema, css, where, changes):
    props = schema.setdefault("properties", {})
    for n in nodes:
        if n["kind"] in ("optional", "action"):
            continue  # buttons are parts in the spec, not data
        name = n["name"]
        if name not in props:
            p = prop_for(n, css)
            if p is None:
                continue
            props[name] = p
            changes.append(f"{where}{name}")
        if n["kind"] == "list" and props[name].get("type") == "array":
            items = props[name].setdefault("items", {"type": "object", "properties": {}})
            kids = [c for c in n.get("children", []) if c["kind"] in ("text", "measure", "media", "var", "label", "input")]
            if items.get("type") != "object" and kids:
                # the spec said "a list of strings (or numbers)"; the marks hold each item's values in slots: items become
                # objects, and a single slot keeps the spec's own limits
                one = {k: v for k, v in items.items() if k != "part"} if len({c["name"] for c in kids}) == 1 else None
                props[name]["items"] = items = {"type": "object", "properties": {}}
                if one:
                    items["properties"][kids[0]["name"]] = one
                changes.append(f"{where}{name}[] as objects")
            if items.get("type") == "object":
                sync_data(n.get("children", []), items, css, f"{where}{name}[].", changes)


def sync(d):
    src = (d / "component.html").read_text()
    if not slots.has_marks(src):
        return None, []
    raw = (d / "meta.json").read_text()
    meta = json.loads(raw)
    css = "".join(re.findall(r"<style>(.*?)</style>", src, re.S))
    sp = meta.setdefault("spec", {})
    data = sp.setdefault("data", {"type": "object", "properties": {}})
    data.setdefault("type", "object")
    changes = []
    sync_data(slots.read_marks(src), data, css, "data.", changes)

    def limit(node, path):  # every string needs a length limit (a photo's address included)
        if isinstance(node, dict):
            if node.get("type") == "string" and "maxLength" not in node and "enum" not in node:
                node["maxLength"] = 2048 if path.endswith("src") else 120
                changes.append(f"{path} maxLength")
            for k, v in (node.get("properties") or {}).items():
                limit(v, f"{path}.{k}")
            if isinstance(node.get("items"), dict):
                limit(node["items"], f"{path}[]")
    limit(data, "data")
    edge = sp.setdefault("edge", {})
    has_img = "<img" in src
    if "missing_image" not in edge:
        if not has_img:
            edge["missing_image"] = {"status": "none", "how": "the part has no photo"}
        elif "data-od-media" in src:
            edge["missing_image"] = {"status": "handled", "evidence": "data-od-media",
                                     "how": "the Smart UI renderer swaps a photo that fails to load for a block of the same size with its alt text"}
        else:
            edge["missing_image"] = {"status": "not_built", "how": "a photo that fails to load shows the browser's broken image"}
        changes.append("edge.missing_image")
    if edge.get("loading", {}).get("status", "not_built") == "not_built" and "data-od-slot" in src:
        edge["loading"] = {"status": "handled", "evidence": "data-od-slot",
                           "how": "the Smart UI renderer draws each marked slot as a quiet block of its size while the data arrives; the static file shows the filled part"}
        changes.append("edge.loading")
    if "data-od-list" in src and edge.get("empty", {}).get("status", "not_built") == "not_built":
        edge["empty"] = {"status": "handled", "evidence": "data-od-list",
                         "how": "the Smart UI renderer puts one plain 'Nothing to show yet.' line in an empty list"}
        changes.append("edge.empty")
    indent = len(re.match(r"\{\n( +)", raw).group(1)) if re.match(r"\{\n( +)", raw) else 1
    return (meta, indent), changes


def main():
    check = "--check" in sys.argv
    total = 0
    for d in sorted(p for p in LIB.iterdir() if (p / "meta.json").exists()):
        res, changes = sync(d)
        if not changes:
            continue
        total += 1
        print(f"{d.name}: {', '.join(changes)}")
        if not check:
            meta, indent = res
            (d / "meta.json").write_text(json.dumps(meta, indent=indent, ensure_ascii=False) + "\n")
    print(f"{total} parts {'out of step' if check else 'updated'}")
    return 1 if check and total else 0


if __name__ == "__main__":
    sys.exit(main())
