#!/usr/bin/env python3
"""Slot marks: the variable parts of a library component, marked in its component.html.

A mark is an attribute. It changes nothing visible; it tells a renderer (Smart UI's <od-surface>) and the catalog
(library.json, Smart UI's catalog.json) which parts of the sample markup hold data.

  data-od-slot="name"      plain text, set with textContent only (the element holds no other elements)
  data-od-list="name"      repeated items; children marked data-od-item are copies, the first is the template
  data-od-item             one item of the nearest list
  data-od-template         on one item that also carries hidden: the full item with every part, kept out of sight in
                           the static file; a renderer repeats it (without it, the first item is the template)
  data-od-var="name"       an enum; the element also carries data-<name>="value", and the allowed values are
                           the ones the component's CSS styles ([data-name="x"])
  data-od-media="name"     an <img>; data gives {src, alt}
  data-od-action="name"    a <button> or <a> the person presses; data gives {label, event}. data-od-effect="change"
                           marks one that changes data (book, pay, send, delete): Smart UI asks for approval first
  data-od-input="name"     an <input>, <select> or <textarea>: its name attribute is the data property "name" of
                           this scope; value, required, min, max and (for a select) options [{label, value}] come from
                           the same scope's data
  data-od-measure="name"   a number; the renderer sets --od-ratio (0 to 1) on the element, for bars and meters
  data-od-label="name"     aria-label of this element comes from the named data property (shown or not)
  data-od-when="name=a|b"  this element is kept only when the enum property name (in this scope) is a or b
  data-od-optional         this element is hidden when none of the slots inside it have a value
  data-od-sample           sample-only decoration (a lighter cents part, an example badge); a renderer removes it

Names are scoped: inside a list item or an action, names belong to that item or action. Inside an action, a slot
named "label" is the action's label. Names match ^[a-z][a-z0-9_]*$ and reuse the property names in the component's
meta.json spec.data, so data keys and marks line up.

  python3 slots.py show <component.html>     the marks as a tree (JSON)
  python3 slots.py check <component.html>    the mark rules; exit 1 on errors
Standard library only.
"""
import html.parser
import json
import pathlib
import re
import sys

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
NAME = re.compile(r"^[a-z][a-z0-9_]*$")
MARKS = ("data-od-slot", "data-od-list", "data-od-item", "data-od-var", "data-od-media", "data-od-action",
         "data-od-measure", "data-od-label", "data-od-optional", "data-od-sample", "data-od-effect", "data-od-when", "data-od-template", "data-od-input")
SVG_INSIDE = {"svg", "path", "circle", "rect", "line", "polyline", "polygon", "ellipse", "g", "use", "defs", "title"}


class El:
    __slots__ = ("tag", "attrs", "children", "parent", "text", "line")

    def __init__(self, tag, attrs, parent, line):
        self.tag, self.attrs, self.parent, self.children, self.text, self.line = tag, dict(attrs), parent, [], [], line

    def walk(self):
        for c in self.children:
            yield c
            yield from c.walk()

    def own_text(self):
        return "".join(self.text).strip()

    def all_text(self):
        return " ".join([self.own_text()] + [c.all_text() for c in self.children if c.tag not in SVG_INSIDE]).strip()


class _Builder(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = El("#root", {}, None, 0)
        self.cur = self.root
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("style", "script"):
            self.skip += 1
            return
        el = El(tag, [(k, v if v is not None else "") for k, v in attrs], self.cur, self.getpos()[0])
        self.cur.children.append(el)
        if tag not in VOID:
            self.cur = el

    def handle_startendtag(self, tag, attrs):
        el = El(tag, [(k, v if v is not None else "") for k, v in attrs], self.cur, self.getpos()[0])
        self.cur.children.append(el)

    def handle_endtag(self, tag):
        if tag in ("style", "script"):
            self.skip = max(0, self.skip - 1)
            return
        n = self.cur
        while n is not self.root and n.tag != tag:
            n = n.parent
        if n is not self.root:
            self.cur = n.parent

    def handle_data(self, data):
        if not self.skip:
            self.cur.text.append(data)


def parse(src):
    b = _Builder()
    b.feed(src)
    b.close()
    return b.root


def has_marks(src):
    return "data-od-" in re.sub(r"<style>.*?</style>|<script>.*?</script>", "", src, flags=re.S)


def _scope_children(el):
    """Marked elements in this scope, not descending into a list item, an action or a sample."""
    for c in el.children:
        if "data-od-sample" in c.attrs:
            continue
        yield c
        if "data-od-item" in c.attrs or "data-od-action" in c.attrs or "data-od-list" in c.attrs:
            continue
        yield from _scope_children(c)


class _Self:
    """A list item read as part of its own scope: its own marks count, but not item/list/action (no recursion)."""
    def __init__(self, el):
        self.tag, self.line, self.children = el.tag, el.line, el.children
        self.attrs = {k: v for k, v in el.attrs.items() if k not in ("data-od-item", "data-od-list", "data-od-action", "data-od-template")}


def _node(el, kind, name):
    return {"kind": kind, "name": name, "tag": el.tag, "line": el.line}


def _read_scope(el, include_self=False):
    out = []
    for c in ([el] if include_self else []) + list(_scope_children(el)):
        if c is el and include_self:
            c = _Self(el)
        a = c.attrs
        if "data-od-slot" in a:
            n = _node(c, "text", a["data-od-slot"])
            n["optional"] = "data-od-optional" in a
            out.append(n)
        if "data-od-var" in a:
            n = _node(c, "var", a["data-od-var"])
            n["value"] = a.get("data-" + a["data-od-var"])
            out.append(n)
        if "data-od-media" in a:
            out.append(_node(c, "media", a["data-od-media"]))
        if "data-od-measure" in a:
            out.append(_node(c, "measure", a["data-od-measure"]))
        if "data-od-label" in a:
            out.append(_node(c, "label", a["data-od-label"]))
        if "data-od-input" in a:
            out.append(_node(c, "input", a["data-od-input"]))
        if "data-od-when" in a:
            n = _node(c, "when", a["data-od-when"].split("=")[0])
            n["values"] = a["data-od-when"].split("=", 1)[1].split("|") if "=" in a["data-od-when"] else []
            out.append(n)
        if "data-od-optional" in a and "data-od-slot" not in a:
            out.append(_node(c, "optional", ""))
        if "data-od-action" in a:
            n = _node(c, "action", a["data-od-action"])
            n["effect"] = a.get("data-od-effect", "none")
            n["children"] = _read_scope(c)
            out.append(n)
        if "data-od-list" in a:
            n = _node(c, "list", a["data-od-list"])
            items = [i for i in c.children if "data-od-item" in i.attrs]
            items.sort(key=lambda i: "data-od-template" not in i.attrs)
            n["items"] = len(items)
            n["children"] = _read_scope(items[0], include_self=True) if items else []
            n["item_tag"] = items[0].tag if items else None
            out.append(n)
    return out


def read_marks(src):
    """The marks of one component as a tree: [{kind, name, tag, line, ...}], lists and actions with children."""
    return _read_scope(parse(src))


def css_values(css, name):
    """The values the CSS styles for data-<name> (from [data-name="x"] selectors)."""
    return sorted(set(re.findall(r'\[data-' + re.escape(name) + r'="([^"]+)"\]', css)))


def parts(src, root_class):
    """S5's library.json "parts" for a marked component, in reading order: name, selector, slot kind."""
    kind = {"text": "text", "list": "list", "media": "media", "action": "action", "measure": "number", "var": "none"}
    attr = {"text": "data-od-slot", "list": "data-od-list", "media": "data-od-media", "action": "data-od-action",
            "measure": "data-od-measure", "var": "data-od-var"}
    out = []

    def walk(nodes, prefix):
        for n in nodes:
            if n["kind"] not in kind:
                continue
            out.append({"name": prefix + n["name"], "selector": f'{root_class} [{attr[n["kind"]]}="{n["name"]}"]',
                        "slot": kind[n["kind"]]})
            if n["kind"] in ("list", "action"):
                walk(n.get("children", []), prefix + n["name"] + ("[]." if n["kind"] == "list" else "."))
    walk(read_marks(src), "")
    return out


def check_marks(src, css=None):
    """Errors in the marks of one component (empty when it has none, or when they are right)."""
    if css is None:
        css = "".join(re.findall(r"<style>(.*?)</style>", src, re.S))
    root = parse(src)
    errs = []
    for el in root.walk():
        a = el.attrs
        for k in a:
            if k.startswith("data-od-") and k not in MARKS:
                errs.append(f"line {el.line}: unknown mark {k}")
        for k in ("data-od-slot", "data-od-list", "data-od-var", "data-od-media", "data-od-action", "data-od-measure", "data-od-label", "data-od-input"):
            if k in a and not NAME.match(a[k] or ""):
                errs.append(f"line {el.line}: {k}={a[k]!r} is not a name (lower case, digits, underscores)")
        if "data-od-slot" in a:
            kids = [c for c in el.children if "data-od-sample" not in c.attrs]
            if kids:
                errs.append(f"line {el.line}: slot {a['data-od-slot']} holds elements ({kids[0].tag}); a slot holds text only, so wrap the text in its own element")
        if "data-od-when" in a and not re.match(r"^[a-z][a-z0-9_]*=[a-z0-9_-]+(\|[a-z0-9_-]+)*$", a["data-od-when"]):
            errs.append(f"line {el.line}: data-od-when={a['data-od-when']!r} is not name=value or name=a|b")
        if "data-od-action" in a:
            inner = [c for c in el.children if c.tag not in SVG_INSIDE and "data-od-sample" not in c.attrs]
            if inner and not any(c.attrs.get("data-od-slot") == "label" for c in el.walk()):
                errs.append(f"line {el.line}: action {a['data-od-action']} holds elements, so it needs a data-od-slot=\"label\" inside for its label")
        if "data-od-input" in a and el.tag not in ("input", "select", "textarea"):
            errs.append(f"line {el.line}: data-od-input goes on an <input>, <select> or <textarea>, not <{el.tag}>")
        if "data-od-media" in a and el.tag != "img":
            errs.append(f"line {el.line}: data-od-media goes on an <img>, not <{el.tag}>")
        if "data-od-action" in a and el.tag not in ("button", "a"):
            errs.append(f"line {el.line}: data-od-action goes on a <button> or <a>, not <{el.tag}>")
        if "data-od-effect" in a and (a["data-od-effect"] not in ("change", "none") or "data-od-action" not in a):
            errs.append(f"line {el.line}: data-od-effect is change or none, on an action")
        if "data-od-item" in a and (el.parent is None or "data-od-list" not in el.parent.attrs):
            errs.append(f"line {el.line}: data-od-item must be a direct child of a data-od-list")
        if "data-od-template" in a and ("data-od-item" not in a or "hidden" not in a):
            errs.append(f"line {el.line}: data-od-template goes on a data-od-item that is also hidden")
        if "data-od-list" in a and sum("data-od-template" in c.attrs for c in el.children) > 1:
            errs.append(f"line {el.line}: list {a['data-od-list']} has more than one data-od-template")
        if "data-od-list" in a and not any("data-od-item" in c.attrs for c in el.children):
            errs.append(f"line {el.line}: list {a['data-od-list']} has no data-od-item child to repeat")
        if "data-od-var" in a:
            v = a["data-od-var"]
            if ("data-" + v) not in a:
                errs.append(f"line {el.line}: var {v} needs data-{v}=\"<current value>\" on the same element")
            vals = css_values(css, v)
            if len(vals) < 2:
                errs.append(f"line {el.line}: var {v}: the CSS styles {len(vals)} value(s) of [data-{v}]; an enum needs at least two")
            elif a.get("data-" + v) not in vals:
                errs.append(f"line {el.line}: var {v}: current value {a.get('data-' + v)!r} is not one the CSS styles ({', '.join(vals)})")
        if "data-od-measure" in a and "--od-ratio" not in css:
            errs.append(f"line {el.line}: measure {a['data-od-measure']}: the CSS never reads var(--od-ratio)")

    def scope(nodes, where):
        seen = {}
        for n in nodes:
            if n["kind"] in ("optional",):
                continue
            key = (n["kind"] if n["kind"] != "measure" else "measure", n["name"])
            if n["kind"] in ("text", "list", "media", "action", "var") and key in seen:
                errs.append(f"line {n['line']}: {n['kind']} {n['name']} appears twice in {where}")
            seen[key] = n
        for n in nodes:
            if n["kind"] == "action":
                scope(n.get("children", []), f"action {n['name']}")
            if n["kind"] == "list":
                if not n.get("children"):
                    errs.append(f"line {n['line']}: list {n['name']}: its item has no marks")
                scope(n.get("children", []), f"list {n['name']}")
    scope(_read_scope(root), "the component")
    return errs


def schema_names(nodes):
    """The data names the marks expect, as {name: kind or nested dict}."""
    out = {}
    for n in nodes:
        if n["kind"] in ("text", "media", "measure", "var", "label", "when", "input"):
            out.setdefault(n["name"], n["kind"])
        elif n["kind"] in ("list", "action"):
            out[n["name"]] = {"kind": n["kind"], "of": schema_names(n.get("children", []))}
    return out


def check_against_spec(src, data):
    """Every mark names a property in the component's spec.data, at the same scope (nothing to compare without one)."""
    errs = []
    if not data:
        return errs

    def walk(names, props, where):
        for k, v in names.items():
            if isinstance(v, dict) and v["kind"] == "action":
                if k not in props:
                    errs.append(f"action {k} is not a property in spec.data ({where})")
                continue
            if k not in props:
                errs.append(f"mark {k} is not a property in spec.data ({where})")
                continue
            if isinstance(v, dict):
                items = props[k].get("items", {})
                walk(v["of"], items.get("properties", {}), f"{where}.{k}[]")
    walk(schema_names(read_marks(src)), (data or {}).get("properties", {}), "root")
    return errs


def main(argv):
    if len(argv) != 3 or argv[1] not in ("show", "check"):
        print(__doc__)
        return 2
    src = pathlib.Path(argv[2]).read_text()
    if argv[1] == "show":
        print(json.dumps(read_marks(src), indent=1))
        return 0
    errs = check_marks(src)
    print("\n".join(errs) or "marks ok")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
