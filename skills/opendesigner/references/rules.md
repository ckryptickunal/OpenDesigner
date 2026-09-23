# Interview rules

How to run the OpenDesigner interview well. Sources: `research/L18-ai-first-distribution.md` Part F and DC-L18-06 to 12, `research/L17-how-systems-get-made.md` Parts A and I, `synthesis/QUESTIONNAIRE.md` (interview protocol). The mechanics adopted from gstack (MIT) and impeccable (Apache-2.0) are described here in our own words, not copied.

## 1. Message style
- **First message: 3 lines at most.** Say what you will do, that it starts with 5 quick questions, then ask the first one. If you already read their repo, one of the lines says what you found.
  > Hi! I'll help you set up your design system: the colors, text, spacing and parts your app uses.
  > We start with 5 quick questions and you get a complete first version. You can go deeper anywhere later.
  > First: what are you making?
- **One idea and one question per message.** Short sentences. No walls of text, no long lists unless asked.
- **Plain words first.** Every term gets its plain meaning the first time (section 2). Skip jargon where a plain word works.
- **Details on request.** Say "why?" or "tell me more" for sources, real systems and trade-offs. Don't volunteer them all at once.
- **Show, then ask.** When the host can show a visual, the visual carries the detail and the message stays short.
- **Never repeat an offer** the person declined.

## 2. Three voices (BRIEF requirement 12; `synthesis/THREE-VOICES.md`)
Every term has three explanations in `glossary.json` (one term per line; search for the term or one of its `aliases`): `plain` (a school student follows it), `designer` and `engineer`, plus two short labels, `designer_says` and `code_name`.
1. **First mention in a session:** the plain sentence, then one short line with the other two voices.
   > The accent color is the one color used for buttons and highlights.
   > Designers: primary or brand accent · Code: `color.bg.accent`
2. **After that, the term name only.** Don't explain the same term twice unless asked.
3. **Switching the lead voice.** When someone says "talk like a designer" or "talk like an engineer", that voice leads on first mentions. Record it with `engine.py set profile.voice '"designer"'` (or `"engineer"` / `"plain"`), and read it back at the start of later sessions. Plain stays available on request.
4. **"Explain fully"** shows all three full voices for that one term. That is the only time all three appear together.
5. **Same words every time.** Use the glossary's `term` in messages and files. Accept `aliases` as input, but answer with the `term`.
6. **If `glossary.json` is missing** (the glossary is still being written), give the plain meaning in your own words, keep it under 20 words, and add the short line only if you are sure of it.
7. **In files:** DESIGN.md decisions open with one plain sentence and the short line, with the rest collapsed. RATIONALE.md is plain first, then designer. Tokens and code comments use the engineer voice.

## 3. The rules, in the order they matter
1. **Look before you ask.** Read the repo, CSS, tokens, brand files and any reference first. Ask only about taste, trade-offs and facts no file holds. If there are several candidates (two blues in the CSS), list them and recommend one.
2. **Every question must change the system, lock an assumption, or pick a trade-off.** For low-impact gaps, assume and label the assumption instead of asking.
3. **Zoom, don't march.** Level 0 first for everyone, then only the areas the person wants (`zoom.md`). Offer "stop here, or zoom into X" after every level.
4. **Order by downstream reach.** Product truth first (what it is, who it's for, where it runs, how it feels), then foundations, then components.
5. **Offer 2 to 4 real options, recommend one with a short reason, and always allow a free answer.** Real systems that use each option are in the stage files. Show them when asked "why?", or when the designer voice leads.
6. **Ask for examples, including one they dislike.** Do this once, when they zoom into direction, color, type, corners or motion.
7. **Word questions neutrally.** The recommendation lives in the options, not in the question.
8. **Record honestly.** A recommendation you made is not an answer you received (statuses below).
9. **Play back before writing outside `opendesigner/`.** List the decisions (question id, value, how it was set) with a way to change each.
10. **Interview in one session, build in a fresh one** when the conversation is long. The written files carry the decisions.
11. **Hold the data, not a script.** Use the stage files for facts, and phrase questions for this person and this product.

## 4. The question card
One message:
```
Corners: how soft should they be?
Rounder corners feel friendlier; square corners feel precise.
Designers: corner radius · Code: border-radius
  A) Slightly rounded, 6 px (recommended: your app is a busy work tool)
  B) Rounded, 12 px
  C) Square, 2 px
  D) Pill-shaped
Pick one, say "show me", or tell me what you want.
```
- The short "Designers · Code" line appears only the first time the term comes up.
- The question id (Q-shape-01) is the stable handle for later changes ("change Q-shape-01"). Show it only when the engineer voice leads or the person asks. The engine numbers log entries D-0001, D-0002 and so on.
- Put the recommended option first. Keep the rest behind "more options". Weight `high` questions get one extra line on what the choice changes elsewhere. Nothing else.

## 5. Answer statuses (`--set-by`)
| Status | Meaning | Record with |
|---|---|---|
| `chosen` | The person picked it (default) | `engine.py set <path> <value> --why "<their words>"` |
| `confirmed_default` | The person accepted your recommended default | `--set-by confirmed_default` |
| `auto_default` | Out of mode, or a Mechanical decision nobody looked at | nothing to run: the default stands; list it in the stage summary |
| `delegated` | The person said "you decide" | `--set-by delegated --why "<your reason>"`; list it at the next gate and in the final summary |
| `assumed` | Owner input you could not ask (Quick mode) | `--set-by assumed`; list it at the end for confirmation; never present it as decided |
| `reference` | Accepted from a reference | `--set-by reference --source-ref <ref-id>` (opendesigner-extract) |
| `asset` | Derived from an asset the person supplied (for example brand color from the logo) | `--set-by asset` |
| locked | Must not change without explicit consent (brand hexes, accessibility floors, anything they lock) | `--lock` on the set, or `engine.py lock <path>` |

A value outside the listed options is recorded as given, with the person's reason in `--why`.

## 6. Sorting decisions
- **Mechanical:** one right answer given earlier choices or a rule (nested radius, on-color text, contrast steps). Decide silently with the default; mention it in the stage summary.
- **Taste:** reasonable people disagree. Ask with a recommendation; if delegated, decide and flag it at the next gate.
- **User challenge:** your recommendation would override something the person said. Never decide it. Present: what they said, what you suggest, why, what you might be missing, the cost if you are wrong. Their answer wins.
- A coherence clash after an override (for example a brutalist direction with bouncy motion) is flagged once, never blocked.

## 7. When answers are vague, skipped or conflicting
- **Vague taste words** ("clean", "modern", "premium"): turn them into 3 to 5 precise visual keywords (for example "clean" becomes "neutral surfaces, one accent, 1 px borders, generous whitespace") and confirm before generating.
- **"You decide" / "skip":** take the default, record `delegated`. For a high fan-out owner input (scope, platforms, audience), push back once: ask only the one or two parts that matter most. If they decline again, respect it and mark it `assumed`.
- **Conflicting answers** inside one cycle: show both answers and the conflict, settle it with their ranked principles (Q-brand-07). Never average silently.
- **Changing an earlier decision:** re-run `generate` and name the downstream decisions that moved (`graph.json` → edges).

## 8. Summaries and the offer after each level
After each level or area, write 2 to 4 plain sentences a teammate could read. For example: "We chose slightly rounded 6 px corners because the app is a busy work tool; cards use 8 px." The engine logs each `set` with its `--why` in `opendesigner/decisions.md`, and DESIGN.md is refreshed after every confirmed decision (`zoom.md`). Then make the offer: stop here, or zoom into at most 3 named areas. Before writing anything outside `opendesigner/`, play the decisions back and get a yes.

## 9. The `OD:` copy-back grammar (spec 3.7, DC-L18-07)
One line per decision, identical whether it arrives from a template button, a widget, a click or a typed reply, and mapped one-to-one onto `engine.py`:
```
OD:set <path>=<json-value> [--why "reason"]     path: a question id (Q-shape-01), dials.<name>, raw.<input>, hooks.<H-id>.status, or a token path
OD:lock <path>          OD:unlock <path>          protect or release a decision (unlock only with consent)
OD:accept <ref-id>:<path>    OD:ignore <ref-id>:<path>    act on a value pre-filled from a reference
OD:remix <dimension>=<option-value>             option gallery only: take color, type, shape or depth from another option
```
- Values are JSON: strings in double quotes (`"subtle"`, `"#167874"`), numbers bare (`45`). The engine also accepts a bare word.
- Parse defensively: ignore text outside `OD:` lines, apply lines in order, and if a value is not a listed option, confirm it as a custom value before recording it.
- Examples: `OD:set Q-depth-01="ring-shadow"` · `OD:set dials.roundness=45 --why "a bit softer"` · `OD:lock raw.brandColor` · `OD:remix color="soft"`.

## 10. Avoiding the generic AI look
Vendors and NN/g have documented that AI-made interfaces converge on the same few looks (L17 finding 4). Flag it once when a choice lands there; do not ban anything.
- Common tells: purple or blue-to-purple gradients; three-column icon-in-a-circle feature grids; everything centered; one bubbly radius on every element; decorative blobs and wavy dividers; emoji as decoration; a colored left border on every card; system-ui as the only voice on an expressive brand; glowing zero-offset shadows.
- Three recurring "default directions": cream background with a serif display and terracotta accent; near-black with one neon accent; newspaper hairlines with italic serif and tiny tracked mono. Each is fine when the brief asks for it.
- Spend boldness in one place: one signature element (a color, a typeface, a shape or a motion moment), tied to the memorable thing from Stage 0, and let everything else stay quiet.
- The fix for sameness is explicit decisions and the person's own assets, not a longer prompt.
