<!-- For the agent adding this note: match it to the system. If the strictness answer (Q-gov-01) is "loose", or every area is
still a sketch (zoom 0), replace the first paragraph with this lighter one, and leave out every line that ends in a "strict" comment:
"This project has a first version of its design system in `opendesigner/`, and `DESIGN.md` describes it. Follow it, and suggest
changes to the owner instead of making them quietly." Then delete these comments; the "strict" markers are harmless if left. -->
## Design system (OpenDesigner)
This project's design is decided. The system lives in `opendesigner/`, and `DESIGN.md` is its living spec. This note keeps later AI sessions from undoing it by accident. Keep this note, `DESIGN.md` and `opendesigner/` on the branch new work starts from: a branch without them builds the old look.

**Which file decides what.** Before you change something, read the row that covers it.

| Area | Where | Read it before you change |
|---|---|---|
| Colors, type, spacing, radii, shadows, motion | `opendesigner/tokens/` (canonical) and its exports in `opendesigner/build/` (for example `build/css/tokens.css` or `build/tailwind/theme.css`) | any styling |
| What each value is for, and the rules | `DESIGN.md` and `PRODUCT.md` at the project root, including the Standards section | any screen or component |
| Why a value is what it is, and who decided | `opendesigner/decisions.md` (newest last) | a value you want to change |
| Things removed on purpose | "Removed on Purpose" in `DESIGN.md`, when it has one | adding a control, label, line, color treatment or flow |
| The states of screens that show data | `opendesigner/STATES.md`, when it exists | a list, total, status or progress display |

**When files disagree,** the owner's newest decision wins, then `decisions.md` and `DESIGN.md`, then the tokens, then older plans, audits and research, then the existing code. Code that differs from a decision is the bug. List every conflict you settled in your report.

**Never, as part of other work**
- Hard-code colors, font sizes, spacing, radii, shadows or durations. Use the tokens, or add a decision (below).
- Edit generated files by hand: `opendesigner/tokens/`, `opendesigner/build/`, or `DESIGN.md` outside `<!-- od:keep -->` blocks. Change the decision and run `engine.py build`.
- Change a locked decision (`locks` in `opendesigner/state.json`) or a standard without the owner's explicit yes. Standards are rules, not suggestions: `engine.py standard override <id> --why "<their words>"` changes one value, `engine.py standard add ... --beats <id>` records the owner's own rule, and `engine.py set --force` never changes a standard's value.
- Bring back anything listed under "Removed on Purpose".
- Restyle or reword a screen or component to suit another task. If the task seems to need a different look, word or interaction, ask. <!-- strict -->
- Weaken a check to make it pass. A raw value kept on purpose gets its reason on the same line: `od-ignore: <why, at least two words>`. The comment never waives a standard or an accessibility floor.
- Rewrite or delete entries in `opendesigner/decisions.md`. It is append-only.

**In a merge conflict** in `opendesigner/` or `DESIGN.md`, keep every entry from both sides of `decisions.md`. For `state.json`, keep the side with the newer decisions, then record the other side's decisions again with `engine.py set` and its removals with `engine.py removed add`. Never hand-merge tokens or exports: run `engine.py build`. In a UI file, keep the design side and re-apply your logic change on top.

**At the end of every implementation** (a page, a component, a refactor)
1. Run `python3 <opendesigner skill>/scripts/engine.py review`. It lists hard-coded values that skip the tokens, code that breaks a standard or brings back something removed, `od-ignore` comments without a reason, missing system files, a token file edited after the last build, tokens older than `state.json`, a locked decision that changed, and `DESIGN.md` sections that are out of date. Its last line is `Review: ok` when nothing is left.
2. Re-read the `DESIGN.md` sections you touched.
3. If the work needed a value the system lacks, add it as a decision: `engine.py set <path> <value> --why "..."`, then `engine.py design-md`. Don't inline it.
4. Fix any drift `review` reports.

**Before you open a pull request or merge,** run `engine.py review --strict` and paste its last line in your report. <!-- strict -->
Report "written", "built" and "verified" separately, and never call something verified that did not run.

**Stop and ask the owner** when a task needs a different look, word or interaction than `DESIGN.md` gives, when a change would reverse a decision or bring back a removed thing, or when an audit or reference conflicts with a decision. Keep today's design until they answer.

**To change or extend the system,** use the `opendesigner-extend` skill. When the owner removes something, record it the same day: `engine.py removed add "<what>" --why "<their words>" --instead "<what replaces it>"`. A removal never takes away an accessibility floor. The accessibility floors are part of the system, not options: WCAG 2.2 AA contrast, 24 px minimum targets, visible focus and reduced motion.

**`opendesigner/journey/` is a private log of the owner's steps.** It stays out of git. Never commit it, share it or read it into other work.

**If a step was missing, wrong or confusing,** record it with `engine.py feedback "..." --kind gap|bug|confusing|idea`. Nothing is posted without the owner's OK.
