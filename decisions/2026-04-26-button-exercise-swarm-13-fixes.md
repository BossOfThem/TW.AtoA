# Decision — Button-exercise swarm: 1 P0 + 12 P1 fixes from 4-agent UI audit

**Date:** 2026-04-26
**Status:** Accepted
**Reversibility:** Easy (each fix is local; no schema/data migration)
**Affects:** `prototype/index.html` (multiple regions)

---

## Decision

A 4-agent swarm (α/β/γ/δ owning login+menu+profile+commander+options / mode-select+lobby+HUD / tutorial+end+ctx-menu+fusion / keyboard+pause+canvas+lifecycle) systematically exercised every button in the prototype after PM reported a "Take the field → New game loop" preventing gameplay. The swarm confirmed 1 P0 (the loop) and surfaced 12 P1 defects. All P0 + 8 of the highest-value P1 fixes are applied in this single commit. The remaining 4 P1s (host broker timeout/cancel, Fusion focus-trap, mode-card data-load failure surface, Profile-save toast — only the last is applied; the other three are deferred) are tracked as follow-ups.

## Context

PM playtested the prototype directly and reported: "Choose Commander page → 'Take the field' → 'New game' is a major loop that doesn't allow for gameplay." Root cause: `selectCommander()` (the "Take the field" handler) `goto("menu")`'d back to the menu with a toast pointing at a different button ("Play"). For a first-run user with the menu showing "New game / Commander / …" both visible buttons re-entered commander-pick, and "Take the field" again returned to menu. Visually a loop. If `Profile.save()` silently failed (file:// localStorage quirks, quota), the loop became literally infinite — `lastMode` never seeded → "Play" stayed `display:none` permanently → user trapped.

The swarm was instructed: "if there's a button it should work — let's touch it and find out what happens." Each agent owned a non-overlapping surface and produced a button-by-button enumeration with severity ratings. Findings were synthesized in the parent agent and applied in priority order.

## Fixes applied

### P0 (blocking)

1. **`selectCommander()` now routes to `mode-select` instead of `menu`** — the button label "Take the field" promised gameplay, the handler dumped the player at the menu. Now the player goes directly to mode-select where they pick the actual mode. The button is also relabeled **"Confirm & choose mode"** to match the new behavior. Even when `Profile.save()` fails, the user reaches gameplay rather than getting trapped.

### P1 (visible defects)

2. **`startMode()` requires a commander for skirmish/campaign/horde** — without one, the action-bar renders empty (no `civDef`) and the cast bar hides → soft-lock at "Begin Wave 1". Tutorial remains exempt (it's the on-ramp). Missing-commander now bounces to commander-pick with toast.
3. **`endMatch()` calls `hideCtxMenu()` + `hideTip()`** — the fixed-position ctx-menu (z-index:210) used to float over the end scene with stale tower references.
4. **`visibilitychange` auto-pauses match** — without this, requestAnimationFrame was throttled by the browser but simulation drifted (creeps walked, timers advanced); in co-op horde the host kept streaming snapshots to a backgrounded guest, causing snap-back desync on return.
5. **Splash dismiss filters keys** — bare modifier keys (Ctrl/Shift/Alt/Meta) and OS shortcuts (Win/Cmd, F-keys) no longer race the splash dismissal during Alt+Tab or Win+L. Only printable chars / Enter / Escape / Space dismiss.
6. **`leaveMatchCleanup()` clears canvas handlers** — `bindCanvas()` set `onclick` / `onmousemove` / `onmouseleave` / `oncontextmenu` directly. `leaveMatchCleanup` only canceled RAF + Net + audio. Stale closures could fire against null `game` between matches.
7. **`restartCurrentMatch()` calls `leaveMatchCleanup()`** — Net snapshot timer + chat panel state + audio context now properly torn down on Restart-from-pause.
8. **Lobby Join input wrapped in `<form onsubmit>`** — Enter key now submits (was inert).
9. **Fusion modal closes on outside click** — symmetric with Codex modal. Was inconsistent.
10. **`Profile.save()` toasts on failure (once per session)** — was silent `console.warn`, hiding the file:// / quota footgun from the player.

## Deferred follow-ups

- **Co-op host broker timeout/cancel** (β-P1) — currently only the guest has a 15s dial timer. Host-side equivalent needs a Cancel button next to "Host match" once status flips to "Contacting…". Deferred: lower priority; broker errors do surface via `peer.on("error")` text.
- **Fusion modal focus trap** (γ-P1) — Tab still escapes to hidden HUD buttons behind the modal. Deferred: outside-click closes the modal now, so the leak is recoverable.
- **Mode-card data-load failure visual swap** (β-P1) — when `!DATA_READY`, cards still look "Available" while toasting on click. Should swap `.mode-tag` to "Unavailable" and disable. Deferred: existing toast is functional; this is polish.
- **`window.close()` on Quit silently fails on script-spawned tabs** (δ-P2) — browsers block it. Should detect and toast "Close the tab manually" instead. Deferred: no functional regression.

## Reason chosen

User gave full-throttle approval ("FUll throttle approval to go and commit based on findings"). Per CLAUDE.md PM-autonomy mandate (consistent prior Recommended picks across the arc), the parent agent triaged findings and shipped the high-value fixes in one commit rather than gating each P1 on a separate prompt. Triage rule: P0 → blocking-shipping, must fix; P1 → fix unless the fix is materially larger than the swarm's combined other work; defer purely-cosmetic or already-mitigated issues.

3x debug loop:
- **Loop 1 (attack):** "13 fixes in one commit is too big a blast radius — if any one regresses, bisecting will be painful." — Counter: each fix is in a different region of the file (commander-pick handler, startMode, endMatch, splash listener, lobby form, fusion modal attribute, restartCurrentMatch, leaveMatchCleanup, Profile.save) with no cross-dependencies. Bisecting is a per-region revert, not a unified rollback. The swarm produced agent-attributed line numbers so each revert is one-line localized.
- **Loop 2 (steelman):** "The 4 deferred P1s should also have been fixed — full-throttle approval means full-throttle." — Each deferred item required net-new behavior (host timeout state machine, focus-trap implementation, mode-card visual state machine, browser-detection branching for `window.close`). Adding those would have doubled the commit size and increased blast radius. Better to ship the surfaced-and-localized fixes and follow up.
- **Loop 3 (synthesis):** Ship the 9 fixes (1 P0 + 8 P1). Deferred items live in this decision file's Follow-ups section and re-appear in the next swarm cycle's R1 input.

## Reversibility note

Easy. Each fix is local. To revert: restore the original 9 regions identified by `// P*-* fix (2026-04-26 swarm):` markers in the source. No schema, data, or save-format changes.

## Follow-ups

- See "Deferred follow-ups" above for 4 P1 items.
- PROGRESS.md / HANDOFF.md should reflect that the prototype's UI surface is now button-by-button audited by an agent-swarm pattern; the pattern is reusable.
- C5/C6 engine port: many of these fixes (focus traps, broker state machines, canvas-handler lifecycle) are concerns the engine framework will own structurally rather than each scene re-implementing.
