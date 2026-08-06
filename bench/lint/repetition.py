#!/usr/bin/env python3
"""Report repetition inside a novel: recurring phrases, near-duplicate sentences,
in-chapter word-frequency outliers, and the construction signatures from the style guide.

    python3 bench/lint/repetition.py novels/<slug> [--top N]

Pointers, not verdicts. Read every flagged passage before changing it -- a script
cannot tell a deliberate refrain from a forgotten one.
"""
import argparse
import pathlib
import re
import sys
from collections import Counter, defaultdict

# Constructions measured as unedited-draft signatures. See templates/commands/revise.md.
SIGNATURES = {
    "characterising appositive": re.compile(
        r"\bwith (?:the|a|an) [a-z\-]+(?:,? [a-z\-]+){0,3} of "
        r"(?:someone|somebody|people|a|an|the)\b[^.;!?]{0,60}?\bwho\b", re.I),
    "appositive (of a man/woman)": re.compile(
        r"\bwith (?:the|a|an) [a-z\-]+(?:,? [a-z\-]+){0,3} of "
        r"(?:a|an) (?:man|woman|person|child|girl|boy)\b", re.I),
    "negation triad": re.compile(r"(?<=[.!?])\s+Not (?:a|an|the|much|quite|because)\b"),
    "not X but Y": re.compile(r"\bnot (?:a|an|the|because|that|much|quite)\b[^.;!?]{0,80}?\bbut\b", re.I),
    "inanimate volition": re.compile(
        r"\bas (?:if|though) (?:it|they|the \w+) "
        r"(?:did ?n['o]?t|didn't|knew|believed|wanted|intended|resented|expected|"
        r"preferred|had decided)\b", re.I),
    "seemed to <mental verb>": re.compile(
        r"\bseemed to (?:want|know|believe|intend|resent|expect|prefer|regret)\b", re.I),
    "the way <X> does": re.compile(r"\bthe way (?:a|an|the|you|people|\w+s)\b", re.I),
    "crutch: specific/particular": re.compile(r"\b(?:specific|particular)(?:ly|ity)?\b", re.I),
    "filter verbs": re.compile(
        r"\b(?:felt|seemed|noticed|realized|realised|watched as|could tell|found (?:him|her)self)\b", re.I),
}

STOP = set("""a an the and or but if then than that this these those of in on at to for with from by as is
are was were be been being it its it's he she they them his her their our your you i we me my mine not no
nor so too very can will just don't dont should would could had has have having do does did what which who
whom whose when where why how all any both each few more most other some such only own same s t d ll m o re
ve y ain aren couldn didn doesn hadn hasn haven isn ma mightn mustn needn shan shouldn wasn weren won wouldn
said says say back down out up over under again there here now still even about into through after before
one two three four five six seven eight nine ten first last next another something anything nothing everything
someone anyone everyone nobody himself herself themselves myself like well much many long good great little
old new right left way thing things time times day days year years man woman men women""".split())

WORD = re.compile(r"[A-Za-z][A-Za-z'\-]+")


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


def ngrams(tokens, n):
    return [" ".join(tokens[i:i + n]) for i in range(len(tokens) - n + 1)]


def interesting(phrase: str) -> bool:
    """Filter ordinary English. Keep a phrase only if it carries an uncommon
    content word, or is long enough that recurrence is unlikely by chance."""
    words = phrase.split()
    if len(words) >= 6:
        return True
    return any(w not in STOP for w in words[1:-1]) and sum(w not in STOP for w in words) >= 2


def normalise(s: str) -> str:
    return " ".join(WORD.findall(s.lower()))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("novel", type=pathlib.Path)
    ap.add_argument("--top", type=int, default=25)
    ap.add_argument("--budget", type=int, default=3,
                    help="max permitted recurrences of a distinctive phrase (see style-guide.md)")
    a = ap.parse_args()

    chs = chapters(a.novel)
    total_words = sum(len(t.split()) for _, t in chs)
    print(f"# {a.novel.name} — {len(chs)} chapters, {total_words:,} words\n")

    # ---- construction signatures, per 10k words
    print("## Construction signatures (per 10,000 words)\n")
    print(f"{'signature':32s} {'count':>6s} {'/10k':>7s}")
    for name, rx in SIGNATURES.items():
        n = sum(len(rx.findall(t)) for _, t in chs)
        print(f"{name:32s} {n:6d} {n / total_words * 1e4:7.1f}")
    print("\nThe first two lines are the highest-signal marker. Published reference: 0.0 per 10k.\n")

    # ---- cross-chapter phrase recurrence
    print(f"## Phrases recurring more than {a.budget}x across the manuscript\n")
    counts, where = Counter(), defaultdict(set)
    for name, text in chs:
        toks = WORD.findall(text.lower())
        for n in (4, 5, 6, 7, 8):
            for g in ngrams(toks, n):
                if interesting(g):
                    counts[g] += 1
                    where[g].add(name)
    # drop phrases fully contained in a more frequent longer phrase
    hits = [(g, c) for g, c in counts.items() if c > a.budget]
    hits.sort(key=lambda kv: (-kv[1], -len(kv[0])))
    kept = []
    for g, c in hits:
        if any(g in longer and c <= lc for longer, lc in kept):
            continue
        kept.append((g, c))
    for g, c in kept[:a.top]:
        print(f"  {c:3d}x  in {len(where[g])} ch  \"{g}\"")
    if not kept:
        print("  (none)")

    # ---- near-duplicate sentences across chapters
    print("\n## Near-duplicate sentences (>=10 words, same normalised form in 2+ places)\n")
    seen = defaultdict(list)
    for name, text in chs:
        for s in re.split(r"(?<=[.!?])\s+", text):
            k = normalise(s)
            if len(k.split()) >= 10:
                seen[k].append((name, " ".join(s.split())[:110]))
    dupes = [(k, v) for k, v in seen.items() if len(v) > 1]
    for k, v in sorted(dupes, key=lambda kv: -len(kv[1]))[:a.top]:
        print(f"  {len(v)}x  {', '.join(n for n, _ in v)}")
        print(f"        \"{v[0][1]}\"")
    if not dupes:
        print("  (none)")

    # ---- in-chapter frequency outliers
    print("\n## In-chapter word-frequency outliers (>=4x in one chapter, rare elsewhere)\n")
    corpus = Counter()
    per = []
    for name, text in chs:
        c = Counter(w for w in (x.lower() for x in WORD.findall(text)) if w not in STOP and len(w) > 4)
        per.append((name, c))
        corpus.update(c)
    for name, c in per:
        flagged = [(w, n) for w, n in c.items() if n >= 4 and corpus[w] <= n * 1.6]
        if flagged:
            flagged.sort(key=lambda kv: -kv[1])
            joined = ", ".join(f"{w} x{n}" for w, n in flagged[:8])
            print(f"  {name}: {joined}")


if __name__ == "__main__":
    main()
