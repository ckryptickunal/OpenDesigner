# Making and reviewing pages with the system

How to build a page, a screen or a section once the design system exists, and how to go round after round with the person who decides. Read it before you build anything a person will look at, and again each time they give feedback on what you built.

Sources: `research/L22-making-and-review.md` (one marketing-site build; reference material, one project's evidence), the house standards in `standards/process-review-taste.md`, and the cards named in each section. Nothing here sets a token value or changes a default.

## 1. Before you build
- **Know the job.** Write one line: who the page is for, and what they should do or believe when they reach the end. Judge every option against that line, not against looks alone.
- **Lock what exists.** Copy the person's existing words exactly, with where each came from and the date. Mark new text as new. Never mix invented text into a record of what exists (`guardrails.md` section 5).
- **Use their real assets,** or ask for them (`hooks.md`). A stand-in is never shown as finished.
- **Look at shipped work before you invent.** For each part of the page, find how shipped products solve it, starting from the person's own references (DC-L19-178). Take structure and quality, never identity (`guardrails.md` section 1). In the source project, whole rounds of the builder's own options were removed, and the pages the owner kept working on were built on rebuilds of shipped sections (DC-L22-01).
- **Agree the pace, once.** Some people approve a plan step by step. Others decide by looking at a built draft. Ask which they want. A draft first is fine. Sections 2 to 10 are what keep a draft honest (DC-L22-01).
- **Build the first draft on the tokens.** A draft may come before the deeper questions, never before the token build. Run the sketch (`zoom.md`, level 0), or read their existing product with opendesigner-extract. Then make the draft read its values from that build's export, and never give it a style file of its own. In the source project a sketch build existed from the first day and the draft was never bound to it. Values lived in three separate style kits, and one page ended with seven type families.
- **Fix the page's materials before the second section is built** (section 4).

## 2. One round
Follow this order every time the person asks for something on a built page.
1. **Say it back in one line.** Read `opendesigner/decisions.md` before you ask anything: it may already be decided.
2. **Find every place it applies** (DC-L22-08). A note on one card, one screen or one section is a note on every one of the same kind, and on nothing of another kind. Say in one line what you will apply it to, and list the places before you edit. When the kind can be counted (bare color markers, a heading style, a corner), count it before and after. A change to something that several pages show goes to all of them in the same round. Before you call the round done, name any page that still shows the old version.
3. **Change only what was asked.** Add no element, and restyle no approved work, as a side effect. A restyle is not a resize. A new color, typeface or corner does not change a size, a gap or a structure. Compare sizes with the version before.
4. **Take every value from the system.** Colors, sizes, corners, shadows and durations come from the tokens. If the round needs a value the system lacks, add it as a decision (opendesigner-extend, section 4) or list it as debt (section 9).
5. **Check it as rendered** (section 5) before you show it.
6. **Show it next to what was there before** (section 3).
7. **Record the decision in their words.** Then remove the options it settled.

**Ask, or act?** Act on what follows from the request, and report it. Ask only at a real fork, with your pick and a visible alternative. Keep waiting decisions in one numbered list the person can answer in one message: a question that is only logged never closes.

**What they say, and what they pick.** A stated preference is something to test. Build the smallest real version, keep the version before one switch away, and record the choice only after they have seen it on the page (DC-L22-01).

## 3. Showing options on a built page
The house standards already say how options are built and compared: STD-process-review-taste-37 to -49. They are written for prototypes of one piece of interface. Follow them for any option on a built page:
- Name each option by what it explores (-37). Build three by default and five at most (-38).
- Every option fully works, with realistic, product-shaped content (-40).
- Options live on a review route or page of their own, never in the live product (-41).
- Show one at a time, full size, inside the real page (-43). A small map or a thumbnail is not enough to decide from.
- Flip through every option yourself first (-47). Say when each is the right choice and what it costs, and don't pick for them (-48).
- When they pick, build only that one into the product (-49).

What one project adds (DC-L22-02):
- **Keep the current version as an option,** with a plain name such as "Today". People judge each new option against it. You test against it too (section 5).
- **One question at a time is still the rule (-42).** When the person asks to judge several things together, such as type, corners and one section's layout, give each question its own switch with a plain name. Each switch remembers its state and has an address in the URL, so a combination can be shared and tested. Keep the count low: every switch multiplies the combinations you must check.
- **The controls never cover the page.** Keep the picker's own look as its spec gives it (-45). If the person says the controls are in the way, let them fold the controls away. The spec has no such control yet (lane L22, Part D3).
- **Boil down after every decision.** Remove the switch, keep the choice, record it. Ask once, early, whether earlier options should stay reachable; some people want to go back to them.
- **Never remove an option the person has not ruled out.**
- **A section made for a light background is not a dark section with the colors swapped.** Design the dark one as its own option, or keep the section light.

## 4. One page, not several
Sections may differ in layout (DC-L19-50). They may not differ in materials. Decide these once, record them, and hold them in every section (DC-L22-03):
- the type families, and the job of each: headings, text, small labels;
- one heading style: size, weight, case, and when a heading is centered;
- which corner rule belongs to which kind of thing;
- how a box is drawn: its edge, its fill and its shadow;
- where content starts and ends on a wide screen;
- one dark text color and one accent;
- how photographs are treated;
- how a section that steps is controlled.

When a reference inspires a section, you may first rebuild its structure closely, with the person's own words and assets, on a review page that never ships, to judge the idea. Take nothing of the reference's identity (`guardrails.md` section 1). Once the person picks it, rebuild it in these materials before anything else is built onto it. In the source project, several rounds each built one section to a strong reference and kept much of that reference's look: its small type, its corners or its boxes. After a few rounds one page held four design languages and seven type families.

**When the person says the page does not hang together,** or calls a section "bland" or "different", don't restyle by eye. Run the cohesion audit first. Copy `assets/output/COHESION-AUDIT.md` to `opendesigner/COHESION-AUDIT.md` and fill it in:
1. Number the sections, and read the numbering back with the person's own words beside each.
2. Ask the same eight questions of every section, measured on the rendered page: background, heading, small type, corners, how a box is drawn, content edges, things to look at, movement.
3. Read down each column. Where the answers change from row to row, write a finding with its proof: counts and values, not adjectives.
4. Match each complaint to its causes. "Bland" is often contrast with a busier neighbor, and only partly a fault inside the section.
5. Offer directions: the least effort (line up the seams only), the most adaptable (one set of materials every section can take), and one or two led by a section they already like. Say what each changes, keeps and costs.
6. Change nothing while you audit. Build the directions they choose as options (section 3).
7. If a measurement shows that something you said earlier was wrong, say so in the report.

## 5. Check it as rendered
`engine.py review` reads values in code. It cannot see the page (DC-L22-05, DC-L19-167). Before you show anything:
- **Look at it.** Take a screenshot of every section you changed and read it, at each size you support. Fix what is broken before the person sees it.
- **Use the person's own window.** Ask once what they review in: which browser, how wide the window is, any zoom. Test there as well as at the usual sizes (DC-L19-56).
- **Test between the breakpoints.** A rule written for tablets can squeeze a layout at a width nobody opened.
- **Test without hover.** Anything that changes on hover must also change another way: by itself on a timer, or on a tap (DC-L19-143). Hover styles themselves sit behind a fine-pointer query (STD-accessibility-motion-15).
- **Measure text as rendered** wherever something is scaled down. A screen shown at reduced scale can pass every type check while its text renders at 8 to 10 px.
- **Compare with the version before** for everything you did not mean to change. Compare computed styles or screenshots, section by section.
- **Emulation is not a device** (STD-process-review-taste-33). When the person reports a fault you cannot reproduce, say so, say what you tried, remove every difference your change introduced, and ask them to look again. Never report it as fixed.
- **When you record the screen to check motion, record only your test window.** A recording of a screen region can catch the person's other windows.

Then tell the person what you checked and what you could not (`guardrails.md` section 5).

## 6. Finished interface inside a page
A product screen on a marketing page, or a live demo in documentation, is a finished design inside another one (DC-L22-04).
- **Keep the two style worlds apart.** A page rule aimed at a bare element or attribute, such as every `svg` or every `[stroke]`, reaches into the embedded interface. Scope page rules so they stop at its edge.
- **Give every class inside the embed its own prefix,** state classes included. A short name such as `on` or `live` will match a page rule with the same name, and nothing reports it.
- **Write the embed's resets so each weighs one element.** Wrap only the scoping part of the selector in `:where(...)`. The reset then beats the page's element rules and still loses to the embed's own classes.
- **After any page-wide restyle, compare the embed with the version before.** Count something cheap, such as icon colors per screen or the computed typefaces.
- **Design it at real size and show it scaled, like a screenshot.** Decide which parts must stay readable (the title, the key figures, the main action) and measure them as rendered.
- **On a small screen, show part of it at a readable size and move the view.** Don't shrink the whole screen.
- **Sample content is realistic** (DC-L19-35). On a public page, use made-up names for companies and people. Spread the examples across the kinds of customer the product serves.
- **Load each embed when it is needed,** and paint only the one that shows.

## 7. Sections that hold the page, and movement
A section that stays in place while its steps play spends the reader's scroll (DC-L22-06, DC-L19-84).
- **Add up the scroll.** For each held section, work out its share of the page's whole scroll, and say it in your report. In the source project, two held sections took 61% of the page's scroll, and the owner agreed to shorten both once the share was shown.
- **One control for every section that steps.** Two sections that behave alike and look different read as two products.
- **Decide what moves it on:** scroll, a clock, or either. On a clock, wait while the section is out of view, stop when the person takes over, and show every step without movement when reduced motion is on.
- **Drive movement by time, not by frames.** A step taken once per frame runs faster on a faster screen.
- **Fade the new layer in over the old one, which stays put until the fade ends.** When both fade at once, the page shows through halfway.
- **Move fine patterns by whole device pixels, or keep them still.** Dither, halftone and hairline grids shimmer when they move by part of a pixel.
- **Several moving things in one section share a manner and differ in what they do.** Six drawings that all fill from left to right read as one template. Let each build in the way that explains its own figure.

## 8. Figures drawn as graphics
A drawing beside a number is a claim (DC-L22-07).
- **Draw only what the words state.** No invented axes, series, scales or trends. If the copy says every order is tracked, draw every order tracked, and nothing more.
- **Use the product's own chart language** when the page also shows product screens. A generic infographic beside real screens looks cheaper than either.
- **Put a set of cards on one grid.** Columns start and end on the same lines, even when the cards differ in height.
- **Keep labels at reading size.** A scale nobody can read is decoration.
- **On a small screen, keep two cards in a row while they stay readable.** One very wide card per row makes a long, thin page.

## 9. Debt, and when it is done
- **Keep a debt list as you go:** every value that did not come from the system, every option still switched on, every check you could not run.
- **A page is done when the list is empty or the person has accepted what is left.** Run `engine.py review`, then ask the eight cohesion questions (section 4) one more time.
- **Send what any product would need back to OpenDesigner** (`improve.md`). Write it about the method, never about the person's product.

## 10. Mistakes builders make, and what a repeated note means
These are mistakes an AI builder made in the source project (DC-L22-09). Most drew a correction from the owner, and several came back more than once. Check your own work against this list before you show anything.

| The mistake | What it looks like | Do this instead |
|---|---|---|
| Doubling down | The person likes one option and asks for more. You make variations of that one | "More" means new ideas at the same level. Keep the liked one untouched, and show others that work in a different way. Say in one line how you read the request |
| Reaching for what is at hand | Asked for something new, you reuse the same picture, asset or style | New means new material. Say what is new about each option |
| Fixing only where they pointed | The same note comes back for the next card, page or screen | Every instance of the same kind, counted (section 2) |
| Fixing everything that looks alike | A note about one kind of thing changes other kinds | The thing named and its true siblings, and nothing else |
| Taking a word to its extreme | "Lighter" becomes all white. "Sharp" becomes square. "Faster" becomes rushed. "Obvious" becomes a banner | A preference is a direction, not an absolute. Move one step that way and show it |
| Inventing first, or following a reference loosely | You design options from your own idea of the problem, or draw something loosely "after" a reference, even after being told to study shipped work | Study shipped examples first, and rebuild their structure closely (section 1). A method the person names holds for the next section too |
| Forgetting what was already said | A rule from an early round is broken on a page built later | Keep standing rules in one list, as decisions or project standards, and read it before each new piece |
| Adding what nobody asked for | A new button, a label, a disclaimer, a tint | Add nothing as a side effect. Offer it in one line instead |
| Changing what was approved or protected | A page-wide pass restyles something they were happy with | Approved work is frozen. Compare it with the version before (section 5) |
| Growing with each pass | Type, cards and detail get bigger or busier every round | A restyle is not a resize. When something is cluttered, take things out |
| A timid fix | The change is so small that the note comes back | Make the change clearly visible, on every instance |
| Asking what follows | You ask whether a rule applies to the next page | Act and report. Ask only at a real fork |
| Showing unseen work | You show something you never looked at as rendered | Section 5 |
| Arguing from analysis | You defend a choice with a measurement while the person is judging by eye | Measure faults and whether rules were kept. For taste, show two versions. An accessibility floor is not taste: show both and say which one meets it (`guardrails.md` section 4) |
| Fixing a different fault | You fix something real that is not what they meant, and call it done | Say back what you think they saw, and where. If you cannot see it, say so |
| Bringing a reference's style in with its structure | A rebuilt section arrives with the reference's type and corners | Rebuild it in the page's materials (section 4) |
| Stating what you did not check | You say two things match, or that something does not move, without looking | `guardrails.md` section 5. When you find out you were wrong, say so in the open |

**A repeated note is the strongest signal you get.** When the person says something a second time, or says "again" or "as I said", another small patch is the wrong answer.
1. Stop, and re-read both of their messages word for word.
2. Name what you got wrong the first time: too narrow, too wide, too literal, or the wrong thing.
3. Write the rule behind the note in one line, and say it back.
4. Apply it to every instance, counted (section 2).
5. Record it as a decision or a project standard, so work built later keeps it.
6. On a third time, write a small check that finds every case, and run it before every showing.

**Read each reply for what it says about your reading, not only for the fix.** "I only wanted that one changed" means your changes reach too far. The same fix asked for on five cards means they reach too little. "You just did more of the same" means "more" was a request for new ideas. Change how you read the next note, and say what you changed.
