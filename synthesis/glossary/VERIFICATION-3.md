# Glossary verification, third pass (fresh-context sample audit)

Checked on 2026-09-24 against `synthesis/glossary.json` (393 entries), after the second fix pass and the engine sweep. I did not write or fix the glossary. Nothing in `glossary.json` or the shards was edited.

**Result in one line:** 8 of 60 sampled entries (13%, 95% CI 7-24%) have a problem, and 3 (5%, CI 2-14%) contain a wrong statement. That is well below the first two passes (30% and 35%). The token-name and config-path failures those passes found are gone from this sample. What remains is smaller: two entries contradict the engine on how hover and press colors are made, a few planned items are still written as current, and a research default is presented as OpenDesigner's default. **Verdict: ship after the listed fixes** (8 rows plus 4 lead entries, all small).

## Method

- **Sample:** 60 entries, seed 457, stratified by layer, excluding the 130 ids sampled in `VERIFICATION.md` and `VERIFICATION-2.md`. `guard` and `dials` have no unsampled entries left, and `builder` has 3, so all 3 are taken. Every other layer gets 4. The 17 spare slots go to the largest layers: `found` 13, `core` 9, `use` 6, `comp` 5.
  ```
  python3 -c "import json,random,collections,re; d=json.load(open('synthesis/glossary.json'))
  b=open('synthesis/glossary/VERIFICATION.md').read().split('**Sample ids (70):**')[1].split('**Severity')[0]
  b2=open('synthesis/glossary/VERIFICATION-2.md').read().split('**Sample ids (60):**')[1].split('## Problems')[0]
  prev={x.strip() for x in re.split(r'[,\n]',b+','+b2) if x.strip()}; random.seed(457); by=collections.defaultdict(list)
  [by[e['layer']].append(e['id']) for e in d if e['id'] not in prev]
  q={l:min(4,len(by[l])) for l in by}; q.update(found=13, core=9, use=6, comp=5)
  print([i for l in sorted(by) for i in random.sample(sorted(by[l]), q[l])])"
  ```
- **Engine ground truth:** I ran `engine.py init` and `build` in a scratch folder and read `state.json`, every file in `tokens/` and `build/` (CSS, Figma `variables.json` with its code syntax and text styles, Swift), `DESIGN.md` and `opendesigner.meta.json` (all 53 lever parameters). I resolved every token and grouped them by DTCG type. Every dotted name in the sampled engineer voices and code names was checked against `engine-token-paths.txt`, `engine-truth.json` and the meta parameters. I read the engine code for `build_color_semantic`, `build_type_scale`, `build_typography`, `build_shape`, `build_elevation`, `build_motion`, `build_motion_context`, `contrast_pairs`, `validate_files`, `answer_effects`, `cmd_set`, `_store`, `log_decision`, `cmd_intake`, `fit_reference`, `cmd_sketch`, `cmd_feedback`, `code_syntax`, `export_figma`, `render_design_md` (Components, Open Items, For Agents) and `main`. I also read `SKILL.md` for all four skills, `css_scan.py`, `questions.json`, `pacing.json`, `data/hooks.json`, `levers.json` and the `#copy` code in all eight templates.
- **Designer-voice sources:** each entry's ontology node and every cited card (`cards.json`), plus `research/L08-component-catalog.md`, `L11`, `L13`, `L15`, `L17`, the L02 and L13 traces, and `OPENDESIGNER-SPEC.md` sections 6.4, 6.6, 7.8 and 10 to 12.
- **Live checks (all correct):** NN/g's error-message article has 13 guideline subheadings (Neusesser and Sunwall, 14 May 2023). DTCG 2025.10 has 13 types, `$type` can be inherited, the transition composite is `{duration, delay, timingFunction}`, and there is no string type (designtokens.org). Penpot imports and exports DTCG tokens, reads `$themes.json` and `$metadata.json`, and has multidimensional themes (help.penpot.app). `HapticFeedbackConstants.CONFIRM` exists from API 30 (developer.android.com).
- **Mechanical check:** `python3 tools/check_glossary.py synthesis/glossary.json` prints 0 errors, with a plain-voice mean grade of 5.3.
- **Severity** uses the scale of the first two passes. *Wrong*: contradicts a source or what the engine does. *Unsupported*: states an `[inferred]` or planned item as current fact, or has no source. *Unclear*: misleading or inconsistent, but not false.

**Sample ids (60):**
builder.hooks, builder.intake, builder.review,
comp.states.loading, comp.overlay, comp, comp.action.button, comp.states,
core.state, core.type-scale, core.design-token, core.padding, core.wcag, core.corner-radius, core.designer-owned, core.letter-spacing, core.sketch-level,
ctx.platforms.sharing, ctx.inventory, ctx.brand.personality, ctx.platforms.os-floor,
deliver.interop.figma.code-syntax, deliver.interop, deliver.ai, deliver.interop.penpot,
found.shape.geometry, found.type.roles, found.elevation.surfaces, found.color.modes, found.layout.grid, found.space.density.context, found.space.density, found.color.ramp, found.color.modes.dark, found.sensory.sound, found.sensory.haptics, found.elevation.materials, found.space.whitespace,
gov.docs.component-page, gov.process, gov.lifecycle, gov.adoption,
pat.motion, pat.destructive, pat.feedback.errors, pat.onboarding,
prin.visual.signifiers, prin.ux.rules, prin.visual.hierarchy, prin.ux.inclusion,
tok, tok.types, tok.naming.primitives, tok.types.typography,
use.interview, use.file-feedback, use.copy-my-choice, use.cmd-set, use.status-chosen, use.cmd-validate

## Problems found (8 rows in 8 entries)

| # | id | field | severity | problem | evidence | fix |
|---|---|---|---|---|---|---|
| 1 | comp.states | designer | wrong | "Hover and press use overlays; selected and error get explicit colors." OpenDesigner makes hover and press colors by stepping along the ramp. Overlays are only the fallback for colors unknown at design time. The entry's own engineer voice names a step token (`color.bg.action.primaryHover`), so the two voices contradict each other. | `engine.py` 1100 and 1138: `boldHover` is accent step 10 (+1 step) and `primaryHover` is a ramp step. The DESIGN.md generator (line 3886) writes "Hover moves one step, pressed two (DC-L01-17). Where a color is unknown at design time, use the state opacities." The overlay rule is DC-L08-09's `[inferred]` default. DC-L01-17's default, which the engine follows, is the step shift. `found.color.states` already states this correctly. | "Hover and press step one and two shades along the ramp; overlays are the fallback for colors unknown in advance. Selected and error get their own colors." |
| 2 | core.state | engineer | wrong (minor) | "Hover and press use a state-layer overlay (M3: 8% and 10%)" is the same error in the engineer voice. | Same evidence as row 1. `opacity.state.hover` = 0.08 and `.pressed` = 0.10 are emitted, but only as the fallback. | "Hover and press shift one and two ramp steps (color.bg.accent.boldHover, boldPressed); opacity.state.hover = 0.08 and .pressed = 0.10 are overlays for unknown colors (M3 values)." |
| 3 | tok.types.typography | engineer | wrong (minor) | "Atomic fontFamily, dimension, fontWeight and number primitives." OpenDesigner emits no number-typed type primitive. Line heights are dimension tokens in px, and the composite carries a raw number multiplier. | In the resolved default build, the only `number` tokens are 6 opacities. `font.lineHeight.*` are `dimension`. `text.body.md` has `"lineHeight": 1.4286` inline (`engine.py` 1359). | "Atomic fontFamily, fontWeight and dimension primitives (font.size.*, font.lineHeight.* in px) plus typography composites such as text.body.md, whose lineHeight is a number multiplier." |
| 4 | found.shape.geometry | engineer, code_name | unsupported | "Web adds corner-shape: squircle over a border-radius fallback" reads as current output, and the code name lists `corner-shape: squircle`. The engine emits no corner-shape anywhere. The research default for the web is circular arcs, with squircle only as optional progressive enhancement. | `grep corner-shape engine.py` finds nothing. DC-L04-04 says corner-shape is "experimental and not Baseline as of 2026-08-27" and gives the default "Use circular arcs on the web today". The DTCG encoding is `[inferred]`. | "... On the web, corner-shape: squircle (experimental) can be layered over border-radius; OpenDesigner does not emit it." code_name: "radius.nested; corner-shape (not emitted)". |
| 5 | deliver.ai | engineer | unsupported (low) | "A shadcn registry, llms.txt and an MCP server are planned." Only the MCP server is planned. | The spec plans a Phase 2 remote MCP server (`OPENDESIGNER-SPEC.md` line 754). llms.txt for a person's system appears in no spec, roadmap or decision file. The shadcn registry appears only as an open question whose default is "specs, docs and previews", with no component code (spec line 800). | "An MCP server is planned (spec Phase 2); llms.txt and a shadcn registry are options from the research, not planned." |
| 6 | found.color.modes.dark | designer | unclear (low) | "The base surface is near-black (about #121212), slightly tinted" is DC-L01-19's research band, stated as if OpenDesigner does it. OpenDesigner's default dark base surface is #1D1D1D (neutral step 2), and it is untinted at Warmth 50. | `engine.py` 1058 sets dark `base` to neutral step 2. The default build writes `surfaceBase = dsColor(0xF4F4F4, 0x1D1D1D)`. Only step 1 (sunken, #151515) sits in the #121212-#1A1A1A band (`DARK_STEP1_Y`, line 629). `color.neutral.tint.oklch` has c = 0 at Warmth 50. | "The base surface is near-black (OpenDesigner: #1D1D1D, tinted only when Warmth moves off 50); accents go lighter in dark." |
| 7 | pat.motion | engineer, code_name | unclear (low) | "Each pattern is a DTCG transition composite" suggests OpenDesigner emits the four named patterns and a stagger token. It does not. Its transitions are named by role (`motion.transition.feedback`, `enter`, `exit`, `move`, `expand`), and no stagger token exists. | `build_motion_context` (`engine.py` 1679-1705). DC-L04-23's default ("Ship 4 named transitions + a stagger token") is research, and its View Transitions note is `[inferred]`. | "OpenDesigner emits role-named transitions (motion.transition.enter, exit, move, expand, feedback); the four patterns and a stagger token (proposed) would be transition composites too. Reduced motion swaps travel for a fade." |
| 8 | prin.visual.hierarchy | code_name | unclear (low) | "maxPrimaryPerView (proposed)" marks as proposed a parameter that exists. Only the lint is planned. `core.visual-hierarchy` names the same parameter correctly, so the two entries disagree. | `emphasis.maxPrimaryPerView` = 1 is a lever parameter in `levers.json` (Expression, DC-L15-03) and is written to `opendesigner.meta.json`. `core.visual-hierarchy` says "emphasis.maxPrimaryPerView = 1 (recorded, not checked yet)". | code_name: "type.ratio, type.weightCount, emphasis.maxPrimaryPerView (lint planned)". |

**Nits, not counted:**
- `found.sensory.haptics`: `.success` belongs to `UINotificationFeedbackGenerator`, a subclass of `UIFeedbackGenerator`. The entry names the superclass.
- `prin.ux.rules`: the designer voice lists "a blocking error" as a rule level. Today `validate` exits 1 on errors, but `build` writes the exports before it validates, so nothing is blocked.
- `found.color.modes`: designer_says is "light, dark and high-contrast modes". OpenDesigner generates only light and dark (DESIGN.md: "High-contrast themes are not generated"). As a name designers use, this is acceptable.
- `deliver.interop.penpot`: "the shared design file" in the plain voice is vague. "The shared file of design choices" is clearer.
- `core.designer-owned` follows L17 (7 designer-owned nodes). `synthesis/ontology.json` labels 38 nodes `designer-owned`, because it folds in owner-input decisions. The glossary is right, but the two data files use the term differently.

## Counts

| | entries | share of 60 |
|---|---|---|
| Entries with at least one problem | 8 | 13% |
| Worst severity: wrong | 3 | 5% |
| Worst severity: unsupported | 2 | 3% |
| Worst severity: unclear | 3 | 5% |

- **By voice:** engineer or code_name 6 rows, designer 2. None is in the plain voice. The short line repeats the error in rows 4, 7 and 8.
- **By layer (entries with problems / sampled):** comp 1/5, core 1/9, deliver 1/4, found 2/13, pat 1/4, prin 1/4, tok 1/4, builder 0/3, ctx 0/4, gov 0/4, use 0/6.
- **What is clean:** every token name in the sample exists in `engine-token-paths.txt` or is marked "(proposed)". Every state key, question id, lever parameter, command, flag and file path exists and behaves as described: hook statuses, the brand-slider-to-macro logic, intake confidence, the `set` and lock rules, the `feedback` format, the `#copy` button in all eight templates, validate's checks and exit codes, the Figma code syntax, and the component status default. No config or metadata path is invented, which was the second pass's main finding. Every WCAG, DTCG, Figma, Penpot, Android, Apple and NN/g fact I checked is correct. I found no invented numbers.

## Estimated error rate

- **Raw:** 8/60 = **13%** (Wilson 95% CI 7-24%). Wrong only: 3/60 = **5%** (CI 2-14%). Wrong or unsupported: 5/60 = 8% (CI 4-18%).
- **Weighted by layer size** over the 263 entries neither earlier pass sampled: **14% ± 10%** have a problem, and **5% ± 5%** contain a wrong statement.
- **Whole glossary:** if the 130 entries from passes 1 and 2 are now clean (their rows were fixed), about **9%** of all 393 entries (roughly 36) still have a problem, and about **3%** (roughly 12) contain a wrong statement. This meets the second pass's ship bar (about 10% and 3%) at the whole-glossary level, but only on that assumption. On the unsampled entries alone, the point estimates are still just above the bar, and the intervals include it.

## Comparison across the three passes

| | Pass 1 (seed 23, n=70) | Pass 2 (seed 91, n=60) | Pass 3 (seed 457, n=60) |
|---|---|---|---|
| State of the glossary | before any fixes | after the row fixes and the token-name checker | after the pass 2 fixes and the engine sweep |
| Entries with a problem, raw | 30% (CI 21-42%) | 35% (CI 24-48%) | **13% (CI 7-24%)** |
| Weighted by layer | 37% ± 15% | 30% ± 13% | **14% ± 10%** |
| Wrong, raw | 13% (CI 7-23%) | 10% (CI 5-20%) | **5% (CI 2-14%)** |
| Problems in the plain voice | 2 | 1 | 0 |
| Main failure | research token names in place of the engine's; planned features in the present tense | invented config and metadata paths; planned features in the present tense | engine-contradicting state method (2 entries); a few leftover planned-as-current claims |
| Layers with the most problems | found, prin, deliver | prin, ctx, gov, guard | spread thin (at most 1 per layer, except found with 2) |

- **The sweep worked.** Pass 3's interval (7-24%) only touches pass 2's (24-48%) at one end, so the drop from 35% to 13% is very unlikely to be sampling noise. In the ctx, gov and prin layers, pass 2 found problems in 10 of 12 entries. This pass finds 1 in 12.
- **The remaining errors are cross-entry consistency, not invention.** Rows 1, 2 and 8 contradict other glossary entries that are correct (`found.color.states`, `core.visual-hierarchy`). An entry-by-entry sweep cannot catch this. A check across entries that share a concept can.
- **One earlier fix introduced an error.** Pass 2 suggested "component pages and llms.txt are planned" for `gov.docs`. llms.txt is not planned, and the same claim now appears in `deliver.ai` (row 5) and nearby entries. Suggested fixes need the same source check as the text they replace.

## Leads outside the sample (not counted)

A scan of the whole glossary for the four patterns above found these. Each needs a check:
- `gov.docs` ("llms.txt are planned"), `deliver.channels` ("A shadcn registry item ... planned") and `deliver.packaging` ("a shadcn variable map is planned"): no spec or roadmap plans these for a person's system.
- `found.elevation.opacity` gives Material's state-layer numbers. It is correctly attributed, but it should say that OpenDesigner uses step shifts first, to match `found.color.states`.
- Search every entry that describes hover or press for "overlay" or "state layer", and align it with DESIGN.md's rule: step first, overlay for unknown colors.

## Verdict: ship after the listed fixes

The plain voice is shippable as it is (0 problems in 60). The designer voice has 2 problems, and the engineer voice and code names are now trustworthy as the "Code:" line: 6 of 60 entries have a problem there, and none names a token or state key that does not exist. The fixes are small and well defined:

1. Apply the 8 row fixes above.
2. Check the 4 lead entries. Drop the "planned" claims for llms.txt and the shadcn registry unless the spec adopts them.
3. Align every hover and press description with DESIGN.md's step-first rule.
4. Add a consistency check to `check_glossary.py`: when a lever parameter name appears in any entry, require its full name (for example `emphasis.maxPrimaryPerView`), and forbid "(proposed)" on names that exist in `opendesigner.meta.json` params.

No new sample is needed after these fixes. They touch about 12 entries, and none of them changes engine behavior.
