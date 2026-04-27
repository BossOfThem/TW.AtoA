# Decision — Visibility auto-pause: extend coverage to tutorial scene

**Date:** 2026-04-26
**Status:** Accepted
**Reversibility:** Easy (one helper + three call-sites in `prototype/index.html`)
**Affects:** `prototype/index.html` (visibilitychange listener, `initMatch`, `initTutorial`)

---

## Decision

Extend the 2026-04-26 visibility hardening fix to also cover the **tutorial** scene. Introduce a small `autoPauseForHidden()` helper that handles both code paths:

- For `currentScene === "match"` it routes through the existing `togglePause()` (which owns pause-overlay UI, co-op vote, etc.).
- For `currentScene === "tutorial"` it directly flips `game.paused = true` (tutorial has no pause overlay; `gameLoop` already honors `game.paused`).

A symmetric on-visible branch auto-resumes the tutorial (no overlay = no manual unpause UI for the player).

## Context

Continuation of `decisions/2026-04-26-visibility-initial-hidden-gap.md`. Today's playthrough verified the *match-scene* fix end-to-end. While exercising the tutorial flow in the same hidden tab, the wave-spawner stalled identically: `tutorialStep: 2`, `wave: 1`, `enemies: 0`, `kills: 0` after 18 s of wall-clock time with `document.hidden: true`. Root cause: `togglePause()` early-returns when `game.mode !== "match"`, so the prior fix's predicate-mirror in the listener and `initMatch` was a no-op for tutorial.

`initTutorial()` constructs the same `game` object and starts the same `gameLoop`, which is throttled by the browser when the tab is hidden. The original throttled-but-not-paused symptom therefore reproduces in tutorial just as it did in skirmish/horde.

## Reason chosen

Smallest local change preserving the previous fix's semantics. One helper, three call-sites. No state, no schema, no UI changes; the tutorial has no pause modal so no visual surprise is introduced.

3x debug loop:
- **Loop 1 (attack):** "Pausing tutorial silently is invisible — when the player un-hides the tab they may not realize anything happened, then a wave snaps into action." — Counter: the on-visible branch auto-resumes; from the player's perspective the simulation simply continues from the last-visible frame instead of advancing while they were elsewhere.
- **Loop 2 (steelman):** "togglePause should be generalized to accept tutorial mode rather than splitting the logic." — Reasonable, but `togglePause` carries co-op pause-vote, lane-wars overlay branching, and overlay toggling — none of which apply to tutorial. Keeping tutorial on a direct flag flip avoids dragging that scope into a fix.
- **Loop 3 (synthesis):** Ship the helper. Match keeps its overlay-driven pause path; tutorial gets the silent flag flip + auto-resume. Together they cover the full visibility ↔ scene matrix.

## Reversibility note

Easy. Delete `autoPauseForHidden()` (8 lines), restore the listener's prior body, drop the new `if (document.hidden) autoPauseForHidden();` calls at the end of `initMatch` and `initTutorial`. Markers: same `// P1 fix (2026-04-26 playthrough cont.)` comment family.

## Follow-ups

- C5/C6 engine port: visibility/pause semantics belong in the engine framework; per-scene init blocks are scaffolding.
- If a future scene (e.g. lane-wars campaign mission, replay viewer) also runs `gameLoop`, audit it against the same predicate.
- If the tutorial ever gains a pause overlay, fold tutorial into the match path of `togglePause` and retire the silent-flag branch.
