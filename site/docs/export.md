---
title: Export to code and design tools
seo_title: Export design tokens to CSS, Tailwind, Swift, Compose, Figma
description: Every format OpenDesigner exports, where each file lands, how to use it, and how the export skill writes into Figma and Paper when their MCP servers are on.
section: Guides
order: 6
updated: 2026-11-07
---

OpenDesigner exports your design system to code and design tools: CSS variables, a Tailwind v4 theme, Swift, Jetpack Compose, Figma variables, Paper tokens, a DTCG resolver, a Claude Design System artifact and a brand and press page. One `engine.py build` writes the ones your platforms need from the DTCG token files, which stay the source of truth. The opendesigner-export skill can also write the system straight into Figma or Paper when their MCP servers are connected.

## One rule: change the decision, then rebuild

Every export is made from the files in `opendesigner/tokens/`. Don't edit an export by hand, because the next build overwrites it. Change the decision instead, then rebuild.

{{figure:export-rebuild-not-edit}}

`build` generates the tokens and checks them. If there are no errors, it writes the exports, `DESIGN.md`, the overview page and the preview pages. Code exports follow the platforms you chose, and the build names what it left out. Figma, Paper, DTCG, the artifact files and the brand page are always written, and a code file already in `build/` is refreshed by every build.

:::dev
Change a decision and rebuild:

```
engine.py set dials.roundness 60 --why "softer corners for a friendlier feel"
engine.py build
```

Write one format, or all of them:

```
engine.py export --format tailwind
```

The formats are `css`, `tailwind`, `figma`, `paper`, `swift`, `compose`, `dtcg`, `artifact`, `brand` and `all`.
:::

## Code exports

{{figure:export-fan}}

| Export | File, inside `opendesigner/` | How to use it |
|---|---|---|
| Tokens | `tokens/`, with `opendesigner.resolver.json` for the modes | With token tools |
| DTCG resolver | `build/dtcg/` | With tools that take a single entry point |
| CSS | `build/css/tokens.css` | Import it once at the root of your app. Light and dark, densities and reduced motion included |
| Tailwind v4 | `build/tailwind/theme.css` | Add one line after Tailwind in your main CSS file. It imports `tokens.css` itself |
| Swift | `build/swift/DesignTokens.swift` | Add it to your iOS target. Text uses Dynamic Type |
| Jetpack Compose | `build/compose/DesignTokens.kt` | Add it to your Android UI module |
| Claude Design System artifact | `build/artifact/project/` | The system as an artifact in Claude: tokens, a brand book, a cover and a button preview |

*Each code export, where it lands and how to use it.*

The wiring for each one is on [For engineers](/docs/engineers/). If your brand font's licence doesn't cover apps, the Swift and Compose files use the system font instead and say so. Check this before you ship an app build.

## Brand and press page

`build/brand/index.html` is a page about your brand that you can host as it is, made from your tokens, in light and dark. It shows:

- your logo files with download links, the clear space and smallest size, and do and don't examples made from your own logo;
- every colour role with its hex, RGB and OKLCH values, and what it is for;
- each font with its weights, its jobs and a licence note;
- the icon grid and its rules, your icon files, and the open icon set you chose, with its licence.

Your short description, facts, leadership, figures and press contact say "Not enough information" until you give them. Nothing on the page is made up. Font files are never included: an open-licence font loads from Google Fonts, and any other font shows only on computers that have it installed. See [Brand assets](/docs/brand-assets/) for the logo rules.

## Figma

What the skill can do depends on what is connected, and it checks before it promises anything.

**With Figma's remote MCP server** (you're signed in, with a Full seat; writing to the canvas this way is still in beta), the skill:

1. confirms the target file with you, and suggests working on a duplicate first;
2. creates five variable collections: Primitives, Color (Light and Dark), Density (Spacious, Comfortable and Compact), Motion (Standard and Reduced), and Tokens for values that don't change by mode;
3. scopes each variable and sets its code syntax to the CSS variable name, so developers see `var(--ds-...)`;
4. adds text styles for the type scale and effect styles for the shadow levels;
5. builds specimen frames and a component sheet, bound to the variables;
6. reads the variables back and reports any mismatch with the tokens.

If a collection has more modes than your Figma plan allows, the engine splits it and warns you. When someone edits in Figma, the skill reads the changes back and records each one as a decision, never editing the token files directly.

**With Figma's desktop MCP server only,** it can read a file but not write to it, so it compares the file with your tokens.

**With nothing connected,** use the files in `build/figma/import/`, one per collection and mode, with Figma's variables import, or `build/figma/variables.json` with Tokens Studio. Figma's import takes one mode per file, sRGB colors, px units and no composite tokens.

{{figure:export-figma-collections}}

Hands-on Figma research is still an open task, so these steps rest on Figma's own docs.

## Paper

Paper's MCP server runs inside Paper Desktop on your computer. While it runs, the skill:

1. reads Paper's guide and looks at the file;
2. writes your tokens. Paper tokens have no modes, so the dark values go in a separate, clearly named set;
3. checks the fonts, then draws specimen artboards and a component sheet with your values;
4. checks each artboard with a screenshot and fixes clipping.

Comments and selections in Paper come back as decisions, the same way Figma edits do.

## Before you hand it over

- `engine.py validate` passes, or each warning has a written reason.
- Each export is explained in one plain sentence, with its path.
- Everyone knows the source is `opendesigner/tokens/`, and nobody edits exports by hand.

The skill asks before wiring an export into your code, such as your main CSS file or build config.

## What is early

- No direct React Native or Flutter export yet.
- The Figma and Paper writes depend on those tools' MCP servers, and no test pass in each tool is recorded yet.
- If an export is wrong or missing, record it with `engine.py feedback`. It prints a GitHub link you can file, and nothing is posted unless you submit it.
