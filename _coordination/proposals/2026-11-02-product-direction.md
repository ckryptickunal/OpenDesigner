# Product direction: what to change, in what order (2026-11-02)

This answers Kunal's notes from reading the repo map (`OWNER-FEEDBACK.md`, section "2026-11-02: reading the repo map", rows 1 to 16). It comes from a file-by-file audit of `skills/`, `site/`, `evals/` and `tools/` against each note. Every proposed change names the files it touches. Nothing here is built yet unless the "Done" section says so.

## Done in this session (not committed)

- **Six document counts corrected** (row 16): review cases 65 to 69 (review `SKILL.md` and `docs/SPEC.md`), the `artifact` export format added to the export skill and its table, style-lab axes 12 to 15, "all eight skills" link to `improve.md` (preflight now links it too), the library split 38 work / 44 consumer in `AGENTS.md`, the `llms.txt` status line, and the brand README's showcase count. Generated copies synced; every `--check` passes.
- **Real signals recorded** (row 14): 59 stars and 4 forks on 2026-11-02 (12 stars on 2026-10-27), and the unprompted Reddit reply, in `docs/FIELD-PLAN.md` and `docs/GITHUB-SETTINGS.md`.
- **Evals page reworked, local only** (row 12): see "Evals" below. Built and checked (`check.py` clean, `check_layout.py` 0 errors at 13 widths on `/docs/evals/` and `/`). Not pushed: a push deploys the public site.

## The shape: two paths, one engine

People arrive with one of two wants, and the router should tell them apart from their words and their repo, not by asking.

| | **Fix** (it exists, make it right) | **Build** (make a system end to end) |
|---|---|---|
| Who | Someone with a built product who wants it to "just work" | Someone starting out, or ready to invest in a full system |
| First step | Read the code, then an element-by-element audit: every CTA, type family, weight, size and colour, with what each breaks | Read the repo, confirm the alignment (mission, vision, purpose, goals), then the 5-question sketch |
| Research | The practices each finding breaks, with sources | Market, competitors, the analogous product, industry UX and copy conventions |
| Shown as | The real page with the audit drawn on it, then the fix beside it | The overview page, then each choice visually |
| Ends with | Fixes rolled out after a yes, a system extracted from what was kept | Tokens, exports, `DESIGN.md`, `PRODUCT.md` |
| Quick path | The component library, when they want speed | The component library, when they want speed |

Both paths share the engine, the accessibility floors, the decision log and the checks. The project's **phase** (idea, building, near launch, live) decides which questions come first in either path. "Phase" is used because "stage" already means an interview topic.

## Wave 1: small changes with the most effect (one session each)

Note: PR #60, merged on 2026-10-26, added a user research step after the sketch (`skills/opendesigner/references/research.md`, `engine.py research plan|add`, `opendesigner/research/users.json`). Items 3 and 10 build on it rather than beside it.

| # | Change | Rows | Files |
|---|---|---|---|
| 1 | **Element-by-element audit for the Fix path.** A checklist by element: CTAs (primary actions per view, hierarchy, verb-first labels, size), type (families, weights, sizes, roles, smallest size), colour (distinct values, accents, contrast, meaning), spacing, radius, states. Each finding gets the measured value, what is wrong, the practice it breaks with a source (house standard id, WCAG, preflight check, `making.md` row) and the fix. Add the checks `review.py` can measure without a system: primary buttons per view, distinct families, weights and colours. | 1, 9 | new `skills/opendesigner/references/audit.md`; `SKILL.md` fast path step 1; `opendesigner-review/scripts/review.py` |
| 2 | **Infer first, ask last.** At `init` and `sketch`, read what the repo already says: product name and description (`package.json`, README, page title), platforms (`expo`, `react-native`, `electron`, `tauri`, `ios/`, `android/`, `pubspec.yaml`), a brand colour candidate (`css_scan.py` on their CSS), the font (`@font-face`, `next/font`), dark mode (`prefers-color-scheme`). Record each as `assumed` and turn the matching sketch question into one confirm line. Fix the contradiction where `rules.md` says owner inputs are always asked while `zoom.md` allows `assumed`. | 3 | `engine.py` (extend `record_stack` into a `detect_project` step); `references/zoom.md`; `references/rules.md` |
| 3 | **An alignment record.** `PRODUCT.md` gains "Purpose and goals" (mission, vision, purpose, goals) and "Market" (analogous product, competitors, their pattern and the gap, industry conventions). The first result adds one line: "What I understood you're trying to do", inferred and confirmed once. Principles are drafted from the goals, not only from the sliders. | 3, 10 | `engine.py` `render_product_md`; `references/zoom.md` "The first result"; `synthesis/questionnaire.json` (Q-brand-07 default), then `build_data.py` |
| 4 | **Project phase.** A new question, idea / building / near launch / live, inferred first (no code: idea; code without deploy config: building; a changelog or version 1+: live). A table in `zoom.md` maps each phase to its first questions: idea gets alignment and the analogous product; near launch gets the audit, copy and preflight; live gets the audit and governance. | 6 | `synthesis/questionnaire.json` (new Q-scope-07), then `build_data.py`; `references/zoom.md` |
| 5 | **The library as the quick path.** Offer it when the person signals speed ("just build it", delegated answers, a logged speed mode), not because they are new. Otherwise settle the component base and states first and mention the library only when asked. | 7 | `references/library.md`, `SKILL.md` |
| 6 | **Name the source of every suggestion.** Every option or fix on a built page says where it came from in one line (a shipped product, a house standard, a review case, or "my own idea") and ends with "keep the fix, keep today's, or try another?". `review.py compare` marks get a `source` field. | 9 | `references/rules.md` section 1; `review.py`; the handoff table in house standard STD-process-review-taste-48 (needs your OK: it is a house standard) |
| 7 | **Ask for an example at the second miss.** After a second failed try at the same note, ask for one example: a screenshot with the spot circled, a link that does it right, or a snippet. Motion the person shares is split into frames (`preflight.py frames`), timed, rebuilt on a review page and compared frame by frame. | 11 | `references/making.md` section 10; `opendesigner-extract/SKILL.md` |

## Wave 2: medium changes

| # | Change | Rows | Files |
|---|---|---|---|
| 8 | **Repeated problems become issues.** `engine.py feedback` matches entries by area and wording and adds "Seen: N (dates)". At 3, the agent offers to file a GitHub issue (the person still says yes; the command is shown first). New labels `recurring` and `needs-research`, a "Times seen" field in the issue template, and a research-first step in `improve.md` before any fix. | 5 | `engine.py` feedback; `references/improve.md`; `.github/ISSUE_TEMPLATE/`, `.github/labels.yml` |
| 9 | **Audits at three points.** The extend skill and the AGENTS.md snippet add the rendered review, the post-change audit and the scorecard to "end of every implementation" (today they only ask for `engine.py review`). A third repeat of the same note becomes a durable check with `engine.py standard add --review-pattern`. Split the post-change audit's section B into "every project" and "OpenDesigner's own site". | 2 | `opendesigner-extend/SKILL.md` section 5; `assets/output/AGENTS-snippet.md`; `references/making.md`; `references/post-change-audit.md` |
| 10 | **Copy and voice research per industry.** A practices section, "Industry words and tone": read the person's own copy and, with consent, competitor and analogous-product pages; draft tone traits and a word list the industry uses, each line sourced and `assumed` until confirmed. It becomes the default for the voice questions. | 10 | `references/practices.md`; `synthesis/questionnaire.json` (Q-voice-01, Q-voice-06), then `build_data.py` |
| 11 | **Lessons kept per project and across projects.** `review.py report` adds one dated line per run to `opendesigner/review/HISTORY.md` instead of only overwriting `REPORT.md`. A global lessons file on the person's machine waits on your decision below. | 4 | `review.py`; `docs/GLOBAL-LOCAL-PREFERENCES.md` |

## Wave 3: the website and proof

| # | Change | Rows | Files |
|---|---|---|---|
| 12 | **A "How OpenDesigner works" page** on opendesigner.dev, linked from the home page: the repo map rewritten for visitors (the two paths, what you get, how it learns), live HTML, light theme, in the site's own system. | 8 | `site/build.py`, new `site/docs/` page or figure, home section 05 link |
| 13 | **A fresh full agent run.** All 12 tasks, 3 tries per side, after fixing why the skill doesn't start for the taste question. Then the page shows one current full run instead of a mix of dates. Costs model usage on your account (the last full run of 8 tasks was about $5.48). | 12 | `tools/agent_evals.py`, `evals/agent/results/` |
| 14 | **The field plan's first gate.** Five people install it and reach a usable preview without help, watched. Stars and the Reddit reply show interest; this shows use. | 14 | `docs/FIELD-PLAN.md` |
| 15 | **Study the package and use steps on our own projects.** Run the Fix path on opendesigner.dev and the other projects built with OpenDesigner. Log each question the repo could have answered, each repeated note and each fix that went off the system in `_coordination/TRIAL-LEDGER.md`, and feed them into rows 2, 5 and 9. | 15 | `_coordination/TRIAL-LEDGER.md` |

## Safety net, self-healing and the human in the loop (row 13)

- **Run the checks without CI.** GitHub Actions is off for the account, so the "Before you commit" checks run only when someone remembers. Run them in a pre-push hook or as the first step of `site/autodeploy.py`.
- **Counts that fix themselves.** `tools/doc_counts.py --check | --fix` reads counts from the JSON files (review cases, preflight checks, sources, components, questions) and corrects the documents that quote them. That would have caught all six drifts.
- **Three places an agent can act before a yes**, against the rule that fixes to existing code wait for one:
  - the main skill's fast path fixes one page before asking (put the fix on a review copy instead);
  - extend applies newer house standards after a one-line notice (make it one question);
  - `illustrate apply` and `paint ingest` write into the person's source folder without asking at that step (ask first).

## Evals: what they are and what the page now shows (row 12)

An eval is a fixed task with fixed checks and a saved result that answers a question someone asks before trusting the tool. The audit found four reasons to be skeptical of the old page:

1. Its headline, 91% with OpenDesigner against 58% without, averaged in a task a plain AI cannot do by design (changing one decision and rebuilding needs OpenDesigner's engine).
2. It showed one run from 20 October. A weaker first run the same day, from the same commit, was not shown, and what changed between them was not recorded.
3. Later single runs were not shown, including two taste tasks that scored 0% with the plugin, while the page said "when a test fails, it says so here".
4. Its limits came last, after every number.

The reworked page (local, not pushed):

- Opens with what an eval is, then four results in the order a visitor asks: compared with a plain AI (92% with, 66% without, on the 7 tasks any AI can attempt, 3 tries per side), accessible and complete (162 of 162 required checks), looks judged blind, and our own checkers.
- Puts "What these numbers don't show yet" second: nobody watched yet, one AI tool, small samples, the two checks we changed on 23 October, AI judges.
- Lists every task with its headline run, every other run under it, and single runs marked as weak evidence.
- Keeps the jobs that need OpenDesigner's files (extend, the taste tasks) in their own table, out of the comparison, with the taste failures stated.

Files: `site/evals_html.py` (reads every file in `evals/agent/results/`; the list of tool-only tasks is `NEEDS_TOOLS`), `site/docs/evals.md`. The home page's "Tested in the open" section uses the same summary, so it changed too.

## Decisions only you can make

1. **Push the evals page?** A push to `main` deploys the public site.
2. **Global lessons:** may OpenDesigner keep a lessons file on the person's machine (outside their project), and is it on by default or only after a yes? (`docs/GLOBAL-LOCAL-PREFERENCES.md` leaves this open.)
3. **Filing issues:** at 3 repeats, should the agent offer to file each issue with a yes, or only draft it for the person to file?
4. **House standard change:** add a "From" column to the review handoff table (STD-process-review-taste-48)?
5. **Spend:** run the full agent evals again after the taste fix? Judging by the last full run (8 tasks for about $5.48), all 12 would cost roughly $8 of model usage.
6. **Order:** start with Wave 1 items 1 to 3 (Fix-path audit, infer first, alignment record), or another order?
