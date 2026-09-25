# Duet (LocalTapiola and Turva)

_Lane L09 teardown. Checked on 2026-09-25 against public documentation and `@duetds/tokens` 5.1.5. This is comparative research, not a recommendation to reuse the proprietary package or brand assets._

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Owner / purpose | LocalTapiola's internal core team; two brand themes for LocalTapiola and Turva | [S-L09-807] |
| Release | Token package `@duetds/tokens` 5.1.5. This is not the component package or documentation site's version | [S-L09-808] |
| License | Restricted use for work on behalf of LocalTapiola; not a generally reusable open-source token library | [S-L09-809] [S-L09-807] |
| Platforms | Web Components; documentation describes framework-independent use and a React wrapper | [S-L09-807] [S-L09-814] |
| Token names / outputs | CSS custom properties and Sass, Less, Stylus, CommonJS, JSON, iOS JSON, Android XML and Figma Tokens Studio exports. JS uses camelCase; JSON snake_case | [S-L09-810] |
| Color | Published legacy `color_primary`: rgb(0,119,179); Turva counterpart rgb(230,23,64). Dark variants rgb(0,75,129) and rgb(140,0,30). These are brand variants, not a light/dark UI mode | [S-L09-811] |
| Typeface | Heading and body begin with `localtapiola-sans`, or `turva-sans` for Turva; system-font fallbacks follow. Typeface files are not copied here | [S-L09-811] [S-L09-812] |
| Type scale | Base 16px. Sizes .75 / .875 / 1 / 1.25 / 1.5 / 2.25 / 3 / 4.5rem; paragraph 1rem. At the documented root this is 12 / 14 / 16 / 20 / 24 / 36 / 48 / 72px | [S-L09-812] |
| Weight | normal 400, semi-bold 600, bold 700, extra-bold 800 | [S-L09-811] |
| Spacing | Documented scale: 2 / 4 / 8 / 12 / 16 / 20 / 28 / 36 / 48 / 72px. Inset, inset-squish, stack and inline patterns describe where spacing belongs | [S-L09-813] |
| Radius | sharp 0, default 4px, medium 8px, intermediate 12px, large 16px, pill 20rem, circle 50% | [S-L09-811] |
| Elevation | Default shadow `0 2px 6px 0 rgba(0,41,77,.07)`; Turva uses the same geometry with `rgba(117,117,117,.13)` | [S-L09-811] |
| Motion | `transition_quickly` = `300ms ease`; `transition_slowly` = `600ms ease` | [S-L09-811] |
| Theming | Brand choice can be global or per component. The two themes do not establish support for a user dark-mode preference | [S-L09-807] [inferred] |
| Accessibility stance | About page states WCAG 2.1 support; accessibility page lists checklist categories including keyboard, forms, contrast and mobile. No independent conformance test was performed | [S-L09-807] [S-L09-815] |

## Visual signature: why it looks like this

- Two related brands share geometry while changing color, font family and shadow tint. This is a useful example of a brand axis rather than a dark-mode axis. [S-L09-807] [S-L09-811] [inferred]
- Spacing uses 28 and 36px where a power-of-two-derived scale might choose 32px. Preserve actual values instead of rounding a reference into a familiar scale. [S-L09-813] [inferred]
- Spacing patterns encode relationships: stack and inline separate siblings; inset controls the inside of a container. A single generic gap value cannot express all four. [S-L09-813] [inferred]

## Version notes and coverage differences

The published token JSON also contains `space_xxxxx_large = 94px`, while the spacing guide's table stops at 72px. Record 94px as an additional shipped token, not as a documented preferred spacing step. The table above uses the documented scale. [S-L09-811] [S-L09-813]

Public documentation and npm availability do not make the full Duet package open source. The license and About page restrict its intended use. For OpenDesigner, the transferable evidence is the relationship between decisions, not permission to distribute Duet code or identity. [S-L09-809] [S-L09-807] [inferred]

## Builder takeaways

- Model brand, density and user preferences as separate decisions. [inferred]
- Preserve both recommended values and additional shipped values with their provenance. [inferred]
- Borrow the distinction between inset/stack/inline relationships without copying proprietary assets. [inferred]

## Gaps / unverified

No component count, launch history, Figma variable inventory or browser runtime test was performed. The Figma export format was documented but not imported. A complete dark-mode/reduced-motion policy was not established from the inspected sources.
