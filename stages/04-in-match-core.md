# Stage 04 — In-Match Core

**Status:** Stub
**Phase in CONCEPT cascade:** 3 (Design) / 4 (Specification — economy, units, enemies)
**Upstream deps:** [Stage 03 — match setup](03-match-setup.md), [CONCEPT §3.3 lineages](../CONCEPT.md), [CONCEPT §3.4 unit categories](../CONCEPT.md), [CONCEPT §4.4 mobile units](../CONCEPT.md), [CONCEPT §4.6 economy](../CONCEPT.md), [CONCEPT §4.7 enemies](../CONCEPT.md)
**Downstream impact:** [Stage 05 — age evolution](05-age-evolution.md), [Stage 06 — hybrids & fusion](06-hybrids-fusion.md)
**Open questions:** See below.
**Research backing:** [01-genre-pulse.md](../research/01-genre-pulse.md)
**Last reviewed:** 2026-04-26

---

## Amendment 2026-04-26 (stub-level — real-cultures frame cascade)

Per [`decisions/2026-04-25-q2-real-cultures-direction-ratified.md`](../decisions/2026-04-25-q2-real-cultures-direction-ratified.md) (Reversibility **Hard**), [`decisions/2026-04-26-attack-type-mapping.md`](../decisions/2026-04-26-attack-type-mapping.md) (Reversibility Medium), and [`decisions/2026-04-26-phase-1-exit-one-pager.md`](../decisions/2026-04-26-phase-1-exit-one-pager.md) — the 3-lineage + 3-tier (Dust/Form/Apotheosis) framings from the 2026-04-22 amendment below are **superseded** by the **4-tier ladder + Fusion endgame** (T1 swarm → T2 mainline → T3 elite → T4 Demigod/Hero → Fusion → God) and the **3-civilization** (Greek/Aztec/Norse) content skeleton. Under the new shape:

- Scope bullet "gameplay within a single age / tier" should read **within a single tier of the 4-tier ladder**. Match is 30 waves, mini-boss at 5/15/25, main-boss at 10/20/30.
- Economy mapping is **Tribute (primary) + Divinity (6-cap mythic token)** per [`concept/phase-4.md §4.6`](../concept/phase-4.md) — Gold/Faith/Cinders [PROPOSAL] is superseded. Tribute is earned from kills + passive trickle and spent on units/towers/merges; Divinity is earned 1 per boss round, capped at 6, and spent only on Fusion (2 to unlock civ-wide Fusion menu + 1 per fusion execution).
- Damage resolution now reads through the **7-type × 5-armor RPS matrix** per the attack-type decision — towers have a single primary attack type, Gods are the only 2-type damage sources (inherit both source Demigod types). Per-type light status procs apply (Fire=burn, Poison=stacking DoT, Piercing=armor-shred, Slashing=bleed, Crushing=stagger, Arcane=slow/debuff, Divine=consecrate).
- Enemy ontology is still OPEN (2026-04-25 Follow-up #9) under the real-cultures frame; myth-creature PvE bosses parked (Follow-up #3). PvP regular waves use a shared cross-cultural pool with civ-matched bosses at 5/10/15/20/25/30 per [`concept/phase-4.md §4.7`](../concept/phase-4.md).
- Verification "first Tier Gate" framing now maps to **T1→T2, T2→T3, T3→T4**, plus the **Fusion event** (trailer beat, not a gate). Civilization-persistence feeling by end of T3 is the core MVP bar per [`concept/phase-6.md §6.4`](../concept/phase-6.md).

Body below is preserved for traceability; dedicated Stage-04 rewrite deferred to a future reopen. §5.4 naming conventions **[LOCKED]** untouched. §2.4a accessibility floor **[LOCKED]** untouched.

---

## Amendment 2026-04-22 (stub-level, deferred from plan A7) — SUPERSEDED BY 2026-04-26

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
