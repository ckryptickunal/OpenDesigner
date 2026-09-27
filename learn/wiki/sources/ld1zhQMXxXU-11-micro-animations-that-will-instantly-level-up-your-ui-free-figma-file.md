---
type: source
title: 11 Micro Animations That Will Instantly Level Up Your UI (free figma file)
created: 2026-09-27
updated: 2026-09-27
video_id: ld1zhQMXxXU
url: https://www.youtube.com/watch?v=ld1zhQMXxXU
channel: Kole Jain
published: 2025-04-29T19:17:58Z
authority: reference
tags:
  - micro-interactions
  - hover-states
  - pressed-state
  - tooltips
  - toasts
  - spring-easing
  - smart-animate
  - figma-prototyping
  - card-stack
  - search-expansion
  - progress-bar
  - upgrade-prompt
---

# 11 Micro Animations That Will Instantly Level Up Your UI (free figma file)

## Metadata

- Video ID: `ld1zhQMXxXU`
- Channel: Kole Jain
- Published: 2025-04-29T19:17:58Z
- URL: https://www.youtube.com/watch?v=ld1zhQMXxXU

## Summary

Kole Jain walks through 11 small interface animations and shows how to prototype each one in Figma: a button hover where the text slides up and the button shrinks on press, an animated keyboard-shortcut hint, richer toasts, a name tag that pops up over a headshot, a shimmering gradient stroke, icon tooltips that appear after a second, text that pops out images on hover, a form progress bar that draws itself in, a swipeable card stack, a search icon that expands into a search bar, and a hover that reveals upgrade limits. Most are tied to a real product (Rainbow Wallet, Vercel, Linear, Huddle, Obsidian, Figma's community page, Dub, Apple), and many come with a UX reason, such as keeping shortcuts memorable, explaining unlabeled icons, keeping people engaged in forms or saving space. The only timing and easing values spoken are the name tag's custom spring (500 milliseconds, stiffness 636, dampening 24) and the tooltip's one-second hover delay. For a design system, it offers a catalogue of micro-interaction patterns for states, tooltips, toasts, stacks and search, and a reminder that, for the name tag, the custom easing is what creates the difference between two versions of the animation.

## Key Ideas

- Hover and pressed states can use motion (text sliding up in a mask, the button shrinking while pressed) instead of last-minute color changes.
- A small animation that shows a keyboard shortcut makes the shortcut harder to forget.
- Toasts can do more than slide up: loading animations and celebratory success messages with particles.
- A small headshot can pop up a name tag on hover, and the custom spring easing is what creates the difference between two versions of that animation.
- A shimmering gradient stroke is a modern effect, but its uneven speed (faster on the edges than on the top and bottom) might bother some people, so the creator added a pause and play toggle.
- Tooltips that appear only after hovering an icon for a full second explain icons when there is no room to label them.
- Hovering text can pop out images that show what the text means, without more words or permanent images.
- Forms are boring, so a smooth progress bar animation helps keep people engaged.
- In a swipeable card stack, the cards behind must move forward to fill the gap while the top card is dragged, or the effect feels incomplete.
- Search bars are large and clunky, so collapse them into the magnifying-glass icon and animate the expansion on click.
- Upgrade prompts can reveal the higher plan's limits on hover with a slide-in instead of crossed-out text.
- All of these can be prototyped in Figma with hover, click, while-pressing, mouse-enter, mouse-leave and delay triggers plus Smart Animate and custom easing.

## Entities

- [[entities/kole-jain|Kole Jain]] (person): YouTube designer who presents the 11 micro-animations and their Figma builds.
- [[entities/figma|Figma]] (tool): Where every animation is prototyped, using masks, auto layout, Smart Animate, triggers, delays and custom easing.
- [[entities/smart-animate|Smart Animate]] (concept): Figma prototype animation used with a custom spring to pop up the name tag on hover.
- [[entities/rainbow-wallet|Rainbow Wallet]] (product): Source of the animated keyboard-shortcut hint.
- [[entities/vercel|Vercel]] (company): Named for having pretty good toast notifications (caption spells it 'Versel').
- [[entities/linear|Linear]] (product): Toasts the creator prefers over Vercel's, and a smooth form progress bar that keeps users engaged.
- [[entities/huddle|Huddle]] (product): Example of a name tag that pops up when hovering a headshot.
- [[entities/microinteraction-co|microinteraction.co]] (product): Site cited as doing the shimmer (gradient) stroke well.
- [[entities/wix|Wix]] (company): A Wix site is cited as doing the shimmer stroke well.
- [[entities/obsidian|Obsidian]] (product): Note-taking app whose icons show an explanatory popup after more than a second of hover.
- [[entities/ace-studio|Ace Studio]] (company): Does text hover pop-outs similar to Figma's, with more playful images.
- [[entities/dub|Dub]] (product): dub.co; source of the swipeable card stack in its sidebar and the hover-for-upgrade-details interaction.
- [[entities/apple|Apple]] (company): Cited for a good search-icon-to-search-bar interaction.
- [[entities/webflow|Webflow]] (tool): A micro-interaction library built for Webflow shows horizontal and diagonal text hover movement.
- [[entities/imessage|iMessage]] (product): Its images are what the Dub card stack reminds the creator of.
- [[entities/newform-community|Newform community]] (company): The creator's design community ('14k designers'), promoted in the description (self-promotion).

## Topics

- [[topics/micro-interactions|Micro-interactions]]: A catalogue of 11 micro-animations (button hover, shortcut hint, toasts, name tag, shimmer stroke, delayed tooltip, text pop-out, progress bar, card swipe, search expansion, upgrade hover), most with a UX reason, each with a Figma build.
- [[topics/buttons-and-actions|Buttons and actions]]: Instead of picking random hover and click colors at the last minute, slide the label up inside a mask on hover and shrink the button while it is pressed; horizontal or diagonal text movement is a variation.
- [[topics/toasts-and-notifications|Toasts and notifications]]: Beyond the obvious slide-up, toasts can carry loading animations and celebratory success messages with particles; Vercel's are good and Linear's are preferred. A swipeable card stack can act as a notification center in the bottom right.
- [[topics/spring-animation|Spring animation]]: The name tag pop-up uses a custom spring of 500 milliseconds, stiffness 636 and dampening 24, which the creator says is what creates the difference between two versions of the animation; the tooltip also gets a custom easing with more bounce.
- [[topics/easing-and-timing|Easing and timing]]: Tooltips appear only after a full second of hover; the search expansion uses a little delay between frames; toasts are built from simple delay triggers.
- [[topics/modals-and-popovers|Modals and popovers]]: Delayed tooltips pop up to explain what an icon does, only after the pointer rests on it for a full second, and hide on mouse leave.
- [[topics/icons-and-imagery|Icons and imagery]]: Delayed tooltips suit interfaces with many icons and little room for labels; the magnifying glass is the universally accepted search icon; text hover can pop out images instead of showing images permanently.
- [[topics/gestures-and-drag|Gestures and drag]]: A dragged card rotates out and fades to 0% opacity while the cards behind scale up and shift down to fill its place, which makes the stack feel like it moves forward.
- [[topics/forms-and-inputs|Forms and inputs]]: Forms are boring but sometimes unavoidable; a smooth progress bar animation (as in Linear) keeps users engaged.
- [[topics/paywalls-and-pricing-pages|Paywalls and pricing pages]]: Hovering an upgrade prompt can reveal the Pro plan's limits; the creator uses a slide-in effect where the 20 disappears, instead of Dub's crossed-out text.
- [[topics/prototyping|Prototyping]]: Step-by-step Figma prototype recipes for each animation: masks, subtract shapes, angular gradients, mouse enter and leave triggers, while-pressing, delays and Smart Animate.
- [[topics/figma-and-design-tools|Figma and design tools]]: Figma prototypes cannot bind the Command or Shift key, so X and A were used as stand-ins for the shortcut demo; auto layout is added with Shift A.

## Notable Claims

- Using motion for hover and click states means you don't have to mess around with different colors. Evidence: Simple button hover effect
- Keyboard shortcuts are easy to forget, and a small animation like Rainbow Wallet's makes them harder to forget. Evidence: Two, keyboard shortcuts
- Figma prototypes cannot bind the Command or Shift key. Evidence: it's not possible to bind the command or shift key
- The custom easing (500 milliseconds, stiffness 636, dampening 24) is what creates the difference between the two name tag animations. Evidence: This is important and creates the difference
- Animating a rotating angular gradient inside a masked stroke makes the shimmer move faster on the edges than on the top and bottom. Evidence: Five, shimmer stroke
- Delayed tooltips are helpful when there are a lot of icons but not a lot of space to label them. Evidence: delayed tool tips
- Text hover pop-outs show what you are talking about without writing more words or taking up space with images. Evidence: Seven text hover pop out
- Linear uses smooth micro-interactions on its progress bar to keep users engaged in forms. Evidence: Eight. Progress bar
- Having the other cards move down to fill the space while the top card is dragged is what completes the card swipe effect. Evidence: One important detail is to make sure
- Search bars are large and clunky and can get in the way, and the magnifying glass is the universally accepted search icon. Evidence: Search bar expansion
- Toast notifications are very important for UX. Evidence: something very important for UX
- The shimmer (gradient) stroke is a really modern animation. Evidence: is a really modern animation
- Delayed tooltips are both a micro-interaction and a massively helpful UX tip. Evidence: a massively helpful UX tip

## Quotes

> This is important and creates the difference between these two animations.
> That's what really completes this effect and makes it feel like they're moving forward.
> Very simple interaction, but definitely a thoughtful one.

<!-- od:learn -->

## For OpenDesigner

- Authority: **reference**
- Caveat: Self-promotion: a free Figma file on the creator's site and a design community ('14k designers') in the description, plus a subscribe request; excluded from rules.
- Caveat: Everything is built as a Figma prototype (Smart Animate, triggers, delays), not code; the spring values are Figma easing settings and the source gives no CSS or code equivalents.
- Caveat: Only the name tag spring (500 milliseconds, stiffness 636, dampening 24) and the one-second tooltip delay are spoken as timing values; the tooltip's bounce settings ('these settings'), the toast delays and the other curves are not spoken.
- Caveat: Auto-caption errors: 'Versel' is Vercel, 'linears' is Linear's, 'headsh shot' is headshot, 'Web Flow' is Webflow, and the tooltip delay is captioned 'th00and millisecond delay' (the surrounding text says a full second).
- Caveat: The statement that Figma prototypes cannot bind the Command or Shift key reflects Figma as of the video's date (2025-04-29) and may be out of date [inferred].
- Caveat: Several choices are personal taste: the text pop-out is the creator's favorite, he dislikes Dub's crossed-out text, and he prefers Linear's toasts to Vercel's.
- Caveat: The description's timestamp list is cut off after 3:22, and the intro refers to on-screen visuals not described in the transcript.

### Rules and practices

- **consider** (components, all): Design the hover and pressed states together with the button, using motion: slide the label up inside a mask on hover and make the button smaller while it is pressed. Why: Hover and click states are easy to forget until the end, which leads to frantically picking random colors; motion avoids messing around with different colors. [Simple button hover effect]
- **consider** (patterns, web): When a site shows small headshots, pop up a small name tag when the user hovers on one. Why: The source gives examples rather than a reason: Huddle has this effect, and typically so do agencies with teams of creatives. [Name tag on hover]
- **should** (motion, all): Animate a hover pop-up like the name tag from slightly lower at opacity zero, using Smart Animate with a custom spring rather than the default easing. Why: The custom easing is important and is what creates the difference between the two versions of the animation. Values: 500 milliseconds, stiffness of 636, dampening of 24, opacity to zero. [some custom easing that takes 500 milliseconds]
- **consider** (motion, all): Give a looping shimmer (gradient) stroke a pause and play control so the user can toggle it. Why: The rotating gradient moves faster on the edges than on the top and bottom, which some people might mind. [we added in a pause and play button]
- **should** (components, desktop): Explain icon-only controls with a tooltip that appears only after the pointer rests on the icon for a full second, and return to the original state on mouse leave. Why: It is really nice when you have a lot of icons but not a lot of space to label them all; with the delay, the popup only appears if the pointer stays on the icon for a full second. Values: a full second. [delayed tool tips]
- **consider** (motion, all): Give the delayed tooltip pop-up a custom easing with a bit more bounce. Why: No reason beyond the feel is given: the creator used custom easing settings to get a bit more bounce on the tooltip. [a custom easing with these settings to get a bit more bounce]
- **consider** (patterns, web): On hover over key words, pop out images or elements that show what the text is talking about. Why: It shows what you mean without writing more words or taking up more space with images. [Seven text hover pop out]
- **consider** (components, all): Animate a form's progress bar smoothly, drawing the stroke in and fading elements in and out as the user advances. Why: Forms are boring but sometimes unavoidable, and smooth micro-interactions on the progress bar keep the user engaged (as in Linear). [Eight. Progress bar]
- **should** (motion, all): In a swipeable card stack, while the top card is dragged away, move the cards behind down and scale them up to fill its place. Why: That detail completes the effect and makes the stack feel like it is moving forward. [One important detail is to make sure]
- **consider** (motion, all): Dismiss a swiped card by rotating it out of the way and setting its opacity to 0%. Why: This is how the card swipe is built, with the cards behind scaling up and shifting down. Values: 0%. [rotating the card out of the way and setting the opacity to 0%]
- **consider** (components, all): Collapse a search bar into the magnifying-glass icon and animate it expanding into the full bar on click. Why: Search bars are large, clunky and can get in the way; collapsing them creates an opportunity for an interaction when the user clicks. [Search bar expansion]
- **consider** (patterns, web): On an upgrade prompt, show the higher plan's limits on hover with a slide-in effect (where the 20 disappears) rather than crossed-out text. Why: The creator is not a big fan of the crossed-out text in Dub's version and calls the slide-in a very simple but thoughtful interaction. [Hover for upgrade details]
- **consider** (patterns, desktop): Give keyboard shortcuts a small micro-animation, like Rainbow Wallet's; in the Figma version, pressing the keys together shows a success message. Why: Keyboard shortcuts are really easy to forget, and an animation makes them harder to forget. [Two, keyboard shortcuts]
- **consider** (components, all): Make toasts more than a slide-up: add simple loading animations and celebratory success messages, optionally with particle animations. Why: The creator says we can do better than Vercel's and Linear's toasts by adding interactive bits to the cards. [Three, toast notifications]

### Decisions it informs

- How should buttons show hover and pressed states? (`Q-state-04`)
  - Color changes: Different colors for hover and click; when left to the end, this means frantically picking random colors. When: Not recommended by the source when done as an afterthought.
  - Label slides up, button shrinks on press: The text slides up out of a mask and a second copy slides in on hover; the button gets smaller while pressed. When: The creator's recommended default; avoids messing around with colors.
  - Horizontal or diagonal label movement: The same masked-text idea, but the text moves sideways or diagonally. When: A variation to mix it up, as in a micro-interaction library built for Webflow.
  - Recommendation: Use motion (text sliding up in a mask on hover, button shrinking while pressed) so you don't have to mess around with different colors.
- How should icon-only controls explain what they do? (`Q-icon-05`)
  - Label every icon: Each icon has visible text, which takes space. When: When there is room to label them [inferred].
  - Delayed tooltip: A popup explains the icon only after the pointer rests on it for a full second. When: When there are a lot of icons but not a lot of space to label them all.
  - Recommendation: Use a tooltip delayed by a full second when icons are many and space is tight, as Obsidian does.
- Should search be a full bar or collapsed into an icon?
  - Always-visible search bar: Large, clunky and can get in the way. When: Not stated in the source.
  - Magnifying-glass icon that expands: Search is packed into the universally accepted icon; clicking it animates into the bar, with the glass disappearing into the circle. When: When the bar would get in the way.
  - Recommendation: Collapse into the magnifying glass and animate the expansion on click, as Apple does.
- How should an upgrade prompt show what the higher plan unlocks?
  - Crossed-out text: On hover, the Pro plan's limits show, with text crossed out (Dub). When: Not recommended by the creator.
  - Slide-in replacement: On hover, a slide-in effect is used instead of the cross-out, and the 20 disappears. When: The creator's preferred version.
  - Recommendation: Use the slide-in; the creator is not a big fan of crossed-out text.
- Should a looping decorative animation run nonstop or be user-controllable?
  - Always running: The shimmer keeps rotating; it moves faster on the edges than the top and bottom. When: If the uneven speed is acceptable; the creator personally doesn't mind it.
  - With a pause and play toggle: The user can stop and start the shimmer whenever they like. When: Because some people might mind the effect.
  - Recommendation: Add a pause and play button so the user can toggle it.
- How much should a toast animate?
  - Slide up only: The obvious animation of the toast sliding up. When: The baseline most products use.
  - Interactive toast: Loading animations while waiting and celebratory success messages with particle animations. When: When you want to do better than the baseline.
  - Recommendation: Add interactive bits such as loading animations and celebratory success messages.
- How should a hover pop-up like the name tag be eased? (`Q-motion-04`)
  - Without the custom easing [inferred]: The other of the two animations the creator compares; the source does not say which settings it uses [inferred]. When: Not recommended by the source.
  - Custom spring: Smart Animate with a custom easing that takes 500 milliseconds, with a stiffness of 636 and a dampening of 24. When: The creator's choice; he says this is important and creates the difference between the two animations.
  - Recommendation: Use the custom spring (500 milliseconds, stiffness 636, dampening 24) for the name tag pop-up.
- Where should a swipeable card stack live?
  - In the sidebar: The stack sits in the sidebar, as dub.co has it. When: The creator likes this placement.
  - Bottom right, as a notification center: The stack sits in the bottom right and acts as a notification center. When: The creator's choice for his version.
  - Recommendation: The creator puts his in the bottom right as a kind of notification center, while saying he likes dub.co's sidebar placement.

### Process

1. Button text slide-up in Figma: Put two copies of the label inside a mask, add a hover effect that slides them up, and add a while-pressing effect for the click that makes the button smaller.
2. Name tag on hover in Figma: Make two frames. Build the tag with auto layout (Shift A), fully rounded corners, slightly adjusted spacing, a black fill, white text and a little tilt. In the first frame put the same tag moved down a little at opacity zero. Connect them with a hover trigger, Smart Animate and a custom easing of 500 milliseconds, stiffness 636 and dampening 24.
3. Shimmer stroke in Figma: Create the stroke outline by subtracting one rectangle from another, create an angular gradient on a circle, mask the two together so only the stroke shows the gradient, then animate the gradient rotating.
4. Delayed tooltip in Figma: Add a mouse-enter trigger with a delay of a full second to show the tooltip, a mouse-leave trigger to return to the original frame, and a custom easing with more bounce.
5. Toast in Figma: Chain simple delay triggers with a single click trigger to move through loading and success states.
6. Text hover pop-out in Figma: Add hover interactions to the frames so the related elements pop out when the text is hovered.
7. Progress bar in Figma: Mask the stroke to a purple rectangle and slide the rectangle along so the stroke looks like it is being drawn in, including around the circles; fade the other elements in or out.
8. Card swipe stack in Figma: Stack the cards on top of each other; animate the top card rotating out of the way to 0% opacity while the cards behind scale up and shift down, and make sure they move down to fill the space while the top card is being dragged.
9. Search expansion in Figma: Use three frames: a click interaction on the first, then a little delay that takes you to the last; the magnifying glass disappears into the circle.
10. Upgrade hover in Figma: On hover, use a slide-in effect instead of the cross-out and make the 20 disappear.
11. Keyboard shortcut hint in Figma: Bind the shortcut keys to the prototype (X and A stood in for Command and Shift, which Figma cannot bind) so pressing them all at once shows a success message.

### Examples and visual references

- Button with sliding text and press shrink (An unnamed agency site): The label slides up on hover and the button gets smaller when clicked.
- Horizontal and diagonal text hover (A micro-interaction library built for Webflow): Button text moves sideways or diagonally instead of straight up.
- Animated keyboard shortcut hint (Rainbow Wallet): A small animation of the shortcut keys; in the Figma version, pressing them together shows a success message.
- Toast notifications (Vercel and Linear): Toasts slide up; the creator's version adds loading animations and celebratory success messages with particles.
- Name tag on a headshot (Huddle and agency team pages): In the creator's Figma build, a black, fully rounded, slightly tilted tag with white text pops up from slightly below when a small headshot is hovered.
- Shimmer (gradient) stroke (microinteraction.co and a Wix site): A gradient travels around a button's outline; in the Figma build it moves faster on the edges than on the top and bottom, with a pause and play button.
- Delayed icon tooltip (Obsidian): Hovering an icon for more than a second shows a popup explaining what it does.
- Text hover pop-out (Figma's community page and Ace Studio): Hovering words pops out images that show what the text refers to; Ace Studio's images are more playful.
- Form progress bar (Linear): In the creator's Figma rebuild, the stroke draws itself in, including around the circles, while other elements fade in or out.
- Swipeable card stack (dub.co (in its sidebar); the creator places it bottom right as a notification center): Stacked cards that remind the creator of iMessage images; in his build the top card rotates away to 0% opacity while the ones behind scale up and shift down.
- Search icon expanding into a bar (Apple (the creator's Figma version is what is described)): In the Figma version, clicking the magnifying glass expands the search, and the glass disappears into the circle.
- Hover for upgrade details (Dub): Hovering shows the Pro plan's limits; Dub shows crossed-out text, while the creator's version uses a slide-in and the 20 disappears.

### Numbers

- 11: Micro-animations covered in the video. [11 Micro Animations That Will Instantly Level Up Your UI]
- 500 milliseconds: Duration of the custom easing on the name tag hover animation. [custom easing that takes 500 milliseconds]
- 636: Stiffness of the name tag's custom spring easing. [has a stiffness of 636]
- 24: Dampening of the name tag's custom spring easing. [a dampening of 24]
- a full second: How long the pointer must rest on an icon before the tooltip appears. [only if we hover on it for a full second]
- 0%: Opacity of the top card once it is swiped away. [setting the opacity to 0%]
- three frames: Frames used for the search bar expansion prototype. [It's just three frames with a click interaction]
- 20: The number that disappears in the creator's upgrade-hover version. [the 20 disappears]

<!-- /od:learn -->
