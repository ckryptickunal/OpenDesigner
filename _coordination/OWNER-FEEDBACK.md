# Owner feedback log

Kunal's feedback from his own test runs, in his words where it matters, with what each point means for the project. Append new entries; never rewrite old ones. Each item stays **open** until a change in the repo addresses it, and then names that change.

## 2026-10-07: explainer video test (Claude Code, Opus 5.5)

The test was "make a fast, kinetic, premium video explaining the project". It was meant to show whether OpenDesigner gets used end to end, for things other than app UI. The working files are `videos/` (`RETROSPECTIVE.md`, `opendesigner-explainer/AUDIT-v1.md` and `opendesigner-film/AUDIT-v2.md`).

| # | Feedback | What it means for the project | Status |
|---|---|---|---|
| 1 | v1 "looks cheap", "very much like AI slop". | Without a design system and references, the agent falls back on its average idea of "premium", and that is slop. | open |
| 2 | "The voiceover is missing." | An explainer means a voice, captions or both. The agent decided on silence and never asked. | addressed in v2 (narration and captions) |
| 3 | "Why don't you use Mobbin... for understanding and building a design system itself for the video?" "This design system thing can also be used in videos." | OpenDesigner has to apply to any visual surface: video, deck, card, page. Nothing currently sends an agent to it when the request is "make a video". | open; `opendesigner-preflight` step 1 says "system first", but the main skill and engine have no film or video surface (engine feedback, gap 1) |
| 4 | The agent should find its own typography and design-system errors, and keep a common-mistakes skill that anyone can use before exporting. | A reusable check before any export. | addressed: `skills/opendesigner-preflight/` (34 checks, 35 mistakes, helper script) |
| 5 | The agent should say where it fell short and why it made its choices, so the process can be improved. | Retrospectives are part of the deliverable. | addressed: `videos/RETROSPECTIVE.md` |
| 6 | Idea: start as AI slop and let the video define itself until the ending looks premium. | A story structure, built in v2. | used in v2 |
| 7 | v2 "looks very okay-ish"; "even the generated one looks shitty". | The film's system (sketch plus taste-poll dials) wasn't enough for a premium result. Either the sketch defaults are too generic, or the references weren't used deeply enough to shape the system. "Use Mobbin to figure out a design system." | open |
| 8 | "There is a white noise at the end of every voiceover, which makes it very frustrating to watch." | Root cause: the TTS API returned a WAV file (`audio/wav`), and the script decoded it as raw PCM. The header and 6,070 bytes of trailing metadata played as noise. No check listened to the clip edges. | cause fixed in `videos/opendesigner-film/audio/tts.py` (audio not regenerated); `preflight.py audio` now fails such clips (M34) |
| 9 | "Do not make any more video yet." | Hold all video work. | standing instruction |
| 10 | Next steps: add the design directory https://styles.refero.design through the OpenWiki system (or whatever fits). Then define what a **blank slate** and a **blank design system** mean to us. Then test the feedback feature, the design features and everything else. | The plan for the next phase. | in progress. Refero's robots.txt blocks AI crawlers, and its Terms of Use forbid scraping and dataset creation. Kunal: "try all, pick the one that produces correctly qualified human results, use llmwiki/openwiki". Results: (a) the MIT Refero Skill went through OpenWiki: 12 files, 280 rules, each checked by an adversarial verifier; Jev supports 245 of 253, with 0 contradictions and 18 flagged for review. (b) Refero Styles was read by hand (3 styles), insights only, in `research/R6-refero-styles-observations.md`. (c) The Refero MCP is not installed and needs Pro. Synthesis into Decision Cards waits for the blank-slate discussion |

Engine gaps found during this test, logged with `engine.py feedback` in `videos/opendesigner-film/system/opendesigner/feedback.md` (not posted):

1. There is no video, film or presentation surface. A house standard blocked a dark-only film.
2. The feel-conflict warning stays after the dials are set explicitly.
3. There is no viewing-distance or medium scale for type.
4. `system-ui` is the font, so renders differ between machines. The engine never asks for a shipped typeface.

## 2026-10-15: taste, a creator's reel, and keeping GitHub current (Claude Code, Opus 5.5)

One session, with several others working in the same checkout. Commits fe52fea to dde7894 on `main`. Quotes are lightly cleaned from dictation.

| # | Feedback | What it means for the project | Status |
|---|---|---|---|
| 1 | "What is taste index and how can we use this in our repo to build a user's particular taste... their choices, their inputs and inspirations?" | OpenDesigner builds from the person's own taste. Every taste signal (poll, decisions, inspirations, style pick, feel words) counts, merged per project. | addressed: taste index (fe52fea), taste card (c3873a9) |
| 2 | "You might need to watch this video to build design taste: understand it frame by frame and all the essence of this." (davecto's Instagram reel) | A video is studied frame by frame, not from its transcript alone: most of this reel's substance was on screen. | addressed: learning-wiki reference source (dde7894) |
| 3 | "Keep everything updated on GitHub as well." | Standing: push finished work once the checks pass. A push carries every session's finished work (his 2026-10-14 rule), never another session's half-done edits. | standing instruction |
| 4 | "Yes, include the 23 brand/kit PNGs in the push and record the exception." | Binaries still need his yes; each yes is recorded like the showcase thumbnails. | addressed: `scan_pr.py` REVIEW, threat table, REPO-PLAN, DECISIONS |
| 5 | "Remove the Pillow crop from taste.py, record a review exception for videos/*/package.json, then push." | Skills stay standard-library only, even for optional imports. Manifests without dependencies or install hooks can be reviewed instead of blocked. | addressed: 091916d, 7fdc90f |
| 6 | "Do this task here... but also critically we should not lose the vision and actual mission of the repo." | An outside idea is adopted as structure only. It keeps the person's taste (not a copied site's identity), never invents owner inputs, lets the repo's evidence beat an outside number, and keeps the DESIGN.md contract. | addressed: c3873a9; rule in `learn/IMPROVING.md` section 3 |
| 7 | "If you have anything left from your side, please check it and implement it and push it." | Before stopping, finish every open item, including a question he never answered, and fix stale notes. | addressed: dde7894 |
| 8 | "Add the instructions and learning that we had in this session to OpenDesigner's own learning thing, so that these kinds of things are not repeated." | Lessons go into repo files that every agent and model reads, not only into one tool's private memory. | addressed: this entry, `PROTOCOL.md` section 4, `learn/README.md`, `learn/IMPROVING.md` |

Mistakes made or caught in this session, and the rule that now prevents each:

1. A bare `git commit` swept in a file rename another session had staged. The commit was redone with explicit paths. Rule: `git commit -- <paths>` in a shared checkout (`PROTOCOL.md` section 4).
2. In zsh, a path list in `$paths` was not split into words, so `git add` failed. Rule: `${=paths}`.
3. A generated copy (`chatgpt-project/knowledge/05-engine.py`) went stale after a last engine edit. The working-copy checks passed because other files hid it; a clean checkout caught it. Rule: run `build_data.py` after the last edit, and check a clean `git worktree` of what you commit.
4. The first taste card sat between a section's plain sentence and its folded detail, which broke the three-voice layout. An existing test caught it, and the card moved after the fold instead of the test being weakened. Rule: when a contract test fails, change the design, not the test.
5. A showcase page offered a copy button for an install command piped from an unregistered domain into a shell. Anyone could have bought the domain. `scan_pr.py` blocked it. Rule: invented brands use RFC 2606 `.example` domains, and shown commands download before they run (`brand/showcase/BRIEF.md`).
6. A rule that quoted the blocked pattern was itself blocked by the scanner. Rule: describe a blocked pattern in words.
7. `yt-dlp` needs a login for Instagram, and `timeout` does not exist on macOS. The working path for login-walled videos is in `learn/README.md`.
