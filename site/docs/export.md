---
title: Export to code and design tools
seo_title: Export design tokens to CSS, Tailwind, Swift, Compose, Figma
description: Every format OpenDesigner exports, where each file lands, how to use it, and how the export skill writes into Figma and Paper when their MCP servers are on.
section: Guides
order: 6
updated: 2026-10-14
---

OpenDesigner exports your design system to CSS variables, a Tailwind v4 theme, Swift, Jetpack Compose, Figma variables, Paper tokens, a DTCG resolver and files for a Claude Design System artifact. One `engine.py build` writes them all from the DTCG token files, which stay the source of truth. The opendesigner-export skill can also write the system straight into Figma or Paper when their MCP servers are connected.

## One rule: change the decision, then rebuild

The files in `opendesigner/tokens/` are the source. Every export is made from them. Don't edit an export by hand, because the next build overwrites it. Change the decision instead, then rebuild:

```
engine.py set dials.roundness 60 --why "softer corners for a friendlier feel"
engine.py build
```

{{figure:export-rebuild-not-edit}}

`build` generates the tokens and checks them. If there are no errors, it writes every export, `DESIGN.md`, the overview page and the preview pages. To write one format only:

```
engine.py export --format tailwind
```

The formats are `css`, `tailwind`, `figma`, `paper`, `swift`, `compose`, `dtcg`, `artifact` and `all`.

## Code exports

All paths are inside `opendesigner/`.

{{figure:export-fan}}

- **Tokens** (`tokens/`): DTCG sets plus `opendesigner.resolver.json` for the modes. Use them with token tools.
- **DTCG resolver** (`build/dtcg/`): one resolver file for tools that take a single entry point.
- **CSS** (`build/css/tokens.css`): custom properties for light and dark, densities and reduced motion. Import it once at the root of your app.
- **Tailwind v4** (`build/tailwind/theme.css`): a Tailwind `@theme` that imports `tokens.css` itself. Add one line after Tailwind in your main CSS file.
- **Swift** (`build/swift/DesignTokens.swift`): SwiftUI values with Dynamic Type text styles. Add it to your iOS target.
- **Jetpack Compose** (`build/compose/DesignTokens.kt`): add it to your Android UI module.
- **Claude Design System artifact** (`build/artifact/project/`): the system as files for an artifact in Claude, with tokens, a brand book, a cover and a button preview.

The wiring for each one is on [For engineers](/docs/engineers/).

If your brand font's licence doesn't cover apps, the Swift and Compose files use the system font instead and say so. Check this before you ship an app build.

## Figma

What the skill can do depends on what is connected. It checks before it promises anything.

### Figma's remote MCP server

This needs you to be signed in, with a Full seat. Writing to the canvas this way is still in beta. The skill:

1. confirms the target file with you, and suggests working on a duplicate first;
2. creates five variable collections: Primitives, Color (Light and Dark), Density (Spacious, Comfortable and Compact), Motion (Standard and Reduced), and Tokens for values that don't change by mode;
3. gives each variable a clear scope, and sets its code syntax to the CSS variable name, so developers see `var(--ds-...)`;
4. adds text styles for the type scale and effect styles for the shadow levels;
5. builds specimen frames for palette, type, spacing, corners and depth, plus a component sheet, all bound to the variables;
6. reads the variables back and reports any mismatch with the tokens.

Your Figma plan limits how many modes a collection can have. The engine splits a collection that goes over the limit and warns you.

When you or a designer edit in Figma, the skill reads the changes back and records each one as a decision. It never edits the token files directly.

### Figma's desktop MCP server only

This server can read a file but not write to it. The skill uses it to compare the file with your tokens.

### Nothing connected

Use the files in `build/figma/import/`, one per collection and mode, with Figma's variables import. Or use `build/figma/variables.json` with Tokens Studio. Figma imports this token format only in part: one mode per file, sRGB colors, px units, and no composite tokens.

{{figure:export-figma-collections}}

Hands-on Figma research is still an open task, so the Figma steps rest on Figma's own docs.

## Paper

Paper's MCP server runs inside Paper Desktop on your computer. When it is running, the skill:

1. reads Paper's guide and looks at the file;
2. writes your tokens. Paper tokens have no modes, so it writes the light values and adds the dark ones as a separate, clearly named set;
3. checks the fonts, then draws specimen artboards: palette, type, spacing, corners, depth and a component sheet, using your values;
4. checks each artboard with a screenshot and fixes clipping.

Comments and selections a designer makes in Paper come back as decisions, the same way Figma edits do.

## Before you hand it over

- `engine.py validate` passes, or each warning has a written reason.
- Each export is explained in one plain sentence, with its path.
- Everyone knows the source is `opendesigner/tokens/`. Exports are rebuilt from it, and nobody edits them by hand.

The skill asks before wiring an export into your code, such as your main CSS file or build config.

## What is early

- No direct React Native or Flutter export yet.
- The Figma and Paper writes depend on those tools' MCP servers, and no test pass in each tool is recorded yet.
- If an export is wrong or missing, record it with `engine.py feedback`. It prints a GitHub link you can file, and nothing is posted unless you submit it.
