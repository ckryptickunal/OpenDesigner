"""The component library shop (/library/) and one page per component (/library/<slug>/).

The components live in skills/opendesigner/assets/library/. They are shown live, recoloured by "looks": real engine systems
from site/library_systems.py (site/static/library-systems.css, site/library-looks.json). People add components and one look
to a kit; the kit turns into one prompt for their coding agent.

build.py calls add(); it writes the shop, the component pages, their Markdown copies, /library.css, /library.js, the raw
component files at /library/r/<slug>.html (what the prompts point to) and /library/index.json.
"""
import html
import hashlib
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
LIB = ROOT / "skills/opendesigner/assets/library/components"
STATIC = ROOT / "site/static"
LOOKS = json.loads((ROOT / "site/library-looks.json").read_text())
esc = html.escape
TYPES = {"data": "Data", "chart": "Charts", "form": "Forms", "overlay": "Overlays", "navigation": "Navigation", "feedback": "Feedback",
         "ai": "AI", "commerce": "Commerce", "content": "Content"}
BLURB = {"data": "Tables, feeds, records", "chart": "Meters, bars, trends", "form": "Inputs and pickers",
         "overlay": "Dialogs, drawers, menus", "navigation": "Menus, tabs, steps", "feedback": "Toasts and banners",
         "ai": "Composers and answers", "commerce": "Plans and checkout", "content": "Media and profiles"}  # one line in a tile
INDUSTRY = {"saas": "SaaS", "crm": "CRM", "devtools": "Dev tools", "money": "Personal finance", "food": "Food and delivery", "home": "Smart home"}
STYLES = ["quiet", "dense", "technical", "friendly", "editorial"]
INDUSTRIES = ["finance", "saas", "devtools", "security", "crm", "logistics", "productivity",
              "social", "media", "retail", "food", "travel", "events", "health", "fitness", "money", "education", "home", "games"]
CONSUMER = {"retail", "health", "education", "social", "media", "travel", "food", "fitness", "events", "home", "money", "games"}
VIEW0 = {"narrow": "phone", "medium": "tablet", "wide": "desktop"}  # the view a part opens on, on its card and its page: the one it is designed for
FRAME_W = {"narrow": 400, "medium": 560, "wide": 720}  # card previews: the parts reflow, so a card shows them whole, at a readable size
# The bento: each aisle's cell span (columns x rows) on a 4-column grid, in order; together they fill 4 x 4.
BENTO = [(t, 1, 1) for t in ("data", "chart", "form", "overlay", "navigation", "feedback", "ai", "commerce", "content", "looks")]  # ten equal tiles
BAG = ('<svg class="i-bag" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M6 8h12l-1 12H7L6 8Z" fill="none" stroke="currentColor" '
       'stroke-width="1.6" stroke-linejoin="round"/><path d="M9 8V6.5a3 3 0 0 1 6 0V8" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>')
PLUS = '<svg viewBox="0 0 16 16" width="16" height="16" aria-hidden="true"><path d="M8 3v10M3 8h10" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"/></svg>'
COPY = ('<svg viewBox="0 0 16 16" width="16" height="16" aria-hidden="true"><rect x="5.5" y="5.5" width="8" height="8" rx="1.5" fill="none" stroke="currentColor" stroke-width="1.4"/>'
        '<path d="M10.5 3.5v-.5A1.5 1.5 0 0 0 9 1.5H3A1.5 1.5 0 0 0 1.5 3v6A1.5 1.5 0 0 0 3 10.5h.5" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>')
DEVICES = [("phone", "Phone", 390), ("tablet", "Tablet", 768), ("desktop", "Desktop", 1280)]


# the look parts open in: a calm, regular-density system (owner, 2026-10-23: the dense Billerwick default read as congested)
DEFAULT_LOOK = "nordic"
VER = "dev"  # set by add() from the CSS and JS it writes


# The shelf's first rows (owner, 2026-10-23: "rearrange the components based on the kind that might engage more people"):
# photo-rich, familiar and interactive parts first, consumer and work-tool parts alternating so both audiences find theirs
# in the first screens. A hypothesis until analytics shows which parts people open and add; then order by that.
LEAD = ["social-post", "command-menu", "product-gallery", "stay-card", "ai-composer", "leaderboard",
        "track-list", "receipts-table", "chat-thread", "plan-picker", "activity-rings", "trip-search",
        "media-shelf", "sidebar-nav", "cart-drawer", "card-wallet", "chat-answer", "approval-panel",
        "story-rail", "kanban-column", "event-ticket", "video-player", "menu-item", "savings-goal"]


def components():
    out = []
    for d in sorted(p for p in LIB.iterdir() if p.is_dir() and (p / "meta.json").exists() and (p / "component.html").exists()):
        src = (d / "component.html").read_text()
        out.append({"slug": d.name, **json.loads((d / "meta.json").read_text()), "src": src,
                    "css": "".join(re.findall(r"<style>(.*?)</style>", src, re.S)),
                    "js": "".join(re.findall(r"<script>(.*?)</script>", src, re.S)),
                    "markup": re.sub(r"<style>.*?</style>|<script>.*?</script>", "", src, flags=re.S).strip(),
                    "kb": round(len(src.encode()) / 1024, 1)})
    order = list(TYPES)
    lead = {slug: i for i, slug in enumerate(LEAD)}
    return sorted(out, key=lambda c: (lead.get(c["slug"], len(LEAD)), order.index(c["type"]), c["width"] != "wide", c["name"]))


def photo_credits(c):
    """A facts row naming each Unsplash photographer whose photo the part shows (the Unsplash License asks for none, but it is fair)."""
    ph = [x for x in c.get("photos", []) if isinstance(x, dict) and x.get("author")]
    if not ph:
        return ""
    names = ", ".join(dict.fromkeys(f'<a href="https://unsplash.com/photos/{esc(x.get("page", ""))}">{esc(x["author"])}</a>' if x.get("page") else esc(x["author"]) for x in ph))
    return f'<div><dt>Photos</dt><dd>{names} on <a href="https://unsplash.com">Unsplash</a></dd></div>\n'


def lead(c):
    """The page's first sentence: what the part is, when to use it, and that it takes your design tokens (the line AI answers quote)."""
    return f"{c['name']}: a free component, built on your design tokens, to use {c['use']}."


def page_desc(c):
    """A meta description of 110 to 160 characters that starts with the lead."""
    l = lead(c)
    for d in (f"{l} {c['summary']}", f"{l} One prompt adds it to your project.", f"{l} MIT licensed.", l):
        if 110 <= len(d) <= 160:
            return d
    return fit_desc(l)


def page_title(c):
    """30 to 65 characters, the part first and the brand last."""
    for t in (f"{c['name']}: a free, token-only component | OpenDesigner", f"{c['name']}: a free, token-only component", f"{c['name']} component | OpenDesigner"):
        if 30 <= len(t) <= 65:
            return t
    return f"{c['name']} | OpenDesigner"


def prompt(b, c):
    return (f'Add the OpenDesigner component {c["slug"]} to this project: {b.SITE_URL}/library/r/{c["slug"]}.html. '
            f"Keep its markup and states; map its --ds-* variables to my tokens.")


def ind(x):
    return INDUSTRY.get(x, x.capitalize())


def who(c):
    return "Consumer" if c["type"] == "content" or (set(c["industries"]) & CONSUMER and not set(c["industries"]) & {"finance", "saas", "devtools", "security", "crm"}) else "B2B"


def meta_line(c):
    first = next((ind(x) for x in c["industries"] if x != "any"), "Any product")
    return f'{c["style"].capitalize()} · {esc(first)}'


def stickers(c):
    """Same colours and meanings as the showcase: B2B cobalt, consumer sky, a style ink, an industry paper."""
    w = who(c)
    first = next((ind(x) for x in c["industries"] if x != "any"), "Any product")
    return (f'<span class="sticker{" sky" if w == "Consumer" else ""}" data-icon="{"person" if w == "Consumer" else "building"}">{w}</span>'
            f'<span class="sticker ink" data-icon="brush">{c["style"].capitalize()}</span><span class="sticker paper" data-icon="tag">{esc(first)}</span>')


def demote(markup):
    """A component's own page title (h1 in an app) is an h2 on our pages, which have their own h1."""
    return re.sub(r"<(/?)h1\b", r"<\1h2", markup)


def anchors(markup):
    """Sample links in a component point at "#"; keep only those whose target is inside the same markup."""
    markup = demote(markup)
    ids = set(re.findall(r'\sid="([^"]+)"', markup))
    return re.sub(r'href="#([^"]+)"', lambda m: m.group(0) if m.group(1) in ids else 'href="#"', markup)


def quiet(markup):
    """A preview copy: no ids, label targets or radio-group names, so it never clashes with the live copy on the same page."""
    markup = re.sub(r'\s(id|for|name|aria-controls|aria-activedescendant|aria-labelledby|aria-describedby)="[^"]*"', "", markup)
    # a preview can sit inside a link (an aisle tile): links inside it become spans, since a link in a link breaks the page
    markup = re.sub(r"<a\b([^>]*?)\shref=\"[^\"]*\"", r"<span\1", markup)
    return demote(re.sub(r"<a\b", "<span", markup).replace("</a>", "</span>"))


def live(c, look=DEFAULT_LOOK):
    """The component in a look, inert: in cards and aisles the card is the link. Its own page has the live copy."""
    return (f'<div class="lib-fit" data-w="{FRAME_W[c["width"]]}"><div class="lib-live odl-sys-{look}" inert aria-hidden="true">{quiet(c["markup"])}</div></div>')


def kit_button(slug, name):
    return (f'<button type="button" class="btn kit-add" data-kit-add="{slug}" aria-pressed="false" aria-label="Add to kit: {esc(name)}">{PLUS}'
            f'<span class="t-add">Add to kit</span><span class="t-in">In your kit</span></button>')


def card(b, c, i):
    return (f'<article class="item{" wide" if c["width"] == "wide" else ""}" id="item-{c["slug"]}" data-view0="{VIEW0[c["width"]]}" data-type="{c["type"]}" data-style="{c["style"]}" data-industries="{" ".join(c["industries"])}" data-who="{who(c).lower()}" '
            f'data-search="{esc(" ".join([c["name"], c["summary"], *c["tags"], c["type"], c["style"], *c["industries"]]).lower())}">'
            f'<div class="item-media stage lib-bg">'
            f'<div class="stage-in item-in">{live(c)}</div></div>'
            f'<div class="item-body"><p class="item-tags"><span class="sticker{" sky" if who(c) == "Consumer" else ""}" data-icon="{"person" if who(c) == "Consumer" else "building"}">{who(c)}</span><span class="item-meta">{meta_line(c)}</span>'
            f'<span class="item-views" aria-hidden="true"><i data-v="desktop"></i><i data-v="tablet"></i><i data-v="phone"></i><span class="item-view-t">Desktop</span></span></p><h3><a class="item-link" href="/library/{c["slug"]}/">{esc(c["name"])}</a></h3><p>{esc(c["summary"])}</p></div>'
            f'<div class="item-acts">{kit_button(c["slug"], c["name"])}<button type="button" class="item-copy" data-copy-text="{esc(prompt(b, c))}">{COPY}<span>Copy prompt</span></button></div></article>')


def looks_bar():
    sw = "".join(f'<button type="button" class="look" data-look="{lk["key"]}" aria-pressed="{"true" if lk["key"] == DEFAULT_LOOK else "false"}" title="{esc(lk["plain"])}">'
                 f'<span class="look-sw odl-sys-{lk["key"]}" aria-hidden="true"><i></i></span>{esc(lk["name"])}</button>' for lk in LOOKS)
    return (f'<div class="looks" role="group" aria-label="Try the components in a look">{sw}</div>')


FAB = (f'<button type="button" class="kit-fab" aria-haspopup="dialog" aria-controls="kit" hidden>{BAG}<span>Your kit</span>'
       f'<b class="kit-n" aria-live="polite">0</b></button>')


def kit_ui(b):
    """The kit as a checkout (owner, 2026-10-21: "look and feel like" Razorpay or Dodo Payments, premium): your order on the
    left, how to get it on the right, one big copy button, and a soft ask for a star after the copy, never a wall."""
    data = {"site": b.SITE_URL, "gh": b.GH,
            "looks": {lk["key"]: {"name": lk["name"], "plain": lk["plain"], "commands": lk["commands"], "home": lk["style"] is None} for lk in LOOKS},
            "items": {c["slug"]: {"name": c["name"], "type": TYPES[c["type"]], "kb": c["kb"]} for c in components()}}
    blob = json.dumps(data).replace("</", "<\\/")
    methods = [("parts", "Any coding agent", "Just the parts, as files", b.logo("openai", 18) + b.logo("cursor", 18)),
               ("system", "With a design system", "The look's recipe, then the parts", '<span class="m-sw"></span>'),
               ("claude", "Claude Code", "Install OpenDesigner, then build", b.logo("claude", 18))]
    tiles = "".join(f'<button type="button" class="co-method" role="radio" aria-checked="{"true" if k == "parts" else "false"}" data-out="{k}">'
                    f'<span class="co-m-ic" aria-hidden="true">{ic}</span><span class="co-m-t"><strong>{t}</strong><span>{d}</span></span></button>' for k, t, d, ic in methods)
    return f"""
<dialog class="kit co" id="kit" aria-labelledby="kit-h">
<div class="co-card">
<section class="co-order" aria-labelledby="kit-h">
<div class="co-brand"><span class="co-logo" aria-hidden="true">{b.lockup()}</span><button type="button" class="kit-x" aria-label="Close">×</button></div>
<h2 id="kit-h" tabindex="-1" autofocus>Your kit</h2>
<p class="kit-empty">Nothing here yet. Add parts with <strong>Add to kit</strong>, and a look if you want the whole system.</p>
<ul class="kit-items" aria-label="Parts in your kit"></ul>
<div class="kit-peek" aria-hidden="true"></div>
<div class="kit-look"></div>
<button type="button" class="btn text kit-clear">Empty the kit</button>
<dl class="co-sum">
<div><dt>Parts</dt><dd class="co-n-parts">0</dd></div>
<div><dt>Files to fetch</dt><dd class="co-kb">0 KB</dd></div>
<div><dt>Licence</dt><dd>MIT</dd></div>
<div class="co-total"><dt>Total</dt><dd>Free<small>, now and later</small></dd></div>
</dl>
</section>
<section class="co-get" aria-labelledby="co-get-h">
<h3 id="co-get-h">How do you want it?</h3>
<div class="co-methods" role="radiogroup" aria-labelledby="co-get-h">{tiles}</div>
<div class="co-step1" hidden><p class="co-label">Step 1 · run these once in Claude Code</p><pre class="kit-cmd" tabindex="0">/plugin marketplace add ckryptickunal/OpenDesigner
/plugin install opendesigner@opendesigner</pre><button type="button" class="btn secondary kit-copy-cmd">{COPY}<span>Copy commands</span></button></div>
<div class="co-prompt-wrap"><p class="co-label co-prompt-l">Your prompt</p><pre class="kit-prompt" tabindex="0"></pre></div>
<button type="button" class="co-pay kit-copy">{COPY}<span>Copy prompt</span></button>
<p class="co-trust"><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M8 1.5 13.5 4v3.6c0 3.2-2.3 5.7-5.5 6.9-3.2-1.2-5.5-3.7-5.5-6.9V4z" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/><path d="m5.5 8 1.8 1.8L10.7 6.3" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg>No sign-up. Nothing leaves your browser until you paste it.</p>
<ol class="co-next" hidden><li>Paste it into Claude Code, Codex, Cursor or any coding agent.</li><li>Your agent fetches each part and maps it to your tokens.</li><li>Review the result like any other change.</li></ol>
<div class="co-star" hidden>
<p><strong>Free and open source.</strong> If this saves you time, a star on GitHub helps other people find it.</p>
<div class="co-star-acts"><a class="btn secondary" href="{b.GH}">{b.GH_ICON} Star on GitHub <span class="co-stars" data-stars>{b.STATE["stars"]}</span></a><button type="button" class="btn text co-star-no">Not now</button></div>
</div>
</section>
<div class="co-bar"><span class="co-bar-t"><strong>Free</strong><span class="co-bar-n"></span></span><button type="button" class="co-pay kit-copy">{COPY}<span>Copy prompt</span></button></div>
</div>
</dialog>
<script type="application/json" id="lib-data">{blob}</script>"""


def shop(b, cs):
    n = len(cs)
    by = {t: [c for c in cs if c["type"] == t] for t in TYPES}
    tiles = []
    for t, w, h in BENTO:
        if t == "looks":
            sw = "".join(f'<span class="look-sw odl-sys-{lk["key"]}" aria-hidden="true"><i></i></span>' for lk in LOOKS)
            tiles.append(f'<a class="aisle aisle-looks c{w} r{h}" href="#looks"><span class="aisle-prev aisle-sw">{sw}</span>'
                         f'<span class="aisle-txt"><strong>Looks</strong><span>{len(LOOKS)} systems to try them in</span></span></a>')
            continue
        if not by[t]:
            continue
        pick = next((c for c in by[t] if (c["width"] == "wide") == (w == 2)), by[t][0])
        more = next((c for c in by[t] if c is not pick and c["width"] == "wide"), None) if h == 2 else None  # a tall tile shows two
        tiles.append(f'<a class="aisle c{w} r{h}" href="#shelf" data-aisle="{t}"><span class="aisle-prev">{live(pick)}{live(more) if more else ""}</span>'
                     f'<span class="aisle-txt"><strong>{TYPES[t]}</strong><span>{BLURB[t]} · {len(by[t])}</span></span></a>')
    chips = (f'<button type="button" class="filter is-on" data-type="all" aria-pressed="true">All <span class="num">{n}</span></button>'
             + "".join(f'<button type="button" class="filter" data-type="{t}" aria-pressed="false">{TYPES[t]} <span class="num">{len(by[t])}</span></button>' for t in TYPES if by[t]))
    return f"""
<link rel="stylesheet" href="/library.css?v={VER}">
<div class="shop">
{FAB}
<header class="shop-hero">
<p class="shop-kicker"><span class="sticker lime" data-icon="tag">Free · MIT</span><span>{n} parts · {len(LOOKS)} looks · one prompt</span></p>
<h1>Ready-made parts that take <strong>your design tokens.</strong></h1>
<p class="shop-sub">Pick the parts you need, see them in your look, and give your coding agent one prompt. Nothing to install.</p>
<label class="shop-search"><span class="visually-hidden">Search components</span>
<svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><circle cx="9" cy="9" r="5.5" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="m13 13 4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
<input id="lib-q" type="search" placeholder="Search {n} parts: table, toast, pricing…" autocomplete="off"></label>
<p class="shop-pop"><span>Popular</span>{"".join(f'<button type="button" class="filter" data-q="{q}">{label}</button>' for q, label in (("table", "Tables"), ("toast", "Toasts"), ("command", "Command menu"), ("pricing", "Pricing"), ("chart", "Charts"), ("ai", "AI")))}</p>
</header>

<section class="shop-sec" aria-labelledby="aisles-h">
<div class="sec-head"><h2 id="aisles-h">Browse by aisle</h2><p>{len(TYPES)} kinds of parts. Pick an aisle to see what is in it.</p></div>
<nav class="aisles" aria-label="Aisles">{"".join(tiles)}</nav>
</section>

<section class="shop-sec looks-sec" id="looks" aria-labelledby="looks-h">
<div class="sec-head sec-head-row"><div><h2 id="looks-h">Try them on</h2><p>Every part re-renders in the look you pick. Each look is a real system from the engine.</p></div>
<button type="button" class="btn secondary look-add" data-kit-look="">{PLUS}<span>Add this look to your kit</span></button></div>
{looks_bar()}
</section>

<section class="shop-sec shelf" id="shelf" aria-labelledby="shelf-h">
<div class="sec-head"><h2 id="shelf-h">All parts</h2></div>
<div class="shelf-bar">
<div class="lib-filters" role="group" aria-label="Filter by type">{chips}</div>
<div class="shelf-more">
<label class="lib-field"><span>For</span><select id="lib-who"><option value="">Anyone</option><option value="consumer">Consumer</option><option value="b2b">B2B</option></select></label>
<label class="lib-field"><span>Style</span><select id="lib-style"><option value="">Any</option>{"".join(f'<option value="{s}">{s.capitalize()}</option>' for s in STYLES)}</select></label>
<label class="lib-field"><span>Made for</span><select id="lib-industry"><option value="">Any industry</option>{"".join(f'<option value="{k}">{ind(k)}</option>' for k in INDUSTRIES)}</select></label>
<p class="shelf-count" aria-live="polite"><span class="n">{n}</span> parts</p></div>
</div>
<div class="items">{"".join(card(b, c, i) for i, c in enumerate(cs))}</div>
<p class="lib-none" hidden>No part matches. Clear a filter, or <a href="{b.GH}/issues/new/choose">ask for one</a>.</p>
</section>

<section class="shop-sec how" aria-labelledby="how-h">
<h2 id="how-h" class="visually-hidden">How it works</h2>
<ol class="how-steps">
<li><span class="num">1</span><div><h3>Fill a kit</h3><p>Add the parts you need, and a look if you want the whole system.</p></div></li>
<li><span class="num">2</span><div><h3>Copy one prompt</h3><p>For Claude, Codex, Cursor or any coding agent. It points to small files, so your agent copies a finished part instead of designing one.</p></div></li>
<li><span class="num">3</span><div><h3>They take your tokens</h3><p>Each part uses only <code>--ds-*</code> variables: in an OpenDesigner project they fit as they are.</p></div></li>
</ol>
<p class="h-fine">Free and MIT, never forced: OpenDesigner suggests a part only when it fits what you are building. Every name and number in the parts is invented. Inspired by how <a href="https://opensourceui.in">Opensource UI</a>, <a href="https://ui.shadcn.com">shadcn/ui</a> and <a href="https://magicui.design">Magic UI</a> present components (all MIT); no code was copied. <a href="{b.GH}/blob/main/skills/opendesigner/assets/library/README.md">The format and the rules</a>.</p>
</section>
</div>
{kit_ui(b)}
<script src="/library.js?v={VER}" defer></script>
"""


def fit_desc(text, extra=(" Free and MIT: one prompt adds it to your project, in your own design tokens.", " Free and MIT, in your own design tokens.", "")):
    for e in extra:
        d = text.rstrip(".") + "." + e
        if 110 <= len(d) <= 160:
            return d
    d = text if len(text) <= 160 else text[:157].rsplit(" ", 1)[0] + "…"
    return d if len(d) >= 110 else (d + " A free OpenDesigner component built on design tokens.")[:160]


def detail(b, c, cs):
    devices = "".join(f'<button type="button" role="tab" data-device="{k}" data-w="{w}" aria-selected="{"true" if k == "desktop" else "false"}">{label} <span class="num">{w}</span></button>'
                      for k, label, w in DEVICES)
    states = "".join(f"<li>{esc(s)}</li>" for s in c["states"])
    related = [x for x in cs if x["type"] == c["type"] and x["slug"] != c["slug"]][:3]
    if len(related) < 3:
        related += [x for x in cs if x["style"] == c["style"] and x["slug"] != c["slug"] and x not in related][:3 - len(related)]
    piece = (c.get("source") or "").split("/")[-1]
    piece = " ".join(piece.split("-")[1:]).capitalize()  # "02-fennick-approvals" -> "Fennick approvals"
    src_link = f'Rebuilt from <a href="{b.GH}/tree/main/{c["source"]}">{esc(piece)}</a> in the showcase' if piece else "Made for the library"
    body = f"""
<link rel="stylesheet" href="/library.css?v={VER}">
<div class="shop part">
{FAB}
<nav class="crumbs" aria-label="Breadcrumb"><a href="/library/">Library</a><span aria-hidden="true">/</span><a href="/library/#aisle-{c["type"]}" data-goto-aisle="{c["type"]}">{TYPES[c["type"]]}</a><span aria-hidden="true">/</span><span aria-current="page">{esc(c["name"])}</span></nav>
<div class="part-grid">
<section class="part-view" aria-label="Preview">
<div class="part-tools">
<div class="tablist part-devices" role="tablist" aria-label="Screen size">{devices}</div>
<label class="lib-field"><span>Look</span><select class="part-look">{"".join(f'<option value="{lk["key"]}">{esc(lk["name"])}</option>' for lk in LOOKS)}</select></label>
</div>
<div class="part-stage stage lib-bg">
<div class="part-device" data-device="desktop" data-view0="{VIEW0[c["width"]]}"><div class="part-frame"><div class="lib-live odl-sys-{DEFAULT_LOOK}">{anchors(c["markup"])}</div></div></div>
</div>
<p class="part-hint">It is live: hover, focus and its own controls respond. Actions that would change data (approve, send, delete) are for your app to wire. The width is a real {", ".join(f"{w} px" for _k, _l, w in DEVICES[:-1])} or {DEVICES[-1][2]} px box, shrunk to fit your screen.</p>
</section>
<aside class="part-side">
<div class="stickers">{stickers(c)}</div>
<h1>{esc(c["name"])}</h1>
<p class="part-sum">{esc(lead(c))} {esc(c["summary"])}</p>
<div class="part-prompt"><p class="kicker">Prompt for your coding agent</p><p class="part-prompt-text">{esc(prompt(b, c)).replace("/", "/<wbr>")}</p>
<div class="part-acts">{kit_button(c["slug"], c["name"])}<button type="button" class="copy" data-copy-text="{esc(prompt(b, c))}">{COPY}<span>Copy prompt</span></button></div></div>
<div class="cmd"><code>python3 &lt;skill&gt;/scripts/library.py add {c["slug"]}</code><button class="copy" type="button">Copy</button></div>
<p class="part-cmd-note">With OpenDesigner installed: copies the file and lists any token your project lacks.</p>
<dl class="part-facts">
<div><dt>States</dt><dd><ul class="part-states">{states}</ul></dd></div>
<div><dt>Accessibility</dt><dd>{esc(c["a11y"])}</dd></div>
<div><dt>Fits</dt><dd>{", ".join(ind(x) if x != "any" else "Any product" for x in c["industries"])} · {c["style"].capitalize()} · designed {c["width"]}</dd></div>
{photo_credits(c)}<div><dt>File</dt><dd><a href="/library/r/{c["slug"]}.html">{c["slug"]}.html</a>, {c["kb"]} KB, MIT{"" if not c["js"].strip() else ", with a short script"}</dd></div>
<div><dt>From</dt><dd>{src_link}</dd></div>
</dl>
</aside>
</div>
<details class="part-src"><summary>Source</summary><pre><code>{esc(c["src"])}</code></pre></details>
<section class="part-more" aria-labelledby="more-h"><h2 id="more-h">More like this</h2>
<div class="items">{"".join(card(b, x, i) for i, x in enumerate(related))}</div></section>
</div>
{kit_ui(b)}
<script src="/library.js?v={VER}" defer></script>
"""
    aisle = (TYPES[c["type"]], f"/library/#aisle-{c['type']}")
    ld = [b.crumbs_ld([("Component library", "/library/"), aisle, (c["name"], f"/library/{c['slug']}/")]),
          {"@context": "https://schema.org", "@type": "SoftwareSourceCode", "name": c["name"], "description": lead(c) + " " + c["summary"],
           "url": f"{b.SITE_URL}/library/{c['slug']}/", "codeSampleType": "full", "programmingLanguage": "HTML",
           "license": "https://opensource.org/license/mit", "codeRepository": b.GH,
           "isPartOf": {"@type": "CollectionPage", "name": "OpenDesigner component library", "url": f"{b.SITE_URL}/library/"},
           "keywords": ", ".join(c["tags"])}]
    md = f"# {c['name']}\n\n{lead(c)} {c['summary']}\n\nPrompt: {prompt(b, c)}\n\nStates: {', '.join(c['states'])}.\n\nAccessibility: {c['a11y']}\n\nFile: {b.SITE_URL}/library/r/{c['slug']}.html\n"
    return b.shell(f"/library/{c['slug']}/", page_title(c), page_desc(c), body, b.load_docs(), ld, home=True), md


DESCRIPTION = ("Free, optional components made only of design tokens. Add them to a kit, try them in ten looks, and copy one prompt for your "
               "coding agent.")


def llms_section(site_url):
    """The library's section of llms.txt: the shop and every part, each with its first sentence."""
    return ("## Component library\n\n" + f"- [Component library]({site_url}/library/index.md): {DESCRIPTION}\n"
            + "\n".join(f"- [{c['name']}]({site_url}/library/{c['slug']}/index.md): {lead(c)}" for c in components()))


def add(b, files, mds, paths):
    """Write the shop, the component pages and their files into the build. b is the build module."""
    cs = components()
    global VER
    css_text = ((STATIC / "library-systems.css").read_text() + "\n" + "\n".join(c["css"] for c in cs) + "\n" + (STATIC / "library.css").read_text())
    js_text = ((STATIC / "library.js").read_text() + "\n" + "\n".join(f"/* {c['slug']} */\n{c['js'].strip()}" for c in cs if c["js"].strip()) + "\n")
    # a version in the file names' links, so a deploy never serves a page with last week's script (a reviewer's browser kept an
    # old library.js that had no Consumer filter)
    VER = hashlib.sha256((css_text + js_text).encode()).hexdigest()[:10]
    ld = [b.crumbs_ld([("Component library", "/library/")]),
          {"@context": "https://schema.org", "@type": "CollectionPage", "name": "OpenDesigner component library", "url": f"{b.SITE_URL}/library/",
           "description": DESCRIPTION, "isPartOf": {"@type": "WebSite", "name": "OpenDesigner", "url": f"{b.SITE_URL}/"},
           "hasPart": [{"@type": "SoftwareSourceCode", "name": c["name"], "url": f"{b.SITE_URL}/library/{c['slug']}/", "description": lead(c)} for c in cs]}]
    files["library/index.html"] = b.shell("/library/", "Component library: free parts that take your design tokens", DESCRIPTION, shop(b, cs), b.load_docs(), ld, home=True)
    mds["library/index.md"] = (f"# OpenDesigner component library\n\n{DESCRIPTION}\n\n"
                               + "\n".join(f"- [{c['name']}]({b.SITE_URL}/library/{c['slug']}/) ({TYPES[c['type']]}, {c['style']}): {c['summary']}" for c in cs) + "\n")
    paths.append("/library/")
    for c in cs:
        files[f"library/{c['slug']}/index.html"], mds[f"library/{c['slug']}/index.md"] = detail(b, c, cs)
        paths.append(f"/library/{c['slug']}/")
    (b.DIST / "library" / "r").mkdir(parents=True, exist_ok=True)
    for c in cs:
        (b.DIST / "library" / "r" / f"{c['slug']}.html").write_text(c["src"])
    (b.DIST / "library" / "index.json").write_text(json.dumps(
        [{k: c[k] for k in ("slug", "name", "summary", "type", "style", "industries", "tags", "states", "a11y", "width")}
         | {"url": f"{b.SITE_URL}/library/r/{c['slug']}.html", "page": f"{b.SITE_URL}/library/{c['slug']}/", "prompt": prompt(b, c)} for c in cs], indent=1) + "\n")
    (b.DIST / "library.css").write_text(css_text)
    (b.DIST / "library.js").write_text(js_text)
