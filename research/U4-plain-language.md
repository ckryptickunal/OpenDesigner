# U4: plain-language and clutter pass

Each U4 session appends its before/after numbers (`python3 tools/readability.py`) and meaning-level fixes under its own heading. Rules: `_coordination/lanes/U4-rules.md`. Baseline: `research/U4-baseline.json`.

## U4a docs (2026-09-24)

Scope: `README.md` and every `docs/*.md` except `docs/GLOSSARY.md` (generated). `docs/SPEC.md` got only the V1 corrections, no plain-language pass. "Before" is the state after the earlier, partial U4 edits (commit 2ca83ae); "baseline" is `research/U4-baseline.json`.

| File | Baseline grade (long) | Before this pass | After |
|---|---|---|---|
| README.md | 9.8 (16) | 7.0 (0) | 6.9 (0) |
| docs/FAQ.md | 10.0 (26) | 6.9 (1) | 6.9 (0) |
| docs/HOW-IT-WORKS.md | 10.6 (23) | 7.0 (2) | 7.0 (0) |
| docs/SEED-ISSUES.md | 10.4 (20) | 10.4 (20) | 7.1 (0) |
| docs/SPONSORSHIP.md | 7.9 (6) | 7.9 (6) | 7.2 (0) |
| docs/RESEARCH.md | 7.5 (3) | 7.5 (3) | 6.3 (0) |
| docs/GITHUB-SETTINGS.md | 7.2 (3) | 7.2 (3) | 5.8 (0) |
| docs/JOURNEY-TRACKER.md | not in baseline | 7.7 (5) | 6.5 (0) |
| docs/PRIVACY.md | not in baseline | 7.5 (7) | 6.9 (1) |
| docs/SPEC.md (corrections only) | 13.0 (177) | 13.0 (177) | 13.0 (177) |
| **docs/ without SPEC.md**, weighted | 9.4 (81) | 7.7 (47) | 6.9 (1) |
| **all docs/**, weighted | 11.2 (258) | 9.7 (224) | 8.9 (178) |

The one long sentence left in PRIVACY.md is the sharing consent text, which must match `journey.py share-consent` word for word.

Meaning-level fixes (each checked against the files or the GitHub API on 2026-09-24):
- README first screen: what it is, what you get, how to start, then one line for designers and one for engineers.
- Counts: ontology 271 to 275 nodes; 211 building blocks from `ontology.json` (156 generatable, 30 designer-owned, 23 tool-assisted, 2 extractable) replace the 207-block five-class table in README and HOW-IT-WORKS, which keeps the L17 counts as history [S-V1b-091]. Sources: 2,740 from the research lanes, 3,225 in `traces/` with R4 and V1. Tests: 25 engine plus 23 journey.
- New facts: four named zoom levels; the journey tracker and opt-in sharing (README, HOW-IT-WORKS section 11, FAQ privacy answer); V1 done (README, RESEARCH); `engine.py sketch` in the README's try-it block; the repo is public; seed issues filed as #1 to #21; GitHub settings status (security features, merge settings and ruleset not applied; Actions disabled at the account level; orphaned commit `1ac2ebe` still served); funding.json exists with an empty `entity.email`.
- Corrections: HOW-IT-WORKS said every one of the 192 questions has a zoom level; Q-ref-01 (the reference panel) has none. FAQ said the skills make no network calls; the engine makes none, and `journey.py share` posts only after consent.
- V1 rows applied: 4b, 5, 15b, 16b, 27, 28, 29, and 24b in part. Still open: `docs/GLOSSARY.md:418` (edit `synthesis/glossary.json`), `synthesis/OPENDESIGNER-SPEC.md:7, :233` (the original of docs/SPEC.md, which now carries a dated note the original lacks), and the classification choice in 24c.

Checks: `tools/check_links.py` 163 links, 0 broken; `tools/jev_nav.py check` 0 dangling (it does not scan `docs/`, so the S-V1 ids cited there were checked by hand against `traces/V1-trace.md`).

## U4b skills (2026-09-24)

Scope: `skills/*/SKILL.md`, the hand-written `skills/opendesigner/references/*.md`, `assets/templates/*.html` text, `assets/output/*`, the wording in `synthesis/QUESTIONNAIRE.md` (Ask lines, question headings, option labels, Why lines), and message strings in `engine.py`. "Before" is commit 2ca83ae; "baseline" is `research/U4-baseline.json`. Grade (sentences over 25 words), from `tools/readability.py`.

| File | Baseline | Before this pass | After |
|---|---|---|---|
| skills/opendesigner/SKILL.md | 6.2 (4) | 6.2 (2) | 6.0 (0) |
| skills/opendesigner-extract/SKILL.md | 9.9 (6) | 9.9 (6) | 7.1 (0) |
| skills/opendesigner-export/SKILL.md | 8.4 (1) | 8.4 (1) | 6.9 (0) |
| skills/opendesigner-extend/SKILL.md | 5.9 (0) | 5.9 (0) | 5.9 (0), not changed |
| references/rules.md | 7.9 (9) | 7.0 (5) | 6.3 (0) |
| references/zoom.md | 5.1 (3) | 4.8 (5) | 4.7 (1, a quoted offer) |
| references/hooks.md | 10.8 (5) | 8.5 (2) | 6.8 (0) |
| references/guardrails.md | 9.9 (2) | 8.3 (2) | 7.9 (0) |
| references/improve.md | 4.9 (0) | 5.1 (0) | 5.1 (0), not changed |
| assets/output (4 files) | 6.8 (1) | 6.8 (1) | 6.4 (0) |
| references/stages/*.md (56, generated) | 8.9 (277) | 8.9 (277) | 7.8 (230) |
| **all skills/ files**, weighted | 8.6 (301) | 8.6 (301) | 7.5 (231) |

What the model says, measured per item (`check_glossary.grade`; citations stripped from Why lines):

| Questionnaire text | Before | After |
|---|---|---|
| Ask lines (192) | grade 7.2; 95 of 211 sentences over grade 8 | grade 5.0; 1 of 202 over grade 8 |
| Question headings (192) | grade 5.4; 37 over grade 8 | grade 4.5; 5 over grade 8 |
| Option labels (766) | grade 7.3; 264 over grade 8; 11 over 25 words | grade 5.7; 122 over grade 8 (mostly product names and citations); 6 over 25 words |
| Why lines (192) | grade 11.6; 14 over 25 words | grade 6.3; 0 over 25 words |

Stage files still carry 230 long sentences. They are in the Default, Show, Hook, Use/avoid and option-effect fields, which are model-facing data with citations. This pass left them alone.

Meaning-level changes:
- About 75 Ask lines no longer contain the recommendation (rules.md 3.7, "word questions neutrally"). Most were expert-level asks worded as yes/no proposals of the default ("Keep the standard duration ladder...?"). They are now open questions; the default stays in Default and in the recommended option. Examples of removed hints: "WCAG 2.2 AA is the usual floor", "One is usual", "Four named levels is typical", "Most web and productivity apps stay silent".
- Q-brand-08 now asks "Which of these do you already have? Tick all that apply." The 12 items stay in its options.
- hooks.md: the Ask and Question columns are the plain words the model says, one hook per message except in the Q-brand-08 checklist.
- engine.py (strings only): validation, review, sketch and feedback messages; the DESIGN.md renderer lists "Enforced by construction", the accessibility guarantees and the test matrix as bullets, says "source of truth" instead of "canonical", and its zoom line reads "To zoom in, answer Q-...". `examples/*/DESIGN.md` are now stale (`engine.py review` reports it) until they are regenerated.
- Templates: plain subtitles and headings (for example "Shades (color ramps)", "Easy to read? Contrast checks"), spacing labels "Steps of 4, rhythm of 8", "Steps of 8 only", "Every step of 4".
- Checked after every change: no question's `default_value` changed, `pacing.json` `deep_always` is unchanged (6 questions), every Why line keeps its citation set and numbers, and no test asserts a changed string, so no test was edited.

Checks: build_questionnaire (0 problems, 0 ordering violations), build_data, sync_skills, 48 tests OK, check_glossary --build 0 errors, build_dist --check, jev_nav check 0 dangling.
