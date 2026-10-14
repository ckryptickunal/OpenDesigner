# Showcase stress test: brief for every builder

We are doing two things at once:

1. **Making marketing material.** Every piece here may be posted on GitHub, X and Threads as "made with OpenDesigner". It has to be visually striking, the kind of work a top studio would ship. Generic, template-looking, "AI default" output fails this test, even if it is tidy.
2. **Stress-testing our own process.** Each piece must be made *through* OpenDesigner, end to end, the way a real user's agent would: references, then a design system from the engine, then the build, then checks. Every place the process helps, slows you down, misleads you or is missing something is a finding. Findings matter as much as the pictures.

## Hard rules

- **No real brand names, logos or products** anywhere in the pixels or copy. Invent a fictional brand, product and copy for every piece. Fictional customer logos are fine if they are invented wordmarks.
- **Every piece is a different direction.** Different domain, palette, type, layout idea, shape language and mood from every other piece in your set. Before you start, write all your directions down side by side and make sure no two feel related.
- **References give structure and quality, never identity** (AGENTS.md). Study real work on Mobbin (`mcp__mobbin__search_sections` for web sections, `mcp__mobbin__search_screens` with platform `ios` or `web` for app screens; load the tools with ToolSearch first). Never copy a layout one to one, never copy an exact brand hue, logo, photo or text. **Never save Mobbin images into the repo** (their terms forbid re-hosting). Cite references only by their `mobbin_url` in your notes.
- **Accessibility floors are locked:** WCAG 2.2 AA text contrast (4.5:1 body, 3:1 large text and UI parts), 24 px minimum targets (44 pt on touch), visible focus. Decorative text that carries no meaning is exempt, but say so.
- **Fonts:** only open-licence faces (SIL OFL or Apache), either installed locally (`ls ~/Library/Fonts`: Inter, Geist, Geist Mono, Manrope, Outfit, Sora, Playfair Display, Source Sans Pro are open) or loaded from Google Fonts with a `<link>` (exact families, any of the Google Fonts library). Never use trial, demo or commercial fonts you find installed (GT America Trial, Fontspring DEMO, Apercu, Calibre, Neue Haas, PP Neue Montreal and so on). Never write a font file into the repo.
- **Imagery:** prefer art made in code: SVG, CSS, canvas, generative patterns, gradients, shaders written as canvas 2D or WebGL. You may also use the `opendesigner-illustrate` skill (open-licence SVG illustrations recolored to your tokens) or the `opendesigner-paint` skill (painted art in code). No stock photos, no hotlinked images from the web. Photographs of fake people are not allowed.
- Stay inside your own folder. Do not edit anything outside `brand/showcase/<your category>/` except recording engine feedback (below). Do not commit or push.

## Type and color rules (added by the owner mid-run; they override anything above)

- **At most two fonts in one piece.** No extra mono for small labels unless the mono is one of the two and the label really is code or data. Never two faces inside one heading.
- **Use a real type scale with named roles,** following Apple's (HIG Dynamic Type) and Google's (Material 3) rules: display, H1 to H6 or headline/title, body, label, caption, with their minimum sizes (iOS: 11 pt minimum, 17 pt body; Material: 11 sp label minimum, 14 to 16 body). A web piece uses about 6 sizes at most, and no two sizes within 10% of each other. Write the scale you used in `notes.md`.
- **Titles don't have to be bold.** Light or regular display titles at large size are often stronger and more premium. Choose weight on purpose.
- **Highlighting part of a headline:** keep the rest regular and set the phrase in bold, or use a fill box behind it, or one other font in the same color. Never the one-italic-serif-word trick. Before you choose, think about where the visual weight of the whole screen goes and make the highlight the right one.
- **Color: striking, harmonious, clear tonal contrast.** Light background with strong dark text, or dark background with bright text. No muddy mid-tones: no cream text on brown, and no warm brown-black backgrounds with orange. A high Warmth dial makes the neutrals brown; watch it.
- **Real photos are allowed** from Unsplash (hotlink `images.unsplash.com` URLs in the HTML, which is how Unsplash asks images to be used; no people's faces as fake customers). Code-made art is still welcome.

## The process for each piece (this is what we are testing)

Run every command from the repo root `/Users/Kunal/Desktop/Design-System`. `E=skills/opendesigner/scripts/engine.py`.

1. **Direction.** Fictional brand, domain, audience, mood in one paragraph. Name 3 feel words.
2. **References.** 2 to 4 Mobbin searches. Look at the images. Write down 2 to 4 references (`mobbin_url`) and the one thing each teaches you (structure, rhythm, density, a technique), in `notes.md`.
3. **Design system from the engine.** Make the system in the piece's own folder:
   `python3 $E --dir brand/showcase/<cat>/<nn-slug>/opendesigner sketch --name "<Brand>" --brand "#hex" --audience regular|dense|large --platforms web|ios|... --feel w1,w2,w3 --theme ... --delegated all`
   then move the dials to fit the direction (`python3 $E --dir ... set dials.<id> <0-100> --set-by delegated --why "..."`; the dial ids are expression, brandPresence, density, energy, roundness, depth, colorfulness, warmth). Set the typefaces through the engine if you can find how (look at `engine.py show`, `python3 $E feel`, the stage files in `skills/opendesigner/references/stages/` and DESIGN.md). Then `python3 $E --dir ... build`. Read the generated `DESIGN.md` (next to the opendesigner folder) and `opendesigner/build/css/tokens.css`.
4. **Build** `index.html` in the piece folder. Link the generated tokens (`<link rel="stylesheet" href="opendesigner/build/css/tokens.css">`) and **use the `--ds-*` variables** for color, spacing, radius, type size, motion. Where you must step outside the tokens for the art (a hero gradient, a display size bigger than the scale), do it on purpose and write down why. If the system the engine gave you is not good enough to make something stunning, that is a key finding: say exactly what was missing, then fix it the way a user would (change dials or answers through the engine first; hand-edit only as a last resort, and record it).
5. **Render** with `python3 brand/tools/shot.py brand/showcase/<cat>/<nn-slug>/index.html brand/showcase/<cat>/<nn-slug>/shot.png --w <W> --h <H> --scale 2` (add `--full` for long pages). Open the PNG with the Read tool and look at it at full size. Crop type with `--selector` if you need to. Be your own harshest critic: would a design director at a top studio post this? If not, iterate. At least two rounds of look-and-fix per piece.
6. **Check.** `python3 skills/opendesigner-preflight/scripts/preflight.py html <index.html> --medium web` and `python3 $E --dir .../opendesigner validate`. Fix what is real. Walk `skills/opendesigner-preflight/references/checklist.md` for the type and layout sections.
7. **Notes** in `notes.md` in the piece folder: direction, references with what each taught, dial values and why, fonts, where you went outside the tokens and why, check results, and **process findings** (what in OpenDesigner helped, what was slow, wrong, confusing or missing). Record each real process gap with `python3 $E --dir .../opendesigner feedback "..." --kind gap|bug|confusing|idea` (it is written locally; nothing is posted).

## At the end of your category

Write `brand/showcase/<cat>/PROCESS.md`: a table of the pieces (direction, palette, type, render size), then the process findings across all of them, most important first, each with evidence (command, output, file). Separate "the engine/skill is wrong or missing something" from "I worked around it". Be honest: if a piece is weak, say so.

Your final message to the orchestrator: the list of pieces with paths to their `shot.png`, and your top 5 process findings in plain words.
