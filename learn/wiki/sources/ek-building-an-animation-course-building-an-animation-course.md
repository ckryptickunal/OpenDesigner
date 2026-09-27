---
type: source
title: Building an animation course
created: 2026-09-27
updated: 2026-09-27
video_id: ek-building-an-animation-course
url: https://emilkowal.ski/ui/building-an-animation-course
channel: Emil Kowalski (web)
published: Unknown
authority: non-negotiable
tags:
  - easing
  - ease-out
  - press-feedback
  - interactive-demos
  - ai-skills
  - easing-tokens
  - changelog
  - onboarding
  - packaging
  - word-of-mouth
  - taste
---

# Building an animation course

## Metadata

- Page ID: `ek-building-an-animation-course`
- Publisher: Emil Kowalski (web)
- Published: Unknown
- URL: https://emilkowal.ski/ui/building-an-animation-course

## Summary

Emil Kowalski looks back on two years of building his animation course, animations.dev: how he stayed motivated, how he designed its packaging and platform, how he brought AI into it, and how it spread by word of mouth. The design lessons inside it are a compact easing decision flowchart (enter or exit uses ease-out, moving on screen uses ease-in-out, hover uses ease, constant motion uses linear, default ease-out), the point that a subtle scale-down on press makes an interface feel more responsive, and a set of named custom easings kept as CSS variables on :root. For a design system the main process lessons are that motion has to be felt through interactive demos rather than explained in text, that judgement about easing and duration is a human skill AI is not good at, that motion knowledge can be packaged as a SKILL.md for coding agents, and that a living product needs ongoing updates recorded in a changelog. Much of the page is testimonials and course promotion, which are not design rules.

## Key Ideas

- Pick an easing curve by what the element is doing: entering or exiting the viewport gets ease-out, moving or morphing on screen gets ease-in-out, a hover change gets ease, constant motion gets linear, and anything else defaults to ease-out.
- A subtle scale-down on press makes an interface feel more responsive.
- Good motion work is mostly deciding what not to animate, and aims at great interfaces rather than great demos (shadcn's endorsement of the course).
- People only understand motion by feeling the difference between good and bad themselves, so teaching and documenting motion needs interactive demos, not a wall of text.
- Choosing the right easing and duration is judgement that AI is not good at; intuition and taste are the differentiator when software is abundant.
- People who understand the code AI writes get more leverage from it.
- Motion knowledge can be packaged as a SKILL.md file that coding agents use to build, review and improve animations.
- Custom easing curves can be kept as a named set of CSS variables on :root.
- Packaging (logo, hero, onboarding) creates the first impression and signals the care people can expect from the rest of the product.
- Lower the barrier to practice: a built-in editor with no setup, auto-saved progress, and solutions as both video and text.
- A product that keeps getting free updates, refreshed modules and a changelog stays alive instead of becoming a snapshot in time.
- Teasing a project early can drain the motivation to finish it; a presale with a public deadline creates external pressure to ship.
- Making something great and showing it to a few people lets word of mouth do the marketing, as happened with Sonner, Vaul and the course.

## Entities

- [[entities/emil-kowalski|Emil Kowalski]] (person): Design engineer and author; built the course and draws on experience at Vercel and Linear.
- [[entities/animations-dev|animations.dev]] (product): Emil's animation course (announced as 'Animations on the Web'), the subject of the article.
- [[entities/aiforui-dev|aiforui.dev]] (product): A newer course by Emil, plugged at the top of the page; early access has closed.
- [[entities/ui-land|ui.land]] (product): An earlier Emil project teased in December 2021 and launched in January 2023; his example of how teasing hurt motivation.
- [[entities/sonner|Sonner]] (library): Emil's toast library, cited as spreading through organic word of mouth.
- [[entities/vaul|Vaul]] (library): Emil's drawer library, also cited as spreading through word of mouth.
- [[entities/shadcn|shadcn]] (person): Endorses the course: design engineering is mostly deciding what not to animate.
- [[entities/nev-flynn|Nev Flynn]] (person): Worked with Emil on the butter-cube logo.
- [[entities/motion-passport|Motion Passport]] (concept): A customisable personal identifier on the course's welcome page, used to set the tone on enrolment.
- [[entities/skill-md|SKILL.md]] (tool): A file students feed to coding agents, containing the course's motion knowledge, including the easing decision flowchart.
- [[entities/easing-decision-flowchart|Easing Decision Flowchart]] (concept): The snippet from the course skill file that maps what an element is doing to an easing keyword.
- [[entities/the-vault|The Vault]] (product): A curated collection of articles, videos and personal websites included as a course bonus.
- [[entities/anu-atluru|Anu Atluru]] (person): Author of 'Taste is Eating Silicon Valley', quoted on taste mattering in a world of abundance.
- [[entities/vercel|Vercel]] (company): Where Emil gathered motion experience; also a source of course interviewees.
- [[entities/linear|Linear]] (company): Where Emil gathered motion experience.
- [[entities/family|Family]] (company): Company of one of the interviewed designers.
- [[entities/fey|Fey]] (company): Company of one of the interviewed designers.
- [[entities/poolside|poolside]] (company): Company listed alongside one of the interviewees.
- [[entities/delphi|Delphi]] (company): A testimonial says every frontend engineer there has to take the course, paid by the company.
- [[entities/framer-motion|framer-motion]] (library): Named by a commenter as what most highly polished animation depends on, because of springs.

## Topics

- [[topics/easing-and-timing|Easing and timing]]: Gives the course skill file's easing flowchart: ease-out for entering or exiting the viewport, ease-in-out for moving or morphing on screen, ease for hover changes, linear for constant motion, ease-out as the default. Shows six of 18 named custom easings kept as --ease-* CSS variables. Says choosing easing and duration is judgement that AI is not good at.
- [[topics/micro-interactions|Micro-interactions]]: A subtle scale-down on press makes the interface feel more responsive; hero illustrations respond to hover and click; the logo melts over time through animated SVG paths.
- [[topics/motion-principles|Motion principles]]: Motion has to be felt to be understood, so the course relies on interactive demos. Through shadcn's endorsement it frames design engineering as mostly deciding what not to animate, and as building great interfaces rather than great demos.
- [[topics/ai-assisted-design|AI-assisted design]]: AI is good at code but weak at choosing easing curves and durations; people who understand the code get more leverage; motion knowledge packaged as a SKILL.md lets coding agents build, review and suggest improvements to animations.
- [[topics/design-taste-and-judgement|Design taste and judgement]]: The course aims to build intuition because the right judgement is the biggest differentiator when software is abundant; quotes Anu Atluru on treasuring taste in a world of abundance.
- [[topics/design-systems-and-tokens|Design systems and tokens]]: Custom easing curves are kept as a named set of CSS custom properties on :root (--ease-breeze, --ease-silk, --ease-swift, --ease-nova, --ease-crisp, --ease-glide shown out of 18).
- [[topics/onboarding|Onboarding]]: After enrolling, students land on a welcome page with a customisable Motion Passport, which sets the tone and shows the care to expect from the rest of the course.
- [[topics/design-process|Design process]]: Avoid teasing a project before it is done; a presale with a public deadline gives external motivation; treat the product as living with free updates, refreshed modules and a changelog; go the extra mile rather than ship something mediocre.
- [[topics/web-implementation-css-and-react|Web implementation (CSS and React)]]: Shows an exercise starter for a 'Hold to Delete' clip-path button in React, with a duplicated, aria-hidden overlay copy of the icon and label, and an SVG path-drawing demo; the built-in editor auto-saves code.
- [[topics/design-resources|Design resources]]: Course bonuses include the Vault of curated articles, videos and personal websites, interviews with designers and engineers, and 18 custom easings.
- [[topics/launch-and-marketing|Launch and marketing]]: Organic word of mouth is the best marketing: make something great, make sure a few people see it, and people will share it and answer others' questions about it.

## Notable Claims

- The presale for animations.dev launched in January 2024 with a goal of 1,000 students; more than 10,000 people have enrolled. Evidence: opening paragraph, 'My goal was to eventually get to 1,000 students'
- Teasing ui.land early made Emil less motivated to finish it, because talking about it already felt rewarding enough. Evidence: The work, 'A mistake I made previously with a project called ui.land'
- ui.land was teased in December 2021 and launched in January 2023. Evidence: The work, 'This teaser was posted in December of 2021'
- Offering a presale with zero content and a public deadline helped most, because people had already paid. Evidence: The work, 'deliberately offering a presale for the course when I had zero content'
- The course announcement was made before any work on the course began. Evidence: The work, 'This announcement was made before any work on the course began.'
- The look and feel of a product (its packaging) creates the initial impression, which is important. Evidence: The packaging, 'That's what creates the initial impression'
- The butter-cube logo was chosen because people often call good animations buttery smooth. Evidence: The packaging, 'People often call good animations buttery smooth'
- As enrolment gets closer to closing, the butter cube melts a little more each hour through animated SVG paths. Evidence: The packaging, 'easter egg'
- The animations.dev hero section was animated by a course student. Evidence: The packaging, 'a course student animated it'
- The Motion Passport welcome page sets the tone of the course and shows the care to expect from the rest of the content. Evidence: The packaging, 'Motion Passport'
- Students need to feel the difference between good and bad motion, and the only way is to experience it themselves. Evidence: The course platform, 'Each lesson is packed with interactive demos'
- A subtle scale-down on press makes the interface feel more responsive. Evidence: The course platform, caption under the 'Paste' demo
- A built-in code editor lowers the barrier to doing exercises because there is no repo to clone or environment to set up. Evidence: The course platform, 'built-in code editor'
- The course has more than 50 exercises, each with a video walkthrough and a written version of the solution. Evidence: The course platform, 'In total, there are more than 50 exercises'
- Choosing the right easing curves and duration is something AI is not great at. Evidence: Animations and AI, 'Something AI is not great at.'
- Intuition and judgement will be the biggest differentiator in a world where software is abundant. Evidence: Animations and AI, 'The right judgement is key'
- People who clearly understand the code will be even more leveraged, even though models are great at coding. Evidence: Animations and AI, 'who clearly understand the code will be even more leveraged'
- In 2024 most of the work on a custom platform could not be handed off to LLMs. Evidence: The work, 'Back in 2024 most of the things couldn't have been handed off to LLMs'
- The course's SKILL.md can review animations, suggest improvements, build animations and answer motion questions, based on Emil's experience at companies like Vercel and Linear. Evidence: Animations and AI, 'It can review your animations, suggest improvements'
- The animations.dev skill spans multiple files and is more nuanced than the free skill file based on Emil's blog posts. Evidence: Animations and AI, 'I also created a skill file based on my blog posts'
- Free updates with each enrolment are what people love most; the theory module has been fully refreshed. Evidence: Bonus features, 'free updates with each enrollment'
- Organic word of mouth is the best kind of marketing, and it happened to Sonner, Vaul and the course. Evidence: The marketing, 'this type of organic marketing is the best kind'
- Most highly polished animation depends on framer-motion because of springs (a commenter's opinion, not Emil's). Evidence: The marketing, comments on Ryan Florence's tweet
- The course was announced as 'Animations on the Web', a course about how to craft animations that make people feel something. Evidence: The work, announcement tweet of Jan 16, 2024
- The 'Animations and AI' lesson came out of the free updates, and its skill file is free to enrolled students as part of them. Evidence: Bonus features, 'That's how the “Animations and AI” lesson we talked about earlier was born.'
- Updates are not only new content: as Emil learns how to teach animation better, he refreshes existing modules, such as the theory module. Evidence: Bonus features, 'Updates don't just have to mean new content, though.'
- A product people cannot stop talking about is a win for everyone: users get value, the maker helps more people, and the product gets more exposure. Evidence: The marketing, 'It's a win for everyone.'

## Quotes

> In reality, it’s mostly deciding what not to animate.
> A subtle scale down on press makes the interface feel more responsive.
> They need to feel the difference between good and bad

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: Most of the page promotes Emil's paid course (animations.dev), a waitlist with preview lessons, and a newer course (aiforui.dev); these plugs are not design rules.
- Caveat: Most of the text is testimonials from other people; their praise, and claims such as Delphi requiring the course, are third-party opinions.
- Caveat: The 'deciding what not to animate' idea comes from shadcn's testimonial, not from Emil's own text on this page.
- Caveat: The easing flowchart is only a snippet of a larger, multi-file skill that is part of the paid course.
- Caveat: Only 6 of the 18 custom easings appear in the fetched text. All six visible curves have both control points below the diagonal, which makes them ease-in shaped, so they do not fit the flowchart's ease-out branch for entering elements [inferred].
- Caveat: The scale-down-on-press demo gives no scale value, duration or easing in the text.
- Caveat: The aria-hidden overlay and trash icon come from an exercise starter file; the article does not explain them, and styles.css is not shown.
- Caveat: The page has no publish date; tweets are dated up to January 2026, and the note that LLMs could not help much in 2024 is time-bound.
- Caveat: The comment that polished animation depends on framer-motion because of springs is a reader comment, not Emil's view.
- Caveat: Tweet like counts and the 10,000 enrolment figure are snapshots at the time of writing.
- Caveat: Code values (the cubic-bezier easings and aria-hidden="true") are written in normal CSS and JSX spacing; the extracted text adds spaces inside them, but every number and name is exact.
- Caveat: The page states no durations and no scale value for press feedback; do not attribute duration numbers to this source.

### Rules and practices

- **must** (motion, all): Use ease-out for any element entering or exiting the viewport. Why: The course's easing decision flowchart assigns ease-out to entering and exiting elements. Values: ease-out. [Easing Decision Flowchart, 'Is the element entering or exiting the viewport? Yes → ease-out']
- **must** (motion, all): Use ease-in-out for an element that moves or morphs while it stays on screen. Why: The flowchart assigns ease-in-out to on-screen movement and morphing. Values: ease-in-out. [Easing Decision Flowchart, 'Is it moving/morphing on screen? Yes → ease-in-out']
- **must** (motion, all): Use ease for hover changes. Why: The flowchart assigns ease to hover changes. Values: ease. [Easing Decision Flowchart, 'Is it a hover change? Yes → ease']
- **must** (motion, all): Use linear for constant motion; no other branch of the flowchart gives linear. Why: The flowchart assigns linear to constant motion and to nothing else. Values: linear. [Easing Decision Flowchart, 'Is it constant motion? Yes → linear']
- **must** (motion, all): When an animation is not entering or exiting, not moving or morphing on screen, not a hover change and not constant motion, default to ease-out. Why: The flowchart's fallback branch is ease-out. Values: ease-out. [Easing Decision Flowchart, 'Default → ease-out']
- **should** (motion, all): Choose each easing by walking the questions in order: entering or exiting the viewport, then moving or morphing on screen, then hover change, then constant motion. Why: The flowchart is ordered this way, so the enter/exit check wins before the others are considered. Values: ease-out, ease-in-out, ease, linear. [Easing Decision Flowchart]
- **should** (motion, all): Give pressable elements a subtle scale-down on press. Why: It makes the interface feel more responsive. [The course platform, caption under the 'Paste' demo]
- **should** (motion, all): Treat motion work as mostly deciding what not to animate, and aim at great interfaces rather than great demos. Why: shadcn's endorsement of the course: design engineering is mostly deciding what not to animate, and the course is about great interfaces, not great demos. [shadcn testimonial, 'Somewhere along the way, design engineering became about animations and slick demos']
- **should** (motion, all): Do not accept AI-chosen easing curves and durations without review by someone with trained motion judgement [inferred]. Why: Choosing the right easing curves and duration is something AI is not great at, and the right judgement is key; the review step itself is not stated in the source. [Animations and AI, 'how to choose the right easing curves, duration, etc. Something AI is not great at']
- **should** (process, all): Make sure the people shipping animation code understand how the code works, even when a model wrote it. Why: Those who clearly understand the code will be even more leveraged; understanding the code is still extremely valuable. [Animations and AI, 'Understanding how the code works is still extremely valuable.']
- **should** (tooling, all): Package the project's motion knowledge (such as the easing flowchart) as a SKILL.md file that coding agents load, so they can build, review and suggest improvements to animations. Why: The skill file gives immediate value and lets agents review animations, suggest improvements, build animations and answer motion questions. Values: SKILL.md. [Animations and AI, 'students get a SKILL.md file that they can feed to coding agents']
- **consider** (tokens, css): Keep custom easing curves as a named set of CSS custom properties on :root (--ease-breeze, --ease-silk and so on); not repeating raw cubic-bezier values is the likely benefit [inferred]. Why: This is how Emil's set of 18 custom easing functions, which he uses in his own animation work, is written; the page gives no reason for the format. Values: --ease-breeze: cubic-bezier(.55, .085, .68, .53), --ease-silk: cubic-bezier(.52, .062, .64, .21), --ease-swift: cubic-bezier(.86, .04, .67, .24), --ease-nova: cubic-bezier(.73, .065, .82, .08), --ease-crisp: cubic-bezier(.92, .06, .77, .045), --ease-glide: cubic-bezier(.58, .06, .95, .32). [Bonus features, 'A set of 18 custom easing functions that I use in my animation work.' (the numbers are exact; the extracted code block adds spaces inside cubic-bezier( ), removed here so the values are valid CSS)]
- **consider** (accessibility, web): When a component stacks a duplicate copy of its icon and label as a visual overlay (for example a 'Hold to Delete' overlay), mark the duplicate aria-hidden="true". Why: The course's ClipPathButton starter hides the overlay copy; the reason is not stated, but it keeps assistive technology from reading the label twice [inferred]. Values: aria-hidden="true". [Code Playground, 'ClipPathButton ... aria-hidden = "true" className = "hold-overlay"' (spaces around = removed)]
- **must** (process, all): Explain every motion concept with an interactive demo people can play with, not with text alone. Why: It is essential: people need to feel the difference between good and bad, and the only way is to experience it themselves, like touching a physical object to understand its texture. [The course platform, 'Each lesson is packed with interactive demos.']
- **should** (content, all): Do not present a visual subject such as animation as a dry wall of text. Why: Nobody wants to read a dry wall of text when the subject is that visual; demos are also more fun. [The course platform, 'Nobody wants to read a dry wall of text']
- **consider** (process, all): For technical concepts built up in steps (such as SVG path commands), use a step-through demo with Previous and Next that shows what each new step changes. Why: As you press the arrow the shape is drawn progressively, showing how each new command affects the SVG. [The course platform, 'The demo below is used in the SVG lesson']
- **consider** (tooling, web): Put a built-in code editor next to exercises so people can practise without cloning a repo or setting up a development environment. Why: It lowers the barrier to working on the exercises. [The course platform, 'It lowers the barrier to work on the exercises.']
- **should** (patterns, all): Auto-save work in progress in editors and exercises so stopping midway loses nothing. Why: If you stop in the middle of an exercise, your progress won't be lost. [your code is automatically saved, so if you ever stop in the middle of an exercise]
- **should** (content, all): Offer every walkthrough both as a video and as a written version. Why: Some people prefer the written version. [The course platform, 'a written version for those who prefer it']
- **consider** (process, all): When teaching something as complex as animation, build a platform tailored to the topic with interactive demos, exercises and custom components. Why: It makes the learning experience more engaging and effective. [The course platform, 'I need a platform tailored to the topic']
- **must** (process, all): Do not publicly tease that you are working on a project. (Emil's contrast is the presale he offered when he had zero content for the course: people had already paid and he had set a public deadline.) Why: Emil calls teasing ui.land a mistake: talking about it already felt rewarding enough, so he was less motivated to finish it; it was teased in December of 2021 and launched in January 2023. [A mistake I made previously with a project called ui.land was teasing that I was working on it]
- **consider** (process, all): Consider committing publicly with a presale and a public deadline before building, if you can handle the pressure. Why: People who have already paid create external motivation to finish. [The work, 'I set a public deadline and had to stick to it']
- **should** (process, all): Invest in the look and feel (the packaging) of a product, not only its core content. Why: People love beautiful things, and the packaging creates the initial impression. [The packaging, 'People love beautiful things']
- **consider** (process, all): Consider deriving the brand mark from the quality people associate with the work (for example 'buttery smooth' animation became a butter cube) and reuse it across the site in various forms. Why: The butter-cube logo came from how people describe good animation and is used across the site. [The packaging, 'I thought using a butter cube would be a good idea']
- **consider** (motion, web): Consider small interactive details in the first things people see, such as hero illustrations that animate on hover and respond to clicks, or an easter egg that changes over time. Why: Packaging creates the initial impression, and the hero also shows what the course enables people to do. [The packaging, 'Hover or click on them to see different interactions.']
- **should** (patterns, all): Design the first screen people see after signing up so it sets the tone and shows the care to expect from the rest of the product. Why: The onboarding is part of the packaging and the first impression of the product itself; the Motion Passport welcome page sets the tone. [The packaging, 'Another important aspect of the packaging is the onboarding']
- **should** (process, all): Treat the product as a living thing: keep shipping updates, and refresh existing sections as you learn better ways to explain them. Why: It keeps the product from dying out as a snapshot in time; Emil fully refreshed the theory module as he learned to teach better. [Bonus features, 'not a snapshot in time, but rather a living entity that evolves']
- **should** (process, all): Record every update on a changelog page. Why: To document all the updates. [Bonus features, 'To document all the updates, I created a changelog page.']
- **should** (process, all): Go the extra mile to make things great; do not ship something mediocre. Why: People naturally share things they like; Emil tries to make things he would be proud of, and says it won't always work but there is no point in making something mediocre. [The marketing, 'there's no point in making something mediocre']
- **consider** (process, all): After making something great, make sure at least a few people see it and let word of mouth carry it. Why: If you create great things and a few people see them, word will spread; organic marketing is the best kind. [The marketing, 'If you create great things, and make sure a few people see them']
- **should** (process, all): Aim to make a product that people cannot stop talking about. Why: It is a win for everyone: users get value, the maker helps more people, and the product gets more exposure. [The marketing, 'You have to create a product that people just can’t stop talking about.']
- **consider** (tooling, all): Ship the knowledge file for coding agents (the SKILL.md) as part of the product's ongoing updates, so existing users get it too. Why: The 'Animations and AI' lesson was born from the free updates, and its skill file is free as part of them. Values: SKILL.md. [Bonus features, 'The skill file included in that lesson is also free as part of the ongoing updates.']
- **consider** (content, all): Consider shipping a curated collection of trusted resources (articles, videos, personal websites) alongside the core material. Why: The Vault collects highly curated resources that helped Emil over the years, as a bonus students can learn from. [Bonus features, 'One of them is the Vault']

### Decisions it informs

- Which easing curve should this animation use? (`Q-motion-03`)
  - ease-out: The flowchart's curve for elements entering or exiting the viewport, and its default. When: The element enters or exits the viewport, or no other branch applies.
  - ease-in-out: The flowchart's curve for elements that move or morph while on screen. When: The element is moving or morphing on screen.
  - ease: The flowchart's curve for hover changes. When: It is a hover change.
  - linear: The flowchart's curve for constant motion. When: It is constant motion.
  - Recommendation: Pick by the element's job using the flowchart, and fall back to ease-out; this is a grouping of curves by role [inferred].
- How should motion decisions be explained to people learning or choosing them?
  - Written explanation: A wall of text; people cannot really understand motion until they experience it. When: Not recommended for a visual subject like animation.
  - Interactive demos: People play with the concept and feel the difference between good and bad themselves. When: Every motion concept; the source calls it essential.
  - Step-through demo: Previous and Next controls reveal the concept one step at a time, showing what each step changes. When: Technical concepts built up in steps, such as SVG path commands.
  - Video plus written walkthrough: Each exercise solution is available in the format people prefer. When: Walkthroughs of exercise solutions.
  - Recommendation: Use interactive demos throughout, step-through demos for technical build-ups, and both video and written walkthroughs for solutions, because people need to feel the difference themselves.
- How should AI be brought into motion work?
  - Let AI choose easing and duration: Fast, but AI is not great at choosing the right easing curves and duration. When: Not recommended without review.
  - Human judgement plus a motion SKILL.md for agents: People keep the judgement; agents get the house motion knowledge to build, review and suggest improvements. When: Whenever coding agents build or review animations.
  - Recommendation: Develop intuition and understand the code, and give coding agents a SKILL.md with the motion knowledge; the right judgement is key.
- Should the product be a finished snapshot or a living thing that keeps changing, and how are changes communicated? (`Q-gov-06`)
  - Snapshot in time: The product dies out after launch. When: Not recommended by the source.
  - Living product with ongoing updates and a changelog page: People keep learning new things; refreshed sections improve how things are explained; every update is documented. When: Anything people keep using over time.
  - Recommendation: A living product with ongoing updates, documented on a changelog page.
- How do you stay motivated to finish a large project?
  - Tease it early: Talking about it feels rewarding enough that motivation to finish drops; ui.land took from December 2021 to January 2023. When: Not recommended.
  - Presale with a public deadline: People have already paid, so there is external pressure to deliver on time. When: When you can handle the pressure.
  - Recommendation: A presale with a public deadline, as long as you can handle the pressure.

### Process

1. Commit before building: Avoid teasing the project; instead open a presale with a public deadline so people who paid create external motivation.
2. Design the packaging: Create a logo from the quality people associate with the work (buttery smooth became a butter cube), reuse it across the site, add interactive hero illustrations and small easter eggs, and design the welcome screen (Motion Passport) to set the tone.
3. Build a platform fit for the subject: Pack each lesson with interactive demos people can play with, use step-through demos for technical build-ups, and add a built-in code editor that auto-saves so there is no setup.
4. Write exercises with solutions in two formats: Give each exercise a video walkthrough and a written version of the solution.
5. Choose easing with the flowchart: Ask in order: entering or exiting the viewport (ease-out), moving or morphing on screen (ease-in-out), hover change (ease), constant motion (linear); otherwise ease-out.
6. Package the knowledge for agents: Turn the motion knowledge into a SKILL.md that coding agents load to build, review and improve animations, while people keep developing their own judgement and understanding of the code.
7. Keep it living: Ship ongoing updates, refresh sections when you learn to explain them better, and record every update on a changelog page.
8. Let quality market it: Go the extra mile, make sure a few people see the result, and let word of mouth spread it.

### Examples and visual references

- Press demo with a 'Paste' button (animations.dev lesson demo embedded in the article): Shows that a subtle scale-down on press makes the interface feel more responsive; no scale value is given in the text. The extracted text shows two 'Paste' buttons, probably a side-by-side comparison with and without the effect [inferred].
- Easing Decision Flowchart (animations.dev SKILL.md snippet): A text tree mapping enter/exit to ease-out, on-screen move or morph to ease-in-out, hover to ease, constant motion to linear, default ease-out.
- SVG path-drawing step-through demo (animations.dev SVG lesson): A 0-100 grid with an SVG (viewBox 0 0 100 100, stroke hsl(47, 94%, 66%), strokeWidth 1.5); pressing Previous and Next draws the path command by command to show what each command does.
- 'Hold to Delete' ClipPathButton exercise (animations.dev Code Playground (App.js, styles.css)): A React button that contains an aria-hidden 'hold-overlay' copy of the trash icon and label next to the visible icon and label; a 16 by 16 trash icon drawn with fill currentColor. From the names (ClipPathButton, hold-overlay, 'Hold to Delete') it is probably a clip-path reveal of the overlay while the button is held, but styles.css is not shown [inferred].
- Melting butter-cube logo (animations.dev): An easter egg: as enrolment gets closer to closing, the butter cube melts a little more each hour through animated SVG paths.
- Interactive hero illustrations (animations.dev hero section): Animated illustrations that animate on hover and some respond to clicks; animated by a course student.
- Motion Passport welcome page (animations.dev onboarding): After enrolling, a welcome page with a customisable personal identifier that sets the tone of the course.
- Named custom easing variables (animations.dev bonus easings): A :root block defining --ease-breeze, --ease-silk, --ease-swift, --ease-nova, --ease-crisp and --ease-glide as cubic-bezier values (6 of the 18 shown).
- The Vault (animations.dev bonus): A curated collection of articles, videos and personal websites (image not viewed).
- ui.land teaser (Twitter, Dec 15, 2021): A 'Coming soon' teaser for a project that launched in January 2023; the source's example of teasing too early.
- Physical packaging ideas (animations.dev (planned)): The packaging idea extended to physical goods: a possible sticker pack for early students and a set of animations.dev keycaps in the works; both are plans, not shipped.

### Numbers

- 1,000: Emil's original goal for the number of students [opening paragraph]
- 10,000: More than 10,000 people have enrolled at the time of writing [opening paragraph]
- January 2024: When the presale for animations.dev launched [opening paragraph]
- 2 years: How long Emil worked on the course ['working on this course over the last 2 years']
- December of 2021: When the ui.land teaser was posted (tweet dated Dec 15, 2021) [The work, 'This teaser was posted in December of 2021']
- January 2023: When ui.land launched, about a year after the teaser [The work, 'the project launched in January 2023']
- Jan 16, 2024: Date of the tweet announcing the course, made before any work on it began [The work, announcement tweet]
- 50: More than 50 exercises in the course [The course platform]
- 18: Custom easing functions Emil uses in his own work [Bonus features]
- cubic-bezier(.55, .085, .68, .53): --ease-breeze [Bonus features, :root block (numbers exact; spaces inside cubic-bezier( ) from the extracted code block removed)]
- cubic-bezier(.52, .062, .64, .21): --ease-silk [Bonus features, :root block (numbers exact; spaces inside cubic-bezier( ) from the extracted code block removed)]
- cubic-bezier(.86, .04, .67, .24): --ease-swift [Bonus features, :root block (numbers exact; spaces inside cubic-bezier( ) from the extracted code block removed)]
- cubic-bezier(.73, .065, .82, .08): --ease-nova [Bonus features, :root block (numbers exact; spaces inside cubic-bezier( ) from the extracted code block removed)]
- cubic-bezier(.92, .06, .77, .045): --ease-crisp [Bonus features, :root block (numbers exact; spaces inside cubic-bezier( ) from the extracted code block removed)]
- cubic-bezier(.58, .06, .95, .32): --ease-glide [Bonus features, :root block (numbers exact; spaces inside cubic-bezier( ) from the extracted code block removed)]
- 0 0 100 100: viewBox of the SVG lesson demo, drawn on a 0 to 100 grid [The course platform, SVG demo code]
- hsl(47, 94%, 66%): Stroke color of the SVG lesson demo path [The course platform, SVG demo code]
- 1.5: strokeWidth of the SVG lesson demo path [The course platform, SVG demo code]
- 0 0 16 16: viewBox of the 16 by 16 trash icon in the ClipPathButton exercise [Code Playground]
- every two weeks: How often waitlist sign-ups get tips by email [Try it out yourself]

<!-- /od:learn -->
