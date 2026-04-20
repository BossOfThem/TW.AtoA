# Decision — Spontaneity random events (HoMM/AoE DNA)

**Date:** 2026-04-20
**Status:** Accepted
**Reversibility:** Easy
**Affects:** `prototype/index.html` (`rollSpontaneityEvent`, `applySpontaneityEvent`, `showEventBanner`, `startWave`/`ageUp` hooks, guest `event-roll` receiver), `prototype/data/events.json` **(new)**, `profile.settings.gp.spontaneity`

---

## Decision

Introduce 8 micro-events (new `events.json`) that fire at `wave-start` / `age-gate` / `low-lives` with 25% base probability and weighted pool selection, no two in a row. Seeded by match-start timestamp so co-op host+guest roll identically. Effects are additive, never match-winning: +gold / +knowledge / telegraph-extended / random-tower-upgrade / wave-HP-mult / wave-count-delta / wave-speed-mult. Co-op additive snapshot message `{type:'event-roll', id}` broadcast from host; guest renders the banner on receive. Off-switch at `profile.settings.gp.spontaneity` (default on).

## Context

PM pushed HoMM/AoE DNA specifically called out: "spontaneity via random events / map modifiers, build-vs-combat rhythm — while retaining balance and not over-complicating." Per-wave flat repetition is the enemy; small surprises reward attention without being swingy.

## Alternatives considered

- **Option A — Deterministic event calendar (wave N always fires event X).** Why not: kills surprise; predictable optimal play.
- **Option B — Fully random with no seed (co-op desync).** Why not: host/guest roll differently → state drift.
- **Option C — Seeded LCG keyed on `matchStartMs`, weighted pool, 25% probability, no-repeat memory.** (Chosen.) Surprise-preserving, determinism-preserving for co-op, balance-preserving (both boons and mild downsides present).

## Reason chosen

**Loop 1 — aggressive critique.** 25% per trigger × 3 triggers per wave could mean multiple events per wave — chaos. LCG seeded by timestamp is weak RNG (predictable if someone inspects `matchStartMs`). "Restless Land" is a pure downside — players hate unannounced downsides.

**Loop 2 — steelman.** Triggers are mutually exclusive per call site (wave-start fires once per wave, age-gate once per advance, low-lives once when lives drop below threshold); not 3× per wave. LCG is fine for cosmetic roll — not cryptographic. "Restless Land" is announced in the banner *before* the wave begins, giving the player time to adapt — that's the *point* of spontaneity with balance (downside visible + actionable).

**Loop 3 — synthesis.** Ship as-coded. Add `no-two-in-a-row` memory via `game._eventLastId` (done). Future: if Step 5 playtest shows "Restless Land" feels cheap, bump its weight down or remove. Balance invariant: total expected value ≈ neutral across boons+downsides so the system doesn't creep economy.

## Reversibility note

Easy. Remove 2 JS functions + one JSON file + two hook calls. `events.json` absent → `EVENTS = null` → `rollSpontaneityEvent` no-ops. Co-op schema additive: peer without event code ignores the message.

## Follow-ups

- Strand 7 (this pass): Commander-on-field hero.
- Step 5 playtest: log event roll frequency + player sentiment.
- Port note: Godot → `RandomNumberGenerator` with `seed = match_start_unix_ms` for determinism; `rpc_id(guest, "show_event_banner", id)` for co-op propagation.
