#!/usr/bin/env python3
"""A contact sheet of library components: each one at the three views the site shows (phone 390, tablet 768, desktop 1280 px),
in four looks (Nordic, the default; Billerwick dense; Fernhollow large; Playful with pill controls), unscaled, for reviewing them by eye.

  python3 site/library_sheet.py <slug> [<slug> ...] --out <folder>

Writes <folder>/<slug>.jpg (a small JPEG, about 0.5 scale) per component. Needs Playwright and Chrome. Writes nothing to the repo.
"""
import argparse
import pathlib
import re
import sys

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
LIB = ROOT / "skills/opendesigner/assets/library/components"
VIEWS = [("Phone", 390), ("Tablet", 768), ("Desktop", 1280)]
LOOKS = ["nordic", "billerwick", "fernhollow", "playful"]  # playful: pill controls, which show any box wrongly given a control radius
REFS = r'(id|for|aria-controls|aria-labelledby|aria-describedby|aria-activedescendant|name)="([^"]+)"'


def page(src, css):
    markup = re.sub(r"<style>.*?</style>|<script>.*?</script>", "", src, flags=re.S)
    style = "".join(re.findall(r"<style>(.*?)</style>", src, re.S))
    script = "".join(re.findall(r"<script>(.*?)</script>", src, re.S))
    cells = ""
    for k in LOOKS:
        for name, w in VIEWS:
            m = re.sub(REFS, lambda x, s=f"{k}-{w}": f'{x.group(1)}="{x.group(2)}-{s}"', markup)
            cells += (f'<figure><figcaption>{k} · {name} {w}</figcaption><div class="view odl-sys-{k}" style="width:{w}px">{m}</div></figure>')
    return (f'<!doctype html><meta charset="utf-8"><style>{css}\n{style}\nbody{{margin:0;padding:24px;background:#e9edf3;font:13px system-ui}}'
            f'main{{display:grid;grid-template-columns:390px 768px 1280px;gap:24px;align-items:start}}figure{{margin:0}}figcaption{{margin:0 0 6px;color:#444}}'
            f'.view{{box-sizing:border-box;padding:12px;background:var(--ds-color-surface-base);color:var(--ds-color-text-primary);font:var(--ds-text-body-md);display:grid}}'
            f'.view>*{{margin-inline:auto}}</style><main>{cells}</main><script>{script}</script>')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slugs", nargs="+")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    out = pathlib.Path(a.out); out.mkdir(parents=True, exist_ok=True)
    css = (ROOT / "site/static/library-systems.css").read_text()
    with sync_playwright() as p:
        b = p.chromium.launch(channel="chrome")
        pg = b.new_page(viewport={"width": 2560, "height": 900}, device_scale_factor=0.5)
        for s in a.slugs:
            f = out / f"{s}.html"
            f.write_text(page((LIB / s / "component.html").read_text(), css))
            pg.goto(f.as_uri())
            # wait for every photo (Unsplash, hotlinked) to load or fail, up to 15 s, so a sheet never shows empty boxes
            pg.evaluate("""() => Promise.race([Promise.all([...document.images].map(i => { i.loading = "eager"; return i.complete ? 0 :
                new Promise(r => { i.onload = i.onerror = r; }); })), new Promise(r => setTimeout(r, 15000))])""")
            pg.wait_for_timeout(400)
            pg.screenshot(path=str(out / f"{s}.jpg"), type="jpeg", quality=60, full_page=True)
            f.unlink()
            print(out / f"{s}.jpg")
        b.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
