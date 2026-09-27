export const meta = {
  name: 'learn-synthesis',
  whenToUse: 'Reference sources were analysed (new or changed) and the topic pages, L19 Decision Cards, decide-or-ask page or impact notes need to catch up. `python3 tools/wiki.py next` says when, with the args.',
  description: 'Cross-source topic pages, L19 Decision Cards, the decide-or-ask process and impact notes, each verified, then research/L19 assembled',
  phases: [
    { title: 'Topics', detail: 'one agent per OpenDesigner area writes the wiki synthesis pages for its topics' },
    { title: 'Cards', detail: 'one agent per area writes Decision Cards mapped onto existing questions' },
    { title: 'Process', detail: 'decide-or-ask policy and impact/scale notes for high-impact decisions' },
    { title: 'Verify', detail: 'skeptics check cards, pages and process claims against analysis and raw text' },
    { title: 'Merge', detail: 'assemble research/L19-learning-wiki.md' },
  ],
}

// args: {root: "<repo path>", topics, cards, verify: area keys or "all" or [], process: bool, merge: bool}; all but root are optional.
// Example, to redo one area after new sources: {"root": "<repo path>", "topics": ["motion"], "cards": ["motion"], "verify": ["motion"], "process": false, "merge": true}
// python3 tools/wiki.py next prints these args for the areas whose sources are not used yet (it reads AREAS below).
const A = args || {}
if (typeof A.root !== 'string' || !A.root)
  throw new Error('learn-synthesis needs args {"root": "<repo path>", ...}: the checkout whose wiki it synthesises. python3 tools/wiki.py next prints the full args.')
const ROOT = A.root
const SYN = `${ROOT}/learn/wiki/synthesis`

// OpenDesigner areas; each area owns a block of card ids so parallel agents never collide. New cards take the next free id in the block.
const AREAS = [
  { key: 'color', start: 1, topics: ['Color', 'Dark mode and themes'], od: 'stages 07, 08, 09' },
  { key: 'typography', start: 21, topics: ['Typography', 'Content and microcopy'], od: 'stages 10, 11, 19' },
  { key: 'layout', start: 41, topics: ['Spacing and layout', 'Visual hierarchy', 'Cards and sections'], od: 'stages 06, 12, 13' },
  { key: 'shape-depth', start: 61, topics: ['Shape and corner radius', 'Depth, shadows and borders', 'Icons and imagery', 'Gradients, blend modes and texture effects'], od: 'stages 14, 15, 17, 18' },
  { key: 'motion', start: 81, topics: ['Motion principles', 'Easing and timing', 'Spring animation', 'Animation performance', 'Gestures and drag', 'Micro-interactions', 'Reduced motion'], od: 'stage 16' },
  { key: 'components', start: 101, topics: ['Toasts and notifications', 'Drawers and sheets', 'Buttons and actions', 'Forms and inputs', 'Navigation and sidebars', 'Modals and popovers', 'UI libraries'], od: 'stages 20, 21, 22' },
  { key: 'patterns', start: 121, topics: ['Dashboards and data display', 'Landing pages', 'Onboarding', 'Paywalls and pricing pages', 'Retention and gamification', 'SaaS product UI', 'Feedback, empty and loading states', 'A/B testing and conversion', 'Dark patterns and user-hostile design'], od: 'stage 23' },
  { key: 'platforms', start: 141, topics: ['Mobile app patterns', 'Desktop and macOS apps', 'Accessibility', 'Native implementation (Swift and SwiftUI)'], od: 'stages 02, 04' },
  { key: 'process', start: 161, topics: ['Design taste and judgement', 'Design process', 'Presenting designs', 'Portfolio and case studies', 'AI-assisted design', 'Figma and design tools', 'Prototyping', 'Freelancing and pricing work', 'Design resources', 'Launch and marketing'], od: 'stages 00, 03, 25, 26, 27' },
  { key: 'tokens', start: 181, topics: ['Design systems and tokens', 'Web implementation (CSS and React)'], od: 'stages 05, 24' },
]
const pick = (v) => v === undefined || v === 'all' ? AREAS.map(a => a.key) : v
const want = { topics: pick(A.topics), cards: pick(A.cards), verify: pick(A.verify) }

const COMMON = `Scratch work: put any helper script or temp file in a directory of your own (mktemp -d), and never run a script you did not write in this task (other agents share the scratch space).
Repo: ${ROOT}. Knowledge base (learn/README.md explains it):
- ${ROOT}/learn/analysis/*.json: one verified analysis per source (fields: summary, key_ideas, topics, rules, decisions, process, examples, numbers, caveats, authority). Find a topic's sources with: grep -l '"name": "<Topic>"' ${ROOT}/learn/analysis/*.json
- ${ROOT}/learn/raw/<folder>/<id>.txt: the full source text (git-ignored; read it to confirm anything you rely on).
- ${ROOT}/learn/sids.json: source id -> S-L19-nnn citation id. Cite sources ONLY with these S-ids, e.g. [S-L19-012].
- ${ROOT}/synthesis/standards.json: the house standards (non-negotiable, locked). Never propose anything that contradicts a standard; reference standards by id (STD-...). The readable version is skills/opendesigner/references/standards/<theme>.md.
- ${ROOT}/learn/wiki/sources/*.md: the wiki page per source (link as [[sources/<file name without .md>|<title>]]).
- OpenDesigner's current questions and research: ${ROOT}/skills/opendesigner/references/questions.json (Q-ids, options, defaults), ${ROOT}/skills/opendesigner/references/stages/*.md, ${ROOT}/research/L*.md (existing Decision Cards, DC-Lxx-nn), ${ROOT}/skills/opendesigner/references/pacing.json.
Authority: non-negotiable (Emil Kowalski sources) = house standards; good-to-have (Vaul) = recommended default; reference (Kole Jain, Mobbin, Steve Schoger videos) = trusted practitioner opinion: use it, but a number or "always/never" claim from a single video is opinion unless another source or existing research agrees; say so.
Faithfulness: only what sources say; mark your own connections " [inferred]". Quotes: none needed; if you quote, 15 words max.`

function topicPrompt(a) {
  return `${COMMON}

Write the wiki synthesis pages for these topics: ${a.topics.join('; ')}.
For each topic with at least one source, write ${SYN}/<slug>.md where slug = lowercase, non-alphanumerics to "-" (e.g. "Depth, shadows and borders" -> depth-shadows-and-borders). If the page exists, update it in place: keep what is still true, add what new sources teach. Format (OpenWiki page):
---
type: synthesis
title: <Topic>
created: <keep the existing date, or today>
updated: <today>
sources:
  - <analysis id>
tags:
  - od-area-${a.key}
---
# <Topic>
## In short            (3-5 plain sentences a student could follow)
## House standards     (STD ids and one-line rules from standards.json that apply; "None" if none)
## What the sources teach   (grouped by idea, not by source; each point cites [S-L19-nnn] and links the source page)
## Where they agree and disagree   (between sources, and with OpenDesigner's existing research: cite DC-Lxx-nn ids you actually opened)
## Decisions this informs   (Q-ids from questions.json with a line on how)
## Visual examples worth showing   (concrete examples from the sources that would make a good visual sample, with source)
## Open questions
Also link the topic page: add "- See also: [[synthesis/<slug>|<Topic> synthesis]]" at the end of ${ROOT}/learn/wiki/topics/<slug>.md if that file exists and lacks it.
Return the list of pages written with their source counts.`
}

function cardsPrompt(a) {
  return `${COMMON}

You write Decision Cards for lane L19 (the learning wiki), area "${a.key}" (OpenDesigner ${a.od}; topics: ${a.topics.join('; ')}).
Goal: make OpenDesigner's interview better at this area using what the trusted sources teach: better options and visual effects, better defaults and heuristics, missing questions, real examples to use as visual samples, and a clear note on what each choice changes now and as the product grows.

Read every analysis for your topics (and their raw text where you rely on a detail), the matching stage files, the questions for this area in questions.json, and the existing cards they cite.

The cards live in ${SYN}/_cards/${a.key}.md, numbered in this area's block from DC-L19-${String(a.start).padStart(2, '0')} to DC-L19-${a.start + 18} (at most 19 cards). If the file exists, keep its cards and ids, update the ones new sources change, and add new cards at the next free id; if a card no longer holds, mark it "**Withdrawn:** <why>" instead of deleting it, so its id is never reused. Keep the front matter at the top of the file (a new file starts with one: ---, type: synthesis, title: "<the file's # heading>", tags: decision-cards and the area key, ---), which OpenWiki's lint needs. Use exactly this template (from _coordination/SCHEMA.md) plus the three extra fields at the end:
### DC-L19-<nn>: <Decision name>
- **Block path:** e.g. Foundations > Color > Neutral ramp
- **Questions the designer answers:** 1-4 plain-language questions
- **Options:** each option, and which sources or famous systems use it (with real values where the sources give them)
- **Visual effect:** what each option makes the product look/feel like
- **Depends on (upstream):** decisions that come first
- **Affects (downstream):** tokens, components and patterns that change
- **Token encoding:** DTCG $type and example token names, or "none (process or content decision)"
- **Platform notes:** web / iOS / Android differences, if the sources give any
- **Accessibility constraints:** the floors that bound the options
- **Default + heuristic:** a sensible default and a rule of thumb
- **Evidence:** [S-L19-nnn] ids (and DC ids of existing cards you compared against)
- **Maps to:** the Q-id(s) this improves, and the exact change: "new option X", "new default Y because...", "new heuristic", "new question: ...", "visual sample: ...", or "confirms current default"
- **Impact now / as it grows:** for each option, one line on what it changes today and one on what it means as the product, team or content grows
- **Standards:** STD ids that constrain it, or "none"

Rules: one decision per card; no card that merely restates an existing card with nothing new (say "confirms" inside another card instead); flag any disagreement with an existing card explicitly in Options or Default ("differs from DC-Lxx-nn: ...") rather than silently overriding it; never contradict a house standard.
Return: card ids and titles, and the list of proposed questionnaire changes (Q-id, change, evidence).`
}

const PROCESS_PROMPT = `${COMMON}

OpenDesigner must have a clear process for, at every decision, EITHER choosing for the person on its own OR asking them to pick among a few options shown as visual samples, so they understand how the choice affects them and their process, and how it scales later.

1. Read ${ROOT}/skills/opendesigner/references/rules.md (sections 3-8, including "Decide or ask"), zoom.md, pacing.json (the high-impact list), SKILL.md ("Show, then ask: the visual ladder"), and the templates' od-data in ${ROOT}/skills/opendesigner/assets/templates/option-gallery.html.
2. Read what the sources say about choosing, comparing and presenting options: Emil Kowalski's prototype skill (eks-skills-prototype-*), developing taste / train your judgement (ek-*), agents with taste, Kole Jain on presenting designs and thinking like a product designer, Mobbin's data-driven videos (if analysed), and Steve Schoger's "Designing with Claude Code" (lkKGQVHrXzE).
3. Write or update ${SYN}/decide-or-ask.md (OpenWiki synthesis page: type synthesis, title "Decide or ask", tags od-area-process) with: the policy as a table (what OpenDesigner decides itself and what it asks with visual samples, grounded in rules.md/pacing.json and cited sources); how to ask (2-4 options, recommended first with its reason, each a visual sample of the SAME real screen with "Now:" and "As it grows:" lines, plus the free answer); how to decide silently without surprising people. Cite sources for every practice.
4. Write or update ${ROOT}/synthesis/impact.json: for every question id pacing.json marks high-impact (and Q-motion-01), and each of its options in questions.json:
   {"$comment": "...", "questions": {"Q-xxx-nn": {"options": {"<option id>": {"now": "one plain sentence", "as_it_grows": "one plain sentence"}}, "evidence": ["S-L19-nnn" or "DC-Lxx-nn"]}}}
   Ground each line in the question's option text, its cards, and the sources; end reasoning lines with " [inferred]". Plain words, 25 words max per line.
Return: the policy table in brief and the number of questions/options covered in impact.json.`

function verifyPrompt(a) {
  return `${COMMON}

Adversarially verify the Decision Cards in ${SYN}/_cards/${a.key}.md and the topic pages for: ${a.topics.join('; ')} (in ${SYN}/).
For every card: open each cited S-L19 source (map S-id -> source id with learn/sids.json, then read learn/analysis/<id>.json and, for anything specific, learn/raw/.../<id>.txt). Try to refute: is each option, value, visual effect and default supported? Is a single-video opinion presented as fact? Does the "Maps to" Q-id exist in questions.json and is the proposed change sensible against the question's current options/default? Does any card contradict a house standard (synthesis/standards.json) or silently override an existing card? Are DC-Lxx-nn ids real (grep research/ and benchmarks/)?
Fix or withdraw what fails, in place (a withdrawn card keeps its id and says "**Withdrawn:** <why>"). For topic pages, check the same for their claims and that every [[sources/...]] link target exists in learn/wiki/sources/.
Return counts: cards checked/fixed/withdrawn, pages checked/fixed.`
}

const VERDICT = { type: 'object', properties: {
  cards_checked: { type: 'integer' }, cards_fixed: { type: 'integer' }, cards_deleted: { type: 'integer' },
  pages_checked: { type: 'integer' }, pages_fixed: { type: 'integer' }, notes: { type: 'string' } },
  required: ['cards_checked', 'cards_fixed', 'cards_deleted', 'pages_checked', 'pages_fixed', 'notes'] }

const todo = AREAS.filter(a => want.topics.includes(a.key) || want.cards.includes(a.key) || want.verify.includes(a.key))
log(`areas: ${todo.map(a => a.key).join(', ') || 'none'}; process: ${A.process !== false}; merge: ${A.merge !== false}`)

const areaResults = pipeline(
  todo,
  a => want.topics.includes(a.key) ? agent(topicPrompt(a), { label: `topics:${a.key}`, phase: 'Topics' }) : 'skipped',
  (_t, a) => want.cards.includes(a.key) ? agent(cardsPrompt(a), { label: `cards:${a.key}`, phase: 'Cards' }) : 'skipped',
  (_c, a) => want.verify.includes(a.key)
    ? agent(verifyPrompt(a), { label: `verify:${a.key}`, phase: 'Verify', schema: VERDICT }).then(v => ({ key: a.key, verify: v }))
    : { key: a.key, verify: 'skipped' },
)
const processResult = A.process === false ? Promise.resolve('skipped') : agent(PROCESS_PROMPT, { label: 'decide-or-ask', phase: 'Process' })
  .then(p => agent(`${COMMON}

Adversarially verify ${SYN}/decide-or-ask.md and ${ROOT}/synthesis/impact.json. Check every cited S-L19 id supports the practice it is attached to; every question and option id in impact.json exists in skills/opendesigner/references/questions.json; each now/as_it_grows line is consistent with the option's own text and not contradicted by a house standard; reasoning lines carry [inferred]. Validate impact.json parses. Fix in place. Return a short list of fixes.`, { label: 'verify:decide-or-ask', phase: 'Verify' }).then(v => ({ process: p, verify: v })))

const [areas, proc] = await Promise.all([areaResults, processResult])

let merged = 'skipped'
if (A.merge !== false) {
  phase('Merge')
  merged = await agent(`${COMMON}

Assemble ${ROOT}/research/L19-learning-wiki.md from ${SYN}/_cards/*.md (areas in id order, leaving out each file's front matter; the _cards files stay the source you edit, this file is the repo's research copy). Structure:
# L19: Learning wiki (trusted sources)
<lane overview: sources and their authority (learn/sources.json), how they were processed (learn/README.md), counts, and how this lane feeds OpenDesigner: synthesis/standards.json (house standards), these cards, synthesis/impact.json, learn/wiki/>
## Part A: Decision Cards (every card, text unchanged, withdrawn ones included with their note)
## Part B: Proposed questionnaire changes (table: Q-id | change | evidence | card) from every card's "Maps to" that proposes a change (not "confirms")
## Part C: Conflicts with existing research (table: existing card or default | what the sources say | resolution proposed)
## Open questions / gaps
## Confidence (what is confirmed vs inferred; which claims rest on a single video)
Then run: python3 ${ROOT}/tools/jev_nav.py check 2>&1 | tail -3 and fix any dangling S-id or DC id in the L19 file (an S-id must be in traces/L19-trace.md; a DC id must exist). Then python3 ${ROOT}/tools/jev_nav.py export and python3 ${ROOT}/tools/build_data.py.
Return: number of cards, number of proposed changes, number of conflicts.`, { label: 'merge-cards', phase: 'Merge' })
}

return { areas, proc, merged }
