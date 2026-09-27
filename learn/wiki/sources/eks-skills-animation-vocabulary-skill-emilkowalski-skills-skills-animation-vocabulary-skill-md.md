---
type: source
title: "emilkowalski/skills: skills/animation-vocabulary/SKILL.md"
created: 2026-09-27
updated: 2026-09-27
video_id: eks-skills-animation-vocabulary-skill
url: https://github.com/emilkowalski/skills/blob/85e8e23/skills/animation-vocabulary/SKILL.md
channel: emilkowalski/skills (GitHub, MIT)
published: commit 85e8e23
authority: non-negotiable
tags:
  - animation
  - motion
  - glossary
  - vocabulary
  - easing
  - springs
  - performance
  - micro-interactions
  - gestures
  - reduced-motion
  - transitions
  - ai-prompting
---

# emilkowalski/skills: skills/animation-vocabulary/SKILL.md

## Metadata

- Page ID: `eks-skills-animation-vocabulary-skill`
- Publisher: emilkowalski/skills (GitHub, MIT)
- Published: commit 85e8e23
- URL: https://github.com/emilkowalski/skills/blob/85e8e23/skills/animation-vocabulary/SKILL.md

## Summary

This is Emil Kowalski's animation-vocabulary skill: a reverse-lookup glossary that turns a loose description of a web motion effect into its exact name, so the person knows what to ask an AI or a designer for. It groups its terms into families (entrances and exits, sequencing, transforms, state transitions, scroll, feedback, easing, springs, looping, polish, performance and principles) and tells the agent how to answer: read for intent, quote the glossary verbatim, contrast close terms and never invent new ones. Many definitions carry firm guidance, for example ease-out as the default for UI, linear only for spinners and marquees, animating transform and opacity so the GPU keeps motion smooth, tabular numbers for counters, and shorter, subtler motion the more often it is seen. For a design system this supplies a shared, precise motion vocabulary for tokens, component specs and prompts, plus a compact set of motion and performance rules.

## Key Ideas

- People describe motion by what they see or feel, so a naming tool must map sensations like 'springy' or 'draws itself in' to terms.
- A precise shared vocabulary lets people ask for the exact motion they want from an AI or a designer.
- Close terms need contrasting (clip-path vs mask, pop in vs bounce, shared element transition vs layout animation) so the person can choose.
- If no term fits, name the closest one and say it is an approximation, or combine glossary terms; do not invent new words.
- Ease-out is the default for UI and anything responding to the user; ease-in is usually avoided and linear is kept for spinners and marquees.
- Springs are physics-based (stiffness, damping, mass) instead of fixed-duration, and they carry velocity into the next animation when interrupted.
- 60fps is the baseline for smooth motion (120fps on newer displays); animating transform and opacity keeps it smooth, while animating properties like width, height, top or left forces layout every frame and causes jank.
- Motion should have a job (orient, give feedback, show relationships), not decorate.
- The more often an animation is seen, the shorter and subtler it should be.
- An origin-aware popover grows out of the trigger that opened it instead of from its own center, which is the CSS default.
- Spatial consistency keeps an element's identity and position across states so users never lose track of it.
- Tabular (fixed-width) digits are essential for tickers, timers and counters so numbers do not jump around.
- Respect the reduced-motion setting by toning motion down or removing it.
- The right animation can make an interface feel faster even when it is not.

## Entities

- [[entities/emil-kowalski|Emil Kowalski]] (person): Design engineer whose animation philosophy the glossary is based on
- [[entities/emilkowalski-skills|emilkowalski/skills]] (product): MIT-licensed GitHub repository of agent skills that contains this animation-vocabulary skill
- [[entities/vocabulary-page|/vocabulary page]] (product): The project's vocabulary page that this glossary mirrors as a curated snapshot
- [[entities/dynamic-island|Dynamic Island]] (product): Given as the example of a morph, where one shape smoothly turns into another
- [[entities/ios-overscroll|iOS overscroll]] (concept): The reference feel for rubber-banding: resistance and snap-back when dragging past a boundary
- [[entities/origin-aware-animation|Origin-aware animation]] (concept): An element animates out of its trigger instead of from its own center
- [[entities/ease-out|Ease-out]] (concept): Starts fast and ends slow; the default for most UI
- [[entities/spring|Spring]] (concept): Physics-driven motion (tension, mass, damping) as an alternative to fixed-duration easing
- [[entities/perceptual-duration|Perceptual duration]] (concept): How long a spring feels until it is finished, although it keeps micro-settling
- [[entities/tabular-numbers|Tabular numbers]] (concept): Fixed-width digits that stop numbers shifting as they change
- [[entities/will-change|will-change]] (concept): CSS hint that lets the browser promote an element to its own layer before it animates
- [[entities/layout-thrashing|Layout thrashing]] (concept): Animating width, height, top or left, which forces layout recalculation every frame and causes jank
- [[entities/prefers-reduced-motion|prefers-reduced-motion]] (concept): The user setting that reduced-motion handling must respect
- [[entities/clip-path|Clip-path]] (concept): Clips an element to a shape; used for reveals, masks and before/after sliders
- [[entities/mask|Mask]] (concept): Like clip-path but with soft, fadeable edges

## Topics

- [[topics/motion-principles|Motion principles]]: Principles to know: purposeful animation, anticipation, follow-through, squash and stretch, perceived performance, frequency of use, spatial consistency, hardware acceleration and reduced motion; plus a full naming glossary for entrances, transitions, loops and polish effects.
- [[topics/easing-and-timing|Easing and timing]]: Ease-out is the default for UI and user responses, ease-in is usually avoided, ease-in-out suits on-screen A-to-B moves, linear is only for spinners or marquees, and asymmetric curves feel more alive; also defines keyframes, tweening, stagger, orchestration, delay, duration, fill mode and stepped animation.
- [[topics/spring-animation|Spring animation]]: Springs are driven by stiffness, damping and mass; higher stiffness is snappier, lower damping bouncier, more mass slower; springs carry velocity into the next animation, support interruption and have a perceptual duration.
- [[topics/animation-performance|Animation performance]]: 60fps is the baseline and 120fps on newer displays; jank is visible stutter from dropped frames; animating transform and opacity lets the GPU composite motion without redoing layout or paint, will-change is a hint to promote a layer ahead of time, and animating properties like width, height, top or left causes layout thrashing.
- [[topics/gestures-and-drag|Gestures and drag]]: Defines drag with momentum, drag to reorder where other items shift to make room, swipe to dismiss for drawers and toasts, and rubber-banding past a boundary.
- [[topics/micro-interactions|Micro-interactions]]: Hover effects, a subtle scale-down on press, hold to confirm with a filling progress, shake for errors, ripple from the tap point, text morph and number tickers.
- [[topics/reduced-motion|Reduced motion]]: Respect prefers-reduced-motion by toning down or removing motion.
- [[topics/modals-and-popovers|Modals and popovers]]: Origin-aware animation: a popover grows from the button that opened it instead of from its own center, which is the default in CSS; this is the skill's first worked example.
- [[topics/feedback-empty-and-loading-states|Feedback, empty and loading states]]: Skeleton or shimmer placeholders with a moving sheen while content loads; shake signals rejected input.
- [[topics/typography|Typography]]: Tabular numbers (fixed-width digits) are essential for tickers, timers and counters; text morph and typewriter effects animate text.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: CSS-level terms: keyframes, fill mode (forwards), transform origin, perspective, cubic-bezier, clip-path, mask, will-change, compositing, view transitions and scroll-driven animation.
- [[topics/ai-assisted-design|AI-assisted design]]: The skill exists so people can name a motion effect precisely when prompting an AI or briefing a designer, and it prescribes how an agent answers naming questions.

## Notable Claims

- Users describe motion effects by what they see or feel, not by the technical name. Evidence: Read for intent, not keywords.
- In CSS an element animates from its own center by default, not from the trigger that opened it. Evidence: Origin-aware animation — ... instead of from its own center which is the default in CSS.
- Ease-in starts slow and can feel sluggish. Evidence: Ease-in — Starts slow, ends fast. Usually avoided; can feel sluggish.
- Asymmetric easing feels more alive than a symmetric curve. Evidence: Asymmetric easing — ... Feels more alive than a symmetric one.
- Higher spring stiffness feels snappier. Evidence: Stiffness / Tension — ... Higher feels snappier.
- Lower damping gives more bounce and oscillation. Evidence: Damping — ... Lower damping means more bounce and oscillation.
- More mass makes a spring slower and more sluggish. Evidence: Mass — ... More mass makes it slower and more sluggish.
- A spring keeps micro-settling after it already feels finished. Evidence: Perceptual duration
- When interrupted, a spring carries the element's velocity into the next animation, so a flicked element keeps its speed. Evidence: Velocity — ... A spring carries it into the next animation when interrupted
- A lower perspective value exaggerates 3D depth, as if the viewer is closer. Evidence: Perspective — ... a lower value exaggerates depth
- Mask differs from clip-path by having soft, fadeable edges. Evidence: Mask — ... like clip-path, but with soft, fadeable edges.
- Fixed-width digits stop numbers shifting around as they change. Evidence: Tabular numbers — Fixed-width digits so numbers don't shift around as they change.
- 60fps is the baseline for smooth motion, and newer displays run at 120fps. Evidence: Frame rate (FPS)
- Jank is visible stutter caused by the browser dropping frames. Evidence: Jank — Visible stutter when the browser drops frames
- Animating width, height, top or left forces the browser to recalculate layout every frame, causing jank. Evidence: Layout thrashing
- Animating transform and opacity lets the GPU keep motion smooth, without redoing layout or paint. Evidence: Hardware acceleration; Compositing
- will-change lets the browser promote an element to its own layer ahead of time. Evidence: will-change — A CSS hint that an element is about to animate
- The right animation makes an interface feel faster even when it is not. Evidence: Perceived performance
- The more often an animation is seen, the shorter and subtler it should be. Evidence: Frequency of use
- Direction-aware transitions give navigation a sense of direction. Evidence: Direction-aware transition
- A subtle scale-down on click makes an element feel physical. Evidence: Press / Tap feedback
- The glossary is a curated snapshot of the project's /vocabulary page. Evidence: A curated snapshot mirroring the project's `/vocabulary` page
- A dropped frame is one the browser missed its deadline to draw, causing a tiny hitch in motion. Evidence: Dropped frame
- Momentum is motion that carries velocity, especially after a drag or interruption. Evidence: Momentum
- In a view transition the browser morphs between two states or pages, connecting shared elements. Evidence: View transition
- Pop in is an entrance with a slight overshoot, while bounce is a spring that overshoots and settles; the skill lists them as close terms to contrast. Evidence: Pop in; Bounce; 3. Disambiguate close terms.

## Quotes

> Motion should serve a function — orient, give feedback, show relationships — not just decorate.
> The more often a user sees an animation, the shorter and subtler it should be.
> Avoid for UI; reserve for spinners or marquees.

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: This is a naming glossary, not a spec: it gives almost no durations, curves or scale values, so exact motion tokens must come from Emil Kowalski's other sources. [inferred]
- Caveat: The glossary is described as a curated snapshot of the project's /vocabulary page and this copy is pinned to commit 85e8e23, so it can drift from the live page.
- Caveat: The Accordion / Collapse entry animates height, while the Performance section lists height among properties that cause layout thrashing; the glossary does not reconcile the two. [inferred]
- Caveat: Most entries are neutral definitions (hover effect, parallax, typewriter, orbit, press feedback, layout animation); rules drawn from them are marked consider. Must is kept for explicit instructions to the agent and for entries worded as rules: ease-out as the default, linear avoided for UI, tabular numbers called essential, and the two principles phrased with 'should' (purposeful animation, frequency of use). Principles worded as facts (spatial consistency, hardware acceleration, reduced motion, the 60fps baseline, layout thrashing) are marked should.
- Caveat: The initial-response line attributes the knowledge to Emil Kowalski's animation philosophy; it is self-description, not independent evidence.
- Caveat: Reduced motion is only listed as a principle here; OpenDesigner locks it as an accessibility floor regardless of this source's wording. [inferred]

### Rules and practices

- **must** (process, all): Answer a naming question by mapping what the person sees or feels ('springy', 'slides off', 'draws itself in') to the glossary term, not by matching keywords. Why: Users describe what they see or feel, not the technical name. [1. Read for intent, not keywords.]
- **must** (process, all): Quote glossary descriptions verbatim when naming an effect; do not paraphrase them. Why: The glossary's descriptions are authoritative. [2. Quote the glossary verbatim.]
- **must** (process, all): Format a naming answer as the bold term, an em dash, then its description, for example '**Stagger** — ...'. Why: This is the skill's defined output format. [Quick Start]
- **must** (process, all): When several terms could fit, list the best match first, then 1–2 alternates (under 'Close alternates:'), each with a one-line note on how it differs. Why: Several terms can fit one description; the note on how each differs lets the user pick. [inferred] Values: 1–2 alternates, Close alternates:. [If several terms could fit, list the best match first]
- **must** (process, all): When two close terms compete, such as Clip-path vs Mask, Pop in vs Bounce, or Shared element transition vs Layout animation, contrast them so the person can pick. Why: Contrasting them lets the user pick. [3. Disambiguate close terms.]
- **must** (process, all): When nothing matches exactly, name the closest term and say plainly it is an approximation, or describe the effect by combining glossary terms (e.g. 'a stagger of scale-in entrances'). Why: The source gives no reason; saying plainly it is an approximation stops the user taking it as the exact name. [inferred] [4. When nothing matches exactly]
- **must** (process, all): Do not invent a motion term that is not in the glossary; say it is not there, though you may explain the concept using glossary words. Why: The glossary is the authority (its descriptions are called authoritative); if a term genuinely isn't there, the skill says so. [inferred] [5. Stay within this glossary.]
- **must** (process, all): Lead a naming answer with the term and expand only if asked. Why: A naming question wants a name, not an essay. [6. Keep it tight.]
- **must** (tooling, all): When the vocabulary skill is invoked without a specific question, reply only with its ready message and give no other information until asked. Why: Stated as the skill's fixed opening; the source gives no further reason. [Initial Response]
- **should** (process, all): Use the vocabulary lookup when someone asks "what's it called when…" or describes a motion effect without its name; use it to name an effect, not to design or build one. Why: The skill's description scopes it to finding the right word to prompt an AI or designer with. [description: For naming an effect, not designing or building one.]
- **must** (tooling, all): Keep the glossary and the project's /vocabulary page in sync whenever either changes. Why: The glossary is a curated snapshot mirroring that page. [keep the two in sync when either changes]
- **must** (motion, all): Use ease-out as the default easing for most UI and for anything responding to the user. Why: Ease-out starts fast and ends slow; the source names it the default without a further reason. Values: Ease-out. [Ease-out — Starts fast, ends slow. The default for most UI]
- **should** (motion, all): Usually avoid ease-in for UI motion. Why: It starts slow and can feel sluggish. Values: Ease-in. [Ease-in — ... Usually avoided; can feel sluggish.]
- **should** (motion, all): Use ease-in-out for elements already on screen moving from A to B. Why: Slow, fast, slow suits an on-screen move between two points. Values: Ease-in-out. [Ease-in-out — Slow, fast, slow. Good for elements already on screen]
- **must** (motion, all): Do not use linear easing for UI; reserve it for spinners or marquees. Why: Linear is constant speed; the source says to avoid it for UI and reserve it for spinners or marquees, without a further reason. Values: Linear. [Linear — Constant speed. Avoid for UI]
- **consider** (motion, all): Prefer an asymmetric easing curve, which accelerates and decelerates at different rates, over a symmetric one. Why: It feels more alive than a symmetric curve. [Asymmetric easing]
- **consider** (motion, css): Define a custom cubic-bezier curve when you need precise control over easing. Why: A custom curve gives precise control. Values: Cubic-bezier. [Cubic-bezier — A custom easing curve you define for precise control.]
- **consider** (motion, all): Consider spring animation (stiffness, damping, mass) as an alternative to fixed-duration easing. Why: Springs are driven by physics rather than a set duration. Values: tension, mass, damping. [Spring Animations — physics-based motion as an alternative to fixed-duration easing]
- **consider** (motion, all): Raise spring stiffness (tension) to make motion feel snappier. Why: Stiffness is how strongly the spring pulls toward its target; higher feels snappier. [Stiffness / Tension]
- **consider** (motion, all): Lower spring damping for more bounce and oscillation; damping sets how quickly the spring settles. Why: Damping sets how quickly a spring settles; lower means more bounce. [Damping]
- **consider** (motion, all): Add spring mass to make an element feel heavier, knowing it also becomes slower and more sluggish. Why: More mass makes motion slower and more sluggish. [Mass — How heavy the animated element feels.]
- **consider** (motion, all): Use a bouncing spring (overshoot, then settle) when the moment should feel playful. Why: Bounce adds playfulness. [Bounce — A spring that overshoots and settles, adding playfulness.]
- **consider** (motion, all): Judge a spring's length by when it feels finished (its perceptual duration), not by when it stops micro-settling. [inferred] Why: A spring keeps micro-settling underneath after it feels finished. [Perceptual duration]
- **consider** (motion, all): When an animation is interrupted, carry the element's current velocity into the next animation (for example with a spring) so a flicked element keeps its speed. Why: A spring carries velocity into the next animation when interrupted. [Velocity; Momentum]
- **consider** (motion, all): Make animations interruptible so they can be smoothly redirected mid-flight instead of finishing first. Why: It can be smoothly redirected mid-flight instead of finishing first. [Interruptible animation]
- **consider** (motion, all): Pair a scale-in entrance with a fade. Why: Scale in is often paired with a fade. [Scale in — ... often paired with a fade.]
- **consider** (motion, all): Make popovers origin-aware: animate them out of the trigger that opened them instead of from their own center. Why: In CSS the default is to grow from the element's own center, not from the trigger. [Origin-aware animation]
- **consider** (motion, css): Set the transform origin to the anchor point a scale or rotation should grow or spin from. Why: Transform origin is the anchor for scale and rotation. Values: Transform origin. [Transform origin]
- **consider** (motion, css): Lower the perspective value to exaggerate 3D depth, as if the viewer is closer. Why: A lower value exaggerates depth, like the viewer is closer. Values: Perspective, rotateX, rotateY. [Perspective]
- **consider** (motion, all): When an element's size or position changes, animate it to the new spot instead of letting it snap. Why: That is what a layout animation does. [Layout animation]
- **consider** (motion, all): Slide content one way when navigating forward and the opposite way when going back. Why: It gives navigation a sense of direction. [Direction-aware transition]
- **consider** (motion, all): Visually connect the before and after states of a change, for example by growing and shrinking the same rectangle. Why: A continuity transition keeps the user oriented. [Continuity transition]
- **should** (motion, all): Keep an element's identity and position consistent across states when animating. Why: So users never lose track of where things went. [Spatial consistency]
- **consider** (motion, all): Use a shared element transition when an element travels and transforms from one position into another, like a thumbnail expanding into a card. Why: The element travels and transforms from one position into another, like a thumbnail expanding into a card. [Shared element transition]
- **consider** (motion, all): Use a crossfade when one element replaces another in the same spot. Why: One fades out as the other fades in, in the same spot. [Crossfade]
- **consider** (motion, all): Coordinate the timing of multiple animations so they read as one motion. Why: Orchestration makes several animations feel like one coordinated motion. [Orchestration]
- **consider** (motion, all): Animate a group of items one after another with a small delay between each to create a cascade. Why: That is a stagger. [Stagger]
- **consider** (motion, css): Use a fill mode such as forwards when an element must keep its last frame's styles after the animation ends. Why: Fill mode decides whether first or last frame styles apply outside the animation. Values: forwards. [Fill mode]
- **consider** (motion, all): Use a stepped animation for motion that moves in discrete steps, like a countdown timer. Why: The motion is divided into discrete steps. [Stepped animation]
- **consider** (components, all): Give clickable elements a subtle scale-down on press. Why: It makes the element feel physical. [Press / Tap feedback]
- **consider** (components, all): For hold-to-confirm buttons, show a progress effect that fills while the user holds the button. Why: That is how hold to confirm is defined. [Hold to confirm]
- **consider** (patterns, all): Let dragged elements carry momentum when released. Why: Drag is often paired with momentum on release. [Drag — ... often with momentum when released.]
- **consider** (patterns, all): In drag to reorder, shift the other list items to make room while an item is dragged. Why: That is how drag to reorder is defined. [Drag to reorder]
- **consider** (patterns, all): Let drawers and toasts be closed by swiping them off-screen. Why: Swipe to dismiss is defined with drawers and toasts as examples. [Swipe to dismiss]
- **consider** (patterns, all): Add resistance and snap-back when the user drags past a boundary. Why: Rubber-banding gives the iOS overscroll feel. [Rubber-banding]
- **consider** (patterns, all): Use a quick side-to-side shake to signal an error or rejected input. Why: That is the defined meaning of shake or wiggle. [Shake / Wiggle]
- **consider** (components, all): Use a ripple expanding from the tap point to confirm a press. Why: A ripple confirms the press. [Ripple]
- **consider** (motion, all): Use alternate (yoyo) when a loop should play forward then reverse each iteration instead of jumping back to the start. Why: That is how the glossary defines alternate (yoyo). Values: Alternate (yoyo). [Alternate (yoyo)]
- **consider** (motion, all): Use a gentle repeating scale or opacity pulse to draw attention. Why: That is what a pulse is for. [Pulse]
- **consider** (motion, all): Use a gentle float or idle animation to make a static, waiting element feel alive. Why: Float makes a static element feel alive and weightless. [Float; Idle animation]
- **consider** (motion, all): Use a blur filter to soften an element or mask tiny imperfections. Why: Blur can mask tiny imperfections. Values: blur. [Blur]
- **consider** (motion, css): Use clip-path for reveals, masks and before/after sliders. Why: Clip-path clips an element to a shape. Values: clip-path. [Clip-path]
- **consider** (motion, css): Use a mask instead of clip-path when a reveal needs soft, fadeable edges. Why: Mask is like clip-path but with soft, fadeable edges. Values: mask. [Mask]
- **consider** (motion, all): Animate changing text character by character (text morph) when attention should go to the new value. Why: Text morph draws attention to the new value. [Text morph]
- **consider** (components, all): Show a skeleton placeholder with a moving shimmer while content loads. Why: That is the skeleton or shimmer loading pattern. [Skeleton / Shimmer]
- **must** (typography, all): Use tabular (fixed-width) numbers for tickers, timers and counters. Why: Numbers don't shift around as they change; described as essential. Values: Tabular numbers. [Tabular numbers — ... Essential for tickers, timers, and counters.]
- **should** (motion, all): Treat 60fps as the baseline for smooth motion; newer displays run at 120fps. Why: 60fps is the baseline for smooth motion; 120fps on newer displays. Values: 60fps, 120fps. [Frame rate (FPS)]
- **should** (motion, web): Animate transform and opacity so the GPU can move or fade the element on its own layer. Why: Animating transform and opacity lets the GPU keep motion smooth, without redoing layout or paint. Values: transform, opacity. [Hardware acceleration; Compositing]
- **should** (motion, web): Avoid animating layout properties like width, height, top or left. Why: They force the browser to recalculate layout every frame, causing jank. Values: width, height, top, left. [Layout thrashing]
- **consider** (motion, css): Add will-change to an element that is about to animate so the browser can promote it to its own layer ahead of time. Why: It is a hint that lets the browser prepare a layer. Values: will-change. [will-change]
- **must** (motion, all): Give every animation a function (orient, give feedback or show relationships); do not animate only to decorate. Why: Motion should orient, give feedback or show relationships, not just decorate (Principles to Know). [Purposeful animation]
- **must** (motion, all): Make an animation shorter and subtler the more often a user sees it. Why: Listed under Principles to Know; the source gives no further reason. [Frequency of use]
- **should** (accessibility, all): Respect prefers-reduced-motion by toning down or removing motion. Why: Listed under Principles to Know, the concepts that guide when and how to animate. Values: prefers-reduced-motion. [Reduced motion]
- **consider** (motion, all): Use the right animation to make the interface feel faster. Why: The right animation makes an interface feel faster, even when it isn't. [Perceived performance]
- **consider** (motion, all): Add a small wind-up in the opposite direction before a move to hint at what is about to happen. Why: Anticipation hints at the coming motion. [Anticipation]
- **consider** (motion, all): Let parts of an element keep moving and settle slightly after the main motion stops. Why: Follow-through adds weight. [Follow-through]
- **consider** (motion, all): Deform an element as it moves (squash and stretch) to convey weight, speed and flexibility. Why: That is what squash and stretch conveys. [Squash & stretch]
- **consider** (components, all): Show or hide a section by smoothly expanding and collapsing its height (accordion / collapse). Why: That is how the glossary defines accordion / collapse. [Accordion / Collapse]
- **consider** (motion, all): Use a morph when one shape should smoothly turn into another, as in Dynamic Island. Why: That is how the glossary defines morph. [Morph — One shape smoothly turns into another shape, e.g. Dynamic Island.]

### Decisions it informs

- Which easing curve should a given motion use?
  - Ease-out: Starts fast, ends slow. When: The default for most UI and anything responding to the user.
  - Ease-in: Starts slow, ends fast; can feel sluggish. When: Usually avoided.
  - Ease-in-out: Slow, fast, slow. When: Elements already on screen moving from A to B.
  - Linear: Constant speed. When: Only spinners or marquees; avoid for UI.
  - Asymmetric easing: Accelerates and decelerates at different rates; feels more alive than a symmetric curve. When: When a curve should feel more alive.
  - Custom cubic-bezier: A curve you define yourself. When: When you need precise control.
  - Recommendation: Ease-out by default for UI and user responses; ease-in-out for on-screen A-to-B moves; linear only for spinners and marquees.
- Should motion use fixed-duration easing or spring physics? (`Q-motion-04`)
  - Fixed-duration easing: Motion runs for a set duration along an easing curve. When: When a set duration is wanted. [inferred]
  - Spring physics: Motion is driven by tension, mass and damping; it carries velocity into the next animation when interrupted and has a perceptual duration. When: When motion should keep velocity after a drag or interruption. [inferred]
- How should a spring feel?
  - Snappy: Higher stiffness pulls harder toward the target and feels snappier. When: When the element should arrive quickly. [inferred]
  - Bouncy: Lower damping gives more bounce and oscillation; bounce overshoots and settles. When: When the moment should feel playful.
  - Heavy: More mass makes it slower and more sluggish. When: When the element should feel heavy.
- How should an element appear or disappear?
  - Fade in / fade out: Changes opacity only. When: Simple appear and disappear.
  - Slide in: Enters from off-screen left, right, top or bottom. When: When the element comes from an edge.
  - Scale in: Grows from smaller to full size, often with a fade. When: When the element should grow into view.
  - Pop in: Appears with a slight overshoot, as if bouncing into place. When: When a playful overshoot fits. [inferred]
  - Reveal: Content is uncovered gradually with a clip-path or mask. When: When content should be uncovered rather than moved.
- How should one state, view or element connect to the next? (`Q-motion-06`)
  - Crossfade: One element fades out as another fades in, in the same spot. When: Replacing content in place.
  - Continuity transition: Visually connects before and after, e.g. the same rectangle growing and shrinking. When: When the user must stay oriented.
  - Morph: One shape smoothly turns into another, e.g. Dynamic Island. When: When one shape becomes another.
  - Shared element transition: An element travels and transforms from one position into another, like a thumbnail expanding into a card. When: When an item grows into a larger view, like a thumbnail expanding into a card.
  - Layout animation: Size or position changes animate to the new spot instead of snapping. When: When an element's size or position changes.
  - Direction-aware transition: Slides one way going forward and the opposite way going back. When: Navigation that should feel directional.
  - Page or view transition: Plays when navigating between pages or routes; a view transition has the browser morph between states and connect shared elements. When: Route and page changes.
- When reduced motion is on, should motion be toned down or removed? (`Q-motion-07`)
  - Tone down: Motion stays but is reduced. When: Respecting prefers-reduced-motion while keeping some motion.
  - Remove: Motion is removed. When: Respecting prefers-reduced-motion fully.
  - Recommendation: Either, as long as the prefers-reduced-motion setting is respected.
- Should a reveal use clip-path or a mask?
  - Clip-path: Clips the element to a shape. When: Reveals, masks and before/after sliders.
  - Mask: Like clip-path but with soft, fadeable edges, using a shape or gradient. When: When the edge should be soft.
- How should a looping animation repeat?
  - Loop: Repeats a set number of times or infinitely, jumping back to the start. When: Continuous motion such as a marquee. [inferred]
  - Alternate (yoyo): Plays forward then reverses each iteration. When: When the loop should reverse instead of jumping back to the start.
- How should motion relate to scrolling?
  - Scroll reveal: Elements fade or slide into place as they enter the viewport. When: Content appearing on scroll.
  - Scroll-driven animation: Animation progress is tied directly to scroll position. When: When scroll should scrub the animation.
  - Parallax: Background and foreground move at different speeds, creating depth. When: When scrolling should show depth.
- Where should a popover or menu grow from?
  - Its own center: The CSS default: the element animates from its own center. When: Not stated; it is simply what happens without setting an origin. [inferred]
  - Its trigger (origin-aware): The element animates out of its trigger, like a popover growing from the button that opened it. When: Elements opened from a trigger, such as popovers.
- How should a press be acknowledged?
  - Press / tap feedback: A subtle scale-down when the element is clicked, so it feels physical. When: When the element should feel physical.
  - Ripple: A circle expanding from the point of the tap, confirming the press. When: When the press should be confirmed from the exact tap point. [inferred]

### Process

1. Wait for a question: When invoked without a question, reply only with the ready line and nothing else until the person asks.
2. Read for intent: Map what the person sees or feels ('springy', 'slides off', 'draws itself in') to a glossary term rather than matching keywords.
3. Answer with the term: Reply as '**Term** — description', quoting the glossary description verbatim.
4. Offer alternates: If several terms fit, give the best match first, then 1–2 alternates with a one-line note on how each differs.
5. Disambiguate close terms: Contrast competing terms such as Clip-path vs Mask, Pop in vs Bounce, Shared element transition vs Layout animation.
6. Handle no exact match: Name the closest term and say it is an approximation, or combine glossary words (e.g. 'a stagger of scale-in entrances').
7. Stay within the glossary: If a term is not in the glossary, say so rather than inventing one; explain the concept with glossary words.
8. Keep it tight: Lead with the name and expand only if asked.
9. Keep sources in sync: Update the glossary and the project's /vocabulary page together when either changes.

### Examples and visual references

- A popover that grows out of the button that was clicked, answered as 'Origin-aware animation': Shows a feel-based description mapped to a term; the popover scales from its trigger instead of its own center.
- 'The thing where one image turns into another image', answered as Morph with Crossfade and Shared element transition as alternates: Demonstrates disambiguation: crossfade if they fade over each other in place, shared element transition if the element travels and transforms.
- An iOS scroll that resists and snaps back when pulled too far, answered as Rubber-banding (iOS): Physics feel mapped to a term: resistance and snap-back past a boundary.
- Dynamic Island as the example of a morph (Dynamic Island): One shape smoothly turns into another shape.
- A thumbnail expanding into a card: The example of a shared element transition.
- The same rectangle getting bigger and smaller: The example of a continuity transition that keeps the user oriented.
- A countdown timer: The example of a stepped animation divided into discrete steps.
- A before/after slider: A draggable divider that wipes between two overlaid images; one use of clip-path.
- 'A stagger of scale-in entrances': Shows how to describe an effect with no exact name by combining glossary terms.
- A drawer or toast dragged off-screen to close it: The examples given for swipe to dismiss.
- Spinners and marquees: The only places the glossary reserves linear (constant-speed) easing for.

### Numbers

- 60fps: Baseline frame rate for smooth motion [Frame rate (FPS)]
- 120fps: Frame rate on newer displays [Frame rate (FPS)]
- 0%, 50%, 100%: Example keyframe points the browser fills the gaps between [Keyframes]
- 1–2: Number of alternate terms to list after the best match [then 1–2 alternates with a one-line note]

<!-- /od:learn -->
