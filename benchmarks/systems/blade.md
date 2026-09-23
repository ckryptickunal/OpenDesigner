# Razorpay Blade

_Lane L09 teardown. Verified against live sources on 2026-09-23. Every value carries an [S-L09-xxx] id from `traces/L09-trace.md` or the tag [inferred]._

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Owner | Razorpay design system team. In Jan 2024: 3 designers and 5 engineers, serving about 70 designers and 100 front-end devs | [S-L09-447] [S-L09-467] |
| Launch and major versions | Repo created 2020-01-28; `@razorpay/blade` 1.0.0 2020-02-05. Majors: 4.0/5.0 2022-11-21, 6.0 2023-01, 7.0 2023-04, 8.0 2023-05, 9.0 2023-07, 10.0 2023-08 (React 18 / RN 0.72), 11.0 2024-01-24 (brand refresh), 12.0 2024-12-11 (Motion Presets) | [S-L09-446] [S-L09-452] |
| Current version (Sept 2026) | `@razorpay/blade` 12.126.0, 2026-09-17. Still v12 after 21 months, with frequent minors | [S-L09-446] [S-L09-452] |
| Platforms | Web (desktop and mobile web) and native iOS/Android through React Native, with the same API. Svelte port in progress | [S-L09-461] [S-L09-467] [S-L09-463] |
| Open source + license | Yes; MIT | [S-L09-446] [S-L09-461] |
| Code frameworks | React (>= 18) and React Native (^0.72) in one package. Built on styled-components ^5, Framer Motion (web) and Reanimated ^3.4 (native). `@razorpay/blade-svelte` 0.17.1 and `blade-core` 0.18.0 are in the repo but not on public npm. `@razorpay/blade-mcp` 1.26.0 is an MCP server for AI coding | [S-L09-446] [S-L09-463] |
| Figma kit | Official "Blade Design System" file on the Figma Community, published about 2024-02-27. Tokens moving to Figma variables (Jan 2024). In-repo Figma plugins: token publisher, Blade coverage linter, dev-handoff checklist widget | [S-L09-465] [S-L09-464] [S-L09-467] [S-L09-461] |
| Token tiers + naming | 2 tiers plus component props. Global tokens: `colors.chromatic.azure[500]`, `spacing[5]`, `border.radius.medium`. Theme (semantic) tokens as dot paths: `surface.background.gray.subtle`, `interactive.background.primary.default`, `feedback.text.negative.intense`. Components take dot-path strings, e.g. `color="surface.text.gray.subtle"`, `padding="spacing.5"` | [S-L09-450] [S-L09-451] [S-L09-457] |
| Color model | HSLA strings. 11 chromatic hues (azure, emerald, crimson, cider, sapphire, sea, cloud, forest, orchid, magenta, topaz), each with 11 solid steps (50, 100-1000) plus 5 alpha steps (a50-a400). Neutrals: blueGray and ashGray, each in light and dark. Brand azure[500] = hsla(218,89%,51%), about #1364F1. Semantic groups: surface, feedback, interactive, overlay, popup, data. About 431 color leaves per mode. `createTheme({brandColor})` generates a brand ramp with tinycolor and checks WCAG contrast | [S-L09-450] [S-L09-451] [S-L09-459] [inferred: hex conversion, leaf count] |
| Typeface | Inter (text), TASA Orbiter (headings; "TASA Orbiter Display" on native), Menlo / monospace (code). Before v11 the font was Lato | [S-L09-449] [S-L09-453] [S-L09-454] |
| Type scale | 14 numeric size tokens (25-1100). Desktop: 10, 11, 12, 14, 16, 18, 20, 24, 32, 40, 48, 56, 64, 72 px. Mobile tops out at 40. Line heights 13-78 px. Letter spacing -3.3%, -1.3% or 0. Weights 400/500/600/700. Base body 14px/20px (size 100 / lineHeight 100). Hand-tuned, with separate desktop and mobile sets | [S-L09-449] |
| Spacing | 12 tokens, spacing.0-11: 0, 2, 4, 8, 12, 16, 20, 24, 32, 40, 48, 56 px. Base 4px with a 2px half-step | [S-L09-448] |
| Radius | none 0, 2xsmall 2, xsmall 4, small 8, medium 12, large 16, xlarge 20, 2xlarge 24, max 9999, round 50%. Border widths: thinner 0.5, thin 1, thick 1.5, thicker 2. Default control radius: Button uses `small` 8px at xsmall/small/medium and `medium` 12px at large. Button min heights: 28/32/36/48 | [S-L09-448] [S-L09-486] |
| Elevation | 3 shadow levels per color mode. onLight: lowRaised `0 2px 4px`, midRaised `0 16px 12px`, highRaised `0 8px 24px -4px`, all hsla(200,10%,18%,.06), a blue-gray tint. onDark: the same offsets at black .32. Plus backdrop blur tokens | [S-L09-449] [S-L09-451] |
| Motion | Durations: 2xquick 80, xquick 160, quick 200, moderate 280, xmoderate 360, gentle 480, xgentle 640, 2xgentle 960 ms. Delays 80 ms to 5000 ms. 7 easings: linear, entrance (0,0,0.2,1), exit (0.17,0,1,1), standard (0.3,0,0.2,1), emphasized (0.5,0,0,1), overshoot (0.5,0,0.3,1.5), shake (1,0.5,0,0.5). No springs. Motion preset components (Fade, Move, Scale, Slide, Stagger, Morph, Elevate, AnimateInteractions). Reduced motion sets durations to 0 | [S-L09-448] [S-L09-456] [S-L09-458] |
| Theming + modes | `colorScheme` light / dark / system through `BladeProvider`. Every semantic token has onLight and onDark values. White-labelling with `createTheme({brandColor})`. Themes: `bladeTheme`, plus `bladeNeutralTheme` (added 2026-07-21). No density mode. Breakpoints: 0/320/480/768/1024/1200 | [S-L09-451] [S-L09-459] [S-L09-447] [S-L09-449] [S-L09-487] |
| Component count | Storybook "Components" group: 71 entries on 2026-09-23. About 66 real components after dropping Accessibility, KitchenSink, Interaction Tests and base primitives [inferred]. Plus 8 motion presets in a separate "Motion" group. Source has 97 component directories | [S-L09-455] [S-L09-456] |
| Component doc structure | Storybook page: title and description, "View on Figma" and code links, Usage (Sandpack sandbox), Imports, Example, Properties (controls table), Stories. Every component folder has `_decisions/decisions.md` API records | [S-L09-457] [S-L09-461] |
| Accessibility stance | Accessibility RFC (2022-04-09) cites WCAG 2.0/2.1 techniques: keyboard, focus order, no tabindex > 0, React Aria primitives. `createTheme` auto-picks readable foreground "as per WCAG 2.0" (AAA large-text threshold). No overall conformance level published | [S-L09-462] [S-L09-459] [S-L09-451] |
| Governance / contribution | Public RFCs (17 entries in `/rfcs`), per-component API decision docs, a changeset-style changelog [inferred: from hash-prefixed entries], codemods for majors (v11, v12) | [S-L09-461] [S-L09-452] [S-L09-453] [S-L09-447] |
| Notable innovation | One React API that renders on web and React Native. Brand-color white-labelling with automatic contrast. A Figma coverage-lint plugin. An official MCP server (npm since 2025-05-06) so AI agents generate Blade code | [S-L09-461] [S-L09-459] [S-L09-463] |

## Visual signature: why it looks like this
- TASA Orbiter headings over Inter body text -> crisp, geometric fintech headlines with neutral, dense body copy. It replaced Lato's softer look in 2024 [S-L09-449] [S-L09-454].
- Azure blue about #1364F1 (hsla 218,89%,51%) on blue-gray neutrals (hue 200-218) -> a cool, trustworthy "payments" palette. Even the shadows are tinted blue-gray [S-L09-450] [S-L09-449].
- 8px radius on standard buttons (12px on large), a scale up to 24px, and 0.5px hairline borders -> soft, modern controls and cards that stay crisp on retina screens [S-L09-448] [S-L09-486].
- Very low-opacity shadows (.06) with large blur (up to 24px) -> surfaces float gently. Separation comes from tint and border more than from shadow [S-L09-449].
- Emphasized (0.5,0,0,1) and overshoot (0.5,0,0.3,1.5) easings with 80-480 ms durations -> snappy UI with small playful overshoots on entry [S-L09-448].

## Recent changes 2024-2026
- 2024-01-24: v11.0.0 "Blade Visual Refresh". Brand-refresh visuals, Inter + TASA Orbiter, new font-size and line-height scale, codemods. Breaking for all components [S-L09-452] [S-L09-453] [S-L09-454].
- 2024-02-27: Blade published to the Figma Community [S-L09-464].
- 2024-12-11: v12.0.0 Motion Presets. New duration, delay and easing tokens (RFC 2024-08-21) [S-L09-452] [S-L09-458].
- 2025-05-06: `@razorpay/blade-mcp` first published. At 1.26.0 by Sept 2026 [S-L09-463].
- 2026-01-16: Svelte support started (`blade-svelte`, `blade-core`). 35 Svelte components by Sept 2026 [S-L09-447] [S-L09-463].
- 2026-07-21: `bladeNeutralTheme` and multi-theme token publishing from Figma. Updated 2026-09-10 [S-L09-447].
- 2025-2026: AI and chat components (ChatInput, ChatMessage, GenUI) and Charts appear in source [S-L09-456].
- 2026-09-17: 12.126.0 adds a TreeView `size="small"` [S-L09-452].

## Builder takeaways
- Offer "one API, web + native" as a target. Blade's single-package model shows the token schema must carry platform-specific values (desktop vs mobile type scale; `.web.ts` / `.native.ts` files) [S-L09-449].
- Copy the `createTheme({brandColor})` flow. One brand color in, full ramp out, with a built-in contrast guard [S-L09-459].
- Offer motion as named presets (Fade, Slide, Scale, Stagger) on top of duration and easing tokens, with a built-in reduced-motion kill switch [S-L09-456] [S-L09-458].
- Ask users whether they want an MCP/AI-agent export. Blade, Ant (DESIGN.md) and Uber (Base MCP) all shipped one in 2025-2026 [S-L09-463].

## Gaps / unverified
- blade.razorpay.com is Storybook. Its `index.json` was used for counts, but rendered guideline prose was not read.
- Input and card radii were not traced. Only Button's radius mapping was read.
- Whether `blade-svelte` is published anywhere (private registry) is unknown. It is not on public npm.
- The Figma Community file page itself was not opened (only its listing). WebSearch quota ran out before a direct fetch.
- The Razorpay corporate brand refresh date and agency were not confirmed from a Tier A source. Only Blade's v11 "brand refresh" framing is verified.
