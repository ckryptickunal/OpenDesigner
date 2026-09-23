# GOV.UK Design System

_Lane L09 teardown. Verified against live sources on 2026-09-23. Every value carries an [S-L09-xxx] id from `traces/L09-trace.md` or the tag [inferred]._

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Owner | Government Digital Service (GDS), UK government; code copyright "Crown Copyright (Government Digital Service)" | [S-L09-520] |
| Launch and major versions | govuk-frontend 1.0.0 2018-06-21; 2.0.0 2018-09-10; 3.0.0 2019-07-29; 4.0.0 2021-12-16; 5.0.0 2023-12-08; 6.0.0 2026-02-09 | [S-L09-534] |
| Current version (Sept 2026) | govuk-frontend 6.5.1, 2026-09-14 (docs site footer still shows v6.5.0, 2026-08-27) | [S-L09-500] [S-L09-534] [S-L09-532] |
| Platforms | Web only (server-rendered HTML, progressive enhancement) | [S-L09-522] |
| Open source + license | Yes. Code MIT (Crown Copyright GDS); docs site under Open Government Licence v3.0 | [S-L09-520] [S-L09-532] |
| Code frameworks | HTML + Sass + vanilla JS, with Nunjucks macros (e.g. `govukHeader`). Sass modules via `@use` since 6.2.0. No official React package | [S-L09-502] [S-L09-501]; React absence [inferred] |
| Figma kit | No GDS-managed kit. The "GOV.UK Design System Figma Kit" on Figma Community is maintained by the MoJ Design System team. GitHub issue #4437 "Explore ways the Figma library can be formally managed by GDS" open since 2025-01-13. Variables: unknown | [S-L09-524] [S-L09-528] [S-L09-526] |
| Token tiers + naming | 2 tiers in Sass. Palette: `govuk-colour("blue", $variant: "tint-25")`. Functional: `govuk-functional-colour(brand)`, `(text)`, `(focus)`, `(link-hover)`. Spacing: `govuk-spacing(0..9)`. CSS custom properties emitted by default (`$govuk-output-custom-properties: true`) | [S-L09-502] [S-L09-504] [S-L09-505] [S-L09-506] |
| Color model | sRGB hex. 11 palette colours (blue, green, teal, purple, magenta, red, orange, yellow, brown, black, white), each with tint-25/50/80/95 and shade-25/50 (blue also shade-10). 21 functional colours. Accent is a fixed brand blue #1d70b8, not generated | [S-L09-504] [S-L09-505] |
| Typeface | GDS Transport (custom, restricted: "must use" on service.gov.uk subdomain). Stack `"GDS Transport", arial, sans-serif`. Weights 400 and 700 only. No mono or display face | [S-L09-514] [S-L09-510] |
| Type scale | 7 sizes named by desktop px: 80, 48, 36, 27, 24, 19, 16. Body 19px/25px at all breakpoints (v6 scale). Mobile/tablet: 80 = 53/55 -> 80/80; 48 = 32/35 -> 48/50; 36 = 27/30 -> 36/40; 27 = 21/25 -> 27/30; 24 = 21/25 -> 24/30; 16 = 16/20. Size 14 removed in 6.0.0. Hand-tuned, responsive at 641px | [S-L09-507] [S-L09-502] [S-L09-511] |
| Spacing | 5px base. Static `govuk-spacing` 0-9 = 0, 5, 10, 15, 20, 25, 30, 40, 50, 60px. Responsive scale 4-9 shrinks on mobile: 15->20, 15->25, 20->30, 25->40, 30->50, 40->60px. Page width 960px, gutter 30px | [S-L09-508] [S-L09-509] |
| Radius | 0 everywhere. Button `border-radius: 0` | [S-L09-531] |
| Elevation | None. Flat surfaces separated by borders: form elements 2px, standard 5px, wide 10px, narrow 4px. Only "shadow" is the button's solid 2px bottom edge (`0 2px 0` darker colour); active state drops the button 2px | [S-L09-509] [S-L09-531] |
| Motion | Not public. No duration or easing tokens in the settings folder | [S-L09-503]; absence [inferred] |
| Theming + modes | Light only. No dark mode or density mode documented. Single refreshed blue-based GOV.UK brand (default since 6.0.0). Organisation colour palette for departments. Generic header (6.3.0) for non-GOV.UK services, with brand-colour borders | [S-L09-515] [S-L09-502] [S-L09-501] |
| Component count | 37 components + 30 patterns (10 "Ask users for", 12 "Help users to", 8 "Pages"); counted from the components and patterns index pages on 2026-09-23 | [S-L09-512] [S-L09-513] |
| Component doc structure | When to use this component, How it works (with variants), Research on this component, Recent changes, Help improve this component (GitHub discussion). Many pages add "When not to use this component" | [S-L09-516]; "When not to use" [inferred] |
| Accessibility stance | WCAG 2.2 AA (supported since Dec 2023). Testing with screen readers, magnifiers, speech recognition, high-contrast modes (Assistiv Labs, macOS, Windows). jest-axe and axe-core in CI. Works without JavaScript first. Text contrast must meet 1.4.3 AA | [S-L09-522] [S-L09-515] |
| Governance / contribution | Central GDS team, open community backlog on GitHub. Proposal criteria: Useful, Unique. Publication criteria: Usable (tested incl. disabled users), Consistent, Versatile. Reviewed by the Design System team (current page no longer names a "working group"). "Trial" status tag added 6.5.0 | [S-L09-517] [S-L09-501] |
| Notable innovation | Evidence-first docs ("Research on this component" on every page). Yellow #ffdd00 focus with a 4px black underline, copied by many gov systems. Pattern library for whole questions ("Ask users for...") not only widgets | [S-L09-516] [S-L09-529] [S-L09-513] |

## Visual signature: why it looks like this
- GDS Transport at 400/700 only, body 19px/25px on every screen -> big, plain, signage-like text. No weight in between, so hierarchy comes from size [S-L09-510] [S-L09-507].
- Radius 0 plus no shadows -> hard rectangles; the page reads as a printed form, not an app [S-L09-531].
- Thick black borders (2px inputs, 5px/10px accent bars) instead of fills -> high-contrast, "government paper" feel [S-L09-509].
- Almost no colour on surfaces: text #0b0c0c on white, template background #f4f8fb, one brand blue #1d70b8, links #1a65a6 -> calm and neutral, colour kept for meaning [S-L09-505].
- Focus = yellow #ffdd00 fill + `0 4px` black underline (text) or 4px yellow + 8px black ring (boxes) -> the loudest thing on the page is where the keyboard is [S-L09-529].
- Green button (hover green shade-25 #0b5c3e, bottom edge green shade-50 #083d29) with a 2px solid bottom edge that "presses" 2px on click -> one flat, tactile call to action per page [S-L09-531] [S-L09-555].

## Recent changes 2024-2026
- 2024-02-05: 5.1.0 adds the Tudor Crown; 2024-02-21: 5.2.0 makes it default and adds the new type scale as opt-in [S-L09-519] [S-L09-534].
- 2025-03-04: 5.9.0 moves service name and nav out of the header into Service navigation [S-L09-519] [S-L09-534].
- 2025-05-01: 5.10.0 ships the `govukRebrand` flag ahead of the 25 June 2025 GOV.UK brand refresh (new logo, crown in footer); new organisation colours in 5.10-5.11 [S-L09-519] [S-L09-534].
- 2025-06-24: 5.11.0 lands the day before brand go-live; the legacy organisation palette is deprecated [S-L09-519] [S-L09-534].
- 2025-10-10: 5.13.0 adds Sass functions for custom media queries; `ellipses` class renamed `ellipsis` [S-L09-519] [S-L09-534].
- 2026-01-14: 5.14.0 lets the footer drop the content licence text [S-L09-519] [S-L09-534].
- 2026-02-09: 6.0.0. Refreshed blue-based brand becomes the only brand. New type scale default, size 14 removed. Palette v1.0: green #00703c -> #0f7a52, red #d4351c -> #ca3535, purple #4c2c92 -> #54319f, turquoise -> teal #158187, pink -> magenta #ca357c; light/dark variants replaced by tints and shades. `govuk-functional-colour()` replaces `$govuk-*-colour` variables. Dart Sass 1.79+ required [S-L09-502].
- 2026-03-02: 6.1.0 replaces `_<component>.scss` files with `_index.scss` and adds asset-URL functions [S-L09-501].
- 2026-06-02: 6.2.0 Sass modules (`@use`); 2026-06-23: 6.3.0 Generic header; 2026-07-16: 6.4.0 Interruption panel [S-L09-501] [S-L09-534].
- 2026-08-27: 6.5.0 adds Trial status, Language navigation and Feedback components [S-L09-501].

## Builder takeaways
- Offer a "public service" preset: radius 0, no shadows, 2 weights, 19px body, 5px spacing base, yellow focus ring. It is a proven, legally-defensible accessible baseline.
- Copy the two-tier colour API (palette with tint/shade variants -> named functional roles). It is small enough for non-designers.
- Copy the doc template: "When to use / When not to use / How it works / Research / Recent changes". Ask the user for evidence, not only visuals.
- Ask if the brand has a restricted typeface. GOV.UK shows the pattern: custom face on owned domains, Arial fallback elsewhere.

## Gaps / unverified
- Figma kit variables support not checked (Figma Community page returned 403).
- No motion values: none found in settings; component-level transitions not audited.
- "When not to use this component" not confirmed on the Button page; seen on other pages in memory only.
- Owner's parent department (GDS moved into DSIT in 2023) not re-verified, so left out.
- The functional-colour summary said "19" but listed 21 names; 21 is my count of the listed names.
- The accessibility strategy page was last updated July 2024; audits after that were not checked.
- CSS custom property names emitted by v6 were not listed; only the on/off setting was confirmed.
- Layout values (960px page, 30px gutter, breakpoints 320/641/769px) are confirmed [S-L09-509] [S-L09-511], but grid widths per breakpoint were not checked.
