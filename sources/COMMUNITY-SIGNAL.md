# Community signal (lane L00, source validation)

Written 2026-09-23 by L00. Window: 2026-08-24 to 2026-09-23 for the last30days runs, plus web checks of the sources people cite.
Raw engine output lives in `sources/last30days-raw/` (`<slug>.md` is the full saved raw file, `<slug>.compact.md` is the engine's compact report). Every source opened is logged in `traces/L00-trace.md`.

**How to read this file.** "Community" evidence is Tier C by definition (Reddit, HN, YouTube). I use it to spot what practitioners argue about, which sources they cite, and what changed recently. A claim becomes "confirmed" here only when a Tier A or B source (checked live today) backs it.

**Coverage caveats.** X/Twitter was not available (no auth, and the lane ran without browser cookies by instruction). TikTok and Instagram were not available (no ScrapeCreators key). Perplexity was not available (quota exhausted, HTTP 401). Reddit, Hacker News, YouTube and GitHub worked after fixing a Python SSL certificate problem on the first run. Design practitioners are very active on X and LinkedIn, so this pulse under-represents them; treat "no signal" below as "no signal on Reddit/HN/YouTube", not "nobody is talking about it".

---

## a. Design systems, general practitioner pulse

**Engine result:** 52 items (Reddit 25, HN 18, YouTube 3, GitHub 6). Much of the HN set is keyword noise about "system design" interviews and chip design; ignore it.

**What practitioners say now**
- **AI is the only topic.** Nearly every r/DesignSystems thread this month is about AI agents: "Are design systems becoming more important or less with AI?", "How are you making your design system more agentic and AI-friendly" (31 comments), "Reproducing company design system for agentic use". [S-L00-034]
- **"Code is the source of truth" is now the majority view.** In r/UXDesign's "Those with a Figma design system who don't touch Figma anymore" thread, the top reply (76 upvotes) says "A component library in Figma is not a design system. If you want to use AI tools reliably, a design system in code helps." Another reply describes the working pattern: code becomes the source of truth for components and Figma stops mirroring them. The r/DesignSystems thread "What does your design-system source of truth look like in 2026?" (32 points) lands in the same place: "Design tools are not the source of truth... Code is the source of truth." [S-L00-034, S-L00-040]
- **Pushback on "agentic design system" as a buzzword.** In "Reproducing company design system for agentic use", commenters say a design system already is documentation for how to use things, "person or agent", and that "agentic design system... really doesn't mean anything". Useful counterweight for L11. [S-L00-040]
- **AI-readability is becoming a requirement.** An enterprise DevOps design lead (r/UXDesign, 73 points) reports that agents reinvented existing components and hardcoded values until they rewrote the system's docs for machines. This matches Sanity's published evals (below). [S-L00-034, S-L00-036]
- **Job anxiety is real and loud.** "Replaced by AI today. They had me build the design system they're using to replace me" (r/UXDesign, 471 points, 125 comments) was the highest-engagement design-system post of the month. Replies say the work is still what people hire for, and one designer says their company wants them back "bc Claude is not a good designer". [S-L00-034]
- **Marketing site vs product system drift** and **change logging for large systems** are recurring governance questions. [S-L00-034]

**Sources practitioners cite or trust**
- **Sanity engineering, "How well do agents use your design system?"** by PJ Onori, 26 Aug 2026. Open-source eval harness. Rewriting Sanity UI docs raised agent build success from 20% to 90% (Sonnet) and 40% to 100% (Opus). JSON-structured docs beat Markdown. With docs, code chunks and lints, accessibility violations per iteration fell from 5.1 to 0.6 (Sonnet 4.6, n=30). The author notes it is "not a win across the board": inline styles went up with chunks. Tier B, strong. [S-L00-036]
- **zeroheight Design Systems Report 2026** (read in full, see topic h): 56% of teams use AI with their design system (10% built into processes plus 46% experimenting), and 28% say AI lives up to its potential highly or very highly. Adoption is the top challenge for the fifth year running. The widely shared "only 15% say it lives up to the hype" line comes from a zeroheight LinkedIn post and probably from their separate State of AI report; do not attribute it to the main report. Tier B, vendor survey. [S-L00-056, S-L00-039]
- **NN/g's definition** of a design system gets quoted approvingly in r/DesignSystems. But **Jakob Nielsen personally is a disputed voice right now**: a 119-point r/UXDesign thread criticizes him harshly for AI-replaces-designers commentary. Treat NN/g articles as Tier B. Treat Nielsen's personal Substack (UX Tigers) as opinion. [S-L00-034]
- UI Collective (YouTube, 36k and 42k views): popular tutorials on Figma variables, tokens (100-scale naming) and AI workflows. Tier C, run by a consultancy that sells "AI-ready design system" services. [S-L00-007]

**New since 2025 that other lanes must not miss**
- Agent-facing design system artifacts: **Google Stitch's DESIGN.md** (open-sourced 21 Apr 2026) [S-L00-029], **Storybook MCP** (Storybook 10.3 added MCP for React; 10.6.0 is the current stable, released 2 Sep 2026; 11.0 is in alpha) [S-L00-037, S-L00-041], **shadcn registry + MCP** [S-L00-032, S-L00-033], **Figma MCP server + Code Connect** [S-L00-025, S-L00-026], and design-system **evals** [S-L00-036].
- New open-source systems people are posting: NYPL Reservoir v4, McKinsey QuantumBlack Design System, and a "Design System Atlas" that maps 119 public systems. [S-L00-034]

**Sources to avoid for this topic**
- "Best design system examples 2026" listicles (for example designsystems.surf) and AI-farm explainers. [S-L00-005]

---

## b. Design tokens, DTCG, Style Dictionary, Tokens Studio

**Engine result:** 28 items (Reddit 12, HN 13, YouTube 1, GitHub 2). Community chatter specific to tokens is thin; most token discussion is folded into the AI and source-of-truth threads.

**What practitioners say now**
- Tokens are framed as "design decisions turned into code". The consensus is that tokens and components in code are the source of truth, and Figma variables mirror them. [S-L00-040]
- One tooling recommendation in r/DesignSystems ("Design system tools", 17 comments): "get comfortable with Figma Variables/modes first. Then... Tokens Studio for more serious token workflows." The same thread has a claim that "Claude Code replaced every ds management tool I've needed... with the exception of storybook." Opinion only. [S-L00-040]
- Multi-brand and white-label setups built with Figma variables and modes are a live question (50+ white-label clients thread). [S-L00-040]

**Confirmed facts (Tier A, checked today)**
- **DTCG Format 2025.10 is the first stable spec** (announced 28 Oct 2025). It covers theming and multi-brand, modern color (Display P3, OKLCH, CSS Color 4), and aliases/inheritance. The W3C announcement names Style Dictionary, Tokens Studio and Terrazzo as implementers, and Penpot, Figma, Sketch, Framer, Knapsack, Supernova and zeroheight as supporting or implementing it. [S-L00-008, S-L00-009]
- **Style Dictionary is on v5** (v5.5.5 released 20 Sep 2026; 4.8K stars; 236 open issues). The GitHub README banner still points at "What's new in 4.0", so do not treat the README as the version reference. [S-L00-042]
- **Tokens Studio Figma plugin** 2.12.1 (23 Sep 2026). **Terrazzo** plugins 2.5.0 (26 Jul 2026). The **DTCG repo** has 2.1K stars and 91 open issues (last push 8 Sep 2026). [S-L00-042]

**Disputed or stale**
- Any article that describes DTCG as a "draft" or "editor's draft" is stale after Oct 2025.
- Any "Style Dictionary v4" guide is one major version behind. Check it against styledictionary.com before using its APIs.
- The "Figma supports DTCG" claim needs care. The W3C post says Figma is "supporting or implementing" the standard. Check help.figma.com for what Figma actually imports and exports natively before a lane states it as fact (L07 owns this).

---

## c. Figma variables, Figma design system features, Figma MCP and Code Connect

**Engine result:** 36 items (Reddit 27, YouTube 6, HN 2, GitHub 1). Strongest community signal of all eight topics.

**What practitioners say now**
- **Figma MCP plus Claude is how people build systems now, with shadcn as the scaffold.** In r/FigmaDesign's "Has anyone successfully built a design system using Figma AI / Agents?" (38 points, 34 comments), the top reply (28 upvotes) says "using shadcn as a reference was the best thing I did". It adds that agents "don't reliably find the components", so the author made the system "more AI readable" with a thesaurus of component names. Another reply: "Creating one through claude and the FIGMA MCP has been pretty successful for me." [S-L00-043]
- **Handoff is being rethought.** Replies to "How are design teams handling Figma handoff when AI writes the code?" argue that designers should own a repo of components and tokens, and that prototypes become the handoff file. [S-L00-043]
- **Figma Make is judged weak.** "Figma Make, I just don't understand what it does at this point?" (71 points): top reply (57 upvotes) "Ideation and concepts. Nothing actually usable." [S-L00-043]
- **Mixed feelings about code layers.** In "I love figma but..." (108 points) one designer writes "I don't want code layers. I want to design things." [S-L00-043]
- **Variables, text styles, components and auto layout** are still what people tell newcomers to learn first ("Print designer moving to Figma", top reply 32 upvotes). The "three-tier token architecture (brand, alias, mapped collections)" pattern from UI Collective's videos is widely copied (24.7k views). [S-L00-043]

**Confirmed facts (Tier A, checked today)**
- **Figma MCP server.** The remote server lives at `https://mcp.figma.com/mcp` and is available "on all seats and plans"; the desktop server needs a Dev or Full seat on a paid plan. It reads variables, components, layout data, FigJam and Make resources. **Write-to-canvas** (agents create frames, components, variables and auto layout) is a **free beta** that "will eventually be a usage-based paid feature". Code-to-canvas is also in beta with select clients. [S-L00-044]
- GitHub Copilot and VS Code can send rendered UI back into Figma as editable layers through the MCP server (GitHub changelog, 6 Mar 2026). [S-L00-026]
- **figma/code-connect** repo: 1.6K stars, 201 open issues. [S-L00-043]
- **Extended collections** (a multi-brand parent collection with per-brand overrides that inherit updates) and **slots** (a component property for free content areas inside instances) are documented on help.figma.com. Slots were labelled "beta, gradually rolling out" in the snippet I saw; L07 should confirm the current status on the page. [S-L00-045]
- **Config 2026 (24 June 2026)** did not headline design-system features; see topic g. [S-L00-012, S-L00-013]

**Disputed or stale**
- "The Figma MCP server has N tools" counts from third-party blogs (for example "14 tools as of Feb 2026") go stale fast. Use developers.figma.com/docs/figma-mcp-server as the only source for tool names. [S-L00-027]
- Figma's own 2024 videos ("Syncing variables to code" via the Enterprise Variables REST API + Style Dictionary, and the Config 2024 Code Connect talk) are still widely viewed, but they predate MCP. Use them as history only. [S-L00-043]
- A forum report says `generate_figma_design` was missing from the Claude Code connector. Treat MCP write features as client-dependent. [S-L00-028]

---

## d. Material 3 Expressive

**Engine result:** 44 items, but most HN and GitHub hits are keyword noise ("material", "3"). Real community signal is small: indie Android apps adopting M3 Expressive, Home Assistant cards, a Swift port, and Flutter adaptive packages.

**What practitioners say now**
- Developers see M3 Expressive as **Android/Compose-first**. A beginner in r/HowToMen notes that web, Flutter and React Native "none of them support m3 expressive". [S-L00-046]
- There is **cross-platform style mixing**: "Expressive Glass" (a Compose library that mixes the Material Expressive look with Liquid Glass-style physics) and a Flutter demo that renders Liquid Glass on iOS and M3 Expressive on Android from one codebase (r/FlutterDev, 33 points). The top reply there was "ai;dr" (68 upvotes), so these posts are also read as AI-generated promotion. [S-L00-046]
- iOS developers push back on porting it: "iOS users don't want the Barney buttons with drop shadows from the 90s" (r/swift, 24 upvotes). [S-L00-046]
- Users debate whether M3E is "Pixel UI" rather than stock Android. [S-L00-046]

**Confirmed facts (Tier A, checked today)**
- **Jetpack Compose Material3: latest stable is 1.4.0 (released 24 Sep 2025). Latest alpha is 1.5.0-alpha28 (9 Sep 2026).** (Superseded by 1.5.0-alpha29 on 23 Sep 2026 [S-V1b-035].) Expressive APIs are being "graduated" to non-experimental in the **1.5.0 alphas**: motion scheme, FAB and FAB menu, buttons, split button, floating toolbar, flexible top and bottom app bars, and search bars. Google also **reverted** the promotion of MaterialShapes and LoadingIndicator. So as of today, **no stable Compose release ships the full M3 Expressive API without opt-ins.** [S-L00-047]
- For Wear OS, M3 Expressive ships in the separate Wear Compose Material 3 library (per the same release page). [S-L00-047]
- Material Web v2.5.0 (15 Jul 2026). [S-L00-042]
- Google Design's "Introducing: Material 3 Expressive" video dates from 13 May 2025. [S-L00-046]

**Disputed or stale**
- **Disputed:** web snippets claiming "Jetpack Compose now fully supports Material 3 Expressive... without experimental annotations". That is only true in the 1.5.0 alphas, not in a stable release. [S-L00-022, S-L00-047]
- **Unverified:** I/O 2026 claims ("14 expressive components", "Styles API", "Expressive layout system", "Material Android Compose-first") came from a search snippet of m3.material.io/blog/whats-new-at-io26. The page is JavaScript-rendered and I could not read it. L04 and L10 should confirm them before use.
- **WebFetch warning:** the fetch tool's summary said Compose Material3 1.4.0 was released "September 09, 2026". The raw page says 24 Sep 2025. Check dates against raw pages, not tool summaries. [S-L00-047]

---

## e. Apple Liquid Glass (iOS 26 to iOS 27)

**Engine result:** 51 items (Reddit 25, YouTube 10, HN 3, GitHub 13). iOS 27 shipped during the window, so this pulse is dominated by "iOS 27 is out" reactions.

**What practitioners and users say now**
- **The readability backlash was real, and Apple responded twice.** iOS 26.1 (beta 4, Oct 2025) added a Clear/Tinted choice after complaints [S-L00-019]. At WWDC 2026 Apple announced for iOS 27 a transparency slider (from clear to fully tinted), better diffusion of busy content behind glass, a darkened edge with brighter specular highlights, and a uniform toolbar when content scrolls under floating bars [S-L00-018]. iOS 27 was released around 14 Sep 2026 (HN: "Apple Releases iOS 27 and iPadOS 27 with Siri AI and Liquid Glass Update"). [S-L00-048]
- **Now the opposite complaint exists too.** "Did Apple tone down Liquid Glass too much in iOS 27 compared to iOS 26?" (r/iOS27, 43 points, 60 comments), while others say "Some things still felt off in iOS 26, but Apple finally" fixed them. [S-L00-048]
- **Performance.** Users report that the phone "feels more fluid on iOS 27 when Reduce Transparency is turned on", and that iPadOS 27 lags on an M1 iPad Pro with Liquid Glass app icons. Opinion only, but a useful signal that heavy glass has costs. [S-L00-048]
- **Developers are tokenizing glass on the web.** GitHub PRs add "Liquid Glass tokens in :root" with reduced-motion and focus-visible handling. [S-L00-048]

**Confirmed facts (Tier A, Apple HIG > Materials, read via Apple's docs JSON today)**
- Apple platforms have two material types: **Liquid Glass** (a functional layer for controls and navigation that floats above content) and **standard materials** (for differentiation within the content layer).
- "Don't use Liquid Glass in the content layer", with the exception of transient states of controls such as sliders and toggles while they are active. "Use Liquid Glass effects sparingly."
- Two variants. **Regular** blurs and adjusts luminosity for legibility; most system components use it. **Clear** is highly translucent and meant only for components over visually rich media. Appearance changes with the user's preferred Liquid Glass look and with Reduce Transparency and Increase Contrast. [S-L00-049]

**Disputed or stale**
- Any iOS 26-era article that treats Liquid Glass as a fixed look is stale. The material now has a user-controlled transparency range, so designs must hold up from fully clear to fully tinted, and with Reduce Transparency on.
- The HIG page did not show a change-log date in the JSON. L10 should record the HIG change log from the live page.
- There are many AI-farm "iOS 27 vs iOS 26" explainer sites (for example andrew.ooo, asumetech). Avoid them. [S-L00-021]

---

## f. shadcn/ui and AI-era design systems (agents, MCP, vibe coding)

**Engine result:** 44 items (Reddit 25, HN 17, YouTube 1, GitHub 1) on the second run. The first run was discarded because the engine read "shadcn/ui" as a comparison ("shadcn vs ui"). The bad output is kept in `sources/last30days-raw/_superseded/`.

**What practitioners say now**
- **shadcn is treated as the default scaffold for AI-built UI, and the fight now is about enforcement.** The most-watched item was Better Stack's "Shadcn Just Fixed Tailwind's Biggest Problem" (65k views, 21 Sep 2026) about **shadcn lint**. It is an Oxlint/ESLint plugin for any Tailwind v4 project that flags off-system styles AI tends to add, such as a raw `bg-pink-500` on a themed component or an arbitrary 13px padding. The video's own caveat is worth keeping: "is your component API actually strict enough to enforce against?" This Week In React #297 also lists "shadcn lint". The shadcn changelog page did not mention it when I checked it today, so treat the launch details as community-reported until the official docs show them. [S-L00-050, S-L00-051]
- **"AI slop" sameness is a live complaint.** Threads include "AI-generated frontends all look the same. I built a tool to fix that", "Week 1 of building a UI library that tries to fix AI slop" (26 points) and "Don't want your app to look like AI slop? Stop showing your users raw errors" (15 points). The builder should treat distinctiveness (brand layer on top of a shadcn-like base) as a first-class goal. [S-L00-050]
- **Drift prevention beats "AI features".** In r/DesignSystems' "more agentic" thread, the top reply (18 upvotes) says the biggest unlock "wasn't anything AI-specific. It was making drift impossible." [S-L00-050]
- **MCP servers are an attack surface.** "Notion's Official MCP connector prompt injects AI agents to advertise products mid-task" had 2,269 points and 156 comments. Any design-system MCP server the builder ships or consumes must be treated as untrusted input to agents. This is a governance point for L11. [S-L00-050]

**Confirmed facts (Tier A, checked today)**
- **shadcn/ui changelog** (read live): CLI 3.0 and the MCP server (Aug 2025), `npx shadcn create` (Dec 2025), shadcn/cli v4 (Mar 2026), new themes Luma, Sera and Rhea (Mar to May 2026), registry include + validate (May 2026), GitHub registries (Jun 2026), private GitHub registries (Aug 2026), **"Base UI as the Default"** (Jul 2026), React Aria support (Jul 2026), shadcn/typeset (Jul 2026), and `cn` imported from a `cn` package (Sep 2026). I confirmed "Base UI as the Default", "shadcn/cli v4", "Introducing Rhea", "React Aria" and "shadcn/typeset" as literal strings on the page with curl. [S-L00-051]
- The shadcn MCP server works with any shadcn-compatible registry. shadcn/ui repo: 124K stars, 1,836 open issues, CLI 4.21.0 (4 Sep 2026). [S-L00-033, S-L00-042]
- **DESIGN.md** (Google Labs, Stitch): on 21 Apr 2026 Google open-sourced the **draft specification** so agents "can know exactly what a color is for, and can validate their choices against WCAG accessibility rules". It is a draft, not a standard. [S-L00-052]
- **Storybook MCP**: Storybook 10.3 (6 Apr 2026) added MCP for React; current stable is 10.6.0. [S-L00-037, S-L00-041]
- **zeroheight** now markets itself as a platform "for Teams and AI Agents" and ships a zeroheight MCP (vendor claim). [S-L00-053]

**Disputed or stale**
- Specific claims about what DESIGN.md contains (for example "extracts five types of design tokens") come from AI-farm explainers, not the Google post. Read the spec on GitHub before relying on its schema. [S-L00-031]
- Any shadcn guide that assumes Radix is the only primitive layer is stale. Base UI became the default in Jul 2026, and React Aria is also supported.

---

## g. Figma Config 2026

**Engine result:** 31 items (Reddit 16, YouTube 5, HN 8, GitHub 2). Config was on 24 Jun 2026, three months before this window, so the pulse shows how people are *using* the launches rather than reacting to them.

**Solid facts (Tier A)**
- Config 2026 was on **24 Jun 2026**. Keynote by Dylan Field (Figma YouTube, 208k views). [S-L00-054]
- **Open beta:** Figma Motion (timeline and keyframe animation, exportable as CSS, JSON, React, MP4, WebM, SVG and GIF), custom shader effects and fills (WebGPU, built by prompting the agent), Weave tools inside Figma Design, Figma agent updates for all paid plans, and generative plugins. **Closed beta or coming soon:** code layers, the agent in FigJam and Slides, and 3D transforms. [S-L00-012, S-L00-013, S-L00-016]
- **Config 2026 announced nothing headline-level for design systems** (variables, libraries, Dev Mode, Code Connect, MCP, slots). Figma's design-system features in this period came from Schema 2025 (extended collections, slots) and from separate MCP/Code Connect releases. [S-L00-013, S-L00-016, S-L00-045]

**What people are doing with it**
- Shader fills are the most visible uptake: "Just made a crochet filter shader for Figma" (130 points). Another poster found that the useful part of an agent-built particle shader "was the parameter it did not think to offer". [S-L00-054]
- A designer's manager says "all this AI will be more workable once we have code layers", and the designer answers "I don't want code layers." [S-L00-043]
- Framer released AI agents the week before Config (per a creator recap). [S-L00-054]

**Disputed or stale**
- Medium and agency "10 biggest announcements" recaps sometimes call Figma Motion "generally available". The Help Center and forum both say **open beta**. [S-L00-013, S-L00-014]
- The r/FigmaDesign post "Figma Buys AI Company!" (21 Sep 2026) has no body in the dump. I could not identify the acquisition because my web-search budget ran out. Treat it as unverified.

---

## h. Design system documentation and governance (zeroheight, Storybook, Supernova)

**Engine result:** 50 items (Reddit 25, HN 18, YouTube 6, GitHub 1). Documentation tools themselves are barely discussed on Reddit and HN this month; the governance discussion is folded into the AI and source-of-truth debate (see topic a).

**What practitioners say now**
- "Are design systems becoming more important or less with AI?": top reply "Definitely more, and incredibly so" (35 upvotes). Next: "Look at the inconsistent mess that is your company's internal tools... That's what happens when you don't have a design system" (19). [S-L00-055]
- New thread titles show the shift: "Design Systems 2.0: The source of truth is the code" and "At what point does a UI kit stop being enough and you actually need a design system?" [S-L00-055]
- In the "Design system tools" thread (17 comments) one person claims Claude Code replaced zeroheight-style tools but not Storybook. Opinion only. [S-L00-040]

**The one strong quantitative source: zeroheight Design Systems Report 2026** (read in full from report.zeroheight.com today; Tier B, vendor survey)
- Caveats: zeroheight sells documentation tooling and the report includes product pitches. About 90% of respondents are from North America, Western Europe and Oceania, and 39% work at companies with 5,000+ employees. I could not find the sample size on the page.
- **Tools:** Figma is used by 97% of respondents (73% satisfied). Documentation is fragmented: zeroheight is the leading purpose-built tool, then Confluence 18%, custom sites 16%, Supernova 7%. Satisfaction with documentation tools is 60%. Storybook "remains popular for developer-facing documentation".
- **Tokens:** Tokens Studio is still the most-used Figma plugin (21%), "which suggests that people haven't wholesale moved to Figma's native Variables". Token layers: primitive 90%, semantic 85%, component 52%. 79% use a single library; only 21% alias tokens across libraries (multi-brand). Tokens exist in design tools for 90% and in code for 82%. Only 40% have any token pipeline, 11% sync code to design, and 5% sync both ways.
- **Teams:** 83% of organizations have a dedicated design system team (78% in 2025). Team size: 1-2 people 28%, 3-5 33%, 6-10 25%, and few teams grow past 10. 3 in 5 teams say they are understaffed.
- **Adoption and buy-in:** adoption is the top challenge for the fifth year. Satisfaction with leadership buy-in fell from 42% to 32%, and dissatisfaction rose from 23% to 40%. 69% encourage open contribution. Metrics focus on usage and coverage rather than outcomes; ROI is measured by 5%.
- **Automation and AI:** 37% have some automation. AI: 10% have it built into processes, 46% are experimenting, 44% do not use it (2025: 10/36/54). On whether AI lives up to its potential: 6% very highly, 22% highly, 52% neutral. Only 12% use AI to deliver documentation (via MCP or chatbots); 57% want to. Practitioners want AI for documentation and process automation, and want it to stay away from design generation.
- The report cites Gartner's 2025 Hype Cycle as putting design systems into the "Trough of Disillusionment". That claim is secondhand; do not cite Gartner through zeroheight.
- [S-L00-056]

**Correction to topic a.** The figure "only 15% say AI lives up to the hype" came from a zeroheight LinkedIn snippet and probably refers to the separate "State of AI in Design Systems 2026" report (its page renders only with JavaScript). The main 2026 report says 28% rate AI highly or very highly. Quote the main report's numbers, or label the 15% as coming from the other report.

**Other sources checked**
- **Sparkbox Design Systems Survey:** the latest edition is 2022 (the URL redirects to /2022/). **Stale.** Use it only as history. [S-L00-057]
- Storybook: 10.6.0 stable (2 Sep 2026); 11.0.0-alpha.1 (19 Sep 2026). [S-L00-041]
- Supernova supports Figma extended collections (release note, Mar 2026). [S-L00-045c]

---

## Validation verdicts for other lanes

Legend: **Confirmed** = checked today against a Tier A (or strong Tier B) source. **Disputed** = sources conflict or the community actively contests it. **Stale** = true once, superseded now. **Unverified** = plausible, but I could not open a primary source; check before use. S-ids refer to `traces/L00-trace.md`.

**All lanes**
- **Confirmed:** "code is the source of truth, Figma mirrors it" is the majority practitioner view in Sep 2026 [S-L00-034, S-L00-040, S-L00-055]. Model the builder's output as code-first tokens and components, with Figma as one consumer.
- **Confirmed:** making the system machine-readable measurably helps agents: Sanity's evals (20% to 90% build success for Sonnet, 40% to 100% for Opus; JSON docs beat Markdown; linting cut accessibility violations per iteration from 5.1 to 0.6) [S-L00-036].
- **Disputed:** Jakob Nielsen's personal AI commentary (UX Tigers). NN/g articles remain Tier B [S-L00-034].
- **Warning (method):** WebFetch summaries misdated a Compose release by a year and blurred beta vs GA labels. Take dates from the raw page, release notes, or the GitHub API [S-L00-047].

**L01 Color**
- Confirmed: DTCG 2025.10 is stable and its Color Module supports modern spaces (Display P3, OKLCH, CSS Color 4) [S-L00-008]. CSS Color 4 is live and was updated 13 Sep 2026 [S-L00-059].
- Confirmed: WCAG 2.2 is the current W3C Recommendation; Understanding WCAG 2.2 was updated 11 Feb 2026 [S-L00-059].
- **Disputed:** "WCAG 3 will use APCA". The 10 Sep 2026 WCAG 3.0 Working Draft has "text contrast sufficient" outcomes at developing status and does not mention APCA by name [S-L00-058]. Present APCA as an optional perceptual check, not a compliance standard.
- Stale-risk: the APCA calculator page says "Revised May 27, 2022"; the APCA repo was updated Jul 2026. Cite the repo for current status [S-L00-059].
- Unverified: M3 Expressive color changes. Check m3.material.io directly (the pages render only with JavaScript).

**L02 Typography**
- Confirmed: M3 Expressive adds "emphasized" type scales (Compose Material3 notes: "Updating typography class to support emphasized type scales") [S-L00-047].
- Confirmed: shadcn launched **shadcn/typeset** (typography system, Jul 2026) [S-L00-051].
- Unverified: anything claimed about iOS 27 typography changes. The community pulse only mentions Liquid Glass and toolbar changes.

**L03 Space and layout**
- Confirmed: iOS 27 adds a uniform toolbar when content scrolls under floating bars (MacRumors, WWDC) [S-L00-018].
- Unverified: "M3 Expressive layout system" and "Material Android is Compose-first" from I/O 2026 (snippet only) [S-L00-022b].
- Community: in the zeroheight report, 54% of systems lack UX patterns guidance (only 20% include UX patterns). Layout patterns are an under-served block [S-L00-056].

**L04 Shape, depth, motion**
- Confirmed: Liquid Glass has regular and clear variants, belongs to the controls/navigation layer, never the content layer, and should be used sparingly. It responds to Reduce Transparency, Increase Contrast and a user "look" preference [S-L00-049]. iOS 26.1 added Clear/Tinted, and iOS 27 turned that into a slider plus a darkened edge and brighter specular highlights [S-L00-018, S-L00-019].
- Confirmed: Compose M3 "MotionScheme" (standard and expressive) and shape-morphing buttons have graduated in the **1.5.0 alphas only**. The MaterialShapes and LoadingIndicator promotions were **reverted** [S-L00-047].
- Disputed: "Liquid Glass is unreadable" is now partly stale (the iOS 27 fixes), and the opposite complaint ("toned down too much") exists [S-L00-048].
- Confirmed: Figma Motion is in **open beta**, not GA [S-L00-013].

**L05 Icons, imagery, dataviz**
- Confirmed (constraint, found via community): social-login buttons must use the providers' official logos (Google's branding guidelines page is live) [S-L00-034, S-L00-059]. The builder should not let theming restyle third-party brand marks.
- Community: iPadOS 27 users report lag with "Liquid Glass app icons" turned on [S-L00-048].
- Confirmed: Figma Weave tools (AI image generation inside Figma Design) are in open beta [S-L00-013].

**L06 Brand and voice**
- Community (strong): "AI-generated frontends all look the same". Distinctiveness on top of a shadcn-like base is a real user need [S-L00-050].
- Confirmed (zeroheight 2026): only 37% of systems include brand guidelines, 21% include UX copy guidance, 32% include inclusivity guidance [S-L00-056].
- Community: marketing site and product system drift apart when they sit on different stacks [S-L00-034].

**L07 Tokens and Figma**
- Confirmed: DTCG 2025.10 stable (Format, Color and Resolver modules are live; the Resolver page shows updated 1 Nov 2025) [S-L00-008, S-L00-059]. **Stale:** anything calling DTCG a draft.
- Confirmed: Style Dictionary **v5** (5.5.5, 20 Sep 2026). **Stale:** v4 guides and the README banner [S-L00-042].
- Confirmed: Tokens Studio is still the most-used design-system Figma plugin (21%), so many teams have not moved fully to native Variables [S-L00-056]. Token pipelines exist at only 40% of teams, and bidirectional sync at 5% [S-L00-056].
- Confirmed: Figma remote MCP server is on all seats and plans; write-to-canvas is a free beta that will become usage-based paid [S-L00-044]. Code Connect repo has 1.6K stars and 201 open issues [S-L00-043].
- Confirmed: extended collections (multi-brand) and slots exist on help.figma.com; check the current beta status of slots on the page [S-L00-045].
- Unverified: exactly what Figma imports and exports as DTCG natively. The W3C post only says "supporting or implementing" [S-L00-008].
- Stale: third-party "N MCP tools" counts [S-L00-027].

**L08 Components and patterns**
- Confirmed: shadcn made **Base UI the default** primitive layer (Jul 2026) and supports React Aria. Radix-only assumptions are stale [S-L00-051].
- **Unverified (community-reported):** "shadcn lint", an Oxlint/ESLint plugin that flags off-system Tailwind v4 classes. It is reported by a Better Stack video (65k views) and This Week In React #297, but it was not on the shadcn changelog page when I checked it today. Confirm on ui.shadcn.com before citing [S-L00-050, S-L00-051].
- Confirmed: WAI-ARIA APG page was updated 22 Sep 2026. WAI-ARIA 1.2 is the current Recommendation; 1.3 is a Working Draft (4 Jun 2026) [S-L00-059].
- Confirmed: Compose expressive components graduated in the 1.5.0 alphas include FAB and FAB menu, buttons, split button, floating toolbar, flexible top and bottom app bars, and search bars [S-L00-047].

**L09 Benchmark**
- **Moved:** polaris.shopify.com and polaris-react.shopify.com now redirect to shopify.dev/docs/api/polaris. Polaris is now delivered as web components. Benchmark the shopify.dev pages, not old Polaris React docs [S-L00-059].
- **Moved:** paste.twilio.design redirects to the GitHub repo; the repo's homepage is now paste-dsys.com (live), but that site is an independent fork not affiliated with Twilio, so it is not Paste's new home [S-L00-059] [S-V1a-052].
- **No public docs:** Spotify Encore (the old spotify.design article returns 404). Use it only as a case study from talks and articles [S-L00-059].
- **Moved:** SAP Fiori guidelines moved to sap.com/design-system/fiori-design-web/ (the page blocks bots) [S-L00-059].
- Confirmed live: Salesforce "Lightning Design System 2" (updated 2 Apr 2026), Base by Uber (updated 6 Aug 2025), Gestalt (updated 25 Feb 2026), Porsche Design System v4, NYPL Reservoir v4, Blade (served as a Storybook) [S-L00-059].
- Community: McKinsey open-sourced the QuantumBlack Design System (Sep 2026); a "Design System Atlas" maps 119 public systems. Both are worth a look [S-L00-034].

**L10 Platforms**
- Confirmed: iOS 27 and iPadOS 27 shipped mid-September 2026 with the Liquid Glass changes above [S-L00-048, S-L00-018].
- Confirmed: M3 Expressive is **Compose-first and still alpha** for phones (Compose Material3 1.5.0-alpha28). Wear OS uses Wear Compose Material 3 [S-L00-047].
- Confirmed: **Flutter does not ship M3 Expressive in core.** The umbrella issue #168813 (open since May 2025, updated Aug 2026) says the material and cupertino libraries are being decoupled into standalone packages and M3E work will happen there [S-L00-060].
- Confirmed: Material Web v2.5.0 (Jul 2026) exists; treat web M3 Expressive support as limited [S-L00-042].
- Disputed: "Compose fully supports M3 Expressive without experimental annotations" (only true in alpha) [S-L00-047].

**L11 Process and governance**
- Confirmed (zeroheight 2026, vendor survey): dedicated team at 83% of organizations; typical team of 1-5 people; 3 in 5 understaffed; buy-in satisfaction down from 42% to 32%; AI 10% built in and 46% experimenting; only 12% deliver documentation via AI/MCP [S-L00-056].
- Stale: the Sparkbox survey (latest edition 2022) [S-L00-057].
- Disputed: the zeroheight "15% say AI lives up to the hype" line (see the correction in topic h). Gartner "Trough of Disillusionment" is cited only secondhand [S-L00-056].
- Confirmed: new agent-facing governance artifacts: DESIGN.md (**draft** spec, Apr 2026), Storybook MCP (10.3+), shadcn registry + MCP, Figma MCP + Code Connect, zeroheight MCP (vendor claim), and design-system evals [S-L00-052, S-L00-037, S-L00-033, S-L00-044, S-L00-036].
- Community: MCP connectors can inject instructions into agents (Notion MCP thread, 2,269 points). Include MCP security review in governance [S-L00-050].
- Community: "agentic design system" is contested as a buzzword; practitioners say the real win is "making drift impossible" [S-L00-040, S-L00-050].

---

## Sources to avoid (all topics)
- Undated or AI-generated listicles and explainers: designsystems.surf "best examples", andrew.ooo, asumetech, mindwiredai, aitocore, and generic "Figma Config 2026: 10 biggest announcements" Medium recaps [S-L00-005, S-L00-021, S-L00-031, S-L00-014].
- Third-party blogs that count MCP tools or restate beta/GA status. Go to developers.figma.com and help.figma.com instead [S-L00-027].
- Anything older than Oct 2025 that describes DTCG as a draft, and anything older than Jun 2026 that describes Liquid Glass as a fixed look.
- The Sparkbox survey as a current benchmark (2022).
- Old Polaris React docs and old Twilio Paste docs URLs (both moved).

## Open questions / gaps
- X/Twitter, LinkedIn, TikTok and Instagram were not covered, and design practitioners post heavily on X and LinkedIn. Perplexity was unavailable (quota), and the session's WebSearch budget (200 calls, shared) ran out part-way through, so several leads could not be followed: the "Figma buys AI company" story (21 Sep 2026), m3.material.io I/O 2026 details, and Figma's native DTCG import/export.
- m3.material.io, the Apple HIG HTML and the zeroheight State of AI report render only with JavaScript. I read Apple HIG through its JSON endpoint; m3.material.io was not readable.
- The HN results were dominated by "system design" keyword noise for topics a, b and h, so HN adds little signal for design systems this month.

## Confidence
- **High:** version and date facts pulled from raw pages or APIs (Compose Material3 releases, Style Dictionary, Storybook, shadcn and Tokens Studio release tags, WCAG 3 draft date, DTCG stable, Figma MCP plan/beta terms, Config 2026 beta labels, Apple HIG Materials guidance, zeroheight 2026 numbers as published).
- **Medium:** community sentiment summaries (Tier C, Reddit-heavy, one month of data, no X/LinkedIn).
- **Low / unverified:** I/O 2026 M3 claims, DESIGN.md schema details, "Figma buys AI company", zeroheight's "15%" figure.
