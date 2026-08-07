#!/usr/bin/env python3
"""Validate scenes.md structurally BEFORE drafting starts.

    python3 bench/lint/specs.py novels/<slug>

Exists because a run produced 28 scene blocks of seven lines each -- POV, word
estimate, setting, goal, conflict, outcome, closing move -- with no beats at all.
A goal plus a conflict plus an outcome is one beat, and one beat is a 500-word
scene. The manuscript came in at 16,500 words against 70,000, and every step
downstream behaved correctly given its input: the drafter wrote what was
specified, and realize had nothing to expand toward because nothing was missing
relative to a seven-line spec.

This is the cheapest check in the toolkit and the one with the most leverage,
because it runs before any prose exists.

Exit code 1 on failure.
"""
import argparse
import pathlib
import re
import sys

import _status

# The scenes step has been observed to rename fields, so match on intent, not text.
FIELD = {
    "estimate": r"(?:estimated word count|est\.? words|word count \(est\.?\)|words \(est\.?\))",
    "runway": r"runway target",
    "goal": r"scene goal",
    "conflict": r"conflict",
    "outcome": r"outcome",
    "prohibitions": r"(?:must not do|what this scene must not)",
    "closing": r"closing move",
    "withheld": r"(?:deliberately withheld|information withheld)",
}
# Calibrated against five normally drafted novels in this repository, which sit
# between 221 and 449 words per beat. Outside that band by a clear margin:
WORDS_PER_BEAT_MIN = 150   # below this a beat gets a sentence, not a scene
WORDS_PER_BEAT_MAX = 600   # above this the chapter has more room than story
MIN_BEATS = 3


def blocks(text: str):
    parts = re.split(r"(?m)^#{2,4}\s+(?=(?:Scene|Chapter)\b)", text)
    return [p for p in parts[1:] if p.strip()]


def field(block: str, key: str):
    m = re.search(rf"(?im)^[-*\s]*\**\s*{FIELD[key]}\**\s*[:\-]\s*(.+)$", block)
    return m.group(1).strip() if m else None


def count_beats(block: str) -> int:
    """Beats are a numbered or bulleted list under a beats heading."""
    m = re.search(r"(?is)(?:key beats|beats)\**\s*[:\-]?(.*?)(?=\n\s*[-*]?\s*\**(?:information|"
                  r"knowledge|connections|estimated|runway|closing|compliance|what this)|\Z)", block)
    if not m:
        return 0
    body = m.group(1)
    numbered = re.findall(r"(?m)^\s*\d+[.)]\s+\S", body)
    if numbered:
        return len(numbered)
    return len(re.findall(r"(?m)^\s*[-*]\s+\S", body))


def num(s):
    if not s:
        return None
    m = re.search(r"([\d,]{2,7})", s)
    return int(m.group(1).replace(",", "")) if m else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("novel", type=pathlib.Path)
    ap.add_argument("--target", type=int, help="manuscript target; overrides novel.md")
    a = ap.parse_args()

    scenes = a.novel / "story" / "scenes.md"
    if not scenes.exists():
        sys.exit(f"no {scenes}")
    text = scenes.read_text(encoding="utf-8")
    bs = blocks(text)

    status = a.novel / "novel.md"
    target, source = (a.target, "argument") if a.target else _status.read(status, "target")
    fmt_warning = _status.format_warning(status)

    print(f"# {a.novel.name} — scene specification\n")
    print(f"  scene blocks          {len(bs)}")
    if not bs:
        print("\n## FAIL\n\n  - scenes.md contains no scene or chapter blocks.")
        sys.exit(1)

    rows, fails, est_total, missing = [], [], 0, {k: 0 for k in FIELD}
    beatless, thin = [], []

    for i, b in enumerate(bs, 1):
        title = b.split("\n")[0].strip()[:38]
        est = num(field(b, "estimate"))
        run = num(field(b, "runway"))
        beats = count_beats(b)
        for k in FIELD:
            if field(b, k) is None:
                missing[k] += 1
        if est:
            est_total += est
        if beats < MIN_BEATS:
            beatless.append(i)
        elif est and beats and not (WORDS_PER_BEAT_MIN <= est / beats <= WORDS_PER_BEAT_MAX):
            thin.append((i, est, beats, round(est / beats)))
        rows.append((i, title, est, beats, run))

    print(f"  blocks with an estimate   {sum(1 for r in rows if r[2])}")
    print(f"  blocks with >= {MIN_BEATS} beats     {sum(1 for r in rows if r[3] >= MIN_BEATS)}")
    print(f"  blocks with a runway      {sum(1 for r in rows if r[4])}")
    print(f"  estimates sum to          {est_total:,}"
          + (f"   (target {target:,}, from {source})" if target else "   (NO TARGET FOUND)"))
    print()
    if fmt_warning:
        print(f"  note: {fmt_warning}\n")

    print(f"  {'ch':>3}  {'est':>6}  {'beats':>5}  {'w/beat':>6}  {'runway':>6}  title")
    for i, title, est, beats, run in rows:
        wpb = f"{round(est / beats):>6}" if est and beats else "     —"
        print(f"  {i:>3}  {est or '—':>6}  {beats:>5}  {wpb}  {run or '—':>6}  {title}")
    print()

    if beatless:
        fails.append(f"{len(beatless)} of {len(bs)} blocks have fewer than {MIN_BEATS} beats: "
                     f"{', '.join(map(str, beatless[:15]))}"
                     f"{' …' if len(beatless) > 15 else ''}. "
                     "A goal plus a conflict plus an outcome is one beat, and one beat is a "
                     "500-word scene however large the estimate says it is.")
    crowded = [t for t in thin if t[3] < WORDS_PER_BEAT_MIN]
    roomy = [t for t in thin if t[3] > WORDS_PER_BEAT_MAX]
    if crowded:
        fails.append(f"{len(crowded)} blocks crowd their beats into too few words "
                     f"(under {WORDS_PER_BEAT_MIN} per beat): "
                     + ", ".join(f"ch{i} {e}w/{b} beats={w}w each" for i, e, b, w in crowded[:6])
                     + ". Normally drafted novels in this repository run 221-449 words per beat. "
                     "Below 150 a beat gets a sentence rather than a scene, and the chapter reads "
                     "as a summary of itself.")
    if roomy:
        fails.append(f"{len(roomy)} blocks give a chapter more room than it has story for "
                     f"(over {WORDS_PER_BEAT_MAX} words per beat): "
                     + ", ".join(f"ch{i} {e}w/{b} beats={w}w each" for i, e, b, w in roomy[:6]))
    scale_fails, scale_notes = _status.check_scale(status, target)
    fails.extend(scale_fails)
    cluster = _status.threshold_clustering([r[3] for r in rows], MIN_BEATS, "beat count")
    if cluster:
        fails.append(cluster)
    for n in scale_notes:
        print(f"  note: {n}\n")

    if target is None:
        fails.append("no target word count found in novel.md, in frontmatter or as prose, so "
                     "the specification's scale cannot be checked at all. This is a failure, "
                     "not a skip: a spec for 12,000 words is internally consistent and passes "
                     "every structural check, and nothing else in the pipeline will notice.")
    if target and est_total and abs(est_total - target) / target > 0.15:
        fails.append(f"estimates sum to {est_total:,} against a target of {target:,} "
                     f"({est_total / target * 100:.0f}%).")
    for key, label in (("estimate", "a word estimate"), ("runway", "a runway target"),
                       ("goal", "a scene goal"), ("outcome", "an outcome")):
        if missing[key]:
            fails.append(f"{missing[key]} blocks lack {label}.")
    for key, label in (("prohibitions", "prohibitions"), ("closing", "a closing move"),
                       ("withheld", "withheld information")):
        if missing[key] == len(bs):
            fails.append(f"no block states {label} — the field was never instantiated.")

    for n in scale_notes:
        print(f"  note: {n}\n")

    if fails:
        print("## FAIL — do not begin drafting\n")
        for f in fails:
            print(f"  - {f}")
        print("\nDrafting an under-specified scene produces a chapter the size of its "
              "specification,\nand /novel.realize cannot expand toward beats that were never written down.")
        sys.exit(1)

    print("## PASS — specification is draftable")


if __name__ == "__main__":
    main()
