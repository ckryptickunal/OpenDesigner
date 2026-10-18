# 01 · Halden Private: private banking home

## Direction
Halden Private is a fictional private bank for people with complex wealth (founders, families, trustees). The home screen should feel like the inside of a good leather wallet: deep bottle green-black, one restrained gold, a metal card you want to touch, and numerals set like an engraved certificate. Feel words: **premium, calm, trusted**.

Shape language: sharp tailored corners (4 px controls), hairline rules, a guilloche rosette. Type: a high-contrast didone (Bodoni Moda) for the wealth figure, the wordmark and the section title; Inter for everything you operate. Two fonts, no more.

## References (Mobbin, structure only)
- https://mobbin.com/screens/f1e10eb9-dfe8-4817-8e82-43272bc17ede (a business bank, dark home): the balance with smaller superscript cents directly above a full-bleed line chart. Taught the hero rhythm: label, figure, delta, then the chart with no axis.
- https://mobbin.com/screens/0a2c9de0-048e-444e-876a-de3daf00f81c (a neobank card screen): the physical card as the hero with the next card peeking in from the right, so the carousel reads without arrows.
- https://mobbin.com/screens/7b451837-103e-44be-9d06-4ffa97f48f4e (a business account home, dark): dark grouped content where amounts sit right-aligned in tabular figures with a second line for the change. Taught the row density.

## System (engine)
```
sketch --name "Halden Private" --brand "#C9A86A" --audience regular --platforms ios --feel premium,calm,trusted --theme system-light-dark --delegated all
pick Q-color-01 keep-hex · pick Q-color-21 near-black · set raw.neutralBase "#0E2A1F" · set raw.brandColor "#C9A86A" (restored, see findings)
pick Q-type-01 brand-display · set raw.displayFace "Bodoni Moda" · set raw.textFace "Inter" · pick Q-type-02 yes · pick Q-type-08 17
set overrides.type.displayReach 4
```
Dials (all `--set-by delegated`): expression 55 (one hero figure and one hero card), brandPresence 70 (gold and the serif carry the brand), density 35 (unhurried), energy 10 (nothing hurries), roundness 30 (4 px controls, 8 px containers), depth 65 (the card needs light and shadow), colorfulness 22 (gold is the only color), warmth 45.

The page renders the system's **dark** mapping (`<html data-theme="dark">`). `dark-only` was refused by house standard STD-visual-details-24, so the system keeps a light mode it is never shown in.

## Fonts
Bodoni Moda (SIL OFL) and Inter (SIL OFL), both from Google Fonts with a `<link>`.

## Where I went outside the tokens, and why
- **The metal card** (ISO card corner 13 px, brushed-metal gradients, specular sheen, noise, engraved text shadows, chip). It is a physical object, not UI; every color in it still comes from the neutral-dark and accent-dark ramps. Lines are marked `od-ignore: physical card art`.
- **Wealth figure** at 52 px weight 450 (the token heading weight is 600): a didone at 600 turns heavy and clotted; 450 keeps the hairlines. Pence and currency sign are 21 and 33 px, both scale steps.
- The atmosphere gradient behind the content mixes ramp steps 1, 2, 7 and accent 8.

## Checks
- `engine.py validate`: 0 errors, 2 warnings (light mode only: the gold primary fill on near-white is 2.2:1 against the page; a text-labelled button needs no boundary contrast, and this screen is dark).
- `engine.py review`: from 64 findings down to 12 after tokenising the UI spacing; the rest are element sizes, hairline rings and the home indicator (false positives, see findings).
- `preflight.py html --medium web`: 3 errors. "Bodoni Moda / Inter have no @font-face" (they load through the Google Fonts `<link>` the brief allows) and "text under 12 px for web: 11" (iOS tab labels). Neither is a real defect on an iOS screen; preflight has no app medium.
- Checklist (type and layout): tracking no tighter than -0.015em; 6 sizes (see the type scale below); no wraps; contrast: secondary text #95b1a4 on #171e1b is 7.35:1, tertiary tab labels #7d9c8e on #121614 are 6.1:1, gold link text #dac298 is 9.8:1 (computed); targets 44 pt (bell, avatar, range picker with an enlarged hit area, tabs 72 × 48).
- Reviewed at full size three times: round 1 fixed overflow (accounts under the tab bar), a perspective tilt that made the card look warped, the guilloche reading as a hole, and the chart dot clipped at the edge; round 2 fixed the chart fill running past the line and tuned the rosette.

## Process findings
1. **Bug: the sketch replaced an explicit brand hex.** `--brand "#C9A86A" --delegated all` recorded D-0005 `raw.brandColor = "#8f7032"` "a readable shade ... (an olive)". Gold with dark text passes (about 9:1), so nothing needed fixing. `pick Q-color-01 keep-hex` afterwards did not restore it; I set `raw.brandColor` again.
2. **Bug: iOS body text fell to 14 px** when Brand presence went to 70 (`platform.useNativeBaseSize` turns off at 50+), with 11 px labels. Fixed with `pick Q-type-08 17`.
3. **Gap: open fonts not recognised.** Bodoni Moda is OFL, but validate warned it had no app licence until I answered Q-type-02 `yes`.
4. **Gap: tinted darks.** Ramp ends cap neutral chroma at 0.008, so "deep green-black" needs `raw.neutralBase` with a stronger green; Q-color-09 has no "tinted dark" option.
5. **Gap: no 11 pt iOS caption / tab label step.**
6. **Confusing: review vs tokens.** `engine.py review` flags `gap: 6px` with "write spacing in rem" (STD-accessibility-motion-13), but the generated `--ds-space-*` tokens are themselves in px. It also suggests `--ds-elevation-raised` for a 1 px inset ring and `--ds-space-0` for a negative hit-area margin.
7. **Preflight has no iOS/app medium** and treats a Google Fonts `<link>` as "no @font-face", which contradicts BRIEF.md's font rule.
8. Helped: `set` prints how many token values change, and the dark ramps from a tinted neutral base came out beautifully even, so the whole palette stayed in the system.

All feedback recorded with `engine.py feedback` in `opendesigner/feedback.md`.

## Revision for the owner's type and color rules (mid-run)
Type scale, Apple HIG Dynamic Type roles, set through the engine (`Q-type-10 named`, `Q-type-09 hand-tuned`, 8 `font.size` steps and 11 text-style overrides; see PROCESS-01-05.md):

| Role | Size / line | Used for |
|---|---|---|
| Display (custom) | 52 / 52, Bodoni 450 | the wealth figure |
| Large Title | 34 | the pound sign beside it |
| Title 2 | 22 / 28, Bodoni 400 | "Holdings", the pence, the card monogram |
| Body / Headline | 17 / 22 | rows, amounts, wordmark, status bar |
| Subheadline | 15 / 20 | secondary lines, the overline, card engraving, "See all", range picker |
| Caption 2 | 11 / 13 | tab bar labels (now a token, `--ds-font-size-11`) |

Six sizes, each at least 13% from its neighbour, nothing under 11. Changes made for the rules:
- The wordmark was "HALDEN *Private*" with an italic word: now "HALDEN PRIVATE" in one roman face, the second word in gold (color, not italic).
- "Holdings" was an italic serif title: now roman Bodoni 400 (titles don't have to be bold).
- The overline "TOTAL WEALTH · 14 OCT" in 11 px caps became the Subheadline "Total wealth · 14 October".
- Card "Reserve" was italic: now spaced roman capitals. Card text moved from 14 to 15 (Subheadline), the monogram to 22.
- Sizes 14, 21 and 33 (formula steps) became 15, 22 and 34 (HIG steps).
- Color was already within the rule: green-black background with ivory and gold text (7.35:1 and up).
- `engine.py validate` now warns "15 text sizes", because the old formula steps cannot be removed (finding).

## Round 3 (owner review, 2026-10-14)
**What he said:** "needs work on font; text is not visible." The serif was carrying small text it could not hold: Bodoni Moda hairlines on letterspaced capitals (wordmark, card engraving, "Holdings"), gold foil text on a textured green card, and green mid-tone secondary text on a green-black page.

**What changed:**
- **Type.** Bodoni Moda now sets only the wealth figure (Display 48, weight 500, opsz 48) and the wordmark (Title 2 22, weight 500, no tracking). Everything you read or tap is Inter at iOS Dynamic Type roles: Title 3 20 semibold for "Holdings", Body 17 for rows and amounts, Subheadline 15 for secondary lines, the change and the range picker, Caption 1 12 for tab labels (was 11). Six sizes: 48, 22, 20, 17, 15, 12. No letterspaced capitals anywhere.
- **Contrast.** `raw.neutralBase` moved from #0E2A1F to #1C2B24 through the engine: the page is a greyer green-black (#131614), primary text #e4ebe7 (15:1), secondary text #9fb0a7 (about 8:1, was a greener #95b1a4). The atmospheric gradient behind the page is gone.
- **The card is gone from the home.** The brushed-metal card with guilloche, grain, foil text, a monogram and a blank peeking card is replaced by the one thing a private bank asks of you today: "Approve by Fri 16 Oct · £150,000.00 · To Cardew Aske LLP · Completion · from •••• 0921" with a Review button. `dials.depth` 65 to 30.
- **The brand is said once** (the wordmark). The "H" monogram, "HALDEN RESERVE" and the engraved name are gone.
- **Gold has two jobs:** the Review action and the active tab. The change line is primary text with +/− signs; the chart line is ivory; the bell badge is gone.
- **Chart and range.** Daily closes from Mon 14 Sep to Tue 13 Oct, flat at weekends, no fill, a dotted start-value baseline, end labels, and a full-width iOS segmented control (1W 1M 3M 1Y All) on the 20/370 margins, as in Monarch and Wealthsimple.
- **Numbers re-added from the page.** Holdings £182,440.12 + £3,435,092.17 + £1,244,778.25 = £4,862,310.54 (the total). Changes −£3,612.40 + £37,048.23 + £4,778.25 = £38,214.08 (the month's change); £38,214.08 / £4,824,096.46 = 0.79%. Deposit interest £1,240,000 × 4.85% × 29/365 = £4,778.25. "See all" is gone (the three rows are the whole total); the header says "3 accounts".
- Icons: the Wealth tab is a pie chart (it read as a clock), the deposit a lock.
- New type steps through the engine: `overrides.font.size.12` and `overrides.font.size.48`.
- References for this round: Wealthsimple https://mobbin.com/screens/3451c08b-cf3c-4a71-8064-14580f02ab59 (balance over an axis-free chart, range pills), Monarch https://mobbin.com/screens/4ad2671f-6507-4372-bea6-91263585f5e1 (segmented range under the chart, grouped accounts), Crypto.com https://mobbin.com/screens/8505ff3c-ef22-46a9-b33e-3ae2bcdd39dc (total, change line, range control, products list).

**Fresh-eyes audit** (fresh-context agent, against the B2B product screens and the three references): first pass **3/5** ("stock fintech home; Bodoni hairlines 1 device px on the hero; gold has 8 jobs; placeholder card; numbers that do not hold up: round deposit beside its interest, 4.85% over 29 days is not £4,922.10"). All fixed. Second pass **4/5**, with five small defects (double hairline above the tab bar, faint segment thumb, gold chart line competing with Review, the £150,000 unexplained, two date formats), all fixed after it. Not a 5 because the layout is still the standard wealth home; the approval task is the ownable part.

**Checks:** `engine.py build` passes (warnings: light-mode primary fill 2.2:1 boundary, advisory; 17 text sizes from the old formula steps). `preflight.py html`: 1 error, "Bodoni Moda has no @font-face" (it loads from the Google Fonts `<link>` the brief allows). `check_dates.py --year 2026`: every weekday matches. Contrast from the pixels (auditor): every text 6.1:1 or more; hero hairlines now 2-3 device px.

**Open:** "Halden" also names Halden Freight, a customer row in `components/06-data-table`. The bank is this piece's product and appears in `mockups/01-phone-trio`, so the freight company is the one to rename. `mockups/01-phone-trio` shows this shot.png and its alt text still says "a metal card ... on deep green": its owner should re-render and update the alt text.

## Round 4 (owner review, 2026-10-15)
**What he said:** "some of the app screens like the private banking home with the table ... look absolutely shit. None of them should feel like they are from a vibe coded app or a cheap Chinese app." The round 3 screen had a Bodoni total at display size beside system-style text, a bare ivory polyline over a dotted baseline, a mustard "Review" pill, large loose text and tab icons of mixed weight. AI auditors had scored it 4, so this round was judged by a blind pairwise test against shipped apps and a fresh-eyes audit against the B2B screens.

**The one idea:** a household's total wealth at yesterday's close, with one payment waiting for approval.

**What changed (rebuilt in place):**
- **Light, not dark.** White page, ink text (#222523, 15:1), greys from a near-neutral base (`raw.neutralBase` #5E6460). "The fonts are not visible" came from mid-green text on green-black; every text now measures 5.9:1 or more.
- **One face plus one display moment.** Inter (optical sizes on) for everything read or tapped, at iOS roles. Newsreader sets only the total, at 40 pt (weight 500, rounded to the pound). The brand is said once in the nav, "Halden Private" in Inter 600 with "Voss household" under it (a switcher); the Bodoni wordmark and the monogram are gone.
- **One accent, one job.** Halden green (#14674A, `raw.brandColor`) marks what you can act on: Review and the tab you are on. The chart and every number are ink.
- **The chart:** 23 trading-day closes (weekends skipped, since holdings are valued at the close) as a monotone curve, a 2 pt ink line over a 7% ink fill, a hairline base, and only the start ("14 Sep · £6,001,183"), the high ("£6,062,468 · 6 Oct") and the end ("14 Oct") labelled. The floor sits about 1% under the opening value, so a 0.79% month does not fill the plot. (A 1W to All range control under it was removed in the focused pass.)
- **The ask:** a white card with a hairline: "Payment to Cardew Aske LLP", £150,000.00 at Title 3 20, "House purchase · by Fri 16 Oct", and a green Review button (44 pt hit area).
- **Accounts:** four rows with chevrons under a "Past month" column label: name and mandate on the left, balance (medium, tabular) over the signed change on the right, one-device-pixel separators. A pension row is a real holding in the total; it also closes the dead band above the tab bar the first blind judges noticed.
- **Icons:** one 1.5 pt stroke (CSS `vector-effect: non-scaling-stroke`).
- **Tried and removed this round:** account icon discs, an allocation bar with swatches and shares (the shares read as interest rates), a dotted value grid with four axis labels, a halo on the end point.

**Numbers, re-added from the page:** £182,440.12 + £3,435,092.17 + £1,244,943.01 + £1,186,204.66 = £6,048,679.96, shown as £6,048,680. Changes −£3,612.40 + £37,048.23 + £4,943.01 + £9,118.37 = £47,497.21, shown as £47,497; £47,497.21 / £6,001,182.75 = 0.79%. Deposit interest £1,240,000 × 4.85% × 30/365 = £4,943.01. The chart starts at £6,001,183 (the total less the month's change) and ends at the total. Wed 14 Oct, Fri 16 Oct and Mon 14 Sep match the 2026 calendar.

**Type scale (iOS roles):** Display 40 (the total, Newsreader) · Title 3 20 (the amount to approve) · Body 17 (wordmark, section heads, rows, amounts) · Subheadline 15 (labels, secondary lines, range, Review) · Caption 2 11 (household, chart and tab labels). Five sizes.

**Engine (this round):** `set raw.brandColor "#14674A"`, `set raw.neutralBase "#5E6460"`, `set raw.displayFace "Inter"` (Newsreader is a page-level exception for the one figure), `dials.brandPresence 35`, `dials.depth 10`, `dials.colorfulness 15`, `overrides.font.size.40`, then `build` (passes; 1 warning: 17 text sizes from old formula steps). `preflight.py html`: 0 errors, 1 warning (11 pt labels; iOS Caption 2).

**Blind pairwise test** (ours and a shipped screen, same height, random sides, no labels; fresh-context judges, several pairs per judge). References: Wealthfront home https://mobbin.com/screens/8e5cbd25-73a0-4d79-8c6b-567c425d6f67, Monarch accounts https://mobbin.com/screens/3d951da4-8f9f-44d6-93af-ac3ddef8c85f, Mercury home https://mobbin.com/screens/ebc012c3-f9d6-4e09-b84c-013ba91da31b (Public https://mobbin.com/screens/1499425b-e4ef-4568-95c2-3b414cd95f51 in the first two rounds).
- Round 1 (first rebuild): Wealthfront won by 2; ours won by 3 against Monarch and Public.
- Rounds 2 and 3: ours won all three each time, by 2 to 3.
- Round 4: ours won against Wealthfront by 3 and Mercury by 2; Monarch won by 2 ("rows read like a spreadsheet", "a thin line with no fill").
- Final (the version before the last polish): ours won against Wealthfront by 2 and Mercury by 2; Monarch won by 2 (no icons, gains and losses in one grey). Passes the rule (never clearly weaker by 3, equal or better in 2 of 3). The Mobbin images carry blur redactions and demo data, which favours us; that is noted, not corrected.

**Fresh-eyes audit** (against the B2B product screens, ROUND3-BRIEF rule 6): **3, 3, 3, 3** over four rounds. Each round's defects were fixed (shares read as rates, unlabelled changes, a chart that exaggerated a 0.79% month, the approval card's wording, uneven gaps, heavy separators, no brand on the page). The last audit's verdict: "competent but reads as the stock fintech template", too close to Monarch's order (figure, change, chart, range, accounts). Its last items were applied after it: the wordmark, the approval card's wording, an honest chart floor with the high labelled (audited in the focused pass below). **It does not reach 4.** Not applied: a floating iOS 26 glass tab bar, a "Recent payments" section under the tab bar.

**Checks:** `check_dates.py --year 2026`: every weekday matches. `check_names.py`: 3 flags, all known (Halden against Halde in `heroes/01`, kept on purpose; "Halden Freight", whose registry row remains though NAMES.md records its rename to Ostrel Freight). Shot re-rendered with `brand/tools/shot.py --w 390 --h 844 --scale 3`.

**Outside this folder:** `mockups/01-phone-trio` shows this shot.png; its alt text describes the old screen (£4,862,310.54, the old approval line).

**Focused pass (2026-10-18).** The range chips were removed (the period is in the change line), rows got 8 pt padding, a "Recent payments" section now starts under an iOS 26 floating glass tab bar (with a scroll-edge fade), and the wordmark moved from Newsreader to Inter 600, so the serif sets only the figure. The chart's high is now an unrounded close (£6,062,468 on Tue 6 Oct, the series' 17th close). Blind test of this version: ours won against Wealthfront by 3, Monarch by 2 and Mercury by 3. **Fresh-eyes audit: 3 again** ("it works, but it's the stock fintech home"; "nothing on it belongs to Halden"). Its small items were applied after it (heading clear of the bar, chevron on the wordmark line, head and label on one baseline, the unrounded high, 20 pt bar inset, one date) and not audited again. **Halden does not reach 4 after five audits.** The auditors' remaining objection is the structure itself, the standard wealth-home order; the owner should decide whether a different concept is wanted.
