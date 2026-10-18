# 09 Millrace: footer for a B2B data platform

Replaces `footers/03-quietfield-horizon` (audited 2 of 5, "remake"). Render: 1440 wide, natural height, scale 2 (`shot.png`), dark theme.

## Direction
Millrace is a fictional managed event-streaming platform (a millrace is the channel that carries water to a mill). Developers send events once and read any stream again from any point in its retention window. Buyers are platform and data engineering leads; their security and legal teams read the footer too. So the footer is a dense, quiet directory with the facts a buyer checks: status, where data lives, and an honest compliance record. The one detail only this brand would have is a **retention clock**: "An event sent now stays readable until Fri 13 Nov 2026, 14:02 UTC", computed live as now plus the default 30 days. Feel words: **technical, quiet, trustworthy**.

The brand was first called Runnel. A web search after round 2 found an existing open-source event-streaming library of that name with docs at runnel.dev, so it was renamed (see findings).

What the old piece did that this one must not: a glowing planet horizon, a bold-phrase headline, a centred pill newsletter, a badge inside a badge, dash-flanked labels, and no sign of the company's work (`audit/footers--03-quietfield-horizon.json`).

## References (Mobbin, cited by URL only; no image saved)
| Reference | What it taught |
|---|---|
| https://mobbin.com/sites/sections/59cdf49d-e039-4904-a90e-aebfb09a9771 | A dark developer footer with columns in two bands and status as one small line; compliance kept small. |
| https://mobbin.com/sites/sections/82d7b249-da3b-4e9f-9b61-7f8f21dc94e3 | A dense directory with a "Legal and trust" column and a single status line; density without boxes. |
| https://mobbin.com/sites/sections/9301c687-40d0-4d8d-bbb8-b1325bac2679 | Near-black with a company address top-left and five quiet columns; nothing decorative at all, and it holds. |
| https://mobbin.com/sites/sections/c5908fa0-2fc1-41dc-9669-9c55b0909a9f | Small labels over columns and a long legal row; compliance shown small, not as a badge wall. |

Also read: `b2b-study/site.md` rule 10 (footers are directories with a trust column and one live signal), section 2 "Enterprise, security and governance" (name the data boundary; honest status labels such as "in progress"), and the Keystrata audit (no hero band, no certification chips, no numbered columns).

## System (engine)
```
sketch --name "Runnel" --brand "#F0A830" --audience regular --platforms web --feel technical,quiet,trustworthy
       --theme system-light-dark --surfaces "marketing site:persuade,docs:read" --delegated all
set raw.brandColor "#F0A830"   (the sketch had swapped it for brown #9f6a00)
pick Q-color-01 keep-hex; pick Q-color-09 cool
set raw.textFace "Hanken Grotesk"; set raw.monoFace "Fragment Mono"; pick Q-type-02 yes; build
set name "Millrace"   (rename after the name check)
```
The page sets `data-theme="dark"` on `<html>`, so the generated dark tokens apply; the light theme also works.

| Dial | Value | Why |
|---|---|---|
| expression | 35 | Quiet; the clock is the only display moment |
| brandPresence | 25 | Amber used once |
| density | 60 | A dense directory |
| energy | 15 | Still |
| roundness | 35 | Small corners (there are almost no boxes) |
| depth | 10 | Hairlines only |
| colorfulness | 20 | Graphite plus one amber, plus the status green |
| warmth | 30 | Graphite, never brown under amber |

## Fonts and type scale
**Hanken Grotesk** (OFL) for every word; **Fragment Mono** (OFL) only for data: region codes, the retention time and the health-check command. Chosen from six pairs rendered on the dark ground.

| Role | Size | Used for |
|---|---|---|
| Title (mono) | 25 | The retention clock |
| Title | 20 | Wordmark |
| Body | 16 | Links, the brand sentence, "All systems normal" |
| Footnote / label | 13 | Column labels, the fact cells, the legal row, code |

Four sizes.

## Color
Ground `surface-sunken` #141516. Text #e5e9ee (15.0:1), links #a6abb2 (7.9:1), labels #91969d (6.1:1). Amber is the exact seed `--ds-color-brand-seed` #F0A830 (9.0:1) on the clock only; the engine's dark accent step is dulled to #e0ae69. Status green #63be79 (8.0:1) on one dot, with the words beside it. Compliance rows carry no color at all: the status is in words.

## Honest security and compliance (invented company, no badges)
SOC 2 Type II "Audit period ends 31 Dec; report due Feb 2027"; Encryption "AES-256 at rest, TLS 1.3 in transit"; ISO 27001 "Not certified yet; planned after SOC 2"; GDPR "DPA signed online; EU streams stay in the EU"; penetration test "August 2026, external. Summary under NDA". The region list marks Sydney "Preview". The legal row is the company name and the language menu; legal pages live in the Legal column only.

## Outside the tokens, on purpose
- Grid templates for the region and compliance rows (56 px and 120 px label columns).
- The clock's -0.02em tracking on the mono face.

## Checks
- `engine.py validate`: passes; 2 warnings, both about the light-mode amber button on white (2.0:1). There is no button in this footer; noted, not changed.
- `engine.py review`: clean.
- `preflight.py html --medium web`: 1 error, M9 for Fragment Mono via a Google Fonts link (false positive).
- Every link is at least 24 px tall (32 px in the columns).

## Self-audit (score against the four references at 1440 wide)
- **Round 1, score 3.** The facts row was unbalanced: a wide status cell with empty space, a cramped three-column residency cell, compliance rows wrapping; the clock overran its column; the fact cells did not share grid lines with the link columns; a 96 px "end of page" strip read as an empty bar.
- **Round 2, score 4.** Link columns moved to grid columns 5 to 12 so Data residency lines up under Product and Security under Company; the clock set on two lines (date, then time); the status cell gained a check you can run yourself (`curl api.millrace.dev/v1/health`, which needs no key); compliance copy cut to one line each; the strip removed; a chevron on the language link.
- Section 11 walk: no glow, no art, no decoration without data, no headline or buttons in the footer, no certification chips, no numbered columns, no invented proof, one signal per state, one accent with one job.
- **Round 3, independent audit, score 4.** A fresh-context subagent found: the name "Runnel" is a real event-streaming project (I had found this too and renamed it Millrace); "HRB 231774 B" sits in the range real Berlin companies hold; the ISO line "We have not started an audit" undercut the column; Privacy, Terms and Imprint were repeated in the bottom row; there was no door for enterprise buyers. Fixed: register number removed; an Encryption row added and the ISO line reworded to a plan; the bottom row cut to the copyright and the language menu; "Enterprise" added to the Product column.
- **Final, score 4.** Re-rendered at 1440 and read at full size.

## Process findings
1. **The sketch still swaps an explicit brand hex (bug).** `--brand #F0A830 --delegated all` recorded #9f6a00 ("I picked a brown") so white text would pass, although amber carries dark text. The dark ramp also dulls step 9 to #e0ae69, so the exact amber in dark needs `--ds-color-brand-seed`. Both were reported in earlier runs and are unchanged.
2. **No step checks that an invented name is free (gap).** "Runnel" is an existing event-streaming library (runnel.dev). BRIEF.md says "invent a fictional brand" but never says to search the name first.
3. **Renaming a system is undocumented (bug).** `set raw.name` was accepted silently and logged as a decision that changes nothing; the real path is the top-level `name`. Once, `set name` crashed with `NameError: log_profile_change` while another session was editing `engine.py`; the state was written anyway.
4. Helped: `--theme system-light-dark` plus `data-theme="dark"` gave a complete dark system from semantic tokens with no hand-made colors.

All recorded with `engine.py feedback` in `opendesigner/feedback.md`; nothing posted.

## Fix round 2026-10-14
Nothing on the page changed, so `shot.png` was not re-rendered. A re-render would also move the live retention clock.

- **Names.** "Millrace" and "Millrace Data GmbH" appear in no other piece (`brand/showcase/NAMES.md`).
- **Domain fact pass.** Nothing wrong was found:
  - The clock is now + 30 days in UTC, and the render's Fri 13 Nov 2026 is 30 days after Wed 14 Oct.
  - "Last incident 9 Oct" is a Friday, already past.
  - The SOC 2 period ends 31 Dec, so a report in Feb 2027 is plausible. ISO 27001 is stated as not held.
  - The region codes match their cities.
  - "Imprint" fits a Berlin GmbH.
- **Not changed.** The audit's two design fixes are outside this fix round: link text at 14 px, and a smaller or text-face date.

## Round 4 (18 Oct 2026): quiet footer
This replaces the round-3 design described above. The round-4 audit (`brand/showcase/AUDIT-ROUND4.md`) and the owner called the footer studies cluttered; `brand/showcase/PRESENTATION.md` now sets the footer rules. Built from one shared generator so all four keep the PRESENTATION.md footer rules: link columns in one text size, one muted heading style, one rule, one legal line, at most one signature element, and the last row of the section above (one line of real copy) so the shot reads as the end of a page. No illustrations, charts, chips, badges or boxes.

- Status, residency and compliance mini-tables and the curl command removed; api.millrace.dev is gone, so no invented domain remains
- The amber monospace date replaced by one sentence at the foot, 'An event sent now stays readable until <date>.', the date live (now plus 30 days, UTC) and the only amber
- Fragment Mono dropped: one typeface (Hanken Grotesk)
- Four link columns including a Trust column; the 'Ready to stream?' row of the section above has a real link

**Fresh audit:** 4 of 5. **Pairwise:** lost to Linear by 1 (not blind); the earlier blind test lost to Railway by 2. After the audit: the closing sentence raised to 39 px and phone links to 16 px after the final audit, checked by eye. The shot's date is the render time plus 30 days (17 Nov 2026), so the shot needs re-rendering after that date.

**Checks:** `preflight.py html`: 0 errors, 0 warnings. `check_dates.py --year 2026`: passes. No invented domains on the page. Two typefaces at most, sizes on the token scale.
