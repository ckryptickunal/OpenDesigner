# opendesigner website

The public site for OpenDesigner: a documentation directory with a landing page, light mode only. It is built from the brand system (`brand/design-system/project/tokens.json`) and the docs in `docs/`.

```
python3 site/build.py          # writes site/dist/ (static HTML, Markdown copies, robots.txt, llms.txt, llms-full.txt, sitemap.xml)
python3 site/build.py --og     # also re-renders the Open Graph images (Playwright + Chrome)
python3 site/check.py          # checks the build: h1, canonical, title and description lengths, structured data, links, anchors, assets
python3 site/deploy.py         # builds and publishes to Vercel (--preview for a preview URL)
```

Before every deploy, open the build locally in the browser pane (`preview_start` with the `opendesigner-site` config in `.claude/launch.json`) and look at it.

- **Hosting:** Vercel, project `opendesigner`, at https://opendesigner.vercel.app (the address is in `site-url.txt`). Deploying needs the Vercel CLI, signed in. Each production deploy also pings IndexNow.
- **Figures** live in `figures/*.html` and are placed in a docs page with `{{figure:name}}` on its own line (contract: `figures/README.md`).
- **Showcase** tiles, tags and the lightbox come from `brand/showcase/` and its Mobbin audit files in `brand/showcase/audit/`.
- **Edit the docs** in `docs/*.md`. Front matter: `title`, `seo_title` (50 to 60 characters), `description` (140 to 160), `section` (Getting started, Guides, Concepts or Reference), `order` and `updated`. Links are root-absolute (`/docs/install/`). Every claim must match the product facts; when in doubt, leave it out.
- **The landing page** is in `build.py` (`landing()`). Its photos are free Unsplash photos, hotlinked from images.unsplash.com as Unsplash asks, shown in a cobalt duotone, with the photographer credited under each.
- **One source:** the HTML pages, their Markdown copies, `llms.txt`, `llms-full.txt`, the sitemap and the structured data all come from the same docs.
- **Fonts** (Hanken Grotesk, Source Code Pro; SIL OFL) are downloaded once into `.cache/` and self-hosted with their licence files.
- **robots.txt and llms.txt** sit at the domain root. Search engines and AI crawlers (including GPTBot, ClaudeBot and PerplexityBot) are allowed on purpose: the project wants to be found and cited.
- **Old addresses** (`/install/`, `/how-it-works/`, `/faq/`, `/what-is-a-design-system/`) redirect permanently to their pages under `/docs/`.
- **To switch to a custom domain:** add it to the Vercel project, put the address in `site-url.txt`, and deploy again.
- **The build reads local files** that aren't in git: the overview screenshot (`brand/kit/_work/overview-top.png`, made by `brand/design-system/export_kit.py`) and the brand avatar. Build on the maintainer's machine.
