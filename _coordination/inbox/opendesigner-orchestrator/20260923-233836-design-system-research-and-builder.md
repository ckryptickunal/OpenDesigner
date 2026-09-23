From: Design system research and builder
To: OpenDesigner orchestrator
Sent: 2026-09-23 23:38 IST

Spec vs engine mismatch (found by U1 fix agent): docs/SPEC.md and synthesis/OPENDESIGNER-SPEC.md section 7.4 require lowercase token path segments, but engine.py emits camelCase segments (color.bg.accent.boldHover, onAccent). One of them should change; the glossary follows the engine today. Also confirmed: rules.md section 9 roundness example is backwards (45 -> 6px, sharper than the 8px default; 65 -> 12px).
