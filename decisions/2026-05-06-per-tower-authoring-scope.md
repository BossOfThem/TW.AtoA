# Decision — Per-tower authoring sub-pass: 3-round per-civ axis + 7-field schema

**Date:** 2026-05-06
**Status:** Accepted
**Reversibility:** Medium
**Affects:** [`concept/phase-4.md`](../concept/phase-4.md) (`§4.10` variable nomenclature — read-only inputs; `§4.11` Numbers floor — read-only inputs; `§4.6` economy — read-only inputs; `§4.6a` aux catalog — read-only inputs; `§4.8` exit-condition tick at RN; per-tower mechanical-content body to be added at RN), [`decisions/2026-04-26-attack-type-mapping.md`](2026-04-26-attack-type-mapping.md) (locked attack-type + RPS + status-proc table — read-only inputs), [`decisions/2026-05-05-balance-pass-2-round-5-tower-baselines.md`](2026-05-05-balance-pass-2-round-5-tower-baselines.md) (locked DPS ladder + tier-up costs — read-only inputs)

---

## Decision

Open a **3-round per-tower authoring sub-pass** (plus 1 closing round) to bind seven mechanical fields across the **45 launch towers** (18 T1-T3 mainline + 18 T4 Demigod + 9 God) of the three locked civilizations (Greek / Aztec / Norse).

**Round-queue axis: per-civ across tiers (Axis A).** R2 Greek (15 towers: 6 T1-T3 + 6 T4 Demigod + 3 God) / R3 Aztec (15) / R4 Norse (15). RN closes the arc with cross-civ parity audit + spine-doc edits + Phase-4 exit-gate progress.

**Per-tower schema (locked for the arc, all 7 fields):**

| # | Field | Source | Authoring discipline |
|---|-------|--------|----------------------|
| 1 | `attack_type` | 2026-04-26 mapping (locked) | **Confirms** existing binding per the locked 7-type taxonomy (Piercing / Slashing / Crushing / Fire / Poison / Arcane / Divine). Any deviation is a cascade violation requiring a superseding decision against 2026-04-26. |
| 2 | `cd` | §4.10 (g) base attack cooldown / §4.11 magnitudes | Base attack cadence in seconds. Authored within ±20% of tier-archetype default unless civ-identity hook justifies wider variance (flagged in `notes`). |
| 3 | `range` | §4.10 (j) engagement radius / §4.11.4 ε=0.6 default | Engagement radius in cells. Authored within tier-archetype band; per-map ε=0.6 default applies when range × cell-density yields engagement-time integral. |
| 4 | `status_proc` | 2026-04-26 status-proc table | Primary proc (slow / DoT / armor-shred / stun / knockback / none) + intensity tier. Inherits 2026-04-26 lock; this arc binds magnitude/duration only, never re-assigns the proc kind. |
| 5 | `dps` | 2026-05-05 R5 baseline ladder (T1=20 / T2=60 / T3=180 / T4=540 / God=1080 dmg/sec Standard) | Per-tower variance ±20% band of tier baseline. Civ-archetype roles (e.g., Greek mainline lockdown / Aztec yield-stack / Norse summon-anchor) drive variance direction, not magnitude. |
| 6 | `aux_slot_compat` | §4.6a aux catalog (7-slot universal) | Subset of {Damage Bonus / Economy Bonus / Tower-count expansion / Send-Creeps / Call-for-Help / Maze Stone / [Universal slot]} the tower accepts. Default is full universal compat unless a civ-identity hook narrows it. |
| 7 | `notes` | (this arc) | Civ-identity hook (one phrase) + per-commander affinity-target tag (binds the per-commander R1-R5 arc's interface side: `controlled_by` / `economy_target` / `summon_anchor` per Leonidas / Montezuma II / Ragnar lane locks). |

**Locked content-skeleton names from 2026-04-25 ratification carry forward unchanged.** §5.4 [LOCKED] is untouched. §2.4a [LOCKED] is untouched. The 17-item conceptual frame (a)-(r)+(s) is read-only input. All R1-R7 CONCEPT amendment-pass §-anchors are read-only input. All per-commander R1-R5 spine-doc edits are read-only input (this arc binds the *target-tower-side* of the affinity hooks the per-commander arc bound on its interface side).

The arc opens immediately. PM autonomy mandate from 2026-05-05 carries forward — surface AskUserQuestion only on genuine forks / scope expansion / cascade-violation risk / cultural-sensitivity surface (Follow-up #5) / handoff trigger.

## Context

Three load-bearing surfaces converge on this arc:

1. **§4.11 Numbers floor** binds tier-archetype DPS / cd / range / speed magnitudes globally but explicitly defers per-tower variance to a per-tower authoring sub-pass. This arc is the named owner of that deferral.
2. **§4.10 Tower-vs-Unit math** binds the variable nomenclature (a)-(r)+(s) across the master DPS×integral equation. Per-tower authoring populates the per-tower-row instances of (g) cd / (j) range / (m)+(n) status-proc parameters / (c) dps that the master equation integrates over.
3. **2026-04-26 attack-type mapping** locks the attack_type column for all 45 towers globally. This arc *confirms* those bindings into the per-tower row format and authors the remaining 6 fields against them.
4. **§4.8 Phase 4 exit condition** lists "per-tower spec table populated for all 45 launch towers" as a downstream gate item (item #2 in the exit roster, behind item #1 — per-commander one-pagers, closed 2026-05-05). This arc closes that gate.

The CONCEPT amendment pass closed the §-anchor gap. The Numbers-phase closed the magnitude floors. The per-commander arc closed the interface-side affinity hooks. Per-tower authoring is now downstream of stable spine — the four surfaces above are the spec-floor inputs, not under negotiation.

**Cross-arc dependency.** Per-commander R1-R5 (closed 2026-05-05) bound the *interface side* of three affinity hooks: Leonidas Spartan-Training control-aura applies to *civ-matched towers* in 2-cell radius; Montezuma II Blood-Tribute economy-bonus applies to *Aztec towers* in aura; Ragnar Sons-of-Ragnar summon-anchor spawns from *anointed Norse tower*. The interface side specifies what *kind* of tower receives the hook; this arc specifies which *specific* towers receive the hook (via the `notes` field's per-commander affinity-target tag) and how the receiving tower's own magnitudes interact with the hook (e.g., a Greek T2 mainline with `cd: 1.2s` under 15% slow aura runs at `cd: 1.2s` against enemies slowed by 15%, with the slow itself owned by the commander aura, not the tower).

**Cultural-sensitivity gate (Follow-up #5).** This arc binds *mechanical content* (numbers / cooldowns / effect-type magnitudes / proc intensities). **Visual content** (tower silhouette / firing animation / projectile VFX / civ-flavor surface treatment) remains hard-gated by Follow-up #5 cultural-sensitivity pass. Mechanical-spec writing references the locked content-skeleton tower names verbatim and flags any prose that strays into visual / tonal direction (e.g., "Greek phalanx tower fires bronze-tipped spears" is out-of-scope; "Greek phalanx tower: cd 1.2s, range 4 cells, attack_type Piercing, status_proc none, dps 60, aux_slot_compat universal" is in-scope).

## Alternatives considered

- **Axis A — per-civ across tiers (chosen).** R2 Greek 15 / R3 Aztec 15 / R4 Norse 15 / RN audit + spine-doc. Civ identity coheres per round; smallest authoring queue (3 rounds + RN); mirrors the per-commander R1-R5 arc shape (per-commander identity rounds → cross-commander audit closer); allows civ-identity hooks (Greek lockdown / Aztec yield-stack / Norse summon-anchor) to drive per-tower variance direction in-round.
- **Axis B — per-tier across civs.** R2 T1 (9 towers) / R3 T2 (9) / R4 T3 (9) / R5 T4-Demigods (18) / R6 Gods (9) / RN audit + spine-doc. **Rejected:** 5 authoring rounds (vs. Axis A's 3) for a parity gain Axis A's RN audit recovers. Cross-tier civ-identity coherence fragments across 5 rounds; civ-identity hooks (the load-bearing variance driver per the per-commander arc's affinity-side lock) emerge only at the close of R6 + RN, where mis-assignment surfaces as rework spread across all 5 prior rounds. Furthermore, T4-Demigod and God towers carry per-civ mythic-identity weight (Leonidas's lane locks against Greek-civ summon-targets; Ragnar's signature spawns Heathen Warriors that path through Norse anchor towers) that Axis B's per-tier slicing dilutes.
- **Axis C — per-property across all towers.** R2 cd-all-45 / R3 range-all-45 / R4 attack-type-confirm + status-proc-all-45 / R5 aux-slot-compat-all-45 / RN audit. **Rejected:** property-consistency strong, but civ + tier identity weak per round (a single round authors `cd` across Greek phalanx + Aztec eagle-warrior + Norse housecarl + Greek temple-of-Apollo + Aztec serpent-tower + ...). Per-tower variance discipline (the ±20% band) collapses to per-property rather than per-civ, losing the civ-archetype-role driver. The arc would author 45 cd values without considering whether Greek lockdown civ-archetype calls for tighter cd-band than Norse summon-anchor civ-archetype.

## Reason chosen

**Axis A — per-civ across tiers.** Three reinforcing reasons:

1. **Civ-identity hooks are the load-bearing variance driver.** Per the per-commander R1-R5 lane locks (Leonidas=Control / Montezuma II=Economy / Ragnar=Summon, Hard reversibility), each civ has a characteristic mechanical signature that flows through its tower roster. Greek lockdown civ-archetype calls for moderate cd / wide range / status_proc bias toward control (slow / stun / armor-shred). Aztec yield-stack civ-archetype calls for moderate cd / moderate range / dps variance pulled toward T2-T3 mid-tier consolidation (where Blood-Tribute aura amortizes most). Norse summon-anchor civ-archetype calls for fast cd / short range / status_proc bias toward Bleed (matching Ragnar's signature DOT). Authoring all 15 towers of one civ in one round means the civ-archetype driver is held constant while tier-variance is authored within it — the natural authoring grain.
2. **Cross-arc parity with per-commander R1-R5 binding.** The per-commander arc shipped 5 rounds (R1 scope + R2-R4 authoring + R5 audit-close). This arc ships 4 rounds (R1 scope = this file + R2-R4 authoring + RN audit-close). The shape match makes the cross-arc dependency (per-commander affinity-hook interface-side ↔ per-tower target-side) trivially auditable: each per-commander arc round produced one decision file per slot across all 3 commanders; this arc's per-civ rounds produce one decision file per civ across all 5 tiers (T1+T2+T3+T4-Demigod+God). The 9-spec parity check at per-commander R5 has a natural mirror in the 15-spec parity check at this arc's RN.
3. **Smallest queue that preserves audit discipline.** Axis B costs 5 authoring rounds for parity that Axis A's RN audit recovers in 1. Axis C decoheres civ-identity entirely. Axis A is 3 authoring rounds + RN. Per the 2026-05-05 PM-autonomy-mandate "Numbers-phase pattern" precedent (10 Numbers-phase rounds + 7 CONCEPT-amendment-pass rounds + 5 per-commander rounds), this arc's 4-round queue is the natural shape for an authoring sub-pass downstream of stable spine.

### 3x debug loop on axis

**Loop 1 — aggressive critique.** Per-civ axis fragments tier-parity across rounds. A reader reviewing tier balance (e.g., "is T2 mainline correctly tuned across all 3 civs?") must read R2 Greek + R3 Aztec + R4 Norse decision files and reconstruct the cross-civ T2 picture from 3 sources, then audit at RN. Axis B (per-tier) authors all T2 in one round, where cross-civ parity surfaces inside one decision file. Axis A defers parity to RN where any mis-tuning surfaces as rework across 3 prior rounds. Furthermore, the civ-identity-hook argument (Reason chosen #1) presumes the hooks are *strong enough* to drive per-tower variance direction; if they aren't (e.g., if Greek phalanx and Norse housecarl both want fast cd / short range / Bleed proc despite different civ-archetypes), Axis A's grain is wrong and Axis B's tier-archetype grain is right. Per-tier authoring lets tier-archetype-as-driver emerge in-round; per-civ presumes civ-archetype-as-driver and would have to abandon its grain mid-arc if the presumption fails.

**Loop 2 — steelman.** Tier parity (Loop-1 critique #1) is what the RN audit *exists* to deliver. The arc isn't shipping per-tier demos round-by-round; it's authoring magnitudes that get cross-tier-audited at RN. Reader experience during the arc is "civ-by-civ spec authoring in progress" — not "demo each tier." A round-by-round reader expecting per-tier coherence is reading the wrong artifact; the cross-civ tier-balance audit (RN deliverable) is the readable artifact. The civ-archetype-as-driver presumption (Loop-1 critique #2) is *already* load-bearing: the per-commander R1-R5 arc *locked* civ-archetype as the variance driver via the lane locks (Leonidas=Control on Greek towers / Montezuma II=Economy on Aztec / Ragnar=Summon on Norse, Hard reversibility). Per-tower authoring downstream of that lock has civ-archetype-as-driver as a *spine-doc-locked input*, not a per-arc presumption. If civ-archetype turned out to be too weak a driver, the failure surface is upstream at the per-commander lane locks, not at the per-tower axis pick. Axis A is the natural downstream shape from the per-commander arc's locked civ-archetype direction.

**Loop 3 — synthesis.** Axis A is correct for *authoring discipline* (civ-archetype-as-driver is spine-doc-locked from the per-commander arc; civ-identity hooks coherent per round) but Loop-1 names a real cross-tier-parity reader-experience cost that the RN audit mitigates only at the close. Mitigation: each per-civ round (R2-R4) closes with a brief per-tier reading (one paragraph per tier T1/T2/T3/T4/God summarizing how the round's 15 towers fit the tier-archetype DPS-ladder + cd/range bands), so cross-tier parity discipline builds incrementally rather than landing in a single RN dump. RN then assembles the three per-civ rounds plus the per-round tier readings into the cross-civ × cross-tier audit matrix as the integration artifact. This combines Axis A's civ-coherence-per-round with Axis B's tier-coherence-across-rounds.

**Synthesis-locked output:** Axis A with embedded per-tier readings at the close of R2 / R3 / R4. RN integrates cross-civ × cross-tier into a 5×3 audit matrix.

## §-placement table (locked)

| Source | Target § | Round |
|--------|----------|-------|
| Per-tower mechanical specs for all 15 Greek towers (6 T1-T3 + 6 T4 Demigod + 3 God): 7 fields per row (attack_type confirmed / cd / range / status_proc / dps / aux_slot_compat / notes with civ-identity hook + per-commander affinity-target tag). Per-tier reading at close. | New `decisions/2026-05-06-per-tower-r2-greek-roster.md` (mechanical specs); §4.1 / §4.10 / §4.11 / §4.8 untouched until RN | 2 |
| Per-tower mechanical specs for all 15 Aztec towers (6 T1-T3 + 6 T4 Demigod + 3 God). Same 7-field schema. Per-tier reading at close. | New `decisions/2026-05-06-per-tower-r3-aztec-roster.md` (mechanical specs); §4.1 / §4.10 / §4.11 / §4.8 untouched until RN | 3 |
| Per-tower mechanical specs for all 15 Norse towers (6 T1-T3 + 6 T4 Demigod + 3 God). Same 7-field schema. Per-tier reading at close. | New `decisions/2026-05-06-per-tower-r4-norse-roster.md` (mechanical specs); §4.1 / §4.10 / §4.11 / §4.8 untouched until RN | 4 |
| Cross-civ × cross-tier audit (5-tier × 3-civ matrix; ±20% DPS-ladder band parity check; cd/range tier-archetype band parity check; status_proc civ-archetype consistency; aux_slot_compat coverage) + new §4.x per-tower spec body in `phase-4.md` cross-linking R2-R4 decision files + §4.8 exit-condition gate item #2 tick | `phase-4.md §4.x` body added (cross-link to R2-R4) + `§4.8` checkbox tick + new `decisions/2026-05-06-per-tower-r5-audit-and-spine-doc.md` | 5 (RN) |

## Round queue (locked)

1. **Round 1 (this file)** — scope decision + axis 3x debug loop + 7-field schema lock + §-placement table + 4-round queue.
2. **Round 2** — Greek roster: 15 towers × 7 fields. Civ-identity-hook prose: lockdown / control archetype. Per-commander affinity-target tags via Leonidas's `controlled_by` interface. Per-tier reading at close.
3. **Round 3** — Aztec roster: 15 towers × 7 fields. Civ-identity-hook prose: yield-stack / economy archetype. Per-commander affinity-target tags via Montezuma II's `economy_target` interface. Per-tier reading at close.
4. **Round 4** — Norse roster: 15 towers × 7 fields. Civ-identity-hook prose: summon-anchor archetype. Per-commander affinity-target tags via Ragnar's `summon_anchor` interface. Per-tier reading at close.
5. **Round 5 (RN — CLOSES arc)** — cross-civ × cross-tier audit matrix + `phase-4.md §4.x` per-tower spec body + §4.8 exit-condition gate item #2 tick. CASCADE pointer + decisions table + version footer bump. Dual-push closes arc.

Dual-push points: after R2 (carries R1+R2), after R3 (carries R3), after RN (carries R4+RN + closes arc). Cascade-lint after every round.

## Reversibility note

**Medium.** Each round produces a decision file with mechanical specs that bind 15 towers × 7 fields = 105 magnitude rows; the RN spine-doc edit adds the cross-link body to `phase-4.md` and ticks `§4.8` exit-gate item #2. Reverting requires:

1. Superseding decision entry per round to be reverted (re-opens 105 magnitude rows for that civ).
2. RN spine-doc edits reverted (remove per-tower spec body cross-link from `phase-4.md`; un-tick `§4.8` exit-gate item #2).
3. Cross-arc parity to per-commander R1-R5 affinity-target tags re-validated if any tag is removed.

Each reversal is a single decision file + bounded edits. The 17-item conceptual frame (a)-(r)+(s) is *not* under negotiation. The Numbers-phase magnitudes (DPS ladder, tier-up costs, cd/range/speed bounds) are *not* under negotiation. The 2026-04-26 attack-type mapping is *not* under negotiation. The per-commander R1-R5 lane locks are *not* under negotiation.

**Hard-class risks (explicit guards):**

- **§5.4 [LOCKED] / §2.4a [LOCKED]** — every round verifies untouched headers before commit. Cultural-sensitivity Follow-up #5 hard-gates art lock; this arc is mechanical-content only (no visual / VFX / civ-flavor surface direction prose).
- **2026-04-25 locked content skeleton** — every round verifies the 45 tower content-skeleton names appear verbatim in the new decision files; any rephrasing is a cascade violation.
- **2026-04-26 attack-type lock** — every round's `attack_type` column verbatim-confirms the locked taxonomy mapping; any deviation requires a superseding decision against 2026-04-26 (Reversibility Medium escalates to Hard).
- **2026-05-05 R5 baseline DPS ladder** — every per-tower `dps` is within ±20% of the tier baseline (T1=20 / T2=60 / T3=180 / T4=540 / God=1080). Any out-of-band magnitude requires cascade-violation flagging and a superseding decision against 2026-05-05 R5.
- **Per-commander R1-R5 lane locks (Hard reversibility)** — every per-commander affinity-target tag in `notes` resolves cleanly to one of the three locked lane interfaces (Control on Greek / Economy on Aztec / Summon on Norse); cross-civ affinity (e.g., Leonidas tagged on Aztec tower) is a cascade violation requiring escalation to PM.

## Follow-ups

- **R2 onward** runs autonomously per 2026-05-05 PM autonomy mandate. Surface AskUserQuestion only on genuine forks / scope expansion / cascade-violation risk / cultural-sensitivity surface (Follow-up #5) / handoff trigger.
- **Cascade-lint** after every round.
- **Dual-push** at the three checkpoints (after R2, after R3, after RN).
- **Cross-arc dependency on per-commander R1-R5** — every per-tower row's `notes` field carries the per-commander affinity-target tag (if applicable); the per-commander interface-side is locked, this arc owns target-side. Any divergence is a cascade violation flagged in-round.
- **Per-civ specialization sub-pass (post-arc track #2)** — owns civ-archetype matchup affinities (Greek vs. boss-archetype, Aztec vs. swarm-archetype, Norse vs. elite-archetype) downstream of this arc. Cross-arc parity guaranteed by both sides referencing the locked civ-archetype lanes.
- **Per-map / Round-11 mandate (post-arc track #3)** — consumes per-tower `range` × per-map ε=0.6 × good-cell coverage. Cross-arc parity guaranteed by both sides referencing §4.11.4 + this arc's range-band locks.
- **Cultural-sensitivity Follow-up #5** continues to gate art / VFX / civ-flavor surface direction. This arc explicitly defers all visual / tonal direction prose to the Follow-up #5 pass; mechanical specs use civ-neutral effect-type language.
- **Follow-up #6 Patch-1 commanders + Thor recipe-layer dissonance** stays parked. This arc binds within-launch-roster only (3 civs × 5 tiers × 3 entries-per-tier = 45 towers). Patch-1 expansions are downstream.
- **`research/06-tw-subgenres.md` / `admin/concept.json` migration** — both stay deferred (separate post-arc tracks, unchanged from prior handoff).
