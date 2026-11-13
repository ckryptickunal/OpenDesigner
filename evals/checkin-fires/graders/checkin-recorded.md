---
type: regex
target: { source: file, path: opendesigner/state.json }
pattern: '"checkins":\s*\{\s*"last":\s*\{\s*"date":\s*"(?!2026-11-10)'
flags: s
---
