# Decisions

Append-only, ADR-style (spec 7.9): one entry per decision, newest last. A later entry for the same path supersedes an earlier one; nothing is edited or deleted. set_by is chosen, confirmed_default, auto_default, assumed, delegated, reference, asset or standard.

## D-0001 · init with defaults
- set_by: auto_default · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: Start of the design system; every default traces to references/levers.json.

## D-0002 · answers.Q-aud-01 = "regular"
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: sketch: picked for them
- also set: dials.density = 50 (from Q-aud-01)

## D-0003 · context.audience = "people who use it often, as an everyday app"
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: sketch: plain words for Q-aud-01, picked for them
- previous value: ""

## D-0004 · raw.brandColor = "#2a5bd7"
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: sketch: picked for them

## D-0005 · answers.Q-plat-01 = ["ios"]
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: sketch: picked for them
- also set: raw.platforms = ["ios"] (from Q-plat-01)

## D-0006 · macros = ["playful", "bold", "friendly"]
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: sketch: picked for them (feel words: playful, bold, cheerful)
- previous value: []

## D-0007 · taste.feelWords = ["playful", "bold", "cheerful"]
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: sketch: feel words picked for them

## D-0008 · House standards v2: 339 applied
- set_by: standard · locked: yes · date: 2026-10-14 · supersedes: none · source_ref: standards.json v2
- reason: OpenDesigner's house standards (sources marked non-negotiable) are applied without asking and locked. Change one only when the person asks: engine.py standard override <id> --why "<their words>".
- <details><summary>339 standards</summary> STD-when-to-animate-01, STD-when-to-animate-03, STD-when-to-animate-04, STD-when-to-animate-05, STD-when-to-animate-06, STD-when-to-animate-07, STD-when-to-animate-08, STD-when-to-animate-09, STD-when-to-animate-10, STD-when-to-animate-11, STD-when-to-animate-13, STD-when-to-animate-14, STD-when-to-animate-15, STD-when-to-animate-16, STD-when-to-animate-17, STD-when-to-animate-20, STD-when-to-animate-22, STD-easing-duration-01, STD-easing-duration-02, STD-easing-duration-03, STD-easing-duration-06, STD-easing-duration-07, STD-easing-duration-09, STD-easing-duration-10, STD-easing-duration-11, STD-easing-duration-12, STD-easing-duration-13, STD-easing-duration-15, STD-easing-duration-17, STD-enter-exit-origin-01, STD-enter-exit-origin-02, STD-enter-exit-origin-06, STD-enter-exit-origin-13, STD-enter-exit-origin-16, STD-enter-exit-origin-24, STD-enter-exit-origin-25, STD-enter-exit-origin-31, STD-enter-exit-origin-33, STD-enter-exit-origin-37, STD-enter-exit-origin-39, STD-springs-gestures-01, STD-springs-gestures-02, STD-springs-gestures-04, STD-springs-gestures-05, STD-springs-gestures-06, STD-springs-gestures-07, STD-springs-gestures-08, STD-springs-gestures-09, STD-springs-gestures-11, STD-springs-gestures-12, STD-springs-gestures-13, STD-springs-gestures-14, STD-springs-gestures-16, STD-springs-gestures-17, STD-springs-gestures-19, STD-springs-gestures-20, STD-springs-gestures-21, STD-springs-gestures-25, STD-springs-gestures-26, STD-springs-gestures-30, STD-springs-gestures-34, STD-springs-gestures-39, STD-springs-gestures-41, STD-springs-gestures-42, STD-springs-gestures-59, STD-springs-gestures-60, STD-springs-gestures-61, STD-springs-gestures-63, STD-performance-properties-01, STD-performance-properties-02, STD-performance-properties-10, STD-performance-properties-13, STD-performance-properties-16, STD-performance-properties-18, STD-performance-properties-19, STD-performance-properties-20, STD-performance-properties-25, STD-accessibility-motion-01, STD-accessibility-motion-02, STD-accessibility-motion-06, STD-accessibility-motion-07, STD-accessibility-motion-08, STD-accessibility-motion-09, STD-accessibility-motion-10, STD-accessibility-motion-13, STD-accessibility-motion-20, STD-accessibility-motion-24, STD-components-toasts-drawers-08, STD-components-toasts-drawers-11, STD-components-toasts-drawers-15, STD-components-toasts-drawers-18, STD-components-toasts-drawers-37, STD-components-toasts-drawers-40, STD-components-toasts-drawers-44, STD-components-toasts-drawers-48, STD-components-toasts-drawers-60, STD-components-toasts-drawers-72, STD-mobile-touch-05, STD-mobile-touch-07, STD-mobile-touch-08, STD-mobile-touch-09, STD-mobile-touch-16, STD-mobile-touch-24, STD-mobile-touch-28, STD-mobile-touch-30, STD-mobile-touch-33, STD-mobile-touch-34, STD-mobile-touch-35, STD-mobile-touch-36, STD-mobile-touch-37, STD-mobile-touch-38, STD-mobile-touch-39, STD-mobile-touch-41, STD-mobile-touch-42, STD-mobile-touch-44, STD-mobile-touch-48, STD-mobile-touch-51, STD-mobile-touch-60, STD-mobile-touch-61, STD-mobile-touch-62, STD-visual-details-02, STD-visual-details-03, STD-visual-details-04, STD-visual-details-05, STD-visual-details-06, STD-visual-details-07, STD-visual-details-08, STD-visual-details-09, STD-visual-details-11, STD-visual-details-13, STD-visual-details-14, STD-visual-details-17, STD-visual-details-18, STD-visual-details-19, STD-visual-details-20, STD-visual-details-21, STD-visual-details-24, STD-visual-details-25, STD-visual-details-26, STD-visual-details-27, STD-visual-details-28, STD-visual-details-29, STD-visual-details-30, STD-visual-details-31, STD-visual-details-32, STD-visual-details-33, STD-visual-details-34, STD-visual-details-35, STD-visual-details-36, STD-visual-details-37, STD-visual-details-38, STD-visual-details-39, STD-visual-details-40, STD-visual-details-41, STD-visual-details-42, STD-visual-details-43, STD-visual-details-44, STD-visual-details-45, STD-visual-details-46, STD-visual-details-47, STD-visual-details-48, STD-visual-details-49, STD-visual-details-50, STD-visual-details-51, STD-visual-details-64, STD-process-review-taste-01, STD-process-review-taste-02, STD-process-review-taste-03, STD-process-review-taste-04, STD-process-review-taste-05, STD-process-review-taste-06, STD-process-review-taste-07, STD-process-review-taste-08, STD-process-review-taste-09, STD-process-review-taste-10, STD-process-review-taste-11, STD-process-review-taste-12, STD-process-review-taste-13, STD-process-review-taste-14, STD-process-review-taste-15, STD-process-review-taste-16, STD-process-review-taste-17, STD-process-review-taste-18, STD-process-review-taste-19, STD-process-review-taste-20, STD-process-review-taste-21, STD-process-review-taste-22, STD-process-review-taste-23, STD-process-review-taste-24, STD-process-review-taste-25, STD-process-review-taste-26, STD-process-review-taste-27, STD-process-review-taste-28, STD-process-review-taste-29, STD-process-review-taste-30, STD-process-review-taste-31, STD-process-review-taste-32, STD-process-review-taste-33, STD-process-review-taste-34, STD-process-review-taste-35, STD-process-review-taste-36, STD-process-review-taste-37, STD-process-review-taste-38, STD-process-review-taste-39, STD-process-review-taste-40, STD-process-review-taste-42, STD-process-review-taste-43, STD-process-review-taste-44, STD-process-review-taste-47, STD-process-review-taste-48, STD-process-review-taste-49, STD-process-review-taste-50, STD-process-review-taste-51, STD-process-review-taste-52, STD-process-review-taste-53, STD-process-review-taste-54, STD-process-review-taste-55, STD-process-review-taste-56, STD-process-review-taste-57, STD-process-review-taste-58, STD-process-review-taste-59, STD-process-review-taste-60, STD-process-review-taste-63, STD-process-review-taste-64, STD-process-review-taste-66, STD-process-review-taste-67, STD-swift-01, STD-swift-02, STD-swift-03, STD-swift-04, STD-swift-05, STD-swift-06, STD-swift-07, STD-swift-08, STD-swift-09, STD-swift-10, STD-swift-11, STD-swift-12, STD-swift-13, STD-swift-14, STD-swift-15, STD-swift-16, STD-swift-17, STD-swift-18, STD-swift-19, STD-swift-20, STD-swift-21, STD-swift-22, STD-swift-23, STD-swift-24, STD-swift-25, STD-swift-26, STD-swift-27, STD-swift-28, STD-swift-29, STD-swift-30, STD-swift-31, STD-swift-32, STD-swift-33, STD-swift-34, STD-swift-35, STD-swift-36, STD-swift-37, STD-swift-38, STD-swift-39, STD-swift-40, STD-swift-41, STD-swift-42, STD-swift-43, STD-swift-44, STD-swift-45, STD-swift-46, STD-swift-47, STD-swift-48, STD-swift-49, STD-swift-50, STD-swift-51, STD-swift-52, STD-swift-53, STD-swift-54, STD-swift-55, STD-swift-56, STD-swift-57, STD-swift-58, STD-swift-59, STD-swift-60, STD-swift-61, STD-swift-62, STD-swift-63, STD-swift-64, STD-swift-65, STD-swift-66, STD-swift-67, STD-swift-68, STD-swift-69, STD-swift-70, STD-swift-71, STD-swift-72, STD-swift-73, STD-swift-74, STD-swift-75, STD-swift-76, STD-swift-77, STD-swift-78, STD-swift-79, STD-swift-80, STD-swift-81, STD-swift-82, STD-swift-83, STD-swift-84, STD-swift-85, STD-swift-86, STD-swift-87, STD-swift-88, STD-swift-89, STD-swift-90, STD-swift-91, STD-swift-92, STD-swift-93, STD-swift-94, STD-swift-95, STD-swift-96, STD-swift-97, STD-swift-98, STD-swift-99, STD-swift-100, STD-swift-101, STD-swift-102, STD-swift-103, STD-swift-104, STD-swift-105, STD-swift-106, STD-swift-107, STD-swift-108, STD-swift-109, STD-swift-110, STD-swift-111, STD-swift-112, STD-swift-113</details>
- STD-when-to-animate-01: followed; it sets no values (DESIGN.md carries it)
- STD-when-to-animate-03: followed; it sets no values (DESIGN.md carries it)
- STD-when-to-animate-04: followed; it sets no values (DESIGN.md carries it)
- STD-when-to-animate-05: motion.duration.instant = 0ms
- STD-when-to-animate-06: followed; it sets no values (DESIGN.md and review carry it)
- STD-when-to-animate-07: followed; it sets no values (DESIGN.md carries it)
- STD-when-to-animate-08: followed; it sets no values (DESIGN.md carries it)
- STD-when-to-animate-09: followed; it sets no values (DESIGN.md carries it)
- STD-when-to-animate-10: followed; it sets no values (DESIGN.md carries it)
- STD-when-to-animate-11: followed; it sets no values (DESIGN.md carries it)
- STD-when-to-animate-13: followed; it sets no values (DESIGN.md carries it)
- STD-when-to-animate-14: followed; it sets no values (DESIGN.md and review carry it)
- STD-when-to-animate-15: followed; it sets no values (DESIGN.md carries it)
- STD-when-to-animate-16: followed; it sets no values
- STD-when-to-animate-17: followed; it sets no values (DESIGN.md carries it)
- STD-when-to-animate-20: followed; it sets no values (DESIGN.md carries it)
- STD-when-to-animate-22: followed; it sets no values
- STD-easing-duration-01: motion.easing.linear = [0, 0, 1, 1]
- STD-easing-duration-01: motion.easing.hover = [0.25, 0.1, 0.25, 1]
- STD-easing-duration-02: motion.easing.enter = [0.23, 1, 0.32, 1]
- STD-easing-duration-02: motion.easing.exit = [0.23, 1, 0.32, 1]
- STD-easing-duration-02: motion.easing.standard = [0.77, 0, 0.175, 1]
- STD-easing-duration-03: followed; it sets no values (DESIGN.md and review carry it)
- STD-easing-duration-06: followed; it sets no values (DESIGN.md and review carry it)
- STD-easing-duration-07: motion.duration.micro = 100ms
- STD-easing-duration-07: motion.duration.short = 150ms
- STD-easing-duration-07: motion.duration.medium = 200ms
- STD-easing-duration-07: motion.duration.long = 250ms
- STD-easing-duration-09: followed; it sets no values (DESIGN.md carries it)
- STD-easing-duration-10: followed; it sets no values (DESIGN.md carries it)
- STD-easing-duration-11: followed; it sets no values (DESIGN.md carries it)
- STD-easing-duration-12: followed; it sets no values (DESIGN.md carries it)
- STD-easing-duration-13: followed; it sets no values (DESIGN.md carries it)
- STD-easing-duration-15: followed; it sets no values (DESIGN.md carries it)
- STD-easing-duration-17: followed; it sets no values (DESIGN.md carries it)
- STD-enter-exit-origin-01: motion.scale.enter = 0.95
- STD-enter-exit-origin-02: followed; it sets no values (DESIGN.md carries it)
- STD-enter-exit-origin-06: followed; it sets no values (DESIGN.md carries it)
- STD-enter-exit-origin-13: motion.duration.stagger = 50ms
- STD-enter-exit-origin-16: followed; it sets no values (DESIGN.md carries it)
- STD-enter-exit-origin-24: followed; it sets no values (DESIGN.md and review carry it)
- STD-enter-exit-origin-25: followed; it sets no values (DESIGN.md and review carry it)
- STD-enter-exit-origin-31: followed; it sets no values (DESIGN.md carries it)
- STD-enter-exit-origin-33: followed; it sets no values (DESIGN.md and review carry it)
- STD-enter-exit-origin-37: followed; it sets no values
- STD-enter-exit-origin-39: followed; it sets no values (DESIGN.md carries it)
- STD-springs-gestures-01: followed; it sets no values (DESIGN.md carries it)
- STD-springs-gestures-02: followed; it sets no values (DESIGN.md carries it)
- STD-springs-gestures-04: motion.spring.spatial.dampingRatio = 1.0
- STD-springs-gestures-04: motion.spring.spatial.stiffness = 246.7
- STD-springs-gestures-05: followed; it sets no values (DESIGN.md carries it)
- STD-springs-gestures-06: motion.spring.momentum = {"dampingRatio": 0.8, "stiffness": 246.7, "mass": 1}
- STD-springs-gestures-07: followed; it sets no values (DESIGN.md and review carry it)
- STD-springs-gestures-08: motion.spring.sheet = {"dampingRatio": 0.8, "stiffness": 438.6, "mass": 1}
- STD-springs-gestures-09: motion.spring.rotation = {"dampingRatio": 0.8, "stiffness": 246.7, "mass": 1}
- STD-springs-gestures-11: followed; it sets no values (DESIGN.md carries it)
- STD-springs-gestures-12: followed; it sets no values (DESIGN.md carries it)
- STD-springs-gestures-13: followed; it sets no values (DESIGN.md carries it)
- STD-springs-gestures-14: followed; it sets no values (DESIGN.md carries it)
- STD-springs-gestures-16: followed; it sets no values (DESIGN.md carries it)
- STD-springs-gestures-17: followed; it sets no values (DESIGN.md carries it)
- STD-springs-gestures-19: motion.gesture.deceleration-rate = 0.998
- STD-springs-gestures-20: followed; it sets no values (DESIGN.md carries it)
- STD-springs-gestures-21: motion.gesture.dismiss-velocity = 0.11
- STD-springs-gestures-25: motion.gesture.rubberband-constant = 0.55
- STD-springs-gestures-26: followed; it sets no values (DESIGN.md carries it)
- STD-springs-gestures-30: motion.gesture.direction-threshold = 10px
- STD-springs-gestures-34: followed; it sets no values (DESIGN.md carries it)
- STD-springs-gestures-39: followed; it sets no values (DESIGN.md and review carry it)
- STD-springs-gestures-41: followed; it sets no values (DESIGN.md carries it)
- STD-springs-gestures-42: followed; it sets no values (DESIGN.md carries it)
- STD-springs-gestures-59: followed; it sets no values (DESIGN.md carries it)
- STD-springs-gestures-60: followed; it sets no values (DESIGN.md carries it)
- STD-springs-gestures-61: followed; it sets no values (DESIGN.md carries it)
- STD-springs-gestures-63: followed; it sets no values (DESIGN.md carries it)
- STD-performance-properties-01: followed; it sets no values (DESIGN.md and review carry it)
- STD-performance-properties-02: followed; it sets no values (DESIGN.md carries it)
- STD-performance-properties-10: followed; it sets no values (DESIGN.md and review carry it)
- STD-performance-properties-13: followed; it sets no values (DESIGN.md carries it)
- STD-performance-properties-16: followed; it sets no values (DESIGN.md carries it)
- STD-performance-properties-18: followed; it sets no values (DESIGN.md and review carry it)
- STD-performance-properties-19: followed; it sets no values (DESIGN.md and review carry it)
- STD-performance-properties-20: followed; it sets no values (DESIGN.md and review carry it)
- STD-performance-properties-25: followed; it sets no values (DESIGN.md carries it)
- STD-accessibility-motion-01: followed; it sets no values (DESIGN.md carries it)
- STD-accessibility-motion-02: raw.reducedMotion = "replace"
- STD-accessibility-motion-02: motion.duration.reduced-fade = 200ms
- STD-accessibility-motion-02: reduced:motion.transition.enter = {"duration": "{motion.duration.reduced-fade}", "delay": {"value": 0, "unit": "ms"}, "timingFunction": [0.25, 0.1, 0.25, 1]}
- STD-accessibility-motion-02: reduced:motion.transition.exit = {"duration": "{motion.duration.reduced-fade}", "delay": {"value": 0, "unit": "ms"}, "timingFunction": [0.25, 0.1, 0.25, 1]}
- STD-accessibility-motion-02: reduced:motion.transition.expand = {"duration": "{motion.duration.reduced-fade}", "delay": {"value": 0, "unit": "ms"}, "timingFunction": [0.25, 0.1, 0.25, 1]}
- STD-accessibility-motion-06: followed; it sets no values
- STD-accessibility-motion-07: followed; it sets no values (DESIGN.md carries it)
- STD-accessibility-motion-08: followed; it sets no values (DESIGN.md and review carry it)
- STD-accessibility-motion-09: followed; it sets no values (DESIGN.md carries it)
- STD-accessibility-motion-10: followed; it sets no values (DESIGN.md carries it)
- STD-accessibility-motion-13: followed; it sets no values (DESIGN.md and review carry it)
- STD-accessibility-motion-20: followed; it sets no values (DESIGN.md carries it)
- STD-accessibility-motion-24: followed; it sets no values (DESIGN.md carries it)
- STD-components-toasts-drawers-08: followed; it sets no values (DESIGN.md carries it)
- STD-components-toasts-drawers-11: followed; it sets no values (DESIGN.md carries it)
- STD-components-toasts-drawers-15: component.toast.duration = 4000ms
- STD-components-toasts-drawers-18: followed; it sets no values (DESIGN.md carries it)
- STD-components-toasts-drawers-37: followed; it sets no values (DESIGN.md carries it)
- STD-components-toasts-drawers-40: motion.easing.drawer = [0.32, 0.72, 0, 1]
- STD-components-toasts-drawers-44: motion.gesture.drag-lock-after-scroll = 100ms
- STD-components-toasts-drawers-48: followed; it sets no values (DESIGN.md carries it)
- STD-components-toasts-drawers-60: followed; it sets no values (DESIGN.md carries it)
- STD-components-toasts-drawers-72: followed; it sets no values (DESIGN.md carries it)
- STD-mobile-touch-05: motion.scale.press = 0.97
- STD-mobile-touch-05: motion.duration.micro = 100ms
- STD-mobile-touch-07: followed; it sets no values (DESIGN.md carries it)
- STD-mobile-touch-08: followed; it sets no values (DESIGN.md carries it)
- STD-mobile-touch-09: size.target.touch = 44px
- STD-mobile-touch-09: size.target.min = 44px
- STD-mobile-touch-16: followed; it sets no values (DESIGN.md carries it)
- STD-mobile-touch-24: followed; it sets no values
- STD-mobile-touch-28: followed; it sets no values (DESIGN.md carries it)
- STD-mobile-touch-30: followed; it sets no values (DESIGN.md carries it)
- STD-mobile-touch-33: followed; it sets no values (DESIGN.md and review carry it)
- STD-mobile-touch-34: followed; it sets no values (DESIGN.md and review carry it)
- STD-mobile-touch-35: followed; it sets no values (DESIGN.md carries it)
- STD-mobile-touch-36: followed; it sets no values (DESIGN.md carries it)
- STD-mobile-touch-37: followed; it sets no values (DESIGN.md carries it)
- STD-mobile-touch-38: followed; it sets no values (DESIGN.md carries it)
- STD-mobile-touch-39: followed; it sets no values (DESIGN.md and review carry it)
- STD-mobile-touch-41: followed; it sets no values (DESIGN.md and review carry it)
- STD-mobile-touch-42: followed; it sets no values (DESIGN.md carries it)
- STD-mobile-touch-44: followed; it sets no values (DESIGN.md carries it)
- STD-mobile-touch-48: followed; it sets no values (DESIGN.md carries it)
- STD-mobile-touch-51: motion.spring.spatial.dampingRatio = 1.0
- STD-mobile-touch-60: followed; it sets no values (DESIGN.md carries it)
- STD-mobile-touch-61: followed; it sets no values (DESIGN.md and review carry it)
- STD-mobile-touch-62: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-02: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-03: followed; it sets no values (DESIGN.md and review carry it)
- STD-visual-details-04: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-05: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-06: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-07: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-08: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-09: followed; it sets no values (DESIGN.md and review carry it)
- STD-visual-details-11: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-13: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-14: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-17: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-18: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-19: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-20: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-21: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-24: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-25: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-26: followed; it sets no values (DESIGN.md and review carry it)
- STD-visual-details-27: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-28: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-29: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-30: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-31: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-32: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-33: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-34: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-35: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-36: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-37: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-38: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-39: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-40: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-41: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-42: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-43: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-44: followed; it sets no values
- STD-visual-details-45: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-46: followed; it sets no values
- STD-visual-details-47: followed; it sets no values
- STD-visual-details-48: followed; it sets no values
- STD-visual-details-49: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-50: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-51: followed; it sets no values (DESIGN.md carries it)
- STD-visual-details-64: followed; it sets no values (DESIGN.md carries it)
- STD-process-review-taste-01: followed; it sets no values (DESIGN.md carries it)
- STD-process-review-taste-02: followed; it sets no values
- STD-process-review-taste-03: followed; it sets no values (DESIGN.md carries it)
- STD-process-review-taste-04: followed; it sets no values (DESIGN.md carries it)
- STD-process-review-taste-05: followed; it sets no values (DESIGN.md carries it)
- STD-process-review-taste-06: followed; it sets no values (DESIGN.md carries it)
- STD-process-review-taste-07: followed; it sets no values
- STD-process-review-taste-08: followed; it sets no values
- STD-process-review-taste-09: followed; it sets no values
- STD-process-review-taste-10: followed; it sets no values
- STD-process-review-taste-11: followed; it sets no values
- STD-process-review-taste-12: followed; it sets no values
- STD-process-review-taste-13: followed; it sets no values
- STD-process-review-taste-14: followed; it sets no values
- STD-process-review-taste-15: followed; it sets no values
- STD-process-review-taste-16: followed; it sets no values
- STD-process-review-taste-17: followed; it sets no values
- STD-process-review-taste-18: followed; it sets no values
- STD-process-review-taste-19: followed; it sets no values
- STD-process-review-taste-20: followed; it sets no values
- STD-process-review-taste-21: followed; it sets no values
- STD-process-review-taste-22: followed; it sets no values
- STD-process-review-taste-23: followed; it sets no values
- STD-process-review-taste-24: followed; it sets no values
- STD-process-review-taste-25: followed; it sets no values
- STD-process-review-taste-26: followed; it sets no values (DESIGN.md carries it)
- STD-process-review-taste-27: followed; it sets no values (DESIGN.md carries it)
- STD-process-review-taste-28: followed; it sets no values (DESIGN.md carries it)
- STD-process-review-taste-29: followed; it sets no values (DESIGN.md carries it)
- STD-process-review-taste-30: followed; it sets no values (DESIGN.md carries it)
- STD-process-review-taste-31: followed; it sets no values
- STD-process-review-taste-32: followed; it sets no values (DESIGN.md carries it)
- STD-process-review-taste-33: followed; it sets no values (DESIGN.md carries it)
- STD-process-review-taste-34: followed; it sets no values
- STD-process-review-taste-35: followed; it sets no values
- STD-process-review-taste-36: followed; it sets no values (DESIGN.md carries it)
- STD-process-review-taste-37: followed; it sets no values
- STD-process-review-taste-38: followed; it sets no values
- STD-process-review-taste-39: followed; it sets no values
- STD-process-review-taste-40: followed; it sets no values (review carries it)
- STD-process-review-taste-42: followed; it sets no values
- STD-process-review-taste-43: followed; it sets no values
- STD-process-review-taste-44: followed; it sets no values
- STD-process-review-taste-47: followed; it sets no values
- STD-process-review-taste-48: followed; it sets no values
- STD-process-review-taste-49: followed; it sets no values
- STD-process-review-taste-50: followed; it sets no values
- STD-process-review-taste-51: followed; it sets no values
- STD-process-review-taste-52: followed; it sets no values
- STD-process-review-taste-53: followed; it sets no values
- STD-process-review-taste-54: followed; it sets no values
- STD-process-review-taste-55: followed; it sets no values
- STD-process-review-taste-56: followed; it sets no values
- STD-process-review-taste-57: followed; it sets no values
- STD-process-review-taste-58: followed; it sets no values
- STD-process-review-taste-59: followed; it sets no values
- STD-process-review-taste-60: followed; it sets no values
- STD-process-review-taste-63: followed; it sets no values
- STD-process-review-taste-64: followed; it sets no values
- STD-process-review-taste-66: followed; it sets no values
- STD-process-review-taste-67: followed; it sets no values (DESIGN.md carries it)
- STD-swift-01: followed; it sets no values (DESIGN.md carries it)
- STD-swift-02: followed; it sets no values (DESIGN.md carries it)
- STD-swift-03: followed; it sets no values (DESIGN.md carries it)
- STD-swift-04: followed; it sets no values
- STD-swift-05: followed; it sets no values
- STD-swift-06: followed; it sets no values
- STD-swift-07: followed; it sets no values (DESIGN.md carries it)
- STD-swift-08: followed; it sets no values
- STD-swift-09: followed; it sets no values
- STD-swift-10: followed; it sets no values
- STD-swift-11: followed; it sets no values
- STD-swift-12: followed; it sets no values
- STD-swift-13: followed; it sets no values
- STD-swift-14: followed; it sets no values
- STD-swift-15: followed; it sets no values (DESIGN.md carries it)
- STD-swift-16: followed; it sets no values (DESIGN.md carries it)
- STD-swift-17: followed; it sets no values (DESIGN.md carries it)
- STD-swift-18: followed; it sets no values (DESIGN.md carries it)
- STD-swift-19: followed; it sets no values (DESIGN.md and review carry it)
- STD-swift-20: followed; it sets no values
- STD-swift-21: followed; it sets no values
- STD-swift-22: followed; it sets no values
- STD-swift-23: followed; it sets no values
- STD-swift-24: followed; it sets no values
- STD-swift-25: followed; it sets no values
- STD-swift-26: followed; it sets no values
- STD-swift-27: followed; it sets no values
- STD-swift-28: followed; it sets no values
- STD-swift-29: followed; it sets no values
- STD-swift-30: followed; it sets no values
- STD-swift-31: followed; it sets no values
- STD-swift-32: followed; it sets no values
- STD-swift-33: followed; it sets no values
- STD-swift-34: followed; it sets no values
- STD-swift-35: followed; it sets no values (DESIGN.md carries it)
- STD-swift-36: followed; it sets no values (review carries it)
- STD-swift-37: followed; it sets no values
- STD-swift-38: followed; it sets no values
- STD-swift-39: followed; it sets no values
- STD-swift-40: followed; it sets no values
- STD-swift-41: followed; it sets no values
- STD-swift-42: followed; it sets no values
- STD-swift-43: followed; it sets no values (DESIGN.md and review carry it)
- STD-swift-44: followed; it sets no values (DESIGN.md carries it)
- STD-swift-45: followed; it sets no values (DESIGN.md carries it)
- STD-swift-46: followed; it sets no values (DESIGN.md carries it)
- STD-swift-47: followed; it sets no values
- STD-swift-48: followed; it sets no values
- STD-swift-49: followed; it sets no values
- STD-swift-50: followed; it sets no values
- STD-swift-51: followed; it sets no values
- STD-swift-52: followed; it sets no values (review carries it)
- STD-swift-53: followed; it sets no values
- STD-swift-54: followed; it sets no values
- STD-swift-55: followed; it sets no values
- STD-swift-56: followed; it sets no values
- STD-swift-57: followed; it sets no values
- STD-swift-58: followed; it sets no values
- STD-swift-59: followed; it sets no values
- STD-swift-60: followed; it sets no values (review carries it)
- STD-swift-61: followed; it sets no values
- STD-swift-62: followed; it sets no values
- STD-swift-63: followed; it sets no values
- STD-swift-64: followed; it sets no values
- STD-swift-65: followed; it sets no values
- STD-swift-66: followed; it sets no values
- STD-swift-67: followed; it sets no values
- STD-swift-68: followed; it sets no values
- STD-swift-69: followed; it sets no values (review carries it)
- STD-swift-70: followed; it sets no values
- STD-swift-71: followed; it sets no values
- STD-swift-72: followed; it sets no values
- STD-swift-73: followed; it sets no values
- STD-swift-74: followed; it sets no values
- STD-swift-75: followed; it sets no values
- STD-swift-76: followed; it sets no values
- STD-swift-77: followed; it sets no values
- STD-swift-78: followed; it sets no values
- STD-swift-79: followed; it sets no values
- STD-swift-80: followed; it sets no values
- STD-swift-81: followed; it sets no values
- STD-swift-82: followed; it sets no values
- STD-swift-83: followed; it sets no values
- STD-swift-84: followed; it sets no values
- STD-swift-85: followed; it sets no values
- STD-swift-86: followed; it sets no values
- STD-swift-87: followed; it sets no values
- STD-swift-88: followed; it sets no values (review carries it)
- STD-swift-89: followed; it sets no values
- STD-swift-90: followed; it sets no values
- STD-swift-91: followed; it sets no values
- STD-swift-92: followed; it sets no values
- STD-swift-93: followed; it sets no values
- STD-swift-94: followed; it sets no values
- STD-swift-95: followed; it sets no values
- STD-swift-96: followed; it sets no values
- STD-swift-97: followed; it sets no values (DESIGN.md and review carry it)
- STD-swift-98: followed; it sets no values
- STD-swift-99: followed; it sets no values
- STD-swift-100: followed; it sets no values
- STD-swift-101: followed; it sets no values
- STD-swift-102: followed; it sets no values
- STD-swift-103: followed; it sets no values
- STD-swift-104: followed; it sets no values
- STD-swift-105: followed; it sets no values
- STD-swift-106: followed; it sets no values
- STD-swift-107: followed; it sets no values
- STD-swift-108: followed; it sets no values
- STD-swift-109: followed; it sets no values
- STD-swift-110: followed; it sets no values
- STD-swift-111: followed; it sets no values
- STD-swift-112: followed; it sets no values
- STD-swift-113: followed; it sets no values

## D-0009 · dials.expression = 90
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: a game-like lesson: mascot, chunky tiles, celebration

## D-0010 · dials.brandPresence = 85
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: the lesson is the brand moment

## D-0011 · dials.density = 40
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: one exercise per screen, big tap tiles
- previous value: 50

## D-0012 · dials.energy = 85
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: snappy, bouncy feedback

## D-0013 · dials.roundness = 75
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: chunky, toy-like corners

## D-0014 · dials.depth = 60
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: tiles sit on a hard bottom edge so they read as pressable

## D-0015 · dials.colorfulness = 95
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: bright primaries: cobalt, sunflower, tomato

## D-0016 · dials.warmth = 60
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: warm white paper under the primaries

## D-0017 · raw.textFace = "Nunito"
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: rounded sans (OFL), sturdy and friendly at reading sizes
- previous value: "system"

## D-0018 · raw.displayFace = "Fredoka"
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: chunky rounded display (OFL) for prompts and buttons
- previous value: "=textFace"

## D-0019 · raw.fontLicence = {"web": true, "app": true, "selfHost": true}
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: SIL Open Font License faces from Google Fonts: web, apps and self-hosting allowed
- previous value: {"web": null, "app": null, "selfHost": null}

## D-0020 · raw.accentCount = 3
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: bright primaries: cobalt, sunflower, tomato

## D-0021 · raw.secondaryColors = ["#FFC531", "#F2493B"]
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: sunflower yellow and tomato red
- previous value: []

## D-0022 · answers.Q-scope-06 = "experience"
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: a game-like lesson is an experience surface
- also set: raw.productType = "marketing" (from Q-scope-06)
- also set: raw.marketingSurfaces = true (from Q-scope-06)

## D-0023 · raw.baseSize = 17
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: iOS body text is 17 pt; the engine gave 14-16 because brand presence is above 50

## D-0024 · answers.Q-dir-01 = "neo-brutalist"
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: chunky toy-like tiles with a hard bottom edge read as pressable; playful indie product
- also set: preset = "neobrutal" (from Q-dir-01)

## D-0025 · raw.textFace = "Plus Jakarta Sans"
- set_by: chosen · locked: no · date: 2026-10-15 · supersedes: D-0017 · source_ref: none
- reason: round 4: owner said the app screens look cheap and toy-like; rebuilt as a calm speaking-feedback screen; the UI face
- previous value: "Nunito"

## D-0026 · raw.displayFace = "Spectral"
- set_by: chosen · locked: no · date: 2026-10-15 · supersedes: D-0018 · source_ref: none
- reason: round 4: owner said the app screens look cheap and toy-like; rebuilt as a calm speaking-feedback screen; the Italian itself is set like a book, so the language is the hero
- previous value: "Fredoka"

## D-0027 · raw.fontLicence = {"web": true, "app": true, "selfHost": true}
- set_by: chosen · locked: no · date: 2026-10-15 · supersedes: D-0019 · source_ref: none
- reason: Plus Jakarta Sans and Spectral are SIL OFL
- previous value: {"web": true, "app": true, "selfHost": true}

## D-0028 · raw.brandColor = "#CC3B22"
- set_by: chosen · locked: no · date: 2026-10-15 · supersedes: D-0004 · source_ref: none
- reason: round 4: owner said the app screens look cheap and toy-like; rebuilt as a calm speaking-feedback screen; one vermilion accent with one job: what to fix (4.98:1 on white)
- previous value: "#2a5bd7"

## D-0029 · raw.accentCount = 1
- set_by: chosen · locked: no · date: 2026-10-15 · supersedes: D-0020 · source_ref: none
- reason: one accent
- previous value: 3

## D-0030 · raw.secondaryColors = []
- set_by: chosen · locked: no · date: 2026-10-15 · supersedes: D-0021 · source_ref: none
- reason: sunflower and tomato removed
- previous value: ["#FFC531", "#F2493B"]

## D-0031 · raw.neutralBase = "#8A8F98"
- set_by: chosen · locked: no · date: 2026-10-15 · supersedes: none · source_ref: none
- reason: cool neutral: white page, near-black ink

## D-0032 · dials.expression = 40
- set_by: delegated · locked: no · date: 2026-10-15 · supersedes: D-0009 · source_ref: none
- reason: round 4: owner said the app screens look cheap and toy-like; rebuilt as a calm speaking-feedback screen
- previous value: 90

## D-0033 · dials.brandPresence = 40
- set_by: delegated · locked: no · date: 2026-10-15 · supersedes: D-0010 · source_ref: none
- reason: round 4: owner said the app screens look cheap and toy-like; rebuilt as a calm speaking-feedback screen
- previous value: 85

## D-0034 · dials.energy = 35
- set_by: delegated · locked: no · date: 2026-10-15 · supersedes: D-0012 · source_ref: none
- reason: round 4: owner said the app screens look cheap and toy-like; rebuilt as a calm speaking-feedback screen
- previous value: 85

## D-0035 · dials.roundness = 55
- set_by: delegated · locked: no · date: 2026-10-15 · supersedes: D-0013 · source_ref: none
- reason: round 4: owner said the app screens look cheap and toy-like; rebuilt as a calm speaking-feedback screen
- previous value: 75

## D-0036 · dials.depth = 15
- set_by: delegated · locked: no · date: 2026-10-15 · supersedes: D-0014 · source_ref: none
- reason: round 4: owner said the app screens look cheap and toy-like; rebuilt as a calm speaking-feedback screen
- previous value: 60

## D-0037 · dials.colorfulness = 30
- set_by: delegated · locked: no · date: 2026-10-15 · supersedes: D-0015 · source_ref: none
- reason: round 4: owner said the app screens look cheap and toy-like; rebuilt as a calm speaking-feedback screen
- previous value: 95

## D-0038 · dials.warmth = 35
- set_by: delegated · locked: no · date: 2026-10-15 · supersedes: D-0016 · source_ref: none
- reason: round 4: owner said the app screens look cheap and toy-like; rebuilt as a calm speaking-feedback screen
- previous value: 60

## D-0039 · dials.density = 45
- set_by: delegated · locked: no · date: 2026-10-15 · supersedes: D-0011 · source_ref: none
- reason: round 4: owner said the app screens look cheap and toy-like; rebuilt as a calm speaking-feedback screen
- previous value: 40

## D-0040 · overrides.font.size.11 = {"value": 11, "unit": "px"}
- set_by: chosen · locked: no · date: 2026-10-15 · supersedes: none · source_ref: none
- reason: iOS roles: Caption 2, Footnote, Subheadline, Body, Title 2, and 30 for the Italian sentence
- new dimension token in primitives.tokens.json

## D-0041 · overrides.font.size.13 = {"value": 13, "unit": "px"}
- set_by: chosen · locked: no · date: 2026-10-15 · supersedes: none · source_ref: none
- reason: iOS roles: Caption 2, Footnote, Subheadline, Body, Title 2, and 30 for the Italian sentence
- new dimension token in primitives.tokens.json

## D-0042 · overrides.font.size.15 = {"value": 15, "unit": "px"}
- set_by: chosen · locked: no · date: 2026-10-15 · supersedes: none · source_ref: none
- reason: iOS roles: Caption 2, Footnote, Subheadline, Body, Title 2, and 30 for the Italian sentence
- new dimension token in primitives.tokens.json

## D-0043 · overrides.font.size.17 = {"value": 17, "unit": "px"}
- set_by: chosen · locked: no · date: 2026-10-15 · supersedes: none · source_ref: none
- reason: iOS roles: Caption 2, Footnote, Subheadline, Body, Title 2, and 30 for the Italian sentence

## D-0044 · overrides.font.size.22 = {"value": 22, "unit": "px"}
- set_by: chosen · locked: no · date: 2026-10-15 · supersedes: none · source_ref: none
- reason: iOS roles: Caption 2, Footnote, Subheadline, Body, Title 2, and 30 for the Italian sentence
- new dimension token in primitives.tokens.json

## D-0045 · overrides.font.size.30 = {"value": 30, "unit": "px"}
- set_by: chosen · locked: no · date: 2026-10-15 · supersedes: none · source_ref: none
- reason: iOS roles: Caption 2, Footnote, Subheadline, Body, Title 2, and 30 for the Italian sentence
- new dimension token in primitives.tokens.json

## D-0046 · raw.textFace = "IBM Plex Sans"
- set_by: chosen · locked: no · date: 2026-10-15 · supersedes: D-0025 · source_ref: none
- reason: round 4 audit: Plus Jakarta Sans draws I and l alike ('Al bar' read as 'AI bar') and read as a startup template; Plex Sans has a serifed I and a tailed l, which a language app needs
- previous value: "Plus Jakarta Sans"

## D-0047 · raw.textFace = "Inter"
- set_by: chosen · locked: no · date: 2026-10-15 · supersedes: D-0046 · source_ref: none
- reason: round 4 audit 2: IBM Plex digits made the status bar read as not-iOS; Inter is the closest open face to SF. The Italian lesson name is set in Spectral so 'Al bar' cannot read as 'AI bar'
- previous value: "IBM Plex Sans"

## D-0048 · raw.textFace = "IBM Plex Sans"
- set_by: chosen · locked: no · date: 2026-10-15 · supersedes: D-0047 · source_ref: none
- reason: round 4 audit 3: Inter read as the vibe-coded default and Spectral inside an Inter line looked like a fallback; Plex Sans has a serifed I and a tailed l, so 'Al bar' reads right in one face
- previous value: "Inter"

## D-0049 · overrides.font.size.48 = {"value": 48, "unit": "px"}
- set_by: chosen · locked: no · date: 2026-10-15 · supersedes: none · source_ref: none
- reason: round 4 audit 3: the score becomes one confident number
- new dimension token in primitives.tokens.json

## D-0050 · overrides.font.size.34 = {"value": 34, "unit": "px"}
- set_by: chosen · locked: no · date: 2026-10-18 · supersedes: none · source_ref: none
- reason: round 4 audit 5: the word to fix becomes the one large moment (Large Title)
- new dimension token in primitives.tokens.json
