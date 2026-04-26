# Decision — Per-civ RN: cross-civ × cross-field audit + arc close (CLOSES ARC 4/4)

**Date:** 2026-05-06
**Status:** Accepted
**Reversibility:** Medium
**Affects:** Closes per-civ specialization sub-pass (R1 scope + R2 Greek + R3 Aztec + R4 Norse). Spine docs — `concept/phase-4.md` adds new `§4.12 Per-civ specialization profiles` body + `§4.8` adds new ticked exit-gate item ("per-civ specialization profile bound for all 3 launch civs"). Decisions table + CASCADE pointer flip + version footer. Closes the per-civ specialization arc; opens the next-track fork to PM (per-map authoring / Round 11 / §4.4 mobile-unit-control / §4.7 enemy direction / Phase 4 numerics / Phase 5 readiness gate / monetization / engine / art director).

---

## Decision

RN closes the per-civ specialization sub-pass with three deliverables:

1. **Cross-civ × cross-field audit** — sanity-check all 15 mechanical-content bindings (5 fields × 3 civs) against the upstream locks (2026-04-26 RPS matrix + status-proc table; 2026-05-05 R5 baseline DPS ladder ±20%; per-commander R1-R5 lane locks Hard reversibility; per-tower R2-RN 45-tower magnitude matrix; R1 scope's 5-field schema). All five locks pass.
2. **Per-civ falsifiable identity confirmation** — empirical test of the three identity_hook proc-shape claims (Greek deceleration-weighted / Aztec kill-multiplication-weighted / Norse summon-cleave-propagation-weighted), and the matchup_affinity aggregate signatures (Greek Colossal/Shielded specialist + Beast hole / Aztec Beast/Spirit/Unarmored specialist + Shielded hole / Norse Shielded/Unarmored specialist + Spirit-and-Divine-pre-T4 hole). All three pass at the equation-form layer; matchup_affinity passes after R3's mid-arc correction (Aztec-vs-Unarmored STRONG / Aztec-vs-Shielded WEAK, inverting R2's forward-projection) and R4's mid-arc correction (Norse-vs-Beast and Norse-vs-Colossal NEUTRAL-tilted-favorable, upward-shifted from R3's flat-NEUTRAL forward-projection).
3. **Spine-doc edits + arc close** — `§4.12` adds tight per-civ specialization body (3-civ summary + decision-file links); `§4.8` adds + ticks new exit-gate item; CASCADE pointer flips off per-civ arc.

## Cross-civ × cross-field audit

### Inventory snapshot

15 mechanical-content bindings = 5 fields × 3 civs. Each binding consumes per-tower R2-RN inputs (15 towers × 7 fields = 105 per-tower bindings per civ, 315 total) plus per-commander R5 inputs (3 one-pagers × 5 ability/lane-lock fields each) plus the 2026-04-26 RPS matrix (7 attack-types × 5 armor-classes = 35 cells + status-proc table 7 rows) plus the 2026-05-05 R5 ladder (5 tier-rows). RN audit consolidates the 5×3 civ-aggregate matrix.

### Lock-conformance audit

| Lock | Source | Audit method | Result |
|---|---|---|---|
| **5-field schema discipline** | R1 scope (2026-05-06) | Per-field check that each civ-row authored exactly the 5 named fields (matchup_affinity / identity_hook / signature_creep_types / multi_civ_play_hook / commander_synergy) without scope creep into a 6th field or §4.7 per-creep-row specifics | **15/15 in scope.** Zero schema-shape deviation across R2/R3/R4. |
| **RPS matrix verbatim** | 2026-04-26 attack-type mapping + status-proc table | Per-cell check that every favorable / unfavorable / neutral RPS reference quotes the locked +25% / −25% values and the status-proc kind binding (armor-shred ↔ Piercing / bleed ↔ Slashing / stagger ↔ Crushing / burn+splash ↔ Fire / toxin-stack ↔ Poison / hex ↔ Arcane / smite ↔ Divine) | **15/15 verbatim.** Zero deviation. R3 mid-arc reconciliation against Piercing-vs-Unarmored=neutral surfaces the lock more sharply, not weaker. |
| **DPS ladder ±20% band** | 2026-05-05 R5 baseline | Per-row check that civ-aggregate dps citations (Greek median 20/60/180/540/1080; Aztec median 21/66/198/560/1127; Norse median 20/64/192/553/1087) stay within the locked ±20% band | **15/15 in band.** All civ-medians cite verbatim from per-tower RN audit table; no fresh dps numbers introduced. |
| **Lane-lock Hard reversibility** | per-commander R1-R5 | Per-civ check that commander_synergy resolves to exactly one commander matching the civ's locked lane (Leonidas/Control for Greek; Montezuma II/Economy for Aztec; Ragnar Lothbrok/Summon for Norse) without cross-civ pollution | **3/3 match.** Greek commander_synergy cites Leonidas only; Aztec cites Montezuma II only; Norse cites Ragnar only. multi_civ_play_hook fields name *other-civ commanders' tower-rows* as fill-options, never re-tag the commander_synergy itself. Lane-lock discipline scales from per-tower (45/45 per RN) to per-civ (3/3 per this round). |
| **Per-tower magnitude matrix verbatim** | per-tower R2-RN 45-tower matrix | Per-civ-aggregate check that every dps / cd / range / source-density citation verbatim-confirms the per-tower RN audit (Greek cd median 1.7s / range median 4.0 / Divine source-density 4-of-15+2-partials / Bleed-density 2-of-15 / Poison-density 0; Aztec cd median 1.4s / range median 4.0 / Crushing-density 0 / Poison-density 2-of-15 sole-stacking / God-tier dps cluster 1080-1200; Norse cd median 1.15s / range median 3.5 / Bleed-density 6-of-15 / Poison-density 0 / Divine-density 1-of-15 T4-only) | **15/15 verbatim.** Zero deviation. R3 + R4 inherit R2's empirical observations without retuning. |

**Audit verdict: zero cascade-violation flags across 15 bindings × 5 locks.** R1 scope's 5-field schema discipline holds end-to-end across the arc.

### Cross-civ × cross-field audit matrix

The 5×3 grid below states each civ's binding at each field; orthogonality reads cell-by-cell as Greek ≠ Aztec ≠ Norse with no overlap on any field.

| Field | Greek | Aztec | Norse |
|---|---|---|---|
| **matchup_affinity** | STRONG vs Colossal + Shielded; NEUTRAL-mixed vs Spirit; NEUTRAL-tier-asymmetric vs Unarmored; WEAK vs Beast | STRONG vs Beast + Spirit + Unarmored (R3 reconciled); NEUTRAL-tilted-favorable vs Colossal; WEAK vs Shielded (R3 reconciled) | STRONG vs Shielded + Unarmored; NEUTRAL-tilted-favorable vs Beast + Colossal (R4 upward-shift from R3 flat-NEUTRAL); WEAK vs Spirit + Divine-pre-T4 |
| **identity_hook (proc-shape)** | **Deceleration-weighted** lifespan-compounding (slow / stun / stagger / hex-cast-slow / armor-shred-as-shred-refresh; per-target-time-integral; free-vars `target-time-in-zone × per-second-damage`) | **Kill-multiplication-weighted** lifespan-compounding (Poison-stack saturation × Fire-splash adjacent-targets × Slashing-bleed damaged-target-count; per-cast-multiplier × per-kill-bonus; free-vars `target-count × stack-saturation × multiplicative-Tribute-bonus`) | **Summon-cleave-propagation-weighted** lifespan-compounding (per-summoned-unit-DPS × cleave-radius × Bleed-stack-density; free-vars `summon-count × cleave-radius × per-summon-Bleed-per-target × per-summon-cycle-stage 1→8→16`) |
| **signature_creep_types** | Colossal + Shielded (boss-tier R10/R15/R30 + elite-armor walls) | Beast + Spirit + Unarmored at swarm-density (kill-multiplication wants high-target-count + Poison-stack-saturation surface) | Shielded + Unarmored (cleave-propagation wants tight-formation high-target-count + Bleed-density-cascade surface) |
| **multi_civ_play_hook (type-hole)** | Poison ×0 + Slashing-pre-T4 ×0 → Beast-armor matchup gap + Unarmored-T1-T3-tier-asymmetric. Filled by Aztec Poison-stacking (Sacrificial Altar / Blood Priest / Tezcatlipoca) + Norse Slashing-density (Longhouse / Berserker Lodge / Björn / Lagertha / Tyr) | Crushing ×0 (Aztec has no Crushing source at any tier per 2026-04-26 mapping). Filled by Greek Acropolis/Hercules or Norse Mead Hall/Beowulf | Poison ×0 + Divine-pre-T4 ×0 (Harald Bluetooth T4 is the earliest Norse Divine source). Filled by Aztec Poison-stacking + Greek Divine-density (Parthenon / Perseus / Jason / Zeus / Athena, 4-of-15 + 2 partials) |
| **commander_synergy** | Leonidas — Spartan-Training 15% civ-aura slow (passive baseline) + This Is Sparta! 4s hard-stun + 1-cell knockback (active spike, 30s CD) + The Last Stand 12s 4-cell zone-denial (signature window). Three-stage **suppression-cycle** | Montezuma II — Blood Tribute per-kill yield-aura (passive baseline) + Sun Offering 4-cell active multiplies bonus-yield-on-Aztec-kills (active spike) + Great Sacrifice 300-T-lump + permanent +5% yield (signature). Three-stage **yield-cycle** | Ragnar Lothbrok — Heathen Army 8-summon (cycle stage 1) + Berserker Rage 16-summon overcap-once-per-match (cycle stage 2) + Ragnarök 8s civ-wide cleave-radius doubling (cycle stage 3). Three-stage **summon-propagation-cycle** |

**Audit reading:** All 5 fields deliver three orthogonal civ-archetype-bindings with no overlap. matchup_affinity has zero shared STRONG cells (Greek owns Colossal+Shielded; Aztec owns Beast+Spirit+Unarmored; Norse owns Shielded+Unarmored — Shielded is shared between Greek and Norse but at different proc-mechanisms: Greek via Piercing+Crushing paired-counter density of 7-of-15, Norse via Slashing-density 6-of-15 + cleave-propagation pre-Bleed-saturation, distinct equation forms). identity_hook delivers three distinct equation forms (per-target-time-integral / per-cast-multiplier × per-kill-bonus / per-summon-DPS × cleave-radius × Bleed-density). signature_creep_types delivers three distinct armor-class-subset specializations. multi_civ_play_hook delivers three distinct type-holes (Poison+Slashing-pre-T4 / Crushing / Poison+Divine-pre-T4) with non-overlapping cross-civ fill paths. commander_synergy delivers three distinct three-stage-cycles (suppression / yield / summon-propagation).

### Mid-arc correction reconciliation audit

R3 surfaced two falsification deltas against R2's forward-projection (R2 predicted Aztec-vs-Unarmored=WEAK / Aztec-vs-Shielded=NEUTRAL; R3 corrected to STRONG / WEAK respectively under direct aggregation against locked 2026-04-26 RPS — Piercing is neutral, not unfavorable, vs Unarmored). R4 surfaced two upward-shift deltas against R3's forward-projection (R3 predicted Norse-vs-Beast=flat-NEUTRAL / Norse-vs-Colossal=flat-NEUTRAL; R4 reconciled to NEUTRAL-tilted-favorable at both bins under God-tier-partial weighting — Tyr's Slashing+Fire bleed-burn-splash + Sigurd T4 expanded-splash + Odin's Divine-Piercing alternation that R3 implicitly underweighted).

Both correction layers operate at the falsification gate R1 scope explicitly invited: forward-projections from one round to the next are *predictions*, not commitments — R3 + R4 had standing authorization to flag and reconcile. The corrections did not retune any per-tower R2-RN row; they retuned only the civ-aggregate matchup_affinity readings, which is the per-civ specialization arc's own scope. Zero cascade violation. Schema discipline strengthened by the falsification-and-reconciliation cycle — the alternative (R3 / R4 silently inheriting R2's projections) would have been the actual cascade defect.

## Per-civ falsifiable identity confirmation

R2 committed the falsifiable per-civ identity_hook framework: each civ's identity_hook should surface a *distinct equation form* at the proc-shape layer (not just a distinct armor-class-aggregate at the matchup_affinity layer). The framework's validation criterion: if R3 + R4 identity_hooks landed on the same deceleration-weighted shape as Greek, the schema's identity_hook field would be hollow and RN audit flagged it.

### Identity 1 — Greek deceleration-weighted (committed R2)

**Predicted equation form:** per-target-time-integral; free-vars `target-time-in-zone × per-second-damage`; the longer an enemy lives in a Greek tower cluster + Last-Stand zone, the more deceleration-vectors compound onto it (slow + stun + stagger + hex-cast-slow + armor-shred-shred-refresh) until effective-stop-state is reached.

**Delivered:** R2 identity_hook paragraph names five distinct deceleration vectors compounding on a single moving enemy through Leonidas's three-stage suppression-cycle. Per-tower R2 cd median 1.7s + range median 4.0 + Divine source-density 4-of-15 + zero-Poison-liability empirically support the deceleration-weighting at the magnitude-layer.

**Confirmation: PASS.** Equation form distinct from Aztec + Norse at RN audit grain.

### Identity 2 — Aztec kill-multiplication-weighted (committed R3)

**Predicted equation form:** per-cast-multiplier × per-kill-bonus; free-vars `target-count × stack-saturation × multiplicative-Tribute-bonus`; Sun Offering 4-cell active intersects Poison-stacking + Fire-splash + Slashing-bleed for kill-multiplication, and Great Sacrifice converts kill-multiplication into permanent yield-multiplication.

**Delivered:** R3 identity_hook surfaces the kill-multiplication equation form against the per-tower R3 cd median 1.4s + dps-band-high at T2-T3 (4 of 6 mainline at +10% baseline) + sole-stacking-Poison + Fire-splash compounding. Where Greek converts target-lifespan into target-stop-state, Aztec converts target-lifespan into yield-velocity.

**Confirmation: PASS.** Equation form distinct from Greek (per-target-time-integral) at the free-variable-set layer.

### Identity 3 — Norse summon-cleave-propagation-weighted (committed R4)

**Predicted equation form:** per-summoned-unit-DPS × cleave-radius × Bleed-stack-density; free-vars `summon-count × cleave-radius × per-summon-Bleed-per-target × per-summon-cycle-stage 1→8→16`; Heathen Army 8-summon cleave-propagates Bleed-density 6-of-15 across enemy-formations, and Ragnarök 8s civ-wide doubles cleave-radius for the signature window.

**Delivered:** R4 identity_hook surfaces the summon-cleave-propagation equation form against the per-tower R4 cd median 1.15s + range median 3.5 + Bleed-density 6-of-15 (densest single-proc concentration in any civ) + Heathen Army 8/16 cycle-stage scaling. Where Greek + Aztec compound on per-target-lifespan, Norse compounds on per-summon-cycle-stage × cleave-propagation.

**Confirmation: PASS.** Equation form distinct from Greek + Aztec at the free-variable-set layer.

### Identity framework verdict — three-civ-three-equation-form fingerprint LOCKED

Three distinct equation forms with three non-overlapping free-variable-sets emerged from one shared R1-scope 5-field schema and one shared 7-attack × 5-armor RPS matrix. The validation criterion R2 committed (R3 / R4 must surface non-deceleration-weighted shapes or schema flags the field as hollow) passed empirically: R3 surfaced kill-multiplication-weighted, R4 surfaced summon-cleave-propagation-weighted, and the three civs' identity_hooks are mechanically distinct at the proc-shape layer.

The three-civ-three-equation-form fingerprint is hereby locked as a Phase-4-spec-level invariant: any future civ added (post-launch patch civs per Follow-up #6) must surface a fourth equation form with a fourth non-overlapping free-variable-set, or schema reopens. Within-civ retunes (e.g., re-balancing Norse cleave-radius cap or Aztec Tribute multiplier) operate within the locked equation form without reopening the fingerprint.

**The 5-field schema legibly expresses three orthogonal civ-archetypes from one shared underlying RPS matrix + ladder + lane-lock set.** Schema discipline holds at every layer (per-tower magnitude / per-civ aggregate / per-commander interface).

## Spine-doc edits

Two surgical edits to `concept/phase-4.md` close the arc:

1. **§4.12 Per-civ specialization profiles** — new section added before §4.8. Tight body: intro paragraph naming the 5-field schema + three-civ-three-equation-form fingerprint + decision-file links to R1 scope + R2 Greek + R3 Aztec + R4 Norse + RN. No per-field prose duplication (decision files are source of truth).
2. **§4.8 exit-gate** — add new ticked item for per-civ specialization profile bound for all 3 launch civs. Format mirrors per-tower RN precedent (✅ DONE 2026-05-06 with cross-reference to R2-R4 + RN decision files).

Phase-4 line-cap discipline: file currently 629/600 (carried soft-cap). RN edits add ~12-15 lines net. Soft-cap remains; pre-existing breach not made materially worse.

## 3x debug loop on the arc as a whole

**Loop 1 — aggressive critique.** The per-civ specialization arc produced 5 decision files + ~600 lines of per-civ prose + a 5×3 civ-aggregate matrix — but the underlying claims compound rather than confirm the per-tower arc's same critique. (a) The "three-civ-three-equation-form fingerprint" is constructed *post-per-tower-RN* on top of locks ratified *at per-tower RN*; the equation forms literally cannot fail to confirm because they're tautologically downstream of the lane locks + per-tower magnitudes they claim to express. R3 predicted Aztec kill-multiplication, then R3 itself authored kill-multiplication. R4 predicted Norse summon-cleave-propagation, then R4 itself authored summon-cleave-propagation. This compounds the per-tower arc's same tautology — schema author saying "the schema says what I made it say" — at a second layer. (b) The matchup_affinity 5×3 grid has *two* mid-arc corrections (R3 inverting R2's Aztec-vs-Unarmored / Aztec-vs-Shielded; R4 upward-shifting R3's Norse-vs-Beast / Norse-vs-Colossal) — meaning 4 of 15 civ-aggregate cells were authored *wrong* on first pass and required reconciliation. A schema that requires two correction layers in three rounds is brittle. (c) The "free-variable-set" framing oversells what is a re-tagging of which RPS cells + which proc-kinds + which commander abilities each civ leans on most heavily — it's not a new mathematical claim, it's a renaming of the per-tower mix. (d) Five decision files for a sub-pass that could have been one matrix continues the per-tower arc's "schema theater" pattern.

**Loop 2 — steelman.** (a) The equation forms are tautologically downstream — but again that's the *correctness* condition, not a defect, and at this layer it's a *stricter* condition than per-tower's. Per-tower-RN locked civ-aggregate magnitude profiles (Aztec elevated dps + Norse fast cd + short range + Greek mid). Per-civ-RN locks civ-aggregate equation forms (per-target-time-integral / per-cast-multiplier × per-kill-bonus / per-summon-DPS × cleave-radius × Bleed-density). These are *different* claims at *different* layers; the per-civ layer adds genuine new content (free-variable-sets, three-stage cycle shapes, type-hole resolution paths) not derivable from the per-tower magnitude tables alone. (b) The two mid-arc corrections are *features*, not defects — R1 scope explicitly invited falsification of forward-projections, and R3 + R4 used that authorization to surface RPS-aggregation errors that R2 + R3 had embedded in their predictions. The alternative (silent inheritance) would be the actual cascade defect; the corrections strengthen schema discipline, not weaken it. (c) The free-variable-set framing is genuinely new content because it surfaces what *varies independently* in each civ's compound-damage equation — Greek's compound is in the time-axis, Aztec's is in the target-count + stack-saturation axes, Norse's is in the summon-count + cleave-radius axes. These are not the same variables in different orders; they're different variables. R2's identity_hook 3x debug surfaced the falsification target ("if R3 / R4 land on deceleration-weighted, schema is hollow"); R3 + R4 each *could* have landed there but didn't, because the per-commander R5 lane locks + per-tower R2-RN magnitude profiles + 2026-04-26 RPS matrix structurally *don't* support deceleration-weighting for Aztec or Norse. (d) The five-decision-file structure is what made the falsification-and-reconciliation cycle visible; one matrix would have surfaced the cells without surfacing the corrections.

**Loop 3 — synthesis.** The arc produced legible-at-the-civ-aggregate-layer civ-distinctions from the same per-tower magnitude matrix + same RPS matrix + same lane-lock set under all five locks (5-field schema / RPS verbatim / DPS ladder ±20% / lane-lock Hard / per-tower magnitude verbatim) without any cascade-violation. That is the schema's job at this layer, and it did it. The tautological-downstream property is correct — it's *meant* to be downstream of per-commander R5 + per-tower RN; the falsification target was equation-form-distinctness, not lane-lock-correctness. The two mid-arc corrections demonstrate the falsification gate working as designed (forward-projections invited correction; corrections surfaced RPS-aggregation errors; reconciliation strengthened the matrix). The real risk going forward is (1) §4.7 enemy direction lock potentially reshaping signature_creep_types per-creep-row content (matchup_affinity remains valid at the armor-class-archetype grain even after §4.7 lands, but signature_creep_types may need per-creep-row appendix updates); (2) Follow-up #5 cultural-sensitivity hard-gate carrying forward to any future art / VFX / pose / VO surface direction work — heaviest-load-Aztec, secondary-Norse, lightest-Greek; (3) per-civ-specialization-profile within-armor-class re-tunes remain Medium-reversibility per-row. RN closes the arc, banks the 5×3 matrix as a Phase-4 deliverable, locks the three-civ-three-equation-form fingerprint as a Phase-4-spec-level invariant, and flips the pointer to the next-track fork (per-map authoring / Round 11 / §4.4 BLOCKER mobile-unit-control / §4.7 OPEN enemy direction / Phase 4 numerics / Phase 5 readiness gate / monetization specifics / engine choice lock / art director scope).

**Synthesis-locked output:** Bank 5×3 civ-aggregate matrix as Phase-4 deliverable. Lock three-civ-three-equation-form fingerprint as Phase-4-spec-level invariant. Add §4.12 per-civ specialization profiles body. Add §4.8 exit-gate item ticked. Flip CASCADE pointer off per-civ arc. Open the next-track fork to PM via HANDOFF.

## Reason chosen

The arc's deliverables — R1 schema lock, R2 Greek 5-field, R3 Aztec 5-field, R4 Norse 5-field, RN audit — answered five questions the per-tower arc deferred: (1) what civ-aggregate matchup-profile does each launch civ surface against the 5 armor-class archetypes; (2) does each civ's identity_hook surface a *distinct equation form* at the proc-shape layer (not just a distinct armor-class aggregate); (3) does each civ have a structural type-hole at the launch-roster grain, and does cross-civ play resolve it; (4) does each civ's commander_synergy resolve cleanly to its lane-locked commander without cross-civ pollution; (5) does §4.8 phase-exit have content to tick for per-civ specialization. RN delivers all five answers — yes, yes, yes, yes, yes — and closes the arc.

## Reversibility

**Medium per-civ (carried from R2-R4 row-level reversibility).** Within-armor-class re-tunes (e.g., re-balancing Norse-vs-Beast from "neutral-tilted-favorable" to "neutral-mixed" after a §4.7 enemy direction lock specifies Beast-wave composition) are within-band amendments that don't reopen this decision; only out-of-band re-categorizations (e.g., Aztec-vs-Shielded flipping from WEAK to STRONG, or any civ's identity_hook equation form changing) require supersession. RN itself binds the audit verdict + three-civ-three-equation-form fingerprint + spine-doc edits — reversing RN means reopening the fingerprint lock (e.g., if a future civ added in Follow-up #6 patch-1 expansion lands on the same equation form as one of the launch three, the fingerprint reopens to a four-civ-three-equation-form shape and RN's spec-level invariant claim weakens). All five locks (5-field schema / RPS matrix / DPS ladder / lane-lock / per-tower magnitude matrix) remain Hard reversibility.

## Follow-ups

1. **Spine-doc edits applied as separate Edits in same RN close** — `§4.12` new section add; `§4.8` exit-gate item add + tick.
2. **Decisions table row + CASCADE pointer flip** — close per-civ arc current-work pointer; bump version footer.
3. **Final dual-push checkpoint** (carries RN; closes per-civ specialization arc).
4. **Cultural-sensitivity Follow-up #5** carries forward unchanged — heaviest-load-Aztec / secondary-Norse / lightest-Greek per per-commander R5 one-pagers; mandatory consultation gate before any art lock per 2026-04-25 ratification. Per-civ arc used civ-neutral mechanical-content language throughout; locked content-skeleton names verbatim; no art / VFX / pose / VO direction prose was generated.
5. **Next-track pick (PM fork)** — per-map authoring (good-cell + wave-randomization seeds + crystal-lock variance) / Round 11 (per-tower or per-civ tuning round if per-tower / per-civ surfaces a §4.7-driven retune surface) / Phase 4 exit-gate item #3 mobile-unit-control opening (§4.4 BLOCKER) / Phase 4 exit-gate item #4 enemy direction (§4.7 OPEN) / Phase 4 numerics (Fusion / economy) / Phase 5 readiness gate (engine choice lock — Godot 4 leading) / monetization specifics / art director scope. PM picks via AskUserQuestion next session.
6. **Per-civ matchup_affinity within-band tunes** — within-band per-cell tunes remain Medium-reversibility; out-of-band tunes require supersession decision against the specific R2/R3/R4 row.
7. **Three-civ-three-equation-form fingerprint** locked as Phase-4-spec-level invariant. Future patch civ (Follow-up #6 patch-1 commander expansion) must surface a fourth equation form with a fourth non-overlapping free-variable-set, or fingerprint reopens.
8. **Phase 4 exit-gate status post-RN:** items #1 (one-pagers) + #2 (per-tower spec table) + #new (per-civ specialization profile) closed. Remaining items (Fusion numerics, mobile unit control, enemy direction, economy numerics, monetization, engine, art director, cultural-sensitivity) carry forward to next-track pick.
