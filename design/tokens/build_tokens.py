#!/usr/bin/env python3
"""Generate the starter token set (DTCG 2025.10) for design agent D1.

Stdlib only. Run from anywhere:  python3 design/tokens/build_tokens.py
Writes the *.tokens.json files, the resolver and contrast-pairs.json next to this script.

Color method (sources in design/README.md):
- Ramps are built in OKLCH (DC-L01-01) and are contrast-indexed (DC-L01-03, the Spectrum/Leonardo
  approach): every hue hits the same WCAG luminance target at the same step, so swapping the accent
  keeps every text/background pairing valid.
- 12 steps with a fixed job per step (DC-L01-02, L09 A1 row 4, Radix pattern in DC-L01-03).
- Separate light and dark ramps; dark mode is a separate semantic mapping (DC-L01-18).
- Chroma peaks at step 9 and falls at the extremes (DC-L01-03, DC-L01-06); every value is
  gamut-mapped into sRGB by lowering chroma, and stored with a hex fallback (DC-L01-05).
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
NS = "dev.dsbuilder"  # placeholder reverse-domain namespace for $extensions

# ---------------------------------------------------------------- color math (OKLab, Ottosson)

def oklch_to_linear_srgb(L, C, H):
    h = math.radians(H)
    a, b = C * math.cos(h), C * math.sin(h)
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = l_ ** 3, m_ ** 3, s_ ** 3
    return (
        4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
        -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
        -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s,
    )


def in_gamut(rgb, eps=1e-6):
    return all(-eps <= c <= 1 + eps for c in rgb)


def encode(c):
    c = min(max(c, 0.0), 1.0)
    return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055


def hex_of(rgb_lin):
    return "#" + "".join(f"{round(encode(c) * 255):02x}" for c in rgb_lin)


def luminance_of_hex(hx):
    """WCAG 2.2 relative luminance of an sRGB hex color."""
    def lin(v):
        v = v / 255
        return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (int(hx[i:i + 2], 16) for i in (1, 3, 5))
    return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)


def max_chroma(L, H):
    lo, hi = 0.0, 0.4
    for _ in range(30):
        mid = (lo + hi) / 2
        if in_gamut(oklch_to_linear_srgb(L, mid, H)):
            lo = mid
        else:
            hi = mid
    return lo


def solve_step(target_Y, C_want, H):
    """Find OKLCH L so the (gamut-mapped) color has relative luminance target_Y."""
    lo, hi = 0.0, 1.0
    for _ in range(40):
        L = (lo + hi) / 2
        C = min(C_want, max_chroma(L, H))
        r, g, b = oklch_to_linear_srgb(L, C, H)
        Y = 0.2126 * r + 0.7152 * g + 0.0722 * b
        if Y < target_Y:
            lo = L
        else:
            hi = L
    L = (lo + hi) / 2
    C = min(C_want, max_chroma(L, H))
    return L, C, hex_of(oklch_to_linear_srgb(L, C, H))


# ---------------------------------------------------------------- ramp recipe

# Light targets are WCAG contrast against white; converted to luminance Y = 1.05/c - 0.05.
LIGHT_CONTRAST_VS_WHITE = [1.02, 1.05, 1.10, 1.16, 1.24, 1.38, 1.75, 3.30, 4.80, 5.60, 6.60, 15.50]
LIGHT_Y = [1.05 / c - 0.05 for c in LIGHT_CONTRAST_VS_WHITE]
# Dark targets are luminance directly (step 1 is the darkest surface).
DARK_Y = [0.0065, 0.0095, 0.014, 0.019, 0.025, 0.034, 0.050, 0.165, 0.270, 0.310, 0.370, 0.800]

STEP_JOBS = {
    1: "app background", 2: "subtle background / sunken", 3: "component background",
    4: "component background hover", 5: "component background pressed or selected",
    6: "subtle border, divider", 7: "default border (decorative)", 8: "strong border (3:1 interactive), disabled text",
    9: "solid fill", 10: "solid fill hover", 11: "low-contrast text, solid fill pressed",
    12: "high-contrast text",
}

ACCENT_CHROMA_LIGHT = [0.008, 0.016, 0.035, 0.055, 0.075, 0.095, 0.115, 0.150, 0.200, 0.190, 0.170, 0.080]
ACCENT_CHROMA_DARK = [0.012, 0.018, 0.035, 0.050, 0.065, 0.080, 0.100, 0.130, 0.150, 0.150, 0.140, 0.050]
NEUTRAL_CHROMA_LIGHT = [0.002, 0.003, 0.005, 0.006, 0.007, 0.009, 0.011, 0.013, 0.014, 0.014, 0.013, 0.010]
NEUTRAL_CHROMA_DARK = [0.004, 0.005, 0.006, 0.007, 0.008, 0.009, 0.011, 0.013, 0.014, 0.013, 0.010, 0.004]

ACCENT_HUE = 265  # placeholder seed; the builder asks for the brand color (Q-color-01) [inferred]
HUES = {
    "neutral": (ACCENT_HUE, "Hue-matched cool neutral, chroma <= 0.014 (DC-L01-06)."),
    "accent": (ACCENT_HUE, "The single brand/UI accent (DC-L01-08, L09 A1 row 3). Hue 265 is a placeholder seed [inferred]."),
    "success": (150, "Status: success (DC-L01-15)."),
    "warning": (75, "Status: warning (DC-L01-15). Contrast-indexing makes its solid a dark amber that carries white text."),
    "danger": (27, "Status: danger (DC-L01-15)."),
    "info": (230, "Status: info (DC-L01-15). Sits 35 deg from the accent hue, so it always ships with an icon and label (DC-L01-15, DC-L01-23) [inferred]."),
}


def oklch_value(L, C, H, hx):
    return {"colorSpace": "oklch", "components": [round(L, 4), round(C, 4), H], "hex": hx}


def srgb_value(hx, alpha=None):
    comps = [round(int(hx[i:i + 2], 16) / 255, 4) for i in (1, 3, 5)]
    v = {"colorSpace": "srgb", "components": comps, "hex": hx}
    if alpha is not None:
        v["alpha"] = alpha
    return v


def build_ramps():
    color = {
        "$type": "color",
        "$description": "Primitive color ramps. Private tier: components never use these directly (DC-L01-26, L09 A1 row 1).",
        "$extensions": {NS: {
            "method": "OKLCH, contrast-indexed, 12 steps, separate light and dark ramps",
            "sources": ["DC-L01-01", "DC-L01-02", "DC-L01-03", "DC-L01-05", "DC-L01-06", "DC-L01-18", "L09-A1.3", "L09-A1.4"],
            "stepJobs": {str(k): v for k, v in STEP_JOBS.items()},
            "lightContrastVsWhite": LIGHT_CONTRAST_VS_WHITE,
            "darkLuminance": DARK_Y,
        }},
        "white": {"$value": srgb_value("#ffffff"), "$description": "Pure white (Carbon keeps White and Black in its palette, DC-L01-02)."},
        "black": {"$value": srgb_value("#000000"), "$description": "Pure black; shadow base in dark mode (DC-L04-12)."},
    }
    report = {}
    for name, (H, desc) in HUES.items():
        neutral = name == "neutral"
        group = {"$description": desc}
        for scheme, targets, chroma in (
            ("light", LIGHT_Y, NEUTRAL_CHROMA_LIGHT if neutral else ACCENT_CHROMA_LIGHT),
            ("dark", DARK_Y, NEUTRAL_CHROMA_DARK if neutral else ACCENT_CHROMA_DARK),
        ):
            sub = {}
            for i, (Y, C) in enumerate(zip(targets, chroma), start=1):
                L, Cu, hx = solve_step(Y, C, H)
                sub[str(i)] = {"$value": oklch_value(L, Cu, H, hx), "$description": STEP_JOBS[i]}
                report[f"{name}.{scheme}.{i}"] = hx
            group[scheme] = sub
        color[name] = group
    return {"color": color}, report


# ---------------------------------------------------------------- semantic color

def A(path):
    return "{" + path + "}"


def semantic_color(mode):
    L = mode == "light"
    n = (lambda s: A(f"color.neutral.{mode}.{s}"))
    r = (lambda hue, s: A(f"color.{hue}.{mode}.{s}"))
    # dark surfaces step up in lightness (DC-L01-13, DC-L04-13); light uses white for raised/overlay
    surf = {
        "sunken": (n(2) if L else n(1), "Wells, code blocks, page gutters."),
        "base": (n(1) if L else n(2), "The page background."),
        "raised": (A("color.white") if L else n(3), "Cards and panels that sit on the page."),
        "overlay": (A("color.white") if L else n(4), "Menus, popovers, dialogs (always with a shadow)."),
    }
    on_bold = A("color.white") if L else A(f"color.neutral.dark.1")
    tok = lambda v, d: {"$value": v, "$description": d}
    out = {
        "surface": {k: tok(v, d) for k, (v, d) in surf.items()},
        "text": {
            "primary": tok(n(12), "Body copy, headings, labels."),
            "secondary": tok(n(11), "Supporting text, descriptions, table meta."),
            "tertiary": tok(n(9), "Placeholders and captions on surfaces only (not on component fills)."),
            "disabled": tok(n(8), "Disabled labels. Exempt from contrast minimums (WCAG 1.4.3, S-L08-071)."),
            "inverse": tok(A("color.white") if L else n(1), "Text on bg.inverse (tooltips, toasts)."),
            "accent": tok(r("accent", 11), "Links and accent text."),
            "onAccent": tok(on_bold, "Text and icons on bg.accent.bold* fills."),
        },
        "bg": {
            "neutral": {
                "subtle": tok(n(3) if L else n(5), "Secondary button, chips, hovered rows."),
                "subtleHover": tok(n(4) if L else n(6), "Hover on neutral subtle fills (+1 step, DC-L01-17)."),
                "subtlePressed": tok(n(5) if L else n(7), "Pressed or selected neutral fills (+2 steps, DC-L01-17)."),
            },
            "accent": {
                "subtle": tok(r("accent", 3), "Selected rows, accent badges, focus-within wells."),
                "bold": tok(r("accent", 9), "Primary action fill. One per view (DC-L15-03, L15 P08)."),
                "boldHover": tok(r("accent", 10), "Primary action hover (+1 step)."),
                "boldPressed": tok(r("accent", 11), "Primary action pressed (+2 steps)."),
            },
            "disabled": tok(n(3) if L else n(4), "Disabled control fill."),
            "inverse": tok(n(12), "Tooltips and toasts: the inverted surface."),
        },
        "border": {
            "subtle": tok(n(6), "Dividers, card edges, decorative lines."),
            "default": tok(n(7), "Outline buttons, table grid (decorative; text carries the meaning)."),
            "strong": tok(n(8), "Input and checkbox borders: the only boundary, so 3:1 (DC-L01-16)."),
            "focus": tok(r("accent", 9) if L else r("accent", 11), "Focus ring: 3:1 against every surface (DC-L04-09, DC-L08-11)."),
            "accent": tok(r("accent", 8), "Selected card or accent outline."),
        },
        "icon": {
            "default": tok(n(11), "Icons beside text; aliases secondary text (DC-L05-08)."),
            "accent": tok(r("accent", 11), "Selected and interactive icons."),
        },
        "overlay": {
            "scrim": tok(srgb_value(scrim_base(mode), 0.45 if L else 0.60),
                         "Modal backdrop: 45% (light) / 60% (dark) of the tinted near-black (DC-L04-18)."),
        },
        "shadow": {
            "soft": tok(srgb_value(shadow_base(mode), 0.08 if L else 0.16), "Contact and raised shadow color; alpha doubles in dark (DC-L04-12)."),
            "strong": tok(srgb_value(shadow_base(mode), 0.16 if L else 0.32), "Ambient shadow for overlays; alpha doubles in dark (DC-L04-12)."),
            "ring": tok(srgb_value(RING_HEX, 0.0 if L else 0.12), "1px edge ring for overlays: alpha 0 in light, 12% in dark (Primer/Atlassian pattern, DC-L04-12)."),
        },
    }
    for status in ("success", "warning", "danger", "info"):
        out["bg"][status] = {
            "subtle": tok(r(status, 3), f"{status.title()} banner and badge background."),
            "bold": tok(r(status, 9), f"{status.title()} solid fill."),
            "boldHover": tok(r(status, 10), f"{status.title()} solid hover."),
            "boldPressed": tok(r(status, 11), f"{status.title()} solid pressed."),
        }
        out["text"][status] = tok(r(status, 11), f"{status.title()} text and icons; always paired with an icon or label (DC-L01-15).")
        out["text"]["on" + status.title()] = tok(on_bold, f"Text on bg.{status}.bold* fills.")
        out["border"][status] = tok(r(status, 8), f"{status.title()} outline (for example an invalid field).")
    return {"color": {
        "$type": "color",
        "$description": f"Semantic color roles, {mode} mapping. Names never change across modes; only values do (DC-L01-11, DC-L01-18, S-L07-112).",
        "$extensions": {NS: {"mode": mode, "grammar": "property.role.emphasis.state (DC-L01-11, DC-L01-12)",
                             "sources": ["DC-L01-11", "DC-L01-12", "DC-L01-13", "DC-L01-14", "DC-L01-15", "DC-L01-16", "DC-L01-17", "DC-L01-18", "DC-L01-19", "DC-L04-12", "DC-L04-18"]}},
        **out,
    }}


RAMPS = {}
RING_HEX = None


def scrim_base(mode):
    return RAMPS["neutral.light.12"] if mode == "light" else RAMPS["neutral.dark.1"]


def shadow_base(mode):
    return RAMPS["neutral.light.12"] if mode == "light" else "#000000"


# ---------------------------------------------------------------- dimensions

def dim(v, unit="px"):
    return {"value": v, "unit": unit}


def spacing_primitives():
    steps = [("0", 0), ("025", 2), ("050", 4), ("075", 6), ("100", 8), ("150", 12), ("200", 16), ("250", 20),
             ("300", 24), ("400", 32), ("500", 40), ("600", 48), ("800", 64), ("1000", 80), ("1200", 96)]
    space = {
        "$type": "dimension",
        "$description": "Spacing primitives on a 4px grid with an 8px rhythm; names are percent of 8px (Atlassian style). Never use padding or margin in a primitive name.",
        "$extensions": {NS: {"sources": ["L09-A1.2", "DC-L03-01", "DC-L03-02", "DC-L03-03", "DC-L03-06"]}},
    }
    for name, px in steps:
        space[name] = {"$value": dim(px)}
    space["layout"] = {
        "$description": "Layout spacing varies by breakpoint, never by density (DC-L03-17).",
        "gutter": {"$value": A("space.300"), "$description": "Column gutter, medium+ (DC-L03-15)."},
        "margin": {"$value": A("space.300"), "$description": "Page margin, medium+; 16px on compact widths (DC-L03-15)."},
        "section": {"$value": A("space.600"), "$description": "Gap between page sections; keeps inner:outer >= 1:2 (DC-L03-24, DC-L15-05)."},
    }
    size = {
        "$type": "dimension",
        "control": {
            "$description": "Control heights shared by buttons, inputs and selects (DC-L03-07, DC-L08-07). Height = 20px line box + 2 x block padding (DC-L03-05).",
            "sm": {"$value": dim(32)}, "md": {"$value": dim(40)}, "lg": {"$value": dim(48)},
        },
        "icon": {
            "$description": "Icon sizes; pair to the adjacent line height (DC-L05-05, DC-L03-08).",
            "sm": {"$value": dim(16)}, "md": {"$value": dim(20)}, "lg": {"$value": dim(24)},
        },
        "target": {
            "min": {"$value": dim(24), "$description": "Minimum pointer target, WCAG 2.5.8 AA; hit area grows to 44 on coarse pointers (DC-L03-12)."},
        },
    }
    return {"space": space, "size": size}


def spacing_semantic(density):
    comfy = density == "comfortable"
    # compact shrinks insets and gaps by one scale step (DC-L03-10, DC-L03-11)
    ladder = ["025", "050", "100", "150", "200", "300"]
    sizes = ["xs", "sm", "md", "lg", "xl"]
    base = 1 if comfy else 0
    inset = {s: {"$value": A(f"space.{ladder[base + i]}")} for i, s in enumerate(sizes)}
    gap = {s: {"$value": A(f"space.{ladder[base + i]}")} for i, s in enumerate(sizes)}
    notes = {
        "inset": {"xs": "Tag and badge padding.", "sm": "Compact chip padding, icon-button inset.",
                  "md": "Small control padding, list-row block padding.", "lg": "Default control and card padding.",
                  "xl": "Dialog and panel padding."},
        "gap": {"xs": "Icon to label inside a control.", "sm": "Between related controls (DC-L03-13: 8px desktop).",
                "md": "Form field stack, label to field group.", "lg": "Between groups inside a card.",
                "xl": "Between cards (outer gap: at least 2x the inner gap, DC-L03-24)."},
    }
    for fam, d in (("inset", inset), ("gap", gap)):
        for s in sizes:
            d[s]["$description"] = notes[fam][s]
    return {"space": {
        "$type": "dimension",
        "$description": f"Semantic spacing, {density} density. Parents own spacing (padding + gap); children never set outer margins (DC-L03-04).",
        "$extensions": {NS: {"density": density, "sources": ["DC-L03-04", "DC-L03-10", "DC-L03-11", "DC-L03-24"]}},
        "inset": inset, "gap": gap,
    }}


def radius_tokens():
    radius = {
        "$type": "dimension",
        "$description": "Radius scale (L09 A1 row 7: 0-24 plus full; median control radius 6). Semantic roles below (DC-L04-03).",
        "$extensions": {NS: {"sources": ["L09-A1.7", "DC-L04-01", "DC-L04-02", "DC-L04-03", "DC-L04-05"]}},
    }
    for v in (0, 2, 4, 6, 8, 12, 16, 24):
        radius[str(v)] = {"$value": dim(v)}
    radius["full"] = {"$value": dim(9999), "$description": "Pills and avatars (person = full, DC-L04-03)."}
    radius["detail"] = {"$value": A("radius.4"), "$description": "Checkboxes, tags, small badges."}
    radius["control"] = {"$value": A("radius.6"), "$description": "Buttons, inputs, selects (L09 median 6px)."}
    radius["container"] = {"$value": A("radius.12"), "$description": "Cards and panels. Nested radius = outer - padding (DC-L04-05)."}
    radius["overlay"] = {"$value": A("radius.16"), "$description": "Dialogs, sheets, popovers."}
    border = {
        "$type": "dimension",
        "width": {
            "$description": "Border widths 1/2/4 (DC-L03-09, DC-L04-07).",
            "1": {"$value": dim(1)}, "2": {"$value": dim(2)}, "4": {"$value": dim(4)},
            "default": {"$value": A("border.width.1")},
            "selected": {"$value": A("border.width.2"), "$description": "Use an inset shadow so layout does not jump (DC-L04-07)."},
        },
    }
    focus = {
        "$type": "dimension",
        "$description": "Focus indicator: 2px solid ring, 2px offset, color border.focus (DC-L04-09, DC-L08-11; WCAG 2.4.7, 2.4.13).",
        "ring": {"width": {"$value": A("border.width.2")}, "offset": {"$value": dim(2)}},
    }
    return {"radius": radius, "border": border, "focus": focus}


# ---------------------------------------------------------------- typography

SIZES = [12, 14, 16, 20, 24, 28, 32, 40, 48]
LINES = [16, 20, 24, 28, 32, 36, 40, 52]

STYLES = [
    # name, size, line, weight, tracking(em), family, use, avoid
    ("display", 48, 52, "semibold", -0.02, "sans", "One hero line per page: marketing, empty-state headline.", "App chrome, cards, anything repeated."),
    ("headline.lg", 32, 40, "semibold", -0.01, "sans", "Page titles.", "Section titles inside a page."),
    ("headline.md", 28, 36, "semibold", -0.01, "sans", "Dialog and settings page titles.", "Card titles."),
    ("headline.sm", 24, 32, "semibold", 0.0, "sans", "Top-level section titles.", "Dense tables and toolbars."),
    ("title.lg", 20, 28, "semibold", 0.0, "sans", "Card and panel titles.", "Body emphasis."),
    ("title.md", 16, 24, "semibold", 0.0, "sans", "Group titles, list headers.", "Buttons (use label.lg)."),
    ("title.sm", 14, 20, "semibold", 0.0, "sans", "Table headers, field-group titles.", "Paragraph emphasis (use weight in body)."),
    ("body.lg", 16, 24, "regular", 0.0, "sans", "Long-form reading, docs, onboarding copy.", "Dense tables and forms."),
    ("body.md", 14, 20, "regular", 0.0, "sans", "Default UI text: forms, tables, descriptions.", "Long articles (use body.lg)."),
    ("body.sm", 12, 16, "regular", 0.0, "sans", "Helper text, timestamps, captions.", "Anything people must read at length."),
    ("label.lg", 14, 20, "medium", 0.0, "sans", "Button and control labels (md, lg).", "Headings."),
    ("label.md", 12, 16, "medium", 0.0, "sans", "Small control labels, badges, tabs in dense bars.", "Body text."),
    ("label.sm", 12, 16, "medium", 0.04, "sans", "Overlines in all caps with +0.04em tracking (DC-L02-18).", "Sentences; all caps below 11px."),
    ("code.md", 14, 20, "regular", 0.0, "mono", "Token names, code in docs.", "UI labels."),
    ("code.sm", 12, 16, "regular", 0.0, "mono", "Inline values, code syntax rows.", "Paragraphs."),
]


def typography_tokens():
    font = {
        "family": {
            "$type": "fontFamily",
            "$description": "One UI family plus one mono (DC-L02-03); open-source neutral face (L09 A2 row 5, DC-L02-01).",
            "sans": {"$value": ["Inter", "system-ui", "-apple-system", "Segoe UI", "Roboto", "sans-serif"]},
            "mono": {"$value": ["JetBrains Mono", "SF Mono", "ui-monospace", "Menlo", "Consolas", "monospace"]},
        },
        "weight": {
            "$type": "fontWeight",
            "$description": "Three weights: 400 body, 500 labels, 600 headings (DC-L02-15, L15 P03).",
            "regular": {"$value": 400}, "medium": {"$value": 500}, "semibold": {"$value": 600},
        },
        "size": {
            "$type": "dimension",
            "$description": "9 sizes: ratio 1.2 from a 14px base, rounded to even px and hand-adjusted (DC-L02-08, DC-L02-09, DC-L02-10). Adjacent steps differ by >= 10%.",
            **{str(s): {"$value": dim(s)} for s in SIZES},
        },
        "lineHeight": {
            "$type": "dimension",
            "$description": "Line heights snapped to 4px: ~1.5 at 12-16px, ~1.4 at 20-24px, ~1.25 at 28-40px, ~1.1 at 48px (DC-L02-13).",
            **{str(v): {"$value": dim(v)} for v in LINES},
        },
    }
    text = {
        "$type": "typography",
        "$description": "15 semantic styles: role x size (DC-L02-07, L09 A1 row 8). lineHeight is a unitless multiplier as DTCG requires; the px value is in $extensions for Figma.",
        "$extensions": {NS: {"sources": ["DC-L02-07", "DC-L02-08", "DC-L02-09", "DC-L02-10", "DC-L02-13", "DC-L02-14", "DC-L02-15", "DC-L02-18", "L09-A1.8"]}},
    }
    for name, size, line, weight, em, fam, use, avoid in STYLES:
        node = text
        parts = name.split(".")
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        ext = {"lineHeightPx": line, "letterSpacingEm": em, "use": use, "avoid": avoid,
               "fontSizeRef": f"font.size.{size}", "lineHeightRef": f"font.lineHeight.{line}"}
        if name == "label.sm":
            ext["textTransform"] = "uppercase"
        node[parts[-1]] = {
            "$value": {
                "fontFamily": A(f"font.family.{fam}"),
                "fontSize": A(f"font.size.{size}"),
                "fontWeight": A(f"font.weight.{weight}"),
                "letterSpacing": dim(round(size * em, 2)),
                "lineHeight": round(line / size, 4),
            },
            "$extensions": {NS: ext},
        }
    return {"font": font, "text": text}


# ---------------------------------------------------------------- elevation and motion

def shadow_layer(color, x, y, blur, spread):
    return {"color": A(color), "offsetX": dim(x), "offsetY": dim(y), "blur": dim(blur), "spread": dim(spread)}


def elevation_tokens():
    return {"elevation": {
        "$description": "Hybrid depth: in-page containers are flat with a 1px border; shadows only for things that float. Dark mode raises surface lightness; shadow colors swap per theme (DC-L04-10, DC-L04-11, DC-L04-12, L09 A1 row 12).",
        "$extensions": {NS: {"levels": {"sunken": "color.surface.sunken, no shadow", "base": "color.surface.base, no shadow",
                                        "raised": "color.surface.raised + border.subtle + shadow.raised",
                                        "overlay": "color.surface.overlay + shadow.overlay"},
                             "sources": ["DC-L04-10", "DC-L04-11", "DC-L04-12", "DC-L04-13", "L09-A1.12"]}},
        "shadow": {
            "$type": "shadow",
            "raised": {"$value": [shadow_layer("color.shadow.soft", 0, 1, 2, 0), shadow_layer("color.shadow.soft", 0, 2, 8, 0)],
                       "$description": "Cards, sticky headers, dragged rows. 1px contact + soft blur."},
            "overlay": {"$value": [shadow_layer("color.shadow.soft", 0, 1, 2, 0), shadow_layer("color.shadow.strong", 0, 8, 24, -4),
                                   shadow_layer("color.shadow.ring", 0, 0, 0, 1)],
                        "$description": "Menus, popovers, dialogs. Negative spread tucks the ambient layer; the ring shows only in dark."},
        },
    }}


def motion_tokens():
    durations = [0, 50, 100, 150, 200, 300, 400, 500]
    motion = {
        "duration": {
            "$type": "duration",
            "$description": "Duration ladder in the 100-300ms band (L09 A1 row 5, DC-L04-20).",
            **{str(d): {"$value": {"value": d, "unit": "ms"}} for d in durations},
            "instant": {"$value": A("motion.duration.0")},
            "micro": {"$value": A("motion.duration.100"), "$description": "Hover, press feedback, color changes."},
            "short": {"$value": A("motion.duration.150"), "$description": "Exits, tooltips (exit ~75% of enter, DC-L04-24)."},
            "medium": {"$value": A("motion.duration.200"), "$description": "Menus and popovers entering."},
            "long": {"$value": A("motion.duration.300"), "$description": "Dialogs and side panels entering."},
            "xlong": {"$value": A("motion.duration.400"), "$description": "Full-screen transitions only."},
        },
        "easing": {
            "$type": "cubicBezier",
            "$description": "Four curves (DC-L04-21). Linear only for spinners and progress.",
            "standard": {"$value": [0.2, 0, 0, 1], "$description": "Moving and morphing on screen."},
            "enter": {"$value": [0, 0, 0, 1], "$description": "Entering: strong decelerate."},
            "exit": {"$value": [0.3, 0, 1, 1], "$description": "Leaving: accelerate out of the way."},
            "linear": {"$value": [0, 0, 1, 1], "$description": "Spinners and progress only."},
        },
    }
    return {"motion": motion}


def motion_transitions(context):
    reduced = context == "reduced"
    t = lambda dur, ease, d: {"$value": {"duration": A(f"motion.duration.{dur}"), "delay": {"value": 0, "unit": "ms"},
                                         "timingFunction": A(f"motion.easing.{ease}")}, "$description": d}
    if reduced:
        body = {
            "feedback": t("micro", "standard", "Unchanged: color and opacity feedback stays."),
            "enter": t("micro", "standard", "Fade only: components drop translate and scale in this context (DC-L04-25)."),
            "exit": t("micro", "standard", "Fade only (DC-L04-25)."),
        }
    else:
        body = {
            "feedback": t("micro", "standard", "Hover and press feedback."),
            "enter": t("medium", "enter", "Popovers and menus entering."),
            "exit": t("short", "exit", "Popovers and menus leaving (shorter than enter, DC-L04-24)."),
        }
    return {"motion": {"transition": {
        "$type": "transition",
        "$description": f"Semantic transitions, {context} motion (DC-L04-24, DC-L04-25; reduced motion as a token mode).",
        **body,
    }}}


# ---------------------------------------------------------------- resolver

RESOLVER = {
    "name": "Starter design system",
    "version": "2025.10",
    "description": "DTCG Resolver Module 2025.10. Three orthogonal modifiers (no two set the same token): theme x density x motion = 8 permutations (S-L07-004, DC-L07-15, DC-L07-17).",
    "sets": {
        "foundation": {
            "description": "Primitives and mode-independent semantics.",
            "sources": [{"$ref": "color.primitives.tokens.json"}, {"$ref": "spacing.tokens.json"},
                        {"$ref": "radius.tokens.json"}, {"$ref": "typography.tokens.json"},
                        {"$ref": "elevation.tokens.json"}, {"$ref": "motion.tokens.json"}],
        }
    },
    "modifiers": {
        "theme": {"description": "Color scheme. Dark is a separate mapping, not an inversion (DC-L01-18).",
                  "contexts": {"light": [{"$ref": "color.light.tokens.json"}], "dark": [{"$ref": "color.dark.tokens.json"}]},
                  "default": "light"},
        "density": {"description": "Semantic spacing density; primitives and target minimums never change (DC-L03-11).",
                    "contexts": {"comfortable": [{"$ref": "spacing.comfortable.tokens.json"}],
                                 "compact": [{"$ref": "spacing.compact.tokens.json"}]},
                    "default": "comfortable"},
        "motion": {"description": "Reduced motion as a token mode (DC-L04-25).",
                   "contexts": {"standard": [{"$ref": "motion.standard.tokens.json"}],
                                "reduced": [{"$ref": "motion.reduced.tokens.json"}]},
                   "default": "standard"},
    },
    "resolutionOrder": [{"$ref": "#/sets/foundation"}, {"$ref": "#/modifiers/theme"},
                        {"$ref": "#/modifiers/density"}, {"$ref": "#/modifiers/motion"}],
}


# ---------------------------------------------------------------- contrast claims

def contrast_pairs():
    """Pairs the semantic layer promises. check_contrast.py recomputes each ratio from the token files."""
    text_on = {
        "color.text.primary": ["color.surface.base", "color.surface.raised", "color.surface.sunken", "color.surface.overlay",
                               "color.bg.neutral.subtle", "color.bg.neutral.subtleHover", "color.bg.neutral.subtlePressed", "color.bg.accent.subtle"],
        "color.text.secondary": ["color.surface.base", "color.surface.raised", "color.surface.sunken", "color.surface.overlay", "color.bg.neutral.subtle"],
        "color.text.tertiary": ["color.surface.base", "color.surface.raised", "color.surface.sunken", "color.surface.overlay"],
        "color.text.accent": ["color.surface.base", "color.surface.raised", "color.surface.sunken", "color.bg.accent.subtle"],
        "color.text.onAccent": ["color.bg.accent.bold", "color.bg.accent.boldHover", "color.bg.accent.boldPressed"],
        "color.text.inverse": ["color.bg.inverse"],
    }
    for s in ("success", "warning", "danger", "info"):
        text_on[f"color.text.{s}"] = ["color.surface.base", "color.surface.raised", f"color.bg.{s}.subtle"]
        text_on[f"color.text.on{s.title()}"] = [f"color.bg.{s}.bold", f"color.bg.{s}.boldHover", f"color.bg.{s}.boldPressed"]
    non_text = {
        "color.border.strong": ["color.surface.base", "color.surface.raised", "color.surface.sunken", "color.surface.overlay"],
        "color.border.focus": ["color.surface.base", "color.surface.raised", "color.surface.sunken", "color.surface.overlay", "color.bg.neutral.subtle"],
        "color.bg.accent.bold": ["color.surface.base", "color.surface.raised"],
        "color.icon.default": ["color.surface.base", "color.surface.raised", "color.bg.neutral.subtle"],
    }
    pairs = []
    for mode in ("light", "dark"):
        for fg, bgs in text_on.items():
            for bg in bgs:
                pairs.append({"mode": mode, "fg": fg, "bg": bg, "min": 4.5, "kind": "text (WCAG 1.4.3 AA)"})
        for fg, bgs in non_text.items():
            for bg in bgs:
                pairs.append({"mode": mode, "fg": fg, "bg": bg, "min": 3.0, "kind": "non-text (WCAG 1.4.11 AA)"})
    return pairs


# ---------------------------------------------------------------- main

def write(name, data):
    path = os.path.join(HERE, name)
    with open(path, "w") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
        f.write("\n")


def main():
    global RAMPS, RING_HEX
    prims, RAMPS = build_ramps()
    RING_HEX = RAMPS["neutral.dark.12"]
    write("color.primitives.tokens.json", prims)
    write("color.light.tokens.json", semantic_color("light"))
    write("color.dark.tokens.json", semantic_color("dark"))
    write("spacing.tokens.json", spacing_primitives())
    write("spacing.comfortable.tokens.json", spacing_semantic("comfortable"))
    write("spacing.compact.tokens.json", spacing_semantic("compact"))
    write("radius.tokens.json", radius_tokens())
    write("typography.tokens.json", typography_tokens())
    write("elevation.tokens.json", elevation_tokens())
    write("motion.tokens.json", motion_tokens())
    write("motion.standard.tokens.json", motion_transitions("standard"))
    write("motion.reduced.tokens.json", motion_transitions("reduced"))
    write("design-system.resolver.json", RESOLVER)
    write("contrast-pairs.json", {"$description": "Contrast claims for the semantic layer. Ratios are filled in and verified by check_contrast.py.",
                                  "standard": "WCAG 2.2 AA (DC-L01-22, L09 A1 row 11)", "pairs": contrast_pairs()})
    print("wrote tokens; ramps:")
    for hue in HUES:
        for scheme in ("light", "dark"):
            print(f"  {hue:8s} {scheme:5s}", " ".join(RAMPS[f"{hue}.{scheme}.{i}"] for i in range(1, 13)))


if __name__ == "__main__":
    main()
