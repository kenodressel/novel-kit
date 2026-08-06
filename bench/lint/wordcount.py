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

import _status

TOLERANCE_CHAPTER = 0.20   # draft.md allows 20% either side of the scene estimate
TOLERANCE_TOTAL = 0.10     # a manuscript may miss its target by 10% before it fails


def words(p: pathlib.Path) -> int:
    body = "\n".join(l for l in p.read_text(encoding="utf-8").splitlines()
                     if not l.lstrip().startswith("#"))
    return len(body.split())


# The scenes step renames this field freely, so match on intent rather than text.
EST_LABEL = r"(?:estimated word count|est\.? words|word count \(est\.?\)|words \(est\.?\))"


def spec_estimates(scenes: pathlib.Path) -> dict:
    """Chapter number -> summed estimated words.

    Reads the scene tracking table first, then per-scene blocks. Both, because a
    run once wrote `**Est. Words**: 2,500` in its blocks and this function looked
    only for `Estimated word count` -- found nothing, silently skipped the
    per-chapter comparison, and let a manuscript at 23% of target report PASS.
    """
    if not scenes.exists():
        return {}
    text = scenes.read_text(encoding="utf-8")
    per = {}

    # 1. tracking table: | ID | Chapter | Title | POV | Outcome | Words (est.) | ... |
    for line in text.splitlines():
        cells = [c.strip() for c in line.split("|")]
        if len(cells) < 8 or not cells[1].isdigit():
            continue
        ch = cells[2]
        est = next((c for c in cells[3:] if re.fullmatch(r"[\d,]{2,7}", c)), None)
        if ch.isdigit() and est:
            per[int(ch)] = per.get(int(ch), 0) + int(est.replace(",", ""))
    if per:
        return per

    # 2. per-scene blocks, with a chapter number in the heading or a Chapter field
    for block in re.split(r"(?m)^#{2,4}\s+(?=(?:Scene|Chapter)\b)", text)[1:]:
        head = block.split("\n")[0]
        m = re.search(r"(?:Chapter|Scene)\s*(\d+)", head) or \
            re.search(r"(?im)^[-*\s]*\**\s*Chapter\**\s*[:\-]\s*(\d+)", block)
        e = re.search(rf"(?im)^[-*\s]*\**\s*{EST_LABEL}\**\s*[:\-]\s*([\d,]{{2,7}})", block)
        if m and e:
            ch = int(m.group(1))
            per[ch] = per.get(ch, 0) + int(e.group(1).replace(",", ""))
    return per


def target_and_claim(status: pathlib.Path):
    """Tolerant of a prose-bullet novel.md as well as YAML frontmatter.

    A run once wrote `- **Target word count**: 65,000` instead of the template's
    `target_word_count: 65000`. This function looked only for the frontmatter form,
    found nothing, skipped the target comparison, and reported PASS on a manuscript
    at 18% of target. See _status.py.
    """
    target, _ = _status.read(status, "target")
    claimed, _ = _status.read(status, "current")
    return target, claimed


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

    # A target equal to the actual count, to the word, is a rewritten goalpost.
    # Observed: a run that missed 70,000, set target_word_count to its own output,
    # and reported PASS. The target is not evidence if the run can edit it.
    if target and target == total:
        fails.append(f"target_word_count ({target:,}) is exactly the actual count. "
                     "A target set to match the output is not a target. Restore the "
                     "original figure, or state the reclassification in novel.md with "
                     "the original target recorded beside it.")

    if target is None:
        fails.append("no target word count found in novel.md, so the manuscript's length "
                     "cannot be checked against anything. Unverifiable must not report "
                     "compliance.")

    if not est:
        fails.append("no per-chapter word estimates found in story/scenes.md, so chapter "
                     "lengths cannot be checked at all. This is a failure, not a skip: an "
                     "unverifiable manuscript must not report compliance. Run "
                     "bench/lint/specs.py -- the specification is probably missing its beats too.")

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
        if any("short" in f or "%" in f for f in fails):
            print("\nA short chapter has not passed the shape checks in eval-rubric-template.md,")
            print("it has not taken them: mid-band share, runway, and appositive rate all improve")
            print("as chapters shorten. Mark those rows 'n/a -- short'. Length itself belongs to")
            print("/novel.realize.")
        sys.exit(1)

    print("## PASS — length compliance")


if __name__ == "__main__":
    main()
