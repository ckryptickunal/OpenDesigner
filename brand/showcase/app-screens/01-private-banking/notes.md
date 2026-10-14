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
