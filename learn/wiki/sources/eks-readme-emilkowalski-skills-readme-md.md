---
type: source
title: "emilkowalski/skills: README.md"
created: 2026-09-27
updated: 2026-09-27
video_id: eks-readme
url: https://github.com/emilkowalski/skills/blob/85e8e23/README.md
channel: emilkowalski/skills (GitHub, MIT)
published: commit 85e8e23
authority: non-negotiable
tags:
  - agent-skills
  - ai-taste
  - easing
  - ease-out
  - shadows
  - borders
  - ui-libraries
  - mobile-web
  - react-native
  - prototyping
  - animation-review
---

# emilkowalski/skills: README.md

## Metadata

- Video ID: `eks-readme`
- Channel: emilkowalski/skills (GitHub, MIT)
- Published: commit 85e8e23
- URL: https://github.com/emilkowalski/skills/blob/85e8e23/README.md

## Summary

The README of Emil Kowalski's skills repository explains why the skills exist and lists what each one does. Its core argument is that AI agents lack taste: they pick ease-in for an enter animation where ease-out is right, or a solid border where a semi-transparent shadow is right, and these small mistakes compound. The skills encode the author's experience at Vercel and Linear as lists of such mistakes and their fixes, so agents reach the right design and animation decisions faster. It frames AI as an amplifier of domain expertise, not a replacement. For a design system, it supplies two concrete defaults (ease-out for enter, shadows over solid borders), a map of which skill handles which job (build, review, audit, find opportunities, name effects, pick libraries, prototype, mobile polish), and the install command.

## Key Ideas

- Knowing whether an animation or design choice is right is hard; these skills aim to shorten the path to the right decision.
- AI agents do not have great taste and often pick the wrong ingredients for an animation.
- Enter animations should use ease-out; agents often wrongly use ease-in.
- A semi-transparent shadow is the better choice where agents reach for a solid border.
- Small wrong choices compound until an interface is either amazing or just not that great.
- The skills list the small mistakes agents make and explain how to fix them.
- AI amplifies domain expertise rather than replacing it, so learning to code or design stays valuable.
- Each skill covers one job: build an animation, review strictly, audit a codebase, find where motion helps, name effects, pick a library, prototype variants, or make web apps feel native on phones.
- Agents should use trusted libraries instead of hand-rolling components like toasts or installing abandoned packages.

## Entities

- [[entities/emil-kowalski|Emil Kowalski]] (person): Author of the skills, drawing on years at Vercel and Linear
- [[entities/vercel|Vercel]] (company): Company where the author gained the experience the skills are based on
- [[entities/linear|Linear]] (company): Company where the author gained the experience the skills are based on
- [[entities/emilkowalski-skills|emilkowalski/skills]] (product): MIT-licensed GitHub repository of agent skills described by this README (commit 85e8e23)
- [[entities/animations-dev|animations.dev]] (product): The author's site, linked from the header image and hosting the skills newsletter signup
- [[entities/skills-sh|skills.sh]] (tool): Badge at the top of the README linking to skills.sh/emilkowalski/skills; the install command uses the npx package skills@latest
- [[entities/agents-with-taste|Agents with Taste]] (product): The author's piece at emilkowal.ski/ui/agents-with-taste, cited for the point that these skills list agents' little mistakes and how to fix them
- [[entities/7-practical-animation-tips|7 Practical Animation Tips]] (product): The author's piece at emilkowal.ski/ui/7-practical-animation-tips, linked (section 4, choose the right easing) for why enter animations use ease-out
- [[entities/sonner|Sonner]] (library): The author's toast library, covered by the ask-sonner skill
- [[entities/emil-design-eng|emil-design-eng]] (tool): Main skill, mostly animation plus some design advice
- [[entities/animate|animate]] (tool): Skill that builds an animation from scratch, choosing curve, duration and properties
- [[entities/animate-expo|animate-expo]] (tool): Same bar for React Native and Expo: gestures, sheets, haptics, screen transitions, motion off the JS thread
- [[entities/review-animations|review-animations]] (tool): Skill that reviews animations strictly against the author's rules
- [[entities/improve-animations|improve-animations]] (tool): Skill that audits all animations in a codebase and writes prioritized, self-contained plans
- [[entities/find-animation-opportunities|find-animation-opportunities]] (tool): Skill that finds where motion genuinely helps and says what not to animate
- [[entities/animation-vocabulary|animation-vocabulary]] (tool): Skill that gives the right words to describe an animation to an AI
- [[entities/apple-design|apple-design]] (tool): Apple's interface and fluid-motion principles from WWDC design talks, translated for the web
- [[entities/write-swift|write-swift]] (tool): Skill for modern Swift: value types, Swift 6 concurrency, generics, performance, Swift Testing
- [[entities/pick-ui-library|pick-ui-library]] (tool): Skill that picks a trusted library instead of hand-rolling components or installing abandoned packages
- [[entities/prototype|prototype]] (tool): Skill that builds several versions of a UI piece and lets you compare them with a switcher
- [[entities/mobile-native|mobile-native]] (tool): Skill with small fixes that make a web app feel native on a phone
- [[entities/ask-sonner|ask-sonner]] (tool): Guide to Sonner: setup, styling, recipes and common fixes
- [[entities/ease-out|ease-out]] (concept): Easing the README says enter animations should use
- [[entities/ease-in|ease-in]] (concept): Easing agents wrongly pick for enter animations

## Topics

- [[topics/ai-assisted-design|AI-assisted design]]: Agents lack taste and make small, compounding mistakes; the skills list those mistakes and their fixes, and AI amplifies expertise rather than replacing it.
- [[topics/design-taste-and-judgement|Design taste and judgement]]: Judging whether a choice is right is hard; small ingredients compound into an amazing or mediocre interface.
- [[topics/easing-and-timing|Easing and timing]]: Enter animations should use ease-out, not ease-in, which agents often get wrong.
- [[topics/depth-shadows-and-borders|Depth, shadows and borders]]: Agents choose a solid border where a semi-transparent shadow is the better ingredient.
- [[topics/motion-principles|Motion principles]]: Skills exist to build animations (curve, duration, properties), review them strictly, audit them, find where motion genuinely helps and decide what not to animate.
- [[topics/ui-libraries|UI libraries]]: Agents should pick trusted libraries instead of hand-rolling a toast component or installing an abandoned package; Sonner is the author's toast library.
- [[topics/toasts-and-notifications|Toasts and notifications]]: A toast component should come from a trusted library such as Sonner rather than be hand-rolled by AI [inferred].
- [[topics/mobile-app-patterns|Mobile app patterns]]: Web apps on phones need fixes for sticky hover states, tap highlight flashes, the 100vh bug, zooming inputs, laggy taps and safe areas; React Native/Expo motion should stay off the JS thread.
- [[topics/prototyping|Prototyping]]: Build several versions of a UI piece and switch between them to compare.
- [[topics/design-resources|Design resources]]: Index of the author's skills, with install command and newsletter.

## Notable Claims

- Knowing whether you made the right choice in animation or design is hard, and the skills aim to get you to the right decisions faster. Evidence: Knowing whether you made a right choice
- The skills are based on the author's years of experience working at companies like Vercel and Linear. Evidence: They are based on my years of experience
- AI does not replace domain expertise; it amplifies what you can get out of it and makes you better relative to others. Evidence: All the skills here are a side-effect of domain-expertise
- Agents don't have great taste and often don't pick the right ingredients for an animation. Evidence: Why use it?
- Agents use ease-in for enter animations when they should use ease-out. Evidence: An `ease-in` easing for an enter animation
- Agents choose a solid border instead of a semi-transparent shadow for UIs. Evidence: solid border instead of a semi-transparent shadow
- Small choices compound and make an interface either amazing or just not that great. Evidence: All these small things compound
- The skills list the little mistakes agents can make and explain how to fix them. Evidence: As explained in [Agents with Taste]
- Left alone, AI may hand-roll a toast component or install an abandoned package; pick-ui-library makes the agent pick from libraries the author uses and trusts instead. Evidence: pick-ui-library
- The apple-design skill is distilled from Apple's WWDC design talks and translated for the web. Evidence: apple-design
- Sticky hover states, tap highlight flashes, the 100vh bug, inputs that zoom the page, laggy taps and safe areas are among the small fixes that separate a website from an app on a phone. Evidence: mobile-native

## Quotes

> Agents don’t have great taste
> AI doesn’t replace such expertise, it amplifies what you can get out of it
> A shortcut to stand out in a sea of slop.

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: Contains self-promotion: a newsletter signup at animations.dev/skills and a header image linking to animations.dev.
- Caveat: The README only summarizes each skill; the detailed rules live in the individual skill files, which are separate sources.
- Caveat: The skill list and install command reflect commit 85e8e23 and may change.
- Caveat: The authority rests on the author's experience at Vercel and Linear, not on cited studies.
- Caveat: write-swift is a general coding skill, not a design rule; it is kept for iOS projects only.
- Caveat: The README states that enter animations should be ease-out but not why; the reason is in the linked 7 Practical Animation Tips article, a separate source.
- Caveat: The shadow-over-border example gives no scope (which elements) and no values (opacity, blur), so it is recorded as a should, not a locked must; the detailed rule should come from the skill files.
- Caveat: Skill descriptions are summaries of what each skill does, so the rules drawn from them (review strictly, audit into plans, name effects, prototype variants) are recorded as should or consider, not must.

### Rules and practices

- **must** (motion, all): Use ease-out, not ease-in, for enter animations. Why: The README names ease-in on an enter animation as one of the little mistakes agents make, when it is 'supposed to be ease-out'; the reason itself is in the linked 7 Practical Animation Tips article, not in the README. Values: ease-out, ease-in. [An `ease-in` easing for an enter animation]
- **should** (elevation, all): Prefer a semi-transparent shadow over a solid border in UIs (the README gives no narrower scope or values). Why: Choosing a solid border instead of a semi-transparent shadow is one of the small agent mistakes that compound. Values: semi-transparent shadow, solid border. [solid border instead of a semi-transparent shadow]
- **should** (tooling, all): Pick the library for a task from libraries the author uses and trusts, instead of letting an agent hand-roll a component such as a toast or install an abandoned package. Why: The pick-ui-library skill exists so the agent picks the right library instead of hand-rolling a toast component or installing an abandoned package. [pick-ui-library]
- **should** (motion, all): When building an animation from scratch, explicitly choose its curve, duration and properties. Why: The animate skill exists to pick the correct curve, duration and properties. [animate]
- **should** (motion, all): Add motion only where it genuinely benefits the UI, and state explicitly what should not be animated. Why: find-animation-opportunities searches for places that would genuinely benefit from motion while also saying what not to animate. [find-animation-opportunities]
- **should** (process, all): Review animations strictly against the author's rules. Why: review-animations reviews animations in a strict way based on the author's rules. [review-animations]
- **should** (process, all): When auditing a codebase's animations, produce prioritized, self-contained plans that any agent can execute. Why: improve-animations audits all animations and returns prioritized, self-contained plans. [improve-animations]
- **should** (process, all): Describe an animation to an AI with its exact term rather than a vague description. Why: Using the right words gets better animations from an AI. [telling it exactly what you want by using the right words]
- **consider** (process, all): Build several different versions of a UI piece you describe and go through them with a switcher. Why: The prototype skill builds multiple versions of a described UI piece to go through with a switcher. [prototype]
- **should** (platforms, web): When a web app runs on a phone, fix sticky hover states, tap highlight flashes, the 100vh bug, inputs that zoom the page, laggy taps and safe areas. Why: These small fixes separate a website from an app and make it feel native on a phone. Values: 100vh. [mobile-native]
- **should** (motion, react): In React Native and Expo, hold gestures, sheets, haptics and screen transitions to the same bar as the other animation skills, and keep motion off the JS thread. Why: animate-expo is described as 'the same bar' for React Native and Expo, and names keeping motion off the JS thread. [animate-expo]
- **consider** (tooling, ios): Write modern Swift: value types, Swift 6 concurrency, generics, attention to performance, and Swift Testing. Why: The write-swift skill defines modern Swift by these practices. Values: Swift 6. [write-swift]
- **should** (process, all): Keep developing real design or engineering expertise and use AI to amplify it, not to replace it. Why: The skills are a side-effect of domain expertise; AI amplifies expertise and makes you better relative to others. [So learn to code, design, or develop expertise]

### Decisions it informs

- What easing should an enter animation use?
  - ease-out: The curve the README says enter animations are supposed to use When: Any element entering the screen
  - ease-in: The curve agents wrongly pick; the README counts it as a mistake When: Not for enter animations
  - Recommendation: ease-out; the README names ease-in on an enter animation as a typical agent mistake and links the 7 Practical Animation Tips article for the reason.
- Should a UI separate things with a solid border or a semi-transparent shadow? (`Q-depth-01`)
  - Solid border: What agents tend to choose; the README treats it as a wrong ingredient When: Not given by the source
  - Semi-transparent shadow: The ingredient the README treats as correct When: Setting UI surfaces apart
  - Recommendation: Semi-transparent shadow; the README lists a solid border in its place as a small mistake that compounds.
- Which of the author's skills fits the job at hand?
  - animate: Builds a new animation with the right curve, duration and properties When: Creating an animation from scratch
  - review-animations: Strict review against the author's rules When: Checking animations that already exist
  - improve-animations: Codebase-wide audit with prioritized, self-contained plans any agent can execute When: Improving all animations in a codebase
  - find-animation-opportunities: Finds places that genuinely benefit from motion and says what not to animate When: Deciding where to add motion
  - animation-vocabulary: Supplies the exact words for an effect When: Prompting an AI for a specific animation
  - pick-ui-library: Chooses a trusted library instead of hand-rolled code or an abandoned package When: A component like a toast is needed
  - prototype: Several versions of a UI piece with a switcher When: Comparing directions before committing
  - mobile-native: Fixes that make a web app feel native on a phone When: A web app is used on phones
  - animate-expo: Same motion bar for React Native and Expo When: Building in React Native or Expo
  - apple-design: Apple's interface and fluid-motion principles for the web When: Aiming for Apple-style interaction and motion
  - emil-design-eng: Main skill, mostly animation plus some design advice When: General design-engineering guidance
  - ask-sonner: Setup, styling, recipes and fixes for Sonner toasts When: Working with Sonner
  - write-swift: Modern Swift practices When: Writing Swift

### Process

1. Install the skills: Run npx skills@latest add emilkowalski/skills.
2. Name the effect: Use animation-vocabulary to find the exact term for an effect before asking an AI to build it [inferred order].
3. Prototype variants: Build several versions of the UI piece and go through them with a switcher [inferred order].
4. Build the animation: Use animate to choose the correct curve, duration and properties [inferred order].
5. Review and audit: Review animations strictly with review-animations; for a whole codebase, run improve-animations to get prioritized, self-contained plans any agent can execute. The ordering of these steps is not given by the source [inferred].

### Examples and visual references

- An agent using ease-in on an enter animation (AI agents generally): No visual; the README's first example of an agent picking the wrong animation ingredient, where ease-out is correct.
- An agent using a solid border instead of a semi-transparent shadow (AI agents generally): No visual; the README's second example of a small wrong choice that compounds across an interface.

### Numbers

- 100vh: The '100vh bug' named among mobile web problems the mobile-native skill fixes [mobile-native]
- Swift 6: The concurrency model the write-swift skill targets [write-swift]

<!-- /od:learn -->
