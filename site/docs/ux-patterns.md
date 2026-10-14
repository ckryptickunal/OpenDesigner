---
title: UX patterns, compared
seo_title: UX patterns compared: toasts, tooltips, errors and hover
description: Common interface patterns shown as Do and Don't pairs, from toasts and swipe to dismiss to tooltips, form errors, undo, drawers and hover on touch screens.
section: Craft
order: 2
updated: 2026-10-15
---

Each pattern on this page is shown twice: once in a way that works against people, and once in a way that works for them. The rule comes first, then the reason, then where it comes from. Many of the drawings are live, so hover over them, press them or tab through them.

Every rule here is an OpenDesigner house standard or one of its accessibility floors, and OpenDesigner applies them in every project. Most come from Emil Kowalski's writing on building Sonner, his toast library, and Vaul, his drawer library, and from his [emilkowalski/skills](https://github.com/emilkowalski/skills) repo. OpenDesigner is not affiliated with him.

## Toasts: where they sit and how long they stay

A toast is a short message that appears for a moment and then goes away on its own, such as "Link copied".

- **Put toasts in one corner, bottom-right by default.** Choose only from six places: the four corners and the top or bottom center. *(STD-components-toasts-drawers-29)*
- **Keep them 32 px from the screen edges, or 16 px on screens under 600 px wide.** *(STD-components-toasts-drawers-30)*
- **Show three at most, stacked with depth.** Each toast behind the front one sits 14 px higher and 5% smaller. Hovering the stack spreads it out with 14 px between toasts, and the gaps stay part of the hover area so the stack does not collapse as the pointer crosses them. The stack moves with Sonner's own timing, `transform 400ms ease`. That is slower than most interface motion, which the standards allow because it fits the component. *(STD-easing-duration-13, STD-components-toasts-drawers-14, STD-components-toasts-drawers-10, STD-components-toasts-drawers-12, STD-components-toasts-drawers-13)*
- **Close a toast after 4 seconds, but pause the timer while the pointer is over it or the tab is hidden.** Otherwise people lose a message they are reading, or one that arrived while they were elsewhere. *(STD-components-toasts-drawers-15, STD-components-toasts-drawers-16, STD-components-toasts-drawers-17)*
- **A toast with an action, such as Undo or Retry, stays until the person uses it or closes it.** A timer would put a time limit on the action. The standard bases this on WCAG's Timing Adjustable rule and marks it as OpenDesigner's own inference. *(STD-components-toasts-drawers-15)*

{{figure:craft-ux-toasts}}

Source: the [Sonner docs](https://sonner.emilkowal.ski/toaster) and Emil Kowalski's essay [Building a toast component](https://emilkowal.ski/ui/building-a-toast-component).

## Swipe to dismiss: speed counts, not only distance

**Dismiss when the swipe goes far enough or fast enough.** Speed here is the distance moved divided by the milliseconds since the drag began. Above 0.11, the element goes, however short the swipe. People should not have to drag past a fixed point. *(STD-springs-gestures-21)*

**Let people swipe it back the way it came.** The allowed swipe directions follow the toast's position, so the swipe heads back toward the edge it entered from. *(STD-components-toasts-drawers-18, STD-enter-exit-origin-06)*

{{figure:craft-ux-swipe}}

Source: Emil Kowalski's [Building a toast component](https://emilkowal.ski/ui/building-a-toast-component), where the 0.11 threshold was found by trial and error, and [Building a drawer component](https://emilkowal.ski/ui/building-a-drawer-component).

## No animation on keyboard actions

**Never animate an action started from the keyboard.** That covers shortcuts, opening a command menu (a search box of actions, often opened with Cmd K) and moving a highlight with the arrow keys. People repeat these hundreds of times a day, and any motion makes the interface lag behind their fingers. *(STD-when-to-animate-06)*

**Give no animation to anything used 100 or more times a day,** such as a launcher or a command menu. *(STD-when-to-animate-05)* When a review finds one, delete the animation before trying to tune it. *(STD-when-to-animate-17)*

{{figure:craft-ux-keyboard}}

Source: Emil Kowalski's [You don't need animations](https://emilkowal.ski/ui/you-dont-need-animations) and the animate and review-animations skills in emilkowalski/skills.

## Tooltips: only the first one waits

**Delay the first tooltip, then open its neighbors at once.** The delay stops tooltips from popping up when the pointer only passes by. Once one is open, the next opens with no delay and no animation, which makes the whole toolbar feel faster. In Base UI this is `transition-duration: 0ms` on tooltips marked `[data-instant]`. *(STD-enter-exit-origin-10)*

**A tooltip scales out of its trigger,** from scale(0.97) and opacity 0, over 125 ms on the house ease-out curve. *(STD-enter-exit-origin-09)*

{{figure:craft-ux-tooltips}}

The demo waits 500 ms before the first tooltip. The standards do not fix the length of that delay.

Source: Emil Kowalski's [7 practical animation tips](https://emilkowal.ski/ui/7-practical-animation-tips) and the animate recipes in emilkowalski/skills.

## Errors: next to the field, before submit

**Check form input inline, not on submit.** Feedback should come as soon as possible, so the interface feels like it is listening. *(STD-visual-details-49)* In the drawing, the message sits under the field it is about.

**Never show an error with color alone.** Add an icon or words, so people who cannot tell the colors apart still see it. This is one of the [accessibility floors](/docs/accessibility/).

{{figure:craft-ux-errors}}

Source: Emil Kowalski's [7 practical animation tips](https://emilkowal.ski/ui/7-practical-animation-tips) and the apple-design skill in emilkowalski/skills.

## Undo instead of "Are you sure?"

**Offer Undo for slips, and ask for confirmation only before destructive actions that cannot be undone.** Confirmation dialogs used too often train people to click straight through them. *(STD-visual-details-40)*

For a destructive action, a hold-to-confirm button is one option: see [Show the press](/docs/motion/#show-the-press). *(STD-components-toasts-drawers-77)*

{{figure:craft-ux-undo}}

Source: the apple-design skill in emilkowalski/skills.

## Drawers on phones

**On a phone, show secondary content in a drawer from the bottom edge instead of a centered dialog.** A drawer, also called a bottom sheet, feels more native on mobile. *(STD-components-toasts-drawers-37)*

**Open it on the drawer curve.** A web drawer moves from `translateY(100%)` to its place over 500 ms on `cubic-bezier(0.32, 0.72, 0, 1)`. The curve comes from the Ionic Framework and closely matches the iOS sheet. Once a finger drags the drawer, a spring takes over. *(STD-enter-exit-origin-41, STD-components-toasts-drawers-40)*

**Never trap people.** A drawer closes with a drag down, a tap outside or the Escape key. If one must stay open, give it a visible close button. *(STD-accessibility-motion-24, STD-components-toasts-drawers-39)*

{{figure:craft-ux-drawer}}

Source: Emil Kowalski's [Building a drawer component](https://emilkowal.ski/ui/building-a-drawer-component) and the [Vaul docs](https://vaul.emilkowal.ski/api). Vaul's README says the library is no longer maintained, so OpenDesigner treats its drawer craft as guidance and says so before suggesting it as a dependency.

## Hover only where there is a mouse

**Put every hover style inside `@media (hover: hover) and (pointer: fine)`.** Touch screens have no hover, so the browser fakes one: the first tap applies the hover style and leaves it there until you tap somewhere else. The press style, `:active`, is a real press on touch, so it stays outside the query. *(STD-accessibility-motion-15)*

**Detect touch by what the device can do, not by guessing from its name or screen width.** Laptops have touch screens and tablets have trackpads. *(STD-mobile-touch-02)*

{{figure:craft-ux-hover}}

Source: the mobile-native and animate skills in emilkowalski/skills.

## Loading spinners

No house standard chooses between skeleton screens and spinners, so this guide does not either. For spinners there are two rules. Make them spin fast, because a fast spinner makes the same wait feel shorter. And spin at a constant speed, with linear easing. *(STD-easing-duration-15, STD-easing-duration-01)*

## Where these rules come from

The standards cited here are listed with their sources in the [standards file](https://github.com/ckryptickunal/OpenDesigner/blob/main/skills/opendesigner/references/standards.md). [Who OpenDesigner learns from](/docs/resources/) describes every source and how one becomes a standard. For the motion behind these patterns, see [Motion that feels right](/docs/motion/).
