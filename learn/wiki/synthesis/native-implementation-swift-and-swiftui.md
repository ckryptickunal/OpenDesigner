---
type: synthesis
title: Native implementation (Swift and SwiftUI)
created: 2026-09-27
updated: 2026-09-27
sources:
  - eks-skills-write-swift-skill
tags:
  - od-area-platforms
---

# Native implementation (Swift and SwiftUI)

## In short

This page is about the Swift code behind an iPhone, iPad or Mac design system: how its data models, background work, SwiftUI views, tests and logs are written. The one source is Emil Kowalski's write-swift skill, whose through-line is to start with the simplest, most static, single-threaded code that works and to add concurrency, shared references or unsafe code only for a reason you can state. For SwiftUI that means views stay on the main thread, an animation that answers a gesture starts on the same frame as the gesture, and code SwiftUI runs off the main thread copies the one value it needs instead of capturing the whole view. The owner marked this source non-negotiable, so its rules are already the 113 locked `STD-swift` house standards; still, the page rests on a single source, and the parts the author states as preference stay opinion until another source agrees. It is a coding standard, not visual guidance, and it is dated: Swift 6.3 is the baseline, and Swift 6.4 features must not be written yet.

## House standards

This source is non-negotiable, so every rule it gives is a locked house standard: the whole Swift theme, 113 rules (50 must), all citing [S-L19-034]. Eight of them are checked in code by `engine.py review` (marked below). The full rules and their reasons are in `skills/opendesigner/references/standards/swift.md`.

The four that touch a design system's UI code most directly:

- `STD-swift-43` (should, checked by review): leave `@MainActor` off SwiftUI views and view models, and delete the ones you have once main-actor-by-default is on.
- `STD-swift-44` (must): when code that SwiftUI runs off the main thread (APIs marked `@Sendable`: `visualEffect`, `Shape.path(in:)`, `Layout` requirements, `onGeometryChange`) hits an isolation error, do not send `self`; copy the one value you need into the closure's capture list, for example `[pulse]`.
- `STD-swift-45` (must): start an animation that answers a gesture or scroll event with a `withAnimation` state change inside SwiftUI's synchronous action callback, on the same frame as the event; open a `Task` only for the long-running work that follows, and never make the callback async.
- `STD-swift-46` (should): put a piece of state on the seam between UI and async work: the view starts a task, the async layer makes a synchronous change when it finishes, and the UI reacts.

The whole theme, grouped as the source groups it:

- **Start here:** `STD-swift-01` Check the Swift toolchain first (must) · `STD-swift-02` Simplest, most static thing first (must)
- **Values and models:** `STD-swift-03` Value types by default (must) · `STD-swift-04` Declare with let by default (must) · `STD-swift-05` No mutable references inside structs (must) · `STD-swift-06` Copy-on-write for out-of-line storage (should) · `STD-swift-07` Make invalid states unrepresentable (must) · `STD-swift-08` Compose values into values (should) · `STD-swift-09` Noncopyable types for unique ownership (should)
- **Errors and optionals:** `STD-swift-10` Throw recoverable, trap on mistakes (must) · `STD-swift-11` Errors carry their context (should) · `STD-swift-12` guard for errors, if let to unwrap (should) · `STD-swift-13` Typed throws only internally (should) · `STD-swift-14` Force-unwrap only with a stated invariant (must)
- **Concurrency order and build settings:** `STD-swift-15` Main actor first, then step down (must) · `STD-swift-16` Enable Approachable Concurrency everywhere (must) · `STD-swift-17` MainActor default isolation for app modules (must) · `STD-swift-18` Libraries ship nonisolated APIs (must) · `STD-swift-19` @concurrent moves heavy work off-main (must, checked by review) · `STD-swift-20` No tasks for trivial work (must) · `STD-swift-21` One task per end-to-end operation (should) · `STD-swift-22` Nothing carried across an await (must) · `STD-swift-23` Actor methods are transactions (must) · `STD-swift-24` Never use actors for ordering (must) · `STD-swift-25` Isolate shared mutable state (should)
- **Sendable and sharing data:** `STD-swift-26` Write Sendable on public types (should) · `STD-swift-27` Model classes non-Sendable on purpose (should) · `STD-swift-28` Stop touching what you send (must) · `STD-swift-29` @Sendable only across domains (should) · `STD-swift-30` Unchecked promises are a last resort (must) · `STD-swift-31` Fix data races by not sharing (must) · `STD-swift-32` Globals: let before locks (should) · `STD-swift-33` Bridge callback APIs to the main actor (should)
- **Structured concurrency:** `STD-swift-34` Prefer structured tasks for children (must) · `STD-swift-35` Task { } only when no scope fits (should) · `STD-swift-36` Almost never use Task.detached (must, checked by review) · `STD-swift-37` Check cancellation before expensive work (must) · `STD-swift-38` Cancellation handlers need real locks (must) · `STD-swift-39` Bound how many children run (must) · `STD-swift-40` Pass context through @TaskLocal values (should) · `STD-swift-41` Resume a continuation exactly once (must) · `STD-swift-42` AsyncStream for callback APIs (should)
- **SwiftUI:** `STD-swift-43` No @MainActor on SwiftUI views (should, checked by review) · `STD-swift-44` Copy values into @Sendable SwiftUI closures (must) · `STD-swift-45` Start animations on the event's frame (must) · `STD-swift-46` State on the UI/async seam (should)
- **Protocols and generics:** `STD-swift-47` Concrete types before protocols (must) · `STD-swift-48` No protocol without customization (should) · `STD-swift-49` Prefer has-a over is-a (should) · `STD-swift-50` Customization points are requirements (must) · `STD-swift-51` Composition over class inheritance (should) · `STD-swift-52` Treat forced downcasts as a smell (should, checked by review) · `STD-swift-53` some P by default (must) · `STD-swift-54` Open an existential through some P (should) · `STD-swift-55` Constrained opaque types, caller-facing associated types (should) · `STD-swift-56` Pin cross-protocol relationships with where (should) · `STD-swift-57` Homogeneous collections before any P (should)
- **API design:** `STD-swift-58` Clarity at the point of use (must) · `STD-swift-59` No type prefixes in Swift-only APIs (should) · `STD-swift-60` Drop the leading get (should, checked by review) · `STD-swift-61` Explicit access control at boundaries (should) · `STD-swift-113` Property wrappers for access policies (should)
- **Performance:** `STD-swift-62` Know which of four costs you pay (should) · `STD-swift-63` Do algorithmic work before micro-optimizing (must) · `STD-swift-64` Know the complexity you call (must) · `STD-swift-65` Size hot pipelines once (should) · `STD-swift-66` Profile a test in Instruments (must) · `STD-swift-67` final and whole-module optimization (should) · `STD-swift-68` Array until profiling says InlineArray (must) · `STD-swift-69` Span, not unsafe pointers (must, checked by review) · `STD-swift-70` async only when something awaits (should) · `STD-swift-71` Batch hops to the main actor (should) · `STD-swift-110` Inline and specialize only when measured (should)
- **Memory and object lifetime:** `STD-swift-72` Never depend on deinit timing (must) · `STD-swift-73` weak and unowned only break cycles (must) · `STD-swift-74` Break cycles by restructuring (should)
- **Testing:** `STD-swift-75` Swift Testing for new tests (must) · `STD-swift-76` #expect with plain expressions (should) · `STD-swift-77` try #require to stop a test (should) · `STD-swift-78` Test suites are structs (should) · `STD-swift-79` Parameterize, don't loop or copy (must) · `STD-swift-80` Traits carry test intent (should) · `STD-swift-81` Never comment a test out (must) · `STD-swift-82` confirmation for repeated callbacks (should) · `STD-swift-83` Keep tests parallel and random (should) · `STD-swift-84` Migrate tests incrementally, strict interop (should) · `STD-swift-109` Raw identifiers for test names (should) · `STD-swift-111` Exit tests for trap paths (should)
- **Macros:** `STD-swift-85` Macros only for derivable code (should) · `STD-swift-86` Test macros as syntax transforms (should) · `STD-swift-87` Macros emit real diagnostics (must)
- **Logging:** `STD-swift-88` Log with Logger, not print (must, checked by review) · `STD-swift-89` Opt log values into privacy (must) · `STD-swift-90` Log levels on purpose (should) · `STD-swift-91` Log a correlation ID (should) · `STD-swift-112` Format log values with format: and align: (should)
- **Unsafe code and interop:** `STD-swift-92` Keep unsafe regions tiny (must) · `STD-swift-93` Strict memory safety where it matters (should) · `STD-swift-94` Adopt Swift one file at a time (must)
- **Modern syntax:** `STD-swift-95` if and switch expressions (should) · `STD-swift-96` Parameter packs over arity overloads (should) · `STD-swift-97` Use @Observable, not ObservableObject (should, checked by review) · `STD-swift-98` Observations instead of polling for changes (should) · `STD-swift-99` Concrete notification types over userInfo (should) · `STD-swift-100` Use Subprocess for scripting processes (should) · `STD-swift-101` Swift Regex over index math (should) · `STD-swift-102` Swift Binary Parsing for binary formats (should) · `STD-swift-103` Foundation parsers inside regexes (must) · `STD-swift-104` Explicit locale when parsing (should) · `STD-swift-105` Stop regexes backtracking across input (should) · `STD-swift-108` Module selectors when a type shadows a module (should)
- **Migrating to Swift 6:** `STD-swift-106` Migrate to Swift 6 target by target (must) · `STD-swift-107` Refactor after migrating, separately (must)

Standards from other themes that reach native Apple UI code (written for every platform):

- `STD-when-to-animate-05` (must): no animation on anything people trigger or see 100+ times a day; on iOS that includes tab switches, keyboard open and close, scrolling and settings toggles (platform default or nothing).
- `STD-easing-duration-07` (must): on iOS and Android, press feedback 100-150ms, toggles, chips and small state changes 150-200ms, and sheets, modals and drawers a spring of about 300ms perceived.
- `STD-springs-gestures-19` (must): on release, project where a flick would come to rest with Apple's exponential-decay function and decide the outcome from that projected point.
- `STD-mobile-touch-09` (must): touch targets at least 44×44pt on iOS; when the visual is smaller, grow the hit area, never the visual.
- `STD-accessibility-motion-02` (must): under reduced motion, remove movement and keep a short cross-fade; never remove all feedback.
- `STD-visual-details-50` (should): build the details people will not consciously notice, such as matching the behaviour they expect from native components.

## What the sources teach

### Buy dynamism only with a reason

- Swift rewards "progressive disclosure": start with the simplest, most static, most single-threaded thing that works, and add concurrency, reference semantics, existentials or unsafe pointers only where you can point at the reason. The source gives a ladder of defaults: data as `struct` or `enum`, abstraction as a concrete type, polymorphism as `some P`, execution on the main actor and synchronous, memory as `Array` and `String`, and safe APIs; move down a rung only when you need identity or sharing, see repeated code, need mixed storage, or profiling shows a cost [S-L19-034] ([[sources/eks-skills-write-swift-skill-emilkowalski-skills-skills-write-swift-skill-md|emilkowalski/skills: skills/write-swift/SKILL.md]]).
- Check the toolchain first: Swift 6.3 is the baseline (current as of August 2026), the concurrency advice assumes the Swift 6.2 model and does not apply on 6.1 or earlier, and rows marked as Swift 6.4 are safe to plan around but not to write until the project builds with it [S-L19-034] ([[sources/eks-skills-write-swift-skill-emilkowalski-skills-skills-write-swift-skill-md|emilkowalski/skills: skills/write-swift/SKILL.md]]).

### Model data so wrong states cannot exist

- Use `struct` and `enum` by default and `class` only for identity, shared mutable state, inheritance or resource lifetime: a window or a database connection has identity, a point or a material does not. Declare with `let` unless you mutate [S-L19-034] ([[sources/eks-skills-write-swift-skill-emilkowalski-skills-skills-write-swift-skill-md|emilkowalski/skills: skills/write-swift/SKILL.md]]).
- Replace a pile of optional properties (`isSharing`, `selectedRows`, `shareTarget`) with one `enum State`, so invalid combinations cannot be written and a state change happens in one step. A struct built only from value types gets undo, diffing and state restoration through one code path [S-L19-034] ([[sources/eks-skills-write-swift-skill-emilkowalski-skills-skills-write-swift-skill-md|emilkowalski/skills: skills/write-swift/SKILL.md]]).
- A struct holding a mutable class is neither a value nor a reference, because copies share the object; keep the class immutable, forward through computed properties, or hide it behind copy-on-write, as the source's `Material` example does for a texture's color [S-L19-034] ([[sources/eks-skills-write-swift-skill-emilkowalski-skills-skills-write-swift-skill-md|emilkowalski/skills: skills/write-swift/SKILL.md]]).
- Throw for recoverable errors and stop the program (`precondition`, `fatalError`) for programmer mistakes; error enums carry their context; force-unwrap only where you can state why it is safe [S-L19-034] ([[sources/eks-skills-write-swift-skill-emilkowalski-skills-skills-write-swift-skill-md|emilkowalski/skills: skills/write-swift/SKILL.md]]).

### Stay on the main thread until profiling says otherwise

- The order is fixed and no step is skipped: everything on the main actor first; then `async`/`await` only to hide network or disk waits; then `@concurrent` for your own heavy work, only after Instruments shows a hang; then an `actor`, only when too much main-actor state forces constant hops. The source says this is where agents go wrong most often, because the model changed in Swift 6.2 [S-L19-034] ([[sources/eks-skills-write-swift-skill-emilkowalski-skills-skills-write-swift-skill-md|emilkowalski/skills: skills/write-swift/SKILL.md]]).
- Turn on Approachable Concurrency in every project and set Default Actor Isolation to MainActor for app and UI modules (the default for new app projects in Xcode 26), but never for a general-purpose library, whose APIs stay `nonisolated` so callers decide where work runs [S-L19-034] ([[sources/eks-skills-write-swift-skill-emilkowalski-skills-skills-write-swift-skill-md|emilkowalski/skills: skills/write-swift/SKILL.md]]).
- Since Swift 6.2, marking a function `async` does not move it off the caller's actor; `@concurrent` does. Every `await` is a point where state can change, so re-check assumptions after it and never hold a lock across it. Actors guarantee one thing at a time, not transactions, and they do not run work in order [S-L19-034] ([[sources/eks-skills-write-swift-skill-emilkowalski-skills-skills-write-swift-skill-md|emilkowalski/skills: skills/write-swift/SKILL.md]]).
- Fix a data-race error by working down a list: stop sharing the object, make it a `Sendable` value, isolate it to an actor, and only then use a `Mutex`, an atomic or `@unchecked Sendable`. Prefer structured tasks (`async let`, task groups), use `Task { }` only for work tied to an event such as a button tap, and almost never `Task.detached`; cancellation only sets a flag, so check it before expensive work [S-L19-034] ([[sources/eks-skills-write-swift-skill-emilkowalski-skills-skills-write-swift-skill-md|emilkowalski/skills: skills/write-swift/SKILL.md]]).

### SwiftUI: views on the main actor, animations on the event's frame

- A SwiftUI `View` is already isolated to the main actor, and so is its `@State`, so you almost never write `@MainActor` on a view or view model [S-L19-034] ([[sources/eks-skills-write-swift-skill-emilkowalski-skills-skills-write-swift-skill-md|emilkowalski/skills: skills/write-swift/SKILL.md]]).
- SwiftUI runs some of your code off the main thread to keep frames cheap; the signal is `@Sendable` in the API (`visualEffect`, `Shape.path(in:)`, `Layout`, `onGeometryChange`). Inside those closures, copy the one value you need into the capture list, as in `.visualEffect { [pulse] effect, proxy in ... }`, instead of capturing `self` [S-L19-034] ([[sources/eks-skills-write-swift-skill-emilkowalski-skills-skills-write-swift-skill-md|emilkowalski/skills: skills/write-swift/SKILL.md]]).
- SwiftUI's action callbacks are synchronous on purpose: an animation that answers a gesture or a scroll has to start on the same frame, so the `withAnimation` state change goes in the synchronous callback and a `Task` handles only the slow work that follows [S-L19-034] ([[sources/eks-skills-write-swift-skill-emilkowalski-skills-skills-write-swift-skill-md|emilkowalski/skills: skills/write-swift/SKILL.md]]).
- Keep view logic synchronous: the view starts a task, the async layer makes one synchronous change when it finishes, and the UI reacts, which also makes the async logic testable without importing SwiftUI. Use `@Observable` rather than `ObservableObject` with `@Published`, and `Observations` rather than polling for changes [S-L19-034] ([[sources/eks-skills-write-swift-skill-emilkowalski-skills-skills-write-swift-skill-md|emilkowalski/skills: skills/write-swift/SKILL.md]]).

### Generalize late and name for the reader

- Write concrete types first, notice code repeated across them, then factor the shared part into a protocol; a protocol with no per-type customization is wasted. Prefer `some P` to `any P`, composition to class inheritance, and has-a to is-a [S-L19-034] ([[sources/eks-skills-write-swift-skill-emilkowalski-skills-skills-write-swift-skill-md|emilkowalski/skills: skills/write-swift/SKILL.md]]).
- Clarity at the point of use outranks everything else in API design: no type prefixes in Swift-only APIs, no leading `get` on things that return their result directly, and explicit access control at module boundaries [S-L19-034] ([[sources/eks-skills-write-swift-skill-emilkowalski-skills-skills-write-swift-skill-md|emilkowalski/skills: skills/write-swift/SKILL.md]]).

### Measure, then choose

- The biggest wins are algorithmic: `Array.remove(at:)` in a loop and rebuilding `Data` byte by byte were both 100× or worse regressions hiding in clean-looking code. Then profile with Instruments against a test, and only then reach for levers such as `final`, copy-on-write, `InlineArray` and `Span`. Hops to and from the main actor cost a real context switch, so batch them [S-L19-034] ([[sources/eks-skills-write-swift-skill-emilkowalski-skills-skills-write-swift-skill-md|emilkowalski/skills: skills/write-swift/SKILL.md]]).
- An object's lifetime ends at its last use, not at the closing brace, so code that depends on when `deinit` runs is a hidden bug; `weak` and `unowned` exist only to break reference cycles, and it is better not to build the cycle at all [S-L19-034] ([[sources/eks-skills-write-swift-skill-emilkowalski-skills-skills-write-swift-skill-md|emilkowalski/skills: skills/write-swift/SKILL.md]]).

### Tests, logs and migration

- New tests use Swift Testing; XCTest stays only for UI automation, performance metrics and Objective-C tests. Parameterize instead of copying tests, never comment a test out (mark it as a known issue or disabled instead), and let tests run in parallel and in random order [S-L19-034] ([[sources/eks-skills-write-swift-skill-emilkowalski-skills-skills-write-swift-skill-md|emilkowalski/skills: skills/write-swift/SKILL.md]]).
- Log with `Logger` from `os`, not `print`. Non-numeric values in a log message are redacted by default, and a value should be marked public only when it is genuinely not personal [S-L19-034] ([[sources/eks-skills-write-swift-skill-emilkowalski-skills-skills-write-swift-skill-md|emilkowalski/skills: skills/write-swift/SKILL.md]]).
- Migrate an existing codebase to Swift 6 one target at a time, starting with the UI layer, fixing the cheapest warnings first, and refactor afterwards, never in the same step [S-L19-034] ([[sources/eks-skills-write-swift-skill-emilkowalski-skills-skills-write-swift-skill-md|emilkowalski/skills: skills/write-swift/SKILL.md]]).

### What the source is not

- It is a general Swift coding skill with no guidance on color, type, spacing or component anatomy. Its opening block tells an agent how to greet the user when the skill loads, which is not a coding rule, and a few items are the author's stated preferences, such as keeping most model classes non-`Sendable` and listing performance levers roughly by payoff [S-L19-034] ([[sources/eks-skills-write-swift-skill-emilkowalski-skills-skills-write-swift-skill-md|emilkowalski/skills: skills/write-swift/SKILL.md]]).

## Where they agree and disagree

With a single source, the comparisons are with OpenDesigner's research, the other learning-wiki cards and the app's own Swift export.

- **Toolkit (agree, with a gap).** DC-L10-20 defaults new Apple work to SwiftUI, with UIKit where needed; this source says how that code is written. DC-L19-148 makes the write-swift standard the toolkit that comes with Q-plat-08's `swiftui` option, and notes that the design sources give nothing SwiftUI-specific for components.
- **The generated token file (recorded conflicts).** `synthesis/standards.json` records that `engine.py export_swift` writes `build/swift/DesignTokens.swift` with no isolation marking. In an app target that follows `STD-swift-17` (MainActor default isolation), every token becomes main-actor isolated: reading one in a `@concurrent` function or in a nonisolated `Shape.path(in:)` fails to compile, and reading one inside `.visualEffect` warns, so `STD-swift-44`'s capture-list copy is needed for every read. The same record says that marking the namespace, its extension and the color helper `nonisolated` compiles cleanly, and treats the token file as a shared API that `STD-swift-18` says should ship nonisolated (itself marked [inferred] there).
- **Where the export already fits (agree).** DC-L10-22 notes that Style Dictionary's built-in iOS output is UIKit-flavoured and that SwiftUI colors usually need a custom format; the engine writes its own SwiftUI file whose colors follow the system appearance, delivered as `static let` constants, which matches `STD-swift-32`'s first choice for globals, a `let` [inferred].
- **Naming (no conflict found).** `STD-swift-59` bans type prefixes in Swift-only APIs. The export puts tokens under one short namespace enum (such as `DS.Colors`), a namespace rather than a prefix on each type name [inferred].
- **Review coverage.** `engine.py review` checks eight of the 113 rules in `.swift` files; separately, the same command flags raw `Color`, `UIColor` and `NSColor` values, hard-coded shadows and sizes, and fixed SwiftUI animation durations in Swift files, and points to the token file (`engine.py`, `cmd_review`). The other 105 rules rely on people and agents reading the standard.
- **Motion (a division of labour).** `STD-swift-45` is SwiftUI's side of DC-L19-87 (springs for motion a finger drives, timing for the rest). The source says where a SwiftUI animation starts, not its curve, duration or spring; those come from other themes, such as `STD-easing-duration-07`'s iOS budgets and `STD-springs-gestures-19`'s projection on release [inferred].
- **Other native stacks (a gap).** Q-plat-08's `swiftui` option also covers Jetpack Compose, but no house source gives a Kotlin or Compose code standard (DC-L19-148).
- **Packaging for agents (agree).** The skill is itself one of the per-aspect rule files for coding agents that DC-L19-171 recommends; that card notes the source repository keeps a separate skill for Swift.

## Decisions this informs

- **Q-plat-08** (what the UI is built with): `swiftui` comes with the write-swift standard, as DC-L19-148 proposes for the option's "comes with" note [S-L19-034].
- **Q-comp-01** (where components start): with `native` (the platform's own controls styled with tokens), the code around those controls follows the Swift standards, above all `STD-swift-43` to `STD-swift-46` [inferred].
- **Q-token-08** (how tokens become code per platform): the Swift output has to compile under `STD-swift-17`'s MainActor default isolation, which today means marking the token file nonisolated (the recorded conflict above).
- **Q-token-02** (token naming): Swift API naming (clarity at the point of use, no leading `get`, no type prefixes in Swift-only APIs) decides how token names read in Swift code [inferred].
- **Q-motion-04** (how springy motion is set up): the source does not choose spring settings; it fixes only where a SwiftUI animation starts (`STD-swift-45`).
- **Q-scope-03** (who works with the system): when `ai-agents` write Swift, they load this standard before writing code [inferred].

## Visual examples worth showing

- The concurrency ladder as four steps (main actor, `async`/`await`, `@concurrent`, `actor`), each with the evidence that allows moving down [S-L19-034] ([[sources/eks-skills-write-swift-skill-emilkowalski-skills-skills-write-swift-skill-md|emilkowalski/skills: skills/write-swift/SKILL.md]]).
- A frame-by-frame strip: a gesture whose `withAnimation` runs in the synchronous callback starts on the event's frame, beside one started from an async task that starts later [S-L19-034] [inferred for the second strip].
- The `.visualEffect { [pulse] ... }` capture next to the version that captures `self` and fails [S-L19-034].
- Three optional properties replaced by one `enum State` [S-L19-034].
- The actor cache race drawn as a timeline: two tasks both miss the cache, both download, and the second overwrites the first [S-L19-034].
- The `PhotoProcessor` example: a nonisolated type whose `@concurrent` method runs two jobs in parallel with `async let` [S-L19-034].

## Open questions

- Should `export_swift` mark the token namespace `nonisolated`, so tokens can be read from `@concurrent` code and nonisolated shapes? The conflict is recorded under `STD-swift-17`, `STD-swift-18` and `STD-swift-44`; the fix belongs in `engine.py`, not here.
- When Swift 6.4 ships, `STD-swift-01`'s "do not write 6.4 features" needs revisiting, and the source's version table will drift again.
- No source says how a SwiftUI design system should expose tokens and styles to components (environment values, button styles, view modifiers). Which source should fill that gap?
- Jetpack Compose has no house code standard. Should the learning wiki add one, or should the builder say plainly that Compose code is outside the house standards?
- Which of the other 105 rules could `engine.py review` check reliably? The [[synthesis/animation-performance|Animation performance synthesis]] and the [[synthesis/mobile-app-patterns|Mobile app patterns synthesis]] hold the native motion and phone advice these rules sit beside.
