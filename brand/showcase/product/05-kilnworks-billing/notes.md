# 05 · Usage and billing · Kilnworks

Final render: `shot.png` (1440 × 900 at 2×). Final self-audit score: **4 of 5**.

## Direction
Kilnworks is a fictional cloud compute platform. The screen is Billing and usage for the fictional company Marlpit Analytics on day 14 of 31 in October 2026. Spend is $6,412.38 against a $12,000 budget, and the forecast passes the budget on Oct 26. The users are engineering leads and a finance admin (Jonas Ekdahl, billing admin). They need to know three things: are we going over, why, and what will the invoice say.

Burnt orange is used in only two places: the primary action ("Edit budget") and the forecast crossing (the marker, the dotted segment past the budget, and its label). Everything else is cool grey, with no brown neutrals (owner rule).
Feel words: **trustworthy, precise, plain**. The engine dropped "precise".

The study's section 5.5 is followed point by point:
- **Plan line:** "Team · Active · $480.00 per month for 10 seats · Includes a $1,000 usage credit · Renews Nov 1, 2026 · Card ending 2861", with Change plan and a quiet Cancel plan.
- **Spend against budget:** actual in ink, forecast grey and dotted with a pale likely-range band, budget dashed, and the crossing in the accent.
- **Usage by product:** grouped by family, with a daily bar sparkline per row, signed and right-aligned charges, and group subtotals.
- **Meters:** budget, seats and included credit, each with its reset or alert facts.
- **Receipt ledger:** plan, usage and credit, then subtotal, tax and amount due.
- **Invoices table:** mono references, status with icon and word, totals and a download button.
- **Overage terms in words:** "billed at the listed rates, with no overage multiplier".

## References
The study's references for 5.5 are [Vercel usage](https://mobbin.com/screens/b7b0e5e1-192b-4306-b2a6-88bca0d49bb6), [OpenAI usage and budget](https://mobbin.com/screens/2bf4f941-a9a7-4308-aa0c-864135823830) and [Cofounder billing receipt](https://mobbin.com/screens/e9c05b3d-54e8-44db-9995-15ab9a95078a). I compared against these, all opened in this session:
- [Vercel usage, consumption breakdown](https://mobbin.com/screens/fd0e54a5-45cc-4a47-be0d-3fdb7e804ec7) and [its product rows with subtotals](https://mobbin.com/screens/e828f30f-3564-432d-8a2f-33b3116dd465): family group rows, a sparkline per product, right-aligned charges, and "Usage data can be up to 1 hour old." They taught me the table structure and the freshness note.
- [OpenAI Platform usage](https://mobbin.com/screens/fe36ec31-b25c-4cf1-9932-85bf66cd89fc): a "March budget $0.13 / $10" meter with tick marks, "Resets in 28 days. Edit budget", and a dotted budget line over the spend chart. It taught me the budget meter's ticks and where the budget action goes.
- [Unify usage](https://mobbin.com/screens/34bc05a5-e664-4772-9308-462fde6a7c01): thin meters with "385 / 500 used" and an end date under each. It taught me meter anatomy and restraint.
- [Replit account usage](https://mobbin.com/screens/4c77ec78-b670-4655-95cd-a18a614743d7): "Total this period / Average daily spend" as the chart's headline pair. It taught me the figure row above the chart.

## System (engine)
`sketch --name "Kilnworks" --brand "#c24e14" --audience dense --platforms web --feel trustworthy,precise,plain --theme system-light-dark --delegated all --surfaces operate`

The sketch kept #c24e14 pinned (4.78:1 with white text) but called it "a brown". I then set the P1 profile by hand, each with `--set-by delegated` and the study as the reason:

| Setting | Value | Why |
|---|---|---|
| dials.roundness | 42 | 6 / 8 / 12 px corners |
| dials.depth | 10 | Borders only |
| dials.expression | 25 | P10 |
| dials.warmth | 38 | Cool greys under the orange (tint hue 264), keeping default borders. Below 34 the borders turn into strong rules |
| overrides.type.weightCount | 3 | 400 / 500 / 600 |
| raw.numericStyles | true | Tabular digits |
| answers.Q-color-19 | brand-gray | P7 |
| raw.focusColor | #222428 | Orange is only for the primary action and the crossing, so focus is ink |
| raw.textFace / monoFace | Public Sans / Source Code Pro | Both SIL OFL, from Google Fonts. I checked tabular figures in Chrome first: DM Sans and Albert Sans lack `tnum` in the Google build. My first pair, Instrument Sans + DM Mono, turned out to be the exact pair in `product/02-fennick`. Onest's tabular "1" left gaps ("Oct 1 3"), so I went to Public Sans. All three changes went through `engine.py set` (D-0022 to D-0024) |

Colorfulness stayed at 36 and brand presence at 50 (from the feel words). `bg.action.primary` is the accent, which is right here, because the spec puts orange on the primary.

## Type scale
I used five sizes, and no two are within 10% of each other:

| Size | Role | Where |
|---|---|---|
| 12 | Label and caption | Meta text, units, column headers, legend, axis ends, invoice references (Source Code Pro) |
| 14 | Body | Body text, table cells, ledger lines |
| 17 | Title | Meter figures (`title-md`, 500) |
| 20 | Title | Page title (`title-lg`, 600) |
| 24 | Headline | The spend figure (`headline-sm`, 500), with cents in the tertiary color |

The weights are 400, 500 and 600, checked in the DOM.

## Where I stepped outside the tokens, and why
- **Hairlines.** Neutral 4 for rows and neutral 5 for card edges, because there is no separator role. `--row: 36px` is set by hand; I measured 36 px rows and 32 px group rows.
- **Chart grammar.** The dotted forecast, the likely-range band (neutral 3 at 75%), the dashed budget line (neutral 10), the today line (neutral 8) and the crossing marker are all hand-made. There are no chart tokens for forecast, budget or threshold.
- **Meter bars.** The 6 px track and fill and the hatched forecast are hand-made from neutral steps. There is no meter or progress token.
- **Cents.** Cents are de-emphasized with `text.tertiary`. There is no numeric "minor units" style.

## Data
The data is invented and adds up:
- The 9 product charges add up to the usage line: $6,932.38. Each charge is its quantity × its rate; for example, 21,406 vCPU-h × $0.034 = $727.80.
- Plan $480.00 + usage $6,932.38 − credit $1,000.00 = $6,412.38. That figure appears as the chart headline, the ledger subtotal, the amount due and the last point of the actual line.
- The daily values are generated per product with a weekday/weekend pattern and scaled to each product's charge. The chart's actual line is built from them: it stays flat at $480 while the credit covers usage, and the credit is used up on Oct 2. The meter says so.
- The forecast comes from the last 7 days' weekday and weekend averages, with 0.6% daily growth.
- The crossing day (Oct 26), the month-end forecast ($15,536.26), "Over by $3,536.26" and "Forecast 129%" are all computed from that same forecast.
- Oct 1, 2026 is a Thursday, and the weekends fall where the calendar puts them.

## Checks
- `engine.py validate`: no errors and no warnings. 10 notes: the ink focus color in dark mode (the same finding as 04), APCA advisories, orphan steps, the 24 px control note and asset hooks.
- `preflight.py html --medium web`: 1 error, a false positive (M9: Source Code Pro is loaded from a Google Fonts `<link>`; the DOM check confirmed Source Code Pro 400 and Public Sans 400/500/600 loaded). No size errors, after one fix: `<small>` inside table cells was rendering at 11.67 px, so it is now pinned to the 12 px token.
- `engine.py review`: 18 hard-coded values remain. They are component sizes with no token: the row, the meter bar, sparkline cells and the 28 px download button.
- Contrast:
  - white on the orange button 4.78:1
  - accent 11 text 7.18:1
  - `text.success` on success-subtle comes from the engine's validated pairs

## Self-audit rounds
I compared each round with the Vercel, OpenAI and Unify screens above at 1440 px.

1. **Round 1: 3/5.**
   - Shaded weekend columns made the chart look striped and spilled past the plot edge.
   - The product sparklines were scaled from the minimum, so weekend bars nearly vanished and read like a barcode.
   - The forecast end label read "$15,536.00" against a figure of "$15,536.26".
   - The invoice download icons overflowed the card.
   - The legend note ran off the card.
2. **Round 2: 4/5.**
   - The weekend shading is gone.
   - Bars are zero-based, with weekends one grey lighter.
   - The likely range is a flat pale band instead of a hatch.
   - The end label is whole dollars.
   - The invoice total and download share one cell, and the shortened note fits.
   - The budget meter shows the forecast percentage.
3. **Round 3: 4/5.**
   - The "$9k" label is gone, leaving Y labels at the maximum and the budget only.
   - The sidebar is sticky, so the user block shows.
   - Cell `<small>` is set to 12 px.
   - The budget meter now reads "53% of $12,000.00" with "Forecast 129% by Oct 31", so the dollar spend isn't repeated a third time on screen.
4. **Round 4: 4/5, typeface change.**
   - I found my pair duplicated `product/02-fennick` (Instrument Sans + DM Mono), so I compared Instrument Sans, Onest, Schibsted Grotesk and Public Sans on the same crop.
   - Schibsted's and Onest's tabular figures spread dates and amounts apart. Public Sans reads sober and ledger-like.
   - Public Sans is wider, so the budget note was shortened to "Nothing pauses at 100%" to keep it on one line.

**Why it's a 4 and not a 5.**
- Six blocks on one screen is close to the "everything at once" density line, though each block is something a billing admin checks.
- The product sparklines share one weekday rhythm, so they look a little alike.
- The plan line and the meter strip both live outside cards while the rest of the page is in cards. That matches Vercel and OpenAI, but it is a second containment style on one page.

## Process findings
1. **Gap: no shared registry of choices across parallel builders.** Nothing in the process shows what the other builders' pieces already used, so two pieces in one category picked the same type pair independently. A `showcase` listing of faces and accents per piece would have caught it before the build.
2. **Bug: the sketch called the burnt orange "a brown".** The owner bans brown, so the label misleads anyone reading DESIGN.md. This repeats the data-table piece's finding. (F-001)
3. **Gap: no row-height tokens and no separator role.** All three product pieces set them by hand. (F-002)
4. **Idea: make P1 the dense default.** The profile took 10 manual commands. After them, the engine produced the evidence values exactly, so it should be the default for `--audience dense`. (F-003)
5. **Gap: feel words.** "precise" is unknown, and "quiet" maps only to deferential (P10). (F-004)
6. **Helped:**
   - The brand stayed pinned when it passed text contrast.
   - `bg.action.primary` became the orange with no aliasing.
   - Success tokens gave "Active" and "Paid" a quiet tint.
   - `text.numeric.*` and the 12/14/17/20/24 sizes covered every role I needed.

## Fix round 2026-10-14
After the independent audit (`audit/product--05-kilnworks-billing.json`). Render: `shot.png`, 1440 × 900 at 2×.

- **Alert date.** "Alerts at 50% (sent Oct 13)" contradicted the page's own data. Spend after credit was $5,798 at the end of Oct 13, so it crossed $6,000 on Oct 14. The date is now computed by the script, from the same daily values as the chart, as the first day the spend reaches 50% of the budget. It reads "sent Oct 14".
- **Elapsed time.** The period header said "updated 09:40 UTC", but the data gives Oct 14 a full day of usage (the 14th sparkline bar and the last point of the actual line). It now says "updated 22:40 UTC" (6:40 PM EDT for this US-taxed customer), when the day is about 94% done.
- **Names and numbers.** The workspace Tidewell Analytics is now Marlpit Analytics; Quoin had a Tidewell customer. "Card ending 4417" is now 2861, because 4417 was also in heroes/11 and app-screens/01. The invoice references `KW-4410-…` are now `KW-2783-…`, because Fennick's operating account is ••4410. A web search found no real company called Marlpit Analytics.
- **Re-checked.** The computed figures are unchanged: $6,412.38 spent (53%), $458.03 a day, a forecast of $15,536.26 (129%) that passes the budget on Mon, Oct 26, and the credit used up on Oct 2. Oct 1, 2026 is a Thursday, so the weekend bars fall on Oct 3-4 and 10-11.
- **Not changed (design items from the audit, outside this fix round).** The orange primary button still shares its color with the over-budget warning. "Active" is still a green pill. The page still has several bordered cards.
