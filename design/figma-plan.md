# Figma plan: building the starter system natively

This is the run sheet for writing the D1 work into Figma through the remote MCP. Every step is a ready-made script in `design/figma-scripts/`, generated from `design/tokens/`, so Figma and the token files can't drift. The scripts were syntax-checked and run end to end against a mock of the Plugin API (twice, to prove idempotency). They have not been run in real Figma yet.

## 1. What the remote MCP must provide

| Need | Why | Source |
|---|---|---|
| The **remote** server `https://mcp.figma.com/mcp`, OAuth done, listed as `figma` | Every write tool is remote-only. The desktop server connected today is read-only, and it can shadow the remote tool names | S-L16-001, S-L16-003, S-L16-004 |
| **Full seat** with edit rights on the target file | Needed to write to the canvas | S-L16-002, S-L16-022 |
| `use_figma` | Runs Plugin API JavaScript that creates variables, styles, components and frames | S-L16-001, S-L16-002 |
| `create_new_file` (optional) | Makes a clean Design file in drafts, so the first run doesn't touch a real file (Figma advises testing on a copy) | S-L16-001, S-L16-002 |
| `generate_figma_design` (optional) | Captures the four HTML artboards as editable layers (section 6) | S-L16-003, S-L16-024 |
| `get_metadata`, `get_screenshot`, `get_variable_defs` | Checking the result | S-L16-001 |
| A **paid plan** (Professional or higher) | Starter lists no variable modes. These scripts use at most 2 modes per collection (Pro allows 10) | S-L07-014 |

**How `use_figma` is called** (Figma's own `figma-use` skill, fetched 2026-09-23, source F-1): parameters `fileKey`, `code`, `description`, `skillNames`. `skillNames` must include `figma-use`, or `resource:figma-use` if the skill was loaded as an MCP resource. The code runs inside an async wrapper: top-level `await` is allowed, `return` is the only output, don't use an IIFE, don't call `figma.notify` or `closePlugin`, and switch pages at most once per call. **Pass each `.js` file's full contents as `code`.** Each script returns a short summary (under 2 KB), well below the 20 KB response cap (S-L16-002).

## 2. Run order

Run these one call at a time, in order. Every script finds things by name and updates them, so re-running a step is safe. On an error, follow `safeToRetryWithoutCanvasRead` (F-1).

| Step | File | Creates | Expected return |
|---|---|---|---|
| 0 | `00-inspect.js` | nothing (read-only) | pages, collections, styles, and the available Inter / JetBrains Mono styles |
| 1 | `01-pages.js` | pages: Cover, Foundations, Components, Atlas · Building blocks, Atlas · Builder concept | 5 page ids |
| 2 | `02-primitives.js` | collection **Primitives** | 181 variables, `timingType: "TIMING"` |
| 3 | `03-color.js` | collection **Color** (Light, Dark) | 59 variables |
| 4 | `04-spacing-radius.js` | collections **Spacing** (Comfortable, Compact) and **Radius** (Default) | 20 + 9 variables |
| 5 | `05-typography.js` | collection **Typography** (Default) + 15 text styles | 22 variables, 15 style ids |
| 6 | `06-motion.js` | collection **Motion** (Standard, Reduced) | 16 variables |
| 7 | `07-effects.js` | effect styles `elevation/raised`, `elevation/overlay`, `focus/ring` | 3 ids |
| 8 | `08-icons.js` | components `icon/plus`, `icon/spinner` (Components page) | 2 ids |
| 9-13 | `09-button-primary.js` … `13-button-danger.js` | one component set per variant | 18 variants each |
| 14 | `14-validate.js` | nothing (read-only) | the counts in this table, `unscopedSemantic: 0` everywhere |

Steps 9-13 all write to the Components page, so run them one after another, not in parallel. They skip a set that already exists; set `REBUILD = true` at the top of a file to rebuild that set. After step 14, call `get_screenshot` on the Components page (F-1 asks for one screenshot after composing and one after any fix).

## 3. Variable collections

One collection per tier or per independent theming axis, so mode counts add up instead of multiplying (DC-L07-18). Names use slash groups, which mirror the token paths (`color.text.primary` becomes `color/text/primary`, S-L07-011).

| Collection | Modes | Variables | Contents | Scopes | Publishing |
|---|---|---|---|---|---|
| Primitives | Value | 181 | 146 colors (6 hues × 12 steps × light/dark, plus white and black), 15 space, 9 radius, 3 border widths, 8 durations | none (`[]`), so no picker shows them | hidden (DC-L07-19) |
| Color | Light, Dark | 59 | surface, text, bg, border, icon, overlay, shadow roles, all aliased to Primitives except the alpha scrim and shadow colors | surface/bg: FRAME_FILL, SHAPE_FILL · text: TEXT_FILL · icon: SHAPE_FILL, STROKE_COLOR · border: STROKE_COLOR · overlay: FRAME_FILL · shadow: EFFECT_COLOR | published |
| Spacing | Comfortable, Compact | 20 | `space/inset/*`, `space/gap/*` (compact is one step smaller), `space/layout/*`, `size/control/*`, `size/icon/*`, `size/target/min` | GAP; sizes WIDTH_HEIGHT | published |
| Radius | Default | 9 | `radius/detail`, `control`, `container`, `overlay`, `full`, `border/width/default`, `selected`, `focus/ring/width`, `offset` | CORNER_RADIUS; STROKE_FLOAT; focus STROKE_FLOAT + EFFECT_FLOAT | published |
| Typography | Default | 22 | `font/family/sans` (Inter), `font/family/mono` (JetBrains Mono), 3 weights, 9 sizes, 8 line heights | FONT_FAMILY, FONT_WEIGHT, FONT_SIZE, LINE_HEIGHT | published |
| Motion | Standard, Reduced | 16 | semantic durations (TIMING, aliased), 4 easings (STRING, CSS `cubic-bezier`), transitions `feedback`, `enter`, `exit` as duration + easing pairs; Reduced swaps enter and exit to 100 ms fades | none | published |

**Code syntax** is written on every variable from one rule, so Dev Mode, MCP output and captures all use the same names as code (DC-L07-20, L16 Part A "code syntax as the join key"). Web: `var(--color-text-primary)`. iOS and Android: `DSColor.textPrimary`, `DSSpace.insetLg`. The rule lives in the script prelude. The iOS and Android naming is [inferred]: rename it in one place if the codebase differs.

**What DTCG maps to what** (L07 A7). Color objects go in as sRGB hex from each token's `hex` fallback. Figma's native DTCG import accepts only sRGB or HSL, so the OKLCH primitive files can't be dragged in, and `use_figma` avoids that problem. Dimensions go in as px numbers. Durations become TIMING variables in seconds (F-2). `cubicBezier` becomes a STRING, because the value shape for Figma's EASING type wasn't verified. Typography composites become text styles, and shadows become effect styles (DC-L07-21). The DTCG resolver's three modifiers become three collections with modes: theme to Color, density to Spacing, motion to Motion.

## 4. Styles

- **15 text styles**, `text/display` through `text/code/sm`. Font family and weight are set on the style; `fontSize` and `lineHeight` are bound to Typography variables; letter spacing is in px; `text/label/sm` is uppercase. Each style's description carries its use / avoid note. The script reads the real style names from `listAvailableFontsAsync` (for example "Semi Bold" vs "SemiBold"), as F-1 requires.
- **3 effect styles.** `elevation/raised` has 2 drop shadows; `elevation/overlay` has 3 (contact, ambient with -4 spread, and a 1px ring). `focus/ring` is a 2px spread in the surface color plus a 4px spread in `border.focus`. Every shadow color is bound to a Color variable, so switching a frame to Dark swaps the shadow alphas and turns on the edge ring (DC-L04-12).

## 5. Button as component sets

Figma's `figma-generate-library` guidance caps a component set at 30 combinations and says to split by a primary axis above that (F-3). Five variants × three sizes × six states would be 90, so the script builds **five sets**: `Button/Primary`, `Button/Secondary`, `Button/Outline`, `Button/Ghost` and `Button/Danger`.

- **Variant properties:** `Size` = sm, md, lg; `State` = Enabled, Hover, Focus-visible, Pressed, Disabled, Loading. That gives 18 variants per set, laid out as a grid with one column per state and one row per size.
- **Other properties** (DC-L07-22): `Label` (TEXT), `Leading icon` (BOOLEAN, which toggles the icon's visibility), `Icon` (INSTANCE_SWAP, default `icon/plus`).
- **Bindings on every variant:**
  - height: `size/control/*`
  - padding: `space/inset/md`, `lg` or `xl`, by size
  - gap: `space/gap/sm`
  - corner radius: `radius/control`
  - fill: the state's Color variable
  - outline stroke: `color/border/default`, width `border/width/default`
  - label: text style `text/label/lg`, with the label color variable
  - icon and spinner strokes: the label color
  - Focus-visible: effect style `focus/ring`
- **Loading:** the spinner is visible and the label stays. **Disabled:** `color/bg/disabled` and `color/text/disabled`.

The same token map is drawn in `design/atlas/03-button.html`, group 03.5.

## 6. Pages and the atlas artboards

| Page | Content | How it gets there |
|---|---|---|
| Cover | Title frame (optional) | a hand-written `use_figma` call, or leave empty |
| Foundations | The foundations specimen | capture `02-foundations.html` (below), then set the dark panels' frames to the Dark mode of Color if they are later rebuilt natively |
| Components | icons + the 5 Button sets | steps 8-13 |
| Atlas · Building blocks | `01-building-blocks-map.html` | capture |
| Atlas · Builder concept | `04-builder-concept.html` | capture |

**Capture** (`generate_figma_design`) takes a live browser page (localhost, staging or production) and lands it as editable layers in a new or existing file. It binds variables by matching CSS variable names to code syntax, then names, then scope (S-L16-003, S-L16-024). To serve the artboards: `python3 -m http.server 8765 --directory design/atlas`, then capture `http://localhost:8765/0N-*.html` for each artboard. Caveats:
- The artboards use literal values, not CSS variables (chosen for Paper), so captured layers come in mostly unbound. Treat them as review boards, not as the library.
- Captures are flat layers with no component instances (S-L16-022).
- The tool's exact parameters were not verified from its schema. Read the schema when the server connects.

## 7. Checks after writing

1. `14-validate.js` returns: Primitives 181 (Value), Color 59 (Light, Dark), Spacing 20 (Comfortable, Compact), Radius 9, Typography 22, Motion 16 (Standard, Reduced), 15 text styles, 3 effect styles, 5 component sets with 18 variants each and the properties Label, Leading icon and Icon. Semantic collections should report `unscopedSemantic: 0`.
2. `get_variable_defs` on a Primary / md / Enabled variant lists `color/bg/accent/bold`, `color/text/onAccent`, `space/inset/lg`, `space/gap/sm`, `radius/control` and `size/control/md`.
3. `get_screenshot` of Components in Light, then set the page to Dark mode for Color and screenshot again. Colors should match `design/atlas/03-button.html`.

## 8. Unverified points and fallbacks

- **TIMING type.** The Plugin API added TIMING and EASING in August 2026 (S-L07-013, S-L07-034). If TIMING throws, step 2 falls back to FLOAT milliseconds and step 6 follows whatever type step 2 created.
- **EASING values.** The value shape wasn't found in the docs read. Easings are STRING variables, and upgrading them is a later, one-line change.
- **JetBrains Mono.** It is a Google font and usually available in Figma, but `use_figma` can use only fonts the account has access to (S-L16-002). If it is missing, step 5 falls back to Roboto Mono and says so in `warnings`.
- **`strokeWeight` binding** on component strokes is assumed from the Plugin API's bindable fields. If it throws, remove that one line in 11-button-outline.js and set a 1px stroke.
- **Usage cost.** Writing to the canvas is a free beta that will become usage-priced (S-L16-007). About 16 calls cover the whole plan.

## Sources used by this plan

- S-ids: `research/L16-visual-tooling-for-engineers.md` (Part A, G2) and `research/L07-tokens-figma.md` (A6, A7, DC-L07-18 to DC-L07-22).
- Fetched by D1 on 2026-09-23. These are not in any lane trace; add them to a trace if kept.
  - **F-1** `github.com/figma/mcp-server-guide/skills/figma-use/SKILL.md`: `use_figma` parameters, execution model, critical rules.
  - **F-2** `.../figma-use/references/variable-patterns.md`: `createVariable` signature, the scope list, `setVariableCodeSyntax`, and TIMING in seconds.
  - **F-3** `.../figma-generate-library/references/component-creation.md`: the 30-combination cap, `combineAsVariants`, `addComponentProperty`, and SVG icon components.
