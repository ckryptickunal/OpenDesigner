# 11 Quillon: purchase request approval (iPhone)

Replaces `app-screens/02-sleep-meditation` (audited 2 of 5, "remake"). Render: 390 x 844 pt at scale 3 (1170 x 2532 PNG, `shot.png`), the same as the earlier app screens.

## Direction
Quillon is a fictional purchasing and approvals app for mid-size companies. A department head gets a push between meetings and has to decide on a $14,860 replacement forklift battery. The screen answers, in this order: what it is and what it costs, what happens to the budget and to the order if they approve, which policy applies, who has signed and who comes next, then approve or decline. Feel words: **trustworthy, calm, clean**. Mood: a native iOS work app that respects the person's time.

What the old piece did that this one must not: a glowing orb on a painted gradient, two heroes competing, glow stacked on glow, rings with no data (`audit/app-screens--02-sleep-meditation.json`). Here there is no art at all; the one drawn object, the budget bar, is data.

## References (Mobbin, cited by URL only; no image saved)
| Reference | What it taught |
|---|---|
| https://mobbin.com/screens/9a34e3c2-65fa-49e0-9a6f-5833c749d333 | An approval detail with "Approvals · 1 of 1" and a vertical chain of who submitted and who is waiting; Approve and Reject as plain paired buttons. |
| https://mobbin.com/screens/fdf16c74-5c67-4189-9ffb-4d2b83819811 | Status as a check-circle timeline in grouped sections, label-value rows, and a labelled tab bar. |
| https://mobbin.com/screens/d4e4f075-e8d2-4292-be15-b0bf2031b0db | The consequence written out before the buttons ("6 hr 14 min left to approve, otherwise it will be cancelled"); Approve filled, Reject grey. |
| https://mobbin.com/screens/15f94e0a-3300-4e89-b55e-63c70578ed4f | A policy line in plain words above the action. |

Also read: `b2b-study/product-ui.md` section 2.8 (show the consequence before the decision; approval counts like "0/1 Approved"; the button says what it does).

## System (engine)
```
sketch --name "Quillon" --brand "#1F7A4C" --audience regular --platforms ios --feel trustworthy,calm,clean
       --theme system-light-dark --surfaces "app:operate" --delegated all
pick Q-type-08 17; set raw.textFace "Inter"; pick Q-type-02 yes; pick Q-type-10 named; pick Q-type-12 three
set overrides.font.size.{11,13,15,22,34}; pick Q-color-09 pure; build
```
The brand green survived the sketch unchanged (white text passes on it, 5.3:1).

| Dial | Value | Why |
|---|---|---|
| expression | 25 | A work tool; no decoration |
| brandPresence | 30 | Green is iOS tint: back button, next arrow, the quote link, the chain checks, Approve, the selected tab |
| density | 50 | Native iOS spacing |
| energy | 20 | Calm |
| roundness | 55 | 8 pt controls, 12 pt cards, as iOS inset-grouped lists |
| depth | 15 | Flat cards on the grouped background |
| colorfulness | 25 | One green, plus red only for Decline and the badge |
| warmth | 25 | With `Q-color-09 pure`: plain greys like iOS system grays |

## Fonts and type scale
One family: **Inter** (SIL OFL) with its optical-size axis, standing in for SF Pro, which is not open-licensed. Tabular figures only on numbers: on the whole body they also widened hyphens ("FL - 07").

| Apple Dynamic Type role (Large) | Size | Used for |
|---|---|---|
| Large Title | 34, 500 | The amount ($14,860, with ".00" smaller and lighter) |
| Title 2 | 22, 600 | "Forklift battery for FL-07" |
| Body / Headline | 17 | Status bar time, back button, the "1 of 4" title, buttons |
| Subheadline | 15 | Vendor line, budget row, chain names, the PO sentence |
| Footnote | 13 | Section headers (uppercase, as iOS grouped lists), legend, policy, chain detail, badge |
| Caption 2 | 11, 500 | Tab bar labels (the owner's 11 pt minimum; Apple uses 10) |

Six sizes, nothing under 11.

## iOS conventions
Status bar (time, signal, Wi-Fi, battery); navigation bar with "‹ Approvals", the title "1 of 4" and previous/next arrows (Mail's pattern; previous is disabled on the first request); inset-grouped cards on the grouped background; a decision bar pinned above a four-item tab bar with labels and a badge (4 waiting); the home indicator. Targets: back 44 pt, arrows 44 x 44, Decline and Approve 50 pt tall, tabs 49 pt.

## The data, checked
Facilities budget for Jul–Dec $96,000; spent $57,800 (60.2%); this request $14,860 (15.5%); left after approval $23,340 (24.3%). The bar segments use those exact widths; the request's share is ink, not green, so it does not read as "good". Chain: requested 08:12, procurement approved 09:40, "You" waiting since 09:40, CFO next because the amount is over the $10,000 policy limit, so the consequence line says "Rhea Kapoor (CFO) approves next. Then PO-10482 goes to Ashbury, paid on Net 30." The vendor quote (Q-5571.pdf) is valid until Fri 16 Oct 2026. Approve repeats the amount: "Approve $14,860".

## Color and contrast
Primary #242424 on #f4f4f4 14.1:1; secondary #575757 6.6:1; green text #19633d 6.6:1; white on the Approve green 5.3:1; Decline red #973731 on its grey 5.6:1; inactive tab labels #646464 5.9:1.

## Checks
- `engine.py validate`: passes; 1 warning, "12 text sizes" (the formula steps cannot be removed; the screen uses six).
- `engine.py review`: first run flagged an inset shadow used as a gap, two 48 px heights, the home indicator's negative margin and a 5 px badge padding (breaks STD-accessibility-motion-13). All moved to tokens or rewritten; the 1.5 pt chain connector is kept raw with `od-ignore`. Now clean.
- `preflight.py html --medium web`: 0 errors, 0 warnings (there is no iOS medium).

## Self-audit (score against the four references at 390 wide)
- **Round 1, score 2.** The approval chain was hidden under the decision bar (only two and a half rows showed), and body-wide tabular figures put spaces around hyphens ("FL - 07", "PR - 10482").
- **Round 2, score 3.** Most of the chain showed, but the PO sentence and the policy line each wrapped to two lines and the CFO row was still under the bar.
- **Round 3, score 4 (my own).** Each line rewritten to fit one line, section spacing 20 to 16, chain rows 48 pt. All four steps and both buttons show. Section 11 walk: no glow, no art, no decoration, iOS chrome rebuilt from shipped references, one accent, status by shape and word (filled check, ring, hollow circle).
- **Round 4, independent audit, score 4.** A fresh-context subagent checked the arithmetic (it holds) and found a logic error I had written in round 3: "PO-10482 goes to Kessler today, paid 14 Nov" cannot be true when the CFO still has to approve after you. It also found "Fri 17 Oct" (17 Oct 2026 is a Saturday), no "1 of 4" context, no way to open the quote behind "compared 3 quotes", and a green budget segment that read as "good". Fixed: the consequence line names the CFO step first; "Fri 16 Oct"; a "1 of 4" title; "Quote Q-5571.pdf" as a link; the request's share in ink. A web search then showed "Kessler" is a family of real power-equipment companies, so the vendor became "Ashbury Traction Power" (no match found).
- **Final, score 4.** Re-rendered at 390 x 844 @3x and read at full size: all four chain steps, the policy line and both buttons visible, nothing cut off.

## Process findings
1. **Still no Apple HIG named type scale (gap).** Five `overrides.font.size` steps by hand; `Q-type-10 named` only records a rule, and validate then warns "12 text sizes" for a six-size screen.
2. **Preflight has no iOS medium (gap)** and treats Google Fonts links as missing faces (the hero and footer each got this false M9 error).
3. **Parallel work copies a piece mid-flight (process).** `mockups/10-multi-device` (another builder) rebuilt this request for the web while I was still fixing it; its `desktop.html` still carries the old vendor "Kessler Industrial Power" and "valid until Fri 17 Oct" (a Saturday in 2026); its consequence line is already correct ("Once the CFO approves, PO-10482 goes to Kessler"). It needs the vendor and date corrections to match; I did not edit it (not my folder).
4. Helped: `Q-color-09 pure` turned the neutrals into plain greys in one step, and the sketch kept the brand hex this time because white text already passed on it.

All recorded with `engine.py feedback` in `opendesigner/feedback.md`; nothing posted.

## Fix round 2026-10-14
After the independent audit (`audit/app-screens--11-approvals-mobile.json`). Render: `shot.png`, 390 × 844 pt at 3× (1170 × 2532).

- **Budget period.** The card said "Facilities budget, Q4" with 60% already spent. But the quote is valid until Fri 16 Oct, so the screen is in the second week of Q4, and spending 60% of a quarter's budget in two weeks doesn't fit. It is now "Facilities budget, Jul–Dec": 3.5 of 6 months gone and 60% spent. The bar's aria-label says the same. The amounts are unchanged: 96,000 − 57,800 − 14,860 = 23,340 left.
- **Names.** Owen Castillo is now Owen Marchetti (heroes/10 has R. Castillo). The app keeps the name Quillon; Fennick's vendor "Quillon Software" was renamed instead, so the brand is now used only by this app and by `mockups/10-multi-device`, which shows the same product.
- **Outside this folder.** `mockups/10-multi-device/desktop.html` shows this approval on the web and still says "Owen Castillo" (twice) and "Facilities budget, Q4". It needs the same two changes, and then a re-render of `desktop.png` and its `shot.png`.
- **Not changed.** The audit's design fixes are outside this fix round: sentence-case section headers, and a quieter Decline.

## Round 3 (owner review, 2026-10-14)
**What he said:** "needs better spacing." The render was evenly cramped: 6–16 pt between groups, a decision bar stacked on a tab bar (158 pt of chrome), the chain squeezed to fit above it.

**What changed:**
- **One bottom bar.** This is a pushed detail screen with a pinned decision, so the tab bar is hidden, as Brex does. The decision bar has 12 pt above 50 pt buttons and the 34 pt home area below; it is translucent, and a Details card scrolls under it.
- **An 8 pt rhythm with room:** title to vendor 8, 12 above the amount, 4 below it, 24 before each section, 8 from a header to its card, 16 inside cards, 58 pt sign-off rows (8 above and below the text) with the time in its own column. All four sign-off steps and the "Details" header sit above the decision bar; the Details card starts exactly under it. Section headers are regular weight (they had picked up the browser's bold for h2).
- **Type at iOS roles:** names, the budget label and the vendor line at Body 17; details, legend, times and the quote line at Subheadline 15; section headers at Footnote 13 in sentence case. Decline is regular weight.
- **Its own identity.** Next to Fennick (`product/02`, the same domain on the web, in forest green) Quillon read as a copy, so the accent moved through the engine to cobalt `#2B4C9B` (`set raw.brandColor`), the title is the request ID "PR-2207" (the ID `mockups/10` already uses), the amount is whole dollars, and the section labels are its own ("Budget after approval", "Sign-off · 1 of 3 approved").
- **Content:** the requester is an arrow, not a check (only Owen has approved: 1 of 3); "Waiting" and "Next" sit in the time column; the policy sits on the CFO's row ("CFO, over $10,000 (FIN-04)"); the PO sentence became a Details row with the GL account (6420 Equipment upkeep) and delivery date (Wed 21 Oct); the budget reads "$23,340 of $96,000 left" with "60% spent" and "+15% this request" starting under its own segment (the "24% left" label made the legend add to 99% and repeated the line above); "Quote valid until Fri 16 Oct" is primary text with a clock. The tab badge is gone.
- **Contrast of graphics:** the CFO's empty ring is neutral 8 (#868686), the budget track neutral 6 (#d2d2d2), the spent part neutral 9 (#757575), and Decline has a border-strong outline.
- Arithmetic unchanged and re-checked: $57,800 + $14,860 + $23,340 = $96,000 (60.2% + 15.5% + 24.3%).
- References this round: Brex https://mobbin.com/screens/ecf850cc-08cc-46ef-b321-8248107afc9e (approval timeline on a pushed screen with no tab bar), Remote Global HR https://mobbin.com/screens/0cbdcc18-5e9d-4678-8d0f-b8c2af3c49ab (Decline and Approve pinned at the bottom), Instacart https://mobbin.com/screens/d4e4f075-e8d2-4292-be15-b0bf2031b0db (the consequence stated before the decision).

**For the owner of `mockups/10-multi-device` (not edited here).** `desktop.html` shows this request on the web and links this piece's `tokens.css`, so its colours turn cobalt on its next render. To match the phone:
1. Re-render `desktop.png` and the mockup's `shot.png` (the phone image is this `shot.png`; its tab bar and green are gone).
2. Detail amount: "$14,860" without grey ".00" (the list rows and line items may keep cents).
3. Quote line: "Quote valid until Fri 16 Oct · Q-5571.pdf", primary text, with a clock icon.
4. "If you approve" becomes "Budget after approval"; "Facilities budget, Jul–Dec" becomes "Facilities, Jul–Dec"; "$23,340 left … of $96,000" becomes "$23,340 of $96,000 left"; the legend becomes "60% spent" and "+15% this request" starting under its segment (no "24% left").
5. Meter colours: track `neutral-light-6` (was 4), spent `neutral-light-9` (was 8).
6. Remove "Rhea Kapoor (CFO) approves next. Then PO-10482 goes to Ashbury, paid on Net 30." and the "Policy FIN-04: over $10,000 also needs the CFO" line; the policy moves to the CFO's chain row ("CFO, over $10,000 (FIN-04)"), and "PO-10482 to Ashbury, Net 30" becomes a details row with "GL account 6420 Equipment upkeep" and "Deliver by Wed 21 Oct".
7. "Approvals · 2 of 4 steps done" becomes "Sign-off · 1 of 3 approved"; Elif Demir's row gets the requester arrow instead of a check; details become "Requested it", "Procurement, compared 3 quotes", "Department head", "CFO, over $10,000 (FIN-04)", with 08:12, 09:40, "Waiting" and "Next" in a right-hand column.
8. The CFO's empty ring: `neutral-light-8` (was 7).
9. Decline: white with a `border-strong` outline, primary text, regular weight (was grey fill, red text, semibold).
10. The caption in `mockups/10-multi-device/index.html` still reads "$14,860.00"; the phone now shows "$14,860".

**Fresh-eyes audit** (fresh-context agent, against the B2B product screens and Brex; it could not open the Remote and Instacart screens through search): **3/5** ("better than before but evenly spread; two bars stacked at the bottom; no content text at 17 pt; every gap the same; copies Fennick part for part; seven lines joined with ' · '; '2 of 4 done' counted the requester; faint graphics"), then **4/5**, with four items (a blank card edge at the fold, headers bold by accident, a legend adding to 99%, tight sign-off rows), all applied after it.

**Checks:** `engine.py build` passes (1 warning: 12 text sizes from the old formula steps). `engine.py review`: the one raw value (an inset shadow on Decline) became a token border. `preflight.py html`: no errors. `check_dates.py` on `index.html`: passes; it flags "Fri 17 Oct" in older sections of these notes, which quote the mockup's past error (false positive).
