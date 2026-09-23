# Consistency findings from the glossary work (U1)

While checking every glossary entry against the engine and skills, the writing and verification agents found places where the skills, the questionnaire, the spec and the engine disagree. Fixed items are marked. Open items need a decision from the owner of the file, because the right fix could go either way.

| # | Where | Mismatch | Status |
|---|---|---|---|
| 1 | `skills/opendesigner/references/rules.md` section 9 | Example said `roundness=45` is "a bit softer"; the engine maps 45 to 6px, sharper than the 8px default (65 gives 12px). | **Fixed** 2026-09-24: example now uses 65. Rebuilt `chatgpt-project/` and synced skill copies. |
| 2 | `tools/build_data.py` (tool-hook table parser) | The five tool rows in `hooks.json` had every field shifted one column (the Hook cell holds only the id, so the first split cell was empty). | **Fixed** 2026-09-24: parser drops the empty cell; tool hooks now also list their questions. Engine tests pass (25). |
| 3 | `skills/opendesigner/SKILL.md`, `references/zoom.md` | Told the model to run `engine.py set zoom.all 1`, which the engine rejected. | **Fixed** by R2 (engine now accepts `zoom.all`). |
| 4 | `engine.py` (around lines 3837 and 4121) | Principles are read from Q-brand-04; the principles question is Q-brand-07. | Open (engine owner) |
| 5 | `engine.py` and Q-tool-03 | Answering Q-tool-03 never sets `exports.figmaPlan`. | Open |
| 6 | Q-dir-01 and the engine | Q-dir-01's default is `flat2`, but if it is never answered no preset applies. | Open |
| 7 | Stages 23, 26, 27 | Offer defaults for features that do not exist yet (Q-pattern-05, Q-dist-01 to 03, Q-pref-01 and 02). Mark them planned or hide them. | Open (questionnaire source) |
| 8 | `skills/opendesigner-export/SKILL.md` | Describes 2 Figma collections; the engine writes 5. | Open |
| 9 | `skills/opendesigner-extend/SKILL.md` | Says `review` finds hard-coded shadows and durations; it does not. | Open |
| 10 | Q-comp-02 and `engine.py` | Q-comp-02 defaults to 25 core components; the engine's starting inventory has 22. | Open |
| 11 | `engine.py` validation report and `build` | The report says errors are "to fix before export", but `build` exports first and validates afterwards. | Open (either reorder `build` or reword) |
| 12 | `synthesis/levers.json` and `engine.py` | `type.emphasizedVariants` turns on at Expression 67 and above, but the engine never emits emphasized text styles. | Open |
| 13 | `engine.py` spacing `$description` | Lists multipliers up to 20; the engine emits `space.96` (multiplier 24). | Open |
| 14 | Spec section 7.4 and `engine.py` | Spec requires lowercase token path segments; the engine emits camelCase (`boldHover`, `onAccent`). | Open (spec or engine) |

The glossary describes what the engine does today, so it stays correct whichever way these are resolved. `python3 tools/check_glossary.py --refresh-tokens` re-reads the engine after any change, and `--build` flags glossary entries that no longer match.
