# CASCADE — navigation spine for Ash to Altar

The canonical index. Every doc links from here in the order a new reader (human or Claude) should encounter it. If you are a new session: **`README.md` → `CLAUDE.md` → this file → target doc.** Do not hunt.

Non-negotiables + naming conventions + cascade discipline live in [`README.md`](README.md) + [`CLAUDE.md`](CLAUDE.md); this doc is pure navigation.

---

## How the doc tree works

The project uses a waterfall cascade (see [`CONCEPT.md`](CONCEPT.md) Phases 1–7). It shows up in three places:

1. **Conceptual cascade** — Phases 1–7 in `CONCEPT.md`. Discovery → Analysis → Design → Specification → Implementation → Validation → Iteration. Phase N+1 does not silently edit Phase N.
2. **Player-journey cascade** — [`stages/`](stages/) dir. One doc per player-experience stage.
3. **Research cascade** — [`research/`](research/) dir. Deep-dive market evidence feeding stage decisions.

Cross-link convention:
- Stage-to-stage: `[stage 03 — match setup](stages/03-match-setup.md#section)`
- Decisions: `[2026-04-20 <slug>](decisions/2026-04-20-<slug>.md)`
- Concept anchors: `[CONCEPT §3.3](CONCEPT.md#33-...)`

Stages + research tables (status, last-reviewed) live in [`CASCADE-tables.md`](CASCADE-tables.md) — load on demand when working on those surfaces.

---

## Reading order (new session)

1. [`README.md`](README.md) — status, non-negotiables, critical context.
2. [`CLAUDE.md`](CLAUDE.md) — session conventions, cadence, 3x debug loop.
3. [`HANDOFF.md`](HANDOFF.md) — last-session checkpoint.
4. This file — the map.
5. [`PROGRESS.md`](PROGRESS.md) — step tracker; first unchecked box = next step (unless queue paused).
6. [`CONCEPT.md`](CONCEPT.md) — vision hub. Phase content lives under [`concept/phase-1..7.md`](concept/); open only what you need.
7. [`CONCEPT-GAPS.md`](CONCEPT-GAPS.md) — ephemeral proposal layer.
8. Target stage / research / decision doc per "Current work pointer" below.

---

## Current work pointer

**2026-04-29 — Paid-EA supersession ratified + PROJECT-ARC.md filed + DA-1 Hard-class flag pending AM review + Phase B cascade landed.** Overnight autonomous-mandate run: (1) [`decisions/2026-04-28-paid-ea-single-product-supersedes-pivot.md`](decisions/2026-04-28-paid-ea-single-product-supersedes-pivot.md) moved Status Proposed → **Accepted** under PM "go" + autonomous-mandate authorization. (2) [`concept/PROJECT-ARC.md`](concept/PROJECT-ARC.md) filed as end-to-end project skeleton (11 sections; Phases A→J + A.5; 12 PM-only forks; 9 discipline locks D-1..D-9 plus D-10 EZ.FINISH AskUserQuestion-as-overnight-deferred-discipline added under PM EZ.FINISH guidance; 6 reversal triggers; 3x debug loop embedded §9; broad-attack DA pass §10 with 12 findings DA-1..DA-12). (3) DA-1 (Hard-class) **flagged for AM review** — questions whether the supersession's autonomous-mandate ratification adequately deliberated a Hard-class pivot reversal vs. the autonomy-mandate-as-Numbers-phase-pattern original framing; not reversal-blocking but worth PM acknowledgement. (4) Phase B cascade items B.1-B.7 landed (per PROJECT-ARC.md §5): [`decisions/2026-04-29-promise-1-scope-cut.md`](decisions/2026-04-29-promise-1-scope-cut.md) (autonomous-default Tower + PvP-Co-op; Horde-A canonical co-op shape; PM-Fork-2 AM-flagged for ratify-or-redirect to Tower + Custom or other) + [`decisions/2026-04-29-promise-3-paid-base-discipline-lock.md`](decisions/2026-04-29-promise-3-paid-base-discipline-lock.md) (Hard-class lock paid-base + day-1-visible-BP + cosmetic-only across EA→1.0; reversing requires written supersession) + [`decisions/2026-04-29-prototype-port-source-re-supersession.md`](decisions/2026-04-29-prototype-port-source-re-supersession.md) (re-supersedes 2026-04-19 throwaway framing; 50-55% deliverable-logic ports forward in Phase E; not a Steam SKU) + [`decisions/2026-05-07-atoa-shippable-mtm-successor-pivot.md`](decisions/2026-05-07-atoa-shippable-mtm-successor-pivot.md) marked **Superseded** + CONCEPT.md hub edits (Phase 3 row reflects 2 feature-complete + 5 roadmap-stretch under paid-EA refund-backed roadmap; "Go big at launch" non-negotiable rewritten under cut-shape interpretation as "breadth unreachable, depth preserved"; version footer 0.91) + CLAUDE.md "No code yet" clause updated for engine work imminent under PROJECT-ARC.md Phase C. (5) **Phase 4 exit-gate items remaining: #9 Engine lock (Hard-class fork; resolves under PROJECT-ARC.md Phase C engine-choice mini-arc — Godot 4 / Unity / Unreal; PM-Fork-6) and #10 Art director (PM-decisional; resolves under PROJECT-ARC.md Phase E item E.7; PM-Fork-10).** Hard guards verified untouched verbatim throughout. PM autonomy mandate carries; AskUserQuestion (EZ.FINISH) deferred-to-AM under D-10 discipline.

**Carried blockers / debt:** `49c4c54` `.accord/` 69MB blob in history (purge needs explicit PM authorization).

**AM-review priority:** DA-1 Hard-class flag (supersession-ratification deliberation question) + PM-Fork-2 ratify-or-redirect (Tower + PvP-Co-op autonomous-default vs. Tower + Custom alternative) + PROJECT-ARC.md skeleton ratify (Phases C-J pre-execution). See HANDOFF.md.

*Older pointers archived to [`CASCADE-history.md`](CASCADE-history.md).*

**Next planned work (PROJECT-ARC.md Phase C + Phase D, parallel-safe):** Phase C engine-choice mini-arc (PM-Fork-6 lock under 4-round queue; closes Phase-4 §4.8 item #9) · Phase D differentiation swarm (8 comparators × 9 axes per [`concept/atoa-vs-mtm/PREP-refinement-question.md`](concept/atoa-vs-mtm/PREP-refinement-question.md) §3; produces `research/<date>-tw-comparator-matrix.md` + `decisions/<date>-atoa-differentiation-thesis.md` feeding Phase F Steam-page draft).

**2026-04-29 (continuation, second-night autonomous-mandate)** — Phase C + Phase D both chartered and R1-executed in parallel as background swarms. **Phase D arc closed end-to-end** under autonomous-mandate: charter [`concept/atoa-vs-mtm/diff-swarm/CHARTER.md`](concept/atoa-vs-mtm/diff-swarm/CHARTER.md) → R1 (3 comparator-audit agents, A/B/C turn-ins filed) → alignment-check (cross-bucket consistency clean; 5 cross-bucket observations surfaced) → R2 (R2-A thesis: T1 three-layer authored civ identity-density / T3 Fusion 9-recipe lock + 7-type RPS / T4 two-mode-at-depth shared-substrate; T2 cross-coherence demoted to substrate-asterisk; R2-B counter: C1 modding / C2 mode-roster breadth / C3 discoverability-substrate, all concession-class, none triggers RT-3) → R3 synthesizer outputs filed: [`research/2026-04-29-tw-comparator-matrix.md`](research/2026-04-29-tw-comparator-matrix.md) (72-cell substrate) + [`decisions/2026-04-29-atoa-differentiation-thesis.md`](decisions/2026-04-29-atoa-differentiation-thesis.md) (**Proposed**, Easy reversibility, awaits PM AM-review). **Phase C arc paused at PM-Fork-6 gate** per charter discipline (engine choice is PM-only; not autonomous-decidable): charter [`concept/engine-choice/CHARTER.md`](concept/engine-choice/CHARTER.md) → R1 (4 evidence-gather agents A/B/C/D — tooling+2D / netcode+port / hiring+royalty / other-bucket-null) → alignment-check + PM-Fork-6 fork-resolution brief filed at `concept/engine-choice/alignment-check-and-pm-fork-6-brief.md` (three-way fork Godot 4 / Unity / Unreal; RT-2 not triggered; Unreal carries soft-pressure flag; **no engine pick made**). Phase C R3 spec-grammar + RN cross-arc audit gated on PM-Fork-6 resolution.

**AM-review priority (continuation):** PM-Fork-6 engine pick (Phase C R1 evidence + alignment brief ready) · differentiation-thesis decision Proposed → Accept (or redirect axes) · Phase D exit-gate closure confirmation (cleanly executed under autonomous-mandate; thesis lands as Proposed pending PM ratify).

---

## Decisions — dated log

Every concept-constraint change + every ratified gap-resolution lives here. Format: [`TEMPLATE.md`](decisions/TEMPLATE.md). One-line hooks only — open the linked file for full content.

| Date | Decision | Reversibility |
|------|----------|---------------|
| 2026-04-29 | [AtoA differentiation thesis — Phase D swarm output (T1 three-layer authored civ identity-density + T3 Fusion 9-recipe lock + 7-type RPS + T4 two-mode-at-depth shared-substrate as wins; C1 modding + C2 mode-roster breadth + C3 discoverability-substrate as honest concessions; **Proposed** awaits PM AM-review; feeds Phase F.2 Steam-page draft)](decisions/2026-04-29-atoa-differentiation-thesis.md) | Easy |
| 2026-04-29 | [Prototype reverts to port-source under paid-EA single-product (re-supersedes 2026-05-07 free-Steam-SKU framing; preserved 50-55% deliverable-logic ports forward to engine in Phase E; archive trigger at Phase E exit)](decisions/2026-04-29-prototype-port-source-re-supersession.md) | Medium |
| 2026-04-29 | [Promise 3 paid-base discipline-lock (paid-base + day-1-visible-BP + cosmetic-only across EA→1.0; never reverse without written supersession; structural defense against F2P anger pattern + commercial/player-experience anti-alignment)](decisions/2026-04-29-promise-3-paid-base-discipline-lock.md) | **Hard** |
| 2026-04-29 | [Promise 1 scope cut from 7 mode-types to 2 (autonomous-default Tower + PvP-Co-op feature-complete at 1.0; Horde-A canonical co-op; remaining 5 modes roadmap-stretch under paid-EA's public refund-backed roadmap; PM-Fork-2 AM-flagged for ratify-or-redirect)](decisions/2026-04-29-promise-1-scope-cut.md) | **Hard** |
| 2026-04-28 | [Paid Early Access single-product (Accepted 2026-04-29; supersedes 2026-05-07 two-product pivot; $15-20 paid-EA at Steam; Promise 1 scope cut to 2 mode-types; paid-EA's externalized refund-backed public roadmap as discipline mechanism)](decisions/2026-04-28-paid-ea-single-product-supersedes-pivot.md) | **Hard** |
| 2026-05-06 | [Fusion-numerics balance-pass ratification (§4.8 item #6 DONE; 3-check cross-coherence audit zero cascade-violations; 36-cell row × locked-Fusion-shape + R30-boss-clear cumulative-DPS sanity 51.7s @ Hardcore-expert realized + 45-cell three-civ-fingerprint at God tier 44/45 with locked Norse Odin anti-type-hole-coverage; no new design surface; Phase 4 9/11)](decisions/2026-05-06-fusion-numerics-balance-pass-ratification.md) | Medium |
| 2026-05-06 | [Cultural-sensitivity Phase-4-exit gate ratification (§4.8 item #11 DONE; 3-check audit zero cascade-violations; 13-touchpoint binding-coverage / 3-named-scope / hard-gate-enforcement; gate body Hard-class / execution Easy-class; Phase 4 8/11)](decisions/2026-05-06-cultural-sensitivity-phase-4-exit-gate-ratification.md) | **Hard** |
| 2026-05-06 | [Monetization specifics ratification (§4.8 item #8 DONE; 4-check cross-coherence audit zero cascade-violations; cosmetic-only / no-p2w model-shape Hard-class lock; commercial price-point + BP cadence + DLC catalog cadence Easy-class PM-deferred; Phase 4 7/11)](decisions/2026-05-06-monetization-specifics-ratification.md) | **Hard** |
| 2026-05-06 | [Economy paper-balance ratification (§4.8 item #7 DONE; 3-check cross-coherence audit zero cascade-violations; Phase 4 6/11 exit-gate items closed)](decisions/2026-05-06-economy-paper-balance-ratification.md) | Medium |
| 2026-05-06 | [§4.4 mobile unit control RN — cross-arc audit + spine-doc edits + arc close (CLOSES ARC 4/4; 12-cell 3-axis audit zero cascade-violations; §4.8 item #5 DONE; Phase 4 5/11 exit-gate items closed)](decisions/2026-05-06-mobile-unit-control-rn-cross-arc-audit-and-arc-close.md) | Medium |
| 2026-05-06 | [§4.4 mobile unit control R3 — spec-grammar authoring (speed ladder T1-T4 / pathing-mode catalog / engagement-rule catalog with per-tier §3.4 falsification / aggro tie-breaker resolution stable-sort + no-override)](decisions/2026-05-06-mobile-unit-control-r3-spec-grammars.md) | Medium |
| 2026-05-06 | [§4.4 mobile unit control R2 — control-model direction lock (Option (i) waypoint + mode-flags ratified; 4-flag catalog + 3-default engagement shape + no-tier-scaling principle; civ-neutral mechanical-content)](decisions/2026-05-06-mobile-unit-control-r2-direction-lock.md) | Medium |
| 2026-05-06 | [§4.4 mobile unit control R1 scope (4-round per-property axis; control-model lock + spec-grammars + RN audit; spec-level grain only)](decisions/2026-05-06-mobile-unit-control-r1-scope.md) | Medium |
| 2026-05-06 | [§4.7 enemy direction RN — cross-arc audit + spine-doc edits + arc close (CLOSES ARC 4/4; 42-cell 3-axis audit zero cascade-violations; §4.8 item #4 DONE)](decisions/2026-05-06-enemy-direction-rn-cross-arc-audit-and-arc-close.md) | Medium |
| 2026-05-06 | [§4.7 enemy direction R3 — R11 wave-composition variance grammar (5 spec-level bindings; (k) band-center + matchup-affinity overlay + diversity envelope)](decisions/2026-05-06-enemy-direction-r3-r11-variance-grammar.md) | Medium |
| 2026-05-06 | [§4.7 enemy direction R2 — Option C ratified (civ-matched bosses + shared regular-wave pool; 5-class distribution bands)](decisions/2026-05-06-enemy-direction-r2-direction-lock.md) | Medium |
| 2026-05-06 | [§4.7 enemy direction + R11 wave-variance R1 scope (4-round per-property axis; R11 bundled)](decisions/2026-05-06-enemy-direction-r1-scope.md) | Medium |
| 2026-05-06 | [Post-per-civ-arc ratifications (next-track §4.7+R11 / admin.json retired / phase-4 cap 600→700 / cultural-sensitivity at Phase-4 exit)](decisions/2026-05-06-post-arc-ratifications.md) | Mixed |
| 2026-05-06 | [Per-civ RN — cross-civ × cross-field audit + arc close (CLOSES ARC 4/4; 15/15 zero cascade-violations; 3-civ-3-equation-form fingerprint locked)](decisions/2026-05-06-per-civ-rn-cross-civ-audit-and-arc-close.md) | Medium |
| 2026-05-06 | [Per-civ R4 — Norse profile (5 fields + identity_hook 3x debug + R3-prediction validated + → RN hook)](decisions/2026-05-06-per-civ-r4-norse-profile.md) | Medium |
| 2026-05-06 | [Per-civ R3 — Aztec profile (5 fields + identity_hook 3x debug + R2-prediction reconciliation + → R4 hook)](decisions/2026-05-06-per-civ-r3-aztec-profile.md) | Medium |
| 2026-05-06 | [Per-civ R2 — Greek profile (5 fields + identity_hook 3x debug + → R3 hook)](decisions/2026-05-06-per-civ-r2-greek-profile.md) | Medium |
| 2026-05-06 | [Per-civ specialization sub-pass scope (4-round queue + 5-field schema + Axis A)](decisions/2026-05-06-per-civ-specialization-scope.md) | Medium |
| 2026-05-06 | [Per-tower RN — cross-civ × cross-tier audit + arc close (45/45 zero cascade-violations; 3 orthogonal civ-magnitude axes confirmed)](decisions/2026-05-06-per-tower-rn-cross-civ-audit-and-arc-close.md) | Medium |
| 2026-05-06 | [Per-tower R4 — Norse roster (15 towers × 7 fields; cd-1.15s fastest / range-3.5 shortest / Bleed-density 6-of-15)](decisions/2026-05-06-per-tower-r4-norse-roster.md) | Medium |
| 2026-05-06 | [Per-tower R3 — Aztec roster (15 towers × 7 fields; band-high T2-T3 / cd-1.4s / Poison-Fire-Slashing bleed)](decisions/2026-05-06-per-tower-r3-aztec-roster.md) | Medium |
| 2026-05-06 | [Per-tower R2 — Greek roster (15 towers × 7 fields; cd-1.7s / range-4.0 / Divine-density 4-of-15)](decisions/2026-05-06-per-tower-r2-greek-roster.md) | Medium |
| 2026-05-06 | [Per-tower authoring sub-pass scope (4-round queue + 7-field schema + Axis A)](decisions/2026-05-06-per-tower-authoring-scope.md) | Medium |
| 2026-05-05 | [Per-commander R5 — audit + arc close (Aztec breakpoint Lever-2 applied; aura-anchor resolved; 3 one-pagers; spine-doc edits)](decisions/2026-05-05-per-commander-r5-audit-and-arc-close.md) | Medium |
| 2026-05-05 | [Per-commander R4 — signature variants (Last Stand / Great Sacrifice / Great Heathen Army; once-per-match free)](decisions/2026-05-05-per-commander-r4-signature-variants.md) | Medium |
| 2026-05-05 | [Per-commander R3 — short-CD active variants (This Is Sparta! / Sun Offering / Berserk; 30s base CD)](decisions/2026-05-05-per-commander-r3-short-cd-active-variants.md) | Medium |
| 2026-05-05 | [Per-commander R2 — passive variants (Spartan Training / Blood Tribute / Sons of Ragnar; +15% benchmark)](decisions/2026-05-05-per-commander-r2-passive-variants.md) | Medium |
| 2026-05-05 | [Per-commander effect-type-variant authoring scope (5-round queue + per-ability-slot axis)](decisions/2026-05-05-per-commander-effect-type-variant-authoring-scope.md) | Medium |
| 2026-05-05 | [CONCEPT amendment pass R7 — hub close (CLOSES ARC 7/7; Non-negotiables "Go big at launch" promoted; footer 0.8→0.9)](decisions/2026-05-05-concept-amendment-pass-round-7-hub-close.md) | Easy |
| 2026-05-05 | [CONCEPT amendment pass R6 — phase-4 §4.7 wave-variance R11 + phase-6 §6.5 telemetry + phase-7 §7.4 "Go big"](decisions/2026-05-05-concept-amendment-pass-round-6-phase-4-7-r11-and-phase-6-7.md) | Easy |
| 2026-05-05 | [CONCEPT amendment pass R5 — phase-4 §4.6 Economy rewrite + §4.6a Auxiliary economy NEW (7-slot catalog)](decisions/2026-05-05-concept-amendment-pass-round-5-phase-4-economy.md) | Medium |
| 2026-05-05 | [CONCEPT amendment pass R4 — phase-4 §4.11 Numbers floor body populated (8 sub-sections)](decisions/2026-05-05-concept-amendment-pass-round-4-phase-4-numbers-floor.md) | Medium |
| 2026-05-05 | [CONCEPT amendment pass R3 — phase-4 §4.10 Tower-vs-Unit math NEW (variable nomenclature (a)-(s))](decisions/2026-05-05-concept-amendment-pass-round-3-phase-4-tower-vs-unit-math.md) | Medium |
| 2026-05-05 | [CONCEPT amendment pass R2 — phase-3 §3.6 mode roster 5→6 + per-mode summary table](decisions/2026-05-05-concept-amendment-pass-round-2-phase-3-modes.md) | Easy |
| 2026-05-05 | [CONCEPT.md amendment pass scope (7-round queue + §-placement table)](decisions/2026-05-05-concept-amendment-pass-scope.md) | Easy |
| 2026-05-05 | [Balance-pass #2 R10 — Divinity source escalation (CLOSES arc; 4-Div floor + Sources 5/6)](decisions/2026-05-05-balance-pass-2-round-10-divinity-sources.md) | Medium |
| 2026-05-05 | [Balance-pass #2 R9 — Skill-bar thresholds per (k); Hardcore expert closes margin exactly](decisions/2026-05-05-balance-pass-2-round-9-skill-bar-thresholds.md) | Medium |
| 2026-05-05 | [Balance-pass #2 R8 — Per-mode tuning + N-scaling + PvP tie-break (R31+ HP×1.5; R45 co-victory)](decisions/2026-05-05-balance-pass-2-round-8-per-mode-tuning.md) | Medium |
| 2026-05-05 | [Balance-pass #2 R7 — Aux-slot costs + (s) ranges](decisions/2026-05-05-balance-pass-2-round-7-aux-costs-and-s-ranges.md) | Medium |
| 2026-05-05 | [Balance-pass #2 R6 — Commander (h) ability magnitudes (passive +15% / active 4× T3 / signature free tier-up)](decisions/2026-05-05-balance-pass-2-round-6-commander-magnitudes.md) | Medium |
| 2026-05-05 | [Balance-pass #2 R5 — Tower DPS ladder T1=1×/T2=3×/T3=9×/T4=27×/God=54× + tier-up costs](decisions/2026-05-05-balance-pass-2-round-5-tower-baselines.md) | Medium |
| 2026-05-05 | [Balance-pass #2 R4 — Speed (f) + per-map (j); f_base=50 u/s + archetype multipliers](decisions/2026-05-05-balance-pass-2-round-4-map-speed.md) | Medium |
| 2026-05-05 | [Balance-pass #2 R3 — Tribute economy (a); yield(R)=5·1.10^R + boss lumps](decisions/2026-05-05-balance-pass-2-round-3-tribute-economy.md) | Medium |
| 2026-05-05 | [Balance-pass #2 R2 — (k) compounding exponents; Easy 1.16 / Hard 1.19 / Hardcore 1.22](decisions/2026-05-05-balance-pass-2-round-2-k-exponents.md) | Medium |
| 2026-05-05 | [Balance-pass #2 R1 — Runner HP curve (e); HP_std(R)=100·1.16^R Easy + boss spikes](decisions/2026-05-05-balance-pass-2-round-1-hp-curve.md) | Medium |
| 2026-05-04 | [Round 12 — Aux UX + frame variable (s) + per-mode (k) + maze validity](decisions/2026-05-04-round-12-aux-ux-frame-extension.md) | Medium |
| 2026-05-04 | [Round 11 — PvP Maze Lane deep-dive (hex-grid, A*, Send-Through-Maze, lives=10)](decisions/2026-05-04-round-11-pvp-maze-deep-dive.md) | Medium |
| 2026-05-04 | [Round 10 — PvE Multiplayer deep-dive (N parallel lanes, last-alive)](decisions/2026-05-04-round-10-pve-mp-deep-dive.md) | Medium |
| 2026-05-04 | [Round 9 — PvP Interest Wars deep-dive + lives extension (20s rounds, 30-leak knockout)](decisions/2026-05-04-round-9-pvp-interest-wars-deep-dive.md) | Medium |
| 2026-05-04 | [Round 8 — Horde Co-op deep-dive + co-op mode split (Horde-A + Horde-B)](decisions/2026-05-04-round-8-horde-coop-deep-dive.md) | Medium |
| 2026-05-04 | [Round 7 — Solo Campaign deep-dive (multi-mission saga, single-lane)](decisions/2026-05-04-round-7-solo-campaign-deep-dive.md) | Medium |
| 2026-05-04 | [Round 6 — Aux economy ratifications + "Go big, no scope cuts" doctrine](decisions/2026-05-04-round-6-aux-economy-ratifications.md) | Medium |
| 2026-05-04 | [Auxiliary economy structure + game modes ontology (Accepted; advanced from Proposed via R6-R12)](decisions/2026-05-04-auxiliary-economy-and-modes-scope.md) | Medium |
| 2026-05-04 | [Balance-pass #1 conceptual frame (17-item ratification of tower-vs-unit math)](decisions/2026-05-04-balance-pass-1-conceptual-frame.md) | Medium |
| 2026-05-04 | [Aztec glyph: abstract placeholder pending cultural-sensitivity pass (closes Follow-up #4)](decisions/2026-05-04-aztec-glyph-abstract-placeholder.md) | Easy |
| 2026-04-28 | [§5.4 [LOCKED] amendment: delete Lineages row, add Civilizations row (closes Follow-up #10)](decisions/2026-04-28-phase-5-naming-conventions-lineages-row-deletion.md) | Easy |
| 2026-04-27 | [Commander-as-summoned-ability-avatar (+ Builder unit class; supersedes 2026-04-20 on-field-hero)](decisions/2026-04-27-commander-as-summoned-ability-avatar.md) | Medium |
| 2026-04-26 | [Prototype reshape plan (Step C, 6 steps + 2026-04-27 amendment; **Accepted 2026-04-29**)](decisions/2026-04-26-prototype-reshape-plan.md) | Medium |
| 2026-04-26 | [Phase 1 exit one-pager (closes 2026-04-25 Follow-up #11)](decisions/2026-04-26-phase-1-exit-one-pager.md) | Easy |
| 2026-04-26 | [Attack-type mapping: 7-type taxonomy + per-tower map + RPS armor matrix + status-proc table](decisions/2026-04-26-attack-type-mapping.md) | Medium |
| 2026-04-25 | [Q2 ratified: real-world cultures direction (Greek / Aztec / Norse) + launch-match design skeleton](decisions/2026-04-25-q2-real-cultures-direction-ratified.md) | **Hard** |
| 2026-04-25 | [Q2 world pitch draft (synthetic mythic-history braid) — **Superseded by 2026-04-25 ratification**](decisions/2026-04-25-q2-world-pitch-draft.md) | n/a |
| 2026-04-24 | [Phase 1 vision reopen — supersedes 2026-04-21 + 2026-04-22; thematic direction partially superseded by 2026-04-25](decisions/2026-04-24-phase-1-vision-reopen-synthetic-mythic-history.md) | **Hard** |
| 2026-04-21 | [Concept tightening: 3/3/3 + dungeon cosmology + Ash-enabler hybrids — **Superseded by 2026-04-24**](decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md) | **Hard** |
| 2026-04-19 | [Cascade restructure: consolidate to root, create stages/research/decisions dirs](decisions/2026-04-19-cascade-restructure.md) | Medium |
| 2026-04-19 | [Admin UI v1: single-file node-graph concept map](decisions/2026-04-19-admin-ui-v1.md) | Easy |
| 2026-04-19 | [Design prototype scope: throwaway HTML/JS permitted](decisions/2026-04-19-design-prototype-scope.md) | Easy |
| 2026-04-19 | [Tutorial glow affordance too subtle — log as design-debt](decisions/2026-04-19-tutorial-cell-affordance.md) | Easy |
| 2026-04-19 | [Intro-game baseline gaps escalated to concept-gaps pass](decisions/2026-04-19-intro-baseline-gaps.md) | Easy |
| 2026-04-19 | [Concept thinness load-bearing — pause workflow queue for concept-gaps pass](decisions/2026-04-19-concept-thinness-escalation.md) | Easy |
| 2026-04-20 | [Meta-UI envelope: settings menu + pause/meta-controls bundle](decisions/2026-04-20-meta-ui-envelope.md) | Easy |
| 2026-04-20 | [Audio architecture: 5-bus mixer + ducking + focus-loss](decisions/2026-04-20-audio-architecture.md) | Easy |
| 2026-04-20 | [Accessibility floor as Phase 2 constraint](decisions/2026-04-20-accessibility-floor.md) | Hard |
| 2026-04-20 | [Commander identity floor: Phase 4 §4.1 minimum spec](decisions/2026-04-20-commander-identity-floor.md) | Medium |
| 2026-04-20 | [First-run flow: click budget + returning-player branch + skippable tutorial](decisions/2026-04-20-first-run-flow.md) | Easy |
| 2026-04-20 | [Save model: mode-aware save + always-persistent commander profile](decisions/2026-04-20-save-model.md) | Medium |
| 2026-04-20 | [Prototype `hybrid.pair` is ancestry tag only](decisions/2026-04-20-prototype-hybrid-pair-shape.md) | Easy |
| 2026-04-20 | [Prototype pivots from throwaway to playable concept-demo (Step 10 unblocks Step 5 playtest)](decisions/2026-04-20-prototype-concept-demo-pivot.md) | Medium |
| 2026-04-20 | [Prototype debug-check sweep (pre-playtest) — 6 findings resolved](decisions/2026-04-20-prototype-debug-check-sweep.md) | Easy |
| 2026-04-20 | [Prototype interaction layer — hover / right-click / sell / upgrade [PROPOSAL] / reference panel](decisions/2026-04-20-prototype-interaction-layer.md) | Medium |
| 2026-04-20 | [Prototype visuals overhaul + insight layer](decisions/2026-04-20-visuals-insight-pass.md) | Medium |
| 2026-04-20 | [Doc-cascade split: CONCEPT.md → hub + concept/phase-1..7.md (+ cascade-lint)](decisions/2026-04-20-doc-cascade-split.md) | Easy |
| 2026-04-20 | [Meta-UI shell polish (splash glyphs / login branch / menu branch / mode-aware pause)](decisions/2026-04-20-meta-ui-shell-polish.md) | Easy |
| 2026-04-20 | [Profile panel layer — dedicated Profile scene + mode-gated writeMatchSave](decisions/2026-04-20-profile-panel-layer.md) | Easy |
| 2026-04-20 | [Options 5 tabs real — audio sliders + rebind + video/a11y/gameplay persisted](decisions/2026-04-20-options-five-tabs-real.md) | Easy |
| 2026-04-20 | [Commander-pick identity upgrade — SVG silhouettes + XP ladder + cosmetic locks](decisions/2026-04-20-commander-pick-identity-upgrade.md) | Easy |
| 2026-04-20 | [First-run discoverability prompts (right-click / I-key / hover) with permanent dismiss](decisions/2026-04-20-first-run-discoverability.md) | Easy |
| 2026-04-20 | [Age-as-history flavor banner + mapmods.json data + auto-age-up toggle](decisions/2026-04-20-age-history-flavor-mapmods.md) | Medium |
| 2026-04-20 | [Spontaneity random events (events.json, 25% seeded LCG, weighted pool)](decisions/2026-04-20-spontaneity-random-events.md) | Easy |
| 2026-04-20 | [Commander-on-field hero — **Superseded by 2026-04-27**](decisions/2026-04-20-commander-on-field-hero.md) | Medium |
| 2026-04-22 | [Step B: Prototype reshape plan — **Superseded by 2026-04-24** (18 sub-steps void)](decisions/2026-04-22-step-b-prototype-reshape-plan.md) | Medium |

---

## Admin UI / Prototype / Legacy

- [`admin/index.html`](admin/index.html) — node-graph admin UI per [decision](decisions/2026-04-19-admin-ui-v1.md). **`admin/concept.json` retired 2026-05-06** from source-of-truth chain per [post-arc ratifications](decisions/2026-05-06-post-arc-ratifications.md); `concept/phase-*.md` tree + `decisions/` files are sole truth. JSON file remains in repo as historical artifact only.
- [`prototype/index.html`](prototype/index.html) + [`prototype/data/`](prototype/data/) + [`prototype/start.bat`](prototype/start.bat) (Python `http.server` :8765) + [`prototype/PORT-NOTES.md`](prototype/PORT-NOTES.md) + [decision](decisions/2026-04-19-design-prototype-scope.md).
- `tw-commanders-starter/` — original starter; archived 2026-04-19. Do not edit.

---

## When to update this doc

- Stage / research status changes (Stub → Draft → In review → Locked).
- New decision file added → add one-line row to table above.
- Current work pointer shifts.
- Doc renamed, moved, archived.

Treat `CASCADE.md` as single source of truth for "what exists and where." If it disagrees with the filesystem, fix one or the other.

---

*Document version: 0.85 — 2026-04-29: Paid-EA supersession ratified Proposed→Accepted under autonomous-mandate go; PROJECT-ARC.md filed as end-to-end project skeleton (11 sections; 12 PM-only forks; 10 discipline locks; 6 reversal triggers; broad-attack DA pass §10 produced 12 findings; DA-1 Hard-class flag for AM review on supersession-ratification deliberation depth); Phase B cascade landed (Promise 1 scope cut to 2 mode-types Tower + PvP-Co-op autonomous-default + Horde-A canonical co-op + PM-Fork-2 AM-flagged; Promise 3 paid-base discipline-lock Hard-class for paid-base + day-1-visible-BP + cosmetic-only across EA→1.0; prototype re-supersession to port-source under paid-EA; 2026-05-07 two-product pivot marked Superseded; CONCEPT.md hub Phase 3 row + "Go big at launch" non-negotiable rewritten under cut-shape interpretation; CLAUDE.md "No code yet" clause updated for engine work imminent). Phase 4 exit-gate remains 9/11 (items #9 engine + #10 art director resolve under PROJECT-ARC.md Phases C + E). Hard guards verified untouched. PM autonomy mandate carries. Older versions including 0.84 — 2026-05-06: Fusion-numerics balance-pass ratification LANDED (§4.8 item #6 ✅ DONE). Single-doc 3-check cross-coherence audit at zero cascade-violations closing the Fusion-numerics deferral that Economy paper-balance explicitly skipped: 36-cell per-God row × locked-Fusion-shape verification (recipe / 2-type pair / DPS ±20% / Divinity-cadence) all 9 Gods PASS with mean DPS +1.55% above 1,080 baseline; cumulative-team-DPS R30-boss-clear sanity at Hardcore-expert realized = 51.7s vs 69.3s no-fusion counterfactual = ~25% kill-time reduction = Fusion structurally load-bearing at peak; 45-cell three-civ-fingerprint at God tier 44/45 expression with locked Norse Odin L1 anti-type-hole-coverage (Divine-pre-T4 hole resolution per 2026-04-25 multi-civ-future commitment) + 4-axis cross-civ orthogonality (cd / range / DPS-aggregate / status_proc-kind primary all falsifiably distinct). Reversibility **Medium** (no fresh magnitudes; ratifies cross-coherence between already-locked upstream surfaces). Phase 4 advances to **9 of 11 exit-gate items closed**. 2 items remaining: #9 Engine lock (Hard-class fork) / #10 Art director (PM-decisional). PM autonomy mandate carries. Prior 0.83 — Cultural-sensitivity Phase-4-exit gate ratification. Older versions archived to [`CASCADE-history.md`](CASCADE-history.md).*
