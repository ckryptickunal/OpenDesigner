---
title: Motion that feels right
seo_title: Motion that feels right: easing, duration and origin rules
description: The motion rules every OpenDesigner system follows, with live demos: when to animate, easing, durations under 300 ms, origin, stagger and reduced motion.
section: Craft
order: 1
updated: 2026-10-15
---

Motion in an interface has a job. It shows what changed, where something came from, or that a press was heard. This page shows the motion rules every OpenDesigner design system follows, each with a demo you can watch or touch.

The rules are house standards. OpenDesigner applies them in every project, locks them and writes them into DESIGN.md, and `engine.py review` flags code that breaks the ones it can check. Each rule names its standard id, so you can look it up in the [standards file](https://github.com/ckryptickunal/OpenDesigner/blob/main/skills/opendesigner/references/standards.md). Most of them come from the published work of Emil Kowalski, a design engineer who wrote the Sonner and Vaul libraries and teaches the [animations.dev](https://animations.dev/) course.

Every demo is plain CSS. Hover over a demo, tap it or move keyboard focus to it, and it pauses. If your device asks for reduced motion, the demos rest on their last frame.

## Should it move at all?

**Decide whether something should animate before you pick a curve.** Two questions come first: how often will people see it, and what is the motion for? If either answer is weak, ship no animation. *(STD-when-to-animate-01)*

**The more often people see something, the less it should move.** Something used a hundred times a day gets no animation. Something seen tens of times a day gets almost none. Modals, drawers and toasts, seen now and then, get standard motion. Only rare moments, like onboarding or a first success, get motion whose job is delight. Repeated motion stops being pleasant and starts to slow people down. *(STD-when-to-animate-04, STD-when-to-animate-05, STD-when-to-animate-07, STD-when-to-animate-08, STD-when-to-animate-09)*

{{figure:craft-motion-frequency}}

**Name the purpose.** Valid purposes are feedback, keeping things spatially consistent, showing a change of state, avoiding a jarring jump, explaining how something works, and delight in rare moments. "It looks cool" is not one. *(STD-when-to-animate-03)*

Source: Emil Kowalski's essay [You don't need animations](https://emilkowal.ski/ui/you-dont-need-animations), where a launcher opened hundreds of times a day is better with no open or close animation, and the animate skill in his [emilkowalski/skills](https://github.com/emilkowalski/skills) repo.

## Pick the curve by the motion's job

Easing is how the speed changes during a motion: fast at first and slow at the end, or the other way round. **Pick it by what the motion does**, in this order: *(STD-easing-duration-01)*

| The element | Easing |
|---|---|
| enters or leaves the screen | ease-out |
| moves or changes shape on screen | ease-in-out |
| changes color, or reacts to hover | ease |
| moves at a constant rate, like a spinner or a progress bar | linear |
| none of these | ease-out |

**Never use ease-in on interface motion.** Ease-in starts slowly, so the first moment, the one people watch most closely, looks like nothing is happening. A shorter duration does not fix it; switch to ease-out. *(STD-easing-duration-03)*

{{figure:craft-motion-easing}}

**Use strong custom curves, not the built-in ones.** The built-in CSS curves are too gentle to feel intentional; only the `ease` and `linear` keywords stay allowed. These are OpenDesigner's house curves: *(STD-easing-duration-02, STD-components-toasts-drawers-40)*

```
--ease-out:    cubic-bezier(0.23, 1, 0.32, 1);    /* entering and leaving */
--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);   /* moving on screen */
--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);    /* drawers and sheets */
```

The rest of this guide calls the first one the house ease-out curve. If you need a different curve, take one from [easing.dev](https://easing.dev/) or [easings.co](https://easings.co/) instead of drawing your own.

Source: Emil Kowalski's [7 practical animation tips](https://emilkowal.ski/ui/7-practical-animation-tips) and the emil-design-eng and animate skills in emilkowalski/skills.

## Keep it short

**Interface motion stays under 300 ms.** Short motion stays connected to what the person did. A 180 ms dropdown feels more responsive than a 400 ms one. Anything longer needs a stated reason, such as a drawer that copies the iOS sheet. *(STD-easing-duration-06)*

{{figure:craft-motion-duration}}

**Each kind of element has its own budget:** *(STD-easing-duration-07)*

| Element | Duration |
|---|---|
| Button press feedback | 100–160 ms |
| Tooltips and small popovers | 125–200 ms |
| Dropdowns and selects | 150–250 ms |
| Modals and drawers | 200–500 ms |

Bigger elements and longer distances get longer durations. *(STD-easing-duration-10)* Nothing runs past 1 second unless it explains something, as on a marketing page. *(STD-easing-duration-09)* Loading spinners spin fast, because a fast spinner makes the same wait feel shorter. *(STD-easing-duration-15)*

## Never start from nothing

**Never animate from scale(0).** Nothing in the real world appears out of a single point. Start from scale(0.95) with opacity 0, or anywhere from 0.9 to 0.97. *(STD-enter-exit-origin-01)*

**Do not fade in with opacity alone, either.** Give every entrance a slightly smaller scale or a short slide as well. The two exceptions are reduced motion and the dimmed backdrop behind a modal. *(STD-enter-exit-origin-02)*

{{figure:craft-motion-scale}}

## Grow out of the trigger

**Popovers, dropdowns, menus and tooltips grow from the element that opened them.** The point an element grows from is its `transform-origin`. CSS puts it in the center unless you say otherwise, which is wrong for almost every popover. Set it to the trigger; libraries such as Base UI expose it as `var(--transform-origin)`. *(STD-enter-exit-origin-03)*

**Modals are the exception.** A modal is not anchored to a button on screen, so it stays centered. *(STD-enter-exit-origin-04)*

{{figure:craft-motion-origin}}

The house recipes: dropdowns enter from scale(0.95) over 200 ms, tooltips from scale(0.97) over 125 ms, and modals from scale(0.96) over 250 ms, all with opacity and on the house ease-out curve. *(STD-enter-exit-origin-08, STD-enter-exit-origin-09, STD-enter-exit-origin-11)*

## Show the press

**Every pressable element scales to 0.97 while it is pressed.** On the web that is the `:active` state, over 100 to 160 ms on the house ease-out curve. The whole button shrinks, label and icon included, so the press feels physical. *(STD-mobile-touch-05)*

**Show feedback when the finger goes down, and act when it lifts.** Waiting for the click to finish feels dead, even when nothing is slow. *(STD-components-toasts-drawers-72)*

{{figure:craft-motion-press}}

**Be slow where people decide and fast where the system answers.** A hold-to-confirm button fills over 2 seconds while held and snaps back in 200 ms when released. Use it for a destructive action that a plain click would fire too easily. *(STD-easing-duration-12, STD-components-toasts-drawers-77)*

{{figure:craft-motion-hold}}

Source: Emil Kowalski's [7 practical animation tips](https://emilkowal.ski/ui/7-practical-animation-tips) and the animate, mobile-native and apple-design skills in emilkowalski/skills.

## Leave the way you came, a little faster

**Leave along the path you came in on.** A toast that rises from the bottom leaves through the bottom, and that is also the direction a swipe should dismiss it. Entering from one edge and leaving by another reads as two unrelated things. *(STD-enter-exit-origin-06)*

**Make exits about 20% faster than entrances.** The person has already read the content. A 300 ms entrance leaves in 250 ms. *(STD-easing-duration-11)*

{{figure:craft-motion-toast}}

## Stagger groups by 30 to 80 ms

**When several items enter together, start each one 30 to 80 ms after the one before.** A cascade feels more natural than everything appearing at once. Longer gaps feel slow, and shorter ones look simultaneous. The house recipe uses 50 ms. *(STD-enter-exit-origin-13)*

**Keep the items usable while they cascade, and skip the entrance on lists people use all day.** A list someone scrolls past many times should already be there. *(STD-springs-gestures-13, STD-when-to-animate-13)*

{{figure:craft-motion-stagger}}

## Let people change their minds mid-motion

**Use CSS transitions, not keyframe animations, for anything people can trigger quickly.** A keyframe animation is a motion written as fixed frames with `@keyframes`. It always restarts from its first frame, so a toggle flipped twice jumps. A transition starts from wherever the element is. *(STD-springs-gestures-15)*

**Use springs for anything a finger drags.** A spring is motion driven by simple physics instead of a fixed duration. It keeps its speed when interrupted, so a sheet grabbed while it closes follows the finger. *(STD-springs-gestures-01, STD-springs-gestures-12)*

{{figure:craft-motion-interrupt}}

Source: Emil Kowalski's [Building a toast component](https://emilkowal.ski/ui/building-a-toast-component), which explains why Sonner uses transitions, and the apple-design skill in emilkowalski/skills.

## Animate only transform and opacity

**Move, resize and show things with `transform` and `opacity` only.** Other properties make the browser redo layout and paint on every frame, and the motion stutters when the page is busy. *(STD-performance-properties-01)* The only exceptions are `clip-path` for reveals, `height` for accordions, and `width` on an absolutely positioned element with no children. *(STD-performance-properties-02)*

**Never write `transition: all`.** Name the exact properties that change. *(STD-performance-properties-06)*

{{figure:craft-motion-properties}}

Source: the [performance cheatsheet](https://github.com/emilkowalski/skills/blob/85e8e23/performance-cheatsheet.md) and the animate skill in emilkowalski/skills.

## Reduced motion means gentler, not none

Some people set their device to reduce motion, because movement on screen can make them feel sick. **Ship the reduced version in the same change as the animation, never later.** *(STD-accessibility-motion-01)*

**Remove movement and keep the fades.** With reduced motion on, drop slides, scaling, springs and parallax. Keep the opacity and color changes that explain what changed, as a short cross-fade of about 200 ms. Turning every animation off also removes feedback people still need. *(STD-accessibility-motion-02)*

{{figure:craft-motion-reduced}}

**Gate hover motion to devices that can hover.** See [Hover only where there is a mouse](/docs/ux-patterns/#hover-only-where-there-is-a-mouse). *(STD-accessibility-motion-15)*

## Check it before you ship it

Motion can be correct in code and still feel wrong. Before you call it done:

- Play it at two to five times its length, or step through it frame by frame in the browser's animation tools. Look for the wrong origin, an abrupt start or stop, and properties that drift out of step. *(STD-process-review-taste-30)*
- Use it the way people will: open and close it fast, flip the toggle again and again, hover down the whole list. *(STD-process-review-taste-32)*
- Look at it again the next day. *(STD-process-review-taste-31)*
- Try anything touched or dragged on a real phone. A small desktop window or a device emulator does not count. *(STD-process-review-taste-33)*
- Turn on reduced motion and check that the movement is gone and the fades remain. *(STD-accessibility-motion-05)*

## Where these rules come from

The rules on this page are OpenDesigner house standards, version 3. Most come from Emil Kowalski's essays at [emilkowal.ski](https://emilkowal.ski/), the public pages of [animations.dev](https://animations.dev/) and his [emilkowalski/skills](https://github.com/emilkowalski/skills) repo. OpenDesigner is not affiliated with or endorsed by him; it cites his work because that work shaped these standards. [Who OpenDesigner learns from](/docs/resources/) lists every source and explains how one becomes a standard.
