---
title: Install OpenDesigner in Claude, ChatGPT, Codex or Cursor
seo_title: Install OpenDesigner: Claude, ChatGPT, Codex, Cursor
description: How to add OpenDesigner to the AI tool you already use. Two commands for Claude Code, a Project for ChatGPT, a skills folder for Codex and Cursor.
h1: Install OpenDesigner
updated: 2026-10-14
---

OpenDesigner is free and open source (MIT). It runs inside the AI tool you already use, so there is no account to create. Pick your tool, add OpenDesigner, then say: **"Create a design system for this project."**

## Claude Code

Add the plugin from the repository's marketplace:

```
/plugin marketplace add ckryptickunal/OpenDesigner
/plugin install opendesigner@opendesigner
```

Then open your project and say "Create a design system for this project."

## Claude app (claude.ai or Claude Desktop)

Build the skill zip, then upload `dist/opendesigner.zip` under **Customize > Skills**. Code execution must be turned on.

```
git clone https://github.com/ckryptickunal/OpenDesigner && cd OpenDesigner
python3 tools/build_dist.py
```

## ChatGPT

1. Create a Project.
2. Paste `chatgpt-project/instructions.md` (the part below its line) into the Project instructions.
3. Upload the five files in `chatgpt-project/knowledge/`.

Nothing to install. The files are in the repository.

## Codex, Cursor, VS Code with Copilot, Gemini CLI and other agents

These tools read skills from `.agents/skills/`. Copy the OpenDesigner skills into your project:

```
git clone https://github.com/ckryptickunal/OpenDesigner
mkdir -p your-project/.agents/skills
cp -R OpenDesigner/.agents/skills/opendesigner* your-project/.agents/skills/
```

Tools that support Agent Plugins can also read the root `plugin.json`.

## No AI at all: the engine on its own

The engine is a small Python file (Python 3.10 or newer, standard library only, no network). It builds a complete system from a few answers:

```
python3 path/to/OpenDesigner/skills/opendesigner/scripts/engine.py sketch --name "Acme" --feel friendly,minimal
```

It writes `DESIGN.md`, `PRODUCT.md` and an `opendesigner/` folder with tokens, exports and an overview page.

## What you need

- Your own AI tool and plan. OpenDesigner is free; the AI is not part of it, and your chat goes to your AI provider as with any prompt.
- Python 3.10 or newer for the engine. In the Claude app it runs in Claude's code sandbox.
- For writing straight into Figma: Figma's MCP server and a Full seat. For Paper: Paper Desktop running.

## Honest status

OpenDesigner is new: the repository was created on 2026-09-23. The packaging for each tool is in the repository, but a recorded test run in every tool is still on the to-do list. If a step fails, [open an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new/choose) and say which tool you used.
