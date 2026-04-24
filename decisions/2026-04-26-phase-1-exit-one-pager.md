# Decision — Phase 1 exit one-page write-up

**Date:** 2026-04-26
**Status:** Accepted
**Reversibility:** Easy (formal capture of already-ratified decisions; reversal = reopen Phase 1 via a dated reopen entry, as was done 2026-04-24)
**Affects:** `concept/phase-1.md` (exit gate formally satisfied), `CASCADE.md` (Phase 1 status → Exited), downstream Phase 2+ inherits a closed Phase 1 reference frame.
**Closes:** [`2026-04-25-q2-real-cultures-direction-ratified.md`](2026-04-25-q2-real-cultures-direction-ratified.md) Follow-up **#11**.

---

## The one page

**What game are we building?**

A **tower-wars game where every match plays as a compressed mortal-to-mythic arc grounded in real-world cultures and their native myths.** Lane-wars core loop, 30 waves, 5-25 minute session, PC-first, solo-first, no-pay-to-win, two-dev-team scoped.

**World.**

Three civilizations at launch — **Greek, Aztec, Norse.** Each civilization is a complete self-contained identity: its own 6 T1-T3 towers, 5 units, 6 T4 Demigods & Heroes, and 3 locked Gods reachable only through Fusion. Civilization identity is the match-to-match container the player picks at login and re-picks or varies across sessions.

Cultures are handled with **"mundane outside, myth inside"** discipline. The tower labels are things a high-schooler would recognize as historical buildings (Phalanx, Pyramid, Longhouse). The mythic identity lives inside — in upgrade arcs, ability flavor, unit names once promoted, and most visibly in the T4→God Fusion endgame. Cultural sensitivity is a hard gate before any content lock, not a polish pass ([`decisions/2026-04-25-q2-real-cultures-direction-ratified.md`](2026-04-25-q2-real-cultures-direction-ratified.md) Follow-up #5).

**Commander role.**

The Commander is the player's persistent identity. At launch the three Commanders are **Leonidas of Sparta, Montezuma II, and Ragnar Lothbrok** — one per civilization, each a legally-usable historical leader whose silhouette, voice, and kit a player already has some mental image of ("high-school recognizable"). Each has a 3-ability kit (passive + short-CD active + long-CD active) and a sticky signature flavor distinct from the other two on its civ and across civs.

In-match, the Commander is the player's lever over a match that would otherwise be purely tower-placement optimization. The Commander **spends Tribute** to buy and merge units/towers up the tier ladder (T1 swarm → T2 mainline → T3 elite → T4 Demigod/Hero) and **spends Divinity** to access and execute the Fusion endgame (2 Demigods → one of 9 named Gods per civ). The Commander is not a skin with a stat modifier — their voice lines, progression ladder (20 levels with cosmetic ticks at L5/L10/L15), and identity-floor commitments are baseline, not stretch goals ([`decisions/2026-04-20-commander-identity-floor.md`](2026-04-20-commander-identity-floor.md), re-rebased 2026-04-26).

**Hybrid topology.**

Hybrids in this game are **within-civ tower merges along the tier ladder** plus **cross-T4-demigod Fusion into named Gods**. Specifically:

- **T1+T1 → T2, T2+T2 → T3** are standard within-civ tower promotions. 18 T1-T3 towers total (6 per civ).
- **T3 → T4 Demigod/Hero** is a Tribute-unlocked promotion (not Divinity-gated). 18 T4 Demigods & Heroes total (6 per civ) — all culturally-native mythic/legendary figures (Achilles, High Priest-King, Björn Ironside, etc.).
- **T4 + T4 → God** (**Fusion**) is the endgame differentiator. **9 Gods, 3 per civ, via 9 locked 2-Demigod recipes** (Zeus = Hercules + Jason; Odin = Harald Bluetooth + Leif Erikson; etc.). The two source Demigods are **consumed** into one board slot. Gods are the **only 2-type damage sources** in the game, inheriting both source attack types ([`decisions/2026-04-26-attack-type-mapping.md`](2026-04-26-attack-type-mapping.md)). This is the trailer beat.
- **Cross-civ hybridization is parked** as post-launch **"Foresight coin"** (Follow-up #7) — a future mechanic that may allow a Greek commander to reach an Aztec tower. Not launch scope.

**Why this frame wins.**

Three delighters, in order:

1. **Civilization-persistence callback.** A Greek match feels Greek from first wave through final Fusion — the T1 phalanx you placed in minute 1 has merged into a Hercules at T4 and fused into Zeus by minute 18, but every step in that chain reads as Greek. This is the core promise no existing Tower Wars game ships with. Validation bar at MVP: 50%+ of playtesters report the civilization-persistence feeling by end of T3 (`concept/phase-6.md §6.4`).
2. **"High-school recognizable" throughout.** Commanders, towers, units, Demigods, and Gods are all names and archetypes a player already has a mental model for. Lowers onboarding cost; raises memetic reach. Zeus trailer beat lands because Zeus is already pre-loaded in the audience's brain.
3. **Fusion endgame as earned climax.** The 9 locked Gods are reachable but not automatic — Divinity is 6-per-match capped, 2 to unlock the Fusion menu civ-wide, 1 per execute. Practical reach: 2-3 Gods per match. Validation bar at MVP: 30%+ of playtesters reach at least one Fusion per match — lower than civ-persistence because Fusion is the climax, not the baseline.

**What remains open** (tracked as ratification Follow-ups):

- Cultural-sensitivity pass — mandatory gate before content lock (#5).
- Patch-1 commanders per civ — deferred until post-playtest signal (#6).
- Foresight-coin cross-civ borrowing — parked post-launch (#7).
- PvE campaign + AGES + leveling/attributes — parked (#8).
- Non-boss enemy ontology — open (#9).
- Title lock — Phase 5 question; "Ash to Altar" is working-only (and no longer thematically load-bearing under the real-cultures frame).
- Myth-creature PvE boss roster — parked pending PvE scope (#3).

---

## 3x debug loop

**Loop 1 — aggressive critique.**

This one-pager is synthesis of already-decided work. The risk isn't content-wrong; it's formality-wrong. Specifically: (a) does the one-pager accidentally re-lock something as Phase 1 that was actually deferred (e.g., claiming Fusion is "locked" when the numeric balance pass is still [PROPOSAL])? (b) Does it overclaim Phase 1 closure when the cultural-sensitivity gate is still outstanding? (c) Does it ignore the `2026-04-24-phase-1-reopen` lesson — that Phase 1 can be reopened, so "exit" is provisional? (d) Does the "Why this frame wins" section read as marketing copy rather than design reasoning?

**Loop 2 — steelman.**

(a) The content-vs-numbers distinction is preserved: civs, commanders, towers, units, Demigods, Gods, recipes are **locked as content skeleton**; all numbers remain [PROPOSAL] per 2026-04-25 Follow-up #13. The one-pager makes this explicit by deferring validation thresholds to phase-6 §6.4 rather than restating them. (b) Cultural-sensitivity is flagged in the "What remains open" list and in the World section — not buried. Phase 1 exit doesn't require cultural-sensitivity completion; it requires that the frame *admits* cultural-sensitivity as a gate, which it does. (c) The 2026-04-24 reopen precedent is inherited: this entry is Reversibility **Easy** — reversal = reopen Phase 1 via a dated entry, same mechanism already used once. (d) "Why this frame wins" is design reasoning tied to validation bars, not marketing — each delighter has a measurable MVP threshold.

**Loop 3 — synthesis.**

File as-written. The one-pager is a formal capture, not a new decision. It closes Follow-up #11 and lets downstream phases reference a single Phase-1-exit artifact rather than chasing the ratification decision + the cascade + the re-rebases. No new constraints introduced. No numbers locked. Cultural-sensitivity gate preserved. Reopen mechanism preserved.

---

## Alternatives considered

- **A — No formal one-pager; Phase 1 exit is implicit via the ratification + cascade.** Why not: the 2026-04-25 ratification Follow-up #11 explicitly owes the artifact. Implicit closure leaves downstream phases chasing multiple decision entries to understand "what is Phase 1?" — a rubric-failure mode the one-pager exists to prevent.
- **B — Rewrite `concept/phase-1.md` itself as the one-pager.** Why not: `concept/phase-1.md §1.1-1.5` is already a clean real-cultures-frame write-up (as of 2026-04-26 cascade). Rewriting it again risks losing the target-player / core-promise / success-criteria structure that Phase 2+ already points at. The decision entry is the right vehicle because it's a formal capture, not an in-place rewrite.
- **C — Defer until after stages stub-amendments and CONCEPT-GAPS audit.** Why not: stages and CONCEPT-GAPS are downstream consumers; they benefit from having a single Phase-1-exit artifact to cite. Filing the one-pager first unblocks the rest of the session's autonomy queue.

---

## Reason chosen

Option **A (file formal one-pager as decision entry)** because Follow-up #11 directly names this deliverable, because the cascade already landed the substantive work and the only missing artifact is the formal capture, and because downstream phases gain a single citation target for "what Phase 1 ratified."

---

## Reversibility note

**Easy.** Reversal = reopen Phase 1 via a dated `decisions/<YYYY-MM-DD>-phase-1-reopen-<topic>.md` entry, same mechanism used for the 2026-04-24 reopen. This one-pager does not lock anything that wasn't already locked by the 2026-04-25 ratification + 2026-04-26 cascade — it formalizes, it does not constrain.

---

## Follow-ups

- Bump `CASCADE.md` v0.22 → v0.23 with Phase 1 status **Exited** + new decisions-table row.
- Annotate `PROGRESS.md` session-log with Follow-up #11 CLOSED.
- Downstream: stages `01/04/05/06` stub-amendments can now cite this one-pager as their Phase-1 reference.
- Residual Phase 2 bookkeeping (§2.3 "Content explosion" + "Lineage balance" still reference the superseded 3/3/3 + 5→3 lineage shapes) flagged as a separate sub-task — small in-line rewrite with an amendment banner, not a Phase 2 reopen.
- Cultural-sensitivity pass (Follow-up #5) remains a hard gate before content-lock. This one-pager does not and cannot substitute.
