# Decision — §4.4 mobile unit control sub-pass R3: spec-grammar authoring (speed ladder + pathing-mode catalog + engagement-rule catalog)

**Date:** 2026-05-06
**Status:** Accepted
**Reversibility:** Medium
**Affects:** [`concept/phase-4.md §4.4`](../concept/phase-4.md) (mobile-unit spec-grammar bodies — spine-doc edit lands at RN), [`§4.8`](../concept/phase-4.md) (exit-gate item #5 — tick lands at RN), [`decisions/2026-05-06-mobile-unit-control-r2-direction-lock.md`](2026-05-06-mobile-unit-control-r2-direction-lock.md) (R2 direction lock — read-only input; this round enumerates Body-1 + Body-2 verbatim), [`decisions/2026-05-06-mobile-unit-control-r1-scope.md`](2026-05-06-mobile-unit-control-r1-scope.md) (R1 scope — read-only input), [`concept/phase-4.md §4.11.4`](../concept/phase-4.md) (`f_base = 50 u/s` + archetype multipliers — read-only input; this round maps the 4-tier ladder to existing archetypes, no magnitude re-authoring), [`decisions/2026-05-05-balance-pass-2-round-4-map-speed.md`](2026-05-05-balance-pass-2-round-4-map-speed.md) (Numbers-phase #13 R4 speed lock — read-only), [`concept/phase-3.md §3.4`](../concept/phase-3.md) ("waypoint-style commands, not full RTS per-unit micro" floor — read-only; per-rule falsification gate target), [`decisions/2026-04-27-commander-as-summoned-ability-avatar.md`](2026-04-27-commander-as-summoned-ability-avatar.md) (Commander excluded from §4.4 surface — read-only), [`concept/phase-4.md §4.4a`](../concept/phase-4.md) (Builder excluded from §4.4 surface — read-only).

---

## Decision

R3 authors the three remaining spec-grammars at spec-level grain and lands the R2-handed-down aggro tie-breaker resolution. Per-archetype values stay Phase 5 (per-unit roster instantiation under Follow-up #5 cultural-sensitivity hard-gate).

1. **Body A — Movement-speed-per-tier ladder.** Maps the 4-tier mobile-unit ladder (T1 swarm / T2 mainline / T3 elite / T4 Demigod) to existing §4.11.4 archetype multipliers; reads `f_base = 50 u/s` + archetype × verbatim. No new magnitudes.
2. **Body B — Pathing-mode catalog enumeration.** Enumerates R2 Body-1's four mode flags (`Patrol` / `Follow-Lane` / `Hold` / `Attack-Move`) with one-line spec-level semantics each.
3. **Body C — Engagement-rule catalog enumeration.** Enumerates R2 Body-2's three defaults (`R_engage` / `HP_fall_back` / `Hold_fire`) plus the aggro-priority shape with one-line spec-level semantics + a per-rule falsification gate against §3.4 floor at each of T1 / T2 / T3 / T4.
4. **Body D — Aggro tie-breaker resolution (R2-handed-down).** R2 deferred a falsification gate on the RPS-strong → low-HP → nearest priority shape (eagle-vs-near-dead-berserker scenario). R3 lands the resolution: keep the locked priority but add a stable-sort discipline + an explicit "no per-target manual override" reaffirmation. No structural change to the priority shape.

R4 (RN) integrates these bodies into the §4.4 spine-doc edit and ticks `§4.8` exit-gate item #5.

## Context

R2 locked Option (i) waypoint + mode-flags as the §4.4 control model with three bodies (4-flag catalog / 3-default engagement shape / no-tier-scaling control-surface principle). R3 extends each body into spec-level grammar:

- The §4.4 OPEN ISSUE prose names four needs: movement speed per unit tier / pathing mode catalog / engagement rules / control complexity. R2 closed the **control-complexity** need (Body 3 no-tier-scaling). R3 closes the remaining three.
- §4.11.4 (f) speed magnitudes are locked verbatim (Numbers-phase #13 R4, Hard-class). R3 maps the 4-tier mobile-unit ladder onto the existing archetype-multiplier table — does not author magnitudes. The mapping is conceptual: "T1 swarm uses Swarm-archetype multiplier" is a *spec-grammar* binding, not a numeric re-authoring.
- §3.4 floor ("waypoint-style commands, not full RTS per-unit micro") is the falsification target. Each rule in Body B / Body C must defend the floor at every tier T1-T4. R2 Body-3's no-tier-scaling principle pre-supplies the structural defense (no tier exposes new buttons). R3's per-rule gate is the empirical re-check.
- R2 Body-2.1's aggro-priority shape was flagged for tie-breaker brittleness ("RPS-favorable target picked over near-dead higher-priority threat"). R3 was handed the resolution decision; the result is **structural preservation** of the priority + stable-sort discipline, not addition of player-override surface (which would void Body-3's no-buttons rule).

Six load-bearing surfaces hold from R2 + R1 (verbatim):

1. §4.1 commander-as-summoned-ability-avatar — Commander excluded.
2. §4.4a Builder — excluded.
3. §3.4 floor — per-rule falsification target.
4. §4.11.4 (f) speed magnitudes — read-only; Body A maps tiers to existing rows.
5. §4.10 7-attack × 5-armor RPS — read-only; Body D references RPS-strong as priority axis only.
6. Three-civ-three-equation-form fingerprint — civ-neutral by construction (every rule applies identically to Greek / Aztec / Norse rosters).

## Body A — Movement-speed-per-tier ladder (locked, spec-level)

The 4-tier mobile-unit ladder maps onto the §4.11.4 archetype-multiplier table per the binding below. Per-unit values (within an archetype) are Phase-5 territory — this round locks the *tier-to-archetype* binding only.

| Mobile-unit tier | Bound archetype | Multiplier (×) | Speed (u/s) | Spec-level rationale |
|---|---|---|---|---|
| **T1 swarm** | Swarm | 1.5 | 75 | T1 swarm units exist to apply tempo pressure; faster-than-base reads as "wave of small units crossing the lane before towers can saturate." |
| **T2 mainline** | Standard | 1.0 | 50 | T2 mainline is the spec-anchor — `f_base` exactly. Every other tier's speed is interpreted relative to this floor. |
| **T3 elite** | Standard | 1.0 | 50 | T3 elite trades speed for HP + signature passive; reads as "harder to kill, not faster to arrive." Sharing Standard with T2 is intentional — tier expression lives in stats + passives per R2 Body-3, not in speed. |
| **T4 Demigod** | Boss | 0.7 | 35 | T4 Demigod is per-civ-unique and rare; the slower speed reads as "lumbering threat that *must* be answered" rather than "fast surprise." Mirrors enemy Boss-archetype semantics by design — symmetric tempo across both sides. |

**Builder exemption (verbatim from §4.4a).** Builders walk a deterministic walkable-build-grid path; they consume their own speed value (Phase-5 numerics) which is unrelated to this ladder. They do not occupy a tier on this table.

**Commander exemption (verbatim from §4.1).** Commander emerges only on cast and despawns at cast end; cast-window ability animations are governed by per-commander R5 spec, not by this ladder. Commander does not occupy a tier on this table.

**Per-civ neutrality.** The mapping is identical for every civ's roster. Greek hoplites at T2 mainline, Aztec mainlines at T2, and Norse mainlines at T2 all read the Standard ×1.0 row. Per-archetype-within-tier numeric variation is Phase-5 + Follow-up #5 territory.

**No new magnitudes.** This round binds T1→Swarm, T2/T3→Standard, T4→Boss. The ×1.5 / ×1.0 / ×0.7 are §4.11.4 verbatim. R4 numeric ratification is *not* re-opened by this round.

## Body B — Pathing-mode catalog enumeration (locked, spec-level)

Enumerates R2 Body-1's four mode flags with one-line spec-level semantics each. The catalog is exhaustive at the §4.4-prose grain by construction.

| Flag | One-line spec-level semantics |
|---|---|
| **Patrol** | On waypoint issue, oscillate between waypoint A and the issuing-anchor. Cycle length = `2 · |A − anchor|`. Re-walk on cycle reset. Auto-engage applies (Body C `R_engage`); on engagement end, resume cycle from current position. Civ-neutral. |
| **Follow-Lane** *(default)* | On spawn or anchor-reset, walk toward the per-map authored lane-objective (gate the player defends, or enemy spawn the player pressures). Auto-engage applies; on engagement end, resume lane-walk from current position. The lane-objective is read from per-map authoring (Phase 5 per-map sub-pass), not authored here. |
| **Hold** | On flag-set, freeze position. Do not pursue. Auto-engage applies *only within `R_engage` and only without leaving the hold cell* (turn-and-fire, never pursue). On engagement end, remain at hold cell. |
| **Attack-Move** | On waypoint issue, walk toward waypoint. Auto-engage applies en route. On engagement end, resume waypoint-walk from current position. On reaching waypoint without engagement, behavior collapses to `Hold` at the waypoint cell. |

**Catalog exhaustivity gate.** The §4.4 prose names four modes ("patrol, follow lane, direct to waypoint, attack-move"). The Body-B enumeration covers all four:

- "patrol" → `Patrol`.
- "follow lane" → `Follow-Lane`.
- "direct to waypoint" → covered by `Follow-Lane` if the waypoint is the lane-objective, by `Attack-Move` if engagement en route is desired, or by `Hold` if the waypoint is "stay here." Three of the four flags collectively span the prose's "direct to waypoint" intent.
- "attack-move" → `Attack-Move`.

No fifth flag is needed; adding one would be scope creep against the §4.4 prose grain.

**Group-select behavior (locked at spec-level).** Box-select issues identical waypoints to each unit. Each unit retains its own active mode flag — group-select does *not* override individual flags. A separate group-flag-cycle UI is **deferred to Phase 5** (visual affordance grain). At spec-level, the rule is: `group_select(units).waypoint(wp)` ≡ `for u in units: u.waypoint(wp)`; flags untouched.

## Body C — Engagement-rule catalog enumeration (locked, spec-level)

Enumerates R2 Body-2's three defaults plus the aggro-priority shape with one-line spec-level semantics + a per-rule falsification gate.

| Rule | One-line spec-level semantics | Falsification gate (§3.4 floor at T1 / T2 / T3 / T4) |
|---|---|---|
| **`R_engage` (auto-engage radius)** | Within `R_engage` of the unit, the unit selects a target via aggro-priority (Body 2.1 → resolved in Body D below) and engages. Outside, the unit walks per active mode flag. Per-archetype-within-tier values are Phase-5 numerics; the *shape* (single radius, no per-mode override, no player-tunable threshold mid-match) is locked here. | **Pass at all 4 tiers.** A single radius with no player override at any tier is structurally inside the floor — the player issues a waypoint + flag, the unit decides who to shoot inside `R_engage`. T1 swarm has the same `R_engage` shape as T4 Demigod; tier expresses through the *value* (Phase 5), not the *surface*. No tier exposes a "set R_engage" button. |
| **`HP_fall_back` (fall-back-at-HP%)** | Below `HP_fall_back · HP_max`, the unit disengages (interrupts the engagement only) and walks toward the nearest friendly anchor (spawn / Builder / Commander cast-point). Active mode flag is preserved; on reaching the anchor, the unit resumes the flag's behavior. Threshold value is per-archetype-within-tier (Phase 5); the *shape* (single threshold, deterministic anchor selection, mode preserved) is locked here. | **Pass at all 4 tiers.** Single threshold, deterministic destination, no player-tunable percentage mid-match. T1 swarm fall-back at (e.g.) 30% HP is structurally identical to T4 Demigod fall-back at (e.g.) 50% HP — only the value differs. The player does not pick the anchor; the rule does. No tier exposes a "set HP_fall_back" button. |
| **`Hold_fire` (binary toggle)** | Per-unit binary toggle. When on, the unit ignores `R_engage` entirely and executes movement only. When off (default), `R_engage` applies. Toggle is a separate UI affordance from the mode-flag cycle (per R2 Body-2). | **Pass at all 4 tiers.** Binary surface with no value-tuning. Identical at every tier — T1 swarm `Hold_fire` ≡ T4 Demigod `Hold_fire`. The toggle exists because the floor of `R_engage` is "auto-engage when in range" and one specific use-case (retreat under AOE focus) needs a suppression affordance. Single toggle is the smallest viable surface; alternative would be reopening per-target manual override which voids R2 Body-3. |
| **Aggro-priority** *(see Body D for tie-breaker)* | When multiple targets are in `R_engage`, the unit selects: (1) the target whose attack type the unit's armor type is strong against (per §4.10 RPS), if ≥1 such target exists; (2) else, the target with the lowest current HP; (3) else (tie), the target nearest to the unit. Stable-sort discipline (Body D) resolves order across simultaneous spawns. | **Pass at all 4 tiers.** Three-step priority is rules-driven; the player issues the engagement (waypoint + flag) and the unit decides *which* target to shoot. No tier exposes a "force-attack target X" button. T1 swarm uses the same priority as T4 Demigod. |

**Cross-rule coherence.** The four rules compose: a unit in `R_engage` of multiple targets selects via aggro-priority, engages until target dies / target leaves `R_engage` / unit drops below `HP_fall_back · HP_max` (whichever comes first). `Hold_fire` short-circuits the entire chain when on. Mode flag (`Patrol` / `Follow-Lane` / `Hold` / `Attack-Move`) governs what the unit does *between* engagements — never *during*. The catalog is closed; no fifth rule is needed.

**Builder + Commander exemptions (verbatim).** Builders carry no engagement rules (no AI). Commander rules live in per-commander R5 spec, not here.

## Body D — Aggro tie-breaker resolution (R2-handed-down)

R2 Body-2.1 named a brittle scenario: a Greek hoplite (Pierce-strong vs Beast) sees both an Aztec eagle (Beast — RPS-favorable) and a Norse berserker (Slashing — RPS-unfavorable) at 10% HP. The locked priority picks the eagle; the berserker kills the tower. R2 deferred the resolution to R3.

**Resolution:** **Keep the locked priority shape unchanged.** Add two narrow disciplines:

1. **Stable-sort discipline.** When the priority comparison ties at every step (RPS-equal, HP-equal, distance-equal), tie-break by spawn-order (lower entity-id first). Deterministic and replayable; no player surface.
2. **No-override reaffirmation.** The player has **no per-target manual override**. The eagle-vs-berserker scenario is resolved by tower placement, civ matchup, and R_engage tuning (Phase 5 numerics) — not by adding a "force-attack" button at the per-unit grain.

**Why the locked priority survives the brittleness critique.** Three reasons:

1. **The brittleness is the floor in action.** The §3.4 floor is "waypoint-style commands, not full RTS per-unit micro." A scenario where the *automatic* aggro-priority makes a "wrong" pick from the player's perspective is the *signature* of the floor working as intended. If the priority always made the player-optimal pick, the surface would be redundant — the player could trust auto-engage to be perfect, and the engagement-rules grammar would be doing zero load-bearing work.
2. **The fix-space is upstream, not in this rule.** The eagle-vs-berserker outcome is a function of (a) tower placement (was the hoplite the only response?), (b) civ matchup (does Greek have a Beast-coverage hole that should've been filled by Aztec/Norse multi-civ play?), (c) per-archetype `R_engage` value (is the radius too generous?). All three live in Phase-5 numerics or Phase-4 per-civ R1-RN matchup_affinity (already locked). R3 cannot resolve the brittleness here without breaking R2 Body-3's no-button rule.
3. **Adding override breaks the three-civ-three-equation-form fingerprint.** A per-target manual override would advantage the civ whose mechanical lean rewards micro most — likely Norse (summon-cleave-propagation rewards positioning per-summoned-unit). The fingerprint demands surface-neutrality across all three civs; locking the priority + disallowing override preserves it.

**Stable-sort applies uniformly across all four tiers.** T1 swarm and T4 Demigod both use the same three-step priority with the same spawn-order tie-break. No tier deviation.

## Reason chosen

Three reinforcing reasons:

1. **Body A binds without re-authoring magnitudes.** The 4-tier mobile-unit ladder maps onto existing §4.11.4 archetype rows (T1→Swarm / T2,T3→Standard / T4→Boss). The `f_base` + multiplier values are read-only Numbers-phase #13 R4 locks; this round adds a binding, not a magnitude. R4 (RN) audits the binding against §4.11.4 verbatim — no Hard-class supersession risk.
2. **Body B + Body C enumerate R2 verbatim with falsification gates.** Each pathing-mode and engagement-rule entry has one-line semantics matching R2 Body-1 / Body-2 verbatim plus an explicit per-tier §3.4 floor falsification — every rule passes at T1 / T2 / T3 / T4 because R2 Body-3's no-tier-scaling principle pre-supplies the structural defense (no tier exposes new buttons).
3. **Body D resolves R2's handed-down brittleness without expanding surface.** Stable-sort + no-override-reaffirmation is the smallest fix that preserves the priority shape, the no-buttons rule, the three-civ fingerprint, and the §3.4 floor simultaneously. The brittleness is reframed as a feature of the floor, with the fix-space relocated upstream to placement / matchup / Phase-5 numerics.

### 3x debug loop

**Loop 1 — aggressive critique.** Body A's tier-to-archetype binding is suspicious: T2 mainline and T3 elite share Standard ×1.0 / 50 u/s. A reader looking at the table will ask "why does T3 elite move at the same speed as T2 mainline if T3 is meant to feel different?" — and the spec-level answer ("tier expresses through stats + passives, not speed") is correct but reads as hand-waving without empirical demonstration that T3 actually *feels* different in playtest. Furthermore, T4 Demigod at Boss ×0.7 / 35 u/s is half the speed of T1 swarm; if T4 is rare per-civ-unique and T1 is mass-spawned, the lane will read as "T1 cloud crossing while T4 lumbers behind" — which may be the intent (legibility-by-tempo) or may be a bad pacing surface (T4 arrives long after the moment the player needed it). The mapping needs Phase-5 playtest validation, which R3 cannot supply.

Body B's group-select rule (`group_select.waypoint(wp)` ≡ `for u in units: u.waypoint(wp)`; flags untouched) is too permissive — it allows the player to "smart-select" only `Hold`-flagged units in a group, issue a waypoint to all, and effectively bulk-toggle them out of `Hold` without pressing the flag-cycle. That's a soft-micro affordance the floor was supposed to forbid.

Body C's `HP_fall_back` rule has a deterministic-anchor-selection bug: "nearest friendly anchor (spawn / Builder / Commander cast-point)" — what if the nearest is a Builder mid-walk that despawns on arrival 0.5s later? The unit walks toward a stale destination, gets caught alone, dies. The rule needs a "stable anchor" filter (Builders excluded as anchors — only spawn + Commander cast-point) to be safe.

Body D's stable-sort fix is correct but the "brittleness is the floor in action" framing is weak — calling a UX failure mode "the floor working as intended" is the kind of justification that reviewers correctly flag as designer-rationalization. The framing should acknowledge the cost (player frustration in the eagle-vs-berserker scenario) before invoking the floor.

**Loop 2 — steelman.** Body A's T2/T3 sharing Standard ×1.0 is *the entire point* of R2 Body-3 — control surface does not scale, and *speed is part of control surface in playtest perception*. If T3 moved faster than T2, the player would experience it as "T3 has a different control feel" which voids the no-tier-scaling principle. T3's tier expression must live entirely in stats + passives. The T4 Boss ×0.7 / 35 u/s slow is also intentional: per-civ-unique T4 Demigod is meant to feel like a rare summoned heavyweight, not a fast skirmisher; the lumbering tempo is *the* sign of T4. Phase-5 playtest validation is the right venue for empirical confirmation, but the spec-grammar binding is correct.

Body B's group-select smart-select critique is real but Phase-5 territory: the *spec-level* rule ("flags untouched on box-select") is correct; the *UX* rule ("box-select cannot bulk-toggle flags via waypoint") is what Phase 5 implements. R3 cannot legislate UX without expanding scope into UI-affordance authoring (deferred to Phase 5 + Follow-up #5 explicitly).

Body C's `HP_fall_back` Builder-as-stale-anchor critique is real and actionable at spec-level. **Adopt it.** The rule body is updated to: "nearest friendly **stable** anchor (spawn / Commander cast-point); Builders are *not* valid anchors per their walk-and-despawn lifecycle." This is a one-word add that closes the bug without scope expansion.

Body D's framing critique is also fair. **Adopt the softening.** The opening sentence of "Why the locked priority survives" is rewritten to acknowledge cost first: "The eagle-vs-berserker scenario produces a player-frustrating outcome; resolving it inside this rule is wrong because…" The floor argument follows the cost acknowledgment, not the other way around.

**Loop 3 — synthesis.** Body A locks as drafted (T2/T3-share-Standard is feature-not-bug per R2 Body-3; T4 lumbering tempo is feature-not-bug per Demigod rarity narrative). Body B locks as drafted (group-select rule is spec-level correct; UX deferral to Phase 5 is on-discipline). Body C lock-with-Loop-2-edit (Builders excluded as anchors). Body D lock-with-Loop-2-edit (cost-acknowledged framing).

**Synthesis-locked output:** Bodies A / B / C / D as authored, with the two Loop-2-adopted edits applied below.

---

**Loop-2-adopted edit to Body C `HP_fall_back`:** anchor-selection rule reads "nearest friendly **stable** anchor (spawn / Commander cast-point); Builders are *not* valid anchors (their walk-and-despawn lifecycle would orphan units mid-fall-back)."

**Loop-2-adopted edit to Body D opening framing:** the eagle-vs-berserker scenario produces a player-frustrating outcome; that frustration is real, not dismissible. R3's choice to leave the priority shape unchanged accepts that cost in exchange for preserving the §3.4 floor, R2 Body-3's no-buttons rule, and the three-civ-fingerprint surface neutrality. The fix-space is relocated upstream (tower placement, civ matchup, Phase-5 `R_engage` value tuning) — three legitimate venues that *do* belong in this game's design surface, vs. a per-target manual override that does not.

## Cross-property coherence hook (R4 RN)

R4 RN integrates Bodies A / B / C / D into the §4.4 spine-doc edit and runs the 3-axis cross-arc audit per R1 scope:

- **Axis 1 — §4.1 + §4.4a + §3.4 floor.** Verifies Bodies A-D do not silently re-introduce a controllable on-field Commander surface (R2 Body-3's no-buttons rule + Body D's no-override reaffirmation pre-supply the structural defense; RN re-checks per-rule). Verifies Builder remains zero-control (Body A's Builder exemption + Body C's Builder-as-non-anchor are explicit). Verifies §3.4 floor at T1 / T2 / T3 / T4 (Body C's per-rule falsification gate pre-supplies; RN integrates).
- **Axis 2 — §4.11.4 (f) magnitude consistency.** Verifies Body A's tier-to-archetype binding reads §4.11.4 verbatim (Swarm ×1.5 = 75 u/s / Standard ×1.0 = 50 u/s / Boss ×0.7 = 35 u/s — no magnitude restatement; binding is conceptual). Verifies no Phase-5 numeric authoring leaked into R3 (R3's `R_engage` / `HP_fall_back` / aggro priority are *shapes*; values stay Phase 5).
- **Axis 3 — Control-surface tier-scaling at T1 / T2 / T3 / T4.** Verifies Body B + Body C exposed at every tier are identical (4 flags + 3 rules + 1 toggle, no T3/T4 additions). Verifies Body A's T2/T3 speed-share is consistent with R2 Body-3's no-tier-scaling principle (speed is per-archetype-tagged stat, not control-surface affordance). Verifies T4 Boss-archetype slow is *narrative-tagged* not control-surface-tagged (T4 doesn't get extra controls because it's slow — speed and control surface are decoupled axes).

**RN spine-doc edit deliverables:** `phase-4.md §4.4` OPEN ISSUE → locked control-model body merged from R2 Bodies 1-3 + R3 Bodies A-D. Inline tables for the tier-to-archetype mapping (Body A) + the pathing-mode catalog (Body B) + the engagement-rule catalog (Body C). `§4.8` exit-gate item #5 ✅ tick. CASCADE pointer + decisions table + version footer bump (0.78 → 0.79). PROGRESS appended; R2 archived.

## Reversibility note

**Medium.** Reverting requires:

1. Superseding decision file naming a different tier-to-archetype binding (Body A) or a different catalog enumeration (Body B / C) or a different aggro-priority shape (Body D).
2. R4 RN spine-doc edit reverted (OPEN ISSUE prose restored; tier-to-archetype + catalog tables removed; §4.8 item #5 un-ticked).
3. Cross-arc parity to §4.11.4 + §3.4 + §4.1 + §4.4a re-validated.

Each reversal is a single decision file + bounded edits. Numbers-phase #13 R4 (Hard-class) is not under negotiation — Body A's binding can be re-authored; the underlying magnitudes cannot.

**Hard-class guards verified untouched (R1+R2 verbatim list re-confirmed):**

- §5.4 [LOCKED] / §2.4a [LOCKED] — untouched.
- 2026-04-25 locked content skeleton — no civ / tower / commander / boss names appear in this round's bodies (Body A's "Greek hoplites / Aztec mainlines / Norse mainlines" are illustrative roster-class references, not name authoring).
- 2026-04-26 attack-type lock — Body C aggro-priority references §4.10 RPS read-only; no taxonomy modification.
- §4.1 commander-as-summoned-ability-avatar — Body A + Body B + Body C + Body D explicitly exclude Commander.
- §4.4a Builder — Body A + Body B + Body C explicitly exclude Builder; Body C's anchor-rule edit makes the exclusion stronger (Builder-as-non-anchor).
- §4.11.4 (f) speed magnitudes — Body A binds tiers to existing rows; no new magnitudes; Numbers-phase #13 R4 lock untouched.
- §3.4 control-complexity floor — Body C per-rule falsification gate verified pass at all 4 tiers; floor preserved.
- Per-commander R1-R5 lane locks (Hard) — no commander reference; lanes untouched.
- Per-tower R1-RN magnitude matrix — no tower reference.
- Per-civ R1-RN profiles + signature_creep_types — no per-civ unit-roster authoring; civ-neutral mechanical-content language throughout.
- Three-civ-three-equation-form fingerprint — Body D's no-override reaffirmation makes the fingerprint preservation explicit (rejects Norse-favoring micro surface).
- §4.7 Option C + R11 wave-composition variance grammar — untouched.
- Spec-level scope discipline — R3 authors *grammar-level* shapes only; per-archetype `R_engage` / `HP_fall_back` / per-tier-within-archetype value tuning is Phase 5.

## Follow-ups

- **R4 (RN) next** — 3-axis cross-arc audit (per Cross-property coherence hook above) + `phase-4.md §4.4` spine-doc edits (OPEN ISSUE → locked control-model body merged from R2 Bodies 1-3 + R3 Bodies A-D) + `§4.8` exit-gate item #5 ✅ tick + arc close. Dual-push event 4 of 4.
- **Phase-5 deferrals (verbatim):** per-archetype-within-tier `R_engage` values; per-archetype `HP_fall_back` thresholds; per-civ-roster instantiation under Follow-up #5 cultural-sensitivity hard-gate; group-select UI affordance specifics; per-flag visual treatments; `Hold_fire` toggle visual.
- **Per-map authoring sub-pass** unblocks at RN — per-map lane-objective authoring (Body B `Follow-Lane` reads from this) needs the §4.4 RN-locked spec as input.
- **Cascade-lint after this round.**
- **Dual-push** at this checkpoint (R3 dual-push event 3 of 4).
