---
title: Design tokens and DTCG
seo_title: Design tokens and the DTCG 2025.10 format, in plain words
description: What design tokens are, the three tiers of tokens, what the DTCG 2025.10 format and its resolver do, and how OpenDesigner stores and exports its tokens.
section: Concepts
order: 2
updated: 2026-10-14
---

Design tokens are design decisions saved as named values, such as `color.text.primary` or `space.4`, so code, design tools and AI agents all read the same values. DTCG is the open file format for tokens from the Design Tokens Community Group, and 2025.10 is its first stable version. OpenDesigner keeps every token in this format and makes all its other files from it.

## Why tokens help

When a value has a name, you change it in one place and every use follows. A button, a link and a focus ring that all point to the same accent token change together. Without tokens, someone has to find every copy of the value by hand, and some get missed.

Names also carry meaning. `color.text.primary` tells a person or an AI what the value is for. A raw hex value like `#272321` does not.

## Three tiers of tokens

Most systems sort tokens into three tiers:

- **Primitives:** the raw palette and scales, such as twelve steps of a neutral gray.
- **Semantic tokens:** roles, such as "body text" or "the page background". They point to primitives.
- **Component tokens:** values for one component, such as a button's height.

Here is a real pair from an OpenDesigner test run. The primitive holds the color:

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

In the CSS export, that becomes `--ds-color-text-primary`. Components use the semantic roles. They don't use the primitives directly. That way a dark-mode mapping can point the same role at a different shade.

{{figure:design-tokens-tiers}}

## The DTCG format

DTCG is short for the Design Tokens Community Group, a W3C Community Group. Its specification stores tokens as JSON. Each token has a `$value`, and can have a `$type` and a `$description`. Version 2025.10, its first stable version, was published on 28 October 2025.

The 2025.10 specification has three modules:

- [Format](https://www.designtokens.org/TR/2025.10/format/): how tokens and groups of tokens are written in JSON.
- [Color](https://www.designtokens.org/TR/2025.10/color/): how colors are written, with the color spaces it supports, such as OKLCH.
- [Resolver](https://www.designtokens.org/TR/2025.10/resolver/): how sets of tokens and switches called modifiers combine for contexts such as light and dark mode.

## Modes and the resolver

A mode is a version of the same tokens for a different setting, such as dark mode. OpenDesigner writes one resolver file, `opendesigner.resolver.json`, with three independent switches:

- **theme:** light or dark. Dark mode has its own set of color choices.
- **density:** spacious, comfortable or compact. Target sizes never shrink.
- **motion:** standard or reduced.

No two switches set the same token, so any combination works. In a test run, the engine checked 164 color pairs in every mode and 12 mode combinations.

{{figure:design-tokens-resolver}}

## Where OpenDesigner keeps its tokens

`opendesigner/tokens/` holds 11 files: the primitives, the semantic tokens, one file per theme, one per density, one per motion mode, a small metadata file and the resolver. This folder is the source of truth.

Every build makes these from the tokens:

- CSS variables and a Tailwind v4 theme;
- Swift and Jetpack Compose files;
- Figma variables, one import file per mode, and Paper tokens;
- a single DTCG resolver file for tools that take one entry point.

See [Export](/docs/export/) for each file.

## Tokens and Figma

Figma can import DTCG tokens, with limits: one mode per file, sRGB or HSL colors, px units, and no composite tokens. That is why OpenDesigner also writes Figma variable files directly, one per collection and mode.

## Changing a token

Don't edit token files by hand. Record the change as a decision, then rebuild:

```
engine.py set color.bg.highlight '"#fff4c2"' --why "highlighted search matches"
engine.py build
```

The engine writes the token to the right file, checks contrast, and updates every export. The decision log keeps the reason. See [Decisions, DESIGN.md and the overview page](/docs/decisions/).

## Sources

- [Design Tokens Community Group announcement of 2025.10](https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/)
- [Design Tokens specification 2025.10](https://www.designtokens.org/TR/2025.10/)
