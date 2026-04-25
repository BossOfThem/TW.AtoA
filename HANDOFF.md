# HANDOFF — Session Checkpoint

**Last session:** 2026-04-27 — Commander-as-summoned-ability-avatar ALL 8 steps closed; §5.4 amendment queued with PM go.
**Hand-off by:** Claude (Sonnet 4.6)
**Hand-off to:** next Claude Code session (post `/clear`)

---

## TL;DR (this session)

**Commander-as-summoned-ability-avatar plan-mode pass fully closed.** All 8 steps landed across two same-day sessions. Final commit `09453d9` lands steps 5-8: §4.4a Builder unit class, §4.4 stale-sentence redaction, §4.7 Historic match-arc beats subsection with locked round-30 antagonist roster, and Follow-up #11 closed (Jörmungandr locked; Fenrir reserved post-launch). CASCADE v0.27. PM confirmed §5.4 amendment as next directive before calling handoff.

**Key ratifications this full pass:**
- **Three-surface commander model:** identity plinth / passive pip / active cast avatar.
- **Three-tier cast budget:** ~1.2s / ~2.8s / ~4.5s.
- **Builder unit class:** degenerate mobile-hero (single anim, no AI, no combat, walkable-build-grid distinct from enemy-path-grid).
- **Historic match-arc beats (solo-only):** round-30 antagonists — Xerxes I (Greek) / Tlaxcalan→Tezcatlipoca two-phase pre-contact (Aztec, Cortés OUT) / **Jörmungandr** (Norse, locked — Follow-up #11 closed; Fenrir post-launch).
- **Cross-civ tonal arc:** mortal → bridge → cosmic — intentional asymmetry.
- **Follow-up #11 CLOSED** at both anchors in the 2026-04-27 decision.

---

## Commits this session

- `7fd3be8` — steps 1-4 of 8 + lint-row (prior session).
- Handoff bundle — CASCADE v0.26 + PROGRESS entry (prior session).
- `09453d9` — steps 5-8 of 8 + Follow-up #11 closure (this session).
- This handoff commit — CASCADE "Next planned work" update + HANDOFF rewrite.

---

## State snapshot

### Git

- Branch: **`session/2026-04-25-q2-world-pitch`** dual-pushed to `main` at `09453d9` (plus this handoff commit).
- Working tree: clean except `.accord/` untracked.
- No PR opened.

### Phase status

- **Phase 1 thematic direction: RATIFIED** (real-world cultures + native myth — 2026-04-25).
- **Phase 1 exit one-pager: FILED** (2026-04-26).
- **Commander-as-summoned-ability-avatar: FULLY LANDED** (2026-04-27, all 8 steps, commit `09453d9`).
- **Follow-up #11 CLOSED** — Jörmungandr locked for Norse round-30; Fenrir reserved post-launch.
- **Prototype reshape plan** still **Proposed** (2026-04-27 amendment in tree) — awaiting PM ratification. Prototype files frozen.
- `§2.4a` + `§5.4` **[LOCKED]** — §5.4 amendment queued as next directive with PM go.

### Doc-hygiene state

- `PROGRESS.md` session log: 3 most recent entries maintained (continuation note appended inline to the 2026-04-27 entry rather than creating a 4th).
- `CASCADE.md` pointer: most recent block only (v0.27, all-8-landed state + updated "Next planned work").
- Bootstrap remains lean.

---

## NEXT SESSION — primary directive

**Execute §5.4 [LOCKED] amendment (Follow-up #10).** PM gave explicit "go" this session before handoff. Scope is narrow and fully specified — no open sub-decisions.

### What to do

1. **File `decisions/YYYY-MM-DD-phase-5-naming-conventions-lineages-row-deletion.md`** — decision entry per `decisions/TEMPLATE.md`:
   - Status: Accepted. Reversibility: Easy.
   - Scope: delete Lineages row from `concept/phase-5.md §5.4`; add Civilizations row; preserve Lineages convention in `CASCADE-history.md`. Cite Follow-up #10 from 2026-04-27 decision.
   - 3x debug loop (touches [LOCKED] surface — warrant the loop).

2. **Edit `concept/phase-5.md §5.4`:**
   - Delete the Lineages naming-convention row (one-syllable kenning: Sinew / Ember / Forge / Crown / Veil pattern).
   - Add a **Civilizations** row: convention = real-culture proper nouns; no invented placeholders; no one-syllable-kenning rule; naming convention is "the culture names itself" (Greek / Aztec / Norse at launch; expansions follow same pattern).
   - Add dated amendment banner at the top of §5.4 citing the new decision and Follow-up #10 lineage.

3. **Append to `CASCADE-history.md`** (under an "Archived naming conventions" section or similar) the original Lineages convention rule text for archival traceability.

4. **Update `CASCADE.md` decisions table** — add new row at top for the §5.4 decision entry.

5. **Append `PROGRESS.md` session log note** (or amend the most recent entry; doc-hygiene 3-most-recent rule applies).

6. **Commit + dual-push.** Then **stop** — do not continue to background candidates without PM.

### What NOT to touch

- Any other §5.4 row — only the Lineages row is in scope.
- Locked content-skeleton names from 2026-04-25 — those are under §5.4 conventions but are locked separately.
- Prototype files — reshape plan still Proposed.
- §2.4a — untouched always.

---

## Open threads / carried debts

### Priority order

1. **§5.4 [LOCKED] amendment** (Follow-up #10) — **PM go given; next session primary directive.**
2. **Prototype reshape plan ratification** (Proposed, 2026-04-27 amendment in tree) — then C1→C7 execution.
3. **Cultural-sensitivity pass** (Follow-up #5) — mandatory content-lock gate.
4. **Patch-1 commanders per civ** (Follow-up #6).
5. **Myth-creature PvE bosses** (Follow-up #3).
6. **Title lock** (Q8) — "Mud to Myth" floated; not locked.
7. **Stage body rewrites** (01/03/04/05/06/07) — deferred to dedicated reopens.
8. **`admin/concept.json` full migration** — rewrite / regenerate / retire.
9. **Foresight-coin cross-civ borrowing** (Follow-up #7).
10. **PvE campaign + AGES + leveling + attributes** (Follow-up #8).
11. **Non-boss enemy ontology** (Follow-up #9).
12. **Styling / tone pass** (Follow-up #4).
13. **[PROPOSAL] balance-pass re-ratification** (Follow-up #13).

### LOCKED — do NOT touch

- `concept/phase-5.md §5.4` naming **conventions [LOCKED]** — §5.4 amendment is the ONE permitted touch next session, scoped to Lineages row only.
- `concept/phase-2.md §2.4a` accessibility floor **[LOCKED]**.
- Full 2026-04-25 locked content skeleton.
- Prototype files — no edits until PM ratifies reshape plan.

---

## Cadence rules carried forward

- **Default: one-step-at-a-time with PM "go" gates** per `CLAUDE.md`.
- **Dual-push discipline:** push to BOTH session branch AND `main` after every commit.
- **Local-main hygiene:** `git fetch origin && git log --oneline HEAD..origin/main` BEFORE reading docs.
- **3x debug loop** on any CONCEPT-constraint-touching proposal.
- **Doc hygiene on each handoff:** trim PROGRESS.md to 3 entries, CASCADE.md pointer to 1 block, version footer to 2 bumps.

---

## Next-session prompt (copy-paste after `/clear`)

```
Resuming Ash to Altar — §5.4 naming-conventions amendment (Follow-up #10).

BOOTSTRAP per CLAUDE.md order:
  README → CLAUDE → CASCADE → HANDOFF → PROGRESS → CONCEPT.

BEFORE reading docs:
  git fetch origin
  git log --oneline HEAD..origin/main   # should be empty

STATE ALOUD (before producing anything):
- Phase status + drift vs. last HANDOFF (commander pass fully
  closed at 09453d9; Follow-up #11 closed — Jörmungandr locked;
  §5.4 amendment queued with PM go given).
- Primary directive: §5.4 [LOCKED] amendment (Follow-up #10).
- Specific next-step: file dedicated decision entry for Lineages
  row deletion + Civilizations row addition; propose draft +
  3x debug loop; await PM "go" to execute phase-5.md edit.

CADENCE: one-step-at-a-time with PM "go" gates. STOP after
§5.4 amendment commit + dual-push — do not continue to
background candidates without PM.

PRIMARY DIRECTIVE — §5.4 amendment (Follow-up #10):
  1. File decisions/YYYY-MM-DD-phase-5-naming-conventions-
     lineages-row-deletion.md (Accepted, Easy, 3x debug loop).
  2. Edit concept/phase-5.md §5.4 — delete Lineages row, add
     Civilizations row, add dated amendment banner.
  3. Append archived Lineages convention to CASCADE-history.md.
  4. Update CASCADE.md decisions table (new row at top).
  5. Append PROGRESS.md session note.
  6. Commit + dual-push. STOP.

SCOPE GUARD: only the Lineages row in §5.4 is in scope.
No other §5.4 rows. No prototype files. §2.4a untouched.
2026-04-25 locked names untouched.

BACKGROUND CANDIDATES (do NOT start without PM):
- Prototype reshape plan ratification + C1→C7 execution.
- Cultural-sensitivity pass scheduling (Follow-up #5).
- Patch-1 commanders per civ (Follow-up #6).
```

---

## Escalation triggers

Hard-stop and flag if:

- Any §5.4 row beyond Lineages is touched.
- 2026-04-25 locked names would be modified.
- §2.4a is touched.
- Cultural-sensitivity concern surfaces (Follow-up #5).
- Prototype file edits proposed before PM ratifies reshape plan.
- Local `main` stale on session start.
- `cascade-lint` fails and fix > 5min.
