---
type: source
title: "Prototyping Professional Load Animations in Figma: Part 1"
created: 2026-09-27
updated: 2026-09-27
video_id: nl8OFGdx75w
url: https://www.youtube.com/watch?v=nl8OFGdx75w
channel: Kole Jain
published: 2024-02-27T02:19:40Z
authority: reference
tags:
  - figma
  - prototyping
  - smart-animate
  - load-animation
  - loading-screen
  - navbar
  - text-wipe
  - easing
  - custom-bezier
  - timing
  - page-load
  - kole-jain
---

# Prototyping Professional Load Animations in Figma: Part 1

## Metadata

- Video ID: `nl8OFGdx75w`
- Channel: Kole Jain
- Published: 2024-02-27T02:19:40Z
- URL: https://www.youtube.com/watch?v=nl8OFGdx75w

## Summary

Kole Jain prototypes three website load animations in Figma with Smart Animate: a black loading screen that slides up to reveal the page, a navbar that expands out of a single dot, and a text wipe where a thin bar sweeps across and reveals a line of text. Each one is built as a chain of duplicated frames, each frame holding one state (moved, squeezed or transparent), linked by after-delay interactions. He uses a custom bezier dragged into an exponential curve for the big movements and ease in and out for the nav fades and the dot growing into a circle, and gives the exact delays and durations for every step. For a design system, it is a worked example of choreographing a page-load sequence step by step, with real timing values, and of a practical Figma frame-by-frame workflow for prototyping motion before building it in code.

## Key Ideas

- A page-load sequence can be split into a few small states, each one a Figma frame, and chained with after-delay interactions.
- When a loading screen slides up, nudging the page content down first lets it slide up too, which makes the reveal look better.
- Hide elements that should arrive later by setting them transparent in the early frames, then fade them in at the end.
- Build an expanding shape by working backwards: duplicate the finished frame and squeeze it down until width matches height (a circle), then to a 1 by 1 pixel dot, then make the dot transparent.
- Big movements (the loading screen, the navbar expanding, the text wipe) use a custom bezier dragged into an exponential curve.
- Small fades of navbar items use Smart Animate with ease in and out at 200 milliseconds.
- Steps are chained with a 1 millisecond after-delay, so each Smart Animate step starts right after the previous one and the frames play as one sequence [inferred].
- Instant navigation is used for the steps that only change what is visible, such as showing the dot or switching the text to opaque between the bar's moves.
- A text wipe uses a rectangle one pixel wide, a little taller than the text and in the right colour, that is animated across the text over 700 milliseconds, with the text switched from transparent to opaque between moves.
- Navbar items can come in one after another (menu, then logo, then the join us button) rather than all at once.
- Part 1 prototypes the motion in Figma; part 2 builds the same animations in code with HTML, CSS, JavaScript and GSAP.

## Entities

- [[entities/kole-jain|Kole Jain]] (person): Owner of the channel, who presents the tutorial.
- [[entities/figma|Figma]] (tool): Design tool used to build and prototype all three animations.
- [[entities/smart-animate|Smart Animate]] (tool): Figma's prototyping function named in the description and used for the animated steps; it animates matching layers between frames [inferred].
- [[entities/gsap|GSAP]] (library): Animation library named in the description for building the animations in part 2.
- [[entities/vs-code|VS Code]] (tool): Code editor where part 2 turns the prototypes into HTML, CSS and JavaScript.
- [[entities/loading-screen-animation|Loading screen animation]] (concept): A full-screen cover with the logo that slides up to reveal the page content.
- [[entities/expanding-navbar|Expanding navbar]] (concept): A navbar that grows out of a tiny dot into a circle and then to full size, with its items fading in; the presenter's favourite of the three.
- [[entities/text-wipe|Text wipe]] (concept): A thin bar sweeps across a line of text and reveals it, then sweeps off.
- [[entities/custom-bezier|Custom bezier]] (concept): A Figma easing option whose handles are dragged out to give an exponential curve for the larger movements.

## Topics

- [[topics/prototyping|Prototyping]]: Shows how to prototype three load animations in Figma as chains of frames linked by after-delay interactions, using Smart Animate, instant navigation and flow starting points.
- [[topics/figma-and-design-tools|Figma and design tools]]: Walks through Figma's prototype panel: after-delay triggers, Smart Animate, ease in and out, custom bezier handles, instant navigation and the flow starting point button.
- [[topics/easing-and-timing|Easing and timing]]: Gives exact delays and durations for each step: 1,000 ms hold then an 800 ms custom bezier slide, 200 ms ease in and out fades, 300 ms and 400 ms for the expanding circle, 700 ms for each wipe pass.
- [[topics/feedback-empty-and-loading-states|Feedback, empty and loading states]]: A loading screen with a centred logo slides up to reveal the page, with the content underneath rising with it and the nav fading in afterwards.
- [[topics/landing-pages|Landing pages]]: Presents the three load animations as a way to make a website feel more premium on first load.
- [[topics/navigation-and-sidebars|Navigation and sidebars]]: An expanding navbar grows from a 1 by 1 pixel dot to a 53 by 53 pixel circle and then to full width, after which the menu, logo and join us button fade in one after another.
- [[topics/micro-interactions|Micro-interactions]]: A text wipe reveals a line of text with a thin coloured bar that is animated across it and back.

## Notable Claims

- The three loading animations make a website feel more premium. Evidence: going to make your website feel so much more premium
- Sliding the page content down slightly before the loading screen lifts, so it rises with the screen, makes the effect look good. Evidence: this content will slide up as well which really makes our effect look good
- Dragging out the custom bezier handles gives more of an exponential curve. Evidence: drag out these handles just like before to give us more of an exponential curve
- The expanding navbar frames are built by working backwards from the finished frame, squeezing it down until height and width match. Evidence: we're going to work backwards by duplicating this Frame
- The navbar item fades can all use the same settings. Evidence: all of these animations will in fact be the same

## Quotes

> going to make your website feel so much more premium
> this content will slide up as well which really makes our effect look good
> to give us more of an exponential curve

<!-- od:learn -->

## For OpenDesigner

- Authority: **reference**
- Caveat: This is a hands-on Figma tutorial; the timings are the presenter's choices for one demo (he says 300 milliseconds is probably fine for right now), not tested rules.
- Caveat: The custom bezier is set by dragging handles by eye; no bezier values are given.
- Caveat: For the text wipe, the transcript does not make fully clear the exact frame order or whether the bar is moved or stretched across the text; the analysis keeps to what is said.
- Caveat: It is part 1 of 2; the code build with HTML, CSS, JavaScript and GSAP is in part 2 and not covered here.
- Caveat: Published in February 2024; the Figma prototyping interface may have changed since.
- Caveat: The description promotes a free Figma file with the starting frames and finished prototypes.
- Caveat: Auto-generated captions without punctuation; 'anim' near the start is likely a cut-off 'animation'. The numbers read consistently in context [inferred].

### Rules and practices

- **consider** (motion, all): When a loading screen slides up to reveal the page, place the page content slightly lower at the start so it slides up into its centred position together with the loading screen. Why: The content sliding up as well is what really makes the effect look good. [take all of our other elements and slide them down ever so slightly]
- **consider** (motion, all): Hold the loading screen for 1,000 milliseconds, then slide it up over 800 milliseconds with a custom bezier dragged into an exponential curve. Why: These are the settings the presenter uses for the loading screen reveal. Values: 1,000 milliseconds, 800 milliseconds, custom bezier. [after a delay of 1,000 milliseconds we're going to navigate to our next frame it's going to take 800 milliseconds]
- **consider** (motion, all): Keep nav elements at zero fill (transparent) while the loading screen is up, then fade them to 100% opacity 100 milliseconds after it lifts, using ease in and out over 200 milliseconds. Why: Hiding them first lets them animate in after the reveal. Values: 100 milliseconds, 200 milliseconds, 100%, ease in and out. [set the fill to zero so we can animate them in later]
- **consider** (motion, all): Use a custom bezier with its handles dragged out (an exponential curve) for large movements such as the loading screen, the navbar expanding and the text wipe, and a plain ease in and out for the nav fades and the dot growing into a circle. [inferred] Why: The presenter picks the custom bezier for every big movement and ease in and out for the fades and the first small growth step; he does not state the reason. [inferred] Values: custom bezier, ease in and out. [we're going to use a custom bezier just drag out these handles]
- **consider** (tooling, all): To prototype a navbar that expands from a dot, work backwards: duplicate the finished frame, squeeze it to a circle whose width matches its height, then to a 1 by 1 pixel dot, then make the dot fully transparent. Why: He builds the frames backwards from the finished navbar; each duplicate becomes an earlier state for Smart Animate to move from [inferred]. Values: 53 pixels, 1 pixel by one pixel. [we're going to work backwards by duplicating this Frame]
- **consider** (motion, all): Start the expanding navbar with an 800 millisecond hold on a transparent dot, switch instantly to a visible 1 by 1 pixel dot, then expand in two animated steps: dot to circle with ease in and out over 300 milliseconds, then circle to full navbar with a custom exponential bezier over 400 milliseconds. Why: These are the presenter's settings; he says 300 milliseconds is probably fine for now. Values: 800 milliseconds, 300 milliseconds, 400 milliseconds, ease in and out, custom bezier. [300 milliseconds is probably fine for right now]
- **consider** (motion, all): After the navbar has expanded, fade its items in one after another (menu, then logo, then the join us button), each with Smart Animate, ease in and out and 200 milliseconds. Why: The items are made transparent in successive frames so they animate in after the container; all of these fades use the same settings. Values: 200 milliseconds, ease in and out. [we're going to animate in all of our elements in our navbar]
- **consider** (motion, all): For a text wipe, draw a bar one pixel wide and a little taller than the text, in the right colour. Start with the text and bar transparent, show the bar instantly after 800 milliseconds, animate the bar across the text with Smart Animate over 700 milliseconds and a custom exponential bezier, switch the text to opaque instantly, animate the bar back over 700 milliseconds, then make the bar transparent with a final instant step. Why: This is how the presenter builds the text wipe effect. Values: one pixel wide, 800 milliseconds, 700 milliseconds, custom bezier. [drawing one that is one pixel wide and as tall as our text in fact a little bit taller]
- **consider** (tooling, all): In a Figma prototype, chain animated frames with an after-delay trigger of 1 millisecond, and use instant navigation for frames that only swap what is visible; the 1 millisecond delay makes each step start right after the previous one [inferred]. Why: This is how the presenter links every step of the three animations into one sequence. Values: 1 millisecond. [after a delay of 1 millisecond we are going to use Smart animate]
- **consider** (motion, all): Build the loading screen as a rectangle covering the whole page, filled black, with the logo centred horizontally and vertically. Why: This is how the presenter sets up the loading screen that slides up to reveal the content. Values: black. [take this logo and put it in here and then Center it horizontally and vertically]

### Decisions it informs

- Which load animation should the website play when it first opens?
  - Loading screen slide-up: A black screen with the centred logo slides up and away, the page content rises with it, and the nav fades in after. When: Not stated in the source.
  - Expanding navbar: A tiny dot grows into a circle and then into the full navbar, and the menu, logo and join us button fade in one after another. When: Not stated in the source; it is the presenter's favourite of the three.
  - Text wipe: A thin coloured bar is animated across a line of text, the text becomes visible, and the bar then moves off and disappears. When: Not stated in the source.
- Which easing should each step of a load animation use?
  - Ease in and out: Used for the nav fade after the loading screen and the navbar item fades (200 milliseconds) and the dot-to-circle step (300 milliseconds). When: Fades and the first small growth step in the source's examples.
  - Custom bezier (exponential): Handles dragged out for more of an exponential curve, used for the loading screen slide (800 milliseconds), the navbar expansion (400 milliseconds) and the text wipe (700 milliseconds). When: Larger movements in the source's examples.

### Process

1. Set up the loading screen: Duplicate the page frame, draw a rectangle over the whole screen, fill it black and centre the logo horizontally and vertically.
2. Prepare the hidden and offset states: Hide the loading screen for a moment, set both nav elements' fill to zero, slide the other content down slightly, then unhide the loading screen.
3. Make the end frames: Duplicate the frame and slide the loading screen all the way up and the content up to its centred position; duplicate again and set the nav opacity to 100%.
4. Prototype the loading screen: In prototyping mode, link the first frame to the next after a delay of 1,000 milliseconds, 800 milliseconds long with a custom bezier; link to the nav fade after 100 milliseconds with Smart Animate, ease in and out, 200 milliseconds.
5. Build the expanding navbar frames backwards: Duplicate the finished frame and make its items transparent; duplicate and squeeze the navbar to 53 by 53 pixels; duplicate and squeeze to 1 pixel by 1 pixel; duplicate and make the dot fully transparent; then add frames where the menu, then the logo, then the join us button become opaque.
6. Prototype the expanding navbar: From the first frame, wait 800 milliseconds and navigate instantly; Smart Animate the circle in after 1 millisecond with ease in and out over 300 milliseconds; expand with a custom exponential bezier over 400 milliseconds; fade each navbar item in after 1 millisecond with ease in and out over 200 milliseconds.
7. Build the text wipe frames: Draw a rectangle one pixel wide and a little taller than the text in the right colour. Make frames: text transparent with the bar visible; text and bar both transparent (the starting frame); the bar dragged all the way across with the text transparent; the same with the text opaque; the bar dragged back to this side; the bar transparent.
8. Prototype the text wipe: Set the first frame as the starting point; after 800 milliseconds navigate instantly; Smart Animate after 1 millisecond over 700 milliseconds with a custom exponential bezier; switch instantly; Smart Animate again for 700 milliseconds; finish with an instant move.
9. Preview the flow: Select the first frame, use the flow starting point, and press play to check the sequence.

### Examples and visual references

- Loading screen reveal (Presenter's demo website in a free Figma file): A black full-screen cover with a centred logo slides up to reveal the page; the page content rises slightly with it and then the nav fades in.
- Expanding navbar (Presenter's demo website in a free Figma file): A transparent dot grows to a 53 by 53 pixel circle and then stretches into the full navbar; the menu, logo and join us button then fade in one by one.
- Text wipe (Presenter's demo website in a free Figma file): A one pixel wide coloured bar, slightly taller than the text, is animated across it; the text becomes visible between the bar's moves, and the bar finally disappears.

### Numbers

- 1,000 milliseconds: Delay before the loading screen starts to slide up. [after a delay of 1,000 milliseconds]
- 800 milliseconds: Duration of the loading screen slide with a custom bezier; also the delay before the navbar and text wipe sequences start. [it's going to take 800 milliseconds]
- 100 milliseconds: Delay before the nav fades in after the loading screen. [after a delay of 100 milliseconds we are going to Smart animate]
- 200 milliseconds: Ease in and out duration for the nav fade and for each navbar item fade. [ease in and out with 200 milliseconds]
- 53 pixels: Navbar height; the intermediate circle is squeezed to 53 by 53 pixels. [we have a height of 53 pixels]
- 1 pixel by one pixel: Size of the starting dot for the expanding navbar. [squeeze this down until it is 1 pixel by one pixel]
- 1 millisecond: After-delay used to chain Smart Animate steps back to back. [after a delay of 1 millisecond]
- 300 milliseconds: Ease in and out duration for the dot growing into a circle. [300 milliseconds is probably fine for right now]
- 400 milliseconds: Custom bezier duration for the circle expanding into the navbar. [we're also going to set this to 400 milliseconds]
- 700 milliseconds: Custom bezier duration for each pass of the text wipe bar. [we're going to do 700 milliseconds here]
- one pixel wide: Width of the bar drawn for the text wipe, which is a little taller than the text. [drawing one that is one pixel wide]
- 100%: Opacity the nav content is set to in the final loading screen frame. [unhide it by turning the opacity to 100%]

<!-- /od:learn -->
