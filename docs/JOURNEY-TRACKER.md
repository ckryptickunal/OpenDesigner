# Journey tracker

**In plain words:** while OpenDesigner helps you build a design system, it can keep a private diary of the steps you took: which questions you saw, how you answered, where you got stuck, and where you stopped. The diary stays on your computer. It shows where the process is slower than it needs to be, so it can get shorter.

- **Designers:** a funnel and friction log for the design-system interview, with drop-off points and time per step.
- **Engineers:** an append-only JSONL event log (`opendesigner/journey/events.jsonl`) plus a report generator; stdlib Python, no network unless you opt in to sharing.

It covers BRIEF requirement 18 (the local log). Sending anonymous reports to the maintainers is a separate choice, covered in [PRIVACY.md](PRIVACY.md) (requirement 19).

## Asking first
Nothing is logged until you say yes. The first time, the AI asks one line:

> I keep a private log of your steps on this computer so I can make this faster for you. OK?

Your answer is saved as `profile.tracking` in `opendesigner/state.json` (`on` or `off`). If it is missing, the tracker logs nothing and prints that question for the AI to ask.

## What it records
Each line of `events.jsonl` is one event with a time, a session (S001, S002 and so on), the step (a question id such as `Q-shape-01`, a stage id, or an engine command), the zoom level, the area and a few details.

| Event | What it means |
|---|---|
| `session_start` | You started working. Logged by itself when a new session begins (after 30 quiet minutes, or after `session_end`). |
| `session_end` | You stopped on purpose: you said stop, or the finish steps ran. |
| `step_shown` | A question or screen was put in front of you. |
| `step_answered` | You answered it. `--how`: `default` (kept the recommendation), `option`, `free` (your own answer), `delegated` ("you choose"), `reference` (taken from a reference). Optional `--secs` and `--turns`. |
| `step_skipped` | You or a rule skipped it. `--reason`: `person`, `rule`, `known` (a file already answered it), `speed`, `later`. |
| `step_changed` | You changed an earlier answer. |
| `help` | You asked for help. `--kind`: `explain`, `voice_switch`, `glossary`, `example`. |
| `frustration` | You seemed stuck or annoyed. `--signal`: `said`, `repeat_question`, `undo`, `rage_skip`, `just_do_it`, `error_loop`, `slow`. Optional `--note` of at most 12 words. |
| `error` | The engine reported errors (for example from validate). `--count`. |
| `level_complete` | A zoom level finished: `sketch`, `broad`, `defined` or `detailed`. |
| `export` | Files were exported. `--kind` is the format. |
| `review` | The end-of-implementation review ran. |
| `feedback_filed` | A gap, bug, confusing step or idea was recorded. |
| `speed_mode` | You asked to go faster. |

## What it never records
Your answers, colors, names, brand, file contents, code or links. Notes are cut to 12 words, and emails, links, file paths, color codes and phone-like numbers are removed from them. A note says how a step felt, never who you are.

## Where it lives
`opendesigner/journey/` in your project:
- `events.jsonl`: the log, one event per line, only ever added to
- `JOURNEY.md`: the latest report
- `anonymous-report.json`, `pending.json`, `shared.json`, `outbox/`: used only if you export or share (see [PRIVACY.md](PRIVACY.md))
- `.gitignore`: keeps the whole folder out of git, so it is not committed or pushed by accident

## Turn it off, or delete it
```
python3 <skill>/scripts/journey.py consent off            stop logging, keep what is there
python3 <skill>/scripts/journey.py consent off --forget   stop logging and delete opendesigner/journey/
python3 <skill>/scripts/journey.py consent on             start again
python3 <skill>/scripts/journey.py consent                show the current setting
```
Deleting the `opendesigner/journey/` folder by hand does the same as `--forget`. `<skill>` is the opendesigner skill folder, for example `skills/opendesigner`.

## Logging (what the AI runs)
```
python3 <skill>/scripts/journey.py log step_shown --step Q-shape-01
python3 <skill>/scripts/journey.py log step_answered --step Q-shape-01 --how default
python3 <skill>/scripts/journey.py log help --kind explain
python3 <skill>/scripts/journey.py log frustration --signal repeat_question --note "unsure what density means"
python3 <skill>/scripts/journey.py log speed_mode
python3 <skill>/scripts/journey.py events                  every event and value, in plain words
```
The level and area are filled in from `references/questions.json` when the step is a question id. `help`, `frustration` and `speed_mode` without `--step` attach to the step on screen. If the engine and the AI both log the same answer within two minutes, it counts once.

## Reading the report
```
python3 <skill>/scripts/journey.py report          writes opendesigner/journey/JOURNEY.md, prints the short version
python3 <skill>/scripts/journey.py report --json   all the numbers
```
The short version looks like this (a synthetic test run):
```
2 sessions, 11 min in total. 17 steps taken: 14 answered, 1 skipped, 1 dropped.
Shortest path for what was covered: 14 steps, one per question; you took 17 (82% efficient).
Stopped at: Q-color-02 (Where should your brand color appear: only on...).
Most frustrating: Q-color-02 (Where should your brand color appear: only on...), 2 signals.
Top speed-up: Q-color-02: 2 frustration signals: reword it, split it, or show a visual.
```
JOURNEY.md then has these sections:
- **Funnel by level** and **by area:** how many steps were reached, answered, skipped and dropped at each zoom level and in each area, and whether the level finished.
- **Steps taken / shortest:** steps taken counts every time a step was shown, plus extra back-and-forth (from `--turns`, or one per help request). The shortest path is one message per question reached. A question asked in the same message as another (Q-brand-03 with Q-color-01) is not a separate step. **Planned questions** and **minutes** come from `references/pacing.json`.
- **Where it stopped:** a drop-off is a step still on screen when a session ended without `session_end` and without finishing a level. The session you are in now is not counted until it has been quiet for 30 minutes.
- **Frustration** and **help hotspots:** the steps with the most signals or help requests.
- **Changed answers.**
- **Speed-ups to try:** frustration (2 or more signals: reword or split it), help (2 or more: put the explanation in the question), drop-offs, and defaults. A question whose default was kept at least 80% of the time (accepted, delegated or skipped) is a candidate to auto-apply when its impact is low or medium; high-impact ones stay as questions with the default as a one-tap yes.
- **Default kept, per question**, **slowest steps** (against the planned 60, 30 or 15 seconds for high, medium and low impact), and everything else: errors, exports, reviews, feedback and requests to go faster.

## For maintainers: many reports into one
People who choose to share send an anonymous report (see [PRIVACY.md](PRIVACY.md)); anyone can also attach one to an issue with `journey.py export --anon`. To merge many:
```
python3 <skill>/scripts/journey.py aggregate reports/ more.json --out journeys.md     Markdown report
python3 <skill>/scripts/journey.py aggregate reports/ --out journeys.json            merged numbers
python3 server/telemetry/aggregate_reports.py reports.json --out journeys.md         from the report server's export
```
It reads report files, lists of them, the report server's database export, folders, or raw `events.jsonl` logs (turned into anonymous reports first). Every report is checked against `references/report.schema.json`; reports that fail are skipped and counted, and a report that appears twice counts once. In the merged report, counts are per report, and a speed-up needs at least 3 answers.
