# T1 phase B: wire the journey tracker and report sharing into OpenDesigner

Owner: T1 journey. Start only when the orchestrator says the U4 wording pass on SKILL.md, the references and engine.py has landed. Phase A (done, new files only): `skills/opendesigner/scripts/journey.py`, `test_journey.py`, `references/report.schema.json`, `docs/JOURNEY-TRACKER.md`, `docs/PRIVACY.md`, `server/telemetry/`. BRIEF requirements 18 and 19.

Principles for every change below:
- One consent per purpose. `profile.tracking` (local log) and `profile.share_reports` (sending) are separate, and neither is ever assumed.
- Logging is silent. No message to the person mentions it except the consent line, the optional level line and the sharing question.
- Journey code never breaks design work: the engine calls `journey.record()`, which never raises or prints.
- The engine logs answers; the model logs what only it can see (what was shown, help, frustration, speed requests, session end). `summarize()` drops a second log of the same answer within 2 minutes, so an overlap is harmless.

## 1. `skills/opendesigner/scripts/engine.py` (R2 owns it: send R2 this section, or edit with the orchestrator's OK)
1. Near the imports:
   ```python
   try:
       import journey  # sibling module (scripts/journey.py); optional
   except ImportError:
       journey = None

   def track(d, event, **kw):
       if journey:
           journey.record(d, event, **kw)
   ```
2. `cmd_set`, after `log_decision(...)`: map the path to a question id with `ANSWER_PATHS = {"context.product": "Q-scope-01", "raw.brandColor": "Q-color-01", "macros": "Q-brand-01"}`, plus `answers.<Q-id>` itself. When there is a question id:
   - if `prev is not None and prev != value`: `track(d, "step_changed", step=qid)`
   - always: `track(d, "step_answered", step=qid, how=journey.how_for(qid, value, set_by) if journey else None)`
   `how_for` maps `--set-by` (chosen, confirmed_default, auto_default, assumed, delegated, reference, asset) to `--how`, and returns `free` when a chosen value is not one of the question's options. Do not log dials, raw values or overrides: they are not questions.
3. `cmd_sketch`: the `cmd_set` calls above already log Q-aud-01, Q-plat-01, Q-brand-01, Q-color-01 (only when `--brand` is given) and Q-theme-01. After `cmd_build`, `track(d, "level_complete", level="sketch")`.
4. `main`, `validate` branch: when `rep.count("error")`, `track(d, "error", step="validate", count=rep.count("error"))`. `cmd_build`: the same with `step="build"` when it returns non-zero.
5. `cmd_export`: `track(d, "export", kind=fmt)`. `cmd_review`: `track(d, "review")`. `cmd_feedback`: `track(d, "feedback_filed", kind=kind, step=question)`.
6. `engine.py feedback --from-journey`: new flag. It appends `journey.feedback_text(d)` (public question ids and counts only, never notes; tested in `test_journey.py`) to the text, sets `--kind confusing` when no kind is given, and prints the issue link as today. Nothing is posted. If the text is empty, say "No journey log yet."
7. The level-end message in `cmd_sketch` (and wherever the engine prints the offer) adds `journey.level_line(d, "sketch")` when it is not empty. It prints "You took N steps; the shortest path is M." only when logging is on and 3 or more steps could have been saved.
8. Tests in `test_engine.py`: with `profile.tracking` on, `pick` writes one `step_answered` with the right `how`; with it missing, nothing is written; `sketch` writes `level_complete`; a failing `validate` writes `error`.

## 2. `skills/opendesigner/SKILL.md`
1. **Start, step 3 (greeting):** the greeting's middle line becomes the consent question, word for word: "I keep a private log of your steps on this computer so I can make this faster for you. OK?" On yes run `journey.py consent on`; on no, `journey.py consent off`. Ask only when `profile.tracking` is missing. Trade-off for the orchestrator: rules.md allows one question per message, so either the first sketch question moves to the next message (one extra turn, recommended, because consent must be a real yes) or the consent line rides along as a second, clearly separate question.
2. New short section **"Journey log (only when on)"**, 5 lines at most:
   - When you show a question or screen: `journey.py log step_shown --step <Q-id>`.
   - Answers recorded through `engine.py pick/set/sketch` are logged by the engine. When an answer doesn't go through the engine, log it yourself: `step_answered --how default` or `step_skipped --reason person|rule|known|speed|later`.
   - Help: `log help --kind explain|voice_switch|glossary|example`. Signs of frustration: `log frustration --signal ...` (definitions in rules.md). "Go faster" or "just do it": `log speed_mode`.
   - At Finish or when they say stop: `log session_end`.
   - Never mention the log in normal messages. Notes stay under 12 words and never hold names, answers, colors, links or anything they typed.
3. **Finish:** add "If the log is on, run `journey.py report` and mention one line only if it shows something useful."
4. **Sharing (requirement 19):**
   - When: after the first `level_complete` (normally the sketch), in the message after the result has been shown and the offer made. Never in the first message, never mid-question, and only once: skip it when `profile.share_reports` is set or when the local log is off.
   - How: one message. Show the output of `journey.py share-consent` word for word, as one question with three choices (the host's question tool can carry them: share every time, ask me each time, don't share). If they say "show me", run `journey.py share --dry-run` and show the JSON, then ask again. Record with `journey.py share-consent always|ask|never`.
   - Sending: at `session_end` and after each later `level_complete`. `always`: run `journey.py share` and say nothing unless it fails loudly (it doesn't: failures wait in the outbox). `ask`: one line, "Send this session's anonymous report? Say 'show me' to see it first.", then `journey.py share --yes` on yes. `never` or missing: do nothing.
   - "Stop sharing" at any time: `journey.py share-consent never`, then confirm in one line.
5. Engine block: add the journey commands in 4 lines (`consent`, `log`, `report`, `share-consent`/`share`).

## 3. `skills/opendesigner/references/rules.md`
New section **"Journey signals"** (the model's judgment calls, one line each):
- `said`: they say it is annoying, confusing or too much.
- `repeat_question`: they ask what a question means a second time, or ask the same thing again.
- `undo`: they revert a choice they just made (the engine also logs `step_changed`).
- `rage_skip`: 3 or more skips in a row within about a minute.
- `just_do_it`: "just pick", "whatever", "just do it" (also log `speed_mode`, then apply defaults with `--set-by delegated`).
- `error_loop`: the same validation error comes back after a fix.
- `slow`: they say it is slow or taking too long.
Plus: one frustration event per moment, not per sentence; `--note` is optional, 12 words at most, about the step, never about the person.

## 4. `skills/opendesigner/references/zoom.md`
- "The offer after every level": add one optional line before the choices, from `journey.py level-line <level>`; show it only when it prints something.
- After the sketch offer: point to SKILL.md for the one-time sharing question.

## 5. `skills/opendesigner/references/improve.md`
- "In someone's project", step 1: when the log is on and it shows hotspots, `engine.py feedback --from-journey` pre-fills an issue with question ids and counts. The person still opens and submits it themselves.
- One line: an anonymous report can be attached to an issue with `journey.py export --anon`, only with their OK. Shared reports never go through GitHub issues, because that posts under their account.
- "Never edit generated files" list: note that `references/report.schema.json` is hand-written (`build_data.py` does not manage it). Alternative: move it to `synthesis/report.schema.json` and have `build_data.py` copy it into references and `data/`.

## 6. Other skills
- `skills/opendesigner-extend/SKILL.md` and `opendesigner-extract/SKILL.md`: one line each, "If `profile.tracking` is on, log steps as in the opendesigner skill (rules.md, Journey signals)."
- `skills/opendesigner/assets/output/AGENTS-snippet.md`: one line, "`opendesigner/journey/` is a private, git-ignored log; never commit or share it."

## 7. Repository files (one line each)
- `README.md`: in the docs list, "Journey tracker and privacy: docs/JOURNEY-TRACKER.md, docs/PRIVACY.md".
- `CONTRIBUTING.md`: "Run `python3 skills/opendesigner/scripts/test_journey.py` too. Maintainers merge shared reports with `journey.py aggregate` (docs/JOURNEY-TRACKER.md)."
- `.github/workflows/ci.yml`, step "Engine tests": also run `python3 skills/opendesigner/scripts/test_journey.py`.
- `docs/FAQ.md`: "Does OpenDesigner send anything anywhere?" with a one-line answer and a link to PRIVACY.md.
- `tools/build_dist.py`, `BUNDLE`: add `scripts/journey.py`, `references/pacing.json` and `references/report.schema.json`, because the sub-skill zips carry the engine, and the engine imports journey.
- `chatgpt-project/instructions.md`: one line, "The journey log needs code execution; without it, skip logging and the sharing question."

## 8. When the maintainers host the receiver (Kunal's decision)
- Deploy `server/telemetry/` (README there). Then set `DEFAULT_REPORTS_URL` in journey.py (read after `OPENDESIGNER_REPORTS_URL` and `profile.reports_url`), publish the address in docs/PRIVACY.md, and change the consent line "Until it is set up, reports wait on this computer." Reports already in people's outboxes go with their next `share`.

## 9. Rebuild and check
```
python3 tools/build_data.py && python3 tools/sync_skills.py
python3 tools/build_data.py --check && python3 tools/sync_skills.py --check
python3 tools/build_dist.py --check && python3 tools/jev_nav.py check && python3 tools/check_links.py
python3 skills/opendesigner/scripts/test_engine.py && python3 skills/opendesigner/scripts/test_journey.py
python3 tools/readability.py docs/JOURNEY-TRACKER.md docs/PRIVACY.md
```
Then a dry run from scratch in a temp folder: init, consent on, sketch through the engine, `journey.py report`, `journey.py share --dry-run`, and check that the JSON holds only schema fields.
