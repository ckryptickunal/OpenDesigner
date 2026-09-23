# Atlassian Design System (ADS)

_Lane L09 teardown. Verified against live sources on 2026-09-23. Every value carries an [S-L09-xxx] id from `traces/L09-trace.md` or the tag [inferred]._

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Owner | Atlassian (Atlassian Design System team) | [S-L09-252] |
| Launch and major versions | Atlaskit packages first on npm 2017-01-29 (`@atlaskit/button`, `@atlaskit/icon`). `@atlaskit/tokens` 1.0.0 2023-02-07; `@atlaskit/primitives` 1.0.0 2023-07-06. New brand and design direction announced at Team '25 (April 2025); typography GA 2025-09-09; refreshed themes became default in tokens 8.0.0 (2025-11-07). No system-wide major version; each package is versioned on its own | [S-L09-246] [S-L09-252] [S-L09-249] |
| Current version (Sept 2026) | `@atlaskit/tokens` 19.0.0, `@atlaskit/primitives` 22.5.3, `@atlaskit/button` 25.4.1, `@atlaskit/icon` 37.7.3 (all 2026-09-23) | [S-L09-246] |
| Platforms | Web (React). Forge UI Kit and Brand kit are listed on the site as separate "other libraries" | [S-L09-246] [S-L09-252] |
| Open source + license | Source published on npm under Apache-2.0; contributions from Atlassians only | [S-L09-246] [S-L09-254] |
| Code frameworks | React components (Atlaskit), primitives (`Box`, `Stack`, `Inline`, `Text`, `Pressable`, `Flex`, `Grid`, `Bleed`; `@atlaskit/primitives/compiled` recommended), Compiled CSS-in-JS (`@atlaskit/css`), tokens as CSS variables `--ds-*`, ESLint plugin, `@atlaskit/ads-mcp` | [S-L09-250] [S-L09-246] |
| Figma kit | Atlassian-internal Figma libraries plus a public "community Figma library" (components and foundations) for Marketplace partners. Variables not confirmed | [S-L09-252] [S-L09-255] |
| Token tiers + naming | 2 public tiers, dot-path names mapped to `--ds-` variables. Palette: `color.palette.Blue700` (#1868DB). Design tokens: `color.background.brand.bold`, `elevation.surface.raised`, `space.100`, `font.heading.xxlarge`, `radius.medium`. Motion adds per-pattern tokens (`motion.modal.enter`). 600 token names: 442 color, 76 motion, 23 space, 23 font, 21 elevation, 8 radius | [S-L09-248] [S-L09-247] |
| Color model | 9 hues (Lime, Red, Orange, Yellow, Green, Teal, Blue, Purple, Magenta) x 12 steps (100, 200, 250, 300, 400, 500, 600, 700, 800, 850, 900, 1000) + Neutral (18 incl. alpha) + DarkNeutral (22). Hex with 8-digit alpha. 466 color variables per theme (208 background, 100 chart, 49 text, 40 border, 23 icon, 14 Rovo, 13 surface). Accent `background.brand.bold` #1868DB light / #669DF1 dark. Hand-picked palette [inferred] | [S-L09-248] [S-L09-247] |
| Typeface | Atlassian Sans (a derivative of Inter Variable) and Atlassian Mono (a derivative of JetBrains Mono). Custom. Brand/marketing typeface is Charlie | [S-L09-247] [S-L09-252] |
| Type scale | 14 styles. Headings (weight 653): xxlarge 32/36, xlarge 28/32, large 24/28, medium 20/24, small 16/20, xsmall 14/20, xxsmall 12/16. Body (400): large 16/24, body 14/20, small 12/16. Metric (653): 28/32, 24/28, 16/20. Code 0.875em. Weights 400 / 500 / 600 / 653. Built on a minor-third scale | [S-L09-247] [S-L09-252] |
| Spacing | 8px base. `space.0..1000` = 0, 2, 4, 6, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80px (`space.025` = 2px, `space.100` = 8px). Negatives -2 to -32px | [S-L09-247] |
| Radius | `radius.xsmall` 2px (badges, checkboxes), `small` 4px (lozenges, tags, tooltips), `medium` 6px (buttons, inputs, selects), `large` 8px (cards, dropdowns), `xlarge` 12px (modals, tables), `xxlarge` 16px (video), `full` 9999px (avatars), `tile` 25%. Border widths 1px, selected 2px, focused 2px. Radius is Beta; shape theme on by default since tokens 17.0.0 (2026-09-15) | [S-L09-247] [S-L09-253] [S-L09-249] |
| Elevation | Surfaces + shadows. 4 levels (sunken, default, raised, overlay) + overflow. Light: sunken #F8F8F8, surface/raised/overlay #FFFFFF; `shadow.raised` 0 1px 1px #1E1F2140 + 0 0 1px #1E1F214F; `shadow.overlay` 0 8px 12px #1E1F2126 + 0 0 1px #1E1F214F. Dark: surfaces get lighter as they rise (#18191A, #1F1F21, #242528, #2B2C2F) | [S-L09-247] [S-L09-253] |
| Motion | Durations instant 0, xxshort 50, xshort 100, short 150, medium 200, long 250, xlong 400, xxlong 600ms. Easing in-practical (0.6,0,0.8,0.6), out-practical (0.4,1,0.6,1), out-bold (0,0.4,0,1), inout-bold (0.4,0,0,1), spring as CSS `linear()`. Per-pattern tokens, e.g. modal enter 250ms inout-bold scale 95-100%; popup enter 150ms slide 8px + fade. Early Access behind `platform-dst-motion-uplift`; guidance says motion honors reduced-motion settings | [S-L09-247] [S-L09-253] |
| Theming + modes | Light, dark and auto via `setGlobalTheme` / `data-color-mode` + `data-theme` on `<html>`. Increased-contrast light and dark themes; legacy light/dark themes. Spacing, typography, shape and motion are separate opt-in theme parts. FY27 "Finesse" override themes behind a flag. No public multi-brand theming [inferred] | [S-L09-249] [S-L09-247] [S-L09-248] |
| Component count | About 69 UI components: 76 entries on atlassian.design/components minus 7 tooling packages (css, css-reset, 2 ESLint plugins, Storybook addon, stylelint, tokens), read 2026-09-23. `llms-components.txt` covers 58 packages with 147 component exports | [S-L09-251] [S-L09-250] |
| Component doc structure | Tabs: Examples, Code, Usage, Changelog | [S-L09-254] |
| Accessibility stance | WCAG 2.1 AA. Text under 24px must pass 4.5:1; large text and UI parts 3:1. Increased-contrast themes ship in the token package | [S-L09-250] [S-L09-253] [S-L09-248] |
| Governance / contribution | Central ADS team. Release phases: Early Access (0.x, may break), Beta (1.0+, supported), GA, then Intent to Deprecate and Deprecated. Contributions are Atlassians-only via Slack; outsiders use a feedback collector. Rollouts go through feature flags (`platform-dst-*`) | [S-L09-254] [S-L09-253] [S-L09-249] |
| Notable innovation | Theme "parts" (color, spacing, typography, shape, motion) loaded as separate CSS layers; dark-mode elevation by surface lightness; motion tokens as full CSS animation shorthands per pattern; Rovo UI layer for AI (color, motion, generative border); `llms.txt` and an MCP package | [S-L09-247] [S-L09-253] [S-L09-254] [S-L09-250] |

## Visual signature: why it looks like this
- Atlassian Sans (Inter-derived) at 14/20 body with 653-weight headings -> crisp, modern SaaS text with a clear heading ladder. [S-L09-247] [S-L09-252]
- 6px radius on buttons and inputs, 8px on cards, 12px on modals -> soft but not pill-shaped. [S-L09-253]
- Near-black neutral text (#292A2E, subtle #505258) and a single brand blue (#1868DB) -> calm screens where blue means action. [S-L09-247]
- Alpha-based borders (#0B120E24) and tinted neutral fills (#0515240F) instead of solid grays -> light, layered surfaces that adapt to any background. [S-L09-247]
- Minimal shadows (a 1px shadow plus a 1px outline for raised cards) -> mostly flat UI; dark mode shows height with lighter surfaces. [S-L09-247] [S-L09-253]
- New icons drawn with a 1.5px stroke on a 16px canvas (legacy: 2px on 24px) -> lighter glyphs that sit well next to text. [S-L09-252]

## Recent changes 2024-2026
- 2024-07-18: tokens 1.56.0 adds "brand refresh" colors and tokens behind a feature flag. [S-L09-249]
- 2024-11-21: tokens 2.3.0; the refreshed typography theme now references Atlassian Sans. [S-L09-246] [S-L09-249]
- 2025-03-18: typography and iconography updates announced; buttons and links revamped. [S-L09-252]
- April 2025: new brand and design direction announced at Team '25; UI refresh roundup 2025-04-22 (new colors "being trialed" then). [S-L09-252]
- 2025-09-08: new icon system (replaces 350+ legacy icons). 2025-09-09: typography GA with Atlassian Sans and Mono; legacy type supported until Jan 2026. [S-L09-252]
- 2025-11-07: tokens 8.0.0 makes the refreshed light and dark themes the default (visual-refresh flag removed). [S-L09-249]
- 2026-04-29: tokens 13.0.2 updates the structured docs to cover motion tokens. Motion is still Early Access behind a flag. [S-L09-249] [S-L09-253]
- 2026-06-16: `@atlaskit/ads-mcp` 1.0.0 (package first published 2025-06-06) and `@atlaskit/css` 1.0.0. [S-L09-246]
- 2026-09-02: FY27 "Finesse" overrides behind `platform-dst-tokens-finesse`: neutral dark selected state (#292A2E) and weight 500 for medium and smaller headings. [S-L09-249] [S-L09-247]
- 2026-09-15: tokens 17.0.0 turns the shape (radius) theme on by default (repeated in 18.0.0 on 2026-09-17). [S-L09-249] [S-L09-246]
- 2026-09-23: tokens 19.0.0 merges `motion.input.hovered` and `motion.input.focused` into `motion.input`. [S-L09-249]

## Builder takeaways
- Let users switch on theme parts one at a time (color, spacing, typography, shape, motion). It makes migration and A/B rollouts easy.
- Offer semantic motion tokens per pattern (enter, exit, hover for modal, popup, panel), not only duration and easing primitives.
- Offer ADS-style release phases (Early Access, Beta, GA, deprecation) as a governance preset for generated components.
- For dark mode, offer "lighter surface = higher elevation" plus increased-contrast variants as defaults.

## Gaps / unverified
- Figma libraries page and accessibility page render in JS; Figma variables and the full accessibility statement were not read. [S-L09-255]
- Licensing of Atlassian Sans outside Atlassian products not found.
- History before Atlaskit (Atlassian Design Guidelines, ADG) not dated from a primary source.
- The brief mentioned "Charlie Sans". Sources name the brand typeface "Charlie" and the UI font "Atlassian Sans". [S-L09-252]
- Motion is Early Access; values may change. Radius and border are Beta. [S-L09-253]
- How the palette was generated is not documented in the sources read; treated as hand-picked [inferred].
- "Future" and "new input border" override themes ship in the package (e.g. `border.input` #8590A2) but are not described in the docs. [S-L09-247]
- Grid foundation values (columns, breakpoints) were not captured.
- Rovo UI (the AI layer) was read only at the index level; beyond the 14 `rovo` color tokens its values were not captured. [S-L09-254] [S-L09-247]
- The 100 chart color tokens were counted but not analysed. [S-L09-247]
- `llms.txt` marks the non-compiled `@atlaskit/primitives` entry as legacy and deprecated; the date of that change was not found. [S-L09-250]
- The motion token file has no `prefers-reduced-motion` query; how reduced motion is applied in code was not checked. [S-L09-247] [S-L09-253]
