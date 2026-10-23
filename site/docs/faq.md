---
title: FAQ
seo_title: OpenDesigner FAQ: AI design systems, tokens, teams, privacy
description: Plain answers about OpenDesigner: what it is, which AI tools it works with, privacy, accessibility, how it compares, team governance, and how early it is.
section: Reference
order: 5
updated: 2026-10-15
---

These are short answers to the questions people ask most about OpenDesigner. They cover what it does, which tools it works with, privacy, accessibility, use by teams, and how early the project is. Most answers link to a longer page.

### What is OpenDesigner?

OpenDesigner is a free, open-source add-on for AI tools like Claude, ChatGPT, Codex and Cursor. It helps you make a design system: the rules for how your app looks, like colors, text sizes, spacing, corners and buttons. It reads your project, asks a few plain questions, suggests an answer for each with a reason, checks the result, and saves the rules as files in your project.

The code, skills and data are under the MIT licence. The written research and docs are under CC BY 4.0. You need your own AI tool, which may cost money. See the [introduction](/docs/introduction/).

### Isn't this just a prompt?

Part of it is written instructions your AI follows, yes. The math is done by a Python engine. It works out color ramps, type and spacing scales, contrast checks and every export. The same answers give the same files. The questions follow a fixed order, so nothing is asked before the things it depends on. You can also run the engine with no AI at all. See [How it works](/docs/how-it-works/).

### Which AI tools does it work with?

It is packaged for Claude Code, the Claude app, ChatGPT (as a Project), and for Codex, Cursor, VS Code with Copilot, Gemini CLI and other agents that read skills from `.agents/skills/`. A recorded test run in each of those tools is still on the to-do list. See [Install](/docs/install/).

### Does it send my code or data anywhere?

The engine runs on your computer, uses Python's standard library and makes no network calls. Your chat still goes to whichever AI provider you use, as with any prompt. The illustration skill searches open-licence art sites, but only when you use it. In the Claude app, the scripts run in Claude's code-execution sandbox.

The private log of your steps is off unless you say yes, and it stays in your project. Anonymous reports to the maintainers are a separate yes, and no server collects them yet, so nothing is sent today. See the [privacy page](https://github.com/ckryptickunal/OpenDesigner/blob/main/docs/PRIVACY.md).

### How long does it take?

The sketch is up to five questions. Its planned length is about 3 minutes, but nobody has timed real people yet. The engine part takes about two seconds. After that, you zoom in only where you want to. See [Zoom levels](/docs/zoom-levels/).

### How is it different from a shadcn theme generator?

If you only need colors for shadcn/ui, a theme generator such as tweakcn is a good tool. OpenDesigner works one step earlier. It asks who the app is for, where it runs and what accessibility level you need. It records why you chose each thing, and it writes tool-neutral DTCG tokens plus CSS variables and a Tailwind theme.

### How is it different from Figma's AI tools?

Figma Make builds apps and prototypes by chat, and a Make kit packages a design system you already have. OpenDesigner creates and documents the system itself, with the reason for each choice, and exports Figma variables. It doesn't draw on a canvas. See [For product designers](/docs/designers/).

### Does it replace designers?

No. It does the repetitive system work: scales, tokens, states and contrast. It asks a person for the logo, icons, illustration, photos, brand typeface and voice, and writes briefs a designer can act on. It can't tell you whether real users understand your app. See [Brand assets](/docs/brand-assets/).

### Will my app look like every other AI-made app?

That's a fair worry. OpenDesigner asks what people should remember about your product, sets eight dials from your answers, and asks for your own logo, fonts and art instead of faking them. It won't copy someone else's brand from a reference site. If you love a site's look, or ask it to copy a brand, it offers a Taste Index of that look: the whole look described for your AI, keeping the site's exact colors and font names when first shown. What you keep or change is up to you and your responsibility; logos, names, images and copy never go in.

To be honest about the limits: in our stress test, AI agents made 46 pieces by following the process, plus 8 mockups. An audit against shipped products on Mobbin then passed 28 of the 54, sent 20 back for polish and rebuilt 6; much of the striking work was made outside the tokens. The audit's lessons are now rules every builder checks against. The tokens give you consistency and readable contrast. A distinctive look still needs your input.

### Does it make my app meet WCAG?

It builds WCAG 2.2 AA contrast, minimum target sizes, a focus ring and reduced motion into every system, and errors block the build. These are a minimum. Automated checks catch only part of WCAG, and the engine can't see how your screens use the values. Test with real people, including people who use assistive technology. See [Accessibility floors](/docs/accessibility/).

### We already have an app or a design system. Is this useful?

It can be. The extract skill reads your CSS, token files, Figma variables or brand book, measures the values, and offers them as suggested answers. Then it asks only about the gaps. Nothing is decided until you accept it. Later changes go through the extend skill, which reads the decision log first. See [Start from an existing app or brand](/docs/existing-product/).

### How does governance work for a design-system team?

Everything is a file in your repository, so your normal review process applies. On top of that:

- the decision log records every decision, how it was set and why, and is append-only;
- locked decisions change only with the owner's OK;
- house standards and your own project standards are locked, and change only when someone explicitly asks;
- `engine.py review` finds hard-coded values and code that breaks a standard.

At deeper zoom levels, the interview also asks governance questions, such as who can add to the system and how changes are announced. It records your answers and never invents them. See [For enterprise design-system teams](/docs/enterprise/).

### How would a team adopt it?

There is no team rollout guide yet, because no team has piloted it. What exists today:

- `DESIGN.md`, which designers, engineers and AI agents can all read;
- a short note OpenDesigner offers to add to your `AGENTS.md`, so coding agents read the system first;
- token files and exports your apps import;
- `engine.py review`, which each person can run at the end of their work to catch drift. We haven't tested it in a CI pipeline yet.

A sensible start is one product, with the team reading the decision log together. Please [tell us](https://github.com/ckryptickunal/OpenDesigner/issues/new/choose) what your team needs.

### Does it support several brands or white-label themes?

Each system has light and dark color mappings, three densities and a reduced-motion mode, tied together in one resolver file. The interview can record that more brands will re-skin the system, but the engine doesn't build separate brand modes yet. Don't plan a multi-brand rollout on it today.

### Why should I trust the defaults?

You don't have to trust them. You can check them. The defaults rest on more than 500 Decision Cards. Each card covers one design decision and cites logged sources, or is marked as an inference. A citation check finds no broken references. A verification pass re-checked 161 claims against live sources: it found 5 wrong, and the fixes are logged. The research map is in the [repository](https://github.com/ckryptickunal/OpenDesigner/blob/main/docs/RESEARCH.md).

### How early is it, and how do I report a problem?

It's early. The repository was created on 2026-09-23, and version 0.1.0 has no tagged release yet. No watched user trials have happened. The evidence so far is the engine's tests, three worked examples, usability tests role-played by AI testers, and a stress test in which AI agents made 46 pieces. The worked examples are out of date with the current engine.

To report a problem, tell your AI what went wrong. It saves a note in your project and gives you a ready-to-file GitHub link. You can also [open an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new/choose) directly. Nothing is posted unless you submit it yourself.
