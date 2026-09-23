# OpenDesigner specification

Synthesis S1d, written 2026-09-23. This is the definitive description of what OpenDesigner is and how it works, written so people and agents can implement and extend it without re-reading the research. R1 copies it to `docs/SPEC.md` (`_coordination/REPO-PLAN.md`); edit this file, not the copy.

**How to read the tags.** `DC-Lxx-nn` is a Decision Card (full text in `synthesis/cards.json`, or search with `python3 tools/jev_nav.py find`). `S-Lxx-nnn` is a source in `traces/Lxx-trace.md`. `Q-...` is a question in `synthesis/QUESTIONNAIRE.md` (machine copy `questionnaire.json`). References such as LEVERS B6 or L17 H2 point into `synthesis/LEVERS.md` or a research file. `[inferred]` marks a decision or reading made by this spec: treat it as a default to test, not a finding. Card text is not copied here; look it up by id. Product decisions made here are logged in `_coordination/DECISIONS.md` under "S1d spec (B)" (and three earlier entries under "S1d spec" at 19:01) and summarized in section 11. A first S1d instance wrote an alternative draft, `synthesis/OPENDESIGNER-SPEC.s1d-draft-b.md`; its useful content is merged here and it is not canonical.

**Counts used throughout** (read from the files on 2026-09-23): the ontology has 271 nodes in 10 layers, 207 of them design-system blocks outside the builder meta layer (ONTOLOGY; L17 G1; dated note, 2026-09-24: `ontology.json` has 275 nodes and 211 blocks outside the builder layer [S-V1b-091], and it is now the canonical block classification (orchestrator decision in `_coordination/DECISIONS.md`), with the five classes of section 4.1); `decision-graph.json` has 352 decisions, 465 edges and 12 cycles (DECISION-GRAPH.md prose still says 325 and 431; the JSON wins; dated note, 2026-09-24: 470 edges after session F1 fixes added five L17/L18 edges); the questionnaire has 28 stages and 192 questions, of which Quick asks 10, Standard 92 and Expert 191, with 30 high, 82 medium and 80 low time weights (`questionnaire.json`).

**How the brief's requirements are met** (`_coordination/BRIEF.md`):

| Requirement | Where this spec meets it |
|---|---|
| 1. Define the building blocks first | 3.2 P0 and P1 (block map shown before any choice, pruned at Gate 1), 4.1, 7.12 coverage |
| 2. Designer hooks, not replacement | 2 (principle 4), 4.2-4.5, 7.12 asset ledger and briefs |
| 3. Visual-first, teaching controls for generatable blocks | 3.4 detail panel, 3.6 surfaces and templates, 6 |
| 4. Reference intake at any point, never copying identity | 5 |
| 5. Nothing missed | 2 (principle 6), 3.2 P7, 7.12 coverage report |
| 6. The LLM is the interface | 1, 2 (principle 1), 8 |
| 7. Visual where the host allows, text otherwise | 3.6, 3.7 |
| 8. Time goes where it matters | 3.3, 3.5 |
| 9. Harmony over time | 7.2 DESIGN.md contract, 9 |
| 10. A team communication tool | 7.3 PRODUCT.md, 7.9 decision log, 7.11 rationale one-pager |
| 11. Everything traceable | 2 (principle 8), 5.6, 7.9, 7.10, 9 |

---

## 1. What OpenDesigner is

OpenDesigner is an open-source, AI-first resource for creating design systems, and the designs and visuals built on them. A person loads it into the model they already use (Claude, ChatGPT, Codex, or any of the roughly 46 clients that read the Agent Skills format [S-L18-203]), and the model runs a guided interview: it reads what already exists, shows the full map of building blocks, asks the questions that matter in the order in which they constrain each other, recommends sourced defaults, shows options visually where the host can render them, asks for examples, and writes a complete, checkable system into the person's own repository (BRIEF requirements 6-7; DC-L18-01). It serves four groups: software engineers who need a real system without design training; design engineers who want the decisions explicit and the output in code; designers who want the mechanical part generated (135 of 207 blocks are generatable, L17 G2) so they can spend their time on identity and craft; and anyone who needs to explain design choices to a team or brief a designer (BRIEF requirement 10). Its jobs are: create a system from a brief or a reference; audit an existing product and consolidate it into a system (DC-L17-02, DC-L11-04); extend a system in a later session, possibly with a different model, without breaking it (DC-L18-12); explain every decision in plain language; brief a designer or name a tool for the assets it cannot make well (DC-L17-04); and mirror the result into code, Figma and Paper (DC-L16-02). It is not a designer replacement or a logo generator (BRIEF requirement 2), not a theme generator that stops at color and type (generating from a few inputs yields a theme, not a system: L17 E2 finding 3 [S-L17-206]), not a tool for cloning another brand (DC-L17-03), not a closed canvas product like Claude Design or a hosting and documentation platform like Supernova or zeroheight (L18 E; L11 G), not a hosted app in Phase 1 (section 13), and not a design tool of record: Figma and Paper are mirrors of the system, not its source (DC-L16-02).

---

## 2. Principles

Every skill, template, script and output follows these rules.

| # | Principle | What it means in practice | Evidence |
|---|---|---|---|
| 1 | **AI-first** | The model is the interface. The repo is knowledge (chunked JSON and Markdown), instructions (skills) and a deterministic engine (Python, standard library only). The model holds the conversation and the judgment; the engine holds every calculation, because deterministic math beats model arithmetic for ramps, contrast and scales. No step needs a proprietary app or server; a standalone app is optional (Phase 3). | BRIEF req. 6; DC-L18-01; L18 C2; REPO-PLAN engine contract |
| 2 | **Visual where the host allows, text otherwise** | Every question can be shown on the best surface the host supports, from an MCP App view down to plain text. One JSON payload feeds every surface, and every visual prints its complete text equivalent (values, ratios, px). The interview never waits on a visual. | BRIEF req. 7; DC-L18-06; DC-L18-07 |
| 3 | **Time goes where it matters** | Depth follows downstream reach and block class: slow on high fan-out and taste decisions (brand personality DC-L06-02 fans out to 15 decisions and reaches 127 of the 352 in `decision-graph.json`; DECISION-GRAPH's older prose says 116), one-line confirms on mechanical defaults. Accessibility floors always get full treatment. | BRIEF req. 8; DC-L17-08; DC-L18-08; DECISION-GRAPH section 5 |
| 4 | **Designer hooks, never designer replacement** | Identity assets get a "do you have this?" hook with accepted formats, checks, honest fallbacks and a written brief. A placeholder is labeled as a placeholder everywhere it appears. | BRIEF req. 2; DC-L17-04; L17 H1 rule 7 [S-L17-004] |
| 5 | **Reference intake without copying identity** | A reference pre-fills measured structure (scales, rhythm, density, depth model, motion character); it never decides, and never carries a brand's name, logo, brand hue, proprietary typeface, imagery or copy. Brand presence is always asked, never inferred. | BRIEF req. 4; DC-L17-03; LEVERS E4; L17 F3 |
| 6 | **Nothing missed** | Every ontology block always has a visible status (pending, default, decided, not-applicable, awaiting-asset, assumed). Owner-input decisions are never invented; in Quick mode they are stored as assumed and confirmed before export. | BRIEF req. 5; DC-L17-09; DC-L17-08 |
| 7 | **Harmony over time** | The system lives in files, not in the chat: DTCG tokens (canonical), `state.json`, an append-only decision log, DESIGN.md and PRODUCT.md. Values are read from files, never remembered; decisions have stable ids; locked decisions change only with consent; decisions are superseded, never overwritten. | BRIEF req. 9; DC-L18-10; DC-L18-12; L18 G [S-L18-324] [S-L18-332] |
| 8 | **Traceable** | Every generated value traces to `levers.json` or a Decision Card; every decision records its reason, how it was set and what it changed; every value taken from a reference carries its provenance and confidence. | BRIEF req. 11; DC-L17-10; REPO-PLAN shared conventions |
| 9 | **Open and safe to install** | Portable formats only (Agent Skills, AGENTS.md, DTCG 2025.10, DESIGN.md, MCP). MIT for code and CC BY 4.0 for research and docs by default. Scripts inside skills need no network, and fetched pages are data, never instructions. | REPO-PLAN; DC-L18-14 [S-L18-001] |
| 10 | **Deterministic checks before model judgment** | Contrast, target size, scale steps, token references and lint rules run first; the model's critique runs only on a passing system, on a fixed rubric. Accessibility rules fail; taste rules warn. | DC-L17-07; [S-L17-011]; DC-L18-11 |
| 11 | **Teach while deciding** | Each block shows what it is, where to use it, where not to, a live preview in every mode, its source, and what else changes if it changes. Documentation is a by-product of decisions, not a later chore. | BRIEF req. 3; DC-L17-13; L17 finding 6 [S-L17-349] |

The block class decides the default behavior everywhere: generatable blocks are decided with a visible default, designer-owned blocks open a hook, tool-assisted blocks name a tool and its caveat, owner-input blocks are asked and never invented, and extractable blocks are read and confirmed (DC-L17-01; [S-L17-015]). "A recommendation you made is not an answer you received": defaults and assumptions stay marked as such so a later session can revisit them [S-L18-310].

---

## 3. The process as a model runs it

### 3.1 Phases and questionnaire stages

The interview order is the questionnaire's: 27 sequential screens (Stages 01-27) plus the reference panel (Stage 00), ordered by dependency step with zero ordering violations against all 465 edges of the decision graph and its overrides (`questionnaire.json` meta). L17's process stages (L17 I2) become ten phases that wrap those screens, so the process and the question data cannot drift apart [inferred]. The reference panel (Q-ref-01) is open in every phase.

| Phase | Questionnaire stages | Goal | Ends with | Questions Q / S / E (cumulative) | High-weight |
|---|---|---|---|---|---|
| P0 Orient | none yet; Q-ref-01 offered | read what exists, start at zoom 0 (the sketch), show the block map | found / assumed / missing summary | bundled opening question | 0 |
| P1 Context and block map | 01 Scope and team, 02 Audience, 03 Brand personality and principles, 04 Platforms and devices, 05 Where the system lives | settle the highest-reach context; prune the block map | **Gate 1: block map and scope** | 4 / 24 / 31 | 11 |
| P2 Direction | 06 Visual direction, 07 Themes and modes, 08 Color system | pick one direction from three concepts; build the color system | **Gate 2: direction** | 2 / 16 / 28 | 10 |
| P3 Foundations | 09 Color details, 10 Typeface, 11 Type scale, 12 Space and density, 13 Layout and shell, 14 Shape, 15 Depth, 16 Motion, haptics and sound | derive foundations from dials and raw inputs; tune where it matters | validator clean | 4 / 22 / 61 | 8 |
| P4 Assets, imagery, voice | 17 Icons and logo use, 18 Imagery and charts, 19 Content and voice | give every hook a status; draft voice | **Gate 3: assets** | 0 / 10 / 22 | 1 |
| P5 Components and patterns | 20 Component base, 21 Actions and states, 22 Forms and feedback, 23 Patterns and AI surfaces | pick the v1 set; generate each component with its states | component sheet validates | 0 / 14 / 25 | 0 |
| P6 Encoding, governance, output | 24 Tokens and encoding, 25 Team and governance, 26 Output and AI channels, 27 Builder preferences | decide storage, governance and channels | export plan confirmed | 0 / 6 / 24 | 0 |
| P7 Critique and coverage | none (checks) | find every gap; confirm assumptions and taste decisions | coverage accepted | one question per gap | |
| P8 Export and hand-off | none | write every output; mirror to design tools | validator exit 0 | confirmations only | |
| P9 Extend (later sessions) | any | change the system without breaking it | superseding decision records | per change | |

Totals: 10 / 92 / 191. The three gates follow DC-L17-12 and QUESTIONNAIRE protocol step 11. Gate 3 sits after Stage 19 rather than right after the Stage 03 checklist, because each asset brief must carry the system's tokens and direction (L17 H1 rule 6), which exist only after Stages 06-16 [inferred; logged]. Quick mode keeps only Gate 2 (DC-L17-12).

### 3.2 Each phase in detail

**P0 Orient** (fast: one or two turns).
- *Reads first, asks second:* repo manifests (the stack is an extractable block), token files and CSS custom properties, any `DESIGN.md`, `PRODUCT.md` or `AGENTS.md`, a brand book, a Figma link, and any `opendesigner/state.json` (if one exists, the extend skill takes over, section 9). Code beats prose as a source [S-L17-206]; never ask what files can answer [S-L18-310]. A PRODUCT.md or DESIGN.md counts as prior answers, confirmed in one line, not re-asked [S-L17-003].
- *Asks:* one bundled question with found values pre-filled: what the product is, who it is for, which surfaces and each surface's visitor mode (Persuade, Operate, Read, Experience [S-L17-007]), the entry path (existing product, UI kit, reference, or brief; Q-scope-05, DC-L17-02), and the depth mode with its question count (3.5). Then the memorable-thing question: "What is the one thing someone should remember after first seeing this product?" [S-L17-003]. Offer the reference panel. The surface mode has no question in the questionnaire yet, so it is asked here and stored per surface in `state.json`; it switches default density, card use and hero rules [inferred; section 11].
- *Shows:* the block map (template `block-map`; `design/atlas/01-building-blocks-map.html` is the prototype): ten layers, each block tagged G, E, D, T or I (section 4), with the highest fan-out decisions highlighted: DC-L06-02 (15), DC-L10-01 (12), DC-L15-01 (12), DC-L10-02 (11), DC-L14-01 (10), DC-L16-02 (9), DC-L11-02 (8), DC-L15-04 (8) (`decision-graph.json`). Text fallback: a nested list with class tags and counts. This makes "define the building blocks first" visible (BRIEF requirement 1).
- *Recommends:* Standard for a real product, Quick for a first look or prototype, Expert for multi-platform or multi-brand systems [inferred from the QUESTIONNAIRE depth-mode table].
- *Records:* `engine.py init`; mode, entry path, surfaces with modes, memorable thing; found values marked `reference` or `asset`.
- *Exit:* mode agreed; memorable thing recorded or explicitly skipped.

**P1 Context and block map** (slow).
- *Asks:* Stages 01-05 for the mode. High weight: Q-scope-01, Q-scope-03, Q-aud-01, Q-brand-01, Q-brand-04, Q-brand-06, Q-plat-01, Q-plat-05, Q-plat-07, Q-plat-02, Q-tool-01. Scope, audience and accessibility (Q-scope-01 to -05, Q-aud-02 to -04) are owner input: pre-filled from the repo where possible, never invented (DC-L17-01). Principles and their tie-break order (Q-brand-07) are asked here because every later conflict is settled with them (QUESTIONNAIRE protocol step 6). The grouped asset checklist (Q-brand-08) and the logo hook (Q-brand-03) run here, outside Quick mode. In Quick mode platform posture (Q-plat-05) is derived from the "bold versus deferential" slider and shown as a confirm chip (QUESTIONNAIRE depth modes).
- *Shows:* `dial-board`: the eight dials (LEVERS A0) with a live specimen on real components, macro chips for brand adjectives (Playful, Serious, Premium and others; LEVERS A9) and a "what changed" panel; a reference, if any, placed on the L09 personality map; Q-aud-01's effect on body size and density (DC-L02-08); the platform and device matrix; then the pruned block map with a reason on every block marked not applicable, printed as a gap analysis the way Figma's `figma-generate-library` skill does before it writes anything [S-L17-210]. The asset checklist fills the `asset-tray`.
- *Recommends:* WCAG 2.2 AA as the floor with AAA contrast as a high-contrast mode (DC-L01-22, DC-L11-19); web first with the native options and what each adds (QUESTIONNAIRE disagreements, Q-plat-01); the canonical source in 7.1. The model turns vague words such as "clean" or "modern" into precise visual keywords before generating anything [S-L17-121], and warns when Expression is above 66 on a finance or banking product [S-L06-010] (LEVERS D2).
- *Records:* decisions (7.9); PRODUCT.md content (7.3); blocks set to `not-applicable` with a reason (for example haptics on a web-only product, driving rules when no car is in scope), so the coverage check counts them as decided (L17 I2 Stage 1); an initial status per hook.
- *Gate 1:* the person approves scope and the pruned block map with each block's class. Skipped in Quick mode.

**P2 Direction** (slow).
- *Asks:* first, three direction concepts in one line each, named and genuinely different in typeface, palette and layout (anti-convergence and the headline-swap test [S-L17-005]); each concept is stored as a dial vector plus raw-input suggestions and overrides, built from the presets and macros (LEVERS A9, A10; DC-L17-05). The person picks, edits or remixes ("type from A, color from B"). Then Stage 06 (style, density, hierarchy, grouping), Stage 07 (modes, theme axes, re-skinning, multi-brand) and Stage 08, the color cycle, as one screen with sections (21 decisions that constrain each other, DECISION-GRAPH section 4). At the start of the stage the model asks for one or two examples the person likes and one they dislike (DC-L18-09 [S-L18-323]).
- *Shows:* `option-gallery`: each concept rendered on real components and two or three sample screens, light and dark side by side (DC-L16-06, DC-L17-11); each labeled with its SAFE choices and at least two RISKS, each risk with its gain and cost and at least one tied to the memorable thing (DC-L17-06). The model says once when a concept lands in a known generic AI look (L17 A2 item 7 [S-L17-004] [S-L17-021]). Then `palette`: ramps, role mapping, light and dark, the contrast matrix. When Figma or Paper is connected, the direction boards can also be placed there. Text fallback: the concept lines plus a token table per direction.
- *Recommends:* one direction, with the reason tied to the memorable thing and the audience. Defaults: the Flat 2.0 preset (LEVERS A10), contrast-indexed ramp steps with purpose bands generated in OKLCH (LEVERS B1), WCAG 2.2 enforced with APCA advisory (Q-color-17), dark mode as a separate mapping (LEVERS B4).
- *Records:* the chosen direction, its dial values, all color answers, and the rejected concepts with the reason (useful to later sessions and to the team).
- *Gate 2:* direction approval, kept in every mode including Quick.

**P3 Foundations** (fast on defaults, slow on eight questions).
- *Asks:* Stages 09-16 for the mode. High weight: Q-type-01, Q-type-07, Q-space-01, Q-space-02, Q-layout-01, Q-shape-01, Q-depth-01, Q-motion-01. Everything else is a confirm-the-default turn, grouped up to three. The typeface hook (Q-type-02), sound hook (Q-motion-08) and haptics hook (Q-motion-09) open here.
- *Shows:* the detail panel (3.4) for every block, on templates `palette` (09), `type-scale` (10-11), `spacing-ruler` (12-13), `radius` (14), `elevation` (15), `motion` (16), each with the accessibility rule that bounds it and the check result.
- *Recommends:* the formula output from `levers.json` with its one-line reason and the systems that use it (section 6).
- *Records:* `engine.py set` for each change, then `generate` and `validate`; one decision-log line per changed block.
- *Exit:* no validator errors for the foundation layers; warnings shown with their rule.

**P4 Assets, imagery and voice** (medium).
- *Asks:* the remaining hooks where each asset is used: logo in the product (Q-icon-08), icon set (Q-icon-01), app icon (Q-icon-06), photography (Q-img-01), illustration (Q-img-04), animated assets (Q-img-06), motifs (Q-img-07), charts (Q-viz-01), the voice guide (Q-voice-01, high weight), then tone, capitalization, reading level and word list (Q-voice-02 to -06).
- *Shows:* `asset-tray`: one slot per hook with its status, files, licence and brief; for voice, microcopy on real components (buttons, errors, empty states) in the drafted voice beside a neutral version (L17 I2 Stage 7).
- *Does:* with a yes, ingests, validates and derives (4.3); with a no, offers the fallbacks in order and writes a briefed placeholder slot. Drafted voice stays marked "draft" until a content designer or the owner reviews it; terminology is owner input (L17 H2, H-voice).
- *Gate 3:* every hook has an asset status and every missing asset has a brief. In Quick mode the fallbacks are applied without asking and open hooks are listed in P7.

**P5 Components and patterns** (medium).
- *Asks:* Q-comp-01 (component base, tool hook H-comp), Q-comp-02 (v1 set, owner input), the state and form questions where systems genuinely disagree, which are asked and never assumed: validation timing, disabled submit, tooltips on disabled controls, toasts versus inline messages, undo versus confirm (QUESTIONNAIRE disagreements table; BOARD L08 note); patterns and AI surfaces (Stage 23).
- *Shows:* the component checklist in tiers (the 18 components found in 60 or more of the 90 designsystems.surf systems as the starter set, the next 12 as "likely next" [S-L17-302]), then `component-sheet`: anatomy, variants and the full state matrix (default, hover, focus, active, disabled, loading, error, empty) in every mode, with use / avoid and accessibility behavior (DC-L17-13, DC-L13-12).
- *Records:* component specs and doc pages (7.8), policy answers.
- *Exit:* the component sheet passes target, focus and contrast checks in every state.

**P6 Encoding, governance and output** (fast; mostly Expert).
- *Asks:* Stages 24-27. Standard mode asks Q-token-01, Q-gov-01, Q-dist-01, Q-dist-02, Q-dist-03 and Q-pref-01; everything else takes its default.
- *Shows:* the token tree, the number of mode permutations the resolver will produce (the product of all modifier contexts [S-L07-004]), whether that fits the person's Figma plan (7.6), and the export menu.
- *Records:* the export plan and governance answers.

**P7 Critique and coverage** (medium).
- *Runs:* `engine.py validate` first (section 6). Only on a passing system does the model critique, at the strictness chosen in Q-pref-01 (DC-L15-11): a 0-10 score per ontology layer with "what a 10 looks like" and one question per gap [S-L17-006]; a rubric fixed in advance and at least two critique runs for generated content, because one output is an example, not an evaluation [S-L17-130] [S-L17-132]; a warning when output looks polished but rests on unverified patterns [S-L17-133].
- *Shows:* `coverage`: every block with its status and source; pending assets; assumed owner inputs; blocks still on unreviewed defaults; hard failures; warnings and waivers.
- *Asks:* one question per remaining gap; confirmation of every `assumed` owner-input decision (in Quick mode, the 37 questions in `questionnaire.json` meta `quick_mode_assumed_owner_inputs`); the final review of taste decisions (DC-L17-12).
- *Exit:* no unmet hard rule, every block has a status, and the person accepts any named remainder (DC-L17-09).

**P8 Export and hand-off** (fast).
- *Writes:* every output in section 7; adds the AGENTS.md pointer after asking; shows an export summary, and a `diff` view when an earlier version exists (DC-L16-09).
- *Offers:* mirrors to Figma and Paper when their MCPs are connected, confirming before any write to a real file (Figma advises testing on a duplicate, L16 A1; section 10).
- *Suggests:* building product screens from the written system in a fresh session, so the interview transcript does not crowd the build context [S-L18-300] [S-L18-309].
- *Exit:* `validate` exits 0 and the rationale one-pager exists.

**P9 Extend.** The start-up routine and rules in section 9.

### 3.3 Pacing: where the time goes

- **Time weight per question** (QUESTIONNAIRE time-weight rule, [inferred] from the graph): `high` when a decided card has fan-out 5 or more, or the question is in Quick mode (30 questions); `medium` for fan-out 2-4, asset hooks, raw inputs, the reference panel and owner-input questions (82); `low` otherwise (80). Accessibility floors (Q-aud-03, Q-color-17, Q-motion-07) are treated as high regardless of fan-out, because a wrong answer there fails real users, not just taste [inferred].
- **What each weight gets:** high: say why it matters, show 2-3 options with their visual effect and a real system that uses each, recommend the default with its source, and say what it changes downstream. Medium: the recommended default and the main alternatives. Low: the default in one line, confirm or change, grouped up to three (DC-L18-08, DC-L18-09; QUESTIONNAIRE protocol step 3).
- **Decision kinds** (gstack's split, mapped to classes by DC-L17-01): *mechanical* decisions (generatable blocks) take a visible default; *taste* decisions (designer-owned, taste-heavy tool-assisted and extractable blocks) are recommended and reviewed at the final gate; *user challenges* (owner input, and anything that changes the person's stated direction) are never decided without explicit consent [S-L17-015].

### 3.4 One question, one turn, and the detail panel

- **Question format** (DC-L18-09; L18 F): 2-4 real options, one marked recommended with a one-line reason in "X because Y" form, one visual per option where possible, "other" always allowed, and one line on what the answer changes downstream (from the card's Affects field). Neutral wording, with the recommendation in the option, not the question [S-L18-317]. On cycle screens one form with every linked question and a shared preview is allowed [S-L18-021].
- **Only listed options are offered;** anything else is recorded as a custom value with the person's reason (QUESTIONNAIRE protocol step 8).
- **Defaults are recorded honestly:** an unanswered or delegated question is stored as `auto_default` or `delegated`, never as chosen [S-L18-310].
- **Play back before writing:** after each stage, a plain-sentence summary a teammate could read, with stable decision ids so the person can say "change D14" [S-L18-343] [S-L18-312].
- **Conflicts are shown, not averaged:** when an answer conflicts with an earlier one (the cycles named in the stage headers) or two macros push a dial in opposite directions, the model shows the conflict and settles it with the ranked principles from Q-brand-07 (QUESTIONNAIRE protocol step 6; LEVERS A9).
- **Detail panel** for every block (DC-L17-13): what it is; where to use it; where not to, with the alternative and a threshold where one exists; the current value and its source; a live preview in every mode; the accessibility rule that bounds it and the check result; and the downstream blocks that change with it (from `decision-graph.json`). It also carries three short lines adapted from gstack's research synthesis: the category convention, the current trend, and the person's departure if any (L17 A3). Kept short: precise beats exhaustive [S-L17-113].

### 3.5 Depth modes

| Mode | Questions asked | For whom | Gates | Hooks | Everything else |
|---|---|---|---|---|---|
| **Quick** | 10: Q-aud-01, Q-brand-01, Q-plat-01, Q-tool-01, Q-color-01, Q-color-02, Q-type-01, Q-shape-01, Q-depth-01, Q-motion-01 | "a complete system in minutes" | direction only | not asked; fallbacks applied, asset tray stays open | generatable blocks take defaults; owner-input questions stored as `assumed` and confirmed in P7 |
| **Standard** | 92 (Quick + Standard) | an engineer setting up a real product system | all three | asked | Expert questions take defaults and stay editable |
| **Expert** | 191 (all sequential questions) | design-system leads; multi-platform or multi-brand systems | all three | asked | nothing is decided silently; defaults are still pre-filled |

Quick mode's ten combine the highest fan-out step-0 decisions with the L09 divergence points that change the look most; everything L09 found nearly every system shares is pre-filled instead of asked (QUESTIONNAIRE "Depth modes"). The reference panel is available in every mode and never required. The person can deepen one stage at any time without switching mode (DC-L18-08 option c).

### 3.6 Visual surfaces per host

**The ladder** (DC-L18-06). The model detects what it can use from the tools it sees, picks the highest rung available, says which one is in use, and never blocks on a visual:
1. An OpenDesigner MCP App view (Phase 2 server).
2. Host-native HTML the model writes: Claude custom visuals, Claude artifacts, Claude Code artifacts, the Codex desktop browser.
3. Figma or Paper canvas through their MCP servers (specimen frames or artboards; section 10).
4. A local HTML file (`engine.py preview --open`, or a template filled with the state) that the person opens.
5. The host's question tool (Claude AskUserQuestion, up to 4 options; Codex `request_user_input`).
6. Plain text: hex values, ratios, px values, numbered options, ASCII sketches.

Claude Design is a hand-off target (it can import the DESIGN.md and tokens), not a rung OpenDesigner can drive, because it is a closed product [S-L18-029] [inferred].

| Host | Phase 1 (skills, no server) | Phase 2 (with the MCP server) | How the choice comes back |
|---|---|---|---|
| Claude app, web and desktop | custom visuals (a click sends a follow-up prompt) [S-L18-041]; artifacts for multi-panel screens [S-L18-027] | MCP Apps views [S-L18-013] | follow-up prompt; widget message; typed or pasted `OD:` line |
| Claude app, mobile | text, and artifacts where the app shows them [inferred] (custom visuals are not on mobile [S-L18-041]) | MCP Apps views [S-L18-013] | typed; widget message |
| Claude Code CLI | local `preview.html`; Claude Code artifacts with "copy as prompt" [S-L18-043]; AskUserQuestion [S-L18-304] | none: the CLI does not render MCP Apps [S-L18-044] | pasted `OD:` line; structured answer |
| Claude desktop Code tab | as the CLI | MCP App widgets (date not documented for the standard app) [S-V1a-022] | widget message |
| ChatGPT web and mobile | code-block HTML preview with no channel back [S-L18-128]; text | MCP Apps through a plugin or developer mode [S-L18-055] [S-L18-119] | typed; widget message |
| ChatGPT desktop and Codex app | the built-in browser renders local HTML and takes element comments [S-L18-115] | MCP App panels [S-L18-109] | element comments; widget |
| Codex CLI and IDE | local HTML; `request_user_input` | none; image input only [S-L18-137] | pasted `OD:` line |
| Cursor; VS Code with Copilot | local HTML | MCP Apps (Cursor 2.6+, VS Code 1.109+) [S-L18-222] [S-L18-220] | widget message |
| Gemini CLI and other terminals | local HTML; text | none [S-L18-217] | typed |
| Any host with the Figma remote MCP or Paper MCP | specimen frames or artboards | same | the agent reads the selection (L16 A1, B2) |

**Templates.** One set of static HTML files in `skills/opendesigner/assets/templates/`, each fed one JSON payload (candidate tokens, labels, contrast results), so the same file renders as a custom visual, an artifact, a local file or, in Phase 2, an MCP App view (DC-L18-06). REPO-PLAN names eight: `palette`, `type-scale`, `spacing-ruler`, `radius`, `elevation`, `motion`, `component-sheet`, `option-gallery`. This spec adds six the brief requires [inferred; logged]: `block-map` (requirement 1), `dial-board` (the eight dials with macro chips and a "what changed" panel; requirement 3), `reference-card` (each extracted value with method, confidence and Accept / Adjust / Ignore; requirement 4), `asset-tray` (requirement 2), `coverage` (requirement 5) and `diff` (before and after per mode for extend sessions; DC-L16-09). Rules for all of them: at most two primary actions, no dropdowns or popovers in inline cards, carousels of 3-8 items, fullscreen for anything that scrolls, host style tokens for the chrome in light and dark [S-L18-017] [S-L18-101]; the person's own tokens render inside a visibly fenced preview area so host chrome and their system never mix, and every control has a keyboard path [inferred].

### 3.7 How a visual choice returns to the model

One compact line format for every channel (widget message, click-to-prompt, pasted string, typed reply), parsed identically and mapped one-to-one onto `engine.py set` (DC-L18-07; REPO-PLAN engine contract):

```
OD:set <path>=<json-value> [--why "reason"]       <path> is a question id (Q-shape-01), a dial (dials.roundness) or a token path
OD:lock <path>        OD:unlock <path>            protect or release a decision (unlock needs the person's consent)
OD:accept <ref-id>:<path>    OD:ignore <ref-id>:<path>    act on a value pre-filled from a reference
```

A visible chat message is preferred over a silent context update, so the choice appears in the transcript and survives a context reset; silent `ui/update-model-context` is used only for slider drags (DC-L18-07).

### 3.8 gstack methods adopted

From L17 A3 (gstack is Tier C: concrete, versioned methods, used as opinion [S-L17-001]):

| Method | Verdict | Where it runs |
|---|---|---|
| Read what exists before asking; treat PRODUCT.md or DESIGN.md as prior answers | adopt | P0 [S-L17-003] |
| The memorable-thing question; every later risk cites it | adopt | P0; P2 risks [S-L17-003] |
| Product truth (PRODUCT.md) kept apart from the visual system (DESIGN.md) | adopt | 7.2, 7.3 [S-L17-020] |
| Confirm reference URLs before fetching | adopt | Stage 00; section 5 [S-L17-003] |
| Three-layer synthesis and the "EUREKA" departure | adapt | detail panel lines (3.4) |
| SAFE choices versus RISKS with gain and cost | adopt | P2 and Gate 2 [S-L17-004] |
| Named menus (aesthetic, decoration, color strategy, motion) | adapt | presets and macros over the eight dials (LEVERS A9, A10) |
| Concepts in text first, then rendered variants that differ in type, palette and layout | adopt | P2 and every "show me options" request [S-L17-005] |
| Comparison board with rate, remix, regenerate | adopt | `option-gallery`, remix at block level |
| Taste profile with decay | adapt | per project only, stored in `state.json`, visible and editable, never applied across projects |
| Persuade / Operate / Read / Experience per surface | adopt | P0, stored per surface [S-L17-007] |
| Mechanical / Taste / User Challenge | adopt | 3.3 [S-L17-015] |
| 0-10 per layer with "what a 10 looks like" | adopt | P7 [S-L17-006] |
| Deterministic detector first; slop catalog, "three looks" and font lists as lint with ids and waivers | adopt (lists adapted into warnings) | 6.3, 6.5 [S-L17-011] |
| DESIGN.md in Google's format plus an agent rule to read it | adopt as the readable view | 7.2; AGENTS.md pointer (7.12) [S-L17-010] |
| Tokens extracted by a vision model from an approved mockup | reject as a source of truth | tokens come from the engine; vision reads references only [S-L17-014] |
| Hard font bans | reject as bans | warnings only |
| Raster mockups as the main preview | reject for system work | previews render real HTML/CSS from the tokens (DC-L17-11) |

---

## 4. Building-block classes and hooks

### 4.1 The five classes

Every one of the 207 design-system blocks (L17's count on the 23 September map) carries one primary class (how OpenDesigner gets a good value when the person supplies nothing), optional `also` classes (other routes that work) and, for D and T blocks, a `hook` (DC-L17-01; per-block table in L17 G3, copied into `data/` by `tools/build_data.py`). ONTOLOGY.md's own provenance field used "designer-owned" for team decisions too; the five classes replace it (section 11).

Dated note, 2026-09-24: `ontology.json` is now the canonical block classification (orchestrator decision in `_coordination/DECISIONS.md`). Its `provenance` field uses the same five classes, spelled `generatable`, `extractable`, `designer-owned`, `tool-assisted` and `owner-input`. Its 211 blocks outside the builder layer [S-V1b-091] are 156 generatable, 23 tool-assisted, 21 owner input, 9 designer-owned and 2 extractable. Over all 275 nodes the counts are 208, 26, 27, 11 and 3 (counted from `ontology.json` by session F1 fixes). The table below keeps L17's counts for the 207-block map.

| Class | Blocks | Meaning | What the model does | Decision kind (3.3) | In Quick mode |
|---|---|---|---|---|---|
| **G** generatable | 135 (65%) | derived by formula from the raw inputs and eight dials, or a sourced default | decides with a visible default; teaches with the detail panel; the person adjusts or detaches | mechanical | default applied |
| **E** extractable | 5 (2%) primary; 44 (21%) by any route | best read from something that exists: the product, repo, logo, brand book, Figma file | reads it at intake; shows value, method and confidence; asks Accept, Adjust or Ignore | taste until accepted | pre-filled, marked "from reference" |
| **D** designer-owned | 7 (3%), expanding into 14 asset hooks | needs a human creator for acceptable quality: brand marks, photography, illustration, rich media, motifs, pictograms, sound | opens a hook (4.3); never generates a final version | taste | fallback applied, slot left open |
| **T** tool-assisted | 31 (15%) | an engineer can produce it with a named tool, with a caveat (licence, platform API, specialist review) | names the tool, runs or links it where possible, states the caveat, records the choice | taste when it touches identity, otherwise mechanical | recommended tool recorded as default |
| **I** owner input | 29 (14%) | a business decision only the team can make: scope, platforms, governance, terminology | asks it, pre-filled from the repo where possible; never invents it | user challenge | stored as `assumed`, confirmed in P7 |

Per layer (L17 G2): Context 10 I and 2 E; Principles 10 G and 5 I; Foundations 74 G, 16 T, 7 D, 2 E, 1 I; Tokens 12 G, 2 I, 1 T; Components 15 G, 2 I, 2 T, 1 E; Patterns 14 G, 4 T; Guardrails 3 G, 1 T, 1 I; Delivery 5 G, 6 T, 1 I; Governance 7 I, 2 G, 1 T. Questions carry the class of the block they decide: G 123, I 41, T 17, D 9, E 2 (`questionnaire.json`). A few blocks change class by platform: haptics are T on iOS and Android and not applicable on the web; app icons are D, but their platform size sets are T (DC-L17-01 platform notes).

### 4.2 Rules for every hook (L17 H1)

1. **Ask once, then open each hook where it is used.** The grouped checklist (Q-brand-08) runs in Stage 03; each hook then opens at the stage where its asset is first needed (4.5). Quick mode asks nothing, applies each fallback and keeps the asset tray open (DC-L17-04).
2. **Fallback order.** Identity assets (logo, app icon, illustration, photography, motion signature, motifs, sound): have it, then commission a designer with the generated brief, then an open library with a compatible licence, then a named tool with its caveat, then omit with a placeholder (DC-L17-04). Icons and typefaces are tool-assisted blocks, so they lead with open libraries and verified open faces, and commissioning is for custom pictograms or a brand face (DC-L05-01, DC-L02-01; QUESTIONNAIRE disagreements, "Asset hooks").
3. **One vector master, generated derivatives,** with automatic size and safe-zone checks [S-L17-500] [S-L17-507] (the derivation pipeline itself is [inferred]).
4. **A licence ledger entry per asset:** source, licence, attribution string, allowed slots, owner. Required credits are inserted, library notices kept, and assets are blocked from slots their licence forbids [S-L17-512] [S-L17-522] [S-L17-523].
5. **Fetch per project; never pool assets into a shared catalog,** because several licences forbid offering their assets as a selectable library inside a tool (ITF FFL, unDraw, Blush, Unsplash, Pexels) [S-L17-536] [S-L17-519] [S-L17-529] [inferred application to an open-source package].
6. **AI fallbacks state the terms for the person's plan.** Output ownership varies by tool and plan; purely AI-generated material is not copyrightable in the US (the Supreme Court denied review of Thaler v. Perlmutter on 2 Mar 2026); the EU AI Act Art. 50 requires machine-readable marking of synthetic output [S-L17-525] [S-L17-559] [S-L17-563] [S-L17-578].
7. **The commission path ships a brief and a contract reminder:** required files and sizes, the system's tokens and direction, and a note that a contractor's logo needs a written copyright assignment [S-L17-579].
8. **A generated stand-in is never presented as final;** placeholders are labeled "placeholder" in the product preview, DESIGN.md and the asset ledger [S-L17-004] [S-L17-021].

Every hook writes one Asset Decision Record to `opendesigner/assets.json`: `{hook, status, files, licence, attribution, allowed_slots, owner, brief}`, where status is one of `have`, `commissioning`, `open-library`, `tool`, `placeholder`, `not-needed` [inferred; logged]. DTCG has no asset type, so assets are referenced from this file rather than tokenized (BOARD note L05 to L07).

### 4.3 Asset hooks (designer-owned blocks)

Condensed from L17 H2 (formats, fallbacks and checks verified against 81 Tier A pages, S-L17-500 to S-L17-589) and the Hook lines in QUESTIONNAIRE.

| Hook (question) | Accepted formats | What the model does with it | Fallbacks when the answer is no | Licence checks | Quality checks |
|---|---|---|---|---|---|
| **H-logo** logo, wordmark, lockups (Q-brand-03; Q-icon-08 for in-product use) | SVG or PDF master with outlined text; EPS legacy; PNG 512px+ as a stopgap | places it per the logo rules (DC-L05-13); proposes brand-color candidates from its fills; derives favicon, app-icon and social-image drafts | commission (brief and assignment reminder); a wordmark in the chosen typeface, labeled placeholder; AI logo tools (Looka, Brandmark) with the caveat that their marks may not be ownable or unique, plus a trademark search [S-L17-564] [S-L17-565] | the font licence allows logo use (OFL, Google Fonts, Adobe Fonts and ITF FFL do [S-L17-534]); AI-tool ownership per plan | SVG parses; no `<text>` nodes; no embedded raster; viewBox present; SVGO pass; one-fill mono variant; legible at 16 and 32px; renders on light and dark |
| **H-appicon** app icon (Q-icon-06) | Apple layers as SVG or PDF for Icon Composer; Android adaptive foreground, background and monochrome layers; Play 32-bit PNG; PWA PNG, WebP or SVG | builds each platform set from the layered master | placeholder from the logo glyph, labeled; commission for a shipped app; Icon Composer, Android Studio Image Asset Studio, Maskable.app for assembly | SF Symbols may not be used in app icons or logos [S-L05-010] | Apple 1024x1024 (watchOS 1088), Default, Dark, Clear and Tinted appearances, no custom shadows or photos; Android 108dp layers, 66dp safe zone, monochrome layer; Play 512x512 sRGB under 1024 KB; PWA maskable inside a 40% radius circle [S-L17-500] to [S-L17-507] |
| **H-favicon** (derived with the logo) | master SVG | generates `favicon.ico` 32, `icon.svg` with a dark-scheme style, `apple-touch-icon` 180, manifest 192 and 512 plus maskable 512 | generated from the logo symbol (SVGO, Squoosh, Inkscape) | as H-logo | files exist at the stated sizes [S-L17-508] |
| **H-illus** illustration, characters, empty-state art (Q-img-04) | SVG master; PNG 2x; Lottie for animated pieces | records the style (DC-L05-19, DC-L05-20); places art in empty states and onboarding; tints to the palette only where the licence allows changes | honest icon-plus-text empty states; commission with a brief derived from the icon stroke and palette; open sets under exact terms (unDraw, Open Peeps and Humaaans under CC0, Blush, Storyset); Recraft or Firefly with plan terms and the caveat that style drifts between pieces | Storyset requires credit; Storyset and Blush art barred from logo slots; unDraw bars AI training and competing packs [S-L17-519] [S-L17-522] [S-L17-523] | valid SVG; ledger entry with attribution; palette distance to brand tokens [inferred] |
| **H-photo** photography and art direction (Q-img-01) | JPEG, WebP or AVIF exports plus a written brief; RAW or TIFF masters stay outside the system | writes art-direction rules (DC-L05-14), ratios and crops; adds text-on-image scrims with contrast checks | the model drafts the photo brief from the sliders; commission; stock against the brief (Unsplash, Pexels); AI images with ownership caveats and synthetic-content marking; neutral placeholders until real images arrive (NN/g found AI images close to stock but failing on artifacts and stereotypes [S-L17-126]) | no competing-service use (Unsplash); no endorsement or trademark use (Pexels) [S-L17-529] [S-L17-530]; EU AI Act marking | minimum resolution per slot; source, licence and author stored; faces and logos flagged for release review [inferred] |
| **H-type** brand typeface (Q-type-01, Q-type-02) | WOFF2 for web; OTF or TTF for apps; variable fonts with registered axes preferred | reads axes and Unicode coverage from the file; sets up loading; maps weights to roles; checks coverage of every script in scope (Q-type-04, DC-L02-25) | verified open faces first (Google Fonts under OFL, Apache or UFL: Inter, Roboto Flex, Noto, IBM Plex); platform faces for native-first products; license a commercial face; commission a custom face (slow and costly [S-L06-031]) | Fontshare (ITF FFL v2.0): no subsetting or format conversion, never offered as a picker to other users; Adobe Fonts: web embed code only, no self-hosting, no native apps; OS system fonts never embedded [S-L17-536] [S-L17-538] [S-L02-001] | read name IDs 0, 7, 13, 14 and OS/2 fsType; refuse subsetting when fsType 0x100 is set or the licence is ITF FFL; `fvar` table for variable fonts; WOFF2 signature |
| **H-color** fixed brand colors (Q-color-01; class E) | hex, RGB, OKLCH, Pantone reference, Figma variables JSON, CSS | locks them as seeds (the "brand hue must be exact" flag, LEVERS A7); builds ramps and roles around them; proposes the nearest passing step wherever a locked color fails a text role | candidates from the logo or brand book; otherwise hues suggested from the personality (blue reads competent, red exciting [S-L06-072]), labeled a starting point | none | contrast of every role in every mode; gamut check for P3 values [inferred] |
| **H-motion** motion signature and rich media (Q-img-06) | Lottie JSON, dotLottie, Bodymovin export, Rive `.riv`, glTF or GLB, USDZ | places them in the one authored motion moment the direction allows; wires a reduced-motion alternative | motion from the system's tokens only; commission a motion designer; community Lottie assets under their stated licences | stated licence per community asset | Lottie validates against its JSON Schema; layer types lottie-web cannot render are rejected; size, fps and duration budgets; glTF Validator; a reduced-motion twin exists [S-L17-541] to [S-L17-558] |
| **H-motif** patterns, textures, gradients, signature shape (Q-img-07, Q-shape-05) | SVG patterns, gradient definitions, shape SVG | stores them as brand-expression tokens and assets with allowed surfaces (hero moments only, per the Expression dial) | commission, or ship none: decoration standing in for content reads as generic [S-L17-004] [S-L17-021] | the owner's rights to the motif | text contrast over gradients and textures; usage limited to allowed surfaces |
| **H-sound** UI sounds and sonic logo (Q-motion-08) | Apple: Linear PCM, IMA4, µLaw or aLaw in .aiff, .wav or .caf under 30 s; Android: Ogg, WAV, MP3, AAC, FLAC | maps sounds to semantic events; respects silent mode | stay silent (the norm on the web and in productivity apps); platform system sounds; commission a sound designer; no verified open UI-sound library exists [S-L17-553] [S-L17-555] | licence per file | codec, container and duration checks; loudness normalization [inferred] |
| **H-haptic** custom haptics (Q-motion-09; class T) | Apple AHAP JSON; Android `VibrationEffect` compositions | maps semantic haptic tokens to platform constants | system patterns first (Apple notification, impact, selection; Android `HapticFeedbackConstants`) [S-L17-547] | none | AHAP values 0-1 (out-of-range values are clamped silently, so warn); fallback where a primitive is unsupported |
| **H-voice** voice and tone guide (Q-voice-01; class T) | PDF, Markdown, doc export, existing product copy | extracts voice attributes and rules; drafts the tone matrix and microcopy in that voice | the model drafts traits and examples from the sliders, labeled draft until a content designer or the owner reviews them (22% of teams have no content designer [S-L11-030]); terminology stays owner input | copy read from a reference is never reused verbatim [S-L17-023] | readability lint; banned-word list; capitalization and mechanics applied consistently |
| **H-brandbook** brand guidelines PDF (Q-ref-01 `doc`, Q-brand-08) | PDF | extracts candidate colors from vector fills, font names and embedded logos; asks for the SVG master of any logo found | n/a | assets belong to the brand owner | PDF text, fonts, colors and fills are extractable; a PDF never becomes editable design layers [S-L17-569] [S-L17-571] |
| **H-icons** custom icons, pictograms, spot icons (Q-icon-01; T, with D for custom tiers) | SVG on the library's grid; SF Symbol template SVG; Android Vector Drawable; icon fonts converted to SVG (fonts blur and flash [S-L05-038]) | matches stroke, corners and size scale to the typeface (DC-L05-03, LEVERS B12); ships icons as components; maps to SF Symbols on Apple platforms | adopt an open library whose stroke and corners fit (Lucide, Phosphor, Tabler, Heroicons, Material Symbols); commission only the domain icons the library lacks, drawn on its template; AI icon tools as sketches only [inferred] | ISC, MIT or Apache notice carried into the build [S-L17-512] | viewBox matches the grid; consistent stroke; SF Symbol template validates; SVGO pass; licence file present; every meaningful icon has a label [S-L17-149] |

### 4.4 Tool hooks (tool-assisted blocks that are not identity assets)

| Hook (question) | What the model does | Named tools | Caveat | Check |
|---|---|---|---|---|
| **H-tokens** (Q-token-08, Q-tool-02) | `engine.py export` writes CSS, Tailwind, Swift and Compose itself; for teams that already run a pipeline it also writes a Terrazzo or Style Dictionary config (7.5) | Terrazzo (full DTCG 2025.10 with resolvers), Style Dictionary v5 (no resolver support yet), Tokens Studio; platform dynamic-color and material APIs (DC-L07-25) | only 40% of teams automate token sync [S-L17-347] | build output compiles; every semantic token resolves in every mode |
| **H-figma** (Q-tool-03, Q-tool-04, Q-token-07) | pushes through the remote Figma MCP or writes DTCG import files; pushes to Paper through its MCP (section 10) | `use_figma`, Figma's `figma-generate-library` skill, native DTCG import; Paper MCP; Penpot's native DTCG import | plan limits on modes and extended collections; canvas writes need a Full seat (7.6, 10) | collections within plan limits; scopes set, never "all scopes"; code syntax on every variable (DC-L07-19, DC-L07-20) |
| **H-comp** (Q-comp-01, Q-ai-01) | records the headless base and maps component specs onto it | Radix, Base UI, React Aria, the shadcn registry (shadcn's default base moved to Base UI in July 2026, BOARD L08 note) | AI surfaces and product-specific patterns change fast; review against WAI-ARIA APG | keyboard and ARIA behavior per component; state matrix complete |
| **H-dataviz** (Q-viz-01, Q-color-19) | themes the chart library from tokens (DC-L05-24) | chart libraries per DC-L05-22 | library defaults override tokens unless themed | chart palette passes color-vision-deficiency and contrast checks (DC-L05-23) |
| **H-a11y** (Q-gov-07) | exports automated checks and a manual walkthrough checklist per device class (DC-L14-14) | axe-core and exported lint; human screen-reader walkthroughs | automated tools catch only part of WCAG | automated checks in CI; walkthrough recorded (DC-L11-19) |

### 4.5 Every designer-owned and tool-assisted block, mapped to its hook

From L17 G3: all 7 D and 31 T blocks have a hook.

| Hook | Blocks (class) | Opens at |
|---|---|---|
| H-logo, H-appicon, H-favicon | `found.imagery.brand-marks` (D; size sets T) | Stage 03 (Q-brand-03); Stage 17 (Q-icon-06, Q-icon-08) |
| H-icons | `found.icon.tiers` (D); `found.icon.source`, `.naming`, `.delivery`, `.platform` (T) | Stage 17 |
| H-photo | `found.imagery.photo` (D) | Stage 18 |
| H-illus | `found.imagery.illustration` (D); `pat.empty` (T) | Stage 18 |
| H-motion | `found.imagery.rich-media` (D) | Stage 18 |
| H-motif | `found.imagery.motifs` (D); `found.shape.expressive` (T); `found.color.expressive` (E) | Stages 14 and 18 |
| H-sound | `found.sensory.sound` (D) | Stage 16 |
| H-haptic | `found.sensory.haptics` (T) | Stage 16 |
| H-type | `found.type.typeface.sourcing`, `.families`, `.delivery` (T) | Stage 10 |
| H-voice | `found.content.voice`, `.tone`, `.microcopy`, `.localization`, `pat.onboarding` (T) | Stage 19 |
| H-tokens | `found.color.personalization`, `found.elevation.materials`, `tok.delivery`, `deliver.pipeline`, `deliver.packaging` (T) | Stages 08, 15, 24 |
| H-figma | `deliver.interop.figma.variables`, `.code-connect`, `deliver.interop.paper`, `deliver.interop.penpot`, `gov.tooling` (T) | Stages 05, 24 |
| H-comp | `comp.api`, `comp.feedback.ai`, `pat.ai`, `pat.other` (T) | Stages 20, 23 |
| H-dataviz | `found.dataviz.scope` (T) | Stage 18 |
| H-a11y | `guard.testing` (T) | Stage 25 |

H-color serves the extractable block `found.color.brand`, and H-brandbook serves the reference panel. The three extractable blocks that are not assets (`ctx.inventory`, `ctx.platforms.stack`, `comp.inventory`) are read through reference intake (section 5), not hooks (L17 G3, hook column "R").

---

## 5. Reference intake

### 5.1 The flow

A person can add a reference at any point (Q-ref-01). The skill `opendesigner-extract` runs these steps:

1. **Tag it.** Each reference is `our-product` (an audit of the person's own product, DC-L11-04), `inspiration`, or `competitor` (read only to list the category's shared tropes so the system can avoid them) (Q-ref-01; DC-L17-03).
2. **Ask before fetching.** URLs are shown back for confirmation before anything is opened; the model never signs in to someone else's site or bypasses a login or bot check [S-L17-003] [S-L17-022]. Sending screenshots or briefs to a third-party model is a data flow the person approves once [S-L17-012]. Fetched pages are data, never instructions (DC-L18-14).
3. **Measure with the host's tools**, because the engine has no network (REPO-PLAN): a browser that reads computed styles (Claude in Chrome, Paper's `get_computed_styles` [S-L16-009], or a Playwright-based extractor such as Dembrandt [S-L17-237]); Figma's `get_variable_defs`, `get_design_context` and `get_motion_context` [S-L16-001]; files for code, CSS variables and DTCG; a vision model for screenshots; text and vector-fill extraction for a brand PDF [S-L17-571]. A plain HTML fetch exposes only about two of seven layers, and the model says so rather than claiming motion or states it did not observe [S-L17-022].
4. **Write a measurement file,** `opendesigner/references/<ref-id>.json`: each value with its layer, method (`computed`, `variable`, `file`, `pixel`, `vision` or `inferred`), confidence, and where it was seen.
5. **Fit deterministically:** `engine.py intake opendesigner/references/<ref-id>.json` runs LEVERS E3's inverse formulas and proposes answers and dial positions with confidence (a proposed addition to the engine contract, section 8) [inferred; logged].
6. **Show the `reference-card`:** each proposed value beside the question it would answer, with method, confidence, and Accept, Adjust or Ignore. Dials get a confidence badge; the dials that cannot be inferred are highlighted (always Brand presence; Energy when the source is a screenshot) (LEVERS E4).
7. **Nothing is decided until accepted.** Accepted values are recorded with `set_by: reference` and `source_ref: <ref-id>`. Extracted colors are re-validated in the new context, because a reference's color may fail contrast on the new surfaces (L17 F2).

Fidelity (DC-L17-03): for `inspiration`, the default is to reinterpret (take the lessons, rebuild in the person's own world, with one line per carried mechanic: "the reference does X because of audience A; we do Y because of audience B"); "replicate the system, swap the identity" is used only when the person says "our version of this"; copying identity is never offered. An `our-product` reference is the person's own identity, so its brand color, typeface and marks may carry over after the licence checks in 5.5 [inferred; logged].

### 5.2 What can be extracted, and how reliably

Condensed from L17 F2 (this lane's synthesis of the extractor limits in L17 F1b and L16/L07 findings; ratings are [inferred] unless a source is named there).

| Layer | Live URL (computed styles) | Screenshot | Figma file (MCP) | Code or tokens | Brand book (PDF) |
|---|---|---|---|---|---|
| Color values | high | medium (antialiasing, gradients and photos confuse sampling) | high | high | high for brand colors |
| Color roles | medium (inferred from usage) | low | high if variables are semantically named | high if tokens are tiered | medium |
| Typefaces | high for family names; the licence is not extractable | low (a guess) | high | high | high, often with licence notes |
| Type scale, weights, line heights | high | medium (ratios only) | high | high | medium |
| Spacing scale | medium-high (clustered samples) | low-medium | high with variables | high | rare |
| Radius, borders, shadows | high | medium (radius), low (shadows) | high | high | rare |
| Breakpoints, grid | high (media queries) | low (one width) | medium | high | rare |
| Motion | medium, and only with a live browser observing over time | none | partial (motion and timing variables) | high if motion tokens exist | rare |
| Component inventory and states | medium (DOM patterns); states need interaction | medium (types only); none for states | high (component sets, variants) | high | low |
| Icons and imagery | medium (files downloadable; licences unknown) | low | high | high | medium |
| Voice and tone | medium (the copy itself is never reused) | low | low | low | high if the book has a voice section |
| Intent, principles, audience, why | not extractable | not extractable | only if documented | only in ADRs or docs | partly |

The rule that follows: a reference is strong for surface values and weak for meaning, so OpenDesigner pre-fills the first and always asks for the second (L17 F2).

### 5.3 Mapping onto the dials

Reference intake is the generation formulas run backwards (LEVERS E): measure, fit, read off the dial positions, then let the person adjust with the same dials.

| Dial | Inferable | Measured from | Confidence |
|---|---|---|---|
| Roundness | yes | most common radius on buttons and inputs, looked up in the A5 bands; container and nested radii confirm | high on URL and Figma; medium on screenshots |
| Density | yes | body size, control and row heights, typical paddings (A3 bands) | high |
| Depth | yes | shadow layers and alpha, borders, surface lightness steps, backdrop blur (A6 bands) | high on URL and Figma; medium on screenshots |
| Colorfulness | yes | accent and surface chroma, count of accent hues, chromatic share of the screen | high |
| Warmth (color) | yes | neutral hue and chroma in OKLCH, nearest A8 anchor | high |
| Warmth (voice) | partly | capitalization, contractions | medium; needs enough copy |
| Energy | partly | durations (multiplier = median medium duration / 275ms), easing, overshoot, saturation, heading weight | medium on URLs; low on Figma unless motion is defined; none from screenshots |
| Expression | partly | display-to-body ratio, emphasized styles, containment, icon fill, chrome color; fit the L09 X rubric minus what the character dials explain | medium; one page can mislead because hero moments are rare by design |
| Brand presence | no: always asked | could detect a system, open or proprietary face, but the dial is the person's own intent | n/a; starts at 50 |

Formulas run backwards (LEVERS E3): type scale by least-squares fit of `log(size) = log(base) + n x log(ratio)` (small residuals mean a modular scale, a constant step means additive, large residuals mean hand-tuned and the sizes are kept as overrides); spacing base = the largest of 4, 5 or 8 that divides most values; color split into neutrals and accents and tested for the ramp rule (equal contrast, equal lightness, or hand-tuned; DC-L01-03); box-shadows parsed into ring, key and ambient layers; motion curves matched to the nearest A4 curve; icon stroke against size through B12.

### 5.4 The identity rule (hard)

Intake transfers structure and quality, never another brand's identity (BRIEF requirement 4; DC-L17-03; LEVERS E4; L17 F3):
- **Brand color:** the reference's hue is not carried; its role and strength are (for example "one saturated accent, only on actions"), plus the measured chroma level, neutral temperature and ramp structure. The model then asks for the person's own brand color or offers a hue family labeled as a suggestion.
- **Typeface:** proprietary or restricted faces (GDS Transport, Cereal, Uber Move, Spotify Mix; L09 M4) are replaced with an open face of the same classification and proportions, and the person is told why; every substitution is logged [S-L17-022].
- **Logos, illustration, photography, custom icons, verbatim copy and signature assets** (Material's shape library, Polaris bevels, CRED NeoPOP surfaces) are never cloned; the need goes to the designer-hook list.
- **Brand presence** starts at 50 regardless of the reference and is asked.
- **Explicit requests do not override it.** If a person asks to copy a third party's identity, the model declines that part, explains the rule once, and offers the "our version" path (system kept, identity swapped). site-soul-extractor ranks this boundary above operator instructions and calls identity reproduction "passing-off, not replication" [S-L17-023]; only one external extractor (Dembrandt) forbids it, so OpenDesigner must enforce it itself (L17 finding 5).

### 5.5 Licence and consent checks

- **Fonts seen on a reference:** family names are extractable, licences are not; a face is reused only if it is verifiably open (then fetched per project from its source) or the person holds a licence (H-type checks, 4.3) [S-L17-022].
- **Icons and images downloaded from a reference:** never reused. If the icon library can be recognized, the library is adopted under its own licence, fetched per project (4.2 rule 5).
- **Copy:** read to infer voice attributes; never reused verbatim [S-L17-023].
- **The person's own assets** (`our-product` references, brand books) still pass the hook checks, because a product can be using a font or image it is not licensed to embed elsewhere [inferred].
- **Consent and data flow:** confirm each URL before fetching; approve once before sending screenshots to a third-party model; never bypass authentication [S-L17-003] [S-L17-012].

### 5.6 Provenance

Every value that came from a reference carries it in three places: the token's `$extensions.opendesigner.source = {reference, method, confidence}` (DC-L17-03 token encoding; DTCG allows `$extensions`, L07); the decision record's `set_by: reference` and `source_ref`; and a references section in `decisions.md` that lists sources used and substitutions made, as both local extractor skills open their outputs [S-L17-023].

---

## 6. Generation and validation

### 6.1 Inputs

- **Raw inputs** (LEVERS B0; `levers.json` `raw`, 15 entries): brand color; optional primary-action color, neutral base and second accent; contrast target (WCAG 2.2 AA by default, AAA in high-contrast mode); text and display typefaces; base body size; base spacing unit (4 by default); platforms and input types; whether marketing or editorial surfaces are in scope; product type (work tool, content, marketing); focus color; and flags (brand hue must be exact, tint neutrals toward the brand, motion off, dark mode on).
- **Eight dials, 0-100, 50 = sensible default** (LEVERS A0): three posture dials, **Expression**, **Brand presence** and **Density**, and five character dials, **Energy**, **Roundness**, **Depth**, **Colorfulness** and **Warmth**. Untouched character dials follow the posture dials through the coupling rules (LEVERS A0; `levers.json` `coupling`); touching a dial detaches it. The coupling coefficients are [inferred] and are the weakest mappings in LEVERS.
- **Macros and presets:** brand adjectives (Playful, Serious, Friendly, Authoritative, Minimal, Rich, Premium, Everyday, Modern, Heritage, Bold, Deferential) are offsets on the dials, and opposite pushes are shown as a conflict, never averaged (LEVERS A9); style presets (Flat 2.0, Material tonal, Glass, Neo-brutalist, Soft, Maximal) are named dial settings (LEVERS A10).
- **Detachable overrides** for what the dials do not reach: variable-font weights such as 450, 510, 590 or 653, a separate primary-action color, signature assets, a hand-set type scale (LEVERS C findings). Raw values are editable only through an explicit detach, so a detached value is visible as such (DC-L16-14, DC-L16-15).

### 6.2 From dials and inputs to tokens

`engine.py generate` reads `state.json` and the skill's own copy of `levers.json` and writes DTCG 2025.10 tokens plus a resolver (REPO-PLAN engine contract; file layout in 7.4). The formulas are specified in LEVERS section B and encoded in `levers.json` `formulas` (keys `color`, `type`, `space`, `radius`, `elevation`, `motion`, `icon`, `density`); this spec does not restate them:

| Foundation | Rule (LEVERS) | In one line |
|---|---|---|
| Color ramps | B1 | 12 contrast-indexed steps in OKLCH with Radix-style step jobs; step 8 solved at 3:1, step 11 at 4.5:1 and step 12 at 7:1 against the background; chroma from Colorfulness; the brand color anchored at the nearest step |
| Neutrals | B2 | hue from Warmth or the brand; small chroma tint at middle steps, near zero at the ends |
| Roles and states | B3 | semantic roles alias ramp steps; hover +1 step, pressed +2; state layers when the color is unknown |
| Dark mode | B4 | a separate mapping by role, never an inversion |
| Contrast | B5 | WCAG 2.2 enforced, no rounding; APCA advisory only |
| Type scale | B6 | `base x ratio^n` rounded to whole pixels; ratio from Expression capped by Density; display reach from the marketing-surfaces input |
| Line height, tracking, weights, scripts | B7 | ratio by size rounded to 4px; per-script line-height and tracking rules |
| Spacing | B8 | `unit x [0, 0.5, 1, 1.5, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24]` without non-integers (24 adds the 96 step; section 11); inner spacing always below outer |
| Radius | B9 | control radius from the Roundness bands; role ratios; nested radius `max(outer - padding, smallest step)`; focus radius = radius + offset |
| Elevation | B10 | band from Depth picks the model (borders, ring, tonal, shadow ladder, materials) |
| Motion | B11 | duration ladder scaled by Energy on medium and longer steps; springs stored as damping and stiffness, emitted as duration and bounce plus a sampled CSS `linear()`; reduced motion as a mode |
| Icons | B12 | stroke follows adjacent text weight and size |
| Density | B13 | a semantic-layer mode (compact, comfortable, spacious); primitives and target minimums never change |

Every generated token carries `$description` (its intent, from the question's Use / avoid line) and `$extensions.opendesigner` with its source (`formula`, `default`, `person`, `reference` or `asset`) and the decision ids behind it, so any value can be traced to `levers.json` or a card (REPO-PLAN shared conventions) [inferred encoding]. The 13 look recipes in LEVERS C (Material 3 Expressive to Airbnb) are test fixtures: the engine must reproduce each recipe's generated signature (section 13).

### 6.3 Validation order

1. **By construction:** `generate` cannot emit a text step below its contrast target, a hit area below the input minimum, or a missing reduced-motion or opaque twin (LEVERS D1).
2. **Deterministic validation:** `engine.py validate` checks every foreground and background pair in every mode (no rounding: 4.499:1 fails), non-text contrast at 3:1, target minimums by input type, token references resolving in every mode, orphan tokens, scale monotonicity and on-scale values, nested radii, reduced-motion and reduced-transparency twins, block coverage statuses, and the exported lint rules. It exits 1 on errors and cites the rule for each finding (REPO-PLAN; DC-L18-11).
3. **Model critique,** only on a passing system (P7): a fixed rubric, 0-10 per layer, more than one run (3.2 P7).
4. **The person** decides everything in LEVERS D3.

### 6.4 What is enforced, warned, or left to the person

| Level | What | Examples | Source |
|---|---|---|---|
| **Enforced by construction** | the generator cannot produce a violation | text contrast 4.5:1 and 3:1 large, 7:1 in high contrast; non-text 3:1; automatic on-color text; target minimums keyed to input (24 CSS px web AA, 44pt iOS, 48dp Android, 56-66 for remote and gaze, 76dp in cars); focus ring 2px with 2px offset and 3:1 change; reduced-motion and reduced-transparency modes; text scaling to 200% with min-heights; inner spacing below outer; three text colors and few weights; concentric nested radii; per-script type rules; native behavior on every Brand setting; default loading, empty, error and success behaviors; driving rules when cars are in scope | LEVERS D1; L14 invariants; DC-L14-11 |
| **Lint error** (blocks export) | usage that breaks a hard rule, usually on detached or authored values | a target under 24x24 CSS px without a spacing exception; a field with no programmatic label; meaning shown by color alone; a dialog with no way to dismiss; a pre-checked consent box; any contrast failure on a detached value | LEVERS D2; L13 E1 level 2 |
| **Warning** (flag; the person may override) | practitioner consensus, stated as such in the UI | more than 3 type sizes or more than one primary action per view; accent over about 15% of a view [inferred threshold]; bounce above 0.2 without the Playful macro; Colorfulness above 75 with Density above 66; minimal signifiers with Density above 33; Expression above 66 on finance; equal nested radii; glass in the content layer; the neumorphic preset; standard transitions over 500ms; placeholder-only labels; button labels over 4 words; delete with neither undo nor confirm; APCA below Lc 75 on body text (advisory) | LEVERS D2 |
| **Left to the person** | recorded, never decided | brand personality and dial positions; information architecture and labels; what matters most on each screen; undo versus confirm per action; convention versus novelty for the core differentiator; tone and celebration; logo, illustration, photography and custom icons; golden ratio, color-wheel harmonies and 60-30-10 as optional presets only | LEVERS D3 |
| **Never automated** | misapplied "laws" the product refuses to encode | no 7-item cap on navigation; no automatic option removal for Hick's law; no nag features from Zeigarnik; no strategic delays from the Doherty threshold; no attractiveness score as a usability signal; no hard result caps from choice overload | LEVERS D3; L13 E2 |

**Waivers** [inferred; logged]: a generated value cannot violate an enforced rule, so there is nothing to waive. An accessibility lint error on a detached or authored value blocks export in every critique mode unless the person cites a WCAG-defined exception (for example the spacing, equivalent, inline, user-agent and essential exceptions of SC 2.5.8) and gives a reason; the waiver is recorded in the decision log and listed in the coverage report and the rationale one-pager. Warnings and taste lint can be waived with a reason. The critique strictness question (Q-pref-01: silent, coach, strict, plus a metrics panel; DC-L15-11) changes only how taste and hierarchy findings are shown and whether they block, never the accessibility floor. This reconciles DC-L17-07 ("accessibility rules fail") with L13 E1's written-reason override (section 11).

### 6.5 Anti-generic guardrails

The generic AI look is admitted by vendors and measured by NN/g [S-L17-120] [S-L17-218] [S-L17-021]; the fix is forcing an explicit decision per block and feeding the system itself, not a better prompt [S-L17-121] [S-L17-124]. OpenDesigner ships gstack's slop catalog, the "three looks" calibration and role-scoped font lists as lint rules with ids, severity `warn`, a one-line reason, and per-project waivers; never as bans (DC-L17-07; L17 A3). The rule ids can align with impeccable's engine, which is Apache-2.0 [S-L17-016] [inferred]. In the interview the model names a generic look once, at the moment a choice lands in it, and then respects the person's decision (L17 A2 item 3: the coherence check never blocks).

### 6.6 The validation report

`engine.py validate --json` returns one finding per rule violation: `{rule, severity: error|warn|info, where: token path or component/state/mode, measured, threshold, evidence: DC or S id, fix}`; without `--json` it prints the same grouped by severity in plain sentences. The model reads the JSON, never re-derives the numbers, and quotes the rule's reason when it tells the person (DC-L15-11: messages that name the principle teach the vocabulary [S-L15-070]).

---

## 7. Outputs

### 7.1 What lands in the person's repo

The canonical source of a system is `opendesigner/state.json` plus the DTCG tokens it generates; DESIGN.md, PRODUCT.md, platform code, Figma and Paper are generated views (DC-L16-02, DC-L18-10; DECISIONS 18:59 entry, kept). Code-canonical remains an option for mature systems (Q-tool-01; section 9).

```
<project>/
├── DESIGN.md                     readable view of the system for people and agents (7.2)
├── PRODUCT.md                    product truth: audience, purpose, surfaces, principles (7.3)
├── AGENTS.md                     gets a short OpenDesigner block, after asking (7.12)
└── opendesigner/
    ├── state.json                answers, dials, raw inputs, overrides, statuses (7.10)
    ├── decisions.md              append-only decision log (7.9)
    ├── RATIONALE.md              one page for the team (7.11)
    ├── coverage.md               every block's status and the named remainder (7.12)
    ├── assets.json, briefs/      asset ledger and briefs for missing assets (4.2)
    ├── references/<ref-id>.json  reference measurements (5.1)
    ├── tokens/                   DTCG 2025.10 files and one resolver (7.4)
    ├── build/                    css/, tailwind/, swift/, compose/, figma/, paper/ (7.5-7.7)
    ├── components/<name>.md      component doc pages (7.8)
    ├── lint/                     exported lint rules (7.12)
    └── preview.html              specimen of every token and the v1 components
```

DESIGN.md and PRODUCT.md sit at the project root because gstack, impeccable, Stitch and Claude's artifact design skill look for them there [S-L17-004] [S-L17-020] [S-L17-213] [S-L18-043]; everything else stays in `./opendesigner/` (REPO-PLAN; `--dir` overrides) [inferred; logged].

### 7.2 DESIGN.md: the exact contract

DESIGN.md is the readable view that later sessions and other models read first. It follows Google's open DESIGN.md format (v0.4.0, alpha, Apache-2.0) so other agents and its linter can read it, and adds the sections that format lacks (it has no keys for modes, motion, icons, imagery, voice or breakpoints) [S-L17-213] [inferred from the schema in L17 E1]. It is a draft format, so DTCG stays canonical (COMMUNITY-SIGNAL [S-L00-052]; DC-L18-10).

**Rules** [inferred; logged]:
- Generated by `engine.py design-md` from `state.json`, the tokens and `decisions.md`, after every change. Never edited as a source.
- Hand-written prose survives regeneration only inside `<!-- od:keep -->` ... `<!-- /od:keep -->` blocks, one allowed at the end of each section. The engine stores a hash of every generated file in `state.json`, so the extend skill detects any other hand edit and turns it into proposed decisions instead of losing it.
- **Front matter:** only Google's keys (`version`, `name`, `description`, `colors`, `typography`, `rounded`, `spacing`, `components`), filled from the default mode's semantic tokens, with `{colors.primary}`-style references. No extra keys, so Google's linter (broken references, AA contrast, missing primary, orphaned tokens, section order) can pass.
- **Body:** exactly these level-2 headings, in this order; a section that does not apply keeps its heading with one line saying why (so "not applicable" is visible, principle 6). Sections 1-8 are Google's canonical sections; 9-17 are OpenDesigner's.
- **Inside every section:** an *Intent* paragraph (the decision and its reason, written from the decision log), a *Tokens* table (token path, light value, dark value, use), *Use / avoid* bullets, and the decision ids it rests on.

| # | Heading | Contents |
|---|---|---|
| 1 | `## Overview` | one-line product description, audience, the memorable thing, surfaces and their modes, ranked principles, the chosen direction and its dial positions, platforms; a line saying the tokens in `opendesigner/tokens/` are canonical and this file is generated |
| 2 | `## Colors` | brand color and its role, ramps and how steps are built, semantic roles, interaction states, dark-mode rule, the step-distance contrast table (LEVERS B5), chart palette pointer |
| 3 | `## Typography` | faces with licence status, scale (size, line height, tracking, weight per style), per-script rules, text scaling |
| 4 | `## Layout` | spacing ladder and semantic aliases, density modes, breakpoints, grid and containers, target sizes |
| 5 | `## Elevation & Depth` | depth model, surfaces, shadows or materials with solid fallbacks, stacking layers, borders |
| 6 | `## Shapes` | radius scale and roles, nested-radius rule, focus-ring geometry, any signature shape |
| 7 | `## Components` | v1 inventory with status labels, component-token overrides, the contested policies chosen (disabled submit, toasts, validation timing, undo versus confirm), links to `opendesigner/components/` |
| 8 | `## Do's and Don'ts` | the enforced rules, lint errors and warnings in plain sentences; waivers with their reasons |
| 9 | `## Motion` | duration ladder, easings, springs, reduced motion, haptics and sound |
| 10 | `## Modes and Themes` | theme axes and contexts, the resolver, what a brand or client may override |
| 11 | `## Iconography and Imagery` | icon library, stroke, sizes and labels; logo rules; illustration, photography and motifs, each with its asset status; placeholders labeled |
| 12 | `## Content and Voice` | voice traits, tone by situation, capitalization, reading level, word list; "draft" if unreviewed |
| 13 | `## Accessibility` | the standard, what the system guarantees versus what product teams own (DC-L11-19), the test matrix per device class (DC-L14-14) |
| 14 | `## Platforms and Devices` | platforms, posture, device classes and inputs, native behaviors kept |
| 15 | `## Decisions` | the 10-20 highest-reach decisions with id, value, how set and reason; link to `opendesigner/decisions.md` |
| 16 | `## Open Items` | assumed owner inputs, pending assets with owners, waivers, questions left on defaults |
| 17 | `## For Agents` | read this file, PRODUCT.md and the tokens before any visual work; use tokens, never raw values; do not change a locked decision without asking; after a change run `engine.py generate` then `validate`; how to extend (section 9) |

### 7.3 PRODUCT.md

Product truth kept apart from the visual system, because it has different readers and changes at a different rate (L17 A3 [S-L17-020]). Generated from `state.json` with the same keep-block and hash rules as DESIGN.md. Headings, in order: `## Product`, `## Audience`, `## Surfaces` (each with its Persuade, Operate, Read or Experience mode), `## Memorable Thing`, `## Principles` (ranked, with the tie-break rule), `## Constraints` (accessibility target, platforms, OS floors, legal or brand limits), `## Scope` (in and explicitly out, DC-L11-02), `## Team and Governance`. An existing PRODUCT.md is read as prior answers in P0 and rewritten into this shape only with consent [inferred].

### 7.4 DTCG 2025.10 tokens and the Resolver

DTCG 2025.10 is a stable Community Group format (28 Oct 2025); modes are not in the Format module but in the separate Resolver module (sets, modifiers, contexts, resolution order) [S-L07-002] [S-L07-004].
- **Files:** one per tier and mode plus one resolver, which maps one-to-one onto Figma's one-file-per-mode import and onto resolver contexts (DC-L07-09): `primitives.tokens.json`; `semantic.color.light.tokens.json` and `.dark` (plus `.light-hc` and `.dark-hc` when high contrast ships); `semantic.density.<compact|comfortable|spacious>.tokens.json` when density is an axis; `motion.<standard|reduced>.tokens.json`; `component.tokens.json` only when needed; `opendesigner.resolver.json`.
- **Tiers:** primitive and semantic, with component tokens added only for components a brand must restyle independently or values reused by three or more related components (DC-L07-01, DC-L07-02).
- **Axes:** color scheme and contrast (high contrast as a layered override), density only for data-dense products, motion (standard and reduced) always, brand only with a real second brand; at most three orthogonal axes; a `context` modifier separate from `platform` for device classes (DC-L07-15, DC-L07-17; BOARD L14 note).
- **Values:** colors as 2025.10 color objects in OKLCH with a hex fallback (DC-L07-10); dimensions in px, converted to rem on web export where wanted (DC-L07-11; ONTOLOGY contradiction 3); line height as a unitless number; durations and cubic-bezier easings as DTCG types (DC-L07-14).
- **Extensions:** DTCG has no types for springs, assets, aspect ratios, breakpoints, blur or behavior rules, so they live under `$extensions.opendesigner` (ONTOLOGY open gaps; BOARD L04/L07 and L05/L07 notes); the extension schema is written with the engine (R2) [inferred].
- **Intent and change:** `$description` carries each token's intent; retired tokens get `$deprecated` with a replacement, never deletion (DC-L07-23 [S-L18-325]).
- **Names:** lowercase path segments, no dots or braces in names (DC-L07-06, DC-L07-09).

### 7.5 Platform code

`engine.py export --format css|tailwind|swift|compose|dtcg` (REPO-PLAN) writes into `opendesigner/build/`: CSS custom properties with one scope per resolver context (a `[data-theme]` attribute or media query per context); a Tailwind theme; Swift and Compose token files using platform conventions (continuous corners on iOS, DC-L04-04; sp and Dynamic Type mappings, DC-L02-21). For teams that already run a pipeline, `export` also writes a Terrazzo config (full 2025.10 support including resolvers) or a Style Dictionary v5 config (no resolver support yet, so one build per mode combination) (DC-L07-25; L07 A9).

### 7.6 Figma variables

- **Structure** (DC-L07-18 to DC-L07-21): a hidden Primitives collection; Semantic color (light, dark, and high contrast where used); Semantic dimension (density or breakpoint); Motion with a reduced mode. Every semantic variable is scoped to the properties its name implies (never "all scopes"), primitives are hidden, code syntax is generated from the same name transform as the code export, and composites (typography, shadows) become styles: "variables for values, styles for bundles".
- **Plan limits** (L07 A6 [S-L07-011] [S-L07-014]): Starter lists no modes; Professional allows 10 modes per collection; Organization 20; Enterprise unlimited with extended collections; the REST API caps a collection at 40 modes, and REST variable writes need Enterprise. The engine compares the resolver's mode count per collection with the plan recorded in Q-tool-03 and warns before export (DC-L07-27).
- **Import constraints** (L07 A7 [S-L07-011]): one mode per file; colors in sRGB or HSL only; dimensions in px only; durations in seconds; no composites. So `export --format figma` writes one DTCG file per collection and mode, converts OKLCH to sRGB and flags out-of-gamut colors, and lists the styles to create. Figma now has timing and easing variables (Config 2026; DC-L07-14).
- **Writing** through the remote MCP is covered in section 10.

### 7.7 Paper tokens

Paper tokens are CSS variables (color, radius, spacing, container, breakpoint, font family, weight, size, line height, letter spacing) with no modes, no shared libraries and no DTCG [S-L16-018]. `export --format paper` writes the default mode as a token set for `create_tokens` or `set_tokens`, and an HTML specimen per mode in which the other modes set their CSS variables inline, rendered as labeled artboards; shadows and motion appear only in the specimens [inferred; logged].

### 7.8 Component docs

One page per v1 component in `opendesigner/components/<name>.md`, following the Carbon-style page (DC-L11-18, DC-L08-23) with the detail-panel fields (DC-L17-13): what it is; when to use; when not to (with the alternative); anatomy; variants; the state matrix; tokens used; accessibility (keyboard, ARIA pattern per WAI-ARIA APG, focus, target size); content rules (label length, capitalization); behavior spec (trigger, rules, feedback, loops and modes; DC-L13-12); platform notes; status label (DC-L11-13) and changelog. YAML front matter (id, status, tokens used, decision ids) makes each page machine-readable (Q-dist-04 default: a machine-readable twin) [inferred format].

### 7.9 The decision log

`opendesigner/decisions.md` is append-only and ADR-style: superseded, never edited or deleted (DC-L11-12 [S-L18-342]). `engine.py set --why` appends one entry per decision:

```
### D-0014 · Q-shape-01 · shape.radius.control = 8
- set_by: chosen · locked: no · date: 2026-09-23 · supersedes: D-0006 · source_ref: none
- block: found.shape.radius · cards: DC-L04-02, DC-L09-01
- reason: a calm finance tool; 8px is the Polaris and shadcn control radius
- downstream: radius roles, nested radius, focus ring (DC-L04-03, DC-L04-05, DC-L04-09)
```

`set_by` is one of `chosen`, `confirmed_default`, `auto_default`, `assumed`, `delegated`, `reference`, `asset` (S1b's vocabulary extended; section 11) [inferred; logged]. The log also holds a plain-sentence summary after each stage (QUESTIONNAIRE protocol step 7), a references section with sources used and substitutions (5.6), and a waivers section (6.4).

### 7.10 state.json

REPO-PLAN defines the core: answers keyed by question id, dial values, raw inputs and asset-hook status. This spec fixes the shape [inferred]: `schema_version`, `engine_version`, `levers_version`, `mode`; `context` (product, audience, surfaces with modes, entry path, memorable thing); `answers` (`{Q-id: {value, set_by, locked, decision}}`); `dials` (`{name: {value, set_by, detached}}`); `raw`; `overrides` (detached token values with reasons); `blocks` (`{node id: pending | default | decided | not-applicable | awaiting-asset | assumed}`); `assets` (`{hook: have | commissioning | open-library | tool | placeholder | not-needed}`, details in `assets.json`); `references`; `taste` (per-project preferences); `hashes` (generated files, for drift detection). JSON, because models overwrite JSON less often than Markdown [S-L18-327].

### 7.11 The rationale one-pager

`opendesigner/RATIONALE.md`, written by the model from the decision log in P8 and refreshed after each extend session, for teammates, managers and designers who will not read the log (BRIEF requirement 10; DC-L17-10). At most one page, plain language, ids only in footnotes [inferred]:
1. **What we built,** in one paragraph.
2. **The five choices that shape everything** (the highest-reach decisions made: personality, platforms, direction, density, brand color role), each as "we chose X because Y; the main alternative was Z, and it would have meant W".
3. **What the rules guarantee** (contrast, targets, focus, reduced motion), one sentence each.
4. **What is still open:** assumed answers, pending assets with their owner, waivers.
5. **How to ask for a change:** who approves and what to run.
6. **For designers:** the briefs for missing assets and what is theirs to own.

### 7.12 Coverage, assets, lint and the agent pointer

- `coverage.md`: every block with status and source, a 0-10 score per layer with "what a 10 looks like", and the named remainder the person accepted (DC-L17-09).
- `assets.json` and `briefs/<hook>.md`: the ledger (4.2) and one brief per missing asset, written so a designer can act without reading the system (L17 I2 Stage 3).
- `lint/`: rules generated from the tokens for the person's CI: a stylelint strict-value config, the behavior rules (target size, labels, one primary action) and the anti-generic rules, plus a DESIGN.md lint step when Google's CLI is installed (DC-L18-11, DC-L11-24; L13 E3).
- **Agent pointer:** after asking, a short block appended to the project's AGENTS.md (or CLAUDE.md when the project has no AGENTS.md import): "Design system: read DESIGN.md, PRODUCT.md and opendesigner/tokens before visual work; use tokens, never raw values; ask before changing a locked decision; run `engine.py validate` after changes." CLAUDE.md is context, not enforced configuration, which is why the validator and lint exist [S-L18-329] [S-L17-004].

---

## 8. Repo architecture

### 8.1 Layout

The repository follows `_coordination/REPO-PLAN.md` (built from L18 I1); this section does not repeat the tree. In short: `skills/` is the single source of truth in the portable Agent Skills format; `.agents/skills/` and `.claude/skills/` are generated copies made by `tools/sync_skills.py`, with a CI check for drift, because Claude Code reads only `.claude/skills` while Codex, Cursor, Copilot, Gemini CLI and Zed read `.agents/skills`, and symlinks break on Windows and in zips (DC-L18-02 [S-L18-211] [S-L18-251]); `AGENTS.md` (under 200 lines) is the canonical agent entry and `CLAUDE.md` and `GEMINI.md` import it with `@AGENTS.md` [S-L18-211] [S-L18-213]; two manifests share one version number, `plugin.json` (Agent Plugins 1.0, for Codex, ChatGPT, Cursor, VS Code, Copilot and Kiro) and `.claude-plugin/plugin.json` plus `marketplace.json` (the repo doubles as a Claude marketplace) (DC-L18-03); `data/` holds chunked knowledge built from `synthesis/` by `tools/build_data.py`; `examples/` holds complete worked systems; `chatgpt-project/` holds instructions plus at most five knowledge files for ChatGPT Projects, the only zero-install path for Free users [S-L18-126]; release zips of each skill serve claude.ai upload [S-L18-002]; `research/`, `synthesis/` and the rest of the evidence base stay unchanged. Custom GPTs are not built, because they retire on 11 Dec 2026 [S-L18-118].

### 8.2 The skills

Four skills, as in REPO-PLAN. Budgets for every skill: SKILL.md under 500 lines and about 5k tokens, portable frontmatter only (`name`, `description`, `license`, `compatibility`, `metadata`), reference files one level deep and loaded on demand; the model never needs more than one stage file plus the state file to ask the next question (DC-L18-04 [S-L18-050] [S-L18-003]). Because claude.ai installs each uploaded skill separately [S-L18-001], `tools/sync_skills.py` copies `engine.py` and the reference data a skill calls into that skill, so every skill runs on its own [inferred; logged].

| Skill | Job | Inputs | Outputs | Knowledge it reads |
|---|---|---|---|---|
| **`opendesigner`** (router) | Runs the whole interview (P0-P8): mode, pacing, the surface ladder, gates, critique and coverage, the output contract; hands off to the other three. Triggers include "create a design system", "set up design tokens", "review my design system" | the person's answers and examples; the repo; `opendesigner/state.json` if present | `state.json`, `decisions.md`, tokens, DESIGN.md, PRODUCT.md, RATIONALE.md, `coverage.md`, `assets.json` and briefs, `preview.html` | `SKILL.md`; `references/rules.md` (interview rules: QUESTIONNAIRE protocol, L18 F, 3.3-3.4 here); `references/stages/<nn>-<slug>.md` (one per stage, from `questionnaire.json`); `references/hooks.md` (section 4); `references/guardrails.md` (LEVERS D, L13 E2, anti-generic lint); `references/levers.json`; `references/blocks.json` (ontology nodes with class, hook and cards, for the block map and coverage); `references/graph.json` (fan-out and downstream per decision, for pacing and "what this changes"); `assets/templates/*.html` (14 templates, 3.6); `assets/output/*` (DESIGN.md, PRODUCT.md, RATIONALE.md, decisions.md, state.json and AGENTS-snippet templates); `scripts/engine.py` |
| **`opendesigner-extract`** | Reference intake (section 5): consent, measurement with host tools, deterministic fitting, the reference card, the identity firewall | URL, screenshot, Figma link, repo or CSS or DTCG files, brand PDF, each tagged our-product, inspiration or competitor | `opendesigner/references/<ref-id>.json`; proposed answers and dial positions marked pending; `reference-card` payload; substitution log | `references/intake.md` (what to measure per source, reliability table 5.2, identity rule 5.4, licence checks 5.5); `references/levers.json` (inverse formulas, LEVERS E); `scripts/engine.py` (`intake`) |
| **`opendesigner-extend`** | Later sessions (section 9): the start-up routine, changes with downstream preview, superseding records, audits of an existing OpenDesigner system, capture-back from Figma or Paper as decision forks | an existing `opendesigner/` folder; the change request; optionally a Figma or Paper file to compare | superseding decisions; regenerated tokens and views; a `diff` page; an updated RATIONALE.md | `references/extend.md` (routine, lock and supersede rules, drift handling); the stage file for the affected block; `references/graph.json`; `references/guardrails.md`; `scripts/engine.py` |
| **`opendesigner-export`** | Platform code, Figma and Paper mirrors, lint export (sections 7.5-7.7, 7.12, 10) | tokens and `state.json`; the design tool and plan (Q-tool-03); connected MCP servers | `opendesigner/build/*`; confirmed writes to Figma or Paper; `lint/` | `references/export.md` (Figma collection structure, plan limits, import constraints, `use_figma` limits; Paper token types and limits; pipeline configs); `scripts/engine.py` (`export`) |

Review and critique are not a separate skill: the router runs them at P7 and the extend skill runs them for audits. gstack keeps review separate [S-L17-008], so a fifth skill can be split out if trigger evals show the router missing review requests (section 13) [inferred].

### 8.3 The engine contract

REPO-PLAN defines `init`, `set`, `generate`, `validate`, `export` and `preview`, plus `design-md`, all run from the person's project, stdlib only, no network, with state in `./opendesigner/` unless `--dir` is given. This spec adds or pins down [inferred; logged]:
- **`intake <measurements.json>`** (new): runs LEVERS E3's inverse formulas and prints proposed answers and dial positions with confidence, stored as pending until accepted (5.1).
- **`design-md`** also renders PRODUCT.md, writes both to the project root, keeps `od:keep` blocks, and records file hashes in `state.json` (7.2, 7.3).
- **`set`** accepts the `OD:` paths (question ids, `dials.<name>`, token paths), `--why`, `--lock` and `--set-by` (default `chosen`), and appends to `decisions.md` in the 7.9 format.
- **`validate --json`** returns the 6.6 report and also reports coverage (every block's status) so P7 needs no second tool.
- **`export --format figma`** checks mode counts against the recorded Figma plan (7.6).
- The engine is deterministic: the same `state.json` and `levers.json` produce byte-identical tokens on any machine, which is what lets different models extend the same system (section 9).

### 8.4 Knowledge build

`tools/build_data.py` turns `synthesis/` into `data/` (ontology with classes and hooks, graph with fan-out and downstream, levers, one question file per stage, hooks, pacing) and copies what each skill needs into its `references/`. `data/pacing.json` holds the time-weight rule and its thresholds (DC-L18-08). `data/` is also the source for the Phase 2 MCP server's resources, so the skill and the server never disagree (DC-L18-04). The build fails if a question, block or hook in the synthesis files has no destination, which keeps "nothing missed" true for the package itself [inferred].

---

## 9. Harmony and extension across sessions and models

**What keeps a system coherent,** ranked by strength of evidence (L18 G): a closed, structured token source referenced by name (DTCG 2025.10 with `$description` and `$deprecated`) [S-L18-324] [S-L18-325]; retrievable component docs and examples, which helped most in the one measured evaluation (Sanity's, single-vendor, so indicative) [S-L18-332]; deterministic gates rather than advice [S-L18-323] [S-L18-329]; one short always-loaded context file that routes to the rest (the AGENTS.md pointer to DESIGN.md) [S-L18-330]; rationale plus an append-only decision log [S-L18-342]; a start-of-session routine [S-L18-327]; version-to-version drift checks [S-L18-334]; and a fresh-context visual review [S-L18-300].

**The extend routine** (skill `opendesigner-extend`; DC-L18-12; L17 I2 Stage 10):
1. Read `state.json`, `decisions.md`, DESIGN.md, PRODUCT.md, the tokens, and the git log since the last engine run. Never rely on chat memory.
2. Run `engine.py validate`. Compare file hashes: hand edits to generated files become proposed decisions for the person to accept, not silent losses.
3. List locked decisions and anything still `assumed`, `delegated` or `auto_default` that the change touches.
4. Ask only about what is new. Show the change on the block's detail panel with every downstream block it moves, in every mode, before committing (the `diff` template).
5. If the request conflicts with a locked decision or changes the person's stated direction, say so and ask before superseding (a user challenge, [S-L17-015]).
6. Write superseding records (`supersedes: D-...`), regenerate, validate, refresh DESIGN.md, PRODUCT.md and RATIONALE.md, and show the diff.

**Across models.** The engine is deterministic, the state is plain JSON, questions and decisions have stable ids, the `OD:` grammar is the same in every host, and `set_by` is honest about what was chosen versus defaulted. So Claude, ChatGPT or Codex, given the same files, produce the same tokens and can continue each other's work without the transcript [inferred from principle 7 and 8.3]. Interviewing in one session and building screens in a fresh one keeps the build context clean [S-L18-300].

**Across people.** The governance answers (Stage 25) are written into PRODUCT.md and applied by the extend skill: a fast lane for fixes, icons and docs and a proposal lane for new components (DC-L11-11); decision records as ADRs (DC-L11-12); status labels (DC-L11-13); semantic versioning (DC-L11-14); deprecation with `$deprecated`, a replacement and a migration note (DC-L07-23, DC-L11-15). Changes land as pull requests with the visual diff page (DC-L16-09).

**Typical extensions.**
- *A new component:* run P5 for that component only: states matrix from existing semantic tokens, component tokens only when DC-L07-02's conditions hold, validation, a doc page.
- *A new platform, brand or mode:* a new resolver context; the engine regenerates; the mode count is checked against the Figma plan; a brand overrides only the named brandable tokens, and if brands differ in more than about 20% of semantic tokens they are separate themes (DC-L07-16).
- *A new OpenDesigner release:* `state.json` records the engine and levers versions; when a newer formula would change existing tokens, the extend skill shows which ones and asks before regenerating [inferred].
- *Graduating to code-canonical:* for mature systems whose truth moves into the codebase, OpenDesigner switches to review mode: it reads tokens from the repo and proposes changes as pull requests (L16 G2 option 3; Q-tool-01).

**Taste memory** is per project only, visible and editable in `state.json`, and never applied silently to another project, so it cannot fight the anti-convergence rule (L17 A3).

---

## 10. Round trip with Figma, Paper and code

**One direction, fully automated.** The state and DTCG tokens flow out to code, Figma and Paper. Edits made in a design tool come back only as reviewed decision forks with provenance: the extend skill reads the tool (Figma `get_variable_defs`, Paper `get_computed_styles` or `get_tokens`), diffs against the tokens, and proposes `OD:set` lines; nothing overwrites the state silently (DC-L16-02, DC-L16-04 [S-L16-039]). Only 5% of teams run a two-way sync, so automating one direction completely comes first (DC-L11-16; DC-L16-02 heuristic).

**Figma.**
- *Reading* works through the local desktop MCP server (`http://127.0.0.1:3845/mcp`), which is read-only; on this machine it exposes `get_design_context`, `get_metadata`, `get_screenshot`, `get_variable_defs`, `get_motion_context` and `get_figjam`, and it needs a Dev or Full seat on a paid plan [S-L16-005] [S-L16-008]. It serves reference intake and capture-back.
- *Writing* to the canvas exists only on the remote server (`https://mcp.figma.com/mcp`): `use_figma` (Plugin API JavaScript that creates variables, styles, frames and components) and `generate_figma_design` (captures live UI as layers). It needs OAuth sign-in and a Full seat with edit rights; it is a free beta that "will eventually be a usage-based paid feature" [S-L16-001] [S-L16-002] [S-L16-007] [S-L16-022]. Limits today: 20 KB response per call, no image assets, only fonts uploaded to the account, components published by hand before Code Connect completes; Figma advises testing on a duplicate file [S-L16-002]. Clients that can write include Claude Code, Claude Desktop, Codex, Cursor, VS Code, Copilot CLI and Kiro; Gemini CLI cannot; ChatGPT's listing conflicts, so OpenDesigner treats it as unable to write until verified [S-L16-007] [S-L18-244] [S-L18-136] [inferred].
- *Without write access:* `export --format figma` writes DTCG import files, one per collection and mode, that the person drags into Figma on any plan with modes (7.6); REST variable writes need Enterprise (L07 A6).
- *Flow with write access:* detect the remote tools, offer the write, confirm the target (a new file or a duplicate), create collections and variables with scopes and code syntax, create styles for composites, place specimen and component-sheet frames, read back with `get_variable_defs` to verify, and record the push in the decision log (DC-L18-13).
- *Kunal's setup:* he has a Full seat; the remote server needs `claude plugin install figma@claude-plugins-official` and OAuth in an interactive session, and the desktop server should keep its own id so it does not shadow the remote tools (L16 A2 [S-L16-003] [S-L16-004]).

**Paper.** The Paper MCP runs inside Paper Desktop at `http://127.0.0.1:29979/mcp` and can read and write: `write_html`, `update_styles`, `create_tokens` and `set_tokens`, plus reads such as `get_computed_styles`, `get_jsx` and comment threads [S-L16-009] [S-L16-020]. Its tokens are CSS variables with no modes, no shared libraries and no DTCG [S-L16-018]; the free plan allows 100 MCP calls a week and Pro 1M [S-L16-010]; only the Claude Code connection is documented (L16 B3). OpenDesigner pushes the default mode as tokens and each mode as labeled specimen artboards (7.7), follows Paper's instructions (load `get_guide` first, call `get_font_family_info` before styling type, call `finish_working_on_nodes` at the end [S-L16-020]), and reads comments back as review input. Paper is a mirror and review surface, not a system of record (L16 B5).

**Code.** `export` writes platform code (7.5); changes reach the codebase as pull requests with the visual diff page (DC-L16-09, DC-L16-12). Penpot is the one design tool that imports DTCG natively, so it is offered as a round-trip target for teams that use it (L16 G2; BOARD L16 note).

| Target | Modes | Composites (type, shadow) | Color spaces | Main loss |
|---|---|---|---|---|
| DTCG tokens (canonical) | yes, through the Resolver | yes | OKLCH with hex fallback | none |
| Figma, import files | one mode per file; plan-limited modes per collection | no, recreated as styles | sRGB or HSL only | out-of-gamut OKLCH clipped and flagged |
| Figma, `use_figma` | yes, within plan limits | as styles | as Figma supports | 20 KB per call; no images; account fonts only |
| Paper | no (default mode only; others as artboards) | no | CSS colors | modes, libraries |
| CSS, Tailwind, Swift, Compose | yes (scopes, traits, themes) | yes | per platform | none intended |

---

## 11. Contradictions settled

Each row names the conflict, the resolution this spec adopts, and why. Rows marked "logged" are in `_coordination/DECISIONS.md`.

### 11.1 Between research lanes and synthesis files

| # | Contradiction | Resolution | Why |
|---|---|---|---|
| 1 | Validation timing: L08 validates on submit, on blur only for format checks; L13 validates on blur or at complete input length (DC-L08-17 vs DC-L13-06) | A questionnaire item (Q-form-02) with the merged default: format and complete-length checks on blur, everything else on submit, never while typing | Both agree on no validation while typing and on submit-time validation; evidence does not pick one (ONTOLOGY contradiction 1; QUESTIONNAIRE disagreements) |
| 2 | Figma easing: L04 says Figma variables cannot hold cubic-beziers; L07 verified timing and easing variables (DC-L04-28 vs DC-L07-14) | L07 wins; the easing part of DC-L04-28 is stale, its spring encoding stands | L07 is newer and verified on 2026-09-23 [S-L07-013] (ONTOLOGY contradiction 2) |
| 3 | Source units: L10 stores unitless 4-based numbers; L07 and L03 store px (DC-L10-08 vs DC-L07-11, DC-L03-26) | px in the source; rem on web export where wanted | DTCG `dimension` requires a unit and Figma imports px only [S-L07-002] [S-L07-011] |
| 4 | Radius scale: L04's default has no 6px step; the benchmark median control radius is 6 (DC-L04-01 vs DC-L09-01) | 6 stays in the scale and the snap list | follows the 22-system median (L09-A1.7) |
| 5 | Spacing endpoints: L03 includes 6 and stops at 80; L09 omits 6 and adds 96 | the union: multiplier 24 added to LEVERS B8, giving 96 at unit 4 (logged; `levers.json` needs the change) | keeps every benchmarked step (L09-A1.2) |
| 6 | Motion ladder ends and exit curve: L04 tops out at 700ms with exit (0.3, 0, 1, 1); L09 at 500ms with exit (0.4, 0, 1, 1) | 700ms is the full-screen and dimming step; one exit curve per preset | they differ only at the ends (ONTOLOGY contradiction 6) |
| 7 | Token tiers: "two tiers plus optional component" (L07) vs "three tiers, component optional" (L01, L02, L09) | primitive and semantic, component tokens on demand | the same architecture counted differently (DC-L07-01; Q-token-01) |
| 8 | Source of truth: the builder's model (L16, L11), DTCG in git (L07), or code (the 2026 practitioner majority, L00) | `state.json` plus DTCG in the person's repo is canonical; code and design tools are generated; code-canonical review mode for mature systems | in an AI-first product the "builder model" is files in the repo; one automated direction first (DC-L16-02, DC-L07-08, DC-L11-16; DECISIONS 18:59, kept) |
| 9 | Watch dark mode: L01 says watchOS lacks Dark Mode; L10 says watches are dark-only | not a real conflict: watchOS has no setting because it is always dark | ONTOLOGY contradiction 8 [S-L10-089] |
| 10 | Block provenance: ONTOLOGY uses four values and files team decisions as "designer-owned"; L17 uses five classes including owner input | the five classes (G, E, D, T, I) replace ONTOLOGY's provenance field | 29 business decisions were misfiled; S1b already tags questions this way (DC-L17-01; DECISIONS 18:59, kept) |
| 11 | Hook fallback order: L17 puts commissioning first; the icon and typeface cards put open libraries first (DC-L17-04 vs DC-L05-01, DC-L02-01) | identity assets lead with commissioning; icons and typefaces lead with open libraries | icons and typefaces are tool-assisted blocks; identity assets are designer-owned (QUESTIONNAIRE disagreements) |
| 12 | Quick mode asks 10 questions, but owner input is never auto-decided (DC-L17-08) | skipped owner-input answers are stored as `assumed` and confirmed in P7 | keeps Quick fast without inventing business decisions (`quick_mode_assumed_owner_inputs`) |
| 13 | Accessibility: "never waivable" (DC-L17-07) vs "override with a written reason" (L13 E1 level 2) vs Q-pref-01 where only strict mode blocks | generated values cannot violate the rules; accessibility lint errors on detached or authored values block export in every mode unless a WCAG-defined exception is cited with a reason; strictness affects only taste and hierarchy rules (6.4; logged) | keeps the floor while allowing the exceptions WCAG itself defines |
| 14 | Surface mode (Persuade, Operate, Read, Experience) is adopted by L17 A3 but has no question in the questionnaire | asked in the P0 bundle and stored per surface (logged) | S1b should add a question in its next revision |
| 15 | Energy direction: "energetic" reads as "faster", but calm systems are fast and expressive motion is slower and bouncier (LEVERS weak-evidence notes) | the Energy dial means longer, bouncier hero motion, not faster UI; its tooltip says so | Linear and Carbon productive are fast; Material expressive springs settle later (LEVERS B11) |
| 16 | Type scale: Expression implies a large ratio, but Material, the most expressive system, uses 1.125; the largest display ratios belong to productive systems with marketing sets | the ratio follows Expression capped by Density; display reach follows the marketing-surfaces input; recipes may override | LEVERS B6 and its weak-evidence notes |
| 17 | Body size and control size do not always move together (Carbon: 14px body, 40px md control) | both come from Density by default but are separately overridable | LEVERS weak-evidence note on Carbon [S-L03-082] |
| 18 | The 400ms "Doherty threshold" (L13) is a later restatement not found in the 1982 paper (DC-L16-07) | the 500ms transition warning stays, labeled a practitioner threshold [inferred]; the Doherty name is not used as its evidence; strategic delays are never justified by it | DC-L16-07 [S-L16-369]; L13 E2 |
| 19 | Focus ring: Material 3px, Atlassian and Primer 2px; a Figma article's 3px claim contradicts WCAG (pending V1) | 2px with a 2px offset by default, 3px as an option, both at 3:1 | QUESTIONNAIRE disagreements (Q-state-03); BOARD L13 note |
| 20 | Contrast method: WCAG 2.2 enforced vs APCA used by Radix and Geist; WCAG 3 still a draft | WCAG 2.2 enforced, APCA advisory | DC-L01-22 [S-L01-021] |
| 21 | Other genuine system disagreements: disabled submit, tooltips on disabled controls, toasts, pills, capitalization, dynamic color, base unit 4 versus 8, typeface default, body size 14 versus 16, motion default | presented as options with the QUESTIONNAIRE disagreements-table defaults (never-disable with `aria-disabled`; toasts only for low-stakes results with undo; pill per component role; sentence case; per-platform dynamic color with brand and status fixed; "4 as the grid, 8 as the rhythm"; system stack for tools with Inter one click away; body size tied to Density; two-mode motion with a productive cap for high-trust products) | these are design choices, not lane errors (QUESTIONNAIRE "Where lanes or systems disagree") |

### 11.2 About the process and the package

| # | Contradiction | Resolution | Why |
|---|---|---|---|
| 22 | Process shape: L17 I2's 11 stages (assets before brand) vs the questionnaire's 27 validated screens; the first S1d instance's 12 stages | ten phases wrapping the validated screen order (3.1; logged, superseding the 18:59 twelve-stage entry) | the process can never contradict the question data |
| 23 | Asset gate position: after the Stage 03 checklist (first instance) vs after all hooks resolve | after Stage 19 (logged) | briefs need the tokens and direction (L17 H1 rule 6); gates stay spread across the flow |
| 24 | Record vocabularies: S1b `set_by` (chosen, confirmed_default, auto_default, reference); L18 status (confirmed, default, delegated, locked); L17 source (default, reference, person, designer, asset); REPO-PLAN hook status (have, commissioning, using tool, skipped); L17 hook status (have, commissioning, tool, open library, placeholder, not needed) | `set_by` extended with `assumed`, `delegated`, `asset`, plus `locked`, `source_ref`, `supersedes`; block status (pending, default, decided, not-applicable, awaiting-asset, assumed); asset status (have, commissioning, open-library, tool, placeholder, not-needed) (7.9, 7.10; logged, superseding part of the 19:01 entry) | reuses the vocabulary already in `questionnaire.json`; "skipped" split into placeholder and not-needed so a needed-but-missing asset stays visible |
| 25 | State location and script name: L18's `opendesigner.state.json` at the root and `od.py` vs REPO-PLAN's `./opendesigner/state.json` and `engine.py` | REPO-PLAN wins | REPO-PLAN is the contract R2 and R3 build against |
| 26 | PRODUCT.md: separate file (L17 A3 adopt) vs everything in DESIGN.md | PRODUCT.md and DESIGN.md at the project root, the rest in `./opendesigner/` (logged) | different readers and change rates; gstack, impeccable, Stitch and Claude's artifact skill read the root |
| 27 | DESIGN.md: canonical format (Stitch, gstack) vs a draft spec (L00) | DTCG canonical; DESIGN.md a generated view in Google's section order plus nine fixed OpenDesigner sections (7.2; logged) | DESIGN.md is alpha and lacks modes and motion [S-L00-052] [S-L17-213] |
| 28 | Templates: REPO-PLAN's 8 vs L18's list vs the first instance's 8 plus 6 | REPO-PLAN's names plus block-map, dial-board, reference-card, asset-tray, coverage and diff (logged) | each addition serves a numbered brief requirement or the extend protocol |
| 29 | Skill count: REPO-PLAN's four vs a proposed fifth review skill | four; review runs in the router (P7) and in extend; engine and data copied into each skill (logged) | matches REPO-PLAN; claude.ai installs skills separately [S-L18-001] |
| 30 | L16 recommends a standalone visual canvas (G2 option 4) vs BRIEF requirement 6 (the LLM is the interface) | Phase 1 skills, Phase 2 MCP Apps, the canvas an optional Phase 3 (DECISIONS 18:59, kept) | Phase 1 already realizes option 4's core in miniature: the engine state is the model and templates render real HTML/CSS |
| 31 | Visual ladder: DC-L18-06 lists the Claude Design canvas as rung 2; the questionnaire omits it | a hand-off target, not a rung (logged) | a closed product OpenDesigner cannot drive [S-L18-029] |
| 32 | Figma writes from ChatGPT: Figma's catalog says yes, its write-to-canvas list says no | treated as no until verified; file export offered (logged) | [S-L18-244] vs [S-L18-136] |

### 11.3 Data gaps found while writing (hand-offs, not product decisions)

- `synthesis/cards.json` has 352 cards but ONTOLOGY maps 325; the 27 L17 and L18 cards need owning nodes. Suggested by the first S1d instance: DC-L17-03 to `builder.intake`; DC-L17-01 and -04 to `builder.hooks`; DC-L17-05 and -06 to `builder.ai`; DC-L17-07 and -09 to `guard.checks`; DC-L17-10 to `gov.decisions`; DC-L17-11 to `builder.preview`; DC-L17-12 to `builder.review`; DC-L17-13 to `builder.controls`; DC-L17-02 to `ctx.strategy`; DC-L17-08, DC-L18-08 and -09 to a new `builder.pacing`; DC-L18-06 and -07 to a new `builder.surface`; DC-L18-01, -02, -04, -05 and -14 to `deliver.ai`; DC-L18-03 to `deliver.packaging`; DC-L18-10 to `deliver.channels`; DC-L18-11 to `guard.enforcement`; DC-L18-12 to `builder.state`; DC-L18-13 to `deliver.interop` (for S1a).
- DECISION-GRAPH.md prose still says 325 decisions, 431 edges and DC-L16-02 fan-out 8; `decision-graph.json` has 352, 465 and 9 (and DC-L10-02 at 11). The JSON wins; the prose needs a refresh (for S1c).
- The questionnaire needs a surface-mode question (row 14) (for S1b).
- `levers.json` B8 needs multiplier 24 (row 5); the engine contract gains `intake` and the `design-md` additions in 8.3 (for R2).
- The template set in 3.6, the per-skill copies in 8.2, and the reference files 8.2 adds beyond REPO-PLAN's list (`blocks.json`, `graph.json`, `intake.md`, `extend.md`, `export.md`) (for R3).

---

## 12. Positioning

The open space, found independently by three lanes: no competitor walks a person through the decisions before a system exists (L11 G [S-L11-071] [S-L11-073]); none checks coverage against a full ontology (L17 E2 item 5); none explains why a decision matters as it is made (L16 G3). OpenDesigner competes on exactly those three and interoperates with everything else.

| Product or group | What it does well | Where OpenDesigner differs | Relationship |
|---|---|---|---|
| **Claude Design** (Anthropic Labs) | builds a team system from code, design files and brand documents; checks its own output against the system before showing it; the system persists as an artifact in every conversation; admins can lock it [S-L18-031] [S-L18-032] [S-L18-029] | closed, paid plans only, Claude only, storage format undocumented, no Figma export or version history (Sep 2026); it extracts rather than guides, and nothing public says it teaches why or paces by downstream reach [S-L18-030] [S-L11-055]. OpenDesigner is open, model-portable, inspectable files, a teaching layer and fan-out pacing | hand-off: a person can import OpenDesigner's DESIGN.md and tokens into Claude Design. Claude Design is better today at direct visual editing; OpenDesigner relies on the host's surfaces until Phase 2 |
| **Figma Make kits and the Figma agent** | a kit from packages, library variables and a guidelines folder; an in-canvas agent that writes variable scales, styles and brand-guideline pages [S-L17-200] [S-L17-207] | needs a Full seat on paid plans; guidelines are authored or generated from prose, not decided with the person; long guidelines flood context, so Figma recommends many short files [S-L17-211] | OpenDesigner pushes variables to Figma (section 10); its component pages are short structured files that could seed a Make kit's `guidelines/` [inferred] |
| **Figma's `figma-generate-library` skill** | the closest precedent for the process: discovery and a printed gap analysis, locked scope, foundations before components, forks with provenance, a QA phase [S-L17-210] | starts from an existing codebase and needs a write-capable seat; "never a one-shot task" | a downstream writer for H-figma; OpenDesigner adopts its gap-analysis gate (Gate 1) and adds the start-from-nothing path |
| **tweakcn and theme generators** (tweakcn, shadcn create, Radix Themes playground, Material Theme Builder, Realtime Colors, Adobe Leonardo, Relume, Uizard, Subframe, Token Designer/Bezel) | fast visual tuning from 3-40 inputs with live previews; Leonardo's contrast-based ramps; Radix's step jobs; Material's HCT [S-L11-068] [S-L11-071] [S-L11-073] [S-L11-082] | one stack each, no rationale, accessibility program, modes beyond light and dark, or governance: "a theme rather than a true design system" [S-L17-206]; Material Theme Builder's repo was archived 23 Jul 2026 [S-L11-067]; Bezel is closest at the token layer [S-L11-081] | OpenDesigner adopts their best methods (contrast-indexed steps, step jobs, lock and shuffle) and exports to their formats (shadcn and Tailwind CSS variables) |
| **AI app builders** (v0, Lovable, Bolt, Magic Patterns, Google Stitch, UX Pilot; Motiff discontinued) | build apps and screens with a system; Stitch extracts from a URL and reads DESIGN.md [S-L17-201] to [S-L17-206] [S-L17-213] | they consume an existing system or produce one as a by-product; gated by stack or plan (React only, Team plans, weekly quotas, sales calls) (L17 E2 item 7) | OpenDesigner produces the system they consume: DESIGN.md, DTCG and component docs |
| **Design-system platforms** (Supernova, zeroheight, Knapsack, Tokens Studio, Storybook, UXPin Merge) | host, document, sync, measure and deliver an existing system (L11 G) | none helps make the decisions | export targets: DTCG for Tokens Studio and Supernova, component pages for docs platforms, Storybook for code-canonical review |
| **UI kits** (Untitled UI, Material and Apple kits) | a finished, broad system to adopt [S-L11-078] | the kit's defaults become the look unless changed (L17 D) | a kit can be the component base (Q-comp-01), never the visual direction (DC-L17-02) |
| **gstack's design skills; Anthropic's frontend-design skill** | taste-aware consultation, safe versus risk proposals, variant boards, slop catalogs, DESIGN.md output [S-L17-003] to [S-L17-008] [S-L17-021] | taste-first and single-host; no ontology, coverage check, hooks with licence intelligence, or deterministic engine | OpenDesigner adopts their methods (3.8) and adds those four |
| **Extractors** (Dembrandt, Firecrawl branding, Brandfetch, html.to.design, Project Wallace) | measure a live site's colors, type, spacing, shadows and more [S-L17-237] [S-L17-238] [S-L17-249] | only Dembrandt forbids copying third-party identity | usable as intake tools behind OpenDesigner's identity firewall (section 5) |

---

## 13. Roadmap

### 13.1 Phases

**Phase 1: skills, knowledge, engine and templates, across Claude, ChatGPT and Codex** (REPO-PLAN owners R1-R4). Runs in Claude Code, the Claude app (zip upload or plugin), Codex, ChatGPT desktop (plugin), ChatGPT Projects (the Free fallback), Cursor, VS Code with Copilot and Gemini CLI, with visuals through host-native HTML, local files, or text (L18 I3 item 1). Build order [inferred; logged]:
1. `engine.py` with tests (R2): `init`, `set`, `generate`, `validate`, `export`, `design-md`, `preview`, plus `intake`; the 13 LEVERS C recipes as fixtures.
2. `tools/build_data.py` and the router skill (R3): stage files, rules, hooks, guardrails, the text interview and the output contract.
3. The 14 JSON-fed templates and `preview.html`.
4. The extract, extend and export skills.
5. Manifests, `tools/sync_skills.py`, CI drift checks, release zips, the ChatGPT Project bundle, `examples/`.
6. The Figma and Paper writers as export sub-flows (section 10).

**Phase 2: a remote MCP server with MCP Apps views** (DC-L18-05; L18 C2-C3). Stateless, read-only and no-auth, on the MCP 2026-07-28 transport; the state stays in the person's files and is passed in on each call, so the server stores no user data [S-L18-022]. It exposes chunked knowledge resources, read-only tools (next questions, explain, examples, coverage), pure generators (palette, type scale, contrast, export), the 14 templates as `ui://` MCP App views, prompts (start interview, extend system, review system) and the skill over MCP for ChatGPT plugin submission; a local stdio package comes from the same codebase. Every tool declares `readOnlyHint` and `destructiveHint` [S-L18-019] [S-L18-119]. MCP Apps is the only visual standard that renders in both Claude and ChatGPT (and VS Code, Cursor, Goose, Microsoft 365 Copilot) [S-L18-024]; terminal agents keep the Phase 1 surfaces [S-L18-044].

**Phase 3, optional:** a standalone visual canvas (L16 G2 option 4) with direct manipulation, lock and shuffle, a "show 6" grid, unlimited undo and branches (DC-L16-04, -05, -08, -10); accounts and saved projects with OAuth (DC-L18-05 option d); agent presence and then multiplayer (DC-L16-11); a Figma plugin; CI visual diffs.

### 13.2 What to build first

The engine and the router's text interview with its outputs. That alone runs in every host, produces a complete, validated system, and is the base every visual surface, the server and the canvas reuse (L18 I3; principle 1).

### 13.3 How to test it

**Representative briefs** [inferred; logged], each run in Quick and Standard mode on at least two hosts or models:

| Brief | What it stresses |
|---|---|
| B1 B2B analytics dashboard, web only, dense, existing Tailwind repo | the audit entry path, reading before asking, density |
| B2 Consumer fintech on iOS, Android and web; exact brand color | native posture, the finance Expression warning, the brand-exact flag, platform modes |
| B3 A public service, web, AAA contrast, 19px body, no motion | the GOV.UK recipe, high contrast, motion off |
| B4 A developer tool with docs and a marketing site, dark by default | several surfaces with different modes, display reach, a mono face |
| B5 "Make it feel like Linear, but ours" | reference intake and the identity firewall |
| B6 A multi-brand white-label SaaS | the brand axis, the 20% rule, Figma plan limits |
| B7 A patient app in English, Hindi and Telugu | script rules, text scaling, accessibility floors |
| B8 A TV and in-car companion | device classes, driving rules, targets by input |
| B9 A startup with nothing: no logo, no fonts, Quick mode | hooks, placeholders, assumed owner inputs |
| B10 B1's system six weeks later, in a different model, adding data tables and a compact mode | the extend routine, locks, determinism across models |

**What is measured:**
1. Determinism: the same `state.json` gives byte-identical tokens across hosts and models.
2. Validation: every generated system passes `validate`; zero contrast failures in any mode.
3. Coverage: every block has a status; nothing is silently skipped; assumed answers are listed.
4. Owner input is never invented: every I-class answer is chosen, confirmed or `assumed`.
5. The identity firewall: with a known-brand reference, the output carries no reference brand hue as the brand color, no proprietary face, no logo, imagery or copy.
6. Recipe reproduction: the 13 LEVERS C recipes reproduce their documented signatures and fit grades.
7. Pacing and question format: high-weight questions get why, options, a recommendation and the downstream effect; low-weight ones are grouped; question counts match the mode.
8. Honesty: defaults recorded as defaults; placeholders labeled as placeholders.
9. Interop: Google's DESIGN.md linter passes; Figma accepts the import files; the Paper push succeeds.
10. Team value: an engineer and a designer each say whether they could explain the system or brief a designer from RATIONALE.md alone.
11. Skill triggering: the router catches "create", "extend" and "review" requests (this decides whether a fifth review skill is needed, 8.2).

Transcripts and outputs are graded by fresh-context verifier agents against a rubric fixed in advance, at least two runs per brief, because one output is an example, not an evaluation [S-L17-130] [S-L17-132]; DC-L11-23 recommends testing agent-facing systems with evals rather than hoping documentation changes work.

---

## 14. Open questions for Kunal

Only questions whose answer changes what gets built. Each has the default the build follows if there is no answer.

1. **Component code.** Should Phase 1 generate production component code on one stack (for example React on Base UI through the shadcn registry), or stop at tokens, component specs, doc pages and HTML previews, with the headless base recorded through H-comp? *Default:* specs, docs and previews; no production component library. This changes R2's and R3's scope and the examples.
2. **Designs and visuals beyond the system.** The brief says "design systems, designs and visuals". Phase 1 designs the system and shows it on sample screens. Should Phase 1 also design full product screens and marketing visuals (as Stitch and Claude Design do), or should that wait until the system flow works? *Default:* later; Phase 1 ends at the system plus sample screens.
3. **Phase 2 hosting.** Who runs the remote MCP server (domain, host such as Cloudflare Workers, cost, and whose account submits it to the Claude connectors directory, the MCP Registry and the OpenAI plugin directory)? *Default:* Phase 2 is designed but not built until this is answered.
4. **First host to polish.** Which host should get the best visual experience first: Claude Code (terminal, local HTML, artifacts), the Claude app (custom visuals and artifacts), or ChatGPT and Codex desktop (built-in browser)? *Default:* Claude Code, because it is where the builders work today; this sets template priorities.
5. **Licences.** Confirm MIT for code and CC BY 4.0 for research and docs before the repo goes public (REPO-PLAN default). A change alters the LICENSE files, file headers and the ChatGPT and plugin listings.

---

## Confidence

- **Confirmed from files read on 2026-09-23:** every count in this spec (ontology, graph, questionnaire, block classes, time weights, per-phase question counts); every formula and threshold, which are LEVERS' and cited there; host capabilities, Figma, Paper and DTCG facts, which are L16, L17 and L18 findings with their sources.
- **Inferred (tagged in place and logged):** the ten-phase grouping and gate placement, the record vocabularies, file placement, the DESIGN.md and PRODUCT.md contracts, the six added templates, the engine additions, the accessibility waiver rule, the eval briefs and metrics, and the Phase 1 build order. They are defaults to test with the evals in 13.3, not findings.
- **Weakest links carried from the synthesis:** the dial coupling coefficients, macro offsets, radius role ratios, icon stroke formula and some thresholds (LEVERS "Weak evidence"); the harmony evidence rests mainly on one vendor evaluation [S-L18-332]; DESIGN.md is an alpha format.
