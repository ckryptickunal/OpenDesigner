import re
def norm(v):
    v = re.sub(r"\s+", " ", v.strip().lower())
    v = re.sub(r"(?<![\w.])0\.(\d)", r".\1", v)          # 0.75 -> .75
    v = re.sub(r"(\.\d*?)0+(?=[a-z%\s,)]|$)", r"\1", v)   # trailing zeros
    v = re.sub(r"#([0-9a-f])\1([0-9a-f])\2([0-9a-f])\3\b", r"#\1\2\3", v)  # #ffffff -> #fff
    v = re.sub(r"\b0(px|rem|em)\b", "0", v)
    return v.replace(", ", ",")
def defs(t):
    d = {}
    for k, v in re.findall(r"(--[A-Za-z0-9_-]+)\s*:\s*([^;{}]+)", t): d.setdefault(k, set()).add(norm(v))
    return d
