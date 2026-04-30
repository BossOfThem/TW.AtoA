# Decision — Prototype reverts to port-source under paid-EA single-product (re-supersedes 2026-05-07 framing)

**Date:** 2026-04-29
**Status:** Accepted
**Reversibility:** Medium
**Affects:** [`decisions/2026-04-19-design-prototype-scope.md`](2026-04-19-design-prototype-scope.md) (clarifies disposition under post-supersession arc), [`decisions/2026-05-07-atoa-shippable-mtm-successor-pivot.md`](2026-05-07-atoa-shippable-mtm-successor-pivot.md) (which has itself moved to **Superseded**), CLAUDE.md "No code yet" clause, [`concept/phase-5.md`](../concept/phase-5.md) build-order, [`concept/PROJECT-ARC.md`](../concept/PROJECT-ARC.md) Phase B item B.5

---

## Decision

The HTML prototype's preserved 50-55% deliverable-logic (per the swarm's reconciled HTML preserve number; SYNTHESIS.md §"Reconciled HTML preserve number") **ports across to the engine paid-EA build as port-source**, not as a free Steam SKU. The 2026-05-07 pivot's framing — that the prototype graduates to "shippable Product 1, free on Steam" — is voided by the supersession of that pivot. The original 2026-04-19 throwaway-with-findings-port framing stands, with one update: the **port grain rises from "findings only" to "deliverable-logic"** because subsequent design work (commander R1-R5 / per-tower R1-RN / per-civ R1-RN / Fusion-numerics / attack-type / R11 wave-variance / mobile unit control / enemy direction / economy / monetization) has produced enough machine-portable substrate that the prototype's preserved logic represents real engine-ready content, not just findings.

**The prototype is no longer throwaway, no longer a shippable product. It is a port-source artifact.** It is preserved on the working tree as living documentation of the design substrate it implements; it is neither extended toward a Steam release nor archived to `_archive/` until the engine port consumes its load-bearing logic.

## Context

The 2026-04-19 decision framed `prototype/` as throwaway with findings-only port. The 2026-05-07 pivot tried to promote it to free Product 1 on Steam. The 2026-04-28 supersession (Accepted 2026-04-29) rejected the two-product framing in favor of paid Early Access single-product, leaving the prototype's role mid-cascade between three options: (a) shippable free SKU [voided by supersession], (b) throwaway with findings-only port [original framing], (c) port-source for engine work [implied by supersession but not explicitly resolved].

This decision resolves to (c). The reasoning lives in `concept/atoa-vs-mtm/SYNTHESIS.md` §"Reconciled HTML preserve number" — ~50-55% of the prototype's deliverable-logic (math derivations, balance numbers, R30-boss-clear validation, Fusion-numerics, commander effect-type ladders, attack-type RPS table, economy formulas, mode-of-play loop logic) is engine-substrate-portable and represents real value to the paid-EA build. Treating it as throwaway-with-findings-only would discard that value; treating it as a Steam-shippable SKU would re-introduce the two-product framing the supersession rejected.

## Alternatives considered

- **Option A — Restore throwaway-with-findings-only (2026-04-19 verbatim).** Cleanest against the 2026-05-07 pivot but discards the ~50-55% deliverable-logic that has accreted under subsequent design work. Not chosen.
- **Option B — Hold 2026-05-07 free-on-Steam framing despite supersession.** Internally contradictory with the supersession Accepted 2026-04-29. Not chosen.
- **Option C — Port-source under paid-EA (chosen).** Prototype preserved on tree; deliverable-logic ports forward into engine paid-EA build during Phase E (PROJECT-ARC.md §5); no Steam SKU; no archive yet.

## Reason chosen

3x debug loop synthesis:

- **Loop 1 (critique):** Port-source framing risks a third drift — extending the prototype indefinitely past its port window, dragging logic that the engine version diverges from. Risks a residual "is this still shippable?" question every time the prototype is touched. Risks porting code rather than logic, mistaking the artifact for the substrate.
- **Loop 2 (steelman):** The risks Loop 1 names are real but procedural rather than structural. The original 2026-04-19 framing already established findings-port discipline; the upgrade to "deliverable-logic" port grain doesn't change what is portable, only formalizes that more of it now exists. The "is this still shippable?" question is closed by this decision and by the supersession itself — neither permits a free Steam SKU. The port-code-not-logic risk is addressed by Phase E work item E.3 (PROJECT-ARC.md §5): "Port the prototype's preserved 50-55% deliverable-logic into engine substrate. Math/balance/derivation work transfers across substrates; rendering/transport/UI rebuilds." This is logic-port discipline by name.
- **Loop 3 (synthesis):** Port-source framing is the cleanest fit for current state. Adopt with three guardrails: (1) prototype is not extended toward Steam-shippable polish; (2) deliverable-logic is the port grain, not literal code; (3) archive trigger is engine-port completion (Phase E exit), not a calendar date.

## Reversibility note

**Medium.** Reversing this decision would mean either restoring the 2026-05-07 free-Steam framing (which would also require reversing the 2026-04-28 supersession — Hard cascade impact) or fully archiving the prototype now (which would lose easy access to its deliverable-logic during Phase E porting — recoverable via git but operationally clumsy). The decision can be evolved at Phase E exit when archive trigger fires.

## Follow-ups

- Phase E item E.3 (PROJECT-ARC.md §5): execute the port during engine build arc.
- At Phase E exit, file an archive decision moving `prototype/` to `prototype/_archive/`.
- Two prototype findings still queued (HANDOFF.md §"Two prototype findings still queued") — `prototype/index.html:3310` ReferenceError + `prototype/index.html:495,507,513` retired-ages copy — are deprioritized; they're patchable if the prototype is touched during port work but are not blocking.
- CLAUDE.md "No code yet" clause updates separately under PROJECT-ARC.md §5 Phase B item B.7.
