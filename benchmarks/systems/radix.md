# Radix (Themes + Primitives + Colors)

_Lane L09 teardown. Verified against live sources on 2026-09-23. Every value carries an [S-L09-xxx] id from `traces/L09-trace.md` or the tag [inferred]._

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Owner | WorkOS ("Maintained by @workos"; Themes licence "Copyright (c) 2023 WorkOS"). Originally built by Modulz | [S-L09-575] [S-L09-566]; Modulz origin [inferred] |
| Launch and major versions | Primitives: first packages Dec 2020 (react-dialog 2020-12-15), 1.0.0 line 2022-07-20; unified `radix-ui` 1.1.0 2025-01-22. Colors: 1.0 2023-06-23, 2.0 2023-08-07, 3.0 2023-10-02. Themes: 1.0 2023-08-08, 2.0 2023-10-02, 3.0 2024-03-23 | [S-L09-556] [S-L09-557] |
| Current version (Sept 2026) | `radix-ui` 1.6.7 (2026-07-24); `@radix-ui/themes` 3.3.0 (2026-01-31; 3.4.0 in CHANGELOG, not on npm); `@radix-ui/colors` 3.0.0 (2023-10-02); `@radix-ui/react-icons` 1.3.2 (2024-11-14) | [S-L09-556] [S-L09-576] |
| Platforms | Web (React) | [S-L09-558] |
| Open source + license | Yes, MIT (Primitives, Themes) | [S-L09-575] [S-L09-566] |
| Code frameworks | React only. Primitives are unstyled; Themes ships pre-styled components plus CSS (`@radix-ui/themes/styles.css`), with standalone per-component entrypoints since 3.2.0 | [S-L09-558] [S-L09-576] |
| Figma kit | No official kit listed. Docs Resources page links "Unofficial Radix Themes components for Figma, by Victor Allegret". A Figma Community file named "Radix Themes" exists; publisher not verified | [S-L09-569] [S-L09-568] |
| Token tiers + naming | 2 tiers of CSS variables. Scale: `--indigo-9`, `--gray-a5`, `--space-4`, `--radius-3`, `--font-size-5`. Semantic aliases: `--accent-1..12`, `--accent-a1..a12`, `--accent-contrast`, `--accent-surface`, `--focus-8`, `--color-background`, `--color-panel`, `--color-surface`, `--color-overlay` | [S-L09-559] |
| Color model | 12-step scales. Step jobs: 1 app bg, 2 subtle bg, 3 UI element bg, 4 hover, 5 active/selected, 6 subtle border, 7 border + focus ring, 8 hovered border, 9 solid bg (highest chroma), 10 hovered solid, 11 low-contrast text, 12 high-contrast text. 33 scales (6 grays, 25 colors, 2 overlays), each light/dark/alpha/dark-alpha, sRGB hex + display-p3 twins. Steps 11/12 guaranteed APCA Lc 60 / Lc 90 on step 2. Accent is picked, not generated: 26 `accentColor` values, 7 `grayColor` values (auto pairs a tinted gray) | [S-L09-563] [S-L09-564] [S-L09-565] [S-L09-559] |
| Typeface | System stack: `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', 'Open Sans', system-ui`. Code: `Menlo, Consolas, 'Bitstream Vera Sans Mono'` at size-adjust 0.95. Em and quote: Times New Roman | [S-L09-559] |
| Type scale | 9 steps, numbered: 12/16, 14/20, 16/24, 18/26, 20/28, 24/30, 28/36, 35/40, 60/60px (size/line height). Body = size 3 (16px/24px). Letter-spacing +0.0025em at 1 to -0.025em at 9. Weights 300/400/500/700. Hand-tuned. All multiplied by `--scaling` | [S-L09-559] |
| Spacing | `--space-1..9` = 4, 8, 12, 16, 24, 32, 40, 48, 64px, each x `--scaling` (0.9, 0.95, 1, 1.05, 1.1) | [S-L09-559] |
| Radius | `--radius-1..6` = 3, 4, 6, 8, 12, 16px x scaling x factor. Theme `radius` prop: none (factor 0), small (0.75), medium (1, default), large (1.5), full (1.5 + pill 9999px). Button size 2 (default) = 32px tall with radius-2 = 4px | [S-L09-559] [S-L09-560] |
| Elevation | 6 layered shadows built from alpha grays: shadow-1 is inset (fields); shadow-2..6 each start with a 1px `--gray-a3` ring, then soft drops (e.g. shadow-6 adds 0 12px 60px black-a3 and 0 16px 36px -20px gray-a7). Panels can be translucent with 64px backdrop blur | [S-L09-559] |
| Motion | No motion tokens; per component. Dialog in 200ms, out 160ms, `cubic-bezier(0.16, 1, 0.3, 1)`; tooltip 140ms; switch 120-140ms; segmented control 100ms. Animations wrapped in `prefers-reduced-motion: no-preference` | [S-L09-560] |
| Theming + modes | `<Theme>` props: appearance inherit/light/dark (also `.dark` / `.dark-theme` classes), accentColor (default indigo), grayColor (default auto), panelBackground solid/translucent (default translucent), radius, scaling 90-110%. Nested themes allowed. `highContrast` prop on components. No density mode beyond scaling | [S-L09-559] |
| Component count | Primitives: 30 components (2 unstable: OneTimePasswordField, PasswordToggleField) + 5 utilities, from `radix-ui` 1.6.7 exports and docs sidebar. Themes: 56 docs pages = 36 components + 5 layout + 9 typography + 6 utilities. Counted 2026-09-23 | [S-L09-558] [S-L09-562] [S-L09-561] |
| Component doc structure | Primitives: Features, Anatomy, API Reference, Examples, Accessibility (Keyboard Interactions), Custom APIs. Themes: description, View source / View as Markdown / View in Playground, API Reference (props table), Examples | [S-L09-570] [S-L09-561] |
| Accessibility stance | Primitives follow WAI-ARIA Authoring Practices patterns (each page links its pattern and lists keyboard interactions). No WCAG level stated. Color contrast stated in APCA, not WCAG ratios | [S-L09-570] [S-L09-563] |
| Governance / contribution | Company-maintained open source (WorkOS team), GitHub PRs and Discussions. No RFC process found | [S-L09-575] [S-L09-566]; RFC absence [inferred] |
| Notable innovation | The 12-step scale with a fixed job per step, now copied widely. Unstyled accessible primitives with `asChild` / Slot composition became the base layer of shadcn/ui. Theme-level `scaling` and `radius` factors that rescale the whole UI from one prop | [S-L09-563] [S-L09-558] [S-L09-559] |

## Visual signature: why it looks like this
- System font stack at 14-16px, weights up to 500 for UI -> native, quiet, "app not website" look [S-L09-559].
- Gray steps 1-2 for backgrounds, 6-7 for borders, alpha variants on top -> low-contrast, layered neutrals that tint toward the accent when grayColor is auto [S-L09-563] [S-L09-559].
- Default accent indigo-9 #3e63dd, used only on step 9-11 surfaces -> one saturated color, lots of calm gray [S-L09-565] [S-L09-563].
- Every shadow starts with a 1px gray-a3 ring -> crisp card edges in light and dark without separate borders [S-L09-559].
- Radius-2 4px buttons at 32px height by default, scalable to pill -> compact, precise controls [S-L09-560].
- Translucent panels with 64px blur and fast expo-out motion (200ms) -> soft depth and snappy overlays [S-L09-559] [S-L09-560].

## Recent changes 2024-2026
- 2024-03-23: Themes 3.0 [S-L09-556]. 2024-06-20: Themes 3.1.0 adds React 19 support [S-L09-567].
- 2025-01-22: single `radix-ui` package exposes all primitives; Themes 3.2.0 adds per-component entrypoints (2025-01-23) [S-L09-557] [S-L09-556] [S-L09-576].
- 2025-04-17 and 2025-05-05: unstable One-Time Password Field and Password Toggle Field primitives [S-L09-557].
- 2024-11-14: Radix Icons 1.3.2, the last Icons release; Radix Colors has had no release since 3.0.0 (2023-10-02) [S-L09-556].
- 2025-08-13 to 2026-06-06: no `radix-ui` release for about 10 months [S-L09-556].
- 2025-12-11: Base UI 1.0 (competing unstyled library) ships; at 1.8.0 by 2026-09-04 [S-L09-572].
- 2026-01-31: Themes 3.3.0 (Kbd soft variant, more layout props, `breakpoints` array deprecated). Last Themes repo commit 2026-04-11 [S-L09-576] [S-L09-575].
- Unreleased: Themes CHANGELOG lists 3.4.0 (`ghost-offset` button variant, ThemePanel fixes), not on npm as of 2026-09-23 [S-L09-576] [S-L09-556].
- 2026-07-02: shadcn/ui switches its default base from Radix to Base UI, citing Base UI being built by "the same folks who built Radix" [S-L09-584].
- 2026-06-06 to 2026-07-24: burst of 9 `radix-ui` releases: controlled Context Menu, unstable composition parts, React 19 ref-loop fix, tree-shakable subpath imports [S-L09-557] [S-L09-556].

## Builder takeaways
- Adopt the 12-step "job per step" scale as the builder's default ramp format; it maps directly to states (3/4/5, 6/7/8, 9/10) and text (11/12).
- Offer a "scaling" slider (90-110%) and a radius factor, as Radix does, so one control reshapes the whole system.
- Offer alpha ramps and P3 twins alongside hex, and state contrast in APCA and WCAG both.
- Ask the user whether they want styled components or unstyled primitives; Radix proves the two layers can ship separately.

## Gaps / unverified
- Figma: the Community file "Radix Themes" could not be opened; the docs call the only listed kit unofficial.
- No official statement found on maintenance pace; the 10-month release gap and 2026 burst are from npm dates only. Web search budget ran out before I could look for commentary.
- WCAG conformance level: not public.
- Modulz origin and WorkOS acquisition year not re-verified.
- Themes typography and radius values come from the 3.3.0 npm source; the docs pages for these tokens were not opened separately.
- Themes "36 components" is my split of the 56-page sidebar (Layout / Typography / Components / Utilities headings as shown on the docs site).
