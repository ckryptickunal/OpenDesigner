---
title: Good practices: set your AI up to design well
seo_title: Good practices for designing with AI agents | OpenDesigner
description: What to give your AI agent before it designs: a reference library, competitors to study, a browser, image tools, keys in the right place and real content.
section: Guides
order: 7
updated: 2026-10-21
---

An AI agent designs about as well as the material it can reach. With only your prompt, it falls back on the look every AI tool produces. Give it references, competitors, tools and real content, and its results start to look like work people ship. OpenDesigner checks for each of these at the start of a session and uses whatever it finds without being asked. If something useful is missing, it suggests it once.

## Give it a reference library

The single biggest improvement is a library of real, shipped screens. [Mobbin](https://mobbin.com) is the one we use: if your plan lets you connect it to your AI tool, do (Mobbin's site explains how). With it connected, OpenDesigner:

- searches by the job, not the look ("web, shipment tracking table", then "logistics dashboard"),
- picks the three screens that solve your problem best, and builds on their structure, never their branding,
- uses the same three to score its own work before calling it done ([how quality is checked](https://github.com/ckryptickunal/OpenDesigner/blob/main/skills/opendesigner/references/quality.md)).

Mobbin's images stay on your machine. Its terms don't allow re-hosting them, so OpenDesigner never commits or publishes them.

## Name your competitors

Tell your agent which two or three products your customers compare you with. It will read their public pages (it asks before opening any), note what they all do, which is your baseline, and what none of them does well, which is where you can stand out. If you don't know, it proposes three and asks you to confirm.

## Let it look things up

Give it a browser it can drive: the in-app browser, Chrome or Playwright. It uses it to check best practice, read competitors and look at your own pages the way a customer sees them. Best practice comes first from OpenDesigner's [house standards](/docs/resources/), then from the open web, and it says which.

## Ask for directions, then choose

Ask for two or three real directions, built on your actual page, rather than one "final" design. Each is named by what it's good for ("denser for power users", "calmer for new customers"). You switch between them on the page and choose by looking.

## Connect image and video tools

When a page needs a picture nobody has, such as a hero scene, a product shot or a short film, a generation tool beats stock photos and decoration. [Higgsfield](https://higgsfield.ai/mcp) offers an official connector that agents like Claude can use with your own account. OpenDesigner also has its own skills for open-licence illustration and for painted art in your brand colours. Generating costs credits or money, so the agent says what it will make and asks before the first try.

## Keep keys in your project, not in the repo

Some tools need a key or a sign-in. Put keys in your project's git-ignored `.env` file or your AI tool's secrets settings, or use the tool's own sign-in. Never put them in OpenDesigner's repo or in a commit, and never paste them into chat. If a key is missing, OpenDesigner tells you the variable name to add. It never asks you to send it the key.

## Give it real content

Real logos, screenshots, numbers and customer names lift a design more than any style choice. A placeholder logo or "10,000+ teams" makes even a careful layout look like a template. OpenDesigner asks for these early, and it won't invent proof you don't have.

## Expect a quality bar

OpenDesigner doesn't call a design finished just because its checks pass. It scores the result on nine lines, from "fits the job" to "shown well", against three shipped products. Anything below 4 out of 5 gets fixed before you see it, or you get told exactly what's needed from you. Expect a short scorecard in its report, or a plain note that it couldn't compare.
