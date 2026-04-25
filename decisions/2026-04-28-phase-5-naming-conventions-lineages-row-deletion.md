# Decision — §5.4 naming conventions: delete Lineages row, add Civilizations row

**Date:** 2026-04-28
**Status:** Accepted
**Reversibility:** Easy
**Affects:** [`concept/phase-5.md §5.4`](../concept/phase-5.md#54-naming-conventions-locked-at-phase-5), [`CONCEPT.md`](../CONCEPT.md) (mirrored §5.4 block), [`CASCADE.md`](../CASCADE.md) decisions table, [`CASCADE-history.md`](../CASCADE-history.md) (archive of superseded convention).

---

## Decision

Delete the **Lineages** naming-convention row from `concept/phase-5.md §5.4` and replace it with a **Civilizations** row. The Civilizations convention is "the culture names itself" — real-culture proper nouns (Greek / Aztec / Norse at launch; expansions follow the same pattern). No invented placeholders. No one-syllable-kenning rule. The original Lineages convention text (Sinew / Ember / Forge / Crown / Veil pattern) is archived verbatim in `CASCADE-history.md` for traceability. A dated amendment banner is added to the top of §5.4 citing this decision and Follow-up #10 lineage. No other §5.4 row is touched.

## Context

Follow-up #10 from [`decisions/2026-04-27-commander-as-summoned-ability-avatar.md`](2026-04-27-commander-as-summoned-ability-avatar.md) confirmed-in-principle that the Lineages naming convention was orphaned by the 2026-04-25 real-cultures ratification ([`decisions/2026-04-25-q2-real-cultures-direction-ratified.md`](2026-04-25-q2-real-cultures-direction-ratified.md)). The launch frame is three real cultures (Greek / Aztec / Norse), not five invented one-syllable lineages. The §5.4 Lineages row therefore documents a convention that no surviving design surface uses — and the row's continued presence on a [LOCKED] page risks future drafters generating Sinew/Ember-style names for new content. PM gave explicit "go" on this amendment at handoff (2026-04-27). Scope is narrow and pre-agreed: one row out, one row in, archived for traceability.

§5.4 is [LOCKED]; touching a locked surface warrants a dedicated decision entry and the 3x debug loop (below) per `CLAUDE.md` cascade discipline.

## Alternatives considered

- **Option A — leave Lineages row in place, add a Civilizations row alongside.** Preserves the historical convention inline. Rejected: keeps a dead naming rule on a [LOCKED] page; future drafters could read it as still-active and generate Sinew-style names; violates the "locked surfaces should reflect current truth" principle.
- **Option B — delete Lineages row, add no replacement.** Minimal touch. Rejected: leaves the cultural-naming convention undocumented on the locked surface, which is the very gap that Follow-up #10 surfaced. Civilizations *do* need a convention statement — "the culture names itself" is load-bearing for refusing invented placeholders during cultural-sensitivity pass (Follow-up #5).
- **Option C — delete Lineages row, add Civilizations row, archive Lineages convention to `CASCADE-history.md`.** *(Chosen.)* Locked surface reflects current truth; archive preserves traceability for any future archaeology; Civilizations convention is positively stated rather than implied.

## Reason chosen

3x debug loop (touches [LOCKED] surface):

**Loop 1 — aggressive critique.**
- *"Why archive at all? Just delete."* — Risk: a future session grepping for "Sinew" or "Ember" in decision-context-only will find nothing and won't know whether the term ever had standing. Archive is cheap insurance.
- *"'The culture names itself' is not really a naming convention — it's a sourcing rule."* — Fair, but §5.4 already mixes pattern-rules (Lineages: one-syllable kenning) with sourcing-rules (Heirlooms: mythic-fragment style). The row belongs.
- *"What if a post-launch civ wants an invented name?"* — Then a new decision reopens this row. The Civilizations convention as written is "real cultures at launch + expansions follow same pattern" — it constrains expansion to real cultures, which IS the design intent per the 2026-04-25 ratification.
- *"Won't this orphan in-prototype 'Sinew/Ember' artifacts?"* — Prototype is frozen pending reshape plan ratification (C7.a explicitly guts superseded primitives). No live conflict.
- *"Are we sure no other §5.4 row needs touching?"* — Commanders row already says "first-name + epithet" which fits Greek/Aztec/Norse (Leonidas / Moctezuma / Ragnar-style). Towers/Units row ("job titles") is neutral. Ages row ("Mudbrick Era" pattern) is neutral. Hybrids/Enemies/Heirlooms/Modes — neutral. Confirmed: only Lineages is dead.

**Loop 2 — steelman.** Loop 1 over-weighted the "sourcing-rule vs. pattern-rule" objection — §5.4 is openly mixed-domain, that's not a defect. The "what if post-launch wants invented" worry is also overweighted: the Civilizations convention as written *intentionally* gates that, which is a feature aligned with the 2026-04-25 hard-reversibility ratification, not a bug. Loop 1's strongest point is the audit-of-other-rows: confirming neutrality of the seven retained rows is the actual diligence work, and it passes cleanly.

**Loop 3 — synthesis.** Option C is the right call. The amendment is narrow, archive-preserving, and aligned with the 2026-04-25 hard ratification. The Civilizations row should be worded to (a) name the convention positively ("real-culture proper nouns; the culture names itself"), (b) explicitly forbid invented placeholders, and (c) state the launch roster + expansion rule so future drafters cannot drift. No other row is in scope.

## Reversibility note

**Easy.** To undo: restore the Lineages row text from `CASCADE-history.md`, remove the Civilizations row, remove the amendment banner, file a superseding decision. No code, no asset, no other-doc dependency exists on the Lineages convention (the prototype's residual Sinew/Ember strings are scheduled for removal under reshape-plan C7.a regardless). The Civilizations convention is referenced only by future drafters, not by any current artifact, so removing it would not orphan anything.

## Follow-ups

- **Execution sequence (this decision unblocks):**
  1. Edit `concept/phase-5.md §5.4` — delete Lineages row, add Civilizations row, prepend dated amendment banner.
  2. Mirror the same edit in the `CONCEPT.md` hub if §5.4 is duplicated there (per the §5.4 note "Duplicated in the CONCEPT.md hub for cross-reference; canonical location is here").
  3. Append archived Lineages convention text to `CASCADE-history.md` under an "Archived naming conventions" section.
  4. Add this decision as a new top row in `CASCADE.md` decisions table.
  5. Append `PROGRESS.md` session note (or amend most recent entry; doc-hygiene 3-most-recent rule).
  6. Commit + dual-push (session branch + `main`). Stop for PM review.
- **Closes Follow-up #10** from `decisions/2026-04-27-commander-as-summoned-ability-avatar.md`.
- **Does NOT close** any other Follow-up. Cultural-sensitivity pass (Follow-up #5), patch-1 commanders per civ (Follow-up #6), prototype reshape ratification — all remain open and gated.
- **Scope guard reminder:** any future request to touch another §5.4 row is out of scope for this decision and requires its own [LOCKED]-amendment entry.
