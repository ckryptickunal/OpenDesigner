# Chakra UI

_Lane L09 teardown. Verified against live sources on 2026-09-23. Every value carries an [S-L09-xxx] id from `traces/L09-trace.md` or the tag [inferred]._

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Owner | Open-source project `chakra-ui/chakra-ui`; maintainers include Segun Adebayo (creator), isBatak, Adebesin-Cell | [S-L09-630] [S-L09-633] [S-L09-636] [S-L09-638]; "creator" [inferred] |
| Launch and major versions | 1.0.0 2020-11-13; 2.0.0 2022-05-12; 3.0.0 2024-10-22. v4 not released: direction set 2026-08-31, beta-first, no date | [S-L09-601] [S-L09-639] [S-L09-638] |
| Current version (Sept 2026) | @chakra-ui/react 3.37.0, 2026-08-28 | [S-L09-601] |
| Platforms | Web only | [S-L09-630] |
| Open source + license | Yes, MIT (~40.7k GitHub stars) | [S-L09-630] |
| Code frameworks | React only. v3 = Ark UI 5.39.2 headless parts (built on Zag.js state machines) + Emotion runtime styling with Panda-style APIs. v4 plan: Panda v2 as the only engine, Emotion optional | [S-L09-662] [S-L09-635] [S-L09-638] |
| Figma kit | Official, free "Chakra UI v3 Figma Kit" on Figma Community (file 1506648876941130701). Variables: yes, semantic color modes "Chakra/light" and "Chakra/dark". Launched ~May 2025 | [S-L09-641] [S-L09-642] |
| Token tiers + naming | 2 tiers + a virtual palette. Tokens: `colors.blue.500`, `spacing.4`, `radii.md`. Semantic: `bg.subtle`, `fg.muted`, `border.emphasized`, `blue.solid`, `radii.l2`. Virtual: `colorPalette.solid`, resolved by the `colorPalette="blue"` prop. Plus textStyles, layerStyles, recipes (`cva`) and slot recipes (`sva`) | [S-L09-631] [S-L09-632] [S-L09-635] [S-L09-640] |
| Color model | 10 palettes (gray, red, orange, yellow, green, teal, blue, cyan, purple, pink) x 11 steps 50-950, sRGB hex. blue.500 #3b82f6, blue.600 #2563eb; gray.500 #71717a. 108 semantic color tokens: 28 global (bg 10, fg 9, border 9) + 8 roles per palette (contrast, fg, subtle, muted, emphasized, solid, focusRing, border). Blue mapping light/dark: solid 600/600, fg 700/300, subtle 100/900, muted 200/800, emphasized 300/700, focusRing 500/500, border 500/400. Accent = swap `colorPalette` | [S-L09-631] [S-L09-632] |
| Typeface | Inter for `heading` and `body` with a system fallback stack; mono `SFMono-Regular, Menlo, Monaco, Consolas...`. Not a custom face | [S-L09-631] |
| Type scale | 14 font sizes: 2xs 10px, xs 12, sm 14, md 16, lg 18, xl 20, 2xl 24, 3xl 30, 4xl 36, 5xl 48, 6xl 60, 7xl 72, 8xl 96, 9xl 128. 15 textStyles (2xs-7xl, label, none): sm 14/20, md 16/24, lg 18/28, xl 20/30, 2xl 24/32, 3xl 30/38. Line heights shorter 1.25 to taller 2. Hand-tuned, t-shirt names | [S-L09-631] [S-L09-632] |
| Spacing | 4px base, 34 steps: 0.5 = 2px, 1 = 4, 1.5 = 6, 2 = 8, 2.5 = 10, 3 = 12, 3.5 = 14, 4 = 16, 4.5 = 18, 5 = 20, 6 = 24, 7 = 28, 8 = 32, 9 = 36, 10 = 40, 11 = 44, 12 = 48, 14 = 56, 16 = 64, 20 = 80, 24 = 96 ... 96 = 384px. Breakpoints sm 480, md 768, lg 1024, xl 1280, 2xl 1536px | [S-L09-631] [S-L09-632] |
| Radius | none 0, 2xs 1px, xs 2px, sm 4px, md 6px, lg 8px, xl 12px, 2xl 16px, 3xl 24px, 4xl 32px, full 9999px. Layer radii l1 = xs (2px), l2 = sm (4px), l3 = md (6px). Button uses `l2`, so 4px by default | [S-L09-631] [S-L09-632] |
| Elevation | Shadows with light/dark values, 8 tokens (xs, sm, md, lg, xl, 2xl, inner, inset). Light md: `0px 4px 8px gray.900/10, 0px 0px 1px gray.900/30`; 2xl: `0px 24px 40px gray.900/16, 0 0 1px /30`. Dark: `black/64` blur + `0 0 1px inset gray.300/20-30` highlight. Surfaces via `bg.panel` and layerStyles `fill.*`, `outline.*` | [S-L09-632] |
| Motion | Durations: fastest 50ms, faster 100, fast 150, moderate 200, slow 300, slower 400, slowest 500. Easings: ease-in (0.42, 0, 1, 1), ease-out (0, 0, 0.58, 1), ease-in-out (0.42, 0, 0.58, 1), ease-in-smooth (0.32, 0.72, 0, 1). CSS keyframe animationStyles (slide-fade-in/out); no springs. No global reduced-motion rule found | [S-L09-631] [S-L09-662] [S-L09-639] |
| Theming + modes | Light/dark through `_light` / `_dark` conditions on semantic tokens; color-mode switching delegated to next-themes since v3. Brand theming: `createSystem(defaultConfig, defineConfig({...}))`. Per-component palette via `colorPalette`. No density or high-contrast mode | [S-L09-635] [S-L09-639] [S-L09-632]; no density/HC [inferred] |
| Component count | 114 component doc pages (llms-components.txt: 124 H1s minus 4 code-sample headings and 6 guides), counted 2026-09-23. 116 component directories in `packages/react/src/components` | [S-L09-640] [S-L09-630] |
| Component doc structure | Usage, Examples, Props on nearly every page (116 / 114 / 99 occurrences); 46 pages add an "Explorer" | [S-L09-640] |
| Accessibility stance | Tagline "an accessible component system". Interaction a11y comes from Ark UI (Zag.js machines). No WCAG level stated | [S-L09-640] [S-L09-662]; no level [inferred] |
| Governance / contribution | Maintainer-led OSS. Major direction is debated in public GitHub Discussions (v4: #10936 -> #10959) | [S-L09-636] [S-L09-638] |
| Notable innovation | `colorPalette` virtual token: one prop re-colors every part of a component. Layer radii (l1-l3). Snippets CLI copies composed components into your repo. Early llms.txt docs (2025-03) and an MCP server (2025-07) | [S-L09-640] [S-L09-632] [S-L09-639] [S-L09-637] |

## Visual signature: why it looks like this
- Neutral gray = zinc-like values (#fafafa, #f4f4f5, #e4e4e7, gray.500 #71717a) and Tailwind-like hues (blue.600 #2563eb) -> the familiar modern SaaS palette, slightly cool [S-L09-631]; resemblance [inferred].
- Controls on `l2` = 4px, cards on l3 = 6px -> crisp, small corners [S-L09-632].
- Shadows = soft blur at 10% + a 0-blur 1px ring at 20-30% -> cards get a hairline edge without a border; dark mode swaps to an inset highlight [S-L09-632].
- `solid` = palette 600 in both modes, `subtle` = 100 light / 900 dark -> strong brand fills plus tinted badge backgrounds [S-L09-632].
- Inter at 14/20 and 16/24, buttons medium weight, md button 40px tall (`h: 10`) -> readable, medium-density product UI [S-L09-631] [S-L09-632].

## Recent changes 2024-2026
- 2024-10-22: v3.0. Ark UI-based, recipes replace runtime theme functions, CSS animations replace Framer Motion, "over 25 new components", snippets CLI [S-L09-639].
- 2025-03-18: docs made AI-friendly with llms.txt [S-L09-637].
- 2025-05-15: 3.19 Combobox; 2025-07-07: 3.22 TreeView [S-L09-637].
- ~2025-05: official v3 Figma kit [S-L09-642].
- 2025-07-30: Chakra UI MCP server [S-L09-637].
- 2025-11-22: 3.30 Splitter; 2026-03-03: 3.34 DatePicker; 2026-06-10: 3.36 FloatingPanel; 2026-08-28: 3.37 DateInput (blog post dated 2026-08-22) [S-L09-633] [S-L09-637].
- 2026-08-15: v4 exploration (Panda CSS v2, Ark UI v6, multi-framework) opened; closed 2026-09-04 [S-L09-636].
- 2026-08-31: v4 direction: "Panda v2 is the only styling engine", Emotion moves to optional `@chakra-ui/emotion`, Server Components without providers, beta-first [S-L09-638].

## Builder takeaways
- Offer Chakra's 8 per-palette roles (solid, contrast, fg, subtle, muted, emphasized, focusRing, border) as a default semantic vocabulary. It is small and covers most component states [S-L09-632].
- Build a virtual palette: components reference `colorPalette.*`, users swap palettes per instance. It removes the need for per-color variants [S-L09-640].
- Add layer radii (l1/l2/l3) so nested elements step down in radius from one user-chosen base [S-L09-632].
- Use a 7-step named duration scale (50-500ms) as the motion preset [S-L09-631].

## Gaps / unverified
- Reduced-motion handling: no global rule found; per-component behavior not checked.
- Figma kit component coverage and exact launch date (only an X post, ~May 2025).
- v4 release date: none announced. A third-party site claiming a Tailwind/shadcn-based v4 was rejected because it contradicts the official discussions.
- Chakra UI Pro (paid) current status was not checked.
