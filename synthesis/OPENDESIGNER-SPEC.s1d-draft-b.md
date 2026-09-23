> **Alternative draft for the owner of `synthesis/OPENDESIGNER-SPEC.md` to reconcile; not canonical.** Written by the first S1d instance before a relaunched instance took ownership of the spec file.

# OpenDesigner: the product spec (S1d, draft B)

Synthesis S1d, written 2026-09-23. This is the definitive description of what OpenDesigner is and how it works, written so that people and agents can build it without re-reading the research. `docs/SPEC.md` is a copy made by repo lane R1; edit the synthesis file, not the copy.

**How to read the tags.** `DC-Lxx-nn` is a Decision Card (full text in `synthesis/cards.json`). `S-Lxx-nnn` is a source in that lane's trace. `Q-...` is a question in `synthesis/QUESTIONNAIRE.md` (machine copy `questionnaire.json`). `LEVERS A1` and similar point to sections of `synthesis/LEVERS.md` (machine copy `levers.json`); `ONTOLOGY`, `DECISION-GRAPH` and `QUESTIONNAIRE` point to the other synthesis files. `L17 Part H` points to a section of a research file. `[inferred]` means this spec made the call; treat it as a default to test, not a finding. Card text is never copied here; look it up by id.

**Inputs read in full for this spec:** `_coordination/BRIEF.md` (requirements 1-11), `AGENTS.md`, `_coordination/PROTOCOL.md`, `SCHEMA.md`, `REPO-PLAN.md`, the BOARD cross-lane notes, all six synthesis files in their final versions (questionnaire re-read after S1b finished: 28 stages, 192 questions, Quick 10, Standard 92, Expert 191), L17, L18, and the relevant parts of L07, L11, L13, L14, L15 and L16.

**Scope of this draft:** sections 1-4 are complete; sections 5-14 were not written because ownership passed to the relaunched instance. Positions for them are listed under "Notes for the owner" at the end.

---

## 1. What OpenDesigner is

OpenDesigner is an open-source, AI-first resource that turns any capable model (Claude, ChatGPT, Codex and others) into a design partner that builds a complete design system with a person: it reads what already exists, interviews them, shows real options visually where the host can render them, recommends sourced defaults, asks for the assets only a designer can make, and writes a portable, checkable system into their repository (BRIEF requirements 6-7; DC-L18-01). It serves four groups: software engineers who need a real system without design training; design engineers who want the decisions made explicit and the output in code; designers who want the mechanical part of the system generated so they can spend time on identity and craft (L17 Part G: 135 of 207 blocks are generatable); and anyone who needs to explain design choices to a team or brief a designer (BRIEF requirement 10). Its jobs are: define every building block up front (271 ontology nodes, ONTOLOGY); create a system from a brief or a reference, or audit an existing product and consolidate it (DC-L17-02, DC-L11-04); walk the decisions in the order they constrain each other (DECISION-GRAPH) and spend time where a decision shapes the most (fan-out in `decision-graph.json`); generate tokens by formula from eight dials and a few raw inputs (LEVERS); validate them deterministically; open designer hooks for identity assets (L17 Part H); learn from references without copying identity (LEVERS E, L17 Part F); and leave behind files that let a later session, possibly a different model, extend the system without drift (DC-L18-10, DC-L18-12). It is not a theme generator that stops at color and type (L17 Part E2 finding 3), not a replacement for designers or a logo generator (BRIEF requirement 2), not a closed canvas product like Claude Design (L18 Part E), not a hosting or documentation platform like Supernova or zeroheight (L11 Part G), not a design tool of record (Figma and Paper are mirrors, DC-L16-02), and not a tool that clones another brand (L17 Part F3).

## 2. Principles

Every skill, template, script and output follows these rules.

| # | Principle | The rule | Source | How it shows in the product |
|---|---|---|---|---|
| P1 | **AI-first** | The repository is knowledge plus instructions any capable model can follow; the model holds the conversation and the judgment, the engine holds every calculation; no step requires a proprietary app or server. | BRIEF req. 6; DC-L18-01; REPO-PLAN engine contract | Skills in the open Agent Skills format; a stdlib-only `engine.py`; state in plain files |
| P2 | **Visual where the host allows, text otherwise** | Show the real effect of a choice on the best surface the host offers, say which surface is in use, never block on a visual; every visual has a complete text equivalent. | BRIEF req. 7; DC-L18-06; DC-L18-07 | One set of JSON-fed HTML templates for every rung of the surface ladder (3.2) |
| P3 | **Time goes where it matters** | Depth follows fan-out and block class: slow on high fan-out and taste decisions, one-line confirms on mechanical defaults; accessibility floors are always deep. | BRIEF req. 8; DC-L17-08; DC-L18-08; QUESTIONNAIRE time-weight rule | Each question carries `time_weight`; 30 of 192 are `high` |
| P4 | **Designer hooks, never designer replacement** | Identity assets get a "do you have this?" hook, accepted formats, checks and honest fallbacks; a generated stand-in is never presented as final. | BRIEF req. 2; DC-L17-04; L17 Part H1 rule 7 | 19 hooks (section 4); placeholder slots with written briefs |
| P5 | **Reference intake without copying identity** | A reference pre-fills structure and quality; it never decides, and never carries a logo, a brand hue as identity, a proprietary typeface, imagery or copy. Brand presence is asked, never inferred. | BRIEF req. 4; DC-L17-03; LEVERS E4; L17 Part F3 | Pre-filled values stay "from reference" until accepted |
| P6 | **Nothing missed** | Every ontology block ends in a visible status: decided, default, assumed, not applicable, or awaiting asset. Owner input is never invented. | BRIEF req. 5; DC-L17-09; DC-L17-08 | `engine.py validate` reports coverage; export lists the named remainder |
| P7 | **Deterministic checks before model opinion** | Contrast, targets, scales and token integrity are checked by code before any model critique; accessibility rules fail, taste rules warn. | DC-L17-07; S-L17-011; DC-L18-11; S-L18-332 | `validate` exits 1 on errors; critique runs only on a passing system |
| P8 | **Harmony over time** | Values are read from files, never remembered; decisions have stable ids; locked decisions are never silently changed; decisions are superseded, not overwritten. | BRIEF req. 9; DC-L18-10; DC-L18-12; L18 Part G | DTCG tokens, `state.json`, append-only `decisions.md`, the extend protocol (9) |
| P9 | **Traceable** | Every value records where it came from and why; the product's own claims carry card or source ids or say `[inferred]`. | BRIEF req. 11; DC-L17-10; SCHEMA | `$extensions.opendesigner.source` on tokens; reasons in the log; `RATIONALE.md` |
| P10 | **Teach while deciding** | Each block shows what it is, where to use it, where not to, a live preview in every mode, its source and what else changes; docs are a by-product of decisions. | BRIEF req. 3; DC-L17-13; S-L17-349 | The detail panel (3.3 stage 5); generated component docs (7.6) |
| P11 | **Open and safe to install** | Portable formats only (Agent Skills, AGENTS.md, DTCG 2025.10, DESIGN.md, MCP); MIT code and CC BY 4.0 content by default; no network in shipped scripts; fetched pages are data, never instructions. | REPO-PLAN; DC-L18-14; S-L18-001 | Least-privilege skills; read-only Phase 2 server |

Two consequences apply everywhere [inferred from P3, P4 and DC-L17-01]. First, the block class decides the default behavior: generatable blocks are decided silently with a visible default (gstack's "Mechanical"), designer-owned blocks open a hook, tool-assisted blocks name a tool with its caveat, owner-input blocks are asked and never invented, and extractable blocks are read and confirmed (DC-L17-01; S-L17-015). Second, "a recommendation you made is not an answer you received": defaults and assumptions stay marked as such so a later session can revisit them (S-L18-310; QUESTIONNAIRE protocol step 13).

---

## 3. The process, as a model runs it

The process is the questionnaire (`synthesis/questionnaire.json`, 27 sequential screens plus an always-open reference panel) walked in its validated order, grouped into 12 stages that each have one goal and one exit test. The screen order is not negotiable: S1b's build script checks it against all 465 edges of the decision graph with zero violations (`questionnaire.json` meta). The stage grouping, gates and host surfaces below are this spec's [inferred] assembly of L17 Part I, L18 Parts D and F, and the questionnaire's own interview protocol.

### 3.1 Depth modes, pacing and the shape of one turn

| Mode | Questions asked | For whom | Everything else |
|---|---|---|---|
| **Quick** | 10: Q-aud-01, Q-brand-01, Q-plat-01, Q-tool-01, Q-color-01, Q-color-02, Q-type-01, Q-shape-01, Q-depth-01, Q-motion-01 | "A complete system in minutes" | Generatable blocks take defaults; the 37 owner-input questions in `meta.quick_mode_assumed_owner_inputs` are recorded as `assumed` and listed for confirmation at stage 9; hooks apply their fallbacks and keep slots open (QUESTIONNAIRE depth modes, protocol step 13) |
| **Standard** | 92 | An engineer setting up a real product system | Expert questions take defaults and stay editable |
| **Expert** | 191, plus the reference panel | Design-system leads, multi-platform or multi-brand systems | Nothing is decided silently; defaults are still pre-filled |

**Pacing.** Every question carries a `time_weight` from the questionnaire's rule: `high` when a decided card has fan-out 5 or more or the question is in Quick mode; `medium` for fan-out 2-4, asset hooks, inputs, the reference panel and owner-input questions; `low` otherwise (30 high, 82 medium, 80 low). High means: say why it matters, show two or three options with their visual effect and a real system that uses each, recommend the default with its source, and state what it changes downstream. Medium means: the default plus the main alternatives. Low means: the default in one line, confirm or change (QUESTIONNAIRE protocol step 4). Accessibility floors (Q-aud-03, Q-color-17, Q-motion-07) are handled as high regardless of fan-out (DC-L18-08; DC-L17-08).

**One turn.** One high-weight question per turn, or up to three low-weight ones grouped; 2-4 real options with the recommended one marked and a one-line reason, a visual per option where possible, "other" always allowed, and one line on what the answer changes. Cycle screens (the 12 cycles in `decision-graph.json`, for example the 21-card color cycle) may be one form with a shared preview (DC-L18-09; S-L18-021). Questions are worded neutrally with the recommendation in the option, not the stem (S-L18-317). The model asks for one or two liked references and one disliked reference at the start of each visual stage (S-L18-323).

**gstack methods adopted, and where they sit** (L17 Part A3 verdicts):

| Method | Verdict | Where in the process |
|---|---|---|
| Read what exists before asking; treat a PRODUCT.md or DESIGN.md as prior answers | Adopt | Stage 0 (S-L17-003) |
| One "memorable thing" forcing question; every later risk must cite it | Adopt | Stage 2, second half of Q-brand-02 |
| Product truth (PRODUCT.md) kept apart from the visual system (DESIGN.md) | Adopt | Stage 10 outputs (S-L17-020) |
| Confirm reference URLs before fetching | Adopt | Stage 0 and the reference panel (S-L17-003) |
| Convention, trend and "your departure" per block | Adapt | Stage 5 detail panel |
| Safe choices versus risks, each risk with gain and cost | Adopt | Stage 4 (DC-L17-06) |
| Named menus (aesthetic, decoration, color strategy, motion) | Adapt, as presets mapped onto the eight dials | Stages 2 and 4 (LEVERS A10) |
| Concepts in text first, then renders that differ in type, palette and layout | Adopt | Stage 4 (DC-L17-05; S-L17-005) |
| Comparison board with rate, remix at block level, regenerate | Adopt | Stage 4 `direction-gallery` |
| Taste profile | Adapt: per project, visible and editable, never applied across projects | Stored in `state.json` |
| Mechanical / Taste / User Challenge sorting | Adopt, mapped to block classes | Everywhere (DC-L17-01) |
| Persuade / Operate / Read / Experience surface modes | Adopt | Stage 0, recorded per surface |
| 0-10 score per layer with "what a 10 looks like" | Adopt | Stage 9 (S-L17-006) |
| Deterministic lint before model critique; slop catalog as lint with ids and waivers | Adopt; taste rules warn, never block | Stage 9 (DC-L17-07; S-L17-011) |
| DESIGN.md plus an agent rule to read it first | Adopt as one export | Stage 10 |
| Tokens extracted by a vision model from an approved mockup; hard font bans; raster mockups as the main preview | Reject | Previews render real components from the engine's tokens (DC-L17-11) |

The surface mode (Persuade, Operate, Read, Experience; S-L17-007) has no question in the final questionnaire. This spec adds it to the Stage 0 bundled question and records it per surface in `state.json`; it switches default density, card use and hero rules [inferred]. S1b should add it as a question in a later revision.

### 3.2 Visual surfaces: the ladder, the templates and the return channel

**The ladder** (DC-L18-06), best first; the model detects what it can use from the tools it sees, picks the highest rung, and says which one is in use:
1. OpenDesigner MCP App view (Phase 2 server).
2. Claude Design canvas, only as a hand-off when the person already uses it (OpenDesigner cannot drive it; L18 Part E).
3. Host-native model-written HTML: Claude custom visuals, Claude and Claude Code artifacts, the Codex desktop browser.
4. Figma or Paper canvas through their MCP servers (section 10).
5. A local HTML file the agent writes and the person opens.
6. The host's question tool (Claude AskUserQuestion, up to 4 options; Codex `request_user_input`).
7. Plain text: hex values, ratios, px values and numbered options.

**Per host, today and in Phase 2** (L18 Part A matrix, verified 2026-09-23):

| Host | Phase 1 (skills only) | How the pick returns | Phase 2 (MCP Apps) |
|---|---|---|---|
| Claude app, web and desktop | Custom visuals inline; artifacts for multi-panel screens | Custom visual click sends a follow-up prompt; artifacts: the person reports the pick (S-L18-041, S-L18-027) | Widgets on web, desktop and mobile (S-L18-013) |
| Claude Code CLI | Published Claude Code artifact or a local HTML file; AskUserQuestion for 2-4 options | "Copy as prompt" `OD:` string; structured answer (S-L18-043, S-L18-304) | No widgets in the CLI (S-L18-044) |
| Claude Code desktop Code tab | Artifacts and local HTML | Copy as prompt | Widgets (standard-app date not documented) (S-L18-045, S-V1a-022) |
| ChatGPT web and mobile | Code-block HTML preview or text | Typed reply; the preview has no documented return channel (S-L18-128) | Widgets through a plugin or developer mode (S-L18-055, S-L18-119) |
| ChatGPT desktop and Codex app | Built-in browser rendering the local HTML | Element comments reach the agent (S-L18-115) | Widget panels (S-L18-109) |
| Codex CLI and IDE | Local HTML; `request_user_input` | Pasted `OD:` string | None; image input only (S-L18-137) |
| Cursor; VS Code with Copilot | Local HTML | Pasted `OD:` string | Widgets (Cursor 2.6+, VS Code 1.109+; S-L18-222, S-L18-220) |
| Gemini CLI | Local HTML and text | Typed reply | None (S-L18-217) |

**Templates.** One set of static HTML files in `skills/opendesigner/assets/templates/`, each fed by a JSON payload (candidate tokens, labels, contrast results), so the same file renders as a custom visual, an artifact, a local file or, in Phase 2, an MCP App view (DC-L18-06). REPO-PLAN names eight: `palette`, `type-scale`, `spacing-ruler`, `radius-shape`, `elevation`, `motion`, `component-sheet`, `options-gallery`. This spec adds six [inferred from the stage needs below]: `block-map`, `reference-card`, `asset-shelf`, `dial-board`, `coverage-map` and `diff`. Rules for all of them: the preview area showing the person's system is fenced off from host chrome; host light and dark tokens style the chrome; inline cards keep to 2 actions and no dropdowns, carousels hold 3-8 items, and anything that scrolls goes fullscreen (S-L18-017); every visual prints its text equivalent (values, ratios, px) so rung 7 carries the same content (DC-L18-06); every control has a keyboard path (S-L18-017).

**The return grammar.** Every channel speaks one line format, `OD:set <path>=<value> [--why "reason"]`, where `<path>` is a question id (`Q-shape-01`), a dial (`dials.roundness`) or a token path; it maps one-to-one onto `engine.py set` (DC-L18-07; REPO-PLAN engine contract). In Phase 2 a widget sends it as a visible `ui/message`, so the choice survives a context reset; silent `ui/update-model-context` is only for slider drags (DC-L18-07).

### 3.3 The stages

Question counts are computed from `questionnaire.json` (Quick / Standard / Expert, cumulative), with the number of `high` questions.

| Stage | Screens | Q / S / E | High | Gate |
|---|---|---|---|---|
| 0 Orient | S00 panel | 0 / 0 / 0 (+ panel) | 0 | none |
| 1 Context | S01, S02 | 1 / 7 / 9 | 3 | |
| 2 Brand, principles, assets | S03 | 1 / 7 / 8 | 3 | asset gate |
| 3 Platforms, devices, home of the system | S04, S05 | 2 / 10 / 14 | 5 | **Gate 1: scope and block map** |
| 4 Direction | S06, S07, S08 | 2 / 16 / 28 | 10 | **Gate 2: direction** (kept in Quick) |
| 5 Foundations | S09-S18 | 4 / 28 / 77 | 8 | |
| 6 Content and voice | S19 | 0 / 4 / 6 | 1 | |
| 7 Components, states, patterns | S20-S23 | 0 / 14 / 25 | 0 | |
| 8 Encoding, governance, preferences | S24, S25, S27 | 0 / 3 / 20 | 0 | |
| 9 Review | engine + critique | none | | **coverage check** |
| 10 Export and hand-off | S26 | 0 / 3 / 4 | 0 | confirm before any write to Figma or Paper |
| 11 Extend | later sessions | as needed | | locked decisions need consent |

The gates follow the questionnaire protocol (step 12) and DC-L17-12; Quick mode keeps only Gate 2, because building a full system on a direction nobody chose is the most repeated failure (S-L17-023).

**Stage 0. Orient** (time weight low).
- *Goal:* know what exists and agree how deep to go before asking anything.
- *Reads first:* repo manifests (the stack is an extractable block, `ctx.platforms.stack`), token files and CSS custom properties, an existing DESIGN.md or PRODUCT.md, a brand book, a Figma link, and any `opendesigner/state.json` (if found, jump to Stage 11). Code sources rank above prose (S-L17-206; S-L18-310).
- *Asks:* one bundled message, pre-filled from what it read: what the product is, who it is for, which surfaces and each surface's mode, the entry path (existing product, UI kit, reference, or brief only; DC-L17-02), and the depth mode with its question count. It offers the reference panel (Q-ref-01) and keeps it open on every screen.
- *Shows:* a "found / assumed / missing" summary and the **block map** (template `block-map`): the ontology's ten layers, each block tagged G, E, D, T or I, with the highest fan-out decisions highlighted: DC-L06-02 (15), DC-L10-01 (12), DC-L15-01 (12), DC-L10-02 (11), DC-L14-01 (10), DC-L16-02 (9), DC-L11-02 (8), DC-L15-04 (8) (`decision-graph.json`). Text fallback: a nested list with class tags. This is how the brief's "define the building blocks first" becomes visible (BRIEF req. 1).
- *Recommends:* Quick for a prototype, Standard for a real product, Expert for multi-platform or multi-brand work.
- *Records:* `engine.py init`; mode, entry path, surfaces with modes, found values marked `reference` or `asset`.
- *Exit:* mode agreed.

**Stage 1. Context: scope, audience, commitments** (S01, S02; medium, three high questions).
- *Goal:* set the ceilings later answers must respect: what the system serves, who uses it and how often, what is at stake, and the accessibility standard.
- *Asks:* Q-aud-01 in every mode; Q-scope-01 to Q-scope-05 and Q-aud-02 to Q-aud-04 in Standard and Expert. All nine are owner input: the model may pre-fill from the repo but never invents them (DC-L17-01).
- *Shows:* mostly text; Q-aud-01 previews its effect on body size and density (DC-L02-08, tied to density per the questionnaire's disagreement row).
- *Recommends:* WCAG 2.2 AA as the floor, with AAA contrast as a high-contrast mode (DC-L01-22).
- *Records:* the Product, Audience and Constraints sections of PRODUCT.md; in Quick mode, the assumed owner inputs.
- *Exit:* scope and accessibility target recorded, confirmed or assumed.

**Stage 2. Brand, principles and assets** (S03; high for personality and expressiveness, medium for assets).
- *Goal:* set the personality, the root with the largest reach in the graph (DC-L06-02 reaches 116 decisions; DECISION-GRAPH section 5), and inventory the assets only people can supply.
- *Asks:* Q-brand-01 personality sliders; Q-brand-02 products it should feel like plus the one thing people should remember; Q-brand-04 expressiveness; Q-brand-05 and Q-brand-06 marketing surfaces; Q-brand-07 three to five ranked principles (the tie-breaker when answers conflict, protocol step 7); Q-brand-08, the grouped "which of these do you have?" checklist, which opens Q-brand-03 (logo) here and the other hooks where each asset is used.
- *Shows:* `dial-board`: the eight dials (LEVERS A0) with a live specimen on real components, macro chips for brand adjectives (Playful, Serious, Premium and others; LEVERS A9) and a "what changed" panel; `asset-shelf`: one briefed slot per hook. Text fallback: dial values with one-line meanings, and the checklist.
- *Recommends:* turn vague words such as "clean" or "modern" into precise visual keywords before generating (S-L17-121); warn when Expression is above 66 on a finance or banking product (S-L06-010; LEVERS D2).
- *Records:* dial vector with `set_by`, ranked principles, the memorable thing, one asset decision per hook.
- *Exit:* **asset gate**: every hook has a status (`have`, `commissioning`, `tool`, `library`, `placeholder`, `not-needed`).

**Stage 3. Platforms, devices and where the system lives** (S04, S05; five high questions).
- *Goal:* prune the block map to what applies and fix where the truth lives.
- *Asks:* Q-plat-01 and Q-tool-01 in every mode; Q-plat-05 posture (derived in Quick from the "bold versus deferential" slider and shown as a confirm chip), Q-plat-02 device classes, Q-plat-03 input, Q-plat-04 driving, moving or headset use, Q-plat-06 to Q-plat-10, Q-tool-02 to Q-tool-04 (design tool and plan, which set the Figma limits in section 7).
- *Shows:* the block map again, with blocks that do not apply greyed out and a reason on each (for example haptics for a web-only product, driving rules when no car is in scope), printed as a gap analysis in the style of Figma's `figma-generate-library` skill (S-L17-210); device frames per platform.
- *Recommends:* web as the default platform with the native options and what each adds (questionnaire disagreement row for Q-plat-01); the canonical-source default from section 7.
- *Records:* the pruned block list with a status per block; `not applicable` counts as decided, so the coverage check does not report it as missing (L17 Part I stage 1).
- *Exit:* **Gate 1**: the person approves scope and the block map (skipped in Quick).

**Stage 4. Direction** (S06, S07, S08; the slowest stage, 10 high questions).
- *Goal:* choose one visual direction and the color system before any foundation detail.
- *Runs:* (1) three direction concepts in one line each, named and genuinely different in type, palette and layout (anti-convergence; the headline-swap test; S-L17-005), each stored as a dial vector plus overrides (DC-L17-05); (2) the person picks, edits or remixes ("type from A, color from B"); (3) the chosen concepts are rendered on real components and two or three real screens, light and dark side by side (DC-L16-06; DC-L17-11); (4) each direction is labelled with its safe choices and at least two risks, each with gain and cost, one of them tied to the memorable thing (DC-L17-06); (5) the model says once when a choice lands in a known generic look (S-L17-004; S-L17-021).
- *Asks:* Q-dir-01 style preset (LEVERS A10), Q-dir-02 density, Q-dir-03 to Q-dir-05; Q-theme-01 to Q-theme-04 (modes, other axes, re-skinning, multi-brand); Q-color-01 to Q-color-19, with Q-color-01 (brand color input, a locked-hex hook) and Q-color-02 (brand color placement) in every mode. The color cycle is one screen with sections (QUESTIONNAIRE "How the flow is built").
- *Shows:* `options-gallery` for directions (3-8 items), `palette` for color: ramps, roles, the contrast matrix and light and dark side by side. Figma or Paper can hold the direction boards when connected. Text fallback: the concept lines plus a token table per direction.
- *Recommends:* contrast-indexed ramp steps with purpose bands, generated in OKLCH (LEVERS B1); WCAG 2.2 enforced and APCA advisory (Q-color-17).
- *Records:* chosen direction, rejected directions and why, the resulting dial values, all color answers.
- *Exit:* **Gate 2**: the person approves the direction.

**Stage 5. Foundations** (S09-S18; 77 questions, 40 of them low weight).
- *Goal:* settle every foundation block, fast on defaults and slow only on the high fan-out ones (typeface sourcing DC-L02-01, base unit DC-L03-01, spacing progression DC-L03-02, breakpoints, roundness, depth model, motion feel).
- *Asks:* only the questions in the mode (Quick: Q-type-01, Q-shape-01, Q-depth-01, Q-motion-01). Hooks open where each asset is used: Q-type-02 (brand font files and licence), Q-icon-01, Q-icon-06, Q-img-01, Q-img-04, Q-img-06, Q-img-07, Q-motion-08, Q-motion-09.
- *Shows:* the per-block detail panel for every generatable block (DC-L17-13): what it is, where to use it, where not to (with the alternative and a threshold when one exists), the current value and its source, a live preview on a specimen and on real screens in every mode, the downstream blocks it changes (from the graph), and the accessibility rule that bounds it with the check result. Templates: `palette`, `type-scale`, `spacing-ruler`, `radius-shape`, `elevation`, `motion`.
- *Recommends:* the default with a one-line reason and the systems that use it (from the card).
- *Records:* `engine.py set`, then `generate` and `validate` on every change; one decision-log line per changed block.
- *Exit:* the validator reports no errors for the foundation layers.

**Stage 6. Content and voice** (S19; Q-voice-01 is high weight).
- *Asks:* the voice-guide hook (Q-voice-01); otherwise the model drafts voice traits and a tone matrix from the personality answers (Q-voice-02 to Q-voice-06).
- *Shows:* microcopy for the real components (buttons, errors, empty states) in the drafted voice beside a neutral version.
- *Records:* voice rules and the word list; drafts stay marked as drafts until a content designer or the owner reviews them; terminology is owner input (L17 Part H2, H-voice).

**Stage 7. Components, states and patterns** (S20-S23).
- *Asks:* Q-comp-01 component base (the tool hook H-comp: headless libraries per L08), Q-comp-02 inventory (a starter set of the 18 components found in 60 or more of 90 real systems; S-L17-302), Q-state-*, Q-form-*, Q-pattern-*, Q-ai-01. The contested policies are asked, not assumed: validation timing, disabled submit, tooltips on disabled controls, toasts versus inline messages, undo versus confirm (L08 BOARD note; section 11).
- *Shows:* `component-sheet`: anatomy, variants and a states matrix (default, hover, focus, active, disabled, loading, error, empty) in every mode.
- *Records:* component specs, generated component doc pages (section 7), policy answers.

**Stage 8. Encoding, governance and builder preferences** (S24, S25, S27; almost all Expert).
- *Asks:* token tiers, units, format, naming, composites, mode structure, Figma library hygiene, deprecation, re-skin inputs (Q-token-01 to Q-token-10); strictness, build order, contribution, lifecycle, metrics, communication, assistive-technology testing (Q-gov-01 to Q-gov-07); critique strictness, AI edits and optical corrections (Q-pref-01 to Q-pref-03).
- *Shows:* the token tree, the number of mode permutations the resolver will produce (the product of all contexts; S-L07-004), and whether the result fits the person's Figma plan (section 7).

**Stage 9. Review: validate, critique, coverage** (medium).
- *Runs:* `engine.py validate` first (section 6). Only on a passing system does the model critique: a 0-10 score per layer with "what a 10 looks like" and one question per gap (S-L17-006), a rubric fixed in advance, at least two runs for generated content because one output is an example, not an evaluation (S-L17-130; S-L17-132), at the strictness chosen in Q-pref-01 (DC-L15-11). It flags polished output resting on unverified patterns (S-L17-133).
- *Shows:* `coverage-map`: every block with its status and source; pending assets; assumed owner inputs; hard failures; warnings with any waivers.
- *Asks:* one question per remaining gap; in Quick mode, confirmation of the assumed owner inputs.
- *Exit:* no unmet hard rule, every block has a status, and the person accepts the named remainder (DC-L17-09).

**Stage 10. Export and hand-off** (S26; low).
- *Asks:* Q-dist-01 to Q-dist-04 (how the system leaves, where docs live, how AI tools read it, how adherence is checked).
- *Writes:* every output in section 7; offers the Figma and Paper pushes in section 10 and confirms before writing to a real file (Figma advises testing on a duplicate; L16 A1).
- *Shows:* an export summary and a `diff` view when an earlier version exists.

**Stage 11. Extend** (per change). The start-up routine and rules in section 9.

---

## 4. Building-block classes and hooks

### 4.1 The five classes

Every ontology node carries `class` (one primary route), `also` (other routes that work) and, for D and T blocks, `hook` (DC-L17-01; the full per-block table is L17 Part G3). The counts are L17's, over the 207 leaf blocks outside the `builder` meta layer.

| Class | Count | Meaning | What the model does by default | Decision side (gstack) | In Quick mode |
|---|---|---|---|---|---|
| **G** generatable | 135 (65%) | Derived by formula from raw inputs and the eight dials, or a sourced default | Decides silently with a visible default; teaches through the detail panel; the person can adjust or detach | Mechanical | Default applied |
| **E** extractable | 5 primary, 44 by any route | Best read from something that exists: the person's product, repo, logo, brand book, Figma file | Reads it at intake, shows value, method and confidence, asks to accept, adjust or ignore | Mechanical once accepted | Pre-filled, marked "from reference" |
| **D** designer-owned | 7 blocks, 14 asset hooks | Needs a human creator for acceptable quality: brand marks, photography, illustration, rich media, motifs, pictograms, sound | Opens a hook (4.3): "do you have this?", formats, checks, fallbacks, a briefed placeholder | Taste | Fallback applied, slot left open |
| **T** tool-assisted | 31 | An engineer can produce it with a named tool, with a caveat (licence, platform API, specialist review) | Recommends the tool, runs or links it where possible, states the caveat, records the choice | Taste when it touches identity, otherwise Mechanical | Recommended tool recorded as default |
| **I** owner input | 29 | A decision only the product owner or team can make (scope, platforms, governance, terminology) | Asks it, pre-filled from the repo where possible; never invents it | User Challenge | Recorded as `assumed`, confirmed at stage 9 |

A few blocks change class by platform: haptics are T on iOS and Android and not applicable on the web; app icons are D, but their platform size sets are T (DC-L17-01 platform notes). The questionnaire tags each question with the class of the block it decides (G 123, I 41, T 17, D 9, E 2 questions; `questionnaire.json`).

### 4.2 Rules for every hook

1. **Ask once, then open each hook where it is used.** The grouped checklist Q-brand-08 runs in stage 2; each ticked item opens its hook question at the stage where the asset is first needed (QUESTIONNAIRE "Three kinds of question"; DC-L17-04). Quick mode asks nothing, applies each fallback and keeps the asset shelf open.
2. **One master, generated derivatives.** Ask for the vector master (SVG or PDF with outlined text; layered SVG for app icons) and generate platform sets from it with size and safe-zone checks (L17 H1 rule 2).
3. **A licence ledger on every asset:** source, licence, attribution string, allowed slots, owner. Required credits are inserted, library notices kept, and assets are blocked from slots their licence forbids (L17 H1 rule 3).
4. **Fetch per project; never pool assets into a shared catalog.** Several licences forbid offering assets as a selectable library to a tool's users (ITF FFL, unDraw, Blush, Unsplash, Pexels; L17 H1 rule 4 [inferred application to an open-source builder]).
5. **AI fallbacks state the terms for the person's plan,** including that purely AI-generated material is not copyrightable in the US and that the EU AI Act Art. 50 requires machine-readable marking of synthetic output (L17 H1 rule 5; S-L17-563; S-L17-578).
6. **The commission path ships a brief and a contract reminder:** required files and sizes, the system's tokens and direction, and a note that a contractor's logo needs a written copyright assignment (S-L17-579).
7. **A generated stand-in is never presented as final** (S-L17-004; S-L17-021).
8. **Fallback order.** Identity assets (logo, app icon, illustration, photography, motifs, sound, motion signature): have it, then commission a designer with the generated brief, then an open library with a compatible licence, then a named tool with its caveat, then omit with a placeholder (DC-L17-04). Icons and typefaces are tool-assisted blocks, so they lead with open libraries and verified open faces, and commissioning is for custom pictograms or a brand face (DC-L05-01, DC-L02-01; questionnaire disagreement row "Asset hooks").

Every hook writes one Asset Decision Record into `state.json`: `{hook, status: have|commissioning|tool|library|placeholder|not-needed, files, licence, attribution, allowed_slots, owner, brief}` (DC-L17-04; L17 Part I stage 3). DTCG has no asset type, so assets are referenced from `opendesigner/assets.json`, not tokenized (BOARD note L05 to L07).

### 4.3 The hook table

Every D and T block in L17 Part G3 maps to one row. Formats, fallbacks and checks are condensed from L17 Part H2 and H3, where each carries its sources (S-L17-500 to S-L17-589).

| Hook | Blocks covered (class) | Question | "Do you have this?" | Accepted formats | What the model does with it | Fallbacks when the answer is no | Licence checks | Quality checks |
|---|---|---|---|---|---|---|---|---|
| **H-logo** | `found.imagery.brand-marks` (D) | Q-brand-03 | A logo? Symbol, lockups, one-color version? | Master SVG or PDF, text outlined; EPS legacy; PNG 512px+ as a stopgap | Places it in app bar, sign-in and email per DC-L05-13; proposes brand-color candidates from its fills; derives favicon, app-icon and social drafts | Commission (brief + assignment reminder); a wordmark set in the chosen typeface, labelled placeholder; AI logo tools (Looka, Brandmark) with the caveat that their marks may not be ownable or unique, plus a trademark search | Font licence allows use in logos (OFL, Google Fonts, Adobe Fonts and ITF FFL do); AI-tool ownership terms per plan | SVG parses; no `<text>` nodes; no embedded raster; viewBox present; SVGO pass; one-fill mono variant; legible at 16 and 32px; renders on light and dark |
| **H-appicon** | part of brand marks (D; size sets T) | Q-icon-06 | App icon artwork, ideally layered? | Apple layers as SVG or PDF (Icon Composer); Android adaptive foreground, background and monochrome layers; Play 32-bit PNG; PWA PNG, WebP or SVG | Builds each platform set from the layered master | Designer with a size brief; Icon Composer, Android Studio Image Asset Studio, Maskable.app | as H-logo | Apple 1024 canvas, Default, Dark, Clear and Tinted appearances, no custom shadows or photos; Android 108dp layers, 66dp safe zone, monochrome layer; Play 512x512 sRGB, 1024 KB or less; PWA maskable inside a 40% radius circle |
| **H-favicon** | derivative of brand marks (T) | with Q-brand-03 | asked with the logo | Master SVG | Generates the set | Generated from the logo; SVGO, Squoosh, Inkscape | none beyond the logo's | favicon.ico 32, icon.svg with a dark-scheme query, apple-touch-icon 180, manifest 192 and 512 plus maskable 512 |
| **H-icons** | `found.icon.source`, `.naming`, `.delivery`, `.platform` (T); `found.icon.tiers` (D) | Q-icon-01 (Q-icon-02 to -07 for style) | An icon set, or icons libraries lack? | SVG on the library grid; icon font or sprite; SF Symbol template SVG; Android Vector Drawable | Matches stroke, corners and sizes to the type (LEVERS B12; DC-L05-03); ships icons as components; maps to SF Symbols on Apple | Open libraries first: Lucide (ISC), Phosphor, Tabler, Heroicons (MIT), Material Symbols (Apache 2.0); custom icons on the Material 24dp keyline or an SF Symbols template; pictograms and spot icons commissioned | Library licence file and notices carried into the build | viewBox matches the grid; consistent stroke; SF Symbol template validates; SVGO pass; every meaningful icon has a label |
| **H-illus** | `found.imagery.illustration` (D); `pat.empty` (T) | Q-img-04 | Illustrations or a character style? | Master SVG; PNG derived; Lottie for animated art | Records the style (DC-L05-19, -20); places art in empty states and onboarding; tints to the palette where the licence allows | Commission with a style brief; open sets with their exact terms (unDraw, Open Peeps, Humaaans, Blush, Storyset); Recraft or Firefly with plan terms; or honest text-only empty states | Storyset requires credit; Storyset and Blush art barred from logo slots; unDraw bars AI training and competing packs | Valid SVG; ledger entry with attribution; palette distance to brand tokens [inferred] |
| **H-photo** | `found.imagery.photo` (D) | Q-img-01 | Photography, or a photo style you follow? | Highest-resolution originals; responsive JPEG, WebP, AVIF derived [inferred] | Writes art-direction rules (DC-L05-14); sets ratios and crops; text-on-image scrims with contrast checks | Commission a photographer; Unsplash or Pexels under their terms; AI images with ownership caveats and synthetic-content marking | No competing-service use (Unsplash); no endorsement or trademark use (Pexels); Content Credentials on AI images [inferred] | Minimum resolution per slot; source, licence and author stored; faces and logos flagged for release review [inferred] |
| **H-type** | `found.type.typeface.sourcing`, `.families`, `.delivery` (T) | Q-type-01, Q-type-02 | A brand typeface? Which licences: web, app embedding, self-hosting? | OTF or TTF masters; WOFF2; variable fonts with registered axes | Reads the font's licence fields; sets loading; maps weights to roles; checks script coverage against Q-type-04 | Verified open faces first (Google Fonts under OFL, Apache or UFL); platform faces for native-first products; Fontshare under ITF FFL v2.0; Adobe Fonts for web only; commercial foundry licences | Read name IDs 0, 7, 13, 14 and OS/2 fsType; refuse subsetting when fsType 0x100 is set or the licence is ITF FFL; ITF FFL faces never offered as a picker to other users; Adobe Fonts never self-hosted or embedded in apps | fvar table for variable fonts; WOFF2 signature; coverage of every script in scope |
| **H-color** | `found.color.brand` (E) | Q-color-01 | Brand colors that must be exact? | Hex, RGB, OKLCH, Pantone reference, Figma variables JSON, CSS | Locks them as the seed ("brand hue must be exact" flag, LEVERS A7); builds ramps and roles around them; proposes the nearest passing step where a locked color fails in a text role | Candidates from the logo or brand book; otherwise chosen in stage 4 with the Colorfulness and Warmth dials | none | Contrast of each role in every mode; gamut check for P3 values [inferred] |
| **H-motion** | `found.imagery.rich-media` (D) | Q-img-06 | Animations: logo animation, loaders, animated illustrations, 3D? | Lottie JSON; dotLottie; Rive .riv; glTF or GLB; USDZ | Places them in the one authored motion moment the direction allows; wires reduced-motion alternatives | Commission a motion designer; otherwise motion tokens only; community Lottie assets under their stated licences | Stated licence per community asset | Lottie validates against its JSON Schema; layer types lottie-web cannot render rejected; size, fps and duration budgets; glTF Validator; a reduced-motion alternative exists |
| **H-motif** | `found.imagery.motifs` (D); `found.shape.expressive` (T); `found.color.expressive` (E) | Q-img-07, Q-shape-05 | Brand patterns, textures, gradients or a signature shape? | SVG patterns; gradient definitions; shape SVG | Stores them as brand-expression tokens and assets with allowed surfaces (hero moments only, per the Expression dial) | Commission; or none, since decoration standing in for content reads as generic (S-L17-004; S-L17-021) | Owner's rights to the motif | Contrast of text over gradients and textures; usage limited to allowed surfaces |
| **H-sound** | `found.sensory.sound` (D) | Q-motion-08 | UI sounds or a sonic logo? | Apple: .aiff, .wav or .caf under 30 s; Android: Ogg, WAV, MP3, AAC, FLAC | Maps sounds to semantic events; respects silent mode | Commission a sound designer; platform system sounds; or no sound. No verified open UI-sound library exists (S-L17-552) | Licence per file | Codec, container and duration checks; loudness normalization [inferred] |
| **H-haptic** | `found.sensory.haptics` (T) | Q-motion-09 | Custom haptic patterns, or are system patterns enough? | Apple AHAP JSON; Android `VibrationEffect` compositions | Maps semantic haptic tokens to platform constants | System patterns first (Apple notification, impact, selection; Android `HapticFeedbackConstants`) | none | AHAP values 0-1 (out-of-range values are clamped, so warn); fallback where primitives are unsupported |
| **H-voice** | `found.content.voice`, `.tone`, `.microcopy`, `.localization` (T); `pat.onboarding` (T) | Q-voice-01 | A voice and tone guide or a word list? | PDF, Markdown, doc export, existing product copy | Extracts voice attributes and rules; drafts the tone matrix and microcopy in that voice | The model drafts from the personality answers, marked draft until a content designer or the owner reviews it; terminology stays owner input | Copy read from a reference is never reused verbatim (S-L17-023) | Readability lint; banned-word list; capitalization and mechanics applied consistently |
| **H-brandbook** | reference intake (E) | Q-ref-01, Q-brand-08 | A brand book? | PDF | Extracts candidate color tokens from vector fills, font names and embedded logos; asks for the SVG master of any logo found | n/a | Assets belong to the brand owner | A PDF cannot become editable Figma layers; values are candidates until accepted |
| **H-tokens** | `tok.delivery`, `deliver.pipeline`, `deliver.packaging`, `found.color.personalization`, `found.elevation.materials` (T) | Q-token-08, Q-tool-02 | Which platforms consume tokens, and how do you ship packages? | n/a | `engine.py export` writes CSS, Tailwind, Swift and Compose itself; for teams that want a pipeline it also writes a Style Dictionary or Terrazzo config (7.4) | Style Dictionary, Terrazzo, Tokens Studio; platform dynamic-color and material APIs | Tool licences | Build output compiles; every semantic token resolves in every mode |
| **H-figma** | `deliver.interop.figma.variables`, `.code-connect`, `deliver.interop.paper`, `.penpot`, `gov.tooling` (T) | Q-tool-03, Q-tool-04 | Which design tool and plan? | n/a | Pushes through the remote Figma MCP or writes DTCG import files; pushes to Paper through its MCP (section 10) | `use_figma` or the `figma-generate-library` skill (Full seat); Tokens Studio; Paper MCP; Penpot native DTCG | n/a | Collections within plan limits; scopes set, never all scopes; code syntax on every variable |
| **H-comp** | `comp.api`, `comp.feedback.ai`, `pat.ai`, `pat.other` (T) | Q-comp-01, Q-ai-01 | Which component library or stack? | n/a | Records the headless base and maps component specs onto it | Radix, Base UI, React Aria, the shadcn registry (L08; shadcn's default base moved to Base UI in July 2026, BOARD note L08) | Library licences | Keyboard and ARIA behavior per WAI-ARIA APG; states matrix complete |
| **H-dataviz** | `found.dataviz.scope` (T) | Q-viz-01, Q-color-19 | Do you show charts? Which library? | n/a | Themes the chart library from tokens (DC-L05-24) | Chart libraries per DC-L05-22 | Library licence | Chart palette passes color-vision-deficiency and contrast checks (DC-L05-23) |
| **H-a11y** | `guard.testing` (T) | Q-gov-07 | Who tests with assistive technology? | n/a | Exports automated checks and a manual walkthrough checklist per device class (DC-L14-14) | axe-core and lint rules; human screen-reader walkthroughs | n/a | Automated checks in CI; walkthrough recorded (automated tools catch only part of WCAG) |

The three extractable blocks that are not assets (`ctx.inventory`, `ctx.platforms.stack`, `comp.inventory`) are read through reference intake (section 5), not hooks (L17 Part G3, hook column "R").

---

## Notes for the owner (unique content to reconcile)

**Decisions this instance logged under "S1d spec" in `_coordination/DECISIONS.md` (18:59 IST):**
1. Five block classes (G, E, D, T, I) become node metadata; ONTOLOGY's "designer-owned" label for team decisions becomes owner input. Why: DC-L17-01; S1b already tags questions this way.
2. One canonical source per user system: `./opendesigner/state.json` (answers, dials, generator parameters, detached overrides) plus DTCG 2025.10 tokens with a Resolver; DESIGN.md, code, Figma and Paper are generated views; code-canonical stays an option in Q-tool-01. Why: settles DC-L16-02 vs DC-L07-08 vs the L00 code-first view; in an AI-first product the builder model is files in the repo (DC-L18-10).
3. Phase 1 is the LLM interview as skills; MCP Apps widgets are Phase 2; L16's standalone canvas (G2 option 4) is optional Phase 3. Why: BRIEF req. 6; DC-L18-01.
4. Twelve stages (0-11) laid over questionnaire screens S00-S27 in their validated order, with S1b's three gates plus a final coverage check; block map shown at stage 0, pruned at Gate 1. Why: keeps L17 Part I's stage logic without breaking the order validated against 465 graph edges.

**Positions this draft would have taken in sections 5-14 (not logged; for the owner to accept or drop):**
- *Surface mode gap:* Persuade / Operate / Read / Experience (S-L17-007) has no question in the final questionnaire; ask it in the stage 0 bundle and flag it to S1b.
- *Accessibility waivers:* reconcile DC-L17-07 ("never waivable") with L13 E1 level 2 ("override with a written reason"): values generated by construction cannot be waived; lint errors on authored usage can be overridden only by citing a WCAG-defined exception (for example the 2.5.8 spacing, inline, user-agent and essential exceptions) with a reason; taste lint is freely waivable.
- *Record vocabulary:* S1b uses `set_by` chosen, confirmed_default, auto_default, reference, plus `assumed` for Quick owner inputs; L18 uses confirmed, default, delegated, locked; REPO-PLAN's hook statuses are have, commissioning, using tool, skipped; L17's are have, commissioning, tool, open library, placeholder, not needed. Pick one set (suggested: `set_by` in {chosen, confirmed_default, auto_default, assumed, reference, asset} plus a separate `locked` flag and `supersedes`; hook status as in 4.2).
- *Placement:* DESIGN.md and PRODUCT.md at the project root, where gstack, Stitch and Claude's artifact skill look for them (S-L17-004, S-L17-213, S-L18-043); everything else in `./opendesigner/`.
- *DESIGN.md contract:* Google DESIGN.md v0.4.0 front-matter keys and its eight sections in order (S-L17-213), then OpenDesigner sections after them (Motion, Modes and themes, Iconography and imagery, Content and voice, Accessibility commitments, Platforms and devices, Decisions, Open items, How to extend), since the spec has no keys for modes, motion or breakpoints.
- *Scales:* add 96 (multiplier 24) to the LEVERS B8 spacing ladder (ONTOLOGY contradiction 5); keep 6 in the radius scale (ONTOLOGY contradiction 4); px in the source (ONTOLOGY contradiction 3).
- *Skills:* the four in REPO-PLAN plus `opendesigner-review` (validate, critique, coverage, and audit of an existing product), because review is a distinct trigger intent (gstack separates `/design-review`, S-L17-008; L18's `review-system` prompt). `tools/sync_skills.py` should copy `engine.py` and the data it reads into every skill that calls it, since claude.ai installs each skill separately (S-L18-001).
- *Paper:* push the default mode as Paper tokens and render other modes as labelled artboards until Paper ships modes (S-L16-018) [inferred].
- *Round trip:* automate one direction fully (state and DTCG to code, Figma, Paper); design-tool edits return only as reviewed "decision forks" with provenance (S-L16-039); no automatic two-way sync (only 5% of teams run one, DC-L11-16).
- *Ontology coverage gap:* `cards.json` now has 352 cards but ONTOLOGY maps 325; the 27 L17 and L18 cards need owners (suggested: DC-L17-03 `builder.intake`; DC-L17-01, -04 `builder.hooks`; DC-L17-05, -06 `builder.ai`; DC-L17-07, -09 `guard.checks`; DC-L17-10 `gov.decisions`; DC-L17-11 `builder.preview`; DC-L17-12 `builder.review`; DC-L17-13 `builder.controls`; DC-L17-02 `ctx.strategy`; DC-L17-08, DC-L18-08, -09 a new `builder.pacing`; DC-L18-06, -07 a new `builder.surface`; DC-L18-01, -02, -04, -05, -14 `deliver.ai`; DC-L18-03 `deliver.packaging`; DC-L18-10 `deliver.channels`; DC-L18-11 `guard.enforcement`; DC-L18-12 `builder.state`; DC-L18-13 `deliver.interop`).
- *Count drift:* DECISION-GRAPH.md prose still says 325 decisions and 431 edges and DC-L16-02 fan-out 8; `decision-graph.json` now has 352 nodes, 465 edges, and DC-L16-02 fan-out 9, DC-L10-02 fan-out 11. The JSON wins; the prose needs a refresh.
