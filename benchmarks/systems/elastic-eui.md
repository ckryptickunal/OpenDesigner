# Elastic EUI (Borealis)

_Lane L09 teardown. Checked on 2026-09-25. Numeric theme snapshot: published `@elastic/eui-theme-borealis` 8.1.0. This is not a claim that all EUI themes have these values._

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Owner / distribution | Elastic; theme package `@elastic/eui-theme-borealis` 8.1.0, exported as `EuiThemeBorealis` | [S-L09-777] [S-L09-778] |
| License | Dual choice of Elastic License 2.0 or SSPL v1, not MIT | [S-L09-780] [S-L09-781] |
| Token model | JS theme groups include `size`, `font`, `border` and `animation`; computed values depend on a base size of 16 | [S-L09-780] [S-L09-781] [S-L09-782] |
| Color | Published light JSON: primary `#0B64DD`, primary text `#1750BA`, body text `#384861`, empty shade `#FFFFFF`. Dark: primary `#61A2FF`, body text `#B4C1D5`, empty shade `#111C2C` | [S-L09-779] [S-L09-783] |
| Typeface | Inter first in the sans stack, Roboto Mono first in code. Source serif fallback Georgia. Source line-height multiplier 1.5 | [S-L09-779] [S-L09-780] |
| Type scale | Source factors .5625 / .6875 / .75 / .875 / 1 / 1.25 / 1.5 / 1.875 times 16: 9 / 11 / 12 / 14 / 16 / 20 / 24 / 30px equivalents. Body uses scale `s` (14px) | [S-L09-780] [S-L09-779] |
| Font weights | light 300, regular 400, medium 450, semiBold 500, bold 600. These semantic labels do not imply 500 / 600 / 700 | [S-L09-780] |
| Spacing | `xxs/xs/s/m/base/l/xl/xxl/xxxl/xxxxl`: 2 / 4 / 8 / 12 / 16 / 24 / 32 / 40 / 48 / 64px | [S-L09-782] [S-L09-785] |
| Radius | small / medium / inline 4px; control 8px; panel 12px; frame 16px. Avoid using the generic 4px token to describe every component | [S-L09-781] [S-L09-779] |
| Border | Thin 1px, thick 2px; editable uses a dotted 2px border. Color is a semantic dependency rather than a fixed gray | [S-L09-781] |
| Motion | extraFast / fast / normal / slow / extraSlow: 90 / 150 / 250 / 350 / 500ms. Bounce `(0.34,1.61,0.7,1)` and resistance `(0.32,0.72,0,1)` cubic curves | [S-L09-784] |
| Modes | Separate light and dark theme values; high contrast is another provider option, not synonymous with dark mode | [S-L09-779] [S-L09-783] [S-L09-786] |
| Accessibility stance | Guidelines target WCAG 2.1 and require application-level semantics, keyboard behavior, focus management and testing; no automatic whole-app conformance claim | [S-L09-838] |

## Visual signature: why it looks like this

- 14px body text and 2/4/8/12px small spacing support dense data interfaces; larger role-based corners soften controls and panels without making all elements pill-shaped. [S-L09-779] [S-L09-781] [S-L09-782] [inferred]
- Primary paint and primary text differ in the light palette. A generator should retain that distinction rather than applying the button color to every link. [S-L09-779] [inferred]
- Weight labels map to comparatively light numbers: a consumer that substitutes generic CSS `bold` changes the measured hierarchy. [S-L09-780] [inferred]

## Version notes and disagreements

The live border documentation displays `#E3E8F2` for its border sample. Borealis 8.1.0's published light JSON has `euiColorLightShade = #CAD3E2`, while the pinned TypeScript border uses `colors.borderBaseSubdued`. These are different named surfaces and potentially different documentation/theme contexts: this entry does not force them into one supposedly universal border color. Its radius row uses the published theme and source, including control/panel/frame roles absent from the docs' short small/medium table. [S-L09-779] [S-L09-781] [S-L09-837]

## Builder takeaways

- Store theme identity and version with every value. [inferred]
- Model high contrast separately from light/dark. [S-L09-786] [inferred]
- Keep semantic font weights and radius roles instead of replacing them with a generic small/medium/large scale. [inferred]

## Gaps / unverified

This pass did not count components, inspect the Figma library, execute a component application, or audit reduced-motion behavior and all shadow presets. The source files are pinned; the published JSON supplies the release-specific color evidence.
