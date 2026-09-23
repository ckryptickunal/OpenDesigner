# L03: Space, Sizing, Layout

Lane: L03 (Space, sizing, layout). Author: orchestrator subagent L03. Started 2026-09-23.
Status: complete (26 Decision Cards; sources in traces/L03-trace.md).

## Lane overview

In Nathan Curtis's 2016 comparison of five CSS libraries, space properties appeared more often than anything except color [S-L03-039], and it is the family that most directly sets how "dense" or "airy" a product feels [S-L03-028]. This lane covers the building blocks a design-system builder needs for space, sizing and layout:

1. **Base unit and spacing scale**: the unit (4 or 8), the progression (linear, geometric, hybrid), the number of steps and how steps are named.
2. **Spacing semantics**: inset, stack, inline, gap, margin; component spacing vs layout spacing.
3. **Sizing**: control heights, icon sizes, avatar sizes, border widths.
4. **Density**: whether density is a user setting, a component size prop, a global mode, or a platform scale.
5. **Targets**: touch and pointer target minimums and spacing.
6. **Grids and breakpoints**: columns, gutters, margins, breakpoint sets, containers, max widths.
7. **Layout patterns**: canonical layouts, panes, app-shell regions, navigation placement, safe areas, edge-to-edge, container queries, responsive vs adaptive.
8. **Layering**: z-index order as layout (brief; L04 owns elevation styling).
9. **Whitespace and rhythm**: grouping, hierarchy, vertical rhythm, and how spacing ratios read.
10. **Token encoding**: DTCG `dimension`, units per platform, naming, density modes.

**Biggest change since 2025 (verify-worthy):** Material 3 now publishes system spacing tokens, `md.sys.measurement.space0` to `space900` (0 to 72dp) with `space100 = 8dp`, currently Jetpack Compose only [S-L03-030]. Material also renamed "window size classes" to "breakpoints" and added large (1200-1599dp) and extra-large (1600dp+) [S-L03-025, S-L03-021]. Android 16 (API 36) removes the edge-to-edge opt-out and ignores orientation/resizability locks on displays with smallest width 600dp or more [S-L03-053]. Polaris React and its `space-*` tokens are deprecated; Polaris web components use keyword sizes (`small-500` to `large-500`) [S-L03-005, S-L03-006].

### Comparison table A: spacing scales (px or dp)

| System | Base | Token names | Values | Steps | Progression |
|---|---|---|---|---|---|
| IBM Carbon | 8px "mini unit" [S-L03-002] | `$spacing-01` to `$spacing-13` | 2, 4, 8, 12, 16, 24, 32, 40, 48, 64, 80, 96, 160 [S-L03-001] | 13 | Hybrid: 2-4-8 halving at the small end, +8 to 48, then +16 / +32, then a jump to 160 |
| Atlassian | 8px = `space.100` [S-L03-003] | `space.0` to `space.1000` (% of base) + `space.negative.025` to `.400` | 0, 2, 4, 6, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80 [S-L03-003] | 14 (incl. 0) | Hybrid: fine steps (2) at the bottom, +4 in the middle, +8/+16 at the top |
| Material 3 (Compose) | 8dp = `space100` [S-L03-030] | `md.sys.measurement.space0` to `space900` | 0, 2, 4, 6, 8, 10, 12, 14, 16, 20, 24, 32, 36, 40, 48, 56, 64, 72 [S-L03-030] | 18 | Mostly linear multiples of 8, with "nested units" 2/4/6/10 (and 14, 36) for component internals |
| Fluent 2 (global ramp) | 4px [S-L03-010] | `sizeNone`, `size20` to `size560` (px x 10) | 0, 2, 4, 6, 8, 10, 12, 16, 20, 24, 28, 32, 36, 40, 48, 52, 56 [S-L03-010] | 17 | Linear 4px with 2/6/10 "nudges" for icon alignment |
| Fluent UI React (web alias) | 4px | `spacingHorizontal*` / `spacingVertical*`: None, XXS, XS, SNudge, S, MNudge, M, L, XL, XXL, XXXL | 0, 2, 4, 6, 8, 10, 12, 16, 20, 24, 32 [S-L03-045] | 11 | t-shirt with "Nudge" half-steps |
| GitHub Primer | 4px (with 2/6) | `--base-size-2` to `--base-size-128` (named by px) + negatives | 2, 4, 6, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 64, 80, 96, 112, 128 [S-L03-009] | 19 | Linear 4 up to 48, then +16 |
| Adobe Spectrum 2 | 8px = `spacing-100` [S-L03-044] | `spacing-25` to `spacing-1000` | 1, 2, 4, 6, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96 [S-L03-044] | 15 | Hybrid, same shape as Atlassian; note names are ordinal, not % of base (`spacing-200` = 12px, not 16px) |
| Shopify Polaris React (deprecated) | 4px = `space-100` | `space-0` to `space-3200` (% of 4px) + aliases `space-card-padding` etc. | 0, 1, 2, 4, 6, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 112, 128 [S-L03-005] | 18 | Hybrid; repo archived, tokens last changed 2023-10-03 [S-L03-005] |
| Polaris web components (current) | not published on the page read | keywords `small-500`...`small-100`, `small`, `base`, `large`, `large-100`...`large-500`, `none` [S-L03-006] | pixel values not shown in docs read | 13 + none | Keyword scale centred on `base` |
| Tailwind CSS v4 | `--spacing: 0.25rem` (4px) [S-L03-017] | numeric multiplier: `p-1` = 4px, `p-4` = 16px, any integer [S-L03-015] | calc(var(--spacing) * n) [S-L03-015] | unbounded | Strictly linear, open-ended |
| Bootstrap 5.3 | `$spacer: 1rem` [S-L03-020] | `0` to `5` | 0, 4, 8, 16, 24, 48 (0, .25, .5, 1, 1.5, 3 rem) [S-L03-020] | 6 | Geometric-ish, very coarse |

Pattern across systems [inferred from the table]: almost every mature system lands on the same "hybrid" shape: fine 2px steps below 8, 4px steps from 8 to about 24, 8px steps to about 48, then 16px or larger jumps. The real difference is the base (4 vs 8) and the naming, not the values. Six of the eleven rows (Carbon, Atlassian, Material 3, Primer, Spectrum, Polaris React) contain every one of 2, 4, 8, 12, 16, 24, 32, 40, 48, 64; Tailwind can express all of them but does not name them.

### Comparison table B: breakpoints and grids

| System | Breakpoints (min width) | Columns | Margins / gutters | Notes |
|---|---|---|---|---|
| Material 3 / Android | compact <600dp, medium 600-839, expanded 840-1199, large 1200-1599, extra-large 1600+ [S-L03-025, S-L03-021] | pane-based rather than column-based: 1 pane (compact), 1-2 (medium/expanded/large), 1-3 (XL) [S-L03-025] | margins 16dp compact, 24dp medium and up; 24dp spacer between panes [S-L03-026] | Height classes: <480, 480-899, 900+ dp [S-L03-021] |
| Apple HIG | size classes, not pixel breakpoints: compact or regular, for width and height [S-L03-032] | n/a (system layout guides and margins) | system layout margins and readable-content guides [S-L03-032] | Decide by size class, never by device or orientation [S-L03-032] |
| IBM Carbon | sm 320, md 672, lg 1056, xlg 1312, max 1584 [S-L03-002] | 4 / 8 / 16 / 16 / 16 [S-L03-002] | margin 0 / 16 / 16 / 16 / 24; padding 16 everywhere; gutter 32 (wide), 16 (narrow), 1 (condensed) [S-L03-002, S-L03-054] | "2x" division: fluid grids divide by 2 [S-L03-002] |
| Fluent 2 | small 320-479, medium 480-639, large 640-1023, x-large 1024-1365, xx-large 1366-1919, xxx-large 1920+ [S-L03-010] | 12 common [S-L03-010] | gutters are multiples of the 4px base and can change per breakpoint [S-L03-010] | Calls responsive + adaptive a mix [S-L03-010] |
| GitHub Primer | xsmall 320, small 544, medium 768, large 1012, xlarge 1280, xxlarge 1400 [S-L03-008, S-L03-009] | viewport ranges: narrow <768 (1 col), regular >=768 (up to 2), wide >=1400 (up to 3) [S-L03-008] | content padding 16px, 24px at xlarge+; pane padding 16px [S-L03-008] | Full pages max-width 1280 (xlarge); interstitial pages max 320 [S-L03-008] |
| Bootstrap 5.3 | sm 576, md 768, lg 992, xl 1200, xxl 1400 [S-L03-018] | 12 at every breakpoint [S-L03-066] | gutter 1.5rem (24px); container max-widths 540 / 720 / 960 / 1140 / 1320 [S-L03-019, S-L03-066] | mobile-first min-width queries [S-L03-018] |
| Tailwind CSS v4 | sm 640 (40rem), md 768 (48rem), lg 1024 (64rem), xl 1280 (80rem), 2xl 1536 (96rem) [S-L03-016] | none built in | none built in | 13 container-query sizes @3xs 256px to @7xl 1280px [S-L03-016, S-L03-017] |

Pattern [inferred]: 768 is the one breakpoint shared exactly by Primer, Bootstrap and Tailwind; no single value is shared by all systems. The smallest breakpoint is 320 in Carbon, Fluent and Primer, which matches the width at which WCAG 1.4.10 Reflow requires content to work without two-dimensional scrolling [S-L03-060] (the docs read do not state this as their reason). Material and Apple have moved away from device-width thinking toward "available window space", which matters for foldables, split screen and resizable windows [S-L03-025, S-L03-032].

### Comparison table C: control height scales

| System | Sizes | Heights |
|---|---|---|
| IBM Carbon buttons | xs, sm, md, lg (productive), lg (expressive), xl, 2xl | 24, 32, 40, 48, 48, 64, 80 px [S-L03-042] |
| IBM Carbon data table rows | xs, sm, md, lg (default), xl | 24, 32, 40, 48, 64 px [S-L03-043] |
| Fluent UI React inputs | small, medium (default), large | 24, 32, 40 px [S-L03-046] |
| GitHub Primer controls | xsmall, small, medium, large, xlarge | 24, 28, 32, 40, 48 px [S-L03-009] |
| Adobe Spectrum 2 `component-height-*` | 50, 75, 100, 200, 300, 400, 500 | desktop 20, 24, 32, 40, 48, 56, 64 / mobile 26, 30, 40, 50, 60, 70, 80 px [S-L03-044] |
| Material 3 Expressive buttons | XS, S (default), M, L, XL | 32, 40, 56, 96, 136 dp [S-L03-059] |
| Apple visionOS buttons | mini, small, regular, large, extra large | 28, 32, 44, 52, 64 pt [S-L03-034] |
| Apple iOS / iPadOS controls | default / minimum | 44x44 / 28x28 pt [S-L03-033] |

## Decision Cards

### DC-L03-01: Base spacing unit
- **Block path:** Foundations > Space > Base unit
- **Questions the designer answers:** What single number do all spacing and sizing values derive from? Do we need values finer than that number? Must the unit align with our body text size and icon grid?
- **Options:**
  - **8 (with 2/4 sub-steps).** Carbon's 8px "mini unit" [S-L03-002]; Atlassian `space.100` = 8px [S-L03-003]; Material 3 `space100` = 8dp, plus nested 2/4/6/10dp [S-L03-030]; Spectrum `spacing-100` = 8px [S-L03-044].
  - **4.** Fluent 2 ("A 4x system reduces confusion while being easy to implement"; ramp includes 2, 6, 10 to align icons) [S-L03-010]; Polaris React (`space-100` = 4px) [S-L03-005]; Primer `base-size-4` family [S-L03-009]; Tailwind `--spacing: 0.25rem` [S-L03-017].
  - **16 / rem-based.** Bootstrap `$spacer: 1rem` with fractions [S-L03-020]. Nathan Curtis reports most systems he worked on used 16 because it is a good default font size and a factor of common screen widths [S-L03-039].
  - **Other (6, 10).** Curtis cites a team using base 6 and warns it produces too many options ("Stop the madness!") [S-L03-039].
- **Visual effect:** The base itself is invisible; what users see is the smallest perceptible difference between spacings. An 8 base with few sub-steps gives visibly distinct, "chunky" steps and a calmer, more regular rhythm. A 4 base allows tighter, more precise alignment (icon + label, dense tables) and a more compact, tool-like feel [inferred]. Fluent explicitly adds 2/6/10 so icons with built-in padding still land on the 4px grid [S-L03-010].
- **Depends on (upstream):** body type size and line height (L02); icon artboard sizes (L05); target platform density (Android dp, iOS pt, web px/rem).
- **Affects (downstream):** every spacing token, control heights, icon sizes, grid gutters and margins, radius steps (L04), line-height rounding (L02).
- **Token encoding:** a primitive `dimension` token, e.g. `space.base = {value: 8, unit: "px"}`; scale steps alias or multiply it. Tailwind exposes the base as one variable and derives utilities with calc() [S-L03-015].
- **Platform notes:** Android uses dp and iOS uses pt; DTCG says `px` is the equivalent of dp/pt and translators SHOULD convert [S-L03-038]. On web, rem makes spacing follow the user's font-size preference (see DC-L03-26).
- **Accessibility constraints:** none directly; the base must allow 24px (WCAG 2.5.8) and 44/48 targets (Apple/Material) to be built from whole steps [S-L03-035, S-L03-033, S-L03-029].
- **Default + heuristic:** Default to **4 as the grid, 8 as the rhythm**: name the scale on an 8 base but keep 2, 4, 6 (and 12) available for component internals. This is exactly what Material 3, Atlassian and Spectrum ship [S-L03-030, S-L03-003, S-L03-044]. Pick a pure 4 base for dense, data-heavy tools; pick 8 (or 16/rem) for marketing and content sites where fewer, larger steps keep rhythm obvious [inferred].
- **Evidence:** [S-L03-001, S-L03-002, S-L03-003, S-L03-005, S-L03-009, S-L03-010, S-L03-017, S-L03-020, S-L03-030, S-L03-039, S-L03-044]

### DC-L03-02: Spacing scale progression and step count
- **Block path:** Foundations > Space > Spacing scale
- **Questions the designer answers:** Should steps grow by a fixed amount, by a ratio, or by a mix? How many steps do we publish? What is the largest step?
- **Options:**
  - **Linear (fixed increment).** Tailwind (4px x n, open-ended) [S-L03-015]; Fluent global ramp (4px steps to 56) [S-L03-010]; Primer (4px steps to 48) [S-L03-009].
  - **Geometric (doubling).** Curtis argues for 2, 4, 8, 16, 32, 64 because linear scales offer "too many choices too close together" [S-L03-039]. Carbon's 2x grid applies the doubling idea to grids and fixed sizes [S-L03-002].
  - **Hybrid (fine at the bottom, coarse at the top).** Carbon 2, 4, 8, 12, 16, 24, 32, 40, 48, 64, 80, 96, 160 [S-L03-001]; Atlassian 0-80 in 14 steps [S-L03-003]; Spectrum 1-96 in 15 steps [S-L03-044]; Material 0-72 in 18 steps [S-L03-030].
  - **Coarse (5-6 steps).** Bootstrap 0, 4, 8, 16, 24, 48 [S-L03-020].
  - Step counts in the systems read: 6 (Bootstrap) to 19 (Primer); most sit at 13-18 [S-L03-001, S-L03-003, S-L03-009, S-L03-020, S-L03-030, S-L03-044].
- **Visual effect:** Hybrid and geometric scales produce clearly different "levels" of separation, so grouping reads instantly (tight within a group, loose between groups). Linear scales with many close steps tend to produce near-identical gaps (20 vs 24 vs 28) that read as inconsistency rather than hierarchy [S-L03-039]. Large top steps (80-160) exist for page sections and marketing layouts, not product UI [S-L03-001, S-L03-003].
- **Depends on (upstream):** DC-L03-01 base unit; product type (marketing needs large section steps; enterprise needs more small steps).
- **Affects (downstream):** semantic spacing aliases (DC-L03-04), density modes (DC-L03-11), grid gutters, section rhythm (DC-L03-25).
- **Token encoding:** primitives `space.0` ... `space.1000` (`dimension`); only semantic/component tokens should be used in components (L07 owns tier rules).
- **Platform notes:** identical numbers work on all platforms when expressed as px/dp/pt; on web decide rem vs px (DC-L03-26).
- **Accessibility constraints:** none directly; ensure steps exist that compose 24, 44 and 48 target sizes.
- **Default + heuristic:** Ship a hybrid scale of about 12-15 steps: 0, 2, 4, 6, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80 (Atlassian's exact set [S-L03-003]). Rule of thumb: adjacent steps should differ by at least about 25% above 8px so the difference is visible; below 8px, 2px steps are fine for component internals [inferred from the shape shared by Carbon, Atlassian, Spectrum, Material].
- **Evidence:** [S-L03-001, S-L03-002, S-L03-003, S-L03-009, S-L03-010, S-L03-015, S-L03-020, S-L03-030, S-L03-039, S-L03-044]

### DC-L03-03: Spacing token naming scheme
- **Block path:** Foundations > Space > Naming
- **Questions the designer answers:** Do token names encode the value, a position in a scale, or a size word? Will we need to insert a step later? Must names survive a base-unit change?
- **Options:**
  - **Percent-of-base numeric (100-scale).** Atlassian: "The number suffix representing the percentage of the base unit", so `space.200` = 16px [S-L03-003]; Material `md.sys.measurement.space100` = 8dp, `space150` = 12dp [S-L03-030]; Polaris React `space-400` = 16px on a 4px base [S-L03-005]. Allows insertion (`space.075`, `space.150`).
  - **Ordinal numeric (100-scale, not proportional).** Spectrum `spacing-100` = 8px but `spacing-200` = 12px and `spacing-300` = 16px [S-L03-044]. Looks like Atlassian's scheme but the numbers do not multiply; easy to misread [inferred].
  - **Sequential index.** Carbon `$spacing-01` ... `$spacing-13` [S-L03-001]; Bootstrap `0`-`5` [S-L03-020]. Cannot insert a step without renumbering.
  - **Value-in-name.** Primer `--base-size-16` [S-L03-009]; Fluent global `size160` (px x 10) [S-L03-010]. Transparent, but the name lies if the value changes.
  - **Multiplier.** Tailwind `p-4` = 4 x `--spacing` [S-L03-015]; Carbon's sizing scale uses "1x, 2x, 3x" mini units [S-L03-002].
  - **T-shirt / keyword.** Fluent web `spacingHorizontalXS`, `S`, `SNudge`, `M`, `MNudge`, `L`... [S-L03-045]; Polaris web components `small-500`...`base`...`large-500` [S-L03-006]; Curtis recommends t-shirt names because descriptive labels fail [S-L03-039].
- **Visual effect:** none directly; naming decides whether designers pick the right step. Names that encode a proportion make the ratio between two spacings legible in code review [inferred].
- **Depends on (upstream):** DC-L03-01, DC-L03-02; team's token tier model (L07).
- **Affects (downstream):** Figma variable names, CSS custom properties, code-gen for iOS/Android, AI-agent readability of the system (L00's community signal reports that machine-readable docs raised agent build success in Sanity's evals [S-L03-065]).
- **Token encoding:** `space.100`, `space.150` (primitive); `space.inset.md`, `space.stack.lg` or `spacing.gap.control` (semantic); `button.padding.inline` (component).
- **Platform notes:** dots in DTCG group paths become `--space-100` in CSS, `space100` in Kotlin/Swift [inferred; L07 owns transforms].
- **Accessibility constraints:** none.
- **Default + heuristic:** Use **percent-of-base 100-scale for primitives** (Atlassian/Material style) and **t-shirt or role names for semantic tokens**. Avoid ordinal 100-scales that look proportional but are not (Spectrum pattern) [inferred]. Never put `padding` or `margin` in a primitive name; Curtis notes one spacing concept maps to several CSS properties and to non-HTML platforms [S-L03-039].
- **Evidence:** [S-L03-001, S-L03-002, S-L03-003, S-L03-005, S-L03-006, S-L03-009, S-L03-010, S-L03-015, S-L03-030, S-L03-039, S-L03-044, S-L03-045]

### DC-L03-04: Spacing semantics (inset, stack, inline, gap; component vs layout)
- **Block path:** Foundations > Space > Semantic spacing
- **Questions the designer answers:** Do we give designers named spacing roles or only a raw scale? Is spacing owned by the parent (gap/padding) or by children (margins)? Do layout spacings differ from component spacings?
- **Options:**
  - **Curtis/EightShapes concept set:** inset (all four sides), squish inset, stretch inset, stack (vertical), inline (horizontal, wrapping), grid [S-L03-039].
  - **Material 3 set:** padding (inside), gap (between elements), margin (outside); positions horizontal/vertical/leading/trailing/top/bottom. "Use padding & gaps before using margins"; component tokens are renaming from `leading-space`/`between-space` to `padding`/`gap` [S-L03-030].
  - **Layout vs component split:** Carbon's spacing scale is for inside components and between components, with a separate layout concept (2x grid, margins, padding 16px) [S-L03-001, S-L03-002]; Material separates "component layouts" (padding, gaps) from "page layouts" (margins, spacers between panes, top padding) [S-L03-030]; Fluent names component, pattern and layout spacing [S-L03-010].
  - **Stack/gap primitives in code:** Carbon Stack component delegates spacing to the parent so children carry no margins [S-L03-001]; Primer `--stack-gap-condensed/normal/spacious` = 8/16/24 and matching stack padding [S-L03-009]; Polaris web components `gap`/`padding` keywords [S-L03-006].
  - **Raw scale only.** Tailwind/Bootstrap utilities apply any step to any property [S-L03-015, S-L03-020].
- **Visual effect:** Semantic roles make grouping consistent: the same inset in every card, the same stack between every form field. That consistency is what reads as "rhythm" [S-L03-028]. Raw-scale-only systems drift toward one-off values.
- **Depends on (upstream):** DC-L03-02 scale; component architecture (L08).
- **Affects (downstream):** every container component (card, dialog, list item, form), layout primitives (Stack, Box, Inline, Grid), density modes (density is easiest to tune when inset and stack are distinct dials [S-L03-039]).
- **Token encoding:** semantic `dimension` aliases, e.g. `space.inset.md -> {space.200}`, `space.stack.lg -> {space.300}`, `space.inline.sm -> {space.100}`, `space.gap.control -> {space.100}`, `layout.margin.compact -> 16`, `layout.spacer.pane -> 24` (Material values [S-L03-026]).
- **Platform notes:** leading/trailing (not left/right) so RTL swaps automatically [S-L03-030].
- **Accessibility constraints:** grouping by proximity aids comprehension; NN/g notes responsive stacking can accidentally group unrelated items [S-L03-061].
- **Default + heuristic:** Publish three semantic families: **inset** (padding), **gap** (stack and inline) and **layout** (margins, pane spacers, section spacing). Rule: parents own spacing (padding + gap); children never set outer margins [S-L03-030, S-L03-001].
- **Evidence:** [S-L03-001, S-L03-002, S-L03-006, S-L03-009, S-L03-010, S-L03-026, S-L03-028, S-L03-030, S-L03-039, S-L03-061]

### DC-L03-05: Inset shape (square, squish, stretch)
- **Block path:** Foundations > Space > Semantic spacing > Inset
- **Questions the designer answers:** Are container paddings equal on all sides? Do buttons and table cells use less vertical padding than horizontal? Do inputs use more?
- **Options:**
  - **Square inset** for cards, panels, dialogs [S-L03-039].
  - **Squish inset**: vertical padding reduced (Curtis's team used 50%) for buttons, table cells, list items [S-L03-039]. Example: Fluent button uses `buttonSpacingMedium` vertically and `spacingHorizontalM` (12px) horizontally [S-L03-046]; Material Expressive small button 16dp leading padding on a 40dp-high container [S-L03-059, S-L03-058].
  - **Stretch inset**: more vertical than horizontal, used for text inputs and textareas [S-L03-039].
- **Visual effect:** Squished buttons and rows look sleeker and pack tighter vertically; square insets feel stable and "boxed"; stretch insets make inputs look roomier and easier to hit [inferred]. Carbon notes type must sit against the padding edge, not on it, which is what makes insets align to key lines [S-L03-002].
- **Depends on (upstream):** DC-L03-04, control height scale (DC-L03-07), line height (L02).
- **Affects (downstream):** button, chip, tag, table cell, list item, text field padding tokens.
- **Token encoding:** `space.inset.squish.md = {block: {space.100}, inline: {space.200}}` is not a DTCG composite type; encode as two `dimension` tokens (`...inset.squish.md.block`, `...inline`) [inferred; DTCG has no padding composite in 2025.10, see S-L03-037].
- **Platform notes:** use logical properties (`padding-block`, `padding-inline`) on web [inferred].
- **Accessibility constraints:** squish must not shrink the hit area below 24px (WCAG AA) or 44/48 platform targets [S-L03-035, S-L03-033, S-L03-029].
- **Default + heuristic:** Squish = vertical at half of horizontal for pill-like controls; stretch for inputs only. Derive control height as line box + 2 x block padding: Primer's tokens do exactly this with a 20px line box and block padding 2 / 4 / 6 / 10 / 14px giving 24 / 28 / 32 / 40 / 48px controls, and horizontal padding offered as condensed / normal / spacious (medium: 8 / 12 / 16px) [S-L03-009, S-L03-085].
- **Evidence:** [S-L03-002, S-L03-009, S-L03-029, S-L03-033, S-L03-035, S-L03-037, S-L03-039, S-L03-046, S-L03-058, S-L03-059, S-L03-085]

### DC-L03-06: Fine steps, nudges and negative space tokens
- **Block path:** Foundations > Space > Spacing scale > Fine and negative steps
- **Questions the designer answers:** Do we allow 1, 2, 6, 10px values? Do we publish negative spacing (for overlaps, hanging icons, optical alignment)?
- **Options:**
  - **Nudge steps**: Fluent 2, 6, 10 exist to compensate for icon padding [S-L03-010]; Fluent web `SNudge` 6, `MNudge` 10 [S-L03-045]; Material "nested units" 2, 4, 6, 10dp "actively used in common layouts or Material components" [S-L03-030].
  - **Sub-pixel/hairline**: Spectrum `spacing-25` = 1px [S-L03-044]; Polaris React `space-025` = 1px [S-L03-005].
  - **Negative tokens**: Atlassian `space.negative.025` to `space.negative.400` (-2 to -32px) in code [S-L03-003]; Primer `--base-size-negative-2` to `-48` [S-L03-009].
  - **None**: Bootstrap and Carbon publish no negatives in their spacing scales [S-L03-020, S-L03-001].
- **Visual effect:** nudges fix optical misalignment (icons that look off-centre, text baselines); negatives create overlaps (avatar stacks, hanging punctuation, pulling content into gutters as in Carbon's narrow gutter mode [S-L03-054]).
- **Depends on (upstream):** icon artboard padding (L05); DC-L03-01.
- **Affects (downstream):** icon buttons, avatar groups, list items, focus-ring offsets (Primer `--outline-focus-offset` = -2px [S-L03-009]).
- **Token encoding:** `space.negative.100 = {value: -8, unit: "px"}` (DTCG dimension allows negative numbers since value is any number [S-L03-037]).
- **Platform notes:** negative margins are native on web; SwiftUI/Compose express overlaps with offsets instead [inferred].
- **Accessibility constraints:** overlaps must not make targets overlap (WCAG 2.5.8 spacing exception) [S-L03-035].
- **Default + heuristic:** Include 2, 4, 6 (and 10 only if your icon set needs it); publish negatives for the same steps as positives up to 32. Keep 1px for borders, not spacing [inferred].
- **Evidence:** [S-L03-001, S-L03-003, S-L03-005, S-L03-009, S-L03-010, S-L03-020, S-L03-030, S-L03-035, S-L03-037, S-L03-044, S-L03-045, S-L03-054]

### DC-L03-07: Control height scale (sm / md / lg)
- **Block path:** Foundations > Sizing > Control heights
- **Questions the designer answers:** How many control sizes? What is the default height? Do buttons, inputs, selects and table rows share one height scale?
- **Options:**
  - **24/32/40/48 ladder**: Carbon xs 24, sm 32, md 40, lg 48, then xl 64 and 2xl 80 for buttons that bleed to the edge of modals, side panels and tearsheets [S-L03-042]. Carbon calls large (productive, 48px) "the most common button size in software products"; small and medium buttons pair with 32px and 40px inputs [S-L03-082]. Data table rows use the same 24-64 ladder, and the header row must match the row size [S-L03-043].
  - **24/32/40 with 32 default**: Fluent inputs small 24, medium 32 (default), large 40 [S-L03-046].
  - **24/28/32/40/48 with 32 default**: Primer control sizes xsmall-xlarge [S-L03-009]; Primer Button sizes small, medium (default, "Best for most interfaces"), large ("Use sparingly") [S-L03-083].
  - **Platform-scaled heights**: Spectrum `component-height-100` = 32px desktop / 40px mobile; full ladder 20-64 desktop and 26-80 mobile [S-L03-044].
  - **Large touch-first heights**: Material 3 Expressive buttons 32 / 40 (default small) / 56 / 96 / 136dp [S-L03-059]; Apple iOS default control 44pt [S-L03-033]. Caveat from L00: Compose Material3 stable is 1.4.0 and the Expressive button APIs are only graduating in the 1.5.0 alphas, so these sizes are not yet in a stable Compose release without opt-ins [S-L03-065].
- **Visual effect:** 32px defaults read as desktop productivity (GitHub, Microsoft 365); 40-48px defaults read as touch-friendly or enterprise-comfortable (Carbon lg 48); 56dp+ buttons read as expressive, consumer, playful (M3 Expressive) [inferred from which products use which]. Shared heights let buttons, inputs and selects align on one row, which creates grid relationships naturally [S-L03-002].
- **Depends on (upstream):** DC-L03-01 base, typography line heights (L02), density target (DC-L03-11), platform/input (DC-L03-13).
- **Affects (downstream):** buttons, inputs, selects, segmented controls, table rows, toolbars (Carbon toolbar 48/32 [S-L03-043]), icon-button min widths (Fluent 24/32/40 [S-L03-046]).
- **Token encoding:** `size.control.sm/md/lg` (`dimension`), aliased by `button.height.md`, `input.height.md`. Spectrum shows the pattern of one token with platform sets (desktop/mobile) [S-L03-044].
- **Platform notes:** desktop pointer can go to 24-32; touch should default to 44pt (iOS) / 48dp (Android target) even if the visual control is smaller [S-L03-033, S-L03-029].
- **Accessibility constraints:** WCAG 2.5.8 AA 24x24 CSS px minimum or spacing exception [S-L03-035]; 2.5.5 AAA 44x44 [S-L03-036]; Material requires 48x48dp targets for XS/S buttons [S-L03-058].
- **Default + heuristic:** 3 sizes (sm 32, md 40, lg 48) for touch-inclusive products; (sm 24, md 32, lg 40) for pointer-first desktop tools. Keep the ladder on multiples of 8 so it matches the grid [inferred from Carbon/Fluent/Primer].
- **Evidence:** [S-L03-002, S-L03-009, S-L03-029, S-L03-033, S-L03-035, S-L03-036, S-L03-042, S-L03-043, S-L03-044, S-L03-046, S-L03-058, S-L03-059, S-L03-082, S-L03-083, S-L03-084]

### DC-L03-08: Icon and avatar size scales
- **Block path:** Foundations > Sizing > Media sizes (icons, avatars)
- **Questions the designer answers:** Which icon sizes pair with which text sizes? How many avatar sizes? Linear or doubling?
- **Options:**
  - **Icons 16/20/24/32**: Carbon uses 16px artboards by default; 16 and 20 pair with 14 and 16px IBM Plex; 24 and 32 for larger needs; "Don't alter the icon-text size ratio" [S-L03-062].
  - **Platform-scaled icons**: Spectrum `workflow-icon-size-50..300` desktop 14/16/20/22/26, mobile 16/18/24/28/30 [S-L03-044]; Spectrum React v1.7 "refreshes icon sizing to match text line height" [S-L03-031].
  - **Icon sized to button size**: Material Expressive button icons 20/20/24/32/40dp for XS-XL [S-L03-059].
  - **Hybrid avatar scale**: Primer avatars start at 16 and step by 4 to 32, then by 8 to 48; 64 is the largest [S-L03-063].
  - **T-shirt avatar names**: Atlassian `xxsmall` (16px) ... `xxlarge`; `xsmall` kept as legacy name for 16px [S-L03-064].
- **Visual effect:** Icons sized to the text line height sit optically level with labels; oversized icons shift personality toward friendly/consumer, undersized toward dense/technical [inferred]. Hybrid avatar scales give fine control where lists are dense and big jumps where profile headers need presence [inferred].
- **Depends on (upstream):** type scale (L02), icon grid and optical padding (L05), control heights (DC-L03-07).
- **Affects (downstream):** icon buttons, list item leading elements, avatar groups, chips, navigation rails.
- **Token encoding:** `size.icon.sm = 16`, `size.icon.md = 20`, `size.icon.lg = 24`; `size.avatar.xs..xl`. L05 owns icon construction.
- **Platform notes:** Material Symbols and SF Symbols scale with text (L05/L02); set icon tokens relative to text size where platforms support it [inferred].
- **Accessibility constraints:** icon-only buttons need a target of 44pt/48dp/24px regardless of glyph size; Carbon: "All touch targets for interactive icons need to be 44px or larger" [S-L03-062, S-L03-029].
- **Default + heuristic:** icon 16/20/24/32; avatar 16/20/24/32/40/48/64 (Primer's hybrid [S-L03-063]). Rule: icon size = body line height minus 0-4px [inferred].
- **Evidence:** [S-L03-029, S-L03-031, S-L03-044, S-L03-059, S-L03-062, S-L03-063, S-L03-064]

### DC-L03-09: Border width scale
- **Block path:** Foundations > Sizing > Border widths
- **Questions the designer answers:** How many stroke weights? Which one is the default outline, which marks selection, which marks focus?
- **Options:**
  - **1 / 2 / 4**: Primer `borderWidth-thin` 1px (default), `thick` 2px, `thicker` 4px; focus outline width 2px with -2px offset [S-L03-009]; Spectrum `border-width-100/200/400` = 1/2/4px [S-L03-044].
  - **Hairline + emphasis only (1 and 2)** [inferred common minimum; not verified as a named system here].
- **Visual effect:** 1px borders read as light, precise, "tool-like"; 2px borders read as bolder, friendlier, more accessible; thick 4px is reserved for strong selection or accent bars [inferred]. Carbon's condensed gutter mode uses 1px gutters with darker borders to emphasize the grid [S-L03-054].
- **Depends on (upstream):** L04 shape/radius, L01 contrast of border colors, density target.
- **Affects (downstream):** inputs, cards, dividers, focus rings, selected states, table grid lines.
- **Token encoding:** `border.width.default = {value: 1, unit: "px"}`, `border.width.selected = 2`, `focus.outline.width = 2` (`dimension`). L04 owns borders as a visual style; this lane only owns the size scale.
- **Platform notes:** hairlines on high-density screens may render thinner than 1 physical px in native (pt/dp) contexts [inferred].
- **Accessibility constraints:** WCAG 1.4.11 needs 3:1 contrast for UI component boundaries that identify the control (L01 owns); 2px focus indicators are easier to see (L04/L08 own focus).
- **Default + heuristic:** 1 / 2 / 4 with 1 default and 2 for focus/selection.
- **Evidence:** [S-L03-009, S-L03-044, S-L03-054]

### DC-L03-10: Density strategy (who sets density, and how)
- **Block path:** Foundations > Space > Density
- **Questions the designer answers:** Do our users need to see a lot at once (data, tables, dashboards) or focus on one thing (consumer, marketing)? Is density fixed by us, chosen per component, chosen by the user, or set by platform?
- **Options:**
  - **Fixed density (no setting).** Most marketing and consumer systems [inferred].
  - **Component size props (sm/md/lg) chosen by designers.** Carbon buttons and data tables xs-xl [S-L03-042, S-L03-043]; Fluent small/medium/large [S-L03-046]; Primer xsmall-xlarge [S-L03-009].
  - **User-selectable global density.** Salesforce Lightning: org and user choose comfy, cozy or compact; compact also moves labels inline with fields, i.e. density changes layout, not only padding [S-L03-070]. Gmail's Compact/Cozy/Comfortable toggle cited by Curtis [S-L03-039]. Atlassian Confluence (Feb 2026) added a page-level "compact density" that reduces font size and line spacing; users immediately asked for table padding to shrink too [S-L03-051].
  - **Numbered component density scale.** Material: 0 default, then -1, -2, -3, each step typically removing 4dp of vertical padding or height; opt-in; not for menus, snackbars or dialogs [S-L03-029].
  - **Platform scale.** Spectrum gives component heights and icon sizes separate desktop and mobile values (mobile about 1.25x, e.g. 32 to 40px component height), while base spacing tokens keep one value [S-L03-044].
  - **Input-modality density.** Primer switches some control-stack gaps by pointer type: 12px for coarse pointers, 8px for fine [S-L03-009].
- **Visual effect:** Material: "A denser layout can feel more serious and focused, while a more spacious layout can feel calm and open" [S-L03-028]. High density suits scanning and comparing (data tables, news, financial portals, dashboards); low density suits aesthetics, a focused message, or easy navigation [S-L03-029].
- **Depends on (upstream):** audience and content type (enterprise/data vs consumer/marketing), platform/input (DC-L03-13), type scale (L02: Confluence's compact changes type, not just space [S-L03-051]).
- **Affects (downstream):** inset and stack tokens, control heights, row heights, type sizes in dense modes, label placement in forms (Salesforce [S-L03-070]), icon sizes.
- **Token encoding:** a `density` mode on a spacing/sizing collection (see DC-L03-11).
- **Platform notes:** Salesforce density does not apply to its mobile app [S-L03-070]; Material says density should not change automatically across breakpoints or orientation unless the person changes it [S-L03-029].
- **Accessibility constraints:** keep targets at 48x48dp (Material) even when dense; density settings controls themselves must use default target sizes so users can revert [S-L03-029]; WCAG 2.5.8 24px floor on web [S-L03-035].
- **Default + heuristic:** Consumer/marketing: fixed comfortable density. Enterprise/data: ship component sizes plus a user-level compact mode that shrinks insets, stacks and row heights by one scale step (about 4px per step, Material's rule [S-L03-029]); never shrink targets below the platform minimum.
- **Evidence:** [S-L03-009, S-L03-028, S-L03-029, S-L03-035, S-L03-039, S-L03-042, S-L03-043, S-L03-044, S-L03-046, S-L03-051, S-L03-070]

### DC-L03-11: Density implemented as a token mode
- **Block path:** Foundations > Space > Density > Modes
- **Questions the designer answers:** Which tokens change between density modes? Is density a mode on the same collection as breakpoint/platform, or a separate axis? What stays fixed?
- **Options:**
  - **Figma variable modes** on a number/spacing collection (Figma's own example: spacing and padding modes for watch, mobile, desktop) [S-L03-057].
  - **Token sets per platform**: Spectrum tokens carry `sets: {desktop, mobile}` for heights and icon sizes, while base spacing (`spacing-100` = 8px) has a single value [S-L03-044].
  - **Semantic-layer swap**: keep primitives fixed; remap semantic aliases (`space.inset.md` from `space.200` to `space.150`) per density [inferred; consistent with Material applying density "to the component attribute" rather than the system tokens [S-L03-030]].
  - **Component-level density**: Salesforce `density="auto|comfy|compact"` attribute on forms [S-L03-070].
- **Visual effect:** a density mode changes the whole product's rhythm at once while keeping proportions; a partial mode (type only, as in Confluence) can leave oversized padding around smaller text, which users noticed [S-L03-051].
- **Depends on (upstream):** DC-L03-10 strategy; token tiering (L07); Figma plan mode limits (L07).
- **Affects (downstream):** all semantic spacing and sizing tokens, control heights, row heights, possibly type tokens.
- **Token encoding:** DTCG 2025.10 supports theming/multi-brand via separate sets and resolvers (L07 owns details; COMMUNITY-SIGNAL confirms theming is in the stable spec [S-L03-065]); per-mode values stay `dimension`.
- **Platform notes:** web: CSS custom properties scoped to `[data-density="compact"]` [inferred]; native: environment values (SwiftUI) or CompositionLocals (Compose) [inferred; L10 owns].
- **Accessibility constraints:** target size and text size floors must be encoded as fixed tokens that density modes cannot override [inferred from S-L03-029].
- **Default + heuristic:** Put density on the **semantic layer**, as its own mode axis separate from breakpoints and color themes; leave primitives and target minimums untouched.
- **Evidence:** [S-L03-029, S-L03-030, S-L03-044, S-L03-051, S-L03-057, S-L03-065, S-L03-070]

### DC-L03-12: Minimum touch and pointer target
- **Block path:** Foundations > Sizing > Targets
- **Questions the designer answers:** What is the smallest interactive area we allow? Is the visual control allowed to be smaller than its hit area? Does it differ by platform and input?
- **Options (real values):**
  - **Apple**: iOS/iPadOS default 44x44pt, minimum 28x28pt; macOS 28x28 / 20x20; tvOS 66x66 / 56x56; visionOS 60x60 / 28x28; watchOS 44x44 / 28x28 [S-L03-033]; buttons need a hit region of at least 44x44pt (60x60 in visionOS) [S-L03-034].
  - **Material**: default target at least 48x48 CSS px / dp; target stays 48x48 even if the icon is smaller [S-L03-029]; XS and S icon buttons must have 48x48dp targets [S-L03-058].
  - **WCAG 2.2 SC 2.5.8 (AA)**: at least 24x24 CSS px, with spacing, equivalent, inline, user-agent and essential exceptions [S-L03-035].
  - **WCAG 2.2 SC 2.5.5 (AAA)**: at least 44x44 CSS px [S-L03-036].
  - **Windows**: 7.5mm, about 40x40px at 135 PPI at 1.0x scaling [S-L03-050].
  - **Fluent 2**: spacers should accommodate iOS & Web 44x44 and Android 48x48 [S-L03-010]. **Carbon**: interactive icon targets 44px or larger [S-L03-062].
- **Visual effect:** larger targets push controls apart and increase row heights, which reads as more spacious and friendlier; small targets allow dense toolbars [inferred]. Decoupling hit area from visual size lets a product look dense while staying usable [S-L03-029].
- **Depends on (upstream):** platform and input modality, audience (older users, field workers, accessibility commitments), density strategy.
- **Affects (downstream):** control heights (DC-L03-07), icon buttons, list rows, table row actions, chip spacing, navigation items.
- **Token encoding:** `size.target.min = {value: 24, unit: "px"}` (web AA floor), `size.target.touch = 44` (iOS pt) / `48` (Android dp); these should be fixed across density modes.
- **Platform notes:** web: implement larger hit areas with padding or pseudo-elements; iOS: `contentShape`/hit-test insets; Android: `minimumInteractiveComponentSize` in Compose [inferred; L10 owns].
- **Accessibility constraints:** as listed; 24px is the WCAG 2.2 AA floor, 44px the AAA level [S-L03-035, S-L03-036].
- **Default + heuristic:** Web: 24px visual minimum with 44px hit area on touch (`pointer: coarse`); iOS 44pt; Android 48dp. Rule: visual size may shrink with density; hit area never does.
- **Evidence:** [S-L03-010, S-L03-029, S-L03-033, S-L03-034, S-L03-035, S-L03-036, S-L03-050, S-L03-058, S-L03-062]

### DC-L03-13: Target spacing and control proximity
- **Block path:** Foundations > Space > Target spacing
- **Questions the designer answers:** How far apart must adjacent tappable things be? How many controls fit in a row?
- **Options:**
  - **WCAG 2.5.8 spacing exception**: an undersized target passes if a 24 CSS px circle centred on it does not intersect another target or another target's circle [S-L03-035].
  - **Apple padding**: about 12pt around bezeled elements, about 24pt around elements without a bezel [S-L03-033]; visionOS button centres at least 60pt apart [S-L03-032, S-L03-034]; watchOS: no more than three glyph buttons or two text buttons side by side [S-L03-032].
  - **Windows**: 8epx between buttons and between buttons and flyouts; 12epx between control and label and between content areas; 16epx from surface edge to text [S-L03-047].
  - **Primer by pointer**: control-stack gap 12px on coarse pointers, 8px on fine [S-L03-009].
- **Visual effect:** larger gaps between targets make toolbars look airier and reduce mis-taps; tight clusters read as a single grouped control (proximity) [S-L03-061].
- **Depends on (upstream):** DC-L03-12, DC-L03-02.
- **Affects (downstream):** button groups, toolbars, chip groups, segmented controls, pagination, icon rows.
- **Token encoding:** `space.gap.control` (fine pointer) and `space.gap.control.coarse`; or a pointer-based mode [inferred from S-L03-009].
- **Platform notes:** CSS `@media (pointer: coarse)` lets web switch gaps by input type (Primer's approach) [S-L03-009].
- **Accessibility constraints:** the WCAG circle test above [S-L03-035].
- **Default + heuristic:** 8px gap between adjacent controls on desktop, 12px on touch; never place two sub-24px targets closer than 24px centre-to-centre.
- **Evidence:** [S-L03-009, S-L03-032, S-L03-033, S-L03-034, S-L03-035, S-L03-047, S-L03-061]

### DC-L03-14: Breakpoint set
- **Block path:** Foundations > Layout > Breakpoints
- **Questions the designer answers:** How many layout changes do we design for? Are breakpoints based on device widths, content, or available window space? Do we need large-desktop breakpoints?
- **Options:** (full values in Comparison table B)
  - **Window-space classes (native-first):** Material/Android five width breakpoints 600 / 840 / 1200 / 1600dp plus height classes 480 / 900dp [S-L03-025, S-L03-021]; Apple's two-value size classes (compact/regular for width and height) set by the system [S-L03-032].
  - **Web framework sets:** Tailwind 640 / 768 / 1024 / 1280 / 1536 [S-L03-016]; Bootstrap 576 / 768 / 992 / 1200 / 1400 [S-L03-018].
  - **System-specific sets:** Carbon 320 / 672 / 1056 / 1312 / 1584 [S-L03-002]; Fluent 320 / 480 / 640 / 1024 / 1366 / 1920 [S-L03-010]; Primer 320 / 544 / 768 / 1012 / 1280 / 1400 plus three "viewport ranges" narrow/regular/wide [S-L03-008].
  - **Two-level model:** Primer separates opinionated viewport ranges (for page layout) from raw breakpoints (for fine-tuning) [S-L03-008].
- **Visual effect:** each breakpoint is a moment where the layout visibly reorganizes (panes appear, navigation swaps from bar to rail, columns double). Fewer breakpoints means fewer, bigger shifts; more breakpoints means smoother adaptation but more design and QA [inferred]. Material: "Rather than designing for an ever-increasing number of display states, focusing on breakpoints ensures layouts work across a wide range of devices" [S-L03-025].
- **Depends on (upstream):** platforms targeted (L10), content type, navigation model, whether large desktop matters (Material: "Some products may not need large and extra-large breakpoints" [S-L03-026]).
- **Affects (downstream):** column counts, margins, pane counts, navigation component choice, container max widths, type scale steps (L02 fluid type), responsive spacing.
- **Token encoding:** `breakpoint.md = {value: 48, unit: "rem"}` (Primer and Tailwind publish breakpoints as rem [S-L03-009, S-L03-017]); CSS media queries cannot read custom properties, so breakpoints are usually compiled into build-time variables [inferred].
- **Platform notes:** Android: use `WindowSizeClass` / `currentWindowAdaptiveInfo()`; large/XL need `supportLargeAndXLargeWidth = true` [S-L03-021]. iOS: size classes, not device idiom [S-L03-032]. Web: rem-based breakpoints respond to user font size [S-L03-072].
- **Accessibility constraints:** WCAG 1.4.10 Reflow: content must work at 320 CSS px wide without two-dimensional scrolling (equivalent to 1280px at 400% zoom) [S-L03-060], so the smallest layout must be complete, not a degraded fallback.
- **Default + heuristic:** Adopt Material's five width breakpoints for cross-platform products (they also map to web) [S-L03-025]; for web-only products take Tailwind's set. Express web breakpoints in rem. Design mobile first, then ask Material's five questions at each step: reveal, divide, resize, reposition, swap [S-L03-025].
- **Evidence:** [S-L03-002, S-L03-008, S-L03-009, S-L03-010, S-L03-016, S-L03-017, S-L03-018, S-L03-021, S-L03-025, S-L03-026, S-L03-032, S-L03-060, S-L03-072]

### DC-L03-15: Column grid (columns, gutters, margins)
- **Block path:** Foundations > Layout > Grid
- **Questions the designer answers:** How many columns at each breakpoint? Fixed or changing gutters? Do containers hang into gutters? Column grid or pane model?
- **Options:**
  - **4 / 8 / 16 "2x" grid**: Carbon doubles columns (4 at sm, 8 at md, 16 at lg and up), fixed 16px padding, 32px gutter by default, margins 0-24 [S-L03-002]; gutter modes wide 32, narrow 16 (container hangs into the gutter so type aligns), condensed 1px [S-L03-054].
  - **12 columns**: Bootstrap 12 at every breakpoint with 1.5rem gutters [S-L03-066]; Fluent says 12 is common because it divides into halves, thirds, quarters and sixths [S-L03-010].
  - **Pane model instead of columns**: Material now organizes adaptive layouts with panes, spacers (24dp) and margins (16dp compact, 24dp above), plus "rulers" as global alignment lines [S-L03-026, S-L03-071]; Primer uses 1-3 layout columns by viewport range [S-L03-008].
  - **Other grid types**: baseline, manuscript (single column), modular (rows x columns) [S-L03-010].
- **Visual effect:** more columns (16) enable fine, asymmetric, editorial compositions; 12 gives flexible symmetric splits; pane models give app-like, task-oriented layouts. Wide gutters separate independent items; narrow or gutterless grids make related content read as one surface [S-L03-002, S-L03-054]. Visible key lines (shared alignment edges) increase perceived harmony [S-L03-002].
- **Depends on (upstream):** DC-L03-14 breakpoints, DC-L03-01 base (gutters and margins should be scale steps [S-L03-010]).
- **Affects (downstream):** page templates, card grids, forms (Carbon: use wide gutters for form fields [S-L03-054]), dashboards, image galleries.
- **Token encoding:** `grid.columns.lg = 16` (`number`), `grid.gutter.lg = {32, px}`, `grid.margin.lg = {16, px}` (`dimension`); `layout.spacer.pane = 24dp`.
- **Platform notes:** native mobile rarely uses visible column grids; Material and Apple use margins, panes and layout guides instead [S-L03-026, S-L03-032].
- **Accessibility constraints:** reflow at 320 CSS px means the smallest grid must collapse to one column [S-L03-060].
- **Default + heuristic:** Web product: 4 / 8 / 12 columns (compact / medium / expanded+), gutter 16-24, margin 16 (compact) and 24 (medium+) to match Material [S-L03-026]. Choose 16 columns only for editorial or very wide dashboards. Rule: type never hangs into the gutter; containers may [S-L03-054].
- **Evidence:** [S-L03-002, S-L03-008, S-L03-010, S-L03-026, S-L03-032, S-L03-054, S-L03-060, S-L03-066, S-L03-071]

### DC-L03-16: Container model and max content width
- **Block path:** Foundations > Layout > Containers
- **Questions the designer answers:** Does content stretch with the window (fluid), stop at a max width (fixed), or mix? Centred or left-aligned? What happens on ultra-wide screens? How long can a line of text be?
- **Options:**
  - **Fluid**: Carbon "High-density interface model": full browser width, add columns in increments of 2; for complex product UIs, catalogs, dashboards [S-L03-074]. Bootstrap `.container-fluid` [S-L03-019].
  - **Fixed max width, centred**: Carbon "Editorial model" [S-L03-074]; Bootstrap `.container` 540 / 720 / 960 / 1140 / 1320 [S-L03-019]; Primer full pages limited to 1280 (xlarge) "so the content region doesn't render paragraphs with too many words per line" [S-L03-008].
  - **Fixed max width, left-aligned with nav**: Carbon "Product and docs model" [S-L03-074]; Primer split pages keep the pane flush left and let the content region have a max width [S-L03-008].
  - **Hybrid boxes**: Carbon: fixed in one dimension, fluid in the other (header: fluid width, fixed height; side panel: fixed width, fluid height; data table fluid both) [S-L03-002].
  - **Small fixed width**: Primer interstitial pages (sign-in, loading) max 320px [S-L03-008].
  - **Line length**: Material: keep text between 40-60 characters per line at all breakpoints [S-L03-025]; WCAG 1.4.8 (AAA): no more than 80 characters (40 CJK) [S-L03-073]; Apple provides readable-content layout guides that restrict text width [S-L03-032].
- **Visual effect:** fluid layouts feel like tools and use every pixel; centred max-width layouts feel like documents and marketing pages (calm, focused); left-aligned max width feels like docs/product with a stable navigation anchor [S-L03-074] [inferred for feel].
- **Depends on (upstream):** content type (reading vs scanning vs manipulating data), DC-L03-14, type measure (L02).
- **Affects (downstream):** page templates, hero sections, article layouts, tables (Confluence added a Max width option for wide tables [S-L03-051]), app shell.
- **Token encoding:** `layout.container.max = {value: 80, unit: "rem"}`; `layout.measure.max = 65ch` is not expressible in DTCG `dimension` (only px/rem) [S-L03-037], so keep `ch` values in CSS or convert [inferred].
- **Platform notes:** visionOS: keep content horizontally centred at very large window sizes [S-L03-032]; Android 16 ignores orientation and aspect-ratio locks on sw >= 600dp, so apps must fill the window instead of pillarboxing [S-L03-053].
- **Accessibility constraints:** WCAG 1.4.8 line width (AAA) [S-L03-073]; 1.4.10 reflow [S-L03-060].
- **Default + heuristic:** reading surfaces: centred, max about 1280px with text measure 40-80 characters; product surfaces: left nav + left-aligned content with max width; data surfaces: fluid. Let the builder ask "reading, working, or monitoring?" and pick Editorial / Product / High-density accordingly [S-L03-074].
- **Evidence:** [S-L03-002, S-L03-008, S-L03-019, S-L03-025, S-L03-032, S-L03-037, S-L03-051, S-L03-053, S-L03-060, S-L03-073, S-L03-074]

### DC-L03-17: Responsive spacing (does spacing change with breakpoint?)
- **Block path:** Foundations > Space > Responsive spacing
- **Questions the designer answers:** Do spacing tokens have different values per breakpoint, or do components pick a different step? Do margins grow on large screens?
- **Options:**
  - **Static tokens, step-jumping at breakpoints**: Carbon: "the tokens themselves do not change values based on the screen size", but it is acceptable to jump steps at breakpoints (e.g. `$spacing-05` at 1440px, `$spacing-03` at 768px) [S-L03-001].
  - **Layout spacing changes per breakpoint**: Material margins 16dp compact, 24dp medium+ [S-L03-026]; Primer content padding 16px up to large, 24px at xlarge+ [S-L03-008]; Carbon margins 0 / 16 / 16 / 16 / 24 [S-L03-002].
  - **Responsive props on layout primitives**: a search summary says Polaris web components accept per-screen-size spacing objects, but the primary Stack page read did not show this, so treat it as unverified [S-L03-075]; Primer lists a `useResponsiveValue` hook in its docs navigation (behaviour not read) [S-L03-008].
  - **Spacing modes per device in Figma**: Figma's example modes desktop/tablet/mobile for spacing [S-L03-057].
  - **Context-adaptive spacing**: Material spacing "should adapt to component size, layout, form factor, and other contexts"; "Desktop layouts can use more generous spacing than mobile layouts" [S-L03-030, S-L03-028].
- **Visual effect:** growing margins and section spacing on large screens keeps compositions balanced and prevents cramped-looking wide layouts; keeping component internals static preserves a consistent component identity across sizes [inferred].
- **Depends on (upstream):** DC-L03-14, DC-L03-04 (layout vs component spacing split).
- **Affects (downstream):** page margins, section spacing, card grid gaps, hero padding.
- **Token encoding:** layout tokens get breakpoint modes (`layout.margin` = 16 / 24 / 24 ...); component tokens have no breakpoint modes [inferred from Carbon + Material].
- **Platform notes:** on native, margins come from system layout guides and window size class [S-L03-032, S-L03-026].
- **Accessibility constraints:** none beyond reflow.
- **Default + heuristic:** Only layout-level spacing (margins, pane spacers, section gaps) varies by breakpoint; component spacing varies only by density, never by breakpoint.
- **Evidence:** [S-L03-001, S-L03-002, S-L03-008, S-L03-026, S-L03-028, S-L03-030, S-L03-032, S-L03-057]

### DC-L03-18: Canonical layouts and pane model
- **Block path:** Patterns > Layout > Canonical layouts
- **Questions the designer answers:** Which page archetypes does the product need (feed, list-detail, supporting pane, full page, split page)? How many panes per breakpoint? Fixed or flexible pane widths?
- **Options:**
  - **Material canonical layouts**: feed (configurable grid of cards), list-detail (two side-by-side panes), supporting pane (primary about two-thirds, secondary the rest) [S-L03-027]; panes per breakpoint: 1 compact, 1 (recommended) or 2 medium, 1 or 2 (recommended) expanded and large, 1-3 extra-large [S-L03-025]; fixed pane 360dp at expanded, 412dp at large/XL; side sheet third pane max 400dp; never more than three panes [S-L03-026].
  - **Primer page types**: full pages (centred content + pane, max 1280), split pages (pane flush left with independent scroll, for navigation/filtering/list-detail), interstitial (max 320) [S-L03-008].
  - **Carbon screen regions and panels**: header, global sidenav, local sidenav, content, footer, dialog; panels are flexible (collapsible), fixed, or floating [S-L03-002].
  - **Material adaptive strategies**: show and hide, levitate (float a pane over content), reflow; pane placements co-planar, floating, docked [S-L03-071].
- **Visual effect:** multi-pane layouts make large screens feel like productivity apps and keep context visible; single-pane layouts feel focused and immersive (video, games, creative work) [S-L03-025]. Material warns against two panes at medium width for high-density content [S-L03-025].
- **Depends on (upstream):** DC-L03-14, information architecture, navigation model (DC-L03-19).
- **Affects (downstream):** page templates, navigation components, sheets, dialogs, back behaviour on narrow screens (Primer: split into pages, bottom sheet, or stack vertically [S-L03-008]).
- **Token encoding:** `layout.pane.fixed.expanded = 360dp`, `layout.pane.fixed.large = 412dp`, `layout.pane.supporting.ratio = 0.333` (`number`).
- **Platform notes:** Compose ships canonical layout scaffolds and Navigation 3 for multi-destination layouts [S-L03-027, S-L03-071].
- **Accessibility constraints:** focus order and landmarks must follow visual pane order (L08 owns).
- **Default + heuristic:** Offer the three Material archetypes plus a full-page document template; default to one pane below 840dp, two panes from 840dp, three only at 1600dp+ [S-L03-025, S-L03-026].
- **Evidence:** [S-L03-002, S-L03-008, S-L03-025, S-L03-026, S-L03-027, S-L03-071]

### DC-L03-19: App shell regions and navigation placement
- **Block path:** Patterns > Layout > App shell
- **Questions the designer answers:** Which persistent regions does the product have (header, nav, content, panels, footer)? Where does primary navigation live at each breakpoint? Is the header fixed or scrolling?
- **Options:**
  - **Material swaps by breakpoint**: navigation bar (bottom) at compact; collapsed navigation rail at medium/expanded; modal or standard expanded navigation rail at expanded, large, extra-large. The current table lists no navigation drawer [S-L03-025]. Place navigation near reachable edges (bottom on compact) [S-L03-026].
  - **Apple**: switch from a tab bar to a sidebar when space grows; keep functionality the same across size classes and only change how much is visible [S-L03-032].
  - **Carbon UI shell regions**: header, global sidenav, local sidenav, dropdown menu, content, footer, dialog; panels flexible, fixed or floating; vertical panels fill full height [S-L03-002].
  - **Primer anatomy**: app header (never fixed, scrolls with page), context region, local navigation, left and right pane regions, footer region; narrow screens split list-detail into pages, show panes as bottom sheets, or stack vertically [S-L03-008].
  - **Fluent "re-architect"**: fork or collapse page elements by window size (list beside details on large screens) [S-L03-010].
- **Visual effect:** a bottom bar makes a product feel mobile-native and thumb-first; a rail feels app-like on tablets/desktops; a full sidebar feels like a desktop productivity tool; a scrolling (not fixed) header gives content more vertical room [inferred].
- **Depends on (upstream):** DC-L03-14, information architecture depth, platform conventions (L10).
- **Affects (downstream):** navigation components (bar, rail, sidebar, tabs), header, page templates, content max width (the nav steals width).
- **Token encoding:** `layout.rail.width.collapsed`, `layout.sidebar.width`, `layout.header.height` (`dimension`); Material fixed-pane widths as above [S-L03-026]. [Rail/drawer pixel widths not verified this session.]
- **Platform notes:** Liquid Glass on Apple platforms floats controls over content; extend backgrounds under sidebars, toolbars and tab bars [S-L03-032]. L00 reports iOS 27 (Sept 2026) added a user transparency slider from clear to fully tinted, so content scrolling under floating bars must stay legible across that whole range [S-L03-065].
- **Accessibility constraints:** consistent navigation location across pages (WCAG 3.2.3, L08 owns); reachable placement on touch.
- **Default + heuristic:** compact: bottom bar (3-5 destinations); medium: collapsed rail; expanded+: expanded rail or sidebar. Swap components only when they are functionally equivalent [S-L03-025].
- **Evidence:** [S-L03-002, S-L03-008, S-L03-010, S-L03-025, S-L03-026, S-L03-032]

### DC-L03-20: Safe areas, edge-to-edge and foldables
- **Block path:** Foundations > Layout > Safe areas
- **Questions the designer answers:** Does content draw behind system bars? How are insets applied? What do we do with hinges, cutouts, TV overscan?
- **Options / platform facts:**
  - **Apple**: respect the safe area so hardware such as the Dynamic Island and bars do not obscure content; extend full-screen backgrounds under sidebars, toolbars and tab bars; use a scroll edge effect instead of a solid background under controls (Liquid Glass) [S-L03-032]. tvOS: inset primary content 60pt top/bottom and 80pt at the sides [S-L03-032].
  - **Android**: edge-to-edge is enforced on Android 15 (API 35) when targeting SDK 35; handle system bar, display cutout and system gesture insets [S-L03-052]. Apps targeting Android 16 (API 36) cannot opt out on Android 16 devices [S-L03-053]. Material calls the reserved zones "safety regions" [S-L03-071].
  - **Web**: `env(safe-area-inset-top/right/bottom/left)` gives the safe distances (0 on rectangular viewports) [S-L03-079].
  - **Foldables and large screens**: Material defines fold (hinge or flexible area) and spacer between panes; compact layouts must transition when a device unfolds [S-L03-071, S-L03-026]. Android 16 ignores orientation, resizability and aspect-ratio restrictions on smallest width >= 600dp, and the temporary opt-out ends at API 37 [S-L03-053].
- **Visual effect:** edge-to-edge makes content feel immersive and modern (imagery under translucent bars); ignoring insets makes controls collide with the status bar, notch or gesture area [S-L03-052] [inferred for feel].
- **Depends on (upstream):** platforms (L10), app shell (DC-L03-19), materials/translucency (L04).
- **Affects (downstream):** top app bars, bottom bars, FABs, sheets, full-bleed media, scroll containers, dialogs on foldables.
- **Token encoding:** insets are runtime values, not tokens; tokens define extra padding added on top (`layout.safe.extra = 16`) [inferred].
- **Platform notes:** as above; web needs `viewport-fit=cover` to draw into unsafe areas (MDN summary, not quoted) [S-L03-079].
- **Accessibility constraints:** controls must stay inside safe, reachable regions; system gesture insets must not hold primary targets [S-L03-052].
- **Default + heuristic:** Always draw backgrounds edge-to-edge and pad interactive content by the platform insets plus the normal layout margin. Never place a split or tap target on a hinge [inferred from S-L03-071].
- **Evidence:** [S-L03-026, S-L03-032, S-L03-052, S-L03-053, S-L03-071, S-L03-079]

### DC-L03-21: Component-level responsiveness (container queries vs viewport media queries)
- **Block path:** Foundations > Layout > Responsive mechanism
- **Questions the designer answers:** Do components adapt to the viewport or to the space their container gives them? Do we publish container size tokens?
- **Options:**
  - **Viewport media queries** keyed to the breakpoint set (DC-L03-14) [S-L03-016, S-L03-018].
  - **Container size queries**: `container-type: inline-size | size | normal`, container units `cqw/cqh/cqi/cqb/cqmin/cqmax` [S-L03-055]; Baseline widely available since 2025-08-14 [S-L03-056]. Tailwind v4 ships 13 container sizes @3xs (16rem) to @7xl (80rem) [S-L03-016].
  - **Native equivalents**: Material components adapt "in relation to their containers, content, and pane boundaries" via resizing, showing/hiding, and presentation changes (e.g. FAB to extended FAB) [S-L03-071]; Apple adapts to size classes of the view's environment [S-L03-032].
- **Visual effect:** container-aware components look right in any slot (sidebar card vs main-column card) instead of breaking when placed in a narrow pane on a wide screen [inferred]. List items revealing more text as the container grows is Material's example [S-L03-071].
- **Depends on (upstream):** DC-L03-18 pane model (panes make container width diverge from window width), browser support targets.
- **Affects (downstream):** cards, list items, media objects, data tables, forms inside panes/sheets.
- **Token encoding:** `container.sm = {value: 24, unit: "rem"}` etc. (Tailwind's `--container-*` namespace [S-L03-017]).
- **Platform notes:** web only as CSS; native gets the same effect from layout APIs (L10).
- **Accessibility constraints:** container-based layouts still must reflow at 320 CSS px [S-L03-060].
- **Default + heuristic:** Page layout uses viewport breakpoints; components use container queries. Once a product has multi-pane layouts, container queries become the default for components [inferred].
- **Evidence:** [S-L03-016, S-L03-017, S-L03-018, S-L03-032, S-L03-055, S-L03-056, S-L03-060, S-L03-071]

### DC-L03-22: Responsive vs adaptive strategy
- **Block path:** Foundations > Layout > Adaptation strategy
- **Questions the designer answers:** One fluid layout that scales, or distinct layouts per context? Does the same screen change structure, components, or only size?
- **Options:**
  - **Responsive**: "one layout where the content is fluid", media queries render accordingly [S-L03-010]; Material: "responsive design scales a single layout to fit any screen" [S-L03-071].
  - **Adaptive**: "changes entirely based on the format", multiple fixed layout sizes [S-L03-010]; Material: "adaptive design customizes a product to optimize the experience on each device", adapting to people (preferences), devices (watch to XR) and usage (resizing, rotation) [S-L03-071]. Material renamed "Responsive layout" to "adaptive design" in May 2026 [S-L03-071].
  - **Mixed** (most real products): Fluent says "In some cases, a mix of adaptive and responsive design is the right choice" and lists reposition, resize, reflow, show/hide, re-architect [S-L03-010].
  - **Apple's constraint**: don't change functionality with space; change how much is visible [S-L03-032].
- **Visual effect:** responsive feels continuous (things stretch and wrap); adaptive feels native per device (different navigation, pane counts, component swaps) [inferred].
- **Depends on (upstream):** platforms, team capacity (adaptive costs more design and QA), content type.
- **Affects (downstream):** number of templates, component variants (FAB vs extended FAB), navigation swaps, test matrix.
- **Token encoding:** breakpoint modes for layout tokens; component-variant switching lives in code, not tokens [inferred].
- **Platform notes:** Android 16 forces resizable, full-window behaviour on large screens, which effectively forces adaptive layouts [S-L03-053].
- **Accessibility constraints:** keep the same content and functions available at every size (reflow [S-L03-060]; Apple guidance [S-L03-032]).
- **Default + heuristic:** responsive inside panes, adaptive between breakpoints (pane count, navigation component). Use Material's show-and-hide, levitate and reflow strategies as the named vocabulary [S-L03-071].
- **Evidence:** [S-L03-010, S-L03-032, S-L03-053, S-L03-060, S-L03-071]

### DC-L03-23: Layer order (z-index scale)
- **Block path:** Foundations > Layout > Layers (L04 owns elevation styling)
- **Questions the designer answers:** Which UI sits above which? Do we publish named layer tokens? How do we avoid z-index wars?
- **Options:**
  - **Atlassian**: 100 (no example), 200 Atlassian navigation, 300 inline dialog, 400 popup, 500 blanket (scrim), 510 modal, 600 flag, 700 spotlight, 800 tooltip; elevation levels sunken, default, raised, overlay; "Different UI can have the same elevation style, but each UI should apply a different z-index" [S-L03-040, S-L03-086].
  - **Bootstrap**: 1000 dropdown, 1020 sticky, 1030 fixed, 1040 offcanvas backdrop, 1045 offcanvas, 1050 modal backdrop, 1055 modal, 1070 popover, 1080 tooltip, 1090 toast; 1-3 for overlapping borders inside groups [S-L03-078].
  - **Pane placement model**: Material's co-planar, floating and docked panes and the "levitate" strategy [S-L03-071]; Carbon floating panels sit above content and must be dismissible [S-L03-002].
- **Visual effect:** a coherent layer order keeps tooltips above modals and toasts above everything, so overlays never appear "behind" things; the visual style of each layer (shadow, scrim) is L04's lane.
- **Depends on (upstream):** component inventory (L08), elevation styles (L04).
- **Affects (downstream):** dropdowns, popovers, modals, toasts/flags, sticky headers, onboarding spotlights.
- **Token encoding:** `layer.modal = 510` as DTCG `number` [S-L03-037 for number type]; named semantic layers only, never raw numbers in components [inferred].
- **Platform notes:** native platforms manage window/sheet stacking themselves; tokens matter mostly on web [inferred]. Newer web APIs (top layer via `popover`/`dialog`) reduce the need for z-index [not verified this session].
- **Accessibility constraints:** modal layers need focus management and scrims (L08).
- **Default + heuristic:** publish 6-8 named layers with gaps of 100 (Atlassian style) so new layers can slot in.
- **Evidence:** [S-L03-002, S-L03-037, S-L03-040, S-L03-071, S-L03-078]

### DC-L03-24: Whitespace personality and grouping
- **Block path:** Foundations > Space > Whitespace and hierarchy
- **Questions the designer answers:** Should the product feel airy/premium or dense/utilitarian? How strongly do we separate groups? How much space marks importance?
- **Options:**
  - **Airy / generous**: large section spacing and generous margins; Material: spacious layouts "feel calm and open"; "Desktop layouts can use more generous spacing" [S-L03-028]. Use negative space to give emphasis to important content [S-L03-028].
  - **Dense / utilitarian**: Material: denser layouts "feel more serious and focused" [S-L03-028]; Carbon: sections may be dense but "the whole page should not be crowded" [S-L03-001].
  - **Grouping by proximity**: NN/g: items close together are perceived as a group; minimal label-field spacing, larger space before the next pair [S-L03-061]; Material implicit grouping (proximity, open space) vs explicit grouping (outlines, dividers, shadows) [S-L03-028]; Apple: group related items with negative space, container shapes or separators [S-L03-032]; Carbon and Fluent: space can replace dividers entirely [S-L03-001, S-L03-010].
  - **Space as hierarchy**: more surrounding space = higher perceived importance; elements set too close can be overlooked [S-L03-001, S-L03-010].
- **Visual effect:** high ratio between inner and outer spacing (e.g. 8px inside a group, 32px between groups) reads as clear, confident, premium; low ratio (16 inside, 20 between) reads as muddled [inferred, grounded in proximity principle S-L03-061]. Implicit grouping (space only) feels lighter and more modern; explicit grouping (borders, cards) feels more structured and enterprise [inferred].
- **Depends on (upstream):** brand personality (L06), density strategy (DC-L03-10), content type.
- **Affects (downstream):** semantic spacing defaults, card usage vs plain sections, divider usage, section spacing on marketing pages.
- **Token encoding:** `space.section.sm/md/lg` (layout tier) plus the inner/outer semantic pairs.
- **Platform notes:** mobile has less room; Material recommends more generous spacing on desktop [S-L03-028].
- **Accessibility constraints:** crowded layouts increase cognitive load; Carbon: dense information "can be disorienting or overwhelming" [S-L03-001].
- **Default + heuristic:** keep an inner:outer spacing ratio of at least 1:2 (and 1:3-1:4 for airy brands); prefer implicit grouping and add borders only where interactivity or scanning needs them [inferred].
- **Evidence:** [S-L03-001, S-L03-010, S-L03-028, S-L03-032, S-L03-061]

### DC-L03-25: Vertical rhythm and text-spacing resilience
- **Block path:** Foundations > Space > Vertical rhythm
- **Questions the designer answers:** Do we align text to a baseline grid? How do we stop line-height from adding stray space? Do layouts survive users enlarging text or spacing?
- **Options:**
  - **Baseline grid**: Fluent describes baseline grids that establish vertical rhythm, useful when content spans columns [S-L03-010].
  - **Box-based rhythm**: Carbon sets vertical spacing between sections with the fixed sizing scale added to box margins; "Spacer snaps to the text box and does not necessarily need to snap to the mini unit" [S-L03-002].
  - **Trim line-height**: Curtis's team used negative-margin math to cancel line-height above and below text [S-L03-039]; CSS `text-box` (trim) now does this natively in Chrome/Edge 133 and Safari 18.2 but not Firefox, so it is not Baseline [S-L03-077].
  - **Flexible heights**: Apple: support Dynamic Type by letting rows grow and stacks reflow vertically [S-L03-032]; WCAG 1.4.12 requires layouts to survive line height 1.5x, paragraph spacing 2x, letter spacing 0.12x, word spacing 0.16x [S-L03-076].
- **Visual effect:** consistent vertical rhythm makes long pages feel orderly and "typeset"; stray line-height space makes padding look uneven (top looks bigger than bottom) [S-L03-039] [inferred for feel].
- **Depends on (upstream):** type scale and line heights (L02), base unit.
- **Affects (downstream):** text components, cards, list items, buttons (optical centring), section spacing.
- **Token encoding:** line heights on the 4px grid (L02); section spacing tokens on the scale.
- **Platform notes:** native platforms size text boxes differently from CSS; trimming behaviour differs [inferred; L02/L10].
- **Accessibility constraints:** 1.4.12 [S-L03-076]; avoid fixed heights on text containers so enlarged text is not clipped [S-L03-032].
- **Default + heuristic:** snap line heights and spacing to 4px; measure spacing from the text box (Carbon) rather than enforcing a strict baseline grid on the web; use `text-box` as progressive enhancement [S-L03-002, S-L03-077].
- **Evidence:** [S-L03-002, S-L03-010, S-L03-032, S-L03-039, S-L03-076, S-L03-077]

### DC-L03-26: Units and token encoding across platforms
- **Block path:** Foundations > Tokens > Dimension encoding
- **Questions the designer answers:** Do spacing tokens use px or rem on the web? How do they map to pt and dp? How do we store them in DTCG and in Figma?
- **Options / facts:**
  - **DTCG 2025.10**: `$type: "dimension"`, `$value: {"value": <number>, "unit": "px" | "rem"}`; only px and rem allowed; `number` type for unitless values [S-L03-037]. The Sept 2026 draft keeps this and adds that px equals Android dp and iOS pt, and translators SHOULD convert [S-L03-038].
  - **Native units**: Fluent's ramp is measured in pt on iOS, dp on Android, px on web [S-L03-010]; Material: 1dp = 1 physical px at 160 dpi; dp = px x 160 / density [S-L03-029].
  - **rem on web**: Carbon, Atlassian and Primer publish rem and px side by side [S-L03-001, S-L03-003, S-L03-009]; Tailwind's base is `0.25rem` and its breakpoints are rem [S-L03-017].
  - **Mixed rem/px (practitioner view)**: rem for font sizes and media queries; px for padding, horizontal spacing and borders, because scaling spacing with font size squeezes content further [S-L03-072] (Tier B opinion; contradicts rem-everything systems).
  - **Figma**: number variables are unitless and take units from the bound property; they bind to padding and gap, width/height, layout-guide gutter/margin/count, stroke weight and radius [S-L03-080]; modes model device sizes or screen-based spacing [S-L03-057].
- **Visual effect:** rem spacing grows when users raise their default font size (layouts stay proportional but get roomier); px spacing stays fixed so text gets more room relative to padding [S-L03-072].
- **Depends on (upstream):** platforms, accessibility stance, token pipeline (L07).
- **Affects (downstream):** every dimension token, code generation (CSS, Swift, Kotlin), Figma variable collections.
- **Token encoding (examples across tiers):**
  - primitive: `space.200 = {"$type": "dimension", "$value": {"value": 16, "unit": "px"}}`
  - semantic: `space.inset.md = {"$type": "dimension", "$value": "{space.200}"}`
  - component: `button.padding.inline.md = "{space.inset.md}"`
  - layout number: `grid.columns.expanded = {"$type": "number", "$value": 12}`
- **Platform notes:** export px tokens as pt (iOS) and dp (Android) 1:1 [S-L03-038]; export rem only to web.
- **Accessibility constraints:** WCAG 1.4.4 resize text (L02) and 1.4.10 reflow [S-L03-060] favour rem-based breakpoints so enlarged text triggers narrower layouts [S-L03-072].
- **Default + heuristic:** author tokens in px (maps cleanly to pt/dp and Figma), then transform to rem for web type and breakpoints; let the builder offer "spacing scales with text size" as an explicit toggle rather than a hidden default [inferred].
- **Evidence:** [S-L03-001, S-L03-003, S-L03-009, S-L03-010, S-L03-017, S-L03-029, S-L03-037, S-L03-038, S-L03-057, S-L03-060, S-L03-072, S-L03-080]

## Decision graph for this lane (what drives what)

Upstream inputs from other lanes and from the product brief, then the order in which L03 decisions should be asked. Each arrow means "constrains or sets defaults for". All edges are [inferred] from the cards above unless a card cites a source for that dependency.

1. **Product brief** (audience, content type: reading / working / monitoring; platforms; input: touch / pointer) -> density strategy (DC-10), container model (DC-16), breakpoint set (DC-14), target minimums (DC-12).
2. **Typography base size and line heights (L02)** -> base unit (DC-01) -> spacing scale (DC-02) -> naming (DC-03).
3. **Spacing scale** -> semantic spacing (DC-04) -> inset shapes (DC-05) -> control heights (DC-07) together with **target minimums** (DC-12).
4. **Control heights** -> icon sizes (DC-08) and row heights -> density modes (DC-11) change inset, stack and height tokens but never target minimums.
5. **Breakpoints** (DC-14) -> column grid or pane model (DC-15) -> canonical layouts (DC-18) -> app shell and navigation placement (DC-19) -> responsive spacing on layout tokens only (DC-17).
6. **Pane model** -> container queries for components (DC-21); **platform** -> safe areas and edge-to-edge (DC-20); adaptation strategy (DC-22) decides how much structure changes at each breakpoint.
7. **Brand personality (L06)** + density -> whitespace personality (DC-24): the inner:outer spacing ratio and section spacing.
8. **All of the above** -> token encoding (DC-26): px vs rem, DTCG `dimension`, Figma number variables and modes.

Visual levers a builder can expose as sliders, with their main visible effect:
- **Base unit and scale shape**: how distinct spacing levels look (chunky vs fine-grained).
- **Inner:outer spacing ratio**: how clearly groups read; airy/premium vs muddled.
- **Default control height (32 / 40 / 48)**: desktop-tool vs touch-friendly vs expressive feel.
- **Density mode**: how much fits on screen; serious/focused vs calm/open [S-L03-028].
- **Container model**: document-like (centred max width) vs tool-like (fluid).
- **Grouping style**: implicit (space only) vs explicit (borders, cards, dividers) [S-L03-028].

## Questionnaire extract (plain-language questions for the builder, in order)

1. Who uses this most: people reading, people working through tasks, or people monitoring lots of data? (sets density, container model)
2. Which platforms and inputs: web only, iOS, Android, desktop apps; touch, mouse, both? (sets targets, units, breakpoints)
3. What is your body text size and line height? (sets base unit)
4. Should spacing steps be few and obvious (8-based) or many and fine (4-based)?
5. How big should a standard button or input be: 32, 40 or 48?
6. Do users need a compact mode they can switch on?
7. How many layout sizes do you design for: phone only, phone + tablet, up to large desktop?
8. Should wide screens show more columns/panes, or keep content centred at a max width?
9. Where does main navigation live on phones and on desktops?
10. Should groups be separated by space alone, or by borders and cards?
11. Should spacing grow when users enlarge their browser text?

## Open questions / gaps

- **Polaris web components pixel values**: the Stack page lists keyword sizes (`small-500` to `large-500`) but I did not find their px values on the pages read [S-L03-006].
- **Material 3 spacing tokens on web and Views**: marked "Unavailable" for MDC-Android and web; Compose only today [S-L03-030]. Whether Material Web will adopt `md.sys.measurement.space*` is unknown.
- **Material navigation rail and drawer widths** and Apple layout margin values (for example 16/20pt system margins) were not verified this session; Apple's HIG exposes layout guides but the page read gives no numeric margins for iOS [S-L03-032].
- **Atlassian avatar pixel sizes** beyond 16px, and Atlassian component heights (for example button default/compact), not verified [S-L03-064].
- **Fluent 2 density**: Fluent web has size props but I found no documented global density mode; WinUI "compact sizing" exists per a search snippet but was not verified on a primary page [S-L03-049].
- **Salesforce SLDS 2 density token values**: the SLDS 2 density page did not render; only the LWC developer guide behaviour (label placement, comfy/cozy/compact) is confirmed [S-L03-069, S-L03-070]. The "30% more density" figure from search snippets is unverified.
- **Spectrum 2 website** (spectrum.adobe.com) did not render; values come from the `spectrum-design-data` token source, which may run ahead of or behind the published docs [S-L03-014, S-L03-044].
- **Web top layer (`popover`, `<dialog>`)** as a replacement for z-index scales was not verified this session.
- **Figma plan limits for modes** (relevant to density x breakpoint x theme mode combinations): not on the page read; L07 owns [S-L03-057].
- **No community (Tier C) signal** on spacing, grids, density or targets appeared in the L00 pulls for the last 30 days (checked `sources/COMMUNITY-SIGNAL.md` and the raw files); absence of signal is not evidence of consensus.

## Confidence

**Confirmed against live Tier A sources today (2026-09-23):**
- All spacing scale values in table A (Carbon, Atlassian, Material 3, Fluent global and web, Primer, Spectrum token source, Polaris React source, Tailwind, Bootstrap).
- All breakpoint values in table B, including Material's five breakpoints and the May 2026 rename, Android height classes, Carbon grid columns/margins/gutters, Primer viewport ranges and paddings, Bootstrap containers and gutters, Tailwind breakpoints and container sizes.
- Control heights in table C, target sizes (Apple, Material, WCAG 2.5.8 / 2.5.5, Windows), Material density scale rules, Salesforce density behaviour, Confluence compact mode, Atlassian and Bootstrap z-index values, Android 15/16 edge-to-edge and large-screen changes, DTCG 2025.10 dimension type and the Sept 2026 draft's dp/pt note, container query Baseline date, text-box support status, WCAG 1.4.8 / 1.4.10 / 1.4.12 texts.

**Tier B, used with corroboration:** Nathan Curtis's inset/squish/stretch/stack/inline vocabulary (2016; corroborated by Material's padding/gap/margin model and Carbon's Stack) [S-L03-039]; NN/g proximity [S-L03-061]; Josh Comeau's rem/px split (opinion; flagged as contrasting with rem-everything systems) [S-L03-072]; Atlassian community post on Confluence compact mode (vendor staff) [S-L03-051].

**Reconciled with `sources/COMMUNITY-SIGNAL.md` (sections a-e, read 2026-09-23):** no community item disputes any spacing, grid, breakpoint, density or target value used here. Two caveats were added from it: Material 3 Expressive component sizes are not yet in a stable Compose release (DC-L03-07), and iOS 27's user-controlled Liquid Glass transparency affects content under floating bars (DC-L03-19). Which Compose release ships `md.sys.measurement.space*` was not verified.

**Inferred (clearly tagged in cards):** the cross-system "hybrid scale" pattern; visual-feel descriptions not quoted from a source (for example "32px reads as desktop productivity"); the inner:outer ratio heuristic; recommended defaults; the decision graph edges; DTCG encoding of squish insets as two tokens; density-on-semantic-layer recommendation.

## Cross-lane notes

- [L03 -> L02] Material says keep text at 40-60 characters per line across breakpoints [S-L03-025]; WCAG 1.4.8 (AAA) caps at 80 (40 CJK) [S-L03-073]; WCAG 1.4.12 text-spacing overrides must not break layouts [S-L03-076]. Confluence's 2026 "compact density" is implemented as smaller font size + tighter line spacing, so density is partly a typography decision [S-L03-051]. CSS `text-box` trim is not Baseline (no Firefox) [S-L03-077].
- [L03 -> L04] Atlassian z-index/layer table and Bootstrap z-index scale are in DC-L03-23; L04 owns elevation styling. Border width scale 1/2/4 (Primer, Spectrum) in DC-L03-09. Apple's Liquid Glass guidance asks for scroll-edge effects rather than solid bars under controls [S-L03-032].
- [L03 -> L05] Carbon pairs 16/20px icons with 14/16px text and says not to alter the icon-text ratio [S-L03-062]; Spectrum ships desktop/mobile icon sizes and in Sept 2026 (React Spectrum v1.7) refreshed icon sizing to match text line height [S-L03-044, S-L03-031]; Fluent adds 2/6/10px spacing steps specifically to align icons to the 4px grid [S-L03-010].
- [L03 -> L07] Material 3 now ships system spacing tokens `md.sys.measurement.space0-900` (Compose only) and is renaming component tokens from `*-space` to `padding`/`gap`/`margin` with positional words [S-L03-030]. Figma variables now include Timing and Easing types in addition to color/number/string/boolean; number variables are unitless [S-L03-080]. DTCG draft (2026-09-08) states px maps to Android dp and iOS pt [S-L03-038]. Spectrum tokens model platform scale as `sets: {desktop, mobile}` inside one token [S-L03-044].
- [L03 -> L08] Control height ladders (table C), Material Expressive button sizes 32/40/56/96/136dp with 48dp targets for XS/S [S-L03-059, S-L03-058], Carbon data table row sizes [S-L03-043], Salesforce forms move labels inline in compact density [S-L03-070].
- [L03 -> L10] Android 16 (API 36): no edge-to-edge opt-out; orientation/resizability/aspect-ratio locks ignored on sw >= 600dp; temporary opt-out ends at API 37 [S-L03-053]. Material: "breakpoints (previously window size classes)", large/XL need `supportLargeAndXLargeWidth` in material3.adaptive [S-L03-021, S-L03-025]. Apple: decide layout by size class, not device idiom or orientation [S-L03-032]. Material now frames layouts as mobile / desktop / spatial (XR) experience types [S-L03-071].
- [L03 -> L06] Material explicitly ties spacing to personality: denser feels "serious and focused", spacious feels "calm and open" [S-L03-028]; use as the bridge from brand attributes to spacing tokens.
