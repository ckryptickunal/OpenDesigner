# IBM Carbon Design System

_Lane L09 teardown. Verified against live sources on 2026-09-23. Every value carries an [S-L09-xxx] id from `traces/L09-trace.md` or the tag [inferred]._

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Owner | IBM (Carbon Design System team; repo `carbon-design-system/carbon`) | [S-L09-218] |
| Launch and major versions | GitHub monorepo created 2017-03-13; `carbon-components` on npm 2017-03-23; v10 2019-03-29; v11 2022-03-31 (`@carbon/react` 1.0.0 and `carbon-components` 11.0.0 same day); v12 in development behind the `enable-v12-release` flag (off by default), no release date published | [S-L09-218] [S-L09-217] [S-L09-204] [S-L09-207] |
| Current version (Sept 2026) | v11 (site still labels v11 current). `@carbon/react` 1.116.0 (2026-09-09), `@carbon/web-components` 2.63.0 (2026-09-09), `@carbon/styles` 1.115.0 (2026-09-09), `@carbon/layout` 11.59.0 | [S-L09-200] [S-L09-201] [S-L09-206] |
| Platforms | Web only (React + Web Components). Other frameworks listed only as "community frameworks" | [S-L09-219] |
| Open source + license | Yes. Apache-2.0 | [S-L09-218] [S-L09-217] |
| Code frameworks | React (`@carbon/react`), Web Components (`@carbon/web-components`), Sass (`@carbon/styles`), plus token packages (`@carbon/colors`, `themes`, `type`, `layout`, `motion`) | [S-L09-200] [S-L09-213] |
| Figma kit | Official "(v11) Carbon Design System" library (all 4 themes), "(v11) Carbon Type Sets", IBM Color / UI Icon / Pictogram libraries. Color tokens are Figma variables | [S-L09-219] |
| Token tiers + naming | 3 tiers. Palette: `blue-60`, `gray-100`. Theme (semantic, `$`-prefixed Sass / CSS vars): `$background`, `$layer-01`, `$interactive`, `$text-primary`, `$border-subtle-01`. Component tokens live in `themes/src/dtcg/components`. Non-color: `$spacing-05`, `$duration-fast-01`. Colors, layout and motion moved to DTCG JSON as source of truth in 2026 | [S-L09-211] [S-L09-212] [S-L09-201] [S-L09-210] |
| Color model | 12 families x 10 steps (10-100) plus a hover value for every step (yellow, orange, red, magenta, purple, blue, cyan, teal, green, cool gray, gray, warm gray). sRGB hex. 234 theme color tokens (88 syntax, 21 AI, 21 chat, 104 core). Accent is fixed IBM Blue: `$interactive` = blue-60 #0f62fe (white/g10), blue-50 #4589ff (g90/g100). Not generated | [S-L09-211] [S-L09-212] |
| Typeface | IBM Plex Sans (UI), IBM Plex Mono (code), IBM Plex Serif, Plex Sans Condensed, Plex Sans Hebrew. Custom, open-source IBM family; fallback `system-ui` | [S-L09-213] |
| Type scale | 23-step size scale 12-156px from formula Yn = Yn-1 + (floor((n-2)/4)+1) x 2. 58 exported style objects (incl. v10 aliases and fluid styles). `body-01` 14px / 1.42857 (20px) / 0.16px; `body-compact-01` 14px / 1.28572; `label-01` 12px / 16px / 0.32px; `heading-01` 14px semibold; `heading-07` 54px light; `display-04` 42px fluid up to 92px (lg). Weights 300 / 400 / 600. Productive vs expressive sets | [S-L09-213] |
| Spacing | 8px mini-unit. `$spacing-01..13` = 2, 4, 8, 12, 16, 24, 32, 40, 48, 64, 80, 96, 160px. Fluid spacing 0 / 2vw / 5vw / 10vw. Component sizes xs-2xl = 24, 32, 40, 48, 64, 80px (40px default). Icons 16 / 20px | [S-L09-201] |
| Radius | v11: buttons 0 (`$button-border-radius: 0`), tags pill (16px). New tokens (shipped in `@carbon/layout` 11.59.0): `border-radius-00/02/04/08/16/24/max` = 0, 2, 4, 8, 16, 24, 999999px. Under the v12 flag: inputs and tags 4px, menus/popovers/tooltips rounded, progress bar max; pill buttons proposed in open PR #23259 | [S-L09-201] [S-L09-258] [S-L09-203] [S-L09-205] [S-L09-259] |
| Elevation | Tonal layering, not shadows: `$layer-01..03` alternate against `$background` (white theme: background white, layer-01 gray-10 #f4f4f4). One shadow for floating UI: `0 2px 6px $shadow` (black at 0.3 alpha light, 0.8 dark). Overlay black 0.6 | [S-L09-212] [S-L09-214] |
| Motion | Durations fast-01 70, fast-02 110, moderate-01 150, moderate-02 240, slow-01 400, slow-02 700ms. Easing: standard productive (0.2,0,0.38,0.9) / expressive (0.4,0.14,0.3,1); entrance productive (0,0,0.38,0.9) / expressive (0,0,0.3,1); exit productive (0.2,0,1,0.9) / expressive (0.4,0.14,1,1). No springs. 2026 "motion surfaces" (disclosure 150ms, contextual 110ms, expand 240ms, invoke 240ms). Reduced motion: surfaces never animate; stylelint rule `a11y/media-prefers-reduced-motion` | [S-L09-210] [S-L09-260] |
| Theming + modes | 4 themes: White, Gray 10 (light), Gray 90, Gray 100 (dark). Switched by Sass `$theme` or the React `Theme` / `Layer` components. No high-contrast theme and no brand re-theming documented [inferred]. Density via component size props (xs-2xl) | [S-L09-219] [S-L09-215] [S-L09-201] |
| Component count | 42 components on the website nav (file updated 2026-02-20). 144 directories in `@carbon/react/src/components` and 99 in web-components (these include utilities, sub-parts and v12 components migrated from IBM Products), counted 2026-09-23 | [S-L09-216] [S-L09-215] |
| Component doc structure | Tabs: Usage, Style, Code, Accessibility | [S-L09-257] |
| Accessibility stance | Follows the IBM Accessibility Checklist, which is based on WCAG AA, Section 508 and European standards; WCAG 2.1 AA contrast cited | [S-L09-219] |
| Governance / contribution | Central IBM team plus open contribution ("anyone can contribute code, design, and documentation"); entry through office hours; Product Development Lifecycle and Component checklist pages. For v12, Carbon for IBM Products contributes 21 core components and 24 complex patterns to core | [S-L09-219] [S-L09-207] |
| Notable innovation | Productive vs expressive modes for both type and motion; contextual layer tokens; Carbon for AI (AI label, "light" metaphor, `ai-aura-*` tokens); Carbon MCP server (public preview); DTCG JSON as token source of truth (2026) | [S-L09-213] [S-L09-210] [S-L09-212] [S-L09-219] |

## Visual signature: why it looks like this
- 0px radius on buttons (v11) + 8px mini-unit and 2x grid (16 columns from 1056px) -> hard-edged, rectilinear, "engineered" look. [S-L09-258] [S-L09-202]
- IBM Plex Sans at 14px with +0.16px tracking, headings up to 54px in Light (300) -> editorial, technical tone rather than friendly SaaS. [S-L09-213]
- Tonal layers (white vs gray-10 #f4f4f4) instead of shadows; one 0 2px 6px shadow only for floating menus -> flat, dense surfaces. [S-L09-212] [S-L09-214]
- True neutral grays (#f4f4f4 ... #161616) + a single saturated accent (blue-60 #0f62fe) -> high-contrast enterprise UI with color used only for action and status. [S-L09-211] [S-L09-212]
- Productive motion at 70-110ms with a fast-out curve -> snappy, almost invisible transitions. [S-L09-210]
- AI moments get their own gradient "aura" tokens -> AI is visually marked, not decorative. [S-L09-212] [S-L09-219]

## Recent changes 2024-2026
- 2024-05-08: last `carbon-components` (v10 line) release, 10.58.15. [S-L09-217]
- 2025-10-14: `@carbon/ai-chat` 1.0.0; 1.21.0 on 2026-09-21. [S-L09-217]
- 2026-02-10: Carbon MCP docs added (public preview; IBMers first, others request access); updated 2026-07-02. [S-L09-219]
- 2026-04-20: `@carbon/layout` migrated to TypeScript. [S-L09-202]
- 2026-07-30: motion tokens moved to DTCG; 2026-09-17 motion-surface API accepts custom surfaces. [S-L09-210]
- 2026-08-12: "Carbon Next" (v12) page last updated: "To guide is to partner", motion for wayfinding, AI-agent-ready docs; no release date given. [S-L09-207]
- 2026-08-13: v12 border-radius tokens added (`chore(v12): setup border-radius tokens`). [S-L09-203]
- 2026-08-25: v12 DatePicker adds a Temporal polyfill. [S-L09-203]
- 2026-08-30: v12 rounded-corner styles for Menu. [S-L09-203]
- 2026-09-02: v12 inputs move to 4px radius with a gradient border; v12 tag styles (tags go from pill to 4px). [S-L09-203] [S-L09-258]
- 2026-09-11: v12 popover, toggletip and tooltip get 4px corners and a new caret. [S-L09-203]
- 2026-09-17: v12 progress bar uses `border-radius-max`; Web Components form elements adopt `ElementInternals`. All behind `enable-v12-release`. [S-L09-203] [S-L09-259]
- Aug-Sept 2026: IBM Products components (Coachmark, Guidebanner, TagOverflow, UserAvatar, BigNumber and more) migrated into core React and Web Components for v12. [S-L09-203]
- 2026-09-10 / 2026-09-15: layout and color tokens published as DTCG JSON. [S-L09-201] [S-L09-211]

## Builder takeaways
- Offer "productive / expressive" as a system-wide switch that drives both type styles and easing curves. Carbon proves one system can hold both.
- Treat radius as a first-class token axis that includes 0. Carbon going from 0px to 4px and pill in v12 shows radius is a brand-era choice. Ask the user for it early.
- Offer contextual layer tokens (layer-01/02/03 that flip per theme) as an alternative to shadow elevation for dense data apps.
- Offer an optional "AI layer" module: an AI label component plus a small set of AI surface tokens.

## Gaps / unverified
- v12 release date: not published; Carbon Next page gives none. [S-L09-207]
- The public releases page did not render through fetch; version support policy not confirmed. [S-L09-208]
- Pill buttons for v12 are an open PR, not merged. [S-L09-205]
- Figma variables confirmed for color only; spacing/type variables not confirmed.
- Component token names were not enumerated; only the folder was confirmed. [S-L09-212]
- The team brief listed `$spacing-13` as 128px; the live token is 160px (10rem). Live source used. [S-L09-201]
- Status mismatch: the Carbon for AI page marks AI chat as "Preview", while `@carbon/ai-chat` is already at 1.21.0 on npm. [S-L09-219] [S-L09-217]
- The rendering library behind `@carbon/web-components` was not checked.
- No official high-contrast theme was found; Windows forced-colors handling was not checked.
