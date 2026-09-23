# L14: UI practices by device class (what holds everywhere, what changes)

Lane: L14 (Device classes, input modalities, usage contexts). Author: orchestrator subagent L14. Written 2026-09-23.
Trace: `traces/L14-trace.md` (every source, including rejected ones). Schema: `_coordination/SCHEMA.md`.
Status: complete (14 Decision Cards; 12 device classes; sources in traces/L14-trace.md).

## Lane overview

L10 answers "which operating system and design language?" This lane answers a different question: **what kind of device, held or viewed how, operated with what input, for how long?** A design-system builder needs that second answer to set target sizes, type sizes, navigation, focus states, motion, density and safety rules, because a 42 mm watch, a 65-inch TV across the room, a car screen seen in two-second glances and a headset window 1.75 m away all break the phone defaults in different ways.

To avoid duplicating other lanes, this file reuses and cites:
- L10 (`research/L10-platforms.md`) for OS design languages, units, text scaling, the Apple/Android target and text minimums, navigation per OS, materials, dark mode per OS [S-L10-011, S-L10-012, S-L10-013, S-L10-015, S-L10-089].
- L03 (`research/L03-space-layout.md`) for target sizes, spacing, breakpoints, containers, max widths and safe areas [S-L03-033, S-L03-035, S-L03-016, S-L03-020].
- L02 (`research/L02-typography.md`) for type scales and platform minimum text sizes [S-L02-001, S-L02-022].

New research here concentrates on the device classes those lanes do not cover (watch, TV, car, spatial, voice and AI, kiosk, console, e-ink), on phone ergonomics research (Hoober), and on the two outputs the builder needs most: **invariants** and a **device matrix**.

### Top findings

1. **Text and targets are sized by viewing distance and input precision, not by device name, and the official numbers converge when you convert them to visual angle.** Main text on tvOS (29 pt default on a 1920 pt wide canvas [S-L10-087]), Fire TV (14 sp minimum body on a 960 dp canvas) and Xbox (15 epx minimum main text on a 960 epx canvas) all land at about 1.5% of screen width, and the floor for secondary text (tvOS 23 pt, Xbox 12 epx) at about 1.2% [S-L10-011, S-L14-027, S-L14-026, S-L14-023] [computed]. Converted to visual angle with typical distances, iPhone body 17 pt at arm's length, watch 16 pt at about one foot, and tvOS 29 pt from 10 ft all subtend roughly 0.3-0.5 degrees [computed; distances partly inferred; see Invariant I-3]. The builder should store type as "role x viewing-distance class", not "role x device".
2. **Target minimums split into three families by input precision.** Pointer: 20-28 pt (macOS) and 24 CSS px (WCAG AA). Finger on a hand-held screen: 44 pt / 48 dp (40 dp allowed on Wear OS). Remote focus, gaze and hands, or a moving body: tvOS 66 pt, visionOS 60 pt, Android XR 56 dp, Meta 2.5-3 degrees of visual angle, car screens 64-76 dp under vibration [S-L10-012, S-L03-035, S-L14-018, S-L14-041, S-L14-043, S-L14-032, S-L14-037].
3. **The navigation model changes more than the look.** Phones put actions in the bottom "interaction area" (Samsung One UI, Apple) but people prefer to read and tap the center and change grip every few seconds (Hoober) [S-L14-053, S-L10-015, S-L14-050, S-L14-051]. Watches navigate vertically with the Digital Crown or rotary input [S-L14-002, S-L14-018]. TVs use D-pad focus, where every element must be focusable and edge-to-edge travel should take no more than six clicks [S-L14-004, S-L14-026]. Cars use system templates the app cannot restyle [S-L14-010, S-L14-032]. Headsets use look-and-pinch with no gaze data given to the app [S-L14-009].
4. **Some devices impose hard safety gates, which a builder can encode as lint rules.** NHTSA's voluntary guidelines cap single glances at 2 s and total eyes-off-road time at 12 s per task, and recommend locking out video, auto-scrolling text, manual text entry for messaging, and reading text while driving [S-L14-031]. Android for Cars requires tasks in five screens or fewer, no on-screen animation, and 24 sp text in parked apps [S-L14-032]. Google's Design for Driving requires 4.5:1 contrast and dark (negative-polarity) content at night [S-L14-037]. Headsets require content placement about 1-1.75 m away, within the central field of view, and no head-locked content [S-L14-009, S-L14-041, S-L14-008].
5. **AI is becoming a cross-device surface and a design-system mode.** Apple shipped a chat-based Siri app synced across devices on 14 Sep 2026 and look-to-act on Vision Pro [S-L14-049]. IBM Carbon implements "AI presence" as a Figma variable mode with its own color tokens, an AI label that opens an explainability popover, and "revert to AI" states on 12 components [S-L14-058]. Apple's generative-AI HIG and Microsoft's 18 human-AI guidelines agree on disclosure, easy correction, confirmation before irreversible actions, and specific progress messages [S-L14-011, S-L14-060].

## Part 1: Device classes

Each class below lists the usage context, the real values that differ from a phone baseline, and what the builder must change. Values already documented in L10/L03/L02 are cited to those lanes rather than repeated in full.

### 1.1 Phone (iOS, Android, mobile web)

- **Context.** Held in one or both hands, viewed "no more than a foot or two" away, rotated between portrait and landscape as needed; sessions range from "a minute or two" to an hour or more [S-L14-066]. NN/g measured an average mobile session of 72 s versus 150 s on desktop (2015 data, still the most-cited figure) and lists interruptions, small screen and single-window use as the core constraints [S-L14-054].
- **How people actually hold phones (Hoober).** In 780 observed touch interactions, 49% were one-handed, 36% cradled (one hand holds, the other taps) and 15% two-handed; 67% of one-handed use was with the right thumb, and people change grip "very often", sometimes every few seconds [S-L14-050]. A 2017 follow-up found people prefer to view and tap the **center** of the screen and scroll content there; targets can be about 7 mm at the center but need about 12 mm at the corners [S-L14-051].
- **Reach zones in official guidance.** Samsung One UI splits the screen into a top **viewing area** (titles, no touch components, wide margins) and a bottom **interaction area** for actionable components, so the phone works one-handed [S-L14-053]. Apple says controls in the middle or bottom of the screen are easier to reach (L10 [S-L10-015]).
- **Reconciling the two.** Put persistent navigation and primary actions on the bottom edge (bars, sheets, FABs), put the main content where it can be scrolled into the center, and keep destructive or rare actions out of the bottom corners and away from the thumb's resting arc [inferred from S-L14-051, S-L14-053]. Hoober's data argues against treating the "thumb zone" heatmap as fixed, because grip changes constantly [S-L14-050].
- **Targets and type.** iOS 44x44 pt (28 minimum), Android 48x48 dp; iOS body 17 pt, Android body 14-16 sp, minimum 11 pt/sp (L10, L03, L02 [S-L10-012, S-L03-033, S-L02-001, S-L02-005]).
- **Navigation.** Bottom tab/navigation bar with 3-5 destinations, navigation stack with swipe/predictive back, sheets with detents (L10 DC-L10-09 [S-L10-014, S-L10-025]).
- **Edges.** Edge-to-edge backgrounds with inset-aware controls; Android 15+ enforces it (L10 DC-L10-11, L03 DC-L03-20 [S-L10-023, S-L03-052]).
- **Interruptions.** Save and restore context whenever the app is switched away, pause activities that need attention, finish user-started tasks in the background [S-L14-067].
- **Builder implication.** Phone is the reference class for touch targets and bottom navigation; its defaults should be generated first and every other class expressed as a delta [inferred].

### 1.2 Tablet and foldable

- **Context.** iPad: held, set on a surface or a stand, "typically within about 3 feet"; sessions from quick actions to hours; people combine Multi-Touch, virtual and hardware keyboards, pointer, Apple Pencil and Siri [S-L14-066]. iPadOS 26 windowed apps are resizable like macOS, and apps get no signal about which multitasking arrangement the user chose [S-L14-067].
- **Pointer on touch devices.** The iPad pointer "doesn't replace touch"; it adapts shape and uses highlight, lift and hover content effects plus "magnetism" that snaps to an element's hit region [S-L14-013]. The implication for components: hit regions, hover states and focus states must all exist on tablet components, not only on desktop ones [inferred from S-L14-013].
- **Keyboard focus on iPad.** Focus groups: Tab moves between groups (sidebar, list, grid), arrow keys move within a group; lists use a highlight, text fields use a focus ring [S-L14-004].
- **Foldables.** Android defines FLAT and HALF_OPENED states and two half-open postures: **tabletop** (horizontal fold; split top/bottom) and **book** (vertical fold; split left/right). Controls near the fold are hard to reach and text across it is hard to read; folded devices use a single column with a bottom bar, unfolded ones two panes with a navigation rail. The app restarts on fold/unfold, so state must survive [S-L14-068].
- **Quality bar.** Google's adaptive app quality has three tiers (ready, optimized, differentiated) and names test sizes: foldable 841x701 dp, 8-inch tablet 1024x640 dp, 10.5-inch 1280x800 dp, 13-inch Chromebook 1600x900 dp [S-L14-069]. Android 16/17 ignore orientation and resizability locks at 600 dp and wider (L10 [S-L10-020, S-L10-021]).
- **Builder implication.** Treat tablet as "phone targets plus pointer and keyboard states plus panes". Layout keys off window size (compact/medium/expanded), never off "is tablet" (L10 DC-L10-10 [S-L10-013, S-L10-022]).

### 1.3 Laptop and desktop (native and web)

- **Context.** Mac: stationary, "about 1 to 3 feet" away, sessions from minutes to "several hours of deep concentration", keyboard plus pointer, several apps open [S-L14-066].
- **Pointer precision and density.** macOS targets 28x28 pt default, 20 minimum; web AA floor 24x24 CSS px (L10, L03 [S-L10-012, S-L03-035]). Dense body sizes of 13-14 are the desktop norm (macOS 13 pt, Windows/Fluent/Carbon/Primer 14 px) (L02 [S-L02-001, S-L02-022]).
- **Hover.** Hover can reveal content, but any content that appears on hover or focus must be dismissible without moving the pointer, hoverable, and persistent (WCAG 1.4.13, AA) [S-L14-071]. Hover never exists on touch, so nothing essential can live only on hover [inferred].
- **Keyboard and focus.** Focus must be visible (WCAG 2.4.7) and not obscured (2.4.11) (L10 [S-L10-083]); the AAA target is an indicator at least as large as a 2 CSS px perimeter with 3:1 contrast between focused and unfocused states (2.4.13) [S-L14-070]. On macOS, the menu bar holds every command and people expect standard shortcuts (L10 [S-L10-015]).
- **Windows.** Don't put controls or critical information at the bottom of a Mac window, because people drag windows partly off-screen [S-L14-006]. Resizable windows mean the desktop app must also have compact layouts [inferred from S-L14-067].
- **Right-click, multi-select, drag.** Apple treats pointer gestures and modifier-key behaviors as system-consistent: don't redefine systemwide trackpad gestures, keep modifier-drag results identical across touch and pointer [S-L14-013].
- **Builder implication.** Desktop needs a "pointer" density mode (smaller controls, hover states, visible focus rings, context menus, shortcuts in tooltips and menus) layered on the same components (L03 DC-L03-10 [S-L03-009, S-L03-044]).

### 1.4 Large and ultra-wide displays

- **Values from L03 and L10.** Material adds large (1200-1599 dp) and extra-large (1600+ dp) breakpoints with up to 3 panes [S-L10-025]; Carbon's max breakpoint is 1584 px with three style models above it: editorial (centered max width), product/docs (left-aligned with nav), high-density (fluid) [S-L03-074]; Primer caps full pages at 1280 px [S-L03-008]; Material keeps 40-60 characters per line at every breakpoint and WCAG 1.4.8 (AAA) caps lines at 80 characters [S-L03-025, S-L03-073].
- **What changes on ultra-wide.** More panes, not wider paragraphs; reading surfaces stop growing at a max width while tool and data surfaces stay fluid [S-L03-074] [inferred for ultra-wide]. visionOS gives the same advice for very large windows: keep content horizontally centered [S-L14-006].
- **Builder implication.** Every layout template needs an explicit max-width or "fluid" flag and a pane count per breakpoint; the builder should warn when a text container can exceed 80 characters [inferred from S-L03-073].

### 1.5 Smartwatch (watchOS, Wear OS)

- **Context.** Worn on the wrist, viewed "no more than a foot away", operated with the other hand; people glance many times a day with interactions that "can last for less than a minute", and use complications, notifications and Siri more than the app itself [S-L14-001]. Wear OS: "complete tasks within seconds" to avoid arm fatigue [S-L14-015].
- **Surfaces before apps.** Both platforms rank glanceable surfaces above the app: Apple lists complications, notifications, the Smart Stack and Always On [S-L14-001]; Google's priority matrix puts the single most important datum in a complication, urgent events in a notification, one or two items on a tile, and the rest in the app [S-L14-015]. Tiles must be "immediate, predictable, relevant" [S-L14-020].
- **Input.** watchOS 10+: the Digital Crown is "the main way people navigate", lists and tabs are vertical, apps cannot respond to Crown presses, and Crown interactions must be backed by touch [S-L14-002]. watchOS 26 added a one-handed **wrist flick** to dismiss notifications and calls [S-L14-047]; watchOS 27 added a single-handed tap gesture that opens the Smart Stack [S-L14-049]. Wear OS supports rotary input (rotating side button or bezel) as an accessibility alternative to swiping [S-L14-018]. Voice input is faster than typing on a watch [S-L14-015].
- **Screen and layout.** Wear OS screens run 192-240+ dp with a 225 dp breakpoint; margins are percentages so rows don't clip on round screens; design small-first, and larger screens must never show less [S-L14-017]. watchOS: no more than three glyph buttons or two text buttons in a row [S-L14-006].
- **Targets.** watchOS 44x44 pt (28 minimum) [S-L10-012]. Wear OS 48x48 dp, with 40x40 dp allowed in some cases; list items at least 32 dp for TalkBack [S-L14-018].
- **Type.** watchOS default 16 pt, minimum 12 pt, Dynamic Type up to 140% (L10 [S-L10-011, S-L10-012]). Wear M3 adds arc (curved) and numeral roles and a variable-font axis for expressive feedback [S-L14-019]. Wear OS M3 type scale (Compose source): Display 40/44, 30/34, 24/26 sp; Title 18/20, 16/18, 14/16; Label 20/22, 15/18, 13/16; Body 16/18, 14/16, 12/14 (Extra Small 10/12); curved **Arc** styles 18/22, 15/18, 14/16; Numerals 60, 50, 40, 30, 24 [S-L14-022]. Text 20 sp and larger does not scale with the user's font size on Wear OS because space is too tight [S-L14-021].
- **Appearance.** Dark only: "Dark Mode isn't supported in visionOS or watchOS" (L10 [S-L10-089]; that watchOS is effectively always dark is [inferred]), Wear OS uses black backgrounds and derives color from the watch face (L10 [S-L10-089, S-L10-027]).
- **Builder implication.** A watch is not a small phone: it needs a separate "glance" tier of components (complication, tile, notification, compact list row), a vertical-only navigation template, round-safe percentage margins, and a dark-only theme [inferred from S-L14-001, S-L14-015, S-L14-017].

### 1.6 TV (tvOS, Google TV/Android TV, Fire TV, Samsung Tizen, Xbox)

- **Context.** Viewed from "8 feet or more" (Apple), "approximately 10 feet" (Microsoft's "10-foot experience"), 3 m (Samsung); sessions "often lasting hours"; shared by a household, so profiles and easy sign-in matter [S-L14-003, S-L14-026, S-L14-029].
- **Canvas and units.** Android TV and Fire TV design at 960x540 dp (1080p at xhdpi, 1 dp = 2 px) [S-L14-023, S-L14-027]; Xbox renders UWP apps at 200% scale, so UI is laid out on 960x540 epx [S-L14-026]; tvOS lays out in points on a 1920x1080 canvas (L10 [S-L10-087]).
- **Overscan and safe zones.** Keep text and focusable items out of the outer 5%: Android TV 48 dp sides and 27 dp (rounded to 24) top/bottom, with 58/28 dp recommended [S-L14-023]; Xbox 48 epx sides and 27 epx top/bottom [S-L14-026]; Fire TV "the outer 5% of any edge" [S-L14-027]; tvOS 80 pt sides and 60 pt top/bottom [S-L14-006]. Backgrounds and scrolling rows still run edge-to-edge [S-L14-026, S-L14-023].
- **Text size.** tvOS body 29 pt, minimum 23 pt [S-L14-012]; Fire TV minimum body 14 sp (28 px at 1080p) [S-L14-027]; Xbox 15 epx for main text and 12 epx for supplemental [S-L14-026]; Xbox games 26 px body height at 1080p [S-L14-074]. Android's TV Material library uses the same sp values as phone M3 (Body Medium 14/20, Label Small 11/16), which read larger because the canvas is only 960 dp wide [S-L14-025]. Converted to share of screen width, main text is about 1.5% on every TV platform (tvOS 29/1920, Fire TV 14/960, Xbox 15/960) and the secondary-text floor about 1.2% (tvOS 23/1920, Xbox 12/960) [computed]. Android's TV typography guidance calls for larger type read at a glance from a distance, in Roboto [S-L14-024].
- **Targets and density.** tvOS 66x66 pt, minimum 56 [S-L14-012]; Xbox interactive elements at least 32 epx tall and edge-to-edge travel in no more than **six clicks** [S-L14-026]. Microsoft: information density on a TV "should be comparable to ... a mobile phone, rather than ... a desktop" [S-L14-026]. tvOS grids: 2-9 columns with 40 pt horizontal gaps and at least 100 pt vertical gaps so focused items can grow without overlapping [S-L14-006]. Android TV: 12 columns of 52 dp with 20 dp gutters [S-L14-023].
- **Focus model.** Directional (D-pad) focus reaches **every** element; focus is never moved without user action; focused items scale up, lift and animate, so layouts must reserve room for the larger focused size; tvOS items have five states (unfocused, focused, highlighted/pressed, selected, unavailable); avoid showing a free pointer [S-L14-004]. Samsung: focus must be "clear and highly visible" and visually distinct from selected; prefer grids over diagonal layouts [S-L14-029]. Xbox: A selects, B goes back, the focus order follows the visual flow, linear menus loop and grids don't [S-L14-075]. Avoid tooltips on TV [S-L14-026]. Amazon's Vega OS (Fire TV, 2025) moves focus to the closest item in the D-pad direction, doesn't restore focus automatically when a screen returns, and asks for focus indicators that change physical properties (border, size), not only color, so they survive High Contrast mode [S-L14-089]. Google TV has added pointer-remote support (L10 [S-L10-002]), while Apple says to avoid a free pointer on TV except in games [S-L14-004], so a TV design must work with focus first and may add pointer hover.
- **Remote.** Siri Remote: swipe to move focus, press to select, Back opens the parent screen (not necessarily the previous one), press-and-hold Back goes Home, ignore accidental taps during playback [S-L14-005]. Samsung: remote button names and icons must match what happens on screen [S-L14-028; search snippet of Samsung's design principles, not re-verified].
- **Color.** TVs render color differently; Xbox historically limited UI to RGB 16-235 ("TV-safe") and now scales full-range content automatically; don't rely on subtle color differences; Xbox apps default to the dark theme [S-L14-026]. Fire TV suggests less saturated, cooler colors [S-L14-027].
- **Builder implication.** TV needs its own mode: a distance-scaled type ramp, a focus-state token set (scale, elevation, glow/outline, parallax flag), 5% safe-zone padding, grid layouts with focus headroom, dark default, and no hover-only or tooltip content [inferred from the sources above].

### 1.7 Automotive (CarPlay, CarPlay Ultra, Android Auto, Android Automotive OS)

- **Regulatory frame (US).** NHTSA's Phase 1 Visual-Manual Driver Distraction Guidelines (2013) are voluntary and nonbinding. Tasks should be doable with glances away from the road of **2 s or less** and **12 s or less** cumulative; the occlusion test uses 1.5 s glances with a 12 s total (raised from 9 s in the proposal) [S-L14-031]. The guidelines recommend locking out, while driving: non-driving video, certain graphical or photographic images, automatically scrolling text, manual text entry for messaging or browsing, and text for reading (books, web pages, social media, ads, messages). The proposal's 30-character and six-keypress limits were replaced by these category bans [S-L14-031].
- **Templates, not layouts.** CarPlay apps supply content to system templates (audio, communication, navigation, fueling and others) and iOS renders them; apps don't manage screen sizes or input hardware (touch, knobs, touch pads) [S-L14-010]. Android for Cars templated apps follow the same model [S-L14-032].
- **Google's numbers.** Tasks in **five screens or fewer**; app buttons respond within 2 s; launch and content load within 10 s; no animated elements, no auto-scrolling text, text ads limited to names; limited images; no autoplay [S-L14-032]. Parked apps (video, games, browsers) need 64 dp targets, 24 dp spacing and 24 sp text [S-L14-032]. Design for Driving (now maintained on a partner-only site; public copy dated 2024-07-23): read content within 2 s, show a spinner if loading exceeds 2 s, respond to input within 0.25 s, **76x76 dp** touch targets (height favored because of vibration), 23 dp between targets, primary text 32 dp and secondary 24 dp, at most 120 Roman characters per text item, 4.5:1 contrast [S-L14-035, S-L14-036, S-L14-037].
- **CarPlay layout and color.** Common CarPlay displays range from 800x480 to 1920x720 px; put the most important content in the upper half; test colors in a real car in sunlight and at night; CarPlay switches light/dark automatically with ambient light [S-L14-010]. Never require the phone: CarPlay must work with the iPhone locked or in a bag [S-L14-010].
- **Day/night.** Night content must use negative polarity (light text on dark), because a bright screen at night raises glare and after-images [S-L14-037]. Map apps must draw light or dark maps when told to [S-L14-032].
- **Voice.** Media and navigation apps must support Gemini/Google Assistant voice commands [S-L14-032]; CarPlay relies on Siri [S-L14-038].
- **2025-2026 changes.** CarPlay Ultra (from 15 May 2025, Aston Martin first; Hyundai, Kia, Genesis committed) spans the instrument cluster (speedometer, tachometer, fuel and temperature gauges), climate and media with automaker-specific themes designed with Apple [S-L14-038]. iOS 26 CarPlay added a compact incoming-call view, widgets and Live Activities [S-L14-047].
- **Builder implication.** For car, the builder should not generate custom screens at all for templated app types; it should generate content that fits templates, plus a lint layer that blocks animation, auto-scroll, long text, video and more than five steps [inferred from S-L14-031, S-L14-032].

### 1.8 Spatial computing (visionOS, Android XR, Meta Horizon OS)

- **Input.** visionOS: people look at an element and pinch (indirect gesture) with hands resting in the lap, or touch it directly; the system shows a hover effect when people look at something, and apps receive no gaze data before a tap, for privacy [S-L14-007, S-L14-009]. visionOS 27 adds look-to-act search and questions [S-L14-049]. Meta: touch (poke) for UI within reach, ray casting beyond it, microgestures for simple menus; gaze handles distance targeting where eye tracking exists, and ray and gaze must not run at the same time [S-L14-043].
- **Distance and field of view.** visionOS: aim for at least 1 m for content people read over time; avoid anchoring content to the head; keep important content centered and avoid distracting motion in the periphery [S-L14-009, S-L14-008]. Android XR: panels launch 1.75 m away; keep primary content in the central 41 degrees of the field of view [S-L14-041]. Meta: touch UI at 42-46 cm, ray casting comfortable from 0.46 to 3 m, avoid sustained head tilt beyond +/-15 degrees, and put frequent controls in the lower half of a panel to limit arm fatigue [S-L14-043].
- **Units.** A visionOS point is an angle, and windows scale dynamically so they look the same size near or far [S-L14-008]. Android XR uses dp plus the angular **dmm** (distance-independent millimeter; 0.868 dmm per dp) [S-L14-041]. Meta sizes targets in dp at panel scale and checks the angular size [S-L14-043].
- **Targets.** visionOS 60x60 pt (28 minimum); button centers 60 pt apart or 16 pt of space around each item [S-L14-012, S-L14-009, S-L14-008]. Android XR 56 dp targets (48 dp visual) with 8 dp spacing [S-L14-041]. Meta 48 dp hit target at panel scale (about 22 mm at touch distance), 2.5-3 degree angular minimum, 12 mm between targets [S-L14-043]. All three sit well above phone targets because eye saccades and hand tremor are less precise than a fingertip on glass [S-L14-009, S-L14-043].
- **Type.** visionOS default 17 pt, minimum 12 pt [S-L14-012]; avoid adding depth to text [S-L14-008]. Android XR minimum 14 dp, normal weight or heavier, sentence case [S-L14-041].
- **Panels and windows.** Android XR panels have 32 dp corners [S-L14-041]; in Full Space they have no minimum and a maximum of 2560x1800 dp, keep the same apparent size between 0.75 and 1.75 m, and can be moved between 0.75 and 5 m; orbiters (floating controls anchored to a panel) sit 20 dp off the panel at 15 dp elevation; spatial elevation levels are 16 dp (orbiter), 32 dp (popup) and 56 dp (dialog) [S-L14-087]; Meta panels default 1024x640 dp, minimum 384x500 dp [S-L14-042]. visionOS supports window resizing and asks apps to keep content centered at large sizes and put supplemental content in a new window, not an ornament [S-L14-006].
- **Materials and appearance.** visionOS window glass is system-owned and adapts to surroundings, and there is no Dark Mode setting (L10 [S-L10-008, S-L10-089]). Android XR headsets are opaque, but wired XR glasses are additive, so black renders as transparent [S-L14-041].
- **Feedback.** Hands have no haptics, so every press needs visual and audio confirmation; avoid hover-triggered layout changes and classic scroll bars [S-L14-043].
- **Comfort.** Choose the minimum immersion a moment needs; no overwhelming or fast motion without a stationary frame of reference; avoid repeating patterns that fill the field of view [S-L14-007, S-L14-009]; Meta recommends teleport and snap turning for locomotion [S-L14-045].
- **Builder implication.** Spatial needs angular sizing (targets, type, spacing), a gaze/hover state that is distinct from focus, bigger target and spacing tokens, depth tokens used sparingly, and a "no head-locked UI" rule [inferred from the sources above].

### 1.9 Voice, conversational and AI chat/agent interfaces

- **Voice-only.** Alexa's principles are be natural, brief, contextual, multimodal and trustworthy [S-L14-061]; write for the ear [S-L14-064]. The **one-breath test**: if a response can't be said without taking a breath, shorten it or split it across turns; read lists of 2-5 options, introduced and separated by pauses [S-L14-065].
- **Voice as a secondary input everywhere.** Watch (voice faster than typing) [S-L14-015], car (required voice commands for media and navigation) [S-L14-032], TV (voice search) [S-L14-027], headset (look plus Siri) [S-L14-049].
- **AI chat and agents (2025-2026).** Apple shipped a chat-based Siri app synced across devices on 14 Sep 2026 [S-L14-049]. Apple's generative-AI HIG (updated 8 Jun 2026): keep people in control, say where AI is used, set expectations, warn about hallucinations, ask before irreversible or risky actions, put Edit/Undo/Retry/Adjust next to generated content, give specific progress messages ("Summarizing key themes from your notes" rather than "Processing..."), consider offering alternatives, and keep feedback voluntary [S-L14-011]. Microsoft's 18 human-AI guidelines (CHI 2019) cover the same ground in four phases: initially (make clear what the system can do and how well), during interaction (timing, context, social norms, bias), when wrong (efficient invocation, dismissal and correction, scope when in doubt, explain why), and over time (remember, learn, update cautiously, granular feedback, consequences, global controls, notify of changes) [S-L14-060].
- **AI as a design-system mode.** IBM Carbon for AI marks AI-generated content with a light metaphor (glow, gradients) and dedicated AI color tokens in the normal themes, an **AI label** that opens an explainability popover, an "AI presence" Figma variable mode, AI variants of 12 core components (checkbox, form, select, data table, modal, tag, date picker, number input, text input, dropdown, radio, tile), and a "revert to AI" state when the user overrides a suggestion; it forbids using the AI style as decoration [S-L14-058].
- **Builder implication.** Treat "conversational surface" as a device-independent pattern family (message list, composer, suggestion chips, streaming/progress states, citations, retry/undo, confirmation-before-action) plus an optional "AI presence" mode on components, and render it per device: full chat on phone/desktop, voice turns on car/speaker, short cards on watch, a placeable window in space [inferred from S-L14-011, S-L14-049, S-L14-058].

### 1.10 Kiosks and point of sale, e-ink, game consoles (brief)

- **Kiosk/POS (public, standing, shared).** US ADA reach range for operable parts is 15-48 inches above the floor (44 in when reaching over an obstruction deeper than 20 in), with no more than 5 lbf and no tight grasping or twisting [S-L14-072]. Section 508 requires ICT with closed functionality and a display (kiosks) to offer speech output with volume control and private listening, tactilely discernible controls, and on-screen characters at least 3/16 inch (4.8 mm) high [S-L14-073]. Builder implication: keep touch targets within the 15-48 inch band on large-format screens, give a speech/tactile path, and add an inactivity reset (the last is [inferred], no source read).
- **E-ink.** Full refreshes invert every pixel to clear ghosting, which causes a visible blink; black-and-white updates take about 125-250 ms without flicker and grayscale about 750 ms with a blink, which limits animation and scrolling [S-L14-078]. Builder implication: a "paper" mode with pure black/white, no motion, paging instead of smooth scroll, borders instead of shadows [inferred; a CHI 2026 e-paper design-system paper exists but could not be read, S-L14-077].
- **Game consoles.** Controller-first focus navigation with consistent A (select) / B (back) / bumpers (tabs) / triggers (pages), full navigation by digital input alone, logical focus order, linear menus loop [S-L14-075]. Text: at least 26 px body height at 1080p on console, 18 px on PC/VR, scalable to 200% with one scroll direction only [S-L14-074]. Every Apple platform except watchOS supports game controllers [S-L14-012].

## Part 2: Input modalities and accessibility across devices

### 2.1 Input modality table

| Input | Where it is primary | Precision and target implication | States it requires | Key rules |
|---|---|---|---|---|
| Touch (finger) | Phone, tablet, watch, car screens, kiosks | 44 pt / 48 dp handheld; 40 dp allowed on Wear; 64-76 dp in cars; 7 mm center vs 12 mm corners [S-L10-012, S-L14-018, S-L14-032, S-L14-037, S-L14-051] | pressed, disabled; no hover | Single-pointer alternative to path and multipoint gestures (WCAG 2.5.1); activate on up-event, allow abort (2.5.2) [S-L14-081] |
| Mouse / trackpad | Desktop; optional on tablet and headset | 20-28 pt macOS, 24 CSS px web AA [S-L10-012, S-L03-035] | hover, pressed, focus, context menu | Hover content dismissible, hoverable, persistent (WCAG 1.4.13) [S-L14-071]; don't redefine system gestures; iPad pointer adds to touch, doesn't replace it [S-L14-013] |
| Keyboard | Desktop; tablet with keyboard; TV and console arrow keys | n/a (focus, not hit area) | visible focus ring, focus order, shortcuts | Everything operable by keyboard, no traps (2.1.1, 2.1.2) [S-L14-081]; visible and unobscured focus (2.4.7, 2.4.11) [S-L10-083]; AAA indicator: 2 CSS px perimeter area, 3:1 change (2.4.13) [S-L14-070]; iPad focus groups (Tab between, arrows within) [S-L14-004] |
| Stylus (Apple Pencil, S Pen) | Tablet (drawing, notes, markup) | Pixel-level precision [S-L14-083] | hover preview (never an action) | Mark immediately with no mode switch; controls must accept stylus; design for left and right hands [S-L14-083] |
| D-pad / remote / game controller | TV, console; also switch users elsewhere | Focus steps, not hit areas; 66 pt tvOS targets, 32 epx min height Xbox [S-L14-012, S-L14-026] | focused (scale, lift), pressed, selected, unavailable (5 states on tvOS) [S-L14-004] | Every element reachable; focus never moves on its own; Back opens parent; A select, B back; <=6 clicks edge to edge [S-L14-004, S-L14-005, S-L14-075, S-L14-026] |
| Digital Crown / rotary bezel / side button | Watch; Crown also recenters and sets immersion on Vision Pro | Continuous scroll with haptic detents [S-L14-002] | visual response to every turn | Crown drives vertical navigation; back it up with touch; apps can't use Crown presses [S-L14-002]; rotary as accessibility path on Wear [S-L14-018] |
| Car knobs, touch pads, steering controls | Car | System handles them for templated apps [S-L14-010] | focus (system) | Glance <= 2 s, total <= 12 s [S-L14-031] |
| Eyes (gaze) + pinch | visionOS; Android XR; Meta with eye tracking | 60 pt / 56 dp / 2.5-3 degrees; 16 pt or 12 mm spacing [S-L14-012, S-L14-041, S-L14-043, S-L14-009] | hover effect (system-rendered, not focus) [S-L14-004, S-L14-009] | No gaze data before a tap [S-L14-009]; don't run gaze and ray together [S-L14-043] |
| Hands: direct touch, ray, microgestures | Meta Horizon, visionOS direct touch | 48 dp at panel scale (~22 mm) [S-L14-043] | hover, pressed with audio | Touch at 42-46 cm; ray 0.46-3 m; no haptics so always visual + audio feedback [S-L14-043] |
| Voice | Car, speaker, watch, TV search; accessibility (Voice Control) everywhere | n/a | listening, processing, speaking | One-breath responses; lists of 2-5 [S-L14-065]; label controls so Voice Control can target them [S-L14-079] |
| Device motion / wrist gestures | Watch (wrist flick, tap gesture), phone (shake, tilt) | n/a | n/a | Motion-triggered functions need a UI alternative and a way to disable (WCAG 2.5.4) [S-L14-081, S-L14-047, S-L14-049] |

**Cross-cutting rule.** People switch inputs mid-task: iPad users combine touch, keyboard, pointer and Pencil [S-L14-066]; Apple asks for a consistent experience "whether people are using gestures, eyes, a pointing device, or a keyboard" [S-L14-013]; WCAG 2.5.6 (AAA) says content should not restrict input modalities the platform offers [S-L14-082]. A component therefore needs all of its states (hover, focus, pressed, selected, disabled, and on spatial devices gaze-hover) defined once, with each device showing the subset its inputs can trigger [inferred].

### 2.2 Accessibility per device class

| Device | Screen reader | Motor / switch | Vision (size, zoom, contrast) | Device-specific notes |
|---|---|---|---|---|
| Phone / tablet | VoiceOver, TalkBack (L10 [S-L10-012, S-L10-072]) | Switch Control, AssistiveTouch, Full Keyboard Access, Voice Control; Switch Access [S-L14-079, S-L10-072] | Dynamic Type to AX5, Android font scale to 200% (L10 [S-L10-011, S-L10-071]) | Assistive Access gives iOS/iPadOS a streamlined layout for cognitive disabilities [S-L14-079] |
| Desktop / web | VoiceOver (macOS), Narrator, NVDA/JAWS [inferred for Windows readers] | Keyboard-only; WCAG 2.1.1 [S-L14-081] | Browser zoom and 200% text (L02 [S-L02-028]); forced colors (L10 [S-L10-031]) | Visible focus is the main accessibility surface [S-L10-083, S-L14-070] |
| Watch | VoiceOver on watchOS with no extra HIG considerations [S-L14-080]; TalkBack on Wear [S-L14-018] | Rotary input as an alternative to swiping [S-L14-018] | watchOS Dynamic Type to 140% [S-L10-012]; Wear font scaling, but text 20 sp+ doesn't scale [S-L14-021] | List items at least 32 dp so TalkBack doesn't skip them [S-L14-018] |
| TV | VoiceOver on tvOS [S-L14-080]; TalkBack on Android TV [S-L14-086] | Remote and focus navigation is itself switch-like [inferred] | Android TV apps must honor font scale and reflow [S-L14-086] | Audio description preference (Android 13+) [S-L14-086]; captions [inferred] |
| Car | System-provided (templates) [S-L14-010] | Voice first [S-L14-032] | 4.5:1 contrast, 24-32 dp text [S-L14-037] | Safety rules outrank customization [S-L14-031] |
| Spatial | VoiceOver on visionOS (custom gestures get no hand input while it runs) [S-L14-080] | Dwell Control, Head Pointer, hand/head Pointer Control, Switch Control [S-L14-007, S-L14-079] | Zoom [S-L14-079] | Prefer horizontal layouts to limit neck strain; no head-anchored UI, because it blocks Pointer Control [S-L14-079] |
| Kiosk | Speech output required for closed ICT with a display (Section 508 402) [S-L14-073] | Tactile controls, one-handed, 15-48 in reach [S-L14-073, S-L14-072] | 4.8 mm characters minimum [S-L14-073] | Private listening (headphone jack or equivalent) [S-L14-073] |
| Console | Narration defaults on unless the platform setting says otherwise [S-L14-075] | Full navigation by digital input; remapping [S-L14-075] | Text to 200%, 26 px body height at 1080p [S-L14-074] | Accessibility settings reachable from the first launch screen [S-L14-075] |

## Part 3: Invariants (practices that hold on every device)

Each invariant lists the evidence across device classes. "Holds with exceptions" means an official source documents a deliberate exception.

- **I-1. The hit area never shrinks below the device floor, even when the visual control does.** Material keeps 48x48 dp targets for smaller icons (L03 [S-L03-029]); Wear OS extends a 24 dp icon's target to 48 dp [S-L14-018]; Android XR pairs a 56 dp target with a 48 dp visual [S-L14-041]; Meta uses a 48 dp collider around a smaller visual with 4-6 dp padding [S-L14-043]; WCAG 2.5.8 sets a 24 CSS px floor on the web [S-L03-035]. Density modes may shrink visuals, never hit areas.
- **I-2. Target size grows as input gets less precise or the body is less stable.** Pointer 20-28 pt / 24 px; finger on handheld glass 44-48; remote focus and gaze 56-66 (Meta's 48 dp collider is checked against a 2.5-3 degree angular minimum instead); hands in a moving car 64-76 dp [S-L10-012, S-L03-035, S-L14-012, S-L14-041, S-L14-043, S-L14-032, S-L14-037]. Hoober's 7 mm (center) vs 12 mm (corner) shows the same effect inside one phone [S-L14-051].
- **I-3. Legibility is a visual-angle budget, so type grows with viewing distance.** Official defaults: watch 16 pt at about 1 ft, phone 17 pt at 1-2 ft, Mac 13 pt at 1-3 ft, TV 29 pt at 8+ ft [S-L14-012, S-L14-001, S-L14-066, S-L14-003]. Worked through (assumptions: iPhone @3x at 460 ppi, Watch @2x at 326 ppi, 65-inch 16:9 TV with a 1920 pt canvas): iPhone body = 2.8 mm, about 0.54 degrees at 30 cm and 0.27 at 60 cm; Watch body = 2.5 mm, about 0.48 degrees at 30 cm; TV body = 21.7 mm, about 0.41 degrees at 3.05 m and 0.51 at 2.44 m [computed; ppi values and TV size are assumptions, not from sources read in this lane]. Android XR's 14 dp minimum works out to about 0.7 degrees (14 x 0.868 dmm) [computed from S-L14-041]. Every Apple platform's minimum text is 65-79% of its default (11/17, 10/13, 23/29, 12/17, 12/16) [computed from S-L14-012].
- **I-4. Every function must work with more than one input, and with the device's accessibility path.** Keyboard operability and no traps (WCAG 2.1.1, 2.1.2), single-pointer alternatives to gestures (2.5.1), UI alternatives to device motion (2.5.4) [S-L14-081]; don't restrict available input modalities (2.5.6) [S-L14-082]; Apple: one consistent experience across gestures, eyes, pointer and keyboard [S-L14-013]; Crown interactions backed by touch [S-L14-002]; Xbox: everything navigable by digital input alone [S-L14-075]; TV: every element focusable [S-L14-004].
- **I-5. Focus and selection are always visible, distinct from each other, and never move by themselves.** Apple focus systems (ring, highlight, parallax) and "avoid changing focus without people's interaction" [S-L14-004]; Samsung: focused must be visually distinct from selected [S-L14-029]; Xbox: predictable focus order that follows the visual flow [S-L14-075]; Amazon Vega: focus indicators should change a physical property (border, size), not only color, so High Contrast mode keeps them [S-L14-089]; WCAG 2.4.7 / 2.4.11 / 2.4.13 [S-L10-083, S-L14-070].
- **I-6. Text follows the user's size setting, and containers grow with it (holds with exceptions).** iOS Dynamic Type to AX5, Android to 200%, web 200% (L10, L02 [S-L10-011, S-L10-071, S-L02-028]); Android TV must honor font scale [S-L14-086]; Xbox games scale text to 200% [S-L14-074]; watchOS to 140% [S-L10-012]. Exceptions: macOS has no Dynamic Type (L10 [S-L10-011]); Wear OS does not scale text of 20 sp and above [S-L14-021].
- **I-7. Body text contrast is at least 4.5:1 and boundaries never rely on shadow or translucency alone.** WCAG/Apple/Android 4.5:1 (L10 [S-L10-012, S-L10-072]); cars 4.5:1 for text, icons and selected items [S-L14-037]; forced colors strips shadows (L10 [S-L10-031]). TVs render color unpredictably, so don't separate UI by subtle color alone [S-L14-026].
- **I-8. Interactive content stays inside the device's safe region; backgrounds may run to the edge.** Phone safe areas and edge-to-edge (L10 [S-L10-013, S-L10-023]); TV 5% overscan margins with edge-to-edge backgrounds and rows [S-L14-023, S-L14-026, S-L14-027, S-L14-006]; round watch screens use percentage margins [S-L14-017]; foldable hinges get no controls or text [S-L14-068]; spatial content stays in the central field of view (41 degrees on Android XR) [S-L14-041, S-L14-008].
- **I-9. The more constrained the attention, the shallower the hierarchy and the fewer the steps.** Watch: single-screen, glanceable interactions and shallow navigation [S-L14-001]; TV: remove unnecessary levels, six clicks edge to edge [S-L14-029, S-L14-026]; car: five screens or fewer, 12 s total eyes-off-road [S-L14-032, S-L14-031]; voice: 2-5 options per turn [S-L14-065].
- **I-10. State survives interruptions and configuration changes.** Save/restore on app switch and finish tasks in the background [S-L14-067]; foldables restart on fold and must restore state [S-L14-068]; CarPlay must never lock people out because the phone needs input [S-L14-010]; Always On keeps the layout consistent and switches controls to "unavailable" rather than removing them [S-L14-084].
- **I-11. Every action gets feedback within a bounded time, and waits get honest progress.** Car: response within 0.25 s, spinner past 2 s [S-L14-036]; Samsung TV: loading indicators past a threshold [S-L14-029]; Crown turns must change something visible [S-L14-002]; hands without haptics need visual plus audio confirmation [S-L14-043]; generative AI should describe what it is actually doing while it works [S-L14-011].
- **I-12. The platform owns "back" and "exit".** Android predictive back (L10 [S-L10-020, S-L10-030]); tvOS Back opens the parent screen and press-and-hold goes Home [S-L14-005]; Xbox B goes back, with a persistent route to the main menu [S-L14-075]; Crown presses are reserved for the system [S-L14-002].
- **I-13. Motion is optional, never the only signal, and never flashes more than three times a second.** WCAG 2.3.1 [S-L14-081]; Apple Reduce Motion and "make motion optional" (L10 [S-L10-012, S-L10-088]); cars ban on-screen animation in templated categories [S-L14-032]; Always On minimizes motion [S-L14-084].
- **I-14. Every interactive element and glanceable surface has an accessible name.** VoiceOver and Voice Control labels [S-L14-079]; Wear tiles and complications need content descriptions that match what is shown [S-L14-018]; Android TV TalkBack [S-L14-086].

### What always changes (the variables behind the matrix)

| Variable | What it drives | Range across devices |
|---|---|---|
| Viewing distance | Type size, icon size, detail level | ~30 cm (watch) to 3 m (TV); 0.42 m touch to 3 m ray in XR [S-L14-001, S-L14-026, S-L14-043] |
| Input precision | Target size, spacing, available states | 20 pt pointer to 76 dp car touch [S-L10-012, S-L14-037] |
| Attention per interaction | Density, steps, text length | <2 s glance (car) to hours (TV, desktop) [S-L14-031, S-L14-003, S-L14-066] |
| Ergonomics and posture | Where primary controls go | Phone: bottom interaction area [S-L14-053]; car: most important content in the upper half [S-L14-010]; XR touch panels: frequent controls in the lower half [S-L14-043]; Mac: nothing critical at the bottom of a window [S-L14-006]; TV: inside the central 90% [S-L14-027] |
| Ambient light and power | Appearance mode, dimming | Car auto light/dark with negative polarity at night [S-L14-010, S-L14-037]; watch Always On dimming [S-L14-084]; additive XR glasses show black as transparent [S-L14-041] |
| Social setting | Privacy, profiles | TV multiuser profiles [S-L14-003]; Always On hides sensitive data [S-L14-084]; gaze kept private [S-L14-009] |
| Safety | Hard limits (lint rules) | Driving lock-outs [S-L14-031, S-L14-032]; headset comfort and motion rules [S-L14-007, S-L14-008] |

## Part 4: Device matrix

Every cell is sourced or marked [inferred]. "Min target" gives default / minimum where the platform publishes both. Split into two tables so it stays readable.

### Table A: personal, hand-held and desk devices

| Dimension | Phone | Tablet / foldable | Laptop / desktop (native + web) | Large / ultra-wide display | Smartwatch |
|---|---|---|---|---|---|
| Viewing distance | "no more than a foot or two" (30-60 cm) [S-L14-066] | "within about 3 feet" (~90 cm) [S-L14-066] | "about 1 to 3 feet" (30-90 cm) [S-L14-066] | as desktop; wider field [inferred] | "no more than a foot away" [S-L14-001] |
| Typical screen size | Compact width <600 dp [S-L10-025] | Medium 600-839 / expanded 840+ dp; test sizes 841x701 (foldable), 1024x640, 1280x800 dp [S-L10-025, S-L14-069] | 1024-1600 px/dp wide (Chromebook test 1600x900 dp) [S-L14-069]; Carbon lg 1056, max 1584 [S-L03-002] | Material large 1200-1599, XL 1600+ dp [S-L10-025] | Wear 192-240+ dp, breakpoint 225 dp [S-L14-017] |
| Primary input | Touch, one thumb 49% of the time, grip changes often [S-L14-050] | Touch + keyboard + pointer + stylus, combined [S-L14-066] | Keyboard + mouse/trackpad [S-L14-066] | Keyboard + pointer [inferred] | Touch + Digital Crown / rotary; voice; wrist gestures [S-L14-002, S-L14-018, S-L14-047] |
| Min target | iOS 44/28 pt; Android 48 dp [S-L10-012, S-L10-072] | as phone; pointer adds hover/magnetism [S-L14-013] | macOS 28/20 pt; web 24 px AA, 44 AAA [S-L10-012, S-L03-035] | as desktop [inferred] | watchOS 44/28 pt; Wear 48 dp (40 allowed) [S-L10-012, S-L14-018] |
| Body / min text | iOS 17/11 pt; Android body 14-16 sp, min 11 sp [S-L02-001, S-L02-005] | as phone [S-L02-001] | macOS 13/10 pt; Windows 14 epx (12 regular min); web 14-16 px [S-L02-001, S-L02-022, S-L02-008] | as desktop; cap line length at 40-80 characters [S-L03-025, S-L03-073] | watchOS 16/12 pt; Wear Body 16/14/12 sp (Extra Small 10) [S-L14-012, S-L14-022] |
| Navigation model | Bottom tab/nav bar (3-5), stack + back, sheets [S-L10-014, S-L10-025] | Sidebar-adaptable tab bar (iPad), navigation rail, 1-2 panes; folded vs unfolded swap [S-L10-014, S-L14-068] | Menu bar + toolbar + sidebar (macOS); rails/sidebars; multi-column [S-L10-015] | Up to 3 panes; fixed max width for reading, fluid for data [S-L10-025, S-L03-074] | Vertical lists and pages driven by the Crown; shallow hierarchy [S-L14-002, S-L14-001] |
| Typical density | Comfortable; touch spacing 12 px between controls on coarse pointers [S-L03-009] | Comfortable, more panes [inferred] | Dense: 13-14 px body, 8 px control gaps [S-L02-001, S-L03-009] | Dense or editorial by surface type [S-L03-074] | Very low: max 3 glyph or 2 text buttons in a row [S-L14-006] |
| Session length / attention | Avg 72 s (2015) with frequent interruptions; up to an hour or more [S-L14-054, S-L14-066] | Quick actions to hours [S-L14-066] | Minutes to hours of deep focus [S-L14-066] | Long, task-focused [inferred] | Glances "less than a minute"; tasks "within seconds" [S-L14-001, S-L14-015] |
| Motion norms | System transitions; Reduce Motion honored [S-L10-088, S-L10-012] | as phone; pointer effects animate [S-L14-013] | Subtle; Reduce Motion / prefers-reduced-motion [S-L10-012] | as desktop [inferred] | Built-in layout easing; minimal motion in Always On [S-L10-088, S-L14-084] |
| Dark mode norm | Follow system light/dark [S-L10-089] | Follow system [S-L10-089] | Follow system; web may add a toggle [S-L10-089, S-L10-031] | as desktop [inferred] | Dark only (no Dark Mode setting; black backgrounds on Wear) [S-L10-089, S-L10-027] |
| Focus model | None by default; screen-reader focus; hardware keyboard optional [inferred from S-L14-004] | Focus groups: Tab between, arrows within; pointer hover effects [S-L14-004, S-L14-013] | Tab order + visible focus ring + hover (WCAG 2.4.7/2.4.11) [S-L10-083, S-L14-070] | as desktop | No focus ring; Crown scroll position with haptic detents [S-L14-002] |
| Key guidelines | developer.apple.com/design/human-interface-guidelines/designing-for-ios ; m3.material.io ; developer.samsung.com/one-ui [S-L14-066, S-L14-053] | .../designing-for-ipados ; developer.android.com/guide/topics/large-screens/learn-about-foldables [S-L14-066, S-L14-068] | .../designing-for-macos ; w3.org/TR/WCAG22 ; learn.microsoft.com/windows/apps/design [S-L14-066, S-L14-081] | carbondesignsystem.com/elements/2x-grid/usage [S-L03-074] | .../designing-for-watchos ; developer.android.com/design/ui/wear [S-L14-001, S-L14-017] |

### Table B: shared, ambient, vehicle, spatial and non-screen devices

| Dimension | TV (tvOS, Google TV, Fire TV, Tizen) | Car (CarPlay, Android Auto / AAOS) | Spatial (visionOS, Android XR, Meta Horizon) | Voice and AI chat/agent | Kiosk / POS | Game console |
|---|---|---|---|---|---|---|
| Viewing distance | 8-10 ft / 3 m [S-L14-003, S-L14-026, S-L14-029] | Arm's length from the driver's seat [inferred]; glances only | >=1 m for reading (visionOS); panels at 1.75 m (Android XR); touch UI 42-46 cm (Meta) [S-L14-009, S-L14-041, S-L14-043] | n/a for voice; host device's distance for chat [inferred] | Standing at arm's reach; controls 15-48 in above floor [S-L14-072] | TV distance [S-L14-026] |
| Typical screen size | 960x540 dp / epx canvas (1080p at 2x); tvOS 1920x1080 pt [S-L14-023, S-L14-026, S-L10-087] | 800x480 to 1920x720 px (CarPlay) [S-L14-010] | Panels 1024x640 dp default, 384x500 min (Meta); up to 2560x1800 dp in Full Space (Android XR) [S-L14-042, S-L14-087] | Any; voice has none [inferred] | Large portrait or landscape touchscreens [inferred] | 1920x1080 (Xbox UWP renders at 1080p) [S-L14-026] |
| Primary input | Remote (D-pad, clickpad), game controller, voice search [S-L14-005, S-L14-027] | Touch, knobs, touch pads, steering controls, voice [S-L14-010, S-L14-032] | Eyes + pinch; direct touch; hand rays; controllers [S-L14-007, S-L14-043] | Speech; typed prompts [S-L14-061, S-L14-049] | Touch plus tactile keypad and speech output [S-L14-073] | Controller (A/B, bumpers, triggers) [S-L14-075] |
| Min target | tvOS 66/56 pt; Xbox 32 epx min height [S-L14-012, S-L14-026] | 76x76 dp, 23 dp apart (Design for Driving); 64 dp, 24 dp apart (parked apps) [S-L14-037, S-L14-032] | visionOS 60/28 pt, centers 60 pt apart; Android XR 56 dp; Meta 48 dp / 2.5-3 degrees [S-L14-012, S-L14-041, S-L14-043] | n/a | Physical reach band 15-48 in; on-screen target size not specified by ADA/508 [S-L14-072, S-L14-073] | Focus-based [S-L14-075] |
| Body / min text | tvOS 29/23 pt; Fire TV min 14 sp; Xbox 15 epx main / 12 epx supplemental [S-L14-012, S-L14-027, S-L14-026] | Primary 32 dp, secondary 24 dp; parked apps 24 sp min; <=120 Roman characters per item [S-L14-037, S-L14-032] | visionOS 17/12 pt; Android XR min 14 dp [S-L14-012, S-L14-041] | Voice: one-breath responses; chat inherits host type [S-L14-065] [inferred for chat] | Characters >= 3/16 in (4.8 mm) [S-L14-073] | >= 26 px body height at 1080p, scalable to 200% [S-L14-074] |
| Navigation model | Rows and grids of focusable items; left global menu + content rows (Fire TV); Back = parent [S-L14-027, S-L14-005] | System templates; tasks in <= 5 screens [S-L14-010, S-L14-032] | Windows, volumes, ornaments; immersion levels; new window for supplemental content [S-L14-006, S-L14-007] | Turn-taking; lists of 2-5 options [S-L14-065] | Linear task flow [inferred] | Tabs via bumpers, pages via triggers; linear menus loop [S-L14-075] |
| Typical density | Phone-level, not desktop [S-L14-026] | Minimal; no auto-scroll, limited images, no text ads [S-L14-032] | Sparse: 16 pt / 12 mm spacing; avoid dense packing ("Midas touch") [S-L14-009, S-L14-043] | One idea per turn [S-L14-065] | Low [inferred] | Low to medium [inferred] |
| Session length / attention | "often lasting hours", lean-back [S-L14-003] | Glance <= 2 s, task <= 12 s eyes-off-road [S-L14-031] | Minutes to long sessions; limit sustained direct touch [S-L14-007] | Short turns [S-L14-065] | Short, walk-up [inferred] | Hours [inferred] |
| Motion norms | "subtle and fluid" animation; focus scale/parallax [S-L14-003, S-L14-004] | No on-screen animation in templated categories [S-L14-032] | No overwhelming or fast motion; stationary frame of reference; calm periphery [S-L14-007, S-L14-079] | Progress and streaming states instead of motion [S-L14-011] [inferred for streaming] | Standard [inferred] | Game-defined; Reduce Motion options [inferred] |
| Dark mode norm | tvOS light and dark [S-L10-010]; Xbox defaults dark [S-L14-026] | Auto light/dark by ambient light; negative polarity at night [S-L14-010, S-L14-037] | visionOS no Dark Mode, glass adapts; Android XR light and dark; additive glasses: black = transparent [S-L10-089, S-L14-041] | Host device [inferred] | Either polarity with contrast [S-L14-073] | Dark common [inferred] |
| Focus model | Directional focus, every element focusable, 5 states, never auto-moved [S-L14-004] | System-managed for templates; rotary focus by system [S-L14-010] | Gaze hover effect (system, private), separate from keyboard focus [S-L14-004, S-L14-009] | Conversational turn is the "focus" [inferred] | Touch plus tactile keypad navigation [S-L14-073] | Directional focus, logical order, A/B conventions [S-L14-075] |
| Key guidelines | .../designing-for-tvos ; developer.android.com/design/ui/tv ; developer.amazon.com/docs/fire-tv/design-and-user-experience-guidelines.html [S-L14-003, S-L14-023, S-L14-027] | .../carplay ; developer.android.com/docs/quality-guidelines/car-app-quality ; NHTSA 78 FR 24818 [S-L14-010, S-L14-032, S-L14-031] | .../designing-for-visionos ; developer.android.com/design/ui/xr ; developers.meta.com/horizon/design [S-L14-007, S-L14-041, S-L14-043] | .../generative-ai ; microsoft.com/haxtoolkit ; developer.amazon.com/docs/alexa/alexa-design [S-L14-011, S-L14-059, S-L14-061] | access-board.gov/ict ; access-board.gov/ada [S-L14-073, S-L14-072] | learn.microsoft.com/gaming/accessibility/xbox-accessibility-guidelines [S-L14-074, S-L14-075] |

## Part 5: Decision Cards

### DC-L14-01: Device classes in scope and their support tier
- **Block path:** Platforms > Scope > Device classes
- **Questions the designer answers:** Which device classes must look and work great on day one, which only need to work, and which are out of scope? Will we ever ship on a watch, TV, car or headset? Do any of our users operate the product while driving, walking, or standing at a public kiosk?
- **Options:**
  - **Tiered support (Google's model).** Android's adaptive quality tiers: ready (runs full-window, no letterboxing), optimized (layouts for every size, good input support), differentiated (posture-, stylus-, multitasking-specific UX) [S-L14-069]. Car app quality uses the same idea: car ready, car optimized, car differentiated [S-L14-032]. Wear OS uses "ready for all screen sizes", "responsive", "adaptive and differentiated" [S-L14-017].
  - **Surface-first for constrained devices.** Watch apps are often secondary to complications, tiles and notifications [S-L14-001, S-L14-015]; car apps are content for system templates [S-L14-010].
  - **Everything first-class.** Spotify's Encore spans mobile, web, desktop, TV and watch (L10 [S-L10-040]).
- **Visual effect:** Each first-class class adds a visibly different silhouette: vertical Crown lists on watch, focus rows on TV, template cards in the car, floating glass windows in space [S-L14-002, S-L14-004, S-L14-010, S-L14-007]. "Adapted only" classes look like the phone app stretched or letterboxed, which Google now penalizes on large screens [S-L14-069].
- **Depends on (upstream):** DC-L10-01 (platforms), audience and use contexts.
- **Affects (downstream):** every other L14 card; the token modifier set; the component inventory (glance components, focus states, templates).
- **Token encoding:** a context modifier in the resolver, e.g. `context = handheld | wrist | desk | lean-back | vehicle | spatial | kiosk` [inferred; L07 owns resolver syntax]. Keep it separate from `platform` (L10), because the same OS spans several contexts (Android: phone, Wear, TV, Auto, XR) [S-L14-017, S-L14-023, S-L14-032, S-L14-041].
- **Platform notes:** Android forces the tablet/foldable class on apps (orientation locks ignored at 600 dp+, L10 [S-L10-020, S-L10-021]); iPadOS 26 windowing makes arbitrary sizes normal [S-L14-067].
- **Accessibility constraints:** each class brings its own assistive-tech matrix (Part 2.2).
- **Default + heuristic:** Default: phone + tablet/foldable + desktop/web as first-class, TV/watch/car/spatial off until a named use case exists. Rule of thumb: a device class becomes first-class when a core task is done there, not when the app merely runs there.
- **Evidence:** [S-L14-001, S-L14-002, S-L14-004, S-L14-007, S-L14-010, S-L14-015, S-L14-017, S-L14-032, S-L14-041, S-L14-067, S-L14-069]

### DC-L14-02: One component set with device variants, or separate sets per device
- **Block path:** Components > Architecture > Device variants
- **Questions the designer answers:** Is a TV button the same component as a phone button with different tokens, or a different component? Do watch and car need their own libraries? How do we keep names and behavior consistent?
- **Options:**
  - **One set, tokens vary by mode.** Spectrum ships desktop and mobile values for every size token (L03 [S-L03-044]); Carbon switches 12 components into an "AI presence" variable mode without changing their function [S-L14-058]; Android's TV Material library reuses phone M3 type values in sp [S-L14-025].
  - **Shared foundations, separate component libraries per device.** Google publishes distinct Compose libraries for Wear (Wear Compose Material 3, with arc text, edge buttons) and TV (TV Material, with focus-driven cards and carousels), each with its own type-scale tokens [S-L14-022, S-L14-025, S-L10-026].
  - **System-rendered templates.** Car: the app supplies data, the OS renders components [S-L14-010, S-L14-032].
- **Visual effect:** One set keeps the brand identical and cheap to maintain but risks phone-shaped components on a watch or TV. Separate libraries look native per device (round-aware watch buttons, big focusable TV cards) at the cost of duplicated specs [inferred].
- **Depends on (upstream):** DC-L14-01, DC-L10-03 (sharing layer).
- **Affects (downstream):** Figma library structure (L07/L12), code packages, documentation.
- **Token encoding:** shared semantic names (`button.primary.bg`) resolved per context mode; device-only components (complication, tile, focus card, template list item) live in a device namespace (`wrist.tile.*`, `leanback.card.*`) [inferred].
- **Platform notes:** Wear and TV components differ in behavior, not only size (rotary scrolling, focus scaling), which is why Google split them [S-L14-018, S-L14-004] [inferred for Google's motive].
- **Accessibility constraints:** state semantics (focused, selected, disabled) must be identical across variants so screen readers announce the same thing [inferred from S-L14-080].
- **Default + heuristic:** Default: one set for phone, tablet, desktop and web with context modes; separate small libraries for watch and TV; template adapters (no custom components) for car. Rule of thumb: if the input model changes (touch vs D-pad vs Crown), make a new component; if only size changes, make a mode.
- **Evidence:** [S-L03-044, S-L10-026, S-L14-004, S-L14-010, S-L14-018, S-L14-022, S-L14-025, S-L14-032, S-L14-058]

### DC-L14-03: Target-size policy by input modality
- **Block path:** Foundations > Sizing > Targets > By input
- **Questions the designer answers:** What's the smallest hit area per device? Is it keyed to device or to input? Can density modes shrink it?
- **Options (real values):** pointer: macOS 28/20 pt, web 24 px AA [S-L10-012, S-L03-035]; finger, handheld: 44 pt / 48 dp, Wear 48 dp (40 allowed) [S-L10-012, S-L14-018]; remote focus: tvOS 66/56 pt, Xbox 32 epx min height [S-L14-012, S-L14-026]; gaze and hands: visionOS 60 pt, Android XR 56 dp, Meta 48 dp with 2.5-3 degree minimum [S-L14-012, S-L14-041, S-L14-043]; vehicle: 76x76 dp (Design for Driving), 64 dp for parked apps [S-L14-037, S-L14-032].
- **Visual effect:** Larger minimums spread controls out and make screens calmer and more "chunky" (TV tiles, car buttons, spatial buttons with 16 pt gaps); pointer-first UIs can pack toolbars tightly [inferred].
- **Depends on (upstream):** DC-L14-01, input modalities per class (Part 2.1).
- **Affects (downstream):** control heights, icon-button padding, list rows, spacing between targets, focus headroom on TV.
- **Token encoding:** `size.target.min` and `space.target.gap` as fixed tokens per input mode: `{pointer: 24, touch: 44|48, remote: 66, gaze: 60, vehicle: 76}`, plus `space.target.gap` `{pointer: 8, touch: 12, gaze: 16, vehicle: 23}` [S-L03-009, S-L14-009, S-L14-037] [inferred structure]. Density modes must not override them (L03 DC-L03-11).
- **Platform notes:** web detects input with `pointer: coarse | fine` (L10 [S-L10-073]); spatial sizes should be checked in angle, not only dp [S-L14-043].
- **Accessibility constraints:** WCAG 2.5.8 (24 px) and 2.5.5 (44 px AAA) [S-L03-035, S-L03-036]; car 23-24 dp gaps and 24 dp from screen edges [S-L14-037, S-L14-032].
- **Default + heuristic:** Default: key targets to input, not device, and pick the largest input the device supports (a touch laptop gets touch targets on its touch surfaces). Rule of thumb: the less stable the hand or the farther the eye, the bigger the target.
- **Evidence:** [S-L03-009, S-L03-035, S-L03-036, S-L10-012, S-L10-073, S-L14-009, S-L14-012, S-L14-018, S-L14-026, S-L14-032, S-L14-037, S-L14-041, S-L14-043]

### DC-L14-04: Type sizing by viewing-distance class
- **Block path:** Foundations > Typography > Scale > Distance classes
- **Questions the designer answers:** How much bigger is body text on a TV than on a phone? Do we keep one ramp and scale it, or ship a ramp per device? How small can glanceable text go?
- **Options:**
  - **Native ramp per device.** Apple: watch 16/12, phone 17/11, Mac 13/10, TV 29/23, visionOS 17/12 pt [S-L14-012]. Wear M3: Body 16/14/12 sp, Arc 18/15/14, Numerals 24-60 [S-L14-022].
  - **Same sp values, different canvas.** Android TV Material reuses phone sizes (Body Medium 14 sp) on a 960 dp canvas, so text is physically larger [S-L14-025, S-L14-023].
  - **Distance-scaled minimums.** Xbox 15/12 epx on TV [S-L14-026]; Xbox games 26 px (TV) vs 18 px (PC/VR) body height at 1080p [S-L14-074]; car 32/24 dp [S-L14-037].
- **Visual effect:** Distance-scaled type keeps the same perceived size, so a TV screen shows about as many words as a phone screen, and a car screen fewer [S-L14-026, S-L14-032] [inferred for "as many words"]. Watch ramps add large numerals and curved arc text, which gives watch faces their look [S-L14-022].
- **Depends on (upstream):** DC-L14-01, L02 base size and ratio.
- **Affects (downstream):** all type tokens, icon sizes, line lengths, component heights, truncation rules.
- **Token encoding:** `type.body.size` with a `distance` mode: `{wrist: 16, handheld: 17, desk: 13-14, leanback: 29 (pt) or 14 (sp on the 960 dp canvas), vehicle: 32 (primary), spatial: 17}` [S-L14-012, S-L14-022, S-L14-037, S-L02-022] [inferred structure]. Store the unit per platform (pt, sp, epx, dp) as L10 DC-L10-08 describes.
- **Platform notes:** Wear text 20 sp and up doesn't scale with user settings [S-L14-021]; visionOS points are angles [S-L14-008].
- **Accessibility constraints:** per-platform minimums (above) are floors; Section 508 kiosks 4.8 mm characters [S-L14-073]; console text scalable to 200% [S-L14-074].
- **Default + heuristic:** Default: one semantic ramp with distance modes seeded from each platform's native defaults. Rule of thumb: when moving to a farther device, keep the role and roughly the visual angle (about 0.3-0.5 degrees for body text, Invariant I-3), not the number.
- **Evidence:** [S-L02-022, S-L14-008, S-L14-012, S-L14-021, S-L14-022, S-L14-023, S-L14-025, S-L14-026, S-L14-032, S-L14-037, S-L14-073, S-L14-074]

### DC-L14-05: Navigation container per device class
- **Block path:** Patterns > Navigation > Device containers
- **Questions the designer answers:** What carries top-level navigation on each device? How many steps may a task take? Where does "back" live?
- **Options:** phone bottom bar (3-5) and stack [S-L10-014]; tablet/foldable rail or sidebar and 1-2 panes, swapping on fold [S-L10-025, S-L14-068]; desktop menu bar, toolbar, sidebar [S-L10-015]; watch vertical Crown pages and lists [S-L14-002]; TV left global menu plus horizontal content rows [S-L14-027], focusable grids with 40 pt gaps [S-L14-006]; car system templates, five screens max [S-L14-032]; spatial windows with ornaments for toolbars and extra windows for supplemental content [S-L14-006]; console tabs on bumpers, pages on triggers [S-L14-075]; voice turns with 2-5 options [S-L14-065].
- **Visual effect:** The container is the most recognizable device signature: tab bar vs rail vs menu bar vs content rows vs floating ornament [inferred].
- **Depends on (upstream):** DC-L14-01, DC-L10-09, information architecture (L08).
- **Affects (downstream):** app-shell templates, safe-area handling, search placement, back behavior.
- **Token encoding:** component tokens per container (`nav.bar.*`, `nav.rail.*`, `leanback.menu.*`, `wrist.page.*`) plus a rule table "context x breakpoint -> container" [inferred].
- **Platform notes:** tvOS Back goes to the parent, not necessarily the previous screen [S-L14-005]; Xbox recommends opening the nav pane with the View button or by moving focus to the far left [S-L14-026].
- **Accessibility constraints:** consistent navigation placement across screens (WCAG 3.2.3, cited by Xbox) [S-L14-075]; every destination reachable by keyboard/D-pad [S-L14-004].
- **Default + heuristic:** Default: keep destinations identical across devices and swap only the container (L10 DC-L10-09). Rule of thumb: count steps on the most constrained device you support (car 5 screens, TV 6 clicks edge to edge) and design the IA to fit that [S-L14-032, S-L14-026].
- **Evidence:** [S-L10-014, S-L10-015, S-L10-025, S-L14-002, S-L14-004, S-L14-005, S-L14-006, S-L14-026, S-L14-027, S-L14-032, S-L14-065, S-L14-068, S-L14-075]

### DC-L14-06: Interaction state model across inputs
- **Block path:** Foundations > Interaction > States
- **Questions the designer answers:** Which states does every component define? How does "focused" look on a TV vs a laptop vs a headset? Is gaze hover the same as mouse hover?
- **Options:**
  - **Desktop/web set:** rest, hover, focus-visible, pressed, selected, disabled; hover content must satisfy WCAG 1.4.13 [S-L14-071]; focus indicator ideally 2 px perimeter area and 3:1 change [S-L14-070].
  - **Tablet pointer effects:** highlight, lift, hover with magnetism [S-L14-013].
  - **TV focus set:** unfocused, focused (scale, elevation, illumination, animation), highlighted (pressed), selected, unavailable; assets sized for the focused scale [S-L14-004]; Samsung: focus distinct from selected [S-L14-029].
  - **Spatial:** system-drawn gaze hover effect that is not focus; custom hover effects only for special moments [S-L14-009, S-L14-004]; Meta: hover, pressed with audio [S-L14-043].
  - **Watch:** Crown feedback and haptic detents [S-L14-002].
- **Visual effect:** A TV focus state is large and animated (items grow and lift); a desktop focus ring is thin and static; a headset hover is a soft system glow the app can't fully control [S-L14-004, S-L14-009] [inferred for "soft glow" wording].
- **Depends on (upstream):** Part 2.1 input table, L04 elevation and motion.
- **Affects (downstream):** state tokens (`state.focus.ring.width`, `state.focus.scale`, `state.hover.overlay`), component specs, asset resolution for focused sizes.
- **Token encoding:** `state.focus.*` resolved by context: `{desk: {ring: 2px, offset: 2px}, leanback: {scale: 1.1, elevation: high, ring: optional}, spatial: {system}}` [inferred values except the 2 px perimeter from S-L14-070]. L04/L07 own the exact token names.
- **Platform notes:** iPad and macOS only need focus on content elements because Full Keyboard Access reaches controls; tvOS needs focus on everything [S-L14-004].
- **Accessibility constraints:** WCAG 2.4.7, 2.4.11, 2.4.13 [S-L10-083, S-L14-070]; don't convey state by color alone (Apple: avoid relying solely on color to convey an important detail) [S-L14-012].
- **Default + heuristic:** Default: define all states once per component; each context renders the subset its inputs can trigger. Rule of thumb: focus should be visible from the farthest distance the device is used at.
- **Evidence:** [S-L10-083, S-L14-002, S-L14-004, S-L14-009, S-L14-013, S-L14-029, S-L14-043, S-L14-070, S-L14-071]

### DC-L14-07: Glanceable surfaces tier (complications, tiles, widgets, notifications, Live Activities)
- **Block path:** Patterns > Surfaces > Glanceable
- **Questions the designer answers:** What does the user need without opening the app? Which piece of data goes on the watch face, the tile, the notification, the car widget?
- **Options:** Google's priority matrix (complication = one datum; notification = urgent event; tile = one or two items; app = everything) [S-L14-015]; Apple watch surfaces (complications, notifications, Smart Stack, Always On) [S-L14-001]; tiles "immediate, predictable, relevant" [S-L14-020]; CarPlay widgets and Live Activities (iOS 26) [S-L14-047]; visionOS 26 widgets that persist in the room [S-L14-047].
- **Visual effect:** Glance surfaces look like data, not UI: big numerals, one metric, a status color, almost no chrome [S-L14-022, S-L14-020] [inferred for "look like data"].
- **Depends on (upstream):** DC-L14-01, content strategy.
- **Affects (downstream):** a "glance" component family, numeral type styles, data-refresh and redaction rules (Always On hides sensitive data) [S-L14-084].
- **Token encoding:** numeral styles (`type.numeral.lg` etc., as Wear M3 does), compact spacing, and an `ambient` mode that dims secondary content [S-L14-022, S-L14-084] [inferred for mode].
- **Platform notes:** Always On on iPhone and Watch dims and slows updates [S-L14-084]; Wear ambient mode similar [S-L14-015].
- **Accessibility constraints:** content descriptions must match exactly what's shown [S-L14-018].
- **Default + heuristic:** Default: for any device with glance surfaces, design the complication/tile first, then the app. Rule of thumb: one number or one status per glance.
- **Evidence:** [S-L14-001, S-L14-015, S-L14-018, S-L14-020, S-L14-022, S-L14-047, S-L14-084]

### DC-L14-08: Motion policy per device class
- **Block path:** Foundations > Motion > Device policy
- **Questions the designer answers:** Can we animate at all on this device? How much, where in the field of view, and what happens with Reduce Motion?
- **Options:** phone/tablet/desktop: system transitions plus brand micro-motion, Reduce Motion honored (L10 [S-L10-088, S-L10-012]); TV: "subtle and fluid" animation, focus scale and parallax [S-L14-003, S-L14-004]; watch: built-in layout easing, minimal motion in Always On [S-L10-088, S-L14-084]; car: no animated elements in templated categories, canvas animation only while parked if relevant [S-L14-032]; spatial: no overwhelming, jarring or fast motion, keep a stationary frame of reference, calm periphery, avoid ~0.2 Hz oscillation [S-L14-007, S-L14-079, S-L10-088]; e-ink: effectively none because refresh blinks [S-L14-078].
- **Visual effect:** The same brand can feel lively on phone, cinematic on TV, completely still in the car and slow and grounded in a headset [inferred].
- **Depends on (upstream):** L04 motion tokens, L06 personality, DC-L14-01.
- **Affects (downstream):** duration/easing/spring tokens, transitions, loading indicators, focus animation.
- **Token encoding:** a `motion` context override: `{handheld: full, leanback: subtle, wrist: minimal, vehicle: none, spatial: comfort, paper: none}` mapping to duration multipliers or "disabled" [inferred]; Material already varies spring values by device class (wearable, phone, tablet) (L10 [S-L10-024]).
- **Platform notes:** visionOS motion sickness risk is higher, so reduce speed and intensity especially in the periphery [S-L14-079].
- **Accessibility constraints:** WCAG 2.3.1 three flashes [S-L14-081]; Reduce Motion / prefers-reduced-motion (L10 [S-L10-012]).
- **Default + heuristic:** Default: motion budget shrinks as attention narrows or as the display wraps the body. Rule of thumb: if the user is driving, walking or wearing the screen on their face, animate less.
- **Evidence:** [S-L10-012, S-L10-024, S-L10-088, S-L14-003, S-L14-004, S-L14-007, S-L14-032, S-L14-078, S-L14-079, S-L14-081, S-L14-084]

### DC-L14-09: Appearance modes per device class
- **Block path:** Foundations > Color > Appearance by device
- **Questions the designer answers:** Which devices get light and dark, which are dark-only, which switch automatically by ambient light, and which render black as transparent?
- **Options:** follow system on phone, tablet, desktop, web (L10 [S-L10-089]); dark only on watches (L10 [S-L10-089, S-L10-027]); Xbox defaults to dark [S-L14-026]; car auto-switches by ambient light and must be light-on-dark at night [S-L14-010, S-L14-037]; visionOS has no Dark Mode and glass adapts to surroundings (L10 [S-L10-008, S-L10-089]); Android XR supports light and dark, but on additive wired glasses black is transparent [S-L14-041]; kiosks may use either polarity with contrast [S-L14-073].
- **Visual effect:** Dark-first devices (watch, TV, car at night) make brand colors glow and push the designer toward fewer, brighter accents; additive glasses turn dark UI into floating light shapes with no background [S-L14-041] [inferred for "floating"].
- **Depends on (upstream):** L01 palette and dark mapping, DC-L10-17.
- **Affects (downstream):** color modes, imagery, elevation (tone vs shadow), TV color-safety checks.
- **Token encoding:** `appearance` mode plus per-context availability: `wrist: [dark]`, `vehicle: [day, night]` (auto), `spatial: [system]`, `additive-glasses: [light-on-transparent]` [inferred structure].
- **Platform notes:** TV color varies by set; avoid subtle differences; Xbox scales colors to the TV-safe range automatically [S-L14-026].
- **Accessibility constraints:** 4.5:1 in every mode, including car night mode [S-L14-037].
- **Default + heuristic:** Default: system-following light/dark where the platform has it; dark-only for watch; day/night auto for car. Rule of thumb: the darker and closer the environment (night car, headset, bedroom TV), the darker the default.
- **Evidence:** [S-L10-008, S-L10-027, S-L10-089, S-L14-010, S-L14-026, S-L14-037, S-L14-041, S-L14-073]

### DC-L14-10: Safe zones and edge policy per device
- **Block path:** Foundations > Layout > Device safe zones
- **Questions the designer answers:** How far from the edge must text and controls sit on this device? What can bleed to the edge?
- **Options:** phone safe areas and edge-to-edge insets (L10/L03 [S-L10-013, S-L03-052]); TV 5% overscan: Android TV 48 dp / 27 dp (58/28 recommended), Xbox 48/27 epx, tvOS 80/60 pt, Fire TV outer 5% [S-L14-023, S-L14-026, S-L14-006, S-L14-027]; round watches use percentage margins [S-L14-017]; foldables keep controls and text off the hinge [S-L14-068]; car parked apps keep targets 24 dp from screen edges [S-L14-032]; spatial keeps primary content in the central 41 degrees (Android XR) and avoids head-locked placement [S-L14-041, S-L14-008]; kiosks keep operable parts 15-48 in high [S-L14-072].
- **Visual effect:** TV and watch layouts look inset and centered; backgrounds and scrolling rows still bleed to the edge so the UI doesn't look boxed in [S-L14-026].
- **Depends on (upstream):** DC-L14-01; L03 DC-L03-20.
- **Affects (downstream):** page margins, app-shell padding, carousels, dialogs on foldables.
- **Token encoding:** `layout.safe.*` per context as fixed dimensions (TV) or percentages (watch); insets that the OS provides stay runtime values (L03 DC-L03-20) [inferred].
- **Platform notes:** Xbox apps are boxed into the TV-safe area by default unless they opt into core window bounds [S-L14-026].
- **Accessibility constraints:** WCAG 2.4.11 focus not obscured (L10 [S-L10-083]); TV focus must stay inside the safe area while rows scroll [S-L14-026].
- **Default + heuristic:** Default: backgrounds to the edge, interactive content inside the context's safe zone. Rule of thumb on TV: nothing you need to read or select in the outer 5%.
- **Evidence:** [S-L03-052, S-L10-013, S-L14-006, S-L14-008, S-L14-017, S-L14-023, S-L14-026, S-L14-027, S-L14-032, S-L14-041, S-L14-068, S-L14-072]

### DC-L14-11: Safety and distraction limits as enforceable rules
- **Block path:** Governance > Linting > Context safety rules
- **Questions the designer answers:** Which designs must the builder refuse or flag for driving, walking or immersive contexts? Are these guidelines or requirements?
- **Options:**
  - **Driving (US voluntary + store requirements).** NHTSA: glances <= 2 s, total <= 12 s; lock out video, certain images, auto-scrolling text, manual text entry for messaging/browsing, and reading text [S-L14-031]. Google Play car quality: <= 5 screens per task, no animation, no auto-scroll, 2 s button response, 10 s load, no autoplay [S-L14-032]. Design for Driving: <= 120 characters per text item, 76 dp targets, night negative polarity [S-L14-037].
  - **Spatial comfort.** Content in field of view, not head-locked, at least 1 m for reading, no fast motion without a stationary reference, minimum immersion [S-L14-007, S-L14-008, S-L14-009].
  - **Watch.** Tasks within seconds [S-L14-015]; Always On hides sensitive data [S-L14-084].
- **Visual effect:** Car screens become large, sparse, still and high-contrast; headset UI becomes calm, centered and farther away [S-L14-032, S-L14-037, S-L14-008] [inferred for the adjectives].
- **Depends on (upstream):** DC-L14-01.
- **Affects (downstream):** builder lint rules, component availability per context (no video component in `vehicle` while driving), content length limits.
- **Token encoding:** not tokens; context rules in the builder's validator, e.g. `vehicle.maxTextChars = 120`, `vehicle.maxTaskScreens = 5`, `vehicle.animation = false`, `spatial.minDistance = 1m` [S-L14-037, S-L14-032, S-L14-009] [inferred structure].
- **Platform notes:** NHTSA guidelines are voluntary in the US; Google Play and Apple CarPlay rules are store requirements [S-L14-031, S-L14-032, S-L14-010]. Other regions' rules (EU, Japan) were not researched [gap].
- **Accessibility constraints:** contrast 4.5:1 [S-L14-037]; voice alternatives [S-L14-032].
- **Default + heuristic:** Default: make these hard errors, not warnings, in any `vehicle` context. Rule of thumb: if a design needs a second glance to understand, it fails in a car.
- **Evidence:** [S-L14-007, S-L14-008, S-L14-009, S-L14-010, S-L14-015, S-L14-031, S-L14-032, S-L14-037, S-L14-084]

### DC-L14-12: Conversational and AI surface
- **Block path:** Patterns > Conversational > AI chat, voice and agents
- **Questions the designer answers:** Does the product have an assistant or AI features? How is AI-generated content marked? How does the conversation render on each device?
- **Options:**
  - **Chat surface** (Apple's Siri app, Carbon AI chat) [S-L14-049, S-L14-058].
  - **AI presence as a mode on normal components** (Carbon: AI label, explainability popover, glow/gradient tokens, revert to AI) [S-L14-058].
  - **Voice-only turns** (Alexa one-breath, 2-5 options) [S-L14-065].
  - **Look-to-act / ambient** (Vision Pro gaze-based search and actions in visionOS 27) [S-L14-049].
- **Visual effect:** AI presence styling gives generated content a recognizable "lit" treatment; Carbon warns against using it as decoration [S-L14-058]. Chat surfaces add a message list, composer and suggestion chips that look alike across products [inferred].
- **Depends on (upstream):** DC-L14-01, L06 voice and tone.
- **Affects (downstream):** AI color tokens, label component, progress/streaming states, feedback controls (thumbs, retry, undo), confirmation dialogs before agent actions.
- **Token encoding:** `ai.*` color and effect tokens inside each theme (Carbon's approach) and an `aiPresence = on | off` mode on components [S-L14-058]; message and composer component tokens [inferred].
- **Platform notes:** On watch, car and speaker the same conversation becomes short voice turns or cards [S-L14-015, S-L14-032, S-L14-065] [inferred for cards].
- **Accessibility constraints:** disclose AI, allow correction and dismissal, confirm irreversible actions (Apple, Microsoft) [S-L14-011, S-L14-060]; Carbon's AI glow spread is limited to keep contrast [S-L14-058].
- **Default + heuristic:** Default: treat AI as a cross-device pattern family plus an optional component mode; always pair generated output with Edit/Undo/Retry [S-L14-011]. Rule of thumb: the user should always know what the AI did, why, and how to take it back.
- **Evidence:** [S-L14-011, S-L14-015, S-L14-032, S-L14-049, S-L14-058, S-L14-060, S-L14-065]

### DC-L14-13: Information density per device class
- **Block path:** Foundations > Space > Density by context
- **Questions the designer answers:** How much should one screen show on this device? Is TV density like desktop (big screen) or like phone (far away)?
- **Options:** desktop dense (13-14 px body, 8 px gaps, compact rows) [S-L02-001, S-L03-009]; phone comfortable [S-L03-009]; TV "comparable to ... a mobile phone, rather than ... a desktop" [S-L14-026]; watch at most 2-3 buttons in a row [S-L14-006]; car minimal (limited images, no ads, short text) [S-L14-032]; spatial sparse with 16 pt / 12 mm spacing and no dense packing [S-L14-009, S-L14-043].
- **Visual effect:** Using desktop density on a TV makes text unreadable and focus travel long; using phone density on a desktop wastes space [S-L14-026] [inferred for desktop].
- **Depends on (upstream):** DC-L14-03, DC-L14-04, L03 DC-L03-10.
- **Affects (downstream):** spacing modes, row heights, grid column counts (tvOS 2-9 columns with 40 pt gaps) [S-L14-006].
- **Token encoding:** density keyed to context rather than screen size: `density = {desk: compact, handheld: comfortable, leanback: comfortable, wrist: sparse, vehicle: sparse, spatial: sparse}` [inferred].
- **Platform notes:** Material says density should not change automatically across breakpoints unless the user changes it (L03 [S-L03-029]); context is a different axis from breakpoint [inferred].
- **Accessibility constraints:** targets fixed per I-1.
- **Default + heuristic:** Default: density follows viewing distance and input, not pixel count. Rule of thumb: a 65-inch TV is a far-away phone.
- **Evidence:** [S-L02-001, S-L03-009, S-L03-029, S-L14-006, S-L14-009, S-L14-026, S-L14-032, S-L14-043]

### DC-L14-14: Accessibility test matrix per device class
- **Block path:** Governance > Accessibility > Device test matrix
- **Questions the designer answers:** Which assistive technologies and settings must each shipped device class be tested with?
- **Options:** see Part 2.2: VoiceOver on every Apple platform [S-L14-080]; TalkBack on phone, Wear and TV [S-L10-072, S-L14-018, S-L14-086]; Switch Control, Voice Control, Full Keyboard Access, AssistiveTouch, Pointer Control [S-L14-079]; visionOS Dwell Control and Head Pointer [S-L14-007]; text scaling (Dynamic Type AX5, Android 200%, watch 140%, TV font scale, console 200%) [S-L10-011, S-L10-071, S-L10-012, S-L14-086, S-L14-074]; kiosks speech output and tactile controls [S-L14-073].
- **Visual effect:** Passing large-text tests forces stacked layouts and growing containers on every device (L02 DC-L02-21) [S-L02-001].
- **Depends on (upstream):** DC-L14-01.
- **Affects (downstream):** QA checklists, component acceptance criteria, documentation per component.
- **Token encoding:** not tokens; the builder should attach a per-context checklist to each component [inferred].
- **Platform notes:** in visionOS, custom gestures lose hand input while VoiceOver runs, so every custom gesture needs a standard alternative [S-L14-080].
- **Accessibility constraints:** WCAG 2.2 AA for web; platform guidance elsewhere [S-L14-081].
- **Default + heuristic:** Default: one screen reader, one motor alternative and the largest text size per shipped device class. Rule of thumb: if a device class is first-class (DC-L14-01), its assistive tech is first-class too.
- **Evidence:** [S-L02-001, S-L10-011, S-L10-012, S-L10-071, S-L10-072, S-L14-007, S-L14-018, S-L14-073, S-L14-074, S-L14-079, S-L14-080, S-L14-081, S-L14-086]

## Decision graph (what drives what for devices)

```
Use contexts (who, where, doing what)
  -> DC-L14-01 device classes and tiers  (also constrained by DC-L10-01 platforms)
       -> DC-L14-02 one set + context modes vs separate device libraries
       -> Part 2 input modalities per class
            -> DC-L14-03 target sizes and gaps (by input)      -> control heights, list rows (L03)
            -> DC-L14-06 state model (hover, focus, gaze, TV)  -> state tokens, assets at focused scale (L04)
       -> viewing distance per class
            -> DC-L14-04 type by distance class                -> type tokens, icon sizes (L02)
            -> DC-L14-13 density by context                    -> spacing modes, grid columns (L03)
       -> attention and safety per class
            -> DC-L14-05 navigation container and step budget  -> app shell, IA (L08)
            -> DC-L14-07 glanceable surfaces                   -> glance components, numerals
            -> DC-L14-11 safety lint rules                     -> validator (L11)
            -> DC-L14-08 motion budget                         -> motion tokens (L04)
       -> environment (light, edges, optics)
            -> DC-L14-09 appearance modes                      -> color modes (L01)
            -> DC-L14-10 safe zones                            -> layout margins (L03)
       -> DC-L14-12 conversational/AI surface (cross-device)   -> AI tokens, chat components
       -> DC-L14-14 accessibility test matrix
```

## Builder questionnaire extract (plain-language, in order)

1. Where will people use this: in their hand, at a desk, on the couch, in a car, on their wrist, in a headset, at a public kiosk, or by voice? Which of those are day-one?
2. For each: what do they touch or press with (finger, mouse, keyboard, pen, remote, crown, eyes and hands, voice)?
3. How far away is the screen, and how long do they look at it per visit?
4. Is anyone moving or driving while using it? (If yes, safety rules switch on.)
5. Does the device show things without opening the app (watch face, tile, widget, notification, car widget)? What single number or status belongs there?
6. Does the product have an assistant or AI-generated content? How should AI content be marked?
7. Which assistive technologies must each device class pass (screen reader, switch, voice control, largest text)?

## Cross-lane notes (for the orchestrator to post; this subagent does not edit BOARD.md)

- **L10 / L07:** add a `context` modifier (handheld, wrist, desk, lean-back, vehicle, spatial, kiosk) separate from `platform`; one OS spans several contexts (Android: phone, Wear, TV, Auto, XR) [S-L14-017, S-L14-023, S-L14-032, S-L14-041].
- **L03:** target tokens should key to input (pointer 24, touch 44/48, remote 66, gaze 56-60, vehicle 76) and be immune to density; TV overscan (5%: 48/27 dp or epx; tvOS 80/60 pt) and round-watch percentage margins belong in the safe-area card [S-L14-023, S-L14-026, S-L14-006, S-L14-017, S-L14-037].
- **L02:** official Wear M3 and TV Material type-scale values are in AndroidX source (TypeScaleTokens.kt); TV reuses phone sp values on a 960 dp canvas; Wear text 20 sp+ doesn't scale [S-L14-022, S-L14-025, S-L14-021].
- **L04:** motion budget per context (none in car, calm periphery in headsets, subtle on TV); Android XR publishes spatial elevation levels in dp (16/32/56) that could seed a depth token scale [S-L14-032, S-L14-079, S-L14-087].
- **L08:** component inventory needs a glance family (complication, tile, widget), TV focus cards and rows, car template adapters, spatial orbiters/ornaments, and a chat family (message list, composer, suggestion chips, streaming state, retry/undo) [S-L14-015, S-L14-004, S-L14-010, S-L14-087, S-L14-011].
- **L01 / L07:** IBM Carbon models "AI presence" as a Figma variable mode plus AI color tokens inside each theme [S-L14-058].
- **L11:** the builder's validator can enforce car rules (<=5 screens, no animation, <=120 characters per text item, 76 dp targets, night negative polarity) as hard errors [S-L14-032, S-L14-037, S-L14-031].
- **L13:** device evidence for Fitts's law (target size rises with input imprecision, I-2) and Hick's law (2-5 voice options, car step limits) [S-L14-051, S-L14-065, S-L14-032] [inferred mapping].

## Community signal reconciliation (sources/COMMUNITY-SIGNAL.md)

- **Liquid Glass across Apple devices.** COMMUNITY-SIGNAL records a readability backlash to iOS 26 glass and Apple's response (Clear/Tinted option in 26.1, a transparency slider in 27) [S-L00-019, S-L00-018]; the 27 release confirms the slider "from ultraclear to fully tinted" [S-L14-049], and NN/g's 2025 top list includes "Liquid Glass Is Cracked, and Usability Suffers in iOS 26" [S-L14-056]. watchOS 26 and tvOS 26 adopted Liquid Glass too [S-L14-047]. Implication for this lane: glass on watch and TV focus elements should be tested at both slider extremes and with Reduce Transparency; no device-specific dispute was found.
- **AI dominates community discussion** [S-L00-034]; this lane's DC-L14-12 reflects that with primary sources (Apple HIG, Carbon, Microsoft), not community posts.
- **NN/g is Tier B; Jakob Nielsen's personal commentary is disputed** [S-L00-034]. This lane uses one NN/g article by Raluca Budiu (2015) for the mobile-session figure and flags it as dated [S-L14-054].
- No community claims about TV, car, watch or spatial values were found to contradict the official sources used here.

## Open questions / gaps

- **Regional driving rules.** Only US NHTSA (voluntary) was read; European (e.g., the European Statement of Principles on HMI) and Japanese (JAMA) guidelines were not researched [gap].
- **Design for Driving is frozen publicly.** Google moved it to a partner-only site from 2026-03-11; the public pages used here are dated 2024-07-23 and may be out of date [S-L14-035].
- **Dated TV sources.** Fire TV's design page is from 2020 and Microsoft's 10-foot page is archived (2020 content); Vega OS docs cover focus only [S-L14-027, S-L14-026, S-L14-089]. Samsung Tizen publishes no text or target sizes in the pages read [S-L14-029].
- **Apple device dimensions.** The HIG layout JSON no longer contains the device specification tables (watch and phone sizes in pt), so watch screen sizes in points are not given here [S-L14-006].
- **visionOS point-to-angle conversion** is not published; angular comparisons for visionOS are not possible [S-L14-008].
- **Car viewing distance** and **kiosk on-screen target size** have no official number in the sources read [inferred cells in the matrix].
- **E-ink** rests on a vendor blog; the CHI 2026 e-paper design-system paper could not be read (bot check not bypassed) [S-L14-077, S-L14-078].
- **AI chat patterns** use Apple, Carbon and Microsoft; NN/g's chatbot articles (response outlining, conversation types) and Google PAIR were located but not read [S-L14-055].
- **Smart glasses** (display-less AI glasses and small heads-up displays) are not covered beyond Android XR's note on additive displays [S-L14-041].
- **Dated research.** Hoober (2013, 2017) and NN/g's 72 s session figure (2015) predate large phones and gesture navigation; no newer grip study was found in this pass [S-L14-050, S-L14-051, S-L14-054].
- **Unconfirmed 2026 claims.** Secondary sources claim visionOS 27 adds curved windows and a redesigned Control Center; Apple's release newsroom did not mention them [S-L14-048, S-L14-049].
- **Android XR is in developer preview,** so its elevation levels and sizes may change [S-L14-087].
- **Voice list timing.** The "first list items within about 20 s" figure appeared only in a search snippet [S-L14-063].

## Confidence

- **Confirmed from Tier A sources read in this session:** Apple HIG values for watchOS, tvOS, visionOS, CarPlay, focus, remotes, Crown, pointer, Pencil, Always On, generative AI, games (text and button tables); Wear OS screen ranges, targets, type tokens (AndroidX source); Android TV canvas, overscan, grid and type tokens (AndroidX source); Android foldable postures and adaptive quality tiers; car app quality requirements (2026-09-14); Design for Driving values (public copy 2024-07-23); NHTSA criteria (Federal Register PDF); Android XR visual design and spatial UI values; Meta panels and hands UI values; Microsoft 10-foot values (archived page); Xbox Accessibility Guidelines 101 and 112; Section 508 and ADA reach values; WCAG 2.2 criteria; Carbon for AI; Apple newsroom release notes for the 26 and 27 releases; CarPlay Ultra.
- **Tier B (corroborated or clearly dated):** Hoober's grip and touch studies; NN/g mobile session length; Microsoft's HAX guidelines (CHI 2019 paper); Alexa one-breath blog.
- **Computed:** TV text as share of screen width, visual angles in Invariant I-3 (rely on assumed ppi, TV size and distances), minimum-to-default text ratios.
- **Inferred:** all "Builder implication" lines, all token-encoding structures, context and density mappings, and matrix cells tagged [inferred] (car and kiosk distances, voice/AI rows, console density and dark norms).
