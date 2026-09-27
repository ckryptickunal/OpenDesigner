# Changelog

All notable changes to OpenDesigner are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/). Detailed reasons for each product decision are in [`_coordination/DECISIONS.md`](_coordination/DECISIONS.md).

## [Unreleased]: planned as 0.1.0

The first public version: the research base, the synthesis that turns it into an interview, and the first skills, engine and host packaging.

### Added

- **Learning wiki** (`learn/`, lane L19): the knowledge OpenDesigner draws from sources its owner trusts, kept as an independent, self-updating knowledge base.
  - It covers 99 sources, each with a verified analysis, and an OpenWiki Markdown wiki with 53 cross-source topic pages.
  - `learn/MAP.md` indexes it by area, standard, card and question. `learn/IMPROVING.md` explains how to change the app from it.
  - The pipeline runs through `tools/wiki.py` (`add`, `fetch`, `check`, `ingest`, `trace`, `cite-check` with TypeSafe's Jev, `standards`, `map`, `proposals`, `next`, `upstream`) and five saved workflows in `.claude/workflows/`.
  - OpenWiki is pinned in `learn/openwiki.lock.json` and checked weekly in CI.
  - The rules are in `docs/KNOWLEDGE.md`.
- **House standards** (`synthesis/standards.json`, v2): 455 rules from the owner's non-negotiable sources (Emil Kowalski's writing and skills, Sonner, animations.dev, Vaul).
  - Each rule is citation-checked and reviewed.
  - The engine applies and locks them for each project's platforms and stack, including new tokens such as the 0.97 press scale.
  - Commands: `engine.py standards [--update]`, and `standard override|restore|add|remove`, which covers project standards, per-path overrides and `--beats`.
  - Constraints stop values that break a rule (no ease-in curves on UI; UI motion stays under 300 ms unless a standard names the exception).
  - The interview skips questions a standard settles and refuses options that break one.
  - `review` flags code that breaks a standard. DESIGN.md carries a short summary, with the full list in `opendesigner/standards.md`.
- **Decision Cards from the wiki:** 164 in `research/L19-learning-wiki.md`, with 253 proposed changes and 75 conflicts with older research.
  - Three cards are adopted so far; the rest are listed as pending in `synthesis/QUESTIONNAIRE.md` for lane L20.
  - "Now / As it grows" notes for 30 high-impact questions appear under each option.
- **Research search:** `tools/jev_nav.py find` also searches the house standards and ranks with BM25. It judges each card by its recommended default and marks older cards the house supersedes.

- **Research base:** 18 finished research lanes (L00 to L18, with L12 still open) written as 352 Decision Cards, with 2,740 sources logged in `traces/`, including rejected ones.
- **Benchmark:** 25 public design systems compared with real values in `benchmarks/`.
- **Synthesis:** the building-block ontology (271 nodes in 10 layers), the guided interview (193 questions on 27 screens, 6 of them planned and skipped until built, with Quick, Standard and Expert modes), the eight dials with generation formulas and 13 famous systems as dial recipes, and the decision graph (352 decisions, 465 dependencies, 12 cycles).
- **Starter design artifacts** in `design/`: a DTCG 2025.10 token set with 126 contrast-checked pairs, and four HTML artboards.
- **Coordination system** for parallel human and AI sessions: `tools/od.py`, `_coordination/PROTOCOL.md`, the board, heartbeats, inbox and decision log.
- **Research tools:** `tools/jev_nav.py` (status, search, citation check, card export, decision graph) and `tools/check_links.py` (offline Markdown link check).
- **Product specification:** `docs/SPEC.md` (copied from `synthesis/OPENDESIGNER-SPEC.md`).
- **Skills:** `opendesigner` (the interview), `opendesigner-extract`, `opendesigner-extend` and `opendesigner-export`, in the Agent Skills format, with generated copies in `.agents/skills/` and `.claude/skills/`, knowledge files built from the synthesis, and 8 JSON-fed visual templates.
- **Host packaging:** a Claude plugin and marketplace (`.claude-plugin/`), an Agent Plugins manifest (`plugin.json`), claude.ai skill zips built by `tools/build_dist.py`, and a ChatGPT Project bundle (`chatgpt-project/`).
- **Engine** (being finished): `skills/opendesigner/scripts/engine.py` for state, generation, validation and exports.
- **Community and repository health:** README, CONTRIBUTING, Code of Conduct (Contributor Covenant 2.1), security policy, support, governance, citation file, issue forms, pull request template, labels, CI, `llms.txt`, `funding.json`, a social preview image, a sponsorship plan, and docs (`docs/HOW-IT-WORKS.md`, `docs/RESEARCH.md`, `docs/FAQ.md`, `docs/GITHUB-SETTINGS.md`, `docs/SEED-ISSUES.md`).
- **Licenses:** MIT for code, skills and data; CC BY 4.0 for research and documentation.
