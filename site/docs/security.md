---
title: Security and data
seo_title: OpenDesigner security: what runs where and what data is sent
description: Where OpenDesigner runs, what leaves your computer and what never does, the opt-in journey log, how to report a vulnerability, and its release status.
section: Reference
order: 6
updated: 2026-11-08
---

OpenDesigner is files in your repository plus a small engine that runs on your own computer. There is no hosted service, no account and no server that receives your design. Apart from your chat with your AI tool, it reaches the internet only for a few features you choose to use. They're listed below, for a security or platform team to check before a pilot.

## What runs where

| Part | Where it runs | Network |
|---|---|---|
| The engine | On your computer | None: no network calls |
| The skills (instructions) | Inside the AI tool you already use | Your chat goes to that tool's AI provider, as any prompt does |
| The Claude app | The engine runs in Claude's code-execution sandbox | Whatever that sandbox allows |
| The illustration skill | On your computer | Searches and fetches open-licence art, icons and stock photos, only when you use it |
| The review skill | On your computer | Local addresses only. Its optional browser driver is installed only after you say yes |
| The paint skill | On your computer | Its painting engine is installed only after you say yes, and renders locally |

:::dev
- **The engine** (`engine.py`) needs Python 3.10 or newer and only the standard library.
- **The illustration skill** (`opendesigner-illustrate`) fetches over HTTPS from Openverse, Wikimedia Commons, and Pexels with your own key.
- **The review skill** (`opendesigner-review`): `review.py serve` listens on 127.0.0.1 only while you run it. The optional `capture.py` drives a browser to local addresses only and needs Playwright, which is installed only after you say yes.
- **The paint skill** (`opendesigner-paint`) installs its painting engine with npm.
:::

Everything OpenDesigner writes stays in your project, except taste poll screens, which stay in a folder in your home directory. [The files it writes](/docs/files/) has the full list.

:::dev
In your project: `opendesigner/` (tokens, exports, the decision log), `DESIGN.md` and `PRODUCT.md`. Taste poll screens: `~/.opendesigner/`.
:::

## What can leave your computer

- **Your conversation with your AI tool,** with OpenDesigner's instructions added. The tool you chose decides where it goes, not OpenDesigner.
- **Illustration and photo searches,** when you ask for them and say yes to the search.
- **Photos in library parts.** If you add a library part with a photo, the page loads that photo from Unsplash when someone opens it.
- **Package downloads for the paint engine** (npm and a browser for rendering), only after you say yes. Nothing about your project is sent.
- **Taste poll screens,** if your AI tool is connected to Mobbin and the poll needs more. They're saved on your computer, and nothing about your project is sent.
- **Nothing else by default.** The journey log and shared reports below are both off until you say yes.

## The journey log and shared reports

These are two separate choices, and both start switched off.

- **The journey log** is a private diary of the steps you take, kept in your project and out of git. It is never sent. One command turns it off and deletes it.
- **Shared reports** are an anonymous summary for the OpenDesigner team: which questions came up, how long each took, skips and help requests, the version, the AI tool and the week. They never include your answers, names, colors, brand, files, paths or anything you typed, and carry no ID tied to you or your device.
- **No server collects reports yet.** Until one exists, reports wait in your project files and nothing is sent. Before you agree, a dry run shows exactly what a report contains.

:::dev
- The journey log lives in `opendesigner/journey/`.
- Turn it off and delete it: `journey.py consent off --forget`.
- See what a report contains: `journey.py share --dry-run`.
:::

The full wording of both questions is in [docs/PRIVACY.md](https://github.com/ckryptickunal/OpenDesigner/blob/main/docs/PRIVACY.md).

## Access and accounts

There are no OpenDesigner accounts, roles or SSO. Whoever can change the repository can change the design system, so your repository host's access control, branch protection and review rules apply. Locked decisions add one more guard: the skills refuse to change a locked value without the owner's consent ([For enterprise design-system teams](/docs/enterprise/)).

## Report a vulnerability

Report security problems privately, never in a public issue:

1. Open the repository's **Security** tab.
2. Choose **Report a vulnerability** (GitHub private vulnerability reporting).
3. Describe the problem, the affected files and how to reproduce it.

You should get a first reply within 7 days. What counts, and how secrets are kept out of the repository, is in [SECURITY.md](https://github.com/ckryptickunal/OpenDesigner/blob/main/SECURITY.md).

## Release and maintenance status

- **Version 0.3.1 is the latest release,** from 11 November 2026. Security fixes land on `main` and ship in the next release.
- **One maintainer.** There is no support agreement.
- **No continuous integration runs are recorded yet.** The engine's tests pass on the maintainer's computer.
- **Licence:** MIT for code, skills and data; CC BY 4.0 for the docs.

The repository was created on 2026-09-23. Treat it as early software, and pin the commit you adopt.
