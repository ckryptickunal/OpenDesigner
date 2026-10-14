# Repo audit, 2026-10-04: what is broken and how to fix it

Read-only audit of the whole repository: the decision trail (`_coordination/`, DECISIONS, sessions, inbox), test and CI trail, the engine against its documents, the knowledge pipeline (learning wiki, synthesis, standards), and packaging for each host. Five audit agents worked in parallel. A sixth, fresh-context agent then tried to refute the 15 most important claims, and I re-ran four more myself. Nothing in the repo was changed while auditing; scratch work lives outside the repo.

**Verification key:** **V** = re-verified independently (by the verifier agent or by me). **A** = verified by the one audit agent that found it, not re-checked. **I** = inferred from reading, not run. "HEAD" means committed (78dc59f); "uncommitted" means another session's work in the tree.

## The short version

Every test and check passes (118 engine tests, about 300 tests in all, every `--check` tool). The breakage is in four places the tests do not look:

1. **The engine sometimes breaks its own promises to the person.** It silently replaces answers they chose, recommends options its own standards forbid, and skips contrast checks on colors added later. Its documents also claim checks it does not run.
2. **Users cannot get what has been built.** The plugin version is pinned, three commits were never pushed, the claude.ai instructions upload one zip of five to seven, and the standalone zips and the ChatGPT bundle lose the house standards.
3. **The safety net has never been switched on.** GitHub Actions has never run once, and CI skips one of the main drift checks.
4. **Rules documents and coordination have drifted.** Exceptions are recorded in some places only, counts are stale, the orchestrator role is vacant, and three uncommitted workstreams wait on your rulings.

## How the talk shaped the ranking (no repo changes from it)

The talk (Gus Iwanaga, "The End of the Static Screen", AI Engineer, September 2026) argues three things. Once AI agents assemble interfaces, the design system and component catalog become the contract between the agent and the UI, and every property in it matters. Full model autonomy produces output nobody can ship: the same request gave "Q1" one turn and "January to March" the next. Teams therefore have to codify what good looks like as rules, so the result is consistent every time.

OpenDesigner is that contract-making step: decisions recorded with their reasons, locked values, house standards, DESIGN.md. So I ranked highest the findings that make the contract unreliable: an engine that silently changes recorded choices, rules that contradict each other, documents that claim checks that do not happen, and examples that no longer reproduce. I am not proposing any change based on the talk. The one place its ideas would bear is the open question already in `docs/SPEC.md` ("Component code": stop at tokens and specs, or generate components). That is yours to decide when you choose to.

---

## A. Broken, in order of impact

### A1. The engine and the person's recorded decisions

1. **`engine.py standards --update` silently replaces answers the person chose.** V, HEAD.
   - **What happens:** on a copy of `examples/public-service-accessible`, the update changed `raw.reducedMotion` from the chosen "remove" to "replace". The change is one line out of 320, with no conflict notice. `state.json` still records Q-motion-07 = remove (chosen), and DESIGN.md now contradicts itself: line 456 says "replace" and line 478 says "remove (chosen)". `validate` passes.
   - **Why it's wrong:** `docs/KNOWLEDGE.md` section 2 ranks the person's explicit choice above house standards, and the extend skill tells agents to run this command.
   - **The bug:** it is not that "remove" is refused for new picks (it should be). It is that an answer given before the standard existed is not treated as the person's override.
   - **Fix:** in `cmd_standards`, check each standard against chosen or confirmed answers on the same path, the questions it settles, and the options it breaks before applying it. Report the conflicts. The policy for what happens next is decision D1.

2. **Shipped defaults recommend options that house standards mark as breaking, and no check catches it.** V, HEAD.
   - Q-motion-02 has `default_value` "6-steps", which breaks STD-easing-duration-06 and -07.
   - The Q-motion-06 default includes `fade` and `fade-through`, which break STD-enter-exit-origin-02 and STD-when-to-animate-05 and -14.
   - The Q-depth-04 web default is "opaque", which breaks STD-visual-details-16.
   - **Check gap:** `wiki.py` (lines 676-686) only checks that option names exist, and `build_data.py` (lines 175-187) only marks options.
   - **Fix:** reword the Q-motion-02 and -06 defaults in `synthesis/` (cards DC-L19-86 and -90 already propose this), and add a check that fails when a default is in `breaks_options`. Q-depth-04 waits on D2.

3. **Colors added later through extend are never contrast-checked.** V, HEAD.
   - **What happens:** `contrast_pairs` (`engine.py` lines 2174-2205) is a fixed list. A new `color.bg.highlight` of #111111 with text #141414 builds with 0 errors.
   - **Contradiction:** the extend skill says added colors "still have to pass contrast".
   - **Fix:** derive pairs for any added `color.bg.*` / `color.text.*` (and `border`/`icon` against surfaces) tokens.

4. **Guardrails section 4 says `validate` checks the accessibility floors. It checks some.** V, HEAD.
   - **Checked:** text contrast (4.5:1, or 7:1 under AAA, with no rounding up), input and focus colors at 3:1, pointer and touch targets, density never shrinking hit areas, a focus ring of at least 2 px, and that reduced motion exists.
   - **Not checked:**
     - The focus offset. The offered option Q-state-03 "inset" sets it to -2 px and passes, while DESIGN.md says "2px offset".
     - `size.target.min`. It is missing from the floor list (`engine.py` around line 3032), so it can go below 24px, though only after an explicit override.
     - Text scaling to 200%, color as the only signal, labels, dismissable dialogs, pre-checked consent and flashing.
   - **Fix:** add `min` to the floor list, and rewrite the guardrail's last line to say exactly what `validate` checks and which skill reviews the rest. The focus offset is decision D4.

5. **With no brand color, the accent is grey while DESIGN.md says blue.** V (I re-ran it), HEAD.
   - **What happens:** `sketch --feel serious,minimal --delegated` gives accent `#757575`, so links and the focus ring are grey too. DESIGN.md line 28 says "a stand-in blue is used".
   - **Fix:** the text and the engine have to agree. Which way is decision D5.

6. **The "regular" audience gives 14 px body text, while the stage file promises 16 px.** V (I re-ran it), HEAD.
   - **Cause:** the product type defaults to "work-tool" (`engine.py` line 712). Stage 02 says regular means "body 16px".
   - This is decision D6.

7. **The palette template's contrast table is always empty (issue #47, still open).** V (I re-ran it), HEAD.
   - **Cause:** `engine.py show palette --json` has no `pairs` key, and the template renders `D.pairs`. People never see contrast while they choose colors.
   - **Fix:** add `contrast_pairs()` results to the payload in `build_payload`.

8. **Silent mistakes when setting values.** V, HEAD.
   - `set dials.roundnes 30` (a typo) is stored as a new dial and reported as done. The real dial is unchanged.
   - `pick Q-shape-01 rounded` follows the question text, but the option ids are square/subtle/soft/pill. The engine does warn, but the wording invites the mistake.
   - Unknown question ids (`set Q-zz-99`) are stored without complaint. A.
   - **Fix:** reject dial names not in `levers.json`, warn on unknown question ids, and make the Q-shape-01 wording use the option names.

9. **The voice section cites the wrong question.** V, HEAD.
   - **What happens:** `engine.py` line 8247 writes "Word list: not recorded yet (Q-voice-03)". Q-voice-03 is about capitalization; the word list is Q-voice-06.
   - **Fix:** the fix already exists on `origin/docs/voice-wordlist-id` (bc58d9b), with no PR. Open the PR and merge it.

10. **The engine contradicts some "must" standards.** A (from reading code), HEAD.
    - Q-motion-01 "none" sets feedback, enter and exit to 0ms, against STD-mobile-touch-05 and STD-accessibility-motion-02 ("never zero"). Yet Q-motion-07 "remove", which has the same effect, is refused.
    - The Swift export has no `nonisolated`, against STD-swift-17, -18 and -44. Its effect in Xcode 26 is I.
    - Toasts share the enter transition, and `move` uses a spatial spring.
    - In all, 48 standards carry conflict notes naming `engine.py`.
    - **Fix:** engine changes with tests, which `learn/IMPROVING.md` allows an agent to make. The no-motion posture is decision D3.

11. **The examples no longer reproduce and are 289 house standards behind.** V, HEAD.
    - **What happens:** `make_examples.py` is refused at two picks and deletes generated files in two examples. Their `tokens/` and `build/` are stale on motion values.
    - **Fix:** settle D1-D3 first. Then regenerate the examples in a commit of their own, and add the regenerate-in-a-temp-copy-and-diff check that issue #51 asks for. Until then, regenerate only `preview.html` with `engine.py preview`.

### A2. Users cannot get or run what has been built

12. **The plugin version is pinned, so installed users never get updates.** V, HEAD.
    - **Evidence:** both `plugin.json` files have said `"version": "0.1.0"` since c7f3da6. The Claude Code plugin docs say a set version keeps users on that version until you change it. Early installs therefore lack illustrate and will never get review or paint.
    - The skills' own versions disagree too: paint says 0.2.0 and the rest 0.1.0.
    - **Fix:** a release policy (decision D7), plus a CI check that the versions agree.

13. **Local `main` is three commits ahead of GitHub.** V.
    - **What's missing:** bcfc2c4 (illustrate), 7cc83c9 (its network exception) and 78dc59f (the preview fix). The public repo has lacked the illustrate skill since 28 September.
    - **Fix:** push them. This is your call (D8).

14. **The claude.ai install steps upload one zip, but the router needs all of them.** V, HEAD.
    - **Evidence:** README line 31, AGENTS.md line 74 and the FAQ say to upload `dist/opendesigner.zip`. `build_dist.py` writes 5 zips at HEAD and 7 in the working tree, and the router hands off to the others.
    - **Fix:** document uploading every zip, and correct the "four helper skills" comment.

15. **The standalone sub-skill zips drop the house standards and other files the skills read.** V, HEAD.
    - **Evidence:** `BUNDLE` in `tools/build_dist.py` has no `references/standards.json`. From an extend, export or extract zip, `engine.py standards` reports "No house standards ship with this skill". New systems get 390 tokens instead of 420, and `standards --update` finds nothing.
    - **Also missing:** guardrails, hooks, the stage files, the cards and `AGENTS-snippet.md`. A.
    - **Fix:** add them to `BUNDLE` and assert them in `tools/test_build_dist.py`.

16. **The ChatGPT bundle loses the standards and points at things it can't run.** A, HEAD.
    - **Standards:** `01-protocol.md` contains the full standards and says `init` locks them. But `04-lookup.json` has no standards key, and the setup snippet writes only `levers.json` and `hooks.json`.
    - **Unrunnable references:** the protocol names `engine.py show`, five skills, `taste.py` and `show.py`, none of which exist in a ChatGPT Project.
    - **Fix:** have `build_data.py` put standards in the lookup file, have the setup write out standards, questions and glossary, and strip host-only sections from the ChatGPT build.

### A3. The safety net has never run

17. **GitHub Actions has never run for this repo.** V.
    - **Evidence:** both workflows are active and Actions is enabled, yet there are 0 runs ever, although many PRs have been merged (the latest is #46).
    - **Misleading docs:** README line 14 shows a CI badge, and CONTRIBUTING line 97 says CI runs on every PR.
    - **Cause:** I. `docs/GITHUB-SETTINGS.md` blames an account-level block.
    - **Fix:** you check the account's Actions and billing settings (D8). Then require CI on `main`.

18. **CI skips `build_data.py --check`, and `jev_nav.py check` never fails.** V for `jev_nav` (I read the code); A for `build_data`, HEAD.
    - **build_data:** a changed glossary entry in `synthesis/` would pass CI while the shipped copies go stale.
    - **jev_nav:** it prints the dangling count but always exits 0. Only an error from the remote API ends it with a failure.
    - **Fix:** add the step to CI, and exit 1 when the dangling count or the stale conflict-quote count is above 0.

19. **Three lists of "checks to run" disagree.** A, HEAD.
    - **The lists:** AGENTS.md "Before you commit" (which leaves out every skill test, `test_engine.py` included), CONTRIBUTING lines 74-95, and `ci.yml`.
    - **Fix:** one script (for example `tools/check_all.py`) that CI and both documents call.

20. **Security settings on a public repo.** V (live API).
    - **What's off:** secret scanning, push protection and Dependabot security updates are all disabled.
    - **Doc error:** `docs/GITHUB-SETTINGS.md` line 8 says private vulnerability reporting is off. It is on.
    - **Fix:** you switch them on (D8), and the document gets corrected.

### A4. The rules documents disagree with each other

21. **Network and standard-library exceptions are recorded in some places only.** V/A.
    - **Not yet updated for illustrate:** CONTRIBUTING line 29, the od-pr-review rules row (`SKILL.md` line 74), `skills/opendesigner/references/guardrails.md` section 6, and the FAQ privacy answer. Users' models read the guardrails file.
    - **Not listed anywhere:** `journey.py share` sends with `urllib` when a reports URL is configured. PRIVACY.md documents it, but no "no network" statement lists it. No address ships, so nothing leaks; it is a gap in the documents, not a leak.
    - **Fix:** one list of exceptions, written into all of those places. Journey sharing needs your yes (D9).

22. **AGENTS.md says `engine.py review` validates and refreshes DESIGN.md. It does neither.** V.
    - **What happens:** with 9 validation errors, `review` exited 0 and named none of them. It does detect that DESIGN.md is stale, but leaves it unchanged.
    - **Fix:** correct the AGENTS.md line, or make `review` run validation.

23. **Stale counts.** V/A.

    | Where | Says | Actual |
    |---|---|---|
    | README line 223 | 25 engine tests | 118 |
    | README, FAQ, SPEC | 352 Decision Cards | 527 |
    | AGENTS.md | 271 building blocks | 275 |
    | FAQ | 192 questions | 193 |
    | README | 397 glossary terms | 399 |
    | README | 39 illustration tests | 40 |
    | FIELD-PLAN smoke test | 408 tokens, no errors | 420 tokens, 1 warning |
    | `docs/SPEC.md` | 14 JSON-fed templates | 8; the six added by DECISIONS line 39 were never built (D14) |
    | README, llms.txt, REPO-PLAN | four skills | five at HEAD, seven in the tree |

    These are correct: 193 questions with 6 planned, 28 stage files, 65 review cases, 44 sources, 8 dials, 14 hooks.

24. **The quote limit and the standards evidence disagree.** V, HEAD.
    - **The rule:** KNOWLEDGE.md line 96 allows "at most 3 short quotes per source".
    - **The data:** `synthesis/standards.json` commits 1,130 evidence strings, 411 of them over 15 words; 37 of the 45 sources have more than 3. Some are section headings, but `wiki.py` treats evidence as verbatim.
    - This is a licence question (D13).

25. **Coordination has gone stale.** V/A, HEAD.
    - The orchestrator's last heartbeat was 24 September, yet CLAUDE.md still routes sessions to it (D15).
    - BOARD still shows L19 as claimed. L20's numbers are wrong: it says 253/75, the real figures are 172 pending cards and 86 conflicts.
    - `wiki.py next` says "everything is up to date" while 172 cards wait.
    - 17 inbox messages are unread, all addressed to finished sessions.
    - No lanes exist for illustrate, the preview fix, taste, paint or the playbook worktree.
    - The two SPEC copies diverge: the uncommitted `docs/SPEC.md` adds review, but the source `synthesis/OPENDESIGNER-SPEC.md` does not.
    - **Fix:** refresh BOARD and the L20 lane file, and make `next` show the pending proposals. Edit the spec in `synthesis/` and copy it to docs.

### A5. Other sessions' uncommitted work (needs your rulings before it lands)

26. **Review skill (R5).**
    - **The ruling it waits for:** `capture.py` imports Playwright, `review.py serve` is a loopback server, and an `--allow-remote` flag contradicts "local URLs only" (D10).
    - **No route in:** no router row sends anyone to it, so "review my UI" never arrives.
    - **CI:** the uncommitted `ci.yml` calls the untracked skill folders, so committing it alone breaks CI. Three review tests also need `examples/devtool-dense`.
27. **Paint skill.**
    - **Crash:** `paint.py brief` crashes on a normal project, because unset dials are `None` (A).
    - **Provenance:** 16 "reconstructions of the original film" with no stated source (D11).
    - **Packaging:** no lockfile, and a version that differs from the other skills.
28. **Taste poll** (untouched since 29 September).
    - **Can't run for users:** it is offered to every user but needs Mobbin images that cannot ship.
    - **Self-contradiction:** it suggests publishing the images as an artifact, against its own rule.
    - **Network:** `taste.py add` downloads images (D12).
    - **Blocking:** its edits to the router SKILL.md block R5's router row.
29. **Stranded work.**
    - A transition-token fix with a test sits uncommitted in the worktree `.claude/worktrees/awesome-engelbart-3aa213`; main still lacks it.
    - The worktree `.worktrees/living-2026-09-29` is empty.
    - `_coordination/AGENT-REVIEW-BEFORE-MERGE.md` is superseded but still present (D17).

---

## B. Decisions only you can make

Answer the first group first; the rest can wait.

**Blocking**

| # | Question | Options | My recommendation |
|---|---|---|---|
| D1 | A new house standard conflicts with an answer the person gave before it existed. What should `standards --update` do? | (a) Keep their answer as a recorded override and say so. (b) Stop and ask. | (a). Their choice outranks house standards (KNOWLEDGE.md section 2), and asking on every update would bury real questions. |
| D2 | Should STD-visual-details-24 mean "every mode you ship is fully mapped" instead of "you must ship light and dark"? And may a single-source "should" standard block an option at all? | (a) Reword it and allow light-only and dark-only again. (b) Adopt DC-L19-14 `light-first`. (c) Keep it. For "should": warn and record, or keep refusing. | (a). Light-only breaks no accessibility floor, and the research (DC-L07-15) warns that every extra mode multiplies testing. "Should" standards warn and record. |
| D3 | May a product choose no motion (Q-motion-01 none or Q-motion-07 remove)? | (a) Yes, as an explicit override recorded at pick. (b) No: keep a 100ms press and a cross-fade. | (a). No motion breaks no floor. Make `none` and `remove` behave the same way. |
| D7 | How do plugin users get updates? | (a) Bump `version` on every release. (b) Drop `version` so users follow main. | (a). Tag 0.2.0 now, because main carries unreleased work. |
| D8 | Owner-only switches. | Push the 3 commits; check why Actions never runs (account or billing); turn on secret scanning and push protection. | Do all three. They take minutes and unblock everything else. |
| D10 | Review skill: may `capture.py` (Playwright, never installed by the skill) and `review.py serve` (loopback) ship? Should `--allow-remote` stay? | (a) Both. (b) `capture.py` only. (c) `serve` only. (d) Neither. | (c), or (a) with `capture.py` moved out of `skills/` into `tools/`. Drop `--allow-remote`. |

**Soon**

| # | Question | My recommendation |
|---|---|---|
| D4 | Is the 2 px focus offset a floor, or a default that inset rings may skip if they keep 3:1? | A default. The floor is a visible ring of at least 2 px at 3:1. Then fix the DESIGN.md wording. |
| D5 | With no brand color, should the stand-in accent keep a minimum colorfulness? | Yes, so links and focus stay recognizable. |
| D6 | Should "regular" give 16 px body unless the person says it's a work tool? | Yes, as the stage file says. |
| D9 | Is the opt-in `journey.py share` upload an approved network exception? | Yes. List it with illustrate everywhere. |
| D11 | Paint: whose film are the 16 reconstructions and the demo? Keep or drop them? | Drop them unless the upstream author's licence is confirmed. |
| D12 | Taste poll: ship it to users, or keep it maintainer-only? May `taste.py add` download? | Maintainer-only until there is an image set you may re-host. |
| D13 | Standards evidence against the 3-quote rule. | Trim evidence to anchors of 15 words or fewer, and add a check. |
| D14 | The six planned templates (block-map, dial-board, and so on). | Mark them "planned" in SPEC now; build them later. |
| D15 | The orchestrator role. | Name a new session, or remove the role from CLAUDE.md, AGENTS.md and BOARD. |
| D16 | May CI install pinned third-party packages (OpenWiki, Playwright) in one optional job? | Yes, pinned and optional. |
| D17 | Stranded work: PR the voice branch, keep the worktree fix, delete the superseded file? | Yes to all three. |
| D18 | od-pr-review is hand-edited in `.claude/skills`. Document that, or give it a source folder? | Document it in REPO-PLAN. |

**Still open from earlier logs**
- D06: when to ask the journey-log consent question.
- D07: should exports cover only the recorded platforms?
- The "founder direction" section in `docs/GLOBAL-LOCAL-PREFERENCES.md`.
- Where the telemetry receiver is hosted.
- Narrowing issue #15.
- Two sponsorship verification rows.

## C. Suggested order of work

1. **You, minutes:** D8 (push, Actions, secret scanning). Then answer D1, D2, D3 and D7.
2. **Agent, no decision needed:**
   - The defaults-versus-standards check, plus the two default rewrites (A2).
   - Contrast pairs for added colors (A3) and in the palette payload (A7).
   - Rejecting typos and unknown ids (A8). Merging the voice fix (A9).
   - The `jev_nav` exit code, and `build_data --check` in CI (A18).
   - One shared check script (A19).
   - Honest wording for guardrails section 4 and AGENTS.md `review` (A4, A22).
   - Zip bundle contents and claude.ai install docs (A14, A15).
   - Stale counts (A23).
3. **After D1-D3:**
   - `standards --update` override handling (A1), and the STD-visual-details-24 rewrite with `wiki.py standards --bump`.
   - Engine fixes for "must" standards (A10).
   - Regenerating all three examples in their own commit, with a regenerate-and-diff check (A11).
4. **After D7:** version bumps, a version-agreement check, and the ChatGPT bundle (A12, A16).
5. **With the other sessions:** rulings D10-D12, then commit R5, paint and taste each as one unit, with their router rows, CI steps and lanes. Refresh BOARD and the L20 lane (A25).

## How this was checked

- **Tests:** all suites were run at HEAD (in a temporary worktree) and in the working tree, on Python 3.10, 3.11 and 3.13. All pass.
- **The engine, as a user:** run for three personas in scratch folders, never against the repo.
- **Verification:** a fresh-context agent tried to refute the 15 highest-impact claims. All held at their core, and six needed corrections to line numbers or severity, which this document already includes. I re-ran findings 5, 6, 7 and 18 myself.
- **Live GitHub facts** (runs, security settings, pushed commits) were read with `gh` read-only.
- **Not verified:** whether claude.ai lets one uploaded skill read a sibling skill's files, the Swift export's behavior in Xcode 26, and the cause of Actions never running.
