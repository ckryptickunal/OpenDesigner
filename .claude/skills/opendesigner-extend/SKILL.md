---
name: opendesigner-extend
description: Changes or extends an existing OpenDesigner design system safely. Reads DESIGN.md, tokens, decisions and locks first, asks only about what is new, validates after. Use when opendesigner/ exists.
license: MIT
compatibility: Python 3.10+ (standard library). Needs the opendesigner skill's engine for generate and validate.
metadata:
  version: "0.1.0"
  homepage: "https://github.com/ckryptickunal/OpenDesigner"
---

# OpenDesigner: extend an existing system

Use this skill when the project already has an OpenDesigner system and someone wants something new. That means `opendesigner/state.json` exists, or a root DESIGN.md made by OpenDesigner. Common requests: a new component, a new theme or platform, a token tweak, zooming deeper into an area, or "why is this blue?". The goal is harmony: new work reuses existing values, and every change is recorded.

The engine is `scripts/engine.py` in this skill when it was installed from a release zip. Otherwise use the sibling opendesigner skill's `scripts/engine.py`. Run it from the project root; state lives in `./opendesigner/`. Stage files, zoom levels, rules, the glossary and the Decision Cards live in `<opendesigner>/references/`. Talk the way `rules.md` says: one idea per message, plain words first, and the person's `profile.voice`.

## 1. Start-up routine (before touching anything)
1. Read, in order:
   - `DESIGN.md` and `PRODUCT.md` (project root). Note each section's zoom line.
   - `opendesigner/state.json` (`profile.voice`, `zoom`, answers, `locks`, hooks).
   - `opendesigner/decisions.md` (newest entries last).
   - `opendesigner/tokens/`.
   - `git log --oneline -15 -- opendesigner/ DESIGN.md`, if the project uses git.
2. If `DESIGN.md.hand-edited` exists, someone edited the generated file by hand. Offer to turn each edit into a decision.
3. Run `engine.py review`. If it reports errors or drift, say so first. Fixing them may be the real task.
4. Tell the person in three lines or fewer: the direction, the zoom level of the area they care about, and anything locked or open.
5. Ask only about what is new. Never re-run the whole interview.

In a chat-only host, ask the person to upload `state.json`, `decisions.md` and DESIGN.md before changing anything.

## 2. Classify the request
| Request | Treat it as | Do |
|---|---|---|
| "Add a date picker / pricing table / settings page" | New component or pattern | Build it from existing tokens only. List the tokens it uses. Add states and keyboard behavior |
| "Make buttons a bit rounder", "denser tables" | One decision | Find the question in the stage file. Show the current value and the options, then `set` it |
| "Let's define colors properly", "more detail on type" | Zoom in | Run the next zoom level for that area (`<opendesigner>/references/zoom.md`), then record it, for example `set zoom.color '"defined"'` |
| "New brand color", "dark mode", "add Android" | An area reopened | Ask that area's questions at its current zoom level |
| "Make it feel more playful", a new direction | A challenge | It touches most decisions. Say what would move (`graph.json`), offer safe choices and risks, and change nothing without a clear yes |
| "Why is X like this?" | A question | Answer from `decisions.md` and the cards. Change nothing |
| A value that doesn't exist yet | A token addition | Add it through the engine with a reason. Never hard-code it |

## 3. Locks and conflicts
- Anything in `state.json` → `locks` (brand colors, contrast target, reduced motion, anything the owner locked) changes only with explicit consent. Name the lock and ask.
- A conflict with an earlier decision: show both and let the person choose. The new decision supersedes the old one. Nothing is edited or deleted.
- "You decide" is recorded with `--set-by delegated`.

## 4. Make the change
1. Show it first: the current value, the new value, and what else moves (`graph.json`). Use a template from `<opendesigner>/assets/templates/` when the host can show one.
2. Apply it with `engine.py set <Q-id or path> <value> --why "..."`. Add `--lock` if the owner wants it locked. Use `--force` only with consent to change a locked value.
3. Refresh with `engine.py generate`, then `engine.py validate` (fix errors first), then `engine.py design-md`, then the exports the project uses.
4. Show what changed: `git diff --stat opendesigner/ DESIGN.md` and a short table of changed values. Refresh `opendesigner/RATIONALE.md` if a big decision changed.

## 5. End of every implementation: review
After building anything with the system (a page, a component, a refactor):
1. Run `engine.py review` (add `--project <folder>` to scan a specific folder; `--strict` makes findings fail the run).
2. Re-read the DESIGN.md sections you touched.
3. For every new value the work needed, add a decision. Never inline it.
4. Fix any drift that review lists (raw colors, sizes, radii, shadows or durations in code that aren't tokens). Replace each with the nearest token, or add a token if it's genuinely new. Apply only what the person approves.

## 6. Tell the team
End with a change note that can be read in 20 seconds:
```
Design system change, <date>
What changed: <decision, old -> new>
Why: <reason in the owner's words>
Affects: <tokens and components>
Validation: pass | <warnings with reasons>
Decision log: opendesigner/decisions.md, D-<nnnn>
```

## 7. Improve OpenDesigner
If a question, option or building block was missing, or a step confused the person, follow `<opendesigner>/references/improve.md` (`engine.py feedback ... --kind gap|bug|confusing|idea`). Nothing is posted without their OK.

If `profile.tracking` is `on`, log the steps as `<opendesigner>/references/rules.md` section 11 says. If it is not set, don't ask here: the log question belongs to a first run.
