# 09 Pagewright: on-call page

Replaces `watch/06-hush-breathe` (audited 2 of 5, "remake"). Render: `shot.png`, 205 x 251 CSS px at scale 3 (615 x 753), clipped to the display shape by `../render.py`, the same as the other watch pieces. Page: `index.html`.

## Direction
Pagewright is a fictional incident-management tool for engineering teams. At 3:12 a.m. the on-call engineer for `card-auth` (a payments company's card authorisation service) is paged into a severity-1 incident that two colleagues are already working. The wrist has to answer four questions in one glance (how bad, what, how long, who else) and offer two actions. Feel words: **sober, technical, reliable**.

What the old piece did that this one must not: a blurry glow orb with grain as the whole interface, rings with no data, the progress said twice, a wordmark top-left (`../../audit/watch--06-hush-breathe.json`). Here there is no art, no glow and no wordmark: the top-left holds the severity, the top-right the time, and every other mark is a fact or an action.

## References (Mobbin; cited by link only, nothing saved)
Mobbin has no watch platform and no on-call or incident app on iOS (two searches: "on-call incident alert with severity, acknowledge and escalate", "PagerDuty incident detail"), so the structure comes from iOS urgent-interruption screens and the data grammar from web incident tools.

| Reference | What it taught |
|---|---|
| Rivian, alarm triggered: https://mobbin.com/screens/c25ddb40-e4a0-4f77-a9a6-9996a8afa4ed | One urgent statement, then two stacked full-width actions: the primary filled, the secondary quieter. |
| Messages, incoming call: https://mobbin.com/screens/14202221-b6bd-49f8-bed3-14a8f4bf985a | The system's own "you are being called" layout: what and who at the top, big targets at the bottom, nothing between. |
| incident.io, incident page: https://mobbin.com/screens/b32b19f4-5c25-40d5-837e-408de7cec04d | The grammar of an incident: a short ID, a severity tag as the only filled colour, "Ongoing for 6m 2s". |
| Better Stack, incident timeline: https://mobbin.com/screens/c17baca1-a797-44ab-a5c7-da5d513c31cc | Severity, affected team and who acknowledged written as plain metadata, not badges. |

## System (engine)
Full log: `engine-log.txt`; decisions: `opendesigner/decisions.md`.
```
sketch --name "Pagewright" --brand "#FF3B4E" --audience large --platforms watch --feel sober,technical,reliable --delegated feel,audience,platforms
standard override STD-visual-details-24 --why "watch: black edge-to-edge"; pick Q-theme-01 dark-only; pick Q-color-21 black; pick Q-plat-02 watch; pick Q-plat-04 watch
set raw.textFace "Barlow Semi Condensed"; set raw.fontLicence {...}; set raw.baseSize 17; set dials.* (below); build; design-md
```
| Dial | Value | Why |
|---|---|---|
| expression | 30 | an instrument, not a poster |
| brandPresence | 30 | red marks severity only |
| density | 45 | a page carries five facts and two actions |
| energy | 40 | urgent but calm; nothing moves |
| roundness | 70 | watchOS capsule buttons |
| depth | 0 | flat OLED black |
| colorfulness | 15 | monochrome plus one red |
| warmth | 30 | cool neutral greys, no brown |

Colour: one red, `--ds-color-brand-seed` #FF3B4E (a cool signal red, not the system red #FF453A and not Thrum's red-orange #FF5436), used once as the SEV 1 tag with black text (6.0:1). Everything else is the engine's dark neutrals: text-primary #d7dadf, text-secondary #9298a5 (7.3:1 on black), Escalate label 9.5:1 on neutral-dark-6, Acknowledge black on #d7dadf 15:1.

## Font and type scale
One family: **Barlow Semi Condensed** (SIL OFL, Google Fonts), a narrow DIN-like grotesque that stands in for the watch's compact system face and reads as an instrument. Weights 500, 600, 700.

watchOS text styles at the xLarge size (44/45/49 mm default; Apple HIG, Typography): Large Title 40, Title 1 38, Title 2 30, Title 3 20, Headline 17, Body 17, Caption 1 16, Caption 2 15, Footnote 1 14, Footnote 2 13.

| Role | Size | Used for |
|---|---|---|
| Footnote 2 | 13 | responder initials |
| Caption 2 | 15 | the SEV 1 tag, "Declines 31%, usually 4%", "Open 14 min · INC-2291", "Noor, Bastian on it" |
| Headline / Body | 17 (`--ds-font-size-17`) | the clock, both button labels |
| Title 2 | 30 | the service name `card-auth` |

Four sizes; 13, 15 and 30 are HIG values outside the engine scale (14, 17, 20, 24, 29).

## Outside the tokens, on purpose
- Hardware: `--display-w/h/r` (205 x 251, 48 px corners) and the corner insets (18 px left, 22 px right, 9 px button margins) are the device, as in the other watch pieces.
- The three HIG sizes above.

## Look and fix (rounds, scores)
1. **Round 1, score 3.5.** Red "SEV 1" as plain text, `card-auth` at 600, avatars overlapping. Next to Headway (04) and Onething (08) at the same 615 x 753 size it read as a correct but plain notification; the left edges of the title row (26 px) and the body (14 px) did not line up.
2. **Round 2, score 4.** Severity became a filled tag with black text (one signal plus the word), the service name dropped to weight 500, the title row and body share one 18 px left edge (checked against the 48 px corner: the tag's corner clears it), the body moved up 1 px to give the buttons room.
3. **Round 3 (coordinator's name check), score 4.** Responders were "Ilse, Marek"; "Ilse" is already the engineer in `styles/05-comic`, also an incident story, so they became Noor and Bastian. The overlapping monograms clipped the second letter ("NA" read "N"), so they now sit 4 px apart. The meta lines lost their `<br>` (preflight M7) and are two blocks.

Final score **4 of 5**: it would pass as a shipped watchOS long-look for an on-call tool. It is conventional by design; the two stacked buttons take about 40% of the display, which is right for a page at 3 a.m. but leaves no room for one ownable object.

## Checks
- `validate`: passes, 0 warnings, 5 notes.
- `review --project`: clean after four fixes (3 px paddings and gaps to `space-2`/`space-4`, `bottom: 8px` to `space-8`, the avatar ring shadow removed). DESIGN.md refreshed with `design-md`.
- `preflight --medium web`: M9 false error (Barlow loads through a Google Fonts link, as everywhere in the showcase); M8 warns that 13 px is under 14 px for web, which is a watchOS Footnote 2, not web text (recorded as a gap).
- Targets: both buttons 44 px high and full width; focus outline 2 px on each.
- Names: Pagewright, card-auth, INC-2291, Noor, Bastian checked against all of `brand/showcase` (no other use); "Pagewright" web-searched: no product by that name.

## Process findings (this piece)
- **DESIGN.md front matter is wrong for a dark-only system.** After `Q-theme-01 dark-only` and `Q-color-21 black` it still lists `surface: #fcfdff`, `on-surface: #222428`, `primary: #e0293f` with white text. An agent reading only the front matter would build a light screen. Recorded (`feedback`, bug).
- **The brand red cannot be the alert red.** The engine darkened the brand for buttons ("#E0293F, your exact color is kept for the logo", assuming white text) and keeps its own danger ramp (#c94c44), so the system holds three reds when an incident tool wants one. Recorded (gap).
- **Preflight has no watch medium**, so watchOS Footnote sizes are judged by web minimums. Recorded (gap).
- Mobbin has no watch platform and no incident app on iOS; the structure had to be borrowed from alarms and calls, and the content from web incident tools.
- The shared scratchpad is wiped by parallel sessions: my scratch files and a downloaded reference photo disappeared twice mid-task. I moved scratch work to a session folder of its own.

Fix 2026-10-14 (after the independent audit, score 4): the main button read "Acknowledge" although Noor and Bastian were already on the incident; it now reads "Join incident".
