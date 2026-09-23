# U lanes: ease of use for everyone (BRIEF requirements 12-17)

Any session can take an `open` U lane. Setup for every lane: read `_coordination/BRIEF.md` (especially "Ease of use for everyone"), `_coordination/PROTOCOL.md` and `_coordination/REPO-PLAN.md`; pick a unique session name; `export OD_SESSION="<name>"`; `python3 tools/od.py claim <lane>` (stop if it fails: someone has it); post heartbeats; log decisions with `od.py log`; finish with `od.py done`, the checks in AGENTS.md "Before you commit", and `od.py sync`. Tell the orchestrator ("OpenDesigner orchestrator") when you claim and when you finish.

Writing rules for every U lane: plain words first; one idea per sentence; no wall of text; never all three voices at once unless the person asks.

---

## U1: Glossary in three voices
Output: `synthesis/glossary.json` (source of truth; `tools/build_data.py` ships it into the skills) and `docs/GLOSSARY.md`, with a readability check script. Claimed by the "Design system research and builder" session.
- Cover every term a person can meet: ontology block names (`synthesis/ontology.json`), questionnaire terms (`synthesis/questionnaire.json`), token and DTCG words, DESIGN.md section names, dial names (`synthesis/levers.json`), engine commands and outputs, and common design words (hierarchy, contrast, radius, elevation, density, and so on). Expect 200-400 terms.
- Each entry: `id`, `term`, `plain` (a 12-year-old understands it; one sentence, no other jargon), `designer` (how designers say and think about it), `engineer` (how it lands in code: token path, CSS property, API), `example` (one concrete example), `see_also`, `aliases` (names other systems use, e.g. Snackbar = Toast).
- Plain voice checks: short words, no undefined terms; add a reading-level check (a simple stdlib Flesch-Kincaid estimate) to the build script and keep `plain` at or below grade 6.
- Use the local `dumbify` and `anti-ai-writing` skills for the plain voice.

## U2: Zoom levels and the living DESIGN.md  (assigned to the skills agent R3, continuing)
Interview as zoom levels, not modes: Level 0 "sketch" (about 5 questions, a complete coarse system), Level 1 "broad" (each foundation at a glance), Level 2 "defined", Level 3 "detailed" (per block and component). Stop anywhere. DESIGN.md updates after every decision; each section carries its zoom level; the end-of-implementation review ritual lives in the skills and the AGENTS.md snippet written into the person's repo.

## U3: Self-improvement loop  (skills side: R3; engine side: R2; contributor docs: R1)
`engine.py feedback "text" --kind gap|bug|confusing|idea` records to `opendesigner/feedback.md` and prints a pre-filled GitHub issue link (nothing is posted without the person's OK). Inside the OpenDesigner repo itself, the skill fixes the source file (skills/, synthesis/), runs the checks, and syncs.

## U4: Plain-language and clutter pass  (open after U1 lands)
Rewrite every user-facing text for concision and plain-first clarity, using the glossary: README, docs/, skill SKILL.md messages and stage prompts, template copy, engine messages and validation reports. Keep meaning and sources intact. Record before/after reading levels.

## U5: Three-persona usability test  (open after U2-U4)
Run the `opendesigner` skill end to end, in text mode, as three personas: a school student making a club website, a product designer setting up a system, a backend engineer who needs a UI for an internal tool. Log every point of confusion, clutter, jargon or dead end in `research/U5-usability.md`, fix what is small, and file the rest with `engine.py feedback` or as issues in `docs/SEED-ISSUES.md`.
