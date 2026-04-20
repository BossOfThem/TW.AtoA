# Decision — Prototype visuals overhaul + insight layer

**Date:** 2026-04-20
**Status:** Accepted
**Reversibility:** Medium
**Affects:** prototype/index.html (rendering + insight code), prototype/data/enemies.json (archetype fields already present), PORT-NOTES.md

---

## Decision

Replace the prototype's circle-per-entity rendering with:

- **Archetype silhouettes** for enemies, keyed off `enemies.json[i].kind` (swarmer / infantry / heavy / ranged / elite / boss), each drawn from canvas primitives in `enemy.color` with `enemy.accent` outline.
- **Hex-and-glyph tower bodies** replacing the flat tower circle. Level-crown chevron stack above the hex; guest-owned towers keep the dashed border; colorblind letter label overlay.
- **Per-lineage projectile shapes** (Sinew dart, Ember spark+trail, Forge hex-bolt, Crown chevron-pair, Veil wavy-bezier, Hybrid two-color split).

Add an **insight layer**:
- Muzzle flash on shot creation (radial burst, 3-frame life).
- Floating damage numbers (white/gold/grey by magnitude, 30-frame rise-fade).
- Enemy status icons (slow / burn / marked) applied by lineage-specific tower hits; TTL-ticked; drawn as 6px icon-stack above HP bar.
- HP bar gains a **threat bar** below it: length ∝ `distance / pathLength`, pulses red inside the final 15%.
- Next-wave telegraph strip in the HUD preview slot, renders up-to-8 mini silhouettes + counts before Send-Wave.
- Combat feed DOM panel top-right: kill / leak / hybrid-unlock / upgrade / wave events, 4s fade (respects reduce-motion a11y option).

Co-op snapshot schema is extended **additively only** (enemies gain `kind/color/accent/label/ageIdx/statuses/dist`; shots gain `accent/lineage`). No match-logic changes. All numbers remain `[PROPOSAL]`.

## Context

Prototype data already carries per-tower glyph+color+accent and per-enemy color+accent+glyph+kind fields, but rendering pipeline ignored them — every entity drew as a colored circle. CONCEPT §2.2.7 commits the art direction as silhouette-forward; the prototype was silently violating its own spec. Meanwhile "what's actually happening mid-wave" was near-invisible: no damage feedback, no firing indication beyond a 1-frame shot segment, no next-wave preview, no leak history.

PM directive (2026-04-20): *"we can do better than this for the units enemies and provide more insight as to whats happening than circles now."* PM granted hyper-approve bypass for the 5-hour autonomous window.

## Alternatives considered

- **Option A — do nothing, wait for Godot port.** Cheapest. Rejected: the prototype is now the playtest surface (Step 10 pivot); playtesters cannot evaluate visual identity or moment-to-moment readability against placeholder circles. The whole point of pivoting to a concept-demo was to let PM + friend *feel* the game.
- **Option B — swap to image sprites.** Looks best. Rejected: art pipeline belongs to Phase 4 exit gate; sourcing/licensing/authoring sprites violates scope and introduces asset-management debt the prototype was designed to avoid.
- **Option C — canvas silhouettes from primitives + insight HUD.** (Chosen.) Uses data already present; zero new assets; preserves throwaway-prototype scope; everything ports to Godot `Polygon2D`/`Control` scenes cleanly (see PORT-NOTES additions).

## Reason chosen

**3x debug loop:**

- **Loop 1 — critique.** Hand-drawn canvas silhouettes will look worse than primitives — canvas isn't SVG and the bezier pen is crude. Adding floating damage numbers + feed + status icons + threat bar + telegraph simultaneously is a legibility pileup: the HUD becomes noisier than the game. Status-effect timing is a real game-logic change dressed as a "visual" — slow and burn now actually tick.
- **Loop 2 — steelman.** Silhouettes-from-primitives is not the target fidelity; it is the *spec vehicle*. The point is playtesters can tell a swarmer from a heavy at a glance without reading labels. HUD pileup is mitigated by the a11y reduce-motion toggle + threat-bar toggle and by the fact that the combat feed auto-prunes to 6 rows. Status effects are intentionally real: lineages were mechanically indistinguishable in prototype v1; giving Veil a slow, Ember a burn, and Forge a mark turns "color difference" into "felt difference" and lets playtesters answer the §6.2 secondary-question "which lineage gets picked least and why."
- **Loop 3 — synthesis.** Ship the visuals + insight pass together; they are two halves of the same legibility gain. Keep status effects deliberately subtle (slow ×0.7, burn -0.2/tick) so they change feel without changing win rates materially. Feed + damage numbers are local-only on guest side — no snapshot schema churn. File this decision before the lint+verify sweep so the pass traces back to one written source.

## Reversibility note

Medium. Rendering changes are isolated to `draw()` + helpers and can be reverted to the prior circle/rect primitives. Status-effect ticking is additive behind per-enemy `statuses:[]` and can be stripped. Snapshot schema additions are read-optional on the guest side. The only non-trivial rollback surface is the combat-feed DOM panel; it is one `<div>` and one CSS block.

## Follow-ups

- PORT-NOTES gains rows for silhouette renderer, hex+glyph, projectile shapes, damage numbers, status icons, next-wave telegraph, combat feed, muzzle flash (all mapped to Godot idioms).
- `prototype/README.md` v3 changelog + updated watch-for list.
- CASCADE.md decisions table gains a row for this file.
- PROGRESS.md session-log entry.
- Playtest note: if damage-number density feels overwhelming, threshold the white-number pop to ≥1 base damage (currently all hits).
