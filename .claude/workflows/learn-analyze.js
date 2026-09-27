export const meta = {
  name: 'learn-analyze',
  whenToUse: 'New sources were fetched into learn/raw/ and need analysis JSON. Pass the output of: python3 tools/wiki.py pending --work-items',
  description: 'Analyse each learning-wiki source into OpenDesigner analysis JSON, then adversarially verify it against the source',
  phases: [
    { title: 'Analyze', detail: 'one agent per source or small group writes learn/analysis/<id>.json' },
    { title: 'Verify', detail: 'a fresh agent checks every rule, number and quote against the raw text and fixes the JSON' },
  ],
}

// args: the output of `python3 tools/wiki.py pending --work-items`, or {root: '<repo path>', items: [...]}
const ITEMS = Array.isArray(args) ? args : args.items
const ROOT = (!Array.isArray(args) && args.root) || '/Users/Kunal/Desktop/Design-System'

const SCHEMA_DOC = `
Write ONE JSON file per raw source at ${ROOT}/learn/analysis/<source id>.json (the id is the "Video ID:" header line of the raw file). Shape:
{
  "summary": "3-6 plain sentences: what the source teaches and why it matters to someone building a design system",
  "key_ideas": ["5-15 short ideas, in your own words"],
  "entities": [{"name": "Sonner", "type": "person|company|product|library|tool|concept", "description": "one line on its role here"}],
  "topics": [{"name": "<copy EXACTLY from learn/taxonomy.json topics[].name>", "summary": "what this source says about the topic"}],
  "claims": [{"claim": "a factual or causal claim the source makes", "evidence": "where: section heading or a short phrase that appears near it in the raw text"}],
  "quotes": ["at most 3 verbatim quotes, each 15 words or fewer"],
  "tags": ["short-lowercase-tags"],
  "authority": "<the authority given to you>",
  "rules": [{"rule": "imperative, specific rule", "why": "the reason the source gives", "kind": "do|dont", "strength": "must|should|consider", "area": "color|typography|layout|shape|elevation|motion|components|patterns|content|accessibility|platforms|process|tokens|tooling", "applies_to": "all|web|ios|android|desktop|react|css", "values": ["exact values the source states, e.g. 200ms, cubic-bezier(0.23, 1, 0.32, 1), scale(0.95)"], "evidence": "section heading or short phrase near it"}],
  "decisions": [{"question": "a design decision in plain words", "options": [{"name": "...", "effect": "what it looks/feels like, or what it does to the product", "when": "when to pick it"}], "recommendation": "what the source recommends and why, or null", "maps_to": "Q-xxx-nn id from skills/opendesigner/references/questions.json if one clearly matches, else null", "evidence": "..."}],
  "process": [{"step": "short name", "detail": "how to do it"}],
  "examples": [{"what": "a concrete example, product or visual shown", "where": "which product/site/app, if named", "visual_note": "what it looks like and what it demonstrates"}],
  "numbers": [{"value": "60-30-10", "context": "what the number is about", "evidence": "..."}],
  "caveats": ["sponsor segments, self-promotion, dated info (e.g. a Figma feature list from a given year), opinion vs. fact, auto-caption errors that matter"]
}
Topic names must come from learn/taxonomy.json exactly. If nothing fits, add {"name": "...", "summary": "...", "new": true}.
Empty arrays are fine when a source has nothing of that kind; never pad.`

const FAITHFUL = `
- Scratch work: put any helper script or temp file in a directory of your own (mktemp -d), and never run a script you did not write in this task (other agents share the scratch space).
Faithfulness rules (hard):
- Everything must come from the raw text you read. Never add advice from your own knowledge. If you connect two things yourself, append " [inferred]" to that string.
- Numbers and values must appear in the source. Copy them exactly. Do not round or convert.
- YouTube transcripts are auto-captions without punctuation; fix an obvious mis-hearing only when certain (e.g. "fig ma" -> Figma) and never change a number.
- Sponsor reads and product plugs go in "caveats", not in rules.
- Quotes: verbatim, at most 3, each 15 words or fewer (copyright limit; this repo is public).
- Rules must be specific enough to act on ("Use ease-out for elements entering the screen" not "use good easing").
- For "maps_to", open skills/opendesigner/references/questions.json and search (grep) for the matching question; only map when it clearly matches.`

function analyzePrompt(item) {
  const files = item.files.map(f => `- id ${f.id} (${f.title}) raw: ${ROOT}/${f.raw}` + (f.media ? ` media list: ${ROOT}/${f.media}` : '')).join('\n')
  const auth = item.files[0].authority
  const authNote = auth === 'non-negotiable'
    ? 'Authority is NON-NEGOTIABLE: these rules become house standards that OpenDesigner applies and locks in every project. Completeness matters most: extract EVERY concrete rule, value, do/dont, threshold and checklist item, not a sample. Long files can have 40-120 rules; that is expected.'
    : auth === 'good-to-have'
    ? 'Authority is GOOD-TO-HAVE: these become recommended defaults. Extract every concrete rule and value.'
    : 'Authority is REFERENCE: trusted learning material. Extract the rules, decisions (with options and their visual effect), process steps and concrete examples that would help an AI guide someone through design decisions, and the visual examples that could become visual samples.'
  return `You are building the OpenDesigner learning wiki (repo ${ROOT}). Read each raw source below IN FULL (use Read with offset/limit for long files; do not skim), then write its analysis JSON.

${authNote}

Sources:
${files}

If a media list exists, look at it; for images whose alt text or position suggests they carry a design lesson (before/after, a UI example, a curve), you may download up to 6 with curl into ${ROOT}/learn/raw/_media/ and view them with Read, then describe what they show in "examples". Skip testimonials, avatars and logos.
${SCHEMA_DOC}
${FAITHFUL}

After writing, run: python3 ${ROOT}/tools/wiki.py check 2>&1 | grep -E "<your ids>|^check" (replace with your ids) and fix every ERROR for your files. Do not edit any other file.
Return a one-line summary per file: id, number of rules, decisions, process steps, examples.`
}

function verifyPrompt(item) {
  const files = item.files.map(f => `- ${ROOT}/learn/analysis/${f.id}.json  <-  raw ${ROOT}/${f.raw}`).join('\n')
  return `You are an adversarial verifier for the OpenDesigner learning wiki. Another agent wrote analysis JSON for these sources:
${files}

Read each raw file IN FULL, then each analysis JSON. Try to REFUTE every entry:
- rules: does the source actually say this? Is the value exact? Is strength right (must only if the source states it as a rule or calls breaking it a mistake)? Is "why" the source's reason, not invented?
- numbers and values: each must appear in the raw text exactly.
- quotes: each must be verbatim in the raw text and 15 words or fewer; max 3.
- claims/examples: supported by the text? Sponsor content must be in caveats only.
- decisions.maps_to: open skills/opendesigner/references/questions.json and confirm the id exists and matches; else set null.
- Anything added from outside knowledge without " [inferred]" must be removed or marked.
Also check COMPLETENESS: list important rules, values or decisions in the source that the analysis missed, and add them (same schema).${item.files[0].authority === 'non-negotiable' ? ' This source is NON-NEGOTIABLE (house standards): completeness is critical; walk the source section by section and make sure every concrete rule and value is captured.' : ''}

Fix the JSON files in place (keep the schema). Then run python3 ${ROOT}/tools/wiki.py check and fix any ERROR for these files. Edit nothing else.`
}

const VERDICT = {
  type: 'object',
  properties: {
    files: { type: 'array', items: { type: 'object', properties: {
      id: { type: 'string' },
      removed_or_fixed: { type: 'integer', description: 'entries removed or corrected as unsupported/wrong' },
      added: { type: 'integer', description: 'missed entries added' },
      rules_after: { type: 'integer' },
      notes: { type: 'string', description: 'the most important corrections, one line' },
    }, required: ['id', 'removed_or_fixed', 'added', 'rules_after', 'notes'] } },
  },
  required: ['files'],
}

// args: compact [{k: key, a: authority, d: raw folder, ids: [...]}]
const items = ITEMS.map(it => ({
  key: it.k,
  files: it.ids.map(id => ({ id, title: id, authority: it.a, raw: `learn/raw/${it.d}/${id}.txt`,
    media: `learn/raw/${it.d}/${id}.media.json (may not exist)` })),
}))
log(`${items.length} work items, ${items.reduce((n, i) => n + i.files.length, 0)} raw files`)

const results = await pipeline(
  items,
  (item) => agent(analyzePrompt(item), { label: `analyze:${item.key}`, phase: 'Analyze' }),
  (summary, item) => agent(verifyPrompt(item), { label: `verify:${item.key}`, phase: 'Verify', schema: VERDICT })
    .then(v => ({ key: item.key, analysis: summary, verify: v })),
)

return results.map((r, i) => r || { key: items[i].key, failed: true })
