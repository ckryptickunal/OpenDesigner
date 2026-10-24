#!/usr/bin/env python3
"""Build OpenDesigner's website into site/dist/: the landing page (/), the documentation directory (/docs/) and the showcase (static HTML, light only).

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
import subprocess
import sys
import urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import library_page  # noqa: E402  (the component library page, /library/)

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
DIST = pathlib.Path(os.environ.get("SITE_DIST") or SITE / "dist")  # SITE_DIST: build elsewhere while someone else builds here
CACHE = SITE / ".cache"
DOCS = SITE / "docs"
BRAND = ROOT / "brand"
REPO = "ckryptickunal/OpenDesigner"
GH = f"https://github.com/{REPO}"
_url_file = SITE / "site-url.txt"
SITE_URL = os.environ.get("SITE_URL") or (_url_file.read_text().strip() if _url_file.exists() else "https://opendesigner.dev")
SITE_URL = SITE_URL.rstrip("/")
TODAY = dt.date.today().isoformat()
T = json.loads((BRAND / "design-system/project/tokens.json").read_text())
NAME = "OpenDesigner"
ONE_LINER = ("OpenDesigner is a free, open-source set of skills and a small engine for the AI you already use. It asks the decisions "
             "a design system needs, suggests a sourced default for each, checks accessibility, and writes design tokens, CSS, "
             "a Tailwind theme and a DESIGN.md that your team and your AI build from.")
TEAM_CHECKS = [("A decision log", "with the reason and who set each value, append-only."),
               ("Locked values", "that the skills refuse to change without the owner's consent."),
               ("House and project standards", "applied on every build, each with its reason."),
               ("A drift check", "that names the token to use instead of a hard-coded value."),
               ("DTCG 2025.10 tokens", "with a resolver for light and dark, density and motion."),
               ("Runs locally,", "with no account and no server: your repository's access control applies.")]
STARTS = [("Getting started", "Install", "Two commands in Claude Code, or a skills folder in other tools.", "/docs/install/"),
          ("Getting started", "Your first design system", "Five questions, the files you get, and what to look at first.", "/docs/quickstart/"),
          ("Guides", "For design-system teams", "Decision log, locks, standards, drift checks and a pilot plan.", "/docs/enterprise/"),
          ("Reference", "How it works", "From your answers to tokens, exports and checks.", "/docs/how-it-works/")]
HERO_LEDE = ("It asks the decisions a design system needs, one at a time, and suggests a sourced default for each. It checks contrast "
             "and writes design tokens, CSS, a Tailwind theme and a DESIGN.md that your team and your coding agents build from. Free and open source.")
FIGURES = SITE / "figures"
FIG_RE = re.compile(r"^\{\{figure:([a-z0-9-]+)\}\}$")
EVALS_RE = re.compile(r"^\{\{evals:([a-z-]+)\}\}$")  # live eval results (site/evals_html.py)
# Photo scenes for figures: free Unsplash photos (licence checked 2026-10-14, abstract, no logos). A figure asks for one with data-scene="name".
SCENES = {
    "blue-gradient": ("photo-1760865245520-21b0786f5236", "Philipp Hubert", "dVVjhUcdb30"),
    "blue-waves": ("photo-1618853606840-d2138cef5431", "Marcel Strauß", "h7Lh0f74A6Y"),
    "sky-trees": ("photo-1532935702929-2a7df164ddea", "Photoholgic", "HVQnG6JxxY0"),
    "forest": ("photo-1786797773538-9fb650c5c7c7", "Harshal Tandel", "BrzWSKWCuWo"),
    "blue-soft": ("photo-1645811791231-279658fb46dc", "Sean Fahrenbruch", "kxL6jPPNEWc"),
    "woods-sage": ("photo-1737279722244-4b5f5b896c6b", "Annie Spratt", "5yKrcO8FKwM"),
    "blue-stripes": ("photo-1608488576473-c4ff7000870c", "Eduardo Drapier", "7Ae5sfgyfc0"),
    "blue-pattern": ("photo-1749497268209-c167ed52b682", "Maxim Berg", "XTGTa3Ry6H4"),
}
SECTIONS = ["Getting started", "Guides", "Concepts", "Craft", "Reference"]
REDIRECTS = {"/install/": "/docs/install/", "/how-it-works/": "/docs/how-it-works/", "/faq/": "/docs/faq/",
             "/what-is-a-design-system/": "/docs/design-systems/", "/docs/changelog/": "/changelog/"}
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
    except Exception:  # the anonymous API is rate-limited per address; the signed-in gh CLI is not, when it is there
        try:
            import subprocess
            j = json.loads(subprocess.run(["gh", "api", f"repos/{REPO}"], capture_output=True, text=True, timeout=20, check=True).stdout)
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


_SF = json.loads((ROOT / "synthesis" / "levers.json").read_text())["formulas"]["type"]["tracking"]["sfPro"]  # Apple HIG, S-L02-001
SF_PRO, SF_TEXT_UNTIL = _SF["table"], _SF["textUntil"]
_CORNER = json.loads((ROOT / "synthesis" / "levers.json").read_text())["formulas"]["radius"]["continuous"]  # tools/fit_corner.py


def corners_match_levers(css):
    """site.css draws Apple's continuous corner with the numbers in levers formulas.radius.continuous; stop the build if they drift."""
    shapes = set(re.findall(r"corner-shape: (superellipse\([\d.]+\)|squircle)", css)) | set(re.findall(r"@supports \(corner-shape: ([^)]+\)?)\)", css))
    scales = set(re.findall(r"--corner-k: ([\d.]+);", css)) - {"1"}
    want_shape, want_scale = f"superellipse({_CORNER['superellipse']:g})", f"{_CORNER['radiusScale']:g}"
    if shapes - {want_shape} or scales - {want_scale}:
        raise SystemExit(f"site CSS corners {sorted(shapes)} at {sorted(scales)} differ from levers: {want_shape} at {want_scale}")
    return css


def sf_tracking(px):
    """Apple's SF Pro tracking for a text size, in em, straight-line between the HIG table's rows (the engine's sf_pro_tracking)."""
    if px <= SF_PRO[0][0]:
        return SF_PRO[0][1] / 1000
    for (s0, t0), (s1, t1) in zip(SF_PRO, SF_PRO[1:]):
        if px <= s1:
            return round((t0 + (t1 - t0) * (px - s0) / (s1 - s0)) / 1000, 4)
    return SF_PRO[-1][1] / 1000


def minify_css(css):
    """site.css without comments or extra whitespace (about 8 KB less to download before the first paint). Quoted strings
    are kept as they are; spaces inside values (calc, media queries such as "and (") become one space, never none; an
    empty custom property keeps its space."""
    parts = re.split(r'("(?:[^"\\\n]|\\.)*"|\'(?:[^\'\\\n]|\\.)*\')', css)
    for k in range(0, len(parts), 2):
        t = re.sub(r"/\*.*?\*/", "", parts[k], flags=re.S)
        t = re.sub(r"\s+", " ", t)
        parts[k] = re.sub(r"\s*([{};,>])\s*", r"\1", t).replace(":;", ": ;")
    return "".join(parts).strip() + "\n"


def apple_tracking(css):
    """Give every rule that sets a text size up to 19px Apple's tracking for that size (owner, 2026-10-14: "iOS kerning everywhere").
    letter-spacing in em is turned into pixels where it is declared and inherited as pixels, so a 12px note inside 16px text
    would keep the parent's spacing: each rule that sets its own size needs its own value. A rule that already sets
    letter-spacing keeps it (the owner's headline, code, uppercase labels), and so does monospace, uppercase or a size that is
    not one number (clamp, em, var)."""
    rule = re.compile(r"([^{}]+)\{([^{}]*)\}")
    parts = lambda sel: {x.strip() for x in re.sub(r"/\*.*?\*/", "", sel, flags=re.S).split(",") if x.strip()}
    own = set()  # selectors that set letter-spacing somewhere, so a later rule that only resizes them keeps it
    for m in rule.finditer(css):
        if "letter-spacing" in m.group(2):
            own |= parts(m.group(1))

    def fix(m):
        sel, body = m.group(1), m.group(2)
        if "letter-spacing" in body or "@" in sel or parts(sel) & own or re.search(r"monospace|Source Code|uppercase", body):
            return m.group(0)
        size = re.search(r"(?:^|;)\s*font-size:\s*([\d.]+)(px|rem)\s*(?:;|$)", body) or \
            re.search(r"(?:^|;)\s*font:\s*(?:[a-z-]+\s+)*?(?:\d{3}\s+)?([\d.]+)(px|rem)\b", body)
        if not size:
            return m.group(0)
        px = float(size.group(1)) * (16 if size.group(2) == "rem" else 1)
        if px > SF_TEXT_UNTIL:  # headings are set by eye in site.css (see the iOS block there)
            return m.group(0)
        return f"{sel}{{{body.rstrip().rstrip(';')}; letter-spacing: {fmt_em(sf_tracking(px))}; }}"
    return rule.sub(fix, css)


def apple_tracking_inline(html_):
    """The same rule for a figure's inline styles: style="font-size:13px" with no letter-spacing gets Apple's value for 13px."""
    def fix(m):
        style = m.group(1)
        size = re.search(r"(?:^|;)\s*font-size:\s*([\d.]+)px", style) or re.search(r"(?:^|;)\s*font:\s*(?:[a-z-]+\s+)*?(?:\d{3}\s+)?([\d.]+)px", style)
        if not size or "letter-spacing" in style or re.search(r"monospace|Source Code|uppercase", style) or float(size.group(1)) > SF_TEXT_UNTIL:
            return m.group(0)
        return f'style="{style.rstrip().rstrip(";")};letter-spacing:{fmt_em(sf_tracking(float(size.group(1))))}"'
    return re.sub(r'style="([^"]*)"', fix, html_)


def fmt_em(x):
    return "0" if x == 0 else f"{x:g}em"


def tokens_css():
    light = "\n".join(f"  --{c['name']}: {c['value']['light']};" for c in T["color"]["tokens"])
    light += "\n" + "\n".join(f"  --{s['name']}: {s['value']['light']};" for s in T["shadow"]["tokens"])
    cobalt = "\n".join(f"  --{c['name']}: {c['value']['cobalt']};" for c in T["color"]["tokens"])
    root = "\n".join(f"  --{t['name']}: {t['value']};" for fam in ("spacing", "radius") for t in T[fam]["tokens"])
    return f":root {{\n{light}\n{root}\n  color-scheme: light;\n}}\n.theme-cobalt {{\n{cobalt}\n}}\n"


def status_css():
    """Success, warning and danger from the brand's own generated tokens, for the figure kit's chips (fallbacks live in figures.css)."""
    css = (BRAND / "opendesigner/build/css/tokens.css").read_text()
    out = []
    for var, name in (("ok", "success"), ("warn", "warning"), ("bad", "danger")):
        strong = re.search(rf"--ds-color-{name}-light-11:\s*([^;]+);", css)
        soft = re.search(rf"--ds-color-{name}-light-2:\s*([^;]+);", css)
        if strong and soft:
            out.append(f"--{var}:{strong.group(1).strip()};--{var}-soft:{soft.group(1).strip()};")
    return (":root{" + "".join(out) + "}\n") if out else ""


# ---------------------------------------------------------------- Markdown (headings, lists, code, links, bold)
def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", re.sub(r"<[^>]+>", "", s).lower()).strip("-")


def code_html(s):
    """Escaped code, ready for the page: a word never splits (Chrome breaks "--why" between its hyphens and "tokens.css" anywhere).
    Lines break at spaces and after a path's slash; a word longer than 24 characters may also break after a dot, hyphen or comma."""
    def word(m):
        w = re.sub(r"(?<=[A-Za-z0-9_*])/(?=\S)", "/<wbr>", m.group(0))
        if len(m.group(0)) > 24:
            w = re.sub(r"(?<=[A-Za-z0-9])\.(?=[A-Za-z0-9{]{5})", ".<wbr>", w)
            w = re.sub(r"(?<=[A-Za-z0-9])-(?=[A-Za-z0-9]{3})", "-<wbr>", w)
            w = re.sub(r"(?<=[A-Za-z0-9]),(?=\S)", ",<wbr>", w)
        return f'<span class="w">{w}</span>'
    return re.sub(r"\S+", word, s)


def inline(s):
    s = esc(s, quote=False)
    s = re.sub(r"`([^`]+)`", lambda m: "<code>" + code_html(m.group(1)) + "</code>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', s)
    return s


def render_list(block):
    """A Markdown list at any depth: an item indented further than the one before it belongs to it, and a plain indented
    line continues the latest item."""
    root = {"children": [], "indent": -1}
    stack = [root]
    for raw in block:
        m = re.match(r"^( *)(\d+\.|-) (.*)", raw)
        if m:
            node = {"text": m.group(3), "children": [], "indent": len(m.group(1)), "ordered": m.group(2)[0].isdigit()}
            while len(stack) > 1 and stack[-1]["indent"] >= node["indent"]:
                stack.pop()
            stack[-1]["children"].append(node)
            stack.append(node)
        elif len(stack) > 1:
            stack[-1]["text"] += " " + raw.strip()

    def html_(items):
        tag = "ol" if items[0]["ordered"] else "ul"
        return f"<{tag}>" + "".join(f"<li>{inline(n['text'])}" + (html_(n["children"]) if n["children"] else "") + "</li>" for n in items) + f"</{tag}>"
    return html_(root["children"])


def md_to_html(md, toc=None):
    out, lines, i = [], md.strip().splitlines(), 0
    while i < len(lines):
        ln = lines[i]
        fm = FIG_RE.match(ln.strip())
        if fm:
            out.append(figure(fm.group(1))); i += 1
            continue
        if ln.strip() in CHANGELOG_BLOCKS:  # the version, git's record and CHANGELOG.md, made when the site is built
            out.append(md_to_html(CHANGELOG_BLOCKS[ln.strip()](), toc)); i += 1
            continue
        em = EVALS_RE.match(ln.strip())
        if em:
            import evals_html
            out.append(evals_html.block(em.group(1))); i += 1
            continue
        if ln.startswith("```"):
            j, code = i + 1, []
            while j < len(lines) and not lines[j].startswith("```"):
                code.append(lines[j]); j += 1
            out.append(f'<div class="code"><pre><code>{code_html(esc(chr(10).join(code), quote=False))}</code></pre>'
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
            block = []  # the whole list, with its nested lines; render_list() builds any depth from the indents
            while i < len(lines) and (re.match(r"^(\d+\.|-) ", lines[i]) or (lines[i].startswith("  ") and block)):
                block.append(lines[i]); i += 1
            out.append(render_list(block))
            continue
        elif ln.strip():
            para = [ln]
            while i + 1 < len(lines) and lines[i + 1].strip() and not re.match(r"^(#|```|> |\d+\. |- |\||\{\{figure)", lines[i + 1]):
                i += 1; para.append(lines[i])
            out.append(f"<p>{inline(' '.join(para))}</p>")
        i += 1
    return "\n".join(out)


def changelog_md():
    """CHANGELOG.md from its first version heading on, a level down (it sits under the page's "Highlights" heading), with
    links to repo files pointed at GitHub."""
    text = (ROOT / "CHANGELOG.md").read_text()
    text = re.sub(r"^## \[([^\]]+)\]", r"## \1", text[text.index("\n## ") + 1:], flags=re.M)  # "## [Unreleased]" reads "Unreleased"
    text = re.sub(r"^(#{2,5}) ", r"#\1 ", text, flags=re.M)
    return re.sub(r"\]\((?!https?:|#|/|mailto:)([^)]+)\)", lambda m: f"]({GH}/blob/main/{m.group(1)})", text)

VERSION = json.loads((ROOT / "plugin.json").read_text())["version"]  # in step with engine.py and .claude-plugin (build_dist.py --check)


def git_out(*args):
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else ""


def day_name(iso):
    d = dt.date.fromisoformat(iso)
    return f"{d.day} {d.strftime('%B')} {d.year}"


def version_facts():
    """The version every copy stamps into the systems it builds, the day a git tag v<version> released it (None until
    then), and the day of the newest change."""
    return {"version": VERSION, "released": git_out("log", "-1", "--format=%cs", f"v{VERSION}") or None,
            "latest_change": git_out("log", "-1", "--format=%cs") or TODAY}


def changes_by_day():
    """Every change on main, newest first, grouped by the day it landed: git's own record, so it can't fall behind."""
    days = {}
    for line in git_out("log", "--first-parent", "--format=%H%x1f%cs%x1f%s").splitlines():
        h, day, subject = line.split("\x1f", 2)
        days.setdefault(day, []).append((h, subject))
    return days


def update_md():
    """How to see which version you have and how to update: on the changelog page and in its Markdown copy."""
    return f"""| To find out | Run |
|---|---|
| Which version made your design system, and whether it is older than the copy you have | `engine.py version`, from the OpenDesigner skill's `scripts` folder, in your project (your AI knows where it is) |
| Which version you have installed in Claude Code | `claude plugin list` |

**To update in Claude Code,** run `claude plugin update opendesigner@opendesigner`, or open `/plugin`, find OpenDesigner on the Installed tab and choose Update now. Updates from this marketplace stay off until you turn them on: in `/plugin`, open the Marketplaces tab, select opendesigner and choose Enable auto-update. If you cloned the repository, run `git pull`. In the Claude app, upload the newest [opendesigner.zip]({SITE_URL}/.well-known/agent-skills/opendesigner.zip) again."""


def version_md():
    v = version_facts()
    state = (f"released on {day_name(v['released'])}" if v["released"]
             else "in development. It isn't released yet, so every change on this page is part of it")
    return f"""## Current version

**OpenDesigner {v['version']}**, {state}. The newest change is from {day_name(v['latest_change'])}.

{update_md()}

Tools and AI agents can read the same facts from [version.json]({SITE_URL}/version.json), and follow new changes in the [Atom feed]({SITE_URL}/changelog.xml).
"""


def changes_md(days=60):
    by_day = changes_by_day()
    if not by_day:
        return f"The full history is on GitHub: {GH}/commits/main"
    out = []
    for day in sorted(by_day, reverse=True)[:days]:
        out += [f"### {day_name(day)}", ""] + [f"- {subject} ([{h[:7]}]({GH}/commit/{h}))" for h, subject in by_day[day]] + [""]
    if len(by_day) > days:
        out.append(f"Older changes are in [the full history on GitHub]({GH}/commits/main).")
    return "\n".join(out).strip()


def changes_feed(days=30):
    """An Atom feed with one entry per day of changes, newest first, so anyone can follow them in a feed reader."""
    by_day = changes_by_day()
    ordered = sorted(by_day, reverse=True)[:days]
    entries = "".join(
        f'<entry><title>{esc(day_name(d))}: {len(by_day[d])} change{"s" if len(by_day[d]) != 1 else ""}</title>'
        f'<id>{SITE_URL}/docs/changelog/#{slugify(day_name(d))}</id>'  # ids keep the first address, so feed readers don't list entries again
        f'<updated>{d}T23:59:59Z</updated>'
        f'<link href="{SITE_URL}/changelog/#{slugify(day_name(d))}"/><content type="html">'
        + esc("<ul>" + "".join(f'<li>{esc(s)} (<a href="{GH}/commit/{h}">{h[:7]}</a>)</li>' for h, s in by_day[d]) + "</ul>")
        + "</content></entry>" for d in ordered)
    updated = f"{ordered[0]}T23:59:59Z" if ordered else f"{TODAY}T00:00:00Z"
    return ('<?xml version="1.0" encoding="utf-8"?>\n<feed xmlns="http://www.w3.org/2005/Atom">'
            f'<title>OpenDesigner: every change</title><subtitle>Each change to OpenDesigner, by day. Version {VERSION}.</subtitle>'
            f'<id>{SITE_URL}/changelog.xml</id><link href="{SITE_URL}/changelog.xml" rel="self"/><link href="{SITE_URL}/changelog/"/>'
            f'<updated>{updated}</updated><author><name>{NAME}</name></author>{entries}</feed>\n')


def whats_new_md():
    """CHANGELOG.md's highlights for visitors: one line each, newest first, dated by the day git says the line was
    written (git blame), and marked when it is a fix. The explanation stays under "Highlights, explained"."""
    import datetime as _dt
    items, section, ts, when = [], "", 0, None
    for line in git_out("blame", "--line-porcelain", "CHANGELOG.md").splitlines():
        if line.startswith("committer-time "):
            ts = int(line.split()[1])
        elif line.startswith("committer-tz "):  # the day as the person who wrote it saw it, as git log %cs shows it
            z = line.split()[1]
            tz = _dt.timezone((-1 if z[0] == "-" else 1) * _dt.timedelta(hours=int(z[1:3]), minutes=int(z[3:5])))
            when = _dt.datetime.fromtimestamp(ts, tz).date().isoformat()
        elif line.startswith("\t"):
            text = line[1:]
            if text.startswith("### "):
                section = text[4:].strip()
            m = re.match(r"^- \*\*(.+?)\*\*", text)
            if m and when:
                items.append((ts, when, m.group(1).strip().rstrip(".:"), section == "Fixed"))
    items.sort(key=lambda x: x[0], reverse=True)
    return "\n".join(f"- {day_name(d)}: {t}" + (" (a fix)" if fixed else "") for _, d, t, fixed in items)


CHANGELOG_BLOCKS = {"{{changelog}}": lambda: changelog_md(), "{{version}}": lambda: version_md(), "{{changes}}": lambda: changes_md(),
                    "{{whatsnew}}": lambda: whats_new_md()}
FEED_LINK = f'<link rel="alternate" type="application/atom+xml" href="/changelog.xml" title="OpenDesigner: every change">\n'



def plain(s):
    s = re.sub(r"\{\{figure:[a-z0-9-]+\}\}", "", s)
    return re.sub(r"[`*]", "", re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)).strip()


def figure(name):
    """Inline site/figures/<name>.html, a figure drawn with the kit in static/figures.css. A data-scene gets its photo and credit."""
    f = FIGURES / f"{name}.html"
    if not f.exists():
        raise SystemExit(f"figure not found: {f}")
    h = f.read_text().strip()
    if not h.startswith("<figure") or "<figcaption" not in h or not h.endswith("</figure>"):
        raise SystemExit(f"figure {name}: must be a single <figure class=\"fig\"> ending in <figcaption>...</figcaption></figure>")
    if "<script" in h or "<img" in h or "http" in h:
        raise SystemExit(f"figure {name}: no scripts, images or external links inside figures")
    for key in re.findall(r'data-scene="([a-z0-9-]+)"', h):
        pid, author, page_id = SCENES[key]
        h = h.replace(f'data-scene="{key}"', f'style="background-image:url({scene_url(key)})"', 1)
        h = h.replace("</figcaption>", f' Photo: <a href="https://unsplash.com/photos/{page_id}">{esc(author)}</a> on Unsplash.</figcaption>', 1)
    return apple_tracking_inline(h)


def scene_url(key, w=1400):
    """A figure's photo: one address for its background and for any preload of it, so the browser fetches it once."""
    return f"https://images.unsplash.com/{SCENES[key][0]}?auto=format&fit=crop&w={w}&q=70"


def figure_caption(name):
    m = re.search(r"<figcaption[^>]*>(.*?)</figcaption>", (FIGURES / f"{name}.html").read_text(), re.S)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m.group(1))).strip() if m else ""


def strip_figures(md):
    """The Markdown copies and llms-full.txt keep each figure as its caption, the changelog as its text, and each live
    evals block as a pointer to the page that shows it (no placeholder reaches a reader)."""
    md = re.sub(r"^\{\{figure:([a-z0-9-]+)\}\}$", lambda m: f"*Figure: {figure_caption(m.group(1))}*", md, flags=re.M)
    md = re.sub(r"^(\{\{(?:changelog|version|changes|whatsnew)\}\})$", lambda m: CHANGELOG_BLOCKS[m.group(1)]().strip(), md, flags=re.M)
    return re.sub(r"^\{\{evals:([a-z-]+)\}\}$", lambda m: f"*The latest results for this part are on the page: {SITE_URL}/docs/evals/*", md, flags=re.M)


def load_docs():
    pages = []
    for f in sorted(DOCS.glob("*.md")):
        raw = f.read_text()
        fm, body = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S).groups()
        meta = dict(re.findall(r"^(\w+): (.*)$", fm, re.M))
        slug = f.stem
        meta.update(slug=slug, body=body.strip(), path="/docs/" if slug == "index" else f"/docs/{slug}/",
                    order=float(meta.get("order", 99)), section=meta.get("section", "Reference"))
        if slug == "changelog":  # its own page at /changelog/, outside the docs: no section, so no docs menu, index or next link
            meta.update(path="/changelog/", section="Changelog")
        pages.append(meta)
    pages.sort(key=lambda p: (SECTIONS.index(p["section"]) if p["section"] in SECTIONS else 9, p["order"]))
    return pages


# ---------------------------------------------------------------- shared parts
GH_ICON = ('<svg aria-hidden="true" viewBox="0 0 16 16" width="16" height="16"><path fill="currentColor" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 '
           '0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07'
           '-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 '
           '2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>')
ARROW = '<svg class="arrow" aria-hidden="true" viewBox="0 0 14 14"><path d="M3 11L11 3M5 3h6v6" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
CHEVRON = '<svg aria-hidden="true" viewBox="0 0 16 16" width="16" height="16"><path d="M6 3l5 5-5 5" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>'
STATE = {"stars": ""}
CUR, EAGER, LAZY = ' aria-current="page"', ' fetchpriority="high"', ' loading="lazy"'
NBH = "\u2011"  # non-breaking hyphen: headings keep hyphenated words whole


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
        groups.append(f'<div class="side-group"><h2 class="side-h kicker">{sec}</h2><ul>{lis}</ul></div>')
    show = f'<div class="side-group"><h2 class="side-h kicker">Examples</h2><ul><li><a href="/showcase/"{CUR if current == "/showcase/" else ""}>Showcase</a></li><li><a href="/library/">Component library</a></li></ul></div>'
    return (f'<aside class="side" aria-label="Documentation"><details class="side-mobile"><summary>Documentation menu</summary>'
            f'<nav>{"".join(groups)}{show}</nav></details><nav class="side-desk">{"".join(groups)}{show}</nav></aside>')


def shell(path, seo_title, description, main_html, pages, ld=(), og="/og/home.jpg", md=True, wide=False, robots="index, follow, max-image-preview:large", home=False, og_alt=None, preload=""):  # preload: extra head lines (a preload, a feed link); home: True for the home layout, or a class name for another page without the docs sidebar
    canon = SITE_URL + path
    md_link = f'<link rel="alternate" type="text/markdown" href="{path}index.md" title="Markdown">' if md else ""
    inner = (f'<main id="main" class="{"home" if home is True else home}">\n{main_html}\n</main>' if home else
             f'<div class="layout{" wide" if wide else ""}">\n{sidebar(pages, path)}\n<main id="main" class="main">\n{main_html}\n</main>\n</div>')
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
<meta property="og:image:alt" content="{esc(og_alt or OG_ALT)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(seo_title)}">
<meta name="twitter:description" content="{esc(description)}">
<meta name="twitter:image" content="{SITE_URL}{og}">
<meta name="twitter:image:alt" content="{esc(og_alt or OG_ALT)}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/fonts/hanken-300-700.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preconnect" href="https://images.unsplash.com">
{preload}<link rel="stylesheet" href="/site.css">
<noscript><style>.g-wait{{animation-delay:60ms!important}}</style></noscript>
{md_link}
<link rel="sitemap" type="application/xml" href="/sitemap.xml">
{jsonld(*ld)}
</head>
<body>
{DECO_DEFS}
<a class="skip" href="#main">Skip to content</a>
<header class="bar"><div class="bar-in">
<a class="brand" href="/" aria-label="{NAME} home">{lockup()}</a>
<nav class="top-nav" aria-label="Main"><a href="/docs/"{CUR if path.startswith("/docs/") else ""}>Docs</a><a href="/docs/install/">Install</a><a href="/docs/enterprise/">For teams</a><a href="/showcase/"{CUR if path == "/showcase/" else ""}>Showcase</a><a class="nav-lib" title="Component library" href="/library/"{CUR if path.startswith("/library/") else ""}><svg class="nav-ic" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><rect x="3.5" y="3.5" width="7" height="7" rx="1.5" fill="none" stroke="currentColor" stroke-width="1.8"/><rect x="13.5" y="3.5" width="7" height="7" rx="1.5" fill="none" stroke="currentColor" stroke-width="1.8"/><rect x="3.5" y="13.5" width="7" height="7" rx="1.5" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M17 13.5v7M13.5 17h7" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg><span class="nav-lib-t">Library</span></a></nav>
<a class="nav-book" href="/book/">Book a call</a><a class="gh-btn" href="{GH}">{GH_ICON}<span>GitHub</span><span class="gh-count" data-stars>{STATE["stars"]}</span></a>
</div></header>
{inner}
{footer(pages)}
<script src="/site.js" defer></script>{PH_TAG}
<script src="/_vercel/speed-insights/script.js" defer></script>
</body>
</html>
"""


def footer(pages):
    by = {s: [p for p in pages if p["section"] == s and p["path"] != "/docs/security/"][:6] for s in SECTIONS}  # security is under Trust
    cols = "".join(f'<div><h2 class="foot-h kicker">{s}</h2><ul>' + "".join(f'<li><a href="{p["path"]}">{esc(p["title"])}</a></li>' for p in ps) + "</ul></div>"
                   for s, ps in by.items() if ps)
    trust = (f'<div><h2 class="foot-h kicker">Trust</h2><ul><li><a href="/docs/security/">Security and data</a></li><li><a href="{GH}/blob/main/SECURITY.md">Report a vulnerability</a></li>'
             f'<li><a href="/docs/changelog/">Changelog · v{VERSION}</a></li><li><a href="{GH}/blob/main/LICENSE">Licence (MIT)</a></li></ul></div>')
    proj = (f'<div><h2 class="foot-h kicker">Project</h2><ul><li><a href="{GH}">GitHub</a></li><li><a href="{GH}/issues/new/choose">Report a problem</a></li>'
            f'<li><a href="/docs/contribute/">Contribute</a></li><li><a href="/book/">Book a call</a></li><li><a href="/showcase/">Showcase</a></li><li><a href="/llms.txt">llms.txt</a></li><li><a href="/sitemap.xml">Sitemap</a></li></ul></div>')
    return (f'<footer class="foot"><div class="foot-in"><div class="foot-brand">{lockup()}<p>Free and open source. MIT for code, '
            f'CC BY 4.0 for docs.</p></div>{cols}{trust}{proj}</div><p class="foot-legal">OpenDesigner is an independent open-source project. Claude, '
            f'ChatGPT, Codex, Cursor, Figma and other names belong to their owners and appear only to say where OpenDesigner runs. Photos: Unsplash '
            f'photographers, credited where shown. Updated <time datetime="{TODAY}" style="white-space:nowrap">{TODAY}</time>.</p></footer>')


# Decoration, direction A "Press proof" (owner's choice, 2026-10-15): marks from a printer's proof sheet; styles in static/deco.css.
DECO_DEFS = '<svg width="0" height="0" aria-hidden="true" focusable="false" style="position:absolute">\n<filter id="a-ink" x="-4%" y="-4%" width="108%" height="108%">\n<feTurbulence type="fractalNoise" baseFrequency="1.35" numOctaves="2" seed="7" result="n"/>\n<feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -9 6.6" result="m"/>\n<feComposite in="SourceGraphic" in2="m" operator="in"/>\n</filter>\n</svg>'
A_PICTS = ['<svg class="a-pict" viewBox="0 0 48 32" aria-hidden="true"><path class="a-pf" d="M.5 3.5v-3h3M44.5.5h3v3M47.5 28.5v3h-3M3.5 31.5h-3v-3"/>\n<path d="M9 5.5h11l3.5 3.5v15H9z" fill="#fff"/><path d="M13 9.5h11l4.5 4.5v13H13z" fill="#fff"/><path d="M24 9.5V14h4.5"/>\n<path d="M16 18.5h8M16 21.5h6M16 24.5h7" stroke-width="1"/>\n<circle cx="33" cy="20" r="5.2" fill="#e3ecff" stroke="#2338ff" stroke-width="1.5"/><path d="M36.8 23.8l4.2 4.2" stroke="#2338ff" stroke-width="2.2" stroke-linecap="round"/></svg>', '<svg class="a-pict" viewBox="0 0 48 32" aria-hidden="true"><path class="a-pf" d="M.5 3.5v-3h3M44.5.5h3v3M47.5 28.5v3h-3M3.5 31.5h-3v-3"/>\n<path d="M8 16h32" stroke-width="1"/>\n<circle cx="8" cy="16" r="2.8" fill="#fff"/><circle cx="16" cy="16" r="2.8" fill="#fff"/><circle cx="24" cy="16" r="2.8" fill="#fff"/>\n<circle cx="32" cy="16" r="2.8" fill="#2338ff" stroke="#2338ff"/><circle cx="32" cy="16" r="6.4" stroke="#2338ff"/><circle cx="40" cy="16" r="2.8" fill="#fff"/></svg>', '<svg class="a-pict" viewBox="0 0 48 32" aria-hidden="true"><path class="a-pf" d="M.5 3.5v-3h3M44.5.5h3v3M47.5 28.5v3h-3M3.5 31.5h-3v-3"/>\n<rect x="7" y="7" width="18" height="18" rx="3" fill="#2338ff" stroke="#2338ff"/>\n<text x="16" y="19.6" text-anchor="middle" fill="#fff" stroke="none" font-family="Hanken Grotesk" font-weight="600" font-size="9.5">Aa</text>\n<circle cx="35" cy="16" r="7"/><path d="M31.6 16.2l2.4 2.4 4.8-5" stroke="#2338ff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>', '<svg class="a-pict" viewBox="0 0 48 32" aria-hidden="true"><path class="a-pf" d="M.5 3.5v-3h3M44.5.5h3v3M47.5 28.5v3h-3M3.5 31.5h-3v-3"/>\n<path d="M6 5.5h11l3.5 3.5v17.5H6z" fill="#fff"/><path d="M17 5.5V9h3.5"/><path d="M9 13.5h8M9 16.5h6M9 19.5h8M9 22.5h5" stroke-width="1"/>\n<path d="M23 16h8" stroke-dasharray="2 2"/><path d="M29.5 13l3 3-3 3" stroke-linecap="round" stroke-linejoin="round"/>\n<rect x="35" y="11.5" width="9" height="9" rx="2" fill="#2338ff" stroke="#2338ff"/></svg>']


def idx(n, label):
    """A numbered section tab."""
    return f'<p class="kicker a-idx"><span class="a-idx-n">{n}</span>{label}</p>'


# ---------------------------------------------------------------- the docs home (/docs/): the documentation directory
def docs_home(pages, facts, faq):
    pages = [p for p in pages if p["section"] in SECTIONS]  # the docs only: the changelog has its own page
    stages = [("Start", "Answer up to five questions in your AI tool, or point it at the app or brand you already have. You get a working draft of color, type, spacing, corners, depth and motion, each with its reason."),
              ("Use", "Import the tokens, the CSS variables or the Tailwind theme. Coding agents read DESIGN.md before they touch the interface, so new screens follow the same rules."),
              ("Keep", "Changes go through a decision log that records who set what and why. A review command finds colors, sizes and radii in the code that drifted from the tokens.")]
    roles = [("Product designers", "whiteboard", "/docs/designers/",
              ["Hand the scales, states and contrast checks to the engine, and keep the direction yourself.",
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
    rows = "".join(f'<li><a href="{p["path"]}"><span class="row-n num">{i + 1:02d}</span><span class="row-t">{esc(p["title"])}</span><span class="row-s">{p["section"]}</span>{CHEVRON}</a></li>' for i, p in enumerate(pages))
    n = lambda v: "—" if v is None else f"{v:,}"
    faq_html = "".join(f'<details class="qa"><summary><h3>{esc(q)}</h3></summary><div class="ans">{md_to_html(a)}</div></details>' for q, a in faq[:5])
    body = f"""
<section class="hero">
<nav class="crumb" aria-label="Breadcrumb"><a href="/">{NAME}</a><span aria-hidden="true">/</span><span aria-current="page">Docs</span></nav>
<h1 class="t-hero">OpenDesigner docs: build a design system <strong>with the AI you already use</strong>, and keep it consistent.</h1>
<p class="lede">{HERO_LEDE}</p>
<div class="cta-row">
<a class="btn primary" href="/docs/install/">Install</a>
<a class="btn secondary" href="/docs/introduction/">Read the introduction</a>
</div>
<div class="cmd"><span class="kicker">Claude Code</span><code>/plugin marketplace add ckryptickunal/OpenDesigner</code><button class="copy" type="button" data-copy-text="/plugin marketplace add ckryptickunal/OpenDesigner
/plugin install opendesigner@opendesigner">Copy both</button></div>
<p class="works"><span class="kicker">Works with</span><span>Claude Code, the Claude app, ChatGPT, Codex, Cursor and other tools that read Agent Skills.</span></p>
{figure("hero-interview")}
</section>

<section class="block" id="start">
<div class="block-head"><div><p class="kicker">Documentation</p><h2 class="t-h2">Start here</h2></div><a class="more" href="#all">All {len(pages)} pages {CHEVRON}</a></div>
<div class="starts">{"".join(f'<a class="start" href="{u}"><span class="kicker">{k}</span><strong>{t}</strong><span>{d}</span>{ARROW}</a>' for k, t, d, u in STARTS)}</div>
</section>

<section class="block" id="process">
<p class="kicker">Process</p>
<h2 class="t-h2">Where it fits in your process</h2>
<ol class="stages">{"".join(f'<li><span class="num">0{i + 1}</span><h3>{t}</h3><p>{inline(d)}</p></li>' for i, (t, d) in enumerate(stages))}</ol>
{figure("home-process")}
</section>

<section class="block" id="roles">
<p class="kicker">Who it is for</p>
<h2 class="t-h2">What it changes for you</h2>
<div class="roles">{"".join(f'<article class="role">{photo(k, 480, 480, "duo role-photo", "112px")}<div class="role-text"><h3>{t}</h3><ul>' + "".join(f"<li>{inline(x)}</li>" for x in xs) + f'</ul><a class="more" href="{u}">Guide for {t.lower()} {CHEVRON}</a></div></article>' for t, k, u, xs in roles)}</div>
<p class="roles-credit">Photos: {", ".join(f'<a href="https://unsplash.com/photos/{PHOTOS[k][2]}">{esc(PHOTOS[k][1])}</a>' for _t, k, _u, _x in roles)} on Unsplash.</p>
</section>

<section class="block" id="output">
<div class="split">
<div><p class="kicker">After the first run</p><h2 class="t-h2">What you have after the first run</h2>
<p class="lede">Files in your project, readable by people and AI tools. Nothing lives on a server, and the same answers always give the same tokens and exports.</p>
<ul class="tree">{"".join(f'<li><code>{f}</code><span>{w}</span></li>' for f, w in OUTPUT_FILES)}</ul></div>
{overview_shot()}
</div>
</section>

<section class="block" id="teams">
<div class="split">
<div><p class="kicker">For teams</p><h2 class="t-h2">For design-system teams</h2>
<p class="lede">A written record your team and your AI tools build from, kept as files in your repository. It is early for teams: nobody has run a team pilot yet, and there is no hosted service and no SSO.</p>
<p class="cta-row"><a class="btn primary" href="/docs/enterprise/">Read the team guide</a><a class="btn secondary" href="/docs/security/">Security and data</a></p></div>
<ul class="checks">{"".join(f'<li><span class="check" aria-hidden="true"></span><span><strong>{a}</strong> {b}</span></li>' for a, b in TEAM_CHECKS)}</ul>
</div>
</section>

<section class="block" id="all">
<div class="block-head"><div><p class="kicker">Every page</p><h2 class="t-h2">All {len(pages)} pages</h2></div></div>
<ol class="rows">{rows}</ol>
</section>

<section class="block" id="status">
<div class="split">
<div><p class="kicker">Status</p><h2 class="t-h2">Where it stands</h2>
<ul class="status">{"".join(f"<li>{x}</li>" for x in STATUS)}</ul></div>
{gh_card(facts)}
</div>
</section>

<section class="block" id="faq">
<div class="block-head"><div><p class="kicker">FAQ</p><h2 class="t-h2">Questions</h2></div><a class="more" href="/docs/faq/">All questions {CHEVRON}</a></div>
<div class="faq">{faq_html}</div>
</section>
"""
    ld = [crumbs_ld([("Docs", "/docs/")]),
          {"@context": "https://schema.org", "@type": "CollectionPage", "name": "OpenDesigner documentation", "url": SITE_URL + "/docs/",
           "description": DOCS_DESCRIPTION, "inLanguage": "en", "isPartOf": {"@type": "WebSite", "name": NAME, "url": SITE_URL + "/"},
           "hasPart": [{"@type": "TechArticle", "headline": p["title"], "url": SITE_URL + p["path"]} for p in pages]}]
    return shell("/docs/", "OpenDesigner docs: install, guides, concepts and reference", DOCS_DESCRIPTION, body, pages, ld, wide=True)


DOCS_DESCRIPTION = ("How to install OpenDesigner, make a first design system with your AI tool, use it in a team, and how the engine, "
                    "tokens and checks work.")
OUTPUT_FILES = [("DESIGN.md", "your rules in plain words"), ("opendesigner/tokens/", "DTCG 2025.10"), ("build/css/tokens.css", "CSS variables"),
                ("build/tailwind/theme.css", "Tailwind v4"), ("build/figma/", "Figma variables"), ("build/swift/, build/compose/", "iOS and Android"),
                ("overview.html", "the system on one page"), ("decisions.md", "every choice and why")]
OVERVIEW_IMG = ('<picture><source type="image/webp" srcset="/img/overview-1440.webp 1440w, /img/overview-720.webp 720w" sizes="(max-width: 1100px) 100vw, 640px">'
                '<img src="/img/overview-1440.jpg" width="1440" height="900" loading="lazy" alt="The overview page generated for OpenDesigner\'s own brand, with each area marked Chosen, Default or Not enough information."></picture>')


BA = SITE / "demo" / "before-after"  # the before-and-after demo: capture.py measured it with the review skill's own tools


def demo_before_after_files():
    """review.py compare's report at /demo/before-after/, from capture.py's screenshots and marks. The site's policy allows no
    inline script, so the report's picker moves into its own file. The home page draws the pages themselves (before_after)."""
    if not all((BA / "shots" / f"{n}.png").exists() for n in ("before", "after")):  # git-ignored, like the showcase renders
        raise SystemExit("site/demo/before-after/shots/ is missing: run python3 site/demo/before-after/capture.py first")
    tmp = CACHE / "before-after"
    tmp.mkdir(parents=True, exist_ok=True)
    subprocess.run([sys.executable, str(ROOT / "skills/opendesigner-review/scripts/review.py"), "compare", "--dir", str(tmp), "--out", str(tmp / "compare.html"),
                    "--before", str(BA / "shots/before.png"), "--after", str(BA / "shots/after.png"), "--marks", str(BA / "review/marks-before.json"),
                    "--after-marks", str(BA / "review/marks-after.json"), "--title", "Merriweft invoices: before and after"], check=True, capture_output=True)
    report = (tmp / "compare.html").read_text()
    m = re.search(r"<script>(.*)</script>", report, re.S)
    (DIST / "demo" / "before-after").mkdir(parents=True, exist_ok=True)
    (DIST / "demo" / "before-after" / "picker.js").write_text(m.group(1))
    report = report[:m.start()] + '<script src="picker.js"></script>' + report[m.end():]
    report = report.replace('<link rel="icon" href="data:,">', '<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">')  # the site has its own
    desc = ("An OpenDesigner review of an invented invoicing page: the page today, the audit drawn on it, and the fix, "
            "each with what it makes better.")
    report = report.replace("<title>", f'<meta name="description" content="{desc}">\n<meta name="robots" content="noindex">\n'
                                       f'<link rel="canonical" href="{SITE_URL}/demo/before-after/">\n<title>', 1)
    (DIST / "demo" / "before-after" / "index.html").write_text(report)


DEMO_W = 1200  # the width the demo pages are laid out at on the home page, then scaled to fit (site.js)


def without_media(css):
    """CSS without its @media blocks: the demo pages are always laid out at DEMO_W, whatever the screen."""
    out, i = [], 0
    while (j := css.find("@media", i)) >= 0:
        out.append(css[i:j])
        k, depth = css.index("{", j) + 1, 1
        while depth:
            depth += {"{": 1, "}": -1}.get(css[k], 0)
            k += 1
        i = k
    return "".join(out + [css[i:]])


def demo_tokens(src):
    """Merriweft's token values that src uses (directly or through other tokens), from the blocks that apply by default: the
    light theme, compact density, standard motion and a fine pointer. Written on :host, the demo page's root."""
    css = re.sub(r"/\*.*?\*/", "", (BA / "opendesigner/build/css/tokens.css").read_text(), flags=re.S)
    decl, stack, pos = {}, [], 0  # each block's prelude is the text since the last ; or brace before its {
    for m in re.finditer(r"[{}]", css):
        if m.group() == "{":
            stack.append((css[pos:m.start()].strip().split(";")[-1].strip(), m.end()))
        else:
            prelude, at = stack.pop()
            outer = [p for p, _ in stack]
            if ":root" in [x.strip() for x in prelude.split(",")] and all(o == "@media (pointer: fine)" for o in outer):
                decl.update(re.findall(r"(--ds-[\w-]+)\s*:\s*([^;{}]+);", css[at:m.start()]))
        pos = m.end()
    need, todo = [], re.findall(r"var\((--ds-[\w-]+)", src)
    while todo:
        v = todo.pop()
        if v in decl and v not in need:
            need.append(v)
            todo += re.findall(r"var\((--ds-[\w-]+)", decl[v])
    return ":host {" + "".join(f" {v}: {decl[v].strip()};" for v in decl if v in need) + " }\n"


def demo_page(name):
    """A demo page as a declarative shadow root: its own styles and markup, sealed off from the site's styles and the site's
    from its own. It is a picture of a page, so nothing in it can be tabbed to, followed or typed into."""
    page = (BA / f"{name}.html").read_text()
    css = re.sub(r"/\*.*?\*/", "", "\n".join(re.findall(r"<style>(.*?)</style>", page, re.S)), flags=re.S)
    body = re.search(r"<body>(.*)</body>", page, re.S).group(1).strip()
    body = body.replace(' href="#"', "").replace("<button ", '<button tabindex="-1" ')
    body = re.sub(r'<input class="search" placeholder="([^"]*)"[^>]*>', r'<span class="search">\1</span>', body)
    body = body.replace('id="g"', f'id="mw-{name}-g"').replace("url(#g)", f"url(#mw-{name}-g)")
    # no headings or landmarks of its own inside the home page: each becomes a box with its tag as a class
    tags = ("h1", "main", "header", "nav", "section")
    body = re.sub(r"<(/?)(" + "|".join(tags) + r")\b([^>]*)>", lambda m: "</div>" if m[1] else
                  (f'<div{m[3]}>'.replace('class="', f'class="{m[2]} ', 1) if 'class="' in m[3] else f'<div class="{m[2]}"{m[3]}>'), body)
    body = re.sub(r'\saria-current="[^"]*"', ' class="on"', body)  # the current nav item and filter keep their look
    body = re.sub(r'\s(aria-label|role)="[^"]*"', "", body)
    css = re.sub(r"[^{}]+(?=\{)", lambda m: re.sub(r"(?<![\w.#-])(" + "|".join(tags) + r")\b(?![\w-])", r".\1", m[0]), css)
    css = re.sub(r"\[aria-current\]", ".on", css)
    css = re.sub(r"(^|\n)body(\s*\{)", r"\1:host\2", without_media(css))
    css = ":host { all: initial; display: block; }\n" + (demo_tokens(css + body) if "tokens.css" in page else "") + css
    css += ".search { display: flex; align-items: center; }" + (" .search { color: var(--ds-color-text-secondary); }" if "tokens.css" in page else "")
    css = re.sub(r"\n\s*\n+", "\n", css).strip()
    return f'<template shadowrootmode="open"><style>{css}</style>{body}</template>'


def before_after():
    """Home #before-after: the audit as it happens, on the demo pages themselves (live HTML, not pictures). A scan finds each
    issue in the order it meets them (a dashed box, a number and a short line each), then the fix sweeps down with
    Merriweft's tokens: the fixed page builds itself as the line passes and each box becomes a check. site.js runs it once
    in view, measuring every box on the page as drawn; Today / Audit / Fixed and Replay stay for manual viewing and reduced
    motion. The issues are marks.in.json's, found by capture.py with the review skill's probe.js."""
    spec = json.loads((BA / "marks.in.json").read_text())
    after_sel = [m["sel"] for m in spec["after"]]
    marks = [dict(m, n=i + 1, asel=after_sel[i] if i < len(after_sel) else None) for i, m in enumerate(spec["before"])]
    shot = {n: json.loads((BA / "review" / f"marks-{n}.json").read_text())["page"] for n in ("before", "after")}
    # Numbers follow the scan (owner, 2026-10-22): site.js finds issues by height, those within 2% of the page's height
    # together and left to right (groups()), and each issue's number is its place in marks.in.json, so the two must agree.
    rows = []
    for m in sorted(json.loads((BA / "review" / "marks-before.json").read_text())["marks"], key=lambda m: m["rect"][1]):
        if rows and m["rect"][1] - rows[-1][0]["rect"][1] < shot["before"]["h"] * 0.02:
            rows[-1].append(m)
        else:
            rows.append([m])
    found = [m["n"] for r in rows for m in sorted(r, key=lambda m: m["rect"][0])]
    if found != sorted(found):
        raise SystemExit(f"site/demo/before-after/marks.in.json: list the issues in the order the scan meets them (top to bottom, "
                         f"then left to right), so the numbers count up; it would find them as {found}")
    tall = max(shot["before"]["h"], shot["after"]["h"]) / shot["before"]["w"]  # until site.js measures the pages as drawn
    data = {"width": DEMO_W, "marks": [{k: m[k] for k in ("n", "sel", "asel", "title", "short", "token")} for m in marks]}
    check = ('<svg viewBox="0 0 12 12" aria-hidden="true"><path d="M2.5 6.3 5 8.7l4.6-5.2" fill="none" stroke="currentColor" stroke-width="1.8" '
             'stroke-linecap="round" stroke-linejoin="round"/></svg>')
    boxes = "".join(f'<span class="au-mk" data-n="{m["n"]}"><b>{m["n"]}</b></span><span class="au-ok" data-n="{m["n"]}"><b>{check}</b></span>' for m in marks)
    rows = "".join(f'<li data-n="{m["n"]}"><span class="n"><span>{m["n"]}</span>{check}</span><div><h3>{esc(m["title"])}</h3>'
                   f'<p class="m">{esc(m["before"])}</p><p class="g">Fixing this makes {esc(m["gives"])}.</p><p class="s">{esc(m["stat"])}</p></div></li>'
                   for m in marks)
    # the token card: Merriweft's system as a small drawing; during the fix a chip leaves it for each region
    palette = ('<div class="au-tokens" aria-hidden="true"><svg viewBox="0 0 132 40"><rect x="1" y="1" width="38" height="38" rx="8" fill="#1f6f5c"/>'
               '<path d="M11 28V13l9 9.5L29 13v15" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>'
               '<text x="50" y="27" font-size="18" font-weight="600" fill="#242424">Aa</text>'
               '<path d="M80 30V18a8 8 0 0 1 8-8h12" fill="none" stroke="#242424" stroke-width="1.8" stroke-linecap="round"/>'
               '<path d="M110 16v14M110 23h12M122 16v14" fill="none" stroke="#575757" stroke-width="1.6" stroke-linecap="round"/></svg>'
               '<span>Merriweft tokens</span></div>')
    label = "The Merriweft invoices page, drawn live: as it is today, with the issues an audit finds, and after the fix."
    stage_inner = (f'<div class="au-win"><div class="au-chrome"><span class="au-dots"><i></i><i></i><i></i></span><span class="au-url">merriweft.example/invoices</span></div>'
                   f'<div class="au-stage" role="img" aria-label="{label}" style="aspect-ratio:1 / {tall:.4f}">'
                   f'<div class="au-cam"><div class="au-page b" aria-hidden="true">{demo_page("before")}</div>'
                   f'<div class="au-after"><div class="au-page a" aria-hidden="true">{demo_page("after")}</div></div>{boxes}'
                   f'<div class="au-line" aria-hidden="true"><span class="au-tag"></span></div></div>'
                   f'<div class="au-callout" aria-hidden="true"></div>{palette}</div></div>')
    st, credit = stage("woods-sage", stage_inner, "au-photo")
    replay = ('<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2.5 8a5.5 5.5 0 1 0 1.7-4M2.5 2.5v3h3" fill="none" stroke="currentColor" '
              'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>')
    tabs = "".join(f'<button type="button" role="tab" data-view="{k}" aria-selected="{"true" if k == "audit" else "false"}">{n}</button>'
                   for k, n in (("today", "Today"), ("audit", "Audit"), ("fixed", "Fixed")))
    return (f'<div class="au" data-au><div class="au-bar"><div class="tablist" role="tablist" aria-label="The invoices page: today, the audit, and the fix">{tabs}</div>'
            f'<button type="button" class="au-replay">{replay}<span>Replay</span></button><p class="au-status" aria-live="polite"><b>{len(marks)} issues</b> found on this page.</p></div>'
            f'<div class="au-body"><div>{st}<p class="au-cap" hidden></p></div>'
            f'<div><p class="au-empty" hidden>The page as it is today. Watch the audit, or press Audit to see what it finds.</p><ol class="au-list">{rows}</ol></div></div>'
            f'<script type="application/json" id="au-data">{json.dumps(data)}</script></div>'), credit


def overview_shot():
    st, credit = stage("woods-sage", OVERVIEW_IMG)
    return (f'<figure class="shot staged">{st}<figcaption>A real overview page: what you chose, what is still a default, and what only you can give, '
            f'like a logo. Photo: {credit} on Unsplash.</figcaption></figure>')
STATUS = ["The repository was created on 2026-09-23. It is early, and one person maintains it.",
          "There is no tagged release yet: 0.1.0 is planned. The engine's tests pass on the maintainer's computer; no CI runs are recorded yet.",
          "No watched user trials have happened yet. The usability tests so far were role-played by AI testers, and a recorded run in every AI tool is still on the list.",
          'AI agents built the showcase through the process, and weak pieces were rebuilt after review. <a href="/showcase/">See them</a>, with the findings.']


HOME_STATUS = ["Created on 2026-09-23 and maintained by one person. There is no tagged release yet; 0.1.0 is planned.",
               "No watched user trials yet, and no recorded run in every AI tool. The engine's tests pass."]


def book_link(label, primary=False):
    """A booking link when the owner has set one; otherwise plain text, never a placeholder link (site/config.json)."""
    url = CONFIG.get("BOOKING_FREE_URL")
    if not url:
        return f'<span class="h-soon">Bookings opening soon</span>'
    cls = "btn primary lg" if primary else "h-link"
    return f'<a class="{cls}" href="{esc(url)}" rel="noopener" target="_blank">{esc(label)}{"" if primary else " " + ARROW}</a>'


def book_page(pages):
    m = CONFIG["BOOKING_FREE_MINUTES"]
    body = f"""
<section class="h-sec h-first">
<nav class="crumb" aria-label="Breadcrumb"><a href="/">{NAME}</a><span aria-hidden="true">/</span><span aria-current="page">Book a call</span></nav>
<h1 class="h-h2 book-title">Work through your design with {CONFIG["HOST_NAME"]}.</h1>
<p class="h-lede book-lede">{CONFIG["HOST_NAME"]} is {CONFIG["HOST_ROLE"]}. Bring your product and leave with a clear first step for its design system. OpenDesigner stays free and open source, and you never need a call to use it.</p>
<div class="book-grid">
<article class="book-card">
<p class="kicker">Free · {m} minutes · Google Meet</p>
<h2>Intro call</h2>
<p>To see whether OpenDesigner fits your product, and where to start.</p>
<dl class="book-dl">
<div><dt>You'll be asked</dt><dd>Your product's address or repository (optional), the design problem you have today, your stage and your goal.</dd></div>
<div><dt>You leave with</dt><dd>A suggested first step. The call includes no code changes.</dd></div>
<div><dt>Please don't share</dt><dd>Confidential code or anything under a non-disclosure agreement in the booking form.</dd></div>
</dl>
<div class="book-act">{book_link("Book a free " + str(m) + "-minute call", primary=True)}</div>
<p class="h-fine">Booked through Google Calendar. The confirmation carries the Google Meet link.</p>
</article>
<article class="book-card later">
<p class="kicker">Later</p>
<h2>Paid sessions</h2>
<p>A design-system review of an existing product, and an implementation strategy session, will open later. Nothing is charged today.</p>
<p class="h-soon">Opening soon</p>
</article>
</div>
<p class="h-fine">The site counts visits and clicks without cookies, and records a visit only if you allow it (<a href="{GH}/blob/main/docs/PRIVACY.md#the-websites-product-analytics">what we collect</a>). This page is never recorded, and nothing you send through the booking form is used for anything but the call.</p>
</section>
"""
    ld = [crumbs_ld([("Book a call", "/book/")])]
    return shell("/book/", f"Book a free {m}-minute OpenDesigner intro call",
                 f"A free {m}-minute call with {CONFIG['HOST_NAME']}, OpenDesigner's maintainer: whether it fits your product and where to start. No code changes, no cost.",
                 body, pages, ld, home=True, md=False)


def stage(scene, inner, cls=""):
    """A screen on a photo: a rounded container with a free Unsplash photo and film grain, the screen in a soft glass bezel (owner, 2026-10-15)."""
    pid, author, page_id = SCENES[scene]
    return (f'<div class="stage {cls}" style="background-image:url(https://images.unsplash.com/{pid}?auto=format&fit=crop&w=1800&q=70)">'
            f'<div class="stage-in">{inner}</div></div>'), f'<a href="https://unsplash.com/photos/{page_id}">{esc(author)}</a>'


def gh_card(facts):
    n = lambda v: "—" if v is None else f"{v:,}"
    return (f'<article class="ghcard"><div class="gh-top">{GH_ICON}<a href="{GH}"><strong>{REPO}</strong></a></div>'
            f'<dl class="gh-stats"><div><dt>Licence</dt><dd>MIT</dd></div><div><dt>Release</dt><dd>0.1.0 planned</dd></div><div><dt>Open issues</dt><dd data-issues>{n(facts["issues"])}</dd></div>'
            f'<div><dt>Last push</dt><dd data-pushed>{facts["pushed"]}</dd></div></dl>'
            f'<div class="gh-actions"><a class="btn secondary" href="{GH}">{GH_ICON} Star on GitHub</a><a class="btn text" href="{GH}/issues/new/choose">Report a problem</a></div>'
            f'<p class="note">Live from GitHub. Tell us where it breaks: that is the most useful thing right now.</p></article>')


# ---------------------------------------------------------------- the home page (/): what it is, why, how, examples, install
DEMO = json.loads((SITE / "demo-systems.json").read_text())
CONFIG = {**json.loads((SITE / "config.json").read_text()), **{k: v for k, v in os.environ.items() if k.startswith(("BOOKING_", "CONTACT_"))}}
LOGOS = json.loads((SITE / "logos.json").read_text())["icons"]  # Simple Icons (CC0); owner, 2026-10-15: show the tools' own marks
HOSTS = [("Claude Code / app", "claude"), ("ChatGPT / Codex", "openai"), ("Cursor", "cursor"), ("Copilot in VS Code", "githubcopilot"), ("Gemini CLI", "googlegemini")]


def logo(slug, size=20):
    return (f'<svg class="logo" viewBox="0 0 24 24" width="{size}" height="{size}" aria-hidden="true" focusable="false">'
            f'<path fill="currentColor" d="{LOGOS[slug]["path"]}"/></svg>')
DEMO_UI = {  # the card each example builds with its own values; names, amounts and dates are invented and checked (12,940 + 1,420 + 500 = 14,860)
    "billerwick": {"title": "Invoice 2207", "chip": "Waiting on you", "sub": "Marlowe &amp; Pratt Supplies · due Fri 16 Oct", "big": "$14,860.00",
               "rows": [("Traction battery × 1", "$12,940.00"), ("Charger, three-phase × 1", "$1,420.00"), ("Delivery and fitting", "$500.00")],
               "primary": "Approve $14,860", "secondary": "Decline"},
    "pebbleday": {"title": "Evening reading", "chip": "On track", "sub": "Mia and Sam · 20 minutes a day", "big": "12-day streak",
               "rows": [("This week", "5 of 7 days"), ("Longest streak", "19 days"), ("Next reminder", "19:30")],
               "primary": "Mark today done", "secondary": "Skip today"},
    "fernhollow": {"title": "Renew your parking permit", "chip": "Step 2 of 4", "sub": "Your vehicle", "big": "",
               "field": ("Registration number", "AB12 CDE", "As it appears on your registration document"),
               "rows": [("Permit zone", "Zone C"), ("Permit length", "12 months")],
               "primary": "Continue", "secondary": "Save and finish later"}}
INSTALL_MARKS = {"claude-code": [], "claude-app": [], "agents": [], "chatgpt": [], "engine": []}  # the marks appear once, in the hero row
INSTALL = [
    ("claude-code", "Claude Code", "Add the plugin, then ask for a design system in your project.",
     "/plugin marketplace add ckryptickunal/OpenDesigner\n/plugin install opendesigner@opendesigner", "Then say: “Create a design system for this project.”"),
    ("claude-app", "Claude app", "Build the skill zip, then upload dist/opendesigner.zip under Customize > Skills. Code execution must be on.",
     "git clone https://github.com/ckryptickunal/OpenDesigner && cd OpenDesigner\npython3 tools/build_dist.py", "Then, in a chat: “Create a design system for my app.”"),
    ("agents", "Codex, Cursor, Copilot, Gemini CLI", "These tools read skills from .agents/skills/ in your project.",
     "git clone https://github.com/ckryptickunal/OpenDesigner\nmkdir -p your-project/.agents/skills\ncp -R OpenDesigner/.agents/skills/opendesigner* your-project/.agents/skills/",
     "Then ask your agent: “Create a design system for this project.”"),
    ("chatgpt", "ChatGPT", "No install: a Project with an instructions file and five knowledge files from chatgpt-project/ in the repository.",
     "1. Create a Project.\n2. Paste the part of chatgpt-project/instructions.md below its line into the Project instructions.\n3. Upload the five files in chatgpt-project/knowledge/.", "Then: “Create a design system for my app.”"),
    ("engine", "Engine only", "No AI needed: Python 3.10 or newer, and nothing else to install. The same answers give the same tokens and exports.",
     'git clone https://github.com/ckryptickunal/OpenDesigner\npython3 OpenDesigner/skills/opendesigner/scripts/engine.py sketch --name "Acme" --feel friendly,minimal\npython3 OpenDesigner/skills/opendesigner/scripts/engine.py build',
     "Then open opendesigner/overview.html.")]
STEPS = [
    ("It reads what you have", "It reads your CSS, Tailwind config, tokens, logo and fonts, and never asks what they already answer.",
     '<ul class="vg-files"><li><span class="mono">globals.css</span><span class="chip">colors</span></li><li><span class="mono">tailwind.config.ts</span><span class="chip">theme</span></li>'
     '<li><span class="mono">package.json</span><span class="chip">react</span></li><li><span class="mono">logo.svg</span><span class="chip">main color</span></li></ul>'),
    ("You answer up to five questions", "What you're making, who it's for, where it runs, how it should feel, and your brand color.",
     '<ol class="vg-qs"><li>What are you making?</li><li>Who is it for?</li><li>Where does it run?</li><li class="on">How should it feel?</li><li>A brand color or logo?</li></ol>'),
    ("It checks the rules, then saves them", "It checks contrast, target sizes, focus and motion, then saves the rules as files in your project.",
     '<pre class="code-lines vg-term"><span class="c">$</span> engine.py build\n<span class="ok">Passes: no errors.</span>\nChecked 164 color pairs in every mode,\n12 mode combinations and 427 tokens.</pre>'),
    ("Every new screen follows them", "Your AI reads DESIGN.md before changing the interface, and a review flags any value that drifted.",
     '<pre class="code-lines vg-term"><span class="c">$</span> engine.py review\ncard.css:1 <span class="bad">border-radius: 7px</span>\n→ use <span class="k">var(--ds-radius-container)</span></pre>')]
INSIDE = [  # (benefit title, what it does, vignette, column span)
    ("Nobody has to guess why", "Every value records how it was set and why. Locked values change only with the owner's yes.",
     '<div class="vg-log"><p class="mono">D-0056 · dials.roundness = 75</p><p><span class="chip accent">chosen</span> <span class="chip">supersedes D-0033</span></p><p class="vg-why">“Use iOS style rounded edges with iOS kerning everywhere instead of sharp corners.”</p></div>', 2),
    ("Readable for everyone", "WCAG 2.2 AA contrast, 24 px targets, focus rings and reduced motion: a floor, not a certificate.",
     '<div class="vg-floor"><span class="vg-aa">Aa</span><span class="num">4.5:1</span><span class="vg-target"></span><span class="num">24 px</span></div>', 1),
    ("Start from what you have", "Point it at a website, screenshot, Figma file or repo. It keeps the structure, never another brand's identity.",
     '<p class="vg-from"><span class="chip">Website</span><span class="chip">Screenshot</span><span class="chip">Figma file</span><span class="chip">Repository</span><span class="chip">Brand book</span></p>', 1),
    ("Your brand stays yours", "It asks you for the logo, photos, typeface and voice, and never fakes them.",
     '<p class="vg-from"><span class="tag-missing">Logo · Not enough information</span><span class="tag-missing">Voice guide · Not enough information</span></p>', 1),
    ("Ask for a look in plain words", "Glassmorphism, bento, risograph, Swiss: each style is named, shown and mapped to settings.",
     '<p class="a-tags"><span class="a-tag a-sty">Glassmorphism</span><span class="a-tag a-sty">Bento grid</span><span class="a-tag a-sty">Risograph</span><span class="a-tag a-sty">Swiss</span></p>', 1),
    ("Your work stays on your computer", "No account and no server. The engine is one Python file with no network calls.",
     '<pre class="code-lines vg-term"><span class="c">$</span> python3 engine.py --help\n<span class="c">… stdlib only, no network</span></pre>', 2)]
USES = [("Websites and landing pages", "One type scale, one spacing rhythm, one set of buttons. A new page looks like it was always there.", "/docs/quickstart/", "Your first design system"),
        ("Mobile and web apps", "One system exports to CSS, Tailwind, Swift and Jetpack Compose, so every platform shares one look.", "/docs/export/", "Export to code"),
        ("SaaS dashboards", "Compact rows, tabular numbers and hairline separators keep dense tables and forms easy to scan.", "/docs/engineers/", "For engineers"),
        ("Enterprise software", "A decision log, locked values and house standards. Every change records why it was made.", "/docs/enterprise/", "For design-system teams")]
CRAFT = [("motion", "Motion that feels right", "Easing, timing and where things enter from, shown live.", "craft-motion"),
         ("ux-patterns", "UX patterns, compared", "Side-by-side choices for toasts, drawers, errors and touch.", "craft-ux"),
         ("ui-details", "Interface details", "The small things that add up: radii, numbers, borders, focus.", "craft-ui"),
         ("resources", "Who we learn from", "The people and references behind the house standards.", "craft-res")]
HOME_FILES = [("DESIGN.md", "your rules in plain words"), ("opendesigner/tokens/", "the source, DTCG 2025.10"), ("build/css/, build/tailwind/", "CSS and Tailwind v4"),
              ("build/figma/", "Figma variables"), ("build/swift/, build/compose/", "iOS and Android")]
EXPORTS = ["CSS variables", "Tailwind v4", "Figma variables", "Swift", "Jetpack Compose", "DTCG 2025.10", "Paper"]


def contrast(a, b):
    def lum(h):
        r, g, b_ = (int(h.lstrip("#")[i:i + 2], 16) / 255 for i in (0, 2, 4))
        f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
        return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b_)
    hi, lo = sorted((lum(a), lum(b)), reverse=True)
    return round((hi + 0.05) / (lo + 0.05), 2)


def demo_panel(ex, i):
    t, ui = ex["tokens"], DEMO_UI[ex["key"]]
    style = ";".join(f"--x-{k}:{t[v]}" for k, v in (("bg", "bg"), ("raised", "raised"), ("sunken", "sunken"), ("text", "text"), ("muted", "muted"), ("border", "border"),
                                                      ("sep", "sep"), ("primary", "primary"), ("on", "onPrimary"), ("soft", "accentSoft"), ("soft-text", "accentText"),
                                                      ("r", "rControl"), ("rc", "rContainer"), ("h", "hControl"), ("body", "body"), ("label", "label"),
                                                      ("title", "title"), ("headline", "headline"), ("wh", "wHeading"), ("inset", "inset")))
    answers = [("Making", ex["making"]), ("Who", ex["who"]), ("Where", ex["where"]), ("Feel", ex["feel"]),
               ("Brand color", f'<span class="hh-sw" style="background:{ex["brand"]}"></span><span class="mono">{ex["brand"]}</span>')]
    field = ""
    if ui.get("field"):
        lab, val, hint = ui["field"]
        field = f'<label class="x-field"><span>{lab}</span><span class="x-input">{val}</span><span class="x-hint">{hint}</span></label>'
    big = f'<p class="x-big num">{ui["big"]}</p>' if ui["big"] else ""
    calls = (f'<span class="a-call a-call-top" aria-hidden="true">radius.container <b>{t["rContainer"]}</b></span>'
             f'<span class="a-dim" aria-hidden="true"><span>{t["hControl"].replace("px", "")}</span></span>'
             f'<span class="a-call a-call-bot" aria-hidden="true">size.control <b>{t["hControl"]}</b> · radius.control <b>{t["rControl"]}</b></span>')
    card = (f'<div class="x-card" style="{style}">{calls}<div class="x-head"><span class="x-title">{ui["title"]}</span><span class="x-chip">{ui["chip"]}</span></div>'
            f'<p class="x-sub">{ui["sub"]}</p>{big}{field}<div class="x-rows">' + "".join(f'<div><span>{a}</span><span class="num">{b}</span></div>' for a, b in ui["rows"])
            + f'</div><div class="x-actions"><span class="x-btn">{ui["secondary"]}</span><span class="x-btn primary">{ui["primary"]}</span></div></div>')
    kept = (f'Your color stays exact on buttons: white text on <span class="mono">{t["primary"]}</span> reads at <span class="num">{t["cPrimary"]}:1</span>.' if t["brandKept"] else
            f'<span class="mono">{ex["brand"]}</span> stays your brand color, but white text on it reads at only <span class="num">{t["cBrandWhite"]}:1</span>, and the system\'s dark text at <span class="num">{contrast(ex["brand"], t["text"])}:1</span>. '
            f'So buttons use <span class="mono">{t["primary"]}</span>, which reads at <span class="num">{t["cPrimary"]}:1</span>.')
    values = [("Corners", f'{t["rControl"]} controls, {t["rContainer"]} cards'), ("Control height", t["hControl"]), ("Body text", t["body"]),
              ("Type scale ratio", f'{t["ratio"]}'), ("Heading weight", t["wHeading"])]
    return (f'<div class="demo-panel" role="tabpanel" tabindex="0" id="demo-{ex["key"]}" aria-labelledby="demo-tab-{ex["key"]}">'
            f'<div class="demo-answers"><p class="kicker">The five answers</p><dl>' + "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in answers) + "</dl>"
            f'<p class="kicker">What the engine wrote</p><dl class="demo-values">' + "".join(f'<div><dt>{a}</dt><dd class="num">{b}</dd></div>' for a, b in values) + "</dl>"
            f'<p class="demo-note">{kept}</p></div>'
            f'<div class="demo-stage" style="background-image:url(https://images.unsplash.com/{SCENES["blue-soft"][0]}?auto=format&fit=crop&w=1200&q=70)">{card}</div></div>')


def install_tabs():
    tabs = "".join(f'<button type="button" role="tab" id="inst-tab-{k}" aria-controls="inst-{k}" aria-selected="{"true" if i == 0 else "false"}">{"".join(logo(m, 16) for m in INSTALL_MARKS[k])}{esc(label)}</button>'
                   for i, (k, label, _d, _c, _t) in enumerate(INSTALL))
    panels = "".join(f'<div class="inst-panel" role="tabpanel" tabindex="0" id="inst-{k}" aria-labelledby="inst-tab-{k}"><p>{esc(d)}</p>'
                     f'<div class="code"><button class="copy" type="button" data-copy>Copy</button><pre><code>{code_html(esc(c))}</code></pre></div><p class="inst-then">{esc(then)}</p></div>'
                     for k, _label, d, c, then in INSTALL)
    return f'<div class="tabs" data-tabs><div class="tablist" role="tablist" aria-label="Your AI tool">{tabs}</div>{panels}</div>'


def evals_block(name):
    import evals_html
    return evals_html.block(name)


def home(pages, facts, faq):
    pieces = [p for p in show_pieces() if p["cat"] == "product"][:6]
    total = len(show_pieces())
    demo_tabs = "".join(f'<button type="button" role="tab" id="demo-tab-{e["key"]}" aria-controls="demo-{e["key"]}" aria-selected="{"true" if i == 0 else "false"}">'
                        f'<strong>{e["name"]}</strong><span>{esc(e["making"])}</span></button>' for i, e in enumerate(DEMO["examples"]))
    picks = [("product--02-fennick-approvals", "sky-trees", "big"), ("product--04-sounding-observability", "woods-sage", ""), ("product--06-ferrule-security", "forest", "")]
    byk = {p["key"]: p for p in show_pieces()}
    screens, credits = [], []
    for key, scene, size in picks:
        pc = byk[key]
        img = (f'<img src="/img/show/{key}-1800.webp" srcset="/img/show/{key}.webp 900w, /img/show/{key}-1800.webp 1800w" '
               f'sizes="{"(max-width: 900px) 100vw, 1150px" if size else "(max-width: 900px) 100vw, 570px"}" width="1800" height="1125" loading="lazy" alt="{esc(pc["title"])}">')
        st, cr = stage(scene, img)
        credits.append(cr)
        name, what = pc["title"].split(" · ")[-1], pc["title"].split(" · ")[1]
        screens.append(f'<figure class="screen {size}">{st}<figcaption><strong>{esc(name)}</strong><span>{esc(what)}</span></figcaption></figure>')
    screens_html, screen_credits = "".join(screens), ", ".join(dict.fromkeys(credits))
    examples = "".join(f'<a class="ex" href="/showcase/#product"><span class="ex-img"><img src="/img/show/{p["key"]}.webp" width="900" height="563" loading="lazy" alt="{esc(p["title"])}"></span>'
                       f'<span class="ex-cap"><strong>{esc(p["title"].split(" · ")[-1])}</strong><span>{esc(p["title"].split(" · ")[1] if p["title"].count(" · ") >= 2 else "")}</span></span></a>' for p in pieces)
    faq_html = "".join(f'<details class="qa"><summary><h3>{esc(q)}</h3></summary><div class="ans">{md_to_html(a)}</div></details>' for q, a in faq[:4])
    pid, author, page_id = SCENES["blue-waves"]
    cta_bg = f"background-image:url(https://images.unsplash.com/{pid}?auto=format&fit=crop&w=1600&q=70)"
    ba_html, ba_credit = before_after()
    craft = [c for c in CRAFT if any(p["slug"] == c[0] for p in pages)]
    craft_html = "".join(f'<a class="craft-card {v}" href="/docs/{s}/"><span class="vg" aria-hidden="true"><i></i><i></i><i></i></span><h3>{t}</h3><p>{d}</p><span class="more">Open the guide {CHEVRON}</span></a>' for s, t, d, v in craft)
    craft_sec = f"""
<section class="h-sec" id="craft">
<div class="h-head">{idx("08", "Learn the craft")}<h2 class="h-h2">A field guide to interfaces that feel right.</h2>
<p class="h-lede">The rules come from people who build loved interfaces, such as Emil Kowalski. See each one live, with its source.</p></div>
<div class="craft">{craft_html}</div>
</section>
""" if craft else ""
    news = ("#before-after", "New: the audit, drawn on your own page")
    announce = (f'<p class="h-announce"><span class="h-pill-tag">Free and open source · MIT</span>'
                f'<a href="{news[0]}">{news[1]} {ARROW}</a></p>')
    body = f"""
<section class="h-hero">
{announce}
<h1 class="h-title g-wait"><span class="h-eyebrow">Design systems for AI coding tools</span> Make everything you build <strong>look like it belongs together.</strong></h1>
<p class="h-lede">Your AI tools know what to build. OpenDesigner tells them how it should look: a design system, one set of rules that every new screen follows, and that it updates when you change your mind.</p>
<div class="h-cta"><a class="btn primary lg" href="#install">Get started free</a><a class="h-link" href="#before-after">See it in action {ARROW}</a></div>
<div class="h-cmd-wrap"><p class="h-cmd-label">Two commands in Claude Code, then a few plain questions</p>
<div class="cmd h-cmd"><code>/plugin marketplace add ckryptickunal/OpenDesigner</code><button class="copy" type="button" data-copy-text="/plugin marketplace add ckryptickunal/OpenDesigner
/plugin install opendesigner@opendesigner">Copy both</button></div></div>
{figure("home-hero")}
<div class="h-works"><p class="kicker">Works in the AI tool you already use</p><ul class="hosts">{"".join(f'<li><span class="host-tile">{logo(k, 22)}</span><span>{n}</span></li>' for n, k in HOSTS)}</ul></div>
</section>

<section class="h-sec" id="before-after">
<div class="h-head">{idx("01", "On a page you already built")}<h2 class="h-h2">See what's wrong, then see it fixed.</h2>
<p class="h-lede">Point OpenDesigner at a page you have. It measures the page, marks each problem on it, and fixes it with your own design system. Every fix says what it makes better.</p></div>
{ba_html}
<p class="h-fine">Real output from the review skill on an invented invoicing app. Both pages are live HTML, not pictures: probe.js measured them before and after, and each box is measured on the page as drawn. Laid out at 1200 px and scaled to fit. Photo: {ba_credit} on Unsplash. <a href="/demo/before-after/">Open the full report</a> · <a href="{GH}/tree/main/site/demo/before-after">How it was made</a></p>
</section>

<section class="h-sec" id="why">
<div class="h-head">{idx("02", "The problem")}<h2 class="h-h2">Every new screen drifts a little.</h2>
<p class="h-lede">One page gets rounded buttons, the next gets square ones, and a new blue appears. People notice: they judge how a page looks in 17 to 50 milliseconds, and simple, familiar screens are the ones they rate most appealing (<a href="{GH}/blob/main/research/L15-visual-design-principles.md">research</a>).</p></div>
{figure("design-systems-one-source")}
</section>

<section class="h-sec" id="fix">
<div class="h-head">{idx("03", "The fix")}<h2 class="h-h2">One set of rules that every screen follows.</h2>
<p class="h-lede">OpenDesigner turns a few plain answers into rules for color, type, spacing, corners and motion. Here are three products, each made from five answers.</p></div>
<div class="tabs demo" data-tabs><div class="tablist demo-tabs" role="tablist" aria-label="Example products">{demo_tabs}</div>
{"".join(demo_panel(e, i) for i, e in enumerate(DEMO["examples"]))}</div>
<p class="h-fine">Real engine output (<a href="{GH}/blob/main/site/demo_systems.py">site/demo_systems.py</a>), nothing tuned by hand. Each system also has dark mode, three densities and reduced motion. Photo: <a href="https://unsplash.com/photos/{SCENES["blue-soft"][2]}">{SCENES["blue-soft"][1]}</a> on Unsplash.</p>
</section>

<section class="h-sec" id="screens">
<div class="h-head h-head-row"><div>{idx("04", "Real screens")}<h2 class="h-h2">What consistent looks like.</h2>
<p class="h-lede">B2B screens built by AI agents through OpenDesigner and reviewed by the maintainer. Every brand is invented, and much of the identity work was done outside the tokens.</p></div>
<a class="h-link" href="/showcase/">See all {total} designs {ARROW}</a></div>
<div class="screens">{screens_html}</div>
<p class="h-fine">Photos: {screen_credits} on Unsplash.</p>
</section>

<section class="h-sec" id="how">
<div class="h-head">{idx("05", "How it works")}<h2 class="h-h2">Five answers today. Consistent screens from then on.</h2></div>
<ol class="h-steps">{"".join(f'<li class="h-step">{A_PICTS[i]}<span class="h-n num">0{i + 1}</span><h3>{t}</h3><p>{d}</p><div class="vg">{v}</div></li>' for i, (t, d, v) in enumerate(STEPS))}</ol>
</section>

<section class="h-sec" id="use-cases">
<div class="h-head">{idx("06", "What you can build")}<h2 class="h-h2">Websites, apps, dashboards and enterprise software.</h2></div>
<div class="who">{"".join(f'<a class="who-card" href="{u}"><h3>{t}</h3><p>{d}</p><span class="more">{l} {CHEVRON}</span></a>' for t, d, u, l in USES)}</div>
</section>

<section class="h-sec" id="features">
<div class="h-head">{idx("07", "Why it stays consistent")}<h2 class="h-h2">Built to keep your product together, not just to start it.</h2></div>
<div class="bento">{"".join(f'<article class="bento-card span-{sp}"><h3>{t}</h3><p>{d}</p><div class="vg">{v}</div></article>' for t, d, v, sp in INSIDE)}</div>
<div class="h-split h-files">
<div><h3 class="h-h3">Rules your code and your design tools can read</h3>
<p class="h-lede">The same answers always give the same tokens and exports, for your code, Figma and your next AI session.</p>
<ul class="tree">{"".join(f'<li><code>{f}</code><span>{w}</span></li>' for f, w in HOME_FILES)}</ul></div>
{overview_shot()}
</div>
</section>
{craft_sec}
<section class="h-sec" id="install">
<div class="h-head">{idx("09", "Get started")}<h2 class="h-h2">Add it to the AI tool you already use.</h2>
<p class="h-lede">You need your own AI tool. Claude Code, the Claude app and other agents also need Python 3.10 or newer; ChatGPT needs nothing installed.</p></div>
{install_tabs()}
</section>

<section class="h-sec" id="evals">
<div class="h-head">{idx("10", "Tested in the open")}<h2 class="h-h2">We test it on itself, and publish the numbers.</h2>
<p class="h-lede">AI agents do real tasks with and without OpenDesigner. The engine builds systems from 18 fixed briefs. Our own checkers face pages with planted mistakes. When a test fails, the page says so.</p></div>
{evals_block("summary")}
<p class="h-more"><a class="h-link" href="/docs/evals/">See every test, and run them yourself {ARROW}</a></p>
</section>

<section class="h-sec" id="status">
<div class="h-split">
<div><p class="kicker">Status</p><h2 class="h-h2">Early, and honest about it.</h2>
<ul class="status">{"".join(f"<li>{x}</li>" for x in HOME_STATUS)}</ul>
<p class="h-lede">The most useful help right now: try it on a real project and tell us where it breaks.</p>
<p class="h-contrib"><span class="kicker">Contribute</span><a href="/docs/contribute/">How to contribute</a><a href="{GH}/issues?q=is%3Aopen+label%3A%22good+first+issue%22">Good first issues</a><a href="{GH}/issues/new/choose">Report a problem</a></p>
<p class="h-more"><a class="h-link" href="/changelog/">Version {VERSION}: see every change {ARROW}</a></p></div>
{gh_card(facts)}
</div>
</section>

<section class="h-sec" id="talk">
<div class="h-book">
<div><p class="kicker">Talk it through</p><h2 class="h-h2">Work through your design with {CONFIG["HOST_NAME"]}.</h2>
<p class="h-lede">A free {CONFIG["BOOKING_FREE_MINUTES"]}-minute call with {CONFIG["HOST_NAME"]}, {CONFIG["HOST_ROLE"]}, to see whether it fits your product and where to start. OpenDesigner stays free; you never need a call to use it.</p></div>
<div class="h-book-act">{book_link("Book a free " + str(CONFIG["BOOKING_FREE_MINUTES"]) + "-minute call", primary=True)}<a class="h-link" href="/book/">What the call covers {ARROW}</a></div>
</div>
</section>

<section class="h-sec" id="faq">
<div class="h-head h-head-row"><div><p class="kicker">FAQ</p><h2 class="h-h2">Questions</h2></div><a class="more" href="/docs/faq/">All questions {CHEVRON}</a></div>
<div class="faq">{faq_html}</div>
</section>

<section class="h-end">
<div class="h-end-photo" style="{cta_bg}">
<div class="h-end-card">
<p class="kicker">Try it</p>
<h2 class="h-h2">Make your next feature feel like it was always there.</h2>
<p class="h-end-lede">One set of rules, and every screen after that follows it.</p>
<div class="h-cta"><a class="btn primary lg" href="/docs/install/">Get started free</a>{book_link("Or book a free " + str(CONFIG["BOOKING_FREE_MINUTES"]) + "-minute call")}</div>
</div>
</div>
<p class="h-credit">Photo: <a href="https://unsplash.com/photos/{page_id}">{esc(author)}</a> on Unsplash</p>
</section>
"""
    ld = [{"@context": "https://schema.org", "@type": "SoftwareApplication", "name": NAME, "url": SITE_URL + "/", "description": ONE_LINER,
           "applicationCategory": "DeveloperApplication", "applicationSubCategory": "Design system generator", "operatingSystem": "macOS, Windows, Linux",
           "isAccessibleForFree": True, "license": f"{GH}/blob/main/LICENSE", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
           "image": f"{SITE_URL}/og/home.jpg", "downloadUrl": GH, "softwareHelp": f"{SITE_URL}/docs/", "sameAs": [GH],
           "author": {"@type": "Person", "name": "ckryptickunal", "url": "https://github.com/ckryptickunal"}},
          {"@context": "https://schema.org", "@type": "SoftwareSourceCode", "name": NAME, "codeRepository": GH, "programmingLanguage": ["Python", "Markdown"],
           "license": "https://opensource.org/license/mit", "dateModified": facts["pushed"]},
          {"@context": "https://schema.org", "@type": "Organization", "@id": SITE_URL + "/#org", "name": NAME, "url": SITE_URL + "/",
           "logo": {"@type": "ImageObject", "url": f"{SITE_URL}/apple-touch-icon.png"}, "description": ONE_LINER, "sameAs": [GH]},
          {"@context": "https://schema.org", "@type": "WebSite", "name": NAME, "url": SITE_URL + "/", "description": ONE_LINER, "inLanguage": "en",
           "publisher": {"@id": SITE_URL + "/#org"}},
          {"@context": "https://schema.org", "@type": "HowTo", "name": "Make a design system with OpenDesigner in Claude Code", "step": [
              {"@type": "HowToStep", "text": "/plugin marketplace add ckryptickunal/OpenDesigner"},
              {"@type": "HowToStep", "text": "/plugin install opendesigner@opendesigner"},
              {"@type": "HowToStep", "text": "Say: Create a design system for this project. Answer up to five questions."}]}]
    hero = f'<link rel="preload" as="image" href="{scene_url("blue-gradient")}" fetchpriority="high">\n'  # the phone LCP: a background, found late
    return shell("/", "OpenDesigner: design systems for the AI tool you already use", HOME_DESCRIPTION, body, pages, ld, home=True, preload=hero)


HOME_DESCRIPTION = ("Make everything you build look like it belongs together. Free skills turn your design rules into tokens, CSS, Tailwind "
                    "and DESIGN.md that your AI follows.")

# ---------------------------------------------------------------- docs pages, docs index, showcase, 404
def faq_items(body):
    return [(q.strip(), a.strip()) for q, a in re.findall(r"^### (.+?)\n(.+?)(?=\n### |\Z)", body, re.S | re.M)]


def doc_page(p, pages):
    if p["slug"] == "changelog":
        return changelog_page(p, pages)
    toc = []
    if p["slug"] == "faq":
        items = faq_items(p["body"])
        intro = p["body"].split("\n### ", 1)[0] if not p["body"].startswith("### ") else ""
        content = md_to_html(intro) + "".join(
            f'<details class="qa" id="{slugify(q)}"><summary><h2>{esc(q)}</h2></summary><div class="ans">{md_to_html(a)}</div></details>' for q, a in items)
    else:
        content = md_to_html(p["body"], toc)
    docs = [x for x in pages if x["section"] in SECTIONS]
    idx = docs.index(p)
    prev_, next_ = (docs[idx - 1] if idx > 0 else None), (docs[idx + 1] if idx + 1 < len(docs) else None)
    pn = ('<nav class="prevnext" aria-label="Previous and next">'
          + (f'<a class="prev" href="{prev_["path"]}"><span>Previous</span>{esc(prev_["title"])}</a>' if prev_ else "<span></span>")
          + (f'<a class="next" href="{next_["path"]}"><span>Next</span>{esc(next_["title"])}</a>' if next_ else "") + "</nav>")
    toc_html = ('<nav class="toc" aria-label="On this page"><h2 class="side-h kicker">On this page</h2><ul>' + "".join(f'<li><a href="#{a}">{esc(t)}</a></li>' for a, t in toc) + "</ul></nav>") if len(toc) > 1 else ""
    crumb = (f'<nav class="crumb" aria-label="Breadcrumb"><a href="/docs/">Docs</a><span aria-hidden="true">/</span><span>{p["section"]}</span>'
             + (f'<span aria-hidden="true">/</span><span aria-current="page">{esc(p["title"])}</span>' if p["slug"] != "index" else "") + "</nav>")
    edit = f'{GH}/edit/main/site/docs/{p["slug"]}.md'
    same = [x for x in pages if x["section"] == p["section"]]
    pos = same.index(p) + 1
    kind = {"Getting started": "lime", "Guides": "", "Concepts": "sky", "Craft": "pink", "Reference": "paper"}.get(p["section"], "paper")
    icon = {"Getting started": "play", "Guides": "compass", "Concepts": "bulb", "Craft": "brush", "Reference": "book"}.get(p["section"], "tag")
    main_html = (f'<div class="doc-grid"><article class="doc">{crumb}<p class="doc-stickers a-doc"><span class="a-card"><span class="a-card-k">{esc(p["section"])}</span><span class="a-card-n">{pos:02d}<small>/{len(same):02d}</small></span></span></p><h1 class="t-h1">{esc(p["title"]).replace("-", NBH)}</h1>'
                 f'<p class="meta">Updated <time datetime="{p.get("updated", TODAY)}">{p.get("updated", TODAY)}</time> · <a href="{edit}">Suggest a change</a></p>'
                 f'<div class="prose">{content}</div>{pn}</article>{toc_html}</div>')
    ld = [crumbs_ld([("Docs", "/docs/")] + ([] if p["slug"] == "index" else [(p["title"], p["path"])])),
          {"@context": "https://schema.org", "@type": "Article" if p["slug"] == "design-systems" else "TechArticle", "headline": p["title"],
           "description": p["description"], "url": SITE_URL + p["path"], "datePublished": "2026-10-14", "dateModified": p.get("updated", TODAY),
           "inLanguage": "en", "image": f"{SITE_URL}/og/{'docs/' + p['slug'] if (CACHE / 'og' / 'docs' / (p['slug'] + '.jpg')).exists() else 'home'}.jpg",
           "mainEntityOfPage": SITE_URL + p["path"],
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
    card = (CACHE / "og" / "docs" / f'{p["slug"]}.jpg').exists()  # og_images() draws one for every page; without it, the home card
    og = f'/og/docs/{p["slug"]}.jpg' if card else "/og/home.jpg"
    return shell(p["path"], p["seo_title"], p["description"], main_html, pages, ld, og=og,
                 og_alt=f'{p["title"]}: a page of the OpenDesigner docs' if card else None, preload=FEED_LINK if p["slug"] == "changelog" else "")


def highlight_entries():
    """CHANGELOG.md's highlights as entries for the changelog page: title, explanation and details, the kind of change
    (its "### Added/Changed/Fixed" heading) and the day git says the entry was written, newest first."""
    import datetime as _dt
    entries, section, ts, when, cur = [], "", 0, None, None
    for line in git_out("blame", "--line-porcelain", "CHANGELOG.md").splitlines():
        if line.startswith("committer-time "):
            ts = int(line.split()[1])
        elif line.startswith("committer-tz "):
            z = line.split()[1]
            tz = _dt.timezone((-1 if z[0] == "-" else 1) * _dt.timedelta(hours=int(z[1:3]), minutes=int(z[3:5])))
            when = _dt.datetime.fromtimestamp(ts, tz).date().isoformat()
        elif line.startswith("\t"):
            text = line[1:]
            m = re.match(r"^- \*\*(.+?)\*\*(.*)$", text)
            if text.startswith("#") or (text.startswith("- ") and not m):
                cur = None
                if text.startswith("### "):
                    section = text[4:].strip()
            if m and when:
                cur = {"ts": ts, "day": when, "title": m.group(1).strip().rstrip(".:"), "rest": m.group(2), "more": [], "kind": section}
                entries.append(cur)
            elif cur and text.startswith("  "):
                cur["more"].append(text[2:])
    entries.sort(key=lambda e: e["ts"], reverse=True)
    return entries


def _entry_html(e):
    """One highlight: its explanation without the note on who asked and when, and any sub-points folded under Details."""
    gh = lambda md: re.sub(r"\]\((?!https?:|#|/|mailto:)([^)]+)\)", lambda m: f"]({GH}/blob/main/{m.group(1)})", md)
    rest = re.sub(r"^\s*\([^()]*(?:\([^()]*\)[^()]*)*\)", "", e["rest"]).lstrip(" .:").strip()
    if re.match(r"^ [a-z]", e["rest"]):  # "**The demo's page is rebuilt** that the owner picked": the bold words start the sentence
        rest = e["title"] + " " + rest
    more = md_to_html(gh("\n".join(e["more"]))) if e["more"] else ""
    body = md_to_html(gh(rest)) if rest else ""
    if body and more:
        more = f'<details class="cl-more"><summary>Details</summary>{more}</details>'
    tag = '<span class="cl-tag">Fix</span>' if e["kind"] == "Fixed" else ""
    return f'<article class="cl-entry"><div class="cl-title"><h3>{inline(e["title"])}</h3>{tag}</div><div class="prose cl-body">{body}{more}</div></article>'


def changelog_page(p, pages):
    """The changelog as its own page, not a docs page: no docs menu, breadcrumb or page index. One column of days, newest
    first. Each day shows its highlights from CHANGELOG.md in full, with that day's commits folded underneath."""
    v = version_facts()
    by_day, entries = changes_by_day(), highlight_entries()
    days = sorted(set(by_day) | {e["day"] for e in entries}, reverse=True)
    shown = days[:60]
    state = f'Released {day_name(v["released"])}' if v["released"] else "In development"
    blocks = []
    for d in shown:
        mine = [e for e in entries if e["day"] == d]
        commits = by_day.get(d, [])
        log = ""
        if commits:
            n = len(commits)
            log = (f'<details class="cl-log"{"" if mine else " open"}><summary>{n} change{"s" if n != 1 else ""} to the repository</summary><ul>'
                   + "".join(f'<li>{inline(sub)} <a class="cl-sha" href="{GH}/commit/{h}">{h[:7]}</a></li>' for h, sub in commits) + "</ul></details>")
        dt_ = dt.date.fromisoformat(d)
        blocks.append(f'<section class="cl-day" id="{slugify(day_name(d))}" aria-labelledby="d-{d}"><h2 class="cl-date" id="d-{d}">'
                      f'<time datetime="{d}">{dt_.day} {dt_.strftime("%b")} {dt_.year}</time></h2>'
                      f'<div class="cl-items">{"".join(_entry_html(e) for e in mine)}{log}</div></section>')
    older = (f'<p class="cl-older">Older changes are in <a href="{GH}/commits/main">the full history on GitHub</a>.</p>' if len(days) > len(shown) else "")
    update = md_to_html(update_md())
    head = (f'<header class="cl-head"><h1 class="t-h1">Changelog</h1>'
            f'<p class="cl-lede">What changed in OpenDesigner, newest first, built from the repository each time the site is published.</p>'
            f'<p class="cl-facts"><span class="cl-ver">v{v["version"]}</span><span>{state}</span>'
            f'<span>Latest change <time datetime="{v["latest_change"]}">{day_name(v["latest_change"])}</time></span></p>'
            f'<p class="cl-links"><a href="/changelog.xml">Atom feed</a><a href="/version.json">version.json</a>'
            f'<a href="{GH}/blob/main/CHANGELOG.md">CHANGELOG.md</a><a href="{GH}/commits/main">Every commit</a></p>'
            f'<details class="cl-update"><summary>Check your version and update</summary><div class="prose">{update}</div></details></header>')
    main_html = f'<div class="cl-wrap">{head}<div class="cl-feed">{"".join(blocks)}</div>{older}</div>'
    ld = [{"@context": "https://schema.org", "@type": "TechArticle", "headline": p["title"], "description": p["description"], "url": SITE_URL + p["path"],
           "datePublished": "2026-10-14", "dateModified": p.get("updated", TODAY), "inLanguage": "en", "mainEntityOfPage": SITE_URL + p["path"],
           "author": {"@type": "Person", "name": "ckryptickunal", "url": "https://github.com/ckryptickunal"},
           "publisher": {"@type": "Organization", "name": NAME, "url": SITE_URL + "/", "logo": {"@type": "ImageObject", "url": f"{SITE_URL}/apple-touch-icon.png"}}}]
    card = (CACHE / "og" / "docs" / f'{p["slug"]}.jpg').exists()
    return shell(p["path"], p["seo_title"], p["description"], main_html, pages, ld, og=f'/og/docs/{p["slug"]}.jpg' if card else "/og/home.jpg",
                 og_alt=f'{p["title"]}: OpenDesigner' if card else None, preload=FEED_LINK, home="cl-page")


SHOW_INTRO = ("AI builder agents made every piece here through the whole OpenDesigner process: real references on Mobbin, a design system from the "
              "engine for each piece, the build, then checks. Every brand is invented. Each piece was then audited against shipped products and reviewed by "
              "the maintainer. The pieces called ugly were removed or rebuilt, and the ones marked Being rebuilt are next.")
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
CATS = [("product", "B2B product screens"), ("styles", "Style studies"), ("heroes", "Hero sections"), ("components", "Web components"), ("app-screens", "App screens"), ("watch", "Watch screens"),
        ("footers", "Footer sections"), ("mockups", "Mockups")]
CAT_FRAMES = {"product": "16 / 10", "styles": "16 / 10", "heroes": "16 / 10", "components": "16 / 10", "footers": "16 / 8", "mockups": "4 / 3", "app-screens": "9 / 19.5", "watch": "615 / 753"}
THUMB_W, FULL_W = 900, 1800
AUDIT = BRAND / "showcase" / "audit"
_order = BRAND / "showcase" / "order.json"
ORDER = {"scores": {}, "order": [], "category_order": [], **(json.loads(_order.read_text()) if _order.exists() else {})}
# Words in the audit's "industry" field that mean the product is sold to businesses.
B2B_WORDS = ("b2b", "saas", "enterprise", "payments", "billing", "spend", "accounts", "crm", "sales", "observability", "monitoring", "cloud", "security",
             "devops", "incident", "on-call", "people ops", "hr ", "facilit", "building management", "post-production", "event", "data", "etl", "pipeline",
             "support", "ai eval", "database", "live-ops", "live ops", "analytics", "developer", "devtools", "logistics", "clinical", "hospital")
# Industries sold to businesses (the audit's "industry" field); everything else is shown as consumer.
B2B_INDUSTRIES = {"healthcare", "design tools", "software", "writing tools", "team chat", "logistics", "research", "devtools", "developer tools",
                  "cloud security", "ai research", "productivity", "print", "fintech b2b", "analytics", "hr", "sales", "finance", "security", "infrastructure"}


def piece_text(d):
    title, text = d.name.split("-", 1)[1].replace("-", " ").capitalize(), ""
    notes = d / "notes.md"
    if notes.exists():
        lines = notes.read_text().splitlines()
        title = next((ln[2:].strip() for ln in lines if ln.startswith("# ")), title)
        title = re.sub(r":\s*notes$", "", title)
        title = re.sub(r"^\d{1,2}\s*[·.:–-]?\s+(?=\D)", "", title)  # "01 · Payments table": the number adds nothing in a gallery
        body = [ln.strip() for ln in lines if ln.strip() and not ln.startswith(("#", "|", "-", ">", "!", "```"))
                and not re.search(r"(shot\.png|index\.html|^Render|^Final render|renders?,? each|^Page|^Status|^Built by|scale 2|\d+ ?[×x] ?\d+ at"
                                  r"|\b[\w-]+/[\w./-]+\.(?:html|png|json|md|css|py)\b|\bbrand/|\bsite/|\bengine\.py\b)", ln.strip(), re.I)]
        if d.name in MOCKUP_CAPTIONS:
            body = [MOCKUP_CAPTIONS[d.name]]
        caption = next((ln.split(":", 1)[1].strip() for ln in lines if ln.startswith("Gallery:")), "")
        if caption:  # a rebuilt piece says what it is now in one line; its first paragraph may describe the design it replaced
            body = [caption]
        if body:
            text = re.sub(r"^(Direction|Brief|Concept)[.:]\s*", "", re.sub(r"[*_`]", "", body[0]))
            sentences = re.split(r"(?<=[.!?])\s+", text)
            text = sentences[0]
            if len(sentences) > 1 and len(text) + len(sentences[1]) < 150:
                text += " " + sentences[1]
            text = text if len(text) < 170 else text[:167].rsplit(" ", 1)[0] + "…"
    return title, text


# Gallery titles read "Brand · what it is" (owner, 2026-10-15: the gallery looked cluttered; the audit found device specs, old
# brand names and four title formats). The kind is fixed per folder; the brand comes from the page's own <title>, so a rename
# in the piece shows here without an edit.
KIND = {
    "product": {"01": "Payments table", "02": "Bill approvals", "03": "Company record", "04": "Service overview", "05": "Usage and billing", "06": "Security settings and audit log"},
    "heroes": {"01": "Architecture studio", "02": "Developer tool", "03": "Wellness", "07": "Ocean observatory", "08": "Retro-future hardware", "11": "Spend management",
               "12": "API monitoring", "13": "Security and access", "14": "Bill approvals"},
    "components": {"01": "Pricing table", "02": "Command palette", "03": "Date range picker", "04": "File upload", "05": "Toast stack", "06": "Data table",
                   "07": "AI composer", "08": "Music player", "09": "Onboarding stepper", "10": "Settings"},
    "footers": {"01": "Wordmark footer", "02": "Enterprise footer", "03": "Horizon footer", "04": "Illustrated footer", "05": "Magazine footer", "06": "Brutalist footer",
                "07": "Tea house footer", "08": "App footer", "09": "Data platform footer"},
    "styles": {"01": "Glassmorphism", "02": "Neumorphism", "03": "Claymorphism", "04": "Skeuomorphism", "05": "Comic", "06": "Memphis", "07": "Risograph",
               "08": "Bauhaus", "09": "Bento grid", "10": "Mesh gradient", "11": "Terminal", "12": "Pixel art"},
    "app-screens": {"01": "Private banking", "02": "Sleep story", "03": "Recipe", "04": "Live workout", "05": "Boarding pass", "06": "Plant care", "07": "Language lesson",
                    "08": "Podcast player", "09": "Project roadmap", "10": "Ward vitals", "11": "Purchase approval"},
    "watch": {"01": "Trail run", "02": "Heart-rate zones", "03": "Tide face", "04": "Transit", "05": "Home scenes", "06": "Breathe", "07": "Sailing", "08": "Focus timer", "09": "On-call page"},
}
BRAND_SHORT = {"Isobath Ocean Observatory": "Isobath", "Fenmoor STEM-8 Post Console": "Fenmoor", "Sasame Tea House": "Sasame", "Brask Studio": "Brask",
               "Margin command palette": "Margin", "Nightjar Engineering": "Nightjar", "Lullwort Sleep Teas": "Lullwort", "Orbika SR-1": "Orbika"}


def gallery_title(cat, d, fallback):
    kind = KIND.get(cat, {}).get(d.name[:2])
    page = d / "index.html"
    m = re.search(r"<title>([^<]+)</title>", page.read_text(errors="ignore")) if kind and page.exists() else None
    if not m:
        return fallback
    t = html.unescape(m.group(1)).strip()
    parts = [x.strip() for x in re.split(r":| · | — | – | \| ", t) if x.strip()]
    brand = parts[-1] if cat == "product" or re.match(r"Q\d", parts[0]) else parts[0]
    brand = re.sub(r"\s+(footer|annual report.*)$|\(\d\)$", "", brand).strip()
    return f"{BRAND_SHORT.get(brand, brand)} · {kind}"


def show_pieces():
    """Every showcase piece with its render, its notes and, when the Mobbin audit has run, its tags and verdict."""
    from PIL import Image
    out = []
    for cat, label in CATS:
        folder = BRAND / "showcase" / cat
        if not folder.exists():
            continue
        for d in sorted(x for x in folder.iterdir() if x.is_dir()):
            notes_file = d / "notes.md"
            if notes_file.exists() and "Replaced on 2026-10-14 by" in notes_file.read_text():
                continue  # rebuilt after the Mobbin audit; the original stays in the repo
            shot, thumb = d / "shot.png", BRAND / "showcase" / "_thumbs" / f"{cat}--{d.name}--shot.jpg"
            src = shot if shot.exists() else (thumb if thumb.exists() else None)
            if not src:
                continue
            with Image.open(src) as im:
                w, h = im.size
            title, blurb = piece_text(d)
            title = gallery_title(cat, d, title)
            meta = {"tags": [], "styles": [], "verdict": "", "pattern": ""}
            a = AUDIT / f"{cat}--{d.name}.json"
            if a.exists():
                j = json.loads(a.read_text())
                if j.get("owner", {}).get("verdict") in ("remove", "hold"):
                    continue  # removed after the owner's review, or held until rebuilt; the files stay in the repo
                industry = str(j.get("industry", "")).lower().strip()
                audience = "b2b" if cat == "product" or industry in B2B_INDUSTRIES or any(k in industry for k in B2B_WORDS) else "consumer"
                styles = [str(x).lower().strip() for x in j.get("style", [])][:4]
                # the latest round decides the "Being rebuilt" stamp: a round-4 piece passed the blind comparison; before that, round 3;
                # a piece the round-4 audit sends back for work is stamped until it passes
                latest = j.get("round5") or j.get("round4") or j.get("round3") or {}
                todo = ORDER["scores"].get(f"{cat}--{d.name}", {}).get("action") in ("polish", "rebuild") and not (j.get("round4") or j.get("round5"))
                verdict = "polish" if todo else ("" if (latest.get("score") or 0) >= 4 else j.get("owner", {}).get("verdict") or j.get("verdict", ""))
                meta = {"tags": [audience] + styles + ([industry] if industry else []), "styles": styles, "verdict": verdict, "pattern": j.get("pattern", "")}
            extras = [x for x in sorted(d.glob("shot-*.png")) if not any(k in x.stem for k in ("painted", "-v", "draft", "old"))] if shot.exists() else []
            out.append({"key": f"{cat}--{d.name}", "cat": cat, "label": label, "src": src, "w": w, "h": h, "title": title, "blurb": blurb,
                        "frames": [(x.stem.replace("shot-", ""), x) for x in extras], **meta})
    # strongest first (owner, 2026-10-15: "in the order that people feel good to see them"), from the round-4 audit's ranking;
    # pieces it has not ranked keep their folder order after the ranked ones
    rank = {k: i for i, k in enumerate(ORDER["order"])}
    out.sort(key=lambda p: rank.get(p["key"], len(rank)))
    return out


def show_images(pieces):
    """A 900 px tile and an 1800 px image for the lightbox per piece, cached by the render's modification time."""
    from PIL import Image
    cache = CACHE / "show"; cache.mkdir(parents=True, exist_ok=True)
    (DIST / "img" / "show").mkdir(parents=True, exist_ok=True)
    for p in pieces:
        stamp = int(p["src"].stat().st_mtime)
        for width, name in ((THUMB_W, f"{p['key']}.webp"), (FULL_W, f"{p['key']}-{FULL_W}.webp")):
            c = cache / f"{stamp}-{name}"
            if not c.exists():
                im = Image.open(p["src"]).convert("RGB")
                long_side = max(im.size)
                scale = min(1.0, width / (im.width if width == THUMB_W else long_side))
                if scale < 1:
                    im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
                im.save(c, "WEBP", quality=82 if width == FULL_W else 80)
            shutil.copy(c, DIST / "img" / "show" / name)
        with Image.open(cache / f"{stamp}-{p['key']}.webp") as im:
            p["tw"], p["th"] = im.size
        for fname, fsrc in p.get("frames", []):
            fstamp = int(fsrc.stat().st_mtime)
            c = cache / f"{fstamp}-{p['key']}--{fname}-{FULL_W}.webp"
            if not c.exists():
                im = Image.open(fsrc).convert("RGB")
                scale = min(1.0, FULL_W / max(im.size))
                if scale < 1:
                    im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
                im.save(c, "WEBP", quality=82)
            shutil.copy(c, DIST / "img" / "show" / f"{p['key']}--{fname}-{FULL_W}.webp")
            t = cache / f"{fstamp}-{p['key']}--{fname}.webp"
            if not t.exists():
                im = Image.open(fsrc).convert("RGB")
                scale = min(1.0, THUMB_W / im.width)
                if scale < 1:
                    im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
                im.save(t, "WEBP", quality=80)
            shutil.copy(t, DIST / "img" / "show" / f"{p['key']}--{fname}.webp")
            with Image.open(t) as im:
                p.setdefault("frame_sizes", {})[fname] = im.size


STYLE_WORDS = {"minimal", "swiss", "editorial", "brutalist", "glass", "dark", "neon", "y2k", "organic", "luxury", "playful", "enterprise", "retro", "industrial", "terminal", "clinical"}


def sticker_kind(t, p):
    """B2B cobalt, consumer sky, a style ink, the industry paper."""
    if t == "b2b":
        return ""
    if t == "consumer":
        return "sky"
    if t in STYLE_WORDS or t in p.get("styles", []):
        return "ink"
    return "paper"


def sticker_icon(t, p):
    if t == "b2b":
        return "building"
    if t == "consumer":
        return "person"
    if t in STYLE_WORDS or t in p.get("styles", []):
        return "brush"
    return "tag"


CAPS = {"ai": "AI", "b2b": "B2B", "b2c": "B2C", "ui": "UI", "ux": "UX", "saas": "SaaS", "hr": "HR", "crm": "CRM", "api": "API", "iot": "IoT", "hmi": "HMI"}


def sticker_label(t):
    t = re.split(r"[(/,;:]| - ", t)[0].strip()  # the audit's industry field can be a phrase; the label keeps its head
    t = t if len(t) <= 24 else t[:24].rsplit(" ", 1)[0]
    t = " ".join(CAPS.get(w.lower(), w) for w in t.split(" "))
    return t[:1].upper() + t[1:]


CHEV = {"prev": '<svg viewBox="0 0 16 16" width="16" height="16" aria-hidden="true"><path d="M10 3.5 5.5 8l4.5 4.5" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"/></svg>',
        "next": '<svg viewBox="0 0 16 16" width="16" height="16" aria-hidden="true"><path d="m6 3.5 4.5 4.5L6 12.5" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"/></svg>'}


def piece_card(p, i, frame):
    """One gallery card. A piece with extra frames gets them in its own frame: swipe, chevrons and a dot for each (owner,
    2026-10-15: no "+2 frames" sticker; the image itself changes). Tags are one quiet line, not three styles of label."""
    tags = [t for t in p["tags"] if t in ("b2b", "consumer")][:1] + [t for t in p["tags"] if t in p.get("styles", [])][:1] + [t for t in p["tags"] if t not in ("b2b", "consumer") and t not in p.get("styles", [])][:1]
    meta = " · ".join(esc(sticker_label(t)) for t in tags)
    review = ""
    if p["verdict"] in ("polish", "remake", "improve"):  # a quiet note, not a rotated stamp on the picture (round 4 audit: stamps were clutter)
        meta = (meta + " · " if meta else "") + '<span class="piece-note">Being rebuilt</span>'
    data = f'data-blurb="{esc(p["blurb"])}" data-tags="{esc(", ".join(p["tags"]))}"'
    shots = [(f"/img/show/{p['key']}-{FULL_W}.webp", f"/img/show/{p['key']}.webp", p["tw"], p["th"], p["title"])]
    for fn, _src in p.get("frames", []):
        fw, fh = p.get("frame_sizes", {}).get(fn, (p["tw"], p["th"]))
        shots.append((f"/img/show/{p['key']}--{fn}-{FULL_W}.webp", f"/img/show/{p['key']}--{fn}.webp", fw, fh, f"{p['title']} · {fn.replace('-', ' ')}"))
    links = "".join(f'<a class="piece-link{" slide" if len(shots) > 1 else ""}" href="{full}" data-gallery="{i}" data-title="{esc(t)}" {data}'
                    + ("" if len(shots) > 1 else f' style="aspect-ratio:{frame}"')
                    + f'><img src="{thumb}" width="{w}" height="{h}" loading="lazy" alt="{esc(t)}"></a>' for full, thumb, w, h, t in shots)
    if len(shots) > 1:
        dots = '<span class="sl-dot"></span>' * len(shots)
        media = (f'<div class="slides" data-slides role="group" aria-roledescription="carousel" aria-label="{esc(p["title"])}, {len(shots)} frames" style="aspect-ratio:{frame}">'
                 f'<div class="sl-track">{links}</div>'
                 f'<button type="button" class="sl-arrow sl-prev" aria-label="Previous frame" disabled>{CHEV["prev"]}</button>'
                 f'<button type="button" class="sl-arrow sl-next" aria-label="Next frame">{CHEV["next"]}</button>'
                 f'<span class="sl-status visually-hidden" aria-live="polite">Frame 1 of {len(shots)}</span></div>')
        dots = f'<span class="sl-dots" aria-hidden="true">{dots}<span class="sl-pill"></span></span>'  # beside the title, so they never cover the screen
    else:
        media, dots = links, ""
    return (f'<figure class="piece" data-tags="{esc(" ".join(p["tags"]))}" data-cat="{p["cat"]}">{media}{review}'
            f'<figcaption><span class="piece-head"><strong>{esc(p["title"])}</strong>{dots}</span><span>{esc(p["blurb"])}</span>' + (f'<span class="piece-meta">{meta}</span>' if meta else "") + '</figcaption></figure>')


def showcase(pages):
    pieces = show_pieces()
    show_images(pieces)
    counts = {}
    for p in pieces:
        for t in p["tags"]:
            counts[t] = counts.get(t, 0) + 1
    styles = {"minimal", "swiss", "editorial", "brutalist", "glass", "dark", "neon", "y2k", "organic", "luxury", "playful", "enterprise", "retro", "industrial", "terminal", "clinical"}
    top = [t for t in ("b2b", "consumer") if t in counts] + [t for t, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])) if t in styles and n >= 3]
    filters = ('<div class="filters" role="group" aria-label="Filter by tag"><button type="button" class="filter is-on" data-tag="">All <span class="num">' + str(len(pieces)) + "</span></button>"
               + "".join(f'<button type="button" class="filter" data-tag="{esc(t)}">{esc(sticker_label(t))} <span class="num">{counts[t]}</span></button>' for t in top) + "</div>") if top else ""
    blocks, items, md, i = [], [], ["# Showcase", "", SHOW_INTRO, ""], 0
    cat_rank = {c: n for n, c in enumerate(ORDER["category_order"])}
    for cat, label in sorted(CATS, key=lambda c: cat_rank.get(c[0], len(cat_rank))):
        ps = [p for p in pieces if p["cat"] == cat]
        if not ps:
            continue
        groups = [(None, ps, CAT_FRAMES[cat])]
        if cat == "app-screens":
            groups = [("Phones", [p for p in ps if p["h"] > p["w"]], CAT_FRAMES[cat]), ("Tablet and desktop", [p for p in ps if p["h"] <= p["w"]], "16 / 10")]
        md += [f"## {label}", ""]
        grids = []
        for sub, gp, frame in groups:
            if not gp:
                continue
            cards = []
            for p in gp:
                cards.append(piece_card(p, i, frame)); i += 1
                items.append({"@type": "ImageObject", "name": p["title"], "contentUrl": f"{SITE_URL}/img/show/{p['key']}-{FULL_W}.webp", "thumbnailUrl": f"{SITE_URL}/img/show/{p['key']}.webp", "description": p["blurb"], "keywords": ", ".join(p["tags"])})
                md.append(f"- **{p['title']}**" + (f" ({', '.join(p['tags'])})" if p["tags"] else "") + f": {p['blurb']}")
            grids.append((f'<h3 class="t-h3 sub">{sub}</h3>' if sub else "") + f'<div class="pieces {cat}{" portrait" if frame.startswith("9") or frame.startswith("615") else ""}">{"".join(cards)}</div>')
        md.append("")
        blocks.append(f'<section class="block show-cat" id="{cat}"><p class="kicker">{len(ps)} pieces</p><h2 class="t-h2">{label}</h2>{"".join(grids)}</section>')
    head = (f'<div class="page-head"><nav class="crumb" aria-label="Breadcrumb"><a href="/">{NAME}</a><span aria-hidden="true">/</span><span aria-current="page">Showcase</span></nav>'
            f'<h1 class="t-h1">{len(pieces)} designs, one process</h1><p class="lede">{esc(SHOW_INTRO)} <a href="{GH}/blob/main/brand/showcase/STRESS-TEST.md">Read the findings</a>.</p>{filters}'
            f'</div>')
    lightbox = ('<dialog class="lb" id="lightbox" aria-label="Gallery"><div class="lb-bar"><div class="lb-text"><strong class="lb-title"></strong><span class="lb-blurb"></span><span class="lb-tags kicker"></span></div>'
                '<div class="lb-actions"><a class="lb-open" href="#" target="_blank" rel="noopener">Open image</a><button type="button" class="lb-prev" aria-label="Previous">←</button><button type="button" class="lb-next" aria-label="Next">→</button><button type="button" class="lb-close" aria-label="Close">Esc</button></div></div>'
                '<div class="lb-stage"><img class="lb-img" alt=""></div></dialog>')
    ld = [crumbs_ld([("Showcase", "/showcase/")]), {"@context": "https://schema.org", "@type": "CollectionPage", "name": "OpenDesigner showcase",
                                                    "url": f"{SITE_URL}/showcase/", "description": SHOW_INTRO, "hasPart": items[:60]}]
    html_ = shell("/showcase/", "OpenDesigner showcase: B2B screens, styles and more",
                  "Heroes, components, app and watch screens, footers and mockups that AI agents built through OpenDesigner, audited against real UI and tagged.",
                  head + "".join(blocks) + lightbox, pages, ld, og="/og/showcase.png", wide=True)
    return html_, "\n".join(md)


NOT_FOUND_ART = SITE / "static" / "404.webp"   # the owner's illustration; the page works without it
NOT_FOUND_CSS = """<style>
.nf { display: grid; grid-template-columns: minmax(0, 1fr); align-content: start; gap: 40px; min-height: min(80vh, 780px);
  max-width: var(--shell, 1200px); margin: 0 auto; padding: clamp(32px, 7vh, 88px) clamp(16px, 4vw, 32px) 0; }
.nf-copy { max-width: 600px; }
.nf-copy h1 { font-size: clamp(20px, 2.3vw, 24px); line-height: 1.45; font-weight: 400; color: var(--ink-muted); margin: 12px 0 0; text-wrap: pretty; }
.nf-copy h1 b { color: var(--ink); font-weight: 600; }
.nf-actions { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 28px; }
.nf-art { margin: 0; }
.nf-art img { display: block; width: 100%; height: auto; }
.nf.wide .nf-art { align-self: end; justify-self: center; }
.nf.wide .nf-art img { width: auto; max-width: 100%; max-height: min(54vh, 560px); }
.nf.tall { grid-template-columns: minmax(0, 1fr) minmax(0, .85fr); align-items: center; align-content: center; gap: clamp(24px, 5vw, 72px); padding-bottom: clamp(24px, 5vh, 56px); }
.nf.tall .nf-art img { max-height: 76vh; width: auto; max-width: 100%; margin-left: auto; }
@media (max-width: 767px) {
  .nf, .nf.tall { grid-template-columns: minmax(0, 1fr); min-height: auto; gap: 32px; }
  .nf.tall .nf-art img { max-height: 56vh; margin: 0 auto; }
}
</style>"""


NOT_FOUND_COPY = {
    "label": "Error 404",
    "lead": "Wrong room, right house.",
    "rest": ("That link led somewhere we haven&rsquo;t finished, or somewhere we moved. Thanks for wandering in anyway. "
             "Pick a door below and we&rsquo;ll take it from here."),
    "home": "Front door", "docs": "The library of docs", "report": "Flag this room",
}


def not_found_section(art_url=None, size=None, copy=None):
    """The 404 block. A wide picture sits along the bottom; a tall one sits beside the copy (below it on phones)."""
    c = dict(NOT_FOUND_COPY, **(copy or {}))
    kind, art = "", ""
    if art_url and size:
        w, h = size
        kind = " wide" if w >= h else " tall"
        art = f'<figure class="nf-art"><img src="{art_url}" alt="" width="{w}" height="{h}" decoding="async"></figure>'
    return (f'<section class="nf{kind}"><div class="nf-copy"><p class="kicker">{c["label"]}</p>'
            f'<h1><b>{c["lead"]}</b> {c["rest"]}</h1>'
            f'<div class="nf-actions"><a class="btn primary" href="/">{c["home"]}</a><a class="btn ghost" href="/docs/">{c["docs"]}</a>'
            f'<a class="btn ghost" href="{GH}/issues/new?title=Broken%20link%20on%20opendesigner.dev">{c["report"]}</a></div></div>'
            f'{art}</section>')


def not_found(pages):
    size = None
    if NOT_FOUND_ART.exists():
        from PIL import Image
        with Image.open(NOT_FOUND_ART) as im:
            size = im.size
    body = NOT_FOUND_CSS + not_found_section("/404.webp" if size else None, size)
    return shell("/404.html", "Page not found · OpenDesigner", "This page doesn't exist.", body, pages, md=False, robots="noindex", home=True)


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
    demo_before_after_files()
    mark = BRAND / "kit" / "logo" / "avatar-light-800.png"
    if mark.exists():
        im = Image.open(mark).convert("RGB")
        for size, name in ((180, "apple-touch-icon.png"), (32, "favicon-32.png"), (192, "icon-192.png"), (512, "icon-512.png")):
            im.resize((size, size), Image.LANCZOS).save(DIST / name)
    fav = (BRAND / "design-system/project/assets/Logos/mark-light.svg").read_text().replace('viewBox="0 0 100 100"', 'viewBox="-12 -12 124 124"')
    (DIST / "favicon.svg").write_text(fav)


OG_ALT = "OpenDesigner: make everything you build look like it belongs together. A free, open-source design system builder for the AI tool you already use."


def og_images(pages):
    """Social previews (1200 x 630) in site/.cache/og/: the home card, a card for every docs page (its section and title beside
    the home card's drawing, so a shared link says which page it is), and the showcase card. A card is drawn again only when its
    HTML changes: manifest.json keeps a hash of each. Cards no page uses any more are removed."""
    import hashlib
    import io
    from PIL import Image
    sys.path.insert(0, str(BRAND / "design-system"))
    import export_kit as K
    out = CACHE / "og"
    (out / "docs").mkdir(parents=True, exist_ok=True)
    fill = lambda h: (h.replace("{{FONT_HANKEN}}", (CACHE / "hanken-300-700.woff2").resolve().as_uri())
                       .replace("{{FONT_MONO}}", (CACHE / "sourcecodepro-500.woff2").resolve().as_uri())
                       .replace("{{LOCKUP}}", (BRAND / "design-system/project/assets/Logos/lockup-dark.svg").read_text())
                       .replace("{{DOMAIN}}", SITE_URL.split("//", 1)[-1]))
    jobs = {"home.jpg": ("file", fill((SITE / "og" / "home.html").read_text()).replace(
        "{{LOGOS}}", "".join(logo(k, 22) for k in ("claude", "openai", "cursor", "githubcopilot", "googlegemini"))))}
    card = fill((SITE / "og" / "page.html").read_text())
    for p in pages:
        kicker = "Docs" if p["slug"] == "index" else f'Docs · {p["section"]}'
        jobs[f'docs/{p["slug"]}.jpg'] = ("file", card.replace("{{KICKER}}", esc(kicker)).replace("{{TITLE}}", esc(p["title"])))
    jobs["showcase.png"] = ("post", K.statement("cobalt", 'B2B screens, styles and more. <span class="od-strong">One process.</span>',
                                                "Built by AI agents through OpenDesigner. Every brand is invented.", "Showcase", 1200, 630, "social-subhead"))
    digest = lambda h: hashlib.sha256(h.encode()).hexdigest()
    mf = out / "manifest.json"
    seen = json.loads(mf.read_text()) if mf.exists() else {}
    todo = {n: j for n, j in jobs.items() if seen.get(n) != digest(j[1]) or not (out / n).exists()}
    if todo:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as pw:
            b = pw.chromium.launch(channel="chrome")
            pg = b.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=1)
            for name, (kind, html_) in todo.items():
                if kind == "file":  # fonts load from file:// URLs, so the page must be a file too
                    (CACHE / "og-render.html").write_text(html_)
                    pg.goto((CACHE / "og-render.html").resolve().as_uri(), wait_until="networkidle")
                else:
                    pg.set_content(html_, wait_until="networkidle")
                pg.evaluate("document.fonts.ready")
                pg.wait_for_timeout(150)
                if kind == "file":  # JPEG: the film grain makes a PNG of this card about 800 KB; this is about 60 KB
                    Image.open(io.BytesIO(pg.screenshot())).convert("RGB").save(out / name, "JPEG", quality=86, optimize=True, progressive=True)
                else:
                    pg.locator(".od-post").first.screenshot(path=str(out / name))
                seen[name] = digest(html_)
            b.close()
    for f in [f for ext in ("png", "jpg") for f in list(out.glob(f"*.{ext}")) + list((out / "docs").glob(f"*.{ext}"))]:
        if str(f.relative_to(out)) not in jobs:
            f.unlink()
            seen.pop(str(f.relative_to(out)), None)
    mf.write_text(json.dumps({n: seen[n] for n in sorted(seen) if n in jobs}, indent=1))
    print(f"OG cards: {len(todo)} drawn, {len(jobs) - len(todo)} unchanged")


def robots():
    bots = ["*", "Googlebot", "Bingbot", "OAI-SearchBot", "ChatGPT-User", "GPTBot", "Claude-SearchBot", "Claude-User", "ClaudeBot",
            "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot", "Applebot-Extended"]
    head = ("# OpenDesigner is open source and wants to be found, read and cited by people, search engines and AI assistants.\n"
            "# Search engines and AI crawlers are welcome, including those that train models.\n"
            f"# For AI agents: {SITE_URL}/llms.txt (the site in Markdown) and {SITE_URL}/.well-known/agent-skills/index.json (the skills).\n")
    # Content Signals (contentsignals.org): yes to search, to answering from the pages, and to training. A crawler reads only
    # the group that names it, so each group says it.
    signal = "Content-Signal: search=yes, ai-input=yes, ai-train=yes\n"
    return head + "\n".join(f"User-agent: {b}\n{signal}Allow: /\n" for b in bots) + f"\nSitemap: {SITE_URL}/sitemap.xml\n"


def skill_names():
    return sorted(d.name for d in (ROOT / "skills").iterdir() if (d / "SKILL.md").exists())


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

{library_page.llms_section(SITE_URL)}

## For AI agents

- [Agent Skills index]({SITE_URL}/.well-known/agent-skills/index.json): the {len(skill_names())} OpenDesigner skills ({", ".join(skill_names())}), each as a zip with its digest, to install in any tool that reads Agent Skills
- Claude Code: `/plugin marketplace add {REPO}`, then `/plugin install opendesigner@opendesigner`. Other tools: [Install OpenDesigner]({SITE_URL}/docs/install/index.md)
- Every docs, library and showcase page, and the home page, has a Markdown copy at its address plus `index.md` (for example {SITE_URL}/docs/install/index.md). The links in this file point at those copies. Asking for a page with `Accept: text/markdown` returns the same copy
- [llms-full.txt]({SITE_URL}/llms-full.txt): every page of this site in one file
- [Changelog]({SITE_URL}/changelog/index.md): what changed, newest first, and how to update
- [version.json]({SITE_URL}/version.json): the current version, the date of the latest change and how to update; [changelog.xml]({SITE_URL}/changelog.xml) is an Atom feed of every change

## Optional

- [Book a call]({SITE_URL}/book/): a free {CONFIG["BOOKING_FREE_MINUTES"]}-minute intro call about OpenDesigner
- [Website privacy](https://github.com/{REPO}/blob/main/docs/PRIVACY.md#the-websites-product-analytics): the site measures page load speed (Vercel Speed Insights) and counts visits and clicks with PostHog without cookies; a visit is recorded only if the visitor allows it
- [Showcase]({SITE_URL}/showcase/index.md): B2B product screens, style studies, heroes, components, app and watch screens, footers and mockups built by AI agents through the process, each audited against shipped products
- [GitHub repository]({GH}): source, issues and discussions
- [AGENTS.md](https://raw.githubusercontent.com/{REPO}/main/AGENTS.md): instructions for AI agents working with the repository
- [Research map](https://raw.githubusercontent.com/{REPO}/main/docs/RESEARCH.md): 352 Decision Cards behind the defaults, each with cited sources
"""


# style-src allows inline style attributes: the figures and gallery tiles set sizes and colors inline. The site is static, with no user content.
CSP = ("default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data: https://images.unsplash.com; font-src 'self'; "
       "connect-src 'self' https://api.github.com; frame-ancestors 'none'; base-uri 'self'; form-action 'none'; upgrade-insecure-requests")


# Product analytics: PostHog's US cloud, cookieless by default (session replay only after consent), behind /ingest/ on this site (site/static/ph.js). Off while the key is empty.
ANALYTICS = json.loads((SITE / "analytics.json").read_text()) if (SITE / "analytics.json").exists() else {}
PH_KEY = ANALYTICS.get("posthog_key", "").strip()
PH_TAG = f'\n<script src="/ph.js" data-key="{esc(PH_KEY)}" defer></script>' if PH_KEY else ""
# PostHog's endpoints end in a slash (/i/v0/e/, /flags/). With trailingSlash on, "/ingest/:path*" does not match them and
# Vercel served its 404 to every event (2026-10-24), so the slash form comes first.
PH_REWRITES = [{"source": "/ingest/static/:path*", "destination": "https://us-assets.i.posthog.com/static/:path*"},
               {"source": "/ingest/:path*/", "destination": "https://us.i.posthog.com/:path*/"},
               {"source": "/ingest/:path*", "destination": "https://us.i.posthog.com/:path*"}] if PH_KEY else []


def vercel_json():
    return {"trailingSlash": True,
            **({"rewrites": PH_REWRITES} if PH_REWRITES else {}),
            "redirects": [{"source": src, "destination": b, "permanent": True} for a, b in REDIRECTS.items() for src in (a, a.rstrip("/"))]
                         + [{"source": "/index.html", "destination": "/", "permanent": True},
                            {"source": "/:path*/index.html", "destination": "/:path*/", "permanent": True}],
            "headers": [
                {"source": "/(.*)", "headers": [{"key": "Content-Security-Policy", "value": CSP}, {"key": "X-Content-Type-Options", "value": "nosniff"},
                                                {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
                                                {"key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=(), interest-cohort=()"},
                                                {"key": "Strict-Transport-Security", "value": "max-age=63072000; includeSubDomains"}]},
                {"source": "/fonts/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]},
                {"source": "/img/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=604800"}]},
                {"source": "/library/r/(.*)", "headers": [{"key": "X-Robots-Tag", "value": "noindex"}, {"key": "Content-Type", "value": "text/html; charset=utf-8"}, {"key": "Access-Control-Allow-Origin", "value": "*"}]},
                {"source": "/(.*)\\.md", "headers": [{"key": "Content-Type", "value": "text/markdown; charset=utf-8"}, {"key": "X-Robots-Tag", "value": "noindex"}]},
                {"source": "/(llms.txt|llms-full.txt|robots.txt)", "headers": [{"key": "Content-Type", "value": "text/plain; charset=utf-8"}]},
                {"source": "/changelog.xml", "headers": [{"key": "Content-Type", "value": "application/atom+xml; charset=utf-8"}]},
                {"source": "/", "headers": [{"key": "Link", "value": LINKS}, {"key": "Vary", "value": "Accept"}]},
                {"source": "/(.*)/", "headers": [{"key": "Vary", "value": "Accept"}]},  # a page answers in HTML or, when asked, Markdown
                {"source": "/.well-known/agent-skills/(.*)", "headers": [{"key": "Access-Control-Allow-Origin", "value": "*"}]}]}


# The home page's Link header (RFC 8288): where an agent finds the site as text, the docs and the skills index.
LINKS = ('</llms.txt>; rel="describedby"; type="text/plain", </index.md>; rel="alternate"; type="text/markdown", '
         '</docs/>; rel="service-doc", </.well-known/agent-skills/index.json>; rel="describedby"; type="application/json"')


def agent_skills():
    """/.well-known/agent-skills/: the eight skills for agents that read the Agent Skills discovery index (v0.2.0,
    github.com/cloudflare/agent-skills-discovery-rfc). Each is the self-contained zip tools/build_dist.py makes for
    claude.ai, and the index gives its SHA-256, so a client can check what it downloaded."""
    import hashlib
    subprocess.run([sys.executable, str(ROOT / "tools/build_dist.py")], check=True, capture_output=True)
    out = DIST / ".well-known" / "agent-skills"
    out.mkdir(parents=True, exist_ok=True)
    skills = []
    for d in sorted(x for x in (ROOT / "skills").iterdir() if (x / "SKILL.md").exists()):
        zipped = out / f"{d.name}.zip"
        shutil.copy(ROOT / "dist" / zipped.name, zipped)
        desc = re.search(r"^description:\s*(.+)$", (d / "SKILL.md").read_text(), re.M).group(1).strip().strip('"')
        skills.append({"name": d.name, "type": "archive", "description": desc[:1024], "url": f"/.well-known/agent-skills/{zipped.name}",
                       "digest": "sha256:" + hashlib.sha256(zipped.read_bytes()).hexdigest()})
    (out / "index.json").write_text(json.dumps({"$schema": "https://schemas.agentskills.io/discovery/0.2.0/schema.json", "skills": skills}, indent=1) + "\n")
    return len(skills)


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
    (DIST / "site.css").write_text(minify_css(ff + tokens_css() + corners_match_levers(apple_tracking((SITE / "static" / "site.css").read_text() + (SITE / "static" / "figures.css").read_text() + status_css() + (SITE / "static" / "home.css").read_text() + (SITE / "static" / "craft.css").read_text() + (SITE / "static" / "deco.css").read_text() + (SITE / "static" / "changelog.css").read_text()))))
    shutil.copy(SITE / "static" / "site.js", DIST / "site.js")
    if PH_KEY:
        shutil.copy(SITE / "static" / "ph.js", DIST / "ph.js")
    if NOT_FOUND_ART.exists():
        shutil.copy(NOT_FOUND_ART, DIST / "404.webp")
    shutil.copy(SITE / "middleware.js", DIST / "middleware.js")  # Markdown for agents: Vercel builds it as Routing Middleware
    images()
    pages = load_docs()
    for p in pages:
        if p["slug"] == "changelog":  # the page changes whenever the repository does
            p["updated"] = version_facts()["latest_change"]
    try:
        og_images(pages)  # only the cards whose HTML changed are drawn again
    except Exception as e:
        print("OG images not rendered:", e)
    if (CACHE / "og").exists():
        shutil.copytree(CACHE / "og", DIST / "og", dirs_exist_ok=True, ignore=shutil.ignore_patterns("manifest.json"))
    faq_page = next((p for p in pages if p["slug"] == "faq"), None)
    faq = faq_items(faq_page["body"]) if faq_page else []
    files = {"index.html": home(pages, facts, faq), "docs/index.html": docs_home(pages, facts, faq)}
    mds = {"index.md": f"# {NAME}\n\n{ONE_LINER}\n\nDocs: {SITE_URL}/docs/\nInstall: {SITE_URL}/docs/install/\nShowcase: {SITE_URL}/showcase/\nSource: {GH}\n",
           "docs/index.md": "# OpenDesigner docs\n\n" + "\n".join(f"- [{p['title']}]({SITE_URL}{p['path']}): {p['description']}" for p in pages if p["section"] in SECTIONS) + "\n"}
    for p in pages:
        rel = p["path"].lstrip("/")
        files[rel + "index.html"] = doc_page(p, pages)
        mds[rel + "index.md"] = f"# {p['title']}\n\n{strip_figures(p['body'])}\n"
    sh_html, sh_md = showcase(pages)
    files["showcase/index.html"] = sh_html
    mds["showcase/index.md"] = sh_md + "\n"
    files["404.html"] = not_found(pages)
    files["book/index.html"] = book_page(pages)
    library_paths = []
    library_page.add(sys.modules[__name__], files, mds, library_paths)  # /library/: the optional component library (its own module)
    for rel, text in {**files, **mds}.items():
        f = DIST / rel
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(text)
    paths = ["/", "/docs/"] + [p["path"] for p in pages] + ["/showcase/", "/book/"] + library_paths
    (DIST / "robots.txt").write_text(robots())
    (DIST / "changelog.xml").write_text(changes_feed())
    (DIST / "version.json").write_text(json.dumps({**version_facts(), "name": NAME, "changelog": f"{SITE_URL}/changelog/",
        "feed": f"{SITE_URL}/changelog.xml", "check_your_system": "engine.py version, from the opendesigner skill's scripts folder",
        "update_in_claude_code": "claude plugin update opendesigner@opendesigner"}, indent=1) + "\n")
    agent_skills()
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
