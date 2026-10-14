---
title: For engineers
seo_title: OpenDesigner for engineers: tokens, CSS, Tailwind v4, Swift
description: The tokens and code exports OpenDesigner writes, how to wire them into web, iOS and Android apps, how review finds hard-coded values, and how agents use them.
section: Guides
order: 3
updated: 2026-10-14
---

OpenDesigner turns design decisions into files you import: DTCG 2025.10 tokens, CSS variables, a Tailwind v4 theme, Swift and Jetpack Compose files, and a DTCG resolver. `engine.py review` finds values typed straight into your code that skip the tokens. `DESIGN.md` and a short note in `AGENTS.md` tell coding agents to use the tokens too.

## What you get

All paths are inside `opendesigner/` in your project.

- `tokens/`: the source of truth, in DTCG 2025.10 format. Light and dark, three densities and reduced motion are modes, tied together by `opendesigner.resolver.json`.
- `build/css/tokens.css`: CSS custom properties, named `--ds-...`.
- `build/tailwind/theme.css`: a Tailwind CSS v4 theme.
- `build/swift/DesignTokens.swift`: SwiftUI values under `DS`.
- `build/compose/DesignTokens.kt`: Jetpack Compose values.
- `build/dtcg/`: one resolver file for tools that take a single entry point.

Never edit an export by hand. Change the decision and rebuild, and every export updates together.

## Wire it in

### Plain CSS

Import the file once at the root of your app, then use the variables:

```css
@import "../opendesigner/build/css/tokens.css";

.card {
  background: var(--ds-color-surface-raised);
  color: var(--ds-color-text-primary);
}
```

Dark mode follows `prefers-color-scheme`. Set `data-theme="light"` or `data-theme="dark"` to override it. Density switches with `data-density` (spacious, comfortable or compact). Reduced motion follows `prefers-reduced-motion`, with a `data-motion` override. Font sizes are in rem, so browser text zoom works.

### Tailwind v4

Add two lines to your main CSS file, for example `src/index.css`. Adjust the path to where that file sits:

```css
@import "tailwindcss";
@import "../opendesigner/build/tailwind/theme.css";
```

`theme.css` imports `tokens.css` itself, so modes keep working. Classes follow the token roles, such as `bg-action-primary`, `text-fg-primary`, `rounded-control` and `h-control-md`. `DESIGN.md` lists the class for each role.

By default, the export switches off Tailwind's own colors, text sizes, radii and shadows. That way a stray `bg-blue-600` or `rounded-lg` doesn't compile. To keep them, run `engine.py set exports.tailwindReset false`, then `engine.py build`.

### iOS

Add `DesignTokens.swift` to your iOS target. Colors switch with the system appearance, for example `DS.Colors.textPrimary`. Text uses Dynamic Type text styles, so it follows the person's text size setting.

### Android

Add `DesignTokens.kt` to your Android UI module. It holds light and dark color sets plus spacing, type and motion values.

If the brand font's licence doesn't cover apps, the Swift and Compose files use the system font instead, and say so.

### Token tools

Point your token tool at `tokens/opendesigner.resolver.json`, or at the single file in `build/dtcg/`. The export skill names Style Dictionary, Terrazzo, Tokens Studio and Penpot as tools that read this format. We have not tested any of them yet.

## Add a value the system lacks

First check that no existing token fits. If none does, add one through the engine with a reason:

```
engine.py set size.row.md 36 --why "table rows in the jobs list"
engine.py set color.bg.highlight '"#fff4c2"' --why "highlighted search matches"
engine.py set dark:color.bg.highlight '"#3a3000"' --why "the same highlight in dark mode"
engine.py build
```

A new color still has to pass the contrast check. `build` reports it if it doesn't.

## Find hard-coded values

Run this at the end of any piece of work:

```
engine.py review --project src
```

It reads style sheets, JavaScript and TypeScript, Vue, Svelte, HTML, Swift and Kotlin files. It finds colors, sizes, radii, shadows and durations typed in by hand and names the token to use instead. Here is part of the output from a test run:

```
card.css:1  #f3f4f6  ->  use var(--ds-color-surface-sunken)
card.css:1  border-radius: 7px  ->  use var(--ds-radius-container) (12px, the container radius)
card.css:1  padding: 13px  ->  use var(--ds-space-12) (13 is off the 4px ladder)
```

It also lists code that breaks a standard, and `DESIGN.md` sections that are out of date. Add the comment `od-ignore` to a line to keep a raw value on purpose. `--strict` makes the command fail when it finds anything, and `--json` prints machine-readable output.

## DESIGN.md and AGENTS.md for coding agents

`DESIGN.md` has a section for AI agents. It tells them to read the file and the tokens before changing any screen, to use tokens instead of raw values, and to leave locked decisions alone.

At the end of a session, OpenDesigner asks whether to add a short note to your `AGENTS.md`. It adds it only after you say yes. The note tells later agents to:

- read `DESIGN.md` and `PRODUCT.md` before any visual work;
- use the tokens or their exports, and never hard-code colors, sizes, spacing, radii, shadows or durations;
- check `opendesigner/decisions.md` for why a value is what it is;
- run `engine.py review` at the end of every implementation and fix what it finds.

## About the engine

The engine is one Python file that needs Python 3.10 or newer. It uses only the standard library and makes no network calls. The same `state.json` gives the same tokens. It has 119 tests, which pass on the maintainer's computer. No CI runs are recorded yet.

## Not yet

- No direct React Native or Flutter export.
- Only buttons, a text field and a card are previewed as components.

See [Engine commands](/docs/engine/) and [Export](/docs/export/) for more.
