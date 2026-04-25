# Decision — Balance-pass #1 (conceptual frame): Tower-vs-Unit math

**Date:** 2026-05-04
**Status:** Accepted
**Reversibility:** Medium
**Affects:** CONCEPT.md (new tower-vs-unit math section pending), `prototype/data/balance.json` (downstream numbers phase), Follow-up #13, Follow-up #7

---

## Decision

The tower-vs-unit math for *Ash to Altar* is governed by a 17-item conceptual frame, ratified across five PM `AskUserQuestion` rounds on 2026-05-04. Frame extracted from external-LLM brainstorm (variable-naming convention, special-round template, engagement-time integral form) and reframed against the locked 2026-04-25 ratification (3 civs, 4-tier ladder, dual-currency Tribute + Divinity, locked content skeleton). The frame is the source-of-truth for the equation; the numbers-phase ratification (Follow-up #13) consumes this frame to produce specific values.

## Context

Post-graduation cut (2026-05-03) collapsed `effectiveTowerStats` to scalar damage/cd; the flat curve has not been validated. PM picked Follow-up #13 (Recommended) on the next-track gate. External LLM thread provided a variable-naming convention (a)–(k) and per-round template scaffolding. Frame was reviewed for gaps against the locked content skeleton, then ratified over five `AskUserQuestion` rounds. Round 5 spawned a Priority-#1 scope expansion (auxiliary economy structure + game modes ontology) tracked in a separate same-day decision.

## Variable nomenclature (locked)

| Var | Meaning |
|-----|---------|
| (a) | Tribute pool — primary currency, sourced from kills + sell refunds + boss lump-sums. |
| (b) | Friendly tower roster — count + type composition. |
| (c) | Tower base damage — per-tower per-shot, scaled by level via `effectiveTowerStats` multipliers. |
| (d) | Lane runners — count + type composition per wave. |
| (e) | Runner HP pool — per-runner. |
| (f) | Runner speed — per-runner; modifiable by status procs. |
| (g) | Tower-vs-runner type bonus — RPS matrix lookup, **bidirectional ±25%** (1.25× / 0.75×). |
| (h) | Commander-avatar contribution — three slots (passive / short-CD active / long-CD signature) × four effect types (damage / control / summon / economy). |
| (i) | Tower placement — player-skill axis, function-shaping (sets engagement-time integral). |
| (j) | Map — per-map (ε, N) tuple: ε engagement coefficient ∈ [0,1], N buildable hex count. |
| (k) | Difficulty tier — Easy / Hard / Hardcore. Modifies HP-curve exponent only (single-axis compounding). |
| (l) | Tower lifecycle state — (tier, level) tuple. Tier ∈ {T1, T2, T3, T4 Demigod, God}; Level ∈ {1, 2, 3}. Both axes first-class. |
| (m) | Adjacency / placement-coupling — merge requires same-civ same-tier within `CIV_MERGE_RADIUS`. Promote requires single T3 + 250 Tribute + valid demigod mapping. Fusion requires two T4 Demigods of same civ + 1 Divinity (after 2-Divinity menu unlock). |
| (n) | Buildable-slot binding — derived from (j) N; binds once (a) > N × cost-of-cheapest. |
| (o) | Divinity — second currency. Cap 6/match. Drains 2 (Fusion menu unlock) + 1×N (per fusion). Source: interim pattern below. |
| (p) | Runner armor tag — 5 buckets (Unarmored / Shielded / Beast / Spirit / Colossal). RPS matrix routes through this. |
| (q) | Status-proc layer — 7 procs (Armor-shred / Bleed / Stagger / Burn+splash / Toxin / Hex / Smite). Cross-tower feedback explicit. |
| (r) | Lives — 10 fixed across all (k). Per-leak severity tunable. |

## Master damage equation (canonical form)

For each runner R in a wave:

```
Damage_dealt(R) = Σ_T [ DPS(T) × t_engaged(T, R) × matchup(T, R, p) × passive_modifiers(T, h) × status_state(R, q, t) ]
```

Where:
- `DPS(T) = damage(T) / (cd(T) / 60)` — damage per second.
- `t_engaged(T, R) = path_length_in_range(T, j) / speed(R, q)` — engagement time integral over the path within tower T's range.
- `matchup(T, R, p) ∈ {0.75, 1.00, 1.25}` per RPS matrix.
- `status_state` evolves as (q) procs accumulate on R; cross-tower feedback expressed (e.g., Piercing Armor-shred lowers (p) effective armor for downstream towers' damage).

**Win condition:** lives > 0 at end of round 30. Each leaked runner deducts lives per its severity tag.

## Round template (locked slot typology)

Seven slot types: **Standard / Swarm / Elite / Modifier / Telegraph / Boss / Recovery**.

R-assignments (30-round arc):
- R5 — Modifier
- R10 — Boss (drops 1 Divinity + Tribute medium lump)
- R15 — Elite
- R20 — Modifier
- R25 — Telegraph
- R30 — Final Boss (drops 2 Divinity + Tribute huge lump)
- Recovery slots float post-special (e.g., R6, R11). Standard fills the remainder (~22 rounds).

## Difficulty tier (k) compounding rule

**Single-axis only.** (k) modifies the HP-per-wave curve **exponent**. All other R-curves identical across tiers. Easy / Hard / Hardcore diverge geometrically late, not flatly. **Anti-pattern explicitly flagged:** stacking HP + speed + reward + cost penalties simultaneously per tier — compounds geometrically, makes R30 Hardcore mathematically unwinnable independent of skill execution. Exponent values are numbers-phase work.

## Skill-bar operationalization (k winnability target)

Three QA-instrumentable axes:
1. **Matchup-correctness rate** — % of damage dealt with type advantage.
2. **Placement-coverage** — `ε_actual / ε_max` for the map.
3. **Ability-uptime** — % of commander cooldowns spent.

Per-tier thresholds set in numbers-phase Follow-up #13.

## Sell-refund schedule

| Timing | Refund |
|---|---|
| Pre-wave (before "Send Wave" pressed) | **100%** |
| Same wave post-send | **90%** |
| R+1 (next round) | **80%** |
| R+2 | **70%** |
| R+3 onward | **60% flat** |
| T4 / God (any timing) | **60% capped** |

(k)-coupled: Easy = full schedule. Hard = floor at 60% (current invariant). Hardcore = steeper schedule, floor at 50%.

## Tower target-priority

AI default = First (closest to base). Per-tower override via right-click → {First / Last / Strongest / Weakest / Closest}.

## Boss / Elite reward shape

- R10 Boss: medium Tribute lump + 1 Divinity drop.
- R15 Elite: medium Tribute lump + 0 Divinity.
- R30 Final Boss: huge Tribute lump + 2 Divinity drop.
- Standard / Swarm / Modifier / Telegraph / Recovery: per-runner reward curve only.

## Divinity source — interim pattern

Cap 6/match. Sources:
- R10 Boss: +1
- R20 zero-leakage streak ≥ 3: +1
- R30 Final Boss: +2
- Two additional escalation hooks: TBD

Documented as **interim**; full ratification under Follow-up #7 (Foresight-coin) when that thread lands.

## Alternatives considered (per round, summary)

**Round 1.** (k) Easy/Hard/Hardcore — chose locked 3 tiers over Patch-1 defer / dynamic / two-tier. Win condition — chose lives-bounded over per-wave-binary / clear-bonus / objective-overlay. Damage form — chose DPS×integral over discrete / hybrid / deal-on-kill. Divinity — chose first-class over stub / defer / fold-into-Tribute.

**Round 2.** (l) lifecycle — chose both axes current shape over tier-only / level-only / cap-5. (k) compounding — chose exponent-shift over one-shot scalar / two-axis / multi-axis. Commander (h) — chose three-slots×four-effect-types over single-DPS / damage-only / XP-scalar. Status+armor — chose full feedback over RPS-only / scalar-HP / defer.

**Round 3.** Slot typology — chose 7-slot over 5-slot / 4-slot / freeform. R-assignments — chose every-5 symmetric over every-10-with-mini-bosses / decoupled / per-(k). (j) — chose (ε, N) tuple over ε-only / N-only / per-zone. Lives — chose fixed-10 over tier-scaled / regen / severity.

**Round 4.** Refund — folded into Round 5 with synthesis. Boss — chose lump+guaranteed-Divinity over HP-proportional / streaks / player-choice. Divinity-source — chose interim-pattern over full-defer / pure-streak / passive-trickle. Skill — chose 3-axis over composite / 2-axis / 5-axis.

**Round 5.** Refund — chose PM 4-step + pre-wave-gate + T4-cap + (k)-coupled per 3x debug loop synthesis. Targeting — chose AI-default + per-tower-override over AI-only / manual / per-(k)-AI. Tribute carry — *deferred*; PM redirected to auxiliary economy structure (separate decision). Multi-lane — *deferred*; PM redirected to per-mode discussion (separate decision).

## Reason chosen

Six rounds of PM-Recommended-first `AskUserQuestion` gates with explicit Recommended picks. The frame coheres because every option chain optimized for the same constraints: locked-content-skeleton fidelity, two-dev tractability, single-axis (k) compounding to avoid late-match unwinnability, dual-currency design intent preservation, and player-skill expression across (g)/(h)/(i) without flattening to a single composite.

## Reversibility

**Medium.** Most items can be revised in numbers-phase or Patch-1 without invalidating the frame as a whole. Hard-locked from upstream: dual-currency (per 2026-04-25 Hard), 30-round arc (per 2026-04-25 Hard), tier-up via merge/promote/fuse (per 2026-04-25 Hard), accessibility floor §2.4a (per 2026-04-20 Hard).

## Cascade impact

- CONCEPT.md will gain a new **"Tower-vs-Unit math" section** referencing this decision. Insertion gated on PM ratification of placement (likely §3 or §4).
- `prototype/data/balance.json` **untouched this turn**. Numbers-phase Follow-up #13 ratification consumes this frame.
- Engine-port discipline: equation written so DPS-integral form translates 1:1 to Godot 4 process-tick math.
- `concept/phase-5.md §5.4 [LOCKED]` untouched.

## Follow-ups

- **Numbers-phase Follow-up #13** — consumes this frame, produces ratified values for (a)/(c)/(e)/(f) curves + (g) magnitudes + (h) ability magnitudes + (k) exponent values + (j) per-map (ε, N) values + skill-bar threshold numbers per (k).
- **Auxiliary economy structure + game modes ontology** — PM-redirected from Round-5 Tribute-interest question; separate Proposed decision filed 2026-05-04 same-day: [`2026-05-04-auxiliary-economy-and-modes-scope.md`](2026-05-04-auxiliary-economy-and-modes-scope.md).
- **Follow-up #7 (Foresight-coin)** — Divinity source ratification consumes the interim pattern locked here.
- **CONCEPT.md amendment** — once auxiliary structure ratifies, full §-new write-up against this frame + the auxiliary structure.
- **Tower target-priority UX** — right-click context menu extension; downstream prototype task.
