#!/usr/bin/env python3
"""Build OpenDesigner's website into site/dist/: a documentation directory with a landing page (static HTML, light only).

  python3 site/build.py           build
  python3 site/build.py --og      also re-render the Open Graph images (Playwright + Chrome)

Sources: the brand tokens (brand/design-system/project/tokens.json), the docs (site/docs/*.md, with front matter:
title, seo_title, description, section, order, updated), the landing page below, and the live repository facts
(GitHub API at build time). The same sources make the HTML pages, their Markdown copies, llms.txt, llms-full.txt,
sitemap.xml and the structured data. Fonts (SIL OFL) are fetched once into site/.cache and self-hosted. Photos are
free Unsplash photos, hotlinked from images.unsplash.com as Unsplash asks, with the photographers credited.
"""
import datetime as dt
import html
import json
import os
import pathlib
import re
import shutil
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
DIST = SITE / "dist"
CACHE = SITE / ".cache"
DOCS = SITE / "docs"
BRAND = ROOT / "brand"
REPO = "ckryptickunal/OpenDesigner"
GH = f"https://github.com/{REPO}"
_url_file = SITE / "site-url.txt"
SITE_URL = os.environ.get("SITE_URL") or (_url_file.read_text().strip() if _url_file.exists() else "https://opendesigner.vercel.app")
SITE_URL = SITE_URL.rstrip("/")
TODAY = dt.date.today().isoformat()
T = json.loads((BRAND / "design-system/project/tokens.json").read_text())
NAME = "OpenDesigner"
ONE_LINER = ("OpenDesigner is a free, open-source set of skills and a small engine for the AI you already use. It asks the decisions "
             "a design system needs, suggests a sourced default for each, checks accessibility, and writes design tokens, CSS, "
             "a Tailwind theme and a DESIGN.md that your team and your AI build from.")
HERO_LEDE = ("It asks the decisions a design system needs, one at a time, and suggests a sourced default for each. It checks contrast "
             "and writes design tokens, CSS, a Tailwind theme and a DESIGN.md that your team and your coding agents build from. Free and open source.")
SECTIONS = ["Getting started", "Guides", "Concepts", "Reference"]
REDIRECTS = {"/install/": "/docs/install/", "/how-it-works/": "/docs/how-it-works/", "/faq/": "/docs/faq/",
             "/what-is-a-design-system/": "/docs/design-systems/"}
esc = html.escape

# Free Unsplash photos (licence checked: not Unsplash+), shown in cobalt duotone.
PHOTOS = {
    "sketchbook": ("photo-1600132806608-231446b2e7af", "Compagnons", "4UGmm3WRUoQ", "A hand-drawn website wireframe in a sketchbook, an orange pen beside it"),
    "glasswall": ("photo-1603975711481-18b7aaca4caa", "NEW DATA SERVICES", "0tSiofevpUs", "Hand-drawn screen wireframes and sticky notes on an office glass wall"),
    "whiteboard": ("photo-1532622785990-d2c36a76f5a6", "Kaleidico", "26MJGnCM0Wc", "Two people sketching a page layout on a whiteboard"),
    "swatches": ("photo-1749207325171-ae2294e277ed", "Declan Sun", "XsJQc5r33Ik", "Rows of paint color swatches on a shelf"),
}


# ---------------------------------------------------------------- repository facts, fonts, tokens
def repo_facts():
    try:
        req = urllib.request.Request(f"https://api.github.com/repos/{REPO}", headers={"User-Agent": "opendesigner-site"})
        with urllib.request.urlopen(req, timeout=10) as r:
            j = json.load(r)
        return {"stars": j["stargazers_count"], "forks": j["forks_count"], "issues": j["open_issues_count"], "pushed": j["pushed_at"][:10]}
    except Exception:
        return {"stars": None, "forks": None, "issues": None, "pushed": TODAY}


FONT_SPECS = [("hanken", "Hanken+Grotesk:wght@300..700", "https://raw.githubusercontent.com/google/fonts/main/ofl/hankengrotesk/OFL.txt"),
              ("sourcecodepro", "Source+Code+Pro:wght@400;500", "https://raw.githubusercontent.com/google/fonts/main/ofl/sourcecodepro/OFL.txt")]
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"


def fetch(url, binary=False):
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=20) as r:
        data = r.read()
    return data if binary else data.decode("utf-8")


def fonts():
    CACHE.mkdir(exist_ok=True)
    rules = []
    for key, fam, lic in FONT_SPECS:
        css_path = CACHE / f"{key}.css"
        if not css_path.exists():
            css_path.write_text(fetch(f"https://fonts.googleapis.com/css2?family={fam}&display=swap"))
        for block in re.findall(r"/\* latin \*/\s*(@font-face\s*{[^}]*})", css_path.read_text()):
            url = re.search(r"url\((https://[^)]+\.woff2)\)", block).group(1)
            weight = re.search(r"font-weight:\s*([^;]+);", block).group(1).strip()
            family = re.search(r"font-family:\s*'([^']+)'", block).group(1)
            fname = f"{key}-{weight.replace(' ', '-')}.woff2"
            if not (CACHE / fname).exists():
                (CACHE / fname).write_bytes(fetch(url, binary=True))
            rules.append((family, weight, fname))
        if not (CACHE / f"{key}-OFL.txt").exists():
            (CACHE / f"{key}-OFL.txt").write_text(fetch(lic))
    return rules


def tokens_css():
    light = "\n".join(f"  --{c['name']}: {c['value']['light']};" for c in T["color"]["tokens"])
    light += "\n" + "\n".join(f"  --{s['name']}: {s['value']['light']};" for s in T["shadow"]["tokens"])
    cobalt = "\n".join(f"  --{c['name']}: {c['value']['cobalt']};" for c in T["color"]["tokens"])
    root = "\n".join(f"  --{t['name']}: {t['value']};" for fam in ("spacing", "radius") for t in T[fam]["tokens"])
    return f":root {{\n{light}\n{root}\n  color-scheme: light;\n}}\n.theme-cobalt {{\n{cobalt}\n}}\n"


# ---------------------------------------------------------------- Markdown (headings, lists, code, links, bold)
def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", re.sub(r"<[^>]+>", "", s).lower()).strip("-")


def inline(s):
    s = esc(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', s)
    return s


def md_to_html(md, toc=None):
    out, lines, i = [], md.strip().splitlines(), 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("```"):
            j, code = i + 1, []
            while j < len(lines) and not lines[j].startswith("```"):
                code.append(lines[j]); j += 1
            out.append(f'<div class="code"><pre><code>{esc(chr(10).join(code), quote=False)}</code></pre>'
                       f'<button class="copy" type="button" data-copy>Copy</button></div>')
            i = j + 1
            continue
        if ln.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|$", lines[i + 1].strip()):
            cells = lambda r: [c.strip() for c in r.strip().strip("|").split("|")]
            head, j, body = cells(ln), i + 2, []
            while j < len(lines) and lines[j].startswith("|"):
                body.append(cells(lines[j])); j += 1
            out.append('<div class="table-wrap"><table><thead><tr>' + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>"
                       + "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body) + "</tbody></table></div>")
            i = j
            continue
        m = re.match(r"^(#{2,3}) (.*)", ln)
        if m:
            lvl, text = len(m.group(1)), m.group(2)
            sid = slugify(text)
            if toc is not None and lvl == 2:
                toc.append((sid, re.sub(r"[`*]", "", text)))
            out.append(f'<h{lvl} id="{sid}">{inline(text)}</h{lvl}>')
        elif ln.startswith("> "):
            quote = []
            while i < len(lines) and lines[i].startswith("> "):
                quote.append(lines[i][2:]); i += 1
            out.append(f"<blockquote><p>{inline(' '.join(quote))}</p></blockquote>")
            continue
        elif re.match(r"^(\d+\.|-) ", ln):
            ordered, items = ln[0].isdigit(), []
            while i < len(lines) and (re.match(r"^(\d+\.|-) ", lines[i]) or (lines[i].startswith("  ") and items)):
                if lines[i].startswith("  ") and items:
                    items[-1] += " " + lines[i].strip()
                else:
                    items.append(re.sub(r"^(\d+\.|-) ", "", lines[i]))
                i += 1
            tag = "ol" if ordered else "ul"
            out.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in items) + f"</{tag}>")
            continue
        elif ln.strip():
            para = [ln]
            while i + 1 < len(lines) and lines[i + 1].strip() and not re.match(r"^(#|```|> |\d+\. |- |\|)", lines[i + 1]):
                i += 1; para.append(lines[i])
            out.append(f"<p>{inline(' '.join(para))}</p>")
        i += 1
    return "\n".join(out)


def plain(s):
    return re.sub(r"[`*]", "", re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)).strip()


def load_docs():
    pages = []
    for f in sorted(DOCS.glob("*.md")):
        raw = f.read_text()
        fm, body = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S).groups()
        meta = dict(re.findall(r"^(\w+): (.*)$", fm, re.M))
        slug = f.stem
        meta.update(slug=slug, body=body.strip(), path="/docs/" if slug == "index" else f"/docs/{slug}/",
                    order=float(meta.get("order", 99)), section=meta.get("section", "Reference"))
        pages.append(meta)
    pages.sort(key=lambda p: (SECTIONS.index(p["section"]) if p["section"] in SECTIONS else 9, p["order"]))
    return pages


# ---------------------------------------------------------------- shared parts
GH_ICON = ('<svg aria-hidden="true" viewBox="0 0 16 16" width="16" height="16"><path fill="currentColor" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 '
           '0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07'
           '-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 '
           '2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>')
CHEVRON = '<svg aria-hidden="true" viewBox="0 0 16 16" width="16" height="16"><path d="M6 3l5 5-5 5" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>'
STATE = {"stars": ""}
CUR, EAGER, LAZY = ' aria-current="page"', ' fetchpriority="high"', ' loading="lazy"'


def lockup():
    s = (BRAND / "design-system/project/assets/Logos/lockup-light.svg").read_text()
    return s.replace("<svg ", '<svg class="lockup" aria-hidden="true" focusable="false" ', 1)


def photo(key, w=1600, h=None, cls="duo", sizes="100vw", eager=False):
    pid, author, page_id, alt = PHOTOS[key]
    base = f"https://images.unsplash.com/{pid}?auto=format&fit=crop&q=70"
    hh = h or round(w * 0.42)
    src = lambda ww: f"{base}&w={ww}&h={round(ww * hh / w)}"
    return (f'<figure class="{cls} duo-{key}"><div class="duo-frame"><img src="{src(w)}" srcset="{src(w // 2)} {w // 2}w, {src(w)} {w}w, {src(round(w * 1.5))} {round(w * 1.5)}w" '
            f'sizes="{sizes}" width="{w}" height="{hh}" alt="{esc(alt)}"{EAGER if eager else LAZY}></div>'
            f'<figcaption>Photo: <a href="https://unsplash.com/photos/{page_id}">{esc(author)}</a> on Unsplash</figcaption></figure>')


def jsonld(*objs):
    return "".join(f'<script type="application/ld+json">{json.dumps(o, ensure_ascii=False, separators=(",", ":"))}</script>' for o in objs)


def crumbs_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE_URL + u} for i, (n, u) in enumerate(items)]}


def sidebar(pages, current):
    groups = []
    for sec in SECTIONS:
        items = [p for p in pages if p["section"] == sec]
        if not items:
            continue
        lis = "".join(f'<li><a href="{p["path"]}"{CUR if p["path"] == current else ""}>{esc(p["title"])}</a></li>' for p in items)
        groups.append(f'<div class="side-group"><h2 class="side-h">{sec}</h2><ul>{lis}</ul></div>')
    show = f'<div class="side-group"><h2 class="side-h">Examples</h2><ul><li><a href="/showcase/"{CUR if current == "/showcase/" else ""}>Showcase</a></li></ul></div>'
    return (f'<aside class="side" aria-label="Documentation"><details class="side-mobile"><summary>Documentation menu</summary>'
            f'<nav>{"".join(groups)}{show}</nav></details><nav class="side-desk">{"".join(groups)}{show}</nav></aside>')


def shell(path, seo_title, description, main_html, pages, ld=(), og="/og/home.png", md=True, wide=False, robots="index, follow, max-image-preview:large"):
    canon = SITE_URL + path
    md_link = f'<link rel="alternate" type="text/markdown" href="{path}index.md" title="Markdown">' if md else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(seo_title)}</title>
<meta name="description" content="{esc(description)}">
{"" if robots.startswith("noindex") else f'<link rel="canonical" href="{canon}">'}
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#fcfdff">
<meta name="color-scheme" content="light only">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{esc(seo_title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE_URL}{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(seo_title)}">
<meta name="twitter:description" content="{esc(description)}">
<meta name="twitter:image" content="{SITE_URL}{og}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/fonts/hanken-300-700.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preconnect" href="https://images.unsplash.com">
<link rel="stylesheet" href="/site.css">
{md_link}
<link rel="sitemap" type="application/xml" href="/sitemap.xml">
{jsonld(*ld)}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="bar"><div class="bar-in">
<a class="brand" href="/" aria-label="{NAME} home">{lockup()}</a>
<nav class="top-nav" aria-label="Main"><a href="/docs/"{CUR if path.startswith("/docs/") else ""}>Docs</a><a href="/docs/install/">Install</a><a href="/showcase/"{CUR if path == "/showcase/" else ""}>Showcase</a></nav>
<a class="gh-btn" href="{GH}">{GH_ICON}<span>GitHub</span><span class="gh-count" data-stars>{STATE["stars"]}</span></a>
</div></header>
<div class="layout{" wide" if wide else ""}">
{sidebar(pages, path)}
<main id="main" class="main">
{main_html}
</main>
</div>
{footer(pages)}
<script src="/site.js" defer></script>
</body>
</html>
"""


def footer(pages):
    by = {s: [p for p in pages if p["section"] == s][:6] for s in SECTIONS}
    cols = "".join(f'<div><h2 class="foot-h">{s}</h2><ul>' + "".join(f'<li><a href="{p["path"]}">{esc(p["title"])}</a></li>' for p in ps) + "</ul></div>"
                   for s, ps in by.items() if ps)
    proj = (f'<div><h2 class="foot-h">Project</h2><ul><li><a href="{GH}">GitHub</a></li><li><a href="{GH}/issues/new/choose">Report a problem</a></li>'
            f'<li><a href="/showcase/">Showcase</a></li><li><a href="/llms.txt">llms.txt</a></li><li><a href="/sitemap.xml">Sitemap</a></li></ul></div>')
    return (f'<footer class="foot"><div class="foot-in"><div class="foot-brand">{lockup()}<p>Free and open source. MIT for code, '
            f'CC BY 4.0 for docs.</p></div>{cols}{proj}</div><p class="foot-legal">OpenDesigner is an independent open-source project. Claude, '
            f'ChatGPT, Codex, Cursor, Figma and other names belong to their owners and appear only to say where OpenDesigner runs. Photos: Unsplash '
            f'photographers, credited where shown. Updated {TODAY}.</p></footer>')


# ---------------------------------------------------------------- landing page
def landing(pages, facts, faq):
    stages = [("Start", "Answer up to five questions in your AI tool, or point it at the app or brand you already have. You get a working draft of color, type, spacing, corners, depth and motion, each with its reason."),
              ("Use", "Import the tokens, the CSS variables or the Tailwind theme. Coding agents read DESIGN.md before they touch the interface, so new screens follow the same rules."),
              ("Keep", "Changes go through a decision log that records who set what and why. A review command finds colors, sizes and radii in the code that drifted from the tokens.")]
    roles = [("Product designers", "whiteboard", "/docs/designers/",
              ["Get scales, states and contrast checks done in minutes, and keep the direction yourself.",
               "Every choice has a reason you can show in a design review.",
               "Export Figma variables so the design file and the code use the same names."]),
             ("Design-system teams", "glasswall", "/docs/enterprise/",
              ["A decision log with reasons and who set each value. Lock what must not drift.",
               "House and project standards apply automatically; the extend skill reads decisions before any change.",
               "DTCG 2025.10 tokens fit existing token pipelines. It's new: no team pilots yet."]),
             ("Engineers", "swatches", "/docs/engineers/",
              ["CSS variables, a Tailwind v4 theme, Swift and Compose files from one source.",
               "DESIGN.md and an AGENTS.md note keep coding agents on the system.",
               "`engine.py review` names the token to use instead of a hard-coded value."])]
    rows = "".join(f'<li><a href="{p["path"]}"><span class="row-t">{esc(p["title"])}</span><span class="row-s">{p["section"]}</span>{CHEVRON}</a></li>' for p in pages)
    n = lambda v: "—" if v is None else f"{v:,}"
    faq_html = "".join(f'<details class="qa"><summary><h3>{esc(q)}</h3></summary><div class="ans">{md_to_html(a)}</div></details>' for q, a in faq[:5])
    body = f"""
<section class="hero">
<p class="pill"><span>Open source · MIT</span><a href="/docs/decisions/">New: your whole system on one page {CHEVRON}</a></p>
<h1 class="t-hero">Build a design system <strong>with the AI you already use</strong>, and keep it consistent.</h1>
<p class="lede">{HERO_LEDE}</p>
<div class="cta-row">
<a class="btn primary" href="/docs/install/">Install</a>
<a class="btn secondary" href="/docs/">Read the docs</a>
<button class="btn ghost copy" type="button" data-copy-text="/plugin marketplace add ckryptickunal/OpenDesigner
/plugin install opendesigner@opendesigner">Copy the Claude Code install</button>
</div>
<p class="works">Packaged for Claude Code, the Claude app, ChatGPT, Codex, Cursor and other tools that read Agent Skills.</p>
{photo("sketchbook", 1600, 640, "duo hero-photo", "(max-width: 1100px) 100vw, 900px", eager=True)}
</section>

<section class="block" id="process">
<h2 class="t-h2">Where it fits in your process</h2>
<ol class="stages">{"".join(f'<li><span class="num">0{i + 1}</span><h3>{t}</h3><p>{inline(d)}</p></li>' for i, (t, d) in enumerate(stages))}</ol>
</section>

<section class="block" id="roles">
<h2 class="t-h2">What it changes for you</h2>
<div class="roles">{"".join(f'<article class="role">{photo(k, 600, 340, "duo role-photo", "(max-width: 900px) 100vw, 300px")}<h3>{t}</h3><ul>' + "".join(f"<li>{inline(x)}</li>" for x in xs) + f'</ul><a class="more" href="{u}">Guide for {t.lower()} {CHEVRON}</a></article>' for t, k, u, xs in roles)}</div>
</section>

<section class="block" id="output">
<div class="split">
<div><h2 class="t-h2">What you have after the first run</h2>
<p class="lede">Files in your project, readable by people and AI tools. Nothing lives on a server, and the same answers always give the same files.</p>
<ul class="tree">{"".join(f'<li><code>{f}</code><span>{w}</span></li>' for f, w in [("DESIGN.md", "your rules in plain words"), ("opendesigner/tokens/", "DTCG 2025.10"), ("build/css/tokens.css", "CSS variables"), ("build/tailwind/theme.css", "Tailwind v4"), ("build/figma/", "Figma variables"), ("overview.html", "the system on one page"), ("decisions.md", "every choice and why")])}</ul></div>
<figure class="shot"><div class="frame"><span></span><span></span><span></span></div><picture><source type="image/webp" srcset="/img/overview-1440.webp 1440w, /img/overview-720.webp 720w" sizes="(max-width: 1100px) 100vw, 560px"><img src="/img/overview-1440.jpg" width="1440" height="900" loading="lazy" alt="The overview page generated for OpenDesigner's own brand, with each area marked Chosen, Default or Not enough information."></picture>
<figcaption>A real overview page: what you chose, what is still a default, and what only you can give, like a logo.</figcaption></figure>
</div>
</section>

<section class="block" id="docs">
<div class="block-head"><h2 class="t-h2">Browse the docs</h2><a class="more" href="/docs/">All docs {CHEVRON}</a></div>
<ul class="rows">{rows}</ul>
</section>

<section class="block" id="status">
<div class="split">
<div><h2 class="t-h2">Where it stands</h2>
<ul class="status">
<li>The repository was created on 2026-09-23. It is early, and one person maintains it.</li>
<li>The engine's tests pass, and three worked examples are in the repository.</li>
<li>No watched user trials have happened yet, and a recorded run in every AI tool is still on the list.</li>
<li>In a stress test, AI agents built 46 designs through the process, plus 8 mockups. <a href="/showcase/">See them</a>, with the findings.</li>
</ul></div>
<article class="ghcard"><div class="gh-top">{GH_ICON}<a href="{GH}"><strong>{REPO}</strong></a></div>
<dl class="gh-stats"><div><dt>Stars</dt><dd data-stars>{n(facts["stars"])}</dd></div><div><dt>Forks</dt><dd data-forks>{n(facts["forks"])}</dd></div><div><dt>Open issues</dt><dd data-issues>{n(facts["issues"])}</dd></div><div><dt>Last push</dt><dd data-pushed>{facts["pushed"]}</dd></div></dl>
<div class="gh-actions"><a class="btn secondary" href="{GH}">{GH_ICON} Star on GitHub</a><a class="btn text" href="{GH}/issues/new/choose">Report a problem</a></div>
<p class="note">Live from GitHub. Tell us where it breaks: that is the most useful thing right now.</p></article>
</div>
</section>

<section class="block" id="faq">
<div class="block-head"><h2 class="t-h2">Questions</h2><a class="more" href="/docs/faq/">All questions {CHEVRON}</a></div>
<div class="faq">{faq_html}</div>
</section>
"""
    ld = [{"@context": "https://schema.org", "@type": "SoftwareApplication", "name": NAME, "url": SITE_URL + "/", "description": ONE_LINER,
           "applicationCategory": "DeveloperApplication", "applicationSubCategory": "Design system generator", "operatingSystem": "macOS, Windows, Linux",
           "isAccessibleForFree": True, "license": f"{GH}/blob/main/LICENSE", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
           "image": f"{SITE_URL}/og/home.png", "downloadUrl": GH, "softwareHelp": f"{SITE_URL}/docs/", "sameAs": [GH],
           "author": {"@type": "Person", "name": "ckryptickunal", "url": "https://github.com/ckryptickunal"}},
          {"@context": "https://schema.org", "@type": "SoftwareSourceCode", "name": NAME, "codeRepository": GH, "programmingLanguage": ["Python", "Markdown"],
           "license": "https://opensource.org/license/mit", "dateModified": facts["pushed"]},
          {"@context": "https://schema.org", "@type": "WebSite", "name": NAME, "url": SITE_URL + "/", "description": ONE_LINER, "inLanguage": "en"}]
    return shell("/", "OpenDesigner: build a design system with your AI",
                 "Free, open-source skills and engine that build a design system with the AI you already use: tokens, CSS, Tailwind and a DESIGN.md.",
                 body, pages, ld, wide=True)


# ---------------------------------------------------------------- docs pages, docs index, showcase, 404
def faq_items(body):
    return [(q.strip(), a.strip()) for q, a in re.findall(r"^### (.+?)\n(.+?)(?=\n### |\Z)", body, re.S | re.M)]


def doc_page(p, pages):
    toc = []
    if p["slug"] == "faq":
        items = faq_items(p["body"])
        intro = p["body"].split("\n### ", 1)[0] if not p["body"].startswith("### ") else ""
        content = md_to_html(intro) + "".join(
            f'<details class="qa" id="{slugify(q)}"><summary><h2>{esc(q)}</h2></summary><div class="ans">{md_to_html(a)}</div></details>' for q, a in items)
    else:
        content = md_to_html(p["body"], toc)
    idx = pages.index(p)
    prev_, next_ = (pages[idx - 1] if idx > 0 else None), (pages[idx + 1] if idx + 1 < len(pages) else None)
    pn = ('<nav class="prevnext" aria-label="Previous and next">'
          + (f'<a class="prev" href="{prev_["path"]}"><span>Previous</span>{esc(prev_["title"])}</a>' if prev_ else "<span></span>")
          + (f'<a class="next" href="{next_["path"]}"><span>Next</span>{esc(next_["title"])}</a>' if next_ else "") + "</nav>")
    toc_html = ('<nav class="toc" aria-label="On this page"><h2 class="side-h">On this page</h2><ul>' + "".join(f'<li><a href="#{a}">{esc(t)}</a></li>' for a, t in toc) + "</ul></nav>") if len(toc) > 1 else ""
    crumb = (f'<nav class="crumb" aria-label="Breadcrumb"><a href="/docs/">Docs</a><span aria-hidden="true">/</span><span>{p["section"]}</span>'
             + (f'<span aria-hidden="true">/</span><span aria-current="page">{esc(p["title"])}</span>' if p["slug"] != "index" else "") + "</nav>")
    edit = f'{GH}/blob/main/site/docs/{p["slug"]}.md'
    main_html = (f'<div class="doc-grid"><article class="doc">{crumb}<h1 class="t-h1">{esc(p["title"])}</h1>'
                 f'<p class="meta">Updated <time datetime="{p.get("updated", TODAY)}">{p.get("updated", TODAY)}</time> · <a href="{edit}">Edit on GitHub</a></p>'
                 f'<div class="prose">{content}</div>{pn}</article>{toc_html}</div>')
    ld = [crumbs_ld([("Docs", "/docs/")] + ([] if p["slug"] == "index" else [(p["title"], p["path"])])),
          {"@context": "https://schema.org", "@type": "Article" if p["slug"] == "design-systems" else "TechArticle", "headline": p["title"],
           "description": p["description"], "url": SITE_URL + p["path"], "datePublished": "2026-10-14", "dateModified": p.get("updated", TODAY),
           "inLanguage": "en", "image": f"{SITE_URL}/og/home.png", "mainEntityOfPage": SITE_URL + p["path"],
           "author": {"@type": "Person", "name": "ckryptickunal", "url": "https://github.com/ckryptickunal"},
           "publisher": {"@type": "Organization", "name": NAME, "url": SITE_URL + "/", "logo": {"@type": "ImageObject", "url": f"{SITE_URL}/apple-touch-icon.png"}}}]
    if p["slug"] == "faq":
        ld.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in faq_items(p["body"])]})
    if p["slug"] == "install":
        ld.append({"@context": "https://schema.org", "@type": "HowTo", "name": "Install OpenDesigner in Claude Code", "step": [
            {"@type": "HowToStep", "text": "/plugin marketplace add ckryptickunal/OpenDesigner"},
            {"@type": "HowToStep", "text": "/plugin install opendesigner@opendesigner"},
            {"@type": "HowToStep", "text": "Say: Create a design system for this project."}]})
    og = "/og/guide.png" if p["slug"] == "design-systems" else ("/og/faq.png" if p["slug"] == "faq" else "/og/home.png")
    return shell(p["path"], p["seo_title"], p["description"], main_html, pages, ld, og=og)


SHOW_INTRO = ("In a stress test on 2026-10-14, eight AI builder agents made 46 designs through the whole OpenDesigner process: real references, "
              "a design system from the engine for each piece, the build, then checks. Another agent placed some of them in 8 mockups. Every brand is invented. About a third came out competent but "
              "conventional, and much of the most striking work was shaped by hand on top of the tokens.")
MOCKUP_CAPTIONS = {
    "01-phone-trio": "Three evening apps (sleep, podcast, banking) in generic phones over a lilac field.",
    "02-laptop-desk": "The Swiss architecture hero on a laptop, on a real desk photo with matched perspective.",
    "03-watch-trio": "Three watch faces on generic cases, lit like a product shot.",
    "04-browser-cascade": "Five website heroes as stacked browser windows, each from its own system.",
    "05-components-board": "Five web components at their real size on one board.",
    "06-poster-street": "The music-festival hero on a roadside board at golden hour.",
    "07-tablet-clinic": "A hospital ward's vitals screen on a tablet.",
    "08-made-with-opendesigner": "A launch post in OpenDesigner's own brand system over the work.",
}
THUMB_W = 900


def piece_text(d):
    title, text = d.name.split("-", 1)[1].replace("-", " ").capitalize(), ""
    notes = d / "notes.md"
    if notes.exists():
        lines = notes.read_text().splitlines()
        title = next((ln[2:].strip() for ln in lines if ln.startswith("# ")), title)
        body = [ln.strip() for ln in lines if ln.strip() and not ln.startswith(("#", "|", "-", ">", "!", "```"))
                and not re.search(r"(shot\.png|index\.html|^Render|^Page|^Status|^Built by|scale 2)", ln.strip(), re.I)]
        if d.name in MOCKUP_CAPTIONS:
            body = [MOCKUP_CAPTIONS[d.name]]
        if body:
            text = re.sub(r"^(Direction|Brief|Concept)[.:]\s*", "", re.sub(r"[*_`]", "", body[0]))
            text = text if len(text) < 170 else text[:167].rsplit(" ", 1)[0] + "…"
    return title, text


def showcase(pages):
    from PIL import Image
    cats = [("mockups", "Mockups"), ("heroes", "Hero sections"), ("components", "Web components"), ("app-screens", "App screens"),
            ("watch", "Watch screens"), ("footers", "Footer sections")]
    blocks, items, md = [], [], ["# Showcase", "", SHOW_INTRO, ""]
    for cat, label in cats:
        cards = []
        md += [f"## {label}", ""]
        for d in sorted((BRAND / "showcase" / cat).glob("*/")):
            thumb = BRAND / "showcase" / "_thumbs" / f"{cat}--{d.name}--shot.jpg"
            if not thumb.exists():
                continue
            title, blurb = piece_text(d)
            key = f"{cat}--{d.name}"
            with Image.open(thumb) as im:
                h = round(im.height * THUMB_W / im.width)
            cards.append(f'<figure class="piece"><img src="/img/show/{key}.webp" width="{THUMB_W}" height="{h}" loading="lazy" alt="{esc(title)}">'
                         f'<figcaption><strong>{esc(title)}</strong><span>{esc(blurb)}</span></figcaption></figure>')
            items.append({"@type": "ImageObject", "name": title, "contentUrl": f"{SITE_URL}/img/show/{key}.webp", "description": blurb})
            md.append(f"- **{title}**: {blurb}")
        md.append("")
        blocks.append(f'<section class="block" id="{cat}"><h2 class="t-h3">{label}</h2><div class="pieces {cat}">{"".join(cards)}</div></section>')
    head = (f'<div class="page-head"><nav class="crumb" aria-label="Breadcrumb"><a href="/">{NAME}</a><span aria-hidden="true">/</span><span aria-current="page">Showcase</span></nav>'
            f'<h1 class="t-h1">46 designs and 8 mockups, one process</h1><p class="lede">{esc(SHOW_INTRO)} <a href="{GH}/blob/main/brand/showcase/STRESS-TEST.md">Read the findings</a>.</p></div>')
    ld = [crumbs_ld([("Showcase", "/showcase/")]), {"@context": "https://schema.org", "@type": "CollectionPage", "name": "OpenDesigner showcase",
                                                    "url": f"{SITE_URL}/showcase/", "description": SHOW_INTRO, "hasPart": items[:60]}]
    html_ = shell("/showcase/", "OpenDesigner showcase: 46 designs and 8 mockups",
                  "Heroes, components, app and watch screens, footers and mockups that AI agents built through OpenDesigner, each from its own design system.",
                  head + "".join(blocks), pages, ld, og="/og/showcase.png", wide=True)
    return html_, "\n".join(md)


def not_found(pages):
    body = (f'<div class="page-head"><h1 class="t-h1">Not enough information</h1><p class="lede">This page doesn\'t exist. Like a logo nobody has '
            f'made yet, it shows as missing instead of being faked.</p><p><a class="btn primary" href="/docs/">Go to the docs</a></p></div>')
    return shell("/404.html", "Page not found · OpenDesigner", "This page doesn't exist.", body, pages, md=False, robots="noindex")


# ---------------------------------------------------------------- images, OG, machine files, hosting config
def images():
    from PIL import Image
    (DIST / "img" / "show").mkdir(parents=True, exist_ok=True)
    ov = BRAND / "kit" / "_work" / "overview-top.png"
    if ov.exists():
        im = Image.open(ov).convert("RGB").crop((0, 0, 1440, 900))
        im.save(DIST / "img/overview-1440.webp", "WEBP", quality=82)
        im.save(DIST / "img/overview-1440.jpg", "JPEG", quality=82, optimize=True, progressive=True)
        im.resize((720, 450), Image.LANCZOS).save(DIST / "img/overview-720.webp", "WEBP", quality=82)
    for t in (BRAND / "showcase" / "_thumbs").glob("*--shot.jpg"):
        im = Image.open(t).convert("RGB")
        im = im.resize((THUMB_W, round(im.height * THUMB_W / im.width)), Image.LANCZOS) if im.width > THUMB_W else im
        im.save(DIST / "img/show" / f"{t.name.replace('--shot.jpg', '')}.webp", "WEBP", quality=80)
    mark = BRAND / "kit" / "logo" / "avatar-light-800.png"
    if mark.exists():
        im = Image.open(mark).convert("RGB")
        for size, name in ((180, "apple-touch-icon.png"), (32, "favicon-32.png"), (192, "icon-192.png"), (512, "icon-512.png")):
            im.resize((size, size), Image.LANCZOS).save(DIST / name)
    fav = (BRAND / "design-system/project/assets/Logos/mark-light.svg").read_text().replace('viewBox="0 0 100 100"', 'viewBox="-12 -12 124 124"')
    (DIST / "favicon.svg").write_text(fav)


def og_images():
    sys.path.insert(0, str(BRAND / "design-system"))
    import export_kit as K
    from playwright.sync_api import sync_playwright
    out = CACHE / "og"
    out.mkdir(parents=True, exist_ok=True)
    cards = {"home.png": K.statement("light", 'Build a design system<br><span class="od-strong">with the AI you already use.</span>', "Free and open source.", "opendesigner", 1200, 630, "social-subhead"),
             "faq.png": K.statement("light", 'Questions, <span class="od-strong">plain answers.</span>', "OpenDesigner docs", "FAQ", 1200, 630, "social-subhead"),
             "guide.png": K.statement("light", 'What is a <span class="od-strong">design system?</span>', "A plain guide, with AI.", "Guide", 1200, 630, "social-subhead"),
             "showcase.png": K.statement("cobalt", '46 designs. <span class="od-strong">One process.</span>', "Built by AI agents through OpenDesigner. Every brand is invented.", "Showcase", 1200, 630, "social-subhead")}
    with sync_playwright() as p:
        b = p.chromium.launch(channel="chrome")
        pg = b.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=1)
        for name, html_ in cards.items():
            pg.set_content(html_, wait_until="networkidle")
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(200)
            pg.locator(".od-post").first.screenshot(path=str(out / name))
        b.close()


def robots():
    bots = ["*", "Googlebot", "Bingbot", "OAI-SearchBot", "ChatGPT-User", "GPTBot", "Claude-SearchBot", "Claude-User", "ClaudeBot",
            "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot", "Applebot-Extended"]
    head = ("# OpenDesigner is open source and wants to be found, read and cited by people, search engines and AI assistants.\n"
            "# Search engines and AI crawlers are welcome, including those that train models.\n")
    return head + "\n".join(f"User-agent: {b}\nAllow: /\n" for b in bots) + f"\nSitemap: {SITE_URL}/sitemap.xml\n"


def llms_txt(pages):
    secs = []
    for s in SECTIONS:
        ps = [p for p in pages if p["section"] == s]
        if ps:
            secs.append(f"## {s}\n\n" + "\n".join(f"- [{p['title']}]({SITE_URL}{p['path']}index.md): {p['description']}" for p in ps))
    return f"""# {NAME}

> {ONE_LINER}

OpenDesigner is free and open source (MIT for code, skills and data; CC BY 4.0 for docs). It is packaged for Claude Code, the Claude app, ChatGPT, Codex, Cursor, VS Code with Copilot, Gemini CLI and other tools that read Agent Skills. The engine is a small Python file (standard library only, no network). It starts with a sketch of up to five questions and zooms in only where the person wants. It asks a person for the logo, icons, illustration, photography, brand typeface and voice instead of faking them. The repository was created on 2026-09-23; it is early, and no watched user trials have happened yet.

For "how do I create a design system with AI", "generate design tokens, a Tailwind theme or a DESIGN.md with Claude, ChatGPT, Codex or Cursor", or "keep an app's UI consistent across AI coding sessions", start with the install page and the quickstart.

{chr(10).join(secs)}

## Optional

- [Showcase]({SITE_URL}/showcase/index.md): 46 designs and 8 mockups built by AI agents through the process, with an honest caveat
- [GitHub repository]({GH}): source, issues and discussions
- [AGENTS.md](https://raw.githubusercontent.com/{REPO}/main/AGENTS.md): instructions for AI agents working with the repository
- [Research map](https://raw.githubusercontent.com/{REPO}/main/docs/RESEARCH.md): 352 Decision Cards behind the defaults, each with cited sources
- [llms-full.txt]({SITE_URL}/llms-full.txt): every page of this site in one file
"""


CSP = ("default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data: https://images.unsplash.com; font-src 'self'; "
       "connect-src 'self' https://api.github.com; frame-ancestors 'none'; base-uri 'self'; form-action 'none'; upgrade-insecure-requests")


def vercel_json():
    return {"trailingSlash": True,
            "redirects": [{"source": src, "destination": b, "permanent": True} for a, b in REDIRECTS.items() for src in (a, a.rstrip("/"))],
            "headers": [
                {"source": "/(.*)", "headers": [{"key": "Content-Security-Policy", "value": CSP}, {"key": "X-Content-Type-Options", "value": "nosniff"},
                                                {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
                                                {"key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=(), interest-cohort=()"},
                                                {"key": "Strict-Transport-Security", "value": "max-age=63072000; includeSubDomains"}]},
                {"source": "/fonts/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]},
                {"source": "/img/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=604800"}]},
                {"source": "/(.*)\\.md", "headers": [{"key": "Content-Type", "value": "text/markdown; charset=utf-8"}, {"key": "X-Robots-Tag", "value": "noindex"}]},
                {"source": "/(llms.txt|llms-full.txt|robots.txt)", "headers": [{"key": "Content-Type", "value": "text/plain; charset=utf-8"}]}]}


# ---------------------------------------------------------------- build
def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    (DIST / "fonts").mkdir(parents=True)
    facts = repo_facts()
    STATE["stars"] = "" if facts["stars"] is None else f"{facts['stars']:,}"
    rules = fonts()
    for _fam, _w, fname in rules:
        shutil.copy(CACHE / fname, DIST / "fonts" / fname)
    for key, _f, _l in FONT_SPECS:
        shutil.copy(CACHE / f"{key}-OFL.txt", DIST / "fonts" / f"{key}-OFL.txt")
    ff = "".join(f"@font-face{{font-family:'{fam}';font-style:normal;font-weight:{w};font-display:swap;src:url(/fonts/{f}) format('woff2')}}\n" for fam, w, f in rules)
    (DIST / "site.css").write_text(ff + tokens_css() + (SITE / "static" / "site.css").read_text())
    shutil.copy(SITE / "static" / "site.js", DIST / "site.js")
    images()
    if "--og" in sys.argv or not (CACHE / "og" / "home.png").exists():
        try:
            og_images()
        except Exception as e:
            print("OG images not rendered:", e)
    if (CACHE / "og").exists():
        shutil.copytree(CACHE / "og", DIST / "og", dirs_exist_ok=True)

    pages = load_docs()
    faq_page = next((p for p in pages if p["slug"] == "faq"), None)
    faq = faq_items(faq_page["body"]) if faq_page else []
    files = {"index.html": landing(pages, facts, faq)}
    mds = {"index.md": f"# {NAME}\n\n{ONE_LINER}\n\nDocs: {SITE_URL}/docs/\nInstall: {SITE_URL}/docs/install/\nSource: {GH}\n"}
    for p in pages:
        rel = p["path"].lstrip("/")
        files[rel + "index.html"] = doc_page(p, pages)
        mds[rel + "index.md"] = f"# {p['title']}\n\n{p['body']}\n"
    sh_html, sh_md = showcase(pages)
    files["showcase/index.html"] = sh_html
    mds["showcase/index.md"] = sh_md + "\n"
    files["404.html"] = not_found(pages)
    for rel, text in {**files, **mds}.items():
        f = DIST / rel
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(text)
    paths = ["/"] + [p["path"] for p in pages] + ["/showcase/"]
    (DIST / "robots.txt").write_text(robots())
    (DIST / "llms.txt").write_text(llms_txt(pages))
    (DIST / "llms-full.txt").write_text(f"# {NAME} (full text of {SITE_URL})\n\n" + "\n\n---\n\n".join(mds.values()))
    (DIST / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
                                      + "".join(f"<url><loc>{SITE_URL}{u}</loc><lastmod>{TODAY}</lastmod></url>" for u in paths) + "</urlset>\n")
    (DIST / "site.webmanifest").write_text(json.dumps({"name": NAME, "short_name": NAME, "start_url": "/", "display": "standalone",
                                                       "background_color": "#fcfdff", "theme_color": "#2338ff",
                                                       "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"},
                                                                 {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=1))
    (DIST / "vercel.json").write_text(json.dumps(vercel_json(), indent=1))
    key_file = SITE / "indexnow-key.txt"
    if key_file.exists():
        key = key_file.read_text().strip()
        (DIST / f"{key}.txt").write_text(key)
    print(f"built {DIST} for {SITE_URL}: {len(files)} pages ({len(pages)} docs), stars={facts['stars']}")


if __name__ == "__main__":
    main()
