# Ant Design

_Lane L09 teardown. Verified against live sources on 2026-09-23. Every value carries an [S-L09-xxx] id from `traces/L09-trace.md` or the tag [inferred]._

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Owner | Ant Group (Ant Design team); built for Ant Group's mid- and back-office consoles | [S-L09-460] |
| Launch and major versions | Created 2015; 1.0 2016-05-10; 2.0 2016-09-28; 3.0 2017-12-04; 4.0 2020-02-28; 5.0 2022-11-18 (CSS-in-JS + tokens); 6.0 2025-11-21 on npm (GitHub release 2025-11-22) | [S-L09-460] [S-L09-421] [S-L09-402] |
| Current version (Sept 2026) | `antd` 6.6.5, released 2026-09-20. Minors every 1-3 months (6.1 2025-12-08 to 6.6 2026-08-10), patches about weekly. v5 still tagged `latest-5` = 5.29.3 | [S-L09-400] [S-L09-401] [S-L09-421] |
| Platforms | Web (desktop-first React). Sister libraries: `antd-mobile` 5.43.0 (mobile web), `@ant-design/x` 2.9.0 (AI chat UI) | [S-L09-400] [S-L09-419] [S-L09-418] |
| Open source + license | Yes; MIT | [S-L09-400] |
| Code frameworks | React only (peer react >= 18). Styling: `@ant-design/cssinjs` 2.x; CSS variables on by default since v6; optional `zeroRuntime` mode that uses the static `antd/dist/antd.css` | [S-L09-400] [S-L09-402] [S-L09-413] |
| Figma kit | No official Figma kit. The resources page lists the official "Sketch Symbols" (5.13.3) and the Kitchen Sketch plugin. Every Figma kit listed is third-party (AntUIKit, AntBlocks, and others) | [S-L09-417] |
| Token tiers + naming | 4 tiers: Seed, then Map, then Alias, then Component. camelCase grammar. Seed: `colorPrimary`, `borderRadius`, `sizeUnit`. Map: `colorPrimaryBg`, `borderRadiusLG`, `motionDurationMid`. Alias: `colorLink`, `boxShadowSecondary`, `controlPaddingHorizontal`. Component tokens are set per component under `theme.components`. Counts: about 34 seed fields and 93 alias fields | [S-L09-413] [S-L09-403] [S-L09-408] [inferred: field counts by regex over interface files] |
| Color model | 10-step palettes (`blue-1` to `blue-10`) generated in HSV by `@ant-design/colors`. The base color sits at step 6 (5 lighter, 4 darker). Constants: hueStep 2, saturationStep 0.16/0.05, brightnessStep 0.05/0.15. 12 preset hues plus `pink`, a deprecated alias of magenta. 5 functional seeds (primary #1677ff, success #52c41a, warning #faad14, error #ff4d4f, info #1677ff). Neutral text is alpha black: 0.88 / 0.65 / 0.45 / 0.25. About 79 map color tokens. sRGB hex | [S-L09-412] [S-L09-403] [S-L09-424] [inferred: map color count] |
| Typeface | System stack: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans'. Mono: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier. No custom font | [S-L09-403] |
| Type scale | Generated. Formula: 14 x e^(i/5), rounded to even. Output: 12, 14, 16, 20, 24, 30, 38, 46, 56, 68 px. Base body 14px, line height (14+8)/14 = 1.571 (22px). Named: fontSizeSM 12, fontSize 14, fontSizeLG 16, fontSizeXL 20, Heading1-5 = 38/30/24/20/16. Only 2 weights in UI chrome: 400 and 600 (`fontWeightStrong`) | [S-L09-407] [S-L09-409] [S-L09-426] [S-L09-460] |
| Spacing | 4px unit, derived as sizeUnit 4 x (sizeStep 4 + n). Scale: XXS 4, XS 8, SM 12, MS 16, (base) 16, MD 20, LG 24, XL 32, XXL 48. Padding and margin tokens map onto these | [S-L09-406] [S-L09-408] |
| Radius | Derived from seed 6: XS 2, SM 4, base 6, LG 8, Outer 4. Default control radius 6px | [S-L09-405] [S-L09-403] |
| Elevation | Shadows plus 1px #d9d9d9 borders. 3 alias shadows. `boxShadow` and `boxShadowSecondary` are both `0 6px 16px 0 rgba(0,0,0,.08), 0 3px 6px -4px rgba(0,0,0,.12), 0 9px 28px 8px rgba(0,0,0,.05)`. `boxShadowTertiary` is `0 1px 2px 0 .05 / 0 1px 6px -1px .03 / 0 2px 4px 0 .03`. Page bg #f5f5f5 against white containers | [S-L09-408] [S-L09-424] [S-L09-426] |
| Motion | motionUnit 0.1s, so Fast 0.1s, Mid 0.2s, Slow 0.3s. 8 cubic-beziers, e.g. EaseOut (0.215,0.61,0.355,1), EaseInOut (0.645,0.045,0.355,1), EaseOutBack (0.12,0.4,0.29,1.46), EaseOutCirc (0.08,0.82,0.17,1). No springs. Seed `motion: false` turns animation off. The v6 CSS has 24 per-component `prefers-reduced-motion: reduce` blocks | [S-L09-403] [S-L09-404] [S-L09-425] [S-L09-426] |
| Theming + modes | Algorithms: `defaultAlgorithm`, `darkAlgorithm`, `compactAlgorithm`, combinable (dark + compact). Compact uses font base 12 and controlHeight 28. Brand theming: change the seed and palettes regenerate. Nested `ConfigProvider` for sub-themes. Switched at runtime through the ConfigProvider `theme` prop. v6 emits 1,164 distinct `--ant-*` CSS variables. No high-contrast mode | [S-L09-413] [S-L09-411] [S-L09-423] [S-L09-426] |
| Component count | 73 entries on the components overview (7 groups), 2026-09-23. Includes utilities (App, ConfigProvider, Util, Icon) and the deprecated List. About 68 true components [inferred] | [S-L09-414] [S-L09-416] |
| Component doc structure | When To Use, Examples (live demos), API, Semantic DOM, Design Token, FAQ, Design Guide | [S-L09-422] |
| Accessibility stance | No published WCAG conformance target. The repo's own DESIGN.md admits that white on #1677FF and primary text on pale selected backgrounds fall below WCAG AA 4.5:1. Measured: white on #1677ff = 4.1:1. Advice: darken `colorPrimary` | [S-L09-460] [S-L09-485] [inferred: contrast computed] |
| Governance / contribution | Open GitHub PR model. Core team at Ant Group. Weekly patch releases. Big changes land in the changelog and upgrade guides; no formal public RFC process was found | [S-L09-401] [inferred: no RFC folder observed] |
| Notable innovation | Algorithmic token pipeline: from one seed, the Seed, Map and Alias tiers generate palettes, sizes, radii and type. The dark and compact modes are algorithms, not hand-made token sets. In 2026 it added a `DESIGN.md` for AI coding tools | [S-L09-413] [S-L09-460] |

## Visual signature: why it looks like this
- 14px base with 22px line height, and 32px controls (24 SM, 40 LG) -> dense, table-heavy enterprise screens. A 1440px window fits sidebar, header, an 8-column table and a detail pane [S-L09-403] [S-L09-410] [S-L09-460].
- 6px radius on controls and 8px on cards and modals -> softly rounded but businesslike. Not pill-shaped, not sharp [S-L09-405].
- Saturated #1677ff used only on actions, links, focus and selection. Neutrals are alpha black over #fff/#f5f5f5 -> a calm gray canvas where blue marks interactivity [S-L09-403] [S-L09-424] [S-L09-460].
- 1px #d9d9d9 borders plus a soft 3-layer shadow kept for popups -> flat surfaces. Depth appears only on floating layers [S-L09-408] [S-L09-426].
- System font stack and only weights 400 and 600 -> native, neutral text with no brand voice in the typography [S-L09-403] [S-L09-460].
- 0.1s, 0.2s and 0.3s durations with ease-out-circ and back curves -> quick, slightly springy feedback without physics springs [S-L09-403] [S-L09-404].

## Recent changes 2024-2026
- 2025-11-21: v6.0.0 released. CSS variables became the default. New `zeroRuntime` option. IE support dropped. React 18+ required. Semantic DOM structure across components. Direction props renamed to logical `start`/`end`. BackTop, Dropdown.Button and the Icon placeholder removed. Masonry added. React Compiler enabled in the bundled build [S-L09-402] [S-L09-421].
- 2025-12 to 2026-08: minors 6.1 to 6.6. 6.6.0 (2026-08-10) added the Listy virtualized list, a `focusOutline` token and global input `variant` [S-L09-401] [S-L09-421].
- 2026-05-20: `DESIGN.md` for AI tools added to the repo. Updated 2026-06-24 [S-L09-460].
- v5 kept on the `latest-5` tag (5.29.3) for teams that have not migrated [S-L09-421].

## Builder takeaways
- Offer a "Seed -> generated" preset. The user picks one primary color, one radius, one font size and one control height, and the builder derives palettes, the radius ladder, the type scale and control sizes with formulas like Ant's (e.g. radius LG = base + 2; type = base x e^(i/5)) [S-L09-405] [S-L09-407].
- Treat dark and compact as transforms on tokens, not as separate token files. Let users combine them [S-L09-411] [S-L09-413].
- Build in a contrast check. Ant's own default primary fails AA for white text (4.1:1). A builder should warn when the seed produces small white text below 4.5:1 [S-L09-460].
- Ask about density up front. A 14px/32px base means back-office tool. A 16px/40-48px base means consumer app.

## Gaps / unverified
- The ant.design site is client-rendered. Doc structure was read from the Markdown source in GitHub, not from the rendered page.
- Field counts per token tier are regex counts over interface files. They are approximate.
- No public RFC or governance document was located. The contribution model is inferred from GitHub practice.
- Whether any official Ant Design Figma kit exists outside the resources page was not checked. WebSearch quota was exhausted.
