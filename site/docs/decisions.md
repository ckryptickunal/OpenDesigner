---
title: Decisions, DESIGN.md and the overview page
seo_title: Design decisions, DESIGN.md and the overview page explained
description: How OpenDesigner records each design decision with its reason, keeps DESIGN.md current for people and AI agents, and shows the system on one overview page.
section: Concepts
order: 4
updated: 2026-10-14
---

OpenDesigner writes every decision into a log with how it was set and why. It turns the current decisions into `DESIGN.md`, a plain-words description of your system that people and AI tools read. It also builds `overview.html`, one page that shows your whole system and marks what is still missing.

## The decision log

`opendesigner/decisions.md` has one entry per decision, newest last. Each entry records:

- the value that was set;
- the reason, in the owner's words where possible;
- the date;
- whether it is locked;
- which earlier decision it replaces, if any;
- where it came from, such as a reference;
- how it was set.

{{figure:decisions-log-entry}}

### How a value was set

- **Chosen:** you picked it.
- **Confirmed default:** you saw the suggestion and agreed.
- **Auto default:** nobody was asked, so the sourced default stayed.
- **Assumed:** guessed from your words, without a direct answer. It tells you each guess in one line.
- **Delegated:** you said "you decide" or "just pick".
- **Reference:** a measured value you accepted from a site, file or screenshot you shared.
- **Asset:** taken from a file you supplied, such as the main color of your logo.
- **Standard:** set by a house or project standard.

A suggestion you never answered is never recorded as your choice.

### Why it is append-only

Nothing in the log is edited or deleted. A new decision for the same value replaces the old one and says so. That way a later session, or a different AI tool, can't quietly undo a choice, and anyone can see the history. Here is one entry from a test run:

```
## D-0004 · raw.brandColor = "#2563eb"
- set_by: chosen · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: sketch: Level 0 answer
```

### Locks

You can lock any decision. A locked value changes only with the owner's OK. The accessibility floors and the house standards are locked from the start. See [For enterprise design-system teams](/docs/enterprise/).

## DESIGN.md

`DESIGN.md` sits at the root of your project. It is your design system in plain words.

- **It opens with a short summary:** what the product is, who it is for, where it runs, the feel, and what to do next.
- **Each section shows its zoom level,** so you can see what was decided and what is still a default.
- **Each decision opens with one plain sentence.** Designer and engineer detail sits below it.
- **It has a section for AI agents.** It tells them to read the file and the tokens before changing any screen, to use tokens instead of raw values, and to leave locked decisions alone.
- **It stays current.** Every recorded decision refreshes it, together with `PRODUCT.md`.

Don't edit `DESIGN.md` by hand, because the next refresh rewrites it. Notes you put inside special "keep" blocks survive each refresh. If someone does edit the generated file, the extend skill notices and offers to turn each edit into a decision.

`PRODUCT.md` holds what the product is, who it is for and where it runs, so later sessions don't have to guess.

## The overview page

`opendesigner/overview.html` is your whole system on one page. Every build rewrites it. It works offline and loads nothing from the web.

It shows:

- a cover and a brand book;
- how complete the system is;
- colors in each theme, with their contrast ratios;
- headings h1 to h6 and every text style;
- spacing, corners, depth and motion;
- core components;
- brand assets, and how many of the 14 you have provided;
- how the system grew, decision by decision.

Each area is marked **Chosen**, **Picked for you** or **Default**. Anything only you can give, such as a logo, a voice guide or what the product is for, shows as **Not enough information**, next to the question that fills it.

{{figure:decisions-overview-status}}

Two related files sit next to it. `opendesigner/preview.html` shows every token on one page. `opendesigner/preview/` holds seven visual pages filled with your own values: palette, type scale, spacing ruler, radius, elevation, motion and component sheet.

## RATIONALE.md

At the end of a session, the skill writes `opendesigner/RATIONALE.md` from a template. It is one page for the team: what was chosen, why, and what is still open.

## Where the reasons come from

Every default traces to the research: the dial formulas in `levers.json` and the Decision Cards behind them. A card covers one design decision, with its options, a default and its sources. The defaults rest on 352 cards, and some formulas are marked as inferred. A citation check finds no broken references, and a verification pass re-checked 161 claims against live sources. It found 5 wrong, and the fixes are logged. The research map is in the [repository](https://github.com/ckryptickunal/OpenDesigner/blob/main/docs/RESEARCH.md).

## Known issues

- Only a few core components are shown so far: buttons, a text field and a card. The overview lists 25 components as planned.
- The palette page's contrast table is still empty ([issue #47](https://github.com/ckryptickunal/OpenDesigner/issues/47)). The overview page shows the contrast ratios.
