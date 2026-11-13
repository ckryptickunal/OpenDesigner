#!/usr/bin/env python3
"""OpenDesigner review helper: plan what to look at, check what the page measured, report with evidence.

Standard library only, Python 3.10+, no network. It never opens a browser: the agent captures screenshots and runs
probe.js (in Playwright, Chrome DevTools MCP, Claude in Chrome, the in-app browser or any console); this script does
the bookkeeping and the arithmetic. Work goes in ./opendesigner/review/ (or --dir).

    review.py probe [--print]                     where probe.js is (--print writes it to stdout, to paste into a browser tool)
    review.py serve [--port 7788] [--minutes 60]   loopback helper for browser-tool hosts: serves probe.js to the page and saves what
                                                   the page posts back into review/, so nothing large passes through your context
    review.py plan --url URL [--routes /,/x] [--viewports 320,390,768] [--themes light,dark] [--project P] [--edges] [--wide]
                                                   the coverage matrix (route x viewport x theme, plus the tasks that need a
                                                   real browser state), all "todo", in review/plan.json and review/ledger.json
    review.py mark CELL done|skipped|blocked [--evidence PATH ...] [--why "reason"]     (CELL from plan; "task:" cells too)
    review.py check PROBE.json|DIR [...] [--project P] [--json] [--audience everyone]   (also datastates/ and notfound/ from capture.py)
                                                   findings from probe runs (and focus-walk files) against the accessibility
                                                   floors, against practice any product can be judged on (primary buttons
                                                   per view, typefaces, weights, colors) and, when the project has an
                                                   OpenDesigner system, its tokens; saves what each page's share
                                                   card and hero show in review/share.json, which engine.py review
                                                   dates against git (a share image older than what it shows);
                                                   prints what got fixed and what is new since the last check. A folder
                                                   (the review folder) stands for every probe and capture file in it
    review.py finding "what you saw" --severity error|warn|info --basis seen|operated|inferred --evidence PATH
                     [--where "route, viewport, theme"] [--expected "..."] [--fix "..."] [--case CV-01]
                                                   record something you judged by looking or by operating the page
    review.py report [--name N]                    review/REPORT.md: verdict, what was not checked, findings with evidence
    review.py sheet [DIR] [--open]                 review/sheet.html: every screenshot on one page, in order, with its name
    review.py compare --before B.png --marks marks.json --after A.png [--after-marks M.json] [--title T] [--open]
                                                   review/compare.html: the page today, the audit drawn on it (a dashed box and a
                                                   number on each issue) and the fix, switched with the house variant picker; each
                                                   fix says what it gives the person and, with "source", where it comes from.
                                                   marks.json comes from __od.marks() in probe.js
    review.py cases [--when motion,forms] [--group time] [--id CV-01] [--full]
                                                   the catalogue of things reviews miss, filtered to what applies to this page

Every finding says how it is known: measured (a number from the page), operated (you did it and saw the result), seen
(you looked at pixels), inferred (reasoned, not observed). Findings that are not measured are less certain; the report
says so. The verdict is never "looks good": it is FAIL, INCOMPLETE, or NO ERRORS FOUND in the cells that were checked.
"""
from __future__ import annotations

import argparse
import base64
import datetime as dt
import html
import json
import math
import os
import re
import secrets
import sys
import webbrowser
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
PROBE = HERE / "probe.js"
CASES = HERE.parent / "references" / "cases.json"
STATE_DIR = "opendesigner"
SEV = {"error": 0, "warn": 1, "info": 2}
BASIS = ("measured", "operated", "seen", "inferred")

# Floors that never move (guardrails.md section 4). Everything else compares with the project's own system.
FLOOR_TARGET = 24            # WCAG 2.2 SC 2.5.8, CSS px
TOUCH_TARGET = 44            # Apple's default control size in pt (its minimum is 28 pt); warned on coarse-pointer viewports
CONTRAST_TEXT, CONTRAST_LARGE = 4.5, 3.0
MAX_MEASURE_CH = 80          # WCAG 1.4.8 (AAA) upper bound
UI_MOTION_MS = 300           # STD-easing-duration-06: UI motion under 300 ms unless justified
TIGHT_LINE_HEIGHT = 1.3      # wrapped text over 20 px; body text has its own floor (BODY_LINE_HEIGHT)

# Counts any built product can be judged on, with or without a design system (the audit, opendesigner references/audit.md).
# Each is a practice with a source; they report, as warnings, and never decide.
PRIMARY_RATIO = 3.0          # a fill that stands out from what is behind it as much as WCAG 1.4.11 asks of a control's edge
TEXT_FACES = 2               # DC-L02-03: one interface family plus a mono; a second text face only with a named job
WEIGHTS_SYSTEM = 3           # DC-L02-15 and DC-L19-24: three weights in a system, at most two in any one view
TEXT_GREYS = 3               # DC-L15-02: three text colors (white on filled buttons is not counted)
HUE_NOTE, HUE_WARN = 3, 5    # DC-L01-08: one accent plus status colors; making.md section 12: close to monochrome
NEAR_SAME = 10               # RGB distance under which two colors look the same but are typed twice
TYPE_SIZES = 8               # preflight 7: about 8 sizes at most, from one scale
TRACKING_VALUES = 4          # body, display and caps tracking, plus one spare [inferred]; the owner counted 21 on one page
BUTTON_STYLES = 3            # DC-L08-05: primary, secondary and a quiet third; DC-L08-07: one height scale (32, 40, 48)
PRIMARY_LABEL = 15           # owner review 2026-11-05: a primary label under 15 px reads as fine print
TINY_CAPS = 14               # capitals under 14 px on a button are hard to read (preflight 5) [inferred]
HEADING_LINES = 2            # owner review 2026-11-03 row 23: a title runs to two lines at most, at every width

DEFAULT_VIEWPORTS = [(320, 640), (390, 844), (768, 1024), (1024, 768), (1440, 900)]
WIDE_VIEWPORT = (1920, 1080)


# ----------------------------------------------------------------------------------------------------- files
def die(msg):
    raise SystemExit(msg)


def review_dir(args):
    d = Path(args.dir) if getattr(args, "dir", None) else Path(args.project if getattr(args, "project", None) else ".") / STATE_DIR / "review"
    return d


def read_json(path, default=None):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError:
        if default is not None:
            return default
        die(f"{path} not found")
    except json.JSONDecodeError as e:
        die(f"{path} is not valid JSON: {e}")


def write_json(path, data):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def load_cases():
    try:
        return json.loads(CASES.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return {"cases": [], "groups": []}


# --------------------------------------------------------------------------------------------- the system
def load_system(project):
    """What the project's design system says the page should use, or None when it has no OpenDesigner system.
    Reads opendesigner/tokens/opendesigner.meta.json and build/css/tokens.css; anything missing is left out."""
    base = Path(project) / STATE_DIR
    meta = base / "tokens" / "opendesigner.meta.json"
    if not meta.exists():
        if (Path(project) / "tokens" / "opendesigner.meta.json").exists():   # an example folder or a system dir passed directly
            base, meta = Path(project), Path(project) / "tokens" / "opendesigner.meta.json"
        else:
            return None
    m = read_json(meta)
    prefix = m.get("prefix") or "ds"
    sysm = {"name": m.get("name"), "prefix": prefix, "modes": m.get("modes") or ["light", "dark"],
            "type_sizes": [float(x) for x in (m.get("type") or {}).get("sizes") or []],
            "line_heights": [float(x) for x in (m.get("type") or {}).get("lineHeights") or []],
            "min_size": (m.get("type") or {}).get("minSize"),
            "ladder": [float(x) for x in (m.get("space") or {}).get("ladder") or []],
            "unit": (m.get("space") or {}).get("unit") or 4,
            "target": ((m.get("space") or {}).get("targets") or {}).get("pointer") or FLOOR_TARGET,
            "breakpoints": (m.get("space") or {}).get("breakpoints") or {},
            "radii": sorted({float(v) for v in (m.get("shape") or {}).values() if isinstance(v, (int, float))}),
            "durations": sorted({float(v) for v in ((m.get("motion") or {}).get("durations") or {}).values() if isinstance(v, (int, float)) and v}),
            "faces": [((f or {}).get("face") or "") for f in ((m.get("type") or {}).get("faces") or {}).values()],
            "weights": sorted({int(v) for v in ((m.get("type") or {}).get("weights") or {}).values() if isinstance(v, (int, float))}),
            "palette": {}, "radius_ladder": []}
    css = base / "build" / "css" / "tokens.css"
    if css.exists():
        text = css.read_text(encoding="utf-8")
        for name, hx in re.findall(r"--([a-z0-9-]+):\s*(#[0-9a-fA-F]{6})(?:[0-9a-fA-F]{2})?\s*;", text):
            sysm["palette"].setdefault(hx.lower(), name)
        sysm["radius_ladder"] = sorted({float(v) for v in re.findall(rf"--{re.escape(prefix)}-radius-(\d+):", text)})
    tr = (m.get("type") or {}).get("tracking") or {}
    sysm["tracking"] = {k: float(v) for k, v in tr.items() if isinstance(v, (int, float))}
    sysm["measure"] = (((m.get("space") or {}).get("layout") or {}).get("measure") or {}).get("prose")
    sysm["space_tokens"], sysm["tracking_tokens"], sysm["measure_token"] = {}, {}, None
    if css.exists():
        for name, num, unit in re.findall(rf"--({re.escape(prefix)}-space-\d+):\s*(-?[\d.]+)(px|rem)\s*;", text):
            sysm["space_tokens"].setdefault(float(num) * (16 if unit == "rem" else 1), name)
        styles = dict(re.findall(rf"--({re.escape(prefix)}-text-[a-z]+-[a-z]+)-tracking:\s*(-?[\d.]+)em\s*;", text))
        sizes = {k: float(v) * (16 if u == "rem" else 1) for k, v, u in re.findall(rf"--({re.escape(prefix)}-font-size-[\d]+):\s*([\d.]+)(px|rem)", text)}
        for role, val in sysm["tracking"].items():   # the first text style whose tracking is the role's value
            pick = [st for st, em in styles.items() if abs(float(em) - val) < 1e-4]
            if role in ("display", "heading"):
                pick = [st for st in pick if re.search(r"headline|display|title", st)] or pick
            elif role == "body":
                pick = [st for st in pick if "body" in st] or pick
            elif role.startswith("caps"):
                pick = [st for st in pick if "label" in st] or pick
            if pick:
                sysm["tracking_tokens"][role] = (pick[-1] if role == "display" else pick[0]) + "-tracking"
        mt = re.search(rf"--({re.escape(prefix)}-layout-measure-prose):", text)
        sysm["measure_token"] = mt.group(1) if mt else None
    st = read_json(base / "state.json", {}) or {}
    ans = st.get("answers") or {}
    sysm["case"] = (ans.get("Q-voice-03") or {}).get("value")
    sysm["audience"] = (ans.get("Q-aud-01") or {}).get("value")
    # faces reference each other ("=textFace"); keep the real names only
    sysm["faces"] = [f for f in sysm["faces"] if f and not f.startswith("=")]
    return sysm


def hex_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def nearest(value, options):
    return min(options, key=lambda o: (abs(o - value), o)) if options else None


def nearest_color(hx, palette):
    if not palette:
        return None
    r = hex_rgb(hx)
    best = min(palette, key=lambda p: sum((a - b) ** 2 for a, b in zip(r, hex_rgb(p))))
    return best, palette[best], math.sqrt(sum((a - b) ** 2 for a, b in zip(r, hex_rgb(best))))


def fmt(n):
    return f"{n:g}" if isinstance(n, (int, float)) else str(n)


# ---------------------------------------------------------------------------------------------- findings
class Findings:
    """Findings merged by (case, key): the same defect at three viewports is one finding with three places."""

    def __init__(self):
        self.items = {}
        self.pixel_pass = {}   # where -> selectors whose text passed contrast on the real pixels (check_pixels)

    def add(self, case, sev, title, where, measured=None, expected=None, evidence=None, fix=None, std=None, key=None, basis="measured", decided="rule"):
        k = (case, key or title)
        f = self.items.get(k)
        if not f:
            f = self.items[k] = {"id": "", "case": case, "severity": sev, "basis": basis, "title": title, "where": [], "measured": measured,
                                 "expected": expected, "evidence": [], "fix": fix, "standard": std, "status": "confirmed", "decided": decided}
        if where and where not in f["where"]:
            f["where"].append(where)
        for e in evidence or []:
            if e and e not in f["evidence"] and len(f["evidence"]) < 6:
                f["evidence"].append(e)
        if SEV[sev] < SEV[f["severity"]]:
            f["severity"] = sev

    def done(self):
        out = sorted(self.items.values(), key=lambda f: (SEV[f["severity"]], f["case"], f["title"]))
        for f in out:
            f["id"] = "M-" + re.sub(r"[^A-Z0-9]+", "", f["case"].upper()) + "-" + f"{abs(hash_str(f['case'] + '|' + f['title'])) % 10000:04d}"
        return out


def hash_str(s):
    h = 5381
    for c in s:
        h = ((h << 5) + h + ord(c)) & 0xFFFFFFFF
    return h


def where_of(p):
    u = urlparse(p.get("url") or "")
    route = (os.path.basename(u.path) or "/") if u.scheme == "file" else (u.path or "/") + (("#" + u.fragment) if u.fragment and u.fragment.startswith("/") else "")
    v = p.get("viewport") or {}
    theme = (p.get("mode") or {}).get("theme") or (p.get("media") or {}).get("colorScheme") or "light"
    extra = ""
    if p.get("stress"):
        extra = " · stress: " + "+".join(p["stress"])
    if (p.get("media") or {}).get("reducedMotion"):
        extra += " · reduced motion"
    if (p.get("media") or {}).get("forcedColors"):
        extra += " · forced colors"
    return f"{route} · {fmt(v.get('w'))}x{fmt(v.get('h'))} · {theme}{extra}"


# -------------------------------------------------------------------------------------------- the checks
def check_probe(p, sysm, F):
    w = where_of(p)
    vp = p.get("viewport") or {}
    stressed = bool(p.get("stress"))
    stress_txt = " under " + "+".join(p["stress"]) if stressed else ""
    # text spacing (1.4.12) and 200% text (1.4.4) are requirements; long words, +40% text and RTL are robustness tests
    stress_sev = "error" if (not stressed or set(p["stress"]) & {"textSpacing", "text200"}) else "warn"
    doc, media = p.get("doc") or {}, p.get("media") or {}
    # a stress pass changes sizes and spacing on purpose, and forced colors swaps every color: judge drift on normal runs only
    judge_drift = not stressed and not media.get("forcedColors")

    # --- floors --------------------------------------------------------------------------------------------
    if doc.get("hOverflow", 0) > 0:
        offenders = [o["sel"] for o in (p.get("overflow") or {}).get("list", [])[:4]]
        F.add("CV-05", stress_sev, f"The page scrolls sideways{stress_txt}", w, f"{fmt(doc['hOverflow'])} px wider than the viewport ({fmt(vp.get('w'))} px)",
              "no horizontal scroll (WCAG 1.4.10 at 320 px)", offenders,
              "find the widest element listed and let it wrap, shrink (min-width: 0, max-width: 100%) or scroll inside its own box", "WCAG 1.4.10",
              key="hscroll" + ("-stress" if stressed else ""))
    elif (p.get("overflow") or {}).get("list"):
        o = p["overflow"]["list"]
        F.add("CV-05", "error" if doc.get("rootClipsX") else "warn", "Elements extend past the viewport edge" + (" and the page hides it" if doc.get("rootClipsX") else ""), w,
              f"{len(o)} element(s); the widest is {fmt(o[0]['over'])} px past the edge", "everything inside the viewport unless it scrolls in its own box",
              [x["sel"] for x in o[:4]], "content can be cut off with no way to reach it: remove overflow-x: hidden from html/body and fix the wide element", "WCAG 1.4.10", key="past-edge")
    for c in (p.get("overflow") or {}).get("clipped", []):
        if (c.get("ellipsis") or c.get("clamp")) and c.get("role") in ("heading", "control", "label") and not stressed:
            continue   # ST-13 reports an ellipsis or clamp on a heading, button or label (the craft checks)
        if c.get("ellipsis"):
            F.add("ST-04", "info", "Text is cut with an ellipsis", w, f"{c['sel']}: {c['text']!r} needs {fmt(c['sw'])} px, has {fmt(c['cw'])} px",
                  "intentional, with the full text reachable (title, tooltip, expand)", [c["sel"]], "confirm the full value can be read elsewhere", "WCAG 1.4.4", key="ellipsis:" + c["sel"])
        else:
            F.add("ST-04", stress_sev if stressed else "warn", f"Text is clipped and cannot be read{stress_txt}", w,
                  f"{c['sel']}: content {fmt(c['sw'])}x{fmt(c['sh'])} px in a {fmt(c['cw'])}x{fmt(c['ch'])} px box", "no content lost when text grows",
                  [c["sel"]], "let the box grow (min-height, not height; overflow: visible) or wrap the text", "WCAG 1.4.4 / 1.4.12", key="clip:" + c["sel"] + ("-stress" if stressed else ""))

    ct = p.get("contrast") or {}
    on_pixels = F.pixel_pass.get(w, set())
    for c in ct.get("failing", []):
        need = CONTRAST_LARGE if c.get("large") or c.get("symbol") else CONTRAST_TEXT   # a lone symbol is a graphic: 3:1 (WCAG 1.4.11)
        if c["sel"] in on_pixels:   # the pixels behind it were read and pass: the probe's colour backdrop was a guess (a photo in an <img>, say)
            continue
        unsure = c.get("backdrop") in ("image", "gradient")
        F.add("MS-04", "info" if unsure else "error", f"{'Symbol' if c.get('symbol') else 'Text'} contrast {c['ratio']}:1 is below {need}:1" + (" (background is an image or gradient: sample the pixels)" if unsure else ""),
              w, f"{c['fg']} on {c['bg']}, {fmt(c['fs'])} px, {c['n']} element(s)", f"{need}:1 (no rounding up: 4.49 fails)", [c["sel"]],
              "darken the text or lighten the surface with a token pair that passes; check the same pair in dark mode", "WCAG 1.4.3", key=f"contrast:{c['fg']}:{c['bg']}:{c.get('large')}")

    tg = p.get("targets") or {}
    small = [s for s in tg.get("small", []) if not s.get("spacingException")]
    if small:
        F.add("MS-06", "error", f"Targets smaller than {FLOOR_TARGET}x{FLOOR_TARGET} px with another target close by", w,
              f"{len(small)} target(s): " + "; ".join(f"{s['sel']} {fmt(s['w'])}x{fmt(s['h'])}" for s in small[:4]),
              f"at least {FLOOR_TARGET}x{FLOOR_TARGET} CSS px, or {FLOOR_TARGET} px of clear space around each (WCAG 2.5.8)", [s["sel"] for s in small[:4]],
              "raise min-width and min-height, or add padding to the hit area", "WCAG 2.5.8", key="target-small")
    if tg.get("coarse") and tg.get("small"):
        ts = tg["small"]
        F.add("IN-04", "warn", f"Touch targets under {TOUCH_TARGET} px", w, f"{len(ts)} target(s), e.g. {ts[0]['sel']} at {fmt(ts[0]['w'])}x{fmt(ts[0]['h'])}",
              f"Apple's default control size is {TOUCH_TARGET} pt (minimum 28 pt); Android recommends 48 dp", [s["sel"] for s in ts[:3]], "enlarge the hit area on touch (padding, or an ::after inset)", "Apple HIG, Android accessibility guide", key="touch-target")
    if tg.get("noName"):
        nn = tg["noName"]
        F.add("IN-03", "error", "Controls with no accessible name", w, f"{len(nn)} control(s): " + "; ".join(n["sel"] for n in nn[:4]), "every control has a name a screen reader can say",
              [n["sel"] for n in nn[:4]], "add aria-label, visible text, or a <label>", "WCAG 4.1.2 / 1.1.1", key="noname")
    if tg.get("vague"):  # names that exist but say nothing (Calo et al., CHI EA 2026); context may justify one, so info only
        vg = tg["vague"]
        cnt = {}
        for v in vg:
            cnt[v["name"]] = cnt.get(v["name"], 0) + 1
        F.add("IN-03", "info", f"{len(vg)} name{'s' if len(vg) != 1 else ''} may not say what {'they do' if len(vg) != 1 else 'it does'}", w,
              ", ".join(f"{n} \u00d7{c}" if c > 1 else n for n, c in sorted(cnt.items(), key=lambda kv: -kv[1])[:5]),
              "each link, button, field and image says what it does or shows, read on its own (WCAG 2.4.4, 2.4.6, 1.1.1)",
              [v["sel"] for v in vg[:4]], "name the action or the destination (\"Read the pricing guide\"), or describe the image; "
              "nearby text may already make it clear", "WCAG 2.4.4 / 2.4.6 / 1.1.1", key="vague-names")

    hf = tg.get("hiddenFocusable") or []
    if hf:
        real_hidden = [h for h in hf if h["why"] != "outside the page"]
        if real_hidden:
            F.add("IN-08", "warn", "Controls a keyboard can reach but nobody can see", w, f"{len(real_hidden)}: " + "; ".join(f"{h['sel']} ({h['why']})" for h in real_hidden[:3]),
                  "focusable things are visible when focused", [h["sel"] for h in real_hidden[:3]], "hide with display: none or inert until they are meant to appear", "WCAG 2.4.7 / 1.3.2", key="hidden-focusable")
        off = [h for h in hf if h["why"] == "outside the page"]
        if off:
            F.add("IN-08", "info", "Controls placed outside the page box", w, "; ".join(h["sel"] for h in off[:3]), "a skip link that appears on focus is fine; anything else is off-canvas content", [h["sel"] for h in off[:3]], "Tab to it and confirm it appears", None, key="offcanvas")
    lb_all = (p.get("labels") or {}).get("broken") or []
    lb, seen_lb = [], {}
    for x in lb_all:   # the same button in every table row is one finding with a count
        k = (x["sel"], x["text"])
        if k in seen_lb:
            seen_lb[k]["n"] += 1
        else:
            seen_lb[k] = dict(x, n=1)
            lb.append(seen_lb[k])
    if lb:
        def says(x):
            return (f"{x['sel']}: \"{x['text']}\" on {x['lines']} lines" + (" (inside a word)" if x.get("midWord") else "")
                    + (f", {x['n']} times" if x["n"] > 1 else ""))
        F.add("MS-15", "error", "Labels break across lines" + stress_txt, w, "; ".join(says(x) for x in lb[:4]) + (f" (+{len(lb) - 4} more)" if len(lb) > 4 else ""),
              "every button, tab, chip and tag label on one line", [x["sel"] for x in lb[:4]],
              "keep the label on one line (white-space: nowrap) and give it room: widen the column, drop the icon or shorten the label; let the row wrap, never the label",
              None, key="label-break" + ("-stress" if stressed else ""))
    ph = (p.get("content") or {}).get("placeholders") or []
    if ph:
        F.add("ST-06", "warn", "Placeholder or broken template text on the page", w, "; ".join(f"{x['sel']}: {x['match']!r}" for x in ph[:4]), "real content", [x["sel"] for x in ph[:4]], "replace lorem ipsum; undefined, NaN, null and {{ }} mean data did not arrive or a template did not render", None, key="placeholders")
    if doc.get("blocksZoom"):
        F.add("EN-01", "error", "The page stops people from zooming", w, f"viewport meta: {doc.get('viewportMeta')}", "no user-scalable=no and no low maximum-scale",
              ["meta[name=viewport]"], "remove user-scalable=no and maximum-scale", "WCAG 1.4.4", key="zoom-blocked")
    if not doc.get("lang"):
        F.add("IN-03", "error", "The page does not declare its language", w, "<html> has no lang", "<html lang=\"en\"> (or the real language)", ["html"], "set lang", "WCAG 3.1.1", key="lang")
    a = p.get("a11y") or {}
    hd = a.get("headings") or {}
    if hd.get("levels") and hd.get("h1", 0) == 0:
        F.add("IN-03", "warn", "No level-1 heading", w, f"headings: {hd['levels'][:12]}", "one h1 that names the page", ["h1"], "make the page title an h1", "WCAG 2.4.6 (best practice)", key="no-h1")
    if hd.get("h1", 0) > 1:
        F.add("IN-03", "info", "More than one level-1 heading", w, f"{hd['h1']} h1 elements", "usually one", ["h1"], None, None, key="many-h1")
    if hd.get("skips"):
        s = hd["skips"][0]
        F.add("IN-03", "warn", "Heading levels skip", w, f"h{s['from']} is followed by h{s['to']} ({len(hd['skips'])} skip(s))", "levels go down one at a time", ["h" + str(s["to"])],
              "use the real level and style it with CSS", "best practice (axe: heading-order)", key="heading-skip")
    if a.get("duplicateIds"):
        F.add("IN-03", "warn", "Duplicate ids", w, ", ".join(a["duplicateIds"][:5]), "each id once (labels and aria-labelledby point at ids)", ["#" + a["duplicateIds"][0]], None, "HTML", key="dup-id")
    st = a.get("states") or {}
    if st.get("focusRingRemoved"):
        F.add("IN-02", "error", "The focus ring is removed and nothing replaces it", w, f"{len(st['focusRingRemoved'])} control(s), e.g. {st['focusRingRemoved'][0]}",
              "a visible focus indicator (2 px ring, 2 px offset, not color alone)", st["focusRingRemoved"][:4],
              "replace outline: none with a :focus-visible style", "WCAG 2.4.7 (failure F78)", key="focus-removed")
    n_int = st.get("checked") or 0
    if n_int and len(st.get("noHover", [])) >= max(3, n_int // 2) and (media.get("hover", True)):
        F.add("ST-01", "info", "Most controls have no :hover style", w, f"{len(st['noHover'])} of {n_int} have none in the stylesheets I can read",
              "a hover cue on pointer devices (and nothing that only appears on hover)", st["noHover"][:3], "confirm by hovering a few; touch-only products can skip this", None, key="no-hover")

    im = p.get("images") or {}
    if im.get("broken"):
        F.add("MS-10", "error", "Images failed to load", w, f"{len(im['broken'])}: " + "; ".join(im["broken"][:4]), "every image loads", im["broken"][:4], "fix the path or the asset, and check the network tab", None, key="img-broken")
    if im.get("noAlt"):
        F.add("MS-10", "error", "Images with no alt attribute", w, f"{len(im['noAlt'])}: " + "; ".join(im["noAlt"][:4]), "alt text, or alt=\"\" if it is decoration", im["noAlt"][:4], "add alt", "WCAG 1.1.1", key="img-alt")
    if im.get("stretched"):
        s_ = im["stretched"]
        F.add("MS-10", "warn", "Images stretched out of their shape", w, "; ".join(f"{x['sel']}: file {x['natural']}, shown {x['shown']}" for x in s_[:3]), "same aspect ratio (object-fit: cover or contain)", [x["sel"] for x in s_[:3]], "set object-fit", None, key="img-stretch")
    if im.get("blurry"):
        s_ = im["blurry"]
        F.add("MS-10", "warn", "Images smaller than the space they fill", w, "; ".join(f"{x['sel']}: file {fmt(x['natural'])} px wide, shown {fmt(x['shown'])} px at {fmt(x['dpr'])}x" for x in s_[:3]), "file at least as wide as the shown size times the pixel ratio", [x["sel"] for x in s_[:3]], "use a larger file or srcset", None, key="img-blurry")
    if im.get("oversize"):
        s_ = im["oversize"]
        F.add("MS-10", "info", "Image files far larger than needed", w, "; ".join(f"{x['sel']}: file {fmt(x['natural'])} px wide, shown {fmt(x['shown'])} px" for x in s_[:3]), "about the shown size times the pixel ratio", [x["sel"] for x in s_[:3]], "resize or use srcset", None, key="img-oversize")

    # --- type ----------------------------------------------------------------------------------------------
    ty = p.get("type") or {}
    sm = ty.get("smallest")
    floor_min = (sysm or {}).get("min_size") or 12
    if sm and sm["px"] < floor_min:
        F.add("MS-02", "warn", f"Text smaller than {fmt(floor_min)} px", w, f"{sm['px']} px: {sm['text']!r} in {sm['sel']}", f"at least {fmt(floor_min)} px" + (" (the system's minimum)" if sysm else ""), [sm["sel"]], "raise it to a text style", None, key="min-text")
    if ty.get("longLines"):
        l = ty["longLines"][0]
        F.add("MS-07", "warn", f"Lines longer than {MAX_MEASURE_CH} characters", w, f"{l['sel']} is about {fmt(l['ch'])} characters wide", f"at most {MAX_MEASURE_CH} (WCAG 1.4.8, AAA); 45-75 is the usual target", [x["sel"] for x in ty["longLines"][:3]], "set max-width: 65ch on the text block", "WCAG 1.4.8 (AAA)", key="measure")
    body_lh = [t for t in ty.get("lineHeightTight") or [] if 14 <= t.get("fs", 16) <= 20 and t["ratio"] < BODY_LINE_HEIGHT]   # captions under 14 px are not body text
    big_lh = [t for t in ty.get("lineHeightTight") or [] if t.get("fs", 16) > 20 and t["ratio"] < TIGHT_LINE_HEIGHT]
    if body_lh and not stressed:
        t = body_lh[0]
        lh_tok = f"var(--{(sysm or {}).get('prefix', 'ds')}-text-body-md-line-height)" if sysm else "1.5"
        F.add("MS-07", "warn", f"Body text with line height under {BODY_LINE_HEIGHT}", w,
              "; ".join(f"{x['sel']}: {fmt(x['ratio'])}x at {fmt(x['fs'])} px over several lines" for x in body_lh[:4]),
              f"at least {BODY_LINE_HEIGHT}x for body text; 1.5x is WCAG 1.4.8 (AAA) and what 1.4.12 forces", [x["sel"] for x in body_lh[:4]],
              f"line-height: {lh_tok}, or the body text style", "WCAG 1.4.8 (AAA)", key="tight-lh")
    if big_lh and not stressed:
        t = big_lh[0]
        F.add("MS-07", "info", "Wrapped large text with tight line height", w, f"{t['sel']}: line height {t['ratio']}x its size over several lines", f"at least {TIGHT_LINE_HEIGHT}x for wrapped text over 20 px", [x["sel"] for x in big_lh[:3]], None, "WCAG 1.4.12", key="tight-lh-big")
    if judge_drift:
        check_round(p, w, F)
    check_craft(p, sysm, w, F)
    check_copy(p, sysm, w, F, getattr(F, "audience", None))
    fam = p.get("fonts") or {}
    used = ty.get("families") or {}
    for name, state in (fam.get("familyState") or {}).items():
        if state in ("missing", "failed", "declared-not-loaded") and name in used:
            n = used[name]["n"]
            F.add("MS-03", "error" if state != "declared-not-loaded" else "warn", f"The page asks for {name} but it is not the font being drawn ({state})", w, f"{n} text element(s) fall back to the next font in the stack",
                  f"{name} loaded (@font-face file served, or installed)", [used[name]["ex"][0] if used[name]["ex"] else name],
                  "check the @font-face src path and the network tab; wait for document.fonts.ready before judging type", None, key="font:" + name.lower())
    if judge_drift and sysm and sysm.get("faces"):
        wanted = {f.lower() for f in sysm["faces"]}
        top_family = max(used, key=lambda k: used[k].get("chars", 0)) if used else None
        if top_family and top_family.lower() not in wanted and not re.match(r"^(system-ui|ui-|serif|sans-serif|monospace|-apple)", top_family, re.I):
            F.add("MS-03", "warn", "Most text is not in the system's typeface", w, f"most text is {top_family}; the system says {', '.join(sysm['faces'])}", "the system's text face", [used[top_family]["ex"][0]], "use the font-family token", None, key="face-drift")
    ge = ty.get("weights") or {}
    if judge_drift and sysm and sysm.get("weights"):
        odd = {k: v for k, v in ge.items() if int(float(k)) not in sysm["weights"]}
        if odd:
            k = max(odd, key=lambda x: odd[x]["n"])
            F.add("MS-02", "info", "Font weights outside the system's", w, f"weight {k} on {odd[k]['n']} element(s); the system uses {sysm['weights']}", "the system's weights", [odd[k]["ex"][0]], None, None, key="weights")

    # --- drift from the system ----------------------------------------------------------------------------
    scale = (sysm or {}).get("type_sizes")
    sizes = ty.get("sizes") or {}
    if judge_drift and scale and sizes:
        total = sum(v["n"] for v in sizes.values())
        off = {k: v for k, v in sizes.items() if min(abs(float(k) - s) for s in scale) > 0.6}
        if off:
            uses = sum(v["n"] for v in off.values())
            rows = sorted(off.items(), key=lambda kv: -kv[1]["n"])[:5]
            F.add("MS-02", "warn" if uses / total >= 0.1 else "info", f"Font sizes off the type scale ({len(off)} value(s), {uses} of {total} text elements)", w,
                  "; ".join(f"{k}px x{v['n']} (nearest {fmt(nearest(float(k), scale))})" for k, v in rows), f"sizes from the scale: {', '.join(fmt(s) for s in scale)}",
                  [v["ex"][0] for _, v in rows if v["ex"]], "use a text style; a browser default (buttons 13.33 px, h3 18.72 px) means the element does not inherit", "tokens", key="type-drift")

    ladder = (sysm or {}).get("ladder")
    space = (p.get("space") or {}).get("values") or {}
    if space and judge_drift:
        grid = (sysm or {}).get("unit") or 4
        def on_scale(v):
            return min(abs(v - s) for s in ladder) <= 0.5 if ladder else (v % grid < 0.5 or grid - (v % grid) < 0.5)
        total = sum(v["n"] for v in space.values())
        off = {k: v for k, v in space.items() if not on_scale(float(k)) and float(k) > 1}
        if off:
            uses = sum(v["n"] for v in off.values())
            rows = sorted(off.items(), key=lambda kv: -kv[1]["n"])[:6]
            F.add("MS-01", "warn" if uses / total >= 0.1 else "info", f"Spacing off the {'ladder' if ladder else str(grid) + ' px grid'} ({len(off)} value(s), {uses} of {total} uses)", w,
                  "; ".join(f"{k}px x{v['n']}" + (f" (nearest {fmt(nearest(float(k), ladder))})" if ladder else "") for k, v in rows), (f"steps: {', '.join(fmt(s) for s in ladder)}" if ladder else f"multiples of {grid} px"),
                  [v["ex"][0] for _, v in rows if v["ex"]], "use the spacing tokens; 1-2 px values are usually borders or browser defaults", "tokens", key="space-drift")
    for m in (p.get("space") or {}).get("negativeMargins", [])[:1]:
        F.add("MS-11", "info", "Negative margins in use", w, f"{m['sel']} {m['prop']} {m['v']} px", "usually a workaround that overlaps neighbours", [m["sel"]], None, None, key="neg-margin")

    rads = (p.get("radius") or {})
    rlad = (sysm or {}).get("radius_ladder") or (sysm or {}).get("radii")
    if rlad and rads and judge_drift:
        off = {k: v for k, v in rads.items() if "%" not in k and float(k) < 999 and min(abs(float(k) - r) for r in rlad) > 0.5}
        if off:
            rows = sorted(off.items(), key=lambda kv: -kv[1]["n"])[:5]
            F.add("MS-09", "warn", "Corner radii off the system's", w, "; ".join(f"{k}px x{v['n']} (nearest {fmt(nearest(float(k), rlad))})" for k, v in rows), f"radii: {', '.join(fmt(r) for r in rlad)}",
                  [v["ex"][0] for _, v in rows if v["ex"]], "use the radius tokens", "tokens", key="radius-drift")

    pal = (sysm or {}).get("palette")
    if pal and judge_drift:
        allowed = {"#ffffff", "#000000"}
        for kind in ("text", "bg", "border"):
            cols = (p.get("colors") or {}).get(kind) or {}
            off = {k[:7]: v for k, v in cols.items() if k[:7].lower() not in pal and k[:7].lower() not in allowed}
            if off:
                rows = sorted(off.items(), key=lambda kv: -kv[1]["n"])[:5]
                def near(hx):
                    nc = nearest_color(hx, pal)
                    return f" (closest token --{nc[1]})" if nc and nc[2] < 40 else ""
                F.add("MS-08", "warn" if sum(v["n"] for v in off.values()) >= 5 else "info", f"{kind.capitalize()} colors that are not in the palette ({len(off)})", w,
                      "; ".join(f"{k} x{v['n']}{near(k)}" for k, v in rows), "colors from the tokens", [v["ex"][0] for _, v in rows if v["ex"]], "use a color token; check dark mode too", "tokens", key="color-drift-" + kind)

    if judge_drift:
        check_practice(p, sysm, w, F)

    # --- fixed bars ----------------------------------------------------------------------------------------
    # bars only: a sticky sidebar runs top to bottom but covers nothing beside it, and a pinned scene fills the screen on purpose
    fx = [f for f in p.get("fixed") or [] if (not vp.get("w") or f.get("w", 0) >= vp["w"] / 2) and (not vp.get("h") or f.get("h", 0) < vp["h"] * 0.9)]   # a pinned full-screen scene is not a bar
    if fx and vp.get("h"):
        topcover = max([f["top"] + f["h"] for f in fx if f["top"] <= 1] or [0])
        botcover = max([f["h"] for f in fx if f["bottom"] <= 1 and f["top"] > 1] or [0])
        share = (topcover + botcover) / vp["h"]
        if share >= 0.3:
            F.add("CV-08", "warn", "Fixed bars cover a large part of the viewport", w, f"{fmt(topcover)} px at the top and {fmt(botcover)} px at the bottom of {fmt(vp['h'])} px ({round(share * 100)}%)",
                  "under about 30% so focused elements and anchors are not hidden (WCAG 2.4.11)", [f["sel"] for f in fx[:3]], "add scroll-padding-top / scroll-margin-top and shrink the bar on short screens", "WCAG 2.4.11", key="fixed-cover")

    # --- motion --------------------------------------------------------------------------------------------
    mo = p.get("motion") or {}
    decl = mo.get("declared") or {}
    anim = mo.get("animations") or []
    has_motion = bool(anim or decl.get("animatedNames") or mo.get("transitionDurations"))
    if has_motion and not mo.get("reducedMotionRules") and not media.get("reducedMotion"):
        F.add("EN-02", "error", "Motion with no prefers-reduced-motion rule", w, f"{len(anim)} running animation(s), {len(mo.get('transitionDurations') or {})} transition duration(s), 0 reduced-motion rules in the stylesheets I can read",
              "a reduced-motion path (house floor: WCAG 2.3.3 treated as required)", [a["target"] for a in anim[:2] if a.get("target")], "add @media (prefers-reduced-motion: reduce) that removes movement and long fades, or use the system's motion tokens", "WCAG 2.3.3", key="reduced-rule")
    if media.get("reducedMotion") and (mo.get("running") or 0) > 0:
        F.add("TM-10", "error", "Animations still run with reduced motion on", w, f"{mo['running']} animation(s) running, e.g. {anim[0]['name'] or anim[0]['type']} on {anim[0]['target']}", "no movement",
              [a["target"] for a in anim[:3]], "wrap the animation in @media (prefers-reduced-motion: no-preference) or turn it off in the reduce block", "WCAG 2.3.3", key="reduced-ignored")
    for i in decl.get("infiniteDeclared", [])[:3]:
        F.add("TM-03", "warn", "An animation loops forever", w, f"{i['sel']}: {i['name']}, {fmt(i['ms'])} ms per loop", "anything that moves for over 5 s can be paused (WCAG 2.2.2)", [i["sel"]],
              "give it a pause control, stop it after a few loops, or make it a state change", "WCAG 2.2.2", key="infinite:" + i["sel"])
    for l in decl.get("layoutProps", [])[:3]:
        F.add("TM-09", "warn", "A transition animates layout", w, f"{l['sel']}: {l['prop']} over {fmt(l['ms'])} ms", "animate transform and opacity; layout properties cause reflow and jank", [l["sel"]], "animate transform: scale/translate, or measure and animate to a fixed height", "STD-enter-exit-origin-24", key="layout-anim:" + l["sel"])
    if decl.get("transitionAll"):
        F.add("TM-09", "warn", "transition: all", w, f"{decl['transitionAll']} element(s)", "list the properties that change", [], "name the properties (color, background-color, transform, opacity)", "STD-easing-duration-17", key="transition-all")
    durations = mo.get("transitionDurations") or {}
    known = (sysm or {}).get("durations")
    slow = {k: v for k, v in durations.items() if float(k) > UI_MOTION_MS}
    if slow:
        k = max(slow, key=float)
        F.add("TM-09", "info", f"UI transitions longer than {UI_MOTION_MS} ms", w, f"{k} ms on {slow[k]['n']} element(s), e.g. {slow[k]['ex'][0]}", f"under {UI_MOTION_MS} ms unless the motion is illustrative (STD-easing-duration-06)", [slow[k]["ex"][0]], None, "STD-easing-duration-06", key="slow-ui")
    if known:
        odd = {k: v for k, v in durations.items() if all(abs(float(k) - d) > 1 for d in known)}
        if odd:
            rows = sorted(odd.items(), key=lambda kv: -kv[1]["n"])[:4]
            F.add("TM-09", "info", "Transition durations that are not motion tokens", w, "; ".join(f"{k} ms x{v['n']}" for k, v in rows), f"one of: {', '.join(fmt(d) for d in known)} ms", [v["ex"][0] for _, v in rows], "use the duration tokens", "tokens", key="duration-drift")

    mc = p.get("media_counts") or {}
    if mc.get("autoplayVideo"):
        F.add("TM-03", "warn", "A video autoplays", w, f"{mc['autoplayVideo']} video(s)", "muted, and pausable if it runs over 5 s", ["video"], None, "WCAG 2.2.2", key="autoplay")
    for kind, n in (("canvas", mc.get("canvas")), ("video", mc.get("video")), ("SMIL/svg animation", mc.get("smil")), ("Lottie", mc.get("lottie"))):
        if n:
            F.add("TM-05", "info", f"{kind} on the page: its motion is not in the animation list", w, f"{n} found", "sample frames over time and look at them; the probe cannot read this motion", [], None, None, key="opaque-" + kind)
    if mc.get("iframeCross"):
        F.add("CV-01", "info", "Cross-origin iframes were not measured", w, f"{mc['iframeCross']} frame(s)", "review each frame's own URL as its own page", ["iframe"], None, None, key="iframe")
    if doc.get("truncated"):
        F.add("CV-01", "info", "The probe stopped at its element limit", w, f"{doc.get('elements')} elements", "the page is bigger than what was measured", [], "probe a section, or raise MAX_EL", None, key="probe-truncated")


# ------------------------------------------------------------------------- counts against practice (no system needed)
# ------------------------------------------------------------------------- craft: cut text, room, rhythm, copy
# Review cases ST-12 to ST-14, MS-21 to MS-24 and CP-01 to CP-04, plus the tracking rows of MS-17. Each finding names
# the element, the measured value and, when capture.py saved one, a crop of it; each fix uses the project's tokens when
# it has an OpenDesigner system. `decided` says whether a rule decides it (the same answer every time) or it is a
# judgment the reader makes from the evidence (docs/HOW-IT-WORKS.md section 7).
TOUCH_GAP = 4                # text closer than this to a neighbour or to its own box's edge reads as touching [owner, 2026-11-13]
BODY_LINE_HEIGHT = 1.4       # body text under 1.4x its size [owner, 2026-11-13]; WCAG 1.4.8 (AAA) asks 1.5
MEASURE = (45, 75)           # characters per line for body text (Baymard; WCAG 1.4.8 caps it at 80)
RHYTHM_RATIO = 1.5           # the largest space between sections over the smallest, before it reads as uneven [inferred]
GROW = 0.3                   # the translation stand-in: every word 30% longer (W3C, text size in translation)
NON_EXPERT = {"everyone", "general", "public", "novice", "beginner", "beginners", "non-expert", "nonexpert", "consumer", "large", "plain"}

VERBS = set("""accept access activate add adjust agree allow apply approve archive ask assign attach back begin book
browse buy calculate call cancel change chat check choose claim clear click close collapse compare complete configure
confirm connect contact continue copy create customise customize decline delete deny deploy describe disable discard
discover dismiss display do donate download drag duplicate edit email enable end enter explore export filter find finish
fix follow forgot forward generate get give go grant help hide import install invite join keep launch learn leave like
list load log login logout make manage mark meet merge message move mute navigate open order pause pay pick pin place
play post preview print proceed star fork clone publish purchase read redeem register renew reload remind remove rename reorder reply report request reserve
reset resend restart restore resume retry return review run save schedule search see select send set setup share shop
show sign skip sort start stop submit subscribe support swap switch sync take talk tell test track transfer translate try
turn undo unlock unmute unpin unsubscribe update upgrade upload use verify view visit vote watch write zoom""".split())
NOT_VERB_OK = {"next", "previous", "prev", "back", "done", "ok", "okay", "yes", "no", "more", "less", "menu", "close", "all", "new"}
SMALL_WORDS = {"a", "an", "the", "and", "but", "or", "nor", "for", "so", "yet", "as", "at", "by", "in", "of", "off", "on",
               "per", "to", "up", "via", "vs", "with", "from", "into", "onto", "over", "than", "that", "is", "it", "its", "be"}
SYNONYMS = [("sign in", "log in", "login", "signin", "log on"), ("sign up", "register", "create account", "create an account", "join now"),
            ("sign out", "log out", "logout", "signout"), ("delete", "remove", "erase"), ("settings", "preferences", "options"),
            ("buy", "purchase", "order now"), ("contact us", "get in touch", "talk to us"), ("help", "support centre", "help center", "support center")]


def first_up(w):
    return w[:1].isupper()


def proper_words(text):
    """Words written with a capital in the middle of a sentence and never in lower case: names, which keep their capital."""
    caps, low = Counter(), set()
    for sent in re.split(r"(?<=[.!?:])\s+|\n", text or ""):
        ws = re.findall(r"[A-Za-z][\w'’-]*", sent)
        for w in ws[1:]:
            (caps.update([w]) if first_up(w) else low.add(w.lower()))
    return {w for w, n in caps.items() if w.lower() not in low}


def case_of(text, proper):
    """'title', 'sentence' or None (too short, all capitals, or nothing to tell them apart)."""
    ws = re.findall(r"[A-Za-z][\w'’-]*", text)
    if len(ws) < 2 or not first_up(ws[0]):
        return None
    sig = [w for w in ws[1:] if w.lower() not in SMALL_WORDS and not (w.isupper() and len(w) > 1) and not re.search(r"[a-z][A-Z]", w)
           and w not in proper and not re.search(r"\d", w)]
    if not sig:
        return None
    up = sum(first_up(w) for w in sig)
    return "title" if up == len(sig) else "sentence" if up == 0 else None


def tok_px(sysm, want, at_least=False, key="space_tokens"):
    """The project's spacing token nearest to want px (or the smallest at or over it), as 'var(--x) (N px)'; None without a system."""
    toks = (sysm or {}).get(key) or {}
    vals = sorted(v for v in toks if v > 0)
    if not vals:
        return None
    v = min((x for x in vals if x >= want), default=vals[-1]) if at_least else nearest(want, vals)
    return f"var(--{toks[v]}) ({fmt(v)} px)"


def space_hint(sysm, want, at_least=False):
    t = tok_px(sysm, want, at_least)
    if t:
        return t
    grid = (sysm or {}).get("unit") or 4
    v = max(grid, math.ceil(want / grid) * grid) if at_least else max(grid, round(want / grid) * grid)
    return f"{fmt(v)} px (a step of your spacing scale)"


def crops(items):
    return [x["crop"] for x in items if x.get("crop")]


def check_craft(p, sysm, w, F):
    cr = p.get("craft")
    if not cr:
        return
    stress = set(p.get("stress") or [])
    wcag = bool(stress & {"textSpacing", "text200"})
    translate = "translate" in stress
    sfx = (" when every word is 30% longer (a German stand-in)" if translate else " under " + "+".join(sorted(stress))) if stress else ""
    cut_case = "ST-14" if translate else "ST-19" if stress & {"longNames", "noImages"} else "ST-12"
    if "longNames" in stress:
        sfx = " with a 200-character name"
    if "noImages" in stress:
        sfx = " with every image missing"
        F.add("ST-19", "info", "Look at the page with every image missing", w, f"{fmt(((p.get('images') or {}).get('total')))} image(s) made to fail",
              "cards and rows keep their size, and alt text or a placeholder says what was there", [], "reserve the box (width and height or aspect-ratio) and give it a background", None,
              key="no-images", basis="seen", decided="judgment")
    std = "WCAG 1.4.12" if "textSpacing" in stress else "WCAG 1.4.4" if "text200" in stress else None
    vw = (p.get("viewport") or {}).get("w") or 0

    def sev_for(items):
        named = any(x.get("role") in ("heading", "control", "label") for x in items)
        if stress and not wcag:
            return "warn"
        return "error" if named or wcag else "warn"

    # --- text cut off ----------------------------------------------------------------------------------------
    sp = cr.get("spill") or []
    if sp:
        F.add(cut_case, sev_for(sp), "Text runs out of its box" + sfx, w,
              "; ".join(f"{x['sel']} ({x['role']}): \"{x['text']}\" goes {fmt(x['by'])} px "
                        + (f"below a {fmt(x['h'])} px tall box" if x.get("dir") == "down" else f"past a {fmt(x['w'])} px wide box") for x in sp[:4]),
              "every line of text inside its own box, at 320 px, at 200% text and with longer words",
              [x["sel"] for x in sp[:4]] + crops(sp[:4]),
              "let the text wrap: remove the fixed width or height and white-space: nowrap, set min-width: 0 on flex and grid children, "
              "and overflow-wrap: anywhere for long words", std, key="spill" + ("-" + "+".join(sorted(stress)) if stress else ""))
    hp = cr.get("hiddenByParent") or []
    if hp:
        F.add(cut_case, sev_for(hp), "Text cut off by the box around it" + sfx, w,
              "; ".join(f"{x['sel']} ({x['role']}): \"{x['text']}\" loses {fmt(x['cut'])} px inside {x['parent']} (overflow: hidden)" for x in hp[:4]),
              "no text cut by a parent's overflow: hidden; nobody can scroll to it",
              [x["sel"] for x in hp[:4]] + crops(hp[:4]),
              "remove the fixed height or overflow: hidden on the parent, or let it grow (min-height instead of height)", std,
              key="parent-cut" + ("-" + "+".join(sorted(stress)) if stress else ""))
    tr = [x for x in cr.get("truncated") or [] if x.get("role") in ("heading", "control", "label")]
    if tr and not stress:
        F.add("ST-13", "warn", "An ellipsis or line clamp hides words in a heading, button or label", w,
              "; ".join(f"{x['sel']} ({x['role']}, {x['how']}): \"{x['text']}\" needs {fmt(x['needs'])} px {'tall' if x.get('axis') == 'height' else 'wide'}, shows {fmt(x['shown'])}"
                        + (" (full text only in a title tooltip)" if x.get("title") else "") for x in tr[:4]),
              "headings, buttons and labels show every word; truncate only data people can open in full (a file name, a table cell)",
              [x["sel"] for x in tr[:4]] + crops(tr[:4]),
              "let it wrap to two lines (text-wrap: balance) or shorten the words; a title tooltip does not show on touch screens", None, key="truncated")
    orp = cr.get("orphans") or []
    if orp and not stress:
        F.add("MS-21", "warn", "A heading, lede or label ends on one word", w,
              "; ".join(f"{x['sel']} ({x['role']}): \"{x['text']}\" leaves \"{x['word']}\" alone on line {x['lines']}" for x in orp[:4]),
              "no last line of a single word in headings, ledes and labels, at every width (preflight 39)",
              [x["sel"] for x in orp[:4]] + crops(orp[:4]),
              "text-wrap: balance on headings and labels, text-wrap: pretty on ledes; or rewrite the line", "preflight 39", key="orphans")

    # --- breathing room --------------------------------------------------------------------------------------
    tg_all = cr.get("tight") or []
    tg = [x for x in tg_all if x.get("kind", "text") == "text"]
    if tg and not stress:
        F.add("MS-22", "warn", f"Text blocks closer than {TOUCH_GAP} px to each other", w,
              "; ".join((f"{x['sel']} overlaps the text of {x['after']} by {fmt(-x['seen'])} px" if x["seen"] < 0 else f"{x['sel']} sits {fmt(x['seen'])} px from the text of {x['after']}")
                        + f" ({x['axis']}; the boxes are {fmt(x['gap'])} px apart)" for x in tg[:4]),
              f"at least {TOUCH_GAP} px of visible space between neighbouring text, counting half the line height; usually a step of the scale",
              [x["sel"] for x in tg[:4]] + crops(tg[:4]),
              f"add a gap from the scale between them: gap or margin-block-start of {space_hint(sysm, 8, True)}", "tokens", key="tight")
    bx = [x for x in tg_all if x.get("kind") == "boxes-touching" or (x.get("kind") == "boxes" and x["gap"] > 0)]
    if bx and not stress:
        F.add("MS-22", "warn", "Blocks with no gap between them", w,
              "; ".join(f"{x['sel']} is {fmt(x['gap'])} px from {x['after']} ({x['axis']})" for x in bx[:4]),
              "a step of the spacing scale between boxes with rounded corners; boxes that share an edge on purpose have square corners where they meet",
              [x["sel"] for x in bx[:4]] + crops(bx[:4]), f"gap: {space_hint(sysm, 16)} on the parent", "tokens", key="boxes-touching")
    cap = [x for x in tg_all if x.get("kind") == "caption"]
    if cap and not stress:
        F.add("MS-22", "warn", "Text touching the box next to it", w,
              "; ".join(f"{x['sel']} is {fmt(x['seen'])} px from {x['after']} ({x['axis']})" for x in cap[:4]),
              "a caption or label at least 8 px from the box it belongs to", [x["sel"] for x in cap[:4]] + crops(cap[:4]),
              f"margin-block-start: {space_hint(sysm, 8, True)} on the caption", "tokens", key="caption-touching")
    rd = cr.get("radii") or []
    if rd and not stress:
        F.add("MS-25", "warn", "Boxes side by side with different corner radii", w,
              "; ".join(f"{x['sel']}: " + ", ".join(f"{i['sel'].split(' > ')[-1]} {fmt(i['radius'])} px" for i in x["items"][:4]) for x in rd[:3]),
              "one radius for boxes that sit together as a set", [x["items"][0]["sel"] for x in rd[:3]] + crops(rd[:3]),
              "use one radius token for the set" + (f" ({', '.join('var(--' + (sysm or {}).get('prefix', 'ds') + '-radius-' + fmt(v) + ')' for v in ((sysm or {}).get('radius_ladder') or [])[:3])})" if (sysm or {}).get("radius_ladder") else ""),
              "preflight 45", key="radii")
    mp = cr.get("monoProse") or []
    if mp and not stress:
        F.add("MS-26", "warn", "Prose set in a monospace font", w,
              "; ".join(f"{x['sel']}: \"{x['text']}\" in {x['font']}" for x in mp[:4]),
              "monospace for code, numbers in tables and file names; running text in the text face", [x["sel"] for x in mp[:4]] + crops(mp[:4]),
              f"font-family: var(--{(sysm or {}).get('prefix', 'ds')}-font-family-text)" if sysm else "the text font-family token", "DC-L02-03", key="mono-prose")
    bu = cr.get("brokenUrls") or []
    if bu and not stress:
        F.add("MS-27", "warn", "A web address broken across lines" + (", inside \"https://\"" if any(x.get("inScheme") for x in bu) else ""), w,
              "; ".join(f"{x['sel']}: {x['url']} over {x['lines']} lines" + (" (the break is inside https://)" if x.get("inScheme") else "") for x in bu[:4]),
              "an address on one line: show a short form as link text, or let it break only after a slash", [x["sel"] for x in bu[:4]] + crops(bu[:4]),
              "make the link text words (\"install guide\") or drop https://; for an address that must show, overflow-wrap: anywhere breaks anywhere, so wrap the scheme in a nowrap span or insert <wbr> after slashes", "preflight 8", key="broken-url")
    tw = cr.get("twins") or []
    if tw and not stress:
        F.add("ST-15", "warn", "One block lacks a control its twins have", w,
              "; ".join(f"{x['has']} of {x['of']} {x['kind']}s have \"{x['control']}\"; missing on {', '.join(x['missing'][:3])}" for x in tw[:3]),
              "blocks of one kind offer the same controls", [x["sel"] for x in tw[:3]] + crops(tw[:3]),
              "render the control from the block's component, not per page; or say why this one differs", None, key="twins")
    to = cr.get("touching") or []
    if to and not stress:
        F.add("MS-22", "warn", "Text touches the edge of its box", w,
              "; ".join(f"{x['sel']}: \"{x['text']}\" is {fmt(x['inset'])} px from the {x['side']} edge of its {x['edge']}" for x in to[:4]),
              f"text at least {TOUCH_GAP} px inside a box with a visible edge; a chip or button wants 8 px or more at the sides",
              [x["sel"] for x in to[:4]] + crops(to[:4]),
              f"padding of {space_hint(sysm, 8, True)} on the box", "tokens", key="touching")
    ig = cr.get("insetVsGap") or []
    if ig and not stress:
        x0 = ig[0]
        F.add("MS-22", "warn", "Padding smaller than the space between the items inside", w,
              "; ".join(f"{x['sel']}: {fmt(x['inset'])} px padding around items {fmt(x['gap'])} px apart" for x in ig[:4]),
              "the space inside a group at most the space around it (HOW-IT-WORKS section 7: inner spacing smaller than outer)",
              [x["sel"] for x in ig[:4]] + crops(ig[:4]),
              f"raise the padding to {space_hint(sysm, x0['gap'], True)} or lower the gap to {space_hint(sysm, max(x0['inset'], 4))}", "tokens", key="inset-gap")

    # body line height and measure
    meas = cr.get("measure") or []
    prose = (sysm or {}).get("measure") or 65
    lo, hi = MEASURE
    # a short measure counts only in running text (five lines or more, wide screens): a card's blurb is short on purpose
    out_m = [m for m in meas if (m["ch"] > hi and m["ch"] <= MAX_MEASURE_CH) or (m["ch"] < lo and vw >= 600 and m.get("lines", 0) >= 5)]
    if out_m and not stress:
        F.add("MS-07", "warn", f"Body text outside {lo}-{hi} characters a line", w,
              "; ".join(f"{m['sel']}: about {fmt(m['ch'])} characters a line" for m in out_m[:4]),
              f"{lo} to {hi} characters for body text" + (f"; the system's prose measure is {fmt(prose)}ch" if sysm and sysm.get("measure") else ""),
              [m["sel"] for m in out_m[:4]] + crops(out_m[:4]),
              f"max-width: {'var(--' + sysm['measure_token'] + ')' if sysm and sysm.get('measure_token') else str(prose) + 'ch'} on the text block, or a wider column",
              "WCAG 1.4.8 (AAA)", key="measure-range")

    # --- spacing ---------------------------------------------------------------------------------------------
    sib_all = cr.get("siblings") or []
    sib = [x for x in sib_all if x.get("distinct", 3) >= 3]
    two = [x for x in sib_all if x.get("distinct", 3) == 2]
    if two and not stress:
        F.add("MS-23", "info", "Siblings of one kind with two different gaps", w,
              "; ".join(f"{x['sel']}: {x['kind'].split('@')[0]} items {', '.join(fmt(g) for g in x['gaps'])} px apart" for x in two[:4]),
              "one gap, or a larger one only where a new group starts", [x["sel"] for x in two[:4]] + crops(two[:4]),
              f"if it is not a group break, one gap on the parent ({space_hint(sysm, Counter(two[0]['gaps']).most_common(1)[0][0])})", "tokens",
              key="siblings-two", decided="judgment")
    if sib and not stress:
        def most(g):
            return Counter(g).most_common(1)[0][0]
        F.add("MS-23", "warn", "Items of one kind spaced unevenly", w,
              "; ".join(f"{x['sel']}: {x['kind'].split('@')[0]} items {', '.join(fmt(g) for g in x['gaps'])} px apart ({x['axis']})" for x in sib[:4]),
              "one gap between siblings of the same kind",
              [x["sel"] for x in sib[:4]] + crops(sib[:4]),
              f"set one gap on the parent ({space_hint(sysm, most(sib[0]['gaps']))}) and drop the margins on single items", "tokens", key="siblings")
    vh = (p.get("viewport") or {}).get("h") or 800
    secs = [s for s in cr.get("sections") or [] if 0 < s["space"] < vh]   # a gap taller than the screen is not rhythm: content the probe could not see
    if len(secs) >= 3 and not stress:
        vals = [s["space"] for s in secs]
        steps = sorted({round(v / 8) * 8 for v in vals})
        if max(vals) / max(min(vals), 1) >= RHYTHM_RATIO and len(steps) >= 3:
            F.add("MS-24", "warn", "Uneven space between sections", w,
                  "; ".join(f"{fmt(s['space'])} px before {s['sel']}" for s in secs[:6]),
                  "the same space between sections down the page, or a bigger one only where a new part starts, on purpose",
                  [s["sel"] for s in secs[:4]] + crops(secs[:4]),
                  f"one section spacing token, for example padding-block: {space_hint(sysm, sorted(vals)[len(vals) // 2])}; check each larger break is meant",
                  "tokens", key="rhythm", decided="judgment")

    # --- tracking by role (kerning.md: tight on display sizes, near 0 on body, slightly positive on small text) --
    rows = []
    for k, v in ((p.get("type") or {}).get("tracking") or {}).items():
        try:
            fs, em, caps, *mono = k.split("|")
            if mono:          # code and other monospace text sits at 0 (kerning.md)
                continue
            rows.append((float(fs), float(em), caps == "1", v))
        except ValueError:
            continue
    tk = (sysm or {}).get("tracking") or {}
    tok = (sysm or {}).get("tracking_tokens") or {}

    def use(role, default):
        want = tk.get(role, default)
        name = tok.get(role)
        return f"letter-spacing: var(--{name}) ({fmt(want)}em)" if name else f"letter-spacing: {fmt(want)}em"
    if rows and not stress:
        body_hi = tk.get("body", 0) + 0.01
        small_lo = min(0, tk.get("small", 0)) - 0.005
        has_disp = "display" in tk or "heading" in tk
        disp_want = max(tk.get("display", -0.02), tk.get("heading", -0.02)) if has_disp else -0.01   # the looser of the system's two
        disp_hi = disp_want + 0.005
        caps_lo = min(0.02, tk.get("caps-label", 0.05))
        checks = [
            ("Body text tracked open", lambda fs, em, c, v: 14 <= fs <= 20 and not c and em > body_hi and v.get("chars", 0) >= 80 and v.get("chars", 0) / max(v.get("n", 1), 1) >= 40,
             f"about {fmt(tk.get('body', 0))}em on body text", use("body", 0)),
            ("Small text tracked tight", lambda fs, em, c, v: fs < 14 and not c and em < small_lo,
             "0em or a little more under 14 px, never negative" + (f" (the system's small text: {fmt(tk['small'])}em)" if "small" in tk else ""), use("small", 0.01)),
            ("Capitals with no tracking", lambda fs, em, c, v: c and 0 <= em < caps_lo and v.get("chars", 0) / max(v.get("n", 1), 1) >= 6,
             f"capitals tracked open, about {fmt(tk.get('caps-label', 0.06))}em", use("caps-label", 0.06)),
            ("Display text not tightened", lambda fs, em, c, v: fs >= 32 and not c and em > (disp_hi if has_disp else -0.001),
             f"{fmt(disp_want)}em or tighter at display sizes" + (" (the system's heading and display tracking)" if has_disp else " (about -0.01 to -0.02em, unless the face has a display cut)"),
             use("heading" if tk.get("heading", -1) >= tk.get("display", -1) and "heading" in tk else "display", disp_want)),
        ]
        for title, test, exp, fix in checks:
            hit = [(fs, em, v) for fs, em, c, v in rows if test(fs, em, c, v)]
            if hit:
                F.add("MS-17", "warn", title, w, "; ".join(f"{fmt(fs)} px at {fmt(em)}em, e.g. {v['ex'][0] if v.get('ex') else '?'}" for fs, em, v in hit[:4]),
                      exp, [v["ex"][0] for _, _, v in hit[:4] if v.get("ex")], fix, "kerning.md", key="track-" + title)


def jargon_terms():
    """Terms from the glossary a non-expert would not know: acronyms, token words and code names, each with its plain words."""
    path = HERE.parent / "references" / "glossary.json"
    try:
        g = json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    out = []
    for t in g if isinstance(g, list) else g.get("terms", []):
        term = t.get("term") or ""
        if "(" in term and not re.match(r"^[A-Z]{2,}", term):
            continue
        base = re.sub(r"\s*\(.*\)$", "", term).strip()
        names = [base] + [a for a in t.get("aliases") or [] if a]
        jar = [n for n in names if re.fullmatch(r"[A-Z][A-Z0-9]{1,6}(\.md)?", n) or "token" in n.lower() or t.get("layer") == "tok"]
        if t.get("code_name") and re.fullmatch(r"[a-z]+(\.[a-z0-9-]+){2,}", t["code_name"]):
            jar.append(t["code_name"])
        for n in dict.fromkeys(jar):
            out.append((n, t.get("plain") or ""))
    return out


def check_copy(p, sysm, w, F, audience=None):
    cp = p.get("copy")
    if not cp or p.get("stress"):
        return
    lang = ((p.get("doc") or {}).get("lang") or "en").lower()
    english = lang.startswith("en")
    proper = proper_words(cp.get("text", ""))
    heads = [h for h in cp.get("headings") or [] if not h.get("upper")]
    btns = [c for c in cp.get("controls") or [] if c["kind"] == "button" and not c.get("menu") and not c.get("toggle") and not c.get("upper")]   # a toggle names a state, not an action

    # CP-01 Title Case where the system says sentence case
    rule = (sysm or {}).get("case")
    if english:
        kinds = [("heading", heads), ("button", btns)]
        for kind, items in kinds:
            cases = [(x, case_of(x["text"], proper)) for x in items]
            titled = [x for x, c in cases if c == "title"]
            sentence = [x for x, c in cases if c == "sentence"]
            if not titled:
                continue
            wants = "sentence" if rule == "sentence" or (rule == "title-headings" and kind == "button") else None
            if wants:
                F.add("CP-01", "warn", f"Title Case {kind}s where the system says sentence case", w,
                      "; ".join(f"{x['sel']}: \"{x['text']}\"" for x in titled[:4]), "sentence case: a capital on the first word and on names only (Q-voice-03)",
                      [x["sel"] for x in titled[:4]] + crops(titled[:4]), "rewrite in sentence case; never fake case with text-transform", "Q-voice-03", key="case-" + kind)
            elif rule != "title-headings" and len(sentence) > len(titled):
                F.add("CP-01", "info", f"Mixed case in {kind}s: most are sentence case, some are Title Case", w,
                      "; ".join(f"{x['sel']}: \"{x['text']}\"" for x in titled[:4]) + f" ({len(sentence)} in sentence case)",
                      "one capitalisation rule per kind of text", [x["sel"] for x in titled[:4]] + crops(titled[:4]),
                      "pick one (sentence case by default) and record it: engine.py pick Q-voice-03 sentence", "Q-voice-03", key="case-mix-" + kind, decided="judgment")

    # CP-02 a button label that does not start with a verb
    if english:
        nv = []
        for b in btns:
            first = (re.findall(r"[A-Za-z][\w'’-]*", b["text"]) or [""])[0].lower()
            if not first or first in VERBS or first in NOT_VERB_OK or first.rstrip("s") in VERBS:
                continue
            nv.append(b)
        if nv:
            F.add("CP-02", "info", "Button labels that do not start with a verb", w, "; ".join(f"{x['sel']}: \"{x['text']}\"" for x in nv[:5]),
                  "a button says what it does: a verb first (\"Compare prices\", not \"Pricing details\")",
                  [x["sel"] for x in nv[:5]] + crops(nv[:5]), "start with the action; a word list decided this, so read each one", "DC-L06-22", key="not-verb", decided="judgment")

    # CP-03 one action, two names
    labels = {}
    for c in cp.get("controls") or []:
        t = re.sub(r"[\s→↗>»›→]+$", "", c["text"].lower()).strip()
        labels.setdefault(t, c)
    dup = []
    for group in SYNONYMS:
        found = [labels[g] for g in group if g in labels]
        if len(found) >= 2:
            dup.append(found)
    if dup and english:
        F.add("CP-03", "warn", "One action named two ways on the page", w,
              "; ".join(" and ".join(f"\"{x['text']}\" ({x['sel']})" for x in grp) for grp in dup[:3]),
              "one name for each action, everywhere", [grp[0]["sel"] for grp in dup[:3]] + [grp[1]["sel"] for grp in dup[:3]],
              "pick one name and use it on every button and link", "DC-L06-22", key="synonyms")
    by_href = {}
    for c in cp.get("controls") or []:
        if c["kind"] == "button" and c.get("href") and not c["href"].startswith("#"):
            by_href.setdefault(c["href"], {}).setdefault(re.sub(r"[\d,.]+[kmKM]?\b|\s+$", "", c["text"]).strip().lower(), c)   # a count is not a name
    two = [(h, list(v.values())) for h, v in by_href.items() if len(v) >= 2 and not any(a in b for a in v for b in v if a != b)]
    if two:
        F.add("CP-03", "info", "Buttons to the same place with different names", w,
              "; ".join(f"{h}: " + " / ".join(f"\"{x['text']}\"" for x in xs[:3]) for h, xs in two[:3]),
              "one action, one name", [xs[0]["sel"] for _, xs in two[:3]], "use the same words, unless the two do different things", "DC-L06-22",
              key="same-href", decided="judgment")

    # CP-04 jargon on a page marked for non-experts
    aud = (audience or cp.get("audience") or (sysm or {}).get("audience") or "").lower()
    if english and aud and any(a in aud for a in NON_EXPERT):
        text = "\n".join([cp.get("text", "")] + [h["text"] for h in cp.get("headings") or []] + [c["text"] for c in cp.get("controls") or []])
        hits = []
        for name, plain in jargon_terms():
            rx = re.compile(r"(?<![\w.-])" + re.escape(name) + r"s?(?![\w-])", 0 if name[:2].isupper() or "." in name else re.I)
            m = rx.search(text)
            if m and name.lower().rstrip("s") not in {h[0].lower().rstrip("s") for h in hits} and m.group(0).lower().rstrip("s") not in {h[2].lower().rstrip("s") for h in hits}:
                hits.append((name, plain, m.group(0)))
        if hits:
            F.add("CP-04", "info", f"Words a non-expert may not know ({len(hits)})", w,
                  "; ".join(f"\"{h[2]}\"" for h in hits[:8]), f"plain words on a page marked for {aud}",
                  [], "; ".join(f"{h[0]}: say \"{h[1][:90]}\"" for h in hits[:3]), "glossary.json (plain voice)", key="jargon", decided="judgment")


def hsl(hx):
    r, g, b = (v / 255 for v in hex_rgb(hx))
    mx, mn = max(r, g, b), min(r, g, b)
    l, d = (mx + mn) / 2, mx - mn
    if d == 0:
        return 0.0, 0.0, l
    s = d / (1 - abs(2 * l - 1))
    h = ((g - b) / d) % 6 if mx == r else (b - r) / d + 2 if mx == g else (r - g) / d + 4
    return h * 60, s, l


HUE_NAMES = ((15, "red"), (40, "orange"), (65, "yellow"), (165, "green"), (195, "teal"), (250, "blue"), (290, "purple"), (345, "pink"), (361, "red"))
SYSTEM_FACE = {"system-ui": "the system font", "-apple-system": "the system font", "blinkmacsystemfont": "the system font", "ui-sans-serif": "the system font",
               "ui-rounded": "the system font", "sans-serif": "the system font", "serif": "the browser's serif", "ui-serif": "the browser's serif",
               "monospace": "the system mono", "ui-monospace": "the system mono"}
MONO_FACE = re.compile(r"mono|code|courier|consol|menlo|monaco", re.I)
ICON_FACE = re.compile(r"icon|awesome|symbol|glyph|emoji|dashicons", re.I)


def hue_family(hx):
    """A plain name for a chromatic color ("blue"), or None for grays, near-black and near-white."""
    rgb = hex_rgb(hx)
    h, s, l = hsl(hx)
    if max(rgb) - min(rgb) < 30 or s < 0.2 or l < 0.12 or l > 0.94:
        return None
    return next(name for top, name in HUE_NAMES if h < top)


def opaque_colors(p):
    """Every opaque text, background and border color the probe saw, with its uses and one element. A translucent value
    is left out: how it looks depends on what is behind it."""
    out = {}
    for kind in ("text", "bg", "border"):
        for k, v in ((p.get("colors") or {}).get(kind) or {}).items():
            if len(k) != 7:
                continue
            e = out.setdefault(k.lower(), {"n": 0, "ex": []})
            e["n"] += v.get("n", 0)
            if v.get("ex") and not e["ex"]:
                e["ex"] = v["ex"][:1]
    return out


def check_practice(p, sysm, w, F):
    """What any built page can be judged on without a design system: how many actions shout, and how many typefaces,
    weights and colors are in use, each against a practice with its source. Warnings and notes only: a count past the
    practice is a question for the person, not a fault (opendesigner references/audit.md)."""
    ty = p.get("type") or {}
    label = lambda b: f"\"{b.get('text') or b['sel']}\" ({b['fill']})"

    # --- primary actions ------------------------------------------------------------------------------------
    strong = [b for b in ((p.get("buttons") or {}).get("filled") or []) if (b.get("ratio") or 0) >= PRIMARY_RATIO and b.get("word", True)]   # icon buttons are not calls to action
    first = [b for b in strong if b.get("first")]
    groups = {}
    for b in strong:
        groups.setdefault(b.get("group") or b["sel"], []).append(b)
    near = lambda a, b: abs(a.get("y", 0) - b.get("y", 0)) <= max(a.get("h", 0), b.get("h", 0)) + 16   # one row, or stacked with no gap to speak of
    side = [pair for g in groups.values() for pair in [next(([a, b] for i, a in enumerate(g) for b in g[i + 1:] if near(a, b)), None)] if pair]
    vh = (p.get("viewport") or {}).get("h") or 0
    bands = Counter(int(b["y"] // vh) for b in strong if vh and not b.get("first") and b.get("y") is not None)
    later = sorted(k for k, n in bands.items() if n > 1)
    if len(first) > 1 or side or later:
        parts = []
        if len(first) > 1:
            parts.append(f"{len(first)} filled buttons stand out in the first screen: " + ", ".join(label(b) for b in first[:5]) + (f" (+{len(first) - 5} more)" if len(first) > 5 else ""))
        for g in side[:2]:
            parts.append(" and ".join(label(b) for b in g[:3]) + " sit side by side, both filled" + ("" if any(b.get("first") for b in g) else ", further down"))
        if later:
            parts.append("further down, " + ", ".join(f"{bands[k]} in the screen at about {fmt(k * vh)} px" for k in later[:3]))
        texts = Counter(b.get("text") for b in strong if b.get("text"))
        rep = [t for t, n in texts.most_common() if n >= 3]
        if rep:
            parts.append(f"\"{rep[0]}\" repeats {texts[rep[0]]} times: an action on every row is usually a quiet one")
        title = f"{len(first)} primary buttons in the first screen" if len(first) > 1 else "Two filled buttons side by side" if side else "More than one primary button in one screen"
        F.add("MS-16", "warn", title, w, "; ".join(parts),
              "one primary button per view, for the one action the view exists for; the others quieter (an outline or a text link), and nothing the header already offers repeated as a button "
              "(preflight 36; DC-L08-05: one primary per view; DC-L13-18: at most one per group or dialog)",
              [b["sel"] for b in (first if len(first) > 1 else side[0] if side else [x for x in strong if not x.get("first") and int(x["y"] // vh) in later])[:4]],
              "keep the fill on the one action this view is for and make the others outline or text buttons; opposite actions go on one row, secondary left, primary right (preflight 41)",
              "preflight 36", key="primary-many")
    styles = {}
    for b in strong:
        if hue_family(b["fill"]) != "red":       # a red fill is the danger button, a level of its own (DC-L08-05)
            styles.setdefault(b["fill"], []).append(b)
    if len(styles) >= 2:
        rows = sorted(styles.items(), key=lambda kv: -len(kv[1]))
        F.add("MS-16", "warn", f"{len(styles)} different fills for the main button", w,
              "; ".join(f"{fill} on " + ", ".join(f"\"{b.get('text') or b['sel']}\"" for b in bs[:3]) for fill, bs in rows[:4]),
              "one primary style, the same on every page, plus red for an action that destroys something (DC-L08-05; STD-visual-details-36: same look, same behaviour)",
              [bs[0]["sel"] for _, bs in rows[:4]], "pick one fill for the main action and use it everywhere; give the other buttons the secondary style",
              "STD-visual-details-36", key="primary-styles")

    # --- button styles and labels -----------------------------------------------------------------------------
    btns = (p.get("buttons") or {}).get("styles") or []
    kinds = {}
    for b in btns:
        kinds.setdefault((b["kind"], b["radius"], round(b["h"] / 4) * 4, b["fs"], b["upper"]), []).append(b)
    radii, heights, cases = {k[1] for k in kinds}, {k[2] for k in kinds}, {k[4] for k in kinds}
    if len(kinds) > BUTTON_STYLES or len(radii) > 1 or len(cases) > 1:
        rows = sorted(kinds.items(), key=lambda kv: -len(kv[1]))
        notes = ([f"{len(radii)} corner shapes"] if len(radii) > 1 else []) + ([f"{len(heights)} heights"] if len(heights) > 3 else []) + (["UPPERCASE and normal case mixed"] if len(cases) > 1 else [])
        F.add("MS-19", "warn", f"{len(kinds)} button styles" if len(kinds) > BUTTON_STYLES else "Buttons with different corners or case", w,
              "; ".join(f"{k[0]}, {'pill' if k[1] == 'pill' else fmt(k[1]) + ' px corners'}, {fmt(k[2])} px tall, {fmt(k[3])} px{' caps' if k[4] else ''}: \"{v[0]['text']}\"" for k, v in rows[:5]) + ("; " + ", ".join(notes) if notes else ""),
              "a primary, a secondary and at most one quieter style, sharing one corner shape, one case and a height scale such as 32, 40 and 48 px (DC-L08-05; DC-L08-07; STD-visual-details-36)",
              [v[0]["sel"] for _, v in rows[:4]], "make every button from one component with a size and a variant; the corner shape is one decision for all of them", "DC-L08-07", key="button-styles")
    small = [b for b in strong if b.get("fs") and b["fs"] < PRIMARY_LABEL]
    tiny = [b for b in btns if b.get("upper") and b.get("fs") and b["fs"] < TINY_CAPS]
    if small or tiny:
        F.add("MS-19", "warn", "Button labels too small", w,
              "; ".join([f"primary \"{b['text']}\" at {fmt(b['fs'])} px" for b in small[:3]] + [f"capitals \"{b['text']}\" at {fmt(b['fs'])} px" for b in tiny[:3]]),
              f"a primary label of {PRIMARY_LABEL} px or more (owner review 2026-11-05), and no capitals under {TINY_CAPS} px on a button",
              [b["sel"] for b in (small + tiny)[:4]], "raise the label to the body size or a step above; drop uppercase on small labels", None, key="button-labels")

    # --- type sizes -------------------------------------------------------------------------------------------
    sizes = {}
    for k, v in (ty.get("sizes") or {}).items():
        try:
            sizes[float(k)] = v
        except ValueError:
            continue
    whole = sorted({round(s * 2) / 2 for s in sizes})
    if len(whole) > TYPE_SIZES:
        close = [(a, b) for a, b in zip(whole, whole[1:]) if a and (b - a) / a < 0.10]
        F.add("MS-02", "warn", f"{len(whole)} font sizes", w, ", ".join(fmt(s) for s in whole) + (f"; within 10% of each other: {', '.join(f'{fmt(a)}/{fmt(b)}' for a, b in close[:4])}" if close else ""),
              f"about {TYPE_SIZES} sizes at most, all from one scale, none within 10% of another (preflight 7)", [], "map each size to the nearest step of one scale", "preflight 7", key="type-count")
    frac = {s: v for s, v in sizes.items() if abs(s - round(s)) >= 0.05}
    if frac:
        uses = sum(v["n"] for v in frac.values())
        total = sum(v["n"] for v in sizes.values()) or 1
        F.add("MS-02", "warn" if len(frac) >= 2 or uses / total >= 0.1 else "info", "Font sizes between whole pixels", w,
              "; ".join(f"{fmt(s)} px x{v['n']}" for s, v in sorted(frac.items())[:6]),
              "whole-pixel sizes from the scale: a fluid size (clamp, vw) or an rem step that does not land on a pixel gives a different size at every width, so nothing matches (preflight 7)",
              [v["ex"][0] for v in frac.values() if v.get("ex")][:4], "step the size at breakpoints instead of a fluid clamp, or round the scale to whole pixels; 13.33 px on a button is the browser default", "preflight 7", key="type-frac")

    # --- typefaces ------------------------------------------------------------------------------------------
    faces = {}
    for fam, v in (ty.get("families") or {}).items():
        name = SYSTEM_FACE.get(fam.strip().lower(), fam.strip())
        if not name or ICON_FACE.search(name):
            continue
        e = faces.setdefault(name, {"n": 0, "chars": 0, "ex": []})
        e["n"] += v.get("n", 0)
        e["chars"] += v.get("chars", 0)
        if v.get("ex") and not e["ex"]:
            e["ex"] = v["ex"][:1]
    mono = [f for f in faces if MONO_FACE.search(f) or f == "the system mono"]
    text = [f for f in faces if f not in mono]
    if len(text) >= TEXT_FACES or len(mono) > 1:
        rows = sorted(faces.items(), key=lambda kv: -kv[1]["chars"])
        over = len(text) > TEXT_FACES or len(mono) > 1
        F.add("MS-02", "warn" if over else "info", f"{len(faces)} typefaces on one page" if over else "Two text typefaces", w,
              "; ".join(f"{f} on {v['n']} element(s)" + (" (mono)" if f in mono else "") for f, v in rows[:6]),
              "one family for the interface, plus a mono for code; a second text face only with a named job, such as display headings on a marketing page (DC-L02-03; quality.md Q3: one or two typefaces)",
              [v["ex"][0] for _, v in rows if v["ex"]][:4],
              "move the text set in the extra faces to the main family; a face used on a handful of elements is usually a leftover" if over
              else "keep the second face only if it has a named job (display headings, a marketing page); inside the product, one family is the default",
              "DC-L02-03", key="faces-count")

    # --- weights --------------------------------------------------------------------------------------------
    ws = {}
    for k, v in (ty.get("weights") or {}).items():
        try:
            ws[int(float(k))] = v
        except ValueError:
            continue
    order = sorted(ws)
    close = [(a, b) for a, b in zip(order, order[1:]) if b - a <= 100]
    if len(order) >= WEIGHTS_SYSTEM or close:
        over = len(order) > WEIGHTS_SYSTEM or bool(close)
        title = (f"{len(order)} font weights on one page" if len(order) > WEIGHTS_SYSTEM else "Font weights one step apart" if close else "Three font weights in one view")
        F.add("MS-02", "warn" if over else "info", title, w,
              ", ".join(f"{k} on {ws[k].get('n', 0)} element(s)" for k in order) + "".join(f"; {a} and {b} are one step apart, which can read as a mistake rather than a level" for a, b in close[:2]),
              "three weights at most in a system, and two in any one view, clearly apart, such as 400 and 600 (DC-L19-24; it marks two neighbouring weights reading as a mistake as inferred)",
              [ws[k]["ex"][0] for k in order if ws[k].get("ex")][:4], "give each weight a job (body, labels, headings) and merge the near ones; try size or space before a third weight",
              "DC-L19-24", key="weights-count")

    # --- colors ---------------------------------------------------------------------------------------------
    cols = opaque_colors(p)
    fams = {}
    for hx, v in cols.items():
        f = hue_family(hx)
        if f:
            e = fams.setdefault(f, {"n": 0, "hexes": [], "ex": []})
            e["n"] += v["n"]
            e["hexes"].append(hx)
            if v["ex"] and not e["ex"]:
                e["ex"] = v["ex"]
    if len(fams) >= HUE_NOTE:
        rows = sorted(fams.items(), key=lambda kv: -kv[1]["n"])
        F.add("MS-08", "warn" if len(fams) >= HUE_WARN else "info", f"{len(fams)} color families on one page", w,
              "; ".join(f"{name} ({', '.join(e['hexes'][:3])}) x{e['n']}" for name, e in rows),
              "grays, one accent with one job, and status colors (DC-L01-08), with the danger color only on the part that is going wrong (making.md section 12: \"More visual\" means more information, not more colour)",
              [e["ex"][0] for _, e in rows if e["ex"]][:4], "pick the one accent; turn decorative colors gray; keep status colors for status, and red only on the part that is going wrong",
              "DC-L01-08", key="hues-count")
    tc = (p.get("colors") or {}).get("text") or {}
    greys = {k.lower(): v for k, v in tc.items() if len(k) == 7 and k.lower() != "#ffffff" and not hue_family(k)}
    if len(greys) > TEXT_GREYS:
        rows = sorted(greys.items(), key=lambda kv: -kv[1].get("n", 0))
        F.add("MS-08", "warn" if len(greys) > TEXT_GREYS + 1 else "info", f"{len(greys)} gray text colors", w,
              "; ".join(f"{k} x{v.get('n', 0)}" for k, v in rows[:6]),
              "three: main text, secondary text and hints (DC-L15-02), each at 4.5:1 or more on its background (WCAG 1.4.3)",
              [v["ex"][0] for _, v in rows if v.get("ex")][:4], "give each gray one of the three jobs and replace the rest with it", "DC-L15-02", key="greys-count")
    if not (sysm or {}).get("palette"):   # with a palette, the drift check above already names the nearest token
        clusters = []
        for hx, v in sorted(cols.items(), key=lambda kv: -kv[1]["n"]):
            for c in clusters:
                if math.dist(hex_rgb(hx), hex_rgb(c[0][0])) <= NEAR_SAME:
                    c.append((hx, v))
                    break
            else:
                clusters.append([(hx, v)])
        twins = [c for c in clusters if len(c) > 1]
        if twins:
            uses = sum(v["n"] for c in twins for _, v in c[1:])
            F.add("MS-08", "warn" if uses >= 5 else "info", f"Colors that look the same but are typed differently ({len(twins)} group{'s' if len(twins) > 1 else ''})", w,
                  "; ".join(" = ".join(f"{hx} x{v['n']}" for hx, v in c[:4]) for c in twins[:4]) + f" ({len(cols)} opaque colors in all)",
                  "one value per color, named once and reused (STD-visual-details-26: never a parallel set; preflight 2: count the values that do not come from one system)",
                  [v["ex"][0] for c in twins for _, v in c[1:2] if v.get("ex")][:4], "keep the most used value in each group and replace the others with it: the first step towards a palette",
                  "STD-visual-details-26", key="near-same")


def check_round(p, w, F):
    """What the owner kept catching on a private B2B landing page (owner review 2026-11-03 and 2026-11-05), read from one
    probe run: tracking, heading length, alignment, fonts nobody uses, launch basics, and a page measured mid-animation."""
    ty, mo = p.get("type") or {}, p.get("motion") or {}
    if mo.get("pending") and not (p.get("media") or {}).get("reducedMotion"):
        F.add("TM-01", "warn", "Measured while animations were still running", w, f"{mo['pending']} animation(s) or transition(s) not finished: " + "; ".join(mo.get("pendingOn") or []),
              "the resting page: reveals finished before anything is measured or photographed", [], "await __od.settle() before probe.js and before each screenshot (capture.py does), then measure again", None, key="pending")

    # --- tracking ---------------------------------------------------------------------------------------------
    caps = ty.get("capsTight") or []
    if caps:
        F.add("MS-17", "error", "Capitals with negative tracking", w, "; ".join(f"{c['sel']} \"{c['text']}\" at {fmt(c['em'])}em, {fmt(c['fs'])} px" for c in caps[:4]),
              "capitals tracked open (about +0.02 to +0.08em), never tight: capital shapes have no side bearings to spare, so negative tracking makes them collide (preflight 5)",
              [c["sel"] for c in caps[:4]], "set letter-spacing on uppercase text to a positive caps token, for example 0.04em", "preflight 5", key="caps-tight")
    rows = []
    for k, v in (ty.get("tracking") or {}).items():
        try:
            fs, em, cap = k.split("|")
            rows.append((float(fs), float(em), cap == "1", v))
        except ValueError:
            continue
    plain = sorted((r for r in rows if not r[2] and r[3].get("chars", 0) >= 8), key=lambda r: r[0])
    back = [(a, b) for i, a in enumerate(plain) for b in plain[i + 1:] if b[0] >= a[0] * 1.25 and b[1] > a[1] + 0.005]
    if back:
        a, b = max(back, key=lambda ab: ab[1][1] - ab[0][1])
        F.add("MS-17", "warn", "Tracking gets looser as text gets bigger", w, f"{fmt(b[0])} px is tracked {fmt(b[1])}em but {fmt(a[0])} px is tracked {fmt(a[1])}em ({len(back)} pair(s) like this)",
              "tracking tightens as size grows: body near 0, display text slightly negative, only capitals and tiny labels open (preflight 5; the system's tracking per size)",
              [b[3]["ex"][0], a[3]["ex"][0]], "give the large sizes the tighter value; set tracking with each text style, not per element", "preflight 5", key="track-back")
    values = sorted({round(r[1], 3) for r in rows if r[1]})
    if len(values) > TRACKING_VALUES:
        F.add("MS-17", "warn", f"{len(values)} letter-spacing values", w, ", ".join(f"{fmt(v)}em" for v in values[:12]),
              f"about {TRACKING_VALUES}: one for body, one or two for display sizes, one for capitals; each comes with its text style [inferred]",
              [], "fold letter-spacing into the type tokens and remove the per-element values", "preflight 5", key="track-count")

    # --- headings that run long ------------------------------------------------------------------------------
    long = (ty.get("headings") or {}).get("long") or []
    if long:
        F.add("MS-18", "warn", f"Headings over {HEADING_LINES} lines", w, "; ".join(f"h{h['level']} \"{h['text']}\" runs to {h['lines']} lines at {fmt(h['fs'])} px" for h in long[:3]),
              f"a heading reads in one glance: {HEADING_LINES} lines at most at every width (owner review 2026-11-03)", [h["sel"] for h in long[:4]],
              "shorten the words, or step the size down at this width (a smaller text style, not a fluid clamp that lands between steps)", None, key="head-lines")

    # --- alignment ------------------------------------------------------------------------------------------
    lay = p.get("layout") or {}
    for m in (lay.get("mixed") or [])[:3]:
        F.add("MS-05", "warn", "Mixed alignment under one heading", w,
              f"\"{m['heading']}\" is {m['align']}-aligned; " + "; ".join(f"{i['sel']} is {i['align']}" for i in m["items"][:3]),
              "a heading and the lede, list and buttons under it share one alignment (owner review 2026-11-04 rows 28 to 32: centre headings, lists aligned to them)",
              [m["group"]] + [i["sel"] for i in m["items"][:3]], "align the items with their heading: text-align and the row's justify-content together", None, key="mixed:" + m["group"])
    off = lay.get("offCentre") or []
    if off:
        F.add("MS-05", "warn", "Centred items off the centre line", w, "; ".join(f"{o['sel']} \"{o['text']}\" is {fmt(o['off'])} px off the centre of {o['section']}" for o in off[:3]),
              "centred means within 2 px of its section's centre (preflight 35)", [o["sel"] for o in off[:4]],
              "look for a one-sided padding, margin or a hidden icon on one side; centre the box, then the text in it", "preflight 35", key="off-centre")

    # --- fonts nobody uses, and launch basics ----------------------------------------------------------------
    fo = p.get("fonts") or {}
    if fo.get("unused"):
        F.add("EN-08", "warn", "Fonts downloaded but not used", w, f"{len(fo['unused'])} of {fo.get('loadedFamilies')} loaded families draw no visible text: " + ", ".join(f"{u['family']} ({u['faces']} face(s))" for u in fo["unused"][:5]),
              "load only the families and weights the page draws (one or two families, preflight 10)", [], "remove the @font-face, preload or font link for these; text drawn only by ::before or ::after is not counted, so check an icon font first", "preflight 10", key="fonts-unused")
    check_launch(p, w, F)


# ---- launch files: share text and image, and review tools left on a public address (EN-07, EN-09) ---------------
STOPWORDS = set("""a an and are as at be but by can do for from get has have how in into is it its just more most new no not now
of off on one or our out over so than that the their them then there these they this to up us was we what when where which who
why will with you your all any every each also been being here home page site website welcome official""".split())
SHARE_TITLE_MIN = 0.34   # [inferred] a title shares at least a third of its words with the h1 and the line under it
SHARE_TEXT_MIN = 0.25    # [inferred] a description, a quarter: descriptions paraphrase


def content_words(text):
    """The words that carry meaning, cut to a rough stem so 'invoices' meets 'invoicing' and 'chase' meets 'chasing'."""
    out = set()
    for w in re.findall(r"[a-z0-9]+", (text or "").lower()):
        if len(w) < 3 or w in STOPWORDS:
            continue
        for suf in ("ing", "ed", "es", "s", "e"):
            if w.endswith(suf) and len(w) - len(suf) >= 4:
                w = w[: -len(suf)]
                break
        out.add(w[:6])
    return out


def said_on_page(field, page, brand, split):
    """(words found, words, missing) for a share field against the page's words; a title is judged by its best part,
    so 'Invoices that chase themselves | Acme' is not marked down for the brand. None when there is too little to judge."""
    best = None
    for part in [field] + (re.split(r"\s+[|·•–—-]\s+|:\s+", field) if split else []):
        ws = content_words(part) - brand
        if len(ws) < 2:
            continue
        r = (len(ws & page), len(ws), sorted(ws - page))
        if best is None or r[0] / r[1] > best[0] / best[1]:
            best = r
    return best


def public_host(url):
    """An address visitors can reach: not a file, loopback, private network or reserved test name."""
    u = urlparse(url or "")
    h = (u.hostname or "").lower()
    if u.scheme not in ("http", "https") or not h:
        return False
    return not (h in ("localhost", "::1") or h.startswith(("127.", "0.")) or h.endswith((".localhost", ".local", ".test", ".example", ".internal"))
                or re.match(r"^(10|192\.168|172\.(1[6-9]|2\d|3[01]))\.", h))


def check_launch(p, w, F):
    sh = p.get("share") or {}
    noindex = re.search(r"noindex", sh.get("robots") or "", re.I)
    if sh and (not sh.get("image") or not sh.get("icon") or noindex):
        miss = [x for x, ok in (("a share image (og:image)", sh.get("image")), ("a favicon", sh.get("icon")), ("a meta description", sh.get("description"))) if not ok]
        F.add("EN-09", "info", "Before launch: share image, favicon or indexing", w, ("missing " + ", ".join(miss) if miss else "") + (("; " if miss else "") + f"robots says {sh['robots']}" if noindex else ""),
              "a public page has a share image, a favicon and a description; noindex only on drafts", [], None, None, key="launch")
    route = urlparse(p.get("url") or "").path or "/"
    # the share text against the page: judged only on a page set up for sharing, where a stale title or card is seen
    if sh.get("h1") and (sh.get("image") or any(sh.get(k) for k in ("ogTitle", "ogDescription", "twitterTitle", "twitterDescription"))):
        page = content_words(sh["h1"] + " " + (sh.get("lead") or ""))
        host = (urlparse(p.get("url") or "").hostname or "").split(".")
        brand = content_words(" ".join([sh.get("siteName") or "", sh.get("logoName") or ""] + [x.replace("-", " ") for x in host[:-1] if x != "www"]))
        rows, done = [], set()
        for label, key, split, floor in (("<title>", "title", True, SHARE_TITLE_MIN), ("og:title", "ogTitle", True, SHARE_TITLE_MIN),
                                         ("twitter:title", "twitterTitle", True, SHARE_TITLE_MIN), ("meta description", "metaDescription", False, SHARE_TEXT_MIN),
                                         ("og:description", "ogDescription", False, SHARE_TEXT_MIN), ("twitter:description", "twitterDescription", False, SHARE_TEXT_MIN)):
            text = sh.get(key)
            r = said_on_page(text, page, brand, split) if text and text not in done else None
            if r and r[0] / r[1] < floor:
                done.add(text)
                rows.append(f'{label} "{text[:80]}": {r[0]} of its {r[1]} words are in the h1 or the line under it')
        if rows:
            F.add("EN-09", "warn", "Share text says something the page does not", w, "; ".join(rows[:4]) + f'. The h1 says "{sh["h1"][:80]}"',
                  "the title, description and share text say what the h1 and the line under it say, or differ on purpose", [],
                  "rewrite them from the h1 and its lead, or record why they differ; if the share image shows the old words too, rebuild it", None, key="share-text:" + route)
    pk = p.get("picker") or {}
    if public_host(p.get("url")) and (pk.get("scripts") or pk.get("markup") or pk.get("switchers")):
        bits = ["loads " + ", ".join(os.path.basename(urlparse(s).path) for s in pk["scripts"])] if pk.get("scripts") else []
        if pk.get("markup"):
            bits.append(f"{pk['markup']} house picker element(s) (.proto-picker, data-od-stage, data-od-variant)")
        bits += [f"{s['sel']} holds {s['buttons']} switch buttons" for s in pk.get("switchers") or []]
        F.add("EN-07", "warn", "A variant picker on a public address", w, "; ".join(bits),
              "options are shown on a review copy (a local file, a review route or a preview address), never to visitors", [s["sel"] for s in pk.get("switchers") or []][:3],
              "ship the chosen variant without the picker and its other variants; keep the picker on the review copy. If this address is the review copy, say so in the report",
              "STD-process-review-taste-41", key="picker")


def save_share(docs, rd):
    """review/share.json: per route, the share image and what it should show (headline, hero picture, logo), as the browser
    saw them. engine.py review dates these files against git; this script reads no files outside the review folder."""
    pages = {}
    for p in docs:
        sh = p.get("share") or {}
        route = urlparse(p.get("url") or "").path or "/"
        if p.get("v") == 1 and sh.get("imageUrl") and route not in pages:
            pages[route] = {"url": p.get("url"), "image": sh["imageUrl"], "h1": sh.get("h1"), "hero": sh.get("hero"), "logo": sh.get("logo")}
    if pages:
        write_json(rd / "share.json", {"made": dt.datetime.now().isoformat(timespec="seconds"), "pages": pages})


def check_focus(f, F):
    stops = f.get("stops") or []
    w = where_of(f)
    if not stops:
        return
    real = [s for s in stops if s.get("active")]
    if not real and f.get("tabbable") == 0:  # nothing on the page takes focus, so there is nothing to reach (older probe output has no count)
        F.add("IN-01", "info", "The page has no controls to Tab to", w, f"{len(stops)} Tab presses, 0 focusable elements", "nothing to check for keyboard access", [], None, None, key="tab-none")
        return
    if not real:
        F.add("IN-01", "error", "Tab never reached any control", w, f"{len(stops)} Tab presses, focus stayed on the page", "a keyboard user can reach every control", [], "check tabindex, display: none, and pointer-only handlers", "WCAG 2.1.1", key="tab-none")
        return
    no_ring, thin, covered, partly, offscreen, unnamed = [], [], [], [], [], []
    for s in real:
        ring = s.get("ring") or {}
        if s.get("focusVisible") and not ring.get("visible"):
            no_ring.append(s)
        elif s.get("focusVisible") and ring.get("outlineStyle") != "none" and (ring.get("outlineWidth") or 0) < 2 and ring.get("boxShadow") == "none":
            thin.append(s)
        ob = s.get("obscured")
        if ob and ob["fraction"] >= 0.99:
            covered.append(s)
        elif ob and ob["fraction"] >= 0.5:
            partly.append(s)
        if not s.get("inViewport"):
            offscreen.append(s)
        if not s.get("name"):
            unnamed.append(s)
    names = lambda L: "; ".join(f"{s['sel']} (Tab {s['index'] + 1})" for s in L[:4])
    if no_ring:
        F.add("IN-02", "error", "Focused controls show no focus indicator", w, f"{len(no_ring)} of {len(real)} stops: {names(no_ring)}",
              "a visible indicator (2 px ring, 2 px offset, not color alone)", [s["sel"] for s in no_ring[:4]], "add a :focus-visible outline", "WCAG 2.4.7", key="no-ring", basis="operated")
    if thin:
        F.add("IN-02", "warn", "Focus ring thinner than 2 px", w, f"{len(thin)} stops: {names(thin)}", "2 px ring at a 2 px offset", [s["sel"] for s in thin[:4]], None, "guardrails 4", key="thin-ring", basis="operated")
    if covered:
        F.add("IN-01", "error", "Focused controls are completely covered by something else", w, "; ".join(f"{s['sel']} under {s['obscured']['by']}" for s in covered[:3]),
              "focus never hidden by a sticky header, footer, banner or overlay (WCAG 2.4.11)", [s["sel"] for s in covered[:3]] + [covered[0]["obscured"]["by"]],
              "add scroll-padding-top/bottom equal to the bar, or lower the bar's z-index below the focus", "WCAG 2.4.11", key="obscured", basis="operated")
    if partly:
        F.add("IN-01", "warn", "Focused controls are partly covered", w, "; ".join(f"{s['sel']} {round(s['obscured']['fraction'] * 100)}% under {s['obscured']['by']}" for s in partly[:3]),
              "fully visible when focused (AAA 2.4.12; AA 2.4.11 only fails when it is entirely hidden)", [s["sel"] for s in partly[:3]], "add scroll-padding", "WCAG 2.4.12 (AAA)", key="part-obscured", basis="operated")
    if offscreen:
        F.add("IN-01", "warn", "Focus moved to something that is not on screen", w, names(offscreen), "the page scrolls to the focused control", [s["sel"] for s in offscreen[:3]],
              "check scroll-padding and that the element is not off-canvas", "WCAG 2.4.7", key="offscreen", basis="operated")
    if unnamed:
        F.add("IN-03", "error", "Focused controls have no name", w, names(unnamed), "every control is announced with a name", [s["sel"] for s in unnamed[:4]], "add aria-label or text", "WCAG 4.1.2", key="focus-noname", basis="operated")
    run, last = 0, None
    for s in stops:
        # one control is the same selector in the same place: a list of look-alike rows (a changelog's days) shares a selector
        rc = s.get("page") or s.get("rect") or {}   # page position: Tab scrolls each stop into the same place on screen
        key = (s.get("sel"), rc.get("x"), rc.get("y")) if s.get("active") else None
        run = run + 1 if key and key == last else 1
        last = key
        if run >= 3 and last:
            F.add("IN-01", "warn", "Focus stays on one control across Tab presses (a keyboard trap, or the end of the page)", w, f"{last[0]}, {run} presses in a row", "Tab moves on; Esc leaves a dialog", [last[0]],
                  "if this is a dialog, make sure Esc closes it and focus returns to the trigger", "WCAG 2.1.2", key="trap:" + last[0], basis="operated")
            break
    jumps = 0
    for a, b in zip(real, real[1:]):
        if b["rect"]["y"] < a["rect"]["y"] - 300 and b["index"] != 0:
            jumps += 1
    if jumps >= 2:
        F.add("IN-01", "info", "Tab order jumps back up the page", w, f"{jumps} jumps of more than 300 px against reading order", "focus order follows the visual order (WCAG 2.4.3); a multi-column layout can jump legitimately: look at the order yourself", [], "if it is wrong, reorder the DOM instead of using tabindex or CSS order", "WCAG 2.4.3", key="tab-order", basis="operated")



def check_console(c, F):
    w = where_of(c)
    msgs = [m for m in (c.get("messages") or []) if "favicon" not in m["text"]]    # a missing favicon is the dev server's, not the app's
    failed = [m for m in msgs if m["type"] in ("requestfailed", "http")]
    # the browser also logs "Failed to load resource" as a console error for every failed request: that is the finding below, not a second one
    errs = [m for m in msgs if m["type"] in ("error", "pageerror") and not m["text"].startswith("Failed to load resource")]
    warns = [m for m in msgs if m["type"] == "warning"]
    if errs:
        F.add("EN-06", "error", "Errors in the console", w, f"{len(errs)}: " + " | ".join(m["text"][:110] for m in errs[:3]), "no console errors while the page loads and scrolls", [],
              "open the first error: a thrown error often leaves part of the page unrendered", None, key="console-errors")
    if failed:
        F.add("EN-06", "error", "Requests failed or returned an error status", w, f"{len(failed)}: " + " | ".join(m["text"][:110] for m in failed[:3]), "every request the page makes succeeds", [],
              "a 404 on a font or image explains a fallback font or a broken picture", None, key="failed-requests")
    if warns:
        F.add("EN-06", "info", "Warnings in the console", w, f"{len(warns)}: " + " | ".join(m["text"][:110] for m in warns[:2]), "none, or understood", [], None, None, key="console-warnings")


def check_hover(h, F):
    w = where_of(h)
    rows = h.get("samples") or []
    flat = [r for r in rows if not [k for k in r["changed"] if not k.startswith("transition")] and not r["moved"]]
    if rows and len(flat) >= max(2, len(rows) // 2):
        F.add("ST-01", "info", "Hovering most sampled controls changes nothing you can see", w, f"{len(flat)} of {len(rows)}: " + "; ".join(r["sel"] for r in flat[:3]),
              "a hover cue on pointer devices", [r["sel"] for r in flat[:3]], "confirm with a screenshot while hovering; touch-only products can skip this", None, key="hover-flat", basis="operated")
    nopointer = [r for r in rows if r["sel"].split(" ")[-1].split(".")[0].split(":")[0] in ("a", "button", "summary") and r.get("cursor") not in ("pointer", "text", "default")]
    if nopointer:
        F.add("IN-05", "info", "Clickable controls without a pointer cursor", w, "; ".join(f"{r['sel']} ({r.get('cursor')})" for r in nopointer[:3]), "cursor: pointer on links and buttons, by house habit", [r["sel"] for r in nopointer[:3]], None, None, key="cursor", basis="operated")


def check_states(d, F):
    """capture.py toggles / __od.states(): every option of each tab list, segmented control, radio group and switch."""
    w = where_of(d)
    for g in d.get("groups") or []:
        base, picks = g.get("base") or {}, g.get("picks") or []
        if not picks:
            continue
        names = ", ".join(o["label"] or o["sel"] for o in g["opts"][:4])
        for i, box in enumerate(g.get("boxes") or []):
            hs = [x for x in [(base.get("heights") or [None] * 9)[i]] + [(pk.get("heights") or [None] * 9)[i] for pk in picks] if x is not None]
            if hs and max(hs) - min(hs) > 1:
                F.add("ST-10", "warn", "A box changes height when a toggle changes", w, f"{box} is {' / '.join(fmt(h) for h in sorted(set(hs)))} px across {g['kind']} ({names})",
                      "one footprint for every state: the box is as tall as its tallest state, so nothing below it jumps (owner review 2026-11-03 row 22)", [box, g["opts"][0]["sel"]],
                      "put every state in the same grid cell (grid-area: 1 / 1, visibility instead of display), or give the box the tallest state's height", None, key="height:" + box, basis="operated")
                break
        if all(pk.get("sig") == base.get("sig") for pk in picks) and g.get("pixels") != "changed":
            F.add("ST-11", "warn", "A control that changes nothing", w, f"{g['kind']} ({names}): no option changed anything in {g.get('region')}" + (" (checked by pixels)" if g.get("pixels") == "same" else " (layout, colour and text compared)"),
                  "every option visibly changes what it says it changes", [o["sel"] for o in g["opts"][:3]], "wire the control up, or remove it", None, key="dead:" + g["opts"][0]["sel"], basis="operated")


def check_bars(d, F):
    w = where_of(d)
    hits = d.get("hits") or []
    if hits:
        F.add("CV-08", "error", "A floating bar covers text that cannot scroll out from under it", w,
              "; ".join(f"\"{h['text']}\" ({h['sel']}) under {h['bar']}, {h['why']}" for h in hits[:4]),
              "nothing readable stays under a fixed or floating bar: pinned text clears it, and the page ends with room below the last line", [h["sel"] for h in hits[:4]] + [hits[0]["bar"]],
              "pad the pinned block or the page end by the bar's height (scroll-padding, padding-bottom), or hide the bar where it would cover", None, key="bar-covers", basis="operated")


def check_kern(d, F):
    w = where_of(d)
    lost = [s for s in d.get("split") or [] if max(s.get("maxDx") or 0, s.get("maxDy") or 0) > 0.5]
    if lost:
        F.add("MS-17", "warn", "Letter-by-letter text loses its kerning", w, "; ".join(f"\"{s['text']}\" letters sit up to {fmt(max(s['maxDx'], s['maxDy']))} px from where the font puts them (worst at \"{s['pair']}\")" for s in lost[:3]),
              "letters where the font puts them, within 0.5 px: one span per letter (inline-block above all) breaks kerning pairs such as AV and To",
              [s["sel"] for s in lost[:4]], "split by word, or animate a clip or mask over whole lines; if letters must move, keep them inline and font-kerning: normal", None, key="kern-split")
    jump = [s for s in d.get("swapped") or [] if max(s.get("maxDx") or 0, s.get("maxDy") or 0) > 0.5]
    if jump:
        F.add("MS-17", "warn", "Letters jump when a letter-by-letter reveal ends", w, "; ".join(f"\"{s['text']}\" jumps up to {fmt(max(s['maxDx'], s['maxDy']))} px (at \"{s['pair']}\")" for s in jump[:3]),
              "the last frame of a reveal matches the plain text within 0.5 px", [s["sel"] for s in jump[:4]], "measure the split letters against the plain text and keep the kerning, or leave the spans in place", None, key="kern-jump")


ART = ("svg", "canvas")


def check_pixels(d, F):
    """capture.py text_pixels: the text hidden and the pixels behind each line read."""
    w = where_of(d)
    crossed, low = {}, {}
    for l in d.get("lines") or []:
        photo = any(u["tag"] in ("img", "video") and u.get("covers") for u in l.get("under") or [])
        if l.get("edges", 0) >= 6 and l.get("share", 0) >= 0.002 and l.get("backdrop") in ("solid", "assumed-white", "assumed-dark") and not photo:
            crossed.setdefault(l["sel"], l)
        need = CONTRAST_LARGE if l.get("large") else CONTRAST_TEXT
        if l.get("ratio") is not None:
            if l["ratio"] >= need:
                F.pixel_pass.setdefault(w, set()).add(l["sel"])
            elif (l.get("backdrop") != "solid" or l.get("under")) and l["sel"] not in crossed:   # a line art crosses is one finding (MS-20), not two
                low.setdefault(l["sel"], l)
    if crossed:
        F.add("MS-20", "warn", "Art or an image is drawn through text", w,
              "; ".join(f"\"{l['text']}\": {round(l['share'] * 100, 1)}% of its line box is crossed" + (f" ({', '.join(sorted({u['tag'] for u in l['under']}))} under it)" if l.get("under") else "") for l in list(crossed.values())[:4]),
              "no line art, chart or picture runs through a line of text: hidden text, then a screenshot, shows nothing sharp inside any line box (owner review 2026-11-05 row 6)",
              list(crossed)[:4], "move the art into its own box clear of the text, or give the text a solid backing", None, key="art-over-text")
    for sel_, l in list(low.items())[:6]:
        F.add("MS-04", "error", f"Text contrast {fmt(l['ratio'])}:1 on the pixels behind it", w, f"\"{l['text']}\" in {l['sel']} on a {l.get('backdrop')} backdrop: the 5% of pixels closest to the text colour give {fmt(l['ratio'])}:1",
              f"{CONTRAST_LARGE if l.get('large') else CONTRAST_TEXT}:1 against the real backdrop (preflight 11)", [sel_], "darken the scrim or the photo behind it, or move the text onto a solid backing", "WCAG 1.4.3", key="px-contrast:" + sel_)


GENERIC_FAMILY = re.compile(r"^(system-ui|ui-[a-z-]+|-apple-system|blinkmacsystemfont|serif|sans-serif|monospace|cursive|fantasy|emoji|math)$", re.I)


def check_fonts(f, F):
    w = where_of(f)
    for row in f.get("rows") or []:
        asked = (row.get("asked") or "").strip()
        if not asked or GENERIC_FAMILY.match(asked):
            continue
        drawn = [d["family"] for d in row.get("drawn") or []]
        if not drawn:
            continue
        a = asked.lower().replace(" ", "")
        if any(a in d.lower().replace(" ", "") or d.lower().replace(" ", "") in a for d in drawn):
            continue
        F.add("MS-03", "error", f"{asked} was asked for but the browser drew {', '.join(drawn)}", w, f"{row['sel']}: {', '.join(drawn)} ({sum(d['glyphs'] for d in row['drawn'])} glyphs)",
              f"{asked} (the first family in the stack)", [row["sel"]], "the font file did not load or does not cover these characters: check @font-face, the file path, the format and unicode-range",
              None, key="font:" + asked.lower())


def check_vitals(v, F):
    w = where_of(v)
    if v.get("cls", 0) > 0.1:
        F.add("TM-06", "warn", f"Layout shifts while loading (CLS {v['cls']})", w, "; ".join(f"{s['value']} at {s['at']} ms in {', '.join(n for n in s['nodes'] if n)}" for s in v.get("shifts", [])[:3]),
              "0.1 or less", [n for s in v.get("shifts", [])[:2] for n in s["nodes"] if n], "reserve space for images, fonts and late content (width/height, aspect-ratio, font-display with a matched fallback)", "Core Web Vitals", key="cls")
    if len(v.get("longFrames", [])) >= 3:
        F.add("TM-09", "info", "Long animation frames", w, f"{len(v['longFrames'])} frames over 50 ms, worst {max(f['ms'] for f in v['longFrames'])} ms", "frames under 50 ms during load and animation", [], None, None, key="long-frames")


# ------------------------------------------------------------------------------------------------ commands
def cmd_probe(args):
    if args.print:
        sys.stdout.write(PROBE.read_text(encoding="utf-8"))
        return
    print(PROBE)
    print(f"{PROBE.stat().st_size} bytes. Evaluate the whole file in the page; the last expression is the result (JSON).")
    print("After it runs, window.__od has focus(), style(), motion(), seek(), stress(), setMode(), scrollTo() and walk().")



def check_datastates(d, F):
    """The page on a slow network and with its data empty, failing and offline (capture.py network_states): ST-16, ST-17."""
    w = where_of(d)
    sl = d.get("slow") or {}
    a1 = sl.get("at1s") or {}
    if a1 and not a1.get("chars") and not a1.get("busy") and not a1.get("loadingWords"):
        F.add("ST-16", "warn", "A blank screen while the page loads on a slow network", w, f"1 s into a throttled load (400 ms latency, 50 KB/s): no text and no loading sign; full load took {fmt(sl.get('loadMs'))} ms",
              "something on screen at once: the layout with a skeleton, or a loading sign", [], "render the page frame first, then a skeleton the size of the content that is coming", None, key="blank-load", basis="operated")
    if (sl.get("cls") or 0) > 0.1:
        F.add("ST-17", "warn", f"The layout moves as content arrives (CLS {sl['cls']})", w,
              "; ".join(f"{s['value']} at {s['at']} ms in {', '.join(n for n in s.get('nodes', []) if n) or 'the page'}" for s in sl.get("shifts", [])[:3]) or f"CLS {sl['cls']}",
              "CLS 0.1 or less on a slow load: a skeleton or reserved box the size of what replaces it", [n for s in sl.get("shifts", [])[:3] for n in s.get("nodes", []) if n],
              "give images width and height (or aspect-ratio), and make each skeleton the size and shape of the content it stands for", "Core Web Vitals (CLS)", key="arrival-shift", basis="operated")
    if not d.get("requests"):
        F.add("ST-16", "info", "No data requests: empty, error and offline states not tried", w, "the page made no fetch or XHR request while loading",
              "for a page with data, each state shows a message people can act on", [], "if data arrives another way (server-rendered, a socket), set each state by hand and look", None, key="no-data", basis="operated")
        return
    names = {"empty": ("empty", "an empty state that says there is nothing yet and what to do"), "error": ("failing with a server error", "an error that says what failed and offers a retry"),
             "offline": ("unreachable (offline)", "a message that the connection is down, with a retry")}
    for mode, m in (d.get("modes") or {}).items():
        said, want = names.get(mode, (mode, "a message"))
        if m.get("placeholders"):
            F.add("ST-16", "error", f"Broken text when the data is {said}", w, "; ".join(f"{x['sel']}: {x['match']!r}" for x in m["placeholders"][:3]),
                  "no undefined, NaN or empty template text in any state", [x["sel"] for x in m["placeholders"][:3]] + [m.get("shot")],
                  "handle the missing value before rendering it", None, key="state-broken-" + mode, basis="operated")
        if m.get("busyStill") and mode != "empty":
            F.add("ST-16", "warn", f"Still loading forever when the data is {said}", w, "a loading sign is still on screen after the request ended", "the loading sign gives way to a message",
                  [m.get("shot")], "end the loading state on failure as well as on success", None, key="state-stuck-" + mode, basis="operated")
        elif not m.get("message"):
            F.add("ST-16", "warn", f"No message when the data is {said}", w, f"{fmt(m.get('chars'))} characters on screen and none of the usual words for this state",
                  want, [m.get("shot")], "write the state into the view: say what happened and offer the next step", None, key="state-silent-" + mode, basis="operated", decided="judgment")


def check_notfound(d, F):
    """What an address that cannot exist shows (capture.py not_found): ST-18."""
    w = where_of(d)
    st, h = d.get("status"), (d.get("heading") or "").strip()
    if st != 404:
        F.add("ST-18", "warn", f"A missing page answers {st}, not 404", w, f"{d.get('url')} returned {st}", "status 404, so search engines drop it and tools can tell",
              [d.get("shot")], "serve the not-found page with status 404", None, key="nf-status", basis="operated")
    if not h:
        F.add("ST-18", "warn", "The not-found page has no heading", w, f"{fmt(d.get('chars'))} characters, no h1", "a heading that says the page is not here, in plain words",
              [d.get("shot")], "an h1 such as \"We can't find that page\"", None, key="nf-heading", basis="operated")
    elif re.fullmatch(r"(error\s*)?(404|not found|error response|page not found)[.!]?", h, re.I) or re.fullmatch(r"[\d\W]+", h):
        F.add("ST-18", "warn", "The not-found page says a code, not what happened", w, f"heading: \"{h}\"", "plain words: what happened and what to do", [d.get("shot")],
              "say it as a person would (\"We can't find that page\") and keep 404 as small print", None, key="nf-plain", basis="operated")
    if not d.get("links"):
        F.add("ST-18", "warn", "The not-found page offers no way on", w, "0 links on the page", "a link home, to search or to the main sections", [d.get("shot")],
              "add the site header, or at least a link home", None, key="nf-links", basis="operated")


CAPTURE_CHECKS = {"focus": check_focus, "console": check_console, "hover": check_hover, "vitals": check_vitals, "fonts": check_fonts,
                  "states": check_states, "bars": check_bars, "kern": check_kern, "pixels": check_pixels, "datastates": check_datastates, "notfound": check_notfound}
SAVE_KINDS = set(CAPTURE_CHECKS)
CHECK_FOLDERS = ("probes", "focus", "hover", "console", "fonts", "vitals", "motion", "states", "bars", "kern", "pixels", "datastates", "notfound")   # where serve and capture.py write
MAX_POST = 4 * 1024 * 1024


def loader_js(base, name="NAME"):
    """The one call a browser tool makes per page: load probe.js from the helper, run it, save the result to disk."""
    return ("(async()=>{const B='" + base + "';if(!window.__od)await new Promise((ok,no)=>{const s=document.createElement('script');s.src=B+'probe.js';"
            "s.onload=ok;s.onerror=()=>no('blocked: the page refuses scripts from 127.0.0.1; paste probe.js instead');document.documentElement.appendChild(s)});"
            "window.__odSave=(n,d)=>fetch(B+'save?name='+encodeURIComponent(n),{method:'POST',body:JSON.stringify(d)}).then(r=>r.text());"
            "return await __odSave('" + name + "',__od.probe())})()")


def make_handler(rd, token):
    from http.server import BaseHTTPRequestHandler
    prefix = f"/t/{token}/"

    class H(BaseHTTPRequestHandler):
        server_version = "od-review"

        def log_message(self, fmt, *a):
            sys.stderr.write("serve: " + (fmt % a) + "\n")

        def _cors(self):
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "content-type")
            self.send_header("Access-Control-Allow-Private-Network", "true")

        def _send(self, code, body=b"", ctype="text/plain; charset=utf-8"):
            self.send_response(code)
            self._cors()
            self.send_header("Content-Type", ctype)
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_OPTIONS(self):
            self._send(204)

        def do_GET(self):
            if self.path.split("?")[0] == prefix + "probe.js":
                return self._send(200, PROBE.read_bytes(), "application/javascript; charset=utf-8")
            self._send(404, b"not found")

        def do_POST(self):
            path, _, query = self.path.partition("?")
            if path != prefix + "save":
                return self._send(404, b"not found")
            n = int(self.headers.get("Content-Length") or 0)
            if n <= 0 or n > MAX_POST:
                return self._send(413, b"empty or over 4 MB")
            try:
                doc = json.loads(self.rfile.read(n))
            except ValueError:
                return self._send(400, b"not JSON")
            name = re.sub(r"[^a-z0-9._-]+", "-", (dict(x.split("=", 1) for x in query.split("&") if "=" in x).get("name") or "probe").lower()).strip("-.")[:80] or "probe"
            kind = doc.get("kind") if isinstance(doc, dict) else None
            if isinstance(doc, dict) and doc.get("v") == 1:
                folder = "probes"
            elif kind in SAVE_KINDS:
                folder = kind
            else:
                return self._send(400, ("not a probe result (v: 1) or a capture document (kind: " + ", ".join(sorted(SAVE_KINDS)) + ")").encode())
            out = rd / folder / f"{name}.json"
            write_json(out, doc)
            self._send(200, f"saved {out} ({n // 1024 + 1} KB)".encode())

    return H


def cmd_serve(args):
    """Loopback only, one random path, three verbs. The page is the client: it asks for probe.js and posts JSON back."""
    from http.server import ThreadingHTTPServer
    rd = review_dir(args)
    token = secrets.token_hex(8)
    srv = ThreadingHTTPServer(("127.0.0.1", args.port), make_handler(rd, token))
    base = f"http://127.0.0.1:{srv.server_address[1]}/t/{token}/"
    print(f"serving probe.js and saving to {rd} on 127.0.0.1 only, for {args.minutes} minutes (Ctrl-C stops it).", flush=True)
    print("In each page, evaluate this one line with your browser tool (change NAME to route-width-theme, for example home-390-light):\n", flush=True)
    print(loader_js(base), flush=True)
    print("\nAfterwards __odSave(name, __od.focusDoc()) saves a Tab walk. If the page's security policy blocks the script, paste probe.js instead (review.py probe --print).", flush=True)
    srv.timeout = 1
    import time
    end = time.time() + args.minutes * 60
    try:
        while time.time() < end:
            srv.handle_request()
    except KeyboardInterrupt:
        pass
    finally:
        srv.server_close()



def cmd_plan(args):
    rd = review_dir(args)
    sysm = load_system(args.project) if args.project else load_system(".")
    routes = [r.strip() for r in (args.routes or "/").split(",") if r.strip()]
    if args.viewports:
        vps = []
        for v in args.viewports.split(","):
            v = v.strip()
            w, _, h = v.partition("x")
            vps.append((int(w), int(h) if h else (844 if int(w) < 700 else 900)))
    else:
        vps = list(DEFAULT_VIEWPORTS)
        if sysm and sysm.get("breakpoints"):
            for name, bp in sorted(sysm["breakpoints"].items(), key=lambda kv: kv[1]):
                if bp >= 1280 and not any(abs(bp - w) < 100 for w, _ in vps) and bp < 1700:
                    vps.append((bp, 900))
        if args.wide:
            vps.append(WIDE_VIEWPORT)
    if args.edges and sysm and sysm.get("breakpoints"):
        for bp in sysm["breakpoints"].values():
            for w in (bp - 1, bp):
                if 300 < w < 2000 and all(w != x for x, _ in vps):
                    vps.append((w, 900))
    vps = sorted(set(vps))
    themes = [t.strip() for t in (args.themes or ",".join((sysm or {}).get("modes") or ["light", "dark"])).split(",") if t.strip()]
    cells = [f"{r}|{w}x{h}|{t}" for r in routes for (w, h) in vps for t in themes]
    tasks = ["scroll-walk", "focus-walk", "hover-and-press", "states-and-data", "motion", "stress-text", "reduced-motion", "forced-colors", "console-and-network",
             "letter-reveals", "text-pixels", "floating-bars", "toggles"]
    task_cells = [f"task:{r}|{t}" for r in routes for t in tasks]
    plan = {"url": args.url, "routes": routes, "viewports": [f"{w}x{h}" for w, h in vps], "themes": themes, "tasks": tasks,
            "system": (sysm or {}).get("name"), "made": dt.date.today().isoformat(), "cells": cells, "task_cells": task_cells,
            "notes": ["cells: run probe.js, then screenshot the top and every scroll step; tasks: things a static capture cannot show",
                      "skip a cell only with a reason (mark ... skipped --why); the report lists every skip"]}
    write_json(rd / "plan.json", plan)
    old = read_json(rd / "ledger.json", {"cells": {}})
    ledger = {"cells": {c: old["cells"].get(c, {"status": "todo", "evidence": [], "why": ""}) for c in cells + task_cells}}
    write_json(rd / "ledger.json", ledger)
    print(f"plan: {len(routes)} route(s) x {len(vps)} viewport(s) x {len(themes)} theme(s) = {len(cells)} cells, plus {len(task_cells)} task cells")
    print("viewports: " + ", ".join(plan["viewports"]) + "   themes: " + ", ".join(themes))
    print(f"written: {rd / 'plan.json'} and {rd / 'ledger.json'}")
    print("next: for each cell load the page at that size and theme, wait for fonts, run probe.js, screenshot top and each scroll step, then: review.py mark '<cell>' done --evidence <files>")


def cmd_mark(args):
    rd = review_dir(args)
    led = read_json(rd / "ledger.json")
    cell = args.cell
    if cell not in led["cells"]:
        matches = [c for c in led["cells"] if cell in c]
        if len(matches) != 1:
            die(f"'{cell}' is not one cell of the plan" + (f"; it matches {len(matches)}: {matches[:5]}" if matches else "") + f". Cells look like {next(iter(led['cells']))!r}")
        cell = matches[0]
    if args.status in ("skipped", "blocked") and not args.why:
        die(f"say why: mark ... {args.status} --why \"...\" (the report shows it)")
    e = led["cells"][cell]
    e["status"] = args.status
    e["evidence"] = sorted(set(e.get("evidence", []) + (args.evidence or [])))
    if args.why:
        e["why"] = args.why
    e["at"] = dt.datetime.now().isoformat(timespec="seconds")
    write_json(rd / "ledger.json", led)
    todo = sum(1 for v in led["cells"].values() if v["status"] == "todo")
    print(f"{cell}: {args.status}. {todo} of {len(led['cells'])} cells still todo")


def check_inputs(paths):
    """A folder stands for every probe and capture file in it: the review folder (its probes/, focus/, hover/, console/,
    fonts/, vitals/ and motion/) or one of those subfolders. Missing subfolders are skipped, so one command fits every route."""
    out = []
    for path in map(Path, paths):
        if not path.is_dir():
            out.append(str(path))
            continue
        dirs = [path] if path.name in CHECK_FOLDERS else [path / sub for sub in CHECK_FOLDERS]
        out += sorted(str(x) for d in dirs for x in d.rglob("*.json"))
    return out


def cmd_check(args):
    rd = review_dir(args)
    sysm = load_system(args.project or ".")
    F = Findings()
    F.audience = getattr(args, "audience", None)
    n = 0
    files = check_inputs(args.probes)
    if not files:
        die(f"no probe or capture files in {', '.join(args.probes)}")
    args.probes = files
    docs = []
    for path in args.probes:
        d = read_json(path)
        for p in d if isinstance(d, list) else [d]:
            if p.get("kind") not in CAPTURE_CHECKS and p.get("v") != 1:
                die(f"{path} is not a probe result (no v: 1) or a capture file (kind: {', '.join(CAPTURE_CHECKS)})")
            docs.append(p)
    for p in sorted(docs, key=lambda x: x.get("kind") != "pixels"):   # pixels first: they overrule a guessed backdrop
        if p.get("kind") in CAPTURE_CHECKS:
            CAPTURE_CHECKS[p["kind"]](p, F)
        else:
            check_probe(p, sysm, F)
        n += 1
    save_share(docs, rd)
    findings = F.done()
    last = read_json(rd / "findings.measured.json", {"findings": []})
    prev, prev_inputs = last["findings"], last.get("inputs")
    inputs = sorted(os.path.basename(x) for x in args.probes)
    if prev:
        write_json(rd / "findings.measured.prev.json", last)
    write_json(rd / "findings.measured.json", {"made": dt.datetime.now().isoformat(timespec="seconds"), "system": (sysm or {}).get("name"), "probes": n, "inputs": inputs, "findings": findings})
    if args.json:
        print(json.dumps(findings, indent=2, ensure_ascii=False))
        return
    counts = {s: sum(1 for f in findings if f["severity"] == s) for s in SEV}
    print(f"checked {n} probe run(s) against " + (f"the floors, practice and the {sysm['name']} system" if sysm
                                                 else "the floors and practice (no OpenDesigner system found: type and spacing are judged on a 4 px grid, buttons, typefaces, weights and colors by count)")
          + f": {counts['error']} error, {counts['warn']} warn, {counts['info']} info")
    for f in findings:
        if f["severity"] == "info" and not args.all:
            continue
        print(f"\n[{f['severity'].upper()}] {f['title']}  ({f['case']}, {f['basis']}" + (", a judgment: read the evidence" if f.get("decided") == "judgment" else "") + ")")
        print(f"  where:    {'; '.join(f['where'][:3])}" + (f" (+{len(f['where']) - 3} more)" if len(f["where"]) > 3 else ""))
        if f["measured"]:
            print(f"  measured: {f['measured']}")
        if f["expected"]:
            print(f"  expected: {f['expected']}")
        if f["evidence"]:
            print(f"  element:  {f['evidence'][0]}")
        if f["fix"]:
            print(f"  fix:      {f['fix']}")
    if counts["info"] and not args.all:
        print(f"\n({counts['info']} info notes hidden; --all shows them)")
    if prev and prev_inputs != inputs:
        print("\n(the last check used a different set of files, so nothing is compared. Re-run `check` on the same probe files after a fix to see what was resolved.)")
    elif prev:
        before = {(x["case"], x["title"]) for x in prev}
        now = {(x["case"], x["title"]) for x in findings}
        print(f"\nsince the last check: {len(before - now)} resolved, {len(now - before)} new, {len(before & now)} still open")
        for c, t in sorted(before - now):
            print(f"  resolved: {t}")
        for c, t in sorted(now - before):
            print(f"  new:      {t}")


def cmd_finding(args):
    rd = review_dir(args)
    path = rd / "findings.human.json"
    data = read_json(path, {"findings": []})
    if args.basis == "measured":
        die("measured findings come from `check`. Use --basis seen, operated or inferred")
    if not args.evidence and args.basis != "inferred":
        die("a finding needs evidence: a screenshot path, or the selector you operated (--evidence). Without one, use --basis inferred")
    f = {"id": f"H-{len(data['findings']) + 1:03d}", "case": args.case or "MS-12", "severity": args.severity, "basis": args.basis, "title": args.text, "where": [args.where] if args.where else [],
         "measured": None, "expected": args.expected, "evidence": args.evidence or [], "fix": args.fix, "standard": None,
         "status": "unverified" if args.basis == "inferred" else "confirmed", "at": dt.datetime.now().isoformat(timespec="seconds")}
    data["findings"].append(f)
    write_json(path, data)
    print(f"{f['id']} recorded ({args.severity}, {args.basis})")


def cmd_report(args):
    rd = review_dir(args)
    meas = read_json(rd / "findings.measured.json", {"findings": []})
    hum = read_json(rd / "findings.human.json", {"findings": []})
    led = read_json(rd / "ledger.json", {"cells": {}})
    plan = read_json(rd / "plan.json", {})
    findings = sorted(meas["findings"] + hum["findings"], key=lambda f: (SEV[f["severity"]], f["case"]))
    counts = {s: sum(1 for f in findings if f["severity"] == s) for s in SEV}
    cells = led["cells"]
    by = {k: [c for c, v in cells.items() if v["status"] == k] for k in ("done", "todo", "skipped", "blocked")}
    total = len(cells)
    if counts["error"]:
        verdict = "FAIL"
        line = f"{counts['error']} error(s) found in what was checked."
    elif by["todo"] or by["blocked"] or not total:
        verdict = "INCOMPLETE"
        line = ("No plan or ledger was made, so nothing says what was covered." if not total else f"{len(by['todo'])} of {total} planned cells were not checked and {len(by['blocked'])} were blocked.") + " No errors found so far."
    else:
        verdict = "NO ERRORS FOUND"
        line = f"in the {len(by['done'])} cells that were checked ({len(by['skipped'])} skipped with a reason). That is not the same as correct: see what was not checked."
    cases = {c["id"]: c for c in load_cases().get("cases", [])}
    name = args.name or plan.get("system") or meas.get("system") or "this UI"
    L = [f"# Review report: {name}", "",
         f"Made {dt.date.today().isoformat()} · {plan.get('url') or 'no URL recorded'} · {meas.get('probes', 0)} probe run(s) · system: {plan.get('system') or meas.get('system') or 'none found'}", "",
         f"## Verdict: {verdict}", "", line, "",
         f"{counts['error']} errors · {counts['warn']} warnings · {counts['info']} notes · coverage {len(by['done'])}/{total} cells done", ""]
    unv = [f for f in findings if f["status"] == "unverified"]
    if unv:
        L += [f"{len(unv)} finding(s) below are **unverified** (reasoned, not observed).", ""]
    L += ["## What was not checked", ""]
    if by["todo"] or by["skipped"] or by["blocked"]:
        for k, title in (("todo", "Not done"), ("blocked", "Blocked"), ("skipped", "Skipped on purpose")):
            if by[k]:
                L.append(f"**{title}** ({len(by[k])})")
                for c in by[k][:60]:
                    why = cells[c].get("why")
                    L.append(f"- `{c}`" + (f": {why}" if why else ""))
                L.append("")
    else:
        L += ["Every planned cell was checked. Still not covered by this method: real devices, other browsers, real user data, and anything behind a login that was not opened.", ""]
    for sev, head in (("error", "Errors"), ("warn", "Warnings"), ("info", "Notes")):
        items = [f for f in findings if f["severity"] == sev]
        if not items:
            continue
        L += [f"## {head} ({len(items)})", ""]
        for f in items:
            cs = cases.get(f["case"], {})
            L.append(f"### {f['title']}")
            L.append(f"`{f['id']}` · {f['case']}{(' ' + cs['title']) if cs else ''} · **{f['basis']}**" + (f" · {f['standard']}" if f.get("standard") else "") + ("" if f["status"] == "confirmed" else " · unverified"))
            if f["where"]:
                L.append(f"- Where: {'; '.join(f['where'][:6])}" + (f" (+{len(f['where']) - 6} more)" if len(f["where"]) > 6 else ""))
            if f.get("measured"):
                L.append(f"- Measured: {f['measured']}")
            if f.get("expected"):
                L.append(f"- Expected: {f['expected']}")
            if f["evidence"]:
                L.append("- Evidence: " + ", ".join(f"`{e}`" for e in f["evidence"][:6]))
            if f.get("fix"):
                L.append(f"- Fix: {f['fix']}")
            L.append("")
    L += ["## Coverage", "", "| Cell | Status | Evidence |", "|---|---|---|"]
    for c, v in cells.items():
        L.append(f"| `{c}` | {v['status']} | {', '.join(v.get('evidence', [])[:3]) or (v.get('why') or '')} |")
    L += ["", "## Re-run", "", "Fix, then run the same cells again and `review.py check` on the new probe files: it prints what was resolved and what is new. Do not mark a cell done from memory.", ""]
    out = rd / "REPORT.md"
    out.write_text("\n".join(L), encoding="utf-8")
    print(f"{verdict}: {line}\nwritten: {out}")



def cases_markdown(doc):
    """references/cases.md, rendered from the same data as cases.json (tools/build_data.py calls this)."""
    groups = {g["id"]: g["title"] for g in doc.get("groups", [])}
    srcs = doc.get("sources", {})
    L = ["# Cases where a review goes wrong", "",
         "Generated from `synthesis/review-cases.json` by `tools/build_data.py`. Edit the source, not this file.", "",
         f"{len(doc.get('cases', []))} cases in {len(groups)} groups. **How known** is the strongest way a case can be checked: *measured* (a number read from the page), *operated* (you did it and saw the result) or *seen* (you looked). "
         "Cases marked *inferred* rest on reasoning more than on a cited source. `review.py cases` prints this list filtered to the page in front of you.", ""]
    for gid, title in groups.items():
        L += [f"## {title}", ""]
        for c in [c for c in doc["cases"] if c["group"] == gid]:
            L.append(f"### {c['id']} {c['title']}")
            L.append(f"*How known: {c['evidence']} · default severity: {c['severity']} · applies to: {c['when']}" + (f" · {c['standard']}" if c.get("standard") else "") + (" · inferred" if c.get("inferred") else "") + "*")
            L += ["", f"**What goes wrong.** {c['trap']}", "", f"**Why it is missed.** {c['why_missed']}", "", f"**How to catch it.** {c['catch']}", ""]
            if c.get("sources"):
                L.append("Sources: " + ", ".join(c["sources"]) + "")
                L.append("")
    L += ["## Sources", "", "| Id | Source | Status |", "|---|---|---|"]
    for sid, s in srcs.items():
        L.append(f"| {sid} | [{s['title']}]({s['url']}) | {s['status']}" + (f": {s['note']}" if s.get("note") else "") + " |" if s["url"].startswith("http") else f"| {sid} | {s['title']} (`{s['url']}`) | {s['status']}" + (f": {s['note']}" if s.get("note") else "") + " |")
    return "\n".join(L)


def cmd_cases(args):
    doc = load_cases()
    cases = doc.get("cases", [])
    if not cases:
        die("references/cases.json is missing. Run python3 tools/build_data.py from the OpenDesigner repo, or use the release zip.")
    when = {"always"} | {w.strip() for w in (args.when or "").split(",") if w.strip()}
    if args.id:
        cases = [c for c in cases if c["id"] in args.id.split(",")]
    else:
        if args.when is not None:
            cases = [c for c in cases if c["when"] in when]
        if args.group:
            cases = [c for c in cases if c["group"] == args.group]
    if not cases:
        die("no case matches")
    groups = {g["id"]: g["title"] for g in doc["groups"]}
    cur = None
    for c in cases:
        if c["group"] != cur:
            cur = c["group"]
            print(f"\n== {groups[cur]} ==")
        first = re.split(r"(?<=[.!?]) ", c["catch"])[0]
        if args.full or args.id:
            print(f"\n{c['id']} {c['title']}  [{c['evidence']}, {c['severity']}, applies to: {c['when']}]\n  goes wrong: {c['trap']}\n  missed because: {c['why_missed']}\n  catch it: {c['catch']}")
        else:
            print(f"{c['id']}  {c['title']}: {first}")
    print(f"\n{len(cases)} case(s). `--full` for the whole entry, `--id CV-05` for one, `--when motion,forms,overlays,data,i18n,touch,media` for what applies to this page.")


def cmd_sheet(args):
    rd = review_dir(args)
    folder = Path(args.folder) if args.folder else rd
    imgs = sorted(p for p in folder.rglob("*") if p.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"))
    if not imgs:
        die(f"no screenshots under {folder}")
    cards = "\n".join(f'<figure><a href="{html.escape(os.path.relpath(p, rd))}"><img loading="lazy" src="{html.escape(os.path.relpath(p, rd))}" alt="{html.escape(p.stem)}"></a>'
                      f"<figcaption>{html.escape(str(p.relative_to(folder)))}</figcaption></figure>" for p in imgs)
    page = f"""<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Review sheet</title>
<style>:root{{color-scheme:light dark}}body{{font:14px/1.4 system-ui,sans-serif;margin:16px}}h1{{font-size:18px}}
.g{{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:12px}}figure{{margin:0;border:1px solid #8884;border-radius:8px;overflow:hidden}}
img{{width:100%;display:block;background:#8881}}figcaption{{padding:6px 8px;font-size:12px;word-break:break-all}}</style>
<h1>Review sheet: {len(imgs)} screenshots</h1><p>Click one to open it at full size. Judge small detail on the full-size file, not on this sheet.</p><div class="g">{cards}</div>"""
    out = rd / "sheet.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    print(f"written: {out} ({len(imgs)} images)")
    if args.open:
        webbrowser.open(out.resolve().as_uri())


def image_size(path):
    """Pixel width and height of a PNG or JPEG, read from its header (no imaging library)."""
    b = Path(path).read_bytes()
    if b[:8] == b"\x89PNG\r\n\x1a\n":
        return int.from_bytes(b[16:20], "big"), int.from_bytes(b[20:24], "big")
    if b[:2] == b"\xff\xd8":
        i = 2
        while i < len(b) - 9:
            if b[i] != 0xFF:
                i += 1
                continue
            m = b[i + 1]
            if m in (0xC0, 0xC1, 0xC2):
                return int.from_bytes(b[i + 7:i + 9], "big"), int.from_bytes(b[i + 5:i + 7], "big")
            i += 2 + int.from_bytes(b[i + 2:i + 4], "big")
    die(f"{path}: use a PNG or JPEG screenshot")


def find_picker():
    """The house variant picker (opendesigner/assets/picker.js): bundled beside this skill, or in the sibling skill."""
    for p in (HERE.parent / "assets" / "picker.js", HERE.parent.parent / "opendesigner" / "assets" / "picker.js"):
        if p.exists():
            return p.read_text(encoding="utf-8")
    die("picker.js not found: install the opendesigner skill beside this one")


def source_line(src):
    """Where a fix comes from, in one line: an id gets the kind of source it is; anything else (a WCAG criterion, a
    shipped product, "my own idea") is shown as written."""
    s = src.strip()
    if re.match(r"^STD-[a-z-]+-\d+$", s):
        return f"house standard {s}"
    if re.match(r"^PRJ-\d+$", s):
        return f"project standard {s}"
    if re.match(r"^DC-L\d+-\d+$", s):
        return f"research default {s}"
    cases = {c["id"]: c["title"] for c in load_cases().get("cases", [])}
    if s in cases:
        return f"review case {s}, {cases[s]}"
    return s


def read_marks(path, label):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    marks = data.get("marks") if isinstance(data, dict) else data
    page = (data.get("page") if isinstance(data, dict) else None) or {}
    bad = [str(m.get("n", i + 1)) for i, m in enumerate(marks or []) if m.get("missing") or not m.get("rect")]
    if bad:
        die(f"{label}: marks {', '.join(bad)} found no element on the page; fix their selectors and run __od.marks() again")
    return marks or [], page


def cmd_compare(args):
    """The value of a fix, shown on the person's own page: today, the audit drawn on it, then the fix."""
    rd = review_dir(args)
    marks, page = read_marks(args.marks, "marks")
    if not marks:
        die("marks.json has no marks: list the issues first (review.py check, then __od.marks([{sel, title, gives}]))")
    for i, m in enumerate(marks):
        m.setdefault("n", i + 1)
        for k in ("title", "gives", "before", "after", "finding", "source"):
            if m.get(k) is not None and not isinstance(m[k], str):
                m[k] = str(m[k])
        if not (str(m.get("title") or "").strip() and str(m.get("gives") or "").strip()):
            die(f"mark {m['n']} needs a title (the issue) and gives (what fixing it makes better for the person)")
    unsourced = [str(m["n"]) for m in marks if not str(m.get("source") or "").strip()]
    if unsourced:
        print(f"note: mark(s) {', '.join(unsourced)} do not say where the fix comes from. Add \"source\": a house standard, a WCAG criterion, "
              "a preflight check, a review case, a shipped product, or \"my own idea\" (making.md section 3)")
    after_marks, after_page = read_marks(args.after_marks, "after marks") if args.after_marks else ([], {})
    shots = {}
    for key, path, pg in (("before", args.before, page), ("after", args.after, after_page)):  # no after marks: the shot's own size
        w, h = image_size(path)
        if pg.get("w") and pg.get("h") and abs(w / h - pg["w"] / pg["h"]) > 0.02 * (pg["w"] / pg["h"]):
            print(f"warning: {path} is {w}x{h} px but the page measured {pg['w']}x{pg['h']} CSS px; take a full-page screenshot "
                  "at the same width as __od.marks(), or the boxes will not sit on the issues")
        mime = "image/png" if Path(path).read_bytes()[:4] == b"\x89PNG" else "image/jpeg"
        shots[key] = (f"data:{mime};base64," + base64.b64encode(Path(path).read_bytes()).decode(), pg or {"w": w, "h": h})
    esc = html.escape

    def boxes(ms, pg, kind):
        W, H = pg.get("w") or 1, pg.get("h") or 1
        return "".join(f'<span class="mk {kind}{" edge" if m["rect"][0] < 12 or m["rect"][1] < 12 else ""}" style="left:{m["rect"][0] / W * 100:.3f}%;top:{m["rect"][1] / H * 100:.3f}%;'
                       f'width:{m["rect"][2] / W * 100:.3f}%;height:{m["rect"][3] / H * 100:.3f}%"><b>{m["n"]}</b></span>' for m in ms)

    def view(key, overlay=""):
        src, pg = shots[key]
        alt = "The page before the fix" if key == "before" else "The page after the fix"
        return f'<div class="shot"><div class="pg"><img src="{src}" alt="{alt}">{overlay}</div></div>'

    def gives(m):
        g = m["gives"].strip()
        if g.lower().startswith("fixing this"):
            return g
        return "Fixing this makes " + (g[0].lower() + g[1:] if g[1:2].islower() else g)  # "WCAG ..." keeps its capitals

    rows = "".join(f'<li><span class="n">{m["n"]}</span><div><p class="t">{esc(m["title"])}</p><p class="g">{esc(gives(m))}</p>'
                   + (f'<p class="e">{esc(m["before"])}' + (f' &rarr; {esc(m["after"])}' if m.get("after") else "") + "</p>" if m.get("before") else "")
                   + (f'<p class="e">Evidence: {esc(m["finding"])}</p>' if m.get("finding") else "")
                   + (f'<p class="e">From: {esc(source_line(m["source"]))}</p>' if str(m.get("source") or "").strip() else "") + "</div></li>" for m in marks)
    tall = max(pg.get("h", 1) / max(pg.get("w", 1), 1) for _, pg in shots.values())  # both views get the taller page's height, so nothing jumps
    title = args.title or "Before and after"
    page_html = f"""<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<link rel="icon" href="data:,">
<style>
:root{{color-scheme:light}}*{{box-sizing:border-box}}body{{margin:0;background:#f4f4f5;color:#18181b;font:15px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}}
main{{max-width:1200px;margin:0 auto;padding:24px 16px 120px}}h1{{font-size:22px;line-height:1.25;margin:0 0 4px;text-wrap:balance}}.lead{{margin:0 0 20px;color:#52525b;text-wrap:pretty}}
.shot{{aspect-ratio:1 / {tall:.4f};border-radius:12px;overflow:hidden;box-shadow:0 0 0 1px rgba(0,0,0,.08),0 8px 24px rgba(0,0,0,.08);background:#fff}}
.pg{{position:relative}}.pg img{{display:block;width:100%;height:auto}}
.mk{{position:absolute;border:2px dashed #c8202e;border-radius:4px;box-shadow:0 0 0 1px rgba(255,255,255,.9),inset 0 0 0 1px rgba(255,255,255,.9)}}
.mk.done{{border-style:solid;border-color:#12804a}}
.mk b{{position:absolute;top:-11px;left:-11px;min-width:22px;height:22px;padding:0 6px;border-radius:11px;background:#c8202e;color:#fff;font:600 12px/22px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;text-align:center;box-shadow:0 0 0 2px #fff}}
.mk.done b{{background:#12804a}}
.mk.edge b{{top:3px;left:3px}}
ol{{list-style:none;margin:28px 0 0;padding:0;display:grid;gap:12px;grid-template-columns:repeat(auto-fill,minmax(280px,1fr))}}
li{{display:flex;gap:12px;padding:14px 16px;background:#fff;border-radius:12px;box-shadow:0 0 0 1px rgba(0,0,0,.08)}}
li .n{{flex:none;width:24px;height:24px;border-radius:12px;background:#c8202e;color:#fff;font-size:12px;font-weight:600;line-height:24px;text-align:center}}
li p{{margin:0;text-wrap:pretty}}.t{{font-weight:600;text-wrap:balance}}.g{{color:#3f3f46}}.e{{margin-top:4px!important;color:#52525b;font-size:13px}}
.ask{{margin:24px 0 0;font-weight:600}}.help{{margin:16px 0 0;color:#52525b;font-size:13px}}
</style>
<main>
<h1>{esc(title)}</h1>
<p class="lead">{len(marks)} {"issue" if len(marks) == 1 else "issues"} found on this page. Switch between the page today, the audit and the fix with the bar at the bottom, or press 1, 2 and 3.</p>
<div data-od-stage>
<template data-od-variant="Today">{view("before")}</template>
<template data-od-variant="Audit">{view("before", boxes(marks, shots["before"][1], "todo"))}</template>
<template data-od-variant="Fixed">{view("after", boxes(after_marks, shots["after"][1], "done"))}</template>
</div>
<ol>{rows}</ol>
<p class="ask">Keep the fix, keep today's, or try another?</p>
<p class="help">Made by OpenDesigner (review.py compare). The boxes come from the page itself (probe.js __od.marks), measured at {shots["before"][1].get("w")} px wide.</p>
</main>
<script>{find_picker().replace("</", "<" + chr(92) + "/")}</script>
</html>
"""
    out = Path(args.out) if args.out else rd / "compare.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page_html, encoding="utf-8")
    print(f"written: {out} ({len(marks)} issues, {len(after_marks)} marked after; {out.stat().st_size // 1024} KB, self-contained)")
    if args.open:
        webbrowser.open(out.resolve().as_uri())


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    def common(p):
        p.add_argument("--dir", help="review folder (default ./opendesigner/review)")
        p.add_argument("--project", default=".", help="the project root (default .)")

    p = sub.add_parser("probe"); p.add_argument("--print", action="store_true"); p.set_defaults(fn=cmd_probe)
    p = sub.add_parser("serve"); common(p); p.add_argument("--port", type=int, default=7788); p.add_argument("--minutes", type=int, default=60); p.set_defaults(fn=cmd_serve)
    p = sub.add_parser("plan"); common(p); p.add_argument("--url", required=True); p.add_argument("--routes"); p.add_argument("--viewports", help="320,390x844,768")
    p.add_argument("--themes"); p.add_argument("--edges", action="store_true", help="also test one pixel below and at each breakpoint"); p.add_argument("--wide", action="store_true", help="add 1920x1080"); p.set_defaults(fn=cmd_plan)
    p = sub.add_parser("mark"); common(p); p.add_argument("cell"); p.add_argument("status", choices=["done", "todo", "skipped", "blocked"]); p.add_argument("--evidence", nargs="*"); p.add_argument("--why"); p.set_defaults(fn=cmd_mark)
    p = sub.add_parser("check"); common(p); p.add_argument("probes", nargs="+"); p.add_argument("--json", action="store_true"); p.add_argument("--all", action="store_true", help="also print info notes")
    p.add_argument("--audience", help="who the page is for (everyone, novice, expert): a non-expert audience turns on the jargon check (CP-04); the page's data-audience and the system's Q-aud-01 also set it"); p.set_defaults(fn=cmd_check)
    p = sub.add_parser("finding"); common(p); p.add_argument("text"); p.add_argument("--severity", choices=list(SEV), required=True); p.add_argument("--basis", choices=["seen", "operated", "inferred", "measured"], required=True)
    p.add_argument("--evidence", nargs="*"); p.add_argument("--where"); p.add_argument("--expected"); p.add_argument("--fix"); p.add_argument("--case"); p.set_defaults(fn=cmd_finding)
    p = sub.add_parser("report"); common(p); p.add_argument("--name"); p.set_defaults(fn=cmd_report)
    p = sub.add_parser("cases"); p.add_argument("--when", help="comma list: motion, forms, overlays, data, i18n, touch, media (plus the always-relevant ones)")
    p.add_argument("--group"); p.add_argument("--id", help="one or more ids, comma separated"); p.add_argument("--full", action="store_true"); p.set_defaults(fn=cmd_cases)
    p = sub.add_parser("sheet"); common(p); p.add_argument("folder", nargs="?"); p.add_argument("--open", action="store_true"); p.set_defaults(fn=cmd_sheet)
    p = sub.add_parser("compare"); common(p); p.add_argument("--before", required=True); p.add_argument("--after", required=True); p.add_argument("--marks", required=True)
    p.add_argument("--after-marks"); p.add_argument("--title"); p.add_argument("--out"); p.add_argument("--open", action="store_true"); p.set_defaults(fn=cmd_compare)
    args = ap.parse_args(argv)
    args.fn(args)


if __name__ == "__main__":
    main()
