# 10 · Quillon on a laptop and a phone

Replaces `mockups/03-watch-trio` (audited 2 of 5, "remake"). Render: `shot.png`, 1600 x 1200 at scale 2 (3200 x 2400), path-traced, made with `render.py` (256 samples, about 4 minutes). Page: `index.html`.

## Direction
One B2B product on two devices: the same purchase request in Quillon (a fictional purchasing and approvals app) on a laptop and on a phone, staged like a studio product shot. One large softbox from the upper left, a seamless grey sweep, real contact shadows and real reflections on metal, no glow and no blobs. Feel words: **calm, premium, minimal**.

What the old piece did that this one must not (`../../audit/mockups--03-watch-trio.json`): a case that copied one brand's watch, flat straps with no edges, a background of three vertical soft bands, screens at full brightness with no crystal. Here both devices are drawn as nobody's (below), the set is one continuous sweep lit by one light, and the devices are rendered by a path tracer, so shadows, falloff and reflections come from the light rather than from painted gradients.

## The two screens: one product
- **Phone:** `../../app-screens/11-approvals-mobile/shot.png` (the new Quillon iPhone screen), used as is.
- **Laptop:** `desktop.html`, rendered to `desktop.png` (1440 x 900 at 2x). The showcase had no desktop Quillon: the new desktop approvals piece (`product/02-fennick-approvals`) is a different product with a different green and font. So I designed the web companion from the phone's own system: `desktop.html` links `app-screens/11-approvals-mobile/opendesigner/build/css/tokens.css` and uses the phone's four sizes (13, 15, 22, 34) and Inter. It shows the approval queue with the same request open: same vendor, amount, quote and date, same budget bar with the same exact widths, same policy, same four-step chain, same consequence line, plus what only a desktop has room for (the queue, line items that add up to $14,860.00, the three quotes compared, the PDF).
- The phone's data changed while I worked (the vendor became Ashbury Traction Power; the quote date became Fri 16 Oct). The coordinator flagged it; the desktop now matches the phone word for word, and every date was checked: 16 Oct 2026 is a Friday.

## The devices (drawn here, nobody's)
- **Laptop:** 14-inch class, graphite bead-blasted metal, a 16:10 panel behind black glass with a centred camera dot, a visible **barrel hinge** between lid and base (no wedge, no thumb notch, no logo), a keyboard with legends (`esc`, `F1`… `delete`, `fn ctrl opt alt`), a glass trackpad with a hairline gap.
- **Phone:** a rounded slab with a **centred punch-hole camera** (no notch, no island), side keys on the right, standing on a bent-metal stand (base, back support, front lip).

## Light and render
three.js 0.165 with three-gpu-pathtracer 0.0.23 (both MIT, from jsdelivr). One RectAreaLight softbox (0.6 x 0.45 m, upper left front), a weak bounce card on the right, a dim studio dome for the metal to reflect, Neutral tone mapping, 256 samples per pixel at 3200 x 2400. Screens are emissive with a clear coat, so they light the bezels and keys a little, as real panels do. The set colour is the scene system's `--ds-color-neutral-light-5` (#d6dbe3) read from the tokens at run time.

`render.py` exists because a browser will not let a page put images from disk into WebGL; it launches Chrome with `--allow-file-access-from-files`, waits for the tracer to reach the sample count, then shoots. Opening `index.html` straight from disk shows black screens.

## References (Mobbin; cited by link only, nothing saved)
| Reference | What it taught |
|---|---|
| Wispr Flow, "On-the-go or at your desk": https://mobbin.com/sites/sections/ddc48c4a-43de-4cdc-89f0-791148ca1b3e | One product on desktop and phone, the phone in front and to the right, overlapping depth; generic frames can carry real screens. |
| Mural, "Phone and tablet": https://mobbin.com/sites/sections/a05aae48-8143-448e-a252-e3d13c73b7b1 | The same content on two sizes side by side, the small device nearest the viewer. |
| monday.com, product images ("Board & mobile view"): https://mobbin.com/sites/sections/3fb47700-6e3e-435f-847b-c1337720d302 | The B2B convention itself: the web app with its phone app beside it. |
| Waka Waka, product photography: https://mobbin.com/sites/sections/babbbb04-f1e4-4020-bbd8-16ce43ba2e68 | An object on a plain grey set with one soft light; the falloff does the selling. |
| Apple, iPhone line-up: https://mobbin.com/sites/sections/a2f54b99-919c-4a5b-97c5-0cf35b841a62 | A studio sweep with hardware whose reflections come from the set; also the silhouettes our devices must not resemble. |

## System (engine)
Full log: `engine-log.txt`.
```
sketch --name "Quillon Studio Set" --brand "#1f7a4c" --audience regular --platforms web --feel calm,premium,minimal --surfaces "case study:experience" --delegated feel,audience,platforms
set raw.textFace "Inter"; set raw.fontLicence {...}; set dials.* (below); build; design-md
```
| Dial | Value | Why |
|---|---|---|
| expression | 40 | a studio product shot: light and material carry it |
| brandPresence | 20 | green only inside the product screens |
| density | 10 | two objects on a set |
| energy | 15 | still, one key light |
| roundness | 45 | device corners; the product's own 8 px controls |
| depth | 80 | real shadows and reflections are the whole idea |
| colorfulness | 15 | a pale cool set; the screens bring the colour |
| warmth | 30 | cool daylight grey, no cream, no brown |

## Font and type scale
One family, **Inter** (SIL OFL), the product's own. Scene caption: `body-sm` 15 px, weights 500 and 400, ink on the set (9.9:1, measured on the render). Desktop screen: Footnote 13, Subheadline 15, Title 2 22, Large Title 34, the phone's own roles. The keycap legends are drawn in Inter into the keyboard texture.

## Outside the tokens, on purpose
Everything 3D: device dimensions in metres, materials, light sizes and intensities, camera. Two keycap colours in the canvas are marked `od-ignore` (device art).

## Look and fix (rounds, scores)
1. **Setup.** The first traces were black or showed a grey wall: the path tracer ignores `InstancedMesh` matrices, so the 70 keys became one 1 m cube around the camera. Keys are now merged geometry. The sweep's faces pointed down; fixed.
2. **Round 1, score 3.5** (first full render, 192 samples). A believable studio shot, but the laptop base read as a toy: a 5 mm bullnose edge caught a highlight like a bumper, and the keys had no legends (the old audit's first tell). Trackpad too light. Devices filled 72% of the width.
3. **Round 2, score 4.** Base thinner (13.6 mm) with a 2.4 mm edge radius, legends on every key, trackpad darker and less metallic, lens 22° to 20.5° (devices fill about 78%). Fixed the environment's orientation (its bright half was below the horizon). Tried two ways to put a soft reflection on the screens' glass (a bright patch in the dome, then two white cards out of frame); neither showed on the glass and the cards entered the frame, so both were removed rather than faked.
4. **Round 3 (coordinator's data check), score 4.** Vendor, quote and date matched to the phone; reused names replaced (below); re-rendered.
5. **Round 4 (B2B fix round), score 4.** The phone changed again: "Owen Castillo" is now "Owen Marchetti" and the budget is "Facilities budget, Jul–Dec". I diffed every text line of `desktop.html` against the phone's page; those were the only drift. Both places with Owen now say Marchetti; the budget card, its bar label and the sidebar link now say Jul–Dec. `NAMES.md` showed that Tomás (Tomás Reyes, `styles/03`) was taken, so Tomás Ruiz became Dario Feld. Re-rendered `desktop.png` and `shot.png`.

Final score **4 of 5**. Next to Waka Waka and the Apple line-up at the same size: one light direction, honest soft shadows with dark contact lines, metal that reflects the set, screens readable at 100% (the phone's amounts and chain read; the laptop's title, amount and both buttons read). Below 5 because the set is perfectly clean (no paper texture), the screens carry no glass reflection, and the stand's front lip hides the phone's home indicator.

## Names
Every invented name was checked against all of `brand/showcase` and web-searched. Replaced because another piece already used them: Tessaly, Halvorsen, Brightwater, Lumenfield, Corran, Ostrava, Pellam, and the first name Mira. Removed because it is a real company family: Kessler (from the phone's earlier copy). Now: org Thornquay; vendors Ashbury Traction Power (the phone's), Brisemont Racking, Tolleth Safety Training, Quenby Door Systems, Lumarch Electrical, Stellwick Packaging, Orrinford Plant Hire, Hexley Fire Service, Corlay Steelworks, Vardeck Lift Parts, Dunmerrow Handling; people Hanne Varga, Dario Feld, Aiko Tan (and the phone's Elif Demir, Owen Marchetti, Rhea Kapoor). Web searches for each brand name found no company by that exact name.

## Checks
- `brand/tools/check_dates.py brand/showcase/mockups --year 2026`: every weekday matches its date ("Fri 16 Oct" is the only weekday here).
- Names: every name checked against `../../NAMES.md`; added Thornquay, Hanne Varga, Dario Feld, Vardeck Lift Parts, Dunmerrow Handling and PR-2207, moved Owen Marchetti to list this piece, removed the stale Owen Castillo and Tomás Ruiz lines, and added the avatar HV.
- `validate`: passes, 0 warnings. `review --project`: clean after moving `desktop.html` to tokens (heights, a selection ring as an outline, the tab underline as a 2 px border, pip gaps) and marking the keycap colours. DESIGN.md refreshed.
- `preflight --medium web`: M9 false error only (Inter loads through a Google Fonts link).
- Caption contrast 9.9:1 on the set, measured on the render.

## Process findings (this piece)
- **The showcase's phone and desktop approval pieces are two different products,** so "one product on two devices" needed a companion screen nobody had made. Recorded (gap): a product brief should list every surface it ships on.
- **`review` checks every HTML in a folder against the folder's system,** so it suggested the scene's tokens for `desktop.html`, which uses the phone app's tokens. Recorded (bug).
- **Copied data goes stale.** The phone screen changed twice while I worked (vendor, date, consequence line). A companion screen should read its facts from one shared data file, not from a copy.
- OpenDesigner has no 3D or product-shot step; a path tracer in the page worked, but every material, light and camera value is outside the system, as `PROCESS.md` finding 1 already says for CSS devices.

## Rework 2026-10-14
After the independent audit (`../../audit/mockups--10-multi-device.json`, 3 of 5). It found the path-traced laptop read as a toy (a thick slab, a barrel hinge covering half the function-key row, both "opt" and "alt" on one keyboard), an iOS screen on Android-style phone hardware with a centred punch-hole camera, the top fifth of the frame empty with the devices low and small, and a count error: "Waiting on others · 6" and the "Upcoming 6" tab listed five rows. The sections above describe the 3D version and are kept as its record; this section replaces them where they differ. Render: `shot.png`, 1600 × 1200 at 2×, made with `render.py`.

**The scene is flat now.** `index.html` is HTML and CSS, no WebGL, drawn straight from the front the way shipped multi-device sections do it (structure from Riverside and Wispr Flow; nothing copied):
- **Laptop:** a lid with an even 20 px bezel and a plain camera dot, over a thin base lip that is a little wider than the lid. No keyboard (it is not visible from the front), no hinge, no notch, no logo, no thumb cut-out.
- **Phone:** a plain rounded slab with an even 12 px bezel and no camera cut-out, notch or island, so the hardware no longer contradicts the iOS screen and copies nobody's.
- **One material and one corner rule:** both devices are graphite from the scene's dark neutrals, and each screen's corner radius is its frame's radius minus the bezel. Shadows are the system's: overlay elevation under the phone and, after the fresh audit, floating elevation under the laptop's lip.
- **Composition:** the pair spans 1,370 of 1,600 px (86%), centred, with the caption aligned to the pair's outer edges. The phone stands in front of the laptop's lower-left corner, where it covers only the web app's sidebar; the lower right holds Decline and Approve, which must read.
- **Caption:** "Quillon · one approval, on the phone and on the web" (in the order the devices sit) and "PR-2207 · $14,860.00 · waiting on you". Measured on the full-size render against the darkest 5% of pixels behind each line: 13.1:1 and 6.1:1.

**Fresh audit (a reviewer that did not build it), 4 of 5,** against Riverside (https://mobbin.com/sites/sections/601ce269-1efe-407c-9fb5-7272f7504f43), Wispr Flow (https://mobbin.com/sites/sections/ddc48c4a-43de-4cdc-89f0-791148ca1b3e) and Canva's "Available on desktop, iOS, and Android" (https://mobbin.com/sites/sections/b8ad8173-8057-41e6-b304-ec1f237bde80), the closest in structure and finish. The frames copy no brand (Riverside's laptop has a notch; ours has none), the devices fill 85.6% of the width with about 13% above and below, and the phone hides only the lower part of the web app's sidebar. Its three must-fixes are fixed:
1. **Step counts.** The three requests waiting on you under $10,000 said "1 of 3", but the requester and procurement have already acted, so each is "2 of 3" with two filled pips, counted the way the open request's "2 of 4" is.
2. **Tabs against the list.** "Waiting on you 4 · Upcoming 6 · Done 312" had the first tab selected while the list showed both groups, and the LED retrofit "upcoming" was already past you (with the CFO). The tabs are now "Open 10 · Done 312", and the list keeps its two groups, "Waiting on you · 4" and "Waiting on others · 6".
3. **A name one letter from another piece's.** "Hexley Fire Service" was one letter from "Wexley Freight" (`heroes/11`). It is now Moydell Fire Service (no business by that name found on the web; nothing like it in `NAMES.md`).
Also done from its list: the laptop's base lip now has the scene's floating elevation as its contact shadow, so both devices sit on the plate in the same light.

**The count.** `desktop.html` now lists six requests under "Waiting on others · 6": the new row is "Floor line repainting, aisles 1–8", Brantlow Floor Marking, requested by Elif Demir, $4,738.60, with Owen Marchetti (under $10,000, so it cannot be waiting on the CFO). The six rows use 8 px vertical padding instead of 12 so the last one ends at y 867 of 900. Every other value is unchanged and still matches the phone word for word.

**System.** The 3D values no longer applied, so from this folder: `engine.py set dials.depth 30 --set-by delegated` (was 80: flat frames, one faint shadow) and `engine.py set dials.expression 30 --set-by delegated` (was 40: a flat plate where the screens carry everything), then `build`, `design-md`, `validate` (passes, 0 warnings) and `review --project .` (clean). The commands are in `engine-log.txt`. Device sizes are raw values marked `od-ignore: device art`.

**`render.py`** no longer drives a path tracer. It renders `desktop.html` to `desktop.png`, then the scene to `shot.png`, both through `brand/tools/shot.py`; `--query hide-text` renders the scene without the caption, for the contrast measurement.

**Checks.**
- `check_dates.py --year 2026`: every weekday matches ("Fri 16 Oct"; Oct 16, 2026 is a Friday).
- Line items $12,940.00 + $1,420.00 + $500.00 = $14,860.00. Waiting on you $14,860.00 + $8,412.50 + $3,240.00 + $2,186.40 = $28,698.90. Budget $96,000 − $23,340 left − $14,860 = $57,800 spent (60.2%); the request is 15.5%.
- Names: Brantlow Floor Marking and Moydell Fire Service are new; nothing in `NAMES.md` shares their distinctive words or is one letter from them, and web searches found no company by either name. Both are in `NAMES.md`; Hexley Fire Service was removed.
- A fresh verification after the fixes re-added every total above, counted 4 + 6 rows against "Open 10", and found the open request's facts identical on both screens (vendor, amount, budget, policy FIN-04, chain and times, Q-5571.pdf valid until Fri 16 Oct, PO-10482).

**Still open.**
- **The render's phone is not final.** `shot.png` (rendered 00:56 on Oct 15) shows `app-screens/11-approvals-mobile/shot.png` as it was then. That piece's own round 3 changed the phone at 01:00 and is still changing it: Decline is now outlined and neutral instead of red on grey, "If you approve" is no longer in capitals, the policy line moved into the CFO step, and the tab badge is gone. When the phone is final, `desktop.html` should take the same Decline style and wording so the two screens stay one product, and `render.py` should run again. The coordinator will schedule that sync.
- **No shared data file.** `desktop.html` still copies the phone's facts by hand, which `making.md` section 6 warns against; the phone has changed three times while this mockup was built.
- **Minor:** in "Waiting on others", the With column names a team ("Procurement") on three rows and the procurement approver ("Owen Marchetti") on two. The phone never shows PR-2207, which the caption names.

## Round 3 (2026-10-15): synced with the final phone
`app-screens/11-approvals-mobile` (the source of truth for the request) finished its owner round, so `desktop.html` now matches it, and `desktop.png` and `shot.png` were re-rendered with `render.py`.
- **Cobalt.** `desktop.html` links the phone's `tokens.css`, whose accent moved to cobalt `#2B4C9B`; the render picked it up (selection, chain, link, Approve).
- **Amount** "$14,860 USD" without grey cents (the queue rows and line items keep cents); the caption is now "PR-2207 · $14,860 · waiting on you".
- **Quote line** "Quote valid until Fri 16 Oct · Q-5571.pdf" in primary text with a clock icon; the file name is the accent link.
- **Budget:** "Budget after approval", "Facilities, Jul–Dec", "$23,340 of $96,000 left", the legend "60% spent" and "+15% this request" starting under its own segment (no "24% left"); track `neutral-light-6`, spent `neutral-light-9`.
- **Details card** replaces the "Rhea Kapoor (CFO) approves next…" sentence and the policy line: Then, PO-10482 to Ashbury, Net 30 · GL account, 6420 Equipment upkeep · Deliver by, Wed 21 Oct.
- **Sign-off · 1 of 3 approved:** Elif Demir as an arrow ("Requested it", 08:12), Owen Marchetti approved ("Procurement, compared 3 quotes", 09:40), You ("Department head", Waiting), Rhea Kapoor ("CFO, over $10,000 (FIN-04)", Next), with the time or state in a right-hand column; the CFO's empty ring is `neutral-light-8`.
- **Decline** is white with a `border-strong` outline, primary text, regular weight. Section labels are regular weight, as on the phone.
- **Queue progress counts approvals only**, as the phone does: PR-2207 "1 of 3"; the three requests under $10,000 waiting on you "1 of 2" (procurement and you).
- **Tabular figures only on amounts.** The fresh audit found `num` on whole strings made hyphens wide ("PR - 2207", "PO - 10482", "three - phase"); they now apply to the ledger and quote amounts only.

**Fresh audit, 4 of 5** (a reviewer that did not build it), against Wispr Flow (https://mobbin.com/sites/sections/ddc48c4a-43de-4cdc-89f0-791148ca1b3e), Monarch (https://mobbin.com/sites/sections/2ad09b8b-3ebf-4a76-8159-f8da92880c38) and Ramp (https://mobbin.com/sites/sections/c97365f0-4fee-4ad0-8ad9-c7ef4849bc6d). Every shared line of the open request is identical on both screens; $28,698.90, $14,860.00 and the budget re-add; 4 + 6 rows match "Open 10"; Fri 16 Oct and Wed 21 Oct are right for 2026. Caption 13.1:1 and 6.1:1. Below 5 because the composition is the standard laptop-and-phone layout.

**Still open, outside this folder:**
- **GL account 6420** is also used by `heroes/11` ("6420 Repairs") and `product/02` (GL code 6420). The phone is the source of truth, so the code should change in `app-screens/11` first and then here.
- **The phone's own "PO-10482" Details row** has the same wide-hyphen bug (tabular figures on the whole string), below its fold.
- This mockup and `app-screens/11` are not yet in `brand/showcase/index.html`; `build_gallery.py` adds them.
- The With column still mixes a team ("Procurement") and a person ("Owen Marchetti"); Q-5571.pdf appears twice on the laptop (quote line and file card); FL-07, Q-5571, PO-10482 and FIN-04 are not in `NAMES.md`.
- `check_dates.py --year 2026`: every weekday matches.
- **Later on 2026-10-15:** the name checker (`brand/tools/check_names.py`) found "Stellwick Packaging" two letters from "Pellwick Press", the workspace in the rebuilt `components/05`. The vendor is now **Ashlund Packaging** (no company of that name found on the web; "Brayford Packaging" was rejected because Brayford Plastics is a real packaging firm). `desktop.png` and `shot.png` re-rendered.
