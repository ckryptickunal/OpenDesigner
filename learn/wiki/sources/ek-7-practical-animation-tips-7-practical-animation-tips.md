---
type: source
title: 7 Practical Animation Tips
created: 2026-09-27
updated: 2026-09-27
video_id: ek-7-practical-animation-tips
url: https://emilkowal.ski/ui/7-practical-animation-tips
channel: Emil Kowalski (web)
published: Unknown
authority: non-negotiable
tags:
  - animation
  - motion
  - easing
  - ease-out
  - duration
  - press-feedback
  - scale
  - tooltips
  - popovers
  - transform-origin
  - perceived-performance
  - blur
---

# 7 Practical Animation Tips

## Metadata

- Page ID: `ek-7-practical-animation-tips`
- Publisher: Emil Kowalski (web)
- Published: Unknown
- URL: https://emilkowal.ski/ui/7-practical-animation-tips

## Summary

Emil Kowalski argues that good animation is not an innate art but a set of learnable tricks, and gives seven concrete ones. Buttons should scale down slightly when pressed, enter animations should not start from scale(0), and once one tooltip is open the next ones should open with no delay and no animation. Easing is the most important part of an animation: anything entering or exiting the screen should use ease-out, ideally a custom curve stronger than CSS's built-ins, and never ease-in. Popovers should scale in from their trigger, UI animations should stay fast (generally under 300ms) or be removed when seen tens or hundreds of times a day, and a little blur can hide a transition that still feels off. For a design system, these translate into motion tokens (durations, easing curves, starting scale), component behaviour (tooltip delay, origin-aware popovers, press feedback) and a polish checklist [inferred].

## Key Ideas

- The interface should feel like it is listening: every user action gets feedback as soon as possible.
- A subtle press scale (0.97) makes buttons feel instantly more responsive.
- Starting an animation from scale(0) looks like the element comes from nowhere; start at 0.9 or higher.
- Tooltips need an initial delay, but once one is open, neighbouring tooltips should open with no delay and no animation.
- Easing is the most important part of any animation; it can make a bad animation look great and a great one look bad.
- Use ease-out for anything entering or exiting the screen; ease-in starts slow and feels slower at the same duration.
- Built-in CSS easing curves are usually too weak; custom curves feel more energetic.
- Popovers should scale in from their trigger, so transform-origin must not be left at its default center.
- Unseen details compound: users may not consciously notice them, but in aggregate they make the product feel better.
- Fast animations improve perceived performance; keep UI animations under 300ms as a rule of thumb.
- Animations and hover effects seen tens or hundreds of times a day should be removed because they become annoying.
- When easing and duration tweaks still leave a transition feeling off, a small blur can bridge the old and new states.

## Entities

- [[entities/emil-kowalski|Emil Kowalski]] (person): Design engineer and author of the article
- [[entities/radix-ui|Radix UI]] (library): Unstyled component library cited for skipping subsequent tooltip delays and exposing a transform-origin CSS variable
- [[entities/base-ui|Base UI]] (library): Unstyled component library cited for skipping tooltip delay and animation (data-instant) and exposing --transform-origin
- [[entities/easings-co|easings.co]] (tool): Site the author recommends for custom variations of easing curves
- [[entities/paul-graham|Paul Graham]] (person): Quoted from Hackers and Painters on how unseen details combine into something stunning
- [[entities/hackers-and-painters|Hackers and Painters]] (product): Book by Paul Graham, source of the quote on unseen details
- [[entities/animations-dev|animations.dev]] (product): Emil Kowalski's animation course, which the article points to for deeper theory and practice
- [[entities/you-don-t-need-animations|You Don't Need Animations]] (product): Companion post by the author that covers when to remove animations in more detail
- [[entities/transform-origin|transform-origin]] (concept): CSS property that sets the point an element scales from; its default center is wrong for most popovers
- [[entities/ease-out|ease-out]] (concept): Easing that starts fast (accelerates at the beginning); the recommended curve for anything entering or exiting the screen
- [[entities/easing|Easing]] (concept): The rate at which something changes over a period of time; the author calls it the most important part of any animation
- [[entities/perceived-performance|Perceived performance]] (concept): How fast an interface feels, which fast animations and spinners improve without changing real load time
- [[entities/data-instant|data-instant]] (concept): Base UI attribute on subsequent tooltips that can be targeted to set transition duration to 0ms

## Topics

- [[topics/motion-principles|Motion principles]]: Seven practical tips: press feedback, no scale(0), instant subsequent tooltips, ease-out, origin-aware popovers, fast or no animation, and blur as a last resort.
- [[topics/easing-and-timing|Easing and timing]]: Easing is the most important part of an animation; use ease-out (preferably custom) for enter and exit, avoid ease-in, keep UI animations under 300ms, and 180ms feels more responsive than 400ms.
- [[topics/micro-interactions|Micro-interactions]]: Scale buttons to 0.97 on press, crossfade button states with 2px blur, and give every action immediate feedback such as loading and success states.
- [[topics/buttons-and-actions|Buttons and actions]]: Buttons should scale down subtly (0.97) on :active so the interface feels responsive; a button toggling between two states can crossfade with 2px blur.
- [[topics/modals-and-popovers|Modals and popovers]]: Popovers and dropdowns should scale in from their trigger using transform-origin; tooltips need an initial delay, then open instantly and without animation for neighbouring triggers.
- [[topics/feedback-empty-and-loading-states|Feedback, empty and loading states]]: Submitting a form should show a loading state and copy-to-clipboard should show a success state; a faster-spinning spinner makes loading feel faster.
- [[topics/animation-performance|Animation performance]]: Covers perceived performance only: faster spinners and shorter animations make the app feel faster without changing load time.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: CSS for tooltips with 0.125s ease-out transform and opacity, scale(0.97) start and end styles, data-instant set to 0ms, and library transform-origin variables.
- [[topics/ui-libraries|UI libraries]]: Radix UI and Base UI skip the delay for subsequent tooltips; Base UI can also skip the animation; both expose transform-origin CSS variables for origin-aware animation.
- [[topics/design-taste-and-judgement|Design taste and judgement]]: Animation skill is learnable, not magic; unseen details compound in aggregate even when users do not consciously notice them.

## Notable Claims

- Good animation is not an art you either get or don't; there are learnable tricks that improve animations without the 'magic'. Evidence: One mistake I made early in my career
- Adding a subtle scale-down when a button is pressed makes an interface feel instantly more responsive. Evidence: 1. Scale your buttons
- Animating from scale(0) feels wrong because the element looks like it comes out of nowhere; a higher initial scale resembles the real world, like a deflated balloon that still has a visible shape. Evidence: scale(0) feels wrong because it looks like the element comes out of nowhere
- Opening subsequent tooltips with no delay and no animation feels faster without defeating the purpose of the initial delay. Evidence: This feels faster without defeating the purpose of the initial delay
- Radix and Base UI skip the tooltip delay once a tooltip is shown, and Base UI also allows skipping the animation. Evidence: Radix and Base UI, two unstyled component libraries
- Easing is the most important part of any animation; it can make a bad animation look great and a great animation look bad. Evidence: 4. Choose the right easing
- Most of the article's demo animations use custom easing curves to make them feel better. Evidence: Most of the animations you’ve seen so far also use custom easing curves
- ease-out accelerates at the beginning, which gives the user a feeling of responsiveness. Evidence: If you are animating something that is entering or exiting the screen, use ease-out
- Two dropdowns with the identical 300ms duration feel different: the ease-in one feels slower than the ease-out one. Evidence: The duration for these dropdowns is identical, 300ms
- ease-in is not made for UI animations because it speeds up at the end, the opposite of what UI wants. Evidence: this easing is just not made for UI animations
- Built-in CSS easing curves are usually not strong enough; a custom ease-in-out feels more energetic than the built-in one. Evidence: The built-in easing curves in CSS are usually not strong enough
- transform-origin defaults to center, which is wrong in most cases for popovers. Evidence: 5. Make your animations origin-aware
- The origin mismatch is most noticeable when both the horizontal and vertical origins don't match, like top right. Evidence: The difference is most noticeable when both the horizontal and vertical origins don't match
- Base UI and Radix UI support origin-aware animations through CSS variables that set the correct origin automatically. Evidence: Base UI and Radix UI support origin-aware animations through CSS variables
- Whether users notice small details matters little, because in aggregate unseen details become visible and compound. Evidence: You might think that the difference is subtle
- A faster-spinning spinner makes the app seem to load faster even though load time is the same, improving perceived performance. Evidence: 6. Keep your animations fast
- A 180ms select animation feels more responsive than a 400ms one. Evidence: A 180ms select animation feels more responsive than a 400ms one
- Animations and hover interactions seen tens or hundreds of times a day quickly become annoying and make the interface feel slower instead of delighting. Evidence: Remove animations or hover interactions altogether
- Blur works in a state crossfade because it bridges the visual gap between old and new states; without it the eye sees two distinct objects. Evidence: 7. Use blur when nothing else works
- Blur tricks the eye into seeing a smooth transition by blending the two states together. Evidence: It tricks the eye into seeing a smooth transition by blending the two states together

## Quotes

> It can make a bad animation look great, and a great animation look bad.
> UI animations should generally stay under 300ms
> In the aggregate, unseen details become visible, they compound.

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: Self-promotion: the page opens with a plug for the aiforui.dev course (early access closed) and ends with a waitlist plug for animations.dev.
- Caveat: Publication date is unknown, so library behaviour (Radix and Base UI tooltip delay skipping, data-instant, CSS variable names) may have changed since.
- Caveat: The Radix variable shown is the dropdown-menu one (--radix-dropdown-menu-content-transform-origin); the article does not list the variable names for other Radix components.
- Caveat: The article relies on interactive demos (labelled Paste, Options, Feedback, Ethereum); the scraped text only has their labels and captions, so visual comparisons are described from the surrounding prose.
- Caveat: The code snippets were scraped with extra spaces (e.g. '0.125 s', 'var ( --transform-origin )'); values are normalised here without changing any numbers.
- Caveat: The 300ms ceiling is stated as a rule of thumb ('generally'), not a hard limit; 180ms vs 400ms is a single demo comparison.
- Caveat: No specific custom cubic-bezier values are given; the article defers to easings.co for custom curves.
- Caveat: maps_to is null for every decision: the questionnaire's motion questions ask about duration steps (Q-motion-02) and curve grouping (Q-motion-03), not the specific choices this article makes, so none clearly matches.

### Rules and practices

- **should** (patterns, all): Give the user feedback on every action as soon as possible, so the interface feels like it is listening. Why: The interface should feel as if it's listening to the user. [You should aim to give the user feedback on all of their actions as soon as possible]
- **must** (components, all): Show a loading state when a form is submitted. Why: Every action should get feedback as soon as possible. [Submitting a form should show a loading state]
- **must** (components, all): Show a success state after a copy-to-clipboard action. Why: Every action should get feedback as soon as possible. [copy to clipboard action should show a success state]
- **should** (motion, all): Scale buttons down subtly while pressed: scale 0.97 on the :active pseudo-class. Why: It is an easy way to make the interface feel instantly more responsive. Values: 0.97, :active. [A scale of 0.97 on the :active pseudo-class should do the job]
- **must** (motion, all): Do not animate an element in from scale(0). Why: Elements that animate from scale(0) can make an animation feel off; it looks like the element comes out of nowhere. Values: scale(0). [Elements that animate from scale(0) can make an animation feel off]
- **should** (motion, all): Start scale-in animations from an initial scale of 0.9 or higher (the article's example uses 0.93). Why: A higher initial scale feels more gentle, natural and elegant and resembles the real world, like a deflated balloon that still has a shape. Values: 0.9+, 0.93. [Try animating from a higher initial scale instead (0.9+)]
- **must** (components, all): Give tooltips a delay before they first appear. Why: The delay prevents accidental activation. [Tooltips should have a delay before appearing to prevent accidental activation]
- **must** (components, all): Once a tooltip is open, open other tooltips in the same group immediately, with no delay and no animation. Why: It feels faster without defeating the purpose of the initial delay. [Once a tooltip is open, hovering over other tooltips should open them with no delay and no animation]
- **should** (components, react): In Base UI, disable the animation on subsequent tooltips by targeting the data-instant attribute and setting transition-duration to 0ms. Why: Base UI skips the delay itself; this also skips the animation for subsequent tooltips. Values: data-instant, transition-duration: 0ms. [target the data-instant attribute and set the transition duration to 0ms]
- **consider** (motion, css): Animate tooltips in and out with transform and opacity at 0.125s ease-out, starting and ending at opacity 0 and scale(0.97), with transform-origin set from the library variable. Why: It is the author's example styling for a tooltip whose subsequent opens skip the animation via data-instant. Values: transform 0.125s ease-out, opacity 0.125s ease-out, opacity: 0, scale(0.97), transform-origin: var(--transform-origin), [data-starting-style], [data-ending-style]. [Here’s how the styles would look like to achieve this]
- **should** (motion, all): Treat easing as the most important part of any animation when building or reviewing motion. Why: Easing can make a bad animation look great and a great animation look bad. [Easing ... is the most important part of any animation]
- **must** (motion, all): Use ease-out for anything entering or exiting the screen. Why: It accelerates at the beginning, which gives the user a feeling of responsiveness. Values: ease-out. [If you are animating something that is entering or exiting the screen, use ease-out]
- **should** (motion, all): Pick easing that moves fast at the beginning of the motion and does not speed up at the end. Why: Ease-out moves much faster at the beginning, which is what UI animations want; ease-in speeds up at the end, which is the opposite of what we want. [Notice how much faster it moves at the beginning, that’s what we want for our animations]
- **must** (motion, all): Do not use ease-in for UI animations such as dropdowns. Why: It starts slow and speeds up at the end, the opposite of what UI needs; at the same 300ms it feels slower than ease-out. Values: ease-in. [this easing is just not made for UI animations. It speeds up at the end]
- **should** (motion, all): Do not try to rescue ease-in by shortening the duration; switch the curve instead. Why: Decreasing the duration could make ease-in work, but the curve itself is not made for UI animations. [You could decrease the duration to make ease-in work]
- **should** (motion, css): Avoid the built-in CSS easing curves; use custom easing curves instead. Why: The built-in curves are usually not strong enough; a custom curve feels more energetic. [The built-in easing curves in CSS are usually not strong enough, which is why I almost never use them]
- **should** (motion, all): Apply the easing principles with a custom, stronger ease-out curve for more impact. Why: Custom easing feels more energetic than the built-in version of the same curve. Values: ease-out. [just use a custom ease-out for more impact]
- **consider** (tooling, all): Source custom easing variations from a curated site such as easings.co. Why: The author recommends it for custom variations of all easings. Values: easings.co. [here’s one I recommend: easings.co]
- **must** (motion, all): Make popovers origin-aware: scale them in from their trigger by setting transform-origin to the trigger side. Why: It makes popovers feel better; the difference is most noticeable when both horizontal and vertical origins differ, like top right. Values: transform-origin. [5. Make your animations origin-aware]
- **consider** (process, all): Check origin-aware popovers at a position where both the horizontal and vertical origins differ from center, such as top right. Why: The difference is most noticeable when both the horizontal and vertical origins don't match, like top right [inferred: the source states where the difference shows most, not a testing rule]. Values: top right. [The difference is most noticeable when both the horizontal and vertical origins don’t match, like top right]
- **must** (motion, css): Do not leave transform-origin at its default center for popovers and dropdowns. Why: The default value center is wrong in most cases. Values: center. [its default value is center , which is wrong in most cases]
- **should** (motion, react): With Radix, set transform-origin: var(--radix-dropdown-menu-content-transform-origin); with Base UI, set transform-origin: var(--transform-origin). Why: These library variables set the correct origin automatically. Values: var(--radix-dropdown-menu-content-transform-origin), var(--transform-origin). [applying these variables will set the correct origin automatically]
- **should** (process, all): Polish small details even when users may not consciously notice them. Why: In the aggregate, unseen details become visible; they compound. [whether you or your users notice it doesn’t matter that much]
- **should** (motion, all): Keep UI animations fast: as a rule of thumb, generally under 300ms. Why: Faster animations feel more responsive and improve perceived performance; a 180ms select feels more responsive than a 400ms one. Values: 300ms. [As a rule of thumb, UI animations should generally stay under 300ms]
- **should** (motion, all): Prefer a short duration such as 180ms over a long one such as 400ms for a select menu animation. Why: A 180ms select animation feels more responsive than a 400ms one. Values: 180ms, 400ms. [A 180ms select animation feels more responsive than a 400ms one]
- **should** (motion, all): Make loading spinners spin fast. Why: A faster-spinning spinner makes the app seem to load faster even though load time is the same. [A faster-spinning spinner makes the app seem to load faster]
- **must** (motion, all): Remove animations and hover interactions from elements people see tens or hundreds of times a day. Why: Instead of delighting, they quickly become annoying and make the interface feel slower. Values: tens, maybe even hundreds of times a day. [Remove animations or hover interactions altogether if they are seen tens, maybe even hundreds of times a day]
- **should** (process, all): Before reaching for blur, first try a few different easings and durations. Why: Blur is the fallback for when easing and duration changes still leave the animation feeling off. [If you tried a few different easings and durations for your animation]
- **consider** (motion, all): When a transition still feels off, add a small filter: blur() during it to mask the imperfections. Why: Blur bridges the visual gap between old and new states so the eye sees one smooth transition instead of two distinct objects. Values: filter: blur(). [7. Use blur when nothing else works]
- **consider** (motion, all): When a button crossfades between two states, add 2px of blur to the crossfade (combined with the 0.97 press scale). Why: The blurred version feels much more pleasing because it blends the two states together. Values: 2px, 0.97. [another one that adds 2px of blur to that animation]

### Decisions it informs

- Should buttons react visually the moment they are pressed?
  - No press effect: The button gives no immediate feedback, so the interface feels less responsive [inferred]. When: Not recommended by the source.
  - Scale to 0.97 on :active: A subtle scale-down makes the interface feel instantly more responsive. When: Default for buttons.
  - Recommendation: Scale buttons to 0.97 on the :active pseudo-class, because the interface should feel as if it is listening and give feedback on every action as soon as possible.
- Which easing curve should elements entering or leaving the screen use?
  - ease-in: Starts slow and speeds up at the end; a 300ms dropdown feels slower than the same one with ease-out. When: Not for UI enter or exit animations, per the source.
  - Built-in ease-out: Starts fast, so the UI feels responsive, but the built-in curve is usually not strong enough. When: Follows the ease-out principle, but the source prefers a custom curve for more impact.
  - Custom ease-out: Starts fast with more energy and impact than the built-in keyword. When: Default for enter and exit animations.
  - Recommendation: Custom ease-out: ease-out accelerates at the start, which feels responsive, and custom curves are stronger than CSS's built-ins.
- What scale should a popover, menu or other element start from when it animates in?
  - scale(0): The element appears to come out of nowhere and the animation feels off. When: Never, per the source.
  - 0.9 or higher (e.g. 0.93): Gentle, natural and elegant, like a deflated balloon that still has a visible shape. When: Default for scale-in animations.
  - Recommendation: Start from 0.9 or higher; the article's demo uses 0.93 and its tooltip snippet uses 0.97.
- Where should popovers and dropdowns scale from?
  - Center (CSS default): The popover grows from its own middle rather than from the trigger [inferred]; the mismatch is most noticeable at a top-right position. When: Wrong in most cases, per the source.
  - Origin-aware (from the trigger): The popover grows out of the button that opened it. When: Default for popovers and dropdowns; Radix and Base UI set it through CSS variables.
  - Recommendation: Origin-aware, using the library's transform-origin variable, because center is wrong in most cases and unseen details compound.
- How should tooltips behave when someone moves from one tooltip trigger to the next?
  - Delay and animate every tooltip: Each tooltip waits and animates again, which feels slower when moving across a group of icons [inferred]. When: Not recommended by the source.
  - Delay the first, then open the rest instantly with no animation: Feels faster while still preventing accidental activation of the first tooltip. When: Default; Radix and Base UI skip the delay, and Base UI can skip the animation via data-instant.
  - Recommendation: Delay only the first tooltip; open subsequent ones with no delay and no animation.
- How long should UI animations last?
  - Around 180ms: A select animation feels responsive. When: Select menus and other UI animations, which should generally stay under 300ms.
  - Around 400ms: The same select animation feels less responsive. When: The source uses it as the slower counter-example.
  - Recommendation: Keep UI animations under 300ms as a rule of thumb; 180ms feels more responsive than 400ms.
- Should an interaction people repeat many times a day be animated?
  - Animate it: Delights at first but quickly becomes annoying and makes the interface feel slower. When: Interactions seen rarely [inferred]
  - Remove the animation and hover effect: The interface stays fast for frequent tasks. When: Elements seen tens, maybe even hundreds of times a day.
  - Recommendation: Remove animations or hover interactions altogether for elements seen tens or hundreds of times a day.
- How should a button or element switch between two visual states?
  - Plain crossfade: You see two distinct objects, which feels less natural. When: When the transition already feels right [inferred]
  - Crossfade with 2px blur: Blur blends the two states so the eye reads one smooth transition. When: When easing and duration tweaks still leave it feeling off.
  - Recommendation: Add a little blur (2px in the example) when nothing else works.

### Process

1. Add press and action feedback: Scale buttons to 0.97 on :active; show a loading state on form submit and a success state on copy to clipboard.
2. Check starting scale: Replace any scale(0) entrance with an initial scale of 0.9 or higher (e.g. 0.93).
3. Tune tooltip timing: Keep an initial delay on the first tooltip; open subsequent tooltips with no delay and no animation (Base UI: [data-instant] transition-duration 0ms).
4. Pick the easing: Use ease-out for anything entering or exiting; replace ease-in and built-in keywords with a custom ease-out curve (e.g. from easings.co).
5. Set the origin: Make popovers scale from their trigger by setting transform-origin from the library variable instead of the default center; the difference shows most at a top-right position.
6. Check speed and frequency: Keep UI animations under 300ms; remove animations and hover effects on elements seen tens or hundreds of times a day.
7. Use blur as the last resort: Only after trying a few easings and durations, add a small filter: blur() (e.g. 2px) to crossfades that still feel off.

### Examples and visual references

- Button press demo (Interactive demo labelled 'Paste' in the article): Two 'Paste' buttons, compared with and without the 0.97 press scale [inferred from the paired labels], showing how the press scale makes the button feel responsive.
- scale(0) vs higher initial scale (Interactive demo labelled 'Options'): Two buttons open the same element, one from scale(0) and one from 0.93; the 0.93 version feels gentle while scale(0) appears from nowhere.
- Tooltip group (Row of icons with tooltips): Hover one icon to get a delayed tooltip, then move quickly to another icon in the group and its tooltip appears instantly.
- ease-in vs ease-out dropdowns (Two 'Options' dropdowns side by side): Both last 300ms; the ease-in one on the left starts slow and feels slower than the ease-out one on the right.
- Easing curve graph (Replayable curve visual): Plots ease-out (blue) against ease-in, showing how much faster ease-out moves at the beginning.
- Built-in vs custom ease-in-out (Comparison labelled 'Built-in'): The custom ease-in-out version feels more energetic than CSS's built-in curve.
- Origin-aware feedback popover (Interactive 'Feedback' button): Toggling (J key or grey X icon) switches between center origin and trigger origin; S slows it down; dashed buttons move the component, and top right shows the biggest difference.
- Spinner speed comparison (Spinner demo captioned 'Which one works harder to load the data?' (two spinners [inferred])): The faster-spinning spinner makes loading seem faster though load time is the same.
- 180ms vs 400ms select (Two 'Ethereum' select menus): The 180ms select feels more responsive than the 400ms one.
- Frequently used list (List demo: 'Imagine you interact with this list often during the day'): Shows how animations on something used often become annoying and make the interface feel slower.
- Blur on a two-state button (Toggle button demo with a progress timeline scrubber): One button crossfades plainly, the other adds 2px blur and a 0.97 press scale; scrubbing to progress 0.5 shows the unblurred version as two distinct objects while blur blends them.

### Numbers

- 0.97: Scale applied to a button on :active press; also the start and end scale in the tooltip CSS and the press scale in the blur demo [A scale of 0.97 on the :active pseudo-class]
- 0.9+: Minimum initial scale to animate from instead of scale(0) [Try animating from a higher initial scale instead (0.9+)]
- 0.93: Initial scale used in the scale-in demo [I’m using an initial scale of 0.93 here]
- 0.125s: Tooltip transform and opacity transition duration with ease-out [transform 0.125 s ease-out]
- 0ms: transition-duration for Base UI's [data-instant] subsequent tooltips [set the transition duration to 0ms]
- 300ms: Identical duration of the ease-in and ease-out dropdown demos [The duration for these dropdowns is identical, 300ms]
- under 300ms: Rule of thumb ceiling for UI animation duration [UI animations should generally stay under 300ms]
- 180ms: Select animation duration that feels more responsive [A 180ms select animation feels more responsive than a 400ms one]
- 400ms: Slower select animation duration used as the counter-example [A 180ms select animation feels more responsive than a 400ms one]
- tens, maybe even hundreds of times a day: Frequency at which animations and hover interactions should be removed [Remove animations or hover interactions altogether]
- 2px: Blur added to a two-state button crossfade [adds 2px of blur to that animation]
- 0.5: Timeline progress point in the blur demo where the unblurred crossfade shows two distinct states [Notice how much more distinct the two states are without blur: progress 0.5]
- 0: Opacity of the tooltip at its starting and ending style (paired with scale(0.97)) [opacity : 0 ; transform : scale ( 0.97 )]

<!-- /od:learn -->
