# opendesigner website

The public site for OpenDesigner, built from the brand system (`brand/design-system/project/tokens.json`) and the content in `content/`.

```
python3 site/build.py          # writes site/dist/ (static HTML, robots.txt, llms.txt, llms-full.txt, sitemap.xml)
python3 site/build.py --og     # also re-renders the Open Graph images (Playwright + Chrome)
SITE_URL=https://your.domain python3 site/build.py   # for a custom domain (also writes CNAME)
```

- **Hosting:** Vercel, project `opendesigner`, at https://opendesigner.vercel.app (the address is in `site-url.txt`). `python3 site/deploy.py` builds and uploads the static files; `--preview` gives a preview URL instead. Needs the Vercel CLI, signed in.
- **Edit content** in `content/*.md` (front matter: `seo_title` 50 to 60 characters, `description` 140 to 160). Every claim must match the product fact sheet; when in doubt, leave it out.
- **One source:** the HTML pages, their Markdown copies, `llms.txt`, `llms-full.txt`, the sitemap and the structured data are all made from the same content.
- **Fonts** (Hanken Grotesk, Source Code Pro; SIL OFL) are downloaded once into `.cache/` and self-hosted with their licence files.
- **robots.txt and llms.txt** sit at the domain root, where crawlers and AI tools look for them. Search engines and AI crawlers (including GPTBot, ClaudeBot and PerplexityBot) are allowed on purpose: the project wants to be found and cited.
- **To switch to a custom domain:** add it to the Vercel project, put the address in `site-url.txt`, and deploy again.
- **The build reads local files** that aren't in git: the overview screenshot (`brand/kit/_work/overview-top.png`, made by `brand/design-system/export_kit.py`) and the full-size mockup renders. Build on the maintainer's machine.
