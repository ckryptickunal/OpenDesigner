# 06 · Security settings and audit log · Ferrule

Final renders, each 1440 × 900 at 2×:
- `shot.png`: Settings › Security
- `shot-audit.png`: Settings › Audit log, from `index.html?frame=audit`

Final self-audit score: **4 of 5**. The audit-log frame alone would score 5.

## Direction
Ferrule is a fictional data platform with warehouses, schemas and API keys. The screens are its workspace settings for Larchfield Mutual, a fictional insurer with 214 members on the Business plan. The users are IT admins and security engineers. This is the buyer's view of whether Ferrule is "enterprise-ready", so every policy states its exact effect and who it applies to.

The SAML state is a realistic halfway point. The domain was added at 12:47 UTC and its TXT record hasn't been found yet, so both SAML switches are disabled and the prerequisite says why. Plum is used only on switches that are on and on focus. The primary button is near-black.
Feel words: **secure, quiet, precise**. The engine dropped "precise".

The study's section 5.6 is followed point by point:
- **Settings nav:** grouped by owner (Account / Workspace / Security and access / Billing).
- **Authentication rows:** each has a title, a consequence line and a switch.
- **SAML panel:** the notice "Verify a domain first", read-only ACS URL and Entity ID in mono with Copy buttons, an IdP metadata field with an "e.g." placeholder, and separate Turn on and Require switches, each with its consequence.
- **SCIM:** "Available on Enterprise" as a quiet inline label, not a banner.
- **Sessions:** session length and idle timeout.
- **Danger zone:** a red-tint "Sign out all members" that names its count (187 active sessions, including yours), and the workspace ID with Copy. These two sections are below the 900 px fold, as on a real long settings page.
- **Audit log:**
  - each row has the actor, an action sentence with a mono event code, an IP with its city and country, and the time in UTC with seconds
  - a UTC / Local switch, filters for date, actor, event and IP, and Export CSV
  - the retention limit is stated
  - one row is expanded into a key-value log entry with a before-and-after diff
- **Realistic actors:** people, a service account (hr-sync), an API key (claims-archive ••••3f9a), a system bot (warehouse-scheduler) and vendor support under an access grant (SA-2291).

## References
The study's references for 5.6 are [Linear security](https://mobbin.com/screens/34f99905-3147-4e31-9d52-c091158c4ba3), [Langdock SAML](https://mobbin.com/screens/2f35d1d3-903e-40ab-84d6-09375a5e5535) and [PlanetScale audit log](https://mobbin.com/screens/d7448333-6400-49dd-b11f-e48e4e229200). Mobbin didn't return those three for my searches. I compared against these, all opened in this session:
- [Customer.io security settings](https://mobbin.com/screens/53808563-634e-480f-ae02-460183581cb2): each policy is a bordered block with an exact effect ("This only applies to non-SSO accounts"), and the session expiry is a number plus a unit select. It taught me the consequence lines.
- [Twenty security](https://mobbin.com/screens/e5212b5d-0c11-436d-86f1-583aa0efee80): an "SSO · Enterprise" lock chip, grouped auth-method rows with switches on the right, and a centred settings column. It taught me row grouping and inline plan gating.
- [Linear API settings](https://mobbin.com/screens/fc41ba13-34f5-429c-8f96-d37e18311c2d): the grouped settings sidebar with "Back to app", sections separated by whitespace and hairline panels. It taught me the settings shell and its rhythm.
- [Customer.io audit logs](https://mobbin.com/screens/decad923-b3e9-4e22-8166-7b20e6c22140) and [Railway audit event drawer](https://mobbin.com/screens/3668d9f6-d6bb-4fdf-a4a8-97087947c044): filter fields for date range, team member, IP and event type, Export CSV, and an event broken into When / Who / What with an event ID. They taught me the audit filters and the expanded log entry.

## System (engine)
`sketch --name "Ferrule" --brand "#7b3577" --audience dense --platforms web --feel secure,quiet,precise --theme system-light-dark --delegated all --surfaces operate`

The sketch kept the plum (8.02:1 on white) and called it "a deep magenta", which is close enough. I then set the P1 profile by hand, each with `--set-by delegated`:

| Setting | Value |
|---|---|
| dials.roundness | 42 (6 / 8 / 12 px) |
| dials.depth | 10 |
| dials.expression | 25 |
| dials.warmth | 42 |
| overrides.type.weightCount | 3 |
| raw.numericStyles | true |
| raw.textFace / monoFace | Red Hat Text / Red Hat Mono: one superfamily, SIL OFL, tabular figures checked in Chrome |

`border.focus` is accent step 9 (plum), which is what the spec asks for. There are no charts, so there's no chart palette.

## Type scale
Three sizes:

| Size | Role | Where |
|---|---|---|
| 12 | Label and caption | Consequence lines, sub-labels, event codes, IPs, mono values |
| 14 | Body | Body text, row titles, buttons |
| 20 | Title | Page title (`title-lg`, 600) |

Section headings are 14/600 rather than a bigger size, because the content column is a form and a larger section title would compete with the page title. The weights are 400, 500 and 600, checked in the DOM. Mono appears only on the ACS URL, entity ID, workspace ID, event codes, event and request IDs, IP addresses and the diff keys.

## Where I stepped outside the tokens, and why
- **Near-black primary.** `--primary: color.bg.inverse`, because `bg.action.primary` is the plum and the spec reserves plum for switches and focus. This is the same engine gap as in 04.
- **Switch.** The 32 × 18 switch is hand-sized; there are no switch tokens. Its off track is neutral 8 (3.65:1) so the control's boundary passes WCAG 1.4.11. The engine gives no "control-off" role, and neutral 7 looked nicer but measured 1.64:1.
- **Hairlines.** Neutral 4 and 5, because there is no separator role.
- **Small parts.** The "Available on Enterprise" gate label, the 26 px actor avatars and the 60 px setting rows are hand-sized; there are no badge or row tokens.
- **Knob shadow.** The switch knob's 1 px shadow is the only shadow on either frame.

## Data
- All names, domains (`larchfieldmutual.com`, `id.ferrule.cloud`) and IDs are invented.
- The IPs come from the documentation ranges in RFC 5737 (192.0.2.x, 198.51.100.x and 203.0.113.x).
- The times are consistent with each other:
  - the session-length change at 13:58:07 is the "Last changed by Amara Sjöberg at 13:58 UTC" line on the Security frame
  - the domain was added at 12:47:33, before the 13:52 TXT check
  - Local time is 15:58:07 CEST
  - the 2FA policy was turned on on Oct 13 at 22:17:03 UTC, which is why "12 members haven't set it up"
- The counts agree: 214 members appears in the nav, the lede and the log entry's "Applies to". There are 187 active sessions, and all 214 members sign in with a password, the only method that is on.

## Checks
- `engine.py validate`: no errors and no warnings. 5 notes: APCA advisories, orphan steps, the 24 px control note and asset hooks.
- `preflight.py html --medium web`: 1 error, a false positive (M9: Red Hat Mono loads from a Google Fonts `<link>`; the DOM check confirmed Red Hat Mono 400 and Red Hat Text 400/500/600 loaded). Two real problems were caught earlier and fixed:
  - 10 px `<small>` labels in the SAML fields
  - 11 px avatar initials
- `engine.py review`: 27 hard-coded values remain. They are component sizes with no token: the switch, the avatars, the row heights and the knob shadow.
- Keyboard:
  - every switch is a `button` with `role="switch"` and `aria-checked`, and toggles on click
  - the disabled SAML switches have labels that say why ("needs a verified domain")
  - focus shows a 2 px plum ring
- **Not done:** a dark-mode render. The engine validates dark mode, but neither frame was rendered dark.

## Self-audit rounds
I compared each round with Customer.io, Twenty and Linear at 1440 px.

1. **Round 1: 4/5 for the audit frame, 3/5 for the security frame.** SCIM's "Available on Enterprise" sat below the 900 px fold, so the frame failed the brief. Each section had a description line that repeated its title. The breadcrumb took a line. The SAML panel carried two sub-headings and a separate save footer.
2. **Round 2: 4/5.**
   - The breadcrumb and the redundant section descriptions are gone.
   - Field labels now carry their own small hints ("Reply URL in some providers", "Also called audience URI").
   - Upload XML and Save sit inline with the metadata field.
   - The SAML consequences are one line each.
   - SCIM is now visible above the fold. The metadata placeholder wrapped and the Save button overflowed the panel.
3. **Round 3: 4/5.**
   - The metadata field truncates instead of wrapping, with a shorter placeholder.
   - The "12 members" link no longer breaks across lines.
   - "Sign-in failed" no longer repeats the red "Failed" tag.
   - The two sub-12 px sizes are fixed, and the off-switch contrast is raised.

**Why it's a 4 and not a 5.**
- The security frame's right side holds only the on-this-page list. That's correct for a settings page but leaves the canvas quiet.
- The "K" workspace tile is the generic initials device.

The audit log holds up next to the references in density, honesty and data. I would score it 5 on its own.

## Process findings
1. **Gap: no component tokens for switches, badges, status dots or setting rows.** `engine.py review` then reports these hand-made sizes as hard-coded values. It can't tell "no token exists" from "you skipped the token". (F-001)
2. **Bug: the near-black primary needs a hand alias.** It has to be aliased to `color.bg.inverse` by hand. Same as 04 F-001. (F-002)
3. **Helped:**
   - `text.danger` with `bg.danger.subtle` gave the danger-zone button.
   - `border.input` gave a 3:1 field edge.
   - The plum stayed exact.
   - The compact density set `size.control.sm` and `size.control.md` to 24 and 32, which is right for settings.

## Fix round 2026-10-14
After the independent audit (`audit/product--06-ferrule-security.json`). Renders: `shot.png` and `shot-audit.png` (`?frame=audit`), each 1440 × 900 at 2×.

- **API key name fits its time.** A key called "etl-nightly" exported data at 13:22 UTC (15:22 CEST). It is renamed "claims-archive", which matches what it does (it exports `claims.payments_2026` to the `ext_archive` stage) and runs at any hour.
- **Email sign-in link.** It was off but "used by 6 members in the last 30 days". It now reads "Turned off Oct 9; 6 members used it in the 30 days before."
- **Sign-in methods add up.** Only the password method is on: the email link is off and SAML waits for a verified domain. So "31 members use this method today" left 183 members with no way in. It now reads "All 214 members use it now; it is the only method on." "Require SAML for everyone" now says "Password sign-in stops", because the link is already off.
- **Names.** The customer Kestrel Mutual is now Larchfield Mutual (`larchfieldmutual.com`, ACS path `larchfield-mutual`, tile "L"). Kestrel is the showcase's flagship name and also a real listed insurer. Amara Lindqvist ("AL") is now Amara Sjöberg ("AS"). The deactivated member `tomas.becker@` is now `jakob.hensel@`. A web search found no insurer called Larchfield Mutual.
- **Count.** "1,284 events" is now 1,146, because 1,284 also appears in the hero and in Quoin.
- **Re-checked.** 13:58:07 UTC is 15:58:07 CEST on Oct 14, since CEST runs until Oct 25. The domain was added at 12:47:33, before the 13:52 TXT check. 2FA was required from Oct 13 at 22:17:03. The IPs are from RFC 5737.
