---
title: Decisions, DESIGN.md and the overview page
seo_title: Write a DESIGN.md your AI coding agent follows
description: How OpenDesigner writes a DESIGN.md your AI coding agent follows, records each design decision with its reason, and shows the whole system on one overview page.
section: Concepts
order: 4
updated: 2026-11-13
---

OpenDesigner writes down every decision with how it was set and why. From those it keeps `DESIGN.md`, your system in plain words for people and AI tools, and an overview page that shows the whole system and what is still missing.

## The decision log

The log has one entry per decision, newest last. Each entry records the value, the reason (in the owner's words where possible), the date, whether it is locked, which earlier decision it replaces, where it came from (such as a reference) and how it was set.

{{figure:decisions-log-entry}}

:::dev
The log is `opendesigner/decisions.md`.
:::

### How a value was set

| Label | What happened |
|---|---|
| **Chosen** | You picked it. |
| **Confirmed default** | You saw the suggestion and agreed. |
| **Auto default** | Nobody was asked, so the sourced default stayed. |
| **Assumed** | Guessed from your words, without a direct answer, and told to you in one line. |
| **Delegated** | You said "you decide" or "just pick". |
| **Reference** | A measured value you accepted from a site, file or screenshot you shared. |
| **Asset** | Taken from a file you supplied, such as the main color of your logo. |
| **Standard** | Set by a house or project standard. |
| **Research** | Recommended by the user research, and recorded only after your yes. |

A suggestion you never answered is never recorded as your choice.

### Why nothing is edited or deleted

A new decision for the same value replaces the old one and says so. So a later session, or a different AI tool, can't quietly undo a choice, and anyone can see the history.

:::dev
One entry from a test run:

```
## D-0004 · raw.brandColor = "#2563eb"
- set_by: chosen · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: sketch: Level 0 answer
```
:::

### Locks

You can lock any decision. A locked value changes only with the owner's OK. The accessibility floors and the house standards are locked from the start. See [For enterprise design-system teams](/docs/enterprise/).

## DESIGN.md

`DESIGN.md` sits at the root of your project. It opens with a short summary: what the product is, who it is for, where it runs, the feel, and what to do next. Each decision opens with one plain sentence, with designer and engineer detail below. Each section shows its zoom level, so you can see what is still a default.

A section for AI agents tells them to read the file and the tokens before changing any screen, to use tokens instead of raw values, and to leave locked decisions alone.

Every recorded decision refreshes it, so don't edit it by hand. Notes inside special "keep" blocks survive each refresh. If someone does edit the generated file, the extend skill notices and offers to turn each edit into a decision.

`PRODUCT.md`, refreshed with it, holds what the product is, who it is for and where it runs, so later sessions don't have to guess. For a site that persuades, it also holds the site brief, such as the goal and the proof.

## The overview page

Every build rewrites the overview page. It works offline and loads nothing from the web.

It shows how complete the system is, your colors in each theme with their contrast ratios, every text style, core components and how the system grew, decision by decision.

Each area is marked **Chosen**, **Picked for you** or **Default**. Anything only you can give, such as a logo, a voice guide or what the product is for, shows as **Not enough information**, next to the question that fills it. Unanswered lines in `PRODUCT.md` say the same.

{{figure:decisions-overview-status}}

:::dev
- The page is `opendesigner/overview.html`.
- `opendesigner/preview.html` shows every token on one page.
- `opendesigner/preview/` holds seven visual pages filled with your own values: palette, type scale, spacing ruler, radius, elevation, motion and component sheet.
:::

## RATIONALE.md

At the end of a session, the skill writes `opendesigner/RATIONALE.md`: one page for the team on what was chosen, why, and what is still open.

## Where the reasons come from

Every default traces back to research: more than 500 Decision Cards, each covering one design decision with its options, a default and its sources. Some formulas are marked as inferred. A verification pass re-checked 161 claims against live sources and found 5 wrong, and the fixes are logged. The research map is in the [repository](https://github.com/ckryptickunal/OpenDesigner/blob/main/docs/RESEARCH.md).

:::dev
The dial formulas are in `levers.json`, with the Decision Cards behind them. A citation check finds no broken references.
:::

## Known issues

- The overview page draws only buttons, a text field and a card, and lists the rest by name (25 in a default system). The component sheet in `opendesigner/preview/` shows more parts in their states, and the [component library](/library/) has 82.
