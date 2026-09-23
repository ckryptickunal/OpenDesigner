# OpenDesigner FAQ

Short answers to the questions people ask most. Each answer links to the research if you want the evidence. Unfamiliar words are in the [glossary](GLOSSARY.md).

**Contents:** [Getting started](#getting-started) · [Design tokens and DTCG](#design-tokens-and-dtcg) · [Tools and hosts](#tools-and-hosts) · [How it compares](#how-it-compares) · [Designers, brands and references](#designers-brands-and-references) · [Accessibility](#accessibility) · [Project](#project)

## Getting started

### How do I create a design system with AI?

Load OpenDesigner into the AI tool you already use: Claude Code, Claude, Codex, ChatGPT, Cursor and others. The install steps are in the [README](../README.md#quickstart). Then say "create a design system for this project".

The model reads your repo first. It starts with a short sketch, and you can zoom into any area. It shows each choice visually where your tool allows it. It writes DTCG design tokens, CSS variables, a Tailwind theme, a `DESIGN.md` and a decision log into your project. See [How it works](HOW-IT-WORKS.md).

How is that different from typing "make me a design system"?
- Every recommendation comes from a cited research base: 352 Decision Cards and 25 benchmarked systems.
- The questions come in order of what depends on what.
- Fixed checks (contrast, target sizes, scale steps) run before you see the result.

### How do I make my app look designed without a designer?

Most of what makes an interface look designed is consistency:
- one spacing scale;
- one type scale with a few sizes;
- a small set of colors with clear roles;
- one radius family and one depth model;
- predictable states.

Those can be generated. OpenDesigner generates them from a few inputs and eight dials. Then it checks hierarchy rules: a few type sizes per view, one primary action, and inner spacing smaller than outer spacing.

What it cannot generate well (a logo, custom icons, illustration, photography) it asks you for. If you don't have them, it points you to open libraries or writes a designer brief. See [the eight dials](HOW-IT-WORKS.md#4-the-eight-dials).

### How long does it take?

Start with a sketch. About 3 to 5 questions, in about 3 minutes, give you a complete, working system with sourced defaults. Then zoom into any area you care about, and stop whenever it is enough. The next level, one short screen per foundation, is 8 questions in about 8 minutes. Every default stays editable. The full interview has 192 questions, but you only answer the ones for the areas you zoom into.

### What do I get at the end?

Files in your repo:
- DTCG design tokens, with their modes in one resolver file;
- exports for CSS variables, Tailwind, Figma, Paper, Swift and Jetpack Compose;
- a `DESIGN.md` that people and AI tools can read;
- a `decisions.md` log with the reason for every choice;
- a `state.json` to continue later, and a preview page;
- a snippet for your `AGENTS.md`, so later agents read the system first.

See [what lands in your repo](HOW-IT-WORKS.md#8-export-and-what-lands-in-your-repo). The README's status table says which exporters have shipped.

### I already have a design system. Is this useful?

Yes, in two ways. First, reference intake reads your existing CSS, tokens or Figma variables and pre-fills the interview, so it only asks about gaps. Second, the coverage check shows which building blocks your system is missing. Examples are reduced-motion tokens, focus rings, target sizes and dark-mode mappings. The extend flow then keeps later changes coherent.

## Design tokens and DTCG

### What are design tokens?

Design tokens are design decisions with names, stored as data: `color.text.primary`, `space.4`, `radius.control`, `motion.duration.short`. Code, design tools and documentation all read the same values. So changing a token changes every place it is used.

Most systems use three tiers of tokens:
- primitives: the raw palette and scales;
- semantic tokens: roles such as "text on the brand color";
- component tokens: values for one component.

See [`research/L07-tokens-figma.md`](../research/L07-tokens-figma.md).

### What is DTCG?

DTCG is the Design Tokens Community Group format. It is a W3C Community Group specification for storing tokens as JSON with `$value`, `$type` and `$description`. Version 2025.10 was published as stable on 28 October 2025. Themes and modes (light, dark, compact) live in its Resolver module.

OpenDesigner uses DTCG 2025.10 as its canonical token format and generates everything else from it. See [`research/L07-tokens-figma.md`](../research/L07-tokens-figma.md).

### Can Figma import DTCG tokens?

Partly. The L07 research found that Figma imports DTCG with limits. It takes one mode per file, sRGB or HSL colors, px units, and no composite tokens. That is why the engine also writes Figma variables directly (`engine.py export --format figma`), with one import file per mode. Check the lane for the current details.

## Tools and hosts

### Does it work with Claude and Claude Code?

Yes. In Claude Code, add this repo as a plugin marketplace and install the plugin:

```
/plugin marketplace add ckryptickunal/OpenDesigner
/plugin install opendesigner@opendesigner
```

In the Claude app (claude.ai, Desktop), upload the skill zip that `python3 tools/build_dist.py` builds, under Customize > Skills. Claude can show choices visually through custom visuals and artifacts. Full steps: [README](../README.md#quickstart).

### Does it work with ChatGPT?

Yes, in three ways, depending on your plan:
- a ChatGPT Project with the instructions and knowledge files from `chatgpt-project/` (the simplest path, and it works on the free plan);
- skills in the ChatGPT desktop app;
- a plugin.

Custom GPTs are being retired on 11 December 2026, so OpenDesigner does not ship one. See [`research/L18-ai-first-distribution.md`](../research/L18-ai-first-distribution.md) Part B.

### Does it work with Codex?

Yes. Codex reads `AGENTS.md` and skills in `.agents/skills/`, and OpenDesigner ships both. Codex CLI cannot show UI in the terminal, so previews are written as local HTML files you open in a browser.

### Does it work with Cursor, GitHub Copilot, Gemini CLI and other agents?

Yes, for any agent that reads `AGENTS.md` or Agent Skills from `.agents/skills/`. The L18 lane checked Cursor, VS Code with Copilot, Gemini CLI (through `GEMINI.md`), Goose, Zed, OpenCode and others. The host capability matrix is in [`research/L18-ai-first-distribution.md`](../research/L18-ai-first-distribution.md) Part A. If your tool is missing, open a [host support request](../.github/ISSUE_TEMPLATE/host-support.yml).

### Does it work with Tailwind?

Yes. Tailwind is one of the export formats. The tokens become a Tailwind theme, so utility classes use your system's colors, spacing, radii and type.

### Does it work with shadcn/ui?

Yes. shadcn/ui is one of the 25 benchmarked systems and one of the dial recipes. The export's CSS variables and Tailwind theme are what shadcn/ui components read. OpenDesigner decides the system (roles, scales, states, accessibility targets) that a shadcn theme expresses. A note from L08: shadcn/ui changed its default base library from Radix to Base UI in July 2026.

### Does it work with Figma?

Yes, both ways. Figma is a reference source: the model can read variables from a file through Figma's MCP server. It is also an export target (Figma variables). Writing to the Figma canvas needs Figma's remote MCP server and a Full seat; see [`research/L16-visual-tooling-for-engineers.md`](../research/L16-visual-tooling-for-engineers.md). Paper is also supported as a design-tool round trip.

### Does it work for iOS, Android, React Native or Flutter?

The interview asks for your platforms early, because that decision directly shapes 12 others. These include native type sizes, target sizes (44pt iOS, 48dp Android), platform components, and whether brand or platform wins on each surface. Swift and Jetpack Compose exports are part of the engine. For React Native and Flutter token pipelines, see [`research/L10-platforms.md`](../research/L10-platforms.md).

### Does it send my code or data anywhere?

The skills and engine run on your machine. They use the Python standard library only, and the engine makes no network calls. Your conversation still goes to whichever AI provider you use, as it would for any prompt. Reference intake only fetches a URL after you confirm it.

There is one opt-in exception. If you say yes, the journey tracker keeps a private log of your steps, and that log stays with your project: on your computer when you run OpenDesigner locally, or in the chat's project files in web tools. Sending an anonymous summary to the maintainers is a second, separate yes. It never includes your answers, names, files or anything you typed. See [PRIVACY.md](PRIVACY.md).

## How it compares

### How is this different from Claude Design?

Claude Design (Anthropic Labs, launched April 2026) makes designs and prototypes on a canvas. It builds a team design system from your code and design files. It is a polished, closed product for paid Claude plans.

OpenDesigner is different in a few ways:
- It is open source and runs in any capable model.
- It stores the system in open files you can read: DTCG tokens, `DESIGN.md` and a decision log.
- It explains why each decision matters and where the evidence is.
- It spends more time on the decisions that shape the most.

You can use both, because any tool can read OpenDesigner's `DESIGN.md` and tokens. See [`research/L18-ai-first-distribution.md`](../research/L18-ai-first-distribution.md) Part E.

### How is this different from Figma Make?

Figma Make builds apps and prototypes by chat, with a live preview. A Make kit packages an existing design system (an npm package plus guideline files), so generated screens follow it. OpenDesigner creates and documents the system in the first place, with the rationale and guidelines a kit needs. It can also export Figma variables for it.

### How is this different from tweakcn or other theme generators?

tweakcn is an open-source visual editor for shadcn/ui themes. It has about 46 controls [S-V1a-067]: 32 color inputs, 3 font pickers and 11 sliders. It also has AI generation from text or an image, CSS variables for Tailwind v3 and v4, and a contrast checker. It is a good tool for tuning a shadcn theme.

The L11 and L17 research looked at theme generators: tweakcn, shadcn create, Radix, Realtime Colors and Material Theme Builder. They produce color, type, radius and shadow. None asks about audience, platforms, accessibility targets, component policies or governance. That is the gap OpenDesigner fills. Its output is framework-neutral DTCG, with Tailwind and CSS exports.

### How is this different from asking an AI to "make it look good"?

AI output with no guidance tends toward one look. NN/g's evaluation of AI prototyping tools (14 tested) [S-V1a-069] found a similar generic look, with weak spacing, grouping, contrast and hierarchy. Vendors now ship their own guidance against that generic look ([`research/L17-how-systems-get-made.md`](../research/L17-how-systems-get-made.md) Part B).

OpenDesigner asks for the one thing people should recognize and proposes distinct directions. It labels which choices are safe and which are risks. It checks the result against rules before calling it done.

## Designers, brands and references

### Does it replace designers?

No. It generates what can be generated well. For what cannot, it opens an asset hook: logo, app icon, custom icons, illustration, photography, brand typeface, motion signature, sound and voice. For each one, it asks whether you have it and checks the file. If you don't, it writes a brief a designer can act on, or points to named open libraries and tools with their license caveats. The decision log is also what a designer would ask for when they join.

### Can I start from a website I like? Will it copy their brand?

You can add any website, screenshot, Figma file or brand book as a reference at any step. OpenDesigner reads structure and quality from it: spacing rhythm, type ratios, density, depth model and motion character.

It never copies identity. That means no logos, brand names, brand colors used as identity, proprietary typefaces, photography, illustration or copy. This is a hard rule.

### Does it make logos or icons?

No. It asks whether you have them and checks the files. For example, it checks that a logo SVG has outlined text and works at 16 px on light and dark. It derives the favicon and app-icon sizes from your master file.

If you don't have one, it gives you honest paths:
- a designer brief;
- a wordmark set in your chosen typeface;
- open icon libraries such as Lucide, Phosphor, Tabler, Heroicons or Material Symbols, with their licenses kept.

## Accessibility

### Does it handle accessibility and WCAG?

Yes, and it builds it in wherever possible. Every generated system gets:
- WCAG 2.2 AA text contrast: 4.5:1 for body text, 3:1 for large text;
- 3:1 contrast for borders, focus rings and meaningful icons;
- target sizes that fit the input type: at least 24 CSS px on the web, 44pt on iOS, 48dp on Android;
- a focus ring, reduced-motion and reduced-transparency modes, and text that can scale to 200%.

Lint errors block things like unlabeled fields or meaning shown only by color. WCAG 3 is still a draft, so WCAG 2.2 is the target that can be enforced. APCA appears as an advisory note.

Automated checks catch only part of WCAG, so testing by people with assistive technology still matters. See [`synthesis/LEVERS.md`](../synthesis/LEVERS.md) section D.

### Does it do dark mode?

Yes. Light and dark are generated together, as separate mappings, not an inverted palette. The color research found that dark mode is always a separate mapping in the systems it studied. Contrast is checked in every mode.

## Project

### Is it free? What is the license?

It is free and open source. Code, skills and data files are under the MIT license. Written research and documentation are under CC BY 4.0. See [`LICENSE`](../LICENSE) and [`LICENSE-CONTENT`](../LICENSE-CONTENT).

### Why trust the recommendations?

You don't have to. Every recommendation cites a Decision Card. Every card cites sources logged in `traces/` with URL, publisher, date and tier, or says `[inferred]`. If you find a wrong value, open a [research correction](../.github/ISSUE_TEMPLATE/research-correction.yml). Disputes are settled by sources. See [RESEARCH.md](RESEARCH.md).

### How can I help?

See [CONTRIBUTING.md](../CONTRIBUTING.md) and the [good first issues](https://github.com/ckryptickunal/OpenDesigner/labels/good%20first%20issue). Research gaps, host support, translations and examples are all welcome. To report a problem you hit while using it, see [Report a problem](../README.md#report-a-problem-or-suggest-an-improvement).
