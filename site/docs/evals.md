---
title: Evals: how we test OpenDesigner
seo_title: OpenDesigner evals: how we test it, with every result
description: How OpenDesigner tests itself, what each test can and can't show yet, and every saved result with its date and number of runs, failures included.
section: Reference
order: 7
updated: 2026-11-05
---

An eval here is a fixed task with fixed checks and a saved result. Each one answers a question you might ask before trusting OpenDesigner. Every number on this page is read from the result files in the repository, with its date and how many times it ran, and failures stay on the page until they pass.

{{evals:summary}}

## What these numbers don't show yet

- **Nobody has been watched using it.** These tests use AI agents and fixed inputs. We have not yet watched people install OpenDesigner and use it on their own product. That test is next ([field plan](https://github.com/ckryptickunal/OpenDesigner/blob/main/docs/FIELD-PLAN.md)).
- **One AI tool.** The agent tasks run in Claude Code. The other tools OpenDesigner installs into have not been tested this way yet.
- **Small samples.** The last full agent run tried each task 3 times on each side. Later runs tried one task once, and the tables mark those as weak evidence.
- **We wrote the tests, and we have changed some.** On 23 October two checks changed: the extend task now allows the bookkeeping a rebuild does, and the identity task now also checks that the skill ran. A test we didn't think of can't fail, so you can [run them yourself](#run-them-yourself) and add your own.
- **AI judges.** Where a check needs judgment, such as "asks one plain question", a second model votes three times and the majority counts. Most checks are plain facts instead: a file was written, the brand color appears exactly as typed.
- **The maintainer outranks every score.** In the showcase, the maintainer's verdict decides what stays, whatever the numbers say.

## Does it do better than a plain AI?

The same agent does each task twice: once with OpenDesigner loaded and once without it. Checks score what it produced. The tasks below are ones a capable AI could do on its own, so the comparison is fair: refusing to copy another brand, catching text that fails contrast, building a system from five answers, auditing a page before redesigning it.

{{evals:agent}}

A small difference is a result too. On a task any good model already does, such as spotting text that fails contrast, OpenDesigner adds little, and the table shows it. Every saved run is listed. The first full run on 20 October scored lower on several tasks; the full run shown came from the same commit later that day, after changes that weren't recorded, so both are kept.

### Jobs that need OpenDesigner's own files

These tasks use OpenDesigner's engine and records: changing one decision and rebuilding, or choosing styles from a taste poll. An AI without OpenDesigner can't do them, so the "Without" column is expected to be low and is left out of the comparison above. The question here is whether the job works with it. Two of the three taste tasks scored 0% in their only run: the OpenDesigner skill did not start for that question on its own. They stay listed until it does. The third has not run yet.

{{evals:agent-tools}}

### Before and after a fix

When an eval finds a real fault, the fix is measured the same way. The same task and the same checks run on the skills from before the change and on the skills after it.

{{evals:agent-changes}}

## Is what it makes accessible and complete?

The engine builds a design system from each of 19 fixed briefs. No AI is involved, so the same answers always give the same files. Each brief is a person's five sketch answers: a name, a brand color, who uses the product, the platforms and a few feel words. The briefs include the cases that break design systems: yellow, cyan and lime brand colors, colors that are almost black or almost white, large text for older readers, and three platforms at once.

There are two tiers of checks. The required checks are WCAG 2.2 AA and the files you rely on: text contrast at 4.5:1, borders and focus rings at 3:1, 24 px targets, the exact brand color, every export, and the same result twice. The quality checks are house rules that ask for more than WCAG does. A miss there shows where the engine can improve, and the engine must tell the person about it.

{{evals:design}}

Today's quality misses all have the same cause. With a light brand color such as yellow, cyan, lime or near-white, the primary button's fill stands out less than 3:1 from the page. WCAG does not require that when the button has a text label, and the engine already puts dark text on it and warns the person. It is still a weak button, so it stays listed here until the engine does better.

## Does it look good? The showcase, judged blind

The [showcase](/showcase/) is built with OpenDesigner, so it is a test of the whole process. AI reviewers turned out to be kind: designs they scored 4 out of 5, the maintainer called "rubbish". So each design is now compared blind with a shipped product: side by side, no labels, sides in random order, scored for craft. A fresh reviewer then scores it against the B2B product screens. A design that fails stays hidden from the gallery until it passes.

{{evals:showcase}}

## Do our own checks catch mistakes?

OpenDesigner checks its own work with code: a layout checker that measures every page at 13 widths, the review skill's checker, a preflight that reads a page's type and fonts, and date and name checks. Each one is tested on pages with planted mistakes, such as a one-word last line, a button that is too small or a wrong weekday, and on clean pages with none. Recall is the share of planted mistakes it caught. A false alarm is a finding on a clean page.

{{evals:checkers}}

The second table shows the same test pages against older versions of the layout checker. Each new check came from a mistake the maintainer found in a review, such as a word left alone on the last line, or a Copy button floating above its code. The table shows each version catching more of the planted mistakes.

### Bugs the checker evals found in our own checkers

The first run of these evals found bugs in the checkers themselves. Each one was fixed, and the same test pages were run again.

{{evals:checker-changes}}

Two gaps are still open and stay counted as misses: the preflight finds a type scale only when its names contain "font-size", and the name check does not compare names that have a space in them.

## Run them yourself

The design and checker evals are free and run on your machine without an AI:

```bash
python3 tools/design_evals.py
```

```bash
python3 tools/checker_evals.py
```

The agent evals use [`claude plugin eval`](https://code.claude.com/docs/en/plugin-evals). Every run is a real Claude Code session on your own account, so it counts against your plan or API bill (the last full run cost about the amount shown under its table). Start with the quick set:

```bash
python3 tools/agent_evals.py --tag smoke --runs 1
```

To add a task: copy a folder in `evals/`, write the prompt in `prompt.md`, and add one file per check in `graders/`. Then open a pull request. To share your results, or a task where OpenDesigner did badly, [open an eval report](https://github.com/ckryptickunal/OpenDesigner/issues/new?template=eval-result.yml). The bad results help most.
