---
title: Zoom levels
seo_title: Zoom levels: from a five-question sketch to full detail
description: How OpenDesigner's four zoom levels work: a five-question sketch, eight broad screens, one area at a time, then detail. You can stop at any level.
section: Concepts
order: 3
updated: 2026-10-14
---

OpenDesigner has four zoom levels: sketch, broad, defined and detailed. Everyone starts with the sketch, which gives a complete but rough system from up to five questions. After each level you can stop or zoom into one area, and every level leaves working files.

{{figure:zoom-levels-ladder}}

## The four levels

### Level 0: sketch

Up to five questions: what you are making, who it is for, where it runs, how it should feel, and your brand color or logo. Every token exists afterwards, and every section of `DESIGN.md` is filled from sourced defaults. The planned length is about 3 minutes. See [Your first design system](/docs/quickstart/) for the questions with example answers.

### Level 1: broad

One short screen for each foundation, 8 questions in all, planned at about 8 minutes. In order:

1. the visual style;
2. how much fits on a screen;
3. where the brand color shows;
4. which font;
5. corners;
6. how cards stand apart from the page;
7. how motion feels;
8. where the master copy of the system lives.

You can say "skip" on any screen, and the default stays.

### Level 2: defined

One area at a time, with 1 to 15 questions per area. For example, Color covers color ramps, color roles and contrast.

### Level 3: detailed

Components, patterns and the fine print of each area. This is everything else in the interview.

## The areas you can zoom into

There are 14 areas: overview, accessibility, platforms, modes, color, typography, layout, shape, elevation, motion, iconography, content, components and delivery.

When you zoom into an area, it first asks any questions you skipped at lower levels. For example, if you go into Color after the sketch, it asks where the brand color shows before going deeper.

## How the offer works

After every level, it makes a short offer like this:

```
That's your first version: everything works, and I picked most of the small choices for you.
Stop here, or go deeper on one part:
Colors (about 6 min) · Text (about 2 min) · Everything, in 8 quick screens (about 8 min)
```

{{figure:zoom-levels-offer}}

- It offers at most three choices.
- It puts first the areas whose choices change the most, then areas your answers made risky, such as a light brand color or a dense product.
- "Stop" is always a good answer.
- Accessibility is never offered as something to skip. Its floors are set at level 0. See [Accessibility floors](/docs/accessibility/).

## It slows down where it matters

Some decisions shape many others. In the decision graph, brand personality directly shapes 15 other decisions, and target platforms shape 12. For a question like that, it explains why it matters, shows two or three options with real systems that use them, suggests one with its source, and says what it changes further down.

For a small gap, it takes the default and labels it as an assumption instead of asking. It asks one question per message.

## Fewer questions for some people

- **Plain voice.** If you talk in plain words, it asks fewer questions. In the sketch, it may ask only what you are making, how it should feel and your brand color. It guesses the rest from your words, records the guesses as assumed, and tells you in one line.
- **"Just pick."** Say "just pick", "just do it" or "you choose", and it stops asking. It picks values that fit your words and files, and records them as handed over to it.
- **Questions a standard already settles** are skipped. So are questions marked as planned, whose feature isn't built yet. Six of the 193 questions are planned.

## How you see your level

Each section of `DESIGN.md` shows its zoom level: sketch, broad, defined or detailed. A teammate can see what was decided and what is still a default. The overview page marks each area as Chosen, Picked for you or Default.

## About the time estimates

The minutes are design targets. Nobody has timed real people yet. The engine part of each step takes a couple of seconds. If a level takes much longer for you, please [tell us](https://github.com/ckryptickunal/OpenDesigner/issues/new/choose).
