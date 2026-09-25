# GC Design System

_Lane L09 teardown. Checked on 2026-09-25. This is a token-level snapshot of `@cdssnc/gcds-tokens` 2.14.0. Pixel equivalents assume a 16px root; rem and percentage values remain the source of truth._

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Identity | GC Design System tokens; repository `cds-snc/gcds-tokens`. README describes a shared visual language for Government of Canada requirements | [S-L09-827] [S-L09-828] |
| Current version / license | `@cdssnc/gcds-tokens` 2.14.0; MIT | [S-L09-827] |
| Distribution | Style Dictionary build; standalone CSS/SCSS imports or tokens supplied with GCDS components/utilities | [S-L09-828] |
| Token tiers + naming | Base, global and component tokens; `--gcds-` prefix. Global tokens express intended roles; component tokens should not be reused as global defaults | [S-L09-829] |
| Color | Text primary `#333333`, secondary `#43474e`; primary background `#26374a`, light background `#f1f2f3`; links default `#284162`, hover `#0535d2`, visited `#7532b8` | [S-L09-830] |
| Focus | Focus background and border `#0535d2`, focus text `#ffffff`; these are separate roles from ordinary links and text | [S-L09-830] |
| Typeface | Heading Lato, body Noto Sans, monospace Noto Sans Mono, each with its corresponding generic fallback | [S-L09-831] |
| Body typography | Text desktop 1.25rem / 160%, mobile 1.125rem / 155%; small text desktop 1.125rem / 155%, mobile 1rem / 150% | [S-L09-832] [S-L09-833] |
| Heading scale | Desktop h1-h6: 2.5625 / 2.4375 / 1.8125 / 1.6875 / 1.5 / 1.375rem. Mobile: 2.3125 / 2.1875 / 1.625 / 1.5 / 1.375 / 1.25rem | [S-L09-832] |
| Spacing | Small steps include .125 / .25 / .375 / .5 / .625 / .75 / .875rem. `spacing-200` = 1rem, `400` = 2rem, `600` = 3rem, `1250` = 6.25rem. Numeric suffixes are not pixel values | [S-L09-834] |
| Radius | sm .125rem, md .375rem, lg 3rem, xl 100%; at the assumed root these are 2px, 6px, 48px and a percentage | [S-L09-835] |
| Border width | sm .0625rem, md .125rem, lg .25rem, xl .375rem (1 / 2 / 4 / 6px at the assumed root) | [S-L09-835] |
| Responsive typography | Distinct desktop/mobile font-size and line-height tokens, rather than a single global scaling factor | [S-L09-832] [S-L09-833] |
| Documentation / governance | Bilingual English/French README, standalone token instructions and contribution section | [S-L09-828] |

## Visual signature: why it looks like this

- 1.25rem desktop body text with 160% line height gives reading content more room than a typical compact data table. This is a design comparison, not a user-study result. [S-L09-832] [S-L09-833] [inferred]
- Headings and body use different families while links retain a visited color. The system supports content navigation as well as action controls. [S-L09-830] [S-L09-831] [inferred]
- The radius scale is purposefully non-linear: a 3rem large radius and a 100% extra-large value should not become a formula extrapolated from 2px and 6px. [S-L09-835] [inferred]

## Version notes and interpretation

The live design-token page illustrates three levels of indirection and warns that component tokens can change with the component. Record those roles separately from the resolved palette. The package README still includes a link using the older `design-system.alpha.canada.ca` host; this entry uses the current official documentation and version-pinned package files for values. [S-L09-828] [S-L09-829]

## Builder takeaways

- Ask whether the interface primarily serves reading/form completion or dense operational work before choosing a body size. [inferred]
- Keep mobile body and heading sizes explicit; do not infer them from a blanket percentage. [inferred]
- Export semantic global tokens for application styling and keep component-specific values scoped. [S-L09-829] [inferred]

## Gaps / unverified

This pass did not audit component behavior, certify accessibility conformance, inspect a Figma kit, or establish a dark-mode or motion policy. The token package is not a complete application. No component count, launch-date history or usage metric is inferred from the files inspected.
