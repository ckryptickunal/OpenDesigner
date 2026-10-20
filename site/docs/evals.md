---
title: Evals: how we test OpenDesigner
seo_title: OpenDesigner evals: how we test it, with the numbers
description: How OpenDesigner tests itself: agent tasks with and without the plugin, systems built from fixed briefs, and checkers on planted mistakes.
section: Reference
order: 7
updated: 2026-10-20
---

A tool that says it makes your product look consistent should prove it. These are the tests OpenDesigner runs on itself. The numbers on this page come straight from the result files in the repository, and every one has its date, its version and its cost. When a test fails, it says so here.

{{evals:summary}}

There are four kinds of test:

- **Agent evals:** an AI agent gets a small task, such as "set up a design system from these five answers". It does the task twice: once with OpenDesigner loaded and once without it. Checks score what it produced.
- **Design evals:** the engine builds a design system from each of 18 fixed briefs. No AI is involved, so the same answers always give the same result.
- **Checker evals:** test pages with planted mistakes, such as a one-word last line, a button that is too small or a wrong weekday. They show whether our own checkers catch each mistake.
- **The showcase audit:** the designs in the [showcase](/showcase/), judged against shipped products before and after the rebuild.

## Agent evals: with and without OpenDesigner

Each task runs three times with the plugin and three times without it, and the score is the share of checks that passed. Most checks need no AI judge. They check facts: a file was written, the brand color appears exactly as typed, the agent named the 4.5:1 contrast floor. Where a rule needs judgment, such as "asks one plain question", a second model votes three times and the majority counts.

{{evals:agent}}

The "Without" column is the same agent with no plugin. It shows what OpenDesigner adds. For a task any capable model already does well, such as spotting text that fails contrast, the difference is small, and the table shows that too.

### Before and after a fix

When an eval finds a real fault, the fix is measured the same way. The same task and the same checks run on the skills from before the change and on the skills after it.

{{evals:agent-changes}}

## Design evals: 18 briefs, no AI

Each brief is a person's five sketch answers: a name, a brand color, who uses the product, the platforms and a few feel words. The briefs include the cases that break design systems: yellow, cyan and lime brand colors, colors that are almost black or almost white, large text for older readers, and three platforms at once.

There are two tiers of checks. The required checks are WCAG 2.2 AA and the files you rely on: text contrast at 4.5:1, borders and focus rings at 3:1, 24 px targets, the exact brand color, every export, and the same result twice. The quality checks are house rules that ask for more than WCAG does. A miss there shows where the engine can improve, and the engine must tell the person about it.

{{evals:design}}

Today's quality misses all have the same cause. With a light brand color such as yellow, cyan, lime or near-white, the primary button's fill stands out less than 3:1 from the page. WCAG does not require that when the button has a text label, and the engine already puts dark text on it and warns the person. It is still a weak button, so it stays listed here until the engine does better.

## Checker evals: do our checks catch mistakes?

OpenDesigner checks its own work with code: a layout checker that measures every page at 13 widths, a preflight that reads a page's type and fonts, and date and name checks. Each one is tested on pages with planted mistakes and on clean pages with none. Recall is the share of planted mistakes it caught. A false alarm is a finding on a clean page.

{{evals:checkers}}

The second table shows the same test pages against older versions of the layout checker. Each new check came from a mistake the maintainer found in a review, such as a word left alone on the last line, or a Copy button floating above its code. The table shows each version catching more of the planted mistakes.

### Bugs the checker evals found in our own checkers

The first run of these evals found bugs in the checkers themselves. Each one was fixed, and the same test pages were run again.

{{evals:checker-changes}}

Two gaps are still open and stay counted as misses: the preflight finds a type scale only when its names contain "font-size", and the name check does not compare names that have a space in them.

## The showcase audit, before and after

The [showcase](/showcase/) is built with OpenDesigner, so it is a test of the whole process. AI reviewers turned out to be kind: designs they scored 4 out of 5, the maintainer called "rubbish". So each design is now compared blind with a shipped product: side by side, no labels, sides in random order, scored for craft. A fresh reviewer then scores it against the B2B product screens. A design that fails stays hidden from the gallery until it passes.

{{evals:showcase}}

## What these tests don't prove

- **Small samples.** Eight agent tasks with three runs each show a direction, not a guarantee. Agents vary from run to run.
- **AI judges.** Where a check needs judgment, a model votes. Its votes can differ between runs, so the checks a model judges are kept few and specific, and as many checks as possible are plain facts.
- **Our own tests.** We wrote these tests. A test we didn't think of can't fail. That is why you can [run them yourself](#run-them-yourself) and add your own.
- **The maintainer outranks every score.** In the showcase, the maintainer's verdict decides what stays, whatever the numbers say.

## Run them yourself

The design and checker evals are free and run on your machine without an AI:

```bash
python3 tools/design_evals.py
```

```bash
python3 tools/checker_evals.py
```

The agent evals use [`claude plugin eval`](https://code.claude.com/docs/en/plugin-evals). Every run is a real Claude Code session on your own account, so it counts against your plan or API bill (the last full run cost about the amount shown above). Start with the quick set:

```bash
python3 tools/agent_evals.py --tag smoke --runs 1
```

To add a task: copy a folder in `evals/`, write the prompt in `prompt.md`, and add one file per check in `graders/`. Then open a pull request. To share your results, or a task where OpenDesigner did badly, [open an eval report](https://github.com/ckryptickunal/OpenDesigner/issues/new?template=eval-result.yml). The bad results help most.
