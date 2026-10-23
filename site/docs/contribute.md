---
title: Contribute to OpenDesigner
seo_title: Contribute to OpenDesigner: issues, pull requests and evals
description: How to help OpenDesigner: report where it breaks, fix a fact or a skill, add an eval, or open a pull request. You don't need to be a designer.
section: Reference
order: 9
updated: 2026-10-21
---

OpenDesigner is free and open source, and most of what improves it starts with someone using it on a real project. You don't need to be a designer. Engineers, designers, accessibility specialists, writers and AI agents all have useful work here. The full guide is [`CONTRIBUTING.md`](https://github.com/ckryptickunal/OpenDesigner/blob/main/CONTRIBUTING.md).

## The quickest ways to help

- **Tell us where it broke.** [Open an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new/choose), or ask your AI to draft one: `engine.py feedback "what happened" --kind gap|bug|confusing|idea` writes the report, and nothing is posted until you say so.
- **Pick a small task.** Each [good first issue](https://github.com/ckryptickunal/OpenDesigner/labels/good%20first%20issue) names its files and its source.
- **Run the evals and share the result.** The design and checker evals are free and run on your machine ([evals](/docs/evals/)). A task where OpenDesigner did badly helps most.
- **Fix a wrong fact.** Every claim in the research carries a source or is marked as inferred. If one is wrong, a [research correction](https://github.com/ckryptickunal/OpenDesigner/issues/new?template=research-correction.yml) with the better source fixes it for everyone.

## Opening a pull request

1. Fork the repository and make your change in `skills/`, `synthesis/` or `research/`. Some folders are generated from those, and the checks tell you to rebuild them.
2. Run the checks listed under "Before you commit" in [`AGENTS.md`](https://github.com/ckryptickunal/OpenDesigner/blob/main/AGENTS.md#before-you-commit). The CI workflow (`.github/workflows/ci.yml`) is set up to run the same checks on every push and pull request, but GitHub has no runs of it recorded yet, so run them yourself.
3. Say in the pull request what you changed, why, and what you checked.

Every pull request gets a security scan, a check that it fits the project's goal, and a fact check before the maintainer decides. The process is in [`.claude/skills/od-pr-review/SKILL.md`](https://github.com/ckryptickunal/OpenDesigner/blob/main/.claude/skills/od-pr-review/SKILL.md).

## Sharing it

If OpenDesigner helped you, a star on [GitHub](https://github.com/ckryptickunal/OpenDesigner) or a word to a colleague helps other people find it. What changed lately is in the [changelog](/changelog/).
