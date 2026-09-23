# L09: Benchmark of famous design systems

_Lane L09. Checked against live sources on 2026-09-23. 25 systems. Every value in this file comes from the per-system teardowns in `benchmarks/systems/`, whose Snapshot rows carry the source ids. Evidence here is written as `[S-L09-300, 303]`, which is shorthand for S-L09-300 and S-L09-303 in `traces/L09-trace.md`. `[inferred]` marks my own inference._

## Lane overview

**What this is.** A side-by-side benchmark of 25 design systems (22 requested plus Chakra UI, Mantine and Linear), with real values for tokens, color, type, spacing, radius, elevation, motion, theming, components, docs, accessibility and governance. For each system it also explains which levers produce its look. The goal is to give the design-system builder its **defaults** (what nearly everyone does), its **key questions** (where systems split), and **presets** (named system recipes a user can start from).

**Method.** Six parallel workers wrote one teardown each from Tier A sources: official docs, official repos and token files, npm release data, official blogs and changelogs. Where docs sites render only in JavaScript, values came from the systems' own token source files. A fresh-context verifier then re-checked 32 high-risk claims against live sources: 28 held, 3 were corrected, 1 needed a tie-break (section V). 564 sources are logged in the trace (491 opened by the teardown workers, 67 by the verifier, 6 by the lead); 491 were used and 73 rejected (section "Sources").

**Big changes found since most training data (2025-2026).** These change what a builder should copy:
- Polaris React is deprecated and archived; Polaris is now web components served from Shopify's CDN (stable 2025-10-01) [S-L09-304, 313, 315].
- Material is "Compose-first" since Google I/O 2026 (2026-05-19); Material Web and MDC-Android are in maintenance mode [S-L09-121, 127, 128, 129].
- Apple shipped version 27 of all six OSes on 2026-09-14 with a Liquid Glass transparency slider [S-L09-152, 164].
- GOV.UK Frontend 6.0.0 (2026-02-09) made the refreshed brand the only brand and set body text to 19px at every breakpoint [S-L09-502, 534].
- shadcn/ui switched its default primitive layer from Radix to Base UI (2026-07-02) and added React Aria (2026-07-17) [S-L09-584, 585].
- Tailwind Labs announced it is joining Shopify (2026-09-09); Tailwind stays MIT [S-L09-606].
- Twilio retired the Paste docs site (2026-07-31); no npm release since 2025-08-25 [S-L09-349, 351].
- Carbon v12 is being built behind a flag and moves off 0px corners (inputs and tags to 4px) [S-L09-203, 258].
- Mantine 9 (2026-03-31) doubled its default radius from 4px to 8px [S-L09-646].
- 12 of the 25 systems now ship an MCP server, agent skills, or an agent-readable doc format (llms.txt, DESIGN.md, Markdown twins of every page). Ten of these are dated between March 2025 and May 2026; Uber's and Vercel's are undated but live (list in A1, item 10).

## Systems covered

| # | System | Owner | Status, Sept 2026 | Teardown |
|---|---|---|---|---|
| 1 | Material 3 (incl. M3 Expressive) | Google | Active; Compose-first; web in maintenance | `systems/material-3.md` |
| 2 | Apple HIG (incl. Liquid Glass) | Apple | Active; OS 27 shipped 2026-09-14 | `systems/apple-hig.md` |
| 3 | Fluent 2 | Microsoft | Active | `systems/fluent-2.md` |
| 4 | Carbon | IBM | Active on v11; v12 behind a flag | `systems/carbon.md` |
| 5 | Spectrum 2 | Adobe | Active; React S2 1.0 on 2025-12-16 | `systems/spectrum-2.md` |
| 6 | Lightning / SLDS 2 (Cosmos) | Salesforce | Active; SLDS 2 CSS package on npm since 2026-03, now 2.264.2 | `systems/slds-2.md` |
| 7 | Atlassian Design System | Atlassian | Active; refreshed themes default since 2025-11 | `systems/atlassian.md` |
| 8 | Polaris | Shopify | Web components only; React archived | `systems/polaris.md` |
| 9 | Primer | GitHub | Active; Rails components in maintenance | `systems/primer.md` |
| 10 | Paste | Twilio | Frozen [inferred]; docs site retired | `systems/paste.md` |
| 11 | Gestalt | Pinterest | Public releases stopped Dec 2025; new docs behind login | `systems/gestalt.md` |
| 12 | Base / Base Web | Uber | Base Web maintained at low cadence | `systems/uber-base.md` |
| 13 | Ant Design | Ant Group | Active; v6 | `systems/ant-design.md` |
| 14 | Blade | Razorpay | Active; v12 | `systems/blade.md` |
| 15 | GOV.UK Design System | UK Government Digital Service | Active; Frontend v6 | `systems/govuk.md` |
| 16 | U.S. Web Design System | U.S. GSA | Active at slow cadence | `systems/uswds.md` |
| 17 | Radix (Primitives, Themes, Colors) | WorkOS | Active in bursts; Colors unchanged since 2023 | `systems/radix.md` |
| 18 | shadcn/ui | shadcn (maintainer) | Very active | `systems/shadcn-ui.md` |
| 19 | Tailwind CSS (as a token system) | Tailwind Labs, joining Shopify | Active; v4.3 | `systems/tailwind.md` |
| 20 | Chakra UI | Open-source maintainers | Active; v4 planned | `systems/chakra-ui.md` |
| 21 | Mantine | Open-source maintainers | Active; v9 | `systems/mantine.md` |
| 22 | Geist | Vercel | Docs public; components private | `systems/geist.md` |
| 23 | Encore | Spotify | Internal; public info only | `systems/spotify-encore.md` |
| 24 | Design Language System (DLS) | Airbnb | Internal; public info only | `systems/airbnb-dls.md` |
| 25 | Linear (no published system) | Linear | Internal; blog posts and site CSS only | `systems/linear.md` |

**How to read the tables.** Rows follow the numbering above. "n/p" means not public. Values are as of 2026-09-23. For systems with two themes, the newer theme is listed first (SLDS: Cosmos, then Lightning Blue; Gestalt: classic default, with the visual refresh "VR" noted).

## Matrix

### M1. Identity and distribution

| # | System | First public, major versions | Current (Sept 2026) | Platforms | Open source + license | Code | Figma kit | Evidence |
|---|---|---|---|---|---|---|---|---|
| 1 | Material 3 | M1 2014; M3 May 2021; M3 Expressive 2025-05-13; I/O 2026 update 2026-05-19 | Compose Material3 1.4.0 stable, 1.5.0-alpha29 (2026-09-23) [S-V1b-035]; @material/web 2.5.0; MDC-Android 1.14.0 (final line) | Android, Wear OS, web; watch and XR guidance | Yes, Apache-2.0 | Jetpack Compose (primary); Android Views and Web Components in maintenance | Official "Material 3 Design Kit"; variables not confirmed | [S-L09-112, 117, 118, 119, 121, 125, 128, 129, 130] |
| 2 | Apple HIG | Living document; Liquid Glass 2025-06-09 (v26 on all OSes); v27 at WWDC 2026-06-08 | OS 27 released 2026-09-14; HIG change log 2026-09-18 | iOS, iPadOS, macOS, watchOS, tvOS, visionOS | No (fonts and UI kits free) | SwiftUI, UIKit, AppKit | Official iOS/iPadOS 27 and macOS 27 Figma kits (2026-09-17) | [S-L09-147, 149, 151, 152, 153, 157, 164] |
| 3 | Fluent 2 | Fluent 2017; React v9 GA 2022-06-28; Fluent 2 site by 2023-05; Web Components 3.0 2026-06-29 | react-components 9.74.8; web-components 3.1.3 | Web, Windows, iOS, macOS, Android | Yes, MIT | React v9, Web Components v3, Blazor, UIKit/AppKit, Android, WinUI | Official Web/iOS/Android kits, variables yes | [S-L09-165, 166, 183, 197, 198] |
| 4 | Carbon | 2017; v10 2019-03-29; v11 2022-03-31; v12 behind flag | @carbon/react 1.116.0 (v11) | Web | Yes, Apache-2.0 | React, Web Components, Sass | Official v11 kit; color variables | [S-L09-200, 204, 207, 217, 218, 219] |
| 5 | Spectrum 2 | S1 2018; S2 announced 2023-12-12; React S2 1.0 2025-12-16 | @react-spectrum/s2 1.7.1; tokens 15.4.1 | Web first; desktop and mobile token sets | Code and tokens Apache-2.0; Adobe Clean not open [inferred] | React S2, Web Components, CSS | No public S2 kit found | [S-L09-220, 221, 223, 229, 232, 234] |
| 6 | SLDS 2 | SLDS 2015; SLDS 2 package first on npm 2026-03-19 (alpha), 1.0.0 2026-04-07, 2.0.0 2026-04-08, 2.264.0 (first stable of the Winter '27 line) 2026-07-21 | 2.264.2 (Winter '27) | Web (Salesforce platform) | Mixed: SLDS 1 BSD-3; SLDS 2 proprietary terms; LWC base components MIT | CSS + styling hooks, LWC, Aura | "Figma Kits" page exists; not read | [S-L09-236, 237, 242, 244, 245] |
| 7 | Atlassian | Atlaskit 2017; tokens 1.0 2023-02-07; refreshed themes default 2025-11-07 | @atlaskit/tokens 19.0.0 | Web | Source on npm, Apache-2.0; Atlassian-only contributions | React, primitives, Compiled CSS | Internal libraries + public community library | [S-L09-246, 249, 252, 254, 255] |
| 8 | Polaris | React 1.0 2017-04-20; v12 2023-10-09; web components stable 2025-10-01 | Web components 1.1 on CDN; React 13.9.5 deprecated | Shopify surfaces only (App Home, Admin, Checkout, Customer accounts, POS) | React/tokens MIT + Shopify-only clause; web components no public source | Web Components (`s-` elements) | Community files (v12), variables yes | [S-L09-300, 302, 304, 307, 313, 315, 316] |
| 9 | Primer | CSS 12.0 2019; React v34 2021 to v38 2025-10-27 | @primer/react 38.40.0; primitives 11.10.0 | Web | Yes, MIT | React (primary); Rails in maintenance; CSS keep-the-lights-on | "Primer Web" library, variables yes | [S-L09-320, 321, 322, 323, 335] |
| 10 | Paste | core 1.0 2019-11-11; v21 2025-03-19 | core 21.5.0 (2025-08-25); docs site retired 2026-07-31 | Web; tokens for iOS/Android | Yes, MIT | React | Community kit, variables yes | [S-L09-347, 349, 351, 352, 359, 360] |
| 11 | Gestalt | 1.0 2020-02-20; v177 2025-04-10; "Gestalt 2.0" docs 2025-11-21 | 177.0.12 (2025-12-09) | Web components; tokens for iOS/Android | Yes, Apache-2.0 | React | Internal only | [S-L09-361, 363, 369, 373] |
| 12 | Uber Base | Base Web 1.0 2018-08-20; v16 2026-01-06; Base 2.0 pages | baseui 18.2.0 (2026-07-02) | Base: iOS, Android, web. Base Web: web | Base Web MIT; native not open | React + Styletron | "Base Gallery" (duplicate-only) | [S-L09-427, 428, 436, 440, 443] |
| 13 | Ant Design | 1.0 2016-05-10; v5 2022-11-18; v6 2025-11-21 | antd 6.6.5 (2026-09-20) | Web (+ antd-mobile, Ant Design X) | Yes, MIT | React; CSS-in-JS + CSS variables | No official Figma kit | [S-L09-400, 402, 417, 418, 419, 421, 460] |
| 14 | Blade | 1.0 2020-02-05; v11 2024-01-24 (refresh); v12 2024-12-11 | 12.126.0 (2026-09-17) | Web + iOS/Android (React Native) | Yes, MIT | React + React Native (Svelte port in progress) | Official Community file | [S-L09-446, 452, 461, 463, 464] |
| 15 | GOV.UK | Frontend 1.0 2018-06-21; v5 2023-12-08; v6 2026-02-09 | 6.5.1 (2026-09-14) | Web | Yes, MIT code + OGL docs | HTML, Sass, JS, Nunjucks | None by GDS (MoJ community kit) | [S-L09-500, 520, 524, 532, 534] |
| 16 | USWDS | 0.9 2016; 2.0 2019; 3.0 2022-04-28 | 3.14.0 (2026-08-18) | Web | Yes: GSA code public domain / CC0; bundled fonts OFL-1.1 and icons Apache-2.0 | HTML, Sass, JS; Lit web components (alpha) | Official kit since Nov 2024 | [S-L09-535, 536, 542, 551, 552, 554] |
| 17 | Radix | Primitives Dec 2020; Colors 2023; Themes 1.0 2023-08-08; unified `radix-ui` 2025-01-22 | radix-ui 1.6.7; Themes 3.3.0 | Web | Yes, MIT | React | Unofficial kits only | [S-L09-556, 557, 566, 569, 575, 576] |
| 18 | shadcn/ui | Jan 2023; CLI 3.0 2025-08-27; 4.0 2026-03-06 | CLI 4.21.0; component code unversioned | Web | Yes, MIT | React + Tailwind v4 over Base UI (default), Radix or React Aria | Community kits only | [S-L09-572, 575, 582, 584, 588, 589] |
| 19 | Tailwind | 0.1 2017; v4.0 2025-01-21; v4.3 2026-05-08 | 4.3.3 (2026-07-16) | Web (CSS) | Yes, MIT | Framework-agnostic CSS | None found [inferred] | [S-L09-600, 605, 606, 608] |
| 20 | Chakra UI | 1.0 2020-11-13; v3 2024-10-22; v4 planned | 3.37.0 (2026-08-28) | Web | Yes, MIT | React (Ark UI + Emotion) | Official v3 kit, variables yes | [S-L09-601, 630, 638, 639, 641, 642] |
| 21 | Mantine | 1.0 2021-05-03; v7 2023-09 (native CSS); v8 2025-05-05; v9 2026-03-31 | 9.6.2 (2026-09-21) | Web | Yes, MIT | React; CSS modules + CSS variables | Community only | [S-L09-602, 646, 648, 649, 663] |
| 22 | Geist | Geist font 1.0 2023-10-27; docs public by 2024-03-08; Geist Pixel 2026-02-06 | Docs unversioned; font 1.7.2 | Web | Font OFL-1.1; components private | React / Next.js | None public | [S-L09-603, 619, 621, 622, 625, 627] |
| 23 | Encore | Started 2018; introduced 2019; update Dec 2022 | n/p | Web, iOS, Android, TV, car, wearables | No | React (Encore Web); mobile n/p | Internal, synced by the "Figgy" bot | [S-L09-469, 470, 472, 475] |
| 24 | Airbnb DLS | 2016; Cereal typeface 2018; new app 2025-05-13 | n/p | iOS, Android, web | No (Lottie and others are open source) | n/p | n/p | [S-L09-477, 478, 480, 482, 483] |
| 25 | Linear | Redesign 2024-03-28; "calmer interface" 2026-03-12; StyleX 2026-08-06 | Not versioned | Web + native apps | No | React + StyleX | n/p | [S-L09-652, 654, 655] |

### M2. Token architecture

| # | System | Tiers | Naming grammar | Real examples (primitive -> semantic -> component) | Evidence |
|---|---|---|---|---|---|
| 1 | Material 3 | 3: ref / sys / comp | dot: `md.<tier>.<group>.<name>` | `md.ref.typeface.brand` -> `md.sys.color.primary`, `md.sys.measurement.space100` -> filled-button `container-shape` | [S-L09-123, 134, 169] |
| 2 | Apple HIG | No public token files; 2 layers exposed as API names | camelCase API | `systemBlue` -> `label`, `systemBackground`; `.largeTitle`; glass `.regular` / `.clear` | [S-L09-141, 142, 159] |
| 3 | Fluent 2 | 2: global / alias | camelCase | `borderRadiusMedium`, `fontSizeBase300` -> `colorNeutralBackground1`, `colorBrandBackground`, `shadow16` | [S-L09-171, 173, 187, 192] |
| 4 | Carbon | 3: palette / theme / component | kebab, `$` Sass vars | `blue-60` -> `$background`, `$layer-01`, `$interactive`; `$spacing-05`; DTCG JSON is the source since 2026 | [S-L09-201, 210, 211, 212] |
| 5 | Spectrum 2 | 3: global / alias / component, plus sets (light, dark, wireframe; desktop, mobile) | kebab, 100-scale or t-shirt | `blue-900` -> `accent-color-900`, `background-base-color` -> `slider.json`; 2,495 tokens | [S-L09-221, 222] |
| 6 | SLDS 2 | 4 "styling hook" tiers: reference / global / shared / component | `--slds-{r,g,s,c}-...` | `--slds-r-color-brand-50` -> `--slds-g-color-accent-1` -> `--slds-s-button-radius-border` -> `--slds-c-button-...` | [S-L09-237, 242] |
| 7 | Atlassian | 2 public: palette / design token | dot path -> `--ds-*` | `color.palette.Blue700` -> `color.background.brand.bold`, `elevation.surface.raised`, `space.100`, `motion.modal.enter` | [S-L09-247, 248] |
| 8 | Polaris | 2: primitive / semantic (+ keyword props in web components) | `--p-{category}-{concept}-{variant}-{state}`; number / 25 = px | `--p-space-100` (4px) -> `--p-color-bg-surface`, `--p-space-table-cell-padding`; `padding="base"` | [S-L09-303, 307, 317] |
| 9 | Primer | 3: base / functional / component | camelCase `{property}-{variant}-{state}`; DTCG JSON5 | `--base-size-4` -> `--fgColor-default`, `--bgColor-muted` -> `--button-primary-bgColor-rest` | [S-L09-327, 331, 346, 378] |
| 10 | Paste | 2: palette / semantic (+ named-element overrides) | `{category}-{property}-{variant}-{weight}` | `palette-blue-60` -> `--color-background-primary`, `--color-text-weak`, `--space-40` | [S-L09-352, 354, 359] |
| 11 | Gestalt | VR: 3 (base / sema / comp); classic: 2 | `--{tier}-{category}-{name}` | `--base-color-red-300` -> `--sema-color-background-primary` -> `--comp-checkbox-*` | [S-L09-367, 368] |
| 12 | Uber Base | Color: 4 (primitive / foundation / semantic / component); others numeric steps | camelCase | `blue600` -> `primaryA`, `accent` -> `backgroundPrimary`, `contentSecondary`; `scale600`, `radius300` | [S-L09-430, 432, 433] |
| 13 | Ant Design | 4, generated: Seed / Map / Alias / Component | camelCase | `colorPrimary`, `borderRadius` -> `colorPrimaryBg`, `borderRadiusLG` -> `colorLink` -> `theme.components` | [S-L09-403, 408, 413] |
| 14 | Blade | 2 + component props that take token paths | dot path | `colors.chromatic.azure[500]` -> `surface.background.gray.subtle`, `interactive.background.primary.default` | [S-L09-450, 451, 457] |
| 15 | GOV.UK | 2: palette / functional (Sass functions + CSS vars) | function arguments | `govuk-colour("blue", "tint-25")` -> `govuk-functional-colour(brand)`; `govuk-spacing(0..9)` | [S-L09-502, 504, 505, 506] |
| 16 | USWDS | 3: system / theme / state | `family-grade[v]` | `blue-60v` -> `primary`, `base-lightest` -> `error`, `warning` | [S-L09-538, 547] |
| 17 | Radix | 2: scale / semantic alias | `--{hue}-{step}`, `--accent-*` | `--indigo-9`, `--gray-a5` -> `--accent-9`, `--color-panel`, `--focus-8` | [S-L09-559] |
| 18 | shadcn/ui | 2: raw variables / Tailwind mapping | role + `role-foreground` | `--primary: oklch(0.205 0 0)` -> `--color-primary` -> `bg-primary` | [S-L09-587] |
| 19 | Tailwind | 1 built in (primitives); semantic tier is up to the user | `--{namespace}-{key}` (20 namespaces) | `--color-blue-500`, `--radius-lg`, `--text-sm--line-height` | [S-L09-604, 609] |
| 20 | Chakra UI | 2 + a virtual palette | dot | `colors.blue.500` -> `bg.subtle`, `fg.muted`, `blue.solid` -> `colorPalette.solid` | [S-L09-631, 632, 635, 640] |
| 21 | Mantine | 3: palette / per-color variant / global semantic | `--mantine-{category}-{name}` | `--mantine-color-blue-6` -> `--mantine-color-blue-filled` -> `--mantine-color-body` | [S-L09-643, 644] |
| 22 | Geist | 2 + composite presets | `--ds-{hue}-{step}` | `--ds-blue-700-value` -> `--ds-blue-700`; `text-heading-72`, `material-modal` | [S-L09-616, 618, 620] |
| 23 | Encore | 3 observed | base plus `tighter-n` / `looser-n` | `--encore-spacing-looser-2` -> `--background-elevated-base` -> `--encore-button-min-block-size` | [S-L09-470, 472] |
| 24 | Airbnb DLS | 3 observed; value in the name | `--palette-*`, `--dls-*` | `--palette-rausch600` -> `--palette-bg-primary` -> `--dls-button_border-radius`; `--typography-titles-semibold_22_26` | [S-L09-482] |
| 25 | Linear | Generated: 3 inputs (base, accent, contrast) -> 100+ LCH variables | site: `--color-bg-level-0..3` | n/p for the app | [S-L09-652, 655, 656] |

**Pattern.** 24 of 25 systems put a semantic layer over raw values; only Tailwind ships a single tier, and shadcn/ui exists largely to add the missing semantic layer on top of it [S-L09-604, 587]. Two or three tiers is the norm (11 and 9 systems). Four tiers appear only where a system must re-theme at scale: SLDS (two themes, customer orgs), Ant (algorithms), Uber (brand foundation tier) [S-L09-237, 413, 433]. This matches the 2026 zeroheight survey, where primitive and semantic layers are near-universal (90%, 85%) and component tokens are optional (52%) [S-L09-005; also read in full by L00 as S-L00-056].

### M3. Color

| # | System | Ramp steps | Color space / how ramps are made | Semantic color roles (approx.) | Accent approach | Evidence |
|---|---|---|---|---|---|---|
| 1 | Material 3 | Tones 0-100 (13 key stops + extra neutral tones for surfaces) | HCT (CAM16 hue/chroma + L* tone); generated from one seed; 10 scheme variants | 48 (Compose baseline) to 53 (color utilities) | Seed color or wallpaper -> 5 palettes; primary = tone 40, containers = tone 90 | [S-L09-104, 108, 112, 116] |
| 2 | Apple HIG | 12 hues + 6 grays, each with 4 values (light, dark, increased-contrast light and dark) | sRGB or Display P3; hand-set | 14 on iOS (8 foreground + 6 background); 31+ on macOS | App accent/tint; systemBlue light (0,136,255) | [S-L09-142] |
| 3 | Fluent 2 | Brand 16 steps (10-160); neutral 50 steps; ~52 named colors with shades and tints | sRGB hex; full theme generated from one brand ramp | 184 alias color tokens (light theme) | Pass a 16-step brand ramp; web brand #0f6cbd | [S-L09-170, 178, 187, 188] |
| 4 | Carbon | 12 families x 10 (10-100) + a hover value per step | sRGB hex; hand-set | 234 theme color tokens | Fixed IBM Blue: blue-60 #0f62fe | [S-L09-211, 212] |
| 5 | Spectrum 2 | 20 hues x 16 (100-1600) + gray 13 steps | sRGB `rgb()`; contrast-based generation with Adobe Leonardo | 94 semantic palette + 191 color aliases | Blue shifted toward indigo (blue-900 rgb(59,99,251)) | [S-L09-221, 223] |
| 6 | SLDS 2 | Reference ramps 17 steps (5-95); global 13 hues x 12 + neutral 14 | sRGB hex | 326 global color hooks | Cosmos fixed brand-50 #066afe; Lightning Blue reads the org's brand color | [S-L09-237] |
| 7 | Atlassian | 9 hues x 12 (100-1000) + neutral 18, dark neutral 22 | Hex with alpha; hand-picked [inferred] | 466 color variables per theme | #1868DB light / #669DF1 dark | [S-L09-247, 248] |
| 8 | Polaris | 13 ramps x 16 (1-16) + black/white alpha | sRGB `rgba()` | 225 | Near-black brand fill rgba(48,48,48); blue for links and focus | [S-L09-303, 305] |
| 9 | Primer | 8 hues x 10 (0-9) + neutral 0-13 | HSL + hex | 83 functional roles | Blue #0969da accent; green #1f883d primary button | [S-L09-330, 331] |
| 10 | Paste | 7 hues, steps 05 and 10-100 (+ extras) | sRGB hex | 184 (72 bg + 62 text + 50 border) + 10 data-viz | #0263e0 primary; brand navy #001489 | [S-L09-352, 354] |
| 11 | Gestalt | Classic 8 hues x 12; VR warm gray 12 + 5 hues x 5 | sRGB hex | VR: 90 | Pinterest red #e60023 | [S-L09-367, 368] |
| 12 | Uber Base | 10 steps (50-900) x 10 hues + gray | sRGB hex; hand-picked | ~164 | Monochrome #000 / #fff foundation; accent #276EF1 | [S-L09-432, 433] |
| 13 | Ant Design | 10 steps (1-10), base color at step 6; 12 preset hues | HSV algorithm from a seed | ~79 map color tokens [inferred count] | Seed #1677ff; palettes regenerate | [S-L09-403, 412, 424] |
| 14 | Blade | 11 hues x 11 (50-1000) + 5 alpha steps | HSLA; `createTheme` generates a brand ramp and checks contrast | ~431 leaves per mode [inferred count] | Azure-500 ~#1364F1; any brand color (white-label) | [S-L09-450, 451, 459] |
| 15 | GOV.UK | 11 colours x tints 25/50/80/95 + shades 25/50 | sRGB hex | 21 functional | Fixed #1d70b8 | [S-L09-504, 505] |
| 16 | USWDS | Grades 5-90 (+ "vivid") x 24 families | sRGB hex; grade = lightness band, so contrast is arithmetic | 75 theme tokens | Sass setting; default primary blue-60v #005ea2 | [S-L09-537, 538, 547] |
| 17 | Radix | 12 steps x 33 scales, each light/dark/alpha, sRGB + P3 twins | Hand-tuned; steps 11/12 guarantee APCA Lc 60/90 on step 2 | The 12 steps ARE the roles (bg, hover, border, solid, text) + ~6 named aliases | Pick 1 of 26 accents + 1 of 7 grays | [S-L09-559, 563, 564, 565] |
| 18 | shadcn/ui | Borrows Tailwind ramps; 7 base neutrals | OKLCH | 31 per mode | Achromatic near-black primary oklch(0.205 0 0); user recolors | [S-L09-578, 587, 593] |
| 19 | Tailwind | 26 families x 11 (50-950) = 286 values | OKLCH | 0 (user adds them) | User picks | [S-L09-604, 607, 613] |
| 20 | Chakra UI | 10 palettes x 11 (50-950) | sRGB hex | 108 (28 global + 8 per palette) | Swap `colorPalette` per component | [S-L09-631, 632] |
| 21 | Mantine | 14 palettes x 10 (0-9) | sRGB hex (OKLCH input accepted) | 17 global + 8 per color | `primaryColor` + a separate brand step per mode (6 light, 8 dark) | [S-L09-643, 644, 651] |
| 22 | Geist | 10 scales x 10 (100-1000); each step has a job | HSL sRGB fallback + OKLCH on P3 screens | ~92; step = role | Fixed blue-700 | [S-L09-616, 618] |
| 23 | Encore | 16 "color sets" x the same 25 roles | sRGB hex; theming algorithm guarantees contrast | 25 per set | Spotify green #1ed760 | [S-L09-470, 472] |
| 24 | Airbnb DLS | Rausch 100-1000; grey 0-1100 | sRGB + `color-mix()` | 353 palette tokens incl. semantic | Rausch #FF385C | [S-L09-482] |
| 25 | Linear | Generated | LCH, from base + accent + contrast | 100+ generated variables | Site accent #7170ff | [S-L09-652, 656] |

**Patterns.** Ramps cluster at 10-12 steps (Carbon, Primer, Ant, Uber, Geist, Mantine at 10; Tailwind, Chakra, Blade at 11; Radix, Atlassian, Gestalt classic at 12). Long ramps (16-17 steps) belong to systems that serve many surfaces or themes (Fluent, Spectrum, Polaris, SLDS). Three generation strategies exist: hand-picked hex (most), algorithmic from a seed (Material HCT, Ant HSV, Blade, Fluent, Linear LCH), and contrast-targeted (Spectrum Leonardo, USWDS grades, Radix APCA steps) [S-L09-116, 412, 459, 170, 652, 223, 547, 563]. Perceptual spaces are spreading: OKLCH in Tailwind, shadcn and Geist's P3 layer; HCT in Material; LCH in Linear [S-L09-604, 587, 618, 116, 652].

### M4. Typography

| # | System | Typeface(s) | Named styles | Body size / line height | Scale approach | Evidence |
|---|---|---|---|---|---|---|
| 1 | Material 3 | Roboto in web tokens; Google Sans Flex (6 axes) positioned for expressive type | 15 baseline + 15 "emphasized" (Expressive) | Body Large 16/24; Body Medium 14/20 | Hand-tuned; Display Large 57/64 | [S-L09-100, 110, 132, 134] |
| 2 | Apple HIG | SF Pro, SF Compact, SF Mono, New York (system fonts) | 11 Dynamic Type styles | iOS Body 17/22 pt; macOS Body 13/16 | Hand-tuned per platform; 12 Dynamic Type sizes (iOS Body 14-53 pt) | [S-L09-140, 149] |
| 3 | Fluent 2 | Segoe UI / Segoe UI Variable; SF Pro on Apple; Roboto on Android | 17 web styles | Web 14/20; iOS 17/22; Android 16/24 | Hand-tuned, one ramp per platform | [S-L09-173, 177, 185] |
| 4 | Carbon | IBM Plex Sans / Mono / Serif (custom, open) | 58 exported style objects; productive and expressive sets | body-01 14/20, +0.16px tracking | Formula: 23 sizes 12-156px | [S-L09-213] |
| 5 | Spectrum 2 | Adobe Clean Spectrum VF (custom) | Heading / title / body / detail / code, sizes XXS-XXXXL; 18 size tokens | Body M 16 / 1.5; component text 14/18 | Ratio ~1.125 [inferred]; mobile ~x1.2 of desktop | [S-L09-221, 226] |
| 6 | SLDS 2 | System stack (Salesforce Sans dropped in 2021) | 11 steps (Cosmos) | 13 / 1.5 | Ratio hook 1.15, hand-tuned | [S-L09-237, 244] |
| 7 | Atlassian | Atlassian Sans (Inter derivative), Atlassian Mono (JetBrains Mono derivative) | 14 | 14/20 | Minor-third basis; heading weight 653 | [S-L09-247, 252] |
| 8 | Polaris | Inter + system fallback | 11 | 13/20 at weight 450 | Hand-tuned; token number / 25 = px | [S-L09-303, 307] |
| 9 | Primer | Mona Sans VF (primary since 2026-03-25) + system | 11 functional | 14 / 1.5 | Hand-tuned | [S-L09-326, 327] |
| 10 | Paste | Inter var (default theme); Twilio Sans (Twilio theme) | 11 sizes, no composite styles | Button 14/20 (body not confirmed) | Hand-tuned | [S-L09-352, 356] |
| 11 | Gestalt | Pin Sans (VR, custom); system stack (classic) | 14 (VR) | 16/22 | Hand-tuned; line-height sets per script | [S-L09-367, 368, 370] |
| 12 | Uber Base | Uber Move, Move Text, Move Mono (proprietary) | 18 + 18 mono twins | 16/24 | Hand-tuned on a 4px line-height grid | [S-L09-431] |
| 13 | Ant Design | System stack | 10 generated sizes; H1-H5 | 14/22 | Formula: 14 x e^(i/5), rounded to even | [S-L09-403, 407] |
| 14 | Blade | Inter (text) + TASA Orbiter (headings) | 14 size tokens, desktop and mobile sets | 14/20 | Hand-tuned | [S-L09-449, 454] |
| 15 | GOV.UK | GDS Transport (restricted to gov.uk) + Arial | 7 sizes | 19/25 on every screen (v6) | Hand-tuned, responsive at 641px | [S-L09-502, 507, 510] |
| 16 | USWDS | Source Sans Pro, Merriweather, Roboto Mono, Public Sans (open) | 9 theme steps (3xs-3xl) | 16 / 1.62 | Sizes normalized by cap height per font | [S-L09-536, 539] |
| 17 | Radix Themes | System stack | 9 numbered | 16/24 | Hand-tuned; all sizes x a `scaling` factor | [S-L09-559] |
| 18 | shadcn/ui | Per preset: Geist, Inter, Figtree, JetBrains Mono, Noto Sans + Playfair | Tailwind sizes | Controls 14px; base 16/24 | Inherits Tailwind | [S-L09-591, 592, 593] |
| 19 | Tailwind | System stacks | 13 sizes | Base 16/24 | Hand-tuned | [S-L09-604] |
| 20 | Chakra UI | Inter + system | 14 sizes, 15 text styles | 16/24 | Hand-tuned | [S-L09-631, 632] |
| 21 | Mantine | System stack | 11 (5 text + 6 headings) | 16 / 1.55 | Hand-tuned | [S-L09-643] |
| 22 | Geist | Geist Sans, Geist Mono, Geist Pixel (custom, OFL) | 29 classes | 14/20 | Hand-tuned, named by px; -0.06em tracking at 40-72px | [S-L09-617, 618, 625] |
| 23 | Encore | Spotify Mix (bespoke, 2024) | 10 responsive size tokens | 16px | Responsive per device class | [S-L09-470, 473] |
| 24 | Airbnb DLS | Airbnb Cereal VF (2018) | Value-in-name styles; 13 sizes | 14 or 16 [inferred] | Hand-tuned | [S-L09-478, 482] |
| 25 | Linear | Inter + Inter Display (app); Inter Variable + Berkeley Mono (site) | Site: 6 text + 9 titles | Site 15 / 1.6 | n/p for the app | [S-L09-652, 656] |

**Patterns.** Body size splits by audience: 13px (Polaris, SLDS) and 14px (Fluent web, Carbon, Atlassian, Primer, Ant, Blade, Geist) for work tools; 16px (Material Body Large, Spectrum, Gestalt, Uber, USWDS, Radix, Tailwind, Chakra, Mantine, Encore) for general and consumer UI; 17pt for iOS; 19px for GOV.UK. Named styles cluster at 11-15. Only Carbon and Ant generate sizes from a formula; everyone else hand-tunes [S-L09-213, 407]. Typeface posture splits three ways: system stack (Apple, Fluent, SLDS, Ant, Radix, Tailwind, Mantine), open neutral face (Inter or Roboto: Material, Polaris, Paste, Chakra, Linear), custom face (Carbon Plex, Spectrum Adobe Clean, Atlassian Sans, Primer Mona Sans, Uber Move, GOV.UK Transport, Geist, Pin Sans, Spotify Mix, Cereal).

### M5. Spacing

| # | System | Base unit | Scale (px unless noted) | Evidence |
|---|---|---|---|---|
| 1 | Material 3 | 8dp (`space100`) | 0, 2, 4, 6, 8, 10, 12, 14, 16, 20, 24, 32, 36, 40, 48, 56, 64, 72 dp (Compose only) | [S-L09-122, 123] |
| 2 | Apple HIG | None published | ~12pt around bezeled elements, ~24pt around unbezeled; the "8pt grid" is a community convention [inferred] | [S-L09-144, 145] |
| 3 | Fluent 2 | 4 | 0, 2, 4, 6, 8, 10, 12, 16, 20, 24, 32 (size ramp 2-56) | [S-L09-172, 190] |
| 4 | Carbon | 8 (with 2 and 4 fillers) | 2, 4, 8, 12, 16, 24, 32, 40, 48, 64, 80, 96, 160 | [S-L09-201] |
| 5 | Spectrum 2 | None single | 1, 2, 4, 6, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96 | [S-L09-221] |
| 6 | SLDS 2 | 4 | 4, 8, 12, 16, 24, 32, 40, 48, 56, 64, 72, 80 | [S-L09-237] |
| 7 | Atlassian | 8 (`space.100`) | 0, 2, 4, 6, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80 | [S-L09-247] |
| 8 | Polaris | 4 (`space-100`) | 0, 1, 2, 4, 6, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 112, 128 | [S-L09-303] |
| 9 | Primer | 4 [inferred from `base-size-4`] | 2, 4, 6, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 64, 80, 96, 112, 128 | [S-L09-324, 325] |
| 10 | Paste | 4 with a 2 half-step | 2, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, then +4 up to 120 | [S-L09-352] |
| 11 | Gestalt | 4 | 0, 1, 2, 4, 6, 8, then 4px steps 12-64 | [S-L09-367] |
| 12 | Uber Base | 4 (`scale100`) | 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 28, 32, 36, 40, 48, 56, 64, 96, 128, 192 | [S-L09-430] |
| 13 | Ant Design | 4 (derived: 4 x (4 + n)) | 4, 8, 12, 16, 20, 24, 32, 48 | [S-L09-406, 408] |
| 14 | Blade | 4 with a 2 half-step | 0, 2, 4, 8, 12, 16, 20, 24, 32, 40, 48, 56 | [S-L09-448] |
| 15 | GOV.UK | 5 | 0, 5, 10, 15, 20, 25, 30, 40, 50, 60 (steps 4-9 shrink on mobile) | [S-L09-508] |
| 16 | USWDS | 8 ("1 unit") | 1, 2, 4, 8, 12, 16, 20, 24, 32, 40, 48, 56, 64, 72, 80, 120 | [S-L09-540] |
| 17 | Radix Themes | 4 | 4, 8, 12, 16, 24, 32, 40, 48, 64 (x scaling 0.9-1.1) | [S-L09-559] |
| 18 | shadcn/ui | 4 (Tailwind multiplier) | Any n x 4 | [S-L09-593] |
| 19 | Tailwind | 4 (`--spacing: 0.25rem`) | Any n x 4 | [S-L09-604, 613] |
| 20 | Chakra UI | 4 | 34 steps, 2 to 384 | [S-L09-631] |
| 21 | Mantine | None strict | xs 10, sm 12, md 16, lg 20, xl 32 | [S-L09-643] |
| 22 | Geist | 4 | Full scale n/p; control heights 32 / 36 / 40 | [S-L09-618] |
| 23 | Encore | 16 base with tighter/looser steps | 2, 4, 6, 8, 12, 16, then 20-64 (small screens) or 24-128 (medium) | [S-L09-470] |
| 24 | Airbnb DLS | 8-based | Micro 2, 4, 8, 12, 16, 24, 32; macro 16, 24, 32, 40, 48, 64, 80 | [S-L09-482] |
| 25 | Linear | n/p | Site paddings 24 / 64 | [S-L09-656] |

**Pattern: the universal spacing ladder.** 22 systems publish a spacing scale (Apple, Geist and Linear do not). 17 of those 22 contain all nine steps **4, 8, 12, 16, 24, 32, 40, 48, 64**, either as named steps or through a 4px multiplier. Fluent (no 40, 48 or 64; its ramp stops at 32 [S-V1b-074]), Blade (no 64) and Ant (no 40 or 64) miss only upper steps. Just two systems break the pattern: GOV.UK (5px base) and Mantine (5 named steps: 10, 12, 16, 20, 32) [inferred count from the table]. "4px vs 8px base" is mostly a naming difference: the 8px systems (Material, Carbon, Atlassian, USWDS, Airbnb) all add 2px and 4px fillers.

### M6. Radius

| # | System | Radius scale (px) | Default control radius | Evidence |
|---|---|---|---|---|
| 1 | Material 3 | 0, 4, 8, 12, 16, 20, 28, 32, 48, full | Pill (full) buttons; square variants 12/16/28; press morphs to 12 | [S-L09-101, 169] |
| 2 | Apple HIG | No numeric scale; concentric rule (child corner shares the parent's center) | Concentric; `ConcentricRectangle` API | [S-L09-153, 157, 158] |
| 3 | Fluent 2 | 0, 2, 4, 6, 8, 12, 16, 24, 32, 40, circular | 4 (2 under 32px tall); Windows overlays 8 | [S-L09-137, 171, 191] |
| 4 | Carbon | v11 buttons 0; new tokens 0, 2, 4, 8, 16, 24, max | 0 (v11); 4 on inputs and tags under the v12 flag | [S-L09-201, 203, 258] |
| 5 | Spectrum 2 | 0, 3, 4, 5, 6, 7, 8, 9, 10, 16, full; size-dependent | Pill buttons; action buttons 6-10 by size | [S-L09-221, 226] |
| 6 | SLDS 2 | Cosmos 4, 8, 12, 20, pill; Lightning Blue 2, 4, 8, 16 | Cosmos: pill buttons, 8 inputs, 20 containers. Lightning Blue: 4 | [S-L09-237] |
| 7 | Atlassian | 2, 4, 6, 8, 12, 16, full, tile 25% | 6 (buttons, inputs) | [S-L09-247, 253] |
| 8 | Polaris | 0, 2, 4, 6, 8, 12, 16, 20, 30, full | 8 | [S-L09-303, 377] |
| 9 | Primer | 3, 6, 12, full | 6 | [S-L09-324, 325] |
| 10 | Paste | 0, 2, 4, 8, 12, 16, 20, 24, 28, 32, pill, circle | 8 | [S-L09-352, 356] |
| 11 | Gestalt | 0, 4, 8 ... 32, pill, circle | Classic 24 (near-pill); VR 8 / 12 / 16 by size | [S-L09-367, 371] |
| 12 | Uber Base | 2, 4, 8, 12, 16 | 8 on controls; 0 on cards, modals, toasts | [S-L09-430] |
| 13 | Ant Design | 2, 4, 6, 8 (derived from seed 6) | 6 | [S-L09-403, 405] |
| 14 | Blade | 0, 2, 4, 8, 12, 16, 20, 24, max, round | 8 (12 on large) | [S-L09-448, 486] |
| 15 | GOV.UK | 0 | 0 | [S-L09-531] |
| 16 | USWDS | 0, 2, 4, 8, pill | 4 | [S-L09-540] |
| 17 | Radix Themes | 3, 4, 6, 8, 12, 16 x factor (none 0, small 0.75, medium 1, large 1.5, full) | 4 | [S-L09-559, 560] |
| 18 | shadcn/ui | Base 10: 6, 8, 10, 14, 18, 22, 26 | 8 (Vega style); cards 14 | [S-L09-587, 591] |
| 19 | Tailwind | 2, 4, 6, 8, 12, 16, 24, 32, full | n/a (no components) | [S-L09-604] |
| 20 | Chakra UI | 0, 1, 2, 4, 6, 8, 12, 16, 24, 32, full; layer radii l1/l2/l3 | 4 (l2) | [S-L09-631, 632] |
| 21 | Mantine | 2, 4, 8, 16, 32 | 8 in v9 (was 4) | [S-L09-643, 646] |
| 22 | Geist | 6, 12, 16 (bundled into "materials") | 6 | [S-L09-618, 620] |
| 23 | Encore | 2, 4, 6, 8, 16 (+ 500 pill on the play button) | 4 | [S-L09-470] |
| 24 | Airbnb DLS | 4, 8, 12, 16, 20, 24/28, 32 | 12 buttons; 20 cards and media | [S-L09-482] |
| 25 | Linear | Site: 4, 6, 8, 12, 16, 24, 32, pill | n/p | [S-L09-656] |

**Pattern.** Default control radius: 0 (GOV.UK, Carbon v11), 4 (Fluent, USWDS, Radix, Chakra, Encore, SLDS Lightning Blue), 6 (Atlassian, Primer, Ant, Geist), 8 (Polaris, Paste, Uber, Blade, Mantine v9, shadcn), 12 (Airbnb), pill (Material, Spectrum 2, SLDS Cosmos, Gestalt classic). The median is 6px. **The trend is rounder**: Carbon 0 -> 4 (v12), Mantine 4 -> 8 (v9), SLDS 4 -> pill (Cosmos), Spectrum 1 sharp -> Spectrum 2 pill, Material Expressive adds 20/32/48 [S-L09-258, 646, 237, 228, 101]. Three advanced mechanisms are worth copying: size-dependent radius (Spectrum), concentric radius (Apple), and nested "layer radii" that step down inside containers (Chakra) [S-L09-221, 158, 632].

### M7. Elevation

| # | System | Approach | Levels and example values | Evidence |
|---|---|---|---|---|
| 1 | Material 3 | Tonal surface colors + shadows | Shadow levels 0/1/3/6/8/12 dp; 5 surface-container tones (light N100 to N90) | [S-L09-103, 104] |
| 2 | Apple HIG | Materials, not shadows | Liquid Glass (regular, clear) for controls and navigation; 4 content materials (ultraThin to thick); dark "base vs elevated" backgrounds | [S-L09-141, 163] |
| 3 | Fluent 2 | Dual shadows (ambient + key); Windows adds Mica/Acrylic and strokes | 6: shadow2/4/8/16/28/64 = `0 0 2px` ambient + `0 n/2 n` key; light .12/.14, dark .24/.28 | [S-L09-138, 179, 187] |
| 4 | Carbon | Tonal layers; one shadow for floating UI | `$layer-01..03` against `$background`; `0 2px 6px` at .3 (light) | [S-L09-212, 214] |
| 5 | Spectrum 2 | Background layers + soft multi-layer shadows | base / layer-1 / layer-2; emphasized, elevated (3 layers), dragged (3 layers), black .08-.2 | [S-L09-221] |
| 6 | SLDS 2 | Shadows + surfaces | 4 levels; Cosmos stacks 3 layers with `light-dark()` alpha; Lightning Blue 1 layer | [S-L09-237] |
| 7 | Atlassian | Surfaces + shadows; in dark mode higher = lighter | sunken, default, raised, overlay (+ overflow); raised `0 1px 1px` + 1px outline | [S-L09-247, 253] |
| 8 | Polaris | Shadows + bevels and insets | shadow-0 to 600 (`0 1px 0 .07` to `0 20px 20px -8px .28`) + bevel/inset + 12 button shadows | [S-L09-303] |
| 9 | Primer | Borders first, light shadows second | 1px `#d1d9e0` borders; 8 shadow tokens (resting small to floating xlarge) | [S-L09-331] |
| 10 | Paste | Shadows + "shadow borders" | low / default / high + elevation 05/10/20; 68 shadow-border tokens draw borders with box-shadow | [S-L09-352, 356] |
| 11 | Gestalt | Shadows | VR 5 levels (surface, raised x3, floating); separate dark sets | [S-L09-367] |
| 12 | Uber Base | Shadows + inset overlays for pressed states | shadow400-700 (`0 1px 4px` to `0 8px 24px`, all .16) | [S-L09-430] |
| 13 | Ant Design | 1px borders + 3 shadows for popups | boxShadow 3-layer (.08/.12/.05) | [S-L09-408, 426] |
| 14 | Blade | Tinted low-opacity shadows + backdrop blur | 3 levels at hsla(200,10%,18%,.06) | [S-L09-449] |
| 15 | GOV.UK | None: borders only | 0 levels; button has a solid 2px bottom edge | [S-L09-509, 531] |
| 16 | USWDS | Shadows, used sparingly | 5 levels, all black .1 (`0 1px 4px` to `0 16px 32px`) | [S-L09-541] |
| 17 | Radix Themes | Shadows that start with a 1px ring; translucent panels (64px blur) | 6 levels | [S-L09-559] |
| 18 | shadcn/ui | Hairline rings + light shadows | `ring-1 ring-foreground/10 shadow-xs` on cards | [S-L09-591, 593] |
| 19 | Tailwind | Shadows | 7 (2xs-2xl) + inset + drop + text shadows | [S-L09-604] |
| 20 | Chakra UI | Shadow + 0-blur ring; inset highlight in dark | 8 tokens | [S-L09-632] |
| 21 | Mantine | Layered diffuse shadows | 5 (xs-xl) at 4-10% | [S-L09-643] |
| 22 | Geist | "Materials": radius + 1px ring + faint shadow bundled | 8 (4 surface, 4 floating) | [S-L09-618, 620] |
| 23 | Encore | Tonal (dark UI) | #121212 -> #1f1f1f -> #2a2a2a | [S-L09-470] |
| 24 | Airbnb DLS | Ring + shadow; translucent "materials" | elevation0-5 + named shadows + 5 materials | [S-L09-482] |
| 25 | Linear | Tonal levels | Site dark: #08090a -> #191a1b in 4 levels | [S-L09-656] |

**Pattern.** Four depth models: (1) shadow ladders of 3-8 levels (most systems); (2) tonal layers where lightness carries depth (Carbon, Material surface containers, Encore, Linear, and every system's dark mode that lightens raised surfaces: Atlassian, Apple elevated backgrounds); (3) borders and rings instead of depth (GOV.UK, Primer, shadcn, Geist); (4) materials and glass (Apple, Airbnb, Radix translucent panels, Fluent on Windows). A 1px ring combined with a soft shadow is the most common modern card recipe (Radix, Chakra, Geist, Airbnb, Atlassian, shadcn) [S-L09-559, 632, 618, 482, 247, 591].

### M8. Motion

| # | System | Durations | Easing (cubic-bezier) | Springs | Reduced motion | Evidence |
|---|---|---|---|---|---|---|
| 1 | Material 3 | 16 tokens: short1-4 50-200, medium1-4 250-400, long1-4 450-600, extra-long1-4 700-1000 | emphasized (0.2,0,0,1); emph-decelerate (0.05,0.7,0.1,1); standard (0.2,0,0,1) | Yes. Two schemes. Standard spatial 0.9 damping / 700 stiffness; Expressive spatial 0.8 / 380 (fast 0.6 / 800); effects springs damping 1.0 | Not verified | [S-L09-102, 105, 106] |
| 2 | Apple HIG | None published in HIG | n/a | SwiftUI default `spring(duration: 0.5, bounce: 0)`; `.smooth` 0, `.snappy` 0.15, `.bouncy` 0.3 | Replace moves with fades; avoid animating blur and depth | [S-L09-143, 145, 154, 155] |
| 3 | Fluent 2 | 8: 50, 100, 150, 200, 250, 300, 400, 500 | easyEase (0.33,0,0.67,1); decelerateMax (0.1,0.9,0.2,1) and 7 more | No | Honors prefers-reduced-motion | [S-L09-139, 174, 175] |
| 4 | Carbon | 6: 70, 110, 150, 240, 400, 700 | Productive standard (0.2,0,0.38,0.9) vs expressive (0.4,0.14,0.3,1) | No | Motion surfaces never animate; stylelint rule | [S-L09-210, 260] |
| 5 | Spectrum 2 | No tokens; React S2 default 150 | (0.45,0,0.4,1) | No | Large-area motion must respect it | [S-L09-223, 226] |
| 6 | SLDS 2 | 0, 50, 100, 200, 400ms named instantly to slowly | No easing hooks | No | Not found | [S-L09-237] |
| 7 | Atlassian | 8: 0, 50, 100, 150, 200, 250, 400, 600 | out-practical (0.4,1,0.6,1); inout-bold (0.4,0,0,1) | Spring as CSS `linear()` (Early Access) | Guidance honors it | [S-L09-247, 253] |
| 8 | Polaris | 0-500 in 50ms steps | ease-out (0.19,0.91,0.38,1) | No | Not found | [S-L09-303] |
| 9 | Primer | micro 100, short 200, medium 300, long 500 | easeOut (0.3,0.8,0.6,1); easeInOut (0.6,0,0.2,1) | No | No token | [S-L09-324, 325] |
| 10 | Paste | No tokens; button 100 | ease-in | react-spring in code (modal: mass 0.5, tension 370, friction 26) | `useReducedMotion`; server render treated as reduced | [S-L09-355, 356] |
| 11 | Gestalt | 0-900 (11 steps) | enter (0.05,0.7,0.1,1); bounce (0,0.35,0,1.25) | No (overshoot curve) | `useReducedMotion` | [S-L09-367, 379] |
| 12 | Uber Base | 100-1000 in 100ms steps + long | decelerate (0.22,1,0.36,1); default (0.83,0,0.17,1) | No | None found | [S-L09-430] |
| 13 | Ant Design | 100, 200, 300 | EaseOut (0.215,0.61,0.355,1); EaseOutBack (0.12,0.4,0.29,1.46) | No | `motion: false` seed; 24 reduce blocks in v6 CSS | [S-L09-403, 404, 426] |
| 14 | Blade | 80, 160, 200, 280, 360, 480, 640, 960 | entrance (0,0,0.2,1); emphasized (0.5,0,0,1); overshoot (0.5,0,0.3,1.5) | No; named motion presets (Fade, Slide, Scale, Stagger...) | Durations set to 0 | [S-L09-448, 456, 458] |
| 15 | GOV.UK | None | n/a | No | n/a | [S-L09-503] |
| 16 | USWDS | 150 | ease-in-out | No | Since 3.13.0 | [S-L09-541, 549] |
| 17 | Radix Themes | Per component: 100-200 | (0.16,1,0.3,1) | No | Animations gated by no-preference | [S-L09-560] |
| 18 | shadcn/ui | Overlays 100; default 150 | (0,0,0.2,1); (0.22,1,0.36,1) | No | Not in the Vega style CSS | [S-L09-591, 593] |
| 19 | Tailwind | Default 150 | (0.4,0,0.2,1); in (0.4,0,1,1); out (0,0,0.2,1) | No | Opt-in `motion-safe:` / `motion-reduce:` | [S-L09-604, 661] |
| 20 | Chakra UI | 7: 50, 100, 150, 200, 300, 400, 500 | ease-in-smooth (0.32,0.72,0,1) + CSS standards | No | No global rule found | [S-L09-631] |
| 21 | Mantine | Transition default 250 | ease | No | `respectReducedMotion` off by default | [S-L09-643, 645] |
| 22 | Geist | Popover 200, overlay 300 | swift (0.175,0.885,0.32,1.1), a small overshoot | No | Guideline says provide one | [S-L09-618, 626] |
| 23 | Encore | 6: 50, 100, 150, 200, 250, 300 | productive (0.3,0,0,1) | No | 28 no-preference gates in web CSS | [S-L09-470] |
| 24 | Airbnb DLS | Spring-derived, ~450-760 | standard (0.2,0,0,1); enter (0.1,0.9,0.2,1) | Yes: 6 springs as tokens (stiffness 100-300, damping 14-35, mass 1) + CSS `linear()` | 3 rules on the homepage | [S-L09-482] |
| 25 | Linear | Site 100 / 180 | Penner ease-out set | n/p | n/p | [S-L09-656] |

**Pattern.** Product motion lives between 100 and 300ms nearly everywhere, with 50ms as the fastest step and 400-700ms reserved for large moves. The most common curve family is a strong ease-out for entering, e.g. (0.2,0,0,1), (0,0,0.2,1), (0.22,1,0.36,1) [S-L09-102, 604, 430]. Named duration ladders have 6-8 steps. The live divergence is **springs**: Material (spring tokens with damping and stiffness), Apple (duration + bounce), Airbnb (physics + precomputed CSS `linear()`), Atlassian (spring as `linear()`) and Paste (react-spring) treat springs as first-class; four more fake a bounce with an overshoot bezier (Gestalt, Blade, Geist, Ant) [S-L09-105, 155, 482, 247, 355, 367, 448, 618, 404]. Carbon's productive vs expressive split is the cleanest "mode" model [S-L09-210].

### M9. Theming and modes

| # | System | Dark mode | High contrast | Density / scale | Brand theming | Evidence |
|---|---|---|---|---|---|---|
| 1 | Material 3 | Yes | Contrast levels -1, 0, 0.5, 1 | Spacing tokens | Dynamic color from a seed or wallpaper; 10 scheme variants | [S-L09-112, 122, 167] |
| 2 | Apple HIG | Yes (OS-level) | Increased Contrast: every system color has 2 extra values | Dynamic Type (12 sizes) | App accent only; iOS 27 glass slider is user-controlled | [S-L09-142, 145, 152] |
| 3 | Fluent 2 | Yes | Yes (HC theme generator, Teams HC) | Per-platform ramps | One brand ramp -> full theme; Web, Teams, Office ramps | [S-L09-170, 178, 181] |
| 4 | Carbon | 2 dark themes (Gray 90, Gray 100) + 2 light | None found [inferred] | Size props xs-2xl | None documented | [S-L09-201, 215, 219] |
| 5 | Spectrum 2 | Yes (+ "wireframe" set) | None in tokens | Desktop vs mobile scale | None public | [S-L09-221, 226] |
| 6 | SLDS 2 | Cosmos via CSS `light-dark()`; Lightning Blue light-only | Not found | "Display Density" page | 2 themes over one structure; Lightning Blue reads the org's brand | [S-L09-237, 242] |
| 7 | Atlassian | Yes + auto | Increased-contrast light and dark | Spacing is a separate theme part | None public; theme "parts" load separately | [S-L09-247, 248, 249] |
| 8 | Polaris | `dark-experimental` | `light-high-contrast-experimental` | `light-mobile` | None: apps must look native to the admin | [S-L09-303, 304] |
| 9 | Primer | Dark + dark dimmed | HC variants of every theme; colorblind and tritanopia themes (14 total) | Pointer size fine / coarse | None | [S-L09-325, 328] |
| 10 | Paste | Yes | Not listed | No | 5 themes + `CustomizationProvider` (white-label) | [S-L09-353, 358, 359] |
| 11 | Gestalt | Yes | No | No | Classic vs VR vs experiment themes; per-script line heights | [S-L09-367, 370] |
| 12 | Uber Base | Yes | No | No | Move variants; `createTheme` | [S-L09-445] |
| 13 | Ant Design | `darkAlgorithm` | No | `compactAlgorithm` (combinable) | Change the seed and everything regenerates | [S-L09-411, 413] |
| 14 | Blade | Yes + system | No | No | `createTheme({brandColor})` with contrast check; neutral theme | [S-L09-451, 459] |
| 15 | GOV.UK | No | Tested with Windows high contrast | No | Organisation colours; generic header for non-GOV.UK services | [S-L09-501, 515] |
| 16 | USWDS | No | Windows HC color file | No | Sass theme tokens at compile time | [S-L09-537, 538] |
| 17 | Radix Themes | Yes | `highContrast` prop | `scaling` 90-110% | accentColor, grayColor, radius factor | [S-L09-559] |
| 18 | shadcn/ui | Yes | No | Chosen via "style" | Edit CSS variables or apply a preset code; 8 styles | [S-L09-582, 587] |
| 19 | Tailwind | `dark:` variant | `contrast-more:`, `forced-colors:` variants | No | Override `@theme` | [S-L09-612, 661] |
| 20 | Chakra UI | Yes | No | No | `createSystem`; `colorPalette` per component | [S-L09-632, 635] |
| 21 | Mantine | Yes (+ auto) | No | `--mantine-scale` | `createTheme`; `virtualColor` | [S-L09-643, 644, 651] |
| 22 | Geist | Yes | No | No | None | [S-L09-618] |
| 23 | Encore | Dark default + light | No | Device-size layout themes | Color sets re-skin any subtree; local systems | [S-L09-470] |
| 24 | Airbnb DLS | Web: light only | No | No | Sub-brand palettes (Plus, Luxe) | [S-L09-482] |
| 25 | Linear | Yes + custom themes | Contrast is a theme input | n/p | Base + accent + contrast generator | [S-L09-652] |

**Pattern.** 21 of 25 ship dark mode; Polaris has only an experimental one; GOV.UK, USWDS and Airbnb's website have none (SLDS's older Lightning Blue theme is also light-only). High contrast is rarer (9 systems) and takes three forms: a separate theme (Primer, Atlassian, Fluent, Polaris), a contrast dial (Material, Linear), or extra values per color or component (Apple, Radix, Tailwind variants). A single global density or scale control is uncommon: Ant (compact algorithm), Radix (scaling 90-110%), Mantine (one scale multiplier), Spectrum (desktop vs mobile token sets) and Primer (pointer size), plus SLDS's density page and Polaris's mobile theme. Carbon and most others handle density per component with size props. Brand theming splits into "one brand color in, full theme out" generators (Material, Fluent, Ant, Blade, Linear) and "edit the variables" (Radix, shadcn, Chakra, Mantine, Tailwind) [S-L09-116, 170, 413, 459, 652].

### M10. Components and documentation

| # | System | Component count (2026-09-23 unless noted) | Sections on every component page | Evidence |
|---|---|---|---|---|
| 1 | Material 3 | 36 pages on m3.material.io | Overview, Specs, Guidelines, Accessibility | [S-L09-124] |
| 2 | Apple HIG | 64 pages in 8 categories | Intro, Best practices, topic sections, Platform considerations, Resources, Change log | [S-L09-162] |
| 3 | Fluent 2 | 47 React v9 packages (+12 iOS, 5 Android pages) | Preview, Resources, Behavior, Layout, Accessibility, Content | [S-L09-184, 196] |
| 4 | Carbon | 42 on the site | Usage, Style, Code, Accessibility | [S-L09-216, 257] |
| 5 | Spectrum 2 | 68 in React S2 docs | Overview, Resources, Anatomy, Component options, States, Behaviors, Usage guidelines | [S-L09-223, 227, 256] |
| 6 | SLDS 2 | 48 docs pages | Not verified (JavaScript-only pages) | [S-L09-242] |
| 7 | Atlassian | ~69 | Examples, Code, Usage, Changelog | [S-L09-251, 254] |
| 8 | Polaris | 50 web components (App Home) + 15 patterns | Properties (events, slots), Examples, Best practices, Limitations | [S-L09-312, 344] |
| 9 | Primer | 62 public + 24 internal | React (examples, props), Guidelines, Accessibility; status labels | [S-L09-332, 333] |
| 10 | Paste | 86 doc pages | Guidelines, API, Changelog | [S-L09-353, 357] |
| 11 | Gestalt | 77 | Props, Usage, Best practices, Accessibility, Localization, Variants, Writing, Quality checklist, Related | [S-L09-365, 366] |
| 12 | Uber Base | Base Web 79 (+10 utilities); internal ~70 | Playground, examples, overrides, API | [S-L09-434, 436] |
| 13 | Ant Design | 73 entries (~68 true components) | When To Use, Examples, API, Semantic DOM, Design Token, FAQ, Design Guide | [S-L09-414, 422] |
| 14 | Blade | ~66 + 8 motion presets | Description, Figma link, Usage sandbox, Imports, Properties, Stories | [S-L09-455, 457] |
| 15 | GOV.UK | 37 components + 30 patterns | When to use, How it works, Research on this component, Recent changes, Help improve it | [S-L09-512, 513, 516] |
| 16 | USWDS | 47 | Preview, Code, Guidance (when to use, when to consider something else, usability, accessibility), Accessibility test status, Latest updates | [S-L09-543, 544] |
| 17 | Radix | Primitives 30 + 5 utilities; Themes 36 | Features, Anatomy, API Reference, Examples, Accessibility (keyboard) | [S-L09-558, 561, 570] |
| 18 | shadcn/ui | 64 (Base UI) / 65 (Radix) / 63 (React Aria) | Installation, Usage, Examples, RTL, API Reference | [S-L09-577, 590] |
| 19 | Tailwind | 0 in core | Quick reference, Examples, Customizing your theme | [S-L09-660] |
| 20 | Chakra UI | 114 | Usage, Examples, Props | [S-L09-640] |
| 21 | Mantine | 118 core (+ 16 dates, 23 charts, 14 schedule) + 82 hooks | Usage configurator, Examples, Props, Styles API | [S-L09-647] |
| 22 | Geist | ~70 | Examples per variant, Best Practices; Markdown twin of every page | [S-L09-619, 622] |
| 23 | Encore | n/p | n/p | [S-L09-469] |
| 24 | Airbnb DLS | n/p | n/p | [S-L09-477] |
| 25 | Linear | n/p | n/p | none |

**Pattern.** Among the 21 systems with a count, 15 sit between 40 and 80 components (median 64); only the open-source React libraries go past 100 (Chakra 114, Mantine 118). Counts depend on how "component" is defined (Material documents 36 pages but ships 120 token files in Compose) [S-L09-107, 124]. The component page skeleton that nearly everyone shares is: **usage guidance ("when to use"), live examples by variant, API or props, accessibility**. Differentiators worth copying: GOV.UK's "Research on this component", Gestalt's Writing, Localization and quality checklist, USWDS's accessibility test status, Ant's "Semantic DOM" and per-component token table, and Geist's Markdown twin for agents [S-L09-516, 366, 544, 422, 619].

### M11. Accessibility and governance

| # | System | Accessibility stance | Governance / contribution | Evidence |
|---|---|---|---|---|
| 1 | Material 3 | Contrast built into HCT (tone difference 40 -> 3:1, 50 -> 4.5:1); contrast levels; no WCAG version found | Central Google team; no public RFC | [S-L09-116, 121, 167] |
| 2 | Apple HIG | 4.5:1 below 18pt, 3:1 above; default hit targets iOS 44x44 pt (minimum 28x28), macOS 28 (minimum 20), visionOS 60 (minimum 28) | Closed; big update each WWDC, dated change log on every page | [S-L09-145, 147] |
| 3 | Fluent 2 | WCAG 2.1 AA; targets 44 (web/iOS) and 48 (Android) | Open monorepo, change files, contrib repo, preview packages | [S-L09-180, 190, 193] |
| 4 | Carbon | IBM Accessibility Checklist (WCAG AA, Section 508, EN) | Central + open contribution, office hours | [S-L09-219] |
| 5 | Spectrum 2 | No level stated; 2px focus ring with 2px gap | Central; web components accept outside contributions; Design Data Spec | [S-L09-221, 232, 233] |
| 6 | SLDS 2 | WCAG AA (4.5:1, 3:1) | Central; seasonal release train; SLDS Linter enforces adoption | [S-L09-236, 240, 243] |
| 7 | Atlassian | WCAG 2.1 AA; increased-contrast themes | Central; Early Access -> Beta -> GA phases; Atlassian-only contributions | [S-L09-250, 253, 254] |
| 8 | Polaris | WCAG 2.1 A/AA (React docs); web components warn on missing labels | Central; React repo archived | [S-L09-304, 314, 342] |
| 9 | Primer | WCAG 2.2 AA; colorblind and tritanopia themes | Central; no external contributions; ADRs | [S-L09-334, 338] |
| 10 | Paste | Ship gate: nothing below WCAG 2.1 AA | Anyone at Twilio contributes with core-team pairing | [S-L09-358, 359] |
| 11 | Gestalt | WCAG 2.2 AA on one page, 2.1 AA on another (conflict); 175 Playwright a11y specs | Central; changes ship behind experiments | [S-L09-363, 369, 372] |
| 12 | Uber Base | "A11y first process"; no level published | GitHub PRs; one planned major a year; view-tree adoption counter | [S-L09-436, 440, 484] |
| 13 | Ant Design | No target; its own DESIGN.md says white on #1677ff fails AA (4.1:1) | Open PRs; core team at Ant Group | [S-L09-460] |
| 14 | Blade | WCAG 2.0/2.1 techniques (RFC); contrast auto-check in `createTheme` | Public RFCs; per-component decision docs | [S-L09-459, 461, 462] |
| 15 | GOV.UK | WCAG 2.2 AA; tested with assistive tech; works without JavaScript | Central GDS; community backlog; criteria Useful, Unique -> Usable, Consistent, Versatile | [S-L09-515, 517, 522] |
| 16 | USWDS | Section 508 baseline; targets 2.1 AA, strives for 2.2; published conformance report | Central GSA; 45-day open comment for new components | [S-L09-545, 546] |
| 17 | Radix | WAI-ARIA APG patterns; contrast stated in APCA | Company-maintained open source | [S-L09-563, 570] |
| 18 | shadcn/ui | Inherited from the chosen primitive layer; no level | Maintainer-led; open registry schema | [S-L09-589] |
| 19 | Tailwind | None stated; motion and contrast variants | Company-led; now inside Shopify | [S-L09-606, 661] |
| 20 | Chakra UI | "Accessible"; behavior from Ark UI; no level | Maintainer-led; public discussions | [S-L09-638, 640] |
| 21 | Mantine | WAI-ARIA; jest-axe; no level | Maintainer-led | [S-L09-650] |
| 22 | Geist | Prefers APCA over WCAG 2; no level | Internal | [S-L09-626] |
| 23 | Encore | Theming algorithm guarantees contrast; no level | Federated "system of systems" | [S-L09-469, 472] |
| 24 | Airbnb DLS | "Universal" principle; no level | Central DLS team (2016 description) | [S-L09-477] |
| 25 | Linear | Contrast is a theme input; no level | In-house; two designers using coding agents (2026) | [S-L09-652, 654] |

**Pattern.** Where a target is stated, it is WCAG AA (2.1 or 2.2): 4.5:1 for text, 3:1 for large text and UI parts. 11 systems state a level (Apple via its AA ratios, Fluent, Carbon, SLDS, Atlassian, Polaris, Primer, Paste, Gestalt, GOV.UK, USWDS). 14 state none, mostly the open-source libraries, which delegate accessibility to their primitives, and the internal brand systems. Governance is overwhelmingly central (one team owns the system); only Spotify runs a federated model. Structured outside contribution exists in Carbon ("anyone can contribute", office hours), GOV.UK (community backlog with published criteria), USWDS (public proposals, 45-day comment), Fluent (a contrib repo) and Spectrum's web components; Blade publishes its RFCs. Primer and Atlassian accept staff contributions only [S-L09-469, 219, 517, 545, 180, 232, 461, 338, 254].

### M12. Notable innovation and visual signature

| # | System | Notable innovation | Visual signature: the levers that make it look like itself | Evidence |
|---|---|---|---|---|
| 1 | Material 3 | Seed color -> tonal palettes -> roles (HCT); spring motion tokens; shape morphing (35 shapes) | Tonal, same-hue surfaces instead of gray; pill buttons and 28-48dp corners; big type jumps (57 vs 16); bouncy spatial springs | [S-L09-101, 104, 105, 116, 168] |
| 2 | Apple HIG | Liquid Glass as a separate control layer; concentric corners; Dynamic Type | Controls float on glass over full-bleed content; mostly gray UI with one accent; SF 17pt body under a 34pt title; critically damped springs | [S-L09-140, 141, 142, 158] |
| 3 | Fluent 2 | One language, native ramps per platform; dual shadow; one ramp -> full theme; headless React preview (2026) | 4px corners; Segoe 14/20 with semibold titles; near-neutral surfaces with one blue; soft two-part shadows; short non-bouncy motion | [S-L09-170, 171, 177, 179, 199] |
| 4 | Carbon | Productive vs expressive modes for type and motion; layer tokens; AI "aura" tokens | 0px corners; IBM Plex with light (300) large headings; tonal layers, almost no shadow; true grays + one blue | [S-L09-210, 212, 213, 258] |
| 5 | Spectrum 2 | Desktop vs mobile token sets; Leonardo color; size-dependent radius | Pill buttons; highlight color removed from common controls; solid white base; extra-bold headings; soft 3-layer shadows | [S-L09-221, 223, 226, 228] |
| 6 | SLDS 2 | 4-tier styling hooks; one component set, two themes; linter-driven migration | Cosmos: pill buttons, 20px containers, hover lift. Lightning Blue: 4px everywhere. 13px system text | [S-L09-237, 240] |
| 7 | Atlassian | Theme "parts" (color, spacing, type, shape, motion) loaded separately; per-pattern motion tokens | Inter-derived 14/20 text with 653-weight headings; 6px corners; alpha borders and fills; minimal shadows | [S-L09-247, 252, 253] |
| 8 | Polaris | Design system shipped as a versioned CDN runtime with a stable channel | Near-black primary button; pure R=G=B grays; bevelled buttons; 13px Inter at weight 450 | [S-L09-303, 313] |
| 9 | Primer | 14 themes incl. colorblind; token spec and MCP for agents | 1px borders on white; cool blue-grays; green primary + blue accent; 14px body, 6px corners | [S-L09-328, 329, 331, 336] |
| 10 | Paste | Named-element customization for white-label UIs | Navy-tinted neutrals; box-shadow borders; strong 4px focus ring; spring overlays | [S-L09-352, 356, 359] |
| 11 | Gestalt | Per-script line heights; whole themes A/B-tested by experiment flags | Pinterest red as the only strong fill; near-pill classic buttons; warm grays in VR; bounce easing | [S-L09-367, 370, 371] |
| 12 | Uber Base | Design-system observability (adoption counter on native view trees) | Black-on-white foundation, blue only as accent; Uber Move 700 headings; 0px surfaces with 8px controls | [S-L09-430, 431, 433, 440] |
| 13 | Ant Design | Seed -> Map -> Alias generation; dark and compact as algorithms | 14px / 32px dense controls; 6px corners; blue only for interaction; borders + popup-only shadows | [S-L09-403, 405, 413] |
| 14 | Blade | One React API for web and React Native; brand-color white-label with contrast check | TASA Orbiter headings over Inter; cool azure on blue-gray; 0.5px hairlines; low-opacity blue-gray shadows | [S-L09-449, 450, 459, 461] |
| 15 | GOV.UK | Evidence-first docs; whole-question patterns; yellow focus state | 19px text in 2 weights; 0 radius, no shadows; thick black borders; yellow #ffdd00 focus; one green button | [S-L09-507, 509, 516, 529, 531] |
| 16 | USWDS | Grade-based color with "magic number" contrast; cap-height type normalization; public domain | Merriweather headings over Source Sans 16/1.62; federal blue + red; 4px buttons; flat | [S-L09-538, 539, 547] |
| 17 | Radix | 12-step "job per step" scale; unstyled accessible primitives; global scaling and radius factors | System font; layered low-contrast grays; ringed shadows; translucent panels; fast expo-out overlays | [S-L09-558, 559, 563] |
| 18 | shadcn/ui | Ships source, not a package; registry + CLI + MCP; presets as a portable code | Achromatic OKLCH neutrals with near-black primary; 10px base radius; hairline borders; 100ms overlays | [S-L09-584, 586, 587, 591] |
| 19 | Tailwind | Tokens that generate their own utilities; single spacing multiplier; OKLCH palette | No fixed look; the default look is white cards, faint ring, soft shadow, 6-12px radius, indigo on slate | [S-L09-604, 609, 613] |
| 20 | Chakra UI | `colorPalette` virtual token; layer radii | Zinc-like neutrals; 4px controls; ring + blur shadows; Inter 14/16 | [S-L09-631, 632, 640] |
| 21 | Mantine | Per-mode brand shade; `virtualColor`; one scale multiplier; 82 hooks | 8px corners; bright blue #228be6; system font 16/1.55; diffuse shadows | [S-L09-643, 646, 651] |
| 22 | Geist | Color steps with fixed jobs; agent-readable docs; open typeface as portable brand | Pure black and white; achromatic grays; tight -0.06em headings; 1px alpha rings; visible grid guides | [S-L09-616, 618, 619, 624] |
| 23 | Encore | Color sets; layered family of systems; Figma sync bot | Near-black #121212 with tonal lifts; one green; Spotify Mix; 2-tier text (#fff, #b3b3b3) | [S-L09-470, 472, 473] |
| 24 | Airbnb DLS | Springs as tokens with physics + CSS `linear()`; Lottie, react-sketchapp, Lona | Rausch accent on white; Cereal with tight titles; 12-20px radii framing photos; ring + soft shadow; materials | [S-L09-482, 483] |
| 25 | Linear | Whole themes generated from 3 inputs in LCH | 4 near-black tonal levels; Inter at 510/590; one violet-blue accent; dense 13-15px text | [S-L09-652, 656] |

## Analysis

### A1. Shared patterns: what nearly every system does (these become the builder's defaults)

Counts come from the matrix above; "n of 25" counts only systems where the value is public.

| # | Shared pattern | How common | Builder default | Evidence |
|---|---|---|---|---|
| 1 | **A semantic token layer over raw values.** Components never reference a hex or px directly. | 24 of 25 (Tailwind is the only single-tier system) | 3 tiers: primitive -> semantic -> component, with the component tier optional | M2; [S-L09-005] |
| 2 | **4px base with the ladder 4, 8, 12, 16, 24, 32, 40, 48, 64**, plus 0 and 2 | 17 of the 22 systems with a published scale contain all nine steps | `space` scale of 0, 2, 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96 | M5 |
| 3 | **Neutral surfaces + one saturated accent + status colors.** Color is reserved for action, selection, focus and status. | All but one of the 24 systems with a default look. Material 3 is the exception: its tonal surfaces tint containers with the primary hue. Encore and Linear apply the same rule on a dark canvas | 1 neutral ramp + 1 accent ramp + 4 status ramps (success, warning, danger, info) | M3, M12 |
| 4 | **Ramps of 10-12 steps**, light to dark | 12 systems at 10-12 steps; long 16-17-step ramps only in multi-surface systems | 12 steps with a fixed job per step (Radix/Geist style), exportable to a 50-950 scale | M3; [S-L09-563, 616] |
| 5 | **Motion in the 100-300ms band** with a named duration ladder of 6-8 steps and a strong ease-out for entering | All 16 systems with motion tokens keep their core durations in this band; every one that defines easing uses an ease-out family for entering (SLDS defines durations only) | Durations 50, 100, 150, 200, 300, 400, 500; enter (0,0,0.2,1) or (0.2,0,0,1); exit (0.4,0,1,1); reduced motion swaps moves for fades | M8 |
| 6 | **Light + dark as baseline modes** | 21 of 25 | Light and dark generated together; high contrast as an optional third mode | M9 |
| 7 | **Small radius scale with a 4-8px default for controls** | 16 of 23 default values sit at 4, 6 or 8; median 6 (22 systems, SLDS counted once per theme) | Scale 0, 2, 4, 6, 8, 12, 16, 24, full; control default 6 | M6 |
| 8 | **11-15 named type styles, hand-tuned, body 14px (tools) or 16px (general)** | 11-15 styles in 12 systems; only Carbon and Ant use a formula | 13 styles (display, headline x3, title x3, body x3, label x3); body 16 or 14 by density preset | M4 |
| 9 | **Component page = usage guidance + live examples + API/props + accessibility** | The shared core of every public doc template | This 4-part skeleton, plus "when not to use" and a changelog | M10 |
| 10 | **Agent-readable exports (2025-2026 wave)**: MCP servers, llms.txt, DESIGN.md, Markdown twins | 12 of 25: Primer, Carbon, Atlassian, Blade, Chakra, Mantine, Spectrum, shadcn, SLDS 2, Uber Base, Ant (DESIGN.md), Geist (Markdown twins) | Generate a machine-readable token spec + usage notes per token, and an MCP-ready manifest | [S-L09-336, 219, 246, 463, 637, 646, 220, 586, 238, 436, 460, 619] |
| 11 | **WCAG AA as the stated floor** (4.5:1 text, 3:1 large text and UI) | All 11 systems that state a target | AA checks on every generated pair; show APCA as a second opinion (Radix and Geist use it) | M11; [S-L09-563, 626] |
| 12 | **1px ring + soft shadow for cards; lighter surfaces for elevation in dark mode** | Ring+shadow in 6 modern systems; dark "lighter = higher" in Atlassian, Material, Apple, Encore, Linear | Elevation tokens that pair a hairline ring with a shadow in light mode and a lighter surface in dark mode | M7 |

### A2. Where systems diverge most (these become the builder's key questions)

Ordered by how much each choice changes the look, judged from the visual-signature column (M12) [inferred ranking].

| # | Divergence | The spread (real values) | Question the builder asks | Evidence |
|---|---|---|---|---|
| 1 | **Shape** | Control radius 0 (GOV.UK, Carbon v11) -> 4-8 (most) -> 12 (Airbnb) -> pill (Material, Spectrum 2, SLDS Cosmos). Trend: rounder in every 2025-2026 revision | "How soft should your product feel? Square, slightly rounded, rounded, or pill?" | M6 |
| 2 | **Depth model** | Shadow ladders; tonal layers (Carbon, Material, Encore, Linear); borders only (GOV.UK, Primer); glass/materials (Apple, Airbnb) | "How do surfaces separate: shadows, color steps, lines, or translucent material?" | M7 |
| 3 | **Color strategy on surfaces** | Monochrome + one accent (Uber #000/#fff, Polaris near-black primary, Geist) vs tonal tinted surfaces (Material) vs brand fields (Encore dark sets) | "Where does your brand color appear: only on actions, on containers, or on whole surfaces?" | M3, M12 |
| 4 | **Density / base size** | Body 13px (Polaris, SLDS) / 14px (Carbon, Atlassian, Ant, Primer) / 16px (Material, Radix, Mantine) / 17pt (iOS) / 19px (GOV.UK); control heights 28-32 (dense) vs 40-48 (touch) | "Who uses it: people working all day in data-heavy tools, or occasional and mobile users?" | M4; [S-L09-403, 540] |
| 5 | **Typeface posture** | System stack (Apple, Fluent, Ant, Radix) vs open neutral (Inter, Roboto) vs custom brand face (Plex, Adobe Clean, Uber Move, Cereal, Spotify Mix, Geist, GDS Transport) | "Do you want the platform's font, a neutral open font, or your own brand typeface?" | M4 |
| 6 | **Color generation and space** | Hand-picked hex vs seed algorithm (HCT, HSV, LCH) vs contrast targets (Leonardo, USWDS grades, APCA steps); sRGB vs OKLCH vs HCT vs P3 | "Do you have fixed brand hexes to keep, or should we generate ramps from one color with guaranteed contrast?" | M3 |
| 7 | **Motion model** | None (GOV.UK) vs bezier ladders (most) vs springs (Material, Apple, Airbnb, Atlassian, Paste); productive vs expressive modes (Carbon, Material) | "Should motion be quick and invisible, or physical and playful?" | M8 |
| 8 | **Theming openness / brand posture** | Locked to one brand (Carbon, Primer, Geist) vs white-label generators (Blade, Paste, Ant, Fluent) vs multi-theme (SLDS two themes, Gestalt experiments, Encore color sets) | "Will other brands or products re-skin this system?" | M9 |
| 9 | **Distribution model** | npm component library (most) vs copy-in source (shadcn) vs CDN runtime (Polaris) vs CSS/HTML only (GOV.UK, USWDS) vs headless primitives (Radix, Fluent preview) vs utilities (Tailwind) | "How will engineers consume it?" | M1; [S-L09-313, 589, 199] |
| 10 | **Platform scope** | Web only (most) vs one API for web + native (Blade) vs per-platform ramps under one language (Fluent) vs native only (Apple) | "Which platforms must share the system?" | M1; [S-L09-461, 185] |

### A3. Personality map

**Axes.** X runs from **productive** (efficient, quiet, dense) to **expressive** (soft, colorful, animated). Y runs from **platform-native or brand-neutral** to **brand-led**. Scores come from measurable levers, not taste, so a builder can compute the same score for a user's own system.

**X score (0-10)** = radius of the default control (0-2px = 0, 3-6px = 1, 8-12px = 2, 16px or more, or pill = 3) + color on surfaces (neutral + one accent = 0, tinted containers = 1, brand or dynamic color on surfaces = 2) + type contrast, largest named display style / body (< 3x = 0, 3-4.5x = 1, > 4.5x = 2) + motion (minimal = 0, bezier tokens = 1, springs or overshoot as tokens = 2) + signature material or imagery (glass or translucency, bevels, shape morphing, photo-first content; 0 or 1).

**Y score (0-10)** = typeface (OS system font = 0, open neutral font = 1, open custom face made for the system = 2, proprietary brand face = 3) + default accent (none or user-chosen = 0, generic blue = 1, fixed brand color = 2) + look (defines or follows the platform's conventions = 0, neutral = 1, own look everywhere = 2) + re-skinnability (built for anyone to re-skin = 0, internal brand themes only = 1, locked = 2) + explicit brand voice or illustration guidance in the system (0 or 1). Platform owners score low on Y because they define the native convention; toolkits score low because they are brand-neutral on purpose.

| # | System | Radius | Surface color | Type contrast | Motion | Material/imagery | **X** | Typeface | Accent | Look | Re-skin | Voice | **Y** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Material 3 | 3 | 2 | 1 (57/16) | 2 | 1 | **9** | 1 | 0 | 0 | 0 | 0 | **1** |
| 2 | Apple HIG | 2 [inferred] | 0 | 0 (34/17) | 2 | 1 | **5** | 0 | 1 | 0 | 1 | 0 | **2** |
| 3 | Fluent 2 | 1 | 0 | 2 (68/14) | 1 | 0 | **4** | 0 | 1 | 0 | 0 | 0 | **1** |
| 4 | Carbon (v11) | 0 | 0 | 2 (92/14) | 1 | 0 | **3** | 2 | 2 | 2 | 2 | 1 | **9** |
| 5 | Spectrum 2 | 3 | 0 | 2 (73/16) | 1 | 0 | **6** | 3 | 2 | 2 | 2 | 0 | **9** |
| 6 | SLDS 2 (Cosmos) | 3 | 0 | 1 (48/13) | 1 | 0 | **5** | 0 | 1 | 2 | 1 | 0 | **4** |
| 7 | Atlassian | 1 | 0 | 0 (32/14) | 1 | 0 | **2** | 2 | 2 | 2 | 2 | 1 | **9** |
| 8 | Polaris | 2 | 0 | 1 (40/13) | 1 | 1 | **5** | 1 | 2 | 0 | 2 | 1 | **6** |
| 9 | Primer | 1 | 0 | 0 (40/14) | 1 | 0 | **2** | 2 | 2 | 2 | 2 | 0 | **8** |
| 10 | Paste | 2 | 0 | 1 (48/14) | 2 | 0 | **5** | 1 | 2 | 2 | 0 | 0 | **5** |
| 11 | Gestalt (classic) | 3 | 0 | 0 (36/16) | 2 | 1 | **6** | 0 | 2 | 2 | 2 | 1 | **7** |
| 12 | Uber Base | 2 | 0 | 2 (96/16) | 1 | 0 | **5** | 3 | 2 | 2 | 1 | 1 | **9** |
| 13 | Ant Design | 1 | 0 | 0 (38/14) | 1 | 0 | **2** | 0 | 1 | 2 | 0 | 0 | **3** |
| 14 | Blade | 2 | 0 | 2 (72/14) | 2 | 0 | **6** | 1 | 2 | 2 | 0 | 0 | **5** |
| 15 | GOV.UK | 0 | 0 | 1 (80/19) | 0 | 0 | **1** | 3 | 2 | 2 | 1 | 1 | **9** |
| 16 | USWDS | 1 | 0 | 1 (48/16) | 0 | 0 | **2** | 2 | 1 | 2 | 0 | 0 | **5** |
| 17 | Radix Themes | 1 | 0 | 1 (60/16) | 1 | 1 | **4** | 0 | 1 | 1 | 0 | 0 | **2** |
| 18 | shadcn/ui (Vega) | 2 | 0 | 0 (36/16) | 1 | 0 | **3** | 1 | 0 | 1 | 0 | 0 | **2** |
| 19 | Chakra UI | 1 | 0 | 1 (72/16) | 1 | 0 | **3** | 1 | 0 | 1 | 0 | 0 | **2** |
| 20 | Mantine | 2 | 0 | 0 (34/16) | 1 | 0 | **3** | 0 | 1 | 1 | 0 | 0 | **2** |
| 21 | Geist | 1 | 0 | 2 (72/14) | 2 | 0 | **5** | 2 | 2 | 2 | 2 | 1 | **9** |
| 22 | Encore | 1 | 0 | 2 (96/16) | 1 | 1 | **5** | 3 | 2 | 2 | 1 | 1 | **9** |
| 23 | Airbnb DLS | 2 | 0 | 1 (72/16) | 2 | 1 | **6** | 3 | 2 | 2 | 2 | 1 | **10** |
| - | Tailwind | no component defaults; not scored. Its default look clusters with shadcn/ui | | | | | | | | | | | |
| - | Linear | app values not public; placed from public levers only: dense 13-15px text, tonal depth, 100-180ms motion, Inter [inferred] | | | | | ~2-3 | | | | | | ~5 |

Scores are my application of the rubric to values in the matrix [inferred]. Sources for each lever are the matrix rows above.

**The map** (X = productive to expressive, left to right; Y = brand-led at the top):

| Y \ X | Productive (0-2) | Balanced (3-4) | Leaning expressive (5-6) | Expressive (7-10) |
|---|---|---|---|---|
| **Brand-led (8-10)** | GOV.UK (1,9), Atlassian (2,9), Primer (2,8) | Carbon (3,9) | Uber Base (5,9), Geist (5,9), Encore (5,9), Spectrum 2 (6,9), Airbnb (6,10) | (empty) |
| **Branded, re-skinnable (5-7)** | USWDS (2,5), Linear (~2,~5) [inferred] | | Polaris (5,6), Paste (5,5), Blade (6,5), Gestalt (6,7) | |
| **Neutral toolkits (2-4)** | Ant (2,3) | shadcn (3,2), Chakra (3,2), Mantine (3,2), Radix (4,2) | Apple (5,2), SLDS Cosmos (5,4) | |
| **Platform-native (0-1)** | Tailwind (unscored) | Fluent (4,1) | | Material 3 (9,1) |

**What the map says** [inferred from the scores]:
- **The top-right is empty.** No brand-led system scores above 6 on expressiveness. Brands keep product chrome restrained and spend their personality on typeface, one signature color and imagery. Big expressive moves live in marketing, not in the component layer.
- **Material 3 is alone in the expressive corner.** It is the only system that puts color on surfaces, defaults to pill shapes and ships bouncy springs, all at once. That is why "Material-looking" is so recognizable.
- **The neutral toolkits cluster tightly** (shadcn, Chakra, Mantine, Radix at X 3-4, Y 2). This is the "AI sameness" practitioners complain about this month (L00 topic f, [S-L00-050]): every generated app starts from the same corner. A builder's job is to move users out of this corner on purpose.
- **Productive + brand-led is a real, respected quadrant** (GOV.UK, Atlassian, Primer, Carbon). Identity there comes from typeface and one accent, not from softness or motion.
- **Revisions move right.** Carbon v12 (0 -> 4px), Mantine v9 (4 -> 8px), SLDS Cosmos (4px -> pill), Spectrum 2 (sharp -> pill) and Material Expressive all moved toward the expressive side in 2024-2026 [S-L09-258, 646, 237, 228, 101].

**A second useful axis: density.** Dense (13-14px body, 32px controls): Polaris, SLDS, Carbon, Atlassian, Primer, Ant, Blade, Geist, Linear. Regular (16px body, 36-40px controls): Radix, shadcn, Chakra, Mantine, Tailwind, Gestalt, Uber. Large (17px+ body, or 44-48px controls and touch targets by default): Apple iOS, Material, GOV.UK, USWDS (48px targets), Encore (48px controls) [S-L09-303, 237, 213, 247, 326, 403, 449, 618, 140, 169, 507, 540, 470].

### A4. Decision Cards derived from the benchmark

These cards cover the benchmark-level choices. Lanes L01-L08 hold the deeper cards for each foundation; these add the cross-system evidence.

### DC-L09-01: Shape posture (default control radius)
- **Block path:** Foundations > Shape > Radius scale and default
- **Questions the designer answers:** How soft should the product feel? Do buttons read as rectangles, rounded rectangles, or pills? Should nested elements step their corners down?
- **Options:** 0px (GOV.UK; Carbon v11 buttons) / 4px (Fluent, USWDS, Radix, Chakra) / 6px (Atlassian, Primer, Ant, Geist) / 8px (Polaris, Paste, Blade, Mantine v9, shadcn Vega) / 12px (Airbnb) / pill (Material 3, Spectrum 2, SLDS Cosmos) / rule-based: size-dependent (Spectrum 6-10 by size), concentric (Apple), layer radii (Chakra l1-l3).
- **Visual effect:** 0 reads as official, printed, engineered; 4-6 as businesslike; 8-12 as friendly and modern; pill as consumer, playful, touch-first.
- **Depends on (upstream):** brand personality; density (pill needs taller controls); platform (Apple concentric rules on iOS).
- **Affects (downstream):** buttons, inputs, cards, dialogs, menus, tags, avatars, focus rings (ring radius must follow), image crops.
- **Token encoding:** `$type: dimension`. Primitive `radius.100 = 4px`; semantic `radius.control`, `radius.container`, `radius.overlay`; component `button.radius`. Carbon's new scale 0, 2, 4, 8, 16, 24, max is a clean primitive set [S-L09-201].
- **Platform notes:** iOS 26+ expects concentric corners; Material Expressive adds 20/32/48 and shape morphing on press; web has no concentric primitive.
- **Accessibility constraints:** none direct; keep the focus ring outside the radius so it stays visible.
- **Default + heuristic:** 6px controls, 8-12px containers. Dense tools 4-6px; consumer apps 8-12px or pill. Offer a radius factor slider as Radix does (0, 0.75, 1, 1.5, full) [S-L09-559].
- **Evidence:** M6; [S-L09-101, 158, 221, 237, 258, 559, 632, 646]

### DC-L09-02: Depth model
- **Block path:** Foundations > Elevation
- **Questions the designer answers:** How do layers separate: shadow, color step, line, or translucent material? Does dark mode use the same method?
- **Options:** shadow ladder (Fluent dual shadows, Polaris 7 levels, Tailwind 7) / tonal layers (Carbon layer-01..03, Material surface containers, Encore, Linear) / borders only (GOV.UK, Primer) / ring + soft shadow (Radix, Geist, Chakra, Airbnb) / materials and glass (Apple Liquid Glass, Airbnb materials).
- **Visual effect:** shadows feel tactile and layered; tonal feels flat and calm; borders feel dense and technical; glass feels premium and content-first.
- **Depends on (upstream):** color neutrals (tonal needs 4-5 close neutral steps); dark-mode plan; performance budget (blur is expensive; iOS 27 users report smoother UI with Reduce Transparency, L00 topic e, Tier C).
- **Affects (downstream):** cards, menus, dialogs, sheets, sticky headers, toasts, dragged items.
- **Token encoding:** `$type: shadow` (DTCG composite). Semantic `elevation.surface.raised`, `elevation.shadow.overlay` (Atlassian pattern); or bundled "material" tokens (Geist: radius + ring + shadow) [S-L09-247, 620].
- **Platform notes:** Apple uses materials, not shadows; Windows uses Mica/Acrylic; Android Material uses tonal color.
- **Accessibility constraints:** separation must not rely on shadow alone; keep a 3:1 boundary for essential UI parts (WCAG 1.4.11) [inferred: standard rule, not re-fetched here]; provide Reduce Transparency fallbacks for glass.
- **Default + heuristic:** light mode: 1px ring + 3-level soft shadow; dark mode: lighter surface per level. Data-dense tools: tonal or borders.
- **Evidence:** M7; [S-L09-104, 141, 179, 212, 247, 531, 559, 618]

### DC-L09-03: Color generation method
- **Block path:** Foundations > Color > Palette generation
- **Questions the designer answers:** Do you have brand hexes you must keep? Do you want ramps generated from one color? Should contrast be guaranteed by construction?
- **Options:** hand-picked hex (Carbon, Primer, Atlassian, GOV.UK) / seed algorithm (Material HCT, Ant HSV, Blade `createTheme`, Fluent brand ramp, Linear 3-input LCH) / contrast targets (Spectrum Leonardo, USWDS grades with "magic number", Radix APCA-guaranteed steps).
- **Visual effect:** hand-picked keeps brand nuance; algorithmic gives even, harmonious ramps; contrast-targeted gives predictable legibility across hues.
- **Depends on (upstream):** brand color; color space choice (OKLCH or HCT for perceptual evenness).
- **Affects (downstream):** every semantic color role, dark mode, data-viz palettes, state layers.
- **Token encoding:** `$type: color` with DTCG 2025.10 color spaces (OKLCH, Display P3 allowed per L00 [S-L00-008]). Primitive `color.blue.600`; semantic `color.bg.accent`.
- **Platform notes:** P3 on Apple and modern browsers (Geist ships OKLCH under `@media (color-gamut: p3)`) [S-L09-618].
- **Accessibility constraints:** 4.5:1 text, 3:1 UI. Ant's own default #1677ff fails 4.5:1 with white text (4.1:1), a warning for seed-based systems [S-L09-460].
- **Default + heuristic:** generate from a seed in OKLCH with contrast-checked steps; let users pin exact brand hexes onto the nearest step.
- **Evidence:** M3; [S-L09-116, 170, 223, 413, 459, 547, 563, 652]

### DC-L09-04: Density and base size
- **Block path:** Foundations > Typography + Space > Density preset
- **Questions the designer answers:** Who uses the product and for how long? Mouse or touch? Data tables or content?
- **Options:** dense 13-14px body, 32px controls (Polaris 13, SLDS 13, Ant 14/32, Carbon 14, Atlassian 14, Primer 14/32) / regular 16px body, 36-40px controls (Radix, shadcn, Chakra, Mantine) / large 17pt+ body or 44-48px targets (iOS, GOV.UK 19px, USWDS 48px targets). Global scale controls: Radix `scaling` 0.9-1.1, Mantine `--mantine-scale`, Ant `compactAlgorithm`, Spectrum desktop vs mobile (~x1.2), Primer pointer fine/coarse.
- **Visual effect:** dense looks professional and information-rich; regular looks balanced; large looks calm, accessible and touch-first.
- **Depends on (upstream):** audience, platform, content type.
- **Affects (downstream):** type scale, spacing, control heights, table row heights, icon sizes, hit targets.
- **Token encoding:** a mode on a `density` collection that swaps `size.control.md` (32 / 40 / 48) and `font.body.size` (14 / 16 / 17); or one multiplier token.
- **Platform notes:** iOS default hit target 44pt [S-L09-145]; Fluent asks for 44 (web, iOS) and 48 (Android) [S-L09-190]; Vercel's guidelines set 24px minimum, 44px on mobile [S-L09-626]; WCAG 2.2 SC 2.5.8 sets 24x24 CSS px [inferred: not re-fetched in this lane].
- **Accessibility constraints:** dense modes must still meet target size minimums (use invisible hit areas).
- **Default + heuristic:** 14px / 32px for B2B tools, 16px / 40px for everything else; offer a density mode rather than two systems.
- **Evidence:** M4, M9; [S-L09-303, 237, 403, 559, 644, 221, 325, 140, 507, 540]

### DC-L09-05: Typeface posture
- **Block path:** Foundations > Typography > Typeface
- **Questions the designer answers:** Platform font, neutral open font, or your own? Do you need a mono and a display face?
- **Options:** system stack (Apple, Fluent, Ant, Radix, Mantine, SLDS) / open neutral (Inter: Polaris, Chakra, Paste, Linear; Roboto: Material) / open custom face (IBM Plex, Geist, Public Sans, Mona Sans) / proprietary brand face (Uber Move, Adobe Clean, Cereal, Spotify Mix, GDS Transport, Pin Sans).
- **Visual effect:** system = native and invisible; Inter = the neutral SaaS look; custom = instant recognition (the largest single brand lever after color, per the Y-axis scores in A3 [inferred]).
- **Depends on (upstream):** brand assets, licensing, performance budget, script coverage.
- **Affects (downstream):** type scale (normalize by cap height when swapping faces, as USWDS does), line heights, tracking, numeric tabular figures.
- **Token encoding:** `$type: fontFamily`; `font.family.sans`, `font.family.mono`, `font.family.display`.
- **Platform notes:** Apple's SF is system-only; custom fonts on native need bundling; GOV.UK restricts its face to its own domains.
- **Accessibility constraints:** x-height and open apertures for legibility (Cereal's stated goals) [S-L09-478].
- **Default + heuristic:** Inter or the system stack for a neutral start; move to a custom face only when brand recognition matters more than neutrality.
- **Evidence:** M4; [S-L09-213, 247, 327, 431, 473, 478, 510, 539, 625]

### DC-L09-06: Motion model
- **Block path:** Foundations > Motion
- **Questions the designer answers:** Should motion be quick and invisible or physical and playful? Springs or curves? One mode or two?
- **Options:** none (GOV.UK) / bezier ladder (Fluent 8 durations 50-500 + 9 curves; Carbon 6 durations 70-700) / productive vs expressive modes (Carbon curves; Material Standard vs Expressive spring schemes) / springs as tokens (Material damping + stiffness; Apple duration + bounce 0/0.15/0.3; Airbnb stiffness/damping/mass + CSS `linear()`) / named presets (Blade Fade, Slide, Scale, Stagger).
- **Visual effect:** short beziers feel efficient; springs with bounce feel alive and tactile; no motion feels static but calm.
- **Depends on (upstream):** personality (X axis in A3); platform (springs are native on iOS and Compose).
- **Affects (downstream):** overlays, sheets, toasts, navigation transitions, state changes, loading.
- **Token encoding:** `$type: duration` and `$type: cubicBezier` (DTCG); springs have no DTCG type yet, so encode as a composite (stiffness, damping, mass) plus a generated CSS `linear()` fallback, as Airbnb does [S-L09-482].
- **Platform notes:** web springs need `linear()` or JS; SwiftUI and Compose take spring parameters natively.
- **Accessibility constraints:** honor prefers-reduced-motion: replace moves with fades, avoid animating blur and depth (Apple) [S-L09-145].
- **Default + heuristic:** 7 durations 50-500ms, ease-out enter, ease-in exit, plus an optional "expressive" mode that swaps in springs for spatial moves only (Material keeps color and opacity changes non-bouncy) [S-L09-106].
- **Evidence:** M8; [S-L09-105, 106, 155, 175, 210, 448, 482]

### DC-L09-07: Brand posture and theming openness
- **Block path:** Theming > Brands and modes
- **Questions the designer answers:** Will other brands, products or customers re-skin this system? Which layers may they change?
- **Options:** locked single brand (Carbon, Primer, Geist) / one brand color in, full theme out (Fluent 16-step ramp, Blade `createTheme({brandColor})`, Ant seed, Material seed) / named-element overrides (Paste `CustomizationProvider`) / two themes on one structure (SLDS Cosmos + Lightning Blue) / scoped color sets (Encore) / theme parts loaded separately (Atlassian color, spacing, type, shape, motion).
- **Visual effect:** locked systems look consistent; generator systems look consistent in structure but vary in hue; theme-swap systems can change shape and depth too.
- **Depends on (upstream):** token tiers (need a semantic tier at least; a foundation tier like Uber's primaryA/primaryB makes rebranding cheap) [S-L09-433].
- **Affects (downstream):** token architecture, Figma modes and collections, documentation, testing matrix (every theme x mode).
- **Token encoding:** modes per theme on the semantic tier; component tokens only where themes differ in shape (SLDS shared hooks such as `--slds-s-button-radius-border`) [S-L09-237].
- **Platform notes:** Figma extended collections support per-brand overrides (L00 topic c).
- **Accessibility constraints:** every generated theme must re-pass contrast; Blade and Encore check or guarantee it in the generator [S-L09-459, 472].
- **Default + heuristic:** build every system as if a second brand will come: semantic tier + brand-color generator + contrast check, even if only one brand ships.
- **Evidence:** M9; [S-L09-170, 237, 247, 359, 413, 459, 470]

### DC-L09-08: Distribution model
- **Block path:** Delivery > Packaging
- **Questions the designer answers:** How will engineers consume the system? Who owns component code after install?
- **Options:** npm component library (Carbon, Fluent, Ant, Chakra, Mantine) / copy-in source via CLI and registry (shadcn) / CDN runtime with stable channel and frozen versions (Polaris 1.x) / CSS + HTML macros (GOV.UK, USWDS) / headless primitives (Radix, Fluent headless preview, Base UI under shadcn) / utilities (Tailwind) / one API for web + native (Blade).
- **Visual effect:** indirect: copy-in source drifts per product; CDN runtimes stay uniform; headless layers leave the look entirely to the user.
- **Depends on (upstream):** team model, framework mix (zeroheight 2026: React 72%, Web Components 36%) [S-L09-005].
- **Affects (downstream):** versioning, theming mechanics, lint and codemod strategy, agent tooling (MCP registries).
- **Token encoding:** export targets: CSS variables, Tailwind `@theme`, shadcn variable contract, DTCG JSON, Figma variables.
- **Platform notes:** web components work across frameworks (Polaris, Carbon, Fluent v3, USWDS Elements) [S-L09-313, 200, 183, 542].
- **Accessibility constraints:** headless primitives carry keyboard and ARIA behavior; styled copies must not break it.
- **Default + heuristic:** generate tokens in DTCG JSON first, then emit CSS variables, Tailwind `@theme` and the shadcn contract, because those are where generated systems land today [S-L09-587, 609].
- **Evidence:** M1; [S-L09-199, 313, 461, 542, 558, 584, 589, 609]

## V. Verification pass

A fresh-context verifier (no access to the workers' reasoning) re-checked 32 high-risk claims against live primary sources: npm release data, the systems' repos and token files, Apple's HIG JSON, official blogs. Full table with evidence: rows S-L09-700 to S-L09-766 in the trace.

| Result | Claims |
|---|---|
| Confirmed as written (28) | Tailwind joining Shopify (2026-09-09), 4.3.3, v4.0 date, radius and spacing values; Apple OS 27 release (2026-09-14), "Designing for iPhone Duo" page, iOS type sizes, systemBlue (0,136,255); Material Compose-first and maintenance-mode READMEs, M3 spring values (0.9/700, 0.8/380), Expressive corner tokens (20/32/48dp); Polaris React deprecated + archived, web components stable 2025-10-01; Paste docs retired, 21.5.0; GOV.UK 6.0.0 and 6.5.1 dates, 19px/25px body at all sizes; shadcn Base UI default (2026-07-02), CLI 4.21.0, radius 0.625rem; Mantine 9.0.0 and radius 4 -> 8px; antd 6.0.0, 6.6.5 and seed values; SLDS Cosmos radii 4/8/12/20; Carbon 1.116.0, spacing-13 = 160px, 70ms/700ms; Primer Mona Sans VF in 11.6.0, React 38.40.0, ViewComponents maintenance; Atlassian tokens 19.0.0, 8.0.0 default-theme change, space.100 = 8px; Fluent web components 3.0.0, react-components 9.74.8, brandWeb[80] #0f6cbd, 4px, 200ms; React Spectrum S2 1.0.0 date, tokens 15.4.1; Radix versions and space scale; Chakra, Gestalt, Base Web, Blade, USWDS versions; Blade fonts; Geist Pixel in 1.7.0 (OFL); both Linear posts; Spotify Mix date; Airbnb spring tokens and Rausch #FF385C in live CSS; Material Figma kit (via Material's own posts); zeroheight 2026 sample (147) and token-layer shares [S-L09-700 to 764] |
| Corrected (3) | (1) Apple: 44x44 pt is the iOS **default** hit target; the **minimum** is 28x28 pt [S-L09-714]. (2) SLDS 2: 2.264.0 (2026-07-21) is the first stable of the Winter '27 line, not the package's first stable; 1.0.0 shipped 2026-04-07 and 2.0.0 on 2026-04-08 [S-L09-732, 733]. (3) USWDS: GSA code is CC0, but bundled fonts are OFL-1.1 and icons Apache-2.0 [S-L09-745]. All three are fixed in this file and in the teardowns. |
| Needed a tie-break (1) | "Atlassian Sans is a derivative of Inter": the verifier found no mention on the pages it opened. The lead then found the literal sentence "Atlassian Sans is our derivative of Inter Variable" on Atlassian's own post, so the claim stands [S-L09-006]. |

**Reconciled with the community pulse (`sources/COMMUNITY-SIGNAL.md`, L00):**
- L00 flagged the Google I/O 2026 claims (Expressive layout, spacing system, "Compose-first") as unverified because it could only see a search snippet. L09 read the blog post in a browser and the Android Developers post, and the verifier confirmed the maintenance-mode READMEs, so these claims are now confirmed [S-L09-121, 127, 716, 717, 718].
- L00 notes that no stable Compose Material3 release ships the full M3 Expressive API without opt-ins; the Expressive APIs are graduating only in the 1.5.0 alphas [S-L00-047]. The Material teardown agrees (1.4.0 stable, 1.5.0-alpha28; the latest alpha is now 1.5.0-alpha29, 2026-09-23 [S-V1b-035]) [S-L09-119]. A builder should treat Expressive as preview on Android and absent on web.
- L00 confirms Liquid Glass changed twice after launch (a Clear/Tinted option in iOS 26.1, now confirmed by Apple [S-V1b-021], a transparency slider in iOS 27) and records user reports that heavy glass costs performance [S-L00-018, S-L00-019, S-L00-048]. This supports treating glass as an optional material with a Reduce Transparency fallback, not a default depth model.
- L00 confirms shadcn's "Base UI as the default" and notes a new `shadcn lint` (September 2026) that flags off-system styles [S-L00-050, S-L00-051]. That fits A3: the toolkit corner is crowded, and enforcement against drift is now part of the offer.
- L00 could not find the zeroheight sample size; the L09 verifier found "we heard from 147 design system practitioners" on report.zeroheight.com [S-L09-764]. L00 warns that WebFetch summaries can invent dates; the three survey figures used here were re-read from the page, not from a summary [S-L09-764].
- No L09 claim relies on a source L00 lists as disputed or to avoid.

## Sources

564 rows in `traces/L09-trace.md` (ids S-L09-001 to S-L09-766, with gaps between worker ranges): 491 used, 73 rejected. About 90% are Tier A: official docs sites, official GitHub repos and token files, npm registry metadata, official blogs and newsrooms. Tier B: zeroheight report, component.gallery, Wayback captures of Spotify and Airbnb design blogs. Tier C (used only as opinion or history): a handful, labelled in the trace.

Main rejection reasons: JavaScript-only docs pages that returned empty (Material, Atlassian, SLDS, Spectrum, ant.design), Figma Community pages returning HTTP 403, developer.salesforce.com returning 403, GitHub API rate limits, a third-party claim that Chakra v4 is a Tailwind rewrite (contradicts the official discussion), the paste-dsys.com fork (unaffiliated), Medium returning 403, and the Perplexity API (quota exhausted) and WebSearch (session budget of 200 used up) for late lookups.

## Cross-lane notes

(Per instructions this lane does not edit `_coordination/BOARD.md`; the orchestrator can copy these lines there.)

- [L09 -> L01] Color: 12-step "job per step" ramps are shared by Radix and Geist (steps 1-3 backgrounds, 4-6 borders, 7-8 solids, 9-10 text), and step numbers carry meaning [S-L09-563, 616]. Apple ships 4 values per system color (light, dark, increased-contrast light and dark) [S-L09-142]. USWDS "magic number": grade difference 40+ = AA large, 50+ = AA, 70+ = AAA [S-L09-547]. Ant's default #1677ff with white text is 4.1:1, below AA [S-L09-460]. Tailwind now has 26 families (mauve, olive, mist, taupe added in 4.2) [S-L09-607]. Material color utilities added 2025 and 2026 spec versions and "Dim" roles [S-L09-112, 114].
- [L09 -> L02] Type: GOV.UK v6 body is 19px/25px at every size and size 14 was removed [S-L09-502, 727]. Carbon's size formula and Ant's 14 x e^(i/5) are the only generated scales [S-L09-213, 407]. USWDS normalizes sizes by cap height when swapping fonts [S-L09-539]. Gestalt ships per-script line-height sets (tall, CJK, Thai, Vietnamese) [S-L09-370]. Apple added emphasized weights to Dynamic Type on 2025-12-16 [S-L09-140]. Primer made Mona Sans VF primary on 2026-03-25 [S-L09-327]. Spotify Mix (2024) and Geist Pixel (2026-02-06) are new faces [S-L09-473, 625].
- [L09 -> L03] Space and density: 17 of 22 published spacing scales contain 4-8-12-16-24-32-40-48-64 (M5). Density mechanisms to model: Radix `scaling` 0.9-1.1, Mantine `--mantine-scale`, Ant `compactAlgorithm`, Spectrum desktop vs mobile token sets (~x1.2), Primer pointer fine/coarse, Encore device-class token values [S-L09-559, 644, 411, 221, 325, 470].
- [L09 -> L04] Shape and motion: Material spring values confirmed (Standard spatial 0.9/700, Expressive 0.8/380) and Expressive corners 20/32/48dp [S-L09-719]. Airbnb ships 6 springs as tokens with physics and precomputed CSS `linear()`; Atlassian ships a spring as `linear()` [S-L09-482, 247]. Carbon v12 adds radius tokens 0/2/4/8/16/24/max and moves inputs and tags to 4px [S-L09-201, 203]. Spectrum uses size-dependent radius; Apple uses concentric radius; Chakra uses layer radii [S-L09-221, 158, 632]. Geist and Airbnb bundle radius + ring + shadow into "materials" [S-L09-620, 482].
- [L09 -> L05] Icons: Atlassian's new icons use a 1.5px stroke on a 16px canvas (legacy 2px on 24px) [S-L09-252]; Spotify moved 24px icons from 1px to 2px stroke and cut 5 sizes to 2 [S-L09-474]; Spectrum 2 icons blend S1 rationality with Express's rounder style [S-L09-228].
- [L09 -> L06] Brand: in the personality map, typeface and one fixed accent drive the "brand-led" score far more than radius or motion; no brand-led system scores above 6 of 10 on expressiveness (A3) [inferred].
- [L09 -> L07] Tokens: tier counts per system are in M2 (11 systems with 2 tiers, 9 with 3, 3 with 4). Carbon (2026) and Primer (11.5.0, 2026-02-24) moved token sources to W3C DTCG JSON; Spectrum publishes a normative Design Data Specification [S-L09-210, 327, 233]. SLDS's r/g/s/c hook grammar and Polaris's "number / 25 = px" rule are compact naming presets [S-L09-237, 303]. Figma variables confirmed for Fluent, Carbon (color), Polaris, Primer, Paste, Chakra; unconfirmed for Material, Spectrum, SLDS, Atlassian, USWDS.
- [L09 -> L08] Components: counts and doc-page skeletons are in M10 (median 64). Polaris React is archived; Polaris is 50 App Home web components [S-L09-304, 312]. shadcn's default primitive layer is Base UI since 2026-07-02, with React Aria as a third option [S-L09-584, 585]. Fluent published headless React primitives (preview) on 2026-04-27 [S-L09-199].
- [L09 -> L10] Platforms: Material Android is Compose-first; Material Web and MDC-Android are in maintenance mode; spacing tokens are Compose-only [S-L09-122, 128, 129, 716]. Apple's 27 releases shipped 2026-09-14 with a "Designing for iPhone Duo" (folding iPhone) page [S-L09-164, 707]. Blade renders one React API on web and React Native [S-L09-461]. Fluent keeps per-platform type ramps under shared names [S-L09-185].
- [L09 -> L11] Governance and lifecycle: Paste's docs site retired (2026-07-31) while code lives on in GitHub; Polaris React archived; Gestalt's public releases stopped Dec 2025 with new docs behind a login; Radix went 10 months without a release; Tailwind Labs joined Shopify [S-L09-349, 304, 361, 556, 606]. Adoption tooling: Uber's view-tree adoption counter and SLDS Linter as the main migration path [S-L09-440, 240]. Release phases (Atlassian Early Access / Beta / GA) and experiment-flag rollouts (Gestalt, Atlassian) [S-L09-254, 370]. 12 of 25 systems ship MCP servers or agent-readable docs (A1 item 10).
- [L09 -> L00] Disputes found inside official sources: Gestalt states WCAG 2.2 AA on one page and 2.1 AA on another [S-L09-363, 372]; USWDS says WCAG 2.0 AA on its designers page and a 2.1 AA target on its accessibility page [S-L09-546]; Fluent's shapes page (Large 8px) disagrees with its code tokens (Large 6px) [S-L09-191, 171]; Paste's official repo homepage field points to an unaffiliated fork [S-L09-347, 350].

## Open questions / gaps

- **Not public:** Encore, Airbnb DLS and Linear publish no docs. Their values come from shipped web CSS (labelled "observed") and old blog posts read through the Wayback Machine. Native app values may differ.
- **Behind logins or blocked:** Gestalt 2.0 docs (login), base.uber.com page bodies (zeroheight API refused anonymous access), SLDS 2 docs bodies (JavaScript only), developer.salesforce.com (403), Figma Community pages (403). So SLDS 2 beta and GA dates, Gestalt's current default theme and Uber Base 2.0 color and type values are unknown.
- **Figma variables** are unconfirmed for Material, Spectrum, SLDS, Atlassian, USWDS and Gestalt.
- **Reduced-motion policy** is unverified for Material, SLDS, Polaris and Uber Base.
- **Component counts** use different counting rules (doc pages, package exports, nav entries); each row states its method, but cross-system comparison is approximate.
- **Personality scores** are my application of a stated rubric to matrix values [inferred]. Apple's radius score is inferred because Apple publishes no radius scale; Linear is placed only approximately.
- **Search coverage:** the WebSearch budget and the Perplexity quota ran out mid-session, so late checks relied on source code, npm and archives. Tier B commentary on 2026 changes (for example, why Twilio retired the Paste site) was not found.
- **Not covered:** Workday Canvas, Elastic EUI, NYPL Reservoir, Wise, Monzo and other public systems (component.gallery lists 100+) [S-L09-001].

## Confidence

- **High (Tier A and independently re-verified):** all version numbers and release dates in M1; the recent-change list in the overview; Material spring and corner values; Apple type sizes, colors and hit targets; Tailwind, Radix, Fluent, Carbon, Ant, Mantine, GOV.UK core values; the zeroheight token-layer figures [S-L09-700 to 764].
- **High (Tier A, single pass):** the remaining token values in M2-M9, read from each system's own token files or docs. They were not all re-verified, but they come from primary sources. In the 32-claim sample, 28 held exactly; the 3 corrections were a mislabel (Apple default vs minimum hit target), an overstated "first stable" (SLDS 2) and an incomplete license (USWDS). No numeric token value in the sample was wrong.
- **Medium:** values for Encore, Airbnb and Linear (observed from production web CSS, not documented); component counts (method-dependent); semantic-role counts marked "approx." or "[inferred count]".
- **Inferred (labelled in place):** every "Pattern" paragraph's counts, the A2 ordering, the A3 scores and map, and the "builder default" column in A1.
