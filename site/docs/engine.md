---
title: Engine commands
seo_title: OpenDesigner engine commands: sketch, set, build, review
description: Every OpenDesigner engine command in one line each: start a system, record decisions, build and check, research users, standards, review and feedback.
section: Reference
order: 2
updated: 2026-11-10
---

The engine is the part of OpenDesigner that does the math and writes your files: the tokens, the exports, `DESIGN.md` and the pages. Your AI usually runs it for you, so use this page when you want to run a command yourself or check what one does. It runs on your computer and makes no network calls.

{{figure:engine-commands}}

## How to run it

Run commands from the root of your project, with Python 3.10 or newer. The engine keeps its state in `./opendesigner/`.

```
python3 path/to/OpenDesigner/skills/opendesigner/scripts/engine.py build
```

The tables below write `engine.py` for short. Add `--help` to any command to list its options.

:::dev
The engine is one Python file, `skills/opendesigner/scripts/engine.py`, and uses only the standard library. If you installed the plugin, the file sits in the plugin's own folder. Every command takes `--dir` to use a different state folder.
:::

## Start a system

| Command | What it does |
|---|---|
| `engine.py detect` | Reads what your project folder already answers, such as the name, platforms, brand color, font and dark mode, before any question. It changes nothing. |
| `engine.py init --name "Acme"` | Creates `state.json` with defaults and applies the house standards that fit. |
| `engine.py sketch` | Records the five sketch answers and builds a complete first version. |
| `engine.py feel fun calm` | Shows how the engine reads your feel words. With no words, it lists every word it knows. |
| `engine.py style search frosty` | Finds the named styles that match your words. `style list` shows all 133, and `style mix`, `mutate`, `explore` and `define` make new ones. |

:::dev
A full sketch:

```
engine.py sketch --name "Acme" --audience regular --platforms web --feel friendly,minimal
```

Its options:

- `--audience`: `dense` (all day), `regular` or `large` (now and then, on the go).
- `--platforms`: a comma list of `web`, `ios`, `android` and `desktop`.
- `--feel`: your feel words, in your own words.
- `--brand`: your brand color as a hex value, such as `"#167874"`.
- `--surfaces`: the main surface first, such as `"app:operate,landing page:persuade"`.
- `--delegated`: marks answers as handed over when you said "just pick", for example `--delegated feel,brand`.
- `--theme`: `system-light-dark` (light and dark, matching the device setting), `light-dark-toggle` (light and dark, plus a switch in the app), `light-only` or `dark-only`.
- `--brief` (your own picture of the look), `--stack` (your code stack) and `--logo` (your logo, PNG or SVG) are also accepted. `engine.py sketch --help` explains each.
:::

## Record decisions

| Command | What it does |
|---|---|
| `engine.py set dials.roundness 45 --set-by delegated --why "softer corners"` | Records one decision with its reason and how it was set: `chosen` with `--quote "<their words>"`, `confirmed_default`, `delegated`, `assumed` or `reference`. Fonts, the brand color, dials and answers must say which. |
| `engine.py pick Q-shape-01 subtle --set-by chosen --quote "keep corners small"` | Answers one interview question by its id. |
| `engine.py lock raw.brandColor` | Locks a value. `engine.py unlock raw.brandColor` undoes it. |

{{figure:engine-set-why}}

:::dev
`set` and `pick` share these options:

- `--why "..."`: the reason, saved in the decision log.
- `--set-by`: how it was set. One of `chosen` (the default), `confirmed_default`, `auto_default`, `assumed`, `delegated`, `reference`, `asset`, `standard` or `research`.
- `--lock`: lock the value as you set it.
- `--force`: change a locked value. Use it only with the owner's OK.
- `--no-doc`: skip refreshing `DESIGN.md` and `PRODUCT.md`.
- `--dry-run`: show what the value would change, old and new tokens and the checks, and record nothing.
- `--source-ref`: where the value came from, such as a research file, saved with the decision.
:::

## Build and check

| Command | What it does |
|---|---|
| `engine.py build` | Generates the tokens and checks them. If there are no errors, it writes the exports for the platforms you chose, `DESIGN.md`, the overview page and the preview pages, and names any code file it left out. `--force` exports even with errors. |
| `engine.py generate` | Writes the DTCG 2025.10 tokens to `opendesigner/tokens/`. |
| `engine.py validate` | Checks contrast, target sizes and lint rules, and exits with an error code if anything fails. `--json` prints the results as JSON. |
| `engine.py contrast "#767676" "#ffffff"` | Prints the contrast ratio of two colors, rounded down, and which WCAG minimums it meets. `--min 4.5` exits with an error when the pair is under 4.5:1. |
| `engine.py export --format tailwind` | Writes one export. `--format all` writes every one. |
| `engine.py design-md` | Writes `DESIGN.md` and `PRODUCT.md` at the project root. |
| `engine.py resolve` | Prints the current dial positions and the values made from them, as JSON. |

Run `build` after every change, so the exports and pages are never out of date.

{{figure:engine-build-output}}

:::dev
The export formats are `css`, `tailwind`, `figma`, `paper`, `swift`, `compose`, `dtcg`, `artifact`, `brand` and `all`.
:::

## See the system

| Command | What it does |
|---|---|
| `engine.py overview --open` | Writes `opendesigner/overview.html`, your whole system on one page, and opens it. |
| `engine.py preview --open` | Writes `opendesigner/preview.html`, with every token on one page. |
| `engine.py show palette --open` | Fills one visual template with your real values. |
| `engine.py audit-page --open` | Writes `opendesigner/audit.html`: your system as your code builds it. Each token with how often the code uses it, then each place the code and the system disagree, with the file and line, a count, and up to three ways to settle it that you can preview. |
| `engine.py adapt site.json --open` | Writes `opendesigner/adapt.html`: what a reference would change in your system and what stays yours, side by side. It records nothing. |

:::dev
The templates `show` fills are `palette`, `type-scale`, `spacing-ruler`, `radius`, `elevation`, `motion`, `component-sheet` and `option-gallery`. `audit-page` and `adapt` fill `audit` and `adapt`. Picks on the audit page come back as `OD:fix A-space-01=down` (change the code) or `OD:waive A-color-02 --why "..."` (keep it, with the reason); each becomes a ledger item. `audit-page --json` prints the page's data, every finding included.
:::

## Learn from a reference

`engine.py adapt opendesigner/references/site.json --open` shows the same fit as a page: your system now beside your system with the reference's changes, what changes, and what stays (anything you locked, your brand color and fonts). Tick what to take and copy it back. Nothing is recorded until then.

`engine.py intake opendesigner/references/site.json` fits measurements from a reference to proposed dial positions, each with a confidence. `--accept` accepts them all. The extract skill makes the measurement file. See [Start from an existing app or brand](/docs/existing-product/).

## Research your users

| Command | What it does |
|---|---|
| `engine.py research plan --brief "..."` | Writes the plan: who the users are, what to find out, searches to start from and the tools to look for. |
| `engine.py research add findings.json` | Checks and saves the findings, writes `research/users.md` and lists what they recommend. `research check` checks a file without saving it. |
| `engine.py research market`, `positioning`, `directions` | Show the competitor table, draft and confirm the positioning, and write the board with three directions. |
| `engine.py research skip --why "..."` | Records that you don't want research, and the reminders stop. `research status` says where it stands. |
| `research.py coverage` | Checks the research against the full list: users and their tasks, the competitors' design systems, accessibility, platform conventions, content and voice, your analytics, and stakeholders. Says what is missing and which tool would fill it. |
| `research.py stakeholders scan`, `interview`, `answer`, `show`, `decide` | Skips itself on a solo project (it records "solo: not needed"). Otherwise finds who has a say from your repo, drafts at most five questions for each role, records each answer with who said it, and shows where people agree and where they differ. Only an agreed point becomes a decision on its own; you settle a conflict in your own words. |
| `research.py summary` | Writes `research/summary.html`: the users, the market, what each stakeholder said and what is still open, on one page to share with your team. |

## Keep it consistent

`engine.py review` scans your code for hard-coded colors, sizes, radii, shadows and durations, and for out-of-date `DESIGN.md` sections. It also says when your code uses no tokens or more raw values than tokens, when the brand color or fonts in `DESIGN.md` appear nowhere in your code, and when the system is 10 or more commits behind the code. It also notices when a merge undid a locked decision or a token file was edited by hand. Its last line is `Review: ok`, or how many things are left to fix and why. It only reports: it never edits your code.

{{figure:engineers-review-terminal}}

With no system in the project, it still counts the hard-coded values and names any system it finds in a subfolder. It fails when `AGENTS.md`, `CLAUDE.md` or `DESIGN.md` point at an `opendesigner/` folder that isn't there.

Two more commands keep later sessions on the same system:

| Command | What it does |
|---|---|
| `engine.py status` | Prints where the work stands: the step you're on, what waits for you and the next command. It changes nothing. Run it first in a new session. |
| `engine.py handoff yes` | Writes a short note into your `AGENTS.md`, and a `CLAUDE.md` that imports it, so later AI sessions read the system first. `handoff no` writes nothing. Either answer is recorded, so you're asked once. |

:::dev
`--project src` scans one folder, or one file. When that folder has fewer than three style files, review also reads the page the site ships (the newest `index.html`, in `public/` first) and the files it loads, and lists what it skipped. Findings come newest file first. `docs/` and OpenDesigner's own exports are skipped. `--strict` exits with an error on any finding, tokens not in charge, a `DESIGN.md` that disagrees with the code or validate errors, and names each reason. `engine.py guard install` runs it before every commit, after you say yes; `git commit --no-verify` skips it once and `guard remove` takes it out. `guard status` says whether it is on.

`status --json` prints the same facts as JSON. `status --hook` is what the Claude Code plugin runs when a session starts: five short lines, and nothing in a project with no system.
:::

**What each round did.** Before an AI builds something, it opens a round in the ledger and lists what the round covers. Each item ends as done, broken (with what broke) or skipped on purpose (with the reason and who decided). `review` lists every open item and `review --strict` fails on one, so nothing is quietly dropped, and `DESIGN.md` shows the ledger.

| Command | What it does |
|---|---|
| `engine.py ledger start "Settings page" --items comp.action.button,A-space-01` | Opens a round. An item can be a building block (it counts toward the system's coverage), something from the audit page, or your own name. |
| `engine.py ledger done A-space-01` | Marks it done. `ledger broke <item> --note "..."` records what broke; `ledger waive <item> --why "..." --by owner --quote "your words"` skips it on purpose. An AI can waive with `--by agent`, but the round won't close until you agree. |
| `engine.py ledger close` | Closes the round, and refuses while anything is open. `ledger show` lists every round. |
| `engine.py exempt site/figures --why "demo figures show mistakes on purpose" --by owner` | Keeps files that break the system on purpose out of review. Review lists them, with the reason, so they are never hidden. |

**Things removed on purpose.** Code keeps no record of what was taken out, so a later session tends to add it back. Record a removal the day it happens.

| Command | What it does |
|---|---|
| `engine.py removed add "divider lines between rows" --why "their words" --pattern "border-bottom"` | Records something the owner removed. `DESIGN.md` lists it under "Removed on Purpose", and `review` flags code that brings it back. A pattern that would catch a focus ring, label, alt text, reduced-motion code or a target size is refused. |
| `engine.py removed list` | Lists what was removed, and what was brought back. |
| `engine.py removed restore R-01 --why "their words"` | Allows it again. Only the owner brings a removed thing back. |

## Standards

| Command | What it does |
|---|---|
| `engine.py standards` | Lists the standards this system follows, the ones overridden and why, and any newer house standards. `--update` applies the newer ones and keeps your overrides. |
| `engine.py standard override STD-ID --why "their words"` | Changes a house standard, only when the owner asks. `--path` releases one value instead of all of them. |
| `engine.py standard restore STD-ID` | Follows the house standard again. |
| `engine.py standard add --rule "..." --why "..." --source "..."` | Adds a project standard. |
| `engine.py standard remove PRJ-01 --why "..."` | Removes a project standard. |

Every standard change is recorded in the decision log. See [For enterprise design-system teams](/docs/enterprise/).

:::dev
`standard add` also takes `--path` and `--value`, `--review-pattern` and `--review-message`, `--authority`, and `--beats`.
:::

## Feedback

| Command | What it does |
|---|---|
| `engine.py feedback "the spacing question was confusing" --kind confusing` | Saves a note to `opendesigner/feedback.md` and prints a ready-to-file GitHub issue link. The kinds are `gap`, `bug`, `confusing` and `idea`. Nothing is posted unless you open the link and submit it. |
| `engine.py feedback "buttons feel too loud" --kind note` | Records your own note on the work in `opendesigner/RULES.md`. A note you give twice becomes a rule later sessions follow. `--same N-01` marks a repeat of an earlier note. |

## Good to know

- The same `state.json` gives the same tokens.
- `engine.py version` shows this copy's release and whether the system here was made with an older or newer one. It never checks online.
- When `set` or `pick` changes no tokens, the answer is still saved, as a `DESIGN.md` rule or a `PRODUCT.md` fact. The engine says so.
- The engine has more than 200 tests, which pass on the maintainer's computer. No CI runs are recorded yet.
