# Decision — §4.4 mobile unit control sub-pass R2: control-model direction lock (Option i — waypoint + mode-flags)

**Date:** 2026-05-06
**Status:** Accepted
**Reversibility:** Medium
**Affects:** [`concept/phase-4.md §4.4`](../concept/phase-4.md) (mobile-unit control-model body — locked at this round, spine-doc edit lands at RN), [`§4.8`](../concept/phase-4.md) (exit-gate item #5 — tick lands at RN), [`decisions/2026-05-06-mobile-unit-control-r1-scope.md`](2026-05-06-mobile-unit-control-r1-scope.md) (R1 scope — read-only input), [`decisions/2026-04-27-commander-as-summoned-ability-avatar.md`](2026-04-27-commander-as-summoned-ability-avatar.md) (§4.1 commander-summoned-on-cast — read-only), [`concept/phase-4.md §4.4a`](../concept/phase-4.md) (Builder unit class — read-only / explicitly out-of-scope), [`concept/phase-3.md §3.4`](../concept/phase-3.md) ("waypoint-style commands, not full RTS per-unit micro" floor — read-only), [`decisions/2026-05-05-balance-pass-2-round-4-map-speed.md`](2026-05-05-balance-pass-2-round-4-map-speed.md) (`f_base = 50 u/s` + archetype multipliers — read-only).

---

## Decision

**Option (i) — waypoint + mode-flags is locked** as the §4.4 mobile-unit control model. Player issues a waypoint to a unit (or a group via box-select); a per-unit mode flag governs how that waypoint is interpreted and what engagement defaults apply between waypoints. Attack-Move is one of the mode flags (not a separate command). No per-unit ability buttons at any tier. The control surface stays inside §3.4's "waypoint-style commands, not full RTS per-unit micro" floor across all four tiers (T1 swarm / T2 mainline / T3 elite / T4 Demigod).

This round authors three bodies at spec-level grain:

1. **Mode-flags catalog** — the four flags every mobile unit carries, civ-neutral.
2. **Engagement-defaults shape** — the auto-engage / hold-fire / fall-back rules that operate *between* waypoint commands.
3. **Control-surface 4-tier scaling principle** — how (or rather, whether) the surface scales across T1–T4. Spoiler: it does not scale; the surface is constant. Tier expresses through stats + signature ability framing, not through additional control affordances.

R3 will author the spec-grammar bodies (movement-speed-per-tier shape against §4.11.2 (f); pathing-mode catalog with one-line semantics; engagement-rule catalog with one-line semantics + falsification gate). R4 RN integrates into the cross-arc audit and lands the §4.4 spine-doc edits.

## Context

R1 scope (`decisions/2026-05-06-mobile-unit-control-r1-scope.md`) named three candidate models from the §4.4 OPEN ISSUE prose: (i) waypoint + mode-flags, (ii) attack-move-only, (iii) hybrid-with-tier-gated-micro. R1's steelman pointed to (i) on three independent evidentiary streams: §4.4 prose explicitly endorses "Waypoint + mode flags is achievable. Attack-Move command is useful" (pointing to (i)-with-AM-as-one-flag); (ii) collapses the engagement-rules catalog §4.4 needs-list item #3 mandates ("Engagement rules (auto-engage, hold, fall back)") — collapsing the catalog *is* the failure mode the OPEN ISSUE warns against; (iii) hybrid-with-tier-gated-micro adds T3-elite ability buttons that re-introduce on-field-hero adjacency surface superseded 2026-04-27 by the commander-as-summoned-ability-avatar lock.

This round ratifies (i) absent surprise (no fork) per the PM-autonomy mandate, and authors the three bodies the OPEN ISSUE binds.

Six load-bearing surfaces converge on the body content:

1. **§4.1 commander-as-summoned-ability-avatar** — Commander emerges only on cast; the §4.4 control surface must apply only to the 15 launch-roster combat units (5/civ), never to the Commander.
2. **§4.4a Builder unit class** — Builders have no AI, no combat, no waypoint commands; the control surface explicitly excludes them.
3. **§3.4 control-complexity floor** — "waypoint-style commands, not full RTS per-unit micro." The mode-flag count, engagement-defaults arity, and (non-)tier-scaling all defend this floor.
4. **§4.11.2 (f) speed magnitudes** — `f_base = 50 u/s` + archetype multipliers locked; R2 does not author magnitudes (R3's job, against this read-only input).
5. **§4.10 7-attack × 5-armor RPS** — read-only; the engagement-defaults reference attack/armor only via auto-engage radius and aggro-priority shape, no taxonomy modification.
6. **Three-civ-three-equation-form fingerprint** — Greek deceleration-weighted / Aztec kill-multiplication-weighted / Norse summon-cleave-propagation-weighted. The control surface must remain neutral across all three; the four mode flags + four engagement defaults work identically for every civ's roster.

## Body 1 — Mode-flags catalog (locked)

Every mobile unit carries a single active mode flag at any moment. Default on spawn is `Follow-Lane`. The player toggles the flag via a per-unit (or per-group, on box-select) UI affordance — one button, four states, cycle on click. Pressing a movement key (right-click on a destination) issues a waypoint **interpreted by the active mode flag**.

| Flag | One-line semantics | Auto-engage? | Returns to lane after engagement? |
|------|--------------------|--------------|-----------------------------------|
| **Patrol** | Oscillate between waypoint A and the spawn-anchor / last-issued anchor. Re-walk on every cycle. | Yes — within `R_engage` of the patrol path. | Yes — resumes oscillation after target dies / falls out of range. |
| **Follow-Lane** *(default)* | Walk toward the lane-objective (per-map authored anchor — the gate the player is defending or the enemy spawn the player is pressuring). | Yes — within `R_engage` of the unit. | Yes — resumes lane-walk after target dies. |
| **Hold** | Stay at current position. Do not pursue. | Yes — only within `R_engage` and only without leaving the hold cell (turn-and-fire, no chase). | N/A — unit never left the cell. |
| **Attack-Move** | Walk toward the issued waypoint, but pause to engage any target that enters `R_engage`. Resume waypoint-walk on target death / out-of-range. | Yes — every target in `R_engage`. | Yes — resumes waypoint-walk after engagement. |

**Civ-neutral mechanical-content language.** No civ's roster gets exclusive mode flags. The catalog is identical for Greek hoplites, Aztec eagles, Norse berserkers, and every future-launch-roster unit.

**Builder exemption (verbatim from §4.4a).** Builders carry no mode flag; the catalog does not apply. Builders walk a deterministic walkable-build-grid path and despawn on arrival.

**Commander exemption (verbatim from §4.1).** The Commander is not a mobile unit in the §4.4 sense; it emerges only during a cast window and despawns at cast end. The catalog does not apply.

## Body 2 — Engagement-defaults shape (locked)

Engagement defaults operate *between* waypoint commands — once a unit has reached a waypoint (or is mid-walk in `Attack-Move` / `Patrol` / `Follow-Lane`), three rules govern what it does on contact:

| Default | Shape | Per-tier variance? |
|---------|-------|--------------------|
| **`R_engage` (auto-engage radius)** | Per-unit-archetype constant. Within `R_engage`, the unit selects a target from enemies-in-range using aggro-priority shape (Body 2.1). Outside, it walks. | No. Per-archetype value is a Phase-5 number; the *shape* (single radius, no per-mode override) is locked here. |
| **`HP_fall_back` (fall-back-at-HP%)** | Per-unit-archetype constant, expressed as a fraction of max HP. When a unit drops below `HP_fall_back · HP_max` mid-engagement, it disengages and walks toward the nearest friendly anchor (spawn / Builder / Commander cast point). Mode flag is preserved; on reaching anchor, it resumes the flag's behavior. | No. Per-archetype value is a Phase-5 number; the *shape* (single threshold, deterministic anchor selection, mode preserved) is locked here. |
| **`Hold_fire`** | A binary toggle, off by default. When on, the unit ignores `R_engage` and never auto-engages — it executes movement only. Useful for retreat under enemy AOE focus. Toggling is a per-unit UI affordance, separate from the mode-flag cycle. | No. Per-tier behavior is identical. |

**Aggro-priority shape (locked, Body 2.1).** When multiple targets are in `R_engage`, the unit selects:

1. The target whose attack type the unit's armor type is strong against (per §4.10 RPS), if ≥1 such target exists;
2. Else, the target with the lowest current HP;
3. Else (tie), the target nearest to the unit.

Civ-neutral. Floor-respecting (no player override at the per-target grain — that *would* be full RTS micro).

## Body 3 — Control-surface 4-tier scaling principle (locked)

**The control surface does not scale across tiers.** T1 swarm, T2 mainline, T3 elite, and T4 Demigod all expose the same four mode flags + the same three engagement defaults + the same one Hold-fire toggle. Tier difference is expressed through:

- **Stats** — HP, damage, speed, `R_engage` (per-archetype Phase-5 numbers).
- **Signature ability framing** — T3 / T4 archetypes may have a passive (e.g., aura, on-death proc, on-hit status) that fires automatically per the engagement defaults; **no player-triggered active per-unit ability**.
- **Roster slot count** — T1 swarm spawns in groups; T4 Demigod is per-civ-unique and rare.

This is the load-bearing principle that defends §3.4. T3 / T4 units do not get extra buttons; they get more numbers and more passives. The §3.4 floor (and the 2026-04-27 commander-as-summoned-ability-avatar superseding) hold uniformly across the tier ladder.

**Negative space (verbatim non-goals):**

- No ability-button surface on any mobile unit at any tier.
- No per-target manual aggro override (player cannot say "attack *that* one specifically" — aggro is rules-driven).
- No formation commands (no "march in line," "circle," "wedge"). Group-select issues identical waypoints to each unit.
- No active-pause RTS surface. Pause is a meta-affordance (already locked in `togglePause`); it does not expose unit commands during pause.
- No per-unit retreat micro (`Hold_fire` is a defensive toggle, not a kite-micro affordance).

## Reason chosen

Three reinforcing reasons (synthesized against R1's three evidentiary streams):

1. **§4.4 prose-leading endorsement.** R1's quoted prose ("Waypoint + mode flags is achievable. Attack-Move command is useful") points directly at (i)-with-AM-as-one-flag. Body 1 implements exactly this — Attack-Move is one of four mode flags, not a separate command; the surface is the mode-flag cycle + Hold-fire toggle, nothing more.

2. **§4.4 needs-list item #3 (engagement rules) is preserved by (i) and collapsed by (ii).** The §4.4 prose mandates "Engagement rules (auto-engage, hold, fall back)" as a deliverable. Body 2 instantiates all three (`R_engage` auto-engage / `Hold` mode flag / `HP_fall_back` fall-back-at-HP%), each shape locked at spec-level grain. (ii) attack-move-only would have collapsed the catalog (no `Hold`, no `HP_fall_back` because no surface to invoke them) — *that's the failure mode the OPEN ISSUE warned about*. (i) preserves the catalog by construction.

3. **2026-04-27 commander-as-summoned-ability-avatar is preserved by Body-3's no-tier-scaling principle.** The R1 critique of (iii) was that T3-elite ability buttons re-introduce hero-lite adjacency surface. Body 3 makes the no-buttons rule load-bearing across the tier ladder — explicit non-goal. T4 Demigod cannot be a controllable on-field hero, because *no* mobile unit at any tier exposes a button. The §4.1 lock holds uniformly.

### 3x debug loop

**Loop 1 — aggressive critique.** Four flags is too few — players from RTS / hero-shooter backgrounds will demand `Stand Ground`, `Stop`, `Force Attack` (target an ally, neutral, building), `Move-and-Avoid`, etc. The catalog reads as MOBA-lite minus the abilities, which is the worst of both genres: not granular enough for RTS players, not punchy enough for MOBA players. Furthermore, `Hold_fire` as a separate toggle from the mode-flag cycle is a UI-affordance creep — that's *five* states (four flags + one toggle) which is exactly the surface-bloat §3.4 warns against.

The aggro-priority shape (RPS-strong → low-HP → nearest) is also brittle — if a Greek hoplite sees both an Aztec eagle (RPS-favorable matchup) and a Norse berserker (RPS-unfavorable, but at 10% HP about to nuke a tower), the rule auto-selects the eagle and the berserker kills the tower. Players will read this as "the AI is dumb" and reach for the manual override that Body 2's "no per-target manual aggro override" non-goal forbids.

**Loop 2 — steelman.** On flag count: the four chosen are *exactly* the four §4.4 prose names — "patrol, follow lane, direct to waypoint, attack-move." `Direct to waypoint` is `Follow-Lane` if the lane-objective happens to *be* the waypoint, or `Attack-Move` if engagement is desired en route, or `Hold` if the waypoint is "stay here." The catalog is exhaustive at the §4.4-prose grain by construction — adding more flags is scope creep, not feature parity.

On `Hold_fire` separation: a binary defensive toggle is materially different from a movement-mode flag. Combining them into a five-state cycle would force the player to cycle through irrelevant states to reach the desired one (e.g., `Patrol → Hold → Follow-Lane → Attack-Move → Hold-fire-On → Hold-fire-Off → Patrol…`). Separating them is *less* surface, not more — two short cycles are easier to operate than one long one.

On aggro brittleness: the failure mode (eagle picked over near-dead berserker) is real but proves the *engagement defaults* shape, not refutes it. The fix is in `R_engage` value tuning + tower placement decisions (the player chose to put the hoplite where both targets were in range), not in adding a per-target override surface that breaks the §3.4 floor. The MOBA-comparison reach is misplaced: this is a TD with mobile-unit auxiliary, not a hero shooter — RTS-comparable depth lives in tower placement, civ matchup, and wave-composition response, not in per-unit micro.

The five-states-is-bloat critique inverts the geometry: the alternative isn't four flags + zero toggle, it's four flags + emergency-only toggle. `Hold_fire` exists because the floor of `R_engage` is "auto-engage when in range," and there is one specific case (retreat under AOE focus) where the player needs to *suppress* engagement temporarily. That case is real; the toggle resolves it without re-opening per-target micro.

**Loop 3 — synthesis.** The catalog is right at four flags + one toggle. The aggro-priority shape is correct *and* the brittleness is real — Body 2.1 deserves a falsification gate at R3 ("does the rule produce 'wrong' target selection > X% of the time in canonical engagement scenarios? if yes, R3 may add a tie-breaker before nearest, e.g., 'highest projected DPS to friendly assets'") but the gate stays at spec-grammar grain, not per-target manual override. Cross-property coherence hook to R3 carries the falsification gate forward.

**Synthesis-locked output:** Body 1 (4 flags) + Body 2 (3 engagement defaults + 1 Hold-fire toggle + aggro-priority shape with R3 falsification gate) + Body 3 (no-tier-scaling principle) lock as authored.

## Cross-property coherence hook (R3)

R3 spec-grammars must author against the locked direction:

- **Pathing-mode catalog (R3 deliverable b)** enumerates the four mode flags from Body 1 with one-line semantics each. R3 does not introduce additional flags; the catalog matches Body 1 verbatim.
- **Engagement-rule catalog (R3 deliverable c)** enumerates `R_engage` / `HP_fall_back` / `Hold_fire` from Body 2 with one-line semantics each + the aggro-priority shape from Body 2.1. R3 lands the falsification gate against §3.4 floor at all 4 tiers (does the rule produce floor-violating per-unit micro at any tier? — Body 3's no-tier-scaling principle answers "no" structurally; R3 verifies per-rule).
- **Movement-speed-per-tier shape (R3 deliverable a)** reads against `§4.11.2 (f) f_base = 50 u/s` + archetype multipliers verbatim. R3 authors the per-tier multiplier ladder at archetype-tier grain (T1 / T2 / T3 / T4); Body 3's no-tier-scaling principle applies to *control surface*, not to *stats* — speed values *do* vary per tier.
- **Falsification gate inheritance.** R3's per-rule falsification against §3.4 + §4.11.2 (f) inherits this round's locked direction. If R3 finds a rule that violates the floor, the rule is the violation, not the direction.

## Reversibility note

**Medium.** Reverting requires a superseding decision file naming a different option (ii or iii) + reauthoring Bodies 1 / 2 / 3 against the new direction. R3 spec-grammars become invalid (catalog enumeration mismatch); RN spine-doc edit becomes invalid (control-model body merge would point to wrong direction). Cascade-impact bounded to §4.4 — `§4.1` / `§4.4a` / `§4.11.2 (f)` / `§3.4` floor are upstream and untouched.

**Hard-class guards verified untouched (R1 verbatim list):**

- §5.4 [LOCKED] / §2.4a [LOCKED] — untouched.
- 2026-04-25 locked content skeleton — no civ / tower / commander / boss names appear in this round's bodies.
- 2026-04-26 attack-type lock — engagement-defaults references `§4.10 RPS` read-only; no taxonomy modification.
- §4.1 commander-as-summoned-ability-avatar — Body 1 + Body 3 explicitly exclude Commander; no controllable on-field surface.
- §4.4a Builder — Body 1 explicitly excludes Builder; zero-control preserved.
- §4.11.2 (f) speed magnitudes — this round does not reference magnitudes (R3's job).
- §3.4 control-complexity floor — Body 3 makes no-tier-scaling load-bearing; floor preserved structurally.
- Per-commander R1-R5 lane locks (Hard) — no commander reference; lanes untouched.
- Per-tower R1-RN magnitude matrix — no tower reference.
- Per-civ R1-RN profiles + signature_creep_types — no per-civ unit-roster authoring; civ-neutral mechanical-content language throughout.
- Three-civ-three-equation-form fingerprint — Body 1 + Body 2 + Body 3 are civ-neutral by construction; fingerprint preserved.
- §4.7 Option C + R11 wave-composition variance grammar — untouched; no enemy-direction or wave-variance reference.

## Follow-ups

- **R3 next** — author spec-grammar bodies (movement-speed-per-tier shape against §4.11.2 (f); pathing-mode catalog with one-line semantics matching Body 1; engagement-rule catalog with one-line semantics matching Body 2 + falsification gate against §3.4 floor at all 4 tiers + Body 2.1 aggro-tie-breaker falsification gate).
- **R4 (RN)** — 3-axis cross-arc audit (§4.1 + §4.4a + §3.4 floor / §4.11.2 (f) magnitude consistency / control-surface tier-scaling at T1-T4) + `phase-4.md §4.4` spine-doc edits (OPEN ISSUE → locked control-model body merged from Bodies 1-3 + R3 spec-grammars) + `§4.8` exit-gate item #5 ✅ tick.
- **Phase-5 deferrals (verbatim from R1):** per-unit-archetype `R_engage` / `HP_fall_back` / archetype-multiplier values; per-civ-roster instantiation under Follow-up #5 cultural-sensitivity hard-gate.
- **UI-affordance specifics** (mode-flag cycle button visual, Hold-fire toggle visual, group-select rules, group-flag-cycle behavior) deferred to Phase 5 + Follow-up #5; this round locks the *shape* (one button, four states, cycle on click; separate Hold-fire toggle), not the visual.
- **Cascade-lint after this round.**
- **Dual-push** at this checkpoint (R2 dual-push event 2 of 4).
