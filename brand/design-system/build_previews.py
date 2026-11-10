#!/usr/bin/env python3
"""Write the design system's preview cards (project/components/*/preview.html) and a local tokens.css for testing.

  python3 brand/design-system/build_previews.py          write previews + _local/tokens.css
  python3 brand/design-system/build_previews.py --shots  also render every preview to _local/<Comp>.png

The previews are also the export templates: render.py-style exports read the same HTML.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
P = HERE / "project"
LOCAL = HERE / "_local"
T = json.loads((P / "tokens.json").read_text())
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@300..700&family=Source+Code+Pro:wght@400;500&display=block" rel="stylesheet">')


def svg(name):
    s = (P / "assets/Logos" / f"{name}.svg").read_text()
    return s.replace("<svg ", '<svg class="od-logo" ', 1)


def tokens_css():
    """Local stand-in for the page's generated tokens.css (format.md: 'tokens.css as compiled')."""
    themes = [t["id"] for t in T["color"]["themes"]]
    out = [f"/* {T['name']} — generated from tokens.json (local test copy) */"]
    for i, th in enumerate(themes):
        sel = f':root, [data-theme="{th}"]' if i == 0 else f'[data-theme="{th}"]'
        decl = [f"--{c['name']}: {c['value'][th] if isinstance(c['value'], dict) else c['value']};" for c in T["color"]["tokens"]]
        decl += [f"--{s['name']}: {s['value'][th]};" for s in T["shadow"]["tokens"]]
        out.append(sel + " { " + " ".join(decl) + " }")
    root = [f"--{t['name']}: {t['value']};" for fam in ("spacing", "radius") for t in T[fam]["tokens"]]
    root += [f"--font-{k}: {v};" for k, v in T["type"]["families"].items()]
    out.append(":root { " + " ".join(root) + " }")
    for g in T["type"]["groups"]:
        for s in g["styles"]:
            fam = s.get("family", g["family"])
            out.append(f".{s['name']} {{ font-family: var(--font-{fam}); font-size: {s['fontSize']}; line-height: {s['lineHeight']}; "
                       f"font-weight: {s['fontWeight']}; letter-spacing: {s['letterSpacing']}; }}")
    return "\n".join(out) + "\n"


def tiles(cols, rows, cell, gap, on=(), ink=(), ramp="x", quiet=False):
    """The mark's idea as a pattern: radius ramps from square to circle along x; `on` cells take the accent."""
    cells = []
    for r in range(rows):
        for c in range(cols):
            k = c / max(1, cols - 1) if ramp == "x" else (c + r) / max(1, cols + rows - 2)
            cls = "on" if (c, r) in on else "ink" if (c, r) in ink else ""
            cells.append(f'<i class="{cls}" style="border-radius:{round(k * 50)}%"></i>')
    return (f'<div class="od-tiles{" od-tiles--quiet" if quiet else ""}" style="grid-template-columns:repeat({cols},{cell}px);grid-auto-rows:{cell}px;gap:{gap}px">'
            + "".join(cells) + "</div>")


def page(marker, body, theme=None, w=None, h=None):
    size = f"width:{w}px;height:{h}px;" if w else ""
    attr = f' data-theme="{theme}"' if theme else ""
    return (f"{marker}\n<!doctype html>\n<html>\n<head><meta charset=\"utf-8\">{FONTS}<title>preview</title>\n"
            f"<style>html,body{{margin:0}} body{{background:transparent}}</style></head>\n<body>\n"
            f'<div id="root" class="od-post"{attr} style="{size}">{body}</div>\n</body>\n</html>\n')


CARDS = {}

# ---------- Cover (top-band skeleton: the name at 64px is wider than 440px by the 0.6em rule) ----------
CARDS["Cover"] = """<!-- @dsCard height=300 -->
<!doctype html>
<html>
<head><meta charset="utf-8">""" + FONTS + """<title>Cover</title>
<style>
html,body{margin:0;background:var(--surface)}
.cv{position:relative;width:960px;height:300px;background:var(--surface);font-family:var(--font-sans)}
.cv svg{position:absolute;left:0;top:0}
.b-accent{fill:var(--accent)} .b-ink{fill:var(--ink)} .b-soft{fill:var(--accent-soft)} .b-sunk{fill:var(--surface-sunken)} .b-line{fill:var(--line)} .b-on{fill:var(--on-accent)}
.name{position:absolute;left:48px;top:168px;margin:0;font-size:64px;line-height:60px;font-weight:300;letter-spacing:-0.03em;color:var(--ink)}
.tag{position:absolute;left:50px;top:244px;margin:0;font-size:14px;line-height:20px;color:var(--ink-muted);max-width:440px}
</style></head>
<body>
<div class="cv">
<!--
blocks: accent 384x120 (space-64 x6 by space-24 x5), ink 96x120, accent-soft 192x120, surface-sunken 240x120; radius 0 (a scale starts square)
arrangement: one strip of unequal bands across the top, flush, bleeding off the right edge
pattern: geometric, modular -> tiles cut by the radius tokens; the mark's square-to-circle ramp, 8 tiles of 48 (space-48) at gap 24 (space-24), radius 0..full, last one the decision
steps and radii: space-24, space-48, radius-detail, radius-control, radius-container, radius-overlay, radius-full
-->
<svg width="960" height="128" viewBox="0 0 960 128" aria-hidden="true">
  <rect class="b-accent" x="0" y="0" width="384" height="120"/>
  <rect class="b-ink" x="384" y="0" width="96" height="120"/>
  <rect class="b-soft" x="480" y="0" width="192" height="120"/>
  <rect class="b-sunk" x="672" y="0" width="288" height="120"/>
  <g>
    <rect class="b-on" x="24" y="36" width="48" height="48" rx="0"/>
    <rect class="b-on" x="96" y="36" width="48" height="48" rx="2"/>
    <rect class="b-on" x="168" y="36" width="48" height="48" rx="6"/>
    <rect class="b-on" x="240" y="36" width="48" height="48" rx="12"/>
    <rect class="b-on" x="312" y="36" width="48" height="48" rx="24"/>
    <rect class="b-line" x="504" y="36" width="48" height="48" rx="8"/>
    <rect class="b-line" x="576" y="36" width="48" height="48" rx="12"/>
    <rect class="b-accent" x="696" y="36" width="48" height="48" rx="24"/>
  </g>
</svg>
<p class="name">OpenDesigner</p>
<p class="tag">Design systems, one decision at a time. Free and open source.</p>
</div>
</body>
</html>
"""

# ---------- Headline: the three ways to highlight, loudest first ----------
hl_body = f"""
<div style="display:grid;gap:var(--space-32);padding:var(--space-48);width:1100px">
  <section style="display:grid;gap:var(--space-12)">
    <span class="caption od-muted">1 · Fill box · strongest pull · once per screen, nothing else cobalt</span>
    <h2 class="h1" style="line-height:76px">Design systems, <span class="od-hl">one decision</span> at a time.</h2>
  </section>
  <hr class="od-rule">
  <section style="display:grid;gap:var(--space-12)">
    <span class="caption od-muted">2 · Weight · medium pull · the default</span>
    <h2 class="h1">Design systems, <span class="od-strong">one decision</span> at a time.</h2>
  </section>
  <hr class="od-rule">
  <section style="display:grid;gap:var(--space-12)">
    <span class="caption od-muted">3 · Color · quietest · for running text</span>
    <p class="body-lg" style="max-width:640px">It asks five plain questions and turns <span class="od-accent">every answer into a file</span> your code and your AI can follow.</p>
  </section>
  <div data-theme="dark" style="background:var(--surface);color:var(--ink);padding:var(--space-32);border-radius:var(--radius-container);display:grid;gap:var(--space-12)">
    <span class="caption od-muted">Fill box on Dark · the box turns light, the phrase dark</span>
    <h2 class="h1" style="line-height:76px">Taste is a system. <span class="od-hl">Write it down.</span></h2>
  </div>
</div>"""
CARDS["Headline"] = page('<!-- @dsCard group="Type" height=760 width=1100 subtitle="Highlighting one phrase: box, weight or color" -->', hl_body)

# ---------- Button ----------
def btn_row(theme):
    return f"""<div data-theme="{theme}" style="background:var(--surface);color:var(--ink);padding:var(--space-24);display:flex;gap:var(--space-16);align-items:center;flex-wrap:wrap">
  <span class="caption od-muted" style="width:72px">{theme.title()}</span>
  <button class="od-btn od-btn--primary label">Create a design system</button>
  <button class="od-btn od-btn--secondary label">Read how it works</button>
  <button class="od-btn od-btn--text label">See an example</button>
  <button class="od-btn od-btn--primary label" style="outline:2px solid var(--focus-ring);outline-offset:2px">Focused</button>
  <button class="od-btn od-btn--secondary label" disabled>Disabled</button>
</div>"""
CARDS["Button"] = page('<!-- @dsCard group="Actions" height=300 width=1000 subtitle="Primary, secondary, text; one primary per screen" -->',
                       "<div style='display:grid;width:1000px'>" + btn_row("light") + btn_row("dark") + btn_row("cobalt") + "</div>")

# ---------- Social statement: 1600 x 900, Light, the fill box is the one loud thing ----------
st = f"""
<div style="position:absolute;left:80px;top:80px;height:44px">{svg('lockup-light-mono')}</div>
<span class="social-label od-muted" style="position:absolute;right:80px;top:82px">Open source</span>
<h1 class="social-statement" style="position:absolute;left:72px;top:220px;width:1400px;line-height:172px">Design systems,<br><span class="od-hl">one decision</span><br>at a time.</h1>
<p class="social-body od-muted" style="position:absolute;left:80px;bottom:72px">Free, and it works with the AI you already use.</p>
"""
CARDS["SocialStatement"] = page('<!-- @dsCard group="Marketing" height=900 width=1600 subtitle="X post 1600 x 900 · Light · fill box" -->', st, "light", 1600, 900)

# ---------- Social feature: 1600 x 900, Dark, weight highlight, one specimen ----------
qs = [("Who is it for?", "Home cooks"), ("Where does it run?", "Web and phone"), ("How should it feel?", "Warm, calm"), ("Brand color?", "Yours")]
rows = "".join(f"""<div style="display:flex;justify-content:space-between;align-items:center;padding:var(--space-24) 0;border-top:1px solid var(--line)">
  <span class="social-label" style="font-weight:400">{q}</span><span class="social-label od-muted">{a}</span></div>""" for q, a in qs)
ft = f"""
<div style="position:absolute;left:80px;top:80px;width:780px">
  <span class="social-label od-muted">Start small</span>
  <h2 class="social-headline" style="margin-top:var(--space-32)">Five questions.<br><span class="od-strong">A whole system.</span></h2>
  <p class="social-body od-muted" style="margin-top:var(--space-48)">Colors, type, spacing and motion that work together, in about three minutes.</p>
</div>
<div style="position:absolute;left:80px;bottom:80px;height:44px">{svg('lockup-dark-mono')}</div>
<div class="od-panel" style="position:absolute;right:80px;top:120px;width:620px;padding:var(--space-24) 40px var(--space-32)">
  <div style="display:flex;justify-content:space-between;padding-bottom:var(--space-16)"><span class="social-label od-muted">Sketch</span><span class="social-label od-muted">5 of 5</span></div>
  {rows}
  <div style="display:flex;gap:var(--space-16);align-items:center;padding-top:var(--space-24);border-top:1px solid var(--line)">
    <span style="width:40px;height:40px;border-radius:50%;background:var(--accent);color:var(--on-accent);display:grid;place-items:center;font-size:24px;font-weight:600">✓</span>
    <span class="social-label">Complete, and checked</span></div>
</div>
"""
CARDS["SocialFeature"] = page('<!-- @dsCard group="Marketing" height=900 width=1600 subtitle="X post 1600 x 900 · Dark · weight highlight + one specimen" -->', ft, "dark", 1600, 900)

# ---------- Carousel slide: 1080 x 1350, Cobalt ----------
on = {(5, 2)}
cs = f"""
<div style="position:absolute;left:64px;top:64px;height:40px">{svg('lockup-cobalt')}</div>
<span class="social-label od-muted" style="position:absolute;right:64px;top:64px">1 / 7</span>
<h2 class="social-headline" style="position:absolute;left:60px;top:200px;width:960px">Taste is a system.<br><span class="od-strong">Write it down.</span></h2>
<p class="social-body od-muted" style="position:absolute;left:64px;top:470px;width:880px">OpenDesigner turns your choices into files that your code and your AI follow.</p>
<div style="position:absolute;left:64px;bottom:64px">{tiles(6, 3, 120, 16, on=on)}</div>
"""
CARDS["CarouselSlide"] = page('<!-- @dsCard group="Marketing" height=1350 width=1080 subtitle="Threads / Instagram slide 1080 x 1350 · Cobalt" -->', cs, "cobalt", 1080, 1350)

# ---------- GitHub social preview: drawn at 1600 x 800, exported at 1280 x 640 (0.8) ----------
gh = f"""
<div style="position:absolute;left:80px;top:80px;height:48px">{svg('lockup-light-mono')}</div>
<h1 class="social-headline" style="position:absolute;left:76px;top:236px;width:880px">Design systems, <span class="od-strong">one decision</span> at a time.</h1>
<p class="social-body od-muted" style="position:absolute;left:80px;bottom:80px;width:860px">A free, open-source helper for the AI you already use.</p>
<div style="position:absolute;right:80px;top:80px">{tiles(5, 6, 88, 16, on={(4, 5)}, quiet=True)}</div>
"""
CARDS["GitHubPreview"] = page('<!-- @dsCard group="Marketing" height=800 width=1600 subtitle="GitHub social preview · drawn 1600 x 800, exported 1280 x 640" -->', gh, "light", 1600, 800)

READMES = {
    "Headline": "The one highlighted phrase in a headline, done one of three ways: a fill box (`highlight`, strongest), weight 650 (default) or `accent-text` (quietest). Use one method once per screen, and only after deciding where the eye should land first.\n\n- The consumer provides the headline text and which phrase to mark.\n- Fill box: keep the phrase on one line and the headline's line height at least 1.08, and nothing else on the screen in cobalt.\n- Never an italic serif word, never two methods together.\n",
    "Button": "Buttons in three emphases: primary (`accent` fill, `on-accent` label), secondary (`line-strong` border) and text (`accent-text`). One primary per screen.\n\n- Labels in `label`, sentence case, a verb first (\"Create a design system\").\n- At least 44 px tall; focus is a 2 px `focus-ring` with a 2 px gap.\n",
    "SocialStatement": "The statement post for X and LinkedIn, 1600 x 900 on Light. One `social-statement` headline of up to three lines with one fill-box phrase, one `social-body` line, the one-color lockup.\n\n- Provide: the headline, the phrase to box, one line of body.\n- Uses four styles at most: `social-statement`, `social-body`, `social-label` and the lockup.\n",
    "SocialFeature": "The feature post, 1600 x 900 on Dark: an overline, a `social-headline` with its second line in weight 650, a body line, and one specimen on `surface-raised`.\n\n- Provide: the overline, two headline lines, one body sentence and the specimen rows.\n- The only accent on the screen is the check in the specimen.\n",
    "CarouselSlide": "A 1080 x 1350 slide for Threads and Instagram on Cobalt: `social-headline`, a `social-body` line and the tile pattern, whose last tile (the decision) is the one white circle.\n\n- Use the Cobalt theme for one slide per carousel, usually the first or last.\n",
    "GitHubPreview": "The repository's social preview, drawn at 1600 x 800 and exported at 1280 x 640. Light theme, weight highlight, the tile pattern on the right with one cobalt circle.\n",
}


def main():
    for comp, html in CARDS.items():
        d = P / "components" / comp
        d.mkdir(parents=True, exist_ok=True)
        (d / "preview.html").write_text(html)
        if comp in READMES:
            (d / "README.md").write_text(f"# {comp}\n\n" + READMES[comp])
    LOCAL.mkdir(exist_ok=True)
    (LOCAL / "tokens.css").write_text(tokens_css())
    print("previews:", ", ".join(CARDS))
    if "--shots" in sys.argv:
        from playwright.sync_api import sync_playwright
        css = (LOCAL / "tokens.css").read_text() + (P / "components/bundle.css").read_text()
        with sync_playwright() as p:
            b = p.chromium.launch(channel="chrome")
            for comp in CARDS:
                html = (P / "components" / comp / "preview.html").read_text()
                m = re.search(r'width=(\d+)', html.splitlines()[0]); w = int(m.group(1)) if m else 960
                m = re.search(r'height=(\d+)', html.splitlines()[0]); h = int(m.group(1)) if m else 300
                html = html.replace("</head>", f"<style>{css}</style></head>").replace("<html>", '<html data-theme="light">', 1)
                pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
                pg.set_content(html, wait_until="networkidle")
                pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
                pg.screenshot(path=str(LOCAL / f"{comp}.png"), full_page=True)
                pg.close()
            b.close()
        print("shots in", LOCAL)


if __name__ == "__main__":
    main()
