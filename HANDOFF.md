# HANDOFF — Session Checkpoint

**Last session:** 2026-05-05 → 2026-05-06 (**clear-safe**).
**Hand-off by:** Claude (Opus 4.7)
**Hand-off to:** next Claude Code session after `/clear`.

---

## TL;DR

**Phase C of the prototype UI verification sweep LANDED. FULL SWEEP (A → B → C) CLOSED.** Four commits dual-pushed in Phase C: `5d2f3c8` (Medium #8 end-screen XP persists), `8f67a08` (Large #10 RESOLVED-no-code — markup canonical 2 buttons), `4964895` (Large #9 RESOLVED-no-code — `A` age-up intentionally retired under 2026-04-25 real-cultures ratification), `abcb398` (Medium #6 input rebind wiring via `Profile.setting("input.binds")` w/ `e.code` defaults). 9 of 10 NEEDS-FIX rows resolved. **Two new findings flagged** for next-session sweep: (a) `openReference` ln 3310 `CIVS_DATA` undefined ReferenceError (pre-existing, affects Info button + I-key); (b) mode-select copy ln 495/507/513 obsolete "three ages"/"11-age arc" refs. NEXT session picks next track from the post-sweep roadmap.

---

## NEXT SESSION — primary directive

Phase C is complete; the prototype UI verification sweep is closed. Pick **one** track from the post-sweep roadmap below. Default to `AskUserQuestion` (Recommended-first) at session start to gate the choice — this is a genuine fork.

### Roadmap (Recommended-first)

1. **Per-tower authoring sub-pass** *(Recommended)* — bind cd / range / attack-type / status-proc across 18 T1-T3 + 18 T4 Demigod + 9 God towers across 3 civs. Consumes §4.10 frame + §4.11 magnitudes + §4.6a aux catalog. Likely 5-10 rounds. **Cross-arc dependency:** per-commander affinity hooks (closed last week) bind tower-side targets here. Largest unblocked authoring track; closest to Phase 5 readiness.
2. **Prototype UI verification sweep — micro-followup batch** *(small, contained)* — fix the two new findings flagged from Phase C: (a) `openReference` ln 3310 CIVS_DATA bug; (b) mode-select obsolete copy ln 495/507/513. Both small inline fixes. Good warm-up if context budget tight or PM wants a clean prototype state before opening the next big arc.
3. **Per-civ specialization** — Greek / Aztec / Norse identity profiles. Intersects Follow-up #5 cultural-sensitivity gate.
4. **Per-map authoring (incl. Round 11 mandate)** — good-cell authoring + wave-randomization seeds + crystal-lock variance per §4.7 R11.
5. **Phase 5 readiness gate** — engine-side telemetry per §6.5 + wave variance per §4.7 R11.
6. **`research/06-tw-subgenres.md`** new stub.
7. **`admin/concept.json` migration direction** — long-deferred.
8. **Follow-ups** — #5 cultural-sensitivity / #6 Patch-1 commanders + Thor recipe / #7 Foresight-coin + PvE campaign + AGES + leveling / #8 non-boss enemy ontology / #9 additional commanders / C7.b deferred (Builder concurrency cap + 90% refund-on-cancel UI).

### Discipline (carry forward)

- Preview server: `.claude/launch.json` config `prototype` (port **8766**, since 8765 is occupied on this machine). Or `python -m http.server 8766` from repo root + load `http://localhost:8766/prototype/index.html`.
- Prefer `preview_eval` over `preview_screenshot` for state probes (cheaper, deterministic).
- Commit per fix or per ~3-fix batch. Dual-push every commit.
- Run `python tools/cascade-lint.py` before each commit; expect clean except pre-existing phase-4 soft-cap (626/600).

---

## What is locked (clear-safe)

### Carried forward (untouched this session)

- 17-item conceptual frame (a)-(r) + extension (s) — Accepted.
- All 10 Numbers-phase magnitudes — Accepted.
- 6-mode ontology — Accepted.
- Auxiliary economy structure (Tribute kill-only + Divinity 6-source 4-floor+2-escalation; 6-cap discipline) — Accepted.
- "Go big, no scope cuts" doctrine — Accepted (hub Non-negotiable).
- 2026-04-25 locked content skeleton — Accepted.
- §5.4 [LOCKED] (Civilizations row).
- §2.4a [LOCKED] (accessibility floor).
- All R1-R7 CONCEPT amendment-pass §-anchors — Accepted.
- All per-commander R1-R5 spine-doc edits + lane locks (Leonidas=Control / Montezuma II=Economy / Ragnar=Summon, Hard reversibility) — Accepted.
- Splash-fix `CODEX_DATA` rename — Accepted.

### NEW this session (Phase C)

- Medium #8 LANDED (`5d2f3c8`) — `endMatch` at `prototype/index.html` ln 3390-3408 syncs in-memory `c.progression` mutation back to `Profile.data.commanderProgress[cid]` via `Profile.save()` per §4.9.
- Medium #6 LANDED (`abcb398`) — match keydown ln 3563-3578 resolves all match-scoped binds via `Profile.setting("input.binds", {})` with sensible `e.code` defaults (Space / KeyI / KeyU / KeyX / Digit1..9). Replaces hardcoded `e.key` literals.
- Large #10 RESOLVED-no-code (`8f67a08`) — PM ratified live markup canonical (2 buttons). Obsolete scene-checklist refs amended in this turn's doc-hygiene bundle.
- Large #9 RESOLVED-no-code (`4964895`) — PM ratified `A` age-up intentionally retired under 2026-04-25 real-cultures ratification (4-tier ladder + Fusion replaced AGES; no age-up trigger in Tribute/Divinity economy). Reopens only via Follow-up #8 if PvE-campaign chapter lands. Concept anchors: phase-3.md:167, phase-4.md:325, phase-5.md:54, phase-7.md:31.
- Report carrier `prototype/UI-VERIFICATION-2026-05-05.md` title bumped Phase A → Phases A → B → C (CLOSED) with phase totals summary.

---

## State snapshot

### Git

- Branch: **`session/2026-04-25-q2-world-pitch`**.
- Latest commits: **`abcb398`** (Phase C close — Medium #6), `4964895` (Large #9 RESOLVED-no-code), `8f67a08` (Large #10 RESOLVED-no-code), `5d2f3c8` (Medium #8 XP persist). All dual-pushed.
- Working tree at handoff: doc-hygiene bundle (PROGRESS / CASCADE / CASCADE-history / PROGRESS-archive / HANDOFF) staged for the chore commit. `.accord/` untracked.

### Doc-hygiene state

- `PROGRESS.md` session log: 3 most-recent entries (Phase C / Phase B / Phase A). A→B handoff-prep entry archived to `PROGRESS-archive.md`.
- `CASCADE.md` pointer: 1 most-recent block (Phase C LANDED, sweep CLOSED). Prior pointer (Phase B LANDED) archived to `CASCADE-history.md`.
- `CASCADE.md` version footer: 0.65 + 0.64. 0.63 archived to `CASCADE-history.md`.
- cascade-lint expected clean except pre-existing `concept/phase-4.md` 626/600 soft-cap (carried — not introduced by this handoff).

### New findings flagged for next-session sweep (NOT Phase C scope)

- **(a) `openReference` CIVS_DATA bug** — `prototype/index.html` ln 3310 throws `ReferenceError: CIVS_DATA is not defined` when `game.commander.civ` is falsy and falls through to `CIVS_DATA && Object.keys(CIVS_DATA)[0]`. CIVS_DATA is undefined in the IIFE scope. Affects both Info button onclick and the I-key path. Pre-existing — independent of #6.
- **(b) Mode-select copy obsolete** — `prototype/index.html` ln 495 / 507 / 513 still references "three ages" / "one wave per age" / "11-age arc solo". Obsolete under post-2026-04-25 4-tier ladder + Fusion endgame.

Both small inline fixes; both queued as the "micro-followup batch" track in the roadmap above.

### Open follow-ups (carried — UNCHANGED)

- **#5** — Cultural-sensitivity pass (gates non-abstract civ art).
- **#6** — Patch-1 commanders per civ + Thor recipe-layer dissonance.
- **#7** — Foresight-coin / PvE campaign / AGES / leveling / attributes.
- **#8 / #9** — non-boss enemy ontology / additional commanders.
- **C7.b deferred** — Builder concurrency cap + 90% refund-on-cancel UI.
- **`admin/concept.json` staleness** — long-deferred.
- **`research/06-tw-subgenres.md`** new stub.

### Authoring sub-passes / roadmap (post-arc — preserve)

1. **Per-tower** — bind cd / range / attack-type / status-proc across 18 T1-T3 + 18 T4 Demigod + 9 God towers across 3 civs.
2. **Per-civ specialization** — Greek / Aztec / Norse identity profiles. Intersects Follow-up #5.
3. **Per-map / Round 11** — good-cell authoring + wave-randomization + crystal-lock variance per §4.7 R11 mandate.
4. **Phase 5 readiness gate** — engine-side telemetry per §6.5 + wave variance per §4.7 R11.
5. **`research/06-tw-subgenres.md`** new stub.
6. **`admin/concept.json`** migration.

### Regression-watch

- End-screen XP persist (Phase C #8) — re-verify on a fresh skirmish next session: play → win → reload → Profile XP bar reflects gain.
- Match keybinds (Phase C #6) — re-verify after a rebind round-trip via Options → Input tab → confirm match keydown picks up the new binding.
- Tutorial Esc dismissal (Phase B carry — re-verify sanity).
- Profile scene roster (Phase B carry — confirm L/XP rendering on reload, not just live nav).
- End-screen layout post-Highest-Age row removal (Phase B carry — confirm no orphan styling).
- `menu-last` resolution path (Phase B carry — confirm civ glyph correct for all three real-cultures commanders + legacy fallback path).

---

## Cadence rules carried forward (project-level)

- **Cadence exists to manage the context window, not to gate every step.**
- **PM autonomy mandate:** within established multi-round arcs where PM has consistently picked Recommended, proceed autonomously. See `feedback_autonomy_mandate.md`.
- **AskUserQuestion is the standard interface** when gating is needed. Recommended-first.
- **MD-first preservation** — for any scope expansion or non-trivial conceptual ratification, land in MD before further questions.
- **Dual-push discipline:** push to BOTH session branch AND `main` after every commit.
- **Local-main hygiene:** `git fetch origin && git log --oneline HEAD..origin/main` BEFORE reading docs.
- **3x debug loop** on any CONCEPT-constraint-touching proposal.
- **Doc hygiene on each handoff:** trim PROGRESS to 3, CASCADE pointer to 1 block, footer to 2.
- **Preview MCP cadence:** prefer `preview_eval` for state probes over `preview_screenshot` (cheaper, deterministic). Screenshot only when visual layout is the question.

---

## Next-session prompt (copy-paste after `/clear`)

```
Resuming Ash to Altar. Phase C of the prototype UI verification sweep
LANDED — FULL SWEEP (A→B→C) CLOSED. Four commits dual-pushed in Phase C:
5d2f3c8 (Medium #8 XP persist) + 8f67a08 (Large #10 RESOLVED-no-code:
markup 2-button canonical) + 4964895 (Large #9 RESOLVED-no-code:
A age-up intentionally retired under 2026-04-25 ratification) +
abcb398 (Medium #6 input rebind via Profile.setting("input.binds") +
e.code defaults). Report carrier prototype/UI-VERIFICATION-2026-05-05.md
title bumped to "Phases A → B → C (CLOSED)". 9 of 10 NEEDS-FIX rows
resolved.

BOOTSTRAP per CLAUDE.md: README → CLAUDE → CASCADE → HANDOFF → PROGRESS.

BEFORE reading docs:
  git fetch origin
  git log --oneline HEAD..origin/main   # should be empty

PRIMARY DIRECTIVE — pick next-session track via AskUserQuestion
(Recommended-first):

1. Per-tower authoring sub-pass (RECOMMENDED) — bind cd/range/
   attack-type/status-proc across 18 T1-T3 + 18 T4 Demigod + 9 God
   towers across 3 civs. Consumes §4.10 frame + §4.11 magnitudes
   + §4.6a aux catalog. Likely 5-10 rounds. Largest unblocked
   authoring track; closest to Phase 5 readiness.
2. Prototype micro-followup batch — fix the two new findings flagged
   in Phase C:
   (a) openReference ln 3310 throws ReferenceError: CIVS_DATA is
       not defined when game.commander.civ is falsy. Pre-existing
       bug; affects Info button onclick + I-key. Small inline fix.
   (b) Mode-select copy ln 495 / 507 / 513 still references
       "three ages" / "one wave per age" / "11-age arc solo" —
       obsolete under post-2026-04-25 4-tier ladder + Fusion endgame.
       Small inline copy fix.
   Both fixes ~minutes. Good warm-up if context budget tight.
3. Per-civ specialization (Greek/Aztec/Norse identity profiles;
   intersects Follow-up #5 cultural-sensitivity gate).
4. Per-map / Round 11 mandate (good-cell + wave-randomization +
   crystal-lock variance per §4.7).
5. Phase 5 readiness gate (engine-side telemetry per §6.5 + wave
   variance per §4.7 R11).
6. research/06-tw-subgenres.md new stub.
7. admin/concept.json migration direction (long-deferred).
8. Follow-ups (#5/#6/#7/#8/#9 / C7.b deferred).

CADENCE GUARDRAILS:
- Batch parallel reads; prefer Grep over full-file reads.
- Prefer preview_eval over preview_screenshot for state probes.
- Commit per fix; dual-push every commit.

REGRESSION-WATCH (carried):
- End-screen XP persist (Phase C #8) — verify reload.
- Match keybinds (Phase C #6) — verify rebind round-trip.
- Tutorial Esc; profile roster L/XP after reload; end-screen layout;
  menu-last civ glyph across three real-cultures commanders +
  legacy fallback.

VERIFY each commit with: python tools/cascade-lint.py
  (expect clean except pre-existing phase-4 soft-cap 626/600)
DUAL-PUSH each commit: session branch + main.

PREVIEW SERVER:
  .claude/launch.json config `prototype` (port 8766 — 8765 occupied)
  or python -m http.server 8766 from repo root.
  http://localhost:8766/prototype/index.html

SCOPE GUARD:
- §5.4 [LOCKED]; §2.4a [LOCKED]; locked content skeleton untouched.
- 17-item frame + extension (s) Accepted.
- All Numbers-phase magnitudes Accepted.
- All R1-R7 CONCEPT amendment-pass §-anchors Accepted.
- All per-commander R1-R5 spine-doc edits Accepted.
- Effect-type lane locks Hard reversibility.
- Cultural-sensitivity Follow-up #5 still hard-gates non-abstract
  civ art.

POST-SWEEP ROADMAP (preserve):
1. Per-tower authoring (cd/range/attack-type/status-proc, 45 towers).
2. Per-civ specialization (Greek/Aztec/Norse; Follow-up #5 gate).
3. Per-map / Round 11 (wave-randomization + crystal-lock + good-cell).
4. Phase 5 readiness gate (telemetry + wave variance).
5. research/06-tw-subgenres.md.
6. admin/concept.json migration.
7. Follow-ups #5/#6/#7/#8/#9 + C7.b deferred items.
```

---

## Escalation triggers

Hard-stop and flag if:

- §5.4 row beyond Civilizations would be touched.
- 2026-04-25 locked content-skeleton names would be modified.
- §2.4a is touched.
- Cultural-sensitivity concern surfaces (Follow-up #5).
- Local `main` stale on session start.
- `cascade-lint` fails new (pre-existing phase-4 soft-cap is carried).
- The 17-item frame would be silently edited.
- Any Numbers-phase bound magnitude would be silently re-tuned.
- Any amendment-pass §-anchor would be silently edited.
- Any per-commander R1-R5 spine-doc surface would be silently edited.
- A track touching CONCEPT constraints lands without 3x debug loop.
- Context budget pressure forces a mid-track split → file mini-handoff and stop cleanly.
