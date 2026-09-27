---
type: source
title: Animated Dashboard Sidebar Tutorial in Figma (+ free design files)
created: 2026-09-27
updated: 2026-09-27
video_id: NtZeYmTMuo4
url: https://www.youtube.com/watch?v=NtZeYmTMuo4
channel: Kole Jain
published: 2025-04-11T04:01:39Z
authority: reference
tags:
  - sidebar
  - dashboard
  - figma
  - prototyping
  - smart-animate
  - hover-states
  - focus-state
  - loading-spinner
  - spring
  - shadows
  - outlines
  - micro-interactions
---

# Animated Dashboard Sidebar Tutorial in Figma (+ free design files)

## Metadata

- Video ID: `NtZeYmTMuo4`
- Channel: Kole Jain
- Published: 2025-04-11T04:01:39Z
- URL: https://www.youtube.com/watch?v=NtZeYmTMuo4

## Summary

Kole Jain builds an animated dashboard sidebar in Figma with no code, splitting the work into the sidebar itself (text, dividers and icons) and the cards that pop up as you move through a flow. He points out two visual details: a very subtle outline around the cards and almost every element, which lets the palette stay mostly pure white or near white, and a very subtle drop shadow on pop-ups that uses a light gray instead of transparent black. The rest of the video is a frame-by-frame prototyping recipe: hover rectangles and menus toggled with layer opacity, Smart Animate transitions on hover and click, a menu that slides up because its hidden state sits a few pixels lower, a rectangle that morphs into a search bar because both layers share a name, a yellow-stroke focus state with a blurred background copy, a spinning loader built from rotated frames on a 300 millisecond delay with a custom spring, and a check mark that slides in through a mask. For a design system it is a compact set of hover, focus, loading and success state patterns and shows how named layers drive Figma motion [inferred].

## Key Ideas

- A sidebar can be just a handful of text, some dividers and icons; the icons are called the secret to a great sidebar.
- A very subtle outline around cards and nearly every element lets the color guide stay compact, mostly pure white or near white.
- The pop-up drop shadow is very subtle and uses a very light gray rather than a transparent black.
- In Figma, show and hide elements with the layer opacity, not the fill opacity.
- Hover effects use the 'while hovering' trigger; opening menus and pop-ups uses 'on click'; both use Smart Animate.
- Placing a hidden menu a couple of pixels lower turns a plain fade into a slide-up reveal.
- Smart Animate pairs layers by name: same name means one element that moves or morphs, different names mean a cross-fade.
- Giving a card rectangle and a search bar the same layer name makes the rectangle slide up and become the search bar.
- Hover labels start slid down and fully transparent, and the icon's background tile turns ever so slightly off-white on hover.
- A focus or selected state can be a bright yellow stroke plus a blurred duplicate of the shape behind it.
- A loading spinner can be faked with frames whose icon alternates between unrotated and rotated 180°, chained on a 300 millisecond delay with a custom spring.
- The custom spring is used only for the spinner; the final success step goes back to a regular ease out.
- The creator prefers the success check mark to slide in through a mask rather than just fade in.

## Entities

- [[entities/kole-jain|Kole Jain]] (person): Channel host presenting the sidebar tutorial and offering the free Figma file.
- [[entities/figma|Figma]] (tool): The design tool used to build and prototype the sidebar with no code.
- [[entities/smart-animate|Smart Animate]] (concept): Figma's prototype animation that matches layers by name between frames and animates them.
- [[entities/notion|Notion]] (product): Used as the example integration whose icon gets a hover label, focus state and connect flow.
- [[entities/newform|Newform]] (company): Kole Jain's design community (newform.community), promoted in the video description.

## Topics

- [[topics/navigation-and-sidebars|Navigation and sidebars]]: A dashboard sidebar built from text, dividers and icons, with hover highlights and an options menu that slides up on click.
- [[topics/dashboards-and-data-display|Dashboards and data display]]: The sidebar sits in a dashboard whose integration cards pop up and change as the user moves through a connect flow.
- [[topics/depth-shadows-and-borders|Depth, shadows and borders]]: Very subtle outlines on cards and nearly every element, plus a very subtle light-gray (not transparent black) drop shadow on pop-ups.
- [[topics/color|Color]]: The outlines allow a compact color guide where most colors are pure white or very close to white.
- [[topics/icons-and-imagery|Icons and imagery]]: Icons are called the secret to a great sidebar; integration icons get hover labels and state changes.
- [[topics/micro-interactions|Micro-interactions]]: Hover rectangles, slide-up menus, icon hover labels, a link icon that appears on hover, a spinner and a check mark that slides in.
- [[topics/prototyping|Prototyping]]: Step-by-step Figma prototype: duplicated frames, opacity toggles, while-hovering and on-click triggers, after-delay chains and Smart Animate.
- [[topics/figma-and-design-tools|Figma and design tools]]: Explains how Smart Animate matches layer names, using layer opacity instead of fill opacity, masks for slide-ins, and Figma's custom spring settings.
- [[topics/easing-and-timing|Easing and timing]]: Uses a 300 millisecond after-delay between frames and a regular ease out for the final success transition.
- [[topics/spring-animation|Spring animation]]: A custom spring with stiffness 550, damping 40 and default mass drives the loading spinner, the only custom spring in the flow.
- [[topics/feedback-empty-and-loading-states|Feedback, empty and loading states]]: Shows a focus state, a loading dialogue with a spinning icon and a success state with a check mark.

## Notable Claims

- The design breaks down into two major steps: the sidebar and the cards that pop up as you move through the flow. Evidence: broken down into two major steps
- Icons are the secret to a great sidebar. Evidence: a bunch of icons which really are the secret to a great sidebar
- A very subtle outline around the cards and other elements allows a compact color guide with most colors pure white or close to white. Evidence: very subtle outline around it and basically everything else on here
- The pop-up drop shadow uses a very light gray instead of a transparent black. Evidence: not using a transparent black, but instead a very light gray
- Figma Smart Animate searches the old and new frame for matching layer names; matching names are animated as the same element, different names fade out and in. Evidence: because of how Figma Smart Animate works
- Sliding the transparent menu down a couple of pixels produces a slide-up animation when it appears. Evidence: just give it a couple of pixels
- Frames with the icon alternately rotated 180 degrees, chained after a 300 millisecond delay with a custom spring, produce a spinning loading animation. Evidence: we get this awesome spinning loading animation
- Masking the check mark lets it slide in instead of just fading in. Evidence: I want this check mark to slide in instead of just fading in
- The whole interactive sidebar is built in Figma with zero code. Evidence: absolutely no code; Zero code, super easy to put together

## Quotes

> a bunch of icons which really are the secret to a great sidebar
> Notice how we're not using a transparent black, but instead a very light gray.
> Figma searches the old frame and new frame for matching layer names.

<!-- od:learn -->

## For OpenDesigner

- Authority: **reference**
- Caveat: Self-promotion: the description and outro push a free Figma file on kolejain.com, and the description promotes the creator's design community (13k+ designers).
- Caveat: Figma-specific tutorial from April 2025; menu locations (prototyping mode in the top right, use as mask, K to scale) may have changed since [inferred].
- Caveat: The shadow settings and style guide values are shown on screen but not spoken, so no exact shadow or color values are in the transcript.
- Caveat: The 'little bit of extra time' on the search-bar transition is not quantified.
- Caveat: Auto-caption issues: 'finger file' means Figma file; 'dampening' is taken to be Figma's spring damping setting [inferred]; 'change the weight to be darker' is unclear and may mean a heavier stroke weight [inferred].
- Caveat: The bright yellow focus stroke is the creator's styling for a prototype; the source says nothing about its contrast or keyboard accessibility [inferred].
- Caveat: The spring and delay values are Figma prototype settings, not code values [inferred].
- Caveat: The 'focus state' is a click-selected state in a prototype, not a keyboard focus indicator [inferred].

### Rules and practices

- **consider** (elevation, all): Put a very subtle outline around cards and most other elements so the palette can stay compact, with most colors pure white or very close to white. Why: The source says the outlines allow a pretty compact color guide. [very subtle outline around it and basically everything else on here]
- **consider** (elevation, all): Give pop-ups a very subtle drop shadow colored a very light gray, not a transparent black. Why: The source gives no reason; it only points the choice out ("Notice how") alongside a palette of mostly pure white and near white. [Notice how we're not using a transparent black, but instead a very light gray]
- **consider** (components, all): Build the sidebar from a handful of text, dividers and icons, and invest in the icons. Why: Icons are described as the secret to a great sidebar. [a bunch of icons which really are the secret to a great sidebar]
- **should** (tooling, all): In Figma prototypes, toggle visibility with the layer opacity control, not the fill opacity. Why: The source gives no reason; it tells you to use the layer-level opacity for everything in the animation instead of the fill's. Values: 0%, 100%. [Make sure to use the one up here for everything that we do instead of the one in the fill]
- **must** (tooling, all): Give a layer the exact same name in both frames when it should move or morph between them under Smart Animate. Why: Smart Animate treats layers with matching names as the same element and animates them; different names are treated as separate objects and cross-faded. [Figma searches the old frame and new frame for matching layer names]
- **consider** (tooling, all): Use the 'while hovering' trigger for hover effects and 'on click' for opening menus and pop-ups, both with Smart Animate. Why: These are the settings the source uses for the majority of the sidebar's animations; it describes them, it does not state them as a rule. Values: while hovering, on click, smart animate. [switching between while hovering and on click for the majority of our animations]
- **consider** (motion, all): Place a hidden menu a couple of pixels lower than its shown position so it slides up as it fades in. Why: It steps the reveal up a notch with a really nice slide-up animation; the exact distance does not matter much. Values: a couple of pixels. [slide it down. Doesn't matter too much how much we slide it down]
- **consider** (components, all): For an icon hover label, start the label slid down a touch and fully transparent, and make the icon's background tile ever so slightly off-white on hover. Why: It gives a very nice hover interaction; the source repeats it on every icon for a fully interactive feeling. [we get a very nice hover interaction whenever we hover on notion]
- **consider** (components, all): Show a focus (selected) state with a bright yellow stroke and a duplicate of the shape behind it with a layer blur of about 24 pixels. Why: The source calls the result a nice focus state on the selected integration tile. Values: 24 pixels. [layer blur and set that up to something like 24 pixels]
- **consider** (motion, all): For a hover reveal next to a label, start the icon overlapping the text, scaled down and at opacity 0, then move it beside the text and nudge the text over in the hover frame. Why: It produces the connect hover effect with the link icon. [scale down our link and turn the opacity to zero]
- **consider** (motion, all): Fake a loading spinner in Figma with a chain of frames whose icon alternates between unrotated and rotated 180°, each linked to the next by an on-delay trigger of 300 milliseconds and a custom spring with stiffness 550, damping (spoken as 'dampening') 40 and the mass left as it is. Why: Chaining the rotated frames gives a spinning loading animation with no code. Values: 180°, 300 milliseconds, 550, 40. [set the stiffness to 550 and set the dampening to 40 and leave the mass as it is]
- **consider** (motion, all): Keep the custom spring for the spinner only and use a regular ease out, after a 300 millisecond delay, for the success transition. Why: The spinner is described as the only time a custom spring is created; the success step sets the curve back to the regular ease out. Values: 300 milliseconds, ease out. [set our curve back to the regular ease out]
- **consider** (motion, all): Slide a success check mark in through a mask the same size and corner radius as its container, instead of only fading it in. Why: The creator wants the check mark to slide in rather than fade in; in the previous frame the check mark is nudged out of the masked shape so it is not visible. [I want this check mark to slide in instead of just fading in]
- **consider** (components, all): Give sidebar links and menu items a highlight rectangle behind the text that is at 0% layer opacity by default and 100% only while hovering. Why: The source wants the item rectangles to pop up only when they are hovered. Values: 0%, 100%. [we only want these rectangles to pop up when we're hovering on them]
- **consider** (motion, all): When a rectangle morphs into another element under Smart Animate, such as a card rectangle becoming the search bar, give that transition a little extra time. Why: The source adds it for the morph without saying why or how much. [add a little bit of extra time here]
- **consider** (components, all): Turn the focused tile into a success state by deleting the blurred background, changing the stroke from bright yellow to black and adding a check mark, keeping the icon's layer name identical so it animates. Why: These are the source's steps from the loading dialogue to the success state; it gives no further reason. [change the stroke of this from our bright yellow to a black]

### Decisions it informs

- How should cards and pop-ups stand out on a mostly white interface? (`Q-depth-01`)
  - Very subtle outline: Separates cards and basically every other element while most colors stay pure white or very close to white. When: Cards and most elements.
  - Outline plus a very subtle light-gray drop shadow: Adds a little lift to the pop-ups on top of the outline. When: Pop-ups.
  - Recommendation: Very subtle outlines on nearly everything, with a very subtle light-gray drop shadow on the pop-ups, as the source does.
- What color should the drop shadow under pop-ups be? (`Q-depth-03`)
  - Transparent black: The alternative the source contrasts with its own choice. When: Not recommended in this source.
  - Very light gray: A very subtle shadow that suits a palette of mostly pure white and near-white surfaces. When: Light, white-heavy dashboards with subtle outlines.
  - Recommendation: Very light gray, kept very subtle; the source points it out as the deliberate choice.
- Should two layers in consecutive frames animate as one element or cross-fade?
  - Same layer name: Smart Animate treats them as the same element and animates it, for example a rectangle sliding up to become the search bar. When: When one element should visibly move or transform into another.
  - Different layer names: Smart Animate treats them as separate objects: the first fades out and the second fades in. When: When elements are unrelated and a simple fade is fine.
  - Recommendation: Match the names when you want the morph; the source copies the rectangle's name onto the search bar for exactly that effect.
- How should a hidden options menu appear?
  - Opacity only: The menu fades in; already looking really good when previewed. When: A quick first pass.
  - Opacity plus a few pixels of offset: The menu fades in while sliding up a couple of pixels, a really nice slide-up animation. When: To step the interaction up a notch.
  - Recommendation: Add the few-pixel offset for the slide-up; the source says the distance does not matter much.
- Which prototype trigger should each interaction use?
  - While hovering: The change shows only while the pointer is over the element, for hover rectangles, icon labels and the link icon. When: Hover highlights and reveals.
  - On click: The change happens after a click, for the quick actions menu, the pop-up card, the focus state and the loading dialogue. When: Opening menus, pop-ups and moving through the flow.
  - After delay: The frame advances on its own after a set time, 300 milliseconds here, to chain spinner frames and reach the success state. When: Automatic sequences such as loading and success.
- Which curve should a prototype transition use?
  - Custom spring (stiffness 550, damping 40, default mass): Drives the chained rotated frames so the loading icon spins. When: The loading spinner, the only custom spring in the flow.
  - Regular ease out: The standard curve used for the success transition. When: Revealing the success state after loading.
  - Recommendation: Use the custom spring only for the spinner and return to ease out afterwards, as the source does.
- Should the success check mark fade in or slide in?
  - Fade in: The check mark simply appears by fading. When: When you could leave it at this.
  - Slide in through a mask: The check mark slides into the square, hidden by a mask of the same size and corner radius until it arrives. When: When you want the success moment to feel more deliberate [inferred].
  - Recommendation: Slide in; the creator wants the check mark to slide in instead of just fading in.

### Process

1. Split the design: Treat it as two parts: the sidebar (text, dividers, icons) and the cards that pop up as the user moves through the flow; use the attached style guide if designing from scratch.
2. Duplicate frames: Hold Option and drag a frame to duplicate it; each state of the animation is its own duplicated frame.
3. Add a hover highlight: Add a hover rectangle behind the text, set its layer opacity to 0 in the first frame and 100% in the next, then in prototyping mode drag a node from it to the next frame with 'while hovering' and Smart Animate.
4. Add the options menu: Paste the menu aligned to the right at 0% opacity, duplicate the frame and set the menu to 100% with its item rectangles at 0%, duplicate again with one item's rectangle at 100%; link quick actions 'on click' and each item rectangle 'while hovering'.
5. Make the menu slide up: In the frame where the menu is transparent, move it down a couple of pixels so it slides up as it appears; repeat the process three more times for the rest of the links, all with Smart Animate.
6. Morph a card into a search bar: Duplicate the frame, clear the card except its background, paste in the pop-up content and resize the card; copy the source rectangle's layer name onto the search bar so Smart Animate morphs one into the other, link 'on click' and add a little extra time.
7. Add icon hover labels: Add a label, duplicate the frame, slide the label down and make it fully transparent in the base frame, make the icon's background tile slightly off-white in the hover frame, and link with 'while hovering'; repeat for each icon.
8. Build the focus state: Duplicate, reset the label and background, paste the new content, give the icon rectangle a bright yellow stroke, duplicate it (Command or Control D) and add a layer blur of about 24 pixels to the bottom copy; link 'on click'.
9. Add the connect hover: In the hover frame place a link icon beside the Connect text and nudge the text over; in the previous frame place the link overlapping the text, scale it down with K and set opacity to zero; link with a hover interaction.
10. Build the loading spinner: Replace the requirements with a loading dialogue linked with a click trigger; duplicate the loading frame four times and rotate the icon 180° on the second and fourth frames; drag a node from each frame itself to the next with an on-delay trigger of 300 milliseconds and a custom spring of stiffness 550, damping 40 and the mass left as it is.
11. Build the success state: Duplicate, swap the loading text for success text, keep the icon's layer name identical so Smart Animate treats it as the same element, delete the blurred background, change the stroke from bright yellow to black and add a check mark.
12. Slide the check mark in with a mask: Draw a rectangle the exact same size and border radius as the square and drag it below the check mark, select all three and use as mask; paste the mask group into the previous frame and nudge the check mark and shape out of view; link the frames after a delay of 300 milliseconds with the curve set back to the regular ease out.

### Examples and visual references

- Professional dashboard sidebar (Kole Jain's free Figma file): A sidebar of text, dividers and icons next to cards; nearly everything has a very subtle outline and most colors are pure white or near white.
- Quick actions options menu: Clicking quick actions reveals a menu to the right that slides up a few pixels as it fades in; items highlight with a rectangle on hover.
- Card rectangle becoming a search bar: Because both layers share a name, a rectangle in the integrations card slides up and turns into the search bar instead of cross-fading.
- Integration icon hover label (Notion integration tile): Hovering the Notion icon slides a short description into view and tints the tile slightly off-white.
- Yellow focus state with blurred background (Notion integration tile): The selected tile gets a bright yellow stroke and a blurred duplicate behind it (layer blur around 24 pixels).
- Connect button hover: On hover a link icon grows in from where it overlapped the Connect text, scaled down and transparent, and the text shifts over to make room.
- Spinning loading dialogue: A loading dialogue whose icon appears to spin, made from frames alternating between unrotated and rotated 180°, chained every 300 milliseconds with a springy curve.
- Success state with sliding check mark: The blurred background is removed, the stroke turns black and a check mark slides into the square through a mask rather than fading in.

### Numbers

- 300 milliseconds: After-delay between spinner frames and before the success state [we will grab a delay of 300 milliseconds]
- 550: Custom spring stiffness for the loading spinner [set the stiffness to 550]
- 40: Custom spring damping for the loading spinner (mass left at default) [set the dampening to 40]
- 180°: Icon rotation on alternating spinner frames [set the rotation to 180°]
- 24 pixels: Layer blur on the duplicated shape that forms the focus glow [set that up to something like 24 pixels]
- four times: How many times the loading frame is duplicated [duplicate it four times]
- 0%: Layer opacity for hidden states (menus, highlight rectangles) [set the opacity on it to 0%]
- 100%: Layer opacity for shown states [set the opacity to 100%]
- three more times: How many more times the menu process is repeated for the rest of the sidebar links [repeat the process we went through three more times]

<!-- /od:learn -->
