---
title: Install OpenDesigner
seo_title: Install OpenDesigner in Claude, ChatGPT, Codex or Cursor
description: How to add OpenDesigner to Claude Code, the Claude app, ChatGPT, Codex, Cursor and other agents, or run its engine with no AI. Which paths are tested so far.
section: Getting started
order: 2
updated: 2026-10-21
---

You add OpenDesigner to the AI tool you already use: two commands in Claude Code, or a skills folder, a skill zip or a ChatGPT Project in other tools. After that, open your project and say: **"Create a design system for this project."** There is no account to create.

OpenDesigner is free and open source (MIT).

{{figure:install-hosts}}

## Claude Code

Add the repository as a plugin marketplace, then install the plugin:

```
/plugin marketplace add ckryptickunal/OpenDesigner
/plugin install opendesigner@opendesigner
```

In the Claude desktop app's Code tab, `/plugin` may not run as a command. Run the same two steps in a terminal instead:

```
claude plugin marketplace add ckryptickunal/OpenDesigner
claude plugin install opendesigner@opendesigner
```

Then start a new session. Skills load when a session starts, so the session you installed from won't see them.

The plugin installs eight skills: opendesigner, opendesigner-extract, opendesigner-extend, opendesigner-export, opendesigner-illustrate, opendesigner-review, opendesigner-paint and opendesigner-preflight.

## Claude app (claude.ai or Claude Desktop)

Build the skill zip on your computer, then upload `dist/opendesigner.zip` under **Customize > Skills**. Code execution must be turned on.

```
git clone https://github.com/ckryptickunal/OpenDesigner && cd OpenDesigner
python3 tools/build_dist.py
```

The second command writes the zip files into `dist/`. In the Claude app, the engine runs in Claude's code-execution sandbox.

## Codex, Cursor, VS Code with Copilot, Gemini CLI and other agents

These tools read skills from a folder called `.agents/skills/`. Copy the OpenDesigner skills into your project:

```
git clone https://github.com/ckryptickunal/OpenDesigner
mkdir -p your-project/.agents/skills
cp -R OpenDesigner/.agents/skills/opendesigner* your-project/.agents/skills/
```

Tools that support Agent Plugins can also read the `plugin.json` file at the root of the repository.

Some of these tools can't show pictures in the chat. Then OpenDesigner shows choices as text, or writes a local HTML page you open in your browser.

## ChatGPT

There is nothing to install.

1. Create a Project.
2. Paste the part of `chatgpt-project/instructions.md` below its line into the Project instructions.
3. Upload the five files in `chatgpt-project/knowledge/`.

The files are in the [repository](https://github.com/ckryptickunal/OpenDesigner).

## No AI at all: the engine on its own

The engine is a Python file. It needs Python 3.10 or newer, uses only Python's standard library and makes no network calls. It builds a complete system from a few answers:

```
python3 path/to/OpenDesigner/skills/opendesigner/scripts/engine.py sketch --name "Acme" --feel friendly,minimal
```

It writes `DESIGN.md`, `PRODUCT.md` and an `opendesigner/` folder with tokens, exports and an overview page. See [Engine commands](/docs/engine/) for the rest.

{{figure:install-engine-run}}

## What you need

- **Your own AI tool and plan.** OpenDesigner is free, but the AI is not part of it. Your chat goes to your AI provider, as with any prompt.
- **Python 3.10 or newer** for the engine.
- **To write straight into Figma:** Figma's remote MCP server and a Full seat. Without them, you can still import the Figma variable files by hand. See [Export](/docs/export/).
- **To write into Paper:** Paper Desktop running on your computer.

## What has been tested so far

OpenDesigner is new, so here is what was checked, and when, and what was not.

- **Claude Code:** the plugin manifest passes Claude Code's own check. On 2026-10-21 a demo trial installed it from GitHub with the two terminal commands above, and the skills loaded in a new session. Typing `/plugin` into the desktop app's chat did not run it as a command.
- **Claude app:** the skill files pass the packaging check. Building the zip, uploading it and a run on claude.ai have not been recorded yet.
- **Codex, Cursor and other agents:** the eight skill folders are in the public repository. A run in each of these tools has not been recorded yet.
- **ChatGPT:** the instructions file and the five knowledge files are in the public repository. A run in ChatGPT has not been recorded yet.
- **The engine on its own:** tested with Python 3.10.11. It wrote all its files with no errors.

If a step fails, please [open an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new/choose) and say which tool you used. That helps us fix the steps for everyone.

## After you install

Say "Create a design system for this project." Then follow [Your first design system](/docs/quickstart/).

## Your privacy

The engine runs on your computer and makes no network calls. OpenDesigner asks once whether it may keep a private log of your steps in your project. Only a clear yes turns it on. Sending an anonymous report to the maintainers is a second, separate yes, and no server collects reports yet, so nothing is sent today. The full details are in the [privacy page](https://github.com/ckryptickunal/OpenDesigner/blob/main/docs/PRIVACY.md).
