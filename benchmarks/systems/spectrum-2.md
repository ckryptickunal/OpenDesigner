# Adobe Spectrum 2

_Lane L09 teardown. Verified against live sources on 2026-09-23. Every value carries an [S-L09-xxx] id from `traces/L09-trace.md` or the tag [inferred]._

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Owner | Adobe (Adobe Design; Spectrum Web Components built by a core team in Adobe Design Engineering) | [S-L09-228] [S-L09-232] |
| Launch and major versions | Spectrum 1: `@adobe/spectrum-css` on npm 2018-11-20, React Spectrum 2020-07-07. Spectrum 2 announced 2023-12-12 (web apps first, early 2024). `@react-spectrum/s2` 0.3.0 2024-08-19, 1.0.0 2025-12-16. Token data: S1 frozen at `@adobe/spectrum-tokens` v12.x (`s1-legacy` branch); S2 from 13.0.0 (2025-03-13) | [S-L09-220] [S-L09-229] [S-L09-233] |
| Current version (Sept 2026) | `@react-spectrum/s2` 1.7.1 (2026-09-04); `@adobe/spectrum-tokens` 15.4.1 (2026-09-14); Spectrum Web Components 1.12.2 (2026-07-06); gen2 `@adobe/spectrum-wc` 2.0.0-beta.3 (2026-09-01) | [S-L09-220] [S-L09-232] |
| Platforms | Web first. Tokens carry `desktop` and `mobile` platform sets. Native desktop and mobile versions of S2 are "being worked on" per the S2 FAQ | [S-L09-221] [S-L09-223] |
| Open source + license | Code and tokens yes, Apache-2.0 (tokens, React Spectrum, SWC). Adobe Clean fonts are Adobe-owned, not open [inferred] | [S-L09-220] |
| Code frameworks | React (`@react-spectrum/s2`, with a build-time atomic `style` macro), Web Components (SWC 1st-gen and gen2), CSS (`@spectrum-css/tokens` 16.0.2) | [S-L09-226] [S-L09-227] [S-L09-232] [S-L09-220] |
| Figma kit | An "S2 Web" Figma library is referenced in Adobe's S2 docs (Adobe-internal). No official public S2 Figma Community kit found; variables not confirmed | [S-L09-223] [S-L09-234] |
| Token tiers + naming | 3 tiers, kebab-case, numeric 100-scale or t-shirt sizes. Global: `blue-900`, `gray-25`, `spacing-300`. Alias/semantic: `accent-color-900` -> `{blue-900}`, `background-base-color`, `neutral-content-color-default`. Component: per-component files (`slider.json`, `tabs.json`; 91 files in `src/`). Sets per token: `light`/`dark`/`wireframe` and `desktop`/`mobile`. 2,495 tokens total | [S-L09-221] [S-L09-222] |
| Color model | 20 hue families x 16 steps (100-1600) + gray 13 steps (25-1000) + transparent black/white 13 steps. Values in `rgb()` (sRGB). Palette generated with Adobe Leonardo from key and brand colors, then lightness stops. 94 semantic palette tokens (accent, informative, negative, positive, notice, neutral 100-1600) and 191 color aliases. Accent = blue, shifted toward indigo (blue-900 light rgb(59,99,251)); lightest step contrast lowered to 1.06:1 | [S-L09-221] [S-L09-223] |
| Typeface | Adobe Clean Spectrum VF (default UI, variable), Adobe Clean Spectrum Serif VF, Adobe Clean Han (CJK), Source Code Pro (code). Custom | [S-L09-221] [S-L09-223] |
| Type scale | 18 sizes `font-size-25..1500`: desktop 10, 11, 12, 14, 16, 18, 20, 22, 25, 28, 32, 36, 40, 45, 51, 58, 65, 73px; mobile 12 ... 88px (about x1.2). Ratio about 1.125 [inferred from values]. `body-size-m` 16px / line-height 1.5; component text M 14px / 18px; headings extra-bold (800) at line-height 1.3; detail medium with 0.06em tracking; title bold. Style families heading / title / body / detail / code, sizes XXS-XXXXL | [S-L09-221] [S-L09-226] |
| Spacing | No single base unit. `spacing-25..1000` = 1, 2, 4, 6, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96px. Component heights `component-height-50..500`: desktop 20, 24, 32, 40, 48, 56, 64px; mobile 26, 30, 40, 50, 60, 70, 80px | [S-L09-221] |
| Radius | `corner-radius-0..800` = 0, 3, 4, 5, 6, 7, 8, 9, 10, 16px; `corner-radius-1000` = 0.5 (half the height, "full"). Size-dependent medium radius: XS 6, S 7, M 8, L 9, XL 10px. Style macro: sm 4, default 8, lg 10, xl 16, full, pill. Buttons are pill (height/2); action buttons use the size-dependent default; popovers 10px; cards 8px | [S-L09-221] [S-L09-226] |
| Elevation | Background layers + soft shadows. Base `gray-25` (white light / rgb(17,17,17) dark), layer-1 `gray-50` (#f8f8f8 light). Shadows: emphasized 0 1px 6px (hover 0 2px 8px); elevated = 3 layers (0 4px 12px, 0 2px 6px, 0 0 2px); dragged = 3 layers (0 12px 16px, 0 6px 8px, 0 0 6px). Black at 0.08-0.2 alpha light, 0.24-0.6 dark | [S-L09-221] |
| Motion | No motion tokens in `@adobe/spectrum-tokens` 15.4.1. S2 motion guidance "still being developed" (page dated 2026-02-02): directional, interaction, wayfinding. React S2 defaults: transition 150ms; easing default/in-out cubic-bezier(0.45,0,0.4,1), in (0.5,0,1,1), out (0,0,0.4,1). Large-area motion must respect reduced-motion settings | [S-L09-221] [S-L09-223] [S-L09-226] |
| Theming + modes | Light / dark (plus a `wireframe` color set) via Provider `colorScheme`; Provider background `base` / `layer-1` / `layer-2`; desktop vs mobile (touch) scale. No public brand re-theming [inferred]. Static black/white button variants for use over images | [S-L09-221] [S-L09-226] [S-L09-256] |
| Component count | 68 components documented in React Spectrum S2 docs (69 capitalized pages minus Provider), counted from repo 2026-09-23. S2 design docs cover 69 component pages. SWC gen2 has 27 component folders | [S-L09-227] [S-L09-223] [S-L09-232] |
| Component doc structure | Design docs: Overview, Resources, Anatomy, Component options, States, Behaviors, Usage guidelines (plus a design-token link). React docs: live examples + API | [S-L09-256] [S-L09-223] |
| Accessibility stance | S2 goals: "more inclusive and accessible", dynamic contrast, accessible colors, attention hierarchy. Focus indicator 2px thick with 2px gap. No WCAG level stated in the sources read | [S-L09-229] [S-L09-228] [S-L09-221] |
| Governance / contribution | Central Spectrum team; SWC welcomes contributions from inside and outside Adobe; tokens released with Changesets; a normative Design Data Specification (1.0.0-draft) governs token files | [S-L09-232] [S-L09-233] |
| Notable innovation | Platform scale sets (desktop vs mobile) inside the tokens; contrast-based palette generation (Leonardo); size-dependent corner radius; build-time atomic style macro; Design Data Spec + MCP servers + a Claude Code skill for design data | [S-L09-221] [S-L09-223] [S-L09-226] [S-L09-233] |

## Visual signature: why it looks like this
- Pill buttons (radius = height/2) + 6-10px size-scaled radius on fields and action buttons -> rounder, friendlier than Spectrum 1's sharp look. [S-L09-226] [S-L09-221] [S-L09-228]
- Highlight color removed from common controls and reserved for high-attention actions; blue pushed toward indigo -> calmer screens where the one blue CTA stands out. [S-L09-228] [S-L09-223]
- Solid white base (`gray-25`; the docs say S2 "now uses solid white" for light UI) with #f8f8f8 layer-1 -> brighter, airier canvas. [S-L09-223] [S-L09-221]
- Extra-bold (800) headings over 14px regular component text in Adobe Clean Spectrum VF -> strong hierarchy with compact controls. [S-L09-221]
- Three-layer shadows at 0.08-0.16 alpha -> soft, diffuse depth instead of hard drop shadows. [S-L09-221]
- Icons balance S1's sharp, rational drawing with Adobe Express's thicker, bubblier style, with strokes tuned to Adobe Clean -> softer, more approachable glyphs. [S-L09-228]

## Recent changes 2024-2026
- 2023-12-12: Spectrum 2 announced for 100+ apps; web and iOS first, desktop apps later. [S-L09-229] [S-L09-230]
- 2024-08-19: `@react-spectrum/s2` 0.3.0 published (package created 2024-08-09). [S-L09-220]
- 2024-11-21: `s2-foundations` token prerelease tag published. [S-L09-220]
- 2025-03-13: `@adobe/spectrum-tokens` 13.0.0; S2 data now on `main`, S1 moved to `s1-legacy`. [S-L09-220] [S-L09-233]
- 2025-03-19: `s2-composite-drop-shadow` prerelease tag (the 3-layer composite shadows). [S-L09-220] [S-L09-221]
- 2025-05-22: `adobe-clean-vf` token prerelease tag; Adobe Clean Spectrum VF is now the default family. [S-L09-220] [S-L09-221]
- 2025-06-11: `@spectrum-css/tokens` 16.0.2, the CSS token build. [S-L09-220]
- 2025-09-09: `@react-spectrum/mcp` created (1.2.1 by 2026-09-01). The S2 docs now carry an AI page (Agent Skills + MCP); that page's date is not confirmed. [S-L09-220] [S-L09-227]
- 2025-11-20: `@adobe/spectrum-tokens` 14.0.0. [S-L09-220]
- 2025-12-16: `@react-spectrum/s2` 1.0.0 (stable). [S-L09-220]
- 2026-01-21: gen2 `@adobe/spectrum-wc` created; 2.0.0-beta.3 on 2026-09-01. [S-L09-232]
- 2026-02-02: snapshot date of the S2 design docs in Adobe's public repo; motion guidance still marked in development. [S-L09-223]
- 2026-02-11: `layout` token prerelease tag. [S-L09-220]
- 2026-08-15: tokens 15.0.0; 15.4.1 on 2026-09-14. [S-L09-220]

## Builder takeaways
- Offer a platform-scale toggle (desktop vs touch) that multiplies sizes and type by about 1.2-1.25 from one token set.
- Offer size-dependent radius as an advanced option: radius grows with component size so small and large controls look equally round.
- Offer contrast-target color generation (Leonardo-style): ask the user for target contrast ratios, not hex steps.
- Consider a "wireframe" color set for low-fidelity prototyping from the same components.

## Gaps / unverified
- No public S2 Figma kit found; the S2 docs reference an internal "S2 Web" library. [S-L09-223]
- The S2 design docs read here are Adobe's own scraped copy of an internal site (`s2.spectrum.corp.adobe.com`), dated 2026-02-02. The public hub (`s2.spectrum.adobe.com`) shows no specs. [S-L09-223] [S-L09-224]
- The rollout of S2 into Photoshop, Illustrator and other desktop apps is not dated in any source read. [S-L09-230]
- No WCAG level found; no motion tokens exist yet.
- The brief asked about CIECAM02. Sources confirm Leonardo contrast-based generation but do not name the color space.
- react-spectrum.adobe.com renders in JS, so the component count comes from the docs source in the repo, not the live site. [S-L09-225] [S-L09-227]
- Which web-component generation (1st-gen SWC 1.12.x or gen2 2.0 beta) is the S2 default for new work was not confirmed. [S-L09-232]
- No high-contrast color set exists in the tokens; forced-colors support was not checked.
- Adobe Clean Spectrum licensing for non-Adobe use was not found.
