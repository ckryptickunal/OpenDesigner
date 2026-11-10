---
title: The files it writes
seo_title: The files OpenDesigner writes: tokens, exports and DESIGN.md
description: Every file OpenDesigner writes into your project: DESIGN.md, the DTCG tokens, the exports, the overview page and the decision log, and what each one is for.
section: Reference
order: 3
updated: 2026-11-08
---

OpenDesigner writes your design system into your own project as plain files. `DESIGN.md` and `PRODUCT.md` go at the root, and everything else goes in an `opendesigner/` folder. The token files there are the source of truth, and every other file is made from them.

{{figure:files-tree}}

A web-only sketch and build writes 50 files with no errors, and each extra platform adds its own export (51 with iOS).

## At the root of your project

- **`DESIGN.md`:** your design rules in plain words, for people and AI tools. It refreshes after every decision, and each section shows its zoom level.
- **`PRODUCT.md`:** what the product is, who it's for and where it runs, so later sessions don't have to guess.

## The tokens

**`opendesigner/tokens/`** holds 11 files in the open DTCG 2025.10 format: your palette and scales, the roles built on them, and a file for each color, density and motion mode. See [Design tokens and DTCG](/docs/design-tokens/).

:::dev
- `primitives.tokens.json`: the raw palette and scales;
- `semantic.tokens.json`: roles that don't change by mode;
- `semantic.color.light.tokens.json` and `semantic.color.dark.tokens.json`;
- three density files: spacious, comfortable and compact;
- `motion.standard.tokens.json` and `motion.reduced.tokens.json`;
- `opendesigner.resolver.json`, which ties the modes together;
- a small metadata file.
:::

## The exports

Every build rewrites the files in `opendesigner/build/`, so don't edit them by hand. The code files follow the platforms you chose, and `engine.py export --format all` writes every one.

{{figure:files-edit-exports}}

| In `build/` | What it is |
|---|---|
| `css/tokens.css` | CSS variables you can use in any web project |
| `tailwind/theme.css` | A Tailwind CSS v4 theme, so utility classes use your tokens |
| `figma/` | Figma variables: one import file per collection and mode in `figma/import/`, and `variables.json` for Tokens Studio |
| `paper/` | Tokens for the Paper design tool, in light and dark |
| `swift/DesignTokens.swift` | The same values for iOS apps |
| `compose/DesignTokens.kt` | The same values for Android apps built with Jetpack Compose |
| `dtcg/` | One DTCG resolver file for token tools that take a single entry point |
| `artifact/project/` | The system as files for a Claude Design System artifact: tokens, a brand book, a cover and a button preview |
| `brand/index.html` | A brand and press page you can host as it is, with your logo and icon files in `brand/assets/` |

See [Export](/docs/export/) for how to use each one.

## Pages you open in a browser

- **`opendesigner/overview.html`:** your whole system on one page, including what is still missing. It works offline and loads nothing from the web.
- **`opendesigner/preview.html`:** every token on one page.
- **`opendesigner/preview/`:** seven visual templates, such as the palette and the type scale, filled with your own values.

:::dev
The seven templates are palette, type scale, spacing ruler, radius, elevation, motion and component sheet. The option gallery is filled per question with `engine.py show`, and the taste poll is built by `taste.py build` into `opendesigner/preview/taste-poll/`.
:::

## The record

- **`opendesigner/decisions.md`:** every decision, how it was set and why. It's append-only, so a later session doesn't quietly undo a choice.
- **`opendesigner/standards.md`:** the house and project standards this project follows, locked, with their sources.
- **`opendesigner/state.json`:** where you left off, so you or another AI tool can continue later.
- **`opendesigner/standards-state.json`:** a copy of each standard as this system follows it. Keep it next to `state.json`.
- **`opendesigner/PROTOCOL.md`:** how work runs in this project: six steps, each ending at a gate where you say yes, and the checks every round runs. It's written once; edit it to fit. Its Now line says which step you're on, what waits for you and what comes next. The engine keeps that one line current, and `engine.py status` prints it.

See [Decisions, DESIGN.md and the overview page](/docs/decisions/).

## Written by the skill, or only when you ask

- **`opendesigner/RATIONALE.md`:** one page for the team on what was chosen, why, and what is still open, written by the skill from a template.
- **A short note in your `AGENTS.md`, and a `CLAUDE.md` that imports it,** added only after you say yes. You're asked once, and a no is remembered. The note tells later AI agents to read `DESIGN.md` and `RULES.md` first, use the tokens, and run `engine.py review` before every draft and commit.
- **`opendesigner/feedback.md`,** written only if you report something with `engine.py feedback`.
- **`opendesigner/RULES.md`,** written when you give a note on the work. A note you give twice becomes a rule that later sessions follow.
- **`opendesigner/research/`,** written only if you say yes to user research: the findings with their sources, the positioning and the direction board.
- **`opendesigner/references/`,** written only when you share a reference with the extract skill: the measurements taken from it.
- **`opendesigner/journey/`,** written only if you said yes to the private log.

## What to commit

Commit `DESIGN.md`, `PRODUCT.md` and the `opendesigner/` folder, so your team and your next AI session work from the same rules. The private log in `opendesigner/journey/` stays out of git.

You can commit the exports so your apps import them directly, or rebuild them with `engine.py build` whenever you need them.

## How the files relate

{{figure:how-it-works-pipeline}}

The decision log records why each value is what it is.

To change anything, record a decision with `engine.py set`, then run `engine.py build`. See [Engine commands](/docs/engine/).
