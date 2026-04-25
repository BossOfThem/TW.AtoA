#!/usr/bin/env python3
"""cascade-lint — verify doc cascade integrity for Ash to Altar.

Checks:
  1. Every markdown link in CASCADE.md points at an existing file.
  2. Every stage / research doc has a `**Status:**` and `**Last reviewed:**` line.
  3. Every decision file has `**Reversibility:**` in body.
  4. CASCADE.md decisions table row count matches decisions/*.md count
     (minus TEMPLATE.md).
  5. PROGRESS.md has at least one `[x]` done row and reports a first-unchecked
     box if one exists.

Output: one finding per issue. Exit 0 clean, 1 dirty.
Run: `python tools/cascade-lint.py` from project root.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
findings: list[str] = []


def add(msg: str) -> None:
    findings.append(msg)


def check_cascade_links() -> None:
    cascade = ROOT / "CASCADE.md"
    if not cascade.exists():
        add("CASCADE.md missing")
        return
    text = cascade.read_text(encoding="utf-8")
    for m in re.finditer(r"\[[^\]]+\]\(([^)#]+\.md)(?:#[^)]*)?\)", text):
        target = m.group(1)
        if target.startswith("http") or "<" in target or ">" in target:
            continue
        path = (ROOT / target).resolve()
        if not path.exists():
            add(f"CASCADE.md links to missing file: {target}")


def check_doc_headers(glob: str, kind: str) -> None:
    for path in sorted(ROOT.glob(glob)):
        text = path.read_text(encoding="utf-8")
        if "**Status:**" not in text:
            add(f"{kind} missing Status header: {path.relative_to(ROOT)}")
        if "**Last reviewed:**" not in text:
            add(f"{kind} missing Last reviewed: {path.relative_to(ROOT)}")


def check_decisions() -> None:
    dec_dir = ROOT / "decisions"
    if not dec_dir.exists():
        add("decisions/ dir missing")
        return
    files = [p for p in sorted(dec_dir.glob("*.md")) if p.name != "TEMPLATE.md"]
    for path in files:
        text = path.read_text(encoding="utf-8")
        if "**Reversibility:**" not in text:
            add(f"decision missing Reversibility: {path.relative_to(ROOT)}")

    cascade = (ROOT / "CASCADE.md").read_text(encoding="utf-8")
    table_rows = re.findall(r"^\| \d{4}-\d{2}-\d{2} \|", cascade, re.M)
    if len(table_rows) != len(files):
        add(
            f"CASCADE.md decisions table has {len(table_rows)} rows, "
            f"decisions/ has {len(files)} files"
        )


SIZE_CAP = 600


def check_size_caps() -> None:
    """Soft-cap warning for MDs over the 200-600 readability band."""
    roots = [ROOT / "CASCADE.md", ROOT / "CONCEPT.md", ROOT / "HANDOFF.md", ROOT / "PROGRESS.md", ROOT / "CLAUDE.md", ROOT / "README.md"]
    for p in roots:
        if p.exists():
            n = len(p.read_text(encoding="utf-8").splitlines())
            if n > SIZE_CAP:
                add(f"oversized: {p.relative_to(ROOT)} ({n} lines, cap {SIZE_CAP})")
    for p in sorted((ROOT / "concept").glob("*.md")) if (ROOT / "concept").exists() else []:
        n = len(p.read_text(encoding="utf-8").splitlines())
        if n > SIZE_CAP:
            add(f"oversized: {p.relative_to(ROOT)} ({n} lines, cap {SIZE_CAP})")


def check_concept_folder() -> None:
    """Every concept/phase-N.md has Status + Last reviewed; CONCEPT.md hub links all 7."""
    cfolder = ROOT / "concept"
    if not cfolder.exists():
        add("concept/ folder missing (expected per doc-cascade split)")
        return
    expected = [f"phase-{i}.md" for i in range(1, 8)]
    for name in expected:
        p = cfolder / name
        if not p.exists():
            add(f"concept/{name} missing")
            continue
        text = p.read_text(encoding="utf-8")
        if "**Status:**" not in text:
            add(f"concept/{name} missing Status header")
        if "**Last reviewed:**" not in text:
            add(f"concept/{name} missing Last reviewed")
    hub = ROOT / "CONCEPT.md"
    if hub.exists():
        htxt = hub.read_text(encoding="utf-8")
        for name in expected:
            if f"concept/{name}" not in htxt:
                add(f"CONCEPT.md hub missing link to concept/{name}")


def check_concept_cross_refs() -> None:
    """Warn when `CONCEPT.md §N.M` references elsewhere no longer resolve.

    Best-effort: scans all tracked MDs for the `CONCEPT.md §N.M` pattern and warns
    if the referenced section number does not appear as a header in the hub or
    the matching concept/phase-N.md child.
    """
    hub = ROOT / "CONCEPT.md"
    if not hub.exists():
        return
    mds = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts and "node_modules" not in p.parts]
    for p in mds:
        try:
            text = p.read_text(encoding="utf-8")
        except Exception:
            continue
        for m in re.finditer(r"CONCEPT\.md\s*§(\d+)\.(\d+[a-z]?)", text):
            phase, sub = m.group(1), m.group(2)
            child = ROOT / "concept" / f"phase-{phase}.md"
            targets = []
            if child.exists():
                targets.append(child.read_text(encoding="utf-8"))
            targets.append(hub.read_text(encoding="utf-8"))
            needle = f"{phase}.{sub}"
            if not any(needle in t for t in targets):
                add(f"stale §{needle} ref in {p.relative_to(ROOT)} — no matching header in hub or concept/phase-{phase}.md")


def check_progress() -> None:
    progress = ROOT / "PROGRESS.md"
    if not progress.exists():
        add("PROGRESS.md missing")
        return
    text = progress.read_text(encoding="utf-8")
    done = re.findall(r"- \[x\]", text)
    if not done:
        add("PROGRESS.md has no completed steps — expected Step 0 minimum")
    # Match unchecked rows, but skip ones explicitly tagged `[~skip]` or annotated
    # as default-skipped inline. Reports the next *actually-open* step.
    first_open = None
    for m in re.finditer(r"- \[ \] \*\*(Step [^\*]+)\*\*([^\n]*)", text):
        label = m.group(1).strip()
        tail = m.group(2) or ""
        if "[~skip]" in tail.lower() or "default-skip" in tail.lower():
            continue
        first_open = label
        break
    if first_open:
        print(f"  next-open-step: {first_open}")
    else:
        print("  next-open-step: none (queue clean)")


def check_prototype_data() -> None:
    """Verify prototype/data/*.json schemas for the concept-demo build-out (Phase 10.1)."""
    data_dir = ROOT / "prototype" / "data"
    if not data_dir.exists():
        return
    required = {
        "balance.json": ["wave", "age", "economy", "base", "match", "coop", "multiplayer", "save"],
        "commanders.json": ["active", "roster"],
        "enemies.json": ["enemies"],
        # C1 reshape (2026-04-29) — canonical files. Legacy ages.json + towers.json
        # deleted in C6 slice 2 / Slice C graduation cut (2026-04-25 session).
        "civilizations.json": ["civilizations"],
        "fusion-recipes.json": ["fusionMenuUnlockCost", "fusionExecutionCost", "recipes"],
        "attack-types.json": ["types", "armorTags", "rpsMatrix", "towerTypeAssignments", "demigodTypeAssignments"],
        "tiers.json": ["tiers", "fusion"],
    }
    for name, keys in required.items():
        p = data_dir / name
        if not p.exists():
            add(f"prototype/data/{name} missing")
            continue
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            add(f"prototype/data/{name} invalid JSON: {e}")
            continue
        for k in keys:
            if k not in data:
                add(f"prototype/data/{name} missing top-level key: {k}")
    # Cross-file: commanders all playable for pivot
    cmd_p = data_dir / "commanders.json"
    if cmd_p.exists():
        try:
            cmd = json.loads(cmd_p.read_text(encoding="utf-8"))
            non_playable = [k for k, v in cmd.get("roster", {}).items() if not v.get("playable")]
            if non_playable:
                add(f"commanders.json non-playable roster entries: {non_playable}")
        except Exception:
            pass
    # C1 reshape (2026-04-29) cross-file integrity
    civ_p = data_dir / "civilizations.json"
    fus_p = data_dir / "fusion-recipes.json"
    atk_p = data_dir / "attack-types.json"
    tie_p = data_dir / "tiers.json"
    if civ_p.exists():
        try:
            civ = json.loads(civ_p.read_text(encoding="utf-8"))
            civs = civ.get("civilizations", [])
            if len(civs) != 3:
                add(f"civilizations.json expected 3 civs (Greek/Aztec/Norse), got {len(civs)}")
            for c in civs:
                if len(c.get("towersT1T3", [])) != 6:
                    add(f"civilizations.json[{c.get('id')}] expected 6 T1-T3 towers, got {len(c.get('towersT1T3', []))}")
                if len(c.get("units", [])) != 5:
                    add(f"civilizations.json[{c.get('id')}] expected 5 units, got {len(c.get('units', []))}")
                if len(c.get("demigodsT4", [])) != 6:
                    add(f"civilizations.json[{c.get('id')}] expected 6 T4 demigods, got {len(c.get('demigodsT4', []))}")
                if len(c.get("gods", [])) != 3:
                    add(f"civilizations.json[{c.get('id')}] expected 3 gods, got {len(c.get('gods', []))}")
        except Exception:
            pass
    if fus_p.exists():
        try:
            fus = json.loads(fus_p.read_text(encoding="utf-8"))
            recipes = fus.get("recipes", [])
            if len(recipes) != 9:
                add(f"fusion-recipes.json expected 9 recipes (3 per civ), got {len(recipes)}")
            # Cross-ref god IDs against civilizations.json
            if civ_p.exists():
                try:
                    civ = json.loads(civ_p.read_text(encoding="utf-8"))
                    civ_god_ids = {g["id"] for c in civ.get("civilizations", []) for g in c.get("gods", [])}
                    recipe_god_ids = {r.get("godId") for r in recipes}
                    if civ_god_ids != recipe_god_ids:
                        add(f"fusion-recipes.json godIds {recipe_god_ids - civ_god_ids} not in civilizations.json; missing {civ_god_ids - recipe_god_ids}")
                except Exception:
                    pass
        except Exception:
            pass
    if atk_p.exists():
        try:
            atk = json.loads(atk_p.read_text(encoding="utf-8"))
            if len(atk.get("types", [])) != 7:
                add(f"attack-types.json expected 7 types, got {len(atk.get('types', []))}")
            if len(atk.get("armorTags", [])) != 5:
                add(f"attack-types.json expected 5 armor tags, got {len(atk.get('armorTags', []))}")
        except Exception:
            pass
    if tie_p.exists():
        try:
            tie = json.loads(tie_p.read_text(encoding="utf-8"))
            if len(tie.get("tiers", [])) != 4:
                add(f"tiers.json expected 4 tiers (T1-T4), got {len(tie.get('tiers', []))}")
            if not tie.get("fusion") or tie["fusion"].get("isATier", True):
                add("tiers.json fusion meta missing or marked as a tier (must be isATier:false)")
        except Exception:
            pass


def main() -> int:
    print("cascade-lint starting...")
    check_cascade_links()
    check_doc_headers("stages/*.md", "stage")
    check_doc_headers("research/*.md", "research")
    check_decisions()
    check_prototype_data()
    check_size_caps()
    check_concept_folder()
    check_concept_cross_refs()
    check_progress()

    if findings:
        print(f"\n{len(findings)} finding(s):")
        for f in findings:
            print(f"  - {f}")
        return 1
    print("\nclean.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
