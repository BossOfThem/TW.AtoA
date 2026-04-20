# Claude Code Project Instructions — TW-COMMANDERS

## Project summary

Tower Wars game with commander-based player identity, age-based tower evolution within each match, and cross-lineage hybrid units. Two-dev team. Currently **concept phase — no code yet**. See `docs/CONCEPT.md` for the full design doc.

## Session start checklist

When starting a Claude Code session in this repo, read in order:

1. `README.md`
2. `CLAUDE.md` (this file)
3. `docs/CONCEPT.md`
4. `docs/PLAYER-JOURNEY.md`

Then state aloud:
- Current phase status (which phase is active).
- Open blockers preventing phase exit.
- The specific item being worked this session.

## Working conventions

### Cascade discipline
Phases have explicit exit conditions (see `CONCEPT.md`). No decision in Phase N may violate a Phase N-1 constraint without a written override in the decision log. If a downstream decision requires changing an upstream constraint, reopen the upstream phase properly — do not silently edit.

### 3x debug loop
All major design or technical decisions go through:
- **Loop 1:** aggressive critique. Attack the proposal on every plausible failure mode.
- **Loop 2:** steelman. Read Loop 1 back and identify what it got wrong or overweighted.
- **Loop 3:** synthesis. Combine insights, propose actionable direction with stop-gaps.

This is the ACCORD pattern discipline applied to design work.

### Placeholder flagging
Every name in the design docs is placeholder unless explicitly marked `[LOCKED]`. When proposing new names, run them through the naming convention check (see `CONCEPT.md §5.4`) but do not treat any generated name as final.

### Commander = user
The "Commander" in these docs is the player's persistent identity. When working on commander features, unit interactions, UI flows, or any player-facing design, adopt first-person player perspective. The commander is not an NPC.

### No code yet
This repo is concept-only until Phase 5 begins. Do not generate game code, engine configuration, shader pseudocode, or asset pipelines until Phase 4 exits and engine is locked. Exceptions: structural docs, decision log entries, design artifact markup (tables, diagrams), tooling for doc management.

## Naming conventions (from CONCEPT.md §5.4, LOCKED)

When generating new names for entities:
- **Commanders:** evocative titles, first-name + epithet allowed. Never generic.
- **Lineages:** one-syllable, ancient-feeling nouns (pattern: Sinew, Ember, Forge, Crown, Veil).
- **Ages:** evocative compound nouns, not dates (pattern: The Mudbrick Era).
- **Towers/Units:** job titles, never proper nouns (pattern: Warhost, Spirebinder).
- **Hybrids:** compound or hyphenated (pattern: Tank Corps, Rune-Smiths).
- **Enemies:** single-word kenning (pattern: Thornback, Nullspawn).
- **Heirlooms/items:** mythic-fragment style (pattern: The Last Spear of Heidelberg).
- **Modes:** direct, muscular (pattern: Lane Wars, Horde, Campaign). Not florid.

Flag any generated name that breaks pattern.

## What Claude Code should do

- Refine concept documents when asked.
- Propose names that follow convention.
- Flag cascade violations when they occur.
- Generate design exploration and system specs when prompted.
- Run 3x debug loops on major proposals without being asked.
- Populate the hybrid table, commander roster, age gate UX, etc., when explicitly working those items.
- Propose engine architecture and data model when Phase 4 is close to exit.

## What Claude Code should NOT do

- Lock any name without explicit sign-off.
- Generate game code before engine is locked and Phase 5 begins.
- Expand scope beyond what's in `CONCEPT.md` without a written scope decision.
- Treat any placeholder in the docs as final.
- Propose monetization changes that move toward pay-to-win.
- Suggest adding features that violate the "solo must be fully great" principle.

## Decision log

All major decisions go in `decisions/` (directory to be created when first decision is logged). Format per entry:
- Date
- Decision
- Alternatives considered
- Reason chosen
- Reversibility note

## Style

- Prose over bullets for analysis and design exploration.
- Tables for structured data (hybrid tables, commander rosters, mode comparisons).
- Markdown throughout.
- One document per major system when systems get large enough to warrant it.

## Escalation

If a request requires violating any principle in this file or in `CONCEPT.md`, stop and flag it before proceeding. The discipline is the product.
