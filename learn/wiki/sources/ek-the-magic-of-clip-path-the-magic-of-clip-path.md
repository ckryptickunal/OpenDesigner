---
type: source
title: The Magic of Clip Path
created: 2026-09-27
updated: 2026-09-27
video_id: ek-the-magic-of-clip-path
url: https://emilkowal.ski/ui/the-magic-of-clip-path
channel: Emil Kowalski (web)
published: Unknown
authority: non-negotiable
tags:
  - clip-path
  - css
  - inset
  - reveal-animation
  - comparison-slider
  - tabs
  - theme-switch
  - scroll-animation
  - framer-motion
  - waapi
  - animation-performance
  - layout-shift
---

# The Magic of Clip Path

## Metadata

- Video ID: `ek-the-magic-of-clip-path`
- Channel: Emil Kowalski (web)
- Published: Unknown
- URL: https://emilkowal.ski/ui/the-magic-of-clip-path

## Summary

Emil Kowalski shows that the CSS clip-path property, usually used to cut elements into shapes, is also a strong animation tool. Focusing on the inset() shape, he builds comparison sliders, a text mask effect, image reveals, a scroll-driven progress line, a tab indicator that swaps colours seamlessly, and a theme-switch reveal. The recurring argument is that clip-path does not affect layout, is hardware-accelerated, avoids layout shift and needs no extra wrapper elements, so it beats animating width or height for reveal effects. For a design system this gives concrete, reusable recipes (exact inset values, a 1s cubic-bezier(0.77, 0, 0.175, 1) reveal, viewport-trigger options) and a pattern for tabs and theme transitions that avoids mistimed colour transitions.

## Key Ideas

- clip-path hides everything outside a clipping region without changing layout, just like transform.
- inset(top right bottom left) is the workhorse shape for animation: inset(100%) hides everything, inset(0 0 0 0) shows everything.
- Overlaying two versions of an element and clipping the top one is the basis of comparison sliders, text masks, tabs and theme switches.
- Clipping is cheaper than animating width or height: it is hardware-accelerated, needs no overflow-hidden wrapper and causes no layout shift.
- Reveal animations must be triggered when the element enters the viewport, or the user never sees them; the demo also fires them only once.
- Do not add Framer Motion just to detect viewport entry, because it is quite heavy; the Intersection Observer API does the job.
- Scroll progress can be mapped straight onto an inset value, so a 'drawn' line can just be a clipped div.
- For tabs, a clipped duplicate list styled as active gives a seamless active-state change that a text-colour transition cannot.
- Small details that most people will not consciously notice still add up to a more polished product.
- In the tabs demo code the duplicated overlay is aria-hidden and its buttons have tabIndex -1, keeping the decorative copy out of assistive technology and keyboard focus [inferred].
- Once the basics of clip-path are understood, the same technique covers many effects; it is a matter of creativity.
- Duplicating an element or the whole page to animate between two versions is hacky: fine for a quick prototype, while the View Transitions API gives the same theme reveal without duplication.

## Entities

- [[entities/emil-kowalski|Emil Kowalski]] (person): Design engineer and author of the article.
- [[entities/clip-path|clip-path]] (concept): CSS property that clips an element to a region; the subject of the article and the animated property in every example.
- [[entities/inset|inset()]] (concept): clip-path shape defining top, right, bottom and left offsets of a rectangle; used for all the animations shown.
- [[entities/framer-motion|Framer Motion]] (library): Animation library the author usually uses; provides useInView, useScroll, useTransform and useMotionTemplate, but described as quite heavy.
- [[entities/intersection-observer-api|Intersection Observer API]] (tool): Browser API recommended for viewport-triggered reveals when Framer Motion is not already in the project.
- [[entities/web-animations-api-waapi|Web Animations API (WAAPI)]] (tool): Used via element.animate() for the image reveal to keep animation logic in one place.
- [[entities/motion-value|motion value]] (concept): Framer Motion's internal value that updates without re-rendering the component and updates inline styles automatically.
- [[entities/view-transitions-api|View Transitions API]] (tool): Named as a way to get the theme-switch reveal without duplicating the whole element.
- [[entities/radix-tabs|Radix Tabs]] (library): Accessible tabs primitive the author would reach for in a real implementation of the clip-path tabs.
- [[entities/raycast|Raycast]] (company): Source of the comparison slider visuals; the image reveal demo uses a file named raycast.jpg.
- [[entities/rauno|Rauno]] (person): His tweet inspired the scroll-progress line example.
- [[entities/paco|Paco]] (person): His tweet is where the author first saw the clip-path tabs technique.
- [[entities/vercel|Vercel]] (company): Uses clip-path on its security page.
- [[entities/tuple|Tuple]] (company): Uses the width approach for a reveal where clip-path would be more performant.
- [[entities/stripe|Stripe]] (company): Its blog uses the same clip-path tabs component discussed in the article.
- [[entities/figma|Figma]] (tool): Used to apply the dashed stroke to text before converting it to SVG.
- [[entities/animations-on-the-web-animations-dev|Animations on the Web (animations.dev)]] (product): The author's course, plugged at the end of the article.
- [[entities/aiforui-dev|aiforui.dev]] (product): The author's course, mentioned in a banner at the top of the page.

## Topics

- [[topics/animation-performance|Animation performance]]: clip-path is hardware-accelerated, does not affect layout, avoids layout shift on image reveals and needs no overflow-hidden wrapper, so it outperforms animating width or height.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: Gives CSS keyframes, WAAPI and React/Framer Motion code for inset-based reveals, scroll-mapped clipping and a tabs component that computes inset values from offsetLeft and offsetWidth.
- [[topics/easing-and-timing|Easing and timing]]: Reveal animations run for 1s (duration 1000) with cubic-bezier(0.77, 0, 0.175, 1) and fill forwards.
- [[topics/micro-interactions|Micro-interactions]]: Comparison sliders, a mouse-driven text mask, a scroll-progress line and a tab indicator are all built from animated clipping.
- [[topics/navigation-and-sidebars|Navigation and sidebars]]: Tabs: instead of transitioning the active tab's text colour, clip a duplicated active-styled list to the active tab and animate the clip on click.
- [[topics/dark-mode-and-themes|Dark mode and themes]]: A theme switch can reveal the other theme by animating the clip-path of a duplicated, differently themed layer; the View Transitions API can do the same without duplication.
- [[topics/gestures-and-drag|Gestures and drag]]: A before/after slider adjusts the top image's inset from the drag position.
- [[topics/icons-and-imagery|Icons and imagery]]: Images can be revealed by animating an inset clip from fully hidden to fully visible when they scroll into view.
- [[topics/accessibility|Accessibility]]: The duplicated tab overlay is marked aria-hidden with tabIndex -1 buttons, and a real implementation should use an accessible primitive such as Radix Tabs.
- [[topics/design-taste-and-judgement|Design taste and judgement]]: Small details that often go unnoticed still add up to an experience that feels more polished.
- [[topics/figma-and-design-tools|Figma and design tools]]: The dashed text in the mask demo is a stroke applied in Figma and converted to SVG.
- [[topics/shape-and-corner-radius|Shape and corner radius]]: clip-path clips an element to a shape: circle(50% at 50% 50%), ellipse, polygon, url() for a custom SVG, or an inset rectangle with rounded corners (round 17px on the tabs).
- [[topics/ui-libraries|UI libraries]]: Framer Motion hooks (useInView, useScroll, useTransform, useMotionTemplate) drive the scroll examples, with the caution that Framer Motion is quite heavy; Radix Tabs is the accessible base for real clip-path tabs.

## Notable Claims

- clip-path is often used to trim a DOM node into shapes such as triangles, but it is also great for animations. Evidence: Intro: "But what if I told you that it’s also great for animations?"
- Content outside the clip-path region is hidden and content inside stays visible. Evidence: The Basics: "content outside of this region will be hidden"
- clip-path has no effect on layout; a clipped element occupies the same space as an unclipped one, just like transform. Evidence: The Basics: "This has no effect on layout"
- The clip-path coordinate system starts at the top left corner (0, 0). Evidence: Positioning: "It starts at the top left corner (0, 0)"
- circle(50% at 50% 50%) is a circle with a 50% radius (the article says "border radius of 50%") positioned 50% from the top and 50% from the left, the centre of the element. Evidence: Positioning: "circle(50% at 50% 50%) means"
- Besides inset, clip-path accepts ellipse, polygon and url() for a custom SVG clipping path. Evidence: Positioning: "There are other values like ellipse , polygon , or even url()"
- inset(100%, 100%, 100%, 100%), or inset(100%) as shorthand, hides the whole element; inset(0px 50% 0px 0px) hides the right half. Evidence: Positioning: "we are “hiding” (clipping) the whole element"
- A clip-path comparison slider is hardware-accelerated and needs no additional DOM elements, while the width approach needs an extra overflow-hidden element. Evidence: Comparison Sliders: "hardware-accelerated interaction without additional DOM elements"
- clip-path is hardware-accelerated, so it is more performant than animating an image's height. Evidence: Animating images: "clip-path is hardware-accelerated"
- Using clip-path for an image reveal prevents layout shift because the image is already there, just clipped. Evidence: Animating images: "prevents us from having a layout shift"
- If an image reveal is not triggered when the image enters the viewport, the user will never see it animate. Evidence: Scroll animations: "must be triggered when the image enters the viewport"
- Framer Motion is quite heavy, so it should not be added only for viewport detection. Evidence: Scroll animations: "as Framer Motion is quite heavy"
- useInView's once option triggers the animation only once, and margin "-100px" triggers it when at least 100px of the image is in view. Evidence: Scroll animations: "The once option makes sure"
- The scroll-progress line that looks like a drawn SVG is just a clipped div revealed as the user scrolls. Evidence: Scroll progress: "it’s just a clipped div"
- The offset ["start end", "end end"] measures from when the element's top reaches the viewport bottom until its bottom does, so the animation is not reverted when scrolling past. Evidence: Scroll progress: "we don’t revert the animation when the user scrolls past it"
- Motion values hold the latest value without re-rendering and update inline styles automatically, but this limits how they can be accessed; a value saved into a const would not receive updates. Evidence: Scroll progress: "The beauty of motion values"
- Transitioning the text colour of tabs is okay-ish but the colour transition can never be timed seamlessly. Evidence: Tabs transition: "which would never be seamless anyway"
- A duplicated, active-styled tab list clipped to the active tab gives a seamless transition between tabs. Evidence: Tabs transition: "we get a seamless transition between the tabs"
- Small details add up and make an experience feel more polished even if they go unnoticed. Evidence: Tabs transition: "small details like this add up"
- The theme switch reveal can be done with the View Transitions API instead of duplicating the element. Evidence: Going a step further: "you can achieve the same effect with View Transitions API"
- Vercel's security page uses clip-path, Tuple uses the width approach, and Stripe's blog uses the clip-path tabs component. Evidence: Clip Path is everywhere
- The inset values define the top, right, bottom and left offsets of a rectangle. Evidence: Positioning: "The inset values define the top, right, bottom, and left offsets of a rectangle"
- useMotionTemplate creates a new motion value from a string template containing other motion values. Evidence: Scroll progress: "This is done with the useMotionTemplate function"
- The author's 2021 theme animation duplicated the whole page; it was a bit hacky but worked for a quick prototype. Evidence: Going a step further: "The implementation was a bit hacky, as I duplicated the whole page"

## Quotes

> clip-path is hardware-accelerated, so it’s more performant than animating the height of the image.
> small details like this add up and make the experience feel more polished.
> once you understand the basics you can create many great animations with it

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: Self-promotion: a banner for the author's aiforui.dev course opens the page and the article ends by plugging his 'Animations on the Web' course at animations.dev.
- Caveat: Publication date is unknown; the Framer Motion hook names and options shown (useInView, useScroll, useTransform, useMotionTemplate) reflect the library at the time of writing and may have changed [inferred].
- Caveat: 'Hardware-accelerated' and 'more performant' are the author's statements; the article gives no measurements.
- Caveat: The tabs code is explicitly simplified; the author says a real implementation needs more work, including accessibility via Radix Tabs.
- Caveat: The theme-switch implementation is described by the author as hacky (it duplicates the element); the View Transitions API alternative is named but not shown.
- Caveat: The raw text includes leftover interactive-demo labels (e.g. '1x', 'Toggle clip path', repeated tab names and 'Switch theme') that are UI residue, not content.
- Caveat: The Figma stroke values (dash 12, gap 12, round cap and join) come from an image in the article, not from its text; they were checked by viewing the image.
- Caveat: The article writes inset(100%, 100%, 100%, 100%) and inset(0, 0, 0, 0) with commas; CSS inset() takes space-separated values, as the article's own code uses [inferred].
- Caveat: The tabs code sets the clip-path inline on each change; the transition that animates it is presumably defined in the demo's styles.css, which the text does not show [inferred].

### Rules and practices

- **should** (motion, css): Use clip-path (not width, height or extra wrapper elements) to hide and reveal parts of an element in animations, because it does not change layout. Why: An element with clip-path occupies the same space as one without it, just like transform; the article adds that clip-path is hardware-accelerated, needs no extra overflow-hidden element and avoids layout shift. [This has no effect on layout meaning that an element with clip-path will occupy the same space]
- **should** (motion, css): Use the inset() shape for clip-path animations; inset(100%) (the article's shorthand for inset(100%, 100%, 100%, 100%)) hides the whole element and inset(0 0 0 0) shows all of it. Write the values space-separated, as the article's code does (its comma form in prose is not valid CSS [inferred]). Why: inset defines the top, right, bottom and left offsets of a rectangle, so any edge can be animated to hide or reveal the element; it is what all the article's animations use. Values: inset(100%, 100%, 100%, 100%), inset(100%), inset(0, 0, 0, 0), inset(0 0 0 0). [we are going to focus on inset]
- **consider** (motion, css): To hide one half of an element, set the matching inset edge to 50%: inset(0px 50% 0px 0px) hides the right half, inset(0 0 50% 0) the bottom half, inset(50% 0 0 0) the top half. Why: Each inset value offsets one edge of the clipping rectangle from the element's edge. Values: (0px 50% 0px 0px), inset(0 50% 0 0), inset(0 0 50% 0), inset(50% 0 0 0). [Positioning: "An inset of (0px 50% 0px 0px) would make the right half"]
- **consider** (shape, css): To clip an element into a centred circle, use clip-path: circle(50% at 50% 50%). Why: The article describes it as a border radius of 50%, positioned 50% from the top and 50% from the left, which is the centre of the element. Values: circle(50% at 50% 50%). [Positioning: "circle(50% at 50% 50%) means that the circle will have a border radius of 50%"]
- **consider** (shape, css): For non-rectangular clips, clip-path also accepts ellipse, polygon, or url() to use a custom SVG as the clipping path. Why: These are the other clip-path values the article names; it uses inset for all of its animations. Values: ellipse, polygon, url(). [Positioning: "There are other values like ellipse , polygon , or even url()"]
- **should** (components, css): Build before/after comparison sliders by overlaying the two images and clipping the top one with clip-path: inset(0 50% 0 0), updating the right inset from the drag position. Why: It is the more performant approach and gives a hardware-accelerated interaction without additional DOM elements. Values: inset(0 50% 0 0). [Comparison Sliders: "clip-path: inset(0 50% 0 0)"]
- **should** (motion, css): Do not build comparison (before and after) sliders by changing the width of overflow-hidden divs; clip one of two overlaid elements with clip-path instead. Why: The width approach needs an additional element for overflow hidden and is less performant than clip-path. [we could have two divs with overflow hidden and change their width]
- **consider** (motion, css): For a text mask effect, overlay two text versions; clip the dashed text with inset(0 0 50% 0) and the filled text with inset(50% 0 0 0), then adjust both values from the mouse position. Why: It is technically a vertical comparison slider, so the same clipping technique produces the effect. Values: inset(0 0 50% 0), inset(50% 0 0 0). [Comparison Sliders: "Dashed text clip-path: inset(0 0 50% 0)"]
- **should** (motion, css): Reveal images by starting at clip-path: inset(0 0 100% 0) and animating to inset(0 0 0 0) over 1s (duration 1000 in the WAAPI version) with cubic-bezier(0.77, 0, 0.175, 1) and fill forwards. Why: Starting with a clip-path that covers the whole image makes it invisible, and animating it reveals the image; forwards keeps the revealed end state [inferred]. Values: inset(0 0 100% 0), inset(0 0 0 0), 1 s, 1000, cubic-bezier(0.77, 0, 0.175, 1), forwards. [Animating images: ".image-reveal { clip-path : inset ( 0 0 100 % 0 )"]
- **should** (motion, css): Do not animate an image's height to reveal it; animate clip-path instead. Why: clip-path is hardware-accelerated, so it is more performant than animating height, and it prevents layout shift because the image is already there, just clipped. [Animating images: "We could also do it with a height animation"]
- **must** (motion, web): Trigger reveal animations such as the image reveal when the element enters the viewport. Why: Otherwise the user will never see the image being animated. [Scroll animations: "must be triggered when the image enters the viewport"]
- **should** (tooling, web): If Framer Motion is not already in the project, detect viewport entry with the Intersection Observer API instead of adding Framer Motion. Why: Framer Motion is quite heavy. [Scroll animations: "I’d suggest you use the Intersection Observer API"]
- **should** (motion, react): Fire scroll-triggered reveals only once, and only after a meaningful part of the element is visible: with useInView use { once: true, margin: "-100px" }. Why: once makes sure the animation triggers only once; the margin makes it trigger when at least 100px of the image is in view. Values: -100px, 100px. [Scroll animations: "useInView ( ref , { once : true , margin : "-100px" } )"]
- **consider** (motion, web): Consider driving JavaScript-triggered reveals with the Web Animations API (element.animate) rather than CSS animations, so all animation logic lives in one place. Why: The author used WAAPI instead of CSS animations to keep all animation-related logic in one place. Values: 1000, forwards, cubic-bezier(0.77, 0, 0.175, 1). [Scroll animations: "I used WAAPI here instead of CSS animations"]
- **consider** (motion, web): Build scroll-progress lines as a div whose clip-path is revealed as the user scrolls, rather than an SVG path drawing. Why: The effect looks like a drawn SVG but a clipped div gradually revealed on scroll achieves it. [Scroll progress: "it’s just a clipped div which we gradually reveal upon scrolling"]
- **should** (motion, react): Measure scroll progress for a reveal with offset ["start end", "end end"] (from the element's top reaching the viewport bottom until its bottom reaches the viewport bottom). Why: This way the animation is not reverted when the user scrolls past it. Values: start end, end end. [Scroll progress: "The offset option ensures that we start measuring"]
- **should** (motion, react): Map scroll progress 0 to 1 onto the clip inset 100% to 0% (useTransform(scrollYProgress, [0, 1], ["100%", "0%"])) and apply it as inset(0 0 ${clipPathY} 0). Why: Mapping 0 to 100% and 1 to 0% reveals the element progressively; everything in between is calculated automatically. Values: 0 to 1, 100%, 0%. [Scroll progress: "I basically map 0 to 100% and 1 to 0%"]
- **must** (motion, react): Keep scroll-driven values as motion values end to end (compose them with useMotionTemplate) and pass them as inline style; do not copy them into a plain const. Why: Motion values update inline styles automatically without re-rendering the component; a value saved into a const would not receive updates. [Scroll progress: "If I saved it in a const variable for example, it would not receive updates"]
- **should** (components, web): Do not rely on a text-colour transition to show the active tab changing. Why: It is only okay-ish; the colour transition can never be timed to be seamless. [Tabs transition: "Usually, people apply a transition to the text color"]
- **should** (components, web): Animate tab changes by duplicating the tab list, styling the duplicate as active (blue background, white text), clipping it to the active tab with a rounded inset (e.g. inset(0px 75% 0px 0% round 17px)), and animating that clip-path on click. Why: This gives a seamless transition between tabs without having to time a colour transition. Values: inset(0px 75% 0px 0% round 17px), round 17px. [Tabs transition: "We can duplicate the list and change the styling of it"]
- **consider** (components, react): Compute the tab clip from the active tab's geometry: left inset = (offsetLeft / container.offsetWidth) * 100 %, right inset = 100 - ((offsetLeft + offsetWidth) / container.offsetWidth) * 100 %, rounded with toFixed() and recalculated whenever the active tab changes. Why: The clip must match the active tab's position and width within the container so only that tab in the duplicated list is visible; this is the author's simplified demo code. Values: clipLeft = offsetLeft, clipRight = offsetLeft + offsetWidth, round 17px. [Tabs transition code: "const clipRight = offsetLeft + offsetWidth"]
- **consider** (process, all): When reviewing a layered clip-path transition, turn the clip off to see the unclipped duplicate and slow the animation down to judge the transition. Why: Toggling the clip shows how it looks without clipping, and slowing it down helps you notice the difference in transition. [Tabs transition: "Slowing it down by clicking on the button next to it will help you notice the difference in transition"]
- **should** (accessibility, web): Hide the duplicated decorative layer from assistive technology and keyboard focus, as the author's code does: aria-hidden on the overlay container and tabIndex={-1} on its buttons. Why: The duplicated list is only visual and the real, focusable list sits underneath; the article shows this in code without stating a reason [inferred]. Values: aria-hidden, tabIndex = { - 1 }. [Tabs transition code: "< div aria-hidden className = "clip-path-container""]
- **should** (accessibility, react): In production, build clip-path tabs on an accessible tabs primitive such as Radix Tabs rather than the simplified demo. Why: The demo is simplified to focus on clip-path; the actual implementation would require more work to be accessible. [Tabs transition: "to make it more accessible, I’d reach for Radix’s Tabs"]
- **should** (process, all): Polish small interaction details such as tab transitions even when most users will not notice them. Why: Small details add up and make the experience feel more polished, even if they go unnoticed. [Tabs transition: "You might say that not everyone is going to notice the difference"]
- **consider** (motion, web): Animate theme switches by revealing the new theme with an animated clip-path (inset(0 0 100% 0) to inset(0 0 0 0), 1s, cubic-bezier(0.77, 0, 0.175, 1), forwards) over the current one, choosing which layer to animate from the current theme stored in state. Why: The same basic clip-path reveal technique produces the theme transition. Values: inset(0 0 100% 0), inset(0 0 0 0), 1 s, cubic-bezier(0.77, 0, 0.175, 1), forwards. [Going a step further: ".clipPathReveal { clip-path : inset ( 0 0 100 % 0 )"]
- **should** (motion, web): Prefer the View Transitions API over duplicating the whole page or element for a theme-switch reveal. Why: Duplicating the element you want to animate is hacky (the author's 2021 version was fine only as a quick prototype); the View Transitions API achieves the same effect. [Going a step further: "While this implementation is hacky as it requires duplicating the element"]
- **consider** (tooling, web): Make dashed outline text by applying a dashed stroke to the text in Figma and converting it to SVG (the article's screenshot shows Advanced stroke with style Dash, dash 12, gap 12, round dash cap and round join; values read from the image, not the text). Why: That is how the dashed text in the text mask demo was produced. [Comparison Sliders: "The dashed text here is a stroke applied in Figma that is then converted to SVG"]

### Decisions it informs

- How should a before/after comparison slider hide part of the top image?
  - Two overflow-hidden divs with changing width: Works, but needs an additional element for overflow hidden and is less performant than clip-path. When: The source prefers clip-path; it cites Tuple as using this approach where clip-path would be more performant.
  - clip-path: inset() on the top image: Hardware-accelerated, no extra DOM elements; the right inset follows the drag position. When: Default for comparison sliders and similar reveals.
  - Recommendation: clip-path inset, because it is more performant and needs no additional DOM elements.
- How should an image be revealed when it appears?
  - Animate height: Less performant and causes a layout shift as the image grows. When: The source prefers clip-path over this.
  - Animate clip-path from inset(0 0 100% 0) to inset(0 0 0 0): The image already occupies its space and is uncovered smoothly, with no layout shift. When: Default for image reveals.
  - Recommendation: Animate clip-path, since it is hardware-accelerated and prevents layout shift.
- What should detect that an element has entered the viewport to start a reveal?
  - Framer Motion useInView: Convenient hook returning a boolean, with once and margin options. When: The project already uses Framer Motion.
  - Intersection Observer API: Native browser API, adds no library weight. When: Framer Motion is not already in the project.
  - Recommendation: Use useInView only if Framer Motion is already present; otherwise use the Intersection Observer API because Framer Motion is quite heavy.
- How should the active tab change be animated?
  - Transition the text colour: Okay-ish; timing the colour transition would never be seamless. When: The source calls this okay-ish and prefers the clip-path approach.
  - Clipped duplicate active-styled list: The active style (blue background, white text) slides between tabs as one seamless reveal. When: When a polished tab indicator is wanted.
  - Recommendation: Duplicate the list, style it active and animate its clip-path, because the transition is seamless and needs no colour timing.
- How should a theme-switch reveal animation be built?
  - Duplicate the page or element in both themes and animate clip-path: Works for a quick prototype, but is hacky because everything is rendered twice. When: Quick prototypes.
  - View Transitions API: Achieves the same reveal effect without duplicating the element. When: When you want the same reveal without duplicating the element.
  - Recommendation: The source calls duplication hacky and points to the View Transitions API for the same effect.
- Should JavaScript-triggered animations be written as CSS animations or with the Web Animations API?
  - CSS animations (@keyframes): Animation defined in the stylesheet, separate from the trigger logic. When: Purely CSS-triggered effects [inferred].
  - Web Animations API (element.animate): Keyframes, duration, fill and easing live next to the trigger logic. When: When the animation is started from JavaScript, e.g. on viewport entry.
  - Recommendation: The author used WAAPI to keep all animation-related logic in one place.
- How should a scroll-progress line that grows as the user scrolls be built?
  - SVG path that gets drawn: What the effect looks like at first glance. When: The source does not use it for this effect.
  - Clipped div revealed on scroll: A div whose bottom inset is mapped from scroll progress (0 to 1 onto 100% to 0%), gradually revealed as the user scrolls. When: The source's implementation of the effect.
  - Recommendation: The source builds it as a clipped div gradually revealed upon scrolling.

### Process

1. Overlay two layers: Place the two versions (before/after images, dashed/filled text, inactive/active tab lists, light/dark theme) exactly on top of each other.
2. Clip the top layer with inset(): Start with the inset that hides the part you do not want visible, e.g. inset(0 50% 0 0) for a slider or inset(0 0 100% 0) for a hidden image.
3. Drive the inset from input: Update the inset from drag position, mouse position, scroll progress, the active tab's geometry or the stored theme state.
4. Trigger reveals on viewport entry: Start the reveal when the element enters the viewport, only once and after at least 100px is visible (once: true, margin: "-100px"), using Intersection Observer if Framer Motion is not already used.
5. Animate the reveal: Animate to inset(0 0 0 0) over 1s with cubic-bezier(0.77, 0, 0.175, 1) and fill forwards, via CSS keyframes or element.animate.
6. Check the effect: Toggle the clip off to see the unclipped duplicate and slow the animation down to notice the difference in transition.
7. Hide duplicates from assistive tech: Mark the duplicated overlay aria-hidden and give its buttons tabIndex -1; build real tabs on an accessible primitive such as Radix Tabs.

### Examples and visual references

- Before/after comparison slider (Visuals from Raycast): Two abstract wallpapers of diagonal light bands on black, the 'Before' in reds and pinks and the 'After' in blues and violets; the top image is clipped with inset(0 50% 0 0) and the split follows the drag handle (images viewed from the article's media).
- Text mask effect on the words 'Clip Path' (Article demo): Dashed outline text and filled text stacked; the dashed version shows above the split and the filled version below, and the split follows the mouse. The article image shows Figma's Advanced stroke panel with stroke style Dash, dash 12, gap 12 (greyed) and the round dash cap and round join selected (values read from the image, not the text).
- Scroll-triggered image reveal (Raycast image (raycast.jpg, 644 x 430 in the demo)): Per its alt text, an image of diagonal black and white stripes with a smooth gradient; it starts fully clipped and is uncovered by animating the bottom inset from 100% to 0, so it appears from the top edge downward [inferred].
- Scroll-progress vertical line (Inspired by a tweet from Rauno): A vertical line that grows as the page scrolls; it looks like an SVG being drawn but is a clipped div whose bottom inset is mapped from scroll progress.
- Clip-path tabs (Payments / Balances / Customers / Billing demo; same component used on Stripe's blog; technique first seen in a tweet from Paco): A row of icon-and-label tabs; the active tab has a blue rounded pill (round 17px) with white text, and switching tabs slides the clipped active layer to the new tab instead of cross-fading text colours. A 'Toggle clip path' button in the demo shows the unclipped duplicate list.
- Theme switch reveal (Shared on X in 2021 and rebuilt as a demo in the article): A light and a dark copy of the same content are stacked; pressing 'Switch theme' reveals the other theme by animating the clip-path.
- clip-path in production (Vercel security page; Tuple; Stripe blog): Vercel uses clip-path on its security page, Tuple uses the less performant width approach for a similar reveal, and Stripe's blog uses the clipped tabs.

### Numbers

- circle(50% at 50% 50%): Clip an element to a circle with a 50% radius centred in the element. [The Basics]
- (0, 0): The clip-path coordinate system starts at the top left corner. [Positioning]
- inset(100%): Shorthand for inset(100%, 100%, 100%, 100%), hiding the whole element. [Positioning]
- (0px 50% 0px 0px): An inset of (0px 50% 0px 0px) hides the right half of an element. [Positioning]
- inset(0 50% 0 0): Initial clip on the top image of a comparison slider. [Comparison Sliders]
- inset(0 0 50% 0): Clip on the dashed text in the text mask effect (hides its bottom half). [Comparison Sliders]
- inset(50% 0 0 0): Clip on the filled text in the text mask effect (hides its top half). [Comparison Sliders]
- 1000: Reveal duration in the WAAPI code (duration : 1000); the CSS image and theme reveals use 1s, scraped as "1 s". [Scroll animations; Animating images; Going a step further]
- cubic-bezier(0.77, 0, 0.175, 1): Easing used for the image reveal and theme reveal. [Animating images; Going a step further]
- inset(0 0 100% 0): Hidden start state for the image and theme reveals. [Animating images; Going a step further]
- inset(0 0 0 0): Fully revealed end state for the image and theme reveals. [Animating images; Going a step further]
- -100px: useInView margin so the reveal triggers when at least 100px of the image is in view. [Scroll animations]
- [ "start end" , "end end" ]: useScroll offset for the scroll-progress line so the animation is not reverted after scrolling past. [Scroll progress]
- map 0 to 100% and 1 to 0%: Scroll progress mapped onto the bottom inset of the progress line. [Scroll progress]
- round 17px: Corner rounding of the clipped active-tab region. [Tabs transition]
- inset(0px 75% 0px 0% round 17px): Clip that shows only the first of four tabs in the duplicated active list. [Tabs transition]
- 2021: Year the author shared the original theme animation on X. [Going a step further]

<!-- /od:learn -->
