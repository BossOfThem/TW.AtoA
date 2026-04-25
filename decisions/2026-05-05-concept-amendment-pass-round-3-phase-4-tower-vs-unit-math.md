# Decision — CONCEPT amendment pass Round 3: phase-4 §4.10 Tower-vs-Unit math NEW (+ §4.11 Numbers floor placeholder)

**Date:** 2026-05-05
**Status:** Accepted
**Reversibility:** Medium
**Affects:** [`concept/phase-4.md`](../concept/phase-4.md) (new §4.10, new §4.11 placeholder)

---

## Decision

Round 3 of the 7-round CONCEPT.md amendment pass per [`decisions/2026-05-05-concept-amendment-pass-scope.md`](2026-05-05-concept-amendment-pass-scope.md). **`phase-4.md §4.10 NEW Tower-vs-Unit math`** added between §4.9 and §4.8 (exit condition), absorbing the 2026-05-04 Balance-pass #1 conceptual-frame ratification + 2026-05-04 Round 12 (s)-extension. §4.10 is organized into 9 sub-sections:

- §4.10.1 Variable nomenclature (table of (a)–(r) + extension (s) — 18 first-class variables).
- §4.10.2 Master damage equation (DPS × engagement-time integral × matchup × passives × status, with global (s) outside the sum).
- §4.10.3 Round-slot typology (7 slot types + R-assignments across the 30-round arc; R15 promoted Elite→ +1 Divinity per Round-10 amendment).
- §4.10.4 (k) single-axis compounding rule + PvP-no-(k) note + tie-break HP-only escalation cross-link.
- §4.10.5 Skill-bar axes (3 axes — matchup / placement / uptime; signature ability excluded from uptime).
- §4.10.6 Sell-refund schedule (4-step + T4 cap + (k) coupling).
- §4.10.7 Tower target-priority + Universal aux slot cross-link.
- §4.10.8 Boss / Elite reward shape (incorporates 2026-05-05 Round 10 Divinity-source amendment: R15 0→1 Divinity, R30 floor 1 + match-completion 1).
- §4.10.9 Engine-port discipline note (1:1 Godot 4 translation).

**`phase-4.md §4.11 NEW Numbers floor`** seeded as a placeholder section listing all 8 source numbers-phase decisions (Rounds 1-2-3-4-5-6-8-9) with a "Round 4 of amendment pass populates this" note. Round 4 will replace the placeholder body with the actual magnitudes.

§4.10 cross-references resolve forward to §4.11 (numbers) and §4.6a (auxiliary economy). §4.6a forward-anchor lands empty until Round 5; §4.11 lands empty until Round 4.

## Context

Pre-amendment, `phase-4.md` had no Tower-vs-Unit math § at all. The 17-item conceptual frame + master equation + (k) single-axis rule + sell-refund + targeting + slot typology + skill-bar axes were all locked on 2026-05-04 (Balance-pass #1) but lived only in the decision file. Round 12 same-day added extension (s) to the frame as first-class. Round-3 of the amendment pass binds all of this into a citable spine surface so every future authoring sub-pass can reference §4.10.x anchors directly.

Inserting §4.10 + §4.11 *between* §4.9 (save model) and §4.8 (exit condition) preserves the existing §-numbering (4.1 → 4.2 → 4.3 → 4.4 → 4.4a → 4.5 → 4.6 → 4.7 → 4.9 → 4.8) and lets §4.8 remain the natural visual end-cap. §4.10 / §4.11 numbering follows the §4.9 numerical pattern (next-after-the-highest, with §4.8 as a tail rather than a sequential anchor). This is the same logic that landed §4.4a between §4.4 and §4.5 in the 2026-04-27 commander-as-summoned-ability-avatar amendment.

## Alternatives considered

- **Option A — Insert §4.10 inside §4.6 economy.** Merge Tower-vs-Unit math into the existing §4.6 (currency + economy). Rejected: §4.6 is about *currencies* (Tribute, Divinity, refund schedule); §4.10 is about *combat math*. Different surfaces. The shared overlap (sell refund + Tribute reward shape) gets cross-linked, not merged.
- **Option B — Place §4.10 after §4.8 (exit condition) at the doc tail.** Rejected: the exit condition is the natural visual end-cap of phase-4. Putting normative spec content *after* the exit condition reads as appendix-level afterthought, undermining its load-bearing role.
- **Option C — Insert §4.10 + §4.11 between §4.9 and §4.8 (chosen).** Preserves exit-condition tail; preserves §4.4a precedent; gives §4.10 / §4.11 enough visual weight to read as first-class spec.

## Reason chosen

Option C matches the 2026-04-27 §4.4a precedent and preserves the "exit condition is the visual tail" convention. §4.10's 9 sub-sections (~150 lines) earn placement near the back of the doc — they're the densest spec content in phase-4.

The §4.11 placeholder is intentional: the Round 4 amendment will land specific magnitudes, and seeding the §4.11 anchor in Round 3 means §4.10 can forward-reference §4.11 cleanly even before Round 4 commits. Forward-anchor stability is the consolidation premise of the entire amendment pass.

The (s) extension is folded into §4.10.1 as a first-class variable rather than as a Round-12 addendum — this matches the 2026-05-04 Round 12 ratification's "first-class multiplicative" framing and avoids the future reader having to track a two-stage frame.

## Reversibility note

**Medium.** Reverting §4.10 means deleting ~150 lines and updating cross-references in §4.6 + §4.6a + §4.11 + §3.6 (where the table forward-references §4.10 / §4.11). The conceptual frame itself stays Accepted regardless — this round binds the *display*, not the *decisions*.

## Follow-ups

- **Round 4** — populate §4.11 Numbers floor body with HP curve / (k) exponents / Tribute yield / speed / DPS ladder / commander magnitudes / per-mode tuning. Replaces the placeholder body added this round.
- **Round 5** — §4.6a Auxiliary economy NEW; §4.10.1 (s) cross-reference resolves once §4.6a anchor lands.
- **Round 6** — §4.10.5 skill-bar axes cross-references to phase-6 telemetry definitions; lands once phase-6 §x telemetry surface authored.
- **Per-tower authoring sub-pass** (post-amendment-pass) consumes §4.10 as the spec floor and binds per-tower (cd / range / attack-type / status-proc) variance.
- **Per-commander authoring sub-pass** (post-amendment-pass) consumes §4.10.1 (h) variable + §4.11 magnitudes to bind effect-type variants (control / summon / economy beyond Round-6 damage-floor).
