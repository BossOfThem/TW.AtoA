---
# Decision — CONCEPT amendment pass Round 4: phase-4 §4.11 Numbers floor body populated

**Date:** 2026-05-05
**Status:** Accepted
**Reversibility:** Medium
**Affects:** [`concept/phase-4.md`](../concept/phase-4.md) §4.11 (placeholder → full body)

---

## Decision

Round 4 of the 7-round CONCEPT.md amendment pass per [`decisions/2026-05-05-concept-amendment-pass-scope.md`](2026-05-05-concept-amendment-pass-scope.md). The §4.11 placeholder body seeded in Round 3 is **replaced in-place** with the full Numbers floor — 8 sub-sections binding the magnitudes ratified across 2026-05-05 Numbers-phase #13 Rounds 1-2-3-4-5-6-8-9:

- **§4.11.1 HP curve (e)** — `HP_std(R) = 100 · 1.16^R` Easy default; m(R10)=3, m(R15)=2, m(R30)=5; anchor table R1→R30.
- **§4.11.2 (k) exponents** — Easy 1.16 / Hard 1.19 / Hardcore 1.22 (HP-only single-axis per §4.10.4); R30 anchors 8,585 / 23,737 / 65,498; PvP-no-(k) note.
- **§4.11.3 Tribute economy (a)** — `yield(R) = 5 · 1.10^R`; boss lumps R10 250T+1Div / R15 400T+1Div / R30 1500T+1Div+match-completion 1Div; cumulative Easy ~25,000 T.
- **§4.11.4 Speed (f) + per-map (j)** — `f_base = 50 u/s` constant; archetype mults Std×1.0 / Swarm×1.5 / Elite×1.0 / Boss×0.7 / Colossal×0.5; ε=0.6, N=24 baseline.
- **§4.11.5 Tower DPS ladder (c) + tier-up costs** — T1=20 / T2=60 / T3=180 / T4=540 / God=1080 dmg/sec off T1_base=20; tier-up 100/300/900/2500 T (Fusion 0T+1Div); on-curve Easy spend ~10,700 T.
- **§4.11.6 Commander magnitudes (h)** — Passive +15% civ-matched 2-cell aura; active 4×T3_DPS×4s = 2,880 burst @ 30s CD; signature once-per-match free tier-up.
- **§4.11.7 Per-mode tuning (g/p/q)** — Send-Creeps variants per mode; N=24 default / Horde-B 24×players / PvP-Maze 30; PvP R31+ HP×1.5^(R-30) tie-break + R45 co-victory.
- **§4.11.8 Skill-bar thresholds per (k)** — 3-axis × 3-(k) expert/novice grid; Hardcore expert ≈0.58× realized.

Cross-references resolve into [§4.10.x](../concept/phase-4.md#410-tower-vs-unit-math-conceptual-frame) frame anchors and forward into §4.6a auxiliary economy (lands Round 5) + phase-6 telemetry (lands Round 6).

## Context

Round 3 seeded the §4.11 anchor as a placeholder pointing at 8 source decision URLs but with no body content. Future authoring sub-passes (per-tower / per-commander / per-civ / per-map) need a single citable spine surface for the magnitudes — citing 8 dated decision files for every tuning call would defeat the consolidation premise of the amendment pass. Round 4 lands that body.

## Alternatives considered

- **Option A — Keep §4.11 as placeholder + decision-file URLs.** Rejected: every per-tower / per-commander authoring sub-pass would chase 8 decision URLs to assemble the magnitudes. Citation cost compounds across the ~50 authoring sub-passes ahead.
- **Option B — Populate §4.11 with prose-only summaries.** Rejected: magnitudes are the load-bearing content. Tables are the right format and were the format the source decisions used. Re-prosifying loses precision (e.g., "around 25,000 Tribute" vs "25,000 T cumulative R1→R30").
- **Option C — Populate §4.11 with sub-sectioned tables 1:1 with source rounds (chosen).** Each Numbers-phase round becomes a §4.11.x sub-section; tables verbatim from the source decisions; cross-link forward to §4.10.x frame anchors. Highest density / fastest citation.

## Reason chosen

Option C is the only choice that pays off the Round 3 forward-anchor commitment. The 8 sub-sections mirror the 8 source rounds, so a future reader chasing "where does Hardcore (k) come from" gets §4.11.2 → 2026-05-05 Round 2 decision URL in one hop. Tables match source-decision tables verbatim — no precision loss across the consolidation surface.

The 8th sub-section (§4.11.8 skill-bar thresholds) lands here rather than in phase-6 because the *thresholds* are magnitudes (60% / 75% / 90% etc.) — the *telemetry definitions* (how matchup-correctness is computed from gameplay events) are the phase-6 surface and land in Round 6.

## Reversibility note

**Medium.** Reverting means re-pasting the placeholder body and dropping ~120 lines of tables. Magnitudes themselves stay Accepted regardless — this round is the *display* of the 2026-05-05 Numbers-phase ratifications, not the ratifications themselves.

## Follow-ups

- **Round 5** — `phase-4.md §4.6` economy rewrite + new `§4.6a Auxiliary economy` (Tribute curves, Divinity 4-source floor + 2-source escalation, Universal-aux slot catalog, Mythium retirement note). §4.11.3 Tribute table is the source for §4.6a yield curves; §4.10.8 boss-shape is the source for §4.6 lump rewards.
- **Round 6** — phase-6 skill-bar telemetry definitions; §4.11.8 thresholds resolve forward to phase-6 §x once authored.
- **Per-tower authoring sub-pass** consumes §4.11.5 DPS ladder + tier-up costs as the spec floor; binds per-tower (cd / range / attack-type / status-proc) variance.
- **Per-commander authoring sub-pass** consumes §4.11.6 damage-floor + identity-floor for control / summon / economy effect-type variants beyond the damage-only floor.
