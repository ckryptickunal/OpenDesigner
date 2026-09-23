# GitHub Primer

_Lane L09 teardown. Verified against live sources on 2026-09-23. Every value carries an [S-L09-xxx] id from `traces/L09-trace.md` or the tag [inferred]._

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Owner | GitHub (Primer team) | [S-L09-320] [S-L09-338] |
| Launch and major versions | `@primer/css` 12.0.0 2019-02-19 (older history not checked). Primitives first published 2019-03-14. `@primer/react` published under that name from v34 (2021-12-08); v35 2022-03-09, v36 2023-10-31, v37 2024-10-21, v38 2025-10-27. Primitives v8 2024-04-23, v9 2024-08-21, v10 2024-12-04, v11 2025-07-03. ViewComponents 0.0.1 2021-02-26 | [S-L09-322] [S-L09-321] [S-L09-320] [S-L09-323] |
| Current version (Sept 2026) | `@primer/react` 38.40.0 (2026-09-18); `@primer/primitives` 11.10.0 (2026-07-30); `@primer/view-components` 0.53.5 (maintenance mode); `@primer/css` 22.3.1 (KTLO); `@primer/mcp` 1.1.0 (2026-09-03) | [S-L09-320] [S-L09-321] [S-L09-323] [S-L09-322] [S-L09-336] |
| Platforms | Web (GitHub.com). Token build also outputs Figma variables. No native mobile components in Primer [inferred] | [S-L09-328] [inferred] |
| Open source + license | Yes; MIT (react, primitives, css, view_components, react-brand) | [S-L09-320] [S-L09-321] [S-L09-340] |
| Code frameworks | React (primary). Rails ViewComponents (maintenance mode since Feb 2026). CSS (KTLO). v38 removed styled-components, styled-system, the `sx` prop and `Box` | [S-L09-320] [S-L09-323] [S-L09-322] [S-L09-337] |
| Figma kit | "Primer Web" product library with components, variables and styles; files published on the Primer Figma Community page. Variables: yes | [S-L09-335] |
| Token tiers + naming | 3 tiers: base -> functional -> component (completed in 11.8.0). camelCase `{property}-{variant}-{state}`. Base: `--base-size-4`, `--base-duration-200`. Functional: `--fgColor-default`, `--bgColor-muted`, `--borderColor-default`, `--control-medium-size`, `--space-md`. Component: `--button-primary-bgColor-rest`. Source in W3C DTCG JSON5 | [S-L09-327] [S-L09-331] [S-L09-346] [S-L09-378] |
| Color model | 8 hue ramps (blue, coral, green, orange, pink, purple, red, yellow) x 10 steps (0-9) + neutral 0-13. Stored as HSL + hex (sRGB). 83 functional color roles in light (20 fgColor, 33 bgColor, 30 borderColor); 959 vars in the light theme file. Accent blue-5 `#0969da`; primary button green `#1f883d` | [S-L09-330] [S-L09-331] |
| Typeface | UI: 'Mona Sans VF' first (since 2026-03-25), then -apple-system, Segoe UI, Noto Sans, Helvetica, Arial. Mono: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas. Brand UI also uses Mona Sans and Hubot Sans | [S-L09-326] [S-L09-327] [S-L09-340] |
| Type scale | 11 functional styles: display, title large/medium/small, subtitle, body large/medium/small, caption, codeBlock, codeInline. Base sizes 12 / 14 / 16 / 20 / 32 / 40px. Body-medium 14px, line height 1.5. Line heights 1.25 / 1.375 / 1.5 / 1.625 / 1.75. Weights 300 / 400 / 500 / 600. Hand-tuned. Code block 13px | [S-L09-326] |
| Spacing | Base size scale 2, 4, 6, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 64, 80, 96, 112, 128px (+ negatives). Functional `space-xxs` 2, `xs` 4, `sm` 8, `md` 12, `lg` 16, `xl` 24. Stack gap/padding: condensed 8, normal 16, spacious 24 | [S-L09-324] [S-L09-325] |
| Radius | small 3px, medium 6px, large 12px, full 9999px. `borderRadius-default` = medium (6px). Overlays use medium | [S-L09-324] [S-L09-325] |
| Elevation | Borders first (1px `#d1d9e0`), light shadows second. 8 shadow tokens: resting xsmall `0 1px 1px #1f23280d`, small, medium `0 1px 1px #25292e1a, 0 3px 6px #25292e1f`; floating small, medium, large `0 40px 80px #25292e3d`, xlarge; inset | [S-L09-331] |
| Motion | Base durations 0, 50, 100, 200 ... 1000ms. Easings: ease (0.25,0.1,0.25,1), easeIn (0.7,0.1,0.75,0.9), easeOut (0.3,0.8,0.6,1), easeInOut (0.6,0,0.2,1), linear. Functional: micro 100 / short 200 / medium 300 / long 500ms; hover = 100ms ease, stateChange = 200ms easeInOut, enter = 300ms easeOut, exit = 200ms easeIn. No springs. No reduced-motion token | [S-L09-324] [S-L09-325] |
| Theming + modes | 14 color themes: light, light-high-contrast, light-colorblind, light-colorblind-high-contrast, light-tritanopia, light-tritanopia-high-contrast, dark, dark-high-contrast, dark-dimmed, dark-dimmed-high-contrast, dark-colorblind, dark-colorblind-high-contrast, dark-tritanopia, dark-tritanopia-high-contrast. One CSS file per theme. Pointer density: size-fine / size-coarse (min target 16px vs 44px). Dark default bg `#0d1117` | [S-L09-328] [S-L09-346] [S-L09-325] |
| Component count | 62 public components on primer.style/product/components (counted from page links, 2026-09-23), plus 24 listed "Internal Components" | [S-L09-332] |
| Component doc structure | Tabs: React (examples, props) / Guidelines / Accessibility. Status labels (Alpha, Beta, Stable, Deprecated, Draft) | [S-L09-333] |
| Accessibility stance | "WCAG 2.2 AA conformance". Colorblind (protanopia-deuteranopia), tritanopia and high-contrast variants of light, dark and dark dimmed | [S-L09-334] [S-L09-328] |
| Governance / contribution | Central GitHub team. "not looking for external contributions from non-GitHub staff". ADRs for token decisions; changesets for releases | [S-L09-338] [S-L09-378] [S-L09-327] |
| Notable innovation | Token build writes an LLM spec (`DESIGN_TOKENS_SPEC.md`) and a CSS header rule "Never use raw values (hex/px). Use semantic tokens ONLY." Functional CSS vars carry a one-line usage comment. `@primer/mcp` server exposes components, patterns, tokens, icons, CSS lint and a11y review to agents | [S-L09-329] [S-L09-331] [S-L09-336] |

## Visual signature: why it looks like this
- 1px `#d1d9e0` borders on white, resting shadows no bigger than `0 3px 6px` -> flat, boxed, engineering look where structure comes from lines, not depth. [S-L09-331]
- Cool blue-gray neutrals (HSL hue 207-214, e.g. `#f6f8fa`, `#d1d9e0`, `#59636e`, text `#1f2328`) -> crisp, technical, slightly cold canvas. [S-L09-330] [S-L09-331]
- Green primary `#1f883d` plus blue accent `#0969da` -> the GitHub pair: green means "do/merge", blue means links, focus and selection. [S-L09-331]
- 14px body, 32px medium controls, 6px radius -> dense, desktop-first UI with slightly softened corners. [S-L09-326] [S-L09-325] [S-L09-324]
- Mona Sans VF at the front of every sans stack since March 2026 -> more brand voice than the old pure system stack, while system fonts stay as fallbacks. [S-L09-327]
- Short transitions (100-300ms) with plain CSS curves -> motion stays out of the way. [S-L09-325]

## Recent changes 2024-2026
- 2024-10-21: Primer React v37. [S-L09-320]
- 2024-12-04: primitives v10; motion tokens added in 10.0.0. [S-L09-321] [S-L09-327]
- 2025-05-29: Primer CSS v22; the repo now says KTLO mode (date of that notice not checked). [S-L09-322]
- 2025-07-03: primitives v11 adds high-contrast colorblind, tritanopia and dark dimmed themes. [S-L09-327]
- 2025-08-06: `@primer/mcp` first published. [S-L09-336]
- 2025-10-27: Primer React v38 drops styled-components, styled-system, `sx` and `Box`. [S-L09-337]
- 2026-01-28: primitives 11.4.0 adds a text size scale and line-height scale. [S-L09-327]
- February 2026: ViewComponents enters maintenance mode; GitHub consumers told to migrate to Primer React. [S-L09-323]
- 2026-02-24: primitives 11.5.0 moves dimensions, durations and shadows to W3C DTCG object format (breaking). [S-L09-327]
- 2026-03-25: primitives 11.6.0 makes 'Mona Sans VF' the primary UI font. [S-L09-327]
- 2026-05-08: primitives 11.8.0 adds functional motion and spacing tokens. [S-L09-327] [S-L09-321]

## Builder takeaways
- Offer a "developer tool" preset: cool gray neutrals, 1px borders over shadows, 14px body, 6px radius, 32px controls, green primary + blue accent.
- Offer color-vision themes as a toggle set (protanopia-deuteranopia, tritanopia, high contrast) generated from the same functional role names. Primer proves 14 themes can share one role list.
- Copy the agent-ready outputs: per-token usage comments on semantic tokens, a generated token spec for LLMs, and an MCP server.
- Ask whether the user needs pointer density (fine vs coarse) as a separate axis from color mode.

## Gaps / unverified
- Primer's history before 2019 (the original `primer` CSS package) was not checked.
- How themes are switched at runtime (HTML data attributes) was not confirmed in this pass; only the per-theme CSS files were seen.
- The date GitHub put Primer CSS into KTLO mode is not shown in the README.
- A reduced-motion policy may exist in component code or guidelines; none was found in the token files.
