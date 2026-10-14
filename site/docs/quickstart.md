---
title: Your first design system
seo_title: Quickstart: your first design system with OpenDesigner
description: Make your first design system: the five sketch questions with example answers, the files you get, and why to open overview.html and DESIGN.md first.
section: Getting started
order: 3
updated: 2026-10-14
---

To make your first design system, say "Create a design system for this project" and answer up to five short questions. OpenDesigner then builds a complete first version: tokens, code exports, a `DESIGN.md` and an overview page. Open `opendesigner/overview.html` first to see the whole system, then read the summary at the top of `DESIGN.md`.

## Before you start

[Install OpenDesigner](/docs/install/) in your AI tool, then open the project you want to style. An empty folder works too.

## What happens first

1. **It reads your project.** It looks for CSS, a Tailwind config, `package.json`, token files, and logo or font files. It skips any question these already answer.
2. **It asks once about a private log.** For example: "I keep a private log of your steps on this computer so I can make this faster for you. OK?" Only a clear yes turns it on.

## The five questions, with example answers

The example is a made-up study planner called Studyhall. Each question comes with a suggested answer and its reason. You can answer in your own words, or say "just pick". Then it picks for you and records those answers as handed over to it.

### 1. What are you making?

Example answer: "A study planner for university students, called Studyhall."

It writes this down so `DESIGN.md` and `PRODUCT.md` read well to a teammate.

### 2. Who is it for?

It asks whether people use it all day, regularly, or now and then on the go. This sets how much fits on a screen.

Example answer: "Students open it most days." That means regularly.

### 3. Where does it run?

The choices are web, iPhone, Android and desktop. Web alone is fine.

Example answer: "Web and iPhone."

### 4. How should it feel?

Describe the feel in 2 or 3 words, like fun, calm, serious or bold.

Example answer: "Calm and friendly."

The engine knows many plain feel words. It reads "calm" as minimal, with the brand kept in the background. It reads "friendly" as warmer grays and slightly rounder corners. If it doesn't know a word, it builds with the others and asks you one short question.

### 5. Do you have a brand color or a logo?

Example answer: "Our color is #167874, a deep teal."

The engine keeps your color exact on the main buttons when it passes the contrast check. If it doesn't pass, the engine changes it just enough and tells you. If you have neither a color nor a logo, it suggests three colors that fit your feel words.

## The same build without an AI

You can run the same sketch with the engine alone:

```
python3 path/to/OpenDesigner/skills/opendesigner/scripts/engine.py sketch --name "Studyhall" --audience regular --platforms web,ios --feel calm,friendly --brand "#167874"
```

In a test run on 2026-10-14, this took under two seconds and passed with no errors.

## What you get

- `DESIGN.md` and `PRODUCT.md` at the root of your project.
- `opendesigner/tokens/`: your rules as named values in the open DTCG 2025.10 format.
- `opendesigner/build/`: CSS variables, a Tailwind v4 theme, Figma variables, Paper tokens, Swift and Jetpack Compose files, and more.
- `opendesigner/overview.html` and `opendesigner/preview.html`.
- `opendesigner/decisions.md`: every decision with how it was set and why.

The full list is on [The files it writes](/docs/files/).

## Look at these first

### 1. The overview page

Open `opendesigner/overview.html` in your browser. It shows your whole system on one page: colors with their contrast ratios, headings h1 to h6, every text style, spacing, corners, depth, motion and core components. It works offline.

Each area is marked **Chosen**, **Picked for you** or **Default**. Anything only you can give, such as a logo or a voice guide, shows as **Not enough information**, next to the question that fills it.

Check three things:
- Is your brand color on the main buttons?
- Does the body text size feel right?
- Which areas say "Not enough information"?

### 2. DESIGN.md

`DESIGN.md` is your design rules in plain words, for people and AI tools. It opens with a short summary. Each section shows how far it has been zoomed, so you can see what you decided and what is still a default. It refreshes after every decision.

## What to do next

- **Stop here.** Every level gives you working files.
- **Zoom in** on one area, such as colors or text. See [Zoom levels](/docs/zoom-levels/).
- **Use it in code.** See [For engineers](/docs/engineers/).
- **Let your other AI tools know.** At the end, it asks before adding a short note to your `AGENTS.md`, so later AI sessions follow the same rules.

## Known rough edges

- "About 3 minutes" is the planned length of the sketch. Nobody has timed real people yet.
- If you give no brand color and pick a calm feel, the stand-in accent color can come out gray. Give a brand color, or zoom into colors.
- If something is confusing, tell your AI. It saves a note in your project and gives you a ready-to-file GitHub link. Nothing is posted unless you submit it.
