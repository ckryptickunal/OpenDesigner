"""The answer key: @primer/primitives 11.10.0 light theme, every value resolved to px or #rrggbb(aa), by category."""
import re, json, pathlib, sys
from norm import defs

def hexify(c):
    c = c.strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", c)
    if m:
        h = m.group(1)
        if len(h) in (3, 4): h = "".join(ch * 2 for ch in h)
        if len(h) == 8 and h.endswith("ff"): h = h[:6]
        return "#" + h
    m = re.fullmatch(r"rgba?\(\s*([\d.]+)[ ,]+([\d.]+)[ ,]+([\d.]+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", c)
    if m:
        r, g, b = (round(float(x)) for x in m.groups()[:3]); a = m.group(4)
        a = 1.0 if a is None else (float(a[:-1]) / 100 if a.endswith("%") else float(a))
        h = f"#{r:02x}{g:02x}{b:02x}"
        return h if a >= 0.999 else h + f"{round(a * 255):02x}"
    return None

def px(v):
    m = re.fullmatch(r"(-?[\d.]+)(px|rem)?", v.strip())
    if not m: return None
    n = float(m.group(1)) * (16 if m.group(2) == "rem" else 1)
    return round(n, 2)

def build(keydir):
    files = {p.relative_to(keydir).as_posix(): p.read_text() for p in pathlib.Path(keydir).rglob("*.css") if p.name != "key.css"}
    d = {}
    for t in files.values():
        for k, v in defs(t).items(): d.setdefault(k, set()).update(v)
    def res(v, depth=0):
        if depth > 10: return v
        return re.sub(r"var\((--[\w-]+)(?:,[^()]*)?\)", lambda m: res(sorted(d.get(m.group(1), {m.group(0)}))[0], depth + 1), v)
    R = {k: res(sorted(v)[0]) for k, v in d.items()}
    color = {k: hexify(v) for k, v in R.items() if hexify(v) and "shadow" not in k}
    size_names = lambda k: re.search(r"base-size|space|gap|padding|margin|inset|stack|control-.*-(size|gap|padding)|overlay-.*padding|spacing", k)
    spacing = {k: px(v) for k, v in R.items() if size_names(k) and px(v) is not None and px(v) > 0}
    fsize = {k: px(v) for k, v in R.items() if re.search(r"text-size|-size$", k) and re.search(r"text", k) and px(v) is not None}
    radius = {k: px(v) for k, v in R.items() if k.startswith("--borderRadius") and px(v) is not None}
    shadow = {k: R[k] for k in R if "shadow" in k.lower() and re.search(r"\dpx|\d \d", R[k])}
    return {"color": color, "spacing": spacing, "fontSize": fsize, "radius": radius, "shadow": shadow, "fontStack": R.get("--fontStack-system")}

if __name__ == "__main__":
    k = build(sys.argv[1]); out = pathlib.Path(sys.argv[2]); out.write_text(json.dumps(k, indent=1))
    for cat in ("color", "spacing", "fontSize", "radius", "shadow"):
        vals = sorted(set(k[cat].values()), key=str)
        print(cat, len(k[cat]), "tokens,", len(vals), "distinct values", vals[:40] if cat != "color" and cat != "shadow" else "")
