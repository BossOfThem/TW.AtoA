# Decision — Per-civ specialization sub-pass: 3-round per-civ axis + 5-field schema

**Date:** 2026-05-06
**Status:** Accepted
**Reversibility:** Medium
**Affects:** [`concept/phase-4.md`](../concept/phase-4.md) (`§4.10` 7-attack × 5-armor RPS matrix — read-only inputs; `§4.11` Numbers floor — read-only inputs; `§4.6` economy — read-only inputs; `§4.8` exit-gate — possible item add at RN; civ-identity body to be added at RN), [`decisions/2026-04-26-attack-type-mapping.md`](2026-04-26-attack-type-mapping.md) (locked attack-type taxonomy + status-proc bindings — read-only inputs), [`decisions/2026-05-05-per-commander-r5-audit-and-arc-close.md`](2026-05-05-per-commander-r5-audit-and-arc-close.md) (lane locks Hard reversibility — read-only inputs), [`decisions/2026-05-06-per-tower-rn-cross-civ-audit-and-arc-close.md`](2026-05-06-per-tower-rn-cross-civ-audit-and-arc-close.md) (45-tower magnitude matrix + per-civ falsifiable signatures — read-only inputs)

---

## Decision

Open a **3-round per-civ specialization sub-pass** (plus 1 closing round) to bind five mechanical-content fields per civilization for the three locked civs (Greek / Aztec / Norse).

**Round-queue axis: per-civ deep-dive (Axis A).** R2 Greek / R3 Aztec / R4 Norse / RN cross-civ specialization audit. Mirrors the per-tower R1 axis pick (PM-ratified 2026-05-06): civ-archetype held constant per round, civ-identity profile coheres in-round, smallest queue (4) preserving RN audit discipline.

**Per-civ schema (locked for the arc, all 5 fields):**

| # | Field | Source | Authoring discipline |
|---|-------|--------|----------------------|
| 1 | `matchup_affinity` | §4.10 7-attack × 5-armor RPS matrix (locked) + per-tower RN type-coverage audit | Civ's aggregate matchup profile against the 5 armor classes (Unarmored / Shielded / Heavy / Magic / Boss). Bins per civ: which armor classes the civ's 15-tower roster favors (1.25× cells dominant), which it punishes itself against (0.75× cells dominant), which it neutrals (1.00× cells dominant). Aggregate not per-tower — per-tower magnitudes are bound at per-tower R2-RN. |
| 2 | `identity_hook` | per-commander R5 lane locks (Hard) + per-tower RN civ-archetype signatures (Greek=mid-cd / mid-range / lockdown-procs; Aztec=fast-cd / mid-range / compounding-DoT-procs; Norse=fastest-cd / shortest-range / Bleed-density-cleave) | One-paragraph mechanical thesis tying lane lock + per-tower magnitude signature + status-proc archetype + commander synergy into a single legible identity statement. Civ-neutral effect-type language; no art / VFX / civ-flavor surface direction prose (Follow-up #5 hard-gate). |
| 3 | `signature_creep_types` | §4.10 5-armor RPS classes (locked) + civ's matchup_affinity bins | Armor-class bin(s) the civ specializes against (i.e., where its strongest matchup cells cluster). Pre-§4.7-lock: archetype-grain only, not per-creep-row. Authored from §4.10 5-armor substrate + RN type-coverage audit; does not depend on §4.7 enemy direction lock (which remains OPEN). |
| 4 | `multi_civ_play_hook` | per-tower RN type-coverage audit (Greek lacks Poison; Aztec lacks Crushing; Norse lacks Poison + Divine T1-T3) | The civ's structural type-hole(s) — the matchup bins it is empirically *weakest* in due to type-coverage gaps. Bound at the launch-roster grain (does not include patch-1 commander expansions). Cross-references the locked civ-pair Foresight-coin model (deferred, §4.x) and patch-1 commander Follow-up #6 (deferred). |
| 5 | `commander_synergy` | per-commander R5 lane locks (Hard) + per-tower RN affinity-target tag distribution (45/45 verbatim match) | One-sentence statement of how the civ's lane-locked commander (Leonidas / Montezuma II / Ragnar) interfaces with the civ's per-tower magnitude signature to amplify the identity_hook. Mechanical-content only; commander narrative remains in per-commander R5 one-pagers. |

**Locked surfaces carry forward unchanged.** §5.4 [LOCKED] is untouched. §2.4a [LOCKED] is untouched. The 17-item conceptual frame (a)-(r)+(s) is read-only input. All R1-R7 CONCEPT amendment-pass §-anchors are read-only input. All per-commander R1-R5 spine-doc edits are read-only input. All per-tower R1-RN magnitude bindings are read-only input. **2026-04-25 locked content-skeleton names verbatim — civ names + tower names + commander names appear unchanged.**

The arc opens immediately. PM autonomy mandate from 2026-05-05 carries forward — surface AskUserQuestion only on genuine forks / scope expansion / cascade-violation risk / cultural-sensitivity surface (Follow-up #5) / handoff trigger.

## Context

Five load-bearing surfaces converge on this arc:

1. **§4.10 7-attack × 5-armor RPS matrix** binds the matchup substrate globally (0.75× / 1.00× / 1.25× cells across 35 type-armor pairs). Per-civ aggregation against this matrix has been deferred to a per-civ specialization sub-pass — this arc is the named owner of that deferral.
2. **Per-commander R5 lane locks (Hard)** — Leonidas=Control / Montezuma II=Economy / Ragnar=Summon — bind the *interface side* of civ identity. Per-civ specialization aggregates the *target side* across the civ's 15-tower roster.
3. **Per-tower RN cross-civ audit** delivered the empirical per-civ magnitude signatures (Greek lockdown / Aztec compounding-DoT / Norse Bleed-density-cleave). Per-civ specialization translates those signatures into civ-level identity statements + matchup-affinity bins + multi-civ-play type-coverage hooks.
4. **§4.7 enemy direction lock (OPEN)** binds the wave-composition variance mandate downstream of this arc. This arc explicitly stops at the §4.10 5-armor archetype-grain — `signature_creep_types` is bound at the armor-class grain, not the per-creep-row grain. §4.7 lock will further specify which creep families occupy each armor-class bin; per-civ specialization remains stable across that downstream lock.
5. **Cultural-sensitivity Follow-up #5** hard-gates art / VFX / civ-flavor surface direction. This arc is **mechanical-content only** — civ-neutral effect-type language throughout. Locked content-skeleton names verbatim only; no surface direction prose.

The CONCEPT amendment pass closed the §-anchor gap. The Numbers-phase closed the magnitude floors. The per-commander arc closed the interface-side affinity hooks. The per-tower arc closed the 45-tower magnitude matrix. Per-civ specialization is the next legible-at-civ-grain consolidation — banking three civ-identity profiles that aggregate the per-tower + per-commander outputs into civ-level matchup, identity, and multi-civ-play statements.

## Alternatives considered

- **Axis A — per-civ deep-dive (chosen).** R2 Greek / R3 Aztec / R4 Norse / RN audit. Civ-identity coheres per round; smallest authoring queue (3 rounds + RN); mirrors per-tower R1 + per-commander R1-R5 arc shapes; per-civ identity_hook prose can be written holistically in-round with all 15 per-tower magnitudes + lane lock + status-proc signature held in view simultaneously.
- **Axis B — per-axis cross-civ.** R2 matchup-affinity-all-3 / R3 identity-hook-all-3 / R4 signature-creep-all-3 / RN. **Rejected:** 4 authoring rounds (vs. Axis A's 3) for cross-civ comparative coherence that RN audit recovers in 1. Civ-identity prose fragments across 4 rounds — identity_hook depends on matchup_affinity + signature_creep_types + commander_synergy in synthesis, not in isolation. Authoring identity_hook for Greek in R3 without Greek's signature_creep_types yet bound (R4) inverts the natural reasoning order.
- **Axis C — single condensed round.** One decision file with all 3 civs across all 5 fields. **Rejected:** Loses per-civ 3x debug discipline (each civ's identity_hook deserves its own loop, not a shared one). Risks scope-creep into Follow-up #5 art surface — three civs' worth of mechanical prose authored in one round under context pressure tempts shorthand that drifts into VFX / pose / VO direction. The per-tower arc explicitly used per-civ rounds with Follow-up #5 deferral; per-civ specialization (which engages closer to art surface) needs equal or stronger discipline.

## Reason chosen

**Axis A — per-civ deep-dive.** Three reinforcing reasons:

1. **Identity-hook synthesis requires civ-archetype held constant.** A civ's identity_hook integrates matchup_affinity + signature_creep_types + commander_synergy + per-tower magnitude signature into a single one-paragraph statement. Per-civ rounds hold the civ-archetype constant across all 5 fields per round, allowing the synthesis to land in a single authoring pass. Per-axis rounds (Axis B) fragment the synthesis across 4 rounds where the dependencies between fields cross round boundaries.
2. **Cross-arc parity with per-tower R1 + per-commander R1-R5.** Per-commander shipped 5 rounds (R1 scope + R2-R4 effect-type variants + R5 audit-close). Per-tower shipped 4 rounds (R1 scope + R2-R4 civ rosters + RN audit-close). Per-civ specialization shipping 4 rounds (R1 scope + R2-R4 civ profiles + RN audit-close) keeps the arc-shape rhythm legible across the Phase 4 spine.
3. **Smallest queue that preserves audit discipline.** Axis B costs 4 authoring rounds for cross-civ parity that Axis A's RN audit recovers in 1. Axis C decoheres per-civ 3x discipline. Axis A is 3 authoring rounds + RN. The 5-field schema is held constant across R2-R4 for cross-civ row-by-row comparison at RN.

### 3x debug loop on axis

**Loop 1 — aggressive critique.** Per-civ axis fragments cross-civ parity. A reader auditing matchup_affinity across the three civs (e.g., "do all three civs have a signature creep-type they specialize against?") must read R2 Greek + R3 Aztec + R4 Norse and reconstruct the cross-civ matchup picture from 3 sources, then audit at RN. Axis B (per-axis) authors all three matchup_affinity rows in one round, where cross-civ parity surfaces inside one decision file. Axis A defers parity to RN where mis-balance (e.g., two civs both specialize against the same armor class, leaving a third class uncovered) surfaces as rework spread across 3 prior rounds. Furthermore, the identity_hook-synthesis-needs-civ-archetype-constant argument (Reason chosen #1) presumes the 5 fields are *tightly coupled per civ*; if they aren't (e.g., if Greek matchup_affinity and Greek commander_synergy can be authored independently), per-civ grain over-constrains the authoring rhythm.

**Loop 2 — steelman.** Cross-civ parity (Loop-1 critique #1) is what the RN audit *exists* to deliver. Per-tower RN already validated the per-civ-rounds + RN-audit pattern — three civs' worth of magnitudes audited in one matrix at RN with zero cascade-violations. Per-civ specialization's RN audit follows the same pattern: 3 civs × 5 fields = 15 cells, audited in one matrix. Reader experience during the arc is "civ-by-civ profile authoring in progress" — the cross-civ parity audit (RN deliverable) is the readable artifact. The 5-fields-tightly-coupled presumption (Loop-1 critique #2) is grounded: identity_hook is *defined* as the synthesis of the other 4 fields, so per-civ grain is structurally required. matchup_affinity + signature_creep_types are tightly coupled (both bin against the same §4.10 5-armor substrate). multi_civ_play_hook is the *complement* of matchup_affinity (the type-holes the civ has). commander_synergy ties identity_hook back to the per-commander R5 lane lock. Authoring these 5 fields per civ in isolation — without the other 4 fields' values — would force placeholder authoring and rework.

**Loop 3 — synthesis.** Axis A is correct for *authoring discipline* (5-fields-tightly-coupled-per-civ; identity_hook synthesis needs civ-archetype constant) but Loop-1 names a real cross-civ parity reader-experience cost that the RN audit mitigates only at the close. Mitigation: each per-civ round (R2-R4) closes with a brief **cross-civ parity hook paragraph** (one paragraph forward-pointing to the next round's expected divergence — e.g., R2 Greek closes with "Aztec's compounding-DoT signature predicts Aztec matchup_affinity favors Magic-armor + Boss-armor through Poison-stacking + Sun Offering Fire-splash; R3 will test this prediction"). Cross-civ parity discipline builds incrementally; RN integrates the three per-civ rounds into the cross-civ × cross-field audit matrix as the integration artifact.

**Synthesis-locked output:** Axis A with embedded cross-civ parity hook paragraphs at the close of R2 / R3 / R4. RN integrates cross-civ × cross-field into a 5×3 audit matrix.

## §-placement table (locked)

| Source | Target § | Round |
|--------|----------|-------|
| Per-civ specialization profile for Greek: 5 fields (matchup_affinity / identity_hook / signature_creep_types / multi_civ_play_hook / commander_synergy). Cross-civ parity hook paragraph at close. | New `decisions/2026-05-06-per-civ-r2-greek-profile.md` (mechanical-content); §4.x untouched until RN | 2 |
| Per-civ specialization profile for Aztec: same 5-field schema. Cross-civ parity hook at close. | New `decisions/2026-05-06-per-civ-r3-aztec-profile.md`; §4.x untouched until RN | 3 |
| Per-civ specialization profile for Norse: same 5-field schema. Cross-civ parity hook at close. | New `decisions/2026-05-06-per-civ-r4-norse-profile.md`; §4.x untouched until RN | 4 |
| Cross-civ × cross-field audit (5-field × 3-civ matrix; matchup_affinity coverage check; signature_creep_types non-overlap check; multi_civ_play_hook complementarity check; commander_synergy lane-lock parity) + new `phase-4.md §4.x` per-civ specialization body cross-linking R2-R4 + possible §4.8 exit-gate item add | `phase-4.md §4.x` body added (cross-link to R2-R4) + possible `§4.8` item add + new `decisions/2026-05-06-per-civ-rn-audit-and-arc-close.md` | 5 (RN) |

## Round queue (locked)

1. **Round 1 (this file)** — scope decision + axis 3x debug loop + 5-field schema lock + §-placement table + 4-round queue.
2. **Round 2** — Greek profile: 5 fields. Civ-identity hook prose synthesizing Leonidas Control + per-tower lockdown signature. Cross-civ parity hook to R3 Aztec.
3. **Round 3** — Aztec profile: 5 fields. Civ-identity hook prose synthesizing Montezuma II Economy + per-tower compounding-DoT signature. Cross-civ parity hook to R4 Norse.
4. **Round 4** — Norse profile: 5 fields. Civ-identity hook prose synthesizing Ragnar Summon + per-tower Bleed-density-cleave signature. Cross-civ parity hook to RN.
5. **Round 5 (RN — CLOSES arc)** — cross-civ × cross-field audit matrix + `phase-4.md §4.x` per-civ specialization body + possible `§4.8` exit-gate item add. CASCADE pointer + decisions table + version footer bump. Dual-push closes arc.

Dual-push points: after R2 (carries R1+R2), after R3 (carries R3), after RN (carries R4+RN + closes arc). Cascade-lint after every round.

## Reversibility note

**Medium.** Each round produces a decision file with mechanical-content for one civ across 5 fields; the RN spine-doc edit adds the cross-link body to `phase-4.md` and possibly an `§4.8` exit-gate item. Reverting requires:

1. Superseding decision entry per round to be reverted (re-opens 5 fields for that civ).
2. RN spine-doc edits reverted (remove per-civ specialization body cross-link from `phase-4.md`; un-add `§4.8` item if added).
3. Cross-arc parity to per-commander R1-R5 lane locks + per-tower R1-RN magnitude matrix re-validated if any field crosses an upstream lock.

Each reversal is a single decision file + bounded edits. The 17-item frame, Numbers-phase magnitudes, 2026-04-26 attack-type lock, per-commander R1-R5 lane locks, and per-tower R1-RN magnitude matrix are *not* under negotiation.

**Hard-class risks (explicit guards):**

- **§5.4 [LOCKED] / §2.4a [LOCKED]** — every round verifies untouched headers before commit. **Cultural-sensitivity Follow-up #5 hard-gates art / VFX / civ-flavor surface direction prose.** This arc is mechanical-content only. Civ-neutral effect-type language throughout.
- **2026-04-25 locked content skeleton** — every round verifies the civ + tower + commander content-skeleton names appear verbatim; any rephrasing is a cascade violation.
- **2026-04-26 attack-type lock** — every round's status-proc references verbatim-confirm the locked taxonomy mapping; any deviation requires a superseding decision against 2026-04-26.
- **2026-05-05 R5 baseline DPS ladder** — this arc does not author dps; per-tower R1-RN bound it. Any reference uses the locked ladder verbatim.
- **Per-commander R1-R5 lane locks (Hard)** — every round's commander_synergy field resolves cleanly to the civ's locked lane (Greek=Control via Leonidas / Aztec=Economy via Montezuma II / Norse=Summon via Ragnar); cross-civ commander synergy (e.g., Leonidas tagged on Aztec profile) is a cascade violation.
- **Per-tower R1-RN magnitude matrix** — every round's matchup_affinity + signature_creep_types reference the per-tower RN type-coverage audit verbatim; any deviation requires a superseding decision against per-tower RN.
- **§4.7 enemy direction (OPEN)** — `signature_creep_types` is bound at §4.10 5-armor archetype-grain only; per-creep-row specifics defer to §4.7 lock. Any per-creep-row authoring in this arc is scope creep flagged for handoff.

## Follow-ups

- **R2 onward** runs autonomously per 2026-05-05 PM autonomy mandate. Surface AskUserQuestion only on genuine forks / scope expansion / cascade-violation risk / cultural-sensitivity surface (Follow-up #5) / handoff trigger.
- **Cascade-lint** after every round.
- **Dual-push** at the three checkpoints (after R2, after R3, after RN).
- **Cross-arc dependency on per-tower R1-RN** — every per-civ row's matchup_affinity + signature_creep_types + multi_civ_play_hook references the per-tower RN type-coverage audit + status-proc-density audit. Any divergence is a cascade violation flagged in-round.
- **Cross-arc dependency on per-commander R5** — every per-civ row's commander_synergy + identity_hook references the per-commander R5 one-pagers + lane locks. Any divergence is a cascade violation flagged in-round.
- **Cultural-sensitivity Follow-up #5** continues to gate art / VFX / civ-flavor surface direction. This arc explicitly defers all visual / tonal direction prose to the Follow-up #5 pass; mechanical-content uses civ-neutral effect-type language.
- **§4.7 enemy direction lock (OPEN)** — downstream of this arc's signature_creep_types archetype-grain output. Future §4.7 lock can refine signature_creep_types to per-creep-row specifics without superseding this arc; cross-arc parity guaranteed by both sides referencing §4.10 5-armor classes.
- **Follow-up #6 Patch-1 commanders** stays parked. This arc binds within-launch-roster only (3 civs). Patch-1 expansions are downstream — multi_civ_play_hook explicitly notes the deferred Foresight-coin / patch-1-commander expansion path.
- **`research/06-tw-subgenres.md` / `admin/concept.json` migration** — both stay deferred (separate post-arc tracks, unchanged from prior handoff).
