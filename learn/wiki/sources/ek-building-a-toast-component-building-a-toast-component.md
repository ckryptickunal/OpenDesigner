---
type: source
title: Building a toast component
created: 2026-09-27
updated: 2026-09-27
video_id: ek-building-a-toast-component
url: https://emilkowal.ski/ui/building-a-toast-component
channel: Emil Kowalski (web)
published: Unknown
authority: non-negotiable
tags:
  - toast
  - sonner
  - notifications
  - css-transitions
  - interruptible-animation
  - stacking
  - swipe-to-dismiss
  - gestures
  - pointer-capture
  - hover-state
  - developer-experience
  - documentation
---

# Building a toast component

## Metadata

- Page ID: `ek-building-a-toast-component`
- Publisher: Emil Kowalski (web)
- Published: Unknown
- URL: https://emilkowal.ski/ui/building-a-toast-component

## Summary

Emil Kowalski walks through how he built Sonner, the React toast library, and why it beat a crowded field. He explains the animation engineering (interruptible CSS transitions instead of keyframes, a stacked pile of toasts that scale down for depth, hover-to-expand, and momentum-based swipe to dismiss) with the exact values Sonner uses. He then covers developer experience: a single <Toaster /> plus a toast() function backed by an observer pattern, a promise API for loading, success and error states, and a custom documentation site with interactive examples. Finally he lists the small, mostly unnoticed details (pausing the timer on a hidden tab, filling hover gaps, pointer capture while dragging, friction on the wrong drag direction) and argues that good developer experience plus beauty is what made Sonner succeed. For a design system this is a complete, value-level specification of how a notification component should move, respond to gestures and be documented.

## Key Ideas

- Animations that may be retargeted mid-flight (like a toast pile growing) need an interruptible technique: CSS transitions can be interrupted and retargeted, CSS keyframes cannot, so elements jump.
- An enter transition can be faked by rendering the start state and flipping a mounted flag after the first render; @starting-style can now do this more simply.
- A stacked pile gets depth by offsetting each toast by gap times index and scaling it down by 0.05 per step behind the front one.
- In stacked mode every toast should take the front toast's height so the pile sticks out evenly.
- Swipe to dismiss should be momentum-based: a short but fast flick dismisses as well as a long drag.
- Hovering the pile expands it; each toast's expanded offset is the sum of the heights of the toasts before it plus the gaps.
- Developer experience decides adoption: no hooks, no context, insert <Toaster /> once and call toast() from anywhere.
- Interactive documentation with copyable examples lets people try a component before they install it, and should never be an afterthought.
- Small invisible details add up: pause timers on hidden tabs, keep hover alive across gaps, keep dragging when the pointer leaves, add friction instead of hard stops.
- The fewer details users notice, the more intuitive the experience is.
- Nice defaults and good animations are the real differentiator; beauty is underused in software and can be leverage.
- A distinctive name can make a library stand out, at the cost of discoverability.
- Launch a component by showcasing its signature motion.

## Entities

- [[entities/emil-kowalski|Emil Kowalski]] (person): Design engineer, author of the article and creator of Sonner.
- [[entities/sonner|Sonner]] (library): The React toast library the article dissects; built in 2023.
- [[entities/sonner-docs-sonner-emilkowal-ski-docs|Sonner docs (sonner.emilkowal.ski/docs)]] (product): Custom documentation site with interactive examples and ready-to-use code snippets.
- [[entities/react-hot-toast|react-hot-toast]] (library): Toast library whose rendering API inspired Sonner's API design.
- [[entities/timo|Timo]] (person): Credited with doing a great job on react-hot-toast.
- [[entities/theo|Theo]] (person): Developer whose video reaction and tweet praising Sonner's animations and promise API are shown.
- [[entities/npm|npm]] (tool): Package registry used to cite Sonner's weekly downloads.
- [[entities/cursor|Cursor]] (company): Named as a company that uses Sonner.
- [[entities/x|X]] (company): Named as a company that uses Sonner.
- [[entities/openai|OpenAI]] (company): Named as a company that uses Sonner.
- [[entities/paul-graham|Paul Graham]] (person): Quoted from Hackers and Painters on unseen details combining into something stunning.
- [[entities/react|React]] (library): Framework Sonner is built for; useEffect, useState, useMemo and Context are discussed.
- [[entities/css-transitions|CSS transitions]] (concept): Chosen over keyframes because they can be interrupted and retargeted.
- [[entities/css-keyframes|CSS keyframes]] (concept): First approach for toast animation, dropped because it is not interruptible.
- [[entities/starting-style|@starting-style]] (concept): CSS at-rule that could replace the mounted-flag trick for enter transitions.
- [[entities/observer-pattern|Observer pattern]] (concept): State management approach that lets toast() notify <Toaster /> without React Context.
- [[entities/promise-api-toast-promise|Promise API (toast.promise)]] (concept): Pass a promise plus messages for loading, success and error states.
- [[entities/pointer-capture|Pointer capture]] (concept): Making the toast keep receiving pointer events after a drag starts, even outside its bounds.
- [[entities/document-hidden-visibilitychange|document.hidden / visibilitychange]] (concept): Browser signal used by useIsDocumentHidden to pause the dismiss timer on inactive tabs.
- [[entities/animations-dev|animations.dev]] (product): Emil Kowalski's animation course, plugged at the end of the article.
- [[entities/aiforui-dev|aiforui.dev]] (product): Emil Kowalski's course, plugged in a banner at the top of the page.

## Topics

- [[topics/toasts-and-notifications|Toasts and notifications]]: Full anatomy of the Sonner toast: enter transition, stacked pile with depth, hover-to-expand, optional always-expanded mode, swipe to dismiss, 4-second default timer that pauses on hover and on hidden tabs.
- [[topics/motion-principles|Motion principles]]: Motion that can be retargeted must be interruptible, so transitions beat keyframes; the stacking animation is what made people love the library.
- [[topics/easing-and-timing|Easing and timing]]: Sonner's enter/stack transition is transform 400ms ease; toasts auto-dismiss after 4 seconds by default.
- [[topics/gestures-and-drag|Gestures and drag]]: Swipe down to dismiss, momentum-based with a velocity threshold of 0.11, pointer capture during drag, and friction when dragging the wrong way.
- [[topics/micro-interactions|Micro-interactions]]: 'The big little details': pausing timers on hidden tabs, filling hover gaps with a pseudo-element, pointer capture and drag friction make the component feel right.
- [[topics/feedback-empty-and-loading-states|Feedback, empty and loading states]]: The promise API shows one toast that moves through loading, success and error states from a single call.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: Code-level techniques: data attributes for state styles, CSS variables for stack transforms, useEffect mounted flag, observer-pattern store, useIsDocumentHidden hook, height-based offset calculation.
- [[topics/ui-libraries|UI libraries]]: What makes a component library win adoption: a distinctive name, a signature animation, great developer experience and interactive documentation.
- [[topics/design-taste-and-judgement|Design taste and judgement]]: Beauty is an underused lever; unnoticed details add up, and the fewer details users notice the more intuitive the experience.
- [[topics/presenting-designs|Presenting designs]]: Sonner's launch used announcement videos focused on the stacking animation, the feature most worth showing.

## Notable Claims

- Sonner was built in 2023, is downloaded over 40,000,000 times per week from npm, and is used by companies like Cursor, X and OpenAI. Evidence: Back in 2023, I decided to build a toast library called Sonner
- Sonner is a French word meaning 'to ring', chosen because function-based names feel cheap and generic. Evidence: I looked up French words related to notifications
- Sonner took off immediately because of its stacking animation, which some companies had built before but never open sourced. Evidence: Sonner took off immediately because of the stacking animation
- CSS keyframes are not interruptible: you cannot smoothly change the end position while the animation runs, so older toasts jump into place when new ones are added quickly. Evidence: I initially used CSS keyframes for the animations, but they aren’t interruptible
- CSS transitions can be interrupted and retargeted even before the first transition has finished. Evidence: CSS transitions, on the other hand, can be interrupted and retargeted
- The @starting-style CSS at-rule can now handle the enter transition and would make the implementation much simpler. Evidence: This can now also be solved with the @starting-style CSS at-rule
- Stacking by gap times index breaks with toasts of different heights: they do not stick out evenly. Evidence: This works great until you have toasts with different heights
- Swipe to dismiss is especially useful on devices where people are already used to swiping notifications away. Evidence: especially useful on devices where people are already used to swiping
- With momentum-based swipe, a short but fast swipe dismisses the toast because the velocity is high enough. Evidence: The swipe is momentum-based
- The 0.11 velocity threshold was found through trial and error. Evidence: 0.11 is just a number that I ended up on through trial and error
- If a component is not easy to use, people give up before they even try it. Evidence: people will give up before they even try it
- Good documentation and clear instructions drastically lower the barrier to use any product, yet documentation is often done as an afterthought. Evidence: Good documentation and clear instructions can drastically lower the barrier
- Managing state with the observer pattern avoids React's Context and lets toast() be called from anywhere without hooks. Evidence: To avoid using React’s Context, I manage the state via the Observer Pattern
- Sonner's API design and toast rendering are inspired by react-hot-toast; its state management is different. Evidence: The API design is inspired by react-hot-toast
- Without pausing, a toast triggered while the user is on another tab would time out after 4 seconds and never be seen. Evidence: what if a toast is triggered and the user switches to a different tab?
- Gaps between toasts do not belong to any toast, so hovering them would drop the hover state unless they are filled. Evidence: Another interesting one is maintaining correct hover state
- Without pointer capture, a drag stops when the pointer leaves the toast. Evidence: What if, while dragging the toast, the pointer goes outside of it?
- Letting the toast be dragged the wrong way with friction feels nicer than stopping it immediately. Evidence: One thing that can also be seen in the video above is friction
- The fewer details users notice, the more intuitive the experience; users appreciate it more that way, even subconsciously. Evidence: The less details users notice, the better
- Sonner succeeded for two reasons: good developer experience, and it looks good with nice defaults and good animations, the latter being the real differentiator. Evidence: Why is Sonner successful?
- Beauty is generally underutilized in software, so it can be used as leverage to stand out. Evidence: Beauty is generally underutilized in software

## Quotes

> People simply like beautiful things.
> The less details users notice, the better. It means the experience is intuitive.

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: Self-promotion: the page opens with a banner for the author's aiforui.dev course and ends with a plug for his animations.dev course.
- Caveat: Usage figures (over 40,000,000 weekly npm downloads, used by Cursor, X and OpenAI) are self-reported, and the publish date is unknown, so the numbers may be dated.
- Caveat: Theo's video reaction and tweet are testimonials, not evidence for any rule; the tweet's like count was not used.
- Caveat: The code shown is explicitly simplified; the real Sonner source may differ.
- Caveat: The author says he might switch the enter transition to @starting-style, so the mounted-flag technique may no longer match current Sonner.
- Caveat: The 0.11 velocity threshold is an empirical value from trial and error, and the 400ms ease, 0.05 scale step and 4-second default are Sonner's own values rather than universal constants [inferred].
- Caveat: Several lessons are carried by interactive demos and videos that do not come through in the page text; only the docs screenshot image was viewed.
- Caveat: The naming advice is the author's personal taste and he states it trades away discoverability and clarity.
- Caveat: The page embeds a tweet dated Jul 15, 2024, so it was written after that date [inferred].
- Caveat: In the simplified stacking CSS, the --scale line reads var(--toasts-before) * 0.05 + 1 with no minus sign, while the transform line uses -1 * var(--toasts-before) * 0.05 + 1; the illustration (0.95, 0.9) shows toasts scaling down, so the transform line is the one to follow [inferred].

### Rules and practices

- **must** (motion, css): Animate toast enter and stack position changes with CSS transitions, not CSS keyframes, so the animation can be interrupted and retargeted mid-flight. Why: Keyframes are not interruptible; when toasts are added quickly, older ones jump into their new position instead of moving smoothly. Values: transition: transform 400ms ease. [I initially used CSS keyframes for the animations, but they aren’t interruptible]
- **must** (motion, css): Do not use CSS keyframes for any animation whose end position can change while it is running, such as a toast pile that grows. Why: You cannot smoothly change the end position of a keyframe animation while it runs, so elements jump. [That’s one downside of keyframes]
- **should** (motion, css): Enter a toast by transitioning transform from translateY(100%) to translateY(0) over 400ms with ease. Why: This is how Sonner mimics its enter keyframes with an interruptible transition. Values: translateY(100%), translateY(0), transition: transform 400ms ease. [This makes the toast start at translateY(100%) and transition to translateY(0)]
- **should** (motion, react): To get an enter transition in React, render the toast in its start state, then set a mounted flag to true in a useEffect after the first render and drive the styles through a data attribute. Why: It lets a transition play on mount, imitating an enter keyframe. Values: setMounted(true), data-mounted="true", data-mounted="false", <li data-mounted={mounted}>. [I use a useEffect hook to set mounted to true after the initial render]
- **consider** (motion, css): Consider the @starting-style CSS at-rule for enter transitions instead of a mounted flag. Why: It solves the same problem and makes the implementation much simpler. Values: @starting-style. [This can now also be solved with the @starting-style CSS at-rule]
- **consider** (components, css): Apply state-dependent toast styles through data attributes (mounted, expanded, front). Why: Sonner applies its enter and stacking styles through data attributes. Values: data-mounted, data-expanded="false", data-front="false", data-sonner-toast. [The styles are applied through data attributes]
- **should** (layout, css): Position each toast with position: absolute and set its y position by multiplying the gap between toasts by the toast's index. Why: Absolute positioning simplifies the stacking effect. Values: position: absolute, --lift-amount, --toasts-before. [I multiply the gap between toasts by the toast’s index to get the y position]
- **should** (motion, all): Scale each toast behind the front one down by 0.05 per step (0.05 * index) to create a sense of depth. Why: Scaling down creates a sense of depth in the pile. Values: 0.05 * index, Y(0) scale(1), Y(-14px) scale(0.95), Y(-28px) scale(0.9). [I also scale them down by 0.05 * index to create a sense of depth]
- **should** (components, css): Apply the stacked translate and scale only to toasts that are not in front and when the pile is not expanded. Why: The simplified Sonner CSS targets only collapsed, non-front toasts with the stacking transform. Values: [data-expanded="false"][data-front="false"], --scale: var(--toasts-before) * 0.05 + 1, scale(calc((-1 * var(--toasts-before) * 0.05) + 1)), translateY(calc(var(--lift-amount) * var(--toasts-before))). [Here’s the simplified CSS for it]
- **must** (components, all): In stacked mode, give every toast the height of the toast in front. Why: Toasts with different heights otherwise do not stick out evenly behind the front toast. [The fix is to make all the toasts the height of the toast in front when in stacked mode]
- **should** (patterns, all): Let people swipe toasts to dismiss them, on touch devices and on desktop. Why: People are already used to swiping to dismiss notifications on their devices. [Another Sonner feature is the swipe gesture]
- **should** (patterns, web): Let toasts be swiped down to dismiss, and drive the drag with a pointer-move listener that updates a CSS variable controlling translateY. Why: The source calls it just a simple event listener on the toast that updates the variable responsible for the translateY value. Values: --swipe-amount, event.clientY - pointerStartRef.current.y. [The toasts can be swiped down to dismiss]
- **should** (patterns, all): Make swipe dismissal momentum-based: remove the toast when the drag distance reaches the threshold OR the velocity (absolute distance divided by elapsed time since drag start) exceeds 0.11. Why: A quick, short swipe should dismiss the toast; people should not have to drag past a fixed distance. Values: velocity > 0.11, Math.abs(swipeAmount) >= SWIPE_THRESHOLD, velocity = Math.abs(swipeAmount) / timeTaken. [The swipe is momentum-based]
- **consider** (process, all): Tune gesture thresholds such as the dismiss velocity by trial and error. Why: Sonner's 0.11 was reached through trial and error. Values: 0.11. [0.11 is just a number that I ended up on through trial and error]
- **must** (patterns, all): Once a drag starts, capture all future pointer events on the toast so the drag continues when the mouse or thumb leaves it. Why: Otherwise the drag event stops as soon as the pointer is no longer over the toast. [Once I start dragging, I set the toast to capture all future pointer events]
- **should** (motion, all): When a toast is dragged upwards (a direction that does not dismiss it), let it move with friction so it slows down and eventually stops, instead of blocking it immediately. Why: It feels nicer than stopping the toast immediately. [Instead of just not allowing the toast to be dragged upwards]
- **should** (components, desktop): Expand the stacked pile when the pointer hovers over the toast area so all toasts are visible. Why: Stacked mode hides older toasts; hovering reveals them. [When the toasts are in stacked mode, you can hover over the toast area to expand]
- **should** (layout, all): Compute each toast's expanded offset as its index times the gap plus the sum of the heights of all toasts before it, and use it as the translateY value when expanded. Why: Toasts can have different heights, so each offset has to add up the real heights of the toasts above it [inferred]. Values: heightIndex * GAP + toastsHeightBefore, --offset. [I calculate each toast’s expanded position by adding the heights of all preceding toasts and the gap between them]
- **consider** (components, css): Pass per-toast measurements from JavaScript to CSS as custom properties (the live swipe distance, the expanded offset, the number of toasts before this one) and let the CSS build the transform from them. Why: Sonner's drag handler sets --swipe-amount on the toast, the expanded offset is used as the --offset CSS variable, and the stacking transform is computed in CSS from --lift-amount and --toasts-before. Values: --swipe-amount, --offset, --lift-amount, --toasts-before. [We then use this value as a CSS variable]
- **consider** (components, react): Offer an option to keep the toasts expanded at all times. Why: Some products need all toasts visible at all times; Sonner exposes this as the expand prop on <Toaster />. Values: expand, <Toaster />. [You can also use this expanded mode as the default behavior]
- **must** (components, css): Fill the gaps between toasts with an :after pseudo-element so the hover state stays on while the pointer crosses a gap. Why: Gaps belong to no toast, so hovering them would make the toasts lose their hover state. Values: :after. [I add an :after pseudo-element to fill these gaps]
- **should** (components, all): Auto-dismiss toasts after 4 seconds by default. Why: This is Sonner's default duration. Values: 4 seconds. [By default the toast disappears after 4 seconds unless you hover over it]
- **should** (components, all): Pause the dismiss timer while the pointer hovers over the toasts. Why: The toast disappears after 4 seconds unless you hover over it. [unless you hover over it]
- **must** (components, web): Pause the dismiss timer while the document (tab) is hidden, using document.hidden and the visibilitychange event. Why: Otherwise a toast fired while the user is on another tab times out and is never seen; an inactive tab should freeze its toasts. Values: document.hidden, visibilitychange, useIsDocumentHidden. [That’s why there’s a useIsDocumentHidden hook]
- **must** (process, all): Treat developer experience as key: make the component easy to use. Why: If a component is not easy to use, people give up before they even try it. [Developer experience is key]
- **should** (components, react): Expose toasts through a plain toast() function that can be called from anywhere, with <Toaster /> inserted once; require no hooks and no context. Why: No hooks, no context and one insert is one of the two main reasons Sonner succeeded. Values: toast("My toast"), import { toast } from "sonner", <Toaster />. [There’s no need for hooks or context, just a straightforward function call]
- **should** (components, react): Do not rely on React Context for toast state; manage it with an observer pattern where <Toaster /> subscribes and toast() notifies it. Why: The observer pattern avoids React's Context and lets toast() work from anywhere. Values: ToastState.subscribe. [To avoid using React’s Context, I manage the state via the Observer Pattern]
- **consider** (components, react): Render the toaster as an ordered list (<ol>) that maps the toasts array to list-item toasts keyed by toast id. Why: This is how Sonner's <Toaster /> renders all toasts with Array.map(). Values: <ol>, <Toast key={toast.id} toast={toast} />, Array.map(). [I can then render all the toasts using Array.map()]
- **should** (components, all): Provide a promise API: pass a promise and the message for each of its 3 states (loading, success, error) and let one toast move through them. Why: People often praise it, and most engineers find it pretty intuitive. Values: loading, success, error, toast.promise. [People often praise Sonner’s promise API]
- **consider** (process, all): Reuse a proven API shape when an existing library already does it very well. Why: Sonner's rendering API is modeled on react-hot-toast because it is simply very good. [The API design is inspired by react-hot-toast]
- **should** (tooling, all): Ship interactive documentation: live examples people can play with, paired with ready-to-use code snippets. Why: It lets people touch the product and understand how it works before using it in their own projects, drastically lowering the barrier to use. Values: sonner.emilkowal.ski/docs. [I built a fully custom documentation site for Sonner]
- **must** (process, all): Do not leave documentation and clear instructions as an afterthought. Why: They are often overlooked, yet they drastically lower the barrier to use any product. [I think it’s often overlooked and done as an afterthought when it shouldn’t be]
- **must** (process, all): Implement the small details users will not consciously notice (hidden-tab timer pause, hover gap fill, pointer capture, drag friction). Why: These details add up; together they create a component that feels just right, and the less users notice the more intuitive it is. [The big little details]
- **should** (process, all): Ship nice defaults and good animations; use beauty deliberately as a differentiator. Why: Looking good is the real differentiator; beauty is generally underutilized in software. [Two is that it looks good. It has nice defaults and good animations]
- **consider** (content, all): Give a library a distinctive, elegant name rather than one that just describes its function. Why: Function-based names (react-toast, react-snackbar, react-notifications) feel cheap, boring and generic; a different name helps it stand out, at the cost of discoverability and clarity. [naming things based on their function feels cheap]
- **consider** (process, all): When announcing a component, build the launch material around its signature motion. Why: The stacking animation was what made people fall in love with Sonner, so the announcement videos focused on it. [I knew I had to highlight this motion when introducing the library]

### Decisions it informs

- Should a toast's movement use CSS keyframes or CSS transitions?
  - CSS keyframes: Cannot be interrupted; when toasts arrive quickly, older ones jump into their new position. When: Not recommended for anything whose end position can change mid-animation.
  - CSS transitions: Can be interrupted and retargeted before finishing, so the pile moves smoothly as toasts are added. When: Toast enter and stack movement.
  - Recommendation: CSS transitions, because they are interruptible and retargetable.
- How should the enter transition be triggered?
  - Mounted flag: useEffect sets mounted to true after the first render; data-mounted switches translateY(100%) to translateY(0). When: Sonner's current implementation.
  - @starting-style: CSS defines the start state directly. When: When you want a much simpler implementation.
  - Recommendation: The author says @starting-style would make the implementation much simpler and he might switch to it.
- Should multiple toasts sit in a collapsed stack or all be shown expanded?
  - Stacked, expand on hover: Toasts pile up behind the front one, offset and scaled for depth; hovering expands them. When: Default behavior.
  - Always expanded: All toasts are visible at all times (the expand prop on <Toaster />). When: When you want to ensure all toasts are visible at all times.
  - Recommendation: Stacked is the default; use always-expanded when every toast must stay visible.
- In stacked mode, how should toasts of different heights be sized?
  - Natural heights: Toasts behind do not stick out evenly. When: Not recommended.
  - Match the front toast's height: The pile sticks out evenly. When: Always in stacked mode.
  - Recommendation: Make all toasts the height of the toast in front while stacked.
- What should count as a swipe that dismisses a toast?
  - Distance threshold only: People must drag past a set distance. When: Not what Sonner does: with distance only, a quick short swipe would not dismiss.
  - Momentum-based: Dismiss when distance reaches the threshold or velocity exceeds 0.11, so a quick short flick works. When: Default for swipe-to-dismiss.
  - Recommendation: Momentum-based, so a fast swipe dismisses even over a short distance.
- What happens when someone drags a toast the wrong way?
  - Block it: The toast stops immediately. When: Not recommended.
  - Friction: The toast still moves but slows down and eventually stops. When: Directions that do not dismiss.
  - Recommendation: Friction, because it is nicer than stopping the toast immediately.
- How should app code create toasts?
  - Hooks and React Context: Callers need hooks and React Context. When: Avoided by Sonner.
  - Global toast() function with an observer-pattern store: Insert <Toaster /> once and call toast() from anywhere; no hooks, no context. When: Recommended.
  - Recommendation: A global toast() function backed by the observer pattern; it is one of the two main reasons Sonner succeeded.
- Where should component documentation live and what should it show? (`Q-dist-04`)
  - Custom documentation site: Interactive examples people can play with, plus ready-to-use code snippets. When: When adoption and ease of use matter.
  - Docs as an afterthought: Loses what good docs give: a drastically lower barrier to use. When: Not recommended.
  - Recommendation: A fully custom docs site with interactive examples and copyable code, built with care rather than as an afterthought.
- Should a component library be named for its function or given a distinctive name?
  - Functional name: Clear and discoverable, but boring and generic (react-toast, react-snackbar, react-notifications). When: When discoverability matters most [inferred].
  - Distinctive word: Elegant and different, helps it stand out, but sacrifices discoverability and clarity. When: When you want it to stand out.
  - Recommendation: The author chose a distinctive word (Sonner, French for 'to ring') to stand out.

### Process

1. Name it: Look for a distinctive word related to the component's job (Sonner came from French words about notifications) instead of a function-based name.
2. Choose an interruptible technique: Use CSS transitions rather than keyframes so toasts can be retargeted while the pile changes.
3. Build the enter transition: Start at translateY(100%), flip a mounted flag after first render (or use @starting-style), transition transform 400ms ease to translateY(0).
4. Build the stack: Absolutely position toasts, offset each by gap times index, scale by 0.05 per step, and give all stacked toasts the front toast's height.
5. Add expand on hover: Compute each toast's offset from the heights of preceding toasts plus gaps; fill gaps with an :after pseudo-element; optionally allow always-expanded.
6. Add swipe to dismiss: Track pointer movement into a CSS variable, capture the pointer once dragging starts, add friction in the wrong direction, dismiss on distance threshold or velocity above 0.11.
7. Handle timers: Dismiss after 4 seconds by default; pause while hovered and while the tab is hidden.
8. Design the API: Use an observer-pattern store; insert <Toaster /> once; call toast() anywhere; add a promise API for loading, success and error.
9. Document it: Build interactive docs with live examples and ready-to-use code snippets.
10. Launch it: Make announcement videos that focus on the signature animation.

### Examples and visual references

- Sonner documentation page for toast() (sonner.emilkowal.ski): Screenshot of the docs: a left sidebar grouped into Basics, API (toast(), Toaster, Other) and Guides (Styling); a 'Toast' page with Preview and Code tabs and a Copy Code link; a live preview area containing a 'Render toast' button; an 'On this page' list (Rendering the toast, Success, Error, Action, Cancel, Promise, Loading, Custom, Headless, API Reference); and a light/dark/system theme switch at the bottom. It shows the interactive-example-plus-copyable-code approach to documentation.
- Keyframes vs transitions demo (Sonner (interactive demo in the article)): Adding toasts quickly with keyframes makes older toasts jump into place; with transitions they move smoothly to their new position.
- Stacking illustration (Sonner): Three toasts labelled Y(0) scale(1), Y(-14px) scale(0.95) and Y(-28px) scale(0.9), showing the offset and shrink that create depth.
- Different-heights demo (Sonner (interactive demo in the article)): Toasts of different heights in a stack, shown to explain why stacked toasts take the front toast's height.
- Quick swipe dismissal (Sonner (video in the article)): A short, fast swipe is enough to dismiss the toast.
- Hover gap fill (Sonner (interactive demo in the article)): Dark bars mark the :after pseudo-elements that fill the gaps between expanded toasts to keep the hover state.
- Hidden-tab pause (Sonner (video in the article)): The toast does not disappear while the tab is inactive.
- Pointer capture and friction (Sonner (video in the article)): The toast keeps responding to the drag with the pointer outside it, and dragging upwards slows and stops rather than being blocked.
- Always-expanded mode (Sonner (interactive demo in the article)): With the expand prop on <Toaster />, all toasts stay visible.

### Numbers

- 2023: Year Sonner was built. [Back in 2023, I decided to build a toast library called Sonner]
- 40,000,000: Weekly npm downloads of Sonner (over). [downloaded over 40,000,000 times per week from npm]
- 400ms: Duration of the transform transition (ease) used for toast enter. [transition : transform 400 ms ease]
- translateY(100%): Start position of the toast enter transition. [This makes the toast start at translateY(100%) and transition to translateY(0)]
- translateY(0): End position of the toast enter transition. [This makes the toast start at translateY(100%) and transition to translateY(0)]
- 0.05: Scale reduction per toast behind the front one (0.05 * index). [I also scale them down by 0.05 * index]
- -14px: Y offset of the first toast behind the front one in the stacking illustration; with -28px for the second, it implies a lift of 14px per step [inferred]. [Y(-14px)]
- -28px: Y offset of the second toast behind the front one in the stacking illustration. [Y(-28px)]
- 0.95: Scale of the first toast behind the front one (1 - 0.05). [scale(0.95)]
- 0.9: Scale of the second toast behind the front one (1 - 2 x 0.05). [scale(0.9)]
- 0.11: Swipe velocity (distance divided by elapsed time) above which a toast is dismissed; found by trial and error. [velocity is higher than in this case 0.11]
- 4 seconds: Default time before a toast disappears. [By default the toast disappears after 4 seconds]
- 3: States the promise API covers: loading, success, error. [specify what the toast should say in all 3 states]
- 2: Main reasons Sonner succeeded: developer experience and good looks. [There are two main reasons.]

<!-- /od:learn -->
