# U.S. Web Design System (USWDS)

_Lane L09 teardown. Verified against live sources on 2026-09-23. Every value carries an [S-L09-xxx] id from `traces/L09-trace.md` or the tag [inferred]._

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Owner | U.S. General Services Administration (GSA), USWDS core team (Technology Transformation Services) | [S-L09-543]; TTS unit [inferred] |
| Launch and major versions | npm `uswds` 0.9.0 2016-03-14; 1.0.0 2017-02-23; renamed from "U.S. Web Design Standards" 2018-01-17; 2.0 launched 2019-04-08 (npm 2019-04-04); 3.0 as `@uswds/uswds` 2022-04-28 | [S-L09-552] [S-L09-554] |
| Current version (Sept 2026) | @uswds/uswds 3.14.0, 2026-08-18 (previous 3.13.0 was 2025-05-23, a 15-month gap) | [S-L09-535] |
| Platforms | Web only | [S-L09-543] |
| Open source + license | Yes. GSA work is public domain in the US and CC0 1.0 worldwide. Bundled fonts under SIL OFL 1.1, Material icons and Roboto Mono under Apache-2.0 | [S-L09-536] |
| Code frameworks | HTML + Sass + vanilla JS (USWDS Core). USWDS Elements web components (Lit) in pre-release: `@uswds/elements` 1.0.0-alpha.6 (2025-12-10); Banner web component shipped in 3.13.0 | [S-L09-542] [S-L09-549] |
| Figma kit | Official USWDS design kit for Figma since Nov 2024 (also Sketch; Adobe XD dropped). Download from GitHub or install from Figma Community. Variables: unknown | [S-L09-551] |
| Token tiers + naming | System tokens `family-grade[v]` (`blue-60v`, `gray-cool-50`, `red-warm-50v`) -> theme tokens by role (`primary`, `primary-vivid`, `base-lightest`) and state tokens (`error`, `warning`, `success`, `info`). Set as Sass `$theme-*` settings, e.g. `$theme-color-primary: "blue-60v"` | [S-L09-547] [S-L09-538] |
| Color model | sRGB hex. Grades 5, 10, 20...90 (gray adds 1-4 and 100), plus "vivid" variants; grade 0 = white, 100 = black, regularized across 24 families (25 files incl. gray variants). 75 theme tokens in 11 role families. Contrast by "magic number": grade difference 40+ = AA large, 50+ = AA, 70+ = AAA | [S-L09-537] [S-L09-538] [S-L09-547] [S-L09-541] |
| Typeface | Default code: Source Sans Pro (sans, UI and body), Merriweather (serif, headings), Roboto Mono (code). Public Sans also bundled and used on the docs site. All open-source | [S-L09-539] [S-L09-536] |
| Type scale | Theme scale 9 steps: 3xs 13, 2xs 14, xs 15, sm 16, md 17, lg 22, xl 32, 2xl 40, 3xl 48px. System scale micro 10px + 1-20 (12...140px). Body = sm 16px, line height token 5 = 1.62. Line heights 1, 1.2, 1.35, 1.5, 1.62, 1.75. Sizes normalized per font by cap height (Source Sans Pro 340, Public Sans 362, Merriweather 371) | [S-L09-539] |
| Spacing | 1 unit = 8px. Tokens 1px, 2px, 05 = 4, 1 = 8, 105 = 12, 2 = 16, 205 = 20, 3 = 24, 4 = 32, 5 = 40, 6 = 48, 7 = 56, 8 = 64, 9 = 72, 10 = 80, 15 = 120px; layout sizes card 160 to widescreen 1400px | [S-L09-540] |
| Radius | 0, sm 2px, md 4px (0.5 unit), lg 8px (1 unit), pill 99rem. Default button radius md = 4px | [S-L09-540] |
| Elevation | Shadows, used sparingly. 5 levels, all rgba(0,0,0,0.1): 1 = 0 1px 4px, 2 = 0 4px 8px, 3 = 0 8px 16px, 4 = 0 12px 24px, 5 = 0 16px 32px | [S-L09-541] |
| Motion | One project easing: 0.15s ease-in-out. Since 3.13.0 animated transitions respect prefers-reduced-motion. No spring tokens | [S-L09-541] [S-L09-549] |
| Theming + modes | Brand theming by Sass settings at compile time (swap theme tokens to other system tokens). Light only; no dark mode. Windows high-contrast color file included. No density mode | [S-L09-538] [S-L09-537]; runtime theming absence [inferred] |
| Component count | 47 components ("47 components found" on the components overview, 2026-09-23) | [S-L09-543] |
| Component doc structure | Component preview (variants), Component code, Guidance (When to use, When to consider something else, Usability guidance, Accessibility guidance, Using the component), Accessibility test status, Package, Latest updates | [S-L09-544] |
| Accessibility stance | Section 508 baseline (WCAG 2.0 AA); USWDS targets WCAG 2.1 AA and "strives" for 2.2. ACR (VPAT 2.5) covering 44 components of 3.11.0, tested Mar 2025, published May 2025. 48px touch target, 4px blue-40v focus outline | [S-L09-546] [S-L09-541] [S-L09-540] |
| Governance / contribution | Central GSA core team with public GitHub discussions. Component lifecycle: discussion -> proposal in progress -> 45-day open comment -> build and release. Adoption "maturity model": Principles -> Guidance -> Code | [S-L09-545] [S-L09-548] |
| Notable innovation | Grade-based color system with "magic number" contrast math; cap-height-normalized type sizes; public-domain licence; government-wide banner and identifier components required by federal policy | [S-L09-547] [S-L09-539] [S-L09-536] [S-L09-543] |

## Visual signature: why it looks like this
- Merriweather serif headings over Source Sans Pro 16px/1.62 body -> editorial, "official document" tone with airy, readable paragraphs [S-L09-539].
- Primary blue-60v #005ea2 + secondary red-50 #d83933 on white -> patriotic palette that reads as federal at a glance [S-L09-538] [S-L09-537].
- Base family gray-cool (#dfe1e2 lighter, #71767a base, #1b1b1b ink) -> slightly cool, neutral chrome [S-L09-538] [S-L09-537].
- 4px button radius and 2px strokes on inputs and outline buttons -> softer than GOV.UK, still boxy [S-L09-540].
- 8px unit and 48px touch targets -> roomy layouts that survive low-vision zoom [S-L09-540] [S-L09-541].
- Flat by default; the 10% black shadows are for cards and overlays only -> depth is rare, hierarchy comes from type and color [S-L09-541] [inferred].

## Recent changes 2024-2026
- 2024-03-11 to 2024-12-18: 3.8.0 through 3.11.0 released (about one minor per quarter) [S-L09-535].
- Nov 2024: official Figma design kit launched [S-L09-551].
- 2025-03-07: 3.12.0 localized date pickers, Dart Sass 2.0 color-function fixes [S-L09-535] [S-L09-549].
- May 2025: accessibility conformance report for 44 components (3.11.0) published [S-L09-546].
- 2025-05-23: 3.13.0 first web component (Banner, Lit) and reduced-motion support [S-L09-535] [S-L09-549].
- 2025-01 to 2025-12: USWDS Elements alpha.2 to alpha.6; README says work now takes a "slower-than-previous iterative approach" [S-L09-542].
- 2026-08-18: 3.14.0 after a 15-month gap: left-aligned accordion icon option, breadcrumbs wrap by default, range slider hint text, modal screen-reader fixes, footer XSS fix [S-L09-535] [S-L09-549].

## Builder takeaways
- Copy the grade system: equal lightness per grade across hues lets users pick accessible pairs with one rule ("difference of 50 = AA"). Offer it as a contrast checker in the builder.
- Offer the 3-tier color split (system palette -> theme roles -> state roles) with a simple "pick a family, pick a grade" UI.
- Offer "normalize sizes by cap height" when users swap typefaces.
- Ask whether output must be public domain or needs to meet Section 508; USWDS proves a CC0 system can be widely adopted.

## Gaps / unverified
- Figma kit variables support not checked.
- 15-month gap between 3.13.0 and 3.14.0 is visible in npm; I found no official statement on the cause, so none is given.
- The GitHub releases page fetch mis-stated release years (2024); npm dates were used instead.
- Docs say 24 color families; the token folder has 25 family files (gray, gray-cool, gray-warm counted separately). Not reconciled.
- Owner unit "Technology Transformation Services" not re-verified in 2026.
- First public date: the npm package starts 2016-03-08; an earlier 2015 public alpha is from memory only, so it is not stated as fact.
- The designers page still says designs meet "WCAG 2.0 AA", while the accessibility page says the target is WCAG 2.1 AA. Both are live; the accessibility page is newer (ACR May 2025) [S-L09-551] [S-L09-546].
- Default code sans is Source Sans Pro, but Public Sans is bundled and referenced on the docs site [S-L09-536] [S-L09-543]; which one USWDS "recommends" today was not checked.
