---
title: OpenDesigner FAQ: design tokens, AI design systems, privacy
seo_title: OpenDesigner FAQ: AI design systems, tokens, privacy
description: Straight answers about OpenDesigner: whether it's just a prompt, how it differs from shadcn themes and Figma, what it sends where, and how early it is.
h1: Frequently asked questions
updated: 2026-10-14
---

### What is OpenDesigner?
OpenDesigner is a free, open-source (MIT) helper that builds a design system with the AI you already use, such as Claude, ChatGPT, Codex or Cursor. It asks up to five plain questions, recommends an answer for each with a reason, checks contrast and target sizes, and saves the rules as design tokens, CSS variables, a Tailwind theme and a DESIGN.md in your project.

### What is a design system?
A design system is the set of rules for how a product looks and behaves: colors, text sizes, spacing, corners, depth, motion and components like buttons and fields. Writing the rules down keeps every screen consistent, even when different people, or different AI chats, build them. [Read the full guide](../what-is-a-design-system/).

### What are design tokens?
Design tokens are a design system's rules saved as named values, for example a color called `color.text.primary` with the value `#222428`. Code, design tools and AI agents all read the same names. OpenDesigner writes tokens in the open DTCG format, version 2025.10, the first stable version of the Design Tokens Community Group specification.

### Isn't this just a prompt?
Part of it is written instructions your AI follows. The math isn't left to the model: a Python engine works out color ramps, type and spacing scales, contrast checks and every export, so the same answers always give the same files. The questions follow a fixed order, so nothing is asked before the things it depends on. You can run the engine with no AI at all.

### Why not just use a shadcn theme generator?
If you only need colors for shadcn/ui, a theme generator is a good tool. OpenDesigner works one step earlier: it asks who the app is for, where it runs and what accessibility level you need, records why you chose each thing, and writes tool-neutral tokens plus CSS variables and a Tailwind theme.

### How is it different from Figma's AI tools?
Figma's AI tools build screens and prototypes on a canvas. OpenDesigner creates and documents the system first, with the reason for each choice, and exports Figma variables so your design file can match. It doesn't draw on a canvas.

### Does it send my code anywhere?
The engine runs locally, uses Python's standard library and makes no network calls. Your chat still goes to whichever AI you use, as with any prompt. The illustration skill searches open-licence art sites, but only when you use it. Anonymous usage reports are off unless you say yes, and no server collects them yet, so nothing is sent today.

### Does it work without Claude?
It is packaged for ChatGPT (a Project with an instructions file and five knowledge files) and for Codex, Cursor, VS Code with Copilot, Gemini CLI and other agents that read `.agents/skills/`. A recorded test run in each of those tools is still on the to-do list. The engine also runs with no AI at all.

### AI-made apps all look the same. Will mine?
That's a fair worry. OpenDesigner asks what people should remember about your product, sets eight dials from your answers, and asks for your own logo, fonts and art instead of faking them. In our own stress test, AI agents built 46 pieces through the process: about a third came out competent but conventional, and the most striking work was shaped by hand on top of the tokens. The tokens give you consistency and readable contrast. Being distinctive still needs your input.

### Does it replace designers?
No. It does the repetitive system work: scales, tokens, states and contrast. It asks a person for the logo, icons, illustration, photos, brand typeface and voice, and writes briefs a designer can act on. It can't tell you whether real people understand your app.

### Is the output WCAG compliant?
Every system gets WCAG 2.2 AA contrast, minimum target sizes, a visible focus ring and reduced motion, and errors block the build. That's a floor, not a certificate. Automated checks catch only part of WCAG, so test with real people too.

### How early is it? Has anyone used it?
It's early: the repository was created on 2026-09-23. No watched user trials have happened yet. The evidence so far is the engine's tests, three worked examples, role-played usability tests and a stress test in which AI agents made 46 pieces. "About three minutes" for the five-question sketch is a design target, not a timed result.

### Is it free?
Yes. Code, skills and data are MIT; research and docs are CC BY 4.0. You need your own AI tool, which may have its own cost.

### How do I report a problem or suggest something?
Run `engine.py feedback "what went wrong" --kind bug` and it saves a note and prints a ready-to-file GitHub link, or [open an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new/choose) directly. Nothing is posted unless you submit it yourself.
