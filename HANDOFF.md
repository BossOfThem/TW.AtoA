# HANDOFF — Session Checkpoint

**Last session:** 2026-05-05 → 2026-05-06 (**clear-safe**).
**Hand-off by:** Claude (Opus 4.7)
**Hand-off to:** next Claude Code session after `/clear`.

---

## TL;DR

**Phase B of the prototype UI verification sweep LANDED (`1b81f45` + `2d2a406`, dual-pushed).** All 5 small NEEDS-FIX applied + verified live via preview MCP; medium #7 (profile roster from `COMMANDERS.roster`) ratified by PM and landed. Live walk of (Test) rows updated in place. Report carrier still [`prototype/UI-VERIFICATION-2026-05-05.md`](prototype/UI-VERIFICATION-2026-05-05.md). NEXT session executes **Phase C — remaining medium/large queue, Recommended-first**.

---

## NEXT SESSION — primary directive (Phase C)

Phase A + Phase B are DONE. Carrier is still [`prototype/UI-VERIFICATION-2026-05-05.md`](prototype/UI-VERIFICATION-2026-05-05.md). Read it, then pick the next item from the queue.

### Phase C — medium/large NEEDS-FIX queue (remaining)

Queue (Recommended-first, top is recommended starting point):

1. **Medium #8 — end-screen XP doesn't persist.** `renderEnd` mutates `COMMANDERS.roster[cid].progression` only; it never writes back to `Profile.data.commanderProgress`. Result: XP awarded in-match evaporates on reload. Fix: after the in-memory progression mutation, `Profile.data.commanderProgress[cid] = { xp, level }` and `Profile.save()`. **Recommended first** — small, contained, no scene-flow risk, restores intended persistence.
2. **Medium #6 — input rebind UI decorative.** Match `keydown` (around ln 3537) hardcodes keys; rebound bindings in `Profile.setting("input.binds")` are written but never read at dispatch. Fix: thread `Profile.setting("input.binds")` through the keydown handler with sensible defaults. Larger surface than #8 — touches input dispatch.
3. **Large #9 — `A` (age-up) key absent from match keydown handler.** Was it intentionally retired or did it regress? **Requires PM intent call before any fix.** Check decisions/ + concept §4 for AGE mechanic status.
4. **Large #10 — end-screen Continue / Replay / Menu mismatch.** Markup has 2 buttons; scene-checklist promises 3. **Requires PM intent call** on which is canonical (markup or checklist) before any fix.

Each item: propose → PM "go" → apply → verify live in preview MCP → commit (dual-push). After Recommended #8 lands, AskUserQuestion to PM for #6 vs #9 vs #10 next pick.

### Live-verify discipline (carry from Phase B)

- Preview server runs from `.claude/launch.json` config `prototype` (port **8766**, since 8765 is occupied on this machine). Start with the launch config or `python -m http.server 8766` from repo root and load `http://localhost:8766/prototype/index.html`.
- Use `mcp__Claude_Preview__preview_*` tools for click/eval/screenshot. `COMMANDERS` is closed over inside the prototype IIFE — use `window.goto()` / `window.renderCommanderRoster()` helpers exposed at top level for navigation/state probing.
- Update report Status in place via Edit (not Write).
- Commit per fix or per ~3-fix batch. Dual-push every commit.

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

### NEW this session (Phase B)

- 5 small inline fixes in `prototype/index.html` — Highest-Age row dropped from end screen; tutorial Esc → menu wired; `saveAndExit` toasts mode-aware (campaign saves; skirmish/co-op explicitly toast non-autosave per §4.9); `menu-last` lineage resolves via `COMMANDERS.roster[id].civ` with legacy fallback; `CAST_DURATIONS.long` dead key removed.
- Medium #7 — Profile scene roster sourced from `COMMANDERS.roster` filter `playable:true` (no more legacy hardcode).
- `.claude/launch.json` added with `prototype` config on port **8766** (machine-specific — 8765 occupied).

---

## State snapshot

### Git

- Branch: **`session/2026-04-25-q2-world-pitch`**.
- Latest commits: **`2d2a406`** (medium #7), **`1b81f45`** (small-fix batch 5/5), `e73a2f9` (handoff prep A→B), `caa1e61` (Phase A report). All dual-pushed.
- Working tree at handoff: doc-hygiene bundle (PROGRESS / CASCADE / archives / HANDOFF) staged for the chore commit. `.accord/` untracked.

### Doc-hygiene state

- `PROGRESS.md` session log: 3 most-recent entries (Phase B / Phase A landed / handoff prep A→B). Older archived to `PROGRESS-archive.md`.
- `CASCADE.md` pointer: 1 most-recent block (Phase B LANDED). Prior pointer (Phase A LANDED) archived to `CASCADE-history.md`.
- `CASCADE.md` version footer: 0.64 + 0.63. Older (0.62 / 0.61 / etc.) archived.
- cascade-lint expected clean except pre-existing `concept/phase-4.md` 626/600 soft-cap (carried — not introduced by this handoff).

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

- Tutorial Esc dismissal (just wired — re-verify next session sanity).
- Profile scene roster (just re-sourced — re-verify L/XP rendering still correct after page reload, not just live nav).
- End-screen layout post-Highest-Age row removal — confirm no orphan styling.
- `menu-last` resolution path — confirm civ glyph correct for all three real-cultures commanders + legacy fallback path.

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
Resuming Ash to Altar. Phase B of the prototype UI verification sweep
LANDED (1b81f45 + 2d2a406, dual-pushed). All 5 small fixes applied + medium
#7 (profile roster from COMMANDERS) landed. Report carrier:
prototype/UI-VERIFICATION-2026-05-05.md. NEXT session executes Phase C.

BOOTSTRAP per CLAUDE.md: README → CLAUDE → CASCADE → HANDOFF → PROGRESS.
Then read prototype/UI-VERIFICATION-2026-05-05.md (the report).

BEFORE reading docs:
  git fetch origin
  git log --oneline HEAD..origin/main   # should be empty

PRIMARY DIRECTIVE — Phase C (remaining medium/large queue):
1. Start preview server via .claude/launch.json `prototype` config
   (port 8766 — 8765 is occupied on this machine) or
   python -m http.server 8766 from repo root, then load
   http://localhost:8766/prototype/index.html.
2. RECOMMENDED FIRST — Medium #8: end-screen XP persist.
   renderEnd mutates COMMANDERS.roster[cid].progression but never writes
   Profile.data.commanderProgress. Fix: after the in-memory mutation,
   Profile.data.commanderProgress[cid] = { xp, level } and Profile.save().
   Verify live: play a match → win → reload → confirm XP persisted.
   Commit + dual-push. Update report row in place.
3. Then AskUserQuestion to PM for next pick: Medium #6 (input rebind
   wiring through keydown) vs Large #9 (A age-up intent call) vs
   Large #10 (end-screen 2-vs-3 button mismatch intent call).
   Large items REQUIRE PM intent ratification before any fix.

CADENCE GUARDRAILS (per PM ask, soft):
- Batch parallel reads; prefer Grep over full-file reads.
- Prefer preview_eval over preview_screenshot for state probes.
- Archive findings to the report file, not chat context.
- Commit per fix; dual-push every commit.

REGRESSION-WATCH: tutorial Esc; profile roster L/XP after reload;
end-screen layout post-Highest-Age removal; menu-last civ glyph
across all three real-cultures commanders + legacy fallback.

VERIFY each commit with: python tools/cascade-lint.py
DUAL-PUSH each commit: session branch + main.

SCOPE GUARD:
- §5.4 [LOCKED]; §2.4a [LOCKED]; locked content skeleton untouched.
- 17-item frame + extension (s) Accepted.
- All Numbers-phase magnitudes Accepted.
- All R1-R7 CONCEPT amendment-pass §-anchors Accepted.
- All per-commander R1-R5 spine-doc edits Accepted.
- Effect-type lane locks Hard reversibility.
- Cultural-sensitivity Follow-up #5 still hard-gates non-abstract civ art.

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
- A Phase C fix touches large severity without PM ratification.
- Context budget pressure forces a mid-phase split → file mini-handoff and stop cleanly.
