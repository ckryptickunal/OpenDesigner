---
type: source
title: "referodesign/refero_skill: README.md"
created: 2026-10-07
updated: 2026-10-07
video_id: referodesign-refero-skil-readme
url: https://github.com/referodesign/refero_skill/blob/a9b54a3/README.md
channel: referodesign/refero_skill (GitHub, MIT)
published: commit a9b54a3
authority: reference
tags:
  - ai-design
  - research-first
  - references
  - mcp
  - agent-skills
  - plugin-packaging
  - refero
---

# referodesign/refero_skill: README.md

## Metadata

- Page ID: `referodesign-refero-skil-readme`
- Publisher: referodesign/refero_skill (GitHub, MIT)
- Published: commit a9b54a3
- URL: https://github.com/referodesign/refero_skill/blob/a9b54a3/README.md

## Summary

This README describes Refero, a package of one design skill plus a read-only MCP connection that gives AI agents access to curated visual styles, 150,000+ real app screens and 6,000+ user flows. Its core idea is that research is mandatory before implementation: the agent researches styles, then real screens and flows, extracts concrete patterns and locks references before building. It bundles guidance on typography, color, spacing, motion, icons and copywriting, and checks substantial visual work against the chosen direction before handoff. For someone building a design system, it is a model of an evidence-first AI design workflow and of how to ship one skill across many AI hosts. Most of the file is install and packaging instructions rather than design guidance.

## Key Ideas

- Make research a required step before any design implementation
- Research visual styles first, then real screens and user flows only when the task needs them
- Extract concrete patterns and lock the chosen references before building
- Tie design decisions to evidence rather than generic AI defaults
- Check substantial visual work against the selected direction before handing it off
- Bundle craft guidance for typography, color, spacing, motion, icons and copywriting with the skill
- Ship one canonical skill folder and per-host manifests that all point to the same MCP endpoint
- Keep a skill's references folder beside its SKILL.md when installing manually
- Validate a release for manifests, versions, links, package boundaries and secret leaks

## Entities

- [[entities/refero|Refero]] (product): Package of one design skill plus a read-only MCP connection to curated visual styles, real app screens and user flows
- [[entities/refero-mcp|Refero MCP]] (tool): Read-only MCP connection at api.refero.design/mcp that serves styles, screens and flows; uses OAuth
- [[entities/refero-design-skill|refero-design skill]] (tool): The single canonical skill that enforces research-first design and holds bundled craft references
- [[entities/claude-code|Claude Code]] (product): One of the hosts the plugin installs into via a plugin marketplace
- [[entities/codex|Codex]] (product): OpenAI host that installs Refero from the Plugins Directory or GitHub marketplace
- [[entities/gemini-cli|Gemini CLI]] (product): Host that installs Refero as an extension
- [[entities/cursor|Cursor]] (product): Host that installs Refero from its plugin marketplace once approved
- [[entities/mcp-registry|MCP Registry]] (tool): Official registry described by the package's server.json

## Topics

- [[topics/ai-assisted-design|AI-assisted design]]: Describes an AI design workflow where the agent must research real references, lock them and check the result against the selected direction instead of using generic AI defaults.
- [[topics/design-process|Design process]]: Lays out a five-step order: research styles, then screens and flows, extract patterns and lock references, apply craft guidance, check work before handoff.
- [[topics/design-resources|Design resources]]: Refero offers curated visual styles, 150,000+ real app screens and 6,000+ user flows; live research needs a paid plan, bundled craft references need no account.

## Notable Claims

- With live Refero research, agents can use curated visual styles, 150,000+ real app screens and 6,000+ user flows from well-designed products Evidence: 150,000+ real app screens, and 6,000+ user flows from
- Live Refero research requires a paid Refero plan Evidence: Live research requires a paid Refero plan
- No account is required for the bundled craft references Evidence: No account is required for the bundled craft references
- All connection manifests use the same production endpoint and contain no access tokens Evidence: All connection manifests use the same production endpoint and contain no access tokens
- Keeping both the old root SKILL.md layout and the new layout creates duplicate skills Evidence: keeping both layouts creates duplicate skills
- The release check validates manifests, versions, local links, the canonical MCP URL, package boundaries and common secret leaks Evidence: The check validates manifests, versions, local links, the canonical MCP URL, package

## Quotes

> The skill makes research mandatory before implementation.

> Keeps design decisions tied to evidence instead of generic AI defaults.

<!-- od:learn -->

## For OpenDesigner

- Authority: **reference**
- Caveat: This is a product README and partly promotional: live research requires a paid Refero plan
- Caveat: Most of the file is install and packaging instructions; the design guidance itself lives in the skill's references, which this file does not include
- Caveat: Install commands and the Cursor listing status are as of commit a9b54a3 and may change

### Rules and practices

- **must** (process, all): Research visual references before implementing any design; do not start building from generic AI defaults Why: Keeps design decisions tied to evidence instead of generic AI defaults [The skill makes research mandatory before implementation]
- **should** (process, all): Research visual styles first, and only then real screens and user flows when the task needs them Why: The source states the order but gives no reason; style sets the direction before concrete screens are sought [inferred] [Researches visual styles first, then real screens and user flows when the task needs them]
- **should** (process, all): Extract concrete patterns from the references and lock the chosen references before implementation Why: Keeps design decisions tied to evidence instead of generic AI defaults [Extracts concrete patterns and locks references before implementation]
- **should** (process, all): Check substantial visual work against the selected direction before handoff Why: The source gives no reason; catches drift from the chosen direction before handoff [inferred] [Checks substantial visual work against the selected direction before handoff]
- **should** (tooling, all): When installing a skill manually, copy the whole skill directory so its references/ files stay beside SKILL.md Why: So the skill's references/ files remain beside SKILL.md Values: skills/refero-design/. [copy the entire `skills/refero-design/` directory into the client's skills directory so its `references/` files remain beside `SKILL.md`]
- **must** (tooling, all): Do not keep an old root-level SKILL.md install alongside the new skills/ layout Why: Keeping both layouts creates duplicate skills [keeping both layouts creates duplicate skills]
- **should** (tooling, all): Point every host's connection manifest at the same production endpoint and keep access tokens out of them Why: The source states this as a fact about its manifests, not a reason; one endpoint avoids drift and no tokens avoids leaking secrets [inferred] Values: https://api.refero.design/mcp. [All connection manifests use the same production endpoint and contain no access tokens]
- **should** (tooling, all): Before tagging a release, run the release check plus platform-native validation and clean-profile install tests Why: The check covers manifests, versions, local links, the canonical MCP URL, package boundaries and common secret leaks; platform-native and clean-profile install tests cover what it does not Values: scripts/check-release. [Platform-native validation and clean-profile install tests are still run before tagging a release]

### Decisions it informs

- How should the agent install the design skill: full plugin with live research, or the standalone skill only?
  - Plugin (skill plus MCP): Agent gets live research over styles, screens and flows plus the methodology; needs Refero sign-in, and live research needs a paid plan When: The person wants live reference research
  - Standalone skill: Agent gets the design methodology and bundled craft references without an account When: The client already has Refero MCP configured or only the methodology is needed

### Process

1. Research styles: Research visual styles first, then real screens and user flows when the task needs them
2. Extract and lock: Extract concrete patterns and lock references before implementation
3. Apply craft guidance: Apply bundled guidance for typography, color, spacing, motion, icons and copywriting
4. Tie to evidence: Keep each design decision tied to the researched evidence instead of generic AI defaults
5. Check before handoff: Check substantial visual work against the selected direction before handoff
6. Validate release: Run scripts/check-release to validate manifests, versions, local links, the MCP URL, package boundaries and secret leaks; run platform-native validation and clean-profile install tests before tagging

### Examples and visual references

- One canonical skill folder plus per-host manifests (.mcp.json, mcp.json, gemini-extension.json, .codex-plugin/, .claude-plugin/, .cursor-plugin/, server.json) (refero_skill repository): Shows how a single design skill is packaged for Claude Code, Codex, Cursor and Gemini CLI from one source

### Numbers

- 150,000+: Real app screens available through live Refero research [150,000+ real app screens, and 6,000+ user flows]
- 6,000+: User flows available through live Refero research [150,000+ real app screens, and 6,000+ user flows]

<!-- /od:learn -->
