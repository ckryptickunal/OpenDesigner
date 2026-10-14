---
title: How it works
seo_title: How OpenDesigner works, step by step, from install to review
description: Every step OpenDesigner takes, in order: reading your project, the sketch, a first build, zooming in, the checks, the files it writes, and later changes.
section: Reference
order: 1
updated: 2026-10-15
---

OpenDesigner works inside the AI tool you already use: it reads your project, asks up to five questions, and builds a complete first version with a Python engine. You then zoom in only where you care. It checks the result with fixed rules, writes every decision down, and keeps later changes consistent.

## The steps, from your side

Other AI tools follow the same steps, and some show the choices as text.

1. **Add it to your AI tool.** One or two commands. See [Install](/docs/install/).
2. **Say "Create a design system for this project."**
3. **It looks before it asks.** It reads your CSS, Tailwind config, `package.json`, token files, logo and font files. It doesn't ask what a file already answers.
4. **It asks once about a private log** of your steps. Only a clear yes turns it on.
5. **The sketch: up to five questions, one per message.** What you are making, who it is for, where it runs, how it should feel in 2 or 3 words, and your brand color or logo. Each question comes with a suggested answer and its reason. Answer in your own words, or say "just pick".
6. **You get a complete first version.** The engine builds every token, every export, `DESIGN.md` and an overview page. The engine part takes about two seconds.
7. **You see your whole system on one page.** `opendesigner/overview.html` marks each area Chosen, Picked for you or Default. Anything only you can give shows as "Not enough information", next to the question that fills it.
8. **Zoom in only where you care, or stop.** After each level it offers "stop here, or zoom into" one area. See [Zoom levels](/docs/zoom-levels/).
9. **It checks its own work.** Fixed rules check contrast, target sizes, focus rings and reduced motion before the AI gives any opinion. Errors block the build.
10. **It writes everything down.** Every decision is logged with how it was set and why. It asks before adding a short note to your `AGENTS.md`, so later AI sessions follow the same rules.
11. **Later, it keeps things consistent.** Changes go through the extend skill, which reads the decision log first. `engine.py review` finds hard-coded values in your code and names the token to use.
12. **If something is confusing or broken,** it saves a note in your project and gives you a ready-to-file GitHub link. Nothing is posted unless you submit it.

## Two parts: written instructions and an engine

The skills are written instructions your AI follows. The questions follow a decision graph, so nothing is asked before the things it depends on.

A Python engine does the math. It works out color ramps, type and spacing scales, contrast checks and every export. It uses only Python's standard library and makes no network calls. The same answers give the same files. You can run the engine with no AI at all. See [Engine commands](/docs/engine/).

{{figure:how-it-works-pipeline}}

## How your answers become a system

Your answers move [eight dials](/docs/dials/), such as Density, Roundness and Energy. Each dial runs from 0 to 100, and each position maps to concrete values: a type ratio, a corner radius, a motion duration. Feel words like "playful" or "calm" move several dials at once.

Every answer is recorded with how it was set, such as chosen, assumed or delegated. A suggestion you did not answer is never recorded as your decision. See [Decisions, DESIGN.md and the overview page](/docs/decisions/).

### Your taste

Your taste can move the dials too, but only as a suggestion you confirm.

- **The taste poll** is optional and takes about 5 minutes. You rate 20 to 30 real screens from shipped products, never AI-made ones. The screen images stay on your computer.
- **The taste index** combines every taste signal in your project: the poll, your own decisions, your inspirations, a style you picked and your feel words. It gives each dial a value and a confidence, plus red lines. When it is sure about a dial, it asks "confirm this?". It never offers an option past a red line, and `engine.py review` tells you when the system drifts from your taste.
- **The taste card** sits at the top of `DESIGN.md` and on the overview page. It has five lines: your own picture of the look, color, shape, motion, and what it should never look like. Each line says where it comes from. The picture and the Never list only ever come from you.

Taste never moves an accessibility floor or a house standard, and it stays in your project.

## Showing choices

It shows each choice in the most visual way your AI tool allows: a page in the chat (such as a Claude artifact), Figma or Paper, a local HTML page, the tool's own multiple-choice question, or plain text with numbered options. It never waits on a picture to move on. The pictures come from eight templates, each with a "Copy my choice" button that makes lines you paste back into the chat. Clicking choices directly inside the AI tool is planned ([issue #20](https://github.com/ckryptickunal/OpenDesigner/issues/20)).

## References and assets

You can share a website, screenshot, Figma file, repo or brand book at any point. The extract skill measures what it can and offers each value as a suggested answer. It never copies another brand's name, logo, exact color, proprietary font, images or words. See [Start from an existing app or brand](/docs/existing-product/).

For a logo, custom icons, illustration, photos, a brand typeface or a voice guide, it asks you. See [Brand assets](/docs/brand-assets/).

## The checks

Rule-based checks run first and give the same result every time. Breaking an accessibility rule is an error. Breaking a taste rule is a warning. Only after the system passes does the AI critique it. See [Accessibility floors](/docs/accessibility/).

House standards also apply. These are 455 rules from sources the project owner marked non-negotiable. The engine applies the ones that fit your platforms and locks them.

{{figure:how-it-works-checks}}

## Files, later changes and privacy

- **Files:** `DESIGN.md` and `PRODUCT.md` at the root, and an `opendesigner/` folder with tokens, exports, the overview page and the decision log. See [The files it writes](/docs/files/).
- **Later changes:** see [Change or extend a system](/docs/extend/).
- **Privacy:** the private log stays in your project, out of git. Anonymous reports are a separate yes, and no server collects them yet. See the [privacy page](https://github.com/ckryptickunal/OpenDesigner/blob/main/docs/PRIVACY.md).
- **Defaults:** they rest on 352 Decision Cards, each covering one design decision with its sources. See the [research map](https://github.com/ckryptickunal/OpenDesigner/blob/main/docs/RESEARCH.md).
