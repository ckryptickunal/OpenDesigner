# 02 · Lullwater: sleep session

## Direction
Lullwater is a fictional sleep and wind-down app: short sleep stories and breathing guides for people who lie awake. The session screen is the last thing you see before sleep, so it must feel like dusk over still water: indigo sky, a warm peach orb that breathes, a large calm serif timer, nothing sharp. Feel words: **calm, gentle, dreamy** ("dreamy" is not in the engine's word list; it asked about it instead of guessing).

Shape language: circles and pills only, frosted glass controls. Type: Instrument Serif (one weight plus italic) for the title, breath cue and timer; Instrument Sans for the controls.

## References (Mobbin, structure only)
- https://mobbin.com/screens/ce233a53-df97-4728-9f14-9cab30bc9d4c (a meditation player): a large serif timer as the main reading, not a tiny scrubber time. Taught that the timer can be the hero type.
- https://mobbin.com/screens/17b0bfe1-6fdd-4564-8af8-828391ce17c8 (a meditation player): a full-bleed grainy gradient with the transport row low on the screen. Taught the grain and the bottom-weighted controls.
- https://mobbin.com/screens/a74c67ce-b01a-4028-83f0-089584a1a539 (a breathing session): one soft object in the centre as the focus. Taught the single-focus composition.
- https://mobbin.com/screens/aa9f9f64-c356-4967-9aa9-ea0b6cb5df78 (a session timer sheet): the sleep-timer idea ("fades out by 23:40") as a secondary line rather than a separate screen.

## System (engine)
```
sketch --name "Lullwater" --brand "#E8A48A" --audience regular --platforms ios --feel calm,gentle,dreamy --theme system-light-dark --delegated all
pick Q-color-01 keep-hex · set raw.brandColor "#E8A48A" (restored) · set raw.neutralBase "#231E4A" · pick Q-color-21 near-black
pick Q-color-04 analogous · set raw.secondaryColors ["#C77DA8", "#7E6CC9"]   (rose and lavender ramps for the sky)
pick Q-depth-01 glass · pick Q-depth-04 control-layer · pick Q-motion-01 none
pick Q-type-01 brand-display · raw.displayFace "Instrument Serif" · raw.textFace "Instrument Sans" · pick Q-type-02 yes · pick Q-type-08 17
set overrides.type.displayReach 6   (a 95 px step for the timer)
```
Dials: expression 75 (the orb and timer perform), brandPresence 65, density 15 (one thing at a time), energy 5, roundness 95 (pills: `--ds-radius-control` is full), depth 90 (glass; see findings), colorfulness 60, warmth 75.

Rendered in the system's dark mapping (`data-theme="dark"`).

## Fonts
Instrument Serif and Instrument Sans (both SIL OFL) from Google Fonts.

## Where I went outside the tokens, and why
- **The sky, bay and orb are canvas art.** Every color is read from the generated ramps at run time (`accent`, `accent2` rose, `accent3` lavender, `neutral`); only the in-between mixes are computed. A 14-level film grain is added over it.
- **Display weight 400 instead of the token heading weight 600 / display 700**: Instrument Serif has only one weight, so the tokens would ask for a faux bold.
- The "15" inside the skip icons was 10 px; it is now 11 px (Caption 2), the rule's minimum.
- The play button is 80 pt, a size the spacing ladder has (80) but no control token covers.

## Checks
- `engine.py validate`: 0 errors, 2 warnings (light mode only: the peach primary on near-white page).
- `engine.py review`: 23 values (final), nearly all element sizes, glow rings and canvas mixing colors (it suggests `--ds-color-surface-raised` for the `#ffffff` used to lighten the orb highlight).
- `preflight.py html --medium web`: 3 errors: the two Google Fonts faces "have no @font-face" (they load through `<link>`), and the 10 px icon numeral.
- Contrast sampled from the render: "Night 3 of 7" in text.tertiary was **4.15:1** on the painted sky, so I moved it to text.secondary (5.44:1). Title on sky 9.41:1; small text over the bay 5.57:1; pause icon on the peach 8.77:1.
- Targets: top buttons 44, skip 56, play 80, side buttons 44, mix pill 48 tall.
- Three full-size review rounds: (1) the glass buttons were invisible because `all: unset` came after `.glass` in the cascade, and the mix pill sat on the home indicator; (2) the sky was a flat purple fog and the orb's lower half went grey-brown, so I added the rose and lavender ramps through the engine and a horizon with the orb's reflection; (3) stars landed inside text ("Night 3.of 7" read as a full stop), so stars now avoid text bands, and the reflection was shortened to sit above the timer.

## Process findings
1. **Bug (again): the sketch darkened the brand hex** `#E8A48A` to `#a4654d` "a brown". The Q-color-01 stage file itself says a light brand color should switch its button text to dark instead.
2. **Confusing: a dial silently undid an answer.** `pick Q-depth-01 glass` sets depth 90; my later `set dials.depth 45` removed the glass tokens and DESIGN.md then said both "Materials and glass" and "No materials or glass in this system".
3. **Bug: single-weight faces get bold styles.** Display styles carry weight 600/700 even for Instrument Serif, which has only 400.
4. **Gap: no contrast check for text over art.** Text roles are guaranteed only on generated surfaces 1-4; on the painted sky text.tertiary failed (4.15:1) and nothing in validate, review or preflight could see it.
5. **Helped:** Q-color-04 `analogous` plus `raw.secondaryColors` produced full rose and lavender ramps, so the whole dusk gradient stayed in the system. The glass tokens (`--ds-color-surface-glass`, its fallback and `--ds-material-glass-blur`) are exactly what a frosted iOS control needs.
6. Preflight again flagged Google Fonts `<link>` faces and had no app medium.

## Revision for the owner's type and color rules (mid-run)
Type scale (Apple HIG roles, through the engine as in piece 01):

| Role | Size / line | Used for |
|---|---|---|
| Display (custom) | 95, Instrument Serif 400 | the timer |
| Large Title | 34 / 38, Instrument Serif italic | the story title (the whole title, not one word) |
| Title 2 | 22, Instrument Serif italic | the breath cue in the orb |
| Body | 17 / 22 | "Sleep story · told by…", the sound-mix pill, status bar |
| Footnote | 13 / 18 | the crumb, "left · fades out by 23:40", elapsed and total time, "4 · 7 · 8" |
| Caption 2 | 11 | the "15" inside the skip icons |

Changes made for the rules:
- Title 40 → 34 (Large Title); cue 23 → 22; subtitle and mix pill 13-15 → 17 (Body); small labels → 13 (Footnote); skip numerals 10 → 11.
- The status bar time used the system font, a third face; it now uses Instrument Sans. Two fonts in the piece.
- Color: dark dusk sky with bright text; nothing changed (title on sky 9.41:1, smallest text 5.44:1 or more).

Replaced on 2026-10-14 by app-screens/11-approvals-mobile after the Mobbin audit (score 2).

## Round 3 (2026-10-15): the clock and the timer
Found by the fresh audit of `mockups/01-phone-trio`, which shows this screen.
- **The status bar said 9:41, but the screen is set at night:** "left · fades out by 23:40" with 18:24 left meant about 23:21. The clock now reads the time the screen implies.
- **"18:24" was also `watch/08-onething-focus`'s timer** (reused invented data, `making.md` section 11). The session is now 13:08 played and **16:52** left of 30:00 (13:08 + 16:52 = 30:00), so the clock is **23:22** (23:22:08 + 16:52 = 23:40, "fades out by 23:40"). The progress fill and knob moved from 39% to 43.8% (788 of 1,800 s), and the timer's and slider's accessible labels say the same.
- Re-rendered `shot.png` (390 × 844 at 3×) through `../../mockups/render_still.py` (reduced motion, so the breathing orb is captured at its still frame); everything else is unchanged. `check_dates.py --year 2026` passes.

## Round 4 (owner review, 2026-10-15)
**What he said** about all the app screens: they "look absolutely shit. None of them should feel like they are from a vibe coded app or a cheap Chinese app." The audit before it had said "remake": a glowing orb on an indigo-to-peach sky with rings, stars and a reflection, the canonical AI "calm app" image, and two heroes competing. `AUDIT-ROUND4.md` adds that mockups/01 still shows that orb.

**The idea in one sentence:** at 23:22 a sleep story is playing, and the screen says how long is left and when it will fade out.

**What changed (a rebuild in place; same product, story, clock and timer):**
- **A photograph instead of painted art.** The canvas sky, orb, rings, stars, reflection, play-button glow and glass pill are gone. The story's artwork is a free Unsplash photo of still water at blue hour (Jörg Angeli, "Body of water at night", `photo-1546273735-bea2e41924f1`; the page says "Free Photo on Unsplash"; no people, no logos), cropped so the horizon sits at about 200 pt and graded toward night with a CSS filter. Two gradients carry legibility only: a top scrim for the status bar and nav, and a fade into the page under the title. The title block sits on the photo.
- **One confident number:** "16:52" left at 112 pt, Albert Sans Light. One face for everything: the serif timer and title were dropped in the last round, because a sans title beside serif numerals read as "an unresolved mix" and a big serif countdown under a night photo is Insight Timer's signature.
- **One accent with one job, the sleep timer:** peach only on the moon button and "Fades out by 23:40". The play button is a plain white disc, the scrubber is white on grey.
- **Fewer numbers:** the elapsed and total labels under the scrubber and "30 min" are gone; the clock, the time left and the fade-out time remain.
- **Controls:** iOS-style 15-second glyphs (open arc and chevron), one rendered 1.75 stroke for every icon (`vector-effect: non-scaling-stroke`), five controls on equal centres (33, 114, 195, 276, 357 pt) with the outer glyphs on the 24 pt text edges; the right control is audio output (the AirPlay audio shape, outlined). The rain layer is a 17 pt row with an iOS-sized slider (24 pt thumb).
- **Narrator renamed:** Ines Calder became **Oona Prentice**. `check_names.py` showed "Calder" belongs to "41 Calder Street" (`styles/03`) and "Ines" to "Ines Valcourt" (`app-screens/08`).
- **Kept:** the clock 23:22 and 16:52 left of 30:00 (13:08 + 16:52 = 30:00, the scrubber at 43.8%; 23:22:08 + 16:52 = 23:39:00, so "Fades out by 23:40"), "Low tide at Merrow Bay", "Wind Down · Night 3 of 7", "Rain on the reed beds" at 40%.
- **Tried and dropped:** a full-bleed dusk mudflat photo (judged muddy), and a narration waveform with the fade drawn in peach (one auditor asked for it, the next called it decoration).

**System through the engine:** `raw.textFace "Albert Sans"` (first Inter; an auditor called Inter with Source Serif "the default AI pairing"), `raw.displayFace "Albert Sans"` (first Source Serif 4), `raw.neutralBase "#1C2430"` (slate instead of violet-indigo), `raw.accentCount 1`, `raw.secondaryColors []`, brand `#E8A48A` kept as typed; dials expression 45, brandPresence 40, colorfulness 30, depth 55, energy 5, density 30; `overrides.font.size` 11, 13, 15, 17, 28, 76 and 112; `build` passes.

**Type roles (iOS), one face, Albert Sans:** Timer 112 (300) · Title 1 28 (500, the story title) · Body 17 (narrator, "left", the fade line, the rain row, status bar) · Footnote 13 (nav, "Sleep story") · Caption 2 11 (the "15" inside the skip glyphs).

**References this round (Mobbin, structure only):** Insight Timer https://mobbin.com/screens/9f4d6660-a448-4182-b56a-09be46facc81 (a photo with a large serif timer), Oura https://mobbin.com/screens/3b2948a4-734e-4c08-a403-2c6ae0d5d1f7 (one photo, one title, three controls and a scrubber), Ten Percent Happier https://mobbin.com/screens/397f0ee2-9bfc-4d6b-995e-d3e18ff85baf (the time as the hero on a flat field).

**Where I left the tokens, on purpose:** the iOS chrome (status bar insets 46/30 pt, the 134 × 5 home indicator 8 pt from the bottom), the 4 pt tracks, the nav glyph offsets that put their ink on the text edges, the two photo gradients and the photo grade.

**Checks:** `engine.py build` and `validate` pass (warnings: two light-mode-only button contrasts on a dark-only screen, 16 text sizes in the scale, `text.headline.md` missing from exports). `preflight.py html`: 0 errors, 1 warning (11 px: the iOS Caption 2 numerals in the skip glyphs). `check_dates.py --year 2026` passes. `check_names.py`: 0 errors; "Minimise" is a UI word and "Oona Prentice" is new (added to NAMES.md). Contrast against the rendered pixels behind each line (text hidden, brightest 5% of its box): status time 15.9:1, nav 14.0:1, "Sleep story" 7.9:1, title 14.9:1, narrator 8.0:1, "Fades out by 23:40" 11.4:1. Gallery copy at 192 px: the eye lands on 16:52.

**Blind pairwise test (A).** Each pairing: our render beside a shipped screen, same height, sides random, no labels, judged by fresh-context agents (from round 2 on, each agent judged three unrelated pairs, one per piece, so it never saw the same screen twice). Ours was judged more premium against Oura (+2, +2, +3, +2) and Ten Percent Happier (+3, +3, +3, +3) in every round, and against Insight Timer it went −2, +2, +2, −2, then −2 on the final render. It was never clearly weaker (3 or more), and it won 2 of 3 in every round: **passes**.

**Fresh-eyes audit (B), against the B2B screens:** 3, 3, 3, 3, 3 and 3 over six rounds: **does not pass**. Each round's fixes were real (contrast, icon weights, numbers, alignment), but the verdict stayed "calm, restrained, facts correct, a generic sleep player"; several asks reversed earlier ones (add the fade to the scrubber, then remove it; drop the elapsed and total labels, then add them back).

**After the last audit** (renders of 18 Oct, 22:22), one small change went into the final `shot.png` (22:27): the timer's tracking eased from -0.04 to -0.03 em, which clears preflight M5. It was not re-audited.
