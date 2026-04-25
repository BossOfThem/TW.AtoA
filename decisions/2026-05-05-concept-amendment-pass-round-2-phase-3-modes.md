# Decision — CONCEPT amendment pass Round 2: phase-3 §3.6 mode roster expansion (5→6) + §3.4 / §3.8 cleanup

**Date:** 2026-05-05
**Status:** Accepted
**Reversibility:** Easy
**Affects:** [`concept/phase-3.md`](../concept/phase-3.md) §3.4, §3.6, §3.8

---

## Decision

Round 2 of the 7-round CONCEPT.md amendment pass per [`decisions/2026-05-05-concept-amendment-pass-scope.md`](2026-05-05-concept-amendment-pass-scope.md). **`phase-3.md §3.6` rewritten in-place** to absorb the 6-mode launch roster ratified across 2026-05-04 Rounds 7–12 + 2026-05-05 Round 8 per-mode-tuning + Horde-split. Mode roster:

1. Solo Campaign (single-lane, multi-mission saga; per-mission (k))
2. Horde Co-op A — adjacent lanes with leak-bleed
3. Horde Co-op B — shared lane on ring-of-zones N-scaling map
4. PvE Multiplayer — 8 parallel lanes, last-alive
5. PvP Interest Wars Lane — Squadron-TD Send-for-Interest centerpiece, 20s rounds, 30-leak knockout, R31+ tie-break
6. PvP Maze Lane — Line-Tower-Wars-pattern A* maze on hex grid, Maze Stones, lives=10

§3.6 amendment includes: amendment banner citing the 6 source decisions; per-mode summary table (lane topology / player count / win condition / (k) gating / key auxiliary surface); universal aux-slot recap; per-mode lives declaration; post-launch expansion list; solo-promise audit (3 of 6 modes play solo; Solo Campaign carries the solo non-negotiable). §3.4 stale "Commander Hero Unit" sentence redacted with strikethrough + supersession pointer to §4.1 summoned-on-cast subsection (2026-04-27 supersession was already landed in §4.4 but the §3.4 transitive reference was missed). §3.8 exit-condition prose updated from "5 launch modes" to "6 launch modes (Solo Campaign / Horde-A / Horde-B / PvE-MP / PvP-IW / PvP-Maze)".

## Context

Pre-amendment, `phase-3.md §3.6` listed Solo Campaign / Solo Skirmish / Co-op Horde / Lane Wars 1v1 / Lane Wars 2v2 — a 5-mode roster from before the 2026-05-04 deep-dive arc. After 6 ratification rounds (2026-05-04 Rounds 6–12) + the Horde-split + PvE-MP add + PvP-Maze add + Lane-Wars-1v1/2v2 collapse into PvP-IW, the canonical launch roster is 6 first-class modes — but the spine doc still read as the old 5. Future authoring sub-passes citing modes would either:

- (a) cite outdated §3.6 prose and propagate the 5-mode error, or
- (b) cite each per-mode decision file individually (6 dated decision URLs) and lose §-anchor stability.

Round 2 closes that gap. The §3.6 rewrite is the canonical mode-roster anchor for the next ~6 months of authoring.

## Alternatives considered

- **Option A — Append-only (don't rewrite §3.6).** Add a new §3.6a "Mode roster amendment" subsection listing the 6 modes; leave §3.6's 5-item list intact for "history." Rejected: the §3.6 prose is *wrong*, not historical-and-still-true. Future readers would have to scan past the 5-item list to find the 6-item amendment. Comment-rot vector.
- **Option B — Replace + minimal table.** Replace the 5-item bullet list with a 6-item bullet list; no per-mode summary detail. Rejected: defeats the purpose of consolidation — every authoring sub-pass would still cite Round-7-through-Round-12 decision URLs to get topology / player count / win condition / aux surface. The per-mode table earns its lines back ~10x in citation savings.
- **Option C — Replace + summary table + cross-references (chosen).** Replace the 5-item list with a 6-row summary table (topology / count / win / (k) / aux), banner the amendment, cross-reference §4.6a + §4.11 forward-anchors, append universal-aux recap + per-mode lives declaration + post-launch expansion list + solo-promise audit. Forward-references to §4.6a / §4.11 land empty for Rounds 3-5 but become live anchors after Round 5 lands.

## Reason chosen

Option C is the only choice that pays off the consolidation premise. The summary table is the single biggest ROI in the amendment pass — a future reader asking "what's the win condition for PvP-IW?" gets one cell instead of a decision-file URL. The forward-references to §4.6a / §4.11 are intentional: they bind the §3.6 reader path to the new spine surfaces being authored across Rounds 3–5, and once those land the cross-link graph closes.

§3.4 redaction is technically a corollary turn under the 2026-04-27 supersession decision rather than under this Round 2 — but landing it here costs 2 lines and prevents a missed-redaction follow-up later.

§3.8 prose touch (5→6 modes) is one-line cleanup; not worth a separate round.

## Reversibility note

**Easy.** Reverting the §3.6 rewrite means re-pasting the 5-item bullet list from `git log` and dropping the new table. No magnitudes change. The 6-mode ratification stays Accepted regardless — this round is the *display* of those decisions, not the decisions themselves.

## Follow-ups

- **Round 3** — `phase-4.md §4.10` Tower-vs-Unit math NEW. Forward-anchored from §3.6 already (cross-references will resolve once §4.10 lands).
- **stages/02-mode-select.md** still says "Stub" — mode select stage docs are deferred to a separate Phase-C drill-down pass. Not in this amendment pass scope.
- **research/01-genre-pulse.md** referenced in §3.6 backing-research line — still "Stub." Deferred per Numbers-phase #13 backlog (research/06-tw-subgenres.md is the next research priority, not 01).
