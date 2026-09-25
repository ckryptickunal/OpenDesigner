# AWS Cloudscape

_Lane L09 teardown. Checked on 2026-09-25. Token values are from `@cloudscape-design/design-tokens` 3.0.113, including its visual-refresh JSON; they are not promises about earlier Cloudscape releases._

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Owner / history | Amazon Web Services; package README dates the system's creation to 2016 and describes use in AWS web applications | [S-L09-797] |
| Release / license | `@cloudscape-design/design-tokens` 3.0.113; Apache-2.0 | [S-L09-798] [S-L09-797] |
| Platforms | Web; React component repository. This package supplies design values separately from components | [S-L09-797] [S-L09-805] |
| Token structure | Semantic kebab-case keys, `$value` and `$description`; values may be scalar or maps for light/dark, comfortable/compact or default/disabled motion. JSON also contains context overrides | [S-L09-799] |
| Color | Main background light/dark `#ffffff` / `#161d26`; body text `#0f141a` / `#c6c6cd`; default links and primary button background `#006ce0` / `#42b4ff` | [S-L09-799] |
| Typeface / type scale | Open Sans first, then Helvetica Neue, Roboto, Arial, sans-serif. Body-m 14px/20px, body-s 12px. Heading xs/s/m/l/xl: 14/16/18/20/24px | [S-L09-799] [S-L09-800] |
| Spacing | Documented scale 2 / 4 / 8 / 12 / 16 / 20 / 24 / 32 / 40px. It includes a 2px half-step despite the 4px grid description | [S-L09-801] |
| Density | `space-scaled-m` comfortable 16px, compact 12px; `space-static-m` remains 16px in both. Container horizontal padding remains 20px in both modes | [S-L09-799] |
| Radius | Button 20px, input 8px, container 16px | [S-L09-799] |
| Motion | Responsive 115ms, expressive 165ms, complex 250ms; each has a disabled value of 0ms. Responsive easing `(0,0,0,1)` | [S-L09-799] [S-L09-802] |
| Contexts | JSON lists compact-table, top-navigation, header, app-layout-toolbar, flashbar, flashbar-warning, alert and alert-header; these are contexts, not eight global themes | [S-L09-799] |
| Accessibility stance | Component-specific accessibility guidance includes ARIA naming, localized labels and landmarks. Consumers still need to assemble and test an accessible app | [S-L09-803] |
| Governance / contribution | Public issues and discussions; package README points to contribution, support and versioning guidance | [S-L09-797] |

## Visual signature: why it looks like this

- Compact text and separately controlled density suit data-heavy operational screens without requiring every horizontal margin to shrink. [S-L09-799] [inferred]
- Different radii for controls, buttons and containers create a hierarchy that a single global corner slider cannot faithfully reproduce. [S-L09-799] [inferred]
- Motion can be turned off through token values while retaining the same semantic duration names. [S-L09-799] [inferred]

## Version notes and interpretation

The spacing guidelines call this a 4px grid and also list a 2px token. Treat the documented scale as the authority rather than generating only multiples of four. Likewise, do not infer compact-mode values by multiplying every space by one constant: static spacing remains fixed, while scaled spacing changes by role. [S-L09-801] [S-L09-799]

The design-token documentation explains how to consume the tokens. A numeric benchmark should record resolved values and the package version; copying generated CSS variable identifiers into an unrelated system would couple it to implementation details. [S-L09-804] [inferred]

## Builder takeaways

- Represent color mode, density and motion preference as separate axes. [inferred]
- Offer fixed outer structure plus compact internal spacing for operational interfaces. [inferred]
- Preserve component roles when recommending radius, rather than averaging 8, 16 and 20px into one default. [inferred]

## Gaps / unverified

No browser rendering, Figma inspection, component count or complete shadow inventory was performed. Disabled motion values are evidence of token support, not a test that every consumer honors reduced motion. Package values can vary by context; this table records the top-level values unless a row says otherwise.
