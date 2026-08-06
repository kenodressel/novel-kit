#!/usr/bin/env python3
"""Extract quantitative facts from each chapter and report contradictions.

    python3 bench/lint/continuity_facts.py novels/<slug>

Catches the class of error a reader notices and an author does not: a price that
is eleven dollars, then eighteen, then "$8.50, same as always"; a business that is
six years old and also three; a Thursday that becomes a Tuesday in the same night.

It groups numbers by the noun they attach to and flags any group with more than one
value. Most flags will be legitimate -- different characters, different objects,
deliberate change over time. Read them; the point is to make the set small enough
to read.
"""
import argparse
import pathlib
import re
import sys
from collections import defaultdict

MONEY = re.compile(r"\$\s?([\d,]+(?:\.\d{2})?)|\b([\d,]+)\s+dollars?\b", re.I)
AGE = re.compile(r"\b(?:(\w+|\d+)[\s-]year[\s-]old|aged (\d+)|was (\d+) years old)\b", re.I)
SPAN = re.compile(r"\b(\w+|\d+)\s+(second|minute|hour|day|week|month|year|mile|block|pace|foot|feet|inch|"
                  r"seconds|minutes|hours|days|weeks|months|years|miles|blocks|paces|inches)\b", re.I)
CLOCK = re.compile(r"\b(\d{1,2}:\d{2}\s?(?:a\.?m\.?|p\.?m\.?)?|"
                   r"\d{1,2}\s?(?:a\.?m\.?|p\.?m\.?)|"
                   r"(?:noon|midnight))\b", re.I)
WEEKDAY = re.compile(r"\b(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\b")
MONTH = re.compile(r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\b")
SEASON = re.compile(r"\b(?:early |mid[- ]|late )?(spring|summer|autumn|fall|winter)\b", re.I)

WORDNUM = {w: i for i, w in enumerate(
    "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen "
    "sixteen seventeen eighteen nineteen twenty".split())}
WORDNUM.update({"thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
                "eighty": 80, "ninety": 90, "hundred": 100, "thousand": 1000})


def num(tok: str):
    if tok is None:
        return None
    t = tok.replace(",", "").strip().lower()
    if re.fullmatch(r"\d+(?:\.\d+)?", t):
        return float(t)
    return float(WORDNUM[t]) if t in WORDNUM else None


def chapters(novel: pathlib.Path):
    files = sorted((novel / "manuscript").glob("chapter-*.md"))
    if not files:
        sys.exit(f"no chapter-*.md under {novel / 'manuscript'}")
    return [(f.name, "\n".join(l for l in f.read_text(encoding="utf-8").splitlines()
                               if not l.lstrip().startswith("#")).strip()) for f in files]


def context(text: str, at: int, width: int = 70) -> str:
    lo, hi = max(0, at - width), min(len(text), at + width)
    return " ".join(text[lo:hi].split())


def subject(text: str, at: int) -> str:
    """The nearest preceding content noun, used as a crude grouping key."""
    before = re.findall(r"[A-Za-z][a-z']{3,}", text[max(0, at - 90):at])
    return before[-1].lower() if before else "?"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("novel", type=pathlib.Path)
    a = ap.parse_args()
    chs = chapters(a.novel)
    print(f"# {a.novel.name} — quantitative continuity, {len(chs)} chapters\n")

    groups = defaultdict(list)      # (kind, key) -> [(value, chapter, quote)]
    calendar = defaultdict(set)     # chapter -> {weekday/month/season tokens}

    for name, text in chs:
        for m in MONEY.finditer(text):
            v = num(m.group(1) or m.group(2))
            if v is not None:
                groups[("money", subject(text, m.start()))].append((v, name, context(text, m.start())))
        for m in AGE.finditer(text):
            v = num(m.group(1) or m.group(2) or m.group(3))
            if v is not None:
                groups[("age", subject(text, m.start()))].append((v, name, context(text, m.start())))
        for m in SPAN.finditer(text):
            v = num(m.group(1))
            if v is not None:
                unit = m.group(2).lower().rstrip("s")
                groups[(f"{unit}s", subject(text, m.start()))].append((v, name, context(text, m.start())))
        for rx in (WEEKDAY, MONTH, SEASON):
            for m in rx.finditer(text):
                calendar[name].add(m.group(0).strip().lower())

    print("## Same noun, different number\n")
    shown = 0
    for (kind, key), items in sorted(groups.items()):
        values = {v for v, _, _ in items}
        if len(values) > 1 and len(items) > 1:
            print(f"  [{kind}] \"{key}\": {sorted(values)}")
            for v, ch, q in items[:4]:
                print(f"      {ch}: …{q}…")
            print()
            shown += 1
    if not shown:
        print("  (none)\n")

    print("## Calendar tokens per chapter (a chapter naming two weekdays is worth a look)\n")
    for name, _ in chs:
        toks = sorted(calendar.get(name, ()))
        if toks:
            days = [t for t in toks if t.capitalize() in
                    ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")]
            flag = "  <-- two weekdays in one chapter" if len(days) > 1 else ""
            print(f"  {name}: {', '.join(toks)}{flag}")

    print("\n## Clock times in order of appearance (check the arithmetic by hand)\n")
    for name, text in chs:
        times = [m.group(0) for m in CLOCK.finditer(text)]
        if len(times) > 1:
            print(f"  {name}: {', '.join(times)}")

    cont = a.novel / "story" / "continuity.md"
    if cont.exists():
        print("\n## Numbers in continuity.md not found anywhere in the manuscript\n")
        body = cont.read_text(encoding="utf-8")
        manuscript = " ".join(t for _, t in chs)
        missing = []
        for tok in set(re.findall(r"\b\d[\d,]{1,9}\b", body)):
            if tok not in manuscript and tok.replace(",", "") not in manuscript:
                missing.append(tok)
        print("  " + (", ".join(sorted(missing)) if missing else "(none)"))
    else:
        print(f"\n(no {cont} — skipping the continuity-bible cross-check)")


if __name__ == "__main__":
    main()
