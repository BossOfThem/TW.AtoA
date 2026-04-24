# Decision — Commander-pick identity-floor upgrade

**Date:** 2026-04-20
**Status:** Accepted
**Reversibility:** Easy
**Affects:** `prototype/index.html` (portrait 490–494, XP ladder 502–513, roster 1333+, `applyCommanderCard` 1358+, new `silhouetteSVG`/`previewCommanderVO`/`applySilhouetteTest`)

> **Rebase banner — added 2026-04-22.** This decision is **rebased (not superseded)** under the [2026-04-21 concept tightening (3/3/3 + dungeon cosmology + Ash-enabler hybrids)](2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md) (Reversibility **Hard**). Rebase delta: the silhouette set **collapses 5 → 3** to match the new 3-launch-commander / 3-lineage roster (Ash / Nature / Prayer prose placeholders); the Sinew-pike / Ember-hooded / Forge-anvil / Crown-banner / Veil-masked archetypes become **3 silhouettes under the new lineages**, specific poses TBD under the deferred naming pass and Step B prototype-reshape scope. The **silhouette-test harness (`?silhouette-test=1` + Shift+S grayscale toggle), XP ladder (20 levels [PROPOSAL]), cosmetic tick marks at L5/L10/L15, Voice-bus caption-preview, and pose-differentiation grayscale discipline all survive intact**. The research §6.1 no-go archetype list (gritty-male-soldier / chosen-one-orphan / scruffy-scoundrel) still applies to the 3 chosen poses. SVG path migration 5→3 is a Step B prototype-reshape data edit, not a concept change. Banner is bookkeeping; the Accepted status stands.

> **Re-rebase banner — added 2026-04-26** (2026-04-25 ratification Follow-up #10). The 2026-04-21 parent is now **Superseded by the 2026-04-24 reopen → 2026-04-25 real-cultures ratification** ([`2026-04-25-q2-real-cultures-direction-ratified.md`](2026-04-25-q2-real-cultures-direction-ratified.md), Reversibility **Hard**). This decision is **re-rebased, not superseded**. Re-rebase delta: the 3 silhouettes stay 3, now **civ-coded rather than lineage-coded** — Leonidas (Greek, phalanx / shield-and-spear iconography), Montezuma II (Aztec, priest-king / feathered headdress iconography), Ragnar Lothbrok (Norse, longship / axe / raider iconography). Pose specifics TBD and **gated by cultural-sensitivity pass** (2026-04-25 Follow-up #5) — Aztec silhouette especially must avoid caricature; Leonidas silhouette must pass the 300-movie-ideology audit; Ragnar silhouette must route through TV-show-vs-history framing. The research §6.1 no-go archetype list still applies. **XP ladder (20 [PROPOSAL]), cosmetic tick marks at L5/L10/L15, Voice-bus caption-preview, silhouette-test harness (`?silhouette-test=1` + Shift+S grayscale toggle), and pose-differentiation grayscale discipline survive intact**. SVG path migration and prototype-reshape remain deferred (prototype frozen per 2026-04-25 ratification). Banner is bookkeeping; Accepted status stands.

---

## Decision

Replace initial-letter circle portraits with inline SVG silhouettes per lineage (Sinew hulking pike, Ember hooded caster, Forge anvil-guard, Crown banner-bearer, Veil masked rogue) — each filled with lineage color, rim accent, grayscale-readable. Add 20-level XP ladder with visible L5 / L10 / L15 tick marks and cosmetic-slot chips that flip from "locked" to "unlocked" at the right level. Caption-preview plays a random VO line from `commanders.json` on portrait click (Voice bus shape, no audio file). Add `?silhouette-test=1` URL parameter + `Shift+S` toggle that applies `filter: grayscale(1)` and hides names — silhouette-read self-audit gate.

## Context

[commander-identity-floor.md](2026-04-20-commander-identity-floor.md) specifies the 20-level ladder, 3 cosmetic slots (skin L5 / frame L10 / map-tint L15), and the silhouette-test requirement. [research/03-commander-archetypes.md](../research/03-commander-archetypes.md) avoids over-represented archetypes — the five silhouettes here deliberately span: warmother (Sinew pike), scholar-architect (Ember hooded), elder-quartermaster (Forge anvil), conductor (Crown banner), archivist (Veil masked). None are the disallowed gritty-male-soldier / chosen-one-orphan / scruffy-scoundrel.

## Alternatives considered

- **Option A — Static PNG portraits.** Why not: asset pipeline forbidden in prototype; PNGs don't scale grayscale-test cleanly.
- **Option B — Canvas primitives (2D drawing calls).** Why not: more code, less readable at small chip sizes, harder to embed inline in HTML.
- **Option C — Inline SVG with path-composed silhouettes, per-lineage color + accent rim.** (Chosen.) Single source, scales cleanly, grayscale-filter trivial, small enough (< 1KB per silhouette) to inline.

## Reason chosen

**Loop 1 — aggressive critique.** Five SVG silhouettes at this fidelity risk looking cartoonish or too similar in grayscale. The XP ladder + tick labels could crowd the cmdr-card vertically. Caption preview via click is a pleasant flourish but might be missed by players who don't explore the UI.

**Loop 2 — steelman.** Silhouettes are placeholder by design — they're *pose-differentiated* (vertical pike / hooded arch / wide anvil / banner cross / masked ellipse) which reads clearly in grayscale. The ladder + slots are compact (one vertical band each, total ~60px). Caption preview is discoverability flourish, not a required mechanic — the player still sees the lineage stats regardless.

**Loop 3 — synthesis.** Ship as-coded. Pose-differentiation is the key grayscale-test insight; filter: grayscale + the silhouette-test mode provides a live feedback loop for refining the silhouettes pre-freeze. No CONCEPT change.

## Reversibility note

Easy. Revert = restore the letter-based portrait + the prior `applyCommanderCard`. No data schema changes (commander progression fields were already additive in `commanders.json`; `commanderProgress` per-profile is additive-only).

## Follow-ups

- Strand 5 (this pass): first-run prompts. Strand 7: commander-on-field hero uses same SVG silhouette scaled 1.4×.
- Port note: Godot → use `Sprite2D` with `modulate` for lineage color + grayscale shader toggle for silhouette-test; the SVG paths become vector-drawn outlines or baked PNG textures depending on art direction.
