# Decision — Prototype `hybrid.pair` field is prototype-shape only (does not resolve CONCEPT §7.1 blocker #1)

**Date:** 2026-04-20
**Status:** Accepted (clarification; no new design commitment).
**Reversibility:** Easy (removing or re-shaping the `pair` field costs a single-file edit).
**Affects:** [`prototype/data/towers.json`](../prototype/data/towers.json) (`hybrid.pair` field documentation), [`prototype/PORT-NOTES.md`](../prototype/PORT-NOTES.md), [`CONCEPT.md`](../CONCEPT.md) §4.3 (hybrid system — unaffected; this entry explicitly does *not* resolve blocker #1), [`PROGRESS.md`](../PROGRESS.md) Step 1.5c.

Resolves: PROGRESS Step 1.5c (clarifying entry for `hybrid.pair` prototype-shape semantics).

---

## Decision

The `hybrid.pair` field in [`prototype/data/towers.json`](../prototype/data/towers.json) (currently `["sinew", "ember"]` for the Tank Corps hybrid) is **prototype-shape only**. It encodes *which two lineages this hybrid derives from* for the purpose of:

1. Displaying the hybrid's ancestry in the prototype's tower card / tooltip.
2. Enabling the port target (Godot `TowerData.tres` resource) to carry the same ancestry field.
3. Letting the prototype's adjacency logic (if ever wired) check whether a `sinew`-tower and an `ember`-tower are neighbors.

The field **does not**:

- Resolve, encode, or bias the hybrid *discovery* mechanic (CONCEPT §4.3 / §7.1 blocker #1 — still open, resolution-by-Phase-4-exit).
- Commit to "adjacency-threshold-duration" unlocks as the chosen discovery mechanic (§4.3 Option 1 "accept it").
- Commit to randomness (§4.3 Option 2) or knowledge-gating (§4.3 Option 3).
- Imply any specific age-unlock rule (the `Steamheart` age in §4.3's starter hybrid table is lineage-plus-age; the prototype's Tank Corps uses Primal-age stats for prototype simplicity).

The `pair` field is the *ancestry tag*, not the *discovery rule*. Discovery remains a Phase 4 OPEN BLOCKER.

## Context

PROGRESS Step 1.5c was carried forward from the 2026-04-19 cascade restructure as a small cleanup item: the prototype ships a `hybrid.pair` field that *looks like* a hybrid-unlock-rule commitment, and a reader of the prototype JSON could reasonably infer that the CONCEPT §4.3 hybrid discovery blocker is resolved (it isn't). The risk is cascade confusion: a downstream reader treats prototype shape as concept commitment.

This entry exists to state explicitly that the field is prototype-convenience, not a concept-level resolution. No CONCEPT.md amendment is needed — the purpose is to prevent future amendment drift in the wrong direction.

## Alternatives considered

- **Option A — Remove the `pair` field from `towers.json` entirely.** Rejected: the field is useful for prototype tooltip / ancestry display. Removing it loses prototype signal without gaining clarity. The confusion risk is addressable via documentation, not deletion.
- **Option B — Rename `pair` to `lineageAncestry` (more self-documenting).** Rejected: renaming costs a field-rename across prototype code for marginal clarity gain. A decision-log clarification is cheaper and achieves the same purpose.
- **Option C — Add inline comment to `towers.json` explaining the field's semantics.** Partially accepted: a comment in the `_comment` field at the top of `towers.json` would be a nice complement. This entry remains the authoritative clarification; the comment is a nicety, not a replacement.
- **Option D — (Chosen.) File a decision entry clarifying scope.** Names what the field is and isn't, cites CONCEPT §4.3 blocker #1 explicitly, keeps the prototype-shape stable.

## Reason chosen

No 3x debug loop — this is a clerical clarification with no design commitment to attack or steelman. The entry exists purely to prevent cascade confusion. Included in this sweep because (a) the 2026-04-20 batch is already amending prototype-adjacent concept territory (save model, audio, accessibility) and it is efficient to land the prototype clarification alongside; (b) PROGRESS Step 1.5c was the trailing unchecked pre-queue cleanup item.

## Reversibility note

**Easy.** Marking this entry Superseded leaves `towers.json` unchanged; the file's `pair` field is not created, destroyed, or modified by this entry. Superseding this entry and *then* rewriting the field's semantics (e.g., to encode a discovery rule) would require a new decision entry against CONCEPT §4.3 — i.e., actually resolving blocker #1, which is the proper path.

## Follow-ups

- **PROGRESS.md Step 1.5c** ticks complete with this entry.
- **Optional tiny nicety:** update `towers.json` `_comment` field to include "`pair` field = ancestry tag, not a discovery rule (see decisions/2026-04-20-prototype-hybrid-pair-shape.md)." Not blocking; not filed in this entry.
- **Still open (unchanged by this entry):** CONCEPT §4.3 / §7.1 blocker #1 — hybrid discovery mechanic (accept / randomness / gating). Resolution target: Phase 4 exit.
