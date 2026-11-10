# R6: what Refero Styles teaches about premium design systems (hand-read observations)

October 7, 2026. Kunal asked to add https://styles.refero.design (2,000+ website styles, each with a DESIGN.md) to the project.

**How this was made, and why not by OpenWiki fetch.** Refero's robots.txt blocks AI crawlers by name. Its [Terms of Use](https://doc.refero.design/legal/terms-of-use) (updated August 3, 2026) forbid scraping, systematic extraction, dataset creation and embedding Refero Content in a product without a written agreement. They allow using "insights you learn from Refero" for your own design work. So these notes come from reading three style pages by hand in a browser: Linear, Vercel and ElevenLabs. They are written in our own words. No token values, tables or DESIGN.md text were copied, and nothing from Refero is stored in the repo. The MIT-licensed Refero Skill went through the normal OpenWiki pipeline instead (`learn/analysis/referodesign-refero-skil-*.json`).

Everything here is an observation from three pages, or `[inferred]`. It is not yet a Decision Card.

## How a Refero style is structured

Every page we read followed the same shape. The shape is the reusable part.

1. **A one-line identity in concrete imagery**, a place or an object rather than adjectives ("a typeset terminal on paper" rather than "clean and modern"). Then the theme (light or dark).
2. **An honesty note:** measurements are normalized, roles and recommendations are interpreted, and the examples are reconstructions.
3. **One prose paragraph that explains the system's logic:** what the canvas is, what the single accent is for, why the weights sit where they do, and what carries the visual texture. It explains why, not just what.
4. **Token tables with a role column:** colors, typography (each face with its job), spacing, radius, shadows and layout.
5. **Named component variants** that say where each is used (for example "primary action, one per view").
6. **Do and Don't lists** in which almost every line has a number *and* a reason, often "this choice is the identity, and breaking it destroys it".
7. **Surfaces as numbered levels** (canvas, card, raised, tint), plus how depth is made.
8. **Imagery and layout**, an **agent prompt guide** (a quick color reference and example prompts for specific components), **similar brands**, and quick-start CSS variables and a Tailwind theme.

## What premium systems have in common (three of three pages)

- **One accent with one job.** The chromatic color is kept for one role (the single primary action, or only the product visuals) and is never used as decoration. Everything else is neutral.
- **Heading weights stay low.** The display type is light or regular, not bold. All three pages forbid heavy weights for headlines, and all three keep every weight in the system under 600. Restraint in weight reads as confidence.
- **Display letter spacing is set on purpose.** It is tight on display sizes and is a defined part of the identity, sometimes with the opposite tracking on body text for contrast.
- **A tiny shape vocabulary.** Two or three radii for the whole system, stated as a closed list.
- **Depth from hairlines or tone, not drop shadows.** Separation comes from 1 px or thinner borders, inset rings or tonal steps between surfaces. Two of the three forbid drop shadows outright.
- **Neutrals with a temperature.** No pure black or pure white for text and canvas: warm or cool tinted neutrals.
- **The product is the texture.** Real product UI, or one signature graphic, carries the visual interest. There's almost no ornament.
- **Spacing as a short ladder.** A few named steps from element gap to section gap, with large, even section gaps.

## What this says about OpenDesigner's own output `[inferred]`

Compared with the system OpenDesigner sketched for the film (`videos/opendesigner-film/system/`):

- **Heading weight 650** is heavier than all three references. "Premium, confident" in the feel words should probably pull the heading weight down, not up.
- **Radius:** the engine emits 11 steps (0 to 32) plus role aliases. The references use 2 or 3. A closed, small vocabulary may matter more than a complete scale.
- **Elevation:** the engine's `elevation.overlay` uses stacked drop shadows. The references prefer hairlines or tonal surfaces. Elevation style may deserve its own question or dial reading (`depth` was 34 out of 100, low, yet the output still used drop shadows).
- **The accent's job:** the engine assigns the accent to action, link, focus and brand all at once. The references give it one job. "What is the accent for?" may be a missing sketch-level question.
- **DESIGN.md:** ours is complete but explains less. The references open with a concrete image and a paragraph on the system's logic, and their Do/Don't lines carry reasons and numbers. That could improve our DESIGN.md output, and the agent prompts that read it.
- **Honesty note:** Refero labels what is measured and what is interpreted. We do this per value (`set_by`), but not as a plain statement at the top of DESIGN.md.

These are inputs for the "blank slate" and "blank design system" discussion, not changes. Each would become a Decision Card with sources before any default changes (`learn/IMPROVING.md`).

## Sources

- Refero Styles pages for Linear, Vercel and ElevenLabs, read on 2026-10-07 (reference only; not stored).
- Refero Terms of Use, https://doc.refero.design/legal/terms-of-use (the clauses on scraping and insights).
- Refero Skill (MIT), https://github.com/referodesign/refero_skill, analysed in `learn/analysis/`.
