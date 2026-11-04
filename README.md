<p align="center">
  <a href="https://opendesigner.dev">
    <picture>
      <source media="(max-width: 600px)" srcset="https://raw.githubusercontent.com/ckryptickunal/OpenDesigner/main/brand/kit/readme/banner-narrow.png">
      <img src="brand/kit/readme/banner.png" width="1012" alt="OpenDesigner. Make everything you build look like it belongs together. Your AI tools know what to build. OpenDesigner tells them how it should look.">
    </picture>
  </a>
</p>

<p align="center">
  <a href="https://opendesigner.dev"><b>Website</b></a> &nbsp;·&nbsp;
  <a href="https://opendesigner.dev/docs/">Docs</a> &nbsp;·&nbsp;
  <a href="https://opendesigner.dev/showcase/">Showcase</a> &nbsp;·&nbsp;
  <a href="#quickstart">Install</a> &nbsp;·&nbsp;
  <a href="CONTRIBUTING.md">Contribute</a> &nbsp;·&nbsp;
  <a href="https://calendar.app.google/42qSQUrBiSL4CHfv6">Book a 20-minute intro call</a>
</p>

**A free, open-source (MIT) add-on for your AI coding tool. It gives your product one design system and checks every screen against it.**

<p align="center">
  <picture>
    <source media="(max-width: 600px)" srcset="https://raw.githubusercontent.com/ckryptickunal/OpenDesigner/main/brand/kit/readme/works-in-narrow.png">
    <img src="brand/kit/readme/works-in.png" width="1012" alt="Works in Claude Code and the Claude app, ChatGPT and Codex, Cursor, GitHub Copilot and Gemini CLI.">
  </picture>
</p>

## Two ways in

**Fix what you built.** It audits every button, font, size, color and alignment on your pages, marks each problem with the rule it breaks, and fixes it after your yes.

**Build a system.** It reads your repo, studies your competitors, proposes a positioning and three directions, then writes the rules your AI follows.

<picture>
  <source media="(max-width: 600px)" srcset="https://raw.githubusercontent.com/ckryptickunal/OpenDesigner/main/brand/kit/readme/before-after-narrow.png">
  <img src="brand/kit/readme/before-after.png" width="1012" alt="Two versions of an invoices page. Today: seven issues boxed and numbered, such as three filled buttons, gray text at 2.54:1, amounts that don't line up and status shown by color alone. Fixed: the same page on its own design system, with a check where each fix landed and the money shown as a bento of small charts.">
</picture>


## Every round

- **A plan you sign off,** step by step, written to `opendesigner/PROTOCOL.md` so any AI follows it.
- **Checks before you see it:** contrast, tap targets, type scale, letter-spacing, alignment, buttons, text over images.
- **Screenshots,** before and after. Not a link to open.
- **Your notes stick.** Say something twice and it becomes a rule.

## What lands in your repo

`DESIGN.md`, `PRODUCT.md`, design tokens (DTCG), CSS, Tailwind, Figma, Swift and Compose exports, and a log of every choice with its reason.

## Quickstart

1. Add OpenDesigner to your AI tool. Pick yours below.
2. Open your project and say: **"Create a design system for this project."**
3. Answer a few short questions. It reads your files first, so it asks less.

**Claude Code**

```
/plugin marketplace add ckryptickunal/OpenDesigner
/plugin install opendesigner@opendesigner
```

<details>
<summary><b>Claude app</b> (claude.ai or Desktop)</summary>

Build the skill zip, then upload `dist/opendesigner.zip` under Customize > Skills. Code execution must be on.

```bash
git clone https://github.com/ckryptickunal/OpenDesigner && cd OpenDesigner
python3 tools/build_dist.py        # writes the zip files into dist/
```

</details>

<details>
<summary><b>Codex, Cursor, VS Code with Copilot, Gemini CLI and other agents</b></summary>

These tools read skills from `.agents/skills/`. Copy the OpenDesigner skills into your project. Tools that support Agent Plugins can also read the root `plugin.json`.

```bash
git clone https://github.com/ckryptickunal/OpenDesigner
mkdir -p your-project/.agents/skills
cp -R OpenDesigner/.agents/skills/opendesigner* your-project/.agents/skills/
```

</details>

<details>
<summary><b>ChatGPT</b> (web, any plan, nothing to install)</summary>

1. Create a Project.
2. Paste [`chatgpt-project/instructions.md`](chatgpt-project/instructions.md) (the part below its line) into the Project instructions.
3. Upload the five files in [`chatgpt-project/knowledge/`](chatgpt-project/knowledge/).

</details>

<details>
<summary><b>No AI at all</b> (the engine on its own)</summary>

The engine is one Python file (Python 3.10 or newer, nothing to install). It writes `DESIGN.md`, `PRODUCT.md` and an `opendesigner/` folder with tokens, exports and an overview page.

```bash
python3 path/to/OpenDesigner/skills/opendesigner/scripts/engine.py sketch --name "Acme" --feel friendly,minimal
```

</details>

You need your own AI tool and Python 3.10 or newer. The engine makes no network calls ([privacy](docs/PRIVACY.md)). Help for each tool: [install guide](https://opendesigner.dev/docs/install/).

## Component library

<picture>
  <source media="(max-width: 600px)" srcset="https://raw.githubusercontent.com/ckryptickunal/OpenDesigner/main/brand/kit/readme/library-narrow.png">
  <img src="brand/kit/readme/library.png" width="1012" alt="Six ready-made parts: an approval panel, a monthly spend chart, a command menu, an AI answer with citations, an order summary and settings switches.">
</picture>


82 ready-made parts built only on your tokens. Optional. [Browse them](https://opendesigner.dev/library/).

## Status

- Version 0.2.0, the first tagged release, 5 November 2026. One maintainer.
- Engine tests pass locally. No CI runs, and no watched user trials yet.
- Next: choices you can click inside your AI tool ([#20](https://github.com/ckryptickunal/OpenDesigner/issues/20)).

[Changelog](CHANGELOG.md) · [How it works](docs/HOW-IT-WORKS.md) · [Research behind the defaults](docs/RESEARCH.md) · [Showcase](https://opendesigner.dev/showcase/)

## Help it get better

Tell your AI what went wrong. It saves the note and gives you a ready-to-file GitHub link; nothing is posted until you send it. Or [open an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new/choose). Contributions: [CONTRIBUTING.md](CONTRIBUTING.md). Sponsorship: [docs/SPONSORSHIP.md](docs/SPONSORSHIP.md#for-sponsors).

<!-- Partners: large logos. Companies: small logos. Backers: names. Supported by: in-kind credit programs (never leave the wall empty). -->
<!-- When GitHub Sponsors is approved, point the link above at https://github.com/sponsors/ckryptickunal (see docs/SPONSORSHIP.md). -->

## Star history

<a href="https://github.com/ckryptickunal/OpenDesigner/stargazers">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="brand/kit/readme/stars-dark.svg">
    <img src="brand/kit/readme/stars-light.svg" width="600" alt="OpenDesigner's GitHub stars over time, redrawn from GitHub every 3 hours">
  </picture>
</a>

## License

Code, skills, templates and data files are under the [MIT license](LICENSE). Written research and documentation are under [CC BY 4.0](LICENSE-CONTENT), so you can reuse them with credit. That covers `research/`, `benchmarks/`, `sources/`, `traces/`, `synthesis/` Markdown and `docs/`. Product and design-system names in the research belong to their owners. The tool marks in the "works in" row belong to their owners and only show where OpenDesigner runs (from [Simple Icons](https://simpleicons.org), CC0). Photos in the README images are from Unsplash: [Philipp Hubert](https://unsplash.com/photos/dVVjhUcdb30) (banner), [Sean Fahrenbruch](https://unsplash.com/photos/kxL6jPPNEWc) (how it works), and [Photoholgic](https://unsplash.com/photos/HVQnG6JxxY0), [Annie Spratt](https://unsplash.com/photos/5yKrcO8FKwM) and [Harshal Tandel](https://unsplash.com/photos/BrzWSKWCuWo) (examples).

To cite OpenDesigner or its research, use [CITATION.cff](CITATION.cff) (GitHub's "Cite this repository" button).
