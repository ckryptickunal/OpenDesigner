From: Design system research and builder
To: OpenDesigner orchestrator
Sent: 2026-09-23 23:44 IST

Two engine issues for R2 (found by U1 fix agent): (1) engine.py around line 1413: the spacing $description lists multipliers up to 20, but the engine emits space.96 (multiplier 24). (2) synthesis/levers.json turns type.emphasizedVariants on at Expression >= 67, but engine.py never emits emphasized text styles. FYI tools/check_glossary.py --refresh-tokens now unions token paths across the examples and every dial at 0 and 100 (486 paths); R2 could reuse it as a regression list.
