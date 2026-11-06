---
title: Your first design system
seo_title: Quickstart: your first design system with OpenDesigner
description: Make your first design system: the five sketch questions with example answers, the files you get, and why to open overview.html and DESIGN.md first.
section: Getting started
order: 3
updated: 2026-11-07
---

Say "Create a design system for this project" and answer up to five short questions. OpenDesigner then builds a complete first version: tokens, code exports, a `DESIGN.md` and an overview page.

## Before you start

[Install OpenDesigner](/docs/install/) in your AI tool, then open the project you want to style. An empty folder works too.

## What happens first

1. **It reads your project:** your styles, logo and fonts. It skips any question these already answer.
2. **It asks once about a private log** of your steps. Only a clear yes turns it on.

## The five questions, with example answers

The example is a made-up study planner called Studyhall. Each question comes with a suggested answer and its reason. Answer in your own words, or say "just pick" and it picks for you, recording those answers as handed over.

{{figure:quickstart-five-questions}}

1. **What are you making?** "A study planner for university students, called Studyhall."
2. **Who is it for?** All day, regularly, or now and then on the go. This sets how much fits on a screen. "Students open it most days" means regularly.
3. **Where does it run?** Web, iPhone, Android or desktop. Web alone is fine. "Web and iPhone."
4. **How should it feel?** Two or three words, like fun, calm, serious or bold. "Calm and friendly." The engine reads "calm" as minimal, with the brand in the background, and "friendly" as warmer grays and rounder corners. If it doesn't know a word, it asks you one short question.
5. **Do you have a brand color or a logo?** "Our color is #167874, a deep teal." Your color stays exact on the main buttons if it passes the contrast check; if not, the engine changes it just enough and tells you. From a logo file (PNG or SVG), it reads up to three colors for you to pick from. With neither, it suggests three colors that fit your feel words.

## What you get

- **Your design rules in plain words,** for your team and your AI tools.
- **Your whole system on one page,** with what is still a default.
- **Files your code and design tools use:** tokens, plus code for the platforms you chose and Figma variables.
- **A log of every decision** and why it was made.

:::dev
- `DESIGN.md` and `PRODUCT.md` at the root of your project.
- `opendesigner/tokens/`: your rules in the open DTCG 2025.10 format.
- `opendesigner/build/`: Figma variables, Paper tokens and code for your platforms: CSS and Tailwind for the web, Swift for iOS, Jetpack Compose for Android.
- `opendesigner/overview.html`, `preview.html`, and `decisions.md` with every decision and why.

The same build without an AI:

```
python3 path/to/OpenDesigner/skills/opendesigner/scripts/engine.py sketch --name "Studyhall" --audience regular --platforms web,ios --feel calm,friendly --brand "#167874"
```

The full list is on [The files it writes](/docs/files/).
:::

## Look at these first

### 1. The overview page

Open `opendesigner/overview.html`. It shows your whole system on one page, works offline, and marks each area **Chosen**, **Picked for you** or **Default**. Anything only you can give, such as a logo, shows as **Not enough information**, next to the question that fills it.

{{figure:quickstart-overview-status}}

Check three things: is your brand color on the main buttons, does the body text feel right, and which areas say "Not enough information"?

### 2. DESIGN.md

Your design rules in plain words, for people and AI tools. Each section shows how far it has been zoomed, so you can see what you decided and what is still a default.

## What to do next

- **Stop here.** Every level gives you working files.
- **Research your users.** It offers this right after the first version: about 10 minutes, and it does the work.
- **[Zoom in](/docs/zoom-levels/)** on one area, such as colors or text.
- **Use it in code.** See [For engineers](/docs/engineers/).

At the end, it asks before adding a short note to your `AGENTS.md`, so later AI sessions follow the same rules.

## Known rough edges

- The sketch is planned to take about 3 minutes. Nobody has timed real people yet.
- With no brand color and a calm feel, the stand-in accent can come out gray. Give a brand color, or zoom into colors.
- If something is confusing, tell your AI. It saves a note in your project with a ready-to-file GitHub link, and nothing is posted unless you submit it.
