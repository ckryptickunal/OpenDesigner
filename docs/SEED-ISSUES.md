# Seed issues

These are twenty-one ready-to-file issues. They come from the "Open questions / gaps" sections at the end of each research lane, the verification backlog and the roadmap. Each has a title, labels (all defined in `.github/labels.yml`) and a body that can be pasted as is. The table also says whether it suits a first-time contributor.

All 21 were filed on GitHub on 2026-09-23 as issues #1 to #21, with the same numbers as below. To file them again somewhere else, run this for each entry: `gh issue create -R ckryptickunal/OpenDesigner --title "<title>" --label "<labels>" --body-file <body>`. Create the labels first.

| # | Title | Labels | Good first issue |
|---|---|---|---|
| 1 | Verify Spectrum 2 color, type and spacing guidance against the live docs | research, verification | yes |
| 2 | Settle two Fluent 2 conflicts: radius names and Subtitle 1 line height | research, disputed | yes |
| 3 | Decide which Material 3 tracking values apply to Roboto-based products | research, disputed | no |
| 4 | Re-check Polaris values against the web-components era | research, verification | no |
| 5 | Find a primary source for the 16px input font size rule on iOS Safari | research, needs-source | yes |
| 6 | Replace WCAG criteria cited from memory with the official texts | research, accessibility, needs-source | yes |
| 7 | Keep Figma's "Button states" contrast and focus values out of the defaults | accessibility, verification | yes |
| 8 | Research accessibility law (EAA, ADA, Section 508) for the audience stage | research, accessibility, help wanted | no |
| 9 | Hands-on test: what does Figma's native DTCG export write? | research, figma, tokens, help wanted | no |
| 10 | Start lane L12: inspect three community design-system files through the Figma MCP server | research, figma, help wanted | no |
| 11 | Hands-on test of three reference extractors on the same site | research, help wanted | no |
| 12 | Add European and Japanese driving HMI rules to the car device class | research | yes |
| 13 | Find evidence that isolates corner radius and perceived personality | research, needs-source | no |
| 14 | Per-script type size adjustments for Devanagari, Arabic and CJK | research, accessibility, help wanted | no |
| 15 | Benchmark more public design systems (one PR per system) | research | yes |
| 16 | Verify L08 component anatomy and radius values marked [inferred] | research, verification, help wanted | no |
| 17 | Preference-test generated themes to validate the lever matrix | research, design, help wanted | no |
| 18 | Define an asset-reference token convention for icons, images and aspect ratios | tokens, building-block | no |
| 19 | Test how hosts handle the same skill in .agents/skills and .claude/skills | host-support | yes |
| 20 | Phase 2: a stateless MCP server with MCP Apps views | engine, host-support, help wanted | no |
| 21 | Translate the README and FAQ | translation, docs | yes |

Add the `good first issue` label to every row marked "yes" when creating it.

---

## 1. Verify Spectrum 2 color, type and spacing guidance against the live docs

**Labels:** research, verification, good first issue

Several lanes could not read Adobe's Spectrum 2 site at the time (403, or the page did not render). So Spectrum values came only from the `spectrum-design-data` token source:

- `research/L01-color.md`, Open questions 1: the contrast-indexed palette approach is confirmed for Spectrum v6 only.
- `research/L02-typography.md`, Open questions: usage rules (detail vs body) not verified.
- `research/L03-space-layout.md`, Open questions: spacing values may differ from the published docs.

**Task:** open the current Spectrum 2 docs. Compare their color, type and spacing values and rules with what the lanes say. Log each page, with its date, in the lane's trace (`traces/L01-trace.md` etc.).

**Done when:** each claim is confirmed or corrected with a Tier A source id, and `python3 tools/jev_nav.py check` passes.

## 2. Settle two Fluent 2 conflicts: radius names and Subtitle 1 line height

**Labels:** research, disputed, good first issue

Fluent's design site and its token package disagree in two places:

1. Radius (`research/L04-shape-depth-motion.md`, Open questions 3). The site says "Large 8px / X-Large 12px". The token package has Large = 6px and XLarge = 8px. It added 2XL to 6XL in January 2026 [S-L04-006] [S-L04-007].
2. Web Subtitle 1 line height (`research/L02-typography.md`, Open questions). The site says 20/26. The tokens package says `lineHeightBase500` = 28px [S-L02-007] [S-L02-008].

**Task:** find which is current, using the release notes, the Fluent UI repo or the Figma kit. Record the answer in both lanes, with the rule used to decide. GOVERNANCE.md has the rule: shipped code beats prose when they disagree, and the disagreement is recorded.

## 3. Decide which Material 3 tracking values apply to Roboto-based products

**Labels:** research, disputed

`research/L02-typography.md`, Open questions. Shipped Compose tokens use Roboto-era tracking: Body Large 0.5sp, Body Medium 0.2sp, Display Large -0.2sp. But m3.material.io's token module shows Google Sans with 0 tracking on most styles [S-L02-005] [S-L02-006]. The builder needs one answer for a non-Google product using Roboto.

**Task:** find Google's current guidance (Compose releases, Material Web tokens, the M3 site). Recommend a default, and state which products each set applies to.

## 4. Re-check Polaris values against the web-components era

**Labels:** research, verification

Polaris React is archived, and its docs redirect to shopify.dev web components. Several values came from the archived `polaris-tokens` source. They are the color, spacing, radius, elevation and icon values in L01, L03, L04, L05 and the L09 benchmark. Each lane's Open questions lists them. Polaris is also one of the 13 dial recipes in `synthesis/LEVERS.md` section C.

**Task:** compare the current web-component tokens with the archived values. Update the lanes and `benchmarks/systems/polaris.md`, and mark which values are historical.

## 5. Find a primary source for the 16px input font size rule on iOS Safari

**Labels:** research, needs-source, good first issue

`research/L02-typography.md`, Open questions. The claim is that iOS Safari zooms into inputs with a font size under 16px. It drives the mobile web minimum, but it could not be checked against a primary source [S-L02-064].

**Task:** find a WebKit or Apple source. Or reproduce it and document the device, iOS version and steps. Then update the card and trace.

## 6. Replace WCAG criteria cited from memory with the official texts

**Labels:** research, accessibility, needs-source, good first issue

Two lanes cite WCAG success criteria they could not fetch, tagged `[inferred]`:

- `research/L04-shape-depth-motion.md`, Open questions 12: 1.4.3 (the disabled exemption), 1.4.11, 2.2.2.
- `research/L13-ux-laws-heuristics.md`, Open questions: 1.3.1, 1.3.5, 1.4.1, 2.2.1, 2.4.4, 2.4.6, 3.1.5, 3.3.1 to 3.3.4.

Update (2026-09-24): after the V1 check, L13 cites the official Recommendation for 3.3.4 and 3.1.5 [S-V1b-006].

**Task:** fetch each criterion and its Understanding page from w3.org, and log them in the traces. Replace `[inferred]` with source ids where the claim holds. Correct any claim that does not.

## 7. Keep Figma's "Button states" contrast and focus values out of the defaults

**Labels:** accessibility, verification, good first issue

`research/L13-ux-laws-heuristics.md` has a cross-lane note to V1 about this. Figma's "Button states" article says all states need 4.5:1 contrast and focus rings need 3px [S-L13-106]. But WCAG exempts disabled components from 1.4.3, and 2.4.13 (AAA) specifies a 2 CSS px perimeter.

**Task:** confirm against the WCAG texts. Then check `synthesis/LEVERS.md`, `synthesis/levers.json` and the engine defaults to make sure neither value was imported. Report what you find in the issue.

## 8. Research accessibility law (EAA, ADA, Section 508) for the audience stage

**Labels:** research, accessibility, help wanted

`research/L11-process-governance.md`, Open questions 7. The legal landscape was not researched. Yet it decides the accessibility target the interview asks about (question 4.1 in L11, Q-aud-03 in `synthesis/QUESTIONNAIRE.md`).

**Task:** write a short Decision Card per jurisdiction. Cover the EU European Accessibility Act, the US ADA and Section 508, and at least one more, such as India's RPwD Act. Each card says what the law requires of digital products, which WCAG version it points to, and the dates. Use Tier A sources only (the legal texts or the regulator's pages).

## 9. Hands-on test: what does Figma's native DTCG export write?

**Labels:** research, figma, tokens, help wanted

`research/L07-tokens-figma.md`, Open questions. Figma's help pages describe the DTCG import rules. They don't say what export writes: scopes, code syntax, descriptions, `$extensions` [S-L07-011] [S-L07-046]. The Figma exporter depends on this.

**Task:**
1. Create a small variable collection with two modes, every variable type, scopes, code syntax and descriptions.
2. Export it.
3. Commit the exported JSON as a fixture, and document what survived and what did not.

## 10. Start lane L12: inspect three community design-system files through the Figma MCP server

**Labels:** research, figma, help wanted

Lane L12 is open on `_coordination/BOARD.md`. So far, Figma behavior in the research comes from docs, not real files.

**Task:**
1. Claim L12 (`python3 tools/od.py claim L12`).
2. Open three community kits in Figma desktop, for example Simple Design System, the Material 3 kit and an iOS kit.
3. Read their variables, collections, modes and component properties through the Figma MCP server.
4. Write `research/L12-figma-mcp-handson.md` with Decision Cards and a trace. Follow `_coordination/PROTOCOL.md`.

## 11. Hands-on test of three reference extractors on the same site

**Labels:** research, help wanted

`research/L17-how-systems-get-made.md`, Open questions. The reliability ratings for reference intake (Part F2) are a synthesis, not a benchmark. No vendor except Brandfetch publishes accuracy numbers.

**Task:** pick one public site with published tokens, so there is ground truth. Run three extraction tools on it. Record which values each got right for color, type, spacing, radius and shadows, and add the results to L17 Part F2.

## 12. Add European and Japanese driving HMI rules to the car device class

**Labels:** research, good first issue

`research/L14-device-practices.md`, Open questions. Only the US NHTSA guidelines (voluntary) were read. The European Statement of Principles on HMI and Japan's JAMA guidelines were not. The car rules become hard validator rules (`synthesis/LEVERS.md` section D1), so regional differences matter.

**Task:** summarize glance time, task time, target size and animation rules from each, with sources. Add them to the L14 car section.

## 13. Find evidence that isolates corner radius and perceived personality

**Labels:** research, needs-source

`research/L04-shape-depth-motion.md`, Open questions 11. The only measured evidence on how radius "reads" is Google's M3 Expressive research. It bundles shape with color, size and containment [S-L04-063]. The Roundness dial rests on it.

**Task:** search for peer-reviewed or practitioner studies (Tier A or B) on corner radius in interfaces. Look for effects on perceived friendliness, trust or modernity. Report what exists, even if the answer is "nothing isolates it".

## 14. Per-script type size adjustments for Devanagari, Arabic and CJK

**Labels:** research, accessibility, help wanted

`research/L02-typography.md`, Open questions. No official per-script size adjustment was found: for example, how much larger Devanagari should be than Latin at the same nominal size. W3C's Indic layout requirements are a 2020 draft. The builder already emits script-aware line height and tracking (`synthesis/LEVERS.md` D1, "Script safety").

**Task:** gather values from platform guidance, font vendors (Google Fonts, Noto) and shipped systems. Propose defaults with sources. Native readers of these scripts are especially welcome.

## 15. Benchmark more public design systems (one PR per system)

**Labels:** research, good first issue

`benchmarks/L09-benchmark-matrix.md` covers 25 systems. Not yet covered: Workday Canvas, Elastic EUI, NYPL Reservoir, Wise, Monzo and others listed on component.gallery.

**Task:**
1. Pick one system.
2. Copy the structure of an existing file in `benchmarks/systems/`, for example `primer.md`.
3. Fill it with real values from the system's own docs or published tokens.
4. Log every source in `traces/L09-trace.md`.

One system per PR keeps reviews small.

## 16. Verify L08 component anatomy and radius values marked [inferred]

**Labels:** research, verification, help wanted

`research/L08-components-patterns.md`, Open questions. In the 64-component catalog (`research/L08-component-catalog.md`), many anatomy details and some radii are marked `[inferred]`. Also unverified: M3 focus indicator thickness and offset, and Fluent appearance values beyond the main four.

**Task:** pick one component family: buttons, inputs, selection controls or overlays. Check each `[inferred]` value against each system's spec. Replace the tag with a source id or a correction.

## 17. Preference-test generated themes to validate the lever matrix

**Labels:** research, design, help wanted

`research/L06-brand-voice.md`, Open questions. Most cells of the brand lever matrix are practitioner inference. `synthesis/LEVERS.md` lists the weakest mappings (coupling coefficients, macro offsets) in "Weak evidence and open contradictions". L06 suggests Material's own method: paired comparisons on hierarchy, utility and style attributes [S-L06-011].

**Task:** design a small, repeatable preference test. Generate pairs of themes that differ on one dial. Ask people which feels more "playful", "premium" and so on. Publish the protocol and results. Start with a protocol PR before running anything.

## 18. Define an asset-reference token convention for icons, images and aspect ratios

**Labels:** tokens, building-block

This comes from a cross-lane note, L05 to L07, on `_coordination/BOARD.md`. DTCG has no type for icons, images or aspect ratios. So the builder needs its own convention for referencing assets from tokens. Examples: an icon token that points to a file, or an allowed-ratio list. The designer hooks in `research/L17-how-systems-get-made.md` Part H produce these assets.

**Task:** propose the convention (likely in `$extensions`), with examples. Say how each exporter treats it, and whether an open DTCG issue already covers it. Discuss in the issue before implementing.

## 19. Test how hosts handle the same skill in .agents/skills and .claude/skills

**Labels:** host-support, good first issue

`research/L18-ai-first-distribution.md`, Open questions. OpenDesigner ships generated copies of each skill in both folders. Clients that scan both (Cursor, VS Code with Copilot and others) may list the skill twice. How each one removes duplicates is unverified [S-L18-251].

**Task:** clone the repo and open it in one host you use. Report whether the `opendesigner` skill appears once or twice, and which copy runs. One comment per host is enough; include the host version.

## 20. Phase 2: a stateless MCP server with MCP Apps views

**Labels:** engine, host-support, help wanted

Sources: `_coordination/REPO-PLAN.md` and `research/L18-ai-first-distribution.md` Part I. MCP Apps is the only visual standard that renders in both Claude and ChatGPT (and VS Code, Cursor, Goose). Phase 2 is a stateless MCP server in `server/`. It serves the same visual templates as MCP App views, so choices can be made by clicking in chat.

**Task:** write a design proposal first. It should cover:
- which tools and views;
- how a choice returns to the model (DC-L18-07);
- hosting and auth (DC-L18-05);
- how it reuses `skills/opendesigner/assets/templates/`.

Test locally in Claude Desktop with a stdio entry before any remote hosting.

## 21. Translate the README and FAQ

**Labels:** translation, docs, good first issue

OpenDesigner is for engineers everywhere. Translations of `README.md` and `docs/FAQ.md` lower the barrier most.

**Task:** add `docs/i18n/<language-code>/README.md` and `FAQ.md`. Keep links pointing at the English files for everything else. A second native speaker should review before merge; mention one in the PR if you can.
