# Glossary verification (fresh-context sample audit)

Checked on 2026-09-23 against `synthesis/glossary.json` (393 entries), by a verifier that did not write the glossary. Nothing in `glossary.json` or the shards was edited.

## Method

- **Sample:** 70 entries, stratified by layer. Every layer has 5 entries, with 3 extra for `found`, 1 for `core` and 1 for `use`. Seed 23, sorted ids per layer:
  ```
  python3 -c "import json,random,collections; random.seed(23); d=json.load(open('synthesis/glossary.json')); by=collections.defaultdict(list)
  [by[e['layer']].append(e['id']) for e in d]; q={l:5 for l in by}; q.update(found=8, core=6, use=6)
  print([i for l in sorted(by) for i in random.sample(sorted(by[l]), q[l])])"
  ```
- **Sources read for each entry:** its ontology node, every Decision Card it cites (`synthesis/cards.json`), the research sections it names (`research/L03`, `L07`, `L08-component-catalog`, `L15`, `L16`), `synthesis/levers.json` and `LEVERS.md` for the dials, `OPENDESIGNER-SPEC.md` (sections 6.4, 7.4 to 7.12), and `skills/opendesigner/scripts/engine.py` plus `references/rules.md`, `zoom.md` and `questions.json` for the `use` entries.
- **Emitted token names:** I ran `engine.py sketch` in a scratch directory. It emitted 377 tokens in 60 groups, and I compared every token name in the sampled engineer voices against that output.
- **External standards, checked on live official pages:** WCAG 2.2 SC 1.4.3 and 1.4.11 exempt inactive components; SC 2.5.8 is AA at 24 by 24 CSS px; SC 3.3.8 is AA and is met by allowing paste and password managers; SC 3.1.5 is AAA (all on w3.org). DTCG 2025.10: `fontWeight` takes 1 to 1000 plus aliases up to extra-black 950; curly-brace references target whole tokens and `$ref` reaches inside values; circular references are errors; `dimension` allows only px and rem (designtokens.org). Window size classes break at 840dp and 1600dp (developer.android.com). The M3 standard default spatial spring is damping 0.9 and stiffness 700 (androidx `StandardMotionTokens.kt`). The Figma remote MCP server needs a frame or layer link (developers.figma.com). The 76dp car target comes from `research/L14` with a trace to the Design for Driving page; I did not re-fetch it, because Google moved that page behind a partner login.
- **Mechanical check:** `python3 tools/check_glossary.py synthesis/glossary.json` printed 0 errors, with a plain-voice mean grade of 5.3.

**Sample ids (70):**
builder.controls, builder.ai, builder, builder.state, builder.input,
comp.implementation, comp.layout, comp.feedback.ai, comp.behavior, comp.states.disabled,
core.font-weight, core.margin, core.spring-animation, core.alias, core.grid, core.status-colors,
ctx.strategy, ctx, ctx.brand, ctx.platforms.stack, ctx.platforms,
deliver.interop.figma.code-connect, deliver, deliver.interop.figma.styles, deliver.interop.paper, deliver.source-of-truth,
dial.expression, dial.roundness, dial.brandPresence, dial.colorfulness, dial.warmth,
found.layout.safe-areas, found.icon.construction, found.sensory, found.color.states, found.motion.interruptibility, found.content.readability, found.space, found.icon.color,
gov.measure, gov.decisions, gov.tooling, gov.contribution, gov.team,
guard.safety, guard, guard.enforcement, guard.testing, guard.checks,
pat.navigation.containers, pat.layout.canonical, pat.overlay, pat.other, pat.empty,
prin.ux.heuristics, prin.visual.style, prin.visual, prin.visual.polish, prin.visual.grouping,
tok.types.motion, tok.themes, tok.modes, tok.delivery, tok.coverage,
use.od-line, use.cmd-export, use.status-reference, use.file-build-folder, use.zoom-broad, use.validation-report

**Severity:** *wrong* means the entry contradicts a source or what the engine emits. *Unsupported* means it states an `[inferred]` or planned item as established fact or current behavior. *Unclear* means it is misleading or confusing, but not false.

## Problems found (23 in 21 entries)

| # | id | voice | severity | problem | evidence | suggested fix |
|---|---|---|---|---|---|---|
| 1 | core.status-colors | engineer | wrong | The grammar `color.{bg\|text\|border\|icon}.{success\|warning\|danger\|info}.{subtle\|bold}` does not match OpenDesigner's tokens. | The engine emits `color.bg.<status>.{subtle,bold,boldHover}` and flat `color.text.<status>` and `color.border.<status>`. It emits no `color.icon.<status>`; status icons use `color.text.<status>` (engine.py about line 1150). The grammar comes from DC-L01-15, not from the engine. | Name the real tokens: `color.bg.success.subtle` and `.bold`, `color.text.success`, `color.border.success`, and say that status icons take the text token. |
| 2 | found.color.states | engineer | wrong | `color.bg.brand.bold.hovered` and `state.hover.opacity = 0.08` are not emitted. | The engine emits `color.bg.accent.boldHover` and `boldPressed`, `color.bg.neutral.subtleHover`, and `opacity.state.hover = 0.08` (engine.py lines 1036, 1091-1101). `color.bg.brand` is a separate signature-surface fill. | Use `color.bg.accent.boldHover` (+1 step) and `boldPressed` (+2), or the overlay `opacity.state.hover` = 0.08 applied on the on-color. |
| 3 | found.icon.color | engineer | wrong | `color.icon.danger` does not exist, and `color.icon.default` is not an alias of secondary text. | The engine emits only `color.icon.{default, subtle, accent, onAccent}`. `default` uses the same neutral step 11 as `color.text.secondary` but is not an alias. DC-L05-08 marks its token naming `[inferred]`. | "color.icon.default (the same step as secondary text) and color.icon.subtle; status icons use color.text.danger and the other status text tokens." |
| 4 | found.icon.color | designer | unsupported | "Icons need 3:1 contrast, 4.5:1 beside body text" presents a house rule as a requirement. | WCAG 1.4.11 asks 3:1 only of icons needed to understand the content (verified on w3.org). 4.5:1 is Carbon's stricter choice, adopted as a test heuristic in DC-L05-08. | "Meaningful icons need 3:1 (WCAG); OpenDesigner also tests 4.5:1 beside body text, as Carbon does." |
| 5 | comp.states.disabled | engineer | wrong (minor) | The token `state.disabled.opacity` is misnamed. | The engine emits `opacity.disabled.content` = 0.38 and `opacity.disabled.container` = 0.12. `color.text.disabled` is correct. | Use `opacity.disabled.content` and `.container`. |
| 6 | prin.visual.polish | engineer | wrong | `radius.inner = radius.outer minus space.inset` differs from the engine's token and formula. `icon.keyline.*` is not emitted. | The engine emits `radius.nested = max(outer - padding, smallest step)` (engine.py line 1521). LEVERS B9 says plain subtraction "collapses to square". DC-L15-10 marks the keyline tokens `[inferred]`. | "radius.nested = max(container radius - padding, smallest step); keylines are documented, not tokens." |
| 7 | prin.visual.style | engineer | wrong | `$extensions.builder.stylePreset` is the placeholder that DC-L15-01 marks `[inferred]`. | The engine stores `preset` in `state.json` and `opendesigner.meta.json`, and a preset sets dial positions (`levers.json` presets). Extensions live under `$extensions.opendesigner` (spec 7.4; engine `NS`). | "Not a DTCG type: `preset` (flat2, tonal, glass, neobrutal, soft, maximal) in state.json sets dial positions, which generate shadows, borders and radius." |
| 8 | prin.visual.grouping | engineer | wrong (minor) | `space.stack.inner/outer`, `color.surface.container` and `border.width.divider` do not exist. | DC-L15-05 marks these names `[inferred]`. The engine emits `space.stack.{xs..xl}`, `space.inset.*`, `color.surface.{base,raised,sunken,overlay,nav}`, `border.width.{default,emphasis,selected}` and `color.border.subtle` for dividers. | Use the emitted names and keep "inner spacing at most half the outer". |
| 9 | prin.visual.grouping | designer | unsupported (low) | "Common region beats proximity, which beats similarity" is stated as settled. | `research/L15` line 69: the exact strength order "is less established" and comes from NN/g's applied articles. | "Usually, a boundary beats closeness, which beats looking alike." |
| 10 | core.margin | engineer | unsupported | "OpenDesigner keeps it to layout tokens such as layout.margin.compact = 16" | The engine emits no `layout.*` group; the nearest tokens are `space.section.*`. The value is Material's page margin, quoted as an example in DC-L03-04. | "In Material, page margins are 16 (compact) and 24 above; OpenDesigner uses space.section.* and gives components no outer margin." |
| 11 | tok.coverage | engineer | unsupported | "One DTCG group per category: color, font, space, size, radius, border, shadow, opacity, motion, z, breakpoint" | DC-L07-07 marks the list `[inferred]`. The engine's groups are color, font, text, space, size, radius, border, elevation, opacity, motion, focus and icon. There is no shadow, z or breakpoint group. | List the emitted groups, or say "proposed". |
| 12 | ctx.platforms | engineer | unsupported | "Modeled as a platform modifier in the Resolver (web \| ios \| android \| windows)" | DC-L10-01 marks this `[inferred]`. The generated resolver has only theme, density and motion modifiers. The platform is handled per export, and by pointer media queries for `size.target.min`. | "Handled per export target (CSS, Swift, Compose) and by input-based target sizes; no platform modifier today." |
| 13 | guard.enforcement | engineer | unsupported | Stylelint and eslint rules named no-raw-color, no-unknown-token and contrast-min are described as exported now. | DC-L11-24 marks the rule ids `[inferred]`. Spec 7.12 plans a `lint/` folder with a stylelint strict-value config and does not mention eslint. `engine.py` writes no `lint/`; `validate` and `review` do the checks today. | "Planned: a lint/ folder with a stylelint config (spec 7.12). Today engine.py validate and review catch raw values." |
| 14 | found.content.readability | engineer | unsupported | "The builder flags strings over the reading target, overlong labels and jargon" describes behavior that does not exist, and the config names are presented as real. | DC-L13-13 marks `content.readingGrade.max` and `button.label.maxWords` `[inferred]`. The engine has no string lint. Spec 6.4 lists only "button labels over 4 words" as a warning. | Say "proposed lint", or describe only the spec 6.4 warning. |
| 15 | found.sensory | engineer | unsupported | "Haptics are semantic string tokens mapped to platform APIs in $extensions" | DC-L04-26 marks this encoding `[inferred]`. DTCG 2025.10 has no string type (L07 A5). The engine emits no haptic or sound tokens, only the `haptics.intensity` parameter and the hooks H-haptic and H-sound. | "No DTCG type; OpenDesigner records a haptic intensity and asks for sounds and custom haptics through hooks." |
| 16 | deliver.interop.figma.code-connect | engineer | unsupported | "get_variable_defs returns code syntax with values" | DC-L07-24 marks this `[inferred]`. Figma's tool docs say only that it "returns the variables and styles used in your selection" (developers.figma.com). | Drop "code syntax", or say "variable names and values". |
| 17 | deliver.interop.figma.styles | engineer | wrong (minor) | "Typography, shadows, gradients and layout grids, the DTCG composites" | Layout grids are not a DTCG type. The DTCG composites are strokeStyle, border, transition, shadow, gradient and typography (verified on designtokens.org). | "Typography, shadows and gradients (DTCG composites) and layout grids become styles bound to variables." |
| 18 | use.od-line | example | wrong | "OD:set dials.roundness=45 means a bit softer corners" | Roundness defaults to 50, which gives 8px (band 48-60). 45 gives 6px (band 38-47), so the corners get slightly sharper. The error is inherited from `references/rules.md` section 9 (`--why "a bit softer"`). | "OD:set dials.roundness=65 means softer corners (12px)", and fix rules.md too. |
| 19 | use.status-reference | designer | unsupported (low) | "Identity, such as logos, exact brand hues or typefaces, is never copied" is overstated. | LEVERS E4: the hue is not carried over "by default", and only proprietary or restricted faces are replaced. The engine keeps the brand color when the reference is the person's own product (`fit_reference`, engine.py about line 4492). | "Another brand's logo, exact hue or proprietary typeface is not copied." |
| 20 | deliver.interop.paper | plain | unclear | "It takes your colors but has no dark mode yet." This contradicts the engineer voice ("light and dark need separate sets") and the engine, which writes `paper/tokens.<theme>.css` for each theme. | Paper tokens have no modes (L16 finding 3), but dark colors still work as a second set. | "Paper is a design app made of web pages; it takes your colors, but light and dark need two separate sets." |
| 21 | pat.layout.canonical | engineer | unclear (low) | Values such as `= 360dp` sit next to "(DTCG number)", which implies DTCG dimensions in dp. | DTCG `dimension` allows only px and rem (designtokens.org). The engine does not emit `layout.pane.*`. | "360 (dp; exported as px)", and mark the names as proposed. |
| 22 | tok.modes | engineer | unclear (low) | "Outputs equal the product of contexts, so keep axes orthogonal" gives the wrong reason. | The product of contexts is why axes are kept few. Orthogonality matters because overlapping modifiers let array order decide a value (L07 A4). | "Outputs multiply, so keep axes few; keep them orthogonal so no two set the same token." |
| 23 | pat.overlay | plain | unclear (low) | "Or a small note" reads as a tooltip or toast, not a popover. | DC-L08-20: a popover is a lightweight overlay for small scoped tasks. | "...or a small box that opens next to a button." |

Nits not counted: `dial.colorfulness` says extra accents come "above 60" in the designer voice and "from 60" in the engineer voice (levers.json switches at 60). `dial.brandPresence` says "Fluent reuses native patterns about 80% of the time"; DC-L06-14 describes this as Fluent's 80/20 guidance, not a measurement.

## Counts

| | entries | rows |
|---|---|---|
| Entries checked | 70 | |
| Entries with at least one problem | 21 (30%) | 23 |
| Worst severity: wrong | 9 | 9 |
| Worst severity: unsupported | 8 | 10 |
| Worst severity: unclear | 4 | 4 |

- **By voice:** engineer 17 rows, designer 3, plain 2, example 1.
- **By layer (entries with problems / sampled):** found 4/8, core 2/6, use 2/6, prin 3/5, deliver 3/5, tok 2/5, pat 2/5, comp 1/5, ctx 1/5, guard 1/5, builder 0/5, dials 0/5, gov 0/5.

## Verdict

- **Estimated error rate:** 30% of sampled entries (95% CI 21-42%) have at least one problem. Weighted by layer size, about 37% ± 15% of all 393 entries do. About 13% of sampled entries (95% CI 7-23%), or about 17% weighted, contain a statement that is wrong.
- **Plain and designer voices are close to shippable.** Only 5 rows fall there, and most are overstatements. Every dial entry and every `use` command, flag and file path matches `levers.json` and `engine.py`. Every WCAG criterion and level, DTCG type fact and platform number I checked was correct, and I found no invented numbers.
- **The engineer voice is not ready to ship.** People will trust it as the "Code:" name, and roughly 1 in 5 sampled engineer voices (15 of 70) points to a token name or feature that the generated system does not have.

## Patterns

1. **Engineer voices use research-card token names instead of the engine's names.** Many of these names are `[inferred]` in the cards: status colors, state colors, icon status colors, disabled opacity, nested radius, style preset and grouping tokens (8 of 70 entries). A reader searching their generated `tokens/` for these names will not find them.
2. **Planned or `[inferred]` features are described in the present tense as current behavior.** Examples are lint export, reading-grade lint, the platform resolver modifier, haptic string tokens, `layout.margin.*`, and code syntax from `get_variable_defs` (7 entries). The spec often plans these features, but the engine does not build them yet.
3. **Illustrative names for ungenerated blocks are not marked.** `grid.*`, `layout.pane.*`, `layout.safe.extra`, `nav.*` and `vehicle.*` appear with "such as". I did not count them, but a reader cannot tell a real name from a proposed one. Mark them, for example "(proposed)".
4. **External facts are reliable.** Standards, platform numbers, dial bands and M3, WCAG and DTCG details all verified. The errors are internal naming and tense, not facts about the world.
5. **One inherited source error.** The roundness example in `use.od-line` repeats a mistake from `references/rules.md` section 9, so fixing only the glossary would leave the skill wrong.
6. **Required fields are missing.** No entry has `designer_says` or `code_name`, which `THREE-VOICES.md` requires for the first-mention short line. `check_glossary.py` limits their length but does not require them.

## Recommended fix pass

1. Run `engine.py sketch` in a temporary directory and collect every emitted token path.
2. Flag every dotted token path in an engineer voice that is not in that set. Rename it to the emitted name, or mark it "(proposed)".
3. Rewrite present-tense feature claims that `engine.py` does not implement as "planned (spec x.y)".
4. Fix `references/rules.md` section 9 along with row 18.
5. Add `designer_says` and `code_name`, taking `code_name` from the emitted token set.
