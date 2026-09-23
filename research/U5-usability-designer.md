# U5 usability test: designer persona (Meera)

Session "U5 designer", 2026-09-24. The tester played both roles. As the model, it followed `skills/opendesigner/SKILL.md`, `rules.md`, `zoom.md`, `hooks.md`/`hooks.json`, `guardrails.md`, `improve.md`, the stage files and `opendesigner-extract/SKILL.md`. As Meera, it played a senior product designer building a personal-finance app ("Ledgerly") for web and native iOS. She has a fixed brand color (#1F6F5C), a Söhne licence for web only, a logo still with an agency, and no illustration. She switched the voice to designer and used Stripe as her reference.

The scratch project was a bare Next.js `package.json` plus `src/`, kept in the session scratchpad and never in the repo. Every engine, journey, extract and browser command below was actually run: engine 1.0.0, skill 0.1.0, Python 3.10.11. Stripe was read live with `read_page.js` in the browser pane (two public pages, no login). The visuals were rendered as local pages (`preview.html`, the `palette` template through `show.py`) and inspected in a browser.

## Result in one paragraph
A designer gets a complete, exportable system quickly. The consent text, the identity firewall and the asset hooks behave well: Stripe's accent, typeface and logo were never carried over, and the missing illustration got honest, licence-accurate paths. Three things break Meera's trust.
- **Her brand hex never reached the primary button.** Her feel words (serious, minimal, premium) pushed Colorfulness to 0, the monochrome setting, and that turned the primary button near-black. Before `keep-hex`, the whole accent ramp came out gray.
- **Answers at the defined level did nothing.** She answered 10 color questions and the tokens did not change. Of the 28 defined-level answers, only body size changed a token.
- **The iOS output is wrong for her.** Her web-only Söhne licence cannot be expressed, so the Swift export embeds Söhne in the iOS app. The same Swift file used web text sizes (14, then 16 pt body).

Reference intake measured Stripe's body size backwards on both pages (the density proposals came out inverted), and DESIGN.md states several things that are not true. Validation passes with 0 errors.

## Short transcript
"M" = model, "Me" = Meera. Model lines are condensed. The Check column records the per-message notes the brief asked for:
- **V:** designer voice used
- **S:** reasoning sourced and credible
- **Vis:** visual offered where the host allows it
- **H:** hooks handled
- **Id:** identity kept out

| # | Who | Message (condensed) | Commands | Check |
|---|---|---|---|---|
| M1 | model | "I'll help set up Ledgerly's design system... Your repo is a fresh Next.js app, no tokens, fonts or brand files. 5 quick questions first... I keep a private log of your steps on this computer so I can make this faster for you. OK?" | `init --name Ledgerly` | 4 lines against the 3-line rule (F1). Log question word for word |
| Me1 | Meera | "Fine. I'm a senior product designer. Talk to me like one." | `consent on`, `set profile.voice "designer"`, `log help --kind voice_switch` | |
| M2 | model | "Designer voice from here. 1 of 5: what are you making, and which surfaces should the system cover?" | `log step_shown Q-scope-01` | V yes |
| Me2 | Meera | "Ledgerly, personal finance: accounts, budgets, transactions, bills, net worth. App first, marketing site later this year, email eventually." | `set context.product`, `pick Q-scope-01 [product-app,marketing,email]` | |
| M3 | model | "App = Operate, marketing = Persuade. 2 of 5 (Q-aud-01): A) everyday, comfortable: 16 px body, 36-40 px controls (Radix, shadcn), recommended; B) all day, compact (Polaris 13, Carbon 14); C) now and then, spacious (iOS 17 pt, GOV.UK 19)." | `log step_shown Q-scope-06, Q-aud-01` | V, S: real systems from the stage file, credible |
| Me3 | Meera | "A. Can tables be compact inside a comfortable app?" | `log help --kind explain` | |
| M4 | model | "Yes: a density mode (Q-space-09, detailed level; Carbon and Fluent use size props). Parked. 3 of 5: where does it run first?" | `log step_shown Q-plat-01` | V, S |
| Me4 | Meera | "Web and iOS at launch. iOS is native SwiftUI." | | |
| M5 | model | "4 of 5: pick 2-3 words: playful/serious, friendly/authoritative, minimal/rich, premium/everyday, modern/heritage, bold/quiet." | `log step_shown Q-brand-01` | |
| Me5 | Meera | "Serious, minimal, quiet. Honestly: calm." | `sketch ... --feel serious,minimal,quiet` gave **error: Unknown feel word ['quiet']**. The model re-offered the engine's word "deferential"; Meera took "premium" instead | F2 |
| M6 | model | "5 of 5: brand color or logo? A hex seeds the accent; if the exact hex must be on buttons I pin it." | `log step_shown Q-color-01, Q-brand-03` | |
| Me6 | Meera | "#1F6F5C, exact on primary buttons (brand guidelines). Logo: an agency is doing the wordmark, about 3 weeks. We licensed Söhne, web only. No illustration yet." | `sketch --audience regular --platforms web,ios --feel serious,minimal,premium --brand "#1F6F5C" --surfaces "app:operate,marketing site:persuade"`; `pick Q-color-01 keep-hex`; `lock raw.brandColor`; hooks: H-color have, H-logo commissioning, H-type have (web-only goes only in `--why`) | H: logo handled; font licence scope cannot be recorded (F21) |
| M7 | model | "Sketch built: tokens, CSS, Tailwind, Swift, Figma, DESIGN.md and a preview. Worth a look: 14 px body, and the type scale reaches 72 px because marketing is in scope. Stop, or zoom: Everything broadly (8 screens) · Color · Platforms." | preview opened in the browser | Vis yes (preview). DESIGN.md says the accent "marks buttons" |
| Me7 | Meera | "Why are my primary buttons black? I said the exact hex on primary buttons." | `log frustration --signal said` | F3 |
| M8 | model | "Your three words stacked Colorfulness to 0 (monochrome), which gives neutral-ink primary buttons (the shadcn pattern). A) brand hex on the primary action only; B) Colorfulness 20, still restrained." | `set raw.primaryActionColor "#1F6F5C"`: no effect (F4). Reverted; `set dials.colorfulness 20`; `build`; `feedback --kind bug` | V, S |
| M9 | model | The sharing text, word for word | `share-consent` | Collided with the bug fix above (F11) |
| Me9 | Meera | "Show me." Then: "Ask me each time." | `share --dry-run` (clean: ids, counts, no values), `share-consent ask` | |
| Me10 | Meera | "Everything broadly. But I want the calm of Stripe's product UI, not the marketing gradients." | | |
| M11 | model | "I'll read two public pages, no login: stripe.com and docs.stripe.com. Tag: inspiration, reinterpret (lessons, not looks). The dashboard is behind a login, so I won't see it. OK?" | | Id: consent and tag first, as the skill says |
| Me11 | Meera | "Yes." | `read_page.js` on both pages, `css_scan.py --from-json`, `engine.py intake` x2 | |
| M12 | model | The card: corners 1 px gives roundness 6 (home), 4 px gives 31 (docs); body 14 px gives density 78 (home), 16 px gives 35 (docs); shadow ladder at alpha 0.12 gives depth 56; cool slate neutrals; 4 px unit; 300 ms gives energy 73 (CSS only). Not taken: their accent `#533afd`, `sohne-var`, logo, copy | `log step_shown Q-ref-01` | Id: held. S: the numbers are wrong (F14, F15) |
| Me12 | Meera | "Your body sizes are swapped: home is 16, docs is 14. The 1 px radius is inline links; their buttons are pills. Take the depth, the cool neutrals and the 4 px unit. And Söhne is my own licence." | `log frustration --signal said`; 3 `set --set-by reference --source-ref ...`; 2 `feedback` | F14, F16, F17 |
| M13-20 | model | Broad screens, one per message. Q-dir-01 style: flat2 recommended, tonal, glass as a risk (premium on iOS, can hide content). Then Q-dir-02, Q-color-02, Q-type-01, Q-shape-01, Q-depth-01, Q-motion-01, Q-tool-01 | `pick` x8, `set raw.textFace "Söhne"`, `build`, `log level_complete broad` | Gallery values needed hand-made what-if copies. The 3 styles had identical palettes; they differed mainly in corner radius (F19) |
| Me13-20 | Meera | flat2, but glass on the iOS bars (no option for that); comfortable; accent; brand everywhere; subtle 6 px; ring plus shadow; productive; token file in git | | After Söhne: the Swift file now says `Font.custom("Söhne", ...)`. "That breaks my licence on iOS" (F21; frustration not logged at the time, tester miss) |
| M21 | model | "Send this session's anonymous report? Say "show me" to see it first." | | |
| Me21 | Meera | "Yes." | `share --yes`: "Reports aren't being collected yet... stays on this computer" | Honest |
| M22 | model | Color, defined: one question per message; asks for an example she dislikes; renders the `palette` template (restrained vs tinted, real ramps from what-if runs) | 10 `pick`s | Vis yes. No command records the disliked example (F32) |
| Me22 | Meera | Answers all 10 (restrained, hue-matched grays, workflow status, categorical charts, overlay hover, near-black). "Dislike: neon green on black trading apps." Then: "Nothing changed?" | tokens/ diff is **empty**; `log frustration`; workaround `set raw.flags.tintTowardBrand true`; `feedback` | F22, F23, F24 |
| M23 | model | Text, defined: Q-type-02, 03, 04, 08, 17 | 5 `pick`s, `build` | Only Q-type-08 (16 px) moved tokens. The Swift body went to 16 pt, not 17 (F22) |
| M24 | model | Components, defined: 13 questions. At empty states (Q-pattern-04) it asked the illustration hook, with the paths from `hooks.json`: honest text empty states; commission with a brief; unDraw, Open Peeps, Blush or Storyset with their exact terms; Recraft or Firefly with their plan caveats | 13 `pick`s; `set hooks.H-illus.status "placeholder"`; brief written to `opendesigner/briefs/H-illus.md` | H: well handled and sourced. DESIGN.md's policy line is wrong (F27) |
| Me24 | Meera | "Text empty states for v1; commission after launch. And I need an amount input and a transaction row, not only the 25 core parts." | | F29 |
| M25 | model | Finish: build, coverage, RATIONALE.md, "Add the snippet to AGENTS.md?" ("later"), summary; asked each-time share ("not this one") | `log session_end`, `report`; then `review` after planting a TransactionRow and `globals.css` | |

## Friction
Severity: 3 = breaks trust or gives wrong output; 2 = costs a turn or misleads; 1 = polish. R2 = engine owner.

| # | Step | What happened | Sev | Exact fix | File |
|---|---|---|---|---|---|
| F1 | Greeting | Intro line + "5 questions" line + "what I found" line + log question is 4 lines against a 3-line rule | 1 | In the first-time greeting, the found line replaces the "5 questions" line | `skills/opendesigner/references/rules.md` §1 |
| F2 | Sketch Q4 | zoom.md offers "bold or quiet", but the engine rejects "quiet" (it wants "deferential"). "calm" is in Q-brand-01 but is not a feel word. The error never reached the journey log | 2 | Accept aliases (quiet → deferential; calm → serious with lower energy), change zoom.md to the engine's words, and log a SystemExit in `sketch` as an `error` event | `references/zoom.md`; `synthesis/levers.json` macros; `engine.py` `cmd_sketch` (R2) |
| F3 | Sketch result | serious + minimal + premium stack Colorfulness to 0 (monochrome). Primary buttons became neutral ink (#242424). Before `keep-hex`, the CSS accent ramp was pure gray (step 9 `#757575`) although the brand was #1F6F5C. Also seen by the U5 engineer | 3 | When `raw.brandColor` is set, floor Colorfulness at 11 (the neutral band). With `flags.brandExact`, never use the monochrome primary branch | `engine.py` color roles (~line 1159) and macro stacking (R2); `synthesis/levers.json` macroRules |
| F4 | Fixing F3 | `raw.primaryActionColor` is ignored in the monochrome branch, and its ramp does not pin the exact hex (step 9 `#36826e`, not `#1f6f5c`) | 2 | Check `"action" in has` before the monochrome branch; pin the action ramp when brandExact | `engine.py` (R2) |
| F5 | Sketch DESIGN.md | It says "One accent color... marks buttons" while the preview rendered black buttons. Overview says "accent chroma 0.0 (HCT)"; Colors says "peak HCT chroma 34.72" | 2 | Build the Colors headline and the dial line from the resolved role map, not from intent | `engine.py` design-md (R2) |
| F6 | After any `set`/`pick` | DESIGN.md refreshes but `build/` (CSS, Swift) goes stale until `build`. SKILL.md says only "run generate and validate", so a literal model shows stale CSS | 2 | SKILL.md: "run `build`" after changes; `set` prints "exports are stale: run build" | `skills/opendesigner/SKILL.md`; `engine.py` (R2) |
| F7 | Q-aud-01 | The "regular" option promises 16 px body; the engine produced 14 px (the Operate work-tool default) | 2 | Make the option text say "16 px (14 px on Operate app screens)", or make regular + Operate give 16 | `synthesis/QUESTIONNAIRE.md` Q-aud-01; `engine.py` (R2) |
| F8 | Every build | The default sketch fails the engine's own advice: 11-12 text sizes and 17 styles, both flagged WARN, with no hint which setting fixes it | 2 | Cap display steps when `marketingSurfaces` is on, or name the fix (Q-type-10 / Q-brand-06) in the warning | `engine.py` `build_type_scale` + validate text (R2) |
| F9 | DESIGN.md zoom lines | Overview shows "defined (2 of 3)" right after the sketch, and Components "detailed (3 of 3)" after level-2 answers. It tells her to answer Q-brand-01, which the feel words already answered | 2 | Infer zoom from the `zoom` of answered questions in `questions.json`, not from a decision count; count `macros` as Q-brand-01 | `engine.py` zoom inference (R2) |
| F10 | DESIGN.md facts | "Audience: not recorded yet (Q-aud-01)" and "Base: not chosen yet (Q-comp-01)" appear although both were answered | 2 | Read `answers.Q-aud-01` and `answers.Q-comp-01` | `engine.py` design-md overview and components (R2) |
| F11 | Share ask | The rule forces the sharing block into the message right after the offer, which was the moment Meera reported the black-button bug | 1 | "Ask at the next pause after the result: after their question is settled, or before the next level starts" | `references/rules.md` §11 |
| F12 | Share dry run | Q-brand-03 shows as shown-but-not-answered because the logo was recorded as `hooks.H-logo.status` | 1 | Map `hooks.<H>.status` sets to the hook's question ids when tracking | `engine.py` track (R2) / `journey.py` |
| F13 | Reference capture | `read_page.js` cuts easings at the first comma (`cubic-bezier(0.25`), and samples the first 500 elements in DOM order (mostly the header on stripe.com) | 2 | Split timing functions with `/,(?![^(]*\))/`; sample visible elements across the viewport height | `skills/opendesigner-extract/scripts/read_page.js` |
| F14 | Reference fit | `fit_type` ignores counts: the home page's 16 px (460 elements) was read as base 14, giving density 78; the docs page's 14 px (162) was read as 16, giving density 35. The density proposals were inverted | 3 | Base = the most frequent size between 12 and 20, weighted by count; fit only the ratio | `extract/scripts/css_scan.py` `fit_type` |
| F15 | Reference fit | The accent was the first color in dict order (a slate `#3c4257`, C 0.037) and not `#5469d4` (x113). Radius was the most common across all elements (1 px inline links), giving roundness 6. The ring regex `0 0 0 1px` never matches computed `0px 0px 0px 1px`. A white fade glow (`0 0 64px 64px`, alpha 0.75) gave depth 80 | 2 | Sort accents by count x chroma; take radius from `a,button,input,[role=button]` only; normalise `px` before the ring test; skip white or zero-alpha shadows and spread ≥ blur | `css_scan.py` `analyse`; `read_page.js`; `engine.py` intake (R2) |
| F16 | Reference identity notes | "-apple-system is not carried" (a system font flagged as identity). "sohne-var is not carried" although Meera licenses Söhne herself; the skill has no rule for this | 2 | Skip system stacks. If the reference face equals the person's own `H-type` face, say "your own licensed face, not taken from the reference" | `extract/SKILL.md` §5; `engine.py` intake notes (R2) |
| F17 | Reference record | Accepted proposals stay `pending` in `state.references`. There is no way to mark ignored ones. DESIGN.md has no reference line (source, tag, closeness, taken and not taken), although extract §6 requires one. Closeness ("reinterpret") has no flag | 2 | `set --source-ref` marks the proposal accepted; add `intake --ignore <path>` and `--tag/--closeness`; add a References block to DESIGN.md | `engine.py` (R2); `extract/SKILL.md` §6 |
| F18 | Q-depth-01 | `ring-shadow` silently replaced the depth taken from the reference (56 → 25). It only says "also set" | 1 | Print "supersedes D-0022 (reference stripe-home)" | `engine.py` `cmd_set` (R2) |
| F19 | Q-dir-01 gallery | There is no engine way to fill `option-gallery` with real values. The model copied state into temp dirs, set the preset, generated and parsed CSS. With dials already set, flat2, tonal and glass had identical palettes and surfaces and differed mainly in control radius (2, 12, 6 px) and motion energy, so "directions differ in type, palette and shape" can't be met | 2 | Add `engine.py payload <template> [--preset X] [--set path=value]` that writes a filled payload without touching state. The gallery notes which dials are fixed by earlier answers | `engine.py` (R2); `SKILL.md` visual ladder |
| F20 | Per-platform intent | "Glass only on iOS bars" and "compact only in tables" have no options at levels 1-2 (Q-space-09 and Q-type-16 are level 3) | 1 | When `Q-plat-01` has 2+ platforms, show per-platform variants (Q-plat-05, Q-type-16) at level 2 | `synthesis/QUESTIONNAIRE.md`; `pacing.json` |
| F21 | Font licence | `H-type` can only be `have`; Q-type-02 offers yes / licence-only / no, with no "web only". With `raw.textFace "Söhne"`, `DesignTokens.swift` embeds `Font.custom("Söhne", ...)` in the iOS app. Validate is silent and Open Items does not mention it | 3 | Add licence scope to H-type (`web`, `app`, `desktop`) and a `web-only` option to Q-type-02; per-platform face (`raw.textFaceByPlatform`, iOS falls back to system); validate errors when an export uses a face outside its scope | `synthesis/hooks` source (`hooks.json`/`hooks.md`), `QUESTIONNAIRE.md` Q-type-02; `engine.py` export_swift, export_compose and validate (R2) |
| F22 | iOS type | Swift uses web sizes (body 14, then 16 pt), while Q-type-08's default says iOS 17 pt. On the system-font path Swift writes `Font.system(size: 14, weight: .regular)`, which does not scale with Dynamic Type (known SwiftUI behaviour; not run on a device), although the file header says fonts do | 3 | A platform type mode (iOS body 17 pt) by default when iOS is in scope. The system path uses text styles (`.body`) or `UIFontMetrics`/`relativeTo`, as the custom path already does | `engine.py` export_swift and type scale (R2) |
| F23 | Color, defined | 10 answers (Q-color-03, 04, 06, 09, 14, 15, 17, 19, 20, 21) changed nothing in tokens/ (empty diff). Same for Q-type-02, 03, 04, 17. Hue-matched grays needed an undocumented `raw.flags.tintTowardBrand`. Also reported by the U5 engineer and U5 student | 3 | Map these in `answer_effects` (09 → tintTowardBrand/warmth, 17 → contrastTarget, 19 → chart tokens, 20 → state layers, 21 → dark base, 15 → status ramps). `pick` prints "recorded only: no token effect yet" for the rest; stage files get "Dials:" lines | `engine.py` `answer_effects` (R2); `synthesis/QUESTIONNAIRE.md` |
| F24 | Hover on exact brand | With the hex pinned at step 9, hover (step 10 `#27705e`) is 1.02:1 against `#1f6f5c`, which is effectively invisible. Choosing Q-color-20 `overlay` did not change it | 2 | When a step is pinned, solve steps 10 and 11 relative to it (a minimum lightness difference), or apply `opacity.state.*` overlays when Q-color-20 is `overlay` | `engine.py` ramp solver (R2) |
| F25 | Finance needs | No chart tokens at all (Q-color-19 categorical-6-8 had no effect). Tabular figures (Q-type-06) come only at level 3 and produce no token | 2 | Chart palette plus diverging tokens; `font.numeric.tabular` token; ask Q-type-06 at level 2 for data or finance products | `engine.py` (R2); `synthesis/QUESTIONNAIRE.md` |
| F26 | Type details | The scale has odd sizes (11, 13, 16, 19, 23, 28, 33, 40, 48, 57, 69, 83) and button labels at weight 400. Dark neutral steps 8 and 9 are 1.04:1 apart (`#74847e`, `#758781`) | 1 | Offer snapping to 2 or 4 px (Q-type-09); labels 500 by default; set a minimum step distance in dark ramps | `engine.py` (R2) |
| F27 | Components DESIGN.md | "Contested policies" is mislabeled: "Validation timing" shows Q-form-01 (field style), and "Undo versus confirm" reads Q-state-06, so it stays "pending" although Q-form-05 was answered | 2 | Validation timing and disabled submit ← Q-form-02; undo vs confirm ← Q-form-05; add field style ← Q-form-01 | `engine.py` ~line 4140 (R2) |
| F28 | Illustration hook | Well handled, but the order of paths differs: hooks.md says designer → library → tool → none; hooks.json Q-img-04 says text states → commission → open sets → AI | 1 | Use one order in both | `synthesis` hooks source; `references/hooks.md` |
| F29 | Q-comp-02 | The core 25 lacks the domain parts a finance app needs (amount input, transaction row, stat/KPI, numeric table), and there is no interview path to add to the inventory | 1 | "Add product-specific components" follow-up that writes `components.inventory` | `synthesis/QUESTIONNAIRE.md`; `engine.py` (R2) |
| F30 | `review` | It missed JSX `borderRadius: 12` and `padding: "12px 16px"`. It suggested `--ds-color-bg-accent-bold` for a text color and `motion-duration-long-exit` for a hover transition (nearest number, wrong role). Also reported by the U5 engineer | 2 | Scan camelCase JSX and unitless numbers; suggest a token by the CSS property's role (text, background, border) and by transition purpose | `engine.py` `cmd_review` (R2) |
| F31 | Journey log | `review` after `session_end` opened a phantom session S002 ("2 sessions"). An area-level frustration was pinned to the last step shown (Q-color-21). Speed-ups were recommended from 1 sample | 1 | No auto session for review/validate right after `session_end`; allow `--area` without a step; hide speed-ups under n=3 | `journey.py`; `engine.py` track |
| F32 | Examples she dislikes | rules §3.6 says to ask for liked and disliked examples, but no command records them (`state.taste` exists and is undocumented) | 1 | Document `engine.py set taste.dislikes '[...]'` and show it in DESIGN.md | `references/rules.md` §3; `engine.py` (R2) |
| F33 | DESIGN.md prose | Python booleans leak ("native base text size: False"). A Compose (Android) file is exported for a web + iOS product | 1 | Word booleans; export only the platforms in scope unless asked | `engine.py` design-md and build (R2) |
| F34 | Designer voice | The glossary has both "density" and "Density" entries; "seed color" and "personality sliders" are missing. Every feel-word offset is `offsetsInferred: true`, so "why did three words make it monochrome?" has only an [inferred] answer | 1 | Merge the duplicate; add the terms; DESIGN.md dial lines say which offsets are inferred | `synthesis/glossary.json`; `synthesis/levers.json` |

**Counts:** severity 3: 5 · severity 2: 17 · severity 1: 12 (34 in all).

## What worked well
- **Designer voice with real sources.** Stage files and glossary designer lines give real systems and numbers (Radix, shadcn, Polaris 13 px, Carbon, GOV.UK 19 px, Material). They read as credible to a senior designer when a recommendation was questioned.
- **Identity firewall held on a hard case.** Stripe's `#533afd` accent, its `sohne-var` face, logo and copy were flagged automatically and never carried. Only structure was taken: depth model, cool neutrals, 4 px unit. Brand presence was never inferred.
- **Consent before fetching, and honest limits.** Two URLs were listed and approved, the login-only dashboard was declared off-limits, and motion was marked "CSS only".
- **Asset hooks.** The logo went to `commissioning` and was never faked. The missing illustration got four licence-accurate paths (unDraw's AI-training ban, Storyset's credit, Blush's no-resale, plan terms for Recraft and Firefly), a filled brief, and a `placeholder` status that shows in DESIGN.md's asset table and Open Items.
- **Accessibility floors.** Validate checked 152 color pairs across 12 mode combinations. It passes AA in light and dark with the exact brand hex, plus APCA advice and the 44 pt target note.
- **Exports a designer can use.** Figma variables have Light/Dark, Spacious/Comfortable/Compact and Standard/Reduced modes. There is a Tailwind v4 `@theme inline` file, rem sizes and a DTCG resolver.
- **Visual templates, once filled.** The `palette` template rendered real ramps with contrast numbers per step, light and dark, and a "Copy my choice" `OD:` line. `preview.html` showed real button states.
- **Consent flow.** The text was word for word. The dry run showed only ids and counts, with no colors, names or URLs. `share --yes` honestly said the report stays on this computer because nothing collects it yet.
- **Feedback loop.** `engine.py feedback` wrote 4 entries to `opendesigner/feedback.md` with pre-filled issue links; nothing was posted.

## Journey report (`journey.py report`, end of run)
```
2 sessions, 12 min in total. 42 steps taken: 42 answered, 0 skipped, 0 dropped.
Shortest path for what was covered: 41 steps, one per question; you took 42 (98% efficient).
Most frustrating: Q-color-01 (Do you have fixed brand colors, or should I...), 1 signal.
Top speed-up: Q-color-04: default kept 1 of 1 times and medium impact: auto-apply it and mention it in one line.
```
| Level | Reached | Answered | Finished | Steps / shortest |
|---|---|---|---|---|
| sketch | 7 | 6 | yes | 6 / 5 |
| broad | 8 | 8 | yes | 8 / 8 |
| defined | 28 | 28 | yes | 28 / 28 |

- **Frustration hotspots:**
  - Q-color-01: brand hex missing from the primary buttons
  - Q-ref-01: reference misread body size and radius
  - Q-color-21: defined color answers left the tokens unchanged. This was really an area-level signal (F31).
- **Help:** Q-aud-01 (explain) and one voice switch.
- **How answers were given:** option 28, default 10, free 4.
- **Also counted:** 0 errors (the "quiet" failure was not logged, F2), 9 exports, 1 review and 4 feedback notes.
- **Not logged:** the Söhne-on-iOS frustration (tester miss).
- **Timing is not meaningful:** the persona answered instantly.
- **Sessions:** "2 sessions" is really one session plus a phantom one (F31).

## Validation and review results
- **`engine.py validate`:** passes, 0 errors, 2 warnings and 5 notes.
  - Warnings: 12 text sizes (8-10 usual); 17 text styles (12-15 usual).
  - Notes: dark secondary text APCA Lc 55 and 54 (advice); smallest control 24 px, which needs a 44 px tap area; 14 unused scale steps; 10 asset hooks not asked yet.
  - Checked 152 color pairs, 12 mode combinations and 388 tokens.
- **`engine.py review`** (after adding `TransactionRow.tsx` and `globals.css`) found 5 hard-coded values:
  - `font-size: 15px`, `border-radius: 10px`, `box-shadow` and a 250 ms transition in the CSS
  - `#1F6F5C` in the TSX
  - It missed the TSX `borderRadius: 12` and `padding`, and gave two role-mismatched suggestions (F30). "DESIGN.md matches state.json."
- **Designer read of the outputs:**
  - The final `tokens.css` has the exact brand at `accent-light-9` and the primary action on it, teal-tinted neutrals, 6 px controls and 8 px containers, and a ring plus key shadow on `elevation.raised`.
  - Problems: an invisible hover (F24); no chart, status-workflow or tabular-number tokens (F25); odd type sizes (F26).
  - Wrong: `DesignTokens.swift` embeds Söhne on iOS at a 16 pt body (F21, F22).
  - DESIGN.md is readable and refreshed after every decision, but it states 5 untrue things (F5, F9, F10, F27, and the missing licence scope in Open Items).

## Top 5 fixes, in priority order
1. **Make the brand hex and every answer reach the output** (F3, F4, F23, F24).
   - With a brand color set, Colorfulness never drops into monochrome, and an exact hex always fills the primary action.
   - Every defined-level answer either moves tokens through `answer_effects` or `pick` says "recorded only".
   - A pinned hex gets visible hover and pressed steps.
   - Files: `engine.py` (R2), `synthesis/QUESTIONNAIRE.md`.
2. **Platform-aware type: licence scope, per-platform faces and iOS sizes** (F21, F22, F20).
   - H-type gets a scope (web, app, desktop), and Q-type-02 gets a `web-only` option.
   - Validate errors when Swift or Compose embeds a face the licence doesn't cover.
   - iOS gets a 17 pt body mode, and `Font.system` sizes scale with Dynamic Type.
   - Files: `engine.py` exports and validate (R2), the hooks source, `QUESTIONNAIRE.md`.
3. **Fix reference measurement before anyone trusts it** (F14, F15, F13, F17).
   - Weight body size by count; pick the accent by count x chroma; take radius from controls only.
   - Fix the ring regex and exclude glow shadows; stop cutting easings at the first comma.
   - Mark accepted and ignored proposals, and add a References line to DESIGN.md.
   - Files: `extract/scripts/css_scan.py`, `read_page.js`, `engine.py` intake (R2).
4. **Make DESIGN.md true** (F5, F9, F10, F27, F33).
   - The headline comes from resolved roles, and zoom levels come from the levels of the questions answered.
   - Audience and component base read from the answers, and the contested-policy mapping is fixed.
   - No Python booleans in the text.
   - Files: `engine.py` design-md (R2).
5. **A payload builder for visual-first choices** (F19, F6).
   - `engine.py payload <template> [--preset X] [--set k=v]` fills the gallery, palette, radius and type templates with real what-if values, without touching state.
   - SKILL.md says to run `build`, so exports never go stale.
   - Without this, the model hand-builds visuals or skips them, which undercuts BRIEF requirements 3 and 7.
   - Files: `engine.py` (R2), `skills/opendesigner/SKILL.md`.
