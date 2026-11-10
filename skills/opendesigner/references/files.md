# Files in this skill

Every file in the opendesigner skill, and when to read it. SKILL.md names the ones to read at the start.

| Path | Read it when |
|---|---|
| `references/rules.md` | At the start. How to talk: message style, the three voices, the question card, answer statuses, `OD:` lines |
| `references/zoom.md` | At the start. Zoom levels 0 to 3, the 5 sketch questions, and the offer after each level |
| `references/glossary.json` | Before you name any term in a message. One term per line: search for the term or one of its `aliases` |
| `references/stages/NN-*.md` | When you zoom into an area. Questions in order, with options, defaults, what to show and when to skip. `NN-*.detailed.md` holds zoom 3 |
| `references/pacing.json` | Areas, their questions per level, rough minutes, and the high-impact decisions |
| `references/hooks.md`, `hooks.json` | Whenever an asset comes up: logo, fonts, icons, photos and so on |
| `references/guardrails.md` | Before writing files, before reading a reference, and whenever you are unsure |
| `references/standards.md` | At the start (short). House standards: rules OpenDesigner applies and locks in every project, the values they lock, and how the person can change one |
| `references/standards/<theme>.md` | Before you offer options in that area, and before you implement anything it covers (motion, toasts, drawers, touch, Swift and more) |
| `references/audit.md` | When the product is already built, before you change anything (fast path step 1): the checklist for buttons, type, colour, spacing, corners and states, and the row each finding gets, with the source of its rule |
| `references/making.md` | Before you build a page, a screen or a section with the system, and each time the person gives feedback on what you built. The round, showing options, keeping a page one page, checking it as rendered, and the mistakes builders make |
| `references/quality.md` | Before you call any visual result done or show it as finished. The floors, the nine-line scorecard, a fix prompt for each line, and the report format |
| `references/research.md`, `scripts/research.py` | After the sketch, before level 1, and whenever the person asks about their users: research who they are, the apps they use and what they expect, save the findings with sources, and turn them into recommended answers. Check your tools first (web search, a browser, `/last30days`, Mobbin, analytics); one yes covers the whole run |
| `references/practices.md` | At the start of a session. Which tools and accesses to look for (Mobbin, a browser, image and video tools, the project's keys), how to use each, and what to suggest once when one is missing |
| `references/styles.md` | When the person describes a look in their own words ("frosty", "like a comic", "soft buttons"): map the words to named styles, show them, say the name in plain words first, and record the pick with its dial settings. 28 styles with real examples, and a gradient and surface glossary |
| `references/style-lab.md`, `references/style-catalog.md` | When no named style fits, when the person wants something new or experimental, or when they ask what else exists: search the full catalogue by their words, mix or change styles on 15 trait axes, explore new directions, and save one as their own. The floors never move |
| `references/library.md`, `scripts/library.py`, `assets/library/` | At the first page, screen or component the person asks you to build, and whenever they ask for ready-made parts. The optional component library: when to offer it, to whom, and how to add one |
| `references/post-change-audit.md` | After every implementation (a page, a component, a library), before you show it: the automatic checks, then each owner-corrected rule by eye, at phone, tablet and desktop |
| `references/improve.md` | When something is missing, wrong or confusing |
| `scripts/journey.py`, `references/report.schema.json` | The private journey log and the optional anonymous report (`rules.md` section 11) |
| `references/questions.json`, `graph.json`, `cards/Lxx.json`, `levers.json`, `ontology-slim.json` | Machine index; what a choice changes; "why?" sources; dials and formulas; the full block map |
| `references/taste.md`, `scripts/taste.py`, `assets/taste/library.json` | When you offer the taste poll, and before you offer dials or style options once the project has taste evidence: the taste index merges the poll, the person's own decisions, inspirations, the style pick and feel words. Also when the person gives a picture of the look or says what it should never look like: both go on the taste card |
| `assets/templates/*.html` | Visual steps |
| `assets/output/*` | The shape of the files the person keeps |
| `references/engine.md` | Before you run an engine command whose flags you don't know: every command of `engine.py` and `journey.py`, and how versions are compared |
| `references/visuals.md` | Before you show the overview or fill a template: what the overview holds, the templates, the Design System artifact and **Copy my choice** |
| `references/files.md` | This index |
