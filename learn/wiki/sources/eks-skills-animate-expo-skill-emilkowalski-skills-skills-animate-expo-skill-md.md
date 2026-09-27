---
type: source
title: "emilkowalski/skills: skills/animate-expo/SKILL.md"
created: 2026-09-27
updated: 2026-09-27
video_id: eks-skills-animate-expo-skill
url: https://github.com/emilkowalski/skills/blob/85e8e23/skills/animate-expo/SKILL.md
channel: emilkowalski/skills (GitHub, MIT)
published: commit 85e8e23
authority: non-negotiable
tags:
  - react-native
  - expo
  - reanimated
  - mobile-motion
  - springs
  - easing
  - haptics
  - gestures
  - reduced-motion
  - performance
  - touch-targets
  - emil-kowalski
---

# emilkowalski/skills: skills/animate-expo/SKILL.md

## Metadata

- Video ID: `eks-skills-animate-expo-skill`
- Channel: emilkowalski/skills (GitHub, MIT)
- Published: commit 85e8e23
- URL: https://github.com/emilkowalski/skills/blob/85e8e23/skills/animate-expo/SKILL.md

## Summary

Emil Kowalski's animate-expo skill is a build sequence for motion in React Native and Expo apps: decide whether something should animate at all, name its purpose, pick the cheapest tool, pick cheap properties, choose spring or timing from fixed tables, keep the work on the UI thread, redesign hover as press, add haptics carefully, and ship reduced motion with the animation. It starts from three facts about mobile: there is no hover, there are two runtimes (React Native and the UI thread), and the user's finger is on the element. It gives exact spring configs, three bezier curves, duration bands, haptic calls per moment, touch-target sizes and a Never Ship table. For a design system this is a ready set of mobile motion tokens and guardrails, plus a rule that feel is only verified on a release build on the slowest supported device.

## Key Ideas

- Mobile motion rests on three facts: no hover, two runtimes, and a finger on the element.
- The worst failure is animating something that should not animate; the frequency gate can mean writing no code.
- How often a person sees an animation decides whether it animates: 100+ times a day means none.
- Every animation needs a one-word purpose; without one, it is not built.
- Use the cheapest tool that works, and prefer the platform's native navigation, sheets, tabs and menus over JS rebuilds.
- Only transform and opacity are free; layout properties re-run layout for the node and its siblings every frame.
- If a finger was involved, use a spring and hand it the gesture's velocity; otherwise use timing with a strong ease-out.
- Springs are set with duration and damping ratio (Apple's designer parameters), not mass, stiffness and damping.
- Keep motion off the JS thread: no setState per frame, no per-frame calls back to React Native, no shared-value reads in render.
- Hover has to be redesigned as press: feedback on press-in, commit on press-out, a 0.97 scale in 100-150ms.
- Haptics fire in the same frame as the visual, once per user action, and never as the only feedback.
- Reduced motion means fewer and gentler, not zero: keep opacity and color, drop movement, scale, parallax and overshoot.
- Feel is only verified on a release build on the slowest supported device, never in Expo Go or the simulator.
- Navigation motion matches the platform; everything else beats it and stays under 300ms.

## Entities

- [[entities/emil-kowalski|Emil Kowalski]] (person): Author of the skill; its animation philosophy is the stated source of the knowledge.
- [[entities/expo|Expo]] (tool): The React Native framework and toolchain the skill targets; packages are installed with npx expo install.
- [[entities/react-native|React Native]] (library): The runtime whose JS thread animations must stay off.
- [[entities/reanimated|Reanimated]] (library): react-native-reanimated (version 4): worklets on the UI thread, CSS transitions and animations, layout animations, springs and easings; required instead of core Animated.
- [[entities/react-native-worklets|react-native-worklets]] (library): Worklets runtime package; provides scheduleOnRN, the replacement for the deprecated runOnJS.
- [[entities/react-native-gesture-handler|React Native Gesture Handler]] (library): Gesture.Pan() and GestureHandlerRootView; replaces PanResponder.
- [[entities/expo-router|Expo Router]] (library): Native stack options, formSheet presentation, NativeTabs and Link.Menu / Link.Preview for native navigation motion.
- [[entities/expo-haptics|expo-haptics]] (library): Haptics.selectionAsync, impactAsync and notificationAsync mapped to specific moments.
- [[entities/react-native-keyboard-controller|react-native-keyboard-controller]] (library): Tracks the keyboard's real position frame by frame on the UI thread; needs KeyboardProvider at the root.
- [[entities/lottie|Lottie]] (library): lottie-react-native, for vector illustration and celebration only, never UI state.
- [[entities/react-native-skia|React Native Skia]] (library): @shopify/react-native-skia canvas, for huge animated scenes or freeform drawing when the view hierarchy is the bottleneck.
- [[entities/yoga|Yoga]] (tool): React Native's layout engine; animating layout properties re-runs it every frame for the node and its siblings.
- [[entities/react-compiler|React Compiler]] (tool): Cannot see through direct .value access, so .get() / .set() is the compiler-safe form.
- [[entities/uisheetpresentationcontroller|UISheetPresentationController]] (product): The native iOS sheet that presentation: 'formSheet' gives for free.
- [[entities/expo-go|Expo Go]] (tool): Named as not a performance environment; feel must not be judged there.
- [[entities/promotion|ProMotion]] (concept): iPhones that can run animations at 120fps; third-party animations are capped at 60fps unless CADisableMinimumFrameDurationOnPhone is set.
- [[entities/frequency-gate|Frequency gate]] (concept): Deciding whether to animate by how many times a day a person sees the motion.
- [[entities/velocity-handoff|Velocity handoff]] (concept): Passing the gesture's release velocity into the spring so motion continues without a seam.

## Topics

- [[topics/motion-principles|Motion principles]]: A gated build order: frequency tier, one-word purpose, cheapest tool, cheap properties, spring vs timing, thread, press, haptics, reduced motion.
- [[topics/easing-and-timing|Easing and timing]]: ease-out for enter/exit and default, ease-in-out for on-screen movement, linear for constant motion, never ease-in; three custom beziers; duration bands of 100-150ms, 150-200ms and ~300ms, all under 300ms except platform navigation.
- [[topics/spring-animation|Spring animation]]: Springs whenever a finger was involved, configured with duration and dampingRatio from a fixed table, velocity passed in, overshootClamping at hard edges, bounce only after momentum.
- [[topics/animation-performance|Animation performance]]: Only transform and opacity are free; keep motion on the UI runtime; no setState or scheduleOnRN per frame; no animated elevation or BlurView intensity; enable 120fps on ProMotion; verify on a release build on the slowest device.
- [[topics/gestures-and-drag|Gestures and drag]]: Gesture.Pan() instead of PanResponder, interruptibility and velocity handoff as baseline, velocity-or-distance dismissal and rubber-band resistance at boundaries.
- [[topics/micro-interactions|Micro-interactions]]: Press feedback on press-in with scale 0.97 in 100-150ms, and haptics mapped to selection, snap, heavy landing and success or error.
- [[topics/reduced-motion|Reduced motion]]: Ship it with the animation; keep opacity and color changes, drop translation, scale, parallax and overshoot; screen transitions become fade.
- [[topics/mobile-app-patterns|Mobile app patterns]]: No hover on mobile; use native stack transitions, formSheet, NativeTabs, native menus, large-title headers, RefreshControl and keyboard-controller instead of JS rebuilds.
- [[topics/drawers-and-sheets|Drawers and sheets]]: A sheet that is its own screen uses presentation: 'formSheet'; sheet and drawer springs use duration 300 and dampingRatio 0.8 with velocity.
- [[topics/navigation-and-sidebars|Navigation and sidebars]]: Tab switches never slide (animation: 'none'); screen transitions use the platform default and are never overridden or hand-rolled.
- [[topics/buttons-and-actions|Buttons and actions]]: Pressables scale to 0.97 on press-in, commit on press-out, keep a 44x44pt / 48dp target via hitSlop, and use pressRetentionOffset.
- [[topics/accessibility|Accessibility]]: Reduced motion support, minimum touch targets, haptics never the only feedback, and no hardcoded heights, because a height measured at default type size is wrong at 200% text size.

## Notable Claims

- An animation that touches the React Native runtime stutters the moment the app does anything else. Evidence: There are two runtimes.
- Animating on the wrong thread can look fine in dev on your phone and drop to 20fps on a three-year-old Android. Evidence: Operating Posture: Animating the right thing on the wrong thread
- Core Animated cannot be driven by a gesture without crossing the bridge, and useNativeDriver refuses anything but transform and opacity. Evidence: Hard Rules 2: Reanimated, not core Animated
- Reanimated worklets run on the UI thread and keep running while JS is busy. Evidence: Hard Rules 2
- Sliding between tabs implies depth that is not there, and the user pays for it dozens of times a session. Evidence: Tab switches never slide.
- presentation: 'formSheet' is a real UISheetPresentationController. Evidence: 3. Pick the tool: A bottom sheet that is its own screen
- npx expo install resolves the version that matches the project's SDK, which plain npm install won't. Evidence: Dependencies.
- Animating width, height, margin, padding, flex, top, left or gap re-runs Yoga on every frame for that node and its siblings. Evidence: 4. Pick the properties
- An absolutely positioned element with no children is out of flow, so animating its width re-lays-out nothing else and keeps a corner radius that scaleX would smear. Evidence: The one exception
- In a transform array, [{ translateY }, { scale }] scales after moving; reversed, the translate gets scaled too. Evidence: transform is an array and order matters
- Animating Android elevation re-renders the shadow every frame. Evidence: Android shadows are elevation
- Animating BlurView intensity re-renders the blur each frame on Android. Evidence: Never animate BlurView intensity
- Percentages in translate are relative to the element's own size. Evidence: Percentages work in translate
- Springs carry velocity through an interruption; timing curves restart. Evidence: 5. Timing or spring
- Reanimated's spring takes Apple's two designer parameters (duration and dampingRatio) directly. Evidence: 5. Timing or spring
- ease-in starts slow, delaying the exact moment the user is watching. Evidence: Never ease-in on UI.
- Reanimated's built-in easings are as weak as CSS's. Evidence: Never ease-in on UI.
- The iOS push transition is 350ms. Evidence: Duration: The platform's own transitions are longer
- One React render per frame is the single biggest cause of jank in React Native apps. Evidence: 6. Keep it off the JS thread
- Calling scheduleOnRN inside onUpdate queues a React Native runtime call 60-120 times per second. Evidence: Never schedule back to the RN runtime inside onUpdate
- runOnJS is deprecated in Reanimated 4; scheduleOnRN from react-native-worklets replaces it. Evidence: 6. Keep it off the JS thread; Never Ship
- Reading a shared value during render gives a snapshot that never updates and silently desyncs; writing one during render fires mid-reconciliation. Evidence: Never read a shared value during render
- The React Compiler cannot see through direct .value access; get/set is the compiler-safe way per the Reanimated docs. Evidence: Use .get() / .set(), not .value.
- Functions called from a worklet without 'worklet' throw at runtime on device while working fine in the debugger. Evidence: Functions called from a worklet need 'worklet'
- Waiting for the tap to complete before showing anything feels dead; that is the latency the user perceives. Evidence: 7. Press, not hover
- Scale takes the label and icons with it, which is what makes a press read as physical. Evidence: scale: 0.97 in 100–150ms
- Haptics used sparingly make the app feel expensive; used everywhere, users turn them off. Evidence: 8. Haptics
- A haptic that lags its animation reads as a glitch, not feedback. Evidence: Same frame as the visual.
- Haptics are off system-wide for many users and silent on most Android hardware. Evidence: Never the only feedback.
- allowFontScaling is on by default, so a height measured at default type size is wrong at 200%. Evidence: Text scales.
- In an Expo project, babel-preset-expo configures the worklets Babel plugin automatically; a missing or misplaced plugin throws 'Failed to create a worklet' at runtime. Evidence: Setup that silently breaks motion
- Without GestureHandlerRootView wrapping the app, gestures do nothing and raise no error. Evidence: Setup that silently breaks motion
- Reanimated 4 requires the New Architecture. Evidence: Setup that silently breaks motion
- A dev build's JS thread is slow enough to hide exactly the problems you're looking for. Evidence: Expo Go is not a performance environment.
- On ProMotion iPhones, third-party animations are capped at 60fps unless CADisableMinimumFrameDurationOnPhone is set; recent Expo SDKs set it by default. Evidence: 120fps
- At 120fps the frame budget is 8ms, not 16, which is why UI-thread animation matters more on mobile than on web. Evidence: 120fps
- Gestures, velocity handoff and haptic timing cannot be judged from code. Evidence: Output: What to feel-check on device

## Quotes

> Nothing in the real world appears from nothing.
> The whole craft is keeping motion on the UI runtime.
> Can't name it? Don't build it.

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: Pinned to commit 85e8e23; the APIs are version-specific (Reanimated 4, react-native-worklets scheduleOnRN, runOnJS deprecated, headerLargeTitle deprecated, NativeTabs under expo-router/unstable-native-tabs) and may change.
- Caveat: 'Recent Expo SDKs set it by default' (CADisableMinimumFrameDurationOnPhone) depends on the SDK version; the source says to confirm it.
- Caveat: Link.Menu / Link.Preview and headerLargeTitleEnabled are iOS-only.
- Caveat: The 'Initial Response' and 'Output' sections are instructions for an AI agent using the skill, not design rules.
- Caveat: 'Never present motion options as a menu' is aimed at implementation; it can pull against OpenDesigner's interview, which offers visual options for system-level decisions [inferred].
- Caveat: The 20fps on a three-year-old Android figure is illustrative, not a cited measurement [inferred].
- Caveat: No media list exists for this source; nothing visual was reviewed.

### Rules and practices

- **must** (patterns, react): On mobile, move every hover affordance into press, position, or nothing; redesign it rather than porting it from the web. Why: There is no hover on mobile. [There is no hover.; 7. Press, not hover]
- **must** (motion, react): Keep every React Native animation on the UI runtime (worklets), never on the React Native runtime. Why: An animation that touches the RN runtime stutters the moment the app does anything else. [There are two runtimes.]
- **must** (motion, react): Treat interruptibility and velocity handoff as the baseline for anything a finger touches, not as polish. Why: Gestures are the primary input on mobile; the user's finger is on the element. [The user's finger is on the element.]
- **should** (process, react): When building motion, make the call, state the reasoning in one line and write the code; do not present motion options as a menu. Why: The skill's posture is a senior mobile engineer building the animation. [Operating Posture]
- **must** (motion, all): Do not animate something that should not animate; the gate may correctly produce zero lines of code. Why: Animating something that shouldn't animate is the worse of the two failure modes. [Operating Posture: Two failure modes, and the first is worse]
- **must** (motion, react): Never drive an animation with a setState per frame, a PanResponder or an animated height. Why: It looks fine in dev on your phone and drops to 20fps on a three-year-old Android. Values: 20fps. [Animating the right thing on the wrong thread]
- **must** (process, all): Run the build sequence in order; steps 1 (should it animate) and 2 (what is the purpose) gate everything else. Why: The gate exists to stop motion that should not be built. [Hard Rules 1]
- **must** (tooling, react): Use Reanimated, not React Native's core Animated. Why: Core Animated can't be driven by a gesture without crossing the bridge, and useNativeDriver refuses anything but transform and opacity; Reanimated worklets run on the UI thread and keep running while JS is busy. Values: react-native-reanimated. [Reanimated worklets run on the UI thread and keep running while JS is busy]
- **must** (tokens, react): Take curves and spring configs from the skill's tables; never approximate values. Why: Hard rule: no approximated values. [Hard Rules 3]
- **must** (accessibility, all): Ship reduced-motion support with the animation, not as a follow-up. Why: Hard rule 4. [Hard Rules 4]
- **must** (process, react): Judge animation feel only on a release build on the slowest device you support. Why: Nothing else counts as verified. [Hard Rules 5]
- **must** (motion, all): Do not animate interactions seen 100+ times a day (tab switches, keyboard open/close, scrolling, settings toggles); use the platform default or nothing. Why: Frequency gate: at 100+ times a day the decision is platform default or nothing; stop here. Values: 100+ times/day. [1. Should this animate at all?]
- **must** (motion, all): For interactions seen tens of times a day (press feedback, list navigation, row selection), use only near-imperceptible motion under 150ms, or nothing. Why: Frequency gate. Values: Tens of times/day, under 150ms. [1. Should this animate at all?]
- **should** (motion, all): Give occasional elements (sheets, modals, toasts, onboarding steps) standard animation. Why: Frequency gate: occasional tier. [1. Should this animate at all?]
- **must** (motion, all): Spend the delight budget only on rare or first-time moments (success states, empty-state illustrations, celebration). Why: The delight budget lives in the rare tier. [1. Should this animate at all?]
- **must** (motion, react): Never slide between tabs; set animation: 'none'. Why: Tabs are peers, not a hierarchy; sliding implies depth that isn't there, and the user pays for it dozens of times a session. Values: animation: 'none'. [Tab switches never slide.]
- **must** (process, all): If a requested animation fails the frequency gate, say so and don't write it. Why: Gate result. [If the request fails this gate, say so and don't write it.]
- **must** (motion, all): Name the purpose of each animation in one word before building it: feedback, spatial consistency, state indication, preventing a jarring change, explanation, or delight (rare tier only); if you can't name it, don't build it. Why: An animation with no nameable purpose should not exist. Values: feedback, spatial consistency, state indication, preventing a jarring change, explanation, delight. [2. What is the purpose?]
- **must** (tooling, react): Pick the cheapest tool that works by walking down the tool table and stopping at the first that fits. Why: Cheapest that works. [3. Pick the tool — cheapest that works]
- **should** (tooling, react): Use a Reanimated CSS transition (transitionProperty in the style) for a state-driven change with no gesture: press, toggle, color, a value flipping. Why: Cheapest tool for state changes. Values: transitionProperty. [3. Pick the tool]
- **should** (tooling, react): Use a Reanimated CSS animation (animationName keyframes) for loops, multi-stage motion, or motion that plays on mount with no state change. Why: Tool table. Values: animationName. [3. Pick the tool]
- **should** (tooling, react): Use layout animations (entering / exiting / itemLayoutAnimation) for elements mounting or unmounting and for list reflow. Why: Tool table. Values: entering, exiting, itemLayoutAnimation. [3. Pick the tool]
- **should** (tooling, react): Use useSharedValue + Gesture + useAnimatedStyle for anything a finger touches or anything derived from scroll. Why: Tool table. Values: useSharedValue, Gesture, useAnimatedStyle. [3. Pick the tool]
- **must** (motion, react): Use native stack options in Expo Router for screen-to-screen transitions; never hand-roll them. Why: Tool table: never hand-roll this. [3. Pick the tool: Screen to screen]
- **must** (components, react): Use presentation: 'formSheet' for a bottom sheet that is its own screen. Why: It's a real UISheetPresentationController, free and correct. Values: presentation: 'formSheet'. [3. Pick the tool: A bottom sheet that is its own screen]
- **should** (components, react): Use NativeTabs (from expo-router/unstable-native-tabs) for the tab bar. Why: It is the platform's real tab bar, with its behaviors and transitions included. Values: expo-router/unstable-native-tabs. [the platform's real tab bar, its behaviors and transitions included]
- **must** (components, ios): Use Link.Menu / Link.Preview (Expo Router) for context menus and press-and-hold previews; never rebuild them in JS. Why: They are native menus and peek (iOS-only). Values: Link.Menu, Link.Preview. [3. Pick the tool: Context menu, press-and-hold preview]
- **should** (components, ios): For a header that collapses into a large title, use headerLargeTitleEnabled on the native stack, not a scroll worklet. Why: Native behavior (iOS-only); headerLargeTitle is deprecated. Values: headerLargeTitleEnabled. [3. Pick the tool: Header that collapses into a large title]
- **should** (components, react): Use RefreshControl for pull to refresh; hand-roll it only when it is a signature interaction. Why: Tool table. Values: RefreshControl. [3. Pick the tool: Pull to refresh]
- **should** (tooling, react): Use react-native-keyboard-controller for UI that tracks the keyboard. Why: It gives the keyboard's real position, frame by frame, on the UI thread. Values: react-native-keyboard-controller. [3. Pick the tool: UI that tracks the keyboard]
- **must** (tooling, react): Use Lottie only for vector illustration, celebration and empty states; never for UI state. Why: Tool table: illustration only. Values: lottie-react-native. [3. Pick the tool: Vector illustration, celebration, empty state]
- **consider** (tooling, react): Use @shopify/react-native-skia for a huge animated scene or freeform drawing, when the view hierarchy itself is the bottleneck. Why: A canvas avoids the view hierarchy. Values: @shopify/react-native-skia. [3. Pick the tool: A huge animated scene, freeform drawing]
- **should** (tooling, react): Reach for a shared value only when the value is continuous or interruptible: a press scale is a CSS transition, a drag is a shared value. Why: Using a worklet for a two-state toggle is the mobile equivalent of installing a motion library for a fade. [Reach for a shared value only when]
- **must** (tooling, react): Install motion packages with npx expo install <package>, not plain npm install. Why: It resolves the version that matches the project's SDK, which plain npm install won't. Values: npx expo install <package>. [Dependencies.]
- **should** (tooling, react): Use react-native-reanimated + react-native-worklets for animation, react-native-gesture-handler for gestures, expo-router for navigation, sheets, native tabs and menus, expo-haptics for haptics, react-native-keyboard-controller (with KeyboardProvider at the root) for keyboard-following UI, lottie-react-native for illustration, and @shopify/react-native-skia for very large scenes. Why: Dependency table. Values: react-native-reanimated, react-native-worklets, react-native-gesture-handler, expo-router, expo-haptics, react-native-keyboard-controller, lottie-react-native, @shopify/react-native-skia. [Dependencies.]
- **must** (motion, react): Animate only transform and opacity; do not animate width, height, margin, padding, flex, top, left or gap (the one exception is an absolutely positioned element with no children). Why: transform and opacity are free; the others re-run Yoga on every frame for that node and its siblings. Values: transform, opacity, width, height, margin, padding, flex, top, left, gap. [4. Pick the properties]
- **should** (motion, react): When an absolutely positioned element with no children (a tab pill, a progress bar fill) has to change size, animate its width rather than scaleX; it is the only exception to transform and opacity. Why: It's out of flow, so nothing else re-lays-out, and width keeps the corner radius that scaleX would smear. Values: width, scaleX. [The one exception: an absolutely positioned element with no children]
- **must** (motion, all): Never enter from scale(0); start from scale(0.9–0.97) plus opacity: 0. Why: Nothing in the real world appears from nothing. Values: scale(0), scale(0.9–0.97), opacity: 0, scale(0.95). [Never scale(0).; Never Ship table]
- **should** (motion, react): Put translate before scale in a React Native transform array unless you want the translate multiplied. Why: transform is an array and order matters: [{ translateY }, { scale }] scales after moving; reversed, the translate gets scaled too. Values: [{ translateY }, { scale }]. [transform is an array and order matters]
- **must** (elevation, android): On Android, never animate elevation; animate the opacity of a pre-shadowed layer instead. Why: Android shadows are elevation, and animating elevation re-renders the shadow every frame. Values: elevation. [Android shadows are elevation]
- **must** (motion, react): Never animate BlurView intensity; crossfade the opacity of a static BlurView instead. Why: On Android it re-renders the blur each frame. Values: BlurView. [Never animate BlurView intensity.]
- **consider** (motion, react): Use percentage translates to move an element by its own size, e.g. translateY('100%') to move a sheet by its own height. Why: Percentages in translate are relative to the element's own size, whatever its content. Values: translateY('100%'). [Percentages work in translate]
- **must** (motion, all): If a finger was involved, use a spring; use timing for everything else. Why: Springs carry velocity through an interruption; timing curves restart. [5. Timing or spring]
- **must** (tokens, react): Configure Reanimated springs with duration and dampingRatio (Apple's two designer parameters), not mass/stiffness/damping. Why: Reanimated's spring takes Apple's two designer parameters directly. Values: duration, dampingRatio. [5. Timing or spring]
- **must** (tokens, react): Use { duration: 400, dampingRatio: 1 } for a default settle with no overshoot. Why: Spring table. Values: { duration: 400, dampingRatio: 1 }. [5. Timing or spring: Default settle, no overshoot]
- **must** (tokens, react): Use { duration: 400, dampingRatio: 0.8, velocity } to reposition or snap back after a drag. Why: Spring table. Values: { duration: 400, dampingRatio: 0.8, velocity }. [5. Timing or spring: Reposition / snap back after a drag]
- **must** (tokens, react): Use { duration: 300, dampingRatio: 0.8, velocity } for sheets and drawers. Why: Spring table. Values: { duration: 300, dampingRatio: 0.8, velocity }. [5. Timing or spring: Sheet, drawer]
- **must** (motion, react): Add overshootClamping: true to any spring that must not pass a hard edge. Why: Spring table. Values: overshootClamping: true. [5. Timing or spring: Must not pass a hard edge]
- **must** (motion, all): Allow bounce (overshoot) only when the gesture carried momentum. Why: Overshoot on a menu that faded in feels wrong; overshoot on a card you flicked feels right. [Bounce only when the gesture carried momentum.]
- **must** (motion, all): Use ease-out for elements entering or exiting, and as the default easing. Why: Easing table for motion without a finger on it. Values: ease-out. [Easing, for everything without a finger on it]
- **must** (motion, all): Use ease-in-out for elements moving or morphing on screen. Why: Easing table. Values: ease-in-out. [Easing: Moving / morphing on screen]
- **must** (motion, all): Use linear easing for constant motion such as progress and marquees. Why: Easing table. Values: linear. [Easing: Constant motion (progress, marquee)]
- **must** (motion, all): Never use ease-in (Easing.in(...)) on a UI element. Why: It starts slow, delaying the exact moment the user is watching. Values: ease-in, Easing.in(...). [It starts slow, delaying the exact moment the user is watching]
- **must** (tokens, react): Do not use Reanimated's built-in easings; use custom bezier curves instead. Why: Reanimated's built-ins are as weak as CSS's. [Reanimated's built-ins are as weak as CSS's]
- **must** (tokens, react): Use Easing.bezier(0.23, 1, 0.32, 1) as the strong ease-out for UI. Why: Named EASE_OUT: strong ease-out for UI. Values: Easing.bezier(0.23, 1, 0.32, 1). [const EASE_OUT]
- **must** (tokens, react): Use Easing.bezier(0.77, 0, 0.175, 1) for on-screen movement. Why: Named EASE_IN_OUT: on-screen movement. Values: Easing.bezier(0.77, 0, 0.175, 1). [const EASE_IN_OUT]
- **must** (tokens, react): Use Easing.bezier(0.32, 0.72, 0, 1) as the iOS sheet curve. Why: Named EASE_SHEET: iOS sheet curve. Values: Easing.bezier(0.32, 0.72, 0, 1). [const EASE_SHEET]
- **must** (tokens, all): Give press feedback a duration of 100–150ms. Why: Duration table. Values: 100–150ms. [Duration: Press feedback]
- **must** (tokens, all): Give toggles, chips and small state changes a duration of 150–200ms. Why: Duration table. Values: 150–200ms. [Duration: Toggle, chip, small state change]
- **must** (tokens, react): Animate sheets, modals and drawers with a spring of about 300ms perceived duration. Why: Duration table. Values: ~300ms perceived. [Duration: Sheet, modal, drawer]
- **must** (motion, react): Use the platform default duration for screen transitions; don't override it. Why: Match the platform for navigation. [Duration: Screen transition]
- **must** (motion, all): Keep mobile UI animations under 300ms, the same as web; match the platform only for navigation (iOS push is 350ms) and beat it everywhere else. Why: The platform's own transitions are longer; UI motion should be quicker. Values: 300ms, 350ms. [Mobile UI animations stay under 300ms, same as web.]
- **must** (motion, react): Never call setState from a gesture or scroll handler; drive the style from a shared value through useAnimatedStyle. Why: One React render per frame is the single biggest cause of jank in RN apps; with a shared value React never re-renders. Values: useAnimatedStyle. [6. Keep it off the JS thread]
- **must** (motion, react): Never call scheduleOnRN inside onUpdate or a scroll handler; call it in onEnd, or in a useAnimatedReaction that fires when a value crosses a threshold. Why: In onUpdate it queues an RN-runtime call 60–120× per second. Values: 60–120× per second, onEnd, useAnimatedReaction. [Never schedule back to the RN runtime inside onUpdate]
- **must** (tooling, react): Use scheduleOnRN(fn, ...args) from react-native-worklets instead of the deprecated runOnJS(fn)(...args). Why: runOnJS is deprecated in Reanimated 4. Values: scheduleOnRN(fn, ...args), runOnJS(fn)(...args). [6. Keep it off the JS thread; Never Ship]
- **must** (motion, react): Never read a shared value during render (for example translateY.get() in JSX). Why: It's a snapshot that never updates and it silently desyncs. [Never read a shared value during render]
- **must** (motion, react): Never write a shared value during render; touch shared values only in worklets, handlers and effects. Why: It fires mid-reconciliation, and a re-render you didn't cause replays the write. [Never write one during render either]
- **must** (motion, react): Access shared values with .get() / .set(), not .value; use the functional form sv.set((v) => v + 1) for updates based on the current value. Why: Direct .value access is the form the React Compiler can't see through; get/set is the compiler-safe way. Values: .get(), .set(), sv.set((v) => v + 1). [Use .get() / .set(), not .value.]
- **must** (motion, react): Put 'worklet' as the first line of any function called from a worklet. Why: Otherwise they throw at runtime on device while working fine in the debugger. Values: 'worklet'. [Functions called from a worklet need 'worklet']
- **must** (components, react): Show feedback on press-in and commit the action on press-out. Why: Waiting for the tap to complete before showing anything feels dead; this is the latency the user perceives. [Feedback on press-in, commit on press-out.]
- **must** (components, react): Scale every pressable to 0.97 in 100–150ms, using Pressable plus a CSS transition. Why: Scale takes the label and icons with it, which is what makes it read as physical. Values: scale: 0.97, 100–150ms. [on any pressable, `Pressable` + a CSS transition]
- **must** (accessibility, ios): Make touch targets at least 44×44pt on iOS. Why: Minimum touch target. Values: 44×44pt. [44×44pt minimum touch target]
- **must** (accessibility, android): Make touch targets at least 48dp on Android. Why: Minimum touch target. Values: 48dp. [44×44pt minimum touch target (48dp Android)]
- **must** (accessibility, react): When the visual is smaller than the minimum target, add hitSlop instead of growing the visual. Why: Stated with the 44×44pt minimum: meet the target without growing the visual. Values: hitSlop. [If the visual is smaller, add hitSlop]
- **should** (components, react): Set pressRetentionOffset on pressables. Why: A finger drifting a few pixels shouldn't cancel a press the user meant. Values: pressRetentionOffset. [pressRetentionOffset]
- **should** (components, android): Use the Android ripple only in a Material-styled app; in a custom-designed app use the same press scale on both platforms. Why: The same scale on both platforms is more coherent than a ripple on one. [Android ripple only in a Material-styled app.]
- **should** (patterns, react): Fire Haptics.selectionAsync() when a value ticks past a step: picker, slider detent, segmented control. Why: Haptic mapping table. Values: Haptics.selectionAsync(). [8. Haptics]
- **should** (patterns, react): Fire Haptics.impactAsync(ImpactFeedbackStyle.Light) when something snaps home, a sheet detent catches, or a drag commits. Why: Haptic mapping table. Values: Haptics.impactAsync(ImpactFeedbackStyle.Light). [8. Haptics]
- **should** (patterns, react): Fire Haptics.impactAsync(ImpactFeedbackStyle.Medium) when a heavy object lands or a destructive action fires. Why: Haptic mapping table. Values: Haptics.impactAsync(ImpactFeedbackStyle.Medium). [8. Haptics]
- **should** (patterns, react): Fire Haptics.notificationAsync(NotificationFeedbackType.Success / Error) when an operation succeeds or fails. Why: Haptic mapping table. Values: Haptics.notificationAsync(NotificationFeedbackType.Success / Error). [8. Haptics]
- **must** (patterns, react): Fire a haptic in the same frame as its visual, at the causal moment (the detent catching), not when the animation finishes. Why: A haptic that lags its animation reads as a glitch, not as feedback. [Same frame as the visual.]
- **must** (patterns, react): Use at most one haptic per user action: never on scroll, never per frame, never on an entrance animation the user didn't cause. Why: Used sparingly haptics make the app feel expensive; used everywhere, users turn them off. [One per user action.]
- **must** (accessibility, react): Never make a haptic the only feedback; always pair it with a visual that stands alone. Why: Haptics are off system-wide for many users, and silent on most Android hardware. [Never the only feedback.]
- **must** (tooling, react): From a worklet, schedule haptics back to the React Native runtime, e.g. scheduleOnRN(Haptics.selectionAsync). Why: Haptics must run on the RN runtime. Values: scheduleOnRN(Haptics.selectionAsync). [From a worklet, haptics must be scheduled back]
- **should** (accessibility, react): Read reduced motion with useReducedMotion(), or pass reduceMotion: ReduceMotion.System to each animation. Why: Reduced motion ships with the animation; the snippet shows both forms. Values: useReducedMotion, reduceMotion: ReduceMotion.System. [9. Reduced motion and accessibility]
- **must** (accessibility, all): Under reduced motion, keep opacity and color changes that explain a state change and drop translation, scale, parallax and overshoot. Why: Reduced motion means fewer and gentler, not zero. [Reduced motion means fewer and gentler, not zero]
- **must** (accessibility, react): Under reduced motion, switch screen transitions to animation: 'fade'. Why: Reduced-motion screen transition. Values: animation: 'fade'. [Screen transitions become animation: 'fade'.]
- **must** (accessibility, react): Never animate to a hardcoded height; measure with onLayout, or animate a transform instead. Why: allowFontScaling is on by default, so any height measured at default type size is wrong at 200%. Values: allowFontScaling, 200%, onLayout. [Text scales.]
- **must** (tooling, react): Install Reanimated through Expo (npx expo install react-native-reanimated react-native-worklets) and rely on babel-preset-expo for the worklets Babel plugin; in a bare React Native project without that preset, add the plugin manually and last in the list. Why: A missing or misplaced plugin throws 'Failed to create a worklet' at runtime. Values: npx expo install react-native-reanimated react-native-worklets, babel-preset-expo. [Setup that silently breaks motion]
- **must** (tooling, react): When using react-native-keyboard-controller for keyboard-following UI, put KeyboardProvider at the root. Why: The dependency table says it needs KeyboardProvider at the root. Values: KeyboardProvider. [Dependencies: Keyboard-following UI]
- **must** (tooling, react): Wrap the app in GestureHandlerRootView. Why: Without it, gestures do nothing with no error. Values: GestureHandlerRootView. [Setup that silently breaks motion]
- **must** (tooling, react): Run the app on the New Architecture when using Reanimated 4. Why: Reanimated 4 requires the New Architecture. Values: Reanimated 4. [Setup that silently breaks motion]
- **must** (process, react): Never judge animation feel in Expo Go, a dev build or the simulator; use a release build on the slowest supported device. Why: A dev build's JS thread is slow enough to hide exactly the problems you're looking for. [Expo Go is not a performance environment.; Never Ship table]
- **must** (platforms, ios): Confirm CADisableMinimumFrameDurationOnPhone is true in expo.ios.infoPlist, and add it if missing. Why: On ProMotion iPhones, third-party animations are capped at 60fps unless it is set; with it the frame budget is 8ms, not 16. Values: "CADisableMinimumFrameDurationOnPhone": true, 60fps, 8ms, 16. [120fps]
- **should** (process, react): When a request matches a recipe (press feedback, drag-to-dismiss sheet, swipe-to-delete, collapsing header, list entrances, keyboard-synced UI, tab indicator, screen transitions), start from the recipe rather than a blank file. Why: Recipes are ready-to-build implementations. [Recipes]
- **must** (tooling, react): Never use PanResponder; use Gesture.Pan() from gesture-handler. Why: Never Ship table. Values: PanResponder, Gesture.Pan(). [Never Ship]
- **must** (tooling, react): Never use core Animated for anything a finger touches; use Reanimated. Why: Never Ship table. [Never Ship]
- **must** (motion, react): Never put entering on a virtualized list row; animate the container, or use itemLayoutAnimation. Why: Never Ship table. Values: entering, itemLayoutAnimation. [Never Ship]
- **must** (motion, react): Never rebuild a screen transition in JS; use the native stack animation option. Why: Never Ship table. [Never Ship]
- **must** (motion, all): Never use a distance-only dismissal threshold; dismiss on velocity or distance, so a flick is enough. Why: Never Ship table. [Never Ship: Distance-only dismissal threshold]
- **must** (motion, all): Never hard-stop an element at a boundary; apply rubber-band resistance. Why: Never Ship table. [Never Ship: Hard stop at a boundary]
- **should** (process, react): After writing motion code, report in a few lines: the gate result (frequency tier, named purpose, and what was rejected and why), the ingredients (tool, properties, spring or curve plus duration, thread), and what to feel-check on device (flick it, interrupt it mid-flight, reverse it, run it on the slowest Android). Why: Gestures, velocity handoff and haptic timing cannot be judged from code. [Output]
- **should** (process, all): Do not pad the motion deliverable into a report; the code is the deliverable. Why: Output section. [The code is the deliverable. Don't pad it into a report.]
- **should** (process, all): Say it plainly when the honest answer is that something shouldn't animate, or that it needs a real device before its feel can be judged. Why: Tone: opinionated and brief. [Tone]

### Decisions it informs

- Should this element animate at all, given how often people see it?
  - No animation (100+ times/day): Platform default or nothing; tab switches, keyboard open/close, scrolling and settings toggles stay instant. When: Interactions seen 100+ times a day.
  - Near-imperceptible (tens of times/day): Under 150ms or nothing; press feedback, list navigation, row selection. When: Interactions seen tens of times a day.
  - Standard animation (occasional): Normal enter/exit motion for sheets, modals, toasts, onboarding steps. When: Occasional elements.
  - Delight (rare / first-time): Where the delight budget is spent: success states, empty-state illustrations, celebration. When: Rare or first-time moments.
  - Recommendation: Decide by frequency; anything seen 100+ times a day gets no animation, and a request that fails the gate is not built.
- Which tool should build the motion in a React Native app?
  - Reanimated CSS transition: Declarative transitionProperty in the style; no shared value or worklet. When: State-driven change with no gesture: press, toggle, color.
  - Reanimated CSS animation: animationName keyframes. When: Loops, multi-stage, or plays on mount with no state change.
  - Layout animations: entering / exiting / itemLayoutAnimation. When: Mount, unmount, list reflow.
  - Shared value + Gesture + useAnimatedStyle: Continuous, interruptible, UI-thread motion. When: Anything a finger touches or anything derived from scroll.
  - Native platform components: Native stack options, formSheet, NativeTabs, Link.Menu / Link.Preview, headerLargeTitleEnabled, RefreshControl. When: Screen transitions, sheets that are screens, tab bars, context menus, large-title headers, pull to refresh.
  - Lottie or Skia: Illustration playback or a canvas. When: Illustration and celebration (Lottie); huge scenes or freeform drawing (Skia).
  - Recommendation: Walk down the table and stop at the first tool that fits; prefer the cheapest, and never hand-roll what the platform provides.
- Should a piece of motion use a spring or a timing curve?
  - Spring: Carries velocity through an interruption, so grabbing or reversing mid-flight stays fluid. When: A finger was involved.
  - Timing (easing + duration): Restarts on interruption; predictable length. When: Everything without a finger on it.
  - Recommendation: Spring if a finger was involved; timing for everything else.
- How should springs be configured? (`Q-motion-04`)
  - Duration + dampingRatio (Apple's designer parameters): Default settle {400, 1}; drag snap-back {400, 0.8, velocity}; sheet or drawer {300, 0.8, velocity}; overshootClamping at hard edges. When: The source's required form.
  - Mass / stiffness / damping: Physics parameters. When: The source says not to use this form.
  - Recommendation: Use duration and dampingRatio from the table, and bounce only when the gesture carried momentum.
- Which easing curve fits each situation?
  - ease-out, Easing.bezier(0.23, 1, 0.32, 1): Starts fast; responsive. When: Entering or exiting; the default.
  - ease-in-out, Easing.bezier(0.77, 0, 0.175, 1): Smooth start and stop. When: Moving or morphing on screen.
  - Sheet curve, Easing.bezier(0.32, 0.72, 0, 1): The iOS sheet curve. When: Sheets.
  - linear: Constant speed. When: Progress, marquee.
  - ease-in: Starts slow, delaying the moment the user watches. When: Never on UI.
  - Recommendation: ease-out by default with the custom bezier; never ease-in; never Reanimated's built-in curves.
- How long should each kind of mobile animation be?
  - 100–150ms: Press feedback. When: Pressables.
  - 150–200ms: Toggle, chip, small state change. When: Small state changes.
  - Spring, ~300ms perceived: Sheet, modal, drawer. When: Larger surfaces.
  - Platform default: Screen transitions (iOS push is 350ms). When: Navigation; don't override.
  - Recommendation: Stay under 300ms for UI; match the platform only for navigation.
- Should screen transitions follow the platform or be custom-built? (`Q-motion-09`)
  - Native stack options in Expo Router: Runs on the platform side, keeps the back gesture, matches other apps. When: Always for screen to screen.
  - Rebuilt in JS: Hand-rolled transition. When: Never, per the Never Ship table.
  - Recommendation: Native stack animation, platform default duration; tabs use animation: 'none'.
- Which haptic fits which moment? (`Q-motion-09`)
  - Haptics.selectionAsync(): Light tick. When: A value ticks past a step: picker, slider detent, segmented control.
  - impactAsync(Light): Light impact. When: Snaps home, a sheet detent catches, a drag commits.
  - impactAsync(Medium): Heavier impact. When: A heavy object lands, a destructive action fires.
  - notificationAsync(Success / Error): Outcome feedback. When: An operation succeeded or failed.
  - Recommendation: Map haptics to these moments, fire in the same frame as the visual, once per user action, never as the only feedback.
- What should reduced motion do? (`Q-motion-07`)
  - Fewer and gentler: Keep opacity and color changes that explain a state change; drop translation, scale, parallax and overshoot; screen transitions fade. When: The source's definition.
  - Zero motion: Removes everything, including state-explaining fades. When: The source says reduced motion is not zero.
  - Recommendation: Fewer and gentler, not zero.
- How should pressables give feedback on Android?
  - Android ripple: Material press feedback on Android only. When: A Material-styled app.
  - Same scale on both platforms: scale 0.97 on press-in on iOS and Android. When: A custom-designed app.
  - Recommendation: Ripple only in a Material-styled app; otherwise the same scale on both platforms is more coherent.
- How should a pill or progress fill change size?
  - Animate width: Keeps the corner radius intact; allowed because the element is absolute and childless. When: Absolutely positioned element with no children.
  - Animate scaleX: Smears the corner radius into ovals. When: Not for rounded pills, per the source.
  - Recommendation: Animate width for an absolutely positioned, childless element; transform and opacity everywhere else.

### Process

1. Gate by frequency: Place the interaction in a tier: 100+ times/day gets no animation, tens of times/day gets under 150ms or nothing, occasional gets standard motion, rare gets the delight budget. If it fails, say so and write nothing.
2. Name the purpose: One word: feedback, spatial consistency, state indication, preventing a jarring change, explanation, or delight (rare tier only). If you can't name it, don't build it.
3. Pick the cheapest tool: Walk the tool table: CSS transition, CSS animation, layout animation, shared value + gesture, or a native platform component; install with npx expo install.
4. Pick the properties: transform and opacity only, except width on an absolute childless element; never scale(0); translate before scale; no animated elevation or BlurView intensity.
5. Choose timing or spring: Spring if a finger was involved (duration + dampingRatio from the table, pass velocity); otherwise the custom ease-out, ease-in-out or linear curve with a duration from the table.
6. Keep it off the JS thread: Shared values and useAnimatedStyle; no setState or scheduleOnRN per frame; no shared-value reads or writes in render; .get()/.set(); 'worklet' in helpers.
7. Design the press: Feedback on press-in, commit on press-out, scale 0.97 in 100–150ms, 44×44pt / 48dp target with hitSlop, pressRetentionOffset.
8. Add haptics: Pick the call from the moment table; fire in the same frame as the visual, once per action, never as the only feedback; schedule back from worklets.
9. Ship reduced motion: useReducedMotion or ReduceMotion.System; keep opacity and color, drop movement; screen transitions fade; no hardcoded heights.
10. Check setup: Expo-installed Reanimated and worklets, GestureHandlerRootView at the root, New Architecture, CADisableMinimumFrameDurationOnPhone for 120fps.
11. Feel-check on device: Release build on the slowest supported device: flick it, interrupt it mid-flight, reverse it, run it on the slowest Android.
12. Report briefly: Gate result, ingredients (tool, properties, curve or spring and duration, thread), and what to feel-check; the code is the deliverable.

### Examples and visual references

- Tab pill and progress bar fill: Absolutely positioned, childless elements where animating width is allowed because nothing else re-lays-out and the corner radius stays round, unlike scaleX.
- Sheet moved by its own height: translateY('100%') moves a sheet by its own height whatever its content.
- Flicked card vs faded-in menu: Overshoot feels right on a card that was flicked and wrong on a menu that faded in.
- Reduced-motion spring snippet: useReducedMotion() sets the starting shared value, or withSpring(0, { duration: 300, dampingRatio: 0.8, reduceMotion: ReduceMotion.System }) lets each animation decide.
- 120fps Info.plist setting (ProMotion iPhones): { expo: { ios: { infoPlist: { CADisableMinimumFrameDurationOnPhone: true } } } } lifts the 60fps cap.

### Numbers

- 100+ times/day: Frequency tier that gets no animation. [1. Should this animate at all?]
- under 150ms: Ceiling for motion seen tens of times a day. [1. Should this animate at all?]
- 20fps: What wrong-thread animation drops to on a three-year-old Android. [Operating Posture]
- scale(0.9–0.97): Starting scale for entrances instead of scale(0). [Never scale(0).]
- scale(0.95): Replacement for a scale(0) entrance in the Never Ship table. [Never Ship]
- { duration: 400, dampingRatio: 1 }: Default settle spring, no overshoot. [5. Timing or spring]
- { duration: 400, dampingRatio: 0.8, velocity }: Reposition or snap back after a drag. [5. Timing or spring]
- { duration: 300, dampingRatio: 0.8, velocity }: Sheet or drawer spring. [5. Timing or spring]
- Easing.bezier(0.23, 1, 0.32, 1): Strong ease-out for UI (EASE_OUT). [Never ease-in on UI.]
- Easing.bezier(0.77, 0, 0.175, 1): On-screen movement (EASE_IN_OUT). [Never ease-in on UI.]
- Easing.bezier(0.32, 0.72, 0, 1): iOS sheet curve (EASE_SHEET). [Never ease-in on UI.]
- 100–150ms: Press feedback duration. [Duration]
- 150–200ms: Toggle, chip, small state change duration. [Duration]
- ~300ms perceived: Sheet, modal, drawer spring. [Duration]
- 300ms: Upper limit for mobile UI animations, same as web. [Mobile UI animations stay under 300ms]
- 350ms: Length of the iOS push transition. [iOS push is 350ms]
- 60–120× per second: How often scheduleOnRN in onUpdate calls the RN runtime. [6. Keep it off the JS thread]
- 0.97: Press scale for any pressable. [7. Press, not hover]
- 44×44pt: Minimum touch target (iOS). [7. Press, not hover]
- 48dp: Minimum touch target (Android). [7. Press, not hover]
- 200%: Text scale at which a height measured at default size is wrong. [Text scales.]
- 60fps: Cap on third-party animations on ProMotion iPhones without CADisableMinimumFrameDurationOnPhone. [120fps]
- 8ms: Frame budget at 120fps, instead of 16. [120fps]

<!-- /od:learn -->
