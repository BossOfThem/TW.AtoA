# Decision — Balance-pass #2, Round 4: Speed (f) curve + per-map (j) defaults

**Date:** 2026-05-05
**Status:** Accepted
**Reversibility:** Medium
**Affects:** [`decisions/2026-05-04-balance-pass-1-conceptual-frame.md`](2026-05-04-balance-pass-1-conceptual-frame.md) (item (f) speed — values now bound; item (j) per-map (ε, N) — defaults now bound); CONCEPT.md (pending §-new "Tower-vs-Unit math"); `prototype/data/balance.json` (downstream); Follow-up #13.

---

## Decision

### Speed (f) base curve

```
f_base(R) = 50 units/sec        for all R ∈ [1, 30]      (constant — no R-scaling)
f(archetype, R, status) = f_base · arch_mult(archetype) · Π status_mults(q, t)
```

Per-archetype multipliers (locked):

| Archetype | Multiplier | Effective base speed | Notes |
|-----------|------------|----------------------|-------|
| Standard  | ×1.0  | 50 u/s | Baseline. |
| Swarm     | ×1.5  | 75 u/s | Fast/light; supports R10/R20 modifier-round chaos. |
| Elite     | ×1.0  | 50 u/s | Standard speed; threat is HP/armor, not pace. |
| Boss      | ×0.7  | 35 u/s | Slow / sticky / heavy. R10/R15 boss-spike profile. |
| Colossal  | ×0.5  | 25 u/s | R30 final-boss tier; stationary-feeling, telegraphed. |

Speed is **constant across (k)** per the locked single-axis (k) rule (anti-pattern flag from Round 1: speed-scaling-by-tier compounds geometrically against HP-scaling and breaks Hardcore winnability). Status procs (q) overlay multiplicatively per locked frame item q (e.g., Stagger ×0.5, Bleed ×1.0, etc.).

### Per-map (j) defaults

```
ε_default = 0.6              (60% of path length covered by typical placement)
N_default = 24               (24 buildable hexes per lane)
```

| Knob | Default | Range | Notes |
|------|---------|-------|-------|
| ε    | 0.6 | [0.4, 0.95] | 0.4 = below-curve placement; 0.6 typical; 0.85+ = expert; 0.95 = ceiling. ε feeds engagement-time integral `t_engaged = path_length_in_range / speed`. |
| N    | 24  | [16, 36] (per-mode scaled) | 24 maps cleanly to 3 civs × 8 placements (T1-floor + tier-up runway). Per-mode N-scaling: PvE-MP / Horde-B scale N linearly with player count. |

Mode-specific overrides (held for Round 8 ratification, not bound here):
- **Solo Campaign / Horde-A** — N=24 default holds.
- **Horde-B (shared lane, N-scaling map)** — N = 24 × player_count (linear per locked Round 8).
- **PvP-IW** — N=24 per side; ε independent per lane.
- **PvP-Maze** — N is the maze-buildable-cell count (different shape; deferred to Round 8).
- **PvE-MP** — N per lane = 24; total buildable = 24 × N_lanes.

## Context

Round 1 ratified the HP curve `HP_std(R) = 100 · 1.16^R`; Round 2 ratified (k) exponents (Easy 1.16 / Hard 1.19 / Hardcore 1.22); Round 3 ratified Tribute economy. Round 4 sizes the **time** side of the engagement-time integral — speed (f) — and the **space** side — per-map (ε, N). Together they bound `t_engaged(T, R)` in the master equation.

The 17-item conceptual frame locks (j) as a per-map tuple (ε engagement coefficient ∈ [0,1], N buildable hex count) and (f) as a per-runner speed modifiable by status procs, but does NOT bind the magnitudes. Round 4 sets defaults; per-map authoring later can override ε for specific stage geometries (chokepoint / sprawl / serpentine) and N can flex per-mode.

## Alternatives considered

### Speed (f) shape

- **Option A — Flat 50 + archetype modifiers.** (Chosen.) Constant base across R; archetype multipliers carry the threat-shape variation. Maps cleanly to `t_engaged = path_length / speed` integral; players parse "boss is slow, swarm is fast" as a single axiom that doesn't change late-game.
- **Option B — Linear ramp 40→70 (R1→R30).** Speed grows with R; late-game runners blitz through. Compounds against HP curve — late waves get *both* fatter and faster, which is a multi-axis amplifier (cousin of the (k) anti-pattern flagged in Round 1).
- **Option C — Per-archetype curve (Standard flat, Boss slows further late).** Archetype-by-R matrix. Higher authoring cost; harder to balance against tower range (placement-coverage threshold shifts late if Boss slows).
- **Option D — Compound mild (1.01^R) base.** R30 ≈ 67 u/s. Subtle late-game pressure. Same multi-axis-amplifier critique as Option B; also rejected on "the player should feel HP-pressure late, not speed-pressure" design intent.

### Per-map (j) defaults

- **Option E — ε=0.6, N=24.** (Chosen.) Typical placement covers 60% of path; 24 hexes maps cleanly to 3 civs × 8 placement slots; expert play pushes ε to ~0.95 via wraps + chokepoint stacking.
- **Option F — ε=0.5, N=20 (tighter).** Below-curve typical play; harder onboarding; less placement runway for tier-up cadence (8 T1 + 5 T2 merges + 3 T3 merges + 2 T4 promotes + 1 Fusion needs ≥18 cells; 20 is too tight under T4 spread).
- **Option G — ε=0.7, N=30 (looser).** Easy R30 becomes trivial (placement-coverage skill-axis loses bite; expert ceiling drops because there's nothing left to optimize). Also dilutes commander-aura adjacency tactics — too many cells available.
- **Option H — ε=0.6, N=21 (multi-of-3).** Cleanly 3 civs × 7 cells. Loses the +1 Fusion-prep cell + 0 buffer for sub-optimal placement.

## Reason chosen

**3x debug loop synthesis:**

- *Loop 1 (critique).* Flat speed feels "too static" if players expect late-game pace pressure. R-scaling speed compounds with HP and breaks single-axis (k) discipline. Per-archetype curves are authoring-heavy with no clear payoff.
- *Loop 2 (steelman).* Flat base + archetype modifiers IS the design pattern players already parse intuitively in BTD6 / Kingdom Rush — speed is an *archetype identity* signal, not an R-difficulty signal. Bosses are slow because they're heavy; swarm is fast because it's light. R-scaling threat lives entirely in HP curve + boss-spike `m(R)` overlay; speed stays as identity. Locks the master equation cleanly: `t_engaged` varies only by archetype × placement, not by R-curve compounding.
- *Loop 3 (synthesis).* Flat 50 + archetype multipliers (×1.0/1.5/1.0/0.7/0.5) lands the right archetype identity differentiation, preserves single-axis (k) rule, and keeps `t_engaged` integral analytically clean. ε=0.6 / N=24 lands the placement-coverage skill-bar bite (Round 9 thresholds get a clean 0.6 floor / 0.85 expert / 0.95 ceiling) and the 24-cell tier-up runway (3 civs × 8 placements).

PM picked Recommended on both questions; no override notes.

## Reversibility note

**Medium.** `f_base = 50` and the archetype multiplier table are six values in `prototype/data/balance.json`. Per-map (ε, N) defaults are two-knob tuning; per-map override is per-map authoring not a global change. *Shape* changes (speed becomes R-scaling, or (j) gains a third dimension like elevation) would invalidate Round 9 (skill-bar thresholds tied to ε bracket bands) and would need re-ratifying.

## Cascade impact

- **Round 5 (tower stats — range + cd)** consumes `f_base = 50` and ε=0.6 to size tower range so a placed tower at expected coverage holds runners in-range for ~`(ε · path_length) / 50` seconds; sets a floor on per-tier damage so the time-integral × DPS clears expected R-wave HP totals.
- **Round 8 (per-mode tuning)** consumes per-mode N-scaling (Horde-B linear; PvP-Maze maze cell count; PvE-MP per-lane × N_lanes); ε can flex per-map within mode.
- **Round 9 (skill-bar thresholds)** placement-coverage axis bracket bands set against ε defaults: casual 0.5–0.6 / mid 0.6–0.75 / expert 0.85+. Hardcore threshold sits at expert band per locked Hardcore-winnability ground.
- **Status proc (q) tuning** (deferred — likely Round 7 or Round 11) consumes archetype speed multipliers as the base for status overlay math (Stagger ×0.5 on a Boss = 35 × 0.5 = 17.5 u/s; on a Swarm = 37.5 u/s — different absolute slow but same fractional).
- §2.4a + §5.4 [LOCKED] untouched.
- 17-item conceptual frame untouched (items (f) + (j) now have bound defaults; shape unchanged).
- `prototype/data/balance.json` untouched this turn.

## Follow-ups

- **Round 5 — tower stats** consumes f_base + ε defaults for range/cd sizing.
- **Round 8 — per-mode N-scaling** confirms Horde-B linear / PvE-MP per-lane / PvP-Maze maze-cell math.
- **Round 9 — skill-bar threshold ε bands** locked against 0.6 default.
- **Per-map authoring (post-numbers-phase)** — concrete (ε, N) tuples per ratified map.
- **Decision-table row** added to [`CASCADE.md`](../CASCADE.md).
