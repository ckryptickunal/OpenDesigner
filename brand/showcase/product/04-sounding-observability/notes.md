# 04 · Service overview · Sounding

Final renders: `shot.png` and `shot-tooltip.png` (`?state=tooltip`), each 1440 × 900 at 2×. Final self-audit score: **4 of 5**.

## Direction
Sounding is a fictional API observability tool. The screen is the Overview of one service, `payments-api`, at the fictional company Fulmar Pay, at 14:02 UTC on Oct 14, 2026. A deploy at 13:12 (v2.41.0) pushed p95 latency on `POST /v1/payouts` over its 450 ms objective at 13:21, and an alert is firing. The users are on-call engineers and SREs. They need to see in about five seconds what is wrong, since when, and which endpoint. Near-black ink carries the page. One amber is spent only on the alerting series and on the words that point to it.
Feel words: **technical, precise, calm**. The engine dropped "precise", which it doesn't know.

The study's section 5.4 is followed point by point:
- Environment, range and comparison controls in one row.
- A KPI text row: requests, p50, p95 and error rate, with the latencies in mono.
- Four quiet chart cards. Labels sit only at the axis ends. The previous day is dashed, the last hour is dotted, and deploy markers appear on every chart.
- Hatched no-data gaps, "Updated 14:02 UTC" and a sampling footnote.
- One honest empty card ("No upstream timeouts in this range").
- An endpoints table with a p95 sparkline in every row.
- No donut and no gradient.

## References
The study's own references for 5.4 are [Vercel observability](https://mobbin.com/screens/38a44719-a4b0-482b-bb40-283eec56ebd4), [Stripe Today](https://mobbin.com/screens/a31f7d76-ade4-4cae-a816-a4c9b33814c3) and [Neon monitoring](https://mobbin.com/screens/c5ee5c89-e7ad-43fc-828a-46315320e455). I didn't reopen those three. I compared against the screens below, which I opened in this session at about the same width:
- [Vercel query view](https://mobbin.com/screens/efa48f32-7ab7-4476-a583-00ecf2fa8726): one 1 px line, end-only x labels ("12h ago / 2m ago"), and a searchable table under the chart. It taught me how little chrome a chart needs.
- [Vercel analytics](https://mobbin.com/screens/f58e584d-9481-4125-961f-b08bde53529b): environment and range selects at the top right, and the incomplete last day dashed. It taught me where the range control goes and how to mark partial data.
- [Snowflake performance explorer](https://mobbin.com/screens/fc035908-b904-44a1-9e13-8559a7e7988e): small-multiple chart cards, and a "Previous period / Current period" legend in grey and accent. It taught me the comparison legend and the card rhythm.
- [Gumloop insights](https://mobbin.com/screens/337deb65-cb56-4502-a27d-b7ea42b599d7): KPIs as plain text in one row with no cards. It taught me the KPI text row.

## System (engine)
`sketch --name "Sounding" --brand "#e5a00d" --audience dense --platforms web --feel technical,precise,calm --theme system-light-dark --delegated all --surfaces operate`

I then set the P1 profile by hand, each with `--set-by delegated --why "P1 dense work-tool profile, brand/showcase/b2b-study/product-ui.md…"`:

| Setting | Value | Why |
|---|---|---|
| dials.roundness | 42 | 6 px controls, 8 px containers and 12 px overlays (band 38-47). The sketch gave 2 px |
| dials.depth | 10 | Static surfaces get borders only |
| dials.expression | 25 | P10: 20-30, not 0 |
| dials.colorfulness | 55 | Keeps the amber ramp clean. At 36, steps 3-7 were beige |
| dials.warmth | 40 | Cool greys (tint chroma 0.011 at hue 264). Default borders, not strong rules |
| overrides.type.weightCount | 3 | 400 / 500 / 600. The label weight became 500 |
| raw.numericStyles | true | `text.numeric.*` styles with tabular digits |
| answers.Q-color-19 | brand-gray | P7: the chart palette is the accent plus neutrals |
| raw.brandColor | #c97a06 | The sketch had swapped my amber for "an olive" #9c6b00. #c97a06 is 3.35:1 on white, so the alert line passes 3:1 as a graphic |
| raw.focusColor | #17181c | Amber is reserved for the alert, so focus is ink |
| raw.textFace / monoFace | Inter / JetBrains Mono | Both SIL OFL, loaded from Google Fonts. Two fonts |
| raw.primaryActionColor | set to #17181c, then null | The near-black seed produced a periwinkle #5f6dcc button (bug, recorded) |

What I used from `tokens.css`:
- Every text, surface, status, success-dot, border-input and focus color.
- `chart.categorical.1` (amber) and the neutral ramp steps for the chart lines.
- Spacing tokens 2-32, `size.control.md` (32) for every control, and `size.icon.sm`.
- `radius.control-sm/control/container`: 4, 6 and 8.
- `text.body-sm/md`, `label-sm/md/lg`, `title-lg`, `headline-sm` and the 12/14/20/24 sizes.
- `focus-ring-width` and `focus-ring-offset`.

## Type scale (Material-style roles)
I used four sizes, and no two are within 10% of each other:

| Size | Role | Where |
|---|---|---|
| 12 | Label and caption | Axis ends, meta text, column headers, legend |
| 14 | Body | Body text and table cells, including the mono routes and latencies (`code-md`) |
| 20 | Title | Page title (`title-lg`, 600) |
| 24 | Headline | KPI figures (`headline-sm`, set at 500 rather than 600) |

The weights in use are 400, 500 and 600, measured in the DOM. Mono appears only on routes, HTTP methods, versions and latencies.

## Where I stepped outside the tokens, and why
- **Near-black primary.** The `New alert` button and the mark use `color.bg.inverse`. The engine has no way to make a near-black primary next to a chromatic accent. `bg.action.primary` either is the amber or comes out periwinkle from a near-black seed.
- **Hairlines.** Card and control edges use neutral 5. Row and grid lines use neutral 4. `border.subtle` is neutral 6, about 1.5:1, which is too heavy for 36 px rows. There is no separator role.
- **Row height.** `--row: 36px` is set by hand (there is no row token; P2). I measured 36 px in the DOM.
- **Tooltip shadow.** At depth 10, `elevation.overlay` is `0 0 0 0`, so I wrote the floating tooltip's shadow by hand. It is the only shadow on the page.
- **Chart grammar.** These are all hand-made, because there are no chart tokens for them:
  - comparison series dashed (3 3)
  - partial last hour dotted (0 3.2, round caps)
  - deploy markers: a dashed vertical line plus a 6 px diamond
  - the objective line at accent step 7
  - the hatch pattern on neutral 2 and 6
- **Links.** Links are ink with a neutral-7 underline. Leaving `text.link` at the default would have made them amber, which is reserved for the alert.
- The status dot's 3 px halo uses accent step 3.

## Data
The data is invented but internally consistent:
- The 11 endpoint rows add up to 18,375,270 requests, which the KPI shows as "18.38M".
- 18,375,270 ÷ 86,400 = 213 req/s.
- The errors add up to 41,604, which gives 0.23%.
- The request series is scaled so that 288 five-minute buckets × 300 s equal that same total.
- The error series is scaled so that its request-weighted mean equals 0.23%.
- The p95 regression begins at the 13:12 deploy marker in every chart and in the payouts sparkline.
- The trace collector gap (02:00-03:50 UTC) appears in the latency chart, the error chart and every sparkline, but not in requests, which come from load balancer counts. The footnote says so.
- IPs, names and the company are invented.

## Checks
- `engine.py validate`: no errors and no warnings. 10 notes:
  - 5 say the ink focus color is about 1.05:1 on dark surfaces. The two-tone inner ring carries 3:1. This is a finding: `focusColor` has a single value for both modes.
  - The rest are APCA advisories, orphan steps, the 24 px control note and unasked asset hooks.
- `preflight.py html --medium web`: 2 errors, both false positives (M9: Inter and JetBrains Mono load from a Google Fonts `<link>`; Playwright confirmed both faces and weights loaded). 1 warning: 12 px text under 14 on web, which is meta text by design. Earlier runs caught three real problems, all fixed:
  - a 10 px org badge
  - 13 px mono, within 10% of 12
  - a `/32px` line-height that preflight wrongly read as a font size (bug, recorded)
- `engine.py review`: 34 hard-coded values remain after I replaced every on-scale spacing value with `--ds-space-*`. They are component sizes with no token: the 36 px row, the 8 px status dot, chart heights and the tooltip shadow.
- Contrast I checked by hand:
  - amber text (accent 11) 5.94:1
  - the amber line 3.35:1 against white
  - faint text 5.82:1 on the base surface
  - the filter field uses `border.input` (neutral 8, 3.65:1)

## Self-audit rounds
I compared each round with the four references above at 1440 px.

1. **Round 1: 3/5.**
   - The primary button and the mark rendered periwinkle (engine bug).
   - The tooltip covered the latency chart and its objective label.
   - The legend wrapped onto three lines.
   - The header meta line collided with the buttons.
   - The search placeholder wrapped, and Docs was underlined.
   - The alert was said three ways in one table row (flag, amber value, amber sparkline).
   - A gridline ran through the empty card's text.
   - The error line was jagged.
2. **Round 2: 4/5.**
   - The primary moved to `bg.inverse`.
   - The alert statement moved into the title row, with the meta on its own line.
   - The legend went onto one nowrap line.
   - The KPI tag was removed and the table value made ink, so the table row keeps a dot, a word and the amber series only.
   - The latency scale went to 600 ms and the objective label to the left.
   - The noise was smoothed, and the empty card was left with only its baseline.
   - The tooltip moved to the requests chart, but it still spilled into the next card.
3. **Round 3: 4/5.**
   - A compact two-row tooltip inside the card, with the change in its header.
   - 32 px side gutters aligned across the top bar, tabs and content.
   - The preflight fixes listed under Checks.
   - Spacing written as tokens, and the filter field border raised to 3:1.
   - The final render looks the same apart from the fixes.

**Why it's a 4 and not a 5.**
- The KPI text row is a well-known recipe and adds nothing that only Sounding has.
- The 5-minute noise still reads a little busy at this card width.
- The tooltip covers part of the requests curve, which a pinned hover state always will.

It passes every tell in `making.md` section 11:
- no glow, decoration or invented proof
- status said once, plus text
- regular weight carries the page
- fresh data

## Process findings
1. **Bug: a near-black `primaryActionColor` produces a mid-tone of its hue.** #17181c became a periwinkle #5f6dcc. No question offers "near-black primary plus one chromatic accent", which is P5 and the Vercel/Linear pattern. (feedback F-001)
2. **Bug: the sketch replaced a light brand with a dark "readable shade" and misnamed it.** With `--delegated all`, the amber #e5a00d became #9c6b00, labelled "an olive". The amber was for a chart series and never carries text. (F-002)
3. **Gap: no chart grammar tokens.** Nothing exists for the comparison, partial, no-data, threshold or event-marker series (P7). (F-003)
4. **Gap: depth 10 zeroes `elevation.overlay`.** The floating tooltip had no shadow (P8). (F-004)
5. **Confusing: no way to say "the accent is for data only".** `text.link` and `border.focus` default to the accent. (F-005)
6. **Gap: `focusColor` has one value for both modes.** (F-006)
7. **Bug: preflight reads a shorthand line-height as a font size.** (F-007)
8. **Helped:**
   - Once I set them by hand, the P1 values produced exactly the evidence values (6/8/12 corners, a 500 label weight, tabular numeric styles).
   - `chart.categorical.1` gave the alert series a token.
   - The status success ramp gave the environment dot.
   - `validate` caught the dark-mode focus problem I would not have seen in a light-only render.

## Fix round 2026-10-14
After the independent audit (`audit/product--04-sounding-observability.json`). Renders: `shot.png` and `shot-tooltip.png`, each 1440 × 900 at 2×.

- **One temporary state per frame.** The pinned tooltip and crosshair on the requests chart now show only in `?state=tooltip` (`shot-tooltip.png`). The main frame is the page as the on-call engineer opens it: the firing alert, the objective line, the deploy markers, the no-trace band and the partial last hour. Those are data, not hover states.
- **Tooltip arithmetic.** The change was computed from unrounded values, so "228/s vs 214/s" read "+6.4%". It is now computed from the figures shown, so it reads "+6.5%".
- **p50 line labelled.** The thin grey line in the latency card was not in the legend. The legend now has "Latency p50".
- **Runtime version.** "Go 1.23" was out of support by October 2026; it is now "Go 1.26".
- **Names.** The workspace Wrenfield Pay ("W") is now Fulmar Pay ("F"); Fennick had a Wrenfield vendor. The signed-in user Mara Okafor ("MO") is now Yusuf Hartmann ("YH"). A web search found no payments company called Fulmar Pay.
- **Note on the headline numbers.** The chart-card figures come from the script: peak 327 req/s, now 547 ms and now 0.51%. The static placeholders in the HTML differ (331, 541 ms, 0.41%), but the script replaces them before render. The KPI row, the endpoint totals (18,375,270 requests, 41,604 errors) and the 1-in-10 sampling note are unchanged.
