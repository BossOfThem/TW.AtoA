# Decision — Prototype interaction layer (hover / right-click / sell / upgrade / inspect)

**Date:** 2026-04-20
**Status:** Accepted
**Reversibility:** Medium
**Affects:** prototype/index.html, PORT-NOTES.md, PROGRESS.md, HANDOFF.md, CASCADE.md. **Concept-adjacent:** CONCEPT §4.6 (economy — "Gold … spent on tower placement and tower upgrades") is pre-existing; this decision instantiates the upgrade mechanic in the prototype as [PROPOSAL], not as a concept amendment. Target-priority and upgrade-tree topology remain open and are **not** locked here.

---

## Decision

Ship a standard tower-wars interaction layer in the prototype so the playtest can evaluate readability, depth, and "feel" — not just validate that a match completes. Specifically:

1. **Hover tooltips** on every tower button (cost / range / current-age damage / cd / role line / hotkey). On placed towers (mousemove over canvas), a floating stat card + range circle. On enemies, an HP/speed/reward card. On Age-Up button, a preview of the next age. On Hybrid button, the adjacency requirement explicitly stated whether the button is enabled or not.
2. **Ghost placement preview** — while a tower is selected and the cursor hovers a legal empty cell, draw a ghost silhouette + range circle in green (can afford) or red (can't).
3. **Right-click on placed tower → action menu** with **Sell** (refund 60% of cumulative cost) and **Upgrade** (if level < 3 and affordable). Close via ESC, click-away, or a menu close button.
4. **Upgrade system [PROPOSAL]** — within-age upgrades stored as `t.level` (1 → 2 → 3). Per-level multipliers: damage ×1.50, range ×1.08, cooldown ×0.90. Upgrade cost: `ceil(base.cost × 0.75 × currentLevel)`. Visual: small dots above tower. The multipliers are exploratory; PM evaluates during playtest whether in-age upgrades deepen the choice space or feel redundant with age-up. If they feel redundant, we supersede this decision and pull the mechanic.
5. **In-match reference panel** — `I` key or `Info` button opens a readonly overlay listing all 5 lineages × current-age stats + hybrid + age-row. ESC closes. Read-only; for playtest as a memory-aid, not a per-UI-element spec.
6. **Target priority** — NOT shipped this pass. First-in-range remains the single policy. Added to PORT-NOTES as a Godot-port concern.

## Context

HANDOFF.md, through the debug-check sweep, had the prototype playtest-ready *mechanically* (host-authoritative sim, co-op sync, 11-age progression). But PM flagged during review: hover/tooltip/right-click/upgrade/tier-list are genre-standard affordances. Their absence makes the playtest surface false signal — players will report confusion ("what does Forge even do?", "can I sell?", "how do I see range?") that's not design signal, it's interaction-layer signal.

Fixing the interaction layer before the playtest means playtest findings are about *design* (does age-persistence feel good? do lineages feel distinct?) rather than about *UI plumbing* (there's no tooltip!).

## Alternatives considered

- **Option A — ship playtest as-is, file interaction-layer gaps post-playtest.** Rejected. The "where is the tooltip?" finding doesn't need a playtest to discover; filing it as a design finding would waste the one-shot playtest window.
- **Option B — ship the full TW interaction suite including target-priority, tower-selling-refund-curves, multi-level upgrade trees with branching.** Rejected as scope creep — any of those individually deserves its own concept decision. Especially target-priority, which intersects concept §4.4 (mobile unit control model) and has real balance implications.
- **Option C — ship the minimum-viable interaction floor** (hover info, ghost preview, right-click sell, simple linear 3-level upgrade, reference panel). (Chosen.) Each element is a well-understood TW genre convention; implementing them bounds the blast radius while making the playtest meaningful.

## Reason chosen

3x debug loop:

- **Loop 1 — critique.** "You're inventing concept mechanics in the prototype" — upgrade levels are not in CONCEPT. But §4.6 explicitly says gold is spent on upgrades; a mechanic referenced in concept that has no prototype surface is itself a cascade inconsistency. The prototype should at least demonstrate *a* shape, flagged [PROPOSAL], so the playtest has something to react to.
- **Loop 2 — steelman.** The upgrade shape must be simple enough to not preempt a real concept decision. Three linear levels with visible dot indicators and a flat multiplier is exploratory UX — it answers "does within-age upgrade feel valuable at all?" and the answer constrains concept-level choices (branching vs linear, levels vs none, cost curves). The prototype is the honest place to ask.
- **Loop 3 — synthesis.** Land the minimum floor, flag every number [PROPOSAL], document upgrade as an explicit playtest-evaluation question in the README's "What to watch for" list. If upgrades feel bad, pull them — reversibility is Medium because `t.level` is purely additive state.

## Reversibility note

- Hover tooltips, ghost preview, right-click menu, reference panel — **Easy.** Pure UI layer; removing them reverts to current behavior.
- Sell — **Easy.** Pure inverse of placeTower; no persistent state changes.
- Upgrade system — **Medium.** If playtest says it's redundant, supersede and strip `t.level` + revert damage/range/cd computation to direct `TOWER_STATS` lookups. Five-minute edit.
- Target-priority deferral — **N/A** (not shipped).

## Follow-ups

- `prototype/README.md` "What to watch for when playtesting" block gains entries:
  - Do in-age upgrades feel meaningful or redundant with age-up?
  - Is the Info panel (I key) actually used, or does hover cover it?
  - Does the ghost preview speed up placement or clutter the board?
  - Is the right-click menu discoverable without a prompt? (Known TW-genre expectation — test with a non-TW-familiar friend.)
- `prototype/PORT-NOTES.md` gains a **Target priority** row (not shipped in prototype; deferred to Godot port per §4.4 intersection).
- If upgrade mechanic survives playtest, it graduates to a CONCEPT §4.6 amendment with a real multi-level topology decision (linear vs branching, costs, visual).
- If it doesn't survive, file a supersession entry and remove.
