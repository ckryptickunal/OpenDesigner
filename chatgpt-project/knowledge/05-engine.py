#!/usr/bin/env python3
"""OpenDesigner engine: turns interview answers into a validated, exported design system.

Standard library only, Python 3.10+, no network. Every number it produces comes from
`references/levers.json` (the machine-readable twin of synthesis/LEVERS.md) or from a rule
cited inline with a Decision Card (DC-Lxx-nn) or source id (S-Lxx-nnn). `[inferred]` marks
choices this engine makes where the research gives a range or a direction but not a value.

Commands (run from the user's project; state lives in ./opendesigner/ unless --dir is given):
    engine.py init [--dir D] [--from path/to/state.json] [--name "Acme"]
    engine.py set <dotted.path> <json-value> [--why "reason"]    (also: set path=value, set Q-shape-01 soft)
    engine.py pick <question-id> <option-value> [--why "reason"]
    engine.py lock <dotted.path> | unlock <dotted.path>
    engine.py resolve                     print effective dials and every derived parameter (JSON)
    engine.py generate                    state.json + levers.json -> tokens/ (DTCG 2025.10 + resolver)
    engine.py validate [--json]           contrast, targets, lint; exit 1 on errors, 0 with warnings
    engine.py export --format css|tailwind|figma|paper|swift|compose|dtcg|all
    engine.py design-md                   render DESIGN.md
    engine.py preview [--open]            render preview.html (every token plus a few components)
    engine.py build                       generate + export all + design-md + preview + validate

Output layout inside the state directory:
    state.json, decisions.md, tokens/ (DTCG sets + opendesigner.resolver.json + opendesigner.meta.json),
    css/tokens.css, tailwind/theme.css, figma/variables.json, paper/tokens.json + tokens.css,
    swift/DesignTokens.swift, compose/DesignTokens.kt, dtcg/<theme>.tokens.json (flat, one mode per file),
    DESIGN.md, preview.html
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
NS = "org.opendesigner"  # $extensions namespace (DTCG requires reverse-domain keys)
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


def dump_json(path, data):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    text = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
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

HOOK_STATUSES = ["unknown", "have", "commissioning", "tool", "open-library", "placeholder", "not-needed"]
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
        "engine": ENGINE_VERSION,
        "name": name,
        "summary": "",
        "context": {"product": "", "audience": "", "surfaces": [], "mode": "standard", "memorable": ""},
        "dials": {d: None for d in DIALS},
        "preset": None,
        "macros": [],
        "raw": raw,
        "overrides": {},
        "answers": {},
        "principles": [],
        "components": {"base": None, "inventory": list(DEFAULT_COMPONENTS), "notes": {}},
        "hooks": {hid: {"status": "unknown", "question": q, "files": [], "note": ""} for hid, _n, q in hook_catalog()},
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
    explicit = {k: v for k, v in (state.get("dials") or {}).items() if v is not None}
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

    r.solve_y(8, target_y(3.0 * MARGIN, refs(3 if light else 4), light))
    # step 9: solid fill. Light text (white) or dark text on it, chosen per hue (on-color-auto, S-L06-094)
    if light:
        if text_on_solid == "light":
            r.solve_y(9, target_y(4.5 * MARGIN, 1.0, True))
        else:
            dark_text_y = neutral.y(12) if neutral else 0.012
            y_min = target_y(4.5 * MARGIN, dark_text_y, False)
            seed_L = seed[0] if seed else 0.8
            r.set_L(9, seed_L)
            if r.y(9) < y_min:
                r.solve_y(9, y_min)
        c9 = contrast_y(r.y(9), 1.0)
        y10 = target_y(c9 * 1.15, 1.0, True)
        if text_on_solid == "light":
            y10 = min(y10, target_y(tmin, refs(4), True))  # step 10 doubles as tertiary text
        else:
            dark_text_y = neutral.y(12) if neutral else 0.012
            y10 = max(y10, target_y(4.5 * MARGIN, dark_text_y, False))
        r.solve_y(10, y10)
        c10 = contrast_y(r.y(10), 1.0)
        r.solve_y(11, min(target_y(max(c10, contrast_y(r.y(9), 1.0)) * 1.22, 1.0, True),
                          target_y(tmin, refs(4), True)))
        r.solve_y(12, min(target_y(cfg["c12"], 1.0, True), target_y(7.0 * MARGIN, refs(5), True)))
    else:
        n1 = ref.y(1)
        y9 = target_y(4.5 * MARGIN, n1, False)  # dark solids are lighter and carry dark text (Material 80/20)
        r.solve_y(9, y9)
        if seed is not None:
            seed_L = min(seed[0], 0.82)
            if seed_L > r.steps[9]["L"]:
                r.set_L(9, seed_L)
        c9 = contrast_y(r.y(9), n1)
        y10 = max(target_y(c9 * 1.15, n1, False), target_y(tmin, refs(4), False))
        r.solve_y(10, y10)
        c10 = contrast_y(r.y(10), n1)
        r.solve_y(11, max(target_y(c10 * 1.2, n1, False), target_y(tmin, refs(5), False)))
        r.solve_y(12, max(target_y(cfg["c12"], n1, False), target_y(7.0 * MARGIN, refs(5), False)))
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
            return c_peak * k * curve[step - 1]
        return fn

    def solid_text_for(seed_hex, seed_L):
        if seed_hex is None:
            return "light"
        return "dark" if contrast(seed_hex, "#ffffff") < 3.0 else "light"  # brandAnchor rule (DC-L01-09)

    # status hues stay recognizable at any colorfulness; Material's fixed error palette uses chroma 84 [inferred]
    status_peak = clamp(peak + 16, 48.0, 84.0)
    specs = []  # (name, hue, peak, text_on_solid, seed(L,C,H) or None, seed_hex)
    specs.append(("accent", bH, peak, solid_text_for(brand, bL), (bL, bC, bH) if brand else None, brand))
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
    if brand and raw.get("flags", {}).get("brandExact"):
        acc = ramps[("accent", "light")]
        pinned = min(range(3, 12), key=lambda i: (abs(acc.steps[i]["L"] - bL), i))
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
            "pinnedStep": pinned, "brandAnchorStep": anchor, "statusPeakHct": rnd(status_peak, 2),
            "textMin": text_min, "ramps": [s[0] for s in specs]}
    return ramps, info


# =============================================================================================
# Token assembly
# =============================================================================================

DENSITIES = ("spacious", "comfortable", "compact")
SPACE_MULTIPLIERS = [0, 0.5, 1, 1.5, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20]  # LEVERS B8 (multiplier list [inferred])
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
                "boldPressed": tok(r("accent", 11), "Pressed solid accent (+2 steps)."),
            },
            "disabled": tok(n(3) if L else n(4), "Disabled control fill."),
            "inverse": tok(n(12), "Tooltips and toasts: the inverted surface."),
        },
        "border": {
            "subtle": tok(n(6), "Dividers and card edges (decorative)."),
            "default": tok(n(7), "Outline buttons and table grids (decorative; the label carries meaning)."),
            "strong": tok(n(8), "Boundaries that are the only cue: inputs, checkboxes, switches (3:1, WCAG 1.4.11)."),
            "input": tok(n(8), "Text field and select borders (3:1, DC-L01-16)."),
            "focus": tok(r("accent", 9) if L else r("accent", 11), "Focus ring (3:1 against every surface, DC-L04-09)."),
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
        act = (r("action", 9), r("action", 10), r("action", 11)), on("action")
        act_desc = "Primary action from its own color input."
    else:
        act = (r("accent", 9), r("accent", 10), r("accent", 11)), on("accent")
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
    base = int(raw.get("baseSize") or ctx.P("type.baseSize.web", p["type.baseSize.web"]))
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
    if len(final) < 2 or final.index(base) == 0:  # always keep one step below body for captions
        final = [round_half_up(base / ratio)] + [s for s in final if s != round_half_up(base / ratio)]
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
                "$description": f"Type scale: round({base} x {ratio}^n), n from -2 to {sc['nTop']}; sizes under {sc['minSize']}px dropped; "
                                "adjacent sizes under 10% apart merged (DC-L02-09, DC-L02-10).",
                "$extensions": {NS: {"base": base, "ratio": ratio, "displayReach": sc["reach"], "formulaSizes": sc["raw"],
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
    for m in SPACE_MULTIPLIERS:
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
