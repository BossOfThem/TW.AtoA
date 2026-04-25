# HANDOFF — Session Checkpoint

**Last session:** 2026-05-05 (**clear-safe**).
**Hand-off by:** Claude (Opus 4.7)
**Hand-off to:** next Claude Code session after `/clear`.

---

## TL;DR

**Per-commander effect-type-variant authoring sub-pass — ARC CLOSED 5/5 + prototype splash-fix LANDED.**

Two tracks closed this session:

1. **Per-commander arc** (commits `256cec7` R1-R3 + `6069c49` R4+R5+spine-doc edits, both dual-pushed). 5-round queue per Axis B (per-ability-slot, all 3 commanders per round) closed all (h)+(g)+(i) effect-type variants for Leonidas / Montezuma II / Ragnar Lothbrok. Effect-type lanes locked Leonidas=Control / Montezuma II=Economy / Ragnar=Summon. R5 cross-commander balance audit surfaced Aztec breakpoint breach (~110-140% of Hard 100%); **Lever-2 applied** (Great Sacrifice lump 600→300 T + permanent yield +10%→+5%) → ~88-104% in band, PvP-IW winrate 50-58% Aztec. Aura-anchor sub-decision resolved via 3x debug loop → **anointed-tower with auto-anoint fallback + free re-anoint UX**; active-cast targeting decoupled from aura center. 3 per-commander one-pagers filed (Leonidas / Montezuma II / Ragnar Lothbrok) — closes `phase-4.md §4.8` exit-condition item #1. Spine-doc edits APPLIED to `concept/phase-4.md` (§4.1 mechanical-content rewrite + Surface table reword + Non-goals reword + NEW Anointed-tower aura model subsection + §4.11.6 deferral removal + §4.8 exit tick).

2. **Prototype splash-fix** (commit `90f6f1c`, dual-pushed). PM reported splash dismiss broken ("click or press any key to skip" non-responsive). Root cause: `ATTACK_TYPES` declared twice in `prototype/index.html` — `let ATTACK_TYPES = null` (data-loaded, line ~1397) collided with inline `const ATTACK_TYPES = {...}` (Codex copy, line ~2003). The `const` redeclaration threw `Uncaught SyntaxError` on script parse, halting all event-listener registration before splash handlers could attach. Fix: renamed inline copy to `CODEX_DATA` and updated 6 references in `openCodex()`. Splash dismiss + every interaction wired again. Data-loaded `ATTACK_TYPES` (richer shape with towerTypeAssignments + demigodTypeAssignments) remains canonical for in-match logic; inline `CODEX_DATA` stays alongside per the alongside-and-non-breaking discipline until C6 retires inline copies.

PM autonomy mandate carried forward — R2-R5 produced fully autonomously. Two arc dual-push checkpoints + splash-fix dual-push + this handoff hygiene commit. cascade-lint clean throughout.

**§5.4 + §2.4a [LOCKED] UNTOUCHED. 17-item conceptual frame UNTOUCHED. All Numbers-phase magnitudes UNTOUCHED. All R1-R7 amendment-pass §-anchors UNTOUCHED. 2026-04-25 locked content skeleton UNTOUCHED.**

---

## NEXT SESSION — primary directive (NEW)

**Prototype UI verification sweep.** PM directive: *"verify all 'buttons' work and full review all buttons/commands options work or atleast say (Test) if your unsure or needs to be refined (But doesn't forget the next steps/roadmap etc...)"*.

Run `prototype/start.bat` (Python `http.server` on :8765 + auto-open). Walk every scene end-to-end and produce a per-scene verification report. For each interactive element record: **OK** (verified working as designed), **(Test)** (unsure / needs PM call / behavior ambiguous), or **NEEDS-FIX** (broken / regressed). Don't fix anything mid-sweep; collect findings, then surface AskUserQuestion at the end with prioritized fix queue.

### Scene checklist (11 scenes — exhaustive)

1. **Splash** — auto-advance after 3s; click-to-dismiss; any-key-to-dismiss; reduce-motion respected. (Splash dismiss verified post-fix this session — re-verify in next session is a sanity check, not a regression hunt.)
2. **Login** — username entry; "Continue as Guest" branch; Enter-key submit; localStorage `atoA.profile.v1` write; existing-profile detect → Returning branch.
3. **Menu** — greeting text reflects username; Continue (resume last save) / Play / Commander / Options / Logout / Quit buttons; keyboard nav.
4. **Profile** — XP bar; cosmetic-slot rendering; Back-to-menu; profile-clear option; mode-gated `writeMatchSave` annotation.
5. **Mode-select** — Skirmish / Tutorial / Co-op Horde / Campaign-stub cards; card hover state; selection commit; back navigation.
6. **Lobby-coop** — host invite-code generation; `?join=<peerID>` URL paste path; ready-state toggle; host-start gate; chat panel 100-char limit; disconnect flow.
7. **Commander-pick** — 5 lineage-colored portrait chips (legacy commander-a..e) + 3 civ portraits (Leonidas / Montezuma II / Ragnar Lothbrok) — confirm all 8 listed and clickable; XP progress bar reflects pick; cosmetic L5/L10/L15 lock badges; pick commit; back navigation; `?silhouette-test=1` harness.
8. **Tutorial** — Skip button → menu; build-glow affordance; sequenced prompts; codex (📖) button → modal opens with 7×5 attack-type vs armor RPS grid; Esc closes codex.
9. **Match** — Send-Wave (Space); pause (Esc); age-up (A); tower-select 1-5; tower placement on cell; merge-preview ghost on hover-over T1/T2 same-civ partner; T3 promote `↑` indicator; right-click sell; right-click targeting menu; Tribute / Divinity / lives HUD increments; Fusion HUD button (disabled until ≥2 Divinity); Cast Bar 3 buttons (passive decorative / short-CD 8s / long-CD 18s); Codex button; toast feed; combat feed; chat panel (co-op); reduce-motion path; UI-scale slider live-preview.
10. **End-of-match** — Victory / Defeat banner; XP award (40 win / 12 loss); auto-level-up toasts; Continue / Replay / Menu buttons; co-op host broadcast `match-end` sync.
11. **Options** — 5 tabs (Audio / Input / Video / Accessibility / Gameplay): per-tab sliders + toggles persisted to localStorage; rebind capture; UI-scale 75-150% live-preview; colorblind-glyph toggle; Apply / Reset / Back buttons.

### Cross-cutting checks

- **Keyboard shortcuts global:** Space=send-wave, A=age-up, 1-5=tower-select, Esc=pause/back, Q=cast-passive (post-C7.a comment-out — verify still inert), C=cast-short (post-C7.a — same).
- **Console clean** — no SyntaxError, no unhandled promise rejections, no fetch 404s (favicon 404 is known-cosmetic).
- **Data fetches** — confirm `prototype/data/{balance,civilizations,fusion-recipes,attack-types,tiers,commanders,enemies}.json` all 200 (note: investigate whether `civilizations.json` contains commanders-shaped data — flagged this session as possible curl-output-ordering artifact, needs in-browser check).
- **Co-op snapshot/intent loop** — host snapshot at 10Hz; guest intents drained per tick; guest-owned towers dashed-white border; net status badge.
- **Mode-aware pause behavior** — Resume / Options / Restart / Save-and-Exit / Quit depending on mode.

### Output shape

Produce a single Markdown report (`prototype/UI-VERIFICATION-2026-05-MM.md` or similar) with one section per scene + cross-cutting section, marking each row OK / (Test) / NEEDS-FIX with one-sentence detail. End with prioritized fix queue (NEEDS-FIX first, then (Test) ranked by player-facing severity). Then surface AskUserQuestion to PM for which items to fix in next track.

---

## What is locked (clear-safe)

### Carried forward (untouched this session, except where noted)

- 17-item conceptual frame (a)-(r) + extension (s) — Accepted.
- All 10 Numbers-phase magnitudes — Accepted.
- 6-mode ontology — Accepted.
- Auxiliary economy structure (Tribute kill-only + Divinity 6-source 4-floor+2-escalation; 6-cap discipline) — Accepted.
- "Go big, no scope cuts" doctrine — Accepted (hub Non-negotiable).
- 2026-04-25 locked content skeleton (3 civs × full ladder + 3 Gods via 9 Fusion recipes + 6 launch modes) — Accepted.
- §5.4 [LOCKED] (Civilizations row).
- §2.4a [LOCKED] (accessibility floor).
- All R1-R7 CONCEPT amendment-pass §-anchors — Accepted.

### NEW spine-doc surfaces this session

| Surface | Bound by |
|---------|----------|
| `phase-4.md §4.1` Anointed-tower aura model subsection (mechanics + auto-anoint + re-anoint + active-cast vs passive-aura distinction + summon-cap signature-window exception 3→9 + per-commander effect-type lane-lock table) | Per-commander R5 |
| `phase-4.md §4.1` Surface table "passive effect" row reword + Non-goals bullet reword + header-tag CLOSED | Per-commander R5 |
| `phase-4.md §4.11.6` deferral language replaced with R2-R5 outcomes + Lever-2 note | Per-commander R5 |
| `phase-4.md §4.8` exit-gate item #1 ticked DONE | Per-commander R5 |
| 5 per-commander decision documents (R1 scope + R2 passive + R3 short-CD active + R4 signature + R5 audit/arc-close) | Per-commander R1-R5 |
| `prototype/index.html` `CODEX_DATA` rename (was inline `ATTACK_TYPES`) | Splash fix |

---

## State snapshot

### Git

- Branch: **`session/2026-04-25-q2-world-pitch`**.
- Latest commit (pre-handoff): **`90f6f1c`** — "fix(prototype): rename inline Codex const to unblock splash."
- Arc commits this session: `256cec7` (per-commander R1-R3) + `6069c49` (R4+R5+spine-doc edits) + `90f6f1c` (prototype splash-fix). All dual-pushed to session branch + `main`.
- Working tree before handoff commit: `PROGRESS.md` (modified — new entry + R9 trim) + `.accord/` (untracked).
- This handoff itself produces one additional commit (PROGRESS / CASCADE / HANDOFF doc-hygiene); will be dual-pushed.

### Phase status

- Per-commander effect-type-variant authoring **CLOSED** — Phase 4 §4.1 mechanical content + §4.8 exit item #1 + §4.11.6 deferral all anchored.
- All upstream untouched: 17-item frame + Numbers-phase magnitudes + amendment-pass §-anchors + locked content skeleton.
- **Phase 5 readiness gate items** (engine-side telemetry per §6.5 + wave-composition variance per §4.7 R11) remain spec-anchored Phase-5-owns-this items.

### Doc-hygiene state

- `PROGRESS.md` session log: 3 entries (per-commander arc + splash-fix / CONCEPT amendment-pass arc / Numbers-phase R10). R9 archived to `PROGRESS-archive.md`.
- `CASCADE.md` pointer: 1 most-recent block (handoff hygiene + splash-fix + per-commander arc closed). Per-commander arc-close prior pointer archived to `CASCADE-history.md`.
- `CASCADE.md` version footer: 0.61 + 0.60 reference. Older (0.59 / 0.58 / etc.) archived to `CASCADE-history.md`.
- cascade-lint expected clean.

### Open follow-ups (carried — UNCHANGED, all preserved for roadmap)

- **#5** — Cultural-sensitivity pass (gates non-abstract civ art; intersects per-civ specialization track).
- **#6** — Patch-1 commanders per civ + Thor recipe-layer dissonance.
- **#7** — Foresight-coin / PvE campaign / AGES / leveling / attributes.
- **#8 / #9** — non-boss enemy ontology / additional commanders.
- **C7.b deferred items** — Builder concurrency cap + 90% refund-on-cancel UI.
- **`admin/concept.json` staleness debt** — still on pre-2026-04-21 5-lineage / 11-age shape; PM picks (a) full rewrite, (b) regenerate from CONCEPT.md, or (c) retire.
- **`research/06-tw-subgenres.md`** new stub — Squadron TD / Legion TD 2 / BTD6 / Element TD / Line Tower Wars / Mini-TD deep dives.

### Authoring sub-passes / roadmap (post-arc — per-commander now CLOSED, others remain queued)

- **Per-tower** — bind cd / range / attack-type / status-proc across 18 T1-T3 + 18 T4 Demigod + 9 God towers across 3 civs. Cross-arc dependency: per-commander affinity hooks (per-commander arc's interface side) bind tower-side targets here. Per-tower target-side hook contracts already specified across R2-R4: `aztec_tower.bonus_tribute_yield_in_active_zone` + `aztec_tower.permanent_tribute_yield_multiplier` + global `summons_alive_max = 3` w/ signature-window exception 3→9 + Berserker/Heathen Warrior Slashing-Bleed cross-ref to 2026-04-26 attack-type-mapping.
- **Per-civ specialization** — Greek / Aztec / Norse identity profiles. Intersects Follow-up #5 cultural-sensitivity gate.
- **Per-map / Round 11** — good-cell authoring + wave-randomization seeds + crystal-lock variance per §4.7 R11 mandate. Cross-cuts all 6 modes.
- **Phase 5 readiness gate** — engine-side telemetry per §6.5 + wave-composition variance per §4.7 R11.
- **`research/06-tw-subgenres.md`** new stub.
- **`admin/concept.json` migration direction** — long-deferred.

### Regression-watch

- Tutorial / match flow / merge-preview hover / Promote-T4 indicator / Aztec glyph (◈) / `logBalanceCurve` / `effectiveTowerStats` / snapshot.
- **NEW post-splash-fix:** confirm Codex modal still opens correctly and renders 7×5 grid (the rename touched `openCodex()` references). Also verify `ATTACK_TYPES` data-loaded variant is what feeds in-match RPS multipliers.

---

## Cadence rules carried forward

- **Cadence exists to manage the context window, not to gate every step.** Concrete plan = execute end-to-end; gate on genuine ambiguity only.
- **PM autonomy mandate:** within established multi-round arcs where PM has consistently picked Recommended, proceed autonomously without per-question gates. See `feedback_autonomy_mandate.md`.
- **AskUserQuestion is the standard interface** when gating is needed. Always Recommended-first.
- **MD-first preservation** — for any scope expansion or non-trivial conceptual ratification, land in MD before further questions. /clear must be safe at any prompt.
- **Dual-push discipline:** push to BOTH session branch AND `main` after every commit. Commit at every ~3 rounds (or per-track for sweep work).
- **Local-main hygiene:** `git fetch origin && git log --oneline HEAD..origin/main` BEFORE reading docs.
- **3x debug loop** on any CONCEPT-constraint-touching proposal.
- **Doc hygiene on each handoff:** trim PROGRESS to 3 entries, CASCADE pointer to 1 block, version footer to 2 bumps.

---

## Next-session prompt (copy-paste after `/clear`)

```
Resuming Ash to Altar — per-commander effect-type-variant authoring sub-pass
ARC CLOSED 2026-05-05 (5/5 rounds; spine-doc edits applied; dual-pushed
6069c49). Prototype splash-fix landed same session (90f6f1c — ATTACK_TYPES
const collision renamed to CODEX_DATA, restoring all event-listener wiring).

BOOTSTRAP per CLAUDE.md order:
  README → CLAUDE → CASCADE → HANDOFF → PROGRESS → CONCEPT.

BEFORE reading docs:
  git fetch origin
  git log --oneline HEAD..origin/main   # should be empty after dual-push

STATE ALOUD (before producing anything):
- Phase status: Per-commander arc CLOSED 5/5 + spine-doc edits applied
  to concept/phase-4.md (§4.1 + §4.11.6 + §4.8). All upstream untouched.
  Splash fix landed; prototype playable. Per-tower / per-civ / per-map /
  Phase 5 readiness gate / research/06-tw-subgenres / admin migration /
  Follow-ups #5/#6/#7/#8/#9 / C7.b deferred items all in roadmap.
- Open blockers: none load-bearing.
- Specific next-step: PRIMARY DIRECTIVE this session is the
  PROTOTYPE UI VERIFICATION SWEEP per PM ask. Walk all 11 scenes
  (splash/login/menu/profile/mode-select/lobby-coop/commander-pick/
  tutorial/match/end/options) end-to-end. For each interactive element
  mark OK / (Test) / NEEDS-FIX with one-sentence detail. Cross-cutting
  checks: keyboard shortcuts, console clean, data fetches, co-op
  snapshot loop, mode-aware pause. Output: single Markdown report
  (prototype/UI-VERIFICATION-2026-05-MM.md). End with prioritized
  fix queue + AskUserQuestion to PM for which items to fix next.

CADENCE: AskUserQuestion is standard interface when gating needed.
Recommended-first. MD-first on scope expansions. Execute end-to-end
when plan concrete; gate on genuine ambiguity only. Commit + dual-push
per logical batch.

PM AUTONOMY MANDATE: once an arc establishes a stable "PM picks
Recommended" pattern, proceed autonomously within that arc. Surface
gates only on genuine forks / scope expansion / cascade-risk / handoff.
See feedback_autonomy_mandate.md.

CURRENCY REMINDER: Tribute (kill-only, k-invariant) + Divinity (6-cap;
4-floor R10/R15/R30 boss + match-completion + 2-escalation Perfect-Wave
+ First-Hybrid). Mythium RETIRED.

DOCTRINE REMINDER: "Go big at launch" is hub Non-negotiable. MVP ships
full content skeleton (3 civs × full ladder + 3 Gods via 9 Fusion
recipes + 6 launch modes). Cuts go to post-launch content, NEVER to
launch skeleton.

REGRESSION-WATCH: Tutorial / match flow / merge-preview / Promote-T4
indicator / Aztec glyph ◈ / logBalanceCurve / effectiveTowerStats /
snapshot. NEW: Codex modal post-splash-fix (rename touched
openCodex() references); ATTACK_TYPES data-loaded variant feeds
in-match RPS multipliers.

VERIFY each step with: python tools/cascade-lint.py
DUAL-PUSH each commit: session branch + main.
PROTOTYPE RUN: prototype/start.bat (Python http.server on :8765).

SCOPE GUARD:
- §5.4 [LOCKED]; §2.4a [LOCKED]; 2026-04-25 locked content skeleton
  untouched.
- 17-item frame + extension (s) Accepted.
- All Numbers-phase magnitudes Accepted.
- All R1-R7 CONCEPT amendment-pass §-anchors Accepted.
- All per-commander R1-R5 spine-doc edits Accepted.
- 6-mode ontology + auxiliary economy structure Accepted.
- "Go big at launch" doctrine Accepted (Non-negotiable).
- Effect-type lane locks Hard reversibility (Leonidas=Control /
  Montezuma II=Economy / Ragnar=Summon).
- Cultural-sensitivity Follow-up #5 still hard-gates non-abstract
  civ art.

POST-SWEEP ROADMAP (preserve in any forward proposal):
1. Per-tower authoring sub-pass (cd/range/attack-type/status-proc
   across 45 towers; consumes per-commander target-side hooks).
2. Per-civ specialization (Greek/Aztec/Norse; Follow-up #5 gate).
3. Per-map / Round 11 (wave-randomization + crystal-lock + good-cell).
4. Phase 5 readiness gate (engine-side telemetry + wave variance).
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
- `cascade-lint` fails and fix > 5min.
- The 17-item frame would be silently edited.
- Any Numbers-phase bound magnitude would be silently re-tuned without a superseding decision entry.
- Any amendment-pass §-anchor (§3.6 / §4.6 / §4.6a / §4.7 R11 / §4.10 / §4.11 / §6.5 / §7.4 / hub phase-index rows) would be silently edited.
- Any per-commander R1-R5 spine-doc surface (§4.1 anointed-tower aura subsection / §4.11.6 outcomes summary / §4.8 exit tick / lane locks) would be silently edited.
- A scope expansion occurs and PM has not landed it in MD before further questions.
- An authoring-sub-pass commit lands without a `decisions/<date>-*-<slug>.md` entry capturing the bindings.
- Prototype changes regress splash dismiss / event-listener registration / Codex modal / data-loaded `ATTACK_TYPES` shape.
