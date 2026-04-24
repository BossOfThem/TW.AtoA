# HANDOFF — Session Checkpoint

**Last session:** 2026-04-24 (Phase 1 vision reopen ratified by PM; no doc edits made — decisions captured, next session executes)
**Hand-off by:** Claude (Sonnet 4.6)
**Hand-off to:** next Claude Code session (post `/clear` or cloud-session reset)

---

## TL;DR (this session)

No commits landed this session — session was discovery + planning only. The PM confirmed a **Phase 1 vision reopen** (entire concept rehaul). Prior 2026-04-21 concept tightening (3/3/3 + dungeon cosmology + Ash-enabler, Reversibility Hard) is superseded in intent. The actual reopen decision file and cascade execution are the first items for the next session.

**PM decisions captured this session (no artifacts yet — captured here for next-session handoff):**

| # | Decision |
|---|----------|
| 1 | **Phase 1 vision reopen confirmed.** Full rehaul — vision, theme, 3/3/3 shape, dungeon cosmology, hybrid topology, title all on the table. Supersedes 2026-04-21. |
| 2 | **Mechanics stay.** TD / merge / debuff / magic mechanic surface untouched. |
| 3 | **Thematic direction: synthetic mythic-history braid.** Philosophy + real history + comparative religion + mythology combined into a single invented world — not pure history, not pure fantasy, not locked to one tradition. |
| 4 | **Age model deferred.** Don't decide "within-match vs. seasonal vs. campaign-chapters" until the story/background/world is established first. |
| 5 | **Locked items still locked.** §2.4a accessibility floor [LOCKED], §5.4 naming *conventions* [LOCKED] (specific names changeable), CASCADE cascade discipline, decision-log process. |
| 6 | **Step B plan (prototype reshape) superseded by rehaul.** It remains a Proposed doc but the 18-sub-step plan is now downstream of the vision reopen, not upstream of playtest. |

---

## State snapshot

### Git
- Branch in use: **`claude/resume-ash-to-altar-NMwFW`** (pushed; tracking origin).
- HEAD: **`bebcffc`** (HANDOFF/PROGRESS/CASCADE close from 2026-04-22 session).
- Working tree clean; cascade-lint clean.
- No PR opened.

### Artifacts delta this session
- 0 concept/ files touched.
- 0 prototype files touched.
- 0 decision files created.
- HANDOFF.md, PROGRESS.md, CASCADE.md updated in this commit only.

### Docs state
- All concept docs unchanged from 2026-04-22 state (3/3/3 + dungeon cosmology + Ash-enabler shape).
- That shape is now **pending reopen** per PM decision above — but no reopen decision file is filed yet. Next session files it first.

---

## Open threads / carried debts

### Highest priority (blocks everything)
- **Phase 1 vision reopen decision file** — must be filed before any concept edits. This supersedes 2026-04-21. Format: `decisions/2026-04-24-phase-1-vision-reopen-synthetic-mythic-history.md` (Reversibility Hard, 3x debug loop inline).

### Discovery sequence (Socratic, one question per turn — PM drives)
After the reopen decision is filed, proceed through these in order. Each produces one artifact.

1. **Q1 — Reopen decision filed.** (See above.)
2. **Q2 — World pitch.** What IS the world? Synthetic mythic-history braid — but what are its one-paragraph flavor rules? What makes the era system feel historic + religious + mythic simultaneously without being generic?
3. **Q3 — Actors.** Who is the Commander in this world? What are the lineages (how many, what do they represent)? What are towers — structures, spirits, summoned warriors? Are there sent-units/minions at all?
4. **Q4 — Match arc.** What story does one match tell in this world?
5. **Q5 — Age model.** (Now contextually answerable.) Within-match, seasonal, campaign, or braid?
6. **Q6 — Hybrid topology.** Does one lineage stay as "enabler"? Or any-pair hybrids? What does hybridizing MEAN in this world?
7. **Q7 — Economy.** What resources drive the game in the new frame?
8. **Q8 — Title.** Candidates under §5.4 conventions; 3x debug loop on options.
9. **Q9 — 3x debug loop** over the full rebuilt concept.
10. **Q10 — Ratification + cascade execution plan.** Which phase files update, which decisions rebase, which retire.

### LOCKED — do not touch
- `concept/phase-5.md §5.4` naming conventions [LOCKED] (specific names can change; *conventions* cannot).
- `concept/phase-2.md §2.4a` accessibility floor [LOCKED].
- Prototype + mechanics (no prototype edits until vision ratified + Step B plan re-filed for new shape).

### Freeze date
- 2026-05-15 was the prior Step B freeze. With vision reopen that date is soft — but next session should assess whether it's still achievable.

---

## Next-session prompt

```
Resuming Ash to Altar. 2026-04-24 session — Phase 1 vision reopen ratified by PM,
no doc edits yet. Bootstrap per CLAUDE.md: README → CLAUDE → CASCADE → HANDOFF
→ PROGRESS → CONCEPT. State aloud phase status + drift + next step, then WAIT for PM go.

CADENCE: ONE FILE PER TURN. Push to BOTH session branch AND main every commit.

WHAT THIS SESSION DECIDED (not yet in any doc except HANDOFF.md):
- Phase 1 vision reopen confirmed by PM. Supersedes 2026-04-21 (3/3/3 + dungeon
  cosmology + Ash-enabler, Reversibility Hard).
- Full rehaul: vision, theme, shape, hybrid topology, title all open.
- Mechanics stay (TD/merge/debuff/magic). §2.4a + §5.4 conventions stay [LOCKED].
- Thematic direction: synthetic mythic-history braid (history + comparative religion
  + mythology + philosophy — a single invented world with all four as raw material).
- Age model deferred: do not decide within-match vs. seasonal vs. campaign-chapters
  until story/background/world is established.
- Step B prototype-reshape plan (Proposed) is downstream of rehaul, not a priority.

FIRST MOVE NEXT SESSION:
  File decisions/2026-04-24-phase-1-vision-reopen-synthetic-mythic-history.md
  (Reversibility Hard, supersedes 2026-04-21, 3x debug loop inline).
  Then proceed to Q2 — World pitch.
  One question per turn, PM drives pacing.

DO NOT start reopen decision without PM "go".

LOCKED (do NOT touch):
- concept/phase-5.md §5.4 naming conventions [LOCKED].
- concept/phase-2.md §2.4a accessibility floor [LOCKED].
- Prototype files (no edits until vision ratified).
```

---

*End of HANDOFF — 2026-04-24. Phase 1 vision reopen ratified by PM; first artifact (reopen decision file) is next session's first move. Awaiting PM "go".*
