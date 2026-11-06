---
title: How it works
seo_title: How OpenDesigner works, step by step, from install to review
description: Every step OpenDesigner takes, in order: reading your project, the sketch, a first build, zooming in, the checks, the files it writes, and later changes.
section: Reference
order: 1
updated: 2026-11-07
---

OpenDesigner works inside the AI tool you already use, and a small Python engine does the math. To see it drawn, with the real numbers, open [How OpenDesigner works](/tour/).

## The steps, from your side

1. **Add it to your AI tool** with one or two commands. See [Install](/docs/install/).
2. **Say "Create a design system for this project."**
3. **It reads before it asks:** your styles, tokens, logo and fonts. It skips what a file already answers.
4. **It asks once about a private log** of your steps. Only a clear yes turns it on.
5. **The sketch: up to five questions, one per message.** What you are making, who it is for, where it runs, how it should feel, and your brand color or logo. Each comes with a suggested answer and its reason. Answer in your own words, or say "just pick".
6. **You get a complete first version** in a few seconds: every token, the code for your platforms, your rules in plain words, and an overview page that marks each area Chosen, Picked for you, Default or Not enough information.
7. **It offers to research your users.** About 10 minutes, and it does the work after one yes: a table of competitors, a positioning for you to confirm and three directions on one board. Say no, and it doesn't ask again.
8. **Zoom in only where you care, or stop.** See [Zoom levels](/docs/zoom-levels/).
9. **It checks its own work.** Fixed rules check contrast, target sizes, focus rings and reduced motion before the AI gives any opinion. Errors block the build.
10. **It writes everything down,** and asks before adding a short note for your other AI agents, so later sessions follow the same rules.
11. **Later changes** read the decision log first. A review finds values in your code that skip the system and names the right one to use.
12. **If something is confusing or broken,** it saves a note with a ready-to-file GitHub link. Nothing is posted unless you submit it.

## Four things you can ask for

Your AI picks the skill from your words; there are no extra commands to learn.

| Ask for | What happens |
|---|---|
| **Audit** what you have | It measures your site, repo, Figma file or brand book, then checks the built screens at every size and theme |
| **Establish** a system | The five-question sketch and a complete first build |
| **Improve** it | A change to the system, with what it would move named first |
| **Check** the work | Fixed rules on the code and the page, then what still needs your eye |

:::dev
| Job | What runs |
|---|---|
| Audit | the extract skill, then the review skill |
| Establish | `engine.py sketch`, then `engine.py build` |
| Improve | the extend skill, which reads `opendesigner/decisions.md` first |
| Check | `engine.py review` on the code, the review skill on the page, the preflight skill before you share |

The note for other agents goes in your `AGENTS.md`. The overview page is `opendesigner/overview.html`.
:::

## Two parts: written instructions and an engine

The skills are written instructions your AI follows, and the questions follow a decision graph, so nothing is asked before what it depends on. The Python engine does the math: color ramps, type and spacing scales, contrast checks and every export. It uses only Python's standard library, makes no network calls, and gives the same files for the same answers, with or without an AI. See [Engine commands](/docs/engine/).

{{figure:how-it-works-pipeline}}

## How your answers become a system

Your answers move [eight dials](/docs/dials/), such as Density and Roundness, each from 0 to 100. Each position maps to concrete values, like a corner radius or a motion duration, and feel words like "calm" move several dials at once. Every answer is recorded with how it was set; a suggestion you didn't answer is never recorded as your decision. See [Decisions, DESIGN.md and the overview page](/docs/decisions/).

### Your taste

Your taste can move the dials too, but only as a suggestion you confirm.

- **The taste poll** (optional, about 5 minutes): you rate 20 to 30 real screens from shipped products. The screens come from Mobbin, so the poll needs your own Mobbin access, and the images stay on your computer.
- **The taste index** merges every taste signal in your project into a value and a confidence per dial, plus red lines. It asks you to confirm what it's sure of, never offers an option past a red line, and a review tells you when the system drifts from your taste.
- **The taste card** is five lines at the top of `DESIGN.md`. Your picture of the look and the Never list only ever come from you.

Taste never moves an accessibility floor or a house standard, and it stays in your project.

## Showing choices

It shows each choice in the most visual way your AI tool allows, from a page in the chat to numbered options, and never waits on a picture to move on. Ten templates draw the choices, each with a button that copies your pick back into the chat. Clicking choices inside the AI tool is planned ([issue #20](https://github.com/ckryptickunal/OpenDesigner/issues/20)).

## References and assets

Share a website, screenshot, Figma file, repo or brand book at any time: the extract skill measures it and offers each value as a suggestion. Another brand's name, logo, images and words never come across; exact colors and font names do only in a Taste Index you ask for. See [Start from an existing app or brand](/docs/existing-product/).

For a logo, icons, illustration, photos, a brand typeface or a voice guide, it asks you. See [Brand assets](/docs/brand-assets/).

## The checks

Rule-based checks run first and give the same result every time: breaking an accessibility rule is an error, breaking a taste rule a warning. The AI critiques only after the system passes. See [Accessibility floors](/docs/accessibility/).

- **Checked by rules:** contrast, target sizes, focus rings and reduced motion; hard-coded values that skip the tokens; `DESIGN.md` sections that no longer match; and, on the built page, sizes off the scale, missing focus rings, overflow and fonts that did not load.
- **Judged by the AI and by you:** hierarchy, personality, and whether a page looks generic. The AI says what it measured and what it only saw, and its score can rule work out but never approve it: your verdict wins.
- **Nothing rewrites your interface on its own.** The checks only report. A fix to code you already have waits for your yes.

House standards also apply: 457 rules from sources the project owner marked non-negotiable and from the owner's own rules, applied where they fit your platforms and locked.

{{figure:how-it-works-checks}}

## Files, later changes and privacy

- **Files:** `DESIGN.md` and `PRODUCT.md` at the root, and an `opendesigner/` folder with tokens, exports, the overview page and the decision log. See [The files it writes](/docs/files/).
- **Later changes:** see [Change or extend a system](/docs/extend/).
- **Privacy:** the private log stays in your project, out of git. Anonymous reports are a separate yes, and no server collects them yet. See the [privacy page](https://github.com/ckryptickunal/OpenDesigner/blob/main/docs/PRIVACY.md).
- **Defaults:** they rest on more than 500 Decision Cards, each with its sources. See the [research map](https://github.com/ckryptickunal/OpenDesigner/blob/main/docs/RESEARCH.md).
