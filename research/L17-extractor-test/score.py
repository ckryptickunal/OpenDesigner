"""Score three extractors on one page against (a) what the page renders and (b) the published @primer/primitives key."""
import json, re, sys, pathlib
from key import hexify, px

S = pathlib.Path(sys.argv[1]); OUT = S / "out"
key = json.loads((OUT / "key/answer.json").read_text())
truth = json.loads((OUT / "truth/rendered.json").read_text())["rendered"]

def top_split(s):
    out, depth, cur = [], 0, ""
    for ch in s:
        depth += ch == "("; depth -= ch == ")"
        if ch == "," and depth == 0: out.append(cur); cur = ""
        else: cur += ch
    return out + [cur]

def fallback(v):  # var(--x, fallback) -> fallback (recursively); var(--x) alone -> None
    v = v.strip()
    while True:
        m = re.fullmatch(r"var\(\s*--[\w-]+\s*(?:,\s*(.*))?\)", v, re.S)
        if not m: return v
        if m.group(1) is None: return None
        v = m.group(1).strip()

def shadow_norm(s):
    s = fallback(s) if s and "var(" in s.split(",")[0] else s
    if not s or "var(" in s: return None
    layers = []
    for layer in top_split(s):
        t = layer.strip().lower(); inset = "inset" in t; t = t.replace("inset", "")
        col = re.search(r"#[0-9a-f]{3,8}\b|rgba?\([^)]*\)", t)
        c = hexify(col.group(0)) if col else None
        if col: t = t.replace(col.group(0), " ")
        nums = [px(x) for x in t.split()]
        if None in nums or not nums: return None
        nums = (nums + [0, 0, 0, 0])[:4]
        layers.append((inset, *nums, c))
    return tuple(layers)

def length(v):
    if v is None: return None
    v = str(v).strip()
    if "var(" in v: v = fallback(v) or ""
    return px(v) if v else None

near = lambda a, b: abs(a - b) <= 0.06

def score_lengths(rep, rendered, keyvals):
    rep = sorted({round(x, 2) for x in rep if x is not None and x > 0})
    inR = [x for x in rep if any(near(x, r) for r in rendered)]
    inK = [x for x in rep if any(near(x, k) for k in keyvals)]
    target = sorted({r for r in rendered if any(near(r, k) for k in keyvals)})
    got = [t for t in target if any(near(t, x) for x in rep)]
    return {"reported": len(rep), "rendered": len(inR), "onKey": len(inK), "recallRenderedKey": f"{len(got)}/{len(target)}",
            "missed": [t for t in target if t not in got], "offPage": [x for x in rep if x not in inR][:12], "values": rep[:40]}

def score_set(rep, rendered, keyvals):
    rep = {x for x in rep if x}
    inR = rep & rendered; inK = rep & keyvals; target = rendered & keyvals
    return {"reported": len(rep), "rendered": len(inR), "onKey": len(inK), "recallRenderedKey": f"{len(target & rep)}/{len(target)}",
            "missed": sorted(target - rep), "offPage": sorted(rep - rendered)[:12]}

# truth sets
T = {"color": {hexify(c) if c.startswith("#") else c for c in truth["color"]},
     "fontSize": [float(x) for x in truth["fontSize"]], "spacing": [float(x) for x in truth["spacing"]],
     "radius": [float(x) for x in truth["radius"]], "shadow": {shadow_norm(s) for s in truth["shadow"]}}
K = {"color": {c for c in key["color"].values() if c}, "fontSize": set(key["fontSize"].values()), "spacing": set(key["spacing"].values()),
     "radius": set(key["radius"].values()), "shadow": {shadow_norm(s) for s in key["shadow"].values()} - {None}}

def hexes(o):
    return {hexify(h) for h in re.findall(r"#[0-9a-fA-F]{6,8}\b|#[0-9a-fA-F]{3}\b|rgba?\([^)]*\)", json.dumps(o))} - {None}

tools = {}
# ours
o = json.loads((OUT / "ours/scan.json").read_text())
roles = o["type"].get("roles", {})
tools["OpenDesigner"] = {
    "color": hexes({k: o[k] for k in ("color", "surfaces", "components")}),
    "fontSize": list(o["type"]["scale"]["sizes"]) + [r.get("size") for r in roles.values() if isinstance(r, dict) and isinstance(r.get("size"), (int, float))],
    "spacing": o["space"]["steps"],
    "radius": [float(x) for part in ("control", "container") for x in (o["radius"].get(part) or {}).get("values", {})],
    "shadow": {shadow_norm(s) for s in o["depth"]["shadows"]}}
# dembrandt
d = json.loads((OUT / "dembrandt/tokens.json").read_text())
tools["Dembrandt"] = {
    "color": hexes({"p": [c["normalized"] for c in d["colors"]["palette"]], "s": d["colors"]["semantic"], "d": [c["normalized"] for c in d["colors"]["detected"]]}),
    "fontSize": [px(s["size"].split()[0]) for s in d["typography"]["styles"]],
    "spacing": [v["numericValue"] for v in d["spacing"]["commonValues"]],
    "radius": [px(x) for v in d["borderRadius"]["values"] for x in v["value"].split() if px(x)],
    "shadow": {shadow_norm(s["shadow"]) for s in d["shadows"]}}
# project wallace
w = json.loads((OUT / "wallace/values.json").read_text())["values"]
wun = lambda g: list((w[g].get("unique") or {}).keys())
tools["Project Wallace"] = {
    "color": {hexify(c) for c in wun("colors")} - {None},
    "fontSize": [length(v) for v in wun("fontSizes")],
    "spacing": [],
    "radius": [length(v) for v in wun("borderRadiuses")],
    "shadow": {shadow_norm(v) for v in wun("boxShadows")}}
unresolved = {g: sum(1 for v in wun(g) if length(v) is None) for g in ("fontSizes", "borderRadiuses")}

res = {}
for name, t in tools.items():
    res[name] = {"color": score_set(t["color"], T["color"], K["color"]),
                 "fontSize": score_lengths(t["fontSize"], T["fontSize"], K["fontSize"]),
                 "spacing": score_lengths(t["spacing"], T["spacing"], K["spacing"]) if t["spacing"] else {"reported": 0, "note": "no spacing output"},
                 "radius": score_lengths(t["radius"], T["radius"], K["radius"]),
                 "shadow": score_set(t["shadow"] - {None}, T["shadow"], K["shadow"])}
res["_truth"] = {k: (len(v) if not isinstance(v, list) else len(set(v))) for k, v in T.items()}
res["_truthOnKey"] = {"color": len(T["color"] & K["color"]), "fontSize": sorted({x for x in T["fontSize"] if any(near(x, k) for k in K["fontSize"])}),
                      "spacing": sorted({x for x in T["spacing"] if any(near(x, k) for k in K["spacing"])}),
                      "radius": sorted({x for x in T["radius"] if any(near(x, k) for k in K["radius"])}), "shadow": len(T["shadow"] & K["shadow"])}
res["_wallaceUnresolved"] = unresolved
(OUT / "scores.json").write_text(json.dumps(res, indent=1, default=str))
for name in tools:
    print("==", name)
    for cat, r in res[name].items(): print(f"  {cat:9}", {k: v for k, v in r.items() if k not in ("values",)})
print("truth:", res["_truth"], "| rendered and on key:", res["_truthOnKey"], "| wallace unresolved:", unresolved)
