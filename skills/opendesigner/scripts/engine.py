#!/usr/bin/env python3
"""OpenDesigner engine: turns interview answers into a validated, exported design system.

Standard library only, Python 3.10+, no network. Every number it produces comes from
`references/levers.json` (the machine-readable twin of synthesis/LEVERS.md) or from a rule
cited inline with a Decision Card (DC-Lxx-nn) or source id (S-Lxx-nnn). `[inferred]` marks
choices this engine makes where the research gives a range or a direction but not a value.

Commands (run from the user's project; state lives in ./opendesigner/ unless --dir is given):
    engine.py init [--name "Acme"] [--from path/to/state.json]
    engine.py sketch [--brand HEX] [--audience dense|regular|large] [--platforms web,ios] [--feel playful,...] [--theme ...]
                                          Level 0: a complete, coarse system from about five answers
    engine.py set <dotted.path> <json-value> [--why "reason"] [--set-by S] [--lock] [--source-ref R]
                                          also: set path=value; set Q-shape-01 '"soft"'; a status word may start --why
    engine.py pick <question-id> <option-value> [--why "reason"]
    engine.py lock <dotted.path> | unlock <dotted.path>
    engine.py resolve                     effective dials, zoom per area and every derived parameter (JSON)
    engine.py generate                    state.json + levers.json -> tokens/ (DTCG 2025.10 + resolver)
    engine.py validate [--json]           contrast, targets, lint; exit 1 on errors, 0 with warnings
    engine.py export --format css|tailwind|figma|paper|swift|compose|dtcg|all
    engine.py design-md [--out DIR]       DESIGN.md and PRODUCT.md (project root when the state is ./opendesigner)
    engine.py preview [--open]            preview.html (every token plus a few components, light and dark)
    engine.py intake <measurements.json> [--accept] [--json]   reference values -> proposed dials (LEVERS E)
    engine.py review [--project P] [--strict] [--json]         hard-coded values that bypass tokens; stale DESIGN.md
    engine.py feedback "text" --kind gap|bug|confusing|idea [--from-journey]   local note + a pre-filled issue link (never posts)
    engine.py build                       generate + export all + design-md + preview + validate
    engine.py show <template> [--open]    a visual template filled with real values (palette, radius, option-gallery, ...)
    engine.py feel [words...]             how plain feel words (fun, calm, techy) map to the feel settings

When the person said yes to the private journey log (profile.tracking "on", see journey.py), the engine logs its own
steps there: answers and changed answers from set/pick/sketch, the finished sketch, validation errors, exports, reviews
and feedback. It never logs values, and it logs nothing without that yes.

Output layout inside the state directory (spec 7.1):
    state.json, decisions.md, feedback.md, preview.html,
    tokens/ primitives, semantic, semantic.color.<theme>, semantic.density.<mode>, motion.<standard|reduced> (.tokens.json),
            opendesigner.resolver.json, opendesigner.meta.json
    build/  css/tokens.css, tailwind/theme.css, figma/variables.json + figma/import/*.tokens.json, paper/tokens.json,
            swift/DesignTokens.swift, compose/DesignTokens.kt, dtcg/<name>.resolver.json
"""
from __future__ import annotations

import argparse
import copy
import datetime as _dt
import json
import math
import os
import re
import sys
import webbrowser

ENGINE_VERSION = "1.0.0"
HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_ROOT = os.path.dirname(HERE)
REFERENCES = os.path.join(SKILL_ROOT, "references")
NS = "opendesigner"  # $extensions key fixed by the spec (7.4, 5.6); DTCG recommends, not requires, reverse-domain keys
STATE_SCHEMA = "opendesigner-state/1"
DEFAULT_DIR = "opendesigner"

try:
    import journey  # scripts/journey.py: the private journey log (BRIEF requirement 18); optional
except ImportError:
    journey = None


def track(d, event, **kw):
    """Log a step to the journey log if the person said yes. Silent, and never stops design work."""
    if journey:
        journey.record(d, event, **kw)


# Paths that answer a sketch question without being answers.<Q-id> (zoom.md, level 0), and how a chosen value was given
ANSWER_PATHS = {"context.product": ("Q-scope-01", "free"), "raw.brandColor": ("Q-color-01", "free"), "macros": ("Q-brand-01", "option"),
                "hooks.H-logo.status": ("Q-brand-03", "option")}


# =============================================================================================
# Small utilities
# =============================================================================================

def clamp(x, lo, hi):
    return lo if x < lo else hi if x > hi else x


def rnd(x, nd=4):
    """Deterministic rounding for output (avoids -0.0)."""
    v = round(float(x), nd)
    return 0.0 if v == 0 else v


def round_half_up(x):
    return int(math.floor(x + 0.5))


def snap_to(value, steps):
    return min(steps, key=lambda s: (abs(s - value), s))


def dump_json(path, data, compact=False):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    text = (json.dumps(data, separators=(",", ":"), ensure_ascii=False) if compact else json.dumps(data, indent=2, ensure_ascii=False)) + "\n"
    write_text(path, text)


def write_text(path, text):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def read_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-") or "x"


def camel(parts):
    out = []
    for i, p in enumerate(parts):
        p = re.sub(r"[^A-Za-z0-9]+", " ", str(p)).strip()
        words = p.split()
        for j, w in enumerate(words):
            out.append(w.lower() if (i == 0 and j == 0) else w[:1].upper() + w[1:])
    s = "".join(out)
    return ("n" + s) if s[:1].isdigit() else s


def A(path):
    """DTCG curly-brace alias."""
    return "{" + path + "}"


def dim(v, unit="px"):
    return {"value": rnd(v, 3) if isinstance(v, float) else v, "unit": unit}


def ms(v):
    return {"value": int(v), "unit": "ms"}


# =============================================================================================
# Color math: OKLab/OKLCH (Ottosson), sRGB and Display P3, WCAG 2.2, APCA (advisory), CAM16 chroma
# =============================================================================================

def oklch_to_oklab(L, C, H):
    h = math.radians(H or 0.0)
    return L, C * math.cos(h), C * math.sin(h)


def oklab_to_lms_(L, a, b):
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    return l_ ** 3, m_ ** 3, s_ ** 3


def oklch_to_linear_srgb(L, C, H):
    l, m, s = oklab_to_lms_(*oklch_to_oklab(L, C, H))
    return (4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
            -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
            -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s)


def linear_srgb_to_oklch(r, g, b):
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l_, m_, s_ = (math.copysign(abs(v) ** (1 / 3), v) for v in (l, m, s))
    L = 0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_
    a = 1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_
    bb = 0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_
    C = math.hypot(a, bb)
    H = math.degrees(math.atan2(bb, a)) % 360
    return L, C, H


# linear sRGB -> linear Display P3 (both D65)
_SRGB_TO_XYZ = ((0.4123907993, 0.3575843394, 0.1804807884),
                (0.2126390059, 0.7151686788, 0.0721923154),
                (0.0193308187, 0.1191947798, 0.9505321522))
_XYZ_TO_P3 = ((2.4934969119, -0.9313836179, -0.4027107845),
              (-0.8294889696, 1.7626640603, 0.0236246858),
              (0.0358458302, -0.0761723893, 0.9568845240))
_P3_TO_XYZ = ((0.4865709486, 0.2656676932, 0.1982172852),
              (0.2289745641, 0.6917385218, 0.0792869141),
              (0.0000000000, 0.0451133819, 1.0439443689))


def _mat(m, v):
    return tuple(m[i][0] * v[0] + m[i][1] * v[1] + m[i][2] * v[2] for i in range(3))


def linear_srgb_to_linear_p3(rgb):
    return _mat(_XYZ_TO_P3, _mat(_SRGB_TO_XYZ, rgb))


def in_gamut(rgb, eps=1e-7):
    return all(-eps <= c <= 1 + eps for c in rgb)


def encode(c):
    c = clamp(c, 0.0, 1.0)
    return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055


def decode(v):
    return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4


def hex_of_linear(rgb):
    return "#" + "".join(f"{round_half_up(encode(c) * 255):02x}" for c in rgb)


def hex_to_rgb8(hx):
    hx = hx.strip().lstrip("#")
    if len(hx) == 3:
        hx = "".join(ch * 2 for ch in hx)
    return tuple(int(hx[i:i + 2], 16) for i in (0, 2, 4))


def hex_to_linear(hx):
    return tuple(decode(v / 255) for v in hex_to_rgb8(hx))


def hex_to_oklch(hx):
    return linear_srgb_to_oklch(*hex_to_linear(hx))


def oklch_to_hex(L, C, H):
    return hex_of_linear(oklch_to_linear_srgb(L, C, H))


def luminance(hx):
    """WCAG 2.2 relative luminance of an sRGB hex color (the values browsers and Figma display)."""
    r, g, b = (decode(v / 255) for v in hex_to_rgb8(hx))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_y(y1, y2):
    hi, lo = max(y1, y2), min(y1, y2)
    return (hi + 0.05) / (lo + 0.05)


def contrast(a, b):
    """WCAG 2.2 contrast ratio between two hex colors. No rounding: 4.499 fails 4.5 (DC-L01-22)."""
    return contrast_y(luminance(a), luminance(b))


def composite(fg_hex, alpha, bg_hex):
    """Alpha-composite in gamma-encoded sRGB, as browsers do."""
    f, b = hex_to_rgb8(fg_hex), hex_to_rgb8(bg_hex)
    return "#" + "".join(f"{round_half_up(alpha * x + (1 - alpha) * y):02x}" for x, y in zip(f, b))


def apca_lc(text_hex, bg_hex):
    """APCA-W3 0.0.98G-4g lightness contrast. Advisory only: WCAG 3 is a Working Draft (S-L01-021)."""
    def y(hx):
        r, g, b = (v / 255 for v in hex_to_rgb8(hx))
        yy = 0.2126729 * r ** 2.4 + 0.7151522 * g ** 2.4 + 0.0721750 * b ** 2.4
        return yy + (0.022 - yy) ** 1.414 if yy < 0.022 else yy
    yt, yb = y(text_hex), y(bg_hex)
    if abs(yb - yt) < 0.0005:
        return 0.0
    if yb > yt:
        sapc = (yb ** 0.56 - yt ** 0.57) * 1.14
        out = 0.0 if sapc < 0.1 else sapc - 0.027
    else:
        sapc = (yb ** 0.65 - yt ** 0.62) * 1.14
        out = 0.0 if sapc > -0.1 else sapc + 0.027
    return out * 100


# ---- CAM16 chroma (the "C" of Material's HCT), used to read the Colorfulness dial's HCT anchors.
# Viewing conditions follow Material Color Utilities' defaults (D65, L_A = 200/pi * Y(L*50)/100,
# background L* 50, average surround) so HCT chroma values from S-L01-010 mean the same thing here.
def _cam16_setup():
    wp = (95.047, 100.0, 108.883)
    y_l50 = 100 * ((50 + 16) / 116) ** 3
    la = (200 / math.pi) * y_l50 / 100
    yb = y_l50
    f, c, nc = 1.0, 0.69, 1.0
    m16 = ((0.401288, 0.650173, -0.051461), (-0.250268, 1.204414, 0.045854), (-0.002079, 0.048952, 0.953127))
    rgb_w = _mat(m16, wp)
    d = clamp(f * (1 - (1 / 3.6) * math.exp((-la - 42) / 92)), 0, 1)
    rgb_d = tuple(d * (100 / x) + 1 - d for x in rgb_w)
    k = 1 / (5 * la + 1)
    k4 = k ** 4
    fl = k4 * la + 0.1 * (1 - k4) ** 2 * (5 * la) ** (1 / 3)
    n = yb / wp[1]
    z = 1.48 + math.sqrt(n)
    nbb = 0.725 / n ** 0.2

    def adapt(x):
        p = (fl * abs(x) / 100) ** 0.42
        return math.copysign(400 * p / (p + 27.13), x)
    rgb_aw = [adapt(rgb_d[i] * rgb_w[i]) for i in range(3)]
    aw = (2 * rgb_aw[0] + rgb_aw[1] + 0.05 * rgb_aw[2]) * nbb
    return dict(m16=m16, rgb_d=rgb_d, adapt=adapt, nbb=nbb, ncb=nbb, aw=aw, c=c, z=z, nc=nc, n=n)


_CAM = _cam16_setup()


def cam16_hue_chroma(lin_rgb):
    """(hue, chroma) of a linear-sRGB color in CAM16 under Material's default viewing conditions."""
    xyz = tuple(100 * v for v in _mat(_SRGB_TO_XYZ, lin_rgb))
    rc = _mat(_CAM["m16"], xyz)
    ra, ga, ba = (_CAM["adapt"](rc[i] * _CAM["rgb_d"][i]) for i in range(3))
    a = (11 * ra - 12 * ga + ba) / 11
    b = (ra + ga - 2 * ba) / 9
    u = (20 * ra + 20 * ga + 21 * ba) / 20
    p2 = (40 * ra + 20 * ga + ba) / 20
    hue = math.degrees(math.atan2(b, a)) % 360
    ac = p2 * _CAM["nbb"]
    if ac <= 0:
        return hue, 0.0
    j = 100 * (ac / _CAM["aw"]) ** (_CAM["c"] * _CAM["z"])
    et = 0.25 * (math.cos(math.radians(hue) + 2) + 3.8)
    p1 = 50000 / 13 * et * _CAM["nc"] * _CAM["ncb"]
    if u + 0.305 <= 0:
        return hue, float("inf")  # far outside any display gamut; callers only need "too chromatic"
    t = p1 * math.hypot(a, b) / (u + 0.305)
    alpha = (t ** 0.9) * (1.64 - 0.29 ** _CAM["n"]) ** 0.73
    return hue, alpha * math.sqrt(j / 100)


def hct_chroma_of_hex(hx):
    return cam16_hue_chroma(hex_to_linear(hx))[1]


_MAXC_CACHE = {}


def max_chroma(L, H, gamut="srgb"):
    key = (round(L, 5), round(H, 3), gamut)
    if key in _MAXC_CACHE:
        return _MAXC_CACHE[key]
    lo, hi = 0.0, 0.45
    for _ in range(28):
        mid = (lo + hi) / 2
        rgb = oklch_to_linear_srgb(L, mid, H)
        if gamut == "p3":
            rgb = linear_srgb_to_linear_p3(rgb)
        if in_gamut(rgb):
            lo = mid
        else:
            hi = mid
    _MAXC_CACHE[key] = lo
    return lo


def oklch_chroma_for_hct(hct_c, L, H):
    """OKLCH chroma that has the given CAM16 (HCT) chroma at this OKLCH lightness and hue."""
    if hct_c <= 0:
        return 0.0
    lo, hi = 0.0, 0.45
    for _ in range(18):
        mid = (lo + hi) / 2
        if cam16_hue_chroma(oklch_to_linear_srgb(L, mid, H))[1] < hct_c:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def y_of_oklch(L, C, H):
    r, g, b = (clamp(v, 0, 1) for v in oklch_to_linear_srgb(L, C, H))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


# =============================================================================================
# Levers: load and evaluate the dial maps in levers.json
# =============================================================================================

_LEVERS = None


def levers():
    global _LEVERS
    if _LEVERS is None:
        path = os.path.join(REFERENCES, "levers.json")
        if not os.path.exists(path):  # running from the research repo before the skill copy exists
            alt = os.path.join(SKILL_ROOT, "..", "..", "synthesis", "levers.json")
            path = alt if os.path.exists(alt) else path
        _LEVERS = read_json(path)
    return _LEVERS


def lever_index():
    idx = {}
    for d in levers()["dials"]:
        for drv in d["drives"]:
            idx[drv["param"]] = dict(drv, dial=d["id"])
    return idx


def eval_map(m, x):
    """Evaluate a levers.json map at dial value x (0-100). Bands are inclusive; anchors interpolate."""
    if m["kind"] == "bands":
        xi = int(round(x))
        for lo, hi, val in m["bands"]:
            if lo <= xi <= hi:
                return copy.deepcopy(val)
        return copy.deepcopy(m["bands"][-1][2])
    pts = m["points"]
    if x <= pts[0][0]:
        return copy.deepcopy(pts[0][1])
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if x0 <= x <= x1:
            if isinstance(y0, (int, float)) and isinstance(y1, (int, float)):
                t = 0 if x1 == x0 else (x - x0) / (x1 - x0)
                return y0 + t * (y1 - y0)
            if isinstance(y0, dict) or isinstance(y1, dict):
                return _interp_tint(x, x0, y0, x1, y1)
            # "max" anchor (gamut maximum): numeric stand-in large enough to always clamp to gamut
            y0n = 120.0 if y0 == "max" else y0
            y1n = 120.0 if y1 == "max" else y1
            t = 0 if x1 == x0 else (x - x0) / (x1 - x0)
            return y0n + t * (y1n - y0n)
    return copy.deepcopy(pts[-1][1])


def _interp_tint(x, x0, y0, x1, y1):
    """Warmth anchors: linear on chroma between neighbouring anchors; hue from the non-zero side."""
    t = 0 if x1 == x0 else (x - x0) / (x1 - x0)
    c = y0["c"] + t * (y1["c"] - y0["c"])
    h = y0["h"] if y0.get("h") is not None and (y1.get("h") is None or t < 0.5) else y1.get("h")
    if h is None:
        h = y0.get("h")
    return {"c": c, "h": h}


# =============================================================================================
# State: defaults, dial resolution (presets, coupling, macros), derived parameters
# =============================================================================================

POSTURE = ("expression", "brandPresence", "density")
CHARACTER = ("energy", "roundness", "depth", "colorfulness", "warmth")
DIALS = POSTURE + CHARACTER

HOOK_STATUSES = ["pending", "have", "commissioning", "tool", "open-library", "placeholder", "not-needed"]
SET_BY = ["chosen", "confirmed_default", "auto_default", "assumed", "delegated", "reference", "asset"]  # spec 7.9
SET_BY_ALIASES = {"confirmed": "chosen", "default": "confirmed_default", "pending": "assumed"}
FALLBACK_HOOKS = [
    ("H-logo", "Logo, wordmark, symbol, lockups", "Q-brand-03"), ("H-appicon", "App icon", "Q-icon-06"),
    ("H-favicon", "Favicon set", "Q-brand-03"), ("H-icons", "Custom icons, pictograms, spot icons", "Q-icon-01"),
    ("H-illus", "Illustration, characters, empty-state art", "Q-img-04"),
    ("H-photo", "Photography and art direction", "Q-img-01"), ("H-type", "Brand typeface files", "Q-type-02"),
    ("H-color", "Fixed brand colors", "Q-color-01"), ("H-motion", "Motion signature and rich media", "Q-img-06"),
    ("H-motif", "Graphic devices, patterns, textures, brand gradients", "Q-img-07"),
    ("H-sound", "UI sounds and sonic logo", "Q-motion-08"), ("H-haptic", "Custom haptic patterns", "Q-motion-09"),
    ("H-voice", "Voice and tone guide", "Q-voice-01"), ("H-brandbook", "Brand guidelines PDF", "Q-ref-01"),
]


def hook_catalog():
    path = os.path.join(REFERENCES, "hooks.json")
    if os.path.exists(path):
        try:
            data = read_json(path)
            out = [(h["id"], h.get("name", h["id"]), (h.get("questions") or [None])[0])
                   for h in data.get("hooks", []) if h.get("kind") == "asset"]
            if out:
                return out
        except (ValueError, KeyError):
            pass
    return FALLBACK_HOOKS


DEFAULT_COMPONENTS = [  # Q-comp-02 default "core-25": the 25 components in 8-10 of the 10 benchmark systems (DC-L08-01)
    "button", "text-field", "textarea", "select", "checkbox", "radio", "switch", "slider", "tabs", "tooltip",
    "popover", "dialog", "menu", "progress-bar", "spinner", "banner", "badge", "avatar", "card", "list",
    "table", "link", "breadcrumbs", "side-navigation", "accordion",
]


def default_state(name="Untitled design system"):
    raw = {r["id"]: copy.deepcopy(r["default"]) for r in levers()["raw"]}
    raw.update({
        "brandColor": None, "primaryActionColor": None, "focusColor": None, "neutralBase": None,
        "secondaryColors": [], "contrastTarget": "AA", "textFace": "system", "displayFace": "=textFace",
        "monoFace": "ui-monospace", "baseSize": None, "spaceUnit": 4, "platforms": ["web"],
        "inputs": ["pointer", "touch"], "productType": "work-tool", "marketingSurfaces": False,
        "scripts": ["Latn"], "domain": None, "defaultTheme": "system",
    })
    # brandExact on by default: a person's own brand hex that passes the contrast target stays exact (U5 F10, F3)
    raw["flags"] = {"brandExact": True, "tintTowardBrand": False, "motionOff": False, "darkMode": True, "p3": True}
    return {
        "$schema": STATE_SCHEMA,
        "schema_version": 1,
        "engine_version": ENGINE_VERSION,
        "levers_version": f"{levers().get('schema')} {levers().get('date')}",
        "mode": "standard",
        "name": name,
        "summary": "",
        "context": {"product": "", "audience": "", "surfaces": [], "entryPath": "", "memorable": "", "scope": {"in": [], "out": []},
                    "constraints": [], "team": ""},
        "dials": {d: None for d in DIALS},
        "preset": None,
        "macros": [],
        "raw": raw,
        "overrides": {},
        "answers": {},
        "principles": [],
        "components": {"base": None, "inventory": list(DEFAULT_COMPONENTS), "notes": {}},
        "hooks": {hid: {"status": "pending", "name": n, "question": q, "files": [], "note": ""} for hid, n, q in hook_catalog()},
        "zoom": {},
        "profile": {"voice": "plain"},
        "blocks": {},
        "references": {},
        "taste": {},
        "hashes": {},
        "exports": {"prefix": "ds", "figmaPlan": "professional", "tailwindReset": True},
        "locks": [],
    }


def merge_defaults(state):
    """Fill any keys missing from an older or hand-written state with defaults (never overwrites)."""
    base = default_state(state.get("name", "Untitled design system"))

    def fill(dst, src):
        for k, v in src.items():
            if k not in dst:
                dst[k] = copy.deepcopy(v)
            elif isinstance(v, dict) and isinstance(dst[k], dict) and k not in ("overrides", "answers", "notes"):
                fill(dst[k], v)
    fill(state, base)
    return state


def dial_value(v):
    """Dials are stored as {value, set_by, detached} (spec 7.10); plain numbers are accepted too."""
    if isinstance(v, dict):
        return v.get("value")
    return v


def answer_value(v):
    if isinstance(v, dict) and "value" in v:
        return v["value"]
    return v


def _macro_list(state):
    out = []
    for m in state.get("macros") or []:
        if isinstance(m, str):
            out.append((m, 1.0))
        elif isinstance(m, dict) and m.get("id"):
            out.append((m["id"], float(m.get("strength", 1.0))))
    return out


DEFAULT_PRESET = "flat2"  # Q-dir-01's default_value (references/questions.json); applies until Q-dir-01 is answered


def effective_preset(state):
    """(preset id, is_default). An unanswered Q-dir-01 takes its default like any other question (spec 7.9)."""
    if state.get("preset"):
        return state["preset"], False
    if "Q-dir-01" in (state.get("answers") or {}):
        return None, False
    return DEFAULT_PRESET, True


def resolve_dials(state):
    """Effective dial values. Order: explicit value > preset > coupling/default; then macro offsets on
    untouched dials; clamp 0-100. Touching a dial detaches it from coupling and macros (LEVERS A0, A9)."""
    L = levers()
    explicit = {k: dial_value(v) for k, v in (state.get("dials") or {}).items() if dial_value(v) is not None}
    pid, _default = effective_preset(state)
    preset = next((p for p in L["presets"] if p["id"] == pid), None) if pid else None
    macros = {m["id"]: m for m in L["macros"]}
    offsets, pushes = {}, {}
    for mid, strength in _macro_list(state):
        m = macros.get(mid)
        if not m:
            continue
        for dial, off in m["offsets"].items():
            offsets[dial] = offsets.get(dial, 0) + off * strength
            pushes.setdefault(dial, []).append((mid, off * strength))
    conflicts = []
    for dial, lst in pushes.items():
        if any(o > 0 for _, o in lst) and any(o < 0 for _, o in lst):
            conflicts.append({"dial": dial, "macros": [m for m, _ in lst],
                              "rule": "macroRules.conflict: show the conflict, do not average silently (L06 4.2)"})
    src, out = {}, {}

    def base(d, fallback):
        if d in explicit:
            src[d] = "set"
            return float(explicit[d])
        if preset and d in preset["dials"]:
            src[d] = f"preset:{preset['id']}"
            return float(preset["dials"][d])
        src[d] = "coupled" if d in ("energy", "roundness", "colorfulness", "depth") else "default"
        return float(fallback)

    def fin(d, v):
        if d not in explicit and d in offsets:
            v += offsets[d]
            src[d] += "+macros"
        out[d] = int(round(clamp(v, 0, 100)))

    for d in POSTURE:
        fin(d, base(d, 50))
    e, dn = out["expression"], out["density"]
    fin("energy", base("energy", 50 + 0.5 * (e - 50)))
    fin("roundness", base("roundness", 50 + 0.5 * (e - 50) - 0.2 * max(0, dn - 50)))
    fin("colorfulness", base("colorfulness", 50 + 0.5 * (e - 50) + 0.3 * (out["energy"] - 50)))
    floor = int((L.get("macroRules") or {}).get("brandFloor", {}).get("colorfulness", 36))
    if state["raw"].get("brandColor") and "colorfulness" not in explicit and out["colorfulness"] < floor:
        out["colorfulness"] = floor  # a brand color never disappears behind feel words or presets (levers macroRules.brandFloor)
        src["colorfulness"] += "+brand floor"
    dep = base("depth", 40 + 0.5 * (e - 50))
    fin("depth", dep)
    materials_ok = e > 60 and any(p in ("ios", "ipados", "macos", "visionos", "windows")
                                  for p in state["raw"].get("platforms", []))
    if src["depth"].startswith("coupled") and out["depth"] > 80 and not materials_ok:
        out["depth"] = 80  # coupling rule: materials band only if expression > 60 and platform supports it
    fin("warmth", base("warmth", 50))
    return out, src, conflicts


def derive_params(state, dials):
    """Evaluate every levers.json drive at the effective dials, then apply overrides (DC-L16-14)."""
    params, meta = {}, {}
    for pid, drv in lever_index().items():
        v = eval_map(drv["map"], dials[drv["dial"]])
        params[pid] = v
        meta[pid] = {"dial": drv["dial"], "evidence": drv.get("evidence", []), "inferred": drv.get("inferred", False)}
    raw = state["raw"]
    # density band value may depend on product type
    bs = params["type.baseSize.web"]
    if isinstance(bs, dict):
        params["type.baseSize.web"] = bs.get(raw.get("productType") or "work-tool", bs.get("content", 16))
    # ratio capped by density (LEVERS B6)
    cap = params.get("type.ratioCap")
    if cap:
        params["type.ratio"] = min(params["type.ratio"], cap)
    for k, v in (state.get("overrides") or {}).items():
        params[k] = v
        meta.setdefault(k, {})["override"] = True
    return params, meta


# =============================================================================================
# Color: contrast-indexed 12-step ramps in OKLCH, separate light and dark ramps (LEVERS B1-B5)
# =============================================================================================

STEP_JOBS = {1: "app background", 2: "subtle background", 3: "component background", 4: "component hover",
             5: "component pressed or selected", 6: "subtle border", 7: "interactive border (decorative)",
             8: "strong border, focus, 3:1 boundary", 9: "solid fill (peak chroma)", 10: "solid hover, tertiary text",
             11: "low-contrast text", 12: "high-contrast text"}
# Chroma curve as a fraction of the peak (peak at step 9, falling toward both ends; Radix pattern S-L01-002).
ACCENT_CURVE_LIGHT = [0.04, 0.08, 0.17, 0.27, 0.37, 0.47, 0.57, 0.75, 1.0, 0.95, 0.85, 0.45]
ACCENT_CURVE_DARK = [0.08, 0.12, 0.23, 0.33, 0.43, 0.53, 0.67, 0.87, 1.0, 1.0, 0.93, 0.33]
NEUTRAL_CURVE = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.0, 0.9, 0.6]
MARGIN = 1.02         # solve 2% above each WCAG floor so 8-bit hex rounding never drops below it [inferred]
LIGHT_STEP1 = 1.02    # contrast of step 1 against white (build_tokens.py starter set) [inferred]
LIGHT_STEP7 = 1.65    # decorative border anchor (Radix gray7 #cecece is 1.6:1) [inferred]
DARK_STEP1_Y = 0.0075  # dark base luminance, inside the #121212-#1a1a1a band (DC-L01-19)
DARK_STEP7 = 2.0      # vs dark step 1 (Radix dark gray7 is 2.06:1 against gray1) [inferred]
DARK_ACCENT_CHROMA = 26 / 32  # Material 2025 TonalSpot primary chroma 32 light -> 26 dark (DC-L01-19)
# Status seeds: hue and whether the solid carries dark text (warning), as in Atlassian and Radix [inferred]
STATUS = {"success": (150, 0.55, "light"), "warning": (80, 0.80, "dark"), "danger": (27, 0.55, "light"),
          "info": (240, 0.55, "light")}


def target_y(ratio, y_ref, darker):
    """Luminance a foreground needs to reach `ratio` against y_ref (darker or lighter than it)."""
    y = (y_ref + 0.05) / ratio - 0.05 if darker else ratio * (y_ref + 0.05) - 0.05
    return clamp(y, 0.0, 1.0)


class Ramp:
    """One 12-step ramp for one mode. Steps are dicts with L, C, H, hex, y (WCAG luminance)."""

    def __init__(self, name, mode, hue, chroma_fn, text_on_solid="light", seed=None):
        self.name, self.mode, self.hue = name, mode, hue
        self.chroma_fn = chroma_fn  # (step, L) -> OKLCH chroma before gamut clamp
        self.text_on_solid = text_on_solid
        self.seed = seed
        self.steps = {}
        self.pinned = None
        self.p3 = {}

    def color_at(self, step, L):
        want = self.chroma_fn(step, L)
        C = min(want, max_chroma(L, self.hue))
        return C, want

    def set_L(self, step, L):
        C, want = self.color_at(step, L)
        hx = oklch_to_hex(L, C, self.hue)
        self.steps[step] = {"L": L, "C": C, "H": self.hue, "hex": hx, "y": luminance(hx), "want": want}

    def solve_y(self, step, y_target):
        lo, hi = 0.0, 1.0
        for _ in range(34):
            mid = (lo + hi) / 2
            C, _w = self.color_at(step, mid)
            if y_of_oklch(mid, C, self.hue) < y_target:
                lo = mid
            else:
                hi = mid
        self.set_L(step, (lo + hi) / 2)

    def y(self, step):
        return self.steps[step]["y"]

    def hexes(self):
        return [self.steps[i]["hex"] for i in range(1, 13)]


def build_ramp(name, mode, hue, chroma_fn, text_on_solid, cfg, neutral=None, seed=None):
    """Solve a ramp. cfg: text_min (4.5 or 7), c12 (primary text target), light/dark references.
    neutral: the already-solved neutral Ramp of this mode (None when building the neutral itself)."""
    r = Ramp(name, mode, hue, chroma_fn, text_on_solid, seed)
    light = mode == "light"
    tmin = cfg["text_min"] * MARGIN
    ref = neutral or r

    if light:
        r.solve_y(1, target_y(LIGHT_STEP1, 1.0, True))
        r.solve_y(7, target_y(LIGHT_STEP7, 1.0, True))
    else:
        if neutral is None:
            r.solve_y(1, cfg.get("dark_base_y", DARK_STEP1_Y))
        else:
            r.solve_y(1, target_y(1.03, neutral.y(1), False))
        r.solve_y(7, target_y(DARK_STEP7, ref.y(1), False))
    L1, L7 = r.steps[1]["L"], r.steps[7]["L"]
    for i in range(2, 7):  # steps 2-6 evenly spaced in lightness between step 1 and step 7 (see NOTES)
        r.set_L(i, L1 + (L7 - L1) * (i - 1) / 6)

    def refs(upto):
        ys = [r.y(i) for i in range(1, upto + 1)]
        if neutral is not None:
            ys += [neutral.y(i) for i in range(1, upto + 1)]
        if light:
            ys.append(1.0)  # white raised and overlay surfaces
            return min(ys)  # darkest background is the worst case for dark text
        return max(ys)      # lightest background is the worst case for light text

    # step 8 carries 3:1 boundaries on surfaces and on the neutral subtle fill (light: steps 1-3, dark: 1-5)
    r.solve_y(8, target_y(3.0 * MARGIN, refs(3 if light else 5), light))
    # step 9: solid fill. Light text (white) or dark text on it, chosen per hue (on-color-auto, S-L06-094)
    if light:
        if text_on_solid == "light":
            r.solve_y(9, target_y(tmin, 1.0, True))  # white text on the solid meets the text minimum (AA or AAA)
        else:
            dark_text_y = neutral.y(12) if neutral else 0.012
            y_min = target_y(tmin, dark_text_y, False)
            seed_L = seed[0] if seed else 0.8
            r.set_L(9, seed_L)
            if r.y(9) < y_min:
                r.solve_y(9, y_min)
        c9 = contrast_y(r.y(9), 1.0)
        y10 = target_y(c9 * 1.15, 1.0, True)
        if text_on_solid == "light":
            y10 = min(y10, target_y(tmin, refs(4), True))  # step 10 doubles as tertiary text
        else:
            y10 = max(y10, y_min)
        r.solve_y(10, y10)
        c10 = contrast_y(r.y(10), 1.0)
        if text_on_solid == "dark":  # pressed for a light solid: darker again, still carrying dark text (step "13")
            r.solve_y(13, max(target_y(c10 * 1.15, 1.0, True), y_min))
        r.solve_y(11, min(target_y(max(c10, contrast_y(r.y(9), 1.0)) * 1.22, 1.0, True),
                          target_y(tmin, refs(4), True)))
        r.solve_y(12, min(target_y(cfg["c12"], 1.0, True), target_y(7.0 * MARGIN, refs(5), True)))
    else:
        n1 = ref.y(1)
        y9 = max(target_y(tmin, n1, False), r.y(8) * 1.04)  # dark solids are lighter and carry dark text (Material 80/20)
        r.solve_y(9, y9)
        if seed is not None:
            seed_L = min(seed[0], 0.82)
            if seed_L > r.steps[9]["L"]:
                r.set_L(9, seed_L)
        c9 = contrast_y(r.y(9), n1)
        y10 = max(target_y(c9 * 1.15, n1, False), target_y(tmin, refs(4), False))
        r.solve_y(10, y10)
        c10 = contrast_y(r.y(10), n1)
        # dark neutral fills sit on steps 5-7, so secondary text must clear step 6 and primary text step 7
        y11 = target_y(tmin, refs(6), False)
        if text_on_solid == "light":
            y11 = max(y11, target_y(c10 * 1.2, n1, False))
        r.solve_y(11, y11)
        y12 = max(target_y(cfg["c12"], n1, False), target_y(7.0 * MARGIN, refs(5), False), target_y(tmin, refs(7), False))
        r.solve_y(12, min(1.0, max(y12, r.y(11) + 0.05)))  # step 12 always lighter than step 11
    return r


def neutral_alpha(hx, bg_hex, mode):
    """Radix-style alpha twin: the most transparent color that composites over bg to hx."""
    c, b = hex_to_rgb8(hx), hex_to_rgb8(bg_hex)
    if mode == "light":
        a = max((bb - cc) / bb if bb else 0 for cc, bb in zip(c, b))
    else:
        a = max((cc - bb) / (255 - bb) if bb < 255 else 0 for cc, bb in zip(c, b))
    a = clamp(math.ceil(a * 1000) / 1000, 0.001, 1.0)
    f = [clamp(round_half_up((cc - (1 - a) * bb) / a), 0, 255) for cc, bb in zip(c, b)]
    return "#" + "".join(f"{v:02x}" for v in f), a


def p3_variant(step):
    """Display P3 version of a step when sRGB clipped its chroma and P3 can hold more. Kept only when its
    luminance stays within 1.5% of the sRGB value, so every contrast pair still holds [inferred]."""
    L, H, want, C = step["L"], step["H"], step["want"], step["C"]
    if want - C < 0.01:
        return None
    cp3 = min(want, max_chroma(L, H, "p3"))
    if cp3 - C < 0.01:
        return None
    lin = oklch_to_linear_srgb(L, cp3, H)
    y = 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]
    if step["y"] <= 0 or abs(y - step["y"]) / step["y"] > 0.015:
        return None
    p3 = linear_srgb_to_linear_p3(lin)
    comps = [rnd(encode(clamp(v, 0, 1)), 4) for v in p3]
    return {"colorSpace": "display-p3", "components": comps, "oklch": [rnd(L, 4), rnd(cp3, 4), rnd(H, 2)]}


# Visible states (U5 F24): hover and pressed differ from their solid by at least these WCAG contrast ratios, and still
# carry the on-color text at the text minimum. Radix steps 9 to 10 are about 1.1:1; 1.15 and 1.3 keep them visible [inferred].
STATE_MIN = {"hover": 1.15, "pressed": 1.3}
NEUTRAL_TINTS = {"pure": (0.0, 0.0), "cool": (0.012, 255.0), "warm": (0.010, 70.0)}  # [inferred] mid-step tints near Warmth 25 / 75
DARK_BASES = {"black": 0.0, "near-black": DARK_STEP1_Y, "charcoal": 0.0194, "dimmed": 0.026}  # #000, #121212-#1a1a1a, #262626, dimmed
HARMONY = {"triadic": (60, -60), "analogous": (30, -30), "complementary": (180, 120)}  # accent2 / accent3 hue offsets [inferred]


def _state_y(y_base, ratio, darker):
    return (y_base + 0.05) / ratio - 0.05 if darker else ratio * (y_base + 0.05) - 0.05


def fit_states(r, on_y, tmin):
    """Re-solve hover (step 10) and pressed (step 13, 'solid-pressed') from the solid (step 9): each at least STATE_MIN apart
    from it, in the ramp's usual direction when that keeps the on-color text at tmin, else the other way. Steps 11 and 12
    (text) are then kept in order past the hover, which only raises their contrast."""
    light = r.mode == "light"
    y9 = r.y(9)
    prefer_darker = light
    chosen = {}
    for step, key in ((10, "hover"), (13, "pressed")):
        k = STATE_MIN[key] * 1.03  # solve 3% above the minimum so 8-bit rounding never lands under it
        pick = None
        for darker in (prefer_darker, not prefer_darker):
            y = _state_y(y9, k, darker)
            if 0.0 <= y <= 1.0 and contrast_y(y, on_y) >= tmin:
                pick = y
                break
        if pick is None:  # neither way keeps both: keep the text readable and move as far as that allows
            cands = [(_state_y(y9, k, d), d) for d in (True, False)]
            cands = [(clamp(y, 0.0, 1.0), d) for y, d in cands]
            pick = max(cands, key=lambda c: (contrast_y(c[0], on_y) >= tmin, contrast_y(c[0], y9)))[0]
        r.solve_y(step, pick)
        chosen[step] = pick
    if r.text_on_solid == "light" and light:
        if r.y(11) >= r.y(10):
            r.solve_y(11, _state_y(r.y(10), 1.1, True))
        if r.y(12) >= r.y(11):
            r.solve_y(12, _state_y(r.y(11), 1.1, True))
    elif not light and r.y(11) <= r.y(10):
        r.solve_y(11, min(1.0, _state_y(r.y(10), 1.1, False)))
        if r.y(12) <= r.y(11):
            r.solve_y(12, min(1.0, r.y(11) + 0.05))
    return chosen


def solve_L(hue, chroma, y_target):
    """OKLCH lightness with the given luminance at this hue, chroma clamped to the sRGB gamut."""
    lo, hi = 0.0, 1.0
    for _ in range(34):
        mid = (lo + hi) / 2
        if y_of_oklch(mid, min(chroma, max_chroma(mid, hue)), hue) < y_target:
            lo = mid
        else:
            hi = mid
    L = (lo + hi) / 2
    C = min(chroma, max_chroma(L, hue))
    return L, C


def chart_colors(n, start_hue, chroma, bg_y, light):
    """n categorical chart colors (Q-color-19): hues spread from the brand hue in an order that keeps neighbours apart,
    each at least 3:1 against the page (WCAG 1.4.11), alternating two lightness levels so they differ without hue too
    (color-vision safety) [inferred ordering; Atlassian and Carbon keep a fixed order, S-L01-030, S-L01-056]."""
    order = [0, 180, 90, 270, 45, 225, 135, 315, 22.5, 202.5, 112.5, 292.5, 67.5, 247.5][:n]
    out = []
    for i, off in enumerate(order):
        h = (start_hue + off) % 360
        ratio = (3.2 if i % 2 == 0 else 4.8) * MARGIN
        L, C = solve_L(h, chroma, target_y(ratio, bg_y, light))
        out.append({"L": L, "C": C, "H": h, "hex": oklch_to_hex(L, C, h)})
    return out


def build_palette(state, params):
    raw = state["raw"]
    flags = raw.get("flags", {}) or {}
    aaa = raw.get("contrastTarget") == "AAA"
    text_min = 7.0 if aaa else 4.5
    peak = float(params["color.accentChroma.hct"])
    scheme = params["color.schemeVariant"]
    brand = raw.get("brandColor")
    placeholder = brand is None
    if brand:
        bL, bC, bH = hex_to_oklch(brand)
    else:
        bL, bC, bH = 0.55, 0.15, float(params.get("color.placeholderHue", 255))  # blue reads competent (S-L06-072)
    brand_hct = hct_chroma_of_hex(brand) if brand else 0.0
    exact = flags.get("brandExact") is not False  # on unless the person chose seed (Q-color-01)
    if exact and brand and scheme != "monochrome":
        peak = max(peak, min(brand_hct, 120.0))  # Material Fidelity: the ramp peaks at the brand's own chroma (S-L06-083)
    tint = params["color.neutral.tint.oklch"]
    n_c, n_h = float(tint.get("c") or 0.0), tint.get("h")
    nt = raw.get("neutralTint") or ("brand" if flags.get("tintTowardBrand") else None)
    if nt == "brand":
        n_h = bH
        n_c = max(n_c, 0.012)  # [inferred] minimum visible tint toward the brand hue (DC-L01-06: 0.01-0.03 at mid steps)
    elif nt in NEUTRAL_TINTS:
        n_c, n_h = NEUTRAL_TINTS[nt]
    if raw.get("neutralBase"):
        nL, nC, nH = hex_to_oklch(raw["neutralBase"])
        n_h, n_c = nH, min(max(nC, 0.0), 0.05)
    n_h = float(n_h if n_h is not None else 0.0)
    if n_c < 0.0005:
        n_c = 0.0

    def neutral_chroma(step, L):
        c = n_c * NEUTRAL_CURVE[(10 if step > 12 else step) - 1]
        return min(c, 0.008) if step in (1, 12) else c  # ramp ends keep c <= 0.008 (DC-L01-06)

    def accent_chroma_fn(peak_hct, hue, mode):
        # The dial's anchor is HCT chroma (S-L01-010). It is converted to OKLCH once, at the solid step's
        # typical lightness (L 0.55), and the step curve is applied in OKLCH. Applying the curve in HCT
        # would grey out steps 1-3: CAM16 gives even pure white a chroma of about 2.9 [inferred].
        curve = ACCENT_CURVE_LIGHT if mode == "light" else ACCENT_CURVE_DARK
        k = 1.0 if mode == "light" else DARK_ACCENT_CHROMA
        c_peak = oklch_chroma_for_hct(peak_hct, 0.55, hue) if peak_hct > 0 else 0.0

        def fn(step, L):
            return c_peak * k * curve[(10 if step > 12 else step) - 1]
        return fn

    dark_text_y = target_y(17.5 if aaa else 15.5, 1.0, True)  # neutral light 12, solved below to this target

    def solid_text_for(seed_hex, seed_L, pinned=False):
        """On-color auto (S-L06-094) with the brandAnchor rule (DC-L01-09): keep the seed's own lightness when some text
        color passes on it; white wins ties; below 3:1 with white the solid always carries dark text."""
        if seed_hex is None:
            return "light"
        cw = contrast(seed_hex, "#ffffff")
        if cw >= text_min * MARGIN:
            return "light"
        if cw < 3.0 or contrast_y(luminance(seed_hex), dark_text_y) >= text_min * MARGIN:
            return "dark"
        return "light"  # neither passes at the seed's lightness: darken the solid until white text passes

    passes_white = bool(brand) and contrast(brand, "#ffffff") >= text_min
    passes_dark = bool(brand) and contrast_y(luminance(brand), dark_text_y) >= text_min
    pin_ok = bool(brand and exact and (passes_white or passes_dark))

    # status hues stay recognizable at any colorfulness; Material's fixed error palette uses chroma 84 [inferred]
    status_peak = clamp(peak + 16, 48.0, 84.0)
    specs = []  # (name, hue, peak, text_on_solid, seed(L,C,H) or None, seed_hex)
    brand_tos = ("light" if passes_white else "dark") if pin_ok else solid_text_for(brand, bL)
    specs.append(("accent", bH, peak, brand_tos, (bL, bC, bH) if brand else None, brand))
    pac = raw.get("primaryActionColor")
    if pac:
        pL, pC, pH = hex_to_oklch(pac)
        specs.append(("action", pH, max(peak, hct_chroma_of_hex(pac)) if exact else peak, solid_text_for(pac, pL), (pL, pC, pH), pac))
    count = raw.get("accentCount")
    count = int(count) if isinstance(count, (int, float)) else int(params["color.accentCount"])
    off2, off3 = HARMONY.get(raw.get("accentHarmony") or "triadic", HARMONY["triadic"])
    sec = raw.get("secondaryColors") or []
    if count >= 2:
        if len(sec) >= 1:
            s1 = hex_to_oklch(sec[0])
            specs.append(("accent2", s1[2], max(peak, hct_chroma_of_hex(sec[0])) if exact else peak, solid_text_for(sec[0], s1[0]), s1, sec[0]))
        else:  # Material TonalSpot: tertiary hue +60, chroma 24/36 of primary [inferred mapping S-L01-010]
            specs.append(("accent2", (bH + off2) % 360, peak * 24 / 36, "light", None, None))
    if count >= 3:
        if len(sec) >= 2:
            s2 = hex_to_oklch(sec[1])
            specs.append(("accent3", s2[2], max(peak, hct_chroma_of_hex(sec[1])) if exact else peak, solid_text_for(sec[1], s2[0]), s2, sec[1]))
        else:
            specs.append(("accent3", (bH + off3) % 360, peak * 24 / 36, "light", None, None))
    status = dict(STATUS)
    if raw.get("statusSet") in ("discovery", "workflow"):
        status["discovery"] = (300, 0.55, "light")  # Atlassian discovery purple (S-L01-030)
    for sname, (h, sl, tos) in status.items():
        specs.append((sname, float(h), status_peak, tos, (sl, 0.15, float(h)), None))

    dark_base = DARK_BASES.get(raw.get("darkBase") or "", params.get("color.dark.baseY", DARK_STEP1_Y))
    ramps = {}
    for mode in ("light", "dark"):
        cfg = {"text_min": text_min, "c12": 17.5 if aaa else 15.5, "dark_base_y": dark_base}
        if mode == "dark":
            cfg["c12"] = 17.0 if aaa else 15.0
        neutral = build_ramp("neutral", mode, n_h, neutral_chroma, "light", cfg)
        ramps[("neutral", mode)] = neutral
        acfg = dict(cfg, c12=14.0 if aaa else 12.5)
        for name, hue, pk, tos, seed, seed_hex in specs:
            r = build_ramp(name, mode, hue, accent_chroma_fn(pk, hue, mode), tos, acfg, neutral=neutral, seed=seed)
            ramps[(name, mode)] = r
    # brand exact: the person's hex becomes the light-mode solid (container role, Material Fidelity)
    pinned = None
    if pin_ok:
        acc = ramps[("accent", "light")]
        pinned = 9
        acc.steps[pinned] = {"L": bL, "C": bC, "H": bH, "hex": brand.lower(), "y": luminance(brand), "want": bC}
        acc.pinned = pinned
    tmin_m = text_min * MARGIN
    for (name, mode), r in ramps.items():
        if name == "neutral":
            continue
        n = ramps[("neutral", mode)]
        on_y = (1.0 if r.text_on_solid == "light" else n.y(12)) if mode == "light" else n.y(1)
        fit_states(r, on_y, tmin_m)
    # nearest step to the brand color (documented anchor; bg.brand uses a step that carries its on-color)
    anchor = None
    if brand:
        acc = ramps[("accent", "light")]
        anchor = min(range(1, 13), key=lambda i: (abs(acc.steps[i]["L"] - bL), i))
    if flags.get("p3", True):
        for r in ramps.values():
            for i in list(r.steps):
                v = p3_variant(r.steps[i]) if r.name != "neutral" and not (r.pinned == i) and i <= 12 else None
                if v:
                    r.p3[i] = v
    charts = {}
    cp = raw.get("chartPalette")
    if cp in ("categorical-8", "categorical-14"):
        cc = clamp(oklch_chroma_for_hct(max(peak, 40.0), 0.6, bH), 0.08, 0.2)
        for mode in ("light", "dark"):
            n = ramps[("neutral", mode)]
            bg_y = n.y(1) if mode == "light" else n.y(2)
            charts[mode] = chart_colors(8 if cp == "categorical-8" else 14, bH, cc, bg_y, mode == "light")
    adjusted = None
    if brand and not pin_ok:
        acc = ramps[("accent", "light")]
        adjusted = acc.steps[9]["hex"]
    info = {"scheme": scheme, "peakHct": rnd(peak, 2), "brandHct": rnd(brand_hct, 2), "placeholderBrand": placeholder,
            "brandOklch": [rnd(bL, 4), rnd(bC, 4), rnd(bH, 2)], "neutralTint": {"c": rnd(n_c, 4), "h": rnd(n_h, 2)},
            "pinnedStep": pinned, "brandAnchorStep": anchor, "brandExact": exact,
            "brandPinFailed": bool(brand and exact and not pin_ok), "brandAdjustedTo": adjusted,
            "brandContrastWhite": rnd(contrast(brand, "#ffffff"), 2) if brand else None,
            "statusPeakHct": rnd(status_peak, 2), "textMin": text_min, "ramps": [s[0] for s in specs],
            "accentCount": count, "chart": {m: [c["hex"] for c in v] for m, v in charts.items()}}
    info["_chart"] = charts
    return ramps, info


# =============================================================================================
# Token assembly
# =============================================================================================

DENSITIES = ("spacious", "comfortable", "compact")
def space_multipliers(raw=None):
    """LEVERS B8 multiplier list parsed from levers.json; x24 (the 96 step) added per the spec (6.2, section 11).
    Q-space-02 swaps the curve (linear: even steps; geometric: doubling) and Q-space-07 adds a hairline or nudge steps."""
    m = re.search(r"\[([0-9.,\s]+)\]", levers()["formulas"]["space"]["ladder"])
    mult = [float(x) for x in m.group(1).split(",")] if m else [0, 0.5, 1, 1.5, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20]
    if 24 not in mult:
        mult.append(24.0)
    raw = raw or {}
    if raw.get("spaceLadder") == "linear":
        mult = [0, 0.5] + [float(x) for x in range(1, 17)]  # even steps (Tailwind, Fluent to 56, Primer to 48; S-L03-015)
    elif raw.get("spaceLadder") == "geometric":
        mult = [0, 0.5, 1, 2, 4, 8, 16, 24]
    extras = raw.get("spaceExtras") or []
    if "hairline" in extras:
        mult.append(0.25)
    if "nudges" in extras:
        mult += [1.5, 2.5]
    return sorted(set(float(x) for x in mult))
SNAP_RADII = [0, 2, 4, 6, 8, 12, 16, 20, 24, 28, 32]
FULL = 9999
SYSTEM_SANS = ["system-ui", "-apple-system", "Segoe UI", "Roboto", "Helvetica Neue", "Arial", "sans-serif"]
SYSTEM_MONO = ["ui-monospace", "SF Mono", "Menlo", "Consolas", "Liberation Mono", "monospace"]
SYSTEM_SERIF = ["ui-serif", "Georgia", "Cambria", "Times New Roman", "serif"]
SYSTEM_ROUNDED = ["ui-rounded", "SF Pro Rounded", "system-ui", "sans-serif"]
# Q-type-03 font style -> an open (SIL OFL, Google Fonts) face of that class, used when Q-type-01 is open-custom [inferred picks]
OPEN_FACES = {"neo-grotesque": "Inter", "geometric": "Plus Jakarta Sans", "humanist": "Source Sans 3", "serif": "Source Serif 4",
              "slab": "Roboto Slab", "rounded": "Nunito"}
# Open-licence faces (SIL OFL or Apache 2.0): usable on the web, in apps and self-hosted, so no licence scope is needed
OPEN_FONTS = {f.lower() for f in list(OPEN_FACES.values()) + [
    "Roboto", "Roboto Mono", "Roboto Flex", "Atkinson Hyperlegible", "JetBrains Mono", "IBM Plex Sans", "IBM Plex Serif", "IBM Plex Mono",
    "Noto Sans", "Noto Serif", "Open Sans", "Lato", "Montserrat", "Poppins", "Work Sans", "DM Sans", "DM Serif Display", "Manrope",
    "Figtree", "Geist", "Geist Mono", "Fira Sans", "Fira Code", "Public Sans", "Lexend", "Outfit", "Space Grotesk", "Sora", "Karla",
    "Rubik", "Merriweather", "Lora", "Playfair Display", "Source Code Pro", "Recursive", "Instrument Sans", "Onest", "Hanken Grotesk"]}


def _generic_face(name):
    return (not name or name in ("system", "=serif", "=rounded") or str(name).lower() in GENERIC_FONTS
            or str(name).lower().startswith(("ui-", "sf ", "sf pro")))


def font_faces(raw):
    """Which face each role uses and where its licence allows it (U5 F21). A brand face whose licence does not cover a
    platform falls back to the system font there: web in the tokens, apps in the Swift and Compose exports."""
    lic = raw.get("fontLicence") or {}
    cls = raw.get("fontClass")

    def resolve(v):
        if v == "=brandFace":
            return raw.get("brandFace") or "system"
        if v == "=openClass":
            return OPEN_FACES.get(cls or "neo-grotesque", "Inter")
        return v
    text = resolve(raw.get("textFace")) or "system"
    disp = raw.get("displayFace")
    disp = "=textFace" if disp in (None, "=textFace") else resolve(disp)
    if disp == "=textFace" and text == "system" and cls in ("serif", "slab", "rounded"):
        disp = "=rounded" if cls == "rounded" else "=serif"  # Q-type-03 with the device font: headings in the system serif or rounded

    def info(name):
        if isinstance(name, list):
            name = name[0] if name else "system"
        if name == "=textFace":
            return None
        if _generic_face(name) or str(name).lower() in OPEN_FONTS:
            return {"face": name, "web": True, "app": True, "selfHost": True, "open": True}
        rec = {"face": name, "web": lic.get("web"), "app": lic.get("app"), "selfHost": lic.get("selfHost"), "open": False}
        cut = [k for k in ("web", "app") if rec[k] is False]
        if cut:
            rec["note"] = f"{name} is not licensed for {' or '.join('apps' if k == 'app' else k for k in cut)}, so the system font is used there"
        return rec
    t = info(text)
    d = info(disp) or dict(t, face="=textFace")
    return {"text": t, "display": d}
TARGETS = {"pointer": 24, "touch": 44, "touch-android": 48, "remote": 66, "gaze": 60, "vehicle": 76}
TARGET_GAPS = {"pointer": 8, "touch": 12, "gaze": 16, "vehicle": 23, "remote": 16}
BREAKPOINTS = {"material": {"sm": 600, "md": 840, "lg": 1200, "xl": 1600},            # Material width classes (S-L03-025)
               "tailwind": {"sm": 640, "md": 768, "lg": 1024, "xl": 1280, "2xl": 1536},  # Tailwind (S-L03-016)
               "bootstrap": {"sm": 576, "md": 768, "lg": 992, "xl": 1200, "2xl": 1400}}  # Bootstrap (S-L03-018)
DEVICE_INPUTS = {"phone": "touch", "tablet-foldable": "touch", "watch": "touch", "wrist": "touch", "desktop-web": "pointer",
                 "tv": "remote", "car": "vehicle", "driving": "vehicle", "spatial": "gaze", "headset": "gaze"}


class Ctx:
    def __init__(self, state):
        self.state = merge_defaults(copy.deepcopy(state))
        self.raw = self.state["raw"]
        self.flags = self.raw.get("flags", {})
        self.dials, self.dial_src, self.conflicts = resolve_dials(self.state)
        self.params, self.pmeta = derive_params(self.state, self.dials)
        self.ramps, self.cinfo = build_palette(self.state, self.params)
        self.charts = self.cinfo.pop("_chart", {})
        self.modes = ["light", "dark"] if self.flags.get("darkMode", True) else ["light"]
        if self.raw.get("defaultTheme") == "dark" and "dark" not in self.modes:
            self.modes = ["dark"]
        self.notes = []
        self.used = {}  # param -> value actually used by a generator (recorded in meta)

    def P(self, name, computed):
        v = self.params[name] if name in (self.state.get("overrides") or {}) else computed
        self.used[name] = v
        return v

    def ramp(self, name, mode):
        return self.ramps[(name, mode)]


def color_value(step):
    L, C, H = step["L"], step["C"], step["H"]
    v = {"colorSpace": "oklch", "components": [rnd(L, 4), rnd(C, 4), rnd(H if C > 1e-4 else 0, 2)], "hex": step["hex"]}
    return v


def srgb_value(hx, alpha=None):
    v = {"colorSpace": "srgb", "components": [rnd(c / 255, 4) for c in hex_to_rgb8(hx)], "hex": hx.lower()}
    if alpha is not None and alpha < 1:
        v["alpha"] = rnd(alpha, 3)
    return v


def tok(value, desc=None, ext=None, type_=None):
    t = {"$value": value}
    if type_:
        t["$type"] = type_
    if desc:
        t["$description"] = desc
    if ext:
        t["$extensions"] = {NS: ext}
    return t


def build_color_primitives(ctx):
    color = {
        "$type": "color",
        "$description": "Primitive color ramps. Private tier: components use the semantic roles, never these (DC-L01-26).",
        "$extensions": {NS: {
            "method": "OKLCH, contrast-indexed, 12 steps, separate light and dark ramps, sRGB gamut-mapped by lowering chroma",
            "evidence": ["DC-L01-01", "DC-L01-02", "DC-L01-03", "DC-L01-05", "DC-L01-06", "DC-L01-18", "S-L01-002"],
            "stepJobs": {str(k): v for k, v in STEP_JOBS.items()},
            "scheme": ctx.cinfo["scheme"], "accentPeakHct": ctx.cinfo["peakHct"]}},
        "white": tok(srgb_value("#ffffff"), "Pure white: light raised and overlay surfaces, on-color text."),
        "black": tok(srgb_value("#000000"), "Pure black: dark-mode shadow base (DC-L04-12)."),
    }
    if ctx.raw.get("brandColor"):
        color["brand"] = {"seed": tok(srgb_value(ctx.raw["brandColor"]),
                                      "The brand color exactly as given. For logos and marketing; UI fills use color.bg.brand.")}
    if ctx.raw.get("focusColor"):
        color["focus"] = {"custom": tok(srgb_value(ctx.raw["focusColor"]), "Focus color given as a raw input (L09 M12).")}
    descs = {"neutral": "Neutral ramp; tint from the Warmth dial (DC-L01-06, S-L01-062).",
             "accent": "Accent ramp from the brand color's hue; chroma from the Colorfulness dial (S-L01-010).",
             "action": "Primary-action ramp from its own raw input (Primer pattern, S-L09-331).",
             "accent2": "Second accent (Colorfulness 60+ allows three accents, DC-L01-08).",
             "accent3": "Third accent (Colorfulness 60+ allows three accents, DC-L01-08).",
             "success": "Status: success. Always paired with an icon or label (DC-L01-15).",
             "warning": "Status: warning. The solid carries dark text (on-color-auto, S-L06-094).",
             "danger": "Status: danger. Always paired with an icon or label (DC-L01-15).",
             "info": "Status: info. Always paired with an icon or label (DC-L01-15).",
             "discovery": "Status: discovery, for new things (Atlassian purple, S-L01-030; Q-color-15)."}
    names = ["neutral"] + [n for n in ctx.cinfo["ramps"]]
    for name in names:
        group = {"$description": descs.get(name, name)}
        for mode in ("light", "dark"):
            r = ctx.ramp(name, mode)
            sub = {}
            for i in range(1, 13):
                ext = {}
                if r.pinned == i:
                    ext["pinned"] = "brand color kept exactly (flags.brandExact, S-L06-083)"
                if i in r.p3:
                    ext["p3"] = r.p3[i]
                sub[str(i)] = tok(color_value(r.steps[i]), STEP_JOBS[i], ext or None)
            if 13 in r.steps:
                sub["solid-pressed"] = tok(color_value(r.steps[13]), f"Pressed solid: at least {STATE_MIN['pressed']}:1 from step 9, "
                                                                     "still carrying its text (visible states, U5).")
            group[mode] = sub
        group["$extensions"] = {NS: {"textOnSolid": {m: ctx.ramp(name, m).text_on_solid for m in ("light", "dark")}}}
        color[name] = group
    alpha = {"$description": "Alpha twins of the neutral ramp over the page background (Radix and Atlassian pattern, DC-L01-07)."}
    for mode in ("light", "dark"):
        r = ctx.ramp("neutral", mode)
        bg = "#ffffff" if mode == "light" else r.steps[1]["hex"]
        sub = {}
        for i in range(2, 13):
            fx, a = neutral_alpha(r.steps[i]["hex"], bg, mode)
            sub[str(i)] = tok(srgb_value(fx, a), f"Composites to neutral {mode} {i} over {'white' if mode == 'light' else 'neutral dark 1'}.")
        alpha[mode] = sub
    color["neutral-alpha"] = alpha
    so = {"hover": 0.16, "focus": 0.16, "pressed": 0.32, "drag": 0.32} if ctx.raw.get("stateOpacity") == "atlassian" else \
        {"hover": 0.08, "focus": 0.10, "pressed": 0.10, "drag": 0.16}  # Atlassian 16/32% (S-L04-070) or Material (S-L04-003)
    opacity = {
        "$type": "number",
        "$description": "State and disabled opacities for colors unknown at design time (Material state layers, DC-L01-17).",
        "state": {k: tok(v) for k, v in so.items()},
        "disabled": {"container": tok(0.12), "content": tok(0.38)},
        "$extensions": {NS: {"evidence": ["DC-L01-17", "S-L01-005", "S-L01-064"]}},
    }
    return {"color": color}, {"opacity": opacity}


def _state_layer(base_hex, on_hex, ratio, start, tmin=4.5 * MARGIN):
    """Smallest see-through layer over a fill that moves it at least `ratio` away and keeps the on-color text readable
    (Q-color-20 overlay). The on-color layer comes first (Material state layers, DC-L01-17); when it would wash out the text,
    the opposite (black under white text, white under dark text) is used."""
    other = "#000000" if luminance(on_hex) > 0.5 else "#ffffff"
    for layer in (on_hex, other):
        a = start
        while a <= 0.6:
            hx = composite(layer, a, base_hex)
            if contrast(hx, base_hex) >= ratio * 1.01 and contrast(hx, on_hex) >= tmin:
                return hx, rnd(a, 2), layer
            a += 0.01
    return composite(other, 0.3, base_hex), 0.3, other


def build_color_semantic(ctx, mode):
    L = mode == "light"
    p = ctx.params
    raw = ctx.raw
    has = set(ctx.cinfo["ramps"])
    n = lambda s: A(f"color.neutral.{mode}.{s}")
    r = lambda name, s: A(f"color.{name}.{mode}.{s}")
    white = A("color.white")
    model = ctx.P("elevation.model", p["elevation.model"])
    # surfaces: dark raises surfaces by lightness (DC-L04-13); tonal light steps the page down one step
    if L:
        if model == "tonal" or raw.get("surfaceLayers") == "alternating":
            surf = {"sunken": n(3), "base": n(2), "raised": n(1), "overlay": white}
        else:
            surf = {"sunken": n(2), "base": n(1), "raised": white, "overlay": white}
    elif raw.get("darkBase") == "black":
        surf = {"sunken": n(1), "base": n(1), "raised": n(2), "overlay": n(3)}  # pure black page (OLED), Q-color-21
    else:
        surf = {"sunken": n(1), "base": n(2), "raised": n(3), "overlay": n(4)}
    nav = p["chrome.navTreatment"]
    brand_chrome = p["color.brandRole"] == "brand-chrome-allowed"
    if nav == "colored-if-expression-allows" and brand_chrome:
        surf_nav, nav_desc = r("accent", 9), "Colored navigation (Energy 67+ with brand chrome allowed by Expression 67+)."
    elif nav == "recessive":
        surf_nav, nav_desc = (n(2) if L else n(1)), "Recessive navigation, dimmer than content (Linear 2026, S-L06-067)."
    else:
        surf_nav, nav_desc = surf["base"], "Navigation on the page background."
    lt = lambda name: ctx.ramp(name, mode).text_on_solid
    on = lambda name: (white if lt(name) == "light" else n(12)) if L else n(1)
    on_hex = lambda name: ("#ffffff" if lt(name) == "light" else ctx.ramp("neutral", mode).steps[12]["hex"]) if L \
        else ctx.ramp("neutral", mode).steps[1]["hex"]
    overlay_states = raw.get("stateMethod") == "overlay"

    def states(name, desc):
        """bold, bold-hover, bold-pressed for a solid: shade steps, or see-through state layers (Q-color-20)."""
        base = tok(r(name, 9), desc)
        if overlay_states:
            b = ctx.ramp(name, mode).steps[9]["hex"]
            so = {"hover": 0.16, "pressed": 0.32} if raw.get("stateOpacity") == "atlassian" else {"hover": 0.08, "pressed": 0.10}
            tm = (7.0 if raw.get("contrastTarget") == "AAA" else 4.5) * MARGIN
            hv, ah, lh = _state_layer(b, on_hex(name), STATE_MIN["hover"], so["hover"], tm)
            pr, ap, lp = _state_layer(b, on_hex(name), STATE_MIN["pressed"], max(so["pressed"], ah + 0.02), tm)
            return (base, tok(srgb_value(hv), f"Hover: {lh} at {int(round(ah * 100))}% over the solid (state layer, DC-L01-17).",
                              {"stateLayer": {"over": r(name, 9), "color": lh, "alpha": ah}}),
                    tok(srgb_value(pr), f"Pressed: {lp} at {int(round(ap * 100))}% over the solid (state layer).",
                        {"stateLayer": {"over": r(name, 9), "color": lp, "alpha": ap}}))
        return (base, tok(r(name, 10), f"Hover: one step, at least {STATE_MIN['hover']}:1 from the solid (DC-L01-17)."),
                tok(r(name, "solid-pressed"), f"Pressed: at least {STATE_MIN['pressed']}:1 from the solid."))
    fs = raw.get("focusStyle") or "brand"
    focus_step = 9 if (lt("accent") == "light") else 11
    focus = (n(12) if fs in ("neutral", "two-tone") else (r("accent", focus_step) if L else r("accent", 11)))
    acc_b, acc_h, acc_p = states("accent", "Solid accent fill.")
    out = {
        "surface": {
            "sunken": tok(surf["sunken"], "Wells, code blocks, page gutters."),
            "base": tok(surf["base"], "The page background."),
            "raised": tok(surf["raised"], "Cards and panels on the page."),
            "overlay": tok(surf["overlay"], "Menus, popovers, dialogs; always with elevation.floating or elevation.overlay."),
            "nav": tok(surf_nav, nav_desc),
        },
        "text": {
            "primary": tok(n(12), "Body copy, headings, labels (guaranteed >= 7:1 on steps 1-5)."),
            "secondary": tok(n(11), "Supporting text (guaranteed >= the text minimum on surfaces and neutral fills 1-4)."),
            "tertiary": tok(n(10), "Captions and placeholders (still meets the text minimum on surfaces 1-4)."),
            "disabled": tok(n(8), "Disabled labels; exempt from contrast minimums (WCAG 1.4.3 exception)."),
            "inverse": tok(white if L else n(1), "Text on color.bg.inverse (tooltips, toasts)."),
            "link": tok(r("accent", 11), "Links. Underline them in running text so color is not the only cue."),
            "accent": tok(r("accent", 11), "Accent text and selected labels."),
            "on-accent": tok(on("accent"), "Text and icons on color.bg.accent.bold* (auto-picked light or dark, S-L06-094)."),
        },
        "bg": {
            "neutral": {
                "subtle": tok(n(3) if L else n(5), "Secondary buttons, chips, hovered rows."),
                "subtle-hover": tok(n(4) if L else n(6), "Hover: +1 step (DC-L01-17)."),
                "subtle-pressed": tok(n(5) if L else n(7), "Pressed or selected: +2 steps (DC-L01-17)."),
            },
            "accent": {
                "subtle": tok(r("accent", 3), "Selected rows, accent badges."),
                "subtle-hover": tok(r("accent", 4), "Hover on accent subtle fills."),
                "subtle-pressed": tok(r("accent", 5), "Pressed accent subtle fills."),
                "bold": acc_b, "bold-hover": acc_h, "bold-pressed": acc_p,
            },
            "disabled": tok(n(3) if L else n(4), "Disabled control fill."),
            "inverse": tok(n(12), "Tooltips and toasts: the inverted surface."),
            "field": tok((n(3) if L else n(4)) if raw.get("fieldStyle") == "filled" else surf["raised"],
                         "Text field fill: " + ("filled fields (Q-form-01, M3 filled)." if raw.get("fieldStyle") == "filled"
                                               else "outlined fields sit on the raised surface (Q-form-01).")),
        },
        "border": {
            "subtle": tok(n(6), "Dividers and card edges (decorative)."),
            "default": tok(n(7), "Outline buttons and table grids (decorative; the label carries meaning)."),
            "strong": tok(n(8), "Boundaries that are the only cue: inputs, checkboxes, switches (3:1, WCAG 1.4.11)."),
            "input": tok(n(8), "Text field and select borders (3:1, DC-L01-16)."),
            "focus": tok(focus, "Focus ring (3:1 against every surface, DC-L04-09)" + ({"neutral": "; neutral ring (Q-color-23).",
                                                                                         "two-tone": "; outer ring of a two-tone ring (Q-state-03)."}.get(fs, "."))),
            "accent": tok(r("accent", 8), "Selected card or accent outline."),
        },
        "icon": {
            "default": tok(n(11), "Icons beside text; same color as secondary text (DC-L05-08)."),
            "subtle": tok(n(10), "Decorative icons."),
            "accent": tok(r("accent", 11), "Selected and interactive icons."),
            "on-accent": tok(on("accent"), "Icons on solid accent fills."),
        },
    }
    softness = p["border.softness"]
    if softness == "strong-rules":
        out["border"]["subtle"] = tok(n(7), "Dividers (strong rules: Warmth 0-33, S-L06-067 inverse).")
        out["border"]["default"] = tok(n(8), "Outlines (strong rules).")
    elif softness == "soft":
        out["border"]["subtle"] = tok(n(5), "Dividers (soft borders: Warmth 67+, Linear 2026 S-L06-067).")
        out["border"]["default"] = tok(n(6), "Outlines (soft borders).")
    # primary action: monochrome schemes use the neutral ink (shadcn pattern); raw primaryActionColor its own ramp
    if ctx.cinfo["scheme"] == "monochrome" and "action" not in has:
        act = (tok(n(12), "Primary action (monochrome scheme: neutral ink, as shadcn/ui)."),
               tok(n(11), "Primary action hover."), tok(n(10), "Primary action pressed.")), (white if L else n(1))
    elif "action" in has:
        act = states("action", "Primary action from its own color input."), on("action")
    else:
        act = states("accent", "Primary action. One per view (DC-L15-03, L15 P08)."), on("accent")
    out["bg"]["action"] = {"primary": act[0][0], "primary-hover": act[0][1], "primary-pressed": act[0][2]}
    out["text"]["on-action"] = tok(act[1], "Text on the primary action fill.")
    brand_step = ctx.cinfo["pinnedStep"] or 9
    out["bg"]["brand"] = tok(r("accent", brand_step) if L else r("accent", 9),
                             "Brand fill for signature surfaces; carries text.on-brand (brandAnchor rule, DC-L01-09).")
    out["text"]["on-brand"] = tok(on("accent"), "Text on color.bg.brand.")
    for extra in ("accent2", "accent3"):
        if extra in has:
            b_, h_, p_ = states(extra, f"{extra} solid fill.")
            out["bg"][extra] = {"subtle": tok(r(extra, 3), f"{extra} subtle fill."), "bold": b_, "bold-hover": h_, "bold-pressed": p_}
            out["text"][extra] = tok(r(extra, 11), f"{extra} text.")
            out["text"]["on-" + extra] = tok(on(extra), f"Text on {extra} solid.")
    surfaces_mode = p["color.surfaces"]
    if surfaces_mode in ("tinted-containers", "brand-or-dynamic-surfaces"):
        out["surface"]["tinted"] = tok(r("accent", 2 if surfaces_mode == "tinted-containers" else 3),
                                       "Tinted container (Colorfulness 50+, L09 X rubric; Q-color-05).")
    for s_ in [x for x in ("success", "warning", "danger", "info", "discovery") if x in has]:
        b_, h_, p_ = states(s_, f"{s_.title()} solid fill.")
        out["bg"][s_] = {"subtle": tok(r(s_, 3), f"{s_.title()} banner and badge background."), "bold": b_, "bold-hover": h_, "bold-pressed": p_}
        out["text"][s_] = tok(r(s_, 11), f"{s_.title()} text and icons; pair with an icon or label (DC-L01-15).")
        out["text"]["on-" + s_] = tok(on(s_), f"Text on bg.{s_}.bold.")
        out["border"][s_] = tok(r(s_, 8), f"{s_.title()} boundary, for example an invalid field (3:1).")
    if raw.get("statusSet") == "workflow":  # Q-color-15 workflow states: fixed meanings on the status hues [inferred]
        wf = {"todo": "neutral", "in-progress": "info", "done": "success", "blocked": "danger", "review": "discovery"}
        out["workflow"] = {}
        for st, hue in wf.items():
            sub_bg = (n(3) if L else n(5)) if hue == "neutral" else r(hue, 3)
            sub_fg = n(11) if hue == "neutral" else r(hue, 11)
            out["workflow"][st] = {"bg": tok(sub_bg, f"Workflow state '{st}' badge fill."), "text": tok(sub_fg, f"Workflow state '{st}' label.")}
    if raw.get("focusColor"):
        out["border"]["focus"] = tok(A("color.focus.custom"), "Focus ring from the raw focus color (L09 M12).")
    if raw.get("focusColor") or fs == "two-tone":
        out["border"]["focus-inner"] = tok(n(12) if raw.get("focusColor") else (white if L else n(1)),
                                           "Inner ring of the two-tone focus indicator; keeps 3:1 on every surface (DC-L08-11).")
    scrim_alpha = {"fluent": (0.4, 0.5), "atlassian": (0.46, 0.6)}.get(raw.get("scrim") or "", (0.45, 0.6))[0 if L else 1]
    shadow_base = ctx.ramp("neutral", "light").steps[12]["hex"] if L else "#000000"
    a = shadow_alpha(ctx)
    k = 1 if L else 2  # dark mode doubles shadow opacity (DC-L04-12)
    ring_hex = ctx.ramp("neutral", "dark").steps[12]["hex"]
    out["overlay"] = {"scrim": tok(srgb_value(ctx.ramp("neutral", "light").steps[12]["hex"] if L and raw.get("scrim") != "fluent" else "#000000", scrim_alpha),
                                   "Modal backdrop (DC-L04-18; Q-depth-06).")}
    out["shadow"] = {
        "key": tok(srgb_value(shadow_base, min(0.6, a * k)), "Key shadow color; alpha doubles in dark (DC-L04-12)."),
        "ambient": tok(srgb_value(shadow_base, min(0.6, a * 0.85 * k)), "Ambient shadow color."),
        "ring": tok(srgb_value(shadow_base if L else ring_hex, 0.1 if L else 0.12),
                    "1px ring for ring-and-shadow depth and dark overlays (#BDBDBD at 12% pattern, DC-L04-12)."),
    }
    if (model == "materials" and raw.get("glass") is not False) or raw.get("glass") is True:
        glass_base = "#ffffff" if L else ctx.ramp("neutral", "dark").steps[3]["hex"]
        out["surface"]["glass"] = tok(srgb_value(glass_base, 0.72), "Glass for controls and navigation only, never content (DC-L04-15).")
        out["surface"]["glass-fallback"] = tok(surf["overlay"], "Solid twin under Reduce Transparency and Increase Contrast (DC-L04-16).")
        out["surface"]["glass-dimming"] = tok(srgb_value("#000000", 0.35), "35% dimming under clear glass over bright content (S-L15-073).")
    cp = raw.get("chartPalette")
    if cp and cp != "none":
        chart = {"$description": "Chart colors (Q-color-19): categorical colors in a fixed order, each at least 3:1 against the page "
                                 "(WCAG 1.4.11); a sequential ramp from the accent; one neutral for 'other'.",
                 "sequential": {str(i + 1): tok(r("accent", s_)) for i, s_ in enumerate((3, 5, 7, 9, 11))},
                 "neutral": tok(n(9), "Other, baseline or comparison series.")}
        if cp == "brand-gray":
            chart["categorical"] = {"1": tok(r("accent", 9), "The brand series."), "2": tok(n(9), "Everything else.")}
        else:
            chart["categorical"] = {str(i + 1): tok(color_value(c)) for i, c in enumerate(ctx.charts.get(mode, []))}
        out["chart"] = chart
    return {"color": dict({"$type": "color",
                           "$description": f"Semantic color roles, {mode} mapping. Names never change across modes; only values do. "
                                           "Dark is a separate mapping, never an inversion (DC-L01-18).",
                           "$extensions": {NS: {"mode": mode, "evidence": ["DC-L01-11", "DC-L01-12", "DC-L01-17", "DC-L01-18", "DC-L01-19", "DC-L04-12", "DC-L04-13"]}}},
                          **out)}


def shadow_alpha(ctx):
    depth = ctx.dials["depth"]
    if depth < 16:
        return 0.0
    return rnd(eval_map({"kind": "anchors", "points": [[16, 0.08], [100, 0.24]]}, depth), 3)


# ---------------------------------------------------------------------------------------------- type

def line_height_ratio(size):
    """LEVERS B7 bands: [12,16]->1.5, [18,24]->1.4, [28,40]->1.25, [48,+]->1.12; gaps go to the nearer band."""
    if size <= 17:
        return 1.5
    if size <= 26:
        return 1.4
    if size <= 44:
        return 1.25
    return 1.12


def snap4_down_on_tie(x):
    return int(math.ceil(x / 4 - 0.5) * 4)


def type_scale_sizes(base, ratio, n_lo, n_hi):
    """The LEVERS B6 formula without any post-processing: round(base * ratio^n) for n in [n_lo, n_hi]."""
    return [round_half_up(base * ratio ** k) for k in range(n_lo, n_hi + 1)]


def build_type_scale(ctx):
    p, raw = ctx.params, ctx.raw
    base = raw.get("baseSize")
    plats = raw.get("platforms") or ["web"]
    pb = levers()["formulas"]["type"]["platformBase"]
    if not base and p.get("platform.useNativeBaseSize") and plats[0] in pb:
        # Brand presence below 50 keeps the platform's own body size when a native platform leads (LEVERS B6, DC-L02-08)
        nb = pb[plats[0]]
        base = (nb[1] if raw.get("productType") == "content" else nb[0]) if isinstance(nb, list) else nb
        ctx.used["type.baseSize.native"] = base
    base = int(base or ctx.P("type.baseSize.web", p["type.baseSize.web"]))
    ratio = float(ctx.P("type.ratio", p["type.ratio"]))
    marketing = bool(raw.get("marketingSurfaces"))
    reach = float(p.get("type.displayReach") or (5.5 if marketing else 2.5))  # LEVERS B6 display reach [inferred bands]
    top_n = max(3, round_half_up(math.log(reach) / math.log(ratio)))
    sizes = type_scale_sizes(base, ratio, -2, top_n)
    min_size = 11  # smallest legible UI size, 11 pt/sp (L14, S-L02-001)
    kept = sorted(set(s for s in sizes if s >= min_size) | {base})
    merged = []
    below = [s for s in kept if s < base]
    above = [s for s in kept if s > base]
    # merge adjacent sizes less than 10% apart (DC-L02-10): below base keep the larger, above base keep the larger
    b2 = []
    for s in sorted(below, reverse=True):
        prev = b2[-1] if b2 else base
        if prev / s - 1 < float(p.get("type.maxStepGapMerge", levers()["formulas"]["type"]["maxStepGapMerge"])):
            merged.append(s)
            continue
        b2.append(s)
    a2 = []
    for s in above:
        prev = a2[-1] if a2 else base
        if s / prev - 1 < 0.1:
            merged.append(prev if a2 else s)
            if a2:
                a2[-1] = s
            continue
        a2.append(s)
    final = sorted(b2) + [base] + a2
    if final.index(base) == 0:  # keep one step below body for captions when the formula gave none
        cap = max(min_size, round_half_up(base / ratio))
        if cap < base:
            final = [cap] + final
    return {"base": base, "ratio": ratio, "reach": reach, "nTop": top_n, "raw": sizes, "sizes": final,
            "merged": sorted(set(merged)), "minSize": min_size}


def build_typography(ctx):
    p, raw = ctx.params, ctx.raw
    sc = build_type_scale(ctx)
    S, base = sc["sizes"], sc["base"]
    b = S.index(base)
    wc = int(ctx.P("type.weightCount", p["type.weightCount"]))
    hw = int(ctx.P("type.headingWeight", p["type.headingWeight"]))
    if wc <= 2:
        hw = 600 if hw < 700 else 700
    w = {"body": 400, "label": 500 if wc >= 3 else 400, "heading": hw}
    if wc >= 4:
        w["display"] = min(900, hw + 100)
    compact_lh = bool(p.get("type.compactLineHeightVariant"))

    faces = font_faces(raw)

    def face(v, fallback):
        if v == "=serif":
            return list(SYSTEM_SERIF)
        if v == "=rounded":
            return list(SYSTEM_ROUNDED)
        if not v or v == "system":
            return list(fallback)
        if isinstance(v, list):
            return v
        return [v] + list(fallback)
    tf = faces["text"]
    text_face = face(tf["face"] if tf["web"] is not False else "system", SYSTEM_SANS)
    df = faces["display"]
    disp = df["face"] if df["web"] is not False else None
    note = " " + "; ".join(f["note"] for f in (tf, df) if f.get("note")) if (tf.get("note") or df.get("note")) else ""
    fam = {"text": tok(text_face, "Text face for UI and body (DC-L02-01)." + note),
           "display": tok(A("font.family.text") if disp in (None, "=textFace", tf["face"]) else face(disp, text_face),
                          "Display face for headings (Apple, Google and Linear split display and text faces, DC-L06-07)."),
           "mono": tok(face(raw.get("monoFace"), SYSTEM_MONO), "Code, tokens, tabular values.")}
    weights = {"$type": "fontWeight", "$description": f"{wc} weights: body 400, labels {w['label']}, headings {hw} (DC-L02-15; Energy sets heading weight, S-L06-031).",
               "body": tok(400), "label": tok(w["label"]), "heading": tok(hw)}
    if "display" in w:
        weights["display"] = tok(w["display"], "Display sizes (32px and up) only.")
    size_tok = {"$type": "dimension",
                "$description": f"Type scale: round({base} x {sc['ratio']}^n), n from -2 to {sc['nTop']}; sizes under {sc['minSize']}px dropped; "
                                "adjacent sizes under 10% apart merged; only the steps a named text style uses are kept (DC-L02-09, DC-L02-10).",
                "$extensions": {NS: {"base": base, "ratio": sc["ratio"], "displayReach": sc["reach"], "formulaSizes": sc["raw"],
                                     "merged": sc["merged"], "evidence": ["DC-L02-09", "DC-L02-10", "S-L02-021", "S-L09-407"]}}}
    grid = 2 if raw.get("lineHeightGrid") == 2 else 4
    snap = (lambda x: int(math.ceil(x / 2 - 0.5) * 2)) if grid == 2 else snap4_down_on_tie
    lh_tok = {"$type": "dimension", "$description": f"Line heights snapped to a {grid}px grid: 1.5 up to 17px, 1.4 to 26px, 1.25 to 44px, 1.12 above (DC-L02-13)."}
    for s in S:
        lh = max(s + 2, snap(s * line_height_ratio(s)))
        lh_tok[str(lh)] = tok(dim(lh))
    text = {"$type": "typography",
            "$description": "Semantic text styles (role x size). lineHeight is a unitless multiplier as DTCG requires; px is in $extensions.",
            "$extensions": {NS: {"evidence": ["DC-L02-07", "DC-L02-13", "DC-L02-14", "DC-L02-15", "DC-L15-02"]}}}

    def sz(k):
        return S[clamp(b + k, 0, len(S) - 1)]

    zero_tracking = raw.get("tracking") == "zero"

    def tracking(size, caps=False):
        if zero_tracking:  # Q-type-13 zero: the font's own spacing everywhere
            return 0.0
        if caps:
            return 0.05
        if size <= 12:
            return 0.02
        if size >= 48:
            return -0.02
        if size >= 32:
            return -0.01
        return 0.0

    styles = []  # (path, size, weightRole, family, use, avoid, caps)
    styles += [("body.sm", sz(-1), "body", "text", "Helper text, timestamps, captions.", "Anything read at length.", False),
               ("body.md", base, "body", "text", "Default UI text: forms, tables, descriptions.", "Long articles when body.lg exists.", False),
               ("body.lg", sz(1), "body", "text", "Long-form reading, onboarding copy.", "Dense tables and forms.", False),
               ("label.sm", sz(-1), "label", "text", "Overlines in capitals with wide tracking (DC-L02-18).", "Sentences; scripts without case.", True),
               ("label.md", sz(-1), "label", "text", "Small control labels, badges, dense tabs.", "Body text.", False),
               ("label.lg", base, "label", "text", "Button and control labels.", "Headings.", False),
               ("code.sm", sz(-1), "body", "mono", "Inline values, dense code rows.", "Paragraphs.", False),
               ("code.md", base, "body", "mono", "Code blocks, token names.", "UI labels.", False),
               ("title.sm", base, "heading", "text", "Table headers, field-group titles.", "Paragraph emphasis.", False)]
    heading_names = ["title.md", "title.lg", "headline.sm", "headline.md", "headline.lg", "display.sm", "display.md", "display.lg"]
    H = S[b + 1:]
    if len(H) > 6:  # 9 base styles + 6 headings = 15, the top of the usual range (DC-L02-10; U5 F8, F28): spread over the scale
        H = [H[i] for i in sorted({round(i * (len(H) - 1) / 5) for i in range(6)})]
        heading_names = ["title.md", "title.lg", "headline.sm", "headline.lg", "display.md", "display.lg"]
    uses = {"title": ("Card, panel and group titles.", "Page titles."), "headline": ("Page and section titles.", "Card titles."),
            "display": ("One hero line per page: marketing, empty states.", "App chrome and repeated elements.")}
    for name, s in zip(heading_names, H):
        role = "display" if name.startswith("display") and "display" in w else "heading"
        fam_name = "display" if not name.startswith("title") else "text"
        u, av = uses[name.split(".")[0]]
        styles.append((name, s, role, fam_name, u, av, False))

    if raw.get("numericStyles"):  # Q-type-06 numeric-face / Q-layout-03 data: tabular figures for amounts and tables
        styles += [("numeric.md", base, "body", "text", "Amounts and table figures: tabular digits line up in columns.", "Running text.", False),
                   ("numeric.lg", sz(2), "heading", "text", "Key numbers: balances, KPIs.", "Headings.", False)]
    used_lh = {}

    def add_style(root, path, s, role, fam_name, use, avoid, caps):
        lh = max(s + 2, snap(s * line_height_ratio(s)))
        used_lh[lh] = True
        em = tracking(s, caps)
        ext = {"lineHeightPx": lh, "letterSpacingEm": em, "use": use, "avoid": avoid}
        if caps:
            ext["textTransform"] = "uppercase"
        if path.startswith("numeric."):
            ext["fontVariantNumeric"] = "tabular-nums"
        if compact_lh and (path.startswith("label") or path in ("body.sm", "body.md")):
            ext["lineHeightTightPx"] = s + 4 if s <= 16 else snap4_down_on_tie(s * 1.2)
        node = root
        parts = path.split(".")
        for q in parts[:-1]:
            node = node.setdefault(q, {})
        node[parts[-1]] = tok({"fontFamily": A(f"font.family.{fam_name}"), "fontSize": A(f"font.size.{s}"),
                               "fontWeight": A(f"font.weight.{role}"), "letterSpacing": dim(rnd(s * em, 2)),
                               "lineHeight": rnd(lh / s, 4)}, None, ext)
    for st in styles:
        add_style(text, *st)
    used_sizes = sorted({st[1] for st in styles} | {base})  # the font.size steps a named style uses (DC-L02-10: 8-10 sizes)
    for s in used_sizes:
        size_tok[str(s)] = tok(dim(s))
    sc = dict(sc, sizes=used_sizes, scaleSizes=S)
    # Emphasized variants: Expression 67 and up (levers.json type.emphasizedVariants). Material 3 Expressive pairs each
    # baseline style with a heavier one for selection, actions, headlines and editorial moments (DC-L02-11, S-L02-006).
    # Each uses the next heavier weight the system already has, so the weight count stays as DC-L02-15 set it.
    emphasized = []
    if ctx.P("type.emphasizedVariants", p.get("type.emphasizedVariants")):
        order = sorted(w, key=lambda r: (w[r], r))

        def heavier(role):
            return next((r for r in order if w[r] > w[role]), None)
        emph = {"$description": "Emphasized variants: the same size and line height, one weight heavier. Use them for the selected "
                                "item, key actions, headlines and editorial moments, not for whole paragraphs (DC-L02-11, S-L02-006)."}
        for path, s, role, fam_name, use, avoid, caps in styles:
            hr = heavier(role)
            if path.startswith(("code.", "numeric.")) or caps or not hr:
                continue
            add_style(emph, path, s, hr, fam_name, f"Emphasized {path}: selection, actions, headlines.", "Whole paragraphs.", False)
            emphasized.append("emphasized." + path)
        if emphasized:
            text["emphasized"] = emph
    scripts = levers()["formulas"]["type"]["scripts"]
    script_notes = {}
    for sc_code in raw.get("scripts") or ["Latn"]:
        f = 1.0
        for band, codes in (("medium", scripts["medium"]), ("large", scripts["large"]), ("extraLarge", scripts["extraLarge"])):
            if sc_code in codes:
                f = scripts["lineHeightFactor"][band]
        if sc_code in ("Hans", "Hant", "Jpan", "Kore"):
            script_notes[sc_code] = {"lineHeightFactor": f, "cjk": scripts["cjk"]}
        elif f != 1.0 or sc_code in levers()["formulas"]["type"]["tracking"]["zeroScripts"]:
            script_notes[sc_code] = {"lineHeightFactor": f,
                                     "zeroTracking": sc_code in levers()["formulas"]["type"]["tracking"]["zeroScripts"]}
    text["$extensions"][NS]["scripts"] = script_notes
    ctx.type_info = dict(sc, weights=w, styles=[s[0] for s in styles], emphasized=emphasized, lineHeights=sorted(used_lh), scripts=script_notes,
                         faces=faces)
    font = {"family": dict({"$type": "fontFamily"}, **fam), "weight": weights, "size": size_tok,
            "line-height": {k: v for k, v in lh_tok.items() if k.startswith("$") or int(k) in used_lh}}
    return {"font": font, "text": text}


# ---------------------------------------------------------------------------------------------- space

def space_ladder(unit, raw=None):
    vals = []
    for m in space_multipliers(raw):
        v = unit * m
        if abs(v - round(v)) < 1e-9:
            vals.append(int(round(v)))
    return sorted(set(vals))


def targets_for(ctx):
    plats = set(ctx.raw.get("platforms") or ["web"])
    inputs = set(ctx.raw.get("inputs") or ["pointer", "touch"])
    inputs |= {DEVICE_INPUTS[x] for x in (ctx.raw.get("devices") or []) + (ctx.raw.get("situations") or []) if x in DEVICE_INPUTS}
    out = {}
    if "pointer" in inputs or plats & {"web", "desktop", "macos", "windows"}:
        out["pointer"] = TARGETS["pointer"]
    if "touch" in inputs or plats & {"ios", "android", "ipados"}:
        out["touch"] = TARGETS["touch-android"] if "android" in plats else TARGETS["touch"]
    if "remote" in inputs or "tv" in plats:
        out["remote"] = TARGETS["remote"]
    if "gaze" in inputs or plats & {"visionos", "xr"}:
        out["gaze"] = TARGETS["gaze"]
    if "vehicle" in inputs or "car" in plats:
        out["vehicle"] = TARGETS["vehicle"]
    if ctx.raw.get("minTarget"):
        out = {k: max(v, int(ctx.raw["minTarget"])) for k, v in out.items()}
    return out


def build_space_foundation(ctx):
    unit = int(ctx.raw.get("spaceUnit") or 4)
    ladder = space_ladder(unit, ctx.raw)
    space = {"$type": "dimension",
             "$description": f"Spacing ladder: {unit} x [{', '.join(fmt_num(m) for m in space_multipliers(ctx.raw))}], non-integers dropped "
                             "(LEVERS B8; x24 added by spec 6.2). Names are pixel values.",
             "$extensions": {NS: {"unit": unit, "evidence": ["DC-L03-01", "DC-L03-02", "S-L09-508"]}}}
    for v in ladder:
        space[str(v)] = tok(dim(v))
    tg = targets_for(ctx)
    icon_default = int(ctx.P("icon.defaultSize", ctx.params["icon.defaultSize"]))
    pairs = {16: 14, 20: 16, 24: 20}  # icon size -> paired text size (DC-L05-05)
    label_w = 500 if int(ctx.params["type.weightCount"]) >= 3 else 400

    fixed = ctx.raw.get("iconStroke")

    def stroke(sz):  # LEVERS B12 [inferred formula]: round_to_0.5((size/12) * (weight/400)), min 1; Q-icon-03 fixes it at 24px
        if isinstance(fixed, (int, float)):
            return max(1.0, round(fixed * sz / 24 * 2) / 2)
        return max(1.0, round((sz / 12) * (label_w / 400) * 2) / 2)
    size = {"$type": "dimension",
            "icon": {"$description": "Icon sizes paired with text sizes 14/16/20 (DC-L05-05).",
                     "sm": tok(dim(16)), "md": tok(dim(20)), "lg": tok(dim(24)),
                     "default": tok(A(f"size.icon.{ {16: 'sm', 20: 'md', 24: 'lg'}.get(icon_default, 'md') }"),
                                    "Default icon size from the Density dial (DC-L05-05).")},
            "target": {"$description": "Minimum hit areas per input. Density never changes these (L14 I-1, DC-L03-12, DC-L14-03).",
                       **{k: tok(dim(v)) for k, v in tg.items()},
                       "min": tok(dim(tg.get("touch", tg.get("pointer", 24)) if "touch" in tg else tg.get("pointer", 24)),
                                  "Hit-area floor for the product's primary input; grow hit areas (not visuals) to reach it.")}}
    gaps = {k: TARGET_GAPS.get(k, 8) for k in tg}
    space["target"] = {"gap": tok(dim(max(gaps.values()) if "touch" in tg else gaps.get("pointer", 8)),
                                  "Gap between adjacent targets: 12 coarse, 8 fine (Primer, S-L03-009).")}
    icon = {"stroke": {"$type": "dimension",
                       "$description": "Icon stroke = round_to_0.5((size/12) x (label weight/400)), min 1 (LEVERS B12, [inferred] fit to Material 2px@24 and Octicons 1.5px@16).",
                       "sm": tok(dim(stroke(16))), "md": tok(dim(stroke(20))), "lg": tok(dim(stroke(24)))}}
    bp = BREAKPOINTS.get(ctx.raw.get("breakpoints") or "")
    if bp:
        size["breakpoint"] = {"$description": f"Layout breakpoints ({ctx.raw['breakpoints']}, Q-layout-01): the minimum width where each layout starts.",
                              **{k: tok(dim(v)) for k, v in bp.items()}}
    ctx.space_info = {"unit": unit, "ladder": ladder, "targets": tg, "iconDefault": icon_default,
                      "iconStroke": {16: stroke(16), 20: stroke(20), 24: stroke(24)}, "breakpoints": bp or {}}
    return {"space": space, "size": size, "icon": icon}


def build_space_density(ctx, density):
    ladder = ctx.space_info["ladder"]
    unit = ctx.space_info["unit"]
    shift = {"spacious": 1, "comfortable": 0, "compact": -1}[density]
    ratio = {"spacious": 3.5, "comfortable": 2.5, "compact": 2.0}[density]  # innerOuterRatio bands (DC-L03-24 [inferred])
    ratio = {"1:3-1:4": {"spacious": 4.0, "comfortable": 3.0, "compact": 3.0},   # Q-space-05 [inferred]
             "dense": {"spacious": 3.0, "comfortable": 2.0, "compact": 2.0}}.get(ctx.raw.get("groupRatio") or "", {}).get(density, ratio)
    nz = [v for v in ladder if v > 0]

    def at(mult):
        want = mult * unit
        i = min(range(len(nz)), key=lambda j: (abs(nz[j] - want), nz[j]))
        return nz[clamp(i + shift, 0, len(nz) - 1)]

    inset = {k: at(m) for k, m in (("xs", 1), ("sm", 2), ("md", 3), ("lg", 4), ("xl", 6))}
    stack = {k: at(m) for k, m in (("xs", 1), ("sm", 2), ("md", 3), ("lg", 4), ("xl", 6))}
    inline = {k: at(m) for k, m in (("xs", 1), ("sm", 2), ("md", 3))}

    def outer(inner):  # smallest ladder value >= ratio x inner and at least one step above it (L15 P16)
        cands = [v for v in nz if v >= ratio * inner and v > inner]
        return cands[0] if cands else nz[-1]
    section = {"sm": outer(stack["md"]), "md": outer(stack["lg"]), "lg": outer(stack["xl"])}
    md_home = int(ctx.P("control.height.md", ctx.params["control.height.md"]))
    home = ctx.params["space.densityMode"]
    steps = [24, 32, 40, 48, 56]
    idx = {"spacious": 0, "comfortable": 1, "compact": 2}
    md = md_home + 8 * (idx[home] - idx[density])
    md = clamp(md, 32 if "touch" in ctx.space_info["targets"] else 24, 56)
    sm = max(24, md - 8)
    lg = md + 8
    ref = lambda v: A(f"space.{v}")
    out = {"space": {"$type": "dimension",
                     "$description": f"Semantic spacing, {density} density: aliases into the ladder, shifted {shift:+d} step (DC-L03-10, DC-L03-11). "
                                     "Parents own spacing; children never set outer margins (DC-L03-04).",
                     "$extensions": {NS: {"density": density, "innerOuterRatio": ratio, "excluded": levers()["formulas"]["density"]["excluded"],
                                          "evidence": ["DC-L03-04", "DC-L03-10", "DC-L03-11", "DC-L03-24", "S-L03-029"]}},
                     "inset": {k: tok(ref(v)) for k, v in inset.items()},
                     "stack": {k: tok(ref(v)) for k, v in stack.items()},
                     "inline": {k: tok(ref(v)) for k, v in inline.items()},
                     "section": {k: tok(ref(v), "Outer gap between groups: at least ratio x the inner gap (inner < outer, L15 P16).")
                                 for k, v in section.items()}},
           "size": {"$type": "dimension",
                    "control": {"$description": f"Control heights, {density} (DC-L03-07). Hit areas never shrink below size.target.min.",
                                "sm": tok(dim(sm)), "md": tok(dim(md)), "lg": tok(dim(lg))}}}
    ctx.__dict__.setdefault("density_info", {})[density] = {"inset": inset, "stack": stack, "inline": inline, "section": section,
                                                          "control": {"sm": sm, "md": md, "lg": lg}, "ratio": ratio}
    return out


# ---------------------------------------------------------------------------------------------- shape

def build_shape(ctx):
    p = ctx.params
    control = ctx.P("radius.control", p["radius.control"])
    full = control == "full" or (isinstance(control, (int, float)) and control >= FULL)
    rough = ctx.dials["roundness"]
    if full:
        control_v = FULL
        container = snap_to(16 + (rough - 93) / 7 * 12, SNAP_RADII) if rough >= 93 else 20
        detail = 4  # [inferred]: pill controls keep small square-ish details (M3 checkbox 2dp)
    else:
        control_v = int(control)
        container = snap_to(control_v * 1.5, SNAP_RADII)
        if control_v > 0:
            container = max(container, 8)
        # LEVERS B9 says detail = max(2, control/2); a sharp system (control 0) keeps 0, the same guard
        # container already has (correction logged in NOTES)
        detail = 0 if control_v == 0 else snap_to(max(2, control_v / 2), SNAP_RADII)
    container = ctx.P("radius.container", container)
    overlay = ctx.P("radius.overlay", snap_to(min(32, container * 1.5), SNAP_RADII) if container else 0)
    detail = ctx.P("radius.detail", detail)
    smallest = min([v for v in SNAP_RADII if v > 0])
    if full:
        control_sm = FULL
    else:
        i = SNAP_RADII.index(snap_to(control_v, SNAP_RADII))
        control_sm = SNAP_RADII[max(0, i - 1)] if control_v > 0 else 0  # shapes under 32px drop one step (S-L04-007)
    pad = ctx.density_info[ctx.params["space.densityMode"]]["inset"]["lg"]
    nested = 0 if container == 0 else max(container - pad, smallest)  # DC-L04-05
    focus_w = int(ctx.raw.get("focusWidth") or 2)
    offset = int(ctx.raw.get("focusOffset") if isinstance(ctx.raw.get("focusOffset"), (int, float)) else 2)
    focus_r = FULL if full else (max(0, control_v + offset) if control_v > 0 else 0)
    radius = {"$type": "dimension",
              "$description": "Radius scale snapped to 0, 2, 4, 6, 8, 12, 16, 20, 24, 28, 32 plus full (LEVERS B9, [inferred] ratios checked against Atlassian).",
              "$extensions": {NS: {"evidence": ["DC-L04-02", "DC-L04-03", "DC-L04-05", "S-L04-016", "S-L04-007"]}}}
    for v in sorted(set(SNAP_RADII)):
        radius[str(v)] = tok(dim(v))
    radius["full"] = tok(dim(FULL), "Pills and avatars.")
    rr = lambda v: A("radius.full") if v >= FULL else A(f"radius.{v}")
    radius.update({
        "detail": tok(rr(detail), "Checkboxes, tags, small badges."),
        "control": tok(rr(control_v), "Buttons, inputs, selects (Roundness dial, DC-L04-02)."),
        "control-sm": tok(rr(control_sm), "Controls under 32px tall drop one step (Fluent, S-L04-007)."),
        "container": tok(rr(container), "Cards and panels."),
        "overlay": tok(rr(overlay), "Dialogs, sheets, popovers."),
        "person": tok(A("radius.full"), "Avatars."),
        "nested": tok(dim(nested), "Inner radius for an element inset by space.inset.lg inside a container: max(outer - padding, smallest step) (DC-L04-05)."),
        "focus": tok(dim(focus_r), "Focus ring radius = control radius + ring offset (Atlassian radius + 2px, S-L04-016)."),
    })
    widths = sorted({1, 2, 4} | {int(x) for x in (ctx.raw.get("borderWidths") or []) if isinstance(x, (int, float)) and 0 < x <= 8})
    border = {"$type": "dimension", "width": {
        "$description": f"Border widths {' / '.join(str(x) for x in widths)}. Width changes on state use an inset shadow so layout does not jump (DC-L04-07).",
        **{str(x): tok(dim(x)) for x in widths},
        "default": tok(A("border.width.1")), "selected": tok(A("border.width.2")), "emphasis": tok(A("border.width.4"))}}
    focus = {"$type": "dimension",
             "$description": f"Focus indicator: {focus_w}px ring, {offset}px offset" + (" (inside the edge)" if offset < 0 else "")
                             + ", color.border.focus; never color-only (DC-L04-09, WCAG 2.4.7, 2.4.13).",
             "ring": {"width": tok(dim(focus_w)), "offset": tok(dim(offset))}}
    ctx.shape_info = {"control": "full" if full else control_v, "control-sm": control_sm, "detail": detail, "container": container,
                      "overlay": overlay, "nested": nested, "focusWidth": focus_w, "focusRadius": focus_r,
                      "iconCorners": p["icon.cornerStyle"], "iconCaps": p["icon.caps"]}
    return {"radius": radius, "border": border, "focus": focus}


# ---------------------------------------------------------------------------------------------- elevation

def shadow_layer(color, x, y, blur, spread=0, inset=False):
    v = {"color": A(color), "offsetX": dim(x), "offsetY": dim(y), "blur": dim(blur), "spread": dim(spread)}
    if inset:
        v["inset"] = True
    return v


def build_elevation(ctx):
    model = ctx.P("elevation.model", ctx.params["elevation.model"])
    none = [shadow_layer("color.shadow.key", 0, 0, 0, 0)]
    ring = shadow_layer("color.shadow.ring", 0, 0, 0, 1)
    two = lambda y, b: [shadow_layer("color.shadow.key", 0, 1, 2, 0), shadow_layer("color.shadow.ambient", 0, y, b, 0)]
    ladder = {}
    if model in ("shadow-ladder", "materials"):
        for i, nlev in enumerate(levers()["formulas"]["elevation"]["shadowLadder"]["levels"], start=1):
            ladder[str(i)] = tok([shadow_layer("color.shadow.ambient", 0, 0, 2, 0),
                                  shadow_layer("color.shadow.key", 0, nlev / 2, nlev, 0)],
                                 f"Level {nlev}: ambient 0 0 2px + key 0 {nlev / 2:g}px {nlev}px (Fluent formula, S-L09-179).")
        raised, floating, overlay = A("elevation.shadow.1"), A("elevation.shadow.3"), A("elevation.shadow.5")
    elif model == "tonal":
        raised, floating, overlay = none, two(4, 12), two(12, 32)
    elif model == "ring+faint-shadow":
        raised = [ring, shadow_layer("color.shadow.key", 0, 1, 2, 0)]
        floating = [ring] + two(4, 12)
        overlay = [ring] + two(12, 32)
    else:  # borders
        raised = floating = overlay = none
    desc = {"borders": "Borders only: surfaces separate by 1px borders; no shadows (GOV.UK, Primer; L09 M7).",
            "ring+faint-shadow": "1px alpha ring plus an extra-small shadow (shadcn, Geist, Radix).",
            "tonal": "Tonal layers: surfaces step in lightness; shadows only on floating UI (Carbon, Material 3, Linear).",
            "shadow-ladder": "Key + ambient shadow ladder (Fluent 2, Polaris).",
            "materials": "Shadow ladder plus glass for controls and navigation only, with solid fallbacks (Liquid Glass, Acrylic)."}[model]
    el = {"$type": "shadow", "$description": desc + " Dark mode doubles shadow alpha and lifts surfaces (DC-L04-12, DC-L04-13).",
          "$extensions": {NS: {"model": model, "depth": ctx.dials["depth"], "shadowAlphaLight": shadow_alpha(ctx),
                               "evidence": ["DC-L04-10", "DC-L04-12", "DC-L04-13", "L09-M7"]}},
          "raised": tok(raised, "Cards that lift on hover, sticky headers, dragged rows."),
          "floating": tok(floating, "Menus, popovers, dropdowns."),
          "overlay": tok(overlay, "Dialogs and sheets (with color.overlay.scrim).")}
    out = {"elevation": el}
    if ladder:
        el["shadow"] = ladder
    if (model == "materials" and ctx.raw.get("glass") is not False) or ctx.raw.get("glass") is True:
        out["material"] = {"glass": {"blur": tok(dim(24), "Backdrop blur for glass controls and bars.", type_="dimension")}}
    ctx.elev_info = {"model": model, "alpha": shadow_alpha(ctx)}
    return out


# ---------------------------------------------------------------------------------------------- motion

def spring_curve(damping, stiffness, samples=24):
    """Step response of a mass-1 spring, sampled into CSS linear() (DC-L04-22). Returns (linear(), ms)."""
    w = math.sqrt(stiffness)
    z = damping
    if z < 1:
        t_end = math.log(1000) / (z * w)
    else:
        t_end = 9.2 / w
    wd = w * math.sqrt(max(1e-9, 1 - z * z))

    def x(t):
        if z < 1:
            return 1 - math.exp(-z * w * t) * (math.cos(wd * t) + (z * w / wd) * math.sin(wd * t))
        return 1 - math.exp(-w * t) * (1 + w * t)
    pts = [rnd(x(t_end * i / samples), 3) for i in range(samples + 1)]
    pts[0], pts[-1] = 0, 1
    return "linear(" + ", ".join(f"{v:g}" for v in pts) + ")", int(round(t_end * 1000 / 10) * 10)


def build_motion(ctx):
    p = ctx.params
    energy = ctx.dials["energy"]
    mult = float(ctx.P("motion.durationMultiplier", p["motion.durationMultiplier"]))
    r10 = lambda v: int(round(v / 10) * 10)
    d = {"instant": 0, "micro": 100, "short": 150, "medium": r10(250 * mult), "long": r10(400 * mult), "extra": r10(700 * mult)}
    exit_k = 0.75  # exits 20-35% shorter than entrances (Atlassian 250/200, Primer 300/200) [inferred midpoint]
    d["medium-exit"] = r10(d["medium"] * exit_k)
    d["long-exit"] = r10(d["long"] * exit_k)
    std = p["motion.easing.standard"]
    if energy <= 33:
        enter, exit_ = [0, 0, 0.38, 0.9], [0.2, 0, 1, 0.9]      # Carbon productive (S-L06-002)
    elif energy <= 66:
        enter, exit_ = [0, 0, 0, 1], [0.3, 0, 1, 1]            # Material decelerate / accelerate
    else:
        enter, exit_ = [0, 0, 0.3, 1], [0.4, 0.14, 1, 1]       # Carbon expressive (S-L06-002)
    zeta = float(ctx.P("motion.spring.spatial.dampingRatio", p["motion.spring.spatial.dampingRatio"]))
    k = float(ctx.P("motion.spring.spatial.stiffness", p["motion.spring.spatial.stiffness"]))
    zeta, k = rnd(zeta, 3), rnd(k, 1)
    springs = {}
    for group, (z, ks) in {"spatial": (zeta, {"fast": k * 2, "default": k, "slow": k * 0.45}),
                           "effects": (1.0, {"fast": 3800, "default": 1600, "slow": 800})}.items():
        g = {}
        for speed, stiff in ks.items():
            stiff = rnd(stiff, 1)
            lin, dur = spring_curve(z, stiff)
            apple_d = rnd(2 * math.pi / math.sqrt(stiff), 3)
            ext = {"spring": {"dampingRatio": z, "stiffness": stiff, "mass": 1},
                   "apple": {"duration": apple_d, "bounce": rnd(max(0.0, 1 - z), 3)},
                   "css": {"easing": lin if z < 1 else "cubic-bezier(" + ", ".join(f"{v:g}" for v in std) + ")", "durationMs": dur},
                   "use": {"fast": "small components (switches, buttons)", "default": "partial-screen (sheets, drawers)",
                           "slow": "full-screen"}[speed]}
            g[speed] = tok({"duration": ms(dur), "delay": ms(0), "timingFunction": A("motion.easing.standard")},
                           None, ext)
        springs[group] = g
    motion = {
        "duration": {"$type": "duration",
                     "$description": f"Duration ladder (DC-L04-20); Energy multiplies medium and longer by {mult:.2f} (0.8-1.2, A4). Exits 25% shorter.",
                     **{kk: tok(ms(v)) for kk, v in d.items()}},
        "easing": {"$type": "cubicBezier", "$description": "Standard, enter (decelerate), exit (accelerate); linear only for spinners and progress (DC-L04-21).",
                   "standard": tok(std, "Moving and morphing on screen."), "enter": tok(enter, "Entering: decelerate."),
                   "exit": tok(exit_, "Leaving: accelerate out of the way."), "linear": tok([0, 0, 1, 1], "Spinners and progress only.")},
        "spring": {"$type": "transition",
                   "$description": "Springs. DTCG 2025.10 has no spring type (S-L07-002, issue #429): each is a transition with a cubic-bezier "
                                   "fallback; dampingRatio and stiffness live in $extensions with Apple duration/bounce and a CSS linear() "
                                   "sample (DC-L04-22, L04 token-encoding default). Effects springs stay critically damped (S-L04-004).",
                   **springs},
    }
    ctx.motion_info = {"durations": d, "multiplier": mult, "standard": std, "enter": enter, "exit": exit_,
                       "spatial": {"dampingRatio": zeta, "stiffness": k, "bounce": rnd(1 - zeta, 3) if zeta < 1 else 0},
                       "motionOff": bool(ctx.flags.get("motionOff"))}
    return {"motion": motion}


def build_motion_context(ctx, context):
    reduced = context == "reduced" or ctx.flags.get("motionOff")
    off = bool(ctx.flags.get("motionOff")) or (context == "reduced" and ctx.raw.get("reducedMotion") == "remove")

    def t(dur, ease, desc):
        return tok({"duration": A(f"motion.duration.{dur}"), "delay": ms(0), "timingFunction": A(f"motion.easing.{ease}")}, desc)
    if reduced:
        fb = "instant" if off else "micro"
        body = {"feedback": t(fb, "standard", "Color and opacity feedback stays (reduced motion keeps feedback, DC-L04-25)."),
                "enter": t(fb, "standard", "Fade only: no translate or scale."),
                "exit": t(fb, "standard", "Fade only."),
                "move": t("instant", "standard", "Travel removed: position changes are instant."),
                "expand": t(fb, "standard", "Fade only.")}
    else:
        body = {"feedback": t("micro", "standard", "Hover, press, color changes."),
                "enter": t("medium", "enter", "Menus, popovers, toasts entering."),
                "exit": t("medium-exit", "exit", "Leaving: shorter than enter (DC-L04-24)."),
                "move": tok(A("motion.spring.spatial.default"), "On-screen movement: spatial spring (web: linear() sample)."),
                "expand": t("long", "enter", "Dialogs, sheets, side panels entering.")}
    desc = f"Semantic transitions, {context} motion. Reduced motion is a token mode: travel becomes opacity, feedback stays (DC-L04-25)."
    if off and not ctx.flags.get("motionOff"):
        desc += " Q-motion-07 remove: feedback is instant too."
    elif off:
        desc += " flags.motionOff is set, so standard equals reduced (GOV.UK posture, L09 M8)."
    return {"motion": {"transition": dict({"$type": "transition", "$description": desc}, **body)}}


# =============================================================================================
# Generate: files, resolver, contrast pairs, meta
# =============================================================================================

TOKEN_FILES_ORDER = ["primitives", "semantic"]


def contrast_pairs(ctx):
    """Every foreground/background pair the semantic layer promises, per mode (DC-L01-22, B5)."""
    tmin = 7.0 if ctx.raw.get("contrastTarget") == "AAA" else 4.5
    surfaces = ["color.surface.base", "color.surface.raised", "color.surface.sunken", "color.surface.overlay"]
    text_on = {
        "color.text.primary": surfaces + ["color.bg.neutral.subtle", "color.bg.neutral.subtle-hover", "color.bg.neutral.subtle-pressed",
                                          "color.bg.accent.subtle"],
        "color.text.secondary": surfaces + ["color.bg.neutral.subtle", "color.bg.neutral.subtle-hover"],
        "color.text.tertiary": surfaces,
        "color.text.link": surfaces + ["color.bg.accent.subtle"],
        "color.text.on-accent": ["color.bg.accent.bold", "color.bg.accent.bold-hover", "color.bg.accent.bold-pressed"],
        "color.text.on-action": ["color.bg.action.primary", "color.bg.action.primary-hover", "color.bg.action.primary-pressed"],
        "color.text.on-brand": ["color.bg.brand"],
        "color.text.inverse": ["color.bg.inverse"],
    }
    text_on["color.text.primary"].append("color.bg.field")
    for s in [x for x in ("success", "warning", "danger", "info", "discovery") if x in ctx.cinfo["ramps"]]:
        text_on[f"color.text.{s}"] = ["color.surface.base", "color.surface.raised", f"color.bg.{s}.subtle"]
        text_on[f"color.text.on-{s}"] = [f"color.bg.{s}.bold", f"color.bg.{s}.bold-hover", f"color.bg.{s}.bold-pressed"]
    for extra in ("accent2", "accent3"):
        if extra in ctx.cinfo["ramps"]:
            text_on[f"color.text.{extra}"] = ["color.surface.base", "color.surface.raised", f"color.bg.{extra}.subtle"]
            text_on[f"color.text.on-{extra}"] = [f"color.bg.{extra}.bold", f"color.bg.{extra}.bold-hover", f"color.bg.{extra}.bold-pressed"]
    if ctx.raw.get("statusSet") == "workflow":
        for st in ("todo", "in-progress", "done", "blocked", "review"):
            text_on[f"color.workflow.{st}.text"] = [f"color.workflow.{st}.bg"]
    non_text = {
        "color.border.strong": surfaces,
        "color.border.input": surfaces + ["color.bg.neutral.subtle", "color.bg.field"],
        "color.icon.default": surfaces + ["color.bg.neutral.subtle"],
        "color.border.danger": surfaces,
    }
    focus_bgs = surfaces + ["color.bg.neutral.subtle"]
    pairs = []
    for mode in ctx.modes:
        for fg, bgs in text_on.items():
            for bg in bgs:
                pairs.append({"mode": mode, "fg": fg, "bg": bg, "min": tmin, "kind": "text",
                              "rule": "WCAG 2.2 SC 1.4.3" + (" / 1.4.6 (AAA)" if tmin > 4.5 else ""), "level": "error"})
        for fg, bgs in non_text.items():
            for bg in bgs:
                pairs.append({"mode": mode, "fg": fg, "bg": bg, "min": 3.0, "kind": "non-text", "rule": "WCAG 2.2 SC 1.4.11", "level": "error"})
        for bg in focus_bgs:
            pr = {"mode": mode, "fg": "color.border.focus", "bg": bg, "min": 3.0, "kind": "focus", "rule": "WCAG 2.2 SC 1.4.11, 2.4.13",
                  "level": "error"}
            if ctx.raw.get("focusColor") or ctx.raw.get("focusStyle") == "two-tone":
                pr["inner"] = "color.border.focus-inner"
            pairs.append(pr)
        cp = ctx.raw.get("chartPalette")
        if cp in ("categorical-8", "categorical-14", "brand-gray"):
            n_cat = {"categorical-8": 8, "categorical-14": 14, "brand-gray": 2}[cp]
            for i in range(1, n_cat + 1):
                pairs.append({"mode": mode, "fg": f"color.chart.categorical.{i}", "bg": "color.surface.base", "min": 3.0, "kind": "chart",
                              "rule": "WCAG 2.2 SC 1.4.11 (chart marks)", "level": "warning"})
        for bg in ("color.surface.base", "color.surface.raised"):
            pairs.append({"mode": mode, "fg": "color.bg.action.primary", "bg": bg, "min": 3.0, "kind": "fill-boundary",
                          "rule": "WCAG 2.2 SC 1.4.11 (advisory: a text-labelled button needs no boundary contrast)", "level": "warning"})
    return pairs


def build_resolver(ctx, files):
    foundation = [f for f in files if not re.search(r"\.(light|dark|spacious|comfortable|compact|standard|reduced)\.tokens\.json$", f)
                  and f.endswith(".tokens.json")]
    order = {n: i for i, n in enumerate(TOKEN_FILES_ORDER)}
    foundation.sort(key=lambda f: order.get(f.replace(".tokens.json", ""), 99))
    res = {"name": ctx.state.get("name") or "Design system", "version": "2025.10",
           "description": "DTCG Resolver Module 2025.10. Orthogonal modifiers (no two set the same token): "
                          + " x ".join(["theme"] if len(ctx.modes) > 1 else []) + (" x " if len(ctx.modes) > 1 else "")
                          + "density x motion (S-L07-004, DC-L07-15, DC-L07-17).",
           "sets": {"foundation": {"description": "Primitives and mode-independent tokens.",
                                   "sources": [{"$ref": f} for f in foundation]}},
           "modifiers": {}, "resolutionOrder": [{"$ref": "#/sets/foundation"}]}
    if len(ctx.modes) > 1:
        default_theme = "dark" if ctx.raw.get("defaultTheme") == "dark" else "light"
        res["modifiers"]["theme"] = {"description": "Color scheme; dark is a separate mapping, not an inversion (DC-L01-18).",
                                     "contexts": {m: [{"$ref": f"semantic.color.{m}.tokens.json"}] for m in ctx.modes},
                                     "default": default_theme}
        res["resolutionOrder"].append({"$ref": "#/modifiers/theme"})
    else:
        res["sets"]["theme"] = {"description": f"Single color scheme ({ctx.modes[0]}).",
                                "sources": [{"$ref": f"semantic.color.{ctx.modes[0]}.tokens.json"}]}
        res["resolutionOrder"].append({"$ref": "#/sets/theme"})
    res["modifiers"]["density"] = {"description": "Semantic spacing density; primitives and target minimums never change (DC-L03-11).",
                                   "contexts": {d: [{"$ref": f"semantic.density.{d}.tokens.json"}] for d in DENSITIES},
                                   "default": ctx.params["space.densityMode"]}
    res["modifiers"]["motion"] = {"description": "Reduced motion as a token mode (DC-L04-25; WCAG 2.3.3 treated as required).",
                                  "contexts": {c: [{"$ref": f"motion.{c}.tokens.json"}] for c in ("standard", "reduced")},
                                  "default": "reduced" if ctx.flags.get("motionOff") else "standard"}
    res["resolutionOrder"] += [{"$ref": "#/modifiers/density"}, {"$ref": "#/modifiers/motion"}]
    return res


PARAM_OVERRIDES = {"type.displayReach", "radius.container", "radius.overlay", "radius.detail", "color.dark.baseY",
                   "color.placeholderHue", "type.maxStepGapMerge"}
MODE_WORDS = {"light": "theme", "dark": "theme", "spacious": "density", "comfortable": "density", "compact": "density",
              "standard": "motion", "reduced": "motion"}


def is_param_override(key):
    return key in PARAM_OVERRIDES or key in lever_index()


def split_mode_key(key):
    """'compact:size.row.md' -> ('compact', 'size.row.md'); 'size.row.md' -> (None, 'size.row.md')."""
    if ":" in key:
        mode, path = key.split(":", 1)
        return mode.strip(), path.strip()
    return None, key


def _node_at(tree, parts):
    node = tree
    for q in parts:
        node = node.get(q) if isinstance(node, dict) else None
        if node is None:
            return None
    return node


def _group_type(tree, parts):
    """$type inherited from the nearest group of a path inside one token file."""
    node, t = tree, tree.get("$type") if isinstance(tree, dict) else None
    for q in parts[:-1]:
        node = node.get(q) if isinstance(node, dict) else None
        if not isinstance(node, dict):
            break
        t = node.get("$type", t)
    return t


def infer_token_type(value, path):
    """DTCG $type for a value a person gives (U5 F2): hex -> color, 12 / '12px' -> dimension, '250ms' -> duration."""
    head = path.split(".")[0]
    if isinstance(value, str):
        v = value.strip()
        if re.fullmatch(r"#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})", v):
            return "color"
        if re.fullmatch(r"-?\d+(\.\d+)?(px|rem)", v):
            return "dimension"
        if re.fullmatch(r"\d+(\.\d+)?(ms|s)", v):
            return "duration"
        if path.startswith("font.family."):
            return "fontFamily"
        return None
    if isinstance(value, dict) and "unit" in value:
        return "duration" if value["unit"] in ("ms", "s") else "dimension"
    if isinstance(value, dict) and "colorSpace" in value:
        return "color"
    if isinstance(value, list) and len(value) == 4 and all(isinstance(x, (int, float)) for x in value) and "easing" in path:
        return "cubicBezier"
    if isinstance(value, list) and path.startswith("font.family."):
        return "fontFamily"
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if path.startswith("font.weight."):
            return "fontWeight"
        if head == "opacity":
            return "number"
        if path.startswith("motion.duration."):
            return "duration"
        if head in ("space", "size", "radius", "border", "focus", "font", "icon", "material"):
            return "dimension"
    return None


def coerce_token_value(value, typ):
    """A person's value in DTCG 2025.10 form for a token type; None when it cannot be (aliases pass through)."""
    if isinstance(value, str) and value.startswith("{") and value.endswith("}"):
        return value
    if typ == "color":
        if isinstance(value, dict) and "colorSpace" in value:
            return value
        if isinstance(value, str) and re.fullmatch(r"#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})", value.strip()):
            hx = value.strip().lower()
            hx = "#" + "".join(c * 2 for c in hx[1:]) if len(hx) == 4 else hx
            return srgb_value(hx)
        return None
    if typ == "dimension":
        if isinstance(value, dict) and isinstance(value.get("value"), (int, float)) and value.get("unit") in ("px", "rem"):
            return value
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            return dim(value)
        m = re.fullmatch(r"\s*(-?\d+(?:\.\d+)?)(px|rem)\s*", value) if isinstance(value, str) else None
        return {"value": float(m.group(1)) if "." in m.group(1) else int(m.group(1)), "unit": m.group(2)} if m else None
    if typ == "duration":
        if isinstance(value, dict) and value.get("unit") in ("ms", "s"):
            return value
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            return ms(value)
        m = re.fullmatch(r"\s*(\d+(?:\.\d+)?)(ms|s)\s*", value) if isinstance(value, str) else None
        return {"value": float(m.group(1)) if "." in m.group(1) else int(m.group(1)), "unit": m.group(2)} if m else None
    if typ in ("number", "fontWeight"):
        return value if isinstance(value, (int, float)) and not isinstance(value, bool) else None
    if typ == "fontFamily":
        return value if isinstance(value, (str, list)) else None
    if typ == "cubicBezier":
        return value if isinstance(value, list) and len(value) == 4 else None
    return value  # composite types (shadow, typography, transition) are passed through as given


def override_plan(files, key, value, default_density):
    """Where a token override lands and in what form: {files: [..], values: {file: value}, type, new, note} or {error}.
    Existing tokens keep their type; a density token without a mode prefix changes the default density only, so the
    other densities keep their own values. New tokens go to the files of their group, in every context of a modifier,
    so names stay the same across modes (DTCG resolver rule)."""
    mode, path = split_mode_key(key)
    if mode and mode not in MODE_WORDS:
        return {"error": f"unknown mode {mode!r}; use one of {', '.join(MODE_WORDS)}"}
    parts = path.split(".")
    if not path or any(not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", q) for q in parts):
        return {"error": f"{path!r} is not a token path: use lowercase kebab-case segments, like size.row.md"}
    tokfiles = [fn for fn in files if fn.endswith(".tokens.json")]
    have = [fn for fn in tokfiles if isinstance(_node_at(files[fn], parts), dict) and "$value" in _node_at(files[fn], parts)]
    note = ""
    if have:
        typ = None
        for fn in have:
            node = _node_at(files[fn], parts)
            typ = node.get("$type") or _group_type(files[fn], parts) or typ
        targets = [fn for fn in have if (f".{mode}." in fn)] if mode else have
        if not mode and len(have) > 1 and all(".density." in fn for fn in have):
            targets = [fn for fn in have if f".{default_density}." in fn]
            note = (f"changed the {default_density} density only (the default); the other densities keep their values. "
                    f"Set one with a prefix, for example compact:{path}")
        if not targets:
            moded = sorted({fn.split(".")[-3] for fn in have if fn.count(".") >= 3})
            return {"error": f"{path} has no {mode} value: " + (f"its modes are {', '.join(moded)}" if moded else
                                                                 "it is the same in every mode, so set it without a prefix")}
        v = coerce_token_value(value, typ) if typ else value
        if v is None:
            return {"error": f"{path} is a {typ} token; {json.dumps(value)} is not a {typ} value"}
        return {"files": targets, "values": {fn: v for fn in targets}, "type": typ, "new": False, "note": note, "path": path}
    typ = infer_token_type(value, path)
    if isinstance(value, str) and value.startswith("{") and value.endswith("}"):
        tgt = value[1:-1]
        for fn in tokfiles:
            node = _node_at(files[fn], tgt.split("."))
            if isinstance(node, dict) and "$value" in node:
                typ = node.get("$type") or _group_type(files[fn], tgt.split("."))
                break
        else:
            return {"error": f"alias target {tgt} does not exist"}
    if not typ:
        return {"error": f"no token {path} yet, and the type of {json.dumps(value)} is unclear. Give a hex color, a size like 36 or "
                         "\"36px\", a duration like \"200ms\", or an alias like \"{space.16}\""}
    v = coerce_token_value(value, typ)
    if v is None:
        return {"error": f"{json.dumps(value)} is not a valid {typ} value"}
    group_ctx = None
    if mode:
        group_ctx = MODE_WORDS[mode]
    elif parts[0] == "color" and not PRIMITIVE_RE.match(path + "."):
        group_ctx = "theme"
    elif re.match(r"(space\.(inset|stack|inline|section)|size\.control)\.", path):
        group_ctx = "density"
    elif parts[0] == "motion" and parts[1:2] == ["transition"]:
        group_ctx = "motion"
    if group_ctx:
        pat = {"theme": ".color.", "density": ".density.", "motion": "motion."}[group_ctx]
        targets = sorted(fn for fn in tokfiles if pat in fn and (group_ctx != "motion" or fn.startswith("motion.")))
        if group_ctx == "theme" and not targets:
            targets = sorted(fn for fn in tokfiles if fn.startswith("semantic.color."))
    else:
        targets = ["primitives.tokens.json" if PRIMITIVE_RE.match(path) else "semantic.tokens.json"]
    if not targets:
        return {"error": f"no token file takes {path}"}
    values = {fn: v for fn in targets}
    if mode and len(targets) > 1:
        note = f"new token: {mode} gets {json.dumps(value)}; the other {group_ctx} modes start with the same value (names match across modes)"
    return {"files": targets, "values": values, "type": typ, "new": True, "note": note or f"new {typ} token in {', '.join(targets)}",
            "path": path}


def apply_token_overrides(ctx, files):
    """Overrides whose key is not a lever parameter patch or add a token: 'path' or '<mode>:path' (light, dark, spacious,
    comfortable, compact, standard, reduced). Values are DTCG; new tokens carry source: person."""
    applied = []
    ov = ctx.state.get("overrides") or {}
    default_density = ctx.params["space.densityMode"]
    # unprefixed keys first, so a mode-prefixed value for the same token wins in its mode
    for key in sorted((k for k in ov if not is_param_override(k)), key=lambda k: (":" in k, k)):
        plan = override_plan(files, key, ov[key], default_density)
        if "error" in plan:
            ctx.notes.append(f"override {key} skipped: {plan['error']}")
            continue
        parts = plan["path"].split(".")
        for fn in plan["files"]:
            node = files[fn]
            for q in parts[:-1]:
                node = node.setdefault(q, {})
            leaf = node.get(parts[-1])
            if isinstance(leaf, dict) and "$value" in leaf:
                leaf["$value"] = copy.deepcopy(plan["values"][fn])
                leaf.setdefault("$extensions", {}).setdefault(NS, {})["source"] = "person"
            else:
                node[parts[-1]] = {"$value": copy.deepcopy(plan["values"][fn]), "$type": plan["type"],
                                   "$description": "Added by a person (engine.py set).", "$extensions": {NS: {"source": "person"}}}
            applied.append(f"{fn}:{plan['path']}")
    return applied


PRIMITIVE_RE = re.compile(r"^(color\.(white|black|brand|focus|neutral-alpha|neutral|accent|action|accent2|accent3|success|warning|danger|info)\."
                          r"|color\.(white|black)$|opacity\.|space\.\d+$|radius\.(\d+|full)$|font\.(size|line-height)\.|border\.width\.\d+$"
                          r"|motion\.(duration|easing|spring)\.|elevation\.shadow\.)")


def merge_trees(a, b):
    for k, v in b.items():
        if isinstance(v, dict) and isinstance(a.get(k), dict) and "$value" not in v:
            merge_trees(a[k], v)
        else:
            a[k] = copy.deepcopy(v)
    return a


def split_tree(tree, pred, prefix=""):
    """Split a DTCG tree into (matching, rest) by token path; group $-keys go to whichever side has children."""
    yes, no = {}, {}
    meta = {k: v for k, v in tree.items() if k.startswith("$")}
    for k, v in tree.items():
        if k.startswith("$"):
            continue
        path = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict) and "$value" in v:
            (yes if pred(path) else no)[k] = v
        elif isinstance(v, dict):
            y, n = split_tree(v, pred, path)
            if y:
                yes[k] = y
            if n:
                no[k] = n
    if yes:
        yes = dict(meta, **yes)
    if no:
        no = dict(meta, **no)
    return yes, no


def generate_system(state):
    """Files follow the spec's tiering (7.4): primitives, semantic, semantic.color.<theme>, semantic.density.<mode>,
    motion.<standard|reduced>, plus the resolver and a meta file."""
    ctx = Ctx(state)
    files = {}
    prim, opacity = build_color_primitives(ctx)
    foundation = {}
    for tree in (prim, opacity, build_typography(ctx), build_space_foundation(ctx)):
        merge_trees(foundation, tree)
    dens = {dname: build_space_density(ctx, dname) for dname in DENSITIES}
    for tree in (build_shape(ctx), build_elevation(ctx), build_motion(ctx)):
        merge_trees(foundation, tree)
    p_tree, s_tree = split_tree(foundation, lambda path: bool(PRIMITIVE_RE.match(path)))
    for t in (p_tree, s_tree):
        t["$extensions"] = {NS: {"source": "formula", "note": "Every value comes from references/levers.json formulas at the dials "
                                 "recorded in opendesigner.meta.json; tokens a person detached carry source: person."}}
    files["primitives.tokens.json"] = p_tree
    files["semantic.tokens.json"] = s_tree
    for m in ctx.modes:
        files[f"semantic.color.{m}.tokens.json"] = build_color_semantic(ctx, m)
    for dname in DENSITIES:
        files[f"semantic.density.{dname}.tokens.json"] = dens[dname]
    for c in ("standard", "reduced"):
        files[f"motion.{c}.tokens.json"] = build_motion_context(ctx, c)
    applied = apply_token_overrides(ctx, files)
    files["opendesigner.resolver.json"] = build_resolver(ctx, list(files))
    ramps = {}
    for (name, mode), r in sorted(ctx.ramps.items()):
        ramps.setdefault(name, {})[mode] = {"hex": r.hexes(), "textOnSolid": r.text_on_solid,
                                            "oklch": [[rnd(r.steps[i]["L"], 3), rnd(r.steps[i]["C"], 3)] for i in range(1, 13)]}
    meta = {
        "engine": ENGINE_VERSION, "name": ctx.state.get("name"), "prefix": ctx.state["exports"].get("prefix", "ds"),
        "dials": ctx.dials, "dialSources": ctx.dial_src, "macroConflicts": ctx.conflicts,
        "preset": effective_preset(ctx.state)[0], "presetIsDefault": effective_preset(ctx.state)[1], "macros": ctx.state.get("macros"),
        "params": {k: {"value": ctx.params[k], **ctx.pmeta.get(k, {})} for k in sorted(ctx.params)},
        "color": ctx.cinfo, "ramps": ramps, "modes": ctx.modes,
        "type": ctx.type_info, "space": ctx.space_info, "density": ctx.density_info, "shape": ctx.shape_info,
        "elevation": ctx.elev_info, "motion": ctx.motion_info,
        "contrastPairs": contrast_pairs(ctx), "tokenOverrides": applied,
        "platforms": ctx.raw.get("platforms"), "inputs": ctx.raw.get("inputs"),
        "textScaling": ctx.raw.get("textScaling") or "full", "notes": ctx.notes,
    }
    meta["stateHash"] = state_hash(state)
    files["opendesigner.meta.json"] = meta
    return files, meta, ctx


# =============================================================================================
# DTCG reading: flatten, resolve aliases, permutations (used by validate and every exporter)
# =============================================================================================

DTCG_TYPES = {"color", "dimension", "fontFamily", "fontWeight", "duration", "cubicBezier", "number", "strokeStyle",
              "border", "transition", "shadow", "gradient", "typography"}


def flatten(node, prefix="", inherited=None, out=None, problems=None):
    out = {} if out is None else out
    t = node.get("$type", inherited) if isinstance(node, dict) else inherited
    if isinstance(node, dict) and "$value" in node:
        out[prefix] = {"$value": node["$value"], "$type": t, "$description": node.get("$description", ""),
                       "$extensions": node.get("$extensions", {})}
        return out
    if not isinstance(node, dict):
        return out
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if problems is not None and ("." in k or "{" in k or "}" in k):
            problems.append(f"{prefix}.{k}: token and group names must not contain '.', '{{' or '}}' (DTCG 2025.10)")
        if isinstance(v, dict):
            flatten(v, f"{prefix}.{k}" if prefix else k, t, out, problems)
    return out


def load_token_dir(tokdir):
    files = {}
    for fn in sorted(os.listdir(tokdir)):
        if fn.endswith(".json"):
            files[fn] = read_json(os.path.join(tokdir, fn))
    return files


def resolver_contexts(res):
    mods = res.get("modifiers", {})
    return {name: list(m["contexts"]) for name, m in mods.items()}


def sources_for(res, choice):
    out = []
    for entry in res["resolutionOrder"]:
        ref = entry["$ref"]
        _, kind, name = ref.split("/")
        if kind == "sets":
            out += [s["$ref"] for s in res["sets"][name]["sources"]]
        else:
            m = res["modifiers"][name]
            ctxn = choice.get(name) or m.get("default")
            out += [s["$ref"] for s in m["contexts"][ctxn]]
    return out


def deep_resolve(value, flat, trail):
    if isinstance(value, str) and value.startswith("{") and value.endswith("}"):
        path = value[1:-1]
        if path in trail:
            raise ValueError("alias cycle: " + " -> ".join(trail + [path]))
        if path not in flat:
            raise KeyError(f"alias target missing: {path} (from {trail[0]})")
        return deep_resolve(flat[path]["$value"], flat, trail + [path])
    if isinstance(value, dict) and "colorSpace" not in value:
        return {k: deep_resolve(v, flat, trail) for k, v in value.items()}
    if isinstance(value, list):
        return [deep_resolve(v, flat, trail) for v in value]
    return value


def resolve_type(path, flat, seen=None):
    t = flat[path]["$type"]
    if t:
        return t
    v = flat[path]["$value"]
    if isinstance(v, str) and v.startswith("{"):
        seen = seen or set()
        if path in seen:
            return None
        seen.add(path)
        tgt = v[1:-1]
        return resolve_type(tgt, flat, seen) if tgt in flat else None
    return None


def resolve_all(files, choice):
    res = files["opendesigner.resolver.json"]
    flat = {}
    for src in sources_for(res, choice):
        flatten(files[src], "", None, flat)
    out = {}
    for path, t in flat.items():
        out[path] = dict(t, resolved=deep_resolve(t["$value"], flat, [path]), type=resolve_type(path, flat))
    return out


def all_choices(res):
    ctxs = resolver_contexts(res)
    names = list(ctxs)
    combos = [{}]
    for n in names:
        combos = [dict(c, **{n: v}) for c in combos for v in ctxs[n]]
    return combos


def hex_of(v):
    """Hex of a resolved DTCG color value (alpha ignored)."""
    if isinstance(v, dict) and v.get("hex"):
        return v["hex"]
    if isinstance(v, dict) and v.get("colorSpace") == "oklch":
        return oklch_to_hex(*v["components"])
    if isinstance(v, dict) and v.get("colorSpace") == "srgb":
        return "#" + "".join(f"{round_half_up(c * 255):02x}" for c in v["components"])
    raise ValueError(f"not a color: {v}")


# =============================================================================================
# Validate
# =============================================================================================

COLOR_SPACES = {"srgb", "srgb-linear", "hsl", "hwb", "lab", "lch", "oklab", "oklch", "display-p3", "a98-rgb",
                "prophoto-rgb", "rec2020", "xyz-d65", "xyz-d50"}
WEIGHT_NAMES = {"thin", "hairline", "extra-light", "ultra-light", "light", "normal", "regular", "book", "medium", "semi-bold",
                "demi-bold", "bold", "extra-bold", "ultra-bold", "black", "heavy", "extra-black", "ultra-black"}
FIGMA_MODE_LIMITS = {"starter": 1, "professional": 10, "organization": 20, "enterprise": 40}


class Report:
    def __init__(self):
        self.items = []
        self.stats = {}

    SEV = {"error": "error", "warning": "warn", "warn": "warn", "advisory": "info", "info": "info"}

    def add(self, level, check, message, rule="", source="", where="", measured=None, threshold=None, fix=""):
        """One finding in the spec 6.6 shape: {rule, severity, where, measured, threshold, evidence, fix}."""
        self.items.append({"severity": self.SEV[level], "category": check, "rule": rule, "where": where, "measured": measured,
                           "threshold": threshold, "evidence": source, "fix": fix, "message": message})

    def count(self, level):
        sev = self.SEV[level]
        return sum(1 for i in self.items if i["severity"] == sev)


GEN_KEYS = ("name", "dials", "preset", "macros", "raw", "overrides", "exports")


def state_hash(state):
    """Hash of the state keys that change tokens (answers, hooks, hashes and notes do not)."""
    import hashlib
    core = {k: state.get(k) for k in GEN_KEYS}
    core["dials"] = {k: dial_value(v) for k, v in (core.get("dials") or {}).items()}
    return hashlib.sha256(json.dumps(core, sort_keys=True, ensure_ascii=False).encode()).hexdigest()[:16]


def _check_value(t, v, path, rep):
    """DTCG 2025.10 value-shape checks on a resolved value."""
    def bad(msg):
        rep.add("error", "dtcg", f"{path}: {msg}", "DTCG 2025.10 Format, $type table", "S-L07-002 (L07 A3)", path)
    if t == "color":
        if not isinstance(v, dict) or v.get("colorSpace") not in COLOR_SPACES:
            return bad("color must be an object with a known colorSpace")
        comps = v.get("components")
        if not (isinstance(comps, list) and len(comps) == 3 and all(isinstance(c, (int, float)) or c == "none" for c in comps)):
            return bad("color components must be three numbers (or 'none')")
        if "alpha" in v and not (0 <= v["alpha"] <= 1):
            bad("alpha must be 0-1")
        if "hex" in v and not re.fullmatch(r"#[0-9a-fA-F]{6}", v["hex"]):
            bad("hex fallback must be #rrggbb")
        if v["colorSpace"] == "oklch" and "hex" in v:
            want = hex_to_rgb8(oklch_to_hex(*[0 if c == "none" else c for c in comps]))
            got = hex_to_rgb8(v["hex"])
            if max(abs(a - b) for a, b in zip(want, got)) > 1:
                bad(f"hex fallback {v['hex']} does not match its OKLCH components")
    elif t == "dimension":
        if not (isinstance(v, dict) and isinstance(v.get("value"), (int, float)) and v.get("unit") in ("px", "rem")):
            bad("dimension must be {value, unit: px|rem}")
    elif t == "duration":
        if not (isinstance(v, dict) and isinstance(v.get("value"), (int, float)) and v.get("unit") in ("ms", "s")):
            bad("duration must be {value, unit: ms|s}")
    elif t == "cubicBezier":
        if not (isinstance(v, list) and len(v) == 4 and all(isinstance(x, (int, float)) for x in v) and 0 <= v[0] <= 1 and 0 <= v[2] <= 1):
            bad("cubicBezier must be [x1, y1, x2, y2] with x in [0, 1]")
    elif t == "fontWeight":
        if not ((isinstance(v, (int, float)) and 1 <= v <= 1000) or v in WEIGHT_NAMES):
            bad("fontWeight must be 1-1000 or a named weight")
    elif t == "fontFamily":
        if not (isinstance(v, str) or (isinstance(v, list) and v and all(isinstance(x, str) for x in v))):
            bad("fontFamily must be a string or a list of strings")
    elif t == "number":
        if not isinstance(v, (int, float)):
            bad("number must be a JSON number")
    elif t == "typography":
        need = {"fontFamily", "fontSize", "fontWeight", "letterSpacing", "lineHeight"}
        if not (isinstance(v, dict) and need <= set(v)):
            return bad("typography needs fontFamily, fontSize, fontWeight, letterSpacing, lineHeight")
        _check_value("dimension", v["fontSize"], path + ".fontSize", rep)
        _check_value("number", v["lineHeight"], path + ".lineHeight", rep)
    elif t == "shadow":
        layers = v if isinstance(v, list) else [v]
        for lay in layers:
            if not (isinstance(lay, dict) and {"color", "offsetX", "offsetY", "blur", "spread"} <= set(lay)):
                return bad("shadow layers need color, offsetX, offsetY, blur, spread")
    elif t == "transition":
        if not (isinstance(v, dict) and {"duration", "delay", "timingFunction"} <= set(v)):
            bad("transition needs duration, delay, timingFunction")
    elif t not in DTCG_TYPES:
        bad(f"unknown $type {t!r}")


def _px(v):
    return v["value"] if v.get("unit") == "px" else v["value"] * 16


def validate_files(files, state, rep):
    meta = files.get("opendesigner.meta.json") or {}
    res = files.get("opendesigner.resolver.json")
    if not res:
        rep.add("error", "dtcg", "tokens/opendesigner.resolver.json is missing; run generate", "DTCG Resolver 2025.10", "S-L07-004")
        return
    # ---- resolver structure
    if res.get("version") != "2025.10":
        rep.add("error", "dtcg", "resolver version must be \"2025.10\"", "DTCG Resolver 2025.10", "S-L07-004")
    for entry in res.get("resolutionOrder", []):
        ref = entry.get("$ref", "")
        parts = ref.split("/")
        if len(parts) != 3 or parts[1] not in ("sets", "modifiers") or parts[2] not in res.get(parts[1], {}):
            rep.add("error", "dtcg", f"resolutionOrder entry {ref} does not point at a set or modifier", "DTCG Resolver 2025.10", "S-L07-004")
    for name, m in res.get("modifiers", {}).items():
        if not m.get("contexts"):
            rep.add("error", "dtcg", f"modifier {name} has no contexts", "DTCG Resolver 2025.10", "S-L07-004")
        elif len(m["contexts"]) < 2:
            rep.add("warning", "dtcg", f"modifier {name} has one context; the spec says SHOULD have two or more", "DTCG Resolver 2025.10", "S-L07-004")
        if m.get("default") not in m.get("contexts", {}):
            rep.add("error", "dtcg", f"modifier {name} default {m.get('default')!r} is not one of its contexts", "DTCG Resolver 2025.10", "S-L07-004")
        for cname, srcs in m.get("contexts", {}).items():
            for s in srcs:
                if s["$ref"] not in files:
                    rep.add("error", "dtcg", f"{name}/{cname} source {s['$ref']} is missing", "DTCG Resolver 2025.10", "S-L07-004")
    for sname, sset in res.get("sets", {}).items():
        for s in sset.get("sources", []):
            if s["$ref"] not in files:
                rep.add("error", "dtcg", f"set {sname} source {s['$ref']} is missing", "DTCG Resolver 2025.10", "S-L07-004")
    if rep.count("error"):
        return
    # ---- names, types, value shapes (per file)
    problems = []
    for fn, tree in files.items():
        if fn.endswith(".tokens.json"):
            flatten(tree, "", None, {}, problems)
    for pmsg in problems:
        rep.add("error", "dtcg", pmsg, "DTCG 2025.10 names", "S-L07-002")
    # ---- orthogonal modifiers and consistent names across contexts
    for name, m in res.get("modifiers", {}).items():
        sets_ = []
        for cname, srcs in m["contexts"].items():
            paths = set()
            for s in srcs:
                paths |= set(flatten(files[s["$ref"]]))
            sets_.append((cname, paths))
        base_c, base_p = sets_[0]
        for cname, paths in sets_[1:]:
            diff = base_p ^ paths
            if diff:
                rep.add("error", "dtcg", f"modifier {name}: contexts {base_c} and {cname} define different tokens ({sorted(diff)[:4]}...)",
                        "Names never change across modes; only values do", "DC-L01-18, S-L07-112")
    mod_paths = {}
    for name, m in res.get("modifiers", {}).items():
        for srcs in m["contexts"].values():
            for s in srcs:
                for pth in flatten(files[s["$ref"]]):
                    mod_paths.setdefault(pth, set()).add(name)
    for pth, owners in mod_paths.items():
        if len(owners) > 1:
            rep.add("error", "dtcg", f"{pth} is set by more than one modifier ({', '.join(sorted(owners))})",
                    "Resolver modifiers should be orthogonal", "S-L07-004")
    # ---- every permutation resolves
    choices = all_choices(res)
    resolved = {}
    for ch in choices:
        try:
            resolved[tuple(sorted(ch.items()))] = resolve_all(files, ch)
        except (KeyError, ValueError) as ex:
            rep.add("error", "dtcg", f"permutation {ch}: {ex}", "Aliases must resolve without cycles", "S-L07-002")
    rep.stats["permutations"] = len(choices)
    if rep.count("error"):
        return
    first = next(iter(resolved.values()))
    rep.stats["tokens"] = len(first)
    for key, toks in resolved.items():
        for pth, t in toks.items():
            if not t["type"]:
                rep.add("error", "dtcg", f"{pth}: no $type on the token, its groups or its alias target", "DTCG 2025.10 $type", "S-L07-002")
            else:
                _check_value(t["type"], t["resolved"], pth, rep)
        break  # value shapes do not change across permutations except values; one pass is enough
    for key, toks in list(resolved.items())[1:]:
        for pth, t in toks.items():
            if t["type"] in ("color", "dimension", "duration"):
                _check_value(t["type"], t["resolved"], pth, rep)

    def pick(**kw):
        for key, toks in resolved.items():
            d = dict(key)
            if all(d.get(k, v) == v for k, v in kw.items()):
                return toks
        return first
    modes = meta.get("modes") or (list(res["modifiers"]["theme"]["contexts"]) if "theme" in res.get("modifiers", {}) else ["light"])
    dials = meta.get("dials", {})
    params = {k: v.get("value") for k, v in meta.get("params", {}).items()}

    # ---- contrast (WCAG 2.2, no rounding)
    lows, n_pairs = {}, 0
    for pr in meta.get("contrastPairs", []):
        toks = pick(theme=pr["mode"])
        if pr["fg"] not in toks or pr["bg"] not in toks:
            rep.add("error", "contrast", f"{pr['mode']}: pair {pr['fg']} on {pr['bg']} names a missing token", pr["rule"], "DC-L01-22")
            continue
        bg = hex_of(toks[pr["bg"]]["resolved"])
        fgv = toks[pr["fg"]]["resolved"]
        fg = hex_of(fgv)
        if isinstance(fgv, dict) and fgv.get("alpha") is not None:
            fg = composite(fg, fgv["alpha"], bg)
        ratio = contrast(fg, bg)
        n_pairs += 1
        ok = ratio >= pr["min"]
        if not ok and pr.get("inner") and pr["inner"] in toks:
            inner = hex_of(toks[pr["inner"]]["resolved"])
            ok = contrast(inner, bg) >= 3.0 and contrast(inner, fg) >= 3.0  # two-tone ring (L09 M12 pattern)
            if ok:
                rep.add("advisory", "contrast", f"{pr['mode']}: focus color is {ratio:.2f}:1 on {pr['bg']}; the two-tone inner ring carries 3:1",
                        pr["rule"], "DC-L04-09")
        key = (pr["mode"], pr["kind"])
        if key not in lows or ratio < lows[key][0]:
            lows[key] = (ratio, pr["fg"], pr["bg"])
        if not ok:
            lvl = "warning" if pr.get("level") == "warning" else "error"
            rep.add(lvl, "contrast", f"{pr['mode']}: {pr['fg']} ({fg}) on {pr['bg']} ({bg}) is {ratio:.2f}:1, needs {pr['min']}:1",
                    pr["rule"], "DC-L01-22, S-L01-022, S-L01-023", f"{pr['mode']}:{pr['fg']} on {pr['bg']}",
                    measured=rnd(ratio, 3), threshold=pr["min"],
                    fix="Point the role at a step further from the background: steps 11-12 for text, 8 or higher for edges. "
                        "Or remove the override that detached it. Generated steps always pass.")
    rep.stats["contrastPairs"] = n_pairs
    rep.stats["lowest"] = {f"{m} {k}": f"{r:.2f}:1 ({fg} on {bg})" for (m, k), (r, fg, bg) in sorted(lows.items())}
    for mode in modes:
        toks = pick(theme=mode)
        for fg, need in (("color.text.primary", 75), ("color.text.secondary", 60)):
            for bg in ("color.surface.base", "color.surface.raised"):
                if fg in toks and bg in toks:
                    lc = abs(apca_lc(hex_of(toks[fg]["resolved"]), hex_of(toks[bg]["resolved"])))
                    if lc < need:
                        rep.add("advisory", "apca", f"in {mode} mode, {words_of(fg)} on the {words_of(bg)} scores Lc {lc:.0f} on APCA, a newer reading-contrast score. {need} or more is advised",
                                "APCA advisory only; WCAG 3 contrast is undetermined", "S-L01-026, S-L01-021")

    # ---- visible states (U5 F24): hover and pressed must differ from their solid fill
    n_states = 0
    for mode in modes:
        toks = pick(theme=mode)
        for base_ in sorted(k for k in toks if re.fullmatch(r"color\.bg\.[a-z0-9-]+\.(bold|primary)", k)):
            for st, need in (("hover", STATE_MIN["hover"]), ("pressed", STATE_MIN["pressed"])):
                sp_ = f"{base_}-{st}"
                if sp_ not in toks:
                    continue
                n_states += 1
                bh, sh = hex_of(toks[base_]["resolved"]), hex_of(toks[sp_]["resolved"])
                ratio = contrast(sh, bh)
                if ratio < need - 0.005:
                    rep.add("warning", "states", f"in {mode} mode, {words_of(sp_)} ({sh}) is only {ratio:.2f}:1 from {words_of(base_)} ({bh}); "
                            f"people may not see the {st} state. {need}:1 or more is needed", "Visible states", "DC-L01-17",
                            f"{mode}:{sp_}", measured=rnd(ratio, 3), threshold=need,
                            fix="Remove the override on this state, or point it at a step further from the fill.")
    rep.stats["statePairs"] = n_states
    # ---- font licences (U5 F21): a brand face outside its licence is never shipped silently
    faces = (meta.get("type") or {}).get("faces") or {}
    plats_ = set(state.get("raw", {}).get("platforms") or [])
    for role, f in faces.items():
        if not f or f.get("open") or f.get("face") in (None, "=textFace"):
            continue
        if f.get("web") is False or f.get("app") is False:
            rep.add("advisory", "licence", f"{f.get('note')}.", "Font licence scope", "Q-type-02, hooks H-type")
        apps = plats_ & {"ios", "android", "desktop", "macos", "windows", "ipados"}
        if apps and f.get("app") is None:
            rep.add("warning", "licence", f"the {role} font {f['face']} has no recorded app licence, but the product ships on "
                    f"{', '.join(sorted(apps))}. The Swift and Compose files use the system font until you record it: "
                    "engine.py set raw.fontLicence '{\"web\": true, \"app\": true}'", "Font licence scope", "Q-type-02, hooks H-type")

    # ---- targets (L14 device floors; density never shrinks hit areas)
    toks = first
    plats = set(meta.get("platforms") or state.get("raw", {}).get("platforms") or ["web"])
    tg = {k.split(".")[-1]: _px(v["resolved"]) for k, v in toks.items() if k.startswith("size.target.")}
    if "min" not in tg:
        rep.add("error", "targets", "size.target.min is missing", "Minimum target size (WCAG 2.2 SC 2.5.8)", "DC-L03-12, L14 I-1")
    floors = {"pointer": (24, "WCAG 2.2 SC 2.5.8 (24x24 CSS px)", "S-L03-035"),
              "touch": (48 if "android" in plats else 44, "Apple 44pt / Material 48dp", "S-L03-033, S-L03-029"),
              "remote": (66, "tvOS 66pt", "S-L14-012"), "gaze": (60, "visionOS 60pt", "S-L14-012"),
              "vehicle": (76, "Design for Driving 76dp", "S-L14-037")}
    for k, (floor, rule, src) in floors.items():
        if k in tg and tg[k] < floor:
            rep.add("error", "targets", f"size.target.{k} is {tg[k]:g}px, below the {floor}px minimum", rule, f"DC-L14-03, {src}",
                    f"size.target.{k}", measured=tg[k], threshold=floor, fix=f"Set size.target.{k} to at least {floor}px.")
    for key, t2 in resolved.items():
        for k, v in t2.items():
            if k.startswith("size.target.") and _px(v["resolved"]) != tg.get(k.split(".")[-1]):
                rep.add("error", "targets", f"{k} changes with {dict(key)}. Density must never change tap areas", "L14 I-1", "DC-L03-11")
                break
    ctl_min = min(_px(t2[k]["resolved"]) for t2 in resolved.values() for k in t2 if k.startswith("size.control."))
    if ctl_min < 24 and tg.get("min", 0) < 24:
        rep.add("error", "targets", f"the smallest control is {ctl_min:g}px, and there is no 24px tap-area token", "target < 24x24 CSS px (lint error)", "L13-E1-level2, S-L03-035")
    elif tg.get("min") and ctl_min < tg["min"]:
        rep.add("advisory", "targets", f"the smallest control is {ctl_min:g}px tall. Give it a {tg['min']:g}px {term('hit area')} with padding "
                "(size.target.min), never a smaller one", "L14 I-1", "DC-L03-12, S-L03-029")
    rep.stats["targets"] = tg

    # ---- lint: type
    sizes = sorted({_px(v["resolved"]) for k, v in toks.items() if k.startswith("font.size.")})
    rep.stats["typeSizes"] = sizes
    if len(sizes) > 10:
        rep.add("warning", "lint", f"{len(sizes)} text sizes; 8 to 10 is the usual range", "Type scale size count", "DC-L02-10")
    if sizes and sizes[0] < 11:
        rep.add("warning", "lint", f"the smallest text size, {sizes[0]:g}px, is under 11px", "Minimum legible size 11pt/sp", "S-L02-001, S-L02-005")
    styles = {k: v["resolved"] for k, v in toks.items() if k.startswith("text.") and not k.startswith(("text.emphasized.", "text.numeric."))
              and v["type"] == "typography"}  # emphasized and numeric variants pair with a baseline style; they are not extra levels
    if len(styles) > 15:
        rep.add("warning", "lint", f"{len(styles)} text styles; 12 to 15 is the usual range", "Type style count", "DC-L02-10")
    body_weights = {v["fontWeight"] for k, v in styles.items() if not k.startswith("text.display")}
    if len(body_weights) > 3:
        rep.add("warning", "lint", f"{len(body_weights)} font weights outside display styles ({sorted(body_weights)}). Only two or three look different",
                "Hierarchy tiers: weights 2-3", "L15-P03, S-L15-038")
    heads = sorted(((_px(v["fontSize"]), v["fontWeight"], k) for k, v in styles.items()
                    if k.split(".")[1] in ("title", "headline", "display")), key=lambda x: (x[0], x[1]))
    for (s1, w1, k1), (s2, w2, k2) in zip(heads, heads[1:]):
        if s2 / s1 - 1 < 0.1 and abs(w2 - w1) < 200 and not (s1 == s2 and w1 == w2):
            rep.add("warning", "lint", f"{k1} ({s1:g}px/{w1}) and {k2} ({s2:g}px/{w2}) look almost the same: under 10% apart in size and under 200 in weight",
                    "Adjacent hierarchy levels must differ visibly", "DC-L15-02 (200 [inferred])")
    text_tiers = [k for k in toks if re.fullmatch(r"color\.text\.(primary|secondary|tertiary|quaternary|muted|subtle)", k)]
    if len(text_tiers) > 3:
        rep.add("warning", "lint", f"{len(text_tiers)} gray text colors; three is the most that stay distinct", "Hierarchy tiers: 3 text colors", "L15-P04, S-L15-038")

    # ---- lint: motion
    if "motion" not in res.get("modifiers", {}) or "reduced" not in res["modifiers"]["motion"]["contexts"]:
        rep.add("error", "lint", "no reduced-motion mode", "Reduced motion as a token mode (WCAG 2.3.3 treated as required)", "DC-L04-25, L14-I-13")
    else:
        red = pick(motion="reduced")
        mv = red.get("motion.transition.move")
        if not mv or mv["resolved"]["duration"]["value"] != 0:
            rep.add("error", "lint", "reduced motion still moves things: motion.transition.move must be 0ms in the reduced context",
                    "Reduced motion: travel to opacity, travel durations 0", "DC-L04-25, S-L09-458")
    std = pick(motion="standard")
    for k, v in std.items():
        if k.startswith("motion.transition."):
            dms = v["resolved"]["duration"]["value"] * (1000 if v["resolved"]["duration"]["unit"] == "s" else 1)
            if dms > 500:
                rep.add("warning", "lint", f"{k} takes {dms}ms. Over 500ms feels slow", "transition-over 500ms", "L13-E1 [inferred link]")
            elif dms > 400:
                rep.add("advisory", "lint", f"{k} takes {dms}ms. Changes feel instant only up to 400ms", "Doherty threshold 400ms", "L13-B5, DC-L04-20")
    macros = [m if isinstance(m, str) else m.get("id") for m in (meta.get("macros") or [])]
    for k, v in toks.items():
        if k.startswith("motion.spring.") and v["type"] == "transition":
            sp = (v.get("$extensions") or {}).get(NS, {}).get("spring")
            if sp and 1 - sp["dampingRatio"] > 0.2 and "playful" not in macros:
                rep.add("warning", "lint", f"{k} bounces {1 - sp['dampingRatio']:.2f}, over 0.2, but the playful feel is not chosen",
                        "Bounce cap", "DC-L04-19")
    # ---- lint: focus
    if "color.border.focus" not in toks or "focus.ring.width" not in toks:
        rep.add("error", "lint", "the focus outline tokens are missing (color.border.focus, focus.ring.width)", "Visible focus (WCAG 2.4.7, 2.4.13)", "DC-L04-09")
    elif _px(toks["focus.ring.width"]["resolved"]) < 2:
        rep.add("error", "lint", "the focus ring is thinner than 2px", "Focus ring 2px + 2px offset", "DC-L04-09, L14-I-5")
    # ---- lint: shape
    rc = toks.get("radius.control")
    rcont = toks.get("radius.container")
    if rc and rcont:
        a_, b_ = _px(rc["resolved"]), _px(rcont["resolved"])
        if a_ == b_ and 0 < a_ < FULL:
            rep.add("warning", "lint", f"radius.control and radius.container are both {a_:g}px; nested corners will look uneven", "Equal nested radii read as uneven", "DC-L04-05")
        nst = toks.get("radius.nested")
        if nst and b_ > 0 and _px(nst["resolved"]) >= b_:
            rep.add("error", "lint", "radius.nested is not smaller than radius.container", "Nested radius = outer - padding", "DC-L04-05, S-L04-057")
    # ---- lint: materials
    if any(k == "color.surface.glass" for k in toks) and "color.surface.glass-fallback" not in toks:
        rep.add("error", "lint", "a glass surface has no solid fallback for people who turn off transparency", "Materials emit a solid twin (Reduce Transparency)", "DC-L04-16")
    # ---- lint: spacing (inner < outer, per density)
    if "density" in res.get("modifiers", {}):
        for dname in res["modifiers"]["density"]["contexts"]:
            t2 = pick(density=dname)
            inner = _px(t2["space.stack.md"]["resolved"])
            outer = _px(t2["space.section.sm"]["resolved"])
            if not (inner < outer and inner <= outer / 2):
                rep.add("error", "lint", f"{dname}: the inner gap ({inner:g}px) must be at most half the outer gap ({outer:g}px)",
                        "Proximity: inner <= half the outer gap", "L15-P16, DC-L03-24")
    ladder = {_px(v["resolved"]) for k, v in toks.items() if re.fullmatch(r"space\.\d+", k)}
    for k, v in toks.items():
        if re.match(r"space\.(inset|stack|inline|section)\.", k) and _px(v["resolved"]) not in ladder:
            rep.add("warning", "lint", f"{k} = {_px(v['resolved']):g}px is not on the spacing scale", "Spacing on scale", "DC-L03-02")
    # ---- lint: dial combinations
    if dials:
        if dials.get("expression", 0) > 66 and (state.get("raw", {}).get("domain") or "").lower() == "high-trust":
            rep.add("warning", "lint", "a very expressive look in a money, health or government product can cost trust", "expressive-high-trust", "S-L06-010")
        if dials.get("colorfulness", 0) > 75 and dials.get("density", 0) > 66:
            rep.add("warning", "lint", "vivid color on a dense layout can feel noisy", "vivid-and-dense", "S-L15-047")
        if params.get("signifier.minStrength") == "minimal-allowed" and dials.get("density", 0) > 33:
            rep.add("warning", "lint", "buttons and links barely look clickable on a layout that is not roomy", "minimal-signifiers-dense", "S-L15-004")
        if dials.get("expression", 0) > 66 and (state.get("raw", {}).get("domain") or "").lower() in ("finance", "banking", "fintech"):
            rep.add("warning", "lint", "a very expressive look in a finance product can cost trust", "expressive-finance", "S-L06-010")
    if (effective_preset(state)[0] or meta.get("preset")) == "soft":
        rep.add("warning", "lint", "the soft (neumorphic) look fails 3:1 edge contrast by design", "neumorphic-preset", "S-L15-060")
    for c in meta.get("macroConflicts") or []:
        rep.add("warning", "lint", f"the feel words {', '.join(c['macros'])} pull {c['dial']} in opposite directions. Pick which one wins",
                "Macro conflict", "L06 4.2 usage note")
    if (meta.get("color") or {}).get("placeholderBrand") and dials.get("colorfulness", 0) > 10:
        rep.add("warning", "lint", "no brand color yet, so the accent uses a stand-in blue", "Brand color is a raw input", "DC-L06-06")
    # ---- modes and tool limits
    flags = state.get("raw", {}).get("flags", {})
    if flags.get("darkMode", True) and len(modes) < 2:
        rep.add("error", "lint", "dark mode is on (flags.darkMode), but there is no dark theme", "Dark mode is a separate mapping", "DC-L01-18")
    plan = (state.get("exports") or {}).get("figmaPlan", "professional")
    limit = FIGMA_MODE_LIMITS.get(plan, 10)
    biggest = max([len(m["contexts"]) for m in res.get("modifiers", {}).values()] or [1])
    if biggest > limit:
        rep.add("warning", "export", f"Figma {plan} allows {limit} mode(s) per collection, and the largest modifier has {biggest}. "
                "The Figma export splits them into separate collections.", "Figma plan limits", "S-L07-014, S-L07-038")
    # ---- scale monotonicity (spec 6.3)
    def mono(vals, name, strict=True):
        bad_ = [(a, b) for a, b in zip(vals, vals[1:]) if (b <= a if strict else b < a)]
        if bad_:
            rep.add("error", "lint", f"{name} does not grow step by step: {bad_[0][0]:g} then {bad_[0][1]:g}", "Scales increase step by step",
                    "DC-L02-09, DC-L03-02, DC-L04-20", name)
    mono(sizes, "font.size scale")
    mono(sorted(ladder), "space ladder")
    dur = [toks[f"motion.duration.{k}"]["resolved"]["value"] for k in ("instant", "micro", "short", "medium", "long", "extra")
           if f"motion.duration.{k}" in toks]
    mono(dur, "motion.duration ladder", strict=False)
    for mode in modes:
        t2 = pick(theme=mode)
        ramps_ = sorted({k.split(".")[1] for k in t2 if re.fullmatch(rf"color\.[a-zA-Z0-9-]+\.{mode}\.\d+", k)} - {"neutral-alpha"})
        for rname in ramps_:
            ys = [luminance(hex_of(t2[f"color.{rname}.{mode}.{i}"]["resolved"])) for i in range(1, 13)]
            seg = [ys[i] for i in list(range(0, 8)) + [10, 11]]  # steps 1-8 and 11-12; 9-10 may be light fills
            ok = all(b <= a for a, b in zip(seg, seg[1:])) if mode == "light" else all(b >= a for a, b in zip(seg, seg[1:]))
            if not ok:
                rep.add("error", "lint", f"color.{rname}.{mode} shades are out of order (steps 1-8 and 11-12 must get steadily darker or lighter)",
                        "Ramp steps are ordered by contrast", "DC-L01-03", f"color.{rname}.{mode}")
    # ---- orphans: primitives no semantic token uses (info only; ramps keep spare steps on purpose)
    used = set()
    for fn, tree in files.items():
        if fn.endswith(".tokens.json") and not fn.startswith("primitives"):
            used |= set(re.findall(r"\{([^{}]+)\}", json.dumps(tree)))
    prim_tree = files.get("primitives.tokens.json")
    if prim_tree:
        pp = set(flatten(prim_tree))
        orphans = sorted(p for p in pp - used if re.match(r"(space|radius|font\.size|border\.width|motion\.(duration|easing))\.", p))
        rep.stats["orphans"] = orphans
        if orphans:
            rep.add("advisory", "lint", f"{len(orphans)} scale steps are not used by any named value yet (for example {', '.join(orphans[:3])}). "
                    "That is fine if you plan to use them", "Orphan tokens", "spec 6.3")
    # ---- coverage (block statuses from the interview)
    blocks = state.get("blocks") or {}
    if blocks:
        counts = {}
        for v in blocks.values():
            st = v.get("status") if isinstance(v, dict) else v
            counts[st] = counts.get(st, 0) + 1
        rep.stats["coverage"] = counts
        if counts.get("pending"):
            rep.add("advisory", "coverage", f"{counts['pending']} building blocks still pending: " + ", ".join(sorted(k for k, v in blocks.items()
                    if (v.get("status") if isinstance(v, dict) else v) == "pending")[:12]), "Nothing missed", "BRIEF req. 5")
    # ---- designer-owned assets (coverage, never an error)
    open_hooks = [(h, v) for h, v in (state.get("hooks") or {}).items() if (v or {}).get("status", "pending") in ("pending", "unknown")]
    if open_hooks:
        names = [hook_label(h, v) for h, v in open_hooks]
        rep.add("advisory", "hooks", f"{len(open_hooks)} assets a person must make, not asked about yet: {'; '.join(names)}",
                "Designer hooks, not designer replacement", "BRIEF req. 2, Q-brand-08", where=", ".join(h for h, _ in open_hooks))


def hook_label(hid, rec):
    """Plain asset name for a hook id: 'H-logo' -> 'logo, wordmark, symbol, lockups' (from hooks.json via state)."""
    name = (rec or {}).get("name") or dict((h, n) for h, n, _q in hook_catalog()).get(hid) or hid
    return name[:1].lower() + name[1:] if name[1:2].islower() else name


def validate_dir(d, write_state_hash=True):
    rep = Report()
    state_path = os.path.join(d, "state.json")
    state = merge_defaults(read_json(state_path)) if os.path.exists(state_path) else default_state()
    tokdir = os.path.join(d, "tokens")
    if not os.path.isdir(tokdir):
        rep.add("error", "setup", "there is no tokens/ folder yet. Run `engine.py generate` first", "", "")
        return rep
    files = load_token_dir(tokdir)
    meta = files.get("opendesigner.meta.json") or {}
    if os.path.exists(state_path) and meta.get("stateHash") and meta["stateHash"] != state_hash(read_json(state_path)):
        rep.add("warning", "setup", "the tokens are older than state.json. Run `engine.py generate`", "", "")
    validate_files(files, state, rep)
    return rep


TERM_DEFAULTS = {  # plain voice first (BRIEF req. 12); a glossary file, when present, overrides these
    "contrast": "contrast", "non-text contrast": "edge contrast", "hit area": "tap area", "focus ring": "focus outline",
    "token": "design value", "semantic token": "named design value", "primitive": "base value", "resolver": "mode map",
    "reduced motion": "reduced motion", "type scale": "text sizes", "spacing ladder": "spacing steps", "radius": "corner rounding",
    "elevation": "depth", "density": "density", "dial": "dial",
}
_GLOSSARY = None
_GLOSSARY_FULL = {}


def glossary():
    """Plain names from synthesis/glossary.json or references/glossary.json when another session has written one."""
    global _GLOSSARY
    if _GLOSSARY is None:
        _GLOSSARY = {}
        for path in (os.path.join(REFERENCES, "glossary.json"), os.path.join(SKILL_ROOT, "..", "..", "synthesis", "glossary.json")):
            if os.path.exists(path):
                try:
                    data = read_json(path)
                except ValueError:
                    continue
                items = data.get("terms", data) if isinstance(data, dict) else data
                if isinstance(items, dict):
                    items = [dict(v, term=k) if isinstance(v, dict) else {"term": k, "plain": v} for k, v in items.items()]
                for it in items if isinstance(items, list) else []:
                    if isinstance(it, dict):
                        key = str(it.get("term") or it.get("id") or it.get("name") or "").lower()
                        plain = it.get("plain") or (it.get("voices") or {}).get("plain")
                        if key and isinstance(plain, str):
                            _GLOSSARY[key] = plain
                            _GLOSSARY_FULL[key] = it
                break
    return _GLOSSARY


def short_line(key):
    """The one-line 'Designers: X · Code: Y' note for a glossary term (synthesis/THREE-VOICES.md), or ''."""
    glossary()
    it = _GLOSSARY_FULL.get(key.lower()) or {}
    ds, cn = it.get("designer_says"), it.get("code_name")
    return f"Designers: {ds} · Code: `{cn}`" if ds and cn else ""


def term(key):
    g = glossary()
    v = g.get(key.lower())
    if v:
        return v.split(".")[0].split(";")[0].strip()[:60]  # a short name, not the whole definition
    return TERM_DEFAULTS.get(key, key)


def words_of(path):
    """color.bg.neutral.subtle-hover -> 'neutral subtle hover background' (plain words for a token path)."""
    parts = [re.sub(r"(?<=[a-z0-9])([A-Z])", lambda m: " " + m.group(1).lower(), x).replace("-", " ") for x in path.split(".")]
    if parts and parts[0] == "color":
        parts = parts[1:]
    kind = {"bg": "background", "text": "text", "border": "border", "surface": "surface", "icon": "icon"}.get(parts[0] if parts else "", None)
    rest = [x for x in parts[1:]]
    if kind == "text" and rest and rest[0].startswith("on "):
        return f"text on {rest[0][3:]} fills"
    return " ".join(rest + ([kind] if kind else parts[:1])).strip()


def plain_of(it):
    """One short plain sentence per finding; the rule and source id go at the end of the printed line."""
    cat, where, m, th = it["category"], it.get("where") or "", it.get("measured"), it.get("threshold")
    if cat == "contrast" and " on " in where and ":" in where:
        mode, pair = where.split(":", 1)
        fg, bg = pair.split(" on ")
        what = "hard to read" if (".text." in fg) else "too faint to see"
        return f"In {mode} mode, {words_of(fg)} on {words_of(bg)} is {what}: {term('contrast')} {m}:1, needs {th}:1."
    if cat == "targets" and m is not None:
        return f"{words_of(where) or where} is too small to tap or click: {m:g}px, needs {th:g}px."
    if cat == "dtcg":
        return "The token files break the DTCG file format: " + it["message"]
    if cat == "apca":
        return "Advice only: " + it["message"]
    if cat == "hooks":
        return "Not asked yet (assets a person must make): " + it["message"].split(": ", 1)[-1]
    return it["message"][:1].upper() + it["message"][1:]


def print_report(rep, d, as_json=False):
    for it in rep.items:
        it["plain"] = plain_of(it)
    if as_json:
        print(json.dumps({"dir": d, "errors": rep.count("error"), "warnings": rep.count("warning"),
                          "advisories": rep.count("advisory"), "items": rep.items, "stats": rep.stats}, indent=2))
        return
    label = {"error": "ERROR", "warn": "WARN ", "info": "NOTE "}
    ne, nw, ni = rep.count("error"), rep.count("warning"), rep.count("advisory")
    head = "Passes: no errors." if not ne else f"Fails: {ne} error{'s' if ne != 1 else ''} to fix before you export."
    print(f"{head} {nw} warning{'s' if nw != 1 else ''}, {ni} note{'s' if ni != 1 else ''}.  ({d})")
    for sev in ("error", "warn", "info"):
        for it in rep.items:
            if it["severity"] != sev:
                continue
            cite = "; ".join(x for x in (it["rule"], it["evidence"]) if x)
            print(f"{label[sev]} {it['plain']}" + (f"  [{cite}]" if cite else ""))
            if it.get("fix") and sev != "info":
                print(f"      Fix: {it['fix']}")
    st = rep.stats
    print(f"Checked {st.get('contrastPairs', 0)} color pairs in every mode, {st.get('permutations', 0)} mode combinations and "
          f"{st.get('tokens', 0)} tokens.")


# =============================================================================================
# State editing: set, pick, lock (the OD:set / OD:pick grammar maps one-to-one onto these)
# =============================================================================================

TOP_KEYS = {"name", "summary", "context", "dials", "preset", "macros", "raw", "overrides", "answers", "principles",
            "components", "hooks", "exports", "locks", "zoom", "blocks", "references", "taste", "waivers", "mode", "profile"}
VOICES = ["plain", "designer", "engineer"]  # BRIEF req. 12: plain first
# Q-scope-06 surface modes [S-L17-007]. Tokens stay global: the main surface sets raw.productType, any Persuade or
# Experience surface sets raw.marketingSurfaces, and each surface gets its density mode and hero rule in the docs [inferred].
SURFACE_MODES = {
    "persuade": {"name": "Persuade", "productType": "marketing", "density": "spacious",
                 "rule": "one hero line per page; sections, not card grids"},
    "operate": {"name": "Operate", "productType": "work-tool", "density": None,
                "rule": "no hero; cards only to group related data"},
    "read": {"name": "Read", "productType": "content", "density": "comfortable",
             "rule": "no hero; `text.body.lg` for long text; no cards around running text"},
    "experience": {"name": "Experience", "productType": "marketing", "density": "spacious",
                   "rule": "hero moments and big imagery allowed; display styles welcome"},
}


def surface_list(value):
    """Q-scope-06 answer -> [{name, mode}] with the main surface first. Takes a mode word, a list of mode words,
    a list of {name, mode}, or 'name:mode' strings."""
    items = value if isinstance(value, list) else [value]
    out = []
    for it in items:
        if isinstance(it, dict):
            name, mode = it.get("name") or "", str(it.get("mode") or "")
        elif isinstance(it, str) and ":" in it:
            name, mode = (x.strip() for x in it.split(":", 1))
        else:
            name, mode = "", str(it)
        key = mode.strip().lower()
        if key in SURFACE_MODES:
            out.append({"name": name or SURFACE_MODES[key]["name"] + " surface", "mode": SURFACE_MODES[key]["name"]})
    return out


def surface_rule(surface, density_default):
    info = SURFACE_MODES.get(str(surface.get("mode", "")).lower()) if isinstance(surface, dict) else None
    if not info:
        return ""
    return f"density {info['density'] or density_default}; {info['rule']}"


FIGMA_PLAN_OF = {"figma-starter": "starter", "figma-pro": "professional", "figma-org": "organization", "figma-ent": "enterprise"}  # Q-tool-03
BRAND_ROWS = {"A": ("playful", "serious"), "B": ("friendly", "authoritative"), "C": ("minimal", "rich"),
              "D": (None, None), "E": ("premium", "everyday"), "F": ("modern", "heritage"), "G": ("bold", "deferential")}


EXTENDED_COMPONENTS = [  # Q-comp-02 "extended": about 25 more parts (DC-L08-01 long tail) [inferred list]
    "date-picker", "combobox", "multi-select", "file-upload", "toast", "skeleton", "pagination", "stepper", "tag", "chip",
    "segmented-control", "icon-button", "drawer", "sheet", "navigation-bar", "tab-bar", "toolbar", "search-field", "empty-state",
    "data-table", "tree-view", "rating", "carousel", "command-palette", "number-field"]
AI_COMPONENTS = ["logo", "ai-label", "ai-button", "chat-message", "prompt-input"]  # Q-comp-02 "logo-ai"
UNSET = "__unset__"  # an answer effect that removes an earlier value, so the engine default applies again
LABEL = "__label__"  # an answer effect whose value is the chosen option's plain label

# Answer -> engine input, per question and option (U5: every answer reaches the system, or says why not).
# Values are [inferred] positions inside the levers.json bands that each option names.
ANSWER_TABLE = {
    "Q-aud-01": {"dense": {"dials.density": 80}, "regular": {"dials.density": 50}, "large": {"dials.density": 15}},
    "Q-aud-02": {"high-trust": {"raw.domain": "high-trust"}, "work": {"raw.domain": "work"}, "consumer": {"raw.domain": "consumer"},
                 "play": {"raw.domain": "play"}},
    "Q-aud-03": {"wcag22-aa": {"raw.contrastTarget": "AA"}, "wcag22-aa-plus": {"raw.contrastTarget": "AAA"},
                 "wcag22-a": {"raw.contrastTarget": "AA"}},  # AA stays the floor (guardrails)
    "Q-brand-02": {"sig-typeface": {"context.memorable": LABEL}, "sig-color": {"context.memorable": LABEL},
                   "sig-device": {"context.memorable": LABEL}, "sig-character": {"context.memorable": LABEL}},
    "Q-brand-03": {"yes-full": {"hooks.H-logo.status": "have"}, "yes-wordmark": {"hooks.H-logo.status": "have"},
                   "no": {"hooks.H-logo.status": "placeholder"}},
    "Q-brand-04": {"productive": {"dials.expression": 25}, "hero-moments": {"dials.expression": 50}, "expressive": {"dials.expression": 80}},
    "Q-brand-06": {"two-sets": {"raw.marketingSurfaces": True}, "emphasized": {"overrides.type.emphasizedVariants": True},
                   "brand-face": {"raw.displayFace": "=brandFace"},
                   "productive-only": {"raw.marketingSurfaces": False, "overrides.type.emphasizedVariants": False}},
    "Q-brand-08": {k: {f"hooks.{h}.status": "have"} for k, h in (
        ("logo", "H-logo"), ("brand-colors", "H-color"), ("typeface", "H-type"), ("icons", "H-icons"), ("app-icon", "H-appicon"),
        ("photography", "H-photo"), ("illustration", "H-illus"), ("motion-assets", "H-motion"), ("motifs", "H-motif"),
        ("sounds", "H-sound"), ("voice-guide", "H-voice"), ("brand-book", "H-brandbook"))},
    "Q-plat-02": {k: {"raw.devices": [k]} for k in ("phone", "tablet-foldable", "desktop-web", "watch", "tv", "car", "spatial")},
    "Q-plat-03": {"touch": {"raw.inputs": ["touch"]}, "pointer": {"raw.inputs": ["pointer"]}, "keyboard": {"raw.inputs": ["keyboard"]},
                  "remote": {"raw.inputs": ["remote"]}, "spatial": {"raw.inputs": ["gaze"]}},
    "Q-plat-04": {"driving": {"raw.situations": ["driving"]}, "spatial": {"raw.situations": ["headset"]},
                  "watch": {"raw.situations": ["wrist"]}, "none": {"raw.situations": []}},
    "Q-plat-05": {"native-first": {"dials.brandPresence": 25}, "hybrid": {"dials.brandPresence": 50}, "brand-first": {"dials.brandPresence": 75}},
    "Q-dir-02": {"compact": {"dials.density": 80}, "comfortable": {"dials.density": 50}, "spacious": {"dials.density": 20},
                 "user-selectable": {"dials.density": 50}},
    "Q-dir-03": {"subtle": {"overrides.type.ratio": 1.2}, "balanced": {"overrides.type.ratio": 1.25}, "dramatic": {"overrides.type.ratio": 1.333}},
    "Q-dir-04": {"space": {"overrides.border.softness": "soft", "overrides.layout.containment": "whitespace"},
                 "containers": {"overrides.border.softness": "default", "overrides.layout.containment": "visible-containers"},
                 "lines": {"overrides.border.softness": "strong-rules", "overrides.layout.containment": "whitespace"}},
    "Q-color-01": {"keep-hex": {"raw.flags.brandExact": True}, "seed": {"raw.flags.brandExact": False},
                   "seed-3": {"raw.flags.brandExact": False}, "contrast-targets": {"raw.flags.brandExact": False}},
    "Q-color-02": {"accent": {"overrides.color.brandRole": "reserved-accent", "overrides.chrome.navTreatment": "neutral", "overrides.color.surfaces": UNSET},
                   "signature-surface": {"overrides.color.brandRole": "accent+signature-surface", "overrides.chrome.navTreatment": "neutral",
                                         "overrides.color.surfaces": "tinted-containers"},
                   "flooded-chrome": {"overrides.color.brandRole": "brand-chrome-allowed", "overrides.chrome.navTreatment": "colored-if-expression-allows",
                                      "overrides.color.surfaces": UNSET},
                   "content-layer": {"overrides.color.brandRole": "reserved-accent", "overrides.chrome.navTreatment": "neutral",
                                     "overrides.color.surfaces": UNSET, "raw.glass": True},
                   "neutral-first": {"overrides.color.brandRole": "reserved-accent", "overrides.chrome.navTreatment": "recessive",
                                     "overrides.color.surfaces": UNSET, "raw.neutralTint": "brand"}},
    "Q-color-03": {"monochrome": {"dials.colorfulness": 5}, "tonal": {"dials.colorfulness": 45}, "vivid": {"dials.colorfulness": 92},
                   "expressive": {"dials.colorfulness": 75}, "fidelity": {"raw.flags.brandExact": True, "dials.colorfulness": 60}},
    "Q-color-04": {"one": {"raw.accentCount": 1, "raw.accentHarmony": UNSET},
                   "analogous": {"raw.accentCount": 3, "raw.accentHarmony": "analogous"},
                   "contrasting": {"raw.accentCount": 2, "raw.accentHarmony": "complementary", "raw.neutralTint": "brand"},
                   "three": {"raw.accentCount": 3, "raw.accentHarmony": "triadic"},
                   "multi": {"raw.accentCount": 3, "raw.accentHarmony": "triadic", "raw.chartPalette": "categorical-8"}},
    "Q-color-05": {"strict": {"overrides.color.surfaces": "neutral+one-accent"}, "moderate": {"overrides.color.surfaces": "tinted-containers"},
                   "expressive": {"overrides.color.surfaces": "brand-or-dynamic-surfaces"}},
    "Q-color-09": {"pure": {"raw.neutralTint": "pure"}, "cool": {"raw.neutralTint": "cool"}, "warm": {"raw.neutralTint": "warm"},
                   "hue-matched": {"raw.neutralTint": "brand"}},
    "Q-color-11": {"srgb": {"raw.flags.p3": False}, "p3-enhance": {"raw.flags.p3": True}, "oklch-wide": {"raw.flags.p3": True},
                   "native-p3": {"raw.flags.p3": True}},
    "Q-color-14": {"alternating": {"raw.surfaceLayers": "alternating"}, "role-tiers": {"raw.surfaceLayers": UNSET},
                   "container-tiers": {"raw.surfaceLayers": UNSET}, "elevation-named": {"raw.surfaceLayers": UNSET}},
    "Q-color-15": {"classic-4": {"raw.statusSet": "classic-4"}, "discovery": {"raw.statusSet": "discovery"}, "workflow": {"raw.statusSet": "workflow"}},
    "Q-color-17": {"aa": {"raw.contrastTarget": "AA"}, "aaa": {"raw.contrastTarget": "AAA"}, "aa-apca": {"raw.contrastTarget": "AA"}},
    "Q-color-19": {"none": {"raw.chartPalette": "none"}, "brand-gray": {"raw.chartPalette": "brand-gray"},
                   "categorical-6-8": {"raw.chartPalette": "categorical-8"}, "carbon-14": {"raw.chartPalette": "categorical-14"}},
    "Q-color-20": {"overlay": {"raw.stateMethod": "overlay"}, "step-shift": {"raw.stateMethod": "step"}, "hybrid": {"raw.stateMethod": "hybrid"}},
    "Q-color-21": {"black": {"raw.darkBase": "black"}, "near-black": {"raw.darkBase": "near-black"}, "charcoal": {"raw.darkBase": "charcoal"},
                   "dimmed": {"raw.darkBase": "dimmed"}},
    "Q-color-23": {"focus-brand": {"raw.focusStyle": "brand"}, "focus-neutral": {"raw.focusStyle": "neutral"},
                   "two-tier": {"overrides.border.softness": "default"}, "by-purpose": {"overrides.border.softness": "strong-rules"}},
    "Q-type-01": {"system": {"raw.textFace": "system", "raw.displayFace": "=textFace"},
                  "open-neutral": {"raw.textFace": "Inter", "raw.displayFace": "=textFace"},
                  "open-custom": {"raw.textFace": "=openClass", "raw.displayFace": "=textFace"},
                  "brand-display": {"raw.textFace": "system", "raw.displayFace": "=brandFace"},
                  "brand-everywhere": {"raw.textFace": "=brandFace", "raw.displayFace": "=textFace"}},
    "Q-type-02": {"yes": {"hooks.H-type.status": "have", "raw.fontLicence": {"web": True, "app": True, "selfHost": True}},
                  "license-only": {"hooks.H-type.status": "placeholder", "raw.fontLicence": {"web": True, "app": True, "selfHost": True}},
                  "no": {"hooks.H-type.status": "open-library", "raw.fontLicence": {"web": False, "app": False, "selfHost": False}},
                  "web-only": {"hooks.H-type.status": "have", "raw.fontLicence": {"web": True, "app": False, "selfHost": True}},
                  "app-only": {"hooks.H-type.status": "have", "raw.fontLicence": {"web": False, "app": True, "selfHost": False}}},
    "Q-type-03": {c: {"raw.fontClass": c} for c in ("neo-grotesque", "geometric", "humanist", "serif", "slab", "rounded")},
    "Q-type-04": {"latin": {"raw.scripts": ["Latn"]}, "indic": {"raw.scripts": ["Latn", "Deva", "Beng"]},
                  "cjk": {"raw.scripts": ["Latn", "Hans", "Jpan", "Kore"]}, "arabic-hebrew": {"raw.scripts": ["Latn", "Arab", "Hebr"]},
                  "thai-other": {"raw.scripts": ["Latn", "Thai"]}},
    "Q-type-05": {"one": {"raw.displayFace": "=textFace"}, "superfamily": {"raw.displayFace": "=textFace"},
                  "sans-serif": {"raw.displayFace": "=serif"}, "display-face": {"raw.displayFace": "=brandFace"}},
    "Q-type-06": {"system-mono": {"raw.monoFace": "ui-monospace"}, "numeric-face": {"raw.numericStyles": True}},
    "Q-type-09": {"1.125": {"overrides.type.ratio": 1.125}, "1.2": {"overrides.type.ratio": 1.2}, "1.25": {"overrides.type.ratio": 1.25},
                  "1.333": {"overrides.type.ratio": 1.333}},
    "Q-type-11": {"4pt": {"raw.lineHeightGrid": 4}, "2pt": {"raw.lineHeightGrid": 2}},
    "Q-type-12": {"two": {"overrides.type.weightCount": 2}, "three": {"overrides.type.weightCount": 3}, "four": {"overrides.type.weightCount": 4},
                  "emphasized-twin": {"overrides.type.emphasizedVariants": True}, "strong-stronger": {"overrides.type.emphasizedVariants": True}},
    "Q-type-13": {"size-table": {"raw.tracking": "size-table"}, "per-style": {"raw.tracking": "size-table"}, "zero": {"raw.tracking": "zero"}},
    "Q-type-17": {"full": {"raw.textScaling": "full"}, "capped-chrome": {"raw.textScaling": "capped"}, "none": {"raw.textScaling": "none"}},
    "Q-space-02": {"hybrid": {"raw.spaceLadder": "hybrid"}, "linear": {"raw.spaceLadder": "linear"}, "geometric": {"raw.spaceLadder": "geometric"}},
    "Q-space-03": {"web-24-44": {"raw.minTarget": UNSET}, "ios-44": {"raw.minTarget": 44}, "android-48": {"raw.minTarget": 48},
                   "vehicle-76": {"raw.minTarget": 76}},
    "Q-space-04": {"pointer-24-32-40": {"overrides.control.height.md": 32}, "touch-32-40-48": {"overrides.control.height.md": 40},
                   "expressive-m3": {"overrides.control.height.md": 56}},
    "Q-space-05": {"1:2": {"raw.groupRatio": "1:2"}, "1:3-1:4": {"raw.groupRatio": "1:3-1:4"}, "dense": {"raw.groupRatio": "dense"}},
    "Q-space-07": {"nudges": {"raw.spaceExtras": ["nudges"]}, "hairline": {"raw.spaceExtras": ["hairline"]}},
    "Q-space-10": {"icons-16-32": {"overrides.icon.defaultSize": 16}, "button-sized": {"overrides.icon.defaultSize": 20}},
    "Q-layout-01": {"material": {"raw.breakpoints": "material"}, "tailwind": {"raw.breakpoints": "tailwind"},
                    "bootstrap": {"raw.breakpoints": "bootstrap"}, "apple-size-classes": {"raw.breakpoints": UNSET}},
    "Q-layout-03": {"reading": {"raw.productType": "content"}, "working": {"raw.productType": "work-tool"},
                    "data": {"raw.productType": "work-tool", "raw.numericStyles": True}},
    "Q-shape-01": {"square": {"dials.roundness": 5}, "subtle": {"dials.roundness": 40}, "soft": {"dials.roundness": 55}, "pill": {"dials.roundness": 97}},
    "Q-depth-01": {"borders": {"dials.depth": 8}, "ring-shadow": {"dials.depth": 25}, "tonal": {"dials.depth": 45}, "shadow": {"dials.depth": 68},
                   "glass": {"dials.depth": 90}},
    "Q-depth-04": {"none": {"raw.glass": False}, "control-layer": {"raw.glass": True}, "transient": {"raw.glass": True}, "decorative": {"raw.glass": True}},
    "Q-depth-05": {"1-2-4": {"raw.borderWidths": [1, 2, 4]}, "1-2-3-4": {"raw.borderWidths": [1, 2, 3, 4]},
                   "dividers-space-first": {"overrides.border.softness": "soft"}},
    "Q-depth-06": {"scrim-fluent": {"raw.scrim": "fluent"}, "scrim-atlassian": {"raw.scrim": "atlassian"},
                   "overlays-material": {"raw.stateOpacity": "material"}, "overlays-atlassian": {"raw.stateOpacity": "atlassian"}},
    "Q-motion-01": {"none": {"dials.energy": 0, "raw.flags.motionOff": True}, "productive": {"dials.energy": 20, "raw.flags.motionOff": False},
                    "two-mode": {"dials.energy": 50, "raw.flags.motionOff": False}, "springs": {"dials.energy": 80, "raw.flags.motionOff": False}},
    "Q-motion-04": {"durations-only": {"overrides.motion.spring.spatial.dampingRatio": 1.0},
                    "spatial-effects": {"overrides.motion.spring.spatial.dampingRatio": UNSET},
                    "apple-bounce": {"overrides.motion.spring.spatial.dampingRatio": 0.85}},
    "Q-motion-07": {"replace": {"raw.reducedMotion": "replace"}, "remove": {"raw.reducedMotion": "remove"}, "per-device": {"raw.reducedMotion": "replace"}},
    "Q-motion-08": {"silent": {"hooks.H-sound.status": "not-needed"}, "rare-events": {"hooks.H-sound.status": "placeholder"},
                    "sound-forward": {"hooks.H-sound.status": "placeholder"}},
    "Q-motion-09": {"haptics-system": {"hooks.H-haptic.status": "not-needed"}, "haptics-semantic": {"hooks.H-haptic.status": "placeholder"}},
    "Q-icon-01": {"platform-native": {"hooks.H-icons.status": "open-library"}, "open-source": {"hooks.H-icons.status": "open-library"},
                  "custom": {"hooks.H-icons.status": "have"}, "extend": {"hooks.H-icons.status": "open-library"}},
    "Q-icon-02": {"outlined": {"overrides.icon.restStyle": "outline"}, "filled": {"overrides.icon.restStyle": "filled-or-colored"},
                  "duotone": {"overrides.icon.restStyle": "duotone"}, "rounded": {"overrides.icon.cornerStyle": "rounded"},
                  "sharp": {"overrides.icon.cornerStyle": "sharp"}},
    "Q-icon-03": {"2-at-24": {"raw.iconStroke": 2}, "1.5-at-24": {"raw.iconStroke": 1.5}, "1.5-at-16": {"raw.iconStroke": 2.25},
                  "variable": {"raw.iconStroke": UNSET}},
    "Q-icon-04": {"material-grid": {"overrides.icon.defaultSize": 24}, "carbon": {"overrides.icon.defaultSize": 16},
                  "fluent": {"overrides.icon.defaultSize": 20}},
    "Q-icon-06": {"yes-layered": {"hooks.H-appicon.status": "have"}, "yes-flat": {"hooks.H-appicon.status": "have"},
                  "no": {"hooks.H-appicon.status": "placeholder"}},
    "Q-img-01": {"none": {"hooks.H-photo.status": "not-needed"}, "documentary": {"hooks.H-photo.status": "placeholder"},
                 "portraiture": {"hooks.H-photo.status": "placeholder"}, "still-life": {"hooks.H-photo.status": "placeholder"}},
    "Q-img-04": {"none": {"hooks.H-illus.status": "not-needed"}, "line": {"hooks.H-illus.status": "placeholder"},
                 "flat": {"hooks.H-illus.status": "placeholder"}, "hand-drawn": {"hooks.H-illus.status": "placeholder"},
                 "mascot": {"hooks.H-illus.status": "placeholder"}},
    "Q-img-06": {"symbol-animation": {"hooks.H-motion.status": "open-library"}, "lottie": {"hooks.H-motion.status": "placeholder"},
                 "3d": {"hooks.H-motion.status": "placeholder"}, "emoji-stickers": {"hooks.H-motion.status": "placeholder"}},
    "Q-img-07": {"none": {"hooks.H-motif.status": "not-needed"}, "expressive-only": {"hooks.H-motif.status": "placeholder"},
                 "logo-shapes": {"hooks.H-motif.status": "placeholder"}},
    "Q-voice-01": {"upload": {"hooks.H-voice.status": "have"}, "plainspoken": {"hooks.H-voice.status": "placeholder", "context.voice": LABEL},
                   "warm-crisp": {"hooks.H-voice.status": "placeholder", "context.voice": LABEL},
                   "bold-optimistic": {"hooks.H-voice.status": "placeholder", "context.voice": LABEL},
                   "custom": {"hooks.H-voice.status": "placeholder"}},
    "Q-voice-03": {"sentence": {"overrides.content.capitalization": "sentence-case"}, "title-headings": {"overrides.content.capitalization": "title-case"}},
    "Q-comp-01": {k: {"components.base": k} for k in ("headless", "copy-in-styled", "web-components", "native", "adopt")},
    "Q-comp-02": {"core-25": {"components.inventory": list(DEFAULT_COMPONENTS)},
                  "extended": {"components.inventory": list(DEFAULT_COMPONENTS) + EXTENDED_COMPONENTS},
                  "logo-ai": {"components.inventory": list(DEFAULT_COMPONENTS) + AI_COMPONENTS}},
    "Q-state-02": {"strong": {"overrides.signifier.minStrength": "strong"}, "balanced": {"overrides.signifier.minStrength": "balanced"},
                   "minimal": {"overrides.signifier.minStrength": "minimal-allowed"}},
    "Q-state-03": {"outer-2-2": {"raw.focusWidth": 2, "raw.focusOffset": 2}, "material-3": {"raw.focusWidth": 3, "raw.focusOffset": 2},
                   "inset": {"raw.focusWidth": 2, "raw.focusOffset": -2}, "two-tone": {"raw.focusStyle": "two-tone"}},
    "Q-state-04": {"overlays": {"raw.stateMethod": "overlay"}, "explicit": {"raw.stateMethod": "step"}},
    "Q-form-01": {"outlined": {"raw.fieldStyle": "outlined"}, "filled": {"raw.fieldStyle": "filled"}},
    "Q-ai-01": {"none": {}, "label-button": {"components.inventory+": ["ai-label", "ai-button"]},
                "presence-mode": {"components.inventory+": ["ai-label"]}, "chat": {"components.inventory+": ["chat-message", "prompt-input"]},
                "voice": {}},
    "Q-theme-01": {"system-light-dark": {"raw.flags.darkMode": True, "raw.defaultTheme": "system"},
                   "light-dark-toggle": {"raw.flags.darkMode": True, "raw.defaultTheme": "system"},
                   "light-only": {"raw.flags.darkMode": False, "raw.defaultTheme": "system"},
                   "dark-only": {"raw.flags.darkMode": True, "raw.defaultTheme": "dark"}},
    "Q-space-01": {"4-grid-8-rhythm": {"raw.spaceUnit": 4}, "4": {"raw.spaceUnit": 4}, "8": {"raw.spaceUnit": 8}, "rem-16": {"raw.spaceUnit": 4}},
}
# Questions whose answers are recorded without changing tokens, and what they shape instead (U5: say so, never be silent).
RECORD_KINDS = {
    "rule": "recorded; this shapes DESIGN.md rules, not tokens",
    "owner": "recorded as an owner input in PRODUCT.md; it does not change tokens",
    "hook": "recorded as an asset status (DESIGN.md asset table and Open Items); it does not change tokens",
    "reference": "recorded; add the reference with the opendesigner-extract skill, then engine.py intake",
    "export": "recorded; this changes the files in build/ on the next build, not the tokens",
}
_R = {
    "rule": """Q-brand-05 Q-dir-05 Q-plat-06 Q-plat-10 Q-aud-04 Q-theme-02 Q-theme-03 Q-theme-04 Q-color-06 Q-color-07 Q-color-08 Q-color-10
               Q-color-12 Q-color-13 Q-color-16 Q-color-18 Q-color-22 Q-color-24 Q-color-25 Q-color-26 Q-type-07 Q-type-10 Q-type-14 Q-type-15
               Q-type-16 Q-space-06 Q-space-08 Q-space-09 Q-layout-02 Q-layout-04 Q-layout-05 Q-layout-06 Q-shape-02 Q-shape-03 Q-shape-04
               Q-shape-05 Q-depth-02 Q-depth-03 Q-motion-02 Q-motion-03 Q-motion-05 Q-motion-06 Q-motion-10 Q-icon-05 Q-icon-07 Q-icon-08
               Q-img-02 Q-img-03 Q-img-05 Q-viz-01 Q-voice-02 Q-voice-04 Q-voice-05 Q-voice-06 Q-comp-03 Q-comp-04 Q-comp-05 Q-state-01
               Q-state-05 Q-state-06 Q-state-07 Q-state-08 Q-form-02 Q-form-03 Q-form-04 Q-form-05 Q-pattern-01 Q-pattern-02 Q-pattern-03
               Q-pattern-04 Q-pattern-05 Q-pattern-06 Q-token-01 Q-token-02 Q-token-03 Q-token-04 Q-token-05 Q-token-06 Q-token-07 Q-token-08
               Q-token-09 Q-token-10 Q-brand-02 Q-shape-01 Q-type-06 Q-type-09 Q-type-11 Q-space-07 Q-space-10 Q-layout-03 Q-depth-05
               Q-motion-09 Q-voice-03 Q-form-01 Q-state-04 Q-ai-01 Q-icon-02 Q-color-23 Q-state-02""",
    "owner": """Q-scope-01 Q-scope-02 Q-scope-03 Q-scope-04 Q-scope-05 Q-tool-01 Q-tool-02 Q-tool-04 Q-gov-01 Q-gov-02 Q-gov-03 Q-gov-04 Q-gov-05
                Q-gov-06 Q-gov-07 Q-dist-01 Q-dist-02 Q-dist-03 Q-dist-04 Q-pref-01 Q-pref-02 Q-pref-03 Q-plat-07 Q-plat-08 Q-plat-09
                Q-comp-01 Q-comp-02 Q-aud-02 Q-brand-07""",
    "hook": "Q-brand-03 Q-brand-08 Q-icon-01 Q-icon-06 Q-img-01 Q-img-04 Q-img-06 Q-img-07 Q-motion-08 Q-voice-01 Q-type-02",
    "reference": "Q-ref-01",
    "export": "Q-type-17 Q-tool-03",
}
ANSWER_RECORDS = {q: k for k, qs in _R.items() for q in qs.split()}
ANSWER_NOTES = {  # one plain line for options the engine cannot build yet, so the reply stays honest
    ("Q-type-06", "brand-mono"): "name the code font with engine.py set raw.monoFace '\"Name\"'",
    ("Q-type-01", "open-custom"): "the open font follows the style you pick (Q-type-03); name another with engine.py set raw.textFace",
    ("Q-type-09", "hand-tuned"): "keep your own sizes by setting font.size tokens one by one (engine.py set font.size.<n> ...)",
    ("Q-color-21", "dimmed"): "the dark theme uses a dimmed base; a separate third theme is not generated",
    ("Q-shape-01", "rule-based"): "corners follow the Roundness dial; set dials.roundness to move them",
    ("Q-space-07", "negatives"): "negative spacing is not generated; use margins in code sparingly",
}


def _questions_path():
    for path in (os.path.join(REFERENCES, "questions.json"), os.path.join(SKILL_ROOT, "..", "..", "data", "questions.json")):
        if os.path.exists(path):
            return path
    return None


_QUESTIONS = None


def questions():
    """references/questions.json by id: zoom level, area, options (v, l). Empty when the file is missing."""
    global _QUESTIONS
    if _QUESTIONS is None:
        _QUESTIONS = {}
        path = _questions_path()
        if path:
            try:
                _QUESTIONS = {q["id"]: q for q in read_json(path).get("questions", [])}
            except (ValueError, KeyError):
                _QUESTIONS = {}
    return _QUESTIONS


def option_values(q):
    out = []
    for o in (q or {}).get("options") or []:
        v = o.get("v", o.get("value"))
        out += [str(x) for x in v] if isinstance(v, list) else [str(v)]
    return out


def option_label(qid, value):
    """Plain label of an option, without its source tags; None when the value is not a listed option."""
    for o in (questions().get(qid) or {}).get("options") or []:
        v = o.get("v", o.get("value"))
        if str(v) == str(value) or (isinstance(v, list) and str(value) in [str(x) for x in v]):
            lab = o.get("l", o.get("label", str(value)))
            return re.sub(r"\s*\[[^\]]*\]\.?\s*$", "", lab).rstrip(". ").strip()
    return None


def answer_words(qid, value):
    """Plain words for an answer: the option labels, or the value itself."""
    if isinstance(value, dict):
        if qid == "Q-brand-01":
            return ", ".join(m["id"] if isinstance(m, dict) else str(m) for m in answer_effects(qid, value).get("macros", [])) or "balanced"
        return ", ".join(f"{k} {v}" for k, v in value.items() if not isinstance(v, (dict, list)))
    if qid == "Q-scope-06":
        items = surface_list(value)
        if items:
            return ", ".join(f"{x['name']} ({x['mode']})" if not x["name"].endswith(" surface") else x["mode"] for x in items)
    vals = value if isinstance(value, list) else [value]
    out = []
    for v in vals:
        if isinstance(v, dict):
            out.append(v.get("name") or json.dumps(v, ensure_ascii=False))
            continue
        out.append(option_label(qid, v) or str(v))
    return ", ".join(out)


FEEL_STOP = {"a", "an", "and", "bit", "little", "very", "really", "super", "quite", "kind", "of", "the", "but", "more", "too", "so", "not",
             "lot", "lots", "with", "feel", "feeling", "look", "looking", "like", "it", "should", "be", "i", "want", "we", "our", "my"}


def feel_words(words):
    """Plain feel words -> (macro ids in order, {word: [macros]}, unknown words). Never raises (U5 F6, F7)."""
    table = (levers().get("feelWords") or {}).get("words") or {}
    known = {m["id"] for m in levers()["macros"]}
    macros, mapping, unknown = [], {}, []

    def look(w):
        w = w.strip().lower().strip("!.?,;:'\"()")
        for cand in (w, w.replace(" ", "-"), w.replace("_", "-"), w[:-1] if w.endswith("s") else None, w[:-2] if w.endswith("ly") else None):
            if cand and (cand in known or cand in table):
                return [cand] if cand in known else table[cand]
        return None
    for phrase in words:
        phrase = str(phrase).strip()
        if not phrase:
            continue
        ids = look(phrase)
        if ids is None:
            parts = [x for x in re.split(r"[\s/+&]+", phrase.lower()) if x and x.strip("!.?,") not in FEEL_STOP]
            found = [look(x) for x in parts]
            ids = [m for f in found if f for m in f] or None
        if ids is None:
            unknown.append(phrase)
            continue
        mapping[phrase] = ids
        for m in ids:
            if m not in macros:
                macros.append(m)
    return macros, mapping, unknown


def _merge_effects(into, eff):
    for k, v in eff.items():
        if isinstance(v, list) and isinstance(into.get(k), list):
            into[k] = into[k] + [x for x in v if x not in into[k]]
        else:
            into[k] = v
    return into


def answer_effects(qid, value, state=None):
    """Engine inputs implied by a questionnaire answer (ANSWER_TABLE, plus the questions whose answers are free-form).
    UNSET removes an earlier value; LABEL stands for the option's plain label. A list answer merges its options."""
    v = value
    eff = {}
    if qid == "Q-plat-01":
        plats = v if isinstance(v, list) else [v]
        return {"raw.platforms": [str(x) for x in plats if x]} if plats else {}
    if qid == "Q-type-08":
        try:
            return {"raw.baseSize": int(v)}
        except (TypeError, ValueError):
            return {}
    if qid == "Q-dir-01":
        return {"preset": {"neo-brutalist": "neobrutal"}.get(v, v)} if isinstance(v, str) else {}
    if qid == "Q-scope-06":
        surfaces = surface_list(v)
        if surfaces:
            if any(isinstance(it, dict) or (isinstance(it, str) and ":" in it) for it in (v if isinstance(v, list) else [v])):
                eff["context.surfaces"] = surfaces
            eff["raw.productType"] = SURFACE_MODES[surfaces[0]["mode"].lower()]["productType"]
            eff["raw.marketingSurfaces"] = any(x["mode"] in ("Persuade", "Experience") for x in surfaces)
        return eff
    if qid == "Q-scope-01":
        items = [str(x) for x in (v if isinstance(v, list) else [v]) if x]
        eff["context.scope.in"] = [option_label(qid, x) or x for x in items]
        if "marketing" in items:
            eff["raw.marketingSurfaces"] = True
        return eff
    if qid == "Q-tool-03":
        plans = [FIGMA_PLAN_OF.get(x) for x in (v if isinstance(v, list) else [v]) if isinstance(x, str)]
        plan = next((pl for pl in plans if pl), None)
        return {"exports.figmaPlan": plan} if plan else {}
    if qid == "Q-brand-07":
        items = v.get("principles") if isinstance(v, dict) else v
        if isinstance(items, list) and all(isinstance(x, str) for x in items) and items:
            return {"principles": [x.strip() for x in items if x.strip()]}
        return {}
    if qid == "Q-brand-01":
        if isinstance(v, dict):
            macros = []
            for row, pos in v.items():
                row = row[:1].upper()
                left, right = BRAND_ROWS.get(row, (None, None))
                if row == "D":
                    try:
                        eff["dials.energy"] = int(pos)
                    except (TypeError, ValueError):
                        pass
                    continue
                if left is None or pos is None:
                    continue
                strength = rnd(abs(float(pos) - 50) / 50, 2)
                if strength > 0:
                    macros.append({"id": left if float(pos) < 50 else right, "strength": strength})
            eff["macros"] = macros
            return eff
        words = v if isinstance(v, list) else re.split(r"\s*,\s*", str(v))
        words = [re.sub(r"^[A-G]\s+", "", w) for w in words]            # 'A playful-serious' names a slider: its left end
        words = [w.split("-")[0] if re.fullmatch(r"[a-z]+-[a-z]+", w) and w.split("-")[0] in BRAND_ROW_WORDS else w for w in words]
        macros, _m, _u = feel_words(words)
        return {"macros": macros} if macros else {}
    if isinstance(v, list) and qid in ANSWER_TABLE:
        for item in v:
            _merge_effects(eff, answer_effects(qid, item, state))
        return eff
    table = ANSWER_TABLE.get(qid) or {}
    if isinstance(v, str) and v.startswith("state-") and qid == "Q-aud-02":
        return {"context.feelings+": [v[len("state-"):]]}
    row = table.get(str(v)) if not isinstance(v, (dict, list)) else None
    if row is None and isinstance(v, (int, float)) and not isinstance(v, bool):
        row = table.get(fmt_num(v))
    if not row:
        return {}
    for k, val in row.items():
        if val == LABEL:
            val = option_label(qid, v) or str(v)
        eff[k] = copy.deepcopy(val)
    if qid == "Q-type-01" and state is not None and v in ("brand-display", "brand-everywhere"):
        raw = state.get("raw") or {}
        cur = raw.get("textFace")
        if not raw.get("brandFace") and isinstance(cur, str) and not cur.startswith("=") and not _generic_face(cur):
            eff["raw.brandFace"] = cur  # keep the face the person already named as the brand face
    return eff


BRAND_ROW_WORDS = {w for pair in BRAND_ROWS.values() for w in pair if w} | {"calm"}


def answer_outcome(qid, value, state=None):
    """(effects, record kind or None, note) for an answer: what it changes, or what it shapes when it changes no token."""
    eff = answer_effects(qid, value, state)
    vals = value if isinstance(value, list) else [value]
    note = next((ANSWER_NOTES[(qid, str(x))] for x in vals if (qid, str(x)) in ANSWER_NOTES), "")
    return eff, ANSWER_RECORDS.get(qid), note


def parse_value(text):
    try:
        return json.loads(text)
    except (ValueError, TypeError):
        return text


def set_path(state, path, value):
    parts = path.split(".")
    node = state
    for q in parts[:-1]:
        if not isinstance(node.get(q), dict):
            node[q] = {}
        node = node[q]
    old = node.get(parts[-1])
    node[parts[-1]] = value
    return old


def normalize_path(path):
    if re.match(r"^Q-[a-z]+-\d+$", path):
        return "answers." + path
    m = re.match(r"^assets\.(H-[a-z]+)$", path)
    if m:
        return f"hooks.{m.group(1)}.status"
    head = path.split(".")[0]
    if head in TOP_KEYS:
        return path
    if head in DIALS:
        return "dials." + path
    return "overrides." + path  # any derived parameter or token path can be detached and set (DC-L16-14)


def is_locked(state, path):
    if any(path == lk or path.startswith(lk + ".") for lk in state.get("locks") or []):
        return True
    parts = path.split(".")
    if parts[0] in ("dials", "answers") and len(parts) >= 2:
        node = (state.get(parts[0]) or {}).get(parts[1])
        return isinstance(node, dict) and bool(node.get("locked"))
    return False


def _decision_entries(d):
    path = os.path.join(d, "decisions.md")
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        heads = re.findall(r"^## (D-\d+) · (.*)$", f.read(), flags=re.M)
    return [(did, rest.split(" = ")[0].strip() if " = " in rest else "") for did, rest in heads]


def log_decision(d, path, value, why, set_by="chosen", locked=False, source_ref=None, extra=None, title=None):
    """Append one decision in the spec 7.9 shape. Returns the decision id."""
    fp = os.path.join(d, "decisions.md")
    if not os.path.exists(fp):
        write_text(fp, DECISIONS_HEADER)
    entries = _decision_entries(d)
    did = f"D-{len(entries) + 1:04d}"
    prev = [e for e, pth in entries if pth == path]
    head = title or f"{path} = {json.dumps(value, ensure_ascii=False)}"
    lines = [f"\n## {did} · {head}\n",
             f"- set_by: {set_by} · locked: {'yes' if locked else 'no'} · date: {_dt.date.today().isoformat()} · "
             f"supersedes: {prev[-1] if prev else 'none'} · source_ref: {source_ref or 'none'}\n",
             f"- reason: {why or '(no reason given)'}\n"]
    for e in extra or []:
        lines.append(f"- {e}\n")
    with open(fp, "a", encoding="utf-8", newline="\n") as f:
        f.writelines(lines)
    return did


DECISIONS_HEADER = ("# Decisions\n\nAppend-only, ADR-style (spec 7.9): one entry per decision, newest last. A later entry for the same "
                    "path supersedes an earlier one; nothing is edited or deleted. set_by is chosen, confirmed_default, auto_default, "
                    "assumed, delegated, reference or asset.\n")


def split_status(why, set_by):
    """R3's skills put a status word at the start of --why ('delegated: ...'); read it into set_by."""
    if set_by:
        return why, SET_BY_ALIASES.get(set_by, set_by)
    m = re.match(r"^\s*(chosen|confirmed_default|auto_default|assumed|delegated|reference|asset|confirmed|default|pending)\s*:\s*(.*)$",
                 why or "", flags=re.S)
    if m:
        return m.group(2), SET_BY_ALIASES.get(m.group(1), m.group(1))
    return why, "chosen"


def _default_at(path):
    node = default_state()
    for q in path.split("."):
        node = node.get(q) if isinstance(node, dict) else None
    return copy.deepcopy(node)


def get_path(state, path):
    node = state
    for q in path.split("."):
        node = node.get(q) if isinstance(node, dict) else None
    return node


def _store(state, path, value, set_by, did, lock, via=None):
    """Write a value; dials and answers keep {value, set_by, ...} records (spec 7.10). A path ending in '+' appends to a
    list; UNSET removes an override or puts a raw input back to its default."""
    if path.endswith("+"):
        path = path[:-1]
        cur = get_path(state, path)
        lst = list(cur) if isinstance(cur, list) else []
        for x in (value if isinstance(value, list) else [value]):
            if x not in lst:
                lst.append(x)
        value = lst
    parts = path.split(".")
    if value == UNSET and parts[0] == "overrides":
        return state.setdefault("overrides", {}).pop(path.split(".", 1)[1], None)
    if value == UNSET:
        value = None if parts[0] == "dials" else _default_at(path)
    if parts[0] == "dials" and len(parts) == 2:
        old = state["dials"].get(parts[1])
        rec = dict(old) if isinstance(old, dict) else {}
        rec.update({"value": value, "set_by": set_by, "detached": value is not None, "decision": did})
        if lock:
            rec["locked"] = True
        state["dials"][parts[1]] = rec
        return dial_value(old)
    if parts[0] == "answers" and len(parts) == 2:
        old = state["answers"].get(parts[1])
        rec = dict(old) if isinstance(old, dict) else {}
        rec.update({"value": value, "set_by": set_by, "decision": did})
        if via:
            rec["via"] = via  # 'sketch': asked in the 5-question sketch, so it stays at zoom 0
        else:
            rec.pop("via", None)
        rec.setdefault("locked", False)
        if lock:
            rec["locked"] = True
        state["answers"][parts[1]] = rec
        return answer_value(old)
    if parts[0] == "overrides" and len(parts) >= 2:  # overrides are keyed by the whole parameter or token path
        key = path.split(".", 1)[1]
        old = state.setdefault("overrides", {}).get(key)
        state["overrides"][key] = value
    else:
        old = set_path(state, path, value)
    if lock and path not in (state.get("locks") or []):
        state.setdefault("locks", []).append(path)
    return old


EXPORT_ONLY = ("raw.textScaling", "raw.fontLicence", "exports.")


def token_diff(old_state, new_state):
    """Token paths whose value changes between two states (every token file and the resolver's modes)."""
    if state_hash(old_state) == state_hash(new_state):
        return []
    try:
        a, _m, _c = generate_system(old_state)
        b, _m2, _c2 = generate_system(new_state)
    except Exception as ex:  # a state the generator cannot read is reported, never hidden
        return [f"(tokens could not be generated: {ex})"]

    def flat(files):
        out = {}
        for fn, tree in files.items():
            if fn.endswith(".tokens.json"):
                mode = fn.split(".")[-3] if fn.count(".") >= 3 else ""
                for pth, t in flatten(tree).items():
                    out[(pth, mode)] = json.dumps(t["$value"], sort_keys=True)
        out[("modes", "")] = json.dumps(files["opendesigner.resolver.json"].get("modifiers", {}), sort_keys=True)
        return out
    fa, fb = flat(a), flat(b)
    changed = {pth for (pth, m) in set(fa) | set(fb) if fa.get((pth, m)) != fb.get((pth, m))}
    return sorted(changed, key=lambda x: (bool(PRIMITIVE_RE.match(x)), x != "color.bg.action.primary", x))  # named roles first


def change_lines(path, value, old_state, new_state, effects=None):
    """Plain lines saying what an answer or a setting changed: tokens, or what it shapes instead (U5: never silent)."""
    changed = token_diff(old_state, new_state)
    lines = []
    qid = path.split(".", 1)[1] if path.startswith("answers.") else ANSWER_PATHS.get(path, (None, None))[0]
    if changed:
        ex = ", ".join(changed[:3]) + (", ..." if len(changed) > 3 else "")
        lines.append(f"tokens: {len(changed)} value{'s' if len(changed) != 1 else ''} change ({ex}). "
                     "Run `engine.py build` to refresh the tokens, exports and preview.")
    elif path.startswith("answers."):
        kind = ANSWER_RECORDS.get(qid)
        eff = effects or {}
        if eff and all(k.startswith(EXPORT_ONLY) or k.startswith("hooks.") for k in eff) and any(k.startswith(EXPORT_ONLY) for k in eff):
            lines.append(RECORD_KINDS["export"] + ".")
        elif kind:
            lines.append(RECORD_KINDS[kind] + ".")
        elif eff:
            lines.append("recorded; the tokens already match this answer.")
        else:
            lines.append(RECORD_KINDS["rule"] + ".")
    elif path.startswith(EXPORT_ONLY):
        lines.append(RECORD_KINDS["export"] + ".")
    elif path.split(".")[0] in ("dials", "raw", "overrides", "preset", "macros"):
        lines.append("no token changed: the system already had this value.")
    if qid:
        _e, _k, note = answer_outcome(qid, value)
        if note:
            lines.append("note: " + note + ".")
    return lines


def cmd_set(d, path, value, why=None, force=False, quiet=False, set_by=None, lock=False, source_ref=None, via=None):
    sp = os.path.join(d, "state.json")
    if not os.path.exists(sp):
        raise SystemExit(f"no state at {sp}; run `engine.py init --dir {d}` first")
    state = merge_defaults(read_json(sp))
    old_state = copy.deepcopy(state)
    path = normalize_path(path)
    why, set_by = split_status(why, set_by)
    if set_by not in SET_BY:
        raise SystemExit(f"--set-by must be one of {', '.join(SET_BY)}")
    if is_locked(state, path) and not force:
        raise SystemExit(f"{path} is locked. Ask the owner before changing it, then run `engine.py unlock {path}` (or pass --force).")
    if path.startswith("dials."):
        if value is not None and not (isinstance(value, (int, float)) and 0 <= value <= 100):
            raise SystemExit("A dial takes a number from 0 to 100, or null to follow the other dials.")
    if path.startswith("zoom."):
        if isinstance(value, int) and 0 <= value < len(ZOOM_LEVELS):
            value = ZOOM_LEVELS[value]
        if value not in ZOOM_LEVELS:
            raise SystemExit(f"zoom levels are {', '.join(ZOOM_LEVELS)} (or 0-3)")
        if path == "zoom.all":
            for key, _t in ZOOM_AREAS:
                cur = (state.get("zoom") or {}).get(key)
                if cur not in ZOOM_LEVELS or ZOOM_LEVELS.index(cur) < ZOOM_LEVELS.index(value):
                    state.setdefault("zoom", {})[key] = value
            path = "zoom.all"
    if path == "profile.voice" and value not in VOICES:
        raise SystemExit(f"profile.voice is one of {', '.join(VOICES)}")
    m = re.match(r"^hooks\.(H-[a-z]+)\.status$", path)
    if m and value not in HOOK_STATUSES:
        raise SystemExit(f"hook status must be one of {', '.join(HOOK_STATUSES)}")
    plan_note = ""
    if path.startswith("overrides.") and not is_param_override(path.split(".", 1)[1]) and value is not None:
        files0, meta0, _c0 = generate_system(state)
        plan = override_plan(files0, path.split(".", 1)[1], value, meta0["params"]["space.densityMode"]["value"])
        if "error" in plan:
            raise SystemExit(f"Nothing was changed: {plan['error']}.")
        value = next(iter(plan["values"].values()))  # stored in DTCG form, so the tokens stay valid
        plan_note = plan.get("note") or ""
    did = f"D-{len(_decision_entries(d)) + 1:04d}"
    prev = _store(state, path, value, set_by, did, lock, via)
    extra = []
    if prev is not None:
        extra.append(f"previous value: {json.dumps(prev, ensure_ascii=False)}")
    if plan_note:
        extra.append(plan_note)
    effects = {}
    if path.startswith("answers."):
        qid = path.split(".", 1)[1]
        q = questions().get(qid)
        opts = option_values(q)
        vals = value if isinstance(value, list) else [value]
        custom = [str(x) for x in vals if not isinstance(x, (dict, list)) and opts and str(x) not in opts
                  and not str(x).startswith("state-") and qid not in ("Q-brand-01", "Q-scope-06", "Q-brand-07")]
        if custom:
            extra.append(f"note: {', '.join(custom)} is not one of the listed options for {qid}; kept as your own answer")
        effects = answer_effects(qid, value, state)
        for epath, evalue in effects.items():
            if is_locked(state, epath.rstrip("+")) and not force:
                extra.append(f"skipped {epath} (locked)")
                continue
            _store(state, epath, evalue, set_by, did, False)
            shown = "back to the default" if evalue == UNSET else json.dumps(evalue, ensure_ascii=False)
            extra.append(f"also set: {epath.rstrip('+')} = {shown} (from {qid})")
    dump_json(sp, state)
    log_decision(d, path, value, why, set_by, lock, source_ref, extra)
    qid, how = (path.split(".", 1)[1], None) if path.startswith("answers.") else ANSWER_PATHS.get(path, (None, None))
    if qid and journey:
        if prev not in (None, "", [], {}) and prev != value:
            track(d, "step_changed", step=qid)
        track(d, "step_answered", step=qid, how=how if how and set_by == "chosen" else journey.how_for(qid, value, set_by))
    if not quiet:
        print(f"{did} set {path} = {json.dumps(value, ensure_ascii=False)} ({set_by}{', locked' if lock else ''})")
        for e in extra:
            print("  " + e)
        for line in change_lines(path, value, old_state, state, effects):
            print("  " + line)
    return state


def cmd_lock(d, path, on=True):
    sp = os.path.join(d, "state.json")
    state = merge_defaults(read_json(sp))
    path = normalize_path(path)
    parts = path.split(".")
    if parts[0] in ("dials", "answers") and len(parts) == 2:
        node = state[parts[0]].get(parts[1])
        rec = node if isinstance(node, dict) else {"value": node}
        rec["locked"] = on
        state[parts[0]][parts[1]] = rec
    else:
        locks = state.setdefault("locks", [])
        if on and path not in locks:
            locks.append(path)
        if not on and path in locks:
            locks.remove(path)
    dump_json(sp, state)
    cur = state
    for q in parts:
        cur = cur.get(q) if isinstance(cur, dict) else None
    log_decision(d, path, answer_value(cur), "locked: change only with the owner's consent" if on else "unlocked for change",
                 "chosen", on, title=f"{'lock' if on else 'unlock'} {path}")
    print(f"{'locked' if on else 'unlocked'} {path}")


def cmd_init(d, src=None, name=None, force=False):
    sp = os.path.join(d, "state.json")
    if os.path.exists(sp) and not force:
        raise SystemExit(f"{sp} already exists (use --force to replace it)")
    os.makedirs(d, exist_ok=True)
    if src:
        state = merge_defaults(read_json(src))
    else:
        state = default_state(name or "Untitled design system")
    if name:
        state["name"] = name
    dump_json(sp, state)
    dp = os.path.join(d, "decisions.md")
    if not os.path.exists(dp) or force:
        write_text(dp, DECISIONS_HEADER)
        log_decision(d, "init", None, "Start of the design system; every default traces to references/levers.json.", "auto_default",
                     title="init" + (f" from {os.path.basename(src)}" if src else " with defaults"))
    print(f"initialized {sp}")


# =============================================================================================
# Commands that write outputs
# =============================================================================================

def load_state(d):
    sp = os.path.join(d, "state.json")
    if not os.path.exists(sp):
        raise SystemExit(f"no state at {sp}; run `engine.py init --dir {d}` first")
    return read_json(sp)


def cmd_generate(d, quiet=False):
    state = load_state(d)
    files, meta, ctx = generate_system(state)
    tokdir = os.path.join(d, "tokens")
    os.makedirs(tokdir, exist_ok=True)
    for fn in os.listdir(tokdir):  # drop stale token files (for example color.dark after dark mode is turned off)
        if fn.endswith(".json") and fn not in files:
            os.remove(os.path.join(tokdir, fn))
    for fn, data in files.items():
        dump_json(os.path.join(tokdir, fn), data)
    if not quiet:
        print(f"generated {len(files)} files in {tokdir}")
        dl = ", ".join(f"{k} {v}" for k, v in meta["dials"].items())
        print(f"  dials: {dl}")
        print(f"  type: base {meta['type']['base']}px x {meta['type']['ratio']} -> {meta['type']['sizes']}")
        print(f"  accent: {' '.join(meta['ramps']['accent']['light']['hex'])}")
    return files, meta, ctx


# =============================================================================================
# Exporters
# =============================================================================================

def kebab(seg):
    return re.sub(r"(?<=[a-z0-9])([A-Z])", r"-\1", str(seg)).lower()


def css_var(prefix, path):
    return f"--{prefix}-" + "-".join(kebab(s) for s in path.split("."))


def fmt_num(x):
    if isinstance(x, float) and x.is_integer():
        return str(int(x))
    return f"{x:g}" if isinstance(x, (int, float)) else str(x)


def css_color(v):
    hx = hex_of(v)
    a = v.get("alpha") if isinstance(v, dict) else None
    if a is not None and a < 1:
        r, g, b = hex_to_rgb8(hx)
        return f"rgb({r} {g} {b} / {fmt_num(rnd(a, 3))})"
    return hx


def css_dim(v, rem=False):
    if v["unit"] == "px" and rem:
        return f"{fmt_num(rnd(v['value'] / 16, 4))}rem"
    return f"{fmt_num(v['value'])}{v['unit']}"


def css_duration(v):
    return f"{fmt_num(v['value'])}{v['unit']}"


def css_bezier(v):
    return "cubic-bezier(" + ", ".join(fmt_num(x) for x in v) + ")"


def spring_ext(tokinfo, flat):
    """Follow an alias chain to a spring's $extensions, if any."""
    seen = 0
    t = tokinfo
    while t is not None and seen < 10:
        ext = (t.get("$extensions") or {}).get(NS, {})
        if "spring" in ext:
            return ext
        v = t.get("$value")
        if isinstance(v, str) and v.startswith("{"):
            t = flat.get(v[1:-1])
            seen += 1
        else:
            return None
    return None


def css_decls(flat, prefix, paths, rem_fonts=True):
    """CSS declarations for the given token paths. Aliases become var() so modes cascade."""
    out = []
    for path in paths:
        t = flat[path]
        typ, raw, val = t["type"], t["$value"], t["resolved"]
        name = css_var(prefix, path)
        if isinstance(raw, str) and raw.startswith("{") and typ not in ("transition",):
            out.append(f"  {name}: var({css_var(prefix, raw[1:-1])});")
            if typ == "typography":
                pass
            continue
        if typ == "color":
            out.append(f"  {name}: {css_color(val)};")
        elif typ == "dimension":
            out.append(f"  {name}: {css_dim(val, rem=rem_fonts and path.startswith('font.size.'))};")
        elif typ == "duration":
            out.append(f"  {name}: {css_duration(val)};")
        elif typ == "cubicBezier":
            out.append(f"  {name}: {css_bezier(val)};")
        elif typ == "number":
            out.append(f"  {name}: {fmt_num(val)};")
        elif typ == "fontWeight":
            out.append(f"  {name}: {fmt_num(val)};")
        elif typ == "fontFamily":
            fams = val if isinstance(val, list) else [val]
            out.append(f"  {name}: " + ", ".join(f'"{f}"' if " " in f else f for f in fams) + ";")
        elif typ == "shadow":
            layers = raw if isinstance(raw, list) else [raw]
            parts = []
            for lay, rl in zip(layers, val if isinstance(val, list) else [val]):
                if isinstance(lay, str):  # alias to another shadow token
                    parts.append(f"var({css_var(prefix, lay[1:-1])})")
                    continue
                col = lay["color"]
                cs = f"var({css_var(prefix, col[1:-1])})" if isinstance(col, str) else css_color(rl["color"])
                parts.append(("inset " if lay.get("inset") else "") + " ".join(css_dim(rl[k]) for k in ("offsetX", "offsetY", "blur", "spread")) + " " + cs)
            out.append(f"  {name}: {', '.join(parts)};")
        elif typ == "typography":
            fam = raw["fontFamily"]
            famv = f"var({css_var(prefix, fam[1:-1])})" if isinstance(fam, str) and fam.startswith("{") else ", ".join(val["fontFamily"])
            size = raw["fontSize"]
            sizev = f"var({css_var(prefix, size[1:-1])})" if isinstance(size, str) else css_dim(val["fontSize"], rem=True)
            wt = raw["fontWeight"]
            wv = f"var({css_var(prefix, wt[1:-1])})" if isinstance(wt, str) and wt.startswith("{") else fmt_num(val["fontWeight"])
            em = (t.get("$extensions") or {}).get(NS, {}).get("letterSpacingEm", 0)
            lh = fmt_num(val["lineHeight"])
            out.append(f"  {name}-size: {sizev};")
            out.append(f"  {name}-line-height: {lh};")
            out.append(f"  {name}-weight: {wv};")
            out.append(f"  {name}-tracking: {fmt_num(em)}em;")
            out.append(f"  {name}-family: {famv};")
            out.append(f"  {name}: {wv} {sizev}/calc({lh} * var(--{prefix}-script-line-height-scale, 1)) {famv};")
        elif typ == "transition":
            sp = spring_ext(t, flat)
            if sp and "css" in sp:
                out.append(f"  {name}-duration: {sp['css']['durationMs']}ms;")
                out.append(f"  {name}-easing: {sp['css']['easing']};")
            else:
                out.append(f"  {name}-duration: {css_duration(val['duration'])};")
                out.append(f"  {name}-easing: {css_bezier(val['timingFunction'])};")
            out.append(f"  {name}-delay: {css_duration(val['delay'])};")
    return out


def token_paths_in(files, fnames):
    paths = []
    for fn in fnames:
        paths += list(flatten(files[fn]))
    return paths


def export_css(files, meta, prefix):
    res = files["opendesigner.resolver.json"]
    mods = res.get("modifiers", {})
    foundation_files = [s["$ref"] for s in res["sets"]["foundation"]["sources"]]
    theme_ctx = mods.get("theme", {}).get("contexts") or {meta["modes"][0]: res["sets"]["theme"]["sources"]}
    default_theme = mods.get("theme", {}).get("default", meta["modes"][0])
    dens = mods["density"]
    mot = mods["motion"]
    head = [f"/* {meta.get('name')} design tokens. Generated by the OpenDesigner engine {ENGINE_VERSION} from state.json;",
            "   do not edit by hand. Source of truth: tokens/*.tokens.json (DTCG 2025.10) + opendesigner.resolver.json.",
            "   Themes: prefers-color-scheme with a [data-theme] override. Density: [data-density]. Motion: prefers-reduced-motion",
            "   with a [data-motion] override. Font sizes are rem so browser text zoom works (WCAG 1.4.4). */", ""]
    lines = list(head)

    def block(selector, choice, fnames, indent=""):
        flat = resolve_all(files, choice)
        paths = token_paths_in(files, fnames)
        body = css_decls(flat, prefix, paths)
        return [f"{indent}{selector} {{"] + [indent + b for b in body] + [f"{indent}}}"]

    base_choice = {"theme": default_theme, "density": dens["default"], "motion": mot["default"]}
    lines += block(":root", base_choice, foundation_files)
    lines.append("")
    for mode, srcs in theme_ctx.items():
        fn = [s["$ref"] for s in srcs]
        sel = f':root, [data-theme="{mode}"]' if mode == default_theme else f'[data-theme="{mode}"]'
        blk = block(sel, dict(base_choice, theme=mode), fn)
        blk.insert(1, f"  color-scheme: {mode};")
        lines += blk + [""]
    if "dark" in theme_ctx and default_theme != "dark":
        blk = block(':root:not([data-theme="light"])', dict(base_choice, theme="dark"),
                    [s["$ref"] for s in theme_ctx["dark"]], indent="  ")
        blk.insert(1, "    color-scheme: dark;")
        lines += ["@media (prefers-color-scheme: dark) {"] + blk + ["}", ""]
    for dname, srcs in dens["contexts"].items():
        sel = f':root, [data-density="{dname}"]' if dname == dens["default"] else f'[data-density="{dname}"]'
        lines += block(sel, dict(base_choice, density=dname), [s["$ref"] for s in srcs]) + [""]
    for cname, srcs in mot["contexts"].items():
        sel = f':root, [data-motion="{cname}"]' if cname == mot["default"] else f'[data-motion="{cname}"]'
        lines += block(sel, dict(base_choice, motion=cname), [s["$ref"] for s in srcs]) + [""]
    if mot["default"] != "reduced":
        lines += ["@media (prefers-reduced-motion: reduce) {"]
        lines += block(':root:not([data-motion="standard"])', dict(base_choice, motion="reduced"),
                       [s["$ref"] for s in mot["contexts"]["reduced"]], indent="  ") + ["}", ""]
    tg = meta["space"]["targets"]
    if "touch" in tg and "pointer" in tg:
        lines += ["/* Hit-area floor per input (L14 I-1, DC-L03-12): pointer 24px (WCAG 2.5.8), touch 44/48. */",
                  "@media (pointer: fine) {", f"  :root {{ {css_var(prefix, 'size.target.min')}: {tg['pointer']}px; }}", "}",
                  "@media (pointer: coarse) {", f"  :root {{ {css_var(prefix, 'size.target.min')}: {tg['touch']}px; }}", "}", ""]
    # Display P3 upgrades where sRGB clipped chroma (luminance kept within 1.5%, so contrast pairs hold)
    p3 = []
    prim = flatten(files["primitives.tokens.json"])
    for path, t in prim.items():
        ext = (t.get("$extensions") or {}).get(NS, {})
        if "p3" in ext:
            c = ext["p3"]["components"]
            p3.append(f"    {css_var(prefix, path)}: color(display-p3 {' '.join(fmt_num(x) for x in c)});")
    if p3:
        lines += ["@media (color-gamut: p3) {", "  :root {"] + p3 + ["  }", "}", ""]
    scripts = meta["type"].get("scripts") or {}
    lang = {"Arab": "ar", "Beng": "bn", "Hans": "zh-Hans", "Hant": "zh-Hant", "Deva": "hi", "Jpan": "ja", "Kore": "ko", "Thai": "th",
            "Viet": "vi", "Mymr": "my", "Telu": "te", "Aran": "ur"}
    for code, info in sorted(scripts.items()):
        if code in lang:
            f = info.get("lineHeightFactor", 1)
            if code in ("Hans", "Hant", "Jpan", "Kore"):
                f = rnd(info["cjk"]["lineHeight"]["body"] / 1.5, 3)
            lines += [f":lang({lang[code]}) {{ --{prefix}-script-line-height-scale: {fmt_num(f)}; }}"
                      + (" /* zero tracking for this script (DC-L02-14) */" if info.get("zeroTracking") else "")]
    if scripts:
        lines.append("")
    # utility classes for text styles and focus
    lines.append("/* Text style classes (one per typography token). */")
    for path, t in resolve_all(files, base_choice).items():
        if t["type"] == "typography":
            v = css_var(prefix, path)
            cls = "." + prefix + "-" + "-".join(kebab(s) for s in path.split("."))
            ext_ = (t.get("$extensions") or {}).get(NS, {})
            extra = (" text-transform: uppercase;" if ext_.get("textTransform") else "") + \
                (f" font-variant-numeric: {ext_['fontVariantNumeric']};" if ext_.get("fontVariantNumeric") else "")
            lines.append(f"{cls} {{ font: var({v}); letter-spacing: var({v}-tracking);{extra} }}")
    lines += ["", f".{prefix}-focus-ring:focus-visible {{",
              f"  outline: var({css_var(prefix, 'focus.ring.width')}) solid var({css_var(prefix, 'color.border.focus')});",
              f"  outline-offset: var({css_var(prefix, 'focus.ring.offset')});"]
    if any(k.endswith("focus-inner") for k in flatten(files[[s['$ref'] for s in theme_ctx[default_theme]][0]])):
        lines.append(f"  box-shadow: 0 0 0 var({css_var(prefix, 'focus.ring.offset')}) var({css_var(prefix, 'color.border.focus-inner')});")
    lines += ["}", "@media (forced-colors: active) {", f"  .{prefix}-focus-ring:focus-visible {{ outline-color: Highlight; }}", "}", ""]
    return "\n".join(lines)


TW_COLOR_MAP = [("color.surface.", "surface-"), ("color.text.", "fg-"), ("color.bg.", ""), ("color.border.", "line-"),
                ("color.icon.", "icon-"), ("color.overlay.", "overlay-"), ("color.chart.", "chart-"), ("color.workflow.", "workflow-")]


def export_tailwind(files, meta, prefix, reset=True):
    """Tailwind CSS v4 theme (U5 F7, F8, F15): imports tokens.css itself, so one @import is enough; optionally switches off
    Tailwind's default colors, text sizes, radii and shadows so only the design system's values compile."""
    flat = resolve_all(files, {})
    unit = meta["space"]["unit"]
    lines = [f"/* Tailwind CSS v4 theme for {meta.get('name')}. Generated by the OpenDesigner engine {ENGINE_VERSION}.",
             "   Usage, in your main CSS file (one import is enough; this file imports tokens.css itself):",
             "     @import \"tailwindcss\";",
             "     @import \"<path from your CSS file>/opendesigner/build/tailwind/theme.css\";",
             "   @theme inline points utilities at the design-system variables, so light/dark, density and reduced",
             "   motion keep working through data-theme / data-density / data-motion and the media queries in tokens.css."
             + (" Tailwind's default colors, text sizes, radii and shadows are switched off (exports.tailwindReset); "
                "set it to false to keep them." if reset else "") + " */",
             "@import \"../css/tokens.css\";", ""]
    if reset:
        lines += ["@theme {", "  --color-*: initial;", "  --text-*: initial;", "  --radius-*: initial;", "  --shadow-*: initial;", "}", ""]
    bps = (meta.get("space") or {}).get("breakpoints") or {}
    if bps:  # media queries cannot read var(), so breakpoints are literal values
        lines += ["@theme {"] + (["  --breakpoint-*: initial;"] if reset else []) + \
                 [f"  --breakpoint-{k}: {fmt_num(rnd(v / 16, 4))}rem; /* {v}px */" for k, v in bps.items()] + ["}", ""]
    lines += ["@theme inline {", f"  --spacing: {unit}px; /* p-1 = one base unit (LEVERS B8) */"]
    for path in sorted(flat):
        t = flat[path]
        v = f"var({css_var(prefix, path)})"
        if t["type"] == "color" and not re.match(r"color\.(neutral|accent|action|success|warning|danger|info|discovery|neutral-alpha|accent2|accent3|white|black|brand|focus)\b", path):
            for src, dst in TW_COLOR_MAP:
                if path.startswith(src):
                    rest = "-".join(kebab(s_) for s_ in path[len(src):].split("."))
                    lines.append(f"  --color-{dst}{rest}: {v};")
                    break
    lines.append("  --color-white: #fff;")
    lines.append("  --color-transparent: transparent;")
    lines.append("  --color-current: currentColor;")
    for fam in ("text", "display", "mono"):
        name = {"text": "sans", "display": "display", "mono": "mono"}[fam]
        lines.append(f"  --font-{name}: var({css_var(prefix, 'font.family.' + fam)});")
    for path in sorted(flat):
        if path.startswith("font.weight."):
            lines.append(f"  --font-weight-{kebab(path.split('.')[-1])}: var({css_var(prefix, path)});")
    for path in sorted(flat):
        t = flat[path]
        if t["type"] == "typography":
            n = "-".join(kebab(s_) for s_ in path.split(".")[1:])
            v = css_var(prefix, path)
            lines += [f"  --text-{n}: var({v}-size);", f"  --text-{n}--line-height: var({v}-line-height);",
                      f"  --text-{n}--letter-spacing: var({v}-tracking);", f"  --text-{n}--font-weight: var({v}-weight);"]
    for path in sorted(flat):
        if re.match(r"space\.(inset|stack|inline|section)\.", path):
            lines.append(f"  --spacing-{'-'.join(kebab(s_) for s_ in path.split('.')[1:])}: var({css_var(prefix, path)});")
        elif re.match(r"size\.(control|target|icon|row)\.", path):  # h-control-md, size-icon-sm (no doubled size- prefix)
            lines.append(f"  --spacing-{'-'.join(kebab(s_) for s_ in path.split('.')[1:])}: var({css_var(prefix, path)});")
    for r in ("detail", "control", "control-sm", "container", "overlay", "person", "full"):
        lines.append(f"  --radius-{kebab(r)}: var({css_var(prefix, 'radius.' + r)});")
    for e in ("raised", "floating", "overlay"):
        lines.append(f"  --shadow-{e}: var({css_var(prefix, 'elevation.' + e)});")
    for e in ("standard", "enter", "exit", "linear"):
        lines.append(f"  --ease-{e}: var({css_var(prefix, 'motion.easing.' + e)});")
    lines += ["}", ""]
    lines += ["/* Semantic motion helpers (durations follow the reduced-motion mode automatically). */",
              "@utility transition-feedback {", f"  transition-duration: var({css_var(prefix, 'motion.transition.feedback')}-duration);",
              f"  transition-timing-function: var({css_var(prefix, 'motion.transition.feedback')}-easing);", "}", ""]
    num = [p for p in flat if p.startswith("text.numeric.")]
    if num:
        lines += ["/* Tabular figures for amounts and tables (text.numeric.*). */", "@utility tabular {", "  font-variant-numeric: tabular-nums;", "}", ""]
    return "\n".join(lines)


def _figma_rgba(v):
    r, g, b = (c / 255 for c in hex_to_rgb8(hex_of(v)))
    return {"r": rnd(r, 4), "g": rnd(g, 4), "b": rnd(b, 4), "a": rnd(v.get("alpha", 1) if isinstance(v, dict) else 1, 3)}


def figma_scopes(path, typ):
    if typ == "color":
        if path.startswith("color.text."):
            return ["TEXT_FILL"]
        if path.startswith(("color.surface.", "color.bg.", "color.overlay.")):
            return ["FRAME_FILL", "SHAPE_FILL"]
        if path.startswith("color.border."):
            return ["STROKE_COLOR"]
        if path.startswith("color.icon."):
            return ["SHAPE_FILL", "STROKE_COLOR"]
        if path.startswith("color.shadow."):
            return ["EFFECT_COLOR"]
        return []
    if path.startswith("space."):
        return ["GAP"]
    if path.startswith(("size.control", "size.target", "size.icon")):
        return ["WIDTH_HEIGHT"]
    if path.startswith("radius."):
        return ["CORNER_RADIUS"]
    if path.startswith(("border.width", "focus.ring", "icon.stroke")):
        return ["STROKE_FLOAT"]
    if path.startswith("font.size."):
        return ["FONT_SIZE"]
    if path.startswith("font.line-height."):
        return ["LINE_HEIGHT"]
    if path.startswith("font.weight."):
        return ["FONT_WEIGHT"]
    if path.startswith("font.family."):
        return ["FONT_FAMILY"]
    if path.startswith("opacity."):
        return ["OPACITY"]
    return []


def code_syntax(prefix, path):
    """Figma code syntax that matches the names the Swift and Compose exports actually define (DC-L07-20)."""
    parts = path.split(".")
    P, K = prefix.upper(), prefix.capitalize()
    out = {"WEB": f"var({css_var(prefix, path)})"}
    if re.match(r"color\.(surface|text|bg|border|icon|overlay|shadow)\.", path):
        out["iOS"] = f"{P}.Colors.{camel(parts[1:])}"
        out["ANDROID"] = f"Local{K}Colors.current.{camel(parts[1:])}"
    elif re.match(r"(space|size)\.", path):
        out["iOS"] = f"{P}.Space.{camel(parts)}"
        out["ANDROID"] = f"{K}Space.{camel(parts)}"
    elif re.match(r"(radius|border|focus)\.", path):
        out["iOS"] = f"{P}.Radius.{camel(parts)}"
        out["ANDROID"] = f"{K}Space.{camel(parts)}"
    elif path.startswith("motion.duration."):
        out["iOS"] = f"{P}.Motion.{camel(parts[1:])}"
        out["ANDROID"] = f"{K}Motion.{camel(parts[1:])}Ms"
    return out


GENERIC_FONTS = {"system-ui", "-apple-system", "blinkmacsystemfont", "ui-sans-serif", "ui-monospace", "ui-serif", "sans-serif",
                 "serif", "monospace", "segoe ui", "helvetica neue", "arial", "sf mono", "menlo", "consolas", "liberation mono"}


def figma_font(fams):
    """Figma needs a real family name: the first non-generic family, else Inter / Roboto Mono (both on Google Fonts)."""
    fams = fams if isinstance(fams, list) else [fams]
    for f in fams:
        if f.lower() not in GENERIC_FONTS:
            return f
    return "Roboto Mono" if any("mono" in f.lower() for f in fams) else "Inter"


FIGMA_STYLE = {100: "Thin", 200: "Extra Light", 300: "Light", 400: "Regular", 500: "Medium", 600: "Semi Bold", 700: "Bold",
               800: "Extra Bold", 900: "Black"}


def export_figma(files, meta, state, prefix):
    res = files["opendesigner.resolver.json"]
    mods = res.get("modifiers", {})
    plan = (state.get("exports") or {}).get("figmaPlan", "professional")
    limit = FIGMA_MODE_LIMITS.get(plan, 10)
    flat0 = resolve_all(files, {})
    primitive_paths = {p for p in token_paths_in(files, ["primitives.tokens.json"])
                       if flat0.get(p, {}).get("type") in ("color", "dimension", "number", "fontWeight", "fontFamily")}

    def var_entry(path, t, collection, modes_vals):
        typ = t["type"]
        ftype = {"color": "COLOR", "dimension": "FLOAT", "number": "FLOAT", "fontWeight": "FLOAT", "fontFamily": "STRING",
                 "duration": "TIMING", "cubicBezier": "EASING"}.get(typ)
        if not ftype:
            return None
        e = {"name": path.replace(".", "/"), "type": ftype, "valuesByMode": modes_vals,
             "scopes": [] if path in primitive_paths else figma_scopes(path, typ),
             "codeSyntax": code_syntax(prefix, path), "description": (t.get("$description") or "")[:500]}
        if ftype == "TIMING":
            e["fallback"] = {"type": "FLOAT", "unit": "ms"}
        if ftype == "EASING":
            e["fallback"] = {"type": "STRING", "format": "cubic-bezier(x1, y1, x2, y2)"}
        return e

    def value_for(path, t, flatc, primitive_names):
        raw = t["$value"]
        if isinstance(raw, str) and raw.startswith("{") and raw[1:-1] in primitive_names:
            return {"type": "VARIABLE_ALIAS", "name": raw[1:-1].replace(".", "/"), "collection": primitive_names[raw[1:-1]]}
        v = t["resolved"]
        typ = t["type"]
        if typ == "color":
            return _figma_rgba(v)
        if typ == "dimension":
            return rnd(_px(v), 3)
        if typ == "duration":
            return rnd(v["value"] / (1000 if v["unit"] == "ms" else 1), 4)  # plugin API timing is in seconds (L07)
        if typ == "cubicBezier":
            return {"type": "CUBIC_BEZIER", "x1": v[0], "y1": v[1], "x2": v[2], "y2": v[3]}
        if typ == "fontFamily":
            return v[0] if isinstance(v, list) else v
        return v

    collections = []
    names = {}
    # 1. Primitives (hidden from publishing)
    prim_vars = []
    for p in sorted(primitive_paths):
        t = flat0[p]
        ent = var_entry(p, t, "Primitives", {"Value": value_for(p, t, flat0, {})})
        if ent:
            prim_vars.append(ent)
            names[p] = "Primitives"
    collections.append({"name": "Primitives", "modes": ["Value"], "hiddenFromPublishing": True, "variables": prim_vars})

    def moded(collection, modifier, fnames_by_ctx):
        ctxs = list(fnames_by_ctx)
        per = {c: resolve_all(files, {modifier: c}) if modifier else flat0 for c in ctxs}
        paths = token_paths_in(files, fnames_by_ctx[ctxs[0]])
        vars_ = []
        for p in paths:
            t0 = per[ctxs[0]][p]
            vals = {c.title(): value_for(p, per[c][p], per[c], names) for c in ctxs}
            ent = var_entry(p, t0, collection, vals)
            if ent:
                vars_.append(ent)
        return {"name": collection, "modes": [c.title() for c in ctxs], "variables": vars_}
    theme_srcs = {c: [s["$ref"] for s in v] for c, v in mods["theme"]["contexts"].items()} if "theme" in mods else \
        {meta["modes"][0]: [s["$ref"] for s in res["sets"]["theme"]["sources"]]}
    collections.append(moded("Color", "theme" if "theme" in mods else None, theme_srcs))
    collections.append(moded("Density", "density", {c: [s["$ref"] for s in v] for c, v in mods["density"]["contexts"].items()}))
    # motion: transitions become duration + easing variables per mode
    mvars = []
    for c in mods["motion"]["contexts"]:
        pass
    per = {c: resolve_all(files, {"motion": c}) for c in mods["motion"]["contexts"]}
    for p in sorted(k for k in per["standard"] if k.startswith("motion.transition.")):
        for part in ("duration", "easing"):
            vals = {}
            for c, fl in per.items():
                sp = spring_ext(fl[p], fl)
                v = fl[p]["resolved"]
                if part == "duration":
                    vals[c.title()] = rnd((sp["css"]["durationMs"] if sp and c == "standard" else v["duration"]["value"]) / 1000, 4)
                else:
                    if sp and c == "standard" and sp["spring"]["dampingRatio"] < 1:
                        vals[c.title()] = {"type": "SPRING", "damping": sp["spring"]["dampingRatio"], "stiffness": sp["spring"]["stiffness"],
                                           "mass": 1, "bounce": sp["apple"]["bounce"]}
                    else:
                        tf = v["timingFunction"]
                        vals[c.title()] = {"type": "CUBIC_BEZIER", "x1": tf[0], "y1": tf[1], "x2": tf[2], "y2": tf[3]}
            mvars.append({"name": p.replace(".", "/") + "/" + part, "type": "TIMING" if part == "duration" else "EASING",
                          "valuesByMode": vals, "scopes": [], "codeSyntax": code_syntax(prefix, p + "." + part),
                          "fallback": {"type": "FLOAT", "unit": "ms"} if part == "duration" else {"type": "STRING"}})
    collections.append({"name": "Motion", "modes": [c.title() for c in mods["motion"]["contexts"]], "variables": mvars})
    # 4. mode-independent semantic tokens (radius roles, sizes, weights, families, opacity, durations, easings)
    sem = []
    for p in sorted(flat0):
        if p in primitive_paths or p in names or re.match(r"(color\.|space\.(inset|stack|inline|section)|size\.control|motion\.transition|text\.|elevation\.)", p):
            continue
        ent = var_entry(p, flat0[p], "Tokens", {"Value": value_for(p, flat0[p], flat0, names)})
        if ent:
            sem.append(ent)
    collections.append({"name": "Tokens", "modes": ["Value"], "variables": sem})
    warnings = []
    final = []
    for col in collections:
        if len(col["modes"]) > limit:
            warnings.append(f"{col['name']}: {len(col['modes'])} modes exceed the {plan} limit of {limit}; split into one collection per mode.")
            for m in col["modes"]:
                final.append({"name": f"{col['name']} ({m})", "modes": ["Value"],
                              "variables": [dict(v, valuesByMode={"Value": v["valuesByMode"][m]}) for v in col["variables"]]})
        else:
            final.append(col)
        if len(col["variables"]) > 5000:
            warnings.append(f"{col['name']}: more than 5,000 variables per collection (Figma limit).")
    # text and effect styles (composites are styles in Figma, not variables)
    light = resolve_all(files, {"theme": "light"} if "theme" in mods else {})
    text_styles, effect_styles = [], []
    for p, t in sorted(light.items()):
        if t["type"] == "typography":
            v = t["resolved"]
            ext = (t.get("$extensions") or {}).get(NS, {})
            raw = t["$value"]
            text_styles.append({"name": p.replace(".", "/"), "fontFamily": figma_font(v["fontFamily"]),
                                "fontStyle": FIGMA_STYLE[min(900, max(100, int(round(v["fontWeight"] / 100) * 100)))],
                                "fontSize": _px(v["fontSize"]), "fontWeight": v["fontWeight"],
                                "lineHeight": {"unit": "PIXELS", "value": ext.get("lineHeightPx")},
                                "letterSpacing": {"unit": "PERCENT", "value": rnd(ext.get("letterSpacingEm", 0) * 100, 2)},
                                "textCase": "UPPER" if ext.get("textTransform") else "ORIGINAL",
                                "boundVariables": {"fontSize": raw["fontSize"][1:-1].replace(".", "/"),
                                                   "fontWeight": raw["fontWeight"][1:-1].replace(".", "/"),
                                                   "fontFamily": raw["fontFamily"][1:-1].replace(".", "/")}})
        if t["type"] == "shadow" and p.startswith("elevation.") and p.count(".") == 1:
            layers = t["resolved"] if isinstance(t["resolved"], list) else [t["resolved"]]
            eff = []
            for lay in layers:
                if isinstance(lay, list):
                    for sub in lay:
                        eff.append(sub)
                else:
                    eff.append(lay)
            effect_styles.append({"name": p.replace(".", "/"), "effects": [
                {"type": "DROP_SHADOW", "color": _figma_rgba(l["color"]), "offset": {"x": _px(l["offsetX"]), "y": _px(l["offsetY"])},
                 "radius": _px(l["blur"]), "spread": _px(l["spread"]), "visible": True, "blendMode": "NORMAL"} for l in eff]})
    return {"$schema": "opendesigner/figma-variables/1", "generatedBy": f"OpenDesigner engine {ENGINE_VERSION}",
            "about": "Payload for the Figma MCP use_figma write flow (or a plugin): create collections in order, primitives first, "
                     "then alias semantic variables by name. Colors are sRGB 0-1. TIMING values are seconds and EASING values are "
                     "cubic-bezier or spring objects (plugin API, 5 Aug 2026, L07); if the file rejects them, use each variable's "
                     "fallback. Composite tokens become text styles and effect styles (light values; bind colors to the Color collection).",
            "plan": plan, "limits": {"modesPerCollection": limit, "variablesPerCollection": 5000, "codeSyntaxPlatforms": 3},
            "warnings": warnings, "collections": final, "textStyles": text_styles, "effectStyles": effect_styles}


PAPER_TYPES = [("color", None), ("spacing", "space."), ("radius", "radius."), ("fontSize", "font.size."), ("lineHeight", "font.line-height."),
               ("fontWeight", "font.weight."), ("fontFamily", "font.family."), ("opacity", "opacity.")]


def export_paper(files, meta, prefix):
    """Paper has no modes yet: one flat token list per theme, literal values in create_tokens order
    (semantic colors first, neutral before accents; other types smallest first)."""
    res = files["opendesigner.resolver.json"]
    mods = res.get("modifiers", {})
    themes = list(mods["theme"]["contexts"]) if "theme" in mods else meta["modes"]
    out = {}
    css = {}
    for theme in themes:
        flat = resolve_all(files, {"theme": theme} if "theme" in mods else {})
        entries = []
        sem = [p for p in flat if flat[p]["type"] == "color" and re.match(r"color\.(surface|text|bg|border|icon)\.", p)]
        sem.sort(key=lambda p: (0 if ("neutral" in p or p.startswith(("color.surface", "color.text.primary", "color.text.secondary"))) else 1, p))
        prim = [p for p in flat if flat[p]["type"] == "color" and re.match(rf"color\.(neutral|accent|action|accent2|accent3|success|warning|danger|info)\.{theme}\.", p)]
        order = {"neutral": 0, "accent": 1, "action": 2, "accent2": 3, "accent3": 4}
        prim.sort(key=lambda p: (order.get(p.split(".")[1], 5), p.split(".")[1],
                             int(p.split(".")[-1]) if p.split(".")[-1].isdigit() else 99))
        for p in sem + prim:
            t = flat[p]
            entries.append({"type": "color", "name": css_var(prefix, p), "value": css_color(t["resolved"]), "description": (t["$description"] or "")[:200]})
        for ptype, pre in PAPER_TYPES[1:]:
            group = []
            for p, t in flat.items():
                if not p.startswith(pre) or t["type"] not in ("dimension", "fontWeight", "fontFamily", "number"):
                    continue
                v = t["resolved"]
                if t["type"] == "dimension":
                    num, val = _px(v), f"{fmt_num(_px(v))}px"
                elif t["type"] == "fontFamily":
                    num, val = 0, ", ".join(v) if isinstance(v, list) else v
                else:
                    num, val = v, v
                group.append((num, p, val, t["$description"]))
            group.sort(key=lambda x: (x[0], x[1]))
            for num, p, val, desc in group:
                entries.append({"type": ptype, "name": css_var(prefix, p), "value": val, "description": (desc or "")[:200]})
        out[theme] = entries
        css[theme] = ":root {\n" + "\n".join(f"  {e['name']}: {e['value']};" for e in entries) + "\n}\n"
    payload = {"$about": "Tokens for Paper's create_tokens MCP tool (Paper has no modes yet, so each theme is a separate list; "
                         "use one theme per file or page). Values are literal, not var() aliases, so creation order cannot break references.",
               "generatedBy": f"OpenDesigner engine {ENGINE_VERSION}", "themes": out}
    return payload, css


IOS_TEXT_STYLES = {  # our text style -> (SwiftUI text style, its default size in pt) (Apple HIG type sizes, S-L02-001)
    "display": (".largeTitle", 34), "headline.lg": (".title", 28), "headline.md": (".title2", 22), "headline.sm": (".title3", 20),
    "title.lg": (".title3", 20), "title.md": (".headline", 17), "title.sm": (".headline", 17), "body.lg": (".body", 17),
    "body.md": (".body", 17), "body.sm": (".subheadline", 15), "label.lg": (".body", 17), "label.md": (".subheadline", 15),
    "label.sm": (".caption", 12), "code.md": (".body", 17), "code.sm": (".footnote", 13), "numeric.md": (".body", 17),
    "numeric.lg": (".title2", 22)}


def export_swift(files, meta, prefix):
    res = files["opendesigner.resolver.json"]
    mods = res.get("modifiers", {})
    P = prefix.upper()
    light = resolve_all(files, {"theme": "light"} if "theme" in mods else {})
    dark = resolve_all(files, {"theme": "dark"}) if "theme" in mods and "dark" in mods["theme"]["contexts"] else light
    base = resolve_all(files, {})
    L = [f"// {meta.get('name')} design tokens for SwiftUI. Generated by the OpenDesigner engine {ENGINE_VERSION}; do not edit.",
         "// Colors switch with the system appearance. Spacing uses the default density; text uses Dynamic Type text styles.",
         "import SwiftUI", "#if canImport(UIKit)", "import UIKit", "#elseif canImport(AppKit)", "import AppKit", "#endif", "",
         f"public enum {P} {{}}", "",
         "private func dsColor(_ light: UInt32, _ dark: UInt32, _ la: Double = 1, _ da: Double = 1) -> Color {",
         "    func comps(_ v: UInt32) -> (Double, Double, Double) {",
         "        (Double((v >> 16) & 0xFF) / 255, Double((v >> 8) & 0xFF) / 255, Double(v & 0xFF) / 255)",
         "    }",
         "    let (lr, lg, lb) = comps(light), (dr, dg, db) = comps(dark)",
         "    #if canImport(UIKit)",
         "    return Color(UIColor { $0.userInterfaceStyle == .dark",
         "        ? UIColor(red: dr, green: dg, blue: db, alpha: da) : UIColor(red: lr, green: lg, blue: lb, alpha: la) })",
         "    #elseif canImport(AppKit)",
         "    return Color(NSColor(name: nil) { $0.bestMatch(from: [.darkAqua, .aqua]) == .darkAqua",
         "        ? NSColor(red: dr, green: dg, blue: db, alpha: da) : NSColor(red: lr, green: lg, blue: lb, alpha: la) })",
         "    #else",
         "    return Color(red: lr, green: lg, blue: lb, opacity: la)",
         "    #endif",
         "}", "", f"public extension {P} {{", "    enum Colors {"]
    for p in sorted(light):
        if light[p]["type"] == "color" and re.match(r"color\.(surface|text|bg|border|icon|overlay|shadow)\.", p):
            lv, dv = light[p]["resolved"], dark[p]["resolved"]
            la, da = lv.get("alpha", 1), dv.get("alpha", 1)
            L.append(f"        public static let {camel(p.split('.')[1:])} = dsColor(0x{hex_of(lv)[1:].upper()}, 0x{hex_of(dv)[1:].upper()}"
                     + (f", {fmt_num(la)}, {fmt_num(da)})" if (la != 1 or da != 1) else ")"))
    L += ["    }", "", "    enum Space {"]
    for p in sorted(base, key=lambda x: (x.split(".")[:2], _px(base[x]["resolved"]) if base[x]["type"] == "dimension" else 0)):
        t = base[p]
        if t["type"] == "dimension" and re.match(r"(space|size)\.", p):
            L.append(f"        public static let {camel(p.split('.'))}: CGFloat = {fmt_num(_px(t['resolved']))}")
    L += ["    }", "", "    enum Radius {"]
    for p in sorted(base):
        t = base[p]
        if t["type"] == "dimension" and p.startswith(("radius.", "border.width.", "focus.ring.")):
            L.append(f"        public static let {camel(p.split('.'))}: CGFloat = {fmt_num(_px(t['resolved']))}")
    faces = (meta.get("type") or {}).get("faces") or {}
    scaling = (meta.get("textScaling") or "full")
    notes = []
    for role, f in faces.items():
        if f and not f.get("open") and f.get("face") not in (None, "=textFace") and f.get("app") is not True:
            why = "is not licensed for apps" if f.get("app") is False else "has no recorded app licence (raw.fontLicence.app)"
            notes.append(f"    // {f['face']} {why}, so the {role} styles use the system font (San Francisco) here.")
    L += ["    }", "", "    /// Text styles use Dynamic Type (U5 F22): iOS sizes come from the text style (body 17 pt), not the web scale,",
          "    /// and follow the person's text size setting" + {"full": ".", "capped": "; cap chrome text such as tab labels with "
                                                              ".dynamicTypeSize(...DynamicTypeSize.accessibility2) (Q-type-17).",
                                                              "none": "; Q-type-17 'none' keeps fixed sizes."}.get(scaling, "."),
          *notes, "    enum Typography {"]
    wname_of = {100: "ultraLight", 200: "thin", 300: "light", 400: "regular", 500: "medium", 600: "semibold", 700: "bold", 800: "heavy", 900: "black"}
    for p in sorted(base):
        t = base[p]
        if t["type"] != "typography":
            continue
        v = t["resolved"]
        rawv = t["$value"]
        role_fam = rawv["fontFamily"][1:-1].split(".")[-1] if isinstance(rawv.get("fontFamily"), str) and rawv["fontFamily"].startswith("{") else "text"
        key = ".".join(p.split(".")[1:])
        key = key[len("emphasized."):] if key.startswith("emphasized.") else key
        style, size = IOS_TEXT_STYLES.get(key) or IOS_TEXT_STYLES.get(key.split(".")[0], (".body", 17))
        wt = int(v["fontWeight"])
        wname = wname_of[min(900, max(100, int(round(wt / 100) * 100)))]
        f = faces.get("display" if role_fam == "display" else "text") or {}
        face_name = f.get("face") if isinstance(f.get("face"), str) else "system"
        if role_fam == "display" and face_name == "=textFace":
            f = faces.get("text") or {}
            face_name = f.get("face") if isinstance(f.get("face"), str) else "system"
        mono = key.startswith("code.")
        if mono:
            mf = v["fontFamily"][0] if isinstance(v["fontFamily"], list) else v["fontFamily"]
            custom = None if _generic_face(mf) or mf.lower() not in OPEN_FONTS else mf
            design = ".monospaced"
        else:
            custom = None if (_generic_face(face_name) or (not f.get("open") and f.get("app") is not True)) else face_name
            design = {"=serif": ".serif", "=rounded": ".rounded"}.get(face_name, ".default")
        if custom:
            expr = (f"Font.custom(\"{custom}\", fixedSize: {size}).weight(.{wname})" if scaling == "none"
                    else f"Font.custom(\"{custom}\", size: {size}, relativeTo: {style}).weight(.{wname})")
        else:
            expr = (f"Font.system(size: {size}, weight: .{wname}, design: {design})" if scaling == "none"
                    else f"Font.system({style}, design: {design}, weight: .{wname})")
        L.append(f"        public static let {camel(p.split('.')[1:])} = {expr}")
    L += ["    }", "", "    enum Motion {"]
    for p in sorted(base):
        t = base[p]
        if t["type"] == "duration":
            L.append(f"        public static let {camel(p.split('.')[1:])}: Double = {fmt_num(rnd(t['resolved']['value'] / 1000, 3))}")
        sp = (t.get("$extensions") or {}).get(NS, {}).get("apple") if t["type"] == "transition" and p.startswith("motion.spring.") else None
        if sp:
            L.append(f"        public static let {camel(p.split('.')[1:])} = Animation.spring(duration: {fmt_num(sp['duration'])}, bounce: {fmt_num(sp['bounce'])})")
    L += ["    }", "}", ""]
    return "\n".join(L)


def export_compose(files, meta, prefix):
    res = files["opendesigner.resolver.json"]
    mods = res.get("modifiers", {})
    P = prefix.capitalize()
    light = resolve_all(files, {"theme": "light"} if "theme" in mods else {})
    dark = resolve_all(files, {"theme": "dark"}) if "theme" in mods and "dark" in mods["theme"]["contexts"] else light
    base = resolve_all(files, {})
    cols = [p for p in sorted(light) if light[p]["type"] == "color" and re.match(r"color\.(surface|text|bg|border|icon|overlay|shadow)\.", p)]

    def argb(v):
        a = round_half_up((v.get("alpha", 1) if isinstance(v, dict) else 1) * 255)
        return f"Color(0x{a:02X}{hex_of(v)[1:].upper()})"
    K = [f"// {meta.get('name')} design tokens for Jetpack Compose. Generated by the OpenDesigner engine {ENGINE_VERSION}; do not edit.",
         f"package {slug(prefix).replace('-', '')}.tokens", "",
         "import androidx.compose.animation.core.spring", "import androidx.compose.runtime.Immutable",
         "import androidx.compose.runtime.staticCompositionLocalOf", "import androidx.compose.ui.graphics.Color",
         "import androidx.compose.ui.text.TextStyle", "import androidx.compose.ui.text.font.FontFamily",
         "import androidx.compose.ui.text.font.FontWeight",
         "import androidx.compose.ui.unit.dp", "import androidx.compose.ui.unit.em", "import androidx.compose.ui.unit.sp", "",
         "@Immutable", f"data class {P}Colors("]
    K += [f"    val {camel(p.split('.')[1:])}: Color," for p in cols]
    K += [")", ""]
    for name, fl in (("Light", light), ("Dark", dark)):
        K.append(f"val {P}{name}Colors = {P}Colors(")
        K += [f"    {camel(p.split('.')[1:])} = {argb(fl[p]['resolved'])}," for p in cols]
        K += [")", ""]
    K += [f"val Local{P}Colors = staticCompositionLocalOf {{ {P}LightColors }}", "", f"object {P}Space {{"]
    for p in sorted(base):
        t = base[p]
        if t["type"] == "dimension" and re.match(r"(space|size|radius|border|focus)\.", p):
            v = _px(t["resolved"])
            K.append(f"    val {camel(p.split('.'))} = {fmt_num(v if v < FULL else 999)}.dp")
    faces = (meta.get("type") or {}).get("faces") or {}
    fam_lines = []
    for role, f in faces.items():
        if not f or f.get("face") in (None, "=textFace"):
            continue
        nm = f["face"] if isinstance(f["face"], str) else "system"
        if _generic_face(nm):
            fam_lines.append(f"// {role}: the system font (Roboto on most devices).")
        elif not f.get("open") and f.get("app") is not True:
            why = "is not licensed for apps" if f.get("app") is False else "has no recorded app licence (raw.fontLicence.app)"
            fam_lines.append(f"// {role}: {nm} {why}, so this app uses the system font. Do not bundle it.")
        else:
            fam_lines.append(f"// {role}: {nm}. Add its font files to res/font and replace FontFamily.Default with FontFamily(Font(R.font.<file>)).")
    K += ["}", ""] + fam_lines + [f"val {P}TextFamily: FontFamily = FontFamily.Default", "", f"object {P}Type {{"]
    for p in sorted(base):
        t = base[p]
        if t["type"] == "typography":
            v = t["resolved"]
            ext = (t.get("$extensions") or {}).get(NS, {})
            K.append(f"    val {camel(p.split('.')[1:])} = TextStyle(fontFamily = {P}TextFamily, fontSize = {fmt_num(_px(v['fontSize']))}.sp, "
                     f"lineHeight = {fmt_num(ext.get('lineHeightPx'))}.sp, fontWeight = FontWeight({int(v['fontWeight'])}), "
                     f"letterSpacing = {fmt_num(ext.get('letterSpacingEm', 0))}.em)")
    K += ["}", "", f"object {P}Motion {{"]
    for p in sorted(base):
        t = base[p]
        if t["type"] == "duration":
            K.append(f"    const val {camel(p.split('.')[1:])}Ms = {int(t['resolved']['value'])}")
        sp = (t.get("$extensions") or {}).get(NS, {}).get("spring") if t["type"] == "transition" and p.startswith("motion.spring.") else None
        if sp:
            K.append(f"    fun <T> {camel(p.split('.')[1:])}() = spring<T>(dampingRatio = {fmt_num(sp['dampingRatio'])}f, stiffness = {fmt_num(sp['stiffness'])}f)")
    K += ["}", ""]
    return "\n".join(K)


def export_dtcg(files, meta):
    """(1) one self-contained resolver with inline sources; (2) flat per-theme files for Figma's native
    DTCG import (one mode per file, sRGB colors, px dimensions, seconds; L07 A7)."""
    res = copy.deepcopy(files["opendesigner.resolver.json"])

    def inline(srcs):
        return [copy.deepcopy(files[s["$ref"]]) for s in srcs]
    for s in res["sets"].values():
        s["sources"] = inline(s["sources"])
    for m in res.get("modifiers", {}).values():
        for c in m["contexts"]:
            m["contexts"][c] = inline(m["contexts"][c])
    flats = {}
    mods = files["opendesigner.resolver.json"].get("modifiers", {})

    def import_tree(flat, paths):
        tree = {}
        for p in paths:
            t = flat[p]
            typ, v = t["type"], t["resolved"]
            if typ == "color":
                hx = hex_of(v)
                val = {"colorSpace": "srgb", "components": [rnd(c / 255, 4) for c in hex_to_rgb8(hx)], "hex": hx}
                if v.get("alpha") is not None:
                    val["alpha"] = v["alpha"]
            elif typ == "dimension":
                val = {"value": _px(v), "unit": "px"}
            elif typ == "duration":
                val = {"value": rnd(v["value"] / 1000 if v["unit"] == "ms" else v["value"], 4), "unit": "s"}
            elif typ == "fontFamily":
                val = v[0] if isinstance(v, list) else v
            elif typ in ("number", "fontWeight"):
                val, typ = v, "number"
            elif typ == "transition" and p.startswith("motion.transition."):
                sp = spring_ext(t, flat)
                ms_ = sp["css"]["durationMs"] if sp else (v["duration"]["value"] if v["duration"]["unit"] == "ms" else v["duration"]["value"] * 1000)
                p, typ, val = p + ".duration", "duration", {"value": rnd(ms_ / 1000, 4), "unit": "s"}
            else:
                continue  # composites (typography, shadow) become Figma styles, listed in variables.json
            node = tree
            parts = p.split(".")
            for q in parts[:-1]:
                node = node.setdefault(q, {})
            node[parts[-1]] = {"$type": typ, "$value": val}
        return tree
    flat0 = resolve_all(files, {})
    flats["Primitives.Value"] = import_tree(flat0, token_paths_in(files, ["primitives.tokens.json"]))
    flats["Tokens.Value"] = import_tree(flat0, token_paths_in(files, ["semantic.tokens.json"]))
    groups = [("Color", "theme"), ("Density", "density"), ("Motion", "motion")]
    for coll, mod in groups:
        if mod in mods:
            for c, srcs in mods[mod]["contexts"].items():
                fl = resolve_all(files, {mod: c})
                flats[f"{coll}.{c.title()}"] = import_tree(fl, token_paths_in(files, [x["$ref"] for x in srcs]))
        elif coll == "Color":
            srcs = files["opendesigner.resolver.json"]["sets"]["theme"]["sources"]
            flats[f"Color.{meta['modes'][0].title()}"] = import_tree(flat0, token_paths_in(files, [x["$ref"] for x in srcs]))
    return res, flats


def cmd_export(d, fmt, files=None, meta=None, quiet=False):
    state = merge_defaults(load_state(d))
    if files is None:
        files, meta, _ = generate_system(load_state(d))
    prefix = slug(meta.get("prefix") or state["exports"].get("prefix") or "ds").replace("-", "")
    formats = ["css", "tailwind", "figma", "paper", "swift", "compose", "dtcg"] if fmt == "all" else [fmt]
    written = []
    for f in formats:
        if f == "css":
            p = os.path.join(d, "build", "css", "tokens.css")
            write_text(p, export_css(files, meta, prefix))
        elif f == "tailwind":
            p = os.path.join(d, "build", "tailwind", "theme.css")
            write_text(p, export_tailwind(files, meta, prefix, reset=(state.get("exports") or {}).get("tailwindReset", True) is not False))
        elif f == "figma":
            p = os.path.join(d, "build", "figma", "variables.json")
            dump_json(p, export_figma(files, meta, state, prefix), compact=True)
            _bundle, flats = export_dtcg(files, meta)
            for theme, tree in flats.items():  # Figma native import: one DTCG file per collection and mode (spec 7.6)
                dump_json(os.path.join(d, "build", "figma", "import", f"{theme}.tokens.json"), tree, compact=True)
        elif f == "paper":
            payload, css = export_paper(files, meta, prefix)
            p = os.path.join(d, "build", "paper", "tokens.json")
            dump_json(p, payload, compact=True)
            for theme, text in css.items():
                write_text(os.path.join(d, "build", "paper", f"tokens.{theme}.css"), text)
        elif f == "swift":
            p = os.path.join(d, "build", "swift", "DesignTokens.swift")
            write_text(p, export_swift(files, meta, prefix))
        elif f == "compose":
            p = os.path.join(d, "build", "compose", "DesignTokens.kt")
            write_text(p, export_compose(files, meta, prefix))
        elif f == "dtcg":
            bundle, _flats = export_dtcg(files, meta)
            p = os.path.join(d, "build", "dtcg", f"{slug(meta.get('name') or 'design-system')}.resolver.json")
            dump_json(p, bundle, compact=True)
        else:
            raise SystemExit(f"unknown format {f}; use css, tailwind, figma, paper, swift, compose, dtcg or all")
        written.append(p)
    if not quiet:
        for p in written:
            print(f"wrote {p}")
    return written


# =============================================================================================
# DESIGN.md and PRODUCT.md (spec 7.2, 7.3)
# =============================================================================================

DESIGN_SECTIONS = ["Overview", "Colors", "Typography", "Layout", "Elevation & Depth", "Shapes", "Components", "Do's and Don'ts",
                   "Motion", "Modes and Themes", "Iconography and Imagery", "Content and Voice", "Accessibility",
                   "Platforms and Devices", "Decisions", "Open Items", "For Agents"]
PRODUCT_SECTIONS = ["Product", "Audience", "Surfaces", "Memorable Thing", "Principles", "Constraints", "Scope", "Team and Governance"]
SECTION_PATHS = {  # which decisions each DESIGN.md section rests on
    "Overview": r"^(dials\.(expression|brandPresence|density)|preset|macros|answers\.Q-(aud|brand|dir|scope)-)",
    "Colors": r"^(dials\.(colorfulness|warmth)|raw\.(brandColor|primaryActionColor|focusColor|neutralBase|secondaryColors|contrastTarget|flags)|answers\.Q-(color|theme)-)",
    "Typography": r"^(raw\.(textFace|displayFace|monoFace|baseSize|scripts|marketingSurfaces)|overrides\.type|answers\.Q-type-)",
    "Layout": r"^(dials\.density|raw\.(spaceUnit|inputs|minTarget)|answers\.Q-(space|layout)-)",
    "Elevation & Depth": r"^(dials\.depth|answers\.Q-depth-)",
    "Shapes": r"^(dials\.roundness|overrides\.radius|answers\.Q-shape-)",
    "Components": r"^(components|answers\.Q-(comp|state|form|pattern)-)",
    "Motion": r"^(dials\.energy|raw\.flags\.motionOff|answers\.Q-motion-)",
    "Modes and Themes": r"^(raw\.(defaultTheme|flags\.darkMode)|answers\.Q-(theme|token)-)",
    "Iconography and Imagery": r"^(hooks\.H-(logo|appicon|favicon|icons|illus|photo|motif)|answers\.Q-(icon|img|viz)-)",
    "Content and Voice": r"^(hooks\.H-voice|answers\.Q-voice-)",
    "Platforms and Devices": r"^(raw\.(platforms|inputs)|answers\.Q-plat-)",
    "Accessibility": r"^(raw\.(contrastTarget|minTarget|focusWidth)|answers\.Q-(color-2[2-4]|aud-0[2-4]))",
}
# Zoom (BRIEF req. 14-15): every area starts as a sketch from the Level 0 answers and can be zoomed in step by step.
ZOOM_LEVELS = ["sketch", "broad", "defined", "detailed"]
ZOOM_AREAS = [("overview", "Overview"), ("color", "Colors"), ("typography", "Typography"), ("layout", "Layout"),
              ("elevation", "Elevation & Depth"), ("shape", "Shapes"), ("components", "Components"), ("motion", "Motion"),
              ("modes", "Modes and Themes"), ("iconography", "Iconography and Imagery"), ("content", "Content and Voice"),
              ("accessibility", "Accessibility"), ("platforms", "Platforms and Devices")]
ZOOM_NEXT = {"overview": ["Q-brand-01", "Q-dir-01"], "color": ["Q-color-01", "Q-color-02", "Q-color-20"], "typography": ["Q-type-01", "Q-type-08"],
             "layout": ["Q-space-01", "Q-layout-01"], "elevation": ["Q-depth-01"], "shape": ["Q-shape-01"],
             "components": ["Q-comp-01", "Q-state-01"], "motion": ["Q-motion-01", "Q-motion-02"], "modes": ["Q-theme-01", "Q-theme-02"],
             "iconography": ["Q-icon-01", "Q-img-01"], "content": ["Q-voice-01"], "accessibility": ["Q-color-24", "Q-aud-02"],
             "platforms": ["Q-plat-01", "Q-plat-05"]}


def _md_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c).replace("|", "\\|").replace("\n", " ") for c in r) + " |")
    return "\n".join(out)


def _decisions(d):
    """Latest decision per path from decisions.md: path -> {id, value, set_by, reason, locked}."""
    fp = os.path.join(d, "decisions.md")
    out = {}
    if not os.path.exists(fp):
        return out
    with open(fp, encoding="utf-8") as f:
        text = f.read()
    for m in re.finditer(r"^## (D-\d+) · (.*?)\n- set_by: (\S+) · locked: (\S+).*?\n- reason: (.*?)\n", text, flags=re.M):
        did, head, set_by, locked, reason = m.groups()
        path, _, val = head.partition(" = ")
        if not val:
            continue
        out[path.strip()] = {"id": did, "value": val.strip(), "set_by": set_by, "locked": locked == "yes", "reason": reason.strip()}
    return out


def _keep_blocks(text):
    """od:keep blocks by section heading, so hand-written prose survives regeneration (spec 7.2)."""
    keeps = {}
    if not text:
        return keeps
    for sec in re.split(r"^## ", text, flags=re.M)[1:]:
        title = sec.split("\n", 1)[0].strip()
        m = re.search(r"<!-- od:keep -->.*?<!-- /od:keep -->", sec, flags=re.S)
        if m:
            keeps[title] = m.group(0)
    return keeps


def _direction_words(state):
    pid, is_default = effective_preset(state)
    if not pid:
        return "no named preset"
    return f"preset {pid}" + (" (the default until Q-dir-01 is answered)" if is_default else "")


def dial_words(dial, v, params, ci=None):
    L = {d["id"]: d for d in levers()["dials"]}[dial]
    side = (L["left"] if v <= 33 else f"leaning {L['left']}" if v < 45 else "balanced" if v <= 55
            else f"leaning {L['right']}" if v < 67 else L["right"])
    pretty = re.sub(r"(?<=[a-z])([A-Z])", lambda m_: " " + m_.group(1).lower(), dial)
    head = f"**{pretty[0].upper() + pretty[1:]} {v}/100** ({L['left']} to {L['right']}: {side})"
    say = {
        "expression": f"type ratio {params['type.ratio']}, hero moments: {params['emphasis.heroMoments']}, expressive motion: "
                      f"{params['motion.expressiveScope']}, brand color role: {params['color.brandRole']}, containment: {params['layout.containment']}",
        "brandPresence": f"typeface suggestion: {params['type.faceSuggestion']}, brand color placement: {params['color.brandPlacement']}, "
                         f"native component share about {int(round(params['components.nativeShare'] * 100))}%, voice guidance: {params['content.voiceGuidance']}",
        "density": f"body {params['type.baseSize.web']}px on the web, default control {params['control.height.md']}px, density mode "
                   f"{params['space.densityMode']}, icons {params['icon.defaultSize']}px; hit areas never shrink",
        "energy": f"standard easing {params['motion.easing.standard']}, duration multiplier {rnd(params['motion.durationMultiplier'], 2)}, "
                  f"spring damping {rnd(params['motion.spring.spatial.dampingRatio'], 2)}, heading weight {params['type.headingWeight']}, "
                  f"navigation: {params['chrome.navTreatment']}",
        "roundness": f"control radius {params['radius.control']}, icon corners {params['icon.cornerStyle']}, caps {params['icon.caps']}",
        "depth": f"depth model: {params['elevation.model']}",
        "colorfulness": f"scheme {params['color.schemeVariant']}, accent chroma {rnd((ci or {}).get('peakHct', params['color.accentChroma.hct']), 1)} (HCT), "
                        f"{(ci or {}).get('accentCount', params['color.accentCount'])} accent(s), surfaces: {params['color.surfaces']}",
        "warmth": f"neutral tint chroma {rnd(params['color.neutral.tint.oklch'].get('c') or 0, 3)} at hue {params['color.neutral.tint.oklch'].get('h')}, "
                  f"borders: {params['border.softness']}, {params['content.capitalization']}, contractions {params['content.contractions']}",
    }[dial]
    return f"{head}: {say}."


def _hex_pair(light, dark, path):
    lv = hex_of(light[path]["resolved"]) if path in light else "-"
    dv = hex_of(dark[path]["resolved"]) if dark and path in dark else "same"
    la = (light[path]["resolved"] or {}).get("alpha") if path in light and isinstance(light[path]["resolved"], dict) else None
    if la is not None:
        lv += f" @{la}"
    return f"`{lv}`", f"`{dv}`"



MODE_PLAIN = {"Persuade": "a page that shows off and invites people in", "Operate": "screens where people get work done",
              "Read": "pages people read", "Experience": "something people explore and enjoy"}


def answered_label(state, qid):
    rec = (state.get("answers") or {}).get(qid)
    if rec is None:
        return None
    return answer_words(qid, answer_value(rec))


def product_words(state):
    ctx = state.get("context") or {}
    return ctx.get("product") or state.get("summary") or answered_label(state, "Q-scope-01") or ""


def audience_words(state):
    """context.audience, else the Q-aud-01 answer in plain words (U5 F24: never 'not recorded' once answered)."""
    ctx = state.get("context") or {}
    if ctx.get("audience"):
        return ctx["audience"]
    rec = (state.get("answers") or {}).get("Q-aud-01")
    if rec is None:
        return ""
    v = answer_value(rec)
    return AUDIENCE_WORDS.get(v) or answer_words("Q-aud-01", v)


def surface_words(state):
    surf = (state.get("context") or {}).get("surfaces") or []
    if surf:
        return "; ".join(f"{s.get('name')} ({MODE_PLAIN.get(s.get('mode'), s.get('mode'))})" if isinstance(s, dict) else str(s) for s in surf)
    rec = (state.get("answers") or {}).get("Q-scope-06")
    if rec is None:
        return ""
    items = surface_list(answer_value(rec))
    return "; ".join(MODE_PLAIN.get(x["mode"], x["mode"]) for x in items)


def feel_phrase(state, dials):
    ids = [m if isinstance(m, str) else m.get("id") for m in state.get("macros") or []]
    ids = [x for x in ids if x]
    if ids:
        return ", ".join(ids[:-1]) + (" and " if len(ids) > 1 else "") + ids[-1]
    return "calm" if dials["expression"] <= 33 else "balanced" if dials["expression"] <= 66 else "lively"


def licence_risks(state, meta):
    """Licence risks to show the person (U5): fonts outside their licence scope, and the terms of the asset paths
    chosen through the hooks (open libraries, tools, commissioned work), from references/hooks.json."""
    out = []
    raw = state.get("raw") or {}
    apps = set(raw.get("platforms") or []) & {"ios", "android", "desktop", "macos", "windows", "ipados"}
    for role, f in ((meta.get("type") or {}).get("faces") or {}).items():
        if not f or f.get("open") or f.get("face") in (None, "=textFace"):
            continue
        if f.get("note"):
            out.append(f["note"] + ".")
        elif apps and f.get("app") is None:
            out.append(f"{f['face']}: the app licence is not recorded, so the {', '.join(sorted(apps))} files use the system font until it is.")
        if f.get("web") is None:
            out.append(f"{f['face']}: confirm the web licence (record it with engine.py set raw.fontLicence).")
        if f.get("selfHost") is False:
            out.append(f"{f['face']}: load it from the licensed font service; the licence does not allow self-hosting.")
    data = {}
    path = os.path.join(REFERENCES, "hooks.json")
    if os.path.exists(path):
        try:
            data = {h["id"]: h for h in read_json(path).get("hooks", [])}
        except (ValueError, KeyError):
            data = {}
    for hid, rec in (state.get("hooks") or {}).items():
        st = (rec or {}).get("status")
        name = hook_label(hid, rec)
        if st == "commissioning":
            out.append(f"{name[:1].upper() + name[1:]}: get a written copyright assignment from the designer before you use it.")
        elif st in ("open-library", "tool") and hid != "H-type":
            text = (data.get(hid) or {}).get("if_no", "")
            sents = [x for x in re.split(r"(?<=[.;])\s+(?=[A-Z(])", text)
                     if re.search(r"licen|credit|attribut|terms|trademark|resale|AI train|copyright|royalt", x, re.I)
                     and not x.lower().startswith("commission")]
            if sents:
                out.append(f"{name[:1].upper() + name[1:]}: check the terms of the set you use. {sents[0].strip()[:220]}")
    return out


def face_licence_words(faces, raw):
    parts = []
    for role, f in faces.items():
        if not f or f.get("face") in (None, "=textFace"):
            continue
        name = {"=serif": "the system serif", "=rounded": "the system rounded font"}.get(f["face"], f["face"])
        if f.get("open"):
            parts.append(f"{role}: {name} (open licence or system font: web, apps and self-hosting)")
            continue
        yes = [k for k in ("web", "app", "selfHost") if f.get(k) is True]
        no = [k for k in ("web", "app", "selfHost") if f.get(k) is False]
        unk = [k for k in ("web", "app", "selfHost") if f.get(k) is None]
        words = {"web": "web", "app": "apps", "selfHost": "self-hosting"}
        parts.append(f"{role}: {name}: licensed for {', '.join(words[k] for k in yes) or 'nothing recorded'}"
                     + (f"; not for {', '.join(words[k] for k in no)} (the system font is used there)" if no else "")
                     + (f"; not recorded for {', '.join(words[k] for k in unk)}" if unk else ""))
    return "; ".join(parts) + "." if parts else "system fonts only."


def render_summary(d, state, meta, zoom):
    """The first screen of DESIGN.md (U5 F26): what this is, for whom, where, how it feels, the brand color, what is
    decided and what is next, in plain words and at most about 15 lines."""
    name = state.get("name") or "This design system"
    ans = state.get("answers") or {}
    by = {}
    for rec in ans.values():
        sb = rec.get("set_by", "chosen") if isinstance(rec, dict) else "chosen"
        by[sb] = by.get(sb, 0) + 1
    for path, (_q, _h) in ANSWER_PATHS.items():
        if get_path(state, path) not in (None, "", [], {}, "pending") and _q not in ans:
            by["chosen"] = by.get("chosen", 0) + 1
    mine = by.get("chosen", 0) + by.get("confirmed_default", 0) + by.get("reference", 0) + by.get("asset", 0)
    picked = by.get("delegated", 0) + by.get("assumed", 0)
    sketchy = [t for k, t in ZOOM_AREAS if k != "overview" and zoom[k]["level"] == "sketch"]
    feel_own = (state.get("taste") or {}).get("feelWords") or []
    macros = [m if isinstance(m, str) else m.get("id") for m in state.get("macros") or []]
    feel = ", ".join(feel_own) + (f" ({', '.join(macros)})" if macros and [w.lower().strip('!.') for w in feel_own] != macros else "") \
        if feel_own else ", ".join(macros)
    risks = licence_risks(state, meta)
    what = product_words(state)
    if what and what.lower().startswith(name.lower()):
        what = what[len(name):].lstrip(" ,:;-") or what
    if what and re.match(r"^(a|an|the)\s", what, re.I):
        head = f"**{name}** is {what[:1].lower() + what[1:]}"
    elif what:
        head = f"**{name}**: {what}"
    else:
        head = f"**{name}** is a design system; what it is for is not recorded yet (Q-scope-01)"
    lines = [head.rstrip(".") + ".", ""]
    rows = [("For", audience_words(state) or "not asked yet"),
            ("Screens", surface_words(state) or "not asked yet"),
            ("Runs on", ", ".join(state.get("raw", {}).get("platforms") or ["web"])),
            ("Feel", feel or "not asked yet"),
            ("Brand color", brand_line(meta, state) or "none yet: a stand-in blue is used"),
            ("Decided", f"{mine} answer{'s' if mine != 1 else ''} you gave" + (f", {picked} picked for you" if picked else "")
             + "; everything else uses sourced defaults"),
            ("Next", (f"zoom into {', '.join(sketchy[:3])}, or stop here: each level works" if sketchy
                      else "every area is past the sketch; zoom deeper where it matters, or stop here")),
            ("Licence risks", " ".join(risks[:2]) + (f" (+{len(risks) - 2} more in Open Items)" if len(risks) > 2 else "") if risks else "none found")]
    lines += [f"- **{k}:** {v}" for k, v in rows]
    return "\n".join(lines)


def colors_lead(meta, state, light):
    ci = meta["color"]
    brand = (state.get("raw") or {}).get("brandColor")
    extra = [x for x in ("accent2", "accent3") if x in ci.get("ramps", [])]
    if ci.get("scheme") == "monochrome" and "action" not in ci.get("ramps", []):
        return "**Buttons use near-black ink; color is kept for status, links and focus.** Everything else stays neutral."
    if brand:
        how = "exactly" if ci.get("pinnedStep") else "as a readable shade"
        first = f"your brand color `{brand}` ({how}) marks buttons, links and focus"
    else:
        first = "a stand-in blue marks buttons, links and focus (no brand color yet)"
    if extra:
        others = [hex_of(light[f"color.bg.{x}.bold"]["resolved"]) for x in extra if f"color.bg.{x}.bold" in light]
        word = {2: "Two", 3: "Three"}.get(1 + len(extra), str(1 + len(extra)))
        return f"**{word} accent colors: {first}; `{'`, `'.join(others)}` add{'s' if len(others) == 1 else ''} highlights.** Everything else stays neutral."
    return f"**One accent color: {first}.** Everything else stays neutral."


def tailwind_classes(files):
    """Tailwind v4 class names generated by build/tailwind/theme.css, grouped for DESIGN.md (U5 F14)."""
    flat = resolve_all(files, {})
    has = lambda p: p in flat
    out = {"color": [], "layout": [], "shape": [], "elevation": [], "type": [], "motion": []}
    for p, c in (("color.bg.action.primary", "bg-action-primary"), ("color.bg.action.primary-hover", "hover:bg-action-primary-hover"),
                 ("color.bg.action.primary-pressed", "active:bg-action-primary-pressed"), ("color.text.on-action", "text-on-action"),
                 ("color.surface.base", "bg-surface-base"), ("color.surface.raised", "bg-surface-raised"), ("color.text.primary", "text-fg-primary"),
                 ("color.text.secondary", "text-fg-secondary"), ("color.text.link", "text-fg-link"), ("color.border.subtle", "border-line-subtle"),
                 ("color.border.input", "border-line-input"), ("color.border.focus", "outline-line-focus"), ("color.bg.danger.bold", "bg-danger-bold")):
        if has(p):
            out["color"].append(c)
    for p, c in (("space.inset.md", "p-inset-md"), ("space.stack.md", "gap-stack-md"), ("space.inline.sm", "gap-inline-sm"),
                 ("size.control.md", "h-control-md"), ("size.icon.md", "size-icon-md"), ("size.target.min", "min-h-target-min")):
        if has(p):
            out["layout"].append(c)
    out["shape"] = ["rounded-control", "rounded-container", "rounded-overlay", "rounded-full"]
    out["elevation"] = ["shadow-raised", "shadow-floating", "shadow-overlay"]
    out["type"] = [f"text-{'-'.join(p.split('.')[1:])}" for p in ("text.body.md", "text.label.lg", "text.title.md", "text.headline.md") if has(p)]
    out["motion"] = ["transition-feedback", "ease-standard"]
    return out


def render_design_md(d, files, meta, state, existing=""):
    res = files["opendesigner.resolver.json"]
    mods = res.get("modifiers", {})
    has_dark = "theme" in mods and "dark" in mods["theme"]["contexts"]
    light = resolve_all(files, {"theme": "light"} if "theme" in mods else {})
    dark = resolve_all(files, {"theme": "dark"}) if has_dark else None
    params = {k: v["value"] for k, v in meta["params"].items()}
    dials = meta["dials"]
    decs = _decisions(d)
    keeps = _keep_blocks(existing)
    raw = state["raw"]
    ctx = state.get("context") or {}
    prefix = meta.get("prefix", "ds")
    tinfo, sinfo, shp, mot, el = meta["type"], meta["space"], meta["shape"], meta["motion"], meta["elevation"]
    H = lambda p: hex_of(light[p]["resolved"])

    def dec_ids(sec):
        rx = SECTION_PATHS.get(sec)
        if not rx:
            return ""
        ids = [f"{v['id']} ({k})" for k, v in decs.items() if re.match(rx, k)]
        return "Decisions: " + (", ".join(ids) if ids else "none recorded yet; values are defaults from references/levers.json") + "."

    zoom = zoom_levels(d, state)
    ztitle = {t: k for k, t in ZOOM_AREAS}
    by_area = {}
    for qid, rec in sorted((state.get("answers") or {}).items()):
        by_area.setdefault((questions().get(qid) or {}).get("area") or "overview", []).append((qid, rec))

    def answers_block(area):
        """Every answer in the area in plain words, with how it was set and what it shapes (U5: answers are never silent)."""
        items = by_area.get(area) or []
        if not items:
            return ""
        shapes = {"rule": "a rule here", "owner": "owner input", "hook": "asset status", "export": "exports", "reference": "reference"}
        rows = []
        for qid, rec in items:
            q = questions().get(qid) or {}
            ask = re.split(r"(?<=[?.])\s", q.get("ask") or qid)[0]
            if len(ask) > 100:
                ask = ask[:100].rsplit(" ", 1)[0] + "..."
            kind = shapes.get(ANSWER_RECORDS.get(qid)) or "tokens"
            rows.append(f"- {ask} **{answer_words(qid, answer_value(rec))}** ({rec.get('set_by', 'chosen') if isinstance(rec, dict) else 'chosen'}; "
                        f"{kind}; {qid})")
        return "**Your answers here** (each one either sets tokens or is a rule for this section):\n" + "\n".join(rows)

    def section(title, body, lead=None, term_key=None, fold=True):
        """Three-voice layout (synthesis/THREE-VOICES.md, assets/output/DESIGN.md): zoom line, one plain sentence,
        the one-line 'Designers · Code' note, then the full designer and engineer detail folded under 'More'."""
        parts = [f"## {title}", ""]
        zk = ztitle.get(title)
        if zk:
            z = zoom[zk]
            nxt = f" To zoom in, answer {', '.join(z['next'])}." if z["level"] != "detailed" and z["next"] else ""
            li = ZOOM_LEVELS.index(z["level"])
            parts += [f"> Zoom: {z['level']} ({li} of 3), {z['decisions']} decision{'s' if z['decisions'] != 1 else ''} in this area.{nxt}",
                      f"<!-- od:zoom area={zk} level={li} -->", ""]
        if lead:
            sl = short_line(term_key) if term_key else ""
            parts += [lead + ("\n" + sl if sl else ""), ""]
        detail = [answers_block(zk or ("delivery" if title == "For Agents" else None)), body.strip(), ""]
        detail = [x for x in detail[:1] if x] + ([""] if detail[0] else []) + detail[1:]
        di = dec_ids(title)
        if di:
            detail += [di, ""]
        parts += (["<details><summary>More</summary>", ""] + detail + ["</details>", ""]) if fold and lead else detail
        if title in keeps:
            parts += [keeps[title], ""]
        return "\n".join(parts)

    # ---- front matter: Google DESIGN.md keys, kept as short as the template (assets/output/DESIGN.md); tokens/ has the rest
    styles = sorted(p for p, t in light.items() if t["type"] == "typography")
    bm = light["text.body.md"]["resolved"]
    bext = (light["text.body.md"].get("$extensions") or {}).get(NS, {})
    bfam = bm["fontFamily"][0] if isinstance(bm["fontFamily"], list) else bm["fontFamily"]
    fm = ["---", "version: alpha", f"name: {json.dumps(state.get('name') or 'Design system')}",
          f"description: {json.dumps(product_words(state) or 'Design system generated by OpenDesigner', ensure_ascii=False)}", "colors:"]
    for k, p in (("primary", "color.bg.action.primary"), ("on-primary", "color.text.on-action"), ("surface", "color.surface.base"),
                 ("on-surface", "color.text.primary"), ("error", "color.bg.danger.bold")):
        if p in light:
            fm.append(f'  {k}: "{H(p)}"')
    fm += ["typography:",
           f"  body-md: {{ fontFamily: {json.dumps(bfam)}, fontSize: {fmt_num(_px(bm['fontSize']))}px, lineHeight: {bext.get('lineHeightPx')}px }}",
           "rounded:", f"  control: {fmt_num(_px(light['radius.control']['resolved']))}px",
           f"  container: {fmt_num(_px(light['radius.container']['resolved']))}px",
           "spacing:", f"  unit: {sinfo['unit']}px", "---", ""]
    dflt = meta["density"][params["space.densityMode"]]
    ctl = dflt["control"]
    ci = meta["color"]
    brand = raw.get("brandColor")
    out = ["\n".join(fm), f"# {state.get('name') or 'Design system'}", "", render_summary(d, state, meta, zoom), "",
           f"> Generated by the OpenDesigner engine {ENGINE_VERSION} from `state.json` and `decisions.md`; `tokens/` is the source of truth. "
           "Change the system with `engine.py set ...` and `engine.py build`, not by editing this file (notes inside "
           "`<!-- od:keep -->` blocks survive). Each section opens with one plain sentence; open **More** for the designer and engineer detail.", ""]

    # 1 Overview
    principles = state.get("principles") or []
    pl = "\n".join(f"{i}. {p}" for i, p in enumerate(principles, 1)) if principles else \
        "No principles recorded yet (Q-brand-07). Until they are, the dials act as the tie-breakers below."
    surf = ctx.get("surfaces") or []
    surf_txt = "; ".join((s.get('name', '') + ' (' + s.get('mode', '') + ((': ' + surface_rule(s, params['space.densityMode'])) if surface_rule(s, '') else '') + ')')
                         if isinstance(s, dict) else str(s) for s in surf) or surface_words(state) or "not recorded yet (Q-scope-06)"
    body = [f"**Intent.** {product_words(state) or 'A design system generated from eight dials and a few raw inputs.'}",
            "", f"- Audience: {audience_words(state) or 'not recorded yet (Q-aud-01)'}",
            f"- The memorable thing: {ctx.get('memorable') or answered_label(state, 'Q-brand-02') or 'not recorded yet (Q-brand-02)'}",
            f"- Surfaces: {surf_txt}",
            f"- Platforms: {', '.join(raw.get('platforms') or [])}; inputs: {', '.join(raw.get('inputs') or [])}",
            f"- Direction: {_direction_words(state)}"
            + (f"; feel {', '.join((m if isinstance(m, str) else m['id'] + ' x' + str(m.get('strength', 1))) for m in state['macros'])}" if state.get("macros") else "")
            + (f" (your words: {', '.join((state.get('taste') or {}).get('feelWords') or [])})" if (state.get("taste") or {}).get("feelWords") else ""),
            "", "**Principles (ranked).**", pl, "", "**Dial positions.** Three posture dials set the overall stance. Five character dials fine-tune it.", ""]
    body += [f"- {dial_words(k, dials[k], params, ci)}" for k in DIALS]
    body += ["", "**Zoom by area** (sketch, broad, defined, detailed). You can stop at any level; each one works.", "",
             _md_table(["Area", "Zoom", "Next questions"], [(t, zoom[k]["level"], ", ".join(zoom[k]["next"]) if zoom[k]["next"] else "-")
                                                           for k, t in ZOOM_AREAS if k != "overview"])]
    body += ["", "The tokens in `tokens/` (DTCG 2025.10 with `opendesigner.resolver.json`) are the source of truth. This file is a generated view."]
    dw = "roomy" if dials["density"] <= 33 else "comfortable" if dials["density"] <= 66 else "compact"
    style = {"flat2": "a flat", "tonal": "a tonal", "glass": "a glass", "neobrutal": "a bold, blocky", "soft": "a soft 3D",
             "maximal": "a loud, busy"}.get(effective_preset(state)[0] or "", "its own")
    lead_overview = f"**{state.get('name') or 'This system'} feels {feel_phrase(state, dials)}. Screens are {dw}, in {style} style.**"
    out.append(section("Overview", "\n".join(body), lead=lead_overview, term_key="Visual style direction"))

    # 2 Colors
    rows = []
    for p in sorted(light):
        if light[p]["type"] == "color" and re.match(r"color\.(surface|text|bg|border|icon|overlay|chart|workflow)\.", p):
            lv, dv = _hex_pair(light, dark, p)
            rows.append((f"`{p}`", lv, dv, light[p]["$description"]))
    nl = [luminance(hx) for hx in meta["ramps"]["neutral"]["light"]["hex"]]
    step_rows = []
    for fg in (8, 9, 10, 11, 12):
        step_rows.append([f"neutral {fg}"] + [f"{contrast_y(nl[fg - 1], nl[bg - 1]):.2f}" for bg in (1, 2, 3, 4, 5)])
    ramp_rows = [(f"`{n}`", " ".join(f"`{h}`" for h in v["light"]["hex"]), v["light"]["textOnSolid"]) for n, v in meta["ramps"].items()]
    st_rows = []
    for base_ in ("color.bg.action.primary", "color.bg.accent.bold"):
        if base_ in light and base_ + ("-hover" if base_.endswith("primary") else "-hover") in light:
            hv = light[base_ + "-hover"]["resolved"]
            pr = light[base_ + "-pressed"]["resolved"]
            st_rows.append((f"`{base_}`", f"`{H(base_)}`", f"`{hex_of(hv)}` ({contrast(hex_of(hv), H(base_)):.2f}:1)",
                            f"`{hex_of(pr)}` ({contrast(hex_of(pr), H(base_)):.2f}:1)"))
    body = [f"**Intent.** {('Brand color `' + brand + '`') if brand else 'No brand color yet: the accent uses a placeholder blue hue'} "
            f"drives the accent ramp's hue; the Colorfulness dial ({dials['colorfulness']}) sets its chroma "
            f"(scheme {ci['scheme']}, peak HCT chroma {ci['peakHct']}). The brand's role is **{params['color.brandRole']}** and it sits "
            f"closest to accent step {ci.get('brandAnchorStep') or '-'}. " + (brand_line(meta, state) or ""),
            "", "**How ramps are built.** Each hue gets twelve steps in OKLCH, placed by contrast. Step 8 reaches at least 3:1 (edges and focus). "
            "Steps 10 and 11 reach the text minimum on backgrounds 1-4. Step 12 reaches at least 7:1. Steps 2-6 are spaced evenly in lightness "
            "between step 1 and step 7. Light and dark ramps are solved separately. Dark solids are lighter and carry dark text "
            f"(dark mode is a separate mapping, never an inversion). Text minimum: {ci['textMin']}:1 "
            f"({'WCAG 2.2 AAA' if ci['textMin'] > 4.5 else 'WCAG 2.2 AA'}).",
            "", _md_table(["Ramp", "Light steps 1-12", "Solid carries"], ramp_rows),
            "", "**Step-distance guarantee** (neutral, light; WCAG contrast of a foreground step on background steps 1-5):", "",
            _md_table(["Foreground", "on 1", "on 2", "on 3", "on 4", "on 5"], step_rows),
            "", f"**States.** Hover is at least {STATE_MIN['hover']}:1 from its fill and pressed at least {STATE_MIN['pressed']}:1, "
            + ("as see-through state layers of the text color (Q-color-20 overlay). " if raw.get("stateMethod") == "overlay" else "as shade steps (DC-L01-17). ")
            + "Where a color is unknown at design time, use the state opacities in `opacity.state.*`.",
            "", _md_table(["Fill", "Base", "Hover", "Pressed"], st_rows) if st_rows else "",
            "", "**Semantic roles** (use these, never the ramps):", "", _md_table(["Token", "Light", "Dark", "Use"], rows),
            "", "**Use / avoid.**", "- Use one solid accent fill per view for the primary action; spend chroma on small, meaningful elements.",
            "- Avoid gray text on colored fills; use the matching `text.on-*` role.",
            "- Avoid color as the only signal: pair status colors with an icon or label.",
            ("- Charts: use `color.chart.categorical.*` in order, `color.chart.sequential.*` for amounts, `color.chart.neutral` for other."
             if raw.get("chartPalette") not in (None, "none") else
             "- Charts: no chart palette yet (Q-color-19). Take chart colors from the status and accent hues, and check them separately.")]
    tw = tailwind_classes(files)
    if tw.get("color"):
        body += ["", "**Tailwind classes:** " + ", ".join(f"`{c}`" for c in tw["color"]) + "."]
    out.append(section("Colors", "\n".join(body), lead=colors_lead(meta, state, light), term_key="accent color"))

    # 3 Typography
    rows = []
    for p in styles:
        if p.startswith("text.emphasized."):
            continue
        v = light[p]["resolved"]
        ext = (light[p].get("$extensions") or {}).get(NS, {})
        rows.append((f"`{p}`", f"{fmt_num(_px(v['fontSize']))}/{ext.get('lineHeightPx')}", int(v["fontWeight"]),
                     f"{fmt_num(ext.get('letterSpacingEm', 0))}em" + (" caps" if ext.get("textTransform") else ""), ext.get("use", "")))
    fam = light["font.family.text"]["resolved"]
    h_type = (state.get("hooks") or {}).get("H-type", {}).get("status", "pending")
    scripts = tinfo.get("scripts") or {}
    body = [f"**Intent.** Body text is {tinfo['base']}px; sizes follow `round({tinfo['base']} x {tinfo['ratio']}^n)` for n from -2 to "
            f"{tinfo['nTop']}, reaching about {tinfo['reach']}x body ({'marketing surfaces in scope' if raw.get('marketingSurfaces') else 'product surfaces only'}). "
            f"Sizes: {', '.join(str(x) for x in tinfo['sizes'])}px" + (f" (merged as too close: {tinfo['merged']})" if tinfo["merged"] else "") + ".",
            "", f"- Text face: {', '.join(fam) if isinstance(fam, list) else fam}. Licence status (hook H-type): **{h_type}**."
            + (" A system font needs no licence; it must not be embedded in apps." if raw.get("textFace") in (None, "system") else ""),
            "- Licence by platform: " + face_licence_words(tinfo.get("faces") or {}, raw),
            "- On iOS the Swift file uses Dynamic Type text styles (body 17 pt), so text follows the person's text size setting; "
            "Compose uses sp, which follows the Android font scale.",
            f"- Weights: {', '.join(f'{k} {v}' for k, v in tinfo['weights'].items())} (two or three distinct weights per view).",
            (f"- Emphasized variants (Expression {dials['expression']}, on from 67): {len(tinfo.get('emphasized') or [])} styles under "
             "`text.emphasized.*`, the same size one weight heavier, for the selected item, key actions and headlines (DC-L02-11)."
             if tinfo.get("emphasized") else "- Emphasized variants: off (they turn on at Expression 67 and up, DC-L02-11)."),
            f"- Line heights snap to a {2 if raw.get('lineHeightGrid') == 2 else 4}px grid: 1.5 up to 17px, 1.4 to 26px, 1.25 to 44px, 1.12 above.",
            ("- Letter spacing: none beyond the font's own (Q-type-13 zero)." if raw.get("tracking") == "zero"
             else "- Letter spacing: +0.02em at 11-12px, -0.01em from 32px, -0.02em from 48px."),
            "- Text scaling: CSS sizes are rem, line heights unitless, so text scales to 200% (WCAG 1.4.4); containers must grow with it.",
            "- Scripts: " + (", ".join(f"{k}: line height x{v.get('lineHeightFactor')}" + (", tracking 0" if v.get("zeroTracking") else "")
                                      for k, v in scripts.items()) if scripts else "Latin only; add scripts in raw.scripts to get per-script line heights (DC-L02-25)."),
            "", _md_table(["Style", "Size/line (px)", "Weight", "Tracking", "Use"], rows),
            "", "**Use / avoid.**", "- Use at most three sizes and two weights in one view; let color and weight carry hierarchy before size.",
            "- Avoid all caps for sentences and in scripts without case; use weight for emphasis there."]
    if tw.get("type"):
        body += ["", "**Tailwind classes:** " + ", ".join(f"`{c}`" for c in tw["type"]) + "."]
    out.append(section("Typography", "\n".join(body), lead=f"**Body text is {tinfo['base']}px, and each larger size is about {tinfo['ratio']} times the one below.**", term_key="type scale"))

    # 4 Layout
    drows = []
    for dn, info in meta["density"].items():
        drows.append((dn + (" (default)" if dn == params["space.densityMode"] else ""),
                      " / ".join(str(info["inset"][k]) for k in ("xs", "sm", "md", "lg", "xl")),
                      " / ".join(str(info["section"][k]) for k in ("sm", "md", "lg")),
                      " / ".join(str(info["control"][k]) for k in ("sm", "md", "lg")), info["ratio"]))
    body = [f"**Intent.** Everything sits on a {sinfo['unit']}px unit: ladder {', '.join(str(x) for x in sinfo['ladder'])}. "
            f"Density is a mode on the semantic layer (default **{params['space.densityMode']}**). Primitives and minimum tap areas never change.",
            "", _md_table(["Density", "inset xs/sm/md/lg/xl", "section sm/md/lg", "control sm/md/lg", "outer:inner"], drows),
            "", "- Target sizes: " + ", ".join(f"{k} {v}px" for k, v in sinfo["targets"].items())
            + f"; `size.target.min` is the floor for the primary input, and `space.target.gap` separates adjacent targets.",
            "- Inner gaps stay below outer gaps (at least half), so grouping reads without borders (L15 P16).",
            "- Breakpoints and grid: not generated yet; use the platform defaults and keep layout spacing independent of density (DC-L03-17).",
            "", "**Use / avoid.**", "- Parents own spacing (padding and gap); children never set outer margins.",
            "- Avoid values off the ladder; if one is needed, add it as a decision."]
    out.append(section("Layout", "\n".join(body), lead=f"**Spacing comes in steps of {sinfo['unit']}px, and screens use {params['space.densityMode']} spacing by default.**", term_key="spacing scale"))

    # 5 Elevation & Depth
    rows = []
    for p in ("elevation.raised", "elevation.floating", "elevation.overlay"):
        if p in light:
            layers = light[p]["resolved"]
            layers = layers if isinstance(layers, list) else [layers]
            flat_l = []
            for lay in layers:
                flat_l += lay if isinstance(lay, list) else [lay]
            txt = ", ".join(f"{fmt_num(_px(l['offsetX']))} {fmt_num(_px(l['offsetY']))} {fmt_num(_px(l['blur']))} {fmt_num(_px(l['spread']))}"
                            for l in flat_l if _px(l["blur"]) or _px(l["offsetY"]) or _px(l["spread"])) or "none"
            rows.append((f"`{p}`", txt, light[p]["$description"]))
    body = [f"**Intent.** Depth {dials['depth']}/100 selects the **{el['model']}** model. Shadow alpha in light mode is {el['alpha']}; dark mode "
            "doubles it and lifts surfaces by lightness instead (sunken, base, raised, overlay).",
            "", _md_table(["Token", "Layers (x y blur spread)", "Use"], rows),
            "", "- Borders: 1px default, 2px selected and focus, 4px emphasis; width changes use an inset shadow so layout does not jump.",
            "- Stacking: page < raised < floating (menus) < overlay (dialogs with `color.overlay.scrim`).",
            "- " + ("Glass is for controls and navigation only, with `color.surface.glass-fallback` under Reduce Transparency." if el["model"] == "materials"
                    else "No materials or glass in this system.")]
    lead_depth = {"borders": "**Surfaces are separated by thin borders, with no shadows.**",
                  "ring+faint-shadow": "**Cards get a faint outline and a very soft shadow.**",
                  "tonal": "**Surfaces step in lightness; only menus and dialogs cast shadows.**",
                  "shadow-ladder": "**Raised things cast soft shadows that grow with height.**",
                  "materials": "**Controls and bars can be see-through glass, with solid fallbacks.**"}.get(el["model"], "")
    out.append(section("Elevation & Depth", "\n".join(body), lead=lead_depth, term_key="Depth model"))

    # 6 Shapes
    body = [f"**Intent.** Roundness {dials['roundness']}/100 gives controls a **{shp['control']}** radius; details {shp['detail']}px, containers "
            f"{shp['container']}px, overlays {shp['overlay']}px, people full. Controls under 32px tall use `radius.control-sm` ({shp['control-sm'] if shp['control-sm'] < FULL else 'full'}).",
            "", f"- Nested radius: inner = max(outer - padding, smallest step). Here it is {shp['nested']}px inside a container with `space.inset.lg` "
            "padding. Equal radii on nested shapes look uneven (DC-L04-05).",
            f"- Focus ring: {shp['focusWidth']}px, 2px offset, radius = control radius + offset ({shp['focusRadius'] if shp['focusRadius'] < FULL else 'full'}).",
            f"- Icons: {shp['iconCorners']} corners, {shp['iconCaps']} caps. On iOS, use continuous corners (DC-L04-04).",
            "- Signature shapes: none generated; a brand shape library is a designer asset (hook H-motif)."]
    out.append(section("Shapes", "\n".join(body), lead=f"**Buttons and fields have {'fully round' if shp['control'] == 'full' else str(shp['control']) + 'px'} corners; cards have {shp['container']}px corners.**", term_key="corner radius"))

    # 7 Components
    inv = (state.get("components") or {}).get("inventory") or []
    notes = (state.get("components") or {}).get("notes") or {}
    rows = [(c, notes.get(c, "planned (tokens ready)")) for c in inv]
    ans = {k: answer_value(v) for k, v in (state.get("answers") or {}).items()}
    pol = [("Validation timing and disabled submit", "Q-form-02"), ("Field style", "Q-form-01"), ("Toasts", "Q-form-04"),
           ("Undo versus confirm", "Q-form-05"), ("Danger actions", "Q-state-06"), ("Button emphasis levels", "Q-state-01")]
    pol = [(k, answer_words(q, ans[q]) if q in ans else None) for k, q in pol]  # U5 F27: each policy reads its own question
    base_c = (state.get("components") or {}).get("base")
    base_c = (answer_words("Q-comp-01", base_c) if base_c else None) or "not chosen yet (Q-comp-01)"
    body = [f"**Intent.** v1 components use the semantic tokens only. Base: {base_c}. "
            f"Buttons are {ctl['md']}px tall ({params['space.densityMode']}), {shp['control']} radius, `text.label.lg`; one primary action per view.",
            "", _md_table(["Component", "Status"], rows) if rows else "No inventory recorded.",
            "", "**Contested policies:** " + "; ".join(f"{k}: {v if v is not None else 'pending'}" for k, v in pol) + ".",
            "", "**Use / avoid.**", "- Every interactive component shows hover, pressed, focus-visible and disabled states from the tokens.",
            f"- Inputs keep a 3:1 boundary (`color.border.input`); signifier strength: {params['signifier.minStrength']}.",
            "- Component docs belong in `opendesigner/components/<name>.md` (spec 7.8)."]
    out.append(section("Components", "\n".join(body), lead=f"**Version 1 plans {len(inv)} components, all built from these tokens.**", term_key="Component inventory scope"))

    # 8 Do's and Don'ts
    vr = Report()
    validate_files(files, state, vr)
    warns = [i for i in vr.items if i["severity"] in ("error", "warn")]
    body = ["**Enforced by construction.** The generator cannot break these:",
            f"- text contrast {ci['textMin']}:1, and 3:1 for edges, in every mode",
            "- text on colored fills picked automatically",
            "- tap areas " + ", ".join(f"{k} {v}px" for k, v in sinfo["targets"].items()),
            "- a 2px focus ring with a 2px offset",
            "- a reduced-motion mode",
            "- inner spacing smaller than outer spacing, three text colors, and nested radii",
            "", "**Do**", "- Use semantic tokens; never raw hex, px or ms values in components.",
            "- Keep one primary action per view and at most three type sizes per view.",
            "- Pair every status color with an icon or label; underline links in running text.",
            "", "**Don't**", "- Don't shrink hit areas in dense layouts; shrink visuals and extend the hit area.",
            "- Don't use motion as the only signal, or flash more than three times a second.",
            "- Don't copy another brand's identity from a reference (colors, typeface, logo, imagery, copy).",
            "", "**Current validation findings:** " + (", ".join(f"{i['severity']}: {i['message']}" for i in warns) if warns else "none (errors 0, warnings 0)."),
            "", "**Waivers:** " + ("; ".join(f"{k}: {v}" for k, v in (state.get("waivers") or {}).items()) or "none.")]
    out.append(section("Do's and Don'ts", "\n".join(body), lead="**These rules keep screens clear and easy to read.** The engine checks the ones it can.", term_key="Guardrails and validation"))

    # 9 Motion
    rows = [(f"`motion.duration.{k}`", f"{v}ms") for k, v in mot["durations"].items()]
    sp = light.get("motion.spring.spatial.default")
    spx = (sp.get("$extensions") or {}).get(NS, {}) if sp else {}
    body = [f"**Intent.** Energy {dials['energy']}/100: durations x{mot['multiplier']:.2f} on medium and longer steps; standard easing "
            f"`cubic-bezier({', '.join(fmt_num(x) for x in mot['standard'])})`, enter `{mot['enter']}`, exit `{mot['exit']}`. "
            f"Spatial spring: damping {mot['spatial']['dampingRatio']}, stiffness {mot['spatial']['stiffness']} "
            f"(Apple duration {spx.get('apple', {}).get('duration')}s, bounce {spx.get('apple', {}).get('bounce')}; web `linear()` sample over "
            f"{spx.get('css', {}).get('durationMs')}ms)." + (" Motion is off (flags.motionOff): standard equals reduced." if mot.get("motionOff") else ""),
            "", _md_table(["Token", "Value"], rows),
            "", "- Exits are about 25% shorter than entrances; linear easing only for spinners and progress.",
            "- Reduced motion (`prefers-reduced-motion` or `data-motion=\"reduced\"`): travel becomes opacity, feedback stays, `motion.transition.move` is 0ms.",
            "- Springs are stored as damping and stiffness in `$extensions.opendesigner.spring` because DTCG 2025.10 has no spring type.",
            f"- Haptics: {params['haptics.intensity']} intensity where the platform has them; sound: hook H-sound is "
            f"{(state.get('hooks') or {}).get('H-sound', {}).get('status', 'pending')}."]
    out.append(section("Motion", "\n".join(body), lead=("**Motion is off: things change in place without moving.**" if mot.get("motionOff") else f"**Most movements take {mot['durations']['medium']}ms.** They turn into fades when a person asks for less motion."), term_key="Motion"))

    # 10 Modes and Themes
    rows = [(n, ", ".join(m["contexts"]), m.get("default")) for n, m in mods.items()]
    body = ["**Intent.** Modes live in the DTCG resolver (`tokens/opendesigner.resolver.json`); modifiers are orthogonal, so no two set the same token.",
            "", _md_table(["Modifier", "Contexts", "Default"], rows) if rows else "Single theme.",
            "", f"- Web: `prefers-color-scheme` with a `[data-theme]` override; `[data-density]`; `prefers-reduced-motion` with `[data-motion]` (see `build/css/tokens.css`).",
            "- High-contrast themes are not generated; set `raw.contrastTarget` to AAA for 7:1 text everywhere.",
            "- A second brand or a client re-skin may override the color primitives and `color.bg.brand`; semantic names never change."]
    out.append(section("Modes and Themes", "\n".join(body), lead=f"**The system has {'light and dark' if has_dark else 'one'} color {'modes' if has_dark else 'mode'}, three spacing densities and a reduced-motion mode.**", term_key="Modes and theming axes"))

    # 11 Iconography and Imagery
    hooks = state.get("hooks") or {}
    hs = lambda h: hooks.get(h, {}).get("status", "pending")
    st = sinfo.get("iconStroke", {})
    body = [f"**Intent.** Default icon size {sinfo['iconDefault']}px; sizes 16/20/24 pair with 14/16/20px text. Stroke follows the label weight: "
            f"{st.get(16, st.get('16'))}px at 16, {st.get(20, st.get('20'))}px at 20, {st.get(24, st.get('24'))}px at 24. Rest style: {params['icon.restStyle']}.",
            "", _md_table(["Asset", "Hook", "Status"], [("Logo and marks", "H-logo", hs("H-logo")), ("Favicon set", "H-favicon", hs("H-favicon")),
                                                       ("App icon", "H-appicon", hs("H-appicon")), ("Custom icons", "H-icons", hs("H-icons")),
                                                       ("Illustration", "H-illus", hs("H-illus")), ("Photography", "H-photo", hs("H-photo")),
                                                       ("Motifs and brand shapes", "H-motif", hs("H-motif"))]),
            "", "- Placeholders are labelled as placeholders. A generated stand-in is never shown as a finished brand asset.",
            "- Icon-only buttons need an accessible name and a hit area of `size.target.min`."]
    out.append(section("Iconography and Imagery", "\n".join(body), lead=f"**Icons are {sinfo['iconDefault']}px by default.** The logo, photos and custom icons come from a person, not from the engine.", term_key="Iconography"))

    # 12 Content and Voice
    vstat = hs("H-voice")
    body = [f"**Intent.** {'Draft: ' if vstat not in ('have',) else ''}voice guidance level **{params['content.voiceGuidance']}** "
            f"(Brand presence {dials['brandPresence']}); **{params['content.capitalization']}**; contractions **{params['content.contractions']}** "
            f"(Warmth {dials['warmth']}). Voice guide hook H-voice: {vstat}.",
            "", "- Buttons say what they do in two to four words; errors say what happened and how to fix it.",
            "- Reading level: plain language; avoid jargon in UI copy.",
            "- Word list: not recorded yet (Q-voice-03)."]
    out.append(section("Content and Voice", "\n".join(body), lead="**Words stay plain and short, and every button says what it does.**", term_key="Content and voice"))

    # 13 Accessibility
    body = [f"**Intent.** Standard: WCAG 2.2 {'AAA for text' if ci['textMin'] > 4.5 else 'AA'}. APCA is reported as advice only.",
            "", "**The system guarantees:**", "- text and edge contrast in every mode", "- visible focus (2px ring, 2px offset, 3:1)",
            "- minimum target sizes for each kind of input", "- a reduced-motion mode", "- rem-based type, so text scales to 200%",
            "- text on colored fills chosen automatically",
            "", "**Product teams own:** accessible names and labels, alt text, reading and focus order, and never using color alone. "
            "Also: clear error messages, dialogs that can be closed, no pre-checked consent boxes, and captions for media.",
            "", "**Test on each platform:**", "- keyboard only", "- a screen reader (VoiceOver, NVDA or TalkBack)", "- 200% zoom",
            "- forced colors (Windows High Contrast)", "- reduced motion", "- touch on a phone, for every surface that allows touch"]
    out.append(section("Accessibility", "\n".join(body), lead=f"**Text passes WCAG 2.2 {'AAA' if ci['textMin'] > 4.5 else 'AA'} contrast in every mode, and focus is always visible.**", term_key="Accessibility"))

    # 14 Platforms and Devices
    body = [f"**Intent.** Platforms: {', '.join(raw.get('platforms') or [])}. Inputs: {', '.join(raw.get('inputs') or [])}. "
            f"Brand presence {dials['brandPresence']}: each platform keeps its own shapes and materials: "
            f"{'yes' if params['platform.overridesShapeAndMaterial'] else 'no'}; each platform keeps its own body text size: "
            f"{'yes' if params['platform.useNativeBaseSize'] else 'no'}.",
            "", "- Navigation, back, sheets and pickers stay native on every platform (DC-L10-02).",
            "- Swift and Compose files in `build/` use the same names as the CSS variables (Figma code syntax matches them).",
            "- Fonts by platform: " + face_licence_words(tinfo.get("faces") or {}, raw)]
    out.append(section("Platforms and Devices", "\n".join(body), lead=f"**It runs on {', '.join(raw.get('platforms') or ['web'])}, and each platform keeps its own navigation.**", term_key="Target platforms"))

    # 15 Decisions
    rows = [(v["id"], f"`{k}`", v["value"], v["set_by"] + (" (locked)" if v["locked"] else ""), v["reason"])
            for k, v in sorted(decs.items(), key=lambda kv: kv[1]["id"])][-20:]
    body = ["The highest-reach decisions, newest value per path. Full log: [decisions.md](decisions.md).", "",
            _md_table(["Id", "Path", "Value", "Set by", "Reason"], rows) if rows else "No decisions recorded yet."]
    out.append(section("Decisions", "\n".join(body), lead=f"**{len(decs)} decision{'s' if len(decs) != 1 else ''} so far.** Each one says who set it and why.", term_key="decisions.md"))

    # 16 Open Items
    pend = [f"{v.get('name', h)} ({h}): {v.get('status')}" for h, v in hooks.items() if v.get("status") in ("pending", "placeholder", "commissioning")]
    assumed = [f"{k} ({v['set_by']})" for k, v in decs.items() if v["set_by"] in ("assumed", "delegated", "auto_default")]
    sketchy = [t for k, t in ZOOM_AREAS if k != "overview" and zoom[k]["level"] == "sketch"]
    body = ["- Still defaults (zoom 0, sketch): " + (", ".join(sketchy) if sketchy else "none."),
            "- Assets not final: " + ("; ".join(pend) if pend else "none."),
            "- Answers taken on assumption or delegated: " + (", ".join(assumed) if assumed else "none."),
            "- Waivers: " + ("; ".join(f"{k}: {v}" for k, v in (state.get("waivers") or {}).items()) or "none."),
            "- Licence risks: " + (" ".join(licence_risks(state, meta)) or "none found."),
            f"- Validation: {vr.count('error')} errors, {vr.count('warning')} warnings."]
    out.append(section("Open Items", "\n".join(body), lead="**These parts are still defaults, guesses, or waiting for a person.**", fold=False))

    # 17 For Agents
    body = ["1. Before any visual work, read this file, PRODUCT.md and `tokens/` (start at `tokens/opendesigner.resolver.json`).",
            f"2. Use tokens, never raw values: CSS `var(--{prefix}-...)`, Tailwind classes from `build/tailwind/theme.css`, `{prefix.upper()}.*` in Swift, "
            f"`{prefix.capitalize()}Theme` in Compose.",
            "3. Do not change a locked decision without asking the owner.",
            "4. To change the system: `engine.py set <path> <value> --why \"...\"`, then `engine.py generate`, `engine.py validate`, `engine.py design-md`.",
            "5. To extend: add a decision (never hand-edit tokens or this file). Keep semantic names the same across modes. Deprecate instead of deleting.",
            "6. After any implementation, run `engine.py review` and re-read this file."]
    if tw:
        body += ["", "**Tailwind v4 classes** (one import: `@import \"tailwindcss\"; @import \"<path>/opendesigner/build/tailwind/theme.css\";`"
                 + ("; Tailwind's default colors, text sizes, radii and shadows are switched off, so only these exist" if (state.get("exports") or {}).get("tailwindReset", True) else "")
                 + "):", "", _md_table(["Area", "Classes"], [(k.title(), ", ".join(f"`{c}`" for c in v)) for k, v in tw.items() if v])]
    out.append(section("For Agents", "\n".join(body), lead="**AI agents: read this file and the tokens before you change any screen.**", fold=False))
    return "\n".join(out).rstrip() + "\n"


def render_product_md(state, existing=""):
    ctx = state.get("context") or {}
    keeps = _keep_blocks(existing)
    raw = state["raw"]

    def sec(t, body):
        parts = [f"## {t}", "", body.strip(), ""]
        if t in keeps:
            parts += [keeps[t], ""]
        return "\n".join(parts)
    surf = ctx.get("surfaces") or []
    sc = ctx.get("scope") or {}
    out = [f"# {state.get('name') or 'Product'}: product truth", "",
           "> Generated by the OpenDesigner engine from `state.json`. It is kept apart from DESIGN.md because it changes at a different pace. "
           "Hand-written notes survive only inside `<!-- od:keep -->` blocks.", ""]
    out.append(sec("Product", product_words(state) or "Not recorded yet (Q-scope-01)."))
    aw = audience_words(state)
    out.append(sec("Audience", (aw[:1].upper() + aw[1:] + ("" if aw.endswith(".") else ".")) if aw else "Not recorded yet (Q-aud-01)."))
    out.append(sec("Surfaces", "\n".join(f"- {s.get('name')}: {s.get('mode')} mode" + (f" ({surface_rule(s, 'set by the Density dial')})" if surface_rule(s, "") else "")
                                         if isinstance(s, dict) else f"- {s}" for s in surf)
                   or surface_words(state)
                   or "Not recorded yet (Q-scope-06). Each surface gets a mode: Persuade, Operate, Read or Experience."))
    out.append(sec("Memorable Thing", ctx.get("memorable") or answered_label(state, "Q-brand-02") or "Not recorded yet (Q-brand-02)."))
    pr = state.get("principles") or []
    out.append(sec("Principles", ("\n".join(f"{i}. {p}" for i, p in enumerate(pr, 1)) + "\n\nTie-break: the higher-ranked principle wins.")
                   if pr else "Not recorded yet (Q-brand-07)."))
    cons = [f"Accessibility: WCAG 2.2 {raw.get('contrastTarget', 'AA')}", f"Platforms: {', '.join(raw.get('platforms') or [])}"]
    cons += ctx.get("constraints") or []
    out.append(sec("Constraints", "\n".join(f"- {c}" for c in cons)))
    out.append(sec("Scope", "**In:** " + (", ".join(sc.get("in") or []) or "not recorded yet") + "\n\n**Out:** " + (", ".join(sc.get("out") or []) or "not recorded yet")))
    owner = [(qid, rec) for qid, rec in sorted((state.get("answers") or {}).items())
             if ANSWER_RECORDS.get(qid) == "owner" and qid not in ("Q-brand-07", "Q-comp-01", "Q-comp-02")]
    first_sentence = lambda q: re.split(r"(?<=[?.])\s", (questions().get(q) or {}).get("ask") or q)[0]
    lines = [f"- {first_sentence(q)} **{answer_words(q, answer_value(r))}** ({q})" for q, r in owner]
    out.append(sec("Team and Governance", "\n".join(x for x in [ctx.get("team") or ""] + lines if x) or "Not recorded yet (Q-scope-03, Q-scope-04, Q-gov-01)."))
    return "\n".join(out).rstrip() + "\n"


def _sha(text):
    import hashlib
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def doc_dir(d):
    return os.path.dirname(os.path.abspath(d)) if os.path.basename(os.path.abspath(d)) == DEFAULT_DIR else d


def refresh_docs(d):
    """DESIGN.md is a living document (BRIEF req. 15): once it exists, every decision re-renders it and PRODUCT.md."""
    if os.path.exists(os.path.join(doc_dir(d), "DESIGN.md")):
        cmd_design_md(d, quiet=True)
        print("  DESIGN.md and PRODUCT.md updated (tokens update on the next `generate`)")


def cmd_design_md(d, out_dir=None, files=None, meta=None, quiet=False):
    state = merge_defaults(load_state(d))
    if files is None:
        files, meta, _ = generate_system(load_state(d))
    if out_dir is None:  # spec 7.1: project root when the state lives in ./opendesigner/, else next to the state
        out_dir = os.path.dirname(os.path.abspath(d)) if os.path.basename(os.path.abspath(d)) == DEFAULT_DIR else d
    written = []
    hashes = state.setdefault("hashes", {})
    for name, render in (("DESIGN.md", lambda ex: render_design_md(d, files, meta, state, ex)),
                         ("PRODUCT.md", lambda ex: render_product_md(state, ex))):
        path = os.path.join(out_dir, name)
        existing = ""
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                existing = f.read()
            if hashes.get(name) and _sha(existing) != hashes[name]:
                stripped_old = re.sub(r"<!-- od:keep -->.*?<!-- /od:keep -->", "", existing, flags=re.S)
                if not quiet:
                    print(f"note: {name} was edited outside od:keep blocks; the previous text is saved as {name}.hand-edited "
                          "so the extend skill can turn the edits into decisions")
                write_text(path + ".hand-edited", stripped_old)
        text = render(existing)
        write_text(path, text)
        hashes[name] = _sha(text)
        written.append(path)
    raw_state = load_state(d)
    raw_state["hashes"] = hashes
    dump_json(os.path.join(d, "state.json"), raw_state)
    if not quiet:
        for p in written:
            print(f"wrote {p}")
    return written


# =============================================================================================
# Preview: one self-contained HTML specimen (every token, a few components, light and dark side by side)
# =============================================================================================

def _esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def preview_kind(state):
    """Which sample screen fits the person's main surface (U5 F11): persuade (a club or product site), operate (an admin
    table), finance (a money dashboard) or read (a guide)."""
    ctx = state.get("context") or {}
    raw = state.get("raw") or {}
    mode = ""
    surf = ctx.get("surfaces") or []
    if surf and isinstance(surf[0], dict):
        mode = str(surf[0].get("mode", "")).lower()
    elif (state.get("answers") or {}).get("Q-scope-06"):
        items = surface_list(answer_value(state["answers"]["Q-scope-06"]))
        mode = items[0]["mode"].lower() if items else ""
    if not mode:
        mode = {"marketing": "persuade", "content": "read"}.get(raw.get("productType") or "", "operate")
    words = f"{ctx.get('product') or ''} {state.get('summary') or ''} {state.get('name') or ''}".lower()
    if mode in ("persuade", "experience"):
        return "persuade"
    if mode == "read":
        return "read"
    if re.search(r"financ|money|budget|bank|invoic|payment|ledger|expense|wallet|net worth", words):
        return "finance"
    return "operate"


def logo_src(state, preview_dir):
    """The person's logo file for the preview header, relative to preview.html, when one was recorded and exists."""
    for f in ((state.get("hooks") or {}).get("H-logo") or {}).get("files") or []:
        for path in (f if os.path.isabs(f) else os.path.join(os.path.dirname(os.path.abspath(preview_dir)), f),
                     os.path.join(os.path.abspath(preview_dir), f)):
            if os.path.exists(path):
                return os.path.relpath(path, os.path.abspath(preview_dir))
    return None


def render_preview(files, meta, state, preview_dir="."):

    prefix = slug(meta.get("prefix") or "ds").replace("-", "")
    css = export_css(files, meta, prefix)
    V = lambda path: f"var({css_var(prefix, path)})"
    VV = lambda path, suffix: f"var({css_var(prefix, path)}-{suffix})"
    res = files["opendesigner.resolver.json"]
    mods = res.get("modifiers", {})
    themes = list(mods["theme"]["contexts"]) if "theme" in mods else meta["modes"]
    base = resolve_all(files, {})
    dials = meta["dials"]
    name = _esc(state.get("name") or "Design system")
    tinfo, sinfo, shp, mot = meta["type"], meta["space"], meta["shape"], meta["motion"]
    t = lambda p: f"font: var({css_var(prefix, p)}); letter-spacing: var({css_var(prefix, p)}-tracking);"
    label = "text.label.lg" if "text.label.lg" in base else "text.body.md"
    ui_css = f"""
*,*::before,*::after{{box-sizing:border-box}}
body{{margin:0;background:#f4f4f5;color:#18181b;font:14px/1.45 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}}
.pv-wrap{{max-width:1240px;margin:0 auto;padding:24px 20px 64px}}
.pv-h1{{font-size:22px;font-weight:650;margin:0 0 4px}} .pv-sub{{color:#52525b;margin:0 0 14px}}
.pv-chips{{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 18px}}
.pv-chip{{background:#fff;border:1px solid #e4e4e7;border-radius:999px;padding:3px 10px;font-size:12px;color:#3f3f46}}
.pv-chip b{{font-weight:600;color:#18181b}}
.pv-h2{{font-size:15px;font-weight:650;margin:34px 0 10px;padding-top:14px;border-top:1px solid #e4e4e7}}
.pv-note{{color:#71717a;font-size:12px;margin:0 0 10px}}
.pv-grid2{{display:grid;grid-template-columns:repeat(auto-fit,minmax(360px,1fr));gap:16px}}
.pv-mono{{font:11px/1.3 ui-monospace,SFMono-Regular,Menlo,monospace}}
.pv-theme{{background:{V('color.surface.base')};color:{V('color.text.primary')};border-radius:14px;padding:18px;border:1px solid {V('color.border.subtle')}}}
.pv-theme-label{{{t('text.label.sm') if 'text.label.sm' in base else ''}color:{V('color.text.secondary')};margin:0 0 12px}}
.pv-row{{display:flex;flex-wrap:wrap;gap:{V('space.stack.sm')};align-items:center;margin:0 0 {V('space.stack.lg')}}}
.ds-btn{{{t(label)}height:{V('size.control.md')};min-width:{V('size.control.md')};padding:0 {V('space.inset.lg')};border-radius:{V('radius.control')};
  border:1px solid transparent;cursor:pointer;display:inline-flex;align-items:center;gap:{V('space.inline.xs')};
  transition:background-color {VV('motion.transition.feedback', 'duration')} {VV('motion.transition.feedback', 'easing')}}}
.ds-btn.primary{{background:{V('color.bg.action.primary')};color:{V('color.text.on-action')}}}
.ds-btn.primary:hover,.ds-btn.primary.is-hover{{background:{V('color.bg.action.primary-hover')}}}
.ds-btn.primary:active,.ds-btn.primary.is-pressed{{background:{V('color.bg.action.primary-pressed')}}}
.ds-btn.secondary{{background:{V('color.bg.neutral.subtle')};color:{V('color.text.primary')}}}
.ds-btn.secondary:hover,.ds-btn.secondary.is-hover{{background:{V('color.bg.neutral.subtle-hover')}}}
.ds-btn.outline{{background:transparent;color:{V('color.text.primary')};border-color:{V('color.border.default')}}}
.ds-btn.danger{{background:{V('color.bg.danger.bold')};color:{V('color.text.on-danger')}}}
.ds-btn.is-focus,.ds-btn:focus-visible,.ds-input:focus-visible{{outline:{V('focus.ring.width')} solid {V('color.border.focus')};outline-offset:{V('focus.ring.offset')}}}
.ds-btn[disabled]{{background:{V('color.bg.disabled')};color:{V('color.text.disabled')};cursor:not-allowed;border-color:transparent}}
.ds-field{{display:flex;flex-direction:column;gap:{V('space.stack.xs')};min-width:200px;flex:1}}
.ds-label{{{t('text.label.md') if 'text.label.md' in base else ''}color:{V('color.text.secondary')}}}
.ds-input{{{t('text.body.md')}height:{V('size.control.md')};padding:0 {V('space.inset.md')};border-radius:{V('radius.control')};
  border:1px solid {V('color.border.input')};background:{V('color.surface.raised')};color:{V('color.text.primary')}}}
.ds-input::placeholder{{color:{V('color.text.tertiary')}}}
.ds-input.is-error{{border-color:{V('color.border.danger')}}}
.ds-input[disabled]{{background:{V('color.bg.disabled')};color:{V('color.text.disabled')};border-color:{V('color.border.subtle')}}}
.ds-help{{{t('text.body.sm')}color:{V('color.text.tertiary')}}} .ds-help.err{{color:{V('color.text.danger')}}}
.ds-card{{background:{V('color.surface.raised')};border:1px solid {V('color.border.subtle')};border-radius:{V('radius.container')};
  padding:{V('space.inset.xl')};box-shadow:{V('elevation.raised')};display:flex;flex-direction:column;gap:{V('space.stack.sm')}}}
.ds-card h3{{margin:0;{t('text.title.md') if 'text.title.md' in base else t('text.title.sm')}}}
.ds-card p{{margin:0;{t('text.body.md')}color:{V('color.text.secondary')}}}
.ds-badge{{{t('text.label.md') if 'text.label.md' in base else ''}padding:2px {V('space.inset.sm')};border-radius:{V('radius.detail')}}}
.ds-banner{{{t('text.body.md')}padding:{V('space.inset.md')} {V('space.inset.lg')};border-radius:{V('radius.control')};flex:1;min-width:150px}}
.ds-link{{color:{V('color.text.link')};text-decoration:underline;text-underline-offset:2px}}
.ds-table{{width:100%;border-collapse:collapse;{t('text.body.md')}}}
.ds-table th{{text-align:left;{t('text.label.md') if 'text.label.md' in base else ''}color:{V('color.text.secondary')};padding:{V('space.inset.sm')} {V('space.inset.md')};border-bottom:1px solid {V('color.border.default')}}}
.ds-table td{{padding:{V('space.inset.sm')} {V('space.inset.md')};border-bottom:1px solid {V('color.border.subtle')};height:{V('size.control.md')}}}
.pv-details{{margin:0 0 18px}} .pv-details summary{{cursor:pointer;color:#52525b;font-size:12px;margin:0 0 8px}}
.sw-ramp{{display:grid;grid-template-columns:90px repeat(12,1fr);gap:3px;margin:0 0 3px;align-items:stretch}}
.sw{{height:38px;border-radius:4px;display:flex;align-items:flex-end;padding:2px 3px;font:9px/1 ui-monospace,Menlo,monospace}}
.sw-name{{font-size:12px;color:#3f3f46;align-self:center}}
.role-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:6px}}
.role{{display:flex;gap:8px;align-items:center;font:11px/1.25 ui-monospace,Menlo,monospace;color:{V('color.text.secondary')}}}
.role i{{width:28px;height:28px;border-radius:6px;flex:none;border:1px solid {V('color.border.subtle')}}}
.ruler{{display:flex;align-items:flex-end;gap:10px;flex-wrap:wrap}}
.ruler div{{background:#6366f1;opacity:.85;border-radius:2px}}
.pv-card{{background:#fff;border:1px solid #e4e4e7;border-radius:12px;padding:16px}}
.motion-box{{width:36px;height:36px;border-radius:8px;background:{V('color.bg.action.primary')}}}
.motion-lane{{position:relative;height:44px;background:#f4f4f5;border-radius:8px;margin:0 0 8px}}
.motion-lane .motion-box{{position:absolute;left:4px;top:4px}}
.pv-card:hover .motion-box.m-std{{transform:translateX(420px);transition:transform {V('motion.duration.medium')} {V('motion.easing.standard')}}}
.pv-card:hover .motion-box.m-spring{{transform:translateX(420px);transition:transform {VV('motion.transition.move', 'duration')} {VV('motion.transition.move', 'easing')}}}
.motion-box{{transition:transform {V('motion.duration.medium-exit')} {V('motion.easing.exit')}}}
@media (prefers-reduced-motion: reduce){{.pv-card:hover .motion-box{{transform:none}}}}
"""
    chips = "".join(f'<span class="pv-chip">{_esc(k)} <b>{v}</b></span>' for k, v in dials.items())
    chips += f'<span class="pv-chip">body <b>{tinfo["base"]}px x {tinfo["ratio"]}</b></span>'
    chips += f'<span class="pv-chip">unit <b>{sinfo["unit"]}px</b></span>'
    chips += f'<span class="pv-chip">radius <b>{shp["control"]}</b></span>'
    chips += f'<span class="pv-chip">depth <b>{_esc(meta["elevation"]["model"])}</b></span>'
    if state.get("raw", {}).get("brandColor"):
        chips += f'<span class="pv-chip">brand <b>{_esc(state["raw"]["brandColor"])}</b></span>'
    kind = preview_kind(state)
    head = "headline.sm" if "text.headline.sm" in base else ("title.lg" if "text.title.lg" in base else "title.md")
    big = "headline.lg" if "text.headline.lg" in base else head
    logo = logo_src(state, preview_dir)
    num = "text.numeric.md" if "text.numeric.md" in base else "text.body.md"
    num_lg = "text.numeric.lg" if "text.numeric.lg" in base else ("text." + head)
    raw_name = state.get("name") or "Your product"
    what = product_words(state)
    clubby = bool(re.search(r"\b(club|team|school|community|society|group|league|class)\b", (what + " " + raw_name).lower()))
    lead_style = t("text.body.lg") if "text.body.lg" in base else t("text.body.md")

    def badge(kind_, text):
        return f'<span class="ds-badge" style="background:{V(f"color.bg.{kind_}.subtle")};color:{V(f"color.text.{kind_}")}">{_esc(text)}</span>'

    def components(theme):
        brandbar = (f'<img src="{_esc(logo)}" alt="{name} logo" style="height:32px;width:auto">' if logo else
                    f'<span style="{t("text.label.lg") if "text.label.lg" in base else ""}color:{V("color.text.primary")}">{name}</span>')
        nav = (f'<div style="display:flex;align-items:center;justify-content:space-between;gap:12px;margin:0 0 20px;padding:0 0 12px;'
               f'border-bottom:1px solid {V("color.border.subtle")}">{brandbar}<a class="ds-link" href="#">'
               f'{"Settings" if kind in ("operate", "finance") else "Contact"}</a></div>')
        if kind == "persuade":
            tag = _esc(what) if what else f"Everything {name} does, in one place."
            cta, cta2 = ("Join us", "See what we do") if clubby else ("Get started", "See how it works")
            cards = (("Meet the team", "Who we are and what we build."), ("What we do", "Projects, builds and competitions."),
                     ("Upcoming events", "Next meet-up: Friday after school.")) if clubby else \
                    (("Quick to start", "Set up in minutes, no training needed."), ("Made for you", "Every screen fits how you work."),
                     ("Help when you need it", "Real people answer within a day."))
            body = (f'<div style="{t("text." + big)}margin:0 0 8px">{name}</div>'
                    f'<p style="{lead_style}color:{V("color.text.secondary")};margin:0 0 18px;max-width:52ch">{tag}</p>'
                    f'<div class="pv-row"><button class="ds-btn primary">{cta}</button><button class="ds-btn outline">{cta2}</button></div>'
                    '<div class="pv-row" style="align-items:stretch">'
                    + "".join(f'<div class="ds-card" style="flex:1;min-width:160px"><h3>{_esc(a)}</h3><p>{_esc(b_)}</p></div>' for a, b_ in cards)
                    + "</div>"
                    f'<div class="pv-row" style="align-items:flex-end"><label class="ds-field"><span class="ds-label">Your email</span>'
                    f'<input class="ds-input" placeholder="you@example.com"><span class="ds-help">We only use it to reply.</span></label>'
                    f'<button class="ds-btn primary">{"Sign up" if clubby else "Request access"}</button></div>')
        elif kind == "finance":
            rows_ = (("12 Sep", "Grocer", "Food", "-54.20", "success"), ("11 Sep", "Salary", "Income", "+3,200.00", "success"),
                     ("10 Sep", "Power bill", "Bills", "-88.15", "warning"), ("09 Sep", "Card refund", "Refund", "+19.99", "info"))
            trs = "".join(f'<tr><td>{a}</td><td>{b_}</td><td>{badge(k_, c_)}</td><td style="text-align:right;{t(num)}">{d_}</td></tr>'
                          for a, b_, c_, d_, k_ in rows_)
            body = (f'<div style="{t("text." + head)}margin:0 0 12px">Overview</div>'
                    '<div class="pv-row" style="align-items:stretch">'
                    + "".join(f'<div class="ds-card" style="flex:1;min-width:150px"><p>{a}</p><div style="{t(num_lg)}color:{V("color.text.primary")}">{b_}</div></div>'
                              for a, b_ in (("Balance", "$12,480.20"), ("Spent this month", "$2,140.75"), ("Bills due", "3")))
                    + "</div>"
                    f'<div class="pv-row" style="justify-content:space-between"><span style="{t("text.title.md") if "text.title.md" in base else ""}">Transactions</span>'
                    '<button class="ds-btn primary">Add transaction</button></div>'
                    f'<table class="ds-table"><thead><tr><th>Date</th><th>Payee</th><th>Category</th><th style="text-align:right">Amount</th></tr></thead><tbody>{trs}</tbody></table>')
        elif kind == "read":
            body = (f'<div style="{t("text." + big)}margin:0 0 8px">Getting started with {name}</div>'
                    f'<p style="{lead_style}color:{V("color.text.primary")};max-width:60ch">'
                    'This guide takes about five minutes. Each step shows what to do and what you will see. '
                    '<a class="ds-link" href="#">Skip to the examples</a>.</p>'
                    f'<div class="ds-banner" style="background:{V("color.bg.info.subtle")};color:{V("color.text.info")};margin:0 0 12px">Tip: you can come back to any step later.</div>'
                    f'<pre style="{t("text.code.md")}background:{V("color.surface.sunken")};padding:{V("space.inset.md")};border-radius:{V("radius.container")};margin:0 0 12px">npm install {_esc(slug(raw_name))}</pre>'
                    '<div class="pv-row"><button class="ds-btn primary">Next step</button><button class="ds-btn secondary">Back</button></div>')
        else:
            people = (("Asha Rao", "Admin", "Active", "success"), ("Ben Ortiz", "Editor", "Invited", "info"),
                      ("Chen Wei", "Viewer", "Suspended", "danger"), ("Dana Kim", "Editor", "Active", "success"))
            trs = "".join(f'<tr><td>{a}</td><td>{b_}</td><td>{badge(k_, c_)}</td><td style="text-align:right"><a class="ds-link" href="#">Edit</a></td></tr>'
                          for a, b_, c_, k_ in people)
            body = (f'<div class="pv-row" style="justify-content:space-between"><span style="{t("text." + head)}">Users</span>'
                    '<span style="display:flex;gap:8px"><input class="ds-input" placeholder="Search users" style="max-width:200px">'
                    '<button class="ds-btn primary">Add user</button></span></div>'
                    f'<table class="ds-table"><thead><tr><th>Name</th><th>Role</th><th>Status</th><th></th></tr></thead><tbody>{trs}</tbody></table>'
                    '<div class="pv-row" style="align-items:flex-start;margin-top:16px">'
                    '<label class="ds-field"><span class="ds-label">Email</span><input class="ds-input" placeholder="name@example.com"><span class="ds-help">Used to sign in.</span></label>'
                    '<label class="ds-field"><span class="ds-label">Team</span><input class="ds-input is-error" value="Ops Team!"><span class="ds-help err">Use letters, numbers and dashes.</span></label>'
                    '<label class="ds-field"><span class="ds-label">Plan</span><input class="ds-input" value="Team" disabled><span class="ds-help">Set by your admin.</span></label></div>')
        states = ('<p class="pv-theme-label" style="margin-top:20px">Button states</p>'
                  '<div class="pv-row"><button class="ds-btn primary">Default</button><button class="ds-btn primary is-hover">Hover</button>'
                  '<button class="ds-btn primary is-pressed">Pressed</button><button class="ds-btn primary is-focus">Focus</button>'
                  '<button class="ds-btn primary" disabled>Disabled</button><button class="ds-btn secondary">Secondary</button>'
                  '<button class="ds-btn danger">Delete</button></div>')
        return f'<div class="pv-theme" data-theme="{theme}"><p class="pv-theme-label">{theme} theme</p>{nav}{body}{states}</div>'
    html = [f"<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">",
            f"<title>{name} preview</title><style>\n{css}\n{ui_css}</style></head><body><div class=\"pv-wrap\">",
            f"<h1 class=\"pv-h1\">{name}</h1><p class=\"pv-sub\">{_esc((product_words(state) or 'Your design system').rstrip('. '))}. "
            f"Sample screens use only your tokens; the words are examples.</p>",
            f"<details class=\"pv-details\"><summary>Details: the settings behind this</summary><div class=\"pv-chips\">{chips}</div></details>",
            "<div class=\"pv-grid2\">" + "".join(components(th) for th in themes) + "</div>"]
    # color ramps
    html.append("<h2 class=\"pv-h2\">Color ramps</h2><p class=\"pv-note\">Primitives, 12 contrast-indexed OKLCH steps per hue; light and dark are separate ramps.</p>")
    for mode in ("light", "dark"):
        html.append(f"<div class=\"pv-card\" style=\"margin:0 0 10px;{'background:#0c0c0e;border-color:#27272a' if mode == 'dark' else ''}\">")
        for rname, rv in meta["ramps"].items():
            cells = []
            for i, hx in enumerate(rv[mode]["hex"], 1):
                fg = "#000" if contrast(hx, "#000000") > contrast(hx, "#ffffff") else "#fff"
                cells.append(f'<div class="sw" style="background:{hx};color:{fg}" title="{rname} {mode} {i} {hx}">{i}</div>')
            html.append(f'<div class="sw-ramp"><span class="sw-name" style="color:{"#d4d4d8" if mode == "dark" else "#3f3f46"}">{rname} {mode}</span>{"".join(cells)}</div>')
        html.append("</div>")
    # semantic roles per theme
    html.append("<h2 class=\"pv-h2\">Semantic color roles</h2><div class=\"pv-grid2\">")
    for th in themes:
        flat = resolve_all(files, {"theme": th} if "theme" in mods else {})
        items = []
        for p in sorted(flat):
            if flat[p]["type"] == "color" and re.match(r"color\.(surface|text|bg|border|icon)\.", p):
                items.append(f'<div class="role"><i style="background:{V(p)}"></i><span>{_esc(p[6:])}<br>{hex_of(flat[p]["resolved"])}</span></div>')
        html.append(f'<div class="pv-theme" data-theme="{th}"><p class="pv-theme-label">{th}</p><div class="role-grid">{"".join(items)}</div></div>')
    html.append("</div>")
    # typography
    html.append("<h2 class=\"pv-h2\">Typography</h2>")
    html.append(f"<p class=\"pv-note\">round({tinfo['base']} x {tinfo['ratio']}^n): {', '.join(str(x) for x in tinfo['sizes'])}px. "
                f"Weights {', '.join(f'{k} {v}' for k, v in tinfo['weights'].items())}.</p><div class=\"pv-theme\" data-theme=\"light\">")
    for p in sorted((p for p in base if base[p]["type"] == "typography"), key=lambda p: -_px(base[p]["resolved"]["fontSize"])):
        ext = (base[p].get("$extensions") or {}).get(NS, {})
        v = base[p]["resolved"]
        caps = "text-transform:uppercase;" if ext.get("textTransform") else ""
        html.append(f'<div style="display:flex;gap:16px;align-items:baseline;margin:0 0 8px"><span class="pv-mono" style="width:170px;flex:none;color:{V("color.text.tertiary")}">'
                    f'{p[5:]} {fmt_num(_px(v["fontSize"]))}/{ext.get("lineHeightPx")} {int(v["fontWeight"])}</span>'
                    f'<span style="{t(p)}{caps}">{_esc(ext.get("use", "The quick brown fox"))}</span></div>')
    html.append("</div>")
    # spacing, density, radius
    ladder = sinfo["ladder"]
    html.append("<h2 class=\"pv-h2\">Space, density, radius and targets</h2><div class=\"pv-grid2\"><div class=\"pv-card\"><p class=\"pv-note\">Spacing ladder</p><div class=\"ruler\">")
    for v in ladder:
        if v:
            html.append(f'<div style="width:{v}px;height:{v}px" title="space.{v}"></div>')
    html.append("</div><p class=\"pv-mono\" style=\"margin:8px 0 0\">" + " ".join(str(v) for v in ladder) + "</p></div><div class=\"pv-card\"><p class=\"pv-note\">Density modes (same component)</p>")
    for dn in DENSITIES:
        html.append(f'<div data-density="{dn}" data-theme="light" style="display:flex;gap:10px;align-items:center;margin:0 0 8px"><span class="pv-mono" style="width:90px">{dn}</span>'
                    f'<button class="ds-btn primary">Save</button><input class="ds-input" style="max-width:160px" placeholder="Search"></div>')
    html.append("</div><div class=\"pv-card\"><p class=\"pv-note\">Radius roles</p><div style=\"display:flex;gap:12px;flex-wrap:wrap\">")
    for r in ("detail", "control-sm", "control", "container", "overlay", "full"):
        html.append(f'<div style="text-align:center"><div style="width:64px;height:48px;background:#e0e7ff;border:1.5px solid #6366f1;border-radius:{V("radius." + r)}"></div><span class="pv-mono">{r}</span></div>')
    html.append("</div></div><div class=\"pv-card\"><p class=\"pv-note\">Hit-area floors (L14 I-1)</p><div style=\"display:flex;gap:14px;align-items:flex-end\">")
    for k, v in sinfo["targets"].items():
        html.append(f'<div style="text-align:center"><div style="width:{v}px;height:{v}px;border:1.5px dashed #6366f1;border-radius:6px"></div><span class="pv-mono">{k} {v}</span></div>')
    html.append("</div></div></div>")
    # elevation
    html.append("<h2 class=\"pv-h2\">Elevation</h2><div class=\"pv-grid2\">")
    for th in themes:
        boxes = "".join(f'<div style="flex:1;min-width:100px;height:80px;border-radius:{V("radius.container")};background:{V("color.surface." + ("raised" if e == "raised" else "overlay"))};'
                        f'box-shadow:{V("elevation." + e)};border:1px solid {V("color.border.subtle")};display:flex;align-items:center;justify-content:center"><span class="pv-mono">{e}</span></div>'
                        for e in ("raised", "floating", "overlay"))
        html.append(f'<div class="pv-theme" data-theme="{th}" style="background:{V("color.surface.sunken")}"><p class="pv-theme-label">{th} &middot; {_esc(meta["elevation"]["model"])}</p><div style="display:flex;gap:16px;flex-wrap:wrap">{boxes}</div></div>')
    html.append("</div>")
    # motion
    html.append("<h2 class=\"pv-h2\">Motion</h2><div class=\"pv-card\"><p class=\"pv-note\">Hover this card: the top box uses motion.duration.medium with the standard easing, the "
                "bottom one the spatial spring (CSS linear() sample). Reduced motion removes travel.</p>")
    html.append('<div class="motion-lane"><div class="motion-box m-std"></div></div><div class="motion-lane"><div class="motion-box m-spring"></div></div>')
    html.append("<p class=\"pv-mono\">" + " &middot; ".join(f"{k} {v}ms" for k, v in mot["durations"].items()) + "</p>")
    sp = base.get("motion.spring.spatial.default")
    if sp:
        ext = (sp.get("$extensions") or {}).get(NS, {})
        pts = re.findall(r"[-\d.]+", ext.get("css", {}).get("easing", ""))
        if pts and ext.get("spring", {}).get("dampingRatio", 1) < 1:
            ys = [float(x) for x in pts]
            n = len(ys) - 1
            path = " ".join(f"{'M' if i == 0 else 'L'}{rnd(10 + 280 * i / n, 1)},{rnd(90 - 60 * y, 1)}" for i, y in enumerate(ys))
            html.append(f'<svg width="300" height="100" viewBox="0 0 300 100" role="img" aria-label="spring curve"><path d="M10 30H290" stroke="#d4d4d8" stroke-dasharray="3 3"/>'
                        f'<path d="{path}" fill="none" stroke="#6366f1" stroke-width="2"/></svg><p class="pv-mono">spatial spring: damping {ext["spring"]["dampingRatio"]}, stiffness '
                        f'{ext["spring"]["stiffness"]}, {ext["css"]["durationMs"]}ms; Apple duration {ext["apple"]["duration"]}s bounce {ext["apple"]["bounce"]}</p>')
    html.append("</div></div></body></html>")
    return "\n".join(html) + "\n"


def cmd_preview(d, open_=False, files=None, meta=None, quiet=False):
    state = merge_defaults(load_state(d))
    if files is None:
        files, meta, _ = generate_system(load_state(d))
    path = os.path.join(d, "preview.html")
    write_text(path, render_preview(files, meta, state, d))
    if not quiet:
        print(f"wrote {path}")
    if open_:
        webbrowser.open("file://" + os.path.abspath(path))
    return path


# =============================================================================================
# Intake: reference measurements -> proposed dials and raw inputs (LEVERS E, spec 5)
# =============================================================================================

def _inverse_anchors(points, y):
    """x for a y on a piecewise-linear, monotonic anchor map."""
    pts = [(x, 120.0 if v == "max" else float(v)) for x, v in points if isinstance(v, (int, float)) or v == "max"]
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        lo, hi = min(y0, y1), max(y0, y1)
        if lo <= y <= hi and y1 != y0:
            return x0 + (y - y0) / (y1 - y0) * (x1 - x0)
    return pts[0][0] if abs(y - pts[0][1]) < abs(y - pts[-1][1]) else pts[-1][0]


def _band_mid(dial, param, value):
    drv = lever_index()[param]
    best = None
    for lo, hi, out in drv["map"]["bands"]:
        if out == value:
            return (lo + hi) // 2
        if isinstance(out, (int, float)) and isinstance(value, (int, float)):
            dist = abs(out - value)
            if best is None or dist < best[0]:
                best = (dist, (lo + hi) // 2)
    return best[1] if best else None


def _shadow_alpha(s):
    m = re.findall(r"rgba?\(([^)]*)\)", s)
    al = []
    for grp in m:
        parts = [p for p in re.split(r"[\s,/]+", grp.strip()) if p]
        if len(parts) >= 4:
            try:
                a = parts[3]
                al.append(float(a[:-1]) / 100 if a.endswith("%") else float(a))
            except ValueError:
                pass
    return max(al) if al else None


def _face_key(name):
    """'sohne-var', 'Söhne', 'Söhne Buch' -> 'sohne': compare typeface names across CSS and a person's words."""
    import unicodedata
    t = unicodedata.normalize("NFKD", str(name or "")).encode("ascii", "ignore").decode().lower()
    t = re.sub(r"[\s_-]*(var|variable|vf|text|display|web|buch|regular|pro)$", "", re.sub(r"[\"']", "", t).strip())
    return re.sub(r"[^a-z0-9]", "", t)


def _shadow_strength(dep, shadows):
    """Count-weighted median shadow strength (U5, coordinator): each elevation layer's alpha scaled by how soft it is
    (blur plus spread over 16px, at least a quarter), so a tight key shadow with a high alpha does not read as deep.
    White or transparent layers do not count."""
    items = []
    for lv in dep.get("levels") or []:
        a, b, sp = float(lv.get("alpha") or 0), float(lv.get("blur") or 0), float(lv.get("spread") or 0)
        if a > 0:
            items.append((a * clamp((b + max(sp, 0)) / 16, 0.25, 1.0), int(lv.get("count") or 1)))
    if not items:
        for sh in shadows or []:
            for lay in re.split(r",(?![^(]*\))", sh):
                if re.search(r"rgba?\(\s*255[\s,]+255[\s,]+255", lay) or "#fff" in lay.lower():
                    continue
                al = _shadow_alpha(lay)
                nums = [float(x) for x in re.findall(r"(-?\d*\.?\d+)px", lay)]
                blur = abs(nums[2]) if len(nums) > 2 else 0.0
                spread = nums[3] if len(nums) > 3 else 0.0
                if al:
                    items.append((al * clamp((blur + max(spread, 0)) / 16, 0.25, 1.0), 1))
    if not items:
        return None
    items.sort()
    total, acc = sum(c for _, c in items), 0
    for a, c in items:
        acc += c
        if acc * 2 >= total:
            return rnd(a, 3)
    return rnd(items[-1][0], 3)


def fit_reference(ref, state=None):
    """Run LEVERS E3 backwards on a measurement file (engine schema or opendesigner-extract css_scan --json output).
    With the person's state, a reference typeface that is the person's own licensed face may carry over (their asset)."""
    kind = ref.get("kind") or ("url" if ref.get("method") == "computed" else "code")
    tag = ref.get("tag", "inspiration")
    conf_kind = {"url": "url", "code": "url", "figma": "figma", "screenshot": "screenshot", "pdf": "screenshot"}.get(kind, "url")
    ri = levers()["referenceIntake"]["dials"]
    m = ref.get("measurements") or ref  # css_scan output is flat
    props, notes = [], []

    def conf(dial):
        return ri.get(dial, {}).get("confidence", {}).get(conf_kind, "medium")

    def add(path, value, confidence, basis):
        if value is None or confidence == "none":
            return
        props.append({"path": path, "value": value, "confidence": confidence, "basis": basis, "status": "pending"})
    # roundness
    rad = (m.get("radius") or {}).get("mostCommon", m.get("controlRadius"))
    if rad is not None:
        v = 97 if rad == "full" or (isinstance(rad, (int, float)) and rad >= 999) else _band_mid("roundness", "radius.control",
                                                                                                  snap_to(float(rad), [0, 2, 4, 6, 8, 12, 16]))
        add("dials.roundness", int(v), conf("roundness"), f"most common control radius {rad} -> A5 band")
    # density
    ty = m.get("type") or {}
    scale = ty.get("scale") or {}
    body = m.get("bodySize") or scale.get("base")
    ctl = m.get("controlHeight")
    guesses = []
    if ctl:
        guesses.append(_band_mid("density", "control.height.md", snap_to(float(ctl), [32, 40, 48])))
    if body:
        guesses.append({13: 95, 14: 78, 15: 60, 16: 35, 17: 25, 18: 15, 19: 5}.get(int(round(float(body))), 50))
    if guesses:
        add("dials.density", int(round(sum(guesses) / len(guesses))), conf("density"),
            f"body {body}px" + (f", controls {ctl}px" if ctl else "") + " -> A3 bands")
    # depth
    dep = m.get("depth") or {}
    shadows = dep.get("shadows") or m.get("shadows") or []
    if m.get("backdropBlur"):
        add("dials.depth", 90, conf("depth"), "backdrop blur on controls -> materials band")
    elif dep.get("hint") or shadows is not None:
        hint = dep.get("hint") or ("borders" if not shadows else "shadow-ladder")
        v = {"borders": 8, "ring+faint-shadow": 25, "tonal": 45, "shadow-ladder": 68}.get(hint, 40)
        al = _shadow_strength(dep, shadows) or 0
        if al and hint in ("shadow-ladder", "ring+faint-shadow"):
            pos = 16 + (clamp(al, 0.08, 0.24) - 0.08) / 0.16 * 84
            lo, hi = (16, 35) if hint == "ring+faint-shadow" else (56, 80)
            v = int(round(clamp(pos, lo, hi)))
        add("dials.depth", v, conf("depth"), f"{hint}" + (f", median shadow strength {al} (alpha weighted by softness)" if al else "") + " -> A6 bands")
    # colorfulness and warmth
    col = m.get("color") or {}
    accents = col.get("accents") or []
    if accents:
        top = accents[0]["hex"] if isinstance(accents[0], dict) else accents[0]
        hct = hct_chroma_of_hex(top)
        pts = next(d for d in levers()["dials"] if d["id"] == "colorfulness")["drives"][0]["map"]["points"]
        v = _inverse_anchors(pts, hct)
        hues = {round(hex_to_oklch(a["hex"] if isinstance(a, dict) else a)[2] / 30) for a in accents[:6]
                if hex_to_oklch(a["hex"] if isinstance(a, dict) else a)[1] > 0.06}
        if len(hues) >= 3:
            v = max(v, 62)
        add("dials.colorfulness", int(round(clamp(v, 0, 100))), conf("colorfulness"),
            f"top accent HCT chroma {rnd(hct, 1)}, {len(hues)} distinct accent hue(s) -> A7 anchors")
        if tag == "our-product":
            add("raw.brandColor", top, "high", "the person's own product: its brand color may carry over")
        else:
            notes.append(f"Accent {top} is the reference's identity: carry its role and chroma level, not the hue; ask for the brand color.")
    nt = col.get("neutralTint")
    if nt:
        c, h = float(nt.get("chroma", nt.get("c", 0))), float(nt.get("hue", nt.get("h", 0)) or 0)
        if c < 0.004:
            w = 50
        elif 180 <= h <= 320:  # cool: slate 0.046 (0), gray 0.027 (25)
            w = 25 - (c - 0.027) / 0.019 * 25 if c >= 0.027 else 50 - c / 0.027 * 25
        else:  # warm: stone 0.013 (75), taupe 0.021 (100)
            w = 50 + c / 0.013 * 25 if c <= 0.013 else 75 + (c - 0.013) / 0.008 * 25
        add("dials.warmth", int(round(clamp(w, 0, 100))), conf("warmth"), f"neutral tint chroma {c} at hue {h} -> A8 anchors")
    # type
    if scale.get("base"):
        b = int(round(float(scale["base"])))
        if 12 <= b <= 20:
            add("raw.baseSize", b, "high" if conf_kind != "screenshot" else "medium", f"type scale fit base {scale['base']}")
        r = scale.get("ratio")
        if r:
            if (scale.get("meanLogResidual") or 0) < 0.03:
                add("dials.expression", int(_band_mid("expression", "type.ratio", min([1.2, 1.25, 1.333], key=lambda x: abs(x - r)))),
                    "medium", f"modular type ratio {r} -> A1 ratio band (partly: expression also covers emphasis)")
                if r not in (1.2, 1.25, 1.333):
                    add("overrides.type.ratio", r, "medium", "measured ratio is between the dial's bands; keep it as an override")
            else:
                notes.append("Type sizes are hand-tuned (large residuals): keep the measured sizes as overrides rather than a ratio.")
    fams = ty.get("families") or m.get("fontFamilies") or ((m.get("typefaces") if isinstance(m.get("typefaces"), list) else None) or [])
    fams = [f if isinstance(f, str) else (f.get("family") or f.get("name") or "") for f in fams]
    fams = [f for f in fams if f and not _generic_face(f.strip("'\" ").lower())]
    raw_s = (state or {}).get("raw") or {}
    own = [x for x in (raw_s.get("brandFace"), raw_s.get("textFace"), raw_s.get("displayFace"))
           if isinstance(x, str) and not x.startswith("=") and not _generic_face(x)]
    h_type = (((state or {}).get("hooks") or {}).get("H-type") or {}).get("status")
    licensed = h_type in ("have", "placeholder") or any(v is True for v in (raw_s.get("fontLicence") or {}).values())
    if fams:
        mine = next((o for o in own for f in fams if _face_key(o) and _face_key(o) == _face_key(f)), None)
        if tag == "our-product":
            add("raw.textFace", fams[0], "high", "the person's own product; confirm the licence covers web and apps (hook H-type)")
        elif mine and licensed:
            add("raw.textFace", mine, "high", f"{fams[0]} is your own licensed face ({mine}, hook H-type), not taken from the reference; "
                                                "its licence scope still decides where it is used (raw.fontLicence)")
            notes.append(f"Typeface {fams[0]} matches your own licensed {mine}: kept as yours, not copied from the reference.")
        else:
            notes.append(f"Typeface {fams[0]} is not carried; pick an open face of the same classification (identity rule, spec 5.4)."
                         + (" If you license it yourself, record it first (hook H-type and raw.fontLicence)." if not licensed else ""))
    sp = m.get("space") or {}
    if sp.get("unit"):
        add("raw.spaceUnit", int(sp["unit"]), "high" if conf_kind != "screenshot" else "low", f"largest of 4/5/8 dividing most values ({sp.get('shareDivisible')})")
    mo = m.get("motion") or {}
    if mo.get("durationMultiplier") and conf("energy") != "none":
        pts = next(d for d in levers()["dials"] if d["id"] == "energy")["drives"]
        mp = next(x for x in pts if x["param"] == "motion.durationMultiplier")["map"]["points"]
        v = _inverse_anchors(mp, clamp(float(mo["durationMultiplier"]), 0.8, 1.2))
        eas = " ".join(str(e) for e in mo.get("easings") or [])
        if re.search(r"cubic-bezier\([^)]*,\s*1\.\d+", eas) or "linear(" in eas:
            v = max(v, 72)
        add("dials.energy", int(round(v)), conf("energy"), f"median duration {mo.get('median')}ms -> multiplier {mo['durationMultiplier']} -> A4 anchors")
    notes.append("Brand presence is never inferred: it starts at 50 and is asked (LEVERS E2).")
    if tag == "competitor":
        props = []
        notes.insert(0, "Competitor reference: read only to list the category's shared tropes; nothing is proposed.")
    return {"id": ref.get("id") or "ref", "tag": tag, "kind": kind, "proposals": props, "notes": notes}


def cmd_intake(d, path, accept=False, as_json=False):
    ref = read_json(path)
    sp0 = os.path.join(d, "state.json")
    fit = fit_reference(ref, merge_defaults(read_json(sp0)) if os.path.exists(sp0) else None)
    rid = fit["id"] if fit["id"] != "ref" else slug(os.path.splitext(os.path.basename(path))[0])
    fit["id"] = rid
    fit["file"] = os.path.relpath(path, d) if os.path.exists(d) else path
    sp = os.path.join(d, "state.json")
    if os.path.exists(sp):
        state = merge_defaults(read_json(sp))
        state.setdefault("references", {})[rid] = {"tag": fit["tag"], "kind": fit["kind"], "file": fit["file"],
                                                    "proposals": fit["proposals"], "notes": fit["notes"],
                                                    "status": "accepted" if accept else "pending"}
        dump_json(sp, state)
        if accept:
            for pr in fit["proposals"]:
                cmd_set(d, pr["path"], pr["value"], why=f"from reference {rid} ({pr['confidence']} confidence): {pr['basis']}",
                        set_by="reference", source_ref=rid, quiet=True)
                pr["status"] = "accepted"
    if as_json:
        print(json.dumps(fit, indent=2))
        return fit
    print(f"Reference {rid} ({fit['tag']}, {fit['kind']}): {len(fit['proposals'])} proposal(s)"
          + (" accepted" if accept else ", pending until accepted"))
    for pr in fit["proposals"]:
        print(f"  {pr['path']:26s} {json.dumps(pr['value']):>8s}  {pr['confidence']:6s}  {pr['basis']}")
    for n in fit["notes"]:
        print(f"  note: {n}")
    if not accept and fit["proposals"]:
        print(f"Accept one with: engine.py set <path> <value> --set-by reference --source-ref {rid} --why \"...\"  (or rerun with --accept)")
    return fit


# =============================================================================================
# CLI
# =============================================================================================

def cmd_resolve(d):
    state = load_state(d)
    ctx = Ctx(state)
    out = {"dials": ctx.dials, "dialSources": ctx.dial_src, "macroConflicts": ctx.conflicts,
           "zoom": zoom_levels(d, merge_defaults(state)), "params": {k: ctx.params[k] for k in sorted(ctx.params)}}
    print(json.dumps(out, indent=2, ensure_ascii=False))


def cmd_build(d, force=False):
    """generate -> validate -> (only if no errors, or --force) export all + DESIGN.md + PRODUCT.md + preview."""
    files, meta, _ = cmd_generate(d, quiet=True)
    rep = validate_dir(d)
    errors = rep.count("error")
    if errors and not force:
        track(d, "error", step="build", count=errors)
        print_report(rep, d)
        print(f"Stopped after tokens/: nothing was exported, and DESIGN.md and preview.html were not refreshed. "
              f"Fix the error{'s' if errors != 1 else ''} above and run build again (--force exports anyway).")
        return 1
    cmd_export(d, "all", files, meta, quiet=True)
    cmd_design_md(d, files=files, meta=meta, quiet=True)
    cmd_preview(d, files=files, meta=meta, quiet=True)
    track(d, "export", kind="all")
    print(f"built {d}: tokens, build/ (css, tailwind, figma, paper, swift, compose, dtcg), DESIGN.md, PRODUCT.md, preview.html"
          + (" (exported with errors because of --force)" if errors else ""))
    print_report(rep, d)
    return 1 if errors else 0


def main(argv=None):
    top = argparse.ArgumentParser(add_help=False)
    top.add_argument("--dir", default=None, help=f"state directory (default ./{DEFAULT_DIR})")
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--dir", default=argparse.SUPPRESS, help=f"state directory (default ./{DEFAULT_DIR})")
    ap = argparse.ArgumentParser(prog="engine.py", description="OpenDesigner engine (stdlib only, no network).", parents=[top])
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("init", parents=[common], help="create state.json with defaults")
    p.add_argument("--from", dest="src")
    p.add_argument("--name")
    p.add_argument("--force", action="store_true")
    for name in ("set", "pick"):
        p = sub.add_parser(name, parents=[common], help="record one decision" if name == "set" else "answer a question (answers.<Q-id>)")
        p.add_argument("path")
        p.add_argument("value", nargs="?")
        p.add_argument("--why", default=None)
        p.add_argument("--set-by", dest="set_by", default=None, help="chosen (default), confirmed_default, auto_default, assumed, delegated, reference, asset")
        p.add_argument("--source-ref", dest="source_ref", default=None)
        p.add_argument("--lock", action="store_true")
        p.add_argument("--force", action="store_true", help="change a locked decision (only with the owner's consent)")
        p.add_argument("--no-doc", dest="no_doc", action="store_true", help="do not refresh DESIGN.md and PRODUCT.md")
    for name in ("lock", "unlock"):
        p = sub.add_parser(name, parents=[common])
        p.add_argument("path")
        p.add_argument("--no-doc", dest="no_doc", action="store_true")
    sub.add_parser("resolve", parents=[common], help="effective dials and derived parameters as JSON")
    sub.add_parser("generate", parents=[common], help="write tokens/ (DTCG 2025.10 + resolver)")
    p = sub.add_parser("validate", parents=[common])
    p.add_argument("--json", action="store_true")
    p = sub.add_parser("export", parents=[common])
    p.add_argument("--format", required=True, choices=["css", "tailwind", "figma", "paper", "swift", "compose", "dtcg", "all"])
    p = sub.add_parser("design-md", parents=[common], help="render DESIGN.md and PRODUCT.md")
    p.add_argument("--out", default=None, help="folder for DESIGN.md and PRODUCT.md (default: project root, or the state folder)")
    p = sub.add_parser("preview", parents=[common])
    p.add_argument("--open", action="store_true")
    p = sub.add_parser("intake", parents=[common], help="fit reference measurements to proposed dials and inputs")
    p.add_argument("file")
    p.add_argument("--accept", action="store_true")
    p.add_argument("--json", action="store_true")
    p = sub.add_parser("build", parents=[common], help="generate + validate, then (if no errors) export all + design-md + preview")
    p.add_argument("--force", action="store_true", help="export even when validation finds errors")
    p = sub.add_parser("sketch", parents=[common], help="Level 0: a complete coarse system from about five answers")
    p.add_argument("--name")
    p.add_argument("--brand", help="brand color hex")
    p.add_argument("--audience", choices=["dense", "regular", "large"])
    p.add_argument("--platforms", help="comma list: web,ios,android,desktop,secondary")
    p.add_argument("--feel", help="comma list of feel words in the person's own words (fun, calm, bold, techy, ...); `engine.py feel` lists them")
    p.add_argument("--delegated", nargs="?", const="all", default=None,
                   help="the person said 'just pick': record the sketch answers as delegated (all, or a comma list such as feel,brand)")
    p.add_argument("--theme", choices=["system-light-dark", "light-dark-toggle", "light-only", "dark-only"])
    p.add_argument("--surfaces", help="Q-scope-06, main surface first: a mode (persuade, operate, read, experience) or name:mode pairs, "
                                      "for example 'app:operate,landing page:persuade'")
    p = sub.add_parser("show", parents=[common], help="fill a visual template with real values from the current state and write it")
    p.add_argument("template", help="palette, type-scale, spacing-ruler, radius, elevation, motion, component-sheet or option-gallery")
    p.add_argument("--out", default=None, help="folder for the page (default opendesigner/preview)")
    p.add_argument("--open", action="store_true")
    p.add_argument("--json", action="store_true", help="print the payload instead of writing the page")
    p = sub.add_parser("feel", parents=[common], help="map plain feel words (fun, calm, techy...) to feel settings; no words lists them all")
    p.add_argument("words", nargs="*")
    p = sub.add_parser("review", parents=[common], help="find hard-coded values that bypass tokens and stale DESIGN.md sections")
    p.add_argument("--project", default=None, help="folder to scan (default: the project root)")
    p.add_argument("--strict", action="store_true", help="exit 1 when anything is found")
    p.add_argument("--json", action="store_true")
    p = sub.add_parser("feedback", parents=[common], help="record a gap, bug, confusing step or idea and print an issue link")
    p.add_argument("text", nargs="?", default="")
    p.add_argument("--kind", default=None, choices=list(FEEDBACK_KINDS), help="default: idea (confusing with --from-journey)")
    p.add_argument("--from-journey", dest="from_journey", action="store_true",
                   help="add the hotspots from the journey log: question ids and counts only, never notes")
    p.add_argument("--area", default=None)
    p.add_argument("--question", default=None)
    a = ap.parse_args(argv)
    d = a.dir or DEFAULT_DIR
    if a.cmd == "init":
        cmd_init(d, a.src, a.name, a.force)
    elif a.cmd in ("set", "pick"):
        path, value = a.path, a.value
        if value is None and "=" in path:
            path, value = path.split("=", 1)
        if value is None:
            raise SystemExit("give a value: engine.py set <path> <json-value>  (or path=value)")
        if a.cmd == "pick" and not path.startswith("answers."):
            path = "answers." + path
        cmd_set(d, path, parse_value(value), a.why, a.force, set_by=a.set_by, lock=a.lock, source_ref=a.source_ref)
        if not a.no_doc:
            refresh_docs(d)
    elif a.cmd in ("lock", "unlock"):
        cmd_lock(d, a.path, a.cmd == "lock")
        if not a.no_doc:
            refresh_docs(d)
    elif a.cmd == "resolve":
        cmd_resolve(d)
    elif a.cmd == "generate":
        cmd_generate(d)
    elif a.cmd == "validate":
        rep = validate_dir(d)
        print_report(rep, d, a.json)
        if rep.count("error"):
            track(d, "error", step="validate", count=rep.count("error"))
        return 1 if rep.count("error") else 0
    elif a.cmd == "export":
        cmd_export(d, a.format)
        track(d, "export", kind=a.format)
    elif a.cmd == "design-md":
        cmd_design_md(d, a.out)
    elif a.cmd == "preview":
        cmd_preview(d, a.open)
    elif a.cmd == "intake":
        cmd_intake(d, a.file, a.accept, a.json)
    elif a.cmd == "build":
        return cmd_build(d, a.force)
    elif a.cmd == "sketch":
        return cmd_sketch(d, a.name, a.brand, a.audience, a.platforms, a.feel, a.theme, surfaces=a.surfaces, delegated=a.delegated)
    elif a.cmd == "feel":
        return cmd_feel(a.words)
    elif a.cmd == "show":
        cmd_show(d, a.template, a.out, a.open, a.json)
    elif a.cmd == "review":
        return cmd_review(d, a.project, a.strict, a.json)
    elif a.cmd == "feedback":
        os.makedirs(d, exist_ok=True)
        text = a.text
        if a.from_journey:
            hot = journey.feedback_text(d) if journey else ""
            if not hot:
                raise SystemExit("There is no journey log yet, so there are no hotspots to add.")
            text = f"{text} {hot}".strip()
        cmd_feedback(d, text, a.kind or ("confusing" if a.from_journey else "idea"), area=a.area, question=a.question)
    return 0



# =============================================================================================
# Zoom levels, sketch (Level 0), review, feedback (BRIEF requirements 12-16)
# =============================================================================================

def answered_ids(state, decs=None, for_zoom=False):
    """{question id: set_by} for every question answered: answers.<Q-id>, plus the sketch paths that answer one
    (context.product, raw.brandColor, macros, the logo hook; ANSWER_PATHS)."""
    out = {}
    for q, rec in (state.get("answers") or {}).items():
        if for_zoom and isinstance(rec, dict) and rec.get("via") == "sketch" and (questions().get(q) or {}).get("zoom", 0):
            continue  # a sketch answer (for example the theme) does not zoom its area in
        out[q] = (rec.get("set_by") if isinstance(rec, dict) else None) or "chosen"
    for path, (q, _how) in ANSWER_PATHS.items():
        v = get_path(state, path)
        if v not in (None, "", [], {}, "pending") and q not in out:
            out[q] = ((decs or {}).get(path) or {}).get("set_by", "chosen")
    return out


def zoom_levels(d, state):
    """Each area's zoom (BRIEF req. 14-15, U5 F23): the explicit state.zoom value when the model recorded one, else
    inferred from the zoom level of the questions answered in the area. Level k counts once at least half of the area's
    level-k questions are answered (delegated counts, auto defaults do not), and every lower level with questions
    counts too. A sketch alone reads 'sketch' everywhere."""
    decs = _decisions(d)
    answered = answered_ids(state, decs)
    counted = answered_ids(state, decs, for_zoom=True)
    qs = questions()
    out = {}
    for key, title in ZOOM_AREAS:
        rx = SECTION_PATHS.get(title)
        n = sum(1 for k, v in decs.items() if rx and re.match(rx, k) and v["set_by"] != "auto_default")
        by = {1: [], 2: [], 3: []}
        for q in qs.values():
            if q.get("area") == key and q.get("zoom") in by:
                by[q["zoom"]].append(q["id"])
        lvl = 0
        for k in (1, 2, 3):
            if not by[k]:
                continue
            done = [q for q in by[k] if counted.get(q) not in (None, "auto_default")]
            if len(done) * 2 >= len(by[k]):
                lvl = k
            else:
                break
        explicit = (state.get("zoom") or {}).get(key)
        if explicit in ZOOM_LEVELS:
            lvl = ZOOM_LEVELS.index(explicit)  # the model recorded the level it ran; never infer past it
        nxt = []
        for k in range(lvl + 1, 4):
            nxt = [q for q in by.get(k, []) if q not in answered][:3]
            if nxt:
                break
        if not qs:
            nxt = [q for q in ZOOM_NEXT.get(key, []) if q not in answered]
        out[key] = {"level": ZOOM_LEVELS[lvl], "decisions": n, "next": nxt}
    return out


AUDIENCE_WORDS = {"dense": "people who use it all day for work, in screens full of data",
                  "regular": "people who use it often, as an everyday app",
                  "large": "people who use it now and then, often on a phone"}
SKETCH_FLAGS = ("name", "brand", "audience", "platforms", "feel", "theme", "surfaces")


def normalize_hex(v):
    """'2563eb', '#2563EB' or '#abc' -> '#2563eb'; None when it is not a hex color."""
    if not isinstance(v, str):
        return None
    t = v.strip().lower()
    t = t if t.startswith("#") else "#" + t
    if re.fullmatch(r"#[0-9a-f]{3}", t):
        t = "#" + "".join(c * 2 for c in t[1:])
    return t if re.fullmatch(r"#[0-9a-f]{6}", t) else None


def brand_line(meta, state):
    """One plain line on what happened to the person's brand color (U5 F10): kept exactly, or changed and why."""
    brand = (state.get("raw") or {}).get("brandColor")
    ci = (meta or {}).get("color") or {}
    if not brand:
        return ""
    B = brand.upper()
    if ci.get("pinnedStep"):
        cw = ci.get("brandContrastWhite") or contrast(brand, "#ffffff")
        tail = f"white text on it reads at {cw:.2f}:1" if cw >= ci.get("textMin", 4.5) else "dark text on it, because white text would be too faint"
        return f"Your brand color {B} is on the buttons exactly ({tail})."
    if ci.get("brandPinFailed"):
        adj = (ci.get("brandAdjustedTo") or "").upper()
        cw = ci.get("brandContrastWhite") or contrast(brand, "#ffffff")
        return (f"Your brand color {B} is too {'light' if cw < 3 else 'mid-toned'} for readable button text ({cw:.2f}:1 with white; "
                f"buttons need {ci.get('textMin', 4.5):g}:1), so buttons use {adj}, a {'darker' if luminance(adj) < luminance(brand) else 'lighter'} "
                "shade of it. The exact color stays in color.brand.seed for your logo.")
    if ci.get("brandExact") is False:
        adj = (ci.get("brandAdjustedTo") or "").upper()
        return f"Buttons use {adj}, made from your color {B} (Q-color-01: generate from a seed)."
    return ""


COLOR_WORDS = {"red", "orange", "yellow", "green", "teal", "blue", "navy", "purple", "violet", "pink", "brown", "black", "white", "gray",
               "grey", "gold", "silver", "cyan", "magenta", "maroon", "lime", "indigo", "turquoise", "beige", "cream"}


def cmd_feel(words):
    """Show how plain feel words map onto the twelve feel settings (macros); with no words, list the words it knows."""
    table = (levers().get("feelWords") or {}).get("words") or {}
    if not words:
        by = {}
        for w, ids in sorted(table.items()):
            by.setdefault(", ".join(ids), []).append(w)
        print("Feel words the engine understands (any other word is asked about, never rejected):")
        for ids, ws in sorted(by.items()):
            print(f"  {ids}: {', '.join(ws)}")
        return 0
    macros, mapping, unknown = feel_words(words)
    for w, ids in mapping.items():
        print(f"{w} -> {', '.join(ids)}")
    for w in unknown:
        print(f"{w} -> not known yet: is it closer to playful, calm, bold, friendly or serious?")
    return 0


def cmd_sketch(d, name=None, brand=None, audience=None, platforms=None, feel=None, theme=None, quiet=False, surfaces=None, delegated=None):
    """Level 0: about five answers give a complete, coarse system; everything else stays on defaults.
    Every input is checked before anything is written. delegated names the answers the person left to the model
    ('all' or a comma list of sketch flags); they are recorded as set_by delegated."""
    macros, mapping, unknown = feel_words([w for w in re.split(r"\s*,\s*", feel or "") if w.strip()])
    items = [x.strip() for x in (surfaces or "").split(",") if x.strip()]
    if items and (not surface_list(items) or len(surface_list(items)) != len(items)):
        raise SystemExit(f"--surfaces takes mode words or name:mode pairs; modes are {', '.join(SURFACE_MODES)}.")
    if brand is not None:
        hx = normalize_hex(brand)
        if not hx:
            raise SystemExit(f"--brand takes a hex color like #2563EB; {brand!r} is not one. Nothing was written.")
        brand = hx
    deleg = {x.strip() for x in str(delegated).split(",") if x.strip()} if delegated else set()
    bad = deleg - set(SKETCH_FLAGS) - {"all"}
    if bad:
        raise SystemExit(f"--delegated takes all or a comma list of: {', '.join(SKETCH_FLAGS)}.")

    def sb(flag):
        return "delegated" if ("all" in deleg or flag in deleg) else None
    fresh = not os.path.exists(os.path.join(d, "state.json"))
    if fresh:
        cmd_init(d, name=name)
    elif name and load_state(d).get("name") != name:
        cmd_set(d, "name", name, "sketch: the product's name", quiet=True, set_by=sb("name"))  # --name wins over init's folder name
    why = "sketch: Level 0 answer"
    if audience:
        cmd_set(d, "answers.Q-aud-01", audience, why, quiet=True, set_by=sb("audience"), via="sketch")
        if not (load_state(d).get("context") or {}).get("audience"):
            cmd_set(d, "context.audience", AUDIENCE_WORDS.get(audience, audience), "sketch: plain words for Q-aud-01", quiet=True,
                    set_by=sb("audience") or "assumed")
    if brand:
        cmd_set(d, "raw.brandColor", brand, why, quiet=True, set_by=sb("brand"))
    if platforms:
        cmd_set(d, "answers.Q-plat-01", [p.strip() for p in platforms.split(",") if p.strip()], why, quiet=True, set_by=sb("platforms"),
                via="sketch")
    if macros:
        cmd_set(d, "macros", macros, why + (f" (their words: {', '.join(mapping)})" if mapping else ""), quiet=True, set_by=sb("feel"))
        cmd_set(d, "taste.feelWords", [w.strip("!.?,;: ").lower() for w in mapping], "sketch: the person's own feel words", quiet=True,
                set_by=sb("feel"))
    if theme:
        cmd_set(d, "answers.Q-theme-01", theme, why, quiet=True, set_by=sb("theme"), via="sketch")
    if items:
        cmd_set(d, "answers.Q-scope-06", items if len(items) > 1 or ":" in items[0] else items[0], why, quiet=True, set_by=sb("surfaces"),
                via="sketch")
    code = cmd_build(d) if not quiet else 0
    if not quiet:
        if mapping and any([w] != ids for w, ids in mapping.items()):
            print("Feel: " + "; ".join(f"{w} -> {' + '.join(ids)}" for w, ids in mapping.items()) + ".")
        for w in unknown:
            if w.strip("!.?, ").lower() in COLOR_WORDS:
                print(f"'{w}' is a color, not a feel, so I left it out of the feel. Give the exact color with --brand (a hex such as #2563EB), "
                      "or share your logo and I'll read its colors.")
            else:
                print(f"I don't know the feel word '{w}' yet, so I left it out. Is it closer to playful, calm, bold, friendly or serious?")
        mp = os.path.join(d, "tokens", "opendesigner.meta.json")
        line = brand_line(read_json(mp), load_state(d)) if os.path.exists(mp) else ""
        if line:
            print(line)
        print("This is a sketch: every part works, and most choices are still defaults. Zoom into any area later (see the Zoom lines in DESIGN.md).")
        if code == 0:
            track(d, "level_complete", level="sketch")
            jl = journey.level_line(d, "sketch") if journey else ""
            if jl:
                print(jl)
    return code


TW_PALETTE_HEX = {  # Tailwind v3 palette hexes (v4 uses OKLCH equivalents), to suggest the nearest role token [inferred approximation]
    "slate-50": "#f8fafc", "slate-100": "#f1f5f9", "slate-200": "#e2e8f0", "slate-300": "#cbd5e1", "slate-400": "#94a3b8", "slate-500": "#64748b",
    "slate-600": "#475569", "slate-700": "#334155", "slate-800": "#1e293b", "slate-900": "#0f172a", "slate-950": "#020617",
    "gray-50": "#f9fafb", "gray-100": "#f3f4f6", "gray-200": "#e5e7eb", "gray-300": "#d1d5db", "gray-400": "#9ca3af", "gray-500": "#6b7280",
    "gray-600": "#4b5563", "gray-700": "#374151", "gray-800": "#1f2937", "gray-900": "#111827", "gray-950": "#030712",
    "zinc-100": "#f4f4f5", "zinc-200": "#e4e4e7", "zinc-500": "#71717a", "zinc-700": "#3f3f46", "zinc-900": "#18181b",
    "neutral-100": "#f5f5f5", "neutral-200": "#e5e5e5", "neutral-500": "#737373", "neutral-700": "#404040", "neutral-900": "#171717",
    "red-500": "#ef4444", "red-600": "#dc2626", "red-700": "#b91c1c", "orange-500": "#f97316", "amber-500": "#f59e0b", "yellow-400": "#facc15",
    "green-500": "#22c55e", "green-600": "#16a34a", "emerald-500": "#10b981", "teal-500": "#14b8a6", "cyan-500": "#06b6d4", "sky-500": "#0ea5e9",
    "blue-50": "#eff6ff", "blue-100": "#dbeafe", "blue-500": "#3b82f6", "blue-600": "#2563eb", "blue-700": "#1d4ed8", "indigo-500": "#6366f1",
    "indigo-600": "#4f46e5", "violet-500": "#8b5cf6", "purple-500": "#a855f7", "pink-500": "#ec4899", "rose-500": "#f43f5e"}


REVIEW_EXT = {".css", ".scss", ".sass", ".less", ".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte", ".html", ".swift", ".kt", ".kts"}
REVIEW_SKIP = {"node_modules", ".git", "dist", "build", ".next", "out", "vendor", "coverage", "Pods", ".gradle", "opendesigner",
               "DerivedData", "__pycache__", ".venv", "venv"}
RX_HEX = re.compile(r"(?<![\w&])#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b")
RX_FN = re.compile(r"\b(rgba?|hsla?|oklch)\(\s*[\d.]")
RX_SWIFT_COLOR = re.compile(r"\b(Color|UIColor|NSColor)\(\s*(red|\.sRGB|hue|white)")
RX_KT_COLOR = re.compile(r"\bColor\(\s*0x[0-9A-Fa-f]{6,8}")
RX_SIZE = re.compile(r"\b(padding|margin|gap|row-gap|column-gap|font-size|border-radius|inset|top|left|right|bottom|width|height)"
                     r"(-[a-z]+)?\s*:\s*(-?\d+(?:\.\d+)?)px")
# JSX and JS style objects (U5 F3, F30): borderRadius: 10, padding: '20px', fontSize: 15
RX_JSX_SIZE = re.compile(r"\b(padding(?:Top|Right|Bottom|Left|Inline|Block|X|Y)?|margin(?:Top|Right|Bottom|Left|Inline|Block|X|Y)?|gap|rowGap|"
                         r"columnGap|fontSize|borderRadius|border(?:Top|Bottom)(?:Left|Right)Radius|top|left|right|bottom|inset|width|height)"
                         r"\s*:\s*(['\"`]?)(-?\d+(?:\.\d+)?)(px)?(?:\s|['\"`,}])")
RX_SHADOW = re.compile(r"\b(box-shadow|text-shadow|boxShadow|textShadow)\s*:\s*['\"`]?\s*((?:inset\s+)?-?\d[^;'\"`{}]*)")
RX_DROP_SHADOW = re.compile(r"\bdrop-shadow\(\s*(-?\d[^)]*)\)")
RX_SHADOW_NATIVE = re.compile(r"\.shadow\(\s*(?:color:|radius:\s*\d|elevation\s*=\s*\d|\d+(?:\.\d+)?\.dp)")
RX_MOTION = re.compile(r"\b(transition|transition-duration|animation|animation-duration|transitionDuration|animationDuration)"
                       r"\s*:\s*['\"`]?([^;'\"`{}]*)")
RX_TIME = re.compile(r"(?<![\w.-])(\d*\.?\d+)(ms|s)\b")
RX_SWIFT_ANIM = re.compile(r"\.(easeInOut|easeIn|easeOut|linear|spring|smooth|snappy|bouncy)\(\s*duration:\s*(\d*\.?\d+)")
RX_KT_ANIM = re.compile(r"\b(?:tween\(\s*(?:durationMillis\s*=\s*)?|durationMillis\s*=\s*)(\d+)")
RX_RADIUS_NATIVE = re.compile(r"(cornerRadius\s*[:(]\s*(\d+)|RoundedCornerShape\(\s*(\d+)\.dp|\.padding\(\s*(\d+)\s*\)|(\d+)\.dp\b)")
# Tailwind: arbitrary values (bg-[#2563eb], p-[13px]) and the default scales that bypass the tokens (bg-blue-600, rounded-lg)
RX_TW_CONTEXT = re.compile(r"\b(className|class|clsx|cn|cva|twMerge|tw)\s*[=(`]|@apply\b")
RX_TW_ARB = re.compile(r"(?<![\w\[-])((?:[a-z0-9-]+:)*)(bg|text|border(?:-[trblxy])?|ring|outline|fill|stroke|p[xytrbl]?|m[xytrbl]?|"
                       r"gap(?:-[xy])?|space-[xy]|rounded(?:-[a-z]+)?|shadow|duration|delay|leading|tracking)-\[([^\]\s]+)\]")
TW_HUES = ("slate|gray|zinc|neutral|stone|red|orange|amber|yellow|lime|green|emerald|teal|cyan|sky|blue|indigo|violet|purple|fuchsia|"
           "pink|rose")
RX_TW_PALETTE = re.compile(r"(?<![\w\[-])((?:[a-z0-9-]+:)*)(bg|text|border|ring|outline|fill|stroke|from|to|via|divide|placeholder|decoration|"
                           rf"accent|caret)-(?:({TW_HUES})-(50|[1-9]00|950)|(white|black))(?:/\d+)?(?![\w-])")
RX_TW_RADIUS = re.compile(r"(?<![\w\[-])((?:[a-z0-9-]+:)*)rounded(?:-(none|xs|sm|md|lg|xl|2xl|3xl))?(?![\w\[-])")
RX_TW_SHADOW = re.compile(r"(?<![\w\[-])((?:[a-z0-9-]+:)*)shadow(?:-(2xs|xs|sm|md|lg|xl|2xl|inner))?(?![\w\[-])")
RX_TW_TEXT = re.compile(r"(?<![\w\[-])((?:[a-z0-9-]+:)*)text-(xs|sm|base|lg|xl|[2-9]xl)(?![\w-])")
TW_TEXT_PX = {"xs": 12, "sm": 14, "base": 16, "lg": 18, "xl": 20, "2xl": 24, "3xl": 30, "4xl": 36, "5xl": 48, "6xl": 60, "7xl": 72,
              "8xl": 96, "9xl": 128}
TW_RADIUS_PX = {None: 4, "none": 0, "xs": 2, "sm": 4, "md": 6, "lg": 8, "xl": 12, "2xl": 16, "3xl": 24}
TW_SHADOW_ROLE = {None: "raised", "2xs": "raised", "xs": "raised", "sm": "raised", "md": "floating", "lg": "floating", "xl": "overlay",
                  "2xl": "overlay", "inner": "raised"}
RX_STATUS_WORD = re.compile(r"error|danger|invalid|destructive|delete|remove|warn|success|valid|done|complete|info|notice|alert", re.I)
RX_ACTION_WORD = re.compile(r"button|btn|cta|primary|submit|save|action", re.I)
ROLE_OF_PROP = {"background": "bg", "background-color": "bg", "backgroundcolor": "bg", "bg": "bg", "color": "text", "text": "text",
                "border": "border", "border-color": "border", "bordercolor": "border", "outline": "border", "outline-color": "border",
                "ring": "border", "fill": "icon", "stroke": "icon", "caret-color": "text", "accent-color": "bg"}


def _nearest_color(hx, palette):
    L1 = hex_to_oklch(hx)
    a1 = oklch_to_oklab(*L1)

    def dist(h2):
        a2 = oklch_to_oklab(*hex_to_oklch(h2))
        return sum((x - y) ** 2 for x, y in zip(a1, a2)) ** 0.5
    best = min(palette.items(), key=lambda kv: (round(dist(kv[1]), 3), ROLE_RANK(kv[0]), kv[0]))
    return best[0], dist(best[1])


def ROLE_RANK(path):
    """Tie-break for equally close colors: the primary action first, then accent, text roles, neutrals, status last."""
    order = ("color.bg.action.primary", "color.text.on-action", "color.bg.accent.bold", "color.text.primary", "color.surface.base",
             "color.surface.raised", "color.border.default", "color.icon.default")
    return order.index(path) if path in order else (50 if re.search(r"\.(success|warning|danger|info|discovery)\b", path) else 20)


def _nearest_duration(ms_val, durations):
    """Closest duration token name for a raw time in ms (instant only for 0)."""
    cands = {k: v for k, v in durations.items() if v > 0} or durations
    return min(cands.items(), key=lambda kv: (abs(kv[1] - ms_val), kv[1]))[0]


def _shadow_role(value):
    """Map a raw shadow to the elevation role of the same size: the largest blur decides (DC-L04-10)."""
    nums = [float(x) for x in re.findall(r"(-?\d*\.?\d+)px", value)]
    blur = max((abs(x) for x in nums[2::4] or nums), default=0)  # offset-x offset-y blur spread
    return "raised" if blur <= 4 else "floating" if blur <= 16 else "overlay"


def _prop_before(line, pos):
    """The CSS or JSX property a value belongs to: the last 'name:' before it on the line."""
    m = re.search(r"([A-Za-z-]+)\s*:\s*[^;:{}]*$", line[:pos])
    return m.group(1).lower() if m else ""


def role_palette(light, role, line):
    """Candidate color tokens for a raw color, narrowed by the property's role (U5 F9): backgrounds get bg/surface
    roles, text gets text roles, borders get border roles; status colors only when the line talks about a status."""
    prefixes = {"bg": ("color.bg.", "color.surface."), "text": ("color.text.",), "border": ("color.border.",),
                "icon": ("color.icon.", "color.text.")}.get(role, ("color.surface.", "color.text.", "color.bg.", "color.border.", "color.icon."))
    status_ok = bool(RX_STATUS_WORD.search(line))
    out = {p: hex_of(t["resolved"]) for p, t in light.items() if t["type"] == "color" and p.startswith(prefixes)
           and not (t["resolved"] or {}).get("alpha") and (status_ok or not re.search(r"\.(success|warning|danger|info|discovery)\b", p))
           and not p.startswith(("color.chart.", "color.workflow."))}
    if RX_ACTION_WORD.search(line) and role == "bg":
        out = {k: v for k, v in out.items() if not k.startswith("color.surface.")} or out
    return out


def tw_class_for(path):
    """Tailwind class for a semantic color token (build/tailwind/theme.css naming)."""
    for src, dst in TW_COLOR_MAP:
        if path.startswith(src):
            rest = "-".join(kebab(s_) for s_ in path[len(src):].split("."))
            util = {"color.surface.": "bg", "color.bg.": "bg", "color.text.": "text", "color.border.": "border", "color.icon.": "text"}.get(src, "bg")
            return f"{util}-{dst}{rest}"
    return path


def cmd_review(d, project=None, strict=False, as_json=False, limit=40):
    """End-of-implementation check: hard-coded colors, sizes, radii, shadows and durations that bypass tokens (CSS, JSX style
    objects, Tailwind arbitrary values and default scales, SwiftUI, Compose), role-appropriate token suggestions, and stale
    or untrue DESIGN.md sections."""
    state = merge_defaults(load_state(d))
    files, meta, _ = generate_system(load_state(d))
    prefix = slug(meta.get("prefix") or "ds").replace("-", "")
    if project is None:
        project = os.path.dirname(os.path.abspath(d)) if os.path.basename(os.path.abspath(d)) == DEFAULT_DIR else os.getcwd()
    light = resolve_all(files, {"theme": meta["modes"][0]} if "theme" in files["opendesigner.resolver.json"].get("modifiers", {}) else {})
    ladder = meta["space"]["ladder"]
    radii = {k: v for k, v in (("detail", meta["shape"]["detail"]), ("control", meta["shape"]["control"]),
                               ("container", meta["shape"]["container"]), ("overlay", meta["shape"]["overlay"])) if isinstance(v, int)}
    sizes = meta["type"]["sizes"]
    durations = meta["motion"]["durations"]
    depth_model = meta["elevation"]["model"]
    P, K = prefix.upper(), prefix.capitalize()
    tw_on = os.path.exists(os.path.join(d, "build", "tailwind", "theme.css"))
    tw_reset = (state.get("exports") or {}).get("tailwindReset", True) is not False
    styles_by_size = {}
    for pth, t in light.items():
        if t["type"] == "typography" and not pth.startswith(("text.emphasized.", "text.numeric.")):
            styles_by_size.setdefault(int(_px(t["resolved"]["fontSize"])), pth)

    def color_fix(hx, role, line, tw=False):
        pal = role_palette(light, role, line)
        if not pal:
            return "use a color token"
        tokn, dd = _nearest_color(hx.lower(), pal)
        close = "" if dd <= 0.02 else " (closest match)"
        return (f"use {tw_class_for(tokn)}" if tw else f"use var({css_var(prefix, tokn)})") + close

    def shadow_fix(value, tw=False):
        if depth_model == "borders":
            return f"this system uses borders, not shadows (depth model: borders); use var({css_var(prefix, 'color.border.default')})"
        role = _shadow_role(value)
        return f"use shadow-{role}" if tw else f"use var({css_var(prefix, 'elevation.' + role)})"

    def text_fix(val, tw=False):
        near = min(sizes, key=lambda x: (abs(x - val), x))
        style = styles_by_size.get(near)
        if tw and style:
            return f"use {'text-' + '-'.join(style.split('.')[1:])} (a text style)" + ("" if near == val else f"; {val:g}px is not on the scale")
        return (f"use a text style (for example .{prefix}-{'-'.join(style.split('.'))}) or var({css_var(prefix, 'font.size.' + str(near))})"
                if style else f"use var({css_var(prefix, 'font.size.' + str(near))})")

    def space_fix(val, tw=False):
        near = min(ladder, key=lambda x: (abs(x - val), x))
        sem = next((k for k, v in sorted(meta["density"][meta["params"]["space.densityMode"]["value"]]["inset"].items()) if v == near), None)
        if tw:
            return (f"use p-inset-{sem} / gap-inline-{sem}" if sem else f"use the {near}px step") + ("" if near == val else f" ({val:g} is off the {meta['space']['unit']}px ladder)")
        return f"use var({css_var(prefix, 'space.' + str(near))})" + ("" if near == val else f" ({val:g} is off the {meta['space']['unit']}px ladder)")

    def radius_fix(val, tw=False):
        near = min(radii.items(), key=lambda kv: (abs(kv[1] - val), kv[0])) if radii else None
        if not near:
            return "use a radius token"
        return f"use rounded-{near[0]}" if tw else f"use var({css_var(prefix, 'radius.' + near[0])})"

    def motion_fix(line, v_ms, tw=False):
        feedback = v_ms <= 200 or re.search(r"hover|focus|active|color|background|border|opacity|box-shadow|fill", line, re.I)
        role = "feedback" if feedback else ("enter" if v_ms <= 320 else "expand")
        if tw:
            return "use transition-feedback" if role == "feedback" else f"use duration and easing from motion.transition.{role}"
        return (f"use var({css_var(prefix, 'motion.transition.' + role)}-duration) and its -easing "
                f"(the {role} transition: {'hover, press and color changes' if role == 'feedback' else 'things entering' if role == 'enter' else 'panels and dialogs'})")
    findings, scanned = [], 0
    stateroot = os.path.abspath(d)
    for root, dirs, fnames in os.walk(project):
        dirs[:] = sorted(x for x in dirs if x not in REVIEW_SKIP and not x.startswith("."))
        if os.path.abspath(root).startswith(stateroot):
            continue
        for fn in sorted(fnames):
            ext = os.path.splitext(fn)[1].lower()
            if ext not in REVIEW_EXT:
                continue
            path = os.path.join(root, fn)
            try:
                if os.path.getsize(path) > 1_000_000:
                    continue
                with open(path, encoding="utf-8", errors="ignore") as f:
                    lines = f.readlines()
            except OSError:
                continue
            scanned += 1
            rel = os.path.relpath(path, project)
            jsx = ext in (".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte")
            for i, line in enumerate(lines, 1):
                if re.search(r"^\s*(//|/\*|\*|<!--)", line) or "od-ignore" in line:
                    continue
                if "var(--" in line and not RX_HEX.search(line) and not RX_TW_CONTEXT.search(line):
                    continue
                custom_prop = bool(re.match(r"\s*--", line))  # a custom property definition is a token source, not a bypass
                tw_ctx = bool(RX_TW_CONTEXT.search(line)) or (ext in (".css", ".scss") and "@apply" in line)
                add = lambda kind, value, fix: findings.append({"kind": kind, "file": rel, "line": i, "value": value, "fix": fix})
                # Tailwind arbitrary values and default scales
                spans = []
                if tw_ctx or ext in (".html", ".vue", ".svelte"):
                    for m in RX_TW_ARB.finditer(line):
                        spans.append(m.span())
                        util, val = m.group(2), m.group(3)
                        cls = m.group(0)
                        if val.startswith("#") or val.startswith(("rgb", "hsl", "oklch")):
                            role = "bg" if util == "bg" else "text" if util == "text" else "icon" if util in ("fill", "stroke") else "border"
                            hx = "#" + (val[1:] if len(val) == 7 else "".join(c * 2 for c in val[1:4])) if val.startswith("#") else None
                            add("color", cls, color_fix(hx, role, line, tw=True) if hx and re.fullmatch(r"#[0-9a-fA-F]{6}", hx) else "use a color class from the theme")
                        elif util.startswith("rounded"):
                            mv = re.match(r"(\d+(?:\.\d+)?)px", val)
                            add("radius", cls, radius_fix(float(mv.group(1)), tw=True) if mv else "use rounded-control or rounded-container")
                        elif util == "text":
                            mv = re.match(r"(\d+(?:\.\d+)?)(px|rem)", val)
                            add("size", cls, text_fix(float(mv.group(1)) * (16 if mv.group(2) == "rem" else 1), tw=True) if mv else "use a text style class")
                        elif util == "shadow":
                            add("shadow", cls, shadow_fix(val.replace("_", " "), tw=True))
                        elif util in ("duration", "delay"):
                            mv = RX_TIME.search(val)
                            v_ms = float(mv.group(1)) * (1 if mv.group(2) == "ms" else 1000) if mv else 0
                            add("duration", cls, motion_fix(line, v_ms, tw=True))
                        elif util in ("leading", "tracking"):
                            add("size", cls, "use a text style class; it sets line height and letter spacing together")
                        else:
                            mv = re.match(r"(-?\d+(?:\.\d+)?)(px|rem)", val)
                            add("size", cls, space_fix(float(mv.group(1)) * (16 if mv.group(2) == "rem" else 1), tw=True) if mv else "use a spacing class")
                    if tw_on and tw_ctx:
                        gone = " (it does not exist once Tailwind's defaults are off)" if tw_reset else ""
                        for m in RX_TW_PALETTE.finditer(line):
                            util = m.group(2)
                            hx = TW_PALETTE_HEX.get(f"{m.group(3)}-{m.group(4)}") if m.group(3) else ("#ffffff" if m.group(5) == "white" else "#000000")
                            role = "bg" if util in ("bg", "from", "to", "via", "accent") else "text" if util in ("text", "placeholder", "caret", "decoration") \
                                else "icon" if util in ("fill", "stroke") else "border"
                            add("color", m.group(0), color_fix(hx, role, line, tw=True) + gone if hx else "use a color class from the theme" + gone)
                        for m in RX_TW_RADIUS.finditer(line):
                            add("radius", m.group(0), radius_fix(TW_RADIUS_PX.get(m.group(2), 4), tw=True) + gone)
                        for m in RX_TW_SHADOW.finditer(line):
                            add("shadow", m.group(0), f"use shadow-{TW_SHADOW_ROLE.get(m.group(2), 'raised')}" + gone)
                        for m in RX_TW_TEXT.finditer(line):
                            add("size", m.group(0), text_fix(TW_TEXT_PX[m.group(2)], tw=True) + gone)
                shadow_m = RX_SHADOW.search(line) or RX_DROP_SHADOW.search(line)
                if shadow_m:
                    spans.append(shadow_m.span())
                for m in RX_HEX.finditer(line):  # a raw shadow is replaced whole, color included; other hexes on the line still count
                    if custom_prop or any(a <= m.start() < b for a, b in spans):
                        continue
                    hx = "#" + (m.group(1) if len(m.group(1)) == 6 else "".join(c * 2 for c in m.group(1)))
                    role = ROLE_OF_PROP.get(_prop_before(line, m.start()).replace("_", "-"), None)
                    add("color", hx, color_fix(hx.lower(), role, line))
                if RX_FN.search(line) and not shadow_m and not custom_prop:
                    fm_ = RX_FN.search(line)
                    if not any(a <= fm_.start() < b for a, b in spans):
                        add("color", fm_.group(0) + "...)", "use a color token (var(--" + prefix + "-color-...))")
                if ext == ".swift" and RX_SWIFT_COLOR.search(line):
                    add("color", RX_SWIFT_COLOR.search(line).group(0) + "...)", f"use {P}.Colors.<role> from build/swift/DesignTokens.swift")
                if ext in (".kt", ".kts") and RX_KT_COLOR.search(line) and "DesignTokens" not in rel:
                    add("color", RX_KT_COLOR.search(line).group(0) + ")", f"use Local{K}Colors.current.<role>")
                for m in RX_SIZE.finditer(line):
                    prop, val = m.group(1), float(m.group(3))
                    if val == 0 or (prop in ("width", "height", "top", "left", "right", "bottom", "inset") and val not in ladder):
                        continue
                    if prop == "border-radius":
                        add("radius", f"{prop}: {val:g}px", radius_fix(val))
                    elif prop == "font-size":
                        add("size", f"{prop}: {val:g}px", text_fix(val))
                    else:
                        add("size", f"{prop}: {val:g}px", space_fix(val))
                if jsx and not custom_prop:
                    for m in RX_JSX_SIZE.finditer(line):
                        prop, val = m.group(1), float(m.group(3))
                        if val == 0 or (prop in ("width", "height", "top", "left", "right", "bottom", "inset") and val not in ladder):
                            continue
                        if prop.startswith("border") and prop.endswith("Radius"):
                            add("radius", f"{prop}: {m.group(3)}", radius_fix(val))
                        elif prop == "fontSize":
                            add("size", f"{prop}: {m.group(3)}", text_fix(val))
                        else:
                            add("size", f"{prop}: {m.group(3)}", space_fix(val))
                if shadow_m and not custom_prop:
                    val = shadow_m.group(0)
                    add("shadow", val.strip()[:80], shadow_fix(val))
                m = RX_MOTION.search(line)
                if m and not custom_prop and "infinite" not in m.group(2):  # looping spinners are not on the duration ladder
                    tm = RX_TIME.search(m.group(2))
                    if tm:
                        v_ms = float(tm.group(1)) * (1 if tm.group(2) == "ms" else 1000)
                        if v_ms > 0:
                            near = _nearest_duration(v_ms, durations)
                            if m.group(1) in ("transition", "transitionDuration", "transition-duration"):
                                fix = motion_fix(line, v_ms)
                            else:
                                fix = (f"use var({css_var(prefix, 'motion.duration.' + near)})"
                                       + ("" if durations[near] == v_ms else f" ({durations[near]}ms, the closest step)"))
                            add("duration", f"{m.group(1)}: {tm.group(0)}", fix)
                native = ext in (".swift", ".kt", ".kts") and "DesignTokens" not in rel
                if native and RX_SHADOW_NATIVE.search(line):
                    add("shadow", RX_SHADOW_NATIVE.search(line).group(0) + "...)",
                        "use an elevation token: the raised, floating or overlay shadow in build/swift or build/compose")
                    continue
                if native:
                    ma = RX_SWIFT_ANIM.search(line) if ext == ".swift" else RX_KT_ANIM.search(line)
                    if ma:
                        v_ms = float(ma.group(ma.lastindex)) * (1000 if ext == ".swift" else 1)
                        near = _nearest_duration(v_ms, durations) if v_ms > 0 else "instant"
                        name = camel(["duration", near])
                        add("duration", ma.group(0) + ")", f"use {P}.Motion.{name}" if ext == ".swift" else f"use {K}Motion.{name}Ms")
                        continue
                if native:
                    for m in RX_RADIUS_NATIVE.finditer(line):
                        add("size", m.group(0), f"use {P}.Space / {P}.Radius (Swift) or {K}Space (Compose)")
                        break
    # stale or untrue DESIGN.md / PRODUCT.md sections: render now and compare section by section
    stale, untrue = [], []
    out_dir = os.path.dirname(os.path.abspath(d)) if os.path.basename(os.path.abspath(d)) == DEFAULT_DIR else d
    dm = os.path.join(out_dir, "DESIGN.md")
    if os.path.exists(dm):
        with open(dm, encoding="utf-8") as f:
            cur = f.read()
        fresh = render_design_md(d, files, meta, state, cur)

        def secs(text):
            return {x.split("\n", 1)[0].strip(): x for x in re.split(r"^## ", text, flags=re.M)[1:]}
        a, b = secs(cur), secs(fresh)
        stale = [t for t in b if a.get(t) != b[t]]
        missing = [t for t in b if t not in a]
        answered = answered_ids(state)
        for fname in ("DESIGN.md", "PRODUCT.md"):
            fp = os.path.join(out_dir, fname)
            if os.path.exists(fp):
                with open(fp, encoding="utf-8") as f:
                    for q in re.findall(r"not recorded yet \((Q-[a-z]+-\d+)\)", f.read(), flags=re.I):
                        if q in answered:
                            untrue.append(f"{fname} says {q} is not recorded, but it was answered")
    else:
        missing = ["DESIGN.md"]
    by = {}
    for f_ in findings:
        by[f_["kind"]] = by.get(f_["kind"], 0) + 1
    result = {"project": project, "filesScanned": scanned, "counts": by, "findings": findings[:500], "staleSections": stale,
              "missing": missing, "untrue": sorted(set(untrue))}
    if as_json:
        print(json.dumps(result, indent=2))
    else:
        total = len(findings)
        print(f"Review of {project}: {scanned} files scanned.")
        if not scanned:
            print("No code yet, so there is nothing to check.")
        elif total:
            print(f"{total} hard-coded value{'s' if total != 1 else ''} skip the tokens: "
                  + ", ".join(f"{n} {k}{'s' if n != 1 else ''}" for k, n in sorted(by.items())) + ".")
            for f_ in findings[:limit]:
                print(f"  {f_['file']}:{f_['line']}  {f_['value']}  ->  {f_['fix']}")
            if total > limit:
                print(f"  ... and {total - limit} more (use --json for all).")
            print("  To keep a raw value on purpose, add the comment od-ignore on that line.")
        else:
            print("No hard-coded colors, sizes, radii, shadows or durations found: the code uses the tokens.")
        for u in sorted(set(untrue)):
            print(f"Untrue: {u}. Fix: run `engine.py design-md`.")
        if missing == ["DESIGN.md"]:
            print("DESIGN.md is missing. Run `engine.py design-md`.")
        elif stale:
            print(f"DESIGN.md is out of date in {len(stale)} section{'s' if len(stale) != 1 else ''}: {', '.join(stale)}. "
                  "Fix: run `engine.py design-md`. Notes inside od:keep blocks are kept.")
        elif not untrue:
            print("DESIGN.md matches state.json.")
    track(d, "review")
    return 1 if strict and (findings or stale or missing or untrue) else 0


# =============================================================================================
# show: fill a visual template with real values from the current state (U5 F19, F34)
# =============================================================================================

TEMPLATE_QUESTIONS = {"palette": ("Q-color-03", ["tonal", "vivid", "monochrome", "expressive"]),
                      "type-scale": ("Q-type-09", ["1.2", "1.25", "1.333"]),
                      "spacing-ruler": ("Q-space-01", ["4-grid-8-rhythm", "8"]),
                      "radius": ("Q-shape-01", ["square", "subtle", "soft", "pill"]),
                      "elevation": ("Q-depth-01", ["borders", "ring-shadow", "tonal", "shadow"]),
                      "motion": ("Q-motion-01", ["productive", "two-mode", "springs"]),
                      "component-sheet": ("Q-dir-01", []),
                      "option-gallery": ("Q-dir-01", ["flat2", "tonal", "glass"])}


def what_if(state, qid=None, value=None):
    """A generated system for the state with one answer applied; the state on disk is never touched."""
    s2 = merge_defaults(copy.deepcopy(state))
    if qid:
        s2.setdefault("answers", {})[qid] = {"value": value, "set_by": "chosen"}
        for pth, v in answer_effects(qid, value, s2).items():
            _store(s2, pth, v, "chosen", "what-if", False)
    files, meta, ctx = generate_system(s2)
    return files, meta, s2


def _css_shadow(val):
    layers = val if isinstance(val, list) else [val]
    out = []
    for lay in layers:
        for sub in (lay if isinstance(lay, list) else [lay]):
            if not isinstance(sub, dict):
                continue
            col = css_color(sub["color"]) if isinstance(sub.get("color"), dict) else "transparent"
            nums = " ".join(f"{fmt_num(_px(sub[k]))}px" for k in ("offsetX", "offsetY", "blur", "spread"))
            if any(_px(sub[k]) for k in ("offsetY", "blur", "spread")):
                out.append(("inset " if sub.get("inset") else "") + f"{nums} {col}")
    return ", ".join(out) or "none"


def template_vars(files, meta):
    """The --t-* variables the component-sheet and option-gallery templates read, from generated tokens."""
    res = files["opendesigner.resolver.json"]
    mods = res.get("modifiers", {})
    dens = meta["density"][meta["params"]["space.densityMode"]["value"]]
    base = resolve_all(files, {})
    fam = base["font.family.text"]["resolved"]
    shared = {"font": ", ".join(f'"{f}"' if " " in f else f for f in (fam if isinstance(fam, list) else [fam])),
              "size": f"{meta['type']['base']}px", "radius-control": f"{meta['shape']['control'] if meta['shape']['control'] != 'full' else 999}px",
              "radius-container": f"{meta['shape']['container']}px", "control-h": f"{dens['control']['md']}px",
              "pad-x": f"{dens['inset']['lg']}px", "gap": f"{dens['stack']['md']}px", "ratio": str(meta["type"]["ratio"]),
              "heading-weight": str(meta["type"]["weights"]["heading"])}
    out = {"shared": shared}
    for mode in (meta.get("modes") or ["light"]):
        fl = resolve_all(files, {"theme": mode} if "theme" in mods else {})
        H = lambda p: hex_of(fl[p]["resolved"]) if p in fl else None
        v = {"bg": H("color.surface.base"), "surface": H("color.surface.raised"), "surface-2": H("color.bg.neutral.subtle"),
             "fg": H("color.text.primary"), "fg-muted": H("color.text.secondary"), "border": H("color.border.subtle"),
             "border-strong": H("color.border.strong"), "accent": H("color.bg.action.primary"), "accent-hover": H("color.bg.action.primary-hover"),
             "accent-pressed": H("color.bg.action.primary-pressed"), "on-accent": H("color.text.on-action"), "accent-subtle": H("color.bg.accent.subtle"),
             "focus": H("color.border.focus"), "danger": H("color.bg.danger.bold"), "on-danger": H("color.text.on-danger"),
             "danger-subtle": H("color.bg.danger.subtle"), "success-subtle": H("color.bg.success.subtle"), "on-success-subtle": H("color.text.success"),
             "warning-subtle": H("color.bg.warning.subtle"), "on-warning-subtle": H("color.text.warning"),
             "shadow-1": _css_shadow(fl["elevation.raised"]["resolved"]) if "elevation.raised" in fl else "none",
             "shadow-2": _css_shadow(fl["elevation.floating"]["resolved"]) if "elevation.floating" in fl else "none"}
        out[mode] = {k: x for k, x in v.items() if x}
    if "dark" not in out:
        out["dark"] = dict(out.get("light", {}))
    return out


def build_payload(state, template):
    """The od-data payload for one template, from the current state and what-if copies (one per option)."""
    if template not in TEMPLATE_QUESTIONS:
        raise SystemExit(f"unknown template {template!r}; choose one of: {', '.join(TEMPLATE_QUESTIONS)}")
    qid, values = TEMPLATE_QUESTIONS[template]
    cur = answer_value((state.get("answers") or {}).get(qid)) if (state.get("answers") or {}).get(qid) else None
    name = state.get("name") or "Your product"
    q = questions().get(qid) or {}
    label = lambda v: option_label(qid, v) or str(v)
    fixed = sorted(k for k, v in (state.get("dials") or {}).items() if dial_value(v) is not None)
    note_fixed = (f" Your earlier answers fix {', '.join(fixed)}, so the options differ in the rest." if fixed else "")
    payload = {"question": qid, "recommended": str(cur or q.get("default_value") or (values[0] if values else "")),
               "generatedBy": f"engine.py show {template} (OpenDesigner engine {ENGINE_VERSION}); real values from {name}'s state"}
    if template == "palette":
        payload.update(title=f"{name}: how colorful", subtitle="Each option is your palette, built for real. The shades go from light to dark; "
                       "the number under each is its contrast with the first shade." + note_fixed, options=[])
        for v in values:
            files, meta, s2 = what_if(state, qid, v)
            ramps = [{"name": n, "light": meta["ramps"][n]["light"]["hex"], "dark": meta["ramps"][n]["dark"]["hex"]}
                     for n in ("accent", "accent2", "neutral") if n in meta["ramps"]]
            ci_ = meta["color"]
            note = {"monochrome": "almost no color", "neutral": "a little color", "tonalSpot": "calm color", "expressive": "strong color",
                    "vibrant": "the strongest color"}.get(ci_["scheme"], ci_["scheme"])
            note += f", {ci_.get('accentCount', 1)} accent{'s' if ci_.get('accentCount', 1) != 1 else ''}"
            note += "; your brand color exactly on buttons" if ci_.get("pinnedStep") else (f"; buttons {ci_.get('brandAdjustedTo')}" if ci_.get("brandAdjustedTo") else "")
            payload["options"].append({"value": v, "label": label(v), "note": note, "ramps": ramps})
    elif template == "type-scale":
        files, meta, s2 = what_if(state)
        payload.update(title=f"{name}: text sizes", subtitle="Your body size with three ratios. Each size is the one below it times the ratio, "
                       "rounded to whole pixels.", options=[{"value": v, "label": label(v), "note": {"1.2": "calm, dense screens", "1.25": "balanced",
                                                                                                     "1.333": "expressive, marketing"}[v],
                                                          "base": meta["type"]["base"], "ratio": float(v)} for v in values],
                       adjust={"base": "OD:set raw.baseSize={v}", "ratio": "OD:set Q-type-09={v}"},
                       sample={"persuade": f"{name}: join us", "finance": "Bills due this week", "read": f"Getting started with {name}"}.get(
                           preview_kind(state), "Users waiting for review"), fontHref=None)
    elif template == "spacing-ruler":
        payload.update(title=f"{name}: spacing steps", subtitle="The ruler is drawn at real size. Red dashes mark padding; red numbers mark gaps.",
                       options=[])
        for v in values:
            files, meta, s2 = what_if(state, qid, v)
            lad = [x for x in meta["space"]["ladder"] if x > 0][:9]
            dens = meta["density"][meta["params"]["space.densityMode"]["value"]]
            payload["options"].append({"value": v, "label": label(v), "note": f"{meta['space']['unit']}px unit",
                                       "steps": [{"name": str(i + 1), "px": x} for i, x in enumerate(lad)],
                                       "demo": {"pad": str(min(4, len(lad))), "gap": str(min(3, len(lad))), "inner": "1"},
                                       "controls": dens["control"]})
    elif template == "radius":
        files, meta0, _s = what_if(state)
        fl = resolve_all(files, {"theme": "light"} if "theme" in files["opendesigner.resolver.json"].get("modifiers", {}) else {})
        payload.update(title=f"{name}: corners", subtitle="Pick a style, or drag the Roundness dial. Cards get about 1.5 times the button corners.",
                       options=[], dial={"line": "OD:set dials.roundness={v}", "value": meta0["dials"]["roundness"],
                                         "bands": lever_index()["radius.control"]["map"]["bands"]},
                       surface={"light": [hex_of(fl["color.surface.raised"]["resolved"]), hex_of(fl["color.text.primary"]["resolved"])],
                                "dark": [hex_of(fl["color.surface.raised"]["resolved"]), hex_of(fl["color.text.primary"]["resolved"])]})
        for v in values:
            files, meta, s2 = what_if(state, qid, v)
            c = meta["shape"]["control"]
            payload["options"].append({"value": v, "label": label(v), "note": f"buttons {c if c != 'full' else 'pill'}{'px' if c != 'full' else ''}",
                                       "radii": {"control": 9999 if c == "full" else c, "container": meta["shape"]["container"]}})
    elif template == "elevation":
        payload.update(title=f"{name}: depth", subtitle="Three surfaces on the page, then every level with its exact CSS." + note_fixed, options=[])
        for v in values:
            files, meta, s2 = what_if(state, qid, v)
            levels = {}
            for mode in meta.get("modes") or ["light"]:
                fl = resolve_all(files, {"theme": mode} if "theme" in files["opendesigner.resolver.json"].get("modifiers", {}) else {})
                row = [{"name": "0", "border": f"1px solid {hex_of(fl['color.border.subtle']['resolved'])}"}]
                for i, e in enumerate(("raised", "floating", "overlay"), 1):
                    sh = _css_shadow(fl[f"elevation.{e}"]["resolved"])
                    ent = {"name": str(i), "shadow": sh} if sh != "none" else {"name": str(i), "border": f"1px solid {hex_of(fl['color.border.default']['resolved'])}"}
                    if mode == "dark":
                        ent["bg"] = hex_of(fl["color.surface." + ("raised" if i == 1 else "overlay")]["resolved"])
                    row.append(ent)
                levels[mode] = row
            payload["options"].append({"value": v, "label": label(v), "note": meta["elevation"]["model"], "levels": levels})
    elif template == "motion":
        payload.update(title=f"{name}: motion", subtitle="Press Play to feel each option. Things leave a little faster than they arrive.", options=[])
        for v in values:
            files, meta, s2 = what_if(state, qid, v)
            mo = meta["motion"]
            payload["options"].append({"value": v, "label": label(v), "note": "springs throughout" if v == "springs" else "no overshoot",
                                       "durations": {"short": mo["durations"]["short"], "medium": mo["durations"]["medium"], "long": mo["durations"]["long"]},
                                       "easing": {k: css_bezier(mo[k]) for k in ("standard", "enter", "exit")}})
    elif template == "component-sheet":
        files, meta, s2 = what_if(state)
        pid = effective_preset(state)[0] or "custom"
        payload.update(title=f"{name}: components", subtitle="Every part here uses only your tokens. Hover, press Tab to move the focus, "
                       "and flip the switch.", recommended=pid,
                       options=[{"value": pid, "label": f"{name} as it is now", "note": brand_line(meta, s2) or "", "vars": template_vars(files, meta)}])
    elif template == "option-gallery":
        payload.update(title=f"{name}: three directions", subtitle="Each direction is built for real from your answers. Pick one, or take one "
                       "part from another. The logo spot stays empty on purpose." + note_fixed, remix=["color", "type", "shape", "depth"], options=[])
        for v in values:
            files, meta, s2 = what_if(state, qid, v)
            dw = {k: meta["dials"][k] for k in ("roundness", "depth", "colorfulness", "energy")}
            payload["options"].append({"value": v, "label": label(v),
                                       "summary": f"{meta['elevation']['model']} depth, corners {meta['shape']['control']}, "
                                                  f"{meta['color']['scheme']} color, body {meta['type']['base']}px.",
                                       "safe": [f"Contrast passes in light and dark ({meta['color']['textMin']}:1 text)"],
                                       "risks": ([{"what": "Glass on bars", "gain": "depth and polish", "cost": "can hide content; needs solid fallbacks"}]
                                                 if v == "glass" else []),
                                       "dials": dw, "vars": template_vars(files, meta)})
    return payload


def cmd_show(d, template, out=None, open_=False, as_json=False):
    """Fill assets/templates/<template>.html with the current state (show.py's od-data substitution) and write it."""
    state = merge_defaults(load_state(d))
    name = template[:-5] if template.endswith(".html") else template
    payload = build_payload(state, name)
    if as_json:
        print(json.dumps(payload, indent=1, ensure_ascii=False))
        return payload
    tdir = os.path.join(SKILL_ROOT, "assets", "templates")
    tpath = os.path.join(tdir, f"{name}.html")
    if not os.path.exists(tpath):
        raise SystemExit(f"no template at {tpath}")
    with open(tpath, encoding="utf-8") as f:
        html = f.read()
    blob = json.dumps(payload, indent=1, ensure_ascii=False).replace("</", "<\\/")
    html = html.replace(">Acme<", f">{_esc(state.get('name') or 'Your product')}<")  # the templates' stand-in name
    html, n = re.subn(r'(<script type="application/json" id="od-data">).*?(</script>)',
                      lambda m: m.group(1) + "\n" + blob + "\n" + m.group(2), html, count=1, flags=re.S)
    if n != 1:
        raise SystemExit("template has no od-data block")
    dest = os.path.join(out or os.path.join(d, "preview"), f"{name}.html")
    write_text(dest, html)
    print(f"wrote {dest}")
    if open_:
        webbrowser.open("file://" + os.path.abspath(dest))
    return dest


FEEDBACK_KINDS = {"gap": "gap", "bug": "bug", "confusing": "confusing", "idea": "enhancement"}
ISSUES_URL = "https://github.com/ckryptickunal/OpenDesigner/issues/new"


def cmd_feedback(d, text, kind="idea", quiet=False, area=None, question=None):
    """Record feedback locally and print a pre-filled issue link. Nothing is posted: the person decides."""
    from urllib.parse import quote
    if kind not in FEEDBACK_KINDS:
        raise SystemExit(f"--kind must be one of {', '.join(FEEDBACK_KINDS)}")
    text = " ".join(str(text).split())
    if not text:
        raise SystemExit("Add the feedback text, in quotes.")
    fp = os.path.join(d, "feedback.md")
    if not os.path.exists(fp):
        write_text(fp, "# Feedback\n\nGaps, bugs, confusing steps and ideas found while using OpenDesigner. Each entry has a ready-to-file "
                       "issue link. Nothing is posted unless you open the link and submit it yourself.\n")
    title = f"[{kind}]" + (f"[{area}]" if area else "") + f" {text[:70]}" + ("..." if len(text) > 70 else "")
    where = ", ".join(x for x in (f"area {area}" if area else "", f"question {question}" if question else "") if x)
    body = (f"**Kind:** {kind}\n\n" + (f"**Where:** {where}\n\n" if where else "") + f"**What happened or what is missing:**\n{text}\n\n"
            f"**Engine:** {ENGINE_VERSION} (Python {sys.version_info.major}.{sys.version_info.minor})\n\n"
            "_Filed from `engine.py feedback`. Please remove anything private before submitting._")
    url = f"{ISSUES_URL}?title={quote(title)}&body={quote(body)}&labels={quote(FEEDBACK_KINDS[kind] + ',from-engine')}"
    with open(fp, encoding="utf-8") as f:
        n = sum(1 for line in f if line.startswith("## F-"))
    with open(fp, "a", encoding="utf-8", newline="\n") as f:
        f.write(f"\n## F-{n + 1:03d} · {_dt.date.today().isoformat()} · {kind}" + (f" · {where}" if where else "")
                + f"\n{text}\n\n[File this as an issue]({url})\n")
    track(d, "feedback_filed", kind=kind, step=question)
    if not quiet:
        print(f"Saved to {fp}.")
        print("To report it, open this link, check it, and submit it yourself (nothing was posted):")
        print(url)
    return url


if __name__ == "__main__":
    sys.exit(main())
