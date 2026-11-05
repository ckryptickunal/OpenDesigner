# Changelog

All notable changes to OpenDesigner are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/). Detailed reasons for each product decision are in [`_coordination/DECISIONS.md`](_coordination/DECISIONS.md).

<!-- Every push that changes what people get adds one entry per change: `- **Short title** (YYYY-MM-DD). One to three plain sentences.` The date is the day it lands on main, and the website's changelog uses it. Keep each entry under 400 characters; put the full story in the commit or pull request. `python3 tools/changelog_check.py` checks the format. -->

## [Unreleased]

### Added

- **Brand colors from your logo** (2026-11-05). `engine.py sketch --logo logo.png` (or an SVG) shows up to three colors from the logo, how much of it each one covers, and the command that confirms one. White, black and see-through parts are left out, and nothing is recorded until the person picks.
- **Build writes only the exports your platforms use** (2026-11-05). `engine.py build` writes CSS and Tailwind for the web, Swift for iOS and Compose for Android, and names what it left out. Figma, Paper, DTCG and artifact files are written for every platform, and `export --format all` still writes everything.
- **More icons drawn like your own** (2026-11-05). If you have a few icons and need more, `illustrate.py icons` reads how yours are drawn (badge, glyph box, line weight, colour), ranks 24 open icon sets by how close they are, and redraws the glyphs you pick the same way. They are shown next to yours first, and each licence is recorded.
- **A site brief for sites that persuade** (2026-11-05). A landing page or marketing site now gets five questions at the broad level: the goal and how it is counted, the roles to convince, the proof, how people find it, and its kinds of pages. Each answer is drafted from your words and repo first. PRODUCT.md shows each line, or "Not enough information" with its question, and the proof is never made up.
- **Two colour rules for every project** (2026-11-05). New house standards: colours with a known meaning keep it (approved green, rejected red, pending amber, info blue, and well-known apps in their own colour), and a product never uses pure white and pure black together. `engine.py validate`, `review` and `preflight.py html` enforce the second; three library parts now draw their codes in near-black.
- **Kerning and letter spacing, checked in every project** (2026-11-05). A new guide, `preflight/references/kerning.md`, lists the type-spacing mistakes that keep coming back and how to avoid each. `preflight.py html` now flags kerning switched off, tracking in px or %, untracked capitals and words split into letters without their kerning (check 57).
- **Rules for references, samples and content** (2026-11-05). `making.md` now asks for a board of shipped samples to pick from before a new direction, live measurement instead of thumbnails, principles from a reference instead of its page, a content list that "less text" never cuts, and one system for every figure. Moving calls to action are banned.

### Fixed

- **The website and docs say what is true today** (2026-11-05). The security page names the 0.2.0 release, the engine page lists `version`, `detect`, `research` and owner notes, and counts, the home page's examples and the showcase's tags match the repo again. Release lines on the site now come from the git tag, so they can't fall behind.
- **The worked examples match the engine again** (2026-11-05). The three systems in `examples/` were rebuilt from their `state.json`, and `python3 tools/build_examples.py --check` now fails, in CI too, when the engine writes something they do not show. The old replay script, which could wipe them, is gone.
- **The link check knows the website's pages** (2026-11-05). A link like `/tour/` in the website's docs is now checked against the pages `site/build.py` makes, so real pages pass and a mistyped one still fails.
- **The palette page shows its contrast checks** (2026-11-05). The table under the shades was always empty because the engine sent no colour pairs ([#47](https://github.com/ckryptickunal/OpenDesigner/issues/47)). Each option now carries the pairs people read most, in every mode and measured the same way as `engine.py validate`, and the page works out each ratio from the colours it shows.
- **The footer links every docs page again** (2026-11-05). The footer had dropped to 20 links. It now links every docs page by section from every page, so search engines and AI crawlers reach them, and each label still fits on one line down to 320 px.

## [0.2.0]: 2026-11-05

The first tagged release: the research base, the synthesis that turns it into an interview, eight skills, the engine and host packaging. Copies installed before it report 0.1.0; update to get everything below.

### Added

- **A shorter README and home page that claim only what ships** (2026-11-05). Two ways in (fix what you built, build a system), what happens every round, and the status. Supporting paragraphs under the home page headings are gone, and the library count says 82.
- **The research steps in the main flow** (2026-11-05). `engine.py research market`, `positioning` and `directions` run the competitor table, the positioning and the direction board, and the skill asks for them before any colour. PRODUCT.md gains its own Positioning section. `OD:direction` records a pick. An AI-made photo is named to the person, never captioned on the page.
- **Landing pages get room and a hero** (2026-11-05). A marketing page now gets spacious spacing, 48 to 56px buttons and its own fluid display scale, 96 to 120px for the hero. Capitals never take negative tracking, text keeps three greys, and the system writes one container, columns, gutters and a reading measure.
- **A button shape you choose holds** (2026-11-05). Feel words no longer make buttons square or pill; those are choices. A chosen shape is stored as the exact radius and locked, and typed values such as "6px", "400/500" or "major third" are stored as values. Each page's caps (8 sizes, 3 weights, 2 families) are written down for the review to check.
- **A protocol in every project** (2026-11-05). `init` writes `opendesigner/PROTOCOL.md`: six steps with owner gates, and checks every round, shown as screenshots before and after. `engine.py review` says when code uses no tokens or the system is behind the code. A note said twice becomes a rule in `RULES.md`; landing pages get marketing questions.
- **Research before colour, then three directions** (2026-11-05). Research now ends with a table of competitors, linked, with their colours, fonts and button shapes, to show before any colour. Then comes a positioning you confirm, and three directions that each change the ground, fonts, photo style, accent and layout, on one board with licensed stock photos checked for brand logos.
- **A stronger audit, every round** (2026-11-05). The review now measures what an owner kept catching by eye: tight capitals, lost kerning, art drawn through text, bars covering text, mixed alignment, boxes that jump between tabs, controls that do nothing, and too many sizes, buttons and fonts. audit.md lists the checks to run on every draft.
- **How it works is easier to find** (2026-11-04). The "How OpenDesigner works" page is now linked from the top of the home page, two home page sections, the footer on every page, the top of the docs sidebar, the docs home and the Introduction.
- **How OpenDesigner works, on one page** (2026-11-02). A new page at opendesigner.dev/tour/ draws the whole system in live HTML: the two ways in, the engine's dials, the files you keep, what protects you, and how a confirmed mistake becomes a check. Every number on it is read from the repository when the site is built.
- **Reads your repo before asking** (2026-11-02). A new `engine.py detect` reads the product's name, where it runs, a brand colour, the font, dark mode and the project's phase from your files. `init` and `sketch` record each one as assumed, with its source, never over an answer you gave, and the sketch turns each answered question into one line to confirm.
- **Purpose, goals and market in PRODUCT.md** (2026-11-02). PRODUCT.md gains Purpose and goals, Phase and Market sections, each saying "Not enough information" until your words or the research fill them. The user research gains a market topic: competitors, what they all do, the gap and an analogous product, with sources. Principles are drafted from the goals.
- **The project's phase sets what comes first** (2026-11-02). A new question, Q-scope-07: an idea, being built, close to launch, or live, read from the repo first. An idea starts with its purpose and an analogous product, close to launch with an audit, copy and preflight, and live with the audit and governance.
- **An audit for products that are already built** (2026-11-02). `references/audit.md` is the first step for fixing a product someone already built. It goes through every button, font, weight, size, colour, gap, corner and state, and writes each problem as one row: where it is, what is wrong in plain words, the fix, and the rule it breaks with its source.
- **The review counts what competes on a page** (2026-11-02). `review.py check` now counts what any page can be judged on without a design system: filled buttons competing in one view (new review case MS-16), typefaces, weights, colour families, gray text colours and colours typed twice. Each is a warning that names its source.
- **Every fix says where its rule comes from** (2026-11-02). `review.py compare` shows the source of each fix, such as "From: preflight 36", and ends with "Keep the fix, keep today's, or try another?". `making.md` asks the same of every option shown on a built page.
- **The evals page compares fairly and shows every run** (2026-11-02). The headline compares OpenDesigner with a plain AI only on the 7 tasks a plain AI can attempt (92% with, 66% without). Every saved run is listed, including the two taste tasks that scored 0%, and the limits come first.
- **A product direction proposal** (2026-11-02). Sixteen notes on direction are in `_coordination/OWNER-FEEDBACK.md`, answered by a proposal in `_coordination/proposals/`. The field plan records 59 stars and 4 forks.
- **A star chart in the README** (2026-10-31). The README shows OpenDesigner's GitHub stars as its own chart, in light and dark. `tools/star_chart.py` redraws it from GitHub every 3 hours, and `tools/gh_snapshot.py` saves the repo's GitHub numbers as JSON.
- **Preflight measures flashing** (2026-10-28). `preflight.py video` now checks the final video against the WCAG 2.2 flash limit (SC 2.3.1) with ffmpeg, and `--flash-where` saves the worst moment. 8 of 73 Instagram reels we measured flashed over the limit. Checklist item 49 lists the usual causes.
- **User research before the defaults** (2026-10-26). After the sketch, OpenDesigner offers to research who the users are. After one yes it searches with the tools it has, cites every finding, and turns them into recommended answers to the audience questions. Nothing changes without the person's yes. See `references/research.md`.
- **Library pages with less to read** (2026-10-25). Each part's page shows its name, one line, Add to kit and Copy prompt. The full description, install command and credits fold into Details. Agents still get the full text in each page's Markdown copy.
- **Product analytics with PostHog** (2026-10-24). The site counts visits without cookies and records where each visit came from. Session recording runs only after a visitor says yes, with every input masked. `docs/PRIVACY.md` says what is counted.
- **A Taste Index of a look you love** (2026-10-24). `taste_index.py` describes one site's look from a few pages or a screenshot: colours, type, components, motion, voice and a Never list, each marked measured or inferred. It may keep exact colours and font names, never logos, names, images or copy. The system follows it only when the person chooses it.
- **Forty consumer parts in the component library** (2026-10-24). The library grows from 42 to 82 parts, adding social, media, shopping, travel, health, money and learning. The shop gains a Consumer / B2B filter.
- **The component library, reworked to a craft standard** (2026-10-23). All 82 parts were rebuilt with more room, one accent colour, Lucide icons and real Unsplash photos. Card previews load as you scroll, so the shop lays out in 70 ms instead of 830 ms.
- **Every push to main goes live by itself** (2026-10-23). `site/autodeploy.py` runs on the maintainer's Mac. When main has been still for 5 minutes, it builds, checks and publishes the site. A failed deploy leaves the live site as it was.
- **Six measurement fixes in reference intake** (2026-10-23). Reading a site now catches borders drawn by pseudo-elements, keeps looping animations apart from UI motion, ignores the browser's default link blue, and reads density from the page's spacing, not only body size.
- **Preview a value before recording it** (2026-10-23). `engine.py set ... --dry-run` and `pick ... --dry-run` show each token's old and new value and any check it would change, and write nothing.
- **The changelog is its own page** (2026-10-23). It moved from /docs/changelog/ to /changelog/, and the old address redirects. Each day shows its highlights, with its commits folded underneath.
- **Agent evals for the taste index** (2026-10-23). Two cases, `taste-leaves-out` and `taste-all-past`, check that the style gallery respects a person's taste poll.
- **Lists and sidebars breathe** (2026-10-23). The 24 px accessibility floor is a minimum, not a size. `making.md` section 12 now asks for rows at control height and room between icon and label, and preflight check 48 looks for it.
- **A changelog anyone can check** (2026-10-22). The changelog page opens with the current version, how to check yours and how to update. `/version.json` and an Atom feed give tools the same facts.
- **Markdown for agents** (2026-10-22). A request for `text/markdown` gets the page's Markdown copy. Browsers and search engines still get HTML.
- **Agents can find and read the site** (2026-10-22). robots.txt allows search and AI crawlers, the home page links llms.txt and its Markdown copy, and `/.well-known/agent-skills/` lists all eight skills as zips.
- **The analogous product** (2026-10-22). Before designing, OpenDesigner names a product that already solved the same interface problem, confirms it with the person and studies it as an inspiration.
- **Before and after in the README** (2026-10-22). Two new panels show the invoices page with its seven measured issues beside the fixed page, and six parts from the component library.
- **A social preview for every page** (2026-10-22). Each shared docs link shows its own card with its section and title. Cards are about 60 KB instead of 800 KB.
- **The home page says what OpenDesigner is** (2026-10-22). The headline names the category, "Design systems for AI coding tools", so search engines and AI answers can tell what the page is about.
- **The review skill catches labels that break across lines** (2026-10-22). `review.py check` reports a button, tab or chip label that wraps onto a second line. Overflow checks missed these.
- **An optional component library** (2026-10-22). Finished components built only on the engine's `--ds-*` tokens, so each takes the project's colours, type, spacing and corners. `library.py` lists, suggests, adds and checks them, and the website shows them as a shop at /library/.
- **The audit, as it happens, on the home page** (2026-10-21). The before-and-after section plays once: a scan line finds each issue on an invented invoicing page, then a green line fixes it with the system's tokens. Both pages are live HTML, and reduced motion keeps it still.
- **The demo's fixed page is a bento** (2026-10-21). Each tile holds one figure with a small chart, and red is kept for late money.
- **Agent notes stay out of design decisions** (2026-10-21). `engine.py set profile.seen.<name> ...` stores a note without writing a decision.
- **The trial ledger** (2026-10-21). `_coordination/TRIAL-LEDGER.md` lists every correction a person typed in a demo trial, each with its fix. Trial 1 gave 15, and they became rules in `making.md` section 12.
- **The quality bar and good practices** (2026-10-21). `references/quality.md` sets floors and a nine-line scorecard judged against shipped products. `references/practices.md` lists the tools an agent looks for at the start.
- **Correct is not finished** (2026-10-21). After building, the skill opens the result, compares it blind with three shipped products and reports a score. A built product is audited before it is redesigned.
- **Before and after, on the person's own page** (2026-10-21). `review.py compare` writes one `compare.html` with the page today, the audit drawn on it and the fix, with measured numbers before and after.
- **A ready-made variant picker** (2026-10-21). `assets/picker.js` switches between 2 to 5 options on a review copy of a page, by key or by `?v=` in the address.
- **The changelog and a contribute guide on the website** (2026-10-21). The changelog page is built from this file on every publish, and `/docs/contribute/` sums up how to help.
- **One line asking people to recommend OpenDesigner** (2026-10-21). It appears once per project, only after OpenDesigner has helped, and never next to another question.
- **Each system knows which OpenDesigner made it** (2026-10-21). `state.json` records the release that made and last built the system. Commands say once when it is out of date, and `engine.py version` prints both releases.
- **Evals, published with the numbers** (2026-10-20). Agent evals run eight small tasks with and without OpenDesigner (91% against 58% at the time). Design evals run the engine on 18 fixed briefs (a CI job is set up for them), and checker evals test the review checks on planted pages.
- **Showcase round 4** (2026-10-18). Components, app screens and footers were rebuilt and judged blind against shipped products. Pieces that didn't reach 4 of 5 are hidden until they do.
- **Taste: the poll, the taste index and the taste card** (2026-10-15). The person rates 20 to 30 shipped screens, and the result recommends the eight dials. The taste index merges every taste signal with red lines, and DESIGN.md opens with a five-line taste card.
- **Defaults for dense B2B work tools** (2026-10-15). When the audience is `dense`, the engine fills tighter corners, row heights, one selection blue and tabular digits, only where the person hasn't answered. On the web, no text style is smaller than 12 px.
- **Painting skill** (2026-10-15). `opendesigner-paint` paints original art and films in code in the brand's palette (watercolour, pointillism, charcoal, sketch, woodcut, 2D cel). `paint.py` turns the system into a painting brief, sets up a film project and brings the result into the app with a reduced-motion still.
- **Review skill** (2026-10-15). `opendesigner-review` checks a built UI at every size, theme and state, and reports with evidence. `probe.js` measures the running page, and `review.py` checks the results against the floors and the tokens.
- **Preflight skill** (2026-10-15). `opendesigner-preflight` is the last look at a page, video, deck or card before it is shared: yes-or-no checks, and `preflight.py` for type, fonts and video frames.
- **House standards** (2026-10-15). 455 rules from the owner's non-negotiable sources. The engine applies and locks them per project, the interview skips what they settle, and `review` flags code that breaks one.
- **Lessons from the owner's website review** (2026-10-15). Preflight checks 35 to 42 and review cases MS-05 and CV-04: alignment at every width, one primary action, no widows and whole labels on phones.
- **Your own design-system page** (2026-10-14). Every `build` rebuilds `opendesigner/overview.html`: colours, type, spacing, corners, motion and components on one page. Anything only a person can give says "Not enough information".
- **The system as a Claude Design System artifact** (2026-10-14). `engine.py export --format artifact` writes the tokens, brand book and previews ready to publish with the Artifact tool.
- **Illustration skill** (2026-10-14). `opendesigner-illustrate` finds open-licence illustrations, ranks them, recolours them to the tokens and applies them, with a licence ledger. Its directory covers 44 sources with their licences.
- **Making and reviewing pages** (2026-10-13). `references/making.md` guides agents after the system exists: the first draft on the tokens, one round of feedback at a time, and options on a review copy.
- **Learning wiki** (2026-09-27). `learn/` holds what OpenDesigner learned from 99 trusted sources, with 53 topic pages. `tools/wiki.py` adds, checks and maps it.
- **Decision Cards from the wiki** (2026-09-27). 164 cards with 253 proposed changes. Three are adopted so far; the rest wait in `synthesis/QUESTIONNAIRE.md`.
- **Research search** (2026-09-27). `tools/jev_nav.py find` also searches the house standards and ranks results with BM25.
- **Synthesis** (2026-09-24). The ontology (271 nodes), the interview (193 questions), the eight dials with their formulas, and the decision graph.
- **Research base** (2026-09-23). 18 research lanes written as 352 Decision Cards, with 2,740 sources logged in `traces/`.
- **Benchmark** (2026-09-23). 25 public design systems compared with real values in `benchmarks/`.
- **Starter design artifacts** (2026-09-23). A DTCG token set with 126 contrast-checked pairs, and four HTML artboards in `design/`.
- **Coordination system** (2026-09-23). `tools/od.py` and `_coordination/` let parallel human and AI sessions work on one repo.
- **Research tools** (2026-09-23). `tools/jev_nav.py` for search, citation checks and the decision graph, and `tools/check_links.py` for Markdown links.
- **Product specification** (2026-09-23). `docs/SPEC.md`.
- **Skills** (2026-09-23). `opendesigner`, `opendesigner-extract`, `opendesigner-extend` and `opendesigner-export`, in the Agent Skills format.
- **Host packaging** (2026-09-23). A Claude plugin and marketplace, an Agent Plugins manifest, claude.ai skill zips and a ChatGPT Project bundle.
- **Engine** (2026-09-23). `engine.py` for state, generation, validation and exports.
- **Community and repository health** (2026-09-23). README, CONTRIBUTING, Code of Conduct, security policy, issue forms, CI and `llms.txt`.
- **Licenses** (2026-09-23). MIT for code, skills and data; CC BY 4.0 for research and documentation.

### Fixed

- **Counts in the docs match the files again** (2026-11-02). Review case, export format, skill and library counts in the docs, SPEC, AGENTS.md and llms.txt now match the repo.
- **A calmer site footer** (2026-11-02). The footer went from 8 columns and 42 links to 4 columns and 20 links. Every link fits on one line down to 320 px.
- **Favicon on dark browser tabs** (2026-10-28). The favicon switches to the dark mark when the browser tab is dark, so its squares stay visible.
- **Five small slips on the home page and in the library** (2026-10-26). "1 false alarms" became "1 false alarm", the audit's check marks no longer cover text, library dates use 2026 weekdays, and the header fits at 320 px again.
- **Library cards in Safari** (2026-10-25). 53 of 82 shop cards drew their part as a thin column in Safari. Cards now scale with a transform, and `site/check_browsers.py` checks every card in WebKit and Chrome.
- **The library's activity part no longer copies Apple** (2026-10-24). `activity-rings` used Apple's rings and words. It is now `daily-goals`: flat bars for steps, active minutes and water in the system's accent.
- **A corner radius between the steps builds** (2026-10-24). `engine.py set radius.control 10` used to stop the next build. A radius between the steps now gets its own step, and `set` refuses values that can't be a radius.
- **Two agent eval graders** (2026-10-23). `no-identity-copy` now checks that the skill ran, and `extend-rounder` no longer fails a reply for listing the files a rebuild wrote.
- **Agent evals run the cases you ask for** (2026-10-23). `tools/agent_evals.py` takes several cases or tags, `--list` shows what matches, and a filter that matches nothing stops with an error instead of running nothing.
- **The option gallery is never empty** (2026-10-23). A taste red line now judges only the dials the style directions differ on. If every direction is past a line, all show with a warning.
- **The home audit counts up as it scans** (2026-10-22). Issues are numbered in reading order, and on phones the view moves to each issue as it is named.
- **The home page paints faster on phones** (2026-10-22). The hero photo is preloaded, and site.css shrank from 37 KB to 26 KB.
- **Fixes from the fresh verifier's re-check** (2026-10-21). `review.py compare` meets 4.5:1 contrast, the variant picker can't show two options at once, and Markdown copies no longer show raw `{{...}}` placeholders.
- **Screen-reader-only text is not "clipped"** (2026-10-21). The review probe no longer reports visually hidden labels as clipped text.
- **The glossary has one source again** (2026-10-21). `synthesis/glossary.json` is the file to edit, and `check_glossary.py --check` is set up to run in CI. A rebuild would have deleted 13 terms.
- **Apple's letter spacing and corners change the files they promise to** (2026-10-21). `size-table` now uses Apple's SF Pro tracking table, and `squircle-enhance` adds Apple's continuous corner to the CSS, Tailwind, Figma and Swift exports.
- **Another company's colour is never your brand** (2026-10-20). Asked for "Stripe's exact purple", the skill once saved it as the person's brand. A colour named as another company's is now only a reference.
- **Four checker bugs found by the checker evals** (2026-10-20). Contrast after a semi-transparent element, a page with nothing to focus reported as a keyboard trap, and screen-reader-only text flagged by the layout check.
- **Renaming a system leaves no old export behind** (2026-10-15). `export --format dtcg` keeps only the current system's files.
- **Accessibility claims match the engine** (2026-10-15). The docs no longer promise reduced-transparency or high-contrast modes the engine doesn't make. Glass surfaces get a solid fallback.
- **A brand colour the person typed is never replaced** (2026-10-15). The sketch used to swap light brands like yellow #FFE500 for olive. A typed hex now stays exact, and only fills that carry text use a readable shade.
