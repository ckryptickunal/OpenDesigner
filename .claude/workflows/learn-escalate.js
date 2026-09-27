export const meta = {
  name: 'learn-escalate',
  whenToUse: 'After `python3 tools/wiki.py cite-check` (and `cite-check --standards`) leaves items flagged: a reasoning agent reads each against the raw source and confirms, fixes or removes it.',
  description: 'Review every rule and standard Jev flagged against the raw source, fix or confirm it, then re-check',
  phases: [
    { title: 'Collect', detail: 'read the flagged list from tools/wiki.py flagged --json' },
    { title: 'Review', detail: 'one agent per group of flagged items reads the raw text and decides' },
    { title: 'Recheck', detail: 'Jev re-checks what changed' },
  ],
}

// args (optional): {root}
const ROOT = (args && args.root) || '/Users/Kunal/Desktop/Design-System'

const RULES = `Scratch work: put any helper script or temp file in a directory of your own (mktemp -d), and never run a script you did not write in this task (other agents share the scratch space).
You are the escalation step of OpenDesigner's citation check (repo ${ROOT}; see learn/README.md, "cite-check"). TypeSafe's Jev judged each item below against the passage its evidence points to, and flagged it: its verdict was not "supports", or its confidence was under 0.8. A flag is NOT proof of an error: the passage finder may have looked in the wrong place. Decide by reading the raw source yourself (learn/raw/<folder>/<id>.txt; ids starting ek- are in emil-kowalski/, eks- in emil-skills/, sonner- in sonner/, adev- in animations-dev/, vaul- in vaul/, 11-character YouTube ids in kole-jain/, mobbin/ or videos/).
For each item decide one of:
- confirmed: the source supports it as written. If its "evidence" string does not appear verbatim in the raw text, replace it with a short verbatim phrase that does, so the next check finds the right passage.
- fixed: the source supports a different wording, value or strength. Edit it to match the source exactly.
- removed: the source does not support it. Delete it. For a standard, delete the entry from "standards" (the maintainer's version bump moves it to "retired").
Edit only the files named in your items. Keep each file's schema. Afterwards run python3 ${ROOT}/tools/wiki.py check (analysis files) and python3 ${ROOT}/tools/wiki.py standards (standards file; a changed content hash is expected until the bump) and fix any other error you caused.
Return every item with its decision.`

const VERDICT = { type: 'object', properties: { items: { type: 'array', items: { type: 'object', properties: {
  item: { type: 'string' }, decision: { type: 'string', enum: ['confirmed', 'fixed', 'removed'] }, note: { type: 'string' } },
  required: ['item', 'decision', 'note'] } } }, required: ['items'] }
const FLAGGED = { type: 'object', properties: {
  rules: { type: 'array', items: { type: 'object', properties: { source: { type: 'string' }, n: { type: 'integer' }, rule: { type: 'string' },
    verdict: { type: 'string' }, confidence: { type: 'number' } }, required: ['source', 'n', 'rule', 'verdict', 'confidence'] } },
  standards: { type: 'array', items: { type: 'object', properties: { std: { type: 'string' }, source: { type: 'string' },
    verdict: { type: 'string' }, confidence: { type: 'number' } }, required: ['std', 'source', 'verdict', 'confidence'] } } },
  required: ['rules', 'standards'] }

phase('Collect')
const flagged = await agent(`Run: cd ${ROOT} && python3 tools/wiki.py flagged --json. Return its JSON exactly (rules and standards arrays). Do nothing else.`,
  { label: 'collect', phase: 'Collect', schema: FLAGGED, effort: 'low' })

const byFile = {}
for (const r of flagged.rules) (byFile[r.source] = byFile[r.source] || []).push(r)
const ruleGroups = []
let cur = []
for (const [src, items] of Object.entries(byFile)) {
  cur.push({ src, items })
  if (cur.reduce((n, g) => n + g.items.length, 0) >= 12) { ruleGroups.push(cur); cur = [] }
}
if (cur.length) ruleGroups.push(cur)
const stdGroups = []
for (let i = 0; i < flagged.standards.length; i += 8) stdGroups.push(flagged.standards.slice(i, i + 8))
log(`${flagged.rules.length} flagged analysis rules in ${ruleGroups.length} groups; ${flagged.standards.length} flagged standards in ${stdGroups.length} groups`)

phase('Review')
// Standards share one file, so their groups run one after another; analysis groups touch separate files and run in parallel.
const ruleResults = parallel(ruleGroups.map((g, i) => () => agent(`${RULES}

Items (analysis rules; the file is ${ROOT}/learn/analysis/<source>.json and n is the index in its "rules" array; indices shift when you delete, so work from the highest n down):
${g.map(x => x.items.map(r => `- ${x.src} rule ${r.n} [Jev: ${r.verdict} ${r.confidence}]: ${r.rule}`).join('\n')).join('\n')}`,
  { label: `rules:${i + 1}`, phase: 'Review', schema: VERDICT })))
const stdResults = (async () => {
  const out = []
  for (const [i, g] of stdGroups.entries()) {
    out.push(await agent(`${RULES}

Items (house standards in ${ROOT}/synthesis/standards.json; find each by id). Each names the source Jev could not confirm it against, but check ALL of the standard's sources before deciding: a standard stands if any cited source supports it, and a cited source that does not support it should be dropped from its "sources":
${g.map(s => `- ${s.std} vs ${s.source} [Jev: ${s.verdict} ${s.confidence}]`).join('\n')}`,
      { label: `standards:${i + 1}`, phase: 'Review', schema: VERDICT }))
  }
  return out
})()
const results = [...(await ruleResults), ...(await stdResults)].filter(Boolean)

phase('Recheck')
const all = results.flatMap(r => r.items)
const recheck = await agent(`From ${ROOT}:
1. Record the review decisions so settled items stop being flagged: write this JSON to a temp file (mktemp) and run python3 tools/wiki.py review-log < that file:
${JSON.stringify(all)}
2. Run python3 tools/wiki.py check; python3 tools/wiki.py cite-check ${[...new Set(flagged.rules.map(r => r.source))].join(' ')}; python3 tools/wiki.py cite-check --standards; python3 tools/wiki.py flagged.
Report the new counts for analysis rules and for standards, and how many items are still flagged (Jev's confidence varies a little between runs, so borderline items can reappear; run this workflow again for them). Do not edit other files.`,
  { label: 'recheck', phase: 'Recheck' })
return {
  counts: { confirmed: all.filter(x => x.decision === 'confirmed').length, fixed: all.filter(x => x.decision === 'fixed').length,
    removed: all.filter(x => x.decision === 'removed').length },
  removed: all.filter(x => x.decision === 'removed'), fixed: all.filter(x => x.decision === 'fixed'), recheck,
}
