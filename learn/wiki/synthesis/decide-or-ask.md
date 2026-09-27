---
type: synthesis
title: Decide or ask
created: 2026-09-24
updated: 2026-09-24
sources:
  - eks-skills-prototype-skill
  - eks-skills-prototype-picker
  - eks-skills-animate-skill
  - eks-skills-pick-ui-library-skill
  - eks-skills-improve-animations-skill
  - eks-readme
  - ek-agents-with-taste
  - ek-developing-taste
  - ek-train-your-judgement
  - ek-you-dont-need-animations
  - ek-building-a-toast-component
  - ek-7-practical-animation-tips
  - eks-skills-emil-design-eng-skill
  - 7cTdCu8HMgM
  - HE4rLEQpiXY
  - ADaQuZS04Rc
  - t7mpEDXzjCg
  - 9WVt1CelBfg
  - xHD01_Onac0
  - PDcQJOPby1k
  - lkKGQVHrXzE
tags:
  - od-area-process
---

# Decide or ask

At every decision, OpenDesigner does one of two things:

- **It decides for the person.** It tells them in one line what it chose and how to change it, and records how the value was set.
- **It asks the person to pick.** It shows 2 to 4 options, each as a sample of the same real screen. Each option carries a **Now:** line (what changes today) and an **As it grows:** line (what the choice means with more screens, people, platforms and content).

This page covers the policy, how to ask, how to decide quietly, and the conflicts found while writing it. The short version is the "Decide or ask" table in `skills/opendesigner/references/rules.md` section 6. The Now and As it grows lines for the 30 high-impact questions are in `synthesis/impact.json`. `tools/build_data.py` copies them into the stage files and `questions.json`.

**How the sources count.** Emil Kowalski's site and skills are house standards (non-negotiable), cited here with their `STD-` ids. Kole Jain and Steve Schoger are trusted practitioners (reference). When a number or an "always" or "never" comes from only one of their videos, this page calls it opinion unless another source or OpenDesigner's own research agrees. No Mobbin videos have been analysed: the extractor skipped the four it found, and `learn/raw/mobbin/` holds no transcripts. So this page cites no Mobbin evidence.

## The policy

| The decision is... | How to tell | OpenDesigner... | What it says | Recorded as | Grounded in | Sources |
|---|---|---|---|---|---|---|
| **Settled by a house standard or a locked floor** | The rule is in `synthesis/standards.json` (for example easing, durations, reduced motion, touch targets), or it is an accessibility floor from `guardrails.md` (WCAG 2.2 AA contrast, 24 px targets, visible focus) | Applies it and locks it. It never asks, and never offers an option that breaks a standard | Once, in the first result: which areas the standards cover, and that the person can ask to change one | `standard` (locked) | rules.md §5 and §6; `standards.json` → `policy`; `guardrails.md` §4 | Agents don't reliably pick the right ingredients on their own [S-L19-014]. Make the call, give the reason in one line, and never present motion options as a menu [S-L19-018] (STD-process-review-taste-26). When a curated list has a clear answer, recommend one and don't offer a menu [S-L19-029]. Strict written rules mean the agent doesn't have to guess [S-L19-004] (STD-process-review-taste-55) |
| **Mechanical** | Earlier choices or a rule give one right answer: nested corner radius, text color on a filled button, contrast steps, hover shades | Keeps the default | Lists it in the stage summary | `auto_default` | rules.md §6 "Mechanical"; DC-L17-01 (G blocks are mechanical); DC-L17-08 ("auto-decide G blocks with visible defaults") | Nice defaults are named as a real reason Sonner succeeded, and the fewer details people have to notice, the better [S-L19-006] (STD-process-review-taste-50) |
| **Low impact, and the person didn't zoom in** | Weight low or medium: under pacing.json's `time_weight_rule`, the question's card has fan-out under 5 and it isn't a Quick question | Keeps the default | One line in the level summary, for example: "I also picked the grays and hover colors for you." | `auto_default` | pacing.json `time_weight_rule`; zoom.md levels 2 and 3 ("Plain voice: ask fewer"); DC-L18-08 (group up to 3 low-impact choices) | Rank by leverage and prefer a short list [S-L19-027] (STD-process-review-taste-09). Take the single piece with the most leverage and say why [S-L19-031] (STD-process-review-taste-42) |
| **Handed over** | The person says "you pick", "just do it" or "skip the rest", or the run is unattended | Decides, with a reason rooted in the product's personality and how often people use it | One line now, then again at the next gate and in the final summary | `delegated` | rules.md §5 and §7; zoom.md "People in a hurry" | When asked for a pick, answer from the product's personality and frequency of use, not looks alone [S-L19-031] (STD-process-review-taste-48). When nobody can answer, default to the top items by leverage [S-L19-027] (STD-process-review-taste-15) |
| **Owner input** | Only the business knows it: scope, audience, platforms, team, governance (block class I) | Always asks. If their words or files already point to an answer, it records that answer as a guess and says so | "I guessed people visit now and then, mostly on phones. Say if that's wrong." | `chosen`, or `assumed` when guessed | rules.md §6 (last row) and §7; pacing.json `assumed_owner_inputs_below_zoom2`; DC-L17-08 ("never auto-decide an I block") | Start from what users intend to do [S-L19-054]. A design system has to reflect the team's values: a lean startup needs something light, while Material Design is massive because it serves dozens of products [S-L19-054]. That is reference opinion from one video; DC-L11-02, which scopes version 1 to the products the pilot touches, agrees in spirit |
| **Taste, identity or high impact** | Weight high: the card has fan-out 5 or more, or it is a Quick question. That covers the 30 questions in `impact.json`, every question in pacing.json `top_decisions`, and anything that changes many tokens at once (brand color, style, font, corners, depth, motion) | Asks, with 2 to 4 visual samples of the same real screen and the recommended option first | Each option gets one **Now:** line and one **As it grows:** line | `chosen`, or `confirmed_default` when the person accepts the recommendation | rules.md §3.5, §4 and §6; pacing.json `top_decisions` and `thresholds.show_visual_if_reach_gt` | Build genuinely different versions behind a picker; the choice belongs to the person [S-L19-031]. Taste is a trained instinct: compare, pick, and say why [S-L19-008] [S-L19-011]. "Never let an AI choose" your colors or layout [S-L19-061]: one video's opinion, but [S-L19-103] shows AI defaulting to indigo and centering everything, and rules.md §10 lists the same generic tells |
| **User challenge** | Your recommendation would override something the person said | Never decides. It shows what they said, what you suggest and why, what you might be missing, and the cost if you are wrong | The person's answer wins | `chosen` | rules.md §6 "User challenge" | Break the system's rules on purpose, never by accident [S-L19-054] (reference) |

Two notes on the table:

- **Where "weight" lives.** rules.md §6 says "weight low in `pacing.json`". pacing.json holds the rule and the counts for each stage, but the weight of each question is in `questions.json` (the `weight` field). Both use the same rule.
- **Q-motion-01 is not a motion menu.** STD-process-review-taste-26 bans offering motion options as a menu when *building one animation*. Q-motion-01 asks something else: the product's motion personality, which STD-easing-duration-13 says should set how much motion there is. The easing, duration and springs of each animation are never asked; the standards set them [inferred]. The standards file records no conflict between these two.

## How to ask

**1. One decision per message, and the job first.** Say what the thing is for before the choice (rules.md §1 and §2.8).

**2. Two to four real options.**
- AskUserQuestion takes 4 options at most, and the house standard caps a prototype comparison at 5 variants [S-L19-031] (STD-process-review-taste-38).
- Each option is a direction on a named axis (layout, density, personality, motion or interaction) that you could defend shipping.
- Two options that differ only in accent color or wording count as one. Cut one instead of padding the list. Two truly different options beat three padded ones [S-L19-031] (STD-process-review-taste-37).
- OpenDesigner's brand research agrees: show 2 to 3 generated style tiles instead of one finished design (DC-L06-02, from Samantha Warren's method).
- When a question has more options, show the 3 closest and put the rest behind "more options" (rules.md §4).

**3. Recommended option first, with its reason.**
- Put the recommendation first, with a short reason rooted in the product's personality and how often people use it, not looks alone [S-L19-031].
- Word the question itself neutrally (rules.md §3.7).
- **Scope:** STD-process-review-taste-48 says never to pre-pick a favorite when handing off prototype variants of one UI piece. Design-system questions follow rules.md §3.5, which asks for a recommendation. The standard's own `conflicts` note treats the two as different jobs [inferred].
- When OpenDesigner runs a prototype round (several versions of one component), it follows STD-process-review-taste-48 as written: an honest table, no favorite, and a stop.

**4. Every option is the same real screen.**
- Build each sample from the person's own screen, or from the engine preview filled with their tokens.
- Use realistic copy, names and numbers. No lorem ipsum and no buttons that do nothing [S-L19-031] (STD-process-review-taste-40).
- Show real context: a toast needs a page behind it, and a card needs other cards beside it [S-L19-031] (STD-process-review-taste-43).
- Between samples, only the decision being asked changes, so the person sees its effect and nothing else [inferred].
- Practitioners agree:
  - Show the work in a realistic context, so people can see what the final product will be [S-L19-041].
  - Test with imperfect content, such as a very long name [S-L19-054].
  - Restyling one layout twice (warm and friendly, then modern and premium) shows two personalities on the same screen [S-L19-043].
  - A real product screenshot beats a generated fake screen [S-L19-103].
  - A real product makes a better reference for an AI than a busy Dribbble shot [S-L19-086].

**5. Full size, one at a time, with an instant switch.**
- Show one option at a time, full size. The person flips between them with number keys or arrow keys, and the swap itself has no animation [S-L19-031] [S-L19-030] (STD-process-review-taste-43 to -46).
- Side-by-side thumbnails distort spacing and scale.
- Kole Jain says the same about presenting work: show designs large, and don't squish many screens down until the detail is lost [S-L19-083].
- A small side-by-side overview can work as an index, but never as the view where the person judges [inferred].

**6. Let people feel motion and interaction.** When the choice is about motion, depth while scrolling, or gestures, the sample must play, so people can touch it (STD-process-review-taste-59) and try it the way users would, for example opening and closing it rapidly [S-L19-011] (STD-process-review-taste-32). Give it a replay button and a slow-motion option [S-L19-003] (STD-process-review-taste-30). "Don't describe, show" [S-L19-041].

**7. A Now line and an As it grows line on every option.**
- **Now:** one plain line on what changes today on this screen.
- **As it grows:** one plain line on what the choice means with more screens, more people, more platforms and more content.
- **Why these two lines:**
  - The prototype hand-off gives each variant "when it's the right choice" and "its cost" [S-L19-031].
  - Kole Jain puts the reasoning next to each design [S-L19-083].
  - The As it grows line matters because a design system is a set of decisions you stick to [S-L19-044], and it has to reflect the team and how many products it serves [S-L19-054].
- **Where they appear:** in a visual, the two lines are captions under each sample, and the chat message stays short (rules.md §1: "Show, then ask"). In plain text, they appear for questions with weight high (rules.md §4).
- **Where they come from:** `synthesis/impact.json`.

**8. Honest costs, and why it feels that way.** Every option names what it costs. Explain why an option feels the way it does and name the pattern behind it, instead of calling it good or bad [S-L19-008] [S-L19-011] [S-L19-004] (STD-process-review-taste-52). At the style screen (Q-dir-01), split the options into safe choices and risks, each risk with its gain and cost (rules.md §3.5, DC-L17-06). A risk may never break a hard rule (DC-L17-06).

**9. Always a free answer.**
- End with: "Pick one, say 'show me', or tell me what you want."
- Map their own words to the nearest option. Record a value outside the options exactly as given (rules.md §4, §5 and §7).
- If they lean toward one option, run another round of options around it ("riff") [S-L19-031], or take one part from another option (`OD:remix`, rules.md §9).

**10. Likes and dislikes, once per taste area.** When the person zooms into direction, color, type, corners or motion, ask once for an example they like and one they dislike (rules.md §3.6). Taste is trained on great work [S-L19-008].

**11. After they pick.**
- Record the answer as `chosen`, with their words.
- Lock identity values such as brand colors.
- Confirm in one sentence, rebuild, and name the later decisions that moved (rules.md §5, §7 and §9).
- Only the pick goes forward. The other options stay in the log (DC-L17-05), and a prototype surface is deleted [S-L19-031] (STD-process-review-taste-49).

**Where the samples appear.** Use the best surface the host has, following the visual ladder in SKILL.md: a host-rendered template, a Figma or Paper canvas, a local page, the host's question tool, or plain text. Every visual has a text version. The text version of a card, with the lines from `impact.json` shortened:

```
How round should corners be?
  A) Slightly rounded, 4-6 px (recommended: your app is a busy work tool)
     Now: businesslike, like Primer and Atlassian.
     As it grows: the safest default across audiences; containers get 8-12 px.
  B) Rounded, 8-12 px
     Now: friendly and modern, like Polaris and Airbnb.
     As it grows: nested cards need matching inner corners.
  C) Pill
     Now: consumer, playful and touch-first.
     As it grows: needs taller controls, so it fits poorly in dense data tools.
  More options: square (0-2 px), or set by size
Pick one, say "show me", or tell me what you want.
```

## How to decide quietly without surprising people

1. **Look first.**
   - Before deciding, check the existing tokens, CSS and installed libraries, the product's personality, and how often each screen is used [S-L19-031] (STD-process-review-taste-11).
   - Use what the project already has. If something else would be better, flag it, but don't swap it without being asked [S-L19-029]. This is rules.md §3.1.
2. **Say it in one line, with the reason.** For example: "I kept corners slightly rounded (6 px), because it's a busy work tool." Make the call and state the reasoning in one line [S-L19-018] (STD-process-review-taste-26 and -28).
3. **Say how to change it.** Every quiet decision is one message away: "Say 'rounder' or 'change the corners'." Show the question id only when the engineer voice leads (rules.md §4).
4. **Record how it was set.** Use `standard`, `auto_default`, `delegated` or `assumed` (rules.md §5). A recommendation you made is not an answer you received (rules.md §3.8).
5. **Group the quiet ones.** List them in one line at the next gate or level summary. No dial numbers, token lists or hex codes unless the person asks (rules.md §8; zoom.md "The first result").
6. **Mention the standards once.**
   - Say once, in the first result, which areas the house standards already settle.
   - A person changes a standard only by asking. The agent then restates the standard and its reason once, records the change with the person's own words, and keeps the old record instead of deleting it (`standards.json` → `policy.override`).
7. **Call a guess a guess.** Owner inputs taken from the person's words go in the first result as "I guessed…" (zoom.md "The first result"; rules.md §5 `assumed`).
8. **Don't quietly pick identity.**
   - When a person in a hurry hands over the brand color, style or font, pick from their words and files, call it a starting point (the Q-color-01 hook), and flag it once.
   - AI tools tend to land on an indigo accent, centered layouts and the basic, default version of Inter [S-L19-103]. Kole Jain says never to let an AI pick your colors or layout [S-L19-061]. That is one video's opinion; rules.md §10 and L17 finding 4 agree that AI output converges on the same few looks.
9. **Say when feel can't be judged from code.** Name the check instead of guessing at a value (STD-process-review-taste-29).
10. **With nothing to learn from, stay restrained.** When there is no project, use neutral grays, one accent color and the system font stack [S-L19-031] (STD-visual-details-25).

## Conflicts and gaps found

- **The option gallery breaks two standards.** `option-gallery.html` and SKILL.md show "3 to 8 directions side by side". STD-process-review-taste-38 caps prototype variants at 5, and STD-process-review-taste-43 says to show options one at a time, full size. This policy uses 2 to 4 options flipped at full size. The gallery would need a one-at-a-time mode, with its grid kept as an index [inferred]. Both conflicts are recorded in `standards.json`.
- **Recommending first versus no favorite.** STD-process-review-taste-48 bans a favorite in prototype hand-offs, while rules.md §3.5 asks for a recommendation. This page separates the two by job [inferred]. The owner may want to confirm that split.
- **DC-L17-05 shows light and dark side by side.** Its default renders variants with light and dark next to each other, which sits badly with STD-process-review-taste-43. A light/dark toggle on the full-size sample would satisfy both [inferred].
- **Q-motion-01's stage text breaks motion standards.** Its default says "ease-in to exit", and its use/avoid line says to use expressive motion for page transitions and the primary action. Both conflict with STD-easing-duration-03, STD-when-to-animate-05 and STD-when-to-animate-09, which are already recorded in `standards.json`. The `impact.json` lines follow the standards: bold motion stays on rare moments, core navigation doesn't animate, and bounce stays for flicks, drags and rare playful moments.
- **Q-brand-04's `hero-moments` text has the same problem.** It names "opening a page or the primary action" as big moments, which are frequent surfaces under STD-when-to-animate-05 and -09. `standards.json` does not record this one yet [inferred]. Its `impact.json` lines use a first success instead.
- **Q-motion-01 `springs` ("Springs throughout") goes further than STD-springs-gestures-01 [inferred].** That standard gives springs to motion a finger drives and puts other motion on timing curves. `standards.json` records a conflict only for the Q-motion-01 default. The `impact.json` line says springs drive what a finger moves.
- **Q-motion-01 `none` must keep feedback.** STD-mobile-touch-05 keeps press feedback on every pressable element, and STD-accessibility-motion-02 records that the engine's `none` leaves no animation at all under reduced motion. The `impact.json` line keeps press feedback and fades that explain a change.
- **Two options rely on solid borders.** Q-depth-01 `borders` and Q-dir-01 `neo-brutalist` both do, and STD-visual-details-14 (a should) prefers a see-through shadow. Their `impact.json` lines say so, so the person sees the cost before choosing.
- **The generated copies are stale.** `tools/build_data.py` has the code to copy the lines, but `questions.json` and `stages/*.md` do not carry them yet. Run `python3 tools/build_data.py`.
- **Medium-weight questions have no Now or As it grows lines yet.** `impact.json` covers only the 30 high-weight questions. When a medium question is asked (designer voice, or "ask me everything"), the card has no scaling line.

## Where the parts live

- `skills/opendesigner/references/rules.md` §5 (answer statuses), §6 (sorting decisions and the Decide or ask table), §7 (vague or handed-over answers) and §8 (summaries).
- `skills/opendesigner/references/pacing.json`: `time_weight_rule`, `top_decisions`, `thresholds` and `assumed_owner_inputs_below_zoom2`.
- `synthesis/impact.json`: 30 questions and 132 options, each option with a Now line and an As it grows line, plus its evidence and the standards it respects. `tools/build_data.py` copies these into `stages/*.md` and `questions.json` (`now`, `grows`).
- `skills/opendesigner/assets/templates/option-gallery.html`: the `od-data` fields `recommended`, `safe` and `risks`, and the Copy my choice button, which produces `OD:` lines.

## Sources

Non-negotiable (house standards):
- [[sources/eks-skills-prototype-skill-emilkowalski-skills-skills-prototype-skill-md|emilkowalski/skills: skills/prototype/SKILL.md]] [S-L19-031]
- [[sources/eks-skills-prototype-picker-emilkowalski-skills-skills-prototype-picker-md|emilkowalski/skills: skills/prototype/PICKER.md]] [S-L19-030]
- [[sources/eks-skills-animate-skill-emilkowalski-skills-skills-animate-skill-md|emilkowalski/skills: skills/animate/SKILL.md]] [S-L19-018]
- [[sources/eks-skills-pick-ui-library-skill-emilkowalski-skills-skills-pick-ui-library-skill-md|emilkowalski/skills: skills/pick-ui-library/SKILL.md]] [S-L19-029]
- [[sources/eks-skills-improve-animations-skill-emilkowalski-skills-skills-improve-animations-skill-md|emilkowalski/skills: skills/improve-animations/SKILL.md]] [S-L19-027]
- [[sources/eks-readme-emilkowalski-skills-readme-md|emilkowalski/skills: README.md]] [S-L19-014]
- [[sources/ek-agents-with-taste-agents-with-taste|Agents with Taste]] [S-L19-004]
- [[sources/ek-developing-taste-developing-taste|Developing Taste]] [S-L19-008]
- [[sources/ek-train-your-judgement-train-your-judgement|Train Your Judgement]] [S-L19-011]
- [[sources/ek-you-dont-need-animations-you-don-t-need-animations|You Don't Need Animations]] [S-L19-012] (cited in `impact.json`)
- [[sources/ek-building-a-toast-component-building-a-toast-component|Building a toast component]] [S-L19-006]
- [[sources/ek-7-practical-animation-tips-7-practical-animation-tips|7 Practical Animation Tips]] [S-L19-003]
- [[sources/eks-skills-emil-design-eng-skill-emilkowalski-skills-skills-emil-design-eng-skill-md|emilkowalski/skills: skills/emil-design-eng/SKILL.md]] [S-L19-023] (cited in `impact.json`)

Reference (practitioner opinion):
- [[sources/7cTdCu8HMgM-the-definitive-process-to-present-uis-like-a-pro|The DEFINITIVE process to present UIs like a pro]] [S-L19-041]
- [[sources/HE4rLEQpiXY-how-to-think-like-a-genius-ui-ux-designer|How to think like a GENIUS UI/UX designer]] [S-L19-054]
- [[sources/ADaQuZS04Rc-stop-making-pretty-uis-think-like-a-product-designer|Stop Making Pretty UIs. Think Like a Product Designer]] [S-L19-044]
- [[sources/t7mpEDXzjCg-make-a-perfect-ux-case-study-in-8-steps|Make A Perfect UX Case Study In 8 Steps]] [S-L19-083]
- [[sources/9WVt1CelBfg-the-stupid-simple-way-to-learn-ui-ux-design-in-exactly-10-minutes|The stupid simple way to learn UI/UX design in exactly 10 minutes]] [S-L19-043]
- [[sources/xHD01_Onac0-vibe-coding-a-pro-ui-in-seconds-with-ai|Vibe Coding a Pro UI in SECONDS With AI]] [S-L19-086]
- [[sources/PDcQJOPby1k-5-saas-ui-ux-mistakes-that-scream-you-vibe-code|5 SaaS UI/UX mistakes that SCREAM you Vibe Code]] [S-L19-061]
- [[sources/lkKGQVHrXzE-designing-with-claude-code|Designing with Claude Code]] (Steve Schoger) [S-L19-103]

Related: [[synthesis/house-standards|House standards]].
