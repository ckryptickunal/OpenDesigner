# Mantine

_Lane L09 teardown. Verified against live sources on 2026-09-23. Every value carries an [S-L09-xxx] id from `traces/L09-trace.md` or the tag [inferred]._

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Owner | Open-source project, GitHub org `mantinedev` (repo created 2021-01-07); lead maintainer Vitaly Rtishchev | [S-L09-648]; maintainer name [inferred] |
| Launch and major versions | 1.0.0 2021-05-03; 2.0.0 2021-07-05; 3.0.0 2021-10-10; 4.0.0 2022-03-10; 5.0.0 2022-07-25; 6.0.0 2023-03-02; 7.0.0 2023-09-18 (native CSS); 8.0.0 2025-05-05; 9.0.0 2026-03-31 | [S-L09-602] [S-L09-663] |
| Current version (Sept 2026) | @mantine/core 9.6.2, 2026-09-21. Monthly minors 9.1-9.6 (2026-04-21 to 2026-08-31). `legacy` tag = 7.17.8 | [S-L09-602] |
| Platforms | Web only | [S-L09-648] |
| Open source + license | Yes, MIT (~31.8k GitHub stars) | [S-L09-648] |
| Code frameworks | React (19.2+ required from v9). Styling = shipped `styles.css` + CSS modules + CSS variables (no CSS-in-JS since v7). Packages: core, hooks, form, dates, charts (Recharts 3+), schedule (new in v9), tiptap (3+), notifications, spotlight, carousel, dropzone, modals, nprogress, code-highlight | [S-L09-646] [S-L09-663] [S-L09-647] |
| Figma kit | No official kit found. Community kits only (e.g. Pretine 7 by Ravn, "Mantine UI Component Library" by the Shews). Variables: n/a | [S-L09-649] |
| Token tiers + naming | JS theme object (`createTheme`) compiled to CSS variables, 3 layers. Palette: `--mantine-color-blue-6`, `--mantine-spacing-md`, `--mantine-radius-md`. Per-color variant tokens: `--mantine-color-blue-filled`, `-filled-hover`, `-light`, `-light-hover`, `-light-color`, `-outline`, `-outline-hover`, `-text`. Global semantic: `--mantine-color-body`, `--mantine-color-text`, `--mantine-color-dimmed`, `--mantine-color-default-border`, `--mantine-primary-color-filled`. Sizes multiplied by `--mantine-scale` | [S-L09-643] [S-L09-644] |
| Color model | 14 palettes (dark, gray, red, pink, grape, violet, indigo, blue, cyan, teal, green, lime, yellow, orange) x 10 shades indexed 0-9, sRGB hex; overrides must supply at least 10 shades; OKLCH input accepted. Primary: `primaryColor: 'blue'`, `primaryShade: { light: 6, dark: 8 }` -> #228be6 / #1971c2. 17 global semantic vars + 8 variant vars per color. Accent options: `virtualColor` (different color per scheme), `autoContrast` (luminance threshold 0.3, off by default) | [S-L09-643] [S-L09-644] [S-L09-651] |
| Typeface | System stack: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif + emoji. Mono: ui-monospace, SFMono-Regular, Menlo... No custom face | [S-L09-643] |
| Type scale | 11 styles. Text: xs 12, sm 14, md 16, lg 18, xl 20px; line heights 1.4 / 1.45 / 1.55 / 1.6 / 1.65. Headings (weight 700): h1 34/1.3, h2 26/1.35, h3 22/1.4, h4 18/1.45, h5 16/1.5, h6 14/1.5. Weights: regular 400, medium 600, bold 700. Body 16px / 1.55. Hand-tuned | [S-L09-643] [S-L09-644] |
| Spacing | 5 steps, no strict base unit: xs 10px, sm 12, md 16, lg 20, xl 32. Breakpoints xs 36em, sm 48em, md 62em, lg 75em, xl 88em | [S-L09-643] [S-L09-644] |
| Radius | xs 2px, sm 4px, md 8px, lg 16px, xl 32px. `defaultRadius: 'md'` = 8px (was sm = 4px before v9) | [S-L09-643] [S-L09-646] |
| Elevation | 5 layered shadows at 4-10% black. xs `0 1px 3px rgba(0,0,0,.05), 0 1px 2px rgba(0,0,0,.1)`; md `0 1px 3px /.05, 0 20px 25px -5px /.05, 0 10px 10px -5px /.04`; xl `0 1px 3px /.05, 0 36px 28px -7px /.05, 0 17px 17px -7px /.04`. Borders optional (`withBorder`; Dialog on by default in v9) | [S-L09-643] [S-L09-646] |
| Motion | No duration or easing tokens in the theme. `Transition` defaults: 250ms enter, 250ms exit, `ease`. `respectReducedMotion: false` by default; when true and the OS asks, durations become 0 | [S-L09-643] [S-L09-645] |
| Theming + modes | `defaultColorScheme`: light (default), dark, auto; sets `data-mantine-color-scheme` on `<html>`. Dark body = dark-7 (#242424). Global density knob `--mantine-scale`. Brand via `createTheme` (colors, primaryColor, component default props). No high-contrast mode | [S-L09-651] [S-L09-644] [S-L09-643]; no HC [inferred] |
| Component count | Doc pages in llms.txt, 2026-09-23: 118 core components (119 core slugs minus 1 package page), 16 dates, 23 charts, 14 schedule, 9 extensions; plus 82 hooks | [S-L09-647] |
| Component doc structure | Usage (interactive configurator), feature/example sections, Props table, Styles API (named inner parts) | [S-L09-647] |
| Accessibility stance | Follows WAI-ARIA; interactive components tested with jest-axe, keyboard and focus unit tests; "more than 10,000 unit tests"; manual VoiceOver checks. No WCAG level stated | [S-L09-650] |
| Governance / contribution | Maintainer-led OSS with GitHub discussions and sponsorship ("Support Mantine development" in each changelog) | [S-L09-646] [S-L09-649] |
| Notable innovation | Per-scheme primary shade (6 light / 8 dark); `virtualColor`; `autoContrast`; one `--mantine-scale` multiplier for all sizes; Styles API for every inner element; large hooks library (82). v9 ships an MCP server and agent skills for Claude Code and Codex | [S-L09-643] [S-L09-651] [S-L09-647] [S-L09-646] |

## Visual signature: why it looks like this
- 8px default radius (v9) + filled blue-6 #228be6 -> friendly, rounded controls in a bright, slightly cyan blue [S-L09-643] [S-L09-646].
- System font at 16px / 1.55 body, medium weight 600 -> roomy text that looks native on each OS [S-L09-643].
- Spacing 10/12/16/20/32 (not a 4px grid) -> padding feels a little airier than Tailwind-style systems at the same size names [S-L09-643]; comparison [inferred].
- Layered shadows at 4-5% alpha with large negative spread -> soft, diffuse depth rather than crisp edges [S-L09-643].
- Neutral `dark` palette (#242424 body, #C9C9C9 lightest) -> dark mode is plain charcoal, not blue-tinted [S-L09-643] [S-L09-663].
- Opaque `light` variant since v9 -> tinted buttons and badges read with more contrast than the old translucent tints [S-L09-646].

## Recent changes 2024-2026
- 2025-05-05: v8.0. Menu submenus, date values as strings, TimePicker, TimeGrid, Heatmap, CodeHighlight with shiki [S-L09-648] [S-L09-602].
- 2026-03-31: v9.0. React 19.2+ required; new `@mantine/schedule`; FloatingWindow, OverflowList, Marquee, Scroller, BarsList; loading state on all inputs; Combobox virtualization [S-L09-646].
- v9.0 default changes: `theme.fontWeights` added and medium moved 500 -> 600; `defaultRadius` sm (4px) -> md (8px); `light` variant made opaque; Dialog `withBorder` on by default [S-L09-646].
- v9.0 AI tooling: `@mantine/mcp-server` and Mantine skills for Claude Code and Codex [S-L09-646].
- 2026-04-21 to 2026-09-21: monthly minors 9.1-9.6, latest 9.6.2 [S-L09-602].

## Builder takeaways
- Offer one global density multiplier (like `--mantine-scale`) in addition to per-token edits [S-L09-644].
- Ask which ramp step is "brand" separately for light and dark (Mantine: 6 and 8). A single brand step rarely works in both modes [S-L09-643].
- Provide `virtualColor`-style tokens (one name, different palette per scheme) and an optional auto-contrast toggle [S-L09-651].
- Version presets. Mantine changed its defaults in v9 (radius 4 -> 8px, medium 500 -> 600), so a "Mantine preset" must say which version it copies [S-L09-646].

## Gaps / unverified
- No official Figma kit found; community kits were not opened.
- Lead maintainer name is from memory, not a source opened this session.
- Component counts are doc-page counts from llms.txt; some dates/schedule pages are views or guides rather than separate components.
- No stated WCAG level; no motion tokens beyond the Transition defaults.
