#!/usr/bin/env python3
"""Check the manuscript's actual length against what it claims and what it specified.

    python3 bench/lint/wordcount.py novels/<slug>

Exists because a pipeline run produced a 27,127-word manuscript, specified 70,000
in its own scene table, and recorded 70,420 in novel.md as complete. Nothing in the
pipeline computed the number, so nothing contradicted it.

Every shape metric in this toolkit -- mid-band share, runway, appositive rate --
improves as chapters get shorter. A scene sketch passes them all. So length
compliance is checked FIRST, and a chapter that is short against its own spec is
not eligible to pass anything else.

Exit code 1 if any check fails, so it can gate a step.
"""
import argparse
import pathlib
import re
import sys

TOLERANCE_CHAPTER = 0.20   # draft.md allows 20% either side of the scene estimate
TOLERANCE_TOTAL = 0.10     # a manuscript may miss its target by 10% before it fails


def words(p: pathlib.Path) -> int:
    body = "\n".join(l for l in p.read_text(encoding="utf-8").splitlines()
                     if not l.lstrip().startswith("#"))
    return len(body.split())


def spec_estimates(scenes: pathlib.Path) -> dict:
    """Chapter number -> summed estimated words, read from the scene tracking table.
    Table shape: | ID | Chapter | Title | POV | Outcome | Words (est.) | ... |"""
    if not scenes.exists():
        return {}
    per = {}
    for line in scenes.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.split("|")]
        if len(cells) < 8 or not cells[1].isdigit():
            continue
        ch = cells[2]
        est = next((c for c in cells[3:] if re.fullmatch(r"[\d,]{2,7}", c)), None)
        if ch.isdigit() and est:
            per[int(ch)] = per.get(int(ch), 0) + int(est.replace(",", ""))
    return per


def target_and_claim(status: pathlib.Path):
    if not status.exists():
        return None, None
    text = status.read_text(encoding="utf-8")
    def grab(key):
        m = re.search(rf"^{key}:\s*\"?([\d,]+)\"?", text, re.M)
        return int(m.group(1).replace(",", "")) if m else None
    return grab("target_word_count"), grab("current_word_count")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("novel", type=pathlib.Path)
    a = ap.parse_args()

    files = sorted((a.novel / "manuscript").glob("chapter-*.md"))
    if not files:
        sys.exit(f"no chapter-*.md under {a.novel / 'manuscript'}")

    actual = {}
    for f in files:
        m = re.search(r"chapter-(\d+)", f.name)
        if m:
            actual[int(m.group(1))] = words(f)
    total = sum(actual.values())

    est = spec_estimates(a.novel / "story" / "scenes.md")
    target, claimed = target_and_claim(a.novel / "novel.md")

    print(f"# {a.novel.name}\n")
    print(f"  chapters on disk      {len(actual)}")
    print(f"  actual words          {total:,}")
    if est:
        print(f"  specified in scenes   {sum(est.values()):,}")
    if target:
        print(f"  target_word_count     {target:,}")
    if claimed is not None:
        print(f"  current_word_count    {claimed:,}   <- as recorded in novel.md")
    print()

    fails = []

    if claimed is not None and total:
        drift = abs(claimed - total) / total
        if drift > 0.02:
            fails.append(f"recorded word count is off by {claimed - total:+,} "
                         f"({drift * 100:.0f}%). novel.md must be computed, not asserted.")

    if target and total < target * (1 - TOLERANCE_TOTAL):
        fails.append(f"manuscript is {total / target * 100:.0f}% of target "
                     f"({total:,} of {target:,}). Short by {target - total:,}.")

    if est:
        print("  per chapter, actual vs specified:\n")
        short = []
        for ch in sorted(set(actual) | set(est)):
            got, want = actual.get(ch, 0), est.get(ch)
            if not want:
                continue
            ratio = got / want
            flag = "" if abs(ratio - 1) <= TOLERANCE_CHAPTER else ("  SHORT" if ratio < 1 else "  LONG")
            if flag.strip() == "SHORT":
                short.append(ch)
            print(f"    ch {ch:>3}  {got:>6,}  vs {want:>6,}   {ratio * 100:5.0f}%{flag}")
        if short:
            fails.append(f"{len(short)} chapters more than {TOLERANCE_CHAPTER:.0%} short "
                         f"of their scene estimate: {', '.join(map(str, short))}")
        print()

    if fails:
        print("## FAIL\n")
        for f in fails:
            print(f"  - {f}")
        print("\nShape metrics are not meaningful until length compliance passes:")
        print("mid-band share, runway, and appositive rate all improve as chapters shorten.")
        sys.exit(1)

    print("## PASS — length compliance")


if __name__ == "__main__":
    main()
