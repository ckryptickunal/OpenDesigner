---
type: source
title: "emilkowalski/skills: skills/animate-expo/RECIPES.md"
created: 2026-09-27
updated: 2026-09-27
video_id: eks-skills-animate-expo-recipes
url: https://github.com/emilkowalski/skills/blob/85e8e23/skills/animate-expo/RECIPES.md
channel: emilkowalski/skills (GitHub, MIT)
published: commit 85e8e23
authority: non-negotiable
tags:
  - react-native
  - expo
  - reanimated
  - recipes
  - bottom-sheet
  - swipe-to-delete
  - momentum
  - rubber-band
  - toast
  - keyboard
  - screen-transitions
  - haptics
---

# emilkowalski/skills: skills/animate-expo/RECIPES.md

## Metadata

- Video ID: `eks-skills-animate-expo-recipes`
- Channel: emilkowalski/skills (GitHub, MIT)
- Published: commit 85e8e23
- URL: https://github.com/emilkowalski/skills/blob/85e8e23/skills/animate-expo/RECIPES.md

## Summary

The animate-expo RECIPES file gives ready-to-build React Native and Expo implementations for the motion that comes up most: press feedback, a drag-to-dismiss bottom sheet, swipe to delete, a collapsing header, list entrances, keyboard-synced UI, a tab indicator, native screen transitions, toasts and firing something once at a threshold. Each recipe states the exact values (durations, springs, curves, offsets, interpolation ranges) and the few details that separate a fluid version from a broken one, such as capturing the current value on grab, deciding by projected velocity, handing velocity to the spring and clamping interpolation. It also shares two worklets, Apple-style momentum projection and rubber-banding. For a design system it supplies concrete mobile motion tokens and component behaviors that can be locked as defaults, plus platform differences for native sheets on iOS and Android.

## Key Ideas

- Check for a native component first (formSheet, ReanimatedSwipeable, native stack) and hand-build only when the interaction is different in kind.
- Momentum projection decides where a flick was going, so a fast short swipe commits and a slow long one doesn't.
- Rubber-banding makes a boundary resist instead of stopping dead.
- Grabbing an element mid-animation must continue from where it is on screen, not jump back to zero.
- Handing the release velocity to the spring removes the seam between finger and animation.
- Derive related visuals (a backdrop, a header title) from the same shared value so they stay in sync for free.
- Collapse headers by translating content in a fixed-height, clipped container, never by animating height.
- Never put entrance animations on rows of a virtualized list; recycled rows re-fire and flicker.
- Drive keyboard-following UI from the keyboard's real position, not from an event plus a guessed duration.
- Toasts stay under 300ms, exit the way they entered, exit about 20% faster, and respect safe-area insets.
- Fire one-off effects at a threshold with useAnimatedReaction, so the JS call happens only when the state flips.
- Build gestures and layout-animation builders once (useMemo or module scope), not on every render.

## Entities

- [[entities/emil-kowalski|Emil Kowalski]] (person): Author of the skills repository these recipes come from.
- [[entities/expo|Expo]] (tool): Toolchain; packages are installed with npx expo install, and babel-preset-expo configures the worklets plugin.
- [[entities/expo-router|Expo Router]] (library): Root _layout, Stack screen options, presentation modal and formSheet with detents.
- [[entities/reanimated|Reanimated]] (library): Shared values, useAnimatedStyle, withSpring, withTiming, interpolate, layout animations (FadeInDown, FadeOutDown, LinearTransition).
- [[entities/react-native-worklets|react-native-worklets]] (library): scheduleOnRN, the replacement for runOnJS.
- [[entities/react-native-gesture-handler|React Native Gesture Handler]] (library): Gesture.Pan() builder (v2) or usePanGesture hook (v3), GestureDetector, GestureHandlerRootView.
- [[entities/reanimatedswipeable|ReanimatedSwipeable]] (library): Gesture-handler component for swipe-to-reveal action rows with thresholds and overshoot on the UI thread.
- [[entities/expo-haptics|expo-haptics]] (library): Light impact when a sheet snaps home or a threshold arms; selection on tab press.
- [[entities/react-native-keyboard-controller|react-native-keyboard-controller]] (library): KeyboardProvider and useReanimatedKeyboardAnimation for UI that follows the keyboard frame by frame.
- [[entities/flatlist-flashlist|FlatList / FlashList]] (library): Virtualized lists whose recycled rows must not carry entering animations.
- [[entities/react-compiler|React Compiler]] (tool): Reason shared values use .get() / .set() instead of .value.
- [[entities/momentum-projection|Momentum projection]] (concept): Apple's exponential-decay estimate of where a flick would come to rest.
- [[entities/rubber-banding|Rubber-banding]] (concept): Resistance that grows the further an element is pulled past an edge.

## Topics

- [[topics/gestures-and-drag|Gestures and drag]]: Pan gestures with declared axes, context captured on start, momentum projection for commit decisions, velocity handed to springs, rubber-banding past edges, gestures memoized.
- [[topics/drawers-and-sheets|Drawers and sheets]]: Use formSheet when the sheet is its own destination; otherwise a drag-to-dismiss sheet with a 40% projected threshold, clamped dismissal spring, snap-back spring with a light haptic, and a backdrop derived from the same value. Android caps detents at three.
- [[topics/spring-animation|Spring animation]]: Dismiss with { duration: 300, dampingRatio: 1, velocity, overshootClamping: true }; snap back with { duration: 300, dampingRatio: 0.8, velocity }; row return with dampingRatio 1.
- [[topics/easing-and-timing|Easing and timing]]: Press 120ms with cubic-bezier(0.23, 1, 0.32, 1); swipe-out 200ms ease-out; tab pill 250ms ease-in-out; list entrance 250ms with 30–80ms stagger; toast 300ms in, 250ms out.
- [[topics/animation-performance|Animation performance]]: Never animate header height; clamp interpolations; build layout-animation builders at module scope or in useMemo; don't call JS per frame; drive keyboard UI on the UI thread.
- [[topics/micro-interactions|Micro-interactions]]: Press scale 0.97 over 120ms with hitSlop and pressRetentionOffset; haptics on snap home, threshold arming and tab press.
- [[topics/toasts-and-notifications|Toasts and notifications]]: Toasts enter with FadeInDown 300ms and exit with FadeOutDown 250ms, both ease-out, positioned above the safe-area inset, and exit the way they entered.
- [[topics/navigation-and-sidebars|Navigation and sidebars]]: Native stack transitions per navigation type, animation: 'none' between tabs, animationMatchesGesture for custom animations, and a measured tab indicator pill.
- [[topics/mobile-app-patterns|Mobile app patterns]]: Recipes for swipe to delete, collapsing header, keyboard-synced footer, pull-to-refresh arming and form-sheet differences between iOS and Android.
- [[topics/reduced-motion|Reduced motion]]: Screen transitions switch to animation: 'fade' when reduced motion is on.

## Notable Claims

- npx expo install resolves the versions that match the SDK, unlike npm install. Evidence: Setup the recipes assume
- The worklets Babel plugin is configured by babel-preset-expo automatically. Evidence: Setup the recipes assume
- Reading and writing shared values with .get() / .set() is the form the Reanimated docs recommend for React Compiler support; the compiler can't see through .value. Evidence: Three conventions
- Rebuilding a gesture on every render can reattach the recognizer and drop a drag that's mid-flight. Evidence: Gestures are wrapped in useMemo.
- Expo installs Gesture Handler v2; in v3 each gesture is a hook, onStart becomes onActivate, onEnd becomes onDeactivate, and success is replaced by an inverted event.canceled. Evidence: Gesture Handler v3
- The projection function uses Apple's exponential-decay form, not v²/2a from physics class. Evidence: Two worklets you'll need everywhere
- 120ms and a 3% scale is the ceiling for something touched as often as a pressable. Evidence: Press feedback
- setState is fine for press feedback because it fires twice per press, not per frame. Evidence: Press feedback
- Without capturing the current value in onStart, grabbing a sheet mid-animation teleports it. Evidence: The four details that separate this from a bad drag
- Requiring 40% travel makes a sheet feel heavy; with projection a quick flick dismisses even a few pixels down. Evidence: Velocity decides, not distance.
- Handing velocity to the spring is the single detail that most separates fluid from fine. Evidence: Velocity is handed to the spring
- Without overshootClamping on dismissal, the sheet springs past the bottom of the screen and flashes a gap. Evidence: overshootClamping on dismissal
- A backdrop derived from the sheet's shared value is always in sync and costs nothing. Evidence: The backdrop derives from the same value
- ReanimatedSwipeable already does swipe-to-reveal actions, including thresholds, overshoot and open/close methods, on the UI thread. Evidence: Swipe to delete a row
- A pan handler inside a scroll view with no axis declared steals vertical scrolls, and the list feels broken in a way that looks like a scrolling bug. Evidence: activeOffsetX is the mobile-specific part.
- Layout-animation builders rebuilt in render cost every re-render. Evidence: ROW_CLOSE ... module scope
- Animating a header's height runs a layout pass on the header and everything below it on every scroll frame, competing with the scroll itself. Evidence: Collapsing header on scroll
- Without Extrapolation.CLAMP, scrolling past 60 drives opacity negative and the header reappears inverted at the bottom of a long list. Evidence: Extrapolation.CLAMP is not optional
- Stagger longer than 30–80ms feels slow; shorter reads as simultaneous. Evidence: List entrances
- Entering animations on rows of a virtualized list re-fire every time a recycled row scrolls back into view, so the list appears to flicker. Evidence: Never put entering on a row inside FlatList
- The keyboard rides a private system curve and its event arrives on the JS thread after it has started moving, so any chosen duration visibly lags or leads it. Evidence: Keyboard-synced UI
- scaleX on a rounded pill smears the corners into ovals. Evidence: Tab / segmented indicator
- Native screen transitions run on the platform side, keep the interactive back gesture and match every other app on the device. Evidence: Screen transitions (Expo Router)
- animationMatchesGesture: true makes the iOS back swipe run the custom transition in reverse under the finger. Evidence: animationMatchesGesture
- Android caps form-sheet detents at three and silently truncates longer arrays. Evidence: Android caps detents at three.
- sheetGrabberVisible is iOS-only; Android shows no grabber. Evidence: formSheet is native on both platforms
- Android form sheets can't host native headers or nested stacks. Evidence: formSheet is native on both platforms
- fitToContents needs explicitly sized content; a flex: 1 root has no intrinsic height to fit. Evidence: formSheet is native on both platforms
- A toast at bottom: 16 sits under the home indicator on every modern iPhone. Evidence: Toast: Safe area insets, always.
- There is no formula for tuning toast opacity against a stacking reflow; it has to be tuned by eye. Evidence: If toasts stack and the list reflows
- With useAnimatedReaction, the comparison runs on the UI thread every frame while the JS call happens twice per pull. Evidence: Firing something once at a threshold

## Quotes

> Velocity decides, not distance.
> Requiring 40% travel makes the sheet feel heavy.
> It exits the way it entered.

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: Pinned to commit 85e8e23; APIs are version-specific (Reanimated 4, react-native-worklets, Gesture Handler v2 builder vs v3 hooks) and may change.
- Caveat: The form-sheet platform differences come from the Expo modal docs at the time of writing; the source points there for the full list.
- Caveat: HEIGHT, WIDTH, SWIPE_THRESHOLD and REFRESH_THRESHOLD are placeholders the recipes leave undefined; only the 40% sheet threshold is a stated value.
- Caveat: Tuning toast opacity against a stacking reflow is explicitly by eye; the source says there is no formula.
- Caveat: Code snippets are illustrative starting points ('start from the recipe, then adapt'), not complete components.
- Caveat: No media list exists for this source; nothing visual was reviewed.

### Rules and practices

- **must** (tooling, react): Install react-native-reanimated, react-native-worklets, react-native-gesture-handler and expo-haptics with npx expo install, not npm install; add react-native-keyboard-controller only when keyboard-synced UI is needed. Why: expo install resolves the versions that match the SDK. Values: npx expo install react-native-reanimated react-native-worklets react-native-gesture-handler expo-haptics. [Setup the recipes assume]
- **must** (tooling, react): Wrap the app once in GestureHandlerRootView with style { flex: 1 }; in Expo Router, do it in the root _layout. Why: Setup every gesture recipe assumes. Values: { flex: 1 }. [GestureHandlerRootView wraps the app once]
- **should** (tokens, react): Define the shared easing constants once: EASE_OUT = Easing.bezier(0.23, 1, 0.32, 1) for UI, EASE_IN_OUT = Easing.bezier(0.77, 0, 0.175, 1) for on-screen movement, EASE_SHEET = Easing.bezier(0.32, 0.72, 0, 1) for the iOS sheet curve. Why: The recipes share these constants, commented as the strong ease-out for UI, on-screen movement and the iOS sheet curve. Values: Easing.bezier(0.23, 1, 0.32, 1), Easing.bezier(0.77, 0, 0.175, 1), Easing.bezier(0.32, 0.72, 0, 1). [Imports and constants every recipe below shares]
- **should** (motion, react): Read and write shared values with .get() / .set() rather than .value. Why: It is the form the Reanimated docs recommend for React Compiler support; .value still works, but the compiler can't see through it. Values: .get(), .set(). [Three conventions]
- **must** (tooling, react): Call back to the React Native runtime from a worklet with scheduleOnRN(fn, ...args), not the deprecated runOnJS(fn)(...args). Why: scheduleOnRN replaces runOnJS. Values: scheduleOnRN(fn, ...args). [Three conventions]
- **must** (motion, react): Wrap Gesture Handler v2 gestures in useMemo. Why: Rebuilding a gesture on every render can reattach the recognizer and drop a drag that's mid-flight. Values: useMemo. [Rebuilding a gesture on every render can reattach the recognizer]
- **should** (tooling, react): On Gesture Handler v3, use the hook form (e.g. usePanGesture with one config object), map onStart to onActivate and onEnd to onDeactivate, read the inverted event.canceled instead of success, and drop the useMemo. Why: In v3 the builder is legacy and the hook manages its own identity. Values: usePanGesture, onActivate, onDeactivate, event.canceled. [Gesture Handler v3]
- **must** (motion, all): Decide where a flick was going with momentum projection: project(velocity, decelerationRate = 0.998) = ((velocity / 1000) * decelerationRate) / (1 - decelerationRate). Why: A fast short swipe should commit and a slow long one shouldn't; this is Apple's exponential-decay form, not v²/2a. Values: decelerationRate = 0.998, ((velocity / 1000) * decelerationRate) / (1 - decelerationRate). [Two worklets you'll need everywhere]
- **must** (motion, all): Make boundaries resist with rubberband(overshoot, dimension, constant = 0.55) = (overshoot * dimension * constant) / (dimension + constant * Math.abs(overshoot)). Why: The further past the edge, the less the element follows, instead of stopping dead. Values: constant = 0.55, (overshoot * dimension * constant) / (dimension + constant * Math.abs(overshoot)). [Two worklets you'll need everywhere]
- **must** (components, react): Give every pressable a press scale of 0.97 over 120ms with transitionTimingFunction cubic-bezier(0.23, 1, 0.32, 1) on transform, and treat 120ms and a 3% scale as the ceiling for something touched this often. Why: It passes the frequency gate only because it's near-imperceptible; anything longer or larger belongs to rarer moments. Values: scale: 0.97, 120ms, 3%, cubic-bezier(0.23, 1, 0.32, 1), transitionProperty: 'transform'. [a CSS transition is the whole implementation]
- **should** (components, react): Implement press feedback as a CSS transition on an Animated.View toggled by onPressIn / onPressOut, with no gesture and no shared value. Why: A CSS transition is the whole implementation; setState is fine because it fires twice per press, not per frame. Values: onPressIn, onPressOut. [Press feedback]
- **should** (accessibility, react): Use hitSlop (the recipe sets hitSlop={12}) to bring a small icon up to the 44pt target without growing it, and pressRetentionOffset (the recipe sets pressRetentionOffset={16}) so slight finger drift doesn't cancel the press. Why: hitSlop brings a small icon up to the 44pt target without growing it; pressRetentionOffset stops a slight finger drift from cancelling. Values: hitSlop={12}, pressRetentionOffset={16}, 44pt. [pressRetentionOffset={16}]
- **must** (components, react): If a bottom sheet is its own destination, use presentation: 'formSheet'; build a custom drag-to-dismiss sheet only when it has to live inside an existing screen. Why: formSheet gives the platform's real sheet for free. Values: presentation: 'formSheet'. [Bottom sheet you can drag to dismiss]
- **should** (motion, react): Give a vertical sheet pan activeOffsetY([-10, 10]). Why: Lets a horizontal swipe win and requires intent before committing. Values: activeOffsetY([-10, 10]). [Bottom sheet you can drag to dismiss]
- **must** (motion, react): In a drag gesture's onStart, capture the current on-screen value (context.set(translateY.get())) and add the translation to it. Why: Without it, grabbing a sheet mid-animation teleports it; the animation must continue from where the eye last saw it. Values: context.set(translateY.get()). [start from the current on-screen value, not from 0]
- **should** (motion, all): Let a sheet move freely downward and apply rubberband resistance when dragged upward past the top. Why: Downward is free; upward past the top resists. [downward is free; upward past the top resists]
- **must** (motion, all): Decide sheet dismissal from the projected position (current position + project(velocityY)) against 40% of the sheet height, so a quick flick dismisses even a few pixels down. Why: Velocity decides, not distance; requiring 40% travel makes the sheet feel heavy. Values: HEIGHT * 0.4. [Velocity decides, not distance.]
- **should** (motion, react): Dismiss a sheet with withSpring(HEIGHT, { duration: 300, dampingRatio: 1, velocity: e.velocityY, overshootClamping: true }) and call onClose via scheduleOnRN only when the spring finishes. Why: Recipe values; overshootClamping stops the sheet springing past the bottom and flashing a gap. Values: duration: 300, dampingRatio: 1, velocity: e.velocityY, overshootClamping: true. [duration: 300, dampingRatio: 1, velocity: e.velocityY, overshootClamping: true]
- **should** (motion, react): Snap a sheet back with withSpring(0, { duration: 300, dampingRatio: 0.8, velocity: e.velocityY }) and fire Haptics.impactAsync(Light) because it snapped home. Why: Recipe values; the code comment marks the Light haptic as 'it snapped home'. Values: { duration: 300, dampingRatio: 0.8, velocity: e.velocityY }, Haptics.ImpactFeedbackStyle.Light. [it snapped home]
- **must** (motion, all): Hand the gesture's release velocity to the spring. Why: There's no seam between the finger releasing and the animation continuing; this is the single detail that most separates fluid from fine. Values: velocity: e.velocityY. [Velocity is handed to the spring]
- **must** (motion, react): Use overshootClamping on sheet dismissal. Why: Otherwise the sheet springs past the bottom of the screen and flashes a gap. Values: overshootClamping: true. [otherwise the sheet springs past the bottom of the screen and flashes a gap]
- **should** (motion, react): Derive the sheet backdrop's opacity from the sheet's own shared value: interpolate(translateY, [0, HEIGHT], [1, 0], Extrapolation.CLAMP). Why: It's always in sync and costs nothing. Values: interpolate(translateY.get(), [0, HEIGHT], [1, 0], Extrapolation.CLAMP). [The backdrop derives from the same value]
- **should** (components, react): Use ReanimatedSwipeable for rows that reveal action buttons; build the gesture yourself only for an interaction different in kind, such as swipe-to-commit with momentum projection. Why: ReanimatedSwipeable already does thresholds, overshoot and open/close methods on the UI thread. Values: ReanimatedSwipeable. [Swipe to delete a row]
- **must** (motion, react): Declare the axis on any pan inside a scroll view, e.g. activeOffsetX([-10, 10]) for a horizontal row swipe. Why: With no axis declared it steals vertical scrolls, and the list feels broken in a way that looks like a scrolling bug. Values: activeOffsetX([-10, 10]). [A pan handler inside a scroll view with no axis declared will steal vertical scrolls]
- **should** (motion, react): Commit a swipe-to-delete when the projected position passes -SWIPE_THRESHOLD: slide out with withTiming(-WIDTH, { duration: 200, easing: EASE_OUT }) and call onDelete when it finishes; otherwise spring back with { duration: 300, dampingRatio: 1, velocity: e.velocityX }. Why: Recipe values: a committed swipe slides off with a 200ms ease-out timing and onDelete runs only when it finishes; an uncommitted one springs home with the release velocity. Values: { duration: 200, easing: EASE_OUT }, { duration: 300, dampingRatio: 1, velocity: e.velocityX }. [if (projected < -SWIPE_THRESHOLD)]
- **must** (motion, react): Let the list close the gap a deleted row leaves, with itemLayoutAnimation={LinearTransition.duration(200)} defined at module scope. Why: Closing the gap is the list's job, not the row's; builders rebuilt in render cost every re-render. Values: LinearTransition.duration(200). [Closing the gap the deleted row left is the list's job]
- **should** (motion, react): Drive a collapsing header from useAnimatedScrollHandler into a shared value, fading title opacity 1 to 0 and moving translateY 0 to -12 over scroll 0 to 60, with scrollEventThrottle={16}. Why: Recipe values. Values: [0, 60], [1, 0], [0, -12], scrollEventThrottle={16}. [Collapsing header on scroll]
- **must** (motion, react): Never animate a header's height to collapse it; give the container a fixed height, translate the content inside and clip with overflow: 'hidden'. Why: Animating height runs a layout pass on the header and everything below it every scroll frame, competing with the scroll itself. Values: overflow: 'hidden'. [Never animate the header's height to collapse it.]
- **must** (motion, react): Pass Extrapolation.CLAMP to scroll-driven interpolations such as the collapsing header's; the source calls it not optional. Why: Without it, scrolling past 60 keeps driving opacity negative and the header reappears inverted at the bottom of a long list. Values: Extrapolation.CLAMP. [Extrapolation.CLAMP is not optional]
- **must** (motion, react): Build layout-animation builders outside components or in useMemo; for a per-index delay, memoize it inside the row. Why: An inline chain in JSX rebuilds the builder on every render. Values: useMemo(() => FadeInDown.duration(250).delay(index * 40), [index]). [List entrances]
- **must** (motion, all): Stagger list entrances by 30–80ms per item (the recipe uses FadeInDown.duration(250).delay(index * 40)). Why: Longer feels slow; shorter reads as simultaneous. Values: 30–80ms, FadeInDown.duration(250), index * 40. [Stagger 30–80ms.]
- **must** (motion, react): Never put entering on a row inside FlatList, FlashList or any virtualized list; animate the list container once on mount, or use itemLayoutAnimation for reflow only. Why: Rows are recycled, so the animation re-fires every time one scrolls back into view and the list appears to flicker. Values: entering, itemLayoutAnimation. [Never put entering on a row inside FlatList]
- **must** (motion, all): Use entrance animations only for content the user asked for and is waiting on; a list they scroll past all day should already be there. Why: A list they scroll past all day should already be there. [Entrance animations are for content the user asked for]
- **must** (tooling, react): For keyboard-synced UI, install react-native-keyboard-controller and put KeyboardProvider in the root _layout next to GestureHandlerRootView. Why: The hooks do nothing without the provider. Values: KeyboardProvider. [Keyboard-synced UI]
- **must** (motion, react): Move keyboard-following UI with useReanimatedKeyboardAnimation's height (0 to -keyboardHeight) applied as translateY on the UI thread. Why: The UI must be driven by the keyboard's actual position, frame by frame. Values: useReanimatedKeyboardAnimation, 0 → -keyboardHeight. [Keyboard-synced UI]
- **must** (motion, react): Never build keyboard-following motion from Keyboard.addListener plus a timing animation. Why: The keyboard rides a private system curve and the event arrives on the JS thread after it has started moving, so any duration visibly lags or leads it. Values: Keyboard.addListener. [Never build this from Keyboard.addListener]
- **should** (components, react): For a tab or segmented indicator, measure each tab once with onLayout (not per frame), then animate the pill's translateX and width with withTiming over 250ms using EASE_IN_OUT. Why: Measure once, then animate transforms; ease-in-out because the pill is moving across the screen rather than entering or leaving it. Values: duration: 250, EASE_IN_OUT, onLayout. [Tab / segmented indicator]
- **must** (motion, react): Animate the indicator pill's width rather than scaleX, since the pill is absolutely positioned with no children. Why: Nothing else re-lays-out and the corner radius survives; scaleX would smear the corners into ovals. Values: width, scaleX. [This is the sanctioned width animation]
- **must** (patterns, react): Fire Haptics.selectionAsync() when the tab is pressed, not when the pill lands. Why: Stated as a directive with no separate reason in this file; it matches firing a haptic at the causal moment [inferred]. Values: Haptics.selectionAsync(). [on the press, not when the pill lands]
- **must** (motion, react): Configure screen transitions on the native stack; never rebuild a screen transition in JS. Why: The native one runs on the platform side, keeps the interactive back gesture and matches every other app on the device. [Screen transitions (Expo Router)]
- **should** (motion, react): Use animation: 'default' (the unmodified platform push) when going deeper into a hierarchy. Why: Navigation table: deeper into a hierarchy gets the platform push, unmodified. Values: animation: 'default'. [Deeper into a hierarchy]
- **should** (patterns, react): Use presentation: 'modal' for a self-contained task the user can abandon. Why: Navigation table. Values: presentation: 'modal'. [A self-contained task the user can abandon]
- **should** (patterns, react): Use presentation: 'formSheet' with detents for a short interruption such as a picker, filter or share. Why: Navigation table. Values: presentation: 'formSheet', sheetAllowedDetents. [A short interruption: picker, filter, share]
- **must** (motion, react): Use animation: 'none' between tabs. Why: Navigation table. Values: animation: 'none'. [Between tabs]
- **must** (accessibility, react): Switch the stack's screenOptions to animation: 'fade' when reduced motion is on. Why: Navigation table: reduced motion. Values: animation: reduced ? 'fade' : 'default'. [Reduced motion | animation: 'fade']
- **must** (motion, ios): Set animationMatchesGesture: true whenever you set a custom animation on a screen. Why: It makes the iOS back swipe run the transition in reverse under the finger; otherwise dragging back looks like a different app than pushing forward. Values: animationMatchesGesture: true. [animationMatchesGesture: true makes the iOS back swipe]
- **must** (platforms, android): Design form-sheet detents for at most three. Why: Android caps detents at three; a longer sheetAllowedDetents array works on iOS and silently truncates on Android. Values: three. [Android caps detents at three.]
- **must** (platforms, android): Don't rely on sheetGrabberVisible as the only 'this is draggable' affordance. Why: It is iOS-only; Android shows no grabber. Values: sheetGrabberVisible. [sheetGrabberVisible is iOS-only.]
- **must** (platforms, android): Keep a form sheet's content a single screen; if it needs its own navigation, use presentation: 'modal' instead. Why: Android form sheets can't host native headers or nested stacks. Values: presentation: 'modal'. [Android form sheets can't host native headers or nested stacks.]
- **must** (layout, react): Give explicitly sized content to a sheet using sheetAllowedDetents: 'fitToContents'. Why: A flex: 1 root has no intrinsic height to fit, so the detent is wrong. Values: 'fitToContents', flex: 1. [fitToContents needs explicitly sized content.]
- **should** (components, react): Animate toasts in with FadeInDown.duration(300).easing(EASE_OUT) and out with FadeOutDown.duration(250).easing(EASE_OUT), with both builders at module scope. Why: Recipe values; layout-animation builders live outside the component. Values: FadeInDown.duration(300).easing(EASE_OUT), FadeOutDown.duration(250).easing(EASE_OUT). [Toast]
- **must** (motion, all): Keep toast animations within the 300ms cap. Why: A toast is uninvited, so if anything it should be quicker and quieter than motion the user asked for. Values: 300ms. [The 300ms cap holds here too.]
- **must** (motion, all): Make a toast exit the way it entered. Why: Entering from the bottom and leaving to the side reads as two unrelated elements. [It exits the way it entered.]
- **must** (motion, all): Make toast exits about 20% faster than entries. Why: The user has finished reading; the arrival deserves the time, the departure doesn't. Values: ~20%. [Exit ~20% faster than entry.]
- **must** (layout, react): Always offset toasts by the safe-area inset (e.g. bottom: insets.bottom + 16, left: 16, right: 16). Why: A toast at bottom: 16 sits under the home indicator on every modern iPhone. Values: bottom: insets.bottom + 16, left: 16, right: 16. [Safe area insets, always.]
- **consider** (process, react): When stacked toasts reflow, add itemLayoutAnimation and tune the opacity against the reflow by eye, then look at it again the next day. Why: There's no formula for that pair. Values: itemLayoutAnimation. [If toasts stack and the list reflows]
- **must** (motion, react): To fire something once when a crossing point is reached (a detent, a snap, pull-to-refresh arming), use useAnimatedReaction comparing on the UI thread and call JS only when the state flips; don't poll from JS and don't scheduleOnRN every frame. Why: The comparison runs on the UI thread every frame; the JS call happens twice per pull. Values: useAnimatedReaction. [Firing something once at a threshold]
- **should** (patterns, react): Fire a Light impact haptic when a pull crosses its refresh threshold in either direction. Why: Recipe: the reaction schedules Haptics.impactAsync(Light) when isArmed changes. Values: Haptics.ImpactFeedbackStyle.Light. [Firing something once at a threshold]
- **should** (process, react): Start from the matching recipe, then adapt it to the case. Why: The recipes are ready-to-build implementations for the cases that come up most in a React Native app. [Start from the recipe, then adapt.]
- **consider** (motion, react): Let a swipe-to-delete row follow the finger only toward the delete side, clamping its position with Math.min(0, context.get() + e.translationX). Why: Shown in the recipe's onUpdate; the source states no separate reason. Values: Math.min(0, context.get() + e.translationX). [Swipe to delete a row]

### Decisions it informs

- Should a bottom sheet be the platform's native sheet or a custom drag-to-dismiss sheet?
  - presentation: 'formSheet': The platform's real sheet for free, with detents; Android caps detents at three and shows no grabber. When: The sheet is its own destination.
  - Custom drag-to-dismiss sheet: A shared-value sheet with projection, rubber-banding, velocity-handed springs and a derived backdrop. When: The sheet has to live inside an existing screen.
  - Recommendation: formSheet whenever the sheet is its own destination; custom only when it must live inside a screen.
- How should a new screen be presented? (`Q-pattern-01`)
  - animation: 'default': The unmodified platform push. When: Going deeper into a hierarchy.
  - presentation: 'modal': A full modal the user can dismiss. When: A self-contained task the user can abandon, or a sheet that needs its own navigation.
  - presentation: 'formSheet' with detents: A partial-height native sheet. When: A short interruption: picker, filter, share.
  - animation: 'none': Instant switch. When: Between tabs.
  - animation: 'fade': Crossfade. When: Reduced motion is on.
  - Recommendation: Pick by navigation type from the table; always use the native stack.
- When should a drag or swipe commit (dismiss, delete)?
  - Distance only: The user must drag far; requiring 40% travel makes a sheet feel heavy. When: Not recommended.
  - Projected position (distance plus momentum): A quick flick commits even a few pixels in; a slow long drag may not. When: Default for sheets and swipe-to-delete.
  - Recommendation: Use project() on release velocity and compare the projected position to the threshold (40% of height for the sheet).
- Should a swipeable row use the built-in component or a custom gesture?
  - ReanimatedSwipeable: Swipe-to-reveal action buttons with thresholds, overshoot and open/close methods on the UI thread. When: The row reveals action buttons.
  - Custom pan gesture: Swipe-to-commit with momentum projection and a slide-out. When: The interaction is different in kind, such as swipe to delete.
  - Recommendation: ReanimatedSwipeable for revealing actions; custom only for swipe-to-commit.
- How should list items appear? (`Q-motion-06`)
  - Staggered entrance per row: FadeInDown 250ms with a 30–80ms stagger. When: Non-virtualized lists of content the user asked for and is waiting on.
  - Animate the container once on mount: One entrance for the whole list. When: Virtualized lists (FlatList, FlashList).
  - itemLayoutAnimation for reflow only: Rows glide to close gaps. When: Virtualized lists that reorder or delete rows.
  - No entrance: The list is already there. When: Lists the user scrolls past all day.
  - Recommendation: Stagger 30–80ms only for awaited content in non-virtualized lists; never entering on virtualized rows.
- Should toasts leave faster than they arrive, and in which direction? (`Q-motion-02`)
  - Same path, exit about 20% faster: FadeInDown 300ms in, FadeOutDown 250ms out; reads as one element. When: The source's recipe.
  - Different exit direction: Entering from the bottom and leaving to the side reads as two unrelated elements. When: Not recommended.
  - Recommendation: Exit the way it entered, about 20% faster, within the 300ms cap.
- How should UI follow the on-screen keyboard?
  - react-native-keyboard-controller: Follows the keyboard's real position frame by frame on the UI thread. When: Always.
  - Keyboard.addListener + timing animation: Visibly lags or leads the keyboard, which rides a private system curve. When: Never.
  - Recommendation: keyboard-controller with KeyboardProvider at the root.
- Which Gesture Handler API should gestures use?
  - v2 Gesture.Pan() builder: What Expo installs; wrap in useMemo. When: Projects on v2.
  - v3 hooks (usePanGesture): One config object, onActivate / onDeactivate, event.canceled; no useMemo. When: Projects already on v3.
  - Recommendation: Follow the installed version; the recipes use the v2 builder.

### Process

1. Set up once: npx expo install the animation, worklets, gesture and haptics packages; wrap the root _layout in GestureHandlerRootView (and KeyboardProvider if needed); define EASE_OUT, EASE_IN_OUT and EASE_SHEET.
2. Check for a native option first: formSheet for sheets that are destinations, ReanimatedSwipeable for action rows, native stack options for screen transitions; build by hand only when the interaction differs in kind.
3. Build the gesture: Memoize it, declare the axis with activeOffsetX/Y([-10, 10]), capture the current value in onStart, add translation in onUpdate, apply rubberband past edges.
4. Decide on release: Add project(velocity) to the current position and compare with the threshold, so velocity decides rather than distance.
5. Settle with velocity: Pass the release velocity into withSpring; clamp overshoot on dismissal; call JS (onClose, onDelete, haptics) via scheduleOnRN in the completion callback or onEnd.
6. Derive dependents: Compute backdrop opacity, header title fades and similar from the same shared value with interpolate and Extrapolation.CLAMP.
7. Fire effects at thresholds: Use useAnimatedReaction to compare on the UI thread and call JS only when the state flips.
8. Hand reflow to the list: Use itemLayoutAnimation (LinearTransition.duration(200) at module scope) to close gaps; never put entering on virtualized rows.

### Examples and visual references

- PressableScale component: Pressable toggling a pressed style: scale 1 to 0.97, 120ms, cubic-bezier(0.23, 1, 0.32, 1), hitSlop 12, pressRetentionOffset 16.
- Drag-to-dismiss bottom sheet: Sheet follows the finger down freely, resists upward, dismisses when projected past 40% of its height, otherwise springs home with a light haptic; backdrop fades 1 to 0 as it moves down.
- Swipe-to-delete row: Row slides left under the finger; a projected pass beyond the threshold slides it off in 200ms ease-out and deletes; the list closes the gap with LinearTransition.duration(200).
- Collapsing header: Title fades out and moves up 12 over the first 60 of scroll inside a fixed-height, clipped container.
- Keyboard-synced footer: Footer translates up by the keyboard's live height, frame by frame.
- Tab / segmented indicator pill: Pill slides and resizes to the measured tab over 250ms ease-in-out, keeping its round corners.
- Expo Router stack configuration (Expo Router): settings slides from right with animationMatchesGesture, compose opens as a modal, filter opens as a formSheet sized to its content with a grabber on iOS.
- Toast: Enters with FadeInDown over 300ms and exits with FadeOutDown over 250ms, both ease-out, positioned 16 above the bottom safe-area inset and 16 from each side.
- Pull-to-refresh arming: A light haptic fires once each time the pull crosses the refresh threshold.

### Numbers

- 0.998: Default deceleration rate in the momentum projection worklet. [Two worklets you'll need everywhere]
- 0.55: Default rubber-band constant. [Two worklets you'll need everywhere]
- 120ms: Press feedback transition duration. [Press feedback]
- 3%: Press scale reduction (scale 0.97); the ceiling for frequently touched elements. [Press feedback]
- 12: hitSlop on the pressable. [Press feedback]
- 16: pressRetentionOffset on the pressable. [Press feedback]
- 44pt: Touch target hitSlop brings a small icon up to. [Press feedback]
- [-10, 10]: activeOffsetY / activeOffsetX for sheet and row pans. [Bottom sheet; Swipe to delete]
- 40%: Travel a distance-only threshold would require, which makes the sheet feel heavy; the recipe compares the projected position with HEIGHT * 0.4 instead. [Velocity decides, not distance.]
- HEIGHT * 0.4: Projected-position threshold for dismissing the sheet. [Bottom sheet you can drag to dismiss]
- duration: 300, dampingRatio: 1, velocity: e.velocityY, overshootClamping: true: Sheet dismissal spring. [Bottom sheet you can drag to dismiss]
- { duration: 300, dampingRatio: 0.8, velocity: e.velocityY }: Sheet snap-back spring. [Bottom sheet you can drag to dismiss]
- 200: Swipe-to-delete slide-out duration (ms, EASE_OUT) and the LinearTransition duration for closing the gap. [Swipe to delete a row]
- { duration: 300, dampingRatio: 1, velocity: e.velocityX }: Row snap-back spring. [Swipe to delete a row]
- 60: Scroll distance over which the header title fades and moves. [Collapsing header on scroll]
- -12: Header title translateY at the end of the collapse. [Collapsing header on scroll]
- scrollEventThrottle={16}: Scroll event throttle on the animated ScrollView. [Collapsing header on scroll]
- 250: List entrance FadeInDown duration and tab pill withTiming duration (ms). [List entrances; Tab / segmented indicator]
- index * 40: Per-row entrance delay in the recipe. [List entrances]
- 30–80ms: Stagger range for list entrances. [List entrances]
- three: Maximum form-sheet detents on Android. [Android caps detents at three.]
- 300: Toast entrance duration (ms) and the cap for toast motion. [Toast]
- 250: Toast exit duration (ms). [Toast]
- ~20%: How much faster a toast exits than it enters. [Toast]
- insets.bottom + 16: Toast bottom offset; left and right are 16. [Toast]

<!-- /od:learn -->
