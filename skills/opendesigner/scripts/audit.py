"""OpenDesigner: the system as the code builds it (audit-page), and what a reference would change in it (adapt).

Both pages report only. They read the person's code and state, and write one HTML page each; nothing in the code or in
state.json changes. A choice on a page comes back as OD: lines (references/rules.md section 9), and the agent acts on
those only after the person copies them:

    engine.py audit-page [--project <folder>] [--open] [--json]   opendesigner/audit.html
    engine.py adapt <reference.json> [--open] [--json]           opendesigner/adapt.html

audit-page builds on `engine.py review`: it runs the same scan (with the same od-ignore lines and exempt folders), then
groups what it found into inconsistencies a person can decide on: near-duplicate colours, spacing, radii and type sizes off
the scale, raw values that are on the scale but skip the tokens, raw shadows, and components drawn several ways. Each comes
with file:line evidence, a count, and two or three options previewed with the project's own values.

adapt builds on `engine.py intake` (fit_reference): it fits a reference's measurements to the dials, applies them to a copy
of the system, and shows what changes and what stays side by side. It keeps the identity rules in AGENTS.md: structure and
quality only; a reference's logo, brand hue, typeface, imagery and copy never carry over, except through a Taste Index the
person chose to follow.

The engine module is passed in (eng), so this file never imports engine.py itself and works wherever engine.py runs.
"""
from __future__ import annotations

import collections
import copy
import json
import os
import re
import webbrowser

TEMPLATES = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "templates")
EVIDENCE_CAP = 40       # file:line rows kept per issue (the count is always the full count)
NEAR_COLOR = 0.02       # OKLab distance under which two raw colours read as the same colour [inferred: 2 delta E OK; white and #f3f4f6, 0.033 apart, are two surfaces]
TOP_VALUES = 6          # off-scale values that get an issue of their own; the rest share one
COMPONENT_WORDS = [("button", r"btn|button|cta"), ("card", r"card|tile|panel"), ("badge", r"badge|chip|tag|pill|label"),
                   ("input", r"input|field|textfield|textarea|select"), ("dialog", r"modal|dialog|sheet|drawer"),
                   ("tab", r"tabs?\b|tab-"), ("tooltip", r"tooltip|popover"), ("alert", r"alert|toast|banner|callout|notice"),
                   ("avatar", r"avatar")]
SIG_PROPS = ("border-radius", "padding", "font-size", "height", "min-height", "background", "background-color", "font-weight")
RX_RULE = re.compile(r"([^{}@;]+)\{([^{}]*)\}")
RX_PX = re.compile(r"(-?\d+(?:\.\d+)?)(px|rem)\b")


# ---------------------------------------------------------------------------------------------- shared helpers

def _plural(n, word, many=None):
    return f"{n} {word if n == 1 else (many or word + 's')}"


def _px_of(value):
    m = RX_PX.search(value or "")
    if not m:
        return None
    v = float(m.group(1)) * (16 if m.group(2) == "rem" else 1)
    return int(v) if v.is_integer() else round(v, 2)


def _fill(name, payload, title, dest):
    """Write template <name>.html with payload in its od-data block (the same substitution cmd_show uses)."""
    with open(os.path.join(TEMPLATES, f"{name}.html"), encoding="utf-8") as f:
        html = f.read()
    blob = json.dumps(payload, indent=1, ensure_ascii=False).replace("</", "<\\/")
    html, n = re.subn(r'(<script type="application/json" id="od-data">).*?(</script>)',
                      lambda m: m.group(1) + "\n" + blob + "\n" + m.group(2), html, count=1, flags=re.S)
    if n != 1:
        raise SystemExit(f"template {name}.html has no od-data block")
    html = html.replace("<title>OpenDesigner · ", f"<title>{_esc(title)} · ", 1)
    os.makedirs(os.path.dirname(os.path.abspath(dest)), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        f.write(html)
    return dest


def _esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _look(eng, files, meta):
    """The light-mode look the previews are drawn in: the --t-* variables the other templates read."""
    tv = eng.template_vars(files, meta)
    return {"shared": tv["shared"], "light": tv.get("light") or {}, "dark": tv.get("dark") or {}}


def _short(path):
    rel = os.path.relpath(path)
    return rel if not rel.startswith(".." + os.sep + "..") else os.path.abspath(path)


def _token_vars(eng, light, prefix):
    """{--ds-x: css value} for colours and sizes, so a preview of code written with var(--ds-x) draws as it does in the app."""
    out = {}
    for p, t in light.items():
        v = t.get("resolved")
        if t["type"] == "color":
            out[eng.css_var(prefix, p)] = eng.hex_of(v)
        elif t["type"] == "dimension" and isinstance(v, dict) and isinstance(v.get("value"), (int, float)):
            out[eng.css_var(prefix, p)] = f"{eng.fmt_num(v['value'])}{v.get('unit', 'px')}"
    return out


def _var_name(eng, prefix, path):
    return eng.css_var(prefix, path)[len(prefix) + 3:]


# ---------------------------------------------------------------------------------------------- audit-page

def _near(a, b):
    """OKLab distance with the colour axes counted twice: a pale blue and a pale grey of the same lightness are two colours
    on purpose more often than two lightness steps 0.02 apart are [inferred]."""
    return ((a[0] - b[0]) ** 2 + 4 * ((a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)) ** 0.5


def _clusters(eng, hex_rows):
    """Raw colours that read as the same colour: [[hex, ...] sorted by use], each cluster with two or more hexes."""
    counts = collections.Counter(h for h, _ in hex_rows)
    lab = {h: eng.oklch_to_oklab(*eng.hex_to_oklch(h)) for h in counts}
    out = []
    for h, _ in counts.most_common():
        for c in out:
            if _near(lab[h], lab[c[0]]) < NEAR_COLOR:
                c.append(h)
                break
        else:
            out.append([h])
    return [c for c in out if len(c) > 1], counts


def _evidence(rows, cap=EVIDENCE_CAP):
    return [{"file": f, "line": ln, "value": v} for f, ln, v in rows[:cap]]


def _issue(iid, kind, title, plain, rows, options, preview, why=""):
    return {"id": iid, "kind": kind, "title": title, "plain": plain, "count": len(rows), "files": len({r[0] for r in rows}),
            "evidence": _evidence(rows), "more": max(0, len(rows) - EVIDENCE_CAP), "options": options, "preview": preview, "why": why}


def _opt(oid, label, note, after, recommended=False, od=None):
    return {"id": oid, "label": label, "note": note, "after": after, "recommended": recommended, **({"od": od} if od else {})}


def _keep(iid):
    return _opt("keep", "Keep as it is, on purpose", "Nothing changes. Say why below: it goes in the ledger as a waiver, with your name.",
                None, od=[f"OD:waive {iid}"])


def _neighbours(v, steps):
    steps = sorted(set(steps))
    lo = max([s for s in steps if s < v], default=None)
    hi = min([s for s in steps if s > v], default=None)
    return lo, hi


def _components(eng, d, project):
    """Component rules in the project's CSS (and <style> blocks), grouped by kind, with the values that draw them."""
    targets, base, _ = eng.review_targets(project, os.path.abspath(d))
    state = eng.load_state(d)
    rules_ = eng.exempt_rules(state)
    root = eng.exempt_root(d, project)
    found = collections.defaultdict(list)
    for path in targets:
        if os.path.splitext(path)[1].lower() not in (".css", ".scss", ".less", ".html", ".vue", ".svelte"):
            continue
        if rules_ and eng.exempt_match(rules_, path, root):
            continue
        try:
            if os.path.getsize(path) > 1_000_000:
                continue
            with open(path, encoding="utf-8", errors="ignore") as f:
                text = f.read()
        except OSError:
            continue
        if eng.generated_file(text.splitlines(True)[:12]):
            continue
        rel = os.path.relpath(path, base)
        text = re.sub(r"/\*.*?\*/|<!--.*?-->", lambda m: re.sub(r"[^\n]", " ", m.group(0)), text, flags=re.S)  # same length
        for m in RX_RULE.finditer(text):
            sel, body = m.group(1).strip(), m.group(2)
            if not sel or ":" in re.sub(r"::?(?:root|where|is|not)\b", "", sel) or "od-ignore" in body or len(sel) > 160:
                continue  # states (:hover, :focus) are not variants; very long selectors are resets
            last = re.split(r"[\s>+~]+", sel.split(",")[-1].strip())[-1]  # .bento-card h3 is a heading, not a card
            classes = re.findall(r"\.([A-Za-z][\w-]*)", last)
            kind = next((k for k, rx in COMPONENT_WORDS for c in classes if re.search(rx, c, re.I)), None)
            if not kind:
                continue
            props = {}
            for decl in body.split(";"):
                if ":" in decl:
                    k, v = decl.split(":", 1)
                    k = k.strip().lower()
                    if k in SIG_PROPS:
                        props["background" if k == "background-color" else k] = v.strip()
            if len(props) < 2:
                continue
            line = text.count("\n", 0, m.start() + len(m.group(0)) - len(m.group(0).lstrip())) + 1
            found[kind].append({"file": rel, "line": line, "selector": sel[:80], "props": props})
    return found


def audit_data(eng, d, project=None):
    """Everything audit.html shows, from one run of review's scan."""
    col = {}
    eng.cmd_review(d, project, collect=col)
    state, meta, light, prefix = col["state"], col["meta"], col["light"], col["prefix"]
    ladder, radii, sizes = sorted(col["ladder"]), col["radii"], sorted(col["sizes"])
    uses = col["tokenUses_by"]
    findings = col["allFindings"]
    files = col["files"]
    H = lambda p: eng.hex_of(light[p]["resolved"]).lower() if p in light and light[p]["type"] == "color" else None
    proj = col["project"]

    # ---- the system: every token family, and where the code follows it
    def where(path):
        rows = uses.get(_var_name(eng, prefix, path)) or []
        return len(rows), [f"{f}:{ln}" for f, ln in rows[:4]]

    def fam(name, plain, items):
        n_used = sum(1 for x in items if x["uses"])
        return {"name": name, "plain": plain, "tokens": items, "used": n_used, "total": len(items)}
    colors = []
    for p, t in light.items():
        if t["type"] != "color" or not p.startswith(("color.text.", "color.bg.", "color.surface.", "color.border.", "color.icon.")):
            continue
        n, at = where(p)
        colors.append({"path": p, "var": eng.css_var(prefix, p), "value": H(p), "uses": n, "at": at})
    colors.sort(key=lambda x: (-x["uses"], x["path"]))
    space = []
    for v in ladder:
        n, at = where(f"space.{v}")
        space.append({"path": f"space.{v}", "var": eng.css_var(prefix, f"space.{v}"), "value": v, "uses": n, "at": at})
    rad = []
    for k, v in radii.items():
        n, at = where(f"radius.{k}")
        rad.append({"path": f"radius.{k}", "var": eng.css_var(prefix, f"radius.{k}"), "value": v, "uses": n, "at": at})
    type_ = []
    for v in sizes:
        n, at = where(f"font.size.{v}")
        type_.append({"path": f"font.size.{v}", "var": eng.css_var(prefix, f"font.size.{v}"), "value": v, "uses": n, "at": at})
    elev = []
    for p in ("elevation.raised", "elevation.floating", "elevation.overlay"):
        if p in light:
            n, at = where(p)
            elev.append({"path": p, "var": eng.css_var(prefix, p), "value": eng._css_shadow(light[p]["resolved"]), "uses": n, "at": at})
    motion = []
    for p, t in light.items():
        if p.startswith("motion.duration.") and t["type"] == "duration":
            n, at = where(p)
            motion.append({"path": p, "var": eng.css_var(prefix, p), "value": eng.duration_ms(t["resolved"]), "uses": n, "at": at})
    families = [fam("Colours", "The named colours: text, backgrounds, surfaces, borders and icons.", colors),
                fam("Spacing", f"The space ladder, on a {meta['space']['unit']}px unit.", space),
                fam("Corners", "The corner radius for each kind of element.", rad),
                fam("Type sizes", f"The type scale, ratio {meta['type']['ratio']}.", type_),
                fam("Depth", f"Shadows (depth model: {meta['elevation']['model']}).", elev),
                fam("Motion", "How long things take to move.", motion)]

    # ---- decisions: each answer, how it was set, and whether it changes tokens (purpose audit C1, said plainly)
    raw_by_kind = collections.Counter(f["kind"] for f in findings)
    area_kind = {"color": ("Colours", "color"), "type": ("Type sizes", "size"), "space": ("Spacing", "size"), "density": ("Spacing", "size"),
                 "layout": ("Spacing", "size"), "shape": ("Corners", "radius"), "depth": ("Depth", "shadow"), "motion": ("Motion", "duration")}
    fam_uses = {f_["name"]: sum(x["uses"] for x in f_["tokens"]) for f_ in families}
    decisions = []
    for qid, rec in sorted((state.get("answers") or {}).items()):
        area = qid.split("-")[1] if qid.count("-") >= 2 else ""
        try:
            val = eng.answer_value(rec)
            words = eng.answer_words(qid, val)
            effects = eng.answer_effects(qid, val, state)
        except Exception:  # an answer the engine no longer knows: shown, never fatal
            words, effects = str(rec), {}
        fam_name, kind = area_kind.get(area, (None, None))
        decisions.append({"id": qid, "answer": str(words)[:120], "setBy": (rec.get("set_by") if isinstance(rec, dict) else None) or "chosen",
                          "changesTokens": bool(effects) or qid in getattr(eng, "STATE_QS", ()), "family": fam_name,
                          "follows": fam_uses.get(fam_name) if fam_name else None, "raw": raw_by_kind.get(kind) if kind else None})
    dials = [{"id": k, "value": v.get("value") if isinstance(v, dict) else v,
              "setBy": (v.get("set_by") if isinstance(v, dict) else None) or "default"} for k, v in sorted((state.get("dials") or {}).items())]

    # ---- inconsistencies
    issues = []
    tokens_hex = {p: H(p) for p in light if light[p]["type"] == "color" and p.startswith(("color.text.", "color.bg.", "color.surface.", "color.border."))}

    def nearest_token(hx):
        best, dist = None, 9
        a = eng.oklch_to_oklab(*eng.hex_to_oklch(hx))
        for p, h in tokens_hex.items():
            if not h:
                continue
            b = eng.oklch_to_oklab(*eng.hex_to_oklch(h))
            dd = sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5
            if dd < dist:
                best, dist = p, dd
        return best, dist

    hex_rows = [(f["value"].lower(), (f["file"], f["line"], f["value"].lower())) for f in findings
                if f["kind"] == "color" and re.fullmatch(r"#[0-9a-fA-F]{6}", f["value"])]
    clusters, hex_count = _clusters(eng, hex_rows)
    clusters.sort(key=lambda c: -sum(hex_count[h] for h in c))
    for c in clusters[:8]:
        iid = f"A-color-{c[0][1:]}"   # named after the colour used most: stable across runs and exempt changes
        rows = [r for h, r in hex_rows if h in c]
        top = c[0]
        tok, dist = nearest_token(top)
        opts = []
        if tok and dist < 0.08:
            opts.append(_opt("token", f"Use {tok}", f"Every one of these becomes var({eng.css_var(prefix, tok)}), {tokens_hex[tok]}.",
                             {"color": tokens_hex[tok]}, recommended=True))
        if not (tok and tokens_hex[tok] == top):
            opts.append(_opt("common", f"Merge into {top}, the one used most", f"{_plural(len(rows) - hex_count[top], 'use')} {'changes' if len(rows) - hex_count[top] == 1 else 'change'} to {top}. "
                             + ("It is not a token yet: add it as one first (engine.py set color.<role>.<name>)." if not (tok and dist < 0.01) else ""),
                             {"color": top}, recommended=not opts))
        if len(opts) < 2 and tok and tokens_hex[tok] != top:
            opts.append(_opt("token", f"Use {tok}, the nearest token", f"Every one becomes var({eng.css_var(prefix, tok)}), "
                             f"{tokens_hex[tok]}; a visible change, so check it on the page.", {"color": tokens_hex[tok]}))
        opts.append(_keep(iid))
        issues.append(_issue(iid, "color", f"{len(c)} colours that look the same", "These raw colours are so close that nobody can tell "
                             "them apart, so they are one colour written several ways.", rows, opts,
                             {"values": [{"value": h, "count": hex_count[h]} for h in c]}))

    def size_rows(kind, prop_rx):
        out = []
        for f in findings:
            if f["kind"] != kind:
                continue
            v = _px_of(f["value"])
            if v is None or not re.search(prop_rx, f["value"], re.I):
                continue
            out.append((v, (f["file"], f["line"], f["value"])))
        return out

    def scale_issues(kind, rows, steps, unit_word, title_fn, plain, preview_kind, token_of, near_word, min_v=0, max_v=10 ** 9):
        """One issue per off-scale value (the most used first), one for the rest. min_v leaves out hairlines (1px and 2px
        nudges are optical, not spacing); max_v leaves out pill radii (999px means fully round, not a scale step)."""
        by_val = collections.defaultdict(list)
        for v, r in rows:
            by_val[v].append(r)
        off = sorted(((v, rs) for v, rs in by_val.items() if v not in steps and v > min_v and v < max_v), key=lambda x: -len(x[1]))
        steps = [x for x in steps if x > 0]
        on = [r for v, rs in by_val.items() if v in steps for r in rs]
        for v, rs in off[:TOP_VALUES]:
            iid = f"A-{kind}-{v:g}px".replace(".", "_")
            lo, hi = _neighbours(v, steps)
            opts = []
            for s_, which in sorted(((s_, w) for s_, w in ((lo, "down"), (hi, "up")) if s_ is not None), key=lambda x: abs(x[0] - v)):
                opts.append(_opt(f"{which}", f"Round {which} to {s_:g}{unit_word}", f"Use {token_of(s_)}.", {"value": s_},
                                 recommended=not opts))
            if len(opts) < 2:
                opts.append(_opt("add", f"Add {v:g}{unit_word} to the system", f"Record it as a token with a reason (engine.py set), "
                                 f"then use the token: worth it only if {v:g}{unit_word} is a deliberate step.", {"value": v}))
            opts.append(_keep(iid))
            issues.append(_issue(iid, preview_kind, title_fn(v, len(rs)), plain, rs, opts, {"value": v, "steps": steps}))
        rest = [r for v, rs in off[TOP_VALUES:] for r in rs]
        if rest:
            iid = f"A-{kind}-others"
            vals = sorted({v for v, _ in off[TOP_VALUES:]})
            issues.append(_issue(iid, preview_kind, f"{_plural(len(vals), 'more ' + near_word + ' value')} off the scale",
                                 f"Values used less often: {', '.join(f'{x:g}' for x in vals[:16])}{' and more' if len(vals) > 16 else ''}.",
                                 rest, [_opt("nearest", "Round each to the nearest step", "Each value moves to the closest token.", {"nearest": True},
                                             recommended=True), _keep(iid)], {"values": vals, "steps": steps}))
        return on

    on_space = scale_issues("space", size_rows("size", r"^(padding|margin|gap|row-gap|column-gap|p[xytrbl]?-|m[xytrbl]?-|gap-)"),
                            ladder, "px", lambda v, n: f"Spacing of {v:g}px, {_plural(n, 'time')}",
                            "This spacing is not on the system's ladder, so gaps drift a pixel or two from screen to screen.",
                            "space", lambda s_: f"var({eng.css_var(prefix, f'space.{s_:g}')})", "spacing", min_v=2)
    on_type = scale_issues("type", size_rows("size", r"font-?size|^text-\["), sizes, "px",
                           lambda v, n: f"Text at {v:g}px, {_plural(n, 'time')}",
                           "This text size is not on the type scale, so headings and labels stop lining up as one family.",
                           "type", lambda s_: f"var({eng.css_var(prefix, f'font.size.{s_:g}')}) or a text style", "type")
    rvals = sorted(set(radii.values()))
    rname = {v: k for k, v in radii.items()}
    on_rad = scale_issues("radius", size_rows("radius", r"radius|rounded"), rvals, "px",
                          lambda v, n: f"Corners of {v:g}px, {_plural(n, 'time')}",
                          "This corner radius is not one of the system's, so similar things end up with different corners.",
                          "radius", lambda s_: f"var({eng.css_var(prefix, 'radius.' + rname[s_])}), the {rname[s_]} radius", "corner",
                          max_v=100)
    on_scale = on_space + on_type + on_rad
    raw_colors_on_token = [r for h, r in hex_rows if nearest_token(h)[1] < 0.004]
    bypass = on_scale + raw_colors_on_token
    if bypass:
        iid = "A-bypass"
        issues.append(_issue(iid, "bypass", f"{_plural(len(bypass), 'value')} on the scale, written by hand",
                             "These values match a token already, but they are typed in, so a change to the system never reaches them.",
                             sorted(bypass, key=lambda r: (r[0], r[1])),
                             [_opt("tokens", "Write the token instead", "The page looks the same; the value now follows the system.",
                                   {"same": True}, recommended=True), _keep(iid)], {"same": True}))
    shadows = [(f["file"], f["line"], f["value"]) for f in findings if f["kind"] == "shadow"]
    if shadows:
        iid = "A-shadow"
        distinct = collections.Counter(r[2] for r in shadows)
        steps = [{"path": e_["path"], "value": e_["value"]} for e_ in elev]
        issues.append(_issue(iid, "shadow", f"{_plural(len(distinct), 'shadow')} written by hand",
                             f"The system has {_plural(len(steps), 'shadow step')}; these {_plural(len(distinct), 'other')} make depth look uneven.",
                             shadows, [_opt("tokens", "Use the system's shadow steps", "Each becomes the raised, floating or overlay step.",
                                            {"steps": steps}, recommended=True),
                                       _opt("borders", "Borders instead of shadows", "Each becomes a 1px border in the border colour; flat "
                                            "and quiet, like the borders depth model.", {"steps": [{"path": "border", "value": "0 0 0 1px rgba(128,128,128,.45)"}]}),
                                       _keep(iid)],
                             {"values": [{"value": v, "count": n} for v, n in distinct.most_common(6)], "steps": steps}))
    comps = _components(eng, d, project or proj)
    tv = _look(eng, files, meta)
    for kind, rows in sorted(comps.items(), key=lambda kv: -len(kv[1])):
        sigs = collections.OrderedDict()
        for r in rows:
            key = json.dumps(r["props"], sort_keys=True)
            sigs.setdefault(key, []).append(r)
        if len(sigs) < 3:
            continue
        iid = f"A-comp-{kind}"
        variants = sorted(({"props": json.loads(k), "count": len(v), "at": [f"{x['file']}:{x['line']}" for x in v[:3]],
                            "selector": v[0]["selector"]} for k, v in sigs.items()), key=lambda x: -x["count"])
        once = [v for v in variants if v["count"] == 1]
        sysv = {"border-radius": tv["shared"]["radius-control" if kind in ("button", "input", "badge", "tab") else "radius-container"],
                "padding": f"0 {tv['shared']['pad-x']}" if kind in ("button", "input") else tv["shared"]["pad-x"],
                "font-size": tv["shared"]["size"]}
        if kind in ("button", "input"):
            sysv["height"] = tv["shared"]["control-h"]
        evid = [(r["file"], r["line"], r["selector"]) for r in rows]
        issues.append(_issue(iid, "component", f"{len(variants)} different {kind}s",
                             f"The code draws {kind}s {len(variants)} ways; {_plural(len(once), 'of them is', 'of them are')} used once. "
                             "One look per kind, with named variants, is easier to keep consistent.", evid,
                             [_opt("system", f"One {kind}, from the system's tokens", "Every variant takes the system's corner, padding and "
                                   "size; a variant you keep gets a name (primary, quiet...).", {"props": sysv}, recommended=True)]
                             + ([_opt("common", f"One {kind}, the one used most ({variants[0]['selector']})",
                                      f"Every variant takes the values of {variants[0]['selector']}, used {variants[0]['count']} times.",
                                      {"props": variants[0]["props"]})] if variants[0]["count"] > 1 else
                                [_opt("named", f"Two {kind}s: a main one and a quiet one", "The system's look for the main one, and the same "
                                      "shape with no fill for the rest; every variant becomes one of the two.", {"props": dict(sysv, background="transparent")})])
                             + [_keep(iid)],
                             {"variants": variants[:8], "kind": kind}))

    order = {"component": 0, "color": 1, "space": 2, "type": 3, "radius": 4, "shadow": 5, "bypass": 6}
    issues.sort(key=lambda i: (order.get(i["kind"], 9), i["id"]))
    rounds = eng.ledger_rounds(state)
    seen = {it["id"]: it for r in rounds for it in r.get("items") or []}
    for i in issues:
        if i["id"] in seen:
            i["ledger"] = {"status": seen[i["id"]].get("status"), "why": seen[i["id"]].get("why"), "by": seen[i["id"]].get("by")}
    raw_total = sum(1 for f in findings if f["kind"] not in ("standard", "chart", "removed"))
    return {"name": state.get("name") or "Your product", "project": os.path.basename(os.path.abspath(proj).rstrip(os.sep)) or _short(proj),
            "scanned": col["filesScanned"], "tokenUses": col["tokenUses"], "raw": raw_total,
            "standards": sum(1 for f in findings if f["kind"] == "standard"), "verdict": col["reasons"], "ok": col["ok"],
            "tokens": col["tokens"], "notes": col["notes"], "families": families, "decisions": decisions, "dials": dials,
            "issues": issues, "exempt": col["exempt"],
            "kept": [{"file": k["file"], "line": k["line"], "reason": k["reason"]} for k in col["keptAll"][:200]],
            "keptCount": len(col["keptAll"]), "ledger": rounds, "vars": _token_vars(eng, light, prefix), "ledgerOpen": col["ledgerOpen"], "look": tv, "prefix": prefix}


def audit_page(eng, d, project=None, open_=False, as_json=False, out=None):
    if not os.path.exists(os.path.join(d, eng.STATE_FILE)):
        raise SystemExit(f"No system here ({os.path.join(d, eng.STATE_FILE)}). The audit page compares the code with a system: run "
                         "engine.py sketch (or init) first, or point --dir at one. engine.py review still scans code with no system.")
    data = audit_data(eng, d, project)
    if as_json:
        print(json.dumps(data, indent=1, ensure_ascii=False))
        return 0
    dest = out or os.path.join(d, "audit.html")
    _fill("audit", data, data["name"], dest)
    n = len(data["issues"])
    print(f"wrote {dest}: {data['scanned']} files, {data['tokenUses']} token uses against {data['raw']} raw values, "
          f"{_plural(n, 'inconsistency', 'inconsistencies')} to decide on, each with file:line evidence and options.")
    for i in data["issues"][:8]:
        print(f"  {i['id']}  {i['title']} ({_plural(i['files'], 'file')})")
    if n > 8:
        print(f"  ... and {n - 8} more on the page.")
    if data["exempt"]:
        print("  Left out on purpose: " + "; ".join(f"{r['glob']} ({r['files']} files)" for r in data["exempt"]))
    print("Nothing in the code changed. The person picks on the page and copies OD: lines; apply them only then "
          "(references/rules.md section 9), each one as a ledger item.")
    eng.track(d, "audit-page")
    if open_:
        webbrowser.open("file://" + os.path.abspath(dest))
    return 0


# ---------------------------------------------------------------------------------------------- adapt

IDENTITY = ("raw.brandColor", "raw.brandFace", "raw.textFace", "raw.displayFace", "raw.monoFace", "raw.logo")
COMPARE = [("radius.control", "Button and field corners"), ("radius.container", "Card corners"),
           ("control.height.md", "Control height"), ("font.size.body", "Body text size"), ("type.ratio", "Type scale ratio"),
           ("space.inset", "Padding inside things"), ("depth", "Depth"), ("surface", "Page and card colours"),
           ("accent", "Accent colour")]


def _facts(eng, files, meta):
    tv = eng.template_vars(files, meta)
    sh, lt = tv["shared"], tv.get("light") or {}
    return {"radius.control": sh["radius-control"], "radius.container": sh["radius-container"], "control.height.md": sh["control-h"],
            "font.size.body": sh["size"], "type.ratio": sh["ratio"], "space.inset": sh["pad-x"], "depth": meta["elevation"]["model"],
            "surface": f"{lt.get('bg')} / {lt.get('surface')}", "accent": lt.get("accent")}, tv


def adapt_data(eng, d, ref_path):
    if not os.path.isfile(ref_path):
        raise SystemExit(f"File not found: {ref_path}. Give the measurements from opendesigner-extract (css_scan.py --json).")
    try:
        ref = eng.read_json(ref_path)
    except ValueError as ex:
        raise SystemExit(f"{ref_path} is not JSON the engine can read ({ex}).")
    state = eng.merge_defaults(eng.load_state(d))
    fit = eng.fit_reference(ref, state)
    rid = fit["id"] if fit["id"] != "ref" else eng.slug(os.path.splitext(os.path.basename(ref_path))[0])
    follows = (state.get("tasteIndex") or {}).get("follows") == rid  # only the index the person follows may carry identity
    held = eng.std_held(state) if eng.std_has_records(state) else {}
    files0, meta0, _ = eng.generate_system(eng.load_state(d))
    s2 = copy.deepcopy(state)
    changes, stays = [], []
    for pr in fit["proposals"]:
        path = eng.normalize_path(pr["path"])
        rec = eng.get_path(state, path)
        cur = rec.get("value") if isinstance(rec, dict) and "value" in rec else rec
        how = rec.get("set_by") if isinstance(rec, dict) else None
        if path in IDENTITY and not (follows or pr["basis"].startswith("the person's own")):
            stays.append({"path": path, "now": cur, "why": "identity: a reference's brand colour and typeface never carry over "
                          "(only a Taste Index you choose to follow keeps them)"})
            continue
        if eng.is_locked(state, path):
            stays.append({"path": path, "now": cur, "ref": pr["value"], "why": "you locked it"})
            continue
        sid = held.get(path) or held.get("overrides." + path)
        if sid:
            stays.append({"path": path, "now": cur, "ref": pr["value"], "why": f"standard {sid} holds it"})
            continue
        if cur == pr["value"]:
            stays.append({"path": path, "now": cur, "why": "already the same as the reference"})
            continue
        eng._store(s2, path, pr["value"], "reference", f"adapt preview from {rid}", False)
        changes.append({"path": path, "now": "default" if cur is None else cur, "ref": pr["value"], "confidence": pr["confidence"],
                        "basis": pr["basis"], "chosen": how == "chosen",
                        "od": f"OD:accept {rid}:{path}={json.dumps(pr['value'], ensure_ascii=False)}"})
    files1, meta1, _ = eng.generate_system(s2)
    before, tv0 = _facts(eng, files0, meta0)
    after, tv1 = _facts(eng, files1, meta1)
    table = [{"what": label, "key": k, "now": before[k], "adapted": after[k], "changed": before[k] != after[k]} for k, label in COMPARE]
    for k in ("raw.brandColor", "raw.textFace", "raw.displayFace"):
        if not any(s_["path"] == k for s_ in stays + changes):
            v = eng.get_path(state, k)
            v = v.get("value") if isinstance(v, dict) and "value" in v else v
            if v:
                stays.append({"path": k, "now": v, "why": "yours: identity stays with you"})
    for k, v in sorted((state.get("locks") or {}).items()) if isinstance(state.get("locks"), dict) else []:
        if v and not any(s_["path"] == k for s_ in stays):
            stays.append({"path": k, "now": None, "why": "you locked it"})
    return {"name": state.get("name") or "Your product", "ref": {"id": rid, "tag": fit["tag"], "kind": fit["kind"],
                                                                 "file": _short(ref_path)},
            "changes": changes, "stays": stays, "notes": fit["notes"], "table": table, "before": tv0, "after": tv1,
            "tasteIndex": follows, "intake": f"engine.py intake {_short(ref_path)}"}


def adapt_page(eng, d, ref_path, open_=False, as_json=False, out=None):
    if not os.path.exists(os.path.join(d, eng.STATE_FILE)):
        raise SystemExit(f"No system here ({os.path.join(d, eng.STATE_FILE)}). adapt changes an existing system: run engine.py sketch "
                         "first, or start from the reference with engine.py intake.")
    data = adapt_data(eng, d, ref_path)
    if as_json:
        print(json.dumps(data, indent=1, ensure_ascii=False))
        return 0
    dest = out or os.path.join(d, "adapt.html")
    _fill("adapt", data, data["name"], dest)
    mine = [c["path"] for c in data["changes"] if c["chosen"]]
    print(f"wrote {dest}: {_plural(len(data['changes']), 'change')} proposed from {data['ref']['id']}, "
          f"{_plural(len(data['stays']), 'thing')} that stay. Nothing was recorded.")
    for c in data["changes"]:
        print(f"  {c['path']}: {json.dumps(c['now'])} -> {json.dumps(c['ref'])}  ({c['confidence']}; {c['basis']})")
    for s_ in data["stays"]:
        print(f"  stays {s_['path']}: {s_['why']}")
    if mine:
        print(f"  The person chose {', '.join(mine)} themselves: those start unticked, and change only if they tick them.")
    print(f"The person ticks what to take and copies OD:accept lines; record each with engine.py set <path> <value> --set-by reference "
          f"--source-ref {data['ref']['id']} (or {data['intake']} --accept for all).")
    eng.track(d, "adapt")
    if open_:
        webbrowser.open("file://" + os.path.abspath(dest))
    return 0
