// Project Wallace css-analyzer on one CSS file; writes its "values" section (the design-token view) as JSON.
import { readFileSync, writeFileSync } from 'node:fs';
const [mod, input, out] = process.argv.slice(2);
const { analyze } = await import(mod);
const r = analyze(readFileSync(input, 'utf8'));
writeFileSync(out, JSON.stringify({ values: r.values, stylesheet: { size: r.stylesheet.size }, declarations: r.declarations.total }, null, 1));
console.log('value groups:', Object.keys(r.values).join(', '));
