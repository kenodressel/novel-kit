#!/usr/bin/env python3
"""Report proper nouns shared between novels, and invented-compound place names.

    python3 bench/lint/names.py            # every novel under novels/
    python3 bench/lint/names.py novels/<slug>   # one novel against all the others

Nothing in the pipeline reads what previous novels already used, so names collide.
Measured: the same house name appearing in two unrelated novels, and five settlements
across a corpus built from one two-morpheme nature kit -- Briarwood, Willowbrook,
Thornfield, Ridgeline, Saltwick.
"""
import argparse
import pathlib
import re
import sys
from collections import defaultdict

# Capitalised token that is NOT sentence-initial and not a common opener.
CANDIDATE = re.compile(r"(?<![.!?\"'\n]\s)(?<!^)\b([A-Z][a-z]{2,})\b")
COMMON = set("""The A An And But Or If So Then When Where While After Before Because Not No Yes She He
They It We You I His Her Their Its Our My Mr Mrs Ms Dr Sir Lady Lord God Christmas Easter Monday Tuesday
Wednesday Thursday Friday Saturday Sunday January February March April May June July August September
October November December English French German American British Spanish Italian
Hey Hi Hello Thank Thanks Yeah Okay Oh Ah Well Sorry Please Sure Nope Yep Excuse Goodbye Morning
Mom Mum Mama Dad Papa Grandma Grandpa Don Dona Senor Senora Madam Madame Miss Uncle Aunt Jesus Christ""".split())

# The two-morpheme nature kit that unedited fantasy/contemporary drafts reach for.
MORPHEMES = ("briar", "willow", "thorn", "ridge", "salt", "wick", "field", "brook", "wood", "haven",
             "stone", "hollow", "vale", "moor", "crest", "mere", "fell", "shaw", "combe", "burn",
             "ash", "oak", "elm", "black", "white", "grey", "gray", "iron", "gold", "silver",
             "north", "south", "east", "west", "high", "low", "old", "new", "bridge", "ford",
             "port", "bay", "cliff", "glen", "birch", "cedar", "fern", "frost", "storm", "dawn")


def names_in(novel: pathlib.Path) -> set:
    """Proper nouns in the prose only. Design documents are excluded -- they are
    built from templates, so their headings ("Conflict", "Outcome", "Notes") would
    otherwise be reported as names shared by every novel in the repository."""
    d = novel / "manuscript"
    if not d.is_dir():
        return set()
    texts = []
    for f in sorted(d.rglob("*.md")):
        texts.append("\n".join(l for l in f.read_text(encoding="utf-8").splitlines()
                               if not l.lstrip().startswith("#")))
    prose = "\n".join(texts)

    counts = defaultdict(int)
    for m in CANDIDATE.finditer(prose):
        counts[m.group(1)] += 1

    # A real proper noun almost never appears lowercase in the same book. This one
    # test removes sentence openers ("That", "Every", "For") and common nouns that
    # happen to start a line, which the positional lookbehind cannot catch reliably.
    lowercased = set(re.findall(r"\b([a-z][a-z']{2,})\b", prose))
    return {w for w, n in counts.items()
            if n >= 2 and w not in COMMON and w.lower() not in lowercased}


def compound(name: str):
    low = name.lower()
    parts = [p for p in MORPHEMES if p in low and len(p) >= 3]
    return parts if len(parts) >= 2 else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("novel", nargs="?", type=pathlib.Path)
    a = ap.parse_args()

    root = pathlib.Path("novels")
    if not root.is_dir():
        sys.exit("run from the repository root (no novels/ directory here)")
    novels = sorted(d for d in root.iterdir() if d.is_dir() and not d.name.startswith("."))
    if not novels:
        sys.exit("no novels found")

    per = {d.name: names_in(d) for d in novels}

    owners = defaultdict(list)
    for slug, names in per.items():
        for n in names:
            owners[n].append(slug)

    target = a.novel.name if a.novel else None

    print("## Proper nouns used in more than one novel\n")
    shared = {n: v for n, v in owners.items() if len(v) > 1}
    if target:
        shared = {n: v for n, v in shared.items() if target in v}
    if shared:
        for n, v in sorted(shared.items(), key=lambda kv: (-len(kv[1]), kv[0])):
            print(f"  {n:24s} {', '.join(sorted(v))}")
    else:
        print("  (none)")

    print("\n## Invented two-morpheme compounds (the nature-kit tell)\n")
    any_hit = False
    for slug, names in sorted(per.items()):
        if target and slug != target:
            continue
        hits = sorted(n for n in names if compound(n))
        if hits:
            any_hit = True
            print(f"  {slug}: {', '.join(hits)}")
    if not any_hit:
        print("  (none)")

    print("\nNames should come from a stated real-world regional convention for the setting.")
    print("Record the source in world.md so the next novel can avoid it.")


if __name__ == "__main__":
    main()
