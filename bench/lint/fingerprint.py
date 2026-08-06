#!/usr/bin/env python3
"""Measure the prose fingerprint of a manuscript or a comparison text.

    python3 bench/lint/fingerprint.py novels/<slug>              # a novel
    python3 bench/lint/fingerprint.py path/to/comp.txt           # a comparison text
    python3 bench/lint/fingerprint.py a.txt b.txt novels/<slug>  # side by side

Produces the numbers that `style-guide-template.md` asks for. Fill that template
by running this over 3-5 comps you want the book to read like, then set targets
inside the observed range -- not at the mean of it, which is how books come to read
like the average of their influences.

Variance is the signal. Two books with the same mean sentence length read nothing
alike if one clusters at the mean and the other swings.
"""
import argparse
import pathlib
import re
import statistics
import sys

SENT = re.compile(r"(?<=[.!?])[\"'”’]?\s+")
WORD = re.compile(r"[A-Za-z][A-Za-z'\-]*")
# Straight and curly quote pairs, plus the guillemets and low-9 quotes German uses.
DIALOGUE = re.compile(r"[\"“„«](.+?)[\"”“»]", re.S)
ATTRIB = re.compile(r"\b(said|asked|replied|whispered|muttered|shouted|answered|added|"
                    r"murmured|snapped|called|told|breathed|offered|admitted)\b", re.I)
SIMILE = re.compile(r"\b(?:like|as (?:if|though))\b", re.I)
BANDS = ((1, 3), (4, 11), (12, 25), (26, 10**6))


def load(target: pathlib.Path) -> tuple[str, str]:
    """Return (label, text). Accepts a novel directory or a plain text/markdown file."""
    if target.is_dir():
        files = sorted((target / "manuscript").glob("chapter-*.md"))
        if not files:
            files = sorted(target.glob("chapter-*.md"))
        if not files:
            sys.exit(f"no chapter-*.md under {target}")
        parts = ["\n".join(l for l in f.read_text(encoding="utf-8").splitlines()
                           if not l.lstrip().startswith("#")) for f in files]
        return target.name, "\n\n".join(parts)
    if not target.exists():
        sys.exit(f"no such path: {target}")
    text = target.read_text(encoding="utf-8", errors="ignore")
    if target.suffix == ".md":
        text = "\n".join(l for l in text.splitlines() if not l.lstrip().startswith("#"))
    return target.stem[:22], text


def measure(text: str) -> dict:
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    sents = [s for s in SENT.split(text) if WORD.search(s)]
    lens = [len(WORD.findall(s)) for s in sents]
    words = WORD.findall(text)
    n_words = len(words) or 1

    dialogue_words = sum(len(WORD.findall(m.group(1))) for m in DIALOGUE.finditer(text))
    attribs = ATTRIB.findall(text)
    said = sum(1 for a in attribs if a.lower() == "said")

    m = {
        "words": n_words,
        "sentences": len(sents),
        "paragraphs": len(paras),
        "mean sentence": statistics.mean(lens) if lens else 0,
        "median sentence": statistics.median(lens) if lens else 0,
        "stdev sentence": statistics.pstdev(lens) if len(lens) > 1 else 0,
        "longest sentence": max(lens) if lens else 0,
        "mean paragraph": statistics.mean([len(WORD.findall(p)) for p in paras]) if paras else 0,
        "paras <=8 words %": 100 * sum(1 for p in paras if len(WORD.findall(p)) <= 8) / (len(paras) or 1),
        "dialogue words %": 100 * dialogue_words / n_words,
        "said / attributions %": 100 * said / (len(attribs) or 1),
        "attributions per 1k": len(attribs) / n_words * 1000,
        "semicolons per 10k": text.count(";") / n_words * 1e4,
        "parentheses per 10k": text.count("(") / n_words * 1e4,
        "colons per 10k": text.count(":") / n_words * 1e4,
        "em-dashes per 10k": (text.count("—") + text.count(" -- ")) / n_words * 1e4,
        "ellipses per 10k": (text.count("…") + text.count("...")) / n_words * 1e4,
        "similes per 1k": len(SIMILE.findall(text)) / n_words * 1000,
    }
    for lo, hi in BANDS:
        key = f"sent {lo}-{hi if hi < 10**6 else '+'} %"
        m[key] = 100 * sum(1 for x in lens if lo <= x <= hi) / (len(lens) or 1)
    return m


ORDER = ["words", "sentences", "paragraphs",
         "mean sentence", "median sentence", "stdev sentence", "longest sentence",
         "sent 1-3 %", "sent 4-11 %", "sent 12-25 %", "sent 26-+ %",
         "mean paragraph", "paras <=8 words %",
         "dialogue words %", "attributions per 1k", "said / attributions %",
         "semicolons per 10k", "parentheses per 10k", "colons per 10k",
         "em-dashes per 10k", "ellipses per 10k", "similes per 1k"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("targets", nargs="+", type=pathlib.Path)
    a = ap.parse_args()

    cols = [load(t) for t in a.targets]
    results = [(label, measure(text)) for label, text in cols]

    width = max(14, max(len(l) for l, _ in results) + 2)
    print(f"{'metric':24s}" + "".join(f"{l:>{width}s}" for l, _ in results))
    print("-" * (24 + width * len(results)))
    for key in ORDER:
        row = f"{key:24s}"
        for _, m in results:
            v = m[key]
            row += f"{v:>{width},.0f}" if key in ("words", "sentences", "paragraphs",
                                                  "longest sentence") else f"{v:>{width}.1f}"
        print(row)

    if len(results) > 1:
        print("\nSet targets inside the observed range, not at its mean.")


if __name__ == "__main__":
    main()
