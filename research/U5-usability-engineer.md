# U5 usability test: engineer persona (Arjun)

Session "U5 engineer", 2026-09-24. Tester played both roles: the model (following `skills/opendesigner/SKILL.md`, `rules.md`, `zoom.md`, `guardrails.md`, `improve.md`, `opendesigner-export`, `opendesigner-extend`) and Arjun (backend engineer, internal admin tool, React 19 + Tailwind v4 via Vite, dense tables and forms, desktop only, no brand, no designer, impatient, switches to the engineer voice).

The scratch project lived in the session scratchpad (`arjun-admin/`), never in the repo. It had 7 hard-coded hex colors, a `boxShadow`, a 250 ms transition, `borderRadius: 10` and `padding: 20` planted in `Sidebar.jsx` and `UserForm.jsx`. Every engine, journey and export command below was actually run (engine 1.0.0, skill 0.1.0). Tailwind output was checked by compiling with a Tailwind 4.3.3 copy already installed on this machine (`@tailwindcss/node` + oxide scanner, read-only, nothing downloaded).

## Result in one paragraph
The first export files existed after 7 messages (4 from the model, 3 from Arjun), because `sketch` builds every export. Arjun's "just pick something" was taken at once for personality and seed color. Even so, tokens were wired into the app and compiling only after 13 messages, against about 9 for an ideal run. The delegated picks came out gray (the seed blue vanished) and the fix answer (`Q-color-03 tonal`) did nothing, which cost about 2 messages. The 7-line share question, which has to come right after the result, cost 2 more. The Tailwind v4 `@theme inline` + CSS-variable exports dropped in with two `@import` lines, and every token utility compiled, hover and disabled variants included. The extend flow built a jobs data table from existing tokens only. `review` found 8 of the planted values, but it misses the React/Tailwind forms of drift (JSX numbers, arbitrary values, default utilities). DESIGN.md refreshed itself after every decision.

## Short transcript
Model voice lines are condensed. "M" = model, "A" = Arjun. Commands run are in brackets.

| # | Who | Message (condensed) | Commands |
|---|---|---|---|
| M1 | model | "I'll help you set up your design system... 5 quick questions. I read your repo: React 19 + Tailwind v4, 9 hard-coded colors, two blues. I keep a private log of your steps on this computer so I can make this faster for you. OK?" | `engine.py init --name "Ops Admin"` |
| A1 | Arjun | "sure. keep it quick." | `journey.py consent on` |
| M2 | model | "First: what are you making?" | `log step_shown --step Q-scope-01` |
| A2 | Arjun | "Internal admin for ops: users, jobs, billing. Big tables and forms. Desktop browser only. Just pick something sensible for the rest." | `set context.product`, `log frustration --signal just_do_it`, `log speed_mode` |
| M3 | model | "One app for getting work done, desktop web. One thing I shouldn't guess: density (plain + Designers/Code line). Is it used all day (dense) or a few times a week (regular)?" (rules.md 7: push back once on audience) | `log step_shown --step Q-aud-01` |
| A3 | Arjun | "All day. And talk like an engineer, I know what a token is." | `log help --kind voice_switch`, `set profile.voice "engineer"`, `set macros [serious,minimal] --set-by delegated`, `set raw.brandColor "#2563eb" --set-by delegated` (seed = the button blue already in UserForm.jsx), `sketch --audience dense --platforms web --surfaces "admin app:operate"` |
| M4 | model | Result: compact (32 px controls, 14 px body), flat, system-ui, light+dark. Flag: "serious+minimal made the palette monochrome; your blue appears nowhere, primary buttons are near-black." Offer: stop, or zoom into Color / Components. | preview at `opendesigner/preview.html` |
| A4 | Arjun | "Blue on links, focus and the primary button. Rest is fine. Then wire it into my Tailwind setup." | `pick Q-color-03 tonal` (no effect, see F1), `set dials.colorfulness 45` (workaround), 2x `engine.py feedback --kind bug`, `build` |
| M5 | model | "Accent is now #60769f (from your blue, toned for contrast)." + the share-consent block, word for word (rules.md 11) | `journey.py share-consent` |
| A5 | Arjun | "Don't share." | `share-consent never`; `share` and `share --yes` both print "Not sent: sharing is off." |
| M6 | model | Play-back of the decisions with how each was set, plan to edit `src/index.css`. "OK to edit it?" | none |
| A6 | Arjun | "Yes, just index.css for now." | 2 `@import` lines + tokens on `body` |
| M7 | model | Wired; Tailwind class names; finish summary; "Add the OpenDesigner snippet to AGENTS.md?" | `opendesigner/RATIONALE.md` written, snippet appended after the yes, `log session_end`, `report` |
| (later) | Arjun | "Add a jobs data-table screen: sortable, status badges, row actions, pagination. Keep it consistent." | extend start-up: read DESIGN.md, state, decisions, `git log`, `review` (8 findings) |
| E1 | model | "Flat, compact, one muted blue; Components is at sketch; nothing locked. Review found 8 hard-coded values in Sidebar and UserForm. Table first, or fix those first?" | none |
| E1a | Arjun | "Table first." | none |
| E2 | model | "Tables page with numbered pages (recommended), or load more? Rows: lines (recommended) or zebra?" | `log step_shown --step Q-pattern-02` |
| E2a | Arjun | "Just build it." | `log frustration just_do_it`, `set Q-pattern-02 pagination --set-by delegated`, `set components.notes.table "..." --set-by delegated` |
| E3 | model | Built `JobsPage.jsx` + `StatusBadge.jsx` from token classes only; listed tokens used; review shows the 8 old values with fixes. "Fix them?" | `review` |
| E3a | Arjun | "Yes." | Sidebar and UserForm rewritten with tokens (the model picked roles by hand, not review's suggestions, see F9); `review` is clean; DESIGN.md re-read |
| E4 | model | 20-second change note: Q-pattern-02 and the table note (D-0011, D-0012), validation passes, drift fixed. | `log session_end`, `report`, `share` (refused) |

## Measurements
| Measure | Result |
|---|---|
| Messages to first export files (`build/tailwind/theme.css`, `build/css/tokens.css`) | **7** (M1 to M4, 4 model + 3 Arjun). That is the fewest the skill allows after "just pick" at Q1: the log question and one audience push-back are both required |
| Messages to a working export wired into the app and compiling | **13** (M1 to M7, 7 model + 6 Arjun), against about 9 for an ideal run: the share block (F11) added 2 and the gray-palette fix (F4, F1) added 2 |
| Time | Simulated clock from greeting: exports at about 1 min, wired at about 4 min; each `sketch` / `build` takes 0.2 s. Estimated human time including reading and typing: about 3 min to exports and 6 min to wired [inferred]. The journey log recorded 7 min over 2 sessions |
| "Just pick something" honoured quickly? | **Partly.** Personality and seed were delegated at once with no extra question. There was one rule-mandated push-back on audience. The delegated result then needed a fix round (A4 to M5) because it came out gray, and the fix answer itself did nothing (F1, F4). The second "just build it" (extend) was honoured at once |
| Exports drop-in? | **Yes, with caveats.** Two `@import` lines after `@import "tailwindcss"`. Tailwind 4.3.3 generated every token utility tried (`bg-action-primary`, `text-fg-primary`, `border-line-subtle`, `rounded-control`, `shadow-raised`, `p-inset-md`, `h-size-control-md`, `text-body-md`, `transition-feedback`, `hover:`/`disabled:` variants). CSS variables cover light/dark (`prefers-color-scheme` + `[data-theme]`), density (`[data-density]`, compact default), reduced motion, and a 24 px pointer / 44 px touch target floor. Caveats: F7, F8, F14, F15 |
| Review found the drift? | **8 of 11 planted values**: 6 hex colors, the `boxShadow`, the 250 ms transition. Missed: `borderRadius: 10`, `padding: 20`, `background: '#ffffff'` on the shadow line, and Tailwind defaults (`rounded`, `text-lg`, `text-white`). After the fixes, review was clean |
| DESIGN.md updated? | **Yes.** Every `set` refreshed it: the table note in Components (zoom sketch to broad), D-0011 and D-0012 in Decisions, the delegated list in Open Items, and "DESIGN.md matches state.json" from review. One wrong line: Audience (F10) |
| "Don't share" respected? | **Yes.** `share` and `share --yes` both refused; unsent reports were deleted; the only network call in `journey.py` (line 540) sits behind the choice. `opendesigner/journey/.gitignore` keeps the log out of git. `export --anon` held no project strings (0 matches for the project name, the seed hex or note text) |

## Friction
Severity: 3 = wrong output or broken promise, 2 = costs messages or misleads, 1 = polish. The engine is owned by R2, so engine fixes go there as messages.

| # | Step | What happened | Sev | Exact fix | File |
|---|---|---|---|---|---|
| F1 | Color fix (A4) | `pick Q-color-03 tonal` was recorded, but tokens stayed monochrome. The same is true for `Q-color-02` (a level-1 screen) and `Q-dir-02 spacious`: the token hash was unchanged after each pick. `pick` still says "tokens update on the next generate" | 3 | Add `answer_effects` branches: Q-color-03 to `dials.colorfulness` {monochrome 5, tonal 45, expressive 75, vivid 92; fidelity also sets `raw.flags.brandExact`}; Q-color-02 to `color.brandPlacement`; Q-dir-02 to `dials.density` {compact 80, comfortable 50, spacious 20}. Make `set`/`pick` print "recorded; no token effect yet" for any Q-id with no mapping | `skills/opendesigner/scripts/engine.py` `answer_effects` (~l. 2674) |
| F2 | Extend: new value | `set size.row.md 36` is accepted and logged as a decision, but no token is written (only `meta.json` gets `override: true`). opendesigner-extend section 2 promises "a token addition through the engine" | 3 | When the path is new, create the token (type taken from the value, in `semantic.tokens.json`, `source: person`), or exit 1 with "no such token; to add one use ...". Never log a no-op as a decision | engine.py `apply_token_overrides` (~l. 1845) |
| F3 | Review | Plain CSS is caught; the React/Tailwind forms are not. In a probe, 0 of 15 were flagged: `borderRadius: 10`, `padding: 20`, `fontSize: 15`, `borderRadius: '10px'`, `padding: '20px'`, `rounded-[10px]`, `p-[13px]`, `text-[15px]`, `shadow-[0_4px_12px_rgba(...)]`, `duration-[250ms]`, `bg-blue-600`, `text-white`, `rounded-lg`, `shadow-md`, `text-lg`. A hex on the same line as a shadow is skipped too | 3 | Match camelCase props with unitless numbers or `'Npx'` in `.jsx/.tsx`. Match Tailwind arbitrary values `\b[\w-]+-\[([^\]]+)\]`. When `build/tailwind/` exists, flag default-palette, radius, shadow and text-size classes. Scan hex outside the shadow's match span only | engine.py `RX_SIZE` (l. 4966), review loop (~l. 5046-5054) |
| F4 | Sketch (M4) | `serious,minimal` stacks colorfulness 40 - 25 - 20 = -5, clamped to 0, so the scheme is monochrome and the delegated seed #2563eb appears in no role (links and focus are gray) with no warning. `08-color-system.md` says the default for productivity products is tonal | 2 | When `raw.brandColor` is set and Q-color-03 is not `monochrome`, floor colorfulness at 36 (tonal band); or have `validate` WARN "brand color appears in no role" | `skills/opendesigner/references/levers.json` macroRules / engine.py resolve |
| F5 | Sketch (A3) | `sketch` has no `--set-by`, so "just pick" answers are recorded as `chosen` unless the model first runs separate `set ... --set-by delegated` calls. Neither zoom.md nor SKILL.md says so | 2 | `sketch --delegated feel,brand` (names the flags that were delegated), or document the pre-`set` pattern in zoom.md level 0 | engine.py `cmd_sketch` (l. 4923); `skills/opendesigner/references/zoom.md` |
| F6 | Sketch feel words | zoom.md offers "bold or quiet", but `sketch --feel ...,quiet` exits with `Unknown feel word ['quiet']` after it has already written audience and platforms | 2 | Alias `quiet` to `deferential` and check the feel words before any `set`; or change zoom.md to the engine's word | engine.py `cmd_sketch` (l. 4934); zoom.md l. 22 |
| F7 | Wiring | The export skill says to import only `theme.css`, but it needs `tokens.css`. Following the table literally compiles with 0 errors and leaves 61 `var(--ds-*)` references undefined, so the UI renders unstyled. The usage comment's paths only work from `build/tailwind/` | 2 | Emit `@import "../css/tokens.css";` at the top of `theme.css`, so one import is enough. Change the table to show the line from `src/` (`@import "../opendesigner/build/tailwind/theme.css";`) | `skills/opendesigner-export/SKILL.md` l. 31; engine.py `export_tailwind` (l. 3217) |
| F8 | Tailwind export | The default theme is not reset. `text-lg` (18 px, not in the scale), `rounded` (4 px against a 2 px control radius) and `bg-blue-600` still compile beside the tokens, and review can't see them (F3) | 2 | An export option (default on for new projects) that adds `--color-*: initial; --text-*: initial; --radius-*: initial; --shadow-*: initial;` inside `@theme` | engine.py `export_tailwind` |
| F9 | Review fixes | Fix suggestions go by nearest color and ignore the role: primary button bg #2563eb to `bg-info-bold`, button text #fff to `icon-on-accent`, hover link text to `border-info`, a 250 ms hover transition to `duration.long-exit` | 2 | Narrow the candidates by property first (background: `bg.*`/`surface.*`; color: `text.*`; border: `border.*`; transition on `:hover`: `transition.feedback`), then take the nearest | engine.py `_nearest_color` (l. 4979) and review loop |
| F10 | PRODUCT.md / DESIGN.md | "Audience: Not recorded yet (Q-aud-01)" even though D-0006 recorded Q-aud-01 = dense | 2 | Fall back to the label of `answers.Q-aud-01` when `context.audience` is empty | engine.py l. 3988, l. 4286 |
| F11 | Share ask (M5) | The 7-line share block must come in the message right after the result. It landed while Arjun was waiting for wiring and cost one message before M6 | 2 | When `speed_mode` is logged, defer the share ask to Finish step 7 | `skills/opendesigner/references/rules.md` l. 148; SKILL.md journey section |
| F12 | Extend: tweak | `set space.inset.md 12` writes a bare `12` (not DTCG `{value, unit}`) into all three density files, which flattens density | 2 | Coerce to a DTCG dimension, and patch only the named mode (`compact:space.inset.md`) or the default density | engine.py `apply_token_overrides` |
| F13 | Data table | There is no table question and no table tokens (row height, header surface, striping, numeric alignment), yet DESIGN.md lists table as "planned (tokens ready)". The rows reused `size.control.md` | 2 | Add a level-2 table question for Operate surfaces, plus component-tier tokens (`table.row.height` per density, `table.header.bg`) | `synthesis/QUESTIONNAIRE.md` (then `build_questionnaire.py`); engine |
| F14 | DESIGN.md for engineers | No role-to-class map, so the engineer has to read `theme.css` to learn `text-fg-*`, `border-line-*` and `h-size-control-md` | 2 | When a Tailwind export exists, add a "Tailwind" line to Colors, Layout, Shapes and Elevation | engine.py `render_design_md` |
| F15 | Tailwind names | Doubled prefixes: `size-size-icon-sm`, `h-size-control-md`, `w-size-control-md`, `accent-accent-bold` | 1 | Drop the `size-` in spacing keys (`--spacing-control-md` gives `h-control-md`) | engine.py `export_tailwind` |
| F16 | Validate / Open Items | All 14 designer-asset hooks show as pending for an internal tool with no brand (sonic logo, haptics, photography...) | 1 | Mark hooks not applicable when surfaces are Operate-only and no brand is given, or offer one bulk "not needed" command | engine.py hooks |
| F17 | AGENTS snippet | `<opendesigner skill>` is left as a placeholder, so the model must fill in a machine-specific path | 1 | `engine.py agents-snippet`, which prints the snippet with the real engine path | `skills/opendesigner/assets/output/AGENTS-snippet.md` l. 11 |
| F18 | Finish step 2 | "Show coverage in one line", but `validate --json` stats.coverage is `None` | 1 | Fill coverage from answers, defaults and n/a | engine.py ~l. 2476 |
| F19 | Journey report | Delegated counts as "default kept", so the report says for Q-brand-01/Q-color-01 "keep asking, with the default as a one-tap yes", which is backwards after "just pick". The sketch's "What are you making?" is labelled with Q-scope-01's scope wording | 1 | Separate delegated from kept default in the speed-up rules; give the sketch Q1 its own label | `skills/opendesigner/scripts/journey.py` |
| F20 | pick | `pick Q-type-01 open-source` (not an option) is accepted silently | 1 | Warn "not a listed option; recorded as custom" | engine.py `cmd_set` |
| F21 | Validate note | "Give it a 44px tap area" on a desktop-only web product (the CSS itself correctly uses 24 px under `pointer: fine`) | 1 | Word the note by platform | engine.py validate |
| F22 | Glossary | "density" (code `semantic.density.*`) and "Density" (code `density: compact, ...`) are two entries with different code names | 1 | Merge them | `synthesis/glossary.json` |
| F23 | Zoom lines | Overview shows "defined (2 of 3)" after a sketch plus delegated macros | 1 | Count delegated sketch answers as sketch level | engine.py zoom inference |
| F24 | Greeting | A 3-line cap, but the first message must hold the intro, the "found" line and the log question | 1 | Allow 4 lines when the repo was read | rules.md section 1 |

**Counts:** severity 3: 3 · severity 2: 11 · severity 1: 10 (24 in total).

## What worked
- **Look before you ask** found the stack, the hex values and the existing button blue, so the seed was reused instead of asked for.
- **Speed:** `sketch` builds tokens, all 7 exports, DESIGN.md, PRODUCT.md and the preview in 0.2 s. With no errors and 0 warnings, the export exists at message 4.
- **Tailwind v4 `@theme inline`** points utilities at CSS variables, so light/dark, density and reduced motion keep working through `data-*` attributes and media queries. `transition-feedback` is a nice `@utility`.
- **Honest records:** delegated answers show up in DESIGN.md Open Items; decisions carry who set them and why; the colors section explains why the button fill is not the exact brand hex.
- **Extend flow:** the start-up routine (read, then `review` first, then a 3-line status) is right for an engineer. The table was built from existing tokens only, and review plus the DESIGN.md re-read closed the loop.
- **Privacy:** the log question was asked word for word, logging was quiet, "don't share" held everywhere, and the anonymous report is clean. `feedback` saved locally and printed a pre-filled issue link without posting.

## Journey report (`journey.py report`, end of the extend session)
```
2 sessions, 7 min in total. 8 steps taken: 8 answered, 0 skipped, 0 dropped.
Shortest path for what was covered: 7 steps, one per question; you took 8 (88% efficient).
Most frustrating: Q-pattern-02 (How should long lists load: in pages, with a...), 1 signal.
Top speed-up: Q-pattern-02: default kept 1 of 1 times and low impact: auto-apply it and mention it in one line.
```
| Level | Reached | Answered | Finished | Steps taken / shortest |
|---|---|---|---|---|
| sketch | 6 | 6 | yes | 6 / 5 (83%) |
| defined | 1 | 1 | no | 1 / 1 |
| detailed | 1 | 1 | no | 1 / 1 |

Frustration hotspots: Q-scope-01 (just_do_it 1) and Q-pattern-02 (just_do_it 1). Help: Q-aud-01 (voice_switch 1). How answers were given: delegated 3, option 3, free 2. Errors 0, exports 2, reviews 4, feedback notes 2, asked to go faster 2. The log can't see the 2 extra messages caused by F1 and F4, because the engine thought everything had worked.

## Review output
Before the fixes (the extend start-up, and again after the table was built):
```
Review of .../arjun-admin: 9 files scanned.
8 hard-coded values skip the tokens: 6 colors, 1 duration, 1 shadow.
  src/components/Sidebar.jsx:3  #1f2937  ->  use var(--ds-color-bg-inverse) (closest match)
  src/components/Sidebar.jsx:5  #60a5fa  ->  use var(--ds-color-border-info) (closest match)
  src/components/Sidebar.jsx:6  #60a5fa  ->  use var(--ds-color-border-info) (closest match)
  src/components/UserForm.jsx:3  boxShadow: '0 4px 12px rgba(0,0,0,0.15)  ->  use var(--ds-elevation-floating)
  src/components/UserForm.jsx:6  #d1d5db  ->  use var(--ds-color-border-subtle)
  src/components/UserForm.jsx:7  #2563eb  ->  use var(--ds-color-bg-info-bold) (closest match)
  src/components/UserForm.jsx:7  #ffffff  ->  use var(--ds-color-icon-on-accent)
  src/components/UserForm.jsx:7  transition: 250ms  ->  use var(--ds-motion-duration-long-exit) (260ms, the closest step)
DESIGN.md matches state.json.
```
After the fixes: "No hard-coded colors, sizes, radii, shadows or durations found: the code uses the tokens. DESIGN.md matches state.json." `UserForm.jsx` line 3 also had `borderRadius: 10`, `padding: 20` and `background: '#ffffff'`: none were reported (F3).

## Top 5 fixes, in priority order
1. **Make every answer move the tokens, or say it didn't** (F1). Map Q-color-02, Q-color-03 and Q-dir-02 in `answer_effects`, and have `set`/`pick` warn when a Q-id has no effect. Today a person's explicit choice can be silently ignored. `engine.py`.
2. **Make `review` see React and Tailwind drift** (F3, with F9). Cover JSX camelCase and unitless values, Tailwind arbitrary values and default utilities, and a hex beside a shadow. Suggest tokens by role, not only by nearest color. Review is the consistency promise for the most common stack. `engine.py` review.
3. **Let extend add and tweak tokens for real** (F2, F12). A new path creates a token, or the command fails loudly. Overrides write valid DTCG and respect density modes. `engine.py apply_token_overrides`.
4. **A clean "just pick" path** (F4, F5, F11). Add `sketch --delegated`; keep a delegated brand seed visible (no monochrome wipe); defer the share ask to Finish when speed mode is on. This would have saved about 4 messages in this run. `engine.py`, `levers.json`, `rules.md`, `zoom.md`.
5. **A self-contained Tailwind export** (F7, F8, F14). Have `theme.css` import `tokens.css`; add an option to reset Tailwind's default scales; put the role-to-class names in DESIGN.md. Following the skill literally today gives an unstyled app with no error. `opendesigner-export/SKILL.md`, `engine.py export_tailwind`.
