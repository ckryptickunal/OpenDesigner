---
type: source
title: Building a drawer component
created: 2026-09-27
updated: 2026-09-27
video_id: ek-building-a-drawer-component
url: https://emilkowal.ski/ui/building-a-drawer-component
channel: Emil Kowalski (web)
published: Unknown
authority: non-negotiable
tags:
  - drawer
  - bottom-sheet
  - vaul
  - radix
  - drag-gesture
  - momentum
  - snap-points
  - easing
  - animation-performance
  - virtual-keyboard
  - visual-viewport
  - multi-touch
---

# Building a drawer component

## Metadata

- Page ID: `ek-building-a-drawer-component`
- Publisher: Emil Kowalski (web)
- Published: Unknown
- URL: https://emilkowal.ski/ui/building-a-drawer-component

## Summary

Emil Kowalski explains how he built Vaul, an open-source drawer (bottom sheet) for the web modelled on Apple's iOS Sheet. He covers the anatomy (built on Radix's Dialog primitive with a Radix-like API), a drag gesture that must not drop frames, momentum and damping, how scrolling and dragging coexist, scaling the page behind the drawer, the iOS-matched curve and 500ms duration, handling the virtual keyboard with the Visual Viewport API, ignoring extra touches, snap points, syncing Safari's theme bar, and testing on real devices. For a design system it is a concrete checklist of the invisible details that make a sheet feel native, with exact motion values, performance traps and interaction thresholds.

## Key Ideas

- On mobile a drawer feels more native than a modal.
- Build on an accessible dialog primitive (Radix Dialog) and mirror its API so the component feels familiar.
- Changing an inherited CSS variable on every drag frame forces style recalculation for all children; set transform directly on the element instead.
- Momentum-based dragging lets a flick close the drawer; damping past the top makes it feel physical because real things slow down before stopping.
- Only allow dragging when scrolled to the top, and block drag for 100ms after reaching the top so a fast scroll cannot close the drawer.
- The drawer uses cubic-bezier(0.32, 0.72, 0, 1) from the Ionic Framework and 500ms to mimic the iOS Sheet; easing and duration make a big difference to how any component feels.
- Background scale and corner radius follow drag progress while dragging.
- Handle the virtual keyboard with the Visual Viewport API so the drawer sits above the keyboard and stays fully scrollable.
- Ignore extra touches after the first to stop the drawer jumping.
- Snap points snap to the closest point on release, can be viewport fractions or fixed pixels, and respect momentum.
- Safari's theme bar cannot transition or use transparency, so compute the opaque overlay colour and step it with the same curve as the drawer.
- Invisible details matter because they match users' expectations from native OS drawers.
- Debug on a real phone (or Xcode Simulator), not a shrunken desktop window.

## Entities

- [[entities/emil-kowalski|Emil Kowalski]] (person): Design engineer and author of the article and of Vaul.
- [[entities/vaul|Vaul]] (library): The open-source drawer component for the web whose build process the article describes.
- [[entities/radix-dialog|Radix Dialog]] (library): Dialog primitive Vaul is built on; handles accessibility and focus management, and its API is mirrored by Vaul.
- [[entities/vercel|Vercel]] (company): Company where the author's team ('we') already used a drawer that lacked drag-to-dismiss and had input issues.
- [[entities/ios-sheet|iOS Sheet]] (product): Apple's sheet component whose natural feel Vaul tries to recreate on the web.
- [[entities/ionic-framework|Ionic Framework]] (library): Source of the easing curve Vaul uses, which closely matches iOS.
- [[entities/visual-viewport-api|Visual Viewport API]] (tool): Browser API used to resize and reposition the drawer when the virtual keyboard shows.
- [[entities/bezier-easing|bezier-easing]] (library): Library used to interpolate theme-bar colours along the drawer's custom bezier curve.
- [[entities/safari|Safari]] (product): Browser whose theme bar colour the author tried to sync with the drawer overlay, and whose devtools he used for debugging.
- [[entities/xcode-simulator|Xcode Simulator]] (tool): macOS simulator offered as an alternative to testing on a physical phone.
- [[entities/apple-maps|Apple Maps]] (product): Example of the snap-points pattern on iOS.
- [[entities/family|Family]] (product): Product whose drawer the author recreated with Vaul to show how far it can be customised.
- [[entities/snap-points|Snap points]] (concept): Checkpoints a drawer snaps to on release, set as viewport fractions or fixed pixels.
- [[entities/momentum-based-dragging|Momentum-based dragging]] (concept): Using release velocity so a flick can close the drawer or skip snap points.
- [[entities/animations-on-the-web-animations-dev|Animations on the Web (animations.dev)]] (product): The author's animation course, plugged in the Motion section and at the end of the article, where this component is built.

## Topics

- [[topics/drawers-and-sheets|Drawers and sheets]]: Full build notes for a web drawer that feels like the iOS Sheet: anatomy, drag, scroll, background scale, snap points, keyboard and multi-touch handling.
- [[topics/gestures-and-drag|Gestures and drag]]: Momentum-based dismissal, damping past the top, a shouldDrag rule tied to scroll position, a 100ms post-scroll block, ignoring extra touches, and momentum-aware snap points.
- [[topics/animation-performance|Animation performance]]: Updating an inherited CSS variable per drag frame recalculated styles for every child and lagged beyond about 20 list items; setting transform directly on the element fixed it.
- [[topics/easing-and-timing|Easing and timing]]: The drawer uses transform 0.5s cubic-bezier(0.32, 0.72, 0, 1), an iOS-like curve from the Ionic Framework; the right easing and duration make a big difference to how any component feels.
- [[topics/forms-and-inputs|Forms and inputs]]: Focusing an input inside a drawer makes the browser scroll and hide content; the Visual Viewport API keeps the drawer above the keyboard and fully scrollable, at the cost of a slight delay.
- [[topics/mobile-app-patterns|Mobile app patterns]]: Drawers are preferred over modals on mobile for a native feel; snap points as in Apple Maps; users bring expectations from native OS drawers.
- [[topics/modals-and-popovers|Modals and popovers]]: The author prefers a drawer to a modal on mobile, and builds the drawer on Radix's Dialog primitive.
- [[topics/accessibility|Accessibility]]: Building on Radix's Dialog primitive gives the drawer accessibility and focus management.
- [[topics/ui-libraries|UI libraries]]: Vaul is open source, built on Radix Dialog with a Radix-like compound API, and can be styled and composed freely.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: Code for inline transform during drag, a visualViewport resize listener in a React effect, opaque overlay colour maths and theme-color meta tag updates.
- [[topics/design-process|Design process]]: Debug drawers on a real phone via cable and Safari devtools or in Xcode Simulator; open-sourcing brings more feedback.
- [[topics/design-taste-and-judgement|Design taste and judgement]]: Invisible details feel invisible because they match users' inherent expectations; missing them makes a component feel off.

## Notable Claims

- At Vercel the existing drawer lacked drag-to-dismiss and had issues with inputs, which led to building Vaul from scratch. Evidence: Why a drawer?
- Open-sourcing means more people use a component, which brings more feedback and ultimately a better component. Evidence: Open-sourcing meant that more people will use it
- Radix's Dialog primitive ensures the component is accessible and handles focus management. Evidence: Anatomy
- Once drawer content grew beyond about 20 list items, the drag gesture became laggy even without re-renders. Evidence: Drag gesture: ~20 list items
- Because CSS variables are inheritable, changing one causes style recalculation for all children, so cost grows with the number of items. Evidence: Since CSS Variables are inheritable
- Updating the transform style directly on the element fixed the lag; finding this took hours. Evidence: Updating the style directly on the element fixed the issue
- Momentum-based dragging means you can flick the drawer closed instead of dragging to a certain point. Evidence: I added momentum based dragging next
- Damping an upward drag at the top makes the interaction feel natural because real things slow down before they stop. Evidence: the drawer will damp the drag
- Fast mobile scrolling can carry past the top into a drag with enough velocity to accidentally close the drawer. Evidence: Scrolling: We tend to scroll pretty fast
- The Vaul curve closely matches iOS and comes from the Ionic Framework; 500ms is meant to mimic iOS's Sheet. Evidence: Motion
- When an input is focused the virtual keyboard shows and the browser scrolls upward, pushing the drawer up and potentially hiding content. Evidence: Inputs
- When the keyboard shows the visualViewport height decreases, and vice versa. Evidence: When the keyboard shows, the visualViewport height will decrease
- Sitting the drawer right above the keyboard keeps it fully scrollable, which the browser default does not. Evidence: will make it fully scrollable
- The Visual Viewport approach has a slight delay because the new height arrives only after the keyboard is fully visible. Evidence: The only downside to this approach
- Without handling, adding a second finger during a drag makes the drawer jump to the new position. Evidence: Multi touch
- Invisible details are invisible because they align with users' inherent expectations from native OS drawers. Evidence: They are ’invisible’
- Snap points are a common iOS pattern, used in Apple Maps. Evidence: Snap points
- Fixed-pixel snap points ensure something like an input sticks out evenly on all devices. Evidence: Fixed values are particularly useful
- Safari's theme bar does not support CSS transitions or semi-transparent colours. Evidence: Safari Theme Bar
- Linear colour interpolation will not match a drawer animated with a custom bezier curve. Evidence: interpolating the colors will give us a linear transition
- The theme-bar sync is not in Vaul because it does not match the overlay transition when frames drop. Evidence: This isn’t available in Vaul yet
- Shrinking the desktop devtools window is not enough to debug a drawer; it needs a real mobile environment. Evidence: Debugging
- Xcode Simulator offers a replica that matches an actual phone almost exactly. Evidence: An alternative would be Xcode Simulator

## Quotes

> Not losing frames while dragging is a good start, but I already failed there.
> things in real life don’t suddenly stop, they slow down first.
> Using the right easing and duration makes a big difference

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: Self-promotion: the page opens with a plug for the author's aiforui.dev course, plugs Animations on the Web in the Motion section, and ends with a plug for animations.dev, where this component is built.
- Caveat: The article says the library is not finished and notes will be added as it matures; the publish date is unknown, so details may be dated.
- Caveat: The theme-bar sync is explicitly an unshipped idea: it is not in Vaul because it does not match the overlay when frames drop.
- Caveat: The visualViewport code is simplified by the author, declares unused variables (keyboardHeight, drawerHeight) and leaves OFFSET undefined; the approach has a slight delay.
- Caveat: The interpolateColor snippet references `linear` and `easing` without defining them, and the function name getNonTrasparentOverlayColor is misspelled in the source.
- Caveat: Preferring a drawer to a modal on mobile is the author's stated preference, not a measured finding.
- Caveat: The media list has one image (Xcode Simulator with the Vaul site); it was described from alt text and not downloaded. Videos and the interactive Family demo were not available in the raw text.
- Caveat: The prose says the keyboard handling relies on a "change" event, but the code listens for the visualViewport "resize" event.
- Caveat: Code in the raw text has extraction spacing (for example 'cubic-bezier ( 0.32 , 0.72 , 0 , 1 )'); code values here are written without those spaces and match the raw text once whitespace is ignored.
- Caveat: Not from this article: learn/sources.json records that the Vaul README says the library is unmaintained (checked 2026-09-24), so treat Vaul as a craft reference rather than a dependency to recommend [inferred].

### Rules and practices

- **should** (patterns, web): On mobile, present content in a drawer (bottom sheet) rather than a modal. Why: A drawer gives a more native feel on mobile. [Why a drawer?]
- **should** (components, all): Give drawers drag-to-dismiss. Why: The previous Vercel drawer lacked drag-to-dismiss, one of the reasons Vaul was built. [lacked drag-to-dismiss functionality]
- **should** (accessibility, react): Build the drawer on an accessible dialog primitive such as Radix's Dialog. Why: Radix ensures the component is accessible and handles focus management. [Anatomy]
- **should** (components, react): Mirror the underlying primitive's API with compound parts: Drawer.Root wrapping Drawer.Trigger and Drawer.Portal, with Drawer.Content and Drawer.Overlay rendered inside Drawer.Portal. Why: An API very similar to Radix's feels familiar. Values: Drawer.Root, Drawer.Trigger, Drawer.Portal, Drawer.Content, Drawer.Overlay. [Anatomy]
- **must** (motion, all): Keep the drag gesture at full frame rate; do not drop frames while dragging. Why: The author calls not losing frames while dragging 'a good start' and describes his own dropped frames as a failure. [Not losing frames while dragging is a good start, but I already failed there.]
- **should** (motion, react): Update the drag position without triggering component re-renders. Why: The author's drag already avoided re-renders, which he treats as the expected cause of dropped frames ('so what could cause it to drop frames?'). [Dragging was done without any re-renders, so what could cause it to drop frames?]
- **must** (motion, css): Do not drive the drag position through an inherited CSS custom property (such as --swipe-amount) set on the drawer. Why: CSS variables are inheritable, so each change triggers style recalculation for all children; the drag became laggy once content passed about 20 list items. Values: --swipe-amount, ~20 list items. [Since CSS Variables are inheritable]
- **must** (motion, css): Set the drag offset directly on the moving element as an inline transform: translateY(<draggedDistance>px). Why: Updating the style directly on the element fixed the dropped frames. Values: translateY(), transform: `translateY(${draggedDistance}px)`. [Updating the style directly on the element fixed the issue]
- **should** (motion, all): Use momentum-based dragging so a flick can close the drawer without dragging it past a set point. Why: You don't need to drag until a certain point to close the drawer; you can just flick it. [I added momentum based dragging next]
- **should** (motion, all): When the user drags upward while the drawer is already at its top, damp the drag: the further they drag, the less the drawer moves. Why: It feels more natural, as things in real life don't suddenly stop, they slow down first. [the drawer will damp the drag]
- **should** (components, all): Allow dragging the drawer only when its scrollable content is scrolled to the top (a shouldDrag check). Why: Being scrollable and draggable at once is tricky, and this is very similar to how native drawers work on iOS. [I’ve written a shouldDrag function that doesn’t allow you to drag unless you are scrolled to the top of the drawer.]
- **should** (components, all): After scrolling reaches the top of the drawer, block dragging for 100ms. Why: Fast mobile scrolling can overshoot the top into a drag with enough velocity to accidentally close the drawer. Values: 100ms. [I added a timeout of 100ms]
- **consider** (motion, web): Offer an opt-in option (scaleBackground) that makes the page behind the drawer look like another sheet by applying transform and border radius to a wrapper element ([vaul-drawer-wrapper]). Why: It creates the illusion of the body becoming another sheet. Values: scaleBackground, [vaul-drawer-wrapper]. [Background animation]
- **should** (motion, all): While dragging, derive the background's transform and border radius from drag progress rather than fixed values. Why: The same background logic applies during drag, with values based on progress; dragging the drawer down 40% sets the radius to 60% of its max. Values: 40%, 60%. [Dragging the drawer down by 40% will change the border radius to 60%]
- **should** (motion, all): Use the iOS-matching curve cubic-bezier(0.32, 0.72, 0, 1) (from the Ionic Framework) for drawer and sheet motion. Why: The curve closely matches the one used in iOS, and the author says using the right easing and duration makes a big difference to how a component feels. Values: cubic-bezier(0.32, 0.72, 0, 1), transition: transform 0.5s cubic-bezier(0.32, 0.72, 0, 1). [The curve used in Vaul closely matches the one used in iOS]
- **should** (motion, all): Use a 500ms duration for the drawer's transform transition. Why: 500ms is meant to mimic iOS's Sheet. Values: 500ms, 0.5s. [Duration of 500ms is also supposed to mimic iOS’s Sheet]
- **should** (motion, all): Choose easing and duration deliberately for every component, not only drawers. Why: Using the right easing and duration makes a big difference to how this, and any other component, feels. [Motion]
- **should** (components, web): When an input inside a drawer gets focus, disable the browser's default scroll-into-view behaviour and position the drawer with the Visual Viewport API instead. Why: When the virtual keyboard shows, the browser scrolls upward, pushing the drawer up and potentially hiding important content. Values: visualViewport. [Inputs]
- **should** (components, web): Listen for visualViewport resize; set the drawer's height to the visual viewport height minus an offset, and its bottom to the larger of (window.innerHeight minus visual viewport height) and 0, in px. Why: The visual viewport height shrinks when the keyboard shows and grows when it hides, so it tells you how to update the drawer's height and position. Values: window.innerHeight - visualViewportHeight, `${visualViewportHeight - OFFSET}px`, `${Math.max(diffFromInitial, 0)}px`. [We then use this information to update the drawer’s height and position accordingly]
- **consider** (components, react): Register the visualViewport resize listener in an effect and remove it in the effect's cleanup. Why: The source's React example adds the listener with window.visualViewport?.addEventListener and removes it in the returned cleanup. Values: resize. [window.visualViewport?. removeEventListener]
- **should** (components, web): Keep the Visual Viewport approach even though the drawer's height updates with a slight delay after the keyboard appears. Why: The new visual viewport height arrives only after the keyboard is fully visible; the author calls it not ideal but found this approach works best. [It’s not ideal, but I found that this approach works best.]
- **should** (components, web): Place the drawer directly above the virtual keyboard while it is open. Why: It keeps the drawer fully scrollable, which would not be the case with the browser's default behaviour. [changing the position of the drawer to sit right above the keyboard]
- **must** (components, all): Ignore every touch after the first one until the user releases (for example, return early from the press handler while isDragging is true). Why: Otherwise adding a second finger makes the drawer jump to the new position; the author says that if this were not addressed the drawer would feel off. Values: isDragging. [Multi touch]
- **must** (patterns, all): Match the behaviours users expect from native OS drawers, including the small 'invisible' details. Why: People use native drawers often, which creates expectations; when a feature works as assumed, users proceed without a second thought, and missing details make the drawer feel off. [It’s minor, but makes a difference]
- **should** (components, all): When a drawer has snap points, on each release snap it to the point closest to its current position. Why: Multiple checkpoints are a common iOS pattern, as in Apple Maps; the check runs every time you drag and release, provided snap points are specified. [Snap points]
- **consider** (components, all): Let snap points be set either as a fraction of the viewport or as a fixed pixel value. Why: The source's snap points accept both forms. [either be a fraction of the viewport or a fixed value in pixels]
- **should** (components, all): Use a fixed-pixel snap point when something such as an input must stick out by the same amount on every device. Why: Fixed values ensure the content sticks out evenly on all devices. [Fixed values are particularly useful]
- **should** (motion, all): Make snap points momentum-based: a hard enough flick skips points or closes the drawer completely, and the same applies when dragging upward. Why: The source says snap points are also momentum based, like its flick-to-close dragging. [This is also momentum based]
- **consider** (color, web): Match Safari's theme bar colour to the app's current background colour, including the dimmed colour while the drawer overlay is shown. Why: The author wanted Safari's theme colour to match the current background colour of the app. Values: meta[name="theme-color"]. [I wanted to match Safari’s theme color with the current background color of our app.]
- **consider** (color, web): To match Safari's theme bar to a semi-transparent overlay, compute the overlay's opaque equivalent on the background per channel: round(a * channel + (1 - a) * background). Why: Safari's theme bar cannot use CSS transitions or semi-transparent colours. Values: Math.round(a * r + (1 - a) * Number(background[0])), rgba(0, 0, 0, 0.5), [255, 255, 255]. [Safari Theme Bar]
- **consider** (motion, web): To transition the theme bar, precompute 50 interpolated colours (step factor 1 / (steps - 1), so the first and last steps are the two end colours) and update the theme-color meta tag every 10ms after the drawer opens, so the steps fill the 500ms drawer transition. Why: The theme bar cannot use CSS transitions; 50 colours at 10ms each (10x50) matches the 500ms duration. Values: 50 steps, 10ms, 500ms, 10x50, 1 / (steps - 1). [I created 50 steps]
- **should** (motion, web): When stepping colours for the open/close transition, interpolate along the drawer's own bezier curve (for example with the bezier-easing library), not linearly. Why: Linear interpolation won't match a drawer animated with a custom bezier curve. [interpolation is done using the same curve as the drawer with the help of bezier-easing]
- **consider** (color, web): When interpolating theme colours, round each channel and clamp it to the 0-255 range. Why: The source's interpolateColor rounds every component and clamps it below 0 and above 255. Values: Math.round(newColorComponent), 255. [if (result[i] > 255 ) result[i] = 255 ;]
- **consider** (motion, web): During a drag, pick the theme colour from a linearly interpolated array by drag progress: index = floor(dragProgress * array length). Why: The drag interaction needs a linear mapping from drag progress (0 to 1) to colour. Values: Math.floor(dragProgress * interpolatedColorsLinear.length). [We also needed a linear interpolation for the drag interaction]
- **should** (motion, web): Do not ship a JavaScript-timed theme-colour transition if it falls out of step with the CSS overlay transition when frames drop. Why: That mismatch is why the author has not added the theme-bar sync to Vaul. [This isn’t available in Vaul yet]
- **must** (process, web): Test drawers in a real mobile environment, not by shrinking the desktop devtools window. Why: A component like this needs the same environment as an actual mobile device. [just simply open the dev tools and make the window smaller]
- **should** (process, web): Debug on a physical phone connected by cable, using Safari's devtools on the computer, and open the local dev server via the computer's IP address and port with both devices on the same network. Why: It lets you use desktop devtools while testing on a physical phone. [Most of the time, I used my phone]
- **consider** (tooling, web): Use Xcode Simulator on macOS as an alternative test device. Why: It offers a replica that matches an actual phone almost exactly. [An alternative would be Xcode Simulator]
- **should** (components, all): Keep the drawer fully styleable and composable so drawers do not all have to look the same. Why: Not every drawer has to look the same; Family's drawer was recreated with Vaul to show what's possible. [Getting creative]
- **consider** (process, all): Consider open-sourcing reusable components. Why: More people use them, which brings more feedback and ultimately a better component. [Open-sourcing meant that more people will use it]

### Decisions it informs

- On mobile, should secondary content open in a drawer or a modal? (`Q-pattern-01`)
  - Drawer (bottom sheet): Slides up from the bottom and can be dragged or flicked away; feels native, like the iOS Sheet. When: Mobile layouts where a native feel matters.
  - Modal: A less native feel on mobile than a drawer, per the author's preference; the source gives no further detail about modals. When: Not recommended on mobile by the source.
  - Recommendation: Use a drawer on mobile for a more native feel.
- Should the drawer's API be built from compound parts or configured through props? (`Q-comp-03`)
  - Compound parts mirroring Radix Dialog: Drawer.Root, Trigger, Portal, Content and Overlay; feels familiar to people who know Radix. When: The source's choice for Vaul.
  - A single component configured with props: Not discussed in the source [inferred]. When: Not the source's choice [inferred].
  - Recommendation: Compound parts with an API very similar to Radix's, so it feels familiar.
- How should the drag position be written to the page on each frame?
  - Inherited CSS variable (--swipe-amount) used by translateY(): Every change recalculates styles for all children; became laggy beyond about 20 list items. When: Not recommended.
  - Inline transform on the moving element: No inherited recalculation; fixed the dropped frames. When: For per-frame drag updates, as in the source's drawer.
  - Recommendation: Set transform: translateY(...) directly on the element.
- How does a user dismiss the drawer by dragging?
  - Drag past a set point: The user must drag until a certain point to close it. When: The source does not recommend this alone.
  - Momentum-based: A flick closes the drawer even if it has not travelled far; with snap points a hard flick can skip points. When: Default for drawers.
  - Recommendation: Momentum-based dragging, so a flick is enough.
- How should a scrollable drawer decide between scrolling its content and being dragged?
  - Drag only at the top, with a 100ms block after reaching it: Works like native iOS drawers; a fast scroll that overshoots the top cannot turn into a drag that closes the drawer. When: Any drawer with scrollable content.
  - Drag only at the top, no block: Fast mobile scrolling can carry past the top into a drag with enough velocity to accidentally close the drawer. When: Not recommended by the source.
  - Recommendation: Use a shouldDrag check that allows dragging only when scrolled to the top, plus a 100ms timeout after reaching the top.
- How should the drawer respond when an input inside it opens the on-screen keyboard?
  - Browser default: The browser scrolls upward, pushing the drawer up and potentially hiding content; the drawer is not fully scrollable. When: Not recommended.
  - Visual Viewport API: The drawer resizes and sits right above the keyboard and stays fully scrollable, with a slight delay because the new height arrives after the keyboard is fully visible. When: Any drawer that contains inputs.
  - Recommendation: Disable the browser behaviour and use the Visual Viewport API; the author found it works best despite the delay.
- Should the page behind the drawer shrink into a sheet of its own?
  - Scale the background (scaleBackground): The body looks like another sheet: transform and border radius are applied to the wrapper, following drag progress while dragging. When: When you want the layered, iOS-like sheet illusion.
  - Leave the background as is: No transform or radius is applied to the page behind the drawer [inferred]. When: The prop is opt-in, so this is the default [inferred].
- Should snap points be set as a fraction of the viewport or as fixed pixels?
  - Fraction of the viewport: The checkpoint scales with the screen height. When: General-purpose checkpoints [inferred].
  - Fixed pixels: Content such as an input sticks out by the same amount on every device. When: When a specific piece of content must peek out evenly on all devices.
  - Recommendation: Fixed pixels when an input must stick out evenly on all devices; otherwise either works [inferred].
- Should the browser's theme bar colour follow the drawer overlay?
  - Leave the theme bar static: The theme bar does not change when the drawer opens; this is what Vaul shipped when the article was written. When: Default, until the sync can stay in step with the overlay.
  - Sync via stepped theme-color updates: 50 precomputed opaque colours, eased with the drawer's curve and updated every 10ms, linearly by progress during drag; can drift from the overlay when frames drop. When: Experimental; only if it matches the overlay transition.
  - Recommendation: The author shares the idea but has not shipped it because it does not match the overlay when frames drop.
- Where should a drawer be tested?
  - Shrunk desktop devtools window: Not the same environment as a real mobile device. When: Not enough for a component like this.
  - Physical phone via cable with Safari devtools: Real device behaviour with desktop devtools; load the dev server by IP and port on the same network. When: The author's main method.
  - Xcode Simulator: A replica that matches an actual phone almost exactly. When: An alternative on macOS.
  - Recommendation: Mostly a physical phone connected to the computer, with Xcode Simulator as an alternative.

### Process

1. Start from an accessible primitive: Build the drawer on Radix's Dialog primitive for accessibility and focus management, and mirror its compound API (Root, Trigger, Portal, Content, Overlay).
2. Make the drag fast: Drag without re-renders and write the offset as an inline transform: translateY() on the element, not through an inherited CSS variable.
3. Add physics: Add momentum-based dismissal so a flick closes the drawer, and damp upward drag past the top.
4. Reconcile scroll and drag: Allow drag only when scrolled to the top (shouldDrag) and block drag for 100ms after reaching the top.
5. Scale the background: Optionally apply transform and border radius to the wrapper element, driven by drag progress while dragging.
6. Tune the motion: Transition transform over 0.5s with cubic-bezier(0.32, 0.72, 0, 1) to mimic the iOS Sheet.
7. Handle the keyboard: Disable the browser's scroll-to-input behaviour; on visualViewport resize, set the drawer's height and bottom so it sits above the keyboard.
8. Guard against multi-touch: Ignore touches after the first until release so the drawer never jumps.
9. Add snap points: On release snap to the closest point (viewport fraction or fixed px), letting strong flicks skip points or close.
10. Optionally sync the theme bar: Compute the opaque overlay colour, precompute 50 eased steps, update the theme-color meta tag every 10ms on open, and pick linearly by drag progress while dragging; ship only if it stays in step with the overlay.
11. Test on real devices: Connect a phone by cable, use Safari devtools on the computer, open the dev server by IP and port on the same network, or use Xcode Simulator.

### Examples and visual references

- Apple's Sheet component on iOS (iOS): The native sheet whose natural feel Vaul recreates on the web, including its curve and 500ms duration.
- Vercel's earlier drawer (Vercel): An in-house drawer that lacked drag-to-dismiss and had input issues, prompting a rebuild.
- Snap points in Apple Maps (Apple Maps): A sheet that rests at several checkpoints; shown in a video in the article (not viewed here).
- Recreation of Family's drawer built with Vaul (Family): An interactive demo in the article (not viewed here) showing that Vaul can be styled and composed to look unlike a default drawer.
- Opaque overlay colour calculation (Safari theme bar): getNonTrasparentOverlayColor("rgba(0, 0, 0, 0.5)", [255, 255, 255]) gives the solid colour of a dark semi-transparent overlay on white, matching the drawer overlay.
- Background radius tied to drag (Vaul): Dragging the drawer down by 40% sets the background's border radius to 60% of its max value.
- Xcode Simulator running the Vaul site (Xcode Simulator): Per the image's alt text (image not downloaded): Xcode's simulator app with the Vaul site open, illustrating device-accurate debugging.

### Numbers

- ~20 list items: Content size at which the CSS-variable drag approach became laggy [Drag gesture]
- 100ms: Time after reaching the top of the scroll during which dragging is blocked [Scrolling]
- 40%: Drag-down distance in the example: dragging the drawer down by 40% changes the background border radius to 60% of its max [Background animation]
- 60%: Share of the max background border radius after dragging the drawer down by 40% [Background animation]
- cubic-bezier(0.32, 0.72, 0, 1): Drawer easing curve, from the Ionic Framework, closely matching iOS (raw code block reads 'cubic-bezier ( 0.32 , 0.72 , 0 , 1 )') [Motion]
- 500ms: Drawer transition duration, meant to mimic iOS's Sheet (0.5s in the CSS) [Motion]
- rgba(0, 0, 0, 0.5): Example dark semi-transparent overlay colour for the opaque colour calculation, on a white [255, 255, 255] background [Safari Theme Bar]
- 50 steps: Number of interpolated theme-bar colours [Safari Theme Bar]
- 10ms: Interval between theme-color meta tag updates; 10x50 matches the 500ms transition [Safari Theme Bar]
- 255: Upper clamp for colour channels during interpolation (lower clamp 0) [interpolateColor]
- between 0 and 1: Range of dragProgress used to pick a colour index [onDrag]

<!-- /od:learn -->
