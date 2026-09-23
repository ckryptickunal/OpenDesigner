# Source registry (master list of candidate sources)

Built 2026-09-23 by lane L00. This is the list every lane can draw from. Each row was live-checked today with a scripted HTTP GET (certifi CA bundle, browser user-agent, redirects followed). The raw results are logged as S-L00-059 in `traces/L00-trace.md`. Community sentiment comes from the eight last30days runs summarized in `sources/COMMUNITY-SIGNAL.md`.

**Totals:** 100 entries. That covers 31 design systems and component libraries (42 rows, because some systems have several doc URLs), 11 Figma documentation pages, 14 standards/spec pages, 13 tooling sources, and 20 practitioner, survey, press and index sources.

**Tiers (from `_coordination/SCHEMA.md`).** A = the system's or standard's own official docs. B = recognized practitioner, vendor research or press with a track record; corroborate numbers. C = community or secondary; opinion only.

**How to read the columns**
- *Live check* is the HTTP status. "->" means the URL redirected, and the final location is shown. 403 usually means the site blocks scripts, not that it is down; open it in a browser.
- *Last-updated shown* is the date the page displays ("Updated", "Published", "Last updated") and/or the server's Last-Modified header. Many modern doc sites (m3.material.io, Figma Help, shadcn) show neither. A Last-Modified header records when the file was last deployed, not necessarily when the content was reviewed.
- *last30days signal* is whether the source or system came up in Reddit, HN, YouTube or GitHub discussion between 2026-08-24 and 2026-09-23, and with what sentiment. "Not mentioned" does not mean distrusted. X and LinkedIn were not covered.
- *Verdict*: USE, USE WITH CARE, USE AS DRAFT ONLY, OPINION ONLY, MOVED (use the new URL), STALE, UNREACHABLE, REJECT.

**Key registry findings**
1. **Moved:** Shopify Polaris (now shopify.dev/docs/api/polaris, delivered as web components), Twilio Paste (paste.twilio.design redirects to GitHub; docs now at paste-dsys.com), SAP Fiori (now sap.com/design-system/fiori-design-web/). Lanes quoting old URLs or old Polaris React docs are citing stale material.
2. **No public docs:** Spotify Encore. Treat it as a case study only.
3. **JavaScript-only sites** (scripts and fetch tools read nothing): m3.material.io, Apple HIG HTML (use the JSON endpoint `developer.apple.com/tutorials/data/design/human-interface-guidelines/<page>.json`), zeroheight's State of AI report. Read these in a browser or through the Figma/Apple JSON endpoints.
4. **Stale:** Sparkbox Design Systems Survey (latest edition 2022); NN/g "Design Systems 101" (2021, still fine as a definition); Spectrum v1 site (Last-Modified 2024); APCA calculator page ("Revised May 27, 2022").
5. **Unreachable today:** eightshapes.com (DNS/connect failure) and myndex.com/APCA (network error). Use Medium (EightShapes) and git.apcacontrast.com instead.
6. **Drafts, not standards:** WCAG 3.0 (Working Draft, 10 Sep 2026), WAI-ARIA 1.3 (Working Draft, 4 Jun 2026), DESIGN.md (draft spec, 21 Apr 2026). **Stable:** DTCG 2025.10, WCAG 2.2, WAI-ARIA 1.2. CSS Color 4 is formally a Candidate Recommendation Draft (13 Sep 2026) but is widely implemented in browsers, so OKLCH and P3 are safe to rely on.

## Design systems (official docs)

| # | Source | URL | Tier | Live check 2026-09-23 | Last-updated shown | last30days signal | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | Material Design 3 (Google) | https://m3.material.io/ | A | 200 | not shown | Mentioned (M3 Expressive; mixed: indie Android devs adopt it, iOS devs mock it; seen as Compose-first) | USE. Site renders only with JavaScript; read with a browser. Cross-check M3E API status in Compose release notes |
| 2 | Material 3 in Compose (Android Developers) | https://developer.android.com/develop/ui/compose/designsystems/material3 | A | 200 | Last updated 2026-09-22; Last-Modified 22 Sep 2026 | Indirect | USE for platform status; page updated 22 Sep 2026 |
| 3 | Compose Material3 release notes | https://developer.android.com/jetpack/androidx/releases/compose-material3 | A | 200 | Last-Modified 10 Sep 2026 | n/a | USE as the source of truth for M3 Expressive API maturity (stable 1.4.0 = 24 Sep 2025; 1.5.0-alpha28 = 9 Sep 2026) |
| 4 | Material Design blog | https://m3.material.io/blog | A | 200 | not shown | n/a | USE; JavaScript-only site |
| 5 | Material I/O 2026 post | https://m3.material.io/blog/whats-new-at-io26 | A | 200 | Published 2026-05-19 | n/a | USE but UNREAD: published 19 May 2026; body needs JavaScript. Claims seen only in snippets |
| 6 | Material Theme Builder | https://material-foundation.github.io/material-theme-builder/ | A | 200 | Last-Modified 21 May 2025 | n/a | USE for HCT/dynamic color; Last-Modified May 2025, check it reflects M3E |
| 7 | Apple Human Interface Guidelines | https://developer.apple.com/design/human-interface-guidelines/ | A | 200 | Last-Modified 21 Sep 2026 | Heavy (Liquid Glass, iOS 27) | USE. HTML is JavaScript-rendered; the docs JSON endpoint works (tutorials/data/design/human-interface-guidelines/<page>.json) |
| 8 | Apple HIG: Materials (Liquid Glass) | https://developer.apple.com/design/human-interface-guidelines/materials | A | 200 | Last-Modified 21 Sep 2026 | Heavy | USE; primary rules for regular vs clear glass, content-layer ban |
| 9 | WWDC26 videos | https://developer.apple.com/videos/wwdc2026/ | A | 200 | Last-Modified 23 Sep 2026 | Indirect (iOS 27 changes) | USE for Liquid Glass changes in iOS 27 |
| 10 | Fluent 2 (Microsoft) | https://fluent2.microsoft.design/ | A | 200 | not shown | Not mentioned | USE |
| 11 | Carbon (IBM) | https://carbondesignsystem.com/ | A | 200 | Last-Modified 09 Sep 2026 | Not mentioned | USE; Last-Modified 9 Sep 2026 |
| 12 | Polaris (Shopify), old domain | https://polaris.shopify.com/ | A | 200 -> shopify.dev/docs/api/polaris | not shown | Not mentioned | MOVED: redirects to shopify.dev/docs/api/polaris. Do not cite old Polaris React pages |
| 13 | Polaris (Shopify), current | https://shopify.dev/docs/api/polaris | A | 200 | not shown | Not mentioned | USE; Polaris is now delivered as web components under shopify.dev |
| 14 | Polaris web components | https://shopify.dev/docs/api/app-home/polaris-web-components | A | 200 -> shopify.dev/docs/api/app-home/latest/web-components | not shown | Not mentioned | USE (redirects to .../app-home/latest/web-components) |
| 15 | Atlassian Design System | https://atlassian.design/ | A | 200 | Last-Modified 23 Sep 2026 | Not mentioned | USE; Last-Modified 23 Sep 2026 |
| 16 | Primer (GitHub) | https://primer.style/ | A | 200 | not shown | Not mentioned | USE |
| 17 | Spectrum (Adobe), v1 site | https://spectrum.adobe.com/ | A | 200 | Last-Modified 28 Feb 2024 | Not mentioned | USE with care; Last-Modified Feb 2024. Prefer Spectrum 2 |
| 18 | Spectrum 2 (Adobe) | https://s2.spectrum.adobe.com/ | A | 200 | Last-Modified 25 Sep 2024 | Not mentioned | USE; Last-Modified Sep 2024 (static site); design data repo adobe/spectrum-design-data pushed 22 Sep 2026 |
| 19 | React Aria (Adobe) | https://react-spectrum.adobe.com/react-aria/ | A | 200 -> react-aria.adobe.com/ | Last-Modified 08 Sep 2026 | Mentioned (shadcn now supports React Aria) | USE; redirects to react-aria.adobe.com |
| 20 | Salesforce Lightning Design System 2 | https://www.lightningdesignsystem.com/ | A | 200 -> www.lightningdesignsystem.com/2e1ef8501 | updated 2026-04-02 | Not mentioned | USE; page title 'Lightning Design System 2', updated 2 Apr 2026 |
| 21 | Base (Uber) | https://base.uber.com/ | A | 200 | updated 2025-08-06 | Not mentioned | USE; updated 6 Aug 2025 |
| 22 | Ant Design | https://ant.design/ | A | 200 | Last-Modified 20 Sep 2026 | Not mentioned | USE; Last-Modified 20 Sep 2026 |
| 23 | GOV.UK Design System | https://design-system.service.gov.uk/ | A | 200 | not shown | Not mentioned | USE (gold standard for research-backed patterns) |
| 24 | USWDS | https://designsystem.digital.gov/ | A | 200 | Last-Modified 17 Sep 2026 | Not mentioned | USE; Last-Modified 17 Sep 2026 |
| 25 | Radix UI | https://www.radix-ui.com/ | A | 200 | not shown | Indirect (shadcn moved default to Base UI) | USE |
| 26 | Base UI | https://base-ui.com/ | A | 200 | not shown | Indirect (now shadcn default, Jul 2026) | USE |
| 27 | shadcn/ui | https://ui.shadcn.com/ | A | 200 | not shown | Strong positive (default scaffold for AI-built systems; shadcn lint) | USE; changelog is the version reference |
| 28 | Geist (Vercel) | https://vercel.com/geist/introduction | A | 200 | not shown | Not mentioned | USE |
| 29 | Twilio Paste, old domain | https://paste.twilio.design/ | A | 200 -> github.com:443/twilio-labs/paste | not shown | Not mentioned | MOVED: redirects to github.com/twilio-labs/paste; repo homepage is paste-dsys.com |
| 30 | Twilio Paste, current | https://paste-dsys.com/ | A | 200 | not shown | Not mentioned | USE (HTTP 200 today); repo not archived, pushed 5 Sep 2026 |
| 31 | Gestalt (Pinterest) | https://gestalt.pinterest.systems/ | A | 200 | updated 2026-02-25 | Not mentioned | USE; updated 25 Feb 2026 |
| 32 | Blade (Razorpay) | https://blade.razorpay.com/ | A | 200 | Last-Modified 22 Sep 2026 | Not mentioned | USE; served as a Storybook; Last-Modified 22 Sep 2026 |
| 33 | Encore (Spotify) | https://spotify.design/article/reimagining-design-systems-at-spotify | B | 404 -> open.spotify.com/article/reimagining-design-systems-at-spotify Not Found | not shown | Not mentioned | NO PUBLIC DOCS: guessed article URL 404s. Use only talks/articles as a case study |
| 34 | Workday Canvas | https://canvas.workday.com/ | A | 200 | not shown | Not mentioned | USE |
| 35 | Elastic UI (EUI) | https://eui.elastic.co/ | A | 200 | Last-Modified 21 Sep 2026 | Not mentioned | USE; Last-Modified 21 Sep 2026 |
| 36 | PatternFly (Red Hat) | https://www.patternfly.org/ | A | 200 | Last-Modified 17 Sep 2026 | Not mentioned | USE; Last-Modified 17 Sep 2026 |
| 37 | SAP Fiori | https://experience.sap.com/fiori-design-web/ | A | 403 -> www.sap.com/design-system/fiori-design-web/ Forbidden | not shown | Not mentioned | MOVED: redirects to sap.com/design-system/fiori-design-web/ (blocks bots with 403; open in a browser) |
| 38 | Wise Design | https://wise.design/ | A | 200 | Last-Modified 15 Jul 2026 | Not mentioned | USE; Last-Modified 15 Jul 2026 |
| 39 | Porsche Design System | https://designsystem.porsche.com/ | A | 200 -> designsystem.porsche.com/v4/ | Last-Modified 09 Sep 2026 | Not mentioned | USE; redirects to /v4/ |
| 40 | NYPL Reservoir v4 | https://nypl.github.io/nypl-design-system/reservoir/v4/ | A | 200 | Last-Modified 19 Aug 2026 | Mentioned (HN, Aug 2026) | USE as a public-sector example |
| 41 | Chakra UI | https://chakra-ui.com/ | A | 200 | not shown | Not mentioned | USE (optional, OSS library) |
| 42 | Figma Simple Design System (community file) | https://www.figma.com/community/file/1380235722331273046/simple-design-system | A | 200 | updated 2026-08-13 | Not mentioned | USE for Figma variables/components reference; updated 13 Aug 2026 |

## Figma documentation

| # | Source | URL | Tier | Live check 2026-09-23 | Last-updated shown | last30days signal | Verdict |
|---|---|---|---|---|---|---|---|
| 43 | Figma Help: variables overview | https://help.figma.com/hc/en-us/articles/14506821864087-Overview-of-variables-collections-and-modes | A | 200 | not shown | Strong (variables/modes are what people learn first) | USE |
| 44 | Figma Help: guide to variables | https://help.figma.com/hc/en-us/articles/15339657135383-Guide-to-variables-in-Figma | A | 200 | not shown | Strong | USE |
| 45 | Figma Help: extend a variable collection | https://help.figma.com/hc/en-us/articles/36346281624471-Extend-a-variable-collection | A | 200 | not shown | Indirect (white-label/multi-brand threads) | USE |
| 46 | Figma Help: slots fundamentals | https://help.figma.com/hc/en-us/articles/39745565646871-Components-collection-Slots-fundamentals | A | 200 | not shown | Not mentioned | USE; confirm beta status on page |
| 47 | Figma Help: guide to the MCP server | https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Figma-MCP-server | A | 200 | not shown | Strong positive (Claude + Figma MCP works) | USE; write-to-canvas free beta, later usage-based paid |
| 48 | Figma Help: what's new from Config 2026 | https://help.figma.com/hc/en-us/articles/39582753756695-What-s-new-from-Config-2026 | A | 200 | not shown | Mentioned (shaders, code layers) | USE for beta/GA labels |
| 49 | Figma developer docs: MCP server | https://developers.figma.com/docs/figma-mcp-server/ | A | 200 | Last-Modified 22 Sep 2026 | Strong | USE as the only source for MCP tool names |
| 50 | Figma developer docs: Code Connect | https://developers.figma.com/docs/code-connect/ | A | 200 | Last-Modified 22 Sep 2026 | Mentioned | USE |
| 51 | Figma REST API: variables | https://developers.figma.com/docs/rest-api/variables/ | A | 200 | Last-Modified 22 Sep 2026 | Indirect | USE (Enterprise-only endpoints; verify plan limits) |
| 52 | Figma blog: Config 2026 recap | https://www.figma.com/blog/config-2026-recap/ | B | 200 | Published 2026-06-24 | Mentioned | USE with Help Center for status labels |
| 53 | Figma blog: design context everywhere you build | https://www.figma.com/blog/design-context-everywhere-you-build/ | B | 200 | Published 2025-09-23 | Indirect | USE as history; published 23 Sep 2025 |

## Standards and specifications

| # | Source | URL | Tier | Live check 2026-09-23 | Last-updated shown | last30days signal | Verdict |
|---|---|---|---|---|---|---|---|
| 54 | W3C DTCG Format Module 2025.10 | https://www.designtokens.org/tr/2025.10/format/ | A | 200 | not shown | GitHub repo 2.1K stars; little chatter | USE (stable) |
| 55 | W3C DTCG Color Module 2025.10 | https://www.designtokens.org/tr/2025.10/color/ | A | 200 | not shown | n/a | USE (stable) |
| 56 | W3C DTCG Resolver Module 2025.10 | https://www.designtokens.org/tr/2025.10/resolver/ | A | 200 | updated 2025-11-01 | n/a | USE (theming/sets); updated 1 Nov 2025 |
| 57 | W3C Design Tokens Community Group | https://www.w3.org/community/design-tokens/ | A | 200 | not shown | n/a | USE |
| 58 | WCAG 2.2 | https://www.w3.org/TR/WCAG22/ | A | 200 | Last-Modified 12 Dec 2024 | Indirect | USE (current Recommendation) |
| 59 | Understanding WCAG 2.2 | https://www.w3.org/WAI/WCAG22/Understanding/ | A | 200 | Updated 11 February 2026; Last-Modified 02 Jul 2026 | n/a | USE; updated 11 Feb 2026 |
| 60 | WCAG 3.0 (Working Draft) | https://www.w3.org/TR/wcag-3.0/ | A | 200 | Last-Modified 10 Sep 2026 | Not mentioned | USE AS DRAFT ONLY (WD 10 Sep 2026); no APCA named |
| 61 | WAI-ARIA Authoring Practices Guide | https://www.w3.org/WAI/ARIA/apg/ | A | 200 | Last-Modified 22 Sep 2026 | Not mentioned | USE; Last-Modified 22 Sep 2026 |
| 62 | WAI-ARIA 1.2 | https://www.w3.org/TR/wai-aria-1.2/ | A | 200 | Published 2023-06-06; Last-Modified 01 Jun 2023 | n/a | USE (Recommendation, 6 Jun 2023); 1.3 is a Working Draft (4 Jun 2026) |
| 63 | CSS Color Module Level 4 | https://www.w3.org/TR/css-color-4/ | A | 200 | Last-Modified 13 Sep 2026 | n/a | USE (OKLCH, P3) |
| 64 | APCA repo/docs | https://git.apcacontrast.com/ | B | 200 | Last-Modified 25 Jul 2026 | Not mentioned | USE as a perceptual contrast tool, not a compliance standard; updated Jul 2026 |
| 65 | APCA calculator | https://apcacontrast.com/ | B | 200 | Revised May 27, 2022; Last-Modified 24 May 2026 | Not mentioned | USE with care; page says 'Revised May 27, 2022' |
| 66 | Myndex APCA page | https://www.myndex.com/APCA/ | C | ERR <urlopen error [Errno 51] Network is unreachable> | not shown | Not mentioned | UNREACHABLE today (network error); use git.apcacontrast.com |
| 67 | Google Sign-In branding guidelines | https://developers.google.com/identity/branding-guidelines | A | 200 | Last updated 2026-07-07; Last-Modified 07 Jul 2026 | Mentioned indirectly (official-logo rule) | USE for third-party brand-mark constraints |

## Token, documentation and tooling sources

| # | Source | URL | Tier | Live check 2026-09-23 | Last-updated shown | last30days signal | Verdict |
|---|---|---|---|---|---|---|---|
| 68 | Style Dictionary | https://styledictionary.com/ | A | 200 | not shown | Mentioned (tokens pipeline) | USE; current major is v5 (5.5.5, 20 Sep 2026) |
| 69 | Tokens Studio docs | https://docs.tokens.studio/ | A | 200 | Last-Modified 15 May 2026 | Positive (recommended for serious token workflows; top plugin in zeroheight 2026) | USE; plugin 2.12.1 (23 Sep 2026) |
| 70 | Terrazzo | https://terrazzo.app/ | A | 200 | not shown | Not mentioned | USE (DTCG reference implementation) |
| 71 | Storybook docs | https://storybook.js.org/docs | A | 200 | not shown | Positive ('replaced everything except Storybook') | USE; 10.6.0 stable, 11.0 alpha |
| 72 | Storybook 10.3 (MCP) | https://storybook.js.org/blog/storybook-10-3/ | A | 200 | Published 2026-04-06 | Mentioned | USE; published 6 Apr 2026 |
| 73 | zeroheight | https://zeroheight.com/ | B | 200 | not shown | Neutral (one claim that Claude Code replaced it) | USE as vendor; now markets MCP for agents |
| 74 | Supernova | https://www.supernova.io/ | B | 200 | not shown | Not mentioned | USE as vendor |
| 75 | Knapsack | https://www.knapsack.cloud/ | B | 200 | Last-Modified 20 Sep 2026 | Not mentioned | USE as vendor |
| 76 | Google Stitch DESIGN.md announcement | https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-design-md/ | A | 200 | Published 2026-04-21 | Indirect (agent-facing DS files) | USE; it is a DRAFT spec (21 Apr 2026) |
| 77 | Leonardo (Adobe color tool) | https://leonardocolor.io/ | B | 200 | Last-Modified 08 Jul 2026 | Not mentioned | USE for contrast-based ramps |
| 78 | Tailwind CSS theme variables | https://tailwindcss.com/docs/theme | A | 200 | not shown | Indirect (shadcn lint targets Tailwind v4) | USE |
| 79 | Utopia (fluid type/space) | https://utopia.fyi/ | B | 200 | not shown | Not mentioned | USE |
| 80 | Sanity: design-system evals | https://www.sanity.io/engineering/design-system-evals | B | 200 | Published 2026-08-26 | Mentioned (HN) | USE; strong evidence on agent-readiness (26 Aug 2026) |

## Practitioners, surveys and indexes

| # | Source | URL | Tier | Live check 2026-09-23 | Last-updated shown | last30days signal | Verdict |
|---|---|---|---|---|---|---|---|
| 81 | EightShapes (Nathan Curtis), site | https://eightshapes.com/ | B | ERR <urlopen error [Errno 8] nodename nor servname provided, or not known> | not shown | Not mentioned | UNREACHABLE today (DNS/connect failure). Use the Medium publication in a browser |
| 82 | EightShapes on Medium | https://medium.com/eightshapes-llc | B | 403 Forbidden | not shown | Not mentioned | USE (Medium returns 403 to scripts; open in a browser) |
| 83 | Brad Frost blog | https://bradfrost.com/blog/ | B | 200 | not shown | Not mentioned | USE |
| 84 | Atomic Design (book, free online) | https://atomicdesign.bradfrost.com/ | B | 200 | not shown | Not mentioned | USE as foundational history |
| 85 | Dan Mall | https://danmall.com/ | B | 200 | Last-Modified 22 Sep 2026 | Not mentioned | USE; site now focused on designer careers |
| 86 | Design System University (Dan Mall) | https://designsystem.university/ | B | 200 | Last-Modified 07 Sep 2026 | Not mentioned | USE |
| 87 | NN/g: Design Systems 101 | https://www.nngroup.com/articles/design-systems-101/ | B | 200 | Published 2021-04-11; Last-Modified 27 Aug 2026 | Positive (definition quoted in r/DesignSystems) | USE; published 11 Apr 2021, so pair with newer sources. Separate NN/g from Jakob Nielsen's personal opinions (disputed) |
| 88 | Smashing Magazine: design systems | https://www.smashingmagazine.com/category/design-systems/ | B | 200 | Updated 2026-07-15 | Not mentioned | USE; updated 15 Jul 2026 |
| 89 | zeroheight Design Systems Report 2026 | https://report.zeroheight.com/ | B | 200 | Last-Modified 22 Sep 2026 | Cited in web results | USE (vendor survey; mostly large Western companies) |
| 90 | Sparkbox Design Systems Survey | https://designsystemssurvey.seesparkbox.com/ | B | 200 -> designsystemssurvey.seesparkbox.com/2022/ | not shown | Not mentioned | STALE: latest edition 2022; history only |
| 91 | Design Systems Collective | https://www.designsystemscollective.com/ | C | 403 Forbidden | not shown | Not mentioned | OPINION ONLY; site blocks bots (403) |
| 92 | Into Design Systems | https://www.intodesignsystems.com/ | C | 200 | not shown | Not mentioned | OPINION ONLY; now an 'AI Design Systems Conference 2027' site |
| 93 | Clarity conference (Jina Anne) | https://www.clarityconf.com/ | B | 200 | Last-Modified 18 Aug 2026 | Not mentioned | USE for talks |
| 94 | Big Medium (Josh Clark) | https://bigmedium.com/ | B | 200 | Last-Modified 17 Sep 2026 | Not mentioned | USE for AI + design systems essays |
| 95 | The Design System Guide (Romina Kavcic) | https://thedesignsystem.guide/ | C | 200 | Last-Modified 19 Mar 2026 | Not mentioned | OPINION ONLY (paid guide) |
| 96 | The Component Gallery | https://component.gallery/ | B | 200 | not shown | Not mentioned | USE for cross-system component naming |
| 97 | Adele (UXPin) repository | https://adele.uxpin.com/ | C | 200 | not shown | Not mentioned | USE as an index only; check freshness per entry |
| 98 | Design Systems Repo | https://designsystemsrepo.com/ | C | 200 | not shown | Not mentioned | USE as an index only |
| 99 | MacRumors: Liquid Glass in iOS 27 | https://www.macrumors.com/2026/06/10/how-liquid-glass-is-changing-in-ios-27/ | B | 200 | Published 2026-06-10 | Consistent with community | USE as press corroboration; published 10 Jun 2026 |
| 100 | designsystems.surf 'best examples 2026' | https://designsystems.surf/articles/11-best-design-system-examples-in-2026 | C | 200 | Last-Modified 23 Sep 2026 | Not mentioned | REJECT (listicle) |

## Version facts checked via the GitHub API today (for lanes that cite tool versions)
| Tool | Latest release | Date | Stars |
|---|---|---|---|
| Style Dictionary | v5.5.5 | 2026-09-20 | 4.8K |
| Tokens Studio Figma plugin | 2.12.1 | 2026-09-23 | 1.6K |
| Terrazzo | plugins 2.5.0 | 2026-07-26 | 460 |
| Storybook | v10.6.0 stable; v11.0.0-alpha.1 | 2026-09-02; 2026-09-19 | 91.1K |
| shadcn CLI | 4.21.0 | 2026-09-04 | 124K |
| Material Web | v2.5.0 | 2026-07-15 | n/a |
| Compose Material3 (Android Developers release notes, not GitHub) | stable 1.4.0; alpha 1.5.0-alpha28 | 2025-09-24; 2026-09-09 | n/a |
| figma/code-connect | n/a | pushed 2026-09 | 1.6K |
| design-tokens/community-group (DTCG) | n/a (spec 2025.10) | pushed 2026-09-08 | 2.1K |

## Gaps in this registry
- It does not yet list platform-specific references (Android Views/MDC, SwiftUI API docs, Flutter material package docs), content-design sources (Mailchimp style guide, GOV.UK content style), or dataviz systems (Carbon Charts, IBM dataviz guidance, Datawrapper). L05, L06 and L10 should add those to their own traces.
- The "last-updated" column is empty for many JavaScript-rendered sites. Lanes should record the in-page change log (Apple HIG, Material, Fluent) when they read those pages in a browser.
- There is no per-page freshness check below the home page for most systems; a system's home page being live says nothing about individual component pages.
