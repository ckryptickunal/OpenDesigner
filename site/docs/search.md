---
title: Get found in search and AI answers
seo_title: "SEO, AEO and GEO: get found in search and AI answers"
description: How OpenDesigner checks a site for search and AI answer engines, asks ChatGPT and Perplexity a few questions by hand, and proposes page fixes.
section: Guides
order: 8
updated: 2026-11-07
---

Ask your AI to "do SEO" or "help us show up in ChatGPT", and OpenDesigner's search skill checks your site the way search engines and AI answer engines read it. It reports what it found with the evidence, proposes fixes, and changes nothing until you say yes.

{{figure:search-loop}}

## What it checks

It reads the pages your server sends, from a production build such as `dist/`:

```
python3 skills/opendesigner-search/scripts/search.py audit dist/ --base https://your-site.example
```

- **Who may read the site.** It checks robots.txt for each search bot, each bot that fetches a page for one person, and each training bot. Blocking a training crawler such as GPTBot is your choice, and doesn't remove you from ChatGPT search. Blocking OAI-SearchBot does.
- **Each page:** a canonical address, a title and description that fit in a result, one main heading, and text that is there without JavaScript.
- **Structured data** that matches what the page shows. FAQ markup that matches is fine. Google no longer shows FAQ results, but answer engines may still read the markup, so it stays.
- **The sitemap, llms.txt,** pages nothing links to, and images with no description or size.

## Asking the answer engines

The agent asks about six questions, by hand, logged out, in a browser you can see:
- what your product is;
- two or three questions your customers ask before they know you;
- one how-to question.

For each one it notes what the engine searched for, which pages it read, whom it named and what it expects to be asked next. Perplexity shows its searches. ChatGPT shows its sources but not its searches. Claude needs a sign-in, so it is skipped.

Then it turns that into page fixes:
- a page whose title and first sentence use the words people asked with;
- short answers to the follow-up questions;
- an honest comparison when a competitor comes first;
- a list of directories and roundups to be listed in.

Each fix waits for your yes. So does every submission anywhere off your site.

## What it never does

- It never invents a number, quote or review. Real facts with sources help AI answers use a page, but only facts you gave.
- It never repeats keywords or makes near-identical pages to rank. Google counts both as spam.
- It never runs queries by script, signs in to an engine or gets past a CAPTCHA.

It also says what it can't do, and what it needs from you instead: your Search Console data, keyword volumes, links from other sites. If you filled in a [site brief](/docs/zoom-levels/), its questions and page families are what the search skill aims for.
