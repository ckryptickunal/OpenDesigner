# Workday Canvas

_Lane L09 teardown. Checked on 2026-09-25. This snapshot describes Canvas Tokens Web 4.5.0, not every Canvas Kit component. Pixel equivalents assume a 16px root; the shipped values remain in rem._

## Snapshot (this block feeds the benchmark matrix; keep one line per field)

| Field | Value (real values, not adjectives) | Evidence |
|---|---|---|
| Owner / distribution | Workday; `@workday/canvas-tokens-web` 4.5.0. Package exports CommonJS, ES modules and declarations, and includes CSS, Less and SCSS | [S-L09-767] |
| License | Token package: CC BY-ND 4.0. Do not infer the license of other Canvas packages from this entry | [S-L09-767] [S-L09-768] |
| Token tiers + naming | `base`, `sys`, `brand` and `component` source namespaces; CSS uses `--cnvs-*`. System values reference base values; brand primary references the blue palette | [S-L09-769] [S-L09-770] [S-L09-771] |
| Color model | Base palette uses OKLCH, including alpha colors. Blue-600 is `oklch(0.5198 0.1782 256.11 / 1)`; `brand.primary.600` aliases it. This is a brand primitive, not a universal text color | [S-L09-769] [S-L09-771] |
| Typeface | Default Roboto, mono Roboto Mono, global Noto Sans. Numeric weight tokens 300 / 400 / 500 / 700 | [S-L09-769] [S-L09-772] |
| Type scale | `body.sm/md/lg`: 1 / 1.125 / 1.25rem; `heading.sm/md/lg`: 1.5 / 1.75 / 2rem; `title.sm/md/lg`: 2.5 / 3 / 3.5rem. Body-small line height 1.5rem | [S-L09-770] [S-L09-773] |
| Spacing | Named gap tokens `none/xs/sm/md/lg/xl/xxl`: 0 / .25 / .5 / 1 / 1.5 / 2 / 4rem. Thus 0 / 4 / 8 / 16 / 24 / 32 / 64px at the assumed root | [S-L09-770] [S-L09-772] [S-L09-773] |
| Radius | `shape.sm/md/lg/xl/xxl/xxxl`: .25 / .5 / .75 / 1 / 1.5 / 2rem. `shape.full` is `base.size.75 * 100`, or 37.5rem; it is not a percentage | [S-L09-770] [S-L09-772] [S-L09-773] |
| Elevation | Six depth levels. Depth 1 combines offsets .0625rem and .125rem with .25rem and .5rem blur, respectively; colored OKLCH shadows rather than a single opaque gray | [S-L09-773] |
| Motion | Base durations 50 through 1000ms in 50ms steps. Quick standard easing `cubic-bezier(0.2, 0, 0.2, 1)` | [S-L09-772] |
| Compatibility | Published CSS includes both old `space.x*` / `shape.x*` names and newer gap/padding / named shape tokens. The two vocabularies must not be mixed by suffix alone | [S-L09-773] |
| Governance | Contributions welcome; README promises support only for the latest major token package | [S-L09-768] |

## Visual signature: why it looks like this

- Separate gap roles and progressively rounded container shapes allow spacing and shape to change independently. Using one multiplier for both would erase this distinction. [S-L09-770] [inferred]
- The body starts at 1rem while titles reach 3.5rem; this offers a wider hierarchy than simply enlarging a compact table font. [S-L09-770] [inferred]
- Brand colors are aliases rather than duplicated hex values. Keep the role indirection when adapting a theme; do not copy Workday's identity into an unrelated product. [S-L09-771] [inferred]

## Version notes and disagreements

The source JSON retains `deprecatedValues.v3` names. The 4.5.0 archive still ships compatibility variables, so finding `shape.x2` in CSS does not mean it is the new `shape.md` naming scheme. For example, published `shape.x2` computes from the legacy base unit; `shape.md` references `base.size.100`. The values and names should be recorded together. This teardown checked the published archive as well as the pinned source files. [S-L09-770] [S-L09-773]

## Builder takeaways

- Treat density, typography and corner shape as separate decisions. [inferred]
- Preserve both semantic aliases and their primitive resolutions in exported research evidence. [inferred]
- Record the package version alongside token names; a migration alias is not evidence that a token disappeared. [inferred]

## Gaps / unverified

Component inventory, Canvas Kit release, Figma variables, runtime theme switching and accessibility conformance were not audited. This is a token-level benchmark, not a tested application or a license grant to redistribute Workday assets.
