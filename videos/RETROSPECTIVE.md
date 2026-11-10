# Retrospective: the OpenDesigner explainer videos

October 7, 2026. Version 1 (`opendesigner-explainer/`) was judged cheap and AI-looking. Version 2 (`opendesigner-film/`) rebuilt it the way it should have been built from the start. This page says where I fell short and why, so the process can be fixed and not just this one video.

## The short version

I treated "make a video" as a video task, not as a design task. So I skipped the one thing this repo exists to do. I never made a design system for the video. I didn't research references. I didn't add a voice to something called an explainer. And I took "all checks passed" to mean "good". The look came from one social-preview image plus my own defaults, and my defaults are what AI slop is.

## Where I fell short, and why I made those choices

1. **No design system for the video.** I read the social preview, took its colors and fonts, and made up every other value: 27 font sizes, random radii, hand-picked easing. *Why:* the video skill I loaded (HyperFrames) has its own "house style" fallback, and I followed it rather than this repo's own rule ("Create a design system... use `opendesigner`"). Nothing told me a video counts as a surface, and I didn't ask myself.
2. **No reference research.** You use Mobbin throughout the workflow, and there's a taste poll built from real shipped screens. I used neither. *Why:* building felt faster than looking. Without references, "premium" falls back on my average idea of premium, which is the generic look.
3. **I ignored my own memory note.** A stored preference said to study the reference's actual motion first and to keep things restrained. I read it and didn't apply it.
4. **No voice.** I called the silence "deliberate" for an explainer. *Why:* I asked about format and review, not about sound, and then talked myself into the default.
5. **I trusted the linter.** v1 had 0 errors and 57 of 57 contrast passes. The audit then found 19 problems, including clipped letters in the brand name and a fake DTCG card. *Why:* a passing check feels like a finish line.
6. **I reviewed thumbnails.** I looked at 600 px contact sheets, where clipped descenders, touching letters and overflow can't be seen.
7. **I verified facts, not design.** I counted every number carefully. I didn't check that the drawings matched their own labels (a "10-step ramp" with two hues, a "0 to 32" radius that animated to 50).
8. **Slide-deck structure.** Eleven scenes, each "headline plus cards", with the same entrance and exit throughout, and 38% of the runtime frozen.

The fresh-eyes audit of v1 is in [opendesigner-explainer/AUDIT-v1.md](opendesigner-explainer/AUDIT-v1.md): 19 findings with timestamps and frames, and 20 reusable checks.

## What version 2 does differently

- **It runs on its own OpenDesigner system.** I ran `engine.py sketch` for the film (brand #e4572e; feel premium, confident, warm) and set the eight dials from your taste-poll profile. The film loads the generated `tokens.css`, and every color comes from it. The heading weight (650), the display letter spacing (−0.02em), the radii and the three easing curves are the engine's values. A written film layer multiplies the px tokens by 2.5 for a 1920 px frame watched on a phone. The system is in `opendesigner-film/system/`.
- **It's based on references.** Mobbin sections (Antimetal, Retool, Frontify, Base and others) showed that the premium ones lead with real product UI, use light display weights and leave a lot of empty space. The slop act copies the pattern they avoid: purple gradient cards.
- **It's a story, not slides.** Your idea: the film opens as AI slop. The narrator (OpenDesigner) then asks its questions about the film itself, and each answer fixes one layer on screen. The last act is the same film, full frame, on its own system. One object carries the whole story.
- **It uses real assets.** The panel shows the engine's real token values, file names, dial names and contrast ratios. The canvas shows a screenshot of the preview page the engine generated for this film.
- **It has a voice and captions.** 18 narration lines from Gemini TTS (`gemini-3.8-flash-tts`, voice Charon). Every line was transcribed and checked against the script, which caught the model reading its style instructions aloud. Captions run through the whole film.
- **It was reviewed at full size,** including after the fixes. That caught four more bugs: a status pill wrapping, file paths overflowing, stat labels hidden by a class-name clash, and a wrong file count ("11" where the folder holds 9).

## Gaps this exposed in OpenDesigner itself

These are recorded with `engine.py feedback` in `opendesigner-film/system/opendesigner/feedback.md`, each with a prefilled issue link. None was posted.

1. **No video, film or presentation surface.** One house standard requires light and dark values for every color role, and it blocked a dark-only film.
2. **A warning that never clears.** The feel-conflict warning (authoritative against friendly) stays after all eight dials are set explicitly.
3. **No viewing-distance scale.** The type scale stops at 95 px for desk viewing. A film needs a medium multiplier, so I wrote one by hand.
4. **`system-ui` as the font.** It renders differently on each machine. Renders that must look the same everywhere need a typeface you ship, and the engine never asks for one.

The biggest process gap is the first one in the list above. When someone asks for a video, deck or card, nothing sends the agent to `opendesigner` first. The new preflight skill now makes "system first" its step 1.

## What's still not right in version 2

A second fresh review used the new preflight skill. It found 2 severity-1 problems, and both are fixed:

- **Phone legibility.** My first film rule (tokens × 2.5) gave about 8 pt text on a phone, so I worked the maths again. Captions are now 56 px, panel text 40 to 62 px, and the panel is wider.
- **A stale claim.** "Seven skills" became wrong as soon as I added the preflight skill. The narration was regenerated: "seven more skills" plus the main one makes eight.

Its moderate findings are fixed too: captions over the cards, card overflow, highlights drifting from the voice, unlabelled contrast pairs, a repeated phrase, and a grid the cards didn't sit on. The full review is in [opendesigner-film/AUDIT-v2.md](opendesigner-film/AUDIT-v2.md).

Still open:

- **Held frames.** 32% of the runtime after the slop act is held for 1.5 s or more. The longest hold is 2.7 s, and each one sits under narration. The skill's guideline is 15%.
- **Panel labels.** They are 40 px: above the 40 px error floor, but under the 54 px target. The film inside the canvas is drawn at about 0.46 scale, so its text is small by design. The same frame is shown at full size in the last act.
- **The typeface.** Inter Tight was my choice, not yours. The engine's default (`system-ui`) can't render the same everywhere.
- **The dials.** The taste-poll dial values are estimates Claude made against shared anchors. No designer has checked them yet.
- **Sound.** There's no music bed or sound design yet.

## The fix that lasts

`skills/opendesigner-preflight/` is a new, portable skill. It has a 32-point checklist (system, type, layout, motion, truth, sound, process), a catalog of 33 real mistakes with how to catch each one, and a standard-library helper. The helper checks type scale, tracking, fonts that never load, small text and layout tweens, and measures a render's frozen time, black frames, audio and loudness. Run on v1, it reports 2 errors and 5 warnings (3 from the page, 2 from the render).
