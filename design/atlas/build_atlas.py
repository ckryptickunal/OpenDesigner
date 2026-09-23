#!/usr/bin/env python3
"""Build the four review artboards from the token files (stdlib only).

    python3 design/atlas/build_atlas.py

Every color, size and type value is read from design/tokens/*.tokens.json through the resolver
(check_contrast.resolve), so the artboards cannot drift from the tokens. Output is plain HTML with
inline styles and literal values (no CSS variables, no external assets), 1440px wide, flexbox only.
Each top-level <section data-group="..."> is one visual group = one Paper write_html call.
"""
import html
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "tokens"))
from check_contrast import contrast, resolve  # noqa: E402

T = {"light": resolve("light"), "dark": resolve("dark")}
TC = resolve("light", "compact")
NS = "dev.dsbuilder"


# ---------------------------------------------------------------- token access

def col(path, mode="light"):
    v = T[mode][path]["resolved"]
    a = v.get("alpha", 1)
    if a < 1:
        r, g, b = (int(v["hex"][i:i + 2], 16) for i in (1, 3, 5))
        return f"rgba({r},{g},{b},{a})"
    return v["hex"]


def hx(path, mode="light"):
    return T[mode][path]["resolved"]["hex"]


def num(path, t=None):
    return (t or T["light"])[path]["resolved"]["value"]


def ratio(fg, bg, mode="light"):
    return contrast(hx(fg, mode), hx(bg, mode))


def stack(lst):
    return ", ".join(f"'{x}'" if " " in x else x for x in lst)


SANS = stack(T["light"]["font.family.sans"]["resolved"])
MONO = stack(T["light"]["font.family.mono"]["resolved"])


def ty(style):
    tok = T["light"]["text." + style]
    v, ext = tok["resolved"], tok["$extensions"][NS]
    s = "" if "Inter" in v["fontFamily"] else f"font-family:{MONO};"
    s += f"font-size:{v['fontSize']['value']}px;line-height:{ext['lineHeightPx']}px;font-weight:{v['fontWeight']}"
    if v["letterSpacing"]["value"]:
        s += f";letter-spacing:{v['letterSpacing']['value']}px"
    if ext.get("textTransform"):
        s += ";text-transform:uppercase"
    return s


def shadow_css(path, mode="light"):
    layers = T[mode][path]["resolved"]
    out = []
    for l in layers:
        c = l["color"]
        r, g, b = (int(c["hex"][i:i + 2], 16) for i in (1, 3, 5))
        out.append(f"{l['offsetX']['value']}px {l['offsetY']['value']}px {l['blur']['value']}px "
                   f"{l['spread']['value']}px rgba({r},{g},{b},{c.get('alpha', 1)})")
    return ", ".join(out)


# ---------------------------------------------------------------- html helpers

def esc(s):
    return html.escape(str(s), quote=False)


def E(tag, style="", *kids, **attrs):
    if (style and "box-sizing" not in style and any(k in style for k in ("width:", "height:"))
            and any(k in style for k in ("padding", "border:"))):
        style += ";box-sizing:border-box"
    a = "".join(f' {k.replace("_", "-")}="{v}"' for k, v in attrs.items())
    s = f' style="{style}"' if style else ""
    return f"<{tag}{s}{a}>" + "".join(kids) + f"</{tag}>"


def D(style, *kids, **attrs):
    return E("div", style, *kids, **attrs)


def S(style, text):
    return E("span", style, esc(text))


ICONS = {
    "plus": '<path d="M8 3.5v9M3.5 8h9"/>',
    "check": '<path d="M3.5 8.5l3 3 6-7"/>',
    "arrow": '<path d="M3.5 8h9M9 4.5L12.5 8 9 11.5"/>',
    "x": '<path d="M4.5 4.5l7 7M11.5 4.5l-7 7"/>',
    "upload": '<path d="M8 10.5V3M5 6l3-3 3 3M3 10.5V13h10v-2.5"/>',
    "image": '<rect x="2.5" y="3.5" width="11" height="9" rx="1.5"/><path d="M2.5 10.5l3-3 3 3 2-2 3 3"/>',
    "spinner": '<circle cx="8" cy="8" r="5.5" opacity="0.3"/><path d="M8 2.5a5.5 5.5 0 0 1 5.5 5.5"/>',
    "question": '<circle cx="8" cy="8" r="5.5"/><path d="M6.6 6.4a1.5 1.5 0 1 1 2.1 1.4c-.5.2-.7.6-.7 1.1M8 11h.01"/>',
    "alert": '<path d="M8 2.8l5.7 10H2.3L8 2.8zM8 6.8v2.6M8 11.2h.01"/>',
    "info": '<circle cx="8" cy="8" r="5.5"/><path d="M8 7.4V11M8 5.2h.01"/>',
    "xcircle": '<circle cx="8" cy="8" r="5.5"/><path d="M6.2 6.2l3.6 3.6M9.8 6.2l-3.6 3.6"/>',
    "checkcircle": '<circle cx="8" cy="8" r="5.5"/><path d="M5.8 8.2l1.5 1.5 3-3.3"/>',
    "chevron": '<path d="M6 4l4 4-4 4"/>',
    "down": '<path d="M4 6l4 4 4-4"/>',
    "dot": '<circle cx="8" cy="8" r="2.5" fill="currentColor" stroke="none"/>',
    "ring": '<circle cx="8" cy="8" r="5" stroke-dasharray="2 2"/>',
    "sliders": '<path d="M3 5h10M3 11h10"/><circle cx="6" cy="5" r="1.6" fill="white"/><circle cx="10" cy="11" r="1.6" fill="white"/>',
}


def icon(name, color="currentColor", size=16, sw=1.5):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 16 16" fill="none" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round" style="flex:none;display:block">{ICONS[name]}</svg>')


# chrome palette (light board)
BG, CARD, SUNK = col("color.surface.base"), col("color.surface.raised"), col("color.surface.sunken")
BORDER, BORDER2 = col("color.border.subtle"), col("color.border.default")
T1, T2, T3 = col("color.text.primary"), col("color.text.secondary"), col("color.text.tertiary")
NEU = col("color.bg.neutral.subtle")
ROOT = f"font-family:{SANS};color:{T1};"


def board(name, title, groups, pad="56px 64px 80px", gap=56):
    body = "\n".join(groups)
    return (f'<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><title>{esc(title)}</title>'
            f'<style>body{{margin:0;background:{BG}}} *{{box-sizing:border-box}}</style></head><body>\n'
            f'<div data-artboard="{name}" style="width:1440px;padding:{pad};display:flex;flex-direction:column;gap:{gap}px;'
            f'background:{BG};color:{T1};font-family:{SANS};box-sizing:border-box">\n{body}\n</div>\n</body></html>\n')


def header(gid, kicker, title, desc, meta):
    left = D("display:flex;flex-direction:column;gap:12px;max-width:760px",
             S(ty("label.sm") + f";color:{T3}", kicker),
             D(ty("headline.md") + f";color:{T1}", esc(title)),
             D(ty("body.md") + f";color:{T2}", esc(desc)))
    right = D("display:flex;gap:32px", *[
        D("display:flex;flex-direction:column;gap:4px", S(ty("label.sm") + f";color:{T3}", k), S(ty("code.sm") + f";color:{T1}", v))
        for k, v in meta])
    return E("section", f"{ROOT}display:flex;justify-content:space-between;align-items:flex-end;gap:48px;padding-bottom:32px;border-bottom:1px solid {BORDER}",
             left, right, data_group=gid)


def section(gid, number, title, desc, *body, gap=24):
    head = D("display:flex;gap:16px;align-items:baseline",
             S(ty("code.sm") + f";color:{T3};width:24px;flex:none", number),
             D("display:flex;flex-direction:column;gap:4px;max-width:800px",
               S(ty("title.sm") + f";color:{T1}", title), S(ty("body.md") + f";color:{T2}", desc)))
    return E("section", f"{ROOT}display:flex;flex-direction:column;gap:{gap}px", head, *body, data_group=gid)


def card(extra, *kids):
    return D(f"background:{CARD};border:1px solid {BORDER};border-radius:12px;padding:24px;{extra}", *kids)


def note(use, avoid, src):
    item = lambda lab, text: D("flex:1;display:flex;flex-direction:column;gap:4px",
                               S(ty("label.sm") + f";color:{T3}", lab), S(ty("body.md") + f";color:{T1}", text))
    return D(f"display:flex;gap:32px;align-items:flex-start;padding:16px 20px;background:{SUNK};border-radius:8px",
             item("Use it for", use), item("Avoid it for", avoid),
             S(ty("code.sm") + f";color:{T3};flex:none;max-width:200px;text-align:right", src))


def mono(text, color=None, style="code.sm"):
    return S(ty(style) + f";color:{color or T2}", text)


def badge_num(n):
    return D(f"width:20px;height:20px;border-radius:9999px;background:{col('color.bg.inverse')};color:{col('color.text.inverse')};"
             f"display:flex;align-items:center;justify-content:center;flex:none;{ty('label.md')}", esc(n))


def chip(text, bg, fg, extra="", icon_name=None):
    kids = ([icon(icon_name, fg, 14)] if icon_name else []) + [S(ty("label.md") + f";color:{fg}", text)]
    return D(f"display:flex;align-items:center;gap:4px;padding:2px 8px;border-radius:9999px;background:{bg};flex:none;{extra}", *kids)


# ---------------------------------------------------------------- shared specimens

SPACE_STEPS = [(k, num(f"space.{k}")) for k in ("025", "050", "075", "100", "150", "200", "250", "300", "400", "500", "600", "800", "1000", "1200")]


def staircase(mode="light", selected=None, gap=16, handle=False, minw=28):
    tc = lambda p: col(p, mode)
    cols = []
    for name, v in SPACE_STEPS:
        sel = name == selected
        fill = tc("color.bg.accent.bold") if sel else tc("color.border.default")
        sq = D(f"width:{v}px;height:{v}px;background:{fill};border-radius:1px;flex:none")
        if sel and handle:
            sq = D("display:flex;align-items:flex-end;gap:3px", sq,
                   D(f"width:4px;height:{min(v, 20)}px;border-radius:2px;background:{tc('color.bg.accent.bold')};opacity:0.55"))
        w = max(v, minw)
        cols.append(D(f"display:flex;flex-direction:column;align-items:center;gap:8px;width:{w + (7 if sel and handle else 0)}px;flex:none",
                      D(f"height:96px;display:flex;align-items:flex-end;justify-content:center;width:100%;border-bottom:1px solid {tc('color.border.strong')}", sq),
                      S(ty("code.sm") + f";color:{tc('color.text.accent') if sel else tc('color.text.tertiary')}", name),
                      S(ty("label.md") + f";color:{tc('color.text.primary')}", f"{v}")))
    return D(f"display:flex;gap:{gap}px;align-items:flex-end", *cols)


def button(variant, state="enabled", size="md", mode="light", label="Button", lead_icon=False):
    tc = lambda p: col(p, mode)
    surface = tc("color.surface.raised")
    fills = {
        "primary": ("color.bg.accent.bold", "color.bg.accent.boldHover", "color.bg.accent.boldPressed", "color.text.onAccent", None),
        "secondary": ("color.bg.neutral.subtle", "color.bg.neutral.subtleHover", "color.bg.neutral.subtlePressed", "color.text.primary", None),
        "outline": (None, "color.bg.neutral.subtle", "color.bg.neutral.subtlePressed", "color.text.primary", "color.border.default"),
        "ghost": (None, "color.bg.neutral.subtle", "color.bg.neutral.subtlePressed", "color.text.primary", None),
        "danger": ("color.bg.danger.bold", "color.bg.danger.boldHover", "color.bg.danger.boldPressed", "color.text.onDanger", None),
    }[variant]
    rest, hover, pressed, fg, border = fills
    bg = {"hover": hover, "pressed": pressed}.get(state, rest)
    fgc = tc(fg)
    shadows = []
    if border:
        shadows.append(f"inset 0 0 0 1px {tc(border)}")
    if state == "disabled":
        bg = "color.bg.disabled" if variant in ("primary", "secondary", "danger") else None
        fgc = tc("color.text.disabled")
        shadows = [f"inset 0 0 0 1px {tc('color.border.subtle')}"] if border else []
    if state == "focus":
        shadows += [f"0 0 0 2px {surface}", f"0 0 0 4px {tc('color.border.focus')}"]
    h = int(num(f"size.control.{size}"))
    padx = {"sm": num("space.inset.md"), "md": num("space.inset.lg"), "lg": num("space.inset.xl")}[size]
    isz = 20 if size == "lg" else 16
    kids = []
    if state == "loading":
        kids.append(icon("spinner", fgc, isz, 2))
    elif lead_icon:
        kids.append(icon("plus", fgc, isz))
    kids.append(S(ty("label.lg") + f";color:{fgc};white-space:nowrap", label))
    style = (f"display:flex;align-items:center;justify-content:center;gap:{num('space.gap.sm')}px;height:{h}px;padding:0 {padx}px;"
             f"border-radius:{num('radius.control')}px;background:{tc(bg) if bg else 'transparent'};flex:none")
    if shadows:
        style += ";box-shadow:" + ", ".join(shadows)
    return D(style, *kids)


def ease_plot(bez, label, token, mode="light"):
    x1, y1, x2, y2 = bez
    P = lambda x, y: f"{8 + x * 104:.1f} {112 - y * 104:.1f}"
    svg = (f'<svg width="120" height="120" viewBox="0 0 120 120" fill="none" style="display:block;flex:none">'
           f'<rect x="8" y="8" width="104" height="104" rx="4" stroke="{BORDER}"/>'
           f'<path d="M{P(0, 0)} L{P(x1, y1)} M{P(1, 1)} L{P(x2, y2)}" stroke="{BORDER2}" stroke-width="1"/>'
           f'<path d="M{P(0, 0)} C{P(x1, y1)} {P(x2, y2)} {P(1, 1)}" stroke="{T1}" stroke-width="2" stroke-linecap="round"/>'
           f'<circle cx="{8 + x1 * 104:.1f}" cy="{112 - y1 * 104:.1f}" r="3" fill="{col("color.bg.accent.bold")}"/>'
           f'<circle cx="{8 + x2 * 104:.1f}" cy="{112 - y2 * 104:.1f}" r="3" fill="{col("color.bg.accent.bold")}"/></svg>')
    return D("display:flex;gap:16px;align-items:center", svg,
             D("display:flex;flex-direction:column;gap:4px;width:176px", S(ty("title.sm"), label), mono(token, T3),
               mono(f"cubic-bezier({x1:g}, {y1:g}, {x2:g}, {y2:g})", T2),
               S(ty("body.sm") + f";color:{T2}", T[mode][token]["$description"])))


# ================================================================= 01 building blocks map

LAYERS = [
    ("L0", "Context and inputs", "Why the system exists, who it serves, where it runs and the brand it carries. Collected first.",
     ["Starting point", "Scope and audience", "UI inventory (audit)", "Target platforms", "Brand personality", "Hard constraints"],
     [("Logo and brand mark", "Q-brand-03"), ("Fixed brand colors", "Q-color-01"), ("Voice and tone guide", "Q-voice-01")], "bounds"),
    ("L1", "Principles", "Tie-breaker statements, UX behavior rules and visual principles, turned into checks.",
     ["Design principles", "UX behavior rules", "Visual principles: hierarchy, grouping, contrast"], [], "constrain"),
    ("L2", "Foundations", "The visual raw material. Generatable blocks are edited on a live preview; assets come from people.",
     ["Color", "Typography", "Space and density", "Layout", "Interaction and input", "Shape and borders",
      "Elevation and materials", "Motion", "Sound and haptics", "Iconography", "Imagery", "Data visualization"],
     [("Brand typeface", "Q-type-02"), ("Custom icon set", "Q-icon-01"), ("App icon", "Q-icon-06"), ("Photography", "Q-img-01"),
      ("Illustration or mascot", "Q-img-04"), ("Animated assets", "Q-img-06"), ("UI sounds, sonic logo", "Q-motion-08")], "are stored as"),
    ("L3", "Tokens", "Foundations as named, portable values: primitives, semantic roles, optional component tokens, and modes.",
     ["Primitives", "Semantic roles", "Component tokens (optional)", "Modes and themes (resolver)", "Naming and code syntax", "DTCG 2025.10 files"], [], "style"),
    ("L4", "Components", "Reusable parts with anatomy, variants, states and props.",
     ["Actions", "Inputs", "Selection", "Navigation", "Feedback", "Overlays", "Containment", "Data display", "Media", "Layout"], [], "compose into"),
    ("L5", "Patterns and templates", "Recurring solutions assembled from components.",
     ["Forms and validation", "Navigation", "Search and filtering", "Onboarding", "Empty, loading and error", "Notifications",
      "Authentication", "Data tables", "Settings", "Destructive confirmations", "Progressive disclosure"], [], "are all checked by"),
    ("L6", "Guardrails and validation", "Checks that run on every edit, not after the fact.",
     ["Contrast pairs, WCAG 2.2 AA", "Token-only styling and scopes", "Hierarchy lint", "Target sizes", "Reduced motion", "Coverage: nothing missed"], [], "ship through"),
    ("L7", "Delivery and tooling", "How the system reaches code, design tools and agents.",
     ["DTCG + resolver export", "CSS, Swift, Compose", "Figma variables and components", "Paper tokens and artboards", "Docs site", "Agent manifest (MCP)"], [], "are run over time by"),
    ("L8", "Governance, docs and adoption", "How the system is maintained as products change.",
     ["Contribution model", "Versioning and deprecation", "Component docs template", "Adoption metrics", "Team model"], [], None),
]

HOOKS = [
    ("Logo and brand mark", "Q-brand-03", "Logo component, favicon set, app icon", "SVG (preferred), PDF or EPS, PNG 512px+; light, dark, mono",
     "Commission a designer (recommended) · placeholder wordmark in the chosen typeface · logo tool, may not be ownable"),
    ("Fixed brand colors", "Q-color-01", "Accent ramp, semantic roles", "Hex, RGB or OKLCH values, brand book PDF, a reference",
     "Seed suggested from the personality sliders, labelled a starting point"),
    ("Voice and tone guide", "Q-voice-01", "Microcopy, errors, empty states", "An existing guide, or 3-4 traits in 'X, but not Y' form",
     "The builder drafts copy examples from the traits"),
    ("Brand typeface", "Q-type-02", "Type scale, every text style", "WOFF2 for web, OTF or TTF for apps; variable preferred; license",
     "Open-source face under SIL OFL · license a commercial face · commission a custom face (slow, costly)"),
    ("Custom icon set", "Q-icon-01", "Icon sizes, buttons, navigation", "One SVG per icon on a 16 or 24px master, or a Figma icon library",
     "Adopt an open-source set (default) · commission domain icons only · AI icons as sketches"),
    ("App icon", "Q-icon-06", "Home screen, stores, PWA", "Layered SVG or PNG at 1024px; Android adaptive layers; maskable 512px",
     "Placeholder from the logo glyph · commission a designer for a shipped app"),
    ("Photography", "Q-img-01", "Heroes, cards, empty states", "JPEG, WebP or AVIF plus a written brief",
     "Builder drafts the brief · commission a photographer · licensed stock · AI for placeholders only"),
    ("Illustration or mascot", "Q-img-04", "Empty states, onboarding", "SVG (preferred), PNG at 2x, Lottie JSON",
     "Icon-plus-text empty states · commission an illustrator · AI drafts only"),
    ("Animated assets", "Q-img-06", "Celebration, onboarding moments", "Lottie or dotLottie, animated SVG, GLB or USDZ",
     "Built-in symbol animation · commission a motion designer"),
    ("UI sounds, sonic logo", "Q-motion-08", "Earcons on mobile or spatial", "WAV master plus AAC or CAF",
     "Stay silent (the norm on web) · system sounds · commission a sound designer"),
]


def gen_chip(text):
    return D(f"padding:8px 12px;background:{NEU};border-radius:{num('radius.control')}px;flex:none", S(ty("body.md") + f";color:{T1}", text))


def hook_chip(text, qid):
    return D(f"display:flex;align-items:center;gap:10px;padding:7px 12px 7px 10px;border:1px dashed {col('color.border.strong')};"
             f"border-radius:8px;flex:none",
             icon("question", T2, 18),
             D("display:flex;flex-direction:column", S(ty("body.md") + f";color:{T1}", text),
               S(ty("body.sm") + f";color:{T3}", f"Do you have this? · {qid}")))


def building_blocks_map():
    legend = D("display:flex;gap:24px;align-items:center;padding-left:40px",
               D("display:flex;gap:8px;align-items:center", gen_chip("Block"), S(ty("body.md") + f";color:{T2}", "Generated and edited visually in the builder")),
               D("display:flex;gap:8px;align-items:center",
                 D(f"display:flex;align-items:center;gap:8px;padding:8px 12px 8px 10px;border:1px dashed {col('color.border.strong')};border-radius:8px",
                   icon("question", T2, 18), S(ty("body.md") + f";color:{T1}", "Hook")),
                 S(ty("body.md") + f";color:{T2}", "Designer-owned: the builder asks, accepts the file, offers paths if the answer is no")))
    rows = []
    for i, (lid, name, desc, gens, hooks, verb) in enumerate(LAYERS):
        left = D("width:300px;flex:none;display:flex;flex-direction:column;gap:6px",
                 D("display:flex;gap:10px;align-items:baseline", mono(lid, T3), S(ty("title.sm") + f";color:{T1}", name)),
                 S(ty("body.md") + f";color:{T2};padding-left:30px", desc))
        right_rows = [D("display:flex;flex-wrap:wrap;gap:8px;align-items:center", *[gen_chip(g) for g in gens])]
        if hooks:
            right_rows.append(D(f"display:flex;gap:8px;align-items:flex-start;padding-top:12px;border-top:1px solid {BORDER}",
                                D("width:72px;flex:none;padding-top:16px", S(ty("label.sm") + f";color:{T3}", "Asks for")),
                                D("flex:1;display:flex;flex-wrap:wrap;gap:8px", *[hook_chip(h, q) for h, q in hooks])))
        right = D("flex:1;display:flex;flex-direction:column;gap:12px", *right_rows)
        rows.append(card("display:flex;gap:32px;align-items:flex-start;padding:20px 24px", left, right))
        if verb:
            rows.append(D("display:flex;align-items:center;gap:12px;height:36px;padding-left:40px",
                          D(f"width:1px;height:36px;background:{BORDER2}"), icon("down", T3, 14), mono(verb, T3)))
    return section("01.2-layers", "01", "The stack of decisions",
                   "Nine layers, top to bottom. Each layer bounds the one below it, and every block is either generated or asked for. Nothing is silently skipped: coverage is checked against this map.",
                   legend, D("display:flex;flex-direction:column", *rows), gap=20)


def hooks_table():
    head = D(f"display:flex;gap:24px;padding:0 20px 12px;border-bottom:1px solid {BORDER}",
             *[S(ty("label.sm") + f";color:{T3};{w}", t) for t, w in
               (("Hook", "width:220px;flex:none"), ("Feeds", "width:220px;flex:none"), ("Accepts", "width:320px;flex:none"), ("If the answer is no", "flex:1"))])
    rows = []
    for i, (name, qid, feeds, accepts, paths) in enumerate(HOOKS):
        line = f"border-bottom:1px solid {BORDER};" if i < len(HOOKS) - 1 else ""
        rows.append(D(f"display:flex;gap:24px;padding:14px 20px;{line}align-items:flex-start",
                      D("width:220px;flex:none;display:flex;gap:10px;align-items:flex-start", icon("question", T2, 18),
                        D("display:flex;flex-direction:column;gap:2px", S(ty("title.sm"), name), mono(qid, T3))),
                      S(ty("body.md") + f";color:{T2};width:220px;flex:none", feeds),
                      S(ty("body.md") + f";color:{T1};width:320px;flex:none", accepts),
                      S(ty("body.md") + f";color:{T2};flex:1", paths)))
    return section("01.3-hooks", "02", "Designer hooks: “Do you have this?”",
                   "Ten blocks a generator should not invent. For each, the builder asks, names the formats it accepts, and offers honest paths when the answer is no. In Quick mode the fallback is applied and the asset tray stays open.",
                   card("padding:12px 0 4px", head, *rows))


def board_01():
    return board("01-building-blocks-map", "Building blocks map", [
        header("01.1-header", "Atlas 01 · Building blocks", "What a design system is made of",
               "Every design system is the same stack of decisions, from context down to governance. The builder walks it top to bottom, generates what it can, and asks for what only a person can provide.",
               [("Layers", "9"), ("Hooks", "10"), ("Source", "synthesis/ontology.json")]),
        building_blocks_map(),
        hooks_table(),
    ])


# ================================================================= 02 foundations

HUE_ORDER = ["neutral", "accent", "success", "warning", "danger", "info"]


def ramp_panel(mode):
    tc = lambda p: col(p, mode)
    bg = tc("color.surface.raised") if mode == "light" else tc("color.surface.base")
    t1, t2, t3 = tc("color.text.primary"), tc("color.text.secondary"), tc("color.text.tertiary")
    ring = tc("color.shadow.soft") if mode == "light" else "rgba(255,255,255,0.06)"
    lab = lambda s: D("width:72px;flex:none", S(ty("code.sm") + f";color:{t2}", s))
    head = D("display:flex;gap:2px;align-items:center", lab(""),
             *[D("flex:1;text-align:center", S(ty("code.sm") + f";color:{t3}", str(i))) for i in range(1, 13)])
    rows = [head]
    for hue in HUE_ORDER:
        rows.append(D("display:flex;gap:2px;align-items:center", lab(hue),
                      *[D(f"flex:1;height:40px;border-radius:4px;background:{col(f'color.{hue}.{mode}.{i}', mode)};box-shadow:inset 0 0 0 1px {ring}")
                        for i in range(1, 13)]))
    bands = [("Backgrounds", 2), ("Component fills", 3), ("Borders", 3), ("Solid", 2), ("Text", 2)]
    rows.append(D("display:flex;gap:2px;margin-top:4px", lab(""),
                  *[D(f"flex:{w};margin:0 1px;padding-top:6px;border-top:2px solid {tc('color.border.default')}", S(ty("body.sm") + f";color:{t2}", b))
                    for b, w in bands]))
    base = "#ffffff" if mode == "light" else hx("color.neutral.dark.1", "dark")
    vals = [contrast(hx(f"color.neutral.{mode}.{i}", mode), base) for i in range(1, 13)]
    rows.append(D("display:flex;gap:2px;align-items:center;margin-top:4px",
                  lab("vs white" if mode == "light" else "vs step 1"),
                  *[D("flex:1;text-align:center", S(ty("code.sm") + f";color:{t3}", f"{v:.1f}" if v < 10 else f"{v:.0f}")) for v in vals]))
    title = D("display:flex;justify-content:space-between;align-items:baseline",
              S(ty("title.sm") + f";color:{t1}", "Light ramps" if mode == "light" else "Dark ramps"),
              S(ty("code.sm") + f";color:{t3}", f"color.{{hue}}.{mode}.{{1-12}}"))
    return D(f"flex:1;background:{bg};border:1px solid {tc('color.border.subtle')};border-radius:12px;padding:24px;display:flex;flex-direction:column;gap:10px",
             title, *rows)


def color_ramps():
    return section("02.2-ramps", "01", "Color ramps",
                   "Six hues, 12 steps each, built in OKLCH. Every step has a fixed job, and every hue hits the same contrast at the same step, so swapping the accent never breaks a pairing. Dark mode uses its own ramps.",
                   D("display:flex;gap:24px", ramp_panel("light"), ramp_panel("dark")),
                   note("Semantic tokens only. Components read color.text.primary, never color.neutral.light.12.",
                        "Picking a step by eye, or inverting a light ramp to get dark mode.",
                        "DC-L01-01 · 02 · 03 · 18 · L09 A1.4"))


def semantic_panel(mode):
    tc = lambda p: col(p, mode)
    t1, t3 = tc("color.text.primary"), tc("color.text.tertiary")
    surf = []
    for name, extra in (("sunken", ""), ("base", f"border:1px solid {tc('color.border.subtle')}"),
                        ("raised", f"border:1px solid {tc('color.border.subtle')};box-shadow:{shadow_css('elevation.shadow.raised', mode)}"),
                        ("overlay", f"box-shadow:{shadow_css('elevation.shadow.overlay', mode)}")):
        surf.append(D(f"flex:1;height:76px;border-radius:10px;background:{tc('color.surface.' + name)};padding:12px;display:flex;flex-direction:column;justify-content:space-between;{extra}",
                      S(ty("title.sm") + f";color:{t1}", name.title()), S(ty("code.sm") + f";color:{t3}", f"surface.{name}")))
    texts = []
    for tok, label in (("primary", "Primary text"), ("secondary", "Secondary text"), ("tertiary", "Tertiary, placeholder"),
                       ("accent", "Link text"), ("disabled", "Disabled")):
        r = ratio(f"color.text.{tok}", "color.surface.raised", mode)
        texts.append(D("display:flex;align-items:center;gap:12px",
                       D("flex:1;display:flex;flex-direction:column",
                         S(ty("body.md") + f";color:{tc('color.text.' + tok)}", label),
                         S(ty("code.sm") + f";color:{t3}", f"text.{tok}")),
                       S(ty("code.sm") + f";color:{tc('color.text.secondary')};text-align:right", "exempt" if tok == "disabled" else f"{r:.1f}:1")))
    text_card = D(f"flex:1;background:{tc('color.surface.raised')};border:1px solid {tc('color.border.subtle')};border-radius:10px;padding:16px;display:flex;flex-direction:column;gap:10px",
                  *texts)
    sts = []
    for s, ic in (("success", "checkcircle"), ("warning", "alert"), ("danger", "xcircle"), ("info", "info")):
        sts.append(D(f"display:flex;align-items:center;gap:6px;padding:4px 10px 4px 8px;border-radius:6px;background:{tc(f'color.bg.{s}.subtle')}",
                     icon(ic, tc(f"color.text.{s}"), 16), S(ty("label.md") + f";color:{tc(f'color.text.{s}')}", s.title())))
    fills = D("display:flex;flex-direction:column;gap:12px;flex:1",
              D("display:flex;gap:8px;flex-wrap:wrap", button("primary", mode=mode, label="Primary", size="sm"),
                button("secondary", mode=mode, label="Secondary", size="sm"),
                D(f"display:flex;align-items:center;height:32px;padding:0 12px;border-radius:6px;background:{tc('color.bg.inverse')}",
                  S(ty("label.lg") + f";color:{tc('color.text.inverse')}", "Inverse"))),
              D("display:flex;gap:6px;flex-wrap:wrap", *sts),
              D("display:flex;gap:8px", *[
                  D("display:flex;flex-direction:column;gap:6px;align-items:center",
                    D(f"width:56px;height:32px;border-radius:6px;background:{tc('color.surface.raised')};border:{2 if b == 'focus' else 1}px solid {tc('color.border.' + b)}"),
                    S(ty("code.sm") + f";color:{t3}", b)) for b in ("subtle", "default", "strong", "focus")]))
    return D(f"flex:1;background:{tc('color.surface.base')};border:1px solid {tc('color.border.subtle')};border-radius:12px;padding:24px;display:flex;flex-direction:column;gap:20px",
             D("display:flex;justify-content:space-between;align-items:baseline", S(ty("title.sm") + f";color:{t1}", mode.title()),
               S(ty("code.sm") + f";color:{t3}", f"color.{mode}.tokens.json")),
             D("display:flex;gap:12px", *surf), D("display:flex;gap:20px", text_card, fills))


def semantic_roles():
    return section("02.3-semantic", "02", "Semantic roles in light and dark",
                   "Same names, different values per mode. Ratios are measured against surface.raised; all 126 text and non-text pairs pass WCAG 2.2 AA in both modes (check_contrast.py).",
                   D("display:flex;gap:24px", semantic_panel("light"), semantic_panel("dark")),
                   note("Pairing each text token with the surfaces it may sit on; the builder tests every pair in every mode.",
                        "Hex values in components, and conveying status by color alone (always add an icon or label).",
                        "DC-L01-11 · 13 · 14 · 15 · 16 · 22 · 23"))


SPECIMEN = {
    "display": "Decisions, made visible", "headline": "Spacing sets the rhythm", "title": "Card and panel titles",
    "body": "Body text carries most of the interface, so it is tuned for reading at length.",
    "label": "Save changes", "code": "space.inset.lg = 16px",
}


def type_scale():
    rows = []
    for tok_path, tok in T["light"].items():
        if not tok_path.startswith("text.") or tok["$type"] != "typography":
            continue
        name = tok_path[5:]
        v, ext = tok["resolved"], tok["$extensions"][NS]
        meta = f"{v['fontSize']['value']}/{ext['lineHeightPx']} · {v['fontWeight']}" + (f" · {ext['letterSpacingEm']:+}em" if ext["letterSpacingEm"] else "")
        spec = SPECIMEN[name.split(".")[0]]
        if name == "label.sm":
            spec = "Overline label"
        rows.append(D(f"display:flex;gap:32px;align-items:center;padding:16px 0;border-bottom:1px solid {BORDER}",
                      D("width:200px;flex:none;display:flex;flex-direction:column;gap:2px", mono(f"text.{name}", T1), mono(meta, T3)),
                      D(ty(name) + f";flex:1;color:{T1};white-space:nowrap;overflow:hidden", esc(spec)),
                      D("width:360px;flex:none;display:flex;flex-direction:column;gap:2px",
                        S(ty("body.sm") + f";color:{T2}", "Use: " + ext["use"]), S(ty("body.sm") + f";color:{T3}", "Avoid: " + ext["avoid"]))))
    return section("02.4-type", "03", "Type scale",
                   "Inter and JetBrains Mono. Nine sizes from a 14px base at a ratio of about 1.2, rounded to even pixels; line heights snap to 4px. Fifteen named styles, three weights.",
                   card("padding:8px 24px", *rows),
                   note("14px body for controls and tables, 16px where people read paragraphs; one display line per page.",
                        "Text people must read below 12px, and light weights for body.",
                        "DC-L02-08 · 09 · 10 · 13 · 15 · L09 A1.8"))


def spacing_block():
    sem = []
    for fam in ("inset", "gap"):
        for s in ("xs", "sm", "md", "lg", "xl"):
            p = f"space.{fam}.{s}"
            sem.append(D(f"display:flex;gap:16px;align-items:baseline;padding:8px 0;border-bottom:1px solid {BORDER}",
                         D("width:120px;flex:none", mono(p, T1)),
                         S(ty("label.md") + f";width:96px;flex:none;text-align:right;color:{T1}", f"{num(p):g}"),
                         S(ty("label.md") + f";width:72px;flex:none;text-align:right;color:{T3}", f"{num(p, TC):g}"),
                         S(ty("body.sm") + f";color:{T2};flex:1", T["light"][p]["$description"])))
    lab = lambda t, w: S(ty("label.sm") + f";color:{T3};{w}", t)
    sem_head = D(f"display:flex;gap:16px;padding-bottom:8px;border-bottom:1px solid {BORDER}",
                 lab("Token", "width:120px"), lab("Comfortable", "width:96px;text-align:right"),
                 lab("Compact", "width:72px;text-align:right"), lab("Job", "flex:1"))
    pad_t, gap_t = col("color.accent.light.4"), col("color.warning.light.4")
    strip = lambda: D(f"height:12px;background:{gap_t}")
    inner = D(f"background:{CARD};display:flex;flex-direction:column",
              S(ty("title.sm"), "Invite teammates"), strip(),
              S(ty("body.sm") + f";color:{T2}", "People you invite can edit tokens and components."), strip(),
              D(f"height:40px;padding:0 12px;border-radius:6px;border:1px solid {col('color.border.strong')};display:flex;align-items:center",
                S(ty("body.md") + f";color:{T3}", "name@company.com")), strip(),
              D("display:flex;justify-content:flex-end;gap:8px", button("ghost", size="sm", label="Cancel"), button("primary", size="sm", label="Send invite")))
    demo = D(f"border:1px solid {BORDER};border-radius:12px;overflow:hidden;width:360px;flex:none;box-shadow:{shadow_css('elevation.shadow.raised')}",
             D(f"padding:16px;background:{pad_t}", inner))
    legend = D("display:flex;flex-direction:column;gap:6px", *[
        D("display:flex;gap:8px;align-items:center", D(f"width:12px;height:12px;border-radius:2px;background:{c}"),
          mono(t, T1), S(ty("body.sm") + f";color:{T2}", d)) for c, t, d in
        ((pad_t, "space.inset.lg · 16", "padding, owned by the card"), (gap_t, "space.gap.md · 12", "gaps between children"))])
    rules = D(f"width:300px;flex:none;border-left:1px solid {BORDER};padding-left:24px;display:flex;flex-direction:column;gap:12px", *[
        D("display:flex;flex-direction:column;gap:2px", S(ty("title.sm"), t), S(ty("body.sm") + f";color:{T2}", d)) for t, d in (
            ("4px grid, 8px rhythm", "Every value is a multiple of 4; names count in 8s (DC-L03-01)."),
            ("Names are percent of 8px", "space.100 = 8px, space.050 = 4px; no padding or margin in a name (DC-L03-03)."),
            ("Steps you can tell apart", "Above 8px, each step is at least 25% larger than the last (DC-L03-02)."),
            ("Small steps stay inside", "2, 4 and 6px are for component internals only (DC-L03-06)."))])
    return section("02.5-spacing", "04", "Spacing",
                   "A 4px grid with an 8px rhythm, shown at 1:1. Semantic tokens say what the space is for; the compact density moves each one down a step, while primitives and target sizes stay fixed.",
                   card("display:flex;gap:32px;align-items:stretch",
                        D("flex:1;display:flex;flex-direction:column;justify-content:space-between;gap:24px",
                          D("display:flex;justify-content:space-between;align-items:baseline", S(ty("title.sm"), "Scale · space.{name}"), mono("actual pixels", T3)),
                          staircase("light")), rules),
                   D("display:flex;gap:24px;align-items:flex-start",
                     card("flex:1;display:flex;flex-direction:column", sem_head, *sem),
                     D("display:flex;flex-direction:column;gap:16px", demo, legend)),
                   note("2, 4 and 6px inside components; inset for padding, gap between siblings, layout tokens between sections.",
                        "Sub-8px steps between sections, and margins on reusable components.",
                        "DC-L03-01 · 02 · 03 · 04 · 10 · 24 · L09 A1.2"))


def radius_block():
    tiles = []
    for v in ("0", "2", "4", "6", "8", "12", "16", "24", "full"):
        r = num(f"radius.{v}")
        tiles.append(D("display:flex;flex-direction:column;gap:8px;align-items:center",
                       D(f"width:72px;height:72px;background:{NEU};border:1px solid {BORDER2};border-radius:{min(r, 36):g}px"),
                       mono(f"radius.{v}", T1), mono("9999" if v == "full" else f"{r:g}px", T3)))
    strong = col("color.border.strong")
    roles = [
        ("detail", "Checkboxes, tags", D(f"width:20px;height:20px;border:1px solid {strong};border-radius:{num('radius.detail'):g}px;background:{CARD}")),
        ("control", "Buttons, inputs", button("secondary", label="Button", size="sm")),
        ("container", "Cards, panels", D(f"width:136px;height:72px;border:1px solid {BORDER};border-radius:{num('radius.container'):g}px;background:{CARD};box-shadow:{shadow_css('elevation.shadow.raised')}")),
        ("overlay", "Dialogs, popovers", D(f"width:152px;height:84px;border-radius:{num('radius.overlay'):g}px;background:{CARD};box-shadow:{shadow_css('elevation.shadow.overlay')}")),
        ("full", "People, pills", D(f"width:36px;height:36px;border-radius:9999px;background:{col('color.bg.accent.subtle')};display:flex;align-items:center;justify-content:center",
                                    S(ty("label.md") + f";color:{col('color.text.accent')}", "KB"))),
    ]
    role_row = D("display:flex;justify-content:space-between", *[
        D("display:flex;flex-direction:column;gap:8px;align-items:flex-start",
          D("height:92px;display:flex;align-items:flex-end;padding-left:4px", el), mono(f"radius.{n}", T1),
          S(ty("body.sm") + f";color:{T2}", f"{num('radius.' + n):g}px · {d}" if n != "full" else d)) for n, d, el in roles])
    borders = D("display:flex;gap:40px;align-items:flex-end", *[
        D("display:flex;flex-direction:column;gap:8px", D(f"width:120px;height:{w}px;background:{T1}"), mono(f"border.width.{w}", T2)) for w in (1, 2, 4)],
        D("display:flex;flex-direction:column;gap:12px;align-items:flex-start", button("primary", "focus", "sm", label="Focused"),
          mono("focus.ring.width 2 · offset 2 · border.focus", T2)))
    return section("02.6-radius", "05", "Radius, borders and focus",
                   "Nine radius steps with a 6px control default (the median across 22 systems). Radius grows with the element; nested corners use outer radius minus padding.",
                   card("display:flex;flex-direction:column;gap:32px", D("display:flex;justify-content:space-between", *tiles),
                        D(f"height:1px;background:{BORDER}"), role_row, D(f"height:1px;background:{BORDER}"), borders),
                   note("control for buttons and inputs, container for cards, overlay for dialogs, full for people and pills.",
                        "The same radius on a small badge and a large dialog, and equal radii on nested elements.",
                        "DC-L04-01 · 03 · 05 · 07 · 09 · L09 A1.7"))


def elevation_panel(mode):
    tc = lambda p: col(p, mode)
    tiles = []
    for lvl, extra, recipe in (("sunken", "", ""), ("base", f"border:1px solid {tc('color.border.subtle')}", ""),
                               ("raised", f"border:1px solid {tc('color.border.subtle')};box-shadow:{shadow_css('elevation.shadow.raised', mode)}", "shadow.raised"),
                               ("overlay", f"box-shadow:{shadow_css('elevation.shadow.overlay', mode)}", "shadow.overlay")):
        tiles.append(D(f"flex:1;height:112px;border-radius:12px;background:{tc('color.surface.' + lvl)};padding:14px;display:flex;flex-direction:column;justify-content:space-between;{extra}",
                       S(ty("title.sm") + f";color:{tc('color.text.primary')}", lvl.title()),
                       D("display:flex;flex-direction:column", S(ty("code.sm") + f";color:{tc('color.text.tertiary')}", f"surface.{lvl}"),
                         S(ty("code.sm") + f";color:{tc('color.text.tertiary')}", recipe) if recipe else "")))
    return D(f"flex:1;background:{tc('color.surface.base')};border:1px solid {tc('color.border.subtle')};border-radius:12px;padding:24px;display:flex;flex-direction:column;gap:16px",
             S(ty("title.sm") + f";color:{tc('color.text.primary')}", mode.title()), D("display:flex;gap:16px", *tiles))


def elevation_block():
    return section("02.7-elevation", "06", "Elevation",
                   "Four levels. In-page containers stay flat with a hairline; only floating things cast shadows. In dark mode higher surfaces get lighter, shadow alpha doubles and overlays gain a 1px edge ring.",
                   D("display:flex;gap:24px", elevation_panel("light"), elevation_panel("dark")),
                   note("Shadows on menus, popovers, dialogs and dragged items.",
                        "Shadows on static in-page cards where a border or tone step would do.",
                        "DC-L04-10 · 11 · 12 · 13 · L09 A1.12"))


def motion_block():
    bars = []
    for n in ("micro", "short", "medium", "long", "xlong"):
        p = f"motion.duration.{n}"
        ms = T["light"][p]["resolved"]["value"]
        bars.append(D("display:flex;gap:16px;align-items:center",
                      D("width:200px;flex:none", mono(p, T1)), S(ty("label.md") + f";width:56px;flex:none;text-align:right;color:{T1}", f"{ms}ms"),
                      D(f"height:8px;width:{ms}px;border-radius:4px;background:{T1};flex:none"),
                      S(ty("body.sm") + f";color:{T2}", T["light"][p]["$description"])))
    plots = [ease_plot(T["light"][f"motion.easing.{e}"]["resolved"], e.title(), f"motion.easing.{e}") for e in ("standard", "enter", "exit", "linear")]
    trans = []
    for tname in ("feedback", "enter", "exit"):
        std = resolve("light", "comfortable", "standard")[f"motion.transition.{tname}"]["resolved"]
        red = resolve("light", "comfortable", "reduced")[f"motion.transition.{tname}"]["resolved"]
        fmt = lambda r: f"{r['duration']['value']}ms · cubic-bezier({', '.join(f'{x:g}' for x in r['timingFunction'])})"
        trans.append(D(f"display:flex;gap:16px;padding:8px 0;border-bottom:1px solid {BORDER}",
                       D("width:200px;flex:none", mono(f"motion.transition.{tname}", T1)),
                       S(ty("code.sm") + f";color:{T1};width:300px;flex:none", fmt(std)),
                       S(ty("code.sm") + f";color:{T2};flex:1", fmt(red))))
    return section("02.8-motion", "07", "Motion",
                   "Durations stay in the 100-300ms band; exits run about 25% shorter than entrances. Four curves. Reduced motion is a token mode: it keeps fades and drops travel.",
                   card("display:flex;flex-direction:column;gap:14px", S(ty("title.sm"), "Durations"), *bars),
                   card("display:flex;justify-content:space-between", *plots),
                   card("display:flex;flex-direction:column",
                        D(f"display:flex;gap:16px;padding-bottom:8px;border-bottom:1px solid {BORDER}",
                          S(ty("label.sm") + f";color:{T3};width:200px", "Transition"), S(ty("label.sm") + f";color:{T3};width:300px", "Standard"),
                          S(ty("label.sm") + f";color:{T3}", "Reduced motion")), *trans),
                   note("Feedback and state changes people need to notice; ease-out curves for anything entering.",
                        "Motion over 300ms on repeated UI, linear easing except spinners, and travel when reduced motion is on.",
                        "DC-L04-20 · 21 · 24 · 25 · L09 A1.5"))


def board_02():
    return board("02-foundations", "Foundations", [
        header("02.1-header", "Atlas 02 · Foundations", "Starter foundations",
               "The values behind every token file in design/tokens, shown the way the builder teaches them: what each block is, where to use it, and where not to.",
               [("Format", "DTCG 2025.10"), ("Modes", "light · dark"), ("Contrast", "126/126 AA")]),
        color_ramps(), semantic_roles(), type_scale(), spacing_block(), radius_block(), elevation_block(), motion_block(),
    ])


# ================================================================= 03 button

VARIANTS = [("primary", "Save changes"), ("secondary", "Preview"), ("outline", "Export"), ("ghost", "Cancel"), ("danger", "Delete file")]
STATES = [("enabled", "Enabled"), ("hover", "Hover"), ("focus", "Focus-visible"), ("pressed", "Pressed"), ("disabled", "Disabled"), ("loading", "Loading")]


def anatomy():
    acc, on = col("color.bg.accent.bold"), col("color.text.onAccent")
    k = 3  # drawing scale
    pad, isz, gap, lab_w = num("space.inset.lg") * k, num("size.icon.sm") * k, num("space.gap.sm") * k, 188
    h = num("size.control.md") * k
    guide = "rgba(255,255,255,0.24)"
    segs = [(pad, "5", "16", True), (isz, "2", "16", False), (gap, "3", "8", True), (lab_w, "4", "label", False), (pad, "5", "16", True)]
    markers = D("display:flex", *[D(f"width:{w:g}px;flex:none;display:flex;justify-content:center", badge_num(n)) for w, n, _, _ in segs])
    parts_x = []
    for w, n, _, is_guide in segs:
        if n == "2":
            parts_x.append(D(f"width:{w:g}px;height:{h:g}px;flex:none;display:flex;align-items:center;justify-content:center", icon("plus", on, int(w), 1.5)))
        elif n == "4":
            parts_x.append(D(f"width:{w:g}px;flex:none;font-size:42px;line-height:60px;font-weight:500;color:{on};text-align:center", "Create"))
        else:
            parts_x.append(D(f"width:{w:g}px;height:{h:g}px;flex:none;background:{guide}"))
    big = D(f"display:flex;align-items:center;height:{h:g}px;border-radius:{num('radius.control') * k:g}px;background:{acc};overflow:hidden;flex:none", *parts_x)
    vdim = D("display:flex;align-items:center;gap:8px",
             D(f"width:1px;height:{h:g}px;background:{T3}"), D("display:flex;flex-direction:column;gap:6px", badge_num("1"), mono("40", T2)))
    dims = D("display:flex", *[D(f"width:{w:g}px;flex:none;display:flex;flex-direction:column;align-items:center;gap:4px",
                                 D(f"width:100%;height:1px;background:{T3}"), mono(t, T2)) for w, _, t, _ in segs])
    small = D("display:flex;gap:40px;align-items:center;padding-top:8px",
              D("display:flex;gap:12px;align-items:center", button("primary", "focus", label="Create"), badge_num("6"), mono("focus-visible", T3)),
              D("display:flex;gap:12px;align-items:center", button("primary", "loading", label="Create"), badge_num("7"), mono("loading", T3)))
    parts = [
        ("1", "Container", "color.bg.accent.bold · radius.control 6 · size.control.md 40"),
        ("2", "Leading icon, optional", "size.icon.sm 16 · inherits the label color"),
        ("3", "Gap", "space.gap.sm 8"),
        ("4", "Label", "text.label.lg 14/20 · 500 · color.text.onAccent"),
        ("5", "Padding inline", "space.inset.lg 16 (sm: inset.md 12, lg: inset.xl 24)"),
        ("6", "Focus ring", "border.focus · 2px ring · 2px offset, keyboard focus only"),
        ("7", "Spinner", "replaces the icon; label and width stay"),
    ]
    plist = D("display:flex;flex-direction:column;gap:14px;flex:1", *[
        D("display:flex;gap:12px;align-items:flex-start", badge_num(n),
          D("display:flex;flex-direction:column;gap:2px", S(ty("title.sm"), t), mono(tok, T2))) for n, t, tok in parts])
    return section("03.2-anatomy", "01", "Anatomy",
                   "Drawn at 3x. Height is a 20px line box plus block padding, so every size stays on the 8px ladder; the tinted bands are padding and gap.",
                   card("display:flex;gap:64px;align-items:center;padding:40px",
                        D("display:flex;flex-direction:column;gap:10px;align-items:flex-start", mono("button · primary · md · 3x", T3),
                          markers, D("display:flex;gap:16px;align-items:center", big, vdim), dims, small),
                        plist))


def matrix(mode):
    tc = lambda p: col(p, mode)
    head = D("display:flex;gap:16px;align-items:center", D("width:112px;flex:none"),
             *[D("flex:1", S(ty("label.sm") + f";color:{tc('color.text.tertiary')}", s)) for _, s in STATES])
    rows = [head]
    for v, lab in VARIANTS:
        rows.append(D("display:flex;gap:16px;align-items:center",
                      D("width:112px;flex:none", S(ty("title.sm") + f";color:{tc('color.text.primary')}", v.title())),
                      *[D("flex:1;display:flex", button(v, s, mode=mode, label=lab)) for s, _ in STATES]))
    return D(f"background:{tc('color.surface.raised')};border:1px solid {tc('color.border.subtle')};border-radius:12px;padding:28px;display:flex;flex-direction:column;gap:20px",
             D("display:flex;justify-content:space-between", S(ty("title.sm") + f";color:{tc('color.text.primary')}", f"{mode.title()} · md"),
               S(ty("code.sm") + f";color:{tc('color.text.tertiary')}", "Variant × State")), *rows)


def matrices():
    return section("03.3-matrix", "02", "Variants and states",
                   "Five variants by six states, in both modes. Hover is one ramp step, pressed two. Focus-visible draws a 2px ring with a 2px gap. Loading keeps the label and the width.",
                   matrix("light"), matrix("dark"), gap=20)


def sizes():
    cols = []
    for sz in ("sm", "md", "lg"):
        h = num(f"size.control.{sz}")
        pad = {"sm": "inset.md", "md": "inset.lg", "lg": "inset.xl"}[sz]
        cols.append(D("display:flex;flex-direction:column;gap:16px;flex:1",
                      D("display:flex;gap:12px;align-items:center;height:48px", button("primary", size=sz, label="Save changes", lead_icon=True),
                        button("secondary", size=sz, label="Preview")),
                      D("display:flex;flex-direction:column;gap:2px", S(ty("title.sm"), f"{sz} · {h:g}px"),
                        mono(f"size.control.{sz} · space.{pad} · icon {20 if sz == 'lg' else 16}", T2))))
    return section("03.4-sizes", "03", "Sizes",
                   "Three heights shared with inputs and selects. Never mix sizes in one group. The visual height can drop to 32px, but the hit area never drops below 24px, or 44px on touch.",
                   card("display:flex;gap:40px", *cols))


def token_map():
    rows_def = [("Fill · rest", 0), ("Fill · hover", 1), ("Fill · pressed", 2), ("Label", 3), ("Border", 4)]
    m = {
        "Primary": ("bg.accent.bold", "bg.accent.boldHover", "bg.accent.boldPressed", "text.onAccent", "none"),
        "Secondary": ("bg.neutral.subtle", "bg.neutral.subtleHover", "bg.neutral.subtlePressed", "text.primary", "none"),
        "Outline": ("transparent", "bg.neutral.subtle", "bg.neutral.subtlePressed", "text.primary", "border.default"),
        "Ghost": ("transparent", "bg.neutral.subtle", "bg.neutral.subtlePressed", "text.primary", "none"),
        "Danger": ("bg.danger.bold", "bg.danger.boldHover", "bg.danger.boldPressed", "text.onDanger", "none"),
    }

    def cell(tok):
        sw = (D(f"width:12px;height:12px;border-radius:3px;flex:none;background:{col('color.' + tok)};box-shadow:inset 0 0 0 1px {col('color.shadow.soft')}")
              if tok not in ("transparent", "none") else D(f"width:12px;height:12px;border-radius:3px;flex:none;border:1px dashed {BORDER2}"))
        return D("flex:1;display:flex;gap:8px;align-items:center", sw, mono(tok, T1 if tok not in ("transparent", "none") else T3))
    head = D(f"display:flex;gap:16px;padding-bottom:10px;border-bottom:1px solid {BORDER}", D("width:120px;flex:none"),
             *[D("flex:1", S(ty("label.sm") + f";color:{T3}", v)) for v in m])
    rows = [head] + [D(f"display:flex;gap:16px;padding:10px 0;border-bottom:1px solid {BORDER};align-items:center",
                       D("width:120px;flex:none", S(ty("title.sm"), rname)), *[cell(m[v][i]) for v in m]) for rname, i in rows_def]
    shared = [("Disabled", "bg.disabled + text.disabled (exempt from contrast)"), ("Focus", "border.focus ring, 2px, offset 2px"),
              ("Shape", "radius.control"), ("Height", "size.control.sm · md · lg"), ("Padding", "space.inset.md · lg · xl"),
              ("Gap", "space.gap.sm"), ("Type", "text.label.lg"), ("Motion", "motion.transition.feedback (100ms, standard)")]
    return section("03.5-tokens", "04", "Token map",
                   "Every part reads a semantic token; nothing is hard-coded. A component token tier is optional and only earns its place when a part must diverge from its role.",
                   card("display:flex;flex-direction:column", *rows,
                        D("display:flex;flex-wrap:wrap;gap:8px 24px;padding-top:16px", *[
                            D("display:flex;gap:8px;align-items:baseline", S(ty("label.sm") + f";color:{T3}", k), mono(v, T1)) for k, v in shared])))


def usage():
    rules = [
        ("One primary per view", "If you need two primaries, one of them is secondary.", "DC-L08-05 · DC-L15-03 · L15 P08"),
        ("Don't disable submit", "Validate on submit and explain; use aria-disabled with helper text when an action truly cannot run.", "DC-L08-10"),
        ("Loading keeps focus", "Show the spinner after about 1s, keep the label and width, block repeat clicks.", "DC-L08-12 · DC-L13-01"),
        ("Verb-first labels", "Two to four words in sentence case that name the action: “Delete file”, not “OK”.", "DC-L08-08 · DC-L13-13"),
        ("Danger in context", "Subtle danger in lists; the solid danger fill belongs in the confirmation step. Prefer undo.", "DC-L08-06 · DC-L13-08"),
        ("Targets", "At least 24 × 24px (WCAG 2.5.8); 44px hit area on touch even when the visual is 32px.", "DC-L03-12 · DC-L08-07"),
    ]
    return section("03.6-usage", "05", "Usage",
                   "The rules the builder enforces while you compose screens.",
                   D("display:flex;flex-wrap:wrap;gap:16px", *[
                       card("width:426px;display:flex;flex-direction:column;gap:6px;padding:20px", S(ty("title.sm"), t),
                            S(ty("body.md") + f";color:{T2}", d), mono(src, T3)) for t, d, src in rules]))


def board_03():
    return board("03-button", "Button", [
        header("03.1-header", "Atlas 03 · Component", "Button",
               "The first component built on the starter tokens: anatomy, five variants, three sizes and six states, with the token behind every part.",
               [("Variants", "5"), ("Sizes", "3"), ("States", "6"), ("Figma", "5 sets × 18")]),
        anatomy(), matrices(), sizes(), token_map(), usage(),
    ])


# ================================================================= 04 builder concept

def seg_control(options, active):
    return D(f"display:flex;padding:2px;border-radius:8px;background:{NEU}", *[
        D(f"padding:4px 10px;border-radius:6px;{'background:' + CARD + ';box-shadow:' + shadow_css('elevation.shadow.raised') if o == active else ''}",
          S(ty("label.md") + f";color:{T1 if o == active else T2}", o)) for o in options])


def labeled(label, ctrl):
    return D("display:flex;flex-direction:column;gap:6px", S(ty("label.sm") + f";color:{T3}", label), ctrl)


def top_bar():
    logo = D(f"width:24px;height:24px;border-radius:6px;border:1px dashed {col('color.border.strong')};display:flex;align-items:center;justify-content:center",
             icon("question", T3, 14))
    return D(f"display:flex;align-items:center;justify-content:space-between;height:56px;padding:0 20px;background:{CARD};border-bottom:1px solid {BORDER}",
             D("display:flex;align-items:center;gap:12px", logo, S(ty("title.sm"), "Untitled system"),
               chip("Draft", NEU, T2)),
             D("display:flex;align-items:center;gap:8px", S(ty("body.md") + f";color:{T3}", "Foundations"), icon("chevron", T3, 14),
               S(ty("body.md") + f";color:{T1}", "Spacing")),
             D("display:flex;align-items:center;gap:8px", button("ghost", size="sm", label="History"),
               button("secondary", size="sm", label="Export"), button("primary", size="sm", label="Commit 3 changes")),
             data_subgroup="04.1a-topbar")


RAIL = [
    ("L0", "Context", "done", []), ("L1", "Principles", "done", []),
    ("L2", "Foundations", "open", [("Color", "done"), ("Typography", "done"), ("Spacing", "active"), ("Layout", "todo"), ("Shape", "todo"),
                                   ("Elevation", "todo"), ("Motion", "todo"), ("Iconography", "hook"), ("Imagery", "hook"), ("Data viz", "todo")]),
    ("L3", "Tokens", "todo", []), ("L4", "Components", "todo", []), ("L5", "Patterns", "todo", []),
    ("L6", "Guardrails", "todo", []), ("L7", "Delivery", "todo", []), ("L8", "Governance", "todo", []),
]


def status_icon(s):
    return {"done": icon("checkcircle", col("color.text.success"), 16), "active": icon("dot", col("color.text.accent"), 16),
            "todo": icon("ring", T3, 16), "hook": icon("question", T2, 16), "open": icon("down", T3, 16)}[s]


def rail():
    items = []
    for lid, name, st, kids in RAIL:
        items.append(D("display:flex;align-items:center;gap:10px;padding:6px 8px;border-radius:6px",
                       status_icon(st), S(ty("body.md") + f";color:{T1};flex:1", name), mono(lid, T3)))
        for kname, ks in kids:
            active = ks == "active"
            items.append(D(f"display:flex;align-items:center;gap:10px;padding:6px 8px 6px 34px;border-radius:6px;{'background:' + col('color.bg.accent.subtle') if active else ''}",
                           status_icon(ks), S(ty("body.md") + f";color:{col('color.text.accent') if active else (T1 if ks != 'todo' else T2)};flex:1;{'font-weight:500' if active else ''}", kname),
                           D(f"padding:0 6px;border:1px dashed {col('color.border.strong')};border-radius:4px", S(ty("label.md") + f";color:{T2}", "Ask"))
                           if ks == "hook" else ""))
    progress = D(f"height:4px;border-radius:2px;background:{NEU};display:flex", D(f"width:43%;height:4px;border-radius:2px;background:{col('color.bg.accent.bold')}"))
    return D(f"width:272px;flex:none;background:{CARD};border-right:1px solid {BORDER};padding:20px 12px;display:flex;flex-direction:column;gap:16px",
             D("display:flex;flex-direction:column;gap:10px;padding:0 8px",
               D("display:flex;align-items:center;gap:8px", badge_num("1"), S(ty("title.sm"), "Building blocks")),
               progress, S(ty("body.sm") + f";color:{T2}", "18 of 42 blocks decided · 2 hooks open")),
             D("display:flex;flex-direction:column;gap:2px", *items),
             D(f"margin-top:auto;padding:12px;border-radius:8px;background:{SUNK};display:flex;flex-direction:column;gap:4px",
               S(ty("label.md") + f";color:{T1}", "Nothing missed"),
               S(ty("body.sm") + f";color:{T2}", "24 blocks left. Next up: Layout, which depends on the spacing you set here.")),
             data_subgroup="04.1b-rail")


def mini_ui(mode, highlight=True):
    tc = lambda p: col(p, mode)
    tint = col(f"color.accent.{mode}.{4 if mode == 'light' else 5}", mode) if highlight else "transparent"
    inp = D(f"height:40px;padding:0 12px;border-radius:6px;border:1px solid {tc('color.border.strong')};background:{tc('color.surface.raised')};display:flex;align-items:center",
            S(ty("body.md") + f";color:{tc('color.text.primary')}", "Field notes"))
    row = lambda initials, name, role: D(f"display:flex;align-items:center;gap:12px;padding:8px 0;border-top:1px solid {tc('color.border.subtle')}",
                                         D(f"width:28px;height:28px;border-radius:9999px;background:{tc('color.bg.neutral.subtle')};display:flex;align-items:center;justify-content:center",
                                           S(ty("label.md") + f";color:{tc('color.text.secondary')}", initials)),
                                         S(ty("body.md") + f";color:{tc('color.text.primary')};flex:1", name),
                                         S(ty("body.sm") + f";color:{tc('color.text.tertiary')}", role))
    content = D(f"background:{tc('color.surface.raised')};display:flex;flex-direction:column;gap:12px",
                D("display:flex;flex-direction:column;gap:2px", S(ty("title.sm") + f";color:{tc('color.text.primary')}", "Workspace settings"),
                  S(ty("body.sm") + f";color:{tc('color.text.secondary')}", "Changes apply to everyone in this workspace.")),
                D("display:flex;flex-direction:column;gap:6px", S(ty("label.md") + f";color:{tc('color.text.primary')}", "Workspace name"), inp),
                D("display:flex;flex-direction:column", row("AR", "Asha Rao", "Owner"), row("MK", "Mo Kim", "Editor")),
                D("display:flex;justify-content:flex-end;gap:8px", button("ghost", mode=mode, size="sm", label="Cancel"),
                  button("primary", mode=mode, size="sm", label="Save changes")))
    card_ = D(f"border:1px solid {tc('color.border.subtle')};border-radius:12px;overflow:hidden;box-shadow:{shadow_css('elevation.shadow.raised', mode)}",
              D(f"padding:16px;background:{tint}", content))
    return D(f"flex:1;background:{tc('color.surface.base')};border-radius:10px;padding:20px;display:flex;flex-direction:column;gap:12px;border:1px solid {tc('color.border.subtle')}",
             D("display:flex;justify-content:space-between;align-items:center", S(ty("label.md") + f";color:{tc('color.text.secondary')}", mode.title()),
               S(ty("code.sm") + f";color:{tc('color.text.tertiary')}", f"inset.lg = 16")), card_)


def center():
    head = D("display:flex;justify-content:space-between;align-items:flex-start;gap:24px",
             D("display:flex;flex-direction:column;gap:4px;max-width:440px", S(ty("title.lg"), "Spacing"),
               S(ty("body.md") + f";color:{T2}", "The distance inside and between things. One scale, used everywhere, keeps layouts calm and aligned.")),
             D("display:flex;gap:16px;align-items:flex-end",
               labeled("Base unit", seg_control(["4px", "8px"], "4px")),
               labeled("Density", seg_control(["Comfortable", "Compact"], "Comfortable")),
               button("outline", size="sm", label="Show 6 variations")))
    ruler = card("display:flex;flex-direction:column;gap:20px;padding:20px",
                 D("display:flex;justify-content:space-between;align-items:center",
                   D("display:flex;gap:8px;align-items:center", badge_num("2"), S(ty("title.sm"), "Scale")),
                   mono("14 steps · 4px grid · shown at 1:1", T3)),
                 staircase("light", selected="200", gap=10, handle=True, minw=24),
                 D("display:flex;justify-content:space-between;align-items:center",
                   D("display:flex;gap:8px;align-items:baseline", mono("space.200 = 16px", T1),
                     S(ty("body.sm") + f";color:{T2}", "feeds space.inset.lg, which 14 components use")),
                   S(ty("body.sm") + f";color:{T3}", "Drag a step to resize it. Values snap to the 4px grid.")))
    preview = card("display:flex;flex-direction:column;gap:16px;padding:20px",
                   D("display:flex;justify-content:space-between;align-items:center",
                     D("display:flex;gap:8px;align-items:center", badge_num("3"), S(ty("title.sm"), "Live preview"),
                       S(ty("body.sm") + f";color:{T3}", "re-renders on every change, both modes at once")),
                     D("display:flex;gap:8px;align-items:center", D(f"width:12px;height:12px;border-radius:2px;background:{col('color.accent.light.4')}"),
                       S(ty("body.sm") + f";color:{T2}", "Highlight: where space.inset.lg applies"))),
                   D("display:flex;gap:16px", mini_ui("light"), mini_ui("dark")))
    changes = card("display:flex;flex-direction:column;gap:10px;padding:16px 20px",
                   D("display:flex;justify-content:space-between;align-items:center",
                     D("display:flex;gap:8px;align-items:baseline", S(ty("title.sm"), "Change set"), S(ty("body.sm") + f";color:{T3}", "3 changes since the last commit")),
                     button("ghost", size="sm", label="Review visual diff")),
                   *[D(f"display:flex;gap:16px;align-items:baseline;padding-top:8px;border-top:1px solid {BORDER}",
                       D("width:160px;flex:none", mono(tok, T1)), S(ty("label.md") + f";color:{T1};width:160px;flex:none", chg),
                       S(ty("body.sm") + f";color:{T2}", eff))
                     for tok, chg, eff in (("space.inset.lg", "12 → 16px", "14 components, both modes; contrast unaffected"),
                                           ("space.gap.md", "8 → 12px", "Form stacks and card groups"),
                                           ("density default", "compact → comfortable", "Compact stays available per user"))])
    return D(f"flex:1;min-width:0;background:{SUNK};padding:24px;display:flex;flex-direction:column;gap:16px", head, ruler, preview, changes,
             data_subgroup="04.1c-editor")


def panel_block(n, title, right, *kids):
    return D(f"display:flex;flex-direction:column;gap:12px;padding:20px;border-bottom:1px solid {BORDER}",
             D("display:flex;justify-content:space-between;align-items:center",
               D("display:flex;gap:8px;align-items:center", badge_num(n), S(ty("title.sm"), title)), right), *kids)


def bullet_list(items, glyph, color):
    return D("display:flex;flex-direction:column;gap:6px", *[
        D("display:flex;gap:8px;align-items:flex-start", D("padding-top:2px;flex:none", icon(glyph, color, 16)),
          S(ty("body.md") + f";color:{T1}", t)) for t in items])


def right_panel():
    detail = panel_block("4", "Token", mono("Spacing collection", T3),
                         D("display:flex;align-items:baseline;justify-content:space-between",
                           mono("space.inset.lg", T1, "code.md"), S(ty("title.lg"), "16px")),
                         mono("→ space.200 · compact: 12px", T3),
                         S(ty("body.md") + f";color:{T2}", "Default padding inside controls and cards. It sets how roomy the product feels."),
                         S(ty("label.sm") + f";color:{T3}", "Use it for"),
                         bullet_list(["Card and panel padding", "Button and input padding (md)"], "check", col("color.text.success")),
                         S(ty("label.sm") + f";color:{T3}", "Avoid it for"),
                         bullet_list(["Gaps between page sections (space.layout.section)", "Margins on reusable components"], "x", col("color.text.danger")),
                         D("display:flex;flex-wrap:wrap;gap:6px", *[chip(c, NEU, T1) for c in ("Button · md", "Card", "Input", "Dialog body", "+10")]),
                         D(f"display:flex;flex-direction:column;gap:4px;padding:10px 12px;border-radius:8px;background:{SUNK}",
                           *[D("display:flex;gap:12px", S(ty("label.sm") + f";color:{T3};width:52px;flex:none", k), mono(v, T1))
                             for k, v in (("CSS", "var(--space-inset-lg)"), ("Figma", "space/inset/lg"), ("iOS", "DSSpace.insetLg"))]))
    drop = D(f"display:flex;flex-direction:column;gap:10px;padding:14px;border:1px dashed {BORDER2};border-radius:8px;background:{SUNK}",
             D("display:flex;gap:10px;align-items:center", icon("upload", T2, 16),
               S(ty("label.lg") + f";color:{T1}", "Add an example website or file")),
             D("display:flex;gap:8px",
               D(f"flex:1;height:32px;padding:0 10px;border-radius:6px;border:1px solid {col('color.border.strong')};background:{CARD};display:flex;align-items:center",
                 S(ty("body.md") + f";color:{T3}", "https://")),
               button("secondary", size="sm", label="Read")))
    found = D(f"display:flex;flex-direction:column;gap:8px;padding:12px;border:1px solid {BORDER};border-radius:8px",
              D("display:flex;justify-content:space-between;align-items:center", mono("reference-site.example", T1), chip("Inspiration", NEU, T2)),
              *[D("display:flex;justify-content:space-between;gap:8px", S(ty("body.sm") + f";color:{T2}", k), S(ty("body.sm") + f";color:{T1}", v))
                for k, v in (("Base unit", "4px · matches"), ("Card padding", "20px → nearest space.250"), ("Section gap", "48px · matches"))],
              D("display:flex;gap:8px", button("secondary", size="sm", label="Accept"), button("ghost", size="sm", label="Adjust"),
                button("ghost", size="sm", label="Ignore")))
    refs = panel_block("5", "References", mono("any step", T3), drop, found,
                       S(ty("body.sm") + f";color:{T3}", "Values are estimates until you accept them. Structure is copied, identity never is."))
    hooks = []
    for name, st, action in (("Logo", "Not yet", "Upload SVG"), ("Icon set", "Library", "Change"), ("Illustration", "Not yet", "See options"),
                             ("Brand typeface", "Inter · OFL", "")):
        bg, fg = {"Not yet": (col("color.bg.warning.subtle"), col("color.text.warning")),
                  "Library": (NEU, T2)}.get(st, (col("color.bg.success.subtle"), col("color.text.success")))
        hooks.append(D("display:flex;align-items:center;gap:10px",
                       icon("question" if st == "Not yet" else "checkcircle", T2 if st == "Not yet" else col("color.text.success"), 16),
                       S(ty("body.md") + f";color:{T1};flex:1", name), chip(st, bg, fg),
                       S(ty("label.md") + f";color:{col('color.text.accent')};width:76px;text-align:right", action)))
    hook_block = panel_block("6", "Do you have these?", mono("2 open", T3), *hooks,
                             S(ty("body.sm") + f";color:{T3}", "No logo yet? Commission a designer, use a placeholder wordmark, or try a tool, with honest caveats."))
    return D(f"width:360px;flex:none;background:{CARD};border-left:1px solid {BORDER};display:flex;flex-direction:column", detail, refs, hook_block,
             data_subgroup="04.1d-inspector")


def app_window():
    return E("section", f"display:flex;flex-direction:column;width:1440px;background:{CARD};border-bottom:1px solid {BORDER}",
             top_bar(), D("display:flex;align-items:stretch", rail(), center(), right_panel(), data_subgroup="04.1-body"), data_group="04.1-app")


def annotations():
    items = [
        ("1", "Blocks first, with coverage", "The system starts as the complete map of blocks. Progress counts every block, so nothing is skipped.", "BRIEF 1 · 5 · ontology"),
        ("2", "A visual ruler", "The scale is drawn at real size. Engineers drag steps; values stay on the grid.", "DC-L03-01 · DC-L16-14"),
        ("3", "Live preview, both modes", "Real components re-render in light and dark side by side, with the edited token highlighted.", "DC-L16-06 · L16 G1.1"),
        ("4", "Fine detail", "What the token is, where to use it, where not to, who uses it, and its name in code and Figma.", "BRIEF 3 · DC-L03-04"),
        ("5", "Reference intake", "Add a site, screenshot or Figma file at any step. Found values arrive as suggestions to accept.", "BRIEF 4 · Q-ref-01"),
        ("6", "Designer hooks", "Logo, icons, illustration and type are asked for, not faked, with paths when the answer is no.", "BRIEF 2 · Q-brand-03"),
    ]
    return E("section", "display:flex;flex-direction:column;gap:24px;padding:48px 64px 72px",
             D("display:flex;flex-direction:column;gap:6px", S(ty("label.sm") + f";color:{T3}", "Atlas 04 · Builder concept"),
               S(ty("headline.md"), "The spacing block editor"),
               S(ty("body.md") + f";color:{T2};max-width:760px", "One screen of the builder in its visual-first mode: pick values on a live preview, learn why as you go, bring references, and hand designer-owned work to designers.")),
             D("display:flex;flex-wrap:wrap;gap:24px", *[
                 D("width:421px;display:flex;gap:12px;align-items:flex-start", badge_num(n),
                   D("display:flex;flex-direction:column;gap:4px", S(ty("title.sm"), t), S(ty("body.md") + f";color:{T2}", d), mono(src, T3)))
                 for n, t, d, src in items]),
             data_group="04.2-annotations")


def board_04():
    return board("04-builder-concept", "Builder concept", [app_window(), annotations()], pad="0", gap=0)


# ================================================================= main

def main():
    out = {"01-building-blocks-map.html": board_01(), "02-foundations.html": board_02(),
           "03-button.html": board_03(), "04-builder-concept.html": board_04()}
    for name, doc in out.items():
        with open(os.path.join(HERE, name), "w") as f:
            f.write(doc)
        groups = doc.count("data-group=")
        print(f"{name}: {len(doc) // 1024} KB, {groups} groups")


if __name__ == "__main__":
    main()
