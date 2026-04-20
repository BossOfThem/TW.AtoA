# Research 00 — Methodology

**Status:** Draft
**Feeds into:** All other research docs (sets the rules they must follow).
**Last reviewed:** 2026-04-20

---

## Purpose

This doc sets the rules every other research doc under [research/](.) must follow. If a claim in another doc conflicts with these rules, the doc is wrong, not this one.

## Rules

### Source triage

- **Tier 1 (preferred):** public platform data (Steam charts, SteamDB concurrents, Twitch tracker watch-hour counts, Newzoo reports, Sensor Tower/AppMagic for mobile), 2024–2026 freshness.
- **Tier 2 (acceptable, flag):** reputable trade press (GameDiscoverCo, Naavik, GamesIndustry.biz), public post-mortems by developers, reviewer aggregate data.
- **Tier 3 (only with caveat):** Reddit/Discord/forum sentiment, YouTuber retrospectives — useful for *direction* but never the sole basis of a claim.
- **Tier 4 (reject):** marketing materials, publisher hype, single-anecdote playtest quotes presented as representative.

### Freshness policy

- Prefer claims dated 2024–2026.
- Claims from 2022–2023 get a "freshness note" flag.
- Claims older than 2022 either get a strong caveat or are discarded.
- Any claim lacking a date gets a `[date unknown]` tag and is treated as Tier 3.

### Conflict resolution

When sources disagree:

1. Prefer higher tier.
2. Prefer more recent.
3. If both equal, present both with an explicit "sources disagree" note — do not hide the disagreement.
4. Never average numbers across sources with different methodologies.

### "So what for this game" synthesis rule

Every major section of every research doc ends with a **"So what for this game"** paragraph. This is where the research becomes actionable. The synthesis goes through the 3x debug loop from [CLAUDE.md](../CLAUDE.md):

- Loop 1: attack the conclusion.
- Loop 2: steelman it.
- Loop 3: synthesize with named caveats.

Only the Loop-3 synthesis ships. Loops 1 and 2 live in a "working notes" appendix if preserved at all.

### Citation format

Plain prose + source pointer in parentheses: *(SteamDB, "Legion TD 2" concurrents, retrieved 2026-03)*. No heavy footnote apparatus. We're making decisions, not writing an academic paper.

### What this methodology does NOT do

- Claim statistical rigor we don't have.
- Pretend a 10-source survey is a study.
- Overrule playtest evidence when real playtesters exist — research is a *prior*, not a *verdict*.
