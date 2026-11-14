---
title: Evals: how we test OpenDesigner
seo_title: OpenDesigner evals: how we test it, with every result
description: How OpenDesigner tests itself, what each test can and can't show yet, and every saved result with its date and number of runs, failures included.
section: Reference
order: 7
updated: 2026-11-10
---

Each test here answers a question you might ask before trusting OpenDesigner. An eval is a fixed task with fixed checks and a saved result, and every number on this page is read from those result files, with its date and how many times it ran. Failures stay on the page until they pass.

{{evals:summary}}

## What these numbers don't show yet

- **Nobody has been watched using it.** These tests use AI agents and fixed inputs. We haven't yet watched people use OpenDesigner on their own product. That test is next ([field plan](https://github.com/ckryptickunal/OpenDesigner/blob/main/docs/FIELD-PLAN.md)).
- **One AI tool.** The agent tasks run in Claude Code. The other tools OpenDesigner installs into haven't been tested this way yet.
- **Small samples.** The last full agent run tried each task 3 times on each side. Later runs tried one task once, and the tables mark those as weak evidence.
- **We wrote the tests, and we have changed some.** On 23 October we changed two checks: the extend task now allows a rebuild's bookkeeping, and the identity task also checks that the skill ran. A test we didn't think of can't fail, so you can [run them yourself](#run-them-yourself) and add your own.
- **AI judges.** Where a check needs judgment, such as "asks one plain question", a second model votes three times and the majority counts. Most checks are plain facts instead: a file was written, the brand color appears exactly as typed.
- **The maintainer outranks every score.** In the showcase, the maintainer's verdict decides what stays, whatever the numbers say.

## Does it do better than a plain AI?

The same agent does each task twice, once with OpenDesigner loaded and once without, and checks score what it made. Each task is one a capable AI could do on its own, such as refusing to copy another brand or auditing a page before redesigning it, so the comparison is fair.

{{evals:agent}}

A small difference is a result too: on a task any good model already does, such as spotting text that fails contrast, OpenDesigner adds little. Every saved run is listed. The first full run on 20 October scored lower on several tasks. The one shown ran on the same commit later that day, after changes that weren't recorded, so both are kept.

### Jobs that need OpenDesigner's own files

These tasks use OpenDesigner's engine and records: changing one decision and rebuilding, or choosing styles from a taste poll. An AI without OpenDesigner can't do them, so the "Without" column is expected to be low and is left out of the comparison above. Two of the three taste tasks scored 0% in their only run, because the OpenDesigner skill did not start for that question on its own. They stay listed until it does. The third hasn't run yet.

{{evals:agent-tools}}

### Before and after a fix

When an eval finds a real fault, the fix is measured the same way: the same task and checks run on the skills from before the change and after it.

{{evals:agent-changes}}

## Is what it makes accessible and complete?

The engine builds a design system from each of 20 fixed briefs. No AI is involved, so the same answers always give the same files. Each brief is a person's five sketch answers, and they include the cases that break design systems, such as a yellow or almost-black brand color, large text for older readers, and three platforms at once.

| Checks | What they ask for |
|---|---|
| Required | WCAG 2.2 AA and the files you rely on: text contrast at 4.5:1, borders and focus rings at 3:1, 24 px targets, the exact brand color, the exports its platforms need, and the same result twice |
| Quality | House rules that ask for more than WCAG does. A miss shows where the engine can improve, and the engine must tell the person about it |

{{evals:design}}

Today's quality misses have one cause: with a light brand color, such as yellow or near-white, the primary button's fill stands out less than 3:1 from the page. WCAG doesn't require that when the button has a text label, and the engine already puts dark text on it and warns the person. It's still a weak button, so it stays listed here until the engine does better.

## Does it look good? The showcase, judged blind

The [showcase](/showcase/) is built with OpenDesigner, so it tests the whole process. AI reviewers turned out to be kind: designs they scored 4 out of 5, the maintainer called "rubbish". So each design is now scored for craft blind, side by side with a shipped product, with no labels and the sides in random order. A fresh reviewer then scores it against the B2B product screens. A design that fails stays hidden from the gallery until it passes.

{{evals:showcase}}

## Do our own checks catch mistakes?

OpenDesigner checks its own work with code, such as a layout checker that measures every page at 13 widths and a preflight that reads a page's type and fonts. Each checker is tested on pages with planted mistakes, such as a button that is too small or a wrong weekday, and on clean pages with none. A false alarm is a finding on a clean page.

{{evals:checkers}}

The second table runs the same test pages against older versions of the layout checker. Each new check came from a mistake the maintainer found in a review, such as a Copy button floating above its code.

### Bugs the checker evals found in our own checkers

The first run found these. Each one was fixed, and the same test pages ran again.

{{evals:checker-changes}}

## Smart UI: does the assistant show the right part?

Smart UI is tested on a small billing app with a real model in the loop (`examples/smart-ui-support/`). 26 questions, three runs each: 21 that need a part, some of them follow-ups, five of them changes like paying an invoice, and 5 that should stay text. Results from 14 November 2026, after two rounds of fixes:

| | Claude Sonnet 5.5 | Gemini 3.1 Pro |
|---|---|---|
| Showed the right part | 86% | 84% |
| Answer passed every check the first time | 94% | 34% |
| Passed after one repair round | 100% | 98% |
| Kept a short fact as text | 100% | 100% |
| Asked for approval before a change | 100% | 93% |
| Changes the model ran on its own | 0 | 0 |

The checks now include wording: headings in sentence case, no filler words, no value shown twice. Gemini's first answers usually fail them (mostly Title Case headings) and pass after the repair round. Both models answered "What plan are we on and when does it renew?" in text, where the test expected a summary card.

When a change didn't get an approval prompt, the model answered in text and nothing happened: changes run only after the person presses the button. The full report, with every miss, is `evals/smart-ui/REPORT.md`.

## Run them yourself

The design and checker evals are free and run on your machine without an AI. The agent evals use [`claude plugin eval`](https://code.claude.com/docs/en/plugin-evals): every run is a real Claude Code session on your own account, so it counts against your plan or API bill (the last full run cost about the amount shown under its table).

:::dev
The design and checker evals:

```bash
python3 tools/design_evals.py
```

```bash
python3 tools/checker_evals.py
```

The agent evals, starting with the quick set:

```bash
python3 tools/agent_evals.py --tag smoke --runs 1
```

To add a task: copy a folder in `evals/`, write the prompt in `prompt.md`, and add one file per check in `graders/`. Then open a pull request.
:::

To share your results, or a task where OpenDesigner did badly, [open an eval report](https://github.com/ckryptickunal/OpenDesigner/issues/new?template=eval-result.yml). The bad results help most.
