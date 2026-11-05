---
title: Engine commands
seo_title: OpenDesigner engine commands: sketch, set, build, review
description: Every OpenDesigner engine command in one line each: start a system, record decisions, build and check, research users, standards, review and feedback.
section: Reference
order: 2
updated: 2026-11-05
---

The OpenDesigner engine is one Python file, `skills/opendesigner/scripts/engine.py`, that does the math and writes the tokens, exports and pages. Your AI usually runs these commands for you, but you can run them yourself from your project folder. It needs Python 3.10 or newer, uses only the standard library, and makes no network calls.

## How to run it

Run commands from the root of your project. The engine keeps its state in `./opendesigner/`.

```
python3 path/to/OpenDesigner/skills/opendesigner/scripts/engine.py build
```

The commands below write `engine.py` for short. If you installed the plugin, the file sits in the plugin's own folder. Every command takes `--dir` to use a different state folder, and `--help` to list its options.

{{figure:engine-commands}}

## Start a system

- `engine.py detect` reads what your project folder already answers, such as the name, platforms, brand color, font and dark mode, before any question. It changes nothing.
- `engine.py init --name "Acme"` creates `state.json` with defaults and applies the house standards that fit.
- `engine.py sketch --name "Acme" --audience regular --platforms web --feel friendly,minimal` records the five sketch answers and builds a complete first version.
- `engine.py feel fun calm` shows how the engine reads your feel words. With no words, it lists every word it knows.
- `engine.py style search frosty` finds the named styles that match your words. `style list` shows all 133, and `style mix`, `mutate`, `explore` and `define` make new ones.

The sketch takes these options:

- `--audience`: `dense` (all day), `regular` or `large` (now and then, on the go).
- `--platforms`: a comma list of `web`, `ios`, `android` and `desktop`.
- `--feel`: your feel words, in your own words.
- `--brand`: your brand color as a hex value, such as `"#167874"`.
- `--surfaces`: the main surface first, such as `"app:operate,landing page:persuade"`.
- `--delegated`: marks answers as handed over when you said "just pick", for example `--delegated feel,brand`.
- `--brief`, `--stack` and `--theme` are also accepted: your own picture of the look, your code stack, and light, dark or both. `engine.py sketch --help` explains each.

## Record decisions

- `engine.py set dials.roundness 45 --why "softer corners"` records one decision with its reason.
- `engine.py pick Q-shape-01 subtle --why "dense work tool"` answers one interview question by its id.
- `engine.py lock raw.brandColor` locks a value, and `engine.py unlock raw.brandColor` unlocks it.

`set` and `pick` share these options:

- `--why "..."`: the reason, saved in the decision log.
- `--set-by`: how it was set. One of `chosen` (the default), `confirmed_default`, `auto_default`, `assumed`, `delegated`, `reference`, `asset` or `standard`.
- `--lock`: lock the value as you set it.
- `--force`: change a locked value. Use it only with the owner's OK.
- `--no-doc`: skip refreshing `DESIGN.md` and `PRODUCT.md`.
- `--dry-run`: show what the value would change, old and new tokens and the checks, and record nothing.
- `--source-ref`: where the value came from, such as a research file, saved with the decision.

{{figure:engine-set-why}}

## Build and check

- `engine.py build` generates the tokens and checks them. If there are no errors, it writes every export, `DESIGN.md`, the overview page and the preview pages. `--force` exports even with errors.
- `engine.py generate` writes the DTCG 2025.10 tokens to `opendesigner/tokens/`.
- `engine.py validate` checks contrast, target sizes and lint rules, and exits with an error code if anything fails. `--json` prints the results as JSON.
- `engine.py export --format tailwind` writes one export. The formats are `css`, `tailwind`, `figma`, `paper`, `swift`, `compose`, `dtcg`, `artifact` and `all`.
- `engine.py design-md` writes `DESIGN.md` and `PRODUCT.md` at the project root.
- `engine.py resolve` prints the current dial positions and the values made from them, as JSON.

Run `build` after every change, so the exports and pages are never out of date.

{{figure:engine-build-output}}

## See the system

- `engine.py overview --open` writes `opendesigner/overview.html`, your whole system on one page, and opens it.
- `engine.py preview --open` writes `opendesigner/preview.html`, with every token on one page.
- `engine.py show palette --open` fills one visual template with your real values. The templates are `palette`, `type-scale`, `spacing-ruler`, `radius`, `elevation`, `motion`, `component-sheet` and `option-gallery`.

## Learn from a reference

- `engine.py intake opendesigner/references/site.json` fits measurements from a reference to proposed dial positions, each with a confidence. `--accept` accepts them all. The extract skill makes the measurement file. See [Start from an existing app or brand](/docs/existing-product/).

## Research your users

- `engine.py research plan --brief "..."` writes the plan: who the users are, what to find out, searches to start from and the tools to look for.
- `engine.py research add findings.json` checks and saves the findings, writes `research/users.md` and lists what they recommend. `research check` checks a file without saving it.
- `engine.py research market`, `positioning` and `directions` show the competitor table, draft and confirm the positioning, and write the board with three directions.
- `engine.py research skip --why "..."` records that you don't want research, and the reminders stop. `research status` says where it stands.

## Keep it consistent

- `engine.py review` scans your code for hard-coded colors, sizes, radii, shadows and durations, and for out-of-date `DESIGN.md` sections. It also says when your code uses no tokens or more raw values than tokens, and when the system is 10 or more commits behind the code. It only reports: it never edits your code. `--project src` scans one folder. `--strict` exits with an error when it finds anything.

## Standards

- `engine.py standards` lists the standards this system follows, the ones overridden and why, and any newer house standards. `--update` applies the newer ones and keeps your overrides.
- `engine.py standard override STD-ID --why "their words"` changes a house standard, only when the owner asks. `--path` releases one value instead of all of them.
- `engine.py standard restore STD-ID` follows the house standard again.
- `engine.py standard add --rule "..." --why "..." --source "..."` adds a project standard. Optional: `--path` and `--value`, `--review-pattern` and `--review-message`, `--authority`, and `--beats`.
- `engine.py standard remove PRJ-01 --why "..."` removes a project standard.

Every standard change is recorded in the decision log. See [For enterprise design-system teams](/docs/enterprise/).

## Feedback

- `engine.py feedback "the spacing question was confusing" --kind confusing` saves a note to `opendesigner/feedback.md` and prints a ready-to-file GitHub issue link. The kinds are `gap`, `bug`, `confusing` and `idea`. Nothing is posted unless you open the link and submit it.
- `engine.py feedback "buttons feel too loud" --kind note` records your own note on the work in `opendesigner/RULES.md`. A note you give twice becomes a rule later sessions follow. `--same N-01` marks a repeat of an earlier note.

## Good to know

- The same `state.json` gives the same tokens.
- `engine.py version` shows this copy's release and whether the system here was made with an older or newer one. It never checks online.
- When `set` or `pick` changes no tokens, the answer is still saved, as a `DESIGN.md` rule or a `PRODUCT.md` fact. The engine says so.
- The engine has more than 200 tests, which pass on the maintainer's computer. No CI runs are recorded yet.
