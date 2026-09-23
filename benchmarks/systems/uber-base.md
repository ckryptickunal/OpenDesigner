# Uber Base (Base design system + Base Web)

_Lane L09 teardown. Verified against live sources on 2026-09-23. Every value carries an [S-L09-xxx] id from `traces/L09-trace.md` or the tag [inferred]._

Two things share the name. **Base** is Uber's internal, cross-platform design system, documented publicly at base.uber.com (a zeroheight site). **Base Web** (`baseui` on npm, github.com/uber/baseweb) is the open-source React implementation. Values below come from Base Web source unless marked "Base (internal)".

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Owner | Uber Technologies. Base design team (internal) and the Base Web maintainers | [S-L09-440] [S-L09-428] |
| Launch and major versions | Base Web repo created 2018-03-09. `baseui` 1.0 2018-08-20. Majors: 9.0 2019-09, 10.0 2021-07, 11.0 2022-04, 12.0 2022-07, 13.0 2023-06, 14.0 2023-12, 15.0 2024-12-27, 16.0 2026-01-06. 17.x and 18.0.0 were never published to npm. Base (internal) docs now include "About Base 2.0", "Color 2.0" and "Typography 2.0" | [S-L09-428] [S-L09-427] [S-L09-436] |
| Current version (Sept 2026) | `baseui` 18.2.0, 2026-07-02. Canary `0.0.0-next-*` builds as recent as 2026-09-04. base.uber.com default release "9.14.26", created 2026-09-14 | [S-L09-427] [S-L09-436] |
| Platforms | Base (internal): iOS, Android, web. The docs cover VoiceOver, TalkBack and Haptics. Base Web: web only (Chrome >= 89, Safari >= 15, Firefox ESR, Edge >= 89) | [S-L09-440] [S-L09-436] [S-L09-484] |
| Open source + license | Base Web: yes, MIT. Base (internal) native libraries: not open source | [S-L09-427] [S-L09-428] |
| Code frameworks | Base Web: React (peer react >= 18) plus the Styletron CSS-in-JS engine (peer `styletron-react` >= 6). Styling is customized through the `overrides` API. Internal native frameworks: not public | [S-L09-427] [S-L09-484] |
| Figma kit | "Base Gallery" on the Figma Community (@uber). Published 2020-02-13 as a duplicate-only file; the library itself is not published. Variables: not verified (Figma returned 403) | [S-L09-443] [S-L09-441] |
| Token tiers + naming | Color has 4 tiers: primitive (`gray50`, `blue600`), then foundation (`primaryA` #000, `primaryB` #fff, `accent`), then semantic (`backgroundPrimary`, `contentSecondary`, `borderOpaque`), then component tokens. Non-color tokens use a numeric-step grammar: `scale600`, `radius300`, `shadow500`, `timing200`, `font350` | [S-L09-432] [S-L09-433] [S-L09-430] |
| Color model | sRGB hex. Primitive hues run in 10 steps 50-900: blue, green, red, yellow, orange, purple, magenta, teal, lime, amber, plus gray50-900 and separate `*Dark` twins. brown, cobalt and platinum are deprecated. Monochrome foundation: primaryA #000000 on primaryB #FFFFFF. Accent blue600 #276EF1. About 164 semantic entries in the light theme. Hand-picked, not generated | [S-L09-432] [S-L09-433] |
| Typeface | Uber Move (display), Uber Move Text (UI) and Uber Move Mono. Proprietary. Made for the 2018 rebrand by MCKL (Jeremy Mickel) with Wolff Olins. Fallbacks: system-ui, Helvetica Neue, Arial | [S-L09-431] [S-L09-436] [S-L09-439] |
| Type scale | 18 named styles, plus 18 Mono twins. Groups: Paragraph XS-L (12/20, 14/20, 16/24, 18/28, weight 400), Label XS-L (12/16 to 18/24, weight 500), Heading XS-XXL (20/28 to 40/52, weight 700), Display XS-L (36/44, 44/52, 52/64, 96/112, weight 700). Hand-tuned on a 4px line-height grid. Base body = ParagraphMedium 16/24 | [S-L09-431] |
| Spacing | `sizing` scale in px: scale0 2, 100 4, 200 6, 300 8, 400 10, 500 12, 550 14, 600 16, 650 18, 700 20, 750 22, 800 24, 850 28, 900 32, 950 36, 1000 40, 1200 48, 1400 56, 1600 64, 2400 96, 3200 128, 4800 192. Grid: 4/8/12 columns, gutters 16/36/36, margins 16/36/64, max width 1280 | [S-L09-430] |
| Radius | radius100 2, radius200 4, radius300 8, radius400 12, radius500 16. Component radii: button 8 (mini 4), input 8 (mini 4), popover 8, tag 24, checkbox 0, surface (card, modal, toast) 0 | [S-L09-430] |
| Elevation | Shadows plus inset overlays. shadow400 `0 1px 4px`, 500 `0 2px 8px`, 600 `0 4px 16px`, 700 `0 8px 24px`, all hsla(0,0%,0%,.16). Also shallowAbove/Below (`0 ±4px 16px`, .12) and deepAbove/Below (`0 ±16px 48px`, .22). overlay100-600 = inset black at 4-24% for pressed states. Borders border100-600 = 1px black at 4-24% alpha | [S-L09-430] |
| Motion | Durations timing0, 100-1000 ms in 100 ms steps (plus 150, 250), then 1500, 3000, 5000, 7000. 5 semantic easings: easeLinear (0,0,1,1); easeDecelerate (0.22,1,0.36,1) for entering; easeAccelerate (0.64,0,0.78,0) for exiting; easeAccelerateDecelerate (0.83,0,0.17,1) as the default; easeResponsiveAccelerate (0.11,0,0.5,0). The Base (internal) Timing page says "five main easing curves". No springs. No `prefers-reduced-motion` handling found in Base Web | [S-L09-430] [S-L09-438] [S-L09-444] |
| Theming + modes | Light and dark (`LightTheme`, `DarkTheme`), plus Move variants (`LightThemeMove`, `DarkThemeMove`). Build your own with `createLightTheme` / `createDarkTheme`. Switched by passing a theme to `BaseProvider`. No density or high-contrast mode in Base Web | [S-L09-445] |
| Component count | Base Web docs nav, 2026-09-23: 89 entries in 10 groups, 79 without the 10 utilities. Includes v2 duplicates (Checkbox-v2, Radio-v2) and map markers. Base (internal) nav lists about 70 components plus a Maps section | [S-L09-434] [S-L09-436] [inferred: internal count from nav names] |
| Component doc structure | Base Web: interactive "Yard" playground, examples, overrides reference, API cheat sheet. Base (internal) pages include Overview, Specs and "Status & changelog" tabs | [S-L09-434] [S-L09-438] [inferred: Base Web page sections from docs source] |
| Accessibility stance | Base (internal): an "A11y first process" plus pages on disability, VoiceOver, TalkBack, text resizing and screen readers. Base Web: an A11y Validator utility; 0 mentions of WCAG in the repo. No conformance level published | [S-L09-436] [S-L09-434] [S-L09-485] |
| Governance / contribution | Base Web: GitHub PRs, CODEOWNERS, SemVer, one planned major a year "around September", codemods for each major. Internal changes sync into the repo through UberOpenSourceBot. Base (internal): a "Playbook" of adoption steps and an extension library | [S-L09-484] [S-L09-428] [S-L09-436] |
| Notable innovation | Design System Observability: "Base Counter" walks native view trees to flag Base vs custom components, backed by daily automated screenshot analysis. Uber claims 3X faster development, 4X fewer visual parity issues and 50% less code. Base (internal) now ships "Base MCP" and "Base skills" pages for AI tooling | [S-L09-440] [S-L09-436] |

## Visual signature: why it looks like this
- Foundation primaryA #000 on primaryB #fff, with blue #276EF1 kept for accent only -> the stark black-and-white Uber look. Color barely appears on surfaces [S-L09-433].
- Uber Move headings at weight 700 over Uber Move Text 400/500 -> geometric but warm type. The quirky lowercase a and its links to transit lettering give Uber its own voice [S-L09-431] [S-L09-439].
- Surface radius 0 (cards, modals, toasts) against 8px controls and 24px tags -> rectangular panels with softer touch targets [S-L09-430].
- Neutral grays (#F3F3F3 to #282828) and alpha-black borders -> no warm or cool tint, so the palette reads engineered [S-L09-432] [S-L09-430].
- One shadow alpha (.16) across four blur sizes (4-24px) -> low-drama depth that looks the same at every level [S-L09-430].
- Quintic-style curves (0.22,1,0.36,1) -> fast starts and long settles; motion feels decisive, not bouncy [S-L09-430].

## Recent changes 2024-2026
- 2024-09-24: Uber Engineering publishes the Design System Observability post covering Base on iOS and Android [S-L09-440].
- 2024-12-27: `baseui` 15.0.0. Then no release for about a year, until 15.0.1 on 2025-12-11 [S-L09-427].
- 2026-01-06/07: v16.0.0 and the blog post "Base Web v16 Released". It calls itself the first update "after more than a year", refreshes Button, Button Group and Tag, adds Tag Group, and says the team remains "committed to maintaining the external codebase" [S-L09-429].
- 2026-02 to 2026-07: new Checkbox-v2, Switch, Radio-v2 and SlidingButton components. Publishing moved to npm trusted publishing (OIDC). Releases 16.1.x, then 18.1.0 (2026-06-08) and 18.2.0 (2026-07-02) [S-L09-428] [S-L09-427].
- 2026-09: the repo is still active (45 commits since 2025-09-01, last push 2026-09-22). Verdict: maintained at low cadence, not archived [S-L09-428].
- 2026-09-14: base.uber.com republished as release "9.14.26", with Base 2.0 color and typography pages alongside 1.0, plus Base AI / MCP / skills pages [S-L09-436].

## Builder takeaways
- Offer a "monochrome + one accent" preset: primaryA/primaryB foundation tokens with a single accent ramp. It is a distinct, very legible brand strategy [S-L09-433].
- Copy the 4-tier color model (primitive, foundation, semantic, component). The small foundation tier (primaryA/B, accent, negative, warning, positive) is where rebranding happens [S-L09-433].
- Let users choose radius per component family (controls, popovers, surfaces, tags) as well as a global scale. Base proves a 0px-surface / 8px-control split works [S-L09-430].
- Ask whether the system needs adoption metrics. Base's view-tree counter is a feature a builder could generate: a "coverage" lint [S-L09-440].

## Gaps / unverified
- base.uber.com page bodies are loaded from zeroheight's API. It refused anonymous requests (401/400) and marked pages as password-protected. Only the navigation JSON and search snippets were readable. Base 2.0 color and type values are therefore not public to us.
- Internal Base native tokens (iOS/Android) and any differences from Base Web are not public.
- Figma Base Gallery details (last update, variables) were blocked (403).
- Uber Move designer credit comes from a Tier C source only.
- GitHub releases stop at v13.0.0 (2023). Later versions were checked only through npm and commits.
