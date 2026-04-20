# Decision — Prototype debug-check sweep (pre-playtest)

**Date:** 2026-04-20
**Status:** Accepted
**Reversibility:** Easy
**Affects:** prototype/index.html, tools/cascade-lint.py, prototype/README.md, PROGRESS.md, HANDOFF.md, CASCADE.md

---

## Decision

Sweep the 6 debug-check findings documented in `HANDOFF.md §"Debug check — known issues"` *before* the Step 5 PM playtest, rather than letting them contaminate playtest signal. All fixes are prototype-scope and introduce no CONCEPT constraint changes, no engine code, and no scope expansion. All numbers remain [PROPOSAL].

Findings swept:
1. `</h3>` typo on Co-op Horde mode card (`index.html:331`).
2. Guest-side `game.cells[*].occupied` not reconciled from host snapshots.
3. PeerJS free-broker SLA risk (documentation only — code change not appropriate at prototype scope).
4. Inline `AGES` fallback only has 3 entries; `file://` open silently truncates to 3 ages.
5. `cascade-lint` reports `next-open-step: Step 2` even though Step 2 is explicitly PM-default-skipped.
6. First-snapshot tower-position flash on guest (cosmetic; one-frame skip band-aid applied).

## Context

Step 10 concept-demo pivot landed in full last session under a PM cadence override. The debug sweep was deliberately deferred ("found but not fixed") so HANDOFF would document them for the next session. Step 5 is the critical gate — a first real two-player co-op playtest with a friend — and findings 1/4/6 cosmetic-flaw the first impression while 2 pollutes the guest-side co-op signal the playtest is specifically there to evaluate.

Freeze date for the concept-demo is 2026-05-15; there is time to land the sweep and still give the playtest a clean window.

## Alternatives considered

- **Option A — playtest first, file findings, fix after.** Respects the "only real signal counts" principle. Rejected because findings 1/2/4/6 are already known and would generate noise findings during playtest, burning a scarce PM+friend two-browser window on re-discovering documented bugs.
- **Option B — sweep first, then playtest.** (Chosen.) Each fix is small + isolated + locally verifiable; total surface area is ~25 lines across 3 files plus a README note. Lets the playtest produce genuinely new signal.
- **Option C — defer sweep to after the freeze date.** Rejected — sweep cost is hours not days; dragging it across the freeze boundary risks forgetting it and baking the defects into whatever comes next.

## Reason chosen

3x debug loop:

- **Loop 1 — critique.** Fixing the six things just before a first-time live friend playtest risks introducing *new* defects worse than the known ones, and delays the playtest. Each fix site must therefore be provably minimal.
- **Loop 2 — steelman.** The findings list is explicitly small: two one-line edits (1, 4), one doc edit (3), one tooling edit (5), two ~3-line edits inside one function (2, 6). None of the fixes touch match logic, economy, wave progression, hybrid discovery, or PeerJS handshake. The blast radius of each is bounded to the site it names.
- **Loop 3 — synthesis.** Sweep in one pass, verify each fix in isolation, keep the cascade-lint green bar as the hard gate. If any fix proves non-trivial (e.g. the `cell.occupied` reconciliation requires snapshot-schema changes), *stop* and escalate rather than deepen the blast radius. The PM directive ("bypass permissions aggressively, come back when you need me") explicitly supports this mode.

## Reversibility note

All changes are local to `prototype/*`, `tools/*`, and the doc layer. Zero CONCEPT constraint change. Revert by reverting this commit-equivalent; no downstream amendments cascade.

## Follow-ups

- Step 5 playtest unblocked (per `PROGRESS.md`). PM + friend run a 2-browser Co-op Horde match and file findings as dated `decisions/` entries.
- `cascade-lint` now recognizes `[~skip]` tag on PROGRESS.md rows; `Step 2` marked `[~skip]` so `next-open-step` correctly reports `Step 5`.
- Broker-SLA limitation is documented in `prototype/README.md`; self-hosted broker remains an engine-port concern, not a prototype one.
- `PORT-NOTES.md` does **not** gain a snapshot-occupancy-reconciliation row: the prototype's O(towers × cells) reconstruction is a workaround for the prototype's 10Hz wholesale overwrite pattern, which the Godot port will replace with incremental state sync. Findings-not-code discipline preserved.
