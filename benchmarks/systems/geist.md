# Vercel Geist

_Lane L09 teardown. Verified against live sources on 2026-09-23. Every value carries an [S-L09-xxx] id from `traces/L09-trace.md` or the tag [inferred]._

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Owner | Vercel (design team). Typeface made with Basement Studio and Andrés Briganti | [S-L09-619] [S-L09-625] |
| Launch and major versions | Geist typeface: npm `geist` 1.0.0 2023-10-27. Geist docs at vercel.com/geist: earliest web-archive capture 2024-03-08. Geist Pixel added 2026-02-06. The design system itself has no public version numbers | [S-L09-603] [S-L09-659] [S-L09-625] |
| Current version (Sept 2026) | Docs are live and unversioned. Font package `geist` 1.7.2 (2026-06-01); GitHub font release tags go up to 1.8.0 (2026-03-03) | [S-L09-603] [S-L09-625] |
| Platforms | Web only (React / Next.js) | [S-L09-619] |
| Open source + license | Split. Typeface: yes, SIL OFL-1.1. Components: no. Docs import from `@vercel/geistcn`, which returns 404 on public npm, so it is private/internal. Docs pages are public | [S-L09-625] [S-L09-621] [S-L09-622] |
| Code frameworks | React components (`@vercel/geistcn/components`), icons and logos in `@vercel/geistcn-assets`. Type presets ship as Tailwind classes. Tokens are CSS variables `--ds-*` | [S-L09-619] [S-L09-617] [S-L09-618] |
| Figma kit | No official public kit found. Typography docs cite an internal "Geist Core Figma system". Community recreation by Jonathan Pinto (unofficial, "32/42 components") | [S-L09-617] [S-L09-627] |
| Token tiers + naming | 2 visible tiers. Raw value: `--ds-blue-700-value` (HSL triplet). Color token: `--ds-blue-700` (hsla in sRGB, oklch on P3). A few semantic tokens: `--ds-focus-color`, `--ds-background-100`, `--ds-shadow-border`, `--ds-motion-popover-duration`. Step numbers carry fixed meanings (see Color). Composite presets: `text-{heading,button,label,copy}-{px}`, `material-{name}` | [S-L09-618] [S-L09-616] [S-L09-620] |
| Color model | 10 scales: backgrounds (2 values), gray, gray-alpha, blue, red, amber, green, teal, purple, pink; 10 steps 100-1000. Each step has a job: 100 default bg, 200 hover bg, 300 active bg, 400 default border, 500 hover border, 600 active border, 700 high-contrast bg, 800 hover high-contrast bg, 900 secondary text/icons, 1000 primary text/icons. sRGB HSL fallback, OKLCH under `@media (color-gamut: p3)`. blue-700 = hsl(212 100% 48%) / oklch(57.61% .2508 258.23). Grays are pure achromatic (hsl 0 0% x). ~92 color tokens (9 scales x 10 + 2 backgrounds). Accent fixed blue | [S-L09-616] [S-L09-618] |
| Typeface | Geist Sans (UI), Geist Mono (code, labels), Geist Pixel (display; Square, Grid, Circle, Triangle, Line). Custom, open source. Cited influences: Inter, Univers, SF Pro/Mono, Suisse International, ABC Diatype | [S-L09-625] [S-L09-617] |
| Type scale | 29 documented classes: 10 headings (72, 64, 56, 48, 40, 32, 24, 20, 16, 14), 3 buttons (16, 14, 12), 9 labels (20-12 incl. 3 mono), 7 copy (24-13 incl. 13-mono). Body `text-copy-14` 14/20 weight 400; `text-label-14` 14/20 is "most common". Headings 600 with tracking -0.06em at 72-40 (72/72 -4.32px), -0.04em at 32-24, -0.02em at 20-14. Buttons 500. Hand-tuned, named by px | [S-L09-617] [S-L09-618] |
| Spacing | 4px base (`--geist-space: 4px`). Control heights: small 32px, medium 36px (form default), large 40px. Page width 1400px. Full spacing scale not published | [S-L09-618] |
| Radius | Materials: base 6px, small 6px, medium 12px, large 12px, tooltip 6px, menu 12px, modal 12px, fullscreen 16px. Control radius `--geist-radius: 6px`; marketing 8px; popover row 6px | [S-L09-620] [S-L09-618] |
| Elevation | 8 "materials" in 2 groups: surface (base, small, medium, large) and floating (tooltip, menu, modal, fullscreen). Built from a 1px ring `0 0 0 1px #00000014` (light) / `#ffffff25` (dark) plus very faint shadows, e.g. medium `0 2px 2px #0000000a, 0 8px 8px -8px #0000000a`; modal = ring + `0 1px 1px #00000005, 0 8px 16px -4px #0000000a, 0 24px 32px -8px #0000000f` | [S-L09-620] [S-L09-618]; light/dark assignment [inferred] |
| Motion | `--ds-motion-timing-swift: cubic-bezier(.175, .885, .32, 1.1)` (small overshoot). Popover 200ms; overlay 300ms with scale .96. Reduced motion: Vercel's Web Interface Guidelines say "Provide a reduced-motion variant" | [S-L09-618] [S-L09-626] |
| Theming + modes | Light and dark (every `--ds-*` value swaps; `theme-switcher` component). P3 wide gamut where supported. No density or multi-brand mode found | [S-L09-618] [S-L09-616] [S-L09-619]; no density [inferred] |
| Component count | ~70 component pages: 77 `/geist/*` links on the intro page minus 7 foundation/asset pages, counted 2026-09-23 (e.g. button, combobox, command-menu, file-tree, gauge, json-view, split-button, status-dot) | [S-L09-619] |
| Component doc structure | Live examples per variant, then Best Practices. Button page: Sizes, Types, Shapes, Prefix and suffix, Rounded, Loading, Disabled, Link, Custom, Best Practices. Every page has a Markdown twin (`.md` or `Accept: text/markdown`) | [S-L09-622] [S-L09-619] |
| Accessibility stance | "A high contrast, accessible color system"; no WCAG level stated. Web Interface Guidelines: prefer APCA over WCAG 2, `:focus-visible`, hit targets >= 24px (44px mobile). Focus ring `0 0 0 2px bg, 0 0 0 4px blue-700` | [S-L09-619] [S-L09-626] [S-L09-618] |
| Governance / contribution | Internal Vercel team; no public contribution model. Unlisted doc slugs (release-guide, geistcn-upgrade-guide, changelog) point to an internal release process | [S-L09-622]; process [inferred] |
| Notable innovation | Color steps with fixed UI jobs (400 = border, 900 = secondary text) across every hue. Docs written for agents (Markdown twin of every page, `/design.md` skill). Open-source typeface as the portable part of the brand | [S-L09-616] [S-L09-619] [S-L09-625] |

## Visual signature: why it looks like this
- Pure #fff / #000 page backgrounds (background-200 #fafafa) + achromatic grays (hsl 0 0% x) -> stark black-and-white; no warm or cool tint anywhere [S-L09-618].
- Geist Sans 600 headings with -0.06em tracking at 40-72px -> tight, Swiss-poster headlines that read as "engineered" [S-L09-618] [S-L09-625].
- 1px alpha rings (`0 0 0 1px #00000014`) instead of solid borders, shadows at 2-6% alpha -> hairline edges and almost flat surfaces [S-L09-618].
- 6px control radius, 12px panels, 16px only for fullscreen -> precise, slightly soft corners, never pill-shaped by default [S-L09-620].
- Color kept for meaning: one blue (blue-700) for focus and links, other hues for status -> the UI is ~95% grayscale [S-L09-616] [inferred share].
- Visible grid guides (`GridSystem` with `guideWidth={1}`) -> the "blueprint" look of vercel.com; docs call the grid "a core part of the Vercel aesthetic" [S-L09-624] [S-L09-619].
- Swift overshoot curve (y2 = 1.1) at 200-300ms with a .96 scale-in -> overlays pop in quickly and settle [S-L09-618].

## Recent changes 2024-2026
- 2024-03-08: earliest archived capture of vercel.com/geist docs [S-L09-659].
- 2025-05-28: font 1.5.0; 2025-11-13: 1.6.0 adds Vietnamese [S-L09-625].
- 2026-01-29: font 1.7.0 redesigns Cyrillic; coding ligatures move from default to Stylistic Set 11 [S-L09-625].
- 2026-02-06: Geist Pixel ships (npm `geist@1.7.0`) with 5 pixel variants [S-L09-625] [S-L09-603].
- Undated, live now: components documented as `@vercel/geistcn` (private npm); every docs page offered as Markdown for agents; Web Interface Guidelines published at vercel.com/design/guidelines [S-L09-619] [S-L09-621] [S-L09-626].

## Builder takeaways
- Offer a "purpose-stepped ramp" preset: 10 steps where 1-3 are background states, 4-6 border states, 7-8 solid fills, 9-10 text. It turns token choice into a lookup [S-L09-616].
- Generate P3 values in OKLCH behind `@media (color-gamut: p3)` with sRGB fallbacks, as Geist does [S-L09-618].
- Model elevation as "materials" (radius + ring + shadow bundled per level), not separate shadow and radius tokens [S-L09-620].
- Ship a Markdown twin of every generated docs page so coding agents can read the system [S-L09-619].

## Gaps / unverified
- Full spacing scale, icon count, and grid breakpoints: not published in pages that render server-side.
- Component count is a link scan of the intro page, not an official number.
- Which shadow values belong to light vs dark theme is inferred from alpha levels.
- No public changelog: `/geist/changelog` shows the intro content only.
- Launch date of the docs: only the archive capture date (2024-03-08) is known.
- GitHub font tag 1.8.0 (2026-03-03) is newer than npm latest 1.7.2 (2026-06-01); the repo mixes font-file and npm-package tags.
