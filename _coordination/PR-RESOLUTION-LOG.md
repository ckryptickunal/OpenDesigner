# Open PR resolution log

Date: 2026-09-25  
Repo: [ckryptickunal/OpenDesigner](https://github.com/ckryptickunal/OpenDesigner)  
Reviewer: local agent, read-only GitHub inspection (`gh pr list/view/diff/checks`, `git fetch` of `refs/pull/*/head` into `refs/od-review/pr-*` without checkout).  
Working tree at review time: dirty `main` (L19 wiki / standards work). No PR branches were checked out. No commits, merges, pushes, approvals, or closes.

This file did not exist; it is the first resolution log. Extend it in later reviews rather than starting a second copy.

## Audio briefing

Source: `/Users/Kunal/Downloads/Audio Message.caf` (2026-09-25 14:32 IST, 3:17). Converted with `afconvert`. Transcribed locally with already-installed `faster_whisper` (`tiny`, CPU). The Python `whisper` CLI is installed but broken (`numba` vs `coverage.types.Tracer`). Tiny-model wording is approximate.

The file is a **founder product-vision note**, not a PR-review script. It does not ask to commit, merge, push, disable safety checks, or run untrusted code. PRs 30–34 cite this 14:32 note. A “2:39 PM IST follow-up” cited in PRs 31 and 33 was **not** in this file.

### Criteria taken from the audio

1. OpenDesigner is unfinished and must not be described as complete or as replacing human judgment.
2. Intended users: designers using AI tools; frontend / large-project engineers; people polishing an existing project.
3. Separate global/repo-level change from project-local adaptation.
4. After testing, learn where the interview should shorten or extend.
5. Show a readable board of gathered inputs, what was thought, and examples/outputs.

## Inventory

`gh pr list --state open --limit 100` returned **8** open PRs. All target `main`, all `MERGEABLE`/`CLEAN` vs `origin/main`, none reviewed. `gh pr checks` and `gh run list` are empty. `docs/GITHUB-SETTINGS.md` already records that GitHub Actions is disabled at the account level. “No failing checks” is not green CI.

By the task definition (draft, absent CI, missing reviews, incomplete implementation, or security problems), **all 8 are incomplete**. None is safe to merge as-is.

| # | Title | Author | Draft | Reviews | CI | Conflicts |
|---|---|---|---|---|---|---|
| 27 | Align illustration fallback order across hook references | fatihcvs | no | none | none (Actions off) | none vs origin/main |
| 28 | Test journey consent in local and web hosts | ckryptickunal | no | none | none | none |
| 29 | Include visual templates in standalone skill zips | ckryptickunal | no | none | none | none |
| 30 | Draft founder-grounded OpenDesigner product vision | ckryptickunal | no (title says draft) | none | none | none |
| 31 | Propose separate user and project preference scopes | ckryptickunal | no | none | none | none |
| 32 | Document test-first interview flow learning | ckryptickunal | no | none | none | none |
| 33 | Design project status board for inputs and outputs | ckryptickunal | no | none | none | none |
| 34 | Add a read-only project status board exporter | ckryptickunal | **yes** | none | none | none |

Local uncommitted L19 wiki / `ci.yml` edits are not in these PRs. Later merges will need a rebase onto that work.

## Cross-cutting security (static only)

Did not execute PR code or workflows.

- No `pull_request_target`, permission escalation, secrets, obfuscated payloads, binaries, new dependencies, install hooks, miners, or unexpected network clients.
- Only workflow edit is PR 29 adding `python3 tools/test_build_dist.py` under existing `permissions: contents: read`.
- PR 27 (only external author): structural JSON diff vs `origin/main` is **one field** (`Q-img-04.if_no` / questionnaire hook) plus a unit test.
- PR 34 is stdlib-only. Writes only if `--out` is passed.

No PR is a malware do-not-merge. Highest process risk: merging with Actions still off.

---

## PR 27 — https://github.com/ckryptickunal/OpenDesigner/pull/27

Author: fatihcvs · `fix/illustration-fallback-order` · claims Closes #25 (issue still open).

**Incomplete:** no review, no CI; regression test is weaker than claimed.

**Security:** clean. One-field JSON change, markdown hook-line reorder, 15-line unittest. No workflow or network code.

**Correctness:** the bug is real on `origin/main`. L17 Part H and `hooks.md` already say Commission → open sets → AI → no illustration. Top-level `hooks.json` `H-illus.if_no` already matches. Nested `questionnaire.Q-img-04.if_no` and the stage Hook line still put “ship honest icon-plus-text empty states” first. PR 27 reorders only that nested text and rebuilds generated copies (skills, `.agents`, `.claude`, `data/`, ChatGPT lookup). Source + generated together is the correct pattern.

New test `test_hook_and_questionnaire_share_the_documented_order` uses first-match of `\bcommission\b`, `\bopen sets\b`, `\bai\b`, `no illustration|ship honest`. Top-level `if_no` contains “bans AI training” **before** “AI: Recraft”, so `\bai\b` hits the open-sets clause. The test stays green if “AI tools” and “open sets” are swapped. It does catch putting “ship honest” first.

**Verdict:** needs specific fixes. Then re-review.

**Fix (apply on the contributor branch, not this dirty tree):**

```python
patterns = (
    r"\bcommission\b",
    r"\bopen sets\b",
    r"\bai(?:\s|:| vector tools)\b",
    r"no illustration|ship honest",
)
```

And for the questionnaire string only:

```python
self.assertRegex(
    q_if_no,
    r"^\(1\) commission[\s\S]+\(2\) open sets[\s\S]+\(3\) AI tools[\s\S]+\(4\) ship no illustration",
)
```

**Local change:** none (`test_engine.py` is already dirty from L19).

---

## PR 28 — https://github.com/ckryptickunal/OpenDesigner/pull/28

Author: ckryptickunal · `instinct/fix-journey-consent-test` · 1 file: `skills/opendesigner/scripts/test_journey.py`.

**Incomplete:** no review, no CI. Generated copies not updated.

**Security:** clean. Test-only env mocks. Does not change consent or logging.

**Correctness:** `journey.py` `detect_where()` is web unless `CLAUDECODE` is set and `CLAUDE_CODE_REMOTE` is not. `CONSENT_QUESTION` is the local string, so the old test fails on a generic host (as PR 27 also reported). The new test expects web wording when those vars are empty, then local wording when `CLAUDECODE=1`, and still asserts no `events.jsonl` before opt-in. That matches the code.

**Blocker:** `sync_skills.py --check` copies every file under `skills/`. After this PR, `.agents/skills/opendesigner/scripts/test_journey.py` and `.claude/skills/opendesigner/scripts/test_journey.py` still match `origin/main` and **not** `skills/`. Confirmed with `git show` on `refs/od-review/pr-28`. CI will fail once Actions is on. Optional gap: no `CLAUDE_CODE_REMOTE=1` case (should stay web).

**Verdict:** needs specific fixes. Copy the same test into both generated trees (or run `python3 tools/sync_skills.py` on a clean tree). Do not merge until `sync_skills.py --check` and `test_journey.py` can run.

**Local change:** none.

---

## PR 29 — https://github.com/ckryptickunal/OpenDesigner/pull/29

Author: ckryptickunal · `instinct/fix-standalone-templates`.

**Incomplete:** no review, no CI; test can pass with zero templates; temp dir created under the repo root.

**Security:** clean. Workflow stays `contents: read`. No `pull_request_target`.

**Correctness:** real gap. `BUNDLE` copies the engine into extract/extend/export zips, but `show` reads `assets/templates/*.html` from the skill root. The eight shipped templates are not in `BUNDLE`. The extra glob is right. Main `opendesigner.zip` already includes them via `rglob`. `test_build_dist.py` never asserts `len(list(templates)) >= 8`.

**Verdict:** needs small fixes, then this is the closest-to-correct code PR. Assert at least eight templates; drop `dir=build_dist.ROOT` unless required; enable Actions before merge.

**Local change:** none. Note: dirty local `ci.yml` already has wiki steps that this PR does not.

---

## PR 30 — https://github.com/ckryptickunal/OpenDesigner/pull/30

Author: ckryptickunal · new `docs/PRODUCT-VISION.md`.

**Incomplete:** body says “draft for review” but the GitHub PR is not a draft. Docs only.

**Security:** clean. No licences invented. No instruction-override text.

**Correctness vs audio:** matches the 14:32 note (unfinished; designers / FE engineers / people polishing existing apps; human judgment; AI cannot certify feel). Code claims match `origin/main` and `docs/HOW-IT-WORKS.md`. Correctly refuses demand/adoption/revenue claims.

**Verdict:** needs process fix. Convert to a GitHub draft, or merge only after Kunal accepts the written wording. Do not treat merge as locking owner inputs beyond the audio.

**Local change:** none.

---

## PR 31 — https://github.com/ckryptickunal/OpenDesigner/pull/31

Author: ckryptickunal · new `docs/GLOBAL-LOCAL-PREFERENCES.md`.

**Incomplete:** proposal only. Cites a 2:39 PM IST clarification **not** in the supplied audio. The audio mentioned global-to-repo vs project-local changes; the PR asserts Kunal confirmed both user-wide taste and reviewed repo contributions, with storage/sync as the remaining question.

**Security:** clean as docs. Proposed contract (no silent promotion of project context; tracking/sharing never inherited; no cloud sync assumed) is privacy-safe.

**Correctness:** `profile.voice` is project-local on main; treating a user-wide schema as unimplemented is honest. Merging “Resolved: Kunal means both…” overclaims relative to the only audio we have.

**Verdict:** needs Kunal to confirm or tone down the 2:39 claim. Keep as proposal. Do not implement cloud sync from this PR.

**Local change:** none.

---

## PR 32 — https://github.com/ckryptickunal/OpenDesigner/pull/32

Author: ckryptickunal · new `docs/FLOW-LEARNING.md`.

**Incomplete:** docs only. Correctly refuses a behavior-changing PR from assumptions.

**Security:** clean. Keeps consent, owner-input questions, and accessibility floors. No free-text answers in telemetry.

**Correctness:** matches the audio (“after testing… shorten or extend”). Accurately describes `journey.py` (opt-in; `analyze()` does not reroute; ChatGPT bundle omits the tracker). The pointer to PR 28 for the consent test is true.

**Verdict:** acceptable as a design note after human review. Do not start auto-routing.

**Local change:** none.

---

## PR 33 — https://github.com/ckryptickunal/OpenDesigner/pull/33

Author: ckryptickunal · new `docs/PROJECT-STATUS-BOARD.md`.

**Incomplete:** docs only; visual board not built. Also cites the unverified 2:39 board-vs-tree clarification.

**Security:** clean. Keep evidence local; do not invent citations; no default server send.

**Correctness:** matches the audio’s board of gathered info, thought, and examples. Correct that `graph.json` is a research DAG and `docs/HOW-IT-WORKS.md` is a process flowchart. The data contract is larger than PR 34 implements.

**Verdict:** keep as the spec for #34. Confirm board-vs-tree wording with Kunal. Do not merge as if a UI shipped.

**Local change:** none.

---

## PR 34 — https://github.com/ckryptickunal/OpenDesigner/pull/34

Author: ckryptickunal · draft · `tools/project_board.py` + `tools/test_project_board.py`.

**Incomplete:** GitHub draft. Does not implement #33 (no needed/received/pending/declined, no work grouping, no default `board.json`, no HTML, no “why / made from”). Sketch IDs are hardcoded (currently equal to `questions.json` `zoom0`). JSON lists every later question as `unrecorded`. New test is not in CI.

**Security:** clean for malware. Local file read. `--out` writes a caller-chosen path (normal CLI, not hidden exfil). No network.

**Correctness:** honest inventory slice vs the PR body. Handles example projects with `state.json` at the example root (`examples/devtool-dense`). Tests cover missing project, one recorded answer, hook status without file proof. Does not modify decisions. Does not yet give the user-facing board the audio asked for. `file_presence_not_checked` is `True` when a file list is non-empty (meaning “we did not stat those paths”).

**Verdict:** keep draft. Before ready: read `zoom0` from `questions.json`; default the human view to sketch + recorded later answers; add `python3 tools/test_project_board.py` to CI; do not claim #33 is implemented.

**Local change:** none.

---

## Local files touched in this review

- Added: `_coordination/PR-RESOLUTION-LOG.md` (this file).
- No PR patches applied (dirty L19 working tree).
- Temporary refs `refs/od-review/pr-27` … `pr-34` were fetched for `git show` only. Not checked out. Delete with `git update-ref -d refs/od-review/pr-N`.

## Deliberately not done

- No `git commit`, `git commit --amend`, `git merge`.
- No push, merge, close, or approve.
- No checkout that would overwrite uncommitted work.
- No execution of PR scripts or workflows.
- No skill rebuild and no edits to generated copies.

## Suggested order after fixes and after Actions is enabled

1. PR 28 — after skill copies are synced.  
2. PR 27 — after the order-check is tightened.  
3. PR 29 — after the “≥ 8 templates” assert.  
4. PRs 30–33 — docs/proposals only after Kunal accepts wording; 31/33 need the 2:39 claim confirmed or removed.  
5. PR 34 — last, still draft, after a thinner accepted slice of #33.

## Code written (2026-09-25, not committed)

Fixes are uncommitted in detached worktrees under `.worktrees/`. Main was not checked out onto these branches. Nothing was merged, pushed, or committed. The next agent can commit each worktree onto its pull-request branch.

| PR | Worktree | What the code now does | Checks run |
|---|---|---|---|
| 27 | `.worktrees/pr-27` | Order test matches commission, open sets, then the AI step (`AI vector tools` / `AI: Recraft` / `(3) AI tools`), then no illustration. A swapped sample fails. Skill copies synced. | `IllustrationFallbackOrder` OK; `sync_skills.py --check` in sync |
| 28 | `.worktrees/pr-28` | Consent test also covers `CLAUDE_CODE_REMOTE=1` (web wording, still no log). Generated `test_journey.py` copies synced. | Consent test OK; sync check in sync |
| 29 | `.worktrees/pr-29` | Zip test requires at least 8 templates. Temp dir is outside the repo. `build_dist.py` prints a path that is not under the repo root. | `test_build_dist.py` OK |
| 30 | `.worktrees/pr-30` | `tools/test_product_vision.py` locks the vision note to the engine, 8 templates, no `suggest_flow` in the engine, and the ChatGPT bundle's "no journey log" line. CI step added. | `test_product_vision.py` OK |
| 31 | `.worktrees/pr-31` | `preferences.py` resolves an in-memory user-workflow profile. Project voice wins on conflict, a lock blocks override, tracking/sharing/names/answers are refused, malformed input is ignored. `improvement_proposal()` redacts and sets `posted: false`. No file write and no cloud sync. | `test_preferences.py` OK; sync check in sync |
| 32 | `.worktrees/pr-32` | `suggest_flow()` returns keep / shorten / show-example / explain-more and never writes or skips. Owner and high-impact questions stay on a speed request. Help counts apply only when consent is passed in. Report text says `hypothesis, not applied` instead of auto-apply. The engine does not call it. | FlowSuggestions, delegation report, aggregate report OK; sync check in sync |
| 33 | `.worktrees/pr-33` | Spec now names the PR 34 contract: `zoom0`, needed/received/unrecorded, asset `board_status`, `link: unlinked`. | Doc only |
| 34 | `.worktrees/pr-34` | Board reads `questions.json` `zoom0`, groups decisions, keeps superseded decisions, does not stat asset files, writes only with `--out`. CI step added. | `test_project_board.py` 5 tests OK |

Still not done: GitHub Actions is off, so these tests ran locally only. No pull request was updated on GitHub.

## One stack (2026-09-25)

Pull requests 27–34 and the local fixes above are combined in `.worktrees/pr-stack`, based on `origin/main` (`30f0429`). Review instructions for the coding agent are in `_coordination/AGENT-REVIEW-BEFORE-MERGE.md` (also copied into that worktree). Do not merge the eight pull requests, and do not merge the stack, until that review is filled in. The stack is uncommitted. Local checks on the stack passed: illustration order, consent, flow suggestions, preferences, product vision, template zips, project board, and `sync_skills.py --check`.

---

## Second review: PRs 35–43, and the checklist for the 27–34 stack (2026-09-27)

Method: pulled each PR's commit into `refs/od-review/pr-35` … `pr-43`. No branch was checked out on `main`, and nothing was committed, pushed, merged or commented on GitHub. For each research PR, a separate fact-checker with no prior context re-fetched every cited npm tarball, pinned repo file and docs page and compared the values with the PR. PRs 36–43 were also merged together into a throwaway worktree, which has since been deleted, and the repo checks were run on the result.

### How the contributions fit the goal

All nine external PRs (27, 36–43) come from one contributor, fatihcvs, and each answers an issue the maintainer seeded: #25, #2 and #15. The quality is high. Each claim cites a Tier A source (published packages pinned to a version, plus official docs). Inferences carry `[inferred]`. Trace-id ranges were chosen in advance so they do not collide. No brand identity is copied. The PRs also avoid silently recomputing the 25-system averages. The volume and uniform style suggest an AI agent did much of the work. CONTRIBUTING welcomes that, so it is fine, but it is why every value had to be re-checked.

The bigger question is whether the work moves the product forward. Research that nothing downstream reads does not change what users get.
- Nothing downstream reads `benchmarks/systems/*.md` except the `jev_nav` search index. `build_questionnaire.py` reads `L09-benchmark-matrix.md` only to collect valid source ids. Merging the seven benchmarks makes them searchable, but no default, preset or question changes until a `synthesis/` card or lever cites them.
- The new teardowns cover 13–17 of the 21 Snapshot fields in the template (they are token-level). They leave out launch history, Figma kit, component count, doc structure and notable innovation, so they cannot slot into the matrix like the original 25.
- Licences affect what the product may do with this evidence. Of the seven new systems, only Cloudscape (Apache-2.0), NYPL (Apache-2.0) and GC (MIT) are permissive. Workday tokens are CC BY-ND 4.0 (no derivatives). EUI is ELv2 or SSPL. Duet is licensed only for work on behalf of LocalTapiola. Porsche code is Apache-2.0, but its fonts, icons and marque are restricted. Stating these facts is fine. The builder must never turn these four into presets or copy their values into a user's system.
- The systems differ in how much they add. The strongest additions are Cloudscape and EUI (dense data tools, relevant to #23), Porsche (fluid type and spacing), and Workday (OKLCH, and old and new token names shipped side by side). The weaker ones are GC (the matrix already has GOV.UK and USWDS) and Duet (a narrow licence and a niche market).

### Results per PR

| PR | Accuracy (live re-check) | Repo checks | Verdict |
|---|---|---|---|
| 36 Fluent conflicts (#2) | All 6 claims confirmed; 9.2.2 and alpha.24 are the current `latest` | pass | Merge after one fix. The `DECISIONS.md` line contains byte 0xFC (a non-UTF-8 "ü"), so `open(..., encoding="utf-8")` on that file now raises `UnicodeDecodeError`. Rewrite the line in ASCII with an IST timestamp. Follow-up: `benchmarks/systems/fluent-2.md` lines 56–57 still list both conflicts as open |
| 37 Workday Canvas | All confirmed, including the CC BY-ND licence and the pinned commit | pass | Merge |
| 38 Elastic EUI | Snapshot confirmed. **One error:** the "Version notes" paragraph and trace row S-L09-837 claim the docs border `#E3E8F2` differs from 8.1.0. It does not, because `euiBorderColor` is `#E3E8F2`. The PR compared it with a different token | pass | Fix that paragraph, then merge |
| 39 NYPL Reservoir | All confirmed (4.5.1 is `latest`, Apache-2.0) | pass | Merge. It omits the `headerDonate` radius, which is minor |
| 40 AWS Cloudscape | All confirmed (3.0.113 is `latest`, Apache-2.0) | pass | Merge. The header's mention of "visual-refresh JSON" slightly overstates it, which is minor |
| 41 GC Design System | Values match 2.14.0 exactly, but **`@cdssnc/gcds-tokens` is deprecated** and was replaced by `@gcds-core/tokens` 1.6.0 (2026-08-10), which changed 6 of the 10 listed colors | pass | Changes requested: move to 1.6.0, or label the entry as a historical snapshot |
| 42 Duet | All confirmed (5.1.5 released 2026-09-23, actively maintained, restrictive licence) | pass | Merge after dropping the unsupported word "legacy" from the Color row. Lowest priority |
| 43 Porsche | All confirmed (4.7.0 is `latest`; the Apache-2.0 code and restricted asset licences are both stated correctly) | pass | Merge |
| 35 Public feedback corpus (maintainer) | Not fact-checked. 23 records (20 Reddit, 3 GitHub, 2 HN) | n/a | Changes requested. It is a new file at the repo root and uses its own `OD-NN` ids instead of trace rows. Its content is Tier C community signal, so it belongs in `sources/` next to `COMMUNITY-SIGNAL.md` and should be cited from there. The PR template is left empty |

Combined tree (origin/main + 36–43): `build_data --check`, `sync_skills --check` and `build_dist --check` exit 0. `jev_nav check` reports 3294 ids and 0 dangling. `check_links` reports 168 links and 0 broken. 60 engine tests pass.

**Merge mechanics:** 37–43 each append to the end of `traces/L09-trace.md`, so after the first one merges, the other six conflict on GitHub. Each conflict needs both blocks kept (a union merge). No ids collide. Maintainers can edit these branches (`maintainerCanModify: true`).

### Stack for PRs 27–34: checklist run

In `.worktrees/pr-stack`: IllustrationFallbackOrder OK; test_journey OK; test_preferences OK; test_product_vision OK; test_build_dist OK; test_project_board OK; `sync_skills --check` in sync. `engine.py` has no `suggest_flow`. `project_board.py` has no `urllib` and writes only with `--out` (line 199). A search of the tracked diff and untracked files found no `pull_request_target`, `urlopen`, `requests`, `subprocess`, `eval` or base64 decoding. Not re-done: the swap-mutation check on the illustration test, which the earlier session reported as failing correctly. Result: **pass**. The record at the bottom of `AGENT-REVIEW-BEFORE-MERGE.md` is still empty, for the maintainer to sign.

### Policy recommendation (for Kunal)

1. Accept benchmarks only when they add a distinct archetype or close a gap listed in the lane's open questions. After this batch, narrow issue #15 to name the archetypes still missing, so it stops being an open call for more systems.
2. Require each new teardown to state what it can be used for (evidence only, or a possible preset source), based on its licence.
3. List the extended systems in `L09-benchmark-matrix.md` with what their licences allow (done 2026-09-27). The evidence reaches users only when a `synthesis/` card cites it, for example Cloudscape and EUI for data-heavy tokens (#23), or Porsche for fluid type.

---

## Merge record (2026-09-27)

Kunal asked to "rectify the PRs, either close them or correctly merge them". Each PR head was re-checked against the reviewed SHA, fixes were pushed to contributor branches (maintainers can edit them), each branch was brought up to date with `main` (traces merged with both sides kept), and then the local checks and the static scan ran again before a squash merge with `--match-head-commit`.

| PR | Outcome | Fix applied before merge |
|---|---|---|
| #27 | Merged (`0df8a42`), closed #25 | Order test matches the AI step by name; a swapped order must fail |
| #28–#34 | Closed; merged together as #44 (`65f74b7`) | Review fixes from the stack. #31 and #33 no longer say "Resolved": the 2:39 PM clarification is not in the saved 14:32 voice note, so it is marked "to confirm" |
| #36 | Merged (`27eeab1`), closed #2 | Decision line rewritten as UTF-8 with `21:11 IST`; `benchmarks/systems/fluent-2.md` notes both conflicts are resolved for React v9 |
| #37, #39, #40, #43 | Merged (`14e8cf8`, `465eae9`, `1e6ee5b`, `02cad05`) | None |
| #38 | Merged (`991b844`) | The border note had claimed a mismatch; `#E3E8F2` is 8.1.0 `euiBorderColor`. Only the docs prose differs from the source |
| #41 | Merged (`20600b1`) | Moved from deprecated `@cdssnc/gcds-tokens` 2.14.0 to `@gcds-core/tokens` 1.6.0. Five colors changed; all else was identical. New sources S-L09-839 to 846 |
| #42 | Merged (`c849b63`) | Dropped the unsupported word "legacy" |
| #35 | Merged (`998a8f4`) | Moved into `sources/` and linked from `COMMUNITY-SIGNAL.md`. A re-check of all 23 records (Reddit through the Arctic Shift archive, HN through its API) restored two trimmed quotes, labelled three promotional posts, and fixed two dates, one link, a dead link (now an archived copy) and three overstated summary lines |

After the last merge, `origin/main` has no conflict markers and no duplicate L09 source ids. `jev_nav check` reports 0 dangling and `check_links` reports 0 broken. The `build_data`, `sync_skills` and `build_dist` checks pass, and every Markdown file decodes as UTF-8. The stack tests (61 engine tests, journey, preferences, product vision, zip, project board, extract) passed on #44 before it merged.

`L09-benchmark-matrix.md` now lists the seven extended systems with what their licences allow. Four of them (Workday, EUI, Duet, and Porsche's assets) are evidence only.

All 17 PRs open on 2026-09-25 are now resolved. `tools/living_docs.py` now tracks the facts these documents depend on (baseline in `_coordination/living-docs.json`).

Open for Kunal: confirm or correct the "founder direction" in `docs/GLOBAL-LOCAL-PREFERENCES.md`. `_coordination/AGENT-REVIEW-BEFORE-MERGE.md` stayed local and is superseded by this record.
