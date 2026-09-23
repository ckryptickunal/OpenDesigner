# Twilio Paste

_Lane L09 teardown. Verified against live sources on 2026-09-23. Every value carries an [S-L09-xxx] id from `traces/L09-trace.md` or the tag [inferred]._

> Status note (Sept 2026): the docs site paste.twilio.design was retired on 2026-07-31 and now redirects to the GitHub repo. The last npm release was `@twilio-paste/core` 21.5.0 on 2025-08-25. Since then the repo has had only chore commits. Treat Paste as maintained-but-frozen [inferred from release and commit history].

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Owner | Twilio (Paste design systems team), repo `twilio-labs/paste` | [S-L09-347] |
| Launch and major versions | `@twilio-paste/design-tokens` first on npm 2019-08-15; `@twilio-paste/core` 0.1.0 2019-10-29, 1.0.0 2019-11-11. Core majors are frequent (v2 2020 ... v20 2023-08-11); v21.0.0 2025-03-19 (React 19, drops React 16) | [S-L09-351] [S-L09-360] |
| Current version (Sept 2026) | `@twilio-paste/core` 21.5.0 (2025-08-25); `@twilio-paste/design-tokens` 10.15.0 (2025-08-13) | [S-L09-351] |
| Platforms | Web (React). Token package also emits Android XML and iOS JSON per theme | [S-L09-352] |
| Open source + license | Yes; MIT | [S-L09-347] |
| Code frameworks | React only (supports the 3 latest React majors) | [S-L09-360] |
| Figma kit | "Twilio Paste Components" on Figma Community (file 1207476064127503112). Variables: yes, with the most-used themes as variable modes. Fonts: Inter + Twilio Sans Mono | [S-L09-359] |
| Token tiers + naming | 2 tiers: alias palette (`palette-blue-60`) -> global semantic tokens. Grammar `{category}-{property}-{variant}-{weight}`. Semantic: `--color-background-primary`, `--color-text-weak`, `--shadow-border-weak`, `--space-40`, `--border-radius-30`. JS camelCase (`colorBackgroundPrimary`). No component tier; per-component overrides go through CustomizationProvider `elements` | [S-L09-354] [S-L09-352] [S-L09-359] |
| Color model | 7 hue ramps (blue, gray, green, orange, purple, red, yellow), steps 05 and 10-100, with extras (blue-55, orange-65, red-65, gray 15/55/75/85/95/110). sRGB hex. Semantic roles: 72 background + 62 text + 50 border (+10 data-viz). Primary `#0263e0` (blue-60); brand `#001489`; brand highlight `#f22f46` | [S-L09-354] [S-L09-352] |
| Typeface | Default theme: 'Inter var experimental', 'Inter var', then system stack. Twilio theme: TwilioSansText / TwilioSansDisplay. Code: TwilioSansMono. Separate stacks for Japanese, Korean, Chinese (traditional, simplified) | [S-L09-352] |
| Type scale | 11 sizes: 10, 12, 14, 16, 18, 20, 24, 28, 32, 40, 48px (`font-size-10`..`110`). Line heights 12-64px (`line-height-05`..`110`). Weights 400 / 400 / 500 / 600 / 700 / 800 (light = normal = 400). No composite style tokens. Buttons 14px / 20px semibold | [S-L09-352] [S-L09-356] |
| Spacing | 4px grid with a 2px half step: `space-10` 2, `20` 4, `30` 8, `40` 12, `50` 16, `60` 20, `70` 24, `80` 28, `90` 32, `100` 36, `110` 40, then +4px per step to `space-310` 120px (32 steps). 20 negative steps | [S-L09-352] |
| Radius | 0, `10` 2px, `20` 4px, `30` 8px, `40` 12px, `50` 16px, `60` 20px, `70` 24px, `80` 28px, `90` 32px, pill 100px, circle 50%. Button radius 8px (`borderRadius30`) | [S-L09-352] [S-L09-356] |
| Elevation | Shadows plus "shadow borders". `shadow-low` `0 2px 8px rgba(18,28,45,.1)`, `shadow` `0 4px 16px .2`, `shadow-high` `0 16px 24px .2`, `shadow-card`, `shadow-elevation-05/10/20` (+ top/bottom/left/right, inverse). 68 `shadow-border-*` tokens: inputs draw borders with box-shadow. Focus ring `0 0 0 4px rgba(2,99,224,.7)` | [S-L09-352] [S-L09-356] |
| Motion | No motion tokens. Animation library wraps react-spring. Modal: spring mass 0.5, tension 370, friction 26, scale 0.675 -> 1. Button: 100ms ease-in color/shadow transitions. `useReducedMotion` hook; server render treated as reduced (animations off) | [S-L09-355] [S-L09-356] |
| Theming + modes | `Theme.Provider theme=` 'default', 'dark', 'twilio', 'twilio-dark', 'evergreen' (Segment). Token package also ships 'sendgrid'. `CustomizationProvider` takes `baseTheme` (default or dark) plus token overrides and per-element styles | [S-L09-358] [S-L09-353] [S-L09-359] |
| Component count | 86 component doc pages on main (2026-09-23, counted from `paste-website/src/pages/components`). Packages: 81 components + 11 primitives + 5 layout | [S-L09-353] |
| Component doc structure | Tabs: Guidelines / API / Changelog. Guidelines: About (with an Accessibility subsection), Examples, States, Composition notes, Do and don't | [S-L09-357] [S-L09-353] |
| Accessibility stance | Ship gate: no component "if it does not meet or surpass our target of WCAG 2.1 AA". Text 4.5:1, icons 3:1, with separate `color-text-icon-*` tokens | [S-L09-358] |
| Governance / contribution | Anyone at Twilio can contribute; the core team assigns a designer and engineer to help. Proposals via GitHub Discussions; a changeset per package change | [S-L09-359] [S-L09-347] |
| Notable innovation | Named-element customization: `CustomizationProvider elements={{CARD: {...}}}` restyles any component part by name, for white-label customer UIs. Also dedicated AI UI components (AI Chat Log, already at v2 by 2025-03, expanded 2025-08) | [S-L09-359] [S-L09-360] |

## Visual signature: why it looks like this
- Navy-tinted neutrals (text `rgb(18,28,45)`, gray-10 `#f4f4f6`, gray-20 `#e1e3ea`, borders `#8b93aa`) -> cool blue-gray chrome that matches Twilio's navy brand. [S-L09-352]
- Saturated primary `#0263e0` plus brand navy `#001489`, with red `#f22f46` held back as a highlight -> confident blue product UI with a small red brand spark. [S-L09-352]
- Borders drawn with box-shadow tokens (`shadow-border`, `shadow-border-primary` on hover) -> border color and weight change on hover and focus without layout shift. [S-L09-356]
- 14px/20px semibold button text, 8px/12px padding, 8px radius -> compact but friendly controls. [S-L09-356]
- 4px focus ring at 70% blue -> very visible keyboard focus, in line with the a11y gate. [S-L09-352] [S-L09-358]
- Spring-driven overlays (modal grows from 0.675 scale) -> lively entrances with a short settle. [S-L09-355]

## Recent changes 2024-2026
- 2025-03-19: core 21.0.0 upgrades all packages to React 19 and drops React 16. [S-L09-360]
- 2025-07-31: Footnote component added. 2025-08-22: new AI Chat Log components. [S-L09-347]
- 2025-08-25: core 21.5.0, the last npm release as of Sept 2026. [S-L09-351]
- 2026-07-01/02: banner added: "paste.twilio.design website will be retired on July 31, 2026"; docs stay in the GitHub project. [S-L09-349]
- 2026-08-20: Cypress removed (chore). [S-L09-347]
- Sept 2026: paste.twilio.design 301-redirects to github.com/twilio-labs/paste. [S-L09-348]
- Sept 2026: the repo's homepage field points to paste-dsys.com, which calls itself an independent fork "not affiliated with ... Twilio". Not used as a source. [S-L09-347] [S-L09-350]

## Builder takeaways
- Copy named-element customization: give every component part a stable name so a theme can restyle it without forking.
- Offer "shadow borders" as a preset option for inputs and cards when the user wants hover/focus border changes with no layout shift.
- Make the a11y gate explicit in the builder (text 4.5:1, icon 3:1) and split text vs icon color tokens.
- Ask the user about the docs hosting plan. Paste shows a system can outlive its docs site; docs kept in the repo survive.

## Gaps / unverified
- Why Twilio retired the docs site is not stated in the PRs; "maintained-but-frozen" is an inference from releases and commits.
- Default body text size (14px vs 16px) was not confirmed from the Paragraph component; only Button text was checked.
- Whether the SendGrid token theme is still supported is unclear: it ships in the token package but not in the `Theme.Provider` enum.
- Why the official repo's homepage field points to a third-party fork is unknown; this is a conflict worth flagging.
- The component count on the retired docs site could not be checked live; the count comes from the repo's docs source.
