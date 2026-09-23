# Three voices: how OpenDesigner explains terms

Every term has three explanations in `synthesis/glossary.json`: **plain** (a school student follows it), **designer**, and **engineer**, plus two short labels for the one-line form: **designer_says** (what designers call it) and **code_name** (what it is called in code). This file says when to show which, so every person gets clarity every time without clutter (BRIEF requirements 12-13). Agreed with the OpenDesigner orchestrator on 2026-09-23.

## In conversation
1. **First mention: plain sentence plus one short line.** The first time a term appears in a session, give the plain sentence, then one line with the other two voices:
   > The accent color is the one color used for buttons and highlights.
   > Designers: primary or brand accent · Code: `color.bg.accent`
2. **After that, the term name only.** Don't explain the same term twice in a session unless asked.
3. **Switch which voice leads.** "Talk like a designer" or "talk like an engineer" makes that voice lead on first mentions (stored as `profile.voice`: `plain`, `designer` or `engineer`). The plain meaning stays available on request.
4. **"Explain fully" shows all three** full voices for that term.
5. **Same words every time.** Use the glossary's `term` names in every message and file. Accept `aliases` as input, but answer with the `term`.

## In files the person keeps
| File | Voices |
|---|---|
| `DESIGN.md` | Each decision opens with one plain sentence and the short line. Full designer and engineer notes sit in a collapsed `<details>` block under it. |
| `opendesigner/RATIONALE.md` (for sharing with a team) | Plain, then designer. |
| Tokens, code comments, exports | Engineer. |
| `docs/GLOSSARY.md` | Plain and the short line visible; full designer and engineer voices collapsed. |

## In visual templates
Each control shows its plain label and the short line. Full designer and engineer detail appear on hover or tap ("More").

## Checking
`python3 tools/check_glossary.py --build` enforces the word limits (plain 20, designer and engineer 30, designer_says and code_name 8), bans acronyms and jargon in the plain voice, and keeps the plain voice at a primary-school reading level (mean Flesch-Kincaid grade 6 or lower).
