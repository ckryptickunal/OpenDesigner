# Premium B2B product UI: a Mobbin study for OpenDesigner

Study date: 2026-10-14. Purpose: show what premium B2B and enterprise product screens do, so that (1) our next showcase pieces pass as real B2B products, (2) OpenDesigner's builders learn checkable rules, and (3) OpenDesigner's questions and defaults for B2B products get better.

**Method.** I ran 28 screen searches and 2 flow searches on Mobbin (platform web) and looked at every returned image. That came to about 260 screens and 11 flows. I went wide across 8 screen types, then went deeper on the products that kept looking best: Linear, Stripe, Vercel, Attio and Mercury, plus Notion. Ramp, Datadog and a real Retool admin app never came back from Mobbin. Two Ramp-named searches returned other products, so I used Mercury, Airwallex and Navan as the finance references and Vercel, Neon, Sentry and Supabase as the observability references.

**How sure the numbers are.**
- Mobbin returns previews about 768 px wide. Desktop captures look about 1440 px wide, so I divided measured preview pixels by about 0.53.
- Every px value marked "≈" is an estimate, roughly ±15%. Treat these as ranges. They are not specs.
- Hex values for borders and greys can't be read reliably from compressed previews, so those are marked [inferred].
- I didn't download or save any image. Each reference is cited only by its `mobbin_url`.

**OpenDesigner defaults.** I read them from `levers.json`, `questions.json` and the stage files. I also produced them with a real engine run in a scratch folder outside the repo: `engine.py sketch --audience dense --platforms web --feel professional,minimal,technical`, then `resolve` and `validate`. Then I re-read the generated `tokens.css` myself. Section 4 has the values.

**Judgement calls** are marked [inferred]. Names of real companies appear here only as references. None of them may appear in our designs.

---

## 1. The top-tier signals, in ten lines

1. **One accent, spent sparingly.** It goes on the primary action, selection, links, checkboxes and focus. Everything else is greys. Status color lives in small glyphs and dots, or in tinted badges that carry an icon and a word.
2. **Small, calm type.** Body text is 13-14 px and meta text is 12 px. Two or three weights (400/500/600). Page titles are about 20-28 px. Display type never appears inside the product.
3. **Rows of about 34-42 px for one line, and about 56-78 px for two lines.** Rows are split by hairlines. There's no zebra striping, and no vertical gridlines except in spreadsheet-like views.
4. **Numbers are set like a ledger.**
   - Right-aligned and tabular.
   - Currency code shown, cents de-emphasized.
   - An em dash (—) for empty cells.
   - Mono only for IDs, hashes, keys and codes.
5. **Hairlines and one tonal step instead of shadows.** Shadows appear only on things that float: menus, popovers, dialogs, toasts and the bulk-action bar.
6. **Small, consistent corners.** About 6 px on controls, 8 px on cards and panels, 10-12 px on overlays, and about 4 px on badges.
7. **Charts are quiet instruments.**
   - A 1-1.5 px line in the accent or grey.
   - Labels only at the ends of each axis.
   - The comparison period dashed or grey, and an incomplete period dotted or hatched.
   - An "Updated 11:08" freshness stamp.
8. **Data looks real.** Odd amounts with cents, mono IDs, real-looking names and emails, timestamps with a time zone. Counts appear everywhere: "6 results", "1/2 seats", "28 of 75".
9. **Every consequential action names its consequence.** It says how many items, what happens next, and whether it can be undone. Then it offers Undo or Reopen.
10. **Keyboard and state are always present, and decoration never is.**
    - Always present: ⌘K, shortcuts listed in menus, saved views, "1 issue hidden by filters", inline "Available on Enterprise".
    - Never present inside working screens: gradient blobs, glass, emoji, mascots or hero illustrations.

**What separates the top tier from average B2B.** Average B2B products use the same layouts. They get the materials wrong:
- They put a saturated filled pill on every status. Examples: [ClickUp](https://mobbin.com/screens/121f6597-00b0-42f6-80bb-d026b24d5ed4), [Employment Hero](https://mobbin.com/screens/dc27e1a5-e4e2-4d37-93e4-560024a3e7be).
- They shout an exception on every row. Examples: "No manager" in red on [Qatalog](https://mobbin.com/screens/1ab44f61-585c-40f2-b635-afc480c4fad8), "This needs a category" in yellow on [YNAB](https://mobbin.com/screens/f08c0bf3-14ab-437e-9c15-0475bebbe4fc).
- They put 3D illustrations in empty states. Examples: [Remote](https://mobbin.com/screens/8dceed64-1b82-4fd8-a9ee-ef3bc9f75318), [Salesforce](https://mobbin.com/screens/bf414371-b0bb-48c1-b294-29c292829ca7).
- They put promo carousels and gradient headers inside the app: [Deel home](https://mobbin.com/flows/660b306b-5ba2-400e-bbb8-86f4e4c75690).
- They draw charts with rotated axis titles, gridlines in both directions and rainbow series. Examples: [LangChain](https://mobbin.com/screens/b43a980d-6a77-48d5-b764-d697475a157c), [Replit](https://mobbin.com/screens/f929df2e-7ee2-4f62-ab93-eb0ce891df7b).
- They add emoji and gamification: [beehiiv](https://mobbin.com/screens/447a8ac8-9cea-4831-95d8-3d8c1b0a9edb) ("Hi John 👋", "3 week streak").

The top tier differs mostly by **what it leaves out** and by **how exact its numbers, states and copy are**.

---

## 2. Rules per screen type, with evidence

Each rule is written so a builder or a check can test it. "Evidence" names a product and its `mobbin_url`.

### 2.1 Dense data tables (filters, bulk actions, column controls, row states)

**Rules**

**Layout and rows**
- **Row height:**
  - About 34-36 px for a dense single line ([Stripe](https://mobbin.com/screens/140880ca-003b-4498-8932-c09c223ed9de), [Attio](https://mobbin.com/screens/5bb2a956-b937-497e-bd31-afc2616bb111)).
  - About 40-42 px for an issue list ([Linear](https://mobbin.com/screens/ed670cda-0527-4716-a1a6-0159f12c4f42)).
  - About 48 px for finance lists that are comfortable rather than dense ([Mercury](https://mobbin.com/screens/a930c1be-a15a-4dbc-a843-8a62ac0febf5)).
  - About 56-78 px when a cell has two lines ([Vercel](https://mobbin.com/screens/b9d9cc23-34a1-434c-a4ed-52a2a4f49bb7), [PlanetScale](https://mobbin.com/screens/d7448333-6400-49dd-b11f-e48e4e229200)).
- **Separators:** one hairline between rows.
  - No zebra striping. No vertical gridlines, except in spreadsheet-like grids such as Attio.
  - Group header rows are a light grey band with a status glyph, the group name and a count: Linear's "In Progress 5" ([Linear](https://mobbin.com/screens/ed670cda-0527-4716-a1a6-0159f12c4f42)).
- **Column headers:** 12-13 px, sentence case, medium weight, muted, with a sort arrow on the sorted column (Stripe, Attio, Mercury).
  - Some data-platform products use 11 px uppercase tracked headers instead ([Snowflake](https://mobbin.com/screens/f47ed82d-47bd-45d3-b0a2-ecf5a8ab2e50), [Vanta](https://mobbin.com/screens/41659ab7-5710-4abf-91ca-c6bf482c9b0b)).
  - Pick one style per product.
  - Linear and Vercel drop column headers entirely and let each cell's form explain itself.

**Numbers and data**
- **Numbers:** right-aligned and tabular, with the currency code shown.
  - Mercury and Grok set cents smaller or lighter: "$1,001.00", "−$2.55" ([Mercury](https://mobbin.com/screens/a930c1be-a15a-4dbc-a843-8a62ac0febf5), [Grok](https://mobbin.com/screens/1bc2df4c-3505-4cad-95f9-16db8bf921a1)).
  - Stripe treats amount as the identity column: left, bold, with a muted code, as in "US$1.00 USD" ([Stripe](https://mobbin.com/screens/140880ca-003b-4498-8932-c09c223ed9de)).
  - Money in is green text. A failed amount is struck through and gets a small outlined "Failed" badge (Mercury).
  - Empty cells show "—" (Stripe, Mercury).
- **IDs, hashes and branches use mono.** Names and text never do: "239A2C49-0002" ([Stripe search](https://mobbin.com/screens/3a15e105-2b7d-4857-9fb6-478731427ebb)); "main", "15c35eb" ([Vercel](https://mobbin.com/screens/b9d9cc23-34a1-434c-a4ed-52a2a4f49bb7)).

**Row states**
- **Status is quiet:**
  - In Linear and Vercel it's a dot or glyph plus a word, such as "• Ready" or "• Error".
  - In Stripe and Mercury it's a tinted badge about 18 px high with an icon: "Succeeded ✓", "Failed ×", "Incomplete ◷".
  - Labels are neutral chips with only a colored dot ([Linear](https://mobbin.com/screens/ed670cda-0527-4716-a1a6-0159f12c4f42)).
- **De-emphasis is itself a row state.**
  - Transfers are grey text ([Origin](https://mobbin.com/screens/bc9b0fad-17b8-4d8b-8dae-56f95d45d8b0)).
  - A failed amount is struck through (Mercury).
  - Selected rows get a pale accent tint ([Attio](https://mobbin.com/screens/5bb2a956-b937-497e-bd31-afc2616bb111)).
  - Only true exceptions get color.

**Filters, views and columns**
- **The filter bar sits above the table.** Each filter is a chip that shows its current value, and you can clear it:
  - "Date and time | Last 3 days", "Status | Cancelled, Blocked", with the value in the accent ([Stripe](https://mobbin.com/screens/373146e1-8686-43b0-8a10-5da707dc8873)).
  - Stripe adds a "Clear filters" link.
  - Filter popovers are small forms: "is in the last [3] [days]", a time-zone radio and a full-width Apply ([Stripe](https://mobbin.com/screens/5aba8f78-028a-4ad6-81f1-6ca698a41451)).
  - Filter menus show a live count on each option: "High 14 issues" ([Linear](https://mobbin.com/screens/2579f037-4e90-4330-ac35-19323ca9828a)).
- **Status tiles act as quick filters.** Each tile carries a count, as in "All 6 / Succeeded 1 / Refunded 0 / Failed 3" ([Stripe](https://mobbin.com/screens/140880ca-003b-4498-8932-c09c223ed9de)). A summary strip is the alternative: "Net change this month / Money in / Money out" ([Mercury](https://mobbin.com/screens/a930c1be-a15a-4dbc-a843-8a62ac0febf5)).
- **Column controls:**
  - "Edit columns" lists "Fixed columns", checkboxes and drag handles ([Stripe](https://mobbin.com/screens/140880ca-003b-4498-8932-c09c223ed9de)).
  - The header menu offers sort asc/desc, move, rename and hide ([Attio](https://mobbin.com/screens/f87ae525-00b1-405b-b82c-a38a96811837)).
  - Table options include a time zone and "Show graph" ([Mercury](https://mobbin.com/screens/b83e3032-537b-4bad-8449-830cb416fa79)).
- **Views are saved objects.**
  - When you change a view, "Discard changes" and "Save" appear ([Attio](https://mobbin.com/screens/1feec693-b9aa-4028-8c79-0271a6b7e4d5)).
  - The board footer says "1 issue hidden by filters | Clear Filters" ([Linear](https://mobbin.com/screens/410846e7-09d4-4ed8-baf2-ec94d96c29f4)).

**Bulk actions and table footer**
- **Bulk actions use a floating dark bar at the bottom center.** It holds the count first, 3-4 verbs, a "More" menu and a close ×:
  - "3 selected | Add to List | Send email | Run workflow | More" ([Attio](https://mobbin.com/screens/5bb2a956-b937-497e-bd31-afc2616bb111), [YNAB](https://mobbin.com/screens/f08c0bf3-14ab-437e-9c15-0475bebbe4fc)).
  - A destructive bulk action asks first, naming the count and the consequence: "Remove 3 records from list. Are you sure? Removing records will also delete their list attribute data." The button is red and repeats the verb ([Attio](https://mobbin.com/screens/f6aa5c36-a41b-432f-a620-5248fb8bc7b0)).
- **The table always says how much is there:**
  - "6 results" (Stripe), "33 count" plus "+ Add calculation" per column (Attio), "Showing 1 to 2 of 2" ([Whop](https://mobbin.com/screens/6472b575-afa7-4fb6-9a91-dbfaa034e121)).
  - The export flow is honest: "Preparing export…", then "Your export is ready. If you don't see your file, you can try downloading it again." ([Stripe](https://mobbin.com/screens/0e0a134f-11bb-435d-bc59-23da4d8e753b)).

**Average looks like:**
- Saturated uppercase pills on every row ([ClickUp](https://mobbin.com/screens/121f6597-00b0-42f6-80bb-d026b24d5ed4), [Jira](https://mobbin.com/screens/8ee03824-8a10-4a60-bdf1-727c0e9ecbb1)).
- Zebra rows plus many green buttons ([QuickBooks](https://mobbin.com/screens/799374e9-c3b3-4dbe-9a44-55bdcff00996)).
- Rainbow tag pills and centered bold titles, which is the "built fast in an internal-tool builder" look ([Retool](https://mobbin.com/screens/f074d0b0-63f2-41a9-83b2-9d2e8cda443b)).

### 2.2 Analytics and overview dashboards (KPI rows, charts, comparison, time range)

**Rules**

**Page structure**
- **Time range and comparison come first, as controls in one row.**
  - "Last 7 days · compared to · Previous period · Daily" ([Stripe](https://mobbin.com/screens/a31f7d76-ade4-4cae-a816-a4c9b33814c3)).
  - Segmented presets "4w 3m 6m 1y" plus "Compared to Similar businesses" ([Stripe Radar](https://mobbin.com/screens/63b47007-2529-42d0-8701-6ef4ff10342e)).
  - An environment select plus "Last 12 hours" ([Vercel](https://mobbin.com/screens/38a44719-a4b0-482b-bb40-283eec56ebd4)).
- **KPI layout:** label (12-13 px, muted), then value (≈20-32 px, weight 500-600), then a comparison line: "MYR 0.00 previous period" and a small delta badge (Stripe). There are two styles:
  - KPIs as plain text in a row with no cards ([Snowflake](https://mobbin.com/screens/2b274a0b-53e6-4e30-a10b-26a6366707af)).
  - KPIs as bordered tiles where the selected tile drives the chart ([Amplitude](https://mobbin.com/screens/fe0b2859-c23a-4e24-a0f0-7e527fdc9197)).
- **Widgets have no chrome until you edit them.** Stripe's overview widgets are separated by whitespace and hairline rules. Borders, shadows and an × appear only in edit mode ([Stripe edit](https://mobbin.com/screens/673e89af-fe9e-4ab9-ac27-435dedf21888)). Every widget ends with "View more" and "Updated 11:08".

**Chart style**
- **Lines:**
  - 1-1.5 px, with no smoothing dots and no gradient fill.
  - Mercury is the exception: one hue with a very pale fill ([Mercury](https://mobbin.com/screens/a17be959-5966-495f-a230-65fcdcc333cf)).
- **Axes:**
  - Y labels at min and max only, or 3 ticks. X labels only at the two ends: "3 Dec / Today", "12h ago / 1m ago" (Stripe, Vercel).
  - Horizontal hairline grid only.
  - Axis labels are about 11 px and muted.
- **Comparison and incomplete data:**
  - The comparison period is grey or dashed ([Google Analytics](https://mobbin.com/screens/f4f2cebe-5496-4959-9fbb-fe37fe2a5dd6); [Stripe payment methods](https://mobbin.com/screens/cb9a784d-e7d5-451b-88a8-bac710506120) shows the baseline bar grey and the focus bar in the accent).
  - An incomplete period is dotted ([Amplitude](https://mobbin.com/screens/fe0b2859-c23a-4e24-a0f0-7e527fdc9197)).
  - Inactive periods are hatched ([Neon](https://mobbin.com/screens/c5ee5c89-e7ad-43fc-828a-46315320e455)).
- **Series colors:**
  - Small multiples use grey lines: 4 charts with no fill ([Stripe Billing](https://mobbin.com/screens/80db4fcd-360a-4ee9-8be0-f69f7edf83f8)).
  - Categorical color appears only when the series really are categories: Vercel's usage dots per product ([Vercel usage](https://mobbin.com/screens/b7b0e5e1-192b-4306-b2a6-88bca0d49bb6)), and Stripe's single stacked status bar with a legend list ([Stripe](https://mobbin.com/screens/673e89af-fe9e-4ab9-ac27-435dedf21888)).

**Tooltips, honesty and narrative**
- **Tooltips are mini tables:** series × Count / Rate / Volume ([Stripe Radar](https://mobbin.com/screens/bed8e57d-ab3d-401f-9a4d-ab14bfdcec79)). Neon uses mono values with units: "Allocated: 1.07 GB" ([Neon](https://mobbin.com/screens/c5ee5c89-e7ad-43fc-828a-46315320e455)).
- **Data is honest:**
  - "Top 6 groups extrapolated from 9k span samples" ([Sentry](https://mobbin.com/screens/6ab05b5f-3384-492f-882b-bf2aa462a2f8)).
  - "Not enough data to display a trend." ([Grok](https://mobbin.com/screens/661ddba6-bb26-4b5c-b1c6-9f3e9f2f743f)).
  - "No invocations in this time range" inside an empty chart card (Vercel).
- **Narrative sentences can carry the headline number.** "Gross volume for the month of December so far is **MYR 2.00**." ([Stripe reporting](https://mobbin.com/screens/6e67d584-93ed-426b-908a-e467c2ab6a18)). Benchmarks appear as "48th percentile" badges, a "0% median" and a grey peer band ([Stripe benchmarking](https://mobbin.com/screens/21e1c3f3-1b45-4140-a208-4fd250a52533)).
- **Drill-in sits on the card title.** Vercel puts a chevron on each card title ("Edge Requests ›"). A searchable table sits under the charts ([Vercel](https://mobbin.com/screens/38a44719-a4b0-482b-bb40-283eec56ebd4)).

**Average looks like:**
- Rotated axis titles, gridlines in both directions, tinted chart cards ([LangChain](https://mobbin.com/screens/b43a980d-6a77-48d5-b764-d697475a157c)).
- Fat rounded bars ([WRITER](https://mobbin.com/screens/70317d27-8815-4253-bdff-dafe6cb5771b)).
- Rainbow donuts ([Basedash](https://mobbin.com/screens/4f4bfb27-f1a7-4aae-ba5a-543316cb782e)).
- A pink gradient area, a "↑100%" pill on every KPI and an emoji greeting ([beehiiv](https://mobbin.com/screens/447a8ac8-9cea-4831-95d8-3d8c1b0a9edb)).

### 2.3 Record and detail pages (activity timelines, side panels)

**Rules**
- **Layout:**
  - Breadcrumb, then the record header (logo or avatar, name, star), with secondary actions on the right.
  - A meta row of chips: owner, last interaction.
  - Tabs with counts: "Emails 73 / Team 1 / Notes 0".
  - The main column takes about 58-65%. A right panel of about 320-360 px holds the details ([Attio](https://mobbin.com/screens/d76ba56f-98c3-463f-9e1d-bbe4831ee47a), [Stripe](https://mobbin.com/screens/1a4aa88b-e0be-49b2-a87f-1264e0b5e786)).
- **The right panel is a key-value list,** with a muted label (icon plus label) and the value. Empty values are muted, editable placeholders:
  - "Set Description…" (Attio).
  - Verbs: "Set priority", "Assign", "Add label" ([Linear](https://mobbin.com/screens/d0f8ebba-34b7-469c-a708-1069e55a3e02)).
  - Values edit in place: Attio turns the field into a focused input on click ([Attio](https://mobbin.com/screens/4596651f-1527-4ddb-9cde-b19067b5753f), [relation picker](https://mobbin.com/screens/072188cc-ccb7-41d4-af44-c66842c7a9cb)).
  - Stripe uses label-over-value pairs, with mono IDs and a copy icon: "cus_RLKFqz68EhCJdl" ([Stripe](https://mobbin.com/screens/1a4aa88b-e0be-49b2-a87f-1264e0b5e786)).
- **The timeline records changes, not just events.**
  - Each event is a 16 px icon, a sentence ("Alex Smith changed Stage and 7 other attributes in Sales") and a muted relative time.
  - Events expand into a diff list: "Stage → Meeting", "Estimated contract value → $50,000.00".
  - Events are grouped by period ("This week", "June") and the groups fold ([Attio](https://mobbin.com/screens/d76ba56f-98c3-463f-9e1d-bbe4831ee47a)).
  - Stripe's payment timeline says what failed and why, with a dated "View details" ([Stripe payment](https://mobbin.com/screens/2cf3b950-fa12-475b-a34d-202923af949f)). Its refund line says what happens next: "It may take a few days for the money to reach the customer's bank account." ([Stripe](https://mobbin.com/screens/ebf7e9fe-326a-4459-ae16-f94aea16f56b)).
- **Money is shown as a ledger.** "Payment amount MYR 2.00 / Stripe processing fees − MYR 1.08 / **Net amount MYR 0.92**", right-aligned with a total rule ([Stripe](https://mobbin.com/screens/2cf3b950-fa12-475b-a34d-202923af949f)).
- **Empty sub-sections stay visible.** They show as a dashed box holding one muted line, "No credit grants" or "No metadata", with the (+) action on the section header ([Stripe](https://mobbin.com/screens/731c4495-3c95-42b2-9502-5a1b60ab96eb)).
- **Moving between records is built in.**
  - "28 of 75 in All Companies" with up and down arrows (Attio).
  - "2 / 5" with arrows (Linear).
  - Linear's inbox splits a list and a detail ([Linear inbox](https://mobbin.com/screens/beb9d6b3-ec34-46d7-9332-320fcb32a338)).
- **Drawers instead of pages for quick detail.** Mercury's transaction drawer has:
  - an autosave stamp ("✓ Saved")
  - a vertical mini timeline with UTC times
  - a GL code select, Notes and Attachments ("or email receipts to …")
  - Comments with "Mention a team member with @, press Enter to send." ([Mercury](https://mobbin.com/screens/b71279bb-6f4a-4ec2-83b7-9b73d5530ca4))
- **Changing money asks for a before and after.** Stripe's credit adjustment shows "Starting balance MYR 0.00 | New balance −MYR 2.00", with the new value in the accent. It has an internal-note field with "This is an internal note and will not be visible to your customer.", and the button says what it does: "Apply to credit balance" ([Stripe](https://mobbin.com/screens/bd229058-a354-43cf-a92f-2680531ba5a8)).

### 2.4 Settings: members and roles, permissions, SSO and security, audit log

**Rules**

**Settings layout**
- **The settings nav is grouped by who owns the setting:** Account / Workspace / Features / Admin (Security, Identity) / Access & billing ([Notion](https://mobbin.com/screens/e78d4c10-2356-4a90-9021-f3179d6435d2)). StackAI's groups are Workspace / Security (SSO, Provisioning, Audit Logs, Data Retention) / Integrations / Billing ([StackAI](https://mobbin.com/screens/4aaa3f09-719f-41e5-9310-b19989af1600)).
- **The content column is about 600-760 px wide.**
- **Every setting row has the same shape:** a 13-14 px medium title, a one-line consequence in muted 12-13 px, and the control on the right. Related rows are grouped in a bordered panel with hairline dividers ([Linear security](https://mobbin.com/screens/34f99905-3147-4e31-9d52-c091158c4ba3), [Notion general](https://mobbin.com/screens/9edd43f8-6e14-4c48-8d04-26c1f76e949d)).
- **Plan limits are stated inline, not hidden or advertised.**
  - "SAML & SCIM … Available on Enterprise" as a greyed row (Linear).
  - A small "Enterprise" chip ([ClickUp](https://mobbin.com/screens/6516b0ae-d90c-49f8-ab74-6f63d4d2ceaa), [Air](https://mobbin.com/screens/9b416e7d-4e24-4c72-b1d1-7bd806aafa82)).
  - Average products drop illustrated upsell cards into settings instead ([Otter](https://mobbin.com/screens/4ac0dbb9-40fd-43f9-b9b3-6f5f9557814b), [Mixpanel](https://mobbin.com/screens/c46926cd-0504-4499-9124-b3d0201b8b95)).

**Members and roles**
- **The members table:**
  - Tabs with counts: "Members 3 / Guests / Groups".
  - Each row has a name with a muted email below.
  - Role is a quiet text select ("Workspace owner ▾"). Status ("Pending" or "Invited") is a grey or tinted badge.
  - Row actions sit in a kebab menu, with Delete last and in red ([Notion](https://mobbin.com/screens/e78d4c10-2356-4a90-9021-f3179d6435d2), [Rows](https://mobbin.com/screens/8808750f-9991-4817-95d1-8eafcc747f7e), [Copilot](https://mobbin.com/screens/a69fb602-4ac4-4032-93d4-326fdcbaebb7), [Mercury](https://mobbin.com/screens/d620d481-387a-4cbc-b0a8-67463a5ecf73)).
- **Inviting states cost and scope up front.**
  - "Adding members is a billable action." ([Notion invite](https://mobbin.com/screens/9f7bcb4e-d95c-423d-b298-f40d338e310e)).
  - "Invitations expire after 1 week." with a seat meter, "1/2 seats allocated" ([StackAI](https://mobbin.com/screens/4aaa3f09-719f-41e5-9310-b19989af1600)).
  - "You're using 1 of 10 seats available." ([Contractbook](https://mobbin.com/screens/e2655ea1-7aee-4a7b-b182-553885892bb4)).
- **Every role option carries a one-line capability.** "Member: Can't change workspace settings or invite new members to the workspace" (Notion). "Invite a viewer: Can only follow others' work and review their documents." (Contractbook). Permission levels work the same way: "Open: Anyone can see and join this teamspace" ([Notion](https://mobbin.com/screens/46c17681-bc6e-4490-9855-8ae5c3bd6002)).
- **Permission matrices never use color alone.** Each cell is an icon plus a word: "✓ Edit", "👁 View only", "☒ No access", "N / A" ([Vanta roles](https://mobbin.com/screens/6dd83a18-ede6-44a5-adc5-2ebff239c7de)). Other forms:
  - A checkbox plus "Allowed" or "Not allowed" ([Langdock](https://mobbin.com/screens/66158752-4b06-43f5-ab8c-0bee0cfe6ea3)).
  - System roles show as locked, with the reason: "This is a system role and it cannot be edited or deleted…" ([PandaDoc](https://mobbin.com/screens/45354dd7-0e9e-4597-b6d0-7b0e0e307dc9)).
  - Editing has an explicit "Reset to default" and "Save updates" ([Workable](https://mobbin.com/screens/4d08132c-05e5-43e0-b90f-ed8af36fd105)).

**SSO and security**
- **SSO setup reads like an engineer's form.**
  - Read-only SP values in mono with Copy buttons (Audience URI, ACS URL).
  - Example placeholders: "e.g. https://idp.example.com".
  - Prerequisites stated as a notice: "You need at least one verified domain before you can activate SAML SSO." ([Langdock](https://mobbin.com/screens/2f35d1d3-903e-40ab-84d6-09375a5e5535)).
  - "Enable" and "Enforce" are separate toggles, each with its consequence ([Air](https://mobbin.com/screens/9b416e7d-4e24-4c72-b1d1-7bd806aafa82)).
  - SAML and SCIM are cards that each hold a "Configure" button and a "Learn more" footer ([Dub](https://mobbin.com/screens/67d657f0-5b61-4dbe-a1e1-4302fb2eaddf)).
- **A policy change says exactly what will happen.**
  - "After three logins, anyone who doesn't have 2FA set up will be required to enable 2FA using SMS…" ([ClickUp](https://mobbin.com/screens/6516b0ae-d90c-49f8-ab74-6f63d4d2ceaa)).
  - "…This only applies to non-SSO accounts." ([Customer.io](https://mobbin.com/screens/53808563-634e-480f-ae02-460183581cb2)).
  - Governance warnings: "always maintain more than one active user with full administrative permissions" ([Docusign](https://mobbin.com/screens/13ee7cf6-9f92-4a10-bb89-c71a8eac8137)).
- **Danger zone:** red-tint secondary buttons, each with a consequence line ("Permanently delete this workspace, including all pages and files."), plus a mono workspace ID with copy ([Notion](https://mobbin.com/screens/9edd43f8-6e14-4c48-8d04-26c1f76e949d)).

**Audit log**
- **Each row is actor + action sentence + target + IP + exact time.**
  - The action sentence comes with a mono event code ("deploy_request.queued").
  - The IP has its country below it.
  - The time is ISO with seconds, "2025-08-15 06:22:50", with a UTC switch in the header ([PlanetScale](https://mobbin.com/screens/d7448333-6400-49dd-b11f-e48e4e229200)).
  - Rows expand into a key-value "Log entry" ([Customer.io](https://mobbin.com/screens/5e4f44d9-4c65-4381-8681-d2921df2591e)).
  - Filters: date range, member, IP, event type. An "Export CSV" button. The time zone appears in each row or in the header ([Cloudflare](https://mobbin.com/screens/fa5520ff-fda8-435f-b65b-bf910991fab4), [Vanta](https://mobbin.com/screens/41659ab7-5710-4abf-91ca-c6bf482c9b0b)).
  - Retention limits are stated: "Data retention is limited to 14 days for organizations on the Free plan" ([Braintrust](https://mobbin.com/screens/ed5eb948-f7a2-411f-a73d-02393ab17dbb)).
- **A security overview row of policy tiles** (Password strength Off / 2-step verification Optional / External sharing Email and link), each linking to its setting ([Dropbox](https://mobbin.com/screens/99f74382-4244-40e8-bc02-a1c8664b381a)).

### 2.5 Billing and plans, usage meters, invoices

**Rules**
- **The plan summary is one line of facts:**
  - "Personal [Active] $25/month · Renews May 28, 2026" plus "Manage Plan" ([Obvious](https://mobbin.com/screens/331ff15c-a8b4-4ce4-adc2-29b4b1ab33f3)).
  - "Free [Current] – Your usage is shared across all projects and counts toward a single organization limit." ([Browserbase](https://mobbin.com/screens/e53c8b1d-85e9-4bde-a820-97da8cbf0720)).
- **Usage meters:**
  - A thin 4-6 px bar, a label with the used/included ratio, and a percent chip: "Workflow credits [7% used] 177 used / 2,500 included".
  - The reset date: "Credits will reset on September 6, 2024".
  - The bar turns orange only at the limit ([Attio](https://mobbin.com/screens/b61ed5a1-0a58-4744-8bab-277a6564ef7e)).
  - OpenAI adds a budget meter with tick marks: "$0.13 / $10 — Resets in 28 days. Edit budget" ([OpenAI](https://mobbin.com/screens/2bf4f941-a9a7-4308-aa0c-864135823830)).
- **Usage by product is a table with a sparkline in every row.** Each row has a colored dot, the metric, a sparkline in the series color, the usage ("10.89 seconds") and a right-aligned charge ("$0.00"). Rows are grouped by product family ([Vercel](https://mobbin.com/screens/b7b0e5e1-192b-4306-b2a6-88bca0d49bb6)).
- **Spend over time:**
  - Actual is in the accent and the forecast is grey. Example header: "Aug 2026 – Day 3 of 31 … Avg 3.1 credits/day" ([Snowflake](https://mobbin.com/screens/acf53a58-0fc7-49b7-93e0-f62c164ecc79)).
  - The budget is a dashed line (OpenAI).
  - Total, average and peak are shown with the trailing digits lighter ([Grok](https://mobbin.com/screens/1bc2df4c-3505-4cad-95f9-16db8bf921a1)).
- **The receipt is a ledger:** "Period allowance +$20.00", then usage charges "Custom Agent −$32.05" with "92.9% of period usage", all signed and right-aligned ([Cofounder](https://mobbin.com/screens/e9c05b3d-54e8-44db-9995-15ab9a95078a)).
- **The invoices table** has a mono reference ("97BC80AA-0001"), the total including tax, a status badge (Paid, Upcoming, Success with icon), a date and a download icon. "Cancel subscription" is a quiet secondary button at the bottom (Attio, Obvious, [Zapier](https://mobbin.com/screens/ff2d2205-2893-45a2-8244-936a2c60f1bd)).
- **Overage and billing state come with rates and dates:**
  - "…you will pay for each additional task … at a rate of 1.25x the cost of a task on your plan" (Zapier).
  - "Payment method removed – … A new card can be added at the beginning of the next billing cycle (Sep 1, 2025)." ([Render](https://mobbin.com/screens/3042dc86-958b-4bd6-8f23-25811c57d378)).
  - Render also adds an on-page table of contents for long billing pages.
- **The plan comparison inside the app is plain.**
  - Columns are split by hairlines, not cards.
  - Features are grouped by job, with concrete limits: "Reimburse up to 20 users/month + $5/additional user".
  - A monthly/annual switch shows the saving ("−15%") ([Mercury plans](https://mobbin.com/screens/11a7714a-6539-4b13-9885-94fbe1a2b39e)).
  - The Enterprise column lists DPA, "Domain verification, SAML-based SSO, and SCIM" and SLA. The trust facts are a plain footer line: "ISO 27001 certified and GDPR compliant. Data encrypted at rest with AES 256 and in transit with TLS 1.2+." ([Sana](https://mobbin.com/screens/ac6c7b82-6ced-408e-8ea5-50836a4ba830)).

**Average looks like:**
- A customer logo strip inside the upgrade modal ([Juicebox](https://mobbin.com/screens/ff01e3c7-e545-45ba-b76a-faf4ed5745e5)).
- A full-width orange banner plus a red over-limit bar and rotated axis titles ([Rox](https://mobbin.com/screens/e5e92b3f-be93-4e3d-a6db-5ccfd2181b83)).
- A plan card that's mostly empty, next to a large card graphic ([Profound](https://mobbin.com/screens/4016a872-372c-48e4-916c-70d4a85dff26)).

### 2.6 Onboarding and empty states in B2B tools

**Rules**
- **Empty state anatomy:**
  - A 32-40 px icon tile, or nothing at all.
  - A title of about 16-20 px: "No X yet" or "Add your first X".
  - One sentence about what will appear here or what the object is for.
  - One action plus "Learn more".
  - The table's column headers and filters stay in place, and sometimes skeleton rows as well. Examples: [Mercury](https://mobbin.com/screens/5cbd36cf-911a-4db6-bfaf-dea24625d3d4) ("Add your first customer / Manage all of your customer information in one place."), [Copilot](https://mobbin.com/screens/bf4b8506-2424-470f-9620-c286480f53dd), [Whop](https://mobbin.com/screens/a2f0b4e1-71f9-451c-bf14-c0c79ff7afce) ("A product is needed to organize access to your offering. + Create product · View docs"), [LangChain](https://mobbin.com/screens/8e744fe3-f3d0-482b-9b88-9e3f76a614eb).
- **"Filtered to nothing" is a different state, with different copy:** "No payments found – There aren't any results for that query. Try using different filters." ([Stripe](https://mobbin.com/screens/2b2d5f4f-bdd9-4186-b383-e3b30140a551)). AWS goes further and lists the possible reasons: "This could be due to a new account, unchanged costs, or your current filter selection." ([AWS](https://mobbin.com/screens/b59a3360-394f-4a2e-8cb7-eebfd3652808)).
- **The empty action is often secondary.** When the page header already holds the primary button, the empty state repeats it as a secondary button so the screen keeps one primary ([Front](https://mobbin.com/screens/3e18c118-95a2-4448-af5f-e78a0b148442), [Mercury](https://mobbin.com/screens/5cbd36cf-911a-4db6-bfaf-dea24625d3d4)).
- **An empty home page says there's nothing to do and what will appear:** "You don't have any tasks requiring your action." ([Mercury employee home](https://mobbin.com/screens/d3e836dd-8e36-46d6-ae65-72cd10aced61)).
- **Onboarding (premium):**
  - One centered column on near-white, the app mark, a one-line purpose and one button.
  - Step dots, and "I'll do this later" on every optional step.
  - Invites are a plain textarea ("email@example.com, email2@example.com…").
  - Keyboard use is taught during onboarding: "Meet the command menu … ⌘ K". Examples: [Linear onboarding flow](https://mobbin.com/flows/cbaf58a9-fd84-4afe-b214-e65b24484013), [Linear step](https://mobbin.com/screens/1e783aca-8b8e-4ae5-994d-284a8ddae491).
  - Developer products deliver the first value inside the flow: a real API key with "Make sure to copy your API key now as you won't be able to see it again", plus a curl sample. The flow lands on a home of next-action cards (verb, one line, arrow) ([Grok flow](https://mobbin.com/flows/0a988ace-d6ce-4fcb-a1bd-5e1db4b71236)).

**Average looks like:**
- Gradient waves, customer logos and a "Which solution would you like to start with?" chip wall, followed by a mascot video modal ([ClickUp flow](https://mobbin.com/flows/d46b7798-ba1e-4e4b-b8be-3c05123dd7aa)).
- An AI upsell modal on the first visit ([Productboard flow](https://mobbin.com/flows/54bce0a9-613c-4770-85e0-92c09b001e90)).
- 3D illustrations with marketing headlines in empty states ([Shopify](https://mobbin.com/screens/f6502782-43ac-476a-a486-4e084f754435), [Remote](https://mobbin.com/screens/8dceed64-1b82-4fd8-a9ee-ef3bc9f75318), [Twenty](https://mobbin.com/screens/de2c33e7-9982-4424-973a-c7beccf0c87d), [Zoho](https://mobbin.com/screens/d8374e82-baf0-4c3d-b19b-f11b0abe8a77)). Zoho also shows two equal primaries.

### 2.7 Command palettes, search and keyboard-first navigation

**Rules**
- **Anatomy:**
  - About 600-730 px wide, opening 5-20% from the top, with a dimmed and lightly blurred backdrop.
  - An input with a search icon and a verb-led placeholder: "Type a command or search…".
  - Muted group labels: Actions / Recent / Navigation / Settings.
  - Rows of about 34-38 px: a 16 px icon, a label, an optional muted breadcrumb ("Metrics — Observe"), and the shortcut as keycaps on the right.
  - Selection is a neutral grey fill, not the accent.
  - A footer of hints: "↑↓ to navigate · ↵ to select · esc · 14 results".
  - Examples: [Vapi](https://mobbin.com/screens/593d7acd-2e16-4365-bcd6-02ce52f48f3b), [Devin](https://mobbin.com/screens/274435b9-f420-4a7c-ab68-82514c1419f9), [Magnific](https://mobbin.com/screens/e22e26e2-f813-4f1e-beda-43c9ecf26419), [Juicebox](https://mobbin.com/screens/2af813bf-0129-45d1-81ed-069edee76e16).
- **Commands start with a verb.** "+ New Agent", "Go to Admin Settings" ([Mistral](https://mobbin.com/screens/8450c1c7-7c10-40a3-9af3-c9c234ac4b53)). Commands react to the query: "New branch on spice-crumb-website", "Start new chat with *website*", with a recency stamp ("7 hours ago") on the right ([v0](https://mobbin.com/screens/29db691c-e7fb-4ee3-9f4b-e16c4970b92a)).
- **Two-line rows (title plus description) are for products with many destinations** ([StackAI](https://mobbin.com/screens/bbcc94bb-f535-4dca-8532-56b135fce5c3), [Replit](https://mobbin.com/screens/9bfad190-392c-4ad0-ba1b-6475cd1bd0d8)).
- **Shortcuts live in menus, not on the page.**
  - Overflow menus list a shortcut on each row: "Move to ⇧P", "Rename… ⇧R", "Favorite ⌥F", "Delete ⌘⌫" ([Linear](https://mobbin.com/screens/83e65fd8-259c-4568-8fa6-5a2269ed4123)).
  - Filter inputs show their key ("F").
  - The sidebar search shows "⌘K" or "F" (Attio, [Vercel](https://mobbin.com/screens/b9d9cc23-34a1-434c-a4ed-52a2a4f49bb7), Mercury).
  - **None of the top-tier screens has a permanent shortcut footer.** [inferred: absence across all Linear, Stripe, Vercel, Attio and Mercury screens seen]
- **Global search results are grouped by object type.** Each group is a mini table with its own columns and a "View 3 results" link. The match is highlighted ([Stripe search](https://mobbin.com/screens/3a15e105-2b7d-4857-9fb6-478731427ebb)).

### 2.8 Notifications, approvals, and review-and-approve flows

**Rules**
- **The notification sentence:** the actor in bold, a verb, the object in bold, then a second line with the context and a relative time. "**Jane D** assigned you **Enter standup information** / Daily Standup · 6 min ago" ([Qatalog](https://mobbin.com/screens/fa31cac2-0773-4bc7-9d06-b79e16361dfc)). A quoted snippet follows for mentions ([Slite](https://mobbin.com/screens/8c928b01-d319-4b3b-91d4-6905cc0f0fca)).
- **Notifications are triaged by need, not by type.**
  - "Where you're needed / Nice to see" (Slite).
  - "Primary (1 unread) / Other (14 unread) / Later / Cleared", with per-row Clear on hover ([ClickUp](https://mobbin.com/screens/f1374e47-4168-46b0-baab-445916244ac6)).
  - "All / Mentions / Requests" (Qatalog).
  - Every inbox has "Mark all as read" and "Unread only" ([fal](https://mobbin.com/screens/d7f3f613-38ca-49f3-a382-e51c1f1d435c)). Security notices name the device, place and time, then the action ([Deel](https://mobbin.com/screens/9c9ca12e-bf5c-4c93-8630-508e19ded346)).
- **The approval queue:**
  - Tabs carry counts: "Draft 1 / Approve 2 / Ready for payment 3 / Paid 2".
  - Status shows the approval count so far: "0/1 Approved".
  - Each row has small inline ✓ and × icon buttons for fast decisions ([Acctual](https://mobbin.com/screens/4b992650-0ce5-4fc7-9efb-8407b7ac70ac), [Miro flow](https://mobbin.com/flows/e8153f2d-14c3-4428-8dc4-a0614000d440)).
  - The queue can be grouped by state with one quick action per group: Approve, Pay ([Xero](https://mobbin.com/screens/e4a6f6e1-5668-4e73-98ae-2ab3bb4f7274)).
  - Bulk actions carry the count: "Approve all your pending (71)" ([Deel](https://mobbin.com/screens/ebede796-0ca0-408a-bf05-630420732e1f)).
- **The review drawer:**
  - The list stays visible.
  - The drawer shows the amount large (cents smaller), a status badge and a vertical mini timeline ("Submitted Oct 28th at 6:11pm by …", then "Pending Review").
  - Approve in the accent, Decline in a red tint, and More.
  - Then the coding fields (GL code), the notes and the attachments ([Mercury](https://mobbin.com/screens/acd32944-7f4b-445f-a510-5a7750b11a19)).
  - Airwallex puts comments and an attachment drop zone in the drawer, and a sticky footer with "Reject ▾" and the next-step primary ([Airwallex flow](https://mobbin.com/flows/9afbce42-5ab9-4c7a-a574-2b6b83cde1fd)).
- **Show the consequence before the decision.** Remote shows a "Balance summary" ledger with "Remaining after request −4 days 1 hour" in red before you approve ([Remote flow](https://mobbin.com/flows/6df75953-9bc6-487b-92f1-6925aa40dd79)). Vercel's rollback shows the from and to deployments side by side, with "Current" and "Previous" chips, and asks for a reason ([Vercel](https://mobbin.com/screens/c96aec5a-e11c-474f-a377-d0aea68f85b9)).
- **After the decision, say what happens next and allow a reversal.**
  - "Spend request approved – The request will now be forwarded to the finance admin for card creation." (Airwallex).
  - "Added to block list. | Undo" ([Stripe](https://mobbin.com/screens/2cf3b950-fa12-475b-a34d-202923af949f)).
  - An approved timesheet offers "Reopen" ([ClickUp flow](https://mobbin.com/flows/19a9f545-daa2-4792-b300-6c5ecd048c90)).

**Average looks like:**
- Loud green and red pill buttons plus a yellow warning icon on every line ([Expensify](https://mobbin.com/screens/3eeed405-32d1-4bc4-bb42-04d44b5286a5)).
- Explainer cards with emoji inside the inbox ([Wrike](https://mobbin.com/screens/a2b51485-af81-4c80-8f06-b357e0fe5bda)).
- Gamified notifications ("Karma unlocked!") ([Todoist](https://mobbin.com/screens/c6a5fe74-6389-4d7e-8e85-980cb1010b9b)).

---

## 3. Slop and premium in B2B product UI

| Area | Slop or average (what AI-built and mid-tier B2B screens do) | Premium (what the top tier does) | How to check it |
|---|---|---|---|
| Accent | Several saturated hues compete. A gradient primary button. Accent on headings and icons | One accent, only on the primary action, selection, links, checkboxes and focus | Count chromatic hues outside status. Allow 1 |
| Status | A filled uppercase pill on every row, in 5+ hues | A dot or glyph plus a word, or a tinted badge about 18 px high with icon plus word. Normal states are quiet | Status never uses color alone. The normal state has no fill |
| Exceptions | The same warning repeated on every row ("No manager" in red) | Only real exceptions get color. Exceptions are counted in a tab or tile ("Failed 3") | Fewer than about 20% of visible rows carry a warning color [inferred] |
| Type | 16 px body, bold everywhere, 4+ weights, a big display H1 | 13-14 px body, 12 px meta, 400/500/600, page title about 20-28 px | Weights per screen ≤3. Body 13-14. No size above about 32 px except KPI figures |
| Numbers | Left-aligned, proportional digits, "$1001", no currency | Right-aligned, tabular, "$1,001.00 USD", cents muted, "—" for empty | `font-variant-numeric: tabular-nums` and `text-align: right` on numeric cells |
| Data | "John Doe" ×5, "Item 1", round numbers, no IDs, no time zones | Varied names and emails, mono IDs, odd amounts with cents, "Oct 28 at 9:21AM UTC", counts | No two rows identical. Amounts not all round. At least one ID column where the domain has IDs |
| Surfaces | Cards inside cards, every block shadowed, thick borders | Hairline borders and one tonal step. Shadows only on floating layers | No box-shadow on static in-flow elements |
| Corners | Pill buttons and 16 px cards in a dense tool, or brutal 0 px everywhere | About 6 px controls, 8 px panels, 10-12 px overlays, 4 px badges | At most 4 radius values per screen [inferred] |
| Charts | Rainbow series, pies, gradient fills, rotated axis titles, gridlines both ways, smoothed curves with dots | A 1-1.5 px line in the accent or grey, endpoint labels, comparison dashed, incomplete dotted, "Updated hh:mm" | Series colors ≤2 unless the series are categories. No gradient fill except one pale single-hue area |
| Empty states | A 3D illustration, a marketing headline, two equal CTAs | An icon tile or nothing, "No X yet", one sentence, one action, table headers kept | ≤1 primary. No raster illustration in the content area |
| Onboarding | Gradient waves, mascots, confetti, video modals, chip walls | One column, one sentence, skip always available, first value inside the flow | No full-bleed gradient in the product. A skip on every optional step |
| Settings | Illustrated upsell cards and promo banners | Title, consequence line and control per row. "Available on Enterprise" stated inline | Every toggle row has a description line |
| Destructive actions | "Are you sure?" | "Remove 3 records from list. Removing records will also delete their list attribute data." Then Undo or Reopen | The confirm names the count or object and the consequence |
| Copy | Emoji, exclamation marks, "Welcome back, superstar! 🎉", gamification | Plain and specific, with numbers and dates | No emoji in UI chrome |
| Keyboard | Keycaps on tabs and a permanent shortcut footer, as decoration | ⌘K, with shortcuts listed in menus and tooltips | No always-visible shortcut legend |
| Density | Everything at once: timeline, board, shortcuts and stats on one screen | One job per screen. Detail opens in drawers. Counts tell you what's hidden | Name the screen's single job in one line |
| Materials | Glass panels, blurred blobs, glowing borders | Opaque surfaces. Blur only on the backdrop behind a modal or palette | No `backdrop-filter` except on overlay scrims |
| Icons | Mixed sets, colored emoji icons, 20-24 px | One 16 px line set, monochrome. Color only on status glyphs | One icon family. Icon size 16 in dense UI |

**A note on our own last attempt.** I compared our own `app-screens/09-project-workspace` (Quarry) with the evidence above, and saw these "demo-ware" signals [inferred judgement]:
- Keycaps inside the view tabs ("Board 1").
- A permanent shortcut footer.
- An outlined chip around every label.
- A mono date range inside a chip.
- A saturated primary with a keycap inside it.
- A board and a timeline on the same screen.

Each of those is tidy on its own. Together they read as a product showing off its features, not one being used.

---

## 4. OpenDesigner's current B2B defaults against the evidence

### 4.1 What the engine produces today for "a B2B work tool for teams, dense, used all day"

I ran `sketch --audience dense --platforms web --feel professional,minimal,technical`. The engine doesn't know the feel words "precise", "efficient" or "dense", so I used the nearest ones it knows. The run resolved to these dials: expression 0, density 80, energy 15, roundness 20, colorfulness 0, depth 30, warmth 50. The values below are from the generated `tokens.css`, which I read myself.

| Setting | OpenDesigner today | Premium B2B evidence | Gap |
|---|---|---|---|
| Body size | 14/20 | 13-14 px | Fine |
| Type scale | Ratio 1.2: 12, 14, 17, 20, 24, 29, 35 | Sizes picked by role: 12 meta, 13-14 body, about 16 section title, about 20-28 page title, about 24-32 KPI | 17 and 29 are sizes no role asked for [inferred] |
| Weights | body 400, **label 400**, heading 600 (two weights) | 400 / 500 / 600 (titles in rows and headers are medium) | Labels, column headers and row titles have no medium weight |
| Control heights | 24 / 32 / 40 (compact mode on `:root`) | Buttons and inputs about 28-32 px, filter chips about 24-28 px | Fine |
| Row height | **No token** | About 34-42 px single line, about 48 px comfortable, about 56-78 px two lines | Missing. Builders invent it |
| Tabular numerals | **Off** (`numericStyles` false unless Q-type-06 or Q-layout-03 = data) | Every numeric column | Contradicts the house standard STD-visual-details-02 ("must") |
| Control radius | **2 px** (detail 2, container 8, overlay 12) | About 6 px controls, 8 panels, 10-12 overlays | Too sharp. Expression 0 pulls roundness to 20 through the coupling `roundness = 50 + 0.5·(expression−50) − 0.2·max(0, density−50)` |
| Accent | **Grey #757575** (no brand color given), primary near-black #242424, focus ring grey #757575 | One chromatic accent, or a black primary plus a chromatic selection, link and focus color (Vercel) | Selection, links and focus read as grey text |
| Status colors | 4 (success, warning, danger, info) | 3-5 status hues, used small | Fine. The status *form* is undefined |
| Borders | subtle #d2d2d2 (1.51:1 on white), default #c9c9c9 (1.66:1) | Row separators look lighter in previews [inferred]. Inputs need ≥3:1 | Separator and control borders should be separate tokens |
| Elevation | raised = 1 px ring + `0 1px 2px` shadow | Static cards: border only. Shadow only on floating layers | A small shadow on static cards |
| Charts | Stage 08: "categorical-6-8 for dashboards" | Accent plus greys. Categorical only for real categories | The default palette is louder than the evidence |
| Gradients | Q-color-25 default "brand-only", but the engine has no mapping and no check | None in product surfaces (one pale single-hue area fill at most) | No enforcement |

**Other things I found:**
- **Q-aud-01 "regular" promises 16 px body, but the engine gives 14.** A `regular, fun, friendly` sketch still produced 14 px body. The density band 34-66 in `levers.json` resolves `{content:16, work-tool:14}`, and nothing tells the engine that a product is a content product.
- **Q-dir-02 defaults to "comfortable" even after Q-aud-01 = dense.**
- **Q-type-08 (body size) and Q-type-12 (weights) have no default.**
- **Stage 14 contradicts the evidence.** It says "use sharp corners when density and precision are brand values (data, developer tools)" (`14-shape.md`, line 30). The top-tier data and developer tools (Linear, Vercel, Stripe, PlanetScale) all use about 6 px controls. The stage's own default line agrees with them: "6px controls, 8-12px containers", median of 23 systems.

### 4.2 Proposals (none applied; each says what to change and why)

**P1 (most important). Give "dense / work tool" a calibrated work-tool profile, and stop feel words from pushing it to extremes.** Trigger it when Q-aud-01 = dense. Q-aud-02 = work counts only when the person chose it: it is already the default for everyone, so on its own it can't be the trigger. For each specific question the person hasn't answered, default to:
- **Corners:** controls 6 / containers 8 / overlays 12. To get there, clamp the coupled roundness to at least the 6 px band (38-47) unless Q-shape-01 was answered "square".
- **Weights:** 400 / 500 / 600. Set `type.weightCount` ≥3 and make label weight 500.
- **One chromatic role** for selection, links and focus, even when the primary button is near-black (see P5).
- **Numbers:** tabular numerals on (P3).
- **Rows:** row-height tokens (P2).
- **Surfaces:** static surfaces border-only, shadows only on floating layers (P8).

*Why:* every top-tier reference shows all six together:
- Linear: [ed670cda](https://mobbin.com/screens/ed670cda-0527-4716-a1a6-0159f12c4f42)
- Stripe: [140880ca](https://mobbin.com/screens/140880ca-003b-4498-8932-c09c223ed9de)
- Vercel: [b9d9cc23](https://mobbin.com/screens/b9d9cc23-34a1-434c-a4ed-52a2a4f49bb7)
- Attio: [5bb2a956](https://mobbin.com/screens/5bb2a956-b937-497e-bd31-afc2616bb111)
- Mercury: [a930c1be](https://mobbin.com/screens/a930c1be-a15a-4dbc-a843-8a62ac0febf5)

Today, "professional, minimal" sends expression to 0, and that alone produces 2 px corners, two weights and a grey accent: a look the evidence doesn't support. The exact clamp values are [inferred]. This is a default for a choice the person hasn't made, so it should be recorded as `assumed` and stay easy to override.

**P2. Add row-height tokens and a formula.**
- `--ds-size-row-compact` ≈ 32-36
- `--ds-size-row-default` ≈ 40
- `--ds-size-row-comfortable` ≈ 48
- `--ds-size-row-two-line` ≈ 56-64

One possible formula [inferred]: row = control.md + 2 × space step 1, plus 4-8 px at lower density. Add a matching `--ds-size-badge` (≈18-20) and `--ds-size-status-dot` (≈6-8).

*Evidence:*
- Stripe ≈35, Attio ≈34, Linear ≈40-42, Snowflake ≈38, Mercury ≈48.
- Vercel ≈68 for two lines, PlanetScale ≈78 for two lines.

**P3. Turn on tabular numerals by default for dense, work and data products, and emit a numeric-cell style.**
- The style: right-aligned, `tabular-nums`, currency code in the muted color, an optional muted-cents style.
- *Why:* the house standard STD-visual-details-02 says tabular digits are a **must**, yet `numericStyles` defaults to false. Every top-tier money table aligns numbers ([Mercury](https://mobbin.com/screens/a930c1be-a15a-4dbc-a843-8a62ac0febf5), [Cofounder ledger](https://mobbin.com/screens/e9c05b3d-54e8-44db-9995-15ab9a95078a), [Stripe breakdown](https://mobbin.com/screens/2cf3b950-fa12-475b-a34d-202923af949f), [Vercel charges](https://mobbin.com/screens/b7b0e5e1-192b-4306-b2a6-88bca0d49bb6)).
- Also add a review check (P11a).

**P4. Fix the Q-aud-01 "regular" mismatch, and make Q-dir-02 follow Q-aud-01.**
- **Option A:** change the option text to "Body text 14-16 px (14 in work tools, 16 in reading apps)".
- **Option B:** use Q-aud-02 = consumer, or Q-layout-03 = reading, to select the `content:16` branch.
- Separately, when Q-aud-01 = dense, default Q-dir-02 to "compact", or skip it.
- *Why:* an engine run gives 14 px for "regular". The option promises 16.

**P5. Never ship a grey selection, link and focus role.** When there's no brand color and colorfulness is below about 10, ask one short question: "Pick one color for actions, selection and focus". Recommend one of two options:
- a near-black primary plus one blue-violet for selection, links and focus, as Vercel's black primary with blue "Current" and check marks does ([Vercel](https://mobbin.com/screens/b9d9cc23-34a1-434c-a4ed-52a2a4f49bb7))
- or one chromatic accent

Record the answer as `assumed` until confirmed. Don't invent a brand hue (guardrails).

*Evidence:* every top-tier product has a chromatic selection or focus color (Linear, Stripe, Attio, Mercury, Notion). [inferred: that grey selection hurts scannability]

**P6. Add a "status style" question (zoom 2), and status tokens.**
- Ask: "How should status show in lists?"
- Options:
  - Dot or glyph plus word, like Linear and Vercel (recommended for dense work tools).
  - Tinted badge with icon plus word, like Stripe and Mercury (recommended for money and records).
  - Filled pill (shown as a cost: it's loud and hard to scan).
- Emit `--ds-status-dot`, and tinted badge background and foreground tokens per status.
- A check: status never uses color alone.
- *Evidence:* sections 2.1 and 2.8, plus the average examples (ClickUp, Employment Hero).

**P7. Change the dashboard chart default from "categorical-6-8" to accent plus neutrals,** and emit chart tokens:
- line 1.5 px, hairline grid, axis label 11-12 px muted
- comparison series grey and dashed
- incomplete period dotted or hatched
- forecast grey

Categorical palettes only when the series are real categories. Change `08-color-system.md` line 174 and the chart stage. *Evidence:* section 2.2 (Stripe, Vercel, Amplitude, Neon, Google Analytics).

**P8. Split borders and elevation for dense tools.**
- `border-separator`: about steps 3-4 of the neutral ramp (≈1.2-1.3:1), for row and section hairlines only.
- `border-control`: ≥3:1, for inputs and interactive edges. Today's input border (neutral-8, #868686) already is.
- `elevation-raised`: border only, no shadow, when density is above about 66. Shadows remain for floating layers.

*Evidence:*
- Stripe widgets have no chrome until edit mode ([Stripe](https://mobbin.com/screens/673e89af-fe9e-4ab9-ac27-435dedf21888)).
- Linear and Mercury cards use hairlines.
- Stage 15 already says "avoid shadows on static in-page cards".

Hex steps [inferred].

**P9. Use a role-anchored type scale for work tools,** instead of a pure ratio: 12 (label and meta), 13 or 14 (body), 16 (section title), 20 (page title), 24 (headline), 32 (KPI figure). *Evidence:* the measured page titles, section titles and KPI figures in sections 2.2-2.5. The exact steps are [inferred]. Note the BRIEF's "no two sizes within 10%" rule: pick 13 *or* 14 for body, not both.

**P10. Add the missing feel words and correct the stage 14 corner advice.**
- Add these feel words: precise, efficient, dense, quiet, trustworthy. Map them to expression about 20-30 (not 0), energy about 15-25, colorfulness about 15-25 (one accent), depth about 15-25. The numbers are [inferred].
- Reword `14-shape.md` line 30: "sharp 0-2 px is a deliberate brand statement; top-tier data and developer tools use 4-6 px controls". Cite Linear, Vercel, Stripe and PlanetScale.

**P11. New checks for opendesigner-review and preflight.** Items (a) to (f) are measurable from the DOM and computed styles. Items (g) to (j) are copy heuristics that warn rather than fail.
- **(a) Numbers:** numeric table cells have `tabular-nums` and are right-aligned (the identity column is exempt).
- **(b) Weights:** at most 3 distinct font weights per screen.
- **(c) Hues:** at most 1 chromatic hue outside the status tokens.
- **(d) Gradients and blur:** no `linear-gradient` or `radial-gradient` backgrounds and no `backdrop-filter` on in-flow product surfaces. Allowed: overlay scrims, and one single-hue chart area at ≤15% opacity.
- **(e) Shadows:** box-shadow only on fixed, absolute or popover layers.
- **(f) Rows:** row heights match a row token.
- **(g) Emoji:** no emoji in UI chrome (nav, buttons, headings, badges).
- **(h) Lists:** every list or table shows a count. Every empty state has a title, one sentence and ≤1 primary action.
- **(i) Confirms:** destructive confirm dialogs name a count or object and a consequence.
- **(j) Audit:** audit and activity timestamps include a time zone, or the page states one.

Q-color-25's default ("brand-only") gets real enforcement through (d).

**P12. Add a "B2B product UI" reference for builders,** next to `making.md`. It would hold:
- the rules of section 2, cut down to one checklist per screen type
- the "slop and premium" table
- a data-realism rule: names, emails, odd amounts with cents, mono IDs, time zones, varied states. It extends DC-L19-35, which `making.md` section 6 already cites.
- a "one job per screen" rule: shortcut legends and feature showcases belong in docs and marketing, not in the product screen

[inferred that a separate file is better than growing `making.md`]

---

## 5. Six B2B product screens worth rebuilding for the showcase

All brands are invented. Check that each name is free before publishing. Each piece is a different domain and a different screen type, with a different accent family. None of the accents is a reference's exact brand hue. All six would use `--audience dense` and the P1 profile, set by hand until the engine has it, and recorded as a process finding.

### 5.1 Quoin: payments table for a mid-market platform's finance operations team
- **Screen:** "Payments". Status count tiles, filter chips with values, a dense table (amount, status, method, customer, date, ID), the Edit columns popover open, three rows selected with the bulk bar.
- **Users:** payments ops and support agents who live in it all day.
- **References:**
  - [Stripe transactions + edit columns](https://mobbin.com/screens/140880ca-003b-4498-8932-c09c223ed9de): tiles, chips, column control.
  - [Mercury transactions](https://mobbin.com/screens/a930c1be-a15a-4dbc-a843-8a62ac0febf5): amount formatting, summary strip, failed state.
  - [Attio contacts with bulk bar](https://mobbin.com/screens/5bb2a956-b937-497e-bd31-afc2616bb111): selection tint and floating bulk actions.
- **What makes ours premium:**
  - Rows ≈36 px. Amounts right-aligned and tabular, with the currency code muted.
  - Mono payment IDs.
  - Exactly one accent (deep teal) on the primary, the selection and the filter values.
  - Status as tinted icon badges.
  - The ✗ "Failed 3" tile is the only red on screen.
  - 40 rows of varied, realistic data with three currencies and time zones.
  - The empty-filter state built as a second frame.

### 5.2 Fennick: bill approvals for an accounts-payable team
- **Screen:** "Bills". Tabs with counts (Draft / To approve / Scheduled / Paid), a queue with "1/2 approved" approval counts and inline ✓/×, and the right drawer open on one bill. The drawer holds the amount, a policy line ("Over $5,000: needs CFO"), an approval timeline, the GL code, the invoice PDF row and comments, with Approve and Reject ▾ in a sticky footer.
- **Users:** controllers and department approvers.
- **References:**
  - [Mercury reimbursement drawer](https://mobbin.com/screens/acd32944-7f4b-445f-a510-5a7750b11a19)
  - [Acctual bills queue](https://mobbin.com/screens/4b992650-0ce5-4fc7-9efb-8407b7ac70ac)
  - [Airwallex approval flow](https://mobbin.com/flows/9afbce42-5ab9-4c7a-a574-2b6b83cde1fd)
- **What makes ours premium:**
  - The consequence before the decision ("Paying this bill leaves $41,208.17 in Operating ••4410").
  - A toast that names the next step, with Undo.
  - ⌘↵ / ⌘⌫ shortcuts listed in the drawer's button tooltips, not in a footer.
  - Forest-green accent. Approvals in plain words.

### 5.3 Corvane: company record in a CRM for B2B sales teams
- **Screen:** a company record:
  - Header with logo tile, name, owner and last interaction chips, and "12 of 214 in Enterprise pipeline" navigation.
  - Tabs with counts.
  - The activity timeline, with one event expanded into attribute diffs.
  - The right details panel with inline-editable empty values.
  - A ⌘K palette variant frame.
- **Users:** account executives and RevOps.
- **References:**
  - [Attio record with diffs](https://mobbin.com/screens/d76ba56f-98c3-463f-9e1d-bbe4831ee47a)
  - [Linear issue properties panel](https://mobbin.com/screens/d0f8ebba-34b7-469c-a708-1069e55a3e02)
  - [Stripe customer page sections](https://mobbin.com/screens/1a4aa88b-e0be-49b2-a87f-1264e0b5e786)
- **What makes ours premium:**
  - The timeline reads as a record of changes, not an activity feed.
  - Deal value and close date as diffs ("$48,000 → $62,500").
  - The empty "Set …" placeholders.
  - A cobalt accent, used only on links and selection.
  - Invented companies spread across industries.

### 5.4 Sounding: service overview in an API observability tool
- **Screen:**
  - Environment and range controls ("Production · Last 24 hours · compared to previous day").
  - A KPI text row (requests, p50, p95 in mono, error rate).
  - Four chart cards with endpoint-only labels, the comparison dashed, the last hour dotted, and deploy markers.
  - An endpoints table with sparklines below.
- **Users:** on-call engineers and SREs.
- **References:**
  - [Vercel observability](https://mobbin.com/screens/38a44719-a4b0-482b-bb40-283eec56ebd4)
  - [Stripe Today and overview](https://mobbin.com/screens/a31f7d76-ade4-4cae-a816-a4c9b33814c3)
  - [Neon monitoring](https://mobbin.com/screens/c5ee5c89-e7ad-43fc-828a-46315320e455)
- **What makes ours premium:**
  - Near-black primary with a single amber for the one alerting series.
  - Hatched "no data" gaps.
  - "Updated 14:02 UTC" freshness stamps.
  - A sampling footnote.
  - No donut, no gradient. One honest empty card.

### 5.5 Kilnworks: usage and billing for a cloud compute platform
- **Screen:**
  - Plan line ("Team · $480/month · renews Nov 1").
  - Spend this period against budget (actual in the accent, forecast grey, budget dashed).
  - Usage by product, grouped by family, with sparklines and right-aligned charges.
  - Seat and credit meters with reset dates.
  - The billing receipt ledger.
  - Invoices table.
- **Users:** engineering leads and finance admins.
- **References:**
  - [Vercel usage](https://mobbin.com/screens/b7b0e5e1-192b-4306-b2a6-88bca0d49bb6)
  - [OpenAI usage and budget](https://mobbin.com/screens/2bf4f941-a9a7-4308-aa0c-864135823830)
  - [Cofounder billing receipt](https://mobbin.com/screens/e9c05b3d-54e8-44db-9995-15ab9a95078a)
- **What makes ours premium:**
  - A burnt-orange accent, used only on the primary action and the "over budget" forecast crossing.
  - Every figure signed, aligned and in tabular digits.
  - Overage rates stated in words.
  - "Cancel plan" a quiet secondary button.

### 5.6 Ferrule: security and access settings for a data platform
- **Screen:** Settings, then Security:
  - A grouped settings nav.
  - Authentication method rows, each with a consequence line and a toggle.
  - A SAML card with copyable SP values in mono and the prerequisite notice "Verify a domain first".
  - SCIM "Available on Enterprise" stated inline.
  - Session length.
  - A danger zone.
  - A second frame shows the audit log tab: actor, action sentence plus event code, IP plus country, ISO time with a UTC switch, and one row expanded.
- **Users:** IT admins and security engineers at customer companies (the buyer's view of "enterprise-ready").
- **References:**
  - [Linear security](https://mobbin.com/screens/34f99905-3147-4e31-9d52-c091158c4ba3)
  - [Langdock SAML](https://mobbin.com/screens/2f35d1d3-903e-40ab-84d6-09375a5e5535)
  - [PlanetScale audit log](https://mobbin.com/screens/d7448333-6400-49dd-b11f-e48e4e229200)
- **What makes ours premium:**
  - A plum accent, used only on toggles and focus.
  - Each policy states its exact effect and who it applies to.
  - Plan gating shown as a quiet inline label, not a banner.
  - The audit data is realistic (bots, API keys, people).

---

## Appendix: coverage and limits

- **Searches.** Screens:
  - Linear list, Stripe payments, Ramp-named (no Ramp results), Vercel deployments, Attio table, admin users table.
  - Stripe dashboard, observability dashboards, product analytics.
  - Attio record, Linear issue detail, Stripe customer.
  - Members, SSO and security, audit log, roles and permissions.
  - Billing, usage, plan modal.
  - Empty states, command palette, Linear command menu.
  - Approvals, notifications.
  - Linear dark, Ramp spend home (no Ramp results), Mercury home, Notion members.

  Flows: B2B onboarding, review and approve.
- **What Mobbin did not have:** Ramp, Datadog, and a designed Retool admin app. The Retool result was a default builder app. The substitutes are named in Method.
- **What I could not measure:** exact hex values and exact type sizes. The previews are about 768 px wide and compressed. Rebuilds should check type and spacing against the live products, or against higher-resolution references viewed on Mobbin. Never save those images into the repo.
- **What I verified myself:**
  - The engine values in section 4.1 (from the generated `tokens.css`).
  - The Q-aud-01, Q-dir-02, Q-type-06, Q-type-08, Q-type-12, Q-color-04, Q-color-05, Q-color-25, Q-shape-01 and Q-depth-01 texts in `questions.json`.
  - The stage lines quoted from `02-audience-and-commitments.md`, `14-shape.md`, `15-depth-borders-and-materials.md` and `08-color-system.md`.
  - STD-visual-details-02 in `standards/visual-details.md`.
  - The answer mapping `Q-aud-01: dense → dials.density 80` at `engine.py` line 3437.
