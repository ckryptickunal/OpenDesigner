# 05 · Aerlo: boarding pass

## Direction
Aerlo is a fictional short-haul airline app. The boarding pass is the screen people pull up in a queue with a bag in one hand: it must answer "which gate, which seat, when" in one glance and scan at the gate, and it should feel like the first minute of the trip: high, light, blue. White perforated ticket, a dot-matrix route map, crisp geometric type. Feel words: **airy, crisp, trustworthy** ("airy" and "crisp" are not in the engine's feel list).

Shape language: one big white ticket with punched notches and dashed perforations, 24 px outer corners, pill chips, a dot grid. Type: Sora for everything, DM Mono only for codes and flight data. Two fonts.

## References (Mobbin, structure only)
- https://mobbin.com/screens/f06fb631-010c-4715-acb2-6f1305b1607c (a focus-timer app styled as a boarding pass): a perforated ticket with side notches and a map texture behind the route. Taught the ticket construction and map-as-texture.
- https://mobbin.com/screens/fe3800b2-59af-4229-9412-115dcb51c881 (a wallet pass): huge airport codes with small label/value pairs in a strict grid. Taught the label-over-value rhythm.
- https://mobbin.com/screens/a315a3cc-6234-4d7c-a3ce-9271f5a10092 (a flight tracker widget): a dotted route line with a plane glyph between the two ends. Taught the route line.
- https://mobbin.com/screens/78642fe1-4cb2-4edc-816c-016fa8559431 (an airline app): the seat number set much larger than everything else. Taught the seat as the second hero.

## System (engine)
```
sketch --name "Aerlo" --brand "#2A66E8" --audience regular --platforms ios --feel airy,crisp,trustworthy --theme system-light-dark --delegated all
pick Q-color-01 keep-hex · pick Q-color-09 cool · pick Q-color-04 analogous · set raw.secondaryColors ["#7CC4FF", "#5B5BD6"]
pick Q-depth-01 ring-shadow
pick Q-type-01 open-custom · set raw.textFace "Sora" · set raw.monoFace "DM Mono" · pick Q-type-08 17 · set overrides.type.displayReach 3.4
HIG type scale (Q-type-10 named, Q-type-09 hand-tuned, font.size steps, text-style overrides)
```
Dials: expression 60, brandPresence 55, density 40 (glanceable), energy 45, roundness 70 (12 px controls, 16 px containers, 24 px overlay), colorfulness 50, warmth 35; depth 25 from Q-depth-01 `ring-shadow`.

The brand blue was kept by the sketch (white text on it is 5.04:1). Rendered in the light mapping.

## Type scale (Apple HIG roles)
| Role | Size / line | Used for |
|---|---|---|
| Display (custom) | 52, Sora 600 | airport codes and the seat |
| Title 2 | 22 / 28 | passenger, gate, boarding time, group, the "aerlo" mark, the booking code (mono) |
| Body / Headline | 17 / 22 | nav title (semibold), departure and arrival times, status bar |
| Subheadline | 15 / 20 | city names, the status pill, "Brightens at the gate" |
| Footnote | 13 / 18 | field labels, flight number and date (mono), duration, "Window" |

Five sizes, nothing under 13.

## Image
The header is a photograph by Nicholas Szewczyk on Unsplash (a wing above the clouds, `images.unsplash.com/photo-1647363377737-8d0ad7c2f494`, hotlinked, cropped with Unsplash's crop parameters so the nav title sits on open sky; free Unsplash licence, not Unsplash+). A navy gradient over its top keeps white header text at 5.46:1 or better at the brightest sampled point, and it fades into the pale-sky ramp (`accent2`) under the ticket.

The route map is SVG made in code: a dot matrix with rough coastlines (Iceland, the Faroes, Scotland, Norway, Sweden, Denmark) between 26°W-16°E and 54-68°N, stretched vertically to fit the card, so it is a diagram, not a chart. The great-circle bow is drawn as a quadratic curve. The 2D code is a seeded mock with an Aztec-style bullseye; it does not scan.

## Where I went outside the tokens, and why
- The ticket shape: radial-gradient notches and a stacked `drop-shadow` filter (so the shadow follows the cut-outs). The shadow's blue tint is literal.
- The header photo overlay is a literal navy, chosen for text contrast over the photo.
- Map dots use the `accent2` ramp (land step 9, sea step 6) and the route uses `accent` to `accent3`.

## Checks
- `engine.py validate`: 0 errors, 1 warning ("14 text sizes": the formula steps that cannot be removed after hand-tuning).
- `engine.py review`: 17 findings: element sizes, the map's literal colors inside the SVG script, the ticket shadow.
- `preflight.py html --medium web`: 2 errors, Sora and DM Mono "have no @font-face" (Google Fonts `<link>`). Its tracking warning (-0.04em on the codes) and `<br>` warning were real; tracking is now -0.03em and the line break is two block spans.
- Contrast (computed): ink #222428 on white 15.54:1; secondary #54585e 7.16:1; labels #60656b 5.88:1; seat blue #1f50ba 7.2:1; "On time" green on its tint 6.07:1; "Window" 6.06:1; header text on the photo 5.46:1 at worst.
- Targets: back and share 44; the pill is information, not a control.
- Full-size rounds: (1) land and sea dots were indistinguishable, a latitude label collided with "CPH", and "12:55 Copenhagen" wrapped so the two codes did not align; (2) the seat "14A" overflowed its column and the map felt like a texture, so I framed it as a pale sky window and widened the seat column; (3) after the owner's rules, the photo header: the first crop put the white title over the grey wing (3.66:1 at worst), so I moved the crop to open sky and darkened the top of the overlay (5.46:1).

## Process findings
1. **Gap: "airy" and "crisp" are not feel words.**
2. **Gap: no HIG named scale** (see PROCESS-01-05.md): to get Dynamic Type sizes in CSS I had to add eight size steps and override eleven text styles with full JSON, and validate then complains about the formula steps it keeps.
3. **Confusing: per-property type overrides are refused** (`set text.body.sm.fontSize` is "not a token path").
4. **Helped:** `ring-shadow` gave exactly the faint ring plus soft shadow a paper ticket wants, and the `accent2` pale-sky ramp supplied the map and the page gradient without leaving the system.
