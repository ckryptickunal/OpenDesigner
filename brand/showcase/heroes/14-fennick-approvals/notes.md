# 14 Fennick: bill approvals hero (B2B)

Built in round 3, after the owner's review (`brand/showcase/ROUND3-BRIEF.md`). It is one of three heroes made for the B2B product screens the owner loves, in place of the four heroes he removed. Render: `shot.png`, 1440 × 900 at 2×.

## Direction
Fennick is the fictional accounts-payable product in `product/02-fennick-approvals`. This is its marketing hero, aimed at controllers and finance teams. What sets the product apart is in its review drawer: before you approve a bill, it shows what will be left in the operating account on the day the bill pays.

The hero puts that claim and its proof side by side:
- **Left:** a two-line headline in the buyer's words, with the one green button under it.
- **Right:** the drawer's "If you approve" ledger, footed the way an accountant foots a column. It uses tabular figures, with a $ only on the first line and the total, a single rule over the total and a double rule under it, on the figures only.

Below sits the real bills screen, flat and whole. The ledger's left edge stands exactly over the drawer's content edge in the screen (966 px), so the quote sits over its source. The double rule ends level with the button.

Feel words (the product's): **calm, trustworthy, precise**.

What makes it this brand's own: the footed sum, `$63,904.52 − 15,277.75 − 7,418.60 = $41,208.17`. These are the product's own figures, and the arithmetic works.

## References (Mobbin, cited by URL only; nothing saved)
| Reference | What it taught |
|---|---|
| https://mobbin.com/sites/sections/83a61ac1-4ad8-48d0-91be-13ac7b374e22 (Ramp) | A regular-weight headline, a live figure, then the product. My live figure is the cash-left sum. |
| https://mobbin.com/sites/sections/a5e87e77-0bc7-4b65-8f28-7cb0ecee16bb (Slash) | A large, flat screenshot of a list with a detail drawer, under the copy. |
| https://mobbin.com/sites/sections/ca1841d9-bfa2-43c6-ad49-ba6eceddf894 (Sequence) | What to avoid: a blurred colour wash and a small product. |
| `brand/showcase/b2b-study/site.md` | Rule 8: proof a reader can check. Rule 3: one primary call to action, in sentence case. |

## System (engine)
The hero uses the product's own system, extended for marketing:
- I copied `state.json`, `decisions.md`, `standards-state.json` and `standards.md` from `product/02-fennick-approvals/opendesigner/`.
- I ran `engine.py --dir …/opendesigner pick Q-brand-06 two-sets` (this sets `raw.marketingSurfaces`, which adds display sizes 42, 50 and 72), then `build`.

Everything else is the product's: the faces (Instrument Sans; the screen also uses DM Mono), the forest green #2a6141 (the button only), the warm greys, the dials and the overrides. The page uses `data-theme="light"`, with `data-density="comfortable"` on `<body>` (finding 2 in heroes/12).

## Type scale (hero)
| Size | Role | Where |
|---|---|---|
| 50 | display-md, 400, -0.025em | Headline, two lines |
| 29 | headline-sm size, tabular, 400 (total 500) | Ledger figures, on 40 px rows |
| 17 | body-lg / title-md | Ledger labels, button (500), wordmark |
| 14 | body-md / label-lg | Ledger caption, nav, Sign in |

There are four sizes, and neighbours are at least 21% apart. The embedded screen renders at 0.9333, so its 12 / 14 / 29 px read as 11.2 / 13.1 / 27 px.

## Colour and contrast (token values on white)
| Element | Colour | Contrast |
|---|---|---|
| Ink | #252423 | 15.6:1 |
| Labels | #595756 | 7.0:1 |
| Button text | white on #2a6141 | 7.3:1 |

## The picture
The picture is `<iframe src="../../product/02-fennick-approvals/index.html">`, 1440 px wide, scaled to 1344 px. At 1344 px wide the product cuts off vendor names, so I scale its 1440 layout instead. The window is 488 px tall, which shows 523 product px.

I measured the product's layout in Chrome (Playwright) at several heights. At 523 px:
- The list ends exactly on a row boundary, after Ember Valley Produce.
- The drawer's sticky footer (Reject, Approve) starts at 466 px, just under "If you approve · Operating ••4410", so no line is cut in half.

Other heights failed:
- At 579 px the footer sliced through "This bill".
- At 626 px the selected Calloway row was jammed against the window edge.
- A crop that shows the whole selected row and the drawer's full ledger (636 px) does not fit in 900 px with the copy.

The iframe is not focusable. A hidden figcaption says what the screen shows.

## Outside the tokens, on purpose
- **Nav height 56 px.** There is no nav-height token.
- **Ledger rows 40 px for the 29 px figures,** and the table is 426 px wide (1392 − 966). These line it up with the drawer.
- Each of these values is marked `od-ignore` with its reason.

## Checks
- `engine.py validate` passes, with 0 warnings and 6 notes.
- `engine.py review --project heroes/14-fennick-approvals` is clean. The first run flagged `#ffffff` in the mark (now `currentColor` on `text.inverse`), two sizes and a shadow (now an `outline`).
- `preflight.py html --medium web` reports 0 errors and 0 warnings.
- `check_dates.py --year 2026` passes. Oct 14, 2026 is a Wednesday; the ACH payment on Tue Oct 20 is a business day, one day before the Oct 21 due date.
- I re-added the arithmetic from the page: 63,904.52 − 15,277.75 = 48,626.77, and 48,626.77 − 7,418.60 = 41,208.17. That matches the product's "Left on Oct 20".
- The 14 bills in the product add up to the $92,663.95 total (checked by two fresh audits).
- `.example` rule (added 2026-10-15): the hero copy names no domain or email address and shows no shell command. The embedded product still shows `ap@bramblecote.com` in the drawer (product/02); it should become `bramblecote.example` in the product page.
- The frame is `inert`, so keyboard focus never enters the product's controls.

## Round 3 (owner review)
**What he said.** "I love the B2B product screens. They look absolutely crazy." He removed four heroes he called very ugly, and asked for three new heroes, each built around one of the B2B product screens. For each one:
- the real screen is the picture: flat, whole, readable and inside the grid;
- the hero uses the product's own system;
- it takes its own direction;
- the headline is in the user's words;
- there is one action;
- the only proof is real proof.

**What I built and changed.** Seven rounds, each audited by a fresh-context agent against this brief, the product screens, Orbika and the three references:
1. **Centred one-line headline over the screen.** Scored 3. The auditor called it the most conventional of the finance heroes. The note claimed bills arrive "matched to their PO", which the screen does not support. The selected row was jammed against the window edge.
2. **The drawer's ledger lifted into the hero as a centred one-line sum.** Scored 3. The window hid the feature the headline sells, the minus signs read as ranges, and "already scheduled" clashed with the "Scheduled 22" tab.
3. **Signed figures in a row with the button.** Scored 3. Too close to hero 13's stat row, and the crop jammed the selected row.
4. **Two-line headline beside a footed sum, on a white page.** Scored 3 (four times as an echo of hero 11). The rules ran under the labels, the ledger outweighed the headline, and its edge sat on nothing.
5. **Final.** Scored **4**. The kicker is gone (11 has the same "for finance teams" kicker). The nav is now How it works / Integrations / Pricing, so "Bills" no longer repeats the product sidebar. The rules sit on the figures only, and the figures are 29 px against the 50 px headline. The ledger's left edge stands on the drawer's content edge, and the double rule ends level with the button. After that audit, the total figure went to 500 and the caption is laid out like the drawer's own heading (label left, account right), which were its two remaining notes.

**Fresh score: 4.** The auditor called it a low 4. What still holds it back:
- At thumbnail size it is a sibling of heroes/11: a white finance page with a two-line headline on the left, a block on the right and the product below.
- The frond mark appears twice: the product uses it as the customer's workspace icon (product-side).

## Process findings
1. **There is no "start from an existing system" path** (gap). A product's marketing page should inherit the product's system; I copied its state by hand and picked Q-brand-06.
2. **Density modes don't apply on `<html>`** (bug). I set the mode on `<body>`.
3. **Cropping a live product screen needs measurement** (gap). The right window height depends on two things at once: the list's row boundaries and where the drawer's sticky footer falls. Nothing in the process tells a builder to check what a crop slices through.
4. **Fresh audits pull in different directions.** One round asked for the ledger to be bigger, the next for it to be smaller than the headline. Scoring against the same named references every round kept the changes converging.
5. **Product-side issues** (outside this folder):
   - `product/02` uses the Fennick frond as Bramblecote Foods' workspace icon.
   - `product/02` has no `data-theme`, so under an OS dark preference the iframe shows the product's unfinished dark theme.

Findings 1 to 3 are recorded with `engine.py feedback` in `opendesigner/feedback.md`. Nothing was posted.
