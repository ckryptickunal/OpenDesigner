#!/usr/bin/env python3
"""Render OpenDesigner's marketing images from the brand system (tokens.json + components/bundle.css).

  python3 brand/design-system/export_kit.py [out_dir]      default: brand/kit/

Every image is built from the same tokens, type styles and parts as the artifact's preview cards (build_previews.py),
so the kit can't drift from the system. Needs Playwright with Chrome; fonts come from Google Fonts at render time.
"""
import pathlib
import sys

from PIL import Image
from playwright.sync_api import sync_playwright

import build_previews as B

HERE = B.HERE
ROOT = HERE.parent.parent
SHOW = ROOT / "brand" / "showcase"
OUT = pathlib.Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / "brand" / "kit"
CSS = B.tokens_css() + (B.P / "components" / "bundle.css").read_text()


def doc(body, theme, w, h):
    return (f'<!doctype html><html data-theme="light"><head><meta charset="utf-8">{B.FONTS}<style>{CSS}'
            f'html,body{{margin:0}}</style></head><body><div class="od-post" data-theme="{theme}" style="width:{w}px;height:{h}px">'
            f'{body}</div></body></html>')


def img(path, style=""):
    return f'<img src="{pathlib.Path(path).resolve().as_uri()}" style="display:block;{style}" alt="">'


def logo(theme):
    return B.svg({"light": "lockup-light-mono", "dark": "lockup-dark-mono", "cobalt": "lockup-cobalt"}[theme])


# ---------- specimens (inside an od-panel) ----------
def spec_rows(rows, check=None):
    out = "".join(f'<div style="display:flex;justify-content:space-between;gap:24px;padding:var(--space-24) 0;border-top:1px solid var(--line)">'
                  f'<span class="social-label" style="font-weight:400">{a}</span><span class="social-label od-muted">{b}</span></div>' for a, b in rows)
    if check:
        out += (f'<div style="display:flex;gap:var(--space-16);align-items:center;padding-top:var(--space-24);border-top:1px solid var(--line)">'
                f'<span style="width:40px;height:40px;border-radius:50%;background:var(--accent);color:var(--on-accent);display:grid;place-items:center;'
                f'font-size:24px;font-weight:600">&#10003;</span><span class="social-label">{check}</span></div>')
    return out


def panel(head_l, head_r, inner, width=620):
    return (f'<div class="od-panel" style="width:{width}px;padding:var(--space-24) 40px var(--space-32)">'
            f'<div style="display:flex;justify-content:space-between;padding-bottom:var(--space-16)"><span class="social-label od-muted">{head_l}</span>'
            f'<span class="social-label od-muted">{head_r}</span></div>{inner}</div>')


QUESTIONS = panel("Sketch", "5 of 5", spec_rows([("Who is it for?", "Home cooks"), ("Where does it run?", "Web and phone"),
                                                  ("How should it feel?", "Warm, calm"), ("Brand color?", "Yours")], "Complete, and checked"))
FLOORS = panel("Accessibility floors", "locked", spec_rows([("Text contrast", "4.5 : 1"), ("Target size", "24 px +"),
                                                             ("Keyboard focus", "always visible"), ("Motion", "respects reduce")]))
TREE = panel("your-project/", "written by your AI", "".join(
    f'<div style="display:flex;justify-content:space-between;gap:24px;padding:14px 0;border-top:1px solid var(--line);padding-left:{d * 36}px">'
    f'<span class="code" style="font-size:30px;line-height:40px">{n}</span><span class="social-label od-muted">{w}</span></div>'
    for n, d, w in [("opendesigner/", 0, ""), ("tokens/", 1, "DTCG"), ("build/", 1, "CSS, Tailwind, native"), ("overview.html", 1, "your system"),
                    ("decisions.md", 1, "every why"), ("DESIGN.md", 0, "for your AI")]))


# ---------- layouts ----------
def statement(theme, headline, body, label="Open source", w=1600, h=900, size="social-statement", tiles=False):
    m = 80 if w > h else 64
    if w <= h:  # portrait: headline, then the body right under it, the tiles along the bottom
        t = f'<div style="position:absolute;left:{m}px;bottom:{m}px">{B.tiles(6, 3, 136, 16, on={(5, 2)})}</div>' if tiles else ""
        return doc(f'<div style="position:absolute;left:{m}px;top:{m}px;height:40px">{logo(theme)}</div>'
                   f'<span class="social-label od-muted" style="position:absolute;right:{m}px;top:{m}px">{label}</span>'
                   f'<div style="position:absolute;left:{m - 4}px;top:200px;width:{w - 2 * m}px"><h1 class="{size}">{headline}</h1>'
                   f'<p class="social-body od-muted" style="margin-top:var(--space-48)">{body}</p></div>{t}', theme, w, h)
    t = f'<div style="position:absolute;right:80px;bottom:80px">{B.tiles(6, 3, 96, 16, on={(5, 2)})}</div>' if tiles else ""
    return doc(f'<div style="position:absolute;left:80px;top:80px;height:44px">{logo(theme)}</div>'
               f'<span class="social-label od-muted" style="position:absolute;right:80px;top:82px">{label}</span>'
               f'<h1 class="{size}" style="position:absolute;left:72px;top:220px;width:{w - 160}px">{headline}</h1>'
               f'<p class="social-body od-muted" style="position:absolute;left:80px;bottom:72px;width:{w - 160 - (720 if tiles else 0)}px">{body}</p>{t}',
               theme, w, h)


def feature(theme, over, head, body, spec, w=1600, h=900):
    if w > h:
        return doc(f'<div style="position:absolute;left:80px;top:80px;width:780px"><span class="social-label od-muted">{over}</span>'
                   f'<h2 class="social-headline" style="margin-top:var(--space-32)">{head}</h2>'
                   f'<p class="social-body od-muted" style="margin-top:var(--space-48)">{body}</p></div>'
                   f'<div style="position:absolute;left:80px;bottom:80px;height:44px">{logo(theme)}</div>'
                   f'<div style="position:absolute;right:80px;top:120px">{spec}</div>', theme, w, h)
    return doc(f'<div style="position:absolute;left:64px;top:64px;height:40px">{logo(theme)}</div>'
               f'<div style="position:absolute;left:64px;top:160px;width:{w - 128}px"><span class="social-label od-muted">{over}</span>'
               f'<h2 class="social-headline" style="margin-top:var(--space-24)">{head}</h2>'
               f'<p class="social-body od-muted" style="margin-top:var(--space-32)">{body}</p></div>'
               f'<div style="position:absolute;left:64px;bottom:64px">{spec}</div>', theme, w, h)


def mosaic(theme, over, head, body, shots, cols, w=1600, h=900, cell_w=None, aspect=0.625):
    gap = 16
    cell_w = cell_w or (w - 160 - gap * (cols - 1)) // cols
    rows = (len(shots) + cols - 1) // cols
    h = max(h, 260 + rows * int(cell_w * aspect) + (rows - 1) * gap + (120 if body else 80))
    grid = "".join(f'<div style="border-radius:var(--radius-container);overflow:hidden;box-shadow:var(--shadow-raised);height:{int(cell_w * aspect)}px">'
                   f'{img(s, "width:100%;height:100%;object-fit:cover;object-position:top")}</div>' for s in shots)
    return doc(f'<div style="position:absolute;left:80px;top:72px;right:80px;display:flex;justify-content:space-between;align-items:flex-end">'
               f'<div><span class="social-label od-muted">{over}</span><h2 class="social-subhead" style="margin-top:12px">{head}</h2></div>'
               f'<div style="height:40px">{logo(theme)}</div></div>'
               f'<div style="position:absolute;left:80px;right:80px;top:260px;display:grid;grid-template-columns:repeat({cols},1fr);gap:{gap}px">{grid}</div>'
               + (f'<p class="social-label od-muted" style="position:absolute;left:80px;bottom:56px">{body}</p>' if body else ""), theme, w, h)


def framed(theme, over, head, body, shot, w=1600, h=900):
    return doc(f'<div style="position:absolute;left:80px;top:80px;height:44px">{logo(theme)}</div>'
               f'<div style="position:absolute;left:80px;top:200px;width:600px"><span class="social-label od-muted">{over}</span>'
               f'<h2 class="social-headline" style="margin-top:var(--space-24)">{head}</h2>'
               f'<p class="social-body od-muted" style="margin-top:var(--space-32)">{body}</p></div>'
               f'<div class="od-panel" style="position:absolute;left:760px;top:96px;width:960px;height:900px;overflow:hidden;padding:0">'
               f'<div style="display:flex;gap:10px;padding:16px 20px;border-bottom:1px solid var(--line)">'
               + '<i style="width:14px;height:14px;border-radius:50%;background:var(--line)"></i>' * 3
               + f'</div>{img(shot, "width:960px")}</div>', theme, w, h)


def header(w=1500, h=500):
    return doc(f'<div style="position:absolute;left:470px;top:170px;width:760px"><h2 class="social-subhead">Design systems,<br>'
               f'<span class="od-strong">one decision</span> at a time.</h2></div>'
               f'<div style="position:absolute;right:64px;top:146px">{B.tiles(3, 3, 64, 12, on={(2, 2)}, quiet=True)}</div>', "light", w, h)


def avatar(theme, size=800):
    mark = B.svg({"light": "mark-light", "dark": "mark-dark", "cobalt": "mark-cobalt"}[theme])
    return doc(f'<div style="position:absolute;inset:0;display:grid;place-items:center"><div style="width:{int(size * .46)}px;height:{int(size * .46)}px">{mark}</div></div>',
               theme, size, size)


def shots(cat, names=None):
    out = sorted((SHOW / cat).glob("*/shot.png"))
    return [p for p in out if not names or any(n in p.parent.name for n in names)]


def overview_shot(page):
    """The brand's own overview.html, top of the page, with the real face loaded."""
    src = (ROOT / "brand" / "opendesigner" / "overview.html").resolve()
    page.set_viewport_size({"width": 1440, "height": 1400})
    page.goto(src.as_uri(), wait_until="networkidle")
    page.add_style_tag(url="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@300..700&display=block")
    page.evaluate("document.fonts.ready")
    page.wait_for_timeout(800)
    page.evaluate("var n=document.getElementById('ov-font'); if(n) n.hidden=true")
    out = OUT / "_work" / "overview-top.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    page.screenshot(path=str(out), clip={"x": 0, "y": 0, "width": 1440, "height": 1400})
    return out


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(channel="chrome")
        pg = b.new_page(device_scale_factor=1)
        ov = overview_shot(pg)
        heroes = shots("heroes")
        apps = shots("app-screens", ["01-", "04-", "05-", "08-"])
        mixed = [heroes[0], heroes[6], heroes[7], heroes[8], *shots("components", ["08-", "10-"]), *shots("footers", ["01-", "05-"])]
        A = {
            "x/01-statement.png": statement("light", 'Design systems,<br><span class="od-hl">one decision</span><br>at a time.',
                                            "Free, and it works with the AI you already use."),
            "x/02-five-questions.png": feature("dark", "Start small", 'Five questions.<br><span class="od-strong">A whole system.</span>',
                                               "Colors, type, spacing and motion that work together, from up to five plain questions.", QUESTIONS),
            "x/03-showcase.png": mosaic("dark", "Built by AI agents through OpenDesigner", '46 designs. <span class="od-strong">46 directions.</span>',
                                        "Each one started from real references and its own system from the engine. Every brand is invented.",
                                        mixed, 4),
            "x/04-overview.png": framed("light", "New", 'Your system, <span class="od-strong">gaps marked.</span>',
                                        "What you chose, what is a default, and what only you can give.", ov),
            "x/05-accessible.png": feature("light", "Built in", 'Accessible <span class="od-strong">by default.</span>',
                                           "Contrast, target size, focus and reduced motion are floors, not settings.", FLOORS),
            "x/06-files.png": feature("dark", "Yours to keep", 'Everything lands <span class="od-strong">in files.</span>',
                                      "Tokens, CSS, a Tailwind theme and a DESIGN.md that your code and your AI follow.", TREE),
            "x/07-taste.png": statement("cobalt", 'Taste is a system.<br><span class="od-strong">Write it down.</span>',
                                        "OpenDesigner turns your choices into files.", "Free · MIT", size="social-headline", tiles=True),
            "x/08-heroes.png": mosaic("light", "Same process, ten products", 'Ten heroes. <span class="od-strong">No two alike.</span>', "",
                                      heroes, 5),
            "x/header-1500x500.png": header(),
            "carousel/01-cover.png": statement("cobalt", 'Design systems,<br><span class="od-strong">one decision</span><br>at a time.',
                                               "How OpenDesigner works.", "1 / 6", 1080, 1350, "social-headline", tiles=True),
            "carousel/02-questions.png": feature("dark", "Start small", 'Five questions.<br><span class="od-strong">A whole system.</span>',
                                                 "Up to five plain questions.", QUESTIONS.replace("width:620px", "width:952px"), 1080, 1350),
            "carousel/03-files.png": feature("light", "Yours to keep", 'Everything lands <span class="od-strong">in files.</span>',
                                             "Your code and your AI follow them.", TREE.replace("width:620px", "width:952px"), 1080, 1350),
            "carousel/04-accessible.png": feature("dark", "Built in", 'Accessible <span class="od-strong">by default.</span>',
                                                  "Floors, not settings.", FLOORS.replace("width:620px", "width:952px"), 1080, 1350),
            "carousel/05-showcase.png": mosaic("light", "Built by AI agents with it", '<span class="od-strong">46 designs.</span>', "Every brand is invented.",
                                               [heroes[0], heroes[6], heroes[7], heroes[8], heroes[3], heroes[1]], 2, 1080, 1350),
            "carousel/06-try.png": statement("cobalt", 'Free. Open source.<br><span class="od-strong">Say one sentence.</span>',
                                             "“Create a design system for this project.” Link in the first reply.", "6 / 6", 1080, 1350, "social-headline", tiles=True),
            "github/social-preview-1600x800.png": B.CARDS["GitHubPreview"].replace("</head>", f"<style>{CSS}</style></head>"),
            "reddit/01-showcase-grid.png": mosaic("light", "Built by AI agents through OpenDesigner", "46 pieces, one process", "Heroes, components and footers. Every brand is invented.",
                                                  [*heroes[:4], *shots("components")[:4], *shots("footers")[:4]], 4, 1600, 900),
            "reddit/02-app-screens.png": mosaic("dark", "Ten app screens", "Different products, one process", "", shots("app-screens", ["01-", "02-", "03-", "04-", "05-", "06-", "07-", "08-"]), 4, 1600, 900, aspect=2.164),
            "reddit/03-watch.png": mosaic("dark", "Eight watch screens", "Built from each app's own system", "", shots("watch"), 4, 1600, 900, aspect=1.224),
            "logo/avatar-cobalt-800.png": avatar("cobalt"),
            "logo/avatar-light-800.png": avatar("light"),
        }
        for rel, html in A.items():
            out = OUT / rel
            out.parent.mkdir(parents=True, exist_ok=True)
            pg.set_content(html, wait_until="networkidle")
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(250)
            el = pg.locator("#root, .od-post").first
            el.screenshot(path=str(out))
            print(rel)
        b.close()
    gh = OUT / "github" / "social-preview-1600x800.png"
    Image.open(gh).resize((1280, 640), Image.LANCZOS).save(OUT / "github" / "social-preview-1280x640.png")
    for name in ("lockup-light", "lockup-dark", "lockup-cobalt", "mark-light", "mark-dark", "mark-cobalt"):
        (OUT / "logo" / f"{name}.svg").write_text((B.P / "assets" / "Logos" / f"{name}.svg").read_text())


if __name__ == "__main__":
    main()
