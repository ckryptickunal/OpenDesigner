#!/usr/bin/env python3
"""Make the three example systems on the landing page with the real engine, and save their values to site/demo-systems.json.

  python3 site/demo_systems.py

Each example is one `engine.py sketch` with five answers, then `build`, in a temporary folder. Nothing is tuned by hand: the
landing page shows the light-mode values the engine wrote, plus contrast ratios measured from them. Run it again after the
engine changes, then rebuild the site.
"""
import datetime as dt
import json
import pathlib
import re
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
ENGINE = ROOT / "skills/opendesigner/scripts/engine.py"
OUT = ROOT / "site/demo-systems.json"
EXAMPLES = [
    {"key": "pebbleday", "name": "Pebbleday", "making": "a habit app for families", "who": "Used regularly", "audience": "regular",
     "where": "iPhone and web", "platforms": "ios,web", "feel": "friendly, playful", "brand": "#E0457B", "surfaces": "experience"},
    {"key": "fernhollow", "name": "Fernhollow", "making": "a public service for renewing a permit", "who": "Used now and then", "audience": "large",
     "where": "Web", "platforms": "web", "feel": "calm, trustworthy", "brand": "#1E3A8A", "surfaces": "read"},
    {"key": "billerwick", "name": "Billerwick", "making": "a finance tool for approving invoices", "who": "Used all day", "audience": "dense",
     "where": "Web", "platforms": "web", "feel": "precise, calm", "brand": "#15803D", "surfaces": "operate"},
]
TOKENS = {"bg": "color-surface-base", "sunken": "color-surface-sunken", "raised": "color-surface-raised", "text": "color-text-primary",
          "muted": "color-text-secondary", "border": "color-border-default", "sep": "color-border-separator", "primary": "color-bg-action-primary",
          "onPrimary": "color-text-on-action", "accentSoft": "color-bg-accent-subtle", "accentText": "color-text-accent",
          "okSoft": "color-bg-success-subtle", "okText": "color-text-success", "rControl": "radius-control", "rContainer": "radius-container",
          "hControl": "size-control-md", "row": "size-row-md", "body": "text-body-md-size", "label": "text-label-md-size",
          "title": "text-title-md-size", "headline": "text-headline-sm-size", "wHeading": "font-weight-heading", "wLabel": "font-weight-label",
          "inset": "space-inset-md", "stack": "space-stack-md"}


def contrast(a, b):
    def lum(h):
        r, g, b_ = (int(h.lstrip("#")[i:i + 2], 16) / 255 for i in (0, 2, 4))
        f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
        return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b_)
    hi, lo = sorted((lum(a), lum(b)), reverse=True)
    return round((hi + 0.05) / (lo + 0.05), 2)


def light_values(css):
    """The default (light, default density) value of each token, with aliases resolved and rem turned into px."""
    v = {}
    for _sel, body in re.findall(r"^(:root[^{]*){(.*?)^}", css, re.S | re.M):
        v.update(re.findall(r"--ds-([a-z0-9-]+):\s*([^;]+);", body))

    def res(x, depth=0):
        m = re.fullmatch(r"var\(--ds-([a-z0-9-]+)\)", x.strip())
        x = res(v[m.group(1)], depth + 1) if m and depth < 9 else x.strip()
        r = re.fullmatch(r"([\d.]+)rem", x)
        return f"{round(float(r.group(1)) * 16)}px" if r else x
    return {k: res(v[name]) for k, name in TOKENS.items()}


def main():
    out = {"made": dt.date.today().isoformat(), "engine": str(ENGINE.relative_to(ROOT)), "examples": []}
    for ex in EXAMPLES:
        with tempfile.TemporaryDirectory() as d:
            cmd = [sys.executable, str(ENGINE), "sketch", "--name", ex["name"], "--audience", ex["audience"], "--platforms", ex["platforms"],
                   "--feel", ex["feel"].replace(" ", ""), "--brand", ex["brand"], "--surfaces", ex["surfaces"]]
            subprocess.run(cmd, cwd=d, check=True, capture_output=True)
            build = subprocess.run([sys.executable, str(ENGINE), "build"], cwd=d, check=True, capture_output=True, text=True).stdout
            if "Passes" not in build:
                raise SystemExit(f"{ex['name']}: build did not pass\n{build}")
            t = light_values((pathlib.Path(d) / "opendesigner/build/css/tokens.css").read_text())
            meta = json.loads((pathlib.Path(d) / "opendesigner/tokens/opendesigner.meta.json").read_text())
        dials = {k: (x["value"] if isinstance(x, dict) else x) for k, x in meta["dials"].items()}
        t.update(ratio=meta["type"]["ratio"], dials=dials,
                 cPrimary=contrast(t["primary"], t["onPrimary"]), cText=contrast(t["text"], t["bg"]), cMuted=contrast(t["muted"], t["bg"]),
                 cBrandWhite=contrast(ex["brand"], "#ffffff"), brandKept=t["primary"].lower() == ex["brand"].lower())
        out["examples"].append({**{k: ex[k] for k in ("key", "name", "making", "who", "where", "feel", "brand")}, "command": " ".join(
            ["engine.py sketch", f'--name "{ex["name"]}"', f"--audience {ex['audience']}", f"--platforms {ex['platforms']}",
             f"--feel {ex['feel'].replace(' ', '')}", f"--brand \"{ex['brand']}\""]), "tokens": t})
    OUT.write_text(json.dumps(out, indent=1) + "\n")
    print(f"wrote {OUT.relative_to(ROOT)}: " + ", ".join(f"{e['name']} (radius {e['tokens']['rControl']}, controls {e['tokens']['hControl']})" for e in out["examples"]))


if __name__ == "__main__":
    main()
