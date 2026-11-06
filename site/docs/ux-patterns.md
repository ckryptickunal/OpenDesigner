---
title: UX patterns, compared
seo_title: UX patterns compared: toasts, tooltips, errors and hover
description: Common interface patterns shown as Do and Don't pairs, from toasts and swipe to dismiss to tooltips, form errors, undo, drawers and hover on touch screens.
section: Craft
order: 2
updated: 2026-11-07
---

Each pattern is shown twice: once working against people, once working for them. Many drawings are live, so hover, press or tab through them.

Every rule here is an OpenDesigner house standard or [accessibility floor](/docs/accessibility/), applied in every project. Most come from Emil Kowalski's writing on Sonner, his toast library, and Vaul, his drawer library, and from his [emilkowalski/skills](https://github.com/emilkowalski/skills) repo. OpenDesigner is not affiliated with him.

## Toasts: where they sit and how long they stay

A toast is a short message that appears for a moment and goes away on its own, such as "Link copied".

**Put toasts in one corner, bottom-right by default,** choosing only from the four corners and the top or bottom center. *(STD-components-toasts-drawers-29)* Keep them 32 px from the screen edges, or 16 px on screens under 600 px wide. *(STD-components-toasts-drawers-30)*

**Show three at most, stacked with depth.** Each toast behind the front one sits 14 px higher and 5% smaller. Hovering spreads the stack with 14 px gaps that stay part of the hover area, so it doesn't collapse under the pointer. The stack moves with Sonner's `transform 400ms ease`, longer than the 300 ms limit and allowed for this component. *(STD-easing-duration-13, STD-components-toasts-drawers-14, STD-components-toasts-drawers-10, STD-components-toasts-drawers-12, STD-components-toasts-drawers-13)*

**Close a toast after 4 seconds, but pause the timer while the pointer is over it or the tab is hidden,** so people don't lose a message they're reading. *(STD-components-toasts-drawers-15, STD-components-toasts-drawers-16, STD-components-toasts-drawers-17)* **A toast with an action, such as Undo, stays until it's used or closed,** so the action has no time limit. This one is OpenDesigner's inference from WCAG's Timing Adjustable rule. *(STD-components-toasts-drawers-15)*

{{figure:craft-ux-toasts}}

Source: the [Sonner docs](https://sonner.emilkowal.ski/toaster) and Emil Kowalski's essay [Building a toast component](https://emilkowal.ski/ui/building-a-toast-component).

## Swipe to dismiss: speed counts, not only distance

**Dismiss when the swipe goes far enough or fast enough.** Speed is the distance moved divided by the milliseconds since the drag began; above 0.11 the element goes, however short the swipe. *(STD-springs-gestures-21)* **Let people swipe it back toward the edge it came from.** *(STD-components-toasts-drawers-18, STD-enter-exit-origin-06)*

{{figure:craft-ux-swipe}}

Source: Emil Kowalski's [Building a toast component](https://emilkowal.ski/ui/building-a-toast-component) and [Building a drawer component](https://emilkowal.ski/ui/building-a-drawer-component).

## No animation on keyboard actions

**Never animate an action started from the keyboard:** shortcuts, opening a command menu (a search box of actions, often Cmd K) or moving a highlight with the arrow keys. People repeat these hundreds of times a day, and any motion lags behind their fingers. *(STD-when-to-animate-06)* The same goes for anything used 100 or more times a day ([Should it move at all?](/docs/motion/#should-it-move-at-all)). *(STD-when-to-animate-05)* When a review finds one animated, delete the animation before trying to tune it. *(STD-when-to-animate-17)*

{{figure:craft-ux-keyboard}}

Source: Emil Kowalski's [You don't need animations](https://emilkowal.ski/ui/you-dont-need-animations) and the animate and review-animations skills in emilkowalski/skills.

## Tooltips: only the first one waits

**Delay the first tooltip, then open its neighbors at once,** with no delay and no animation; the toolbar feels faster. In Base UI that is `transition-duration: 0ms` on tooltips marked `[data-instant]`. *(STD-enter-exit-origin-10)* A tooltip scales out of its trigger from scale(0.97) and opacity 0, over 125 ms on the house ease-out curve. *(STD-enter-exit-origin-09)*

{{figure:craft-ux-tooltips}}

The demo waits 500 ms before the first tooltip; the standards don't fix that delay.

Source: Emil Kowalski's [7 practical animation tips](https://emilkowal.ski/ui/7-practical-animation-tips) and the animate recipes in emilkowalski/skills.

## Errors: next to the field, before submit

**Check form input inline, not on submit,** so the interface feels like it is listening. *(STD-visual-details-49)* **Never show an error with color alone:** add an icon or words, so people who can't tell the colors apart still see it. This is an accessibility floor.

{{figure:craft-ux-errors}}

Source: Emil Kowalski's [7 practical animation tips](https://emilkowal.ski/ui/7-practical-animation-tips) and the apple-design skill in emilkowalski/skills.

## Undo instead of "Are you sure?"

**Offer Undo for slips, and confirm only destructive actions that can't be undone.** Dialogs shown too often train people to click straight through them. *(STD-visual-details-40)* For a destructive action, a [hold-to-confirm button](/docs/motion/#show-the-press) is one option. *(STD-components-toasts-drawers-77)*

{{figure:craft-ux-undo}}

Source: the apple-design skill in emilkowalski/skills.

## Drawers on phones

**On a phone, show secondary content in a drawer from the bottom edge (a bottom sheet) instead of a centered dialog.** *(STD-components-toasts-drawers-37)* It moves from `translateY(100%)` over 500 ms on `cubic-bezier(0.32, 0.72, 0, 1)`, a curve from the Ionic Framework close to the iOS sheet, and a spring takes over once a finger drags it. *(STD-enter-exit-origin-41, STD-components-toasts-drawers-40)*

**Never trap people.** A drawer closes with a drag down, a tap outside or Escape; one that must stay open gets a visible close button. *(STD-accessibility-motion-24, STD-components-toasts-drawers-39)*

{{figure:craft-ux-drawer}}

Source: Emil Kowalski's [Building a drawer component](https://emilkowal.ski/ui/building-a-drawer-component) and the [Vaul docs](https://vaul.emilkowal.ski/api). Vaul's README says it is no longer maintained, so OpenDesigner says so before suggesting it as a dependency.

## Hover only where there is a mouse

**Put every hover style inside `@media (hover: hover) and (pointer: fine)`.** Touch screens fake hover: the first tap applies the hover style and leaves it there. `:active` is a real press on touch, so it stays outside the query. *(STD-accessibility-motion-15)* **Detect touch by what the device can do,** not its name or screen width: laptops have touch screens and tablets have trackpads. *(STD-mobile-touch-02)*

{{figure:craft-ux-hover}}

Source: the mobile-native and animate skills in emilkowalski/skills.

## Loading spinners

No house standard chooses between skeleton screens and spinners, so this guide doesn't either. Spinners spin fast and at a constant speed ([Keep it short](/docs/motion/#keep-it-short)). *(STD-easing-duration-15, STD-easing-duration-01)*

## Where these rules come from

The [standards file](https://github.com/ckryptickunal/OpenDesigner/blob/main/skills/opendesigner/references/standards.md) lists each standard with its sources, and [Who OpenDesigner learns from](/docs/resources/) describes every source.
