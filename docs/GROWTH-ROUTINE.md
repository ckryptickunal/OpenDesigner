# Release growth routine

The site, the README and the files crawlers read (robots.txt, llms.txt, llms-full.txt, the sitemap, the structured data, the titles and descriptions) go stale quietly. Each new page or feature makes it worse. Run this routine at every release and once a month, so people and answer engines keep finding what OpenDesigner does today.

It has two halves. A script checks what a rule can settle. A person (or an agent with a browser) does the rest: asking ChatGPT and Perplexity the questions people ask, and deciding the fixes. The method behind the second half is the search skill's: `skills/opendesigner-search/SKILL.md`, `references/probe.md` and `references/fixes.md`.

## When
- **Every release:** after the tag and the GitHub Release, once the site is built from that commit.
- **Every month:** the whole routine, including the probe. Add a row to the trend table even when nothing changed.
- **After a feature page lands:** steps 1 and 2 only, so its question shows up in llms.txt.

## 1. The automatic checks

```
python3 site/build.py
python3 tools/growth_check.py
```

`growth_check.py` reads `site/dist` and the README, offline. It fails on:
- any `search.py audit` error (it reports warnings as well);
- robots.txt blocking a search or answer bot. Training bots (GPTBot, ClaudeBot, Google-Extended) are Kunal's choice, and today they are allowed;
- a built page missing from the sitemap, or a sitemap address with no page;
- llms.txt without its questions section, or a docs page missing from llms-full.txt;
- a README fact that no longer matches the repo: the version, the number of library parts, the number of skills.

It warns when the README's opening never names the category ("design system", "Claude Code", "Cursor", "design tokens"). Engines quote a repository's first lines when they answer "which open-source tool" questions. Its tests: `python3 tools/test_growth_check.py`.

## 2. llms.txt and the page words

- `LLMS_QUESTIONS` in `site/build.py` turns the questions below into llms.txt's first section, each linked to the page that answers it.
- A question about a feature that hasn't shipped names the page it needs as a third item. It stays out of llms.txt until that page is built, so nothing on its way is claimed.
- When a new page answers a question, add its path there.
- Titles (`seo_title`), descriptions and FAQ answers live in each page's front matter in `site/docs/`. Perplexity searches the question word for word, so a page whose title says the question in the asker's words is the one it finds.

## 3. The answer-engine probe (monthly)

1. Use a browser you can see, logged out: chatgpt.com and perplexity.ai.
2. Ask each question below by hand, word for word, one new chat each. Never sign in or solve a CAPTCHA, and never call an engine's endpoints from a script. When several tabs run at once, keystrokes can leak between them: check the sent question matches before reading the answer.
3. Record, per question:
   - the searches it shows;
   - the pages it read or cited, ours first;
   - who it named, in order;
   - what it said about us.

   What each engine exposes:
   - **ChatGPT, logged out:** the conversation stream the page loads (`conversation/updates` in the browser's request list) lists every page it read, with titles (`searchSources`), and the links in its answer (`approvedUrls`). It shows "Searched N websites" but not the words, and for many how-to questions it doesn't search at all.
   - **Perplexity:** the thread data the page loads (`/rest/thread/<id>`) has its searches and sources.
4. Save the raw notes in `_coordination/plans/<date>-answer-engine-probe.md`. That folder is private to the maintainer's Mac, and the notes quote the engines.
5. Add one row per engine to the trend table, then take each miss through `fixes.md`.

Keep the wording fixed so runs compare. A reworded question gets a new id.

## 4. By hand, at most one fetch per page
- `/robots.txt`, `/llms.txt` and `/sitemap.xml` on the live site return 200, and `opendesigner.vercel.app` redirects to `opendesigner.dev` (ChatGPT still read a page at the old address on 2026-11-13). Never poll the live site: one fetch per page.
- Ask Kunal for Search Console and Bing Webmaster numbers (clicks, impressions, pages indexed) and add them to the trend row.
- Off-site places the engines read (GitHub lists, skill and MCP directories, dev.to) are proposals only, each with Kunal's yes.

## What better means
Each item is measured the same way every run:
- **Named us:** more questions name or cite OpenDesigner, by engine. The brand questions (B1 to B3) must always find us.
- **Our pages read:** engines read our pages for category and how-to questions, not only for brand questions.
- **No regressions:** `growth_check.py` passes, and `search.py audit` has 0 errors and 0 warnings.
- **Search Console:** impressions and pages indexed hold or grow (from Kunal).

A question that moves from "no" to "yes" after a page went live is the evidence that page works. One that stays "no" for two runs needs a different fix, not the same one again.

## The questions

| id | use case | question |
|---|---|---|
| B1 | brand | What is OpenDesigner? |
| B2 | brand | What is opendesigner.dev? |
| B3 | brand | Is OpenDesigner free, and which AI tools does it work with? |
| D1 | build a design system with AI | How do I create a design system with AI? |
| D2 | build a design system with AI | Best AI tool to generate a design system for my app in 2026 |
| D3 | build a design system with AI | Open-source tool to create a design system for an app built with Claude Code or Cursor |
| D4 | build a design system with AI | Is there a Claude skill that builds a design system and checks color contrast? |
| D5 | build a design system with AI | How do I write a DESIGN.md file so my AI coding agent follows it? |
| V1 | fix a vibe-coded UI | How do I make my vibe-coded app look professional? |
| V2 | fix a vibe-coded UI | My app built with Lovable / Bolt / v0 looks generic. How do I fix the UI? |
| V3 | fix a vibe-coded UI | How do I audit an existing web app for inconsistent spacing, colors and fonts? |
| V4 | fix a vibe-coded UI | Tool that finds hard-coded colors and spacing in my React code and replaces them with design tokens |
| T1 | tokens with Claude or Cursor | How do I give Cursor my design tokens so every screen matches? |
| T2 | tokens with Claude or Cursor | How do I generate design tokens with Claude Code? |
| T3 | tokens with Claude or Cursor | How do I create a Tailwind v4 theme from design tokens with AI? |
| T4 | tokens with Claude or Cursor | What is the DTCG design tokens format and which tools export it? |
| T5 | tokens with Claude or Cursor | How do I keep UI consistent across AI coding sessions? |
| G1 | generative UI | How do I add generative UI to my chatbot that uses my own design system components? |
| G2 | generative UI | How can an AI assistant render UI components instead of text, using my brand's components? |
| G3 | generative UI | What is generative UI and how do I make it match my design system? |
| M1 | MCP component library | Is there an MCP server that gives my coding agent a component library? |
| M2 | MCP component library | Free component library my AI agent can fetch and adapt to my design tokens |
| M3 | MCP component library | Component library built on design tokens that works with Claude Code |
| S1 | empty, loading, error states | How do I design empty states, loading states and error states for my app? |
| S2 | empty, loading, error states | Skeleton loader vs spinner: which should I use and when? |
| S3 | empty, loading, error states | Checklist of UI states every screen needs (empty, loading, error, partial) |
| A1 | the system as built | How do I see what design system my codebase actually uses? |
| A2 | the system as built | How do I extract a design system from an existing website? |
| R1 | user and stakeholder research | How do I do user research before designing a product with AI? |
| R2 | user and stakeholder research | How do I interview stakeholders before building a design system? |
| C1 | alternatives | Alternatives to UI UX Pro Max skill |
| C2 | alternatives | Alternatives to Figma's design system tools for developers using AI coding agents |
| C3 | alternatives | Style Dictionary vs Tokens Studio vs AI design token generators |
| C4 | alternatives | Open-source alternative to v0 or Magic Patterns for design systems |
| X1 | accessibility | How do I make sure my AI-generated UI meets WCAG 2.2 AA contrast? |
| X2 | search | How do I get my website cited by ChatGPT and Perplexity? |

## Trend table

| Date | Engine | Asked | Named us | Our pages read | Named first most often | Search Console (from Kunal) | Change since last run |
|---|---|---|---|---|---|---|---|
| 2026-11-13 | ChatGPT, logged out | 36 | 3 (B1, B2, B3: brand only) | 9 docs pages, all on B1 | GitHub repos and shadcn/ui | not asked yet | First run |
| 2026-11-13 | Perplexity, logged out | 18 (B1 D1 D2 D3 D5 V1 V3 T1 T2 T5 G1 M1 M2 S1 A1 R2 C1 X2) | 2 (B1, D3 via the GitHub repo) | about 9, on B1 | GitHub repos and dev.to posts | not asked yet | First run. One search per question, the question word for word |
