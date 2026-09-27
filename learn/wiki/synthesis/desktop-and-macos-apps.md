---
type: synthesis
title: Desktop and macOS apps
created: 2026-09-24
updated: 2026-09-28
sources:
  - Vy0KKvZJRH8
tags:
  - od-area-platforms
---

# Desktop and macOS apps

## In short

A Mac app feels native when it shows up where people are already working, for example a small window opened by a keyboard shortcut, and then gets out of the way. The main window follows the layout of Apple's own utility apps: global actions along the top, navigation in a sidebar, content in the middle, and the top strip of the window left clear so people can drag it. Show only what people need right now, design dark mode on its own instead of inverting light mode, make every keyboard shortcut produce a visible change, and let people drag things in and out of the app. All of this comes from one practitioner video, so it is trusted opinion; where OpenDesigner's research or house standards say something different, they win.

## House standards

- **STD-visual-details-42** (should): adapt the design to the platform and situation: deep workflows with precise pointer control on desktop.
- **STD-when-to-animate-05** (must): give no animation to anything people trigger 100+ times a day, such as a launcher or command palette opening and closing, keyboard shortcuts and core navigation.
- **STD-when-to-animate-06** (must): never animate an action started from the keyboard, including shortcuts, command-palette toggles, focus jumps and moving a highlight with the arrow keys; the change happens instantly. **STD-when-to-animate-17** (must) makes animation on a keyboard-started action a blocking, high-severity review finding.
- **STD-visual-details-24** (should): give each color role a light value and a dark value. **STD-accessibility-motion-09** (should): ease the switch between dark and light instead of letting brightness jump.
- **STD-visual-details-17** (should): darker, heavier materials separate structural regions such as sidebars; lighter materials draw attention to interactive elements.
- **STD-visual-details-16** (should) and **STD-accessibility-motion-11** (must): bars, toolbars and sheets can be translucent, and they turn frostier or solid under `prefers-reduced-transparency: reduce` (both written for the web).
- **STD-accessibility-motion-15** (must): hover styles live inside `@media (hover: hover) and (pointer: fine)`. **STD-mobile-touch-02** (must): touch and mouse are handled together, since laptops can have touchscreens.
- **STD-accessibility-motion-16** (must): dialogs, popovers, menus and selects are built on an accessible primitive, and command menus on cmdk.
- **STD-visual-details-36** (must): things that look the same behave the same and live in the same place.

## What the sources teach

### The app comes to you
- A native-feeling Mac app is a system that shows up exactly where it is needed, not a destination people have to visit. Spotlight (Command Space, draggable anywhere) and Raycast are the models; third-party apps such as Notion (a pop-up when it detects a meeting) and Paste (docked at the bottom of the screen with a native blur) do the same [S-L19-067] ([[sources/Vy0KKvZJRH8-everything-you-need-to-design-macos-apps-exactly-like-apple-beginner-friendly|Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)]]).
- Start outside the main window: popovers, new windows, notifications and shortcut-triggered panels. Then look at how people actually work (Figma, then code, then Notion) and give them a shortcut that works without switching apps, such as Command Shift S for a quick-save window [S-L19-067].
- Keep a quick-capture window minimal: no traffic lights (the window buttons), a drop area, a simple input, a few buttons that show their shortcut, and a native blur [S-L19-067].
- On Enter, the window collapses into a toast and slides away while the save finishes in the background. This is optimistic UI: show the action as done and assume it will succeed, as Apple Mail does when it moves an email to the trash before the server confirms [S-L19-067].

### The main window
- Apple's utility apps (Finder, Notes, Reminders, Calendar, Settings) share one layout: global actions on top, navigation in a sidebar, content in the center, and the traffic lights built into the top bar or sidebar like any other element [S-L19-067].
- Roughly the top 50 pixels of Apple's windows are used to drag the window, so keep that strip uncluttered [S-L19-067]. This number is from the video alone.
- Skip the sidebar when navigation is only browsing and searching; the space goes to the user's content, and the UI becomes a container for it [S-L19-067].
- An app holds the user's own changing content, which makes it more user-focused than a landing page even when the pieces look alike. Before adding colors or effects, find the minimum UI that lets that content shine [S-L19-067].

### Show only what is needed
- A simple empty state invites the first action, and filters stay hidden until there is content to filter. An item's full details appear only when it is clicked [S-L19-067].
- Search is prominent and always reachable in native Mac apps (Music, Shortcuts, Weather). The example app chose a collapsed floating search bar that expands on click or shortcut, with a slide-out preview, over a command palette, whose results usually take people to a new screen. Search matches what is inside the images, not only titles. Results show a count, a clear (X) button, and the query with a back arrow at the top left [S-L19-067].
- Frequent item actions (copy, find, delete) sit in a floating action bar in the preview panel. The video also brings in Apple's universal share button, found on almost all apps, because sharing that way is sometimes simply more convenient [S-L19-067].

### Light and dark
- Every Mac lets people switch between light and dark mode, and apps should respect that setting as much as possible [S-L19-067].
- The two modes are not exact opposites. The video's reasoning is that dark mode needs colors that are further apart from each other; inverting a dark design into light mode makes the contrast too high, and pulling the light colors closer together looks more refined. The captions are muddled here, so this reading is the analysis's best interpretation [S-L19-067].
- The example app still puts a light/dark setting in its settings popover, next to the shortcut cheat sheet and the side the quick-save panel appears on [S-L19-067].

### Shortcuts, feedback and drag and drop
- Every shortcut and every interaction needs visible feedback, "micro animations, or at least a state change"; without it people assume something went wrong. In the example, Command Shift S slides the quick-save panel out, Escape slides it away, and the collapsed search bar expands when clicked or triggered [S-L19-067].
- Drag and drop of anything, anywhere, is a must: into the app and out of it to Figma, Finder or other apps, as Photos, Finder, Reminders and Shortcuts allow [S-L19-067].
- Desktop apps should still have onboarding, mainly to teach shortcuts, which are powerful but easy to forget. The example uses a simple modal that closes when people perform the shortcut, plus a cheat sheet in the settings popover; Raycast is cited for its onboarding [S-L19-067].

## Where they agree and disagree

With a single source, the comparisons are with OpenDesigner's research and house standards.

- **Window layout (agree, with one gap).** Top bar, sidebar and content [S-L19-067] match DC-L10-09 and DC-L14-05 (desktop: menu bar, toolbar, sidebar), DC-L03-19 (a full sidebar reads as a desktop productivity tool) and the desktop end of Q-layout-04's default. The video never mentions the menu bar, which native macOS expects together with keyboard shortcuts (DC-L10-24, the L10 platform table) and which holds "all the commands" (DC-L10-09).
- **Skipping the sidebar (no conflict).** DC-L08-19 defaults desktops to a sidebar for 3-5 destinations; the example app has only browse and search, so it falls below that range [inferred]. Q-layout-04 has no "no navigation container" option besides `hidden`.
- **Window chrome (partly covered).** Integrated traffic lights and a clear drag strip [S-L19-067] fit DC-L10-24's note that Electron shells expose `titleBarStyle` (hidden, hiddenInset) and Window Controls Overlay, and that an app ignoring native chrome reads as "a website in a window". No card gives a drag-strip height, so the 50-pixel figure stays the video's opinion.
- **Dark mode is not an inversion (agree).** [S-L19-067] matches DC-L10-17 (Apple: the dark palette isn't an inversion) and DC-L01-18 (no major system ships a pure inversion), plus STD-visual-details-24. DC-L01-18 also notes that Spectrum's dark themes target higher contrast ratios, which is close to the video's "more different colors in dark mode" [inferred].
- **An in-app appearance setting (disagree).** Following the system setting [S-L19-067] matches DC-L10-17 and Q-theme-01's default `system-light-dark`. But DC-L10-17 reports Apple's advice to avoid an app-specific appearance setting and recommends an in-app override only on the web, while the example app adds one in its settings popover [S-L19-067]. That corresponds to Q-theme-01's `light-dark-toggle` option.
- **Shortcut feedback versus no keyboard animation (disagree).** The video's panel slides out on Command Shift S and away on Escape, and the search bar expands on its shortcut [S-L19-067]. The house standards say a keyboard-started action, a launcher or a command palette opening and closing changes instantly with no animation (STD-when-to-animate-05, -06), and review blocks it (STD-when-to-animate-17). The sources behind STD-when-to-animate-05 cite Raycast having no open/close animation, while the video cites Raycast as its model for appearing when needed. The two agree that feedback must be visible; the house standard wins on how, so the panel should appear instantly and the "state change" half of the video's rule is the part to keep [inferred].
- **Progressive disclosure and empty states (agree).** Hidden filters and details on click [S-L19-067] match DC-L13-03 (primary options first, at most two levels; contextual reveal on selection) and the `progressive` default of Q-pattern-03. The first-use empty state matches DC-L13-10's "first use" type, which asks for a message, an explanation and an action.
- **Onboarding (partly disagree).** DC-L13-11 defaults to no forced tour, with contextual help and empty states, and everything skippable. The video's modal that closes when people perform the shortcut is a short interactive walkthrough, which DC-L13-11 reserves for genuinely new, complex interfaces; the video itself says onboarding isn't standard for Apple apps [S-L19-067]. The shortcut cheat sheet fits DC-L10-24's point that Mac users expect keyboard shortcuts [inferred].
- **Optimistic UI (agree, one detail missing).** DC-L13-01 lists optimistic UI as an option and warns that a failed action produces a visible rollback. The video assumes success and does not say what happens when a save fails [S-L19-067].
- **Native blur (agree, fallback missing).** The Paste-style blur on the quick-save window [S-L19-067] fits STD-visual-details-16 and DC-L10-24's macOS vibrancy materials. The video doesn't mention a reduced-transparency fallback, which STD-accessibility-motion-11 and DC-L04-16 require.
- **Drag and drop (agree, alternative needed).** Making drag and drop a must [S-L19-067] is compatible with DC-L10-15's WCAG 2.5.7 constraint only when a non-drag path exists; the floating action bar's copy action and the share button are such paths [inferred].
- **Sizes (not covered by the video).** The video gives no target or text sizes apart from the drag strip. The research gives macOS targets of 28x28pt by default and 20pt at minimum (DC-L10-15, DC-L03-12) and a 13pt default text size with a 10pt minimum (L10 platform table), and DC-L10-07 notes that macOS has no Dynamic Type. The [[synthesis/mobile-app-patterns|Mobile app patterns synthesis]] compares that desktop size with the phone's.

## Decisions this informs

- **Q-plat-01** (`desktop`): this is the wiki's only source on desktop app design; its patterns are the practitioner layer on top of DC-L10-24 [S-L19-067].
- **Q-plat-03** (pointer and keyboard): shortcuts as a primary input, each with a visible change [S-L19-067] that happens instantly, with no animation (STD-when-to-animate-06; the video itself asks for micro-animations).
- **Q-plat-05, Q-plat-10** (look like the platform or the brand): the video's "native feel" means following Apple's utility layout, integrating the traffic lights and offering the system share button [S-L19-067]. That points to `native-first` or `hybrid` in Q-plat-05 and at least `custom-skin` (usual behavior, your own look) in Q-plat-10 [inferred].
- **Q-layout-04** (where navigation sits): sidebar on desktop by default; no sidebar when navigation is only browsing and searching [S-L19-067].
- **Q-theme-01** (light and dark): follow the system [S-L19-067]; whether to add an in-app toggle on macOS is disputed (DC-L10-17).
- **Q-color-16** (deriving dark mode): design dark separately rather than inverting [S-L19-067]; all three options already avoid inversion.
- **Q-pattern-03** (show everything or disclose progressively): `progressive`, with filters hidden until content exists [S-L19-067].
- **Q-pattern-04** (empty screens and first use): `empty-kinds` for the first-use state, and a short shortcut-teaching modal as the video's choice [S-L19-067].
- **Q-state-08** (what people see while they wait): optimistic UI for background saves, with a failure path still to be designed [S-L19-067].
- **Q-depth-04** (glass or solid): native blur on floating utility windows, with a solid fallback [S-L19-067]. `standards.json` now refuses the question's `none` (opaque) and `transient` options under STD-visual-details-16, so translucent bars are the house direction and the solid surface stays as the reduced-transparency fallback (STD-accessibility-motion-11).

## Visual examples worth showing

- Apple's utility-app layout in Finder or Notes: top-bar actions, sidebar, content, traffic lights built into the bar, and the roughly 50-pixel drag strip highlighted [S-L19-067].
- The same main window with and without a sidebar, showing the space freed for large images [S-L19-067].
- The quick-save window (drop area, input, buttons with shortcut hints, native blur) collapsing into a toast on Enter [S-L19-067].
- The first-use empty state with all filters hidden, beside the filled browse view with filters showing [S-L19-067].
- A dark design inverted into light mode (harsh contrast) beside a light mode with the colors pulled closer together [S-L19-067].
- The collapsed floating search bar, then expanded with a result count, clear X, query label and back arrow, and the slide-out preview with its floating action bar (copy, find, delete) [S-L19-067].
- An image dragged out of the app into Figma or Finder [S-L19-067].
- The onboarding modal that closes when the shortcut is pressed, and the settings popover holding the shortcut cheat sheet, the panel side and the appearance setting [S-L19-067].

## Open questions

- No OpenDesigner question covers the desktop app shell yet: window chrome and the drag region, the menu bar, a shortcut list, drag and drop, or floating utility windows. The platform cards propose three (Q-plat-13 app presence, Q-plat-14 title bar, Q-plat-15 shortcuts; DC-L19-149 to DC-L19-151); the menu bar and drag and drop still have none (DC-L19-158 offers drag-out as a sharing option only). The earlier id clash is settled in the cards: DC-L19-96's slowest-device question is back at Q-plat-11 (`_cards/motion.md`), and Q-plat-15 stays with shortcuts. Should Q-plat-01 `desktop` unlock them, in stage 04 or stage 13?
- DC-L19-149 proposes that a shortcut-opened panel appears and closes instantly, with the state change as the feedback, and reads the confirming toast as a separate notification that may enter as toasts do [inferred]. Does the owner accept that reading of STD-when-to-animate-06 for the toast?
- Should macOS apps offer an in-app light/dark setting (the video) or only follow the system (DC-L10-17)?
- The 50-pixel drag strip is one video's estimate. Is there a platform source to confirm it before it becomes a layout token?
- Which pointer target should desktop apps use as the floor: macOS 28pt (20pt minimum) or the web's 24px?
- Windows desktop apps have no source in the wiki. Should the research on Mica, Acrylic and 4/8px radii (DC-L10-24) be matched by a practitioner source?
- What should an optimistic save show when it fails?
