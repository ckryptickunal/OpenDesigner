# Field plan: testing OpenDesigner with real people

September 2026. This is a test plan, not proof of demand. No outreach or posting has been done. It sits under [the product vision](PRODUCT-VISION.md): the vision says who OpenDesigner is for and why; this file says how to find out whether it works for them. Funding routes are in [SPONSORSHIP.md](SPONSORSHIP.md) and are not repeated here.

Checked against the repo and live sources on 2026-09-27. Owner decisions are marked **Kunal decides**. Everything else is a proposal.

## Where things stand

- **Evidence so far:** the engine works end to end. A fresh `sketch --name "Test App" --feel calm,modern` followed by `build` finishes and validates 408 tokens with no errors. That is a smoke test, not a user trial. It does not show that a host follows the interview as intended.
- **No outside use yet:** the repo was created on 2026-09-23 and had 0 stars on 2026-09-27. Adoption and willingness to pay are both unshown.
- **CI has never run:** GitHub Actions is disabled at the account level ([GITHUB-SETTINGS.md](GITHUB-SETTINGS.md)). The workflow tests only Python 3.11, although the docs promise 3.10 and newer.
- **Known failures, now fixed:** at `30f0429` the journey consent test failed 1 of 31, because it expected local wording in a web host. The standalone sub-skill zips also left out the eight visual templates. Both fixes merged on 2026-09-27 in #44 ([PR-RESOLUTION-LOG.md](../_coordination/PR-RESOLUTION-LOG.md)).

## The gate that comes first

A new person installs OpenDesigner, runs it on a real project and reaches a usable preview without help. Until five observed people can do that, fix that path and hold back wider distribution. Prioritize a failure seen by at least two people over any new export target.

## Who to test with

The vision names three use cases. Test all three. Do not narrow the product to one segment before observing anyone.

| Use case (from the vision) | A good tester | Disqualifies them for this round |
|---|---|---|
| Designers who use AI tools to build | Makes UI with Claude, Cursor or similar and has a live project | Only wants a visual canvas and never touches the files |
| Front-end engineers, especially on larger projects | Has repeated one-off CSS values and no maintained tokens | Already runs a token pipeline they are happy with |
| People polishing something they already built | Has a finished side project or startup UI that feels inconsistent | Their real problem is brand identity, not consistency |

**Round one:** first, Kunal's own from-scratch run with the journey log on (BRIEF requirement 18). Then five watched trials: two engineers, two designers and one project-polisher. A small Next.js and Tailwind v4 app is a practical *sample project*, because CSS and Tailwind are the most tested exports. It is a fixture, not the target audience.

**Before the demo, ask:** where did the last inconsistent screen come from? Which file owns the current choices? Who approves a changed button or color? Which AI tool actually edits your UI?

**During the demo, note:** time to install, time to the first useful preview, wrong assumptions, the moment they stop, and which files they would keep. Ask whether they understood the journey-log consent. Consent to a local log is not consent to share it.

**After a week, ask:** did they use `DESIGN.md` or `engine.py review` in a later edit? Success means a second voluntary use or a generated file they kept. Compliments and stars do not count. Never copy a tester's screenshots or code into public issues without their permission.

## Experiments, in order

1. **A reproducible sample.** Publish one small, permission-cleared app with a deliberately inconsistent UI, in a separate repo. Record its raw color and spacing values and a screenshot. Run the skill with no special prompting, then show the token, CSS and screen diff. A stranger should be able to reproduce it from the README. Do not imply that a designer approved the result. **Kunal decides:** which app, and approval to publish its UI.
2. **One unscripted pass per host.** Claude Code first, then a ChatGPT Project, Codex and Cursor. Use a fresh project each time. Record the first prompt, the number of questions asked, and whether `sketch` and `build` ran and the preview opened. Pass means the outputs exist, the generated CSS is imported, the app builds, the validator reports 0 errors, and contrast and focus are checked on the *rendered* app. Engine unit tests are not evidence of how a host behaves.
3. **Round trip is a gate, not a claim.** Import and export the Figma output on a throwaway file, then compare light and dark values, modes, aliases and names. The README already lists the Figma and Paper round-trip writers as planned. For Penpot, see below.
4. **Readability and trust.** Ask each tester to explain one generated choice from `DESIGN.md` and to find one deliberate override. If they cannot, shorten the explanation before adding more research.

### Penpot, specifically

Do not claim Penpot support yet. Two open Penpot issues matter:
- [penpot#9305](https://github.com/penpot/penpot/issues/9305): Penpot's importer expects a hex string, not the DTCG 2025.10 color object. The thread suggests a workaround: include the optional `hex` field inside the object. In the smoke test, every literal color OpenDesigner writes carries `hex`: all 178 primitives, plus the few semantic colors that are not aliases. So a one-way import *may* work already. Test that before saying so.
- [penpot#9307](https://github.com/penpot/penpot/issues/9307): Penpot drops `$extensions` on import and export. That is where OpenDesigner keeps each token's evidence and rationale. So Penpot can at best be a one-way preview, and OpenDesigner's own files must stay the source of truth.

**Kunal decides:** whether a tested one-way Penpot path is worth maintaining.

## Stop or change course if

- Testers praise the demo but do not keep the generated files. That calls for a product fix.
- Generated tokens break their existing build. That also calls for a product fix.
- A second AI session ignores `DESIGN.md`. That calls for narrower claims, not more channels.
- Round-trip claims cannot be reproduced. That also calls for narrower claims, not more channels.

After 10 trials, look for 3 people who kept a generated file and 2 who came back for a later edit. These thresholds are for choosing focus. They are not market benchmarks.

## Distribution, only as proof arrives

1. **Before anything public:** turn Actions back on and add Python 3.10 to the CI matrix. Publish the sample's before-and-after, an uncut 90-second recording from install to preview, a known-limits page, and the exact matrix of supported hosts and versions.
2. **First ten testers:** answer questions in GitHub Discussions. Add an issue template for a failed host run: host and version, install path, command, expected file, actual file, and no credentials or private design assets. Fix repeated onboarding failures before adding another export.
3. **First public examples:** post a Show HN or in design and developer communities only when a reader can reproduce the result in minutes, and only where the community's rules allow it. Share the fixture and its limits, not the card count or a generic "AI design" pitch.
4. **Tool partners:** once a one-way import is tested, invite Penpot or Tokens Studio users to challenge a small public fixture. Announce an integration only with the other project's explicit participation.

**Track weekly:** README visitors (GitHub Insights), clones and release downloads, voluntarily reported successful builds, outside repos using the outputs, returning users, time from issue to fix, and outside contributors. Stars are a discovery signal, not activation.

## Where testers might come from

These are public problem signals. None of these people asked for OpenDesigner, and none has endorsed it. Never message an issue author unprompted, and never pitch in a bug thread. Recruit through GitHub Discussions, opt-in community posts and referrals from maintainers. Never use scraped contact lists. **Kunal approves** every outgoing message, tailored to the person, on a channel where it is welcome.

| Signal (checked 2026-09-27) | What it shows | A fair first step |
|---|---|---|
| [Penpot community Tailwind token kit](https://community.penpot.app/t/tailwindcss-base-theme-design-tokens/8775) | People discussing token import, scale names and import order | Later, after a tested import: share the fixture and ask whether it helps |
| [penpot#9305](https://github.com/penpot/penpot/issues/9305), [#9307](https://github.com/penpot/penpot/issues/9307) (open) | Real interoperability gaps | Ask a narrow question only after reproducing it with OpenDesigner's output and a minimal fixture |
| [Tokens Studio#3775](https://github.com/tokens-studio/figma-plugin/issues/3775) (export to Figma creates no variables), [#3778](https://github.com/tokens-studio/figma-plugin/issues/3778) (aliases flattened on export) (both open) | Pain in the code-to-Figma step | Interview practitioners about reviewable exports. Never claim OpenDesigner fixes their plugin |
| [Tailwind discussion #19570](https://github.com/tailwindlabs/tailwindcss/discussions/19570) | Circular `@theme inline` output from a different plugin | Add a compile test showing OpenDesigner's Tailwind output avoids it. Publish only if it passes |
| [claude-code#60327](https://github.com/anthropics/claude-code/issues/60327), [#71523](https://github.com/anthropics/claude-code/issues/71523) (both closed by a bot for inactivity) | Requests to query a design system from Claude Code, and for `/design-sync` beyond React | A job to learn about, not a market. Claude Code's `/design-sync` targets React design systems for Claude Design. OpenDesigner does not replace it |

A useful ask looks like this: "I'm testing whether this makes your next UI edit more consistent. Would you try it on a throwaway branch and tell me where it breaks?"

## Money: hypotheses and red lines

**Kunal decides** all of this. These are options to test, not a plan.
- Keep the engine, formats, research and skills free under the existing licences.
- **First to test:** paid implementation help. This is a fixed-scope engagement to map a team's existing UI values, run the interview, wire up CSS or Tailwind, and hand over the system with a migration checklist. Set no public price until three discovery calls show the size of the work, who approves it, and what review costs. Track hours and rework on the first project.
- **Second to test:** training a team to maintain its own `DESIGN.md` and token pipeline. Both options sell time and accountability, not access to open code.
- **Only after returning users:** a hosted service for team collaboration or interactive MCP views. It would need a real data-retention and security model, kept apart from local-only journey logs. Promise no enterprise privacy or team accounts today.
- **Never:** let a sponsor or customer buy favorable design or tool recommendations.

## Four weeks

| Week | Deliverable | Evidence | Kunal decides |
|---|---|---|---|
| 1 | Turn Actions on, add Python 3.10, test a fresh zip install, write the sample-repo spec and a Tailwind build fixture. Kunal runs his own from-scratch test | CI runs, install output, journey report | Which sample app to use; turning Actions on |
| 2 | Five watched trials (two engineers, two designers, one project-polisher) | Consented notes: install minutes, first preview, kept files, top two failures | Introductions and the recruitment messages |
| 3 | Fix the top recurring failure; add a Figma round-trip fixture and a table of gaps; test the one-way Penpot import | A before-and-after trial and an import/export diff | Whether to keep a Penpot path |
| 4 | Public demo, and one paid-help discovery offer if the gate is met | Completed installs, returning edits, quality of inquiries | Offer scope and price; any public post |

## What changed from the earlier draft

An earlier agent-written draft (seven files, 2026-09-25) was reviewed before this version.
- **Kept:** the install-to-preview gate, the host acceptance checklist, success measured by kept files, the Penpot caution, the ethical recruiting rules, the stop conditions and the monetization red lines.
- **Dropped:** its product-vision section. It made small Next.js and Tailwind teams the first audience, which the founder's vision rejects as a limit. Designers who use AI tools were missing entirely. Those teams are now one sample fixture among three use cases.
- **Corrected:** "CI did not catch the zip bug" (CI has never run, because Actions is off). The two Claude Code issues are closed, not open. "DesignSync" is Claude Code's `/design-sync` and covers React only. The Penpot hex workaround applies, and OpenDesigner's output already includes `hex`.
- **Added:** Kunal's own first run with the journey log, and owner-decision markers throughout.

## Keeping this current

This is a living document. Update it, in the same change, when any of these happen:
- a trial, host pass or round-trip test produces a result (record it where the plan asks for it);
- an owner decision marked **Kunal decides** is made;
- a fact under "Where things stand" changes (stars, CI, known failures);
- a linked issue or discussion opens, closes or changes what it says.

`python3 tools/living_docs.py` checks the facts that change on their own and names this file when one moves. After updating the text, run it with `--accept`. Change the "Checked against" date at the top whenever facts are re-verified.
