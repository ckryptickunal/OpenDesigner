---
type: regex
target: { source: file, path: opendesigner/state.json }
pattern: '"checkins":\s*\{\s*"last":\s*\{[^}]*"decisions":\s*1[1-9]'
flags: s
---
