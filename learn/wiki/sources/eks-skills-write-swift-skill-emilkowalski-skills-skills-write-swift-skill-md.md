---
type: source
title: "emilkowalski/skills: skills/write-swift/SKILL.md"
created: 2026-09-27
updated: 2026-09-27
video_id: eks-skills-write-swift-skill
url: https://github.com/emilkowalski/skills/blob/85e8e23/skills/write-swift/SKILL.md
channel: emilkowalski/skills (GitHub, MIT)
published: commit 85e8e23
authority: non-negotiable
tags:
  - swift
  - swiftui
  - swift-6
  - concurrency
  - value-types
  - generics
  - api-design
  - performance
  - arc
  - swift-testing
  - macros
  - logging
---

# emilkowalski/skills: skills/write-swift/SKILL.md

## Metadata

- Video ID: `eks-skills-write-swift-skill`
- Channel: emilkowalski/skills (GitHub, MIT)
- Published: commit 85e8e23
- URL: https://github.com/emilkowalski/skills/blob/85e8e23/skills/write-swift/SKILL.md

## Summary

A coding skill for writing modern Swift (current through Swift 6.4, baseline 6.3) the way the language wants to be written. Its through-line is progressive disclosure: start with value types, concrete types, some-generics and single-threaded main-actor code, and add concurrency, references, existentials or unsafe pointers only for a reason you can state. It covers Swift 6.2 concurrency (async stays on the caller's actor, @concurrent for heavy work, actors, Sendable, structured tasks), SwiftUI isolation, protocols and generics, API naming, performance and ARC, Swift Testing, macros, logging, unsafe code, modern syntax and a target-by-target Swift 6 migration. For a design system it sets the engineering standard for any Swift/SwiftUI component code, including keeping gesture-driven animations on the event's frame [inferred].

## Key Ideas

- Swift rewards progressive disclosure: start static, single-threaded and value-based, and add dynamism only with a stated reason.
- struct and enum are the default; class is for identity, sharing, inheritance or resource lifetime.
- Enums with one State value make invalid combinations unrepresentable.
- Since Swift 6.2 async does not leave the caller's actor; @concurrent is how your own heavy work moves off the main thread.
- Concurrency goes main actor, then async/await, then @concurrent, then actor, never skipping a step: async/await only to hide latency, @concurrent only after Instruments shows a hang, actor only when main-actor state forces constant hops.
- Apps default to MainActor isolation; libraries ship nonisolated APIs.
- Most data-race errors are fixed by not sharing the object, not by @unchecked Sendable.
- Prefer structured tasks; Task { } only for work whose lifetime doesn't fit a scope (a UI event, a delegate callback), and Task.detached almost never.
- SwiftUI animation starts must happen synchronously on the event's frame.
- Generalize late: concrete types first, protocols only once code repeats, some before any.
- Performance work starts with algorithms, then Instruments against a test, then levers such as final, copy-on-write, InlineArray and Span.
- Never depend on deinit timing; break cycles by restructuring into a tree.
- New tests use Swift Testing; XCTest only for its three remaining uses.
- Migrate to Swift 6 one target at a time, UI layer first, and never mix it with refactoring.

## Entities

- [[entities/emil-kowalski|Emil Kowalski]] (person): Owner of the emilkowalski/skills repository that publishes this skill [inferred from the repo name]
- [[entities/write-swift|write-swift]] (tool): The agent skill itself: modern Swift guidance current through Swift 6.4
- [[entities/swift|Swift]] (product): The programming language the skill covers; baseline 6.3, concurrency model 6.2
- [[entities/swiftui|SwiftUI]] (library): Apple UI framework whose views are @MainActor-isolated and whose callbacks are synchronous on purpose
- [[entities/xcode|Xcode]] (tool): IDE providing build settings such as Approachable Concurrency, Default Actor Isolation and Optimize Object Lifetimes
- [[entities/instruments|Instruments]] (tool): Profiler (Time Profiler, Allocations, hangs, Swift Concurrency template) to run before offloading or optimizing
- [[entities/swift-testing|Swift Testing]] (library): Default test framework: @Test, #expect, #require, traits, parameterized and exit tests
- [[entities/xctest|XCTest]] (library): Older test framework kept only for UI automation, performance metrics and Objective-C tests
- [[entities/approachable-concurrency|Approachable Concurrency]] (concept): Build setting to enable in every project
- [[entities/default-actor-isolation|Default Actor Isolation]] (concept): Build setting set to MainActor for app and UI modules
- [[entities/sendable|Sendable]] (concept): Marks a type safe to share across isolation domains
- [[entities/copy-on-write|Copy-on-write]] (concept): Technique for out-of-line storage with value semantics
- [[entities/noncopyable-types-copyable|Noncopyable types (~Copyable)]] (concept): Express unique ownership with compile-time checks
- [[entities/synchronization-module|Synchronization module]] (library): Provides Mutex and Atomic, a late option for data races
- [[entities/inlinearray-span|InlineArray / Span]] (concept): Swift 6.2 fixed-size inline storage and safe contiguous-memory access
- [[entities/logger-os|Logger (os)]] (library): Structured logging to use instead of print
- [[entities/subprocess|Subprocess]] (library): Package replacing Process plus pipes for scripting
- [[entities/swift-regex-regexbuilder|Swift Regex / RegexBuilder]] (library): Regex literals and builder replacing hand-rolled string index math
- [[entities/lldb|LLDB]] (tool): Debugger that steps through await and shows task info
- [[entities/address-sanitizer|Address Sanitizer]] (tool): Run when unsafe pointers are unavoidable

## Topics

- [[topics/native-implementation-swift-and-swiftui|Native implementation (Swift and SwiftUI)]]: How to write the Swift code behind an iOS or macOS design system: value types, Swift 6.2+ concurrency (main actor first, @concurrent, actors), Sendable, structured tasks, SwiftUI isolation, generics, API naming, performance, ARC, Swift Testing, macros, logging and Swift 6 migration.
- [[topics/animation-performance|Animation performance]]: In SwiftUI, start animations with a withAnimation state change in the synchronous callback on the same frame as the gesture or scroll event; SwiftUI runs @Sendable closures such as visualEffect off the main thread to keep frames cheap, so copy values into their capture list.

## Notable Claims

- In Swift 6.2, marking a function async does not move it off the current actor; it runs where it was called from. Evidence: The rule that changed
- @concurrent always switches to the concurrent thread pool; nonisolated runs wherever it is called from. Evidence: The rule that changed
- Main-actor default isolation is the default for new app projects in Xcode 26. Evidence: Turn on the right build settings first
- Array, String and Dictionary use copy-on-write to combine out-of-line storage with value semantics. Evidence: Copy-on-write is how you get out-of-line storage
- throws is throws(any Error) and non-throwing is throws(Never), which lets map abstract over both. Evidence: Typed throws
- Actors guarantee mutual exclusion, not transactions, and are not FIFO: they run highest-priority work first to avoid priority inversion. Evidence: Actor reentrancy
- Value types are Sendable when their storage is, inferred automatically for non-public types; public types never get inferred sendability. Evidence: 4. Sendable and sharing data
- Actors and @MainActor classes are implicitly Sendable. Evidence: 4. Sendable and sharing data
- Globals in Swift are initialized lazily and atomically, unlike C. Evidence: Global and static variables
- Structured tasks inherit cancellation, priority and task-local values; Task.detached inherits nothing. Evidence: 5. Structured concurrency
- Cancelling a task sets a flag and stops nothing. Evidence: Cancellation is cooperative
- Never resuming a continuation hangs the caller forever; resuming twice is a fatal error. Evidence: Bridging callbacks
- SwiftUI View is @MainActor-isolated, including @State; APIs marked @Sendable (visualEffect, Shape.path(in:), Layout, onGeometryChange) may run off the main thread. Evidence: 6. Concurrency in SwiftUI
- A method only in a protocol extension is statically dispatched, so a conformer's version shadows rather than overrides it. Evidence: A protocol requirement is a customization point
- Heap allocation is expensive (search plus locking), stack allocation is cheap (one subtraction), and global allocation is free. Evidence: Allocation — global (free)
- Chained map/flatMap/filter allocate an array per stage. Evidence: Elegant ≠ fast
- Async functions keep their state on a per-task slab allocator and split into partial functions at each suspension point, with slightly higher call overhead than sync functions. Evidence: Async functions keep their state
- Hops to and from the main actor cost a real context switch. Evidence: Hops to and from the main actor
- An object's guaranteed lifetime ends at its last use, not at the closing brace. Evidence: 10. ARC and object lifetime
- Swift Testing creates a fresh suite instance per test and runs tests in parallel in randomized order by default. Evidence: Suites are `struct`s; Tests run in parallel by default
- Macros are type-checked before expansion, so misuse is an error at the call site. Evidence: 12. Macros
- Logger messages are stored in an optimized form and rendered only when displayed; non-numeric interpolations are redacted by default. Evidence: 13. Logging and debugging
- 'Unsafe' means the API cannot fully validate input, so violating preconditions is undefined behavior rather than a crash. Evidence: 14. Unsafe code and interop
- A Swift 6 migration produces hundreds of warnings from a handful of root causes; a single line can clear dozens. Evidence: Fix the warnings, cheapest first
- You can turn strict checking back off and ship; every fix made is a genuine improvement that survives. Evidence: You can turn strict checking back off
- @Test works on any function (global, static or instance); async, throws and global-actor-isolated functions all work. Evidence: on any function
- Expanded macro code is ordinary Swift: inspectable (Expand Macro), debuggable and steppable. Evidence: Expanded code is ordinary Swift
- Safe APIs trap deliberately; a clean fatal error is the safe outcome. Evidence: trap deliberately
- C, Objective-C and C++ types map into Swift directly, including C++ value semantics, containers as Swift collections and move-only types as ~Copyable. Evidence: Interop is bidirectional and incremental
- The debug log level is never persisted and is fastest, its message construction optimized away when not streaming; notice is the default level and fault is the most persistent and slowest. Evidence: Levels control persistence and cost
- Starting a Swift 6 migration with the UI/app layer gives a high fix rate because much of it is already main-actor-annotated by the SDK. Evidence: much of it is already main-actor-annotated by the SDK

## Quotes

> Swift is a progressive-disclosure language.
> Actors guarantee mutual exclusion, not transactions.
> Cancellation is cooperative. Cancelling sets a flag; it stops nothing.

<!-- od:learn -->

## For OpenDesigner

- Authority: **non-negotiable**
- Caveat: This is a general Swift coding skill, not visual design guidance; it matters to OpenDesigner only for projects that ship SwiftUI/Swift code (for example the Swift export target) [inferred].
- Caveat: applies_to 'ios' is used as the nearest available value; the rules apply to Swift code on any Apple platform. Exit tests are the exception: the source says they run on macOS, Linux, FreeBSD and Windows only, so that rule is marked 'desktop'.
- Caveat: Version-dated: the baseline is Swift 6.3 as of August 2026; rows marked with the warning sign are unreleased Swift 6.4 and must be re-checked against the project's toolchain.
- Caveat: Test framework interoperability (ST-0021) availability depends on the Xcode version, per the source.
- Caveat: The 'Initial Response' block is an instruction for how the agent greets the user when the skill loads, not a design or coding rule.
- Caveat: Several items are the author's stated preferences (e.g. keeping most model classes non-Sendable, the order of levers 'roughly in order of what they buy') rather than compiler-enforced facts.

### Rules and practices

- **must** (process, ios): Check the project's Swift toolchain before applying this guidance: treat Swift 6.3 as the baseline, treat rows marked with the warning sign as unreleased Swift 6.4, and do not apply the Swift 6.2 rules about async and @concurrent to projects on Swift 6.1 or earlier. Why: Everything compiles on 6.3 unless marked; the concurrency guidance assumes the Swift 6.2 model. Values: Swift 6.3, Swift 6.4, Swift 6.2, 6.1 or earlier. [Toolchain baseline: Swift 6.3]
- **must** (process, ios): Start with the simplest, most static, most single-threaded thing that works, and add concurrency, reference semantics, existentials or unsafe pointers only where you can point at the reason. Why: Swift is a progressive-disclosure language; every other rule applies this one. [The through-line]
- **must** (process, ios): Move down the hierarchy of defaults only with a reason you can state: data starts as struct/enum, abstraction as a concrete type, polymorphism as some P, execution on the main actor synchronously, memory as Array/String, safety as a safe API. Why: Each level down buys dynamism at a cost; the table lists the only reasons to move. Values: struct / enum, concrete type, some P, main actor, synchronous, Array, String, safe API. [Model this hierarchy of defaults]
- **must** (platforms, ios): Keep Array and String for memory until profiling shows the cost; only then reach for InlineArray or Span. Why: Hierarchy of defaults: move down a level only with a reason you can state (Memory row: profiling shows the cost). Values: Array, String, InlineArray, Span. [Memory | `Array`, `String`]
- **must** (platforms, ios): Use safe APIs by default; use Unsafe* only for C interop or a measured hot path. Why: Hierarchy of defaults: Safety row. Values: Unsafe*. [Safety | safe API]
- **must** (platforms, ios): Default to struct and enum; use class only for identity, shared mutable state, inheritance or resource lifetime. Why: Value types are the default in Swift; a window or database connection has identity, a Point or Material does not. Values: struct, enum, class. [1. Model data with value types]
- **must** (platforms, ios): Declare with let by default and use var only when you mutate. Why: Same discipline as some before any and value before reference: start narrow, widen with cause. Values: let, var. [`let` by default]
- **must** (platforms, ios): Do not leave a struct with a mutable reference-type property as is: keep the referenced type immutable, expose only computed properties that forward to it, or make it a private stored property behind copy-on-write. Why: Such a struct is neither a value nor a reference: copies share the object and mutations leak across copies. [A struct with a mutable reference-type property]
- **should** (platforms, ios): Implement copy-on-write by wrapping a final class in a struct and checking isKnownUniquelyReferenced(&storage) before mutating, copying first if it is not unique. Why: It gives out-of-line storage and value semantics; Array, String and Dictionary work this way. Values: isKnownUniquelyReferenced(&storage), final class. [Copy-on-write is how you get out-of-line storage]
- **must** (platforms, ios): Model a fixed set of things and mutually exclusive state with an enum; replace piles of optional stored properties (isSharing, selectedRows, shareTarget) with one enum State. Why: It makes invalid combinations unrepresentable and state change atomic instead of a sequence of writes you can forget to finish. Values: enum State. [Enums are the tool for "a fixed set of things"]
- **should** (platforms, ios): Compose structs from value-type stored properties so the whole type has value semantics. Why: That makes undo, diffing and state restoration a single code path instead of one per property. [Composing values yields a value]
- **should** (platforms, ios): Use noncopyable types (~Copyable) for unique ownership such as a file descriptor, a bank transfer or an open resource, and mark the finishing method consuming. Why: Suppressing the copy turns 'you must not run this twice' into a compile error and makes deinit on a struct meaningful; consuming lets the compiler prove it is the last use. Values: ~Copyable, consuming. [Noncopyable types]
- **consider** (platforms, ios): Make parameter ownership explicit: borrowing for read-only (the default), consuming to take it away, inout/mutating for temporary write access. Why: Ownership becomes explicit with noncopyable types. Values: borrowing, consuming, inout, mutating. [Parameter ownership becomes explicit]
- **must** (platforms, ios): Throw for recoverable errors; use precondition or fatalError for programmer mistakes. Why: A failed network call keeps the program running; an out-of-bounds index means the code is wrong and must halt before the bug becomes a security issue. Values: throw, precondition, fatalError. [Recoverable → `throw`. Programmer mistake]
- **should** (platforms, ios): Make error types enums with associated values that carry context, e.g. case duplicateFriend(String) rather than case duplicateFriend. Why: The context is the whole point of the error. Values: case duplicateFriend(String). [Enums with associated values make the best error types]
- **should** (platforms, ios): Use guard for error conditions and if let for the ordinary unwrap. Why: guard forces the exit path. Values: guard, if let. [`guard` for error conditions]
- **should** (platforms, ios): Use typed throws (throws(MyError)) only for internal functions, error-forwarding generic code and constrained environments; use untyped throws for public API. Why: Boxing any Error can be too costly in constrained environments, while untyped throws preserves freedom to change a public error type later. Values: throws(MyError), throws, throws(any Error), throws(Never). [Typed throws]
- **must** (platforms, ios): Force-unwrap only where you can state the invariant, and prefer a failing #require or precondition with a message over a bare !. Why: The section's aim is to make failure paths visible; a failing #require or precondition with a message does that, a bare ! does not [inferred]. Values: #require, precondition, !. [Force-unwrap only where you can state the invariant]
- **must** (platforms, ios): Start every app entirely on the main thread. Why: Single-threaded code goes a long way, and most apps never need to leave it. [Start every app entirely on the main thread]
- **must** (process, ios): Add concurrency in this order without skipping steps: single-threaded on the main actor; async/await to hide latency; @concurrent for your expensive work only after Instruments shows a hang; actor only when too much main-actor state forces tasks to hop back constantly. Why: This is where agents go wrong most often because the model changed in Swift 6.2. Values: async/await, @concurrent, actor, URLSession.data(from:). [The progression, in order. Do not skip steps.]
- **must** (tooling, ios): Enable the Approachable Concurrency build setting in every project. Why: It dramatically reduces the number of errors you will see. Values: Approachable Concurrency. [Turn on the right build settings first]
- **must** (tooling, ios): For app and UI-facing modules set Default Actor Isolation to MainActor; in a package use swiftSettings: [.defaultIsolation(MainActor.self)]. Why: It is the default for new app projects in Xcode 26 and deletes most @MainActor annotations. Values: Default Actor Isolation, MainActor, swiftSettings: [.defaultIsolation(MainActor.self)], Xcode 26. [Default Actor Isolation]
- **must** (tooling, ios): Do not set main-actor-by-default for a general-purpose library; ship nonisolated APIs and let clients decide where work runs. Why: The caller should decide where library work runs. Values: nonisolated. [Do not set main-actor-by-default for a general-purpose library]
- **must** (platforms, ios): Do not rely on async to move work off the current actor; mark your own CPU-heavy functions @concurrent to switch to the concurrent thread pool. Why: In Swift 6.2 an async function runs where it was called from. Values: @concurrent, Swift 6.2. [The rule that changed]
- **should** (platforms, ios): Use nonisolated as the default isolation for library APIs, not @MainActor or @concurrent; nonisolated on a type makes all its members nonisolated (Swift 6.1+). Why: nonisolated runs wherever it is called from, so the caller decides. Values: nonisolated, @MainActor, @concurrent, Swift 6.1+. [`nonisolated` — runs wherever it's called from]
- **must** (process, ios): Profile with Instruments (Time Profiler, hangs) before offloading work, and make code faster without concurrency first whenever possible. Why: Concurrency has real cost: task allocation, scheduling and reasoning. Values: Time Profiler, hangs. [Profile before you offload]
- **must** (platforms, ios): Do not spawn a task for trivial work such as reading a UserDefaults value. Why: A child task for that costs more than it saves. Values: UserDefaults. [Don't spawn a task for trivial work]
- **should** (platforms, ios): Use one task per end-to-end operation: put work that must happen in order in one task and give independent operations separate tasks. Why: The runtime can then interleave independent operations. [One task per end-to-end operation]
- **must** (platforms, ios): Re-check assumptions after every await, never hold a lock across an await, and never rely on thread-local storage across one. Why: await is a suspension point that breaks atomicity; state can change and you may resume on a different thread. Values: await. [`await` is a suspension point, and it breaks atomicity]
- **must** (platforms, ios): Mutate actor state in synchronous methods. Why: Synchronous code on an actor runs to completion uninterrupted; that is the transaction boundary. [Mutate actor state in synchronous methods]
- **should** (platforms, ios): Keep async actor methods thin, composed of synchronous transactional operations, and leave the actor consistent at every await. Why: Actors guarantee mutual exclusion, not transactions; other work runs between awaits. [Keep async actor methods thin]
- **must** (platforms, ios): After awaiting a download inside an actor, re-check the cache before writing it, or dedupe the in-flight work. Why: Otherwise two tasks both miss, both download, and the second clobbers the first. [The classic bug: check cache]
- **must** (platforms, ios): Do not use an actor to guarantee ordering; use a task or an AsyncStream. Why: Actors are not FIFO; they run highest-priority work first to avoid priority inversion. Values: AsyncStream. [Actors are not FIFO]
- **should** (platforms, ios): Use an actor or a @MainActor class for shared mutable state, not a class plus a lock you must remember. Why: Quick Reference: shared mutable state row. Values: actor, @MainActor. [Shared mutable state | `actor`, or `@MainActor` class]
- **must** (platforms, ios): Move work off the main thread with a @concurrent async function, not Task.detached or DispatchQueue.global(). Why: Quick Reference: move work off the main thread row. Values: @concurrent func … async, Task.detached, DispatchQueue.global(). [Move work off the main thread]
- **must** (platforms, ios): Never use a blocking primitive such as DispatchSemaphore or NSCondition across an await; restructure instead. Why: Quick Reference: blocking primitive across await row. Values: DispatchSemaphore, NSCondition. [Blocking primitive across `await`]
- **must** (platforms, ios): Write Sendable explicitly on public types that should be shareable. Why: Public types never get inferred sendability; marking one Sendable is a promise to clients. Values: Sendable. [Public types never get inferred sendability]
- **should** (platforms, ios): Keep most model classes neither @MainActor nor Sendable (a shared model class is non-Sendable or @MainActor, never Sendable plus manual locking); if one must leave the main actor, make it nonisolated rather than Sendable. Why: Non-Sendable on purpose prevents half the model being mutated on the main thread while the other half is mutated in the background. Values: nonisolated, @MainActor, Sendable. [Most model classes should be neither]
- **must** (platforms, ios): When sending a non-Sendable object to another isolation domain, make all mutations before the hand-off and do not touch it afterwards. Why: Sending is allowed as long as the sender stops using it; touching it afterwards is the error. [You can still _send_ a non-`Sendable` object]
- **should** (platforms, ios): Mark a function type @Sendable only if it genuinely crosses isolation domains. Why: Closures capture state too. Values: @Sendable. [Closures capture state too]
- **must** (platforms, ios): Reserve @unchecked Sendable for types with real internal synchronization (a Mutex or a lock), and use nonisolated(unsafe) on a global only as a last resort, never to silence a warning. Why: Both are promises the compiler cannot check. Values: @unchecked Sendable, Mutex, nonisolated(unsafe). [`@unchecked Sendable` is a promise the compiler can't check]
- **must** (process, ios): Fix a data-race error in this order: stop sharing (move the object into a local per job); make it a Sendable value type; isolate it to an actor; only then use Mutex/Atomic from the Synchronization module (in let properties) or @unchecked Sendable. Why: Not sharing fixes the overwhelming majority of real errors. Values: Mutex, Atomic, Synchronization, @unchecked Sendable. [When you hit a data-race error, work down this list]
- **should** (platforms, ios): Fix global and static variables in this order of preference: make it a let; put it on @MainActor; wrap it in a Mutex; nonisolated(unsafe). Why: Globals and statics are the most common source of errors. Values: let, @MainActor, Mutex, nonisolated(unsafe). [Global and static variables are the most common source of errors]
- **should** (platforms, ios): Bridge old callback APIs by annotating delegate protocols you own with @MainActor; for ones you do not own, mark the method nonisolated and use MainActor.assumeIsolated { } (or @preconcurrency on the conformance). Why: assumeIsolated asserts rather than hopping, so it traps loudly instead of racing silently. Values: @MainActor, nonisolated, MainActor.assumeIsolated { }, @preconcurrency. [Bridging old callback APIs]
- **consider** (platforms, ios): Use @preconcurrency import only to temporarily silence sendability warnings from a module that has not migrated. Why: The warnings correctly come back once the module migrates. Values: @preconcurrency import. [Use `@preconcurrency import` to temporarily silence]
- **must** (platforms, ios): Prefer structured tasks (async let, task groups) over unstructured ones. Why: Structured tasks cannot outlive their block, are awaited automatically, and inherit cancellation, priority and task-local values. Values: async let, withTaskGroup. [5. Structured concurrency]
- **should** (platforms, ios): Use async let for a fixed, statically known number of concurrent children, not N unstructured Tasks. Why: Section 5 and Quick Reference. Values: async let. [`async let` for a fixed, statically known number]
- **should** (platforms, ios): Use withTaskGroup when the number of children is dynamic, iterating results as they land. Why: Task groups conform to AsyncSequence. Values: withTaskGroup, AsyncSequence. [`withTaskGroup` when the number is dynamic]
- **should** (platforms, ios): Use withDiscardingTaskGroup when children return nothing, not a withTaskGroup you never drain. Why: It frees each child's resources immediately and cancels siblings on the first error. Values: withDiscardingTaskGroup. [Use withDiscardingTaskGroup when children return nothing]
- **should** (platforms, ios): Use Task { } only when the work's lifetime does not fit a scope (a delegate callback, a button tap, a view appearing): open it inside the synchronous callback rather than making the callback async, and manage its cancellation yourself. Why: It inherits actor isolation and priority, but unstructured tasks give you none of the automatic cancellation, awaiting or scoping of structured tasks. Values: Task { }. [only when the work's lifetime doesn't fit a scope]
- **must** (platforms, ios): Almost never use Task.detached; if you need a detached root, put a task group inside it rather than detaching repeatedly. Why: It inherits nothing: not isolation, not priority, not task-locals. Values: Task.detached. [`Task.detached` almost never]
- **must** (platforms, ios): Check Task.isCancelled or try Task.checkCancellation() before starting expensive work, in synchronous helpers too. Why: Cancellation is cooperative: cancelling sets a flag and stops nothing. Values: Task.isCancelled, try Task.checkCancellation(). [Cancellation is cooperative]
- **must** (platforms, ios): For suspended work such as an AsyncSequence's next(), use withTaskCancellationHandler and protect the state it touches with an atomic or a lock, not an actor. Why: The handler runs immediately and concurrently with the body, and ordering cannot be guaranteed on an actor. Values: withTaskCancellationHandler. [use `withTaskCancellationHandler`]
- **must** (platforms, ios): Bound concurrency: start N children, then add a new one each time one finishes, instead of one child per item over an unbounded list. Why: Unbounded fan-out is listed as the thing not to do. [Bound your concurrency]
- **should** (platforms, ios): Propagate context such as a request ID or trace span with @TaskLocal values, and make them optional. Why: It avoids threading a parameter through every signature; optional gives unbound reads a sensible default. Values: @TaskLocal. [Make them optional so unbound reads have a sensible default]
- **must** (platforms, ios): When bridging callbacks with withCheckedContinuation or withCheckedThrowingContinuation, resume exactly once on every path; for delegate APIs, store the continuation and nil it out when you resume. Why: Never resuming hangs the caller forever; resuming twice is a fatal error. Values: withCheckedContinuation, withCheckedThrowingContinuation. [resume exactly once on every path]
- **should** (platforms, ios): Iterate async sequences with for await / for try await, and adapt handler- or delegate-based APIs with AsyncStream / AsyncThrowingStream: construct the source inside the closure, yield from the handler, clean up in onTermination. Why: That is the adaptation pattern the source gives. Values: for await, for try await, AsyncStream, AsyncThrowingStream, onTermination. [`AsyncSequence`:]
- **should** (platforms, ios): Do not add @MainActor to SwiftUI views or view models (you almost never need it); with main-actor-by-default, delete the ones you have. Why: View is @MainActor-isolated, and so is everything it contains, including @State. Values: @MainActor, @State. [`View` is `@MainActor`-isolated]
- **must** (platforms, ios): Inside SwiftUI closures marked @Sendable (visualEffect, Shape.path(in:), Layout requirements, onGeometryChange), copy the one value you need into the capture list instead of capturing self. Why: SwiftUI deliberately runs these off the main thread to keep frames cheap. Values: visualEffect, Shape.path(in:), Layout, onGeometryChange, [pulse]. [don't send `self` — copy the one value]
- **must** (motion, ios): Start animations for gestures and scroll events with a withAnimation state change inside SwiftUI's synchronous action callback, on the same frame as the event, and open a Task only for the long-running work that follows; do not make the callback async. Why: Time-sensitive UI updates must happen on the same frame as the event; the callbacks are synchronous on purpose. Values: withAnimation, Task { }. [SwiftUI's action callbacks are synchronous on purpose]
- **should** (platforms, ios): Put a piece of state on the seam between UI and async work: the view starts a task, the async layer does a synchronous mutation when it finishes, and the UI reacts. Why: It keeps view logic synchronous and makes async logic testable without importing SwiftUI. [Put a piece of state on the seam]
- **must** (process, ios): Do not start with a class or a protocol: write concrete types, notice repeated code, factor the shared capability into a protocol, then write generic code against it. Why: Overloads with near-identical bodies are the signal that it is time to generalize. [Don't start with a class. **Don't start with a protocol either.**]
- **should** (platforms, ios): Do not create a protocol with no per-type customization; write a constrained extension on an existing protocol instead. Why: Elaborate protocol hierarchies cost compile time and binary size and buy nothing. [A protocol with no per-type customization is a wasted protocol]
- **should** (platforms, ios): Prefer has-a to is-a: if only some of a protocol's operations fit your type, wrap it in a generic struct exposing exactly the API you mean (GeometricVector<Storage: SIMD>, not GeometricVector: SIMD). Why: Refining the protocol would expose operations that do not make sense. Values: GeometricVector<Storage: SIMD>. [Prefer has-a to is-a]
- **must** (platforms, ios): Make anything a conforming type should be able to customize a protocol requirement, not a method only in an extension. Why: Extension-only methods are statically dispatched, so a conformer's version shadows rather than overrides and any P calls the extension's. [A protocol requirement is a customization point]
- **should** (platforms, ios): Compose small values instead of using class inheritance. Why: Inheritance is monolithic, intrusive and leaves unwritten contracts about overriding and calling super. [Composition over inheritance]
- **should** (platforms, ios): Treat a forced downcast as a code smell and look for the lost type relationship. Why: It usually means a type relationship was lost to a class hierarchy or an existential. [A forced downcast is a code smell]
- **must** (platforms, ios): Write some P by default and change to any P only when you need to store arbitrary types (heterogeneous collections, optional underlying type, hiding the abstraction). Why: some keeps every type relationship and lets the compiler specialize; any erases associated types and is opaque to the optimizer. Values: some P, any P. [Write `some P` by default]
- **should** (platforms, ios): To call a method that takes an associated type on an any P, pass the existential into a function taking some P. Why: Erasure works in producing position but not consuming position; the compiler unboxes the existential. Values: any P, some P. [You cannot call a method that takes an associated type]
- **should** (platforms, ios): Use constrained existentials and opaque types (some Collection<Element>) to hide concrete types while exposing the element type, and declare primary associated types on your own protocols only for the type callers supply, not for details like Iterator. Why: They hide LazyFilterSequence<[Animal]> while still exposing the element type. Values: some Collection<Element>, any Collection<any Animal>, protocol Container<Item>. [Constrained existentials and opaque types]
- **should** (platforms, ios): Pin relationships across protocols with same-type requirements in where clauses. Why: Without them 'grow then harvest' does not typecheck and wrong conformances compile. Values: where Self.CropType.FeedType == Self. [Same-type requirements in `where` clauses]
- **should** (platforms, ios): Use [any P] for a heterogeneous collection rather than a class hierarchy. Why: Quick Reference: heterogeneous collection row. Values: [any P]. [| Heterogeneous collection]
- **must** (platforms, ios): Aim API design at clarity at the point of use above every other goal. Why: It is the goal that outranks every other one in API design. [8. API design — clarity at the point of use]
- **should** (platforms, ios): Do not use type prefixes in Swift-only APIs (keep them only where an API mirrors an Objective-C one), and avoid very general names from specific frameworks. Why: Modules disambiguate; general names read badly out of context and force manual disambiguation. [No type prefixes in Swift-only APIs]
- **should** (platforms, ios): Drop a leading get from async alternatives and from anything that returns its result directly (persistentPosts, not getPersistentPosts). Why: Naming convention for clarity at the point of use. Values: persistentPosts, getPersistentPosts. [Drop leading `get`]
- **should** (platforms, ios): Be explicit about access control (private, internal, package, public) at module boundaries. Why: Access control is documentation and forces the sendability and API-evolution decisions. Values: private, internal, package, public. [Access control is documentation]
- **must** (platforms, ios): Design models so illegal states cannot be spelled: private setters plus a validating mutating method, enums for closed sets, a strongly typed UUID instead of a String. Why: Illegal states become impossible to express. Values: UUID. [Design the model so illegal states can't be spelled]
- **consider** (platforms, ios): Use property wrappers to factor out an access policy so the declaration states it in one word, combined with @dynamicMemberLookup on a key path to project through a wrapper. Why: That is how $binding.title works. Values: @Argument, @Published, @dynamicMemberLookup, $binding.title. [Property wrappers]
- **consider** (platforms, ios): Use result builders for declarative DSLs and macros only when the boilerplate is code the compiler could have written. Why: Stated in API design and section 12. [Result builders]
- **must** (process, ios): Do the algorithmic work before micro-optimizing: each time you write a loop, try replacing it with a call to an algorithm. Why: The largest wins are almost never micro-optimizations. [But do the algorithmic work first]
- **must** (platforms, ios): Use removeAll(where:) instead of Array.remove(at:) in a loop, and popFirst() instead of re-slicing a Data per byte. Why: remove(at:) in a loop is O(n²) versus O(n); per-byte re-slicing is O(n²) versus O(1); both were 100×+ regressions. Values: removeAll(where:), O(n), O(n²), popFirst(), O(1), 100×+. [Know the complexity of what you call]
- **should** (platforms, ios): In a hot per-pixel or per-element pipeline, size the output once and write into it instead of chaining map/flatMap/filter. Why: Each chained stage allocates an array; elegant is not fast. Values: map, flatMap, filter. [Chained `map`/`flatMap`/`filter` allocate an array per stage]
- **must** (process, ios): Profile with Instruments' Time Profiler and Allocations run against a test (secondary-click the test's run button, then Profile), and read the signals: platform_memmove means accidental copying, a million transient allocations means intermediate arrays, swift_beginAccess means runtime exclusivity checks, swift_retain/swift_release means reference-counting traffic. Why: It measures exactly the code you care about; decide to optimize with Instruments, not intuition. Values: Time Profiler, Allocations, platform_memmove, swift_beginAccess, swift_retain, swift_release. [Then profile.]
- **should** (platforms, ios): Mark classes you do not intend to subclass final, and use whole-module optimization. Why: final turns dynamic dispatch static and unlocks inlining; WMO can prove it and enables generic specialization. Values: final. [`final` on classes you don't intend to subclass]
- **should** (platforms, ios): Use copy-on-write for large structs with several reference-typed fields that get copied a lot. Why: A large struct with three reference-typed fields costs three retains per copy versus one for a class. Values: three retains. [Struct storage is inline; class storage is out-of-line]
- **consider** (platforms, ios): Give large types stored in an any P indirect storage with copy-on-write so they fit the existential's inline buffer. Why: An existential has a 3-word inline buffer; larger values are heap-allocated per copy. Values: 3-word inline buffer. [An `any P` existential has a 3-word inline buffer]
- **should** (platforms, ios): Prefer a homogeneous [MyModel] over [any Model] unless you need the flexibility. Why: Homogeneous arrays are densely packed, pass type info once and are specializable. Values: [MyModel], [any Model]. [Homogeneous `[MyModel]` beats `[any Model]`]
- **consider** (platforms, ios): Constrain a generic parameter to a class (T: AnyObject) when it is one. Why: It gives the compiler a known representation even without specialization. Values: T: AnyObject. [Constraining a generic parameter to a class]
- **should** (platforms, ios): Use InlineArray<N, T> for fixed-size storage in a hot path, but not if it gets copied or shared. Why: Elements are inline with no heap allocation, reference counting, or uniqueness or exclusivity checks. Values: InlineArray<N, T>, Swift 6.2. [InlineArray<N, T> (Swift 6.2)]
- **must** (platforms, ios): Use Span / RawSpan / OutputSpan (.span, .bytes) instead of withUnsafeBufferPointer for direct access to contiguous storage. Why: They are non-escapable, so you get pointer performance with no lifetime bugs and the retains/releases disappear. Values: Span, RawSpan, OutputSpan, .span, .bytes, withUnsafeBufferPointer, Swift 6.2. [`Span` / `RawSpan` / `OutputSpan`]
- **consider** (platforms, ios): Move stored properties out of a nested class into the parent struct to remove runtime exclusivity checks. Why: Listed as a concrete performance lever. [Moving stored properties out of a nested class]
- **consider** (platforms, ios): Use @inline(always) (paired with final on methods) and @specialized(where T == ...) only when you have measured the need. Why: Shipped in Swift 6.3 for pre-specializing generics for hot concrete types. Values: @inline(always), @specialized(where T == ...), SE-0460, Swift 6.3. [Shipped in Swift 6.3, when you've measured the need]
- **should** (platforms, ios): Do not make a function async if it has nothing to await. Why: Async functions have slightly higher call overhead and split into partial functions at each suspension point. [not to make something `async` that has nothing to await]
- **should** (platforms, ios): Batch hops to and from the main actor: push the loop into functions like loadArticles/updateUI that take arrays instead of hopping twice per iteration. Why: Each hop costs a real context switch. Values: loadArticles, updateUI. [Hops to and from the main actor cost a real context switch]
- **must** (platforms, ios): Do not write code that depends on when a deinit runs. Why: An object's guaranteed lifetime ends at its last use, not the closing brace, and observed lifetimes will change with the optimizer. Values: deinit. [An object's guaranteed lifetime ends at its last use]
- **must** (platforms, ios): Use weak/unowned only to break reference cycles, and do not optional-bind a weak reference that may be read after the strong owner's last use. Why: It may legitimately be nil; optional binding turns a loud crash into a silent wrong answer. Values: weak, unowned. [`weak`/`unowned` are for breaking reference cycles]
- **should** (platforms, ios): Break a reference cycle by not building it: factor the shared data into a third type both sides reference, turning the cycle into a tree. Why: Better than weak. [Better than `weak`: don't build the cycle]
- **should** (platforms, ios): If a cycle cannot be removed, redesign the API so the object is only reachable through a strong reference; treat withExtendedLifetime as a patch, not a design. Why: withExtendedLifetime shifts correctness onto you and spreads through a codebase. Values: withExtendedLifetime. [Next best: redesign the API]
- **must** (platforms, ios): Keep deinit side effects local: use defer at the call site for metrics or global effects and leave deinit for verification. Why: Effects in deinit are sequenced against optimizer decisions. Values: defer, deinit. [Keep `deinit` side effects local]
- **consider** (tooling, ios): Turn on Xcode's Optimize Object Lifetimes build setting to surface lifetime bugs. Why: It shortens observed lifetimes toward the guaranteed minimum. Values: Optimize Object Lifetimes. [Optimize Object Lifetimes]
- **must** (tooling, ios): Write new tests with Swift Testing (@Test + #expect); keep XCTest only for UI automation (XCUIApplication), performance metrics (XCTMetric), and tests written in or catching Objective-C. Why: XCTest remains required for exactly those three things. Values: Swift Testing, @Test, #expect, XCUIApplication, XCTMetric. [11. Testing — Swift Testing by default]
- **should** (tooling, ios): Write #expect with ordinary expressions (#expect(a == b)) instead of XCTAssertEqual-style functions. Why: It captures and displays subexpression values on failure. Values: #expect(a == b), XCTAssertEqual. [`#expect(...)` takes ordinary expressions]
- **should** (tooling, ios): Use try #require(...) to stop a test on failure and to unwrap optionals, instead of continueAfterFailure = false. Why: It lets you choose per expectation. Values: try #require, continueAfterFailure = false. [`try #require(...)`]
- **should** (tooling, ios): Make test suites structs with init for setup; use a class or actor only when you need deinit for teardown, and nest suites to group. Why: A fresh instance per test function means state cannot leak between tests. Values: struct, init, deinit. [Suites are `struct`s]
- **must** (tooling, ios): Parameterize tests with @Test(arguments: [...]) instead of copy-pasting or looping, and use zip() for matched pairs rather than the cross product. Why: Each case runs independently, in parallel, individually re-runnable, with the failing argument named. Values: @Test(arguments: [...]), zip(). [Parameterize instead of copy-pasting or looping]
- **should** (tooling, ios): Express test intent with traits (.enabled(if:), .disabled("reason"), .bug(url), .tags(...), .timeLimit, .serialized) and @available, and never comment a test out. Why: A disabled test still compiles; @available lets the testing library know, unlike a runtime #available check. Values: .enabled(if:), .disabled("reason"), .bug(url), .tags(...), .timeLimit, .serialized, @available, #available. [Traits carry intent]
- **should** (tooling, ios): Wrap a test failing on something outside your control in withKnownIssue { } rather than .disabled or commenting it out. Why: It keeps compiling and running and tells you when the issue is fixed. Values: withKnownIssue { }, .disabled. [`withKnownIssue { }`]
- **should** (tooling, ios): Use confirmation for callbacks that fire N times and withCheckedContinuation for one-shot callbacks with no async overload. Why: Stated testing pattern. Values: confirmation, withCheckedContinuation. [`confirmation` for callbacks]
- **should** (tooling, ios): Keep tests running in parallel and randomized order; refactor hidden inter-test dependencies instead of reaching for .serialized. Why: Parallel randomized runs surface hidden inter-test dependencies. Values: .serialized. [Tests run in parallel by default, in randomized order]
- **consider** (tooling, desktop): Cover precondition/fatalError paths with exit tests: #expect(processExitsWith: .failure) { ... }. Why: They run in an isolated child process; exit tests are available on macOS, Linux, FreeBSD and Windows only. Values: #expect(processExitsWith: .failure), macOS, Linux, FreeBSD, Windows only. [Exit tests]
- **should** (tooling, ios): Migrate tests incrementally with both frameworks in one target, write new tests in Swift Testing today, and set test framework interoperability mode to complete or strict (not limited, never none). Why: Those modes keep cross-framework issues as errors and point at the Issue.record replacement. Values: ST-0021, complete, strict, limited, none, Issue.record. [Test framework interoperability]
- **consider** (tooling, ios): Name tests with raw identifiers, e.g. @Test func `fruits have a tropical climate`(), instead of awkward function names. Why: Modern syntax table, since Swift 6.0. Values: 6.0. [raw identifiers]
- **should** (tooling, ios): Write a macro only when you are writing code the compiler could derive. Why: Reach for a macro only then. [12. Macros]
- **should** (tooling, ios): Test macros as pure syntax-tree transforms with assertMacroExpansion; to learn a node's shape, set a breakpoint in expansion and po the syntax node. Why: It is the fastest loop and avoids bugs in code nobody reads. Values: assertMacroExpansion, po. [Test macros as pure syntax-tree transforms]
- **must** (tooling, ios): Emit real diagnostics when a macro does not apply (throw an error, or context.addDiagnostic for warnings and fix-its); never let a macro silently generate code that will not compile. Why: Misuse should be a clean error at a specific location. Values: context.addDiagnostic. [Emit real diagnostics]
- **must** (tooling, ios): Log with Logger from os, one per subsystem and category, not print. Why: Messages are stored in an optimized form and rendered only when displayed, so logging is cheap enough to leave in. Values: Logger, os, print. [`Logger` from `os`, not `print`]
- **must** (tooling, ios): Opt log values into privacy: .public only when the data is genuinely not personal, and use .private(mask: .hash) to correlate values without exposing them. Why: Non-numeric interpolations are redacted by default. Values: privacy: .public, .private(mask: .hash). [Non-numeric interpolations are redacted by default]
- **should** (tooling, ios): Choose log levels deliberately and log at error or fault for anything you will want in a bug report. Why: Levels control persistence and cost, from debug (never persisted, fastest) to fault (most persistent, slowest). Values: debug, info, notice, error, fault. [Levels control persistence and cost]
- **should** (tooling, ios): Log a correlation ID (a task or request UUID) so a failure's history can be filtered from a device log archive; collect with log collect --device --start ... and filter by subsystem in Console. Why: You can then diagnose without reproducing the failure. Values: log collect --device --start .... [Log a correlation ID]
- **consider** (tooling, ios): Use the format: and align: options in log interpolations. Why: They are free and make logs readable and column-selectable. Values: format:, align:. [`format:` and `align:` are free]
- **must** (platforms, ios): Prefer Span over Unsafe*Pointer and reserve raw pointers for C interop. Why: Since Swift 6.2 there is a safe, non-escaping, equally fast way to reach contiguous storage. Values: Span, Unsafe*Pointer, Swift 6.2. [Prefer `Span` over `Unsafe*Pointer`]
- **must** (platforms, ios): When pointers are unavoidable, keep the unsafe region as small as possible, use buffer pointers (address + count), never let a pointer escape the closure that vends it, and run the Address Sanitizer. Why: Violating an unsafe API's preconditions is undefined behavior, not a crash. [If you must use pointers]
- **should** (tooling, ios): Enable strict memory safety in security-critical modules. Why: It forces every unsafe use to be acknowledged in source, which makes an audit possible. [Enable **strict memory safety**]
- **must** (process, ios): Adopt Swift through interop one file at a time instead of rewriting; use Swift 6.3's @c attribute to expose Swift functions back to C (with @implementation when the declaration already exists in a header). Why: Interop with C, Objective-C and C++ is bidirectional and incremental. Values: @c, @implementation, Swift 6.3. [Adopt Swift one file at a time; don't rewrite]
- **should** (platforms, ios): Use if/switch expressions instead of nested ternaries or an immediately-called closure to initialize a let. Why: Agents routinely write the older, longer form (since 5.9). Values: 5.9. [Nested ternaries]
- **should** (platforms, ios): Use parameter packs (each T, and for over a pack) instead of overloads for 1, 2, 3… arguments. Why: Modern syntax table (since 5.9). Values: each T, 5.9. [parameter packs]
- **should** (platforms, ios): Use @Observable instead of ObservableObject with @Published on every property. Why: Modern syntax table (since 5.9). Values: @Observable, ObservableObject, @Published, 5.9. [`ObservableObject` + `@Published`]
- **should** (platforms, ios): Use Observations { ... } instead of polling an object for changes. Why: It is an AsyncSequence of transactional updates (since 6.2). Values: Observations { ... }, 6.2. [Polling an object for changes]
- **should** (platforms, ios): Use concrete notification types (MainActorMessage / AsyncMessage) instead of NotificationCenter with stringly-typed userInfo. Why: Modern syntax table (since 6.2). Values: MainActorMessage, AsyncMessage, 6.2. [`NotificationCenter` with stringly-typed `userInfo`]
- **should** (tooling, ios): Use the Subprocess package instead of Process plus pipes for scripting, with AsyncBufferSequence.strings() for line-by-line output. Why: Modern syntax table (6.2+; 1.0 lands with 6.4). Values: Subprocess, AsyncBufferSequence.strings(), 6.2+. [the **Subprocess** package]
- **should** (platforms, ios): Use Swift Regex (literals for brevity, RegexBuilder for structure) instead of hand-rolled string index math. Why: Modern syntax table (since 5.7). Values: Swift Regex, RegexBuilder, 5.7. [Hand-rolled string index math]
- **consider** (platforms, ios): Use a module selector (Rocket::SaturnV) when a type shadows a module. Why: Modern syntax table (since 6.3). Values: Rocket::SaturnV, 6.3. [module selector]
- **should** (platforms, ios): Use Swift Binary Parsing (ParserSpan, overflow-checked parsing initializers) instead of manually parsing binary formats with pointers. Why: Modern syntax table (since 6.2). Values: ParserSpan, 6.2. [Swift Binary Parsing]
- **must** (process, ios): Do not write Swift 6.4 features (Task cancellation shield SE-0504, mapKeyedValues, @available(anyAppleOS ...), @diagnose, weak let / ~Sendable, borrow/mutate accessors, UniqueArray/UniqueBox, Ref/MutableRef, the Continuation type) in projects targeting 6.3 or earlier; plan around them but use the older form. Why: Swift 6.4 has not shipped; its proposals are safe to plan around and unsafe to write today. Values: 6.4, SE-0504, mapKeyedValues, @available(anyAppleOS ...), @diagnose, weak let, ~Sendable, borrow/mutate, UniqueArray/UniqueBox, Ref/MutableRef, Continuation. [Rows marked ⚠ are Swift 6.4, which has not shipped]
- **must** (platforms, ios): Never hand-roll date or number parsing inside a regex; compose Swift Regex with Foundation's parsers (.date(...), .currency(...)). Why: Swift Regex parsers compose with Foundation's real parsers. Values: .date(...), .currency(...). [never hand-roll date or number parsing inside a regex]
- **should** (platforms, ios): Make the locale explicit in parsing rather than inheriting the system's. Why: Stated alongside regex parsing guidance. [Make the locale explicit]
- **should** (platforms, ios): Use NegativeLookahead or Local (atomic groups) to stop a regex backtracking across a whole input. Why: Prevents backtracking across the whole input. Values: NegativeLookahead, Local. [use `NegativeLookahead` or `Local`]
- **must** (process, ios): Migrate to Swift 6 target by target in this order: build with the new compiler in Swift 5 mode; enable complete concurrency checking starting with the UI/app layer; fix warnings cheapest first; flip the target to Swift 6 language mode; move to the next target. Why: The order matters, and mixing steps is how migrations stall; the UI/app layer goes first because much of it is already main-actor-annotated by the SDK, so the fix rate is high. Values: Swift 5 mode, Swift 6 language mode, UI/app layer. [16. Migrating an existing codebase to Swift 6]
- **must** (process, ios): Never combine a significant refactor with enabling data-race safety; refactor afterwards, separately. Why: Otherwise you will have to back out both. [Refactor afterwards, separately]
- **should** (process, ios): Enable Approachable Concurrency and, for app modules, main-actor-by-default before starting a Swift 6 migration, and use Xcode's migration tooling (swift.org/migration). Why: Both dramatically reduce the number of errors you will see. Values: Approachable Concurrency, swift.org/migration. [Enable **Approachable Concurrency** and, for app modules, main-actor-by-default _before_ you start]
- **should** (platforms, ios): Before optimizing, identify which of the four low-level costs you are paying: function calls (argument copies, static vs dynamic dispatch, call-frame allocation, blocked optimization), memory layout (inline vs out-of-line storage, dynamically sized types), allocation (global free, stack cheap, heap expensive) or copies (retains/releases, recursive struct copies). Why: Low-level Swift performance is dominated by these four costs. Values: four costs, one subtraction, search plus locking. [dominated by four costs. Know which one you're paying]
- **must** (tooling, ios): Never comment a test out: use .disabled("reason") or .enabled(if:) for conditions, and withKnownIssue { } for a test failing on something outside your control. Why: A disabled test still compiles; withKnownIssue keeps it compiling and running and tells you when the issue is fixed. Values: .disabled("reason"), .enabled(if:), withKnownIssue { }. [never comment a test out]
- **consider** (tooling, ios): Debug concurrency with LLDB's task support: step through await across threads, use swift task info for priority and children, and name tasks so they show up in the debugger and Instruments' Swift Concurrency template. Why: LLDB understands Swift tasks. Values: swift task info. [LLDB understands Swift tasks]

### Decisions it informs

- Where should a piece of work run?
  - Main actor, synchronous: No concurrency at all; simplest code When: The default for every app; fine for most apps
  - async/await: Hides latency of network or disk without your own concurrency When: Waiting on SDK APIs like URLSession.data(from:)
  - @concurrent: Moves your expensive work to the concurrent thread pool When: Only after Instruments shows a hang
  - actor: Moves state off the main actor When: Too much main-actor state forces tasks to hop back constantly
  - Recommendation: Start single-threaded on the main actor and move down one step at a time without skipping; profile first.
- Should a module default to main-actor isolation?
  - Default Actor Isolation = MainActor: Deletes most @MainActor annotations; code runs on the main actor by default When: App modules and UI-facing modules
  - nonisolated APIs: Work runs wherever the caller runs it; the client decides When: General-purpose libraries
  - Recommendation: MainActor for app and UI modules; never for a general-purpose library.
- Should a data type be a value or a reference?
  - struct / enum: Value semantics; copies are independent; undo, diffing and state restoration become one code path When: The default for all data
  - class: Shared identity and reference semantics When: Identity, shared mutable state, inheritance or resource lifetime
  - ~Copyable type: Unique ownership; double use becomes a compile error When: A file descriptor, a bank transfer, an open resource
  - Recommendation: struct or enum unless you need identity, sharing or inheritance.
- How should code abstract over several types?
  - some P: One fixed type per scope; keeps type relationships and specializes When: The default
  - any P: Type-erased box; flexible but opaque to the optimizer When: Heterogeneous storage, optional underlying type, or hiding the abstraction
  - Constrained extension: Shared behavior with no new protocol When: No per-type customization is needed
  - Protocol requirement: Dynamically dispatched customization point When: A conformer must be able to customize the behavior
  - Recommendation: Write some P by default; change to any P only for storage of arbitrary types.
- How should a function report failure?
  - throw (untyped): Recoverable error; public error type can change later When: Recoverable errors in public API
  - throws(MyError): Typed error without boxing any Error When: Internal functions, error-forwarding generic code, constrained environments
  - precondition / fatalError: Halts the program When: Programmer mistakes, such as an out-of-bounds index
  - Recommendation: throw for recoverable errors; precondition for programmer mistakes; typed throws only internally.
- Which kind of task should run concurrent work?
  - async let: Structured, fixed number of children When: A statically known number of jobs
  - withTaskGroup: Structured, dynamic number of children, results as they land When: A dynamic number of jobs (bounded)
  - withDiscardingTaskGroup: Frees each child immediately, cancels siblings on first error When: Children return nothing
  - Task { }: Unstructured; inherits isolation and priority; you manage cancellation When: Work tied to a UI event or a delegate callback
  - Task.detached: Inherits nothing When: Almost never; put a task group inside it if used
  - Recommendation: Always prefer structured tasks.
- How do you fix a data-race error?
  - Don't share it: Each concurrent job gets its own instance When: First; fixes the overwhelming majority
  - Sendable value type: Sharing becomes copying When: Second
  - Isolate to an actor: Main actor or your own actor owns the state When: Third
  - Mutex / Atomic or @unchecked Sendable: Manual synchronization the compiler cannot check When: Only after the others
  - Recommendation: Work down the list in order; stop sharing the object rather than using @unchecked Sendable.
- How should a global or static variable be made safe?
  - let: Immutable global When: First choice
  - @MainActor: Isolated to the main actor When: Second
  - Mutex: Manual synchronization When: Third
  - nonisolated(unsafe): Unchecked promise When: Last resort, never as a warning silencer
  - Recommendation: In that order of preference.
- How do you break a reference cycle?
  - Restructure to a tree: Shared data moves to a third type both sides reference When: Best option
  - Redesign the API: Object only reachable through a strong reference When: Next best
  - weak/unowned + withExtendedLifetime: Works but shifts correctness onto you and spreads When: A patch, not a design
  - Recommendation: Don't build the cycle; restructure to a tree.
- Which test framework should a test use?
  - Swift Testing: @Test + #expect, parallel randomized runs, traits, parameterized tests When: All new tests
  - XCTest: Still required for exactly three things When: UI automation (XCUIApplication), performance metrics (XCTMetric), Objective-C tests or exceptions
  - Recommendation: Swift Testing by default; XCTest only for its three remaining uses.
- Which test framework interoperability mode should be set?
  - complete: Cross-framework issues stay errors When: Recommended
  - strict: Cross-framework issues stay errors When: Recommended
  - limited: Not recommended by the source When: Avoid
  - none: Not recommended by the source When: Never
  - Recommendation: complete or strict, so issues stay errors and point at the Issue.record replacement.
- What should a temporarily broken test do?
  - withKnownIssue { }: Keeps compiling and running and reports when fixed When: Failing on something outside your control
  - .disabled("reason"): Still compiles but does not run When: A condition makes the test inapplicable
  - Comment it out: Stops compiling When: Never
  - Recommendation: withKnownIssue; never comment a test out.

### Process

1. Check the toolchain: Confirm the project's Swift version: 6.3 is the baseline; 6.4 features are unreleased; the Swift 6.2 async/@concurrent rules do not apply on 6.1 or earlier.
2. Set build settings: Enable Approachable Concurrency everywhere; set Default Actor Isolation to MainActor for app and UI modules (not general-purpose libraries).
3. Concurrency step 1: Run single-threaded on the main actor with no concurrency.
4. Concurrency step 2: Add async/await only to hide latency from network or disk.
5. Concurrency step 3: Add @concurrent to your expensive work only after Instruments shows a hang.
6. Concurrency step 4: Add an actor only when too much main-actor state forces constant hops.
7. Generalize late: Write concrete types, notice repeated code, factor the shared capability into a protocol, then write generic code against it.
8. Fix a data race: Stop sharing, then Sendable value type, then isolate to an actor, then Mutex/Atomic or @unchecked Sendable.
9. Optimize: Do the algorithmic work first, then profile with Time Profiler and Allocations against a test, then apply levers such as final, copy-on-write, InlineArray and Span.
10. Migration 1: build: Build with the new compiler in Swift 5 mode.
11. Migration 2: check: Per target, enable complete concurrency checking, starting with the UI/app layer.
12. Migration 3: fix: Fix warnings cheapest first: var globals to let, free functions onto @MainActor, public structs : Sendable.
13. Migration 4: lock in: Flip the target to the Swift 6 language mode.
14. Migration 5: repeat: Move to the next target and repeat.
15. Migration 6: refactor: Refactor afterwards, separately, never together with enabling data-race safety.

### Examples and visual references

- Material struct with a private class-typed _texture and a copy-on-write color setter using isKnownUniquelyReferenced: Code sample: preserves value semantics while storing a reference type out of line.
- nonisolated struct PhotoProcessor with a @concurrent async process(_:) that runs extractSticker and extractColors via async let: Code sample: work decoupled from the main actor, guaranteed to run in the background, with two independent jobs in parallel.
- .visualEffect { [pulse] effect, proxy in effect.blur(radius: pulse ? 2 : 0) } (SwiftUI): Code sample: copies the Bool into the capture list instead of capturing self in a @Sendable closure SwiftUI runs off the main thread.
- Replacing isSharing, selectedRows and shareTarget optionals with one enum State: Makes invalid state combinations unrepresentable and state change atomic.
- Actor cache race: check cache, await download, write cache: Two tasks both miss, both download, and the second clobbers the first; fix by re-checking after the await or deduping in-flight work.
- GeometricVector<Storage: SIMD> rather than GeometricVector: SIMD: Has-a over is-a: wrap a protocol in a generic struct exposing only the intended API.
- Array.remove(at:) in a loop and per-byte Data re-slicing: Two 100×+ regressions hiding behind clean-looking code; fixed with removeAll(where:) and popFirst().
- @Observable composes member, member-attribute and conformance macro roles (Swift macros): Shows attached macro roles combining.
- Raw identifier test name: @Test func `fruits have a tropical climate`() (Swift Testing): Readable test names instead of awkward function names (since Swift 6.0).

### Numbers

- Swift 6.3: Toolchain baseline, current release as of August 2026 [Toolchain baseline: Swift 6.3]
- Swift 6.4: Unreleased features marked with a warning sign; safe to plan around, unsafe to write [Rows marked ⚠ are Swift 6.4]
- Swift 6.2: Concurrency model assumed; async no longer moves a function off the current actor [The rule that changed]
- 6.1 or earlier: Projects where the async and @concurrent rules do not apply [Toolchain baseline]
- Xcode 26: Main-actor default isolation is the default for new app projects [Default Actor Isolation]
- four: Low-level performance costs: function calls, memory layout, allocation, copies [dominated by four costs]
- O(n²): Array.remove(at:) called in a loop, versus O(n) total for removeAll(where:) [Know the complexity of what you call]
- O(1): popFirst() versus O(n²) per-byte Data re-slicing [Know the complexity of what you call]
- 100×+: Regressions caused by the two complexity mistakes [Both of these were 100×+ regressions]
- three retains: Per copy of a large struct with three reference-typed fields, versus one for a class [Struct storage is inline]
- 3-word: Inline buffer of an any P existential; larger values are heap-allocated per copy [An `any P` existential has a 3-word inline buffer]
- five: Attached macro roles: member, peer, accessor, member-attribute, conformance [one of five roles]
- three: Remaining uses of XCTest: UI automation, performance metrics, Objective-C tests/exceptions [exactly three things]
- SE-0460: @specialized(where T == ...) pre-specialization, shipped in Swift 6.3 [Shipped in Swift 6.3]
- SE-0504: Task cancellation shield, Swift 6.4 (unreleased) [cancellation shield]
- ST-0021: Swift Testing test framework interoperability proposal [Test framework interoperability]
- O(n): Total cost of removeAll(where:), versus O(n²) for remove(at:) in a loop [Know the complexity of what you call]
- one subtraction: Why stack allocation is cheap; heap allocation is expensive (search plus locking), global is free [Allocation]
- Swift 6.1+: nonisolated on a type makes all its members nonisolated [nonisolated on a type makes all its members nonisolated]
- 5.9: Since-version for if/switch expressions, parameter packs and @Observable [Modern syntax you should be using]
- 5.7: Since-version for Swift Regex [Hand-rolled string index math]
- 6.0: Since-version for raw identifiers (e.g. readable test names) [Awkward test function names]
- 1.0 lands with 6.4: Subprocess package release timing [the Subprocess package]

<!-- /od:learn -->
