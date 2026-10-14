# 01 · Payments table · Quoin

## Direction
Quoin is a fictional payments platform. The screen is the "Payments" table that a mid-market company's finance operations and support agents keep open all day The workspace is the fictional "Tamsin & Rowe", a wholesale supplier of tableware and kitchen equipment to restaurants, hotels and caterers in the US, UK and EU, so every customer in the table is a hospitality business paying for an order or an invoice. One job: find and act on payments. Status tiles that double as quick filters, filter chips that show their values, a dense table, and three rows selected with the bulk bar. Two more frames show one temporary state each: `?state=columns` (`shot-columns.png`) opens Edit columns with nothing selected, and `?state=empty` (`shot-empty.png`) shows the table filtered to nothing.
Feel words: **precise, quiet, trustworthy** (the engine knew "quiet" and "trustworthy"; it dropped "precise").

## References (Mobbin, cited by link only; nothing saved)
| Reference | What it taught |
|---|---|
| Stripe transactions + edit columns, https://mobbin.com/screens/140880ca-003b-4498-8932-c09c223ed9de (seen again this session as https://mobbin.com/screens/d1ccc54c-679b-406f-893a-8c18cb5690f3) | Status tiles with counts as quick filters, the selected tile outlined in the accent, "Fixed columns" plus drag handles in the column popover, "6 results" count |
| Stripe date filter, https://mobbin.com/screens/5aba8f78-028a-4ad6-81f1-6ca698a41451 | A filter chip shows its value in the accent beside its name, plus "Clear filters" |
| Mercury transactions, https://mobbin.com/screens/fa5c5663-2455-49da-b9c5-8d8cece557a6 and https://mobbin.com/screens/f77b24a7-e68e-4fc1-b5ac-91856a92f12b | Ledger amounts: right-aligned, cents lighter, a failed amount struck through; status shown only when it is not the normal state; the table-options popover with a time zone |
| Attio contacts with bulk bar, https://mobbin.com/screens/5bb2a956-b937-497e-bd31-afc2616bb111 (and https://mobbin.com/screens/f6aa5c36-a41b-432f-a620-5248fb8bc7b0) | Pale accent tint on selected rows, a floating bar at the bottom center that leads with "3 selected", 3-4 verbs, More and × |

## System (engine)
`sketch --name "Quoin" --brand "#0f6b66" --audience dense --platforms web --feel precise,quiet,trustworthy --theme system-light-dark --delegated all --surfaces operate`

The sketch resolved roundness 0 (0 px corners), depth 30, colorfulness 36, warmth 25 (slate-blue greys) and two weights. P1 dense profile set by hand, each with `--set-by delegated --why "P1 dense work-tool profile, brand/showcase/b2b-study/product-ui.md"`:

| Setting | Value | Result |
|---|---|---|
| dials.roundness | 0 → 42 | radius.control 6, container 8, overlay 12, control-sm 4 |
| dials.depth | 30 → 10 | borders model; static surfaces have no shadow (but see findings: floating ones lost theirs too) |
| dials.colorfulness | 20 | one accent; status hues stay muted |
| dials.warmth | 25 → 45 | near-neutral greys (#f3f4f5 … #232426); the slate-blue greys fought the green-blue teal |
| overrides.type.weightCount | 3 | label weight 500: column headers, tile labels, buttons |
| raw.numericStyles | true | `.ds-text-numeric-*` with tabular-nums |
| raw.textFace / monoFace | Geist / Geist Mono | SIL OFL, from Google Fonts |

Expression 20, brandPresence 20, density 80, energy 15 were left as the sketch set them.

## Type (two families)
Geist for everything; Geist Mono only for payment IDs (`qpy_3NfT8kQ2aXwL`). Four sizes from the engine scale, no two within 10%:
- 12 label/meta: column headers, chips, badges, IDs, counts (`label-sm/md`, `code-sm`)
- 14 body: cells, buttons, nav (`body-md`)
- 20 numeric: tile counts (`numeric-lg`, weight set to 500)
- 24 headline: page title "Payments" (`headline-sm`, 600)
Weights 400 / 500 / 600 only. The scale's 17, 29 and 35 are unused.

## Color
One accent (teal `accent-9 #0f6b66`): primary button, selected tile, filter values, checkboxes, selected-row tint (`bg.accent.subtle`), links. Status: green only in the ✓ glyphs of the quiet "Succeeded" state (no fill); Refunded and Uncaptured are grey badges with an icon; Disputed would be the one amber badge, but no disputed payment is on screen, because a payment made this morning can't be disputed yet; the × on the "Failed 38" tile is the only red on screen (three card declines are rows 22, 30 and 36, below the fold, with struck-through amounts).

## Where I stepped outside the tokens, and why
- `--row: 36px` and `--badge: 20px`: no row-height or badge token exists.
- `--sep: neutral-light-4` for row hairlines: `border.subtle` is neutral 7 (#c8c9cc), too heavy for 18 rules; there is no separator role. `--line: neutral-light-5` for tile, chip and button edges.
- `--float` shadow on the popover and bulk bar: depth 10 makes `elevation.floating` and `elevation.overlay` `0px 0px 0px 0px`.
- Bulk bar text on `bg.inverse` uses white at 66-72% for the sum and icons (no "on-inverse secondary" role).
- Muted cents (`.c`), muted currency code (`.cur`) and the quiet normal-state badge: no numeric-cell or status-form tokens.

## Checks
- `engine.py validate`: passes, 0 warnings, 5 notes (APCA advice in dark mode, 24 px smallest control, orphan steps, unasked asset hooks).
- `preflight.py html --medium web`: 2 errors, both false positives: M9 "Geist has no @font-face". The faces load from a Google Fonts `<link>`; a Playwright check found Geist 400/500/600 and Geist Mono 400 loaded and `document.fonts.check` true. Preflight also lists "font sizes in px: []" because every size is a rem token.
- Rendered measurements (scratch Playwright audit, 1440 × 900): font sizes 12/14/20/24; weights 400/500/600; families Geist + Geist Mono; 18 body rows at 36 px, header 32 px; no gradients, no backdrop-filter; the only in-flow shadow is the 1 px ring on the active nav item (a border drawn as a ring). Amount cells right-aligned with tabular-nums.
- Contrast: all text uses engine roles checked by validate (164 pairs). Measured: tertiary text (#636468) is 5.9:1 on white and 5.0:1 on the selected-row tint; the Disputed badge text is 5.0:1 on its tint; bulk-bar secondary text (white at 66% on #232426) is 7.6:1.
- Status never uses color alone (icon + word in every badge; the tile × sits beside the word "Failed").

## Rounds (self-audit, each against Stripe 140880ca, Mercury a930c1be/fa5c5663 and Attio 5bb2a956 at 1440 wide)
1. **Score 3.** The app grid grew past the viewport, so the bulk bar and the sidebar's Developers/Settings were off screen. "Succeeded" was a grey-filled badge on 80% of rows: a column of fills that made the exceptions harder to find (slop table: "the normal state has no fill").
2. **Score 4.** Fixed the grid (`grid-template-rows: 100vh`, `min-height: 0`). Succeeded became a quiet ✓ + word with no fill, so Uncaptured, Refunded and Disputed read as the exceptions. The bulk bar now leads with the count and the selection's sum, "$21,162.82 USD" (the three amounts add up). Payment method changed from a 12 px rail label to "Card •••• 4409" at body size. Rendered the empty-filter frame.
3. **Score 5.** Badges were 1-2 px high against the row baseline (inline-flex baseline); now `vertical-align: middle`. Empty frame: header checkbox no longer shows the indeterminate state with nothing selected; empty-state title names the full customer. Tiles 4 px shorter. Next to the three references at the same width nothing reads as invented: odd amounts in three currencies, rails (ACH, SEPA DD, Bacs, Wire), mono IDs, EDT stated once, counts that add up (2,291 + 61 + 4 + 3 + 59 = 2,418).

What still separates it from the real thing, honestly: there is no row hover or keyboard focus state in the frame, and the column popover lists only 11 columns where a real product has 20 or more.

## Process findings
1. **The P1 profile had to be set by hand.** `--audience dense` plus "quiet, trustworthy" resolved to 0 px corners, two weights and a shadowed raised card (depth 30). Four `set` calls fixed it (roundness 42, depth 10, weightCount 3, numericStyles). Feedback F-001, F-005.
2. **Depth 10 removes the shadow from floating layers too** (`elevation.floating: 0px 0px 0px 0px`). Dense tools want borders on static surfaces and a real shadow on popovers, menus and the bulk bar. F-002.
3. **No row-height token and no separator color.** 36 px rows and the neutral-4 hairline were invented. F-003.
4. **numericStyles is half a pattern:** tabular-nums yes, but no right-aligned numeric cell, muted code or muted cents. F-004.
5. **No status form.** Badge height, the quiet normal state and tinted exception badges are all hand-made. F-006.
6. **Helped:** the compact control sizes (24/32/40) on `:root` were right with no work; the accent ramp gave a usable selected-row tint (`bg.accent.subtle`) and border (`accent-5`); validate's contrast table meant no status color needed hand-checking; changing warmth regenerated a clean neutral ramp in one command.
7. **Preflight still reports Google Fonts faces as missing** (M9) and cannot see rem sizes (known from components/06).

## Fix round 2026-10-14
After the independent audit (`audit/product--01-quoin-payments.json`). Renders: `shot.png`, `shot-columns.png`, `shot-empty.png`, each 1440 × 900 at 2×.

- **One temporary state per frame.** The Edit columns popover was open over the Created and Payment ID columns while three rows were selected. The main frame now keeps only the selection and the bulk bar, so the dates and mono IDs read. The popover moved to its own frame (`?state=columns`), with nothing selected and no hover row inside it.
- **Uncaptured only on cards.** The EUR row marked Uncaptured was a SEPA Direct Debit, and a second Uncaptured row was ACH. Only a card authorisation can be held uncaptured, so all three Uncaptured rows are now card orders.
- **One kind of business.** "Tamsin & Rowe" is now a wholesale supplier of tableware and kitchen equipment, and all 40 customers are restaurants, hotels, caterers, cafés and event venues. Descriptions are only "Order …" (card orders) or "Invoice …" (invoices paid by card or by bank transfer). The retainers, subscriptions and seat memberships are gone.
- **Rows that fit the counts.** 2,418 payments in 7 days is about 15 an hour, but the 40 rows spanned two and a half days. All 40 are now the last two hours (Oct 14, 09:00 to 11:02 EDT), and order numbers fall with time. That made three more facts visible, each fixed:
  - A disputed payment created that morning is impossible. The visible dispute became a normal payment, and the Disputed tile is 1. The sidebar's open disputes (all time) is 6, so it is no longer equal to this week's count.
  - A direct debit created this morning would still be pending, and could not have failed yet. The bank rails on screen are now transfers the customer sends (ACH, Wire, SEPA credit, Bacs). The failed SEPA debit is a declined card.
  - Three failures in two hours against "Failed 3" for the week did not fit. The tiles are now 2,259 + 61 + 1 + 38 + 59 = 2,418, re-added. Only one refund is visible (an order cancelled the same morning).
- **Names.** The signed-in user Mira Okafor ("MO") is now Celeste Arnaud ("CA"). Customers that collided with other pieces were replaced: Calder & Voss, Tidewell, Kovač, Juniper & Pell, Halvard, Brightwater, Quarry Lane, Fenwick (close to Fennick), Harrowfield (close to Harrowgate), Northbank, Norrell (close to Norrland) and Corlett (close to Corlay in mockups/10). The empty frame now names Penwarden Hotels. Every name was checked against `brand/showcase/NAMES.md`.
- **Unchanged and re-checked.** The selection sum is $452.08 + $1,029.99 + $19,680.75 = $21,162.82. The column popover's "7 of 11 shown" is 1 fixed + 6 shown, with 4 hidden. EDT (UTC−4) is right for Oct 14.
- **Outside this folder.** `mockups/09-laptop-dashboard` places this `shot.png` on a laptop. Its alt text still says "the Edit columns panel open", which is now in `shot-columns.png`. Its "2,418 payments" caption still holds.

## Rework 2026-10-14
After the second independent audit (`../../audit/product--01-quoin-payments.json`, and `audit/mockups--09-laptop-dashboard.json`, which shows this screen), which found the page nearly copied Stripe's Transactions page: the same six status tiles in the same order (All, Succeeded, Refunded, Disputed, Failed, Uncaptured), the same filter chips and button labels (Export, Create payment, Edit columns) and Stripe-style payment IDs (`qpy_3N…`). The rule it broke is now in `making.md` section 11 ("A reference rebuilt too closely"). The sections above describe the Payments version and are kept as its record; this section replaces them where they differ. Renders: `shot.png`, `shot-match.png` and `shot-empty.png`, each 1440 × 900 at 2×.

**What the screen is now.** Quoin is a receivables product for wholesale suppliers, and the screen is **Receipts**: the money Tamsin & Rowe's customers send, matched to the invoices it pays. That is the job the finance team does all day (cash application). Card orders match themselves, so the work is bank money: ACH, wires, checks from a lockbox, SEPA credits, Bacs and Faster Payments (FPS), each with whatever reference the customer typed.

| Before (Stripe's structure and identity) | Now (this product's own) |
|---|---|
| Six count tiles, All first, as quick filters | Four money figures as plain text with no cards (Received, Matched to invoices with a meter, Waiting to match, Held as credit), then four queue tabs in the order the team works them: To match 192, Held as credit 63, Matched 2,163, All 2,418. The main frame opens on To match, not All |
| Succeeded, Refunded, Disputed, Failed, Uncaptured | The states a supplier's receipts really have. **Suggested** is the queue's normal state, so it is an icon and a word with no fill: an exact amount with no invoice number in the reference ("amount only, no ref"), two invoices that sum to it ("+1 sum of 2"), or a reference one digit off ("reference close"). **Part payment** (also quiet): a refit paid in stages, "leaves $14,544.67". **Short** (grey fill, with the amount): paid less than billed, a wire fee or a deducted breakage. **2 sets fit** (grey fill): two sets of open invoices add up to the amount. **No match** (the only amber): no open invoice of that size, or a payer who is not a customer, shown by the name the bank sent ("VARNHOLD HOSP GRP LLC"). Three of the 16 visible rows are amber |
| Created, Currency and dashed "+ Amount / + Payment method / + More filters" chips, "Clear filters" | One Filter button, then only the filter in force ("Received Oct 1 – 14"); chip values in ink, not the accent; "Match rules" instead of "Edit columns"; a freshness stamp ("bank feeds updated 11:06") |
| Export / Create payment | Import bank file / Record receipt |
| Amount, Status, Payment method, Customer, Description, Created, Payment ID | Received, Customer, Their reference (the raw bank text, the reason matching is needed), Paid by, Amount, Match, Invoice, Receipt |
| `qpy_3NfT8kQ2aXwL` | Receipts `RC-412917` (sequential) and Tamsin & Rowe invoices `TR-256379` |
| Bulk bar: Export CSV, Add to review, Refund… | "3 selected $21,162.82 USD", then Confirm matches, Hold as credit, Assign… The three are suggestions from the 08:30 ACH file |
| Second frame: the Edit columns popover (Stripe's "Fixed columns" with drag handles) | `shot-match.png` (`?state=match`): the match panel for Stonebridge Hall's $12,960.00 ACH with the reference "PAYMENT". Their four open invoices are weekly deliveries; $4,320.00 plus either of two $8,640.00 invoices makes the amount, so Quoin left it for a person. The panel has the oldest-first pick checked, the tally ($12,960.00 selected, $0.00 left over) and an option to save that pick as a match rule. The old `shot-columns.png` no longer matches the page and was moved to the macOS Trash (recoverable) |
| Empty frame: no failed payments for one customer | `shot-empty.png`: To match filtered to Penwarden Hotels: "Nothing to match", their 12 receipts are 11 matched and $212.40 held as credit, the money figures follow the filter, and there is one action (Clear customer filter) |

**Kept.** 36 px rows on hairlines, right-aligned tabular amounts with muted cents and currency code, three currencies, one teal accent (primary button, selected tab and its count, checkboxes, selected-row tint, the matched meter), one temporary state per frame, the dark bulk bar that leads with the count and the sum, Geist with Geist Mono only for IDs, sizes 12/14/20/24 and weights 400/500/600.

**Rates that hold the page together** (also in the script's comments).
- The period is Oct 1–14, 10 working days: 2,418 receipts is about 250 a working day. Receipt numbers run at that rate: RC-412603 (Tue Oct 13, 05:00) to RC-412917 (Wed Oct 14, 11:04) is 314, about 1.25 working days.
- Tamsin & Rowe issues about 230 invoices a working day; TR-261480 was issued this morning, so an invoice on Net 30 due today is about TR-256300. Every invoice on the page is three to seven weeks old, as invoices paid by bank transfer are, and every due date is its issue date plus Net 14 or Net 30 (the old `QN-20418` invoices were paid the day they were issued).
- Arrival times: next-day ACH settles at 08:30 ET and the first same-day window at 13:00; the lockbox check file lands at 09:40; SEPA credits at 05:00 EDT (11:00 CEST) and Bacs at 02:10 EDT (07:10 BST), both summer times running to Oct 25 and EDT to Nov 1; wires and Faster Payments any time.

**Totals, re-added from the page.**
- Received = matched + waiting + held: $2,492,802.73 + $311,482.09 + $41,906.55 = $2,846,191.37 (USD at booking rates, EUR 1.165 and GBP 1.34); receipts 2,163 + 192 + 63 = 2,418. Matched is 87.58% of value, shown as 87.6%.
- Waiting covers its own rows: the 19 receipts in the table come to $148,599.49, so the other 173 average about $940 (matched receipts average $1,152).
- Bulk bar: $452.08 + $1,029.99 + $19,680.75 = $21,162.82, all USD.
- Shorts: $18,425.00 − $18,400.00 = $25.00; $6,512.50 − $6,400.00 = $112.50; €4,047.00 − €4,012.00 = €35.00. Part payment: $40,560.00 invoice − $26,015.33 = $14,544.67 left.
- Match panel: $4,320.00 + $8,640.00 = $12,960.00; TR-256178 was due Sun Oct 11, 3 days before Wed Oct 14.
- Empty frame: $18,210.20 + $0.00 + $212.40 = $18,422.60 (98.8% matched); tabs 0 + 1 + 11 = 12.
- `check_dates.py --year 2026` passes; it skips script data, so the weekdays in the script were worked out by hand (Oct 13, 2026 is a Tuesday and Oct 14 is a Wednesday).

**Dark mode (found by the review skill's check).** The bulk bar's sum, icons and dividers were white at 66%, 72% and 16%. In dark mode `bg.inverse` is a light grey, so the sum read 1.14:1. They are now `text.inverse` mixed into `bg.inverse` (`color-mix`), which holds in both themes: from computed colors, the sum is 7.5:1 in light and 5.4:1 in dark, the icons 8.7:1 and 6.6:1. The workspace mark had the same fault (white squares on `bg.inverse`) and now draws in `text.inverse`.

**Fresh audit (a reviewer that did not build it), 4 of 5,** against Deel's Payments due, Mercury's Transactions and Xero's bank reconciliation; nobody could name Stripe or any one product from it. Its four must-fixes are fixed:
1. Three customer names were real hospitality businesses: Whitlock Inn (Marietta, Georgia), Hotel De Zwaluw (Texel) and Ravintola Saaristo (Helsinki). They are now Thackery Inn, Hotel Brakelduin BV and Ravintola Kuusiluoto Oy. Ravensworth Inns Ltd, the closest of the rest to real inns, is now Haddleby Inns Ltd. Their bank references changed with them.
2. Stonebridge Hall said "No match" in amber while its note said two sets of invoices fit: it is now its own neutral state, "2 sets fit", which agrees with the match panel.
3. The three volume rates disagreed (receipts per day from the summary, from the receipt numbers and from the invoice numbers): fixed by the two-week period and renumbered receipts above.
4. "Waiting to match" ($187,264.18) was smaller than its own rows allow: now $311,482.09, with Matched lowered by the same amount.
It also asked, and these were done: the bank's payer name instead of "Unknown payer", a reason on exact-amount suggestions, a "Part payment" state, a wider Match column, quiet Suggested badges, the freshness stamp, ACH at real settlement times, one action in the empty state and the avatar initials centred. A wire reference that contained "4410" (product/02's operating account) became "77-3815", and "GRV AP 4471" became "GRV AP 5208" (4471 is used in three other pieces).

**Names.** New: Thackery Inn, Hotel Brakelduin BV, Ravintola Kuusiluoto Oy, Haddleby Inns Ltd, and the payers Varnhold Hosp Grp LLC and Granthorpe Events Ltd. Each was searched in `NAMES.md` (with its distinctive words) and on the web: no business by those names; the nearest were the Ellerby Country Inn (which ruled out "Ollerby Inn"), the Hundleby Inn, Merivale in Sydney (which ruled out "Meridale") and two Finnish islands called Kuusiluoto with no restaurant. `NAMES.md` dropped the 22 customers no longer on the page and the five renamed ones, lists the names visible in `mockups/09` with both pieces, and replaces this piece's card endings with bank account 6120 and checks 7716 and 3302.

**Checks.** `engine.py validate` passes (0 warnings). `engine.py review --project` lists 89 raw values (1 shadow, 88 px sizes; the page before the rework had 75, 8 of them colors): the page writes spacing in px, as it did before, and the shadow is the `--float` value recorded above. Spacing was not moved to tokens in this round.
