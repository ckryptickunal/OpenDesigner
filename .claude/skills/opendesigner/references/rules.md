# Interview rules

How to run the OpenDesigner interview well. Sources: `research/L18-ai-first-distribution.md` Part F and DC-L18-06 to 12, `research/L17-how-systems-get-made.md` Parts A and I, `synthesis/QUESTIONNAIRE.md` (interview protocol). The mechanics adopted from gstack (MIT) and impeccable (Apache-2.0) are described here in our own words, not copied.

## 1. The rules, in the order they matter
1. **Look before you ask.** Read the repo, CSS, tokens, brand files and any reference first. Ask only about taste, trade-offs and facts no file holds. If several candidates exist (two blues in the CSS), list them and recommend one.
2. **Every question must change the system, lock an assumption, or pick a trade-off.** For low-impact gaps, assume and label the assumption instead of asking.
3. **One high-impact decision per turn.** Group up to three small related ones. On a cycle screen (the stage header names the linked decisions) one form with all of them is fine, because they constrain each other.
4. **Order by downstream reach.** Product truth first (audience, the job of the design, constraints), then one visual direction, then foundations, then components. No color or font questions during product intake.
5. **Offer 2 to 4 real options, recommend one with a one-line reason, always allow free text.** State reasons as "X because Y". Name a real system that uses each option (they are in the stage files).
6. **Show, do not describe.** Use the visual ladder in SKILL.md. Every visual carries its text equivalent.
7. **Ask for examples, including one they dislike.** At the start of each visual stage (direction, color, type, shape, motion), ask for 1 to 3 references they like and 1 they don't.
8. **Word questions neutrally.** The recommendation lives in the options, not in the question.
9. **Record honestly.** A recommendation you made is not an answer you received (statuses below).
10. **Play back before writing.** At each gate list the decisions (question id, value, status) and a way to change each one.
11. **Stay short.** Essential answer first; detail on request; do not re-offer something the person declined.
12. **Interview in one session, build in a fresh one** when the conversation is long; the written spec carries the decisions.
13. **Hold the data, not a script.** Use the stage files for facts; phrase questions for this person and this product.

## 2. The question card
See SKILL.md for the layout. Details:
- **Header:** `<Q-id> · <short title> (weight <w>, changes <fan-out> decisions)`. The question id is the stable handle across sessions ("change Q-shape-01"); the engine's log numbers entries D-001, D-002.
- **Grounding:** one sentence connecting the choice to their product ("Your dashboard shows dense tables, so...").
- **Plain explanation:** two or three sentences a newcomer can follow. No jargon without a gloss.
- **Stakes:** one line on what goes wrong with a bad pick.
- **Options:** at most 4, recommended first, each with its visual effect in a few words and one real system. Put the rest behind "more options".
- **Recommendation:** "A because ..." tied to their earlier answers and the default's source.
- **Close:** "Reply with a letter, a value, 'show me', or your own answer."

## 3. Answer statuses (`--set-by`)
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

## 4. Sorting decisions
- **Mechanical:** one right answer given earlier choices or a rule (nested radius, on-color text, contrast steps). Decide silently with the default; mention it in the stage summary.
- **Taste:** reasonable people disagree. Ask with a recommendation; if delegated, decide and flag it at the next gate.
- **User challenge:** your recommendation would override something the person said. Never decide it. Present: what they said, what you suggest, why, what you might be missing, the cost if you are wrong. Their answer wins.
- A coherence clash after an override (for example a brutalist direction with bouncy motion) is flagged once, never blocked.

## 5. When answers are vague, skipped or conflicting
- **Vague taste words** ("clean", "modern", "premium"): turn them into 3 to 5 precise visual keywords (for example "clean" becomes "neutral surfaces, one accent, 1 px borders, generous whitespace") and confirm before generating.
- **"You decide" / "skip":** take the default, record `delegated`. For a high fan-out owner input (scope, platforms, audience), push back once: ask only the one or two parts that matter most. If they decline again, respect it and mark it `assumed`.
- **Conflicting answers** inside one cycle: show both answers and the conflict, settle it with their ranked principles (Q-brand-07). Never average silently.
- **Changing an earlier decision:** re-run `generate` and name the downstream decisions that moved (`graph.json` → edges).

## 6. Stage summaries and gates
After each stage, write 2 to 5 plain sentences a teammate could read ("We chose subtle 6 px corners because the product is a dense work tool; cards use 8 px."). The engine appends each `pick`/`set` with its `--why` to `opendesigner/decisions.md`; add the summary to your reply.
Gates: after stages 01-05 (scope, with the block map tagged G/E/D/T/I), after 06-08 (direction), after the asset checklist (03). Quick mode keeps only the direction gate. End with the coverage check.

## 7. The `OD:` copy-back grammar (spec 3.7, DC-L18-07)
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

## 8. Avoiding the generic AI look
Vendors and NN/g have documented that AI-made interfaces converge on the same few looks (L17 finding 4). Flag it once when a choice lands there; do not ban anything.
- Common tells: purple or blue-to-purple gradients; three-column icon-in-a-circle feature grids; everything centered; one bubbly radius on every element; decorative blobs and wavy dividers; emoji as decoration; a colored left border on every card; system-ui as the only voice on an expressive brand; glowing zero-offset shadows.
- Three recurring "default directions": cream background with a serif display and terracotta accent; near-black with one neon accent; newspaper hairlines with italic serif and tiny tracked mono. Each is fine when the brief asks for it.
- Spend boldness in one place: one signature element (a color, a typeface, a shape or a motion moment), tied to the memorable thing from Stage 0, and let everything else stay quiet.
- The fix for sameness is explicit decisions and the person's own assets, not a longer prompt.
