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
   - `opendesigner/decisions.md` (newest entries last), including the open questions in its newest `## Open items` entry. Ask the ones that block what the person wants now; carry the rest forward (`<opendesigner>/references/rules.md` section 7).
   - `opendesigner/tokens/`.
   - `git log --oneline -15 -- opendesigner/ DESIGN.md`, if the project uses git.
2. If `DESIGN.md.hand-edited` exists, someone edited the generated file by hand. Offer to turn each edit into a decision.
3. Run `engine.py validate`. It checks the system and reports the house standards version. If it says OpenDesigner's house standards are newer than this system's, say so in one line, run `engine.py standards --update`, then `engine.py build`, and show what changed by area. Their overrides and project standards stay as they are.
4. Run `engine.py review`. If it reports errors or drift, say so first. Fixing them may be the real task. Its guard lines catch the accidental reverts: a missing system file (a branch that lacks the design work), tokens out of step with `state.json`, and a locked decision whose value changed (often a merge that took the older side of `state.json`). Never "fix" a guard line by picking a value yourself: show both values and ask which is right.
   - If the project has an agent file (AGENTS.md, CLAUDE.md) that no longer holds the "Design system (OpenDesigner)" note, and `profile.agentsNote` in `state.json` is not `"no"`, say so in one line and offer to add it back.
5. Tell the person in three lines or fewer: the direction, the zoom level of the area they care about, and anything locked or open.
6. Ask only about what is new. Never re-run the whole interview.

In a chat-only host, ask the person to upload `state.json`, `decisions.md` and DESIGN.md before changing anything.

## 2. Classify the request
| Request | Treat it as | Do |
|---|---|---|
| "Add a date picker / pricing table / settings page" | New component or pattern | Build it from existing tokens only. List the tokens it uses. Add states and keyboard behavior |
| A new screen or flow that shows data: a list, a total, a status, progress against a limit | New screen with states | Build it like a new component, and offer to list its states first in `opendesigner/STATES.md` (copy `<opendesigner>/assets/output/STATES.md` the first time): each state's words, tone and next step, and the rows below, at and above each threshold. Build the states the person wants. When someone flags one wrong state, list every state of that feature before fixing the one named. For engineers, the template's "Building from it" offers one function per screen that returns the state's words |
| "Make buttons a bit rounder", "denser tables" | One decision | Find the question in the stage file. Show the current value and the options, then `set` it |
| "Let's define colors properly", "more detail on type" | Zoom in | Run the next zoom level for that area (`<opendesigner>/references/zoom.md`), then record it, for example `set zoom.color '"defined"'` |
| "New brand color", "dark mode", "add Android" | An area reopened | Ask that area's questions at its current zoom level |
| "Make it feel more playful", a new direction | A challenge | It touches most decisions. Say what would move (`graph.json`), offer safe choices and risks, and change nothing without a clear yes |
| "It looks dull", "this screen is wrong", a marked screenshot, a comment on a built screen | Feedback on what was built | Follow `<opendesigner>/references/rules.md` section 7, "Feedback on what was built": answer every numbered part, read for the intent, check the decisions first, treat one example as a class, and say the smallest change and what stays before you touch anything. After two rejected tries, follow the reference instead of inventing |
| "Why is X like this?" | A question | Answer from `decisions.md`, the standards (`engine.py standards`) and the cards. Change nothing |
| "Follow this guide", "use this article as a rule", a link to learn from | A new source | `<opendesigner>/references/rules.md` section 12: agree its weight, read it with consent, keep the rules they pick |
| A value that doesn't exist yet | A token addition | Add it through the engine with a reason (section 4, "Add a token"). Never hard-code it |
| "Remove the divider lines", "never show that banner again" | A removal | Remove it everywhere it appears (never an accessibility floor: focus rings, labels, alt text, reduced motion, contrast, target sizes), then record it the same day: `engine.py removed add "<what, and where>" --why "<their words>" --instead "<what replaces it>"`. Add `--pattern <regex>` when code that brings it back can be found line by line; first search the code, and make sure nothing matches except survivors marked `od-ignore: <why>`. Without a pattern, it becomes a check by hand on each screen |

## 3. Locks and conflicts
- Anything in `state.json` → `locks` (brand colors, contrast target, reduced motion, anything the owner locked) changes only with explicit consent. Name the lock and ask.
- A conflict with an earlier decision: show both and let the person choose. The new decision supersedes the old one. Nothing is edited or deleted.
- "You decide" is recorded with `--set-by delegated`.
- Something listed under "Removed on Purpose" in DESIGN.md comes back only when the person asks for it: `engine.py removed restore <R-id> --why "<their words>"`. An audit, a research note or a reference product that shows a removed thing does not count as asking.
- **Merge conflicts in the system's files.** Keep every entry from both sides of `opendesigner/decisions.md` (it is append-only). For `state.json`, keep the side with the newer decisions, then record the other side's decisions again with `engine.py set`, and its removals with `engine.py removed add`. Never hand-merge tokens or exports: run `engine.py build`, then `engine.py review --strict`. In a UI file, keep the design side and re-apply the logic change on top.

### Standards
- A value locked by a standard (house `STD-...` or project `PRJ-...`) changes only when the person explicitly asks to improve, remove or change that standard. Restate the rule and its reason once. Then their words pick the route:
  - "Just this value", "just here": `engine.py standard override <id> --why "<their words>" --path <path> [--value <json>]` (it releases only that value; without `--path`, every value the standard sets). `engine.py standard restore <id>` undoes it.
  - "It's our brand", "we always do it this way": a project standard that beats the house one, `engine.py standard add ... --beats STD-...` (`<opendesigner>/references/rules.md` section 12).
- `engine.py set --force` never changes a value a standard holds. It is only for locks the person set.
- "Follow this guide" or "this is non-negotiable for us": add it as a project standard (`<opendesigner>/references/rules.md` section 12).
- `engine.py standards` lists what applies, what was overridden and why, and any pending house updates.

## 4. Make the change
1. Show it first: the current value, the new value, and what else moves (`graph.json`). Use a template from `<opendesigner>/assets/templates/` when the host can show one.
2. Apply it with `engine.py set <Q-id or path> <value> --why "..."`. Add `--lock` if the owner wants it locked. `--force` is for person locks, never standards: use it only with the owner's consent to change a value they locked. A value a standard holds changes only through `standard override` (section 3, "Standards").
3. Refresh with `engine.py build`. It generates, validates (fix errors first), and rewrites the exports, DESIGN.md and the preview.
4. Show what changed: `git diff --stat opendesigner/ DESIGN.md` and a short table of changed values. Refresh `opendesigner/RATIONALE.md` if a big decision changed.

### Add a token
When the work needs a value the system doesn't have, first check that no existing token fits: reuse beats a near-duplicate. Then add it with a plain name for its role, in the same family as its neighbors:
```
engine.py set size.row.md 36 --why "table rows in the jobs list"
engine.py set color.bg.highlight '"#fff4c2"' --why "highlighted search matches"
engine.py set dark:color.bg.highlight '"#3a3000"' --why "the same highlight in dark mode"
engine.py set compact:space.inset.md 10 --why "tighter cards in compact mode"
```
- A new path creates the token. The engine takes its type from the value and writes it to the right file. A new color goes into the light and dark files; a new size has one value for every mode.
- A prefix (`dark:`, `compact:`) changes one mode of a token that already differs by mode, such as a color or a spacing step. Without a prefix, a change to a spacing or control-size token changes the default density only.
- Colors you add still have to pass contrast: run `engine.py build` and fix what `validate` reports.
- Tell the person the token's name and where to use it, in one line. Then use the token in the code, never the raw value.

## 5. End of every implementation: review
After building anything with the system (a page, a component, a refactor):
1. Run `engine.py review` (add `--project <folder>` to scan a specific folder; `--strict` makes findings fail the run).
2. Re-read the DESIGN.md sections you touched.
3. For every new value the work needed, add a decision. Never inline it.
4. Fix any drift that review lists (raw colors, sizes, radii, shadows or durations in code that aren't tokens). Replace each with the token for that role: a background gets a `bg` token, text gets a `text` token, a border gets a `border` token, a hover transition gets the feedback transition. The nearest value alone can pick the wrong role. Add a token if the value is genuinely new. Apply only what the person approves.
5. A raw value kept on purpose carries its reason on the same line: `od-ignore: <why, at least two words>`. Review lists those lines as kept on purpose and notes a bare `od-ignore`. The comment keeps a raw value or a removed thing; it never waives a standard or an accessibility floor, so review still reports those. When the same reason shows up three times, it is probably a missing token or a rule to change: ask the person.
6. Before a pull request or a merge, run `engine.py review --strict`. Its last line is `Review: ok` when nothing is left; quote that line in the change note.

## 6. Tell the team
End with a change note that can be read in 20 seconds:
```
Design system change, <date>
What changed: <decision, old -> new>
Why: <reason in the owner's words>
Affects: <tokens and components>
Validation: pass | <warnings with reasons>
Checked: <each command that ran and its result, for example "engine.py review --strict: Review: ok">
Not verified: <what nobody ran or looked at, riskiest first> | none
Check by hand: <numbered, riskiest first: where, one action, what should happen, what must not> | none
Skipped: <what, and why> | none
Decision log: opendesigner/decisions.md, D-<nnnn>
Open questions: <numbered, each with the default that holds until answered> | none
```
Keep "written", "built" and "verified" apart (`<opendesigner>/references/guardrails.md` section 5). A check by hand is needed whenever the change moves, answers a touch, or can only be judged on the screen or device it is for; mark a step "not seen yet" when nobody has watched it run.

## 7. Improve OpenDesigner
If a question, option or building block was missing, or a step confused the person, follow `<opendesigner>/references/improve.md` (`engine.py feedback ... --kind gap|bug|confusing|idea`). Nothing is posted without their OK.

If `profile.tracking` is `on`, log the steps as `<opendesigner>/references/rules.md` section 11 says. If it is not set, don't ask here: the log question belongs to a first run.
