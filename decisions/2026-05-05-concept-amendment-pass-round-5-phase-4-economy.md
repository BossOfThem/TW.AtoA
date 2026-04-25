# Decision — CONCEPT amendment pass Round 5: phase-4 §4.6 economy rewrite + §4.6a Auxiliary economy NEW

**Date:** 2026-05-05
**Status:** Accepted
**Reversibility:** Medium
**Affects:** [`concept/phase-4.md`](../concept/phase-4.md) §4.6 (rewrite), §4.6a (NEW)

---

## Decision

Round 5 of the 7-round CONCEPT.md amendment pass per [`decisions/2026-05-05-concept-amendment-pass-scope.md`](2026-05-05-concept-amendment-pass-scope.md). **`phase-4.md §4.6` rewritten in-place** to absorb 2026-05-05 Numbers-phase #13 Round 3 (Tribute economy + boss lumps) + Round 7 (aux costs) + Round 10 (Divinity 4-floor + 2-escalation source roster). **`§4.6a Auxiliary economy NEW`** authored as the consolidated home for the universal-aux-slot catalog + currency-budget audit + per-mode availability shape.

**§4.6 rewrite** drops the prior "every build touches an economy lineage" prose (was already invalidated by 2026-04-25 real-cultures ratification), the stale 5-bullet "open under the new shape" trailer (compressed into one sentence), and the placeholder Mythium subsection (replaced with explicit retirement note). Adds: Tribute curve binding to §4.11.3 anchors; Divinity 6-source table (4 floor + 2 escalation per R10 amendment) with PvP / co-op award-shape note; Mythium-retirement note pointing to the kill-only-currency lock + PvP-IW Send-for-Interest as the Squadron-TD shape preserved.

**§4.6a NEW** lands between §4.6 and §4.7. Three subsections:

- **Universal aux-slot catalog** — 7-row table (Damage Bonus / Economy Bonus / Tower-count expansion / Send-Creeps / Send-for-Interest / Call-for-Help / Maze Stone) with cost / effect / cap / mode-availability columns.
- **Currency-budget audit** — explicit max-aux + max-Fusion combinations against 6-cap; Tribute headroom check; combined per-tower expert stack 1.725× cross-link to §4.11.8 realized math.
- **Mode availability matrix pointer** — cross-link to §4.11.7 per-mode tuning rather than duplicating mode-by-mode optimization detail (deferred to per-mode authoring sub-pass).

§4.6a forward-anchor seeded in Round 3 (§4.10.1 (s) variable + §4.10.7 target-priority cross-link) now resolves live.

§4.6 "Open" trailer compressed to a single sentence to fit the 600-line phase-4 cap (post-rewrite phase-4 = 600 lines exactly; was 604 pre-trim).

## Context

Pre-amendment, `phase-4.md §4.6` was a 26-line subsection from the 2026-04-25 ratification — Tribute / Divinity locked in shape but with `[PROPOSAL]` magnitudes throughout, a still-live Mythium placeholder, and a 5-bullet "Open" trailer that pre-dated the entire 2026-05-05 Numbers-phase #13 arc. After R3 (yield curve + boss lumps locked), R7 (aux costs locked + (s) bound to 1.20), and R10 (4-floor + 2-escalation Divinity source roster locked), the §4.6 prose was 80% obsolete.

§4.6a did not exist. The 2026-05-05 R7 ratification authored the universal-aux-slot frame as a free-floating decision-file artifact; the Round 3 §4.10.1 cross-reference to (s) and §4.10.7 cross-reference to "Universal aux slot" forward-anchored to a §-surface that hadn't been authored yet. Round 5 lands that surface.

## Alternatives considered

- **Option A — Append-only §4.6a; leave §4.6 untouched.** Rejected: §4.6 prose contradicts the now-locked numbers (e.g., "Mythium time-based PvP-only worker income" directly conflicts with R3's kill-only-currency-across-all-modes lock). Future readers would have to scan past the contradicted prose.
- **Option B — Inline aux catalog into §4.6 (no §4.6a).** Rejected: §4.6 is currency-side (income / cap rules); §4.6a is spend-side (slot catalog). Different surfaces; merging them produces a ~70-line monolith and breaks the §4.10.7 / §4.10.1 forward-anchors that Round 3 already set.
- **Option C — Rewrite §4.6 + author §4.6a (chosen).** Currency-side / spend-side split mirrors §4.10 (frame) / §4.11 (numbers) split landed in Rounds 3-4. Mode-availability matrix stays inside §4.11.7 per-mode tuning rather than duplicating in §4.6a — single source of truth.

## Reason chosen

Option C is the only option that closes Round 3's forward-anchors cleanly and absorbs the R3 + R7 + R10 magnitudes without contradicting the prior §4.6 prose. The currency-side / spend-side split matches the §4.10 / §4.11 frame / numbers split, so the four sections form a consistent 2×2 grid (frame-currency = §4.6; numbers-currency = §4.6a; frame-combat = §4.10; numbers-combat = §4.11). This is the same pattern that landed §4.10 / §4.11 in Round 3.

The Mythium retirement note is the load-bearing prose change — without it, the next reader would chase a placeholder name that no longer exists in any locked decision. Explicit retirement (rather than silent deletion) lets a future reader who remembers Mythium from earlier docs trace the supersession in one hop.

## Reversibility note

**Medium.** Reverting §4.6 means re-pasting the 2026-04-25 prose from `git log` and dropping ~50 lines of new content. Reverting §4.6a means deleting the section and updating §4.10.1 / §4.10.7 cross-references back to the placeholder pointers. The R3 + R7 + R10 magnitudes themselves stay Accepted regardless — this round binds the *display*, not the *decisions*.

## Follow-ups

- **Round 6** — phase-4 §4.7 Round-11 mandate hook (skill-bar threshold integrity defense) + phase-6 skill-bar telemetry definitions (resolves §4.11.8 forward-anchor) + phase-7 §7.4 "Go big" non-negotiable.
- **Round 7** — Hub CONCEPT.md version bump + phase-3 / phase-4 / phase-6 / phase-7 index row touches + cascade-lint clean run + commit + dual-push + close arc.
- **Per-tower authoring sub-pass** consumes §4.6a Send-Creeps + Call-for-Help + Maze-Stone slot definitions for special-effect-tower variant authoring.
- **Per-mode authoring sub-pass** consumes §4.6a aux catalog + §4.11.7 availability matrix to bind per-mode optimization paths (e.g., Horde-B Tower-count-expansion-priority vs PvP-IW Send-for-Interest-rush).
- **Dual-push checkpoint** triggers after Round 5 per scope-decision queue (carries Rounds 4-5).
