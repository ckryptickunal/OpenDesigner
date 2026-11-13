---
title: Install OpenDesigner
seo_title: Install OpenDesigner in Claude, ChatGPT, Codex or Cursor
description: Add OpenDesigner to Claude Code, the Claude app, ChatGPT, Codex or Cursor, or run its engine with no AI. How to update or remove it, and what is tested so far.
section: Getting started
order: 2
updated: 2026-11-10
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

Then start a new session, because skills load when a session starts. You get all nine skills ([what each one does](/docs/introduction/#the-nine-skills)).

The plugin also has one start-of-session hook. In a project with a design system (`opendesigner/state.json`), it tells Claude where the work stands each time a session starts, resumes or gets compacted, so the rules aren't lost in a long chat. It only reads files, sends nothing anywhere, and stays silent in every other project.

## Claude app (claude.ai or Claude Desktop)

You don't need a terminal.

1. Download [opendesigner.zip](https://opendesigner.dev/.well-known/agent-skills/opendesigner.zip).
2. In Claude, open **Customize > Skills**, press **+**, then **Create skill**, then **Upload a skill**, and choose the zip. Code execution must be on (**Settings > Capabilities**).

That zip builds a design system. Each of the other eight skills is its own zip, so upload only the ones you need:

| To | Also upload |
|---|---|
| Audit an app you already built | [opendesigner-review.zip](https://opendesigner.dev/.well-known/agent-skills/opendesigner-review.zip) and [opendesigner-extract.zip](https://opendesigner.dev/.well-known/agent-skills/opendesigner-extract.zip) |
| Learn from a website, a screenshot, a Figma file or a brand book | [opendesigner-extract.zip](https://opendesigner.dev/.well-known/agent-skills/opendesigner-extract.zip) |
| Change a system you already have | [opendesigner-extend.zip](https://opendesigner.dev/.well-known/agent-skills/opendesigner-extend.zip) |
| Get the system into code, Figma or Paper | [opendesigner-export.zip](https://opendesigner.dev/.well-known/agent-skills/opendesigner-export.zip) |
| Add illustrations or icons | [opendesigner-illustrate.zip](https://opendesigner.dev/.well-known/agent-skills/opendesigner-illustrate.zip) |
| Paint original art in your palette | [opendesigner-paint.zip](https://opendesigner.dev/.well-known/agent-skills/opendesigner-paint.zip) |
| Check a page, deck or video before you share it | [opendesigner-preflight.zip](https://opendesigner.dev/.well-known/agent-skills/opendesigner-preflight.zip) |
| Get a site found by search engines and AI answers | [opendesigner-search.zip](https://opendesigner.dev/.well-known/agent-skills/opendesigner-search.zip) |

The audit also measures your running app in a browser. Where your AI can't drive one, the review says what it could not check.

:::dev
To build the zips yourself:

```
git clone --depth 1 https://github.com/ckryptickunal/OpenDesigner && cd OpenDesigner
python3 tools/build_dist.py
```

They land in `dist/`.
:::

## Codex, Cursor, VS Code with Copilot, Gemini CLI and other agents

These tools read skills from `.agents/skills/`. Run this inside your project. It copies in the nine skill folders and leaves nothing else behind:

```
git clone --depth 1 https://github.com/ckryptickunal/OpenDesigner .opendesigner-tmp
mkdir -p .agents/skills
cp -R .opendesigner-tmp/.agents/skills/opendesigner* .agents/skills/
rm -rf .opendesigner-tmp
```

If your tool can't show pictures in the chat, you get the choices as text or as a local HTML page.

:::dev
Tools that support Agent Plugins can read the repository's `plugin.json` instead of the copied folder.
:::

## ChatGPT

There is nothing to install, and you don't need a terminal.

1. Download [opendesigner-chatgpt.zip](/downloads/opendesigner-chatgpt.zip) and unzip it.
2. Create a Project and paste everything in `instructions.txt` into the Project instructions.
3. Upload the five files in the `knowledge` folder.

Then start a chat in the Project and say: **"Create a design system for my app."** This bundle builds a system; it doesn't include the audit of a built app.

:::dev
The zip holds the five files of `chatgpt-project/knowledge/` in the [repository](https://github.com/ckryptickunal/OpenDesigner) and the part of `chatgpt-project/instructions.md` below its line. `python3 tools/build_dist.py` builds it.
:::

## No AI at all: the engine on its own

You can build a complete system without any AI: the engine turns a few answers into the same files the skills make.

{{figure:install-engine-run}}

:::dev
```
python3 path/to/OpenDesigner/skills/opendesigner/scripts/engine.py sketch --name "Acme" --feel friendly,minimal
```

It writes `DESIGN.md`, `PRODUCT.md` and an `opendesigner/` folder. Every command is on [Engine commands](/docs/engine/).
:::

## What you need

- **Your own AI tool and plan.** OpenDesigner is free; the AI is not part of it.
- **Python 3.10 or newer** for the engine.
- **To write straight into Figma:** Figma's remote MCP server and a Full seat. Without them, import the variable files by hand ([Export](/docs/export/)).
- **To write into Paper:** Paper Desktop, running.

## Smart UI

Nothing extra to install: Smart UI comes with OpenDesigner in every way above, and stays off until you ask for it ("make our assistant answer with our components"), or until OpenDesigner sees an assistant in your product and you say yes to its one offer. In the Claude app, upload `opendesigner-smart-ui.zip` next to `opendesigner.zip`. Its live mode needs your own model key or the `claude` command; without one, the demo replays recorded answers. [Add it to your assistant](/docs/smart-ui-quickstart/).

## What has been tested so far

Tested: the Claude Code install from GitHub with the terminal commands (2026-10-21), the plugin and skill packaging checks, and the engine on Python 3.10.11. Not yet recorded: a run in the Claude app, Codex, Cursor, other agents or ChatGPT.

If a step fails, please [open an issue](https://github.com/ckryptickunal/OpenDesigner/issues/new/choose) and say which tool you used. That helps us fix the steps for everyone.

Tried it in a tool on the "not yet recorded" list? Say what you saw in [issue #19](https://github.com/ckryptickunal/OpenDesigner/issues/19) or in [Discussions](https://github.com/ckryptickunal/OpenDesigner/discussions).

Installed? Make [your first design system](/docs/quickstart/).

## Update it

| Where | How |
|---|---|
| Claude Code | Run `claude plugin update opendesigner@opendesigner` in a terminal, or open `/plugin`, find OpenDesigner on the Installed tab and choose Update now. Then start a new session. |
| Claude app | Delete the old skill, then upload the newest zip from the links above. |
| Codex, Cursor and other agents | Run the same commands again. They write the new files over the old ones. |
| ChatGPT | Download the bundle again, then replace the Project's instructions and its five files. |

The [changelog](/changelog/) says what changed and how to see which version you have.

:::dev
`claude plugin list` shows the version you have. Updates from this marketplace stay off until you turn them on: in `/plugin`, open the Marketplaces tab, select opendesigner and choose Enable auto-update.
:::

## Remove it

First undo what it wrote in your project, while your AI can still run the engine. Everything is a plain file, so undoing it means deleting files:

- `DESIGN.md` and `PRODUCT.md` at the root, and the `opendesigner/` folder. [The files it writes](/docs/files/) lists what is inside.
- If you said yes to the note for later sessions: the part of `AGENTS.md` between the two `opendesigner` marker lines, and the `@AGENTS.md` line in `CLAUDE.md`.
- If you turned on the check before each commit: turn it off before you delete the folder.

If your code already imports the token files, change those imports first.

Then take it out of your AI tool:

| Where | How |
|---|---|
| Claude Code | Run `claude plugin uninstall opendesigner@opendesigner` in a terminal |
| Claude app | Open the skill under **Customize > Skills**, press **...** next to its switch, then **Delete** |
| Codex, Cursor and other agents | Delete the folders in `.agents/skills/` whose names start with `opendesigner` |
| ChatGPT | Delete the Project |

:::dev
- `engine.py guard remove` turns off the check before each commit. It removes only the pre-commit hook OpenDesigner wrote.
- The marker lines in `AGENTS.md` are `<!-- opendesigner:start -->` and `<!-- opendesigner:end -->`.
- `rm -rf .agents/skills/opendesigner*` deletes the nine skill folders and leaves your other skills alone.
- `claude plugin marketplace remove opendesigner` also removes the marketplace entry from Claude Code.
:::

## Your privacy

The engine runs on your computer and makes no network calls; your chat goes to your AI provider, as any prompt does. A private log of your steps and anonymous reports to the maintainers each need their own yes, and no server collects reports yet. See the [privacy page](https://github.com/ckryptickunal/OpenDesigner/blob/main/docs/PRIVACY.md).
