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
