# 11 Purlin: spend management hero (B2B)

Replaces `heroes/06-playful-fintech` (audited 2 of 5, "remake"). Render: 1440 x 900 at scale 2 (`shot.png`).

## Direction
Purlin is a fictional spend-management platform for finance teams: company cards with vendor limits, bills routed by amount, receipts matched on arrival, and a nightly sync of coded transactions to the general ledger. The buyer is a controller or finance lead at a company of 50 to 2,000 people. The hero shows the product doing the job the buyer is judged on: closing the month. One sample customer's October close is on screen at real size, with the journal entry one card transaction will post tonight. Feel words: **trustworthy, clean, precise**. Mood: a quiet, exact tool, not a fintech toy.

What the old piece did that this one must not: a gradient circle, sparkles, a "New" pill, a highlight block, two buttons plus check marks, tilted floating cards and a sticker (`audit/heroes--06-playful-fintech.json`).

## References (Mobbin, cited by URL only; no image saved)
| Reference | What it taught |
|---|---|
| https://mobbin.com/sites/sections/83a61ac1-4ad8-48d0-91be-13ac7b374e22 | Left-aligned headline, one sub-line, one action, then the product on a plain grey stage below. The stage is a surface, not art. |
| https://mobbin.com/sites/sections/85da8987-9cb3-438d-9fb5-2ca3efd9ab1b | The product as a flat, real-size window under the headline, dense and legible, with real numbers in it. |
| https://mobbin.com/sites/sections/ba4ff47e-3460-4256-b2fb-0e0948cd8eb9 | One window, whole and face-on, list plus detail panel, sitting on a tinted band; nothing floats over it. |
| https://mobbin.com/sites/sections/544ab60b-31ea-4849-aba2-e90c6a6998ed | A finance product shown as a sidebar app with tabs and status chips; how little chrome a credible product frame needs. |

Also read: `b2b-study/site.md` (headline says what and for whom; real product; one primary in sentence case) and `b2b-study/product-ui.md` (one accent, 13 px body, ledger numbers, quiet status, hairlines).

## System (engine)
```
sketch --name "Purlin" --brand "#2C3FD0" --audience regular --platforms web --feel trustworthy,clean,precise
       --theme system-light-dark --surfaces "landing page:persuade,app:operate" --delegated all
set raw.textFace "Golos Text"; pick Q-type-02 yes; pick Q-type-12 three; build
```
`--theme light-only` was refused by house standard STD-visual-details-24, so the system has both themes; the page uses semantic tokens and is rendered light.

| Dial | Sketch gave | Set to | Why |
|---|---|---|---|
| expression | 0 | 30 | Credible, product-led; 0 gave 2 px corners |
| brandPresence | 50 | 35 | Blue only on the action, selection, links, the progress bar and the mark |
| density | 50 | 62 | The product frame is a dense work tool |
| energy | 15 | 20 | Calm |
| roundness | 0 | 42 | 6 px controls, 8 px panels, 12 px window, as shipped finance tools use |
| depth | 30 | 15 | Flat: hairlines, no shadow on anything in flow |
| colorfulness | 36 | 25 | One accent |
| warmth | 25 | 20 | Cool neutrals, no cream |

## Fonts and type scale
One family: **Golos Text** (SIL OFL, Google Fonts), 400 / 500 / 600. It has tabular figures, which the ledger needs (checked in the font's GSUB table). Picked from a 16-face specimen at 44 px and 13 px; Inter was left for the phone piece and Instrument Sans was already used by `heroes/10`.

| Role | Size | Weight | Used for |
|---|---|---|---|
| Display | 57 (`--ds-font-size-57`) | 400 | Headline. Regular on purpose: the product carries the weight |
| Title | 28 | 400 | Drawer amount |
| Product page title | 19 | 600 | "October close" |
| Body / label | 16 | 400 / 500 | Nav, sub-line, button, drawer title |
| Product body / meta | 13 | 400 / 500 | Table, sidebar, drawer, kicker |

Five sizes, neighbours at least 19% apart.

## Color
White page, ink #222428 (15.5:1), secondary #505765 (7.3:1), tertiary #5c6474 (6.0:1). One blue, #2C3FD0, on the button (white text 7.7:1), the progress bar, the selected row tint, links (#2333a5, 10.1:1) and the mark. Status is a word, and only exceptions get a 6 px colored dot beside it (amber "Missing receipt", "Needs GL code"; red "Over policy"); "Ready" is plain secondary text. Green appears once, on "matched" (7.3:1). The wordmark is type only.

## Outside the tokens, on purpose
- Headline line height 1.07 and tracking -0.028em (the display token is 1.12 and -0.02em).
- `text-wrap: balance` with a 820 px measure for an even two-line break.
- Table column widths for a fixed 1:1 product frame (`od-ignore`).
- Row hairlines use the ramp step `--ds-color-neutral-light-4`: `border-subtle` (neutral-7, 1.6:1) is too heavy for row separators, and there is no separator token.

## Checks
- `engine.py validate`: passes, 0 warnings (5 notes, APCA advice for dark mode).
- `engine.py review`: first run flagged 13 raw sizes (row and control heights, dots); all moved to tokens. Now clean.
- `preflight.py html --medium web`: 1 error, M9 "Golos Text has no @font-face", a false positive (the face loads from the Google Fonts link). The `<br>` warning was fixed with `text-wrap: balance`.
- Checklist (type and layout): 5 sizes; no wraps or ellipses in the product frame; the window sits on the 12-column grid (1280 content, 80 margins); every product number is right-aligned with tabular figures.

## Self-audit (score against the four references at 1440 wide)
- **Round 1, score 2.** The window ran past the fold (not whole), the GL column collapsed to "6...", the button wrapped to two lines, and the header was 300 px tall. Fixed: shorter sub-line, 32 px top padding, window 540 px with all four edges visible, narrower columns, `white-space: nowrap` on the button, a plain "Spend management for finance teams" kicker (text, not a pill).
- **Round 2, score 3.5.** Whole and readable, but the drawer overflowed and pushed the sidebar footer out, "Tomás Echev..." and "Calder Inn, Leeds £418...." were cut, the kicker floated 60 px above the headline, the logo read as a "text align" icon, and six sample names were already used by other showcase pieces. Fixed: drawer cut to three facts plus the journal entry, kicker stacked on the headline, an F mark, fresh names (`grep` across `brand/showcase`), the receipt file renamed to match the merchant.
- **Round 2 result, score 4 (my own).** Section 11 walk: no glow, no texture, no decoration without data, no "New" pill or highlight, one button, nothing floats or tilts, no invented proof (no logos or counts), one status signal per state, regular weight carries the page, one accent.
- **Round 3, independent audit, score 4.** A fresh-context subagent scored the render against the same references and checked the arithmetic (1,284 of 1,302 = 98.6%; 11 + 5 + 2 = 18 exceptions = 1,302 - 1,284; the journal entry balances). It found what my rounds missed: "Books lock Monday 3 November" used the wrong calendar (3 Nov 2026 is a Tuesday); "Dana Whitfield" and "Priya Raman" were already used by `product/02-fennick-approvals`; "Amount, USD" overflowed its column; "Paid by" mixed people with bill numbers; "Synced 02:00 · 1,206 lines" did not connect to "1,284 ready"; the grey dot on every "Ready" row carried nothing; the F-in-a-tile logo was generic. Fixed: Tuesday; fresh names (Mirela K., Kofi M.) checked by grep; header "Amount" with "amounts in USD" in the table footer; a "Source" column with a card or bill icon before "Mirela K." or "Bill #4471"; "1,206 posted · 78 tonight" (1,206 + 78 = 1,284); no dot on "Ready"; a type-only wordmark.
- **Final, score 4.** Re-rendered and read at full size: nothing cut off, every number consistent.

## Process findings
1. **The B2B work-tool profile is still missing (gap).** `--feel trustworthy,clean` resolved expression 0 and roundness 0 (2 px detail corners), two weights and no row-height token; I set roundness 42 and `Q-type-12 three` by hand. This is `b2b-study/product-ui.md` P1, unchanged.
2. **No row-height or separator tokens (gap).** `review` suggested `--ds-space-40` for a table row height (a spacing token for a size), and row hairlines need a raw ramp step (P2, P8).
3. **Sample data collides across builders (gap).** My first draft reused six names already in other pieces, including a parallel `product/01-quoin-payments`: Halvard, Saltmarsh, Brightwater, Northgate, Adeyemi, Ferreira. My grep fixed those, and the independent audit then found two more (Dana Whitfield and Priya Raman, in `product/02-fennick-approvals`, written while I worked). Section 11 names the tell but nothing checks for it, and parallel builders keep drawing the same names.
4. **A fresh-context verifier beats self-review (process).** Three of my own rounds missed a wrong weekday, two name collisions and an overflowing header; one independent subagent audit found all of them, plus a logic error and a second wrong weekday in the phone piece. Nothing in the process checks that a weekday matches its date.
5. "precise" is not a feel word (idea); the engine said so and dropped it.
6. Helped: the product study's rules (13 px body, tabular right-aligned amounts, dot plus word status, hairlines) turned straight into CSS, and `review` caught every raw height.

All recorded with `engine.py feedback` in `opendesigner/feedback.md`; nothing posted.

## Fix round 2026-10-14
After the independent audit (`audit/heroes--11-spend-platform.json`). Render: `shot.png`, 1440 × 900 at 2×.

- **Brand renamed: Ferrow is now Purlin.** Ferrow was one letter-swap from Ferrule (product/06). A purlin is the horizontal beam that carries a roof, which fits the set's building-trade names (Quoin, Ferrule). The rename covers `index.html`, this file, `DESIGN.md`, `PRODUCT.md`, `opendesigner/state.json`, `decisions.md`, the previews, the overview and every export. `build/dtcg/ferrow.resolver.json` is now `purlin.resolver.json`. Web searches found no spend-management or corporate-card company called Purlin.
- **People and merchants.** Names that collided with other pieces were replaced: Mirela Kovač ("Mirela K.") is now Petra Szabo ("Petra S."), Tomás I. is now Arjun D., Calder Inn is now Kingsmere Inn, Kettle & Co. Catering is now Harvest Table Catering, and Corran Labs (one letter from components/06's Corrin Rail) is now Brindle Food Labs. The card is now ••7302 instead of ••4417, which was also in Kilnworks and app-screens/01.
- **Repeated numbers.** The selected transaction was $1,284.50, beside "1,284 of 1,302 ready to post". It is now $1,318.40, so the same digits don't appear twice. The journal entry still balances: Dr 6420 Repairs 1,318.40 and Cr 2010 Card clearing 1,318.40. The bill numbers #4471, #4468 and #4462 are now #3871, #3868 and #3862, because 4471 was also a Fennick invoice.
- **Re-checked.** Books lock Tue 3 Nov 2026. CET applies after Oct 25. 1,284 / 1,302 = 98.6%. 11 + 5 + 2 = 18 not ready. 1,206 + 78 = 1,284. £418.00 = $546.32 is a rate of 1.307.
- **Not changed.** The audit's design point, that the brand needs one owned element, is outside this fix round.

## Round 3 (owner review, 2026-10-15)

**What he said.** "Okay-ish." It had to become clearly better, at the level of the B2B product screens and the Orbika hero. The earlier audit (score 4) called the layout a conventional SaaS hero on a pale lavender band, the blue a generic royal blue, the wordmark plain, and nothing besides the product UI ownable.

**What changed.**
- **One element only this brand owns, made big: the October ledger.** Purlin's promise is that coded spend reaches the ledger every night. The "October close" screen now opens with it across the whole main area: one column per night from 1 October to the day the books lock, the lines posted at 02:00 ET each night. The 27 nights so far add to 1,206 and dip on weekends (1 October 2026 is a Thursday); tonight's 78 is the one blue bar, labelled "Tonight"; the five nights to come are baseline ticks; an ink rule marks "Books lock, Tue 3 Nov".
- **Blue has one job: what posts tonight.** The tonight bar and its label, "78 tonight", the "Posts tonight" statuses and the journal entry's header. The button is ink, links are ink with an underline, the selected row is a neutral fill with an ink rule, "matched" is plain text. The hue is the engine's brand seed, kept; its job is what changed.
- **The finance logic holds.** 1,206 posted + 78 tonight = 1,284 coded and matched; 11 + 5 + 2 = 18 held; 1,302 in all. Rows dated Oct 28 "Post tonight"; older rows say "Posted" with that night's journal entry (one entry per night: JE-1026, JE-1027, tonight JE-1028); exceptions are held. One geography: USD books, Eastern time (02:00 ET; EDT until US daylight time ends on 1 November). The sidebar's last sync posted 61 lines, the height of the Oct 27 bar.
- **A mark.** A purlin is the beam that carries a roof; the mark is a Z-purlin in section, beside the wordmark.
- **Product craft.** Cents in a lighter tone; filter tabs on their own row on top of the table; the sidebar's empty gap now holds ledger settings shown nowhere else (period Oct 2026 open, base currency USD, card clearing 2010, entries one per night); the lavender band is gone; the frame grew to 568 px; 40 px between header and frame.
- **Footers and actions.** The table's footer is a ruled band directly under the last row; "Edit coding" sits in the drawer's header. The journal-entry box is labelled "Its lines in tonight's JE-1028", so its two lines read as this transaction's share of the night's entry.
- **Removed:** the £418.00 note on Kingsmere Inn (it truncated) and the dashed future bars.

**Type scale.** Unchanged: Display 57 · Title 28 · Product title 19 · Body 16 · Product body 13; one family, Golos Text.

**Checks.** `engine.py review`: the code uses the tokens (bar heights are data, marked `od-ignore`); DESIGN.md refreshed. `preflight.py html`: no errors or warnings. `check_dates.py`: `index.html` passes; it flags "Monday 3 November" in this file's round 2 notes, which quote the old error (a false positive).

**Fresh-eyes audit.** A fresh-context subagent scored it against the B2B screens, Orbika and shipped fintech heroes on Mobbin (the three links in the earlier notes returned 403 to it, so it compared Mercury https://mobbin.com/sites/sections/254b0eb2, Origin https://mobbin.com/sites/sections/7617d355 and Ramp https://mobbin.com/sites/sections/7c14b269 from a search).
- Round 1, **3**: the first pass (a small posting strip in the header, a mark, no band) read as the same page as before; blue still had four jobs; "1,284 ready to post" next to "1,206 posted"; no row ever said "Posted"; USD books with CET times.
- Round 2, **4**, "clearly better": the full-width ledger is the element only this brand would show, the ink button is more serious, rows show the nightly posting. Small notes: two labels on one line, a sidebar checklist that repeated the main area, journal-entry numbers with no rule, a floating footer, a drawer with no action.
- Round 3, **4**: those fixed; its last nits (a padded last row, a phrase split across label and value, the journal-entry box reading as the whole entry) were then fixed.
It re-added every total (27 nights = 1,206; 1,206 + 78 + 18 = 1,302; 11 + 5 + 2 = 18), checked every weekend dip against the 2026 calendar, Tue 3 Nov, EDT on 28 Oct, and the journal entry; text contrast on the pixels is 5.88:1 or better, bars 4.58:1. What it says keeps the piece below 5: the header is still the stock kicker, headline, paragraph and button, and the blue hue itself is generic.
