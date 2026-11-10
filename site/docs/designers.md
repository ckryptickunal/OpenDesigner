---
title: For product designers
seo_title: OpenDesigner for product designers: decisions and Figma
description: How OpenDesigner fits a product designer's process: what it automates, what you keep control of, how logged decisions help in reviews, and Figma variables.
section: Guides
order: 1
updated: 2026-11-10
---

OpenDesigner does the repetitive part of design-system work for you: scales, tokens, component states, contrast checks and keeping the code in step with the design. You keep the direction, the taste and every asset a person should make. It writes down each decision with its reason, and it exports Figma variables so your design file can match the code.

## Where it fits in your process

- **Turning a direction into a system.** The sketch builds a complete first version from about five answers. Then you zoom into the areas you care about, such as color or type.
- **Handing off to engineering.** The same decisions become tokens, CSS variables, a Tailwind theme, and Swift and Compose files. Engineers and their AI tools read the rules in `DESIGN.md`.
- **Keeping it consistent later.** Changes go through the extend skill, which reads the decision log first. See [Change or extend a system](/docs/extend/).

It doesn't draw screens. Your canvas work stays in your design tool.

## What you keep control of

- **Direction and taste.** It asks you for the brand personality and the dial positions, and never decides these for you. The same goes for which element matters most on each screen, and which actions get undo or a confirmation step.
- **Every big choice.** For a decision that shapes many others, it shows two or three options with real systems that use them, suggests one with its source, and says what it changes further down. You can always answer in your own words.
- **What counts as your decision.** A suggestion you didn't answer is never recorded as your choice.
- **Locks.** Lock a value, such as an exact brand color, and it changes only with your OK.
- **Assets.** For a logo, custom icons, illustration, photos, a brand typeface or a voice guide, it asks you. If you don't have one, it writes a brief a designer can act on. See [Brand assets](/docs/brand-assets/).

Say "talk like a designer", and it leads with design terms.

## Using decisions in design reviews

{{figure:designers-reason-vs-value}}

- **`opendesigner/decisions.md`** lists every decision with its reason, its date and how it was set. A later decision replaces an earlier one, but nothing is deleted, so anyone can see the history.
- **`DESIGN.md`** shows how far each area was zoomed, so a reviewer can tell what was decided and what is still a default.
- **`opendesigner/overview.html`** puts the whole system on one page, with each area marked Chosen, Picked for you or Default. It's a good page to share on screen in a review.
- **`opendesigner/RATIONALE.md`** is one page for the team: what was chosen, why, and what is still open.
- **"Why is this blue?"** Ask your AI. The extend skill answers from the decision log and changes nothing.

{{figure:designers-review-why-blue}}

The defaults rest on more than 500 Decision Cards, each with its options, a default and its sources. See [Decisions, DESIGN.md and the overview page](/docs/decisions/).

## Figma variables

Every build writes Figma files in `opendesigner/build/figma/`: one file per collection and mode for Figma's own variables import, and `variables.json` for Tokens Studio. Figma's import takes only part of this token format (one mode per file, sRGB colors, px units, no composite tokens), which is why there is one file per mode.

With Figma's remote MCP server and a Full seat, the export skill can also write straight into your file: the variables, text styles, effect styles and specimen frames. It suggests working on a duplicate first, and checks the result by reading the variables back. When you change something in Figma, it records the change as a new decision instead of editing token files.

{{figure:designers-figma-round-trip}}

Hands-on Figma research is still an open task ([issue #10](https://github.com/ckryptickunal/OpenDesigner/issues/10)), so the Figma steps come from Figma's own docs. Paper is also supported while Paper Desktop is running. See [Export](/docs/export/).

## Where you are still needed

In a stress test in October 2026, 8 AI agents built 46 pieces by following the OpenDesigner process, all for made-up brands.

- The engine helped most where things are easy to get wrong: contrast-safe colors, spacing, radii, focus rings and motion.
- A later audit of these and 8 mockups against shipped products kept 28 of the 54, sent 20 back for polish and rebuilt 6.
- Most display type, light weights, tinted backgrounds, hard shadows and art colors were made outside the tokens, or against them.

So the tokens give you consistency and readable contrast, and a distinctive look still needs your eye. The full findings are in the [stress test report](https://github.com/ckryptickunal/OpenDesigner/blob/main/brand/showcase/STRESS-TEST.md). The [showcase](/showcase/) shows a different count today: since that audit, pieces were rebuilt or held back, and B2B product screens and style studies were added.
