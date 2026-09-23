# Lane L14 prompt: UI practices by device class

Paste this into a Claude Code session opened in /Users/Kunal/Desktop/Design-System, after claiming L14 in `_coordination/BOARD.md` (see `_coordination/PROTOCOL.md`).

---

You are research lane L14 (UI PRACTICES BY DEVICE CLASS: WHAT IS COMMON ACROSS DEVICES AND WHAT CHANGES) on a project in /Users/Kunal/Desktop/Design-System. Kunal is building a "design-system builder": a product that makes creating design systems, designs and visuals a beautiful, visual process for engineers and technical people, the way Figma makes it for designers. Users will target mobile, web, or any other device, so the builder must know which practices hold everywhere and which change per device.

First read `_coordination/SCHEMA.md`, `_coordination/PROTOCOL.md` and `_coordination/BOARD.md`. Claim L14 in BOARD.md if it is still `open`, and message the session "Design system research and builder" that you claimed it. Follow SCHEMA exactly: source tiers, logging every source in `traces/L14-trace.md`, Decision Card format, [S-id] or [inferred] tags. Read `sources/COMMUNITY-SIGNAL.md` before finalizing. Lane L10 covers OS platforms (iOS, Android, web, Windows/macOS) and cross-platform frameworks; read `research/L10-platforms.md` and do not duplicate it. Your focus is device classes, input modalities and usage contexts.

Output: `research/L14-device-practices.md`.

Cover each device class with real values from official guidelines (Apple HIG per platform, Material/Android per form factor, Microsoft, Amazon, Samsung, W3C) and research (NN/g, Steven Hoober's research on how people hold phones, Baymard):
- Phone: one-handed use and thumb reach, bottom navigation, gestures, sheets, safe areas, portrait-first, interruptions and short sessions.
- Tablet and foldables: multitasking, split views, pointer support, posture changes.
- Laptop/desktop (native and web): pointer precision, hover, right-click, keyboard shortcuts and focus, windows and resizing, information density, multi-column layouts.
- Large and ultra-wide displays; responsive max widths.
- Smartwatch (watchOS, Wear OS): glanceability, complications/tiles, crown/bezel input, font sizes and targets.
- TV (tvOS, Android/Google TV, Fire TV, Samsung Tizen): the 10-foot UI, D-pad focus navigation and focus states, overscan/safe zones, minimum text sizes, remote input.
- Automotive (CarPlay, Android Auto, Android Automotive OS): driver-distraction limits (e.g. NHTSA glance-time guidelines; verify), templates, voice-first, day/night modes.
- Spatial computing (visionOS, Android XR, Meta Horizon OS): eye and hand input, minimum target sizes (e.g. visionOS 60 pt; verify), depth, ergonomics and field of view, glass materials, comfort.
- Voice and conversational interfaces, and AI chat/agent interfaces (2024-2026 patterns; verify).
- Kiosks/POS, e-ink, and game consoles, briefly.
- Input modalities across all of these: touch, mouse, trackpad, keyboard, stylus, D-pad/remote, crown, gaze, voice, gestures; and accessibility per device (screen readers, switch access, magnification).

Then produce the two outputs the builder needs most:
1. **Invariants**: practices that hold on every device, with evidence.
2. **Device matrix**: devices as columns, dimensions as rows: viewing distance, typical screen size, primary input, minimum target size, minimum body text size, navigation model, typical density, session length and attention, motion norms, dark mode norms, focus model, key platform guidelines URL. Every cell sourced or marked [inferred].

Add Decision Cards for the decisions a designer makes per device (e.g. which devices are first-class, how the system adapts targets and type per device, one component set with device variants vs separate sets). Use WebSearch, WebFetch and Perplexity. Today is 2026-09-23; verify recent platform changes (visionOS 26, Android XR, watchOS 26, tvOS 26, CarPlay Ultra; verify each) against live sources. Write incrementally. When finished, set L14 to `done` in BOARD.md and message the orchestrator with the file path and your top 5 findings.
