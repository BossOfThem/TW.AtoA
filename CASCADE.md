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

**2026-05-05 — Numbers-phase Follow-up #13 ARC CLOSED: Rounds 1–10 of 10 LANDED.** PM picked Numbers-phase #13 (Recommended) on the next-track gate. **Round 1** ratified runner-HP curve: standard `HP_std(R) = 100 · 1.16^R` Easy baseline (R30≈8,585 ≈85× R1) + asymmetric boss-spike overlay R10 ×3 / R15 ×2 / R30 ×5 (final boss ≈42,925 HP). **Round 2** ratified (k) compounding exponents: Easy 1.16 / Hard 1.19 / Hardcore 1.22 (symmetric +0.03 step; R30 std HP 8,585 / 23,737 / 65,498; ratios 1× / 2.76× / 7.63×). Single-axis (k) preserved per locked frame — boss-spike `m(R)` constant across (k); speed (f) / cost / reward / targeting / refund-floor unchanged by tier (refund (k)-coupling already locked from Round 1 frame). **Round 3** ratified Tribute economy: per-runner yield `yield(R) = 5 · 1.10^R` (compound lagging HP curve; R30=87/kill; constant across (k) per single-axis rule) + boss-round Tribute lumps R10=250 / R15=400 / R30=1,500 (Easy cumulative R1→R30 ≈ 25,000 Tribute; Hardcore yields same per-kill but tighter income relative to HP wall — aspirational design). No interest carry-over (in aux economy Round 7). No R-clear bonus. Sell-refund schedule unchanged (locked Round 1). **Round 4** ratified speed (f) curve + per-map (j) defaults: `f_base = 50 u/s` constant across R (no R-scaling — keeps single-axis (k) discipline; pace pressure lives in HP curve only) with archetype multipliers Standard ×1.0 / Swarm ×1.5 / Elite ×1.0 / Boss ×0.7 / Colossal ×0.5; per-map defaults ε=0.6 (typical placement coverage; expert pushes to ~0.95) and N=24 buildable hexes (3 civs × 8 placements; per-mode N-scaling for Horde-B linear / PvE-MP per-lane / PvP-Maze maze-cell deferred to Round 8). Status procs (q) overlay multiplicatively on archetype speed per locked frame item q. Filed [`decisions/2026-05-05-balance-pass-2-round-1-hp-curve.md`](decisions/2026-05-05-balance-pass-2-round-1-hp-curve.md) (Medium) + [`decisions/2026-05-05-balance-pass-2-round-2-k-exponents.md`](decisions/2026-05-05-balance-pass-2-round-2-k-exponents.md) (Medium) + [`decisions/2026-05-05-balance-pass-2-round-3-tribute-economy.md`](decisions/2026-05-05-balance-pass-2-round-3-tribute-economy.md) (Medium) + [`decisions/2026-05-05-balance-pass-2-round-4-map-speed.md`](decisions/2026-05-05-balance-pass-2-round-4-map-speed.md) (Medium). **Round 5** ratified tower (c) DPS ladder + tier-up costs: per-tier multipliers T1=1.0× / T2=3.0× / T3=9.0× / T4 Demigod=27× / Fused God=54× (geometric ×3×3×3×2 — mirrors Round 2 winnability math; T1_base=20 dmg/sec Standard archetype anchor); tier-up costs T1=100 / T2-merge=300 / T3-merge=900 / T4-promote=2500 / Fusion=0 Tribute (Divinity-priced, 1 Divinity per Fusion + 2-Divinity menu unlock). Expected on-curve spend ≈10,700 Tribute against ≈25K Easy income → ~14,300 Tribute headroom for aux + cycling. Per-tower (cd, range, attack-type, status-proc) deferred to post-Round-10 authoring sub-pass. Filed [`decisions/2026-05-05-balance-pass-2-round-5-tower-baselines.md`](decisions/2026-05-05-balance-pass-2-round-5-tower-baselines.md) (Medium). **Round 6** ratified commander (h) ability magnitudes for damage-variant baseline floor: **passive** +15% damage to civ-matched towers within 2-cell aura (multiplicative; civ-gated; ~5–10% effective uplift at expert positioning); **active** 4× T3 DPS burst in 3-cell radius for 4s on 30s CD (2,880 burst damage; ~13% uptime; ~6.7% R30 final-boss HP per cast); **signature** once-per-match instant tier-up of one targeted tower T1→T2 or T2→T3 (free of Tribute, adjacency rule preserved; T3+ locked out). Control / summon / economy variants of the three slots deferred to per-commander authoring sub-pass (post-Round 10). Filed [`decisions/2026-05-05-balance-pass-2-round-6-commander-magnitudes.md`](decisions/2026-05-05-balance-pass-2-round-6-commander-magnitudes.md) (Medium). **Round 7** ratified aux-slot costs + (s) magnitude: **(s) Damage Bonus** = 1 Divinity = (s)=1.20 global multiplicative on damage equation, max 1 active/match (anchors Round 5 Hardcore-margin promise exactly); **Economy Bonus** = 1 Divinity = +25% per-kill Tribute on yield(R) curve (boss lumps R10/R15/R30 untouched), max 1 active/match; **Tower-count expansion** = 1 Divinity = +2 N (cap 3 Div → N=24→30 +25%); **Send-Creeps tactical baseline** = 100 Tribute (universal anchor — mode-variant income-yields tuned Round 8; PvP-IW Send-for-Interest stays Divinity-priced per Round 6 Q2 → Round 8); **Call-for-Help** = 300 Tribute one-shot; **Maze Stone** = 25 Tribute (+75 T upgrade to T1 = 100 T parity). Currency-budget audit: max-aux+1-Fusion = 5 Div ✓ (6-cap); max-aux no-Fusion = 5 Div ✓; Tribute headroom drops ~14.3K → ~12.4K Co-op/Maze typical = healthy cycling preserved. Combined per-tower expert stack = 1.20 (s) × 1.15 (h passive) × 1.25 (matchup) = **1.725× pre-(i)/(q)** validates Round 5 Hardcore-closure ground. Filed [`decisions/2026-05-05-balance-pass-2-round-7-aux-costs-and-s-ranges.md`](decisions/2026-05-05-balance-pass-2-round-7-aux-costs-and-s-ranges.md) (Medium). **Round 8** ratified per-mode tuning across 6 magnitudes: **Solo Offensive Wave + PvE-MP Lane-Trade** = 100 T → 3 std creeps + +50% kill-bonus on yield(R) (crossover ~R12-13 net-loss to net-gain); **Horde Reinforce-Lane** = 100 T → 1 helper @ `400·1.16^R` HP (= 4× R-runner HP, constant 4-runner leak-block across all R), cap 1 active per send; **PvP-Maze Send-Through-Maze** = success → +5 T/round permanent rest-of-match (early-send compounding, fail → opponent yield(R) refund); **PvP-IW Send-for-Interest** = 1 Divinity unlock (one-time) + 150 T/send + +3 T/round permanent regardless of kill outcome (Squadron TD volume-based pattern; opponent kill yields refund as defensive incentive); **Per-mode N-scaling** = Solo / Horde-A / PvP-IW / PvE-MP per-lane = N=24 (Round 4 baseline), Horde-B = 24 × player_count (linear, ring-of-zones parameterized authoring), PvP-Maze = N_maze=30/side (above Solo to fit stone-blocker pathing); **PvP tie-break (PvP-IW + PvP-Maze shared)** = R31+ HP × 1.5^(R-30) compound escalation (R35=7.6× / R40=57× / R45=437× unwinnable) + co-victory floor at R45 (single-axis (k) discipline preserved — escalation HP-only). PM picked Recommended on all 6 across 3 batches. Filed [`decisions/2026-05-05-balance-pass-2-round-8-per-mode-tuning.md`](decisions/2026-05-05-balance-pass-2-round-8-per-mode-tuning.md) (Medium). **Round 9** ratified skill-bar thresholds per (k): **Matchup-correctness** Hardcore expert 90% / Hard 75% / Easy 60% / novice 30% (drives (q) 1.25× coverage); **Placement-coverage** Hardcore expert 80% / Hard 65% / Easy 50% / novice 30% (drives (i) bonus + engaged-time ε); **Ability-uptime** Hardcore expert 80% / Hard 60% / Easy 40% / novice 20% (drives Round 6 active-burst math). Hardcore expert realized stack = 0.90 × 0.80 × 0.80 = 0.576 × 1.725× per-tower ceiling = ~1.0× realized → closes Round 5 Hardcore margin exactly with Fusion-on-schedule + tier-ladder 54×. Easy expert (0.12) sits well above novice-clear floor (0.018 → tier-ladder alone 0.635× margin clears Easy). Hard novice fails; Hardcore novice fails by orders of magnitude — first-clear gates work as designed. Telemetry definitions captured (per-axis measurement protocol; engine-side gathering is Phase 5). Round 11 mandate: random-seeded wave composition + per-map crystal-lock variance to defend threshold integrity from memorization meta. Filed [`decisions/2026-05-05-balance-pass-2-round-9-skill-bar-thresholds.md`](decisions/2026-05-05-balance-pass-2-round-9-skill-bar-thresholds.md) (Medium). **Round 10** ratified Divinity source escalation hooks (closes Numbers-phase Follow-up #13 arc): confirmed 4-Div floor (R10 boss + R15 boss + R30 final boss + match-completion = 1 Div each); **Source 5 — Perfect-Wave Bonus** = +1 Div per boss-wave (R10/R15/R30) cleared with zero leak (additive to base drop, max +3 Div across match, per-side in PvP, shared-team in co-op); **Source 6 — First-Hybrid Construction Bonus** = +1 Div one-shot per match for first true hybrid built per locked adjacency topology (per-side PvP, team-shared co-op). Total ceiling: 4 floor + 3 perfect-wave + 1 first-hybrid = **8 Div theoretical / 5–6 Div realistic expert** — fits 6-cap discipline (Round 7: max-Fusion no-aux = 6 Div ✓; max-aux+1-Fusion = 5 Div ✓). Skill-bar (Round 9) hard-gates source escalation — novice cannot accidentally accrue ceiling. PvP-IW Send-for-Interest feasibility confirmed: 1 Div unlock + 1 Div Damage Bonus = 2 Div spent vs 4 Div floor → fits without escalation; expert with perfect-R10 + first-hybrid = +2 Div = full 6-Div aux-build ceiling. 3x debug loop ran inline (R30-perfect "free for Hardcore" rejected — empirically ~30-50% expert-rate not 100%; first-hybrid "too cheap" rejected — topology meta-knowledge gate + 200 T floor; PvP-Maze rush-meta retained as strategic-decision lever; 8-Div overflow risk irrelevant — realistic 5-6, no carry-over per Round 3). Filed [`decisions/2026-05-05-balance-pass-2-round-10-divinity-sources.md`](decisions/2026-05-05-balance-pass-2-round-10-divinity-sources.md) (Medium). 3x debug loops ran inline. PM picked Recommended on every question. R1=100 normalized; rescalable. Rounds 9–10 backlog: skill-bar thresholds · Divinity sources. **No code edits** — pure concept/math. cascade-lint clean. §2.4a + §5.4 [LOCKED] untouched.

**Next planned work:**
1. **Authoring sub-pass mandate** — Numbers-phase Follow-up #13 arc CLOSED. Per-tower (cd / range / attack-type variance), per-commander (effect-type variants beyond damage-floor: control / summon / economy), per-civ specialization, per-map (good-cell authoring + wave-randomization seeds + crystal-lock variance per Round 11 mandate from R9). Likely 5-10 rounds each.
2. **CONCEPT.md amendment pass** — roll the 12-round ratifications + numbers-phase results into CONCEPT.md as §-new sections. Authoring-heavy.
3. **`admin/concept.json` migration direction** — long-deferred. PM picks: full rewrite to 3-civ/4-tier/Fusion shape, regenerate from CONCEPT.md, or retire entirely.
4. **`research/06-tw-subgenres.md`** new stub — Squadron TD / Legion TD 2 / BTD6 / Element TD / Line Tower Wars / Mini-TD deep dives.
5. **Follow-up #5 cultural-sensitivity pass scheduling.** Hard pose-lock + content-lock gate before any culturally-coded civ art ships.
6. **Follow-up #6** — Patch-1 commanders per civ + Thor Slashing+Crushing recipe-layer dissonance.
7. **C7.b deferred items** — Builder concurrency cap + 90% refund-on-cancel UI.
8. Other follow-ups #7 / #8 / #9 (Foresight-coin / PvE campaign + AGES + leveling + attributes / non-boss enemy ontology).

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

*Document version: 0.47 — 2026-05-05: Numbers-phase Round 10 LANDED — CLOSES Numbers-phase Follow-up #13 arc (10-of-10 rounds). Divinity source escalation hooks: confirmed 4-Div floor (R10 + R15 + R30 boss + match-completion = 1 Div each); Source 5 Perfect-Wave Bonus +1 Div per zero-leak boss-clear (max +3 across match, per-side PvP, team-shared co-op); Source 6 First-Hybrid Construction Bonus +1 Div one-shot per match for first true hybrid (topology-gated, per-side PvP, team-shared co-op). Ceiling 8 Div theoretical / 5-6 Div realistic expert fits 6-cap (Round 7 audit). PvP-IW Send-for-Interest feasibility confirmed; skill-bar (Round 9) hard-gates source escalation. 1 new decision document; arc closed. Authoring sub-passes (per-tower / per-commander / per-civ / per-map) now top of backlog. cascade-lint pending. §2.4a + §5.4 [LOCKED] + 17-item frame untouched. Prior: 0.46 — 2026-05-05: Round 9 (skill-bar thresholds). [Older version history archived to [`CASCADE-history.md`](CASCADE-history.md).]*
