#!/usr/bin/env python3
"""Split an atlas artboard into Paper write_html chunks.

Paper builds designs from inline-styled HTML, one visual group per write. An element whose HTML fits under
LIMIT is written whole into its parent; a larger one is written as an empty shell and its children are
chunked into it. Output: JSON list of {id, parent, html} in write order; parent null means the artboard.

  python3 design/atlas/paper_plan.py design/atlas/04-builder-concept.html > plan.json
"""
import json, re, sys
from html.parser import HTMLParser

LIMIT = 15000
VOID = {"br", "img", "hr", "input", "meta", "link", "path", "circle", "rect", "line", "polyline", "polygon", "ellipse", "stop", "use"}


class Tree(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=False)
        self.text, self.root, self.stack = text, {"children": []}, []
        self.stack.append(self.root)
        self.lines = [0]
        for line in text.splitlines(keepends=True):
            self.lines.append(self.lines[-1] + len(line))

    def pos(self):
        line, col = self.getpos()
        return self.lines[line - 1] + col

    def handle_starttag(self, tag, attrs):
        start = self.pos()
        node = {"tag": tag, "start": start, "open_end": start + len(self.get_starttag_text()), "children": []}
        self.stack[-1]["children"].append(node)
        if tag in VOID or self.get_starttag_text().endswith("/>"):
            node["end"] = node["open_end"]
        else:
            self.stack.append(node)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i]["tag"] == tag:
                for n in self.stack[i:]:
                    n["end"] = self.pos() + len(f"</{n['tag']}>") if n is self.stack[i] else n.get("end", self.pos())
                del self.stack[i:]
                return


def clean(html):
    """Paper does not support margin: turn vertical margins into padding and drop hairline side margins."""
    html = re.sub(r"margin-top:\s*(\d+px)", r"padding-top:\1", html)
    html = re.sub(r"margin:\s*0 1px;?", "", html)
    return html


def plan(path):
    text = open(path).read()
    t = Tree(text)
    t.feed(text)
    board = next(n for n in _walk(t.root) if 'data-artboard' in text[n["start"]:n["open_end"]])
    style = re.search(r'style="([^"]*)"', text[board["start"]:board["open_end"]]).group(1)
    out = []

    def emit(node, parent):
        src = text[node["start"]:node["end"]]
        nid = f"n{len(out)}"
        if len(src) <= LIMIT or not node["children"]:
            out.append({"id": nid, "parent": parent, "html": clean(src)})
            return
        shell = text[node["start"]:node["open_end"]] + f"</{node['tag']}>"
        out.append({"id": nid, "parent": parent, "html": clean(shell)})
        emit_children(node["children"], nid)

    def emit_children(children, parent):
        """Batch neighbouring small siblings into one write; recurse into any sibling that is too big alone."""
        batch = ""
        for child in children:
            src = text[child["start"]:child["end"]]
            if len(src) > LIMIT and child["children"]:
                if batch:
                    out.append({"id": f"n{len(out)}", "parent": parent, "html": clean(batch)}); batch = ""
                emit(child, parent)
            elif len(batch) + len(src) > LIMIT:
                out.append({"id": f"n{len(out)}", "parent": parent, "html": clean(batch)}); batch = src
            else:
                batch += src
        if batch:
            out.append({"id": f"n{len(out)}", "parent": parent, "html": clean(batch)})

    emit_children(board["children"], None)
    return {"artboard_style": style, "name": re.search(r"<title>(.*?)</title>", text).group(1), "writes": out}


def _walk(node):
    for c in node.get("children", []):
        yield c
        yield from _walk(c)


if __name__ == "__main__":
    p = plan(sys.argv[1])
    json.dump(p, sys.stdout)
    sys.stderr.write(f"{p['name']}: {len(p['writes'])} writes, largest {max(len(w['html']) for w in p['writes'])} chars\n")
