---
title: The files it writes
seo_title: The files OpenDesigner writes: tokens, exports and DESIGN.md
description: Every file OpenDesigner writes into your project: DESIGN.md, the DTCG tokens, the exports, the overview page and the decision log, and what each one is for.
section: Reference
order: 3
updated: 2026-10-15
---

OpenDesigner writes `DESIGN.md` and `PRODUCT.md` at the root of your project, and everything else into an `opendesigner/` folder. The token files in `opendesigner/tokens/` are the source of truth, and every other file is made from them. In a test run, one sketch and build wrote 50 files with no errors.

{{figure:files-tree}}

## At the root of your project

- **`DESIGN.md`:** your design rules in plain words, for people and AI tools. It refreshes after every decision, and each section shows its zoom level.
- **`PRODUCT.md`:** what the product is, who it is for and where it runs, so later sessions don't have to guess.

## The tokens

**`opendesigner/tokens/`** holds 11 files in the open DTCG 2025.10 format:

- `primitives.tokens.json`: the raw palette and scales;
- `semantic.tokens.json`: roles that don't change by mode;
- `semantic.color.light.tokens.json` and `semantic.color.dark.tokens.json`;
- three density files: spacious, comfortable and compact;
- `motion.standard.tokens.json` and `motion.reduced.tokens.json`;
- `opendesigner.resolver.json`, which ties the modes together;
- a small metadata file.

See [Design tokens and DTCG](/docs/design-tokens/).

## The exports

All of these are in `opendesigner/build/`. Every build rewrites them, so don't edit them by hand.

{{figure:files-edit-exports}}

- **`css/tokens.css`:** CSS variables you can use in any web project.
- **`tailwind/theme.css`:** a Tailwind CSS v4 theme, so utility classes use your colors, spacing, radii and type.
- **`figma/`:** Figma variables, with one import file per collection and mode in `figma/import/`, and `figma/variables.json` for Tokens Studio.
- **`paper/`:** tokens for the Paper design tool, in light and dark.
- **`swift/DesignTokens.swift`:** the same values for iOS apps.
- **`compose/DesignTokens.kt`:** the same values for Android apps built with Jetpack Compose.
- **`dtcg/`:** one DTCG resolver file for token tools that take a single entry point.
- **`artifact/project/`:** the system as files for a Claude Design System artifact: tokens, a brand book, a cover and a button preview.

See [Export](/docs/export/) for how to use each one.

## Pages you open in a browser

- **`opendesigner/overview.html`:** your whole system on one page, including what is still missing. It works offline and loads nothing from the web.
- **`opendesigner/preview.html`:** every token on one page.
- **`opendesigner/preview/`:** seven visual templates filled with your own values: palette, type scale, spacing ruler, radius, elevation, motion and component sheet. The option gallery is filled per question with `engine.py show`, and the taste poll is built by `taste.py build` into `opendesigner/preview/taste-poll/`.

## The record

- **`opendesigner/decisions.md`:** every decision, how it was set and why. It is append-only, so a later session doesn't quietly undo a choice.
- **`opendesigner/standards.md`:** the house and project standards this project follows, locked, with their sources.
- **`opendesigner/state.json`:** where you left off, so you or another AI tool can continue later. `DESIGN.md` and the tokens are made from it.
- **`opendesigner/standards-state.json`:** a copy of each standard this system follows, as it follows it. Keep it next to `state.json`.

See [Decisions, DESIGN.md and the overview page](/docs/decisions/).

## Written by the skill, or only when you ask

These are not part of an engine build:

- **`opendesigner/RATIONALE.md`:** one page for the team on what was chosen, why, and what is still open. The skill writes it from a template.
- **A short note in your `AGENTS.md`,** added only after you say yes. It tells later AI agents to read `DESIGN.md`, use the tokens and run `engine.py review`.
- **`opendesigner/feedback.md`,** written only if you report something with `engine.py feedback`.
- **`opendesigner/references/`,** written only when you share a reference with the extract skill. It holds the measurements taken from it.
- **`opendesigner/journey/`,** written only if you said yes to the private log. It is kept out of git.

## What to commit

Commit `DESIGN.md`, `PRODUCT.md` and the `opendesigner/` folder, so your team and your next AI session work from the same rules. The private log in `opendesigner/journey/` stays out of git.

Because the exports are made from the tokens, you can rebuild them at any time with `engine.py build`. You can commit them so your apps import them directly, or rebuild them when you need them.

## How the files relate

- `opendesigner/state.json` holds your answers and settings.
- The tokens in `opendesigner/tokens/` are made from it. They are the source for everything else.
- The exports, the pages and `DESIGN.md` are made from these.
- The decision log records why each value is what it is.

To change anything, record a decision with `engine.py set`, then run `engine.py build`. See [Engine commands](/docs/engine/).
