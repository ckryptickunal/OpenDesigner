# Glossary verification, second pass (fresh-context sample audit)

Checked on 2026-09-23 against `synthesis/glossary.json` (393 entries) after the first fix pass, by a verifier that neither wrote nor fixed the glossary. Nothing in `glossary.json` or the shards was edited.

**Result in one line:** 21 of 60 sampled entries (35%, 95% CI 24-48%) still have a problem. The token-name errors the first pass found are gone, but the same two failure modes now show up in names the checker cannot see (config and metadata paths such as `system.platforms`, `principles[]`, `$extensions.builder.feedback`, `layout.*`) and in planned features written in the present tense. **Verdict: ship after the listed fixes**, provided the fixes include the two glossary-wide sweeps below, not only the 21 rows.

## Method

- **Sample:** 60 entries, seed 91, stratified by layer, excluding the 70 ids in `VERIFICATION.md`. Each layer gets 4, except `guard` (only 1 unsampled entry left) and `dials` (3 left). The spare slots go to the largest layers: `found` 10, `core` 7, `use` 6, `comp` 5.
  ```
  python3 -c "import json,random,collections,re; d=json.load(open('synthesis/glossary.json'))
  b=open('synthesis/glossary/VERIFICATION.md').read().split('**Sample ids (70):**')[1].split('**Severity')[0]
  prev={x.strip() for x in re.split(r'[,\n]',b) if x.strip()}; random.seed(91); by=collections.defaultdict(list)
  [by[e['layer']].append(e['id']) for e in d if e['id'] not in prev]
  q={l:min(4,len(by[l])) for l in by}; q.update(found=10, core=7, use=6, comp=5)
  print([i for l in sorted(by) for i in random.sample(sorted(by[l]), q[l])])"
  ```
- **Engine ground truth:** I regenerated the token list myself (every example plus each dial at 0 and 100). It came out identical to `engine-token-paths.txt` (486 paths). I also ran `engine.py init` and `build` in a scratch folder, and I read `state.json`, `decisions.md`, `DESIGN.md`, `opendesigner.meta.json`, the resolver, and every file in `build/`, plus the example `state.json` files. I read `engine.py` for `resolve_dials`, `log_decision`, `_store`, `cmd_resolve`, `cmd_review`, `cmd_export`, `build_motion` and `render_design_md`, and checked `assets/templates/` and `show.py`.
- **Sources for the designer voice:** each entry's ontology node, every card it cites (`cards.json`), `levers.json`, `research/L13`, `L17` and `L18`, and `OPENDESIGNER-SPEC.md` sections 6.3-6.4 and 7.1-7.8.
- **Live checks (all correct):** MCP's current version is 2026-07-28 (modelcontextprotocol.io). Figma allows 5,000 variables per collection (help.figma.com). Style Dictionary v5 does not yet support the full 2025.10 format and has no resolver support; Terrazzo's JS API applies resolvers. DTCG issue #429 (springs, keyframes) is open. Storybook's docs toolset needs the component manifest, which only React, `angular-vite` and `vue3-vite` generate. Apple's Body style is 17pt on iOS and 29pt on tvOS (HIG data). The M3 Expressive spatial spring is damping 0.8, stiffness 380 (androidx `ExpressiveMotionTokens.kt`).
- **Mechanical check:** `check_glossary.py synthesis/glossary.json` prints 0 errors, with a plain-voice mean grade of 5.3.
- **Severity** uses the first pass's scale. *Wrong*: contradicts a source or what the engine does. *Unsupported*: states an `[inferred]` or planned item as current fact. *Unclear*: misleading or inconsistent, but not false.

**Sample ids (60):**
builder.canvas, builder.interaction, builder.collab, builder.preview,
comp.inventory, comp.navigation, comp.device-variants, comp.data.avatar, comp.data,
core.shadow, core.spacing-scale, core.mcp, core.design-to-code, core.source-of-truth, core.variant, core.generatable,
ctx.brand.layering, ctx.scope, ctx.platforms.posture, ctx.platforms.devices,
deliver.packaging, deliver.interop.figma, deliver.interop.figma.variables, deliver.pipeline,
dial.depth, dial.energy, dial.density,
found.content, found.icon, found.icon.source, found.shape.radius, found.icon.platform, found.space.scale, found.type.typeface.personality, found.motion, found.type.scale, found.type.responsive,
gov.change.deprecation, gov.change, gov, gov.docs,
guard.critique,
pat.layout, pat.layout.shell, pat.feedback, pat.feedback.messaging,
prin.ux.ethics, prin.design, prin.ux.timing, prin.ux.laws,
tok.tiers, tok.types.extensions, tok.types.layout, tok.themes.generator,
use.status-supersedes, use.file-tokens-folder, use.cmd-resolve, use.status-auto-default, use.file-state, use.template

## Problems found (21 rows in 21 entries)

"Short line" means the error is repeated in `code_name` or `designer_says`.

| # | id | field | severity | problem | evidence | fix |
|---|---|---|---|---|---|---|
| 1 | ctx.scope | engineer, code_name | wrong | "Stored as metadata system.platforms ... and system.frameworks. These fields decide which exporters run." | The engine has no `system.*` keys. Platforms live in `raw.platforms`, and scope in `context.scope {in, out}` (`default_state`). `build` and `export --format all` always run all seven exporters (`cmd_export`). The text is copied from DC-L11-02's token encoding. | "Stored in state.json as raw.platforms and context.scope. Today build writes every export (CSS, Tailwind, Figma, Paper, Swift, Compose, DTCG) regardless." code_name: `raw.platforms, context.scope`. |
| 2 | prin.design | engineer, code_name | wrong | "Stored as ordered records, principles[] {name, statement, doExample, dontExample}, with beats relationships; keywords can map to suggested token presets." | `state.principles` is an ordered list of plain strings (all three `examples/*/state.json`). DESIGN.md prints them numbered, with "the higher-ranked principle wins". No record fields, `beats` or keyword-to-preset mapping exist. The ontology marks the record shape `[inferred]`. | "Not tokens: state.principles is an ordered list of statements; order is rank, and DESIGN.md and PRODUCT.md print them as tie-breakers." |
| 3 | guard.critique | engineer, code_name | wrong | "$extensions.builder.feedback = coach, strict ... Strict blocks export on hard failures." | The engine has no feedback mode. Its extension namespace is `$extensions.opendesigner`. Nothing blocks export: `review --strict` only exits 1 when it finds hard-coded values. DC-L15-11 marks the key `[inferred]`. The first pass fixed the same pattern in `prin.visual.style`. | "Planned (Q-pref-01, spec 6.4): a coach or strict setting. Today validate reports errors and review --strict fails on hard-coded values." Mark the key "(proposed)". |
| 4 | gov | engineer, code_name | wrong (minor) | "Stored as builder metadata and records such as governance.teamModel, decisions[], component.status and package.version." | State has `context.team` (free text), `components.inventory` and the `decisions.md` log. It has no `governance.*`, `component.status` or `package.version`, and decisions are not an array. | "No tokens: team notes in context.team, the decision log in decisions.md, the component list in components.inventory; status and versioning fields are proposed." |
| 5 | deliver.interop.figma.variables | engineer | wrong (minor) | "Collections: Primitives (hidden), Semantic color (light, dark, optional high contrast), Semantic dimension, Motion." | `build/figma/variables.json` writes `Primitives` (hidden), `Color` (Light, Dark), `Density` (Spacious, Comfortable, Compact), `Motion` (Standard, Reduced) and `Tokens` (one mode). No high-contrast mode is generated. The quoted names are the spec 7.6 plan. | Use the emitted names: "Primitives (hidden), Color (Light, Dark), Density, Motion (Standard, Reduced), Tokens." |
| 6 | found.shape.radius | designer, designer_says, example | wrong (minor) | "Builder scale: 0, 2, 4, 6, 8, 12, 16, 24, full; 6px controls." | Matches neither the card nor the engine. DC-L04-01's scale has no 6. The engine emits radius.0 to radius.32 plus full, and roundness 50 (the default) gives radius.control = 8px and radius.container = 12px (levers.json band 48-60). It also contradicts this entry's own engineer voice. | "Research default 6px controls (DC-L09-01); OpenDesigner's default is 8px controls and 12px containers at Roundness 50." Example: 8px buttons in 12px cards. |
| 7 | ctx.platforms.devices | engineer, code_name | unsupported | "A resolver context modifier (handheld \| wrist \| desk \| ...)" in the present tense. | The generated resolver has only `theme`, `density` and `motion` modifiers. DC-L14-01 marks this `[inferred]`. The first pass fixed the same claim in `ctx.platforms`. | "Planned, not generated: a device-class context modifier, kept separate from platform..." code_name: add "(planned)". |
| 8 | ctx.platforms.posture | engineer, code_name | unsupported | "A system-level setting ... Native-first maps color.text.primary to label on iOS and onSurface on Android; brand-first emits literals." | State has no posture setting. The Swift and Compose exports write literal colors (`textPrimary = dsColor(0x242424, 0xE9E9E9)`). DC-L10-02 marks the mapping `[inferred]`. | "Not built: exports emit literal values today; mapping semantic roles to platform colors (label, onSurface) is planned." |
| 9 | prin.ux.timing | engineer, code_name | unsupported | "Ships as duration tokens like feedback.acknowledge.max = 50ms." | No `feedback.*` token is generated. `pat.feedback` says the opposite: "Duration threshold tokens are not generated yet." DC-L13-01 marks the names `[inferred]`. | "Could ship as duration tokens, such as feedback.acknowledge.max (proposed) = 50ms; not generated yet." |
| 10 | prin.ux.ethics | engineer; also designer, plain | unsupported | Engineer: "Lint rules live in $extensions or config". Designer: "which the builder detects". Plain: "which ones get caught for you". | No deceptive-pattern lint exists. `guardrails.md` states "no pre-checked consent" as a rule for the agent, and Q-pattern-05 offers "lint errors" as an option. DC-L13-15 calls the implementation `[inferred]`. | Engineer: "Planned lint (DC-L13-15); today guardrails.md forbids pre-checked consent." Designer and plain: "which ones can be checked automatically". |
| 11 | tok.types.layout | engineer, code_name | unsupported | Names `layout.grid.columns`, `layout.gutter` and `layout.margin` as the encoding, with no "(proposed)". | The engine emits no `layout.*` group. The checker misses this because `layout` is not in its `TOKEN_ROOTS`. The first pass fixed `layout.margin.compact` in `core.margin`. | Add "(proposed)" to each name and "not generated yet". |
| 12 | builder.collab | engineer, code_name | unsupported (low) | "Version 1 keeps state in the URL and git." | Version 1 keeps state in `opendesigner/state.json` and `decisions.md` (spec 7.1, engine). A URL only carries a template's display payload (`#data=`). "URL and git" is DC-L16-11's `[inferred]` default. | "Version 1 keeps state in files in your repo (state.json, decisions.md), so git gives history." |
| 13 | found.icon | engineer, code_name | unsupported (low) | "Glyphs are SVG assets listed in a manifest." | The engine writes no icon manifest, and the ontology says the builder still "needs its own asset-reference convention". Custom icons go through the `H-icons` hook. | "Glyphs are SVG assets (an icon manifest is proposed)..." Drop "SVG manifest" from code_name. |
| 14 | gov.change.deprecation | engineer, code_name | unsupported (low) | "component.deprecated {since, removeIn, replacement}" given as a real record. | There is no component record in state. Only `$deprecated` is real DTCG, and the engine does not emit it yet. | Mark it "(proposed)". |
| 15 | prin.ux.laws | engineer | unsupported (low) | "The UI shows the grade beside every rule." | There is no such UI. The ontology default is `[inferred]`, and no skill file shows the grades. | "Planned: show the grade beside every rule." |
| 16 | core.variant | designer | unsupported (low) | "More than one [primary] is a lint warning." | Spec 6.4 plans this warning. `engine.py review` checks only hard-coded values, and `validate` checks tokens, not views. | "More than one is flagged as a warning (planned lint, spec 6.4)", or "keep one primary per view". |
| 17 | deliver.packaging | engineer, code_name | unsupported (low) | Lists "the shadcn variable contract" among the outputs. | The engine emits CSS custom properties and a Tailwind `@theme inline`, but no shadcn variables (`--background`, `--primary` and so on). The card default is a recommendation, not the engine's behavior. | "Emits CSS variables and Tailwind @theme today; a shadcn variable map is planned." |
| 18 | found.space.scale | designer, designer_says vs engineer, code_name | unclear (low) | Designer: "12-15 steps from 0 to 80 ... above 8px, steps differ by 25% or more". Engineer: "space.0 to space.96". | The engine's default ladder has 15 steps and ends at 96. The quoted Atlassian set breaks its own 25% rule (20 to 24 and 40 to 48 are 20% steps). DC-L03-02 says "at least about 25%" as a target. | "About 15 steps from 0 to 96; above 8px, aim for steps about 25% apart." designer_says: "spacing scale, 0 to 96". |
| 19 | core.spacing-scale | designer, example vs engineer | unclear (low) | Designer: "about 14 steps from 0 to 80". Example ends at 80. Engineer: "space.0 to space.96". | Same mismatch as row 18. The engine default adds 96. | Say "0 to 96" in the designer voice and the example, or note that 96 is OpenDesigner's extra step. |
| 20 | gov.docs | engineer, code_name | unclear (low) | "Docs pages generate from the same data model as the tokens, plus llms.txt or an MCP server" reads as current behavior. | OpenDesigner generates DESIGN.md. The component doc pages (spec 7.8) and llms.txt are not built. DC-L11-17 marks the idea `[inferred]`. | "OpenDesigner generates DESIGN.md from the same data; component pages and llms.txt are planned." |
| 21 | use.status-auto-default | engineer | unclear (low) | "init logs D-0001 this way; logged ones appear in DESIGN.md Open Items." | D-0001 has no value, so `_decisions` skips it and it never appears in Open Items. Only auto_default entries that carry a value appear, and unlogged defaults are not listed. | "init logs D-0001 this way; an auto_default decision logged with a value is listed in DESIGN.md Open Items." |

**Nits, not counted:**
- `builder.preview` says controls "re-render within one frame while dragging", and `builder.canvas` says native outputs have "their own preview images". Both are card aspirations in the present tense. The first pass also left builder entries alone.
- `gov.change` gives `package.version per artifact` as a code name without saying nothing is versioned today.
- `comp.inventory` says "about 25 core components". The engine's default inventory has 22, and it includes toast and skeleton, which the research counts as extended.
- `ctx.brand.layering`'s plain voice says "ads" for marketing surfaces.

## Counts

| | entries | share of 60 |
|---|---|---|
| Entries with at least one problem | 21 | 35% |
| Worst severity: wrong | 6 | 10% |
| Worst severity: unsupported | 11 | 18% |
| Worst severity: unclear | 4 | 7% |

- **By voice:** engineer 17 rows, designer 4 (rows 6, 16, 18, 19), plus plain in row 10. The short line repeats the error in 15 rows.
- **By layer (entries with problems / sampled):** prin 4/4, ctx 3/4, gov 3/4, guard 1/1, deliver 2/4, found 3/10, core 2/7, builder 1/4, tok 1/4, use 1/6, comp 0/5, pat 0/4, dials 0/3.
- **What is clean:** every name under the checker's token roots exists in the engine list or is marked "(proposed)". Every dial band, formula and default matches `levers.json` and the engine. Every `use` command, flag, file and state key checked is right. Every WCAG, DTCG, Apple, Material, Figma, MCP and Storybook fact checked is correct. I found no invented numbers.

## Estimated error rate

- **Raw:** 21/60 = **35%** (Wilson 95% CI 24-48%). Wrong only: 6/60 = 10% (CI 5-20%).
- **Weighted by layer size** over the 323 entries the first pass did not sample: **30% ± 13%** have a problem, and **7% ± 7%** contain a wrong statement.
- **Whole glossary:** all 23 first-pass rows are fixed in `glossary.json`. If those 70 entries are now clean, about **25%** of all 393 entries (roughly 95) still have a problem, and about **6%** (roughly 23) contain a wrong statement.

## Comparison with the first pass

| | First pass (seed 23, n=70, before fixes) | Second pass (seed 91, n=60, after fixes) |
|---|---|---|
| Entries with a problem, raw | 30% (CI 21-42%) | 35% (CI 24-48%) |
| Weighted by layer | 37% ± 15% | 30% ± 13% (unsampled 323) |
| Wrong, raw | 13% (CI 7-23%) | 10% (CI 5-20%) |
| Main failure | research token names in place of the engine's names; planned features in the present tense | config and metadata names outside the checker's reach; planned features in the present tense |
| Layers with the most problems | found, prin, deliver | prin, ctx, gov, guard |

- **The token-name fix worked.** The first pass found 8 of 70 entries with wrong token names. I found none in the checked roots, because `check_glossary.py` now blocks them.
- **The overall rate did not drop measurably.** The intervals overlap almost completely. The fix pass repaired the 21 flagged entries and the checkable token paths, but the other two patterns were never swept across the population. They now dominate: 13 of my 21 rows are unbuilt names or features stated as current.
- **The problems moved to layers without tokens.** In ctx, prin, gov and guard, the engineer voice describes storage (`system.*`, `governance.*`, `component.*`, `principles[]`, `$extensions.builder.*`, `feedback.*`, `layout.*`) that the checker never examines, because those roots are not in its `TOKEN_ROOTS`.
- **One recommended fix was not applied.** `skills/opendesigner/references/rules.md` line 96 still reads `OD:set dials.roundness=45 --why "a bit softer"`. The first pass showed 45 makes corners sharper (6px against the default 8px).

## Leads outside the sample (not counted)

A scan of the whole glossary for dotted names in the engineer voice or code_name that are unmarked and not found in the engine's tokens, state keys, levers parameters or ontology ids flags these entries beyond my sample. Each needs a check:
- `core.grid` and `prin.visual.composition` (`grid.*`)
- `found.layout` (`grid.*`, `layout.*`, `breakpoint.*`)
- `found.layout.grid` (`grid.gutter.*`, `grid.margin.*` unmarked)
- `ctx.strategy` (`system.origin`, `system.base`, `governance.posture`)
- `ctx.inventory` (`audit.findings[]`)
- `gov.team`, `gov.contribution`, `gov.lifecycle`, `gov.measure` and `gov.docs.component-page` (`governance.*`, `component.*`, `team.roles`, `system.maturityStage`)
- `gov.decisions` (`decisions[]`)
- `guard.safety` (`vehicle.*`)
- `ctx.brand.personality` (`$extensions.brand.personality`)
- `prin.visual.hierarchy` (`$extensions.builder.hierarchy`)
- `deliver.interchange`, which gives the file name `semantic.dark.tokens.json`; the engine writes `semantic.color.dark.tokens.json`.

## Verdict: ship after the listed fixes

The plain and designer voices are close to shippable: 5 of 21 rows touch them. The external facts are reliable. The engineer voice is not yet trustworthy as the "Code:" line, because about 1 in 4 of its entries names storage or behavior that does not exist. The fixes are well defined:

1. Apply the 21 row fixes above.
2. **Extend `check_glossary.py`** so that any dotted name in the engineer voice or code_name must be a generated token, a key in `state.json`, a parameter in `opendesigner.meta.json` or `levers.json`, a real file name, or carry "(proposed)" or "(planned)". Then fix everything it flags, starting with the 16 lead entries above.
3. **Sweep the present tense** in the ctx, prin, gov, guard and builder layers (64 entries). Rewrite any feature `engine.py` does not implement as planned, and cite the spec section.
4. Fix `references/rules.md` line 96.
5. Draw a fresh 40-entry sample (a new seed, excluding both samples) and check it. Ship when entries with a problem fall below about 10% and wrong statements below 3%.

Fixing only the 21 rows is not enough. The first pass showed that row fixes leave the rest of the population where it was.
