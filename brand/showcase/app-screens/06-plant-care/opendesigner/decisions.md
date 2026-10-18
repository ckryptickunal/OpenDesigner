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

## D-0004 · raw.brandColor = "#4e6e48"
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: sketch: picked for them

## D-0005 · answers.Q-plat-01 = ["ios"]
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: sketch: picked for them
- also set: raw.platforms = ["ios"] (from Q-plat-01)

## D-0006 · macros = ["friendly", "deferential"]
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: sketch: picked for them (feel words: gentle, cozy)
- previous value: []

## D-0007 · taste.feelWords = ["gentle", "cozy"]
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

## D-0009 · raw.textFace = "Figtree"
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: humanist-geometric sans, open (OFL), friendly at small sizes
- previous value: "system"

## D-0010 · raw.displayFace = "Fraunces"
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: soft old-style serif (OFL) with a gardener's-notebook warmth
- previous value: "=textFace"

## D-0011 · dials.expression = 55
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: calm-but-crafted diary; the illustration carries the personality

## D-0012 · dials.brandPresence = 45
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: brand shows in the arch portraits and terracotta, not on every surface

## D-0013 · dials.density = 38
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: a slow daily ritual: airy cards, one task per row
- previous value: 50

## D-0014 · dials.energy = 30
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: unhurried; nothing shouts

## D-0015 · dials.roundness = 82
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: organic: leaves, pots, arches

## D-0016 · dials.depth = 25
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: paper-flat with a soft lift on the hero card

## D-0017 · dials.colorfulness = 45
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: moss and terracotta; the rest is warm neutral

## D-0018 · dials.warmth = 82
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: terracotta, cream paper, sunlight

## D-0019 · raw.fontLicence = {"web": true, "app": true, "selfHost": true}
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: SIL Open Font License faces from Google Fonts: web, apps and self-hosting allowed
- previous value: {"web": null, "app": null, "selfHost": null}

## D-0020 · raw.accentCount = 2
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: moss for actions, terracotta for pots and the watering schedule

## D-0021 · raw.secondaryColors = ["#C0603A"]
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: terracotta, the color of clay pots
- previous value: []

## D-0022 · raw.neutralBase = "#E8DCC6"
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: cream paper neutrals, like a potting-shed notebook

## D-0023 · raw.neutralBase = "#E6E0D2"
- set_by: chosen · locked: no · date: 2026-10-14 · supersedes: D-0022 · source_ref: none
- reason: owner rule: no muddy brown mid-tones; a calmer paper keeps secondary text olive-grey, not brown (the Warmth dial does nothing once neutralBase is set)
- previous value: "#E8DCC6"

## D-0024 · raw.displayFace = "Alegreya"
- set_by: chosen · locked: no · date: 2026-10-14 · supersedes: D-0010 · source_ref: none
- reason: piece 03 already uses Fraunces; Alegreya is a calligraphic book serif with 400-900 weights, so a phrase can be set in bold
- previous value: "Fraunces"

## D-0025 · raw.accentCount = 1
- set_by: chosen · locked: no · date: 2026-10-14 · supersedes: D-0020 · source_ref: none
- reason: Round 3: one accent with one job. Moss marks today and the actions; the terracotta second accent is gone (audit: cream + orange-brown is the forbidden combination)
- previous value: 2

## D-0026 · raw.secondaryColors = []
- set_by: chosen · locked: no · date: 2026-10-14 · supersedes: D-0021 · source_ref: none
- reason: Round 3: terracotta removed
- previous value: ["#C0603A"]

## D-0027 · raw.neutralBase = "#8E928C"
- set_by: chosen · locked: no · date: 2026-10-14 · supersedes: D-0023 · source_ref: none
- reason: Round 3: a cool grey-green base gives a clean white page and near-black ink instead of cream paper and brown-grey text
- previous value: "#E6E0D2"

## D-0028 · dials.roundness = 60
- set_by: delegated · locked: no · date: 2026-10-14 · supersedes: D-0015 · source_ref: none
- reason: Round 3: friendly but not blobby; photos and cards at 16, controls full
- previous value: 82

## D-0029 · overrides.font.size.11 = {"value": 11, "unit": "px"}
- set_by: chosen · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: Round 3: iOS Dynamic Type step
- new dimension token in primitives.tokens.json

## D-0030 · overrides.font.size.12 = {"value": 12, "unit": "px"}
- set_by: chosen · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: Round 3: iOS Dynamic Type step
- new dimension token in primitives.tokens.json

## D-0031 · overrides.font.size.13 = {"value": 13, "unit": "px"}
- set_by: chosen · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: Round 3: iOS Dynamic Type step
- new dimension token in primitives.tokens.json

## D-0032 · overrides.font.size.15 = {"value": 15, "unit": "px"}
- set_by: chosen · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: Round 3: iOS Dynamic Type step
- new dimension token in primitives.tokens.json

## D-0033 · overrides.font.size.17 = {"value": 17, "unit": "px"}
- set_by: chosen · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: Round 3: iOS Dynamic Type step

## D-0034 · overrides.font.size.20 = {"value": 20, "unit": "px"}
- set_by: chosen · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: Round 3: iOS Dynamic Type step
- new dimension token in primitives.tokens.json

## D-0035 · overrides.font.size.22 = {"value": 22, "unit": "px"}
- set_by: chosen · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: Round 3: iOS Dynamic Type step
- new dimension token in primitives.tokens.json

## D-0036 · overrides.font.size.28 = {"value": 28, "unit": "px"}
- set_by: chosen · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: Round 3: iOS Dynamic Type step
- new dimension token in primitives.tokens.json

## D-0037 · overrides.font.size.34 = {"value": 34, "unit": "px"}
- set_by: chosen · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: Round 3: iOS Dynamic Type step
- new dimension token in primitives.tokens.json

## D-0038 · overrides.font.size.48 = {"value": 48, "unit": "px"}
- set_by: chosen · locked: no · date: 2026-10-14 · supersedes: none · source_ref: none
- reason: Round 3: the soil reading, a custom display role above Large Title 34
- new dimension token in primitives.tokens.json

## D-0039 · raw.textFace = "Onest"
- set_by: chosen · locked: no · date: 2026-10-15 · supersedes: D-0009 · source_ref: none
- reason: round 4: owner said the app screens look cheap; rebuilt as a plant detail with a soil-moisture chart; one SF-like face does the work through size and weight
- previous value: "Figtree"

## D-0040 · raw.displayFace = "Onest"
- set_by: chosen · locked: no · date: 2026-10-15 · supersedes: D-0024 · source_ref: none
- reason: round 4: owner said the app screens look cheap; rebuilt as a plant detail with a soil-moisture chart; Alegreya removed, one face
- previous value: "Alegreya"

## D-0041 · raw.fontLicence = {"web": true, "app": true, "selfHost": true}
- set_by: chosen · locked: no · date: 2026-10-15 · supersedes: D-0019 · source_ref: none
- reason: Onest is SIL OFL
- previous value: {"web": true, "app": true, "selfHost": true}

## D-0042 · raw.brandColor = "#3F6B45"
- set_by: chosen · locked: no · date: 2026-10-15 · supersedes: D-0004 · source_ref: none
- reason: round 4: owner said the app screens look cheap; rebuilt as a plant detail with a soil-moisture chart; a deeper, cooler moss so white button text passes AA and it reads as leaf, not olive
- previous value: "#4e6e48"

## D-0043 · dials.expression = 35
- set_by: delegated · locked: no · date: 2026-10-15 · supersedes: D-0011 · source_ref: none
- reason: round 4: owner said the app screens look cheap; rebuilt as a plant detail with a soil-moisture chart
- previous value: 55

## D-0044 · dials.roundness = 55
- set_by: delegated · locked: no · date: 2026-10-15 · supersedes: D-0028 · source_ref: none
- reason: round 4: owner said the app screens look cheap; rebuilt as a plant detail with a soil-moisture chart
- previous value: 60

## D-0045 · dials.depth = 15
- set_by: delegated · locked: no · date: 2026-10-15 · supersedes: D-0016 · source_ref: none
- reason: round 4: owner said the app screens look cheap; rebuilt as a plant detail with a soil-moisture chart
- previous value: 25

## D-0046 · dials.density = 50
- set_by: delegated · locked: no · date: 2026-10-15 · supersedes: D-0013 · source_ref: none
- reason: round 4: owner said the app screens look cheap; rebuilt as a plant detail with a soil-moisture chart
- previous value: 38

## D-0047 · dials.colorfulness = 35
- set_by: delegated · locked: no · date: 2026-10-15 · supersedes: D-0017 · source_ref: none
- reason: round 4: owner said the app screens look cheap; rebuilt as a plant detail with a soil-moisture chart
- previous value: 45

## D-0048 · overrides.font.size.11 = {"value": 11, "unit": "px"}
- set_by: chosen · locked: no · date: 2026-10-15 · supersedes: D-0029 · source_ref: none
- reason: iOS roles: Caption 2, Footnote, Subheadline, Body, Title 2, Large Title
- previous value: {"value": 11, "unit": "px"}

## D-0049 · overrides.font.size.13 = {"value": 13, "unit": "px"}
- set_by: chosen · locked: no · date: 2026-10-15 · supersedes: D-0031 · source_ref: none
- reason: iOS roles: Caption 2, Footnote, Subheadline, Body, Title 2, Large Title
- previous value: {"value": 13, "unit": "px"}

## D-0050 · overrides.font.size.15 = {"value": 15, "unit": "px"}
- set_by: chosen · locked: no · date: 2026-10-15 · supersedes: D-0032 · source_ref: none
- reason: iOS roles: Caption 2, Footnote, Subheadline, Body, Title 2, Large Title
- previous value: {"value": 15, "unit": "px"}

## D-0051 · overrides.font.size.17 = {"value": 17, "unit": "px"}
- set_by: chosen · locked: no · date: 2026-10-15 · supersedes: D-0033 · source_ref: none
- reason: iOS roles: Caption 2, Footnote, Subheadline, Body, Title 2, Large Title
- previous value: {"value": 17, "unit": "px"}

## D-0052 · overrides.font.size.22 = {"value": 22, "unit": "px"}
- set_by: chosen · locked: no · date: 2026-10-15 · supersedes: D-0035 · source_ref: none
- reason: iOS roles: Caption 2, Footnote, Subheadline, Body, Title 2, Large Title
- previous value: {"value": 22, "unit": "px"}

## D-0053 · overrides.font.size.34 = {"value": 34, "unit": "px"}
- set_by: chosen · locked: no · date: 2026-10-15 · supersedes: D-0037 · source_ref: none
- reason: iOS roles: Caption 2, Footnote, Subheadline, Body, Title 2, Large Title
- previous value: {"value": 34, "unit": "px"}

## D-0054 · overrides.font.size.64 = {"value": 64, "unit": "px"}
- set_by: chosen · locked: no · date: 2026-10-15 · supersedes: none · source_ref: none
- reason: round 4 audit 3: the reading needs to be a confident number, like the 172 and 14A the owner likes
- new dimension token in primitives.tokens.json
