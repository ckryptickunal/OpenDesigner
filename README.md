# OpenDesigner

**Create a real design system with the AI you already use.** OpenDesigner is an open-source AI design system generator, packaged as Agent Skills: a Claude skill that also runs in Codex, ChatGPT, Cursor and other agents. It interviews you, recommends sourced defaults, shows each choice visually where your tool allows it, checks accessibility (WCAG 2.2), and writes DTCG design tokens, CSS, a Tailwind theme and a `DESIGN.md` into your project.

[![CI](https://github.com/ckryptickunal/OpenDesigner/actions/workflows/ci.yml/badge.svg)](https://github.com/ckryptickunal/OpenDesigner/actions/workflows/ci.yml) [![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

![OpenDesigner: build a real design system with the AI you already use](docs/assets/social-preview.png)

[Quickstart](#quickstart) · [How it works](docs/HOW-IT-WORKS.md) · [FAQ](docs/FAQ.md) · [The research](docs/RESEARCH.md) · [Contributing](CONTRIBUTING.md)

## What it does

Most AI tools can make a screen look fine once. Keeping a whole product consistent needs a design system: a spacing scale, a type scale, colors with clear roles, radii, elevation, motion, component states, accessibility rules, and the reasons behind each. OpenDesigner walks you through building one, in the AI tool you already use, in minutes (Quick mode, 10 questions) or in depth (Expert mode, 191 questions).

It starts by showing you every building block a design system needs and how each one shapes the rest. It generates what can be generated well (spacing, type, color ramps, radii, elevation, motion, states), asks you for what cannot (logo, custom icons, illustration, photography, a brand typeface) instead of faking it, and lets you add a reference website, screenshot or Figma file at any point, borrowing its structure and quality, never its brand identity.

Everything it recommends traces to a cited research base: 352 Decision Cards across 18 research lanes, 2,740 logged sources and a teardown of 25 public design systems (Material, Apple HIG, Carbon, Fluent, Polaris, Primer, shadcn/ui and more). Contrast, target sizes and scale rules are checked by code before you see the result, and every decision is written down with its reason, so your team and the next AI session can extend the system without breaking it.

**Who it is for:** software engineers and design engineers who need a product to look designed without a full-time designer; designers who want the system documented and encoded as tokens; teams who need to explain design decisions to each other.

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

> **Status:** the skills, manifests and ChatGPT bundle are in the repo, and the Claude plugin manifests pass `claude plugin validate`. The engine that generates and exports tokens is still being finished, and the plugin install needs the repository to be public. See [Status and roadmap](#status-and-roadmap).

## What a session looks like

An illustrative example of the flow (not a recorded transcript), condensed:

```
You:    Create a design system for this project.
Model:  I read package.json (Next.js, Tailwind), app/globals.css (14 colors, 3 radii)
        and found no DESIGN.md. Quick mode is 10 questions; Standard is about 92.
        What is the one thing people should remember about this product?
You:    Standard. It should feel calm and fast.
Model:  Here are the building blocks and who makes each one. Do you have a logo,
        an icon set or a brand typeface? [checklist]
You:    Logo yes (SVG). No icons, no typeface.
Model:  Logo checked: outlined text, readable at 16 px on light and dark.
        For icons I suggest Lucide (ISC license) matched to your type weight.
        Brand personality next: it directly shapes 15 other decisions. [dials, live preview]
        ...
Model:  Three directions for "calm and fast", light and dark side by side. [A] [B] [C]
        ...
Model:  Wrote DTCG tokens, CSS and Tailwind exports, DESIGN.md and the decision log.
        Validation: 0 errors, 2 warnings (explained). Still open: the brand typeface (placeholder marked).
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

Worked examples (a complete `DESIGN.md`, decision log, tokens and preview for each) will live in [`examples/`](examples/) once the engine ships. Until then, [`design/`](design/) holds a starter token set in DTCG 2025.10 with 126 contrast-checked text and background pairs, and four HTML artboards generated from it: the building-blocks map, foundations, a button sheet and the builder concept.

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
| Engine: generate, validate, export (DTCG, CSS, Tailwind, Figma, Paper, Swift, Compose) | Being finished: [`engine.py`](skills/opendesigner/scripts/engine.py) |
| Worked examples | Being built |
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
