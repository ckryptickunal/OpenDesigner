---
title: FAQ
seo_title: OpenDesigner FAQ: AI design systems, tokens, teams, privacy
description: Plain answers about OpenDesigner: what it is, which AI tools it works with, privacy, accessibility, how it compares, team governance, and how early it is.
section: Reference
order: 5
updated: 2026-11-10
---

### What is OpenDesigner?

A free, open-source add-on for AI tools like Claude, ChatGPT, Codex and Cursor. It helps you make a design system: the rules for how your app looks, like colors, text sizes, spacing, corners and buttons. It reads your project, asks a few plain questions, suggests an answer for each with a reason, checks the result, and saves the rules as files in your project.

Code, skills and data are MIT; the written research and docs are CC BY 4.0. You need your own AI tool, which may cost money. See the [introduction](/docs/introduction/).

### Isn't this just a prompt?

Partly: the skills are written instructions your AI follows. A Python engine does the math, from color ramps and type scales to contrast checks and every export, and the same answers give the same files. You can run the engine with no AI at all. See [How it works](/docs/how-it-works/).

### Which AI tools does it work with?

It is packaged for Claude Code, the Claude app, ChatGPT (as a Project), and Codex, Cursor, VS Code with Copilot, Gemini CLI and other agents that read `.agents/skills/`. A recorded test run in each of them is still to do. See [Install](/docs/install/).

### Is OpenDesigner a Claude skill?

Yes. In Claude Code the plugin installs its nine skills, and in the Claude app you upload them as a skill zip; the same skill folders also work in Codex, Cursor and other agents that read skills. See [Install](/docs/install/).

### How do I install OpenDesigner?

In Claude Code it takes two commands and a new session; the Claude app, ChatGPT, Codex, Cursor and other agents each have a short path too. Then open your project and say "Create a design system for this project." See [Install](/docs/install/).

:::dev
```
/plugin marketplace add ckryptickunal/OpenDesigner
/plugin install opendesigner@opendesigner
```
:::

### What does it cost?

Nothing. OpenDesigner is free and open source, with no account to create: code, skills and data are MIT, and the written research and docs are CC BY 4.0. You need your own AI tool, which may cost money. The engine also runs with no AI at all. See [Install](/docs/install/).

### How do I update it?

In Claude Code it takes one command and a new session. In the Claude app you delete the old skill and upload the newest zip. In Codex, Cursor and other agents you run the copy commands again. The [changelog](/changelog/) says what changed. See [Update it](/docs/install/#update-it).

:::dev
```
claude plugin update opendesigner@opendesigner
```
:::

### How do I remove it or undo what it did?

Everything it writes is a plain file in your project, so undoing it means deleting `DESIGN.md`, `PRODUCT.md` and the `opendesigner/` folder. If you said yes to the note for later sessions, also delete its part of `AGENTS.md` and the `@AGENTS.md` line in `CLAUDE.md`. Then uninstall the plugin, or delete the skill you uploaded or copied. See [Remove it](/docs/install/#remove-it).

### What does it ask during setup?

Up to five questions: what you're making, who it's for, where it runs, how it should feel, and your brand color or logo. Each comes with a suggested answer and its reason, and you can say "just pick". It also asks once whether it may keep a private log of your steps. See [Your first design system](/docs/quickstart/).

### What files does OpenDesigner create in my project?

`DESIGN.md` and `PRODUCT.md` at the root, and an `opendesigner/` folder with DTCG tokens, code exports for your platforms, an overview page and the decision log. See [The files it writes](/docs/files/).

{{figure:files-tree}}

### How does it work with Tailwind CSS?

It reads your Tailwind config before asking anything. When your platforms include the web, every build writes a Tailwind CSS v4 theme, so utility classes use your colors, spacing, radii and type. See [Export](/docs/export/).

### How do AI coding agents use DESIGN.md?

`DESIGN.md` holds your design rules in plain words, and coding agents read it before they touch the interface. OpenDesigner asks before adding a short note to your `AGENTS.md` that tells agents to read it, use the tokens and run `engine.py review` when they finish. See [Decisions, DESIGN.md and the overview page](/docs/decisions/).

### Does it send my code or data anywhere?

The engine runs on your computer and makes no network calls. Your chat goes to your AI provider, as any prompt does. The illustration skill searches open-licence art and photo sites only when you use it, and library parts with a photo load it from Unsplash. In the Claude app, the scripts run in Claude's code-execution sandbox.

The private log of your steps is off unless you say yes, and it stays in your project. Anonymous reports are a separate yes, and no server collects them yet. See the [privacy page](https://github.com/ckryptickunal/OpenDesigner/blob/main/docs/PRIVACY.md).

### How long does it take?

The sketch is up to five questions, planned at about 3 minutes, though nobody has timed real people yet. The engine takes a few seconds. Then you zoom in only where you want. See [Zoom levels](/docs/zoom-levels/).

### How is it different from a shadcn theme generator?

If you only need colors for shadcn/ui, a theme generator such as tweakcn is a good tool. OpenDesigner starts a step earlier: who the app is for, where it runs and what accessibility it needs. It records why you chose each thing, and writes tool-neutral DTCG tokens plus CSS variables and a Tailwind theme.

### How is it different from Figma's AI tools?

Figma Make builds apps and prototypes by chat, and a Make kit packages a design system you already have. OpenDesigner creates and documents the system itself, with the reason for each choice, and exports Figma variables. It doesn't draw on a canvas. See [For product designers](/docs/designers/).

### How is it different from UI UX Pro Max?

UI UX Pro Max is an open-source (MIT) design knowledge base for your AI: it recommends a style, color palette, fonts and page pattern for your kind of product, with guidelines for many tech stacks, and can save the result as a Markdown master file. OpenDesigner builds the system from your own answers into DTCG tokens and code exports, records why each value was chosen, and blocks the build when contrast or target sizes fail. Pick UI UX Pro Max for quick, broad style recommendations; pick OpenDesigner when you want tokens your code imports and decisions your team can review. See [How it works](/docs/how-it-works/).

### Does it replace designers?

No. It does the repetitive system work: scales, tokens, states and contrast. It asks a person for the logo, icons, illustration, photos, typeface and voice, and it can't tell you whether real users understand your app. See [Brand assets](/docs/brand-assets/).

### Will my app look like every other AI-made app?

That's a fair worry. OpenDesigner asks what people should remember about your product, sets eight dials from your answers, and asks for your own logo, fonts and art instead of faking them. It won't copy another brand; if you love a site's look, it can write a Taste Index of it, and what you keep is your call and your responsibility. Logos, names, images and copy never go in.

The limits, honestly: in our stress test in October 2026, AI agents made 46 pieces plus 8 mockups by following the process. An audit against shipped products passed 28 of the 54, sent 20 back for polish and rebuilt 6, and much of the striking work was made outside the tokens. The tokens give you consistency and readable contrast; a distinctive look still needs your input.

The [showcase](/showcase/) shows a different count today: since that audit, pieces were rebuilt or held back, and B2B product screens and style studies were added.

### Does it check color contrast?

Yes. Every text, border and focus-ring color pair the tokens produce is checked against WCAG 2.2 AA, in light and dark mode and every mode combination, including text on hover and pressed fills, and a failure is an error that blocks the build. See [Accessibility floors](/docs/accessibility/).

### Does it make my app meet WCAG?

It builds WCAG 2.2 AA contrast, minimum target sizes, a focus ring and reduced motion into every system, and errors block the build. That is a minimum: automated checks catch only part of WCAG. Test with real people, including people who use assistive technology. See [Accessibility floors](/docs/accessibility/).

### We already have an app or a design system. Is this useful?

Yes. The extract skill measures your CSS, token files, Figma variables or brand book and offers the values as suggested answers, then asks only about the gaps. Nothing is decided until you accept it. See [Start from an existing app or brand](/docs/existing-product/).

### How does governance work for a design-system team?

Everything is a file in your repository, so your normal review applies. On top of that, the decision log is append-only and records why; locked decisions and standards change only when someone explicitly asks; and `engine.py review` finds hard-coded values and code that breaks a standard. Deeper zoom levels ask who can change the system and how changes are announced, and never invent the answers. See [For enterprise design-system teams](/docs/enterprise/).

### How would a team adopt it?

No team has piloted it yet, so there is no rollout guide. Today you get `DESIGN.md` for designers, engineers and agents; a note for your `AGENTS.md` so coding agents read the system first; token files your apps import; and `engine.py review` to catch drift, not yet tested in a CI pipeline. Start with one product, and please [tell us](https://github.com/ckryptickunal/OpenDesigner/issues/new/choose) what your team needs.

### Does it support several brands or white-label themes?

Not yet. Each system has light and dark modes, three densities and reduced motion in one resolver file, and the interview can record that more brands will follow, but the engine doesn't build separate brand modes. Don't plan a multi-brand rollout on it today.

### Why should I trust the defaults?

You don't have to trust them. You can check them. They rest on more than 500 Decision Cards, each citing logged sources or marked as an inference. A verification pass re-checked 161 claims against live sources and found 5 wrong, now fixed. See the [research map](https://github.com/ckryptickunal/OpenDesigner/blob/main/docs/RESEARCH.md).

### How early is it, and how do I report a problem?

Early. Version 0.3.1 came out on 11 November 2026, six days after the first tagged release, and no watched user trials have happened. The evidence so far is the engine's tests, three worked examples, usability tests role-played by AI testers, and the stress test above.

To report a problem, tell your AI what went wrong. It saves a note in your project with a ready-to-file GitHub link, or you can [open an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new/choose) directly. Nothing is posted unless you submit it.
