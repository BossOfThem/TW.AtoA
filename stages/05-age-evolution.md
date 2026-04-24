# Stage 05 — Age Evolution

**Status:** Stub
**Phase in CONCEPT cascade:** 3 (Design) / 4 (Specification — divergence system)
**Upstream deps:** [Stage 04 — in-match core](04-in-match-core.md), [CONCEPT §3.5 three tiers (Dust/Form/Apotheosis)](../CONCEPT.md), [CONCEPT §4.2 Divergence system](../CONCEPT.md)
**Downstream impact:** [Stage 06 — hybrids & fusion](06-hybrids-fusion.md), [Stage 07 — match end](07-match-end.md)
**Open questions:** See below.
**Research backing:** [02-theme-era.md](../research/02-theme-era.md) — the era spine decision fully lands here.
**Last reviewed:** 2026-04-26

---

## Amendment 2026-04-26 (stub-level — real-cultures frame cascade)

Per [`decisions/2026-04-25-q2-real-cultures-direction-ratified.md`](../decisions/2026-04-25-q2-real-cultures-direction-ratified.md) (Reversibility **Hard**) + [`decisions/2026-04-26-phase-1-exit-one-pager.md`](../decisions/2026-04-26-phase-1-exit-one-pager.md) — the 3-tier (Dust/Form/Apotheosis) dungeon-cosmology framing from the 2026-04-21 amendment below is **superseded** by the **4-tier ladder + Fusion endgame** (T1 swarm → T2 mainline → T3 elite → T4 Demigod/Hero → Fusion → God). Under the new shape:

- This stage's subject is now more accurately "**tier evolution + Fusion event**" than "age evolution." The title is kept for file-path stability; body rewrite belongs to a dedicated Stage-05 reopen.
- Tier-transition gates are now **T1→T2, T2→T3, T3→T4**, plus the **Fusion event** which is trailer-beat rather than tier-gate (2 T4 Demigods → 1 God via locked recipe, consumed into one board slot).
- Divergence forks move to **T2→T3 and T3→T4** per [`concept/phase-4.md §4.2`](../concept/phase-4.md) — T2→T3 picks between two T3 elite variants; T3→T4 is reframed as a Demigod-pair emphasis that nudges Fusion reachability.
- "Tier-persistence" feeling is subsumed into the stronger **civilization-persistence** delighter — a Greek match feels Greek from minute 1 through final Fusion. Per `concept/phase-6.md §6.4` 50%+ of MVP playtesters must report civilization-persistence by end of T3.
- Dungeon-cosmology aesthetic (mysterious / descending / unexplained) is **superseded**. Aesthetic is now **real cultures + native myth** (Greek / Aztec / Norse) with the "mundane outside, myth inside" tower-label heuristic — T1-T3 tower labels are mundane historical building types; mythic identity lives in stats/behaviors/upgrades/flavor/Fusion outputs.
- [`decisions/2026-04-20-age-history-flavor-mapmods.md`](../decisions/2026-04-20-age-history-flavor-mapmods.md) is **re-rebased** (not superseded) as of 2026-04-26 — banner-mechanic applies at Tier Gates + Fusion events; `ages.json` data reinterprets per-civ; PvE campaign AGES is proper home for expanded age-as-history (Follow-up #8, parked).
- The [`decisions/2026-04-26-attack-type-mapping.md`](../decisions/2026-04-26-attack-type-mapping.md) 7-type × 5-armor matrix is the live combat surface across all tiers; Gods are the only 2-type damage sources, inheriting both source Demigod types.

Body below is preserved for traceability; dedicated Stage-05 rewrite deferred. §5.4 naming conventions **[LOCKED]** untouched. §2.4a accessibility floor **[LOCKED]** untouched.

---

## Amendment 2026-04-21 (stub-level) — SUPERSEDED BY 2026-04-26

Upstream Phase 3 §3.5 collapsed from **11 civilizational ages** (Primal → Ascendant) to **3 tiers** — **Dust / Form / Apotheosis** — under an **Ash→Altar dungeon-cosmology arc** per [2026-04-21 concept tightening](../decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md) (Reversibility Hard). Consequences for this stage:
- Scope bullets referencing "age 1" / "age 6" / "age 6–8" / "age 9–10" / "age 10–11" are **obsolete**; under the new shape there are at most 3 tiers and at most 2 tier-transition gates (Dust→Form, Form→Apotheosis).
- Divergence fork placeholders (Steamheart / Atomic / Synthetic / Stellar) are **superseded** by the rescoped Phase 4 §4.2 fork model (at most 2 tier-transition forks, themes OPEN).
- Open question "Number of ages — eleven is placeholder; may collapse to nine" is **closed** — ratified at 3 tiers.
- Open question "Fork count — four is placeholder" is **closed** — at most 2.
- The "age-persistence" feeling rephrases to **tier-persistence** (same minute-1-matters invariant, compressed arc).
- Era-spine decision in [research/02-theme-era.md](../research/02-theme-era.md) is **constrained** by the PM-locked dungeon-cosmology aesthetic (mysterious, descending, unexplained) — classical→posthuman / tech-timeline framings no longer qualify.
- [2026-04-20 age-history flavor + mapmods](../decisions/2026-04-20-age-history-flavor-mapmods.md) is **rebased** (not superseded): age-gate logic survives; `ages.json` data collapses 11→3 in Step B prototype reshape.

Remaining content below is preserved for traceability; a dedicated Stage-05 rewrite happens when this stage is next opened in a Phase-C pass (this session's scope is stub-level only per plan A7). Names Dust / Form / Apotheosis are prose placeholders — `concept/phase-5.md §5.4 [LOCKED]` is untouched.

---

## Scope

The core delighter of the game. Covers:

- Age Gate trigger conditions (wave count vs timer, per mode).
- Gate UX — pause, dim, voice line, tower auto-upgrade animation.
- Divergence Forks (placeholder: Steamheart, Atomic, Synthetic, Stellar) — 2–3 choices per fork.
- Tower carry-over — how the tower you built in age 1 is visually/mechanically the same tower in age 6.
- Age-persistence callback — the "this still feels like my opening choice" moment.
- New unit/tower unlocks revealed at each gate.
- Max age reached per mode (solo TD caps at 6–8, ranked at 9–10, endgame at 10–11).

## To be written (Phase C pass)

Second-longest stage after Stage 04. The era-spine decision from [02-theme-era.md](../research/02-theme-era.md) drives everything here — age names, visual identity, fork framing, boss-wave identity.

## Open questions (seed list)

- Era spine — classical→posthuman, myth-forward, collapse-and-rebuild, or hybrid. (Research-gated.)
- Number of ages — eleven is placeholder; may collapse to nine.
- Fork count — four is placeholder; may collapse to three.
- Fork reversibility — one-way or can a late-match choice reshape an earlier fork.
- Age Gate length — brief pause or a longer "upgrade ceremony" moment.

## Verification

- 50%+ of playtesters report the age-persistence feeling by age 4 or 5.
- Fork choices feel mechanically distinct, not cosmetic reskins.
- Age Gate pacing does not break flow — pause is long enough to breathe, short enough to stay engaged.
