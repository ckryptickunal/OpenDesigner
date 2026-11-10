# Review this stack before merging

This file is for the coding agent. Read it before any merge.

The work in `.worktrees/pr-stack` is one stack of open pull requests 27 through 34, including the local fixes already applied on top of those branches. It is based on `origin/main` at `30f0429`. It is not merged. It is not committed. Do not merge it, and do not merge pull requests 27–34, until the review below is finished and recorded.

## What this stack is

| Former PR | What landed in this stack |
|---|---|
| 27 | Illustration fallback order, plus a regression test that does not treat "bans AI training" as the AI step |
| 28 | Journey consent test for web, local, and remote Claude Code. Still writes no log before a yes |
| 29 | Standalone skill zips include the eight visual templates |
| 30 | Product vision note, locked to the repo by `tools/test_product_vision.py` |
| 31 | In-memory user-workflow resolver in `preferences.py`. No cloud sync. No posted issue |
| 32 | `suggest_flow()` suggestions only. The engine does not call it. Report text says hypothesis, not auto-apply |
| 33 | Board spec aligned with the exporter |
| 34 | Read-only `tools/project_board.py`. Sketch ids come from `questions.json` `zoom0` |

GitHub still has eight separate pull requests. After this review passes, put this stack on one new branch, open one pull request, and leave 27–34 unmerged so they can be closed in favor of that one pull request. Do not push this stack onto `main`.

## Review before merge

1. Read this file and `_coordination/PR-RESOLUTION-LOG.md` on the main working tree.
2. Run, from this worktree:

```
python3 skills/opendesigner/scripts/test_engine.py IllustrationFallbackOrder
python3 -m unittest skills.opendesigner.scripts.test_journey
python3 skills/opendesigner/scripts/test_preferences.py
python3 tools/test_product_vision.py
python3 tools/test_build_dist.py
python3 tools/test_project_board.py
python3 tools/sync_skills.py --check
```

The journey command above may need to be run as `python3 -m unittest test_journey` from `skills/opendesigner/scripts/`. Use that form if the package path fails.

3. Reject the merge if any of these are true:
   - A test fails.
   - `suggest_flow` is imported or called from `engine.py`.
   - `preferences.py` writes a file, sends a request, or copies `tracking`, `share_reports`, names, or answers across projects.
   - `project_board.py` imports `urllib` or writes `board.json` without `--out`.
   - Skill copies under `.agents/skills` or `.claude/skills` differ from `skills/`.
   - The illustration order test passes when "AI tools" is placed before "open sets".
4. Static security check, again, on the combined diff against `origin/main`: no new dependencies, no `pull_request_target`, no obfuscated payloads, no unexpected network calls. The earlier pass found none. Confirm the combined diff still has none.
5. Do not treat empty GitHub Actions as a pass. Actions is off for this account. Local tests are the evidence.
6. Write the result at the bottom of this file: date, commands run, pass or fail, and anything you refused to merge. Then, and only then, the maintainer may merge the single pull request.

## Do not do this during review

- Do not merge pull requests 27, 28, 29, 30, 31, 32, 33, or 34 on their own.
- Do not merge this stack into `main` before the checklist is checked off below.
- Do not enable cloud sync or automatic interview routing while reviewing.

## Review record

- Reviewer:
- Date:
- Commands:
- Result: not reviewed
