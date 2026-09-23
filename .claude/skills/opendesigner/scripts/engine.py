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
    engine.py feedback "text" --kind gap|bug|confusing|idea    local note + a pre-filled issue link (never posts)
    engine.py build                       generate + export all + design-md + preview + validate

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


DEFAULT_COMPONENTS = [
    "button", "icon-button", "link", "text-field", "textarea", "select", "checkbox", "radio", "switch",
    "card", "dialog", "menu", "tooltip", "toast", "tabs", "table", "badge", "avatar", "banner", "progress",
    "skeleton", "navigation",
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
    raw["flags"] = {"brandExact": False, "tintTowardBrand": False, "motionOff": False, "darkMode": True}
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
        "exports": {"prefix": "ds", "figmaPlan": "professional"},
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


def resolve_dials(state):
    """Effective dial values. Order: explicit value > preset > coupling/default; then macro offsets on
    untouched dials; clamp 0-100. Touching a dial detaches it from coupling and macros (LEVERS A0, A9)."""
    L = levers()
    explicit = {k: dial_value(v) for k, v in (state.get("dials") or {}).items() if dial_value(v) is not None}
    preset = None
    if state.get("preset"):
        preset = next((p for p in L["presets"] if p["id"] == state["preset"]), None)
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


def build_palette(state, params):
    raw = state["raw"]
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
    if raw.get("flags", {}).get("brandExact") and brand:
        peak = max(peak, brand_hct)  # Material Fidelity: the ramp peaks at the brand's own chroma (S-L06-083)
    tint = params["color.neutral.tint.oklch"]
    n_c, n_h = float(tint.get("c") or 0.0), tint.get("h")
    if raw.get("flags", {}).get("tintTowardBrand"):
        n_h = bH
        n_c = max(n_c, 0.012)  # [inferred] minimum visible tint when the flag is on
    if raw.get("neutralBase"):
        nL, nC, nH = hex_to_oklch(raw["neutralBase"])
        n_h, n_c = nH, min(max(nC, 0.0), 0.05)
    n_h = float(n_h if n_h is not None else 0.0)
    if n_c < 0.0005:
        n_c = 0.0

    def neutral_chroma(step, L):
        c = n_c * NEUTRAL_CURVE[step - 1]
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
    exact = bool(raw.get("flags", {}).get("brandExact"))

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

    pin_ok = bool(brand and exact and (contrast(brand, "#ffffff") >= text_min
                                       or contrast_y(luminance(brand), dark_text_y) >= text_min))

    # status hues stay recognizable at any colorfulness; Material's fixed error palette uses chroma 84 [inferred]
    status_peak = clamp(peak + 16, 48.0, 84.0)
    specs = []  # (name, hue, peak, text_on_solid, seed(L,C,H) or None, seed_hex)
    specs.append(("accent", bH, peak, solid_text_for(brand, bL, pin_ok), (bL, bC, bH) if brand else None, brand))
    pac = raw.get("primaryActionColor")
    if pac:
        pL, pC, pH = hex_to_oklch(pac)
        specs.append(("action", pH, max(peak, hct_chroma_of_hex(pac) if raw.get("flags", {}).get("brandExact") else peak),
                      solid_text_for(pac, pL), (pL, pC, pH), pac))
    if params["color.accentCount"] >= 3:
        sec = raw.get("secondaryColors") or []
        if len(sec) >= 1:
            s1 = hex_to_oklch(sec[0])
            specs.append(("accent2", s1[2], peak, solid_text_for(sec[0], s1[0]), s1, sec[0]))
        else:  # Material TonalSpot: tertiary hue +60, chroma 24/36 of primary [inferred mapping S-L01-010]
            specs.append(("accent2", (bH + 60) % 360, peak * 24 / 36, "light", None, None))
        if len(sec) >= 2:
            s2 = hex_to_oklch(sec[1])
            specs.append(("accent3", s2[2], peak, solid_text_for(sec[1], s2[0]), s2, sec[1]))
        else:
            specs.append(("accent3", (bH - 60) % 360, peak * 24 / 36, "light", None, None))
    for sname, (h, sl, tos) in STATUS.items():
        specs.append((sname, float(h), status_peak, tos, (sl, 0.15, float(h)), None))

    ramps = {}
    for mode in ("light", "dark"):
        cfg = {"text_min": text_min, "c12": 17.5 if aaa else 15.5, "dark_base_y": params.get("color.dark.baseY", DARK_STEP1_Y)}
        if mode == "dark":
            cfg["c12"] = 17.0 if aaa else 15.0
        neutral = build_ramp("neutral", mode, n_h, neutral_chroma, "light", cfg)
        ramps[("neutral", mode)] = neutral
        acfg = dict(cfg, c12=14.0 if aaa else 12.5)
        for name, hue, pk, tos, seed, seed_hex in specs:
            r = build_ramp(name, mode, hue, accent_chroma_fn(pk, hue, mode), tos, acfg, neutral=neutral, seed=seed)
            ramps[(name, mode)] = r
    # brand exact: pin the brand hex at the nearest-lightness step of the light accent ramp (Material Fidelity)
    pinned = None
    if pin_ok:  # the exact brand hex becomes the light-mode solid (container role, Material Fidelity)
        acc = ramps[("accent", "light")]
        pinned = 9
        acc.steps[pinned] = {"L": bL, "C": bC, "H": bH, "hex": brand.lower(), "y": luminance(brand), "want": bC}
        acc.pinned = pinned
    # nearest step to the brand color (documented anchor; bg.brand uses a step that carries its on-color)
    anchor = None
    if brand:
        acc = ramps[("accent", "light")]
        anchor = min(range(1, 13), key=lambda i: (abs(acc.steps[i]["L"] - bL), i))
    for r in ramps.values():
        for i in range(1, 13):
            v = p3_variant(r.steps[i]) if r.name != "neutral" and not (r.pinned == i) else None
            if v:
                r.p3[i] = v
    info = {"scheme": scheme, "peakHct": rnd(peak, 2), "brandHct": rnd(brand_hct, 2), "placeholderBrand": placeholder,
            "brandOklch": [rnd(bL, 4), rnd(bC, 4), rnd(bH, 2)], "neutralTint": {"c": rnd(n_c, 4), "h": rnd(n_h, 2)},
            "pinnedStep": pinned, "brandAnchorStep": anchor,
            "brandPinFailed": bool(brand and exact and not pin_ok), "statusPeakHct": rnd(status_peak, 2),
            "textMin": text_min, "ramps": [s[0] for s in specs]}
    return ramps, info


# =============================================================================================
# Token assembly
# =============================================================================================

DENSITIES = ("spacious", "comfortable", "compact")
def space_multipliers():
    """LEVERS B8 multiplier list parsed from levers.json; x24 (the 96 step) added per the spec (6.2, section 11)."""
    m = re.search(r"\[([0-9.,\s]+)\]", levers()["formulas"]["space"]["ladder"])
    mult = [float(x) for x in m.group(1).split(",")] if m else [0, 0.5, 1, 1.5, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20]
    if 24 not in mult:
        mult.append(24.0)
    return mult
SNAP_RADII = [0, 2, 4, 6, 8, 12, 16, 20, 24, 28, 32]
FULL = 9999
SYSTEM_SANS = ["system-ui", "-apple-system", "Segoe UI", "Roboto", "Helvetica Neue", "Arial", "sans-serif"]
SYSTEM_MONO = ["ui-monospace", "SF Mono", "Menlo", "Consolas", "Liberation Mono", "monospace"]
TARGETS = {"pointer": 24, "touch": 44, "touch-android": 48, "remote": 66, "gaze": 60, "vehicle": 76}
TARGET_GAPS = {"pointer": 8, "touch": 12, "gaze": 16, "vehicle": 23, "remote": 16}


class Ctx:
    def __init__(self, state):
        self.state = merge_defaults(copy.deepcopy(state))
        self.raw = self.state["raw"]
        self.flags = self.raw.get("flags", {})
        self.dials, self.dial_src, self.conflicts = resolve_dials(self.state)
        self.params, self.pmeta = derive_params(self.state, self.dials)
        self.ramps, self.cinfo = build_palette(self.state, self.params)
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
             "info": "Status: info. Always paired with an icon or label (DC-L01-15)."}
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
                sub["solidPressed"] = tok(color_value(r.steps[13]), "Pressed state of a light solid that carries dark text.")
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
    color["neutralAlpha"] = alpha
    opacity = {
        "$type": "number",
        "$description": "State and disabled opacities for colors unknown at design time (Material state layers, DC-L01-17).",
        "state": {"hover": tok(0.08), "focus": tok(0.10), "pressed": tok(0.10), "drag": tok(0.16)},
        "disabled": {"container": tok(0.12), "content": tok(0.38)},
        "$extensions": {NS: {"evidence": ["DC-L01-17", "S-L01-005", "S-L01-064"]}},
    }
    return {"color": color}, {"opacity": opacity}


def build_color_semantic(ctx, mode):
    L = mode == "light"
    p = ctx.params
    has = set(ctx.cinfo["ramps"])
    n = lambda s: A(f"color.neutral.{mode}.{s}")
    r = lambda name, s: A(f"color.{name}.{mode}.{s}")
    white = A("color.white")
    model = ctx.P("elevation.model", p["elevation.model"])
    # surfaces: dark raises surfaces by lightness (DC-L04-13); tonal light steps the page down one step
    if L:
        if model == "tonal":
            surf = {"sunken": n(3), "base": n(2), "raised": n(1), "overlay": white}
        else:
            surf = {"sunken": n(2), "base": n(1), "raised": white, "overlay": white}
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
    pressed = lambda name: r(name, "solidPressed") if (L and 13 in ctx.ramp(name, mode).steps) else r(name, 11)
    focus_step = 9 if (lt("accent") == "light") else 11
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
            "onAccent": tok(on("accent"), "Text and icons on color.bg.accent.bold* (auto-picked light or dark, S-L06-094)."),
        },
        "bg": {
            "neutral": {
                "subtle": tok(n(3) if L else n(5), "Secondary buttons, chips, hovered rows."),
                "subtleHover": tok(n(4) if L else n(6), "Hover: +1 step (DC-L01-17)."),
                "subtlePressed": tok(n(5) if L else n(7), "Pressed or selected: +2 steps (DC-L01-17)."),
            },
            "accent": {
                "subtle": tok(r("accent", 3), "Selected rows, accent badges."),
                "subtleHover": tok(r("accent", 4), "Hover on accent subtle fills."),
                "subtlePressed": tok(r("accent", 5), "Pressed accent subtle fills."),
                "bold": tok(r("accent", 9), "Solid accent fill."),
                "boldHover": tok(r("accent", 10), "Hover on the solid accent (+1 step)."),
                "boldPressed": tok(pressed("accent"), "Pressed solid accent (+2 steps)."),
            },
            "disabled": tok(n(3) if L else n(4), "Disabled control fill."),
            "inverse": tok(n(12), "Tooltips and toasts: the inverted surface."),
        },
        "border": {
            "subtle": tok(n(6), "Dividers and card edges (decorative)."),
            "default": tok(n(7), "Outline buttons and table grids (decorative; the label carries meaning)."),
            "strong": tok(n(8), "Boundaries that are the only cue: inputs, checkboxes, switches (3:1, WCAG 1.4.11)."),
            "input": tok(n(8), "Text field and select borders (3:1, DC-L01-16)."),
            "focus": tok(r("accent", focus_step) if L else r("accent", 11), "Focus ring (3:1 against every surface, DC-L04-09)."),
            "accent": tok(r("accent", 8), "Selected card or accent outline."),
        },
        "icon": {
            "default": tok(n(11), "Icons beside text; same color as secondary text (DC-L05-08)."),
            "subtle": tok(n(10), "Decorative icons."),
            "accent": tok(r("accent", 11), "Selected and interactive icons."),
            "onAccent": tok(on("accent"), "Icons on solid accent fills."),
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
    if ctx.cinfo["scheme"] == "monochrome":
        act = (n(12), n(11), n(10) if L else n(10)), (white if L else n(1))
        act_desc = "Primary action (monochrome scheme: neutral ink, as shadcn/ui)."
    elif "action" in has:
        act = (r("action", 9), r("action", 10), pressed("action")), on("action")
        act_desc = "Primary action from its own color input."
    else:
        act = (r("accent", 9), r("accent", 10), pressed("accent")), on("accent")
        act_desc = "Primary action. One per view (DC-L15-03, L15 P08)."
    out["bg"]["action"] = {"primary": tok(act[0][0], act_desc), "primaryHover": tok(act[0][1], "Primary action hover."),
                           "primaryPressed": tok(act[0][2], "Primary action pressed.")}
    out["text"]["onAction"] = tok(act[1], "Text on the primary action fill.")
    brand_step = ctx.cinfo["pinnedStep"] or 9
    out["bg"]["brand"] = tok(r("accent", brand_step) if L else r("accent", 9),
                             "Brand fill for signature surfaces; carries text.onBrand (brandAnchor rule, DC-L01-09).")
    out["text"]["onBrand"] = tok(on("accent"), "Text on color.bg.brand.")
    for extra in ("accent2", "accent3"):
        if extra in has:
            out["bg"][extra] = {"subtle": tok(r(extra, 3), f"{extra} subtle fill."), "bold": tok(r(extra, 9), f"{extra} solid fill.")}
            out["text"][extra] = tok(r(extra, 11), f"{extra} text.")
            out["text"]["on" + extra[0].upper() + extra[1:]] = tok(on(extra), f"Text on {extra} solid.")
    surfaces_mode = p["color.surfaces"]
    if surfaces_mode in ("tinted-containers", "brand-or-dynamic-surfaces"):
        out["surface"]["tinted"] = tok(r("accent", 2), "Tinted container (Colorfulness 50+, L09 X rubric).")
    for s in ("success", "warning", "danger", "info"):
        out["bg"][s] = {"subtle": tok(r(s, 3), f"{s.title()} banner and badge background."),
                        "bold": tok(r(s, 9), f"{s.title()} solid fill."),
                        "boldHover": tok(r(s, 10), f"{s.title()} solid hover.")}
        out["text"][s] = tok(r(s, 11), f"{s.title()} text and icons; pair with an icon or label (DC-L01-15).")
        out["text"]["on" + s.title()] = tok(on(s), f"Text on bg.{s}.bold.")
        out["border"][s] = tok(r(s, 8), f"{s.title()} boundary, for example an invalid field (3:1).")
    if ctx.raw.get("focusColor"):
        out["border"]["focus"] = tok(A("color.focus.custom"), "Focus ring from the raw focus color (L09 M12).")
        out["border"]["focusInner"] = tok(n(12), "Inner ring of the two-tone focus indicator; keeps 3:1 when the custom color alone does not.")
    scrim_alpha = 0.45 if L else 0.6
    shadow_base = ctx.ramp("neutral", "light").steps[12]["hex"] if L else "#000000"
    a = shadow_alpha(ctx)
    k = 1 if L else 2  # dark mode doubles shadow opacity (DC-L04-12)
    ring_hex = ctx.ramp("neutral", "dark").steps[12]["hex"]
    out["overlay"] = {"scrim": tok(srgb_value(ctx.ramp("neutral", "light").steps[12]["hex"] if L else "#000000", scrim_alpha),
                                   "Modal backdrop (DC-L04-18).")}
    out["shadow"] = {
        "key": tok(srgb_value(shadow_base, min(0.6, a * k)), "Key shadow color; alpha doubles in dark (DC-L04-12)."),
        "ambient": tok(srgb_value(shadow_base, min(0.6, a * 0.85 * k)), "Ambient shadow color."),
        "ring": tok(srgb_value(shadow_base if L else ring_hex, 0.1 if L else 0.12),
                    "1px ring for ring-and-shadow depth and dark overlays (#BDBDBD at 12% pattern, DC-L04-12)."),
    }
    if model == "materials":
        glass_base = "#ffffff" if L else ctx.ramp("neutral", "dark").steps[3]["hex"]
        out["surface"]["glass"] = tok(srgb_value(glass_base, 0.72), "Glass for controls and navigation only, never content (DC-L04-15).")
        out["surface"]["glassFallback"] = tok(surf["overlay"], "Solid twin under Reduce Transparency and Increase Contrast (DC-L04-16).")
        out["surface"]["glassDimming"] = tok(srgb_value("#000000", 0.35), "35% dimming under clear glass over bright content (S-L15-073).")
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

    def face(v, fallback):
        if not v or v == "system":
            return list(fallback)
        if isinstance(v, list):
            return v
        return [v] + list(fallback)
    text_face = face(raw.get("textFace"), SYSTEM_SANS)
    disp = raw.get("displayFace")
    fam = {"text": tok(text_face, "Text face for UI and body (DC-L02-01)."),
           "display": tok(A("font.family.text") if disp in (None, "=textFace", raw.get("textFace")) else face(disp, text_face),
                          "Display face for headings (Apple, Google and Linear split display and text faces, DC-L06-07)."),
           "mono": tok(face(raw.get("monoFace"), SYSTEM_MONO), "Code, tokens, tabular values.")}
    weights = {"$type": "fontWeight", "$description": f"{wc} weights: body 400, labels {w['label']}, headings {hw} (DC-L02-15; Energy sets heading weight, S-L06-031).",
               "body": tok(400), "label": tok(w["label"]), "heading": tok(hw)}
    if "display" in w:
        weights["display"] = tok(w["display"], "Display sizes (32px and up) only.")
    size_tok = {"$type": "dimension",
                "$description": f"Type scale: round({base} x {sc['ratio']}^n), n from -2 to {sc['nTop']}; sizes under {sc['minSize']}px dropped; "
                                "adjacent sizes under 10% apart merged (DC-L02-09, DC-L02-10).",
                "$extensions": {NS: {"base": base, "ratio": sc["ratio"], "displayReach": sc["reach"], "formulaSizes": sc["raw"],
                                     "merged": sc["merged"], "evidence": ["DC-L02-09", "DC-L02-10", "S-L02-021", "S-L09-407"]}}}
    lh_tok = {"$type": "dimension", "$description": "Line heights snapped to a 4px grid: 1.5 up to 17px, 1.4 to 26px, 1.25 to 44px, 1.12 above (DC-L02-13)."}
    for s in S:
        size_tok[str(s)] = tok(dim(s))
        lh = max(s + 2, snap4_down_on_tie(s * line_height_ratio(s)))
        lh_tok[str(lh)] = tok(dim(lh))
    text = {"$type": "typography",
            "$description": "Semantic text styles (role x size). lineHeight is a unitless multiplier as DTCG requires; px is in $extensions.",
            "$extensions": {NS: {"evidence": ["DC-L02-07", "DC-L02-13", "DC-L02-14", "DC-L02-15", "DC-L15-02"]}}}

    def sz(k):
        return S[clamp(b + k, 0, len(S) - 1)]

    def tracking(size, caps=False):
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
    if len(H) > len(heading_names):
        H = H[:len(heading_names) - 1] + [H[-1]]
    uses = {"title": ("Card, panel and group titles.", "Page titles."), "headline": ("Page and section titles.", "Card titles."),
            "display": ("One hero line per page: marketing, empty states.", "App chrome and repeated elements.")}
    for name, s in zip(heading_names, H):
        role = "display" if name.startswith("display") and "display" in w else "heading"
        fam_name = "display" if not name.startswith("title") else "text"
        u, av = uses[name.split(".")[0]]
        styles.append((name, s, role, fam_name, u, av, False))
    used_lh = {}
    for path, s, role, fam_name, use, avoid, caps in styles:
        lh = max(s + 2, snap4_down_on_tie(s * line_height_ratio(s)))
        used_lh[lh] = True
        em = tracking(s, caps)
        ext = {"lineHeightPx": lh, "letterSpacingEm": em, "use": use, "avoid": avoid}
        if caps:
            ext["textTransform"] = "uppercase"
        if compact_lh and (path.startswith("label") or path in ("body.sm", "body.md")):
            ext["lineHeightTightPx"] = s + 4 if s <= 16 else snap4_down_on_tie(s * 1.2)
        node = text
        parts = path.split(".")
        for q in parts[:-1]:
            node = node.setdefault(q, {})
        node[parts[-1]] = tok({"fontFamily": A(f"font.family.{fam_name}"), "fontSize": A(f"font.size.{s}"),
                               "fontWeight": A(f"font.weight.{role}"), "letterSpacing": dim(rnd(s * em, 2)),
                               "lineHeight": rnd(lh / s, 4)}, None, ext)
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
    ctx.type_info = dict(sc, weights=w, styles=[s[0] for s in styles], lineHeights=sorted(used_lh), scripts=script_notes)
    font = {"family": dict({"$type": "fontFamily"}, **fam), "weight": weights, "size": size_tok,
            "lineHeight": {k: v for k, v in lh_tok.items() if k.startswith("$") or int(k) in used_lh}}
    return {"font": font, "text": text}


# ---------------------------------------------------------------------------------------------- space

def space_ladder(unit):
    vals = []
    for m in space_multipliers():
        v = unit * m
        if abs(v - round(v)) < 1e-9:
            vals.append(int(round(v)))
    return sorted(set(vals))


def targets_for(ctx):
    plats = set(ctx.raw.get("platforms") or ["web"])
    inputs = set(ctx.raw.get("inputs") or ["pointer", "touch"])
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
    ladder = space_ladder(unit)
    space = {"$type": "dimension",
             "$description": f"Spacing ladder: {unit} x [0, 0.5, 1, 1.5, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20], non-integers dropped (LEVERS B8). "
                             "Names are pixel values.",
             "$extensions": {NS: {"unit": unit, "evidence": ["DC-L03-01", "DC-L03-02", "S-L09-508"]}}}
    for v in ladder:
        space[str(v)] = tok(dim(v))
    tg = targets_for(ctx)
    icon_default = int(ctx.P("icon.defaultSize", ctx.params["icon.defaultSize"]))
    pairs = {16: 14, 20: 16, 24: 20}  # icon size -> paired text size (DC-L05-05)
    label_w = 500 if int(ctx.params["type.weightCount"]) >= 3 else 400

    def stroke(sz):  # LEVERS B12 [inferred formula]: round_to_0.5((size/12) * (weight/400)), min 1
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
    ctx.space_info = {"unit": unit, "ladder": ladder, "targets": tg, "iconDefault": icon_default,
                      "iconStroke": {16: stroke(16), 20: stroke(20), 24: stroke(24)}}
    return {"space": space, "size": size, "icon": icon}


def build_space_density(ctx, density):
    ladder = ctx.space_info["ladder"]
    unit = ctx.space_info["unit"]
    shift = {"spacious": 1, "comfortable": 0, "compact": -1}[density]
    ratio = {"spacious": 3.5, "comfortable": 2.5, "compact": 2.0}[density]  # innerOuterRatio bands (DC-L03-24 [inferred])
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
    offset = 2
    focus_r = FULL if full else (control_v + offset if control_v > 0 else 0)
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
        "controlSm": tok(rr(control_sm), "Controls under 32px tall drop one step (Fluent, S-L04-007)."),
        "container": tok(rr(container), "Cards and panels."),
        "overlay": tok(rr(overlay), "Dialogs, sheets, popovers."),
        "person": tok(A("radius.full"), "Avatars."),
        "nested": tok(dim(nested), "Inner radius for an element inset by space.inset.lg inside a container: max(outer - padding, smallest step) (DC-L04-05)."),
        "focus": tok(dim(focus_r), "Focus ring radius = control radius + ring offset (Atlassian radius + 2px, S-L04-016)."),
    })
    border = {"$type": "dimension", "width": {
        "$description": "Border widths 1 / 2 / 4. Width changes on state use an inset shadow so layout does not jump (DC-L04-07).",
        "1": tok(dim(1)), "2": tok(dim(2)), "4": tok(dim(4)),
        "default": tok(A("border.width.1")), "selected": tok(A("border.width.2")), "emphasis": tok(A("border.width.4"))}}
    focus = {"$type": "dimension",
             "$description": f"Focus indicator: {focus_w}px ring, {offset}px offset, color.border.focus; never color-only (DC-L04-09, WCAG 2.4.7, 2.4.13).",
             "ring": {"width": tok(dim(focus_w)), "offset": tok(dim(offset))}}
    ctx.shape_info = {"control": "full" if full else control_v, "controlSm": control_sm, "detail": detail, "container": container,
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
    if model == "materials":
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
    d["mediumExit"] = r10(d["medium"] * exit_k)
    d["longExit"] = r10(d["long"] * exit_k)
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
    off = bool(ctx.flags.get("motionOff"))

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
                "exit": t("mediumExit", "exit", "Leaving: shorter than enter (DC-L04-24)."),
                "move": tok(A("motion.spring.spatial.default"), "On-screen movement: spatial spring (web: linear() sample)."),
                "expand": t("long", "enter", "Dialogs, sheets, side panels entering.")}
    desc = f"Semantic transitions, {context} motion. Reduced motion is a token mode: travel becomes opacity, feedback stays (DC-L04-25)."
    if off:
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
        "color.text.primary": surfaces + ["color.bg.neutral.subtle", "color.bg.neutral.subtleHover", "color.bg.neutral.subtlePressed",
                                          "color.bg.accent.subtle"],
        "color.text.secondary": surfaces + ["color.bg.neutral.subtle", "color.bg.neutral.subtleHover"],
        "color.text.tertiary": surfaces,
        "color.text.link": surfaces + ["color.bg.accent.subtle"],
        "color.text.onAccent": ["color.bg.accent.bold", "color.bg.accent.boldHover", "color.bg.accent.boldPressed"],
        "color.text.onAction": ["color.bg.action.primary", "color.bg.action.primaryHover", "color.bg.action.primaryPressed"],
        "color.text.onBrand": ["color.bg.brand"],
        "color.text.inverse": ["color.bg.inverse"],
    }
    for s in ("success", "warning", "danger", "info"):
        text_on[f"color.text.{s}"] = ["color.surface.base", "color.surface.raised", f"color.bg.{s}.subtle"]
        text_on[f"color.text.on{s.title()}"] = [f"color.bg.{s}.bold", f"color.bg.{s}.boldHover"]
    for extra in ("accent2", "accent3"):
        if extra in ctx.cinfo["ramps"]:
            text_on[f"color.text.{extra}"] = ["color.surface.base", "color.surface.raised", f"color.bg.{extra}.subtle"]
            text_on[f"color.text.on{extra[0].upper() + extra[1:]}"] = [f"color.bg.{extra}.bold"]
    non_text = {
        "color.border.strong": surfaces,
        "color.border.input": surfaces + ["color.bg.neutral.subtle"],
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
            if ctx.raw.get("focusColor"):
                pr["inner"] = "color.border.focusInner"
            pairs.append(pr)
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


def apply_token_overrides(ctx, files):
    """Overrides whose key is not a lever parameter patch a token directly: 'path' or 'light:path' / 'dark:path'."""
    known = set(lever_index()) | {"type.displayReach", "radius.container", "radius.overlay", "radius.detail", "color.dark.baseY",
                                  "color.placeholderHue", "type.maxStepGapMerge"}
    applied = []
    for key, val in (ctx.state.get("overrides") or {}).items():
        if key in known:
            continue
        mode, path = (key.split(":", 1) + [None])[:2] if ":" in key else (None, key)
        if path is None:
            path, mode = mode, None
        parts = path.split(".")
        for fname, tree in files.items():
            if not fname.endswith(".tokens.json"):
                continue
            if mode and f".{mode}." not in fname:
                continue
            node = tree
            for q in parts:
                node = node.get(q) if isinstance(node, dict) else None
                if node is None:
                    break
            if isinstance(node, dict) and "$value" in node:
                node["$value"] = val
                node.setdefault("$extensions", {}).setdefault(NS, {})["source"] = "person"
                applied.append(f"{fname}:{path}")
    return applied


PRIMITIVE_RE = re.compile(r"^(color\.(white|black|brand|focus|neutralAlpha|neutral|accent|action|accent2|accent3|success|warning|danger|info)\."
                          r"|color\.(white|black)$|opacity\.|space\.\d+$|radius\.(\d+|full)$|font\.(size|lineHeight)\.|border\.width\.\d+$"
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
        "preset": ctx.state.get("preset"), "macros": ctx.state.get("macros"),
        "params": {k: {"value": ctx.params[k], **ctx.pmeta.get(k, {})} for k in sorted(ctx.params)},
        "color": ctx.cinfo, "ramps": ramps, "modes": ctx.modes,
        "type": ctx.type_info, "space": ctx.space_info, "density": ctx.density_info, "shape": ctx.shape_info,
        "elevation": ctx.elev_info, "motion": ctx.motion_info,
        "contrastPairs": contrast_pairs(ctx), "tokenOverrides": applied,
        "platforms": ctx.raw.get("platforms"), "inputs": ctx.raw.get("inputs"),
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
    styles = {k: v["resolved"] for k, v in toks.items() if k.startswith("text.") and v["type"] == "typography"}
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
    if any(k == "color.surface.glass" for k in toks) and "color.surface.glassFallback" not in toks:
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
        if dials.get("colorfulness", 0) > 75 and dials.get("density", 0) > 66:
            rep.add("warning", "lint", "vivid color on a dense layout can feel noisy", "vivid-and-dense", "S-L15-047")
        if params.get("signifier.minStrength") == "minimal-allowed" and dials.get("density", 0) > 33:
            rep.add("warning", "lint", "buttons and links barely look clickable on a layout that is not roomy", "minimal-signifiers-dense", "S-L15-004")
        if dials.get("expression", 0) > 66 and (state.get("raw", {}).get("domain") or "").lower() in ("finance", "banking", "fintech"):
            rep.add("warning", "lint", "a very expressive look in a finance product can cost trust", "expressive-finance", "S-L06-010")
    if (state.get("preset") or meta.get("preset")) == "soft":
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
        ramps_ = sorted({k.split(".")[1] for k in t2 if re.fullmatch(rf"color\.[a-zA-Z0-9]+\.{mode}\.\d+", k)} - {"neutralAlpha"})
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
    open_hooks = [h for h, v in (state.get("hooks") or {}).items() if (v or {}).get("status", "pending") in ("pending", "unknown")]
    if open_hooks:
        rep.add("advisory", "hooks", f"{len(open_hooks)} assets a person must make, not asked about yet: {', '.join(open_hooks)}",
                "Designer hooks, not designer replacement", "BRIEF req. 2, Q-brand-08")


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
                break
    return _GLOSSARY


def term(key):
    g = glossary()
    v = g.get(key.lower())
    if v:
        return v.split(".")[0].split(";")[0].strip()[:60]  # a short name, not the whole definition
    return TERM_DEFAULTS.get(key, key)


def words_of(path):
    """color.bg.neutral.subtleHover -> 'neutral subtle hover background' (plain words for a token path)."""
    parts = [re.sub(r"(?<=[a-z0-9])([A-Z])", lambda m: " " + m.group(1).lower(), x) for x in path.split(".")]
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
BRAND_ROWS = {"A": ("playful", "serious"), "B": ("friendly", "authoritative"), "C": ("minimal", "rich"),
              "D": (None, None), "E": ("premium", "everyday"), "F": ("modern", "heritage"), "G": ("bold", "deferential")}


def answer_effects(qid, value):
    """Engine inputs implied by a questionnaire answer. Values are [inferred] positions inside the levers.json
    bands that each option names (for example Q-shape-01 'soft' = 8-12px -> Roundness 55 -> 8px)."""
    v = value
    eff = {}
    if qid == "Q-aud-01":
        eff["dials.density"] = {"dense": 80, "regular": 50, "large": 15}.get(v)
    elif qid == "Q-plat-01" and isinstance(v, list):
        eff["raw.platforms"] = v
    elif qid == "Q-color-01":
        eff["raw.flags.brandExact"] = v == "keep-hex"
    elif qid == "Q-type-01":
        if v == "system":
            eff["raw.textFace"] = "system"
    elif qid == "Q-type-08":
        try:
            eff["raw.baseSize"] = int(v)
        except (TypeError, ValueError):
            pass
    elif qid == "Q-space-01":
        eff["raw.spaceUnit"] = {"4-grid-8-rhythm": 4, "4": 4, "8": 8, "rem-16": 4}.get(str(v))
    elif qid == "Q-shape-01":
        eff["dials.roundness"] = {"square": 5, "subtle": 40, "soft": 55, "pill": 97}.get(v)
    elif qid == "Q-depth-01":
        eff["dials.depth"] = {"borders": 8, "ring-shadow": 25, "tonal": 45, "shadow": 68, "glass": 90}.get(v)
    elif qid == "Q-motion-01":
        eff["dials.energy"] = {"none": 0, "productive": 20, "two-mode": 50, "springs": 80}.get(v)
        eff["raw.flags.motionOff"] = v == "none"
    elif qid == "Q-theme-01":
        eff["raw.flags.darkMode"] = v != "light-only"
        if v == "dark-only":
            eff["raw.defaultTheme"] = "dark"
    elif qid == "Q-dir-01":
        eff["preset"] = {"neo-brutalist": "neobrutal"}.get(v, v)
    elif qid == "Q-brand-01" and isinstance(v, dict):
        macros = []
        for row, pos in v.items():
            row = row[:1].upper()
            left, right = BRAND_ROWS.get(row, (None, None))
            if row == "D":
                eff["dials.energy"] = int(pos)
                continue
            if left is None or pos is None:
                continue
            strength = rnd(abs(float(pos) - 50) / 50, 2)
            if strength > 0:
                macros.append({"id": left if float(pos) < 50 else right, "strength": strength})
        eff["macros"] = macros
    return {k: val for k, val in eff.items() if val is not None}


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


def _store(state, path, value, set_by, did, lock):
    """Write a value; dials and answers keep {value, set_by, ...} records (spec 7.10)."""
    parts = path.split(".")
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
        rec.setdefault("locked", False)
        if lock:
            rec["locked"] = True
        state["answers"][parts[1]] = rec
        return answer_value(old)
    old = set_path(state, path, value)
    if lock and path not in (state.get("locks") or []):
        state.setdefault("locks", []).append(path)
    return old


def cmd_set(d, path, value, why=None, force=False, quiet=False, set_by=None, lock=False, source_ref=None):
    sp = os.path.join(d, "state.json")
    if not os.path.exists(sp):
        raise SystemExit(f"no state at {sp}; run `engine.py init --dir {d}` first")
    state = merge_defaults(read_json(sp))
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
    did = f"D-{len(_decision_entries(d)) + 1:04d}"
    prev = _store(state, path, value, set_by, did, lock)
    extra = []
    if prev is not None:
        extra.append(f"previous value: {json.dumps(prev, ensure_ascii=False)}")
    if path.startswith("answers."):
        qid = path.split(".", 1)[1]
        for epath, evalue in answer_effects(qid, value).items():
            if is_locked(state, epath) and not force:
                extra.append(f"skipped {epath} (locked)")
                continue
            _store(state, epath, evalue, set_by, did, False)
            extra.append(f"also set: {epath} = {json.dumps(evalue, ensure_ascii=False)} (from {qid})")
    dump_json(sp, state)
    log_decision(d, path, value, why, set_by, lock, source_ref, extra)
    if not quiet:
        print(f"{did} set {path} = {json.dumps(value, ensure_ascii=False)} ({set_by}{', locked' if lock else ''})")
        for e in extra:
            print("  " + e)
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
            extra = " text-transform: uppercase;" if (t.get("$extensions") or {}).get(NS, {}).get("textTransform") else ""
            lines.append(f"{cls} {{ font: var({v}); letter-spacing: var({v}-tracking);{extra} }}")
    lines += ["", f".{prefix}-focus-ring:focus-visible {{",
              f"  outline: var({css_var(prefix, 'focus.ring.width')}) solid var({css_var(prefix, 'color.border.focus')});",
              f"  outline-offset: var({css_var(prefix, 'focus.ring.offset')});"]
    if any(k.endswith("focusInner") for k in flatten(files[[s['$ref'] for s in theme_ctx[default_theme]][0]])):
        lines.append(f"  box-shadow: 0 0 0 var({css_var(prefix, 'focus.ring.offset')}) var({css_var(prefix, 'color.border.focus-inner')});")
    lines += ["}", "@media (forced-colors: active) {", f"  .{prefix}-focus-ring:focus-visible {{ outline-color: Highlight; }}", "}", ""]
    return "\n".join(lines)


TW_COLOR_MAP = [("color.surface.", "surface-"), ("color.text.", "fg-"), ("color.bg.", ""), ("color.border.", "line-"),
                ("color.icon.", "icon-"), ("color.overlay.", "overlay-")]


def export_tailwind(files, meta, prefix):
    res = files["opendesigner.resolver.json"]
    flat = resolve_all(files, {})
    unit = meta["space"]["unit"]
    lines = [f"/* Tailwind CSS v4 theme for {meta.get('name')}. Generated by the OpenDesigner engine {ENGINE_VERSION}.",
             "   Usage:  @import \"tailwindcss\";  @import \"../css/tokens.css\";  @import \"./theme.css\";",
             "   @theme inline points utilities at the design-system variables, so light/dark, density and reduced",
             "   motion keep working through data-theme / data-density / data-motion and the media queries in tokens.css. */", "",
             "@theme inline {"]
    lines.append(f"  --spacing: {unit}px; /* p-1 = one base unit (LEVERS B8) */")
    for path in sorted(flat):
        t = flat[path]
        v = f"var({css_var(prefix, path)})"
        if t["type"] == "color" and not re.match(r"color\.(neutral|accent|action|success|warning|danger|info|neutralAlpha|accent2|accent3|white|black|brand|focus)\b", path):
            for src, dst in TW_COLOR_MAP:
                if path.startswith(src):
                    rest = "-".join(kebab(s) for s in path[len(src):].split("."))
                    lines.append(f"  --color-{dst}{rest}: {v};")
                    break
            else:
                if path.startswith("color.shadow."):
                    continue
    lines.append("  --color-white: #fff;")
    for fam in ("text", "display", "mono"):
        name = {"text": "sans", "display": "display", "mono": "mono"}[fam]
        lines.append(f"  --font-{name}: var({css_var(prefix, 'font.family.' + fam)});")
    for path in sorted(flat):
        t = flat[path]
        if path.startswith("font.weight."):
            lines.append(f"  --font-weight-{kebab(path.split('.')[-1])}: var({css_var(prefix, path)});")
    for path in sorted(flat):
        t = flat[path]
        if t["type"] == "typography":
            n = "-".join(kebab(s) for s in path.split(".")[1:])
            v = css_var(prefix, path)
            lines += [f"  --text-{n}: var({v}-size);", f"  --text-{n}--line-height: var({v}-line-height);",
                      f"  --text-{n}--letter-spacing: var({v}-tracking);", f"  --text-{n}--font-weight: var({v}-weight);"]
    for path in sorted(flat):
        if re.match(r"space\.(inset|stack|inline|section)\.", path):
            lines.append(f"  --spacing-{'-'.join(kebab(s) for s in path.split('.')[1:])}: var({css_var(prefix, path)});")
        elif re.match(r"size\.(control|target|icon)\.", path):
            lines.append(f"  --spacing-{'-'.join(kebab(s) for s in path.split('.'))}: var({css_var(prefix, path)});")
    for r in ("detail", "control", "controlSm", "container", "overlay", "person", "full"):
        lines.append(f"  --radius-{kebab(r)}: var({css_var(prefix, 'radius.' + r)});")
    for e in ("raised", "floating", "overlay"):
        lines.append(f"  --shadow-{e}: var({css_var(prefix, 'elevation.' + e)});")
    for e in ("standard", "enter", "exit", "linear"):
        lines.append(f"  --ease-{e}: var({css_var(prefix, 'motion.easing.' + e)});")
    lines += ["}", ""]
    lines += ["/* Semantic motion helpers (durations follow the reduced-motion mode automatically). */",
              "@utility transition-feedback {", f"  transition-duration: var({css_var(prefix, 'motion.transition.feedback')}-duration);",
              f"  transition-timing-function: var({css_var(prefix, 'motion.transition.feedback')}-easing);", "}", ""]
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
    if path.startswith("font.lineHeight."):
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


PAPER_TYPES = [("color", None), ("spacing", "space."), ("radius", "radius."), ("fontSize", "font.size."), ("lineHeight", "font.lineHeight."),
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


def export_swift(files, meta, prefix):
    res = files["opendesigner.resolver.json"]
    mods = res.get("modifiers", {})
    P = prefix.upper()
    light = resolve_all(files, {"theme": "light"} if "theme" in mods else {})
    dark = resolve_all(files, {"theme": "dark"}) if "theme" in mods and "dark" in mods["theme"]["contexts"] else light
    base = resolve_all(files, {})
    L = [f"// {meta.get('name')} design tokens for SwiftUI. Generated by the OpenDesigner engine {ENGINE_VERSION}; do not edit.",
         "// Colors switch with the system appearance. Spacing uses the default density; fonts scale with Dynamic Type.",
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
    L += ["    }", "", "    enum Typography {"]
    textstyle = {"body": ".body", "label": ".callout", "code": ".body", "title": ".headline", "headline": ".title2", "display": ".largeTitle"}
    for p in sorted(base):
        t = base[p]
        if t["type"] == "typography":
            v = t["resolved"]
            fam = v["fontFamily"][0] if isinstance(v["fontFamily"], list) else v["fontFamily"]
            size = fmt_num(_px(v["fontSize"]))
            rel = textstyle.get(p.split(".")[1], ".body")
            wt = int(v["fontWeight"])
            wname = {100: "ultraLight", 200: "thin", 300: "light", 400: "regular", 500: "medium", 600: "semibold", 700: "bold",
                     800: "heavy", 900: "black"}[min(900, max(100, int(round(wt / 100) * 100)))]
            mono = p.split(".")[1] == "code"
            if fam in ("system-ui", "-apple-system", "ui-monospace") or fam.startswith("SF"):
                expr = f"Font.system(size: {size}, weight: .{wname}{', design: .monospaced' if mono else ''})"
            else:
                expr = f"Font.custom(\"{fam}\", size: {size}, relativeTo: {rel}).weight(.{wname})"
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
         "import androidx.compose.ui.text.TextStyle", "import androidx.compose.ui.text.font.FontWeight",
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
    K += ["}", "", f"object {P}Type {{"]
    for p in sorted(base):
        t = base[p]
        if t["type"] == "typography":
            v = t["resolved"]
            ext = (t.get("$extensions") or {}).get(NS, {})
            K.append(f"    val {camel(p.split('.')[1:])} = TextStyle(fontSize = {fmt_num(_px(v['fontSize']))}.sp, "
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
            write_text(p, export_tailwind(files, meta, prefix))
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
LEVEL0 = ["answers.Q-aud-01", "raw.brandColor", "answers.Q-plat-01", "macros", "answers.Q-theme-01"]


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


def dial_words(dial, v, params):
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
        "colorfulness": f"scheme {params['color.schemeVariant']}, accent chroma {rnd(params['color.accentChroma.hct'], 1)} (HCT), "
                        f"{params['color.accentCount']} accent(s), surfaces: {params['color.surfaces']}",
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

    def section(title, body):
        parts = [f"## {title}", ""]
        zk = ztitle.get(title)
        if zk:
            z = zoom[zk]
            nxt = f" To zoom in, answer {', '.join(z['next'])}." if z["level"] != "detailed" and z["next"] else ""
            li = ZOOM_LEVELS.index(z["level"])
            parts += [f"<!-- od:zoom area={zk} level={li} -->",
                      f"> Zoom: {z['level']} ({li} of 3), {z['decisions']} decision{'s' if z['decisions'] != 1 else ''} in this area.{nxt}", ""]
        parts += [body.strip(), ""]
        di = dec_ids(title)
        if di:
            parts += [di, ""]
        if title in keeps:
            parts += [keeps[title], ""]
        return "\n".join(parts)

    # ---- front matter (Google DESIGN.md keys only)
    styles = sorted(p for p, t in light.items() if t["type"] == "typography")
    fm = ["---", "version: alpha", f"name: {json.dumps(state.get('name') or 'Design system')}",
          f"description: {json.dumps(state.get('summary') or (ctx.get('product') or 'Design system generated by OpenDesigner'))}", "colors:"]
    fm_colors = [("primary", "color.bg.action.primary"), ("on-primary", "color.text.onAction"), ("accent", "color.bg.accent.bold"),
                 ("on-accent", "color.text.onAccent"), ("surface", "color.surface.base"), ("surface-raised", "color.surface.raised"),
                 ("on-surface", "color.text.primary"), ("on-surface-variant", "color.text.secondary"), ("outline", "color.border.default"),
                 ("outline-strong", "color.border.strong"), ("focus", "color.border.focus"), ("error", "color.bg.danger.bold"),
                 ("on-error", "color.text.onDanger"), ("success", "color.bg.success.bold"), ("warning", "color.bg.warning.bold")]
    for k, p in fm_colors:
        if p in light:
            fm.append(f'  {k}: "{H(p)}"')
    fm.append("typography:")
    for p in styles:
        v = light[p]["resolved"]
        ext = (light[p].get("$extensions") or {}).get(NS, {})
        fam = v["fontFamily"][0] if isinstance(v["fontFamily"], list) else v["fontFamily"]
        fm += [f"  {'-'.join(kebab(x) for x in p.split('.')[1:])}:", f"    fontFamily: {json.dumps(fam)}",
               f"    fontSize: {fmt_num(_px(v['fontSize']))}px", f"    fontWeight: {int(v['fontWeight'])}",
               f"    lineHeight: {ext.get('lineHeightPx')}px", f"    letterSpacing: {fmt_num(ext.get('letterSpacingEm', 0))}em"]
    fm.append("rounded:")
    for r in ("detail", "controlSm", "control", "container", "overlay", "full"):
        fm.append(f"  {kebab(r)}: {fmt_num(_px(light['radius.' + r]['resolved']))}px")
    fm.append("spacing:")
    dflt = meta["density"][params["space.densityMode"]]
    for k in ("xs", "sm", "md", "lg", "xl"):
        fm.append(f"  {k}: {dflt['inset'][k]}px")
    fm.append(f"  section: {dflt['section']['md']}px")
    lbl = "typography.label-lg" if "text.label.lg" in light else "typography.body-md"
    ctl = dflt["control"]
    fm += ["components:",
           "  button-primary:", '    backgroundColor: "{colors.primary}"', '    textColor: "{colors.on-primary}"',
           f'    typography: "{{{lbl}}}"', '    rounded: "{rounded.control}"', f"    height: {ctl['md']}px",
           f"    padding: 0 {dflt['inset']['lg']}px",
           "  input:", '    backgroundColor: "{colors.surface-raised}"', '    textColor: "{colors.on-surface}"',
           '    rounded: "{rounded.control}"', f"    height: {ctl['md']}px", f"    padding: 0 {dflt['inset']['md']}px",
           "  card:", '    backgroundColor: "{colors.surface-raised}"', '    textColor: "{colors.on-surface}"',
           '    rounded: "{rounded.container}"', f"    padding: {dflt['inset']['xl']}px", "---", ""]
    out = ["\n".join(fm), f"# {state.get('name') or 'Design system'}", "",
           f"> Generated by the OpenDesigner engine {ENGINE_VERSION} from `state.json`, the tokens and `decisions.md`. Don't edit this file to change the system. "
           "Run `engine.py set ...`, then `engine.py generate` and `engine.py design-md`. Hand-written notes survive only inside "
           "`<!-- od:keep -->` ... `<!-- /od:keep -->` blocks at the end of a section. The DTCG files in `tokens/` are the source of truth.", ""]

    # 1 Overview
    principles = state.get("principles") or []
    pl = "\n".join(f"{i}. {p}" for i, p in enumerate(principles, 1)) if principles else \
        "No principles recorded yet (Q-brand-04). Until they are, the dials act as the tie-breakers below."
    surf = ctx.get("surfaces") or []
    body = [f"**Intent.** {state.get('summary') or ctx.get('product') or 'A design system generated from eight dials and a few raw inputs.'}",
            "", f"- Audience: {ctx.get('audience') or 'not recorded yet (Q-aud-01)'}",
            f"- The memorable thing: {ctx.get('memorable') or 'not recorded yet (Q-brand-02)'}",
            f"- Surfaces: {', '.join((s.get('name', '') + ' (' + s.get('mode', '') + ')') if isinstance(s, dict) else str(s) for s in surf) or 'not recorded yet'}",
            f"- Platforms: {', '.join(raw.get('platforms') or [])}; inputs: {', '.join(raw.get('inputs') or [])}",
            f"- Direction: {('preset ' + state['preset']) if state.get('preset') else 'no named preset'}"
            + (f"; brand macros {', '.join((m if isinstance(m, str) else m['id'] + ' x' + str(m.get('strength', 1))) for m in state['macros'])}" if state.get("macros") else ""),
            "", "**Principles (ranked).**", pl, "", "**Dial positions.** Three posture dials set the overall stance. Five character dials fine-tune it.", ""]
    body += [f"- {dial_words(k, dials[k], params)}" for k in DIALS]
    body += ["", "**Zoom by area** (sketch, broad, defined, detailed). You can stop at any level; each one works.", "",
             _md_table(["Area", "Zoom", "Next questions"], [(t, zoom[k]["level"], ", ".join(zoom[k]["next"]) if zoom[k]["level"] != "detailed" else "-")
                                                           for k, t in ZOOM_AREAS if k != "overview"])]
    body += ["", "The tokens in `tokens/` (DTCG 2025.10 with `opendesigner.resolver.json`) are the source of truth. This file is a generated view."]
    out.append(section("Overview", "\n".join(body)))

    # 2 Colors
    ci = meta["color"]
    brand = raw.get("brandColor")
    rows = []
    for p in sorted(light):
        if light[p]["type"] == "color" and re.match(r"color\.(surface|text|bg|border|icon|overlay)\.", p):
            lv, dv = _hex_pair(light, dark, p)
            rows.append((f"`{p}`", lv, dv, light[p]["$description"]))
    nl = [luminance(hx) for hx in meta["ramps"]["neutral"]["light"]["hex"]]
    step_rows = []
    for fg in (8, 9, 10, 11, 12):
        step_rows.append([f"neutral {fg}"] + [f"{contrast_y(nl[fg - 1], nl[bg - 1]):.2f}" for bg in (1, 2, 3, 4, 5)])
    ramp_rows = [(f"`{n}`", " ".join(f"`{h}`" for h in v["light"]["hex"]), v["light"]["textOnSolid"]) for n, v in meta["ramps"].items()]
    body = [f"**Intent.** {('Brand color `' + brand + '`') if brand else 'No brand color yet: the accent uses a placeholder blue hue'} "
            f"drives the accent ramp's hue; the Colorfulness dial ({dials['colorfulness']}) sets its chroma "
            f"(scheme {ci['scheme']}, peak HCT chroma {ci['peakHct']}). The brand's role is **{params['color.brandRole']}** and it sits "
            f"closest to accent step {ci.get('brandAnchorStep') or '-'}."
            + (f" The brand hex is kept exactly at step {ci['pinnedStep']} (brand must be exact)." if ci.get("pinnedStep") else "")
            + (f" The UI fill (`color.bg.action.primary`, {H('color.bg.action.primary')}) is not the brand hex on purpose: Colorfulness sets "
               "its chroma and the contrast target sets its lightness. To use the exact hex, set `raw.flags.brandExact` (Q-color-01 "
               "keep-hex); it is pinned when the hex carries text at the contrast target."
               if brand and not ci.get("pinnedStep") else "")
            + (" The exact hex cannot carry text at the contrast target, so it stays in `color.brand.seed` for logos and marketing."
               if ci.get("brandPinFailed") else ""),
            "", "**How ramps are built.** Each hue gets twelve steps in OKLCH, placed by contrast. Step 8 reaches at least 3:1 (edges and focus). "
            "Steps 10 and 11 reach the text minimum on backgrounds 1-4. Step 12 reaches at least 7:1. Steps 2-6 are spaced evenly in lightness "
            "between step 1 and step 7. Light and dark ramps are solved separately. Dark solids are lighter and carry dark text "
            f"(dark mode is a separate mapping, never an inversion). Text minimum: {ci['textMin']}:1 "
            f"({'WCAG 2.2 AAA' if ci['textMin'] > 4.5 else 'WCAG 2.2 AA'}).",
            "", _md_table(["Ramp", "Light steps 1-12", "Solid carries"], ramp_rows),
            "", "**Step-distance guarantee** (neutral, light; WCAG contrast of a foreground step on background steps 1-5):", "",
            _md_table(["Foreground", "on 1", "on 2", "on 3", "on 4", "on 5"], step_rows),
            "", "**States.** Hover moves one step, pressed two (DC-L01-17). Where a color is unknown at design time, use the state "
            "opacities in `opacity.state.*` (hover 8%, focus 10%, pressed 10%, drag 16%).",
            "", "**Semantic roles** (use these, never the ramps):", "", _md_table(["Token", "Light", "Dark", "Use"], rows),
            "", "**Use / avoid.**", "- Use one solid accent fill per view for the primary action; spend chroma on small, meaningful elements.",
            "- Avoid gray text on colored fills; use the matching `text.on*` role.",
            "- Avoid color as the only signal: pair status colors with an icon or label.",
            "- Charts: no chart palette is generated yet. Take chart colors from the status and accent hues, and check them separately."]
    out.append(section("Colors", "\n".join(body)))

    # 3 Typography
    rows = []
    for p in styles:
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
            f"- Weights: {', '.join(f'{k} {v}' for k, v in tinfo['weights'].items())} (two or three distinct weights per view).",
            "- Line heights snap to a 4px grid: 1.5 up to 17px, 1.4 to 26px, 1.25 to 44px, 1.12 above.",
            "- Letter spacing: +0.02em at 11-12px, -0.01em from 32px, -0.02em from 48px.",
            "- Text scaling: CSS sizes are rem, line heights unitless, so text scales to 200% (WCAG 1.4.4); containers must grow with it.",
            "- Scripts: " + (", ".join(f"{k}: line height x{v.get('lineHeightFactor')}" + (", tracking 0" if v.get("zeroTracking") else "")
                                      for k, v in scripts.items()) if scripts else "Latin only; add scripts in raw.scripts to get per-script line heights (DC-L02-25)."),
            "", _md_table(["Style", "Size/line (px)", "Weight", "Tracking", "Use"], rows),
            "", "**Use / avoid.**", "- Use at most three sizes and two weights in one view; let color and weight carry hierarchy before size.",
            "- Avoid all caps for sentences and in scripts without case; use weight for emphasis there."]
    out.append(section("Typography", "\n".join(body)))

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
    out.append(section("Layout", "\n".join(body)))

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
            "- " + ("Glass is for controls and navigation only, with `color.surface.glassFallback` under Reduce Transparency." if el["model"] == "materials"
                    else "No materials or glass in this system.")]
    out.append(section("Elevation & Depth", "\n".join(body)))

    # 6 Shapes
    body = [f"**Intent.** Roundness {dials['roundness']}/100 gives controls a **{shp['control']}** radius; details {shp['detail']}px, containers "
            f"{shp['container']}px, overlays {shp['overlay']}px, people full. Controls under 32px tall use `radius.controlSm` ({shp['controlSm'] if shp['controlSm'] < FULL else 'full'}).",
            "", f"- Nested radius: inner = max(outer - padding, smallest step). Here it is {shp['nested']}px inside a container with `space.inset.lg` "
            "padding. Equal radii on nested shapes look uneven (DC-L04-05).",
            f"- Focus ring: {shp['focusWidth']}px, 2px offset, radius = control radius + offset ({shp['focusRadius'] if shp['focusRadius'] < FULL else 'full'}).",
            f"- Icons: {shp['iconCorners']} corners, {shp['iconCaps']} caps. On iOS, use continuous corners (DC-L04-04).",
            "- Signature shapes: none generated; a brand shape library is a designer asset (hook H-motif)."]
    out.append(section("Shapes", "\n".join(body)))

    # 7 Components
    inv = (state.get("components") or {}).get("inventory") or []
    notes = (state.get("components") or {}).get("notes") or {}
    rows = [(c, notes.get(c, "planned (tokens ready)")) for c in inv]
    ans = {k: answer_value(v) for k, v in (state.get("answers") or {}).items()}
    pol = [("Disabled submit", ans.get("Q-form-02")), ("Validation timing", ans.get("Q-form-01")), ("Toasts", ans.get("Q-form-04")),
           ("Undo versus confirm", ans.get("Q-state-06")), ("Button emphasis levels", ans.get("Q-state-01"))]
    body = [f"**Intent.** v1 components use the semantic tokens only. Base: {(state.get('components') or {}).get('base') or 'not chosen yet (Q-comp-01)'}. "
            f"Buttons are {ctl['md']}px tall ({params['space.densityMode']}), {shp['control']} radius, `text.label.lg`; one primary action per view.",
            "", _md_table(["Component", "Status"], rows) if rows else "No inventory recorded.",
            "", "**Contested policies:** " + "; ".join(f"{k}: {v if v is not None else 'pending'}" for k, v in pol) + ".",
            "", "**Use / avoid.**", "- Every interactive component shows hover, pressed, focus-visible and disabled states from the tokens.",
            f"- Inputs keep a 3:1 boundary (`color.border.input`); signifier strength: {params['signifier.minStrength']}.",
            "- Component docs belong in `opendesigner/components/<name>.md` (spec 7.8)."]
    out.append(section("Components", "\n".join(body)))

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
    out.append(section("Do's and Don'ts", "\n".join(body)))

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
    out.append(section("Motion", "\n".join(body)))

    # 10 Modes and Themes
    rows = [(n, ", ".join(m["contexts"]), m.get("default")) for n, m in mods.items()]
    body = ["**Intent.** Modes live in the DTCG resolver (`tokens/opendesigner.resolver.json`); modifiers are orthogonal, so no two set the same token.",
            "", _md_table(["Modifier", "Contexts", "Default"], rows) if rows else "Single theme.",
            "", f"- Web: `prefers-color-scheme` with a `[data-theme]` override; `[data-density]`; `prefers-reduced-motion` with `[data-motion]` (see `build/css/tokens.css`).",
            "- High-contrast themes are not generated; set `raw.contrastTarget` to AAA for 7:1 text everywhere.",
            "- A second brand or a client re-skin may override the color primitives and `color.bg.brand`; semantic names never change."]
    out.append(section("Modes and Themes", "\n".join(body)))

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
    out.append(section("Iconography and Imagery", "\n".join(body)))

    # 12 Content and Voice
    vstat = hs("H-voice")
    body = [f"**Intent.** {'Draft: ' if vstat not in ('have',) else ''}voice guidance level **{params['content.voiceGuidance']}** "
            f"(Brand presence {dials['brandPresence']}); **{params['content.capitalization']}**; contractions **{params['content.contractions']}** "
            f"(Warmth {dials['warmth']}). Voice guide hook H-voice: {vstat}.",
            "", "- Buttons say what they do in two to four words; errors say what happened and how to fix it.",
            "- Reading level: plain language; avoid jargon in UI copy.",
            "- Word list: not recorded yet (Q-voice-03)."]
    out.append(section("Content and Voice", "\n".join(body)))

    # 13 Accessibility
    body = [f"**Intent.** Standard: WCAG 2.2 {'AAA for text' if ci['textMin'] > 4.5 else 'AA'}. APCA is reported as advice only.",
            "", "**The system guarantees:**", "- text and edge contrast in every mode", "- visible focus (2px ring, 2px offset, 3:1)",
            "- minimum target sizes for each kind of input", "- a reduced-motion mode", "- rem-based type, so text scales to 200%",
            "- text on colored fills chosen automatically",
            "", "**Product teams own:** accessible names and labels, alt text, reading and focus order, and never using color alone. "
            "Also: clear error messages, dialogs that can be closed, no pre-checked consent boxes, and captions for media.",
            "", "**Test on each platform:**", "- keyboard only", "- a screen reader (VoiceOver, NVDA or TalkBack)", "- 200% zoom",
            "- forced colors (Windows High Contrast)", "- reduced motion", "- touch on a phone, for every surface that allows touch"]
    out.append(section("Accessibility", "\n".join(body)))

    # 14 Platforms and Devices
    body = [f"**Intent.** Platforms: {', '.join(raw.get('platforms') or [])}. Inputs: {', '.join(raw.get('inputs') or [])}. "
            f"Brand presence {dials['brandPresence']}: platform overrides shape and material: {params['platform.overridesShapeAndMaterial']}; "
            f"native base text size: {params['platform.useNativeBaseSize']}.",
            "", "- Navigation, back, sheets and pickers stay native on every platform (DC-L10-02).",
            "- Swift and Compose files in `build/` use the same names as the CSS variables (Figma code syntax matches them)."]
    out.append(section("Platforms and Devices", "\n".join(body)))

    # 15 Decisions
    rows = [(v["id"], f"`{k}`", v["value"], v["set_by"] + (" (locked)" if v["locked"] else ""), v["reason"])
            for k, v in sorted(decs.items(), key=lambda kv: kv[1]["id"])][-20:]
    body = ["The highest-reach decisions, newest value per path. Full log: [decisions.md](decisions.md).", "",
            _md_table(["Id", "Path", "Value", "Set by", "Reason"], rows) if rows else "No decisions recorded yet."]
    out.append(section("Decisions", "\n".join(body)))

    # 16 Open Items
    pend = [f"{h} ({v.get('name', h)}): {v.get('status')}" for h, v in hooks.items() if v.get("status") in ("pending", "placeholder", "commissioning")]
    assumed = [f"{k} ({v['set_by']})" for k, v in decs.items() if v["set_by"] in ("assumed", "delegated", "auto_default")]
    body = ["- Assets not final: " + ("; ".join(pend) if pend else "none."),
            "- Answers taken on assumption or delegated: " + (", ".join(assumed) if assumed else "none."),
            "- Waivers: " + ("; ".join(f"{k}: {v}" for k, v in (state.get("waivers") or {}).items()) or "none."),
            f"- Validation: {vr.count('error')} errors, {vr.count('warning')} warnings."]
    out.append(section("Open Items", "\n".join(body)))

    # 17 For Agents
    body = ["1. Before any visual work, read this file, PRODUCT.md and `tokens/` (start at `tokens/opendesigner.resolver.json`).",
            f"2. Use tokens, never raw values: CSS `var(--{prefix}-...)`, Tailwind classes from `build/tailwind/theme.css`, `{prefix.upper()}.*` in Swift, "
            f"`{prefix.capitalize()}Theme` in Compose.",
            "3. Do not change a locked decision without asking the owner.",
            "4. To change the system: `engine.py set <path> <value> --why \"...\"`, then `engine.py generate`, `engine.py validate`, `engine.py design-md`.",
            "5. To extend: add a decision (never hand-edit tokens or this file). Keep semantic names the same across modes. Deprecate instead of deleting."]
    out.append(section("For Agents", "\n".join(body)))
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
    out.append(sec("Product", ctx.get("product") or state.get("summary") or "Not recorded yet (Stage 01)."))
    out.append(sec("Audience", ctx.get("audience") or "Not recorded yet (Q-aud-01)."))
    out.append(sec("Surfaces", "\n".join(f"- {s.get('name')}: {s.get('mode')} mode" if isinstance(s, dict) else f"- {s}" for s in surf)
                   or "Not recorded yet. Each surface gets a mode: Persuade, Operate, Read or Experience."))
    out.append(sec("Memorable Thing", ctx.get("memorable") or "Not recorded yet (Q-brand-02)."))
    pr = state.get("principles") or []
    out.append(sec("Principles", ("\n".join(f"{i}. {p}" for i, p in enumerate(pr, 1)) + "\n\nTie-break: the higher-ranked principle wins.")
                   if pr else "Not recorded yet (Q-brand-04)."))
    cons = [f"Accessibility: WCAG 2.2 {raw.get('contrastTarget', 'AA')}", f"Platforms: {', '.join(raw.get('platforms') or [])}"]
    cons += ctx.get("constraints") or []
    out.append(sec("Constraints", "\n".join(f"- {c}" for c in cons)))
    out.append(sec("Scope", "**In:** " + (", ".join(sc.get("in") or []) or "not recorded yet") + "\n\n**Out:** " + (", ".join(sc.get("out") or []) or "not recorded yet")))
    out.append(sec("Team and Governance", ctx.get("team") or "Not recorded yet (Stage 25)."))
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


def render_preview(files, meta, state):
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
.ds-btn.primary{{background:{V('color.bg.action.primary')};color:{V('color.text.onAction')}}}
.ds-btn.primary:hover,.ds-btn.primary.is-hover{{background:{V('color.bg.action.primaryHover')}}}
.ds-btn.primary:active,.ds-btn.primary.is-pressed{{background:{V('color.bg.action.primaryPressed')}}}
.ds-btn.secondary{{background:{V('color.bg.neutral.subtle')};color:{V('color.text.primary')}}}
.ds-btn.secondary:hover,.ds-btn.secondary.is-hover{{background:{V('color.bg.neutral.subtleHover')}}}
.ds-btn.outline{{background:transparent;color:{V('color.text.primary')};border-color:{V('color.border.default')}}}
.ds-btn.danger{{background:{V('color.bg.danger.bold')};color:{V('color.text.onDanger')}}}
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
.motion-box{{transition:transform {V('motion.duration.mediumExit')} {V('motion.easing.exit')}}}
@media (prefers-reduced-motion: reduce){{.pv-card:hover .motion-box{{transform:none}}}}
"""
    chips = "".join(f'<span class="pv-chip">{_esc(k)} <b>{v}</b></span>' for k, v in dials.items())
    chips += f'<span class="pv-chip">body <b>{tinfo["base"]}px x {tinfo["ratio"]}</b></span>'
    chips += f'<span class="pv-chip">unit <b>{sinfo["unit"]}px</b></span>'
    chips += f'<span class="pv-chip">radius <b>{shp["control"]}</b></span>'
    chips += f'<span class="pv-chip">depth <b>{_esc(meta["elevation"]["model"])}</b></span>'
    if state.get("raw", {}).get("brandColor"):
        chips += f'<span class="pv-chip">brand <b>{_esc(state["raw"]["brandColor"])}</b></span>'

    def components(theme):
        head = "headline.sm" if "text.headline.sm" in base else ("title.lg" if "text.title.lg" in base else "title.md")
        return f"""<div class="pv-theme" data-theme="{theme}">
<p class="pv-theme-label">{theme} theme</p>
<div style="{t('text.' + head)}margin:0 0 4px">Invite your team</div>
<p style="{t('text.body.md')}color:{V('color.text.secondary')};margin:0 0 16px">Collaborators can edit tokens and propose decisions. <a class="ds-link" href="#">Learn about roles</a></p>
<div class="pv-row"><button class="ds-btn primary">Send invite</button><button class="ds-btn primary is-hover">Hover</button><button class="ds-btn primary is-pressed">Pressed</button><button class="ds-btn primary is-focus">Focus</button><button class="ds-btn primary" disabled>Disabled</button></div>
<div class="pv-row"><button class="ds-btn secondary">Secondary</button><button class="ds-btn outline">Outline</button><button class="ds-btn danger">Delete</button></div>
<div class="pv-row" style="align-items:flex-start">
 <label class="ds-field"><span class="ds-label">Email</span><input class="ds-input" placeholder="name@company.com"><span class="ds-help">We never share it.</span></label>
 <label class="ds-field"><span class="ds-label">Workspace</span><input class="ds-input is-error" value="acme corp"><span class="ds-help err">Use lowercase letters and dashes.</span></label>
 <label class="ds-field"><span class="ds-label">Plan</span><input class="ds-input" value="Team" disabled><span class="ds-help">Set by your admin.</span></label>
</div>
<div class="pv-row" style="align-items:stretch">
 <div class="ds-card" style="flex:1;min-width:220px"><h3>Card title</h3><p>Raised surface, container radius, inset xl, elevation.raised.</p>
  <div class="pv-row" style="margin:0"><span class="ds-badge" style="background:{V('color.bg.accent.subtle')};color:{V('color.text.accent')}">Accent</span><span class="ds-badge" style="background:{V('color.bg.success.subtle')};color:{V('color.text.success')}">Success</span><span class="ds-badge" style="background:{V('color.bg.warning.subtle')};color:{V('color.text.warning')}">Warning</span></div></div>
 <div style="flex:1;min-width:220px;display:flex;flex-direction:column;gap:8px">
  <div class="ds-banner" style="background:{V('color.bg.info.subtle')};color:{V('color.text.info')}">Info: tokens regenerated.</div>
  <div class="ds-banner" style="background:{V('color.bg.danger.subtle')};color:{V('color.text.danger')}">Error: contrast pair failed.</div>
  <div class="ds-banner" style="background:{V('color.bg.inverse')};color:{V('color.text.inverse')}">Inverse: toast and tooltip.</div>
 </div>
</div></div>"""
    html = [f"<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">",
            f"<title>{name} preview</title><style>\n{css}\n{ui_css}</style></head><body><div class=\"pv-wrap\">",
            f"<h1 class=\"pv-h1\">{name}</h1><p class=\"pv-sub\">{_esc(state.get('summary') or 'Generated by the OpenDesigner engine')} &middot; OpenDesigner engine {ENGINE_VERSION}</p>",
            f"<div class=\"pv-chips\">{chips}</div>",
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
    for r in ("detail", "controlSm", "control", "container", "overlay", "full"):
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
    write_text(path, render_preview(files, meta, state))
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


def fit_reference(ref):
    """Run LEVERS E3 backwards on a measurement file (engine schema or opendesigner-extract css_scan --json output)."""
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
        al = max([a for a in (_shadow_alpha(s) for s in shadows) if a is not None] or [0])
        if al and hint in ("shadow-ladder", "ring+faint-shadow"):
            pos = 16 + (clamp(al, 0.08, 0.24) - 0.08) / 0.16 * 84
            lo, hi = (16, 35) if hint == "ring+faint-shadow" else (56, 80)
            v = int(round(clamp(pos, lo, hi)))
        add("dials.depth", v, conf("depth"), f"{hint}" + (f", max shadow alpha {al}" if al else "") + " -> A6 bands")
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
    fams = ty.get("families") or m.get("fontFamilies") or []
    if fams:
        if tag == "our-product":
            add("raw.textFace", fams[0], "high", "the person's own product; confirm the licence covers web and apps (hook H-type)")
        else:
            notes.append(f"Typeface {fams[0]} is not carried; pick an open face of the same classification (identity rule, spec 5.4).")
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
    fit = fit_reference(ref)
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


def cmd_build(d):
    files, meta, _ = cmd_generate(d, quiet=True)
    cmd_export(d, "all", files, meta, quiet=True)
    cmd_design_md(d, files=files, meta=meta, quiet=True)
    cmd_preview(d, files=files, meta=meta, quiet=True)
    print(f"built {d}: tokens, build/ (css, tailwind, figma, paper, swift, compose, dtcg), DESIGN.md, PRODUCT.md, preview.html")
    rep = validate_dir(d)
    print_report(rep, d)
    return 1 if rep.count("error") else 0


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
    sub.add_parser("build", parents=[common], help="generate + export all + design-md + preview + validate")
    p = sub.add_parser("sketch", parents=[common], help="Level 0: a complete coarse system from about five answers")
    p.add_argument("--name")
    p.add_argument("--brand", help="brand color hex")
    p.add_argument("--audience", choices=["dense", "regular", "large"])
    p.add_argument("--platforms", help="comma list: web,ios,android,desktop,secondary")
    p.add_argument("--feel", help="comma list of brand macros: playful, serious, friendly, authoritative, minimal, rich, premium, everyday, modern, heritage, bold, deferential")
    p.add_argument("--theme", choices=["system-light-dark", "light-dark-toggle", "light-only", "dark-only"])
    p = sub.add_parser("review", parents=[common], help="find hard-coded values that bypass tokens and stale DESIGN.md sections")
    p.add_argument("--project", default=None, help="folder to scan (default: the project root)")
    p.add_argument("--strict", action="store_true", help="exit 1 when anything is found")
    p.add_argument("--json", action="store_true")
    p = sub.add_parser("feedback", parents=[common], help="record a gap, bug, confusing step or idea and print an issue link")
    p.add_argument("text")
    p.add_argument("--kind", default="idea", choices=list(FEEDBACK_KINDS))
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
        return 1 if rep.count("error") else 0
    elif a.cmd == "export":
        cmd_export(d, a.format)
    elif a.cmd == "design-md":
        cmd_design_md(d, a.out)
    elif a.cmd == "preview":
        cmd_preview(d, a.open)
    elif a.cmd == "intake":
        cmd_intake(d, a.file, a.accept, a.json)
    elif a.cmd == "build":
        return cmd_build(d)
    elif a.cmd == "sketch":
        return cmd_sketch(d, a.name, a.brand, a.audience, a.platforms, a.feel, a.theme)
    elif a.cmd == "review":
        return cmd_review(d, a.project, a.strict, a.json)
    elif a.cmd == "feedback":
        os.makedirs(d, exist_ok=True)
        cmd_feedback(d, a.text, a.kind, area=a.area, question=a.question)
    return 0



# =============================================================================================
# Zoom levels, sketch (Level 0), review, feedback (BRIEF requirements 12-16)
# =============================================================================================

def zoom_levels(d, state):
    """Each area's zoom: the explicit state.zoom value, or inferred from the decisions made in that area
    (0 -> sketch, 1-2 -> broad, 3-5 -> defined, 6+ or any detached override -> detailed) [inferred thresholds]."""
    decs = _decisions(d)
    out = {}
    for key, title in ZOOM_AREAS:
        rx = SECTION_PATHS.get(title)
        n = sum(1 for k, v in decs.items() if rx and re.match(rx, k) and v["set_by"] != "auto_default")
        over = any(re.match(rx, k) for k in decs if k.startswith("overrides.")) if rx else False
        lvl = 3 if (n >= 6 or over) else 2 if n >= 3 else 1 if n >= 1 else 0
        if key == "overview":
            lvl = max(lvl, 1 if any(k in decs for k in LEVEL0) else 0)
        explicit = (state.get("zoom") or {}).get(key)
        if explicit in ZOOM_LEVELS:
            lvl = max(lvl, ZOOM_LEVELS.index(explicit))
        answered = set((state.get("answers") or {}).keys())
        out[key] = {"level": ZOOM_LEVELS[lvl], "decisions": n, "next": [q for q in ZOOM_NEXT.get(key, []) if q not in answered]}
    return out


def cmd_sketch(d, name=None, brand=None, audience=None, platforms=None, feel=None, theme=None, quiet=False):
    """Level 0: about five answers give a complete, coarse system; everything else stays on defaults."""
    if not os.path.exists(os.path.join(d, "state.json")):
        cmd_init(d, name=name)
    why = "sketch: Level 0 answer"
    if audience:
        cmd_set(d, "answers.Q-aud-01", audience, why, quiet=True)
    if brand:
        cmd_set(d, "raw.brandColor", brand, why, quiet=True)
    if platforms:
        cmd_set(d, "answers.Q-plat-01", [p.strip() for p in platforms.split(",") if p.strip()], why, quiet=True)
    if feel:
        macros = [m.strip() for m in feel.split(",") if m.strip()]
        known = {m["id"] for m in levers()["macros"]}
        bad = [m for m in macros if m not in known]
        if bad:
            raise SystemExit(f"Unknown feel word {bad}. Choose from: {', '.join(sorted(known))}.")
        cmd_set(d, "macros", macros, why, quiet=True)
    if theme:
        cmd_set(d, "answers.Q-theme-01", theme, why, quiet=True)
    code = cmd_build(d) if not quiet else 0
    if not quiet:
        print("This is a sketch: every part works, and most choices are still defaults. Zoom into any area later (see the Zoom lines in DESIGN.md).")
    return code


REVIEW_EXT = {".css", ".scss", ".sass", ".less", ".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte", ".html", ".swift", ".kt", ".kts"}
REVIEW_SKIP = {"node_modules", ".git", "dist", "build", ".next", "out", "vendor", "coverage", "Pods", ".gradle", "opendesigner",
               "DerivedData", "__pycache__", ".venv", "venv"}
RX_HEX = re.compile(r"(?<![\w&])#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b")
RX_FN = re.compile(r"\b(rgba?|hsla?|oklch)\(\s*[\d.]")
RX_SWIFT_COLOR = re.compile(r"\b(Color|UIColor|NSColor)\(\s*(red|\.sRGB|hue|white)")
RX_KT_COLOR = re.compile(r"\bColor\(\s*0x[0-9A-Fa-f]{6,8}")
RX_SIZE = re.compile(r"\b(padding|margin|gap|row-gap|column-gap|font-size|border-radius|inset|top|left|right|bottom|width|height)"
                     r"(-[a-z]+)?\s*:\s*(-?\d+(?:\.\d+)?)px")
RX_RADIUS_NATIVE = re.compile(r"(cornerRadius\s*[:(]\s*(\d+)|RoundedCornerShape\(\s*(\d+)\.dp|\.padding\(\s*(\d+)\s*\)|(\d+)\.dp\b)")


def _nearest_color(hx, palette):
    L1 = hex_to_oklch(hx)
    a1 = oklch_to_oklab(*L1)

    def dist(h2):
        a2 = oklch_to_oklab(*hex_to_oklch(h2))
        return sum((x - y) ** 2 for x, y in zip(a1, a2)) ** 0.5
    best = min(palette.items(), key=lambda kv: (dist(kv[1]), kv[0]))
    return best[0], dist(best[1])


def cmd_review(d, project=None, strict=False, as_json=False, limit=40):
    """End-of-implementation check: hard-coded values that bypass tokens, and stale DESIGN.md sections."""
    state = merge_defaults(load_state(d))
    files, meta, _ = generate_system(load_state(d))
    prefix = slug(meta.get("prefix") or "ds").replace("-", "")
    if project is None:
        project = os.path.dirname(os.path.abspath(d)) if os.path.basename(os.path.abspath(d)) == DEFAULT_DIR else os.getcwd()
    light = resolve_all(files, {"theme": meta["modes"][0]} if "theme" in files["opendesigner.resolver.json"].get("modifiers", {}) else {})
    palette = {p: hex_of(t["resolved"]) for p, t in light.items() if t["type"] == "color" and re.match(r"color\.(surface|text|bg|border|icon)\.", p)
               and not (t["resolved"] or {}).get("alpha")}
    ladder = meta["space"]["ladder"]
    radii = {k: v for k, v in (("detail", meta["shape"]["detail"]), ("control", meta["shape"]["control"]),
                               ("container", meta["shape"]["container"]), ("overlay", meta["shape"]["overlay"])) if isinstance(v, int)}
    sizes = meta["type"]["sizes"]
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
            for i, line in enumerate(lines, 1):
                if "var(--" in line and not RX_HEX.search(line):
                    continue
                if re.search(r"^\s*(//|/\*|\*|<!--)", line) or "od-ignore" in line:
                    continue
                for m in RX_HEX.finditer(line):
                    hx = "#" + (m.group(1) if len(m.group(1)) == 6 else "".join(c * 2 for c in m.group(1)))
                    if re.match(r"\s*--", line):  # a custom property definition is a token source, not a bypass
                        continue
                    tokn, dd = _nearest_color(hx.lower(), palette) if palette else (None, 0)
                    findings.append({"kind": "color", "file": rel, "line": i, "value": hx,
                                     "fix": f"use var({css_var(prefix, tokn)})" + (" (closest match)" if dd > 0.02 else "") if tokn else "use a color token"})
                if RX_FN.search(line) and not re.match(r"\s*--", line):
                    findings.append({"kind": "color", "file": rel, "line": i, "value": RX_FN.search(line).group(0) + "...)",
                                     "fix": "use a color token (var(--" + prefix + "-color-...))"})
                if ext == ".swift" and RX_SWIFT_COLOR.search(line):
                    findings.append({"kind": "color", "file": rel, "line": i, "value": RX_SWIFT_COLOR.search(line).group(0) + "...)",
                                     "fix": f"use {prefix.upper()}.Colors.<role> from build/swift/DesignTokens.swift"})
                if ext in (".kt", ".kts") and RX_KT_COLOR.search(line) and "DesignTokens" not in rel:
                    findings.append({"kind": "color", "file": rel, "line": i, "value": RX_KT_COLOR.search(line).group(0) + ")",
                                     "fix": f"use Local{prefix.capitalize()}Colors.current.<role>"})
                for m in RX_SIZE.finditer(line):
                    prop, val = m.group(1), float(m.group(3))
                    if val == 0 or (prop in ("width", "height", "top", "left", "right", "bottom", "inset") and val not in ladder):
                        continue
                    if prop == "border-radius":
                        near = min(radii.items(), key=lambda kv: (abs(kv[1] - val), kv[0])) if radii else None
                        fix = f"use var({css_var(prefix, 'radius.' + near[0])})" if near else "use a radius token"
                        findings.append({"kind": "radius", "file": rel, "line": i, "value": f"{prop}: {val:g}px", "fix": fix})
                    elif prop == "font-size":
                        near = min(sizes, key=lambda x: (abs(x - val), x))
                        findings.append({"kind": "size", "file": rel, "line": i, "value": f"{prop}: {val:g}px",
                                         "fix": f"use a text style (for example .{prefix}-text-body-md) or var({css_var(prefix, 'font.size.' + str(near))})"})
                    else:
                        near = min(ladder, key=lambda x: (abs(x - val), x))
                        findings.append({"kind": "size", "file": rel, "line": i, "value": f"{prop}: {val:g}px",
                                         "fix": f"use var({css_var(prefix, 'space.' + str(near))})" + ("" if near == val else f" ({val:g} is off the {meta['space']['unit']}px ladder)")})
                if ext in (".swift", ".kt", ".kts") and "DesignTokens" not in rel:
                    for m in RX_RADIUS_NATIVE.finditer(line):
                        findings.append({"kind": "size", "file": rel, "line": i, "value": m.group(0),
                                         "fix": f"use {prefix.upper()}.Space / {prefix.upper()}.Radius (Swift) or {prefix.capitalize()}Space (Compose)"})
                        break
    # stale DESIGN.md / PRODUCT.md sections: render now and compare section by section
    stale = []
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
    else:
        missing = ["DESIGN.md"]
    by = {}
    for f_ in findings:
        by[f_["kind"]] = by.get(f_["kind"], 0) + 1
    result = {"project": project, "filesScanned": scanned, "counts": by, "findings": findings[:500], "staleSections": stale,
              "missing": missing}
    if as_json:
        print(json.dumps(result, indent=2))
    else:
        total = len(findings)
        print(f"Review of {project}: {scanned} files scanned.")
        if total:
            print(f"{total} hard-coded value{'s' if total != 1 else ''} skip the tokens: "
                  + ", ".join(f"{n} {k}{'s' if n != 1 else ''}" for k, n in sorted(by.items())) + ".")
            for f_ in findings[:limit]:
                print(f"  {f_['file']}:{f_['line']}  {f_['value']}  ->  {f_['fix']}")
            if total > limit:
                print(f"  ... and {total - limit} more (use --json for all).")
            print("  To keep a raw value on purpose, add the comment od-ignore on that line.")
        else:
            print("No hard-coded colors, sizes or radii found: the code uses the tokens.")
        if missing == ["DESIGN.md"]:
            print("DESIGN.md is missing. Run `engine.py design-md`.")
        elif stale:
            print(f"DESIGN.md is out of date in {len(stale)} section{'s' if len(stale) != 1 else ''}: {', '.join(stale)}. "
                  "Fix: run `engine.py design-md`. Notes inside od:keep blocks are kept.")
        else:
            print("DESIGN.md matches state.json.")
    return 1 if strict and (findings or stale or missing) else 0


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
    if not quiet:
        print(f"Saved to {fp}.")
        print("To report it, open this link, check it, and submit it yourself (nothing was posted):")
        print(url)
    return url


if __name__ == "__main__":
    sys.exit(main())
