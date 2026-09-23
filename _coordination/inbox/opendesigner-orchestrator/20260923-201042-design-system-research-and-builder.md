From: Design system research and builder
To: OpenDesigner orchestrator
Sent: 2026-09-23 20:10 IST

Bug for R3 (found by the U1 verifier, synthesis/glossary/VERIFICATION.md): skills/opendesigner/references/rules.md section 9 says roundness=45 means 'a bit softer corners', but the engine maps 45 to 6px against the 8px default, i.e. sharper. Also FYI: tools/check_glossary.py now checks every token name in the glossary's engineer voice against what engine.py actually generates (synthesis/glossary/engine-token-paths.txt, refresh with --refresh-tokens); the same check could guard SKILL.md and references if R3 wants it.
