# opendesigner website

The public site for OpenDesigner, light mode only: the project's landing page at `/` (what it is, why, how, examples, install), the documentation directory at `/docs/`, and the showcase at `/showcase/`. It is built from the brand system (`brand/design-system/project/tokens.json`) and the docs in `docs/`.

```
python3 site/build.py          # writes site/dist/ (static HTML, Markdown copies, robots.txt, llms.txt, llms-full.txt, sitemap.xml)
python3 site/build.py --og     # also re-renders the Open Graph images (Playwright + Chrome)
python3 site/check.py          # checks the build: h1, canonical, title and description lengths, structured data, links, anchors, assets
python3 site/check_layout.py   # every page at 13 widths: overflow, inner scroll, symmetry, overlap, targets, controls pinned off their content
python3 site/demo_systems.py   # re-makes the home page's three example systems with the engine (site/demo-systems.json); run it after engine changes
python3 site/deploy.py         # builds and publishes to Vercel (--preview for a preview URL)
```

Before every deploy, open the build locally in the browser pane (`preview_start` with the `opendesigner-site` config in `.claude/launch.json`) and look at it.

- **Hosting:** Vercel, project `opendesigner`, at https://opendesigner.vercel.app (the address is in `site-url.txt`). Deploying needs the Vercel CLI, signed in. Each production deploy also pings IndexNow.
- **Figures** live in `figures/*.html` and are placed in a docs page with `{{figure:name}}` on its own line (contract: `figures/README.md`).
- **Showcase** tiles, tags and the lightbox come from `brand/showcase/` and its Mobbin audit files in `brand/showcase/audit/`.
- **Edit the docs** in `docs/*.md`. Front matter: `title`, `seo_title` (50 to 60 characters), `description` (140 to 160), `section` (Getting started, Guides, Concepts or Reference), `order` and `updated`. Links are root-absolute (`/docs/install/`). Every claim must match the product facts; when in doubt, leave it out.
- **The home page** (`/`) is `home()` in `build.py`, styled by `static/home.css`, with the hero figure `figures/home-hero.html`. Its three examples (Tellwick, Pebbleday, Fernhollow; invented names) are real engine output from `demo_systems.py`: never edit their values by hand. Every claim on it must match `brand/gtm/research/facts.md` and the repo.
- **The docs home** (`/docs/`) is `docs_home()`, the documentation directory that was the home page until 2026-10-15. The introduction is `docs/introduction.md` at `/docs/introduction/`. Its photos are free Unsplash photos, hotlinked from images.unsplash.com as Unsplash asks, shown in a cobalt duotone, with the photographer credited under each.
- **One source:** the HTML pages, their Markdown copies, `llms.txt`, `llms-full.txt`, the sitemap and the structured data all come from the same docs.
- **Fonts** (Hanken Grotesk, Source Code Pro; SIL OFL) are downloaded once into `.cache/` and self-hosted with their licence files.
- **robots.txt and llms.txt** sit at the domain root. Search engines and AI crawlers (including GPTBot, ClaudeBot and PerplexityBot) are allowed on purpose: the project wants to be found and cited.
- **Old addresses** (`/install/`, `/how-it-works/`, `/faq/`, `/what-is-a-design-system/`) redirect permanently to their pages under `/docs/`.
- **To switch to a custom domain:** add it to the Vercel project, put the address in `site-url.txt`, and deploy again.
- **The build reads two images from `brand/kit/`:** the overview screenshot (`_work/overview-top.png`: a 1440 × 900 capture of `brand/opendesigner/overview.html` with Hanken Grotesk loaded; re-capture it after the brand changes) and the brand avatar (`logo/avatar-light-800.png`).
