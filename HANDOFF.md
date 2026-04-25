# HANDOFF — Session Checkpoint

**Last session:** 2026-04-28 — §5.4 [LOCKED] amendment LANDED; Follow-up #10 CLOSED.
**Hand-off by:** Claude (Opus 4.7)
**Hand-off to:** next Claude Code session (post `/clear`)

---

## TL;DR (this session)

**§5.4 [LOCKED] amendment fully landed in one tight pass.** Commit `dd97672` on `session/2026-04-25-q2-world-pitch`, dual-pushed to `main`. Decision filed at [`decisions/2026-04-28-phase-5-naming-conventions-lineages-row-deletion.md`](decisions/2026-04-28-phase-5-naming-conventions-lineages-row-deletion.md) (Accepted, Reversibility **Easy**, 3x debug loop inline because [LOCKED] surface). Lineages row (one-syllable kenning: Sinew / Ember / Forge / Crown / Veil) deleted from `concept/phase-5.md §5.4` and `CONCEPT.md §5.4` hub mirror. Replaced with **Civilizations** row: real-culture proper nouns; the culture names itself; Greek / Aztec / Norse at launch; expansions follow the same pattern. Original Lineages convention archived verbatim to `CASCADE-history.md` under new "Archived naming conventions" section. CASCADE.md decisions table gained new top row; pointer rewritten; prior 2026-04-27 pointer block archived to history; version v0.27 → v0.28. PROGRESS.md session note appended; oldest entry (2026-04-26 session close) archived to `PROGRESS-archive.md`. cascade-lint clean throughout.

**Key ratifications this session:**
- **§5.4 row swap:** Lineages OUT, Civilizations IN. The Civilizations convention positively forbids invented placeholders and constrains expansion to real cultures.
- **Audit of the seven retained §5.4 rows** (Game title / Commanders / Ages / Towers/Units / Hybrids / Enemies / Heirlooms / Modes) confirmed neutral to the real-cultures frame — no further amendments warranted.
- **Follow-up #10 CLOSED** at the 2026-04-27 commander-as-summoned-ability-avatar decision and at this new decision entry.

---

## Commits this session

- `dd97672` — §5.4 amendment full bundle (decision + phase-5.md + CONCEPT.md hub + CASCADE.md + CASCADE-history.md + PROGRESS.md). Dual-pushed.
- This handoff commit — HANDOFF rewrite + PROGRESS oldest-entry archive trim.

---

## State snapshot

### Git

- Branch: **`session/2026-04-25-q2-world-pitch`** dual-pushed to `main` at `dd97672` (plus this handoff commit).
- Working tree: clean except `.accord/` untracked.
- No PR opened.

### Phase status

- **Phase 1 thematic direction: RATIFIED** (real-world cultures + native myth — 2026-04-25).
- **Phase 1 exit one-pager: FILED** (2026-04-26).
- **Commander-as-summoned-ability-avatar: FULLY LANDED** (2026-04-27, 8 steps).
- **§5.4 [LOCKED] amendment: FULLY LANDED** (2026-04-28, this session).
- **Follow-up #10 CLOSED.** Follow-up #11 closed prior session.
- **Prototype reshape plan** still **Proposed** (2026-04-27 amendment in tree) — awaiting PM ratification. Prototype files frozen.
- `§2.4a` + `§5.4` **[LOCKED]** — §5.4 has now received its one permitted amendment (Lineages row only).

### Doc-hygiene state

- `PROGRESS.md` session log: 3 most recent entries maintained (2026-04-28 + two 2026-04-27); 2026-04-26 entry archived this handoff.
- `CASCADE.md` pointer: most recent block only (v0.28, §5.4 amendment landed); prior 2026-04-27 pointer archived to history.
- `CASCADE.md` version footer: 2 most recent bumps only (v0.28 + v0.27 reference).
- Bootstrap remains lean.

---

## NEXT SESSION — primary directive

**No specific PM-go directive carried forward.** Background candidates queue is the menu; pick with PM at session start.

### Background candidates (priority order)

1. **Prototype reshape plan ratification** — [`decisions/2026-04-26-prototype-reshape-plan.md`](decisions/2026-04-26-prototype-reshape-plan.md) is Proposed with 2026-04-27 amendment (C4 Cast bar + C7.a/b). Ratify (Proposed → Accepted), then begin C1 → C2 → C3 → C4 → C5 → C7.a → C7.b → C6. Largest unblock for prototype work.
2. **Cultural-sensitivity pass scheduling (Follow-up #5)** — Mandatory content-lock gate. Per-civ name + visual review for Greek / Aztec / Norse. No code dependency; pure scoping + scheduling.
3. **Patch-1 commanders per civ (Follow-up #6)** — Design 2nd commander per civ for first post-launch patch. Pure design; no [LOCKED] surfaces touched.
4. **Myth-creature PvE bosses (Follow-up #3)** — Round-30 antagonists locked (Xerxes / Tlaxcalan→Tezcatlipoca / Jörmungandr); design per-round mini-boss cadence (rounds 5/15/25 sketched in §4.7).
5. **Title lock (Q8)** — "Mud to Myth" floated; not locked.
6. **Stage body rewrites** (01/03/04/05/06/07) — deferred; reopen with discipline.
7. **`admin/concept.json` migration** — rewrite / regenerate / retire.
8. **Foresight-coin cross-civ borrowing (Follow-up #7).**
9. **PvE campaign + AGES + leveling + attributes (Follow-up #8).**
10. **Non-boss enemy ontology (Follow-up #9).**
11. **Styling / tone pass (Follow-up #4).**
12. **[PROPOSAL] balance-pass re-ratification (Follow-up #13).**

### LOCKED — do NOT touch

- `concept/phase-5.md §5.4` naming **conventions [LOCKED]** — the Lineages-row amendment is now LANDED (2026-04-28). No further §5.4 row changes without a new dedicated [LOCKED]-amendment decision.
- `concept/phase-2.md §2.4a` accessibility floor **[LOCKED]**.
- Full 2026-04-25 locked content skeleton.
- Prototype files — no edits until PM ratifies reshape plan.

---

## Cadence rules carried forward

- **Default: one-step-at-a-time with PM "go" gates** per `CLAUDE.md`.
- **AskUserQuestion tool for PM gates** with "Recommended" first option (PM directive 2026-04-28).
- **Dual-push discipline:** push to BOTH session branch AND `main` after every commit.
- **Local-main hygiene:** `git fetch origin && git log --oneline HEAD..origin/main` BEFORE reading docs.
- **3x debug loop** on any CONCEPT-constraint-touching proposal.
- **Doc hygiene on each handoff:** trim PROGRESS.md to 3 entries, CASCADE.md pointer to 1 block, version footer to 2 bumps.

---

## Next-session prompt (copy-paste after `/clear`)

```
Resuming Ash to Altar — open menu of background candidates.

BOOTSTRAP per CLAUDE.md order:
  README → CLAUDE → CASCADE → HANDOFF → PROGRESS → CONCEPT.

BEFORE reading docs:
  git fetch origin
  git log --oneline HEAD..origin/main   # should be empty

STATE ALOUD (before producing anything):
- Phase status + drift vs. last HANDOFF (§5.4 amendment landed
  at dd97672; Follow-up #10 CLOSED; Follow-ups #5/#6/#7/#8/#9
  remain open; prototype reshape plan still Proposed).
- No specific PM-go directive carried forward. Open menu.
- Specific next-step proposal: surface the background-candidates
  list via AskUserQuestion with the highest-leverage option marked
  Recommended (default Recommended: Prototype reshape plan
  ratification, since it's the largest unblock and the next
  natural step after the conceptual pass closed).

CADENCE: one-step-at-a-time with PM "go" gates.
USE AskUserQuestion for PM gates; always include a Recommended
first option per 2026-04-28 PM standing directive.

BACKGROUND CANDIDATES (PM picks one):
- Prototype reshape plan ratification + C1→C7 execution.
- Cultural-sensitivity pass scheduling (Follow-up #5).
- Patch-1 commanders per civ (Follow-up #6).
- Myth-creature PvE bosses (Follow-up #3).
- Title lock (Q8) — "Mud to Myth" candidate.
- Stage body rewrites (01/03/04/05/06/07).
- admin/concept.json migration.
- Follow-ups #7 / #8 / #9 / #4 / #13.

SCOPE GUARD: §5.4 [LOCKED] post-amendment; §2.4a [LOCKED];
2026-04-25 locked names untouched; prototype frozen pending
reshape ratification.
```

---

## Escalation triggers

Hard-stop and flag if:

- §5.4 row beyond Lineages would be touched.
- 2026-04-25 locked names would be modified.
- §2.4a is touched.
- Cultural-sensitivity concern surfaces (Follow-up #5).
- Prototype file edits proposed before PM ratifies reshape plan.
- Local `main` stale on session start.
- `cascade-lint` fails and fix > 5min.
