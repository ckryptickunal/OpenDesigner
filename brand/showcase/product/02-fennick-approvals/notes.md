# 02 · Bill approvals · Fennick

## Direction
Fennick is a fictional accounts-payable product. The screen is "Bills → To approve" as the CFO of the fictional company Bramblecote Foods sees it: a queue of 14 bills with approval progress and inline ✓/× on each row, and the review drawer open on one bill. The drawer states the amount, the policy that applies ("Over $5,000: needs CFO approval"), the approval timeline, the consequence before the decision ("If you approve … Left on Oct 20 $41,208.17"), the GL account and department, the invoice PDF, a comment, and a sticky footer with Reject ▾ and Approve. Two more frames show the temporary states one at a time: `?state=toast` (`shot-toast.png`) confirms the bill approved a moment ago, names the next step and offers Undo; `?state=tooltip` (`shot-tooltip.png`) is the Approve hover, where the ⌘↵ shortcut lives instead of on the page.
Feel words: **calm, trustworthy, precise** (the engine dropped "precise").

## References (Mobbin, cited by link only; nothing saved)
| Reference | What it taught |
|---|---|
| Mercury reimbursement drawer, https://mobbin.com/screens/acd32944-7f4b-445f-a510-5a7750b11a19 (seen this session as https://mobbin.com/screens/8156ac94-1476-4ca2-801e-89444dd78545) | Amount large with cents smaller, status badge beside the title, Approve in the accent next to a red-tint Decline and More; the approve tooltip that states what approving does |
| Mercury transaction drawer, https://mobbin.com/screens/07eac28e-2b9d-478a-bb1b-fb83fae7285e | Drawer anatomy: vertical mini timeline with times, GL code select, notes, attachments, "Mention a team member with @"; the list stays visible beside it |
| Acctual bills queue, https://mobbin.com/screens/4b992650-0ce5-4fc7-9efb-8407b7ac70ac | Tabs with counts (Draft 1 / Approve 2 / Ready for payment 3 / Paid 2), "0/1 Approved" in the status column, inline ✓ and × per row |
| Airwallex approval flow, https://mobbin.com/flows/9afbce42-5ab9-4c7a-a574-2b6b83cde1fd (and the bills list https://mobbin.com/screens/d4f450ab-2275-48d3-8c19-f0c5a4a7ab2f) | A sticky footer with "Reject ▾" and the next-step primary; after approving, say what happens next |

## System (engine)
`sketch --name "Fennick" --brand "#2a6141" --audience dense --platforms web --feel calm,trustworthy,precise --theme system-light-dark --delegated all --surfaces operate`

The sketch resolved expression 0, roundness 0, depth 30, two weights. P1 dense profile set by hand (`--set-by delegated --why "P1 dense work-tool profile, brand/showcase/b2b-study/product-ui.md"`):

| Setting | Value | Result |
|---|---|---|
| dials.roundness | 0 → 42 | 6 px controls, 8 px panels and file row, 12 px toast; badges 4 px |
| dials.depth | 30 → 10 | borders only on static surfaces |
| dials.colorfulness | 20 | one accent |
| dials.warmth | 25 → 55 | greys with a faint warmth (#f4f4f4 … #252423), kept under 60 so nothing turns brown |
| overrides.type.weightCount | 3 | labels at 500 |
| raw.numericStyles | true | tabular digits |
| raw.textFace / monoFace | Instrument Sans / DM Mono | SIL OFL, Google Fonts; tabular figures confirmed by measuring "1111111111" and "0000000000" at equal widths with tabular-nums |

## Type (two families)
Instrument Sans for everything; DM Mono only for invoice numbers, the GL code "6420" and the PDF file name. Five sizes, none within 10%:
- 12 label/meta: column headers, invoice numbers, relative due dates, timeline times, badges
- 14 body: rows, drawer text, buttons
- 20: the cents of the drawer amount
- 24 headline: page title "Bills"
- 29: the drawer amount (`font-size-29`, weight 500, tabular)
Weights 400 / 500 / 600.

## Color
One accent, forest green `accent-9 #2a6141`: New bill and Approve, the open row's tint and left edge, approval pips, completed timeline steps, the filter value. Red only where something is wrong or destructive: "2 days overdue" and the red-tint Reject. Everything else is warm-neutral grey. The toast and tooltip are near-black (`bg.inverse`).

## Where I stepped outside the tokens, and why
- `--row2: 56px` two-line rows, `--badge: 20px`: no row or badge tokens.
- `--sep` (neutral 4) and `--line` (neutral 5): no separator role; `border.subtle` is neutral 7.
- `--float` shadow on the toast and tooltip, `--drawer-shadow` on the drawer edge: depth 10 zeroes every elevation.
- White at 68-80% for secondary text on the toast and tooltip: no on-inverse secondary role.
- The drawer amount's cents at 20 px: there is no "money" style that splits whole and fraction.

## Checks
- `engine.py validate`: passes, 0 warnings, 5 notes.
- `preflight.py html --medium web`: the first run flagged an 8 px "PDF" label and 10 px avatar initials (M8); replaced the label with the file icon and set initials to 12 px. The final run has 2 errors, both false positives (M9: Instrument Sans and DM Mono load from a Google Fonts `<link>`; a Playwright check confirmed Instrument Sans 400/500/600 and DM Mono 400 loaded).
- Rendered measurements (Playwright, 1440 × 900): sizes 12/14/20/24/29; weights 400/500/600; families Instrument Sans + DM Mono; 12 visible rows at 56 px, header 32 px; no gradients, no backdrop-filter. In-flow shadows: 1 px rings on the active nav item and the segmented control, and the drawer's edge shadow (the drawer is a floating layer over the list).
- Arithmetic holds: the 14 amounts add up to the "$92,663.95 total"; $63,904.52 − $15,277.75 − $7,418.60 = $41,208.17.
- Targets: row ✓/× buttons are 26 px (pointer floor 24 px).

## Rounds (self-audit against Mercury acd32944, Acctual 4b992650 and the Airwallex flow 9afbce42 at 1440 wide)
1. **Score 3.** "1/2 approved" was truncated to "1/2 approved…" in four rows; bordered ✓/× boxes on all 14 rows made a column of 28 buttons; the toast wrapped to two lines; the drawer ran 60 px past its footer; the last timeline step ended in a stray "EDT".
2. **Score 4.** Widened the approvals column; row ✓/× became quiet ghost icons, bordered only on the open row; toast cut to one line that still names amount, date and account ("$3,912.08 pays on Oct 17 from Operating ••4410", with Undo); drawer spacing tightened so the comment shows; "ACH payment on Oct 20 · after approval".
3. **Score 5.** Replaced the "F" letter tile (the generic initials device the audits flag) with a small frond mark; swapped the 8 px PDF label for the file icon and the 10 px initials for 12 px; tabular digits on the whole table. Next to the references, the drawer does more than Mercury's (the balance-after ledger and the named policy) without extra chrome, and the queue matches Acctual's density with real counts.

Honest limits: the drawer's comment box sits half behind the sticky footer (the drawer scrolls, as Mercury's does), and the queue shows no bulk selection.

## Process findings
1. **The P1 profile had to be set by hand again:** "calm" sends expression to 0, which with density 80 gives 0 px corners. F-001.
2. **No two-line row token and no drawer tokens** (width, edge elevation). F-002.
3. **No on-inverse secondary text role** for toasts, tooltips and dark bars. F-003.
4. **Depth 10 removed the toast's and tooltip's shadow** (overlay elevation is zero). F-004.
5. **Helped:** `font-size-29` existed for the drawer amount, so the big figure stayed on the scale; the danger-subtle background and danger text gave a Reject tint that passes contrast with no hand-tuning; changing warmth to 55 produced warm greys that are not brown.

## Fix round 2026-10-14
After the independent audit (`audit/product--02-fennick-approvals.json`). Renders: `shot.png`, `shot-toast.png`, `shot-tooltip.png`, each 1440 × 900 at 2×.

- **Payment on a business day.** The toast said Harlow Print Co. "pays on Oct 17", which is a Saturday, and ACH does not settle on weekends. It now pays on Fri, Oct 16, the business day before. That keeps it inside the drawer's "6 bills scheduled before Oct 20" and the "Scheduled 22" tab, both counted after Harlow's approval. No balance changes: $63,904.52 − $15,277.75 − $7,418.60 = $41,208.17. Calloway's ACH on Tue, Oct 20 is a business day.
- **Wait time.** "Waiting for you, CFO · 5 days" is now "4 days". The budget owner approved on Sat, Oct 10 at 9:03 AM, and today is Wed, Oct 14.
- **Quarter.** The comment's "Q4 fuel surcharge" sat on an invoice dated Sep 21, which is in Q3. It now says "Includes the fuel surcharge we agreed on Sep 2. Fine to pay." That fits on one line, so the reply field no longer cuts off at the drawer's edge. Drawer section padding also went from 14 to 13 px.
- **One temporary state per frame.** The main frame is the review drawer on Calloway Freight Brokers only. The toast and the hover tooltip each have their own frame, so neither covers the Brightline Telecom row or the comment field in the main frame.
- **Names and numbers.** The signed-in CFO Marcus Oyelaran ("MO") is now Gideon Afolabi ("GA"). Dana Whitfield ("DW") is now Lorna Petrakis ("LP"). Vendors that collided with other pieces were replaced: Quillon Software became Kanbrook Software (`KS-2026-1009`), because Quillon is the mobile approvals app. Wrenfield Water Co. became Sagebrush Water Co., and Northgate Uniform Supply became Workline Uniform Supply (`WUS-77812`). Pellworth Insurance Brokers became Dunstan Insurance Brokers (`DIB-11-2026`), because "Pell" names were in three other pieces. The GL account is now 6150 Freight & shipping, because 6420 is the hero's Repairs account.
- **Re-checked.** All 14 due dates and "in N days" against Wed, Oct 14 2026 were checked with Python. The 14 amounts still add up to $92,663.95. "Waiting on me 4" still matches the four 1/2-approved bills over $5,000.
