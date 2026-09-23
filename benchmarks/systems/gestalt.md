# Pinterest Gestalt

_Lane L09 teardown. Verified against live sources on 2026-09-23. Every value carries an [S-L09-xxx] id from `traces/L09-trace.md` or the tag [inferred]._

> Status note (Sept 2026): Gestalt runs two token themes through the same React components: "classic" (the open-source default) and "visual refresh" (VR, switched on by experiment). A new docs site ("Gestalt 2.0") launched in Nov 2025 and the public docs moved to `/v1`. The last npm release was 177.0.12 on 2025-12-09.

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Owner | Pinterest (Gestalt team) | [S-L09-362] [S-L09-364] |
| Launch and major versions | Earliest modern npm release 0.15.0 on 2017-03-09 (the npm name also holds unrelated 2012 versions [inferred]). 1.0.0 2020-02-20. Majors ship very often: v130 2024-01-04, v167 2025-01-04, v177.0.0 2025-04-10. "Gestalt 2.0" docs site launched 2025-11-21 | [S-L09-361] [S-L09-363] |
| Current version (Sept 2026) | `gestalt`, `gestalt-design-tokens`, `gestalt-charts` 177.0.12 (2025-12-09). A 177.0.13 bump (2026-01-07) is in git but not on npm | [S-L09-361] [S-L09-362] |
| Platforms | Web: open-source React components. iOS and Android: tokens only (Swift/ObjC and XML outputs); native component libraries are not public ("Android Tooling: Coming Soon!") | [S-L09-369] [S-L09-373] |
| Open source + license | Yes; Apache-2.0 | [S-L09-361] |
| Code frameworks | React (`gestalt`, `gestalt-charts`, `gestalt-datepicker`), plus `eslint-plugin-gestalt` and `stylelint-plugin-gestalt`. Tokens built with Style Dictionary | [S-L09-369] [S-L09-373] |
| Figma kit | Figma libraries are internal (Pinterest Figma org via SAML SSO). Public: Figma Community plugin "Pinterest Assets". Variables: not public | [S-L09-373] |
| Token tiers + naming | VR: 3 tiers base -> sema -> comp. `--base-color-red-300`, `--sema-color-background-primary`, `--sema-rounding-300`, `--comp-checkbox-*`. A web-mapping layer points classic names at VR (`--color-background-primary-base: var(--sema-color-background-primary)`). Classic: 2 tiers, `--color-red-pushpin-450` -> `--color-background-primary-base`, `--rounding-600`, `--space-400` | [S-L09-367] [S-L09-368] |
| Color model | VR: warm grayscale 12 steps (0-500) + 5 hues (blue, green, orange, purple, red) x 5 steps (100-500), with separate hover and pressed base ramps. Classic: 8 named hues x 12 steps (red-pushpin, blue-skycicle, green-matchacado, orange-firetini, pink-flaminglow, purple-mysticool, teal-spabattical, yellow-caramellow) + gray-roboflow 10 steps. sRGB hex. VR semantic roles (default state): 90 = 35 background, 15 border, 14 text, 14 icon, 12 data-viz. Primary Pinterest red `#e60023` | [S-L09-367] [S-L09-368] |
| Typeface | VR: 'Pin Sans' (custom), then -apple-system, BlinkMacSystemFont, Segoe UI, Roboto. Japanese: 'SF Pro JP' first. Mono: 'SF Mono', 'Segoe UI Mono', 'Roboto Mono'. Classic: system stack only | [S-L09-367] [S-L09-368] |
| Type scale | VR: 14 named styles: heading xxs/xs/sm/md/lg (14/16/20/28/36px), body xs/sm/md/lg (12/14/16/20), ui xs/sm/md/lg (12/14/16/20), compact xs (12). Body-md 16px / 22px. Weights 400 / 500 / 700. Line-height sets per script: default, tall, ck, ja, th, vi. Classic sizes 12/14/16/20/28/36px | [S-L09-367] [S-L09-370] [S-L09-368] |
| Spacing | Base unit 4px (`--base-space-unit`). `sema-space` 0, 25=1, 50=2, 100=4, 150=6, 200=8, then 4px steps: 300=12, 400=16 ... 1600=64px. Negatives mirror it. Classic `space-100`..`1600` = 4..64px | [S-L09-367] [S-L09-368] |
| Radius | `rounding` 0, 100=4, 200=8, 300=12, 400=16, 500=20, 600=24, 700=28, 800=32px, pill 999px, circle 50%. Buttons: classic 24px (`rounding-600`); VR sm 8px (24px tall), md 12px (32px), lg 16px (44px) | [S-L09-367] [S-L09-371] |
| Elevation | Shadows. VR 5 levels: surface `0 1px 2px rgba(0,0,0,.1), 0 0 1px .08`; raised-default `0 0 0 .5px .06, 0 1px 6px .1, 0 1px 2px .06`; raised-top; raised-bottom; floating `0 4px 16px .1, 0 1px 4px .08`. Classic 4: floating `0 0 8px .1`, raised-top `0 2px 8px .12`, raised-bottom, datepicker. Separate dark elevation sets | [S-L09-367] [S-L09-368] |
| Motion | VR durations 0, 50, 100, 150, 200, 300, 400, 500, 600, 700, 900ms. Easings: enter (0.05,0.7,0.1,1), exit (0.3,0,0.8,0.15), bounce (0,0.35,0,1.25), lateral (0.8,0,0.2,1), expressive (0.55,0,0,1), linear. Semantic: position-enter 300ms bounce, position-exit 300ms exit, swipe 400ms lateral, opacity 300ms linear, scale-on 150ms. Component motion tokens for checkbox, radio group, spinner. `useReducedMotion` utility documented | [S-L09-367] [S-L09-369] [S-L09-379] |
| Theming + modes | Light and dark (separate token files for classic and VR). Themes `classic` (default), `visualrefresh` (experiment VR01), `calico01` (experiment CA01; currently reuses VR tokens). Language line-height modes. Switched via providers and experiment flags | [S-L09-370] [S-L09-367] [S-L09-368] |
| Component count | 77 web component pages on gestalt.pinterest.systems/v1 (2026-09-23; sidebar links minus Overview and z-index classes) | [S-L09-365] |
| Component doc structure | Props, Usage guidelines, Best practices, Accessibility, Localization, Variants, Writing, Component quality checklist, Internal documentation, Related (plus "also known as") | [S-L09-366] |
| Accessibility stance | Conflict: accessibility page says Pinterest's goal is WCAG 2.2 AA; About page says WCAG 2.1 AA. 175 Playwright accessibility specs, one per docs page. PR checklist covers keyboard, screen reader, dark mode and RTL | [S-L09-372] [S-L09-369] [S-L09-363] |
| Governance / contribution | Central Pinterest team. Fork-and-PR process documented. Visual changes ship behind experiments (VR01, CA01) before becoming default | [S-L09-374] [S-L09-370] |
| Notable innovation | Per-script line-height token sets (tall, ck, ja, th, vi). Whole themes A/B-tested through the same components via experiment flags. "Component quality checklist" and Writing/Localization sections on every component page | [S-L09-370] [S-L09-366] |

## Visual signature: why it looks like this
- Pinterest red `#e60023` as the only strong fill, everything else gray/black -> the pins (user images) supply the color; chrome stays quiet. [S-L09-367] [S-L09-368]
- Classic pill-ish buttons (24px radius) -> bubbly, friendly consumer feel. VR moves to 8/12/16px rounded rectangles -> tidier, more "product" look. [S-L09-371]
- VR warm grays (`#fffef7`, `#f5f4ed`, `#e8e7e1`) vs classic neutral grays (`#f1f1f1`, `#e9e9e9`) -> VR reads warmer and more paper-like. [S-L09-367] [S-L09-368]
- Pin Sans with 16px/22px body and 500/700 headings -> brand-specific type with roomy reading text. [S-L09-367]
- Soft, diffuse shadows (0.5px ring + 6px blur at 10%) -> gentle lift for cards and pins, not hard edges. [S-L09-367]
- Bounce easing (0,0.35,0,1.25) on entrances -> playful overshoot that fits a consumer app. [S-L09-367]

## Recent changes 2024-2026
- 2024-05-23: final VR token files published for Android and iOS consumption. [S-L09-369]
- 2024-10-09 to 2024-11-20: VR motion shipped for RadioGroupButton, Checkbox and Spinner; component (XFN) tokens added 2024-10-16. [S-L09-369]
- 2025-04-10: v177.0.0, the latest major. [S-L09-361]
- 2025-11-21: new gestalt.pinterest.systems ("Gestalt 2.0") launched; legacy docs moved to `/v1` with a banner "Information might be outdated". The new home shows a Login link. [S-L09-363] [S-L09-364]
- 2025-12-09: 177.0.12, the last npm release. [S-L09-361]
- 2026-01-07: 177.0.13 bumped in git but never published. 2026-08-06: last commit (Google Analytics removed from docs). [S-L09-362]

## Builder takeaways
- Offer per-language line-height overrides (tall scripts, CJK, Thai, Vietnamese) as a first-class token mode, not an afterthought.
- Support two themes on one component set, with a mapping layer from old names to new ones. Gestalt's web-mapping file is a clean migration pattern.
- Add Writing, Localization and a quality checklist to the component doc template.
- Ask the user whether their brand color should be the only saturated fill (content-first, like Pinterest) or a full palette on surfaces.

## Gaps / unverified
- Gestalt 2.0 content sits behind a login; its tokens, components and whether VR is now the default could not be checked.
- Whether the React library is still actively developed is unclear: releases stopped in Dec 2025 and the new docs are not public.
- The WCAG target conflicts between two official pages (2.1 AA vs 2.2 AA).
- "Visual refresh" launch date for Pinterest's live product was not confirmed; only token and code dates are shown.
- Web search budget and Perplexity quota were exhausted, so no Tier B article corroborates the VR story.
