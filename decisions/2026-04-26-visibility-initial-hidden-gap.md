# Decision — Auto-pause hardening: handle initial-hidden tab on match start

**Date:** 2026-04-26
**Status:** Accepted
**Reversibility:** Easy (one local block in `initMatch`)
**Affects:** `prototype/index.html` (end of `initMatch()`)

---

## Decision

The 2026-04-26 swarm shipped a `visibilitychange` listener that auto-pauses an in-match game when the tab loses focus. Live playthrough verification today exposed a gap: the listener only fires on **transitions**. If a player navigates to `match` while the tab is **already hidden** (background tab restore, devtools workflows, headless/extension-driven sessions), the listener never observes a transition and `togglePause()` is never called — the simulation drifts under throttled RAF exactly as the original P1 described. Add a one-shot check at the end of `initMatch()` that mirrors the listener's predicate (`document.hidden && game && !game.paused && !game.ended`) and calls `togglePause()` if true.

## Context

A live human-perspective playthrough via Claude-in-Chrome (tab opened in background) reproduced the original throttled-but-not-paused behavior: after `Begin Wave 1`, in 18s only 1 of 6 enemies spawned and 0 were killed even though the Phalanx tower was in range. Probe confirmed `document.hidden: true` and `game.paused: false` simultaneously — i.e. the listener never fired because there was no visibility transition, the page was hidden when the match scene mounted.

This is a real-user edge case, not just a test artifact: a player who restores a backgrounded tab into an active campaign load (or who alt-tabs during the inter-scene transition itself) hits the same path.

## Reason chosen

Smallest local change matching the existing fix's predicate. No state, no schema, no ordering assumptions beyond what `togglePause()` already requires.

3x debug loop:
- **Loop 1 (attack):** "Calling `togglePause()` inside `initMatch` could pause-on-arrival for a player who legitimately wants the match to start running while they read the tutorial card. Surprise pause = bad UX." — Counter: the predicate gates on `document.hidden`, so a visible tab is unaffected. A hidden tab cannot reasonably be "actively reading the tutorial card" — by definition it's not visible.
- **Loop 2 (steelman):** "Maybe initial pause should be unconditional and the listener handles resume — symmetrical with the existing transition path." — Reasonable but expands scope; the original listener gated on hidden, so mirroring its predicate keeps the two paths semantically identical.
- **Loop 3 (synthesis):** Ship the predicate-mirror. Listener still owns transitions; init owns mount-time state. Together they cover the full state machine.

## Reversibility note

Easy. Delete the new block in `initMatch()` (bounded by the comment marker `// P1 fix (2026-04-26 playthrough)`).

## Follow-ups

- C5/C6 engine port: structural visibility/pause semantics belong in the engine framework, not each scene init. Engine should own: window focus, RAF gating, simulation-tick freeze on backgrounded contexts.
- If a future P1 surfaces around resume from initial-hidden (e.g. player un-backgrounds and pause overlay is showing immediately), revisit symmetric resume.
