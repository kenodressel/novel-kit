#!/usr/bin/env python3
"""Is this actually narrative prose, or text of the right length?

    python3 bench/lint/prose_sanity.py novels/<slug>

Every other check in bench/lint assumes the manuscript is prose and asks how good
it is. This one asks whether it is prose at all, and it exists because a run met a
50,000-word target by looping a handful of template sentences with the chapter
number substituted in:

    "...as events in chapter 1 began to unfold"
    "Earl Danbury's extortion network was closing in during beat 8"

50,145 words, 4.1% of sentences unique, 2,997 placeholder leaks, 228 verbatim
duplicate paragraphs, 0.6% dialogue, and all 16 chapters opening with the same
sentence. It passed specs.py and wordcount.py cleanly, because both were built to
verify quantities and this was the right quantity.

That is the shape of the failure: a hard length floor with no authenticity check
makes padding the cheapest way to comply. Thresholds below are calibrated against
eight normally drafted novels in this repository, which score 99.4-100% unique
sentences, 0-1 leaks, 0-4 duplicate paragraphs and 9.3-17% dialogue. The bands sit
far outside those, so only catastrophic failures fire and no real draft trips them.

Exit code 1 on failure. Run it before any other prose check.
"""
import argparse
import collections
import pathlib
import re
import sys

# "in chapter 3", "during beat 8", "in phase 12" -- scaffolding language that
# survived into the prose. Real novels score 0-1 across a whole manuscript.
LEAK = re.compile(
    r"\b(?:in|during|at|for|by|within|throughout|across)\s+"
    r"(?:chapter|scene|beat|phase|movement|sequence|section|step|part)\s+\d+\b", re.I)
DIALOGUE = re.compile(r"[\"“„«](.+?)[\"”“»]", re.S)

MIN_UNIQUE_SENTENCES = 0.90   # real: 0.994 - 1.000
MAX_LEAKS = 3                 # real: 0 - 1
MIN_DIALOGUE_SHARE = 0.04     # real: 0.093 - 0.170
MAX_SHARED_OPENINGS = 1       # real: 0

# Duplicate paragraphs as a share, not a count. A real draft accumulates a few by
# accident -- one novel here repeats four, and a blind reader flagged one of them as
# its clearest self-plagiarism. That is a finding for repetition.py, not evidence
# that the file is not a manuscript. The padding case had 228.
MAX_DUPLICATE_PARA_SHARE = 0.02
MAX_DUPLICATE_PARAS_ABS = 25


def chapters(novel: pathlib.Path):
    files = sorted((novel / "manuscript").glob("chapter-*.md"))
    if not files:
        sys.exit(f"no chapter-*.md under {novel / 'manuscript'}")
    out = []
    for f in files:
        body = "\n".join(l for l in f.read_text(encoding="utf-8").splitlines()
                         if not l.lstrip().startswith("#")).strip()
        out.append((f.name, body))
    return out


def norm(s: str) -> str:
    return " ".join(s.split()).lower()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("novel", type=pathlib.Path)
    a = ap.parse_args()

    chs = chapters(a.novel)
    full = "\n\n".join(t for _, t in chs)
    words = len(full.split())

    sentences = [norm(s) for s in re.split(r"(?<=[.!?])\s+", full) if len(s.split()) > 4]
    unique = len(set(sentences)) / max(1, len(sentences))

    leaks = LEAK.findall(full)

    paras = [norm(p) for _, t in chs for p in re.split(r"\n\s*\n", t) if len(p.split()) > 20]
    para_counts = collections.Counter(paras)
    dup_paras = sum(c - 1 for c in para_counts.values() if c > 1)

    dialogue_words = sum(len(m.group(1).split()) for m in DIALOGUE.finditer(full))
    dialogue_share = dialogue_words / max(1, words)

    openings = collections.Counter(norm(" ".join(t.split()[:12])) for _, t in chs)
    shared_openings = sum(c for c in openings.values() if c > 1)

    print(f"# {a.novel.name} — is this prose?\n")
    print(f"  chapters                    {len(chs)}")
    print(f"  words                       {words:,}")
    print(f"  sentences                   {len(sentences):,}")
    print(f"  unique sentences            {unique * 100:5.1f}%   (real novels: 99.4-100%)")
    print(f"  scaffolding leaks           {len(leaks):5d}     (real novels: 0-1)")
    print(f"  verbatim duplicate paras    {dup_paras:5d}     (real novels: 0)")
    print(f"  words inside dialogue       {dialogue_share * 100:5.1f}%   (real novels: 10-17%)")
    print(f"  chapters sharing an opening {shared_openings:5d}     (real novels: 0)")
    print()

    fails, notes = [], []
    if unique < MIN_UNIQUE_SENTENCES:
        fails.append(f"only {unique * 100:.1f}% of sentences are unique. "
                     f"{100 - unique * 100:.0f}% of this manuscript is repeated text. "
                     "This is padding, not prose.")
    if len(leaks) > MAX_LEAKS:
        ex = ", ".join(f'"{l}"' for l in list(dict.fromkeys(leaks))[:4])
        fails.append(f"{len(leaks)} scaffolding phrases survived into the prose ({ex}). "
                     "No narrative sentence refers to its own beat number. These are "
                     "specification placeholders that were never replaced with events.")
    dup_share = dup_paras / max(1, len(paras))
    if dup_paras > MAX_DUPLICATE_PARAS_ABS or dup_share > MAX_DUPLICATE_PARA_SHARE:
        worst = max(para_counts.values())
        fails.append(f"{dup_paras} paragraphs ({dup_share * 100:.0f}% of the manuscript) are "
                     f"verbatim duplicates of another paragraph; the most repeated appears "
                     f"{worst} times.")
    elif dup_paras:
        notes.append(f"{dup_paras} verbatim duplicate paragraph(s) — under the threshold for "
                     "this check, but worth a look in repetition.py. Accidental "
                     "self-plagiarism is common in unedited drafts.")
    if dialogue_share < MIN_DIALOGUE_SHARE:
        fails.append(f"{dialogue_share * 100:.1f}% of words are inside dialogue. Narrative "
                     "fiction runs 10-17%. Below 4% the characters are being described "
                     "rather than allowed to speak, which is summary, not scene.")
    if shared_openings > MAX_SHARED_OPENINGS:
        fails.append(f"{shared_openings} of {len(chs)} chapters open with the same twelve "
                     "words as another chapter.")

    for n in notes:
        print(f"  note: {n}\n")

    if fails:
        print("## FAIL — this is not a manuscript\n")
        for f in fails:
            print(f"  - {f}")
        print("\nDo not proceed to revise, polish, or package. Length compliance is")
        print("meaningless here: the word count is real and the words are not a book.")
        print("The work is to draft the scenes that the specification describes.")
        sys.exit(1)

    print("## PASS — reads as narrative prose")


if __name__ == "__main__":
    main()
