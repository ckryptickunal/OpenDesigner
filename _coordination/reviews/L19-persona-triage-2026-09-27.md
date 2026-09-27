**Triage of the OpenDesigner persona and retrieval findings**

The reports reduce to 54 distinct issues. 47 have a clear fix, 16 of them high severity. The other 7 need an owner decision, and 2 of those are high.
- **Checks:** every issue was re-run in a temporary copy of the engine or read in the cited file. No finding turned out to be false, so none were dropped.
- **Checked by reading code only:** R24, R25, R26, R27, R30, R33 and part of R45.
- **Not reproduced:** R42's Jev scores. I checked keyword ranks instead.
- **Two tester claims corrected:** see R02 and R13.
- **New evidence:** the sample data inside `assets/templates/motion.html` still has ease-in exits and an overshoot enter (see R10).
- **Repo state:** untouched (`git status` shows only the untracked `_coordination/AGENT-REVIEW-BEFORE-MERGE.md`), and the scratch folders are deleted.

Paths are relative to `/Users/Kunal/Desktop/Design-System`. "engine" means `skills/opendesigner/scripts/engine.py`. Line numbers are from commit a7cce09.

## Part A: fixes that need no product decision

### High

**R01 · engine, standards content**
- **What:** every new project shows a false standards warning about `dampingRatio` "1.0 vs 1".
- **Evidence:**
  - `_same` (line 4239) compares `json.dumps` text.
  - STD-springs-gestures-04 sets `1.0` and STD-mobile-touch-51 sets `1` on the same path.
  - Reproduced: init, then sketch web, gives `WARN ... sets motion.spring.spatial.dampingRatio to 1.0, but it is now 1`. It survives `standards --update`.
  - The suggested `restore` logs a needless decision.
- **Fix:**
  - Make `_same` compare numbers by value, recursively.
  - Change STD-mobile-touch-51's engine value to `1.0` and bump the standards version.
  - Have `wiki.py check_standards` flag two standards that set one path to different JSON values.

**R02 · engine**
- **What:** `init` applies all 455 standards before the platforms are known, and `sketch` never re-scopes them.
- **Evidence:**
  - The first sketch prints `NOTE 167 house standards no longer apply ... Run engine.py standards --update`.
  - DESIGN.md counts rules for platforms the project doesn't use (after the update, 288 for web).
  - `--update` prints 169 flat lines, not grouped by area.
  - SKILL.md, zoom.md and guardrails 4b never say to run it.
- **Fix:**
  - After Q-plat-01 is recorded (`cmd_sketch` at 7977, plus `pick`/`set` of Q-plat-01), call `std_sync(d, quiet=True)`.
  - Print one line of counts per theme.
  - Group `--update` output by theme with counts.
- **Correction:** tester 2's "still there after update" is right, but R01 is the cause.

**R03 · engine**
- **What:** a token silently disappears from every export when its standard is retired or stops applying to the platforms.
- **Evidence:**
  - After `standards --update` on web, `--ds-motion-gesture-sheet-dismiss-fraction` is gone, though `state.overrides` still holds 0.4.
  - `meta.json` says `override ... skipped: ... type of 0.4 is unclear`.
  - With an older standards file, `--ds-motion-scale-enter-tooltip` is dropped too.
  - `std_token_types` (2364) reads types only from live records.
- **Fix:**
  - When a record is released or retired (around 4745 and 4751), keep the standard snapshot and `$type`, or store the type with the override.
  - Turn every "override ... skipped" note into a validate WARN.

**R04 · engine**
- **What:** an older skill install downgrades a project and retires newer standards.
- **Evidence:**
  - With the project at v1 and a v0 file: validate says "2 standards ... left the house file".
  - `--update` then records `house standards v0 ... 2 retired`, `house_version` becomes 0, and the tooltip token is dropped.
  - `std_pending` (around 4688) treats ids missing from the file as retired. validate (5205) only handles hv > sv.
- **Fix:**
  - If the file version is below `state.standards.house_version`, release nothing.
  - validate should say "your OpenDesigner skill is older than this system (vX < vY); update the skill", and `--update` should refuse.

**R05 · engine, skill text**
- **What:** `set --force` bypasses a standard lock, and the extend skill tells agents to use it.
- **Evidence:**
  - `set motion.duration.modal 450 --force` writes `set_by: chosen · locked: no`, with no override recorded.
  - `set focus.ring.width 1 --force` also passes. Only `build` errors on it.
  - The lock check is in `cmd_set` (3898). opendesigner-extend/SKILL.md:56 recommends `--force`.
- **Fix:**
  - In `cmd_set`, when `std_holder(state, path)` exists, refuse even with `--force` and point to `standard override`.
  - Extend SKILL.md:56 should say "`--force` is for person locks, never standards".

**R06 · engine, standards content**
- **What:** the `set` blocker names the wrong standard or only one holder, and gives no reason. Rules that forbid a value aren't enforced.
- **Evidence:**
  - `set motion.easing.exit '[0.42,0,1,1]'` names STD-easing-duration-02. It doesn't name -03 ("Never use ease-in on UI") or -01.
  - `set motion.duration.modal 450` names only -11; -12 also holds the path.
  - After overriding -02, `build` passes with an ease-in exit while DESIGN.md still lists "Never use ease-in on UI", and `review` still flags it.
  - With an engineer project standard, only standards on the same token are caught.
  - `std_lock_message` is at 4462.
- **Fix:**
  - List every holder from `std_held`, each with its rule and why.
  - Add a `constraints` field to standards.json (for STD-03: `motion.easing.*` forbids accelerating curves).
  - Check constraints in `std_validate` (around 5189) and in the blocker.

**R07 · engine**
- **What:** an override releases every path the standard sets, marks untouched tokens as the person's, and makes the decision count drop.
- **Evidence:**
  - Override STD-02 prints `Unlocked: motion.easing.enter, motion.easing.exit, motion.easing.standard`.
  - With no `set` at all, enter and exit get `$extensions source: person` (line 2409), and `standard` loses `$extensions`.
  - `--value` is refused: "sets 3 values".
  - DESIGN.md went from "55 decisions" to "54" after three new decisions.
- **Fix:**
  - Add a repeatable `standard override <id> --path P [--value V]` that releases only those paths.
  - Record provenance as `{"source": "standard-overridden", "standard": sid}` until a `set`.
  - Count unique decision ids.
  - Note in SKILL.md (the override line, around 95) what gets released.

**R08 · engine**
- **What:** override and restore mishandle a path held by two standards. Restore takes no `--why`, and repeating it logs a second decision.
- **Evidence:**
  - Overrode -11 and -12, set 450, then restored -11. The token went back to 250ms while -12 was still overridden.
  - DESIGN.md still showed the -12 override.
  - `restore ... --why` fails with an argparse dump.
  - Two restores of -12 logged D-0015 and D-0016.
- **Fix:**
  - Restore and override should name the other holders, with an `--all-holders` option.
  - Add `--why` to restore (argparse around 7763).
  - Make `std_restore_needed` (4968) a real no-op check.
  - `supersedes` should name the decision that last set each path.

**R09 · engine, skill text**
- **What:** the hover and color transition uses an ease-in-out curve, which breaks STD-easing-duration-01.
- **Evidence:**
  - Line 2066: `"feedback": t("micro", "standard", ...)` gives `--ds-motion-transition-feedback-easing: cubic-bezier(0.77, 0, 0.175, 1)`.
  - `motion.easing.hover` (the `ease` curve) is locked but unused.
  - The Tailwind export has only standard, enter, exit and linear (5696).
  - DESIGN.md For Agents recommends `ease-standard` (6577).
  - Extend SKILL.md:78 says "a hover transition gets the feedback transition".
- **Fix:**
  - Point the feedback transition at `motion.easing.hover`, falling back to standard.
  - Export every `motion.easing.*` key to Tailwind (hover, drawer, toast).
  - Change the For Agents motion row to `transition-feedback`, `ease-enter`, `ease-exit`, `ease-hover`.
  - Press can stay on the enter curve through a separate press transition (optional).

**R10 · engine, skill text**
- **What:** `show motion` fills the template with made-up durations and curves that contradict the locked standards.
- **Evidence:**
  - Payload: productive medium 220 / long 350, enter `(0,0,0.38,0.9)`; two-mode 250/400, `(0,0,0,1)`; springs long 450.
  - The locked values are medium 200, long 250, enter `(0.23,1,0.32,1)`.
  - The motion branch (8599) reads `meta["motion"]`, the pre-override ladder from line 2046.
  - `TEMPLATE_QUESTIONS` (8463) leaves out `none`, and there is no "current" option.
  - `assets/templates/motion.html` sample od-data has `cubic-bezier(0.3,0,1,1)` exits and `(0.34,1.56,0.64,1)`.
- **Fix:**
  - Build each option from the generated `files` (resolved tokens after overrides).
  - Add a "current" option from resolve, and add `none`.
  - Replace the template's sample data with house values.
  - This breaks SKILL.md:74 ("Never fill a template with invented values") until fixed.

**R11 · engine**
- **What:** `pick` accepts an option whose effect a standard locks, then says "the tokens already match".
- **Evidence:**
  - `pick Q-motion-07 remove` prints `skipped raw.reducedMotion (locked by STD-accessibility-motion-02)` and then `recorded; the tokens already match this answer.`
  - DESIGN.md then shows "Remove all non-essential motion (chosen; tokens; Q-motion-07)" next to "travel becomes opacity".
  - `pick Q-motion-02 16-steps` puts "16 steps (Material 3)" above the locked duration table.
- **Fix:**
  - When any `answer_effects` path is standard-held, exit 1 with `std_lock_message`, or send it through `standard override`.
  - Never print "tokens already match" after a skip.
  - (Which questions the stage files should still ask is D02.)

**R12 · standards content**
- **What:** review's fix messages lead straight into another finding.
- **Evidence:**
  - STD-performance-properties-06 says "for example transition: transform 200ms ease-out". That line is flagged by STD-easing-duration-02.
  - STD-easing-duration-03 says "use ease-out, cubic-bezier(0.23, 1, 0.32, 1)". That is flagged by STD-visual-details-26.
  - Both were reproduced with `review`.
- **Fix:**
  - In `synthesis/standards.json`, change -06's `values.instead` and `review.message`, and -03's message, to name tokens, for example `transition: transform var(--ds-motion-duration-medium) var(--ds-motion-easing-enter)`.
  - Then run `wiki.py standards --bump`.

**R13 · tools/wiki.py and workflows**
- **What:** all five learn workflows default ROOT to the owner's checkout.
- **Evidence:**
  - `.claude/workflows/learn-{analyze,standards,escalate,personas,synthesis}.js` lines 13–17 fall back to `'/Users/Kunal/Desktop/Design-System'`.
  - `pending --work-items` prints a bare array with no root.
  - The README doesn't mention `root`.
- **Fix:**
  - Have `--work-items` emit `{"root": ROOT, "items": [...]}`.
  - The workflows should require `root` or fail.
  - Document it in `learn/README.md`.

**R14 · tools/wiki.py**
- **What:** `add` lets two sources share a folder or id prefix, and can list one page twice with conflicting authority.
- **Evidence:**
  - `cmd_add` (116–134) uses a substring check (`args.url in json.dumps(cfg)`).
  - The folder comes from `slug(name)`, with no collision check.
  - GitHub `id_prefix` is `slug(name)[:12]`, so every URL becomes `github-com-o`.
  - A trailing slash counts as a new URL.
- **Fix:**
  - Normalise URLs (scheme, `www.`, trailing slash) and match exactly.
  - Refuse an existing folder or `id_prefix`.
  - Derive GitHub names from owner/repo.
  - On a duplicate, print the owning source and its authority.

**R15 · tools/wiki.py**
- **What:** `ingest` half-updates a page after an analysis edit, and `next` then stops flagging it.
- **Evidence:**
  - `cmd_ingest` (around 339) lets OpenWiki skip an unchanged raw file but still rewrites the "For OpenDesigner" section.
  - `next` (around 927) compares mtimes, so the rewritten page looks fresh.
- **Fix:**
  - Store each analysis hash in `ingested.json`.
  - Force re-ingest when the hash differs.
  - Compare hashes in `pipeline_state`.

**R16 · build_data, docs**
- **What:** changing a standard without a version bump passes every local check, although docs/KNOWLEDGE.md:77 says it "fails the build".
- **Evidence:**
  - `build_standards` (tools/build_data.py 380–400) never checks `content_hash`.
  - The AGENTS.md "Before you commit" list lacks `wiki.py standards`. Only CI (ci.yml:75) catches it.
- **Fix:**
  - `build_data.py` and `--check` compare `standards_hash(doc)` with `content_hash` and exit 1.
  - Add `wiki.py standards`, `map --check`, `proposals --check` and `test_wiki.py` to the AGENTS.md checklist.

**R17 · tools/wiki.py and workflows**
- **What:** a new non-negotiable source is never picked up by the standards and escalation workflows.
- **Evidence:**
  - The learn-standards.js COMMON prompt (line 54) hard-codes `raw/{emil-kowalski,emil-skills,sonner,animations-dev,vaul}`.
  - learn-escalate.js:16 hard-codes the id-prefix-to-folder map.
- **Fix:**
  - Build source names, raw folders and the prefix map from `learn/sources.json`.
  - Add a "new house source" checklist to IMPROVING section 4.
  - (Allowing new themes is part of D07.)

### Medium

**R18 · engine**
- **What:** review misses raw durations on any line that also uses `var()`, and suggests tokens by nearest value in the wrong role.
- **Evidence:**
  - Line 8263 skips lines containing `var(--`: `transition: opacity 250ms var(--ds-motion-easing-enter)` gets no finding.
  - `motion_fix` (8225) maps anything ≤200ms, or any line mentioning opacity, to feedback: 180ms, 250ms opacity and a 160ms exit all get feedback (100ms).
  - 450ms gets expand (250ms), not `motion.duration.modal`.
  - `#ff0000` gets `--ds-color-text-disabled`.
  - `borderRadius: 12` on a Button gets overlay (engineer).
- **Fix:**
  - Scan each literal whether or not the line has `var()`.
  - Prefer an exact-value token.
  - Take the role from selector or name (exit, close, leave go to exit; modal or dialog to `motion.duration.modal`; button to `radius.control`).
  - Suggest no color when the difference is large.
  - Cite the standard that holds the token.

**R19 · engine**
- **What:** generated motion tokens break the 300ms rule and one token's own description.
- **Evidence:**
  - `--ds-motion-duration-extra` is 710ms (`700*mult`, line 2007, never locked).
  - `--ds-motion-transition-move` is 590ms on `cubic-bezier(0.77,0,0.175,1)`. `spring_token` (1990) emits `linear()` only when z<1, although the token says "web: linear() sample".
  - Spatial slow is 870ms.
  - DESIGN.md says "durations x1.02 on medium and longer", but those are locked.
  - Review never flags `var(--ds-motion-duration-extra)`.
- **Fix:**
  - Emit a `linear()` sample for z≥1 as well.
  - Relabel `extra` as "illustrative/marketing only (STD-easing-duration-06)" (whether to cap it is D05).
  - Make the DESIGN.md intent line name the steps the multiplier still moves.
  - `std_validate`: warn on `motion.transition.*` over 300ms without a justifying standard.

**R20 · engine**
- **What:** DESIGN.md and the decision log misreport who decided.
- **Evidence:**
  - With feel and brand delegated, DESIGN.md says "Decided: 4 answers you gave; everything else uses sourced defaults".
  - `render_summary` (6488–6500) counts every `ANSWER_PATHS` path as chosen.
  - `decisions.md` D-0008 says "(their words: fun, friendly)" and D-0009 says "the person's own feel words", both under `set_by: delegated`.
- **Fix:**
  - Count from each path's latest decision `set_by`.
  - In sketch, word delegated reasons as "picked for them".

**R21 · engine**
- **What:** DESIGN.md's Decisions table and links are wrong.
- **Evidence:**
  - The table (6969–6971) is the last 20 by id but labelled "highest-reach", so after an update the person's own choices drop out.
  - "N decisions so far" counts paths (55, while the log has 10 entries).
  - `[decisions.md](decisions.md)` and `tokens/` (lines 85 and 673 of the output) don't exist at the project root.
- **Fix:**
  - List chosen, assumed and delegated decisions and overrides first, with one row per standards batch.
  - Count unique ids.
  - Prefix the links with `opendesigner/`.

**R22 · engine**
- **What:** `opendesigner/standards.md` is not "every rule, with its values, reasons and sources", as DESIGN.md promises.
- **Evidence:**
  - DESIGN.md says 288 standards are followed; `standards.md` lists 225 ids.
  - All `design_md:false` rules are missing, including STD-process-review-taste-40.
  - There are no Why or source lines, and 23 values are truncated with "....".
  - No standards version is shown in either file.
- **Fix:**
  - Put every followed rule in `standards.md` with its why, source ids and full values (`design_md` should only filter DESIGN.md).
  - Add "house standards vN" to both files.

**R23 · engine**
- **What:** DESIGN.md's Standards section is long and shows values that aren't in force.
- **Evidence:**
  - 731 words, with no `<details>`.
  - "Springs and gestures (32 rules)" names 8 and says "and 13 more"; Toasts (22 rules) names 6 with no "more".
  - The Locks list shows `component.toast.duration` 4000ms while the export has 5000ms (the project standard wins).
  - Override lines never state the current value.
- **Fix:**
  - One plain sentence plus 3–5 "don't" bullets, with the per-theme lines inside `<details>` (`rules.md` section 2.9).
  - Keep the counts consistent.
  - Locks should show the value in force with "(PRJ-nn wins)".
  - Override lines should end with "Now: `<path>` <value>".

**R24 · engine**
- **What:** `standard add` takes one `--path`/`--value` pair and silently keeps only the last.
- **Evidence:**
  - With two pairs, only `PRJ-03: focus.ring.offset = 2px` is recorded.
  - The argparse flags at 7772–7773 are plain `store`.
- **Fix:** use `action="append"` on both and pair them by index, or refuse a repeated flag.

**R25 · engine**
- **What:** a project standard on `radius.control` redrives and freezes the whole corner scale.
- **Evidence:**
  - Adding `radius.control = 6` moved container from 24 to 8 and overlay from 32 to 12.
  - `set dials.roundness 90` then prints "no token changed: the system already had this value".
- **Fix:**
  - Keep deriving the other radii from the roundness dial when `radius.control` is standard-held.
  - Replace the message with "PRJ-nn holds radius.control ...".
  - In `rules.md` section 12, tell the agent to say when a token is broader than the rule.

**R26 · engine**
- **What:** a house update never shows what changed, and a no-op update still rewrites files.
- **Evidence:**
  - With a v2 file: `STD-components-toasts-drawers-12: component.toast.gap = 12px` shows no old value, and D-0011 records `supersedes: none`.
  - A second `--update` still prints "DESIGN.md and PRODUCT.md updated".
- **Fix:**
  - Print `path: old -> new` grouped by area.
  - Mark "changed" only when the rule or engine values differ from the snapshot.
  - Set `supersedes` per path.
  - Skip the refresh when nothing changed.

**R27 · skill text**
- **What:** the extend start-up routine can miss a house upgrade and never rebuilds.
- **Evidence:**
  - opendesigner-extend SKILL.md:25–26 runs `review`, which never reports the standards version, and only then refers to validate.
  - `--update` ends with "tokens update on the next generate".
- **Fix:**
  - Step 3 should run `engine.py validate` (or `review` should report the standards version).
  - Add "then `engine.py build`" after `--update`, and print that in `std_sync`.

**R28 · engine**
- **What:** review misses locked component values written in JavaScript, and reports one line twice.
- **Evidence:**
  - `toast.success(msg, { duration: 3000 })` is not flagged while `component.toast.duration` is locked.
  - `transition: "width 200ms"` is reported by both STD-performance-properties-01 and a project standard.
- **Fix:**
  - Check literal values of locked `component.*` tokens, or tell `rules.md` section 12.4 to pair `--path` with `--review-pattern`.
  - Merge findings per file and line, listing every id.

**R29 · engine**
- **What:** the project files are heavy.
- **Evidence:**
  - `state.json` is 576KB even after the platform cleanup (designer saw 819KB), about 415KB of it `standards.records`.
  - `decisions.md` is 66KB, and the D-0002 heading lists 455 ids.
  - The DESIGN.md Motion section cites D-0002 36 times.
- **Fix:**
  - Move the records to a sidecar file, and have agents read them through `engine.py standards --json`.
  - Put counts in decision headings, with the ids in a folded list.
  - Cite D-0002 once per section.

**R30 · engine**
- **What:** `validate` right after a `set` checks old token files.
- **Evidence:** after `set focus.ring.width 1`, validate says "Passes: no errors", while build says `ERROR The focus ring is thinner than 2px`.
- **Fix:** regenerate in memory, or warn "tokens are older than state.json; run build".

**R31 · engine**
- **What:** a kept legacy value plus the standards' absolute values gives an incoherent motion scale, silently.
- **Evidence:**
  - A legacy state with medium 240 keeps it, but gets long 250 and medium-exit 160.
  - validate is silent.
- **Fix:** validate warns when medium ≥ long, or when the exit/entrance ratio falls outside 0.7–0.9. (Deriving exits instead is D05.)

**R32 · standards content, retrieval**
- **What:** some standards' "conflicts" notes describe code and text that a7cce09 already changed.
- **Evidence:**
  - STD-easing-duration-01 and -03 still cite accelerate exits `[0.3,0,1,1]` and "ease-in to exit" in the stage text.
  - -11 cites 0.75×.
  - STD-enter-exit-origin-08 and -11 cite the old exit curve and expand at 400ms.
  - STD-mobile-touch-05 says "no press-scale token".
- **Fix:**
  - Rewrite those conflicts and bump the standards version.
  - Have `tools/jev_nav.py check` confirm that each quoted fragment still exists in the file it names.

**R33 · retrieval**
- **What:** any card named in a standard's conflicts is shown as overridden by the house, even when the house didn't mean that.
- **Evidence:**
  - `house_overrides` (jev_nav.py 181–183) treats every DC id in `conflicts` as overridden.
  - So DC-L08-18 (never auto-dismiss toasts with actions) is marked overridden by STD-components-toasts-drawers-15.
- **Fix:** add a `supersedes` field to standards and use only that. (The toast rule itself is D04.)

**R34 · retrieval**
- **What:** retrieval is weak for broad questions.
- **Evidence:**
  - "color mistakes" ranks button cards first by keyword (DC-L19-107, -106, -104). DC-L19-01 and -03 sit at ranks 65 and 76.
  - DC-L19-171 falls just outside the 40-card pool (`KEYWORD_CANDIDATES = 40`).
  - `judge_text` omits Options.
  - Rows moved below their overrider keep their out-of-order scores.
- **Fix:**
  - Add stopwords (ui, make, look, design, good).
  - Raise the pool to about 60 or weight titles.
  - Pool the L19 cards that cite the chosen lane's cards.
  - Print "no confident answer" when the best score is under 0.6.
  - Pull a missing overrider into the results.
  - Show Options to the judge.
  - Label moved rows "(superseded)".

**R35 · tools/wiki.py**
- **What:** `standards --bump` fails silently outside git and rewrites history.
- **Evidence:**
  - Lines 484–489: when `git show` fails, the old list is empty, the version stays, and history is replaced by one entry listing all 455 as added.
  - test_wiki.py:304–310 asserts exactly that.
- **Fix:**
  - Decide "first release" from the file itself (no `history`).
  - Exit 1 if git is unavailable.
  - Test v1→v2 with a patched git lookup.

**R36 · tools/wiki.py**
- **What:** `--bump` compares with git HEAD rather than the file's current version.
- **Evidence:**
  - Bumping twice before a commit records the same change twice.
  - A bump with no change still moves the version.
  - Line 508 stamps `built_from`, which hides the "[standards] built before N new ..." step.
- **Fix:**
  - Refuse when `content_hash` is unchanged.
  - Amend the uncommitted history entry when HEAD's version is lower.
  - Stamp `built_from` only from the learn-standards merge.

**R37 · tools/wiki.py**
- **What:** `status` and `next` mislead in a fresh clone.
- **Evidence:**
  - `learn/raw/` is git-ignored.
  - `cmd_status` counts from raw files, so it shows 0 analysed and 0 ingested despite 99 committed analyses.
  - `next` (913–919) asks to re-fetch every channel.
- **Fix:**
  - Count from `learn/analysis` and `ingested.json`.
  - List "raw text not on this machine" separately, after real work.

**R38 · tools/wiki.py**
- **What:** fetch problems are silent.
- **Evidence:**
  - `fetch_page` prints `SKIP (too little text)` and exits 0, and `next` repeats "nothing fetched yet" forever.
  - `--only` with no match is silent.
  - There is no `remove` command.
- **Fix:**
  - Exit 1 when nothing was fetched or `--only` matches nothing, listing the valid names.
  - Record skipped URLs.
  - Add `wiki.py remove`.

**R39 · tools/wiki.py**
- **What:** `next` never runs `check`.
- **Evidence:** `pipeline_state` (909–986) has no check call, so an authority mismatch error never surfaces there.
- **Fix:**
  - Run `check_analysis` first in `pipeline_state`.
  - Give a fix command for each error (for example "re-run learn-analyze" for a changed authority).

**R40 · tools/wiki.py**
- **What:** `check_analysis` lets wrong types through, and ingest then garbles them.
- **Evidence:**
  - Lines 1102–1134 don't type-check `values`, `numbers` or `caveats`, or validate `area`, `kind`, `applies_to` or `maps_to`.
  - A string `caveats` renders as one caveat line per character.
- **Fix:**
  - Type-check those fields as lists.
  - Validate enums against the learn-analyze schema.
  - Validate `maps_to` against `references/questions.json`.

**R41 · tools/wiki.py**
- **What:** `pending --work-items` puts a whole new repo into one work item.
- **Evidence:** the grouping regex (267) is written for emilkowalski/skills, so other files fall into one `<folder>-root` item (40 files seen).
- **Fix:** group by parent folder, capped at about 5 files or N characters per item.

**R42 · tools/wiki.py**
- **What:** several "next step" hints can't be run as written.
- **Evidence:**
  - The synthesis and standards steps give no workflow name or args.
  - cite-check doesn't mention `JEV_API_KEY`.
  - `--bump` says only "build_data, CHANGELOG, commit", skipping cite-check, learn-escalate, sync_skills and map.
- **Fix:** print exact commands and workflow args, for example `learn-synthesis {"topics":[...]}`.

### Low

**R43 · engine**
- **What:** small engine issues.
- **Evidence and fix, per issue:**
  - validate repeats source ids ("eks-skills-apple-design-skill" three times). Dedupe them.
  - `intake /nonexistent.json` prints a traceback (around 7613). Print a plain "file not found".
  - Override on a legacy state says "Unlocked: nothing (it sets no values)". Say "not applied yet".
  - `"ease-in"` is rejected as not a cubicBezier. Map `ease`, `ease-in`, `ease-out`, `ease-in-out` and `linear` to their curves.
  - The orphan note (3059) lists standard tokens (`font.size.input`, `motion.duration.drawer`). Exclude standard-held paths.
  - `standard remove` and `override` show `[--why WHY]` but require it. Use `required=True`.
  - `standard add` says "It is locked like a house standard" for rules that lock nothing. Word it per case.
  - `engine.py standards` prints project standards last (line 339 of 346). Show project standards and overrides first; hide off-platform rules unless `--all`.
  - Delegated-feel reasons: see R20.

**R44 · engine, skill text**
- **What:** the brand line isn't plain enough to pass on, as zoom.md:26 asks.
- **Evidence:**
  - It includes a hex, "3.49:1" and `color.brand.seed`, against the plain-voice rule at zoom.md:66.
  - For a delegated color it still says "Your brand color".
- **Fix:**
  - `brand_line` (7931) should have a plain variant.
  - When the brand is delegated, pick a passing shade directly and describe it in words.

**R45 · tools/wiki.py**
- **What:** small wiki.py issues.
- **Evidence and fix, per issue:**
  - `save_sources` rewrites the hand-formatted `sources.json` (the file isn't in `indent=2` form). Format it once canonically.
  - `trace` stamps only `%H:%M`. Use ISO date and time.
  - The 10 `learn/wiki/synthesis/_cards/*.md` files have no front matter, and there is an odd entity page `ami-caption-spelling-...`. Add front matter or exclude them from lint, and remove the entity.
  - `add --help` has no descriptions or allowed authority values. Add them.
  - `next` always appends "...". Only add it when truncated.
  - Website source pages say "Video ID" and "Channel". Use page labels.
  - The README lacks `citation-review.json`. Add it.
  - `openwiki.lock.json` still says "pending: tools/test_wiki.py". Run `upstream --upgrade` in a branch so it rewrites the lock.

**R46 · docs, skill text**
- **What:** three docs disagree on how to record a source.
- **Evidence:**
  - SKILL.md:97 omits review flags, KNOWLEDGE.md:58 uses `--values`, and rules.md:208 uses `--review-pattern`.
  - For good-to-have: KNOWLEDGE.md:59 says `set --set-by reference`, rules.md:209 prefers `standard add --authority good-to-have`.
  - For a reference source: KNOWLEDGE.md:60 says `set references.<id>`, rules.md:210 says record nothing.
- **Fix:**
  - Use one line everywhere: `standard add --rule --why --source [--path P --value V]... [--values] [--review-pattern --review-message] [--authority]`.
  - Follow rules.md's route for good-to-have and reference sources.

**R47 · skill text, glossary**
- **What:** glossary gaps and small skill-text issues.
- **Evidence:**
  - No entry for "standard" or "house standard".
  - Two "reduced motion" entries with different plain sentences (`core.reduced-motion` and `found.motion.reduced`).
  - rules.md section 12, step 6 would offer upstream a private local file name.
  - `context.product` is shown verbatim ("my school coding club").
- **Fix:**
  - Add the term and merge the duplicate in `synthesis/glossary.json`.
  - Skip the upstream offer for local or internal sources.
  - Tell the agent to record the product in the third person.

## Part B: fixes that need an owner decision

**D01 · High · engine**
- **What:** standards tagged only `react`, `react-native` or `css, react` never apply to any project.
- **Evidence:**
  - No Q-plat-01 option (web, ios, android, desktop, secondary) matches those tags.
  - A web `--update` dropped 22 web-relevant standards (20 react-only, 1 "css, react", 1 "react, react-native"), including STD-visual-details-62, which has a review check.
  - React Native-only standards drop on every mobile project.
- **Decision:** does web imply React, or should the stack be detected?
- **Recommendation:**
  - Map web to {web, css} always.
  - Add react and react-native from a recorded `raw.stack`, detected from package.json (look before you ask).
  - Ask once only if package.json doesn't settle it.

**D02 · High · skill text, build_data**
- **What:** stage files still ask questions a standard already settles, and offer options that break standards.
- **Evidence:**
  - Q-motion-02, -03, -04, -07 and -10 are settled but not marked.
  - Q-motion-01 labels `springs` "Springs throughout", cites the Carbon curve for `productive`, and promises "quick fades" for `none`. Its default says "7 durations 50-500ms" and "bounce ≤0.2".
  - Q-motion-02 offers 6 and 16 steps, -03 intensity- and personality-based, -04 durations-only, -06 fade and fade-through with an "all four" default.
- **Decision:** retire settled questions (skip them like Planned ones, with "Settled by STD-...") or keep them as entry points to an override.
- **Then:** `build_data` tags options "breaks STD-..." and the option texts are rewritten.

**D03 · Medium · docs, engine**
- **What:** the docs give two routes for "our brand guide says X", and nothing covers house rules that clash with a project rule on another token.
- **Evidence:**
  - docs/KNOWLEDGE.md:38 says "your guide wins" (a project standard); guardrails 4b says `standard override`.
  - STD-easing-duration-03 kept flagging code that followed a PRJ ease-in exit.
  - `standard add` requires `--source`.
- **Decision:** "it's our brand / always" becomes a project standard, and "just this value" becomes an override. Does a non-negotiable company rule count as the explicit ask?
- **Then:**
  - `standard add --beats STD-a,STD-b` records "project wins", disables those checks, and restores them on remove.
  - Allow `--source "person, <date>"`.

**D04 · Medium · standards content**
- **What:** STD-components-toasts-drawers-15 auto-dismisses every toast after 4000ms.
- **Evidence:** DC-L08-18 and Q-form-04 say never auto-dismiss toasts that contain actions (a timing accessibility concern).
- **Decision:** add an action-toast exception to the standard (recommended), or record that the house overrides DC-L08-18 on purpose.

**D05 · Medium · standards content, engine**
- **What:** exit durations are locked as absolute values, and the 700ms `extra` step has no rule.
- **Evidence:** STD-easing-duration-11 locks 160 and 200 absolutely (see R31). `extra` is unlocked at 700ms × energy multiplier.
- **Decision:**
  - Derive exits as 0.8 × entrance, so a person's kept value stays coherent.
  - Cap `extra` at 300ms, or keep it as illustrative-only.

**D06 · Low · skill text**
- **What:** people in a hurry still get the log question as the whole first message.
- **Evidence:**
  - SKILL.md:47–48 asks the journey-log question first even after "just pick".
  - Greeting line 2 (rules.md:6) promises "a few quick questions".
  - SKILL.md:55 shows a bare `--delegated`; zoom.md:44 says to name the flags. This was harmless in the run.
- **Decision:** can the consent question move to after the first result in hurry mode?
- **Either way:** align SKILL.md:55 with zoom.md:44.

**D07 · Low · engine, tools/wiki.py**
- **What:** export and theme scope.
- **Evidence:**
  - Swift and Compose files are built for a web-only project.
  - learn-standards has a fixed list of 11 themes (see R17).
- **Decision:**
  - Export only the recorded platforms by default, keeping `--format all`.
  - Allow new standards themes, or map by area.