# L23: Defaults for dense B2B work tools

**Lane overview.** OpenDesigner's best-paying customers are B2B and enterprise teams (owner, 2026-10-14). A Mobbin study of premium B2B product UI [S-L23-001] and three showcase builds made with the engine [S-L23-002] found that when a person describes a dense tool used all day, the engine's defaults drift away from what top-tier products do. Plain feel words such as "professional, minimal" or "quiet, trustworthy" pushed corners to 0-2 px, labels to the body weight, the accent to grey and a shadow onto static cards. Rows, separators and tabular digits were missing, so builders invented them.

These cards back the `work-tool` profile in `synthesis/levers.json` (`profiles`) and two token families added for every system. The profile is a set of defaults. It fills only what the person has not answered, set or locked, and the engine records each value it fills as `auto_default` with a reason.

Measured values from product screens are about ±15% (previews scaled from about 768 px). They set a default only where a Tier A system or an existing card points the same way.

### DC-L23-01: The dense work-tool profile
- **Block path:** Builder > Defaults > Profiles (levers.json `profiles.work-tool`)
- **Questions the designer answers:** Is this a tool people work in all day, in screens full of data (Q-aud-01 = dense)? Which of the profile's defaults do you want to keep, and which do you want to decide yourself?
- **Options:**
  - **No profile (before):** dense only changed spacing, control heights and body size. Feel words then set everything else, and "professional, minimal" gave 2 px controls, labels at 400, a grey accent and a faint shadow on static cards [S-L23-001, section 4.1]. Three builds with "quiet, trustworthy" and similar words got 0 px corners, a shadow on static cards and labels at 400. Each needed four or five manual `set` calls [S-L23-002].
  - **A profile for what is left open (chosen):** when Q-aud-01 = dense, four defaults apply unless the person decided them: corners (DC-L23-02), weights (DC-L23-03), one colored accent (DC-L23-04) and flat static surfaces (DC-L23-05). Rows (DC-L23-06), separators (DC-L23-05) and tabular digits (DC-L23-07) are now generated for every system, so the profile does not need them.
  - **Asking one more question each time:** P5 in the study proposes asking for an accent color when there is none [S-L23-001, section 4.2]. It is kept as an option for the interview, but the default must already be usable without it.
- **Visual effect:** the system starts in the same family as Linear, Stripe, Vercel, Attio and Mercury [S-L23-003, S-L23-004, S-L23-005, S-L23-006, S-L23-007]: small even corners, a medium weight for labels and headers, one accent for what is selected or focused, and hairlines instead of shadows.
- **Depends on (upstream):** Q-aud-01 (the trigger). Q-aud-02 = work is not a trigger on its own, because it is the default for everyone [S-L23-001, P1].
- **Affects (downstream):** dials.roundness (a floor), type.weightCount (a floor), color.accentChroma.hct (a floor when there is no brand color), elevation.raised and, for the borders-only model, elevation.floating and elevation.overlay.
- **Token encoding:** none of its own. The profile changes existing params. `opendesigner.meta.json` records `profile.applied[]`, with `set_by: auto_default`, a reason and the evidence for each item, and `profile.skipped{}`, which says why each skipped item was skipped. `decisions.md` gets one `defaults.work-tool` entry (auto_default) whenever the applied set changes.
- **Platform notes:** the same everywhere. Corners and weights reach every export.
- **Accessibility constraints:** none are loosened. The accent floor raises chroma only. The ramp solver still holds every text and boundary contrast.
- **Default + heuristic:** An item is skipped when its question is answered, its dial or value is set, overridden or locked, a chosen style direction (Q-dir-01) sets its dial, or a brand color decides it. A person who confirms a value records it with `--set-by confirmed_default`, and then it is theirs. The trigger and the item list are in levers.json, so the profile can be changed without touching engine code [inferred].
- **Evidence:** [S-L23-001, S-L23-002, S-L23-003, S-L23-004, S-L23-005, S-L23-006, S-L23-007]

### DC-L23-02: Corners in dense work tools
- **Block path:** Foundations > Shape > Radius scale and default
- **Questions the designer answers:** How round should controls, panels and dialogs be in a tool used all day?
- **Options:**
  - **0-2 px:** a deliberate brand statement (GOV.UK, Carbon v11 buttons; Q-shape-01 `square`). The study lists "brutal 0 px everywhere" among the average looks of B2B tools [S-L23-001, section 3].
  - **About 6 px controls, 8 px panels, 10-12 px overlays:** Linear, Vercel, Stripe and PlanetScale [S-L23-003, S-L23-005, S-L23-004, S-L23-008; S-L23-015]. It is also the median control radius of 23 benchmarked systems (16 of 23 at 4-8 px, median 6, DC-L09-01) and Q-shape-01's own default.
  - **Pill or 16 px cards:** read as consumer and waste room in short dense controls [S-L23-001, section 3].
- **Visual effect:** 6 px reads precise but not harsh. 0-2 px reads official or engineered.
- **Depends on (upstream):** Q-aud-01, the Roundness dial, Q-shape-01, Q-dir-01.
- **Affects (downstream):** radius.control, control-sm, container, overlay, focus and nested.
- **Token encoding:** a floor of 38 on the Roundness dial (the lower edge of the 6 px band, 38-47) gives control 6, container 8 and overlay 12 through the existing radius formula.
- **Platform notes:** the same on web, iOS and Android exports.
- **Accessibility constraints:** none.
- **Default + heuristic:** for a dense work tool that has not chosen its corners, use 6 / 8 / 12. Keep 0-2 px only when the person chooses it. The floor value is [inferred]. Small badges stay on radius.detail (2 px at a 6 px control). The study saw about 4 px badges, which is not built yet.
- **Evidence:** [S-L23-001, S-L23-003, S-L23-004, S-L23-005, S-L23-008, S-L23-015; DC-L09-01]

### DC-L23-03: Three weights, with labels at 500
- **Block path:** Foundations > Typography > Metrics > Weights
- **Questions the designer answers:** How many weights, and what weight do labels, column headers and row titles use?
- **Options:**
  - **Two weights (400 / 600):** what low Expression gave (type.weightCount band 0-33). Labels, headers and row titles then have no step between body and heading [S-L23-001, section 4.1].
  - **Three weights (400 / 500 / 600):** column headers are "12-13 px, sentence case, medium weight" (Stripe, Attio, Mercury), and KPI values are 500-600 [S-L23-001, sections 2.1, 2.2; S-L23-004, S-L23-006, S-L23-007, S-L23-015]. Q-type-12's default is already three weights; Material uses 400/500/700 and Atlassian Regular, Medium and Bold (Q-type-12, DC-L02-15).
- **Visual effect:** headers and row titles stand out without color or size, which keeps the type small and calm.
- **Depends on (upstream):** Expression, Energy (heading weight), Q-type-12.
- **Affects (downstream):** font.weight.label, every label.* and title.* style, icon stroke (stroke follows label weight).
- **Token encoding:** a floor of 3 on type.weightCount. The engine then sets label to 500, and heading stays at the Energy band (600 at low Energy).
- **Platform notes:** system fonts carry 500 on every platform. A brand face without a 500 cut needs one, or Q-type-12 = two.
- **Accessibility constraints:** none.
- **Default + heuristic:** three weights in a dense tool unless Q-type-12 is answered. At most three weights per screen (study P11b).
- **Evidence:** [S-L23-001, S-L23-004, S-L23-006, S-L23-007, S-L23-015; DC-L02-15]

### DC-L23-04: One colored accent for selection, links and focus
- **Block path:** Foundations > Color > Accent roles
- **Questions the designer answers:** With no brand color yet, what color marks selection, links and focus? May the primary button stay near-black?
- **Options:**
  - **Grey (before):** with no brand color, "minimal" and "serious" pushed Colorfulness to 0. Links, selection and the focus ring were then grey text, #575757 and #757575 [S-L23-001, section 4.1].
  - **Near-black primary plus one blue for selection, links and focus:** Vercel's black primary with a blue "Current" and check marks [S-L23-005]. Every top-tier product in the study has a chromatic selection or focus color [S-L23-001, signal 1 and P5]. With a brand color, a person gets this by typing an ink as `raw.primaryActionColor`. It used to turn periwinkle: #17181c became #5f6dcc, because the action ramp kept only the seed's hue and took the dial's chroma [S-L23-016]. Now the action ramp keeps the seed's own chroma. An ink, meaning a seed below HCT chroma 22 (the top of the Colorfulness dial's neutral band), stays exact in light mode, and its hover and pressed states stay ink. In dark mode it inverts to near-white with dark text, as the monochrome scheme's ink does [inferred threshold].
  - **One chromatic accent everywhere, the primary included:** what a Colorfulness of 36 or more gives. With a brand color, the brand floor already does this (levers macroRules.brandFloor).
- **Visual effect:** selected rows, links and focus read at a glance, and the rest of the screen stays grey.
- **Depends on (upstream):** brand color, Colorfulness, Q-color-03, Q-dir-01.
- **Affects (downstream):** color.text.link, text.accent, border.focus, border.accent, bg.accent.*, icon.accent. The primary action keeps the neutral ink of a monochrome scheme.
- **Token encoding:** a floor on color.accentChroma.hct at 48, Material's Expressive anchor (S-L01-010), on the placeholder hue 255. It is used only when there is no brand color. It gives light-mode steps 3 #e2edfa, 9 #3d77bf and 11 #295892.
- **Platform notes:** the same everywhere.
- **Accessibility constraints:** the solver keeps link text at 4.5:1 or more and the focus ring at 3:1 or more on every surface. The person is told the blue is a stand-in until a brand color is given.
- **Default + heuristic:** never ship grey for selection, links and focus. Use the stand-in blue until there is a brand color. This is not a brand hue: it is the same placeholder the engine already uses at Colorfulness 11 and up. The floor value is [inferred]. Command palettes may still highlight the active row in grey [S-L23-001, section 2.7].
- **Evidence:** [S-L23-001, S-L23-005; S-L01-010]

### DC-L23-05: Hairlines for static surfaces, shadows for floating ones
- **Block path:** Foundations > Depth > Elevation; Foundations > Color > Borders
- **Questions the designer answers:** How do cards and panels separate from the page? What lifts menus, dialogs and toasts? How heavy are the lines between table rows?
- **Options:**
  - **A faint shadow on static cards (before):** the ring+faint-shadow model gave elevation.raised a `0 1px 2px` shadow [S-L23-001, section 4.1].
  - **Borders only for everything (before, at depth 15 or less):** also removed the shadow from menus, popovers, the bulk bar, toasts and dialogs, so all three builds wrote their own [S-L23-002].
  - **Hairlines and one tonal step for static surfaces, shadows for floating ones (chosen):** Stripe's widgets have no chrome until edit mode [S-L23-010]. Linear and Mercury cards use hairlines [S-L23-003, S-L23-007]. Shadows appear on menus, popovers, dialogs, toasts and the floating bulk bar [S-L23-001, signal 5; S-L23-006]. This is also Q-depth-01's prose default and DC-L04-10.
- **Visual effect:** flat, quiet pages where only what floats casts a shadow.
- **Depends on (upstream):** Depth, Q-depth-01, Q-dir-01, Warmth (border softness).
- **Affects (downstream):** elevation.raised, elevation.floating and elevation.overlay (borders model only), color.border.separator.
- **Token encoding:** under the profile, elevation.raised is a 1px ring with no blur in the ring, shadow-ladder and materials models. In the borders model, floating and overlay get a ring plus the two-layer shadow. For every system there is a new `color.border.separator`: neutral step 4 in light mode and step 5 in dark mode, two steps under border.subtle in light and one in dark, following border softness. The builds chose step 4 by eye because border.subtle was too heavy for 18 rules [S-L23-002]. The study estimates row hairlines at about 1.2-1.3:1 [S-L23-001, P8; inferred hex].
- **Platform notes:** the same everywhere. Dark mode still lifts surfaces by lightness.
- **Accessibility constraints:** separators are decorative, so they are never the only cue. Inputs keep border.input at 3:1 (WCAG 1.4.11).
- **Default + heuristic:** never a shadow on an in-flow static surface in a dense tool, and always one on a floating layer. The separator step is [inferred].
- **Evidence:** [S-L23-001, S-L23-002, S-L23-003, S-L23-006, S-L23-007, S-L23-010; DC-L04-10]

### DC-L23-06: Row heights for lists and tables
- **Block path:** Foundations > Space > Sizing > Row heights
- **Questions the designer answers:** How tall is a table row, dense and roomy, and a row with two lines?
- **Options:**
  - **No token (before):** builders invented 36, 56 and 34 px [S-L23-002].
  - **Carbon's five sizes:** 24, 32, 40, 48 and 64 px, with extra large "only recommended if your data is expected to have two lines of content in a single row" [S-L23-014; S-L08-092].
  - **Premium B2B tables:** about 34-36 px dense (Stripe, Attio) [S-L23-004, S-L23-006, S-L23-015], 38-42 px for issue lists (Snowflake, Linear) [S-L23-009, S-L23-003], about 48 px for comfortable finance lists (Mercury) [S-L23-007], and about 56-78 px for two-line rows (Vercel, PlanetScale) [S-L23-005, S-L23-008].
- **Visual effect:** rows match the controls inside them, and dense tables stop looking hand-made.
- **Depends on (upstream):** density mode, control heights (DC-L03-07).
- **Affects (downstream):** tables, lists, menus, trees and key-value rows.
- **Token encoding:** `size.row.sm` / `md` / `lg` / `two-line` in each `semantic.density.<mode>.tokens.json`, next to `size.control.*`. The value is the density's default control height plus 4 / 8 / 16 / 32 px: 36 / 40 / 48 / 64 at compact (32 px controls), 44 / 48 / 56 / 72 at comfortable, and 52 / 56 / 64 / 80 at spacious. CSS `--ds-size-row-md`, Tailwind `spacing-row-md`, Swift `sizeRowMd`, Compose `sizeRowMd`.
- **Platform notes:** touch rows still need hit areas of size.target.min. A row may be shorter than its hit area only when the row itself is not the target.
- **Accessibility constraints:** targets follow size.target.min, never the row height.
- **Default + heuristic:** md for most tables, sm for dense data grids, two-line when a cell has a title and a meta line. The offsets are [inferred]: they fit Carbon's sizes at 32 px controls (sm is 4 px over Carbon's 32, toward the study's 34-36) and the study's ranges.
- **Evidence:** [S-L23-002, S-L23-003, S-L23-004, S-L23-005, S-L23-006, S-L23-007, S-L23-008, S-L23-009, S-L23-014, S-L23-015; S-L08-092]

### DC-L23-07: Tabular digits by default
- **Block path:** Foundations > Typography > Numeric styles
- **Questions the designer answers:** Do numbers in tables and live values use digits of one width?
- **Options:**
  - **Only on request (before):** `text.numeric.*` appeared only after Q-type-06 `numeric-face` or Q-layout-03 `data`. That contradicted the house standard STD-visual-details-02, a must, and Q-type-06's own default [S-L23-001, section 4.1].
  - **On for every system (chosen):** every top-tier money table aligns its numbers (Mercury, Cofounder, Stripe, Vercel) [S-L23-007, S-L23-011, S-L23-012, S-L23-013]. DC-L02-05 says the same.
- **Visual effect:** columns of amounts line up, and live numbers stop jittering.
- **Depends on (upstream):** none. `raw.numericStyles` can still be set to false.
- **Affects (downstream):** text.numeric.md and text.numeric.lg, the Tailwind `tabular` utility, and the CSS `font-variant-numeric` declaration.
- **Token encoding:** levers raw `numericStyles` defaults to true. The numeric style's note says to right-align numeric columns. A muted currency code and muted cents are not tokens yet [S-L23-002].
- **Platform notes:** the Swift export maps numeric.md to the Dynamic Type body style and numeric.lg to title2. Equal-width digits come from the font's tabular figures.
- **Accessibility constraints:** none.
- **Default + heuristic:** tabular digits in tables, ledgers, timers and counters, never in running text.
- **Evidence:** [S-L23-001, S-L23-002, S-L23-007, S-L23-011, S-L23-012, S-L23-013; DC-L02-05; STD-visual-details-02]

## Open questions / gaps
- A badge radius of about 4 px (the study's value) is not built: radius.detail stays 2 px at a 6 px control, because the LEVERS B9 formula's 3 px rounds down.
- Not built: a status style (P6: dot plus word, or a tinted badge with an icon), a badge height, a numeric cell with a muted currency code and cents, a role-anchored type scale for work tools (P9), quiet chart defaults (P7) and review checks (P11).
- Q-aud-01 `large` promises body 17px or more, but on the web the engine gives 16 (density 15 falls in the 11-33 band). This was not changed here.
- Feel words the study asked for (precise, efficient, dense, quiet) are still unknown to the engine. The profile makes them matter less in dense tools, but the words still are not mapped.
- Existing systems keep `raw.numericStyles: false` in their state.json until someone sets it. Only new systems get the new default.

## Confidence
- **Confirmed:** Carbon's row heights and its two-line guidance [S-L23-014]; a spot check of one Stripe table at about 35 px rows and medium headers [S-L23-015]; the engine's before and after values, which are reproduced in this lane's engine tests; the builds' manual fixes [S-L23-002].
- **Measured by the study, about ±15%:** every other product value in these cards.
- **Inferred:** the roundness floor (38), the accent floor (HCT 48), the row offsets (+4 / +8 / +16 / +32), the separator step, and Q-aud-02 = work not being a trigger.
