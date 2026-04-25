# Balance-pass #2 Numbers-phase Round 9/10 — Skill-bar thresholds per (k) tier

- **Status:** Accepted
- **Date:** 2026-05-05
- **Reversibility:** Medium (numeric thresholds; reshape requires re-running Round 2 winnability stacks)
- **Phase touched:** Numbers (downstream of (k), (q), (i), (h), (s) magnitudes)

## Context

Round 2 winnability math posited a ~5× expert skill-stack against tier-ladder 54× → ~270× expert effective damage. Rounds 5–8 bound the per-tower magnitudes (1.725× expert ceiling: (s) 1.20 × (h passive) 1.15 × (q matchup) 1.25). Round 9 binds the **input rates** that produce that ceiling — concrete player behaviors that, executed at threshold, yield the magnitudes the math assumes.

Three independent skill axes:

1. **Matchup-correctness** — % of towers built/upgraded with civ-matched element vs incoming wave creep. Drives (q) 1.25× coverage.
2. **Placement-coverage** — % of map's "good" cells used (range overlap + choke leverage). Drives (i) bonus + engaged-time ε from Round 4.
3. **Ability-uptime** — % of available (h) commander active casts fired within engaged windows. Drives Round 6 active-burst math.

## Decision

Per-(k)-tier expert/novice thresholds:

| Axis | Easy expert | Hard expert | Hardcore expert | Novice (any k) |
|---|---|---|---|---|
| Matchup-correctness | 60% | 75% | **90%** | 30% |
| Placement-coverage | 50% | 65% | **80%** | 30% |
| Ability-uptime | 40% | 60% | **80%** | 20% |

### Hardcore expert realized stack

`0.90 × 0.80 × 0.80 = 0.576` effective coverage of the per-tower 1.725× ceiling → **~1.0× realized** against Hardcore R30 HP 565× baseline. Closes Round 5 Hardcore margin exactly when paired with Fusion-on-schedule and tier-ladder 54×.

### Easy expert realized stack

`0.60 × 0.50 × 0.40 = 0.12 × 1.725 = 0.207×` realized coverage uplift → still well above novice-clear floor against Easy R30 HP 85×. Easy expert ≠ Hardcore expert; the gap is intentional difficulty design.

### Novice floor (all k)

`0.30 × 0.30 × 0.20 = 0.018 × 1.725 = 0.031×` realized → clears Easy via tier-ladder alone (54× ÷ 85× = 0.635× margin) without any skill stack. Hard novice fails. Hardcore novice fails by orders of magnitude. **First-clear gates work as designed.**

## Measurement (post-Phase-5 telemetry)

- **Matchup-correctness** = (towers placed/upgraded with civ matching incoming wave's most-vulnerable element ÷ total tower placements/upgrades) over match duration. Ties broken by next-2-wave-lookahead.
- **Placement-coverage** = (cells with ≥1 tower in range OR adjacent to choke ÷ total "good" cells per per-map authoring). Per-map "good" cell set authored at level-design time.
- **Ability-uptime** = (active casts fired in engaged windows ÷ available casts during engaged windows). Engaged window = enemy in (h) avatar's 3-cell active radius. Pre-cast and post-window casts not counted.

## 3x debug loop

**L1 — aggressive critique.**
- 90% Hardcore matchup risks rote "always-civ-A vs always-creep-B" memorization meta if waves are predictable. Counter: Round 11+ random-seeded wave compositions per match.
- 80% placement-coverage risks a single optimal layout per map → solved-game by Patch-3. Counter: random-seeded crystal-locks per map (Round 11) + per-civ tower-shape variance (per-tower authoring sub-pass).
- 80% ability-uptime conflicts with Round 6 "strategic-decision lever" framing of signature ability (which is once-per-match, not uptime-driven). Active-only — signature explicitly excluded from uptime metric. Resolved.
- Combined 0.576 coverage assumes axes are independent; in practice high-skill players correlate across all three. Real expert stack may be 0.65–0.70 → Hardcore margin closes with headroom not tightness. Acceptable; widens Hardcore difficulty band slightly favorable to player.

**L2 — steelman.**
- L1's predictability concern is a Round 11 (per-map authoring) problem, not a threshold problem. Thresholds are correct; wave-composition discipline lives downstream.
- Single-optimal-layout concern same: per-map authoring problem, not threshold.
- Independent-axes assumption is conservative (under-estimates expert stack), which biases Hardcore difficulty toward "winnable" not "impossible" — correct direction.

**L3 — synthesis.**
- Lock thresholds at 90/80/80 Hardcore expert; 75/65/60 Hard expert; 60/50/40 Easy expert; 30/30/20 novice floor (all k).
- Flag Round 11 per-map authoring as the venue for wave-randomization + crystal-lock variance to prevent solved-game meta from threshold-memorization.
- Telemetry definitions captured per "Measurement" section above; engine-side gathering is Phase 5 work.

## Cascade

- §2.4a + §5.4 [LOCKED]: untouched.
- 17-item conceptual frame: untouched. Round 9 binds **input-rate thresholds**, not new variables.
- Variable bindings: (k), (q), (i), (h), (s) all unchanged. Round 9 quantifies the **player-input rates** that activate the expert-stack ceiling Rounds 5–8 produced.
- Downstream impact: per-map authoring (Round 11+) inherits "good cells" definition + wave-randomization mandate.

## Open follow-ups

1. **Round 11 mandate** — random-seeded wave composition + per-map crystal-lock variance to defend threshold integrity from memorization meta.
2. **Phase 5 telemetry hooks** — implement matchup/placement/uptime instrumentation per Measurement section; surface in post-match scorecard for player feedback loop.
3. **UI surfacing** — should mid-match HUD show real-time matchup hint (civ recommendation per incoming wave)? Round 12 / per-civ commander authoring sub-pass; risks reducing matchup-correctness from skill to UI-read.
