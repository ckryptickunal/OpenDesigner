# OpenDesigner

**Make your app look good, and keep it consistent, with the AI you already use.**

OpenDesigner is a free helper for AI tools like Claude, ChatGPT and Codex. It asks you simple questions about your app, shows you choices you can see, and writes down the rules for how your app should look: colors, text sizes, spacing, corners, buttons. That set of rules is called a **design system**.

- **If you're a designer:** it does the repetitive system work (scales, tokens, states, accessibility checks) and asks you for the parts only you should make, like the logo and illustrations.
- **If you're an engineer:** it turns each decision into DTCG design tokens, CSS variables, a Tailwind theme and a `DESIGN.md` that your code and your AI agents can follow.

[![CI](https://github.com/ckryptickunal/OpenDesigner/actions/workflows/ci.yml/badge.svg)](https://github.com/ckryptickunal/OpenDesigner/actions/workflows/ci.yml) [![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

![OpenDesigner: build a real design system with the AI you already use](docs/assets/social-preview.png)

[Quickstart](#quickstart) · [How it works](docs/HOW-IT-WORKS.md) · [Glossary](docs/GLOSSARY.md) · [FAQ](docs/FAQ.md) · [The research](docs/RESEARCH.md) · [Contributing](CONTRIBUTING.md)

## Start small, zoom in when you need to

1. **Sketch.** Answer about 5 questions. You already get a complete, working system.
2. **Zoom in.** Pick any area (color, text, spacing, buttons, motion) and go deeper. Each choice is shown, explained and recommended.
3. **Stop whenever it's enough.** Every level leaves you with files that work.

Every term comes in three voices: plain words first, then the designer's word and the engineer's word, one line away. They are all in the [glossary](docs/GLOSSARY.md).

## What it does

Most AI tools can make one screen look fine. Keeping a whole product consistent needs a design system: a spacing scale, a type scale, colors with clear roles, corner radii, shadows, motion, button and form states, accessibility rules, and the reason behind each. OpenDesigner is an open-source AI design system generator that walks you through building one. It is packaged as Agent Skills: a Claude skill that also runs in Codex, ChatGPT, Cursor and other agents.

It generates what can be generated well (spacing, type, color ramps, radii, elevation, motion, states) and asks you for what cannot (logo, custom icons, illustration, photography, a brand typeface) instead of faking it. You can add a website, screenshot or Figma file you like at any point; OpenDesigner borrows its structure and quality, never its brand.

Its recommendations come from research you can check: 352 Decision Cards across 18 research lanes, 2,740 logged sources, and a teardown of 25 public design systems (Material, Apple HIG, Carbon, Fluent, Polaris, Primer, shadcn/ui and more). Code checks contrast (WCAG 2.2), touch-target sizes and scales before you see the result, and every decision is written down with its reason, so your team and the next AI session can extend the system without breaking it.

## Quickstart

**Claude Code** (plugin, from this repo's marketplace):

```
/plugin marketplace add ckryptickunal/OpenDesigner
/plugin install opendesigner@opendesigner
```

**Claude app** (claude.ai, Desktop): build the skill zip, then upload `dist/opendesigner.zip` under Customize > Skills (code execution must be on).

```bash
git clone https://github.com/ckryptickunal/OpenDesigner && cd OpenDesigner
python3 tools/build_dist.py        # writes dist/opendesigner.zip and the three helper skills
```

**Codex, Cursor, VS Code with Copilot, Gemini CLI and other agents:** these read Agent Skills from `.agents/skills/`. Copy the four skills into your project (hosts that support Agent Plugins can also read the root `plugin.json`):

```bash
git clone https://github.com/ckryptickunal/OpenDesigner
mkdir -p your-project/.agents/skills
cp -R OpenDesigner/.agents/skills/opendesigner* your-project/.agents/skills/
```

**ChatGPT** (web, any plan, no install): create a Project, paste [`chatgpt-project/instructions.md`](chatgpt-project/instructions.md) (below its line) into the Project instructions, and upload the five files in [`chatgpt-project/knowledge/`](chatgpt-project/knowledge/).

Then say: **"Create a design system for this project."**

> **Status:** the skills, engine, manifests and ChatGPT bundle are in the repo, and the Claude plugin manifests pass `claude plugin validate`. The plugin install needs the repository to be public. See [Status and roadmap](#status-and-roadmap).

## What a session looks like

An illustrative example of the flow (not a recorded transcript), condensed:

```
You:    Create a design system for this project.
Model:  I read package.json (Next.js, Tailwind) and app/globals.css (14 colors, 3 radii).
        No DESIGN.md yet. Let's start with a 5-question sketch; you can zoom in after.
        First: what should people remember about this product?
You:    It should feel calm and fast.
        ...
Model:  Sketch done: a complete system with 0 errors. Three directions for
        "calm and fast", light and dark side by side: [A] [B] [C]
You:    B. Now zoom into brand assets.
Model:  Do you have a logo, an icon set or a brand typeface? [checklist]
You:    Logo yes (SVG). No icons, no typeface.
Model:  Logo checked: outlined text, readable at 16 px on light and dark.
        For icons I suggest Lucide (ISC license), matched to your type weight.
        The brand typeface stays a marked placeholder until you have one.
        Updated the tokens, CSS and Tailwind exports, DESIGN.md and the decision log.
```

## How it works

1. **Read first.** The model looks at your repo, CSS, existing tokens and any `DESIGN.md` before asking anything.
2. **Define the building blocks.** You see the whole map (271 nodes in 10 layers), each block tagged as generatable, extractable, designer-owned, tool-assisted or owner input.
3. **Designer hooks.** For the 14 kinds of assets that need a human (logo, app icon, icons, illustration, photography, brand typeface, sound and more), it asks "do you have this?", checks what you give it, and otherwise writes a designer brief or points to named open libraries with their licenses.
4. **Direction, then foundations.** Personality and platforms first, because they shape the most. Then color, type, space, shape, depth and motion, block by block, each with a live preview, where to use it and where not to.
5. **Reference intake at any step.** Add a website, screenshot, Figma file or brand book; values are pre-filled with their source, and you accept or ignore each one.
6. **Validate.** WCAG 2.2 contrast, target sizes, focus rings and reduced motion are enforced by construction; lint rules and a coverage check follow. Nothing is silently skipped.
7. **Export and extend.** Tokens and docs land in your repo; later sessions read the decision log before changing anything.

The full walkthrough, with a diagram, is in [docs/HOW-IT-WORKS.md](docs/HOW-IT-WORKS.md); the complete product specification is [docs/SPEC.md](docs/SPEC.md).

## What you get

Written into your project, in files any person or AI tool can read:

| Output | For |
|---|---|
| `opendesigner/tokens/` in **DTCG 2025.10** format, with modes (light, dark and more) in one resolver file | The single source of truth for code and design tools |
| CSS variables and a **Tailwind** theme | Use the system in web code right away, including shadcn/ui |
| **Figma** variables and **Paper** tokens | Mirror the system in your design tool |
| **Swift** and **Jetpack Compose** files | Native iOS and Android apps |
| `DESIGN.md` | A readable description of the system that people and AI tools can follow |
| `decisions.md` | Every decision with its reason, source and how it was set, append-only |
| `state.json` and `preview.html` | Continue later; see every token and the core components on one page |
| A snippet for your `AGENTS.md` and a team summary | Every later agent reads the system first; your team sees what was chosen, why, and what is still open |

The full output contract is in [docs/SPEC.md](docs/SPEC.md#7-outputs); [Status and roadmap](#status-and-roadmap) says what has shipped.

## The eight dials

A few raw inputs (brand color, typeface, base size, platforms, contrast target) plus eight dials from 0 to 100 generate most of the look. Brand words like "playful" or "premium" move several dials at once.

| Dial | From | To |
|---|---|---|
| Expression | productive | expressive |
| Brand presence | native to the platform | brand-led |
| Density | spacious | compact |
| Energy | calm | energetic |
| Roundness | sharp | soft |
| Depth | flat | deep |
| Colorfulness | monochrome | vivid |
| Warmth | cool, formal | warm, friendly |

Tested against 13 real systems, the dials plus raw inputs reproduce 6 of them outright (Apple HIG, Fluent 2, Primer, GOV.UK, shadcn/ui, Blade) and the other 7 with one or two overrides or a signature asset. Formulas, recipes and known weak spots: [`synthesis/LEVERS.md`](synthesis/LEVERS.md).

## Questions people ask

- **How do I create a design system with AI?** Load OpenDesigner into your AI tool and ask for one; it interviews you and writes the tokens and docs. [More](docs/FAQ.md#how-do-i-create-a-design-system-with-ai)
- **How do I make my app look designed without a designer?** Consistency does most of the work: one spacing scale, a small type scale, colors with roles, one radius family. OpenDesigner generates and checks those. [More](docs/FAQ.md#how-do-i-make-my-app-look-designed-without-a-designer)
- **What are design tokens, and what is DTCG?** Named design decisions stored as data, and the W3C Community Group format for them (stable version 2025.10). [More](docs/FAQ.md#design-tokens-and-dtcg)
- **Does it work with Tailwind, shadcn/ui and Figma?** Yes: Tailwind and CSS exports, shadcn/ui is one of the benchmarked systems, and Figma is both a reference source and an export target. [More](docs/FAQ.md#tools-and-hosts)
- **How is it different from Claude Design, Figma Make or tweakcn?** It is open source, runs in any model, stores the system in open files, and explains the evidence for each decision. [More](docs/FAQ.md#how-it-compares)
- **Is it accessible?** WCAG 2.2 AA contrast, target sizes, focus rings, reduced motion and text scaling are enforced by construction. [More](docs/FAQ.md#accessibility)

## Examples

Three complete systems made only with the engine's own commands, for fictional products. Each folder has `DESIGN.md`, `PRODUCT.md`, the decision log, DTCG tokens, every export and a `preview.html`.

| [Devtool Dense](examples/devtool-dense/) | [Consumer Playful](examples/consumer-playful/) | [Public Service Accessible](examples/public-service-accessible/) |
|---|---|---|
| ![Devtool Dense preview](docs/assets/examples/devtool-dense.png) | ![Consumer Playful preview](docs/assets/examples/consumer-playful.png) | ![Public Service Accessible preview](docs/assets/examples/public-service-accessible.png) |
| Calm, compact, sharp: a CI console | Expressive, rounded, colorful: a habit app | Plain, high contrast, no motion: a benefits service |

Try the engine on its own, no AI needed (Python 3.10+, no installs):

```bash
python3 path/to/OpenDesigner/skills/opendesigner/scripts/engine.py init --name "Acme"
python3 path/to/OpenDesigner/skills/opendesigner/scripts/engine.py build
```

This writes `DESIGN.md`, `PRODUCT.md` and an `opendesigner/` folder with tokens, exports and a preview, using sourced defaults.

## The research behind it

OpenDesigner's defaults are not taste. They come from this repo's research, which anyone can check:

| | |
|---|---|
| Research lanes finished | **18** (color, typography, space and layout, shape and motion, icons and data viz, brand and voice, tokens and Figma, components, benchmark, platforms, process and governance, UX laws, device classes, visual principles, tooling, how systems get made, AI distribution, community signal) |
| Decision Cards | **352**, each with options, visual effect, dependencies, token encoding, platform notes, accessibility limits and a default |
| Sources logged | **2,740**, every one opened with its URL, publisher, date, tier and verdict, including the rejected ones |
| Design systems benchmarked | **25**, with real values in 12 dimension tables |
| Interview | **192** questions on 27 screens, ordered by a decision graph of 352 decisions and 465 dependencies |

Start with [docs/RESEARCH.md](docs/RESEARCH.md). Every claim cites a source id or says `[inferred]`, and `python3 tools/jev_nav.py check` verifies that every cited source is logged.

## Status and roadmap

| Piece | Status |
|---|---|
| Research base (18 lanes), synthesis (ontology, interview, dials, decision graph) and [product specification](docs/SPEC.md) | Done |
| Four skills (`opendesigner`, `-extract`, `-extend`, `-export`), knowledge files and 8 visual templates | First version in [`skills/`](skills/) |
| Host packaging: Claude plugin and marketplace, Agent Plugins `plugin.json`, claude.ai zips, ChatGPT Project bundle | In the repo; Claude manifests pass `claude plugin validate` |
| Engine: generate, validate, export (DTCG, CSS, Tailwind, Figma, Paper, Swift, Compose) | Works: [`engine.py`](skills/opendesigner/scripts/engine.py) `build` writes every format; tests being added |
| Worked examples | 3 in [`examples/`](examples/) |
| Zoom levels (a 5-question sketch first), the three-voice glossary, and `engine.py feedback` for reporting gaps | Being added |
| Figma hands-on research (L12) and independent verification of the research (V1) | Open, [help wanted](docs/SEED-ISSUES.md) |
| Figma and Paper round-trip writers | Planned, last step of phase 1 |
| Phase 2: a stateless MCP server with MCP Apps views, so choices can be clicked inside Claude, ChatGPT, VS Code and Cursor | Planned |
| Phase 3 (optional): a standalone visual canvas | Idea |

## Contributing

Research corrections, new building blocks, skill and interview improvements, support for more AI tools, translations and examples are all welcome. Start with [CONTRIBUTING.md](CONTRIBUTING.md) and the [good first issues](https://github.com/ckryptickunal/OpenDesigner/labels/good%20first%20issue); most are research gaps with the file and sources already named.

OpenDesigner is built by many parallel sessions, human and AI, that coordinate through plain files in this repo: a board of lanes, heartbeats, an inbox and an append-only decision log. [`_coordination/PROTOCOL.md`](_coordination/PROTOCOL.md) explains it; `python3 tools/od.py status` shows who is working on what.

Questions go to [Discussions](https://github.com/ckryptickunal/OpenDesigner/discussions); see [SUPPORT.md](SUPPORT.md). Everyone follows the [Code of Conduct](CODE_OF_CONDUCT.md). Security issues: [SECURITY.md](SECURITY.md).

## Sponsors

OpenDesigner is free and open source. Sponsorship funds maintenance, model credits for testing across AI hosts, and the hosted MCP server. [Sponsor OpenDesigner](docs/SPONSORSHIP.md#for-sponsors)

<!-- Partners: large logos. Companies: small logos. Backers: names. Supported by: in-kind credit programs (never leave the wall empty). -->
<!-- When GitHub Sponsors is approved, point the link above at https://github.com/sponsors/ckryptickunal (see docs/SPONSORSHIP.md). -->

## License

Code, skills, templates and data files are under the [MIT license](LICENSE). Written research and documentation (`research/`, `benchmarks/`, `sources/`, `traces/`, `synthesis/` Markdown, `docs/`) are under [CC BY 4.0](LICENSE-CONTENT): reuse them with credit. Product and design-system names mentioned in the research belong to their owners.

## Citation

If OpenDesigner or its research helps your work, cite it with [CITATION.cff](CITATION.cff) (GitHub's "Cite this repository" button uses it).
