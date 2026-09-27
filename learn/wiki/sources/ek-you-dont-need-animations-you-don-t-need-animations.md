---
type: source
title: You Don't Need Animations
created: 2026-09-27
updated: 2026-09-27
video_id: ek-you-dont-need-animations
url: https://emilkowal.ski/ui/you-dont-need-animations
channel: Emil Kowalski (web)
published: Unknown
authority: non-negotiable
tags:
  - animation
  - motion
  - when-to-animate
  - purposeful-animation
  - frequency-of-use
  - perceived-performance
  - duration
  - keyboard
  - tooltips
  - toasts
  - delight
  - emil-kowalski
---

# You Don't Need Animations

## Metadata

- Page ID: `ek-you-dont-need-animations`
- Publisher: Emil Kowalski (web)
- Published: Unknown
- URL: https://emilkowal.ski/ui/you-dont-need-animations

## Summary

Emil Kowalski explains how to decide when to animate and when not to. Every animation needs a purpose: explaining how a feature works, making a button press feel alive and responsive, avoiding a sudden appearance, keeping spatial consistency, or, for rarely used parts, delight. How often people will see an animation is a key factor: things used many times a day, hover effects and every keyboard-initiated action are best with no animation (keyboard actions should never animate). Unless it is a marketing site, animations have to be fast (UI animations generally under 300ms) because speed improves perceived performance and keeps the interface connected to the user's actions. For a design system this becomes a gate before any motion token is used (purpose, frequency, speed) plus concrete component behaviour for toasts, tooltips, dropdowns, command menus and spinners [inferred].

## Key Ideas

- Animations done right make an interface feel predictable, faster and more enjoyable; done wrong they feel unpredictable, slow and annoying and can cost user trust.
- Before animating anything, name its purpose.
- An animation can replace a static marketing asset when it explains how a feature works right in the first viewport.
- A subtle scale-down when pressing a button is a purposeful animation: it makes the interface feel alive and responsive.
- Toasts should animate in, and entering and leaving in the same direction makes swipe-to-dismiss feel intuitive.
- Delight animations work only on things people rarely use; used daily, the delight fades into irritation.
- Frequency of use is a key factor in deciding whether to animate: something opened hundreds of times a day, like Raycast, is best with no animation.
- Keyboard-initiated actions should never be animated because animation makes them feel delayed and disconnected.
- Outside marketing sites, animations must be fast; they improve perceived performance and make the interface feel like it is listening.
- A faster spinner makes loading feel faster even when the load time is the same.
- Keep UI animations under 300ms as a rule of thumb; a 180ms dropdown feels more responsive than a 400ms one.
- Tooltips need a slight first delay, but once one is open, neighbouring tooltips should open instantly with no animation.
- Even a rarely used, purposeful animation still has to be checked for speed.
- The goal is a great interface, not animation for its own sake; sometimes the best animation is no animation.

## Entities

- [[entities/emil-kowalski|Emil Kowalski]] (person): Design engineer and author of the article
- [[entities/linear|Linear]] (company): Company where the author built the marketing animation used as the example of a purposeful animation
- [[entities/product-intelligence|Product Intelligence]] (product): Linear feature explained by the animation on linear.app/ai
- [[entities/sonner|Sonner]] (library): Toast component whose enter animation is the example of an animation with two purposes
- [[entities/raycast|Raycast]] (product): App the author opens hundreds of times a day; it has no open animation, cited as the optimal experience
- [[entities/command-menu|Command menu]] (concept): Interactive demo (with and without animation) used to show why frequently opened UI and arrow-key navigation should not animate
- [[entities/perceived-performance|Perceived performance]] (concept): How fast the app seems; fast animations and faster spinners improve it
- [[entities/spatial-consistency|Spatial consistency]] (concept): An element entering and leaving in the same direction, which makes its dismiss gesture feel intuitive
- [[entities/animations-dev|animations.dev]] (product): The author's animation course, plugged at the end of the article
- [[entities/aiforui-dev|aiforui.dev]] (product): The author's course, plugged in a banner at the top of the page

## Topics

- [[topics/motion-principles|Motion principles]]: Animate only with a purpose, weigh how often the animation will be seen, and remember that the best animation is sometimes none.
- [[topics/easing-and-timing|Easing and timing]]: Product UI animations must be fast: generally under 300ms; a 180ms dropdown feels more responsive than a 400ms one. Marketing sites are the exception.
- [[topics/micro-interactions|Micro-interactions]]: A subtle scale-down on button press makes the interface feel alive and responsive; a hover effect used many times a day would likely be best with no animation; a morphing feedback component is delightful only if rarely used.
- [[topics/toasts-and-notifications|Toasts and notifications]]: Sonner animates toasts in because a sudden appearance feels off, and enters and exits in the same direction so swipe-down-to-dismiss feels intuitive.
- [[topics/modals-and-popovers|Modals and popovers]]: Tooltips get a slight initial delay to prevent accidental activation, then open with no delay and no animation while another is open; a 180ms dropdown feels more responsive than a 400ms one.
- [[topics/feedback-empty-and-loading-states|Feedback, empty and loading states]]: A faster-spinning spinner makes the app seem to load faster at the same load time.
- [[topics/landing-pages|Landing pages]]: On marketing pages an animation can explain a feature in the first viewport better than a static asset (Linear's Product Intelligence), and marketing sites are exempt from the need for fast animation.
- [[topics/gestures-and-drag|Gestures and drag]]: Matching enter and exit direction to the dismiss direction makes a swipe-to-dismiss gesture feel intuitive.
- [[topics/buttons-and-actions|Buttons and actions]]: A subtle scale-down when pressing a button is cited as a purposeful animation that makes the interface feel alive and responsive.
- [[topics/design-taste-and-judgement|Design taste and judgement]]: Deciding when not to animate is part of craft: think about what the user wants to achieve and how often they will see the motion.
- [[topics/design-process|Design process]]: Deciding whether to animate follows an order: name the purpose, weigh how often it will be seen and what the user wants to achieve, then check the speed.

## Notable Claims

- When done right, animations make an interface feel predictable, faster and more enjoyable to use and help a product stand out. Evidence: opening paragraph: "When done right, animations make an interface feel predictable"
- Badly used animations can make an interface feel unpredictable, slow and annoying, and can make users lose trust in the product. Evidence: opening: "But they can also do the opposite"
- Linear could have used a static asset for Product Intelligence, but the animated version helps users understand what the feature does straight in the initial viewport. Evidence: Purposeful animations: "We could have used a static asset"
- A subtle scale-down when pressing a button helps the interface feel more alive and responsive. Evidence: Purposeful animations: "subtle scale down effect when pressing a button"
- A toast that suddenly appears would feel off. Evidence: Sonner's enter animation, first purpose
- A toast that comes from and leaves in the same direction creates spatial consistency, which makes the swipe-down-to-dismiss gesture feel more intuitive. Evidence: Sonner's enter animation, second purpose
- A morphing feedback component is a pleasant surprise when rarely used but becomes irritating and slows users down when used multiple times a day. Evidence: "Used multiple times a day, this component would quickly become irritating"
- How often users will see an animation is a key factor in deciding whether to animate. Evidence: end of Purposeful animations, lead-in to Frequency of use
- Raycast, used hundreds of times a day, has no animation at all when opened, and that is the optimal experience. Evidence: Frequency of use: "I use Raycast hundreds of times a day"
- Animating keyboard-initiated actions makes them feel slow, delayed and disconnected from the user's actions. Evidence: Frequency of use: "The same goes for keyboard-initiated actions"
- When opening a tool like Raycast the user has a clear goal, does not expect or need to be delighted, and wants no unnecessary friction. Evidence: Frequency of use: "I just want to do my work with no unnecessary friction"
- A hover effect is nice, but if used multiple times a day it would likely benefit most from having no animation at all. Evidence: Frequency of use: "A hover effect is nice, but if used multiple times a day"
- Animating the highlight during arrow-key list navigation makes it feel delayed compared to the key presses. Evidence: "Notice how the highlight feels delayed compared to the keys you press"
- Fast animations improve the perceived performance of an app, stay connected to user actions and make the interface feel as if it is listening. Evidence: Perception of speed
- A faster-spinning spinner makes the app seem to load faster even though the load time is the same. Evidence: Perception of speed: spinner example
- A 180ms dropdown animation feels more responsive than a 400ms one. Evidence: Perception of speed: "A 180ms dropdown animation feels more responsive"
- UI animations should generally stay under 300ms. Evidence: "As a rule of thumb"
- A slight delay before a tooltip appears prevents accidental activation; opening subsequent tooltips instantly feels faster without defeating the purpose of that delay. Evidence: Perception of speed: tooltip example
- The goal is not to animate for animation's sake but to build great interfaces users will happily use daily; sometimes the best animation is no animation. Evidence: Building great interfaces: "The goal is not to animate for animation’s sake"

## Quotes

> Sometimes this requires animations, but sometimes the best animation is no animation.
> As a rule of thumb, UI animations should generally stay under 300ms
> How often users will see an animation is a key factor

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: Self-promotion: a banner for the author's aiforui.dev course opens the page and the article ends with a plug for animations.dev; neither is a rule.
- Caveat: The page's interactive demos (morphing feedback, command menu toggle with J/K and Shift, spinners, dropdowns) do not survive text extraction; only their labels and surrounding text are available, so their exact motion values are unknown.
- Caveat: This article gives no numeric values for the button press scale, the tooltip delay or the spinner speed; other Emil Kowalski articles may.
- Caveat: 300ms is stated as a rule of thumb ("generally"), and marketing sites are explicitly exempt from the need for fast animation. The 180ms versus 400ms dropdown is a comparison, not a prescribed exact value.
- Caveat: The Raycast example is the author's personal usage, offered as an illustration rather than measured data.
- Caveat: Publication date unknown. Some demo captions appear twice in the extracted text ("Imagine you interact with this list often during the day.", the Paste button label); this may be two demo variants or an extraction artifact.
- Caveat: The only media item is an Obsidian app icon from the demo list, which carries no design lesson and was not downloaded.

### Rules and practices

- **must** (motion, all): Before adding any animation, state its purpose (explain how something works, make an interaction feel alive and responsive, avoid a sudden appearance, keep spatial consistency, or delight); if it has none, do not animate. Why: Done wrong, animations make an interface feel unpredictable, slow and annoying and can cost user trust; making sure an animation has a purpose is step one of knowing when to animate. [Purposeful animations: "Step one is making sure your animations have a purpose"; "what’s the purpose of this animation?"]
- **must** (motion, all): Do not animate for animation's sake; when an animation does not make the interface better to use daily, ship no animation. Why: The goal is to build interfaces users will happily use daily; sometimes the best animation is no animation. [Building great interfaces: "The goal is not to animate for animation’s sake"]
- **must** (process, all): Decide whether to animate by estimating how often the user will see the animation; the more often it is seen, the stronger the case for no animation. Why: Frequency of use is a key factor: repeated animations turn from pleasant into annoying and slow users down. ["How often users will see an animation is a key factor in deciding whether to animate or not"; "Think about what the user wants to achieve and how often they will see an animation"]
- **should** (components, all): Do not animate the opening of UI that people open hundreds of times a day, such as Raycast or a command menu; show it instantly. Why: If it animated every time it opened it would be very annoying; Raycast has no animation at all and the author calls that the optimal experience. The source illustrates this rather than stating it as a rule; when the open is triggered from the keyboard, the must rule on keyboard-initiated actions applies. [Frequency of use: "I use Raycast hundreds of times a day"; "That’s the optimal experience"]
- **should** (process, all): For goal-driven tools, design for the user's goal with no unnecessary friction instead of trying to delight them. Why: When the user opens such a tool they have a clear goal and do not expect or need to be delighted. ["I don’t expect to be “delighted”, I don’t need to be"]
- **should** (motion, all): Do not animate hover effects on elements users interact with multiple times a day. Why: A hover effect is nice, but used multiple times a day it would likely benefit the most from having no animation at all. ["A hover effect is nice, but if used multiple times a day"]
- **must** (motion, all): Never animate keyboard-initiated actions. Why: They may be repeated hundreds of times a day, and animation makes them feel slow, delayed and disconnected from the user's actions. ["The same goes for keyboard-initiated actions ... You should never animate them."]
- **must** (components, all): Do not animate the highlight when navigating a list with arrow keys (for example in a command menu); move it instantly. Why: Arrow-key navigation is a keyboard-initiated action, which should never be animated; an animated highlight feels delayed compared to the keys the user presses. ["use arrow keys to navigate through the list. Notice how the highlight feels delayed"]
- **should** (components, all): Give buttons a subtle scale-down effect while they are pressed. Why: It helps the interface feel more alive and responsive. [Purposeful animations: "subtle scale down effect when pressing a button"]
- **should** (components, all): Animate toasts in rather than making them appear suddenly. Why: A toast suddenly appearing would feel off. [Sonner’s enter animation: "Having a toast suddenly appear would feel off, so we animate it in"]
- **should** (components, all): Make a toast come from and leave in the same direction, matching its swipe-to-dismiss gesture (Sonner: swipe down to dismiss). Why: Coming from and leaving in the same direction creates spatial consistency, which makes the swipe-down-to-dismiss gesture feel more intuitive. [Sonner’s enter animation: "comes from and leaves in the same direction"]
- **should** (motion, all): Use delight animations (such as a morphing component) only on components users rarely interact with. Why: Rarely seen, the animation is a pleasant surprise and makes the experience unique and memorable. ["This works as long as the user will rarely interact with it"]
- **should** (motion, all): Do not put delight animations on components used multiple times a day. Why: Used multiple times a day the component would quickly become irritating; the initial delight fades and the animation slows users down. Stated as a consequence rather than a rule. ["Used multiple times a day, this component would quickly become irritating"]
- **consider** (patterns, web): On marketing pages, consider an animation instead of a static asset when it explains how a feature works in the initial viewport. Why: The animated version helps the user understand what the feature does straight in the initial viewport. [Purposeful animations: Linear Product Intelligence, linear.app/ai]
- **must** (motion, all): Keep every product UI animation fast; only marketing sites are exempt. Why: Fast animations improve perceived performance, stay connected to the user's actions and make the interface feel as if it is truly listening. [Perception of speed: "Unless you are working on marketing sites, your animations have to be fast"]
- **should** (motion, all): Keep UI animation durations under 300ms. Why: Stated rule of thumb; fast animations improve perceived performance and stay connected to the user's actions. Values: 300ms. ["As a rule of thumb, UI animations should generally stay under 300ms"]
- **should** (motion, all): Keep dropdown animations fast: a 180ms dropdown feels more responsive than a 400ms one. Why: A 180ms dropdown animation feels more responsive than a 400ms one. Values: 180ms, 400ms. ["A 180ms dropdown animation feels more responsive than a 400ms one"]
- **must** (process, all): Even when an animation is rarely seen and has a clear purpose, still check its speed; passing the purpose and frequency checks does not exempt it. Why: The article orders the decision as purpose, then frequency, then speed, and says a rare, purposeful animation still has to be thought about for speed. ["even if your animation won’t be used too often and it fulfills a clear purpose, you still have to think about its speed"]
- **should** (components, all): Use a faster-spinning spinner for loading indicators. Why: A faster spinner makes the app seem to load faster even though the load time is the same, improving perceived performance. [Perception of speed: "a faster-spinning spinner makes the app seem to load faster"]
- **should** (components, all): Give tooltips a slight delay before they first appear. Why: It prevents accidental activation. ["tooltips should have a slight delay before appearing"]
- **should** (components, all): While a tooltip is open, open other tooltips on hover with no delay and no animation. Why: It feels faster without defeating the purpose of the initial delay. ["hovering over other tooltips should open them with no delay and no animation"]
- **consider** (process, all): Judge a frequently used animation by toggling it against a no-animation version and asking which feels better if used hundreds of times a day. [inferred] Why: The article's own demos pose this comparison to show how animation feels when repeated. [Command menu demo: "Which one feels better if used hundreds of times a day?"]

### Decisions it informs

- Should this interaction animate at all?
  - Animate: Can explain a feature, make an interaction feel alive and responsive, avoid a sudden appearance, keep spatial consistency or bring delight. When: The animation has a clear purpose and users see it rarely, or it prevents something from appearing abruptly (e.g. a toast).
  - No animation: The UI responds instantly and feels connected to the user's actions with no friction. When: Users see it multiple or hundreds of times a day (launcher, command menu, frequent hover), or it is keyboard-initiated.
  - Recommendation: Animate only with a purpose; use no animation for every keyboard-initiated action, and lean to no animation for anything seen many times a day; sometimes the best animation is no animation.
- How long should a product UI animation such as a dropdown take?
  - 180ms: Feels responsive and connected to the click. When: Product UI such as dropdowns.
  - 400ms: Feels less responsive than 180ms. When: Not recommended for product UI; the article only exempts marketing sites from the need to be fast [inferred].
  - Recommendation: Keep UI animations generally under 300ms; the 180ms dropdown feels more responsive than the 400ms one.
- Should a component get a delight animation, such as morphing?
  - Delight animation: Makes the experience unique and memorable; a pleasant surprise. When: The user will rarely interact with the component.
  - Plain, unanimated: No irritation or slowdown with repeated use. When: The component is used multiple times a day.
  - Recommendation: Use delight only on rarely used components; used daily, the delight fades and the animation slows users down.
- How should tooltips open when the user moves between several of them?
  - Slight delay on the first tooltip, then instant: Prevents accidental activation, then feels fast while browsing neighbouring tooltips. When: Default.
  - Same delay and animation every time: Each subsequent tooltip waits and animates again, which feels slower [inferred]. When: Not recommended by the source [inferred].
  - Recommendation: A slight delay before the first tooltip, then open other tooltips with no delay and no animation while one is open.
- How should a toast arrive and leave?
  - Animate in, enter and leave in the same direction: Creates spatial consistency and makes swipe-down-to-dismiss feel intuitive. When: Default for toasts.
  - Appear suddenly: Feels off. When: Not recommended.
  - Recommendation: Animate the toast in and have it come from and leave in the same direction.
- On a marketing page, should a feature be shown with a static asset or an animation?
  - Static asset: Shows the feature without motion. When: When motion would not help explain the feature [inferred].
  - Explanatory animation: Helps the user understand what the feature does straight in the initial viewport. When: The feature's workings are easier to understand when shown in motion (Linear's Product Intelligence).
  - Recommendation: Use the animation when its purpose is to explain how the feature works, as Linear did for Product Intelligence.

### Process

1. Name the purpose: Ask what the animation is for: explaining a feature, feedback on a press, avoiding an abrupt appearance, spatial consistency for a gesture, or delight. No purpose means no animation.
2. Estimate frequency of use: Work out how often users will see it. Rare: animation (even delight) is fine. Multiple or hundreds of times a day, or any keyboard-initiated action: no animation.
3. Consider the user's goal: Think about what the user wants to achieve; goal-driven tools should have no unnecessary friction rather than delight.
4. Check the speed: Unless it is a marketing site, make the animation fast, generally under 300ms (a 180ms dropdown beats a 400ms one).
5. Compare with no animation: Toggle the animated and unanimated versions and ask which feels better if used hundreds of times a day, as the article's demos do [inferred].
6. Handle tooltips in sequence: Keep a slight delay before the first tooltip, but while one is open, open the others with no delay and no animation.

### Examples and visual references

- Animated marketing asset explaining Product Intelligence (Linear (linear.app/ai)): An animation in the initial viewport that explains how the feature works, used instead of a static asset.
- Button press scale-down: A demo button labelled Paste with a subtle scale-down while it is pressed; small feedback that makes the interface feel alive and responsive.
- Toast enter animation (Sonner): The toast animates in from the same direction it leaves, making swipe-down-to-dismiss feel intuitive.
- Morphing feedback component: A Feedback button that morphs when pressed; delightful only because it is used rarely.
- Command menu open with and without animation: Shown alongside the Raycast example: a command menu listing apps (Linear, ChatGPT, Cursor, Figma, Obsidian) and commands (Clipboard History, Emoji Picker), toggled open with J and K in an Animation and a No animation version; shows why something opened hundreds of times a day should not animate.
- Frequently used list with a hover effect: A list demo captioned "Imagine you interact with this list often during the day."; shows why a hover effect used many times a day is better without animation.
- Arrow-key list navigation with and without animation: The same command menu navigated with arrow keys; the animated highlight lags behind the key presses, and pressing Shift toggles to the instant version.
- Two spinners at different speeds: Asks which one works harder to load the data; the faster spinner makes loading seem faster.
- Dropdown at 180ms versus 400ms: Two dropdown triggers labelled Options at 180ms and 400ms; the 180ms one feels more responsive.

### Numbers

- 300ms: Rule-of-thumb upper limit for UI animation duration ["UI animations should generally stay under 300ms"]
- 180ms: Dropdown animation duration that feels more responsive [Perception of speed]
- 400ms: Dropdown animation duration that feels less responsive than 180ms [Perception of speed]
- hundreds of times a day: How often the author uses Raycast and how often keyboard actions may repeat; the frequency at which animation should be removed [Frequency of use]
- multiple times a day: Frequency at which a delight animation or hover animation becomes irritating [Feedback morph example; hover effect paragraph]

<!-- /od:learn -->
