# Interview rules

How to run the OpenDesigner interview. Sources: `research/L18-ai-first-distribution.md` Part F and DC-L18-06 to 12, `research/L17-how-systems-get-made.md` Parts A and I, and `synthesis/QUESTIONNAIRE.md` (interview protocol). The mechanics adopted from gstack (MIT) and impeccable (Apache-2.0) are described here in our own words, not copied.

## 1. Message style
- **First message: 3 lines at most.** Say what you will do and that it starts with 5 quick questions. Then ask the first one. If you already read their repo, one line says what you found.
  > I'll help you set up your design system: the colors, text, spacing and parts your app uses.
  > We start with 5 quick questions, and you get a complete first version. You can go deeper anywhere later.
  > First: what are you making?
- **One idea and one question per message.** Short sentences. No walls of text, and no long lists unless asked.
- **Plain words first.** Every term gets its plain meaning the first time (section 2). Skip jargon where a plain word works.
- **Details on request.** Give sources, real systems and trade-offs when the person says "why?" or "tell me more". Don't volunteer them all at once.
- **Show, then ask.** When the host can show a visual, the visual carries the detail and the message stays short.
- **Never repeat an offer** the person declined.

## 2. Three voices (BRIEF requirement 12; `synthesis/THREE-VOICES.md`)
Search `glossary.json` for each term (one term per line; match the term or one of its `aliases`). Each entry has three explanations: `plain` (a school student follows it), `designer` and `engineer`. It also has two short labels: `designer_says` and `code_name`.
1. **First mention in a session:** the plain sentence, then one short line with the other two voices.
   > The accent color is the one strong color used for main buttons and for things you pick.
   > Designers: primary or brand accent · Code: `color.bg.accent`
2. **After that, the term name only.** Don't explain the same term twice unless asked.
3. **Switching the lead voice.** "Talk like a designer" or "talk like an engineer" makes that voice lead on first mentions. Record it with `engine.py set profile.voice '"designer"'` (or `"engineer"` / `"plain"`), and read it back at the start of later sessions. Plain stays available on request.
4. **"Explain fully"** shows all three full voices for that one term. That is the only time all three appear together.
5. **Same words every time.** Use the glossary's `term` in messages and files. Accept `aliases` as input, but answer with the `term`.
6. **If a term is not in `glossary.json`,** give the plain meaning in your own words, under 20 words. Add the short line only if you are sure of it.
7. **In files:** DESIGN.md decisions open with one plain sentence and the short line, with the rest collapsed. RATIONALE.md is plain first, then designer. Tokens and code comments use the engineer voice.

## 3. The rules, in the order they matter
1. **Look before you ask.** Read the repo, CSS, tokens, brand files and any reference first. Ask only about taste, trade-offs and facts no file holds. If there are several candidates (two blues in the CSS), list them and recommend one.
2. **Every question must do one of three things:** change the system, lock an assumption, or pick a trade-off. For small gaps, don't ask: assume, and label the assumption.
3. **Zoom, don't march** (`zoom.md`).
4. **Order by downstream reach.** Product truth first (what it is, who it's for, where it runs, how it feels), then foundations, then components.
5. **Offer 2 to 4 real options.** Recommend one with a short reason, and always allow a free answer. The stage files list real systems that use each option. Show them when asked "why?" or when the designer voice leads. At the style screen (Q-dir-01), give 2 or 3 **safe choices** and at least 2 **risks**. Say what each one gains and what it costs. Directions must differ in type, palette and shape.
6. **Ask for examples, including one they dislike.** Do this once, when they zoom into direction, color, type, corners or motion.
7. **Word questions neutrally.** The recommendation lives in the options, not in the question.
8. **Record honestly.** A recommendation you made is not an answer you received (section 5).
9. **Play back before writing outside `opendesigner/`.** List the decisions (question id, value, how it was set) with a way to change each, and get a yes.
10. **Interview in one session, build in a fresh one** when the conversation is long. The written files carry the decisions.
11. **Hold the data, not a script.** Take facts from the stage files, and phrase questions for this person and this product.

## 4. The question card
One message:
```
How round should corners be?
Corner radius is how round the corners of a box or button are. Rounder feels friendly; square feels precise.
Designers: corner radius, sharp to pill · Code: radius.control, CSS border-radius
  A) Slightly rounded, 6 px (recommended: your app is a busy work tool)
  B) Rounded, 12 px
  C) Square, 2 px
  D) Pill-shaped
Pick one, say "show me", or tell me what you want.
```
- The plain sentence and the "Designers · Code" line appear only the first time the term comes up.
- The question id (Q-shape-01) is the stable handle for later changes ("change Q-shape-01"). Show it only when the engineer voice leads or the person asks. The engine numbers log entries D-0001, D-0002 and so on.
- Put the recommended option first, and keep the rest behind "more options". Questions with weight `high` get one extra line on what the choice changes elsewhere. Nothing else.

## 5. Answer statuses (`--set-by`)
| Status | Meaning | Record with |
|---|---|---|
| `chosen` | The person picked it (default) | `engine.py set <path> <value> --why "<their words>"` |
| `confirmed_default` | The person accepted your recommended default | `--set-by confirmed_default` |
| `auto_default` | A question nobody reached, or a Mechanical decision nobody looked at | nothing to run: the default stands; list it in the stage summary |
| `delegated` | The person said "you decide" | `--set-by delegated --why "<your reason>"`; list it at the next gate and in the final summary |
| `assumed` | Owner input you could not ask (the person stopped before zoom 2) | `--set-by assumed`; list it at the end for confirmation; never present it as decided |
| `reference` | Accepted from a reference | `--set-by reference --source-ref <ref-id>` (opendesigner-extract) |
| `asset` | Derived from an asset the person supplied (for example brand color from the logo) | `--set-by asset` |
| locked | Must not change without explicit consent (brand hexes, accessibility floors, anything they lock) | `--lock` on the set, or `engine.py lock <path>` |

A value outside the listed options is recorded as given, with the person's reason in `--why`.

## 6. Sorting decisions
- **Mechanical:** one right answer, given earlier choices or a rule (nested radius, on-color text, contrast steps). Decide silently with the default, and mention it in the stage summary.
- **Taste:** people can fairly disagree. Ask with a recommendation. If delegated, decide and flag it at the next gate.
- **User challenge:** your recommendation would override something the person said. Never decide it. Present what they said, what you suggest, why, what you might be missing, and the cost if you are wrong. Their answer wins.
- If an override makes two choices clash (for example a brutalist direction with bouncy motion), flag it once. Never block it.

## 7. When answers are vague, skipped or conflicting
- **Vague taste words** ("clean", "modern", "premium"): turn them into 3 to 5 precise visual keywords, and confirm before generating. For example, "clean" could become "gray surfaces, one accent color, thin 1 px borders, lots of space".
- **"You decide" / "skip":** take the default and record `delegated`. For a high fan-out owner input (scope, platforms, audience), push back once: ask only the one or two parts that matter most. If they decline again, respect it and mark it `assumed`.
- **Conflicting answers** inside one cycle: show both answers and the conflict. Settle it with their ranked principles (Q-brand-07). Never quietly split the difference.
- **Changing an earlier decision:** re-run `generate` and name the downstream decisions that moved (`graph.json` → edges).

## 8. Summaries and the offer after each level
After each level or area, write 2 to 4 plain sentences a teammate could read. For example: "We chose slightly rounded 6 px corners, because the app is a busy work tool. Cards use 8 px." The engine logs each `set` with its `--why` in `opendesigner/decisions.md`. Then make the offer (`zoom.md`): stop here, or zoom into at most 3 named areas.

## 9. `OD:` lines (spec 3.7, DC-L18-07)
One line per decision. A line looks the same whether it comes from a template button, a widget, a click or a typed reply. Each line maps to one engine command:
| Line | Run |
|---|---|
| `OD:set <path>=<json-value> [--why "reason"]` | `engine.py set '<path>=<json-value>' --why "reason"`. The path is a question id (Q-shape-01, which records an answer), `dials.<name>`, `raw.<input>`, `hooks.<H-id>.status`, or a token path |
| `OD:lock <path>` / `OD:unlock <path>` | `engine.py lock <path>` / `engine.py unlock <path>`. Unlock only with consent |
| `OD:accept <ref-id>:<path>` | `engine.py set <path> <value> --set-by reference --source-ref <ref-id>`, for a value pre-filled from a reference |
| `OD:ignore <ref-id>:<path>` | Nothing: the pre-filled value is dropped |
| `OD:remix <dimension>=<option-value>` | Option gallery only: take that dimension (color, type, shape or depth) from the named option, and `set` its values |

- Values are JSON: strings in double quotes (`"subtle"`, `"#167874"`), numbers bare (`45`). The engine also accepts a bare word.
- Parse defensively. Ignore text outside `OD:` lines, and apply lines in order. If a value is not a listed option, confirm it as a custom value before recording it.
- Examples: `OD:set Q-depth-01="ring-shadow"` · `OD:set dials.roundness=65 --why "a bit softer"` · `OD:lock raw.brandColor` · `OD:remix color="soft"`.

## 10. Avoiding the generic AI look
Vendors and NN/g have documented that AI-made interfaces converge on the same few looks (L17 finding 4). Flag it once when a choice lands there. Don't ban anything.
- Common tells:
  - purple or blue-to-purple gradients
  - three-column feature grids with an icon in a circle
  - everything centered
  - one bubbly radius on every element
  - decorative blobs and wavy dividers
  - emoji as decoration
  - a colored left border on every card
  - system-ui as the only voice on an expressive brand
  - glowing shadows with no offset
- Three "default directions" keep coming back. Each is fine when the brief asks for it:
  - a cream background with a serif display and a terracotta accent
  - near-black with one neon accent
  - newspaper hairlines with an italic serif and tiny tracked mono
- Spend boldness in one place: one signature element (a color, a typeface, a shape or a motion moment). Tie it to the memorable thing (Q-brand-02), and let everything else stay quiet.
- The fix for sameness is explicit decisions and the person's own assets, not a longer prompt.
