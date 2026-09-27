# NYPL Reservoir

_Lane L09 teardown. Checked on 2026-09-25 against the pinned Reservoir source and package metadata. Pixel equivalents below assume a 16px root; rem values should remain scalable._

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Owner | New York Public Library; Reservoir supplies styled React components for NYPL products | [S-L09-787] |
| Current version / license | `@nypl/design-system-react-components` 4.5.1; Apache-2.0. Published metadata agrees with the source manifest version | [S-L09-788] [S-L09-795] |
| Framework | Built on Chakra UI v2; manifest dependency 2.8.2. React peer range `>=17 <19`. Consumers need `DSProvider` plus the distributed stylesheet | [S-L09-787] [S-L09-788] |
| Token tiers + naming | Named primitives feed UI, brand and section colors. Generic type/spacing tokens also feed component roles such as `button.medium.px` and `desktop.heading.heading1` | [S-L09-789] [S-L09-790] [S-L09-791] |
| Color | Examples of brand primitives: NYPL red `#C60917`, science blue `#0069BF`, tree green `#077719`. Source defines separate light/dark UI maps; primitive values alone do not identify a valid foreground/background pair | [S-L09-789] |
| Typeface | Body and heading both `system-ui, sans-serif` | [S-L09-790] |
| Type scale | Generic sizes .625 / .75 / .875 / 1 / 1.125 / 1.375 / 1.75 / 2.25rem. Desktop display 4.25rem, heading1 3.375rem; mobile display 3.25rem, heading1 2.625rem. Body1 stays 1rem in both | [S-L09-790] |
| Weight | Generic light / regular / medium / semibold / bold: 300 / 400 / 500 / 600 / 700. Declarations include `!important` to coexist with a v2 header/footer | [S-L09-790] |
| Spacing | Reservoir names xxxs / xxs / xs / s / m / l / xl / xxl / xxxl: .125 / .25 / .5 / 1 / 1.5 / 2 / 3 / 4 / 6rem (2–96px). The file also exports the larger Chakra numeric scale but recommends the Reservoir subset | [S-L09-791] |
| Component spacing | Medium button horizontal 1rem, vertical .5rem; large button horizontal 2rem, vertical 1rem. Page horizontal/vertical spacing roles both 2rem | [S-L09-791] |
| Radius | Button default 2px, checkbox 3px, pill 20px, round 100%. A fixed 20px pill and 100% circular radius are distinct tokens | [S-L09-792] |
| Elevation | The local shadow override only sets `outline: none`; this is not proof that all inherited or component shadows are disabled | [S-L09-793] [inferred] |
| Responsive structure | Named desktop/mobile typography maps coexist with breakpoints sm 30em, md 48em, lg 64em, xl 80em; 2xl 96em exists but is not recommended by Reservoir | [S-L09-790] [S-L09-794] |
| Figma / docs | Color source links NYPL Figma sections; README links current v4 Storybook, historical v3 and development docs. Figma content itself was not inspected | [S-L09-789] [S-L09-787] |
| Accessibility stance | README describes JSX accessibility linting, jest-axe in component tests and Storybook accessibility checks, plus per-component guidance. This is tooling evidence, not an independent conformance audit | [S-L09-787] |
| Governance | Public contribution instructions and a documented review/release workflow; README links maintainer guidance | [S-L09-787] |

## Visual signature: why it looks like this

- System fonts, mostly square 2px buttons and comparatively large reading/display sizes suit a content-oriented public-service interface. That interpretation is not a measured usability outcome. [S-L09-790] [S-L09-792] [inferred]
- Mobile headings shrink independently while body text stays 1rem. A single global density multiplier would lose this relationship. [S-L09-790] [inferred]
- The preferred nine-step spacing vocabulary provides a smaller choice set than the underlying Chakra scale. [S-L09-791] [inferred]

## Version notes and disagreements

In the typography source, both desktop and mobile `buttonLarge` are `1rem`, but their inline comments say `26px`. Use the executable `1rem` value (16px at the assumed root), not that comment. The historical v2/v4 weight conflict is explicitly documented in the same source; do not recommend `!important` as a general design-token convention. [S-L09-790]

## Builder takeaways

- Record the recommended subset separately from everything a dependency exports. [inferred]
- Model responsive heading roles explicitly instead of scaling all text equally. [inferred]
- Keep compatibility workarounds out of universal defaults; cite why a system needs them. [inferred]

## Gaps / unverified

No component count, motion timing/reduced-motion audit, browser-rendered preview or Figma variable inventory was performed. Theme source was inspected at a pinned commit, not assumed identical to every consumer's installed version. Inherited Chakra defaults need separate checking before claiming a complete shadow or type-line-height scale.
