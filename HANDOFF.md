# HANDOFF — Session Checkpoint

**Last session:** 2026-05-05 (**clear-safe**).
**Hand-off by:** Claude (Opus 4.7)
**Hand-off to:** next Claude Code session after `/clear`.

---

## TL;DR

**Phase A of the prototype UI verification sweep LANDED (`caa1e61`, dual-pushed).** All 11 scenes walked statically; report filed at [`prototype/UI-VERIFICATION-2026-05-05.md`](prototype/UI-VERIFICATION-2026-05-05.md) with prioritized fix queue (5 small + 3 medium + 2 large NEEDS-FIX, ~25 (Test) rows for Phase B). NEXT session executes **Phase B — live in-browser sweep + small-fix loop**.

---

## NEXT SESSION — primary directive (Phase B)

Phase A is DONE (`caa1e61`). The carrier is [`prototype/UI-VERIFICATION-2026-05-05.md`](prototype/UI-VERIFICATION-2026-05-05.md). Next session reads that file and goes straight to Phase B.

### Phase B — Live in-browser sweep + small-fix loop

1. Start `prototype/start.bat` (or `python -m http.server 8765` from `prototype/`).
2. Load Claude-in-Chrome or preview MCP against `http://localhost:8765/prototype/index.html`.
3. Walk every (Test) row in the report (~25) plus a representative sample of OK rows. For each: update Status in place via Edit (Test → OK or Test → NEEDS-FIX). New NEEDS-FIX discovered live → add a row.
4. **Small NEEDS-FIX queue** (fix inline, commit per ~3-fix batch, dual-push):
   - end-screen "Highest Age" `undefined` (populate or drop the row)
   - tutorial Esc dead (extend global keydown ln 956 to include `tutorial`)
   - `saveAndExit` toasts "Saved." for skirmish (gate to campaign)
   - `menu-last` lineage map stale (resolve via `COMMANDERS.roster[id].civ`)
   - `CAST_DURATIONS.long` dead key (remove or wire)
5. **Medium NEEDS-FIX queue** (do NOT fix — surface in AskUserQuestion at end of B):
   - input-rebind UI decorative (match keydown ln 3537 hardcodes keys; consult `Profile.setting("input.binds")` instead)
   - profile scene roster hardcodes legacy commanders (source from `COMMANDERS.roster` filter `playable:true`)
   - end-screen XP doesn't persist (mutates `COMMANDERS.roster.progression` only, never writes `Profile.data.commanderProgress`)
6. **Large NEEDS-FIX queue** (require PM ratification before any fix):
   - `A` (age-up) key absent from match keydown handler — was it intentionally retired or did it regress?
   - end-screen Continue / Replay / Menu mismatch — markup has 2 buttons, scene-checklist promises 3
7. End Phase B with AskUserQuestion to PM listing the queued medium+large items with a Recommended pick.

### Original Phase A directive (kept for reference)

Read `prototype/index.html` plus the `prototype/data/*.json` files. For every interactive element across all 11 scenes (splash / login / menu / profile / mode-select / lobby-coop / commander-pick / tutorial / match / end / options) record one row in a single Markdown report:

| Scene | Element | Handler / source | Status | Note |
|-------|---------|-------------------|--------|------|
| match | Send-Wave button | `onSendWaveClick()` line ~XXX | OK | Disabled while `waveActive` per intended spec |
| match | Q key (commander cast-passive) | `keydown` line ~XXX | (Test) | Post-C7.a comment-out — verify still inert in browser |
| ... | ... | ... | ... | ... |

**Status legend:**
- **OK** — verified working as designed by reading the code path end-to-end.
- **(Test)** — code path exists but behavior is ambiguous, conditional on runtime state, or depends on something static analysis can't confirm. Carry into Phase B.
- **NEEDS-FIX** — code is broken, dead, regressed, or contradicts the intended spec from CONCEPT / decisions / prior commits.

Output file: `prototype/UI-VERIFICATION-2026-05-MM.md` (use today's date once known). Single file. Don't sprawl across multiple docs.

End Phase A with: prioritized fix queue at the bottom of the report (NEEDS-FIX first, then (Test) ranked by player-facing severity).

**Commit at end of Phase A** (single commit — `feat(prototype): UI verification sweep phase A static-analysis report`). Dual-push.

### Phase B — Live in-browser sweep + small-fix loop

Use Claude-in-Chrome or preview MCP. Start `prototype/start.bat` first (or `python -m http.server 8765` in `prototype/`). Then walk the (Test) rows and a sample of OK rows to confirm. For each row:

- (Test) → OK or (Test) → NEEDS-FIX based on observed behavior. Update the report in place (Edit, not Write).
- New NEEDS-FIX discovered live → add row to report.
- **Small NEEDS-FIX** (typo / dead handler reference / off-by-one / one-line CSS / missing aria-label / broken selector): **fix inline** as you find them. Commit per ~3-fix batch. Dual-push each batch.
- **Medium / large NEEDS-FIX** (touches game logic / data shape / scene flow / requires PM call on intended behavior): leave in queue, do not fix. Surface in AskUserQuestion at end.

End Phase B with: AskUserQuestion to PM listing the queued medium/large NEEDS-FIX items with a Recommended pick for which to tackle next.

### Scene checklist (carried from first handoff — all 11)

1. **Splash** — auto-advance after 3s; click-to-dismiss; any-key-to-dismiss; reduce-motion respected. (Splash dismiss verified post-fix; re-verify is sanity check.)
2. **Login** — username entry; "Continue as Guest"; Enter-key submit; localStorage `atoA.profile.v1` write; existing-profile detect → Returning branch.
3. **Menu** — greeting reflects username; Continue / Play / Commander / Options / Logout / Quit; keyboard nav.
4. **Profile** — XP bar; cosmetic-slot rendering; Back-to-menu; profile-clear option; mode-gated `writeMatchSave` annotation.
5. **Mode-select** — Skirmish / Tutorial / Co-op Horde / Campaign-stub cards; hover state; selection commit; back.
6. **Lobby-coop** — host invite-code generation; `?join=<peerID>` URL paste path; ready-state toggle; host-start gate; chat 100-char limit; disconnect flow.
7. **Commander-pick** — 5 legacy + 3 civ portraits; XP progress; cosmetic L5/L10/L15 lock badges; pick commit; back; `?silhouette-test=1`.
8. **Tutorial** — Skip → menu; build-glow affordance; sequenced prompts; codex (📖) button → modal opens with 7×5 RPS grid; Esc closes.
9. **Match** — Send-Wave (Space); pause (Esc); age-up (A); tower-select 1-5; placement; merge-preview ghost; T3 promote `↑`; right-click sell + targeting; Tribute / Divinity / lives HUD; Fusion HUD button (≥2 Div); Cast Bar 3 buttons; Codex; toast feed; combat feed; chat (co-op); reduce-motion; UI-scale slider.
10. **End-of-match** — Victory / Defeat banner; XP award (40 win / 12 loss); auto-level-up toasts; Continue / Replay / Menu; co-op host broadcast `match-end` sync.
11. **Options** — 5 tabs (Audio / Input / Video / Accessibility / Gameplay): sliders + toggles persisted; rebind capture; UI-scale 75-150%; colorblind-glyph toggle; Apply / Reset / Back.

### Cross-cutting checks

- **Keyboard shortcuts global:** Space / A / 1-5 / Esc / Q (post-C7.a inert) / C (post-C7.a inert).
- **Console clean** — no SyntaxError, no unhandled promise rejections, no fetch 404s (favicon 404 known-cosmetic).
- **Data fetches** — `prototype/data/{balance,civilizations,fusion-recipes,attack-types,tiers,commanders,enemies}.json` all 200. **Verify in-browser whether `civilizations.json` actually contains commanders-shaped data** (flagged previously as possible curl-output-ordering artifact; needs Phase B confirmation).
- **Co-op snapshot/intent loop** — host snapshot at 10Hz; guest intents drained per tick; guest-owned towers dashed-white border; net status badge.
- **Mode-aware pause** — Resume / Options / Restart / Save-and-Exit / Quit per mode.

---

## Cadence guardrails (per PM ask — soft, not hard)

PM ask: *"a cadence that avoids over loading API and causing errors, also keep context window in check softly."*

### API-overload avoidance

- **Batch parallel reads** — when reading several files for a scene's verification, send all Read calls in a single message (parallel tool calls), not sequentially.
- **Prefer Grep over full-file reads** — `prototype/index.html` is large. For a scene check, Grep for the scene's id / function names first, then Read with `offset` + `limit` around the hits. Don't read the whole file unless you genuinely need it (and you usually don't — the splash-fix this session was diagnosed via Grep + targeted Read).
- **Don't re-read files already in context** — the harness tracks file state. If you already Read it this session and haven't edited it elsewhere, your context already has it.
- **Keep tool calls per turn modest** — 3-6 well-chosen calls beats 15 scatter-shot ones.

### Soft context-window discipline

- **Archive findings to the report file, not into chat context.** Each scene's findings → Edit into `UI-VERIFICATION-*.md` immediately, then move to the next scene. Don't accumulate scene reports in your turn output.
- **Use Edit not Write** for incremental report updates after the initial Write that creates the file.
- **Summarize-and-discard intermediate scratch.** If you grep-and-read 200 lines to verify one handler, write the conclusion to the report and move on; don't quote 200 lines back in chat.
- **Periodically self-check budget.** If a scene took heavy investigation, take a quick pulse before starting the next one — if budget feels tight, file a mini-handoff at the end of Phase A and let Phase B happen in a separate session.
- **Acceptable to split A and B across two sessions** if budget pressure is real. Phase A's report file is the carrier between them; the second session reads the report and starts Phase B from there.

### Commit cadence

- **Phase A:** single commit at end of phase. Don't churn intermediate report drafts.
- **Phase B:** commit per ~3-scene live-verification batch, AND per ~3-fix batch when fixing inline. So a typical Phase B session might have 4-8 commits. Each one dual-pushed.
- **Never amend.** Pre-commit hook failure → fix and create a NEW commit.

### Fix-in-flight discipline

| Severity | Examples | Action |
|----------|----------|--------|
| Tiny | Typo in label / missing aria / one-line CSS / dead variable | Fix inline immediately, mention in report |
| Small | Single-handler bug / off-by-one / wrong CSS class / broken selector | Fix inline within Phase B, commit in batch |
| Medium | Touches game logic / data shape / multi-handler interaction | Queue to AskUserQuestion at end of Phase B |
| Large | Touches scene flow / requires PM call on intended behavior / cross-arc cascade | Queue to AskUserQuestion; do NOT fix without ratification |

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

### NEW this session

Doc-hygiene only. No code or spine-doc surfaces touched.

---

## State snapshot

### Git

- Branch: **`session/2026-04-25-q2-world-pitch`**.
- Latest commit: **`caa1e61`** — Phase A static-analysis report (dual-pushed).
- Prior commits: `e964cf5` (handoff prep), `2edb70c` (first handoff), `90f6f1c` (splash-fix), `6069c49` (per-commander arc close).
- Working tree clean; `.accord/` untracked.

### Doc-hygiene state

- `PROGRESS.md` session log: 3 entries (handoff prep / per-commander arc + splash-fix / CONCEPT amendment-pass arc). R10 archived.
- `CASCADE.md` pointer: 1 most-recent block (handoff prep A→B). Prior pointer archived to `CASCADE-history.md`.
- `CASCADE.md` version footer: 0.62 + 0.61. Older (0.60 / 0.59 / etc.) archived.
- cascade-lint expected clean except pre-existing `concept/phase-4.md` 626/600 soft-cap (carried from per-commander R5 spine-doc edits — not introduced by this handoff).

### Open follow-ups (carried — UNCHANGED)

- **#5** — Cultural-sensitivity pass (gates non-abstract civ art).
- **#6** — Patch-1 commanders per civ + Thor recipe-layer dissonance.
- **#7** — Foresight-coin / PvE campaign / AGES / leveling / attributes.
- **#8 / #9** — non-boss enemy ontology / additional commanders.
- **C7.b deferred** — Builder concurrency cap + 90% refund-on-cancel UI.
- **`admin/concept.json` staleness** — long-deferred.
- **`research/06-tw-subgenres.md`** new stub.

### Authoring sub-passes / roadmap (post-arc — preserve in any forward proposal)

1. **Per-tower** — bind cd / range / attack-type / status-proc across 18 T1-T3 + 18 T4 Demigod + 9 God towers across 3 civs. Per-tower target-side hooks already specified by per-commander arc.
2. **Per-civ specialization** — Greek / Aztec / Norse identity profiles. Intersects Follow-up #5 cultural-sensitivity gate.
3. **Per-map / Round 11** — good-cell authoring + wave-randomization + crystal-lock variance per §4.7 R11 mandate.
4. **Phase 5 readiness gate** — engine-side telemetry per §6.5 + wave variance per §4.7 R11.
5. **`research/06-tw-subgenres.md`** new stub.
6. **`admin/concept.json`** migration direction.

### Regression-watch

- Tutorial / match flow / merge-preview / Promote-T4 indicator / Aztec glyph (◈) / `logBalanceCurve` / `effectiveTowerStats` / snapshot.
- **Codex modal** post-splash-fix (rename touched `openCodex()` references) — Phase B should explicitly verify modal opens + 7×5 grid renders.
- Data-loaded `ATTACK_TYPES` shape feeds in-match RPS multipliers — Phase B should verify multiplier math observable in damage numbers.

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

---

## Next-session prompt (copy-paste after `/clear`)

```
Resuming Ash to Altar. Phase A of the prototype UI verification sweep
LANDED (caa1e61, dual-pushed). Report carrier:
prototype/UI-VERIFICATION-2026-05-05.md. NEXT session executes Phase B.

BOOTSTRAP per CLAUDE.md: README → CLAUDE → CASCADE → HANDOFF → PROGRESS.
Then read prototype/UI-VERIFICATION-2026-05-05.md (the report).

BEFORE reading docs:
  git fetch origin
  git log --oneline HEAD..origin/main   # should be empty

PRIMARY DIRECTIVE — Phase B (live in-browser sweep + small-fix loop):
1. Start prototype/start.bat (or python -m http.server 8765 from prototype/).
2. Load Claude-in-Chrome or preview MCP at
   http://localhost:8765/prototype/index.html.
3. Walk every (Test) row in the report (~25) + sample of OK rows.
   Update Status in place via Edit (Test→OK or Test→NEEDS-FIX).
4. Fix the 5 small NEEDS-FIX inline, commit per ~3-fix batch, dual-push:
   - end-screen "Highest Age" undefined (populate or drop)
   - tutorial Esc dead (extend keydown ln 956 to tutorial)
   - saveAndExit toasts "Saved" for skirmish (gate to campaign)
   - menu-last lineage map stale (use COMMANDERS.roster[id].civ)
   - CAST_DURATIONS.long dead key (remove or wire)
5. Queue 3 medium + 2 large NEEDS-FIX to AskUserQuestion at end of B,
   Recommended-first.

CADENCE GUARDRAILS (per PM ask, soft):
- Batch parallel reads; prefer Grep over full-file reads.
- Archive findings to the report file, not chat context.
- Commit per ~3-fix batch; dual-push every commit.
- AskUserQuestion at end of Phase B for medium/large items.

REGRESSION-WATCH: Codex modal post-splash-fix; ATTACK_TYPES data-loaded
shape feeds in-match RPS multipliers; merge-preview / Promote-T4 /
Aztec glyph ◈ / snapshot.

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
- A Phase B fix touches medium/large severity without PM ratification.
- Phase A discovers something so broken that running prototype is unsafe → stop, file findings, AskUserQuestion before continuing.
- Context budget pressure forces a mid-phase split → file mini-handoff and stop cleanly rather than running into context exhaustion.
