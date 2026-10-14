# Changelog

All notable changes to OpenDesigner are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/). Detailed reasons for each product decision are in [`_coordination/DECISIONS.md`](_coordination/DECISIONS.md).

## [Unreleased]: planned as 0.1.0

The first public version: the research base, the synthesis that turns it into an interview, and the first skills, engine and host packaging.

### Added

- **Making and reviewing pages** (lane L22, `research/L22-making-and-review.md`): what to do after the system exists.
  - A guide for agents, `skills/opendesigner/references/making.md`: the first draft built on the tokens, one round of feedback at a time, options on a review copy of the page with the current version kept, what stays the same between sections, checking the rendered page in the person's own window, finished interface shown inside a page, sections that hold the page, and figures drawn as graphics. It ends with the mistakes an AI builder made in that project, and what to do when the person has to repeat a note.
  - A cohesion audit template, `assets/output/COHESION-AUDIT.md`, for a page that stopped looking like one page.
  - Nine Decision Cards (DC-L22-01 to -09) from the decision trail of one marketing-site build, with 22 rows of evidence on existing cards, standards and rules, and six items for the maintainer to decide. No standard, question, default or engine code changed.
  - The main and extend skills point to the guide, and `docs/HOW-IT-WORKS.md` section 9 describes it.
- **Your own design-system page** (`opendesigner/overview.html`, `engine.py overview`): every `build` rebuilds it, so it grows with the system.
  - It shows the cover, brand book, colors per theme with contrast, headings h1 to h6, every text style, spacing, corners, depth, motion, core components, the 14 brand assets and a timeline of decisions.
  - Each area says **Chosen**, **Picked for you** or **Default**. Anything only a person can give (a logo, a voice guide, what the product is for) shows as **Not enough information**, with the question that fills it.
  - `build` also fills every visual template with the person's system in `opendesigner/preview/`, so nobody sees sample data.
- **The system as a Claude Design System artifact** (`engine.py export --format artifact`, also part of `build`): `opendesigner/build/artifact/project/` holds tokens in the artifact's list format, the brand book from DESIGN.md, a cover and a button preview. It is ready to publish with the Artifact tool, and the files stay in the repository.
- **Illustration skill** (`skills/opendesigner-illustrate/`): finds open-licence illustrations for a product's empty states, onboarding, error pages, sign-in, hero and feature tiles, ranks them, recolors them to the design tokens and applies them.
  - `scripts/illustrate.py` searches Openverse, Wikimedia Commons, Open Doodles, Lukasz Adam and CocoMaterial (and Iconify's multicolor sets for small spot art). It is the one skill allowed to use the network (owner decision, 2026-09-28): `search` and `fetch` call the agent-fetch sources over HTTPS, 3 MB per file at most, and `--offline` prints the requests for sandboxes without internet. It ranks by relevance, licence, format and style fit, and draws contact sheets so the model and the person judge by eye.
  - Recoloring keeps each shape's lightness and moves it to a token ramp: grays to neutral, the main hues to accent, accent2 and accent3, and skin tones are kept. It writes six variants (`themed`, `light`, `dark`, `tint`, `mono`, `swap`). The themed one follows light and dark mode through CSS variables.
  - Every SVG passes an allow-list sanitizer first: no scripts, animation, foreign content or remote loads, in markup or CSS. An independent review found four bypasses in the first deny-list version; all are now regression tests.
  - `apply` writes an SVG, HTML or React component, scopes ids, class names and CSS to the drawing, sets `aria-hidden` or a label, and keeps a licence ledger with `ATTRIBUTION.md`. The first piece applied locks the project to one illustration style.
  - **Illustration directory:** `synthesis/illustration-sources.json` (copied into the skill as `references/sources.json` by `build_data.py`) covers 44 sources (flat scenes, people, doodles, spot art and emoji, 3D, animation, pattern generators and open museum collections), each with its licence, credit rule, formats, search link, filters, tips and step-by-step navigation, and lists 12 more that were checked and left out, with the reason. Every source was checked live on 2026-09-28. `build_data.py` also renders `references/directory.md` from it. `illustrate.py directory --open` opens one page with filters and a single search box for every site, and `illustrate.py sources --q "<words>"` prints each site's search link. `references/searching.md` says where to look first, how to word a search, what each file format allows, and how an agent moves through each kind of source.
  - Sources have three access levels: agent fetches (the script searches and downloads over HTTPS: Openverse, Wikimedia Commons, Open Doodles, Lukasz Adam, CocoMaterial, Iconify), agent may browse (bots allowed, no connector), and you download (the site forbids bots).
  - `references/sources.json` records each source's licence as read on 2026-09-28. unDraw, Storyset, ManyPixels, Blush, DrawKit and SVG Repo forbid automated search or download, so the person downloads from them and `illustrate.py add` brings the file in.
  - It adapts ideas from existing tools, without copying code: from Icons8's agent skills, one style per project and a list of what each screen needs before any search; from CaesiumY's unDraw skill, a warning when a recolor changes nothing and never keeping a catalogue.
- **Learning wiki** (`learn/`, lane L19): the knowledge OpenDesigner draws from sources its owner trusts, kept as an independent, self-updating knowledge base.
  - It covers 99 sources, each with a verified analysis, and an OpenWiki Markdown wiki with 53 cross-source topic pages.
  - `learn/MAP.md` indexes it by area, standard, card and question. `learn/IMPROVING.md` explains how to change the app from it.
  - The pipeline runs through `tools/wiki.py` (`add`, `fetch`, `check`, `ingest`, `trace`, `cite-check` with TypeSafe's Jev, `standards`, `map`, `proposals`, `next`, `upstream`) and five saved workflows in `.claude/workflows/`.
  - OpenWiki is pinned in `learn/openwiki.lock.json` and checked weekly in CI.
  - The rules are in `docs/KNOWLEDGE.md`.
- **House standards** (`synthesis/standards.json`, v2): 455 rules from the owner's non-negotiable sources (Emil Kowalski's writing and skills, Sonner, animations.dev, Vaul).
  - Each rule is citation-checked and reviewed.
  - The engine applies and locks them for each project's platforms and stack, including new tokens such as the 0.97 press scale.
  - Commands: `engine.py standards [--update]`, and `standard override|restore|add|remove`, which covers project standards, per-path overrides and `--beats`.
  - Constraints stop values that break a rule (no ease-in curves on UI; UI motion stays under 300 ms unless a standard names the exception).
  - The interview skips questions a standard settles and refuses options that break one.
  - `review` flags code that breaks a standard. DESIGN.md carries a short summary, with the full list in `opendesigner/standards.md`.
- **Decision Cards from the wiki:** 164 in `research/L19-learning-wiki.md`, with 253 proposed changes and 75 conflicts with older research.
  - Three cards are adopted so far; the rest are listed as pending in `synthesis/QUESTIONNAIRE.md` for lane L20.
  - "Now / As it grows" notes for 30 high-impact questions appear under each option.
- **Research search:** `tools/jev_nav.py find` also searches the house standards and ranks with BM25. It judges each card by its recommended default and marks older cards the house supersedes.

- **Research base:** 18 finished research lanes (L00 to L18, with L12 still open) written as 352 Decision Cards, with 2,740 sources logged in `traces/`, including rejected ones.
- **Benchmark:** 25 public design systems compared with real values in `benchmarks/`.
- **Synthesis:** the building-block ontology (271 nodes in 10 layers), the guided interview (193 questions on 27 screens, 6 of them planned and skipped until built, with Quick, Standard and Expert modes), the eight dials with generation formulas and 13 famous systems as dial recipes, and the decision graph (352 decisions, 465 dependencies, 12 cycles).
- **Starter design artifacts** in `design/`: a DTCG 2025.10 token set with 126 contrast-checked pairs, and four HTML artboards.
- **Coordination system** for parallel human and AI sessions: `tools/od.py`, `_coordination/PROTOCOL.md`, the board, heartbeats, inbox and decision log.
- **Research tools:** `tools/jev_nav.py` (status, search, citation check, card export, decision graph) and `tools/check_links.py` (offline Markdown link check).
- **Product specification:** `docs/SPEC.md` (copied from `synthesis/OPENDESIGNER-SPEC.md`).
- **Skills:** `opendesigner` (the interview), `opendesigner-extract`, `opendesigner-extend` and `opendesigner-export`, in the Agent Skills format, with generated copies in `.agents/skills/` and `.claude/skills/`, knowledge files built from the synthesis, and 8 JSON-fed visual templates.
- **Host packaging:** a Claude plugin and marketplace (`.claude-plugin/`), an Agent Plugins manifest (`plugin.json`), claude.ai skill zips built by `tools/build_dist.py`, and a ChatGPT Project bundle (`chatgpt-project/`).
- **Engine** (being finished): `skills/opendesigner/scripts/engine.py` for state, generation, validation and exports.
- **Community and repository health:** README, CONTRIBUTING, Code of Conduct (Contributor Covenant 2.1), security policy, support, governance, citation file, issue forms, pull request template, labels, CI, `llms.txt`, `funding.json`, a social preview image, a sponsorship plan, and docs (`docs/HOW-IT-WORKS.md`, `docs/RESEARCH.md`, `docs/FAQ.md`, `docs/GITHUB-SETTINGS.md`, `docs/SEED-ISSUES.md`).
- **Licenses:** MIT for code, skills and data; CC BY 4.0 for research and documentation.
