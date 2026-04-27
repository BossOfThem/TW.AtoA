# 2026-05-06 — Cultural-sensitivity pass Phase-4-exit gate ratification

**Status:** Accepted
**Reversibility:** Hard (content-identity surface; reopens require Phase-2 / Follow-up #5 reissue with PM sign-off)
**Closes:** §4.8 exit-gate item #11

## Context

The 2026-04-25 Follow-up #5 cultural-sensitivity pass is a **mandatory gate before content lock** — external consultation for Aztec representation, 300-movie-ideology audit for Leonidas visual direction, TV-show-vs-history framing for Ragnar. Phase-4 exit threshold is **schedule-binding**, not pass-execution: Phase 4 closes if and only if every cascade touchpoint that downstream phases will lock content against has the gate inline as a hard pre-condition.

This is a single-doc audit-and-ratify. No new design surface is introduced; the gate body itself is locked at Follow-up #5 (2026-04-25). What this entry confirms: (a) gate scope is sufficiently bounded to be enforceable, (b) every place in the cascade that will perform content-lock cites the gate as a blocking pre-condition, (c) Phase-4-spec-level surfaces that already use placeholder-naming (Builder labels, "Divinity") flag the gate explicitly.

## Decision

**The 2026-04-25 Follow-up #5 cultural-sensitivity pass is locked as a hard pre-content-lock gate, scheduled across Phases 5 / 6 / 7. Phase 4 exits with the schedule binding; pass-execution sits in Phase 5 sprint pre-art-lock per `concept/phase-5.md §5.3` + §5.5 + `concept/phase-7.md §7.4`.**

## 3-check audit at zero cascade-violations

### Check 1 — Binding-point coverage across the cascade

The gate must be cited as a blocking pre-condition at every point the downstream cascade performs content-lock. Audit:

| Cascade point | Spine-doc citation | Pre-condition framing |
|---|---|---|
| Commander voice-line VO direction | `phase-4.md §4.1` line 28 | "subject to cultural-sensitivity pass" |
| Cast-emerge pose lock | `phase-4.md §4.1` cultural-sensitivity inheritance paragraph | "**No pose lock until the consultation pass closes**" |
| Builder unit civ-coded labels | `phase-4.md §4.4a` Visual row + Open list | three working labels gate on the pass; "rename allowed pre-content-lock" |
| Aztec Priest-Builder caste-accuracy | `phase-4.md §4.4a` flag | "rename pending consultation" |
| Norse Thrall Gang slavery framing | `phase-4.md §4.4a` flag | "flagged for review" |
| "Divinity" descriptive name | `phase-4.md §4.6` Open list | "§5.4 + Follow-up #5 cultural-sensitivity pass applies" |
| Phase-5 MVP content lock | `phase-5.md §5.5` | "**mandatory gate before any art lock**" |
| Phase-5 build sprint #2 (enemy roster) | `phase-5.md §5.6` build-order item 2 | "gates any Aztec myth-creature content lock" |
| Phase-5 build sprint #6 (solo campaign) | `phase-5.md §5.6` build-order item 6 | "full script under cultural-sensitivity-pass guardrails" |
| Phase-6 playtest exposure | `phase-6.md §6.5` | "mandatory gate **before** any playtest exposes" representation surfaces |
| Phase-6 validation framework | `phase-6.md §6.7` | "**cultural-sensitivity pass** is scheduled as a hard gate between MVP content-lock and any external playtest" |
| Phase-7 risk register | `phase-7.md §7.4` item 7 | "**MANDATORY GATE** before MVP content-lock" |
| Phase-7 success criteria | `phase-7.md §7.6` item 7 | "hard gate before content-lock" |

13 cascade touchpoints across 4 spine docs; every content-lock-adjacent surface cites the gate as blocking. **PASS.**

### Check 2 — Gate scope correctly bounded

The pass scope is enumerated at three named consultation requirements per Follow-up #5:

1. **Aztec representation** — external consultation; explicit boundaries cited at `phase-4.md §4.4a` (Priest-Builder caste-accuracy: "macehualtin commoners did Aztec construction, not priests") and `phase-5.md §5.6` build #2 (Aztec myth-creature content lock).
2. **Leonidas visual framing** — 300-movie-ideology audit; bounds the visual direction away from the film's pseudo-fascist iconographic conventions (oiled-abs glamorization / Persian-orientalism) toward Spartan-historical framing.
3. **Ragnar Lothbrok visual framing** — TV-show-vs-history framing audit; bounds the visual direction away from the History Channel show's compositing of multiple sagas into a single character (per `phase-4.md §4.7` historic match-arc table notes) toward source-text-aware framing.

The 2026-04-27 commander-as-summoned-ability-avatar 8-Q same-day amendment narrowed the Aztec scope explicitly: **Cortés OUT, Aztec pre-contact** — pre-contact Tenochtitlan civilization-on-its-own-terms; no conquest-narrative framing, no European-encounter perspective.

3 named consultation requirements, each with explicit boundaries; cumulative scope sufficient to gate the three commanders + the Builder caste-flag + the Aztec myth-creature roster. **PASS.**

### Check 3 — Hard-gate enforcement (blocking, not advisory)

The gate is positioned **before** content-lock at every reference, never **at** or **after** content-lock. Verified:

- `phase-5.md §5.5` art direction: "mandatory gate **before any art lock**"
- `phase-6.md §6.5`: "mandatory gate **before** any playtest exposes"
- `phase-6.md §6.7`: "scheduled as a hard gate **between** MVP content-lock **and** any external playtest"
- `phase-7.md §7.4` item 7: "**MANDATORY GATE before** MVP content-lock"
- `phase-4.md §4.1` cast-emerge pose: "**No pose lock until** the consultation pass closes"

No reference frames the pass as advisory, post-hoc, or skippable. Every reference is structured as blocking-with-no-bypass-condition. **PASS.**

## Reversibility classification

**Hard for gate body.** The gate's existence + scope + blocking-position is part of the project's content-identity surface (Phase-2 `CONCEPT.md §6.4` solo-first + respect-source-cultures pact). Reopening requires Phase-2 / Follow-up #5 reissue with PM sign-off — not a Phase-N-of-M routine adjustment.

**Easy for execution surface.** Choice of consultant(s), pass cadence within Phase-5 sprint, document format of the consultation deliverable, and exact pre-pass placeholder vocabulary are all PM-decisional Easy-class adjustments that do not reopen the gate ratification.

## Hard guards verified untouched verbatim

- §5.4 + §2.4a [LOCKED]
- 2026-04-25 content-skeleton names
- 2026-04-26 attack-type lock
- 2026-04-27 commander-as-summoned-ability-avatar lock + 8-Q amendment (Cortés OUT, Aztec pre-contact)
- §4.1 commander-as-summoned-ability-avatar
- §4.4a Builder excluded from §4.4 control model
- §4.7 Option C + R11 grammar
- Three-civ-three-equation-form fingerprint civ-neutral-by-construction
- 2026-04-25 Follow-up #5 gate body (read-only; this entry ratifies its scheduling, not its body)

## Spine-doc edits

- `concept/phase-4.md §4.8` — exit-gate item #11 ✅ ticked DONE with link-back to this decision.

## Phase 4 status post-ratification

**8 of 11 exit-gate items closed.** Remaining: #6 Fusion-numerics (multi-round; reserved for fresh window) / #9 Engine lock (Hard-class; reserved for fresh window) / #10 Art director (engaged or scoped).
