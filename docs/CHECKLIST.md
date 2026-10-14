# Design system checklist

Everything a design system needs, as a list you can tick off.

**How to read it.** Part 1 applies to every design system. Then add the part for what you are making: a website (Part 2), a mobile app (Part 3), or software such as a web app, dashboard or desktop app (Part 4). Part 5 is for everything else.

**How to add to it.** Put one thing per line, in plain words, under the part it belongs to. If it is true for every product, it goes in Part 1.

**◆** marks a line that OpenDesigner does not ask about or build yet. See "About the ◆ marks" at the end.

Each part that makes a product has an **Assets to make** section: the files someone has to produce (name, logo, icons, share images, store art), with sizes where a platform sets them.

Status: second draft, 13 October 2026. Not yet wired into the skills or the engine.

---

## Part 1. Global: every design system

### Starting point
- [ ] What it is for: which products, who uses them, what is left out
- [ ] Where it runs: web, iOS, Android, desktop, other devices
- [ ] Brand inputs: logo, brand colours, fonts, personality in 3 to 5 words
- [ ] An audit of what exists today: screens, colours, type, spacing
- [ ] Hard limits: tech stack, languages, legal rules, deadlines
- [ ] 3 to 5 design principles that settle arguments

### Name
- [ ] A name that is easy to say, spell and search for ◆
- [ ] Checked that the name is free: trademark, web address, social handles, app store names ◆
- [ ] How the name is written: capitals, spacing, short form ◆
- [ ] A one-line description and a one-paragraph description ◆

### Brand assets (files to make)
- [ ] Logo in three forms: symbol with name, symbol alone, name alone (wordmark)
- [ ] Each form in full colour, one colour, and white for dark backgrounds
- [ ] Wide and stacked layouts
- [ ] A simplified symbol that still reads at favicon size
- [ ] Logo rules: smallest size, clear space around it, what not to do ◆
- [ ] Master files as SVG, plus PNG with a transparent background
- [ ] Profile picture (works in a circle and a square) and cover image for social accounts ◆
- [ ] A share image template: what shows when a link is posted ◆
- [ ] Brand font files and their licence
- [ ] One brand sheet: logo, colours and fonts on a single page
- [ ] One folder with clear file names and a note on who owns each asset

### Colour
- [ ] A brand (accent) colour and a neutral grey, each as a ramp of numbered steps
- [ ] Meaning colours: success, warning, danger, info
- [ ] Colours named by job, not by look: background, surface, text, border, accent
- [ ] State colours: hover, pressed, selected, disabled, focus
- [ ] Light mode and dark mode
- [ ] Contrast checked: 4.5:1 for text, 3:1 for large text and for the parts of controls
- [ ] Colour is never the only way meaning is shown
- [ ] Chart colours, if there are charts

### Type
- [ ] Typeface with a licence that covers the use, plus fallback fonts
- [ ] A type scale: each size with its line height and weight
- [ ] Type roles: display, heading, body, label, caption, code
- [ ] Rules for line length, alignment and cut-off text
- [ ] Number style, with equal-width digits for tables
- [ ] Other languages and scripts the product needs
- [ ] Text can be enlarged to 200% without breaking the layout

### Space and layout
- [ ] A base unit and a spacing scale
- [ ] A size scale for controls and icons
- [ ] Density: how tight or airy, and whether there is a compact mode
- [ ] Grid, maximum content width and breakpoints
- [ ] How each layout changes between screen sizes

### Shape, depth and motion
- [ ] Radius scale, and which radius each component uses
- [ ] Border widths and dividers
- [ ] Elevation levels and one shadow recipe
- [ ] Stacking order: what sits above what
- [ ] Opacity values and the dimmed layer behind overlays
- [ ] Motion: a duration scale, a small set of easings, and what animates and why
- [ ] A reduced-motion version of everything that moves

### Icons and imagery
- [ ] One icon set: source, licence, style and sizes
- [ ] Illustration style and photo direction
- [ ] Image shapes (aspect ratios), cropping, and what shows while images load
- [ ] Text on top of images stays readable

### Words
- [ ] Voice, and how the tone shifts by situation
- [ ] Rules for capitals, punctuation, dates and numbers
- [ ] Standard wording for buttons, errors, empty screens and confirmations
- [ ] A word list: what we call things
- [ ] Ready for translation, including right-to-left languages

### Components (the core set)
- [ ] Actions: button (primary, secondary, quiet, destructive), link, icon button
- [ ] Inputs: text field, text area, select, checkbox, radio, switch, slider, date picker, file upload
- [ ] Navigation: bar or header, tabs, menu, breadcrumbs, pagination
- [ ] Feedback: banner, toast, progress bar, spinner, skeleton, badge, tooltip
- [ ] Overlays: dialog, popover, drawer or sheet
- [ ] Containers: card, list, table, accordion, divider
- [ ] Media: avatar, image, icon
- [ ] For each component: its parts, sizes, variants, and when to use it or not

### States
- [ ] Every interactive part has: default, hover, pressed, focus, selected, disabled, loading, error
- [ ] Every screen has: empty, loading, error, success and first-use versions

### Patterns
- [ ] Forms: labels, help text, required fields, when errors appear, error wording
- [ ] Destructive actions: undo or confirm
- [ ] Search, filter and sort
- [ ] Sign up, sign in, reset password
- [ ] Onboarding
- [ ] Page templates for the most common screens

### Accessibility floors (locked)
- [ ] WCAG 2.2 AA contrast
- [ ] Touch and click targets at least 24 px
- [ ] A visible focus ring on everything you can reach
- [ ] Everything works with a keyboard, in a sensible order
- [ ] Every control and meaningful image has a name a screen reader can read
- [ ] The "reduce motion" setting is respected

### Tokens and files
- [ ] Three layers of tokens: raw values, roles, component-specific
- [ ] One naming rule
- [ ] One source of truth; every export is generated from it
- [ ] Modes and themes: light, dark, extra brands
- [ ] The design file library matches the code

### Docs and upkeep
- [ ] DESIGN.md: the whole system on one page
- [ ] A page per component
- [ ] A decision log with the reason for each choice
- [ ] Who owns the system and how to propose a change
- [ ] Versions, a changelog, and how old parts are retired
- [ ] Checks before shipping: token lint, contrast, a visual review
- [ ] Instructions for AI agents working in the project

---

## Part 2. Websites

Marketing sites, landing pages, blogs, docs, shops.

### Assets to make
- [ ] Favicon: `favicon.ico` at 32 px, an SVG icon (it can change for dark mode), and a 180 px `apple-touch-icon.png`
- [ ] If the site can be installed as an app: 192 px and 512 px icons, a 512 px maskable icon with extra padding, and a web manifest
- [ ] Share image: 1200 × 630 px (1.91:1)
- [ ] Share details on every page: title, type, image and address, plus a description and alt text for the image ◆
- [ ] A share image for each key page, or a template that makes them ◆
- [ ] Logo for the header and footer, as SVG
- [ ] Hero art, illustrations and photos in the agreed style

### Structure
- [ ] Header and navigation, including the mobile menu
- [ ] Footer
- [ ] Section rhythm: the space between sections and the content width
- [ ] Section kit: hero, features, logos, pricing, FAQ, call to action
- [ ] Testimonials ◆
- [ ] Reading styles for articles and docs: headings, lists, quotes, code, tables, captions
- [ ] Page templates: home, landing, product, pricing, about, blog list, blog post, contact
- [ ] Legal pages: privacy, terms ◆
- [ ] 404 and error pages

### Responsive
- [ ] Designed phone-first; no sideways scroll at 320 px wide
- [ ] Type and spacing that scale with the screen
- [ ] Images sized and cropped per screen size
- [ ] Finger-sized targets on phones (44 px)
- [ ] Nothing depends on hover alone

### Browser details
- [ ] Link styles: default, hover, visited, focus
- [ ] Browser theme colour
- [ ] Text selection colour ◆
- [ ] Scrollbar style ◆
- [ ] Print styles ◆

### Speed
- [ ] Font loading that does not make the page jump
- [ ] Limits on image and video weight; load below-the-fold media late
- [ ] Scroll effects have a purpose and switch off for reduced motion

### Trust and conversion
- [ ] Cookie and consent banner
- [ ] Contact and lead forms
- [ ] Newsletter sign-up ◆
- [ ] Search basics: one main heading per page, headings in order, page titles, descriptions, image alt text ◆
- [ ] Announcement bar

---

## Part 3. Mobile apps

iOS and Android phones, tablets and foldables.

### Assets to make
- [ ] App name: 30 characters at most on both stores
- [ ] Short pitch: a 30-character subtitle (App Store) and an 80-character short description (Google Play) ◆
- [ ] iOS icon: 1024 × 1024 px square with no rounded corners (the system rounds them), built as a background layer plus foreground layers
- [ ] iOS icon versions: default, dark, clear and tinted (the system makes any you skip)
- [ ] Android icon: two layers of 108 × 108 dp (foreground and background), with the logo inside the middle 66 dp
- [ ] Android single-colour icon layer, so the icon can take the user's theme colour
- [ ] Avoid text and photos in the icon
- [ ] Google Play icon: 512 × 512 px PNG
- [ ] Google Play feature graphic: 1024 × 500 px ◆
- [ ] Screenshots: at least 1 and up to 10 per device size on the App Store; at least 2 in total and up to 8 per device type on Google Play ◆
- [ ] Preview video (optional) ◆
- [ ] Notification icon ◆
- [ ] Launch screen
- [ ] Privacy policy page (the App Store requires the link) ◆

### Platform fit
- [ ] Decide: look like the platform, look like the brand, or a mix
- [ ] Each platform's units and text-size setting are followed (pt and Dynamic Type on iOS, dp and sp on Android)
- [ ] Oldest OS version supported, and which devices: phone, tablet, foldable
- [ ] Android layouts adapt at 600 dp and wider

### Layout
- [ ] Safe areas: notch, status bar, home indicator, rounded corners
- [ ] Portrait and landscape
- [ ] Main actions within thumb reach
- [ ] The on-screen keyboard never covers the field or the main button ◆

### Navigation
- [ ] Tab bar or bottom navigation, and the top bar
- [ ] Back: the iOS swipe and the Android system back both work
- [ ] Sheets versus full-screen screens: when each is used
- [ ] Links from outside open the right screen ◆

### Touch
- [ ] Targets: 44 pt on iOS, 48 dp on Android
- [ ] Gestures (swipe, long press, pull to refresh), each with a visible alternative
- [ ] Pressed states in place of hover
- [ ] Haptics: which vibration means what
- [ ] Sounds, if any

### System pieces
- [ ] Push notifications: look and wording
- [ ] Permission requests: explain before asking
- [ ] Widgets and lock-screen activities, if used
- [ ] System settings respected: dark mode, text size, reduce motion, bold text, high contrast

### App states
- [ ] Offline and weak connection ◆
- [ ] Sign in with face or fingerprint ◆
- [ ] Paywall and in-app purchase screens
- [ ] "Update needed" and "what's new" screens

---

## Part 4. Software

Web apps, dashboards, admin tools and desktop apps.

### Assets to make
- [ ] Product mark for the sidebar, sign-in screen and loading screen
- [ ] Web apps: the favicon set from Part 2
- [ ] Mac app icon: 1024 × 1024 px, layered, same rules as the iOS icon
- [ ] Windows app icon: at least 16, 24, 32, 48 and 256 px, on a transparent background
- [ ] Windows icon versions for light and dark themes
- [ ] The smallest icon redrawn by hand, not shrunk (title bar, tray, menus)
- [ ] Tray or menu bar icon in a single colour ◆
- [ ] File icons for the documents the app owns ◆
- [ ] Installer and splash art ◆
- [ ] Store listing art, if sold through the Mac App Store or Microsoft Store ◆
- [ ] Logo and layout for the emails the product sends (welcome, receipt, reset password)

### App shell
- [ ] Regions: sidebar, top bar, content, side panel
- [ ] Panels that collapse and resize
- [ ] Layouts change by window size, from small to very wide
- [ ] Density modes: comfortable and compact
- [ ] Account or workspace switcher

### Data
- [ ] Tables: sort, filter, resize columns, select rows, sticky header
- [ ] Bulk actions on selected rows ◆
- [ ] Pages versus endless scroll
- [ ] Charts: colours, axes, legends, tooltips, and a non-visual alternative
- [ ] Dashboard cards and number formats
- [ ] Saved filters and views

### Getting work done
- [ ] Keyboard shortcuts and a list of them
- [ ] Command palette
- [ ] Right-click menus ◆
- [ ] Drag and drop, with a keyboard alternative
- [ ] Undo, autosave and an unsaved-changes warning
- [ ] Multi-step flows, long forms and editing in place
- [ ] Text or code editor, if needed
- [ ] Search across the whole product

### System feedback
- [ ] Toast, banner or dialog: which one when
- [ ] Notification centre or inbox ◆
- [ ] Long tasks: progress, running in the background, cancel
- [ ] Roles: what someone sees when they are not allowed
- [ ] Settings and preferences layout

### Desktop apps only
- [ ] Window frame and title bar follow the operating system
- [ ] Menu bar
- [ ] System tray or dock ◆
- [ ] More than one window ◆
- [ ] Shortcuts, dialogs and file pickers follow each OS (Cmd on Mac, Ctrl on Windows)
- [ ] Pointer details: hover, cursor types, tooltips

### AI features, if the product has them
- [ ] Prompt box, streaming answers, sources, retry, feedback, and a clear "made by AI" label

---

## Part 5. Other surfaces

Short for now. Add as needed.

- [ ] Email: one narrow column, fallback fonts, works with images off, safe in dark mode
- [ ] Watch, TV, car, headset: only colours, text roles and icons carry over
- [ ] Slides, social posts and video: brand colours, type, logo rules, motion style
- [ ] Docs sites: see "Reading styles" in Part 2
- [ ] Open-source project: a logo, a README header image, and a repository preview image of 1280 × 640 px under 1 MB ◆
- [ ] Social accounts: profile picture, cover image and a post template ◆

---

## About the ◆ marks

A ◆ means a keyword search of `synthesis/ontology.json`, `synthesis/questionnaire.json` and the asset hooks (`skills/opendesigner/references/hooks.json`, `hooks.md`) on 13 October 2026 found no mention of that item. It is a quick check, not a full audit: an unmarked line may still be covered only thinly. Each ◆ is a candidate for a new building block, question or asset hook.

## Where the sizes come from

Every pixel size, dp size and character limit in the "Assets to make" sections was read from the pages below on 13 October 2026. Platforms change these, so check again before shipping. Lines without a number are judgement, not a quoted rule.

| What | Source |
|---|---|
| iOS and Mac app icon: 1024 px, layers, dark, clear and tinted versions, no text or photos | [Apple Human Interface Guidelines: App icons](https://developer.apple.com/design/human-interface-guidelines/app-icons) |
| App Store name and subtitle limits, privacy policy link | [App Store Connect: App information](https://developer.apple.com/help/app-store-connect/reference/app-information/) |
| App Store screenshot count | [App Store Connect: Screenshot specifications](https://developer.apple.com/help/app-store-connect/reference/screenshot-specifications/) |
| Android adaptive icon: 108 dp layers, 66 dp safe zone, single-colour layer | [Android Developers: Adaptive icons](https://developer.android.com/develop/ui/views/launch/icon_design_adaptive) |
| Google Play icon, feature graphic, screenshot count | [Play Console Help: Preview assets](https://support.google.com/googleplay/android-developer/answer/9866151) |
| Google Play name and short description limits | [Play Console Help: Create and set up your app](https://support.google.com/googleplay/android-developer/answer/9859152) |
| Windows icon sizes, transparent background, theme versions | [Microsoft Learn: Construct your Windows app's icon](https://learn.microsoft.com/en-us/windows/apps/design/style/iconography/app-icon-construction) |
| Favicon files and sizes | [Evil Martians: How to Favicon in 2026](https://evilmartians.com/chronicles/how-to-favicon-in-2021-six-files-that-fit-most-needs) |
| Share image size and ratio | [Meta for Developers: Images in link shares](https://developers.facebook.com/docs/sharing/webmasters/images/) |
| Share details every page needs | [The Open Graph protocol](https://ogp.me/) |
| Repository preview image | [GitHub Docs: Customizing your repository's social media preview](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview) |
