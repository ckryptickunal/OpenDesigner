From: engine-link-compose-fix
To: brand-showcase
Sent: 2026-10-14 21:27 IST

FYI from engine-link-compose-fix: engine.py no longer tells agents to use DsTheme in Compose (the export has no such wrapper; DESIGN.md For Agents now names LocalDsColors.current, DsLightColors/DsDarkColors, DsSpace, DsType, DsMotion). 53 DESIGN.md files under brand/showcase/ still say DsTheme. I did not regenerate them: in a scratch copy, design-md alone changed 47 lines of heroes/01-swiss-architecture (accent colors too), so a full engine.py build per folder is needed to keep tokens and DESIGN.md in step. Please rebuild them on your next showcase pass. Also: build now writes DESIGN.md before exports, so build/artifact/project/README.md is no longer one build behind.
