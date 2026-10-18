# 09 · Onboarding stepper · Mossby

Gallery: Sedge is a fictional payroll tool; this is step 3 of 6, setting paydays for a 14-person bike shop.

## Direction
Mossby is a fictional plant-care app for first-time plant owners, many of whom have already killed a plant and feel a bit guilty about it. Onboarding has four short steps (your space, your plants, your rhythm, all set) and should feel like a friendly storybook: pastel sage, peach, lilac and butter; ink-line plant drawings on soft blobs; a progress line that is a growing vine and sprouts a leaf for each finished step; very round cards and pill buttons; a guilt-free "I'm not sure yet" on every question.
Feel words: **friendly, cheerful, gentle** (all three known: friendly; playful + friendly; friendly + deferential).

## References (Mobbin, cited by link only)
- Monzo home type question, https://mobbin.com/screens/1515fc78-f9a2-4d80-a446-dc3567901f5c : illustrated choice cards with an "I'm not sure" escape hatch in the corner. Taught me the escape hatch and illustrated options.
- Fiverr freelancer type, https://mobbin.com/screens/f052d523-3364-4a0a-a51f-19d832b87cfd : ink line drawings over a single colour blob in a card grid. Taught me the line-art-on-blob technique.
- Insight Timer goal step, https://mobbin.com/screens/580ddba5-e7ec-4532-8c2e-fa6077a2f2a5 : segmented progress bar at the top and calm option rows. Taught me the compact phone progress pattern.
- Public risk step, https://mobbin.com/screens/9be926dd-7e14-4401-84cd-522daa8ab6f3 : "Step 4 of 6" overline above the question, radio cards with a sub-line. Taught me the step overline and option anatomy.

## System (engine)
`sketch --name "Mossby" --brand "#5fae7d" --audience regular --platforms web,ios --feel friendly,cheerful,gentle --theme system-light-dark --delegated all --surfaces experience`, then `set raw.accentCount 3`, `set raw.secondaryColors ["#f08a63", "#9b7be8"]` (peach, lilac).

| Dial | Value | Why |
|---|---|---|
| expression | 66 | illustrated, a little storybook |
| brandPresence | 70 | sage, pastels and the rounded face carry it |
| density | 25 | one question per screen; controls 40/48/56 |
| energy | 55 | gentle lift on hover, calm otherwise |
| roundness | 95 | controls full pill, containers 20, overlays 28 |
| depth | 35 | soft raised / floating only |
| colorfulness | 62 | pastel family |
| warmth | 85 | warm neutrals, caring |

Typefaces: `raw.displayFace "Fredoka"` (rounded display), `raw.textFace "Nunito"` (rounded humanist text), SIL OFL, licence recorded.

Illustrations through **opendesigner-illustrate**: `search "potted house plant" --slot onboarding` (82 candidates), `rank --style flat`, `sheet --candidates`, `fetch` four CC0 CocoMaterial drawings, `recolor --variants themed,tint --tokens ...`, `apply --to art --as svg --variant themed`, `ledger` (ATTRIBUTION.md in opendesigner/illustrations/). The page inlines the four SVGs (built from a template so the SVG markup stays out of the source by hand) and sets `--od-illus-neutral-1` per card to a pastel ramp step, so each drawing's fills take its card's colour.

## Where I stepped outside the tokens, and why
- Pastel fills are ramp steps 3–4 of accent, accent2, accent3 and warning (butter). The semantic roles only expose `bg.*-subtle` (step 3) for accent and status; there is no role for "decorative pastel", so I used ramps on purpose and named them `--sage/--peach/--lilac/--butter`.
- The phone frame bezel is neutral 12 at 6px and 36px radius (a device, not UI).
- Vine leaves use accent step 8; the dashed upcoming vine uses border.subtle.
- Continue's count bubble is 22% white on the action fill.

## Checks
- `engine.py validate`: no errors, 0 warnings, 5 notes.
- `preflight.py html --medium web`: 0 errors, 0 warnings — but only because it can read nothing: every size is a rem token and every family comes through `var()`, so it extracted no sizes and no families (see findings).
- `illustrate.py check art/plant-3.svg`: warn, one leftover #000000 not in the palette (invisible here; the path is covered).
- Contrast: body and option text use text.primary / text.secondary roles (engine-checked). Warning message text on warning subtle is the engine's checked pair. The disabled Continue is exempt. Step states never rely on colour alone: check, number, "!" and arrow glyphs plus labels.
- Targets: picks are 150×262 buttons, options 52px tall, pills 40–56px: all over 44px.
- Interaction: plant cards are `role="checkbox"` buttons (click, Space, Enter) and update the Continue count; Continue is `aria-disabled` at zero and shows a saving spinner; phone options are a radiogroup; the finished step is a link back; `aria-current="step"` on the current step. Reduced motion stops the spinner and leaf drift and zeroes transitions.

## Rounds
1. Card blobs were clipped into octagons by the pot's overflow; the first step label sat 3px higher than the others because only it was a link with padding.
2. Freed the blob, aligned the labels. Looked again at full size: the composition holds; the hovered Snake plant reads as lifted.

## Process findings
1. **The illustrate skill worked end to end and the result is good**, but its `--dir` means something different from the engine's `--dir`; using the same folder dumped search files into opendesigner/ and made `palette` lose the tokens. (feedback: confusing)
2. **Search and rank quality**: "house" matched birdhouses and houses for sale; `--style flat` still ranked heavy line doodles; `fetch` exited 1 on success; `apply --label` left rows unassigned. (feedback: bug)
3. **Recolor for pastel line art**: mono drawings map to neutral 1 and 12 only. Overriding the CSS variable per card was easy and is the strongest part of the skill's output. (feedback: idea)
4. **Preflight passes a fully tokenised page by default**, because it reads only px sizes and literal families. (feedback: bug)
5. **Secondary accents**: three-accent harmony gave grey teal and khaki at 24/36 of the primary chroma; `raw.secondaryColors` fixed it, but no question asks for named secondary colours. (feedback: gap)
6. Helped: roundness 95 gave pill controls and 20/28 containers that matched the direction exactly; density 25 gave 40/48/56 controls; Fredoka/Nunito went in through `raw.*Face` with no friction.

## Owner type and color rules (checked after the rule arrived)
- **Two fonts:** Fredoka (display: questions, step numbers, card names) and Nunito (everything else). Already compliant.
- **Type scale (6 sizes):** caption 13 (step labels, card hints, error text), body 16 (buttons, options), body-large 20 (lede, card names), title 25 (phone question, "Your jungle is set"), headline 39 (sheet number), display 49 (the step question). Adjacent steps are at least 20% apart.
- **Weight:** the question is Fredoka 600, chosen because the rounded face looks thin and timid at 400 on pastel; card names 600, body 400-700 Nunito.
- **No highlight trick** in any heading. **Color:** light warm-white background with near-black text and pastel fills; Warmth 85 tinted the neutrals slightly pink-cream, not brown, so no change.

## Round 4 (owner review, 2026-10-15)

**What he said.** Most of the web components "look absolutely rubbish", and none should "feel like they are from a vibe coded app or a cheap Chinese app". Margin (02) is the only component he does not call ugly; the B2B product screens are the bar. In round 3 he had called this piece "okay".

**The idea in one sentence:** a bike shop owner picks a pay schedule and sees this year's paydays, moved around bank holidays.

**What changed: a new concept, rebuilt in place.** The Mossby plant-care stepper (hand-drawn plants, a vine that grew a leaf per step, a phone mock, a column of button states) could not reach the B2B bar, so the folder now holds a different product with the same component type:
- **Sedge**, a fictional payroll service, setting up **Spokewright Cycles**, a 14-person bike shop in Oregon, at step 3 of 6, *Pay schedule*.
- The stepper rail: progress (2 of 6 done), two done steps with what was saved and an Edit link, the current step, and three steps to come.
- The step: how often (four choices, each with its paydays a year), first payday and first pay period, and a table of this year's five paydays with their approval deadlines. Bank holidays move dates the way a payroll service does, and each note sits under the date it explains: Veterans Day (Wed, Nov 11) moves an approval to Tue, Nov 10; Thanksgiving (Thu, Nov 26) moves one to Tue, Nov 24; Christmas (Fri, Dec 25) moves the payday to Thu, Dec 24.
- Footer: Back, "Next: Your team", Continue, aligned to the form column, with its rule level with the rail's.
- Colour: AUDIT-ROUND4 said the orange-red payroll flow read as Gusto, so the accent is now sedge green (#56701A, 5.6:1 with white), the plant the brand is named for. It has one job: the logo and the button to press. The chosen option and the current step are ink.
- Removed as clutter after the audits: the rail's subtitle, the descriptions of the current and future steps, the "Book a call" block, the holiday-notes column, the struck-through date, two of the four "save" words ("Exit setup", "Continue").

**References (Mobbin, cited by link only).**
- Mercury business onboarding, https://mobbin.com/screens/8b12e7b5-4bd6-4eea-9a61-7ebbcfa4f855 : a numbered step list beside one form column. Taught the rail and form split.
- ElevenLabs publishing flow, https://mobbin.com/screens/428640a6-8442-4468-9ffc-b3bb5ea62ecf : done steps keep a line saying what was saved. Taught the summary under each done step.
- Remote contractor flow, https://mobbin.com/screens/0d2b48f4-1904-4fe9-b335-a34ca87fbb68 : choice cards for one decision. Taught the frequency cards; ours sit in one row and carry their consequence.

**System (engine).** The Mossby system was replaced (git keeps it):
`sketch --name Sedge --brand "#D4421C" --audience regular --platforms web --feel friendly,calm,reliable --theme system-light-dark --delegated all --surfaces "setup:operate"`, then `set raw.textFace "Schibsted Grotesk"`, `raw.neutralTint pure`, `raw.numericStyles true`; dials roundness 45, depth 15, warmth 15, colorfulness 28, expression 35, energy 22 (all `delegated`); later `set raw.brandColor "#56701A" --set-by chosen` and `raw.primaryActionColor null`; `build`.
- Face: Schibsted Grotesk (SIL OFL), one family.
- Type scale, named roles (web px): label 12, body 14, title 18, headline 27. Weights 400, 500, 600.
- Outside the tokens on purpose: the 16 px radio, the 24 px step nodes, the 4 px progress track (no component tokens for them).
- Tabular figures were turned off in the table: in Schibsted Grotesk they put a gap before the comma in "Fri, Oct 30" (recorded with `engine.py feedback`).

**Checks (final render).**
- Dates: periods are two weeks, Sunday to Saturday, paid 6 days after they end; approvals are two business days before payday, skipping bank holidays; 5 runs left in 2026; 26 paydays a year. `check_dates.py --year 2026` passes.
- `check_names.py`: no collisions. New names: Sedge and Spokewright Cycles (web search found no payroll company called Sedge and no business called Spokewright). Christmas, Thanksgiving and Oregon are real holidays and a real state.
- `preflight.py html`: 0 errors, 0 warnings; sizes 12, 14, 18, 27.
- `engine.py validate`: no errors, 0 warnings.
- Computed contrast: 63 runs, lowest 5.63:1.
- Gallery size (337 px): the eye lands on the question and the chosen card, then the green button.

**Blind pairwise test** (ours against a shipped onboarding, sides random, fresh judges):

| Round | Version | Mercury | ElevenLabs | Remote |
|---|---|---|---|---|
| 1 | first build | ours +3 | +3 | +3 |
| 2 | unchanged | +3 | +3 | +3 |
| 3 | footer aligned, current step in ink, deeper button, one icon set | +3 | +3 | +3 |
| 4 | notes under their dates, rules aligned, new mark, fewer save words | +4 | +3 | +2 |
| 5 | final, sedge green, clutter removed | +3 | +3 | +3 |

**Fresh-eyes audit:** round 1, 4 (state said four ways on the Christmas row, repeated facts, a generic logo); round 2, 4 (two rules 30 px apart, a crude logo, an ambiguous notes column); round 3, **4**, "the closest to the B2B bar". Remaining notes from that audit, left for the owner: grey second lines on the choices and done steps, progress shown as a bar and as numbered steps, and a heavy table frame.

**Result: passes both tests.**
