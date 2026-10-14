# 01 · Halden Private: private banking home

## Direction
Halden Private is a fictional private bank for people with complex wealth (founders, families, trustees). The home screen should feel like the inside of a good leather wallet: deep bottle green-black, one restrained gold, a metal card you want to touch, and numerals set like an engraved certificate. Feel words: **premium, calm, trusted**.

Shape language: sharp tailored corners (4 px controls), hairline rules, a guilloche rosette. Type: a high-contrast didone (Bodoni Moda) for the wealth figure, the wordmark and the section title; Inter for everything you operate. Two fonts, no more.

## References (Mobbin, structure only)
- https://mobbin.com/screens/f1e10eb9-dfe8-4817-8e82-43272bc17ede (a business bank, dark home): the balance with smaller superscript cents directly above a full-bleed line chart. Taught the hero rhythm: label, figure, delta, then the chart with no axis.
- https://mobbin.com/screens/0a2c9de0-048e-444e-876a-de3daf00f81c (a neobank card screen): the physical card as the hero with the next card peeking in from the right, so the carousel reads without arrows.
- https://mobbin.com/screens/7b451837-103e-44be-9d06-4ffa97f48f4e (a business account home, dark): dark grouped content where amounts sit right-aligned in tabular figures with a second line for the change. Taught the row density.

## System (engine)
```
sketch --name "Halden Private" --brand "#C9A86A" --audience regular --platforms ios --feel premium,calm,trusted --theme system-light-dark --delegated all
pick Q-color-01 keep-hex · pick Q-color-21 near-black · set raw.neutralBase "#0E2A1F" · set raw.brandColor "#C9A86A" (restored, see findings)
pick Q-type-01 brand-display · set raw.displayFace "Bodoni Moda" · set raw.textFace "Inter" · pick Q-type-02 yes · pick Q-type-08 17
set overrides.type.displayReach 4
```
Dials (all `--set-by delegated`): expression 55 (one hero figure and one hero card), brandPresence 70 (gold and the serif carry the brand), density 35 (unhurried), energy 10 (nothing hurries), roundness 30 (4 px controls, 8 px containers), depth 65 (the card needs light and shadow), colorfulness 22 (gold is the only color), warmth 45.

The page renders the system's **dark** mapping (`<html data-theme="dark">`). `dark-only` was refused by house standard STD-visual-details-24, so the system keeps a light mode it is never shown in.

## Fonts
Bodoni Moda (SIL OFL) and Inter (SIL OFL), both from Google Fonts with a `<link>`.

## Where I went outside the tokens, and why
- **The metal card** (ISO card corner 13 px, brushed-metal gradients, specular sheen, noise, engraved text shadows, chip). It is a physical object, not UI; every color in it still comes from the neutral-dark and accent-dark ramps. Lines are marked `od-ignore: physical card art`.
- **Wealth figure** at 52 px weight 450 (the token heading weight is 600): a didone at 600 turns heavy and clotted; 450 keeps the hairlines. Pence and currency sign are 21 and 33 px, both scale steps.
- The atmosphere gradient behind the content mixes ramp steps 1, 2, 7 and accent 8.

## Checks
- `engine.py validate`: 0 errors, 2 warnings (light mode only: the gold primary fill on near-white is 2.2:1 against the page; a text-labelled button needs no boundary contrast, and this screen is dark).
- `engine.py review`: from 64 findings down to 12 after tokenising the UI spacing; the rest are element sizes, hairline rings and the home indicator (false positives, see findings).
- `preflight.py html --medium web`: 3 errors. "Bodoni Moda / Inter have no @font-face" (they load through the Google Fonts `<link>` the brief allows) and "text under 12 px for web: 11" (iOS tab labels). Neither is a real defect on an iOS screen; preflight has no app medium.
- Checklist (type and layout): tracking no tighter than -0.015em; 6 sizes (see the type scale below); no wraps; contrast: secondary text #95b1a4 on #171e1b is 7.35:1, tertiary tab labels #7d9c8e on #121614 are 6.1:1, gold link text #dac298 is 9.8:1 (computed); targets 44 pt (bell, avatar, range picker with an enlarged hit area, tabs 72 × 48).
- Reviewed at full size three times: round 1 fixed overflow (accounts under the tab bar), a perspective tilt that made the card look warped, the guilloche reading as a hole, and the chart dot clipped at the edge; round 2 fixed the chart fill running past the line and tuned the rosette.

## Process findings
1. **Bug: the sketch replaced an explicit brand hex.** `--brand "#C9A86A" --delegated all` recorded D-0005 `raw.brandColor = "#8f7032"` "a readable shade ... (an olive)". Gold with dark text passes (about 9:1), so nothing needed fixing. `pick Q-color-01 keep-hex` afterwards did not restore it; I set `raw.brandColor` again.
2. **Bug: iOS body text fell to 14 px** when Brand presence went to 70 (`platform.useNativeBaseSize` turns off at 50+), with 11 px labels. Fixed with `pick Q-type-08 17`.
3. **Gap: open fonts not recognised.** Bodoni Moda is OFL, but validate warned it had no app licence until I answered Q-type-02 `yes`.
4. **Gap: tinted darks.** Ramp ends cap neutral chroma at 0.008, so "deep green-black" needs `raw.neutralBase` with a stronger green; Q-color-09 has no "tinted dark" option.
5. **Gap: no 11 pt iOS caption / tab label step.**
6. **Confusing: review vs tokens.** `engine.py review` flags `gap: 6px` with "write spacing in rem" (STD-accessibility-motion-13), but the generated `--ds-space-*` tokens are themselves in px. It also suggests `--ds-elevation-raised` for a 1 px inset ring and `--ds-space-0` for a negative hit-area margin.
7. **Preflight has no iOS/app medium** and treats a Google Fonts `<link>` as "no @font-face", which contradicts BRIEF.md's font rule.
8. Helped: `set` prints how many token values change, and the dark ramps from a tinted neutral base came out beautifully even, so the whole palette stayed in the system.

All feedback recorded with `engine.py feedback` in `opendesigner/feedback.md`.

## Revision for the owner's type and color rules (mid-run)
Type scale, Apple HIG Dynamic Type roles, set through the engine (`Q-type-10 named`, `Q-type-09 hand-tuned`, 8 `font.size` steps and 11 text-style overrides; see PROCESS-01-05.md):

| Role | Size / line | Used for |
|---|---|---|
| Display (custom) | 52 / 52, Bodoni 450 | the wealth figure |
| Large Title | 34 | the pound sign beside it |
| Title 2 | 22 / 28, Bodoni 400 | "Holdings", the pence, the card monogram |
| Body / Headline | 17 / 22 | rows, amounts, wordmark, status bar |
| Subheadline | 15 / 20 | secondary lines, the overline, card engraving, "See all", range picker |
| Caption 2 | 11 / 13 | tab bar labels (now a token, `--ds-font-size-11`) |

Six sizes, each at least 13% from its neighbour, nothing under 11. Changes made for the rules:
- The wordmark was "HALDEN *Private*" with an italic word: now "HALDEN PRIVATE" in one roman face, the second word in gold (color, not italic).
- "Holdings" was an italic serif title: now roman Bodoni 400 (titles don't have to be bold).
- The overline "TOTAL WEALTH · 14 OCT" in 11 px caps became the Subheadline "Total wealth · 14 October".
- Card "Reserve" was italic: now spaced roman capitals. Card text moved from 14 to 15 (Subheadline), the monogram to 22.
- Sizes 14, 21 and 33 (formula steps) became 15, 22 and 34 (HIG steps).
- Color was already within the rule: green-black background with ivory and gold text (7.35:1 and up).
- `engine.py validate` now warns "15 text sizes", because the old formula steps cannot be removed (finding).
