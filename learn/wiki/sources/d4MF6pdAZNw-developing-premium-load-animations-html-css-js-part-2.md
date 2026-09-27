---
type: source
title: "Developing Premium Load animations (HTML, CSS & JS): Part 2"
created: 2026-09-27
updated: 2026-09-27
video_id: d4MF6pdAZNw
url: https://www.youtube.com/watch?v=d4MF6pdAZNw
channel: Kole Jain
published: 2024-03-02T20:11:04Z
authority: reference
tags:
  - gsap
  - load-animation
  - loading-screen
  - preloader
  - navbar
  - text-wipe
  - stagger
  - timeline
  - easing
  - expo-in-out
  - html-css-js
  - code-along
---

# Developing Premium Load animations (HTML, CSS & JS): Part 2

## Metadata

- Video ID: `d4MF6pdAZNw`
- Channel: Kole Jain
- Published: 2024-03-02T20:11:04Z
- URL: https://www.youtube.com/watch?v=d4MF6pdAZNw

## Summary

Kole Jain codes three website load animations with HTML, CSS, JavaScript and the GSAP library, as part 2 of a series that first designed them as Figma prototypes. The first is a loading screen: a black full-screen overlay where the logo fades in, then the overlay slides up while the hero text slides up from below and the navbar fades in last. The second is a navbar that grows from a dot into a circle, stretches into a pill, and then fades its items in one after another. The third is a text wipe, where a colored block (its background color copied from elsewhere in the stylesheet) sweeps across a headline and retracts to reveal it. For the big moves he uses the expo.inOut ease to match the custom curves from the Figma prototypes, and builds each animation as a paused timeline of chained steps. For a design system, it shows how a designed motion curve and a few timing values carry over into code, and how to order steps so related moves run together or in sequence.

## Key Ideas

- A load animation can be built as a GSAP timeline: a chain of steps that run one after another unless told to overlap.
- The expo.inOut ease reproduces the look and feel of the custom bezier curves designed in the Figma prototype.
- Elements that animate in are first put in their starting state (opacity 0, width 0%, max-width 0px, or a yPercent offset), set either in CSS or with gsap.set.
- Related moves can run together: the hero text slides up at the same moment the loading screen slides away, using the "<" position marker.
- Moving an element by yPercent uses a percentage of the element's own height, not the viewport's.
- A pill navbar can grow from a dot: scale from 0 to 1, then widen max-width from the bar's own height (a circle) to its full width.
- Reading an element's real height with gsap.getProperty lets the animation start as a perfect circle.
- Stagger fades a group of items in one at a time with a single call, instead of one call per item.
- A text wipe grows a colored block across the text, makes the text visible underneath, then anchors the block to the right and shrinks it away.
- The navbar simply fades in at the end over 0.3; the source says it doesn't need an ease per se.
- You might need to play with the timings a little after the first run.

## Entities

- [[entities/kole-jain|Kole Jain]] (person): Designer and YouTuber who codes the three load animations in the video.
- [[entities/gsap|GSAP]] (library): JavaScript animation library used for timelines, to, fromTo, set, getProperty and stagger.
- [[entities/figma|Figma]] (tool): Where the animations were prototyped with custom bezier curves in part 1 of the series.
- [[entities/vs-code|VS Code]] (tool): Code editor where the animations are developed.
- [[entities/bubble|Bubble]] (product): The demo's brand name, typed next to the logo on the loading screen.
- [[entities/discord|Discord]] (product): Its icon sits in the navbar's "join us" section of the demo.
- [[entities/timeline|Timeline]] (concept): A paused GSAP sequence of chained animation steps, started with play().
- [[entities/stagger|Stagger]] (concept): A setting that animates several elements one after another from one call.
- [[entities/text-wipe|Text wipe]] (concept): A reveal where a colored block sweeps across text and retracts to show it.
- [[entities/loading-screen|Loading screen]] (concept): A full-screen branded overlay that fades in the logo and then slides away to reveal the page.

## Topics

- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: Step-by-step HTML, CSS and GSAP code for a loading screen, an expanding navbar and a text wipe, including fixed full-screen overlays, flex centering, hidden starting states and paused timelines.
- [[topics/easing-and-timing|Easing and timing]]: Uses expo.inOut to match the Figma prototype's custom bezier curves, with durations of 1 to 1.3 for large moves, 0.8 for the scale-up, 0.6 with a 0.2 stagger for items and 0.3 for the navbar fade.
- [[topics/landing-pages|Landing pages]]: Load animations meant to wow clients (per the video description), shown on demo pages where a header background image with text on top slides into view as the loading screen leaves.
- [[topics/navigation-and-sidebars|Navigation and sidebars]]: A translucent pill navbar with a menu, a centered logo and a join link, which grows from a dot into a pill and then fades its items in one by one.
- [[topics/feedback-empty-and-loading-states|Feedback, empty and loading states]]: A branded loading screen: a black full-screen overlay where the logo and wordmark fade in, then the screen slides up to reveal the page.
- [[topics/prototyping|Prototyping]]: The animations were first prototyped in Figma with custom bezier curves; this part carries that feel into code with expo.inOut.

## Notable Claims

- The expo.inOut ease gives the same look and feel as the custom bezier curves used in the Figma prototype. Evidence: custom bezies in figma
- Setting yPercent to 100 moves an element down by 100% of its own height, not 100% of the viewport. Evidence: not 100% of the viewport
- A chained timeline step normally starts right after the previous one; adding "<" makes it start at the same time. Evidence: hit this back arrow
- fromTo lets you set both a start and an end state, where to only sets the end state. Evidence: use a from two instead of just a two
- If the navbar's width equals its height, it is a circle, so max-width starts at the measured height. Evidence: then we have a circle
- If the navbar's CSS max-width is not changed to 0px before the fromTo, the animation will not work well. Evidence: change this down to0 pixels
- gsap.getProperty returned the nav container's height, 27 pixels in this demo. Evidence: returned pixels 27
- Stagger animates the items one at a time: the first, then the second, then the third. Evidence: stagger is going to do them one at a time
- Setting right to 0 is often enough to make the wipe finish on the right, but sometimes left must also be set to auto. Evidence: set left to Auto in order for it to work
- Hiding an element's starting state can be done in CSS or with gsap.set, and each has pros and cons. Evidence: there are pros and cons

## Quotes

> if our width is equal to our height then we have a circle
> it's 100% of the length of this element okay not 100% of the viewport
> stagger is going to do them one at a time

<!-- od:learn -->

## For OpenDesigner

- Authority: **reference**
- Caveat: Auto-generated captions: GSAP is heard as "gap", expo.inOut as "Expo in out", yPercent as "y%", getProperty as "getet property", to and fromTo as "two" and "from two", navbar as "Navar" and z-index as "Zed index"; the "<" position marker is described only as typing quotes and "this back arrow", and the variable "LMS" is read as elms [inferred]. Numbers were not changed.
- Caveat: This is a code-along tutorial: the values (500px, 1-second delay, 0.2 stagger) fit this demo page, and the source says you might need to play with the timings.
- Caveat: The custom bezier curves from the Figma prototype are in part 1 of the series; this video gives no curve values, only the expo.inOut ease that approximates them.
- Caveat: The duration of the first logo fade-in is not stated.
- Caveat: The first timeline (the loading screen) is created paused, but the transcript never shows play() being called on it; play() is only shown for the navbar and the text wipe.
- Caveat: The caption text around the end of the navbar section is garbled, so the finished navbar result is not described in words.
- Caveat: Published March 2024; the GSAP calls shown are from that time [inferred].
- Caveat: The video does not discuss reduced-motion settings or how long a loading screen holds back the content [inferred].
- Caveat: Ends with a request to subscribe.

### Rules and practices

- **should** (motion, web): Use the expo.inOut ease for the large load-animation moves (the loading screen sliding away, the navbar widening, the text wipe) so the code matches the custom bezier curves designed in Figma. Why: It gives the same look and feel as the custom beziers in the Figma prototype. Values: expo.inOut, duration 1.3, duration 1. [set our ease to Expo in out and this is important]
- **should** (motion, web): Put each element that will animate in into its hidden starting state (opacity 0, width 0% or max-width 0px), in CSS or with gsap.set, before the timeline runs. Why: The element disappears first so it can be animated in with JavaScript. Values: opacity: 0, width: 0%, max-width: 0px. [this opacity to zero okay and so that's going to make our element here disappear]
- **should** (motion, web): When a loading screen slides away, slide the content beneath it up at the same time by starting its step with the "<" position marker instead of chaining it after. Why: The things underneath should also slide up, and a chained step would otherwise start only after the previous one ends. Values: "<", yPercent: -100, yPercent: 100, yPercent: 0, duration 1.3, expo.inOut. [we can then animate it up up while our loading screen is moving up]
- **consider** (motion, web): Offset text below its resting place with yPercent so the distance is relative to the element's own height, then animate it back to 0. Why: yPercent 100 is 100% of the element's length, not 100% of the viewport. Values: yPercent: 100, yPercent: 0. [it's 100% of the length of this element]
- **consider** (motion, web): Fade the navbar in last, after the loading screen and hero text have slid up, with a short fade and no special ease. Why: The navbar should appear after everything has slid up; the source says it doesn't need an ease. Values: opacity: 1, duration 0.3. [we want our navbar to fade in after everything has slid up]
- **consider** (components, css): Build a loading screen as a fixed overlay at top 0 and left 0, 100vw by 100vh, with a high z-index, a black background and flex centering for the logo. Why: Top and left 0 avoid spacing issues, the z-index keeps it on top of everything, and flex centers the logo container. Values: position: fixed, top: 0, left: 0, z-index: 10, width: 100vw, height: 100vh, align-items: center, justify-content: center. [section. loading screen]
- **should** (motion, web): To make a pill navbar grow from a dot, first scale it from 0 to 1, then animate max-width from the bar's measured height up to its full width with expo.inOut. Why: Starting max-width at the bar's height makes width equal height, so the bar starts as a circle before stretching. Values: scale: 0, scale: 1, duration 0.8, max-width: 500px, duration 1.3, expo.inOut. [max width okay so make sure to remember]
- **consider** (motion, web): Measure the navbar's rendered height with gsap.getProperty and use it as the starting max-width. Why: The width must equal the height to get a circle, and getProperty returns the real height (27 pixels here). Values: 27. [gap. getet property]
- **must** (motion, css): Set the navbar's CSS max-width to 0px before animating max-width with fromTo. Why: If you don't change it, the animation isn't going to work very well. Values: max-width: 0px. [make sure to remember to come back here]
- **consider** (motion, web): Fade a group of navbar items in one after another with a single staggered call on an array of the items. Why: It is faster and easier than selecting and animating each item one at a time. Values: opacity: 1, stagger: 0.2, duration 0.6. [something new it's called stagger]
- **should** (motion, web): For a text wipe, grow a colored block from 0% to 100% width over the text, make the text visible, anchor the block to the right, then shrink it back to 0%. Why: The wipe starts on the left and finishes on the right, revealing the text behind it. Values: width: 0%, width: 100%, duration 1, expo.inOut, right: 0, left: auto. [width of that to 100% um we'll set the duration to be equal to 1]
- **consider** (motion, css): If right: 0 alone does not move the wipe block's anchor to the right, also set left to auto. Why: Setting right to 0 is often all you need, but sometimes left also has to be auto for it to work. Values: right: 0, left: auto. [set left to Auto in order for it to work]
- **consider** (motion, css): If the full-size wipe block looks too large, shrink its height (80% here) and move it down (top 10%) so the bottom of the text is still covered. Why: At full size the block was larger than wanted, and after shrinking it the bottom of the text showed until it was moved down. Values: height: 80%, top: 10%. [set the height to 80%]
- **consider** (components, css): Style the navbar as a translucent pill: an outer section that centers the nav container, which uses flex with space-between and centered items, a background color with alpha 61, border-radius 100px, and padding of 10px on top and 30px on the sides. Why: The source adds these so the bar looks better before animating it. Values: justify-content: space-between, align-items: center, 61, border-radius: 100px, 10px, 30px, max-width: 500px, width: 100%, gap: 10px. [add a border radius as well we'll do 100 pixels]
- **consider** (components, css): On the loading screen, wrap the logo image and the brand name in one container set to display flex with a small gap (10px) and centered content, so they sit side by side in the middle and fade in as one. Why: The container lets the logo be centered, and the logo should sit right beside the text rather than one on top of the other. Values: display: flex, gap: 10px, justify-content: center, width: 10%. [so that we can Center it later]
- **should** (layout, css): Give the navbar width: 100% alongside max-width: 500px, because max-width on its own does not size the bar. Why: The source notes that max-width alone is not actually going to do anything, so a width has to be set as well. Values: max-width: 500px, width: 100%. [that's not actually going to do anything]

### Decisions it informs

- Which load animation should greet visitors when the site opens?
  - Loading screen: A black full-screen overlay shows the logo and name fading in, then slides up to reveal the page while the hero text slides up with it. When: When you want a branded moment before the hero appears [inferred].
  - Expanding navbar: The navbar grows from a tiny dot into a circle, stretches into a pill, then its items fade in one by one. When: When the navbar is the element to draw attention to on landing [inferred].
  - Text wipe: A colored block sweeps across a large headline and retracts to the right, revealing the text. When: When a big headline carries the page [inferred].
- Should the next step of the load animation wait for the previous one or run at the same time?
  - One after another (default): Each step starts right after the previous one ends, like the logo fade, then the screen slide, then the navbar fade. When: When one move should finish before the next starts, such as fading the navbar in after everything has slid up.
  - At the same time ("<"): The step starts with the one before it, so the hero text rises together with the loading screen. When: When the content underneath should move along with the element leaving.
  - Recommendation: Run the hero text slide-up at the same time as the loading screen slide-up, and fade the navbar in afterwards.
- Where should an element's hidden starting state be set: in CSS or in JavaScript with gsap.set?
  - CSS: The element is hidden by the stylesheet (for example opacity 0) before any script runs. When: Used here for the logo container and the text wipe's width.
  - gsap.set: The script hides or offsets the element (for example the navbar's opacity or the header text's yPercent) before the timeline runs. When: Used here for the navbar and the header text on the loading-screen page.
- How should several navbar items be faded in?
  - One call per item: Each item is selected and faded separately. When: The source calls it totally a viable option.
  - One staggered call: All items go in an array and fade in one after another from a single call (stagger 0.2, duration 0.6). When: When you want it faster and easier to write.
  - Recommendation: A single staggered call, because it is faster and easier.
- Should an animation step state only where it ends (to) or both where it starts and ends (fromTo)?
  - to: Only the end position is set, for example opacity 1 after the CSS already set opacity 0. When: Used here for the logo fade, the loading-screen slide and the text wipe.
  - fromTo: Both a start and an end position are set, for example scale 0 to 1, or max-width from the bar's height to 500px. When: Used here for the navbar, which starts as a dot and then a circle.

### Process

1. Prototype first: Design the load animations in Figma with custom bezier curves (part 1 of the series), then develop them in code.
2. Build the static page: Set up the page's HTML and CSS without motion, such as a navbar and a hero with a background image and absolutely positioned text.
3. Add the animation element: Add the extra element the animation needs: the loading-screen section, the nav container or the text-wipe block, and style it in CSS.
4. Hide the starting state: Set what will animate in to its hidden start: opacity 0, width 0%, max-width 0px, or a yPercent offset with gsap.set.
5. Create a paused timeline: Create a gsap.timeline with paused set to true.
6. Chain the steps: Add steps with to, fromTo and set, giving each a duration, an ease (expo.inOut for the big moves) and an optional delay; use "<" for steps that should run together and stagger for groups.
7. Play it: Call play() on the timeline, with the brackets.
8. Reload and tune: Reload the page to watch the result and adjust the timings as needed.

### Examples and visual references

- Loading screen for a brand called Bubble (Demo landing page with a hero background image): A black full-screen overlay with a small logo and the word "bubble" side by side in the center. After a 1-second delay the logo fades in, then the overlay slides up (yPercent -100, 1.3, expo.inOut) while the hero text rises from below at the same time; the navbar fades in last over 0.3.
- Expanding pill navbar (Demo page with a blur at the top, intro text and cards): A translucent, fully rounded bar with a hamburger icon and "Menu" on the left, a logo in the middle, and a Discord icon with "join us" on the right. It scales up from a dot (0.8), stretches from a circle to a 500px pill (1.3, expo.inOut), then the three sections fade in one after another (stagger 0.2).
- Text wipe reveal on a large headline (Demo page with a background image and big text): A colored block, 80% as tall as the text container and 10% down from the top, grows left to right to cover the headline (1, expo.inOut), then retracts toward the right (1, expo.inOut) to reveal the text.

### Numbers

- z-index 10: Keeps the loading screen on top of everything. [we'll go with 10]
- 100 view width / 100 view height: Loading screen size. [a width of 100 view width]
- 10 pixels: Gap between the logo and the name on the loading screen, and between icon and text in the navbar sections. [let's start with 10 pixels]
- 10%: Width of the logo image on the loading screen. [a width of maybe 10%]
- 1 second: Delay before the logo fades in. [1 second of DeLay]
- 1.3: Duration of the loading screen slide-up (first tried at 1), the hero text slide-up and the navbar widening. [a duration of maybe 1.3]
- -100%: yPercent that moves the loading screen fully up out of view. [set y% to - 100%]
- 100: yPercent that moves the hero text down by its own height before it slides up. [y% of 100]
- 0.3: Duration of the navbar fade-in. [our duration to 0.3]
- 500 pixels: Final max-width of the pill navbar. [a Max width of 500 pixels]
- 61: Alpha added to the end of the navbar's background color for transparency. [we'll Add 61 at the end]
- 100 pixels: Border radius of the navbar pill. [we'll do 100 pixels]
- 10 pixels on top and 30 pixels on the side: Navbar padding. [10 pixels on top and 30 pixels on the side]
- 27: Height in pixels that gsap.getProperty returned for the nav container. [returned pixels 27]
- 0.8: Duration of the navbar's scale from 0 to 1. [a duration of 0.8]
- 0.2: Stagger between the navbar items fading in. [our stagger to 0.2]
- 0.6: Duration of each navbar item's fade-in. [our duration can be 0.6]
- 80%: Height of the text-wipe block. [set the height to 80%]
- 10%: Top offset of the text-wipe block. [set our top down 10%]
- 1: Duration of each half of the text wipe (grow and shrink). [our duration is going to be one again]
- 100%: Navbar width, set because max-width alone did nothing. [set our width to 100%]

<!-- /od:learn -->
