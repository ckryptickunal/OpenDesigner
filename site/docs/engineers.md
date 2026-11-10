---
title: For engineers
seo_title: OpenDesigner for engineers: tokens, CSS, Tailwind v4, Swift
description: The tokens and code exports OpenDesigner writes, how to wire them into web, iOS and Android apps, how review finds hard-coded values, and how agents use them.
section: Guides
order: 3
updated: 2026-11-10
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

`build` writes the code files for the platforms you chose: CSS and Tailwind for the web, Swift for iOS, Compose for Android. For another, run `engine.py export --format swift` (or `compose`, `css`, `tailwind`, `all`).

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

{{figure:engineers-token-not-raw}}

### Tailwind v4

Add two lines to your main CSS file, such as `src/index.css`, and adjust the path:

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

It reads style sheets, JavaScript and TypeScript, Vue, Svelte, HTML, Swift and Kotlin files, finds colors, sizes, radii, shadows and durations typed in by hand, and names the token to use instead. Part of the output from a test run:

```
card.css:1  #f3f4f6  ->  use var(--ds-color-surface-sunken)
card.css:1  border-radius: 7px  ->  use var(--ds-radius-container) (12px, the container radius)
card.css:1  padding: 13px  ->  use var(--ds-space-12) (13 is off the 4px ladder)
```

It also lists code that breaks a standard or brings back something removed on purpose, and `DESIGN.md` sections that are out of date. To keep a raw value on purpose, add a comment with the reason on that line: `od-ignore: <why>`. A comment without a reason shows as a note. The last line reads `Review: ok`, or how many things are left to fix and why. `--strict` makes the command fail unless it's ok, and `--json` prints machine-readable output.

{{figure:engineers-review-terminal}}

## DESIGN.md and AGENTS.md for coding agents

`DESIGN.md` has a section for AI agents: read the file and the tokens before changing any screen, use tokens instead of raw values, and leave locked decisions alone. At the end of a session, OpenDesigner offers to add a short note to your `AGENTS.md` that says the same, points to `opendesigner/decisions.md` for why a value is what it is, and asks for `engine.py review` at the end of every implementation. It adds the note only after you say yes. A first version gets a shorter note without the strict rules, and the note grows in place once you decide more or ask for stricter rules.

{{figure:engineers-agent-rules}}

For a Cursor rule file and a `CLAUDE.md` line that point at `DESIGN.md`, see [A design system for Cursor](/docs/design-system-for-cursor/) and [Design tokens for Claude Code](/docs/design-tokens-for-claude-code/).

## About the engine

The engine is one Python file that needs Python 3.10 or newer. It uses only the standard library and makes no network calls, and the same `state.json` gives the same tokens. Every build checks every text, border, icon and focus-ring color pair the tokens promise, in light and dark mode, including text on hover and pressed fills; a failing pair stops the build. It has more than 200 tests, which pass on the maintainer's computer. No CI runs are recorded yet.

## Not yet

- No direct React Native or Flutter export.
- The overview page draws only buttons, a text field and a card. The optional [component library](/library/) has 82 finished components built on the tokens.

See [Engine commands](/docs/engine/) and [Export](/docs/export/) for more.
