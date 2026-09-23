# Changelog

All notable changes to OpenDesigner are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/). Detailed reasons for each product decision are in [`_coordination/DECISIONS.md`](_coordination/DECISIONS.md).

## [Unreleased]: planned as 0.1.0

The first public version: the research base, the synthesis that turns it into an interview, and the first skills, engine and host packaging.

### Added

- **Research base:** 18 finished research lanes (L00 to L18, with L12 still open) written as 352 Decision Cards, with 2,740 sources logged in `traces/`, including rejected ones.
- **Benchmark:** 25 public design systems compared with real values in `benchmarks/`.
- **Synthesis:** the building-block ontology (271 nodes in 10 layers), the guided interview (192 questions on 27 screens, with Quick, Standard and Expert modes), the eight dials with generation formulas and 13 famous systems as dial recipes, and the decision graph (352 decisions, 465 dependencies, 12 cycles).
- **Starter design artifacts** in `design/`: a DTCG 2025.10 token set with 126 contrast-checked pairs, and four HTML artboards.
- **Coordination system** for parallel human and AI sessions: `tools/od.py`, `_coordination/PROTOCOL.md`, the board, heartbeats, inbox and decision log.
- **Research tools:** `tools/jev_nav.py` (status, search, citation check, card export, decision graph) and `tools/check_links.py` (offline Markdown link check).
- **Skills, knowledge files, visual templates and the engine** (in progress): `skills/opendesigner/`, `data/`, `chatgpt-project/`.
- **Community and repository health:** README, CONTRIBUTING, Code of Conduct (Contributor Covenant 2.1), security policy, support, governance, citation file, issue forms, pull request template, labels, CI, `llms.txt`, and docs (`docs/HOW-IT-WORKS.md`, `docs/RESEARCH.md`, `docs/FAQ.md`).
- **Licenses:** MIT for code, skills and data; CC BY 4.0 for research and documentation.
