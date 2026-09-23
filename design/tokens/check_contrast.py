#!/usr/bin/env python3
"""Verify the starter tokens (stdlib only).

    python3 design/tokens/check_contrast.py          # verify, print a summary, exit 1 on any failure
    python3 design/tokens/check_contrast.py --write  # also record each computed ratio in contrast-pairs.json

Checks, all computed from the token files themselves (not from build_tokens.py):
1. Every resolver permutation (theme x density x motion = 8) resolves with no missing alias and no cycle.
2. Every primitive's hex fallback matches its OKLCH components (max 1/255 per channel after rounding).
3. Every text/background pair in contrast-pairs.json meets its WCAG 2.2 minimum (4.5:1 text, 3:1 non-text)
   in its mode, using WCAG relative luminance on the sRGB hex values that Figma, Paper and browsers display.

The module also exposes resolve(theme, density, motion) for the atlas builder.
"""
import itertools
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESOLVER = os.path.join(HERE, "design-system.resolver.json")


def _load(name):
    with open(os.path.join(HERE, name)) as f:
        return json.load(f)


def _flatten(node, prefix, inherited_type, out):
    """DTCG group tree -> {dotted.path: {"$value", "$type", ...}}; $type inherits from groups."""
    t = node.get("$type", inherited_type)
    if "$value" in node:
        out[prefix] = {"$value": node["$value"], "$type": t, "$extensions": node.get("$extensions", {}),
                       "$description": node.get("$description", "")}
        return
    for k, v in node.items():
        if k.startswith("$") or not isinstance(v, dict):
            continue
        _flatten(v, f"{prefix}.{k}" if prefix else k, t, out)


def _sources_for(theme, density, motion):
    r = _load("design-system.resolver.json")
    chosen = {"theme": theme, "density": density, "motion": motion}
    files = []
    for entry in r["resolutionOrder"]:
        ref = entry["$ref"]
        kind, name = ref.split("/")[1], ref.split("/")[2]
        if kind == "sets":
            files += [s["$ref"] for s in r["sets"][name]["sources"]]
        else:
            ctx = chosen[name] or r["modifiers"][name]["default"]
            files += [s["$ref"] for s in r["modifiers"][name]["contexts"][ctx]]
    return files


def _deep_resolve(value, flat, seen):
    if isinstance(value, str) and value.startswith("{") and value.endswith("}"):
        path = value[1:-1]
        if path in seen:
            raise ValueError("alias cycle: " + " -> ".join(seen + [path]))
        if path not in flat:
            raise KeyError(f"missing alias target {path}")
        return _deep_resolve(flat[path]["$value"], flat, seen + [path])
    if isinstance(value, dict) and "colorSpace" not in value:
        return {k: _deep_resolve(v, flat, seen) for k, v in value.items()}
    if isinstance(value, list):
        return [_deep_resolve(v, flat, seen) for v in value]
    return value


def resolve(theme="light", density="comfortable", motion="standard"):
    """Merge the resolver's sources in order (last wins) and resolve every alias."""
    flat = {}
    for name in _sources_for(theme, density, motion):
        part = {}
        _flatten(_load(name), "", None, part)
        flat.update(part)
    out = {}
    for path, tok in flat.items():
        out[path] = dict(tok, resolved=_deep_resolve(tok["$value"], flat, [path]))
    return out


# ---------------------------------------------------------------- color math

def luminance(hx):
    def lin(v):
        v = v / 255
        return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (int(hx[i:i + 2], 16) for i in (1, 3, 5))
    return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)


def contrast(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def oklch_to_hex(L, C, H):
    h = math.radians(H)
    a, b = C * math.cos(h), C * math.sin(h)
    l_, m_, s_ = (L + 0.3963377774 * a + 0.2158037573 * b, L - 0.1055613458 * a - 0.0638541728 * b,
                  L - 0.0894841775 * a - 1.2914855480 * b)
    l, m, s = l_ ** 3, m_ ** 3, s_ ** 3
    rgb = (4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
           -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
           -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s)

    def enc(c):
        c = min(max(c, 0.0), 1.0)
        return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055
    return [round(enc(c) * 255) for c in rgb]


def main():
    failures = []

    # 1. permutations
    perms = list(itertools.product(("light", "dark"), ("comfortable", "compact"), ("standard", "reduced")))
    counts = []
    for p in perms:
        try:
            counts.append(len(resolve(*p)))
        except (KeyError, ValueError) as e:
            failures.append(f"resolve {p}: {e}")
    print(f"[1] resolver: {len(perms)} permutations resolved, {min(counts) if counts else 0} tokens each")

    # 2. hex fallback vs OKLCH components
    prim = {}
    _flatten(_load("color.primitives.tokens.json"), "", None, prim)
    worst = 0
    for path, tok in prim.items():
        v = tok["$value"]
        if v.get("colorSpace") != "oklch":
            continue
        want = oklch_to_hex(*v["components"])
        got = [int(v["hex"][i:i + 2], 16) for i in (1, 3, 5)]
        d = max(abs(x - y) for x, y in zip(want, got))
        worst = max(worst, d)
        if d > 1:
            failures.append(f"hex mismatch {path}: {v['hex']} vs oklch -> {want}")
    n_ok = sum(1 for t in prim.values() if t["$value"].get("colorSpace") == "oklch")
    print(f"[2] primitives: {n_ok} OKLCH colors, hex fallback max deviation {worst}/255")

    # 3. contrast pairs
    data = _load("contrast-pairs.json")
    by_mode = {m: resolve(m) for m in ("light", "dark")}
    lows = {}
    for pair in data["pairs"]:
        toks = by_mode[pair["mode"]]
        fg, bg = toks[pair["fg"]]["resolved"]["hex"], toks[pair["bg"]]["resolved"]["hex"]
        ratio = contrast(fg, bg)
        pair["fgHex"], pair["bgHex"], pair["ratio"] = fg, bg, round(ratio, 2)
        pair["pass"] = ratio >= pair["min"]
        key = (pair["mode"], pair["kind"])
        if key not in lows or ratio < lows[key][0]:
            lows[key] = (ratio, pair["fg"], pair["bg"])
        if not pair["pass"]:
            failures.append(f"contrast {pair['mode']} {pair['fg']} on {pair['bg']}: {ratio:.2f} < {pair['min']}")
    passed = sum(p["pass"] for p in data["pairs"])
    print(f"[3] contrast: {passed}/{len(data['pairs'])} pairs pass WCAG 2.2 AA")
    for (mode, kind), (ratio, fg, bg) in sorted(lows.items()):
        print(f"    lowest {mode:5s} {kind:26s} {ratio:5.2f}:1  {fg} on {bg}")

    if "--write" in sys.argv:
        with open(os.path.join(HERE, "contrast-pairs.json"), "w") as f:
            json.dump(data, f, indent=1)
            f.write("\n")
        print("    ratios recorded in contrast-pairs.json")

    if failures:
        print("FAIL")
        for f in failures:
            print("  -", f)
        sys.exit(1)
    print("OK")


if __name__ == "__main__":
    main()
