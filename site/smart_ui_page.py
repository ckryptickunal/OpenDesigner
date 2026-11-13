"""The Smart UI page (/smart-ui/) and its live demo (/smart-ui/demo/).

Owner request, 2026-11-13: Smart UI in the main navigation, with a page that shows it working. Site demos are live HTML,
never screenshots or video (owner, 2026-10-21), so the page embeds the real renderer playing recorded answers: the demo at
/smart-ui/demo/ is examples/smart-ui-chat/ with its paths fixed for the site, served in a same-origin iframe so its tokens
style only the demo and never the site. Every count and every rule on the page is read from the repository at build time
(the Smart UI set, the validator's shared cases, the recorded turns and the docs pages), so the page cannot drift from them.

build.py calls add(); the page's styles are /smart-ui.css (site/static/smart-ui.css). The demo's script and extra styles are
site/static/smart-ui-demo.js and smart-ui-demo.css. /smart-ui/demo/* needs framing by this site only: build.py's
vercel_json() sends it frame-ancestors 'self' instead of 'none'.
"""
import hashlib
import html
import json
import pathlib
import re
import shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
STATIC = ROOT / "site" / "static"
SKILL = ROOT / "skills" / "opendesigner-smart-ui"
EXAMPLE = ROOT / "examples" / "smart-ui-chat"
DOCS = ROOT / "site" / "docs"
esc = html.escape
PATH = "/smart-ui/"
DEMO = PATH + "demo/"
TITLE = "Smart UI"
SEO_TITLE = "Smart UI: generative UI drawn from your own components"
DESCRIPTION = ("Your assistant answers with your own interface: a flight list, a fare comparison, a receipt. "
               "Try the live demo, then see what is checked and what is tested.")
VER = ""
WORDS = {4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight"}
# the systems the demo can switch between: (file in the demo, label, source tokens.css)
SYSTEMS = [("orvell", "Orvell Travel", EXAMPLE / "opendesigner/build/css/tokens.css"),
           ("devtool-dense", "Devtool Dense", ROOT / "examples/devtool-dense/build/css/tokens.css"),
           ("consumer-playful", "Consumer Playful", ROOT / "examples/consumer-playful/build/css/tokens.css")]


def section(md, heading):
    """The body of one '## heading' section of a Markdown file."""
    m = re.search(r"^## " + re.escape(heading) + r"\n(.*?)(?=^## |\Z)", md, re.S | re.M)
    return m.group(1).strip() if m else ""


def table_rows(block):
    rows = [ln.strip().strip("|").split("|") for ln in block.splitlines() if ln.startswith("|")]
    return [[c.strip() for c in r] for r in rows[2:]]  # skip the header and the --- row


def facts():
    s = json.loads((SKILL / "assets/set.json").read_text())
    groups = [g for g in s["groups"] if g != "domain"]
    cases = json.loads((SKILL / "assets/fixtures/validator/cases.json").read_text())["cases"]
    turns = json.loads((EXAMPLE / "turns.json").read_text())["turns"]
    concept = (DOCS / "smart-ui.md").read_text()
    adapters = (DOCS / "smart-ui-adapters.md").read_text()
    steps = re.findall(r"^\d+\. \*\*(.+?)\.\*\* (.+)$", section(concept, "How an answer becomes interface"), re.M)
    rules = table_rows(section(concept, "The rules it keeps"))
    where = table_rows(adapters.split("\n## ")[0])
    untried = re.findall(r"^- (.+)$", section(adapters, "What we haven't tried"), re.M)
    assert steps and rules and where and untried, "smart_ui_page: a docs section it reads has moved (site/docs/smart-ui*.md)"
    lib = ROOT / "skills/opendesigner/assets/library/components"
    by_job = [(g, s["groups"][g], [(c["slug"], json.loads((lib / c["slug"] / "meta.json").read_text())["name"]) for c in s["components"] if c["group"] == g])
              for g in s["groups"]]
    library = sum(1 for d in lib.iterdir() if (d / "meta.json").exists())
    return {"library": library, "parts": len(s["components"]), "by_job": [j for j in by_job if j[2]], "groups": groups, "domain": [c["as"] for c in s["components"] if c["group"] == "domain"],
            "cases": len(cases), "questions": sum(1 for t in turns if t.get("user")), "steps": steps, "rules": rules,
            "where": where, "untried": untried}


def frame(b, src, title, cls, eager=False):
    """The demo in a same-origin iframe, on a photo stage in the site's glass bezel."""
    lazy = "" if eager else ' loading="lazy"'
    st, credit = b.stage("blue-soft", f'<iframe class="su-frame" src="{src}" title="{esc(title)}"{lazy}></iframe>', cls)
    return st, credit


def hero(b, f):
    st, credit = frame(b, DEMO, "Smart UI demo: a travel assistant with recorded answers", "su-stage", eager=True)
    jobs = ", ".join(f["groups"][:-1]) + " and " + f["groups"][-1]
    stats = [(f["parts"], f"parts an answer can use, from the component library."),
             (len(f["groups"]), f"jobs they're sorted into: {jobs}."),
             (f["cases"], "shared test cases. The Python and browser validators must answer each one the same way."),
             (len(SYSTEMS), "design systems in this demo. Same answers, different tokens.")]
    stat_html = "".join(f'<div class="su-stat"><p class="su-big num">{n}</p><p>{esc(t)}</p></div>' for n, t in stats)
    return f"""
<section class="h-sec h-first su-hero">
<nav class="crumb" aria-label="Breadcrumb"><a href="/">{b.NAME}</a><span aria-hidden="true">/</span><span aria-current="page">Smart UI</span></nav>
<p class="kicker su-eyebrow">Comes with OpenDesigner</p>
<h1 class="su-title">Answers that show your interface</h1>
<p class="h-lede su-lede">Smart UI makes your assistant answer by rendering your own components instead of plain text. Ask it for flights and get a list you can book, drawn with your tokens and checked before it shows.</p>
<p class="su-note">It comes with OpenDesigner. Nothing separate to install, and it stays off until you ask for it or say yes when OpenDesigner offers it.</p>
<p class="su-act"><a class="btn primary" href="/docs/smart-ui-quickstart/">Add it to your assistant</a><a class="h-link" href="/docs/smart-ui/">How it works {b.ARROW}</a></p>
<figure class="su-demo">
{st}
<figcaption>Live in this page, not a video. The answers are recorded, then checked and drawn by the same code a live answer goes through. Try a question, book the fare, switch the system, or send a broken answer. Photo: {credit} on Unsplash.</figcaption>
</figure>
<div class="su-stats">{stat_html}</div>
<p class="h-fine">Counted from the repository when this page was built.</p>
</section>
"""


def steps_section(b, f):
    lis = "".join(f'<li class="su-step"><span class="su-n num">0{i + 1}</span><h3>{esc(t)}</h3><p>{b.inline(d)}</p></li>'
                  for i, (t, d) in enumerate(f["steps"]))
    return f"""
<section class="h-sec" id="how">
<div class="h-head">{b.idx("01", "How it works")}<h2 class="h-h2">From a message to a screen, in {WORDS.get(len(f["steps"]), len(f["steps"]))} steps.</h2>
<p class="h-lede">The model picks a part and fills in words and numbers. It never picks a colour, a size or a link.</p></div>
<ol class="su-steps">{lis}</ol>
</section>
"""


def parts_section(b, f):
    cols = "".join(f'<div class="su-job"><h3>{esc(g.capitalize() if g != "domain" else "For one product")}</h3><p>{esc(what if g != "domain" else "Offered only when the scope step picks it")}</p>'
                   f'<ul>' + "".join(f'<li><a href="/library/{slug}/">{esc(name)}</a></li>' for slug, name in parts) + "</ul></div>"
                   for g, what, parts in f["by_job"])
    rest = f["library"] - f["parts"]
    cols += (f'<a class="su-job su-job-more" href="/library/"><h3>The rest of the library</h3><p>{rest} more components for the screens around the chat. '
             f'They use the same tokens.</p><span class="more">Open the library {b.CHEVRON}</span></a>')
    return f"""
<section class="h-sec" id="parts">
<div class="h-head">{b.idx("02", "The parts")}<h2 class="h-h2">{f["parts"]} parts, each one a library component.</h2>
<p class="h-lede">They work in your product with or without the assistant. Your scope step keeps only the ones you need.</p></div>
<div class="su-jobs">{cols}</div>
</section>
"""


def rules_section(b, f):
    rows = "".join(f'<li><h3>{b.inline(r)}</h3><div><p>{b.inline(m)}</p></div></li>' for r, m in f["rules"])  # side by side, not stacked
    return f"""
<section class="h-sec" id="rules">
<div class="h-head">{b.idx("03", "The rules")}<h2 class="h-h2">What every answer has to pass.</h2>
<p class="h-lede">A mistake goes back to the model as an error it can fix. Nothing half-checked reaches the screen.</p></div>
<ul class="su-rules">{rows}</ul>
</section>
"""


def tested_section(b, f):
    cards = "".join(f'<li class="su-where"><h3>{b.inline(w)}</h3><dl><dt>How</dt><dd>{b.inline(h)}</dd><dt>Tested</dt><dd>{b.inline(t)}</dd></dl></li>'
                    for w, h, t in f["where"])
    untried = "".join(f"<li>{b.inline(x)}</li>" for x in f["untried"])
    return f"""
<section class="h-sec" id="tested">
<div class="h-head h-head-row"><div>{b.idx("04", "Where it runs")}<h2 class="h-h2">What we ran, and what we haven't yet.</h2></div>
<a class="h-link" href="/docs/smart-ui-adapters/">Where Smart UI runs {b.ARROW}</a></div>
<ul class="su-wheres">{cards}</ul>
<div class="su-untried"><h3 class="h-h3">Not tried yet</h3><ul>{untried}</ul></div>
</section>
"""


def end_section(b):
    links = [("Smart UI, explained", "What it does, the rules it keeps and what you get.", "/docs/smart-ui/", "Read the concept"),
             ("Add it to your assistant", "Scope your repo, confirm the parts, write the catalog and check each answer.", "/docs/smart-ui-quickstart/", "Open the quickstart"),
             ("Where it runs", "Your own product, A2UI v1.0, and MCP Apps hosts, with what was tested in each.", "/docs/smart-ui-adapters/", "See the adapters")]
    cards = "".join(f'<a class="who-card" href="{u}"><h3>{t}</h3><p>{d}</p><span class="more">{l} {b.CHEVRON}</span></a>' for t, d, u, l in links)
    return f"""
<section class="h-sec su-end" id="docs">
<div class="h-head">{b.idx("05", "Read more")}<h2 class="h-h2">Try it on your own assistant.</h2>
<p class="h-lede">It needs an OpenDesigner system first. The five-question sketch takes a few minutes.</p></div>
<div class="who su-docs">{cards}</div>
</section>
"""


def markdown(b, f):
    steps = "\n".join(f"{i + 1}. **{t}.** {d}" for i, (t, d) in enumerate(f["steps"]))
    rules = "\n".join(f"- **{r}**: {m}" for r, m in f["rules"])
    where = "\n".join(f"- **{w}**: {h}. Tested: {t}" for w, h, t in f["where"])
    untried = "\n".join(f"- {x}" for x in f["untried"])
    parts = "\n".join(f"- **{g}** ({what}): " + ", ".join(f"[{n}]({b.SITE_URL}/library/{sl}/)" for sl, n in ps) for g, what, ps in f["by_job"])
    return f"""# Smart UI: answers that show your interface

{DESCRIPTION}

Smart UI makes your assistant answer by rendering your own components instead of plain text. Ask it for flights and get a list you can book, drawn with your tokens and checked before it shows. It comes with OpenDesigner, so there's nothing separate to install. It stays off until you ask for it, or until OpenDesigner sees an assistant in your product, offers it once, and you say yes.

The page has a live demo: a travel assistant with recorded answers, drawn by the real renderer, in {len(SYSTEMS)} design systems. The broken answer it can send is refused by the validator.

In numbers, read from the repository: {f["parts"]} parts in {len(f["groups"])} jobs ({", ".join(f["groups"])}), plus {len(f["domain"])} made for one kind of product; {f["cases"]} validator test cases that the Python and browser validators must answer the same way.

## How it works

{steps}

## The parts

{parts}

## The rules

{rules}

## Where it runs

{where}

Not tried yet:

{untried}

Read more: {b.SITE_URL}/docs/smart-ui/ · Quickstart: {b.SITE_URL}/docs/smart-ui-quickstart/ · Adapters: {b.SITE_URL}/docs/smart-ui-adapters/
"""


def demo_files(b):
    """/smart-ui/demo/: the example chat with the site's paths, its renderer, catalog, recorded turns and three systems' tokens."""
    out = b.DIST / "smart-ui" / "demo"
    (out / "tokens").mkdir(parents=True, exist_ok=True)
    for name in ("od-validate.js", "od-surface.js", "od-surface.css"):
        shutil.copy(SKILL / "assets" / name, out / name)
    shutil.copy(EXAMPLE / "opendesigner/smart-ui/catalog.json", out / "catalog.json")
    shutil.copy(EXAMPLE / "opendesigner/smart-ui/od-components.js", out / "od-components.js")
    shutil.copy(EXAMPLE / "turns.json", out / "turns.json")
    for key, _label, src in SYSTEMS:
        shutil.copy(src, out / "tokens" / f"{key}.css")
    (out / "chat.css").write_text((EXAMPLE / "chat.css").read_text() + "\n" + (STATIC / "smart-ui-demo.css").read_text())
    (out / "chat.js").write_text((STATIC / "smart-ui-demo.js").read_text())
    ver = hashlib.sha256(b"".join(p.read_bytes() for p in sorted(out.rglob("*")) if p.is_file())).hexdigest()[:10]
    opts = "".join(f'<option value="{DEMO}tokens/{k}.css">{esc(label)}</option>' for k, label, _ in SYSTEMS)
    page = (EXAMPLE / "index.html").read_text()
    head = (f'<title>Smart UI demo: a travel assistant with recorded answers</title>\n'
            f'<meta name="description" content="A live Smart UI demo: recorded assistant answers, checked by the validator and drawn by the real renderer in three design systems.">\n'
            f'<meta name="robots" content="noindex">\n<link rel="canonical" href="{b.SITE_URL}{DEMO}">\n'
            f'<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">\n'
            f'<link id="tokens" rel="stylesheet" href="{DEMO}tokens/orvell.css">\n'
            f'<link rel="stylesheet" href="{DEMO}od-surface.css?v={ver}">\n<link rel="stylesheet" href="{DEMO}chat.css?v={ver}">\n'
            f'<script src="{DEMO}od-components.js?v={ver}"></script>\n')
    page = re.sub(r"<title>.*?<script src=\"opendesigner/smart-ui/od-components.js\"></script>\n", lambda m: head, page, flags=re.S)
    page = re.sub(r'(<select id="system"[^>]*>).*?(</select>)', lambda m: m[1] + opts + m[2], page, flags=re.S)
    # a heading for the conversation, so the answers' own h3 headings do not skip a level (seen hidden, read by screen readers)
    page = page.replace('<main id="log"', '<h2 class="vh">Conversation</h2>\n  <main id="log"', 1)
    page = page.replace('<script type="module" src="chat.js"></script>', f'<script type="module" src="{DEMO}chat.js?v={ver}"></script>')
    assert "opendesigner/" not in page.replace(b.SITE_URL, "").replace(DEMO, ""), "smart_ui_page: a demo path was not fixed for the site"
    (out / "index.html").write_text(page)


def preview(b):
    """The home page's small preview: the same demo in its mini mode, which plays one answer and takes no input."""
    st, credit = frame(b, DEMO + "?mini", "Smart UI preview: a recorded answer drawn as a list of flights", "su-stage su-mini")
    return st, credit


def add(b, files, mds, paths):
    """Write /smart-ui/, its Markdown copy, /smart-ui.css and the demo into the build. b is the build module."""
    global VER
    f = facts()
    css = b.minify_css(b.corners_match_levers(b.apple_tracking((STATIC / "smart-ui.css").read_text())))
    VER = hashlib.sha256(css.encode()).hexdigest()[:10]
    body = hero(b, f) + steps_section(b, f) + parts_section(b, f) + rules_section(b, f) + tested_section(b, f) + end_section(b)
    ld = [b.crumbs_ld([("Smart UI", PATH)]),
          {"@context": "https://schema.org", "@type": "WebPage", "name": "Smart UI: answers that show your interface", "url": b.SITE_URL + PATH,
           "description": DESCRIPTION, "isPartOf": {"@type": "WebSite", "name": b.NAME, "url": b.SITE_URL + "/"}}]
    body = f'<link rel="stylesheet" href="/smart-ui.css?v={VER}">\n' + body
    files["smart-ui/index.html"] = b.shell(PATH, SEO_TITLE, DESCRIPTION, body, b.load_docs(), ld, home=True)
    mds["smart-ui/index.md"] = markdown(b, f)
    paths.append(PATH)
    (b.DIST / "smart-ui.css").write_text(css)
    demo_files(b)
