---
title: For enterprise design-system teams
seo_title: OpenDesigner for enterprise design-system teams: governance
description: What OpenDesigner offers a design-system team: a decision log, locks, house and project standards, drift checks and DTCG tokens, and where it does not fit yet.
section: Guides
order: 2
updated: 2026-11-07
---

OpenDesigner gives a design-system team a written record and a set of checks: a decision log with reasons, locks, house and project standards, a check for hard-coded values in code, and DTCG 2025.10 tokens. Everything lives as files in your repository. It is early for teams: nobody has run a team pilot yet, and there is no hosted service and no SSO.

## At a glance

| What a team needs | Status |
|---|---|
| Decision log, append-only, with reasons | Works |
| Locked values | Works |
| House standards (457 rules, version 4) and project standards | Works |
| Drift check for hard-coded values in code | Works locally; not tested in CI yet |
| DTCG 2025.10 tokens with a resolver for modes | Works |
| Figma variables, one import file per mode | Works |
| Light and dark, three densities, reduced motion | Works |
| WCAG 2.2 AA contrast, target sizes, focus ring and reduced motion, checked on every build | Works; a minimum, not an audit ([Accessibility floors](/docs/accessibility/)) |
| Style Dictionary, Terrazzo, Tokens Studio, Penpot | Named in the export skill; not tested |
| Several brands from one system | Not yet |
| React Native and Flutter exports | Not yet |
| Hosted service, SSO and roles | Not offered; your repository host's access control applies |

*What works today, and what doesn't yet.*

What runs where, and what can leave your computer: [Security and data](/docs/security/). Every export and its path: [Export](/docs/export/).

## The decision log

`opendesigner/decisions.md` records every decision, newest last: the value, the reason, the date, whether it is locked, what it replaces, and how it was set (chosen, a confirmed default, assumed, delegated, or taken from a reference, an asset or a standard). [Decisions, DESIGN.md and the overview page](/docs/decisions/) explains each one.

A suggestion nobody answered is never recorded as a decision. The log is append-only: a later entry replaces an earlier one, and nothing is edited or deleted. One entry from a test run:

```
## D-0004 · raw.brandColor = "#2563eb"
- set_by: chosen · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: sketch: Level 0 answer
```

{{figure:enterprise-log-entry}}

## Locked decisions

Lock any value that must not drift, such as an exact brand color:

```
engine.py set raw.brandColor '"#2563eb"' --set-by reference --why "brand team" --lock
```

After that, the engine refuses to change it and says to ask the owner first. The accessibility floors are locked too, unless you raise them.

{{figure:enterprise-lock}}

## House standards and project standards

**House standards** are 457 rules (version 4, updated 2026-11-02) from sources OpenDesigner's maintainer treats as non-negotiable, in areas such as motion, touch and components. The engine applies the ones that fit your platforms and locks them: a web-only test project on 5 November 2026 got 291. They are listed with their sources in `opendesigner/standards.md`.

A house standard changes only when someone explicitly asks, and the change is recorded with its reason. **Project standards** are your team's own rules, such as "Buttons use sentence case". They can lock token values, let review flag code that breaks them, and win over a house standard you name. Each change is recorded in the decision log.

:::dev
`engine.py standard override` changes one value or the whole standard and records the reason, `standard restore` undoes it, and `standards --update` applies newer house standards while keeping your overrides.

Add a project standard:

```
engine.py standard add --rule "Buttons use sentence case" --why "Our content guide requires it" --source "design team, 2026-10-14"
```

`--path` and `--value` lock the token values a rule sets, `--review-pattern` lets `engine.py review` flag code that breaks it, `--authority` marks it non-negotiable or good-to-have, and `--beats` names the house standards it wins over.
:::

## Changes and drift

Before any change, the extend skill reads `DESIGN.md`, `state.json`, the decision log, the tokens and recent git history. It reports drift, asks only about what is new, and shows both sides when a request clashes with an earlier decision. It ends with a short change note for the team. See [Change or extend a system](/docs/extend/).

`engine.py review` finds colors, sizes, radii, shadows and durations typed into code by hand, names the token for each, and flags code that breaks a standard and `DESIGN.md` sections that are out of date. With `--strict` it exits with an error, so you could run it in your pipeline, though we haven't tested that.

## Governance questions

At deeper zoom levels, the interview asks what only your team can answer: how strict the system is, who can add to it, how components get a status and a version, and how you announce changes. It records your answers in `PRODUCT.md` and never invents one.

## Pilot it with one team

If you try it, this order keeps the pilot small and reversible:

1. Start with one product, not the whole portfolio.
2. Run the sketch, then commit `DESIGN.md`, `opendesigner/tokens/` and the exports.
3. Accept the `AGENTS.md` note, so coding agents read the system before they touch the interface.
4. Lock the values that must not drift.
5. Add your team's own rules as project standards, each with a reason.
6. Read the decision log together in your design review.
7. Have each person run `engine.py review` at the end of their work.

Questions, gaps and results from a pilot are the most useful thing you can send back: open an issue with the [issue forms](https://github.com/ckryptickunal/OpenDesigner/issues/new/choose). There is one maintainer and no support agreement.

## Where it does not fit yet

- **No team pilots or watched user trials.** The usability tests so far were role-played by AI testers.
- **No CI runs.** Version 0.3.1 came out on 11 November 2026; the first tagged release was 0.2.0, on 5 November. No test pass in each AI tool is recorded yet.
- **One brand per system.** The interview can record that more brands will re-skin the system, but the engine doesn't build brand modes yet, so don't plan a multi-brand rollout on it today.
- **A small component set on the overview.** It draws only buttons, a text field and a card. The optional [component library](/library/) has 104 finished components built on the tokens, including empty, loading and error states.
- **No translations.**

Try it on one product, read the decision log with your team, and [tell us](https://github.com/ckryptickunal/OpenDesigner/issues/new/choose) what is missing.
