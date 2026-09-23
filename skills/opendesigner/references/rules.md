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
10. **Play back before writing.** At each gate list the decisions with their D-numbers and a way to change each one.
11. **Stay short.** Essential answer first; detail on request; do not re-offer something the person declined.
12. **Interview in one session, build in a fresh one** when the conversation is long; the written spec carries the decisions.
13. **Hold the data, not a script.** Use the stage files for facts; phrase questions for this person and this product.

## 2. The question card
See SKILL.md for the layout. Details:
- **Header:** `D<n> · <short title> (<Q-id>, weight <w>, changes <fan-out> decisions)`. Number decisions from D1 in the order you ask; keep numbers stable.
- **Grounding:** one sentence connecting the choice to their product ("Your dashboard shows dense tables, so...").
- **Plain explanation:** two or three sentences a newcomer can follow. No jargon without a gloss.
- **Stakes:** one line on what goes wrong with a bad pick.
- **Options:** at most 4, recommended first, each with its visual effect in a few words and one real system. Put the rest behind "more options".
- **Recommendation:** "A because ..." tied to their earlier answers and the default's source.
- **Close:** "Reply with a letter, a value, 'show me', or your own answer."

## 3. Answer statuses
| Status | Meaning | How it gets recorded |
|---|---|---|
| `confirmed` | The person chose or explicitly accepted it | `engine.py pick/set ... --why "<their words>"` |
| `default` | Out of mode, or a Mechanical decision; nobody chose it | The engine's default; listed in the stage summary |
| `delegated` | The person said "you decide" | Recorded with your reason; listed at the direction gate and in the final summary |
| `assumed` | Owner input you could not ask (Quick mode) | Listed at the end for confirmation; never presented as decided |
| `locked` | Must not change without explicit consent (brand hexes, accessibility floors, anything they lock) | `engine.py lock <path>` |
| `from reference` | Pre-filled by opendesigner-extract | Becomes `confirmed` only when the person accepts it |
| custom | A value outside the listed options | Recorded with the person's reason |

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

## 7. The `OD:` copy-back grammar (DC-L18-07)
One line per decision, identical whether it arrives from a template button, a widget or typed by hand:
```
OD:<action> <target>=<value> <status>
```
- `action`: `pick` (answer a question), `set` (write a state path), `lock`, `remix`, `note`.
- `target`: a question id (`Q-shape-01`) for `pick` and `note`; a dotted state path for `set` and `lock` (`dials.roundness`, `raw.brandColor`, `raw.baseSize`, `hooks.H-logo.status`, `answers.Q-shape-01`); a dimension (`color`, `type`, `shape`, `depth`) for `remix`.
- `value`: an option value, a number, a hex color, or a JSON string in double quotes when it contains spaces or `=`.
- `status`: `confirmed`, `default`, `delegated` or `locked`; omitted on `note` and `remix`.
- Parse defensively: ignore text outside `OD:` lines, apply lines in order, and if a value is not a listed option, confirm it as a custom value before recording it.
- Examples: `OD:pick Q-depth-01=ring-shadow confirmed` · `OD:set raw.brandColor=#167874 locked` · `OD:remix color=soft` · `OD:note Q-dir-01="liked: soft, disliked: neo-brutalist"`.

## 8. Avoiding the generic AI look
Vendors and NN/g have documented that AI-made interfaces converge on the same few looks (L17 finding 4). Flag it once when a choice lands there; do not ban anything.
- Common tells: purple or blue-to-purple gradients; three-column icon-in-a-circle feature grids; everything centered; one bubbly radius on every element; decorative blobs and wavy dividers; emoji as decoration; a colored left border on every card; system-ui as the only voice on an expressive brand; glowing zero-offset shadows.
- Three recurring "default directions": cream background with a serif display and terracotta accent; near-black with one neon accent; newspaper hairlines with italic serif and tiny tracked mono. Each is fine when the brief asks for it.
- Spend boldness in one place: one signature element (a color, a typeface, a shape or a motion moment), tied to the memorable thing from Stage 0, and let everything else stay quiet.
- The fix for sameness is explicit decisions and the person's own assets, not a longer prompt.
