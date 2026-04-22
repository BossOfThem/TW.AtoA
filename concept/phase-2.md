---
**Status:** Draft
**Last reviewed:** 2026-04-22
---

# Phase 2 — Analysis

*What constrains the design before we design anything.*

Parent hub: [CONCEPT.md](../CONCEPT.md). Prior: [phase-1.md](phase-1.md). Next: [phase-3.md](phase-3.md).

## 2.1 Competitive landscape

- **Legion TD 2** — the direct genre competitor. We learn from their mechanics (legions, mythium, merc-sending, mastermind drafting); we beat them on polish, single-player depth, and commander-driven identity.
- **Kingdom Rush / Bloons TD 6** — the production quality bar. Kingdom Rush reference for solo TD polish; Bloons for replay depth.
- **Warcraft 3 custom maps** (Element TD, Green TD, Castle Fight, Hero Line Wars) — the genre origin. Our reference for variety, community-driven mode expansion, and the idea that tower wars can host many sub-genres.
- **Clash Royale** — reference for commander/persistent-progression in a multiplayer strategy loop. We borrow structure, not gacha.
- **Deep Rock Galactic** — reference model for fair monetization: premium price + free earnable battle pass + cosmetic DLC, zero pay-to-win.
- **Hades** — reference for meta-progression that respects the player and doesn't gate fun behind grind.
- **Civilization / Humankind** — thematic inspiration only. We are NOT a 4X.
- **Plague Inc. Evolved** — reference for "evolution as mechanic."

## 2.2 Design constraints

- **Match length:** 5–25 minutes depending on mode. Solo TD target ~15min, lane wars ~20min, horde ~25min, quick-match ~8min.
- **Platform:** PC primary. Mobile is a post-launch consideration, not a launch requirement. Competitive multiplayer on mobile is a separate UX problem we are not solving at launch.
- **Team size:** two developers using AI-assisted workflows. Content must be data-driven and generable, not hand-sculpted per unit.
- **Art budget:** unknown at concept stage. Assume silhouette-forward stylized until proven otherwise. Contract an art director in Phase 4 or early Phase 5.
- **Netcode:** user-hosted games + Steam networking for launch. No dedicated server infrastructure required at launch. Dedicated servers for ranked later, maybe.

## 2.3 Known risks

- **Content explosion.** Commanders × lineages × tiers × forks × hybrids = combinatorial content under the 3/3/3 launch shape per [2026-04-21 concept tightening](../decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md); post-launch expansion re-opens the cross-product. Must be scoped aggressively. Data-driven pipeline is non-negotiable.
- **Lineage balance.** Three lineages must feel mechanically distinct, not just cosmetically (amended 2026-04-22 from "five" to follow the 2026-04-21 concept tightening). Under a 3-lineage shape any convergence is more catastrophic than under a 5-lineage scaffold — the risk tightens, it does not relax. Role-differentiation is tracked as an open question at [phase-7 §7.1 #9](phase-7.md#71-open-questions-resolution-targets-noted). Multi-way balance is notoriously hard.
- **Onboarding cliff.** Commander + ages + lineages + economy + send/defend + modes is a lot for a first-time player. Tutorial design is a real UX risk and gets its own Phase 5 attention.
- **Multiplayer cold-start.** If ranked lobbies don't fill, competitive play dies. Solo mode must carry the game independently. See §2.4.
- **Live-service ops commitment.** Battle pass + store + seasonal content requires ongoing team capacity. A two-dev team cannot run AAA-scale live ops. Content cadence must be realistic.
- **Monetization model tension.** Battle pass + cosmetic store works *only* with strict no-pay-to-win discipline. One misstep burns audience trust permanently. This is not a marketing concern; it is an identity constraint.
- **Commander over-promise.** If commanders are visually distinct but mechanically identical, the identity promise fails. Each commander must feel different to play.

## 2.4 Constraints we are choosing to accept

- **Solo mode is first-class.** Fully playable, fully polished, complete on its own. Multiplayer is additive, not required.
- **PC-first, desktop-quality UX.** Mobile later or never.
- **Premium + cosmetic monetization.** Target price point $5–15. Free seasonal battle pass earnable through play. Optional cosmetic DLC. NEVER pay-to-win. NEVER gacha. NEVER gameplay advantage sold.
- **English-first.** Localization is post-launch.
- **User-hosted multiplayer.** No dedicated server ops at launch. Accept peer/host trust model for small-lobby play.

## 2.4a Accessibility floor (launch constraint) — [LOCKED as constraint, per-feature UI [PROPOSAL]]

*Decision entry: [2026-04-20 accessibility floor](../decisions/2026-04-20-accessibility-floor.md). Reversibility: Hard.*

Accessibility is a Phase 2 launch constraint, not a Phase 5 stretch goal. Launch floor:

1. **No information conveyed via color alone.** All gameplay-critical state carries shape / icon / text in addition to color (lineage, tower range, threat, lane ownership, age-gate readiness, hybrid adjacency, Mythium send indicators).
2. **Full input remapping at launch**, in-game UI, no file-edit fallback. Toggle-vs-hold per action where applicable.
3. **WCAG 2.3.1 compliance.** No flashing element exceeds 3 flashes per second. Reduce-effects toggle available.
4. **Independent UI and subtitle scaling.** UI scale 75%–150% minimum. Subtitle scale independent. Subtitles include speaker labels.
5. **Colorblind-safe iconography by default + colorblind-mode toggle** for stronger differentiation.
6. **Xbox Accessible Games Initiative tag taxonomy is the launch self-audit target.** Public accessibility statement at launch enumerates tags filled and gaps remaining.

Per-feature UI spec lives in Phase 5. Phase 5 sizing must confirm deliverability against the two-dev constraint (§2.2); if a floor item is undeliverable, surface via supersession, not silent drop.

## 2.5 Open question flagged here — OPEN

Monetization model specifics: premium price point, battle pass structure, cosmetic store scope. Leading model: Deep Rock Galactic (premium price + free earnable battle pass + optional cosmetic DLC). Must be resolved before Phase 5 exit. Tagged as blocker.

## 2.6 Exit condition for Phase 2

The design team can list, from memory, the top three risks and the top three constraints. Nothing in Phase 3 may violate a Phase 2 constraint without a written override in the decision log.

→ **Hand off to [Phase 3](phase-3.md).**
