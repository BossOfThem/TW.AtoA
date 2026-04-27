# Decision — §4.4 mobile unit control sub-pass RN: cross-arc audit + spine-doc edits + arc close (CLOSES ARC 4/4)

**Date:** 2026-05-06
**Status:** Accepted
**Reversibility:** Medium
**Affects:** [`concept/phase-4.md §4.4`](../concept/phase-4.md) (spine-doc edit lands here — control-model body merged from R2 Bodies 1-3 + R3 Bodies A-D; OPEN BLOCKER cleared), [`concept/phase-4.md §4.8`](../concept/phase-4.md) (exit-gate item #5 ✅ ticked DONE), [`decisions/2026-05-06-mobile-unit-control-r3-spec-grammars.md`](2026-05-06-mobile-unit-control-r3-spec-grammars.md) (R3 spec-grammars — read-only input), [`decisions/2026-05-06-mobile-unit-control-r2-direction-lock.md`](2026-05-06-mobile-unit-control-r2-direction-lock.md) (R2 control-model — read-only input), [`decisions/2026-05-06-mobile-unit-control-r1-scope.md`](2026-05-06-mobile-unit-control-r1-scope.md) (R1 scope — read-only input), [`concept/phase-4.md §4.1`](../concept/phase-4.md) (commander-as-summoned-ability-avatar — read-only audit target Axis 1), [`concept/phase-4.md §4.4a`](../concept/phase-4.md) (Builder excluded — read-only audit target Axis 1), [`concept/phase-3.md §3.4`](../concept/phase-3.md) ("waypoint-style commands, not full RTS per-unit micro" floor — read-only audit target Axis 1), [`concept/phase-4.md §4.11.4`](../concept/phase-4.md) (`f_base = 50 u/s` + archetype multipliers — read-only audit target Axis 2).

---

## Decision

RN closes the §4.4 mobile-unit-control sub-pass at zero cascade-violations across a 3-axis audit, applies spine-doc edits to `concept/phase-4.md §4.4`, and ticks `§4.8` exit-gate item #5 (`Mobile unit control model resolved`) DONE.

The arc lands as **4/4 rounds**:

1. **R1 — Scope** (locked 4-round per-property axis + 6 hard-guard surfaces).
2. **R2 — Control-model direction lock** (Option (i) waypoint + mode-flags ratified; 4-flag mode catalog + 3-default engagement shape + no-tier-scaling control-surface principle).
3. **R3 — Spec-grammar authoring** (4 bodies: speed-ladder T1-T4 / pathing-mode catalog / engagement-rule catalog with per-tier §3.4 falsification gate / aggro tie-breaker resolution = stable-sort + no-override).
4. **RN (this round)** — 3-axis cross-arc audit + spine-doc edits at `phase-4.md §4.4` + `§4.8` exit-gate item #5 ✅ tick + arc close.

Phase 4 advances to **5 of 11 exit-gate items closed** (#1 commander one-pagers / #2 per-tower spec / #3 per-civ specialization / #4 enemy direction / #5 mobile unit control).

## Context

The §4.4 OPEN ISSUE prose enumerated four needs: (a) movement speed per unit tier, (b) pathing mode (patrol / follow lane / waypoint / attack-move), (c) engagement rules (auto-engage / hold / fall back), (d) control complexity (waypoint + mode flags, NOT full RTS per-unit micro). R2 closed (d) via the no-tier-scaling principle. R3 closed (a)/(b)/(c) via the speed-ladder + catalog enumerations. RN's job is verification: the four locked bodies must compose without violating any upstream surface, and the §4.4 spine-doc must be rewritten to reflect the resolution and clear the OPEN BLOCKER tag.

Three orthogonal audit axes were chosen at R1 scope:

- **Axis 1 — §4.1 + §4.4a + §3.4 floor coherence.** The control surface must exclude Commander (per §4.1 commander-as-summoned-ability-avatar lock) and Builder (per §4.4a out-of-scope). The full-stack rule set (mode flags + engagement defaults + speed ladder + tie-breaker discipline) must defend §3.4's "waypoint-style commands, not full RTS per-unit micro" floor.
- **Axis 2 — §4.11.4 magnitude consistency.** The R3 Body-A speed ladder must read magnitudes from §4.11.4 verbatim (no re-authoring); the tier-to-archetype binding must align with `f_base = 50 u/s` + the four archetype multipliers (Swarm 1.5 / Standard 1.0 / Elite 1.0 / Boss 0.7) as locked in Numbers-phase #13 R4 (Hard-class).
- **Axis 3 — Control-surface tier-scaling at T1-T4.** R2 Body-3's no-tier-scaling principle must hold empirically: every rule (mode flag / engagement default / aggro discipline) must produce identical UI surface at T1, T2, T3, and T4 — tier expression lives only in stats + signature passive framing, never in new buttons.

## Cross-arc audit — 3 axes × 12 cells, zero cascade-violations

### Axis 1 — §4.1 + §4.4a + §3.4 floor coherence (4 cells)

| Cell | Verification | Result |
|---|---|---|
| **A1.1** §4.1 Commander excluded from §4.4 surface | R3 Body-B catalog applies to mobile units only; Commander emerges only on cast (no waypoint / no mode flag / no engagement rule). R3 Body-A speed ladder explicitly omits Commander (Commander has no movement speed — emerges, casts, despawns). | **PASS** |
| **A1.2** §4.4a Builder excluded from §4.4 surface | R3 Body-A includes a verbatim Builder exemption (walks deterministic walkable-build-grid path; consumes its own speed value). R3 Body-C HP_fall_back anchor selection explicitly excludes Builders (Loop-2 edit) — walk-and-despawn lifecycle would orphan units. | **PASS** |
| **A1.3** §3.4 floor structurally defended | R2 Body-3 no-tier-scaling principle enumerates negative space (no per-target manual aggro / no formation commands / no active-pause RTS / no per-unit retreat micro / no ability buttons at any tier). Every R3 rule respects this — speed-ladder is passive (no input surface); pathing-mode is binary-state-per-flag; engagement defaults are config-shape (Phase-5 numerics), not per-unit input. | **PASS** |
| **A1.4** Per-rule §3.4 floor falsification gate (T1×T2×T3×T4 × 4 rules = 16 sub-cells, R3 Body-C) | R3 Body-C ran the explicit per-tier × per-rule gate — all 16 sub-cells PASS. R_engage / HP_fall_back / Hold_fire / aggro-priority each produce identical input shape at T1-T4 (zero new buttons per tier). | **PASS** |

### Axis 2 — §4.11.4 magnitude consistency (4 cells)

| Cell | Verification | Result |
|---|---|---|
| **A2.1** Speed magnitudes are read-only | R3 Body-A binds *tiers to archetypes*, not values. The four numeric outputs (75 / 50 / 50 / 35 u/s) are computed from `f_base = 50 u/s` × archetype × — exact match against §4.11.4 (f) Numbers-phase #13 R4 row. No magnitude re-authoring. | **PASS** |
| **A2.2** Archetype-multiplier table coverage | The 4-tier mobile-unit ladder maps to 3 of the 4 archetype rows (Swarm × 1.5 / Standard × 1.0 / Boss × 0.7); Elite × 1.0 is also Standard-equivalent for spec-level grain. The Colossal × 0.5 row is enemy-Colossal territory (§4.7), not mobile-unit territory — correctly omitted. | **PASS** |
| **A2.3** T2/T3 share Standard intentionally | R3 Body-A locks T2 mainline + T3 elite both at Standard × 1.0 = 50 u/s. This is intentional per R2 Body-3 (tier expression in stats + passives, not speed). The 3x debug loop on this read it as feature-not-bug (Loop-1 critique that "T3 elite should be slower than T2 mainline" rejected by Loop-2: T3-as-slower would make elites feel like mini-bosses, eroding the T4 Demigod tempo distinction). | **PASS** |
| **A2.4** Per-civ magnitude neutrality | The speed ladder is civ-neutral (Greek / Aztec / Norse rosters all instantiate the same archetype-tier bindings). Three-civ-three-equation-form fingerprint preserved — civs differentiate through tower-DPS-band / status-proc archetype / signature-passive framing, never through movement-speed re-authoring at the spec-level grain. | **PASS** |

### Axis 3 — Control-surface tier-scaling at T1-T4 (4 cells)

| Cell | Verification | Result |
|---|---|---|
| **A3.1** Mode-flag count is tier-invariant | All 4 mode flags (`Patrol` / `Follow-Lane` / `Hold` / `Attack-Move`) available at T1, T2, T3, T4. Group-select rule applies identically across tiers. No tier exposes a 5th flag. | **PASS** |
| **A3.2** Engagement-default count is tier-invariant | All 3 defaults (`R_engage` / `HP_fall_back` / `Hold_fire`) plus the aggro-priority shape apply identically at T1-T4. Per-archetype values are Phase-5 numerics territory; the *shape* is fixed. No tier exposes a 4th default. | **PASS** |
| **A3.3** Aggro tie-breaker discipline is tier-invariant | R3 Body-D stable-sort by entity-id + no-override reaffirmation applies at T1-T4. The cost-acknowledged framing (eagle-vs-near-dead-berserker remains structural cost of no-buttons rule) applies symmetrically — T1 swarm and T4 Demigod both surrender per-target manual aggro. | **PASS** |
| **A3.4** Negative-space verbatim across tiers | R2 Body-3's negative-space list (no per-target manual aggro / no formation commands / no active-pause RTS / no per-unit retreat micro / no ability buttons) holds at T1, T2, T3, T4. No T4 Demigod exception (which would void the no-tier-scaling principle). | **PASS** |

**Audit summary: 12/12 cells PASS at zero cascade-violations.**

## Spine-doc edits applied to `concept/phase-4.md §4.4`

The §4.4 body is rewritten as follows (full diff lands in this commit). Key changes:

1. **OPEN BLOCKER tag cleared.** The "Contains OPEN BLOCKER (control model)" stub is removed; replaced with "Locked 2026-05-06 R1-RN" status.
2. **OPEN ISSUE paragraph removed.** Replaced with a four-paragraph locked body: (a) speed-ladder summary referencing §4.11.4; (b) pathing-mode catalog inline table; (c) engagement-rule catalog inline table with §3.4 floor verification line; (d) no-tier-scaling principle paragraph + negative-space verbatim list.
3. **Inline tables landed.** Speed-ladder table (4 rows, T1-T4 to archetype × → u/s), pathing-mode table (4 rows, flag → semantics), engagement-rule table (4 rows, rule → shape).
4. **Cross-references added.** §4.4 now points to R1/R2/R3/RN decision files for per-round detail; §4.4a Builder reference reaffirmed in spec-level prose.
5. **Civ-neutrality paragraph.** Body closes with a one-line civ-neutrality assertion: "All four bodies apply identically to Greek / Aztec / Norse rosters; per-civ differentiation lives in tower-DPS-band / status-proc archetype / signature-passive framing per per-civ RN, not in mobile-unit control surface."

## §4.8 exit-gate tick

Item #5 ("Mobile unit control model resolved (§4.4 OPEN BLOCKER)") flips to ✅ DONE 2026-05-06 with reference to this RN file + the R1/R2/R3 sequence. Phase 4 exit-gate count advances 4 → 5 of 11.

## Cascade discipline check (final)

Hard guards verified untouched verbatim:

- §5.4 + §2.4a [LOCKED] naming conventions — no new names introduced (all R2/R3/RN body language is mechanical).
- 2026-04-25 content-skeleton verbatim — no civ / tower / commander / boss names appear in any locked body.
- 2026-04-26 attack-type lock — RPS read-only (R3 Body-D references RPS-strong as priority axis only).
- §4.1 commander-as-summoned-ability-avatar — Commander explicitly excluded from §4.4 surface (Axis 1 cell A1.1).
- §4.4a Builder — explicitly excluded from §4.4 surface (Axis 1 cell A1.2).
- §4.11.4 (f) speed magnitudes — read-only verbatim (Axis 2 cell A2.1).
- §3.4 "waypoint-style commands, not full RTS per-unit micro" floor — structurally defended at all tiers (Axis 1 cells A1.3 + A1.4).
- Per-commander R1-R5 lane locks (Hard) — untouched (Commander excluded from §4.4 surface).
- Per-tower R1-RN — read-only.
- Per-civ R1-RN — read-only.
- Three-civ-three-equation-form fingerprint — preserved (Axis 2 cell A2.4 + Spine-doc civ-neutrality paragraph).
- §4.7 Option C + R11 wave-composition variance grammar (LOCKED 2026-05-06) — read-only.
- Cultural-sensitivity Follow-up #5 hard-gate — preserved (no per-unit-archetype roster authoring; spec-level archetype-tier grain only).

Cascade-lint expected clean post-merge (only carried `92-files-vs-86-rows` finding pre-existing — RN adds 1 file + 1 table row, finding becomes 93-vs-87, structural condition unchanged).

## Reason

R1-R3 produced four locked bodies; RN's role is to (a) verify cross-property coherence empirically, (b) merge the locked bodies into the §4.4 spine-doc, and (c) tick the exit-gate item. The 3-axis audit at 12 cells is the falsifiable artifact — every cell that PASSes raises the structural confidence that the locked grammar can survive Phase-5 numerics instantiation without re-opening the design surface. The spine-doc edit makes the resolution durable: `concept/phase-4.md §4.4` is the consult-on-every-Phase-5-step surface; folding R2 + R3 inline (with decision-file pointers for full reasoning) avoids the trap of "future Claude re-derives the control model from prose ambiguity."

## Reversibility

**Medium.** RN is composition-only — every body it audits was already locked at R2/R3, and the spine-doc edit is mechanical (inline tables + paragraph rewrite, no new design content). Reverting RN re-opens the OPEN BLOCKER without dropping any of R1/R2/R3's content (which remain in their decision files). However, the §4.8 exit-gate tick is sticky — reverting it would also require re-opening Phase 4 exit conditions, which has cascade impact on the Phase-5-readiness gate. Treat the tick as a Phase-boundary commitment.

## Follow-ups

None new. RN closes the arc.

Phase 4 OPEN exit-gate items remaining (6 of 11):

1. Fusion-numerics balance-pass (Numbers-phase candidate; magnitudes [PROPOSAL]).
2. Economy paper-balance ratification (Tribute + Divinity income curves; numerics [PROPOSAL]).
3. Monetization model specifics resolved (cosmetic-only; no-pay-to-win).
4. Engine choice locked (leading: Godot 4 per phase-5.md §5.5).
5. Art director engaged or scoped.
6. Cultural-sensitivity pass scheduled (2026-04-25 Follow-up #5; locked to Phase-4 exit per [post-arc ratifications](2026-05-06-post-arc-ratifications.md) item 4).

Next-track candidates surface at the next PM gate (post-RN dual-push). PM autonomy mandate carries.
