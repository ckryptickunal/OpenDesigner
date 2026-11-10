# 10 Orvita: enterprise clinical AI hero

**Direction.** Orvita is a fictional clinical AI platform for hospitals. It reads vitals, labs and nursing notes from the EHR, flags patients who are deteriorating, and shows the evidence behind each alert. The buyers are CMIOs, CNOs and IT committees; nurses and physicians on the ward are the users. Mood: a calm, credible instrument that a hospital would trust at 3 a.m. Feel words: **trustworthy, clean, professional**.

Render: 1440 x 900 at scale 2 (`shot.png`).

## References (Mobbin, cited by URL only)
| Reference | What it taught |
|---|---|
| https://mobbin.com/sites/sections/a52a1f9a-e372-4769-804f-0d8a8d2562d2 | Product UI shown as composed fragments rather than one flat screenshot, with a quiet logo row under the hero. |
| https://mobbin.com/sites/sections/20e495f3-f34a-4015-9106-747e9d84f1ef | A large headline on the left, the product on the right, and a "trusted by" label anchoring the logo row. |
| https://mobbin.com/sites/sections/e6e87f69-8f6e-42cd-adb6-99a06f281082 | Customer logos in equal cells with hairline dividers: it reads more credible than a floating strip. |
| https://mobbin.com/screens/5999d971-3c12-4486-9f23-8ff1098139bc | Dense dashboard grammar: hairline tables, status pills, small KPI cards. |

## System (engine)
```
init; standard override STD-visual-details-24 (light page)
sketch --name Orvita --brand #0B7A85 --audience regular --platforms web --feel trustworthy,clean,professional --theme light-only --surfaces "landing page:persuade,app:operate" --delegated all
set raw.secondaryColors ["#1F5FD1"]; set raw.accentCount 2   (the secondary was silently dropped until accentCount was raised)
```
| Dial | Value | Why |
|---|---|---|
| expression | 35 | Credible, product-led |
| brandPresence | 50 | Teal on actions and highlights |
| energy | 35 | Calm, no bounce |
| roundness | 30 | 4px controls, 8px containers, 12px overlays |
| depth | 35 | Floating fragments need soft lift |
| colorfulness | 40 | Teal and blue plus status colors |
| warmth | 25 | Cool clinical neutrals |
| density | 60 | Product UI is dense |

**Fonts (final).** Instrument Sans for words (width axis at 92 on the headline, 80 and 75 on two logos) and Geist Mono for clinical data. Both SIL OFL. The first render used Instrument Serif for two logos; it was removed under the owner rules.

## The product fragment
An HTML dashboard: a ward watchlist with a risk score, bar, 12-hour sparkline, signal chips and status pills. One row is flagged. Two floating cards sit over it: an AI explanation that cites its three sources with timestamps, and a risk-trend chart crossing the alert threshold. Every color, radius, elevation and size comes from tokens. Status pills use the danger, warning and success ramps.

Customer wordmarks are invented: St. Aldric, Northvale Medical, Kestrel Bay Hospitals, Lindqvist University Clinic, Harrowgate Children's, thornfield/health. An early draft named two real EHR vendors; that was caught and replaced with "your existing EHR".

## Outside the tokens, on purpose
- The blueprint grid and the teal and blue washes behind the product.
- The tinted big shadow under the window and cards, added to `--ds-elevation-overlay`.
- Logo type treatments (weight, width, tracking within the two faces).

## Checks
- `engine.py validate`: no errors, 0 warnings.
- `preflight.py html`: 3 false M9 errors (Google Fonts). Fixed the real ones:
  - text at 10-12px moved to the 13px step
  - tracking went from -0.035 to -0.03em
  - a `<br>` in a logo was replaced
  - M8 still warns that 13px is under 14px; 13px is the engine's own smallest step.
- `engine.py review`: 0 standards broken. 29 raw values remain: logo sizes, the sparkline viewBox, and the art washes.
- Contrast:
  - button 5.1:1
  - teal "next." 5.1:1 (large)
  - secondary text 7.3:1
  - pills: high 6.1:1, watch 5.0:1, ok 6.0:1
  - evidence chips 6.0:1
  - logo grey 6.0:1
- The product fragment is `aria-hidden`. The logo row is labelled.

## Honest assessment
This is the most conventional layout of my five (headline left, product right, logos below), because the direction asked for credibility. Its quality is in the product fragment: real clinical content, evidence with sources, status color used sparingly. It would not stand out on a gallery the way 07 or 09 would.

## Process findings
1. **`secondaryColors` is silently dropped** when colorfulness implies one accent. (bug)
2. **The engine's smallest text step (13px) conflicts with preflight's 14px warning,** and there is no 12px caption step for dense UI. (confusing)
3. What helped:
   - The "app:operate" surface gave ring-plus-shadow elevations, which look right for product UI straight away.
   - Status ramps at step 3 and step 11 give accessible pills with no tuning.
   - `review` caught 2px and 3px paddings.

## Owner type and color rules (applied after the first render)
- **Fonts:** two only. Instrument Serif was removed from the customer wordmarks. All six are now Instrument Sans (varied weight, width, case and tracking) or Geist Mono (thornfield/health). Geist Mono is otherwise used only for clinical data: bed numbers, scores, timestamps, source chips and the alert line.
- **Highlight:** the teal color on "next." was removed. The headline is now regular 400 with "needs you next." in 650: same ink, weight does the work. Visual weight: the dashboard on the right is busy, so the headline needed calm mass on the left rather than a second accent color.
- **Type scale (5 sizes):**

  | Role | Size | Use |
  |---|---|---|
  | Display | 76 | Headline |
  | Title | 25 | Trend value |
  | Body large | 20 | Lede, wordmark, logos |
  | Body / label | 16 | Nav, buttons, table title, logos |
  | Caption | 13 | Table, chips, captions, logo sublines |

  Logo sizes were normalized from 22/18/15 to 20/16/13.
- **Color:** white with ink (16:1) and teal and blue used for action only. Status colors only in pills.
