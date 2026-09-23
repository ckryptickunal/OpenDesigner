# L08: Components & Patterns

Lane: L08 (Components & Patterns). Author: orchestrator subagent L08. Written 2026-09-23.
Status: complete (see `## Open questions / gaps` and `## Confidence`).
Companion file: `research/L08-component-catalog.md` holds the 64-entry component catalog and the 10-system coverage matrix. Every source is logged in `traces/L08-trace.md`.

## Lane overview

**What this lane gives the builder.**
1. **Ontology:** 64 canonical components in 10 categories, each with aliases across 10 benchmark systems, anatomy, variants, sizes, states, props, WAI-ARIA pattern, native iOS/Android counterparts, and the foundations it consumes (catalog file). Plus 13 patterns and 5 page templates, each listed with the building blocks it composes (this file).
2. **Questions:** 23 Decision Cards covering the component-level choices a designer makes (how many button variants, disabled approach, focus style, density, loading, destructive actions, navigation model, feedback model, API style, build strategy, documentation template).
3. **Causality:** every card lists what it depends on and what it changes; every catalog entry lists the foundation tokens it reads. Together those are the edges of the decision graph from foundations to components to patterns.

**Headline findings.**
- **The core inventory is stable; the edges are moving.** Four components are in all 10 benchmark systems (Switch, Progress bar, Dialog, Menu) and eight more are in 9 (Button, Text field, Select, Checkbox, Tabs, Tooltip, Popover, Spinner) [catalog matrix]. The Component Gallery tracks 60 components across 95 systems [S-L08-002].
- **2025-26 changes the builder must model.** M3 Expressive (May 2025) added button groups, split buttons, FAB menu, loading indicator and toolbars, and demoted the segmented button, navigation drawer, bottom app bar and baseline navigation bar/rail [S-L08-035] [S-L08-037] [S-L08-082] [S-L08-083] [S-L08-080]. iOS 26 added Liquid Glass button styles and a floating, minimizing tab bar with a search tab [S-L08-100] [S-L08-040]. Polaris React is deprecated in favor of Polaris web components [S-L08-024]. Spectrum 2 reached v1.0 on 16 Dec 2025 [S-L08-027]. shadcn/ui made Base UI its default primitive layer in July 2026 and added React Aria [S-L08-020].
- **AI components are the new frontier.** Carbon's AI label, Atlassian's Rovo button appearance, Spectrum 2's `genai`/`premium` button variants and AI Components preview, and shadcn's Message/Bubble/Message Scroller/Questionnaire are all 2025-26 additions [S-L08-009] [S-L08-063] [S-L08-067] [S-L08-027] [S-L08-018].
- **Real disagreements exist, and they are good questionnaire items.** Disabled buttons: Carbon disables the submit button on short forms, Atlassian says never disable form submission, Primer adds an "inactive" state instead [S-L08-106] [S-L08-085] [S-L08-064]. Tooltips on disabled buttons: Fluent says yes, Atlassian says never [S-L08-066] [S-L08-085]. Toasts: M3, Fluent, Atlassian, S2, Radix and shadcn ship them; Primer rejects them on accessibility grounds [S-L08-098].
- **Button hierarchy has converged on 4-6 emphasis levels plus a danger treatment,** but names differ (M3 filled/tonal/outlined/text/elevated; Carbon primary/secondary/tertiary/ghost/danger; Atlassian adds warning and discovery) [S-L08-033] [S-L08-061] [S-L08-063].

## Taxonomy: how systems organize building blocks

### Atomic design (Brad Frost)
Five stages [S-L08-054]:
- **Atoms:** basic elements that cannot be broken down further and still work (button, input, label).
- **Molecules:** "relatively simple groups of UI elements functioning together as a unit", for example a search form made of label, input and button.
- **Organisms:** complex sections built from molecules and atoms (site header, product grid).
- **Templates:** "page-level objects that place components into a layout and articulate the design's underlying content structure".
- **Pages:** templates filled with real, representative content; they test the system.
Frost stresses it is "not a linear process" but a mental model [S-L08-054]. In April 2025 he said the one thing he would add is design tokens, as "subatomic particles" below atoms [S-L08-056].

### Alternative taxonomies used by the benchmark systems
- **Primitives > components > patterns.** Atlassian lists token-backed primitives (Box, Stack, Inline, Flex, Grid, Bleed, Pressable, Anchor, Focusable, Text) separately from components [S-L08-011]. Radix ships behavior primitives plus utilities (Slot, Portal, Visually Hidden) [S-L08-021].
- **Foundations > components > patterns.** Carbon separates components (41) from patterns such as notifications, forms and filtering [S-L08-009] [S-L08-079] [S-L08-106] [S-L08-107]. Apple HIG splits Foundations, Patterns (25, from Charting data to Workouts) and Components (64 in 8 categories) [S-L08-086] [S-L08-017].
- **Purpose categories.** M3 groups components by purpose: action, containment, communication, navigation, selection, text input [S-L08-008]. Polaris web components: actions; feedback and status; forms; layout and structure; media; overlays; typography and content [S-L08-022]. Atlassian: forms and inputs, images and icons, labels, layout and structure, loading, messaging, navigation, overlays and layering, status indicators, text and data display, primitives [S-L08-011].
- **Templates / canonical layouts.** M3 names three canonical layouts (feed, list-detail, supporting pane) on a scaffold of bar, rail and pane regions [S-L08-096]; Primer ships PageLayout and SplitPageLayout as components [S-L08-012].

**Recommendation for the builder's ontology** [inferred]: use five levels that map to both vocabularies: Tokens (subatomic) > Primitives (layout, text, focusable, pressable) > Components (the 64-entry catalog) > Patterns (compositions with behavior rules) > Templates (page layouts). Keep Frost's names as aliases because designers know them.

## Composition vs configuration APIs

| Model | How it works | Who uses it | Trade-off |
|---|---|---|---|
| **Configuration (props)** | One component, many props: `<Button variant size icon loading>` | Carbon, Primer, Atlassian Button, Polaris `s-button` [S-L08-063] [S-L08-064] [S-L08-068] | Easy to keep consistent; every new need becomes a prop |
| **Compound components / parts** | Named sub-parts assembled by the consumer: `Menu.Trigger`, `Menu.Item` | Base UI [S-L08-088], Radix, shadcn | Flexible layouts; more ways to go off-system |
| **asChild / Slot** | Primitive clones its child and merges props; child must spread props and forward ref | Radix [S-L08-087] | Keeps your own element (for example a router Link) with primitive behavior |
| **render prop** | Pass an element or a function that receives state | Base UI [S-L08-088], React Aria [S-L08-089] | Explicit control of prop spreading; state-aware rendering |
| **Named slots** | Children declare `slot="..."`; parent supplies props per slot via context | React Aria [S-L08-089]; Figma now has a "slots" component property (per L00) [S-L00-045] | Maps cleanly to Figma component anatomy |

State exposure matters for styling: React Aria passes states such as isPressed and isSelected to render props [S-L08-089]. The builder should export components that expose state as data attributes or render-prop values so themes can style every state [inferred].

## Headless vs styled libraries (status verified 2026-09-23)

| Library | Status | Scope |
|---|---|---|
| **Radix Primitives** (WorkOS) | Active again: releases 6 Jun, 30 Jun, 6 Jul, 20 Jul 2026 after a gap from 13 Aug 2025 [S-L08-030]. New previews: Form, One-Time Password Field, Password Toggle Field [S-L08-021] | 30 primitives + 5 utilities |
| **Base UI** (MUI) | v1.0.0 stable 11 Dec 2025; v1.8.0 on 4 Sep 2026 [S-L08-026] | 35+ unstyled components incl. Autocomplete, Combobox, Drawer, Field, Meter, Number Field, OTP Field, Toast, Toolbar |
| **React Aria** (Adobe) | Active; "over 50 components", style-free, hooks + components [S-L08-032] | Powers React Spectrum S2 |
| **Ark UI** (Chakra team) | "headless library with 45+ accessible components", React, Solid, Vue, Svelte; state-machine powered [S-L08-031] | Multi-framework |
| **shadcn/ui** (styled, copy-in) | Base UI default since July 2026; React Aria option added July 2026; Radix still supported [S-L08-020] | 64 components incl. AI chat components |

Community note: practitioners building systems with Figma MCP and Claude report "using shadcn as a reference was the best thing I did" [S-L00-043 via sources/COMMUNITY-SIGNAL.md]. That makes shadcn's inventory a sensible default seed for the builder [inferred].

## Decision Cards

### DC-L08-01: Component inventory scope
- **Block path:** Components > Inventory
- **Questions the designer answers:** Which components does the first release need? Which are core vs extended vs product-specific? Do we include AI surfaces?
- **Options:**
  - **Core (about 25):** the components in 8-10 of the 10 benchmark systems: Button, Text field, Textarea, Select, Checkbox, Radio, Switch, Slider, Tabs, Tooltip, Popover, Dialog, Menu, Progress bar, Spinner, Alert/banner, Badge, Avatar, Card, List, Table, Link, Breadcrumbs, Side navigation, Accordion [catalog matrix].
  - **Extended (about 25 more):** combobox, multi-select, date picker, file upload, toast, skeleton, empty state, drawer/sheet, pagination, tree view, segmented control, toolbar, stepper [catalog matrix].
  - **Platform-specific:** FAB, navigation rail, bottom navigation bar (mobile); UI shell, data table toolbars (enterprise) [S-L08-008] [S-L08-009].
  - **AI module:** AI label, chat message, prompt input [S-L08-009] [S-L08-018].
- **Visual effect:** a small core looks coherent but forces teams to hand-build the rest (drift); a large inventory raises maintenance cost [inferred].
- **Depends on (upstream):** product type (L06), platforms (L10), team capacity (L11).
- **Affects (downstream):** every pattern and template; documentation volume.
- **Token encoding:** component token namespaces are created per included component, for example `button.*`, `input.*` [inferred].
- **Platform notes:** Radix ships 30 primitives, shadcn 64, S2 71 nav entries, Primer 62 [S-L08-021] [S-L08-018] [S-L08-015] [S-L08-012]. HIG components are platform controls you configure rather than rebuild [S-L08-017].
- **Accessibility constraints:** each included interactive component must implement its APG pattern [S-L08-041].
- **Default + heuristic:** start with the ~25 core, add extended components when two or more products ask for them [inferred].
- **Evidence:** [S-L08-001] [S-L08-002] [S-L08-008] [S-L08-009] [S-L08-011] [S-L08-012] [S-L08-015] [S-L08-017] [S-L08-018] [S-L08-021] [S-L08-022]

### DC-L08-02: Hierarchy model and naming
- **Block path:** Components > Taxonomy
- **Questions the designer answers:** Do we name levels atoms/molecules/organisms, or primitives/components/patterns? Do we name components by what they look like or what they do?
- **Options:**
  - **Atomic design** (atoms, molecules, organisms, templates, pages) [S-L08-054].
  - **Primitives / components / patterns** (Atlassian, Radix) [S-L08-011] [S-L08-021].
  - **Foundations / components / patterns** (Carbon, HIG) [S-L08-009] [S-L08-086].
  - **Purpose categories** (M3: action, containment, communication, navigation, selection, text input) [S-L08-008].
- **Visual effect:** none directly; affects findability and consistency of names in Figma and code [inferred].
- **Depends on (upstream):** team vocabulary, tooling (L07).
- **Affects (downstream):** file/library structure, token namespaces, docs navigation.
- **Token encoding:** not a token; the chosen names become token path segments (`comp.button`, `pattern.form`) [inferred].
- **Platform notes:** names collide across systems: a "Tag" is a chip in Carbon/Fluent but a status label elsewhere; component.gallery lists Tag, Label and Chip as Badge aliases [S-L08-001].
- **Accessibility constraints:** none.
- **Default + heuristic:** tokens > primitives > components > patterns > templates, with an alias table for cross-system names (the catalog's Names lines) [inferred].
- **Evidence:** [S-L08-001] [S-L08-008] [S-L08-011] [S-L08-054] [S-L08-056] [S-L08-086]

### DC-L08-03: Build strategy (headless, styled, or native)
- **Block path:** Components > Implementation > Base library
- **Questions the designer answers:** Do we build on a headless library, fork a styled one, or use platform controls? Which headless library?
- **Options:**
  - **Headless primitives:** Radix (WorkOS), Base UI (v1 stable Dec 2025), React Aria (Adobe), Ark UI (multi-framework) [S-L08-030] [S-L08-026] [S-L08-032] [S-L08-031].
  - **Copy-in styled layer:** shadcn/ui on Base UI (default), Radix or React Aria [S-L08-020].
  - **Web components:** Polaris web components, Fluent UI Web Components v3 [S-L08-022] [S-L08-010].
  - **Native controls:** SwiftUI/UIKit and Compose Material 3 [S-L08-103] [S-L08-105].
- **Visual effect:** headless leaves every visual choice to your tokens; styled forks inherit the source's look until re-themed; native controls inherit platform look (Liquid Glass, M3) for free [inferred].
- **Depends on (upstream):** platforms and frameworks (L10), a11y bar.
- **Affects (downstream):** which composition API you expose (DC-L08-04), how states are styled, maintenance.
- **Token encoding:** headless: all component tokens are yours; native: map semantic tokens onto platform theming (M3 color roles, SwiftUI tint) [inferred].
- **Platform notes:** M3 Expressive web implementations are "unavailable" [S-L08-033]; Compose ships Expressive in alphas only [S-L00-047 via COMMUNITY-SIGNAL].
- **Accessibility constraints:** headless libraries implement APG keyboard and ARIA behavior; custom builds must do so themselves [S-L08-041] [S-L08-032].
- **Default + heuristic:** React web: shadcn on Base UI or React Aria; multi-framework: Ark UI or web components; mobile: native controls themed with your tokens [inferred].
- **Evidence:** [S-L08-020] [S-L08-021] [S-L08-026] [S-L08-030] [S-L08-031] [S-L08-032] [S-L08-033]

### DC-L08-04: Component API style (configuration vs composition)
- **Block path:** Components > API
- **Questions the designer answers:** Do consumers configure components with props, or compose them from parts? How do we let people swap the rendered element?
- **Options:** props-only configuration (Carbon, Primer, Polaris) [S-L08-064] [S-L08-068]; compound parts (Base UI, Radix) [S-L08-088]; asChild/Slot (Radix) [S-L08-087]; render prop (Base UI, React Aria) [S-L08-088] [S-L08-089]; named slots (React Aria; Figma slots property) [S-L08-089] [S-L00-045].
- **Visual effect:** configuration keeps screens uniform; composition allows richer layouts but more visual variance [inferred].
- **Depends on (upstream):** DC-L08-03.
- **Affects (downstream):** Figma component properties (variant, boolean, instance swap, slot) and Code Connect mappings (L07); docs "Props" section.
- **Token encoding:** none directly; props map to token variants (`variant=primary` selects `button.primary.*`) [inferred].
- **Platform notes:** SwiftUI and Compose favor composition with modifiers and slot lambdas [inferred].
- **Accessibility constraints:** composition must not let consumers drop required parts (labels, titles); asChild children must spread props and forward refs or ARIA wiring breaks [S-L08-087].
- **Default + heuristic:** configuration for leaf components (Button, Badge), compound parts for containers (Dialog, Menu, Card, Table) [inferred].
- **Evidence:** [S-L08-064] [S-L08-068] [S-L08-087] [S-L08-088] [S-L08-089]

### DC-L08-05: Button hierarchy (how many emphasis levels)
- **Block path:** Components > Button > Variants
- **Questions the designer answers:** How many visual emphasis levels? What are they called? Is there a special AI or promotional variant?
- **Options:**
  - **M3:** filled (default), tonal, elevated, outlined, text (5), plus toggle behavior [S-L08-033].
  - **Carbon:** primary, secondary, tertiary, ghost, danger (5) [S-L08-061].
  - **Atlassian:** default, primary, subtle, warning, danger, discovery, Rovo (7) [S-L08-063].
  - **Primer:** primary, default, invisible, danger, link (5) [S-L08-064].
  - **Spectrum 2:** accent, primary, secondary, negative, premium, genai × fill/outline [S-L08-067].
  - **Polaris:** auto, primary, secondary, tertiary × tone critical/neutral [S-L08-068].
  - **shadcn:** default, secondary, outline, ghost, destructive, link (6) [S-L08-065].
  - **HIG:** roles normal, primary, cancel, destructive; prominence through system styles [S-L08-039].
- **Visual effect:** 3 levels (solid, outline, text) read as calm and strict; 5-6 levels allow dense toolbars without shouting; accent/AI variants add a brand signature. Carbon notes secondary is "tonally heavy" and recommends tertiary/ghost when many actions share a view [S-L08-061].
- **Depends on (upstream):** color roles and brand accent (L01), elevation model (L04), product density.
- **Affects (downstream):** button group, split button, dialog footers, toolbars, empty states, forms.
- **Token encoding:** `color.action.primary.bg` (semantic) > `button.primary.container.color` (component); Carbon uses `$button-primary`, `$button-secondary`, `$button-tertiary` [S-L08-062].
- **Platform notes:** HIG: use style, not size, to mark the preferred choice [S-L08-039]; iOS 26 adds `.glass` and `.glassProminent` [S-L08-100].
- **Accessibility constraints:** M3 allows any color roles if container and label reach 3:1 [S-L08-034]; Fluent requires 4.5:1 text and 3:1 icons in all interactive states [S-L08-066].
- **Default + heuristic:** 4 levels (primary, secondary, tertiary/outline, ghost/text) plus danger; one primary per view (Carbon, Fluent) [S-L08-061] [S-L08-066].
- **Evidence:** [S-L08-033] [S-L08-034] [S-L08-039] [S-L08-061] [S-L08-062] [S-L08-063] [S-L08-064] [S-L08-065] [S-L08-066] [S-L08-067] [S-L08-068] [S-L08-100]

### DC-L08-06: Destructive action treatment
- **Block path:** Components > Button > Danger; Patterns > Destructive confirmation
- **Questions the designer answers:** Does "delete" get its own color? Solid or subtle? Do we separate "warning" from "danger"? When do we confirm?
- **Options:** solid red danger button (Carbon danger primary, Primer danger, shadcn destructive) [S-L08-061] [S-L08-064] [S-L08-065]; danger in several emphasis levels (Carbon danger primary/tertiary/ghost) [S-L08-061]; separate warning and danger (Atlassian: warning for significant change or data loss, danger for final irreversible confirmation) [S-L08-063]; tone modifier on any variant (Polaris `tone="critical"`) [S-L08-068]; role-only (HIG destructive role renders system red; never primary role) [S-L08-039].
- **Visual effect:** solid red draws the eye and can invite mis-clicks when used on the main screen; subtle red (ghost/outline) keeps lists calm and saves solid red for the final confirmation [inferred].
- **Depends on (upstream):** error/danger color role (L01), DC-L08-05.
- **Affects (downstream):** confirmation dialog, menus (destructive items), swipe actions, table batch actions.
- **Token encoding:** `color.feedback.danger.*` > `button.danger.container.color`; Carbon `$button-danger-primary`, `$button-danger-secondary`, `$button-danger-hover` [S-L08-062].
- **Platform notes:** SwiftUI `confirmationDialog` with a destructive role; UIKit `UIAlertAction.Style.destructive` [S-L08-103].
- **Accessibility constraints:** color cannot be the only signal; the label must name the action ("Delete file") [S-L08-075].
- **Default + heuristic:** subtle danger in context, solid danger only in the confirmation step; confirm only irreversible or costly actions and prefer undo [S-L08-075].
- **Evidence:** [S-L08-039] [S-L08-061] [S-L08-062] [S-L08-063] [S-L08-064] [S-L08-068] [S-L08-075] [S-L08-103]

### DC-L08-07: Control size scale and shape
- **Block path:** Components > Sizing; Foundations > Shape (L04)
- **Questions the designer answers:** How many control sizes? What heights? Pill, rounded or square corners? Does shape change on interaction?
- **Options:**
  - **M3 Expressive:** XS 32, S 40 (default), M 56, L 96, XL 136 dp; round (full) or square (12/12/16/28/28 dp); pressed shape 8/8/12/16/16 dp; toggles morph round to square when selected [S-L08-102] [S-L08-034].
  - **Carbon:** XS 24, S 32, M 40, L 48, XL 64, 2XL 80 px; sizes pair with 32/40 px inputs [S-L08-062] [S-L08-061].
  - **Primer:** small, medium, large [S-L08-064]. **S2:** S, M, L, XL [S-L08-067]. **Atlassian:** default and compact [S-L08-063].
- **Visual effect:** pill + large sizes = friendly, expressive, touch-first; small square-ish controls = dense, precise, enterprise; shape morph adds playful motion [S-L08-033] [inferred for character].
- **Depends on (upstream):** radius scale and motion (L04), spacing/density (L03), type scale (L02).
- **Affects (downstream):** all controls sharing a height (inputs, selects, buttons, segmented controls), table rows, toolbars.
- **Token encoding:** `dimension` tokens `size.control.sm|md|lg` > `button.height.md`; radius `radius.full` > `button.shape.round` [inferred]. M3 source tokens: ButtonSmallTokens.ContainerHeight = 40 dp [S-L08-102].
- **Platform notes:** HIG minimum hit region 44 × 44 pt (60 × 60 visionOS) [S-L08-039]; M3 XS/S need a 48 dp target [S-L08-034].
- **Accessibility constraints:** WCAG 2.5.8 AA 24 × 24 CSS px minimum target, 2.5.5 AAA 44 × 44 [S-L08-070].
- **Default + heuristic:** 3 sizes (32/40/48 web) with one shared height scale for all inline controls; do not mix sizes in one group [S-L08-061] [inferred for default].
- **Evidence:** [S-L08-033] [S-L08-034] [S-L08-039] [S-L08-061] [S-L08-062] [S-L08-063] [S-L08-064] [S-L08-067] [S-L08-070] [S-L08-102]

### DC-L08-08: Icon placement and content in controls
- **Block path:** Components > Button > Content
- **Questions the designer answers:** Leading or trailing icons? Icon-only allowed? How is text aligned? Casing?
- **Options:** leading icon (M3 buttons "optional leading icon", icon 20 dp) [S-L08-033]; trailing icon with left-aligned label (Carbon: label left, icon right, 16 px icon, ≥16 px label-icon gap) [S-L08-061] [S-L08-062]; both slots (Atlassian iconBefore/iconAfter, Primer leadingVisual/trailingVisual/trailingAction) [S-L08-063] [S-L08-064]; icon-only with required label (M3 icon buttons, Primer IconButton) [S-L08-008] [S-L08-012].
- **Visual effect:** leading icons aid scanning in toolbars; Carbon's trailing icon + left label gives a distinctive, editorial look; icon-only buttons make dense UIs but lower clarity [inferred].
- **Depends on (upstream):** icon set and sizes (L05), type scale (L02).
- **Affects (downstream):** menus, tabs, chips, list items (same icon slot rules).
- **Token encoding:** `button.icon.size`, `button.gap` (Carbon `$spacing-07` 32 px icon spacing) [S-L08-062].
- **Platform notes:** HIG: prefer a familiar SF Symbol or short verb label; visionOS shows tooltips on gaze [S-L08-039].
- **Accessibility constraints:** icon-only controls need an accessible name; icons 3:1 contrast [S-L08-066].
- **Default + heuristic:** optional leading icon, sentence-case verb labels (Carbon, Fluent, Atlassian all use sentence case) [S-L08-062] [S-L08-066] [S-L08-085].
- **Evidence:** [S-L08-033] [S-L08-039] [S-L08-061] [S-L08-062] [S-L08-063] [S-L08-064] [S-L08-066] [S-L08-085]

### DC-L08-09: State model (which states get distinct styling, and how)
- **Block path:** Components > States
- **Questions the designer answers:** Which states are styled? Do we use a generic overlay or a token per state? Can states combine?
- **Options:**
  - **State layers (overlay):** M3 applies a translucent layer of the content color: hover 8%, focus 10%, press 10%, drag 16% (per L01) [S-L01-005]; states inherited only by action, selection and input components; one hover and one focus at a time [S-L08-095].
  - **Explicit token per state:** Carbon defines hover, active, focus and disabled tokens per variant (`$button-primary-hover`, `$button-primary-active`, `$focus`, `$button-disabled`) [S-L08-062].
  - **Extra states:** selected (toggles, chips), loading/pending, inactive (Primer), read-only, error, dragged [S-L08-064] [S-L08-095].
- **Visual effect:** overlays give uniform, automatic states for any color (good for dynamic color and theming); explicit tokens allow tuned, brand-specific hovers but multiply token count [inferred].
- **Depends on (upstream):** color system and dark mode (L01), elevation (L04), motion (L04).
- **Affects (downstream):** every interactive component; token count; Figma variant count.
- **Token encoding:** overlay: `state.hover.opacity = 0.08` applied to `on-*` color; explicit: `button.primary.container.color.hover` (DTCG color) [inferred for names].
- **Platform notes:** touch platforms have no hover; visionOS uses gaze highlight and disallows custom hover effects on buttons [S-L08-039].
- **Accessibility constraints:** states must be perceivable at 3:1 against adjacent colors where they convey information [S-L08-071]; disabled is exempt [S-L08-071].
- **Default + heuristic:** style enabled, hover, focus-visible, pressed, selected, disabled, loading, error; use overlays for hover/press and explicit tokens for selected and error [inferred].
- **Evidence:** [S-L01-005] [S-L08-039] [S-L08-062] [S-L08-064] [S-L08-071] [S-L08-095]

### DC-L08-10: Disabled and unavailable actions
- **Block path:** Components > States > Disabled
- **Questions the designer answers:** Do we disable, hide, or keep actions pressable and explain? Do disabled controls stay focusable? Do we explain why?
- **Options:**
  - **Disable (not focusable):** M3: disabled components cannot be focused, dragged or pressed; disabled need not meet contrast [S-L08-095].
  - **Disable selectively:** Carbon disables the primary button on short forms until valid, never on long forms, and on submit to prevent duplicates [S-L08-106].
  - **Avoid disabling:** Atlassian: keep the button pressable and use validation; disabled buttons are unreachable in tab order [S-L08-085].
  - **Inactive state:** Primer: looks disabled but stays interactive; disabled "should be avoided" [S-L08-064].
  - **aria-disabled (focusable):** APG recommends aria-disabled for unavailable actions [S-L08-108]; S2 isPending keeps focus [S-L08-067].
  - **Hide:** M3: if the FAB's action is unavailable, do not show the FAB [S-L08-095].
  - **Explain via tooltip:** Fluent yes [S-L08-066]; Atlassian never [S-L08-085].
- **Visual effect:** faded controls signal "not now" and reduce visual noise but can hide why; always-enabled buttons look cleaner but produce more error states [inferred].
- **Depends on (upstream):** validation strategy (DC-L08-17), color system.
- **Affects (downstream):** forms, wizards, toolbars, table batch actions.
- **Token encoding:** `color.text.disabled`, `color.bg.disabled`, or `state.disabled.opacity` (M3 uses opacity on content/container [inferred]); Carbon `$text-on-color-disabled`, `$button-disabled` [S-L08-062].
- **Platform notes:** native disabled controls are not focusable on iOS/Android by default [inferred].
- **Accessibility constraints:** WCAG exempts inactive components from 1.4.3 and 1.4.11 contrast [S-L08-071], but unreachable controls hide information from keyboard and screen-reader users [S-L08-085].
- **Default + heuristic:** do not disable submit buttons; validate on submit and explain. Use aria-disabled (focusable) with visible helper text when an action truly cannot run [S-L08-085] [S-L08-108] [inferred for combination].
- **Evidence:** [S-L08-062] [S-L08-064] [S-L08-066] [S-L08-067] [S-L08-071] [S-L08-085] [S-L08-095] [S-L08-106] [S-L08-108]

### DC-L08-11: Focus indicator style
- **Block path:** Components > States > Focus-visible
- **Questions the designer answers:** Outline ring, inset border, or color change? What color and width? Offset or inset? Keyboard-only?
- **Options:** ring-like keyboard focus indicator shown on Tab (M3) [S-L08-095]; inset border using `$focus` + `$focus-inset` (Carbon; 1 px inset box-shadow in structure specs) [S-L08-062]; shared focus primitive (Atlassian Focusable, replacing the deprecated Focus ring) [S-L08-093]; browser default [inferred].
- **Visual effect:** outer rings are obvious and friendly; inset borders keep layouts tight in dense grids and tables; brand-colored rings add identity but can vanish on brand surfaces [inferred].
- **Depends on (upstream):** color roles and contrast (L01), radius (ring follows shape).
- **Affects (downstream):** every interactive component, including custom ones.
- **Token encoding:** `focus.ring.color`, `focus.ring.width` (dimension), `focus.ring.offset`; Carbon `$focus`, `$focus-inset` [S-L08-062] [inferred for generic names].
- **Platform notes:** iOS/Android rely on system focus for keyboards and switch control; web needs `:focus-visible` [inferred].
- **Accessibility constraints:** 2.4.7 Focus Visible is AA [S-L08-072]; 2.4.13 Focus Appearance AAA requires an indicator at least as large as a 2 CSS px perimeter with 3:1 change [S-L08-069]; 1.4.11 needs 3:1 against adjacent colors [S-L08-071].
- **Default + heuristic:** 2 px solid ring, 2 px offset, a color that is 3:1 on every surface (often a two-tone ring: inner white + outer dark) [S-L08-069] [inferred for two-tone].
- **Evidence:** [S-L08-062] [S-L08-069] [S-L08-071] [S-L08-072] [S-L08-093] [S-L08-095]

### DC-L08-12: Loading behavior
- **Block path:** Components > States > Loading; Patterns > Loading states
- **Questions the designer answers:** Spinner, skeleton or progress bar? Does a loading button stay focusable? Is there a delay before showing a spinner?
- **Options:** in-button spinner that disables the button (Carbon inline loading) [S-L08-061]; pending state that keeps focus and shows a spinner after 1 s (S2) [S-L08-067]; spinner with aria-disabled (Primer loading) [S-L08-064]; M3 loading indicator for waits under 5 s, contained or not [S-L08-038]; skeleton for full-page loads, progress bar over 10 s, nothing under 1 s [S-L08-074].
- **Visual effect:** skeletons make pages feel faster and preview layout; spinners are compact but draw attention; M3's shape-morphing indicator is deliberately expressive [S-L08-074] [S-L08-038].
- **Depends on (upstream):** motion system and reduced-motion policy (L04).
- **Affects (downstream):** buttons, tables, cards, pages, pull-to-refresh.
- **Token encoding:** `motion.duration.*`, `loading.delay = 1000ms` (duration), skeleton fill color [inferred].
- **Platform notes:** HIG: show something as soon as possible; let people keep working while content loads [S-L08-086]; UIKit UIRefreshControl, Compose LoadingIndicator [S-L08-103] [S-L08-105].
- **Accessibility constraints:** announce state changes (4.1.3 status messages) and keep focus stable [S-L08-098] [inferred].
- **Default + heuristic:** delay spinners about 1 s; skeletons for first page load; keep loading buttons focusable [S-L08-067] [S-L08-074].
- **Evidence:** [S-L08-038] [S-L08-061] [S-L08-064] [S-L08-067] [S-L08-074] [S-L08-086]

### DC-L08-13: Density modes
- **Block path:** Components > Density; Foundations > Space (L03)
- **Questions the designer answers:** One density or several? Which components get a compact mode? How do row heights scale?
- **Options:** fixed size scale with per-context pairing (Carbon buttons 24-80 px, data table rows XS 24 to XL 64 px, toolbars paired to row size) [S-L08-062] [S-L08-092]; binary spacing prop (Atlassian `spacing="compact"` for tables and dense layouts) [S-L08-063]; user-selectable density [inferred]; platform-driven density (S2 components scale for touch vs pointer) [S-L08-015].
- **Visual effect:** compact = more data per screen, enterprise and pro-tool feel; comfortable = calmer, touch-friendly, consumer feel [inferred].
- **Depends on (upstream):** spacing scale and base unit (L03), type scale (body 14 vs 16 px, per L02 cross-lane note), target-size rules.
- **Affects (downstream):** table, list, menu, tree, input and button heights; toolbar heights.
- **Token encoding:** a density mode on a variable collection, for example `density: compact|default` switching `size.control.md` 32 ↔ 40 px [inferred]; Carbon row-height sizes xs-xl [S-L08-092].
- **Platform notes:** mobile rarely offers compact; desktop pro tools and admin panels do [inferred].
- **Accessibility constraints:** compact targets must still meet 24 × 24 CSS px (2.5.8) or spacing exceptions [S-L08-070].
- **Default + heuristic:** default + compact modes; apply compact only to data-heavy components (tables, lists, menus, trees) [S-L08-063] [inferred].
- **Evidence:** [S-L08-015] [S-L08-062] [S-L08-063] [S-L08-070] [S-L08-092]

### DC-L08-14: Selected and active state treatment
- **Block path:** Components > States > Selected
- **Questions the designer answers:** How do we show the current tab, nav item, chip or toggle? Color fill, indicator, shape change, or neutral?
- **Options:** pill-shaped active indicator behind icon (M3 navigation bar/rail) [S-L08-083] [S-L08-080]; shape morph round to square on selected toggles (M3 Expressive) [S-L08-034]; neutral (non-brand) selected treatment (Atlassian, behind a feature flag) [S-L08-085]; underline indicator (Primer UnderlineNav/UnderlinePanels) [S-L08-012]; filled selected container (M3 toggle selected uses primary/on-primary) [S-L08-034].
- **Visual effect:** brand-colored selection = lively, branded; neutral selection = calmer, lets brand color mean "action" only; indicators with motion feel responsive [inferred].
- **Depends on (upstream):** color roles (L01), motion (L04), DC-L08-05.
- **Affects (downstream):** tabs, navigation, chips, segmented controls, list/table selection, calendars.
- **Token encoding:** `color.selected.bg`, `color.selected.fg`, `indicator.shape` [inferred]; M3 navigation active label changed from on-surface-variant to secondary in May 2025 [S-L08-083].
- **Platform notes:** HIG tab bars and sidebars tint the selected item with the accent color [inferred].
- **Accessibility constraints:** selection must not rely on color alone (use shape, weight, indicator) and needs 3:1 where it conveys state [S-L08-071]; expose aria-selected/aria-current/aria-pressed [S-L08-042] [S-L08-108].
- **Default + heuristic:** indicator + color, never color alone; reserve brand primary for actions if the product is action-dense [inferred].
- **Evidence:** [S-L08-012] [S-L08-034] [S-L08-042] [S-L08-071] [S-L08-080] [S-L08-083] [S-L08-085] [S-L08-108]

### DC-L08-15: Container separation for cards and panels
- **Block path:** Components > Card; Foundations > Elevation (L04)
- **Questions the designer answers:** Do cards float (shadow), sit outlined, or use a tinted fill? Is the whole card clickable?
- **Options:** M3 elevated, filled, outlined cards (Compose Card, ElevatedCard, OutlinedCard) [S-L08-105]; Carbon tiles on layered backgrounds [S-L08-009]; Polaris Section/Box [S-L08-022].
- **Visual effect:** shadow = depth and tactility; outline = crisp, flat, technical; tinted fill = soft, modern, works in dark mode without shadows [inferred].
- **Depends on (upstream):** elevation and shadow tokens (L04), surface layering model (L01), radius.
- **Affects (downstream):** cards, tiles, popovers, dialogs, list containers, dashboards.
- **Token encoding:** `surface.container.*` color roles, `elevation.level1` (shadow), `border.subtle` [inferred].
- **Platform notes:** iOS content layer uses standard materials; Liquid Glass is reserved for the control layer (per L00) [S-L00-049 via COMMUNITY-SIGNAL].
- **Accessibility constraints:** if a border is the only boundary of an interactive card, it needs 3:1 (1.4.11) [S-L08-071].
- **Default + heuristic:** tinted fill or outline for static cards, elevation only for things that float (menus, dialogs) [inferred].
- **Evidence:** [S-L08-009] [S-L08-022] [S-L08-071] [S-L08-105]

### DC-L08-16: Form field style and label placement
- **Block path:** Components > Text field; Patterns > Forms
- **Questions the designer answers:** Filled, outlined or underlined fields? Where do labels go? How do we mark required vs optional?
- **Options:** M3 filled vs outlined text fields [S-L08-105]; top-aligned labels (Carbon's only option) [S-L08-106]; mark the minority case with "(optional)" or "(required)" [S-L08-106]; 1-3 word labels, no colons, sentence case [S-L08-106].
- **Visual effect:** filled = soft, app-like; outlined = crisp, form-heavy, enterprise; underline = minimal but low affordance [inferred].
- **Depends on (upstream):** radius, surface colors, type roles, density.
- **Affects (downstream):** all inputs (select, combobox, date, number, search, textarea), form layouts.
- **Token encoding:** `input.container.color`, `input.border.color.{default,hover,focus,error}`, `input.label.typography` [inferred].
- **Platform notes:** iOS forms use grouped lists with inline labels; Android follows M3 fields [inferred].
- **Accessibility constraints:** every input needs a programmatic label; placeholders are not labels; borders need 3:1 [S-L08-071] [inferred for placeholder rule].
- **Default + heuristic:** outlined fields with top labels for web products; mark whichever of required/optional is rarer [S-L08-106].
- **Evidence:** [S-L08-071] [S-L08-105] [S-L08-106]

### DC-L08-17: Validation timing and error presentation
- **Block path:** Patterns > Forms > Validation
- **Questions the designer answers:** Validate on submit, on blur, or while typing? Error summary or inline only? Do we disable submit?
- **Options:** validate on submit, error summary at top with focus, "Error:" title prefix, inline messages (GOV.UK) [S-L08-077]; inline notification plus inline errors; disable submit on short forms only (Carbon) [S-L08-106]; never disable submit, explain instead (Atlassian) [S-L08-085].
- **Visual effect:** on-submit keeps the form calm while filling; live validation gives instant feedback but can feel naggy; summaries add a red block that orients long forms [inferred].
- **Depends on (upstream):** DC-L08-10, error color role, content guidelines (L06).
- **Affects (downstream):** text fields, checkboxes, selects, alert/banner, dialogs.
- **Token encoding:** `color.feedback.error.*`, `input.border.color.error`, `field.message.typography` [inferred].
- **Platform notes:** GOV.UK turns off browser validation (`novalidate`) for consistent messages [S-L08-077].
- **Accessibility constraints:** errors identified in text (WCAG 3.3.1) and associated with fields; move focus to the summary [S-L08-077] [inferred for 3.3.1 citation].
- **Default + heuristic:** validate on submit (and on blur only for format checks research supports), summary + inline for forms over about 5 fields [S-L08-077] [inferred threshold].
- **Evidence:** [S-L08-077] [S-L08-085] [S-L08-106]

### DC-L08-18: Feedback and notification model
- **Block path:** Patterns > Notifications; Components > Toast, Banner, Alert
- **Questions the designer answers:** Do we use toasts? What persists and what auto-dismisses? How many statuses?
- **Options:** Carbon matrix of 4 statuses (info blue, success green, warning yellow, error red) × 7 types (inline, toast, actionable, callout, banner, notification panel, modal) [S-L08-079]; M3 snackbar [S-L08-008]; Atlassian flags (often in a flag group) [S-L08-011]; no toasts, use banners/dialogs (Primer) [S-L08-098]; HIG: match delivery to significance, use multiple modalities (color, text, sound, haptics) [S-L08-086].
- **Visual effect:** toasts keep layouts still but flash and vanish; banners shift layout but persist and are findable [inferred].
- **Depends on (upstream):** status color roles (L01), iconography (L05), motion durations (L04), voice (L06).
- **Affects (downstream):** alert, toast, banner, dialog, form validation, empty/error states.
- **Token encoding:** `color.feedback.{info,success,warning,error}.{bg,fg,border,icon}`, `toast.duration` [inferred].
- **Platform notes:** iOS uses system notifications and in-place status rather than toasts; Android has snackbars [S-L08-017] [S-L08-105].
- **Accessibility constraints:** auto-dismiss risks WCAG 2.2.1 and 2.2.3; use live regions (4.1.3) without stealing focus [S-L08-098] [S-L08-116].
- **Default + heuristic:** 4 statuses; inline or banner by default; toasts only for low-stakes confirmations with an undo, and never auto-dismiss toasts that contain actions [S-L08-079] [S-L08-098].
- **Evidence:** [S-L08-008] [S-L08-011] [S-L08-017] [S-L08-079] [S-L08-086] [S-L08-098] [S-L08-116]

### DC-L08-19: Navigation model by screen size
- **Block path:** Patterns > Navigation
- **Questions the designer answers:** Bottom bar, rail, sidebar, top nav or tabs? How many destinations? What changes at each breakpoint?
- **Options:** M3: navigation bar for compact/medium (3-5 destinations), collapsed rail for medium+ (3-7 plus FAB), expanded rail replacing the drawer [S-L08-083] [S-L08-080] [S-L08-082]; iOS 26: floating tab bar that can minimize on scroll and hold a search tab; sidebar-adaptable tab views on iPad [S-L08-040] [S-L08-103]; web sidebars (Fluent Nav, Carbon UI shell, Primer NavList, S2 SideNav, shadcn Sidebar) [S-L08-010] [S-L08-009] [S-L08-012] [S-L08-027] [S-L08-018]; tabs for sibling views inside a page [S-L08-042].
- **Visual effect:** bottom bars feel mobile-native; rails keep content wide on tablets; sidebars signal a tool with many areas; top nav suits marketing sites [inferred].
- **Depends on (upstream):** breakpoints and window classes (L03), IA depth, platforms (L10).
- **Affects (downstream):** app shell template, page header, search placement, FAB placement.
- **Token encoding:** `nav.rail.width.collapsed|expanded`, `nav.bar.height`, `nav.indicator.*` [inferred].
- **Platform notes:** M3 says do not show a toolbar together with a navigation bar [S-L08-037].
- **Accessibility constraints:** navigation uses links and landmarks, not the menu role [S-L08-112]; mark current item with aria-current [inferred].
- **Default + heuristic:** 3-5 top destinations: bottom bar (phone) → rail (tablet) → sidebar (desktop); more than 7: sidebar with groups [S-L08-083] [S-L08-080].
- **Evidence:** [S-L08-009] [S-L08-010] [S-L08-012] [S-L08-018] [S-L08-027] [S-L08-037] [S-L08-040] [S-L08-080] [S-L08-082] [S-L08-083] [S-L08-103] [S-L08-112]

### DC-L08-20: Overlay model (dialog, sheet, popover)
- **Block path:** Patterns > Modality; Components > Dialog, Sheet, Popover
- **Questions the designer answers:** When is something modal? Dialog or side sheet or bottom sheet? Where do the buttons go?
- **Options:** HIG: present modally only with a clear benefit; sheets and popovers for scoped tasks; full-screen for immersive multi-step tasks [S-L08-086]; M3 bottom and side sheets [S-L08-008]; Fluent Drawer, Atlassian Drawer/Panel [S-L08-010] [S-L08-011]; M3 "levitate" layered panes for focused tasks (basket, comments, event creation) [S-L08-096].
- **Button order:** iOS sheets put Cancel on the leading edge and Done on the trailing edge, never all of Cancel/Done/Back together [S-L08-040]; Carbon puts the primary button on the outside of a group [S-L08-062]; Fluent puts the primary on top or to the left (right in RTL) [S-L08-066].
- **Visual effect:** centered dialogs interrupt strongly; side sheets keep context visible; popovers feel lightweight [inferred].
- **Depends on (upstream):** navigation model, breakpoints, elevation/scrim (L04).
- **Affects (downstream):** confirmation, forms in overlays, filters panels, detail views.
- **Token encoding:** `scrim.color`, `dialog.radius`, `sheet.radius.top`, `overlay.elevation` [inferred].
- **Platform notes:** iOS resizable sheets use detents and a grabber [S-L08-040].
- **Accessibility constraints:** focus trapped and returned; Escape closes; aria-modal [S-L08-043].
- **Default + heuristic:** dialog for short decisions, side sheet for editing with context, bottom sheet on phones; follow the platform's button order per platform [S-L08-040] [S-L08-066] [inferred].
- **Evidence:** [S-L08-008] [S-L08-010] [S-L08-011] [S-L08-040] [S-L08-043] [S-L08-062] [S-L08-066] [S-L08-086] [S-L08-096]

### DC-L08-21: Long collections (pagination, load more, infinite scroll)
- **Block path:** Patterns > Collections
- **Questions the designer answers:** How do people move through long lists? Numbered pages, a Load more button, or infinite scroll?
- **Options:** pagination (Carbon, Atlassian, Primer, shadcn) [catalog C30]; Load more; integrated pagination; infinite scroll for homogeneous feeds [S-L08-073].
- **Visual effect:** pagination feels orderly and gives landmarks; infinite scroll feels fluid and endless; Load more is a middle path that keeps the footer reachable [S-L08-073].
- **Depends on (upstream):** content type and user goal (browse vs find/compare).
- **Affects (downstream):** tables, lists, search results, feeds, footer reachability.
- **Token encoding:** none; pagination consumes button/link tokens [inferred].
- **Platform notes:** mobile feeds default to continuous scroll; HIG page controls are for paged views, not data sets [S-L08-017] [inferred].
- **Accessibility constraints:** infinite scroll harms keyboard and footer access; APG Feed pattern exists for accessible infinite lists [S-L08-073] [S-L08-041].
- **Default + heuristic:** pagination for tables and goal-directed search; Load more for results lists; infinite scroll only for feeds [S-L08-073].
- **Evidence:** [S-L08-017] [S-L08-041] [S-L08-073]

### DC-L08-22: AI surfaces module
- **Block path:** Components > AI
- **Questions the designer answers:** Do we mark AI-generated content? Do AI actions get their own visual variant? Do we ship chat components?
- **Options:** AI label/indicator (Carbon AI label; AI presence in data tables) [S-L08-009] [S-L08-092]; dedicated AI button variant (S2 `genai`, `premium`; Atlassian Rovo) [S-L08-067] [S-L08-063]; chat components (shadcn Message, Bubble, Message Scroller, Attachment, Marker; Questionnaire Aug 2026) [S-L08-018] [S-L08-020]; S2 AI Components preview (1 Sep 2026) [S-L08-027].
- **Visual effect:** a distinct AI accent (often gradient) makes AI features recognizable but can compete with the primary action color [inferred].
- **Depends on (upstream):** brand color and accent (L01, L06), iconography (L05).
- **Affects (downstream):** buttons, badges, tables, empty states, chat layouts.
- **Token encoding:** `color.ai.*` accent or gradient tokens (DTCG has no gradient composite type per L07 notes; verify) [inferred].
- **Platform notes:** none of the native platforms in this set define an AI control in the HIG component index [S-L08-017].
- **Accessibility constraints:** streaming content should use polite live regions; disclose AI generation in text, not color only [inferred].
- **Default + heuristic:** make it an optional module: AI label + AI button variant first, chat components only for conversational products [inferred].
- **Evidence:** [S-L08-009] [S-L08-017] [S-L08-018] [S-L08-020] [S-L08-027] [S-L08-063] [S-L08-067] [S-L08-092]

### DC-L08-23: Component documentation template
- **Block path:** Documentation > Component page
- **Questions the designer answers:** What sections does every component page have? Who is it for: designers, engineers, agents?
- **Options:**
  - **M3:** tabs Overview, Specs, Guidelines, Accessibility; Specs holds variants, configurations, tokens, anatomy, color, states, measurements [S-L08-033] [S-L08-034].
  - **Carbon:** tabs Usage, Style, Code, Accessibility; Usage covers live demo, accessibility testing status, overview (when to use/not), formatting (anatomy, sizes, emphasis, alignment), content, universal behaviors (states, interactions, loading), per-variant guidance, modifiers, related, references; Style holds per-state color token tables, typography, structure, size [S-L08-061] [S-L08-062].
  - **Atlassian:** tabs Examples, Code, Usage, Changelog; Usage covers parts, accessibility, best practices, content guidelines, related [S-L08-085].
  - **Fluent:** usage page with types, behavior, layout, accessibility, content [S-L08-066].
  - **Primer:** React examples by variant and state plus Props table [S-L08-084].
  - **EightShapes spec:** anatomy, properties, layout and spacing (automatable), plus accessibility, behavior and motion written by hand [S-L08-060].
- **Visual effect:** none on the product; better docs reduce drift [inferred].
- **Depends on (upstream):** DC-L08-01, DC-L08-04; governance (L11).
- **Affects (downstream):** adoption, AI-agent success. L00 reports Sanity's evals: rewriting docs for agents raised agent build success from 20% to 90% (Sonnet) and JSON-structured docs beat Markdown [S-L00-036 via COMMUNITY-SIGNAL].
- **Token encoding:** the Style/Specs section is generated from component tokens [inferred].
- **Platform notes:** add per-platform native mappings (SwiftUI/Compose) when shipping mobile [inferred].
- **Accessibility constraints:** each page states its APG pattern, keyboard map, and test status (Carbon shows default state, advanced states, screen reader, keyboard) [S-L08-061].
- **Default + heuristic:** see "How to document a component" below for the generated template.
- **Evidence:** [S-L08-033] [S-L08-034] [S-L08-060] [S-L08-061] [S-L08-062] [S-L08-066] [S-L08-084] [S-L08-085]

## Component-level decisions at a glance
The brief's list of component decisions, each with the option space and its visual effect (details in the cards).

| Decision | Typical options | Visual effect | Card |
|---|---|---|---|
| How many button variants | 3 (solid, outline, text) · 4-5 (+tonal/secondary, ghost) · 6-7 (+warning, discovery, AI) | fewer = calmer and stricter; more = flexible dense toolbars, risk of muddled hierarchy | DC-L08-05 |
| Which states get distinct styling | overlay layers vs explicit per-state tokens; add selected, loading, inactive, error | overlays = uniform and theme-proof; explicit = tuned brand feel, more tokens | DC-L08-09 |
| Disabled approach | disable · aria-disabled + explain · inactive · hide | faded = quiet but opaque; enabled + errors = clearer, more red on screen | DC-L08-10 |
| Focus indicator | outer ring · inset border · two-tone ring | ring = obvious; inset = tight grids; two-tone = works on any surface | DC-L08-11 |
| Icon placement | leading · trailing (Carbon) · both · icon-only | leading aids scanning; trailing + left label = editorial Carbon look | DC-L08-08 |
| Sizes and density | 3-7 heights; compact mode | large/pill = friendly, touch; small/square = dense, pro | DC-L08-07, DC-L08-13 |
| Loading behavior | in-button spinner · pending with delay · skeleton · progress bar | skeleton feels faster; spinner compact; expressive indicator adds personality | DC-L08-12 |
| Destructive actions | solid danger · subtle danger · warning vs danger · role only | solid red alarms; subtle keeps lists calm | DC-L08-06 |
| Selected state | brand fill · neutral · indicator pill · underline · shape morph | brand = lively; neutral = calm, keeps brand for actions | DC-L08-14 |
| Card separation | elevation · outline · tinted fill | depth vs flat-technical vs soft-modern | DC-L08-15 |

## Patterns
Each pattern lists the building blocks (catalog IDs) it composes and the decisions it raises.

### P1 Forms and validation
- **Blocks:** C21 Form field, C10-C20 inputs, C23-C26 selection controls, C01 Button, C37 Alert (error summary), C36 Steps (long forms).
- **Key decisions:** label placement and required/optional marking (DC-L08-16); validation timing and summary (DC-L08-17); disabled submit (DC-L08-10); one column vs multi-column [inferred].
- **Evidence-backed rules:** validate on submit, show an error summary with focus and an "Error:" title prefix [S-L08-077]; top-aligned labels, 1-3 words, mark the minority case [S-L08-106]; do not disable long-form submit buttons; disable on submit to prevent duplicates [S-L08-106]. HIG: pre-fill from the system, use secure fields, support all input methods [S-L08-086].

### P2 Navigation (top, bottom, side, rail, tabs)
- **Blocks:** C31 Navigation bar, C32 Rail, C33 Sidebar, C34 App bar/header, C28 Tabs, C29 Breadcrumbs, C09 Link, C13 Search.
- **Key decisions:** model by breakpoint and destination count (DC-L08-19); selected-state treatment (DC-L08-14); where search lives (iOS search tab, M3 search bar) [S-L08-040] [S-L08-008].
- **Rules:** M3 bar 3-5 destinations (compact/medium), rail 3-7 (medium+), expanded rail replaces drawer [S-L08-083] [S-L08-080] [S-L08-082]; do not use the menu role for site navigation [S-L08-112].

### P3 Search and filtering
- **Blocks:** C13 Search field, C15 Combobox (suggestions), C27 Chips (applied filters), C14/C16 selects, C23/C24 checkbox/radio sets, C49 Sheet (filter panel on mobile), C42 Empty state (no results), C57 Table / C56 List.
- **Key decisions:** single vs multi-select filters; batch apply vs instant update; where filters live (left rail, toolbar, sheet); reset behavior [S-L08-107]. Search scope and suggestions/recents [S-L08-086].
- **Rules:** Carbon selection methods: single, multi, multiple categories, batch updates, instant updates [S-L08-107]; HIG: one clearly identified search location; search as a tab when it is central [S-L08-086].

### P4 Onboarding
- **Blocks:** C47 Dialog or full-screen flow, C36 Steps, C55 Carousel (intro cards), C45/C46 Tooltip/Popover (coach marks), C42 Empty state (first use), C37 Banner.
- **Key decisions:** upfront tour vs contextual tips; skippable; interactive practice.
- **Rules:** HIG: teach through interactivity, prefer context-specific tips over one flow, keep any required flow brief and optional-feeling [S-L08-086]. Atlassian deprecated its multi-step "Onboarding (spotlight)" and now lists a Spotlight component for focusing attention on one element [S-L08-011]. Empty states double as first-use onboarding [S-L08-078].

### P5 Empty, loading and error states
- **Blocks:** C42 Empty state, C41 Skeleton, C40 Spinner, C39 Progress bar, C37 Alert/banner, C01 Button (retry).
- **Key decisions:** loading indicator by wait time (DC-L08-12); empty-state tone and illustration (L05/L06).
- **Rules:** <1 s nothing, 2-10 s skeleton (page) or spinner (module), >10 s progress bar [S-L08-074]; empty states give status, a learning cue and a direct action; types first-use, user-cleared, no-results [S-L08-078]; HIG: show something as soon as possible [S-L08-086].

### P6 Notifications
- **Blocks:** C37 Alert/banner, C38 Toast, C43 Badge (unread counts), C47 Dialog (critical), notification panel (drawer or popover) [S-L08-079].
- **Key decisions:** feedback model (DC-L08-18): which status × type for which event; task- vs system-generated.
- **Rules:** Carbon: relevant, timely, informative; task-generated messages near the task, system-generated as banners or panel [S-L08-079]; Primer: no toasts [S-L08-098]; APG Alert: live region, no focus move, no auto-disappear [S-L08-116].

### P7 Authentication (sign in, sign up, verification)
- **Blocks:** C10 Text field (email, password with reveal toggle), C20 OTP input, C21 Form field, C01 Button, C37 Alert, C09 Link (forgot password).
- **Key decisions:** passwordless vs password; show-password toggle; one-time codes; social sign-in buttons [inferred].
- **Rules:** WCAG 3.3.8 (AA): no cognitive function test unless there is an alternative or a mechanism such as password managers or copy-paste [S-L08-090]; Radix now ships Password Toggle Field and One-Time Password Field previews [S-L08-021]; HIG has a "Managing accounts" pattern [S-L08-086]; use secure text fields [S-L08-086].

### P8 Data tables
- **Blocks:** C57 Table, C08 Toolbar (search, filters, batch actions), C23 Checkbox (selection), C50 Menu (row overflow), C30 Pagination, C41 Skeleton, C42 Empty state, C53 expandable rows.
- **Key decisions:** row density (DC-L08-13); zebra striping; sticky header; inline vs batch actions; pagination vs scroll (DC-L08-21).
- **Rules:** Carbon rows XS 24 to XL 64 px, header matches rows, toolbar paired to row size; features expandable, selectable, batch actions, inline actions, overflow menu, sorting, search, loading, zebra, AI presence [S-L08-092]; APG Grid for interactive tables, Table for static [S-L08-051].

### P9 Settings
- **Blocks:** C56 List (grouped rows), C25 Switch, C14 Select, C24 Radio group, C33 Sidebar or C28 Tabs (sections), C13 Search (large settings), C48 Confirmation dialog (resets).
- **Key decisions:** immediate apply (switches) vs save button; grouping; searchable settings [inferred].
- **Rules:** HIG: choose defaults that suit most people, minimize the number of settings, put task-specific options inside the task, use the system Settings app for system-level permissions [S-L08-086]; Fluent: switches for immediate changes [S-L08-066].

### P10 Feedback and confirmation
- **Blocks:** C38 Toast / C37 inline message, C40 Spinner, C01 Button (undo), C43 Badge.
- **Key decisions:** confirm success at all? inline vs toast; undo.
- **Rules:** HIG: match the significance of feedback to its delivery; integrate status near the item; use several modalities [S-L08-086]; Primer: self-evident successes need no message [S-L08-098].

### P11 Destructive confirmations
- **Blocks:** C48 Confirmation dialog, C01 Button (danger), C38 Toast with undo, C10 Text field (type-to-confirm).
- **Key decisions:** confirm vs undo; severity tiers (warning vs danger) (DC-L08-06).
- **Rules:** confirm only serious or irreversible actions; specific verb labels; offer undo; type-to-confirm for rare severe actions [S-L08-075]; never make the destructive button the primary/default [S-L08-039]; alertdialog semantics [S-L08-114].

### P12 Pagination vs infinite scroll
- **Blocks:** C30 Pagination, C01 Button (Load more), C40 Spinner, C56/C57 collections.
- **Key decisions:** DC-L08-21.
- **Rules:** infinite scroll for homogeneous browsing feeds; pagination or Load more for goal-directed finding and comparison; infinite scroll hides the footer and hurts refinding [S-L08-073].

### P13 Progressive disclosure
- **Blocks:** C53 Accordion/disclosure, C45 Toggletip, C46 Popover, C49 Sheet, C28 Tabs, "Show more" buttons, C36 Steps (staged disclosure).
- **Key decisions:** what is primary vs secondary; how many levels.
- **Rules:** show the few important options first and defer specialized ones; staged disclosure for linear tasks; more than two levels usually hurts usability [S-L08-076] (NN/g, 2006; evergreen, Tier B). Primer recommends progressive disclosure as a toast alternative for complex results [S-L08-098].

## Templates and page layouts (summary)
| Template | Building blocks | Key decisions | Evidence |
|---|---|---|---|
| **Dashboard** | C63 app shell, C33 sidebar, C34 header, C52 cards (KPI tiles), charts (L05), C57 table, C62 grid | card separation (DC-L08-15), density (DC-L08-13), grid columns (L03) | M3 feed layout arranges cards in a configurable grid [S-L08-096] [inferred for dashboard mapping] |
| **List / index page** | C34 page header with primary action, C08 toolbar (search/filter), C57 table or C56 list, C30 pagination, C42 empty state | pagination vs scroll (DC-L08-21), filters (P3) | Carbon data table [S-L08-092]; Carbon filtering [S-L08-107] |
| **Detail page** | page header (title, breadcrumbs, actions), tabs, content sections, supporting pane (metadata, activity) | list-detail vs full page; supporting pane about 1/3 | M3 list-detail and supporting pane (primary ≈ 2/3) [S-L08-096]; Primer SplitPageLayout [S-L08-012] |
| **Settings** | C33 sidebar or C28 tabs for sections, C56 grouped lists, switches/selects, save bar | immediate vs explicit save (P9) | HIG Settings [S-L08-086] |
| **Marketing / landing** | header with top nav, hero, feature cards, testimonials, CTA buttons, footer | expressive type and imagery (L02, L05, L06); component.gallery tracks Hero (9 examples), Header (38), Footer (19), Quote (11) [S-L08-001] | [S-L08-001] |

Product systems (Carbon UI shell, Atlassian Page and Navigation system, Polaris Page, Primer PageLayout) ship the shell as components [S-L08-009] [S-L08-011] [S-L08-022] [S-L08-012]; marketing templates mostly live outside product design systems (component.gallery's Hero has only 9 examples) [S-L08-001] [inferred interpretation].

## How to document a component (template the builder can generate)
Synthesized from M3, Carbon, Atlassian, Fluent, Primer and EightShapes [S-L08-033] [S-L08-034] [S-L08-060] [S-L08-061] [S-L08-062] [S-L08-066] [S-L08-084] [S-L08-085]:
1. **Header:** name, one-line purpose, status (alpha/beta/stable/deprecated, as Atlassian and Radix label them) [S-L08-011] [S-L08-021], links to code, Figma, storybook.
2. **Live example / playground** (Carbon live demo, Primer React examples) [S-L08-061] [S-L08-084].
3. **Usage:** when to use, when not to use, related components (Carbon Overview + Related) [S-L08-061].
4. **Anatomy:** numbered diagram of parts (M3 container/label/icon; Carbon A/B/C) [S-L08-034] [S-L08-061]; auto-generated from layers (EightShapes) [S-L08-060].
5. **Variants and properties:** each prop with default vs alternatives (EightShapes "Properties") [S-L08-060].
6. **States:** enabled, hover, focus, pressed, selected, disabled, loading, error, shown per variant (M3 and Carbon state grids) [S-L08-034] [S-L08-062].
7. **Specs / redlines:** sizes, padding, spacing, radius, typography with token names (Carbon Style tab tables; EightShapes layout and spacing) [S-L08-062] [S-L08-060].
8. **Behavior and motion:** interactions, responsive behavior, loading, motion (Carbon "Universal behaviors"; EightShapes manual sections) [S-L08-061] [S-L08-060].
9. **Content guidelines:** label rules, casing, length (Atlassian, Fluent) [S-L08-085] [S-L08-066].
10. **Do / Don't** pairs with images (Carbon, Atlassian) [S-L08-061] [S-L08-085].
11. **Accessibility:** APG pattern, keyboard map, ARIA, contrast notes, test status (Carbon testing status block) [S-L08-061] [S-L08-041].
12. **Code:** API/props table, examples, platform mappings (Primer Props; SwiftUI/Compose names from the catalog) [S-L08-084].
13. **Changelog** (Atlassian tab) [S-L08-085].
14. **Machine-readable twin:** the same content as structured JSON for agents; L00 reports JSON-structured docs outperformed Markdown in Sanity's agent evals [S-L00-036 via COMMUNITY-SIGNAL].

## Cross-lane notes
- [L08 -> L01] Component state colors depend on the state model choice (DC-L08-09): M3 overlays at 8/10/10/16% vs Carbon explicit hover/active tokens. Button color roles per M3 style are listed in S-L08-034 (elevated = surface container low + primary; tonal = secondary container).
- [L08 -> L02] Button labels: Carbon body-compact-01 (14 px, 400) and body-compact-02 (16 px) for expressive buttons [S-L08-062]; sentence case in Carbon, Fluent and Atlassian.
- [L08 -> L03] Control height scales: M3 32/40/56/96/136 dp, Carbon 24/32/40/48/64/80 px, data table rows 24-64 px [S-L08-102] [S-L08-062] [S-L08-092]. Navigation switches at M3 compact/medium/expanded breakpoints [S-L08-083].
- [L08 -> L04] M3 Expressive shape morph: square button corners 12/12/16/28/28 dp, pressed 8/8/12/16/16 dp; selected toggles morph round to square [S-L08-034]. Loading indicator uses shape + motion [S-L08-038].
- [L08 -> L05] Button icons: M3 20/20/24/32/40 dp by size [S-L08-102]; Carbon 16 px (20 px expressive) [S-L08-062]; S2 refreshed icon sizing to match text line height (v1.7.0) [S-L08-027].
- [L08 -> L06] Content rules live inside components: Fluent "New"/"Add" labels, buttons answer dialog titles; Atlassian specific labels [S-L08-066] [S-L08-085].
- [L08 -> L07] Component tokens exist in the wild: Carbon `$button-primary-hover`, `$focus-inset`; M3 per-size token files (ButtonSmallTokens etc.) [S-L08-062] [S-L08-102]. Figma component properties should mirror the API style chosen in DC-L08-04.
- [L08 -> L10] Native counterparts per component (SwiftUI/UIKit from HIG links, Compose from androidx source) are in the catalog; Expressive composables are alpha-only in Compose [S-L00-047].
- [L08 -> L11] Documentation template (above) and component status labels (alpha, beta, early access, caution, deprecated) from Atlassian and Radix [S-L08-011] [S-L08-021].
- [L08 -> S1] Questionnaire seeds: DC-L08-05, -06, -07, -09, -10, -11, -13, -14, -18, -19 are the highest-leverage component questions; disagreements between systems (disabled, tooltips on disabled, toasts) should be surfaced as explicit trade-offs, not defaults.

## Open questions / gaps
- **M3 focus indicator dimensions** (thickness, offset) were not found on the rendered states page; only "ring-like" was confirmed [S-L08-095].
- **Fluent appearance values and sizes** beyond primary/outline/subtle/transparent were not verified this session; the Fluent UI React v9 storybook was not opened [S-L08-066].
- **Polaris admin-only UI** (toast, navigation via App Bridge) was not checked; the catalog treats Polaris toast as absent from the web component index [S-L08-022].
- **Radix activity gap** (Aug 2025 to Jun 2026) is visible in the releases page, but I did not find a statement explaining it [S-L08-030].
- **Many anatomy details and some radii** in the catalog are marked [inferred]; V1 should verify them against each system's spec tabs.
- **Session limits:** the shared WebSearch budget ran out and Perplexity was out of quota, so late checks used direct fetches of known URLs only [S-L08-099] [S-L08-025].
- **COMMUNITY-SIGNAL.md** was read at 14:1x while L00 was still writing (sections a-e present). Later sections (for example the shadcn/AI topic, whose raw file was empty) were not available to reconcile.

## Confidence
- **Confirmed from Tier A pages today:** all 10 component inventories and counts; M3 Expressive changes and dates (May 2025); M3 button variants, sizes (from androidx token source), corner values, color mappings and state rules; Carbon button variants, heights, tokens, forms and notification patterns, data-table row sizes; Atlassian, Primer, shadcn, S2, Polaris button variants and props; HIG button roles, hit sizes, tab bar/toolbar/sheet guidance and change-log dates; SwiftUI `.glass`/`.glassProminent` (iOS 26.0); Base UI v1.0 date; S2 v1.0 date; shadcn Base UI default and React Aria (July 2026); Radix release dates; APG keyboard patterns (17 fetched); WCAG 2.4.7 (AA), 2.4.13 (AAA), 2.5.8 (AA), 1.4.11, 3.3.8.
- **Tier B, corroborated or evergreen:** Brad Frost atomic design and 2025 token comment; EightShapes spec sections; NN/g loading, empty-state, confirmation, infinite-scroll and progressive-disclosure guidance (NN/g as an organization remains trusted per L00; the dispute is about Jakob Nielsen's personal AI commentary, not these articles).
- **Inferred (labelled in text):** coverage classification of borderline cells (● vs ◐), recommended defaults and heuristics, visual-effect descriptions, generic token names, some anatomy parts and radii, and the five-level ontology recommendation.
- **Correction logged:** a WebFetch summary labelled WCAG 2.4.7 as Level A; the live Understanding page says Level AA [S-L08-069] [S-L08-072].
