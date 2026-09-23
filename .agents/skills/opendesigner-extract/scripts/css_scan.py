#!/usr/bin/env python3
"""Read design values from a repo's CSS and token files (or from read_page.js output) and fit them
to OpenDesigner's formulas run backwards (synthesis/LEVERS.md section E).

    python3 css_scan.py path/to/repo [more paths]      scan .css .scss .less .html .jsx .tsx .vue .svelte, tailwind config, *.tokens.json
    python3 css_scan.py --from-json page.json          analyse values captured in a browser by read_page.js
    add --json for machine output (default: a short readable report)

Every value is labelled with how it was obtained: "declared" (written in source files; not necessarily
rendered) or "computed" (read from a live page). Nothing here decides anything: the person accepts,
adjusts or ignores each value. Standard library only; no network.
"""
import argparse, json, math, os, re, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
INTAKE = HERE.parent / "references" / "reference-intake.json"
EXT = {".css", ".scss", ".less", ".html", ".htm", ".jsx", ".tsx", ".js", ".ts", ".vue", ".svelte"}
SKIP = {"node_modules", ".git", "dist", "build", ".next", "vendor", "coverage", "opendesigner"}
NUM = r"(-?\d*\.?\d+)(px|rem|em|ms|s)?"


def px(v, unit):
    v = float(v)
    return v * 16 if unit in ("rem", "em") else v


# ---------- colour maths (sRGB hex -> OKLCH) ----------
def hex_norm(h):
    h = h.lstrip("#").lower()
    if len(h) in (3, 4):
        h = "".join(c * 2 for c in h)
    return "#" + h[:6] if len(h) in (6, 8) else None


def oklch(h):
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (1, 3, 5))
    lin = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in (r, g, b)]
    l = 0.4122214708 * lin[0] + 0.5363325363 * lin[1] + 0.0514459929 * lin[2]
    m = 0.2119034982 * lin[0] + 0.6806995451 * lin[1] + 0.1073969566 * lin[2]
    s = 0.0883024619 * lin[0] + 0.2817188376 * lin[1] + 0.6299787005 * lin[2]
    l, m, s = (math.copysign(abs(x) ** (1 / 3), x) for x in (l, m, s))
    L = 0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s
    a = 1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s
    bb = 0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s
    return round(L, 3), round(math.hypot(a, bb), 3), round(math.degrees(math.atan2(bb, a)) % 360)


def rgb_to_hex(m):
    parts = [p for p in re.split(r"[\s,/]+", m.strip()) if p][:3]
    try:
        vals = [round(float(p[:-1]) * 2.55) if p.endswith("%") else round(float(p)) for p in parts]
        return "#" + "".join(f"{max(0, min(255, v)):02x}" for v in vals)
    except ValueError:
        return None


# ---------- capture from files ----------
def scan_files(paths):
    V = {k: Counter() for k in ("colors", "fontFamilies", "fontSizes", "lineHeights", "fontWeights",
                                "spacing", "radii", "shadows", "durations", "easings")}
    props, files = {}, 0
    for root in paths:
        root = Path(root)
        items = [root] if root.is_file() else [p for p in root.rglob("*") if p.is_file()
                                               and not (set(p.parts) & SKIP)]
        for f in items:
            name = f.name.lower()
            if f.suffix.lower() not in EXT and not name.startswith("tailwind.config") and not name.endswith(".tokens.json"):
                continue
            try:
                t = f.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            if len(t) > 2_000_000:
                continue
            files += 1
            for k, v in re.findall(r"(--[\w-]+)\s*:\s*([^;}\n]+)", t):
                props.setdefault(k, v.strip())
            for h in re.findall(r"#[0-9a-fA-F]{3,8}\b", t):
                n = hex_norm(h)
                if n:
                    V["colors"][n] += 1
            for m in re.findall(r"rgba?\(([^)]+)\)", t):
                n = rgb_to_hex(m)
                if n:
                    V["colors"][n] += 1
            for m in re.findall(r"font-family\s*:\s*([^;}\n]+)", t):
                V["fontFamilies"][m.split(",")[0].strip(" '\"")] += 1
            for v, u in re.findall(r"font-size\s*:\s*" + NUM, t):
                if u in ("px", "rem", "em"):
                    V["fontSizes"][round(px(v, u))] += 1
            for v in re.findall(r"font-weight\s*:\s*(\d{3})", t):
                V["fontWeights"][int(v)] += 1
            for v, u in re.findall(r"line-height\s*:\s*" + NUM, t):
                V["lineHeights"][f"{v}{u or ''}"] += 1
            for prop, rest in re.findall(r"\b(padding|margin|gap|row-gap|column-gap)[\w-]*\s*:\s*([^;}\n]+)", t):
                for v, u in re.findall(NUM, rest):
                    if u in ("px", "rem") and 0 < px(v, u) <= 160:
                        V["spacing"][round(px(v, u))] += 1
            for rest in re.findall(r"border-radius\s*:\s*([^;}\n]+)", t):
                for v, u in re.findall(NUM, rest)[:1]:
                    if u in ("px", "rem"):
                        V["radii"][round(px(v, u))] += 1
                    elif "%" in rest or "9999" in rest:
                        V["radii"]["full"] += 1
            for m in re.findall(r"box-shadow\s*:\s*([^;}\n]+)", t):
                V["shadows"][m.strip()] += 1
            for rest in re.findall(r"transition(?:-duration)?\s*:\s*([^;}\n]+)", t):
                for v, u in re.findall(r"(\d*\.?\d+)(ms|s)\b", rest)[:1]:
                    V["durations"][round(float(v) * (1000 if u == "s" else 1))] += 1
                for e in re.findall(r"(cubic-bezier\([^)]+\)|ease-in-out|ease-out|ease-in|linear\([^)]*\)|\bease\b)", rest):
                    V["easings"][e] += 1
    return {"method": "declared", "files": files, "customProperties": props,
            "values": {k: dict(v.most_common(40)) for k, v in V.items()}}


# ---------- analysis ----------
def fit_type(sizes):
    s = sorted({float(x) for x in sizes if str(x).replace(".", "").isdigit() and 9 <= float(x) <= 120})
    if len(s) < 3:
        return None
    best = None
    for base in [x for x in s if 12 <= x <= 20] or s[:1]:
        for r in (1.067, 1.125, 1.2, 1.25, 1.333, 1.414, 1.5, 1.618):
            err = sum(min(abs(math.log(x / base) - n * math.log(r)) for n in range(-3, 13)) for x in s) / len(s)
            if best is None or err < best[2]:
                best = (base, r, err)
    base, r, err = best
    return {"base": base, "ratio": r, "meanLogResidual": round(err, 4),
            "reading": "modular scale" if err < 0.03 else "loose fit: keep measured sizes as overrides",
            "sizes": s}


def fit_space(vals):
    v = [float(x) for x in vals for _ in range(int(vals[x]))]
    if not v:
        return None
    share = {u: round(sum(1 for x in v if x % u == 0) / len(v), 2) for u in (8, 5, 4)}
    unit = next((u for u in (8, 5, 4) if share[u] >= 0.7), 4)
    return {"unit": unit, "shareDivisible": share, "steps": sorted({int(x) for x in vals})[:16]}


def dial_from_band(drives, param, value):
    for d in drives:
        if d["param"] == param and d["map"]["kind"] == "bands":
            for lo, hi, out in d["map"]["bands"]:
                if out == value:
                    return (lo + hi) // 2
            nums = [(abs(out - value), (lo + hi) // 2) for lo, hi, out in d["map"]["bands"]
                    if isinstance(out, (int, float)) and isinstance(value, (int, float))]
            if nums:
                return min(nums)[1]
    return None


def analyse(cap):
    vals = cap["values"]
    dials = {d["id"]: d for d in json.loads(INTAKE.read_text())["dials"]} if INTAKE.exists() else {}
    out = {"method": cap.get("method"), "source": cap.get("source"), "files": cap.get("files")}
    cols = [(h, n) for h, n in vals.get("colors", {}).items() if h]
    neutrals, accents = [], []
    for h, n in cols:
        L, C, H = oklch(h)
        (neutrals if C < 0.03 else accents).append({"hex": h, "count": n, "oklch": [L, C, H]})
    out["color"] = {"accents": accents[:6], "neutrals": neutrals[:8],
                    "note": "the reference's accent hue is identity: carry its role and chroma level, not the hex"}
    if neutrals:
        mid = sorted(neutrals, key=lambda x: abs(x["oklch"][0] - 0.6))[0]["oklch"]
        out["color"]["neutralTint"] = {"chroma": mid[1], "hue": mid[2]}
    if accents:
        out["color"]["accentChroma"] = accents[0]["oklch"][1]
    out["type"] = {"families": list(vals.get("fontFamilies", {}))[:5], "scale": fit_type(vals.get("fontSizes", {})),
                   "weights": sorted(int(w) for w in vals.get("fontWeights", {}))}
    out["space"] = fit_space(vals.get("spacing", {}))
    radii = Counter({k: v for k, v in vals.get("radii", {}).items()})
    if radii:
        top = radii.most_common(1)[0][0]
        top = "full" if top == "full" else int(float(top))
        rd = dial_from_band(dials.get("roundness", {}).get("drives", []), "radius.control", top)
        out["radius"] = {"mostCommon": top, "all": dict(radii.most_common(8)), "roundnessDial": rd}
    sh = list(vals.get("shadows", {}))
    out["depth"] = {"shadows": sh[:5], "hint": "borders" if not sh else
                    ("ring+faint-shadow" if any(re.search(r"0 0 0 1px", s) for s in sh) else "shadow-ladder")}
    du = sorted(float(d) for d in vals.get("durations", {}))
    if du:
        med = du[len(du) // 2]
        out["motion"] = {"durations": du[:10], "median": med, "durationMultiplier": round(med / 275, 2),
                         "easings": list(vals.get("easings", {}))[:5],
                         "note": "declared CSS only; JavaScript-driven motion needs a live browser" if cap.get("method") == "declared" else ""}
    else:
        out["motion"] = {"note": "no motion found; do not infer Energy from this source"}
    out["neverInferred"] = ["brandPresence (always ask)", "intent, audience, principles"]
    return out


def report(a):
    L = [f"Source method: {a['method']} ({a.get('files') or 0} files)"]
    c = a["color"]
    L.append("Accent candidates: " + (", ".join(f"{x['hex']} x{x['count']} (C {x['oklch'][1]})" for x in c["accents"][:4]) or "none"))
    if c.get("neutralTint"):
        L.append(f"Neutral tint: chroma {c['neutralTint']['chroma']}, hue {c['neutralTint']['hue']} (Warmth dial)")
    t = a["type"]
    L.append("Type families: " + (", ".join(t["families"]) or "none"))
    if t["scale"]:
        L.append(f"Type scale: base {t['scale']['base']} x {t['scale']['ratio']} ({t['scale']['reading']})")
    if a["space"]:
        L.append(f"Spacing unit: {a['space']['unit']} (share divisible {a['space']['shareDivisible']})")
    if a.get("radius"):
        L.append(f"Radius: most common {a['radius']['mostCommon']} -> Roundness dial about {a['radius']['roundnessDial']}")
    L.append(f"Depth: {a['depth']['hint']}")
    m = a["motion"]
    L.append(f"Motion: median {m['median']} ms, multiplier {m['durationMultiplier']}" if "median" in m else f"Motion: {m['note']}")
    L.append("Always ask: brand presence, intent, audience. Never copy the accent hex, logo, typeface licence or copy.")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--from-json", help="output of read_page.js saved to a file")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.from_json:
        cap = json.loads(Path(a.from_json).read_text(encoding="utf-8"))
        cap.setdefault("method", "computed")
    elif a.paths:
        cap = scan_files(a.paths)
        cap["source"] = ", ".join(a.paths)
    else:
        ap.error("give paths to scan or --from-json")
    res = analyse(cap)
    print(json.dumps(res, indent=1) if a.json else report(res))


if __name__ == "__main__":
    main()
