# Decision — Ash to Altar shippable HTML/app + Mud to Myth engine successor (product-shape pivot)

**Date:** 2026-05-07
**Status:** Superseded by [`2026-04-28-paid-ea-single-product-supersedes-pivot.md`](2026-04-28-paid-ea-single-product-supersedes-pivot.md) (Accepted 2026-04-29)
**Reversibility:** Hard
**Affects:** CONCEPT.md (hub product framing + non-negotiables), [`concept/phase-1.md`](../concept/phase-1.md) (vision/promise), [`concept/phase-4.md`](../concept/phase-4.md) §4.8 (exit-gate items #9/#10 reframe), [`concept/phase-5.md`](../concept/phase-5.md) (build order + engine-lock semantics), [`concept/phase-6.md`](../concept/phase-6.md) (validation against shipped product, not engine MVP), [`decisions/2026-04-19-design-prototype-scope.md`](2026-04-19-design-prototype-scope.md) (supersedes the "throwaway" framing), monetization-cascade docs (free-on-Steam reframe), §4.8 monetization ratification

---

## Decision

The HTML/JS build under `prototype/` is **promoted from throwaway design-prototype to shippable Product 1**. It will be developed to feature-complete, art-complete, UI-polished state and shipped **free on Steam** as **Ash to Altar** — a complete mirror of the entire concept cascade, playable end-to-end. The engine-native version is **Product 2 — Mud to Myth**, a successor build that replicates AtoA's proven design in a real engine (Godot 4 / Unity / Unreal — engine lock decision deferred to Product 2's own Phase-5 gate). MtM is the premium commercial product; AtoA is the free public artifact + de-risking proof-of-concept.

This pivots the project from a **single-product engine-build trajectory** to a **two-product sequenced trajectory**: AtoA ships first as the free complete game, MtM ships second as the engine-native premium replication.

## Context

PM raised on 2026-05-07 that the current HTML prototype, despite the Phase-4 exit-gate item #6 (Fusion-numerics) closing cleanly, "does not appear complete to me as a gamer — this is not something fun that I can play and really test out the complete scope of the project, all the way to where we work on the img/concept for every aspect and UI touch up." The concept cascade has reached a state where the design is structurally complete (9 of 11 Phase-4 exit-gate items closed), but the **playable artifact** has not. PM's stated goal: ship a complete free Steam product that proves the concept end-to-end, then build the premium engine version on top of that proof.

This reframes a foundational assumption baked in since [`2026-04-19-design-prototype-scope.md`](2026-04-19-design-prototype-scope.md): that HTML is throwaway and the engine build is the Product. PM is rejecting that framing. The HTML build IS the product (Product 1), and the engine build is a successor (Product 2).

The framing also resolves a tension that's been latent in the cascade: "Go big at launch" (CONCEPT.md non-negotiable, [`phase-7.md §7.4`](../concept/phase-7.md#74-notes-to-future-self)) requires shipping the full content skeleton. Doing that as a first-time engine project is high-risk. Doing it in HTML first — where iteration is cheap, no engine-lock cost, no platform porting — and *then* replicating in engine, de-risks the engine project enormously. MtM's Phase-5 begins with a fully-validated playable spec.

## Alternatives considered

- **Option A — Hold current trajectory: ship engine version as the product, HTML stays throwaway.** Lowest scope change. But requires engine lock + engine-build skill from cold. Rejects PM's stated 2026-05-07 product-shape goal. Not chosen.
- **Option B — Ship HTML *as* the only product, abandon engine version.** Avoids the two-product split. But forfeits the premium commercial outcome PM has consistently pointed at (engine version with art/feel/polish that justifies a price tag). Caps the project's commercial ceiling. Not chosen.
- **Option C — Two-product sequence: AtoA (HTML, free, Steam) → Mud to Myth (engine, premium, successor) (chosen).** Ships the proof first, builds the premium on the proof. Honors "Go big at launch" by treating AtoA's launch *as* the big launch (full content skeleton, free, accessible). MtM becomes a quality/feel/polish play, not a from-scratch design+engineering bet.

## Reason chosen

3x debug loop synthesis:

- **Loop 1 (aggressive critique):** Two-product split doubles surface area. Risk that AtoA ships, gets lukewarm reception, and MtM never gets funded. Risk that "free on Steam" misframes the product (Steam free games are often perceived as low-effort; quality bar must clear that perception). Risk that HTML hits a fun-ceiling that no amount of polish can lift — that a tower wars game *needs* engine-grade feel (tower placement haptics, projectile arcs, particle response, audio mix) to be fun, and HTML structurally cannot deliver that. Risk that monetization decisions ratified for the engine product (cosmetic-only IAP, no pay-to-win) become moot for AtoA-as-free, requiring rework. Risk that "complete mirror" scope is enormous — every commander, every civ, every tower/unit/Fusion, every mode (6 launch modes), every UI surface, every art piece, every audio cue — at HTML quality, this could be 12-18 months solo. Risk of the trap pattern: AtoA absorbs all attention, MtM never starts.
- **Loop 2 (steelman):** Critique overweights the "fun ceiling" concern — tower wars is one of the few subgenres where HTML/Canvas can deliver real fun (Bloons TD, Kingdom Rush web, Cursed Treasure all proved this). The genre's feel is *strategic*, not *kinesthetic*. Critique also misses that AtoA-free is not a commercial bet — it's a marketing+validation artifact. Free Steam release with full content is the cheapest possible way to (a) get player feedback at scale, (b) build a wishlist for MtM, (c) prove the design works before spending engine-engineering budget. The "two-product" surface-area concern is real but mitigated by the fact that MtM doesn't *design* anything new — it *replicates* AtoA's proven design. MtM's Phase 1-4 is essentially copy-from-AtoA; only Phase 5 (engine implementation) is fresh work. That's a much cheaper second product than a from-scratch one. Monetization rework is real but small: AtoA gets a free-with-no-IAP model (clean), MtM keeps the cosmetic-only premium model (existing ratification holds).
- **Loop 3 (synthesis):** Proceed with five guardrails:
  1. **Scope-fence AtoA explicitly**: feature-complete = full launch skeleton (3 civs × full ladder × 9 Fusion Gods × 3 commanders × 6 launch modes) at HTML-deliverable quality. NOT engine-grade feel. The bar is "a gamer can play through and feel the design works" not "this rivals engine games on feel."
  2. **Lock MtM as the premium successor early** — file a successor-charter decision now (separate doc) so MtM doesn't drift into vapor.
  3. **Reuse, don't re-design**: MtM's Phase 1-4 inherits from AtoA's ratified cascade verbatim. Only Phase 5 (engine) and any feel-specific Phase 6 work is fresh.
  4. **Free-on-Steam monetization for AtoA = truly free, no IAP**, to maximize wishlist conversion to MtM. Existing cosmetic-only monetization ratification migrates to MtM unchanged.
  5. **Engine-lock decision (Phase-4 exit-gate item #9) defers to MtM's own Phase-4 exit gate** — current Phase 4 exit-gate restructures to remove #9 from AtoA's blocker list. AtoA's "engine" is HTML/JS/Canvas (already in use). Item #10 (Art director) becomes an AtoA decision (HTML art direction) AND an MtM decision (engine art direction) — split, not deferred.

## Resolution of the four PM-decisional forks

- **Fork A — Monetization on AtoA:** **Truly free, no IAP, no cosmetics, no battle pass.** Maximize accessibility and wishlist conversion. Cosmetic-only premium model migrates intact to MtM.
- **Fork B — Scope of "complete":** **Full launch skeleton.** 3 civs (Greek/Aztec/Norse), full tower/unit/Demigod/God ladder per civ, all 9 Fusion recipes, 3 launch commanders (Leonidas/Montezuma II/Ragnar Lothbrok), all 6 launch modes (Solo Campaign / Horde-A / Horde-B / PvE-MP / PvP-IW / PvP-Maze), full first-run UX, full UI polish, full art coverage at HTML-deliverable quality bar. PvP networking is in-scope for AtoA (Steam supports it via Steamworks).
- **Fork C — Timeline shape:** **Sequential, not parallel.** AtoA ships first. MtM Phase-1 kickoff begins after AtoA Steam launch. Avoids the trap of half-built AtoA + half-built MtM. Sequential also means MtM benefits from real player data from AtoA's release.
- **Fork D — "Mud to Myth" naming:** **Placeholder, not [LOCKED].** Treats it under §5.4 placeholder discipline. Both names ("Ash to Altar" and "Mud to Myth") are evocative, fit the alliterative pair pattern, and capture the mortal→divine arc theme. Lock both at Phase-5 of their respective product cascades, not now.

## Reversibility note

**Hard.** This is a top-of-cascade product-shape decision that touches Phase 1 vision, Phase 4 exit-gate composition, Phase 5 build-order semantics, Phase 6 validation framing, monetization ratifications, and the foundational [`2026-04-19-design-prototype-scope.md`](2026-04-19-design-prototype-scope.md) decision. Reversal would require:

- Reverting CONCEPT.md hub framing.
- Reverting Phase 4 exit-gate restructure (re-adding #9 engine-lock as AtoA blocker).
- Re-deleting `prototype/` if AtoA work has materially advanced.
- Re-ratifying monetization for engine-only product.
- Discarding any AtoA-specific art/UI/UX work that doesn't port cleanly to engine.

Cost of reversal scales with how far AtoA work has progressed. **Decision should be confirmed with high conviction.** Proposing-then-ratifying flow with explicit PM sign-off before any spine-doc edits begin.

## Follow-ups (cascade-restructure work, sequenced)

This decision authorizes — but does not perform — the following spine-doc cascade. Each item is its own work session, ratified individually:

1. **Supersede [`2026-04-19-design-prototype-scope.md`](2026-04-19-design-prototype-scope.md)** with a new decision marking it Superseded, pointing to this doc.
2. **CONCEPT.md hub:** rewrite vision line + add two-product framing block + Phase index annotation that AtoA = HTML Product 1, MtM = engine Product 2.
3. **Phase 1 ([`concept/phase-1.md`](../concept/phase-1.md)):** vision/promise reframed as two-product arc.
4. **Phase 4 §4.8 exit-gate restructure:** item #9 (Engine lock) moves to MtM's future Phase-4. Item #10 (Art director) splits into #10a (AtoA art direction — HTML deliverable) and #10b (MtM art direction — engine deliverable). AtoA's Phase-4 exit gate becomes 10 items (1-8 closed + 10a remaining + 11 closed). MtM's Phase-4 inherits from AtoA's at start.
5. **Phase 5 ([`concept/phase-5.md`](../concept/phase-5.md)):** rewrite build-order to AtoA-first sequence; engine-lock content migrates to a new MtM-Phase-5 stub.
6. **Phase 6 ([`concept/phase-6.md`](../concept/phase-6.md)):** validation MVP becomes AtoA Steam release; metrics include wishlist conversion to MtM.
7. **Monetization ratification ([`decisions/2026-05-06-monetization-specifics-ratification.md`](2026-05-06-monetization-specifics-ratification.md)):** add scope-amendment note that the ratified model applies to MtM; AtoA is free-no-IAP.
8. **Charter MtM as a tracked successor product**: file `decisions/2026-05-07-mtm-successor-charter.md` capturing inheritance rules (Phase 1-4 = AtoA verbatim; only Phase 5+ is fresh) + Phase-4-of-MtM kickoff trigger (post-AtoA Steam launch).
9. **CASCADE.md restructure:** add "Product" column (AtoA / MtM / Both) to Phase index; current work pointer reflects AtoA Phase-4 close + AtoA Phase-5 prep.
10. **Update CLAUDE.md "No code yet" section:** the prototype exception broadens to "AtoA build" — code-writing is now permitted within `prototype/` (or rename to `atoa/`) for shippable-product work, governed by AtoA's own Phase-5 gate, not the engine Phase-5 gate.

## Cross-arc citation manifest

This decision relates to or affects:

- [`decisions/2026-04-19-design-prototype-scope.md`](2026-04-19-design-prototype-scope.md) — superseded.
- [`decisions/2026-04-25-q2-real-cultures-direction-ratified.md`](2026-04-25-q2-real-cultures-direction-ratified.md) — content unchanged; applies to both products.
- [`decisions/2026-05-06-monetization-specifics-ratification.md`](2026-05-06-monetization-specifics-ratification.md) — applies to MtM only (scope amendment in Follow-up #7).
- [`decisions/2026-05-06-fusion-numerics-balance-pass-ratification.md`](2026-05-06-fusion-numerics-balance-pass-ratification.md) — applies to both products.
- [`decisions/2026-05-06-economy-paper-balance-ratification.md`](2026-05-06-economy-paper-balance-ratification.md) — applies to both products.
- [`decisions/2026-05-06-cultural-sensitivity-phase-4-exit-gate-ratification.md`](2026-05-06-cultural-sensitivity-phase-4-exit-gate-ratification.md) — applies to both products.

All Phase-1-through-Phase-4 design ratifications transfer verbatim to MtM at MtM's own Phase-1 kickoff. MtM does not re-litigate concept; it inherits.
