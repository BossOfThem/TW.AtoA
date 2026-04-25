# Decision — Per-tower RN: cross-civ × cross-tier audit + arc close (CLOSES ARC 4/4)

**Date:** 2026-05-06
**Status:** Accepted
**Reversibility:** Medium
**Affects:** Closes per-tower authoring sub-pass (R1 scope + R2 Greek + R3 Aztec + R4 Norse). Spine docs — `concept/phase-4.md §4.8` (adds new exit-gate item for per-tower spec table populated, ticked DONE), `§4.11.5` (closing cross-reference to R2-R4 actuals). Decisions table + CASCADE pointer flip + version footer. Unblocks per-civ specialization / per-map authoring as next-track candidates per `HANDOFF.md` post-arc roadmap.

---

## Decision

RN closes the per-tower authoring sub-pass with three deliverables:

1. **Cross-civ × cross-tier audit** — sanity-check all 45 launch towers against the four locks (2026-04-26 attack-type mapping / 2026-05-05 R5 baseline DPS ladder ±20% / 2026-05-05 R5 status-proc kind binding / per-commander R1-R5 Hard-reversibility lane locks). All four pass.
2. **Per-civ falsifiable signature confirmation** — empirical test of the three signatures committed at R2/R3/R4 against the delivered tables. All three pass.
3. **Spine-doc edits + arc close** — `§4.8` adds + ticks new exit-gate item ("per-tower spec table populated for all 45 launch towers"); `§4.11.5` closing cross-reference to R2-R4 actuals; CASCADE pointer flips off the per-tower arc.

## Cross-civ × cross-tier statistical audit

### Inventory snapshot

45 launch towers = 3 civs × (6 T1-T3 mainline + 6 T4 Demigod + 3 God) = 3 × 15 = 45. T1-T3 mainline rows author 3 tier-states each via §4.11.5 merge-progression (single tower-line spans T1+T2+T3); T4 Demigod and God are single-tier rows. Total tier-state magnitudes: 3 × (6 × 3 + 6 + 3) = 3 × 27 = 81 dps cells, 45 cd values, 45 range values, 45 status-proc bindings, 45 lane-tags, 45 aux-compat entries, 45 attack-type bindings.

### Lock-conformance audit

| Lock | Source | Audit method | Result |
|---|---|---|---|
| **Attack-type taxonomy** | 2026-04-26 attack-type mapping | Verbatim string-match per tower across R2/R3/R4 row-1 against locked taxonomy + locked Fusion 2-type pairs | **45/45 verbatim match.** Zero deviation. |
| **DPS ladder ±20% band** | 2026-05-05 R5 baseline (T1=20 / T2=60 / T3=180 / T4=540 / God=1080) | Per-cell range-check: T1∈[16,24] / T2∈[48,72] / T3∈[144,216] / T4∈[432,648] / God∈[864,1296] | **81/81 in band.** Min: 18 (Greek/Norse T1 Mead Hall + Acropolis). Max: 1200 (Aztec God Huitzilopochtli, Nanahuatzin). All within ±20%. |
| **Status-proc kind binding** | 2026-04-26 status-proc table | Per-row check that proc kind matches attack_type binding (armor-shred↔Piercing / bleed↔Slashing / stagger↔Crushing / burn+splash↔Fire / toxin↔Poison / hex↔Arcane / smite↔Divine) | **45/45 match.** T4 intensity bumps follow Follow-up #4 rule (−1→−2 armor / 5%→7% bleed / 25%→30% stagger / 10%→12% smite / 25%→35% hex / 4s→5s toxin duration + 2%→3% per-stack). God-tier alternating-per-shot follows locked 2-type Fusion model. Zero deviation. |
| **Lane-tag** | per-commander R1-R5 Hard reversibility | Per-row check that tag matches civ (`controlled_by: leonidas` for Greek × 15 / `economy_target: montezuma_ii` for Aztec × 15 / `summon_anchor: ragnar` for Norse × 15) | **45/45 match.** Zero cross-civ pollution. |
| **aux_slot_compat** | §4.6a universal default | Per-row check | **45/45 universal.** No civ-identity-hook narrows the catalog at this arc per R1 scope. |

**Audit verdict: zero cascade-violation flags across 45 towers × 4 locks.** R1 scope's 7-field schema discipline holds end-to-end.

### Cross-civ band statistics

Per-tier per-civ medians (extracted from R2/R3/R4 tables; T1-T3 mainline values use median across 6 towers per tier):

| Tier | Greek dps median | Aztec dps median | Norse dps median | Greek cd median | Aztec cd median | Norse cd median | Greek range median | Aztec range median | Norse range median |
|---|---|---|---|---|---|---|---|---|---|
| T1 | 20 | 21 | 20 | 1.7s | 1.4s | 1.15s | 4.0 | 4.0 | 3.5 |
| T2 | 60 | 66 | 64 | 1.7s | 1.4s | 1.15s | 4.0 | 4.0 | 3.5 |
| T3 | 180 | 198 | 192 | 1.7s | 1.4s | 1.15s | 4.0 | 4.0 | 3.5 |
| T4 Demigod | 540 | 560 | 553 | 1.5s | 1.4s | 1.2s | 4.0 | 4.25 | 3.5 |
| God | 1080 | 1127 | 1087 | 1.6s | 1.45s | 1.1s | 5.0 | 4.5 | 4.0 |

**Reading:**
- **dps median order at every tier:** Aztec > Norse > Greek (Aztec elevated, Norse marginally above Greek baseline, Greek at-baseline).
- **cd median order at every tier:** Norse < Aztec < Greek (Norse fastest, Greek slowest).
- **range median order at every tier:** Norse < Greek = Aztec at T1-T3; Norse < Aztec ≤ Greek at T4-God (Greek God range 5.0 driven by Poseidon 5.5 outlier).
- **Three civs cluster around three orthogonal axes**: Greek = mid-cd / mid-range / centered-dps; Aztec = mid-cd-faster / mid-range / elevated-dps-mid-and-peak-tier; Norse = fast-cd / short-range / centered-dps.

### Status-proc density audit (Slashing-Bleed source count of 15 per civ)

| Civ | Mainline T1-T3 (of 6) | T4 Demigod (of 6) | God (of 3) | Total of 15 |
|---|---|---|---|---|
| Greek | 0 | 1 (Theseus) | 1 (Athena) | **2** |
| Aztec | 1 (Jaguar Warrior Hall) | 1 (Jaguar Champion) | 1 (Huitzilopochtli) | **3** |
| Norse | 2 (Longhouse + Berserker Lodge) | 2 (Björn Ironside + Lagertha) | 2 (Thor + Tyr) | **6** |

Norse Bleed-density 6/15 is the densest single-proc concentration in any civ — confirms R4's predicted Norse summon-cleave-Bleed-cascade signature. Greek Bleed-density 2/15 is the lightest (consistent with Greek lockdown's stun/slow/armor-shred-rich profile, not bleed-rich). Aztec Bleed-density 3/15 sits middle (Slashing is one of three Aztec compounding procs alongside Poison-stacking and Fire-splash).

### Type-coverage audit (per civ T1-T3 + T4 + God)

| Civ | Piercing | Slashing | Crushing | Fire | Poison | Arcane | Divine | Coverage |
|---|---|---|---|---|---|---|---|---|
| Greek | 3 (Phalanx + Trireme Dock + Achilles) | 2 (Theseus + Athena) | 2 (Acropolis + Hercules) | 1 (Colossus) | **0** | 2 (Oracle + Odysseus) | 4 (Parthenon + Perseus + Jason + Zeus) + Athena/Poseidon partial | **6 of 7** (Poison absent — multi-civ play hook) |
| Aztec | 2 (Eagle Warrior Hall + Eagle Champion) | 2 (Jaguar Warrior Hall + Jaguar Champion) | **0** | 2 (Temple of the Sun + Nanahuatzin) | 2 (Sacrificial Altar + Blood Priest) | 2 (Feathered Serpent Temple + Serpent-Priest) | 2 (Pyramid + High Priest-King) + Quetzalcoatl/Tezcatlipoca/Huitzilopochtli partial | **6 of 7** (Crushing absent — multi-civ play hook) |
| Norse | 2 (Longship Dock + Leif Erikson) | 2 (Longhouse + Berserker Lodge) at T1-T3 + 2 at T4 (Björn + Lagertha) | 2 (Mead Hall + Beowulf) | 2 (Forge + Sigurd) | **0** | 1 (Rune Stone) | 1 (Harald Bluetooth) at T4 only | **5 of 7** (Poison + Divine absent at T1-T3; Divine arrives at T4 — multi-civ play hook) |

Type-coverage gaps confirm phase-3 line 100 spec ("Greek lacks Slashing/Poison [at launch], Aztec lacks Crushing, Norse lacks Poison/Divine [at T1-T3 mainline]"). Greek Slashing arrives at T4 via Theseus; Norse Divine arrives at T4 via Harald Bluetooth. **Cross-civ play (patch-1 commanders + future Foresight-coin) is the design intent — type-holes are not bugs.**

## Per-civ falsifiable signature confirmation

R2 committed the falsifiable per-civ magnitude signature framework: each civ's `cd` / `range` / `dps` / `status-proc-density` profile should empirically distinguish from the other two civs in a way that maps to the per-commander R5 lane-lock identity (Greek=Control / Aztec=Economy / Norse=Summon).

### Signature 1 — Greek Control (committed R2)

**Predicted:** dps-band-centered (kinetic +10% / utility 0% or −10%) + cd-band-mid + lockdown-status-mix (slow + stun + armor-shred-rich).

**Delivered:**
- dps T1-T3 cluster 18-22 / 54-64 / 162-192; kinetic-type towers (Phalanx, Trireme Dock at +10%) and utility-type towers (Acropolis at −10%, Oracle/Colossus/Parthenon at baseline).
- cd mainline 0.8-2.4s, median 1.7s — mid-of-three-civs.
- range mainline 3-5 cells (mid 4.0); Poseidon God 5.5 longest in any civ.
- status-procs: Piercing armor-shred × 3, Crushing stagger × 2, Arcane hex × 2, Fire burn × 1, Divine smite × 4, Slashing bleed × 2 (T4-only). Lockdown procs (slow + stun + shred) dominate over DoT.

**Confirmation: PASS.** All four predicted axes match delivered.

### Signature 2 — Aztec Economy (committed R3)

**Predicted:** dps-band-high at T2-T3 (4 of 6 mainline at +10% baseline) + cd-band-faster-centered + Poison-stacking + Fire-splash + Slashing-bleed compounding for kill-multiplication.

**Delivered:**
- dps T1-T3 cluster 20-22 / 60-66 / 180-198; 4 of 6 mainline towers (Pyramid, Temple of the Sun, Jaguar Warrior Hall, Eagle Warrior Hall) at +10% baseline at T2-T3 (66 / 198); Sacrificial Altar + Feathered Serpent Temple at baseline. T4 Demigods 480-600. God-tier 1080-1200 (highest cluster across civs).
- cd mainline 0.9-2.0s, median 1.4s — faster-than-Greek center.
- Status-procs: Poison-stacking × 2 sources (Sacrificial Altar + Blood Priest — sole stacking proc per 2026-04-26 lock); Fire-splash × 2 (Temple of the Sun + Nanahuatzin); Slashing-bleed × 3 (Jaguar Warrior Hall + Jaguar Champion + Huitzilopochtli). Three compounding procs intersect inside Sun Offering 4-cell active zone for the kill-multiplication peak.

**Confirmation: PASS.** All three predicted axes match delivered. dps-band-high at T2-T3 + God-tier explicitly visible in the cross-civ snapshot table above.

### Signature 3 — Norse Summon (committed R4)

**Predicted:** cd-band-low + Bleed-density-high + dps-band-centered + range-band-short.

**Delivered:**
- cd mainline 0.8-1.8s, median 1.15s — fastest center across civs at every tier.
- Bleed-density 6 of 15 (Longhouse + Berserker Lodge + Björn Ironside + Lagertha + Thor + Tyr) — densest single-proc concentration across civs (vs Aztec 3, Greek 2).
- dps T1-T3 cluster 18-22 / 54-64 / 162-192; same ±10% kinetic-vs-utility pattern as Greek (Longhouse/Longship Dock/Berserker Lodge at +10%; Mead Hall at −10%; Rune Stone/Forge baseline). NOT mid-tier-elevated like Aztec. T4 Demigod 520-600; God-tier 1080-1100 (matches Greek's 1050-1100 cluster, not Aztec's elevated 1080-1200).
- range mainline 2.5-4.5 cells, median 3.5 — shortest center across civs at every tier; Berserker Lodge 2.5 melee-shortest in any civ.

**Confirmation: PASS.** All four predicted axes match delivered.

### Signature framework verdict

Three independent civ-archetypes empirically expressed across 45 towers from one underlying dps/cd/range ladder. Each civ-archetype mapped to its per-commander R5 lane lock without forcing magnitudes outside locked bands. No signature was confirmed by cherry-picked single-tower outliers — all three signatures are cluster-driven (Norse cd-band-low survives loss-of-Berserker-Lodge stress test; Aztec dps-band-high survives loss-of-any-single-T2 stress test; Greek dps-band-centered is the null-hypothesis baseline). **The 7-field schema legibly expresses three orthogonal civ-archetypes from one shared underlying ladder.** Schema discipline holds.

## Spine-doc edits

Two surgical edits to `concept/phase-4.md` close the arc:

1. **§4.8 exit-gate** — add new ticked item for per-tower spec table populated. Format mirrors item #1 (✅ DONE 2026-05-05 with cross-reference to R2-R4 + RN decision files).
2. **§4.11.5 Tower DPS ladder** — add closing cross-reference paragraph to per-tower R2-R4 actuals (one sentence, no schema change).

Phase-4 line-cap discipline: file currently 626/600 (carried soft-cap). RN edits add ~3 lines net. Soft-cap remains; pre-existing breach not made materially worse.

## 3x debug loop on the arc as a whole

**Loop 1 — aggressive critique.** The per-tower authoring arc produced 4 decision files + ~600 lines of per-civ prose + a 45-tower magnitude matrix — but the underlying claims are thin. (a) The "falsifiable per-civ signature" framework is constructed *post-R5* on top of locks ratified *at R5*; the signatures literally cannot fail to confirm because they're tautologically downstream of the lane locks they claim to express. R3 predicted Aztec dps-band-high, then R3 itself authored Aztec dps-band-high. R4 predicted Norse cd-band-low, then R4 itself authored Norse cd-band-low. This isn't falsification — this is the schema author saying "the schema says what I made it say." (b) The civ-medians table looks distinct (Aztec elevated dps + Norse fast cd + short range), but distinctness ≤ 10% on most axes lives within band-floor noise — a single-tower retune on either side compresses or inverts the order. The "three orthogonal axes" framing oversells what is actually three centroids ~10% apart in a band that allows ±20%. (c) The arc consumed 4 sessions for content that could have been one big spreadsheet — schema discipline became schema theater.

**Loop 2 — steelman.** (a) The signatures are tautologically downstream of R5 lane locks — but that's the *correctness* condition, not a defect. R5 spec was "Greek=Control, Aztec=Economy, Norse=Summon" without per-tower magnitudes; R2/R3/R4 had to *translate* those archetypes into per-tower magnitudes legibly. The signatures are R2/R3/R4's authorial claim about *how* the translation should read at the magnitude layer — and the audit confirms three distinct magnitude profiles emerged from one shared ladder, not that the ladder was reverse-engineered to fit. The falsification gate that *did* exist was: could a 7-field schema express three civ-archetypes without violating locks? Answer: yes, demonstrated. That's the real test, and it passed. (b) The "10% apart in a 20% band" critique is correct on dps but ignores cd and range, where Aztec mainline cd 1.4s vs Norse 1.15s vs Greek 1.7s spans 47% relative spread — well outside band-noise. Range similar (3.5 vs 4.0 = 14%, within tier-archetype variance but cluster-driven across 6 towers per civ, not single-tower-driven). Status-proc-density ratios (Norse Bleed 6/15 = 40%; Aztec 3/15 = 20%; Greek 2/15 = 13%) are factor-of-3 spreads, not ~10% noise. (c) "One big spreadsheet" would have been faster, but the per-civ-prose discipline forced the falsifiable-signature claims to be made *before* the next civ was authored — which is the only methodology that makes confirmation non-trivial. A spreadsheet would have surfaced the medians, not the signatures.

**Loop 3 — synthesis.** The arc produced legible-at-the-magnitude-layer civ-distinctions from a common ladder under all four locks (attack-type / dps-band / proc-kind / lane-tag) without any cascade-violation. That is the schema's job, and it did it. The signature framework's tautological-downstream property is correct — it's *meant* to be downstream of R5; the falsification target was schema-expressivity, not lane-lock-correctness. The real risk going forward is per-civ-specialization scope creep (R2/R3/R4 deferred ALL aux-narrowing to a future round; civ-flavor surface direction prose stays gated by Follow-up #5; signature-magnitude tunes within band remain Medium-reversibility per-row). RN closes the arc, banks the magnitude tables, and flips the pointer to the next-track pick (per-civ specialization / per-map authoring / Phase 4 exit-gate item #4 mobile-unit-control opening / etc.) — PM picks fork.

**Synthesis-locked output:** Bank 45-tower magnitude matrix as a Phase 4 deliverable. Add §4.8 exit-gate item ticked. Cross-reference §4.11.5 to R2-R4 actuals. Flip CASCADE pointer off per-tower arc. Open the next-track fork to PM via HANDOFF.

## Reason chosen

The arc's deliverables — R1 schema lock, R2 Greek 15, R3 Aztec 15, R4 Norse 15, RN audit — answered four questions the per-commander arc deferred: (1) what cd / range / dps / status-proc magnitudes do the 45 launch towers carry; (2) does the §4.10 variable nomenclature + §4.11 numbers floor + 2026-04-26 attack-type lock + 2026-05-05 R5 baseline ladder + per-commander R1-R5 lane locks cohere into a 7-field schema that 3 civs can populate without conflict; (3) does each civ's lane-lock surface legibly at the per-tower magnitude layer; (4) does §4.8 phase-exit item #2 ("per-tower spec table populated for all 45 launch towers") have content to tick. RN delivers all four answers — yes, yes, yes, yes — and closes the arc.

## Reversibility

**Medium per-tower (carried from R2-R4 row-level reversibility).** Within-band magnitude tunes don't reopen this decision; only out-of-band changes or proc-kind reassignments require supersession. RN itself binds the audit verdict + spine-doc edits — reversing RN means reopening the audit verdict (e.g. if a future tower retune pushes a magnitude out of band, the verdict needs amendment; the spine-doc tick needs to be temporarily flipped). All four locks (attack-type / dps-band / proc-kind / lane-tag) remain Hard reversibility.

## Follow-ups

1. **Spine-doc edits applied as separate Edits in same RN close** — `§4.8` exit-gate item add + tick; `§4.11.5` closing cross-reference.
2. **Decisions table row + CASCADE pointer flip** — close per-tower arc current-work pointer; bump version footer.
3. **Final dual-push checkpoint** (carries RN; closes per-tower authoring arc).
4. **Cultural-sensitivity Follow-up #5** carries forward unchanged — heaviest-load-Aztec / secondary-Norse / lightest-Greek per per-commander R5 one-pagers; mandatory consultation gate before any art lock per 2026-04-25 ratification. Per-tower arc used civ-neutral mechanical-content language throughout; locked content-skeleton names verbatim; no art / VFX / pose / VO direction prose was generated.
5. **Next-track pick (PM fork)** — per-civ specialization (matchup affinities + identity hooks + signature creep types per civ) / per-map authoring (good-cell + wave-randomization seeds + crystal-lock variance) / Phase 4 exit-gate item #3 mobile-unit-control opening (§4.4 BLOCKER) / Phase 4 exit-gate item #4 enemy direction (§4.7 OPEN) / monetization specifics / engine choice lock (Godot 4 leading) / art director scope. PM picks via AskUserQuestion next session.
6. **Per-tower magnitude tunes** — within-band per-row tunes remain Medium-reversibility; out-of-band tunes require supersession decision against the specific R2/R3/R4 row.
7. **Phase 4 exit-gate status post-RN:** items #1 (one-pagers) + #2 (per-tower spec table) closed. Remaining items #3-#9 (Fusion numerics, mobile unit control, enemy direction, economy numerics, monetization, engine, art director, cultural-sensitivity) carry forward to next-track pick.
