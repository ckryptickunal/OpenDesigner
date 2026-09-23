# R4 (sponsorship and funding for OpenDesigner) source trace

Append-only. One row per source opened, including rejected and failed ones. Date of work: 2026-09-23 (times IST). Perplexity was out of quota (HTTP 401 insufficient_quota), so WebSearch, WebFetch, curl and the GitHub API were used.
Id ranges: 001-099 helper H1 (sponsorship platforms); 100-199 helper H2 (grants and funds); 200-299 helper H3 (AI-lab and developer-platform programs); 300-399 helper H4 (design-tool companies, reference sponsor models); 400-499 helper H5 (AI coding tools, accelerators, conferences, paid tiers, dual licensing); 600-699 lane author (R4 lead), including spot-checks of helper findings. Helper rows are re-logged here from their reports; helper times are batch windows.
Tiers per `_coordination/SCHEMA.md`: A = the program's or company's own page, B = recognized practitioner or official community post, C = secondary.
Format: `| time | S-id | URL | publisher | published/updated date | tier | verdict | what was taken |`

### Lane author (R4 lead)
| time | S-id | URL | publisher | published/updated date | tier | verdict | what was taken |
|---|---|---|---|---|---|---|---|
| 18:55 | S-R4-601 | https://github.com/ckryptickunal (gh api users + GraphQL hasSponsorsListing) | GitHub API | live 2026-09-23 | A | used | Kunal has no GitHub Sponsors listing yet (hasSponsorsListing=false); repo OpenDesigner is PRIVATE, 0 stars, created 2026-09-23 |
| 19:02 | S-R4-602 | https://docs.github.com/en/sponsors/getting-started-with-github-sponsors/about-github-sponsors | GitHub Docs | undated live page | A | used | 0% fee on personal-account sponsorships; up to 6% on org sponsorships (3% card + 3% service), invoiced billing saves 3%; India listed in supported regions; must reside in supported region to receive; matching fund closed 2020 |
| 19:02 | S-R4-603 | https://docs.github.com/en/sponsors/getting-started-with-github-sponsors/supported-regions-for-github-sponsors | GitHub Docs | n/a | A | failed (404; regions now live on the About page, S-R4-002) | nothing |
| 19:03 | S-R4-604 | https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/displaying-a-sponsor-button-in-your-repository | GitHub Docs | undated live page | A | used | FUNDING.yml keys: community_bridge, github (up to 4), issuehunt, ko_fi, liberapay, open_collective, patreon, tidelift, polar, buy_me_a_coffee, thanks_dev (u/gh/USER), custom (up to 4); button enabled by admin in Settings > Sponsorships |
| 19:04 | S-R4-605 | https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/setting-up-github-sponsors-for-your-personal-account | GitHub Docs | undated live page | A | used | Join, profile, tiers, bank + tax info, 2FA, GitHub review; payout via Stripe Connect bank account (region of residence and bank must match) or fiscal host chosen at signup only; W-8BEN for non-US |
| 19:05 | S-R4-606 | https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/managing-your-payouts-from-github-sponsors | GitHub Docs | undated live page | A | used (light) | Payout dashboard; timing governed by GitHub Sponsors Additional Terms s3.3 |
| 19:07 | S-R4-607 | https://oscollective.org/ | Open Source Collective | undated live page | A | used | "Apply today"; multi-country payee support via bank transfer or PayPal |
| 19:08 | S-R4-608 | WebSearch "Open Source Collective acceptance criteria fee 10% apply fiscal host 2026" | various | 2026-09-23 | n/a | URL finder only | pointed to docs.oscollective.org eligibility and fees pages |
| 19:09 | S-R4-609 | https://docs.oscollective.org/getting-started/acceptance-criteria | Open Source Collective Docs | undated live page | A | used | Must show active development and meaningful impact (ownership, activity, usage, originality); OSI or OSHWA-aligned license; project must be hosted under an ORGANIZATIONAL repository, not a personal account; 2+ admins preferred; GitHub-verified apps meeting criteria auto-approved, others reviewed in days |
| 19:10 | S-R4-610 | https://docs.oscollective.org/welcome-and-introduction-to-osc/fees | Open Source Collective Docs | undated live page | A | used | Fixed 10% host fee on incoming funds; no setup/min fees; Stripe/PayPal/Wise processor fees extra; payee Wise account reduces fees; no discounts |
| 19:11 | S-R4-611 | WebSearch "FOSS United fiscal host open collective India projects" | various | 2026-09-23 | n/a | URL finder only; no evidence FOSS United acts as an Open Collective fiscal host | pointed to fossunited.org grants |
| 19:12 | S-R4-612 | WebSearch "FOSS United grants 2026 open source projects apply" | various | 2026-09-23 | n/a | URL finder only (ictworks.org secondary rejected) | pointed to fossunited.org/grants |
| 19:13 | S-R4-613 | https://fossunited.org/grants | FOSS United Foundation | live page, 2026 grantees listed | A | used | Grants for FOSS creators, maintainers, projects, events in India; INR 3 crore+ disbursed; project grants "non-thematic" (dev tools, consumer apps, individuals); fellowship grants for individuals incl. one "improving design across the open source ecosystem"; event grants via grants@fossunited.org |
| 19:14 | S-R4-614 | https://fossunited.org/grants/projects | FOSS United Foundation | live page | A | used | Project grantee list (Rethink DNS, Parseable, Skytable, CircuitVerse, Data For India (CC BY 4.0 content) etc.); funded via Industry Partnership Program and co-sponsors |
| 19:15 | S-R4-615 | https://fossunited.org/grants/fellowship | FOSS United Foundation | live page | A | used | Fellowship grants for individuals to dedicate time to FOSS; examples incl. INR 6L follow-on fellowship, design-across-OSS fellowship |
| 19:16 | S-R4-616 | https://fossunited.org/grants/projects/apply | FOSS United Foundation | live page | A | used | Project grant application = submit a funding.json manifest (same format as FLOSS/fund); listed in fossunited.org/grants/directory |
| 19:17 | S-R4-617 | WebSearch "fossunited.org grants Indian bank account funding.json evaluation criteria" | various | 2026-09-23 | n/a | URL finder only | pointed to docs.fossunited.org/grants |
| 19:18 | S-R4-618 | https://docs.fossunited.org/grants/ | FOSS United Knowledge Base | (c) 2021-2026 | A | used | Eligibility: individual or org working on FOSS in India, clear plan, demonstrated need; max INR 6 lakh per grant; co-sponsored grants possible. (Search snippet adds "must have an Indian bank account"; not seen on this page, marked as snippet) |
| 19:19 | S-R4-619 | https://floss.fund/ | FLOSS/fund (Zerodha) | live page; tranches May 2025, Oct 2025 | A | used | $1M/year for FOSS; individuals and orgs; apply at dir.floss.fund/submit |
| 19:20 | S-R4-620 | https://floss.fund/faq/ | FLOSS/fund (Zerodha) | undated live page | A | used | Any individual/org with bank account + tax docs; "Very new projects or projects with minimal usage are not considered for the time being"; up to $100k/yr, min $10k then $25k multiples; committee reviews quarterly; up to 4 weeks paperwork |
| 19:21 | S-R4-621 | https://fundingjson.org/ | funding.json project | v1.1.0 live | A | used | funding.json manifest schema v1.1.0 (https://fundingjson.org/schema/v1.1.0.json); cross-host provenance via /.well-known/funding-manifest-urls (for GitHub repos: repo/blob/main/.well-known/funding-manifest-urls) |
| 19:22 | S-R4-622 | https://nlnet.nl/funding.html | NLnet Foundation | live; "Next deadline November 3. 2026" | A | used | Grants EUR 5k-50k; back-to-back calls, deadline on the 3rd of every other month; anyone can apply; all outputs FOSS; open funds: Restack, Open Social Fund, Research and Higher Education Technology Fund, CodeSupply pilot |
| 19:23 | S-R4-623 | https://nlnet.nl/commonsfund/ and /commonsfund/eligibility/ | NLnet Foundation | live | A | used | NGI Zero Commons Fund 13th and final call closed 1 June 2026, no new applications |
| 19:24 | S-R4-624 | https://nlnet.nl/restack/ and /restack/eligibility/ | NLnet Foundation | live; Horizon Europe grant 101299072 | A | used | Restack: core internet infrastructure; "AI-related projects are not within scope" unless >1M active human users; EU/Horizon-associated applicants prioritised, others only if exceptional quality, unique expertise and a clear European dimension |
| 19:25 | S-R4-625 | https://www.sovereign.tech/programs | Sovereign Tech Agency | live; Standards pilot Jun 2026-Jun 2027 | A | used | Four areas: Fund, Resilience, Fellowship (maintainers of critical components), Standards (pilot applications were May 2026); Challenge deadline passed 2023 |
| 19:26 | S-R4-626 | https://www.sovereign.tech/programs/fund | Sovereign Tech Agency | live | A | used | Invests globally in open digital base technologies; work must exceed EUR 50,000; English/German via portal; criteria: public interest, criticality; not a fit for a new design-knowledge project |
| 19:27 | S-R4-627 | WebSearch "GitHub Secure Open Source Fund 2026 cohort applications" | various | 2026-09-23 | n/a | URL finder only (grantedai.com aggregator rejected) | pointed to github.com/open-source/github-secure-open-source-fund |
| 19:28 | S-R4-628 | https://github.com/open-source/github-secure-open-source-fund | GitHub | page content updated 2026-09-01 | A | used | $10,000 per project + 3-week security program; rolling applications for all sessions; any current maintainer with OSS license, located in a GitHub Sponsors region, active GitHub profile; security focus |
| 19:29 | S-R4-629 | WebSearch "Mozilla open source grants 2026 apply" | various | 2026-09-23 | n/a | URL finder only (grantedai, grantforward aggregators rejected) | pointed to mozilla.org/moss |
| 19:30 | S-R4-630 | https://www.mozilla.org/en-US/moss/ | Mozilla | live | A | used | "MOSS Applications Are Closed": indefinite hiatus since 2020 restructuring; points to Mozilla Technology Fund |
| 19:31 | S-R4-631 | https://www.mozillafoundation.org/en/what-we-do/grantmaking/mozilla-technology-fund/ | Mozilla Foundation | n/a | A | failed (HTTP 403 to curl and WebFetch) | nothing; MTF 2026 status unverified |
| 19:32 | S-R4-632 | WebSearch "Mozilla Technology Fund 2026 call for proposals theme deadline" (Mozilla domains) | Mozilla (search snippets) | 2026-09-23 | n/a | used as URL finder; snippets only | Latest MTF call found closed 5 Oct 2023 (environmental justice + AI); 2026 Fellows (up to 10, nominations) and US-faculty Responsible Computing Challenge; no open MTF call found |
| 19:33 | S-R4-633 | https://accelerator.github.com/ | GitHub | live; latest cohort "GitHub Accelerator 2024" | A | used | Only the 2024 (AI) cohort is shown with "Sign up for updates"; no 2025 or 2026 cohort announced: treat as not running |
| 19:34 | S-R4-634 | https://developers.google.com/open-source/gsoc/timeline | Google | live; 2026 timeline + general timing | A | used | Mentoring-org applications open in January for ~2 weeks (2026: Jan 19-Feb 3), orgs announced Feb; so next window about Jan 2027 |
| 19:35 | S-R4-635 | https://developers.google.com/open-source/gsoc/help/mentor-org-application | Google | n/a | A | failed (404) | nothing |
| 19:36 | S-R4-636 | https://developers.google.com/open-source/gsoc/faq | Google | live | A | used | Orgs must be "an active open source project with a solid community that has already released software under an OSI-approved license"; at least two mentors; small stipend per accepted contributor to orgs in good standing |
| 19:37 | S-R4-637 | https://github.com/microsoft/foss-fund (README via gh api) | Microsoft OSPO | repo pushed 2026-05-15, not archived | A | used | Employee-nominated only; project must be used by Microsoft, OSI license, able to receive funds (GitHub Sponsors preferred); up to $12,500 per quarter across projects; no external application |
| 19:40 | S-R4-638 | WebSearch "OpenAI Codex open source fund API credits maintainers apply" | various | 2026-09-23 | n/a | URL finder only (silenceper, oss.fund, ossperks, yangmao, klymentiev secondary: rejected for terms) | pointed to developers.openai.com/community/codex-for-oss |
| 19:41 | S-R4-639 | https://developers.openai.com/community/codex-for-oss | OpenAI | undated live page | A | used | Codex for Open Source: 6 months ChatGPT Pro with Codex, conditional Codex Security, API credits via Codex Open Source Fund ($1M) for PR review/maintainer automation; "core maintainer or run a widely used public project... apply anyway and explain why"; "Apply today" |
| 19:42 | S-R4-640 | https://developers.openai.com/codex/codex-for-oss-terms | OpenAI | undated live page | A | used | Needs valid ChatGPT account; OpenAI weighs repository usage and ecosystem importance; benefits discretionary and may vary |
| 19:43 | S-R4-641 | WebSearch "Anthropic Claude for open source maintainers free Claude Max program 2026" | various (simonwillison.net, verdent, dataconomy, alphasignal) | Feb-Jul 2026 | n/a | URL finder only; third-party terms (5,000 stars, June 30 close) are superseded by the official page | pointed to claude.com/contact-sales/claude-for-oss |
| 19:44 | S-R4-642 | WebSearch "Claude for Open Source apply maintainers" (claude.com, anthropic.com) | Anthropic (search) | 2026-09-23 | n/a | URL finder | official program page URL |
| 19:45 | S-R4-643 | https://claude.com/contact-sales/claude-for-oss | Anthropic | live (c) 2026 | A | used | 6 months free Claude Max 20x; tracks: 500+ dependent repos / 100+ dependent packages / 200k+ monthly downloads; foundation core contributors; 100+ merged PRs to others' repos in 12 months; 20+ external contributors in 12 months; OpenSSF criticality >= 0.4; else "apply anyway" |
| 19:46 | S-R4-644 | https://www.anthropic.com/claude-for-oss-terms | Anthropic | undated live page | A | used | Individuals 18+, resident where Claude.ai is offered, GitHub account in good standing (age requirement), OSS activity in last 90 days, OSI-licensed project; cap 10,000 recipients; rolling until cap or Anthropic closes it; no API credits |
| 19:47 | S-R4-645 | gh api search: merged PRs by ckryptickunal to repos he does not own since 2025-09-23 | GitHub API | 2026-09-23 | A | used | 27 merged PRs (below the 100 needed for Claude for OSS "active contributor" track) |
| 19:49 | S-R4-646 | gh api graphql organization(login).sponsoring for 25 company orgs | GitHub API | 2026-09-23 | A | used | Orgs sponsoring others on GitHub Sponsors: stackblitz 27 (antfu, vitest-dev, mswjs, colinhacks, eslint...), chromaui 4 (vitest-dev, mswjs, budtmo, openwebdocs), vercel 4 (dai-shi, yyx990803, pilcrowonpaper, rafaelalmeidatk), replit 4, workos 1, zed-industries 1; zero for figma, penpot, framer, tokens-studio, supernova-studio, zeroheight, knapsack-labs, storybookjs, BuilderIO, tailwindlabs, getcursor, cline, Kilo-Org, Exafunction, continuedev, warpdotdev, sourcegraph, lovable-dev, untitleduico (org logins guessed; zero can also mean they sponsor via Open Collective or invoices) |
| 19:50 | S-R4-647 | github.com/sponsors, ko-fi.com, buymeacoffee.com, liberapay.com, polar.sh, patreon.com, thanks.dev, opencollective.com/opendesigner (HTTP status of ckryptickunal profile URLs) | each platform | 2026-09-23 | A | used | No existing profiles: BMC, Liberapay, Polar, Patreon, OC "opendesigner" 404; Ko-fi and thanks.dev 403 (bot block, unknown); GitHub Sponsors page 200 but GraphQL says no listing (S-R4-601) |
| 20:12 | S-R4-648 | https://fossunited.org/grants/thesis | FOSS United Foundation | "as of 2025" | A | used (spot-check of helper row S-R4-111) | Up to INR 15L (highest), median INR 3-7L over a year, infra < 3L; "We do not fund ideas or project proposals"; "We look at the person before we look at the project"; asks Indian origin, maintainers in India, number of users. Note: docs.fossunited.org (S-R4-618) still says max INR 6L; thesis is newer |
| 20:13 | S-R4-649 | https://thejeshgn.com/projects/nagarathna-memorial-grant/ | Thejesh GN (grant owner) | 2026 results posted | A (owner's own page) | used (spot-check of S-R4-156) | Yearly INR 1,00,000 micro-grant; prefers FOSS or Creative Commons work; "Closed for 2026. Will open in Jan 2027" |
| 20:15 | S-R4-650 | https://vercel.com/open-source-program | Vercel | undated live page | A | used (spot-check of S-R4-224/304) | "Applications are currently closed"; $3,600 credits over 3 years + OSS Starter Pack; needs active project, hosted or intended on Vercel, measurable impact or growth potential, Code of Conduct |
| 20:15 | S-R4-651 | https://kilo.ai/oss | Kilo | undated live page | A | used (spot-check of S-R4-432) | Kilo Open Source Sponsorship Program: free Kilo tools starting with Code Reviews; banner "Kilo has been acquired by Anaconda!"; showcased projects are large (helm 29k stars) |
| 20:16 | S-R4-652 | https://cline.bot/blog/5m-installs-1m-open-source-grant-program | Cline | 2026-01-30 | A | used (spot-check of S-R4-430) | $1M program, grants "$1,000 to $10,000 dollars in credits", rolling review |
| 20:17 | S-R4-653 | https://www.mercatus.org/emergent-ventures | Mercatus Center | undated live page | A | used (spot-check of S-R4-463) | "Apply Now"; "dedicated support available for projects with a focus on India"; applicants 13+; funds scalable zero-to-one ideas; amounts not stated |
| 20:18 | S-R4-654 | https://claude.com/docs/plugins/submit | Anthropic | undated live page | A | used (spot-check of S-R4-213) | Community plugin directory = claude-plugins-official marketplace in Claude Code; repo must be public; run `claude plugin validate`; individuals submit via Console (platform.claude.com/plugins/submit); updates auto-mirrored |

### Helper H1: individual sponsorship platforms (S-R4-001 to 054), 18:59-19:10
| time | S-id | URL | publisher | published/updated date | tier | verdict | what was taken |
|---|---|---|---|---|---|---|---|
| H1 | S-R4-001 | docs.github.com/en/sponsors/getting-started-with-github-sponsors/about-github-sponsors | GitHub | undated | A | used | Fees, region list with India, Matching Fund closed 2020 |
| H1 | S-R4-002 | docs.github.com/en/repositories/.../displaying-a-sponsor-button-in-your-repository | GitHub | undated | A | used | FUNDING.yml keys and syntax |
| H1 | S-R4-003 | docs.github.com/en/sponsors/.../setting-up-github-sponsors-for-your-personal-account | GitHub | undated | A | used | Bank or fiscal host, W-8BEN, 2FA, review |
| H1 | S-R4-004 | docs.github.com/en/sponsors/.../managing-your-payouts-from-github-sponsors | GitHub | undated | A | used | Stripe Connect payout receipts |
| H1 | S-R4-005 | docs.github.com/en/sponsors/.../about-github-sponsors-for-open-source-contributors | GitHub | undated | A | used | Tiers; "After you join GitHub Sponsors, you can add a sponsor button" |
| H1 | S-R4-006 | docs.github.com/en/site-policy/github-terms/github-sponsors-additional-terms | GitHub | undated | A | used | Stripe is processor; payout within 30 days after month end |
| H1 | S-R4-007 | docs.github.com/en/sponsors/.../using-a-fiscal-host-to-receive-github-sponsors-payouts | GitHub | undated | A | used | Supported fiscal hosts |
| H1 | S-R4-008 | docs.oscollective.org/getting-started/acceptance-criteria | OSC | n/a | A | failed for H1 (404; lead fetched it fine, S-R4-609) | nothing |
| H1 | S-R4-009 | docs.oscollective.org/ | OSC | undated | A | rejected (index only) | nothing |
| H1 | S-R4-010 | docs.oscollective.org/interested-in-joining-osc/acceptance-criteria.md | OSC | undated | A | used | License lists (OSI/FSF/Debian/Fedora); organizational-repository rule |
| H1 | S-R4-011 | docs.oscollective.org/welcome-and-introduction-to-osc/fees.md | OSC | undated | A | used | 10% host fee |
| H1 | S-R4-012 | docs.oscollective.org/llms-full.txt | OSC | undated | A | used | "Is OSC right" table (may not fit if paying only yourself or < $600/yr); payouts Wise or PayPal, PayPal capped at $600 |
| H1 | S-R4-013 | docs.oscollective.org/llms.txt | OSC | undated | A | used | Page index |
| H1 | S-R4-014 | opencollective.com/ofico/updates/a-new-home-for-the-open-collective-platform-same-mission | OFiCo | 2024-10-11 | A | used | Platform moved to a nonprofit |
| H1 | S-R4-015 | blog.opencollective.com/open-collective-official-statement-ocf-dissolution | Open Collective | 2024-02-28 | A | used | OCF dissolved; OSC unaffected |
| H1 | S-R4-016 | fossunited.org/grants/projects | FOSS United | 2020-2026 lists | A | used | Grants to individuals; no fiscal hosting |
| H1 | S-R4-017 | fossunited.org/grants | FOSS United | undated | A | used | Grants program |
| H1 | S-R4-018 | api.opencollective.com/graphql/v2 (host query) | Open Collective | live | A | used | 7 India-based hosts, none a software host; OSC open, 10%, 2,698 hosted |
| H1 | S-R4-019 | api.opencollective.com/graphql/v2 (FOSS United query) | Open Collective | live | A | used | FOSS United not on Open Collective |
| H1 | S-R4-020 | polar.sh/docs/llms.txt | Polar | undated | A | used | Page index |
| H1 | S-R4-021 | polar.sh/docs/merchant-of-record/fees.md | Polar | mentions 2026-05-27 | A | used | Starter 5% + 50c, +1.5% non-US cards |
| H1 | S-R4-022 | polar.sh/docs/merchant-of-record/supported-countries.md | Polar | undated | A | used | India on Stripe Connect Express payout list |
| H1 | S-R4-023 | polar.sh/docs/merchant-of-record/account-reviews.md | Polar | undated | A | used | Up to 14-day review |
| H1 | S-R4-024 | polar.sh/legal/acceptable-use-policy | Polar | effective 2026-03-25 | A | used | Prohibits "Donations, crowdfunding, community access, advertising, and sponsorship" |
| H1 | S-R4-025 | thanks.dev | thanks.dev | n/a | A | failed (needs JavaScript) | nothing |
| H1 | S-R4-026 | docs.thanks.dev | thanks.dev | n/a | A | failed (no response) | nothing |
| H1 | S-R4-027 | thanks.dev/llms.txt | thanks.dev | n/a | A | failed (403) | nothing |
| H1 | S-R4-028 | thanks.dev/faq (browser) | thanks.dev | undated | A | used | Donor fee min 5%; maintainers pay none; payouts via Stripe Connect, GitHub Sponsors, Open Collective; only package-manifest dependencies |
| H1 | S-R4-029 | liberapay.com/about/global | Liberapay | undated | A | used | India "barely supported" (PayPal, not Stripe) |
| H1 | S-R4-030 | liberapay.com/about/faq | Liberapay | undated | A | used | No cut; ~3% Stripe / ~5% PayPal processing |
| H1 | S-R4-031 | liberapay.com/about/payment-processors | Liberapay | undated | A | used | PayPal currencies (INR not among them) |
| H1 | S-R4-032 | paypal.com/in/...help277 | PayPal | n/a | A | failed ("unpublished") | nothing |
| H1 | S-R4-033 | paypal.com/in/cshelp/article/...-help978 | PayPal India | undated | A | used | RBI purpose code needed before withdrawal |
| H1 | S-R4-034 | paypal.com/in/legalhub/paypal/useragreement-full | PayPal India | updated 2025-01-13 | A | used | "Export Payment Services" framing |
| H1 | S-R4-035 | support.stripe.com/questions/support-for-money-transfers-from-international-platforms-to-india-based-stripe-accounts | Stripe | undated | A | used | Transfers to Indian accounts only from US platforms |
| H1 | S-R4-036 | support.stripe.com/questions/stripe-accounts-are-invite-only-in-india | Stripe | undated | A | used | Stripe invite-only in India |
| H1 | S-R4-037 | support.stripe.com/questions/onboarding-requirements-for-stripe-connect-in-india | Stripe | undated | A | used | PAN required |
| H1 | S-R4-038 | help.buymeacoffee.com/en/articles/6258038 | Buy Me a Coffee | 2026-08-24 | A | used | India on Stripe Express payout list |
| H1 | S-R4-039 | help.buymeacoffee.com/en/articles/9770774 | Buy Me a Coffee | 2026-03-18 | A | used | Stripe payout minimums |
| H1 | S-R4-040 | help.buymeacoffee.com/en/articles/4539170 | Buy Me a Coffee | 2026-03-18 | A | used | 5% fee |
| H1 | S-R4-041 | buymeacoffee.com/pricing | Buy Me a Coffee | n/a | A | failed (404) | nothing |
| H1 | S-R4-042 | help.ko-fi.com/.../360009265834 | Ko-fi | 2018-09-17 | A | used | Payouts only via creator's own Stripe or PayPal |
| H1 | S-R4-043 | help.ko-fi.com/.../115003980093 | Ko-fi | n/a | A | failed (403) | nothing |
| H1 | S-R4-044 | ko-fi.com/gold | Ko-fi | undated | A | used | 0% on tips, 5% on memberships/shop; Gold removes it |
| H1 | S-R4-045 | support.patreon.com/.../36426991446797 | Patreon | edited 2026-08-26 | A | used | Standard 10% for pages launched after 4 Aug 2025 |
| H1 | S-R4-046 | support.patreon.com/.../11111747095181 | Patreon | edited 2026-09-11 | A | used | Fee rules |
| H1 | S-R4-047 | support.patreon.com/.../39694936541965 | Patreon | edited 2026-09-16 | A | used | India INR bank transfer via Payoneer; PayPal fees |
| H1 | S-R4-048 | support.patreon.com/.../29467737603981 | Patreon | edited 2024-08-22 | A | used | India on PayPal list |
| H1 | S-R4-049 | patreon.com/pricing | Patreon | n/a | A | rejected (not parsed) | nothing |
| H1 | S-R4-050 | floss.fund | Zerodha | n/a | A | failed for H1 (no text) | nothing |
| H1 | S-R4-051 | floss.fund/faq/ | Zerodha | undated | A | used | $10k-$100k; new projects excluded |
| H1 | S-R4-052 | razorpay.com/docs/payments/international-payments/faqs/ | Razorpay | undated | A | used | Registered businesses only |
| H1 | S-R4-053 | razorpay.com/docs/payments/international-payments/ | Razorpay | undated | A | used | Individuals must use PayPal for international payments |
| H1 | S-R4-054 | github.com/open-source/github-secure-open-source-fund | GitHub | undated | A | used | $10k; Sponsors region; traction required |
| H1 | (8 searches) | WebSearch queries | various | 2026-09-23 | n/a | URL finders only | none cited |

### Helper H2: grants and funds (S-R4-100 to 157), 18:59-19:08
| time | S-id | URL | publisher | published/updated date | tier | verdict | what was taken |
|---|---|---|---|---|---|---|---|
| H2 | S-R4-100 | floss.fund | Zerodha | (c) 2026 | A | used | $1M/year; apply link |
| H2 | S-R4-101 | floss.fund/faq/ | Zerodha | undated | A | used | Amounts, usage rule, bank/tax docs, quarterly review |
| H2 | S-R4-102 | floss.fund/blog/ | Zerodha | posts to 2025-10-18 | A | used | Post list |
| H2 | S-R4-103 | floss.fund/blog/the-second-tranche-and-anniversary-reflection/ | Zerodha | n/a | A | failed (404, guessed URL) | nothing |
| H2 | S-R4-104 | floss.fund/blog/second-tranche-2025-anniversary/ | Zerodha | 2025-10-18 | A | used | Applications perpetual; $1M for 2026; ~300 applications; tranches irregular |
| H2 | S-R4-105 | fundingjson.org | FLOSS/fund | undated | A | used | Schema v1.1.0; entity + funding (channels, plans) required; well-known provenance |
| H2 | S-R4-106 | dir.floss.fund/submit | Zerodha | undated | A | used | Submit form live |
| H2 | S-R4-107 | floss.fund/rss.xml | Zerodha | latest 2025-10-18 | A | used | No 2026 posts |
| H2 | S-R4-108 | zerodha.com/open-source | Zerodha | undated | A | used | No other OSS grant |
| H2 | S-R4-109 | floss.fund/projects/2026/ | Zerodha | 2026 | A | used | 2026 Tranche 1 (April): $130k to LibreOffice and Warpgate |
| H2 | S-R4-110 | fossunited.org/grants | FOSS United | 2026 items | A | used | Program, counts |
| H2 | S-R4-111 | fossunited.org/grants/thesis | FOSS United | "as of 2025" | A | used | Criteria, grant sizes, no ideas funded (lead re-checked: S-R4-648) |
| H2 | S-R4-112 | fossunited.org/grants/fellowship | FOSS United | 2026 | A | used | 2026 fellowships INR 16.5k-6L; 14 grantees, INR 24.9L; INR 1.8L design-across-OSS fellowship |
| H2 | S-R4-113 | fossunited.org/grants/project | FOSS United | 2026 | A | used | 2026 project grants INR 15k-8L |
| H2 | S-R4-114 | fossunited.org/fosshack | FOSS United | 2026 | A | used | FOSS Hack 2026 ended (March), INR 5L pool |
| H2 | S-R4-115 | fossunited.org/indiafoss | FOSS United | 2026 | A | used | IndiaFOSS 26-27 Sep 2026; CFP closed 28 Jun |
| H2 | S-R4-116 | fossunited.org/maintainers-may | FOSS United | May-Aug 2026 | A | used | Maintainers Program meetups |
| H2 | S-R4-117 | nlnet.nl/funding.html | NLnet | deadline 2026-11-03 | A | used | Open funds; AI scope note |
| H2 | S-R4-118 | nlnet.nl/propose/ | NLnet | deadline 2026-11-03 | A | used | EUR 5-50k; European dimension; fund list |
| H2 | S-R4-119 | nlnet.nl/commonsfund/ | NLnet | 2026 | A | used | Final call closed 2026-06-01 |
| H2 | S-R4-120 | nlnet.nl/core/ | NLnet | 2024 | A | used | NGI0 Core closed Oct 2024 |
| H2 | S-R4-121 | nlnet.nl/restack/ | NLnet | undated | A | used | Scope; Horizon Europe funded |
| H2 | S-R4-122 | nlnet.nl/foundation/policies/generativeAI/ | NLnet | 2025-12-08, upd. 2026-01-26 | A | used | Generative-AI disclosure/log rules |
| H2 | S-R4-123 | sovereign.tech/programs | Sovereign Tech Agency | 2026 | A | used | Program list and status |
| H2 | S-R4-124 | sovereign.tech/programs/fund | Sovereign Tech Agency | undated | A | used | EUR 50k minimum; base technologies; invests globally; ~10 weeks reply |
| H2 | S-R4-125 | sovereign.tech/programs/fellowship | Sovereign Tech Agency | updated 2026-04-17 | A | used | Closed 2026-04-06; EUR 64-82k/yr; employment option needs Germany residence |
| H2 | S-R4-126 | sovereign.tech/programs/bug-resilience | Sovereign Tech Agency | n/a | A | failed (no text) | nothing |
| H2 | S-R4-127 | mozilla.org/en-US/moss/ | Mozilla | undated | A | used | On hiatus |
| H2 | S-R4-128 | mozillafoundation.org/.../funding-the-future-of-trustworthy-tech/ | Mozilla Foundation | 2024-11-21 | A | used (context) | 2025 "experimentation" |
| H2 | S-R4-129 | mozillafoundation.org/.../mozilla-technology-fund/ | Mozilla Foundation | n/a | A | failed (403; redirects to Grantmaking) | nothing |
| H2 | S-R4-130 | mozillafoundation.org/en/what-we-do/grantmaking/ | Mozilla Foundation | undated | A | used (browser) | No open opportunities listed |
| H2 | S-R4-131 | mozillafoundation.org/.../grantmaking/incubator/ | Mozilla Foundation | undated | A | used | Themed cohorts (Democracy x AI 2026) |
| H2 | S-R4-132 | builders.mozilla.org | Mozilla | undated | A | rejected (thin) | nothing |
| H2 | S-R4-133 | builders.mozilla.org/programs/ | Mozilla | 2024 | A | used | Only 2024 dates |
| H2 | S-R4-134 | resources.github.com/github-secure-open-source-fund/ | GitHub | n/a | A | redirect | to S-R4-135 |
| H2 | S-R4-135 | github.com/open-source/github-secure-open-source-fund | GitHub | (c) 2026 | A | used | $10k ($6k/$2k/$2k) + $10k Azure credits; up to 2 maintainers; 18+; Sponsors region; rolling |
| H2 | S-R4-136 | github.com/sponsors | GitHub | n/a | A | rejected (no region list) | nothing |
| H2 | S-R4-137 | docs.github.com/.../about-github-sponsors | GitHub | undated | A | used | India supported |
| H2 | S-R4-138 | docs.github.com/.../setting-up-github-sponsors-for-your-personal-account | GitHub | undated | A | used | Payout rules |
| H2 | S-R4-139 | accelerator.github.com | GitHub | 2024 | A | used | Last cohort 2024 |
| H2 | S-R4-140 | github.com/accelerator | GitHub | n/a | A | used | Redirects to /open-source |
| H2 | S-R4-141 | developers.google.com/open-source/gsoc/timeline | Google | 2026 | A | used | 2026 org dates |
| H2 | S-R4-142 | developers.google.com/open-source/gsoc/help/mentor-org-application | Google | n/a | A | failed (404) | nothing |
| H2 | S-R4-143 | developers.google.com/open-source/gsoc/faq | Google | updated 2026-02-20 | A | used | Org requirements; discretionary stipend |
| H2 | S-R4-144 | developers.google.com/open-source/gsoc/rules | Google | n/a | A | failed (empty) | nothing |
| H2 | S-R4-145 | summerofcode.withgoogle.com/rules | Google | 2026 rules | A | used (browser) | OSI license, 2+ org admins, discretionary org stipend |
| H2 | S-R4-146 | github.com/microsoft/foss-fund (README via API) | Microsoft | pushed 2026-05-15 | A | used | Employee nomination; $12.5k; round 36 in March 2026 |
| H2 | S-R4-147 | opensourcepledge.com/about/ | Open Source Pledge | launched 2024-10-08 | A | used | $2k per developer per year; pays via thanks.dev, OC, GitHub Sponsors, ecosyste.ms |
| H2 | S-R4-148 | alpha-omega.dev/grants/ | Alpha-Omega | 2023-10-23 | A | rejected (thin) | nothing |
| H2 | S-R4-149 | alpha-omega.dev/grants/how-to-apply/ | Alpha-Omega | undated | A | used | Quarterly windows (Q4: Oct 1-31, 2026); OSI license; security |
| H2 | S-R4-150 | codeforsociety.org/incubator | CS&S | undated | A | used | No open call |
| H2 | S-R4-151 | codeforsociety.org/fiscal-sponsorship | CS&S | n/a | A | failed (404) | nothing |
| H2 | S-R4-152 | endowment.dev | Open Source Endowment | undated | A | used | Overview |
| H2 | S-R4-153 | endowment.dev/funding | Open Source Endowment | undated | A | used | Up to $5k; downloads/dependents/bus-factor scoring; self-nomination |
| H2 | S-R4-154 | python.org/psf/grants/ | PSF | 2026 round | A | used | Events only; window Aug 4-25 |
| H2 | S-R4-155 | thanks.dev | thanks.dev | n/a | A | failed (needs JavaScript) | nothing |
| H2 | S-R4-156 | thejeshgn.com/projects/nagarathna-memorial-grant/ | Thejesh GN | 2026 | A | used | INR 1L; window Jan 14 - Mar 14, 2027; FOSS United added INR 2L in 2026 |
| H2 | S-R4-157 | forum.fossunited.org/t/.../7712 | FOSS United forum | 2026-04-07 | C | used (leads only) | OTF, Interledger leads |

### Helper H3: AI-lab and developer-platform programs (S-R4-200 to 244), 18:59-19:05
| time | S-id | URL | publisher | published/updated date | tier | verdict | what was taken |
|---|---|---|---|---|---|---|---|
| H3 | S-R4-200 | developers.openai.com/community/codex-for-oss | OpenAI | undated | A | used | Benefits, who should apply, form link |
| H3 | S-R4-201 | raw.githubusercontent.com/openai/codex/main/docs/open-source-fund.md | OpenAI | last commit 2025-10-03 | A | used | $1M fund, up to $25k API credits (older terms), rolling |
| H3 | S-R4-202 | openai.com/form/codex-for-oss/ | OpenAI | n/a | A | failed (403) | nothing |
| H3 | S-R4-203 | openai.com/form/codex-open-source-fund/ | OpenAI | n/a | A | failed (403) | nothing |
| H3 | S-R4-204 | developers.openai.com/codex/codex-for-oss-terms.md | OpenAI | undated | A | used | ChatGPT account required; discretionary benefits |
| H3 | S-R4-205 | developers.openai.com/community/codex-for-oss.md | OpenAI | n/a | A | failed (not found) | nothing |
| H3 | S-R4-206 | claude.com/contact-sales/claude-for-oss | Anthropic | (c) 2026 | A | used | Eligibility tracks |
| H3 | S-R4-207 | anthropic.com/claude-for-oss-terms | Anthropic | undated | A | used | 10k cap; GitHub account 2+ years; OSI project |
| H3 | S-R4-208 | claude.com/open-source-max | Anthropic | n/a | A | used | 308 redirect to S-R4-206 |
| H3 | S-R4-209 | anthropic.com/supported-countries | Anthropic | undated | A | used | India listed |
| H3 | S-R4-210 | developers.openai.com/api/docs/supported-countries.md | OpenAI | undated | A | used | India listed |
| H3 | S-R4-211 | docs.github.com/.../get-free-access-to-copilot-pro | GitHub | undated | A | used | Free Copilot Pro for popular OSS maintainers, rechecked monthly |
| H3 | S-R4-212 | docs.github.com/en/copilot/get-started/plans | GitHub | undated | A | used | "Popular open source" wording |
| H3 | S-R4-213 | claude.com/docs/plugins/submit | Anthropic | undated | A | used | Submission paths (lead re-checked: S-R4-654) |
| H3 | S-R4-214 | claude.com/docs/llms.txt | Anthropic | undated | A | used | No separate skills directory |
| H3 | S-R4-215 | geminicli.com/docs/extensions/releasing/ | Google | undated | A | used | Gallery auto-lists public repos with gemini-cli-extension topic + gemini-extension.json, crawled daily |
| H3 | S-R4-216 | opensource.google/programs-and-services/peer-bonus/ | Google | n/a | A | failed (404) | nothing |
| H3 | S-R4-217 | opensource.google/programs-and-services/peer-bonus/winner | Google | updated 2022-02-09 | A | used | Googler nomination only |
| H3 | S-R4-218 | opensource.googleblog.com/search/label/peer%20bonus | Google | n/a | A | used | Newest labelled post Dec 2023 |
| H3 | S-R4-219 | opensource.googleblog.com/search?q=peer+bonus | Google | n/a | A | used | Nothing newer |
| H3 | S-R4-220 | cloud.google.com/startup/ai | Google | undated | A | used | AI tier criteria (VC-funded) |
| H3 | S-R4-221 | cloud.google.com/startup/pre-funded | Google | undated | A | used | Start tier $2k; needs a startup |
| H3 | S-R4-222 | ai.google.dev/gemini-api/docs/pricing | Google | undated | A | used | Free tier exists |
| H3 | S-R4-223 | ai.google.dev/gemini-api/docs/available-regions | Google | undated | A | used | India listed |
| H3 | S-R4-224 | vercel.com/open-source-program | Vercel | undated | A | used | Closed; terms (lead re-checked: S-R4-650) |
| H3 | S-R4-225 | community.vercel.com/t/.../48567 | Vercel staff | "Aug 28" | B | used | Summer 2026 window open until Sep 13 |
| H3 | S-R4-226 | blog.cloudflare.com/expanding-our-support-for-oss-projects-with-project-alexandria/ | Cloudflare | 2024-09-27 | A | used | Criteria |
| H3 | S-R4-227 | cloudflare.com/lp/project-alexandria/ | Cloudflare | n/a | A | failed (403 bot challenge) | nothing |
| H3 | S-R4-228 | microsoft.com/en-us/startups | Microsoft | undated | A | rejected (thin) | nothing |
| H3 | S-R4-229 | learn.microsoft.com/en-us/startups/microsoft-for-startups/overview | Microsoft | updated 2026-05-29 | A | used | For-profit company required |
| H3 | S-R4-230 | anthropic.com/startup-program-official-terms | Anthropic | undated | A | used | Company account |
| H3 | S-R4-231 | claude.com/programs/startups | Anthropic | undated | A | used | VC-backed requirement |
| H3 | S-R4-232 | support.claude.com/...ai-for-science-program | Anthropic | undated | A | used | $20k credits; research institutions |
| H3 | S-R4-233 | developers.openai.com/plugins/deploy/submission.md | OpenAI | undated | A | used | Plugin directory (ChatGPT + Codex); identity verification |
| H3 | S-R4-234 | help.openai.com/...researcher-access-program-faq | OpenAI | n/a | A | failed (403) | nothing |
| H3 | S-R4-235 | netlify.com/legal/open-source-policy/ | Netlify | undated | A | used | OSS plan and criteria |
| H3 | S-R4-236 | jetbrains.com/community/opensource/ | JetBrains | n/a | A | failed (needs JavaScript) | nothing |
| H3 | S-R4-237 | sales.jetbrains.com/...OSS-development-license... | JetBrains | updated 2026-01-07 | A | rejected (no criteria) | program exists |
| H3 | S-R4-238 | sentry.io/for/open-source/ | Sentry | undated | A | used | Sponsorship plan |
| H3 | S-R4-239 | raw.githubusercontent.com/1Password/for-open-source/main/README.md | 1Password | undated | A | used | Requirements |
| H3 | S-R4-240 | huggingface.co/docs/hub/en/spaces-zerogpu | Hugging Face | undated | A | used | 2 free ZeroGPU Spaces |
| H3 | S-R4-241 | huggingface.co/docs/hub/spaces-gpus | Hugging Face | undated | A | used | Grant path |
| H3 | S-R4-242 | github.com/open-source/github-secure-open-source-fund | GitHub | undated | A | used (duplicate of S-R4-135) | $10k; eligibility |
| H3 | S-R4-243 | docs.github.com/.../about-github-sponsors | GitHub | undated | A | used (duplicate) | India supported |
| H3 | S-R4-244 | docs.github.com/.../about-github-sponsors-for-open-source-contributors | GitHub | undated | A | rejected (no region list) | nothing |
| H3 | (searches) | Simon Willison, OSS Perks, grantedai, klymentiev etc. | third parties | 2026 | C | URL finders only | no terms taken |

### Helper H4: design-tool companies and reference sponsor models (S-R4-300 to 334), 18:59-19:09
| time | S-id | URL | publisher | published/updated date | tier | verdict | what was taken |
|---|---|---|---|---|---|---|---|
| H4 | S-R4-300 | GitHub GraphQL `sponsoring` for 23 company orgs | GitHub | live | A | used | Public sponsorships per org |
| H4 | S-R4-301 | GitHub GraphQL sponsor listings for 16 accounts | GitHub | live | A | used | shadcn tiers ($10 one-time, $20/mo, $100 and $1,000 one-time), 53 public sponsors |
| H4 | S-R4-302 | GitHub REST: READMEs/FUNDING.yml of shadcn-ui/ui, storybookjs/storybook, tailwindlabs/tailwindcss, penpot/penpot, radix-ui/primitives, style-dictionary/style-dictionary | GitHub | live | A | used | Funding links; no README sponsor sections |
| H4 | S-R4-303 | api.opencollective.com/graphql/v2 | Open Collective | live | A | used, partly rate-limited | Company giving; Storybook backers ($219,915 total; Backer $2/mo, Sponsor $100/mo; Applitools $13.5k, Nx $11.4k, Chromatic $10.8k...) |
| H4 | S-R4-304 | vercel.com/open-source-program | Vercel | undated | A | used | Benefits, criteria, closed |
| H4 | S-R4-305 | vercel.com/blog/vercel-open-source-program-spring-2026-cohort | Vercel | 2026-06-29 | A | used | Cohort incl. taste-skill, Marketing Skills, Claude-Mem, shadcnpreset, Reshaped; "four times a year" |
| H4 | S-R4-306 | community.vercel.com/t/.../42278 | Vercel staff | 2026-05-20 | B | used | Application link |
| H4 | S-R4-307 | vercel.com/partners | Vercel | undated | A | used | Partner tracks |
| H4 | S-R4-308 | tailwindcss.com/sponsor (to /partners) | Tailwind Labs | undated | A | used | Partner/Ambassador/Supporter tiers; ~29 Partners incl. Cursor, Vercel, v0, Lovable, Bolt; partners@tailwindcss.com |
| H4 | S-R4-309 | ui.shadcn.com (+ /sponsors 404) | shadcn | undated | A | used | "Built by shadcn at Vercel" |
| H4 | S-R4-310 | framer.com help (creator program), /creators, /pricing | Framer | 2026-09-15 | A | used | Creator Program: 50% referral for 12 months |
| H4 | S-R4-311 | figma.com, /partners, /affiliate-program, /education | Figma | undated | A | used | Affiliate sunset 2024-08-16; Product Integration Partner program |
| H4 | S-R4-312 | help.figma.com/.../About-selling-Community-resources | Figma | undated | A | used | 15% fee; India not a supported payout country |
| H4 | S-R4-313 | penpot.app, /ambassador-program, /plugins-contest, /pricing | Kaleidos | contest 2024 | A | used | Plugins contest ($1,000 + 20 x $200, Dec 2024); ambassadors; OSS discounts |
| H4 | S-R4-314 | paper.design, /community, /pricing | Paper | undated | A | used | No program; team@paper.design listed |
| H4 | S-R4-315 | tokens.studio, /pricing, /partners, /open-source, sitemap | Tokens Studio | undated | A | used (2 pages 404) | No program found |
| H4 | S-R4-316 | styledictionary.com/versions/v4/statement/ | Style Dictionary | undated | A | used | Co-maintained by Amazon and Tokens Studio |
| H4 | S-R4-317 | supernova.io, /pricing, /partners, sitemap | Supernova | undated | A | used (/partners 404) | No program found |
| H4 | S-R4-318 | zeroheight.com, /pricing, /partners, /partner-program, sitemap | zeroheight | undated | A | used (2 pages 404) | No program found |
| H4 | S-R4-319 | knapsack.cloud, /partners, /pricing, sitemap | Knapsack | undated | A | used | Agency Solutions Partner program only |
| H4 | S-R4-320 | chromatic.com, /pricing, /open-source | Chromatic | undated | A | used (/open-source 404) | "Free for open source... Contact us" |
| H4 | S-R4-321 | storybook.js.org, /community | Storybook | undated | A | used | "Maintained by Chromatic"; OC link |
| H4 | S-R4-322 | builder.io, /partners, /affiliate, /pricing, sitemap | Builder.io | undated | A | used (affiliate terms JS-only) | Agency + affiliate programs |
| H4 | S-R4-323 | lovable.dev (403), /partners, /pricing, sitemap | Lovable | undated | A | used | Partner tracks; student discount |
| H4 | S-R4-324 | bolt.new, /pricing, stackblitz.com | StackBlitz | undated | A | rejected (nothing relevant) | nothing |
| H4 | S-R4-325 | blog.stackblitz.com/posts/bolt-100k-oss-fund/ | StackBlitz | 2025-02-13 | A | used | Bolt 100K OSS Fund; StackBlitz picks projects |
| H4 | S-R4-326 | blog.stackblitz.com/posts/stackblitz-joins-osspledge/ | StackBlitz | 2024-09-17 | A | used | Open Source Pledge member |
| H4 | S-R4-327 | untitledui.com, /affiliates | Untitled UI | undated | A | used | 30% affiliate |
| H4 | S-R4-328 | ui.aceternity.com, /sponsor, /affiliate-program | Aceternity | undated | A | used | Sells up to 8 logo slots |
| H4 | S-R4-329 | magicui.design, 21st.dev, sitemaps | Magic UI; 21st Labs | undated | A | used | No program found |
| H4 | S-R4-330 | originui.com (now coss ui), coss.com | coss.com | undated | A | used | Rebrand |
| H4 | S-R4-331 | radix-ui.com | WorkOS | undated | A | used | "Made by WorkOS" |
| H4 | S-R4-332 | v0.app/pricing | Vercel | undated | A | used | Student offer |
| H4 | S-R4-333 | docs.github.com about-github-sponsors; personal-account setup | GitHub | undated | A | used (duplicate) | India supported |
| H4 | S-R4-334 | 11 WebSearch queries | various | n/a | n/a | URL finders only | press and third-party results rejected |

### Helper H5: AI coding tools and other routes (S-R4-400 to 497), 18:59-19:10
| time | S-id | URL | publisher | published/updated date | tier | verdict | what was taken |
|---|---|---|---|---|---|---|---|
| H5 | S-R4-400..412 | github.com/orgs/{getcursor, anysphere, cursor, Exafunction, cognition-ai, cline, Kilo-Org, continuedev, zed-industries, warpdotdev, replit, sourcegraph, Factory-AI}/sponsoring | GitHub | live | A | used | Public sponsorship counts (Zed 1, Replit 4, Warp 26 past; others 0) |
| H5 | S-R4-413..425 | opencollective.com/{cursor, anysphere, windsurf, codeium, cognition, cline, kilo-code, continue, zed, warp, replit, sourcegraph, factory-ai}.json | Open Collective | live | A | used / 7 failed (404) | Profile existence |
| H5 | S-R4-426 | api.opencollective.com/graphql/v2 | Open Collective | live | A | used | Donation history (Sourcegraph 31 projects $41.8k; Warp $14.3k to Neovim) |
| H5 | S-R4-427..429 | cline.bot/oss-grant, forms.gle, docs.google.com form | Cline | undated | A | used | Form open |
| H5 | S-R4-430 | cline.bot/blog/5m-installs-1m-open-source-grant-program | Cline | 2026-01-30 | A | used | $1k-$10k credits; rolling (lead re-checked: S-R4-652) |
| H5 | S-R4-431 | cline.bot/blog/clawcon-sf-... | Cline | 2026-02-10 | A | used | No status update |
| H5 | S-R4-432 | kilo.ai/oss | Kilo | undated | A | used | Tiers (5 Enterprise seats up); Kilo Code Reviews on public PRs; rolling (lead re-checked: S-R4-651) |
| H5 | S-R4-433 | cursor.com/ambassadors | Cursor | undated | A | used | Ambassador program for individuals |
| H5 | S-R4-434 | cursor.com/blog/marketplace | Cursor | 2026-02-17 | A | used | Plugin marketplace submissions |
| H5 | S-R4-435 | Kilo-Org/kilo-marketplace CONTRIBUTING.md | Kilo | undated | A | used | PR process for skills, MCP, modes |
| H5 | S-R4-436..437 | docs.windsurf.com, docs.devin.ai MCP page | Cognition | undated | A | used | MCP store, no public submission |
| H5 | S-R4-438 | devin.ai/blog/windsurfs-next-chapter | Cognition | 2025-07-14 | A | used | Acquisition context |
| H5 | S-R4-439 | devin.ai/blog | Cognition | Sep 2026 | A | used | "Devin Desktop" |
| H5 | S-R4-440 | windsurf.com | Cognition | live | A | used | Redirects to devin.ai/desktop |
| H5 | S-R4-441 | docs.warp.dev/.../open-source-partnership | Warp | n/a | A | failed (redirects to Contributing) | nothing |
| H5 | S-R4-442..444 | warp.dev/{open-source-partnership, oss, open-source} | Warp | n/a | A | failed (404) | nothing |
| H5 | S-R4-445 | factory.com/oss | Factory | undated | A | used | Free tool access for OSS contributors; no amounts |
| H5 | S-R4-446 | ampcode.com/news/amp-free | Amp | 2025-10-15 | A | used | Amp Free paused |
| H5 | S-R4-447 | continue.dev/oss | Continue | n/a | A | failed (404) | nothing |
| H5 | S-R4-448..451 | GitHub API: cline/mcp-marketplace, Kilo-Org/kilo-marketplace, cursor/plugins, zed-industries/extensions | GitHub | 2026-09-23 | A | used | Repos active today |
| H5 | S-R4-452 | hub.continue.dev | Continue | n/a | A | failed (no connection) | nothing |
| H5 | S-R4-453 | continue.dev | Continue | undated | A | used | Acquired by Cursor |
| H5 | S-R4-454 | cursor.com/marketplace/publish | Cursor | live | A | used | Publish page exists |
| H5 | S-R4-455 | zed.dev/docs/extensions/mcp-extensions | Zed | live | A | used | MCP extensions |
| H5 | S-R4-456 | Wikipedia API, Cursor_(company) | Wikipedia | live | C | used as secondary only | Ownership note (not cited in doc) |
| H5 | S-R4-457 | sequoiacap.com/oss | Sequoia | undated | A | used | OSS Fellowship: living costs 6-12 months, no equity, worldwide, rolling, needs adoption |
| H5 | S-R4-458 | ycombinator.com/faq | YC | undated | A | used | Solo and international founders; $500k |
| H5 | S-R4-459 | ycombinator.com/apply | YC | live | A | used | W2027 deadline Nov 2, 2026 |
| H5 | S-R4-460..462 | a16z.com open-source AI grant posts | a16z | 2023-08-30 to 2025-06-26 | A | used | Third batch Jun 2025; no application link |
| H5 | S-R4-463 | mercatus.org/emergent-ventures | Mercatus | undated | A | used | India track; apply link (lead re-checked: S-R4-653) |
| H5 | S-R4-464 | zfellows.com | Z Fellows | undated | A | used | $10k, 1 week |
| H5 | S-R4-465 | heavybit.com | Heavybit | (c) 2026 | A | used | $500k-$10M, company only |
| H5 | S-R4-466 | runacap.com/ross-index | Runa Capital | 2026-07-08 | A | used | Quarterly index, visibility only |
| H5 | S-R4-467 | surge.peakxv.com | Peak XV | (c) 2026 | A | used | Apply live, India/SEA |
| H5 | S-R4-468 | antler.co/location/india | Antler | undated | A | used | Next residency "soon" |
| H5 | S-R4-469 | neo.com/accelerator | Neo | n/a | A | failed (no content) | nothing |
| H5 | S-R4-470 | oss.capital | OSS Capital | undated | A | used | Commercial OSS companies only |
| H5 | S-R4-471 | fossunited.org/indiafoss/2026 | FOSS United | 2026 | A | used | 26-27 Sep 2026, Bengaluru; CFP closed |
| H5 | S-R4-472 | fossunited.org/events/timeline | FOSS United | live | A | used | No FOSS Hack 2027 yet |
| H5 | S-R4-473 | fossunited.org/fosshack/2026 | FOSS United | Mar 2026 | A | used | Ended; INR 5L |
| H5 | S-R4-474 | sessionize.com/figmacallforspeakers | Figma | 2022 | A | rejected (stale) | nothing |
| H5 | S-R4-475 | config.figma.com/call-for-speakers | Figma | n/a | A | failed (404) | nothing |
| H5 | S-R4-476 | config.figma.com | Figma | 2026 | A | used | Config India 15 Oct 2026, in-person closed, virtual free |
| H5 | S-R4-477 | intodesignsystems.com | Into Design Systems | 2027 | A | used | AI Design Systems Conference Mar 10-11, 2027; speakers announced |
| H5 | S-R4-478 | clarityconf.com | Clarity | 2025 | A | used | No 2026 dates |
| H5 | S-R4-479 | smashingconf.com | Smashing | (c) 2026 | A | rejected (no dates) | nothing |
| H5 | S-R4-480 | reactindia.io | React India | 2026 | A | used | Oct 29-31, 2026, Goa, final edition |
| H5 | S-R4-481 | jsconf.in | JSConf India | 2023 | A | rejected (stale) | nothing |
| H5 | S-R4-482 | designsystemsday.com | unknown | n/a | n/a | failed (no connection) | nothing |
| H5 | S-R4-483 | tailwindcss.com/plus | Tailwind Labs | live | A | used | Paid components; core MIT |
| H5 | S-R4-484 | penpot.app/pricing | Penpot | live | A | used | Cloud free or $7/editor/mo |
| H5 | S-R4-485..486 | plus.excalidraw.com, /pricing | Excalidraw | live | A | used | $6/user/mo |
| H5 | S-R4-487..488 | tldraw.dev/pricing, tldraw LICENSE.md | tldraw | live | A | used | Source-available; commercial license |
| H5 | S-R4-489 | cal.com/pricing | Cal.com | live | A | used | Teams $12/user/mo |
| H5 | S-R4-490 | plausible.io/self-hosted-web-analytics | Plausible | live | A | used | AGPL CE + paid cloud |
| H5 | S-R4-491 | shadcnblocks.com | Shadcnblocks | 2026-08-27 | A | used | $79 templates on free shadcn/ui |
| H5 | S-R4-492 | gnu.org/philosophy/selling-exceptions.html | FSF | n/a | A | failed (403/429) | nothing |
| H5 | S-R4-493 | web.archive.org copy of S-R4-492 (2026-09-19) | FSF | updated 2021-10-01 | A | used | Copyright holder sells exceptions to a copyleft license |
| H5 | S-R4-494 | fossa.com/blog/dual-licensing-models-explained | FOSSA | 2023-12-13 | B | used | Dual licensing needs copyleft; permissive gives no incentive to pay |
| H5 | S-R4-495 | devpost.com/api/hackathons | Devpost | n/a | A | failed (403) | nothing |
| H5 | S-R4-496 | floss.fund | Zerodha | (c) 2026 | A | used | $1M/year |
| H5 | S-R4-497 | fossunited.org/grants | FOSS United | 2026 | A | used | Grants and fellowships |
