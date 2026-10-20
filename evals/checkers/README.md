# Checker evals

These evals test OpenDesigner's own audit tools. Each fixture page has known defects planted in it, and the eval scores how many of them each checker catches. Clean pages, with none of those defects, measure false alarms. When a checker misses a defect, the miss stays on record: nobody edits the fixture until the checker passes.

```
python3 tools/checker_evals.py              every checker, plus the history of site/check_layout.py
python3 tools/checker_evals.py --repeat 2   run everything twice and record whether both runs agree
python3 tools/checker_evals.py --checker dates --no-history --no-write
```

You need Python 3.10 or later, Playwright for Python and the installed Chrome. The fixtures are served on 127.0.0.1 only. Results go to `results/<date>.json` and `latest.json`: recall, precision and false alarms for each checker and each check, every miss and every unexpected finding, and the `history` block.

## How it scores
- **Recall:** planted defects caught, out of planted.
- **Precision:** findings that match a planted defect, out of all findings.
- **False alarms:** findings on clean pages.

Errors and warnings count. Info notes do not: review.py's info severity, preflight's indented lines and check_names' NEW to-do list. A layout finding seen at several widths counts as one finding.

Matching is strict. A finding catches a defect only if it names the same check and the same element: a selector segment for layout and review, or the quoted value or text for the other checkers. For layout it must also be at a width where the defect was planted. A finding with the right check on the wrong element is listed as **mislocated** and does not count as a catch. Some defects are seen two ways, for example a broken image is both "Images failed to load" and a failed request. `manifest.json` lists both under one expectation (`any_of`), so the defect counts once.

## The fixtures (`fixtures/`, expectations in `manifest.json`)

| Checker | Pages | What they plant |
|---|---|---|
| `site/check_layout.py` (checks 1 to 13) | `layout/*.html`, each run at the width named in the manifest | page overflow from an image and from an inline svg (320 px); a scrolling `pre` and a clipped note in a `.fig-card`; a hero whose rows lose their centre line (768 px, owner feedback item 8); overlapping cards; a ragged stack; two 20 px buttons 2 px apart, beside a lone 20 px button that the spacing exception allows; a key running past its card; a Copy button in an empty band (item 13) and one with unequal insets; widows in an h2 and a lede (item 14); a lede offset from its heading; a command under its Copy button, a "Default" chip broken inside the word and a two-line chip (item 16); stacked and reversed actions (item 17) |
| | `layout/clean-basics.html`, `layout/clean-docs.html`, at all 13 widths | the corrected version of each defect; a docs-shaped page with a carousel that has a screen-reader-only status, tag filters that scroll on purpose, visually hidden link text, a scrolling table and a form |
| `preflight.py html --medium web` | `preflight/*.html` | 10 px text (error) and 11 px text (warning); a font with no `@font-face`; 11 distinct sizes; 15 px next to 16 px; an 18 px size off a scale named `--fs-*`, and the same page with the engine's `--ds-font-size-*` names; -0.05em tracking, a `<br>` in a heading and a tween of `width`; a linked stylesheet that is missing. `clean.html` is the control |
| opendesigner-review (`probe.js` then `review.py check`) | `review/floors-a.html`, `floors-b.html` (no design system) | low contrast, small pager buttons, no `lang`, blocked zoom, no alt, a removed focus ring; sideways scroll at 320 px, 10 px text, motion with no reduced-motion rule, "undefined" in the page, a skipped heading level, a missing image, 128-character lines |
| | `review/drift.html`, `review/clean.html` (against `review/system/`) | an off-palette text colour, an off-scale size, an off-ladder radius and spacing, and the wrong typeface; `clean.html` is the control |
| `brand/tools/check_dates.py --year 2026` | `dates/wrong.html`, `wrong.md`, `clean.html` | "Thu 24 Oct 2026" (a Saturday), "Fri Oct 18, 2026", "Monday, 3 November 2026", "Wed 31 Sep 2026" (no such date), and one wrong weekday in Markdown |
| `brand/tools/check_names.py` | `names/piece-a.html`, `piece-b.html`, `piece-clean.html`, with `names/NAMES.md` as the registry | Tellwick and Stellwick in two pieces; Vossberg Health and Vosberg Health in two pieces; a registry name that belongs to another piece, one a letter away, and one's distinctive word |

The review pages are measured the way `capture.py` does it. That means a phone profile under 700 px, `probe.js` at every viewport, console messages and failed requests, and the Tab walk and drawn-font check at the narrowest and widest viewport. The stress, hover and motion-frame passes are not part of this eval.

Every invented name uses a `.example` domain or exists only in the fixture registry. None is a real brand.

## Not scored, and why
- **Three typefaces on one page** (`preflight/three-typefaces.html`). The house rule is two families at most. But `preflight.py html` does not claim to count families: its font check (M9) only asks whether each family is loaded. So the page expects no finding, and any finding on it is counted as unexpected.

## History
The eval runs every committed version of `site/check_layout.py`, from `git show <commit>:site/check_layout.py` written to a temporary folder (never the working tree), on the same layout fixtures. It also runs the working-tree file when that differs from the last commit. For each version, `latest.json` records:
- recall and precision;
- the planted defects it newly catches, and the owner feedback items those defects answer (`_coordination/OWNER-FEEDBACK.md`, the 2026-10-14 to 2026-10-15 table, items 8, 13, 14, 16 and 17);
- the clean-page false alarms it removed or added.

## When a checker misses something real
1. Make the smallest page that shows the defect, under `fixtures/<checker>/`. Use plain elements, or the classes the checker already reads (for check_layout: `CARDS`, `PANELS` and the selectors in each check). Say what is planted in an HTML comment at the top.
2. Add it to `manifest.json` with an `id`, the `check` id, the element or text it must name, the widths (for layout), a one-line `what`, and `owner_feedback` if an owner review found it.
3. Run the eval. The new defect shows up as missed, and that record stays until the checker is fixed. Fix the checker in its own change, then run the eval again: the defect moves to caught, and the history shows it.
4. If the page also triggers a finding you did not plant, decide whether the page really has that defect. If it does, remove it from the page. If it does not, it is a false alarm: keep it, and report it.
5. Commit the fixture, the manifest and the new `results/<date>.json` and `latest.json` together.
