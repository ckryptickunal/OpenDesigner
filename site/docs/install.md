---
title: Install OpenDesigner
seo_title: Install OpenDesigner in Claude, ChatGPT, Codex or Cursor
description: How to add OpenDesigner to Claude Code, the Claude app, ChatGPT, Codex, Cursor and other agents, or run its engine with no AI. Which paths are tested so far.
section: Getting started
order: 2
updated: 2026-11-07
---

Add OpenDesigner to the AI tool you already use, open your project and say: **"Create a design system for this project."** It's free and open source (MIT), with no account to create.

{{figure:install-hosts}}

## Claude Code

```
/plugin marketplace add ckryptickunal/OpenDesigner
/plugin install opendesigner@opendesigner
```

In the Claude desktop app's Code tab, `/plugin` may not run. Run the same two steps in a terminal instead:

```
claude plugin marketplace add ckryptickunal/OpenDesigner
claude plugin install opendesigner@opendesigner
```

Then start a new session, because skills load when a session starts. You get all eight skills ([what each one does](/docs/introduction/#the-eight-skills)).

## Claude app (claude.ai or Claude Desktop)

Build the skill zip, then upload `dist/opendesigner.zip` under **Customize > Skills**. Code execution must be on.

```
git clone https://github.com/ckryptickunal/OpenDesigner && cd OpenDesigner
python3 tools/build_dist.py
```

## Codex, Cursor, VS Code with Copilot, Gemini CLI and other agents

These tools read skills from `.agents/skills/`. Copy them into your project:

```
git clone https://github.com/ckryptickunal/OpenDesigner
mkdir -p your-project/.agents/skills
cp -R OpenDesigner/.agents/skills/opendesigner* your-project/.agents/skills/
```

Tools that support Agent Plugins can read the repository's `plugin.json` instead. If your tool can't show pictures in the chat, you get the choices as text or as a local HTML page.

## ChatGPT

There is nothing to install.

1. Create a Project.
2. Paste the part of `chatgpt-project/instructions.md` below its line into the Project instructions.
3. Upload the five files in `chatgpt-project/knowledge/` from the [repository](https://github.com/ckryptickunal/OpenDesigner).

## No AI at all: the engine on its own

The engine builds a complete system from a few answers:

```
python3 path/to/OpenDesigner/skills/opendesigner/scripts/engine.py sketch --name "Acme" --feel friendly,minimal
```

It writes `DESIGN.md`, `PRODUCT.md` and an `opendesigner/` folder. See [Engine commands](/docs/engine/).

{{figure:install-engine-run}}

## What you need

- **Your own AI tool and plan.** OpenDesigner is free; the AI is not part of it.
- **Python 3.10 or newer** for the engine.
- **To write straight into Figma:** Figma's remote MCP server and a Full seat. Without them, import the variable files by hand ([Export](/docs/export/)).
- **To write into Paper:** Paper Desktop, running.

## What has been tested so far

Tested: the Claude Code install from GitHub with the terminal commands (2026-10-21), the plugin and skill packaging checks, and the engine on Python 3.10.11. Not yet recorded: a run in the Claude app, Codex, Cursor, other agents or ChatGPT.

If a step fails, please [open an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new/choose) and say which tool you used. That helps us fix the steps for everyone.

Installed? Make [your first design system](/docs/quickstart/).

## Your privacy

The engine runs on your computer and makes no network calls; your chat goes to your AI provider, as any prompt does. A private log of your steps and anonymous reports to the maintainers each need their own yes, and no server collects reports yet. See the [privacy page](https://github.com/ckryptickunal/OpenDesigner/blob/main/docs/PRIVACY.md).
