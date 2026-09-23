# L08: Component catalog (64 canonical components)

Lane: L08 (Components & Patterns). Companion to `research/L08-components-patterns.md` (Decision Cards, taxonomy, patterns, templates, docs model).
Written 2026-09-23. Every claim is tagged with a source id from `traces/L08-trace.md` or marked [inferred].

## How this catalog was built
- **Canonical names and aliases** start from The Component Gallery (60 components, 95 design systems, 2,671 examples on its home page; the components index sums to 2,310, so the two pages drift) [S-L08-001] [S-L08-002].
- **Benchmark set (10 systems):** Material 3 (36 components) including the May 2025 M3 Expressive additions [S-L08-008], Apple HIG (64 components in 8 categories) [S-L08-017], Fluent 2 web (47) [S-L08-010], Carbon (41, page updated 09 Sep 2026) [S-L08-009], Polaris web components (50; Polaris React is deprecated and archived) [S-L08-022] [S-L08-024], Atlassian (59 components plus 13 primitives) [S-L08-011], Primer (62) [S-L08-012], Spectrum 2 via React Spectrum S2 (71 nav entries, 68 excluding Icons, Illustrations and Provider; v1.0 stable 16 Dec 2025) [S-L08-015] [S-L08-027], Radix Primitives (30 plus 5 utilities) [S-L08-021], shadcn/ui (64; Base UI became its default primitive layer in July 2026) [S-L08-018] [S-L08-020].
- **Coverage marks:** ● = the system ships a dedicated, documented component. ◐ = the system covers it as a variant, mode, API or guideline of another component (for example, M3 toggle buttons are a configuration of Button). · = absent from the system's component index. Counts come from a script over these lists, so they are reproducible; system sizes were re-counted from the captured lists during the verification pass [inferred: the mark per cell is my classification of the listed names].
- **Categories** follow the brief: action, input, selection, navigation, feedback, overlay, containment, data display, media, layout. M3's own categories are action, containment, communication, navigation, selection and text input [S-L08-008]; Atlassian and Polaris use their own groupings [S-L08-011] [S-L08-022].
- **What "foundations consumed" means:** the token families a component reads. This is the edge list the decision graph needs: change the foundation and every component listed here changes.

### Reading the counts
- 10 of 10: Switch, Progress bar, Dialog, Menu.
- 9 of 10: Button, Text field, Select, Checkbox, Tabs, Tooltip, Popover, Spinner.
- Only one system ships a dedicated component: FAB, Split button and Navigation rail (all M3; split buttons also appear as variants in Fluent, Carbon and shadcn), Command palette (shadcn). These are platform or product-type specific.
- Radix is deliberately small (behavior primitives only), and HIG names are platform controls, so both depress counts for web-only widgets such as Breadcrumbs and Pagination [inferred].

## Coverage matrix
Systems: M3 = Material 3, HIG = Apple Human Interface Guidelines, Flu = Fluent 2, Crb = Carbon, Pol = Polaris web components, Atl = Atlassian, Pri = Primer, S2 = Spectrum 2, Rdx = Radix Primitives, shd = shadcn/ui.

| ID | Canonical component | Category | M3 | HIG | Flu | Crb | Pol | Atl | Pri | S2 | Rdx | shd | Dedicated (+variant) of 10 | component.gallery examples |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C01 | Button | action | ● | ● | ● | ● | ● | ● | ● | ● | · | ● | 9 | 118 |
| C02 | Icon button | action | ● | ◐ | ◐ | ◐ | ◐ | ◐ | ● | ◐ | · | ◐ | 2 (+7) | n/a |
| C03 | Floating action button (FAB) | action | ● | · | · | · | · | · | · | · | · | · | 1 | n/a |
| C04 | Split button | action | ● | · | ◐ | ◐ | · | · | · | · | · | ◐ | 1 (+3) | n/a |
| C05 | Button group | action | ● | · | · | ◐ | ● | · | ● | ● | · | ● | 5 (+1) | 35 |
| C06 | Toggle button | action | ◐ | ◐ | ◐ | · | · | ◐ | · | ● | ● | ● | 3 (+4) | n/a |
| C07 | Segmented control / toggle group | selection | ● | ● | · | ● | · | · | ● | ● | ● | ● | 7 | 28 |
| C08 | Toolbar / action bar | action | ● | ● | ● | ◐ | · | · | ● | ● | ● | ◐ | 6 (+2) | n/a |
| C09 | Link | navigation | · | · | ● | ● | ● | ● | ● | ● | · | ◐ | 6 (+1) | 64 |
| C10 | Text field / input | input | ● | ● | ● | ● | ● | ● | ● | ● | ◐ | ● | 9 (+1) | 72 |
| C11 | Textarea | input | ◐ | ◐ | ● | ◐ | ● | ● | ● | ● | · | ● | 6 (+3) | 52 |
| C12 | Number field / stepper | input | · | ● | ● | ● | ● | · | · | ● | · | · | 5 | 20 |
| C13 | Search field | input | ● | ● | ● | ● | ● | ◐ | ◐ | ● | · | ◐ | 6 (+3) | 30 |
| C14 | Select (single-choice dropdown) | input | ◐ | ● | ● | ● | ● | ● | ● | ● | ● | ● | 9 (+1) | 82 |
| C15 | Combobox / autocomplete | input | ◐ | ● | ● | ◐ | · | ◐ | ● | ● | · | ● | 5 (+3) | 37 |
| C16 | Multi-select / token field | input | ◐ | ● | ● | ● | · | ◐ | ● | ◐ | · | ◐ | 4 (+4) | n/a |
| C17 | Date & time picker / calendar | input | ● | ● | · | ● | ● | ● | · | ● | · | ● | 7 | 44 |
| C18 | File upload / drop zone | input | · | ◐ | · | ● | ● | · | · | ● | · | · | 3 (+1) | 32 |
| C19 | Color picker | input | · | ● | · | · | ● | · | · | ● | · | · | 3 | 18 |
| C20 | One-time code (OTP) input | input | · | ◐ | · | · | · | · | · | · | ● | ● | 2 (+1) | n/a |
| C21 | Form field (label, help, error) / form | input | ◐ | ◐ | ● | ● | ◐ | ● | ● | ● | ● | ● | 7 (+3) | 21 |
| C22 | Rating | input | · | ● | ● | · | · | · | · | · | · | · | 2 | 19 |
| C23 | Checkbox | selection | ● | ◐ | ● | ● | ● | ● | ● | ● | ● | ● | 9 (+1) | 84 |
| C24 | Radio group | selection | ● | ◐ | ● | ● | ◐ | ● | ● | ● | ● | ● | 8 (+2) | 85 |
| C25 | Switch | selection | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | 10 | 60 |
| C26 | Slider | selection | ● | ● | ● | ● | · | ● | · | ● | ● | ● | 8 | 38 |
| C27 | Chip / tag | selection | ● | ◐ | ● | ● | ● | ● | ◐ | ● | · | ◐ | 6 (+3) | n/a |
| C28 | Tabs | navigation | ● | ● | ● | ● | · | ● | ● | ● | ● | ● | 9 | 80 |
| C29 | Breadcrumbs | navigation | · | ◐ | ● | ● | · | ● | ● | ● | · | ● | 6 (+1) | 55 |
| C30 | Pagination | navigation | · | ◐ | · | ● | ◐ | ● | ● | · | · | ● | 4 (+2) | 48 |
| C31 | Navigation bar (bottom tab bar) | navigation | ● | ● | · | · | · | · | · | · | · | · | 2 | n/a |
| C32 | Navigation rail | navigation | ● | ◐ | · | · | · | · | · | · | · | · | 1 (+1) | n/a |
| C33 | Side navigation / sidebar | navigation | ● | ● | ● | ● | · | ● | ● | ● | ◐ | ● | 8 (+1) | 62 |
| C34 | App bar / header / page header | navigation | ● | ● | · | ● | ◐ | ● | ● | · | ◐ | ◐ | 5 (+3) | 38 |
| C35 | Tree view | navigation | · | ● | ● | ● | · | ◐ | ● | ● | · | · | 5 (+1) | 14 |
| C36 | Steps / progress tracker | navigation | · | · | · | ● | · | ● | ◐ | · | · | · | 2 (+1) | 38 |
| C37 | Alert / inline message / banner | feedback | · | · | ● | ● | ● | ● | ● | ● | · | ● | 7 | 108 |
| C38 | Toast / snackbar / flag | feedback | ● | · | ● | ◐ | · | ● | · | ● | ● | ● | 6 (+1) | 41 |
| C39 | Progress bar / meter | feedback | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | 10 | 40 |
| C40 | Spinner / loading indicator | feedback | ● | ● | ● | ● | ● | ● | ● | ● | · | ● | 9 | 66 |
| C41 | Skeleton | feedback | · | ◐ | ● | ◐ | · | ● | ● | ● | · | ● | 5 (+2) | 30 |
| C42 | Empty state | feedback | · | · | · | ◐ | ● | ● | ● | ● | · | ● | 5 (+1) | 16 |
| C43 | Badge / status label | feedback | ● | ◐ | ● | ◐ | ● | ● | ● | ● | · | ● | 7 (+2) | 123 |
| C44 | AI indicator & conversation components | feedback | · | · | · | ● | · | ◐ | · | ◐ | · | ● | 2 (+2) | n/a |
| C45 | Tooltip / toggletip | overlay | ● | ◐ | ● | ● | ● | ● | ● | ● | ● | ● | 9 (+1) | 74 |
| C46 | Popover / hover card | overlay | ◐ | ● | ● | ● | ● | ● | ● | ● | ● | ● | 9 (+1) | 50 |
| C47 | Dialog / modal | overlay | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | 10 | 82 |
| C48 | Confirmation / alert dialog | overlay | ◐ | ● | ◐ | ◐ | ◐ | ◐ | ● | ◐ | ● | ● | 4 (+6) | n/a |
| C49 | Sheet / drawer / side panel | overlay | ● | ● | ● | · | · | ● | ◐ | · | ◐ | ● | 5 (+2) | 38 |
| C50 | Menu (dropdown, context, menubar) | overlay | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | 10 | 49 |
| C51 | Command palette | overlay | · | · | · | · | · | · | · | · | · | ● | 1 | n/a |
| C52 | Card / tile | containment | ● | ◐ | ● | ● | ◐ | ◐ | ● | ● | · | ● | 6 (+3) | 77 |
| C53 | Accordion / disclosure | containment | · | ● | ● | ● | · | · | ● | ● | ● | ● | 7 | 101 |
| C54 | Divider / separator | containment | ● | · | ● | · | ● | · | · | ● | ● | ● | 6 | 34 |
| C55 | Carousel | containment | ● | ◐ | ● | · | · | · | · | · | · | ● | 3 (+1) | 22 |
| C56 | List / list item | data display | ● | ● | ● | ● | ● | ◐ | ● | ● | · | ● | 8 (+1) | 67 |
| C57 | Table / data table | data display | · | ● | ◐ | ● | ● | ● | ● | ● | · | ● | 7 (+1) | 73 |
| C58 | Avatar / avatar group | data display | · | · | ● | · | ● | ● | ● | ● | ● | ● | 7 | 38 |
| C59 | Text & heading (typography components) | data display | · | ◐ | ● | · | ● | ● | ● | · | · | ● | 5 (+1) | 29 |
| C60 | Icon | media | ◐ | ◐ | ● | ◐ | ● | ● | ◐ | ● | ◐ | · | 4 (+5) | 45 |
| C61 | Image / thumbnail | media | · | ● | ● | · | ● | ● | · | ● | ◐ | ◐ | 5 (+2) | 29 |
| C62 | Layout primitives (box, stack, grid) | layout | · | · | · | ◐ | ● | ● | ● | · | · | ◐ | 3 (+2) | 10 |
| C63 | Page layout / app shell | layout | ◐ | ● | · | ● | ● | ● | ● | · | · | ◐ | 5 (+2) | n/a |
| C64 | Accessibility utilities (visually hidden, portal, slot) | layout | · | · | · | · | · | ● | · | · | ● | ◐ | 2 (+1) | 11 |

## Catalog entries
Conventions for every entry. **Names** lists what each system calls it; these come from the component indexes [S-L08-008] [S-L08-009] [S-L08-010] [S-L08-011] [S-L08-012] [S-L08-015] [S-L08-017] [S-L08-018] [S-L08-021] [S-L08-022] and are not re-cited per line. **States** uses the shared vocabulary: enabled, hover, focus-visible, pressed, selected, disabled, loading, error, read-only, dragged. M3 defines enabled, disabled, hover, focused, pressed and dragged as its interaction states, and says disabled states need not meet contrast and cannot be focused [S-L08-095]. **APG** = the W3C ARIA Authoring Practices pattern [S-L08-041]. **Native** = SwiftUI / UIKit (from HIG developer links [S-L08-103]) and Jetpack Compose Material 3 (from androidx source [S-L08-105]). **Consumes** = foundation token families.

### Action

#### C01 Button (action) | 9 of 10 | component.gallery 118
- **Names:** M3 Buttons; HIG Buttons; Fluent Button; Carbon Button; Polaris `s-button`; Atlassian Button; Primer Button; S2 Button (plus ActionButton for low-emphasis tool actions); shadcn Button. Radix has no button primitive.
- **Anatomy:** container, label, optional icon, focus indicator; loading spinner replaces or joins the label. M3: container, label text, optional icon [S-L08-034]. Carbon: label, container, optional icon; ghost has no container [S-L08-061]. Atlassian: label, selectable area, optional icon [S-L08-085].
- **Variants (hierarchy):** M3 five color styles, elevated, filled (default), tonal, outlined, text, plus default vs toggle behavior [S-L08-033]. Carbon primary, secondary, tertiary, ghost, danger (danger comes in primary, tertiary, ghost styles) [S-L08-061]. Atlassian default, primary, subtle, warning, danger, discovery, Rovo [S-L08-063]. Primer primary, default, invisible, danger, link [S-L08-064]. Fluent appearances include primary plus outline, subtle and transparent for minor actions, and types button, split, menu, compound [S-L08-066]. S2 variants accent, primary, secondary, negative, premium, genai, with fillStyle fill or outline [S-L08-067]. Polaris variant auto, primary, secondary, tertiary with tone critical, auto, neutral [S-L08-068]. shadcn default, secondary, outline, ghost, destructive, link [S-L08-065]. HIG uses roles, not visual variants: normal, primary, cancel, destructive [S-L08-039].
- **Sizes:** M3 XS 32, S 40 (default), M 56, L 96, XL 136 dp heights, icons 20/20/24/32/40 dp [S-L08-102] [S-L08-033]. Carbon XS 24, S 32, M 40, L 48 (productive and expressive), XL 64, 2XL 80 px [S-L08-062]. Primer small, medium, large [S-L08-064]. S2 S, M, L, XL [S-L08-067]. Atlassian default and compact spacing [S-L08-063]. shadcn xs, sm, default, lg plus icon sizes [S-L08-065].
- **States:** enabled, hover, focus-visible, pressed, disabled, loading; selected for toggles. Carbon specifies a token per state (hover, focus border + inset, active, disabled) [S-L08-062]. Primer adds "inactive" (looks disabled but stays interactive) and discourages disabled [S-L08-064]. S2 isPending keeps focus and shows a spinner after 1 s [S-L08-067].
- **Key props:** variant/appearance, size, iconStart/iconEnd (Atlassian iconBefore/iconAfter, Primer leadingVisual/trailingVisual/trailingAction), loading/isPending, disabled or inactive, fullWidth (shouldFitContainer, block, inlineSize), type, href (renders as link), command/commandFor (Polaris) [S-L08-063] [S-L08-064] [S-L08-068].
- **APG:** Button. Enter and Space activate; toggle buttons expose aria-pressed and keep the same label; menu buttons use aria-haspopup; unavailable actions use aria-disabled [S-L08-108].
- **Native:** SwiftUI Button with `.glass` and `.glassProminent` styles new in iOS 26 [S-L08-100]; UIKit UIButton [S-L08-103]. Compose Button, FilledTonalButton, OutlinedButton, TextButton, ElevatedButton [S-L08-105].
- **Consumes:** color roles (primary/on-primary, secondary container, outline variant, surface container low for elevated, danger/negative) [S-L08-034]; label type role (M3 label; Carbon body-compact-01, 14 px) [S-L08-062]; radius (M3 full, square option 12-28 dp, pressed 8-16 dp) [S-L08-034]; elevation (M3 elevated level 1, 0 disabled) [S-L08-034]; spacing (Carbon 16 px start, 64 px end without icon) [S-L08-062]; motion (M3 shape morph on press and select) [S-L08-033]; target size (HIG 44 x 44 pt, M3 48 x 48 dp for XS/S) [S-L08-039] [S-L08-034].

#### C02 Icon button (action) | 2 of 10 dedicated, 7 as variant
- **Names:** M3 Icon buttons; Primer IconButton; others as an icon-only mode of Button (Carbon icon-only modifier, shadcn `size="icon"`, S2 ActionButton).
- **Anatomy:** container (may be invisible), icon, accessible name (tooltip or aria-label) [inferred].
- **Variants:** M3 standard, filled, tonal, outlined, each with a toggle form (Compose FilledIconButton, FilledTonalIconButton, OutlinedIconButton and their ...ToggleButton pairs) [S-L08-105].
- **Sizes:** follows button sizes; M3 XS and S icon buttons need a 48 x 48 dp target [S-L08-034]; WCAG 2.5.8 minimum 24 x 24 CSS px [S-L08-070].
- **States:** as Button, plus selected for toggle icon buttons.
- **Key props:** icon, label (required, used for aria-label and tooltip), variant, toggle/selected.
- **APG:** Button (toggle: aria-pressed) [S-L08-108].
- **Native:** SwiftUI Button with Label or Image; Compose IconButton family [S-L08-105].
- **Consumes:** color roles, icon size scale (L05), radius, target size.

#### C03 Floating action button (action) | 1 of 10
- **Names:** M3 FABs, Extended FABs, FAB menu. No web system in the set has one.
- **Anatomy:** container, icon, optional label (extended FAB); FAB menu opens a list of related actions from the FAB [S-L08-008].
- **Variants/sizes:** Compose ships FloatingActionButton, Small/Medium/Large FAB, Extended (Small/Medium/Large) and FloatingActionButtonMenu with ToggleFloatingActionButton [S-L08-105].
- **States:** enabled, hover, focus, pressed; M3 says an unavailable FAB should not appear rather than be disabled [S-L08-095].
- **APG:** Button; FAB menu behaves as a menu button [inferred].
- **Native:** Compose FloatingActionButton family [S-L08-105]; no iOS counterpart (HIG has no FAB) [S-L08-017].
- **Consumes:** primary container color, large radius, elevation, motion.

#### C04 Split button (action) | 1 of 10 dedicated, 3 as variant
- **Names:** M3 Split buttons; Fluent Button type "split"; Carbon Menu buttons; shadcn Button Group example.
- **Anatomy:** primary action button plus a menu icon button; the menu part spins and changes shape when activated in M3 [S-L08-036].
- **Variants:** M3 elevated, filled, tonal, outlined (no text style); sizes XS-XL [S-L08-036].
- **Content rule:** the dominant action is not repeated in the menu; secondary options should carry the full phrase via aria-describedby when words are skipped [S-L08-066].
- **APG:** Button + Menu Button [S-L08-045].
- **Native:** Compose SplitButtonLayout [S-L08-105].
- **Consumes:** same as Button, plus menu surface tokens.

#### C05 Button group (action) | 5 of 10 dedicated, 1 as guidance
- **Names:** M3 Button groups; Polaris Button group; Primer ButtonGroup; S2 ButtonGroup and ActionButtonGroup; shadcn Button Group; Carbon gives button-group layout guidance only.
- **Anatomy:** container holding buttons or icon buttons.
- **Variants:** M3 standard and connected; connected groups replace the segmented button, support single-select, multi-select and selection-required, and apply shape morph on press and select [S-L08-035]. Carbon places the primary button on the outside of the set and does not recommend mixing sizes [S-L08-062] [S-L08-061].
- **APG:** none for a plain group; use Toolbar when it is a set of controls with arrow-key movement [S-L08-053].
- **Native:** Compose ButtonGroup [S-L08-105].
- **Consumes:** spacing (gap), radius (connected groups square inner corners), color roles.

#### C06 Toggle button (action) | 3 of 10 dedicated, 4 as variant
- **Names:** S2 ToggleButton; Radix Toggle; shadcn Toggle; M3 toggle configuration of Button; Fluent ToggleButton behavior; Atlassian `isSelected`.
- **Anatomy:** as Button, with a selected treatment. M3 toggles change color and shape (round to square) when selected [S-L08-034].
- **Guidance:** Fluent uses toggle buttons mostly in toolbars and prefers a switch for immediate settings changes [S-L08-066].
- **APG:** Button with aria-pressed; label must not change with state [S-L08-108].
- **Native:** Compose ToggleButton, ElevatedToggleButton, FilledTonalToggleButton, OutlinedToggleButton [S-L08-105].
- **Consumes:** selected-state color roles, shape, motion.

#### C07 Segmented control / toggle group (selection) | 7 of 10 | component.gallery 28
- **Names:** HIG Segmented controls; Carbon Content switcher; Primer SegmentedControl; S2 SegmentedControl and ToggleButtonGroup; Radix Toggle Group; shadcn Toggle Group; M3 Segmented buttons (now "no longer recommended", replaced by connected button groups) [S-L08-035].
- **Anatomy:** track or container, 2-5 segments, selected indicator, optional icons [inferred].
- **Behavior:** single-select (switches views, like tabs) or multi-select (formatting toggles). M3 Compose keeps SingleChoiceSegmentedButtonRow and MultiChoiceSegmentedButtonRow [S-L08-105].
- **APG:** Radio Group when single-select (arrow keys move and select); Toolbar with toggle buttons when multi-select [S-L08-046] [S-L08-053]. When it switches panels, Tabs is the correct pattern [S-L08-042].
- **Native:** SwiftUI `.segmented` picker style, UIKit UISegmentedControl [S-L08-103].
- **Consumes:** surface/secondary-container colors, radius, selected indicator motion.

#### C08 Toolbar / action bar (action) | 6 of 10
- **Names:** M3 Toolbars (docked and floating); HIG Toolbars (navigation bar guidance merged in June 2025); Fluent Toolbar; Primer ActionBar; S2 ActionBar (appears on bulk selection); Radix Toolbar.
- **Anatomy:** container, grouped items (buttons, icon buttons, toggles, text fields), separators, overflow ("More") menu [S-L08-040].
- **Variants:** M3 docked toolbar replaces the bottom app bar; floating toolbar is horizontal or vertical; standard or vibrant color; do not show with a navigation bar [S-L08-037]. HIG: `.prominent` style for one primary action (Done, Submit) on the trailing side; aim for at most three groups [S-L08-040].
- **APG:** Toolbar. One tab stop, arrow keys move between controls (roving tabindex), Home/End optional [S-L08-053].
- **Native:** SwiftUI toolbar placements (primaryAction, bottomBar, topBarLeading/Trailing), UIKit UIToolbar [S-L08-103]; Compose HorizontalFloatingToolbar, VerticalFloatingToolbar, FlexibleBottomAppBar [S-L08-105].
- **Consumes:** surface or material (Liquid Glass on iOS 26), spacing, icon size, elevation.

#### C09 Link (navigation) | 6 of 10 dedicated, 1 as variant | component.gallery 64
- **Names:** Fluent Link; Carbon Link; Polaris Link; Atlassian Link and Anchor primitive; Primer Link; S2 Link and LinkButton; shadcn Button `variant="link"`.
- **Anatomy:** text, underline (always, on hover, or never), optional trailing icon for external links [inferred].
- **Rule:** buttons for actions, links for navigation (Carbon, Atlassian) [S-L08-061] [S-L08-085].
- **States:** enabled, hover, focus-visible, pressed, visited [inferred].
- **APG:** Link (Enter activates) [S-L08-041].
- **Native:** SwiftUI Link [inferred].
- **Consumes:** link color role, body type, focus ring.

### Input

#### C10 Text field / input (input) | 9 of 10 | component.gallery 72
- **Names:** M3 Text fields; HIG Text fields; Fluent Input; Carbon Text input; Polaris Text, Email, URL, Password and Money fields; Atlassian Text field; Primer TextInput; S2 TextField; shadcn Input and Input Group; Radix only Password Toggle Field (preview).
- **Anatomy:** label, container (filled or outlined), input text, placeholder, leading/trailing icon or affix, helper text, error message, character counter [inferred from M3 supporting-text and Carbon helper conventions].
- **Variants:** M3 filled vs outlined (Compose TextField, OutlinedTextField, SecureTextField) [S-L08-105]; Polaris splits by data type (email, URL, password, money, number) [S-L08-022].
- **Sizes:** Carbon pairs 32 px inputs with small buttons and 40 px with medium [S-L08-061].
- **States:** enabled, hover, focus, filled, disabled, read-only, error, warning (Carbon) [inferred].
- **Key props:** label (required), description/helper, error, required, prefix/suffix, type, autoComplete, inputMode, maxLength.
- **APG:** no dedicated pattern; native input semantics plus aria-describedby for help and error, aria-invalid [inferred].
- **Native:** SwiftUI TextField / SecureField, UIKit UITextField [S-L08-103]; Compose TextField, OutlinedTextField, SecureTextField [S-L08-105].
- **Consumes:** surface-container or outline colors, error role, body type, label type, radius (M3 filled has top-only radius [inferred]), spacing, focus indicator.

#### C11 Textarea (input) | 6 of 10 dedicated, 3 as variant | component.gallery 52
- **Names:** Fluent Textarea; Polaris Text area; Atlassian Text area; Primer Textarea; S2 TextArea; shadcn Textarea; M3 multi-line text field; HIG Text views; Carbon text area within Text input.
- **Anatomy/props:** as Text field plus rows, auto-grow, resize handle, character count [inferred].
- **Native:** UIKit UITextView, SwiftUI Text/TextEditor [S-L08-103] [inferred for TextEditor].
- **Consumes:** as Text field.

#### C12 Number field / stepper (input) | 5 of 10 | component.gallery 20 ("Stepper: nudger, quantity, counter")
- **Names:** HIG Steppers; Fluent Spin button; Carbon Number input; Polaris Number field; S2 NumberField.
- **Anatomy:** input, increment and decrement buttons, optional unit/format.
- **Key props:** min, max, step, format (currency, percent), locale.
- **APG:** Spinbutton. Up/Down change value, Home/End jump to min/max, Page Up/Down large steps; aria-valuenow/min/max/valuetext [S-L08-110].
- **Native:** UIKit UIStepper [S-L08-103].
- **Consumes:** as Text field plus icon buttons.

#### C13 Search field (input) | 6 of 10 dedicated | component.gallery 30
- **Names:** M3 Search (search bar and search view); HIG Search fields; Fluent Searchbox; Carbon Search; Polaris Search field; S2 SearchField.
- **Anatomy:** leading search icon, input, clear button, optional scope or filter, suggestion list [inferred].
- **Platform:** iOS can place search as a dedicated tab at the trailing end of the tab bar (guidance updated 8 Jun 2026) [S-L08-040]; HIG says give search a primary position if important [S-L08-086].
- **APG:** Combobox when it shows suggestions [S-L08-044].
- **Native:** SwiftUI `searchable(...)`, UIKit UISearchController/UISearchBar [S-L08-103]; Compose SearchBar, DockedSearchBar, TopSearchBar, AppBarWithSearch [S-L08-105].
- **Consumes:** surface container, full radius (M3 search bar) [inferred], icon size, body type.

#### C14 Select (input) | 9 of 10 dedicated, 1 as variant | component.gallery 82
- **Names:** HIG Pop-up buttons and Pickers; Fluent Select and Dropdown; Carbon Select and Dropdown; Polaris Select; Atlassian Select; Primer Select; S2 Picker; Radix Select; shadcn Select and Native Select; M3 exposed dropdown menu.
- **Split to decide:** native `<select>` (Fluent Select, Primer Select, shadcn Native Select) vs custom listbox (Fluent Dropdown, Radix Select). Fluent recommends Select when choosing one of at least four options [S-L08-010].
- **Anatomy:** label, trigger (value + chevron), listbox popup, option (check indicator), helper/error.
- **APG:** Listbox (popup) or select-only Combobox; typeahead; focus is distinct from selection [S-L08-050] [S-L08-044].
- **Native:** SwiftUI Picker with MenuPickerStyle, UIKit pop-up button (`changesSelectionAsPrimaryAction`) [S-L08-103]; Compose ExposedDropdownMenuBox [S-L08-105].
- **Consumes:** as Text field plus menu surface, elevation, selected color.

#### C15 Combobox / autocomplete (input) | 5 of 10 dedicated, 3 as variant | component.gallery 37
- **Names:** HIG Combo boxes; Fluent Combobox; Primer Autocomplete and SelectPanel; S2 ComboBox; shadcn Combobox; Carbon combo box inside Dropdown; Atlassian searchable Select.
- **Anatomy:** input, toggle button, listbox popup, options, empty/loading row.
- **APG:** Combobox. Down/Alt+Down open, Up/Down move, Enter accepts, Escape closes; four autocomplete behaviors (none, list with manual selection, list with automatic selection, list with inline completion); role combobox with aria-expanded, aria-controls, aria-activedescendant, aria-autocomplete [S-L08-044].
- **Native:** macOS NSComboBox (HIG lists no SwiftUI link) [S-L08-103].
- **Consumes:** as Select.

#### C16 Multi-select / token field (input) | 4 of 10 dedicated, 4 as variant
- **Names:** HIG Token fields; Fluent Tag picker; Carbon Multiselect; Primer TextInputWithTokens; M3 input chips; S2 TagGroup with ComboBox; Atlassian Select isMulti; shadcn Combobox multiple.
- **Anatomy:** input, tokens/chips with remove buttons, popup list with checkboxes.
- **APG:** Combobox + Listbox with aria-multiselectable [S-L08-044] [S-L08-050].
- **Consumes:** chip/tag tokens, input tokens.

#### C17 Date & time picker / calendar (input) | 7 of 10 | component.gallery 44 (plus "Date input" 18)
- **Names:** M3 Date pickers and Time pickers; HIG Pickers; Carbon Date picker; Polaris Date picker and Date field; Atlassian Date time picker and Calendar; S2 DatePicker, DateRangePicker, Calendar, RangeCalendar, TimeField (S2 added multiple-date selection in v1.4.0, 28 May 2026) [S-L08-027]; shadcn Date Picker and Calendar.
- **Anatomy:** segmented date field or text input, calendar trigger, popover/modal calendar grid (month header, weekday row, day cells), range highlight, time input or dial [inferred].
- **Variants:** single date, range, multiple; docked vs modal (M3) [inferred]; Compose DatePicker, TimePicker, TimeInput [S-L08-105].
- **APG:** Grid (calendar) inside a Dialog; Spinbutton for segmented fields [S-L08-051] [S-L08-110].
- **Native:** SwiftUI DatePicker, UIKit UIDatePicker [S-L08-103].
- **Consumes:** primary for selected day, surface container, type scale, radius (full for day cells in M3 [inferred]).

#### C18 File upload / drop zone (input) | 3 of 10 dedicated, 1 as variant | component.gallery 32
- **Names:** Carbon File uploader; Polaris Drop zone; S2 DropZone; HIG Image wells (macOS).
- **Anatomy:** drop area, browse button, accepted-types hint, file list with progress, error and remove [inferred].
- **States:** idle, drag-over, uploading, complete, error [inferred].
- **Consumes:** dashed border/outline, feedback colors, progress bar.

#### C19 Color picker (input) | 3 of 10 | component.gallery 18
- **Names:** HIG Color wells; Polaris Color picker and Color field; S2 ColorArea, ColorWheel, ColorSlider, ColorField, ColorSwatch, ColorSwatchPicker.
- **Native:** UIKit UIColorWell, UIColorPickerViewController [S-L08-103].
- **Consumes:** outline, radius, focus ring; slider thumbs.

#### C20 One-time code (OTP) input (input) | 2 of 10 dedicated, 1 as variant
- **Names:** Radix One-Time Password Field (preview); shadcn Input OTP; HIG Digit entry views (tvOS/watchOS). Base UI also ships an OTP Field [S-L08-026].
- **Rule:** must allow paste and autofill so authentication does not become a cognitive-function test (WCAG 3.3.8 AA) [S-L08-090].
- **Consumes:** input tokens, monospace or tabular numerals (L02).

#### C21 Form field and form (input) | 7 of 10 dedicated, 3 as variant | component.gallery Form 21, Fieldset 32, Label 15
- **Names:** Fluent Field, Label, Info label; Carbon Form; Atlassian Form; Primer FormControl and CheckboxGroup; S2 Form and ContextualHelp; Radix Form (preview) and Label; shadcn Field and Label; Polaris builds label/help/error into each field.
- **Anatomy:** label, required/optional marker, control slot, description/help, validation message, optional info toggletip. Fluent Field wraps any control with label [S-L08-010].
- **Rules:** Carbon uses top-aligned labels only, 1-3 word labels without colons, and marks the minority case "(optional)" or "(required)" [S-L08-106].
- **APG:** none; fieldset/legend or group role for groups [S-L08-109].
- **Consumes:** label and helper type roles, error color, spacing between label/control/help.

#### C22 Rating (input) | 2 of 10 | component.gallery 19
- **Names:** HIG Rating indicators; Fluent Rating ("communicate user sentiment") [S-L08-010].
- **APG:** Radio Group for input [S-L08-046] [inferred].
- **Consumes:** icon, accent color.

### Selection

#### C23 Checkbox (selection) | 9 of 10 dedicated | component.gallery 84
- **Names:** M3 Checkbox; Fluent Checkbox; Carbon Checkbox; Polaris Checkbox and Choice list; Atlassian Checkbox; Primer Checkbox and CheckboxGroup; S2 Checkbox and CheckboxGroup; Radix Checkbox; shadcn Checkbox; HIG covers macOS checkboxes under Toggles.
- **Anatomy:** box, check/indeterminate mark, label, optional description, error.
- **States:** unchecked, checked, indeterminate, hover, focus, pressed, disabled, error. S2 added description and error messaging to Checkbox, Radio and Switch in v1.4.0 [S-L08-027].
- **APG:** Checkbox. Space toggles; aria-checked true/false/mixed; groups use role group with aria-labelledby [S-L08-109].
- **Native:** SwiftUI Toggle with checkbox style (macOS) [S-L08-103]; Compose Checkbox, TriStateCheckbox [S-L08-105].
- **Consumes:** primary (checked fill), on-primary (mark), outline (unchecked border), error, small radius (about 2 dp [inferred]), target size.

#### C24 Radio group (selection) | 8 of 10 dedicated, 2 as variant | component.gallery 85
- **Names:** M3 Radio button; Fluent Radio group; Carbon Radio button; Atlassian Radio; Primer Radio and RadioGroup; S2 RadioGroup; Radix Radio Group; shadcn Radio Group; Polaris Choice list; HIG macOS radio buttons under Toggles.
- **APG:** Radio Group. Tab into the group, arrow keys move and select; inside a toolbar arrows move without selecting [S-L08-046].
- **Native:** Compose RadioButton [S-L08-105].
- **Consumes:** primary, outline, error, target size.

#### C25 Switch (selection) | 10 of 10 | component.gallery 60 ("Toggle")
- **Names:** M3 Switch; HIG Toggles; Fluent Switch; Carbon Toggle; Polaris Switch; Atlassian Toggle; Primer ToggleSwitch; S2 Switch; Radix Switch; shadcn Switch.
- **Anatomy:** track, thumb (handle), optional icon in thumb (M3), label, optional state text.
- **Rule:** switches take effect immediately; use a checkbox when a submit step follows [inferred: common guidance]. Fluent: prefer a switch over a toggle button for immediate settings changes [S-L08-066].
- **APG:** Switch. Space toggles (Enter optional); role switch with aria-checked; the label must not change with state [S-L08-048].
- **Native:** SwiftUI Toggle (`.switch`), UIKit UISwitch [S-L08-103]; Compose Switch [S-L08-105].
- **Consumes:** primary / surface-container-highest (track), outline, full radius, motion (thumb slide), target size.

#### C26 Slider (selection) | 8 of 10 | component.gallery 38
- **Names:** M3 Sliders; HIG Sliders; Fluent Slider; Carbon Slider; Atlassian Range; S2 Slider and RangeSlider; Radix Slider; shadcn Slider.
- **Anatomy:** track (active/inactive), thumb(s), optional tick marks, value label, min/max labels, paired number input (Carbon) [inferred].
- **Variants:** continuous, discrete, range; Compose Slider, RangeSlider, VerticalSlider [S-L08-105].
- **APG:** Slider (arrows, Home/End, Page Up/Down; aria-valuenow/min/max/valuetext) and Slider (Multi-Thumb) [S-L08-049] [S-L08-041].
- **Native:** SwiftUI Slider, UIKit UISlider [S-L08-103].
- **Consumes:** primary, secondary container, radius, motion.

#### C27 Chip / tag (selection) | 6 of 10 dedicated, 3 as variant
- **Names:** M3 Chips (assist, filter, input, suggestion); Fluent Tag; Carbon Tag; Polaris Chip and Clickable chip; Atlassian Tag and Tag group; S2 TagGroup; Primer Token and Label; shadcn Badge; HIG Token fields.
- **Watch the naming collision:** component.gallery lists "Tag, Label, Chip" as aliases of Badge [S-L08-001]. The builder should separate interactive chips (filter, input, removable) from static badges (C43) [inferred].
- **Variants:** M3 four chip types; Compose AssistChip, FilterChip, InputChip, SuggestionChip plus elevated versions [S-L08-105].
- **APG:** Button (assist), toggle Button or checkbox semantics (filter), Listbox/grid for tag groups [inferred].
- **Consumes:** secondary container, outline, small radius (M3 8 dp [inferred]), label type.

### Navigation

#### C28 Tabs (navigation) | 9 of 10 | component.gallery 80
- **Names:** M3 Tabs; HIG Tab views (macOS; iOS uses Tab bars, C31); Fluent Tablist; Carbon Tabs; Atlassian Tabs; Primer UnderlineNav (navigation) and UnderlinePanels (panels); S2 Tabs; Radix Tabs; shadcn Tabs.
- **Anatomy:** tab list, tab (label, optional icon, badge), active indicator, panel.
- **Variants:** M3 primary vs secondary tabs, fixed vs scrollable (Compose PrimaryTabRow, SecondaryTabRow, scrollable versions) [S-L08-105]; line/underline vs contained vs pill [inferred].
- **APG:** Tabs. Arrows move between tabs, Home/End; activate on focus when panels load without latency, else Space/Enter; tablist/tab/tabpanel with aria-selected and aria-controls [S-L08-042]. Primer's split of UnderlineNav (links) vs UnderlinePanels (tabs) follows this line between navigation and panel switching [S-L08-012] [inferred].
- **Native:** SwiftUI TabView [S-L08-103]; Compose Tab, TabRow [S-L08-105].
- **Consumes:** primary (indicator), on-surface-variant (inactive label), label type, motion (indicator slide).

#### C29 Breadcrumbs (navigation) | 6 of 10 dedicated, 1 as variant | component.gallery 55
- **Names:** Fluent Breadcrumb; Carbon Breadcrumb; Atlassian Breadcrumbs; Primer Breadcrumbs; S2 Breadcrumbs; shadcn Breadcrumb; HIG Path controls (macOS).
- **Anatomy:** nav landmark, ordered list of links, separator, current page (aria-current), overflow menu for collapsed middle items [inferred].
- **APG:** Breadcrumb (nav landmark with label, aria-current="page") [S-L08-041] [inferred for details].
- **Consumes:** link color, secondary text, small type, icon.

#### C30 Pagination (navigation) | 4 of 10 dedicated, 2 as variant | component.gallery 48
- **Names:** Carbon Pagination; Atlassian Pagination; Primer Pagination; shadcn Pagination; HIG Page controls (dots, a different concept); Polaris table pagination.
- **Anatomy:** previous/next, page numbers, ellipsis, current page, optional page-size select and item range text (Carbon data tables) [inferred].
- **Consumes:** button/link tokens, selected color.

#### C31 Navigation bar / bottom tab bar (navigation) | 2 of 10
- **Names:** M3 Navigation bar; HIG Tab bars. Web systems in the set have none.
- **M3:** compact and medium windows, 3-5 equal destinations, pill-shaped active indicator; the flexible (shorter) navigation bar replaced the baseline in May 2025 [S-L08-083].
- **iOS 26:** the tab bar floats above content on Liquid Glass, can minimize on scroll when it has an accessory (for example a mini player), and can hold a dedicated search tab at the trailing end [S-L08-040].
- **Native:** SwiftUI TabView with TabBarMinimizeBehavior and TabViewBottomAccessoryPlacement; UIKit UITabBarController.MinimizeBehavior [S-L08-103]; Compose NavigationBar and ShortNavigationBar [S-L08-105].
- **Consumes:** surface container or glass material, secondary container (indicator), label type, icon size, badge.

#### C32 Navigation rail (navigation) | 1 of 10 dedicated, 1 as variant
- **Names:** M3 Navigation rail; HIG visionOS vertical tab bar.
- **M3:** medium to extra-large windows, 3-7 destinations plus optional FAB; collapsed and expanded rails replaced the baseline rail, and the expanded rail replaces the navigation drawer; expanded rail can be modal or non-modal [S-L08-080].
- **Native:** Compose NavigationRail, WideNavigationRail, ModalWideNavigationRail [S-L08-105].
- **Consumes:** surface, secondary (active label), indicator shape, motion (collapse/expand).

#### C33 Side navigation / sidebar (navigation) | 8 of 10 dedicated, 1 as variant | component.gallery 62 ("Navigation")
- **Names:** M3 Navigation drawer (no longer recommended under M3 Expressive) [S-L08-082]; HIG Sidebars; Fluent Nav; Carbon UI shell side nav; Atlassian Navigation system (old Side navigation deprecated); Primer NavList; S2 SideNav (added v1.6.0, 31 Jul 2026) [S-L08-027]; shadcn Sidebar; Radix Navigation Menu.
- **Anatomy:** container, header (product/logo), sections with headings, items (icon, label, badge), nested groups, collapse toggle, footer (account/settings) [inferred].
- **Variants:** persistent, collapsible to icons (rail), overlay/modal on small screens [inferred]; HIG adaptable sidebar that turns into a tab bar [S-L08-103].
- **APG:** Disclosure for nested groups; links with aria-current; not the menu role for site navigation [S-L08-113] [S-L08-112].
- **Native:** SwiftUI NavigationSplitView and `sidebarAdaptable` [S-L08-103]; Compose ModalNavigationDrawer, PermanentNavigationDrawer [S-L08-105].
- **Consumes:** surface/layer colors, selected-item color, body type, icon size, spacing (density).

#### C34 App bar / header / page header (navigation) | 5 of 10 dedicated, 3 as variant | component.gallery Header 38
- **Names:** M3 App bars; HIG Toolbars (navigation bar merged in June 2025) [S-L08-040]; Carbon UI shell header; Atlassian Page header and Navigation system; Primer PageHeader; Polaris Page title; Radix and shadcn Navigation Menu / Menubar.
- **Two different things:** the global app header (product switcher, search, account) and the page header (title, breadcrumbs, primary page actions). Atlassian and Primer document the page header separately [S-L08-011] [S-L08-012].
- **Native:** Compose TopAppBar, CenterAlignedTopAppBar, Medium/Large(Flexible)TopAppBar [S-L08-105]; UIKit `prefersLargeTitles` [S-L08-103].
- **Consumes:** surface, title type roles, icon buttons, elevation or scroll-edge effect.

#### C35 Tree view (navigation) | 5 of 10 dedicated, 1 as variant | component.gallery 14
- **Names:** HIG Outline views; Fluent Tree; Carbon Tree view; Primer TreeView; S2 TreeView; Atlassian Table tree.
- **APG:** Tree View. Right/Left expand, collapse or move to child/parent; Up/Down; Home/End; typeahead; * expands siblings; tree/treeitem/group with aria-expanded [S-L08-111].
- **Native:** SwiftUI OutlineGroup [S-L08-103].
- **Consumes:** indentation spacing, chevron icon, selected color, density.

#### C36 Steps / progress tracker (navigation) | 2 of 10 dedicated, 1 as variant | component.gallery "Progress indicator" 38
- **Names:** Carbon Progress indicator; Atlassian Progress tracker and Progress indicator; Primer Timeline (activity history, related).
- **Anatomy:** ordered steps with status (complete, current, incomplete, error, disabled), connectors, labels [inferred].
- **Consumes:** primary/success colors, icon, label type.

### Feedback

#### C37 Alert / inline message / banner (feedback) | 7 of 10 | component.gallery 108
- **Names:** Fluent Message bar; Carbon Notification (inline, actionable, callout, banner types); Polaris Banner; Atlassian Banner, Section message, Inline message; Primer Banner and InlineMessage; S2 InlineAlert; shadcn Alert. M3 and HIG have no in-page banner in their current indexes.
- **Anatomy:** status icon, title, body, actions, dismiss button, container with status color.
- **Variants:** status info, success, warning, error (Carbon maps blue, green, yellow, red with filled icons) and low vs high contrast [S-L08-079]; scope: page-level banner vs section vs inline next to a field [S-L08-011].
- **Behavior:** Carbon inline notifications persist until resolved or dismissed and should stay under two lines; callouts load with the page and cannot be dismissed [S-L08-079].
- **APG:** Alert (role alert, no focus move) for dynamic messages; avoid auto-disappearing alerts [S-L08-116].
- **Consumes:** feedback color roles (container + on-container + border), icon set, body type, radius, spacing.

#### C38 Toast / snackbar / flag (feedback) | 6 of 10 dedicated, 1 as variant | component.gallery 41
- **Names:** M3 Snackbar; Fluent Toast; Atlassian Flag; S2 Toast; Radix Toast; shadcn Toast; Carbon toast notification type. Primer deliberately has none and says toasts are not recommended [S-L08-098]. Polaris web components list no toast component [S-L08-022].
- **Anatomy:** container, message, optional action, dismiss, optional status icon; a region/stack that queues multiple.
- **Behavior:** Carbon toasts without actions may auto-dismiss; toasts with actions persist until dismissed [S-L08-079]. Primer lists WCAG 2.2.1, 1.3.2, 2.1.1 and 4.1.3 risks and recommends banners, dialogs or no message instead [S-L08-098].
- **APG:** none dedicated; Alert/status live region [S-L08-116].
- **Native:** Compose Snackbar [S-L08-105]; iOS has no in-app toast in HIG [S-L08-017].
- **Consumes:** inverse surface (M3 snackbar [inferred]), elevation, motion (enter/exit), duration tokens (L04).

#### C39 Progress bar / meter (feedback) | 10 of 10 | component.gallery 40
- **Names:** M3 Progress indicators (linear and circular); HIG Progress indicators and Gauges; Fluent Progress bar; Carbon Progress bar; Polaris Progress; Atlassian Progress bar; Primer ProgressBar; S2 ProgressBar, ProgressCircle, Meter; Radix Progress; shadcn Progress.
- **Semantics:** progress (task completion, determinate or indeterminate) vs meter (a static measurement such as storage used). APG has a separate Meter pattern [S-L08-041]. Fluent's Progress bar covers both system and task information [S-L08-010].
- **Guidance:** use a progress bar for waits over 10 seconds [S-L08-074].
- **Native:** SwiftUI ProgressView, Gauge; UIKit UIProgressView [S-L08-103]; Compose LinearProgressIndicator, CircularProgressIndicator [S-L08-105].
- **Consumes:** primary / secondary container (track), status colors, radius, motion.

#### C40 Spinner / loading indicator (feedback) | 9 of 10 | component.gallery 66
- **Names:** M3 Loading indicator (May 2025, replaces most indeterminate circular progress; for waits under 5 s; contained or uncontained; used for pull-to-refresh) [S-L08-038]; HIG activity indicator; Fluent Spinner; Carbon Loading and Inline loading; Polaris Spinner; Atlassian Spinner; Primer Spinner; S2 ProgressCircle; shadcn Spinner.
- **Placement:** inline in a button (Carbon disables the button during inline loading [S-L08-061]; S2 isPending delays the spinner 1 s [S-L08-067]), in a region, or full page.
- **Guidance:** under 1 s show nothing; 2-10 s spinner for a module or skeleton for a page [S-L08-074].
- **Native:** UIKit UIActivityIndicatorView, UIRefreshControl [S-L08-103]; Compose LoadingIndicator, ContainedLoadingIndicator [S-L08-105].
- **Consumes:** primary color, size scale, motion (rotation or M3 shape morph).

#### C41 Skeleton (feedback) | 5 of 10 dedicated, 2 as variant | component.gallery 30
- **Names:** Fluent Skeleton; Atlassian Skeleton (early access); Primer SkeletonText, SkeletonBox, SkeletonAvatar; S2 Skeleton; shadcn Skeleton; Carbon skeleton states per component.
- **Guidance:** skeletons suit full-page loads of 2-10 s; avoid frame-only skeletons [S-L08-074]; HIG: show placeholder content as soon as possible [S-L08-086].
- **Consumes:** surface-variant/neutral fill, radius matching the real content, shimmer or pulse motion with a reduced-motion fallback [inferred].

#### C42 Empty state (feedback) | 5 of 10 dedicated, 1 as variant | component.gallery 16
- **Names:** Polaris Empty state; Atlassian Empty state; Primer Blankslate; S2 IllustratedMessage; shadcn Empty; Carbon empty-states pattern.
- **Anatomy:** illustration or icon, heading, body (why it is empty), primary action, optional secondary link.
- **Types:** first use, user-cleared, no results/errors; content should give status, a learning cue and a direct pathway [S-L08-078].
- **Consumes:** illustration style (L05), heading/body type, spacing, button.

#### C43 Badge / status label (feedback) | 7 of 10 dedicated, 2 as variant | component.gallery 123
- **Names:** M3 Badges (dot or count on icons/navigation); Fluent Badge; Polaris Badge; Atlassian Badge (numeric) and Lozenge (status); Primer CounterLabel, Label, StateLabel; S2 Badge and StatusLight; shadcn Badge; Carbon Tag; HIG tab-bar badge.
- **Sub-types to model separately:** count/notification badge, status label (lozenge), status light (dot + text) [S-L08-011] [S-L08-015].
- **HIG:** tab badges are a red oval with white text for critical information only [S-L08-040].
- **APG:** none; not interactive; ensure text alternative for counts [inferred].
- **Native:** Compose Badge, BadgedBox [S-L08-105].
- **Consumes:** error/status colors, small label type, full radius, min size.

#### C44 AI indicator and conversation components (feedback) | 2 of 10 dedicated, 2 as variant | new in 2025-26
- **Names:** Carbon AI label (and "AI presence" in data tables) [S-L08-009] [S-L08-092]; Atlassian Rovo button appearance and a "Rovo UI" section [S-L08-063] [S-L08-011]; S2 `genai` and `premium` button variants and a first preview of AI Components in v1.7.0 (1 Sep 2026) [S-L08-067] [S-L08-027]; shadcn Message, Bubble, Message Scroller, Attachment, Marker and Questionnaire (Aug 2026) [S-L08-018] [S-L08-020].
- **Anatomy (chat):** message list with scroll anchoring, message bubble (user vs assistant), attachments, prompt input with send/stop, suggestion chips, AI disclosure label [inferred from shadcn names].
- **Why it matters:** this is the fastest-moving part of component inventories; the builder should treat "AI surfaces" as an optional module [inferred].
- **Consumes:** a distinct AI accent or gradient token (Carbon AI label, S2 genai) [inferred], motion (streaming), type.

### Overlay

#### C45 Tooltip / toggletip (overlay) | 9 of 10 dedicated, 1 as variant | component.gallery 74
- **Names:** M3 Tooltips (plain and rich); Fluent Tooltip; Carbon Tooltip and Toggletip; Polaris Tooltip; Atlassian Tooltip; Primer Tooltip; S2 Tooltip and ContextualHelp; Radix Tooltip; shadcn Tooltip; HIG macOS/visionOS tooltips.
- **Tooltip vs toggletip:** tooltips show on hover/focus and hold only non-essential text; toggletips (Carbon Toggletip, S2 ContextualHelp, Fluent Info label) open on click and can hold links [S-L08-009] [S-L08-010] [S-L08-015].
- **Conflict:** Fluent says show a tooltip on disabled buttons explaining why [S-L08-066]; Atlassian says never put tooltips on disabled buttons [S-L08-085].
- **APG:** Tooltip (work in progress, no task-force consensus): shows on focus or hover, Escape dismisses, role tooltip + aria-describedby [S-L08-047].
- **Native:** Compose TooltipBox (PlainTooltip, RichTooltip) [S-L08-105].
- **Consumes:** inverse surface, small body type, small radius, elevation, delay and fade motion.

#### C46 Popover / hover card (overlay) | 9 of 10 dedicated, 1 as variant | component.gallery 50
- **Names:** HIG Popovers; Fluent Popover; Carbon Popover; Polaris Popover; Atlassian Popup and Inline dialog; Primer Popover and AnchoredOverlay; S2 Popover; Radix Popover and Hover Card; shadcn Popover and Hover Card; Base UI Preview Card [S-L08-026].
- **Anatomy:** trigger, anchored surface, optional arrow/caret, content, optional close.
- **APG:** Dialog (non-modal) when it holds interactive content; Escape closes and focus returns to the trigger [S-L08-043] [inferred for non-modal].
- **Native:** SwiftUI `popover(...)`, UIKit UIPopoverPresentationController [S-L08-103].
- **Consumes:** surface container, elevation/shadow, radius, border, motion.

#### C47 Dialog / modal (overlay) | 10 of 10 | component.gallery 82
- **Names:** M3 Dialogs; HIG Alerts and Sheets; Fluent Dialog; Carbon Modal; Polaris Modal; Atlassian Modal dialog (with Blanket scrim); Primer Dialog; S2 Dialog (XL size added v0.12.0) [S-L08-027]; Radix Dialog; shadcn Dialog.
- **Anatomy:** scrim/blanket, container, title, body, actions (footer), close button.
- **Sizes:** small, medium, large, full-screen (M3 full-screen dialog on compact windows [inferred]).
- **Button order:** HIG sheets: Cancel leading, Done trailing [S-L08-040]; Carbon: primary button outside, secondary inside, primary takes default focus when nothing else is actionable [S-L08-062] [S-L08-061].
- **APG:** Dialog (Modal). Focus moves inside, Tab/Shift+Tab trapped, Escape closes, focus returns to the invoker; role dialog, aria-modal, aria-labelledby [S-L08-043].
- **Native:** SwiftUI `sheet(...)`, `alert(...)`; UIKit UIAlertController, UISheetPresentationController [S-L08-103]; Compose AlertDialog, BasicAlertDialog [S-L08-105].
- **Consumes:** surface container high, scrim color, elevation, large radius (M3 28 dp [inferred]), headline type, motion.

#### C48 Confirmation / alert dialog (overlay) | 4 of 10 dedicated, 6 as variant
- **Names:** HIG Alerts and Action sheets; Primer ConfirmationDialog; Radix Alert Dialog; shadcn Alert Dialog; others use a Dialog with a danger button.
- **Rules:** use for serious or irreversible actions only; label buttons with the verb ("Delete file" / "Keep file"); prefer undo; type-to-confirm only for rare severe cases [S-L08-075]. HIG: never give the destructive button the primary role [S-L08-039]. Fluent: buttons answer the title ("Delete this file?" gets "Delete" and "Cancel") [S-L08-066].
- **APG:** Alert and Message Dialogs: role alertdialog, aria-modal, aria-describedby pointing at the message [S-L08-114].
- **Native:** SwiftUI `confirmationDialog(...)` with `destructive` role; UIAlertController action sheet style [S-L08-103].
- **Consumes:** danger color roles, dialog tokens.

#### C49 Sheet / drawer / side panel (overlay) | 5 of 10 dedicated, 2 as variant | component.gallery Drawer 38
- **Names:** M3 Bottom sheets and Side sheets; HIG Sheets and Panels; Fluent Drawer; Atlassian Drawer and Panel; shadcn Sheet and Drawer; Primer Dialog side position; Radix Dialog.
- **Variants:** modal vs non-modal (standard); bottom vs side; detents (iOS resizable sheets rest at detents and can show a grabber) [S-L08-040].
- **Native:** UIKit UISheetPresentationController (detents, prefersGrabberVisible) [S-L08-103]; Compose ModalBottomSheet [S-L08-105].
- **Consumes:** surface container low, scrim, top radius, elevation, motion (slide).

#### C50 Menu: dropdown, context, menubar (overlay) | 10 of 10 | component.gallery "Dropdown menu" 49
- **Names:** M3 Menus; HIG Menus, Context menus, Pull-down buttons, The menu bar; Fluent Menu; Carbon Menu and Menu buttons; Polaris Menu; Atlassian Dropdown menu and Menu; Primer ActionMenu and ActionList; S2 Menu and ActionMenu; Radix Dropdown Menu, Context Menu, Menubar; shadcn same three.
- **Anatomy:** trigger, surface, items (icon, label, shortcut, description), checkable items, groups with headings, separators, submenus.
- **APG:** Menu Button + Menu and Menubar. Enter/Space/Down open; arrows, Home/End, typeahead; Escape closes and returns focus; menuitem, menuitemcheckbox, menuitemradio; do not use menu role for site navigation [S-L08-045] [S-L08-112].
- **Native:** SwiftUI Menu, `contextMenu(...)`; UIKit UIContextMenuInteraction [S-L08-103]; Compose DropdownMenuItem, DropdownMenuGroup [S-L08-105].
- **Consumes:** surface container, elevation, radius, body type, density (item height), destructive color.

#### C51 Command palette (overlay) | 1 of 10
- **Names:** shadcn Command.
- **Anatomy:** dialog, search input, grouped result list, shortcuts (Kbd), empty state.
- **APG:** Combobox + Listbox inside a Dialog [S-L08-044] [S-L08-043] [inferred composition].
- **Consumes:** dialog + menu tokens.

### Containment

#### C52 Card / tile (containment) | 6 of 10 dedicated, 3 as variant | component.gallery 77
- **Names:** M3 Cards (elevated, filled, outlined; Compose Card, ElevatedCard, OutlinedCard) [S-L08-105]; Fluent Card; Carbon Tile; Primer Card; S2 Card and CardView; shadcn Card; Polaris Section/Box; Atlassian Tile (an asset tile, a different meaning); HIG GroupBox.
- **Anatomy:** container, media, header (title, subtitle, avatar), body, actions; whole card clickable or not.
- **Decision:** separation by elevation vs border vs fill (see DC-L08-15) [inferred].
- **Consumes:** surface container colors, elevation, radius (M3 12 dp [inferred]), padding, outline.

#### C53 Accordion / disclosure (containment) | 7 of 10 | component.gallery 101
- **Names:** HIG Disclosure controls; Fluent Accordion; Carbon Accordion; Primer Details; S2 Accordion and Disclosure; Radix Accordion and Collapsible; shadcn Accordion and Collapsible. Atlassian and M3 have none.
- **APG:** Accordion (heading wrapping a button, aria-expanded, aria-controls; single or multiple open) and Disclosure (Enter/Space toggle) [S-L08-052] [S-L08-113].
- **Native:** SwiftUI DisclosureGroup [S-L08-103].
- **Consumes:** divider/outline, chevron icon, body/title type, motion (expand).

#### C54 Divider / separator (containment) | 6 of 10 | component.gallery 34
- **Names:** M3 Divider; Fluent Divider; Polaris Divider; S2 Divider; Radix Separator; shadcn Separator.
- **Variants:** horizontal, vertical, inset, with label; Compose HorizontalDivider, VerticalDivider [S-L08-105].
- **Consumes:** outline-variant color, border width.

#### C55 Carousel (containment) | 3 of 10 dedicated, 1 as variant | component.gallery 22
- **Names:** M3 Carousel; Fluent Carousel; shadcn Carousel; HIG Page controls.
- **APG:** Carousel. Rotation stop control first in tab order; rotation stops on focus or hover; aria-roledescription "carousel"/"slide" [S-L08-115].
- **Native:** Compose HorizontalMultiBrowseCarousel [inferred: not in the checked files]; UIKit UIPageControl [S-L08-103].
- **Consumes:** radius, spacing, motion.

### Data display

#### C56 List / list item (data display) | 8 of 10 | component.gallery 67
- **Names:** M3 Lists; HIG Lists and tables, Collections; Fluent List; Carbon List, Contained list, Structured list; Polaris Ordered/Unordered list; Primer ActionList; S2 ListView; shadcn Item.
- **Anatomy:** leading (icon, avatar, checkbox), headline, supporting text, trailing (meta, icon, switch), divider.
- **Density:** one-, two-, three-line items (M3) [inferred]; Compose ListItem and SegmentedListItem [S-L08-105].
- **APG:** Listbox when selectable; plain list otherwise; Grid for rich interactive rows [S-L08-050] [S-L08-051].
- **Native:** SwiftUI List, UIKit UITableView/UICollectionView [S-L08-103].
- **Consumes:** surface, body/label type, spacing (density), selected state color.

#### C57 Table / data table (data display) | 7 of 10 dedicated, 1 as variant | component.gallery 73
- **Names:** HIG Lists and tables; Carbon Data table; Polaris Table; Atlassian Table, Dynamic table, Table tree; Primer DataTable; S2 TableView; shadcn Table and Data Table; Fluent Table/DataGrid exist in code but not on the design site [inferred].
- **Anatomy:** toolbar (search, filters, batch actions), header row (sort), rows, cells, selection column, expansion, pagination, empty/loading states [S-L08-092].
- **Sizes:** Carbon rows XS 24, S 32, M 40, L 48, XL 64 px; header matches row height; 48 px toolbar with L/XL, small toolbar with S/XS [S-L08-092].
- **APG:** Table for static data; Grid when cells are interactive or editable (arrow navigation, Enter/F2 edit) [S-L08-051]; Treegrid for hierarchical rows [S-L08-041].
- **Native:** SwiftUI Table, UIKit UITableView [S-L08-103].
- **Consumes:** layer/surface colors, zebra option, body-compact type, tabular numerals, row-height density scale.

#### C58 Avatar / avatar group (data display) | 7 of 10 | component.gallery 38
- **Names:** Fluent Avatar, Avatar group, Persona; Polaris Avatar; Atlassian Avatar and Avatar group; Primer Avatar and AvatarStack; S2 Avatar and AvatarGroup; Radix Avatar; shadcn Avatar.
- **Anatomy:** image, initials fallback, icon fallback, presence/status badge, shape (circle, or square for entities) [inferred].
- **Consumes:** full radius, size scale, categorical colors for initials (L01), badge.

#### C59 Text and heading components (data display) | 6 of 10 dedicated, 1 as variant | component.gallery Heading 29
- **Names:** Fluent Text; Polaris Heading, Text, Paragraph; Atlassian Heading, Text, MetricText; Primer Heading, Text, Truncate; shadcn Typography; HIG Labels.
- **Why a component:** it binds the type scale tokens (L02) to semantic props (as, size, weight, color, truncate) so product teams stop hand-setting font values [S-L08-010] [inferred].
- **Consumes:** type roles, text color roles.

### Media

#### C60 Icon (media) | 4 of 10 dedicated, 5 as foundation
- **Names:** Fluent Icon; Polaris Icon; Atlassian Icon (beta); S2 Icons (S2 refreshed icon sizing to match text line height in v1.7.0) [S-L08-027]; M3 Material Symbols, HIG SF Symbols, Carbon and Primer icon libraries as foundations; Radix Accessible Icon utility.
- **Consumes:** icon size scale, color roles; see L05.

#### C61 Image / thumbnail (media) | 5 of 10 dedicated, 2 as variant | component.gallery 29
- **Names:** HIG Image views; Fluent Image; Polaris Image and Thumbnail; Atlassian Image (light/dark switching) [S-L08-011]; S2 Image; Radix and shadcn Aspect Ratio.
- **Consumes:** radius, aspect-ratio tokens, placeholder surface.

### Layout

#### C62 Layout primitives (layout) | 3 of 10 dedicated, 2 as variant | component.gallery Stack 10
- **Names:** Atlassian Box, Stack, Inline, Flex, Grid, Bleed (token-backed primitives) [S-L08-011]; Polaris Box, Stack, Grid, Section, Query container [S-L08-022]; Primer Stack; Carbon 2x Grid; shadcn Resizable, Scroll Area.
- **Why:** primitives expose spacing, color and radius tokens as props so layouts stay on-scale [S-L08-011].
- **Consumes:** spacing scale, breakpoints (L03), surface colors, radius.

#### C63 Page layout / app shell (layout) | 5 of 10 dedicated, 2 as variant
- **Names:** HIG Split views and Windows; Carbon UI shell; Polaris Page; Atlassian Page and Panel; Primer PageLayout and SplitPageLayout; M3 canonical layouts (feed, list-detail, supporting pane) and Compose Scaffold [S-L08-096] [S-L08-105]; shadcn Sidebar + Resizable.
- **Native:** SwiftUI NavigationSplitView, HSplitView/VSplitView; UIKit UISplitViewController [S-L08-103].
- **APG:** Landmarks; Window Splitter for resizable panes [S-L08-041].
- **Consumes:** grid, breakpoints, pane widths, surface layering (L03).

#### C64 Accessibility utilities (layout) | 2 of 10 dedicated, 1 as variant | component.gallery Visually hidden 11
- **Names:** Atlassian Visually hidden, Focusable (replaces the deprecated Focus ring) and Portal [S-L08-011] [S-L08-093]; Radix Visually Hidden, Portal, Slot, Direction Provider, Accessible Icon [S-L08-021]; shadcn Direction.
- **Why:** these are the invisible atoms every component depends on: focus indication, screen-reader-only text, portals for overlays, RTL direction [inferred].
- **Consumes:** focus ring tokens (color, width, offset).

## Catalog gaps
- **Release status of M3 Expressive composables.** The Compose names cited above (ButtonGroup, SplitButtonLayout, FloatingActionButtonMenu, Horizontal/VerticalFloatingToolbar, ShortNavigationBar, WideNavigationRail, LoadingIndicator) were read from androidx-main source [S-L08-105]. Per L00, the latest stable Compose Material3 is 1.4.0 (24 Sep 2025); Expressive APIs are being graduated in the 1.5.0 alphas and the LoadingIndicator promotion was reverted, so no stable release ships them without opt-ins [S-L00-047 via sources/COMMUNITY-SIGNAL.md]. M3's own pages mark every Expressive component "Web: Expressive unavailable" [S-L08-033] [S-L08-035]. Treat Expressive components as Android-first.
- **iOS 26 glass controls are user-adjustable.** iOS 26.1 added a Clear/Tinted choice and iOS 27 (released about 14 Sep 2026) added a transparency slider, so glass buttons and bars must read well from fully clear to fully tinted and with Reduce Transparency on [S-L00-018] [S-L00-019] [S-L00-048 via sources/COMMUNITY-SIGNAL.md].
- Counts for Fluent use the Fluent 2 design site; Fluent UI React v9 code includes more (for example Table/DataGrid) that were not verified this session [inferred].
- Polaris counts use the web components index for App Home; admin-only UI (toasts, navigation) is delivered through App Bridge APIs, which were not checked [inferred].
- component.gallery counts are "examples", not design-system counts, and the site does not date its data [S-L08-002].
- Sizes, radii and anatomy marked [inferred] should be re-checked by the verification lane (V1) against each system's spec pages.
