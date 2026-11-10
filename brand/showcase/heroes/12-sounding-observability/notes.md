# 12 Sounding: API observability hero (B2B)

Built in round 3, after the owner's review (`brand/showcase/ROUND3-BRIEF.md`). It is one of three heroes made for the B2B product screens the owner loves, in place of the four heroes he removed. Render: `shot.png`, 1440 × 900 at 2×.

## Direction
Sounding is the fictional API observability product in `product/04-sounding-observability`. This is its marketing hero, for on-call engineers and SREs.

The hero shows the product first. On a charcoal page (the product system's own dark base surface), the real Overview screen sits at the top, flat and whole. Under it, one line of display type runs exactly the width of the window: "Find the deploy that broke p95." Below that come one 20 px sentence (the category, then facts from the screen) and one white button.

Feel words (the product's): **technical, precise, calm**.

Two things make the page Sounding's own, rather than any observability vendor's:
- The confident display line is measured to the product above it.
- The amber stays where the product puts it, on the alert, and nowhere else.

## References (Mobbin, cited by URL only; nothing saved)
| Reference | What it taught |
|---|---|
| https://mobbin.com/sites/sections/1f8c9d4b-9f7f-4bfa-aed3-9a849b84831e (incident.io) | A light product window on a dark page is the brightest object without any glow. Avoided: the highlighted second line, the outline button and the phone laid over the window. |
| https://mobbin.com/screens/bb369cb4-f7e0-4c16-a0f3-f39e7e4a3adf (Laravel Cloud) | A regular-weight headline with a full-width product window. Avoided: the glow and the floating modal. Our order is reversed, with the product before the claim. |
| https://mobbin.com/sites/sections/ee148e54-0a65-4d40-b945-cef19b160085 (Better Stack) | Shows what to avoid: a bold centred headline and a purple glow. |
| `brand/showcase/b2b-study/site.md` | Rule 1: say what it is, in the user's words. Rule 2: show the real product. Rule 8: proof a reader can check. |

## System (engine)
I copied the product's `state.json`, `decisions.md`, `standards-state.json` and `standards.md` from `product/04-sounding-observability/opendesigner/`. Then I ran:
- `engine.py --dir …/opendesigner pick Q-brand-06 two-sets --why "Marketing hero for the same product…"`, which sets `raw.marketingSurfaces` and adds display sizes 42, 50 and 72;
- `build`.

The light theme, the faces (Inter, plus JetBrains Mono for `v2.41.0` only), the dials and the overrides are all the product's. The page uses `data-theme="dark"`, with `data-density="comfortable"` on `<body>` (process finding 2).

## Type (hero; the embedded screen keeps its own)
| Size | Role | Where |
|---|---|---|
| 107 | display, 400, -0.03em, Inter optical sizing | Headline, one line |
| 20 | title-lg size | Supporting sentence |
| 17 | body-lg / title-md | Button (500), wordmark |
| 14 | label-lg | Nav, Sign in |

107 px is outside the scale on purpose (`calc(var(--ds-font-size-72) * 1.49)`). At that size the line's ink runs from 43 to 1390 px, the same width as the window above. At 72 px it stopped two-thirds of the way across and read as a caption.

The embedded screen renders at 0.9333, so its 12 / 14 / 24 px read as 11.2 / 13.1 / 22.4 px.

## Colour and contrast (measured on the render)
| Text | Contrast on the page |
|---|---|
| Headline | about 14:1 |
| Supporting sentence and nav | 7.3:1 |
| Button text | about 17:1 |

## The picture
The screen is `<iframe src="../../product/04-sounding-observability/index.html">`, 1440 px wide and scaled to 1344 px, which fills the 12-column grid with 48 px margins. I scaled the 1440 layout rather than set the frame to 1344 px, because at 1280–1344 px the product wraps its KPI and legend rows.

The window is 548 px tall, which shows 587 product px. The crop ends about 11 px under the chart legend and its sampling footnote, and above the endpoints card, so all four edges read as one whole screen.

The frame is `inert` and hidden from assistive tech, so keyboard focus never enters the product's controls. A hidden figcaption says what it shows.

Spacing: nav 56, 32 to the window, 40 to the headline, 32 to the sentence row, 37 below the button.

## Outside the tokens, on purpose
- **Headline at 107 px**, with line-height 1 and -0.03em tracking (reason above).
- **Nav height 56 px.** There is no nav-height token.
- Both are marked `od-ignore` or explained in comments.

## Checks
- `engine.py validate`: passes, with 0 warnings and 11 notes. The notes are the product's own: ink focus on dark surfaces, APCA advice, orphan steps, and asset hooks not yet asked.
- `engine.py review --project heroes/12-sounding-observability`: no hard-coded values.
- `preflight.py html --medium web`: 0 errors, 0 warnings. One earlier run flagged tracking tighter than -0.03em; it is now -0.03em.
- `check_dates.py --year 2026`: passes. The page names no weekday.
- Facts, each checked on the screen:
  - v2.41.0 was deployed at 13:12 UTC by ci-release.
  - The alert reads "above its 450 ms objective since 13:21 UTC", nine minutes after the deploy.
  - Deploy diamonds appear on the request, latency and error charts.
  - The sentence reads: "API monitoring for on-call teams. v2.41.0 deployed at 13:12 UTC; nine minutes later, p95 passed 450 ms."
- `.example` rule: the hero copy names no domain or email address and shows no shell command.

## Round 3 (owner review)
**What he said.** "I love the B2B product screens. They look absolutely crazy." He removed four heroes he called very ugly and asked for one hero per B2B product, with these rules:
- the real screen is the picture: flat, whole, readable and inside the grid;
- the hero uses the product's own system;
- it takes its own direction;
- the headline is in the user's words;
- there is one action and real proof only.

**What I built and changed.** About sixteen rounds, each scored by a fresh-context agent against this brief, the product screens, Orbika and the three references:
- **First version, scored 3.** A status kicker, a 72 px headline, the button with a note, and the screen below. The auditor called it "the Purlin layout in dark mode". The note named OpenTelemetry, which the product never shows, and "paged", which it doesn't support.
- **Product first, scored 3 to 3.5.** I moved the product above the claim, then tried a three-line mono incident log, a caption, a hairline tick at the deploy line, and a proof line in the product's legend marks. Auditors said the tick pointed at the wrong legend item, the log repeated the screen, and one draft claimed "every chart marks the deploy" (the timeouts card has none) or a cause the product never states.
- **Final.** The one display line spans the window's width. The last rounds took the sentence to one 20 px line (category first, then the deploy and the breach), opened the space under the headline, made the frame inert, and dropped "Docs" from the marketing nav so the two nav bars don't repeat it. Fresh scores in the final rounds: 4, 3, 3.5, then the conditional 4 ("I would sign a 4 once the two spacing fixes are made"), which these changes apply; the confirming score is in the audit JSON.

**Fresh score: 4** (the confirming audit after the last fixes; recorded in `brand/showcase/audit/heroes--12-sounding-observability.json`).

**What remains:**
- The picture's proof is small: about 10 px of spike at the right edge of one chart card. Only the product can fix that, for example by opening on the alert's time window.
- Apart from its mark, the page has no Sounding-only object besides the type itself.

## Process findings
1. **There is no "start from an existing system" path** (gap). A product's marketing page should inherit the product's system; I copied its state by hand and picked Q-brand-06.
2. **Density modes don't apply on `<html>`** (bug). In `tokens.css` the default `:root, [data-density="compact"]` block comes after `[data-density="comfortable"]` at equal specificity, so the button rendered at 40 px instead of 48. Setting the mode on `<body>` works.
3. **A product's committed tokens go stale without warning** (gap). Rebuilding the product's own state today changes its dark accent ramp: accent-dark-9 goes from #bc8141 to #c97a06.
4. **`review` maps sizes to spacing tokens** (gap). Nav height and logo tile have no role token.
5. **"Display set" adds sizes, not a face** (gap). Q-brand-06 two-sets adds 42, 50 and 72 px, but `--ds-font-family-display` still points to the text face, and nothing above 72 px exists for a headline measured to a full-width object.
6. **The embedded product follows the viewer's colour scheme** (outside this folder). `product/04` has no `data-theme`, so with an OS dark preference the iframe switches to the product's unfinished dark theme. The fix is one line in the product: `<html lang="en" data-theme="light">`.
7. **Fresh audits disagree across rounds** (process). One round asked for a mono log, the next called it repetition. Scoring every round against the same named references and the owner's words kept the work converging.

Findings 1 to 4 are recorded with `engine.py feedback` in `opendesigner/feedback.md`. Nothing was posted.
