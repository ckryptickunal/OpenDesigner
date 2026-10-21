# Demo trials

How we test OpenDesigner the way people will use it. Each trial is a made-up project in a throwaway folder outside this repo. Only the lessons come back here: into `_coordination/OWNER-FEEDBACK.md`, a skill rule, or a new eval case.

## Who it is for

Designers who have already built something and want it to look and work like one system. A blank new project is the rare case.

## The flow every trial should show

1. **Understand.** Read the front-end code first: pages, components, variants, hover and focus states, styles. Read the back end only where it explains behaviour. Use what the person said earlier in the session. Work out what the product is, who uses it and what problem the person is trying to solve.
2. **Audit.** Cohesion, consistency, UI, UX, motion, accessibility and brand. No fix comes before an audit.
3. **Show the value.** Show the current page, then the audit drawn on it (dashed outlines on each issue), then the fix. Each fix says what it gives the person: "fixing this makes X".
4. **Smallest version first.** Propose the MVP of the change before touching anything.
5. **Variants.** A floating button switches between 2 or 3 directions on the real page, so the person can choose by looking.
6. **Build it with them**, then show it working.
7. **Learn.** Record what this person liked as a local rule. Send product lessons to the repo only after review.

## Check every step

After each step of the flow, check it before moving on, and write the result as **done**, **partly done** (say what is missing) or **failed** (say why). Never call a step done without proof.

| After | Proof that it is done |
|---|---|
| Understand | A short summary of the product, users and problem that the person agrees with |
| Audit | Every finding has evidence: a screenshot, a measurement or a line of code |
| Show the value | The before, marked-up and after views open and render at phone and desktop widths |
| Smallest version | The person said yes to the MVP before any code changed |
| Variants | The switcher works on the real page, and each variant uses the tokens |
| Build | `engine.py validate` and `engine.py review` pass, and `opendesigner-review` finds no new issues |
| Learn | The local rule is written, and any repo lesson is in `OWNER-FEEDBACK.md` |

At the end, a fresh agent that did not do the work re-checks the whole run against this table.

## The bar for a finished "after"

A run passes only when the result is good enough to post. Kunal judges it against what designers actually save and share:
- Real content: real-looking data, names and a real product shot, with no placeholders or invented stats.
- One accent colour on neutrals, one or two typefaces, and tabular or mono figures for numbers.
- Headlines that say something specific about the product.
- A work tool aims for dense, crafted screens. A marketing page aims for a quiet light page, shown over a real photo.
- Aligned at phone, tablet and desktop widths, in light and dark. It passes preflight.

"Clean and correct" is not the bar. Trial 1's first run was clean and correct, and still read as a tidy admin template.

## Read the person's words

| They say | They usually mean |
|---|---|
| "realistic" | more images, real content, motion and animation |
| "premium" | more white space, clearer hierarchy, often a serif |
| "just build it with this" | low interest in the details: fewer questions, a short quiz or one visual to confirm |

Ask fewer questions of a non-designer. Always recommend one option.

## The trial grid

| # | Starting point | Persona | Passes when |
|---|---|---|---|
| 1 | Built app with no design system | Designer | It reads the code, audits, shows before and after, and builds the MVP |
| 2 | Built app with a messy partial system | Design lead (B2B) | The audit finds the gaps between the system and the code |
| 3 | Well-built system, rebrand | Brand designer | Identity changes, structure stays, nothing is missed in the code |
| 4 | Review of one built screen | Product manager | A plain-language verdict with evidence, nothing edited without a yes |
| 5 | "Is this better?" | Founder | Side-by-side variants, then a recommendation |
| 6 | Old project, picked up again | Solo designer | It reuses earlier decisions (asking again is fine) |
| 7 | "Make it realistic" or "make it premium" | Non-designer | It reads the word correctly and asks almost nothing |
| 8 | New project from scratch | Designer | The 5-question sketch works (rare case) |
| 9 | Export to Figma | Designer handing off | Only when asked; the file opens and matches |

Run order: 1, 2, 4, then the rest.

## How each run works

- A fresh folder (for example `~/od-trials/01-built-app/`) with a small invented app and a `.example` domain.
- OpenDesigner installed the way a user installs it, in a fresh session.
- Kunal plays the persona: vague, impatient or wrong on purpose. The agent stays in role.
- Keep the transcript and the time locally. Nothing from the folder is committed.

## Score each run (1 to 5, with a note)

1. Time to the first thing worth looking at
2. Moments of confusion (count them)
3. Questions it asked that reading the files would have answered
4. Did it audit before fixing, and show before and after?
5. Output quality: does it look premium?
6. Did it pick the right skill on its own?
7. Would the person keep going? Yes or no, and why

## The ledger: every correction becomes a fix

The point of the trials is to find what people have to ask coding agents for by hand, and to make the repo do it unasked, for every person, whatever their design experience. After each trial:
1. `python3 tools/trial_messages.py <trial folder> --out ~/od-trials/_ledger/<trial>-messages.md` pulls every message the person typed (it stays local).
2. Split each message into single corrections, and log them in `_coordination/TRIAL-LEDGER.md`: their words, the kind, how many times, and the fix.
3. Make each fix where agents read it at the right step, plus a check, and an eval when it can be graded.
4. A correction that comes back after its fix shipped is the most important finding: the fix didn't work.

The measure of progress is the "Times" column: corrections that never repeat.

## Where lessons go

| Lesson | Goes to |
|---|---|
| A mistake or a confusing step | `OWNER-FEEDBACK.md`, then a rule in the skill (`improve.md`) |
| A failure that could happen again | A case in `evals/agent/` |
| The trial's score | One line in `docs/FIELD-PLAN.md` |
| Transcripts and trial folders | Stay local |
