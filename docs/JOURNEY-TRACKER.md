# Journey tracker

**In plain words:** while OpenDesigner helps you build a design system, it can keep a private diary of your steps. It notes which questions you saw, how you answered, where you got stuck, and where you stopped. The diary stays in your project files. It shows where the process is slower than it needs to be, so it can get shorter.

- **Designers:** a funnel and friction log for the design-system interview, with drop-off points and time per step.
- **Engineers:** an append-only JSONL event log (`opendesigner/journey/events.jsonl`) plus a report generator; stdlib Python, no network unless you opt in to sharing.

It covers BRIEF requirement 18 (the local log). Sending anonymous reports to the maintainers is a separate choice, covered in [PRIVACY.md](PRIVACY.md) (requirement 19).

## Asking first
Nothing is logged until you say yes. The first time, the AI asks one line. It says "on this computer" only when it runs on your own computer, for example in Claude Code:

> I keep a private log of your steps on this computer so I can make this faster for you. OK?

In a web chat, such as claude.ai or ChatGPT, it says:

> I keep a private log of your steps in your project files so I can make this faster for you. OK?

Only a clear yes turns the log on. "Whatever", "ok I guess", "idk" or no answer counts as no. Your answer is saved as `profile.tracking` in `opendesigner/state.json` (`on` or `off`). If it is missing, the tracker logs nothing and prints the question for the AI to ask (`journey.py consent --where local|web`).

Sharing an anonymous report is a separate question, asked once at the end of your first session ([PRIVACY.md](PRIVACY.md)). It is short:

> Can I send the OpenDesigner team an anonymous report of which steps were slow or confusing, so they can make them faster?
> It never includes your answers, names, colors, files or anything you typed. Share every time, ask me each time, or don't share?
> Say "details" to see exactly what is sent.

Saying "details" shows the full facts:

> Why: it shows the OpenDesigner team where people get stuck, so the steps get faster for everyone.
> What is sent: which questions came up, how long each took (to 5 seconds), how you answered (kept the default, picked an option and so on), skips, stops and help requests, plus the OpenDesigner version, the AI tool and the week.
> Never sent: your answers, names, colors, brand, files, paths, links, notes or anything you typed. No ID ties reports to you or your device.
> Where it goes: a small server run by the OpenDesigner maintainers. Until it is set up, reports wait in your project files and nothing is sent.
> How long: reports are kept 12 months; after that only the totals stay.
> To see the exact report first, say "show me".
> Choose: share every time · ask me each time · don't share. To change your mind later, say "stop sharing" or "start sharing".

With "ask me each time", the AI asks before each report: "Send this session's anonymous report? Say "show me" to see it first."

## What it records
Each line of `events.jsonl` is one event. It has a time and a session (S001, S002 and so on). The step is a question id such as `Q-shape-01`, a stage id, or an engine command. Each event also has the zoom level, the area and a few details.

| Event | What it means |
|---|---|
| `session_start` | You started working. Logged by itself when a new session begins (after 30 quiet minutes, or after `session_end`). A final review or export right after `session_end` stays in the session that just ended. |
| `session_end` | You stopped on purpose: you said stop, or the finish steps ran. |
| `step_shown` | A question or screen was put in front of you. |
| `step_answered` | You answered it. `--how`: `default` (kept the recommendation), `option`, `free` (your own answer), `delegated` ("you choose"), `reference` (taken from a reference). Optional `--secs` and `--turns`. |
| `step_skipped` | You or a rule skipped it. `--reason`: `person`, `rule`, `known` (your files or earlier words already answered it), `speed`, `later`. |
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
The engine logs its own steps: answers and changed answers from `pick`, `set` and `sketch`, the finished sketch, errors, exports, reviews and feedback. It never logs the values. The AI logs what only it can see: what it showed, help, frustration, requests to go faster and the end of a session.

The level and area are filled in from `references/questions.json` when the step is a question id. If the engine and the AI both log the same answer within two minutes, it counts once.

`help`, `frustration` and `speed_mode` without `--step` belong to the step on screen, and the log records that step with the event. A step stops being on screen when it is answered or skipped, when a level finishes, and when a session ends. A signal with nothing on screen is counted "between steps", never on an older question. `--area color` counts it against a whole area. Messages that are not questionnaire questions have moment ids, which the AI logs with `step_shown` so signals about them land there: `consent.share`, `result`, `offer`, `finish.agents` and `finish.feedback`. Moment ids never go into the anonymous report.

A question skipped with `--reason rule` or `--reason known` (their files or earlier words already answered it) was never in front of the person. It is not counted as a step taken, and it is left out of the default-kept counts.

## Reading the report
```
python3 <skill>/scripts/journey.py report          writes opendesigner/journey/JOURNEY.md, prints the short version
python3 <skill>/scripts/journey.py report --json   all the numbers
python3 <skill>/scripts/journey.py level-line sketch     one line for the offer after a level, only when 3 or more steps could have been saved
python3 <skill>/scripts/engine.py feedback --from-journey   a feedback note with the hotspots: question ids and counts only
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
- **Funnel by level** and **by area:** how many steps were reached, answered, skipped and dropped, at each zoom level and in each area. It also shows whether the level finished.
- **Steps taken / shortest:** steps taken counts every time a step was shown, plus extra back-and-forth (from `--turns`, or one per help request). The shortest path is one message per question reached. A question asked in the same message as another (Q-scope-06 with Q-scope-01, Q-brand-03 with Q-color-01) is not a separate step. **Planned questions** and **minutes** come from `references/pacing.json`.
- **Where it stopped:** a drop-off is a step still on screen when a session ended without `session_end` and without finishing a level. The session you are in now is not counted until it has been quiet for 30 minutes.
- **Frustration** and **help hotspots:** the steps with the most signals or help requests.
- **Changed answers.**
- **Speed-ups to try**, from four signals:
  - frustration: 2 or more signals, so reword or split it;
  - help: 2 or more requests, so put the explanation in the question;
  - drop-offs;
  - defaults: a low- or medium-impact question is a candidate to auto-apply if its default stayed at least 80% of the time. Stayed means accepted, skipped or handed over ("you choose"). A high-impact question whose default was accepted stays a question, with the default as a one-tap yes. A high-impact question people hand over is one to pick for people in a hurry, listed in one line.
- **Default kept, per question.**
- **Slowest steps**, against the planned 60, 30 or 15 seconds for high, medium and low impact.
- Everything else: errors, exports, reviews, feedback and requests to go faster.

## For maintainers: many reports into one
People who choose to share send an anonymous report (see [PRIVACY.md](PRIVACY.md)); anyone can also attach one to an issue with `journey.py export --anon`. To merge many:
```
python3 <skill>/scripts/journey.py aggregate reports/ more.json --out journeys.md     Markdown report
python3 <skill>/scripts/journey.py aggregate reports/ --out journeys.json            merged numbers
python3 server/telemetry/aggregate_reports.py reports.json --out journeys.md         from the report server's export
```
It reads report files, lists of them, folders, and the report server's database export. It also reads raw `events.jsonl` logs, which it turns into anonymous reports first. Every report is checked against `references/report.schema.json`; reports that fail are skipped and counted, and a report that appears twice counts once. In the merged report, counts are per report, and a speed-up needs at least 3 answers.
