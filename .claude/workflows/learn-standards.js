export const meta = {
  name: 'learn-standards',
  whenToUse: 'Non-negotiable or good-to-have sources were added or changed (`python3 tools/wiki.py next` says "standards"). Rebuilds synthesis/standards.json by theme; ids stay stable.',
  description: 'Turn the non-negotiable sources into verified, deduplicated house standards (draft by theme, verify, merge, completeness critic)',
  phases: [
    { title: 'Draft', detail: 'one agent per theme drafts standards from every non-negotiable analysis' },
    { title: 'Verify', detail: 'independent skeptics check each theme against the raw sources' },
    { title: 'Merge', detail: 'dedupe across themes into synthesis/standards.json, keeping existing ids' },
    { title: 'Critic', detail: 'completeness critic: which source rules never became a standard' },
  ],
}

// args (optional): {root, themes: ["easing-duration", ...] to redo only some themes (default all)}
// Afterwards, by hand: python3 tools/wiki.py standards --bump "<what changed>", cite-check --standards, build_data.py.
const A = args || {}
const ROOT = A.root || '/Users/Kunal/Desktop/Design-System'
const OUT = `${ROOT}/learn/wiki/synthesis/_standards`

const THEMES = [
  { key: 'easing-duration', scope: 'Easing curves (exact cubic-bezier values), durations and duration limits, when to use ease-out / ease-in-out / linear, asymmetric enter vs exit timing, speed of UI vs marketing motion.' },
  { key: 'when-to-animate', scope: 'Whether to animate at all: frequency of use, keyboard-initiated actions, purpose of animation, "you do not need animations", friction as a feature, delight budget, first-time vs repeated interactions.' },
  { key: 'enter-exit-origin', scope: 'How things enter and leave: starting scale (never from 0), opacity, blur, transform-origin from the trigger, popovers/dropdowns/tooltips/modals, stagger, height/layout animations, exits.' },
  { key: 'springs-gestures', scope: 'Springs (stiffness, damping, bounce, duration), interruptibility, velocity, drag, momentum, rubber-banding, swipe-to-dismiss thresholds, fluid interfaces, Apple design principles for motion and materials.' },
  { key: 'performance-properties', scope: 'Which properties to animate (transform, opacity, clip-path, filter), CSS vs JS vs WAAPI, will-change, layout thrash, hardware acceleration, Framer Motion / Motion specifics, the performance cheatsheet.' },
  { key: 'components-toasts-drawers', scope: 'Component behaviour: toasts (Sonner: stacking, swipe, pause on hover, positions, promise, rich colors, duration), drawers and sheets (Vaul: snap points, scaling background, drag, inputs), buttons (press scale), tooltips (delay, instant after first), menus, dialogs.' },
  { key: 'visual-details', scope: 'Non-motion design advice: shadows vs borders, colors, typography, spacing, radii, focus rings, hover states, polish details, "agents with taste" mistakes, UI library picks (pick-ui-library) and what not to hand-roll.' },
  { key: 'mobile-touch', scope: 'Mobile web and touch: hover on touch devices, tap highlight, 100vh / dynamic viewport, input zoom (16px), safe areas, fast taps, overscroll, native-feeling web apps; React Native / Expo motion (animate-expo: Reanimated, UI thread, haptics, screen transitions).' },
  { key: 'accessibility-motion', scope: 'prefers-reduced-motion handling, what to keep vs remove, vestibular safety, focus, keyboard users, accessibility in toasts/drawers.' },
  { key: 'process-review-taste', scope: 'Process and craft: developing taste, training judgement, reviewing animations (review/improve/find-opportunities checklists), prototyping several versions with a switcher, building a course/learning, slow-motion review, animation vocabulary for prompting.' },
  { key: 'swift', scope: 'Writing Swift (write-swift skill): value types, concurrency, generics, performance, testing. These apply when OpenDesigner exports to Swift/SwiftUI.' },
]
const todo = A.themes ? THEMES.filter(t => A.themes.includes(t.key)) : THEMES

const STD_SCHEMA_DOC = `Each standard:
{
  "id": "STD-<theme-key>-<nn>",            // nn = 01, 02, ... within the theme; an existing standard keeps its id, a new one takes the next free number
  "theme": "<theme key>",
  "area": "motion|components|color|typography|layout|shape|elevation|accessibility|platforms|process|tokens|tooling",
  "title": "4-8 words",
  "rule": "one imperative, testable sentence",
  "why": "the source's reason, one or two sentences",
  "strength": "must|should",               // only source rules with strength must/should become standards; 'consider' stays in the wiki
  "values": {"name": "exact value"},        // {} if none
  "applies_to": ["web", "ios", "android", "react", "css", "react-native", "swift", "all"],
  "sources": [{"id": "<analysis id>", "evidence": "a short phrase that appears verbatim in the raw source"}],
  "engine": null | {"path": "<DTCG token path>", "value": <value>, "type": "<DTCG $type>", "note": "..."} | [several of those],
  "review": null | {"pattern": "a Python regex that finds a violation on one line of CSS/JS/TSX", "message": "short fix hint"},
  "design_md": true | false,                // true if an implementing agent must follow it
  "conflicts": ["an existing OpenDesigner default that disagrees, with the file and value"]
}`

const COMMON = `Scratch work: put any helper script or temp file in a directory of your own (mktemp -d), and never run a script you did not write in this task (other agents share the scratch space).
Repo ${ROOT}. House standards come from sources the owner marked NON-NEGOTIABLE (learn/sources.json: Emil Kowalski's articles, the emilkowalski/skills repo, the Sonner docs, animations.dev) and, at strength "should" at most, the GOOD-TO-HAVE Vaul docs (unmaintained per its README). The rules for what a standard is and how projects use it: docs/KNOWLEDGE.md.
Inputs: ${ROOT}/learn/analysis/*.json with "authority" non-negotiable or good-to-have (read "rules", "numbers", "decisions"); the raw text in ${ROOT}/learn/raw/{emil-kowalski,emil-skills,sonner,animations-dev,vaul}/ for exact wording and values; the current ${ROOT}/synthesis/standards.json (keep existing ids and wording that is still right).
OpenDesigner's defaults, for conflicts and engine mappings: ${ROOT}/synthesis/levers.json, skills/opendesigner/references/stages/*.md, and the generated tokens (in a temp dir: python3 ${ROOT}/skills/opendesigner/scripts/engine.py init --name T && python3 ${ROOT}/skills/opendesigner/scripts/engine.py generate; read opendesigner/tokens/*.json). Test an engine mapping with engine.py set <path> '<json value>' --why test in that temp dir.`

function draftPrompt(t) {
  return `${COMMON}

Your theme: "${t.key}": ${t.scope}
Write ${OUT}/${t.key}.json: {"theme": "${t.key}", "standards": [...]} using this schema:
${STD_SCHEMA_DOC}
- One standard per distinct rule; merge duplicates across sources (list every source). Only what the sources say; values exact; mark your own inference " [inferred]".
- Be complete for the theme: every must/should rule the sources state is covered.
- "engine" only for a value the standard fixes (existing tokens such as motion.easing.*, motion.duration.*, or a new reusable token with its type). "review" only for mechanically detectable violations, precise enough to avoid false positives.
Return: the number of standards, new ones, changed ones, and the three most important conflicts with current OpenDesigner defaults.`
}

function verifyPrompt(t) {
  return `${COMMON}

Adversarially verify the drafted standards in ${OUT}/${t.key}.json. For EACH standard open its cited raw sources and try to refute it: does the source state this rule at this strength ("must" only if stated as a rule or breaking it is called a mistake)? Is every value exact? Is "why" the source's reason? Is each "conflicts" entry true (open the file)? Is each "review" regex correct Python, one-line, and precise (test it on violating and correct snippets)? Does the evidence appear verbatim in the raw text? Fix, weaken or delete what fails; add must/should rules for this theme the file misses. Write the file back in place.`
}

const VERDICT = { type: 'object', properties: {
  checked: { type: 'integer' }, fixed: { type: 'integer' }, deleted: { type: 'integer' }, added: { type: 'integer' }, notes: { type: 'string' } },
  required: ['checked', 'fixed', 'deleted', 'added', 'notes'] }

const drafts = await pipeline(
  todo,
  t => agent(draftPrompt(t), { label: `draft:${t.key}`, phase: 'Draft' }),
  (_d, t) => agent(verifyPrompt(t), { label: `verify:${t.key}`, phase: 'Verify', schema: VERDICT }).then(v => ({ key: t.key, verify: v })),
)

phase('Merge')
const merged = await agent(`${COMMON}

Merge the verified theme files ${OUT}/{${todo.map(t => t.key).join(',')}}.json into ${ROOT}/synthesis/standards.json.
- Themes you were given replace that theme's standards in the file; other themes stay untouched.
- Keep ids stable: an existing standard keeps its id; a new one takes the next free number in its theme; never reuse a removed id.
- Deduplicate across themes (the same rule in two themes becomes one standard; merge sources; the stronger strength wins).
- Keep "version", "history", "retired", "since" and "changed" as they are: \`python3 tools/wiki.py standards --bump\` stamps new and changed standards and retires removed ones. New standards get "since" and "changed" equal to the current version for now.
- Keep "themes" (key, title, one-sentence summary) matching every standard's theme.
- Validate: ids unique; every sources[].id exists as learn/analysis/<id>.json; every review.pattern compiles.
Also refresh ${ROOT}/learn/wiki/synthesis/house-standards.md (OpenWiki synthesis page listing every standard by theme in plain words).
Return: counts per theme (before -> after), new ids, removed ids, and conflicts with current OpenDesigner defaults.`, { label: 'merge', phase: 'Merge' })

phase('Critic')
const critic = await agent(`${COMMON}

Completeness critic. Read ${ROOT}/synthesis/standards.json, then every non-negotiable and good-to-have analysis in ${ROOT}/learn/analysis/ and every rule with strength must or should. Decide whether a standard covers each. For each uncovered rule that is real (check the raw text) and is a rule for a person's project (not a skill's own start-up behaviour or repo upkeep), add a standard in the right theme with the next free id. No duplicates. Return: rules checked, uncovered found, standards added.`, { label: 'critic', phase: 'Critic' })

return { drafts, merged, critic }
