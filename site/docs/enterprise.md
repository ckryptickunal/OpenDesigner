---
title: For enterprise design-system teams
seo_title: OpenDesigner for enterprise design-system teams: governance
description: What OpenDesigner offers a design-system team: a decision log, locks, house and project standards, drift checks and DTCG tokens, and where it does not fit yet.
section: Guides
order: 2
updated: 2026-10-14
---

OpenDesigner gives a design-system team a written record and a set of checks: a decision log with reasons, locks, house and project standards, a check for hard-coded values in code, and DTCG 2025.10 tokens. Everything lives as files in your repository. It is early for teams: nobody has run a team pilot yet, and there is no hosted service and no SSO.

## The decision log

`opendesigner/decisions.md` records every decision, newest last. Each entry has the value, the reason, the date, whether it is locked, and what it replaces. It also says how the value was set: chosen, confirmed default, auto default, assumed, delegated, or taken from a reference, an asset or a standard. [Decisions, DESIGN.md and the overview page](/docs/decisions/) explains each one.

A suggestion nobody answered is never recorded as a decision. The log is append-only: a later entry replaces an earlier one, and nothing is edited or deleted. Here is one entry from a test run:

```
## D-0004 · raw.brandColor = "#2563eb"
- set_by: chosen · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: sketch: Level 0 answer
```

## Locked decisions

Lock any value that must not drift, such as an exact brand color:

```
engine.py set raw.brandColor '"#2563eb"' --why "brand team" --lock
```

After that, the engine refuses to change it and says to ask the owner first. The accessibility floors are locked too, unless you raise them. The optional `AGENTS.md` note tells coding agents the same.

## House standards and project standards

**House standards** are 455 rules (version 2, updated 2026-09-27) from sources the project owner marked non-negotiable. They cover areas such as motion, touch and components. The engine applies the ones that fit your platforms and locks them. In a test run, a web-only project got 289 of them. They are listed with their sources in `opendesigner/standards.md`.

A house standard changes only when someone explicitly asks. `engine.py standard override` changes one value or the whole standard, and records the reason. `engine.py standard restore` undoes it. `engine.py standards --update` applies newer house standards and keeps your overrides.

**Project standards** are your team's own rules:

```
engine.py standard add --rule "Buttons use sentence case" --why "Our content guide requires it" --source "design team, 2026-10-14"
```

- `--path` and `--value` lock token values the rule sets.
- `--review-pattern` lets `engine.py review` flag code that breaks the rule.
- `--authority` marks it non-negotiable or good-to-have.
- `--beats` names house standards your rule wins over.

Each standard change is recorded in the decision log.

## Changes go through the extend skill

Before any change, the extend skill reads `DESIGN.md`, `state.json`, the decision log, the tokens and recent git history. It reports any drift and asks only about what is new. If a request clashes with an earlier decision, it shows both and the person chooses. It ends with a short change note for the team. See [Change or extend a system](/docs/extend/).

## Drift in code

`engine.py review` finds colors, sizes, radii, shadows and durations typed into your code by hand, and names the token to use for each. It also flags code that breaks a standard and `DESIGN.md` sections that are out of date. With `--strict`, it exits with an error when it finds anything. You could run it as a check in your pipeline, though we have not tested that.

## Tokens your pipeline can read

- `opendesigner/tokens/` holds DTCG 2025.10 tokens: primitives, semantic roles, light and dark, three densities, and standard and reduced motion. One resolver file ties the modes together.
- `opendesigner/build/dtcg/` holds a single resolver file for tools that take one entry point.
- The export skill names Style Dictionary, Terrazzo, Tokens Studio and Penpot as tools that read this format. We have not tested any of them yet.
- Figma variables come with one import file per mode.

## Accessibility floors

Every system gets WCAG 2.2 AA contrast, minimum target sizes, a focus ring and reduced motion, and errors block the build. These are a minimum, so people using assistive technology should still test. See [Accessibility floors](/docs/accessibility/).

## Themes and brands

Each system has light and dark colors, three densities and a reduced-motion mode. The interview can record that more brands will re-skin the system, but the engine doesn't build separate brand modes yet. Don't plan a multi-brand rollout on it today.

## Governance questions

At deeper zoom levels, the interview asks questions only your team can answer. Examples: how strict the system is, who can add to it, how components get a status and a version, and how you announce changes. It records your answers in `PRODUCT.md` and never invents one.

## Where it does not fit yet

- **No team pilots or watched user trials.** The usability tests so far were role-played by AI testers.
- **No hosted service, accounts or SSO.** Access control is whatever your repository host gives you.
- **No CI runs and no tagged release.** Version 0.1.0 is planned. No test pass in each AI tool is recorded yet.
- **A small component set.** Only buttons, a text field and a card are previewed. The overview lists 25 components as planned.
- **No React Native or Flutter export, and no translations.**

Try it on one product, read the decision log with your team, and [tell us](https://github.com/ckryptickunal/OpenDesigner/issues/new/choose) what is missing.
