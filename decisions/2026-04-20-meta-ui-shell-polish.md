# Decision — Meta-UI shell polish (splash / login / menu / mode-aware pause)

**Date:** 2026-04-20
**Status:** Accepted
**Reversibility:** Easy
**Affects:** `prototype/index.html` (splash CSS 61–73, login scene 342–356, menu scene 361–379, profile-scene stub 384–401, togglePause 1703+), `prototype/README.md`, strand 1 of Meta-UI pass

---

## Decision

Instantiate the six filed decision rails (first-run-flow, meta-ui-envelope, save-model, commander-identity-floor, audio-architecture, accessibility-floor) into the HTML prototype's shell layer: (a) splash becomes a diamond-rise + glyph-by-glyph title build with reduce-motion hard-cut at 300ms; (b) login scene branches first-time vs returning copy based on `Profile.load()` result; (c) main menu branches first-time ("New game" primary) vs returning ("Continue" + "Play" + last-played hint line); (d) `togglePause()` is mode-aware — Campaign hard-pause with Save-and-Exit, Skirmish hard-pause with no save/restart, Co-op Horde host-authoritative with 10s vote timeout and additive snapshot message `{type:'pause-vote'}`, Lane Wars read-only overlay that doesn't stop tick.

## Context

Phase 10.1 pivot (2026-04-20) landed a concept-demo focus. Six decision rails filed the same day specified the shell behavior but the HTML still rendered a flat splash label, a single-variant login, a returning-only menu, and a mode-agnostic pause. The PM pushed for TW/HoMM/AoE/SC-WC3 DNA-injection on top — this strand is the floor (shell polish) before the DNA-injection strands (7/8/9) build on it.

## Alternatives considered

- **Option A — External CSS/JS files.** Split the prototype into modules. Why not: prototype is throwaway per `decisions/2026-04-19-design-prototype-scope.md`; single-file keeps the port-findings-not-code guardrail trivial to enforce.
- **Option B — Engine-side implementation (Godot).** Why not: engine code forbidden until Phase 5. Prototype is the design-exploration surface; port notes live in `PORT-NOTES.md`.
- **Option C — Inline HTML/JS edits with additive `Profile` fields + mode-switch inside `togglePause()`.** (Chosen.) Keeps the single-file prototype surface, preserves co-op snapshot additive-only invariant, maps 1:1 to Godot scene / `get_tree().paused` + custom signal patterns.

## Reason chosen

**Loop 1 — aggressive critique.** The splash glyph animation risks feeling gimmicky and slow on returning sessions (3s is an eternity to a daily player). The mode-aware pause branches on `game.matchMode` which could be undefined on first boot if `currentMatchMode` isn't threaded through every code path. The login's auto-prefill of existing username creates a subtle UX trap: "enter" on the prefilled field silently logs in — a returning player who *wants* to logout might miss the distinct "Logout/clear" button. The menu's `menu-last` text references `lastMode` which can drift out of sync with actual save existence.

**Loop 2 — steelman.** Splash glyph cadence (~200ms + 90ms/char for 12 chars ≈ 1280ms) is well under the 3s skip cap and the *whole scene* is skippable by any key/click — fast players skip, slow players get the flavor. `game.matchMode` is set in `initMatch()` from `currentMatchMode`; the `|| "skirmish"` fallback is safe even pre-match. The login auto-prefill-then-Enter matches Steam/most-games UX where "returning" literally means "just hit Enter". The `menu-last` drift is cosmetic; the actual Continue button correctly disables when `hasSave()` is false.

**Loop 3 — synthesis.** Ship the shell polish as coded. Add a one-line correction: the Continue button's `display:none` guard is already in place; the `menu-last` hint is flavor, not gate. For `togglePause` edge cases in co-op, the host-only authority is correct per [meta-ui-envelope.md:16–24](meta-ui-envelope.md) — guests that want pause send a `pause-vote` request message that the host can honor. Reduce-motion users get 300ms hard-cut, fully meeting [accessibility-floor.md](accessibility-floor.md) WCAG 2.3.3. No open mitigations needed; move to Strand 2.

## Reversibility note

Easy. All edits are additive inside `<style>` and `<script>` blocks. Reverting = restore the 3 HTML regions + one `togglePause()` function + `SCENE_IDS` array. No data schema changes, no co-op wire-format changes (pause-vote is additive; guests that don't understand it ignore it safely).

## Follow-ups

- Strand 2 (this pass) — Profile scene populator + mode-aware `writeMatchSave` audit.
- Strand 3 (this pass) — Options tabs real (audio/input/video/a11y/gameplay).
- Port note: Godot `get_tree().paused = true` for hard-pause modes; custom PauseOverlay scene with `process_mode = Always` for Lane Wars read-only overlay; RPC call `pause_vote(by, paused)` for co-op.
