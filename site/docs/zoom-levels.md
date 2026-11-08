---
title: Zoom levels
seo_title: Zoom levels: from a five-question sketch to full detail
description: How OpenDesigner's four zoom levels work: a five-question sketch, eight broad screens, one area at a time, then detail. You can stop at any level.
section: Concepts
order: 3
updated: 2026-11-08
---

OpenDesigner has four zoom levels: sketch, broad, defined and detailed. Everyone starts with the sketch: up to five questions for a complete but rough system. After each level you can stop or zoom into one area, and every level leaves working files.

{{figure:zoom-levels-ladder}}

## The four levels

| Level | What it asks |
|---|---|
| 0 · Sketch | Up to five questions ([with example answers](/docs/quickstart/)), planned at about 3 minutes. Every token exists afterwards, and every section of `DESIGN.md` is filled from sourced defaults. |
| 1 · Broad | One short screen for each foundation, 8 in all, planned at about 8 minutes: the visual style, how much fits on a screen, where the brand color shows, the font, corners, how cards stand apart, how motion feels, and where the master copy lives. Say "skip" and the default stays. |
| 2 · Defined | One area at a time, up to 12 questions each. Color, for example, covers ramps, roles and contrast. |
| 3 · Detailed | Components, patterns and the fine print of each area: everything else in the interview. |

### The site brief

For a site that has to persuade, such as a landing page, level 1 starts with one screen of five lines:

- the goal, and how you'll count it;
- the roles to convince, and what each needs to see;
- the proof you can show;
- how people find the site, in which languages, and the questions it answers;
- the kinds of pages it needs.

It drafts the lines from your words, research and repo, and you correct them. It never drafts the proof: only you can give that. Lines nobody has answered say "Not enough information" in `PRODUCT.md`, next to the question that fills them.

## The areas you can zoom into

There are 14 areas, such as color, typography, motion and components. Zooming into one first asks what you skipped at lower levels: go into Color after the sketch, and it first asks where the brand color shows.

## How the offer works

After every level, it makes a short offer.

{{figure:zoom-levels-offer}}

- After the sketch, it first offers to research your users (about 10 minutes, and it does the work), unless that's done or you said no.
- The areas whose choices change the most come first, then those your answers made risky, such as a light brand color or a dense product.
- "Stop" is always a good answer.
- Accessibility is never offered as something to skip: its [floors](/docs/accessibility/) are set at level 0.

## It slows down where it matters

Some decisions shape many others: in the decision graph, brand personality directly shapes 15 and target platforms 12. For those, it explains why, shows two or three options used by real systems, suggests one with its source, and says what it changes further down.

For a small gap, it takes the default and labels it as an assumption instead of asking. It asks one question per message.

## Fewer questions for some people

- **Plain voice.** If you talk in plain words, it asks fewer questions: in the sketch, maybe only what you're making, how it should feel and your brand color. It guesses the rest, records the guesses as assumed, and tells you in one line.
- **"Just pick."** Say "just pick" or "you choose", and it stops asking. It picks values that fit your words and files, and records them as handed over.
- **Questions a standard already settles** are skipped. So are planned questions, whose feature isn't built yet: six of the 200.

## How you see your level

Each section of `DESIGN.md` shows its zoom level, so a teammate can see what was decided and what is still a default. The overview page marks each area as Chosen, Picked for you or Default.

## About the time estimates

The minutes are design targets. Nobody has timed real people yet. The engine part of each step takes a couple of seconds. If a level takes much longer for you, please [tell us](https://github.com/ckryptickunal/OpenDesigner/issues/new/choose).
