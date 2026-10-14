# 03 · Company record · Corvane

## Direction
Corvane is a fictional CRM for B2B sales teams; the workspace belongs to the fictional vendor Aldermoor Systems. The screen is one company record, "Lathom Aerostructures" (invented aerospace supplier), as an account executive or RevOps sees it: breadcrumb and "12 of 214 in Enterprise pipeline" with up/down, the record header (logo tile, name, star, Add to list, Compose email), chips for owner, last interaction and open deal value, tabs with counts, an activity timeline that records changes, and a details panel with inline-editable empty values ("Set parent company…") and one field being edited. A second frame (`?state=palette`, `shot-palette.png`) shows the ⌘K command menu scoped to the record.
Feel words: **focused, trustworthy, precise** (the engine dropped "precise").

## References (Mobbin, cited by link only; nothing saved)
| Reference | What it taught |
|---|---|
| Attio record with diffs, https://mobbin.com/screens/d76ba56f-98c3-463f-9e1d-bbe4831ee47a (and https://mobbin.com/screens/297adfeb-8312-496b-8acf-41839a6cf775, https://mobbin.com/screens/3f58982f-fb3f-46de-a123-70350ebfa604) | "X changed Stage and 7 other attributes in Sales" expanding into attribute → value rows, groups by period that fold, "1 of 1 in Stage" navigation, tabs with counts, the details panel with "Set Description…" placeholders |
| Linear issue properties panel, https://mobbin.com/screens/d0f8ebba-34b7-469c-a708-1069e55a3e02 | Empty properties as verbs ("Set priority", "Add label"), the "2 / 5" record position with arrows, a quiet one-line activity list |
| Stripe customer page sections, https://mobbin.com/screens/1a4aa88b-e0be-49b2-a87f-1264e0b5e786 | Label-and-value pairs with an ID and a copy icon, sections separated by hairlines with the section action on the header ("Add to list", "Show all 24") |
| Navattic and Magnific command menus, https://mobbin.com/screens/c65971cf-c4ea-45e9-99a5-555930cb5d73 and https://mobbin.com/screens/14ceb943-f04a-460f-b4f5-2ebd78d74aff | Palette anatomy: grouped results, grey (not accent) selection, keycaps on the right, a hint footer |

## System (engine)
`sketch --name "Corvane" --brand "#1f4fd1" --audience dense --platforms web --feel focused,trustworthy,precise --theme system-light-dark --delegated all --surfaces operate`

The sketch resolved roundness 0 and two weights again. P1 dense profile by hand (`--set-by delegated --why "P1 dense work-tool profile, brand/showcase/b2b-study/product-ui.md"`): roundness 0 → 42 (6/8/12), depth → 10 (borders), colorfulness 20, `overrides.type.weightCount` 3, `raw.numericStyles` true. Warmth → 40 (cool-neutral greys #f3f4f6 … #232427 without a slate cast). Face: Hanken Grotesk (SIL OFL), tabular figures confirmed by measurement.

## Type (one family)
Hanken Grotesk only. The record ID (`cmp_8d1fx2q7`) uses the text face with tabular digits; no mono face was needed. Three sizes:
- 12 label/meta: chip text, counts, timestamps, group headers, section titles
- 14 body: everything else
- 20 title: the company name (`title-lg`)
Weights 400 / 500 / 600 (600 only on the company name and the palette match highlights).

## Color
Cobalt `accent-11 #1a41a9` (8.9:1 on white) on links only: the domain, the email subject, "Hide changes", "Show all 24", "Add to list"; and `border.focus` (accent-9) with an accent-4 halo on the field being edited. Selection in the sidebar and in the palette is a neutral fill, as in the references. No status colors appear; the deal stage is a neutral dot (hollow for the old stage, filled for the new).

## Where I stepped outside the tokens, and why
- `--kv: 34px` key-value row height: no row token.
- `--sep` (neutral 4) and `--line` (neutral 5): no separator role.
- `--float` palette shadow: depth 10 zeroes `elevation.overlay`.
- Scrim blur 2 px on top of `color.overlay.scrim`-like tint: no blur token (and the palette's scrim uses a lighter tint than the token's 45%, so the record stays legible behind it).
- The focus halo (accent-4, 3 px) around the inline edit field: no "focus halo" role.

## Checks
- `engine.py validate`: passes, 0 warnings, 5 notes.
- `preflight.py html --medium web`: the first run flagged 9 px avatar initials (M8); the owner avatar became a person icon. Final run: 1 error, the M9 false positive (Hanken Grotesk loads from a Google Fonts `<link>`; Playwright confirmed 400/500/600 loaded).
- Rendered measurements (Playwright, 1440 × 900, both frames): sizes 12/14/20; weights 400/500/600; one family; no gradients; `backdrop-filter` only on the palette scrim; the only in-flow box-shadows are 1 px rings (active nav) and the 3 px focus halo.
- Contrast (measured): tertiary text #61646b is 5.9:1 on white, 5.0:1 on the hovered row; links 8.9:1.
- Dates are consistent with the frame's "today" of Wed Oct 14, 2026: "Mon, 4:52 PM" is the "2 days ago" email; last week's events fall on Oct 5-7.

## Rounds (self-audit against Attio d76ba56f, Linear d0f8ebba and Stripe 1a4aa88b at 1440 wide)
1. **Score 3.** In the details panel, "Parent company" ran into its value and the list names ran into their stage tags (128 px label column); the edit field's focus border was clipped by `overflow: hidden`, showing only top and bottom lines; flex gaps put stray spaces inside the chips ("2 days ago , email"); "Search or run a command" wrapped onto two lines in the sidebar; "Last week" held an Oct 2 event.
2. **Score 4.** Label column 144 px; lists became their own rows (name, "since today", stage tag); the edit field is fully drawn; chip text wrapped in one span; sidebar reads "Quick actions ⌘K"; events re-dated. Palette frame rendered: the flex gap split highlighted matches ("Change st age…"), and one result ("ta-s-k") did not contain the query.
3. **Score 5.** Palette labels wrapped in one span so highlights sit inside words; the non-matching row replaced by "Add stakeholder…"; the result count corrected from 14 to the 7 shown. Removed the 9 px initials. Next to Attio at the same width the record reads as a product someone uses daily: a change record with deltas ("+$14,500.00", "+21 days"), a quoted customer reply that names a date, and empty fields that invite input.

Honest limits: the September group is collapsed, so the lower 100 px of the feed is empty; the palette's context chip is a design choice not seen in the references.

## Process findings
1. **P1 by hand a third time** (roundness 0 from "focused, trustworthy" + dense). F-002 in this folder.
2. **Engine bug:** `raw.monoFace "=textFace"` is accepted but written into CSS literally (`--ds-font-family-mono: =textFace, ui-monospace, …`). displayFace resolves the same syntax. Reverted to `ui-monospace`. F-001 (bug).
3. **No key-value row or inline-edit tokens** for record panels. F-003.
4. **No command-palette tokens** (width, offset, row height, keycaps, scrim blur). F-004.
5. **A shared engine changed under me:** one `engine.py build` failed with `NameError: name 'default_profile' is not defined` (engine.py line 692) while another session was adding a `profiles` mechanism to the engine; the next build a minute later passed. Not an engine defect, but parallel sessions editing the engine can break builders mid-run.
6. **Helped:** a single text face plus `numericStyles` covered IDs and money without a mono face; the accent-11 link color passed 8.9:1 with no tuning.

## Fix round 2026-10-14
After the independent audit (`audit/product--03-corvane-record.json`). Renders: `shot.png`, `shot-edit.png`, `shot-palette.png`, each 1440 × 900 at 2×.

- **List date matches the timeline.** The Lists panel said "Enterprise pipeline · since today", but the timeline shows the company moved there on Oct 6. It now says "since Oct 6".
- **One temporary state per frame.** The main frame keeps the expanded change diff, which is the piece's story: the timeline records old and new values. The Description field shows its saved value, and the hovered "Parent company" row is gone. The field mid-edit (focus ring and caret) moved to its own frame, `?state=edit` (`shot-edit.png`). The ⌘K frame is unchanged apart from names.
- **Names.** The workspace Halyard Systems is now Aldermoor Systems, and the record Tessaly Aerostructures is now Lathom Aerostructures (`lathom-aero.com`). Tomás Herrera is now Gareth Penhale, Joanne Okafor is now Joanne Achterberg, and Eitan Varga (Varga is in styles/02) is now Eitan Mizrahi. Web searches found no real company called Aldermoor Systems or Lathom Aerostructures. (A first pick, Selwick Systems, was dropped because mockups/10 has a Stellwick Packaging.)
- **Brand kept.** Corvane appears in no other piece. While this round ran, `styles/01` had a brand one letter away, "Corvale", but another session rebuilt that piece and the name is gone (`brand/showcase/NAMES.md`).
- **Deal name.** "Tessaly · Fleet expansion" is now "Lathom · 3-site rollout". A tier-2 maker of wing ribs has no fleet, and the deal is seats for three sites (Eitan's security note: "SCIM for 3 sites").
- **Re-checked.** This week's events fall on Mon Oct 12 and Wed Oct 14, and last week's on Oct 5-7. The counts per group are 4 and 3. $48,000 to $62,500 is +$14,500. Nov 14 to Dec 5 is +21 days. "Last interaction 2 days ago" matches the Mon 4:52 PM email.
