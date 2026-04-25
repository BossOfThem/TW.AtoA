# HANDOFF — Session Checkpoint

**Last session:** 2026-04-27 — Commander-as-summoned-ability-avatar plan-mode pass, **steps 1-4 of 8 LANDED**; steps 5-8 queued.
**Hand-off by:** Claude (Sonnet 4.6)
**Hand-off to:** next Claude Code session (post `/clear`)

---

## TL;DR (this session)

**Plan-mode pass on commander mechanics partially executed.** PM ratified the *summoned-on-cast* pattern via 8-question refinement round. Filed canonical decision, superseded the prior on-field-hero design, extended the prototype reshape plan with C4 Cast-bar + new C7 step, and amended `concept/phase-4.md §4.1` with the new in-match presence model. **4 of 8 plan steps complete.** Commit `7fd3be8` is the durable resume point.

**Key ratifications:**
- **Three-surface commander model:** identity plinth (out-of-match) / passive pip (in-HUD) / active cast avatar (summoned-on-cast).
- **Three-tier cast budget:** ~1.2s short-CD / ~2.8s long-CD / ~4.5s signature.
- **Builder unit class:** separated as degenerate mobile-hero (single anim, no AI, no combat).
- **30-wave historic match-arc beats (solo-only):** round-30 = commander's historic antagonist.
- **Round-30 antagonists:** Greek **Xerxes I** / Aztec **two-phase Tlaxcalan→Tezcatlipoca** (pre-contact, Cortés OUT) / Norse **Jörmungandr-or-Fenrir** (sub-Q OPEN as Follow-up #11).
- **§5.4 Lineages-row deletion** confirmed-in-principle (Follow-up #10).

**Steps 5-8 queued for next session** — see "NEXT SESSION" below.

---

## Commits this session

- `7fd3be8` — commander-as-summoned-ability-avatar — steps 1-4 of 8 + lint-row (decision filed, 2026-04-20 superseded, reshape-plan amendment, phase-4 §4.1 subsection, CASCADE decisions-table row).
- Handoff bundle (this commit) — CASCADE pointer + version v0.25 → v0.26, PROGRESS new entry + 2 archived, HANDOFF rewrite.

---

## State snapshot

### Git

- Branch: **`session/2026-04-25-q2-world-pitch`** at handoff bundle (push pending).
- Last pre-handoff commit: **`7fd3be8`**.
- `main` HEAD will be fast-forwarded by handoff push (dual-push discipline).
- Working tree at handoff start: clean except `.accord/` untracked.
- No PR opened.

### Phase status

- **Phase 1 thematic direction: RATIFIED** (real-world cultures + native myth — 2026-04-25).
- **Phase 1 exit one-pager: FILED** (2026-04-26).
- **4-tier + Fusion endgame** frame live across concept/phase-3..7 + stages 01/03/04/05/06/07.
- **7-type × 5-armor RPS matrix** live in [`decisions/2026-04-26-attack-type-mapping.md`](decisions/2026-04-26-attack-type-mapping.md).
- **Commander-as-summoned-ability-avatar** filed Accepted (2026-04-27); supersedes 2026-04-20.
- **Prototype reshape plan** still **Proposed** (now with 2026-04-27 amendment) — awaiting PM ratification. **Prototype files frozen.**
- `§2.4a` + `§5.4` [LOCKED] — untouched.

### Doc-hygiene state

- `PROGRESS.md` session log trimmed to 3 most recent entries (this handoff archived 2 oldest 2026-04-26 entries).
- `CASCADE.md` pointer block: most recent only (2 prior pointer blocks archived to `CASCADE-history.md`).
- `CASCADE.md` version footer: 2 most recent bumps (v0.26 + v0.25).
- Bootstrap stays ~78KB.

---

## NEXT SESSION — primary directive

**Resume Commander-as-summoned-ability-avatar plan-mode pass at step 5 of 8.** PM has not declared session complete — pass is mid-execution and was paused for handoff at context pressure.

Default cadence: **one-step-at-a-time with PM "go" gates**. HARD AUTONOMY MODE is NOT in force.

### Queued steps (5-8)

**Step 5 — `concept/phase-4.md` §4.4a Builder unit class subsection.**
- Insert NEW subsection between §4.4 and §4.5 specifying Builder as degenerate mobile-hero (single walk anim, spawn-from-home, no AI, no combat, despawn-on-arrive, concurrency cap 3, 90% refund cancel, walkable-build-grid distinct from enemy-path-grid).
- Redact `concept/phase-4.md §4.4` line 111 stale on-field-hero sentence ("Commander Hero Units have richer control — direct movement + 2-3 abilities + return-to-base. One active Commander Hero per player per match.") via strikethrough + dated supersede note pointing at the 2026-04-27 decision.

**Step 6 — `concept/phase-4.md` §4.7 banner extension.**
- Append "Historic match-arc beats (solo-only)" subsection.
- Round-30 antagonist roster: Greek = **Xerxes I**; Aztec = **two-phase Tlaxcalan ally turned Tezcatlipoca avatar** (pre-contact, no Cortés); Norse = **Jörmungandr OR Fenrir** (open sub-decision tracked as Follow-up #11 on the 2026-04-27 decision).
- Cross-civ tonal-arc note: mundane → mythic escalation across rounds 1-30; mini-bosses every 5 rounds; round-30 = commander's historic antagonist as boss.

**Step 7 — `CASCADE.md` v0.26 pointer + footer + decisions-table row.**
- ✅ DONE in this handoff bundle (pointer + version + decisions-table row already in tree).
- Re-verify after steps 5-6 land that nothing further is owed.

**Step 8 — `PROGRESS.md` session-log entry + cultural-sensitivity debt note.**
- ✅ Entry already added in this handoff bundle covering steps 1-4 + handoff.
- After steps 5-6 land, append a brief continuation note (or amend the existing entry) capturing §4.4a / §4.7 completion and the Jörmungandr-vs-Fenrir narrowing if PM picks one in-session.
- Cultural-sensitivity pass (Follow-up #5) remains a debt — reaffirm in PROGRESS Debts.

### Open sub-decisions waiting PM input

1. **Jörmungandr vs Fenrir** for Norse round-30 antagonist (Follow-up #11 on 2026-04-27 decision). Affects step 6 prose. Default if PM defers: keep "Jörmungandr OR Fenrir" plural in §4.7 with both options noted.
2. **§5.4 [LOCKED] amendment** to delete "Lineages" row + add "Civilizations" row (Follow-up #10 on 2026-04-27 decision). Confirmed-in-principle but still requires explicit PM "go" since §5.4 is [LOCKED]. NOT in scope for steps 5-8 — separate dedicated PM-gated turn.

### Background candidates (parked; pick up after commander pass closes)

- **Candidate A** — Prototype reshape plan ratification + execution. Ratify [`2026-04-26-prototype-reshape-plan.md`](decisions/2026-04-26-prototype-reshape-plan.md) (Proposed → Accepted, now with 2026-04-27 amendment), then execute C1→C2→C3→C4→C5→C7.a→C7.b→C6 one per turn.
- **Candidate B** — Cultural-sensitivity pass scheduling (Follow-up #5). Mandatory content-lock gate.
- **Candidate C** — Patch-1 commanders per civ (Follow-up #6).
- **Candidate D** — `admin/concept.json` migration path (rewrite / regenerate / retire).

### Prototype UX debt (not blocking)

First-time players stuck: `menuNewGame() → commander-pick → selectCommander()` never sets `Profile.data.lastMode`, so "Play" button never surfaces. **Workaround:** DevTools `Profile.data.lastMode = "skirmish"; Profile.save(); location.reload();`. Proper fix lives in reshape plan C2/C4.

---

## Open threads / carried debts

### Still open (priority order)

1. **Commander-as-summoned-ability-avatar steps 5-8** — primary next-session directive.
2. **Jörmungandr vs Fenrir sub-decision** (Follow-up #11).
3. **§5.4 amendment** (Follow-up #10) — Lineages → Civilizations row.
4. **Prototype reshape plan ratification** (Proposed, now amended).
5. **Cultural-sensitivity pass** (Follow-up #5) — mandatory content-lock gate.
6. **Patch-1 commanders per civ** (Follow-up #6).
7. **Myth-creature PvE bosses** (Follow-up #3).
8. **Title lock** (Q8) — "Mud to Myth" floated; not locked.
9. **Stage body rewrites** (01/03/04/05/06/07) — deferred to dedicated reopens.
10. **`admin/concept.json` full migration** — rewrite / regenerate / retire.
11. **Foresight-coin cross-civ borrowing** (Follow-up #7).
12. **PvE campaign + AGES + leveling + attributes** (Follow-up #8).
13. **Non-boss enemy ontology** (Follow-up #9).
14. **Styling / tone pass** (Follow-up #4).
15. **[PROPOSAL] balance-pass re-ratification** (Follow-up #13).

### LOCKED — do NOT touch

- `concept/phase-5.md §5.4` naming **conventions [LOCKED]** (amendment proposed via Follow-up #10 — wait for explicit PM "go").
- `concept/phase-2.md §2.4a` accessibility floor **[LOCKED]**.
- Mechanics surface (TD / merge / debuff / magic).
- Full 2026-04-25 locked content skeleton.
- Prototype files — no edits until PM ratifies reshape plan.

---

## Cadence rules carried forward

- **Default: one-step-at-a-time with PM "go" gates** per `CLAUDE.md`.
- **Dual-push discipline:** push to BOTH session branch AND `main` after every commit (when autonomy enabled).
- **Local-main hygiene:** `git fetch origin && git log --oneline HEAD..origin/main` BEFORE reading docs.
- **3x debug loop** inline on any CONCEPT-constraint-touching proposal.
- **Doc hygiene on each handoff:** trim PROGRESS.md to 3 entries, CASCADE.md pointer to 1 block, version footer to 2 bumps.

---

## Next-session prompt (copy-paste after `/clear`)

```
Resuming Ash to Altar — Commander-as-summoned-ability-avatar
plan-mode pass, steps 5-8 of 8.

BOOTSTRAP per CLAUDE.md order:
  README → CLAUDE → CASCADE → HANDOFF → PROGRESS → CONCEPT.

BEFORE reading docs, verify local main is current:
  git fetch origin
  git log --oneline HEAD..origin/main   # should be empty
  (If not, pull --ff-only before reading any doc.)

STATE ALOUD (before producing anything):
- Phase status + drift vs. last HANDOFF (2026-04-27 commander
  pass: steps 1-4 of 8 landed at commit 7fd3be8; steps 5-8
  queued).
- Primary open blocker: Commander-as-summoned-ability-avatar
  steps 5-8.
- Specific next-step proposal: open step 5 — propose
  concept/phase-4.md §4.4a Builder unit subsection insertion +
  §4.4 line-111 redaction, present diff, await PM "go".

CADENCE: default one-step-at-a-time with PM "go" gates.
Plan-mode pass continues. HARD AUTONOMY MODE is NOT in force.

PRIMARY DIRECTIVE — Commander-as-summoned-ability-avatar steps 5-8:
  Step 5: concept/phase-4.md §4.4a NEW Builder unit subsection
          (between §4.4 and §4.5) + redact §4.4 line 111 stale
          on-field-hero sentence with strikethrough+supersede note.
  Step 6: concept/phase-4.md §4.7 banner extension — historic
          match-arc beats solo-only + round-30 antagonist roster
          (Greek Xerxes I / Aztec two-phase Tlaxcalan→Tezcatlipoca
          pre-contact / Norse Jörmungandr-or-Fenrir) + cross-civ
          tonal-arc note.
  Step 7: CASCADE.md verification (already at v0.26 + new
          decisions-table row from this handoff — confirm
          nothing further owed after steps 5-6).
  Step 8: PROGRESS.md continuation note (already has steps 1-4
          entry from this handoff — append step 5-6 completion
          + cultural-sensitivity debt reaffirmation).

OPEN SUB-DECISIONS (PM input needed during step 6):
  - Jörmungandr vs Fenrir narrowing (Follow-up #11). If PM
    defers, keep both options plural in §4.7 prose.
  - §5.4 amendment (Follow-up #10) — Lineages → Civilizations
    row. NOT in scope for steps 5-8; dedicated PM-gated turn.

ACTIVE DIRECTION (locked 2026-04-25, exit one-pager 2026-04-26):
  Real cultures + native myth. Greek / Aztec / Norse.
  Commanders: Leonidas / Montezuma II / Ragnar Lothbrok.
  18 T1-T3 towers + 15 units + 18 T4 Demigods & Heroes.
  Fusion-to-Gods: 9 Gods via 9 locked 2-Demigod recipes.
  Tribute + Divinity (6 cap; 2 unlock menu + 1/fusion).
  30-wave lane-wars. 7-type × 5-armor RPS + status procs.

COMMANDER MODEL (locked 2026-04-27):
  Three surfaces: identity plinth / passive pip / active cast
  avatar (summoned-on-cast only). Three-tier cast budget
  ~1.2s/~2.8s/~4.5s. Builder = degenerate mobile-hero (no AI,
  no combat). 30-wave historic arc; round-30 = commander's
  historic antagonist (solo-only).

STOP AND HANDOFF when reaching:
  - Cultural-sensitivity concern (Follow-up #5).
  - §2.4a or §5.4 touch.
  - Locked-name change without PM.
  - Mechanics surface touch.
  - Prototype execution before reshape plan Accepted.

DO NOT:
  - Touch §2.4a or §5.4 conventions without explicit PM go.
  - Touch prototype files until reshape plan Accepted.
  - Assume HARD AUTONOMY MODE.
  - Change 2026-04-25 locked names without PM.
  - Re-execute steps 1-4 (already landed at commit 7fd3be8).
```

---

## Escalation triggers

Hard-stop and flag if:

- A proposed sub-decision would touch `§2.4a` or `§5.4` conventions without explicit PM "go".
- A proposed sub-decision would modify 2026-04-25 locked names without PM.
- A proposed sub-decision would touch mechanics (TD/merge/debuff/magic).
- A cultural-sensitivity concern surfaces (Follow-up #5).
- Prototype file edits proposed before PM ratifies reshape plan.
- Local `main` stale on session start.
- `cascade-lint` fails and fix > 5min.

---
