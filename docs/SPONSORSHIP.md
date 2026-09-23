# Sponsorship and funding for OpenDesigner

Owner: R4. Every program below was checked against its own official page on **2026-09-23**. Programs open, close and change terms often, so re-check the page before you apply. Source ids like `[S-R4-601]` point to rows in [`traces/R4-trace.md`](../traces/R4-trace.md). `[inferred]` marks a judgement that no source states directly.

## For sponsors

OpenDesigner is a free, open-source set of skills and knowledge. It lets Claude, ChatGPT, Codex, Cursor and other agents interview a person and build a real design system. The result is design tokens, CSS, Tailwind config, Figma variables and a DESIGN.md that the next session can read. It is maintained by Kunal Bairwa ([github.com/ckryptickunal](https://github.com/ckryptickunal)).

Sponsorship pays for maintenance time, model credits for testing the skills across AI hosts, and hosting for the planned MCP server. Sponsors get visibility, not influence. What OpenDesigner recommends inside an interview (tools, defaults, designers to hire) stays neutral. We may decline sponsors whose products don't suit the project. GitHub Sponsors is being set up. Until the Sponsor button works, contact Kunal through his GitHub profile.

---

The rest of this page is Kunal's working plan.

## The short answer

OpenDesigner is not sponsorable in any serious way today. The repo is public but has 0 stars [S-V1b-001]. GitHub Sponsors is live since 2026-09-24 (github.com/sponsors/ckryptickunal); other platforms have no account yet. Most funds with real money want proof that people use the project. FLOSS/fund says outright that "very new projects or projects with minimal usage are not considered" [S-R4-620]. FOSS United says "we do not fund ideas" [S-R4-648]. So the order is:
1. Set up the payment rails.
2. Launch and get the project listed in the AI-tool directories.
3. Apply to the few programs that take new projects.
4. Approach companies once there are numbers to show them.

Your Marc Lou teardown (`~/Desktop/SPonsorMe/TEARDOWN.md`) already settled one question: a sponsor auction only works when you already have a large audience. That campaign kept $103k. But it ran on 390k followers on X and a post that had gone viral the day before. The buyers were companies paying to reach his audience. It is not an option until OpenDesigner has an audience of its own. Two lessons from it do carry over:
- **Never show an empty sponsor wall.** List in-kind supporters, such as companies that give credits.
- **Publish your numbers openly.**

## Ranked shortlist

| # | Option | When | Effort | Likely value | Why it ranks here |
|---|---|---|---|---|---|
| 1 | **GitHub Sponsors** | Now | About 2 hours, then GitHub reviews it | Small at first. It is the payment route most other funders use. | India is a supported region. GitHub charges no fee on sponsorships from personal accounts and up to 6% from organizations. Money is paid by Stripe Connect to an Indian bank account [S-R4-602, S-R4-605]. The first payout comes 60 days after the first sponsorship, and Stripe Connect pays out on the 22nd whatever the balance [S-V1b-057]. Microsoft's FOSS Fund prefers it, and Open Source Pledge companies pay through it [S-R4-637, S-R4-147]. |
| 2 | **FOSS United** fellowship or project grant | Week 3, after launch, with first users | About 1 day: a funding.json file and a form | ₹1.8L to ₹7L is realistic | The only large fund that favours Indian individuals. Project grants go up to ₹15L, with a typical grant of ₹3–7L paid over a year. In 2026 it gave a ₹1.8L fellowship for "improving design across the open source ecosystem" [S-R4-648, S-R4-112]. It looks at the person first but asks how many users the project has, so apply after launch. |
| 3 | **AI-tool credits:** Cline open-source grant, then OpenAI Codex for Open Source | Week 2 | 1–2 hours each | Cline: $1k–$10k in credits. OpenAI: 6 months of ChatGPT Pro plus possible API credits. | Both take applications on a rolling basis [S-R4-652, S-R4-639]. The credits pay for testing the skills across models, which this project needs. OpenAI looks for widely used projects but says "apply anyway and explain why" [S-R4-639], so odds are low until there is usage. |
| 4 | **Vercel Open Source Program** (next window) | When it reopens | About 2 hours | $3,600 in credits over 3 years, a starter pack of third-party credits, and a mention in the cohort blog post | Closed now [S-R4-650]. Windows open four times a year, and the Spring 2026 cohort included agent-skill repos [S-R4-305]. Vercel also employs the creator of shadcn/ui [S-R4-309]. |
| 5 | **Emergent Ventures** (India track) | Week 3 | Half a day | Cash grant; amount not stated | Rolling, open to individuals, and has "dedicated support" for India-focused projects [S-R4-653]. A long shot, but it funds early ideas. |
| 6 | **Direct outreach to companies** (Penpot, Paper, Tokens Studio, Chromatic, then AI app builders) | Week 4 onward, with numbers | About 1 hour per company | $100–$500 a month, in-kind support, or co-marketing | None of these companies runs a cash program you can apply to [S-R4-311 to S-R4-323]. See "Companies" below. |
| 7 | **Nagarathna Memorial Grant** | Opens January 2027 | 1 hour | ₹1,00,000 | Open to anyone; prefers free and open-source or Creative Commons work [S-R4-649]. |
| 8 | **FLOSS/fund** (Zerodha) | Once there is real usage | Reuses the funding.json file | $10k–$100k a year | Excludes very new projects [S-R4-620]. The same funding.json file serves FLOSS/fund and FOSS United [S-R4-616, S-R4-621]. |
| 9 | **Claude for Open Source** | Once one of its tracks is met | 30 minutes | 6 months of Claude Max 20x (no API credits) | Tracks include 20+ outside contributors in 12 months, or 100+ merged pull requests to repos you don't own. Kunal has 27 [S-R4-643, S-R4-645]. |
| 10 | **Open Collective** via Open Source Collective | When companies ask for invoices, or a team forms | The repo has to move to a GitHub organization | 10% fee | Requires "an organizational repository, not a personal account" plus signs of usage [S-R4-609, S-R4-610]. |

## Every option checked

Fit is my judgement for OpenDesigner as it is today [inferred]. All rows were checked on 2026-09-23.

### Sponsorship platforms

| Option | India / individuals | Fees and terms | Status | Fit | Src |
|---|---|---|---|---|---|
| [GitHub Sponsors](https://docs.github.com/en/sponsors/getting-started-with-github-sponsors/about-github-sponsors) | Yes. Stripe Connect to an Indian bank; country of residence and bank must match. Needs a W-8BEN tax form and two-factor login. | 0% from personal accounts; up to 6% from organizations (3% saved if they pay by invoice). Paid out within 30 days after month end. The first payout comes 60 days after the first sponsorship; Stripe Connect pays on the 22nd whatever the balance [S-V1b-057]. | Open | **High** | 602, 605, 006 |
| [Open Source Collective](https://docs.oscollective.org/getting-started/acceptance-criteria) | Yes, paid by Wise or PayPal (PayPal capped at $600) | 10% host fee. Needs an organization repo, an OSI-style license, and activity or usage. | Open (2,698 projects hosted) | Later | 609, 610, 012, 018 |
| India-based fiscal host on Open Collective | None credible: 7 India hosts, none for software; FOSS United is not on Open Collective | n/a | n/a | None | 018, 019 |
| [Polar](https://polar.sh/legal/acceptable-use-policy) | Payouts to India are supported | Its policy (effective 2026-03-25) **prohibits donations and sponsorship**. As a seller of paid products it charges 5% + 50¢. | Open, for selling only | Later, for paid products | 021, 022, 024 |
| [thanks.dev](https://thanks.dev/faq) | Unclear for Indian Stripe accounts | Pays only for dependencies listed in package files | Live | Low: OpenDesigner is not a package dependency | 028, 035 |
| [Liberapay](https://liberapay.com/about/global) | "Barely supported": PayPal only | No platform cut; about 5% PayPal fees | Open | Low | 029, 030 |
| [Buy Me a Coffee](https://help.buymeacoffee.com/en/articles/6258038-supported-countries-for-payouts-on-buy-me-a-coffee) | Yes, via Stripe Express | 5% | Open | Medium, as a tip jar | 038, 040 |
| [Ko-fi](https://ko-fi.com/gold) | Uses your own Stripe or PayPal. Stripe is invite-only in India, so in practice PayPal [inferred]. | 0% on tips; 5% on memberships and shop sales | Open | Low to medium | 042, 044, 036 |
| [Patreon](https://support.patreon.com/hc/en-us/articles/11111747095181-Creator-fees-overview) | Yes, via PayPal or Payoneer to an INR bank account | 10% for creators who started after 4 Aug 2025 | Open | Low | 045, 047 |
| [Razorpay](https://razorpay.com/docs/payments/international-payments/) | Registered Indian businesses only; individuals must use PayPal for foreign payments | n/a | n/a | Low | 052, 053 |

India notes:
- PayPal India needs an RBI purpose code before you can withdraw to your bank. It describes its service as receiving payment for exports [S-R4-033, S-R4-034].
- Stripe is invite-only for new Indian accounts and needs a PAN [S-R4-036, S-R4-037].
- Sponsorship money is income. Ask a chartered accountant how to report it [inferred].

### Grants and funds

| Option | India / individuals | Amount | Status | Fit | Src |
|---|---|---|---|---|---|
| [FOSS United project grants](https://fossunited.org/grants/thesis) | Indian-origin projects, maintainers mostly in India | Up to ₹15L; typical ₹3–7L over a year | Rolling; apply by submitting a funding.json | **Medium after launch** | 648, 616, 613 |
| [FOSS United fellowships](https://fossunited.org/grants/fellowship) | Individuals | ₹16.5k–₹6L in 2026, including a design fellowship | No formal call; use the general form | **Medium** | 615, 112 |
| [Nagarathna Memorial Grant](https://thejeshgn.com/projects/nagarathna-memorial-grant/) | Anyone | ₹1L, no strings attached | Closed; opens January 2027 (window Jan 14 – Mar 14) | Medium | 649, 156 |
| [FLOSS/fund](https://floss.fund/faq/) | Anyone with a bank account and tax documents | $10k minimum, then steps of $25k, up to $100k a year | Rolling; reviewed quarterly per its FAQ | Later: needs usage | 620, 104, 109 |
| [NLnet](https://nlnet.nl/funding.html) (Restack and others) | Non-EU applicants only if exceptional and with a "European dimension" | €5k–€50k | Next deadline 3 Nov 2026. NGI Zero Commons Fund closed 1 June 2026 | Low: AI projects are out of scope | 622, 623, 624 |
| [Sovereign Tech Fund](https://www.sovereign.tech/programs/fund) | Invests globally | Work worth at least €50k | Rolling | None: funds core infrastructure only | 626, 125 |
| [Mozilla](https://www.mozilla.org/en-US/moss/) | n/a | n/a | MOSS on hiatus; no open Technology Fund call found | None | 630, 631, 130 |
| [GitHub Secure Open Source Fund](https://github.com/open-source/github-secure-open-source-fund) | Yes (GitHub Sponsors regions) | $10k plus a 3-week security course | Rolling | Low: security focus, needs traction | 628, 135 |
| [GitHub Accelerator](https://accelerator.github.com/) | n/a | n/a | Not running; last cohort 2024 | None | 633, 140 |
| [Google Summer of Code](https://developers.google.com/open-source/gsoc/faq) (as mentor org) | Yes | A small stipend to the org per contributor | Org applications open each January; 2027 dates not published | Low for 2027: needs "a solid community" and 2+ mentors | 634, 636, 145 |
| [Microsoft FOSS Fund](https://github.com/microsoft/foss-fund) | Only Microsoft employees can nominate | Up to $12.5k a quarter | Active | Low | 637 |
| [Open Source Pledge](https://opensourcepledge.com/about/) | Maintainers don't apply; companies choose | At least $2k per developer per year, paid through GitHub Sponsors, thanks.dev or Open Collective | Active | Being on GitHub Sponsors makes you payable | 147 |
| [Alpha-Omega](https://alpha-omega.dev/grants/how-to-apply/) | Critical projects | n/a | Q4 window 1–31 Oct 2026 | None: security only | 149 |
| [Open Source Endowment](https://endowment.dev/funding) | Self-nomination allowed | Up to $5k | No dates | Later: scored on downloads and dependents | 153 |
| PSF grants | n/a | n/a | Events only in 2026 | None | 154 |

### AI labs and developer platforms

| Option | What you get | Eligibility | Status | Fit | Src |
|---|---|---|---|---|---|
| [OpenAI Codex for Open Source](https://developers.openai.com/community/codex-for-oss) | 6 months of ChatGPT Pro with Codex; API credits; conditional Codex Security | Needs a ChatGPT account. No stated thresholds; weighs usage and importance. | Open ("Apply today") | Low now, medium after launch | 639, 640, 201 |
| [Claude for Open Source](https://claude.com/contact-sales/claude-for-oss) | 6 months of Claude Max 20x | Numeric tracks (dependents, downloads, PRs, contributors); must live where Claude.ai is offered; OSI-licensed project | Open until the 10,000 cap is reached or Anthropic closes it | Low now | 643, 644 |
| [Claude plugin directory](https://claude.com/docs/plugins/submit) | Listing in Claude Code's official marketplace and in Cowork | Public repo; `claude plugin validate`; individuals submit through Console | Open | **High for distribution** | 654 |
| [OpenAI plugin directory](https://developers.openai.com/plugins/deploy/submission) (ChatGPT and Codex) | Listing; a plugin with only skills is allowed | Identity verification | Open | **High for distribution** | 233 |
| [Gemini CLI extension gallery](https://geminicli.com/docs/extensions/releasing/) | Automatic listing | Public repo, `gemini-cli-extension` topic, `gemini-extension.json` at the repo root | Crawled daily | **High for distribution** | 215 |
| [Vercel Open Source Program](https://vercel.com/open-source-program) | $3,600 in credits over 3 years, plus a starter pack | Active project hosted (or planned) on Vercel, a Code of Conduct, "growth potential" | Closed (summer window ended 13 Sep) | **High, next window** | 650, 225, 305 |
| [Netlify open-source plan](https://www.netlify.com/legal/open-source-policy/) | Free plan with credits | OSI license, a Code of Conduct, a Netlify link on the site | Live | Medium, for a docs site | 235 |
| GitHub Copilot Pro for maintainers | Free Copilot Pro | "Popular" projects, checked automatically each month | Live | Low | 211 |
| Google for Startups, Microsoft for Startups, Anthropic Startups | Cloud or API credits | Need a company (Anthropic's needs VC backing) | Open | None without a company | 221, 229, 231 |
| Google Open Source Peer Bonus | Prepaid card | Only Googlers can nominate | No round found after 2024 | Low | 217, 218 |
| Anthropic AI for Science | Up to $20k in API credits | Researchers at institutions | Open | None | 232 |
| Cloudflare Project Alexandria, Hugging Face GPU grants, Sentry, 1Password, JetBrains | Free services or licences | Various | Live (Alexandria unverified) | Low | 226, 240, 238, 239 |

### AI coding tools

| Company | Formal program? | Listing route | Fit | Src |
|---|---|---|---|---|
| [Cline](https://cline.bot/oss-grant) | Yes: $1M open-source grant, paid as $1k–$10k in credits | MCP marketplace (for the planned MCP server) | **High** | 652, 430, 448 |
| [Kilo Code](https://kilo.ai/oss) (acquired by Anaconda) | Yes: free Kilo tools, starting with code review, if you enable them on public PRs and agree to be featured. Showcased projects are large. | Kilo marketplace takes skills and MCP servers (by pull request) | Medium for credits, **high for listing** | 651, 432, 435 |
| [Cursor](https://cursor.com/marketplace/publish) | No open-source fund; the Ambassador program is for community organisers | Plugin marketplace (skills, rules, MCP) | **High for listing**, low for cash | 433, 434, 454 |
| [Factory](https://factory.com/oss) | Free tool access for open-source contributors | n/a | Medium | 445 |
| Windsurf (now Devin Desktop), Continue (acquired by Cursor), Zed, Warp, Replit, Sourcegraph/Amp | No program. Zed, Warp, Replit and Sourcegraph sponsor their own dependencies. | Zed MCP extensions | Low | 436–453, 646 |

### Companies whose users overlap OpenDesigner's

None of these runs a cash program an outside project can apply to. The ones below are listed by fit.

| Company | What exists | Best route | Fit | Src |
|---|---|---|---|---|
| Vercel / v0 | Open Source Program (above). Funds shadcn/ui through employment and gives through Open Collective (Astro, webpack, Svelte). | Next program window; then the devrel team | **High** | 650, 305, 303 |
| Penpot (Kaleidos) | Plugin contest (2024: $1,000 first prize plus 20 × $200), unpaid ambassadors, open-source discounts | Direct: open source, design tokens and MCP give a shared story | **High for co-marketing**, low for cash | 313 |
| Paper | No program; contact address listed on its site | Direct: integration showcase (a Paper export is planned in the engine) | Medium | 314 |
| Tokens Studio | No program; co-maintains Style Dictionary with Amazon | Direct: collaboration on the design-token standard (DTCG) | Medium | 315, 316 |
| Chromatic / Storybook | Free Chromatic plan for open source ("contact us"); sponsors Storybook, Vitest and MSW | Only if OpenDesigner ships Storybook stories | Medium | 320, 646 |
| Figma | No open-source program. Product Integration Partner program exists. Figma Community payouts **don't support India**. | Integration partner listing for the Figma variables export | Medium as a partner, low for cash | 311, 312 |
| Lovable, Bolt/StackBlitz, v0, Cursor | Referral and partner programs; StackBlitz picks its own sponsored projects | Pitch like Tailwind's partners: AI app builders pay for "Partner" status with Tailwind because the code they generate uses it [S-R4-308]. The same logic applies once their users rely on OpenDesigner. | Medium, later | 308, 323, 325 |
| Framer, Builder.io, Knapsack, Supernova, zeroheight, Untitled UI, Aceternity, Magic UI, 21st.dev | Referral, affiliate or agency programs, or nothing | Direct outreach only | Low | 310, 317–319, 322, 327–329 |

For comparison, what similar projects receive:
- **Storybook's Open Collective:** $219,915 in total. Tiers are $2 and $100 a month; the top company gave $13.5k.
- **shadcn/ui on GitHub Sponsors:** tiers of $20 a month and $10, $100 or $1,000 one-time.
- **Radix and Style Dictionary:** paid for by the companies that employ their maintainers [S-R4-303, S-R4-301, S-R4-331, S-R4-316].

### Other routes

| Route | Status (2026-09-23) | Fit | Src |
|---|---|---|---|
| [Emergent Ventures](https://www.mercatus.org/emergent-ventures) | Rolling; has an India track | Medium (a long shot) | 653 |
| [Sequoia Open Source Fellowship](https://sequoiacap.com/oss) | Rolling. Pays living costs for 6–12 months and takes no equity; needs real adoption. | Later | 457 |
| Y Combinator, Peak XV Surge, Antler India, Heavybit, OSS Capital, Z Fellows | Open, but these fund companies. YC's Winter 2027 deadline is 2 Nov 2026. | Only if you choose to start a company | 458–470 |
| a16z Open Source AI Grant | No application route; last batch June 2025 | None | 460–462 |
| Hackathons | None found with an official page for Oct 2026 – Mar 2027. FOSS Hack runs in March; the 2027 edition is not announced yet. | Watch | 473, 472 |
| Conference talks | IndiaFOSS is 26–27 Sep 2026 in Bengaluru (talk submissions closed; worth attending to meet the FOSS United grants team). Figma Config India is 15 Oct 2026 (free virtual). React India is 29–31 Oct 2026 in Goa. The AI Design Systems Conference (Into Design Systems) is 10–11 Mar 2027, and its speakers are already announced. No open Config 2027 call for speakers found. | Aim for 2027 calls for talks; talks lead to sponsor contacts [inferred] | 471, 476, 480, 477, 475 |
| Paid tiers that keep the core open | Precedents: Tailwind Plus, Excalidraw+, Penpot's cloud plan, Plausible's cloud, Cal.com. Counter-example: tldraw switched to a source-available licence. OpenDesigner options: a hosted MCP server (Phase 2), team features (shared state and review), paid workshops for engineering teams. From India, Polar can sell these [S-R4-022]. | Later, after adoption | 483–490 |
| Dual licensing | Works only with a copyleft licence plus ownership of every contribution, through a contributor agreement or copyright assignment [S-R4-493, S-R4-494]. MIT and CC BY 4.0 already allow commercial use, so there is nothing to sell. Switching to copyleft would slow adoption by companies and AI hosts [inferred]. | **Not appropriate** | 493, 494 |

## Getting sponsor-ready

### Payment setup (Kunal)
1. **GitHub Sponsors.** Go to github.com/sponsors, join, and fill in the profile. You need Stripe Connect with your PAN and an Indian bank account, the W-8BEN tax form and two-factor login [S-R4-037]. Choose bank or fiscal host at signup; it is hard to change later [S-R4-605]. Then uncomment `github:` in `.github/FUNDING.yml`.
2. **Sponsor button.** The repo is public now [S-V1b-001]. Tick Settings > General > Features > Sponsorships, then "Set up sponsor button" [S-R4-604]. Until GitHub Sponsors is approved, `FUNDING.yml` holds only a `custom:` link to this page's "For sponsors" section.
3. **funding.json.** Publish a [funding.json](https://fundingjson.org/) file (schema v1.1.0) describing the project, the funding channel (GitHub Sponsors) and your plans. If the file's address has a different hostname from the project address, add `.well-known/funding-manifest-urls` [S-R4-621]. Submit its address to FOSS United (fossunited.org/grants/projects/apply) [S-R4-616]. Later, submit it to FLOSS/fund (dir.floss.fund/submit) [S-R4-619]. R1 added it at the repo root ([`funding.json`](../funding.json)). Its `entity.email` is still empty: fill it with a public contact email before you submit.
4. **Decide on a GitHub organization.** Open Source Collective requires one [S-R4-609]. Moving the repo before launch is cheaper than after, but it changes the plugin and marketplace names other lanes use. This is your call.

### Sponsor tiers (monthly, on GitHub Sponsors)

| Tier | Price | What the sponsor gets |
|---|---|---|
| Supporter | $5 | Name in the sponsors list |
| Backer | $20 | Name and link on the README sponsor wall |
| Company | $100 | Small logo in the README and on the docs pages |
| Partner | $500 | Large logo at the top of the README; a line in each release note; a quarterly 30-minute call to hear their feedback (input, not control) |
| One-time | $100 or $1,000 | Same listing as the matching monthly tier, for 12 months |

These prices sit between Storybook's ($2 and $100 a month) and shadcn/ui's ($20 a month, $1,000 one-time) [S-R4-303, S-R4-301]. The policy stays the same at every tier: sponsors never buy influence over recommendations. Storybook's sponsor list shows why you should keep the right to decline sponsors. It includes spam such as "Buy Google Reviews" [S-R4-303].

### Sponsor wall (for R1 to add to the README)
```md
## Sponsors
OpenDesigner is free and open source. Sponsorship funds maintenance, model credits for testing across AI hosts, and the hosted MCP server. [Sponsor OpenDesigner](https://github.com/sponsors/ckryptickunal)

<!-- Partners: large logos. Companies: small logos. Backers: names. Supported by: in-kind credit programs (never leave the wall empty). -->
```

### Numbers to track (log weekly in one sheet)
- **GitHub:** stars, forks, watchers, and traffic (views, clones, referrers). Log weekly, since GitHub keeps only recent traffic data [inferred].
- **Downloads:** release asset downloads (the `download_count` field in the GitHub API), and plugin or directory installs where a directory reports them.
- **People:** outside contributors with merged PRs. The target is 20 in 12 months, which meets a Claude for Open Source track [S-R4-643]. Also count issues opened by people outside the project.
- **Usage:** repos that use OpenDesigner and examples people submit. FLOSS/fund, FOSS United and Open Source Endowment all weigh usage [S-R4-620, S-R4-648, S-R4-153].
- **Money:** sponsors and monthly sponsorship income. Publish these openly, the way Marc Lou did (see the teardown).

### One-page project brief (for outreach and grant forms)
Six blocks, one page:
1. What it is, in two sentences.
2. Who uses it, and a screenshot of one generated design system.
3. The numbers above.
4. How it works: interview, then decisions, then tokens and exports.
5. The next 6 months of roadmap.
6. What the money pays for, the tiers, and how to reach you.

Export it as a PDF and link it from outreach emails.

## Outreach email template (Kunal sends it himself)

```
Subject: OpenDesigner + {Company}: open-source design systems your users build with AI

Hi {first name},

I'm Kunal Bairwa. I maintain OpenDesigner (github.com/ckryptickunal/OpenDesigner), an open-source set of skills
that lets Claude, ChatGPT, Codex and Cursor interview someone and build a real design system: DTCG tokens,
CSS and Tailwind, Figma variables and a DESIGN.md.

Why I'm writing to you: {one specific line, e.g. "it exports straight to {product}", or "your users ask
their agents for design systems every day", or "you already support {peer project}"}.

Where it stands: {stars} stars, {installs} installs, {contributors} outside contributors, {one named user or example}.

The ask: {tier} sponsorship at ${amount}/month through GitHub Sponsors (invoice billing is available).
In return: {logo placement, release-note mention, an example or export guide for {product} if it fits the
project anyway}. Sponsors don't influence what OpenDesigner recommends; that neutrality is why people trust it.

One-page brief: {link}. Happy to do a 20-minute call.

Thanks,
Kunal
```

## 30-day plan (24 Sep – 23 Oct 2026)

| Week | Actions |
|---|---|
| 1 (Sep 24–30) | Join GitHub Sponsors; review takes a few days. Decide on the GitHub organization question. Publish funding.json. The repo is already public, so tick Sponsorships. Submit to the Claude plugin directory (through Console). Make sure R3's manifests meet the Gemini CLI gallery rules (topic plus `gemini-extension.json`). Submit to the OpenAI plugin directory, Cursor marketplace and Kilo marketplace. If you can, attend IndiaFOSS (26–27 Sep, Bengaluru) and meet the FOSS United grants team. |
| 2 (Oct 1–7) | Launch posts. Start the weekly numbers log. Apply to the Cline open-source grant, OpenAI Codex for Open Source ("apply anyway") and Factory's open-source program. Once approved, uncomment `github:` in FUNDING.yml and put in-kind supporters on the sponsor wall. |
| 3 (Oct 8–14) | Apply to FOSS United (a fellowship or project grant, with launch numbers). Apply to Emergent Ventures, choosing India in the region menu. Write the one-page brief. |
| 4 (Oct 15–23) | Send five outreach emails: Penpot, Paper, Tokens Studio, Chromatic, and Vercel devrel (ask about the next program window). Review the numbers. Set reminders: Vercel's next window, the Nagarathna grant (January 2027), FLOSS/fund once there is usage, Claude for Open Source once you have 20 outside contributors, and the Sequoia fellowship once there is adoption. |

Accounts Kunal has to create or use:
- GitHub Sponsors (with Stripe Connect);
- an Anthropic Console account, for the plugin directory, if you're not in a Claude Team org;
- a ChatGPT account plus OpenAI identity verification;
- a Cursor marketplace publisher;
- a FOSS United platform login;
- later, Open Collective;
- optional: Buy Me a Coffee as a tip jar.

## What could not be verified
- Whether GitHub requires an active Sponsors profile before the `github:` key works. The docs imply it [S-R4-005].
- India-specific paperwork for GitHub Sponsors payouts (purpose code, foreign remittance certificate).
- Whether Open Source Collective accepts CC BY 4.0 content alongside MIT code.
- Mozilla Technology Fund status (its page returns 403) [S-R4-631].
- Cloudflare Project Alexandria status (403).
- Vercel's next window date.
- Tailwind's partner prices (quoted by email only).
- Chromatic's free-plan limits.
- The size of an Emergent Ventures grant.
- Config 2027's call for speakers, and Clarity, Smashing and Design Systems London dates.
- "Zero sponsorships" on a company's GitHub account shows only public sponsorships; companies may pay privately or by invoice.

Resolved by the V1 check on 2026-09-24:
- GitHub Sponsors' minimum payout: Stripe Connect has none (GitHub Sponsors Additional Terms 3.3) [S-V1b-057].
- The Cline grant's preference for solo developers: Cline's announcement names solo developers and small teams among the projects it wants [S-V1b-063]. The lead's earlier spot-check had confirmed only the amounts and rolling review [S-R4-652].
