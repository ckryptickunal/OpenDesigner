# Privacy: the journey log and shared reports

**In plain words:** OpenDesigner can keep a private diary of the steps you take (the journey log). That diary stays in your project files and is never sent. Separately, and only if you say yes, it can send the OpenDesigner team a small anonymous report. The report says which questions came up, how long they took and where people got stuck. It never sends your answers, your brand, your files or anything you typed. You can see the exact report before it goes, and you can say no or change your mind at any time.

- **Designers:** opt-in, anonymous usage analytics about the interview flow, never about your design.
- **Engineers:** two consents in `opendesigner/state.json` (`profile.tracking`, `profile.share_reports`); an allowlisted JSON payload validated against `skills/opendesigner/references/report.schema.json`; HTTPS POST only after consent; no persistent identifier.

This covers BRIEF requirements 18 and 19. How the log works is in [JOURNEY-TRACKER.md](JOURNEY-TRACKER.md).

## Two separate choices
| | The journey log | Shared reports |
|---|---|---|
| What it is | A diary of your steps, for you | An anonymous summary, for the OpenDesigner team |
| Where it stays | `opendesigner/journey/` in your project, kept out of git | A server run by the maintainers, once one is set up |
| Default | Off until you say yes | Off until you say yes |
| Saved as | `profile.tracking`: `on` or `off` | `profile.share_reports`: `always`, `ask` or `never` |
| Turn off | `journey.py consent off` (add `--forget` to delete the log) | `journey.py share-consent never` |

Saying yes to the log is not saying yes to sharing. The AI asks about sharing separately, later, and only once. For both questions, only a clear yes counts: "whatever", "ok I guess", "idk" or no answer is a no.

## The questions you are asked
**The log question** comes once, in the first message. The AI says "on this computer" only when it runs on your own computer, for example in Claude Code:

> I keep a private log of your steps on this computer so I can make this faster for you. OK?

In a web chat, such as claude.ai or ChatGPT, it says:

> I keep a private log of your steps in your project files so I can make this faster for you. OK?

**The sharing question** comes once, at the end of your first session, after your files are written. It is never in the first message, and it is never asked again once you answer. The AI shows these lines word for word (`journey.py share-consent` prints them):

> Can I send the OpenDesigner team an anonymous report of which steps were slow or confusing, so they can make them faster?
> It never includes your answers, names, colors, files or anything you typed. Share every time, ask me each time, or don't share?
> Say "details" to see exactly what is sent.

If you say "details", the AI shows the full facts, word for word (`journey.py share-consent --details`):

> Why: it shows the OpenDesigner team where people get stuck, so the steps get faster for everyone.
> What is sent: which questions came up, how long each took (to 5 seconds), how you answered (kept the default, picked an option and so on), skips, stops and help requests, plus the OpenDesigner version, the AI tool and the week.
> Never sent: your answers, names, colors, brand, files, paths, links, notes or anything you typed. No ID ties reports to you or your device.
> Where it goes: a small server run by the OpenDesigner maintainers. Until it is set up, reports wait in your project files and nothing is sent.
> How long: reports are kept 12 months; after that only the totals stay.
> To see the exact report first, say "show me".
> Choose: share every time · ask me each time · don't share. To change your mind later, say "stop sharing" or "start sharing".

- **Share every time** (`always`): a report goes when a session or level ends, without asking again.
- **Ask me each time** (`ask`): before each report, the AI asks "Send this session's anonymous report? Say "show me" to see it first." It sends the report only after your yes. A plain "yes" to the sharing question means this choice, and this session's report goes.
- **Don't share** (`never`): nothing is sent, and reports that were waiting to be sent are deleted. A plain "no", or any answer that isn't a clear choice, means this.

To see exactly what would be sent, before or after you choose: `python3 <skill>/scripts/journey.py share --dry-run`. The report that is sent afterwards has exactly that content. If new steps were logged in between, run it again to see the new one.

## Exactly what is sent
Nothing outside this list can be sent. The list is enforced twice:
- `journey.py` builds the report from an allowlist and checks it against `report.schema.json`;
- the receiver refuses anything that does not match the same schema.

Every object in the schema is closed. Every piece of text is a fixed word or a fixed pattern, and every number has limits.

| Field | Example | What it is |
|---|---|---|
| `schema` | `opendesigner-report/1` | The report format |
| `report_id` | `8fa132f9b5e9a9b9` | Random and new for every report, so two reports can't be linked |
| `version` | `0.1.0` | The OpenDesigner version |
| `host` | `claude-code` | The AI tool, as one word from a fixed list (or `unknown`) |
| `week` | `2026-W39` | The week the report was made: no day, time or timezone |
| `sessions` | `2` | How many sittings the report covers |
| `secs_total` | `635` | Total time, rounded to 5 seconds |
| `levels` | `sketch: completed 1, steps_taken 6, fewest 5, planned 5, secs 205, planned_min 5` | Per zoom level: finished or not, steps taken, the shortest path, the planned questions, time rounded to 5 seconds, planned minutes |
| `events` | `step_shown: 17, help: 2` | How many times each event type happened |
| `questions` | `Q-shape-01: shown 1, answered 1, how default 1, secs [10]` | Only ids from the public questionnaire (`references/questions.json`). For each: counts (shown, answered, skipped, changed, dropped, extra turns, help requests, errors, asked to go faster), how it was answered (`default`, `option`, `free`, `delegated`, `reference`), frustration signal counts (`said`, `repeat_question`, `undo`, `rage_skip`, `just_do_it`, `error_loop`, `slow`) and timings rounded to 5 seconds |

## Never sent
Your answers or the values you chose. Names of people, products, companies or projects. Brand facts, colors, fonts or logos. File names, folders or paths. Links, including the reference sites you shared. Notes, including the short frustration notes in your local log. Code. Anything you typed. Your timezone, the exact date or time. Session ids, or any id that stays the same between reports.

A step that is not a public question id is dropped from the report, not sent. An example is a name typed by mistake into a step.

## How it is sent, and where it goes
- Sending uses a plain HTTPS request with a 5-second timeout, to the address in the `OPENDESIGNER_REPORTS_URL` environment variable or `profile.reports_url` in `state.json`.
- **Right now no server is collecting reports.** Until the maintainers set one up and publish its address here, nothing is sent. A report you agree to share is saved in your project, in `opendesigner/journey/outbox/`, and `journey.py share` says so plainly.
- If the server can't be reached, the report waits in the outbox and goes with the next one. Nothing is retried in the background.
- Reports are never filed as GitHub issues, because an issue is posted under your GitHub account and would show who you are.

## What the server keeps
The reference receiver in `server/telemetry/` (a Cloudflare Worker, not deployed yet) is built to keep as little as possible:
- It stores the report and the week it arrived. Nothing else.
- Every web request carries your IP address; that is how the internet works. The receiver uses it only as a counter key to stop floods. The rate limiter holds it for one minute, and it is never stored. It does not read or store the user agent, other headers or the exact time.
- Request logging (Cloudflare Workers Logs) is turned off in the example configuration.
- The hosting provider handles the connection under its own policies. OpenDesigner does not add any tracking of its own.

## How long reports are kept
Raw reports are kept for 12 months, then deleted automatically (a weekly cleanup in the receiver). Totals made from them are kept and may be published, because they can't be traced to anyone. These totals are the aggregate journey report: counts, rates and averages per question.

## Changing your mind
- Stop sharing: `python3 <skill>/scripts/journey.py share-consent never`. Reports still waiting in the outbox are deleted.
- Stop the local log, and delete it: `python3 <skill>/scripts/journey.py consent off --forget`.
- Reports already sent can't be found or deleted one by one, because nothing in them points to you. That is the design, not an oversight.
- Questions or concerns: open an issue at github.com/ckryptickunal/OpenDesigner.
