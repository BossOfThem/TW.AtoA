# Decision — Accessibility floor as Phase 2 constraint (GAG top-4 + WCAG 2.3.1 + Xbox AGI tagging)

**Date:** 2026-04-20
**Status:** Accepted (resolution direction). CONCEPT.md amendment is a separate follow-up step within this sweep; per-feature UI spec deferred to Phase 5.
**Reversibility:** Hard (this is a Phase 2 constraint reopen — once committed as a launch requirement, removing it is a project-identity change, not a refactor).
**Affects:** [`CONCEPT.md`](../CONCEPT.md) §2 (Phase 2 — pending amendment to add accessibility constraints alongside §2.4 "Constraints we are choosing to accept"), `CONCEPT-GAPS.md` (rows `A11Y-01`, `A11Y-02`, `A11Y-03`, `A11Y-04`, `SETTINGS-02` migrate out on amendment; `A11Y-05` remains as Post-launch-ok), Phase 5 spec (per-feature UI lives here).

Resolves: `CONCEPT-GAPS.md` rows **A11Y-01** (colorblind), **A11Y-02** (font/UI scaling), **A11Y-03** (reduced motion / WCAG 2.3.1), **A11Y-04** (subtitles), and **SETTINGS-02** (full input remap) as a coupled constraint set. **A11Y-05** (one-handed / single-stick / toggle-vs-hold input modes) remains Post-launch-ok per CONCEPT-GAPS row.

---

## Decision

Accessibility is committed as a **Phase 2 launch constraint**, not a Phase 5 stretch goal. The launch floor is:

1. **No information conveyed via color alone.** All gameplay-critical state (lineage identity, tower range, threat level, lane ownership, age-gate readiness, hybrid-eligible adjacency, Mythium send indicators) carries shape, icon, or text in addition to color.
2. **Full input remapping at launch.** Every player-bound action (cursor, place, upgrade, sell, send, ability, pause, quick-select) is rebindable from in-game UI. No `settings.lua`-style file-edit-only fallback. Toggle-vs-hold per action where applicable.
3. **WCAG 2.3.1 compliance.** No flashing element exceeds 3 flashes per second. Reduce-effects toggle exists for users who need additional protection beyond the WCAG floor.
4. **Independent UI and subtitle scaling.** Global UI scale 75%–150% minimum. Subtitle scale independent of UI scale. Subtitles include speaker labels.
5. **Colorblind-safe iconography by default + colorblind-mode toggle.** Default art passes the most common colorblind types (deuteranopia, protanopia, tritanopia) without the toggle on; the toggle adjusts UI palettes for users who want stronger differentiation.
6. **Xbox Accessible Games Initiative tag taxonomy is the launch self-audit target.** Ship tagged against the AGI 24-tag set; not all 24 tags must be filled, but the launch self-audit is run and the gaps are documented (not hidden).

Per-feature UI (slider widgets, remap UI affordance, toggle placement, colorblind preview swatches) is Phase 5. CONCEPT.md Phase 2 will gain language alongside §2.4 naming these constraints.

## Context

`CONCEPT-GAPS.md` rows A11Y-01..04 + SETTINGS-02 collectively flag that CONCEPT.md mentions accessibility zero times. The Game Accessibility Guidelines top-4 most-complained issues (input remapping, text size, colorblind support, subtitles) are all absent. WCAG 2.3.1 is industry baseline (seizure safety) and not optional. Xbox AGI is the 2024–2025 standardized tagging vocabulary that retailers and storefront discovery use. Severity is **Blocks-launch** for all five rows because the legal/commercial cost of shipping without these (refunds, store delisting risk, reputational damage, accessibility-org callouts) outweighs the development cost of meeting the floor.

This entry is unusual in this sweep because it is the only one **reopening Phase 2**. CLAUDE.md is explicit that Phase N+1 may not silently edit Phase N — but Phase 2 amendments via dated decision entries are *the prescribed path*, not the prohibited one. This entry is the prescribed path.

## Alternatives considered

- **Option A — Defer all accessibility to Phase 5 spec.** Rejected: Phase 5 is *implementation planning*, which means the constraints must already be locked. Trying to "add accessibility in Phase 5" without a Phase 2 commitment results in late-cycle scope conflict ("we can't ship remap, the input system was built without it"). The Phase 2 commit is what *enables* Phase 5 to plan honestly.
- **Option B — Adopt the full Xbox AGI 24-tag set as a hard requirement.** Rejected: 24 tags include features (one-handed play, alternate input via switch devices, audio descriptions for cinematics) that may not apply to a TD or that can defensibly land post-launch. The right commitment is "tag against the taxonomy and document gaps;" not "fill every tag."
- **Option C — Keybind remap as Phase 5 only (file-edit fallback acceptable for launch).** Rejected: Kingdom Rush 5 Alliance shipped this way and was community-flagged as substandard. A 2024-going-forward TD launching in 2026+ without in-game remap will face the same callout. Cost-to-build is moderate; cost-of-not-having-it is reputational.
- **Option D — Color-blind toggle only, no default colorblind-safe palette.** Rejected: forces all colorblind users to discover, enable, and configure a toggle before play is comfortable. Default-safe palette + toggle for stronger differentiation is the cascade-correct order (everyone benefits from the default; the toggle is additive).
- **Option E — (Chosen.) Bundled Phase 2 constraint commitment covering the GAG top-4 + WCAG 2.3.1 + AGI tagging, with per-feature UI deferred to Phase 5.** Names what must be true at launch; defers how it looks.

## Reason chosen

### 3x debug loop

**Loop 1 — aggressive critique.**
- This is the most cascade-heavy entry in the sweep — Phase 2 reopen affects every downstream phase. Filing it inside a same-session batch instead of as its own deliberation is exactly the cascade-leak failure mode.
- "No information via color alone" is easy to write and hard to enforce. Without a checklist or tooling commitment (grayscale screenshot review, automated palette audit), the constraint is a gesture.
- Bundling 5 GAG/SETTINGS rows into one entry hides the asymmetry between them — input remap is engineering work, colorblind palette is art-direction work, subtitle scale is UI work. Different teams, different timelines.
- "Default colorblind-safe by default" is a major art-direction constraint that has not been signed off by an art director (who CONCEPT.md says is contracted in Phase 4 / early Phase 5). Pre-committing the art director's hands.
- AGI tagging "self-audit at launch" is governance theater — without a named owner and a date, "we'll self-audit" is wishlist.
- Reversibility tagged Hard, but the entry treats this casually. Hard reversibility *means* the cost of a wrong call here compounds across the project.

**Loop 2 — steelman.**
- The cascade-heaviness is exactly *why* this entry routes through a dated decision entry, not a silent edit. The session-batch concern is valid for *content* speed but the cascade *path* is correct (decision entry → Phase 2 amendment via the next step in this sweep). The PM has signed off the batch; this is the prescribed path inside it.
- "No information via color alone" being hard to enforce is a Phase 5 / QA concern. Phase 2 owns the *constraint*; the enforcement mechanism (grayscale check, palette audit, art-director review checklist) is a Phase 5 follow-up. Not naming the enforcement mechanism in this entry is correct scope discipline.
- The 5-row bundle is justified: the rows share an owning phase (all Phase 2 constraints) and a launch-vs-defer binary (all Blocks-launch). Splitting into 5 entries would force cross-references that say the same thing each time. The asymmetry between *implementation* timelines (engineering / art / UI) is a Phase 5 sequencing concern, not a Phase 2 constraint concern.
- Pre-committing the future art director's hands is *the point* of a Phase 2 constraint. The art director is hired *under* the project's constraints, not authored *into* them. CONCEPT.md §2.2 already names "silhouette-forward stylized" as a working art direction; "colorblind-safe palette" is a compatible refinement, not a contradiction.
- AGI "self-audit at launch" with documented gaps is *not* governance theater if the documented-gaps part is real. The commitment is "we will know what we shipped without and admit it publicly," which is a substantive accountability stance, not a wishlist. A specific owner and date is a Phase 5 / launch-checklist concern.
- Hard reversibility is correctly tagged. The entry's casual tone is a wording issue — addressed in Loop 3.

**Loop 3 — synthesis.**
The decision survives critique with two sharpenings:
1. Reversibility note is rewritten below to reflect the Hard tag substantively (not casually).
2. The "self-audit" commitment is sharpened to "self-audit run and gaps documented in a public-facing accessibility statement at launch" — a specific, falsifiable artifact.

The 5-row bundled Phase 2 constraint is the right shape. Per-feature UI, palette enforcement tooling, and per-row implementation timelines are correctly deferred.

## Reversibility note

**Hard.** A Phase 2 constraint reversal (e.g., "we will not ship in-game keybind remap at launch") would require:
- Reopening Phase 2 with a superseding decision entry that names what changed in the project's identity (cost / timeline / scope) to justify the reversal.
- Reverting the CONCEPT.md §2 amendment that this entry's CONCEPT.md follow-up will land.
- Re-routing every downstream Phase 5 spec row that assumed the constraint (input system architecture, UI palette work, subtitle pipeline).
- Public-relations cost: an accessibility commitment, once stated externally (via the AGI tagging self-audit, store-page accessibility section, etc.), is functionally one-way. Reversal is a launch-credibility hit.

To reduce future-reversal risk: the per-feature UI spec in Phase 5 should be sized realistically against the two-dev team constraint (CONCEPT §2.2). If sizing reveals one of the 5 floor items is undeliverable, surface it *immediately* via supersession — not silently dropped.

## Follow-ups

- **CONCEPT.md amendment** within this sweep: add a Phase 2 sub-section (working `§2.4a — Accessibility floor`) naming the 5 floor items and the AGI tagging commitment. Routes the change through Phase 2 properly.
- **Public-facing artifact (Phase 5 / launch):** accessibility statement page enumerating the AGI tags filled and the gaps remaining. Owner TBD at Phase 5.
- **Cross-row dependency:** the meta-UI envelope entry's Options menu is the surface where every accessibility toggle lives. Confirmed compatible with that entry.
- **Cross-row dependency:** the audio architecture entry's Voice bus enables the subtitles row (A11Y-04) — captioned voice lines route through the same Voice bus.
- **Still open / not addressed:** A11Y-05 (one-handed / single-stick / switch input) remains Post-launch-ok. Re-evaluate at Phase 5 if engineering capacity permits earlier.
- **Two-dev sizing risk** flagged for Phase 5 entry into this work — see Reversibility note.
