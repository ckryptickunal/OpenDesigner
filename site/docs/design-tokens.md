---
title: Design tokens and DTCG
seo_title: Design tokens and the DTCG 2025.10 format, in plain words
description: What design tokens are, the three tiers of tokens, what the DTCG 2025.10 format and its resolver do, and how OpenDesigner stores and exports its tokens.
section: Concepts
order: 2
updated: 2026-11-09
---

Design tokens are design decisions saved as named values, so code, design tools and AI agents all read the same values. DTCG is the open file format for tokens. OpenDesigner keeps every token in this format and makes all its other files from it.

## Why tokens help

When a value has a name, you change it in one place and every use follows. A button and a link that point to the same accent token change together. Without tokens, someone has to find every copy by hand, and some get missed.

Names also carry meaning. "Primary text color" tells a person or an AI what a value is for. A raw color code doesn't.

## Three tiers of tokens

Most systems sort tokens into three tiers:

| Tier | What it holds | Example |
|---|---|---|
| Primitives | The raw palette and scales | Twelve steps of a neutral gray |
| Semantic tokens | Roles, which point to primitives | Body text, the page background |
| Component tokens | Values for one component | A button's height |

Components use the roles, never the primitives directly. That way dark mode can point the same role at a different shade.

{{figure:design-tokens-tiers}}

:::dev
A real pair from an OpenDesigner test run. The primitive holds the color:

```json
"12": {
  "$value": { "colorSpace": "oklch", "components": [0.2613, 0.008, 58.0], "hex": "#272321" },
  "$description": "high-contrast text"
}
```

The semantic token points to it:

```json
"primary": {
  "$value": "{color.neutral.light.12}",
  "$description": "Body copy, headings, labels (guaranteed >= 7:1 on steps 1-5)."
}
```

In the CSS export, that becomes `--ds-color-text-primary`. A name like `color.text.primary` says what the value is for; the raw hex `#272321` doesn't.
:::

## Tokens for tables and charts

Work tools show most of their data in tables and charts, so both get their own tokens.

- **Tables** get four row heights, and number styles whose digits all have the same width, so columns line up. One question decides how rows are separated (lines, striped rows or space), whether the header stays on screen, and how numbers align.
- **Charts** get colors when the chart question asks for them: one color for a single series, a fixed order for groups, light to dark for amounts, a scale around a midpoint, and status colors used with a label. Axes and gridlines use the app's own border and text colors.

A line, a bar or a dot in a chart reaches 3:1 against the page, the WCAG minimum for shapes people need to see. The palest shades for amounts don't: they're for cells that touch, as in a heatmap, with a 1 px gap between cells or the value written in each one. Marks don't reach 3:1 against each other either, so leave a gap or a thin line between neighbors.

:::dev
**Tables.** Rows come in four heights: `size.row.sm`, `md`, `lg` and `two-line`. Numbers use the `text.numeric.*` styles. The question is Q-pattern-07. Striped rows add one color, `color.surface.row-alternate`, one step away from the page. The other answers become rules in `DESIGN.md`.

**Charts.** When the chart question (Q-color-19) asks for chart colors, the system adds:

- `color.chart.brand` for a chart with one series, and `color.chart.categorical.*` for groups, in a fixed order.
- `color.chart.sequential.*` for amounts, from light to dark. The light end is under 3:1 against the page, and each step's description says so. `engine.py review` warns when a line is drawn in one of those steps.
- `color.chart.diverging.1` to `7` for values below and above a midpoint. Step 4 is the midpoint.
- `color.chart.status.*` for success, warning and danger, used with a label.
- `color.chart.axis`, `gridline`, `label` and `reference`, which point at the border and text colors, so charts look like the rest of the app.

Every export carries these tokens, including CSS, Tailwind, Swift, Compose and Figma.
:::

## The DTCG format

DTCG is short for the Design Tokens Community Group, a W3C Community Group. Its specification stores tokens as JSON. Version 2025.10, its first stable version, was published on 28 October 2025. It has three modules:

| Module | What it covers |
|---|---|
| [Format](https://www.designtokens.org/TR/2025.10/format/) | How tokens and groups of tokens are written |
| [Color](https://www.designtokens.org/TR/2025.10/color/) | How colors are written, in color spaces such as OKLCH |
| [Resolver](https://www.designtokens.org/TR/2025.10/resolver/) | How sets of tokens combine for settings such as light and dark mode |

:::dev
Each token has a `$value`, and can have a `$type` and a `$description`. In the resolver, sets of tokens combine through switches called modifiers.
:::

## Modes and the resolver

A mode is a version of the same tokens for a different setting, such as dark mode. OpenDesigner has three independent switches:

- **Theme:** light or dark. Dark mode has its own set of color choices.
- **Density:** spacious, comfortable or compact. Target sizes never shrink.
- **Motion:** standard or reduced.

No two switches set the same token, so any combination works.

{{figure:design-tokens-resolver}}

:::dev
The switches are `theme`, `density` and `motion`, in one resolver file, `opendesigner.resolver.json`. In a test run, the engine checked 164 color pairs in every mode and 12 mode combinations.
:::

## Where OpenDesigner keeps its tokens

Your tokens live in one folder in your project, and that folder is the source of truth. A build makes the other files from it: code for the platforms you chose, Figma variables and Paper tokens. See [Export](/docs/export/) for each file.

:::dev
`opendesigner/tokens/` holds 11 files: the primitives, the semantic tokens, one file per theme, one per density, one per motion mode, a small metadata file and the resolver.

A build makes these from the tokens:

- CSS variables and a Tailwind v4 theme, for the web;
- Swift and Jetpack Compose files, for iOS and Android;
- Figma variables, one import file per mode, and Paper tokens;
- a single DTCG resolver file for tools that take one entry point.

The code files follow the platforms you chose. `engine.py export --format all` writes every one.
:::

## Tokens and Figma

Figma can import DTCG tokens, but with limits, so OpenDesigner also writes Figma variable files directly.

:::dev
Figma's limits: one mode per file, sRGB or HSL colors, px units, and no composite tokens. OpenDesigner writes one Figma variable file per collection and mode.
:::

## Changing a token

Don't edit token files by hand. Record the change as a decision, then rebuild. The engine writes the token to the right file, checks contrast and updates the exports. The decision log keeps the reason. See [Decisions, DESIGN.md and the overview page](/docs/decisions/).

:::dev
```
engine.py set color.bg.highlight '"#fff4c2"' --why "highlighted search matches"
engine.py build
```
:::

## Sources

- [Design Tokens Community Group announcement of 2025.10](https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/)
- [Design Tokens specification 2025.10](https://www.designtokens.org/TR/2025.10/)
