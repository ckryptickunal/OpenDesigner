# Product screens 01-03: process report

Three B2B product screens built through OpenDesigner from `brand/showcase/b2b-study/product-ui.md` section 5, to the bar "passes as a real top-tier B2B product". Each was rendered at 1440 × 900 (scale 2), compared with three shipped products at the same width, and fixed over three rounds. Notes per piece are in each folder's `notes.md`; audit records are in `brand/showcase/audit/product--0N-*.json`.

| Piece | Screen | Accent | Type | Frames | Final score |
|---|---|---|---|---|---|
| [01-quoin-payments](01-quoin-payments/) | Payments table: status tiles, filter chips with values, 40 rows, Edit columns popover open, 3 rows selected with the bulk bar | Deep teal `#0f6b66` | Geist + Geist Mono (IDs only); 12/14/20/24 | `shot.png`, `shot-empty.png` (filtered to nothing) | 5 |
| [02-fennick-approvals](02-fennick-approvals/) | Bills "To approve" queue with "1/2 approved", inline ✓/×, review drawer (policy, timeline, balance-after ledger, GL, PDF, comment, sticky Reject ▾ / Approve), toast with Undo | Forest green `#2a6141` | Instrument Sans + DM Mono (invoice numbers, GL code); 12/14/20/24/29 | `shot.png` | 5 |
| [03-corvane-record](03-corvane-record/) | CRM company record: "12 of 214" navigation, tabs with counts, change timeline with attribute diffs, details panel with "Set …" placeholders and one field mid-edit | Cobalt `#1f4fd1` (links and focus only) | Hanken Grotesk only; 12/14/20 | `shot.png`, `shot-palette.png` (⌘K menu) | 5 |

All three: 1440 × 900, light theme, 6/8/12 corners, borders on static surfaces and shadows only on floating layers, weights 400/500/600, tabular digits, no gradients or glass, invented brands, people and companies. Round scores: Quoin 3 → 4 → 5, Fennick 3 → 4 → 5, Corvane 3 → 4 → 5.

How sure the scores are: they are my own judgement against the references named in each `notes.md`, with the rendered measurements (sizes, weights, row heights, shadows, contrast) checked by a Playwright script. Nobody else has reviewed them yet. Each audit file lists the two weakest points I could still see.

## Process findings, most important first

### The engine is wrong or missing something

1. **The dense work-tool profile (P1) does not exist yet, so every piece started from a look no top-tier product has.** `sketch --audience dense` with plain feel words ("quiet, trustworthy", "calm, trustworthy", "focused, trustworthy") resolved roundness 0 (0 px corners), depth 30 (shadow on static cards) and two weights (labels at 400) all three times. Getting to 6/8/12 corners, borders, a 500 label weight and tabular digits took four or five `set` calls per piece (`dials.roundness 42`, `dials.depth 10`, `overrides.type.weightCount 3`, `raw.numericStyles true`). Evidence: `resolve` output before and after in each `notes.md`; feedback F-001 (Quoin, Fennick) and F-002 (Corvane). During this run another session began adding a `profiles` mechanism to `engine.py` (`default_profile`), which is the right fix.
2. **Low depth removes the shadow from floating layers as well as static ones.** At depth 10, `--ds-elevation-floating` and `--ds-elevation-overlay` are `0px 0px 0px 0px` (Quoin `tokens.css` lines 412-414). The column popover, the bulk bar, the toast, the tooltip and the command palette all need a shadow, so every piece hand-wrote a `--float` value. Dense tools need "borders for static, shadow for floating", which no depth value gives today. Feedback in all three folders.
3. **Table and record primitives are missing: row heights, a separator color, a badge and status form, and key-value rows.** Every piece invented `--row` (36 px), `--row2` (56 px) or `--kv` (34 px), a `--sep` hairline (neutral step 4, because `border.subtle` is step 7, `#c8c9cc`, too heavy for 18 rules), a 20 px badge, and the quiet normal-state status. These are the values that decide whether a table looks premium, and the engine has none of them (product-ui.md P2, P6, P8).
4. **`raw.numericStyles` is half a pattern.** It adds `.ds-text-numeric-*` with `tabular-nums`, but not the numeric cell: right alignment, a muted currency code, muted cents. All three pieces built those by hand (P3).
5. **Engine bug: `raw.monoFace "=textFace"` is accepted but written literally**, producing `--ds-font-family-mono: =textFace, ui-monospace, …` (invalid CSS). `displayFace` resolves the same syntax. Feedback F-001 in `03-corvane-record/opendesigner/feedback.md`.
6. **No on-inverse secondary text role and no palette or drawer tokens.** Toasts, tooltips and dark bulk bars all needed white at 66-80% by hand; the drawer width, palette width, keycaps and scrim blur were invented.
7. **The feel word "precise" is unknown** in all three sketches ("I don't know the feel word 'precise' yet, so I left it out"). Dense B2B buyers use it constantly (P10).

### I worked around it

8. **Preflight's M9 reports Google Fonts faces as missing** in every piece (they load from a `<link>`; Playwright confirmed every weight loaded), and it cannot see rem sizes ("font sizes in px: []"). It did catch real 8-10 px text twice (a PDF label, avatar initials), which I fixed.
9. **The engine changed under me twice.** One `build` failed with `NameError: name 'default_profile' is not defined` and one final `validate` with a `SyntaxError` at `engine.py` line 7095, both while another session was editing the engine. A retry a minute later worked both times. Parallel sessions editing the shared engine can break builders mid-run.
10. **The shared scratchpad is shared:** my audit script and crops were deleted by another session mid-run; I moved them to a named subfolder.

### What helped

- The compact control sizes (24/32/40) on `:root` were right for dense tools with no work.
- `bg.accent.subtle` and accent step 5 gave a selected-row tint and rule in each palette; `bg.danger.subtle` with `text.danger` gave a Reject tint at 6.0:1 with no tuning.
- One `set dials.warmth` call regenerated a clean neutral ramp each time (45 for Quoin, 55 for Fennick, 40 for Corvane), and validate's 164-pair contrast table meant no status color needed hand-checking.
- `font-size-29` existed for the drawer amount, so the largest figure stayed on the engine's scale.

## Checks run

- `engine.py validate` for each piece: passes, 0 warnings, 5 notes (re-run at the end, after the mid-edit `SyntaxError` above cleared).
- `preflight.py html --medium web`: only M9 false positives remain.
- Playwright measurement of each frame: sizes, weights, families, loaded faces, row heights, shadows on in-flow elements, gradients, backdrop filters (results in each `notes.md`).
- Arithmetic: Quoin tiles add up to 2,418 and the bulk-bar sum ($21,162.82) matches the three selected rows; Fennick's 14 bills add up to $92,663.95, its balance ledger to $41,208.17, and its "Waiting on me 4" matches the four bills at 1/2; Corvane's dates are consistent with "today" being Wed Oct 14, 2026.

Nothing was committed. No Mobbin image was saved; references are cited by `mobbin_url` only.
