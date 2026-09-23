# L07: Tokens architecture & Figma

Lane: L07 (Tokens architecture & Figma). Author: orchestrator subagent L07. Started 2026-09-23.
Status: done (2026-09-23). 28 Decision Cards, a DTCG `$type` reference table (A3), a Figma capabilities table (A6), a cross-system tier table (A8), a pipeline tools table (A9) and a suggested builder data model (Part C).
Source ids refer to `traces/L07-trace.md`. Every claim is tagged `[S-L07-xxx]` or `[inferred]`. `[S-L07-100..126]` is shorthand for the helper-sourced rows in that range.

## Lane overview

**What this lane covers.** This lane covers the data layer under a design system: how tokens are tiered and named, the standard file format (DTCG), how Figma stores and exposes the same decisions, and how tokens travel to code. It is the lane most likely to define the builder's internal data model.

**Five things that matter most for the builder**
1. **The token standard is stable.** The DTCG published "Design Tokens Format Module 2025.10" (plus Color and Resolver modules) on 28 Oct 2025 as a stable Final Community Group Report. It is not a W3C Standard. No newer version exists as of 23 Sep 2026. Theming is not part of the token file itself; it lives in a separate **Resolver** document (sets, modifiers, contexts, resolution order) [S-L07-002] [S-L07-004] [S-L07-006] [S-L07-007].
2. **Figma now speaks DTCG natively, but only partly.** It imports and exports DTCG JSON, one file per mode. Import accepts only sRGB/HSL colors, px dimensions, second-based durations, font family strings, numbers and (non-standard) strings. Composites such as typography and shadow do not come in as variables [S-L07-011].
3. **Figma's variable model grew in 2025-26.** It now has six variable types (timing and easing were added for Figma Motion; easing can be a spring). Mode caps rose to 10 per collection on Professional and 20 on Organization. Enterprise gets extended collections for multi-brand. Slots became a fifth component property. Check designs, a linter with no LLM, is available on Org/Ent. The MCP server has write tools (`use_figma`), and `create_design_system_rules` is now a prompt [S-L07-013] [S-L07-014] [S-L07-015] [S-L07-022] [S-L07-025] [S-L07-027].
4. **Tiers: everyone has raw and semantic layers; component tokens are optional.** Material, Primer, Carbon and Spectrum publish component tokens. SLDS 2's are still beta. Atlassian and Polaris have none. Figma's own course says component tokens "might not be necessary for everyone". Themes always live on the semantic layer [S-L07-050] [S-L07-100] [S-L07-109] [S-L07-112] [S-L07-117] [S-L07-120] [S-L07-125].
5. **Pipelines have consolidated on DTCG.** Terrazzo 2.x fully supports DTCG 2025.10 including resolvers. Style Dictionary v5 supports 2025.10 colors and dimensions but not resolvers yet. zeroheight moved to DTCG 2025.10 and Style Dictionary v5. Specify shut down in Nov 2024. Practitioners mostly treat code, not Figma, as the source of truth [S-L07-179] [S-L07-155] [S-L07-203] [S-L07-186] [S-L07-045].

**How to read this file.** Part A holds the reference tables. Part B holds the Decision Cards, in order: tiers and naming (01-07), source of truth and format (08-09), value types (10-14), theming (15-17), Figma structure (18-22), lifecycle and AI (23-24), pipeline (25), governance and plan (26-27), layout (28). Part C sketches the builder data model.

---

## Part A. Reference tables

### A1. DTCG specification status (verified 2026-09-23)

| Item | Fact | Evidence |
|---|---|---|
| Name of first stable version | "Design Tokens Format Module 2025.10" (plus sibling "Design Tokens Color Module 2025.10" and "Design Tokens Resolver Module 2025.10") | [S-L07-002] [S-L07-003] [S-L07-004] |
| Status | "Final Community Group Report", published as a "Candidate Recommendation" by the DTCG; "considered stable"; explicitly "not a W3C Standard nor ... on the W3C Standards Track" | [S-L07-002] |
| Date | 28 October 2025 (all three modules) | [S-L07-002] [S-L07-003] [S-L07-004] [S-L07-006] |
| Format editors | Louis Chenais, Kathleen McMahon, Drew Powers, Matthew Strom-Awn, Donna Vitan | [S-L07-002] |
| Announced tool support | Reference implementations named: Style Dictionary, Tokens Studio, Terrazzo. "Already support or implementing": Penpot, Figma, Sketch, Framer, Knapsack, Supernova, zeroheight | [S-L07-006] |
| Newer version? | None announced as of 2026-09-23. The editor's draft (dated 08 Sep 2026) still carries the 2025.10 content and is labelled "preview, do not implement". The DTCG blog has no status post after 28 Oct 2025; a 17 Jun 2026 post restates that Figma, Penpot, Sketch, Tokens Studio, Style Dictionary and Terrazzo support the spec | [S-L07-001] [S-L07-007] [S-L07-008] |
| File extension / media type | `.tokens` or `.tokens.json`; `application/design-tokens+json` (preferred) or `application/json` | [S-L07-002] |
| Resolver file | `.resolver.json`, served as `application/json` | [S-L07-004] |

Note on naming: people often call this "DTCG 1.0". Figma's Schema 2025 recap calls it the "W3C Design Tokens Community Group 1.0 specification" [S-L07-038]. The spec itself uses the version label **2025.10** [S-L07-002]. The builder should use "DTCG 2025.10" to be exact.

### A2. DTCG 2025.10 file anatomy (reserved properties)

| Property | Where | Rule | Evidence |
|---|---|---|---|
| `$value` | token | Required. Its presence is what makes an object a token rather than a group | [S-L07-002] |
| `$type` | token or group | Optional on the token if it can be inherited from the closest ancestor group or resolved from an alias. If no type can be determined, the token is invalid, and tools must not guess the type from the value | [S-L07-002] |
| `$description` | token or group | Plain string | [S-L07-002] |
| `$extensions` | token or group | Vendor data under reverse-domain keys (for example `com.figma.type`). Tools MUST preserve extension data they do not understand | [S-L07-002] [S-L07-011] |
| `$deprecated` | token or group | `true`, `false`, or a string explaining why; group deprecation is inherited by its children | [S-L07-002] |
| `$root` | inside a group | Reserved token name for a group's base value, for example `{color.accent.$root}` next to `color.accent.light` | [S-L07-002] |
| `$extends` | group | Group inherits another group's tokens (deep merge; local tokens override); MUST NOT point at a token; circular extends are errors. Defined as sugar for JSON Schema `$ref` | [S-L07-002] |
| `$ref` | anywhere | JSON Pointer (RFC 6901). Tools MUST support it. It can reach inside values, e.g. `#/colors/blue/$value/components/0` | [S-L07-002] |
| Names | tokens and groups | MUST NOT start with `$`; MUST NOT contain `{`, `}` or `.` | [S-L07-002] |

Reference syntax [S-L07-002]:
- Curly braces: `"$value": "{color.palette.blue.500}"`. This always targets a whole token and resolves to its `$value`. It cannot reach array items or groups.
- JSON Pointer: `{"$ref": "#/color/palette/blue/500/$value/hex"}`. Use it for property-level references such as a single color channel.
- Chained aliases are allowed. Circular references are errors that affect every token in the chain.

### A3. DTCG 2025.10 `$type` reference table

| `$type` | Kind | `$value` shape (exact) | Constraints | Evidence |
|---|---|---|---|---|
| `color` | simple | `{ "colorSpace": "<space>", "components": [c1, c2, c3], "alpha": 0-1 (optional, default 1), "hex": "#rrggbb" (optional 6-digit fallback) }` | 14 spaces: `srgb`, `srgb-linear`, `hsl`, `hwb`, `lab`, `lch`, `oklab`, `oklch`, `display-p3`, `a98-rgb`, `prophoto-rgb`, `rec2020`, `xyz-d65`, `xyz-d50`. A component may be the string `"none"` (for example a hue that does not apply) | [S-L07-003] |
| `dimension` | simple | `{ "value": <number>, "unit": "px" \| "rem" }` | Only px and rem | [S-L07-002] |
| `fontFamily` | simple | string, or array of strings in fallback order | none | [S-L07-002] |
| `fontWeight` | simple | number from 1 to 1000, or an alias string | Aliases: 100 thin/hairline, 200 extra-light/ultra-light, 300 light, 400 normal/regular/book, 500 medium, 600 semi-bold/demi-bold, 700 bold, 800 extra-bold/ultra-bold, 900 black/heavy, 950 extra-black/ultra-black | [S-L07-002] |
| `duration` | simple | `{ "value": <number>, "unit": "ms" \| "s" }` | Only ms and s | [S-L07-002] |
| `cubicBezier` | simple | `[P1x, P1y, P2x, P2y]` | x values in [0,1]; y values unbounded (this allows overshoot) | [S-L07-002] |
| `number` | simple | JSON number | Used for unitless line height, gradient stop position, opacity | [S-L07-002] |
| `strokeStyle` | composite | a keyword (`solid`, `dashed`, `dotted`, `double`, `groove`, `ridge`, `outset`, `inset`) OR `{ "dashArray": [dimension...], "lineCap": "round" \| "butt" \| "square" }` | Spec notes that Figma lacks inset/outset/double and may fall back to solid | [S-L07-002] |
| `border` | composite | `{ "color", "width" (dimension), "style" (strokeStyle) }` | Each part may be a value or an alias | [S-L07-002] |
| `transition` | composite | `{ "duration", "delay" (both duration), "timingFunction" (cubicBezier) }` | Open issue #103: does not say which property animates or its start and end states | [S-L07-002] |
| `shadow` | composite | one object or an array of objects: `{ "color", "offsetX", "offsetY", "blur", "spread", "inset" (optional boolean) }` | Array elements may be aliases; no array flattening | [S-L07-002] |
| `gradient` | composite | array of stops `{ "color", "position" (number 0-1, clamped) }` | No gradient kind (linear, radial, conic) or angle. Open issue #101 | [S-L07-002] |
| `typography` | composite | `{ "fontFamily", "fontSize" (dimension), "fontWeight", "letterSpacing" (dimension), "lineHeight" (number, multiplier of fontSize) }` | Open issue #102 asks whether lineHeight should be a dimension or a new type. No text-transform, decoration, paragraph spacing or font style | [S-L07-002] |

Listed as likely future types, not normative: font style, percentage/ratio, file (assets) [S-L07-002].

### A4. DTCG Resolver Module 2025.10 (how the spec does theming)

The Format module has no modes. Theming lives in a separate Resolver document [S-L07-002] [S-L07-004].
- Root properties: `name`, `version` (required, MUST be `"2025.10"`), `description`, `sets`, `modifiers`, `resolutionOrder` (required), `$schema`, `$defs` [S-L07-004].
- A **set** is an ordered list of token `sources`: inline tokens and/or `{"$ref": "file.json"}`. When the same token appears more than once, the last one wins [S-L07-004].
- A **modifier** is a named axis (for example `theme`) with a `contexts` map (for example `light`, `dark`, `lightHighContrast`) whose values are lists of sources, plus an optional `default`. A modifier SHOULD have 2 or more contexts, MUST NOT have 0, and MUST NOT reference another modifier [S-L07-004].
- `resolutionOrder`: an array of sets and modifiers. Later entries override earlier ones [S-L07-004].
- The number of possible outputs is the product of all contexts across modifiers. The spec's own example: 3 modifiers with 4, 3 and 2 contexts give 24 permutations [S-L07-004].
- The spec recommends **orthogonal** modifiers, meaning two modifiers should not set the same token. If both `theme` and `brand` set `color.button`, only array order decides the result [S-L07-004].

### A5. What DTCG 2025.10 still lacks (gaps the builder must fill with `$extensions` or its own model)

| Gap | Detail | Evidence |
|---|---|---|
| Springs / physics motion | Only `cubicBezier`, `duration` and `transition`. No spring (stiffness, damping, mass, bounce), keyframe sequence or choreography type. Figma Motion's easing variables can hold springs, so a Figma spring has no DTCG home. DTCG issue #429 (opened 28 Jun 2026, open) is gauging interest in spring and keyframe types; #158 (single Bezier inadequate) is still open | [S-L07-002] [S-L07-013] [S-L07-033] [S-L07-048] |
| Modes inside the Format | Modes and themes need the separate Resolver document. The Format file holds one value per token. Issue #210 "Native modes and theming support" is still open; a `$modes` array proposal (#348) was closed | [S-L07-002] [S-L07-004] [S-L07-048] |
| Conditional values | No media-query, platform or density conditions beyond resolver contexts [inferred from absence in S-L07-002 and S-L07-004] | [S-L07-002] [S-L07-004] |
| String / boolean types | Not DTCG types. Figma accepts `string` on import anyway and encodes booleans as `number` plus `$extensions: {"com.figma.type": "boolean"}` | [S-L07-011] |
| Percentage / ratio, font style, file/asset | Listed only as future candidates | [S-L07-002] |
| Gradient geometry | Stops only; no type or angle | [S-L07-002] |
| Typography completeness | No text case, decoration, paragraph spacing or indent, or font style; lineHeight is unitless only | [S-L07-002] |
| Units | Dimension allows only px and rem (no em, %, vw, pt, dp, sp) | [S-L07-002] |
| Component-state semantics | No standard way to express interaction state or component anatomy; that belongs to naming conventions [inferred] | [S-L07-002] |

---

### A6. Figma capabilities table (verified against help.figma.com and developers.figma.com on 2026-09-23)

Plan names: Starter (free), Professional, Organization, Enterprise. Seats: Full, Dev, Collab, View.

| Feature | What it does | Plan / seat limits | Introduced / status | Evidence |
|---|---|---|---|---|
| Variables: 6 types | color, number, string, boolean, **timing** (ms in the UI; seconds in the plugin API), **easing** (Bezier curve or spring) | Available on any plan | color/number/string/boolean since 2023; timing and easing arrived with Figma Motion (Config 2026, rollout from 24 Jun 2026); plugin API added EASING/TIMING on 5 Aug 2026; REST API still lists only BOOLEAN/FLOAT/STRING/COLOR | [S-L07-013] [S-L07-017] [S-L07-040] [S-L07-034] |
| Collections and groups | Collection = a set of variables plus modes. Groups inside a collection can be nested; slash names (`color/accent/light`) | up to 5,000 variables per collection | 2023; nested groups current | [S-L07-013] [S-L07-018] [S-L07-034] |
| Modes | One value per variable per mode. The left-most column is the default mode. Modes can be set on layers, frames, components, sections, groups and pages; "Auto" inherits from the parent | Starter: no modes listed; **Professional: up to 10 per collection; Organization: up to 20; Enterprise: "unlimited modes with extended collections"**; REST API caps a collection at 40 modes | Limit raised from 4 to 10/20 at Schema 2025 (28 Oct 2025) | [S-L07-011] [S-L07-014] [S-L07-016] [S-L07-038] [S-L07-034] |
| Team default mode | A workspace or team can default to a mode (for example mobile) | Enterprise | current | [S-L07-011] |
| Aliasing | A variable can reference another variable of the same type, including across collections. Alias cycles are rejected | all plans | 2023 | [S-L07-013] [S-L07-034] |
| Composed color | A color variable's color and opacity channels can be aliased separately | all plans | current | [S-L07-013] [S-L07-034] |
| Scoping | Limits which property pickers show a variable. Number: gap/padding, radius, width/height, font size/weight/line height/letter spacing/paragraph spacing/indent, opacity, effects, stroke, text content. Color: frame fill, shape fill, text fill, stroke, effects. String: font family, font style/weight, text, font variations | all plans | current (an older article saying "number only" is stale) | [S-L07-018] [S-L07-034] [S-L07-019] |
| Code syntax | One code name per platform: Web, Android, iOS (at most 3 per variable). Shown in Dev Mode snippets for CSS, SwiftUI and Compose | all plans (Dev Mode needs a paid plan) | current | [S-L07-018] [S-L07-034] |
| Hide from publishing | Keeps primitives out of consumers' pickers while semantic tokens still alias them | publishing needs a paid plan | current | [S-L07-018] [S-L07-025] |
| Native DTCG import/export | Import: drag DTCG JSON into a collection; one mode per file; supports color (sRGB, HSL only), dimension (px only, becomes number), fontFamily (single string), duration (s only), number (becomes boolean if `$extensions.com.figma.type = "boolean"`), and non-DTCG string. Cross-collection aliases via `com.figma.aliasData`. Dots become slashes. Export: per mode or all modes | all plans with modes | Announced at Schema 2025 for November 2025; documented in the modes article (edited 24 Jun 2026) | [S-L07-011] [S-L07-038] |
| Extended collections | Enterprise multi-brand: extend a parent collection per brand, override values, inherit everything else. The extension cannot add variables or modes or change scope/description. Color and opacity count as one override. Chains are allowed (C extends B extends A) | **Enterprise plan**; anyone with can-edit access (no seat type stated) [S-V1a-041] | Announced 28 Oct 2025; article created 14 Nov 2025 | [S-L07-015] [S-L07-016] [S-L07-034] |
| Variable libraries | Publish variables, styles and components to team/org libraries | Education/Pro/Org/Ent | 2023 | [S-L07-013] [S-L07-014] |
| REST API for variables | Read and write variables, modes and extended collections (`file_variables:read/write`) | **Enterprise, Full seat only** | current | [S-L07-034] [S-L07-014] |
| Styles (4 kinds) | Paint/color, text, effect (drop and inner shadow, layer and background blur, texture, noise), layout guide (row, column, grid). Styles hold composites (gradients, images, stacked fills, full type specs); variables can back style fields; styles cannot alias | Create on any plan; publish on paid plans | long-standing | [S-L07-020] [S-L07-019] |
| Typography via variables | Number variables bind to font size, weight, line height, letter spacing (px), paragraph spacing and indent. String variables bind to font family and style. Text styles can be backed by variables, so type can change with mode | all plans | current | [S-L07-013] [S-L07-019] |
| Components and variants | Component sets with variant properties | all plans | long-standing | [S-L07-021] |
| Component properties (5) | boolean (layer visibility only), instance swap (with preferred instances), text (no rich text), variant, **slot** | all plans | slot is the newest | [S-L07-021] |
| Slots | Flexible area inside a component instance: add, resize or reorder content without detaching. Preferred instances, "only allow preferred", min and max layer counts. Cannot be on the top-level layer | "Available in Figma Design on all plans" (Full seat on paid plans per the Schema note) | Announced at Schema 2025 (early access, then open beta); the help article was created 6 Feb 2026 and no longer says beta | [S-L07-016] [S-L07-022] [S-L07-023] [S-L07-038] |
| Variables on variant props | String/number variables drive variant switching by mode. Boolean variables drive true/false variant props. The modes article says boolean variables cannot bind boolean properties on instances | all plans | current | [S-L07-011] |
| Auto layout: grid flow | Third auto layout flow next to horizontal and vertical: tracks, spans, auto rows, fixed/fill tracks; maps to CSS grid in Dev Mode | all plans | Announced at Config 2025 (7 May 2025) | [S-L07-024] [S-L07-044] |
| Library analytics | Adoption and usage of components, styles and variables; daily; 1-year history; styles and variables tracked since 10 Oct 2024 | Organization and Enterprise | current | [S-L07-029] |
| Branching | Branch, review and merge for libraries | Organization and Enterprise, Full seat | long-standing | [S-L07-031] [S-L07-014] |
| Dev Mode | Inspect: variable details (collection, mode, alias chain to raw value, scope, code syntax); suggested variables for raw values | paid plans (Dev or Full seat) | current | [S-L07-030] [S-L07-014] |
| Code Connect (UI and CLI) | UI: inside Figma, GitHub optional (one repo per library file), several framework mappings per component, custom instructions for AI. CLI: templates in the repo, property mappings. Both feed the MCP server | Organization and Enterprise, Full or Dev seat | CLI 2024; UI GA at Schema 2025 | [S-L07-026] [S-L07-016] |
| Figma MCP server | Remote server (preferred) and desktop server. Read tools: `get_design_context` (React + Tailwind by default), `get_metadata`, `get_screenshot`, `download_assets`, `get_variable_defs`, `get_motion_context`, `get_figjam`, `get_libraries`, `search_design_system`, Code Connect tools. Write tools: `use_figma` (creates and edits frames, components, variants, variables, styles), `generate_figma_design`, `create_new_file`, `upload_assets`, `generate_diagram`, plus shader and generative-plugin tools and `weave_*` tools. **`create_design_system_rules` is now an MCP prompt, not a tool.** Several tools are remote-only | Remote: all seats and plans. Desktop: Dev or Full seat on paid plans. Current limits: Starter 20 calls/month; View/Collab seats on paid plans 6/month; Dev/Full seats: Professional 200/day (10/min), Organization 200/day (15/min), Enterprise 600/day (20/min). Some write tools are exempt. Writing to the canvas is free in beta and will become usage-based paid | Guide created 15 May 2025; GA at Schema 2025 (28 Oct 2025) | [S-L07-027] [S-L07-041] [S-L07-016] [S-L07-049] |
| MCP skills | Packaged agent workflows: `/figma-use`, `/figma-generate-design`, `/figma-generate-library` (builds a starter component library with variants) | per MCP access | article created 25 Mar 2026 | [S-L07-043] |
| Check designs (linter) | Finds hard-coded color, type, radius and spacing; assets from the wrong library; detached components; contrast (AA/AAA). Suggests variables ranked by similarity, naming/hierarchy and usage. **No LLM.** One page at a time, 25K-layer cap; cannot swap color styles | Organization and Enterprise | Early access at Schema 2025; article created 8 Apr 2026 | [S-L07-025] [S-L07-016] |
| Figma Make + design systems | Make kits import Figma libraries (components, styles, variables) and generate React components plus a CSS file. Or bring an npm design-system package (public on any plan; private via the org registry on paid plans) with auto-generated guidelines | paid plans, Full seat | Schema 2025; article created 28 Oct 2025 | [S-L07-016] [S-L07-028] |
| Figma agent + design system | The agent uses published libraries as context. Figma advises meaningful names, auto layout, properties and variants, variables, and descriptions. A `_example` suffix or an "Examples" page teaches composition (up to 200 examples) | all plans in beta | agent open beta from 23-24 Jun 2026 | [S-L07-042] [S-L07-017] [S-L07-039] |
| Figma Motion | Timeline, keyframes, presets, animated components, timing and easing variables with modes; Dev Mode timeline; export CSS, JSON or React; `get_motion_context` over MCP | open beta, all plans; publishing animated components needs a paid Full seat | Config 2026; rollout 24 Jun 2026 | [S-L07-017] [S-L07-032] [S-L07-033] [S-L07-039] |

### A7. Figma variables vs DTCG: the translation seams

| DTCG | Figma native import | Loss or caveat | Evidence |
|---|---|---|---|
| `color` (14 color spaces) | color variable | Import accepts only `srgb` and `hsl`. OKLCH, Display P3 and the others are not accepted on import | [S-L07-011] [S-L07-003] |
| `dimension` px | number | `rem` is rejected, so rem-authored tokens must be converted to px first | [S-L07-011] |
| `fontFamily` | string | Single name only; fallback arrays rejected | [S-L07-011] |
| `duration` | number | `s` only on import (the UI shows timing variables in ms) | [S-L07-011] [S-L07-013] |
| `number` | number, or boolean with `com.figma.type` | none | [S-L07-011] |
| (none) | string | Figma accepts a non-standard `"$type": "string"` | [S-L07-011] |
| `fontWeight`, `cubicBezier`, `strokeStyle`, `border`, `transition`, `shadow`, `gradient`, `typography` | not imported as variables | Composites map to Figma **styles** (text, effect) or to several variables. `cubicBezier` has an easing-variable counterpart in Figma Motion, but the import table does not list it | [S-L07-011] [S-L07-020] [S-L07-013] |
| Resolver modifiers and contexts | collections and modes | Figma import creates one mode per imported file. Several resolver modifiers therefore need several collections, or one collection whose modes flatten the combinations | [S-L07-011] [S-L07-004] [inferred] |
| Group path `color.accent.light` | variable name `color/accent/light` | Dots become slashes. When two tokens normalize to the same name, only the first is kept | [S-L07-011] |
| `$extends` group inheritance | extended collection (Enterprise) | Similar idea (inherit and override), but Figma extends a whole collection while DTCG extends a group [inferred] | [S-L07-002] [S-L07-015] |

### A8. Token tiers and naming across major systems (verified 2026-09-23)

| System | Tiers (their words) | Naming grammar | Real examples (value) | Themes / modes | Component tokens public? | Notable rule | Evidence |
|---|---|---|---|---|---|---|---|
| **Material 3** | reference (`ref`) > system (`sys`) > component (`comp`); comp marked "in development" on m3.material.io | dot-separated, general to specific: `md.` + class + role; kebab inside a segment | `md.ref.palette.primary40` = #6750A4; `md.sys.color.primary` = primary40 (light) / primary80 (dark); `md.sys.color.surface` = neutral98 / neutral6; filled button: container color = `sys.color.primary`, height 40px, shape `corner-full`, disabled container opacity 0.12. CSS: `--md-sys-color-primary`, `--md-filled-button-container-color` | light, dark, each with 3 contrast levels (standard, medium, high; added May 2025) | Yes in Material Web (which is "in maintenance mode") | sys is "where theming occurs"; comp should point to sys/ref, not hex | [S-L07-100] [S-L07-102] [S-L07-103] [S-L07-104] |
| **Atlassian** | raw palette behind the tokens; tokens all start with a foundation (no component tier found) | `foundation.property.modifier` (role, emphasis, state), lowercase dots; CSS `--ds-` and the `color`/`elevation` word dropped | `color.background.accent.blue.subtle` = Blue400 #669DF1 / Blue800 #1558BC; `color.text` #292A2E / #CECFD2; `color.background.danger.bold.hovered`; `elevation.surface` → `--ds-surface`; `space.100` = 0.5rem | Docs: light and dark. Package 19.0.0 also ships increased-contrast light/dark and non-color themes (spacing, typography, shape, motion) | No [inferred from names] | "Don't use a token just because the colors appear to match"; 600 tokens (442 color) | [S-L07-105] [S-L07-106] [S-L07-107] [S-L07-108] |
| **GitHub Primer** | base > functional > component/pattern | `prefix-namespace-pattern-variant-property-scale`; camelCase multi-word segments; dashes in CSS, dots in JS; modifiers default/muted/emphasis | `--bgColor-default` #ffffff / #0d1117; `--fgColor-default` #1f2328 / #f0f6fc; `--bgColor-accent-emphasis` #0969da / #1f6feb; `--button-primary-bgColor-rest` = `var(--bgColor-success-emphasis)`; `--base-size-16` = 1rem | 14 theme files: light, dark, dark-dimmed, each also as high-contrast, colorblind (protanopia-deuteranopia) and tritanopia | Yes, "only in component CSS" | "Never use raw values... Only use semantic tokens" | [S-L07-109] [S-L07-110] [S-L07-111] |
| **Salesforce SLDS 2** | design token value > global styling hook > component styling hook > implementation | `--slds-{g\|c}-{category}-{role}-{n}`; numbered sets start at 1 | `--slds-g-color-accent-container-1` #066AFE; `--slds-g-shadow-2` = 0 2px 4px rgba(0,0,0,0.12); `--slds-g-radius-border-2` 0.25rem; `--slds-g-font-scale-3` 1rem; `--slds-c-button-color-background` | Cosmos default theme; custom themes generated from one brand color; dark mode and comfy/compact density since Winter '26 (SLDS 2 GA) | Component hooks are Beta / developer preview, not GA | reference global hooks; never reassign them | [S-L07-116] [S-L07-117] [S-L07-118] [S-L07-119] |
| **IBM Carbon** | palette > role > component | kebab; Sass `$`, CSS `--cds-` | `$background` white / gray10 / gray90 / gray100 (#161616); `$layer-01`; `$text-primary`; `$interactive` blue60 #0f62fe (White, g10) / blue50 (g90, g100); `$button-primary` #0f62fe | 4 themes: White, g10, g90, g100; layering model (base + layer 01-03, contextual tokens) | Yes (button, notification, tag, content-switcher, status) | token names and roles "never change across themes"; only values do | [S-L07-112] [S-L07-113] [S-L07-114] [S-L07-115] |
| **Adobe Spectrum 2** | global > alias > component-specific | flat kebab: context + common unit + clarification | `blue-800` rgb(75,117,255) light / rgb(64,105,253) dark; `corner-radius-75` 2px; `component-height-100` 32px desktop / 40px mobile; `accent-background-color-default` → `accent-color-900`; `checkbox-control-size-small` 14 / 18px | color sets light, dark, wireframe; scale sets desktop, mobile | Yes, but not to be used on other components | "Only use global tokens when there are no available aliases"; S2 data GA in @adobe/spectrum-tokens 13.0.0 (13 Mar 2025); now 15.4.1 | [S-L07-120] [S-L07-121] |
| **Shopify Polaris** | token groups (color, font, text, shadow, space, motion, width, height, border, z-index, breakpoints); no component tier beyond "specialty" tokens | `--p-color-` + element + role + prominence + state (elements bg, bg-surface, bg-fill, text, border, icon) | `--p-color-bg-surface` #fff; `--p-color-text` rgba(48,48,48,1); `--p-color-bg-fill-critical` rgba(199,10,36,1); `--p-space-400` 1rem; `--p-border-radius-200` 0.5rem | light, light-mobile, light-high-contrast-experimental, dark-experimental | No | Polaris React is archived. Polaris Web Components (1 Oct 2025) are styled through props like `tone="critical"` that "can't be overridden with custom CSS" | [S-L07-124] [S-L07-125] [S-L07-126] [S-L07-128] |
| **Figma's own course** | primitive ("what") > semantic ("how") > component-specific ("where") | slash groups, e.g. `surface/brand-contrast` → `pink/400`; component format asset-type/property/state (`button-primary-background-default`) | n/a | example: a Primitives collection (hidden) plus a Tokens collection with light/dark | "might not be necessary for everyone"; "more commonly used by larger, enterprise-level systems" | primitives are reference-only | [S-L07-050] |
| **DTCG Color module (non-normative)** | base > alias > component | groups with dot paths | `color.palette.black` → `color.text.base`; `color.button.primary` → `{color.brand.primary}` | n/a | n/a | descriptive vs numerical (ordered, bounded, computer-generated) base names | [S-L07-003] |

**Patterns across the table** [inferred from the rows above]:
- Every system has a raw layer and a meaning layer. The component layer is the one that varies: public in Material, Primer, Carbon and Spectrum; beta in SLDS 2; absent in Atlassian and Polaris.
- Themes live in the meaning layer in every system. Carbon states it outright: names never change across themes, only values [S-L07-112].
- Contrast has become a mode axis: Material has 3 contrast levels, Primer has high-contrast and color-vision variants, Atlassian has increased contrast, and Polaris has an experimental high-contrast theme [S-L07-104] [S-L07-110] [S-L07-108] [S-L07-126].
- Density or scale is the second most common axis: Spectrum desktop/mobile, SLDS comfy/compact, Polaris light-mobile [S-L07-121] [S-L07-119] [S-L07-126].
- The trend toward closed styling is worth watching. Polaris Web Components remove CSS overrides entirely, and Material Web is in maintenance mode [S-L07-128] [S-L07-103].

### A9. Token pipeline tools (verified 2026-09-23)

| Tool | What it is | Source-of-truth model | DTCG 2025.10 support | Theming / modes | Outputs | Status / pricing note | Evidence |
|---|---|---|---|---|---|---|---|
| **Style Dictionary** | Open-source build system (config, parse, preprocess, transform, resolve refs, format, actions) | JSON/code-first | v4+ auto-detects DTCG. 2025.10 color objects (v5.3.0, 9 Feb 2026) and dimension objects (v5.4.0, 22 Mar 2026) shipped; gradient and duration in progress; **Resolver module not implemented** (issue #1590) | No built-in themes. The official multi-brand example runs one build per brand x platform. `include` = base, `source` = overrides | Transform groups: web, js, scss, css, less, html, android, compose, ios, ios-swift, flutter, react-native. Name transforms: camel, kebab, snake, constant, pascal, human. Formats include css/variables, scss/variables, javascript/es6, typescript, android/resources, compose/object, ios-swift/class.swift, flutter/class.dart | v5.0.0 16 May 2025; latest v5.5.5, 20 Sep 2026; Node 22+ | [S-L07-151] [S-L07-153] [S-L07-155] [S-L07-156] [S-L07-157] [S-L07-158] [S-L07-159] [S-L07-161] [S-L07-162] [S-L07-045] |
| **Tokens Studio** (Figma plugin + Studio platform) | Token authoring in Figma with sets and themes; Git sync; Studio platform adds branching, reviews, releases, CLI and CI/CD | Design-tool-first (the plugin writes to Git) | DTCG format toggle (`$value`/`$type`), no spec version stated. 24 token types including non-DTCG ones (asset, boolean, text, opacity, spacing, sizing, borderRadius, borderWidth; "composition" legacy) | Theme = combination of token sets; multi-dimensional theme groups. On Figma export, **Theme Group becomes a Variable Collection and Theme becomes a Mode** (paid) | via `@tokens-studio/sd-transforms` v2.0.3 (needs Style Dictionary ^5) with `permutateThemes()` | Plugin 2.12.1 (23 Sep 2026); themes are a paid feature ("Starter Plus", formerly Pro); platform plans Variables EUR17/mo, Essential EUR169, Organization EUR499 (annual) | [S-L07-163] [S-L07-165] [S-L07-167] [S-L07-168] [S-L07-171] [S-L07-172] [S-L07-174] [S-L07-175] [S-L07-176] [S-L07-177] [S-L07-045] |
| **Terrazzo** (formerly Cobalt UI) | Open-source DTCG CLI and plugins | JSON/code-first; can import from the Figma REST API (Enterprise) into a `*.resolver.json` | **Full 2025.10 support including resolvers** (CLI 2.0.0, 17 Mar 2026); older-draft files error unless lint is relaxed | Resolvers (sets, modifiers, resolutionOrder). plugin-css "permutations" wrap each context in a selector or media query | css, css-in-js, js, sass, swift (0.3.3, pre-1.0), tailwind, vanilla-extract, token-listing; no Android/Kotlin | CLI latest 2.7.1 (11 Aug 2026) | [S-L07-178] [S-L07-179] [S-L07-180] [S-L07-182] [S-L07-183] [S-L07-217] |
| **Specify** | Former token pipeline SaaS | n/a | n/a | n/a | n/a | **Shut down**: announced 25 Oct 2024, ended 15 Nov 2024 | [S-L07-184] [S-L07-186] |
| **Supernova** | Design-system platform: docs, tokens, pipelines, now "AI context" over MCP | Platform hub fed by Figma variables or Tokens Studio | Listed by W3C as supporting; its own DTCG exporter repo was last pushed in 2022; current docs do not mention DTCG (not verified) | Themes = override sets that resolve "the same way as Figma variable modes" | Exporters: css, css-in-js, jetpack-compose, style-dictionary, tailwind-4, svg-to-react; skills exporter writes SKILL.md | Free / Pro $35 per editor per month / Enterprise; themes 1 (Free) vs unlimited | [S-L07-188] [S-L07-191] [S-L07-192] [S-L07-193] [S-L07-195] [S-L07-006] |
| **zeroheight** | Documentation platform with a token manager | Hub: Git (two-way), Figma variables plugin, Figma styles (read-only), JSON upload | Follows DTCG; **2026 migration to DTCG 2025.10 and Style Dictionary v5**; default export `.tokens.json` | Figma variable collections sync into a token set; renaming a variable breaks the link (mode handling not verified) | CSS, SCSS, iOS, Swift, Android, Compose, Flutter, LESS, JS via Style Dictionary v5; opens a PR per repo | Legacy formats dropped (support to end early Sep 2026) | [S-L07-200] [S-L07-201] [S-L07-202] [S-L07-203] |
| **Knapsack** | Design-system platform with live theming on production components | Hub: imports Figma variables (via plugin), Tokens Studio, Style Dictionary files | Listed by W3C as supporting; own docs do not mention DTCG (not verified) | Collections, groups, modes (first mode = default); types Color, Dimension, Duration, Font Weight, String, Number, Boolean | CI/CD integration | n/a | [S-L07-204] [S-L07-207] [S-L07-208] [S-L07-209] [S-L07-006] |
| **Penpot** (design tool) | Open-source design tool with native tokens | Design-tool-first | Follows DTCG; 2.17.0 adopted `$` keys; exports a single file or multiple files with `$themes.json`/`$metadata.json` | Sets override in order; multi-dimensional themes | JSON | Native tokens since 2.6.0 (9 Apr 2025); latest 2.17.2 | [S-L07-210] [S-L07-216] |
| **Figma native** | Variables with DTCG import/export | Design-tool-first | Imports a subset of DTCG (A7); exports JSON per mode or all modes | Collections x modes; extended collections (Enterprise) | JSON; Dev Mode code syntax (CSS, SwiftUI, Compose) | see A6 | [S-L07-011] [S-L07-015] [S-L07-018] |

**How tokens flow, end to end** [S-L07-011] [S-L07-151] [S-L07-179] [S-L07-203] [inferred synthesis]:
1. **Author** in Figma variables (collections x modes), Tokens Studio (sets + themes) or Penpot, or directly in DTCG JSON in git.
2. **Exchange** as DTCG JSON. Figma exports one file per mode natively. Tokens Studio pushes to Git. The Figma REST API (Enterprise) lets Terrazzo or scripts pull variables.
3. **Resolve themes.** A DTCG resolver (Terrazzo) or one build per theme combination (Style Dictionary; `permutateThemes()` for Tokens Studio files).
4. **Transform** names and values per platform: kebab CSS custom properties, camel/pascal Swift and Kotlin members, Android XML resources, Flutter classes; color space conversion and px-to-rem.
5. **Consume** in components (CSS variables, SwiftUI Color extensions, Compose theme objects), and write names back into Figma code syntax (DC-L07-20).

Version note: L00 reported "Terrazzo plugins 2.5.0 (26 Jul 2026)" [S-L07-045]; the pipelines helper found `@terrazzo/cli` 2.7.1 (11 Aug 2026) [S-L07-178]. These are probably different packages; either way Terrazzo is on 2.x.

---

## Part B. Decision Cards

### DC-L07-01: How many token tiers
- **Block path:** Tokens > Architecture > Tiers
- **Questions the designer answers:** Do we need only raw values, or raw values plus meaning? Do components get their own tokens? Can product teams use raw values directly?
- **Options:**
  1. *One tier (flat values)*: a palette and scales used directly. Fast to start; theming means find-and-replace [inferred].
  2. *Two tiers: primitive to semantic*: the DTCG Color module calls these "base" and "alias" tokens [S-L07-003]. Examples: Atlassian (raw palette behind foundation tokens; no component tier) [S-L07-107] [S-L07-108]; Polaris (token groups plus a few "specialty" tokens) [S-L07-125].
  3. *Three tiers: primitive, semantic, component*: DTCG's third category, "component" tokens, "improve the separation of concerns" [S-L07-003]. Examples: Material 3 ref/sys/comp [S-L07-100]; Primer base/functional/component [S-L07-109]; Carbon palette/role/component [S-L07-112]; Spectrum global/alias/component [S-L07-120]; SLDS 2 token value/global hook/component hook [S-L07-116]; Figma's own course primitive/semantic/component [S-L07-050]; Brad Frost Tier 1/2/3 [S-L07-132].
  4. *Four or more tiers*: adds a brand or theme layer between primitive and semantic, or domain namespaces (EightShapes' "domain") [S-L07-036].
- **Visual effect:** No direct visual effect. More tiers make restyling cheaper (change one alias, not 40 usages), at the cost of indirection [S-L07-019] [inferred].
- **Depends on (upstream):** number of themes and brands (DC-L07-15, DC-L07-16); team size.
- **Affects (downstream):** naming (DC-L07-04), Figma collection structure (DC-L07-18), pipeline complexity (DC-L07-25).
- **Token encoding:** primitive `color.blue.600` -> semantic `color.bg.accent` (`"{color.blue.600}"`) -> component `button.primary.bg` (`"{color.bg.accent}"`) [shape from S-L07-003].
- **Platform notes:** Figma: primitives in a hidden collection, semantics in a moded collection [S-L07-018] [S-L07-025]. Code: primitives are often not exported to consumers at all [inferred].
- **Accessibility constraints:** Contrast is guaranteed at the semantic tier (paired fg/bg roles), not the primitive tier [inferred; see L01].
- **Default + heuristic:** **Default: two tiers (primitive plus semantic), with component tokens added per component only when needed (DC-L07-02).** Rule: add a tier only when a real theming or brand need forces it. Figma's course agrees that structures "should always begin with a foundation of primitive tokens" and that the rest depends on the organization [S-L07-050].
- **Evidence:** [S-L07-003] [S-L07-018] [S-L07-019] [S-L07-025] [S-L07-036] [S-L07-050] [S-L07-100] [S-L07-107] [S-L07-108] [S-L07-109] [S-L07-112] [S-L07-116] [S-L07-120] [S-L07-125] [S-L07-132]

### DC-L07-02: When a component token tier is worth it
- **Block path:** Tokens > Architecture > Component tokens
- **Questions the designer answers:** Do components get their own tokens (button.primary.bg) or read semantic tokens directly? Are component tokens public API that product teams can override? Who owns them?
- **Options:**
  1. *No component tier*: components reference semantic tokens directly. Atlassian (every token starts with a foundation) [S-L07-108] and Polaris (no component tier beyond specialty tokens) [S-L07-125].
  2. *Component tokens for every component*: a full public "hook" surface for theming each component. Material 3 comp tokens (for example the filled button's container color, height 40px, corner-full shape, disabled opacity 0.12) [S-L07-102]; Carbon (`$button-primary`, `$notification-background-error`) [S-L07-114]; Primer (`--button-primary-bgColor-rest`, "only in component CSS") [S-L07-109] [S-L07-111]; Spectrum (`checkbox-control-size-small`, not to be used on other components) [S-L07-120]; SLDS 2 component hooks (`--slds-c-button-color-background`), still Beta / developer preview [S-L07-117]. Figma's course: component tokens are "more commonly used by larger, enterprise-level systems" and "might not be necessary for everyone" [S-L07-050]. Brad Frost defines Tier 3 but gives no criteria for when it pays off [S-L07-132].
  3. *Local first, promote later*: EightShapes' rule is to record component-specific decisions locally (in the component's spec or stylesheet) and promote them to a shared group token once 3 or more components need them ("Start within, then promote"; "Don't globalize decisions prematurely") [S-L07-036].
- **Visual effect:** Component tokens let one component be re-skinned (for example, a pill-shaped button in one brand) without touching global radius [inferred].
- **Depends on (upstream):** DC-L07-01; whether themes or brands need per-component overrides (DC-L07-16).
- **Affects (downstream):** token count (component tiers can reach thousands of tokens) [inferred]; Figma variable count per collection (5,000 cap) [S-L07-013]; maintenance cost.
- **Token encoding:** `button.primary.container.color = {color.bg.accent}` [shape from S-L07-003]. In Figma, component tokens can be a third collection aliasing semantic variables [inferred].
- **Platform notes:** On web, component tokens map neatly to CSS custom properties scoped to a component (styling hooks); on native, to component style structs [inferred].
- **Accessibility constraints:** component overrides must not break the contrast of paired semantic roles; restrict overrides to pairs [inferred].
- **Default + heuristic:** **Default: no component tier at launch; add component tokens only for (a) components a brand must restyle independently, or (b) values reused by 3+ related components (then as a group token like `forms.border.color`).** [S-L07-036] [inferred]
- **Evidence:** [S-L07-003] [S-L07-013] [S-L07-036] [S-L07-050] [S-L07-102] [S-L07-108] [S-L07-109] [S-L07-111] [S-L07-114] [S-L07-117] [S-L07-120] [S-L07-125] [S-L07-132]

### DC-L07-03: Primitive (base) naming: descriptive vs numeric scales
- **Block path:** Tokens > Naming > Primitives
- **Questions the designer answers:** Are palette colors named by hue and step (blue-600) or by evocative names (grass, watermelon)? Which numeric scale: 50-950, 0-100, 1-12? Are spacing steps multiples (space-2x) or t-shirt sizes?
- **Options:**
  1. *Descriptive* (`color.grass`, `brand.watermelon`): human-friendly, but the scale position is unclear and names may not translate across languages [S-L07-003].
  2. *Numeric, ordered* (Material-style 50, 100 ... 900) [S-L07-036] [S-L07-003].
  3. *Numeric, bounded* (lightness 0-100, so the number encodes lightness: `neutral-42` = L 42) [S-L07-036] [S-L07-003].
  4. *Computer-generated scales* (tool-generated steps) [S-L07-003].
  5. Spacing and size: *proportion* (`space-1-x` = 16px, `2-x`, `half-x`) vs *t-shirt* (s, m, l, xl). EightShapes: "Size ≠ space"; prefer proportion over t-shirts for space [S-L07-036].
  - Real scales: Material tonal steps 0-100 (`md.ref.palette.primary40`) [S-L07-102]; Primer `--base-size-4/16` (named by pixel value) [S-L07-111]; Atlassian palette `Blue400`/`Blue800` and space `space.100` = 0.5rem (8px on a 100-based scale) [S-L07-108]; Polaris `--p-space-400` = 1rem and `--p-border-radius-200` [S-L07-126]; Spectrum `corner-radius-75`, `component-height-100` [S-L07-121]; Carbon `blue-60`, `gray-10` [S-L07-112]; SLDS 2 numbered sets starting at 1 (`--slds-g-shadow-2`) [S-L07-116].
- **Visual effect:** none directly; bounded numeric names let designers predict contrast from the number (for example, large steps apart = high contrast) [inferred; see L01].
- **Depends on (upstream):** L01 ramp construction (step count), L03 spacing base unit.
- **Affects (downstream):** semantic aliases (readability of `{color.blue.600}`), Figma primitive collection layout.
- **Token encoding:** `color.blue.600` (`$type: color`), `space.200` or `space.2x` (`$type: dimension`) [shape from S-L07-003].
- **Platform notes:** Names that start with a digit are invalid identifiers in Swift, Kotlin and JS, so the name transform must prefix them (for example `blue600`, `space2x`) [inferred].
- **Accessibility constraints:** a bounded lightness scale makes it easy to write rules like "text steps at least N apart from background" [inferred].
- **Default + heuristic:** **Default: hue + numeric step for color (50-950 or 0-100 bounded), proportion or 100-based numeric for space, t-shirt only for component sizes (sm/md/lg).** Descriptive names only for brand colors.
- **Evidence:** [S-L07-003] [S-L07-036] [S-L07-102] [S-L07-108] [S-L07-111] [S-L07-112] [S-L07-116] [S-L07-121] [S-L07-126]

### DC-L07-04: Semantic naming grammar (which levels, in what order)
- **Block path:** Tokens > Naming > Semantic grammar
- **Questions the designer answers:** Which parts make up a token name? In what order? How long may names get?
- **Options (EightShapes levels)** [S-L07-036]:
  - *Namespace*: system (`esds`), theme (`ocean`), domain (`consumer`).
  - *Object*: component group (`forms`), component (`input`), element (`left-icon`).
  - *Base*: category (`color`, `font`, `space`, `size`, `elevation`, `breakpoint`, `shadow`, `touch`, `time`), concept (`feedback`, `action`, `visualization`, `heading`, `body`), property (`text`, `background`, `border`, `fill`, `size`, `weight`, `line-height`).
  - *Modifiers*: variant (`primary`, `secondary`, `success`, `error`), state (`hover`, `press`, `focus`, `disabled`, `visited`), scale (`1`, `100`, `s`/`m`/`l`), mode (`on-dark`, `on-light`).
  - Orders seen in practice: namespaces first, base in the middle, modifiers last, mode usually last; the order inside base varies: `color-background-interactive` (category + property paired) vs `interactive-background-color` (readability) vs `color-interactive-background` (strict hierarchy) [S-L07-036].
  - Real grammars: Atlassian `foundation.property.modifier` (`color.background.danger.bold.hovered`) [S-L07-105]; Primer `namespace-pattern-variant-property-scale` with camelCase segments (`--bgColor-accent-emphasis`) [S-L07-109]; Polaris element + role + prominence + state (`--p-color-bg-fill-critical`) [S-L07-125]; Material `md.sys.color.on-primary` (role words) [S-L07-100]; Spectrum context + unit + clarification (`accent-background-color-default`) [S-L07-120]; SLDS 2 `category-role-n` (`--slds-g-color-accent-container-1`) [S-L07-116]; Carbon role words (`$text-primary`, `$layer-01`) [S-L07-112].
- **Visual effect:** none directly; predictable names cut wrong-token usage. Check designs also ranks suggestions by "variable naming and hierarchy" [S-L07-025].
- **Depends on (upstream):** DC-L07-01 (tiers), L01 color roles, L08 component inventory.
- **Affects (downstream):** Figma group structure (slash paths), CSS custom property names, scoping (a `text` property maps to a TEXT_FILL scope) [S-L07-018] [S-L07-034].
- **Token encoding:** `color.feedback.background.error`, `font.heading.size.1`, `color.action.text.secondary.focus` [examples from S-L07-036].
- **Platform notes:** DTCG group paths use `.`; Figma uses `/`; CSS uses `-`. Keep each segment a single word or a kebab word so transforms are lossless [S-L07-002] [S-L07-011] [inferred].
- **Accessibility constraints:** put the property (text vs background vs border) in the name so fg/bg pairs can be checked automatically [inferred].
- **Default + heuristic:** **Default grammar: `[namespace].category.property.concept?.variant?.state?` for semantics (for example `ds.color.bg.accent.hover`, `ds.color.text.danger`), and `[namespace].component.element?.property.variant?.state?` for component tokens.** EightShapes: include only the levels needed to distinguish intent; avoid redundant defaults such as `-default-on-light` everywhere [S-L07-036]. Avoid homonyms like `type` and `text` as categories [S-L07-036].
- **Evidence:** [S-L07-002] [S-L07-011] [S-L07-018] [S-L07-025] [S-L07-034] [S-L07-036] [S-L07-100] [S-L07-105] [S-L07-109] [S-L07-112] [S-L07-116] [S-L07-120] [S-L07-125]

### DC-L07-05: Namespace / prefix
- **Block path:** Tokens > Naming > Namespace
- **Questions the designer answers:** Do tokens carry a system prefix? Short name or acronym? Does a theme or brand appear in the name?
- **Options:** no prefix (small single-product teams); system name of 5 characters or fewer (`orbit-`) or an acronym (`slds-`, `mds-`); theme prefix (`aads-ocean-`); domain prefix (`esds-consumer-`) [S-L07-036]. Real prefixes: `--md-` (Material) [S-L07-103], `--ds-` (Atlassian) [S-L07-108], `--slds-g-`/`--slds-c-` (Salesforce) [S-L07-116], `--cds-` (Carbon) [S-L07-115], `--p-` (Polaris) [S-L07-126]. Primer uses no system prefix on functional tokens (`--bgColor-default`) [S-L07-111].
- **Visual effect:** none.
- **Depends on (upstream):** product name; whether tokens ship to third parties (plugins, embeds).
- **Affects (downstream):** CSS custom property collisions; code syntax (DC-L07-20).
- **Token encoding:** usually added at transform time (`--ds-color-bg-surface`) rather than stored in every JSON path [inferred].
- **Platform notes:** On native platforms the namespace is often a type or module (`DSColor.bgSurface`) rather than a string prefix [inferred].
- **Accessibility constraints:** none.
- **Default + heuristic:** **Default: a 2-4 letter prefix added only in platform output; theme and brand never in the name (they are modes, not names).** EightShapes: "Theme ≠ Mode", and a theme is orthogonal to color mode [S-L07-036].
- **Evidence:** [S-L07-036] [S-L07-103] [S-L07-108] [S-L07-111] [S-L07-115] [S-L07-116] [S-L07-126]

### DC-L07-06: Casing, separators and platform name transforms
- **Block path:** Tokens > Naming > Casing
- **Questions the designer answers:** How is the same token spelled in JSON, Figma, CSS, Swift, Kotlin and Android XML?
- **Options:** JSON/DTCG: nested groups (path segments, no dots inside names) [S-L07-002]. Figma: slash groups (`color/bg/surface`); import converts dots to slashes [S-L07-011]. Style Dictionary name transforms: kebab (CSS), camel (JS/Swift members), pascal (types), snake, constant (`COLOR_BG_SURFACE`), human [S-L07-158]. Figma code syntax: one name each for Web, Android, iOS [S-L07-018].
- **Visual effect:** none.
- **Depends on (upstream):** DC-L07-04.
- **Affects (downstream):** every platform output; code syntax; Code Connect and MCP output.
- **Token encoding:** DTCG `{"color":{"bg":{"surface":{...}}}}` becomes CSS `--ds-color-bg-surface`, Swift `Color.dsColorBgSurface` or `DS.Color.bgSurface`, Compose `DsTheme.colors.bgSurface`, Android XML `ds_color_bg_surface` [inferred examples using S-L07-158 transforms].
- **Platform notes:** The DTCG resolver says modifier inputs (for example `theme: dark`) SHOULD be case-insensitive [S-L07-004]. The Format module sets no casing rule for token names, so keep segments lowercase to avoid case-collision bugs across transforms [inferred].
- **Accessibility constraints:** none.
- **Default + heuristic:** **Default: lowercase, single-word or kebab segments in JSON; let the pipeline apply kebab (CSS), camel (JS/Swift/Kotlin), snake (Android XML); generate Figma code syntax from the same transforms** [S-L07-158] [S-L07-018].
- **Evidence:** [S-L07-002] [S-L07-004] [S-L07-011] [S-L07-018] [S-L07-158]

### DC-L07-07: Which properties become tokens (token coverage)
- **Block path:** Tokens > Scope > Coverage
- **Questions the designer answers:** Which visual properties are tokenized: color, type, space, size, radius, border width, shadow, opacity, z-index, breakpoints, motion, icon size? Which stay hard-coded?
- **Options:** Minimal (color + type + space); standard (+ radius, border width, shadow/elevation, opacity, motion); extended (+ z-index/layering, breakpoints, icon sizes, touch targets, data-viz palettes). EightShapes' category list: color, font, space, size, elevation, breakpoints, shadow, touch, time [S-L07-036]. DTCG types available for each: color, dimension, fontFamily, fontWeight, duration, cubicBezier, number, and composites [S-L07-002]. Figma variables can bind color, radius, dimensions, gap and padding, font properties, layout guides, opacity, effects, stroke weight, text, visibility, motion timing and easing [S-L07-013].
  - Real coverage: Atlassian's 600 tokens are 442 color, 76 motion, 23 font, 23 space, 21 elevation [S-L07-108]; Polaris groups color, font, text, shadow, space, motion, width, height, border, z-index, breakpoints [S-L07-126]; SLDS 2 global hook categories color, shadows, borders and radius, typography, spacing, sizing [S-L07-116].
- **Visual effect:** the more properties are tokenized, the more consistent (and more easily themeable) the UI becomes; under-tokenized radius and shadow are common sources of visual drift [inferred].
- **Depends on (upstream):** L01-L05 foundations.
- **Affects (downstream):** Check designs can only flag hard-coded color, type, radius and spacing, so those four are the minimum lintable set [S-L07-025].
- **Token encoding:** one DTCG group per category (`color`, `font`, `space`, `size`, `radius`, `border`, `shadow`, `opacity`, `motion`, `z`, `breakpoint`) [inferred].
- **Platform notes:** z-index and breakpoints are web-centric; native platforms use elevation and size classes instead [inferred; see L10].
- **Accessibility constraints:** tokenize focus-ring color and width and minimum touch target size, so they cannot be dropped per component [inferred].
- **Default + heuristic:** **Default: tokenize every property that Figma variables can bind and Check designs can lint, plus motion and focus.** Leave one-off illustration values untokenized.
- **Evidence:** [S-L07-002] [S-L07-013] [S-L07-025] [S-L07-036] [S-L07-108] [S-L07-116] [S-L07-126]


### DC-L07-08: Source of truth (Figma, JSON repo, or code)
- **Block path:** Tokens > Architecture > Source of truth
- **Questions the designer answers:** Where do token values get edited first? Who is allowed to change them? Does code or the design tool follow the other?
- **Options:**
  1. *Figma-first*: variables are authored in Figma, exported as DTCG JSON (natively per mode, or through the Enterprise REST API or a plugin), then transformed to code. Figma supports native DTCG import and export [S-L07-011]. REST read/write needs Enterprise [S-L07-034].
  2. *JSON-first (tokens repo)*: DTCG `.tokens.json` files plus a `.resolver.json` in git are the master copy. Transformers generate platform code, and Figma is updated by import or a sync plugin [S-L07-002] [S-L07-004] [S-L07-011].
  3. *Code-first*: tokens live in CSS, TypeScript or Swift. Figma is updated through the MCP server's `use_figma` write tool ("create a color variable collection from my design tokens") or by generating JSON [S-L07-027].
  4. *Platform-first*: a SaaS token manager is the hub (see the A9 tool table).
- **Visual effect:** None directly. The choice decides drift: whichever side is not the source of truth drifts unless sync runs automatically [inferred].
- **Depends on (upstream):** team skills, Figma plan (the REST API is Enterprise-only), number of platforms.
- **Affects (downstream):** every pipeline decision (DC-L07-25), review workflow (branching or PRs), deprecation (DC-L07-23).
- **Token encoding:** a DTCG 2025.10 file set plus a resolver is the neutral interchange format whichever side leads [S-L07-002] [S-L07-004].
- **Platform notes:** Figma import is lossy (sRGB/HSL only, px only, no composites; see A7) [S-L07-011]. A JSON-first repo keeps OKLCH/P3 values that Figma drops [S-L07-003] [S-L07-011].
- **Accessibility constraints:** Contrast checks must run on the resolved values of every mode, wherever they are authored [inferred].
- **Community signal:** In September 2026 the majority practitioner view on r/DesignSystems and r/UXDesign is that "code is the source of truth" and Figma mirrors it (Tier C, reconciled via L00) [S-L07-045].
- **Default + heuristic:** **Default: JSON-first (DTCG in git) with Figma as a synced, published view.** Heuristic: go Figma-first only if designers own tokens and you have a single web platform. Go JSON-first as soon as two or more code platforms exist, or you need color spaces or composites that Figma cannot hold [inferred from S-L07-011 and S-L07-002].
- **Evidence:** [S-L07-002] [S-L07-004] [S-L07-011] [S-L07-027] [S-L07-034] [S-L07-045]

### DC-L07-09: Interchange format and file layout
- **Block path:** Tokens > Architecture > File format
- **Questions the designer answers:** Which JSON dialect do tokens use? One file or many? How are themes expressed?
- **Options:**
  1. *DTCG 2025.10 Format + Resolver* (stable since 28 Oct 2025) [S-L07-002] [S-L07-004] [S-L07-006].
  2. *Pre-2025 DTCG drafts* (for example, colors as hex strings). Still common in older tools; the 2025.10 color is an object [S-L07-003].
  3. *Tool-flavoured JSON*: Tokens Studio's format has 24 types including non-DTCG ones (boolean, text, opacity, spacing, sizing, borderRadius, borderWidth, asset) and a DTCG toggle that does not state a spec version [S-L07-168] [S-L07-177]. Pre-DTCG Style Dictionary files used `value`/`type` without `$` [inferred]. Terrazzo 2.x now errors on older-draft files unless lint is relaxed [S-L07-179].
- **Visual effect:** none.
- **Depends on (upstream):** DC-L07-08.
- **Affects (downstream):** tool compatibility; what Figma can import (DTCG only) [S-L07-011].
- **Token encoding:** Split by tier and by mode axis: `primitives.tokens.json`, `semantic.light.tokens.json`, `semantic.dark.tokens.json`, then `project.resolver.json` with `sets` (primitives) and `modifiers` (theme: light/dark) [S-L07-004]. Figma import expects **one file per mode** containing the same token names and types [S-L07-011].
- **Platform notes:** Names must avoid `.`, `{` and `}` (DTCG). Figma REST enforces the same forbidden characters [S-L07-002] [S-L07-034].
- **Accessibility constraints:** none.
- **Default + heuristic:** **Default: DTCG 2025.10, one file per tier-and-mode, plus one resolver.** It maps 1:1 onto Figma's one-file-per-mode import and onto resolver contexts [S-L07-004] [S-L07-011].
- **Evidence:** [S-L07-002] [S-L07-003] [S-L07-004] [S-L07-006] [S-L07-011] [S-L07-034]

### DC-L07-10: Color value encoding (color space, hex fallback)
- **Block path:** Tokens > Types > Color
- **Questions the designer answers:** Which color space are primitives authored in? Do we support wide-gamut (P3)? Do we keep a hex fallback?
- **Options:** `srgb` (plus `hex`); `oklch` (perceptual, good for generating ramps); `display-p3` (wide gamut); `hsl`. DTCG 2025.10 supports 14 spaces and an optional 6-digit `hex` fallback [S-L07-003].
- **Visual effect:** P3 allows more saturated brand colors on capable screens. OKLCH gives even lightness steps across hues (see L01) [inferred; see L01].
- **Depends on (upstream):** L01 color decisions; the source-of-truth choice (Figma import accepts only sRGB and HSL) [S-L07-011].
- **Affects (downstream):** every color token and every platform transform. Gamut mapping becomes the translation tool's job, and the spec leaves the algorithm open [S-L07-003].
- **Token encoding:** `{"$type":"color","$value":{"colorSpace":"oklch","components":[0.62,0.19,259],"hex":"#3b6fe0"}}` [inferred values; shape from S-L07-003].
- **Platform notes:** Figma variables import sRGB/HSL only [S-L07-011]. An OKLCH master needs an sRGB (plus hex) export for Figma [inferred].
- **Accessibility constraints:** Compute contrast on the rendered (gamut-mapped) sRGB value, not on the P3 original [inferred].
- **Default + heuristic:** **Default: author primitives in OKLCH or sRGB, and always include `hex`.** Emit sRGB to Figma. Add P3 only if the brand needs vivid colors and the pipeline can gamut-map [inferred].
- **Evidence:** [S-L07-003] [S-L07-011]

### DC-L07-11: Dimension units (px vs rem) and unitless numbers
- **Block path:** Tokens > Types > Dimension
- **Questions the designer answers:** Are spacing and type sizes stored in px or rem? Are line heights unitless?
- **Options:** px (DTCG allows it; the only unit Figma imports) or rem (DTCG allows it; better for browser zoom on web) [S-L07-002] [S-L07-011]. Line height: unitless `number` (the DTCG typography composite requires a number multiplier) [S-L07-002].
- **Visual effect:** none by itself. rem makes web type and spacing scale with the user's browser font size [inferred].
- **Depends on (upstream):** L02 and L03 scales.
- **Affects (downstream):** web CSS output, Figma variables (numbers without a unit), iOS pt and Android dp/sp transforms [inferred].
- **Token encoding:** `{"$type":"dimension","$value":{"value":16,"unit":"px"}}`. Transform to `1rem` for web and `16` for Figma [inferred].
- **Platform notes:** Figma letter spacing via variables is interpreted as px, not % [S-L07-013]. DTCG has no %, em, dp, sp or pt [S-L07-002].
- **Accessibility constraints:** WCAG 1.4.4 Resize Text favors rem/em on web (see L02/L03) [inferred].
- **Default + heuristic:** **Default: store px in source; convert to rem at the web transform step.** This keeps Figma import lossless [S-L07-011] [inferred].
- **Evidence:** [S-L07-002] [S-L07-011] [S-L07-013]

### DC-L07-12: Typography tokens: composite vs atomic, and styles vs variables in Figma
- **Block path:** Tokens > Types > Typography
- **Questions the designer answers:** Is a text style one composite token or five atomic tokens? In Figma, text styles, variables, or both? Should type change by mode (for example mobile vs desktop sizes)?
- **Options:**
  1. *DTCG `typography` composite* (fontFamily, fontSize, fontWeight, letterSpacing, lineHeight) [S-L07-002].
  2. *Atomic tokens* (`font.size.300`, `font.lineHeight.300`, ...) composed at the component or style level.
  3. *Figma*: text styles hold the composite. Number and string variables back the individual fields so a style can change with mode [S-L07-019] [S-L07-013].
- **Visual effect:** Mode-driven type lets one design switch between compact mobile and larger desktop hierarchy [S-L07-019].
- **Depends on (upstream):** L02 type scale.
- **Affects (downstream):** every text component, and Dev Mode snippets.
- **Token encoding:** primitives `font.size.400 = 16px`; semantic `typography.body.md = {fontFamily:"{font.family.sans}", fontSize:"{font.size.400}", fontWeight:"{font.weight.regular}", letterSpacing:{value:0,unit:"px"}, lineHeight:1.5}` [shape from S-L07-002; values inferred].
- **Platform notes:** Figma cannot import the typography composite as variables [S-L07-011]. String variables must spell the font family and style exactly (Figma tolerates case, hyphen and space differences) [S-L07-013].
- **Accessibility constraints:** line height and letter spacing must allow WCAG 1.4.12 text-spacing overrides (see L02) [inferred].
- **Default + heuristic:** **Default: atomic primitives, plus semantic typography composites in JSON, plus Figma text styles whose fields are bound to variables.** You get mode-switchable type in Figma and one composite for code [S-L07-013] [S-L07-019].
- **Evidence:** [S-L07-002] [S-L07-011] [S-L07-013] [S-L07-019]

### DC-L07-13: Shadow, border and elevation tokens (composites vs Figma effect styles)
- **Block path:** Tokens > Types > Shadow / Border
- **Questions the designer answers:** Is elevation a set of shadow composites? Do dark-mode shadows differ? Are borders one composite token or separate width and color tokens?
- **Options:** DTCG `shadow` (single or layered array, optional `inset`), `border` (color, width, style) [S-L07-002]. In Figma: effect styles for shadows (variables can bind color, X, Y, blur and spread); stroke color and weight variables for borders [S-L07-020] [S-L07-013].
- **Visual effect:** Layered shadows (for example a key light plus an ambient light) read as softer, more realistic depth than one hard shadow (see L04) [inferred].
- **Depends on (upstream):** L04 elevation model.
- **Affects (downstream):** cards, menus, dialogs, focus rings.
- **Token encoding:** `elevation.2 = [{color:"{color.shadow.key}",offsetX:0,offsetY:1px,blur:2px,spread:0},{...ambient}]` [shape from S-L07-002].
- **Platform notes:** Figma has no inset, outset or double stroke styles [S-L07-002]. Android elevation and iOS shadows need custom transforms [inferred].
- **Accessibility constraints:** do not rely on shadow alone to show a boundary; keep a 3:1 non-text contrast border where it carries meaning (WCAG 1.4.11; see L01/L04) [inferred].
- **Default + heuristic:** **Default: shadow composites in JSON; Figma effect styles whose color and offset fields are bound to variables, so dark mode can swap the shadow color** [S-L07-013] [S-L07-020].
- **Evidence:** [S-L07-002] [S-L07-013] [S-L07-020]

### DC-L07-14: Motion tokens (duration, easing, springs)
- **Block path:** Tokens > Types > Motion
- **Questions the designer answers:** Which durations and easing curves are tokens? Do we use springs? Where do springs live, given DTCG has no spring type?
- **Options:**
  1. DTCG `duration`, `cubicBezier`, `transition` composite [S-L07-002].
  2. Figma timing variables (ms) and easing variables (Bezier or spring), with modes, used by Figma Motion presets and keyframes [S-L07-013] [S-L07-033]. Spring presets: Gentle, Quick, Bouncy, Slow; custom springs are set with a "Bounce" field [S-L07-033].
  3. Springs stored in `$extensions` (vendor data) or a custom `$type` [inferred; DTCG gap per S-L07-002].
- **Visual effect:** Springs feel physical and interruptible; Beziers feel designed and predictable (see L04) [inferred].
- **Depends on (upstream):** L04 motion principles.
- **Affects (downstream):** transitions in every interactive component; Dev Mode code export (CSS, JSON, React) [S-L07-017].
- **Token encoding:** `motion.duration.short = {value:150,unit:"ms"}`, `motion.easing.standard = [0.2,0,0,1]`, `motion.transition.enter = {duration:"{motion.duration.short}",delay:{value:0,unit:"ms"},timingFunction:"{motion.easing.standard}"}` [shape from S-L07-002; values inferred]. Spring: `$extensions: {"com.example.spring": {...}}` [inferred].
- **Platform notes:** The Figma plugin API stores timing in seconds (UI shows ms) [S-L07-040] [S-L07-013]. The REST API does not yet list TIMING/EASING [S-L07-034]. Figma import accepts `duration` in `s` only [S-L07-011].
- **Accessibility constraints:** honor reduced-motion preferences; a `reduced` mode on the motion collection is one way to do it [inferred; see L04].
- **Default + heuristic:** **Default: 3-5 duration tokens and 3-4 easing tokens in DTCG; springs as extensions until DTCG adds a type; mirror them as Figma timing and easing variables with a "reduced motion" mode** [S-L07-013] [S-L07-033] [inferred].
- **Evidence:** [S-L07-002] [S-L07-011] [S-L07-013] [S-L07-017] [S-L07-033] [S-L07-034] [S-L07-040]

### DC-L07-15: Theming axes (which modes exist and where they live)
- **Block path:** Tokens > Theming > Modes
- **Questions the designer answers:** Which contexts must the system support: light/dark, high contrast, density, brand, breakpoint, reduced motion, locale? Which tier holds the mode-dependent values?
- **Options:**
  - Color scheme: light/dark (almost universal) (Material light/dark [S-L07-102]; Atlassian light/dark [S-L07-107]; Carbon expresses it as 4 themes: White, g10, g90, g100 [S-L07-112]; Spectrum light, dark, wireframe [S-L07-121]; SLDS 2 dark mode since Winter '26 [S-L07-119]).
  - Contrast: standard/high contrast (Material standard/medium/high contrast for both schemes [S-L07-104]; Primer high-contrast plus protanopia-deuteranopia and tritanopia variants of light, dark and dark-dimmed, 14 theme files in all [S-L07-110]; Atlassian increased-contrast light and dark in @atlaskit/tokens 19.0.0 [S-L07-108]; Polaris light-high-contrast-experimental [S-L07-126]).
  - Density or scale: compact/comfortable, or desktop/mobile sizing (Spectrum desktop/mobile scale sets, for example `component-height-100` = 32px desktop / 40px mobile [S-L07-121]; SLDS 2 comfy/compact [S-L07-119]; Polaris light-mobile [S-L07-126]).
  - Brand (multi-brand, see DC-L07-16)
  - Breakpoint (DC-L07-28), motion (reduced), locale strings (Figma string variables for copy) [S-L07-011]
- **Visual effect:** Dark mode flips surfaces and lowers saturation (see L01). High contrast strengthens borders and text. Compact density tightens padding and control height (see L03) [inferred].
- **Depends on (upstream):** L01 color roles; L03 density model.
- **Affects (downstream):** the number of Figma modes and collections (DC-L07-18); the resolver `modifiers` (A4); build outputs (one CSS scope per context).
- **Token encoding:** Modes live on the **semantic tier**. Carbon: token names and roles "never change across themes", only values do [S-L07-112]. Material: sys is "where theming occurs" [S-L07-100]. Primitives stay single-valued; semantic tokens re-point per mode (`color.bg.surface` = `{color.neutral.0}` in light and `{color.neutral.900}` in dark) [S-L07-004 example of theme modifier; values inferred]. DTCG: one resolver modifier per axis [S-L07-004]. Figma: one collection per axis [S-L07-011].
- **Platform notes:** Web: `[data-theme=dark]` scopes or `prefers-color-scheme`; iOS/Android: dynamic colors / resource qualifiers [inferred; see L10].
- **Accessibility constraints:** every mode must independently pass contrast (WCAG 1.4.3 / 1.4.11); a high-contrast mode is the accessible answer to OS "increase contrast" settings [inferred; see L01].
- **Default + heuristic:** **Default: color scheme (light, dark) + contrast (standard, high) as one or two axes; add density only if the product has data-dense screens; add brand only with a real second brand.** Each extra axis multiplies QA surface [S-L07-004].
- **Evidence:** [S-L07-004] [S-L07-011] [S-L07-100] [S-L07-102] [S-L07-104] [S-L07-107] [S-L07-108] [S-L07-110] [S-L07-112] [S-L07-119] [S-L07-121] [S-L07-126]

### DC-L07-16: Multi-brand architecture
- **Block path:** Tokens > Theming > Brands
- **Questions the designer answers:** How many brands (or white-label clients) share the system? What may differ per brand: only color, or also type, radius and motion? Who maintains brand values: the core team or brand teams?
- **Options:**
  1. *Brand as a mode* in the semantic collection (brand A light, brand A dark, brand B light...). Simple, but capped by the plan's mode limit (Pro 10, Org 20) and it multiplies with other axes [S-L07-014].
  2. *Brand as its own collection/axis* (a "Brand" collection feeding brand primitives; semantic collection keeps light/dark). Additive: 3 brands + 2 schemes = 5 modes across 2 collections [S-L07-011] [inferred].
  3. *Figma extended collections* (Enterprise): the core publishes a parent collection; each brand extends it and overrides only what differs; new variables flow down automatically. Brand teams cannot add variables or modes [S-L07-015] [S-L07-016].
  4. *DTCG*: brand as a resolver modifier (`brand: {a:[...], b:[...]}`), or group `$extends` to inherit and override [S-L07-004] [S-L07-002].
  5. *Separate libraries per brand* sharing a component library [inferred].
  6. *Generated brand themes*: SLDS 2 lets admins create a custom theme from one brand color and generates the palette automatically [S-L07-118].
  - Community signal: multi-brand and white-label setups with Figma variables and modes (a thread about 50+ white-label clients) are a live practitioner question [S-L07-045].
- **Visual effect:** Brands typically differ in accent color, typeface, corner radius and illustration while sharing layout and components; the less they differ, the more one library can serve them [inferred; see L06].
- **Depends on (upstream):** Figma plan (DC-L07-27); L06 brand-to-product translation; which token categories are brandable.
- **Affects (downstream):** mode counts (DC-L07-17), collection structure (DC-L07-18), build outputs per brand.
- **Token encoding:** brand tier: `brand.accent` = `{color.violet.600}` (brand A) or `{color.teal.600}` (brand B); semantic `color.bg.accent` = `{brand.accent}` [inferred example]. Figma REST: extended collection = `parentVariableCollectionId` + `variableOverrides` [S-L07-034].
- **Platform notes:** Extended collection chains are possible (C extends B extends A) [S-L07-034]. Color and opacity override together [S-L07-015]. Migrating to extended collections resets applied modes in consuming files [S-L07-015].
- **Accessibility constraints:** each brand's accent must pass contrast against every surface in every scheme; a brand override can silently break contrast [inferred].
- **Default + heuristic:** **Default: a dedicated brand axis (collection or resolver modifier) that only overrides a small, named set of "brandable" tokens (accent colors, font family, radius).** On Enterprise use extended collections. Rule: if brands differ in more than ~20% of semantic tokens, they are separate themes, not brands [inferred].
- **Evidence:** [S-L07-002] [S-L07-004] [S-L07-011] [S-L07-014] [S-L07-015] [S-L07-016] [S-L07-034] [S-L07-045] [S-L07-118]

### DC-L07-17: Containing the mode-combination explosion
- **Block path:** Tokens > Theming > Combinations
- **Questions the designer answers:** How many theme combinations will ship? Which axes are independent? What must be designed and tested?
- **Options:**
  1. *Flatten everything into one axis* (lightHighContrast, darkHighContrast, brandA-dark-compact...). The DTCG resolver example itself uses a flattened `theme` modifier with 4 contexts (light, lightHighContrast, dark, darkHighContrast) built by layering source files [S-L07-004].
  2. *Orthogonal axes*: each axis (scheme, contrast, density, brand) touches a disjoint set of tokens. The resolver spec recommends orthogonality because overlapping modifiers make array order decide the result [S-L07-004].
  3. *Layered overrides*: high contrast is a small override file applied on top of light or dark, not a full copy (the resolver example layers `dark-high-contrast.json` over `dark.json`) [S-L07-004].
  4. *Separate Figma collections per axis*, so combinations are picked per frame instead of pre-built [S-L07-011].
  5. *Pre-built permutations as files*: Primer ships 14 flattened theme files covering light, dark and dark-dimmed with high-contrast, colorblind and tritanopia variants [S-L07-110]. Style Dictionary builds one output per combination [S-L07-162]; Terrazzo's CSS plugin emits one selector or media-query block per permutation [S-L07-182].
- **Visual effect:** none by itself; unmanaged explosion shows up as inconsistent, untested combinations [inferred].
- **Depends on (upstream):** DC-L07-15, DC-L07-16.
- **Affects (downstream):** QA matrix, build time, Figma mode caps, CSS size.
- **Token encoding:** the number of permutations equals the product of contexts across modifiers (4 x 3 x 2 = 24 in the spec's example) [S-L07-004]. Keep per-axis files small so each context only overrides what it owns.
- **Platform notes:** Figma mode caps apply per collection (Pro 10, Org 20, API 40), so orthogonal collections avoid hitting them [S-L07-014] [S-L07-034].
- **Accessibility constraints:** every shipped combination needs contrast verification; automate it over the full permutation list [inferred].
- **Default + heuristic:** **Default: at most 3 axes, each orthogonal, with high contrast as a layered override.** Rule: if two axes both need to set the same token, merge them into one axis [S-L07-004].
- **Evidence:** [S-L07-004] [S-L07-011] [S-L07-014] [S-L07-034] [S-L07-110] [S-L07-162] [S-L07-182]


### DC-L07-18: Figma collection structure (how tiers map to collections)
- **Block path:** Figma > Variables > Collections
- **Questions the designer answers:** How many collections? Which collection carries modes? Where do primitives live, and can consumers see them?
- **Options:**
  1. *One collection per tier*: `Primitives` (one mode, hidden from publishing), `Semantic` (modes: light, dark, ...), optionally `Component` (aliases semantic) [S-L07-018] [S-L07-025].
  2. *One collection per theming axis*: `Color theme` (light/dark/HC), `Density` (compact/comfortable), `Breakpoint` (mobile/tablet/desktop), `Brand`. Each axis is set independently on frames or pages [S-L07-011].
  3. *Single mega-collection*: fewer clicks, but every mode must hold every variable. Plan mode caps apply (Pro 10, Org 20) [S-L07-014].
  4. *Figma's own course example*: a `Primitives` collection (hidden from publishing, "Show in all supported properties" unchecked) plus a `Tokens` collection holding semantic and component tokens side by side, with dark mode as a mode on `Tokens` [S-L07-050].
- **Visual effect:** none directly; affects how easily designers preview combinations.
- **Depends on (upstream):** DC-L07-01 tier count; DC-L07-15 theming axes.
- **Affects (downstream):** mode switching UI, library publishing, Check designs suggestion quality [S-L07-025].
- **Token encoding:** Figma variable names use slash groups: `color/bg/surface`, `space/inset/md` [S-L07-011].
- **Platform notes:** Each collection has at most 5,000 variables [S-L07-013]. Mode caps are per collection (Pro 10, Org 20, API 40) [S-L07-014] [S-L07-034]. Modes can be set per layer, frame, section or page, and "Auto" inherits [S-L07-011].
- **Accessibility constraints:** a high-contrast mode inside the color collection keeps HC previewable on any frame [S-L07-011].
- **Default + heuristic:** **Default: Primitives (hidden) + Semantic color (light/dark[/HC]) + Semantic dimension (density or breakpoint), plus a Motion collection with a reduced mode.** One collection per orthogonal axis keeps mode counts additive rather than multiplicative [S-L07-011] [inferred].
- **Evidence:** [S-L07-011] [S-L07-013] [S-L07-014] [S-L07-018] [S-L07-025] [S-L07-034] [S-L07-050]

### DC-L07-19: Scoping and visibility (keeping primitives out of designers' hands)
- **Block path:** Figma > Variables > Scope & publishing
- **Questions the designer answers:** Which property pickers should each token appear in? Should primitives be publishable?
- **Options:** "Show in all" (no scope) vs precise scopes (for example text colors scoped to Text fill only; spacing scoped to Gap and Padding; radius scoped to Corner radius) [S-L07-018] [S-L07-034]. Hide primitives from publishing [S-L07-018].
- **Visual effect:** fewer wrong-token mistakes (for example a border color used as a text color), which shows as more consistent UI [inferred].
- **Depends on (upstream):** semantic naming that already encodes the property (DC-L07-04).
- **Affects (downstream):** Check designs suggestions. Figma explicitly recommends hiding primitives and scoping precisely to improve them [S-L07-025].
- **Token encoding:** REST `scopes: ["TEXT_FILL"]`, `["GAP"]`, `["CORNER_RADIUS"]`; `hiddenFromPublishing: true` [S-L07-034].
- **Platform notes:** Scopes exist for number, color and string variables only. The REST doc still says "FLOAT and COLOR" [S-L07-018] [S-L07-034].
- **Accessibility constraints:** scope foreground and background colors separately so contrast-approved pairs are the easy path [inferred].
- **Default + heuristic:** **Default: hide all primitives; scope every semantic variable to the properties its name says** (a `.../text/...` color gets TEXT_FILL only) [S-L07-018] [S-L07-025].
- **Evidence:** [S-L07-018] [S-L07-025] [S-L07-034]

### DC-L07-20: Code syntax and platform names in Figma
- **Block path:** Figma > Variables > Code syntax
- **Questions the designer answers:** What name does a developer see for each variable in Dev Mode, per platform?
- **Options:** Set Web, Android and iOS code syntax per variable (at most 3). They appear in Dev Mode snippets for CSS, SwiftUI and Compose [S-L07-018]. Or leave them unset, and Dev Mode shows the raw Figma name [inferred].
- **Visual effect:** none.
- **Depends on (upstream):** DC-L07-06 casing and name transforms.
- **Affects (downstream):** Dev Mode handoff, MCP `get_variable_defs` output, Code Connect [S-L07-027] [S-L07-030].
- **Token encoding:** Figma `color/bg/surface` becomes Web `var(--ds-color-bg-surface)`, iOS `Color.dsBgSurface`, Android `DsTheme.colors.bgSurface` [inferred example]. REST `codeSyntax: {WEB, ANDROID, iOS}` [S-L07-034].
- **Platform notes:** Only three platform slots (no separate Flutter or React Native) [S-L07-018].
- **Accessibility constraints:** none.
- **Default + heuristic:** **Default: generate code syntax automatically from the same name transform the pipeline uses,** so the Figma and code names can never disagree [inferred].
- **Evidence:** [S-L07-018] [S-L07-027] [S-L07-030] [S-L07-034]

### DC-L07-21: Styles vs variables in Figma (which to use for what)
- **Block path:** Figma > Styles vs Variables
- **Questions the designer answers:** Which decisions become variables, and which stay styles?
- **Options:**
  - *Variables*: single raw values; modes; aliasing; scoping; code syntax [S-L07-013] [S-L07-019].
  - *Styles*: composites expressed all at once (full text specs, layered shadows, gradients, stacked fills, images, blend modes, layout guide grids); no aliasing; cannot be used inside variables [S-L07-019] [S-L07-020].
  - *Hybrid*: styles whose fields are bound to variables [S-L07-019].
- **Visual effect:** none directly; decides whether mode switching changes a property.
- **Depends on (upstream):** DC-L07-12 and DC-L07-13.
- **Affects (downstream):** Check designs can swap hard-coded colors to variables but not to color styles [S-L07-025].
- **Token encoding:** primitive and semantic colors, spacing, radius, sizes, opacity and motion become variables. Typography, shadows, gradients and layout grids become styles bound to variables [S-L07-019] [S-L07-020].
- **Platform notes:** DTCG composites (typography, shadow, gradient) correspond to styles, not variables [S-L07-011] [S-L07-020].
- **Accessibility constraints:** none specific.
- **Default + heuristic:** **Default: "variables for values, styles for bundles".** Any single value that changes by mode must be a variable [S-L07-019].
- **Evidence:** [S-L07-011] [S-L07-013] [S-L07-019] [S-L07-020] [S-L07-025]

### DC-L07-22: Component API in Figma (variants vs properties vs slots)
- **Block path:** Components > Figma component API
- **Questions the designer answers:** Which component differences are variants, and which are boolean, text, instance-swap or slot properties? How much freedom does an instance get?
- **Options (5 property types):** variant (states, sizes, types); boolean (show or hide a layer only); text (editable string, no rich text); instance swap (one swappable nested instance with preferred values); slot (freeform area; preferred instances, "only allow preferred", min/max layer counts) [S-L07-021] [S-L07-022] [S-L07-023].
- **Visual effect:** Slots allow varied layouts (cards, modals, lists) without detaching, so instances keep receiving library updates [S-L07-022].
- **Depends on (upstream):** L08 component anatomy; the code component API (React props and children).
- **Affects (downstream):** variant count (explodes with variant-only modelling), detach rate, library analytics, Code Connect property mapping [S-L07-022] [S-L07-026] [S-L07-029].
- **Token encoding:** Component tokens (if used) bind to the layers the properties expose. String and number variables can drive variant choice by mode, for example a density mode switching a size variant [S-L07-011].
- **Platform notes:** Slots are intended to map to React slots/children [S-L07-022]. Boolean props bind only to layer visibility [S-L07-021].
- **Accessibility constraints:** model states (focus, disabled, error) as variants so they are designed explicitly, not hidden [inferred; see L08].
- **Default + heuristic:** **Default: variants only for state, size and type; booleans for optional icons; text props for labels; instance swap for single fixed-position icons; slots for anything repeating or freeform** [S-L07-023].
- **Evidence:** [S-L07-011] [S-L07-021] [S-L07-022] [S-L07-023] [S-L07-026] [S-L07-029]

### DC-L07-23: Deprecation, descriptions and change management for tokens
- **Block path:** Tokens > Governance > Lifecycle
- **Questions the designer answers:** How is a token retired? Where is a token's intent written down? How are changes reviewed?
- **Options:** DTCG `$deprecated: true` or `$deprecated: "Use X instead"` (group deprecation inherited) plus `$description` [S-L07-002]. Figma: variable descriptions, library publishing and review, branching (Org/Ent) [S-L07-031]. Library analytics identify unused variables before removal (Org/Ent; variables tracked since 10 Oct 2024) [S-L07-029].
- **Visual effect:** none.
- **Depends on (upstream):** DC-L07-08.
- **Affects (downstream):** consumer upgrade pain; AI agents read descriptions [S-L07-042].
- **Token encoding:** `{"$value":"{color.bg.brand}","$type":"color","$deprecated":"Use color.bg.accent (v4)"}` [shape from S-L07-002].
- **Platform notes:** Figma has no native "deprecated" flag on variables [inferred; none found in S-L07-018 or S-L07-034]. The common workaround is a description note or hiding from publishing [inferred].
- **Accessibility constraints:** none.
- **Default + heuristic:** **Default: every semantic token gets a `$description` that states its intended use; deprecate for one release before deleting; check analytics usage before removal** [S-L07-002] [S-L07-029].
- **Evidence:** [S-L07-002] [S-L07-018] [S-L07-029] [S-L07-031] [S-L07-034] [S-L07-042]

### DC-L07-24: Design-to-code linkage and AI readiness (Code Connect, MCP, descriptions)
- **Block path:** Tooling > Design-code bridge
- **Questions the designer answers:** Will AI agents and developers see real code components for Figma components? What must the library contain for agents to use it well?
- **Options:**
  1. Code Connect UI (inside Figma; optional GitHub; several frameworks per component; custom AI instructions) [S-L07-026].
  2. Code Connect CLI (repo templates; property mappings) [S-L07-026].
  3. None: the MCP `get_design_context` then emits generic React + Tailwind [S-L07-027].
  4. AI-readiness content: meaningful names (`Card/Product/Default`), descriptions, auto layout, variables applied, `_example` components or an "Examples" page (up to 200 examples) [S-L07-042]. An MCP rules file from the `create_design_system_rules` prompt [S-L07-027].
- **Visual effect:** Generated UI matches the real system instead of looking generic [S-L07-042].
- **Depends on (upstream):** Organization or Enterprise plan for Code Connect [S-L07-014] [S-L07-026].
- **Affects (downstream):** handoff speed, agent output quality, Figma Make and agent generation [S-L07-028] [S-L07-042].
- **Token encoding:** code syntax on variables (DC-L07-20) is what `get_variable_defs` returns alongside values [S-L07-027] [inferred].
- **Platform notes:** The remote MCP server needs a frame or layer link (selection-based prompting is desktop-only). The `clientFrameworks` parameter picks React vs SwiftUI mappings [S-L07-027].
- **Accessibility constraints:** put a11y usage rules in Code Connect custom instructions so agents inherit them [inferred].
- **Default + heuristic:** **Default: Code Connect UI for the top 20 components first; descriptions on every component and semantic variable; an Examples page.** For a builder product, generating these descriptions is cheap and pays off in AI output quality [S-L07-026] [S-L07-042] [inferred].
- **Evidence:** [S-L07-014] [S-L07-026] [S-L07-027] [S-L07-028] [S-L07-042]

### DC-L07-25: Pipeline and transformer choice
- **Block path:** Tooling > Token pipeline
- **Questions the designer answers:** Which tool turns token JSON into platform code? Must it understand DTCG resolvers? Which platforms must be emitted? Do we want a hosted hub?
- **Options:**
  1. *Style Dictionary v5*: the widest platform coverage (Android XML, Compose, Swift, Flutter, React Native). DTCG 2025.10 colors and dimensions supported; **no resolver support yet**, so themes mean one build per combination [S-L07-151] [S-L07-155] [S-L07-156] [S-L07-162].
  2. *Terrazzo 2.x*: full DTCG 2025.10 including resolvers; web-strong (CSS, Sass, Tailwind, JS, vanilla-extract); Swift pre-1.0; no Android [S-L07-179] [S-L07-180] [S-L07-182].
  3. *Tokens Studio + sd-transforms*: best when designers author in the plugin; exports themes to Figma collections and modes [S-L07-167] [S-L07-172].
  4. *Hosted hubs*: zeroheight (DTCG 2025.10 + Style Dictionary v5 outputs, PRs to repos), Supernova (exporters, themes, MCP context), Knapsack (live theming on real components) [S-L07-203] [S-L07-192] [S-L07-204]. Specify is gone [S-L07-186].
- **Visual effect:** none.
- **Depends on (upstream):** DC-L07-08 (source of truth); the platform list (L10); whether the builder itself will emit code.
- **Affects (downstream):** naming transforms (DC-L07-06), mode strategy (DC-L07-17), code syntax (DC-L07-20).
- **Token encoding:** Keep the source strictly DTCG 2025.10 plus a resolver, so that any of these tools can be swapped in [S-L07-002] [S-L07-004].
- **Platform notes:** Terrazzo's Figma import requires the Enterprise REST API [S-L07-183] [S-L07-034]. Style Dictionary needs Node 22+ from v5 [S-L07-151].
- **Accessibility constraints:** run contrast checks in the pipeline over every resolved permutation [inferred].
- **Default + heuristic:** **Default for a builder: emit DTCG 2025.10 + resolver as the canonical export.** Offer Terrazzo for web-only teams and Style Dictionary v5 when native mobile outputs are needed. For Style Dictionary, pre-expand resolver permutations into one build per combination [S-L07-155] [S-L07-162] [S-L07-179].
- **Evidence:** [S-L07-002] [S-L07-004] [S-L07-034] [S-L07-151] [S-L07-155] [S-L07-156] [S-L07-162] [S-L07-167] [S-L07-172] [S-L07-179] [S-L07-180] [S-L07-182] [S-L07-183] [S-L07-186] [S-L07-192] [S-L07-203] [S-L07-204]


### DC-L07-26: Governance tooling in Figma (lint, analytics, branching)
- **Block path:** Governance > Tooling
- **Questions the designer answers:** How do we find hard-coded values and off-system usage? How do we measure adoption? How are library changes reviewed?
- **Options:** Check designs (Org/Ent; deterministic, no LLM; flags hard-coded color, type, radius and spacing, wrong-library assets and detached components; suggests matching variables; AA/AAA contrast check) [S-L07-025]. Library analytics (Org/Ent) [S-L07-029]. Branching and merging (Org/Ent) [S-L07-031]. Third-party lint plugins [inferred].
- **Visual effect:** more consistent products over time [inferred].
- **Depends on (upstream):** a published, variables-based library with precise scopes. Check designs "works best" with one [S-L07-025].
- **Affects (downstream):** adoption metrics (L11), deprecation decisions (DC-L07-23).
- **Token encoding:** Check designs ranks suggestions partly by "variable naming and hierarchy", so consistent semantic names improve lint quality [S-L07-025].
- **Platform notes:** One page at a time; 25K-layer cap; cannot swap color styles [S-L07-025].
- **Accessibility constraints:** the contrast check covers AA or AAA [S-L07-025].
- **Default + heuristic:** **Default on Org/Ent: run Check designs before "Ready for dev"; review analytics every quarter.** On Professional (no analytics, branching or Check designs) the builder must provide lint and analytics itself [S-L07-014] [S-L07-025] [S-L07-029].
- **Evidence:** [S-L07-014] [S-L07-025] [S-L07-029] [S-L07-031]

### DC-L07-27: Figma plan tier as a design constraint
- **Block path:** Tooling > Figma plan
- **Questions the designer answers:** Which plan does the team have, and which architecture does that allow?
- **Options and what each unlocks:**
  - *Starter*: variables, but no extra modes; cannot publish libraries [S-L07-011] [S-L07-014] [S-L07-020].
  - *Professional*: libraries; **10 modes per collection**; no Code Connect, branching, analytics, Check designs or REST variables [S-L07-014].
  - *Organization*: **20 modes**; Code Connect; branching; analytics; Check designs [S-L07-014] [S-L07-025].
  - *Enterprise*: extended collections (multi-brand), "unlimited modes with extended collections", REST variables API, team default modes [S-L07-014] [S-L07-015] [S-L07-034] [S-L07-011].
- **Visual effect:** none directly. On lower plans, multi-brand must be built from modes or separate files [inferred].
- **Depends on (upstream):** budget and org size.
- **Affects (downstream):** DC-L07-16 (multi-brand), DC-L07-17 (mode explosion), DC-L07-08 (source of truth: REST automation needs Enterprise).
- **Token encoding:** n/a.
- **Platform notes:** the MCP server works on all plans, but Starter gets 20 tool calls a month and View/Collab seats on paid plans get 6. Dev/Full seats get 200 a day on Professional and Organization and 600 a day on Enterprise [S-L07-049].
- **Accessibility constraints:** none.
- **Default + heuristic:** **The builder should ask for the plan first** and grey out architectures the plan cannot hold. Example: Professional with 3 brands and light/dark needs 6 modes (fits within 10); 4 brands with light/dark/HC needs 12 (exceeds 10) [S-L07-014] [inferred arithmetic].
- **Evidence:** [S-L07-011] [S-L07-014] [S-L07-015] [S-L07-016] [S-L07-020] [S-L07-025] [S-L07-034] [S-L07-049]

### DC-L07-28: Layout and breakpoint tokens (grid auto layout, breakpoints as modes)
- **Block path:** Tokens > Layout
- **Questions the designer answers:** Are breakpoints, columns, gutters and margins tokens? Do they switch by mode in Figma?
- **Options:** number variables for layout guides (column and row count, width, margin, offset, gutter) [S-L07-013]; a "Breakpoint" collection with mobile/tablet/desktop modes [S-L07-011]; grid auto layout (tracks, spans) for real responsive structure, which maps to CSS grid [S-L07-024] [S-L07-044].
- **Visual effect:** consistent gutters and margins across devices; bento and dashboard layouts built with grid [S-L07-024].
- **Depends on (upstream):** L03 grid and breakpoints.
- **Affects (downstream):** page templates, containers, cards.
- **Token encoding:** `layout.grid.columns` (number: 4/8/12 by mode), `layout.gutter` (dimension), `layout.margin` (dimension) [inferred example]. DTCG has no media-query type, so breakpoints are plain dimensions or resolver contexts [S-L07-002] [S-L07-004].
- **Platform notes:** Layout guides are visual aids; grid auto layout actually reflows content [S-L07-024].
- **Accessibility constraints:** reflow at 320 CSS px (WCAG 1.4.10; see L03) [inferred].
- **Default + heuristic:** **Default: a Breakpoint collection with 3 modes driving spacing and layout-guide variables; grid auto layout for multi-column components** [S-L07-011] [S-L07-013] [S-L07-024].
- **Evidence:** [S-L07-002] [S-L07-004] [S-L07-011] [S-L07-013] [S-L07-024] [S-L07-044]

---

## Part C. Suggested internal data model for the builder (synthesis, [inferred] from Parts A and B)

This is a recommendation, not a sourced fact. It is built so that every entity round-trips losslessly to DTCG 2025.10 + Resolver, and maps predictably onto Figma collections, modes, styles and component properties.

| Entity | Fields | Round-trips to | Why |
|---|---|---|---|
| `Token` | `path` (array of lowercase segments; no `.`, `{`, `}` or leading `$`), `type` (the 13 DTCG types plus builder extensions `string`, `boolean`, `spring`), `valuesByContext` (map from resolver context to literal or alias), `description`, `deprecated` (bool or string), `tier` (primitive, semantic, component), `extensions` | DTCG token (`$value`, `$type`, `$description`, `$deprecated`, `$extensions`) [S-L07-002] | the spec's name rules and types [S-L07-002] |
| `Alias` | target token path, or a JSON Pointer for property-level references | `"{a.b.c}"` or `{"$ref": "#/a/b/c/$value/..."}` [S-L07-002] | both syntaxes are required by the spec [S-L07-002] |
| `Group` | path, default `type`, description, deprecated, optional `extends` | DTCG group with `$type`, `$extends` [S-L07-002] | type inheritance and group inheritance [S-L07-002] |
| `Set` (tier file) | name, ordered token sources | resolver `sets` [S-L07-004] | primitives, semantics and components as separate files [S-L07-004] |
| `Axis` (modifier) | name (scheme, contrast, density, brand, breakpoint, motion), contexts, default, `orthogonal` check | resolver `modifiers` [S-L07-004]; Figma: one collection per axis, one mode per context [S-L07-011] | permutations = product of contexts; the spec recommends orthogonal axes [S-L07-004] |
| `ResolutionOrder` | ordered sets and axes | resolver `resolutionOrder` [S-L07-004] | last wins [S-L07-004] |
| `FigmaBinding` (extension) | `scopes[]` (REST enum names), `codeSyntax {WEB, ANDROID, iOS}`, `hiddenFromPublishing`, `collection`, `styleKind` (for composites: text, effect, paint, grid) | `$extensions["com.figma.*"]` plus Figma REST/Plugin API [S-L07-034] [S-L07-011] | the fields Figma needs that DTCG lacks [S-L07-018] [S-L07-034] |
| `Brand` | parent collection, overridden token paths | Figma extended collection (Enterprise) or a resolver `brand` axis [S-L07-015] [S-L07-004] | plan-dependent (DC-L07-27) |
| `Component` | name, anatomy, `properties[]` with `kind` in {variant, boolean, text, instanceSwap, slot}, preferred instances, slot min/max, component tokens | Figma component properties [S-L07-021] [S-L07-022]; Code Connect mapping [S-L07-026] | the Figma component API (DC-L07-22) |
| `Permutation` | one resolved token set per context combination | build output (CSS scope, Swift or Kotlin theme object) [S-L07-182] [S-L07-162] | contrast checks and QA run per permutation |

Constraints the builder should enforce, with sources: at most 5,000 variables per Figma collection [S-L07-013]; plan mode caps (Pro 10, Org 20; API 40) [S-L07-014] [S-L07-034]; Figma import accepts only sRGB/HSL colors, px dimensions and s durations [S-L07-011]; aliases must share a type and must not form cycles [S-L07-013] [S-L07-034].

---

## Cross-lane notes
(Kept here, not in BOARD.md, as the orchestrator instructed.)
- [L07 -> L01] Figma's native variable import accepts only `srgb` and `hsl` colors. OKLCH or Display P3 primitives must be exported to Figma as sRGB with a `hex` fallback. DTCG 2025.10 itself supports 14 color spaces and a `"none"` component [S-L07-011] [S-L07-003]. Material's 3 contrast levels, Primer's 14 theme files and Atlassian's increased-contrast themes show contrast is now a theming axis [S-L07-104] [S-L07-110] [S-L07-108].
- [L07 -> L02] The DTCG `typography` composite has only fontFamily, fontSize, fontWeight, letterSpacing and a unitless lineHeight (issue #102 is open). It has no text case, decoration, paragraph spacing or font style. Figma letter-spacing variables are interpreted as px, and Figma cannot import the typography composite as variables [S-L07-002] [S-L07-013] [S-L07-011].
- [L07 -> L03] DTCG `dimension` allows only px and rem. Breakpoint and density are best modelled as a Figma collection with modes, or as a resolver modifier. Grid auto layout (Config 2025, all plans) maps to CSS grid [S-L07-002] [S-L07-011] [S-L07-024].
- [L07 -> L04] Figma now has **timing and easing variables** (easing can be a Bezier curve or a spring: presets Gentle, Quick, Bouncy, Slow, or a custom "Bounce" value). DTCG has no spring type (issue #429 opened 28 Jun 2026). DTCG `shadow` supports `inset` and layered arrays [S-L07-013] [S-L07-033] [S-L07-048] [S-L07-002].
- [L07 -> L06] Figma extended collections (true multi-brand inheritance) are Enterprise-only. SLDS 2 generates a whole theme from one brand color [S-L07-015] [S-L07-118].
- [L07 -> L08] Figma component properties are now 5 types: variant, boolean (visibility only), text, instance swap, and **slot** (preferred instances, "only allow preferred", min/max layer counts). String, number and boolean variables can drive variant choice by mode [S-L07-021] [S-L07-022] [S-L07-011].
- [L07 -> L10] Figma code syntax has only 3 slots (Web, Android, iOS); Dev Mode snippets cover CSS, SwiftUI and Compose. Style Dictionary v5 covers android, compose, ios-swift, flutter and react-native. Terrazzo has Swift (pre-1.0) but no Android output [S-L07-018] [S-L07-156] [S-L07-180].
- [L07 -> L11] Governance features are plan-gated. Check designs (no LLM), library analytics (variables tracked since 10 Oct 2024), branching and Code Connect are Organization/Enterprise only. MCP limits range from 20 calls/month on Starter to 600/day on Enterprise Dev/Full seats. The Figma agent learns composition from a `_example` suffix or an "Examples" page (up to 200 examples). Specify shut down in Nov 2024 [S-L07-025] [S-L07-029] [S-L07-031] [S-L07-049] [S-L07-042] [S-L07-186].
- [L07 -> L12] Current Figma MCP tool names (for when the MCP server is enabled): `get_variable_defs`, `get_design_context`, `get_metadata`, `search_design_system` and `get_libraries` (both remote-only), `use_figma` (write, remote-only). `create_design_system_rules` is now an MCP **prompt**, not a tool. The remote server needs a node link; selection prompting works only on the desktop server [S-L07-027].
- [L07 -> S1] Suggested builder data model: DTCG 2025.10 Format + Resolver as the canonical model, with extensions for Figma scopes, code syntax, springs, and string/boolean types (Part C) [S-L07-002] [S-L07-004] [inferred].

## Open questions / gaps
- **Figma's native DTCG export shape is undocumented.** Help pages describe import rules but not exactly what export writes (for example whether scopes, code syntax or descriptions go into `$extensions`). A hands-on export test is needed; this belongs with L12 once the Figma MCP server is available [S-L07-011] [S-L07-046].
- **Timing vs duration units in Figma** are inconsistent across surfaces: the UI shows ms, the plugin API uses seconds, and DTCG import accepts only `s`. The REST API does not list TIMING/EASING yet [S-L07-013] [S-L07-040] [S-L07-011] [S-L07-034].
- **Slots plan gating**: the help article says "all plans", while the Schema 2025 note said a Full seat is needed on paid plans. The exact seat rule was not re-verified [S-L07-022] [S-L07-016].
- **Boolean variables on boolean properties**: the modes article says boolean variables cannot bind boolean properties on instances, yet the component-properties article lets a boolean property's default take a boolean variable. The real behaviour needs a hands-on test [S-L07-011] [S-L07-021].
- **Stale Figma article**: "The difference between variables and styles" (body edited 1 Oct 2025) still says scoping is number-only and code syntax is "in development"; newer articles contradict both. Figma's course lesson ticks "supports color gradients" for variables, but its own text says variables cannot hold gradients [S-L07-019] [S-L07-018] [S-L07-050].
- **Style Dictionary resolver support** is not implemented (issue #1590). Whether Autodesk's offered resolver layer lands, and when, is unknown [S-L07-155].
- **Not verified**: Supernova's current DTCG import/export; whether Knapsack's docs mention DTCG; zeroheight's mode handling; whether Tokens Studio emits 2025.10 color objects; the Tokens Studio platform launch date (from the pipelines helper).
- **DTCG issue #348** (`$modes` array) was closed, but its close reason was not read because the GitHub API was rate-limited [S-L07-048].
- **Config 2026 exact dates and location** were not captured. Only the 23-24 Jun 2026 launch and rollout dates are verified [S-L07-017] [S-L07-039].
- **Material comp tokens** are marked "in development" on m3.material.io, and Material Web is in maintenance mode, so the current status of the public M3 component-token API is unclear [S-L07-100] [S-L07-103].
- **Perplexity was unavailable** (quota exhausted), so cross-checking relied on WebSearch, WebFetch, curl against official APIs, and the browser.

## Confidence
- **Confirmed from Tier A primary sources (high):**
  - DTCG 2025.10 facts: the three modules, status, 28 Oct 2025 date, all reserved properties, all 13 types and their sub-properties, 14 color spaces, resolver structure [S-L07-002] [S-L07-003] [S-L07-004].
  - Figma variable types (6), the 5,000-variable cap, mode caps (Pro 10, Org 20, API 40), scoping enums, code syntax slots, DTCG import rules, extended collections (Enterprise), plan gates for Code Connect, branching, analytics, Check designs and the REST API [S-L07-011] [S-L07-013] [S-L07-014] [S-L07-015] [S-L07-018] [S-L07-034].
  - The MCP tool list and rate limits [S-L07-027] [S-L07-049].
  - Tool versions (Style Dictionary 5.5.5, Terrazzo CLI 2.x, sd-transforms 2.0.3) [S-L07-151] [S-L07-178] [S-L07-171].
  - System token names and values in A8, all read from official docs or published npm packages [S-L07-100..126].
- **Tier B, corroborated (medium-high):** EightShapes naming levels and the 3-or-more-components promotion rule [S-L07-036]; Brad Frost's tier definitions [S-L07-132]; the Figma blog dates for Schema 2025 (28 Oct 2025) and Config 2026 (24 Jun 2026) [S-L07-038] [S-L07-039].
- **Inferred (marked `[inferred]` in the text):**
  - Every "Default + heuristic" recommendation.
  - The Part C data model.
  - Example token values where no source value is cited.
  - The mode-count arithmetic in DC-L07-27.
  - Native-platform naming examples.
  - The claim that Atlassian publishes no component tokens (inferred from its token names).
- **Community (Tier C via L00):** "code is the source of truth" is the practitioner majority view. It is used only to support the DC-L07-08 default, not as fact [S-L07-045].
