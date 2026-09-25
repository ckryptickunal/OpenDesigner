# Porsche Design System

_Lane L09 teardown. Checked on 2026-09-25. This snapshot is explicitly for the published `@porsche-design-system/components-js` 4.7.0 package and v4 documentation._

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Owner / release | Porsche AG; `@porsche-design-system/components-js` 4.7.0 | [S-L09-817] |
| License | Source code Apache-2.0; Porsche-specific fonts, icons and marque follow a separate, restricted assets agreement. The code license is not a blanket asset license | [S-L09-818] |
| Platforms | Web Components with framework wrappers for React, Angular and Vue, plus vanilla JS; TypeScript and SSR support described by the v4 site | [S-L09-819] |
| Token / styling outputs | Package exposes token modules, with CSS variables, SCSS, Tailwind, Emotion and Vanilla Extract documentation. Inspect token exports rather than overriding component internals | [S-L09-819] [S-L09-820] |
| Color model | Palette and role modules separate light and dark values; combined roles use CSS `light-dark(...)`. Example `colorCanvasLight` is `#fff`; `colorCanvasDark` refers to `palette.dark.grey['50']` | [S-L09-821] |
| Typeface | Porsche Next first; default fallbacks include Arial Narrow, Arial, Heiti SC, SimHei and sans-serif. Published package also provides dedicated CJK stacks | [S-L09-822] |
| Type scale | `typescaleSm = 1rem`; medium `clamp(1.13rem, 0.21vw + 1.08rem, 1.33rem)`; largest `typescale5Xl = clamp(2.28rem, 5.2vw + 1.24rem, 7.48rem)` | [S-L09-822] |
| Line height / weight | `leadingNormal = calc(6px + 2.125ex)`; normal 400, semibold 600, bold 700. The ex term makes font metrics relevant | [S-L09-822] [inferred] |
| Static spacing | 2xs / xs / sm / md / lg / xl / 2xl: 1 / 4 / 8 / 16 / 32 / 48 / 80px | [S-L09-823] |
| Fluid spacing | Medium `clamp(16px, 1.25vw + 12px, 36px)`; 2xl `clamp(80px, 7.5vw + 56px, 200px)`. Static and fluid are different exports | [S-L09-823] |
| Radius | xs / sm / md / lg / xl / 2xl / 3xl / 4xl: 2 / 4 / 6 / 8 / 12 / 16 / 24 / 32px; full `calc(infinity * 1px)` | [S-L09-824] |
| Elevation | Small `0px 3px 8px rgba(0,0,0,.16)`, medium `0px 4px 16px rgba(0,0,0,.16)`, large `0px 8px 40px rgba(0,0,0,.16)` | [S-L09-825] |
| Motion | sm / md / lg / xl durations .25 / .4 / .6 / 1.2s. Ease-in-out `cubic-bezier(.25,.1,.25,1)` | [S-L09-825] |
| Design source of truth | Site identifies coded components as authoritative and notes Figma can differ. Public and internal Figma library links are listed; kit content was not inspected | [S-L09-819] |

## Visual signature: why it looks like this

- Fluid type and fluid section spacing grow at different rates. Retaining each clamp's endpoints and slope matters more than assigning a generic responsive multiplier. [S-L09-822] [S-L09-823] [inferred]
- A line height partly based on `ex` depends on the selected typeface's metrics; copying it with a different font needs visual testing. [S-L09-822] [inferred]
- Role colors combine both modes at the token level, rather than requiring consumers to swap every individual literal themselves. [S-L09-821] [inferred]

## Version notes and disagreements

The v4 SCSS migration guide says the old large radius was 12px and the new `radius-lg` is 8px, with additional sizes above it. Thus the word "large" is insufficient evidence for a radius value without a version and token name. The published 4.7.0 radius exports agree with the v4 table. [S-L09-824] [S-L09-826]

The documentation landing page displayed an earlier-release banner even though the npm `latest` metadata resolved to 4.7.0 in this check. This entry uses that explicit version rather than inferring the existence or values of a newer major from the banner. [S-L09-817] [S-L09-819]

## Builder takeaways

- Export fluid and static spacing as distinct choices. [inferred]
- Carry the font assumptions alongside fluid typography and line-height formulas. [inferred]
- Preserve versioned migration evidence instead of averaging conflicting radius values. [inferred]
- Treat proprietary identity assets separately from reusable implementation techniques. [S-L09-818] [inferred]

## Gaps / unverified

No browser preview, component inventory or accessibility/reduced-motion audit was performed. CSS `light-dark` and `infinity` values were inspected as shipped exports, not compatibility-tested in target browsers. No font, icon or marque asset is included in this benchmark.
