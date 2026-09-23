# design/ (agent D1): starter tokens, review atlas, Figma plan

Everything here is generated from `design/tokens/*.tokens.json`: the tokens, the four HTML artboards and the Figma scripts. Change a token, rerun the three builders, and every output stays in step.

```
python3 design/tokens/build_tokens.py            # writes the token files, the resolver and contrast-pairs.json
python3 design/tokens/check_contrast.py --write  # verifies them and records each ratio (exits 1 on any failure)
python3 design/atlas/build_atlas.py              # writes the 4 artboards from the resolved tokens
python3 design/figma-scripts/build_scripts.py    # writes the use_figma scripts and atlas/paper-tokens.json
```

## Files

| Path | What it is |
|---|---|
| `tokens/color.primitives.tokens.json` | 6 hues (neutral, accent, success, warning, danger, info) × 12 steps × separate light and dark ramps, plus white and black. DTCG 2025.10 color objects in OKLCH with a `hex` fallback |
| `tokens/color.light.tokens.json`, `color.dark.tokens.json` | 59 semantic color roles (surface, text, bg, border, icon, overlay, shadow), with the same names in both modes |
| `tokens/spacing.tokens.json` | Spacing primitives (`space.025`-`space.1200`), layout spacing, control, icon and target sizes |
| `tokens/spacing.comfortable.tokens.json`, `spacing.compact.tokens.json` | Semantic `space.inset.*` and `space.gap.*` per density |
| `tokens/radius.tokens.json` | Radius scale and roles, border widths, focus ring |
| `tokens/typography.tokens.json` | Families, weights, 9 sizes, 8 line heights, 15 `typography` composites (each with use / avoid in `$extensions`) |
| `tokens/elevation.tokens.json` | `shadow.raised` and `shadow.overlay`, whose colors alias theme tokens |
| `tokens/motion.tokens.json`, `motion.standard.tokens.json`, `motion.reduced.tokens.json` | Durations and easings, plus transitions per motion mode |
| `tokens/design-system.resolver.json` | DTCG Resolver 2025.10: foundation set + `theme` × `density` × `motion` modifiers = 8 permutations |
| `tokens/contrast-pairs.json` | 126 text/background claims with their computed ratios |
| `tokens/build_tokens.py`, `check_contrast.py` | Generator and verifier (stdlib only) |
| `atlas/01-building-blocks-map.html` | The 9 layers from context to governance, plus the 10 "Do you have this?" designer hooks with accepted formats and fallback paths |
| `atlas/02-foundations.html` | Ramps and semantic roles in light and dark, type scale, spacing, radius, elevation, motion; each block has a use / avoid note |
| `atlas/03-button.html` | Anatomy at 3x, 5 variants × 6 states in both modes, sizes, token map, usage rules |
| `atlas/04-builder-concept.html` | The builder's spacing block editor, with 6 annotated ideas |
| `atlas/build_atlas.py` | Artboard generator |
| `atlas/paper-tokens.json` | 158 CSS variables for Paper's `create_tokens` (light values; dark values carry a `-dark` suffix) |
| `figma-plan.md` | Run sheet for the remote Figma MCP |
| `figma-scripts/00-14*.js`, `build_scripts.py` | 15 ordered, idempotent `use_figma` scripts and their generator |

`atlas/paper_plan.py` was not written by D1. It chunks an artboard into Paper `write_html` calls and parses all four artboards (8, 29, 9 and 9 writes, largest 14 KB).

## Design direction

**An engineer's instrument: calm, precise and quiet, so the user's decisions are the loudest thing on screen.** Cool neutrals are tinted toward one indigo-blue accent. The accent appears only on actions, selection, focus and the edited token. The type is Inter plus a mono for token names. There are no gradients, and depth is used only where things float.

Why:
- The brief asks engineers to make visual decisions, so the chrome must not compete with the preview.
- L15 favors a strict emphasis budget (one dominant element, one primary action, 2-3 text colors) for app surfaces (DC-L15-03).
- L16's strongest pattern is a live preview on real components with every mode visible, which the concept screen puts at its center (L16 G1.1, DC-L16-06).

On L09's personality rubric the starter scores X≈3, Y≈3. That is the neutral-toolkit corner, on purpose: it is a baseline for the builder's dials and the user's brand hooks to move away from. It is not an identity (L09 A3) [inferred placement].

Hierarchy in each view uses three sizes (a 28px title, or 20px inside the concept app, plus 14 and 12) and separates levels by weight and color (L15 P02, P04). Specimens such as the type scale are the only exception. Grouping keeps inner gaps smaller than outer gaps, at least 1:2 (DC-L03-24, DC-L15-05).

## Verification (run 2026-09-23)

- **Contrast:** 126/126 pairs pass WCAG 2.2 AA in both modes. The lowest ratios:
  - light text: 4.58:1 (`text.tertiary` on `surface.sunken`)
  - dark text: 4.62:1 (`text.tertiary` on `surface.overlay`)
  - light non-text: 3.12:1 (`border.strong` on `surface.sunken`)
  - dark non-text: 3.10:1 (`border.strong` on `surface.overlay`)
  - `text.primary` is 15.5:1 (light) and 13.3:1 (dark) on raised surfaces.
- Alpha colors (scrim, shadows) are decorative and are not contrast-tested.
- **Resolver:** all 8 permutations resolve (320 tokens each, no missing alias, no cycle).
- **Hex fallbacks:** all 144 OKLCH primitives match their hex within 1/255.
- **Figma scripts:** all 15 pass `node --check` and run in order against a mock of the Plugin API. That mock checks alias types, mode values, scopes, binding types, and `combineAsVariants` input. A second run creates nothing new, which shows the scripts are idempotent. They have not been run in real Figma.
- **Artboards:** rendered with headless Chrome at 1440px and reviewed. Final heights: 2893, 6084, 2965 and 1528px.

## Paper write plan (the orchestrator runs this after the reconnect)

Paper's MCP writes HTML, styles and tokens, but its tokens are CSS variables with no modes (S-L16-009, S-L16-018).

1. Load `get_guide({topic: "paper-mcp-instructions"})`, then call `get_font_family_info` for Inter and JetBrains Mono. Paper's server instructions require both (S-L16-020).
2. Create or open a file, with one page per artboard or one page for all four.
3. For each artboard, `create_artboard` with width 1440, named after the root `data-artboard` value. Then `update_styles` with that root div's style (background, padding, flex column, gap, font family, color).
4. `write_html` each `<section data-group>` in document order as children of the artboard. Each section repeats font family and color, so every write stands alone. If a group is too large:
   - Use `paper_plan.py`, which splits at 15 KB.
   - Or, for `04.1-app`, write the shell and then insert the `data-subgroup` children: top bar, then the body with its rail, editor and inspector.
5. `create_tokens` from `atlas/paper-tokens.json`. The tool is undocumented (S-L16-020), so map the fields to its schema when connected.
6. `get_screenshot` each artboard and compare it with a local render of the same HTML (headless Chrome at 1440px wide), then `finish_working_on_nodes`.

The whole plan is about 70 calls (55 `write_html` chunks included), against 100 a week on Paper's free plan (S-L16-010).

## Where every value comes from

| Value | Choice | Source |
|---|---|---|
| Color space, gamut | OKLCH authoring, sRGB hex fallback, gamut-mapped by lowering chroma | DC-L01-01, DC-L01-05 |
| Ramp shape | 12 steps, each with a fixed job (backgrounds 1-2, component fills 3-5, borders 6-8, solid 9-10, text 11-12) | DC-L01-02, DC-L01-03, L09 A1.4 |
| Ramp construction | Contrast-indexed: every hue has the same WCAG luminance at the same step, so an accent swap keeps every pair valid | DC-L01-03 (Spectrum/Leonardo method), DC-L16-14 |
| Chroma | Peaks at step 9 and falls at the extremes; neutrals are hue-matched at chroma ≤ 0.014 | DC-L01-03, DC-L01-06 |
| Palette | 1 neutral + 1 accent + 4 status ramps | L09 A1.3, DC-L01-08, DC-L01-15 |
| Dark mode | Separate ramps and a role-based mapping; darkest base #121315; dark accents lighter, with dark on-text | DC-L01-18, DC-L01-19, S-L07-100 (Material primary80 with dark on-primary) |
| States | Hover +1 step, pressed +2 steps | DC-L01-17 |
| Roles | Four surfaces; text primary, secondary, tertiary, disabled, inverse; three border strengths plus focus; subtle and bold per status | DC-L01-11 to DC-L01-16, DC-L04-13 |
| Contrast target | WCAG 2.2 AA on every pair, in every mode | DC-L01-22, L09 A1.11 |
| Scrim, shadows | Scrim 45% light / 60% dark; 2-3 layer shadows at alpha 8-16%, doubled in dark, 1px ring in dark | DC-L04-18, DC-L04-12, L09 A1.12 |
| Spacing | 2, 4, 6, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96; names are percent of 8px | L09 A1.2, DC-L03-01, DC-L03-02, DC-L03-03, DC-L03-06 |
| Spacing semantics | inset / gap / layout; compact density = one step down; layout spacing never changes with density | DC-L03-04, DC-L03-10, DC-L03-11, DC-L03-17 |
| Sizes | Controls 32/40/48 (20px line box + block padding); icons 16/20/24; target minimum 24 | DC-L03-05, DC-L03-07, DC-L08-07, DC-L05-05, DC-L03-12 |
| Radius | 0, 2, 4, 6, 8, 12, 16, 24, full; control 6 (the benchmark median); roles detail 4, container 12, overlay 16 | L09 A1.7, DC-L04-01, DC-L04-03, DC-L04-05 |
| Borders, focus | Widths 1/2/4; focus ring 2px with a 2px offset in `border.focus` | DC-L03-09, DC-L04-07, DC-L04-09, DC-L08-11 |
| Typeface | Inter (open-source neutral) + JetBrains Mono; 2 families | DC-L02-01, DC-L02-03, L09 A2.5 |
| Type scale | Body 14 (16 for reading); ratio ≈1.2 from 14, rounded to even px; 9 sizes; line heights snapped to 4px; tracking -0.02em at 48px and -0.01em at 28-32px; weights 400/500/600; 15 styles; uppercase only at 12px | DC-L02-08, 09, 10, 13, 14, 15, 18, L09 A1.8, DC-L15-02, L15 P03 |
| Motion | 0-500ms ladder, semantic 100/150/200/300/400; curves standard, enter, exit, linear; exit ≈75% of enter; reduced motion as a mode | L09 A1.5, DC-L04-20, DC-L04-21, DC-L04-24, DC-L04-25 |
| Depth | Flat in-page containers; shadows only for floating things; lighter surfaces in dark | DC-L04-10, DC-L04-11, L09 A1.12 |
| Token format | DTCG 2025.10 types, curly-brace aliases, Resolver for modes, `$extensions` for sources | S-L07-002, S-L07-003, S-L07-004 (shape re-checked on designtokens.org/tr/2025.10/resolver, 2026-09-23), DC-L01-26 |
| Button | 4 levels + danger; 6 states; 3 sizes; loading keeps focus; don't disable submit; verb-first labels; subtle danger in context | DC-L08-05 to DC-L08-12, L08 catalog C01, DC-L13-13, L15 P08 |
| Map layers and blocks | The 10 layers in `synthesis/ontology.json` (the builder meta layer is omitted) and their influence verbs; L08 categories and patterns P1-P13; L11 governance cards | ONTOLOGY overview, L08, L11 |
| Designer hooks | Formats and fallback paths copied from the Hook lines of Q-brand-03, Q-color-01, Q-voice-01, Q-type-02, Q-icon-01, Q-icon-06, Q-img-01, Q-img-04, Q-img-06, Q-motion-08 | synthesis/QUESTIONNAIRE.md |
| Builder concept | Panel plus live preview; light and dark side by side; outcome-first controls; "show 6 variations"; change set with visual diff; reference intake with accept / adjust / ignore; asset hooks | BRIEF 1-5, DC-L16-01, DC-L16-06, DC-L16-14, L16 G1.1-G1.5, Q-ref-01 |
| Figma structure | One collection per tier or axis; hidden primitives; precise scopes; code syntax on every variable; variables for values, styles for bundles; variants only for state, size and type | DC-L07-18 to DC-L07-22, figma-plan.md F-1 to F-3 |

## Inferred or unsourced (flagged, not facts)

- **Seed hues.** The accent hue (265) and the status hues (150, 75, 27, 230) are placeholders. The builder asks for the brand color (Q-color-01). Info sits 35° from the accent, so it relies on icon + label (DC-L01-15).
- **Numeric recipe choices.** These are designed to satisfy the sourced rules, but the exact numbers are mine: the per-step contrast and luminance targets, the chroma curves, the exact dark-surface steps, the shadow alphas within the sourced 8-24% band, and the per-style tracking.
- **Warning.** The warning solid is a dark amber with white text, which comes from contrast-indexing. Q-color-15 instead recommends dark text on a bright amber (the Atlassian pattern). This is an open choice for the builder.
- **Placeholder names.** iOS and Android code-syntax names (`DSColor.textPrimary`) and the `$extensions` namespace `dev.dsbuilder` are placeholders.
- **Illustrative content.** Artboard copy and the concept screen's numbers ("18 of 42 blocks", "14 components", the reference-site values) are illustrations, not data.
- **Figma API unknowns.** Paper's `create_tokens` schema, the parameters of `generate_figma_design`, the value shape of Figma's EASING type, and the `strokeWeight` binding are unverified (figma-plan.md section 8).
