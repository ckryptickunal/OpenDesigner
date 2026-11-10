# B2B and enterprise website study: what the best sites do, and what to change on ours

Study date: 2026-10-14. Sources: about 25 Mobbin searches (website sections and full web screens) across heroes, "how it works", features, enterprise and security, "for teams", trust without logos, open-source and pricing, install, contact, docs homes, docs pages, changelogs, footers, galleries and small details. Our site was checked in the local build (`site/dist`, served on 127.0.0.1) at 1440 and 390 px wide: the landing page `/`, `/docs/enterprise/` and `/showcase/`.

Rules for this file: Mobbin is cited only by `mobbin_url`. No Mobbin image is saved in the repo. Other companies are named here only as evidence; none of their names, logos or screens belong in our designs. Every claim about OpenDesigner comes from `brand/gtm/research/facts.md`, `site/docs/`, `SECURITY.md` or `docs/PRIVACY.md`.

**Caveat on the site state.** Another session was editing `site/` while this study ran. `site/dist` was rebuilt mid-study (for a moment it held only `fonts/`), and the showcase gained filter pills after my first screenshots. Findings below were re-checked against the build at about 20:30 on 2026-10-14. I did not check the live Vercel deployment.

---

## 1. What premium B2B and dev-tool sites consistently do (ten lines)

1. **The headline says what it is and who it is for, in plain words.** An audience pill or a bold audience list sits next to it. Evidence: https://mobbin.com/sites/sections/0eb5722a-4576-49bd-9d04-b2d9556690fc (one-line "open source ... alternative"), https://mobbin.com/screens/b57adf85-2368-4479-9449-a41ae8ccacbe (audiences named in bold), https://mobbin.com/sites/sections/8fa276bd-351b-4988-bdb2-dd8b84661988 (audience pill above the headline).
2. **They show the real product, not icons.** The first image is the actual interface, real code or real terminal output. Evidence: https://mobbin.com/screens/887269c3-bc0d-4090-aaef-13c4462a1b53, https://mobbin.com/sites/sections/38557cd6-0834-4d5a-b186-89ac968d8332, https://mobbin.com/sites/sections/363363b9-a122-4092-8c41-962f962e6a46.
3. **Two calls to action, one primary, in sentence case.** One is "start" and the other is "docs" or "talk to sales". Evidence: https://mobbin.com/sites/sections/2adf9d3a-e8dd-44c5-b8fc-2414bd1dcd65, https://mobbin.com/sites/sections/330752c2-0212-49ba-a09a-ea977cbab9b7, https://mobbin.com/sites/sections/962f4563-2dbe-4876-8944-1805c15b2608.
4. **For developer tools, the install command is itself a call to action.** It is shown verbatim with a copy icon. AI-era tools add "copy prompt". Evidence: https://mobbin.com/sites/sections/e9c68c38-072b-403d-8888-26042d246b35, https://mobbin.com/sites/sections/a2004615-5fee-4e7d-9f84-602f3f1ab1f0, https://mobbin.com/screens/2c39a77f-3e18-453a-ac4e-42b993ea2552, https://mobbin.com/sites/sections/9c8b6826-afc3-44f1-bd37-5914534f2921.
5. **Structure comes from small mono labels and hairlines, not from shadows.** Uppercase mono kickers, section counters, full-height column hairlines and "+" crosshair corners keep pages flat. Evidence: https://mobbin.com/sites/sections/01de94b2-ba4b-4b69-9a08-49a96aef9fca, https://mobbin.com/sites/sections/9562a5cb-3484-42f4-a4c4-10e45c9853ce, https://mobbin.com/sites/sections/363363b9-a122-4092-8c41-962f962e6a46, https://mobbin.com/sites/sections/f413db09-0a6f-44df-ae35-125468d270dc.
6. **Enterprise has its own door.** There is an "Enterprise" item in the top nav, and the section is a scannable list of controls. Sales contact is routed apart from product support. Evidence: https://mobbin.com/sites/sections/e72d1d36-a761-4557-b655-d2797beb7abb, https://mobbin.com/sites/sections/ac340129-6796-44e2-b04e-76a5789a8dce, https://mobbin.com/sites/sections/d6c2b93f-12e3-4d57-88c9-0753507e3abc, https://mobbin.com/sites/sections/87a2d31e-7955-4ab1-961c-086ba5f43f62.
7. **Honest status labels instead of overclaiming.** The best sites write "pending", "coming soon", "limited release", "in progress" and "Beta" right on the feature. Evidence: https://mobbin.com/sites/sections/4d7ccf09-e699-46f8-b59c-a0b8ac745dec (a certification marked pending), https://mobbin.com/sites/sections/bf694248-99fd-43f5-8c69-7aa1d027848c (coming soon), https://mobbin.com/sites/sections/503872ca-2331-4a6f-8cc6-66889b8586f8 (in progress), https://mobbin.com/screens/54bba256-7c7c-44cf-9024-5feedbc3ac3e (Beta pill).
8. **Without customer logos, proof comes from things a reader can check.** That means real outputs, repo facts in mono, a compatibility line and a dated changelog. Evidence: https://mobbin.com/sites/sections/984d6cc2-b46e-4321-8376-cf8d1c444807 (real findings with file paths), https://mobbin.com/sites/sections/597abd57-613c-46d9-885b-c93c29e64133 ("works with" line instead of logos), https://mobbin.com/sites/sections/56c0a44a-16ef-4f35-ae19-dd3f87be370e (version + date changelog strip).
9. **Docs homes start from tasks.** They have search with a key hint, 3 to 6 start cards or audience columns, and a quickstart with real code. The full index lives in the sidebar, not on the page. Evidence: https://mobbin.com/sites/sections/7786124b-cdf7-424f-82e1-e8df8654efe5, https://mobbin.com/sites/sections/bd371d08-9be8-4b31-bda3-695534d63804, https://mobbin.com/screens/1b39571a-c929-4ba6-934c-9786fc50681d.
10. **Footers are dense directories with a trust column.** They hold Security, Privacy, Legal and Changelog links, plus one live signal such as status or version. Evidence: https://mobbin.com/sites/sections/bc31e448-f56a-4b11-939d-55d0b472ebec, https://mobbin.com/sites/sections/e182cf94-4363-4964-ae63-16b5b7791961, https://mobbin.com/sites/sections/82d7b249-da3b-4e9f-9b61-7f8f21dc94e3.

---

## 2. Rules per section type, with evidence

### Heroes
- **Left-aligned or centred, but always one idea.** Headlines run two to three lines. A one-line sub says how it works, and big product visuals sit below or to the right. Evidence: https://mobbin.com/screens/887269c3-bc0d-4090-aaef-13c4462a1b53, https://mobbin.com/sites/sections/cbac56f2-5cdf-45a1-814d-83c855d8f552.
- **The kicker chip carries a live or factual detail, not a slogan.** Evidence: https://mobbin.com/screens/b57adf85-2368-4479-9449-a41ae8ccacbe (a mono metric inside the chip), https://mobbin.com/sites/sections/e9c68c38-072b-403d-8888-26042d246b35 ("open source, MIT licence" in mono).
- **A photo hero works when real UI floats on it.** It does not work when the photo is the whole message. Evidence: https://mobbin.com/screens/4ed803f3-8304-40bd-965d-30a508632fcb (a product input centred on a warm, blurred photo), https://mobbin.com/sites/sections/42d730f3-3f64-4a53-8214-e4bd4201ab6c.
- **Compatibility shown as a plain line, not a logo wall.** Evidence: https://mobbin.com/sites/sections/597abd57-613c-46d9-885b-c93c29e64133, https://mobbin.com/sites/sections/0eb5722a-4576-49bd-9d04-b2d9556690fc.
- **Buttons are sentence case. Mono uppercase is kept for small labels.** The one exception, an all-mono button set, is a deliberate brand voice: https://mobbin.com/sites/sections/d3f78b8c-e9a1-4349-975a-949a9eeb51f6. Most others use sentence case: https://mobbin.com/sites/sections/8fa276bd-351b-4988-bdb2-dd8b84661988, https://mobbin.com/sites/sections/2adf9d3a-e8dd-44c5-b8fc-2414bd1dcd65.

### "How it works"
- **3 or 4 numbered steps, each paired with a real artifact** (a UI fragment, a command or a file). Evidence: https://mobbin.com/sites/sections/a52dff05-8f33-4ec6-92ce-ab2fdd3c550b, https://mobbin.com/sites/sections/27bf1023-ba04-4af0-ae50-5fad11815613, https://mobbin.com/sites/sections/363363b9-a122-4092-8c41-962f962e6a46.
- **Tabs over one large product view.** Each stage swaps the same frame, which is better than three tiny cards. Evidence: https://mobbin.com/sites/sections/451211a8-f24c-418c-b3da-dd010168621f, https://mobbin.com/sites/sections/f83459c1-5d49-4927-866d-7d2788c41352.
- **Plain, specific step copy works even with no image.** Evidence: https://mobbin.com/sites/sections/2cfd3169-f61f-4ca5-bd2a-67627febbc84.

### Feature sections
- **Real UI fragments beat icon grids.** The icon-and-two-lines grid reads as interchangeable. Real fragments: https://mobbin.com/sites/sections/d71c5b4f-5f52-407a-a347-84394e4b3a45, https://mobbin.com/sites/sections/c1122cc1-4b0f-4794-8df3-3a05305a4ca1. Interchangeable icon grids: https://mobbin.com/sites/sections/5b9cd8b3-d6f3-4983-a9f3-fe36687c2bcc, https://mobbin.com/sites/sections/1c441853-c43c-446e-89a0-28eec955725d.
- **A concrete number or data label can replace the icon.** Evidence: https://mobbin.com/sites/sections/940a02f4-40af-4d1c-a41e-0a4d48d9ecf4, https://mobbin.com/sites/sections/0daad8f7-cdde-4ef2-a454-2a26d2bbe0a5.
- **Bold lead-in plus one plain sentence per bullet**, next to a terminal showing a real run. Evidence: https://mobbin.com/sites/sections/01b8c5f1-917e-4593-952b-30765b5bd642 (a "no vendor lock-in" section; the closest analogue to OpenDesigner's "files in your repo").

### Enterprise, security and governance
- **A scannable grid or table of controls, with limits footnoted.** Evidence: https://mobbin.com/sites/sections/ac340129-6796-44e2-b04e-76a5789a8dce.
- **Each control is a small tag plus one plain sentence.** Evidence: https://mobbin.com/sites/sections/b07657a6-9166-45b2-bdc3-3fc8e29e4534, https://mobbin.com/sites/sections/c4f88312-45a4-4a30-b485-a8684024a06b.
- **Name the data boundary concretely** (where data lives, which regions, what is never sent). Evidence: https://mobbin.com/sites/sections/8f745107-850b-4391-890e-658c005b2170, https://mobbin.com/sites/sections/205955a6-96d6-44fc-84c6-80a66c23c15e, https://mobbin.com/screens/8ae8b188-4ba3-4aab-bf47-d7496b9d63cb.
- **Show the control as real UI where possible.** Evidence: https://mobbin.com/sites/sections/40d49384-06e0-4398-86e0-f848ce7d9ba5, https://mobbin.com/sites/sections/7cc957b1-e446-49e9-8313-d23e837b446c.
- **Badge each control with its plan or status.** Evidence: https://mobbin.com/sites/sections/d6c2b93f-12e3-4d57-88c9-0753507e3abc.

### "For teams"
- **Short and concrete: one sentence on who it is for, one contact button, five or six check lines.** One line should be about rollout help. Evidence: https://mobbin.com/sites/sections/c603fba7-9f62-4666-9109-26f84f912d90.
- **Facts grouped as privacy and security, integrations and controls.** Evidence: https://mobbin.com/sites/sections/29a0d1af-ee1c-4bb3-9035-69f773c47418.
- **Roles and governance shown as the real screen.** Evidence: https://mobbin.com/sites/sections/a1c006a2-6308-47b3-a6e5-5258edfc065b, https://mobbin.com/sites/sections/d12976d7-7c69-4c67-b0fa-53cf44e78dcd.

### Trust without logos
- **Repo facts in a mono stat row with vertical dividers.** Evidence: https://mobbin.com/sites/sections/6632f117-5eb8-4cb3-978c-7c23da4d762f.
- **Version and "last updated" as plain metadata.** Evidence: https://mobbin.com/sites/sections/ed9803be-e9b9-4764-8209-c53eb1dbd454, https://mobbin.com/sites/sections/b01fcb69-642b-42c6-97f8-7e5d8530c390.
- **Real outputs as the proof.** Evidence: https://mobbin.com/sites/sections/984d6cc2-b46e-4321-8376-cf8d1c444807.
- **A changelog strip on the home page shows the product is alive.** Evidence: https://mobbin.com/sites/sections/44c38fe6-0c18-4730-a93d-0baf7dbd4f50, https://mobbin.com/sites/sections/56c0a44a-16ef-4f35-ae19-dd3f87be370e.

### Free, open source and enterprise contact
- **The open-source column says what you take on yourself.** That covers self-hosting, upgrades and community-only support. Its call to action is "Go to repo". Evidence: https://mobbin.com/sites/sections/923ce9ff-1152-446a-8654-ce0b7ff3e537.
- **Enterprise is one quiet band under the free option, not a pricing wall.** Evidence: https://mobbin.com/sites/sections/1974c03f-c0ff-4f8e-ae30-250355677442, https://mobbin.com/sites/sections/24e3855a-a55a-46a4-b500-7a8a3311efd0, https://mobbin.com/sites/sections/5297ece1-f418-4646-af39-e8b993c49d4f.
- **The closing band repeats the install command and states the licence and what needs an account.** Evidence: https://mobbin.com/sites/sections/a2004615-5fee-4e7d-9f84-602f3f1ab1f0.
- **Route people: sales one way, product help the other, and security documents named.** Evidence: https://mobbin.com/sites/sections/87a2d31e-7955-4ab1-961c-086ba5f43f62, https://mobbin.com/sites/sections/90aff9e8-a83b-42eb-8f10-8640f0e83ed4.

### Install
- **Per-host rows: icon, name, one action per row, on hairlines.** Evidence: https://mobbin.com/sites/sections/b99fe27f-0826-490b-8dee-8fb256bfc740.
- **Numbered setup steps with the exact commands**, including an "install agent skills" step. Evidence: https://mobbin.com/screens/2c39a77f-3e18-453a-ac4e-42b993ea2552, https://mobbin.com/screens/54bba256-7c7c-44cf-9024-5feedbc3ac3e.

### Docs home
- **Audience columns of plain links, plus "try it" with real output.** Evidence: https://mobbin.com/sites/sections/7786124b-cdf7-424f-82e1-e8df8654efe5.
- **Three start cards, then architecture and use-case groups.** The sidebar has an "Additional resources" group with changelog, FAQ and trust. Evidence: https://mobbin.com/sites/sections/bd371d08-9be8-4b31-bda3-695534d63804.
- **A quickstart card that pairs text with a real code block, and quick links below.** Evidence: https://mobbin.com/screens/fff7b2c5-a015-4027-ab22-901ef51647f2.

### Docs pages
- **The copy button lives in a header bar above the code, never over the text.** Evidence: https://mobbin.com/screens/bfd57dde-b051-45b3-b084-d10dc1ce497a, https://mobbin.com/screens/a6a9687e-bcda-48eb-bd0c-a92d4e0e000b.
- **Each page shows its source files and last-updated date.** Evidence: https://mobbin.com/screens/b3c5d5e4-feea-41e1-94c3-31057a74b3f5.
- **"Was this page helpful?", "Suggest edits" and a next-page link.** Evidence: https://mobbin.com/sites/sections/d15a2ed8-56af-42a0-ad11-7e70c7598865.

### Changelog
- **Date in a left gutter, a title, one or two lines, a type tag and an optional real screenshot.** Evidence: https://mobbin.com/sites/sections/e864a8c7-8fb0-4c1a-82ef-ac735534e6f4, https://mobbin.com/sites/sections/d8e9eea2-16bd-459e-ae0b-dbd3a8239516, https://mobbin.com/sites/sections/a85703b4-636f-407a-8b4f-cade72d6f909 (mono ISO dates).

### Footers and small details
- **Mono column headings, a Legal and Trust column, and one live signal line.** Evidence: https://mobbin.com/sites/sections/f413db09-0a6f-44df-ae35-125468d270dc, https://mobbin.com/sites/sections/59cdf49d-e039-4904-a90e-aebfb09a9771.
- **Bracketed or numbered mono kickers**, such as "[ OPEN SOURCE ]" or "05. CREATING DOCS". Evidence: https://mobbin.com/sites/sections/3acb1f30-cc02-4b04-9dbe-b6425a2b55ed, https://mobbin.com/sites/sections/4adc125a-a0ca-449d-8e47-a778090ef517.
- **Faint grid backgrounds with dot or cross intersections.** Evidence: https://mobbin.com/sites/sections/cbc26de4-8163-49e9-93f9-90ec90f3d9e9, https://mobbin.com/sites/sections/9562a5cb-3484-42f4-a4c4-10e45c9853ce.

### Galleries (for `/showcase/`)
- **Filters first, then cards: the image is cropped to the product, with a title and one line.** Evidence: https://mobbin.com/sites/sections/6dddcdbd-0c26-4214-aa39-988b04c2f511, https://mobbin.com/sites/sections/2e609ed3-249a-49f0-afff-f1d2d15791b1, https://mobbin.com/sites/sections/54de3b10-b16f-44ba-918c-700e4d3df1dc.

---

## 3. Our site against the evidence

### What already works
- **The hero figure is the strongest thing on the site.** It shows a real interview question with four drawn options and the suggested one with its reason. Next to it are the `tokens.css` lines it writes and a review panel naming a drift, all floating on a photo. That is rule 2 (real product) and the photo-plus-UI pattern (https://mobbin.com/screens/4ed803f3-8304-40bd-965d-30a508632fcb).
- **"Where it fits in your process" (Start, Use, Keep)** pairs each step with a real artifact. It matches https://mobbin.com/sites/sections/27bf1023-ba04-4af0-ae50-5fad11815613.
- **"What you have after the first run"** lists real files with plain meanings. This is the proof by artifact that https://mobbin.com/sites/sections/01b8c5f1-917e-4593-952b-30765b5bd642 uses.
- **"Where it stands" and the enterprise page's "Where it does not fit yet"** are more candid than most references (rule 7). Keep them.
- **The enterprise doc's figures** carry the Workshop-style teaching well: the annotated decision-log entry, and "Lock what must not drift" against "Leave the brand color unlocked" using OpenDesigner's own three brand-color entries.
- **The details match the references**: mono uppercase kickers, hairline rows, the "Works with" line (https://mobbin.com/sites/sections/597abd57-613c-46d9-885b-c93c29e64133) and footer columns with mono headings.
- **The showcase now has filter pills** (All, B2B, Consumer, Enterprise and others), which matches the gallery rule.

### What reads as amateur or AI-made, most damaging first
1. **The top bar is collapsed to 8 px on every page, at both widths.** No logo, no nav and no GitHub button are visible. Cause: `site/static/figures.css` line 98 defines `.bar { height: 8px; overflow: hidden }` for a figure's progress bar. `build.py` line 763 appends `figures.css` after `site.css`, so this rule overrides the sticky header's `.bar`. Measured: `header.bar` is 8 px tall. `figures.css` is uncommitted, so this is probably local-only (not checked on the live site). Every reference keeps a visible bar with brand, nav and a primary action.
2. **"What it changes for you" is visibly broken.** `.role` is a two-column grid (112 px and 1fr), but each card has four children (photo, heading, list, link). The bullet list lands in the 112 px photo column, and the right side sits mostly empty. Measured: the `ul` is 112 px wide at 1440. At 390 the "Guide for ..." link overlaps the bullet text.
3. **The same 20 doc links appear three times on the landing page**: the sidebar, a numbered "Browse the docs" list (01 to 20 with section tags), and the footer. A numbered 20-row index reads like generated filler. References give 3 to 8 task entry points instead (https://mobbin.com/sites/sections/bd371d08-9be8-4b31-bda3-695534d63804, https://mobbin.com/screens/1b39571a-c929-4ba6-934c-9786fc50681d).
4. **The hero has three buttons in three styles, all in uppercase mono.** "Copy the Claude Code install" hides the actual command behind a label. References use two sentence-case buttons and show the command itself (https://mobbin.com/sites/sections/e9c68c38-072b-403d-8888-26042d246b35, https://mobbin.com/sites/sections/a2004615-5fee-4e7d-9f84-602f3f1ab1f0).
5. **There is no enterprise or teams door.** The top nav is Docs, Install and Showcase. Teams are only a sidebar guide. Rule 6.
6. **The GitHub card leads with "Stars 1" and "Forks 1"** in large mono, the numbers that matter least to a buyer, shown biggest. References show meaningful facts, such as version and last updated (https://mobbin.com/sites/sections/ed9803be-e9b9-4764-8209-c53eb1dbd454), or real outputs.
7. **Mobile hero problems.** At 390 px the hero composite is about 27 px wider than the screen and gets clipped (`.hero-comp` right edge measured at 417 px). The intro chip breaks into three stacked pieces, with the dot alone on its own line.
8. **The overview screenshot in "After the first run" is too small to read** (its text renders at about 5 px). References show the product large and legible (https://mobbin.com/screens/887269c3-bc0d-4090-aaef-13c4462a1b53).
9. **The Copy button covers code text** on long lines (for example the `engine.py standard add ... --why` line on `/docs/enterprise/`). `.code pre` has right padding, but a horizontally scrolling line still runs under the absolutely positioned button.
10. **The showcase opens on "All 54", which leads with consumer pieces**: an architecture studio, tea, a festival, a fashion house and a teen fintech app. The enterprise and B2B pieces (Orvita, Orrery, Isobath) come later.
11. **Judgment call (for Kunal): the docs sidebar also appears on the landing page.** The hero gets only about 60% of the width, and the home page reads as a docs page. Marketing homes in the references are full width, and docs homes carry the sidebar. Kunal asked for a documentation directory, so this is his call.
12. **Check: the hero's suggested answer names two real design systems** ("like Primer and Atlassian"). It is live text from the question data, but `brand/README.md` says never to put another company's name in any image. Decide whether hero figures count as images.

---

## 4. Change list (each one small; the top 5 are marked ★)

| # | File and place | Change | Why | Reference |
|---|---|---|---|---|
| ★1 | `site/static/figures.css` lines 98-99, and `site/figures/zoom-levels-ladder.html` (the only figure using it) | Rename the figure's `.bar` and `.bar > span` to `.fig-bar`. Optionally scope all figure-kit classes under `.fig-*` so they cannot collide with site classes | The header is invisible on every page | https://mobbin.com/screens/887269c3-bc0d-4090-aaef-13c4462a1b53 |
| ★2 | `site/build.py` `landing()`, roles markup (`<article class="role">`); `site/static/site.css` line 116 | Wrap the heading, list and link in one `<div>`, so the grid has two children: photo and body | The bullets are crushed into the photo column | https://mobbin.com/sites/sections/29a0d1af-ee1c-4bb3-9035-69f773c47418, https://mobbin.com/sites/sections/c603fba7-9f62-4666-9109-26f84f912d90 |
| ★3 | `site/build.py` `landing()` `.cta-row`; `site/static/site.css` `.btn` (line 68) | Keep two buttons, "Install" and "Read the docs", in sentence case (keep mono for kickers only). Replace the ghost button with a visible command chip: `/plugin marketplace add ckryptickunal/OpenDesigner`, a copy icon, and a small "Other AI tools →" link to `/docs/install/` | The real command builds more trust than a label, and three button styles dilute the hero | https://mobbin.com/sites/sections/e9c68c38-072b-403d-8888-26042d246b35, https://mobbin.com/sites/sections/a2004615-5fee-4e7d-9f84-602f3f1ab1f0, https://mobbin.com/sites/sections/2adf9d3a-e8dd-44c5-b8fc-2414bd1dcd65 |
| ★4 | `site/build.py` `shell()` `.top-nav` (line 338), plus a new landing band before the FAQ | Add a "For teams" nav item linking to `/docs/enterprise/`. Add a quiet band: kicker "For design-system teams", one sentence, five check lines taken from `enterprise.md` (decision log, locks, house and project standards, `engine.py review`, DTCG 2025.10), and two links: "Read the team guide" and "Tell us what your team needs" (the issue forms). Keep its last line honest: "No team has piloted it yet." | Enterprise buyers need a door, and the references all have one | https://mobbin.com/sites/sections/c603fba7-9f62-4666-9109-26f84f912d90, https://mobbin.com/sites/sections/5297ece1-f418-4646-af39-e8b993c49d4f, https://mobbin.com/sites/sections/e72d1d36-a761-4557-b655-d2797beb7abb |
| ★5 | `site/build.py` `landing()` `#docs` section | Replace the 20-row numbered list with 3 or 4 start cards: "Install in your AI tool", "Your first design system", "For design-system teams" and "Engine commands". Keep the full index in the sidebar and on `/docs/` | It removes the triple repetition and the generated-index look | https://mobbin.com/sites/sections/bd371d08-9be8-4b31-bda3-695534d63804, https://mobbin.com/sites/sections/7786124b-cdf7-424f-82e1-e8df8654efe5, https://mobbin.com/screens/1b39571a-c929-4ba6-934c-9786fc50681d |
| 6 | `site/build.py` `landing()` `#status`, `.ghcard` `gh-stats` | Show Licence (MIT), Release ("none yet, 0.1.0 planned"), Open issues (live) and Last push (live). Leave the live star count in the header button | Lead with what a buyer checks, and stay honest | https://mobbin.com/sites/sections/ed9803be-e9b9-4764-8209-c53eb1dbd454, https://mobbin.com/sites/sections/6632f117-5eb8-4cb3-978c-7c23da4d762f |
| 7 | `site/static/figures.css` line 87 media query; `site/static/site.css` `.intro` (lines 97-100) | At 420 px and below, give the hero cards `min-width: 0; max-width: 100%`. At 560 px and below, make `.intro` a block with the dot inline and "Read how" as an inline link | Removes the clipping and the broken chip on phones | (a bug fix; the references keep heroes inside the viewport) |
| 8 | `site/build.py` code-block markup; `site/static/site.css` `.code` (lines 78-80) | Move "Copy" into a header row above the `pre`, with a small language or file label on the left | The button stops covering code | https://mobbin.com/screens/bfd57dde-b051-45b3-b084-d10dc1ce497a, https://mobbin.com/screens/a6a9687e-bcda-48eb-bd0c-a92d4e0e000b |
| 9 | `site/build.py` `landing()` `#output` | Make the screenshot about 60% of the split, or crop it to a legible region (the status lines and one palette row) at 2x | Product UI must be readable to count as proof | https://mobbin.com/sites/sections/451211a8-f24c-418c-b3da-dd010168621f |
| 10 | `site/build.py` `showcase()` filters | Open on the "B2B" filter, or sort B2B and Enterprise pieces first within each section. Keep the "AI agents made these" caveat | The first screen an enterprise buyer sees should be work for them | https://mobbin.com/sites/sections/6dddcdbd-0c26-4214-aa39-988b04c2f511, https://mobbin.com/sites/sections/2e609ed3-249a-49f0-afff-f1d2d15791b1 |
| 11 | `site/build.py` `footer()` | Add a "Trust" column: Security policy (`SECURITY.md`), Privacy (`docs/PRIVACY.md`), Licence (`LICENSE`, `LICENSE-CONTENT`) and Changelog (`CHANGELOG.md`). Cap the docs columns at 4 links each, plus "All docs". Add a mono line: "Version 0.1.0, not released yet · Updated {TODAY}" | This is where buyers look for these documents, and it ends the third repetition of the doc list | https://mobbin.com/sites/sections/bc31e448-f56a-4b11-939d-55d0b472ebec, https://mobbin.com/sites/sections/e182cf94-4363-4964-ae63-16b5b7791961 |
| 12 | `site/docs/enterprise.md`, after the intro | Add an at-a-glance table: "What a team gets" and "Status" (Works / Works, not tested in CI / Not yet). Rows are listed in section 5C below | Lets a buyer see everything in 20 seconds, with honest status labels | https://mobbin.com/sites/sections/ac340129-6796-44e2-b04e-76a5789a8dce, https://mobbin.com/sites/sections/d6c2b93f-12e3-4d57-88c9-0753507e3abc |
| 13 | `site/build.py` `landing()`, a closing band after the FAQ | One line, "Free and open source (MIT). OpenDesigner doesn't include the AI: your chat goes to your own AI provider." Then the command chip from ★3 and "Read the docs" | A clear last step, with the cost boundary stated (facts.md section 7) | https://mobbin.com/sites/sections/a2004615-5fee-4e7d-9f84-602f3f1ab1f0, https://mobbin.com/sites/sections/f66e2284-aa38-4877-b2cd-5181ec2185e3 |
| 14 | A new `site/docs/changelog.md` built from `CHANGELOG.md`, and a 3-entry strip on the landing | Dated entries in mono, a title and one line each. State plainly that 0.1.0 is unreleased | Shows the project is alive without inventing numbers | https://mobbin.com/sites/sections/56c0a44a-16ef-4f35-ae19-dd3f87be370e, https://mobbin.com/sites/sections/a85703b4-636f-407a-8b4f-cade72d6f909 |
| 15 | `site/docs/install.md` | Turn the hosts into rows: host, command, and a status of "checked" or "not checked yet", taken from facts.md section 5 | Honest compatibility is the "works with" proof, made precise | https://mobbin.com/sites/sections/b99fe27f-0826-490b-8dee-8fb256bfc740 |
| 16 | `site/build.py` `shell()` / `layout` for `/` only | **Ask Kunal first:** hide the docs sidebar on the landing page only | Gives the hero full width. It conflicts with the "documentation directory" direction, so it is his call | https://mobbin.com/sites/sections/8fa276bd-351b-4988-bdb2-dd8b84661988 |

---

## 5. What an enterprise buyer needs to find that is missing

Everything below uses only facts the repo supports. Sources are named on each line. Nothing here claims customers, certifications, SSO or measured results.

**A. Security and data handling page (the biggest gap).** Today these facts sit in one FAQ answer and in `SECURITY.md`, which the site never links. A `/docs/security/` page could say:
- The engine runs on your computer. It uses Python's standard library and makes no network calls (facts.md section 6; `site/docs/faq.md`).
- Your chat goes to whichever AI provider you use, as with any prompt. In the Claude app the scripts run in Claude's code-execution sandbox (`faq.md`).
- The illustration skill searches open-licence art sites over HTTPS, and only when you use it (facts.md section 7, the network exception approved 2026-09-28).
- The journey log is off unless you say yes. It stays in your project and is kept out of git. Shared reports are a separate yes, and no server collects them yet, so nothing is sent today (`docs/PRIVACY.md`).
- There is no hosted service, no accounts and no SSO. Access control is whatever your repository host gives you (`enterprise.md`).
- To report a vulnerability, use GitHub private vulnerability reporting. The first reply comes within 7 days. There is no tagged release yet, so fixes land on `main` (`SECURITY.md`).

Pattern: one plain summary, then the data boundary named concretely (https://mobbin.com/screens/8ae8b188-4ba3-4aab-bf47-d7496b9d63cb, https://mobbin.com/sites/sections/205955a6-96d6-44fc-84c6-80a66c23c15e). Do not add certification badges; none exist.

**B. "Pilot it with one team" guide.** The content already exists in `faq.md` ("How would a team adopt it?") and `enterprise.md`. Steps:
1. Start with one product.
2. Commit `DESIGN.md` and the tokens.
3. Accept the `AGENTS.md` note so coding agents read the system first.
4. Lock values that must not drift (`engine.py set ... --lock`).
5. Add project standards with a reason (`--why`).
6. Read the decision log together.
7. Have each person run `engine.py review` at the end of their work. `--strict` exits with an error, but it is not tested in a pipeline yet.

Say plainly that no team has piloted it. Pattern: numbered step cards (https://mobbin.com/sites/sections/a52dff05-8f33-4ec6-92ce-ab2fdd3c550b).

**C. At-a-glance controls with an honest status** (change 12). Rows, all from `enterprise.md`:
- Decision log, append-only: works.
- Locked values: works.
- House standards, 455 rules, version 2: works.
- Project standards: works.
- Drift check in code: works locally, not tested in CI.
- DTCG 2025.10 tokens with a resolver: works.
- Style Dictionary, Terrazzo, Tokens Studio and Penpot: named, not tested.
- Figma variables, one file per mode: works.
- Light and dark, three densities, reduced motion: works.
- Multi-brand modes: not yet.
- React Native and Flutter export: not yet.
- Hosted service, SSO and roles: not offered.

**D. Version, release and maintenance signals.** Version 0.1.0 is planned with no tag. CHANGELOG says "Unreleased". No CI runs are recorded. One person maintains it. The repo was created 2026-09-23 (facts.md). These belong in the footer and on the security page, stated once and plainly.

**E. Which AI tools it is checked in.** Use rows per host with "checked" or "not checked yet", copied from facts.md section 5:
- Claude Code: `claude plugin validate` passes; a fresh install is unverified.
- Claude app: `build_dist --check` passes; the upload is unverified.
- Codex, Cursor, Copilot and Gemini CLI: the skill folders are present; a run is unverified.
- ChatGPT: the files are present; a run is unverified.
- The engine alone: checked with Python 3.10.11.

**F. A contact route for teams, with no sales theatre.** Link the GitHub issue forms and Discussions (Discussions is empty so far). Say there is one maintainer and no support agreement. Pattern: https://mobbin.com/sites/sections/5297ece1-f418-4646-af39-e8b993c49d4f, kept honest.

**G. Licence in one place:** MIT for code and CC BY 4.0 for docs. This is in the footer today, but missing from the enterprise page.

**Do not add:** customer logos, user or install counts, "enterprise-grade", SSO, SOC 2 or other certifications, team pilots, or the non-public skills (facts.md section 9 bans these).

---

## Verification notes
- **Measured in the local build with Playwright:**
  - the header is 8 px tall;
  - the role list is 112 px wide;
  - the landing page has 20 doc rows;
  - the hero overflows to 417 px in a 390 px viewport;
  - the top nav has 3 items;
  - the GitHub card shows Stars, Forks, Open issues and Last push;
  - the showcase has filter pills, with "All 54" as the default.
- **Read from source:**
  - the `.bar` collision (`figures.css` line 98 against `site.css` line 30, concatenated by `build.py` line 763);
  - the `.role` grid (`site.css` line 116);
  - `figures.css` is untracked in git.
- **Inferred, not checked:**
  - that the header bug is not on the live site;
  - how readers perceive the uppercase buttons and the 20-row list. These are judgments against the references.
- **Mobbin coverage:** supermemory.ai is not on Mobbin. Its stand-ins for "UI floating on a photo" are the Unify, Whereby and hilos references above.
