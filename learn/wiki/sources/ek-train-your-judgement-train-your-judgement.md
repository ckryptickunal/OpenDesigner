---
type: source
title: Train Your Judgement
created: 2026-09-27
updated: 2026-09-27
video_id: ek-train-your-judgement
url: https://emilkowal.ski/ui/train-your-judgement
channel: Emil Kowalski (web)
published: Unknown
authority: non-negotiable
tags:
  - judgement
  - taste
  - motion
  - animation-review
  - easing
  - interruptions
  - stagger
  - layered-motion
  - ai
---

# Train Your Judgement

## Metadata

- Page ID: `ek-train-your-judgement`
- Publisher: Emil Kowalski (web)
- Published: Unknown
- URL: https://emilkowal.ski/ui/train-your-judgement

## Summary

Emil Kowalski argues that AI can write animation code but cannot tell what feels right, so it produces motion that works yet feels mediocre, and people who cannot tell the difference ship it. The page is a set of interactive exercises: each shows two animations side by side, the reader picks the better one, writes down why, then reads the author's breakdown. The exercises cover the size of the animated element, easing, entry animations, being intentional, frequency of use, using scale, removing elements, handling interruptions, popovers, stagger and layered motion. For a design system this suggests a review bar: motion is not done when it works, it is done when someone has compared alternatives and can name why one feels better [inferred]. The captured text contains the exercise prompts and demo labels only, not the author's verdicts or values.

## Key Ideas

- AI can write animation code but cannot judge what feels right.
- Motion that merely works but feels mediocre should not be shipped; good enough is not good enough.
- Judgement is a trainable skill: spot what is wrong, name it, then fix it.
- Training method: compare two animations side by side, pick one, write down why, then check an expert breakdown.
- Putting into words why something feels right trains your ability to articulate judgement, which the author says will be incredibly valuable in the AI era.
- The dimensions the author trains are: element size, easing, entry animations, intentionality, frequency of use, scale, removing elements, interruptions, popovers, stagger and layered motion.
- Several exercises can only be judged by interacting with them: hovering through both lists, opening and closing each menu rapidly, and removing chips.
- How often an element is used is part of judging its animation.
- The author's design engineering skill file packages these rules so coding agents can follow them in practice.

## Entities

- [[entities/emil-kowalski|Emil Kowalski]] (person): Design engineer and author of the exercises and breakdowns.
- [[entities/aiforui-dev|aiforui.dev]] (product): The author's course, plugged at the top of the page (early access noted as closed).
- [[entities/animations-dev|animations.dev]] (product): The author's animation course for designers and engineers, plugged at the end.
- [[entities/design-engineering-skill-file|Design engineering skill file]] (tool): The author's skill file for coding agents, said to cover everything on the page and more.
- [[entities/judgement|Judgement]] (concept): The ability to spot what is wrong with motion, name it and fix it; the skill the page trains.

## Topics

- [[topics/design-taste-and-judgement|Design taste and judgement]]: Frames judgement as the skill AI lacks and trains it through side-by-side comparisons where the reader picks a variant, writes down why, and compares with the author's breakdown.
- [[topics/motion-principles|Motion principles]]: Lists the motion dimensions worth judging: element size, entry animations, intentionality, frequency of use, removing elements, interruptions, stagger and layered motion.
- [[topics/easing-and-timing|Easing and timing]]: One exercise is dedicated to choosing the right easing, using a toast as the example; the preferred curve is not in the captured text.
- [[topics/micro-interactions|Micro-interactions]]: Exercises on a button press ('Using scale properly') and hovering through an options list judged for frequent use.
- [[topics/toasts-and-notifications|Toasts and notifications]]: A toast animation is the example for choosing the right easing.
- [[topics/modals-and-popovers|Modals and popovers]]: Exercises compare dialog entrance animations and popover animations triggered by a button.
- [[topics/navigation-and-sidebars|Navigation and sidebars]]: A mobile menu is used for the element-size and interruption exercises, and a side panel over a dashboard for layered motion.
- [[topics/landing-pages|Landing pages]]: A hero section (announcement pill, headline, subtext, two buttons) is the example for judging whether a staggered entrance feels intentional.
- [[topics/ai-assisted-design|AI-assisted design]]: AI-generated motion tends to work but feel mediocre; articulating why something feels right is presented as a key skill in the AI era, and the skill file lets coding agents follow the rules.
- [[topics/design-process|Design process]]: Gives a training loop for motion judgement: compare two variants, interact with them, pick one, write down the reason, then compare with the author's breakdown.

## Notable Claims

- AI can write animation code but cannot know what feels right. Evidence: opening: 'AI can write animation code'
- AI produces motion that works but feels mediocre, and if you cannot tell the difference you will ship it and settle for good enough. Evidence: 'It produces motion that works, but feels mediocre'
- Putting into words why something feels right trains your ability to articulate judgement, a skill the author says will be incredibly valuable in the AI era. Evidence: 'Putting into words why something feels right'
- The exercises train the ability to spot what is wrong, name it and fix it. Evidence: 'This article trains your ability to spot what’s wrong'
- Everything covered on the page, and more, is in the author's design engineering skill file, which can be fed to coding agents. Evidence: Going a step further

## Quotes

> What it can’t do is know what feels right
> It produces motion that works, but feels mediocre
> You’ll settle for good enough, and that’s not good enough.

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: The captured text holds only the exercise headings, prompts and demo labels. The interactive demos and the author's breakdowns (which variant is better, why, and any durations, curves or scale values) were not captured, so the per-exercise rules state the criterion and the test method only, not the preferred answer. A re-capture that includes the revealed breakdowns is needed to extract the actual values.
- Caveat: Because the verdicts are missing, rules marked 'consider' name a dimension to judge rather than a settled house standard.
- Caveat: The page opens with a plug for the author's course aiforui.dev (early access noted as closed) and ends with a plug for animations.dev, described as teaching practical animation techniques to make products feel cleaner, faster and more polished; both are self-promotion, not guidance.
- Caveat: The 'design engineering skill file' is referenced without a link in the captured text; that it is the emilkowalski/skills repository is an assumption [inferred].
- Caveat: The claim that articulating judgement will be incredibly valuable in the AI era is the author's opinion, not a measured finding.
- Caveat: Publication date is not given (header says Unknown).

### Rules and practices

- **must** (motion, all): Do not ship animation code, including AI-written code, just because it works; check that the motion feels right before shipping. Why: AI produces motion that works but feels mediocre; if you cannot tell the difference you will ship it and settle for good enough, which is not good enough. [opening: 'It produces motion that works, but feels mediocre']
- **should** (process, all): When reviewing motion, spot what is wrong, name the problem in words, and then fix it. Why: This is the ability the author says the exercises train. ['trains your ability to spot what’s wrong, name it, and fix it']
- **should** (process, all): To train motion judgement, compare two animations side by side and pick the better one. Why: This is the format of every exercise the author uses to train judgement. ['Each exercise shows two animations side by side']
- **should** (process, all): Write down why you chose a variant before reading an expert breakdown, then compare your reasoning with it. Why: Putting into words why something feels right trains your ability to articulate judgement, which the author calls incredibly valuable in the AI era. ['write down why you chose it, and then see my breakdown']
- **should** (tooling, all): Give coding agents Emil Kowalski's design engineering skill file so they follow these animation rules in practice. Why: The author says everything on the page, and more, is covered in that skill file for coding agents. [Going a step further]
- **should** (motion, all): Test menu animations for interruptions by opening and closing the menu rapidly, and prefer the version that handles interruption better. Why: Handling interruptions is one of the author's judgement exercises, and rapid open and close is how he asks readers to test it. [Handling interruptions: 'Open and close each menu rapidly']
- **should** (motion, all): Judge the hover animation of a frequently used list, such as an options menu, by hovering through the whole list and choosing what feels better for frequent use. Why: Frequency of use is one of the author's judgement exercises; he asks which feels better for something you would use frequently. [Frequency of use: 'Hover through both lists']
- **consider** (motion, all): Take the size of the animated element into account when choosing its animation, for example a mobile menu. Why: Size of an element is one of the author's judgement exercises; the preferred variant is not in the captured text. [Size of an element: 'Which mobile menu animation feels better?']
- **consider** (motion, all): Choose the easing for a toast animation deliberately, comparing variants and picking the one that feels better. Why: Choosing the right easing is one of the author's judgement exercises, shown on a toast; the preferred curve is not in the captured text. [Choosing the right easing: 'Which toast animation feels better?']
- **consider** (motion, all): Treat a dialog's entrance animation as its own decision and compare entrances before choosing one. Why: Entry animations is one of the author's judgement exercises, shown on an 'Open dialog' button; the preferred variant is not in the captured text. [Entry animations: 'Click both buttons. Which entrance feels better?']
- **consider** (motion, all): Be intentional about how an accordion animates when it opens and closes. Why: Being intentional is one of the author's judgement exercises, shown on an FAQ accordion; the preferred variant is not in the captured text. [Being intentional: 'Which accordion animation feels better?']
- **consider** (motion, all): Use scale deliberately in button press feedback, comparing press variants before choosing one. Why: Using scale properly is one of the author's judgement exercises, shown on a Subscribe button; the preferred scale is not in the captured text. [Using scale properly: 'Which press feels better?']
- **should** (motion, all): Make removing elements, such as chips, feel smooth, and judge it by actually removing chips in both variants. Why: Removing elements is one of the author's judgement exercises, and smoothness is the criterion he asks readers to judge by. [Removing elements: 'Remove chips on both sides. Which feels smoother?']
- **consider** (motion, all): Compare popover animation variants by clicking the trigger button before choosing how a popover animates. Why: Animating popovers is one of the author's judgement exercises, shown on a 'Show details' button; the preferred variant is not in the captured text. [Animating popovers: 'Which popover feels better?']
- **consider** (motion, all): When staggering a hero section's entrance, judge the stagger by whether the entrance feels intentional. Why: Using stagger is one of the author's judgement exercises, and 'more intentional' is the criterion he asks readers to judge by. [Using stagger: 'Which entrance feels more intentional?']
- **consider** (motion, all): Consider layered motion when animating a side panel opening over a page such as a dashboard. Why: Layered motion is one of the author's judgement exercises, shown on a side panel over a dashboard; the preferred variant is not in the captured text. [Layered motion: 'Open the side panel on both']

### Process

1. Set up two variants: Build or find two versions of the same animation and place them side by side (the source provides the pairs; building your own is an adaptation) [inferred].
2. Interact with both: Use each the way the exercises ask: click the trigger, hover through the list, open and close the menu rapidly, or remove chips.
3. Pick the better one: Choose the variant that feels better for the stated criterion, such as smoother, more intentional, better under interruption, or better for frequent use.
4. Write down why: Put into words why the chosen variant feels right before looking at any expert opinion.
5. Compare with a breakdown: Read an expert breakdown and compare it with your reasoning.
6. Apply to real work: In your own motion, spot what is wrong, name it and fix it; give coding agents the design engineering skill file so they follow the same rules.

### Examples and visual references

- Mobile menu opening (demo site labelled 'Acme'): A mobile menu over page content, used for the element-size exercise and again for handling interruptions (open and close rapidly).
- Toast triggered by a 'Show toast' button: Two toast animations compared to teach choosing the right easing.
- Dialog opened by an 'Open dialog' button: Two dialog entrance animations compared for the entry-animations exercise.
- FAQ accordion ('How does billing work?'): An accordion revealing a short billing answer, used for the being-intentional exercise.
- Options menu (Edit, Copy Link, Move to…, Duplicate, Archive, Delete): Two hover treatments on a menu list, judged for something used frequently.
- Subscribe button press: Two press animations compared for using scale properly.
- Removable chips (React, Next.js, Tailwind, Motion): Chips removed on each side, judged by which feels smoother.
- Popover from a 'Show details' button: Two popover animations compared for the animating-popovers exercise.
- Hero section entrance: An announcement pill ('New – Collaborative workspaces →'), headline 'Ship products that matter', two lines of subtext and 'Get started' and 'Explore' buttons, compared for the stagger exercise; judged by which entrance feels more intentional.
- Side panel over a dashboard: A side panel opening over a page titled 'Dashboard', used for the layered-motion exercise.

<!-- /od:learn -->
