## Decision — Aztec glyph: abstract placeholder pending cultural-sensitivity pass

**Date:** 2026-05-04
**Status:** Accepted
**Reversibility:** Easy
**Affects:** `prototype/data/civilizations.json` (Aztec entry, `glyph` field)

---

## Decision

Replace the Aztec civilization glyph in `prototype/data/civilizations.json` from `𓁹` (Egyptian Hieroglyph D4 / Eye of Horus, U+13099) to `◈` (White Diamond Containing Black Small Diamond, U+25C8) — a culturally-neutral abstract placeholder. Closes Follow-up #4 from [`decisions/2026-04-25-q2-real-cultures-direction-ratified.md`](2026-04-25-q2-real-cultures-direction-ratified.md). Greek (`Ω`) and Norse (`ᚱ`) glyphs are culture-coded and remain in place; Aztec is the only mismatched entry.

## Context

The 2026-04-25 ratification ships three civilizations (Greek / Aztec / Norse) with placeholder glyphs in `civilizations.json`. The Aztec entry was authored with `𓁹`, an Egyptian hieroglyph — the wrong civilization's writing system. This was logged as Follow-up #4 (glyph styling pass) at ratification time and has carried through C1 → C7.b → C6 slice 1 → C6 slice 2 (graduation cut) without being addressed. The graduation cut closed the reshape arc; tracks open for selection. PM picked Follow-up #4 (Recommended) on 2026-05-04.

## Alternatives considered

- **Option A — Pick a culturally-coded Aztec glyph now (e.g., a Nahuatl day-sign or codex motif).** Rejected. Cultural-sensitivity gate Follow-up #5 from the same 2026-04-25 ratification requires a hard pose-lock + content-lock review before any culturally-coded civ art ships. Picking an Aztec-coded glyph in this turn would bypass that gate. Greek `Ω` and Norse `ᚱ` were already in-tree at ratification time and inherit pre-gate status; they are not in scope for this fix.
- **Option B — Leave `𓁹` in place and bundle the swap with the eventual culturally-coded glyph pass.** Rejected. The wrong-civ glyph is actively misleading: it would surface in HUD, silhouettes, and reference panel as "Aztec = Eye of Horus," which is a worse failure mode than an abstract placeholder. Cheap to fix in one line; defer is not free.
- **Option C — Swap to a neutral abstract glyph now; defer the culturally-coded replacement to Follow-up #5.** (Chosen.) One-line edit; closes Follow-up #4 with a defensible interim. Asymmetry with Greek/Norse is acknowledged and intentional — better an honest placeholder for the un-ratified civ than a wrong-culture artifact.

## Reason chosen

Cultural-sensitivity gate is non-negotiable. Removing the wrong-culture artifact is the highest-priority fix the gate permits without itself running. `◈` is visually distinct from both Greek `Ω` (letter) and Norse `ᚱ` (rune), reads as a "shape," and carries no specific cultural coding. The asymmetry (two civs culture-coded, one abstract) is a feature: it surfaces the open Follow-up #5 work to anyone reading the prototype, rather than masking it.

## Reversibility note

One-line revert in `civilizations.json`. No downstream code depends on the glyph value; `renderTowerHex` reads `meta.glyph` opaquely via `glyphChar()`. Any future culturally-coded replacement would land via the Follow-up #5 cultural-sensitivity pass under PM ratification.

## Follow-ups

- Follow-up #5 (cultural-sensitivity pass) remains open. When it runs, the Aztec glyph should be re-evaluated alongside Greek/Norse; either keep `◈`, swap all three to a coherent abstract set, or commission a culturally-coded set under content-lock-gate.
- `iconPlaceholder: "feathered-headdress"` in the same Aztec entry remains untouched — that is descriptive metadata for a future art pass, not a rendered glyph, and does not block anything.
