# opendesigner website

The public site for OpenDesigner, light mode only: the project's landing page at `/` (what it is, why, how, examples, install), the documentation directory at `/docs/`, and the showcase at `/showcase/`. It is built from the brand system (`brand/design-system/project/tokens.json`) and the docs in `docs/`.

```
python3 site/build.py          # writes site/dist/ (static HTML, Markdown copies, robots.txt, llms.txt, llms-full.txt, sitemap.xml)
python3 site/build.py --og     # also re-renders the Open Graph images (Playwright + Chrome)
python3 site/check.py          # checks the build: h1, canonical, title and description lengths, structured data, links, anchors, assets
python3 site/check_layout.py   # every page at 13 widths: overflow, inner scroll, symmetry, overlap, targets, controls pinned off their content
python3 site/library_systems.py # re-makes the component library's ten looks with the engine (site/static/library-systems.css, site/library-looks.json)
python3 site/library_layout.py  # every library component, unscaled, at the 13 widths of check_layout.py
python3 site/check_chrome.py     # the header and footer are the same on every page, at each width (compares with the home page)
python3 site/demo_systems.py   # re-makes the home page's three example systems with the engine (site/demo-systems.json); run it after engine changes
python3 site/deploy.py         # builds and publishes to Vercel (--preview for a preview URL)
```

## Before every deploy

1. Build: `python3 site/build.py`. After engine changes, run `python3 site/demo_systems.py` first: the home page's example values come only from it.
2. Open the build locally in the browser pane (`preview_start` with the `opendesigner-site` config in `.claude/launch.json`) and look at every page you changed, at full size.
3. `python3 site/check.py` reports no problems.
4. `python3 site/post_change_audit.py` passes every automatic check, and section B of `skills/opendesigner/references/post-change-audit.md` is walked by eye. It runs: `python3 site/check_chrome.py` reports 0 pages whose header or footer differs from the home page. `python3 site/check_layout.py` reports 0 errors at all 13 widths (320 to 1920 px). Read each warning. Library components are scaled down on the site, so the checker skips them there; `python3 site/library_layout.py` checks each one unscaled at the same 13 widths, and must also report 0 errors.
5. Check the real headers. The local server sends none, so a script, style or font the Content-Security-Policy in `vercel.json` blocks only fails once deployed: deploy a preview (`python3 site/deploy.py --preview`), open it, and confirm the console shows no CSP errors.
6. Deploy (`python3 site/deploy.py`). It pings IndexNow. Never run `vercel deploy site/dist` by hand: the build recreates `site/dist/` without the project link, and Vercel then quietly creates a new project named "dist" and deploys there (it happened on 2026-10-18). `deploy.py` copies `site/.vercel/` in first.

What the owner's reviews settled for this site (`_coordination/OWNER-FEEDBACK.md`, 2026-10-14 and 2026-10-15):
- **Outcome first.** Copy leads with what the person gets (a product that looks like it belongs together), then how. Short, plain sentences.
- **One primary action per view.** Secondary actions are quiet text links; places already in the header are not repeated as buttons (preflight 36).
- **Known tools show their own marks** beside their names (`logos.json`, Simple Icons, monochrome). Invented brands never use real marks.
- **Short lines with no widows:** headings and short labels use `text-wrap: balance`, and no line ends on one word (preflight 8).
- **Alignment holds at every width:** siblings share a top edge and height, stacked rows share one centre line, and a pinned control sits on the content's first line (preflight 35 and 38).
- **Corners nest** (owner, 2026-10-21: "this issue is everywhere, fix it everywhere"): a rounded box set close inside another takes the outer radius minus the gap, so the curves run parallel. Photo stages set their padding as `--stage-pad` (in vw, so it means the same on the bezel) and the bezel and picture radii follow from it. `check_layout.py` check 14 (`nested-radius`) fails a page that breaks it.
- **One shell on every page** (owner, 2026-10-21: "top nav changes in each and every page"): the header, footer, docs layout, showcase and library share `--shell` (1200 px), so nothing but the content moves between pages (`check_chrome.py`).
- **Same view outside and inside** (owner, same day): a library card and its component page show a part at the same three widths (desktop 1280, tablet 768, phone 390), open on the same one for the screen, and a click carries the card's view (`?view=`). Hovering a card walks the views with a soft crossfade (fade and a 2 px blur, ease-out, under 300 ms; pointer only; never with reduced motion).
- **Frames fit what they hold** (owner, same day): when a part is narrower than its view, the frame wraps the part instead of leaving it small in an empty field.
- **One frame language**: every framed screen is the frosted-glass bezel (cards, the home page's screens, device views); no black device bezels.
- **Calm, structured pages** (owner, same day: "so cluttered"): one backdrop for a set of cards, stickers below a picture and never on it, one rhythm of section spacing, tiles of one size in a grid.
- **Invented names are checked** with `python3 brand/tools/check_names.py site/dist/index.html --gallery` and a web search.

## How the site is put together

- **Hosting:** Vercel, project `opendesigner`, at https://opendesigner.dev (the address is in `site-url.txt`). The old address, https://opendesigner.vercel.app, redirects there. Deploying needs the Vercel CLI, signed in. Each production deploy also pings IndexNow.
- **Figures** live in `figures/*.html` and are placed in a docs page with `{{figure:name}}` on its own line (contract: `figures/README.md`).
- **Showcase** tiles, tags and the lightbox come from `brand/showcase/` and its Mobbin audit files in `brand/showcase/audit/`.
- **Edit the docs** in `docs/*.md`. Front matter: `title`, `seo_title` (50 to 60 characters), `description` (140 to 160), `section` (Getting started, Guides, Concepts or Reference), `order` and `updated`. Links are root-absolute (`/docs/install/`). Every claim must match the product facts; when in doubt, leave it out.
- **The home page** (`/`) is `home()` in `build.py`, styled by `static/home.css`, with the hero figure `figures/home-hero.html`. Its three examples (Billerwick, Pebbleday, Fernhollow; invented names, each in `brand/showcase/NAMES.md`) are real engine output from `demo_systems.py`: never edit their values by hand. Every claim on it must match `brand/gtm/research/facts.md` and the repo.
- **The docs home** (`/docs/`) is `docs_home()`, the documentation directory that was the home page until 2026-10-15. The introduction is `docs/introduction.md` at `/docs/introduction/`. Its photos are free Unsplash photos, hotlinked from images.unsplash.com as Unsplash asks, shown in a cobalt duotone, with the photographer credited under each.
- **One source:** the HTML pages, their Markdown copies, `llms.txt`, `llms-full.txt`, the sitemap and the structured data all come from the same docs.
- **Fonts** (Hanken Grotesk, Source Code Pro; SIL OFL) are downloaded once into `.cache/` and self-hosted with their licence files.
- **robots.txt and llms.txt** sit at the domain root. Search engines and AI crawlers (including GPTBot, ClaudeBot and PerplexityBot) are allowed on purpose: the project wants to be found and cited.
- **Old addresses** (`/install/`, `/how-it-works/`, `/faq/`, `/what-is-a-design-system/`) redirect permanently to their pages under `/docs/`.
- **To switch to a custom domain:** add it to the Vercel project, put the address in `site-url.txt`, and deploy again.
- **The build reads two images from `brand/kit/`:** the overview screenshot (`_work/overview-top.png`: a 1440 × 900 capture of `brand/opendesigner/overview.html` with Hanken Grotesk loaded; re-capture it after the brand changes) and the brand avatar (`logo/avatar-light-800.png`).
