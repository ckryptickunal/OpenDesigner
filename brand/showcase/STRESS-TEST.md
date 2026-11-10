# Showcase stress test: findings

What this covers: 46 pieces from 8 builders (10 heroes, 10 components, 10 app screens, 8 watch screens, 8 footers) plus the orchestrator's brand kit. Inputs: `BRIEF.md`, the 8 `PROCESS*.md` files, all 183 builder entries in `*/opendesigner/feedback.md`, the 7 brand-kit entries in `brand/opendesigner/feedback.md`, `brand/TYPE-REVIEW.md` sections 1 and 7, and `_coordination/OWNER-FEEDBACK.md`.

How it was checked: every bug was checked against the code (function and line given). Most were reproduced in a scratch folder outside the repo (`<tmp>` below), and outputs are pasted as printed. Nothing in the repo's own `opendesigner/` folders was touched.

Line numbers in `engine.py` are from the committed version (HEAD `78dc59f`, last changed 2026-10-04), which is the code the builders ran. While this review was running, another session added an uncommitted overview page and an `artifact` export to `engine.py` (about 400 lines). That change touches none of the findings, but it shifts line numbers: +1 after line 22, and about +395 after line 8712. Search by function name if a line looks off. The one traceback below was printed by the working-tree file, so its line numbers are shifted.

> **Update, later on 2026-10-14: the audit against shipped work.** Kunal judged most pieces as AI slop, so all 54 (the 46 plus 8 mockups) were audited against three to five shipped products each on Mobbin (`audit/`, one JSON per piece: score, verdict, tags, the visible tells, fixes and the references by URL). Result: 28 keep, 20 polish, 6 remake; average 3.5 of 5. The judgement in section 1 below was too kind. The tells, counted, and what the pieces that passed share are now rules for every builder: `skills/opendesigner/references/making.md` section 11. The six remakes and the polish list are being rebuilt with B2B subjects first (Kunal: the highest-paying customers are B2B and enterprise).

---

## 1. The headline result

Yes, mostly. Judged by the five renders I opened and the builders' own rankings, most of the 46 pieces look like studio work (the ocean observatory hero, the phosphor settings panel and the watch board are the standouts). About a third are, in the builders' own words, competent but conventional.

The engine earned its place on the parts that are easy to get wrong: contrast-safe color roles, spacing, radii, focus rings and motion. It got in the way where a piece gets its identity:
- Every builder had to restore or work around a brand color the engine changed.
- Most display type, light weights, tinted grounds, hard shadows and art colors were made outside the tokens or against them.
- The preflight check gave false errors on at least 33 pieces and could not see any font size that came from the tokens.

---

## 2. Findings ranked by impact

"Builders" means the 8 category builders (app 01-05, app 06-10, components 01-05, components 06-10, footers, heroes 01-05, heroes 06-10, watch). "Pieces" counts pieces named in the feedback or in a PROCESS file. "Entries" counts `feedback.md` entries (the appendix maps each one).

| # | Finding | Label | Builders | Pieces | Entries |
|---|---|---|---|---|---|
| 1 | Sketch throws away a brand color the person typed | bug | 8/8 | 17 + brand kit | 17 |
| 2 | Preflight can't read a token-built page | bug | 8/8 | 33+ (false M9 error) | 13 |
| 3 | No display set, and display weight is always heavier | gap | 7/8 | 16+ | 8 |
| 4 | The type scale ignores named roles and platform scales | gap | 5/8 | 14 | 10 |
| 5 | Dark-only and light-only are blocked, then half-ignored | bug, confusing | 8/8 | 25 | 10 |
| 6 | Dark mode dulls the brand color | bug | 5/8 | 12 | 5 |
| 7 | Text floors disagree, and hidden couplings move body size | bug | 8/8 | 15 | 9 |
| 8 | Typefaces are hard to set, and free fonts show as licence risks | gap, confusing | 8/8 | 23+ | 10 |
| 9 | High Warmth makes neutrals brown, with no warning | gap | 7/8 | 9 | 6 |
| 10 | Weights the font does not have | bug | 5/8 | 6 | 3 |
| 11 | Nothing checks text over art, photos or glass | gap | 5/8 | 6 | 4 |
| 12 | Watch is not a platform | bug, gap | 1/8 | 8 | 2 |
| 13 | No palette for artwork | gap | 6/8 | 10 | 9 |
| 14 | Tinted grounds can't be reached | gap | 5/8 | 8 | 6 |
| 15 | `review` suggests the wrong token | bug | 7/8 | 13+ | 11 |
| 16 | Spacing tokens break the house rem standard | bug | 5/8 | 5 named (all systems) | 4 |
| 17 | `set` accepts what it should refuse | bug | 3/8 + brand kit | 6 | 6 |
| 18 | Feel words: common ones unknown, conflicts never clear | gap, bug | 7/8 | 12 | 12 |
| 19 | Secondary colors are not kept as given | bug, confusing | 5/8 | 7 | 5 |
| 20 | Missing depth styles (hard offset shadow, glow, dark depth) | gap | 6/8 | 8 | 8 |
| 21 | Smaller color-role gaps | gap | 6/8 | 9 | 10 |
| 22 | Motion and component recipes stop short | gap | 2/8 | 4 | 6 |
| 23 | Editorial and script type features | gap | 2/8 | 4 | 4 |
| 24 | `opendesigner-illustrate` rough edges | bug, confusing | 3/8 | 3 | 6 |
| 25 | `opendesigner-paint` can't paint one still unattended | gap, bug | 3/8 | 4 | 5 |

### The expected clusters: confirmed or rejected

| Cluster you expected | Verdict |
|---|---|
| Brand color replaced under `--delegated` | Confirmed (finding 1) |
| Dark mode dulling the brand color | Confirmed (6) |
| Preflight missing rem and token sizes, wrongly flagging Google Fonts | Confirmed (2), plus a shorthand parsing bug |
| No display set or light display weight | Confirmed (3), with one nuance: `set type.headingWeight 300` works, but it is undocumented and display is still forced 100 heavier |
| No watch platform | Confirmed (12), plus a one-word key mismatch that drops the native body size |
| Warmth producing brown neutrals | Confirmed (9) |
| House-standard friction with single-theme systems | Confirmed (5). One builder claim is too strong: the second error (from `standard override`) does say to run `init` first; only the first refusal is silent about the order |
| Setting typefaces undiscoverable | Confirmed (8) |
| Weights the font doesn't have | Confirmed (10) |
| No check for text over art or photos | Confirmed (11). Partly covered: the review probe marks a CSS image or gradient backdrop as "sample the pixels"; canvas, SVG and sibling layers are misread |
| Missing artwork palettes | Confirmed (13) |
| `set` accepting unknown keys | Confirmed (17) |

Builder claims I rejected or softened:
- "'precise' was dropped without a word" (heroes/07 F-001). Rejected in part: sketch does print "I don't know the feel word 'precise' yet". What is true is that the word is stored nowhere, so the question is lost unless the agent passes it on at once (finding 18).
- "label-md and label-sm are the same size" (brand F-005). Confirmed, but on purpose: `label.sm` is the capitals overline variant (`build_typography`, engine.py:1690-1691). This is confusing, not a bug.
- "triadic is not triadic" (components/04 F-002). Confirmed: `HARMONY["triadic"] = (60, -60)` (engine.py:905, tagged `[inferred]`, following Material's tertiary +60). The math is intended; the name is misleading.
- "each illustrate search overwrites candidates.json" (app-screens/06 F-002). True by default, but a `--keep` flag exists (illustrate.py:1600). It has no help text and SKILL.md doesn't mention it, so this is confusing, not a bug.
- "an espresso seed gives plain greys for steps 1-8" (heroes/05 F-001). Only at low Colorfulness. At default Colorfulness, my repro gave tinted steps that jump from `#f0bfa6` (step 7) to `#b37858` (step 8). The missing mid-tones are confirmed.

---

### 1. Sketch throws away a brand color the person typed (bug)

- **Hit:** 8 of 8 builders. 17 pieces plus the brand kit:
  - app 01, 02, 04, 08, 09
  - components 01, 03, 04, 06, 08, 09, 10
  - footers 01
  - heroes 01, 02, 08
  - watch 01
- **Evidence:** `components/04-upload-brutal`: `#FFE500` became `#847600` ("an olive"). `app-screens/04`: acid lime `#D4FF3A` became `#677e00`. `footers/01-brask-wordmark/opendesigner/decisions.md` has D-0004 (the given hex), D-0005 (the rewrite) and D-0021 (set back by hand). Three builders who left the brand out of `--delegated` got exact hexes from then on (footers 02-08, heroes 03, watch 02-08).
- **Verified:**
  - `cmd_sketch`, engine.py:9435-9438. When `sb("brand")` is true, it calls `readable_shade` and overwrites `raw.brandColor`. `--delegated all` counts the brand as delegated even when `--brand` was typed.
  - `readable_shade` (engine.py:9296) only ever solves for white text. It never considers dark text, although `solid_text_for` (engine.py:1024) already supports dark on-color.
  - `color_words` (engine.py:9280) renames dark oranges "brown", dark yellows "olive" and dark pinks "crimson".
  - `color.brand.seed` is described as "the brand color exactly as given" (engine.py:1280) but holds the rewritten hex.
  - `pick Q-color-01 keep-hex` only sets `raw.flags.brandExact` (engine.py:3465), so it cannot bring the typed hex back.

  ```
  $ engine.py --dir <tmp>/r1/opendesigner sketch --name Test --brand "#FFE500" --audience regular --platforms web --feel bold,playful --delegated all
  I picked an olive for buttons, links and focus, with white text that reads clearly on it. Say if you want another color.
  state.json raw.brandColor = #847600 ; tokens.css: --ds-color-brand-seed: #847600;
  $ engine.py --dir <tmp>/r1/opendesigner pick Q-color-01 keep-hex
    recorded; the tokens already match this answer.
  raw.brandColor = #847600   ("ffe500" appears 0 times in tokens.css)
  $ ... same sketch with --delegated audience,platforms,feel
  Your brand color is on the buttons exactly, with dark text on it, because white text would be too faint.
  raw.brandColor = #ffe500
  ```
- **User-visible effect:** A light brand color (yellow, lime, amber, peach, gold) turns into a muddy dark shade, so the identity is gone. The message says "I picked" and gives the wrong hue name, so people don't notice.
- **Fix:**
  - In `cmd_sketch` (engine.py:9435), never apply `readable_shade` to a hex given with `--brand`, even under `--delegated all`; record it as `chosen`.
  - Keep `readable_shade` only for a color the model invents. Let it choose dark text when dark text passes (reuse `solid_text_for`).
  - Make `pick Q-color-01 keep-hex` restore the first typed hex from decisions.md.
  - Have `color_words` name the typed hex, not the shade.
- **Already open:** no (not in OWNER-FEEDBACK).

### 2. Preflight can't read a token-built page (bug)

> **Fixed on 2026-10-14** in `skills/opendesigner-preflight` (checked before its first push): Google Fonts faces now count as loaded; font sizes are read from token-built pages (rem, pt, clamp(), var() fallbacks, the font shorthand, inline styles); `--medium app` (11 pt) and `--medium watch` (12 pt) exist; the web floor fails under 11 px and warns at 11 px. Seven tests cover it. Open: the engine still gives web systems an 11 px small body style.

- **Hit:** 8 of 8 builders. The false M9 error appeared on at least 33 of 46 pieces:
  - footers: 7 of 8
  - watch: 8 of 8
  - heroes: 10 of 10
  - components: 06, 07, 08, 10 and 03
  - app screens: 06, 10 and at least one of 01-05

  `font sizes in px: []` was reported on most token pages. In components/09, a fully tokenised page passed with 0 errors.
- **Evidence:** heroes/01 F-007 and F-008; heroes/02 F-006 (`[22]`, a line height read as a size); components/03 F-004 (pass or fail depends on syntax); watch/08 F-001; app-screens PROCESS-01-05 #11.
- **Verified** in `skills/opendesigner-preflight/scripts/preflight.py`:
  - `read_css` (line 39) skips any `href` that contains `:`, so Google Fonts stylesheets are never read.
  - M9 (lines 94-96) counts only local `@font-face`.
  - `font-size` matches only `^\d+px` (line 74), so rem sizes are dropped.
  - The `font` shorthand regex (line 76) takes the first `NNpx`, which is the line height when the size is a `var()`. With no px in the shorthand, it extracts no family at all.
  - `MIN` (line 17) has only `video` and `web`; there is no app, iOS or watch medium.
  - M5 (line 112) ignores size.
  - Nothing looks for infinite animations (heroes/04 F-003).

  ```
  a.html: Google Fonts <link>, tokens.css, h1{font-family:"Fraunces"}, small{font-size:0.6875rem},
          code{font: 400 var(--ds-font-size-12)/22px var(--ds-font-family-mono)}, .tick{animation: ... infinite}
  ERROR  font "Fraunces" is used but has no @font-face, so another face may render  [M9]
         font sizes in px: [22]
  1 error(s), 0 warning(s).
  b.html: same face via h1{font:300 var(--ds-font-size-90)/1.1 "Fraunces",serif}, same 11px <small>
         font sizes in px: []
  0 error(s), 0 warning(s).
  ```
- **User-visible effect:** The one check meant to catch type mistakes before export raises a false error on almost every page, and it is silent about real 11 px text. Builders stopped trusting it and wrote their own Playwright checks.
- **Fix** (`check_html` and `read_css` in preflight.py):
  - Treat a `fonts.googleapis.com/css2?family=` link as declaring its families.
  - Convert rem and em at 16 px after `resolve()`.
  - Parse the shorthand as `[style] [weight] size[/line-height] family` after resolving `var()`.
  - Add `--medium app|watch` with their floors (11 pt and 12 pt).
  - Make M5 size-aware (allow about −0.03 em at 48 px and up).
  - Warn on `animation: ... infinite` with no `animation-play-state` control.
  - TYPE-REVIEW §7.4 also asks preflight to flag sizes that aren't in the scale; read the scale from `tokens.css`.
- **Already open:** OWNER-FEEDBACK item 4 says preflight was added. This finding is new.

### 3. No display set, and display weight is always heavier (gap)

- **Hit:** 7 of 8 builders and the brand kit. At least 16 pieces:
  - all 10 heroes (`displayReach` on 01-05; hand-set 104-124 px on 06 and 08; light weights on 07, 09, 10)
  - components 04 and 07
  - three app screens 01-05 (custom 52, 95 and 169 px numbers) and app 08
  - the watch display numerals
- **Evidence:** heroes/06 F-006 ("tops out at display-sm 90px even with ... expression 85"); brand F-003, F-004 and F-006 (45 distinct sizes in the brand kit); app-screens/08 F-004; heroes/07 F-005; components/07 F-003; TYPE-REVIEW §1 ("one scale with one ratio, 8 steps, stopping at 90 px").
- **Verified:**
  - `build_type_scale` (engine.py:1580) uses a display reach of 5.5 times body only with marketing surfaces, else 2.5. The `type.displayReach` override exists (`PARAM_OVERRIDES`, engine.py:2266) but appears in no stage file or SKILL.md.
  - `build_typography` (engine.py:1625) forces `display = heading + 100`. Heading weight comes from Energy bands 600/650/750 (`synthesis/levers.json`).

  ```
  surfaces "landing page:persuade", expression 85, energy 80, displayFace "Instrument Serif":
  --ds-font-size-12 ... --ds-font-size-90   (top step)
  --ds-font-weight-heading: 750;  --ds-font-weight-display: 850;
  $ engine.py set type.headingWeight 300   ->  --ds-font-weight-heading: 300;  --ds-font-weight-display: 400;
  ```
- **User-visible effect:** Hero and poster type is invented by hand, which led to the 45-size brand kit. The light or regular display titles the owner asked for are always a departure from the tokens.
- **Fix:**
  - In `build_type_scale` and `build_typography`, emit a separate display set (3-4 sizes, each with its own tracking, leading and weight) when marketing surfaces are in scope (DC-L02-11).
  - Add a display-weight answer (300-900, default equal to the heading weight, not +100).
  - Document `displayReach` and `headingWeight` in `stages/11-type-scale-and-text.md` through `synthesis/questionnaire.json`.
  - This is TYPE-REVIEW §7 items 2 and 3.
- **Already open:** OWNER-FEEDBACK engine gap 3 ("no viewing-distance or medium scale for type").

### 4. The type scale ignores named roles and platform scales (gap)

- **Hit:** 5 of 8 builders and the brand kit. 14 pieces:
  - app 01-05 (8 extra steps and 11 overridden styles in each)
  - 6 of 8 watch pieces (hand-set HIG sizes)
  - footers 06, components 01, heroes 08
- **Evidence:**
  - app-screens/05 F-001: the CSS gives body.sm 14, title 21/27 and headline 33, while Swift gives .subheadline 15, .title2 22 and .largeTitle 34.
  - app-screens/05 F-002 and F-003: steps can't be removed, and a step can't be changed by one property.
  - heroes/08 F-004: three face roles, 8 sizes, 14 or more styles and no caption.
  - watch/03 F-001: no watchOS roles.
  - footers/01 F-007: 8 steps against the owner's 6.
- **Verified:**
  - `IOS_TEXT_STYLES` (engine.py:7188) maps styles to Dynamic Type sizes for Swift, while CSS uses the ratio formula (`build_type_scale`, engine.py:1567).
  - Q-type-10 and Q-color-16 are in the record-only list `_R["rule"]` (engine.py:3607-3608), so answering them changes no token.
  - `set text.body.sm.fontSize` is refused: "is not a token path" (`cmd_set`).
- **User-visible effect:** Following Apple's or Google's scale, which the owner's rule requires, costs about 20 `set` calls per system. The CSS and Swift outputs of the same system disagree.
- **Fix:**
  - Make Q-type-10 `named` real: when chosen, `build_typography` takes HIG sizes (iOS, watchOS) or Material sizes (Android, web) for the named roles, instead of the formula.
  - Add a `caption` role.
  - For web marketing, cap the scale at 6 steps.
  - Let `cmd_set` accept `text.<role>.fontSize` and `font.size.<n>: null`.
- **Already open:** no.

### 5. Dark-only and light-only are blocked, then half-ignored (bug, confusing)

- **Hit:** 8 of 8 builders. About 25 pieces:
  - all 8 watch pieces
  - heroes 02, 04 and all of 06-10
  - app 01, 02, 04 and 08
  - components 01, 06, 08 and 10
  - footers 01 and 03
- **Evidence:** watch/02 F-001 ("6 of 8 watch systems warn 'In light mode...'"); components/01 F-003 and F-004; heroes/06 F-001; app-screens/08 F-003.
- **Verified:**
  - `cmd_sketch` (engine.py:9411-9422) refuses any theme that a standard's `breaks_options` lists. STD-visual-details-24 is only a **should** standard (`references/standards/visual-details.md:120`).
  - Q-theme-01 `dark-only` sets `darkMode: True, defaultTheme: dark` (engine.py:3595). `GenCtx` (engine.py:1227-1229) then keeps `modes = ["light", "dark"]`, so the light mode is still validated and exported.

  ```
  $ engine.py --dir <tmp>/r2/opendesigner sketch ... --platforms watch --theme dark-only ...
  Nothing was written: the theme dark-only breaks a standard. ... engine.py standard override STD-visual-details-24 --why "<their words>"
  $ engine.py --dir <tmp>/r2/opendesigner standard override STD-visual-details-24 --why "watch is dark only"
  no state at <tmp>/r2/opendesigner/state.json; run `engine.py init --dir ...` first
  (after init, override, sketch)
  WARN  In light mode, action primary background on base surface is too faint to see: contrast 1.16:1, needs 3.0:1.
  tokens.css still has a [data-theme="light"] block
  ```
- **User-visible effect:** The brief's own command fails, and so do watch, film and poster work. It takes three commands in an order nobody is told. The result still carries light-mode warnings and a light theme the product never shows.
- **Fix:**
  - In `GenCtx.__init__`, set `modes = ["dark"]` when Q-theme-01 is `dark-only`, so validate, `tokens.css` and DESIGN.md skip light.
  - In `synthesis/standards.json`, demote a **should** standard's `breaks_options` to a warning, or scope STD-visual-details-24 away from watch and persuade surfaces.
  - Make the sketch refusal print the working order (`init`, `standard override`, `sketch`), or let sketch take `--override STD-…`.
- **Already open:** yes, OWNER-FEEDBACK engine gap 1 ("A house standard blocked a dark-only film"). Still open.

### 6. Dark mode dulls the brand color (bug)

- **Hit:** 5 of 8 builders. 12 pieces: all 8 watch pieces, app 04, components 10, footers 01 and heroes 07. Every watch piece used `--ds-color-brand-seed` directly.
- **Evidence:** watch/01 F-002 (`#C8FF2E` became `#b0d468`; `#FF5436` became `#e86d55`); app-screens/04 F-002; footers/01 F-003; components/10 F-003; heroes/07 F-003 (the dark button became "muddy #418e9d").
- **Verified:** In `build_palette`, `accent_chroma_fn` (engine.py:1015) multiplies dark chroma by `DARK_ACCENT_CHROMA = 26/32` (line 740). The brand pin is applied only to the light ramp (engine.py:1085-1088, with the comment "becomes the light-mode solid"). Q-color-16 is record-only (engine.py:3608).

  ```
  dark-only watch, brand #C8FF2E:
  --ds-color-brand-seed: #c8ff2e;  --ds-color-accent-light-9: #c8ff2e;  --ds-color-accent-dark-9: #b0d468;
  dark --ds-color-bg-action-primary: var(--ds-color-accent-dark-9)
  sketch says: "Your brand color is on the buttons exactly, with dark text on it"
  ```
- **User-visible effect:** Neon, signal and phosphor brands look grey where they matter most, and the sketch message claims the opposite.
- **Fix:**
  - In `build_palette`, pin the brand at dark step 9 when `brandExact` is on and the on-color passes on the dark base, and always for dark-only.
  - Give Q-color-16 a "keep brand chroma in dark" option that acts on `k`.
  - Make `brand_line` (engine.py:9315) report the dark-mode shade.
- **Already open:** no.

### 7. Text floors disagree, and hidden couplings move body size (bug)

- **Hit:** 8 of 8 builders. 15 pieces:
  - app 01, 07, 08
  - components 03, 04, 06
  - footers 03, 04, 05
  - heroes 04, 05, 10
  - watch 03, 04, 07
- **Evidence:**
  - components/06 F-002: the engine emits 11 px; preflight errors below 12 and warns below 14.
  - app-screens/01 F-002 and app-screens/07 F-002: iOS body is 14 when Brand presence is 50 or more.
  - footers/04 F-001: `--audience large` leaves body at 16.
  - footers/03 F-002: a "read" surface silently caps the largest size at 38.
  - heroes/05 F-002: Density 5 gives a 19 px body.
- **Verified:**
  - `build_type_scale` hard-codes `min_size = 11` (engine.py:1583). Preflight's `MIN["web"] = (12, 14)` (preflight.py:17). Stage 11 says "avoid anything people must read below 12px on web" (`stages/11-type-scale-and-text.md:25`).
  - `synthesis/levers.json` has Brand presence 50-100 turn `platform.useNativeBaseSize` off, and Density 0-10 set the web base to 19.
  - Q-aud-01 `large` only sets Density 15 (engine.py:3436), which gives 16 px, while stage 02 line 20 promises "body 17px or more".

  ```
  ios, feel calm:            --ds-text-body-md-size: var(--ds-font-size-17);
  ios + set dials.brandPresence 70:  --ds-text-body-md-size: var(--ds-font-size-14);  --ds-text-label-sm-size: var(--ds-font-size-12);
  ```
- **User-visible effect:** Brand-led iOS apps get web-sized body text. Dense pages get 11 px text that preflight then calls an error. Each answer quietly changes a different number.
- **Fix:**
  - In `build_type_scale`, make the floor 12 px on web and 11 pt on native, and match preflight's `MIN` to it.
  - In `synthesis/levers.json`, keep the native base on native-only platforms whatever the Brand presence.
  - Map Q-aud-01 `large` to `raw.baseSize` 17 or 18 (engine.py:3436).
  - Print "largest text 38 px, because your surfaces are read or operate" in the sketch summary.
  - Say in the Density help that it changes text size.
- **Already open:** no.

### 8. Typefaces are hard to set, and free fonts show as licence risks (gap, confusing)

- **Hit:** 8 of 8 builders.
  - Licence false alarms on at least 23 pieces: app 01, 06, 07, 08, 10; components 06, 07, 08, 10; footers 04-07; heroes 01, 03, 04, 05, 06, 09; watch 01, 02, 04, 06.
  - Discoverability complaints from 5 builders.
- **Evidence:** footers/08 F-001 (found `raw.fontClass` plus `"=openClass"` by reading engine.py); heroes/06 F-002 (`set textFace` fails); footers/04 F-002; footers/07 F-001 (a Mincho face falls back to sans); heroes/08 F-006 (`ui-monospace` listed twice).
- **Verified:**
  - Sketch has no font option (engine.py:9060-9070).
  - `raw.textFace`, `displayFace` and `monoFace` appear in no stage file or SKILL.md, only in one pick hint (engine.py:3626).
  - `OPEN_FONTS` has 44 names (engine.py:1164). Fraunces, Fredoka, Instrument Serif, Newsreader, Bodoni Moda, Inter Tight, Archivo, Big Shoulders Display, Shippori Mincho, IBM Plex Sans Condensed, Alegreya, Atkinson Hyperlegible Next, Unbounded, VT323, Michroma and Bricolage Grotesque are all missing, though all are open-licence.
  - `face()` (engine.py:1639) appends the sans stack to every face, a serif included; the repro gave `"Instrument Serif", system-ui, ... sans-serif`.

  ```
  $ engine.py set textFace '"Figtree"'
  Nothing was changed: 'textFace' is not a token path: use lowercase kebab-case segments, like size.row.md.
  ```
- **User-visible effect:**
  - The default is `system-ui` and nothing asks for a face, so systems ship without a brand face (TYPE-REVIEW §1).
  - DESIGN.md tells people to "confirm the web licence" of free fonts.
  - Serif and Japanese faces fall back to a system sans.
- **Fix:**
  - Add `--text-face`, `--display-face` and `--mono-face` to sketch.
  - Name `set raw.textFace '"Name"'` in `stages/10-typeface.md` and in DESIGN.md's Typography section.
  - Accept a `google-fonts` licence source, or a much longer list, in `OPEN_FONTS`.
  - Make the fallback in `face()` follow the face's class and `raw.scripts`.
  - This is TYPE-REVIEW §7 items 1 and 6.
- **Already open:** yes, OWNER-FEEDBACK engine gap 4 ("system-ui is the font ... never asks for a shipped typeface").

### 9. High Warmth makes neutrals brown, with no warning (gap)

- **Hit:** 7 of 8 builders. 9 pieces: app 03 and 06, components 07, footers 01 and 04, heroes 03 and 09, watch 02 and 05. Every one was fixed by hand after the owner's color rule.
- **Evidence:** app-screens/03 F-006 (secondary text `#67543b`, inverse surface `#272420` under red-orange); watch/05 F-001 (tile `#261f1c`); app-screens/06 F-004 (Warmth has no effect once `raw.neutralBase` is set); components/07 F-001 (`pick Q-color-09 warm` made the greys less warm).
- **Verified:**
  - `NEUTRAL_CURVE` (engine.py:734) peaks at steps 9-10, which are the text steps, and is lowest at steps 1-2, the paper steps.
  - `raw.neutralBase` replaces the hue and chroma completely (engine.py:1001), so Warmth is ignored.
  - `NEUTRAL_TINTS["warm"] = (0.010, 70)` (engine.py:903) is weaker than a high Warmth tint.

  ```
  brand #E8590C, warmth 50: neutral-light-11 #575757, neutral-dark-1 #151515
  brand #E8590C, warmth 90: neutral-light-11 #605551, neutral-dark-1 #171514, neutral-dark-11 #b6a9a4
  build output lines mentioning brown, muddy or warmth: 0
  ```
- **User-visible effect:** You get exactly the "brown-black with orange" and "cream text on brown" look the owner's rule bans, and validate passes because the contrast is fine.
- **Fix:**
  - In `build_palette`, cap the neutral chroma at the text steps (9-12) at about 0.02, and let paper steps take the tint.
  - Add a validate warning when a dark neutral sits within about 40 degrees of a warm accent at chroma above 0.012.
  - Say in `set` output that `neutralBase` overrides Warmth.
  - Split "warm voice" from "warm neutrals" (footers PROCESS #5).
- **Already open:** no.

### 10. Weights the font does not have (bug)

- **Hit:** 5 of 8 builders. 6 pieces: app 02 and 08, components 01 and 07, heroes 06 and 08.
- **Evidence:** app-screens/02 F-002 (Instrument Serif, which ships 400 only, gets 600 and 700); app-screens/08 F-002 (Fredoka, 300-700, gets 750 and 850); heroes/06 F-005; components/07 F-003 (a serif display is too heavy).
- **Verified:** `build_typography` (engine.py:1617-1625) takes weights only from the dials, with no knowledge of the face. In the repro, Instrument Serif got heading 750 and display 850.
- **User-visible effect:** Browsers fake a bold, or silently cap the weight. Display type looks smeared or lighter than the tokens say.
- **Fix:** Record the weights each face ships (a `raw.fontWeights` list, or a small table next to `OPEN_FONTS`), and clamp `font.weight.*` to it in `build_typography`. Warn in validate when a weight token falls outside the face's range.
- **Already open:** no.

### 11. Nothing checks text over art, photos or glass (gap)

- **Hit:** 5 of 8 builders. 6 pieces with measured failures or misreads:
  - app 02: 4.15:1 on a painted sky
  - app 05: 3.66:1 on a photo
  - components 01: 2.88:1 on lit glass
  - components 03: 4.22:1 on heat cells
  - app 09: 1:1 and 1.29:1 misreads
  - components 08: art-derived colors

  The watch builder hand-checked every oklch color.
- **Evidence:** app-screens/02 F-003; components/01 F-007; app-screens/09 F-002; components/08 F-002. components PROCESS-01-05 #3: "Text over glass, art and tinted cells was where every real contrast failure was."
- **Verified:**
  - The engine's contrast check covers token pairs only (`validate_files`, engine.py:2953).
  - The review probe's `backdrop()` (`skills/opendesigner-review/scripts/probe.js:101`) walks ancestors only, so canvas, SVG and positioned sibling layers are invisible.
  - `review.py` (line 240) downgrades CSS image and gradient backdrops to "info: sample the pixels".
- **User-visible effect:** The contrast failures that matter most reach the render. Only builders who sampled pixels by hand caught them.
- **Fix:**
  - In `probe.js`, sample the rendered pixels under each text box (`elementsFromPoint` plus a screenshot crop through `capture.py`) instead of the ancestor walk.
  - In the engine, let a person declare art colors (`raw.artBackgrounds`) for `validate_files` to test text roles against.
- **Already open:** no.

### 12. Watch is not a platform (bug, gap)

- **Hit:** 1 builder, all 8 watch pieces.
- **Evidence:** watch/01 F-001: `--platforms watch` is accepted silently, and Q-plat-02 and Q-plat-04 `watch` print "tokens already match". watch/03 F-001: no watchOS roles. watch/04 F-001: Mobbin has no watch platform. watch PROCESS #1: `(pointer: fine)` lowers the target floor to 24 px.
- **Verified:**
  - `synthesis/levers.json` `platformBase` uses the key `"watchos"`, but the platform id is `watch`. So `build_type_scale` (engine.py:1572) never finds it.
  - Q-plat-01 options are web, ios, android, desktop and secondary only.

  ```
  ios,   feel calm:  "platform.useNativeBaseSize":true  body = var(--ds-font-size-17)
  watch, feel calm:  "platform.useNativeBaseSize":true  body = var(--ds-font-size-14)
  tokens.css: @media (pointer: fine) { :root { --ds-size-target-min: 24px; } }
  ```
- **User-visible effect:** A watch system gets a 14 px body, web roles and a 24 px target floor, and every piece needed a standard override plus hand-set HIG sizes.
- **Fix:**
  - Rename the key to `watch` in `synthesis/levers.json` (a one-word fix).
  - Add `watch` to Q-plat-01. Have it imply dark-only, a pure black base, watchOS text styles, a 44 pt floor that `(pointer: fine)` can't lower, and a corner safe area.
  - In the SKILL, say that Mobbin has no watch screens and suggest widgets as stand-ins.
- **Already open:** related to OWNER-FEEDBACK item 3 ("OpenDesigner has to apply to any visual surface").

### 13. No palette for artwork (gap)

- **Hit:** 6 of 8 builders. 10 pieces: heroes 03, 05, 06 and 09; footers 03 and 04; app 07; watch 02 and 07; components 03.
- **Evidence:**
  - heroes/03 F-002: terracotta light steps drift pink and jump from `#f2bea9` to `#b6775d`, and art bound to UI roles inverted in dark mode.
  - footers/04 F-003: no saturated mid-tones.
  - heroes/06 F-007 and app-screens/07 F-003: yellow tints come out tan.
  - watch/07 F-001: status colors stay dusty on black.
  - footers/03 F-003: no gradient token.
  - components/03 F-003: the only sequential ramp shares the selection hue.
  - heroes/09 F-001: steps around a pinned red go grey.
- **Verified:**
  - Ramps are built per UI step (`build_ramp`, engine.py:792).
  - Status chroma is `clamp(peak + 16, 48, 84)` (engine.py:1041), so it barely moves at low Colorfulness.

  ```
  brand #FFC83D, light steps 2-9: #f7f4ed #f2ebdc #ede2ca #e9d9b8 #e4d0a5 #dfc793 #a0823c #ffc83d
  ```
  (Tan, not butter. Step 8 is also darker than the pinned step 9.)
- **User-visible effect:** Art colors are mixed by hand with `color-mix()` or hard-coded, so the art drifts off the system and can flip in dark mode.
- **Fix:** Emit theme-independent `color.art.<hue>.1-7` families (5 to 7 saturated tones per hue). `opendesigner-paint`'s `paint.py brief` already computes them. Add a `color.gradient.brand` DTCG gradient from the accents, and a separate `color.heat` sequential ramp.
- **Already open:** no.

### 14. Tinted grounds can't be reached (gap)

- **Hit:** 5 of 8 builders. 8 pieces: app 01, 03 and 08; footers 05; heroes 01, 03, 05 and 07.
- **Evidence:** heroes/01 F-002 (`surface.base` is always step 1, `#fefcfb` even at Warmth 70); footers/05 F-002 (the paper color never appears); heroes/07 F-002 and app-screens/08 F-005 (a navy base still gives `#131519`); app-screens/01 F-004 (green-black).
- **Verified:**
  - `neutral_chroma` caps the ramp ends at 0.008 (engine.py:1008), and `neutralBase` chroma is capped at 0.05 (engine.py:1001).
  - `PARAM_OVERRIDES` has `color.dark.baseY` but no light twin (engine.py:2266).

  ```
  raw.darkBase "black": neutral-dark-1 #000000, -2 #010101, -3 #060606 (base, raised and overlay are indistinguishable)
  ```
- **User-visible effect:** Paper, cream, navy and ink-blue pages are hard-coded, or they borrow a chip-fill role.
- **Fix:**
  - Add `color.light.baseY` to `PARAM_OVERRIDES`.
  - Add a "page tone" answer (white, paper, cream, tinted dark) that lets steps 1-2 carry the base chroma.
  - With `darkBase black`, lift raised and overlay to visibly lighter steps (heroes/02 F-003).
- **Already open:** no.

### 15. `review` suggests the wrong token (bug)

- **Hit:** 7 of 8 builders. At least 13 pieces. Findings per page reached 103 on components/01, 78 on app 09 and 64 on app 01 (counts as reported by the builders; not re-run).
- **Evidence:** components/01 F-008 (a backdrop mapped to `text-on-action`; `width: 80px` mapped to `space-80`); components/02 F-003 (base-ui and Radix advice for a plain HTML page); components/05 F-002 (a spinner's period called over budget); heroes/04 F-004 (an elevation token suggested for a `text-shadow`).
- **Verified:**
  - In `cmd_review` (engine.py:9884-9893), width, height, top and left values on the space ladder go to `space_fix`.
  - `shadow_fix` (engine.py:9698) treats inset hairlines and text-shadows as elevation.
  - `std_applies` matches `web, react` standards on any web project.

  ```
  index.html:2  width: 20px  ->  use var(--ds-space-20)          (tokens.css has --ds-size-icon-md: 20px)
  index.html:3  box-shadow: inset 0 0 0 1px rgb(0 0 0 / .1)  ->  use var(--ds-elevation-raised)
  index.html:4  text-shadow: 0 1px 0 #fff  ->  use var(--ds-elevation-raised)
  index.html:5  margin: -4px  ->  use var(--ds-space-0) (-4 is off the 4px ladder)
  ```
- **User-visible effect:** The real drift is buried in noise, and following some of the advice breaks the CSS.
- **Fix** (in `cmd_review`):
  - Send width and height to `size.icon.*`, `size.control.*` and `size.target.min`, and skip offsets (`top`, `left`, negative margins).
  - Treat `inset 0 0 0 Npx` as a border.
  - Never suggest elevation for `text-shadow`, and exempt zero-offset colored glows.
  - Apply `react`-scoped standards only when `raw.stack` names react.
  - Exempt constant motion (spinners) from the 300 ms budget.
- **Already open:** no.

### 16. Spacing tokens break the house rem standard (bug)

- **Hit:** 5 of 8 builders, and every generated system. Named on components 01, heroes 01 and 07, watch 02, and in the app 01-05 PROCESS file.
- **Evidence:** watch/02 F-002: "review tells me to replace px spacing with var(--ds-space-N)... while every --ds-space-* token is itself in px".
- **Verified:** STD-accessibility-motion-13 (**must**) says to write spacing in rem or em (`standards/accessibility-motion.md:80`). The CSS export converts to rem only for `font.size.*` (engine.py:6690). Repro: `--ds-space-6: 6px;`, and the same review output shows

  ```
  index.html:6  gap: 6px  ->  use var(--ds-space-6)
  index.html:6  gap: 6px  ->  Write spacing in rem or em ... (STD-accessibility-motion-13, must)
  ```
- **User-visible effect:** The system breaks its own **must** rule, and the review contradicts itself in one report.
- **Fix:** Emit `space.*` in rem in the CSS exporter (engine.py:6690: extend the `rem=` condition), keeping px in DTCG `$extensions`. Exempt token values from the standard's review pattern.
- **Already open:** no.

### 17. `set` accepts what it should refuse (bug)

- **Hit:** 3 of 8 builders and the brand kit. 6 pieces: heroes 02, 04, 06 and 10; app 02; brand kit.
- **Evidence:**
  - brand F-001: `dials.colour` and `dials.notADial` were accepted.
  - heroes/04 F-001: a string dimension was accepted, then crashed `build`.
  - heroes/06 F-003: `set raw.feel` was accepted and did nothing.
  - heroes/02 F-004 and heroes/10 F-001: `secondaryColors` was silently ignored.
  - app-screens/02 F-001: a later dial silently undid an answer.
- **Verified:**
  - `cmd_set` (engine.py:4134-4136) checks the dial range, but never checks the id against `DIALS` (engine.py:510).
  - Q-depth-01 is implemented as a dial value (engine.py:3537), so `set dials.depth` overrides the answer with no warning.
  - `secondaryColors` is read only when `accentCount >= 2` (engine.py:1053).

  ```
  $ engine.py set dials.colour 62 --set-by delegated   ->  D-0009 set dials.colour = 62 (delegated)
                                                            no token changed: the system already had this value.
  $ engine.py set raw.secondaryColors '["#1F5FD1"]'      ->  no token changed: the system already had this value.
  $ engine.py set elevation.raised '{"color":"#000000","offsetX":"6px",...}'
  D-0014 set overrides.elevation.raised = {...} (chosen)
  Traceback ... File "engine.py", line 2851, in _px ... AttributeError: 'str' object has no attribute 'get'
  (stored in state.json; every later build fails in `css_dim`, engine.py:6644 in HEAD)
  ```
- **User-visible effect:**
  - Typos look like successes, and DESIGN.md then shows the default value.
  - One bad value bricks `build` with a traceback.
  - "no token changed: the system already had this value" is untrue in all three cases.
- **Fix:** In `cmd_set`:
  - Reject unknown `dials.*` and `raw.*` keys and list the valid ones.
  - Validate overrides against the token's DTCG `$type` before writing.
  - Warn when `secondaryColors` exceeds `accentCount`, or raise the count.
  - Warn when a dial contradicts a recorded answer.
- **Already open:** no.

### 18. Feel words: common ones unknown, conflicts never clear (gap, bug)

- **Hit:** 7 of 8 builders. 12 pieces.
  - Unknown words: editorial, natural, organic, precise, airy, crisp, expressive, literary, dreamy and dense.
  - The conflict warning persisted on app 10, components 10, footers 03 and 08, and watch 02.
- **Evidence:** app-screens/10 F-001; footers/03 F-001; components/10 F-004 (the warning names no command); heroes/06 F-003 ("tidy" maps to minimal and conflicts with playful; the fix is `set macros`, which is undocumented).
- **Verified:** `resolve_dials` (engine.py:658-661) builds conflicts from the macros without checking `explicit`, so setting the dial never clears them. Unknown words are printed once and not stored.

  ```
  sketch --feel serious,minimal,everyday ...  ->  WARN The feel words serious, minimal, everyday pull colorfulness in opposite directions. Pick which one wins
  set dials.colorfulness 35; build           ->  (same WARN again)
  sketch --feel editorial,natural,precise,organic,airy,crisp,expressive,literary,dreamy,tidy,calm
  I don't know the feel word 'editorial' yet, so I left it out. ... (9 such lines)
  taste.feelWords = ['tidy', 'calm']
  ```
- **User-visible effect:** Warnings that can't be cleared train people to ignore warnings. The brand's own words vanish from the record.
- **Fix:**
  - In `resolve_dials`, skip conflicts on dials in `explicit`, and name `engine.py set dials.<id>` in the message.
  - Store unknown words in `taste.unknownFeelWords` and list them in DESIGN.md.
  - Add mappings for the 10 words above (for example editorial: heritage + premium + serif display).
- **Already open:** yes, OWNER-FEEDBACK engine gap 2 ("The feel-conflict warning stays after the dials are set explicitly"). Still open.

### 19. Secondary colors are not kept as given (bug, confusing)

- **Hit:** 5 of 8 builders. 7 pieces: app 03; heroes 02, 03, 04 and 10; components 04 and 09.
- **Evidence:** heroes/03 F-001 (sage `#7E9475` became bright grass `#6c9c57`); app-screens/03 F-002 (olive became acid `#6c7d00`); components/04 F-003 (`secondaryColors` is documented only in zoom.md); components/09 F-005.
- **Verified:** When exact, `build_palette` gives a secondary `max(peak, hct_chroma_of_hex(sec))` (engine.py:1056 and 1062), so a muted color is lifted to the dial's chroma, and nothing pins it at step 9. There is no `accent2.seed` token. `secondaryColors` appears only in `zoom.md:28`.

  ```
  accentCount 2, secondaryColors ["#1F5FD1"] -> accent2-light-9 #3171e3 ; ["#7E9475"] -> #719a5f
  ```
- **User-visible effect:** Exact secondary brand colors (process cyan, sage, olive) drift, so the art and the UI disagree.
- **Fix:** In `build_palette`, pin each secondary at step 9 with its own chroma when `brandExact` is on, and emit `color.accent2.seed` and `color.accent3.seed`. Offer `secondaryColors` in Q-color-01 and Q-color-04 (`synthesis/questionnaire.json`). Rename `triadic`, or use 120 degrees (engine.py:905).
- **Already open:** no.

### 20. Missing depth styles: hard offset shadow, glow, dark depth (gap)

- **Hit:** 6 of 8 builders. 8 pieces.
  - The hard offset shadow was hand-written in app 07, components 04, footers 06 and heroes 04.
  - Other pieces: heroes 02 (glow and dark depth), heroes 08 (chrome), heroes 06 (tinted shadow), components 06 (overlay with no shadow at Depth 15).
- **Evidence:** app-screens/07 F-001: `pick Q-dir-01 neo-brutalist` changes nothing. footers/06 F-001: the stage file says "One hard shadow looks dated".
- **Verified:**
  - `synthesis/levers.json` preset `neobrutal.extra = {"offsetShadow": "4px solid", "borderWidth": "thick", ...}`, but `offsetShadow` appears 0 times in engine.py.
  - Q-depth-01 options are shadow, tonal, borders, ring-shadow and glass.
  - `stages/15-depth-borders-and-materials.detailed.md:28` writes a taste call as a rule.
- **User-visible effect:** Neo-brutalist and retro-print work, a common showcase style, can't come from the tokens.
- **Fix:**
  - Add a `hard` depth model (offset steps, ink color, pressed = 0) and read the preset's `extra` in `resolve_dials` and the elevation builder.
  - Add glow tokens (color plus blur, zero offset) for dark systems.
  - Keep a minimal ring on `elevation.overlay` at low Depth.
  - Soften the stage 15 sentence in `synthesis/questionnaire.json`.
- **Already open:** no.

### 21. Smaller color-role gaps (gap)

- **Hit:** 6 of 8 builders. 9 pieces.

| Gap | Pieces | Verified | Fix (file, function) |
|---|---|---|---|
| Colorfulness mixes "how many hues" with "how saturated" | components 10 | `accentCount` comes from the same dial (`build_palette`, engine.py:1050) | Separate `raw.accentCount` from chroma in the Colorfulness dial map in `synthesis/levers.json` |
| Status colors can't be pinned | app 10, watch 07 | `status_peak` clamp (engine.py:1041) | `raw.statusColors` hexes in `build_palette` |
| No hairline or divider role lighter than `border.subtle` | components 06, footers 02 | builder evidence; not re-run | add `color.border.hairline` (step 4-5) |
| No accent role for inverse surfaces | app 03 | builder evidence | add `color.text.accent-inverse` |
| Alpha ramp exists but is undocumented; no white veil in light mode | components 01, 02 | builder evidence | name the alpha ramps in DESIGN.md; add `neutral-alpha-white-*` |
| A near-black brand collapses steps 10-12 to `#000000` | components 02 | builder evidence | map a monochrome accent onto the neutral ink steps |
| Contrast fix suggests a step that undoes the brand pin; never suggests a border | components 10, footers 06 | message at engine.py:3338 | add "or give the control a 3:1 border" (WCAG 1.4.11) |

- **User-visible effect:** Builders reach into ramp steps by number, which the docs say components must never do.
- **Already open:** no.

### 22. Motion and component recipes stop short (gap)

- **Hit:** 2 of 8 builders. 4 pieces: components 05, 06, 07 and 08.
- **Evidence:** components/08 F-001 (Energy barely changes motion); components/05 F-001 (springs are locked by standards) and F-003 (the toast recipe is only partly tokenised); components/06 F-008 (no table tokens); components/07 F-004 (`prompt-input` is "planned (tokens ready)" with no tokens) and F-005.
- **Verified:** Of 104 motion tokens, Energy 20 and Energy 82 differ in one:

  ```
  <   --ds-motion-duration-extra: 620ms;
  >   --ds-motion-duration-extra: 790ms;
  ```
- **User-visible effect:** DESIGN.md says Energy sets the motion, but an expressive brand gets no overshoot anywhere. Tables and composers are built by hand.
- **Fix:** Say in DESIGN.md which motion tokens standards lock and where personality may add spring. Add `component.table.*` and `component.prompt-input.*` tokens, and stop calling `prompt-input` "tokens ready" until they exist. Make the toast lift, scale and swipe threshold tokens.
- **Already open:** no.

### 23. Editorial and script type features (gap)

- **Hit:** 2 of 8 builders. 4 pieces: footers 01, 05 and 07; heroes 08.
- **Evidence:** footers/01 F-004 (no variable-axis token); footers/05 F-003 (no old-style figures or small caps); footers/07 F-002 (no vertical writing); heroes/08 F-003 (no fourth face role).
- **Verified:** `raw.numericStyles` toggles only tabular figures (builder evidence). There are three face roles (`build_typography`, engine.py:1645-1648).
- **User-visible effect:** Editorial and Japanese pages hand-write the details that carry them.
- **Fix:** Add `font.variation.*` and `font.feature.*` tokens (onum, smcp), and a `vertical` text style when `raw.scripts` includes Jpan.
- **Already open:** no.

### 24. `opendesigner-illustrate` rough edges (bug, confusing)

- **Hit:** 3 of 8 builders. 3 pieces: app 06, components 09, footers 04.
- **Evidence:** components/09 F-001 (`--dir` means the illustrations folder there but the state folder in the engine, so files landed in `opendesigner/`); app-screens/06 F-002 (search replaces candidates); components/09 F-002 (fetch exits 1 on success; `apply --label` leaves the ledger "(unassigned)"); footers/04 F-004 ("ask before fetching" blocks unattended builders).
- **Verified:**
  - `--dir` defaults to `opendesigner/illustrations` (illustrate.py:1582).
  - Search keeps old candidates only with an undocumented `--keep` (illustrate.py:1160 and 1600).
  - SKILL.md line 35 requires "a yes once per session".
  - Not verified: search relevance and the fetch exit code (both need the network).
- **User-visible effect:** Files land in the wrong folder and the first search's candidates are lost.
- **Fix:**
  - Rename the flag to `--illus-dir`, or accept the engine's `--dir` and append `illustrations/`.
  - Document `--keep`, or merge candidates by default.
  - Add a `--pre-approved` note for autonomous runs.
- **Already open:** no.

### 25. `opendesigner-paint` can't paint one still unattended (gap, bug)

- **Hit:** 3 of 8 builders. 4 pieces: app 03, heroes 03, 05 and 09.
- **Evidence:** heroes/03 F-004 and heroes/09 F-002 (a still needs the whole film toolchain and a yes to install); app-screens/03 F-003 (no in-app image slot); heroes/03 F-003 (the licence is not read); heroes/09 F-003 (the brand-tint family is grey).
- **Verified:**
  - SKILL.md lines 5 and 35 require Node, npm, Playwright and ffmpeg after a yes.
  - `font_decision` (paint.py:233-245) reads `fontLicence` only when `brandFace` is set, so a recorded OFL licence on `displayFace` still prints "confirm it is OFL".
  - Not verified: the brand-tint family color.
- **User-visible effect:** Every painted piece was painted by hand from the brief; the brief itself was useful.
- **Fix:**
  - In `font_decision`, read `raw.fontLicence` for any face.
  - Add a no-install still path: one HTML page with p5 from a pinned CDN, rendered by the existing `brand/tools/shot.py`.
  - Add an `in-app` slot with square and portrait sizes.
- **Already open:** no.

---

## 3. What worked well (keep these)

| Feature | Evidence |
|---|---|
| A complete, contrast-checked system in one command | Watch: "each full piece setup ... took a few seconds; build alone about 0.3 s". My repro printed "Checked 188 color pairs in every mode, 12 mode combinations and 481 tokens." Components 06-10: "I never hand-checked a status or on-accent colour." |
| Automatic on-color text, once the hex is kept | My repro with the brand not delegated: "Your brand color is on the buttons exactly, with dark text on it". Components 01-05: dark text on yellow and cyan, white on magenta and terracotta, "with no hand tuning". |
| Dials that map to real decisions | Components 06-10: Density gave control heights of 24/32/40 (dense) and 40/48/56 (airy). Roundness and Depth gave matching radius and elevation roles. App 06-10: radius 0 in 08, chunky in 07. |
| Traceable, safe changes | `set` prints what changes ("tokens: 18 values change ..." in my repro). `decisions.md` made every change traceable (watch D-0025/26; footers D-0004/05/21). Token overrides through `set <path> <DTCG>` are logged and re-validated (heroes 01-05). |
| Escape hatches that stay in the system | `type.displayReach` put 52, 95 and 169 px numbers on the scale (app 01-05). `raw.secondaryColors` plus `accentCount` gave full ramps (app 02 and 05, footers 03, 04, 07 and 08, components 04, heroes 02). `raw.scripts Jpan` added a `:lang(ja)` line-height scale (footers 07, heroes 09). `raw.darkBase black` and `Q-color-21 black` work. |
| House standards that design behavior | Components 01-05: thirteen toast rules set stacking, timing, pause, swipe and placement. "No motion on 100+ times-a-day actions" settled the palette. |
| `engine.py review` plus `od-ignore` | It caught real drift (heroes 01: 22 values; 02: 37) and `100vh` and endless loops (heroes 06-10). Watch moved 36 spacing declarations to tokens. Keep it, and fix the token mapping (finding 15). |
| The review probe (`opendesigner-review`) | App 06-10: "the most useful check": 4 real contrast failures, 9-10 px text, heading skips and an endless animation, each with the exact element. |
| Dark mode almost free on tokens | Heroes 01 and 05 rendered correctly in dark mode with no extra work. |
| Clear standard overrides | `standard override` records the person's words and names the restore command (my repro, D-0003). |
| Unknown feel words are asked about, not guessed | App 01-05: "The engine asked instead of guessing, which is right". Keep the behavior, and store the words (finding 18). |
| `opendesigner-illustrate`'s CSS-variable output and licence ledger | Components 09 tinted line art per card through `--od-illus-neutral-1`. App 06-10: "the smoothest part of the process". |
| `paint.py brief` offline | It gave nine palette families from the tokens (app 01-05) and shaped heroes 09. |
| `engine.py feedback` | 190 entries, each with a ready issue link, and nothing posted. |

---

## 4. Proposed order of work

Eight small changes, each shippable alone, in this order:

| # | Change | Where | Closes |
|---|---|---|---|
| 1 | A hex given with `--brand` is never rewritten. A delegated brand may take dark text. `keep-hex` restores the typed hex. Hue words describe the typed hex. | `cmd_sketch` (engine.py:9435), `readable_shade` (9296), `color_words` (9280), the Q-color-01 answer map (3465) | 1 |
| 2 | Preflight reads token pages: Google Fonts links, rem and em, `var()` shorthands, `--medium app|watch`, size-aware tracking, sizes not in the scale, infinite animations. | `check_html` and `read_css`, preflight.py:17, 37-121 | 2 |
| 3 | Dark-only means dark-only, and the brand stays exact in dark. | `GenCtx` (engine.py:1227), `build_palette` pin (1085), `brand_line` (9315), Q-color-16 | 5 (second half), 6 |
| 4 | Single-theme systems get through: a **should** standard warns instead of refusing, and the refusal names `init → override → sketch`. | `synthesis/standards.json` (STD-visual-details-24), the sketch refusal (engine.py:9411-9422) | 5 (first half) |
| 5 | A display set and a free display weight, documented. | `build_type_scale` (1567), `build_typography` (1614-1625), `synthesis/questionnaire.json` stage 11 | 3, part of 4 |
| 6 | One text floor, and native base sizes that hold: 12 px on web and 11 pt on native, the same in the engine and preflight; native base kept on native-only platforms; `watchos` renamed to `watch`; Q-aud-01 `large` gives a 17 px body. | `build_type_scale` (1583), `synthesis/levers.json`, engine.py:3436, preflight.py:17 | 7, part of 12 |
| 7 | Typefaces: `--text-face` and `--display-face` on sketch; the command written in stage 10 and DESIGN.md; a Google Fonts licence source; class-aware fallbacks; weights clamped to the face. | sketch argparse (engine.py:9060), `OPEN_FONTS` (1164), `face()` (1639), `build_typography` | 8, 10 |
| 8 | Neutrals that never go brown: cap the text-step chroma, warn on warm dark with a warm accent, say that `neutralBase` overrides Warmth, add `color.light.baseY`. | `build_palette` / `neutral_chroma` (engine.py:1006), `NEUTRAL_CURVE` (734), `PARAM_OVERRIDES` (2266), a validate warning | 9, part of 14 |

Next after these, in order:
1. `set` validation (finding 17; about an hour, and it hides other bugs).
2. Review token roles and rem spacing tokens (findings 15 and 16).
3. Text-over-art sampling in `probe.js` (finding 11).
4. Art palette tokens (finding 13).
5. A real watch platform (the rest of finding 12).

---

## 5. What I could not verify

- **Visual quality:** I opened 5 renders (heroes 07 and 10, components 10, footers 04, the watch board). The rest of the quality verdict rests on the builders' own rankings.
- **Network-dependent illustrate claims:** search relevance (Mönsterås arms, "house" queries), the fetch exit code and the ledger labels were not run.
- **Paint:** the `paint.py brief` "brand-tint" family color (heroes/09 F-003) was not run.
- **Review counts:** the 103, 78 and 64 findings per page are the builders' numbers; I re-ran only a 6-line sample.
- **Mobbin:** the claims about Mobbin's platforms and repeated results were not checked.
- **Code-only checks:** status colors barely following Colorfulness, the divider, inverse-accent and alpha-ramp gaps, and the near-black brand collapse were checked against the code or taken from builder evidence, not reproduced.

---

## Appendix: every feedback entry mapped to a finding

190 entries: 183 from the builders and 7 from the brand kit. "What worked" marks an entry that records a success.

| Piece (file: `brand/showcase/<piece>/opendesigner/feedback.md`) | Entry | Kind | Finding |
|---|---|---|---|
| app-screens/01-private-banking | F-001 | bug | 1 |
| app-screens/01-private-banking | F-002 | bug | 7 |
| app-screens/01-private-banking | F-003 | gap | 8 |
| app-screens/01-private-banking | F-004 | gap | 14 |
| app-screens/01-private-banking | F-005 | gap | 4 |
| app-screens/02-sleep-meditation | F-001 | confusing | 17 |
| app-screens/02-sleep-meditation | F-002 | bug | 10 |
| app-screens/02-sleep-meditation | F-003 | gap | 11 |
| app-screens/02-sleep-meditation | F-004 | idea | What worked |
| app-screens/02-sleep-meditation | F-005 | bug | 1 |
| app-screens/03-recipe-editorial | F-001 | gap | 18 |
| app-screens/03-recipe-editorial | F-002 | bug | 19 |
| app-screens/03-recipe-editorial | F-003 | gap | 25 |
| app-screens/03-recipe-editorial | F-004 | gap | 21 |
| app-screens/03-recipe-editorial | F-005 | idea | 14 |
| app-screens/03-recipe-editorial | F-006 | gap | 9 |
| app-screens/04-fitness-neon | F-001 | bug | 1 |
| app-screens/04-fitness-neon | F-002 | bug | 6 |
| app-screens/04-fitness-neon | F-003 | confusing | 15 |
| app-screens/05-travel-boarding | F-001 | gap | 4 |
| app-screens/05-travel-boarding | F-002 | bug | 4 |
| app-screens/05-travel-boarding | F-003 | confusing | 4 |
| app-screens/05-travel-boarding | F-004 | gap | 18 |
| app-screens/06-plant-care | F-001 | bug | 2 |
| app-screens/06-plant-care | F-002 | bug | 24 |
| app-screens/06-plant-care | F-003 | idea | 24 |
| app-screens/06-plant-care | F-004 | gap | 9 |
| app-screens/07-language-lesson | F-001 | bug | 20 |
| app-screens/07-language-lesson | F-002 | gap | 7 |
| app-screens/07-language-lesson | F-003 | gap | 13 |
| app-screens/08-podcast-player | F-001 | bug | 1 |
| app-screens/08-podcast-player | F-002 | gap | 8 |
| app-screens/08-podcast-player | F-003 | confusing | 5 |
| app-screens/08-podcast-player | F-004 | gap | 3 |
| app-screens/08-podcast-player | F-005 | gap | 14 |
| app-screens/09-project-workspace | F-001 | confusing | 15 |
| app-screens/09-project-workspace | F-002 | bug | 11 |
| app-screens/10-clinical-vitals | F-001 | bug | 18 |
| app-screens/10-clinical-vitals | F-002 | gap | 21 |
| components/01-pricing-glass | F-001 | bug | 1 |
| components/01-pricing-glass | F-002 | bug | 1 |
| components/01-pricing-glass | F-003 | confusing | 5 |
| components/01-pricing-glass | F-004 | bug | 5 |
| components/01-pricing-glass | F-005 | gap | 10 |
| components/01-pricing-glass | F-006 | gap | 4 |
| components/01-pricing-glass | F-007 | gap | 11 |
| components/01-pricing-glass | F-008 | bug | 15 |
| components/01-pricing-glass | F-009 | bug | 16 |
| components/01-pricing-glass | F-010 | confusing | 21 |
| components/02-command-palette | F-001 | bug | 21 |
| components/02-command-palette | F-002 | gap | 21 |
| components/02-command-palette | F-003 | bug | 15 |
| components/02-command-palette | F-004 | idea | 15 |
| components/03-date-range-picker | F-001 | bug | 7 |
| components/03-date-range-picker | F-002 | bug | 1 |
| components/03-date-range-picker | F-003 | gap | 13 |
| components/03-date-range-picker | F-004 | bug | 2 |
| components/04-upload-brutal | F-001 | bug | 1 |
| components/04-upload-brutal | F-002 | bug | 19 |
| components/04-upload-brutal | F-003 | confusing | 19 |
| components/04-upload-brutal | F-004 | gap | 20 |
| components/04-upload-brutal | F-005 | confusing | 3 |
| components/05-toast-stack | F-001 | confusing | 22 |
| components/05-toast-stack | F-002 | bug | 15 |
| components/05-toast-stack | F-003 | idea | 22 |
| components/06-data-table | F-001 | bug | 2 |
| components/06-data-table | F-002 | gap | 7 |
| components/06-data-table | F-003 | bug | 2 |
| components/06-data-table | F-004 | idea | 8 |
| components/06-data-table | F-005 | bug | 1 |
| components/06-data-table | F-006 | gap | 21 |
| components/06-data-table | F-007 | gap | 20 |
| components/06-data-table | F-008 | gap | 22 |
| components/06-data-table | F-009 | confusing | 5 |
| components/07-ai-composer | F-001 | gap | 9 |
| components/07-ai-composer | F-002 | idea | 18 |
| components/07-ai-composer | F-003 | gap | 3 |
| components/07-ai-composer | F-004 | gap | 22 |
| components/07-ai-composer | F-005 | idea | 22 |
| components/08-music-player | F-001 | gap | 22 |
| components/08-music-player | F-002 | gap | 11 |
| components/08-music-player | F-003 | bug | 1 |
| components/08-music-player | F-004 | idea | 18 |
| components/09-onboarding-stepper | F-001 | confusing | 24 |
| components/09-onboarding-stepper | F-002 | bug | 24 |
| components/09-onboarding-stepper | F-003 | idea | 24 |
| components/09-onboarding-stepper | F-004 | bug | 2 |
| components/09-onboarding-stepper | F-005 | gap | 19 |
| components/10-settings-terminal | F-001 | bug | 1 |
| components/10-settings-terminal | F-002 | gap | 21 |
| components/10-settings-terminal | F-003 | gap | 6 |
| components/10-settings-terminal | F-004 | confusing | 18 |
| components/10-settings-terminal | F-005 | idea | 21 |
| footers/01-brask-wordmark | F-001 | bug | 1 |
| footers/01-brask-wordmark | F-002 | confusing | 5 |
| footers/01-brask-wordmark | F-003 | gap | 6 |
| footers/01-brask-wordmark | F-004 | gap | 23 |
| footers/01-brask-wordmark | F-005 | bug | 2 |
| footers/01-brask-wordmark | F-006 | idea | 9 |
| footers/01-brask-wordmark | F-007 | gap | 4 |
| footers/02-keystrata-mega | F-001 | gap | 21 |
| footers/02-keystrata-mega | F-002 | bug | 15 |
| footers/02-keystrata-mega | F-003 | idea | 18 |
| footers/03-quietfield-horizon | F-001 | bug | 18 |
| footers/03-quietfield-horizon | F-002 | confusing | 7 |
| footers/03-quietfield-horizon | F-003 | gap | 13 |
| footers/04-tumbletree-meadow | F-001 | bug | 7 |
| footers/04-tumbletree-meadow | F-002 | bug | 8 |
| footers/04-tumbletree-meadow | F-003 | gap | 13 |
| footers/04-tumbletree-meadow | F-004 | confusing | 24 |
| footers/05-salt-ledger-index | F-001 | idea | 18 |
| footers/05-salt-ledger-index | F-002 | gap | 14 |
| footers/05-salt-ledger-index | F-003 | gap | 23 |
| footers/06-knurl-brutalist | F-001 | gap | 20 |
| footers/06-knurl-brutalist | F-002 | idea | 21 |
| footers/07-sasame-tea | F-001 | bug | 8 |
| footers/07-sasame-tea | F-002 | gap | 23 |
| footers/08-rallo-app | F-001 | confusing | 8 |
| footers/08-rallo-app | F-002 | bug | 18 |
| heroes/01-swiss-architecture | F-001 | bug | 1 |
| heroes/01-swiss-architecture | F-002 | gap | 14 |
| heroes/01-swiss-architecture | F-003 | gap | 8 |
| heroes/01-swiss-architecture | F-004 | bug | 16 |
| heroes/01-swiss-architecture | F-005 | bug | 15 |
| heroes/01-swiss-architecture | F-006 | gap | 5 |
| heroes/01-swiss-architecture | F-007 | bug | 2 |
| heroes/01-swiss-architecture | F-008 | bug | 2 |
| heroes/02-luminous-devtool | F-001 | bug | 1 |
| heroes/02-luminous-devtool | F-002 | bug | 5 |
| heroes/02-luminous-devtool | F-003 | gap | 20 |
| heroes/02-luminous-devtool | F-004 | confusing | 17 |
| heroes/02-luminous-devtool | F-005 | bug | 15 |
| heroes/02-luminous-devtool | F-006 | bug | 2 |
| heroes/03-organic-wellness | F-001 | bug | 19 |
| heroes/03-organic-wellness | F-002 | gap | 13 |
| heroes/03-organic-wellness | F-003 | bug | 25 |
| heroes/03-organic-wellness | F-004 | gap | 25 |
| heroes/03-organic-wellness | F-005 | gap | 18 |
| heroes/04-neobrutalist-festival | F-001 | bug | 17 |
| heroes/04-neobrutalist-festival | F-002 | gap | 20 |
| heroes/04-neobrutalist-festival | F-003 | gap | 2 |
| heroes/04-neobrutalist-festival | F-004 | bug | 15 |
| heroes/04-neobrutalist-festival | F-005 | confusing | 7 |
| heroes/05-luxury-maison | F-001 | gap | 13 |
| heroes/05-luxury-maison | F-002 | confusing | 7 |
| heroes/05-luxury-maison | F-003 | gap | 9 |
| heroes/06-playful-fintech | F-001 | bug | 5 |
| heroes/06-playful-fintech | F-002 | gap | 8 |
| heroes/06-playful-fintech | F-003 | confusing | 17 |
| heroes/06-playful-fintech | F-004 | gap | 8 |
| heroes/06-playful-fintech | F-005 | bug | 10 |
| heroes/06-playful-fintech | F-006 | gap | 3 |
| heroes/06-playful-fintech | F-007 | gap | 13 |
| heroes/06-playful-fintech | F-008 | bug | 15 |
| heroes/06-playful-fintech | F-009 | idea | 20 |
| heroes/06-playful-fintech | F-010 | bug | 2 |
| heroes/07-climate-observatory | F-001 | bug | 18 |
| heroes/07-climate-observatory | F-002 | gap | 14 |
| heroes/07-climate-observatory | F-003 | confusing | 6 |
| heroes/07-climate-observatory | F-004 | bug | 5 |
| heroes/07-climate-observatory | F-005 | gap | 3 |
| heroes/07-climate-observatory | F-006 | bug | 16 |
| heroes/08-y2k-retrofuture | F-001 | bug | 1 |
| heroes/08-y2k-retrofuture | F-002 | gap | 20 |
| heroes/08-y2k-retrofuture | F-003 | idea | 23 |
| heroes/08-y2k-retrofuture | F-004 | gap | 4 |
| heroes/08-y2k-retrofuture | F-005 | bug | 2 |
| heroes/08-y2k-retrofuture | F-006 | bug | 8 |
| heroes/09-japanese-ceramics | F-001 | bug | 13 |
| heroes/09-japanese-ceramics | F-002 | gap | 25 |
| heroes/09-japanese-ceramics | F-003 | bug | 25 |
| heroes/10-enterprise-health | F-001 | bug | 17 |
| heroes/10-enterprise-health | F-002 | confusing | 7 |
| watch/01-ridgeline-trail | F-001 | gap | 12 |
| watch/01-ridgeline-trail | F-002 | bug | 6 |
| watch/01-ridgeline-trail | F-003 | bug | 1 |
| watch/02-thrum-heart | F-001 | bug | 5 |
| watch/02-thrum-heart | F-002 | confusing | 16 |
| watch/03-tidemark-face | F-001 | gap | 4 |
| watch/04-headway-transit | F-001 | idea | 12 |
| watch/05-nook-home | F-001 | gap | 9 |
| watch/07-leeward-sail | F-001 | gap | 13 |
| watch/08-onething-focus | F-001 | bug | 2 |
| brand kit (`brand/opendesigner/feedback.md`) | F-001 | bug | 17 |
| brand kit (`brand/opendesigner/feedback.md`) | F-002 | gap | 1 |
| brand kit (`brand/opendesigner/feedback.md`) | F-003 | gap | 3 |
| brand kit (`brand/opendesigner/feedback.md`) | F-004 | gap | 3 |
| brand kit (`brand/opendesigner/feedback.md`) | F-005 | bug | 4 |
| brand kit (`brand/opendesigner/feedback.md`) | F-006 | gap | 3 |
| brand kit (`brand/opendesigner/feedback.md`) | F-007 | idea | 4 |
