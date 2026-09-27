export const meta = {
  name: 'learn-personas',
  whenToUse: 'After a change to house standards, project-standard commands, the skills text or the learning pipeline: end-to-end acceptance tests played by five personas, plus a Jev retrieval check. Args: {"root": "<repo path>"}.',
  description: 'End-to-end tests of house standards, project sources and the learning pipeline, played by five personas, plus Jev retrieval checks',
  phases: [
    { title: 'Personas', detail: 'student, designer, engineer, maintainer, returning project' },
    { title: 'Retrieval', detail: 'Jev find: do realistic questions reach the new knowledge?' },
    { title: 'Triage', detail: 'dedupe findings and rank what to fix' },
  ],
}

// args: {root: "<repo path>", only: ["student", ...] (optional)}
const A = args || {}
if (typeof A.root !== 'string' || !A.root)
  throw new Error('learn-personas needs args {"root": "<repo path>"} (optionally "only": [...]): the checkout to test.')
const ROOT = A.root
const SKILL = `${ROOT}/skills/opendesigner`

const COMMON = `Scratch work: put any helper script or temp file in a directory of your own (mktemp -d), and never run a script you did not write in this task (other agents share the scratch space).
You are testing OpenDesigner (repo ${ROOT}) as a real user would meet it. Read ${SKILL}/SKILL.md, ${SKILL}/references/rules.md (sections 5, 6 "Decide or ask", 12), ${SKILL}/references/guardrails.md (4b), ${SKILL}/references/standards.md, ${ROOT}/skills/opendesigner-extend/SKILL.md and ${ROOT}/docs/KNOWLEDGE.md. Play the AGENT that follows those instructions, and imagine the person's replies as described. Run every engine command for real: python3 ${SKILL}/scripts/engine.py ... from inside your own project folder (make it with mktemp -d; never write inside the repo). Do NOT edit any repo file. Delete your temp folder when you finish.
Record, as you go, every friction point: an instruction that is missing, wrong, ambiguous or contradicts another; an engine command that fails, prints a traceback, or prints something a person would not understand; a standard that makes a bad result; anything the docs promise that does not happen.
Return a numbered findings list. Each: severity (high = wrong result or broken promise; medium = confusing or slow; low = polish), where (file:line or command), what happened (paste the exact command and the relevant output), and the fix you suggest. Then one line: what worked well.`

const PERSONAS = [
  { key: 'student', prompt: `Persona: a school student making a design system for a club website, plain voice, in a hurry ("just pick"). Run the zoom-0 sketch with --delegated as SKILL.md says. Check: were house standards applied and locked (engine.py standards)? Would the agent ask any question a standard already settles (walk the motion stage file and say which questions would still be asked and whether any option contradicts a standard)? Write the first-result message exactly as SKILL.md and rules.md say (standards mentioned once, plainly). Generate DESIGN.md: is the Standards section short and understandable to a 14-year-old, and does opendesigner/standards.md hold the full list? Then write a small styles.css with 3 violations the standards catch (e.g. transition: all, an enter animation from scale(0), ease-in on an entrance) and 2 correct rules, run engine.py review, and report precision/recall of the standards checks.` },
  { key: 'designer', prompt: `Persona: a product designer with an existing brand motion language who says: "Our exits use ease-in, that's our brand, and our dialogs animate over 450ms." Start a project (init + sketch with a feel of your choice). Follow the extend skill and guardrails 4b: the agent must restate the standard once, then override ONLY after the person's explicit words. Run the overrides, set the values, build, validate: do tokens, DESIGN.md (override reason shown?), decisions.md (supersede, set_by) and review all behave? Then the designer changes their mind on one: restore it. Also try the wrong path an agent might take: engine.py set on a standard-locked path without override; is the message clear?` },
  { key: 'engineer', prompt: `Persona: a front-end engineer whose company has UI rules. In your temp folder create company-ui-rules.md with 6 rules of your own making (for example: toasts auto-dismiss after 4000ms; never animate width or height; primary buttons use radius 6px; use Sonner for toasts; focus ring 2px; exits use ease-in, which conflicts with a house standard). The engineer says: "These are non-negotiable for our app." Follow rules.md section 12 end to end with the local file as the source (consent to read: assume yes). Record each rule with engine.py standard add (with --path/--value where a token fits, and --review-pattern where code can be checked). Check the conflict handling with the house standard (project standard should win, said once, recorded). Write a small src/Button.tsx and toast.ts that break 3 of the rules and run review. Then remove one project standard. Report whether the whole flow is possible with the commands that exist.` },
  { key: 'maintainer', prompt: `Persona: an OpenDesigner maintainer adding a new house source, following ${ROOT}/learn/README.md, ${ROOT}/learn/IMPROVING.md and ${ROOT}/_coordination/lanes/L19-learning-wiki.md. Work in a COPY of the committed repo: mkdir -p <your temp dir>/repo && git -C ${ROOT} archive HEAD | tar -x -C <your temp dir>/repo (about 40 MB; never copy .venv-wiki or learn/raw), and run everything there. Steps: python3 tools/wiki.py next (is every step's advice correct and actionable?); python3 tools/wiki.py map --check; python3 tools/wiki.py add https://sonner.emilkowal.ski/getting-started --authority reference (already listed: what happens?); python3 tools/wiki.py add https://example.com --authority reference --name "Example" and fetch it with ${ROOT}/.venv-wiki/bin/python tools/wiki.py fetch --only "Example". Write a small valid analysis JSON for it by hand, run check, ingest (with ${ROOT}/.venv-wiki/bin/python), trace, map and next again. Then simulate a standards change: edit one standard's rule in synthesis/standards.json and run python3 tools/wiki.py standards (must fail), then standards --bump "test", build_data.py, and check that skills/opendesigner/references/standards/<theme>.md changed. Run python3 tools/test_wiki.py and ${ROOT}/.venv-wiki/bin/python tools/wiki.py upstream (read-only).` },
  { key: 'returning', prompt: `Persona: a team that made their system with an OLDER house standards version and comes back months later. Build a fixture in your temp dir: copy ${SKILL}/references/standards.json to std-old.json and edit it into an older version: version one lower, remove two standards, change one standard's locked value. Run the project with OD_STANDARDS_FILE=<that file>: init, sketch, override one standard with a reason. Then point OD_STANDARDS_FILE at the real ${SKILL}/references/standards.json (newer) and follow the extend skill start-up routine: validate should tell them; standards --update should apply new and changed ones and keep the override. Check decisions.md, DESIGN.md, opendesigner/standards.md and tokens after. Also check that a project whose state.json has no "standards" key (delete it) still works with every command.` },
]

const RETRIEVAL = `Scratch work: put any temp file in a directory of your own (mktemp -d) and delete it when you finish.
From ${ROOT}, run python3 tools/jev_nav.py find "<question>" --top 8 for each question below (JEV_API_KEY is in .env; the tool reads it). For each, record whether a relevant house standard (STD-...) or L19 Decision Card (DC-L19-...) appears in the top 8, and whether an older card now contradicts it. Questions:
1. which easing should a modal use when it closes
2. how long should a dropdown animation take
3. should a toast pause when I hover it
4. how should a bottom sheet feel when dragged on mobile
5. what should happen when a user presses a button
6. how do I make a dashboard easy to scan
7. what makes a paywall convert
8. how should I present a design to a client
9. what color mistakes make a UI look amateur
10. how should onboarding work in a mobile app
11. do I need an animation for a keyboard shortcut action
12. how can I design with Claude Code
Also run python3 tools/jev_nav.py check and report dangling references. Return a table (question, best STD/DC-L19 hit and rank or "none", any contradiction) and suggestions to improve retrieval. Do not edit files.`

const people = A.only ? PERSONAS.filter(p => A.only.includes(p.key)) : PERSONAS
// One disk check for the whole run: five personas plus retrieval need about 1 GB of scratch and transcript space.
const disk = await agent(`Run: df -m "$TMPDIR" | tail -1 | awk '{print $4}' and return the number of free megabytes. Do nothing else.`,
  { label: 'disk', phase: 'Personas', effort: 'low', schema: { type: 'object', properties: { free_mb: { type: 'integer' } }, required: ['free_mb'] } })
if (!disk || disk.free_mb < 1000) {
  return { stopped: `Only ${disk ? disk.free_mb : '?'} MB free on the temp volume; the persona tests need about 1 GB. Free space and run again (args {"only": [...]} runs fewer personas).` }
}
phase('Personas')
const personas = await parallel(people.map(p => () => agent(`${COMMON}\n\n${p.prompt}`, { label: `persona:${p.key}`, phase: 'Personas' })
  .then(r => ({ key: p.key, findings: r }))))
phase('Retrieval')
const retrieval = await agent(RETRIEVAL, { label: 'retrieval', phase: 'Retrieval' })

phase('Triage')
const triage = await agent(`You triage end-to-end test findings for OpenDesigner (repo ${ROOT}). Findings from the persona tests and a retrieval test:

${personas.filter(Boolean).map(p => `=== ${p.key} ===\n${p.findings}`).join('\n\n')}

=== retrieval ===
${retrieval}

Deduplicate. For each distinct issue: verify it is real by reading the cited file or re-running the command; drop the ones that are not. Rank by severity. Return a list: id, severity, component (engine | skill text | tools/wiki.py | build_data | standards content | docs | retrieval), what, evidence, fix (specific: file and change). Put fixes that need no product decision first; list any that need the owner's decision separately.`, { label: 'triage', phase: 'Triage' })

return { personas, retrieval, triage }
