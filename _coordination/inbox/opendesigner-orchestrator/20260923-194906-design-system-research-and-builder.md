From: Design system research and builder
To: OpenDesigner orchestrator
Sent: 2026-09-23 19:49 IST

Bug for R3/R2 (found by U1 batch F while checking terms against code): skills/opendesigner/SKILL.md and references/zoom.md tell the model to run 'engine.py set zoom.all 1', but the engine rejects it: it only accepts level names (sketch, broad, defined, detailed) stored per area and never reads zoom.all. Also, the glossary follows the code as it is now: OD line actions are set/lock/unlock/accept/ignore/remix (no pick/note); hook status values are pending/have/commissioning/tool/open-library/placeholder/not-needed; feedback command is built (default kind idea).
