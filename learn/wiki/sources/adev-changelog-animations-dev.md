---
type: source
title: animations.dev
created: 2026-09-27
updated: 2026-09-27
video_id: adev-changelog
url: https://animations.dev/changelog
channel: "animations.dev (public pages only; the course itself is paid and closed) (web)"
published: Unknown
authority: non-negotiable
tags:
  - animation
  - easing
  - duration
  - ease-out
  - css-animations
  - motion-react
  - springs
  - clip-path
  - svg
  - ai-review
  - judgement
  - debugging-motion
---

# animations.dev

## Metadata

- Video ID: `adev-changelog`
- Channel: animations.dev (public pages only; the course itself is paid and closed) (web)
- Published: Unknown
- URL: https://animations.dev/changelog

## Summary

The public changelog of the paid animations.dev course (by Emil Kowalski, per the site's home page [inferred]) records every content update from the first release (September 2024) to April 2026. Most of it describes lessons rather than teaching them, but it does publish a short excerpt of the course's animation guidelines: default to ease-out, keep animations under 1s (unless illustrative) and mostly around 0.2s to 0.3s, and avoid built-in CSS easings other than ease and linear. It also shares two practical debugging tips (try blur-sm when an animation feels off; record the animation and play it back frame by frame) and warns that AI-generated motion works but feels mediocre, so the maker must train the judgement to spot and fix it. For a design system this gives hard duration and easing defaults for motion tokens, a review habit for AI-written motion, and a list of reference builds (toast, tabs with clip-path, hold-to-delete button, navigation menu, SVG hero illustration) that show where each technique belongs.

## Key Ideas

- Default to ease-out, and keep most UI animations around 0.2s to 0.3s; nothing should pass 1s unless it is illustrative.
- Built-in CSS easing keywords are off limits except ease and linear.
- AI can produce motion that works but feels mediocre; if you cannot tell the difference you will ship it, so judgement has to be trained.
- Judgement is trained by comparing two animations side by side, choosing the better one, writing down why, and checking against an expert breakdown.
- When an animation feels off and you cannot say why, record it and step through it frame by frame to see details missed at normal speed.
- A small blur (blur-sm) is a listed practical fix for an animation that feels off.
- Teaching by bad-versus-good examples shows the difference a proper animation makes.
- Giving an AI coding tool a rules or skill file with the animation principles lets it review animations and help properly.
- Spring-driven interactive graphs (useSpring) belong in illustrations, not functional charts such as stock charts.
- CSS transforms are the foundation of web animation; transitions, keyframes, 3D transforms and clip-path build on them.
- clip-path is described as very useful but underrated, and is used to build a tabs component.
- SVG animation needs the fundamentals first: coordinate system and viewBox, path syntax, stroke properties for path drawing, and correct transform origins.
- Building a component is not only implementation: easing and duration are part of the work.
- Animations can be a way to show uncommon care and differentiate yourself (guest lesson by Josh Puckett).

## Entities

- [[entities/animations-dev|animations.dev]] (product): Paid, interactive web animation course whose changelog this is.
- [[entities/emil-kowalski|Emil Kowalski]] (person): Author of the changelog, which is written in the first person; identified as Emil Kowalski from the site's home page [inferred].
- [[entities/josh-puckett|Josh Puckett]] (person): Guest lesson author of 'Animations as Proof of Care', on differentiating yourself through animations.
- [[entities/dimi|dimi]] (person): Course student who worked with the author on the new animations.dev hero animation; basis of a 6 lesson walkthrough.
- [[entities/dennis-brotzky|Dennis Brotzky]] (person): Interviewed (from Fey) about his path and how he thinks about motion at Fey.
- [[entities/fey|Fey]] (company): Company where Dennis Brotzky works; discussed in the motion interview.
- [[entities/lochie-axon|Lochie Axon]] (person): Design engineer at Family, interviewed about animation thinking and the twelve basic principles of animation.
- [[entities/family|Family]] (company): Company where Lochie Axon works; one of his components is shown.
- [[entities/motion-motion-react|Motion (motion/react)]] (library): React animation library; the course examples were moved from framer-motion to motion/react (the renamed Framer Motion [inferred]).
- [[entities/usespring|useSpring]] (concept): Motion hook covered in the hooks lessons; used to build an interactive graph for illustrations.
- [[entities/usetransform|useTransform]] (concept): Motion hook covered alongside useSpring; described as rarely used but very powerful.
- [[entities/clip-path|clip-path]] (concept): CSS property the course calls very useful but underrated; used to build tabs and the Hold to Delete button exercise.
- [[entities/svg-viewbox|SVG viewBox]] (concept): SVG coordinate system taught in the SVG fundamentals lessons before path-drawing animation.
- [[entities/cursor-rules-file-skill-md|Cursor Rules file / skill.md]] (tool): A file of the course's animation principles for coding agents (Cursor, Claude Code, Codex) so they can review animations and suggest improvements.
- [[entities/claude-code|Claude Code]] (tool): Coding agent shown previewing the course skill.md.
- [[entities/cursor|Cursor]] (tool): AI code editor the rules file and SKILLS.md target.
- [[entities/codex|Codex]] (tool): Coding agent the updated skill file added support for.
- [[entities/twelve-basic-principles-of-animation|Twelve basic principles of animation]] (concept): Classic animation principles discussed in the Lochie Axon interview.

## Topics

- [[topics/easing-and-timing|Easing and timing]]: Guideline excerpt: default to ease-out; never longer than 1s unless illustrative; most animations around 0.2s to 0.3s; do not use built-in CSS easings unless ease or linear; use specific easings per use case (list cut off in the public page). The navigation menu walkthrough focuses on easing and duration, not only code.
- [[topics/motion-principles|Motion principles]]: The refreshed theory module teaches through bad-versus-good examples; a practical tips lesson (15+ tips) is a reference for when you feel stuck. Josh Puckett's guest lesson frames animation as proof of care.
- [[topics/design-taste-and-judgement|Design taste and judgement]]: The 'Train your judgement' lesson (25+ exercises) trains spotting, naming and fixing what is wrong by choosing between two animations side by side and writing down why.
- [[topics/ai-assisted-design|AI-assisted design]]: AI produces motion that works but feels mediocre. The course ships a Cursor Rules file and skill.md with its principles so LLMs can review animations and answer motion questions; lessons have a copy-as-markdown button for feeding content to LLMs.
- [[topics/spring-animation|Spring animation]]: Hooks lessons cover useSpring and useTransform; a spring visualiser shows parameters such as mass (with decimals). Spring-driven interactive graphs are for illustrations, not functional charts.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: CSS module order: transforms, transitions, keyframe animations (blinking cursor, orbiting with 3D transforms), then clip-path (tabs). Examples moved from framer-motion to motion/react.
- [[topics/toasts-and-notifications|Toasts and notifications]]: A toast component is built with CSS transforms and transitions in the CSS module.
- [[topics/buttons-and-actions|Buttons and actions]]: A 'Hold to Delete' button exercise combines a scale-down animation with a linear transition for the button color, practising clip-path.
- [[topics/navigation-and-sidebars|Navigation and sidebars]]: A 3-part walkthrough builds a navigation menu component, with attention to easing and duration.
- [[topics/icons-and-imagery|Icons and imagery]]: The hero illustration walkthrough (6 lessons) covers SVG coordinate system and viewBox, path syntax, stroke properties for path drawing, and transform origins for SVG transforms, then two specific hero animations.
- [[topics/accessibility|Accessibility]]: The course site itself moved to more distinct, yellow focus states and added English captions to all videos.
- [[topics/design-resources|Design resources]]: A 'Vault' of resources is updated regularly, and interviews with practitioners (Dennis Brotzky at Fey, Lochie Axon at Family) are part of the course.
- [[topics/typography|Typography]]: The course platform added a serif font for better emphasis of important words, and typography updates such as nicer commas and quotes.

## Notable Claims

- AI produces motion that works but feels mediocre, and people who cannot tell the difference will ship it. Evidence: AI produces motion that works, but feels mediocre
- Most animations should be around 0.2s to 0.3s and none longer than 1s unless illustrative. Evidence: most of them should be around 0.2s to 0.3s
- Built-in CSS easings should not be used except ease and linear. Evidence: Don't use built-in CSS easings unless it's `ease` or `linear`
- Recording an animation and playing it back frame by frame helps you see it in a new light and notice details missed at normal speed. Evidence: record it and play it back frame by frame
- useSpring and useTransform are not used often but are very powerful. Evidence: These hooks are not used often, but they are very powerful.
- Spring-driven interactive graph interactions are meant for illustrations, not functional graphs like stock charts. Evidence: this type of interaction is meant for illustrations, not functional graphs like stock charts
- clip-path is a very useful but underrated tool. Evidence: a very useful, but underrated tool
- CSS transforms are the foundation of web animations. Evidence: the foundation of web animations by learning about CSS transforms
- Bad-versus-good examples show the difference a proper animation makes. Evidence: leans much more into bad vs good examples to really show you the difference a proper animation makes
- A rules file containing the theory principles lets an LLM know how to help with animations properly. Evidence: contains all the principles from the theory lessons so that an LLM knows how to help you properly
- The course skill.md can review animations, suggest improvements and answer motion questions based on the author's experience. Evidence: It can review your animations, suggest improvements, and basically answer all your motion-related questions
- Animations can be used to differentiate yourself and show uncommon care. Evidence: how to differentiate yourself through animations and showcase uncommon care
- The orbiting keyframe animation, though it might not look amazing, unlocks lots of possibilities as it introduces 3D transforms. Evidence: it unlocks lots of possibilities as we learn about 3D transforms

## Quotes

> AI produces motion that works, but feels mediocre
> Default to use `ease-out` for most animations.
> Animations should never be longer than 1s (unless it's illustrative)

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: This is a changelog and marketing page for a paid, closed course; it describes lessons rather than teaching them, so only a handful of rules are actually stated.
- Caveat: The easing guideline list is cut off mid-sentence on the public page ('Use the following easings for their described use case:'), so the specific curves are not available from this source.
- Caveat: The blur-sm tip is named but not explained; how much blur and on which property is not stated.
- Caveat: Interviews, guest lessons, the Vault, certificates, video features and enrollment details are course product plugs, not design guidance.
- Caveat: The page text was extracted from an interactive site; interactive demos (hover cards, graphs, hero illustration, Claude Code preview) appear only as labels.
- Caveat: Dated: entries run from January 2025 to April 2026, and the page says enrollment reopens in 2027.
- Caveat: The guidelines conflict on their face: 'Default to use `ease-out`' names a built-in CSS keyword, while the easing rule allows only the built-in `ease` and `linear`. The likely reading is a custom ease-out curve from the cut-off list [inferred]; confirm against the emilkowalski/skills source before setting a token value.
- Caveat: The guideline excerpt is a preview of the July 2025 Cursor Rules file; the skill file has been revised since (January and April 2026 entries), so the current wording may differ.
- Caveat: The platform improvements turned into 'consider' rules (focus states, captions, serif emphasis, punctuation, copy as markdown) are changes to the course site, not stated design guidance.

### Rules and practices

- **must** (motion, all): Use an ease-out curve as the default easing for most animations. Read with the rule on built-in easings, this means a custom ease-out curve rather than the built-in `ease-out` keyword [inferred]. Why: It is the first item of the course's published animation guidelines, under the heading 'Keep your animations fast'; the page gives no further reason. Values: ease-out. [Default to use `ease-out` for most animations.]
- **must** (motion, all): Never make an animation longer than 1s unless it is illustrative. Why: Listed under the guideline heading 'Keep your animations fast'; illustrative animation is the only stated exception. Values: 1s. [Animations should never be longer than 1s (unless it's illustrative)]
- **should** (motion, all): Keep most animation durations around 0.2s to 0.3s. Why: Listed under the guideline heading 'Keep your animations fast'. Values: 0.2s, 0.3s. [most of them should be around 0.2s to 0.3s]
- **must** (motion, css): Do not use CSS's built-in easing keywords other than `ease` and `linear`. Why: Stated under 'Easing rules' in the course guidelines; the page gives no reason, and the custom curves it points to next are cut off. Values: ease, linear. [Don't use built-in CSS easings unless it's `ease` or `linear`]
- **should** (motion, all): Use each easing curve for its described use case. Why: Stated in the course guidelines ('Use the following easings for their described use case'); the list of curves and cases is cut off on the public page. [Use the following easings for their described use case]
- **consider** (motion, all): When an animation feels off, try adding a small blur (`blur-sm`). Why: Named as one of the course's practical animation tips for an animation that feels off; the page does not explain how or where to apply it. Values: blur-sm. [One tip talks about using blur-sm when your animation feels off.]
- **should** (process, all): When an animation feels off but you cannot tell why, record it and play it back frame by frame. Why: It shows the animation in a new light and helps you notice details you might have missed at normal speed. [record it and play it back frame by frame]
- **must** (process, all): Do not ship AI-generated motion just because it works; review it, name what is wrong and fix it. Why: AI produces motion that works but feels mediocre; if you cannot tell the difference you will ship it and settle for good enough, which the source says is not good enough. [AI produces motion that works, but feels mediocre]
- **should** (process, all): Train motion judgement by comparing two animations side by side, picking the better one and writing down why before reading an expert breakdown. Why: This trains the ability to spot what is wrong, name it and fix it. [Your job is to pick the better one, write down why you chose it]
- **should** (process, all): Explain motion choices with bad-versus-good examples side by side. Why: The refreshed theory module leans on bad vs good examples to really show the difference a proper animation makes. [leans much more into bad vs good examples to really show you the difference a proper animation makes]
- **should** (tooling, all): Give AI coding tools a rules or skill file containing your animation principles before asking them for motion work. Why: So an LLM knows how to help properly; the skill file can review animations, suggest improvements and answer motion questions. [contains all the principles from the theory lessons so that an LLM knows how to help you properly]
- **consider** (tooling, all): Offer a 'copy as markdown' action on documentation or lessons so their content can be fed to LLMs. Why: The course added one to every lesson so learners can feed the content to LLMs. [Added a copy as markdown button to every lesson so you can feed the content to LLMs.]
- **should** (patterns, react): Do not put spring-driven interactive graph behaviour (useSpring and related hooks) on functional data charts such as stock charts; keep it for illustrations. Why: The source says this type of interaction is meant for illustrations, not functional graphs. Values: useSpring. [this type of interaction is meant for illustrations, not functional graphs like stock charts]
- **consider** (tooling, react): Import Motion from `motion/react` rather than `framer-motion` in new code. Why: The course moved all its examples from framer-motion to motion/react; the page gives no reason. Values: motion/react, framer-motion. [Moved examples over from framer-motion to motion/react.]
- **consider** (components, all): For a hold-to-delete button, pair a scale-down animation with a linear transition for the button color. Why: This is how the course's 'Hold to Delete' exercise is built; it practises the clip-path lesson. Values: linear. [a scale down animation with a linear transition for the button color]
- **consider** (motion, css): Consider clip-path for components such as animated tabs. Why: The course calls clip-path a very useful but underrated tool and uses it to build the tabs component among others. Values: clip-path. [a very useful, but underrated tool]
- **consider** (components, css): Build toast enter and exit motion with CSS transforms and transitions. Why: The course's CSS module builds its toast component this way. [A toast component made with CSS transforms and transitions.]
- **consider** (motion, css): Use CSS keyframe animations for effects such as a blinking cursor or an orbiting element (the orbit uses 3D transforms). Why: These are the course's keyframe examples, from simple to more complex. [we’ll learn about keyframe animations. From animations like the blinking cursor]
- **should** (motion, web): Set transform origins correctly before applying transforms to SVG elements. Why: Using transform origins correctly for SVG transforms is one of the SVG fundamentals taught before the hero illustration animations. [How to use transform origins correctly for SVG transforms.]
- **consider** (motion, web): Animate SVG path drawing through stroke properties, working within the SVG's coordinate system and viewBox. Why: The SVG fundamentals lessons teach the coordinate system, viewBox and stroke properties for path drawing animations. [Stroke properties for path drawing animations.]
- **should** (process, all): Decide easing and duration as part of building every component, not only the implementation. Why: The navigation menu walkthrough focuses not only on the implementation but also on the easing, duration and so on. [not only focus on the implementation, but also on the easing, duration, and so on]
- **consider** (accessibility, all): Make keyboard focus states clearly distinct. Why: Listed as an improvement to the course platform ('More distinct, yellow focus states'); no reason is given. [More distinct, yellow focus states.]
- **consider** (accessibility, all): Give videos captions. Why: Listed as an improvement to the course platform (all videos now have English captions); no reason is given. [All videos now have English captions.]
- **consider** (typography, all): Consider a second, serif typeface to emphasise important words. Why: The course platform added a serif font for better emphasis of important words. [Added a new serif font for better emphasis of important words.]
- **consider** (typography, all): Use typographically correct punctuation, such as proper commas and quotes. Why: Listed as a typography improvement to the course platform ('nicer commas, quotes, etc.'); no reason is given. [Typography updates, nicer commas, quotes, etc.]

### Decisions it informs

- How long should a typical interface animation last?
  - Around 0.2s to 0.3s: Fast, responsive motion When: Most animations
  - Up to 1s: Noticeably longer motion When: Upper limit; not stated as a target for UI
  - Longer than 1s: Slow, showcase motion When: Only when the animation is illustrative
  - Recommendation: Keep most animations around 0.2s to 0.3s and never above 1s unless illustrative, so animations stay fast.
- Which easing should animations use by default?
  - ease-out: The default for most animations When: Most animations
  - ease or linear (built-in): The only built-in CSS easings allowed When: When their specific behaviour is wanted, e.g. linear for the button color transition in the Hold to Delete exercise
  - Other built-in CSS easings: Disallowed by the guidelines When: Never
  - Easings matched to a described use case: Each curve has a job When: Per the guidelines' use-case list (not visible on the public page)
  - Recommendation: Default to ease-out, and do not use built-in CSS easings other than ease and linear; read together, the default is a custom ease-out curve rather than the built-in keyword [inferred].
- Should a data graph get a springy, interactive hover animation?
  - Spring-driven interaction (useSpring and other hooks): Playful, physical response to the pointer When: Illustrations
  - No spring-driven interaction: Plain, functional chart When: Functional graphs such as stock charts
  - Recommendation: Use this kind of interaction for illustrations only, not functional graphs like stock charts.
- How should AI coding tools learn your animation standards? (`Q-dist-02`)
  - Rules file (e.g. Cursor Rules): Gives the LLM all the theory principles so it knows how to help properly When: Editors like Cursor
  - skill.md / SKILLS.md: Lets a coding agent review animations, suggest improvements and answer motion questions When: Claude Code, Cursor, Codex
  - Copy lesson content as markdown: Feeds specific guidance to an LLM on demand When: One-off questions
  - Recommendation: Give the tool a file with the animation principles so it can help properly (the course ships both a rules file and a skill file).

### Process

1. Pick, explain, compare: Look at two versions of an animation side by side, pick the better one, write down why, then compare your reasoning to an expert breakdown. Repeat until you can spot, name and fix what is wrong.
2. Review AI motion before shipping: Treat AI-generated motion as a draft that works but may feel mediocre; check it against the guidelines and fix it rather than settling for good enough.
3. Debug an animation that feels off: Record the animation and play it back frame by frame to notice details missed at normal speed; try a small blur (blur-sm); check the practical tips list when stuck.
4. Learn CSS animation in order: Start with CSS transforms (the foundation), then transitions (e.g. a toast), then keyframe animations (blinking cursor, orbiting with 3D transforms), then clip-path (tabs).
5. Learn SVG fundamentals before SVG animation: Understand the SVG coordinate system and viewBox, basic path syntax, stroke properties for path drawing, and transform origins, then build specific illustration animations.
6. Give AI tools the principles: Load a rules file or skill.md with the animation principles into the coding agent so it can review animations and suggest improvements; feed lesson content via copy-as-markdown when needed.
7. Design easing and duration with the component: When building a component such as a navigation menu, decide easing and duration alongside the implementation.

### Examples and visual references

- Two animations shown side by side with 'Select A' and 'Select B' buttons (animations.dev 'Train your judgement' lesson): Two identical mock pages ('Acme', 'Page content') animate differently; the learner picks the better one and explains why. Demonstrates comparison-based judgement training.
- Hero illustration with hover animations (animations.dev home page, built with student dimi): SVG illustrations that animate on hover; the basis of a 6-lesson walkthrough on SVG and two specific animations.
- Interactive SVG path example (animations.dev SVG fundamentals lesson): An SVG with viewBox="0 0 100 100", a path with stroke="hsl(47, 94%, 66%)" and strokeWidth="1.5", drawn over a 0-100 grid with Previous/Next steps, to teach path syntax.
- Hover card built with useSpring and useTransform (animations.dev Framer Motion hooks lesson): A card that reacts to hover; the author says it is not the most beautiful but good practice.
- Interactive graph built with useSpring (animations.dev Framer Motion hooks lesson): An illustrative graph that responds to interaction; explicitly not meant for functional charts like stock charts.
- Hold to Delete button (animations.dev clip-path exercise): A button that scales down while held, with a linear transition for the button color.
- Toast built with CSS transforms and transitions (animations.dev CSS Animations module): An 'Add toast' button triggers a toast animated only with CSS transforms and transitions.
- Blinking cursor and orbiting animation (animations.dev keyframe animations lesson): Simple to complex keyframe animations; the orbit introduces 3D transforms.
- Tabs component using clip-path (animations.dev clip-path lesson): Tabs labelled Payments, Balances, Customers, Billing listed twice in the page text (a duplicated layer, as a clip-path reveal would use [inferred]), with a 1x speed control.
- Navigation menu component (animations.dev 3-part walkthrough): Built with attention to easing and duration as well as implementation.
- Course site polish updates (animations.dev platform): More distinct yellow focus states, a serif font to emphasise important words, nicer commas and quotes, custom scrollbars in code blocks, and a light mode variant of the code editor.
- Spring visualiser (animations.dev spring lesson): Improved to allow decimals for parameters such as mass.
- Twitter DM screenshot in the 'Animating in Public' lesson (animations.dev): Per its alt text (image not viewed): a DM with Jordan Gonen discussing working opportunities, used to illustrate sharing animations publicly [inferred].

### Numbers

- 1s: Maximum animation length unless illustrative [Animations should never be longer than 1s]
- 0.2s to 0.3s: Typical duration for most animations [most of them should be around 0.2s to 0.3s]
- September 2024: Initial release of the course [all updates since the initial release (September 2024)]
- more than 35 lessons and 40+ exercises: Total course content [In total there are more than 35 lessons and 40+ exercises.]
- more than 25 exercises: Side-by-side comparisons in 'Train your judgement' [There are more than 25 exercises]
- 6 lesson: Hero illustration walkthrough series; the entry describes 3 lessons on SVG fundamentals and 2 on specific animations of the hero (the sixth is not described) [We decided to create a 6 lesson walkthrough series]
- 7 lessons: Theory module lessons refreshed [All 7 lessons have been updated]
- more than 15 tips: Practical Animation Tips lesson at launch; 5 added in Jan 2026 and 3 in Apr 2026 [It contains more than 15 tips]
- 3 part: Navigation menu walkthrough [a new, 3 part walkthrough series]
- 70%: Course completion needed for the certificate [after completing 70% of the course]
- hsl(47, 94%, 66%): Stroke color in the SVG path example [stroke="hsl(47, 94%, 66%)"]
- 0 0 100 100: viewBox of the SVG path example in the SVG fundamentals lesson [<svg viewBox="0 0 100 100">]
- 1.5: strokeWidth of the path in the same SVG example [strokeWidth="1.5"]

<!-- /od:learn -->
