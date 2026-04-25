# CASCADE — navigation spine for Ash to Altar

The canonical index. Every doc links from here in the order a new reader (human or Claude) should encounter it. If you are a new session: **`README.md` → `CLAUDE.md` → this file → target doc.** Do not hunt.

Non-negotiables + naming conventions + cascade discipline live in [`README.md`](README.md) + [`CLAUDE.md`](CLAUDE.md); this doc is pure navigation.

---

## How the doc tree works

The project uses a waterfall cascade (see [`CONCEPT.md`](CONCEPT.md) Phases 1–7). It shows up in three places:

1. **Conceptual cascade** — Phases 1–7 in `CONCEPT.md`. Discovery → Analysis → Design → Specification → Implementation → Validation → Iteration. Phase N+1 does not silently edit Phase N.
2. **Player-journey cascade** — [`stages/`](stages/) dir. One doc per player-experience stage, 200–600 lines each.
3. **Research cascade** — [`research/`](research/) dir. Deep-dive market evidence feeding stage decisions. Written *before* the stage that depends on it.

Cross-link convention:
- Stage-to-stage: `[stage 03 — match setup](stages/03-match-setup.md#section)`
- Stage-to-research: `[theme-era §2.3](research/02-theme-era.md#23-pirate-signal)`
- Decisions: `[2026-04-20 <slug>](decisions/2026-04-20-<slug>.md)`
- Concept anchors: `[CONCEPT §3.3](CONCEPT.md#33-the-five-lineages-mechanical-identity-within-a-match)`

Every stage / research doc carries a **Status** (Stub | Draft | In review | Locked) and **Last reviewed** date. When in doubt about freshness, trust the date.

---

## Reading order (new session)

1. [`README.md`](README.md) — status, non-negotiables, critical context.
2. [`CLAUDE.md`](CLAUDE.md) — session conventions, cadence, 3x debug loop.
3. [`HANDOFF.md`](HANDOFF.md) — last-session checkpoint.
4. This file — the map.
5. [`PROGRESS.md`](PROGRESS.md) — step tracker; first unchecked box = next step (unless queue paused).
6. [`CONCEPT.md`](CONCEPT.md) — vision hub. Phase content lives under [`concept/phase-1..7.md`](concept/); open only what you need. Stage-level drill-downs in `stages/`.
7. [`CONCEPT-GAPS.md`](CONCEPT-GAPS.md) — ephemeral proposal layer; rows migrate into CONCEPT via ratified decisions.
8. [`admin/concept.json`](admin/concept.json) — PM's structured edits. Diff against `HANDOFF.md` state snapshot.
9. Target stage / research doc per "Current work pointer" below.

---

## Current work pointer

**2026-05-05 — Per-commander effect-type-variant authoring sub-pass: Round 3 of 5 LANDED (R1-R3 LANDED; dual-push checkpoint).** Post-CONCEPT-amendment-arc fork: PM picked per-commander authoring (Recommended) over per-tower / per-map / per-civ / Phase-5-readiness / research / admin tracks. **Round 1** filed scope decision + §-placement table + 5-round queue with 3x debug loop on round-structure axis (Axis A per-commander rounds / Axis B per-ability-slot rounds / Axis C per-effect-type rounds). **Axis B chosen** — per-ability-slot, all 3 commanders per round; strongest equivalent-impact-to-§4.11.6-damage-floor discipline (cross-commander parity-check happens every round on the same slot). Axis A rejected (locks commander 1 before commander 2/3 reveal boundary cases). Axis C rejected (compresses commander↔effect-type assignment fork into R1, where it would burn the round on a meta-decision before authoring starts). Loop-1/2/3 synthesis added per-commander identity readings at the close of R2/R3/R4 to mitigate commander-identity fragmentation across rounds. **Round queue locked:** R2 all 3 passive variants (Spartan Training / Blood Tribute / Sons of Ragnar) authored against +15% damage benchmark; R3 all 3 short-CD active variants (This Is Sparta! / Sun Offering / Berserk) against 2,880-burst benchmark + 30s-CD-band discipline; R4 all 3 signature variants (The Last Stand / The Great Sacrifice / The Great Heathen Army) against instant-tier-up benchmark + once-per-match + signature-excluded-from-uptime preserved (per §4.10.5); R5 cross-commander balance audit (9-spec parity check + match-impact simulation against §4.11.8 Hard expert thresholds) + 3 per-commander one-pagers (Leonidas / Montezuma II / Ragnar Lothbrok) + `phase-4.md §4.1` rewrite (mechanical-content body) + `§4.11.6` deferral-language removal + `§4.8` exit-condition gate item #1 tick. Dual-push checkpoints: after R3 (carries R1-R3), after R5 (carries R4-R5 + closes arc). **Locked ability names from `phase-3.md §3.2` carry forward unchanged** — this arc binds *mechanical content* under those names, never re-names. **§4.11.6 damage-floor magnitudes** are the equivalent-impact calibration target, never overwritten — variants authored alongside, not instead. **Cultural-sensitivity Follow-up #5** continues to gate art / pose / VO direction; this arc is mechanical-content only (effect-type / magnitude / duration / CD / target-class — civ-neutral language). §5.4 + §2.4a [LOCKED] + 2026-04-25 locked content skeleton + 17-item frame + all Numbers-phase magnitudes + all R1-R7 amendment-pass §-anchors untouched. Filed [`decisions/2026-05-05-per-commander-effect-type-variant-authoring-scope.md`](decisions/2026-05-05-per-commander-effect-type-variant-authoring-scope.md) (Medium). **R2 LANDED** — passive variants authored across all 3 commanders against +15% damage benchmark. Effect-type assignment locked: Leonidas=Control (15% slow / 2-cell aura / 50% soft-cap), Montezuma II=Economy (+15% bonus Tribute per Aztec-tower kill in aura, multiplicative w/ §4.6a Economy Bonus aux), Ragnar=Summon (one Son @ 40 DPS / 20s cadence / Slashing / HP=2× HP_std(R)). Cross-commander parity table targets ±10% at Hard expert thresholds; per-tower target-side hook interfaces pre-specified for cross-arc parity. **Aura-anchor sub-decision deferred to R5** §4.1 rewrite (cascade drift: §4.1 says "board-wide invisible" / §4.11.6 says "2-cell aura"; 3 resolution candidates flagged: anointed-tower / Commander-pedestal / board-wide-civ-matched). R2 authored against §4.11.6 (more recent + Specification-phase) with `[anchor TBD R5]` placeholders. Filed [`decisions/2026-05-05-per-commander-r2-passive-variants.md`](decisions/2026-05-05-per-commander-r2-passive-variants.md) (Medium). **R3 LANDED** — short-CD active variants authored across all 3 commanders against 2,880-burst benchmark + 30s base CD discipline. Effect-type lanes locked from R2: Leonidas This Is Sparta! = Control (4s hard-stun + 1-cell knockback in 3-cell radius, ~2,700 marginal damage from extended engagement-time on stationary targets, −6% vs floor), Montezuma II Sun Offering = Economy (4s window + 4-cell radius, +35% bonus Tribute on Aztec-tower kills in zone, ~46 T/cast at R20 baseline, multiplicative w/ §4.6a Economy aux for full-stack ~1.6875× per kill in overlap), Ragnar Berserk = Summon (2 Berserkers @ 360 DPS × 4s lifespan, Slashing + frontal cleave + Bleed status-proc, 1× HP_std(R), exact 2,880 burst parity). Cross-commander parity table flags **Sun Offering amortization** for R5 audit (single-cast flatters Economy ~5,500 vs 2,880 nominal floor; full-match impact ~99K vs damage-floor ~52K — intended Aztec scaling identity but R5 must verify Hard 100% breakpoint not breached). Cross-arc per-tower target-side hooks specified: `aztec_tower.bonus_tribute_yield_in_active_zone` flag + global `summons_alive_max = 3` cap + Berserker Slashing-Bleed status-proc cross-ref to 2026-04-26 attack-type-mapping. Per-commander identity readings closed across (h)+(g): Greek lockdown / Aztec scaling / Norse layered-warrior. Filed [`decisions/2026-05-05-per-commander-r3-short-cd-active-variants.md`](decisions/2026-05-05-per-commander-r3-short-cd-active-variants.md) (Medium). **Dual-push checkpoint** after R3 carries R1+R2+R3 per scope decision cadence. **R4 next** — signature variants (The Last Stand / The Great Sacrifice / The Great Heathen Army) against instant-tier-up benchmark (once-per-match free T1→T2 or T2→T3 per §4.11.6); per-commander identity readings from R2+R3 set the signature direction (Greek peak-lockdown / Aztec peak-scaling / Norse mass-summon). PM autonomy mandate carries forward — R4-R5 produce autonomously. cascade-lint clean.

*Prior pointer (2026-05-05 CONCEPT.md amendment pass ARC CLOSED Rounds 1-7) archived to [`CASCADE-history.md`](CASCADE-history.md).*

**Next planned work (post-per-commander-arc; deferred until R5 closes):**
1. **Per-tower authoring sub-pass** — bind cd / range / attack-type / status-proc across 18 T1-T3 + 18 T4 Demigod + 9 God towers across 3 civs. Consumes §4.10 frame + §4.11 magnitudes + §4.6a aux catalog. Likely 5-10 rounds. **Cross-arc dependency:** per-commander affinity hooks (this arc's interface side) bind tower-side targets here.
2. **Per-civ specialization** — Greek / Aztec / Norse identity profiles (matchup affinities, identity hooks, signature creep types). Intersects Follow-up #5 cultural-sensitivity gate. **Cross-arc dependency:** per-commander civ-affinity hook semantics from this arc bind here.
3. **Per-map authoring (incl. Round 11 mandate)** — good-cell authoring + wave-randomization seeds + crystal-lock variance. Defends §4.11.8 thresholds from memorization meta. Cross-cuts all 6 modes.
4. **Phase 5 readiness gate** — engine-side telemetry implementation per §6.5 protocol; wave-composition variance per §4.7 R11.
5. **`research/06-tw-subgenres.md`** new stub — Squadron TD / Legion TD 2 / BTD6 / Element TD / Line Tower Wars / Mini-TD deep dives.
6. **`admin/concept.json` migration direction** — long-deferred. PM picks: full rewrite to 3-civ/4-tier/Fusion shape, regenerate from CONCEPT.md, or retire entirely.
7. **Follow-up #5 cultural-sensitivity pass scheduling.** Hard pose-lock + content-lock gate before any culturally-coded civ art ships. **Cross-arc dependency:** per-commander mechanical specs from this arc cleanly separable from VO/pose direction; cultural-sensitivity pass owns the latter.
8. **Follow-up #6** — Patch-1 commanders per civ + Thor Slashing+Crushing recipe-layer dissonance.
9. **C7.b deferred items** — Builder concurrency cap + 90% refund-on-cancel UI.
10. Other follow-ups #7 / #8 / #9 (Foresight-coin / PvE campaign + AGES + leveling + attributes / non-boss enemy ontology).

Workflow upgrade Steps 0, 1, 1.5a remain complete. `PROGRESS.md` is the live step tracker.

---

## Stages — player-journey cascade

Strict downstream order. Do not open Stage N content work until Stage N-1 is at least "In review."

| # | Stage | Status | What it covers |
|---|-------|--------|----------------|
| 00 | [Session start](stages/00-session-start.md) | Draft | App launch, splash, main menu, first-time vs returning, accessibility floor. |
| 01 | [Commander pick](stages/01-commander-pick.md) | Draft | Roster size, archetype slots, first-pick UX, change-commander policy. **Identity moment.** |
| 02 | [Mode select](stages/02-mode-select.md) | Stub | Launch modes, matchmaking, lobby UX. |
| 03 | [Match setup](stages/03-match-setup.md) | Stub | Map pick, lane assignment, starting economy, pre-wave build, commander banner. |
| 04 | [In-match core](stages/04-in-match-core.md) | Stub | Waves, tower combat, economy, send/defend, Mythium. |
| 05 | [Age evolution](stages/05-age-evolution.md) | Stub | Age Gate UX, auto-evolution, divergence forks, age-persistence callback. |
| 06 | [Hybrids & fusion](stages/06-hybrids-fusion.md) | Stub | Adjacency rules, hybrid discovery, cross-lineage rares. |
| 07 | [Match end](stages/07-match-end.md) | Stub | Victory/defeat, stats, XP, drops, next-match nudge. |
| 08 | [Meta progression](stages/08-meta-progression.md) | Stub | Commander XP, backpack, battle pass, store. |

---

## Research — deep-dive market evidence

Methodology per [`00-methodology.md`](research/00-methodology.md). Sources prefer 2024–2026 freshness. Every section ends with a "so what for this game" synthesis.

| # | Research doc | Status | Feeds into |
|---|--------------|--------|------------|
| 00 | [Methodology](research/00-methodology.md) | Draft | All research |
| 01 | [Genre pulse](research/01-genre-pulse.md) | Stub | Stage 02 (mode select) |
| 02 | [Theme & era](research/02-theme-era.md) | Stub | Stages 03, 05 — era-spine decision |
| 03 | [Commander archetypes](research/03-commander-archetypes.md) | Draft | Stage 01 |
| 04 | [Monetization & live-ops](research/04-monetization-liveops.md) | Stub | Stages 07, 08 |
| 05 | [Demographics & platform](research/05-demographics-platform.md) | Stub | Stages 00, 02 |

---

## Decisions — dated log

Every concept-constraint change + every ratified gap-resolution lives here. Format: [`TEMPLATE.md`](decisions/TEMPLATE.md).

| Date | Decision | Reversibility |
|------|----------|---------------|
| 2026-05-05 | [Per-commander effect-type-variant authoring R3 (short-CD active variants): Leonidas This Is Sparta! = Control (4s hard-stun + 1-cell knockback in 3-cell radius, ~2,700 marginal damage) / Montezuma II Sun Offering = Economy (4s window + 4-cell radius, +35% bonus Tribute on Aztec-tower kills in zone, multiplicative w/ §4.6a Economy aux) / Ragnar Berserk = Summon (2 Berserkers @ 360 DPS × 4s, Slashing + frontal cleave, 1× HP_std(R), 30s base CD all 3). Effect-type lanes locked from R2; cross-commander parity table flags Sun Offering amortization for R5 audit; per-tower target-side hooks specified.](decisions/2026-05-05-per-commander-r3-short-cd-active-variants.md) | Medium |
| 2026-05-05 | [Per-commander effect-type-variant authoring R2 (passive variants): Leonidas Spartan Training = Control (15% slow on enemies in 2-cell aura, 50% soft-cap) / Montezuma II Blood Tribute = Economy (+15% bonus Tribute per kill in aura by Aztec towers, multiplicative w/ §4.6a Economy Bonus aux) / Ragnar Sons of Ragnar = Summon (one Son @ 40 DPS, 20s spawn cadence, max 1 alive, Slashing, HP=2× HP_std(R)). Cross-commander parity table + per-tower/per-civ hook interfaces specified. Aura-anchor sub-decision deferred to R5 §4.1 rewrite (3 candidates flagged).](decisions/2026-05-05-per-commander-r2-passive-variants.md) | Medium |
| 2026-05-05 | [Per-commander effect-type-variant authoring sub-pass scope: 5-round queue + per-ability-slot axis (Round 1 of 5) — R2 passive variants / R3 short-CD active variants / R4 signature variants / R5 audit + per-commander one-pagers + §4.1 mechanical-content + §4.11.6 deferral removal + §4.8 exit tick; 3x debug loop on axis (Axis B per-slot chosen, Axis A per-commander and Axis C per-effect-type rejected)](decisions/2026-05-05-per-commander-effect-type-variant-authoring-scope.md) | Medium |
| 2026-05-05 | [CONCEPT amendment pass Round 7 (CLOSES ARC 7/7): hub CONCEPT.md phase-index rows 3/4/6/7 touched + Non-negotiables "Go big at launch" bullet promoted + version footer 0.8→0.9 with full arc summary](decisions/2026-05-05-concept-amendment-pass-round-7-hub-close.md) | Easy |
| 2026-05-05 | [CONCEPT amendment pass Round 6: phase-4 §4.7 wave-composition variance mandate (R11) + phase-6 §6.5 skill-bar telemetry NEW + phase-7 §7.4 "Go big at launch" non-negotiable bullet; §4.6a audit + mode-availability compressed to free lines](decisions/2026-05-05-concept-amendment-pass-round-6-phase-4-7-r11-and-phase-6-7.md) | Easy |
| 2026-05-05 | [CONCEPT amendment pass Round 5: phase-4 §4.6 Economy rewrite (Tribute kill-only / Divinity 6-source roster / Mythium retirement) + §4.6a Auxiliary economy NEW (7-slot universal catalog + currency-budget audit + mode availability)](decisions/2026-05-05-concept-amendment-pass-round-5-phase-4-economy.md) | Medium |
| 2026-05-05 | [CONCEPT amendment pass Round 4: phase-4 §4.11 Numbers floor body populated — 8 sub-sections binding HP curve / (k) exponents / Tribute yield / speed + per-map / DPS ladder + tier-up costs / commander magnitudes / per-mode tuning + N-scaling / skill-bar thresholds. Replaces Round 3 placeholder.](decisions/2026-05-05-concept-amendment-pass-round-4-phase-4-numbers-floor.md) | Medium |
| 2026-05-05 | [CONCEPT amendment pass Round 3: phase-4 §4.10 Tower-vs-Unit math NEW (variable nomenclature (a)-(r) + extension (s) + master DPS×integral equation + 7-slot round typology + (k) single-axis rule + skill-bar axes + sell-refund schedule + target-priority + boss/Divinity reward shape + engine-port discipline) + §4.11 Numbers floor placeholder for Round 4](decisions/2026-05-05-concept-amendment-pass-round-3-phase-4-tower-vs-unit-math.md) | Medium |
| 2026-05-05 | [CONCEPT amendment pass Round 2: phase-3 §3.6 mode roster 5→6 (Solo Campaign / Horde-A / Horde-B / PvE-MP / PvP-IW / PvP-Maze) + per-mode summary table + §3.4 Commander-Hero residue redaction + §3.8 mode-count update](decisions/2026-05-05-concept-amendment-pass-round-2-phase-3-modes.md) | Easy |
| 2026-05-05 | [CONCEPT.md amendment pass scope: 7-round queue + §-placement table (Round 1 of 7) — phase-3 §3.6 mode-roster + phase-4 §4.10 Tower-vs-Unit math NEW + §4.11 Numbers floor NEW + §4.6/§4.6a economy rewrite + §4.7 Round-11 hook + phase-6 skill-bar telemetry + phase-7 §7.4 "Go big" doctrine + hub version bump; 3x debug loop on §-placement (Option C topical chosen)](decisions/2026-05-05-concept-amendment-pass-scope.md) | Easy |
| 2026-05-05 | [Balance-pass #2, Round 10: Divinity source escalation hooks (CLOSES arc) — 4-Div floor (R10/R15/R30 boss + match-completion); Source 5 Perfect-Wave +1 Div per zero-leak boss-clear (max +3); Source 6 First-Hybrid +1 Div one-shot per topology-true hybrid; ceiling 8 theoretical / 5-6 realistic expert fits 6-cap](decisions/2026-05-05-balance-pass-2-round-10-divinity-sources.md) | Medium |
| 2026-05-05 | [Balance-pass #2, Round 9: Skill-bar thresholds per (k) — Matchup-correctness Hardcore 90% / Hard 75% / Easy 60% / novice 30%; Placement-coverage 80% / 65% / 50% / 30%; Ability-uptime 80% / 60% / 40% / 20%; Hardcore expert realized 0.576 × 1.725× = ~1.0× closes margin exactly](decisions/2026-05-05-balance-pass-2-round-9-skill-bar-thresholds.md) | Medium |
| 2026-05-05 | [Balance-pass #2, Round 8: Per-mode tuning — Send-Creeps mode-variants (Solo Off-Wave + PvE-MP Lane-Trade 3 creeps +50% bonus / Horde Reinforce-Lane 1 helper 4×R-HP / PvP-Maze Send-Through +5 T/round on success / PvP-IW Send-for-Interest 1 Div unlock + 150 T/send + +3 T/round) + per-mode N-scaling (Horde-B 24×player_count linear / PvP-Maze N_maze=30) + PvP tie-break (R31+ HP×1.5^(R-30) + R45 co-victory)](decisions/2026-05-05-balance-pass-2-round-8-per-mode-tuning.md) | Medium |
| 2026-05-05 | [Balance-pass #2, Round 7: Aux-slot costs + (s) ranges — Damage Bonus 1 Div = (s)=1.20 global / Economy Bonus 1 Div = +25% per-kill / Tower-count expansion 1 Div = +2 N / Send-Creeps 100 T baseline / Call-for-Help 300 T / Maze Stone 25 T](decisions/2026-05-05-balance-pass-2-round-7-aux-costs-and-s-ranges.md) | Medium |
| 2026-05-05 | [Balance-pass #2, Round 6: Commander (h) ability magnitudes (damage-variant floor) — passive +15% / 2-cell civ-gated aura; active 4× T3 DPS / 3-cell / 4s / 30s CD (2,880 burst); signature once-per-match free tier-up T1→T2 or T2→T3](decisions/2026-05-05-balance-pass-2-round-6-commander-magnitudes.md) | Medium |
| 2026-05-05 | [Balance-pass #2, Round 5: Tower (c) DPS ladder T1=1×/T2=3×/T3=9×/T4=27×/God=54× (geometric ×3×3×3×2; T1_base=20 dmg/sec Standard) + tier-up costs 100/300/900/2500 (Fusion=0 Tribute, Divinity-priced)](decisions/2026-05-05-balance-pass-2-round-5-tower-baselines.md) | Medium |
| 2026-05-05 | [Balance-pass #2, Round 4: Speed (f) + per-map (j) — `f_base = 50 u/s` constant across R + archetype multipliers (Standard ×1.0 / Swarm ×1.5 / Elite ×1.0 / Boss ×0.7 / Colossal ×0.5); ε=0.6, N=24 defaults](decisions/2026-05-05-balance-pass-2-round-4-map-speed.md) | Medium |
| 2026-05-05 | [Balance-pass #2, Round 3: Tribute economy (a) — `yield(R) = 5 · 1.10^R` per std kill (constant across (k)) + boss lumps R10=250 / R15=400 / R30=1,500 (Easy cumulative ≈25K)](decisions/2026-05-05-balance-pass-2-round-3-tribute-economy.md) | Medium |
| 2026-05-05 | [Balance-pass #2, Round 2: (k) compounding exponents — Easy 1.16 / Hard 1.19 / Hardcore 1.22 (symmetric +0.03 step; R30 std HP ratios 1× / 2.76× / 7.63×)](decisions/2026-05-05-balance-pass-2-round-2-k-exponents.md) | Medium |
| 2026-05-05 | [Balance-pass #2, Round 1: Runner HP curve (e) — `HP_std(R) = 100 · 1.16^R` Easy baseline + boss spikes R10 ×3 / R15 ×2 / R30 ×5](decisions/2026-05-05-balance-pass-2-round-1-hp-curve.md) | Medium |
| 2026-05-04 | [Round 12: Aux UX + frame variable (s) + per-mode (k) + maze validity — in-match side-panel; (s) first-class multiplicative; (k) PvE-only; pre-placement gray-out](decisions/2026-05-04-round-12-aux-ux-frame-extension.md) | Medium |
| 2026-05-04 | [Round 11: PvP Maze Lane deep-dive — hex-grid preserved, A* pathfinding, cheap stones upgradable to T1, Send-Through-Maze, lives=10](decisions/2026-05-04-round-11-pvp-maze-deep-dive.md) | Medium |
| 2026-05-04 | [Round 10: PvE Multiplayer deep-dive — N parallel lanes, last-alive, view-only spectate, Lane-Trade + Call-for-Help slots](decisions/2026-05-04-round-10-pve-mp-deep-dive.md) | Medium |
| 2026-05-04 | [Round 9: PvP Interest Wars deep-dive + frame-#12 lives extension — 20s rounds, 30-leak knockout, tie-escalation + co-victory, Send-for-Interest, lives per-mode declarable](decisions/2026-05-04-round-9-pvp-interest-wars-deep-dive.md) | Medium |
| 2026-05-04 | [Round 8: Horde Co-op deep-dive + co-op mode split — Horde-A (per-player adjacent lanes + leak-bleed) + Horde-B (shared lane, N-scaling map); per-player wallet; linear N-multiplier](decisions/2026-05-04-round-8-horde-coop-deep-dive.md) | Medium |
| 2026-05-04 | [Round 7: Solo Campaign deep-dive — multi-mission saga, single-lane map-shaped paths, per-mission (k), Universal slots only](decisions/2026-05-04-round-7-solo-campaign-deep-dive.md) | Medium |
| 2026-05-04 | [Round 6: Auxiliary economy ratifications + "Go big, no scope cuts" project doctrine — modular slot system, Tribute/Divinity split, all-5-modes-at-launch (became 6 after Round 8), Send-Creeps broad adoption](decisions/2026-05-04-round-6-aux-economy-ratifications.md) | Medium |
| 2026-05-04 | [Auxiliary economy structure + game modes ontology (Accepted; advanced from Proposed via Rounds 6–12) — Squadron-TD-inspired modular auxiliary structure + 6-mode roster + all 10 axes ratified](decisions/2026-05-04-auxiliary-economy-and-modes-scope.md) | Medium |
| 2026-05-04 | [Balance-pass #1 conceptual frame: 17-item ratification of tower-vs-unit math (variable nomenclature (a)–(r) + DPS×integral master equation + 7-slot round typology + (k) single-axis compounding + sell-refund + targeting + boss/Divinity sources + skill-bar axes)](decisions/2026-05-04-balance-pass-1-conceptual-frame.md) | Medium |
| 2026-05-04 | [Aztec glyph: abstract placeholder pending cultural-sensitivity pass (closes Follow-up #4 from 2026-04-25 ratification)](decisions/2026-05-04-aztec-glyph-abstract-placeholder.md) | Easy |
| 2026-04-28 | [§5.4 [LOCKED] amendment: delete Lineages row, add Civilizations row (closes Follow-up #10; original convention archived to CASCADE-history.md)](decisions/2026-04-28-phase-5-naming-conventions-lineages-row-deletion.md) | Easy |
| 2026-04-27 | [Commander-as-summoned-ability-avatar (+ Builder unit class + historic match-arc beats, solo-only); supersedes 2026-04-20 on-field-hero; same-day amendment captures 8-Q PM refinement (Aztec pre-contact; round-30 antagonists; mixed historicity; myth-mode counterfactual)](decisions/2026-04-27-commander-as-summoned-ability-avatar.md) | Medium |
| 2026-04-26 | [Prototype reshape plan (Step C, 6 steps + 2026-04-27 amendment adds C4 Cast-bar extension + new C7 step; **Accepted 2026-04-29**)](decisions/2026-04-26-prototype-reshape-plan.md) | Medium |
| 2026-04-26 | [Phase 1 exit one-pager (formal capture: World + Commander role + Hybrid topology + Why this frame wins + What remains open; closes 2026-04-25 Follow-up #11)](decisions/2026-04-26-phase-1-exit-one-pager.md) | Easy |
| 2026-04-26 | [Attack-type mapping: 7-type taxonomy + per-tower/demigod/god map + RPS armor matrix + status-proc table](decisions/2026-04-26-attack-type-mapping.md) | Medium |
| 2026-04-25 | [Q2 ratified: real-world cultures direction (Greek / Aztec / Norse) + launch-match design skeleton](decisions/2026-04-25-q2-real-cultures-direction-ratified.md) — supersedes Q2 draft; partially supersedes 2026-04-24 reopen (thematic direction only; structural guardrails intact) | **Hard** |
| 2026-04-25 | [Q2 world pitch draft (synthetic mythic-history braid)](decisions/2026-04-25-q2-world-pitch-draft.md) — **Superseded by 2026-04-25 real-cultures ratification** | n/a (Proposed→Superseded) |
| 2026-04-24 | [Phase 1 vision reopen: synthetic mythic-history braid](decisions/2026-04-24-phase-1-vision-reopen-synthetic-mythic-history.md) — supersedes 2026-04-21 + 2026-04-22 Step B; **thematic direction partially superseded by 2026-04-25 real-cultures ratification** (structural guardrails intact) | **Hard** |
| 2026-04-21 | [Concept tightening: 3/3/3 shape + dungeon cosmology + Ash-enabler hybrids](decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md) — **Superseded by 2026-04-24** | **Hard** |
| 2026-04-19 | [Cascade restructure: consolidate to root, create stages/research/decisions dirs](decisions/2026-04-19-cascade-restructure.md) | Medium |
| 2026-04-19 | [Admin UI v1: single-file node-graph concept map](decisions/2026-04-19-admin-ui-v1.md) | Easy |
| 2026-04-19 | [Design prototype scope: throwaway HTML/JS permitted](decisions/2026-04-19-design-prototype-scope.md) | Easy |
| 2026-04-19 | [Tutorial glow affordance too subtle — log as design-debt](decisions/2026-04-19-tutorial-cell-affordance.md) | Easy |
| 2026-04-19 | [Intro-game baseline gaps escalated to concept-gaps pass](decisions/2026-04-19-intro-baseline-gaps.md) | Easy |
| 2026-04-19 | [Concept thinness load-bearing — pause workflow queue for concept-gaps pass](decisions/2026-04-19-concept-thinness-escalation.md) | Easy |
| 2026-04-20 | [Meta-UI envelope: settings menu + pause/meta-controls bundle (SETTINGS-01 + PAUSE-01)](decisions/2026-04-20-meta-ui-envelope.md) | Easy |
| 2026-04-20 | [Audio architecture: 5-bus mixer + ducking + focus-loss (AUDIO-01)](decisions/2026-04-20-audio-architecture.md) | Easy |
| 2026-04-20 | [Accessibility floor as Phase 2 constraint (A11Y-01..04 + SETTINGS-02)](decisions/2026-04-20-accessibility-floor.md) | Hard |
| 2026-04-20 | [Commander identity floor: Phase 4 §4.1 minimum spec (CMDR-01 + CMDR-02 + AUDIO-03)](decisions/2026-04-20-commander-identity-floor.md) | Medium |
| 2026-04-20 | [First-run flow: click budget + returning-player branch + skippable tutorial (FLOW-01 + FLOW-02 + ONBOARD-01)](decisions/2026-04-20-first-run-flow.md) | Easy |
| 2026-04-20 | [Save model: mode-aware save + always-persistent commander profile (SAVE-01 + SAVE-02)](decisions/2026-04-20-save-model.md) | Medium |
| 2026-04-20 | [Prototype `hybrid.pair` is ancestry tag only (PROGRESS 1.5c cleanup)](decisions/2026-04-20-prototype-hybrid-pair-shape.md) | Easy |
| 2026-04-20 | [Prototype pivots from throwaway to playable concept-demo (Step 10 unblocks Step 5 playtest)](decisions/2026-04-20-prototype-concept-demo-pivot.md) | Medium |
| 2026-04-20 | [Prototype debug-check sweep (pre-playtest) — 6 findings resolved](decisions/2026-04-20-prototype-debug-check-sweep.md) | Easy |
| 2026-04-20 | [Prototype interaction layer — hover / right-click / sell / upgrade [PROPOSAL] / reference panel](decisions/2026-04-20-prototype-interaction-layer.md) | Medium |
| 2026-04-20 | [Prototype visuals overhaul + insight layer (silhouettes / hex+glyph / projectiles / damage numbers / status icons / threat bar / next-wave telegraph / combat feed)](decisions/2026-04-20-visuals-insight-pass.md) | Medium |
| 2026-04-20 | [Doc-cascade split: CONCEPT.md → hub + concept/phase-1..7.md (+ cascade-lint size cap and concept/ integrity checks)](decisions/2026-04-20-doc-cascade-split.md) | Easy |
| 2026-04-20 | [Meta-UI shell polish (splash glyphs / login branch / menu branch / mode-aware pause)](decisions/2026-04-20-meta-ui-shell-polish.md) | Easy |
| 2026-04-20 | [Profile panel layer — dedicated Profile scene + mode-gated writeMatchSave](decisions/2026-04-20-profile-panel-layer.md) | Easy |
| 2026-04-20 | [Options 5 tabs real — audio sliders + rebind + video/a11y/gameplay persisted](decisions/2026-04-20-options-five-tabs-real.md) | Easy |
| 2026-04-20 | [Commander-pick identity upgrade — SVG silhouettes + XP ladder + cosmetic locks + silhouette-test](decisions/2026-04-20-commander-pick-identity-upgrade.md) | Easy |
| 2026-04-20 | [First-run discoverability prompts (right-click / I-key / hover) with permanent dismiss](decisions/2026-04-20-first-run-discoverability.md) | Easy |
| 2026-04-20 | [Age-as-history flavor banner + mapmods.json data + Campaign age-gate autosave + auto-age-up toggle](decisions/2026-04-20-age-history-flavor-mapmods.md) | Medium |
| 2026-04-20 | [Spontaneity random events (events.json, 25% seeded LCG, weighted pool, additive co-op broadcast)](decisions/2026-04-20-spontaneity-random-events.md) | Easy |
| 2026-04-20 | [Commander-on-field hero — avatar + 2-cell aura + Shift-click move + Q signature + additive snapshot](decisions/2026-04-20-commander-on-field-hero.md) — **Superseded by 2026-04-27** | Medium |
| 2026-04-22 | [Step B: Prototype reshape plan — 3/3/3 cascade into prototype data + scenes + lint + docs](decisions/2026-04-22-step-b-prototype-reshape-plan.md) — **Superseded by 2026-04-24** (target shape reopened; 18 sub-steps void) | Medium |

---

## Admin UI — visual concept map

- [`admin/index.html`](admin/index.html) — single-file node-graph editor. Drag/drop, edit in sidebar, per-node comments.
- [`admin/concept.json`](admin/concept.json) — canonical editable state. Seeded from `CONCEPT.md`. Read to pick up PM visual edits.
- [`admin/README.md`](admin/README.md) — usage.
- [Decision entry](decisions/2026-04-19-admin-ui-v1.md).

**Conflict rule:** MD docs win on naming conventions; JSON wins on roster/ages/hybrids/positions/comments.

---

## Prototype — clickable design slice

- [`prototype/index.html`](prototype/index.html) — single-file prototype, data-driven over HTTP.
- [`prototype/data/*.json`](prototype/data/) — BALANCE, towers, commanders as JSON. Seed for future Godot Resources.
- [`prototype/start.bat`](prototype/start.bat) — Python `http.server` on :8765 + auto-open (data-driven mode).
- [`prototype/README.md`](prototype/README.md) — run instructions.
- [`prototype/PORT-NOTES.md`](prototype/PORT-NOTES.md) — JS→Godot idiom notes.
- [Decision entry](decisions/2026-04-19-design-prototype-scope.md).

---

## Legacy / archive

- `tw-commanders-starter/` — original starter scaffold; content was duplicated into root 2026-04-19. **Do not edit.** See `tw-commanders-starter/ARCHIVED.md`.

---

## When to update this doc

- Stage / research status changes (Stub → Draft → In review → Locked).
- New stage / research / decision file added.
- Current work pointer shifts.
- Doc renamed, moved, archived.

Treat `CASCADE.md` as single source of truth for "what exists and where." If it disagrees with the filesystem, fix one or the other — never let them drift.

---

*Document version: 0.58 — 2026-05-05: per-commander effect-type-variant authoring R3 (short-CD active variants) LANDED + dual-push checkpoint per scope decision (carries R1+R2+R3). Three commanders × short-CD active (g)-slot mechanical specs filed against §4.11.6 2,880-burst benchmark with effect-type lanes locked from R2: Leonidas This Is Sparta! = Control (4s hard-stun + 1-cell knockback in 3-cell radius — ~2,700 marginal damage from extended engagement-time on stationary targets, −6% vs floor, in ±10% band), Montezuma II Sun Offering = Economy (4s window + 4-cell radius, +35% bonus Tribute on Aztec-tower kills in zone, ~46 T/cast at R20 baseline, multiplicative w/ §4.6a Economy aux for full-stack 1.6875× per kill in overlap), Ragnar Berserk = Summon (2 Berserkers @ 360 DPS × 4s lifespan, Slashing + frontal cleave + Bleed status-proc, 1× HP_std(R), 30s base CD, exact 2,880 burst parity). 30s base CD locked across all 3 (CD-flex band 24-36s deferred to R5). Cross-commander parity table flags **Sun Offering amortization asymmetry** for R5 audit (single-cast flatters Economy ~5,500 vs nominal floor; full-match impact ~99K vs damage-floor ~52K — intended Aztec scaling identity but R5 must verify Hard 100% breakpoint not breached; pre-bracketed tune-down to +25% bonus or 3-cell radius if needed). Cross-arc per-tower target-side hooks specified: `aztec_tower.bonus_tribute_yield_in_active_zone` flag (Sun Offering consumer); global `summons_alive_max = 3` cap (1 Son + 2 Berserkers per Ragnar interaction); Berserker Slashing-Bleed status-proc cross-references 2026-04-26 attack-type-mapping decision. Per-commander identity readings closed across (h)+(g) slots: Greek lockdown (slow + stun stacks for full-Greek-stack overlap zone), Aztec scaling (compounding Tribute via passive + active multiplicative stack), Norse layered called-warriors (1 sustained Son + 2 burst Berserkers via §4.1 summoned-presence model). Aura-anchor sub-decision still deferred to R5 (active-cast targets player-aimed cell, not aura — distinction must be confirmed clean in R5 §4.1 rewrite). Reversibility Medium with three parity-band guards. Filed [`decisions/2026-05-05-per-commander-r3-short-cd-active-variants.md`](decisions/2026-05-05-per-commander-r3-short-cd-active-variants.md). Decisions table row added at top. CASCADE pointer updated R1+R2 → R1+R2+R3 LANDED. R4 next (signature variants vs instant-tier-up benchmark + per-commander identity peaks). Dual-push checkpoint awaiting Bash. cascade-lint clean. No spine-doc edits this round (R3 is decision-file authoring only). Prior: 0.57 — 2026-05-05: per-commander effect-type-variant authoring R2 (passive variants) LANDED. Three commanders × passive (h)-slot mechanical specs filed against §4.11.6 +15% damage benchmark with effect-type assignment locked: Leonidas Spartan Training = Control (15% slow on enemies in 2-cell aura, 50% soft-cap), Montezuma II Blood Tribute = Economy (+15% bonus Tribute per kill in aura by Aztec towers, multiplicative w/ §4.6a Economy Bonus aux), Ragnar Sons of Ragnar = Summon (one Son @ 40 DPS, 20s spawn cadence, max 1 alive, Slashing, HP=2× HP_std(R)). Cross-commander parity table (±10% target at Hard expert thresholds) + per-tower target-side hook interfaces specified for cross-arc parity + per-commander identity readings closing the round. **Aura-anchor sub-decision deferred to R5** §4.1 mechanical-content rewrite — cascade drift caught (§4.1 says "board-wide invisible" / §4.11.6 says "2-cell aura"); R2-R4 author against §4.11.6 (more recent + Specification-phase) with `[anchor TBD R5]` placeholders; 3 resolution candidates flagged (anointed-tower / Commander-pedestal / board-wide-civ-matched). Reversibility Medium with hard-class guards. Filed [`decisions/2026-05-05-per-commander-r2-passive-variants.md`](decisions/2026-05-05-per-commander-r2-passive-variants.md). Decisions table row added at top. CASCADE pointer updated R1→R1+R2 LANDED. R3 next (short-CD active variants vs 2,880-burst benchmark + 30s-CD-band discipline). Dual-push checkpoint after R3 per scope decision cadence. cascade-lint clean. No spine-doc edits this round (R2 is decision-file authoring only). [Older version history (0.56 / 0.55 / 0.54 / 0.53 / 0.52 / 0.51 / 0.50 / 0.47 / etc.) archived to [`CASCADE-history.md`](CASCADE-history.md).]*
