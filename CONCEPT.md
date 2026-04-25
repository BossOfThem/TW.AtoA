# TW-COMMANDERS — Concept Cascade (Hub)

> **Navigation note (added 2026-04-19, restructured 2026-04-20):** This doc is now a thin **hub**. Each Phase's full content lives under [concept/](concept/) as `phase-N.md`. Detailed per-stage drill-downs live under [stages/](stages/); deep-dive market research under [research/](research/); dated decisions under [decisions/](decisions/). Start at [CASCADE.md](CASCADE.md) for the full map.

**Working title only.** A tower wars game where every match is a compressed **mortal-to-mythic arc** grounded in **real-world cultures and their native myths** — **Greek, Aztec, Norse** at launch — fought between Commanders (legendary historical leaders: **Leonidas / Montezuma II / Ragnar Lothbrok**) who each command their civilization's full roster (6 T1-T3 towers + 5 units + 6 T4 Demigods/Heroes + 3 Gods reachable via a locked 2-Demigod Fusion endgame). The tower you place in minute 1 still matters at minute 20 — it has promoted through the tier ladder (T1 → T2 → T3 → T4 Demigod), and two of your T4 Demigods may have fused into one of three locked Gods of your civilization's pantheon.

This document is structured as a **waterfall cascade**: seven sequential phases, each with an explicit exit condition that hands off to the next. You do not skip ahead. A phase does not begin until the one above it is signed off. The point of the cascade is that Phase 7 decisions are constrained by Phase 1 decisions, and you can trace every late choice back to an early one.

## Placeholder names

All names in this document and its children — commanders, factions, legions, ages, towers, units, hybrids, heirlooms, currencies, modes, enemies — are **placeholder / conceptual**. They will be revised once mechanics are locked and identity work begins. Do not treat them as final. When a name is finalized, it will be marked `[LOCKED]`.

The only locked decisions about naming are the *conventions* themselves in §5.4 below, not the specific names.

## The Commander is the user

Throughout this document, "the Commander" refers to the player's persistent avatar in the game. The player chooses a Commander at first login. The Commander carries across matches, levels up, unlocks content, and can be deployed as a Hero Unit on the battle map in modes that support it. The Commander is the player's identity in the game world. When in doubt about perspective, assume first-person player.

---

## Phase index

Open only the phase you need. Each file is self-contained with its own §-sections; anchors preserved (e.g. `concept/phase-3.md#32-the-commander-system-central-feature`).

| Phase | File | One-line summary |
|-------|------|------------------|
| 1 — Discovery | [concept/phase-1.md](concept/phase-1.md) | Vision, target player, three-part promise, success criteria. |
| 2 — Analysis | [concept/phase-2.md](concept/phase-2.md) | Competitive landscape, constraints, risks, §2.4a accessibility floor [LOCKED]. |
| 3 — Design | [concept/phase-3.md](concept/phase-3.md) | Match loop, Commander system, 3 civilizations (Greek/Aztec/Norse — each with 6 towers + 5 units + 6 T4 Demigods + 3 Gods), 3 launch commanders (Leonidas / Montezuma II / Ragnar Lothbrok), modes, meta systems, audio, first-run. |
| 4 — Specification | [concept/phase-4.md](concept/phase-4.md) | Commander identity floor, Fusion system (9 locked Gods via 2-Demigod recipes, Divinity-gated), mobile units, economy (Tribute + Divinity), enemies (real-cultures + myth, armor-tag-constrained), save, attack-type mapping (7 types + 5 armor tags + RPS). |
| 5 — Implementation planning | [concept/phase-5.md](concept/phase-5.md) | MVP slice, build order, art direction, **§5.4 naming conventions [LOCKED]**, engine. |
| 6 — Validation | [concept/phase-6.md](concept/phase-6.md) | MVP primary question, success metrics per build phase, playtesting. |
| 7 — Iteration | [concept/phase-7.md](concept/phase-7.md) | Open questions, decision log policy, refinement queue, notes to future self. |

---

## §5.4 Naming conventions (LOCKED — canonical copy here for cross-reference)

The only locked naming decision in the cascade. Full context in [phase-5.md#54-naming-conventions-locked-at-phase-5](concept/phase-5.md#54-naming-conventions-locked-at-phase-5).

**Amendment 2026-04-28:** Lineages row deleted; Civilizations row added. Per [`decisions/2026-04-28-phase-5-naming-conventions-lineages-row-deletion.md`](decisions/2026-04-28-phase-5-naming-conventions-lineages-row-deletion.md) (closes Follow-up #10). Original Lineages convention archived in [`CASCADE-history.md`](CASCADE-history.md).

- **Game title:** TBD. Current working title is placeholder.
- **Commanders:** evocative titles, may be first-name + epithet. Never generic.
- **Civilizations:** real-culture proper nouns; the culture names itself. No invented placeholders. Launch roster: Greek / Aztec / Norse. Expansions follow the same pattern (real cultures only).
- **Ages:** evocative compound nouns, not dates (pattern: The Mudbrick Era).
- **Towers/Units:** job titles, never proper nouns (pattern: Warhost, Spirebinder).
- **Hybrids:** compound or hyphenated (pattern: Tank Corps, Rune-Smiths).
- **Enemies:** single-word kenning (pattern: Thornback, Nullspawn, Ashwake).
- **Heirlooms / inventory items:** mythic-fragment style (pattern: The Last Spear of Heidelberg).
- **Modes:** direct, muscular (pattern: Lane Wars, Horde, Campaign). Not florid.

---

## Non-negotiables (selected from §7.4 notes-to-future-self)

Full list in [phase-7.md#74-notes-to-future-self](concept/phase-7.md#74-notes-to-future-self). The ones to apply without re-reading:

- **The Commander is the user.** Commander must have voice, story, progression, signature ability. Not a skin with a stat modifier.
- **Solo mode must be fully great on its own.** Multiplayer is additive, not required.
- **Strict no-pay-to-win.** Battle pass + cosmetic store works only under this discipline. Non-negotiable.
- **Cascade discipline.** Phase N decisions may not violate a Phase N-1 constraint without a written override in [decisions/](decisions/).
- **Accessibility floor is [LOCKED]** ([phase-2.md §2.4a](concept/phase-2.md#24a-accessibility-floor-launch-constraint--locked-as-constraint-per-feature-ui-proposal)). No information by color alone; full input remap; WCAG 2.3.1; independent UI + subtitle scaling; colorblind-safe iconography; XAGI tag taxonomy at launch.

---

*Document version: 0.8 — 2026-04-26 real-cultures frame cascade (partial). Hub vision line rewritten from "Ash to Altar cosmological arc / lineage paths" to **real-world cultures + native myth** (Greek/Aztec/Norse launch civs + Leonidas/Montezuma II/Ragnar Lothbrok + 18 T1-T3 towers + 15 units + 18 T4 Demigods & Heroes + 9 Gods via locked Fusion recipes). Phase 3 index row rewritten (3 civilizations + locked commanders). Phase 4 index row rewritten (Fusion system + Tribute/Divinity economy + armor-tag enemies + attack-type mapping). Per [`decisions/2026-04-25-q2-real-cultures-direction-ratified.md`](decisions/2026-04-25-q2-real-cultures-direction-ratified.md) (Reversibility Hard) + [`decisions/2026-04-26-attack-type-mapping.md`](decisions/2026-04-26-attack-type-mapping.md) (Reversibility Medium). §5.4 [LOCKED] UNTOUCHED; §2.4a [LOCKED] UNTOUCHED. Follow-on cascade turns will rewrite §3.1, §3.5, §3.8 (tier-ladder / lineage-whiteboard residue), §4.2, §4.5, §4.6, §4.8 (divergence / special-effects / economy / exit-condition), §5.2 (build phases), and §6/§7 upstream-constraint consumers. Prior: v0.7 — 2026-04-21 concept tightening. Hub vision line + Phase 3 index row amended to reflect the 3/3/3 shape (3 lineages Ash/Nature/Prayer, 3 tiers Dust/Form/Apotheosis under Ash→Altar dungeon cosmology, 3 launch commanders, Ash-enabler hybrid model). Decision entry: [2026-04-21 concept tightening](decisions/2026-04-21-concept-tightening-3x3x3-dungeon-cosmology.md) (Reversibility Hard). Names (Ash/Nature/Prayer, Dust/Form/Apotheosis) are prose placeholders — §5.4 [LOCKED] UNTOUCHED per PM-locked naming-pass deferral. Prior: v0.6 (hub split), v0.5 (save-model absorb), v0.4 (batch-amendment). Numerical floors in phase-4.md §4.1 and phase-3.md §3.11 remain [PROPOSAL]; §5.4 naming conventions and §2.4a accessibility floor remain [LOCKED]. 3 is a lean-launch floor, not an expansion ceiling. Reopen any phase with discipline, not convenience.*
