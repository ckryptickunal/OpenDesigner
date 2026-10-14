# 03 · Date range picker (Wayfern)

## Direction
Wayfern is a fictional booking site for small cabins and guesthouses. The picker should feel like the start of a holiday: cream paper, terracotta, apricot, a low sun and rolling hills, soft round shapes, a wonky friendly serif. Every night shows its price, and the price colours the cell from cream (lower) to coral (higher), so cheap stretches jump out. A tiny fern marks the four best-priced nights. Feel words: **playful, warm, sunny**.

## References (Mobbin, cited by link only)
- KAYAK hotel calendar, https://mobbin.com/screens/968c1ad2-ddb5-46ec-b3f8-cac800d7bc22 : whole-cell heat in three tiers with a "Cheaper / Average / Higher" key, and the picked range in a dark contrasting fill. Taught me that the range must not share a colour with the heat.
- Tripadvisor hotel dates, https://mobbin.com/screens/7bd683f8-b76b-4415-8d15-e497857de037 : round, soft heat cells and quick-pick chips ("This weekend"). Became the chips row.
- Kiwi.com dates, https://mobbin.com/screens/1a7ba6fe-e234-4592-83fb-146d20c5985d : a price printed under every day number, and flexible ±N-day chips. Became the two-line cell and "± 2 days flexible".
- Expedia room dates, https://mobbin.com/screens/9706c0d4-421c-4a44-a599-ceb2e3aa716a : circles for the two ends joined by a band. Kept the band, with ink circles for the ends.

## System (engine)
- `sketch --name Wayfern --brand "#E4572E" --audience regular --platforms web --feel playful,warm,sunny --theme system-light-dark --surfaces "booking:operate" --delegated all`. The engine stored #d04418 as the brand ("I picked a red") so white button text passes; accepted, it is still terracotta.
- Dials (all `delegated`): expression 70, density 40, energy 68, roundness 88 (16 px controls, 32 px card), depth 40, colorfulness 72, warmth 88.
- Answers: Q-color-09 warm; **Q-type-08 16 and Q-type-09 1.25**, because the first build gave a 14 px base, ratio 1.333 and an 11 px small size; Q-color-19 categorical-6-8 (to see whether a sequential ramp appears; it does, but see findings).
- Faces: `raw.textFace Nunito` (rounded, OFL), `raw.displayFace Fraunces` (OFL, with its SOFT and WONK axes on). Both from Google Fonts.
- Final scale: 13 / 16 / 20 / 25 / 31 / 39.

## Build
Everything in the picker uses `--ds-*`: colours, radii, the type scale, spacing, focus ring, motion. The heat tiers are composed from the system's own steps: lower `warning.light.3`, typical `warning.light.6`, higher `accent.light.7`; the picked range is `bg.action.primary` with ink end circles; the hover preview is `accent.light.3` with a dashed `accent.light.8` edge.

Outside the tokens on purpose:
- The sunny backdrop (sun and hills) uses token colours but its shapes are art.
- Two coloured shadows (`rgb(160 70 30 / .35)` under the card, a terracotta glow under the button): the elevation tokens are neutral, and a warm page wants a warm shadow.

Interaction: each month is a `role="grid"` with roving tabindex; arrows move by day and week, Home and End jump to the week's ends, Enter or Space picks. The first pick sets check-in, the next later pick sets check-out, a pick across a sold-out night starts over. Hovering (or arrowing) after a check-in shows a dashed preview band. A pointer pick pops the end circle in with the token momentum spring (`motion.spring.momentum`); a keyboard pick does not animate (STD-when-to-animate-06). Totals and an `aria-live` summary update on every change. Sold-out and past nights are `aria-disabled`.

## Revision for the owner's type and color rules (mid-run)
- **Fonts:** already two (Fraunces, Nunito). No change.
- **Weight on purpose.** The headings were Fraunces 650 to 750, which made the title, month names and panel titles compete with the range band for attention. The visual weight of this screen should sit on the picked range, so the headings are now 560 (the soft serif still carries the friendly voice) and the total 650. Day numbers stay 800 because they must be scanned.
- **No brown-black next to orange.** The picked range's end circles were warm near-black (#262421, the neutral ramp at warmth 88) sitting on the terracotta band. They are now white circles with an ink ring, like holes punched in the band: clearer tonal contrast and no brown-black on orange. The warm neutrals are used only as text on cream, where they read as dark ink.
- **Type scale, named roles** (web px): caption 13 (prices, labels, legend), body 16 (day numbers, copy, buttons), title 20 (month names, panel titles), headline-sm 25 (wordmark, total), headline 31 (page title). Five sizes, each at least 23% from the next.

## Checks
- First render had two real bugs: the range band showed behind every cell, and the selected ends were invisible (a more specific "in range" rule made them transparent). Fixed.
- Second look: the in-range band (`accent.light.4`) was the same pink as the "higher" heat cells, so the range read as a run of expensive nights. Changed the band to the terracotta action colour with ink end circles.
- Rendered contrast: first pass 29 failures, mostly secondary-grey prices on the coral and tan heat cells (4.22:1) and white prices at 92% opacity on the band (4.30:1). Prices on heat cells now use ink; the band text is full white (4.65:1). Final: only the struck-through past days fail (3.56:1), which are inactive and exempt.
- `preflight.py html`: first 2 errors (Fraunces and Nunito "no @font-face", false: they load from Google Fonts) plus a misread 24 px size (it was a line height). After removing an unused `font-family` class and writing the line height unitless: 0 errors, 0 warnings.
- `engine.py validate`: no errors, no warnings.
- Computed sizes 13, 16, 20, 25, 31, all on the scale. Faces in use are loaded (Fraunces variable 400 to 800, Nunito 400 to 800).
- Playwright: two clicks give Mon 6 Jul to Thu 9 Jul, 3 nights, €313; the sold-out Sat 20 Jun cannot be picked; "This weekend" gives Fri 5 to Sun 7 Jun; keyboard Enter, arrows and Enter give Fri 5 to Sun 14 Jun, 9 nights, €907, with no pop animation; a range across a sold-out night restarts at the new day.
- `review`: 34 findings, mostly small sizes in the cell internals and the art shadows.

## Process findings
1. **An 11 px small size out of the box.** The engine's own floor (stage 11) and preflight say 12 px. Bug, recorded.
2. **The brand colour was rewritten again** (#E4572E stored as #d04418). Second time; recorded.
3. **No sequential ramp for UI heat.** The only one is `color.chart.sequential`, hidden behind the charts question and built from the accent hue, so it collides with the selection colour. Gap, recorded.
4. **preflight's font checks depend on syntax**: longhand `font-family` with Google Fonts fails, shorthand passes; a line height read as a font size. Bug, recorded.
5. Helped: the momentum spring token gave the end circles a believable pop with no tuning, and the standards' "never animate keyboard actions" rule shaped the keyboard path.
