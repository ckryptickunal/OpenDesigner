# Presenting a showcase piece

For agents who build pieces in `brand/showcase/`. Read it with `BRIEF.md` and `ROUND3-BRIEF.md`; this file covers how a piece is framed and shown. The bar is the B2B product screens (`product/01` to `06`): real product, one accent, quiet chrome, small exact type, no decoration. Each rule can be checked on `shot.png` or on its gallery-size copy. Numbers in brackets point to the sources at the end. "[ours]" marks a measurement or judgment made in this repo, not an outside source.

## Look at it the way the gallery shows it
- The live gallery shows a 1440 × 900 shot 337 px wide, a quarter of its size, and phone and watch shots 192 px wide (measured at a 1440 px browser window on 2026-10-15) [ours].
- Make that copy and look at it before the full-size render: `sips --resampleWidth 337 shot.png --out <scratch>/thumb.png` (use 192 for phone and watch).
- Write down where your eye lands first and the one sentence the shot says. If either is not your idea, the shot is not done.

## 1. The shot
1. **One idea per shot.** Write it in `notes.md` as one sentence before you build ("a controller confirms three matched receipts at once"). If describing the render needs "and", split it: `shot.png` holds the idea and `shot-<state>.png` holds the rest. Apple asks that each screenshot after the first few focus on "a main benefit or feature" [2].
2. **The subject fills the frame.** The product, component or object covers at least 60% of the image. No empty quarter of the canvas, unless the emptiness is the composition (one object on a field) [ours].
3. **Crop through repetition, never through the point.** A crop may cut off more table rows, more cards or the rest of a sidebar. It never cuts a headline, a total, a button label or the component itself. Linear crops its product where it runs off the edge of the page [M1].
4. **Show UI at the size it was designed for.** Render the real viewport (1440 × 900 web, iPhone at 3×, the watch at its App Store size [4]) and never shrink a whole screen into a box. If it does not fit, render a smaller viewport or crop. Refactoring UI: do not scale screenshots down; shoot a smaller screen or a part of it [8]. Everything in one shot shares one scale [10].
5. **Flat and straight on.** No tilt, perspective, isometric stacks or rotated cards. Apple: "Straight-on product shots are preferred" [1].
6. **One plain background.** Put a busy thing on a plain field and a simple thing on a rich one [9]. Neutral or solid backgrounds are the default [10]. A stage colour or photo is allowed only when it is the brand's one asset, used the same way on every shot: Mercury puts its product on one soft single-tone panel [M7], and Radix uses the same panel behind every component demo [17]. Never a violet gradient (section 7).
7. **No words in the image that the product would not show.** No captions, size labels ("Tablet, 1180 × 820"), "1:1" badges, numbered leader lines or taglines. The gallery card carries the title. Apple warns against overlays that "crowd out your app" [3], and Google Play limits taglines to 20% of a screenshot [7].
8. **One presentation per category.** Same canvas size, background treatment and crop logic for every piece in a category, so the differences are in the design and not in the framing [ours].

## 2. Clutter: remove before you add
9. **Count what competes.** List everything a viewer could look at first. Keep one. Make the rest smaller, lighter or closer to the background colour: emphasize by de-emphasizing [8].
10. **"Spend your boldness in one place"** [11]: one display moment, one accent colour with one job, and one depth technique throughout, with no shadows in dark interfaces [9]. We count hairline borders and shadows as two techniques, so use one [ours].
11. **Delete on sight,** unless the piece is about that exact thing: stickers, starbursts, stamps, rotated labels, marquees, "New" pills, glows, blobs, blurred discs, dot or line grids, noise, confetti, invented logo rows and star ratings (our audits, `making.md` section 11); emoji used as icons, coloured side borders on cards and status dots with no defined state [12][13].
12. **Cards only for things a person can act on.** Group everything else with space, alignment and type [12].
13. **Props are clutter.** No hands, cups, calculators, plants or desks around a device [7][10].

## 3. Content
14. **The product in use, mid-task.** Rows selected, a panel open, a value being edited, a toast that just appeared. Apple asks that screenshots show the app in use, not merely title art, a login page or a splash screen [3], and never a blank screen on a device [1]. Our rule: none of these, and no empty state, is `shot.png`; an empty state goes in `shot-empty.png` [ours].
15. **Specific, fictional, lasting data** in the product's own units: totals that add up, names from `NAMES.md`, no real people or companies, nothing that dates fast [1][7][10].
16. **Only the text the product would show.** No marketing copy laid over a product, app or component shot; the UI is the headline. On iOS the status bar shows full signal, Wi-Fi and battery [1].

## 4. Type at gallery size
17. **Small UI text becomes texture, and that is fine if the texture is orderly.** At 337 px, 14 px text is about 3 px tall. The B2B screens still read because their text sits in aligned rows and columns; Quoin (`product/01`) uses four sizes (12, 14, 20 and 24 px) and three weights [ours].
18. **When the idea is words, the words must read in the thumbnail.** A hero headline, a footer wordmark or a style study's line is 40 px or more in a 1440 render (about 9 px in the gallery); on a phone, 20 pt or more [ours]. Google Play: "Avoid overloading the screenshot with text in small font sizes" [7]. Dribbble asks for a thumbnail that is legible at small sizes [14].
19. **Hairlines vanish when shrunk.** A high-contrast serif or a light weight under 40 px disappears in the gallery. Use it for one large figure or not at all. The owner's note on the private banking screen was "text is not visible" [ours].
20. **Two typefaces, at most six sizes, each 10% or more from the next** (`BRIEF.md`). Avoid changes of scale that multiply text sizes and stroke weights [10].

## 5. Devices
21. **Default to no device.** Show the screen itself. Google Play lists device imagery among things to avoid in screenshots and asks for Wear OS screenshots without device frames [7]. Morningstar shows devices "only in the context of device compatibility" [10].
22. **Use a device only when the device is the point:** the same task on a phone and a desktop, the place the product is used (a phone on handlebars [M8]), or one notification on a lock screen [M9].
23. **If you use one:** one device, or one pair showing one task. Straight on, generic hardware drawn in code (Stripe drew its laptop in CSS [15]), the screen at the device's native pixels, one light and one soft contact shadow [ours], and no added glare or reflections (Apple forbids adding them to its product images [1]). The screen is at least half the frame's height [ours].
24. **A device cannot rescue a weak screen.** Only finished, strong pieces go inside one (the owner, 2026-10-14).

## 6. Each kind
**Style study** (`styles/`)
- One product moment drawn in the style, not a sampler of the style's tricks.
- The style lives in one zone: one illustration, one object or one colour field. Type and grid stay calm: one face, regular weight, sentence case, strict alignment, nothing rotated. Gumroad does neubrutalism with regular-weight headlines, flat half-and-half colour fields and thin black rules [M2]. Figma's Shortcut puts one loud illustration inside a plain editorial frame [M3].
- The decoration carries data (`skills/opendesigner/references/making.md` section 11).

**Hero section** (`heroes/`)
- A headline, one supporting line, one action or none, and one subject: a product crop or one object made with care. Above the fold there is nothing else except a quiet nav.
- Linear today: headline on the left, a statement beside it, the product cropped off the edge, no badge, no glow [M1]. Its 2022 hero had the pill badge, two-tone headline, glow and gradient button that are now the AI default [M4].
- VanMoof: the product where it is used, a light headline, one outline button [M8]. Mercury: one headline over one brand photograph [18], and its product shown flat and whole on a single-tone panel [M7].

**Web component** (`components/`)
- The component is the subject, at 1×, with its trigger or the smallest context that explains it. One state per shot.
- Sonner and Vaul each open with one name, one line and one button that runs the real component, and Sonner's variants sit behind buttons, not in a grid [16]. shadcn/ui gives each example its own bordered box [17].
- Vercel shows a real comment thread over a page reduced to grey placeholder blocks [M5]. Linear shows its command menu alone on one gradient stage [M6]. Inside an app, simplify or dim the rest so the component reads first.

**App screen** (`app-screens/`)
- One screen, full bleed, at native resolution, with the complete status bar and home indicator, and no device frame in `shot.png`.
- Mid-task, with platform chrome rebuilt from a shipped app (Lloyds [M10], Public [M11]): 17 pt body, one accent, one face for everything read or tapped.
- The key number or title is 20 pt or more, so it reads at 192 px.

**Watch screen** (`watch/`)
- A black background that merges with the bezel [ours], and one glanceable thing: one number, one ring or one word. The time sits top right [6].
- Most images on Apple's watchOS page give one feature on one watch, in one finish, with one app. Some show the watch, others only its screen [6]. Our `shot.png` is the bare screen at App Store size (416 × 496 for Series 10 to 12) [4].
- Colour and glow only when they carry information. Apple's watchOS guidance uses background colour only when there is "something to communicate", not as a flourish [5].

**Footer section** (`footers/`)
- Quiet: link columns in one text size, one muted heading style, one rule and one legal line. At most one signature element: a large wordmark (Vucko [M12]) or a short statement (Garden [M13]). Glide's plain columns are the baseline [M14].
- Show a sliver of the section above, so it reads as the end of a page [ours]. No illustrations. Choose between a newsletter, socials and app badges; do not stack all three.

**Device mockup** (`mockups/`)
- Rules 21 to 24 apply in full: one device, or one pair on one task, straight on, on a plain stage.
- Selfridges: one phone, one notification, cropped by its panel [M9]. Square: one phone in low light and nothing else [M15]. Sketch: phones straight on, cropped by the panel edge [M16].
- No collages of many pieces, cascades of browser windows, leader lines, captions or desk props.

**B2B product screen** (`product/`), the bar
- The whole app at 1440 × 900: light, flat, one accent, dense real data, mid-task, no decoration, no device, no caption.
- Shipped equivalents: Shopify Bill Pay [M17] and Square invoices [M18].

## 7. Cheap tells, and what premium work does instead
| The tell | Instead |
|---|---|
| Many things at the same volume: stickers, badges, rotated labels, tickers | One idea and one display moment; demote the rest (rules 1, 9) |
| The 2022 SaaS hero: centred pill badge, two-tone headline, glow, gradient button [M4][13] | Decide each part; one action or none; a product crop or one object |
| Violet gradients and glows [12]; decorative gradient washes [11]; blobs and blurred discs | Flat fields; colour only where it means something |
| A whole screen shrunk until its type is mush | The real viewport, cropped (rule 4) |
| Tilted, floating or cascading screens and devices | Flat and straight on (rule 5) |
| Captions, sizes, badges and leader lines inside the image | Words belong on the gallery card (rule 7) |
| Specimen sheets, state grids and collages | One state per shot; other states in their own files |
| A device on a desk with a mug, plant or hand | No device, or one device on a plain stage (rules 21 to 23) |
| Blank screens, round numbers, "John Doe" data | Mid-task, specific, fictional data that adds up |
| Emoji icons, coloured card edges, status dots with no meaning [12][13] | One icon set, text labels, borders only for structure |
| Identical rounded cards for every block [11][12] | Group with space and type; cards only for actionable items |
| The subject small in a large empty canvas | Fill the frame (rule 2) |

In a scan of 1,590 Show HN launch pages, 22% showed four or more of the AI design patterns the author listed [13].

## Sources
1. Apple, Marketing Resources and Identity Guidelines: https://developer.apple.com/app-store/marketing/guidelines/
2. Apple, Creating your product page: https://developer.apple.com/app-store/product-page/
3. Apple, App Review guideline 2.3.3, screenshots: https://developer.apple.com/help/app-review/guideline-reference/2-3-3-screenshots
4. Apple, screenshot specifications: https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications
5. Apple, Human Interface Guidelines, Color: https://developer.apple.com/design/human-interface-guidelines/color
6. Apple, watchOS 27 page, image descriptions read 2026-10-15: https://www.apple.com/os/watchos/
7. Google Play Console Help, preview assets: https://support.google.com/googleplay/android-developer/answer/9866151
8. Refactoring UI (Wathan and Schoger), from reader notes: https://gist.github.com/selcukcihan/b9418596a98abfcd4bbc622550820cc5
9. Anthony Hobday, visual design rules you can safely follow: https://anthonyhobday.com/sideprojects/saferules/
10. Morningstar Design System, product illustration: https://design.morningstar.com/systems/marketing/product-illustration
11. Anthropic, frontend-design skill: https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md
12. The Fountain Institute, signs a UI has been vibe coded: https://www.thefountaininstitute.com/blog/signs-vibe-coded-ui
13. Adrian Krebs, scoring Show HN pages for AI design patterns: https://adriankrebs.ch/blog/design-slop/
14. Dribbble, how to share your work (2026): https://dribbble.com/stories/2026/02/18/how-to-share-your-work-on-dribbble-while-attracting-the-right-clients
15. Stripe, Connect: behind the front-end experience: https://stripe.com/blog/connect-front-end-experience
16. Sonner and Vaul, pages inspected 2026-10-15: https://sonner.emilkowal.ski and https://vaul.emilkowal.ski
17. shadcn/ui and Radix dialog pages, inspected 2026-10-15: https://ui.shadcn.com/docs/components/dialog and https://www.radix-ui.com/primitives/docs/components/dialog
18. linear.app, stripe.com and mercury.com home pages, viewed 2026-10-15.

Mobbin (open only on Mobbin; never save the images): M1 Linear https://mobbin.com/sites/sections/51e7f400-3bc1-4432-9f3b-117d49cd19c1 · M2 Gumroad https://mobbin.com/sites/sections/9639f434-ec35-484c-9564-bc6b572e8984 · M3 Figma Shortcut https://mobbin.com/sites/sections/d89d3841-aea4-4bc6-a310-075eb53e19db · M4 Linear 2022 https://mobbin.com/sites/sections/40a46191-a57a-4bab-9a92-94fc14cad817 · M5 Vercel https://mobbin.com/sites/sections/892a4a8f-55b5-4bad-84b3-c77a538bcfb2 · M6 Linear command menu https://mobbin.com/sites/sections/038755ae-4b0f-4e25-a7df-dca35d71d6bc · M7 Mercury https://mobbin.com/sites/sections/6a232113-eb8b-4583-b72e-5adc3db035c6 · M8 VanMoof https://mobbin.com/sites/sections/f54d5b21-b5a9-4631-a249-e70788205c8d · M9 Selfridges https://mobbin.com/sites/sections/e4e22226-2c40-4474-ba6e-b7f95db2873f · M10 Lloyds https://mobbin.com/screens/79ee9615-7e38-44c5-9386-c3811168a0ad · M11 Public https://mobbin.com/screens/7ea34d91-90a4-4b30-ab50-8965f4257c10 · M12 Vucko https://mobbin.com/sites/sections/325d9889-5eae-493d-926a-a959e8e99005 · M13 Garden https://mobbin.com/sites/sections/1c01c1c6-97bb-43e4-a021-f203e0b04da7 · M14 Glide https://mobbin.com/sites/sections/45cd1ec8-4cbe-483e-a2ac-8782ebfb6a27 · M15 Square https://mobbin.com/sites/sections/fad611b5-d51b-4419-9a48-4efa9cc451c1 · M16 Sketch https://mobbin.com/sites/sections/b0ec8ad2-106f-4646-9c61-302fbf782823 · M17 Shopify https://mobbin.com/screens/5a2d171e-3dba-4cdf-b719-629c91e27ced · M18 Square invoices https://mobbin.com/screens/53479e8d-9459-4667-834b-ba2709cbfeaa
