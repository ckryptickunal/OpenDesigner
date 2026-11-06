"""The tour page (/tour/): how OpenDesigner works, drawn as live HTML for visitors deciding whether to use it.

Owner, 2026-11-02 (OWNER-FEEDBACK.md, "reading the repo map", row 8): a page like the private repo map, linked from the home
page's "How it works" section, written for visitors rather than contributors. Every count and every excerpt on it is read
from the repository at build time (the question bank, the house standards, the preflight checklist, the review cases, the
component library, the engine's band formulas and OpenDesigner's own design system), so the page cannot drift from the files.
Site demos are live HTML, never screenshots or video (owner, 2026-10-21).

build.py calls add(); the page's styles are /tour.css and its one script is /tour.js (both from site/static/).
"""
import hashlib
import html
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
STATIC = ROOT / "site" / "static"
REF = ROOT / "skills" / "opendesigner" / "references"
BRAND = ROOT / "brand"
esc = html.escape
PATH = "/tour/"
TITLE = "How OpenDesigner works"
SEO_TITLE = "How OpenDesigner works: the whole system on one page"
DESCRIPTION = ("Follow one request through OpenDesigner: the two ways in, the engine's math, the files it writes to your project, "
               "what protects you and how it learns.")
VER = ""

# Lucide-style line icons (24 px grid, 1.6 stroke), drawn here so the page loads nothing else
ICONS = {
    "ask": '<path d="M21 15a2 2 0 0 1-2 2H8l-5 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><path d="M8 9h8M8 13h5"/>',
    "read": '<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6"/><circle cx="11" cy="14.5" r="2.6"/><path d="m13 16.5 2.2 2.2"/>',
    "fork": '<circle cx="6" cy="5.5" r="2.5"/><circle cx="18" cy="5.5" r="2.5"/><circle cx="12" cy="18.5" r="2.5"/><path d="M6 8v1.5a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V8M12 11.5V16"/>',
    "engine": '<path d="M4 6h9M17 6h3M4 12h3M11 12h9M4 18h11M19 18h1"/><circle cx="15" cy="6" r="2"/><circle cx="9" cy="12" r="2"/><circle cx="17" cy="18" r="2"/>',
    "files": '<path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M8 13h8M8 16.5h5"/>',
    "screen": '<rect x="3" y="4" width="18" height="16" rx="2.5"/><path d="M3 9h18"/><path d="m9 14.5 2 2 4-4"/>',
    "loop": '<path d="M20 11a8 8 0 0 0-14.3-4.9L4 8"/><path d="M4 3.5V8h4.5"/><path d="M4 13a8 8 0 0 0 14.3 4.9L20 16"/><path d="M20 20.5V16h-4.5"/>',
    "check": '<path d="m5 12.5 4.5 4.5L19 7.5"/>',
    "lock": '<rect x="5" y="10.5" width="14" height="10" rx="2.5"/><path d="M8.5 10.5V8a3.5 3.5 0 0 1 7 0v2.5"/>',
}


def icon(name, size=20, cls="tr-ic"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="currentColor" stroke-width="1.6" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{ICONS[name]}</svg>')


# ---------------------------------------------------------------- facts, read from the repository
def facts(b):
    """Counts a visitor can check against the repository, read from the files the skills themselves use."""
    qs = json.loads((REF / "questions.json").read_text())["questions"]
    live = [q for q in qs if q.get("status") != "planned"]
    stages = [p for p in (REF / "stages").glob("*.md") if not p.name.endswith(".detailed.md")]
    std = json.loads((REF / "standards.json").read_text())
    checklist = (ROOT / "skills/opendesigner-preflight/references/checklist.md").read_text()
    cases = json.loads((ROOT / "skills/opendesigner-review/references/cases.json").read_text())["cases"]
    lev = json.loads((REF / "levers.json").read_text())
    dials = lev["dials"]
    briefs = json.loads((ROOT / "evals/design/briefs.json").read_text())["briefs"]
    return {"questions": len(live), "planned": len(qs) - len(live), "stages": len(stages), "standards": len(std["standards"]),
            "standards_version": std.get("version"), "checks": len(re.findall(r"^\d+\. ", checklist, re.M)), "cases": len(cases),
            "dials": dials, "levers": lev, "components": len(b.library_page.components()), "briefs": len(briefs), "checklist": checklist, "case_list": cases}


def zoom_levels():
    """The four zoom levels as the skill's own zoom.md states them, with their question counts from pacing.json."""
    rows = re.findall(r"^\| (\d) \| (\w+) \| (.+?) \| (.+?) \|$", (REF / "zoom.md").read_text(), re.M)
    pacing = json.loads((REF / "pacing.json").read_text())
    per, areas = {}, {}
    for area in pacing["areas"]:
        for lv, v in area["levels"].items():
            per[lv] = per.get(lv, 0) + len(v["questions"])
            areas[lv] = areas.get(lv, 0) + (1 if v["questions"] else 0)
    return [{"n": int(n), "name": name, "what": re.sub(r"\s*\(.*?\)", "", what).split(":")[0].strip(), "size": size,
             "count": per.get(n, 0), "areas": areas.get(n, 0)} for n, name, what, size in rows[:4]]


def band(dial, value):
    """The engine's band formula for a dial's first parameter (levers.json): the band a value falls in and what it gives."""
    m = dial["drives"][0]["map"]
    if m.get("kind") != "bands":
        return None
    for lo, hi, out in m["bands"]:
        if lo <= value <= hi:
            return lo, hi, out
    return None


def unchosen_radius(out, formulas):
    """What the engine does with a control radius nobody chose (levers.json formulas.radius.unchosen): never square, never a
    pill. Returns (radius, the rule in words) when it moves the band's value, else None."""
    u = formulas["radius"]["unchosen"]
    if out == "full" or (isinstance(out, (int, float)) and out > u["max"]):
        return u["max"], f"corners nobody chose stay at {u['max']} px or less"
    if isinstance(out, (int, float)) and out < u["raiseBelow"]:
        return u["to"], f"corners nobody chose stay at {u['to']} px or more"
    return None


def brand_excerpts():
    """Short, real excerpts of OpenDesigner's own design system (made with OpenDesigner) for the file viewer."""
    od = BRAND / "opendesigner"
    design = (BRAND / "DESIGN.md").read_text().splitlines()
    end = design.index("---", 1) if "---" in design[1:] else 16
    design_md = design[:end + 1] + [""] + [ln for ln in design if ln.startswith("# ")][:1]
    product = {sec.splitlines()[0]: sec.strip() for sec in (BRAND / "PRODUCT.md").read_text().split("\n## ")[1:]}
    product_md = [(BRAND / "PRODUCT.md").read_text().splitlines()[0]] + [ln for k in ("Audience", "Surfaces") if k in product for ln in ["", "## " + product[k]]]
    color = json.loads((od / "tokens/semantic.color.light.tokens.json").read_text())["color"]["surface"]
    dtcg = {"color": {"surface": {k: {"$value": v["$value"], "$description": v["$description"]} for k, v in list(color.items()) if isinstance(v, dict) and "$value" in v}}}
    dtcg["color"]["surface"] = dict(list(dtcg["color"]["surface"].items())[:2])
    css = (od / "build/css/tokens.css").read_text()
    want = ["--ds-color-bg-accent-bold", "--ds-radius-control", "--ds-radius-container", "--ds-motion-duration-medium", "--ds-motion-easing-enter"]
    css_lines = [re.search(rf"^\s*{re.escape(w)}:.*$", css, re.M) for w in want]
    tw = (od / "build/tailwind/theme.css").read_text()
    tw_block = tw[tw.index("@theme inline {"):].splitlines()
    dec = (od / "decisions.md").read_text()
    entry = re.search(r"^## D-0056 .*?(?=^## )", dec, re.M | re.S)
    entries = re.search(r"^## D-0056 .*?(?=^## D-0058 )", dec, re.M | re.S)
    ov = (od / "overview.html").read_text()
    areas = re.findall(r'<tr><td><a href="#[^"]+">([^<]+)</a></td><td><span class="ov-tag ov-(\w+)"[^>]*>([^<]+)</span></td><td>(\w+)</td>', ov)
    return {
        "DESIGN.md": "\n".join(design_md),
        "PRODUCT.md": "\n".join(product_md),
        "tokens": "// opendesigner/tokens/semantic.color.light.tokens.json (part)\n" + json.dumps(dtcg, indent=2),
        "css": "/* opendesigner/build/css/tokens.css (part) */\n:root {\n" + "\n".join("  " + m.group(0).strip() for m in css_lines if m) + "\n}",
        "tailwind": "/* opendesigner/build/tailwind/theme.css (part) */\n" + "\n".join(tw_block[:5]) + "\n  …\n}",
        "decisions": entry.group(0).strip() if entry else "",
        "decisions_more": entries.group(0).strip() if entries else (entry.group(0).strip() if entry else ""),
        "areas": [(html.unescape(a), cls, label, zoom) for a, cls, label, zoom in areas],
        "assets_h": html.unescape(m.group(1)) if (m := re.search(r"<h2>(Brand assets[^<]*)</h2>", ov)) else "",
        "assets": [(html.unescape(n), cls, html.unescape(lbl)) for n, cls, lbl in
                   re.findall(r'<div class="ov-asset[^"]*"><b>([^<]+)</b><span class="ov-tag ov-(\w+)"[^>]*>([^<]+)</span>', ov)],
    }


# ---------------------------------------------------------------- the page
def hero(b, f):
    stops = [("ask", "You ask", "In Claude, ChatGPT, Cursor or another AI tool you already use."),
             ("read", "It reads first", "Your CSS, tokens, logo and fonts, before it asks anything."),
             ("fork", "Fix or build", "Audit what you built, or start a system from five answers."),
             ("engine", "The engine does the math", "Color, type, spacing, corners, depth and motion. Offline."),
             ("files", "Files land in your project", "Tokens, CSS, Tailwind, Figma, Swift, Compose and DESIGN.md."),
             ("screen", "New screens follow them", "Your AI reads DESIGN.md first. A review flags values that skip the tokens.")]
    lis = "".join(f'<li class="tr-stop" style="--i:{i}"><span class="tr-dot" aria-hidden="true"></span>{icon(k)}<h2 class="tr-stop-t">{t}</h2><p>{d}</p></li>'
                  for i, (k, t, d) in enumerate(stops))
    pid, author, page_id = b.SCENES["blue-gradient"]
    stats = [(f["questions"], f'questions it can ask. You answer up to five; the rest wait until you zoom in.'),
             (len(f["dials"]), "dials that set the look, each from 0 to 100, turned into values by fixed formulas."),
             (f["standards"], "house standards from sources we trust. The ones that set a value are locked."),
             (f["checks"], "checks before anything visual is shared: type, layout, motion and contrast."),
             (f["cases"], "known ways a design review goes wrong, each with how it is caught."),
             (f["components"], "finished components in the optional library, built only on your tokens.")]
    stat_html = "".join(f'<div class="tr-stat"><p class="tr-big num">{n:,}</p><p>{esc(t)}</p></div>' for n, t in stats)
    return f"""
<section class="h-sec h-first tr-hero">
<nav class="crumb" aria-label="Breadcrumb"><a href="/">{b.NAME}</a><span aria-hidden="true">/</span><span aria-current="page">How it works</span></nav>
<p class="kicker tr-eyebrow">The whole system, on one page</p>
<h1 class="tr-title">How OpenDesigner works</h1>
<p class="h-lede tr-lede">OpenDesigner is a set of skills and a small engine that your AI tool loads. It reads your project, asks only what it can't find there, and writes the rules your screens follow into your own files.</p>
<p class="tr-hero-act"><a class="h-link" href="/docs/install/">Get started free {b.ARROW}</a></p>
<figure class="tr-map-fig">
<div class="stage tr-stage" style="background-image:url(https://images.unsplash.com/{pid}?auto=format&fit=crop&w=1800&q=70)"><div class="stage-in"><div class="tr-panel">
<ol class="tr-map" aria-label="What happens, in order">{lis}</ol>
<a class="tr-return" href="#learn">{icon("loop", 18)}<span>A mistake the maintainer confirms comes back as a new check for everyone who updates.</span></a>
</div></div></div>
<figcaption>Drawn in HTML. Photo: <a href="https://unsplash.com/photos/{page_id}">{esc(author)}</a> on Unsplash.</figcaption>
</figure>
<div class="tr-stats">{stat_html}</div>
<p class="h-fine">Counted from the repository when this page was built (house standards v{esc(str(f["standards_version"]))}). {f["planned"]} more questions are planned.</p>
</section>
"""


def paths_section(b, f):
    t = next(e for e in b.DEMO["examples"] if e["key"] == "billerwick")["tokens"]
    ui = b.DEMO_UI["billerwick"]
    before = {"bg": "#ffffff", "raised": "#ffffff", "text": "#1f2328", "muted": "#a3a8b1", "border": "#d0d7de", "sep": "#eef0f2", "primary": "#166534",
              "on": "#ffffff", "soft": "#d1fae5", "soft-text": "#047857", "r": "3px", "rc": "10px", "h": "30px", "body": "14px", "label": "12px",
              "title": "19px", "headline": "26px", "wh": "700", "inset": "12px", "link": "#0f766e", "more": "18px", "r2": "12px"}
    after = {"bg": t["bg"], "raised": t["raised"], "text": t["text"], "muted": t["muted"], "border": t["border"], "sep": t["sep"], "primary": t["primary"],
             "on": t["onPrimary"], "soft": t["accentSoft"], "soft-text": t["accentText"], "r": t["rControl"], "rc": t["rContainer"], "h": t["hControl"],
             "body": t["body"], "label": t["label"], "title": t["title"], "headline": t["headline"], "wh": t["wHeading"], "inset": t["inset"],
             "link": t["accentText"], "more": t["hControl"], "r2": t["rControl"]}
    c_before, c_after = (f'{b.contrast(v["muted"], v["raised"]):.1f}' for v in (before, after))

    who, _, when = ui["sub"].partition(" · ")
    sub = f'{who} · {when.replace(" ", "&nbsp;")}' if when else ui["sub"]

    def card(v, fixed):
        style = ";".join(f"--x-{k}:{val}" for k, val in v.items())
        fl = lambda n: f' tr-f{" ok" if fixed else ""}" data-n="{n}'
        return (f'<div class="x-card tr-xcard" style="{style}"><div class="x-head"><span class="x-title">{ui["title"]}</span><span class="x-chip{fl(3)}">{ui["chip"]}</span></div>'
                f'<p class="x-sub{fl(1)}">{sub}</p><p class="x-big num">{ui["big"]}</p>'
                f'<div class="tr-meta"><span class="tr-link{fl(3)}">View the PDF</span><span class="tr-more{fl(4)}" role="img" aria-label="More actions"><i></i><i></i><i></i></span></div>'
                f'<div class="x-actions"><span class="x-btn tr-r2{fl(2)}">{ui["secondary"]}</span><span class="x-btn primary{fl(2)}">Approve</span></div></div>')

    px = lambda v: esc(str(v)).replace("px", "\u00a0px")
    found = [f'Grey text at {c_before}:1. The floor is 4.5:1.',
             'Two corner sizes on two buttons: 3\u00a0px and 12\u00a0px.',
             'Three different greens where the system has one.',
             'An 18\u00a0px button. The floor for a target is 24\u00a0px.']
    fixed = [f'The same text at {c_after}:1.',
             f'One corner size from the tokens: {px(t["rControl"])}.',
             f'One accent from the system, {esc(t["primary"])}, with its own tints.',
             f'The button grows to {px(t["hControl"])}, the system\'s control height.']
    legend = lambda items, ok: ('<ol class="tr-legend">' + "".join(f'<li><span class="tr-n{" ok" if ok else ""}" aria-hidden="true">{i + 1}</span><span>{x}</span></li>' for i, x in enumerate(items)) + "</ol>")
    fix_vg = (f'<div class="tr-vg" data-tabs data-play><div class="tablist tr-seg" role="tablist" aria-label="The audited card">'
              f'<button type="button" role="tab" id="fx-tab-b" aria-controls="fx-b" aria-selected="true">Today</button>'
              f'<button type="button" role="tab" id="fx-tab-a" aria-controls="fx-a" aria-selected="false">After your yes</button></div>'
              f'<div class="tr-switch"><div class="tr-fx" role="tabpanel" id="fx-b" aria-labelledby="fx-tab-b" tabindex="0"><div class="tr-well">{card(before, False)}</div>{legend(found, False)}</div>'
              f'<div class="tr-fx" role="tabpanel" id="fx-a" aria-labelledby="fx-tab-a" tabindex="0" hidden><div class="tr-well">{card(after, True)}</div>{legend(fixed, True)}</div></div></div>')

    levels = zoom_levels()
    five = '<p class="tr-five">' + "".join(f"<span>{q}</span>" for q in ("What you're making", "Who it's for", "Where it runs", "How it should feel", "Brand color")) + "</p>"
    total = sum(lv["count"] for lv in levels) or 1
    so_far, rungs = 0, []
    for lv in levels:
        so_far += lv["count"]
        size = esc(lv["size"]) if lv["n"] < 2 else f'{lv["count"]} questions across {lv["areas"]} areas'
        rungs.append(f'<li class="tr-rung{" on" if lv["n"] == 0 else ""}" style="--w:{max(4, round(100 * so_far / total))}%;--i:{lv["n"]}">'
                     f'<p class="tr-rung-h"><strong>{esc(lv["name"].capitalize())}</strong><span>{size}</span></p>'
                     f'<span class="tr-track" aria-hidden="true"><i></i></span><p class="tr-rung-d">{esc(lv["what"])}</p>{five if lv["n"] == 0 else ""}</li>')
    build_vg = (f'<div class="tr-vg tr-vg-col" data-play><p class="kicker">Zoom levels</p><ol class="tr-ladder">{"".join(rungs)}</ol>'
                f'<p class="tr-stopnote">{icon("check", 16)}<span>Stop after any level. Each one leaves you a complete system.</span></p></div>')

    fix_steps = ["It measures your built pages at each screen size, from type and color to contrast and tap targets.",
                 "It marks each problem on the page, with the measured number and what fixing it gives you.",
                 "It fixes one page from design tokens and shows it beside the original.",
                 "The rest of your product changes only after you say yes."]
    build_steps = ["It reads your project first and skips any question a file already answers.",
                   "You answer up to five questions.",
                   "The engine builds the whole system in a few seconds, with dark mode, three densities and reduced motion.",
                   "You zoom into the areas you care about, or stop. Nothing is asked before the things it depends on."]
    steps = lambda xs: '<ol class="tr-steps">' + "".join(f"<li>{esc(x)}</li>" for x in xs) + "</ol>"
    return f"""
<section class="h-sec" id="paths">
<div class="h-head">{b.idx("01", "Two ways in")}<h2 class="h-h2">Fix what you have, or build a system from the start.</h2>
<p class="h-lede">Your AI picks the path from what you ask. Both share one engine, the same accessibility floors and one decision log.</p></div>
<div class="tr-paths">
<article class="tr-path"><p class="tr-path-k"><span class="tr-tag">Fix</span>You already built something</p><h3>It looks off, and you want it to look like one product.</h3>
{fix_vg}{steps(fix_steps)}<a class="h-link tr-path-more" href="/#before-after">See a full audit drawn on a real page {b.ARROW}</a></article>
<article class="tr-path"><p class="tr-path-k"><span class="tr-tag">Build</span>You're starting, or want the whole system</p><h3>Five answers give you a complete first version.</h3>
{build_vg}{steps(build_steps)}<a class="h-link tr-path-more" href="/docs/quickstart/">Your first design system {b.ARROW}</a></article>
</div>
<p class="h-fine">Drawn in HTML: the "today" values are invented mistakes, the "after" values are real engine output for Billerwick. Zoom levels and counts come from the skill's <a href="{b.GH}/blob/main/skills/opendesigner/references/zoom.md">zoom.md</a> and pacing file.</p>
</section>
"""


DIAL_NAMES = {"expression": "Expression", "brandPresence": "Brand presence", "density": "Density", "energy": "Energy",
              "roundness": "Roundness", "depth": "Depth", "colorfulness": "Colorfulness", "warmth": "Warmth"}


def engine_section(b, f):
    dials = {d["id"]: d for d in f["dials"]}
    exs = sorted(b.DEMO["examples"], key=lambda e: ["billerwick", "pebbleday", "fernhollow"].index(e["key"]) if e["key"] in ("billerwick", "pebbleday", "fernhollow") else 9)
    tabs, panels = [], []
    for i, e in enumerate(exs):
        t = e["tokens"]
        tabs.append(f'<button type="button" role="tab" id="en-tab-{e["key"]}" aria-controls="en-{e["key"]}" aria-selected="{"true" if i == 0 else "false"}">'
                    f'<strong>{esc(e["name"])}</strong><span>{esc(e["making"])}</span></button>')
        answers = [("Who", e["who"]), ("Where", e["where"]), ("Feel", e["feel"]),
                   ("Brand", f'<span class="hh-sw" style="background:{esc(e["brand"])}"></span><span class="mono">{esc(e["brand"].lower())}</span>')]
        worked, shown_keys = [], []
        for key, param, have, unit in (("roundness", "Corner radius of controls", t["rControl"], "px"), ("expression", "Type scale ratio", t["ratio"], "")):
            hit = band(dials[key], t["dials"][key])
            if not hit:
                continue
            lo, hi, out = hit
            fmt = lambda v: f"{v}{' ' + unit if unit and isinstance(v, (int, float)) else ''}"
            step = ""
            moved = unchosen_radius(out, f["levers"]["formulas"]) if key == "roundness" and not t.get("shapeChosen") else None
            if moved:  # the engine's own rule for corners nobody chose (levers.json notes it beside the bands)
                step = f' <span class="num">{esc(fmt(out))}</span>, but {esc(moved[1])}, so it gives'
                out = moved[0]
            if str(out) not in str(have):  # the band and the engine output disagree: show nothing rather than a wrong formula
                print(f"tour: {e['key']} {key}={t['dials'][key]} gives {out}, engine wrote {have}; row left out")
                continue
            shown_keys.append(key)
            worked.append(f'<li><p class="tr-w-in"><span>{DIAL_NAMES[key]}</span><b class="num">{t["dials"][key]}</b></p>'
                          f'<p class="tr-w-band">falls in the band <span class="num">{lo} to {hi}</span>, which gives{step}</p>'
                          f'<p class="tr-w-out"><span>{param}</span><b class="num">{esc(fmt(out))}</b></p></li>')
        hl = lambda k: ' class="hl"' if k in shown_keys else ""
        bars = "".join(f'<li{hl(k)} style="--v:{t["dials"][k]};--i:{j}"><span class="tr-dn">{DIAL_NAMES.get(k, k)}</span><span class="tr-bar" aria-hidden="true"><i></i></span>'
                       f'<span class="tr-dv num">{t["dials"][k]}</span></li>' for j, k in enumerate(d["id"] for d in f["dials"]) if k in t["dials"])
        panels.append(f'<div class="tr-en" role="tabpanel" id="en-{e["key"]}" aria-labelledby="en-tab-{e["key"]}" tabindex="0"{"" if i == 0 else " hidden"} data-play>'
                      f'<div class="tr-en-col"><p class="kicker">The answers</p><dl class="tr-dl">' + "".join(f"<div><dt>{a}</dt><dd>{v if a == 'Brand' else esc(v)}</dd></div>" for a, v in answers) + "</dl></div>"
                      f'<div class="tr-en-col"><p class="kicker">The eight dials</p><ol class="tr-dials">{bars}</ol></div>'
                      f'<div class="tr-en-col"><p class="kicker">{"Two dials" if len(worked) == 2 else "One dial"}, worked through</p><ol class="tr-worked">{"".join(worked)}</ol></div></div>')
    return f"""
<section class="h-sec" id="engine">
<div class="h-head">{b.idx("02", "Inside the engine")}<h2 class="h-h2">Each answer moves a dial. Each dial sets real values.</h2>
<p class="h-lede">Your answers set {len(f["dials"])} dials from 0 to 100, and fixed formulas turn each into values like a corner radius. The same answers always give the same files.</p></div>
<div class="tabs tr-engine" data-tabs><div class="tablist demo-tabs" role="tablist" aria-label="Example systems">{"".join(tabs)}</div>
{"".join(panels)}</div>
<p class="h-fine">Real engine output (<a href="{b.GH}/blob/main/site/demo_systems.py">site/demo_systems.py</a>) and the band formulas from <a href="{b.GH}/blob/main/skills/opendesigner/references/levers.json">levers.json</a>, read when this page was built. <a href="/docs/dials/">What each dial does</a></p>
</section>
"""


def files_section(b, f):
    x = brand_excerpts()
    status = {"chosen": "Chosen", "picked": "Picked for you", "default": "Default"}
    rows = "".join(f'<tr><th scope="row">{esc(a)}</th><td><span class="tr-st {esc(c)}">{esc(lbl)}</span></td><td class="mono">{esc(z)}</td></tr>' for a, c, lbl, z in x["areas"][:8])
    overview = (f'<div class="tr-ov"><p class="tr-ov-h"><strong>How complete it is</strong><span>OpenDesigner brand</span></p>'
                f'<table class="tr-ov-t"><thead><tr><th scope="col">Area</th><th scope="col">Status</th><th scope="col">Zoom</th></tr></thead><tbody>{rows}</tbody></table></div>')
    files = [("DESIGN.md", "Your rules in plain words. Coding agents read it before they touch the interface.", f'<pre class="code-lines tr-code">{esc(x["DESIGN.md"])}</pre>'),
             ("PRODUCT.md", "Who it's for and what it's for, kept apart because it changes at its own pace.", f'<pre class="code-lines tr-code">{esc(x["PRODUCT.md"])}</pre>'),
             ("opendesigner/tokens/", "The source of truth, in the DTCG 2025.10 format other tools read.", f'<pre class="code-lines tr-code">{esc(x["tokens"])}</pre>'),
             ("opendesigner/build/", "Code for the platforms you use (CSS variables and Tailwind v4, Swift, Jetpack Compose), plus Figma variables, DTCG 2025.10 and Paper.", f'<pre class="code-lines tr-code">{esc(x["css"])}\n\n{esc(x["tailwind"])}</pre>'),
             ("opendesigner/decisions.md", "Every decision, how it was set and why. Nothing is edited or deleted.", f'<pre class="code-lines tr-code">{esc(x["decisions_more"])}</pre>'),
             ("opendesigner/overview.html", "Your whole system on one page, with what is still a default.", overview)]
    short = lambda n: n.rstrip("/").split("/")[-1] + ("/" if n.endswith("/") else "")
    tabs = "".join(f'<button type="button" role="tab" id="fl-tab-{i}" aria-controls="fl-{i}" aria-selected="{"true" if i == 0 else "false"}"><span class="mono tr-full">{esc(n)}</span><span class="mono tr-short">{esc(short(n))}</span><span class="tr-fd">{esc(d)}</span></button>'
                   for i, (n, d, _) in enumerate(files))
    panes = "".join(f'<div class="tr-pane" role="tabpanel" id="fl-{i}" aria-labelledby="fl-tab-{i}" tabindex="0"{"" if i == 0 else " hidden"}><p class="tr-pane-h mono">{esc(n)}</p><p class="tr-pane-d">{esc(d)}</p>{body}</div>'
                    for i, (n, d, body) in enumerate(files))
    return f"""
<section class="h-sec" id="files">
<div class="h-head">{b.idx("03", "What you keep")}<h2 class="h-h2">Plain files in your project, not an account somewhere.</h2>
<p class="h-lede">Your team, your design tools and your next AI session all read the same rules, and you can open every file.</p></div>
<div class="tr-files" data-tabs><div class="tr-tree" role="tablist" aria-label="Files OpenDesigner writes" aria-orientation="vertical">{tabs}</div>
<div class="tr-viewer">{panes}</div></div>
<p class="h-fine">From OpenDesigner's own design system, made with OpenDesigner (<a href="{b.GH}/tree/main/brand/opendesigner">brand/opendesigner</a>).</p>
</section>
"""


def assets_html(x):
    """OpenDesigner's own brand assets, as its overview page lists them: what was given, and what only a person can give."""
    keep = [a for a in x["assets"] if a[2] != "Not needed"]
    keep = [a for a in keep if a[1] != "missing"][:2] + [a for a in keep if a[1] == "missing"][:2]
    rows = "".join(f'<li><span>{esc(n.split(",")[0])}</span><span class="{"tag-missing" if c == "missing" else "tr-st chosen"}">{esc(lbl)}</span></li>' for n, c, lbl in keep)
    return (f'<div class="tr-assets"><p class="tr-assets-h">{esc(x["assets_h"])}</p><ul>{rows}</ul>'
            '<p class="tr-assets-n">OpenDesigner leaves a gap open instead of inventing the asset.</p></div>')


def protect_section(b, f):
    x = brand_excerpts()
    entry = x["decisions"].splitlines()
    head = entry[0].replace("## ", "") if entry else ""
    meta = re.search(r"set_by: (\w+)", x["decisions"])
    why = re.search(r"reason: (?:[A-Z][a-z]+ \d{4}-\d{2}-\d{2}: )?(.+)", x["decisions"])
    set_by = meta.group(1) if meta else ""
    kinds = [("chosen", "chosen"), ("confirmed_default", "confirmed default"), ("delegated", "picked for you"), ("assumed", "assumed"), ("reference", "from a reference")]
    chips = "".join(f'<span class="chip{" accent" if k == set_by else ""}">{esc(v)}</span>' for k, v in kinds)
    cards = [
        ("Accessibility floors are locked", "WCAG 2.2 AA contrast, 24 px targets, a visible focus ring and reduced motion. No answer, taste or style can lower them.",
         '<div class="tr-floors"><div><span class="tr-aa">Aa</span><span class="num">4.5:1</span><small>text contrast</small></div>'
         '<div><span class="tr-target"></span><span class="num">24 px</span><small>smallest target</small></div>'
         '<div><span class="tr-focus">Save</span><span>Visible</span><small>focus ring</small></div>'
         '<div><span class="tr-still"><i></i></span><span>Respected</span><small>reduced motion</small></div></div>'),
        ("Every value says how it was set", "Chosen by you, a default you confirmed, picked for you, assumed, or taken from a reference. A suggestion you skipped is never recorded as your answer.",
         f'<div class="tr-log"><p class="mono">{esc(head)}</p><p class="tr-chips">{chips}</p>'
         + (f'<p class="tr-why">“{esc(why.group(1)[:1].upper() + why.group(1)[1:])}”</p>' if why else "") + f'<p class="tr-lockline">{icon("lock", 16)}<span>Lock a value, and it changes only with your yes.</span></p></div>'),
        ("Checks report. They don't rewrite.", "The review lists values in your code that skip the tokens and names the token to use. A fix to code you already have waits for your yes.",
         '<pre class="code-lines tr-term"><span class="c">$</span> engine.py review\n3 hard-coded values skip the tokens.\n'
         '  card.css:2  <span class="bad">border-radius: 7px</span>\n    -&gt; use <span class="k">var(--ds-radius-container)</span>\n'
         '  card.css:4  <span class="bad">#1d33d0</span>\n    -&gt; use <span class="k">var(--ds-color-text-accent)</span></pre>'
         f'<p class="tr-lockline">{icon("check", 16)}<span>It reports and edits nothing.</span></p>'),
        ("Your brand stays yours", "It asks you for the logo, photos, typeface and voice, and never fakes them. A reference gives structure; another brand's logo, name, images and words stay out.",
         assets_html(x)),
    ]
    html_cards = "".join(f'<article class="tr-card"><h3>{t}</h3><p>{d}</p><div class="tr-card-vg">{v}</div></article>' for t, d, v in cards)
    return f"""
<section class="h-sec" id="protect">
<div class="h-head">{b.idx("04", "What protects you")}<h2 class="h-h2">The floors hold, and every choice is on record.</h2>
<p class="h-lede">Rule-based checks run before the AI gives any opinion, with the same result every time. Breaking an accessibility floor stops the build.</p></div>
<div class="tr-cards">{html_cards}</div>
<p class="h-fine">Real output from <code>engine.py review</code> and a real entry from OpenDesigner's own decision log, shortened. <a href="/docs/accessibility/">Accessibility floors</a> · <a href="/docs/decisions/">Decisions and DESIGN.md</a></p>
</section>
"""


def learn_section(b, f):
    steps = [("ask", "You notice something", "A missing option, a wrong value, a step that confused you. Your AI notes it quietly and tells you once, at the end."),
             ("files", "A note, never a post", "It saves the note in your project with a ready-to-file issue link. It stays there unless you submit it."),
             ("check", "It becomes a fix or a check", f"When the maintainer confirms it, a gap or a bug is fixed in the source, and a visual mistake becomes a preflight check or a review case. So far: {f['checks']} checks and {f['cases']} cases."),
             ("screen", "Tested before it reaches you", f"AI agents do real tasks with and without it, the engine builds {f['briefs']} fixed briefs, and the checkers face planted mistakes.")]
    lis = "".join(f'<li class="tr-ls" style="--i:{i}"><span class="tr-ls-ic">{icon(k, 20)}</span><h3>{t}</h3><p>{esc(d)}</p></li>' for i, (k, t, d) in enumerate(steps))
    m = re.search(r"^(\d+)\. \*\*(Corners nest)\.\*\* (.+?)\s*\[M\d+\]$", f["checklist"], re.M)
    case = next((c for c in f["case_list"] if "nest" in (c.get("title") or c.get("name") or "").lower()), None)
    trace = ""
    if m and case:
        cid, ctitle = case.get("id", ""), case.get("title") or case.get("name")
        trace = (f'<div class="tr-trace"><p class="kicker">One mistake, followed through</p><ol>'
                 f'<li><span class="tr-when mono">21 Oct 2026</span><p>In an owner review of this website, rounded boxes inside other rounded boxes had corners that didn\'t run parallel.</p></li>'
                 f'<li><span class="tr-when mono">Check {m.group(1)}</span><p>It became preflight check {m.group(1)}, “{esc(m.group(2))}”: the inner radius is the outer radius minus the gap, at every width.</p></li>'
                 f'<li><span class="tr-when mono">{esc(cid)}</span><p>It became review case {esc(cid)}, “{esc(ctitle)}”, so every review now measures it on your pages too.</p></li></ol></div>')
    return f"""
<section class="h-sec" id="learn">
<div class="h-head">{b.idx("05", "How it learns")}<h2 class="h-h2">A confirmed mistake becomes a check for everyone.</h2>
<p class="h-lede">OpenDesigner improves from use. Each mistake the maintainer confirms turns into a fix or a rule that a script or an agent can check, and the tests run again before the change reaches you. <code>engine.py version</code> tells you when your system was built with an older copy, and what to do.</p></div>
<div class="tr-loop" data-play><ol class="tr-loop-row">{lis}</ol><p class="tr-loop-back">{icon("loop", 18)}<span>Then you update, and the loop starts again.</span></p></div>
{trace}
<p class="h-more"><a class="h-link" href="/docs/evals/">See every test result, and run them yourself {b.ARROW}</a></p>
</section>
"""


def end_section(b):
    pid, author, page_id = b.SCENES["blue-waves"]
    status = "".join(f"<li>{x}</li>" for x in b.HOME_STATUS)
    return f"""
<section class="h-sec" id="status">
<div class="tr-status"><div><p class="kicker">Where it stands</p><h2 class="h-h3">Early, and honest about it.</h2></div><ul class="status">{status}</ul></div>
</section>
<section class="h-end">
<div class="h-end-photo" style="background-image:url(https://images.unsplash.com/{pid}?auto=format&fit=crop&w=1600&q=70)">
<div class="h-end-card">
<p class="kicker">Try it</p>
<h2 class="h-h2">See it work on your own project.</h2>
<p class="h-end-lede">Two commands in Claude Code, then a few plain questions. It's free, and the engine runs on your computer.</p>
<div class="h-cta"><a class="btn primary lg" href="/docs/install/">Get started free</a><a class="h-link" href="/docs/how-it-works/">Read every step in the docs {b.ARROW}</a></div>
</div>
</div>
<p class="h-credit">Photo: <a href="https://unsplash.com/photos/{page_id}">{esc(author)}</a> on Unsplash</p>
</section>
"""


def markdown(b, f):
    levels = zoom_levels()
    bw = next(e for e in b.DEMO["examples"] if e["key"] == "billerwick")["tokens"]
    r = bw["dials"]["roundness"]
    lo, hi, out = band(next(d for d in f["dials"] if d["id"] == "roundness"), r)
    return f"""# {TITLE}

{DESCRIPTION}

OpenDesigner is a set of skills and a small engine that your AI tool loads. It reads your project, asks only what it can't find there, and writes the rules your screens follow into your own files.

## The flow

1. You ask, in Claude, ChatGPT, Cursor or another AI tool.
2. It reads your CSS, tokens, logo and fonts before it asks anything.
3. It takes one of two paths: fix what you built, or build a system from five answers.
4. The engine does the math (color, type, spacing, corners, depth, motion), offline.
5. Files land in your project: tokens, CSS, Tailwind, Figma, Swift, Compose, DESIGN.md.
6. New screens follow them. Your AI reads DESIGN.md first, and a review flags values that skip the tokens.

A mistake the maintainer confirms comes back as a new check for everyone who updates.

In numbers, read from the repository: {f["questions"]} questions ({f["planned"]} more planned), {len(f["dials"])} dials, {f["standards"]} house standards (the ones that set a value are locked), {f["checks"]} preflight checks, {f["cases"]} review cases and {f["components"]} library components.

## 01 Two ways in

- **Fix** (you already built something): it measures your pages at each screen size, marks each problem on the page with the measured number, fixes one page from design tokens and shows it beside the original. The rest changes only after you say yes.
- **Build** (you're starting): it reads your files, asks up to five questions, and the engine builds the whole system. Then you zoom in or stop.

Zoom levels: """ + "; ".join(f'{lv["name"]} ({lv["size"]})' for lv in levels) + f""".

## 02 Inside the engine

Your answers set {len(f["dials"])} dials from 0 to 100: {", ".join(DIAL_NAMES.values())}. Fixed band formulas in levers.json turn each position into values. For example, Roundness {r} falls in the band {lo} to {hi}, which gives {out} px control corners. The same answers always give the same files.

## 03 What you keep

DESIGN.md, PRODUCT.md, opendesigner/tokens/ (DTCG 2025.10), opendesigner/build/ ({", ".join(b.EXPORTS)}), opendesigner/decisions.md and opendesigner/overview.html, all in your own repository.

## 04 What protects you

- Accessibility floors are locked: WCAG 2.2 AA contrast, 24 px targets, a visible focus ring and reduced motion.
- Every value records how it was set: chosen, confirmed default, picked for you, assumed or from a reference.
- Checks report and don't rewrite. A fix to code you already have waits for your yes.
- It asks you for the logo, photos, typeface and voice, and never fakes them.

## 05 How it learns

You notice something; your AI saves a note in your project with a ready-to-file issue link (nothing is posted unless you submit it); when the maintainer confirms it, a gap or a bug is fixed in the source and a visual mistake becomes a preflight check or a review case; the tests run again before the change reaches you. {b.release_line()} Test results: {b.SITE_URL}/docs/evals/

Get started: {b.SITE_URL}/docs/install/ · Every step in detail: {b.SITE_URL}/docs/how-it-works/
"""


def add(b, files, mds, paths):
    """Write /tour/, its Markdown copy, /tour.css and /tour.js into the build. b is the build module."""
    global VER
    f = facts(b)
    css = b.minify_css(b.corners_match_levers(b.apple_tracking((STATIC / "tour.css").read_text())))
    js = (STATIC / "tour.js").read_text()
    VER = hashlib.sha256((css + js).encode()).hexdigest()[:10]
    body = hero(b, f) + paths_section(b, f) + engine_section(b, f) + files_section(b, f) + protect_section(b, f) + learn_section(b, f) + end_section(b)
    ld = [b.crumbs_ld([("How it works", PATH)]),
          {"@context": "https://schema.org", "@type": "WebPage", "name": TITLE, "url": b.SITE_URL + PATH, "description": DESCRIPTION,
           "isPartOf": {"@type": "WebSite", "name": b.NAME, "url": b.SITE_URL + "/"}}]
    head = (f'<script src="/tour.js?v={VER}" defer></script>\n'
            '<noscript><style>.tr-switch>[role=tabpanel],.tr-viewer>[role=tabpanel],.tr-engine>.tr-en{grid-area:auto!important}'
            '[role=tabpanel][hidden]{display:block!important;visibility:visible!important}.tr-engine>.tr-en[hidden]{display:grid!important}</style></noscript>\n')
    body = f'<link rel="stylesheet" href="/tour.css?v={VER}">\n' + body  # after site.css, so the page's rules win ties (as /library/ does)
    files["tour/index.html"] = b.shell(PATH, SEO_TITLE, DESCRIPTION, body, b.load_docs(), ld, home=True, preload=head)
    mds["tour/index.md"] = markdown(b, f)
    paths.append(PATH)
    (b.DIST / "tour.css").write_text(css)
    (b.DIST / "tour.js").write_text(js)
