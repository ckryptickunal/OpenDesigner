# VERIFICATION: merged result of the V1 check (2026-09-24)

Two fresh-context verifiers checked 161 claims against live official sources. Details: [`VERIFICATION-a.md`](VERIFICATION-a.md) (platforms and tools) and [`VERIFICATION-b.md`](VERIFICATION-b.md) (standards, values, studies, funding). Sources: [`traces/V1-trace.md`](../traces/V1-trace.md) (S-V1a-001 to 086, S-V1b-001 to 091).

| Verifier | Checked | Confirmed | Partly right | Wrong | Unverifiable |
|---|---|---|---|---|---|
| V1a, platforms and tools | 78 | 65 | 11 | 1 | 1 |
| V1b, standards, values, studies, funding | 83 | 69 | 8 | 4 | 2 |
| **Total** | **161** | **134** | **19** | **5** | **3** |

**What happened next (session "V1 fix").**
- 49 corrections were applied to `research/`, `benchmarks/`, `sources/` and `synthesis/`. Each corrected claim now carries its verification source id, for example [S-V1b-025].
- Five Decision Cards changed (DC-L02-09, DC-L02-13, DC-L03-26, DC-L13-08, DC-L13-13). `cards.json` was re-exported and the decision graph rebuilt; its edges did not change.
- 8 corrections waited for F1, the session rewriting `README.md` and `docs/`. Session "U4a docs" applied them on 2026-09-24 (row 24b only in part; see its status). 3 wait for Kunal.
- The table also carries a few claims that were confirmed but needed a small update, such as the "press-reported" tag on iOS 26.1.
- The 3 unverifiable claims:
  - Google joining Agent Plugins (L18:34, already marked "?", left as is).
  - The route for applying to a FOSS United fellowship.
  - Emergent Ventures' region menu.

Status key: **applied** = changed in this session; **pending F1** = in files the F1 session owns right now; **pending Kunal** = needs a decision or an action only the owner can take.

## Every wrong or partly-right claim, and the fixes

| # | Verdict | File:line | Correction | Source | Status |
|---|---|---|---|---|---|
| 1 | wrong | research/L02-typography.md:19, :215 | 14 x 1.125^n rounds to 16, 22, 28, 32, 36, 45, **58** (14 x 1.125^12 = 57.54). Material's 57 and 24 are each off-formula by 1 | S-V1b-025 | applied |
| 2 | wrong | synthesis/ONTOLOGY.md:674; synthesis/ontology.json:139 (`found.space`) | The 4-64 ladder appears in 17 of 22 published scales, but only **13 of 22** use a 4px base. "Plus 0 and 2" dropped (SLDS and Radix have neither) | S-V1b-080 | applied |
| 3 | wrong | research/L17-how-systems-get-made.md:184 | zeroheight 2026: more than 10 people is **14%** (10-15 6%, 16-20 4%, 20+ 4%), not 12% | S-V1b-048 | applied |
| 4 | wrong | research/L18-ai-first-distribution.md:32, :448; synthesis/OPENDESIGNER-SPEC.md:180; synthesis/OPENDESIGNER-SPEC.s1d-draft-b.md:97 | "since 2026-09-02" dropped. The Code tab renders MCP App widgets; the changelog added them to third-party-platform builds on 2026-08-25 as "already available in the standard app". The standard app's date is not documented | S-V1a-022 | applied |
| 4b | wrong | docs/SPEC.md:182 | Same fix as row 4 | S-V1a-022 | applied (U4a docs, 2026-09-24) |
| 5 | wrong | docs/SPONSORSHIP.md:17 | The repo is **public** (still 0 stars) | S-V1b-001 | applied (U4a docs, 2026-09-24) |
| 6 | partly | research/L18:24, :443 | Cowork and chat **began** merging on 16 Sep 2026: Pro and Max first, then Team and Free | S-V1a-002 | applied |
| 7 | partly | research/L18:447; research/L16-visual-tooling-for-engineers.md:176 | Claude Design in conversations and Claude Code is a **beta on paid plans**, off by default on Enterprise | S-V1a-003 | applied |
| 8 | partly | research/L11-process-governance.md:455 | "Research preview" at launch (Apr 2026); **beta since Sep 2026** | S-V1a-003 | applied |
| 9 | partly | research/L18:48 | The claude.ai Help Center caps `description` at 200 characters for uploaded skills (the open spec allows 1,024) | S-V1a-009 | applied |
| 10 | partly | research/L18:70 | The 2026-09-02 changelog entry for org-plugin skills in Chat is in the 3P section, so it dates third-party-platform builds | S-V1a-022 | applied |
| 11 | partly | research/L18:63 | The Bedrock and telemetry-off CLAUDE.md-only fallback applies only before v2.1.281 | S-V1a-075 | applied |
| 12 | partly | research/L07-tokens-figma.md:120 | Extended collections: Enterprise plan; anyone with can-edit access (no seat type stated), not "Full seat" | S-V1a-041 | applied |
| 13 | partly | sources/COMMUNITY-SIGNAL.md:261; sources/SOURCE-REGISTRY.md:16, :56 | paste-dsys.com is an **unaffiliated fork**, not Paste's new home. Registry row 30 is now tier C, REJECT | S-V1a-052 | applied |
| 14 | partly | research/L17:953 | Lovable made design systems available on **all paid plans** on 19 Aug 2026; npm-package wrapping stays Enterprise-only | S-V1a-057 | applied |
| 15 | partly | research/L16:230 | tweakcn has **about 46 controls** (32 color tokens, 3 font pickers, letter spacing, 10 sliders), not about 40 | S-V1a-067 | applied |
| 15b | partly | docs/FAQ.md:146 | Same: "about 40 token inputs" should say about 46 controls | S-V1a-067 | applied (U4a docs, 2026-09-24) |
| 16 | partly | research/L17:17, :131, :234 | NN/g **tested 14 tools** in 3 categories; the Oct 2025 article shows outputs from 10 | S-V1a-069 | applied |
| 16b | partly | docs/FAQ.md:152 | "NN/g's study of 10 AI design tools" should say "NN/g's evaluation of AI prototyping tools (14 tested)" | S-V1a-069 | applied (U4a docs, 2026-09-24) |
| 17 | partly | research/L03-space-layout.md:508 | The px = dp / pt note and the SHOULD-convert sentence are **already in 2025.10**; the Sept 2026 draft keeps them | S-V1b-002 | applied |
| 18 | partly | research/L02:582, :289 | Issue 102 is "Typography type feedback" on the whole typography type, not lineHeight alone (:289 had the same scope error) | S-V1b-002 | applied |
| 19 | partly | benchmarks/L09-benchmark-matrix.md:61, :651; benchmarks/systems/material-3.md:11; sources/COMMUNITY-SIGNAL.md:96 | The latest Compose Material3 alpha is **1.5.0-alpha29** (2026-09-23) | S-V1b-035 | applied |
| 20 | partly | research/L04-shape-depth-motion.md:10, :34; synthesis/ONTOLOGY.md:893, :901, :911, :920; synthesis/ontology.json:163-166 | Carbon v12 is **unreleased, behind the `enable-v12-release` flag**. There is no v12 beta; the latest release is v11.117.0 | S-V1b-044 | applied |
| 21 | partly | benchmarks/L09:213 | Fluent 2's ramp stops at 32, so it lacks 40, 48 **and** 64. The 17-of-22 count stands | S-V1b-074 | applied |
| 22 | partly | research/L18:188 | Sanity: the **JSON docs alone** took Sonnet 4.6 from 20% to 90%; code chunks raised it to 93%, and chunks plus lints to 100% | S-V1b-050 | applied |
| 23 | partly | research/L13-ux-laws-heuristics.md:17, :69 | Ghibellini and Meier (1 Jul 2025) analyzed **59 publications**: 39 on Zeigarnik, 21 on Ovsiankina | S-V1b-053 | applied |
| 24 | partly | research/L17:14 | The 207-block count is dated (ONTOLOGY.md, 23 Sep); `ontology.json` now has 211 non-builder leaves, and its `provenance` tags classify them differently | S-V1b-091 | applied |
| 24b | partly | docs/HOW-IT-WORKS.md:44-52; README.md:100; docs/SPEC.md:9, :235; docs/GLOSSARY.md:418; docs/RESEARCH.md:47 | Same 207 / five-class counts. Reword after row 24c is decided | S-V1b-091 | applied (U4a docs, 2026-09-24) in README.md, docs/HOW-IT-WORKS.md and docs/RESEARCH.md with the `ontology.json` counts (275 nodes; 211 blocks: 156/30/23/2), and as a dated note in docs/SPEC.md:9, :235. Still open: docs/GLOSSARY.md:418 (generated from synthesis/glossary.json), synthesis/OPENDESIGNER-SPEC.md:7, :233, and the choice in 24c |
| 24c | partly | L17 classification (207 blocks: 135/31/29/7/5, with owner input) vs `ontology.json` provenance (211: 156/30/23/2, no owner input); also synthesis/OPENDESIGNER-SPEC.md:7, :233 and synthesis/glossary.json | Choose which classification is canonical, then reconcile the counts everywhere | S-V1b-091 | decided by orchestrator 2026-09-24 (DECISIONS.md): ontology.json is canonical; F1 adds the fifth class 'owner input' there and fixes OPENDESIGNER-SPEC.md :7/:233 and glossary.json |
| 25 | confirmed, update | research/L04:14, :304, :650, :678; benchmarks/L09:652 | The iOS 26.1 Clear/Tinted option is now on Apple's own page; the "press-reported" caveat is gone | S-V1b-021 | applied |
| 26 | confirmed, update | research/L13:338, :428 | WCAG 3.3.4 (AA) and 3.1.5 (AAA) now cite the Recommendation instead of [inferred] | S-V1b-006 | applied |
| 27 | confirmed, update | docs/SPONSORSHIP.md:31, :50 | Add: the first GitHub Sponsors payout comes 60 days after the first sponsorship; Stripe Connect pays on the 22nd whatever the balance | S-V1b-057 | applied (U4a docs, 2026-09-24) |
| 28 | answered open item | docs/SPONSORSHIP.md:231 | Resolved: Stripe Connect has no minimum payout (Additional Terms 3.3) | S-V1b-057 | applied (U4a docs, 2026-09-24) |
| 29 | answered open item | docs/SPONSORSHIP.md:240 | Resolved: Cline's blog names solo developers as a target | S-V1b-063 | applied (U4a docs, 2026-09-24) |
| 30 | unverifiable | docs/SPONSORSHIP.md:71 | The FOSS United fellowship page shows no application route | S-V1b-060 | pending Kunal |
| 31 | unverifiable | docs/SPONSORSHIP.md:224 | Emergent Ventures' region menu: only the applicant can open the form | n/a | pending Kunal |

Optional notes not applied:
- research/L11:14: "biggest barrier" could read "top reason systems are not well adopted" [S-V1b-048].
- research/L08:56: the Radix release list could add 1.6.0 and 1.6.4-1.6.7 [S-V1a-048].
- `claude plugin validate` warns that the root `CLAUDE.md` is not loaded for plugin users [S-V1a-030].

Checks after the edits:
- `jev_nav.py check`: 0 files with dangling references. Its pattern matches only `S-L*` ids, so the 22 S-V1 ids cited above were checked against `traces/V1-trace.md` by hand, and all are logged there.
- `build_data.py --check`: clean. The fields that changed are not among those it copies into the generated files, and no line numbers moved.
