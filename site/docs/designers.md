---
title: For product designers
seo_title: OpenDesigner for product designers: decisions and Figma
description: How OpenDesigner fits a product designer's process: what it automates, what you keep control of, how logged decisions help in reviews, and Figma variables.
section: Guides
order: 1
updated: 2026-10-14
---

OpenDesigner does the repetitive part of design-system work for you: scales, tokens, component states, contrast checks and keeping the code in step with the design. You keep the direction, the taste and every asset a person should make. It writes down each decision with its reason, and it exports Figma variables so your design file can match the code.

## Where it fits in your process

- **Turning a direction into a system.** Once you know how the product should feel, the sketch builds a complete first version from about five answers. You then zoom into the areas you care about, such as color or type.
- **Handing off to engineering.** The same decisions become tokens, CSS variables, a Tailwind theme, and Swift and Compose files. Engineers and their AI tools can read the rules in `DESIGN.md`.
- **Keeping it consistent later.** Changes go through the extend skill, which reads the decision log first. See [Change or extend a system](/docs/extend/).

It doesn't draw screens. Your canvas work stays in your design tool.

## What you keep control of

- **Direction and taste.** It asks you for your brand personality and the dial positions, and records your answer. It never decides these for you. The same goes for which element matters most on each screen, and which actions get undo or a confirmation step.
- **Every big choice.** For a decision that shapes many others, it explains why it matters and shows two or three options with real systems that use them. Then it suggests one with its source and says what it changes further down. You can always answer in your own words.
- **What counts as your decision.** A suggestion you did not answer is never recorded as your choice.
- **Locks.** You can lock a value, such as an exact brand color. A locked value changes only with your OK.
- **Assets.** For a logo, custom icons, illustration, photos, a brand typeface or a voice guide, it asks you. If you don't have one, it writes a brief a designer can act on. See [Brand assets](/docs/brand-assets/).

You can also say "talk like a designer". It then leads with design terms, and plain words stay available if you ask.

## Using decisions in design reviews

Reviews go faster when everyone can see why a value is what it is.

{{figure:designers-reason-vs-value}}

- **`opendesigner/decisions.md`** lists every decision with its reason, its date and how it was set: chosen by you, a default you confirmed, assumed from your words, handed over ("you decide"), or taken from a reference. A later decision replaces an earlier one, but nothing is deleted. Anyone can see the history.
- **`DESIGN.md`** shows how far each area was zoomed. A reviewer can tell what was decided and what is still a default.
- **`opendesigner/overview.html`** puts the whole system on one page. Each area is marked Chosen, Picked for you or Default. It is a good page to share on screen in a review.
- **`opendesigner/RATIONALE.md`** is one page for the team: what was chosen, why, and what is still open. The skill writes it at the end of a session.
- **"Why is this blue?"** Ask your AI. The extend skill answers from the decision log and changes nothing.

{{figure:designers-review-why-blue}}

The defaults rest on 352 Decision Cards. Each card covers one design decision, with its options, a default and its sources. See [Decisions, DESIGN.md and the overview page](/docs/decisions/).

## Figma variables

Every build writes Figma files in `opendesigner/build/figma/`:

- `import/` holds one file per collection and mode, for Figma's own variables import. The collections are Primitives, Color (Light and Dark), Density (Spacious, Comfortable and Compact), Motion (Standard and Reduced), and Tokens for everything that doesn't change by mode.
- `variables.json` holds the same variables for Tokens Studio.

Figma imports this token format only in part: one mode per file, sRGB colors, px units, and no composite tokens. That is why the engine writes one file per mode.

### Writing straight into a Figma file

With Figma's remote MCP server and a Full seat, the export skill can create the variables, text styles, effect styles and specimen frames in your file. It suggests working on a duplicate first, and it checks the result by reading the variables back. When you change something in Figma, it records the change as a new decision instead of editing token files.

{{figure:designers-figma-round-trip}}

Hands-on Figma research is still an open task ([issue #10](https://github.com/ckryptickunal/OpenDesigner/issues/10)). The Figma steps so far come from Figma's own docs. Paper is also supported while Paper Desktop is running. See [Export](/docs/export/).

## Where you are still needed

In a stress test, 8 AI agents built 46 pieces by following the OpenDesigner process. All the brands in them were made up.

- The engine helped most where things are easy to get wrong: contrast-safe colors, spacing, radii, focus rings and motion.
- About a third of the pieces were competent but conventional.
- Most display type, light weights, tinted backgrounds, hard shadows and art colors were made outside the tokens, or against them.
- Every builder had to restore or work around a brand color the engine changed.

So the tokens give you consistency and readable contrast, and a distinctive look still needs your eye. Check your brand color on the overview page after each build. The full findings are in the [stress test report](https://github.com/ckryptickunal/OpenDesigner/blob/main/brand/showcase/STRESS-TEST.md).
