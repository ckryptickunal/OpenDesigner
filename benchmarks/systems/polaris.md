# Shopify Polaris

_Lane L09 teardown. Verified against live sources on 2026-09-23. Every value carries an [S-L09-xxx] id from `traces/L09-trace.md` or the tag [inferred]._

> Status note (Sept 2026): Polaris is now a web component library served from Shopify's CDN. Polaris React is deprecated and its repo is archived. The token values below come from `@shopify/polaris-tokens` 9.4.2, the last published token package. Shopify does not publish a CSS token file for the web components [inferred: none found on shopify.dev].

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Owner | Shopify (Polaris team) | [S-L09-304] |
| Launch and major versions | React 1.0.0 on 2017-04-20. v2 2018-05, v3 2018-11, v4 2019-08, v5 2020-07, v6 2021-01, v7 2021-09, v8 2022-01, v9 2022-02, v10 2022-08, v11 2023-05, v12 2023-10-09 (new admin design language, Inter), v13 2024-04-09. Web components: early access 2025-05-21 (Editions Summer '25), stable 2025-10-01 with API version 2025-10 | [S-L09-300] [S-L09-307] [S-L09-316] [S-L09-315] |
| Current version (Sept 2026) | Polaris web components 1.1 (`polaris-1.1.js`; the stable channel `polaris-1.js` currently serves 1.1). React `@shopify/polaris` 13.9.5 (2025-03-26) is marked deprecated on npm. Tokens 9.4.2 (2025-03-17) | [S-L09-313] [S-L09-300] [S-L09-301] |
| Platforms | Shopify surfaces: App Home (iframe and UI extension), Admin UI extensions, Checkout UI extensions, Customer account UI extensions, POS UI extensions | [S-L09-311] |
| Open source + license | React and tokens: MIT text plus a Shopify clause (use only for apps that integrate with Shopify; stand-alone apps must be "visually distinct" from Shopify). Web components: shipped from `cdn.shopify.com`, no public source repo found | [S-L09-302] [S-L09-313] [inferred] |
| Code frameworks | Web Components (`s-` custom elements, built on remote-dom; UI extensions scaffold with Preact). TypeScript types in `@shopify/polaris-types`. React library deprecated | [S-L09-314] [S-L09-313] [S-L09-304] |
| Figma kit | Figma Community files "Polaris components", "Polaris styles", "Polaris icons" (updated for v12). Variables for color, space and size: yes | [S-L09-307] |
| Token tiers + naming | 2 tiers since v12: primitive and semantic. Grammar `--p-{category}-{concept}-{variant}-{state}`. Primitive: `--p-space-100`, `--p-border-radius-200`, `--p-font-size-325`. Semantic: `--p-color-bg-surface`, `--p-color-text-secondary`, `--p-space-table-cell-padding`, `--p-text-heading-lg-font-size`. Web components use keyword props instead (`padding="base"`, `large-100`) | [S-L09-307] [S-L09-303] [S-L09-317] |
| Color model | 13 ramps (gray, azure, blue, cyan, green, lime, magenta, orange, purple, red, rose, teal, yellow) x 16 steps (1-16), plus blackAlpha and whiteAlpha. sRGB `rgba()`. 225 `--p-color-*` semantic tokens in light theme. Brand fill is near-black `rgba(48,48,48,1)` (`--p-color-bg-fill-brand`); blue `rgba(0,91,211,1)` is used for emphasis, links and focus | [S-L09-305] [S-L09-303] |
| Typeface | Inter web font (since v12), then -apple-system, San Francisco, Segoe UI, Roboto. Mono: ui-monospace, SFMono-Regular, SF Mono, Consolas | [S-L09-303] [S-L09-307] |
| Type scale | 11 named styles: heading 3xl/2xl/xl/lg/md/sm/xs + body lg/md/sm/xs. Body-md = 13px / 20px, weight 450. Sizes 11, 12, 13, 14, 16, 18, 20, 22, 24, 30, 32, 36, 40px. Weights 450 / 550 / 650 / 700. Hand-tuned. Token number / 25 = px (`font-size-400` = 16px) | [S-L09-303] |
| Spacing | Base 4px (`--p-space-100`). Steps: 0, 025=1, 050=2, 100=4, 150=6, 200=8, 300=12, 400=16, 500=20, 600=24, 800=32, 1000=40, 1200=48, 1600=64, 2000=80, 2400=96, 2800=112, 3200=128px. Semantic: card padding 16, card gap 16, button-group gap 8, table cell 6 | [S-L09-303] |
| Radius | 0, 050=2, 100=4, 150=6, 200=8, 300=12, 400=16, 500=20, 750=30px, full. Button radius 8px (`--p-border-radius-200`) | [S-L09-303] [S-L09-377] |
| Elevation | Shadows plus bevels. `--p-shadow-0` none, 100 `0 1px 0 rgba(26,26,26,.07)`, 200 `0 3px 1px -1px .07`, 300 `0 4px 6px -2px .20`, 400 `0 8px 16px -4px .22`, 500 `0 12px 20px -8px .24`, 600 `0 20px 20px -8px .28`. Plus `shadow-bevel-100`, `shadow-inset-100/200` and 12 button shadow tokens (inset highlights) | [S-L09-303] |
| Motion | Durations 0 to 500ms in 50ms steps, plus 5000ms. `ease-in` cubic-bezier(0.42,0,1,1), `ease-out` (0.19,0.91,0.38,1), `ease-in-out` (0.42,0,0.58,1). Keyframes: bounce, fade-in, pulse, spin, appear-above, appear-below. No springs. No reduced-motion rule found in the archived motion guidance | [S-L09-303] [S-L09-345] |
| Theming + modes | Token CSS ships `.p-theme-light` (default), `.p-theme-light-mobile`, `.p-theme-light-high-contrast-experimental`, `.p-theme-dark-experimental`. Switched by class. No brand theming: apps are meant to look native to the admin. Web component theming: not public | [S-L09-303] [S-L09-304] |
| Component count | Web components (App Home): 50 on 2026-09-23, counted from shopify.dev index links (6 actions, 5 feedback, 17 forms, 10 layout, 4 media, 2 overlays, 6 typography). Plus 4 App Bridge components and 15 patterns. POS surface had 31 at GA. Archived React docs: 67 current + 22 deprecated + 7 internal pages | [S-L09-312] [S-L09-315] [S-L09-306] |
| Component doc structure | Web components: Properties (with Events, Slots), Examples (HTML), Best practices, Limitations. Archived React: examples + props, Best practices, Content guidelines, Related components, Accessibility | [S-L09-344] [S-L09-343] |
| Accessibility stance | React docs: WCAG 2.1 Level A and AA. Web components: semantic HTML, keyboard, ARIA and focus built in; components log warnings when required a11y props (label, error) are missing | [S-L09-342] [S-L09-314] |
| Governance / contribution | Central Shopify team. React repo archived; "no longer accepting contributions or feature requests". Web components versioned by Shopify on the CDN | [S-L09-304] [S-L09-313] |
| Notable innovation | A design system delivered as a versioned runtime: one script tag, a stable channel (`polaris-1.js`) that auto-updates, and frozen releases (`polaris-1.0.js`, `polaris-1.1.js`). One element vocabulary across 5 surfaces via remote-dom. Declarative `commandFor`/`command` API and container-query values inside attributes | [S-L09-313] [S-L09-314] |

## Visual signature: why it looks like this
- Near-black brand fill `rgba(48,48,48)` for primary buttons, blue only for emphasis and links -> monochrome "pro tool" chrome; merchants' own content and status colors carry the color. [S-L09-303]
- Pure neutral gray ramp (R=G=B, e.g. gray-6 `#f1f1f1` page, gray-8 `#e3e3e3` borders) -> no warm or cool cast; white cards float on a light gray page. [S-L09-305] [S-L09-303]
- Bevel and inset shadows on buttons (`--p-shadow-button`: bottom inset `#b5b5b5`, top highlight `#fff`) -> tactile, slightly skeuomorphic controls ("juicy interactions" in the v12 principles). [S-L09-303] [S-L09-307]
- 13px body at weight 450 in Inter, 20px line height -> dense, calm admin text with slightly heavier-than-regular strokes. [S-L09-303]
- 8px control radius and 12px card-scale radius (300) -> soft but not pill-shaped surfaces. [S-L09-377] [S-L09-303]
- Short motion (50ms steps, max 500ms) with a strong ease-out (0.19,0.91,0.38,1) -> snappy, low-drama transitions. [S-L09-303]

## Recent changes 2024-2026
- 2024-04-09: Polaris React v13 and tokens v9. [S-L09-300] [S-L09-301]
- 2025-03-26: last React release, 13.9.5. Tokens 9.4.2 on 2025-03-17. [S-L09-300] [S-L09-301]
- 2025-05-21: unified Polaris web components in early access (Admin, Checkout, Customer Accounts). [S-L09-316]
- 2025-10-01: web components stable with API 2025-10. +14 App Home components, +36 for Checkout and Customer Accounts, new POS surface with 31 components. [S-L09-315]
- 2026-08-04/05: polaris.shopify.com converted to a static archive on GitHub Pages; npm deprecation workflow added. The repo is now `Shopify/polaris-react-archive` (archived). polaris.shopify.com 301-redirects to shopify.dev/docs/api/polaris. [S-L09-304] [S-L09-318]
- By Sept 2026: versioned script tags `polaris-1.0.js`, `polaris-1.1.js`, channel `polaris-1.js`. [S-L09-313]

## Builder takeaways
- Offer a "pro admin" preset: neutral R=G=B grays, near-black primary, blue reserved for links/focus, 13px body, 8px radius, bevel shadows on buttons.
- Copy the naming rule "token number / 25 = px" (100 = 4px) across space, size, radius and font size. It makes values guessable.
- Ask the user how the system is delivered: npm package vs CDN runtime with a stable channel and frozen versions. Polaris shows the CDN model can replace a React library.
- Keep a keyword layer (`small-100`, `base`, `large-100`) on top of raw tokens for framework-free components.

## Gaps / unverified
- The exact release date of Polaris web components 1.1 is not shown on the versioning page.
- No public token file for the web components, so current (post-React) color and radius values may differ from tokens 9.4.2.
- Dark mode exists only as `dark-experimental` in the token CSS; web component dark mode is not documented.
- No current Figma kit for the web components was confirmed; the Figma links are from the v12 (2023) release notes.
- The Medium "Uplifting Shopify Polaris" article returned HTTP 403, so v12 details come from Shopify's own release notes only.
