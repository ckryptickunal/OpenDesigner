---
type: source
title: Agents with Taste
created: 2026-09-27
updated: 2026-09-27
video_id: ek-agents-with-taste
url: https://emilkowal.ski/ui/agents-with-taste
channel: Emil Kowalski (web)
published: Unknown
authority: non-negotiable
tags:
  - agents
  - skills
  - taste
  - animation
  - easing
  - duration
  - scale
  - typography
  - hit-area
  - css
  - claude-code
  - design-engineering
---

# Agents with Taste

## Metadata

- Page ID: `ek-agents-with-taste`
- Publisher: Emil Kowalski (web)
- Published: Unknown
- URL: https://emilkowal.ski/ui/agents-with-taste

## Summary

Emil Kowalski argues that agents make engineers more leveraged than ever, but coding agents do not quite know what great visual work, such as animation, feels like, and that you can fix this by writing your taste down as strict rules in a skill file for each part of the interface. He shows that most taste decisions have a logical reason (for example, an element should grow from scale(0.95) rather than scale(0) because nothing in the real world appears from nothing). The article includes the exact rules from his own skills: a Practical Tips table for animation fixes, an easing decision flowchart, duration tiers with rules, and seven typography rules. For a design system this matters twice: the values themselves are concrete motion and typography defaults, and the method (articulate the why, set strict rules, hand them to agents) is how house standards get applied consistently by AI tools. [inferred]

## Key Ideas

- Coding agents lack a sense of what great visual work feels like, so taste must be written down for them.
- Write one skill file per aspect of the interface and give it to your agents.
- Almost every taste decision has a logical reason; experience lets you name it, not just feel it.
- Rules must be strict so the agent follows them instead of guessing or inventing its own.
- Elements should enter from a slightly smaller scale (0.95), never from scale(0).
- Easing is the most important part of an animation and is chosen with a fixed flowchart: enter or exit uses ease-out, on-screen movement uses ease-in-out, hover uses ease, constant motion uses linear.
- UI animations stay under 300ms, scale with element size and travel distance, and exits can be about 20% faster than entrances.
- Small CSS fixes solve common animation problems: scale(0.97) on press, will-change for jitter, animating a child to stop hover flicker, transform-origin at the trigger.
- Typography taste can be packaged the same way: about 65ch body width, tabular numbers in price columns, loosened uppercase tracking, matched fallback fonts.
- Underline only links, and use bold rather than italic for interface emphasis.
- The creative part stays with the human; the more you package into a skill, the more leverage you get from agents.

## Entities

- [[entities/emil-kowalski|Emil Kowalski]] (person): Design engineer and author; the rules come from his own skill files.
- [[entities/claude-code|Claude Code]] (tool): Coding agent he used to build an interactive Linear logo and to improve a dialog animation with his animation skill.
- [[entities/anthropic|Anthropic]] (company): Maker of the skill-creator skill he uses to package rules into skills.
- [[entities/skill-creator|skill-creator]] (tool): Anthropic skill he uses to make writing a skill file easier.
- [[entities/skill-file|Skill file]] (concept): A file of strict rules describing taste for one aspect of the interface, fed to coding agents.
- [[entities/linear|Linear]] (company): Its logo was the subject of an interactive demo he built with Claude Code.
- [[entities/sonner|Sonner]] (library): One of his open-source projects; its principles are included in his design engineering skill (a toast library [inferred]).
- [[entities/easing-decision-flowchart|Easing Decision Flowchart]] (concept): A decision tree from his skill that picks ease-out, ease-in-out, ease or linear by scenario.

## Topics

- [[topics/ai-assisted-design|AI-assisted design]]: Encode taste as strict rules in one skill file per interface aspect so coding agents produce better visual work; use Anthropic's skill-creator; ask agents to review work against the skill.
- [[topics/design-taste-and-judgement|Design taste and judgement]]: Taste is explainable: with experience you can say why something feels better, and almost every taste decision has a logical reason.
- [[topics/motion-principles|Motion principles]]: Entering elements grow from scale(0.95), not scale(0), because real objects never appear from nothing (the balloon analogy).
- [[topics/easing-and-timing|Easing and timing]]: Easing is chosen by a strict flowchart (ease-out for enter/exit and default, ease-in-out for on-screen movement, ease for hover, linear for constant motion); durations are 100-150ms, 150-250ms or 200-300ms by element type, under 300ms overall, longer for larger elements and longer travel, exits about 20% faster.
- [[topics/micro-interactions|Micro-interactions]]: Buttons get transform: scale(0.97) on :active; micro-interactions run 100-150ms; tooltips after the first one in a sequence skip their delay and animation.
- [[topics/animation-performance|Animation performance]]: Add will-change: transform to fix shaky or jittery animations; a subtle blur under 20px can mask animations that still feel off.
- [[topics/modals-and-popovers|Modals and popovers]]: Popovers should scale from the trigger by setting transform-origin; modals and drawers animate in 200-300ms; he used his skill to have Claude Code improve a dialog animation.
- [[topics/buttons-and-actions|Buttons and actions]]: Pressed buttons scale to 0.97 to feel responsive; small buttons get a 44px minimum hit area through a pseudo-element.
- [[topics/accessibility|Accessibility]]: Small buttons need a 44px minimum hit area; underlines are reserved for links so they stay a reliable affordance.
- [[topics/typography|Typography]]: Cap body text at about 65ch, use tabular-nums in price columns, use the ellipsis character, loosen uppercase letter-spacing, match fallback font metrics to avoid layout shift, reserve underline for links, prefer bold over italic for UI emphasis.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: Rules are expressed as CSS: transform, :active, will-change, transform-origin, pseudo-element hit areas, blur, tabular-nums, ch units and the … character in markup.
- [[topics/design-process|Design process]]: Step back, ask why you made each decision, articulate it, set the rule and be strict, then feed the packaged rules to agents.

## Notable Claims

- An engineer has never been more leveraged than today thanks to a fleet of agents. Evidence: intro: "never been more leveraged than today"
- Coding agents do not quite know what great feels like for visual work such as animations. Evidence: intro: "coding agents don’t quite know what great feels like"
- Giving agents a skill that holds your taste and knowledge can produce significantly better results. Evidence: intro: "can produce significantly better results, like the interactive Linear logo"
- With enough experience you can tell not only what feels better but also why, and articulate it. Evidence: Transferring taste
- Animating from a higher initial scale makes movement feel more gentle, natural and elegant. Evidence: Transferring taste: "animates from a higher initial scale value"
- scale(0) feels wrong because the element looks like it comes out of nowhere; a higher initial value resembles the real world, like a deflated balloon that still has a visible shape. Evidence: Transferring taste: balloon
- Almost every taste decision has a logical reason if you look closely, in any discipline. Evidence: "That’s the why"; "This applies to any other discipline really"
- The more creative part of the job is still up to the human; the more you package into a skill, the more leverage you get from agents. Evidence: "the more creative part of the job is still up to you"
- Easing is the most important part of any animation. Evidence: "choosing the right easing, the most important part of any animation"
- A strict easing flowchart means the agent does not have to guess or make up its own rules. Evidence: Easing Decision Flowchart intro: "This is strict"
- Any taste decision (layout, icons, color theory, typography) can be packaged into a skill the same way. Evidence: "whether it’s layout, icons, or color theory"
- Tight uppercase text reads cramped. Evidence: Typography rule 4
- Declaring a fallback stack whose x-height and weight match the primary face keeps font loading from causing layout shift. Evidence: Typography rule 5
- Underlining non-link text weakens underline as an affordance and tempts people to click inert copy. Evidence: Typography rule 6
- Italic used for hierarchy reads like print editorial, not UI hierarchy. Evidence: Typography rule 7
- Given his animation skill, Claude Code returns a clear list of issues based on the defined rules and a before and after table of changes. Evidence: "improve a dialog animation using my animation skill"
- Once you can articulate why something feels good, you can guide agents with it just like you would guide a less experienced designer. Evidence: "just like you would guide a less experienced designer"

## Quotes

> Almost every “taste” decision has a logical reason if you look close enough.
> coding agents don’t quite know what great feels like.
> set the rules, be strict

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: Opens with a plug for his course aiforui.dev (early access closed) and ends with a 'Get the skill' plug for one big design engineering skill made from his blog articles (animations, component design, principles from open-source projects like Sonner); neither is a rule.
- Caveat: Publication date is unknown, so tool references (Claude Code, Anthropic's skill-creator) may be dated.
- Caveat: Several demos (the Linear logo, the Options scale comparison, the Claude Code dialog video) are embedded media; the text only describes them, so their exact motion values are not captured.
- Caveat: Some rules are worded permissively in the source: exits 'can be' ~20% faster, and the blur under 20px is a masking fix for when 'something still feels off', not a default.
- Caveat: The easing flowchart is presented as 'my philosophy'; it names only CSS keyword curves (ease-out, ease-in-out, ease, linear) and gives no cubic-bezier values.
- Caveat: The stated reason for the … character (truncation following the container instead of a fixed character count) is copied as given and not explained further in the text.
- Caveat: Small tension in the source: the rule says UI animations should stay under 300ms, while the modal and drawer tier is 200-300ms, whose top end equals 300ms.
- Caveat: The article shows excerpts of his skill files ('some rules on typography', 'many others live under Practical Tips'), not the complete skills.
- Caveat: Strengths follow the source's framing: Practical Tips rows are problem and fix tips (should), except where the alternative is called wrong (scale(0), popover scaling from the wrong point); the easing flowchart is called strict and the duration 'Rules' and typography 'rules' are labelled rules (must), except permissive wording ('can be', 'Prefer').

### Rules and practices

- **should** (motion, css): Make buttons feel responsive by adding transform: scale(0.97) on :active. Why: Makes buttons feel responsive (the Practical Tips scenario it solves). Values: transform: scale(0.97), :active. [Practical Tips: Make buttons feel responsive]
- **must** (motion, all): Animate entering elements from scale(0.95), never from scale(0). Why: scale(0) looks like the element comes out of nowhere; a higher initial scale resembles the real world (a deflated balloon still has a visible shape) and feels more gentle, natural and elegant. Values: scale(0.95), scale(0). [Practical Tips: Element appears from nowhere; Transferring taste]
- **should** (motion, css): Fix shaky or jittery animations by adding will-change: transform. Why: It is the listed fix for shaky or jittery animations; the source gives no further reason. Values: will-change: transform. [Practical Tips: Shaky/jittery animations]
- **should** (motion, css): When a hover effect causes flicker, animate a child element instead of the hovered parent. Why: It is the listed fix for hover-caused flicker; the source gives no further reason. [Practical Tips: Hover causes flicker]
- **must** (motion, css): Set a popover's transform-origin to the location of its trigger so it scales out from the trigger. Why: Otherwise the popover scales from the wrong point. Values: transform-origin. [Practical Tips: Popover scales from wrong point]
- **should** (motion, all): When tooltips open one after another, skip the delay and the animation for every tooltip after the first. Why: Sequential tooltips feel slow when each one waits and animates. [Practical Tips: Sequential tooltips feel slow]
- **should** (accessibility, css): Give small buttons a 44px minimum hit area, built with a pseudo-element. Why: Small buttons are hard to tap. Values: 44px. [Practical Tips: Small buttons hard to tap]
- **consider** (motion, css): If an animation still feels off after other fixes, add a subtle blur under 20px to mask it. Why: Listed as the fix when something still feels off. Values: under 20px. [Practical Tips: Something still feels off]
- **must** (motion, all): Choose easing with the fixed decision flowchart every time, checking in order: entering or exiting the viewport, moving or morphing on screen, hover change, constant motion, then the default; do not improvise or invent easing rules. Why: Easing is the most important part of any animation; the flowchart is strict so the agent doesn't have to guess or make up its own rules. Values: ease-out, ease-in-out, ease, linear. [Easing Decision Flowchart intro]
- **must** (motion, all): Use ease-out for any element entering or exiting the viewport. Why: First branch of the easing flowchart. Values: ease-out. [Easing Decision Flowchart: entering or exiting the viewport]
- **must** (motion, all): Use ease-in-out for elements moving or morphing on screen. Why: Easing flowchart branch for on-screen movement. Values: ease-in-out. [Easing Decision Flowchart: moving/morphing on screen]
- **must** (motion, all): Use ease for hover changes. Why: Easing flowchart branch for hover changes. Values: ease. [Easing Decision Flowchart: hover change]
- **must** (motion, all): Use linear for constant motion (the only flowchart branch that picks linear). Why: Easing flowchart branch for constant motion. Values: linear. [Easing Decision Flowchart: constant motion]
- **must** (motion, all): When no flowchart branch applies, default to ease-out. Why: The flowchart's default outcome. Values: ease-out. [Easing Decision Flowchart: Default → ease-out]
- **should** (motion, all): Run micro-interactions for 100-150ms. Why: Duration Guidelines table value for micro-interactions. Values: 100-150ms. [Duration Guidelines: Micro-interactions]
- **should** (motion, all): Run standard UI animations such as tooltips and dropdowns for 150-250ms. Why: Duration Guidelines table value for standard UI. Values: 150-250ms. [Duration Guidelines: Standard UI (tooltips, dropdowns)]
- **should** (motion, all): Run modal and drawer animations for 200-300ms. Why: Duration Guidelines table value for modals and drawers. Values: 200-300ms. [Duration Guidelines: Modals, drawers]
- **must** (motion, all): Keep every UI animation under 300ms. Why: Stated as a duration rule. Values: under 300ms. [Duration Guidelines Rules: UI animations should stay under 300ms]
- **must** (motion, all): Give larger elements longer durations than smaller ones. Why: Stated as a duration rule: larger elements animate slower than smaller ones. [Duration Guidelines Rules: Larger elements animate slower]
- **consider** (motion, all): Make exit animations about 20% faster than the matching entrance. Why: Stated as a duration rule: exits can be ~20% faster than entrance. Values: ~20%. [Duration Guidelines Rules: Exit animations can be ~20% faster]
- **must** (motion, all): Match duration to distance: the longer the element travels, the longer the duration. Why: Stated as a duration rule. [Duration Guidelines Rules: Match duration to distance]
- **must** (typography, web): Cap body text at about 65ch instead of letting it stretch full width. Why: Keeps line length comfortable to read. Values: 65ch. [Typography rule 1]
- **must** (typography, css): Apply tabular-nums to price columns. Why: Digits align and the column reads cleanly. Values: tabular-nums. [Typography rule 2]
- **must** (typography, web): Use the … character in markup instead of three periods (...). Why: The source says truncation then follows the container instead of snapping at a fixed character count. Values: …, .... [Typography rule 3]
- **must** (typography, all): Loosen letter-spacing on uppercase labels. Why: Tight uppercase reads cramped. [Typography rule 4]
- **must** (typography, web): Declare a fallback font stack whose x-height and weight match the primary face. Why: Font loading then does not cause layout shift. [Typography rule 5]
- **must** (typography, all): Reserve underlines for links; emphasize non-link text with weight or color, never an underline. Why: Underline stays a reliable affordance and people are not tempted to click inert copy. [Typography rule 6]
- **should** (typography, all): Use bold for interface emphasis; keep italic for citations and linguistic stress in prose. Why: Italic hierarchy reads like print editorial, not UI hierarchy. [Typography rule 7]
- **should** (process, all): Write a skill file for each aspect of the interface (for example animation, layout, icons, color theory, typography) and give it to your coding agents. Why: Agents don't know what great feels like for visual work; with your taste packaged as rules they produce significantly better results. ["create a skill file for each aspect of the interface"]
- **should** (process, all): For every taste rule, state why it has to be done that way, and phrase the rule strictly rather than as loose advice. Why: Almost every taste decision has a logical reason; strict rules mean the agent doesn't guess or invent its own, the way you would guide a less experienced designer. ["articulate clearly why something has to be done this way, set the rules, be strict"]
- **consider** (tooling, all): Use Anthropic's skill-creator skill to package your rules into a skill. Why: He says it makes the process easier. ["I use the skill-creator skill from Anthropic"]

### Decisions it informs

- Which easing curve should an animation use? (`Q-motion-03`)
  - ease-out: Starts fast and settles [inferred]; the flowchart's choice for entering and exiting. When: The element is entering or exiting the viewport, or no other branch applies (default).
  - ease-in-out: Speeds up then slows down [inferred]. When: The element is moving or morphing on screen.
  - ease: The CSS ease keyword curve. When: A hover change.
  - linear: Constant speed [inferred]. When: Constant motion.
  - Recommendation: Pick by the job of the animation using the strict flowchart, defaulting to ease-out; easing is the most important part of any animation. Grouping curves by job matches the role-based option [inferred].
- What scale should an element start from when it appears?
  - scale(0): Looks like the element comes out of nowhere; feels wrong. When: Never, per the source.
  - scale(0.95): Gentle, natural and elegant, like a deflated balloon that still has a shape. When: Any element that appears or enters.
  - Recommendation: Start from scale(0.95), not scale(0), because a higher initial value resembles the real world.
- How long should a UI animation run? (`Q-motion-02`)
  - 100-150ms: The shortest tier; quick feedback [inferred]. When: Micro-interactions.
  - 150-250ms: The middle tier; a short, noticeable transition [inferred]. When: Standard UI such as tooltips and dropdowns.
  - 200-300ms: The longest tier; larger elements animate slower than smaller ones. When: Modals and drawers.
  - Recommendation: Use the tier for the element type, stay under 300ms, go longer for larger elements and longer travel, and make exits about 20% faster than entrances.
- How wide can body text run? (`Q-type-14`)
  - Full width: Lines stretch across the container and become uncomfortable to read. When: Not recommended for body text.
  - About 65ch: Comfortable line length. When: Body text.
  - Recommendation: Cap body text at about 65ch so line length stays comfortable to read.
- Should digits in price columns all be the same width? (`Q-type-06`)
  - Default digits: Digits may not line up down the column [inferred]. When: Not recommended for price columns [inferred].
  - tabular-nums: Digits align and the column reads cleanly. When: Price columns.
  - Recommendation: Apply tabular-nums to price columns.
- How should important non-link text stand out? (`Q-type-12`)
  - Underline: Looks clickable; weakens underline as the link affordance and tempts clicks on inert copy. When: Links only.
  - Weight or color: Emphasis without implying a link. When: Emphasizing non-link text.
  - Bold: Reads as interface hierarchy. When: Interface emphasis.
  - Italic: Reads like print editorial, not UI hierarchy. When: Citations and linguistic stress in prose.
  - Recommendation: Use weight or color (bold) for emphasis, underline only for links, italic only for citations and stress in prose.
- How big should the tappable area of a small button be? (`Q-space-03`)
  - Same as the visible button: Small buttons are hard to tap. When: Not recommended for small buttons.
  - 44px minimum hit area: Easier to tap; built with a pseudo-element so the visible size can stay small [inferred]. When: Any small button.
  - Recommendation: Use a 44px minimum hit area via a pseudo-element.

### Process

1. Build and name your taste: With experience, work out not only which version feels better but why, until you can articulate it.
2. Ask why: Step back from each decision and ask why you made it; almost every taste decision has a logical reason.
3. Write one skill per aspect: Create a skill file for each aspect of the interface (animation, layout, icons, color theory, typography) that describes the rules.
4. Make the rules strict: State each rule so the agent does not have to guess, as in his examples: a scenario and solution table (Practical Tips), a decision flowchart (easing), a duration table with rules, and numbered typography rules each with its reason.
5. Package with skill-creator: Use Anthropic's skill-creator skill to make packaging the rules easier.
6. Feed the skill to agents: Give the skill to your coding agents and ask them to improve work, e.g. a dialog animation; the agent returns a list of issues based on your rules and a before and after table of what changed.
7. Keep the creative part: The more creative part of the job stays with you; package everything else to get more leverage from agents.

### Examples and visual references

- Interactive Linear logo built with Claude Code guided by his skills (Linear logo, built with Claude Code): Embedded demo shown as proof that skills produce better results; its visuals are not described in the text.
- Side-by-side comparison of two 'Options' elements appearing (emilkowal.ski article demo): The left one animates from scale(0) and looks like it comes out of nowhere; the correct one starts from a higher scale and feels gentle, natural and elegant.
- Balloon analogy for initial scale: Even deflated, a balloon has a visible shape and never disappears completely, which is why an element should not start from scale(0).
- Practical Tips table from his animation skill (His animation skill): Eight scenario and solution rows, from scale(0.97) on :active to a blur under 20px, showing the format that makes rules easy for agents to follow.
- Easing Decision Flowchart (His animation skill): A text tree: enter or exit leads to ease-out, on-screen movement to ease-in-out, hover to ease, constant motion to linear, default ease-out.
- Claude Code improving a dialog animation using his animation skill (Claude Code (video in the article)): The agent lists issues based on his rules and shows a before and after table of the changes.

### Numbers

- scale(0.97): Button scale on :active to feel responsive [Practical Tips]
- scale(0.95): Starting scale for an appearing element, instead of scale(0) [Practical Tips]
- scale(0): Starting scale to avoid: the element looks like it comes out of nowhere [Practical Tips; Transferring taste]
- 44px: Minimum hit area for small buttons, via a pseudo-element [Practical Tips]
- under 20px: Maximum subtle blur used to mask an animation that still feels off [Practical Tips]
- 100-150ms: Duration for micro-interactions [Duration Guidelines]
- 150-250ms: Duration for standard UI (tooltips, dropdowns) [Duration Guidelines]
- 200-300ms: Duration for modals and drawers [Duration Guidelines]
- 300ms: Upper limit: UI animations should stay under it [Duration Guidelines Rules]
- ~20%: How much faster exit animations can be than entrances [Duration Guidelines Rules]
- 65ch: Approximate cap on body text line length [Typography rule 1]

<!-- /od:learn -->
