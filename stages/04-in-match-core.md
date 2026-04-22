# Stage 04 — In-Match Core

**Status:** Stub
**Phase in CONCEPT cascade:** 3 (Design) / 4 (Specification — economy, units, enemies)
**Upstream deps:** [Stage 03 — match setup](03-match-setup.md), [CONCEPT §3.3 lineages](../CONCEPT.md), [CONCEPT §3.4 unit categories](../CONCEPT.md), [CONCEPT §4.4 mobile units](../CONCEPT.md), [CONCEPT §4.6 economy](../CONCEPT.md), [CONCEPT §4.7 enemies](../CONCEPT.md)
**Downstream impact:** [Stage 05 — age evolution](05-age-evolution.md), [Stage 06 — hybrids & fusion](06-hybrids-fusion.md)
**Open questions:** See below.
**Research backing:** [01-genre-pulse.md](../research/01-genre-pulse.md)
**Last reviewed:** 2026-04-22

---

## Amendment 2026-04-22 (stub-level, deferred from plan A7)

Stage 04 was not in A7's scope (01 / 05 / 06) during the 2026-04-21 concept-tightening cascade and retained pre-pivot framings. Under [2026-04-21 concept tightening](../decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md) (Reversibility Hard), the following body references are now **obsolete**:

- Scope bullet "gameplay within a single age" — should read *within a single tier* (Dust / Form / Apotheosis) per [phase-3 §3.5](../concept/phase-3.md#35-the-three-tiers-in-match-tower-evolution-arc).
- Scope bullet "gold income, knowledge income, influence income" — the three-currency mapping backed by Forge / Ember / Crown no longer applies; under the 3-lineage shape currency mapping is rescoped OPEN at [phase-4 §4.6](../concept/phase-4.md#46-economy-specification) with a Gold / Faith / Cinders [PROPOSAL].
- Open question "parallel evolution vs 'the Left Behind' vs hybrid" — both civilizational-timeline framings are superseded by the new Tier-local / Descent's-residue direction sketches at [phase-4 §4.7](../concept/phase-4.md#47-enemy-system-pve-modes) (rescoped OPEN under dungeon cosmology).
- Verification goal "age 1 alone... first Age Gate" — should read *Dust tier alone... first Tier Gate*.

Remaining content below is preserved for traceability; a dedicated Stage-04 rewrite happens when this stage is next opened in a Phase-C pass. Names Dust / Form / Apotheosis are prose placeholders — `concept/phase-5.md §5.4 [LOCKED]` is untouched.

---

## Scope

Moment-to-moment gameplay within a single age:

- Wave spawning, tower targeting, damage resolution.
- Economy tick — gold income, knowledge income, influence income, optional Mythium (PvP).
- Tower placement, upgrade, sell.
- Mobile unit commands (waypoint + mode flags; no full RTS micro).
- Send/defend loop in PvP (creep sending, merc sending, Mythium spend).
- Commander signature ability on cooldown (hero-mode modes only).
- UI surfaces: health bar, economy, wave indicator, send panel, build menu.

## To be written (Phase C pass)

Longest stage by line count. This is where the game either feels good or does not. Expected 500–600 lines. Will reference specific competitor mechanics (Legion TD 2 worker/Mythium loop, Kingdom Rush targeting priorities) from [01-genre-pulse.md](../research/01-genre-pulse.md).

## Open questions (seed list)

- Mobile unit control model — **OPEN BLOCKER from [CONCEPT §4.4](../CONCEPT.md)**.
- Enemy direction (parallel evolution vs "the Left Behind" vs hybrid) — **OPEN BLOCKER from [CONCEPT §4.7](../CONCEPT.md)**.
- Build menu organization — by lineage, by age, by role, by cost.
- Sell refund percentage (preserves experimentation vs prevents flipping).
- Creep-send latency in PvP — instant, delayed, telegraphed.

## Verification

To be populated. Goal: age 1 alone is fun enough to hold attention for a full 2–3 minutes before the first Age Gate.
