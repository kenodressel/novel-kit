# bench — measurement for the pipeline

Three linters. They count things a reader notices and an author does not, over a whole manuscript or a whole corpus. They produce pointers, never verdicts: read every flagged passage before changing it, because a script cannot tell a deliberate refrain from a forgotten one.

Python 3, standard library only. Run from the repository root.

```
python3 bench/lint/repetition.py       novels/<slug> [--top N] [--budget N]
python3 bench/lint/continuity_facts.py novels/<slug>
python3 bench/lint/names.py           [novels/<slug>]
```

```
python3 bench/lint/specs.py            novels/<slug>            # BEFORE drafting
python3 bench/lint/wordcount.py        novels/<slug>            # after drafting
python3 bench/lint/fingerprint.py <file-or-novel-dir> [more…]   # side-by-side prose fingerprint
```

**Run `wordcount.py` before reading any other output.** Every shape metric here improves as chapters get shorter — a scene sketch has no room for the establishing-shot inventory that produces a long runway or a hollow middle. A manuscript short of its own specification scores *well*, which is the opposite of useful.

Length tells you how to read the rest; it is not a brake on the pipeline. Drafting is allowed to come in short — `/novel.realize` exists for exactly that — so `wordcount.py` belongs at the step boundary and in realize, not after every chapter. Per chapter, log the number and keep going.

| Script | What it reports |
|---|---|
| `specs.py` | Validates `scenes.md` **before drafting**: beats per chapter, word estimates, runway targets, prohibitions, whether estimates sum to target, and whether any chapter claims more length than it specifies story for. Exits 1 on failure. The cheapest check here and the one with the most leverage, because it runs before any prose exists. |
| `wordcount.py` | Actual words per chapter against the scene spec's estimate, manuscript total against target, whether `novel.md`'s recorded count matches reality, and whether the target has been rewritten to match the output. Exits 1 on failure so it can gate a step. |

| Script | What it reports |
|---|---|
| `fingerprint.py` | Sentence-length distribution and median, paragraph shape, dialogue share, `said` ratio, punctuation rates, simile rate — for a novel or any comparison text, several side by side. This is how you fill the measured table in `style-guide-template.md`. |
| `repetition.py` | Construction signatures per 10,000 words (characterising appositive, negation triad, inanimate volition, filter verbs, crutch words); phrases recurring above budget across chapters; near-duplicate sentences; in-chapter word-frequency outliers |
| `continuity_facts.py` | Every price, age, span, and clock time grouped by the noun it attaches to, with contradictions flagged; calendar tokens per chapter; numbers in `continuity.md` absent from the prose |
| `names.py` | Proper nouns shared between novels in this repository, and place names assembled from the two-morpheme nature kit |

`/novel.revise` runs all three as its required Pass 0, before any reading pass.

## Reference points

The thresholds in the templates are measured, not invented. Where a number appears in `style-guide-template.md` or `eval-rubric-template.md`, it came from comparing a 349,000-word corpus of unedited drafts against 749,000 words of published fiction by five authors:

| | Published | Unedited drafts |
|---|---|---|
| `with the [abstract noun] of [someone] who…` used to describe a person | **0** in 749,000 words | 218 in 349,000 words |
| Words before the POV character acts, chapter openings | 84–147 | 426–513 |
| Explicit want on the page, chapter one | 5 of 6 | 1–2 of 7 |
| Narrative-voice specificity, blind 1–5 | 4.17 | 2.9 |

## What these linters are not

They do not detect machine-generated prose. Every failure mode they measure was also found, at comparable or higher rates, in an unedited self-published novel written by a human — including the arithmetic contradictions, the seven-fold thesis restatement, and the single repeated scene shape. Two blind readers ranked one of this pipeline's chapters above two trade-published bestsellers, and ranked the human-written self-published book last of four.

The useful conclusion is not that machines write well or badly. It is that **the gap between an unedited draft and a finished book is measurable, and most of it is countable.** That is what these scripts count.

## Known limits

- `repetition.py`'s inanimate-volition detector matches a narrow syntactic form and undercounts badly. A blind reader found 9–14 instances in 6,000 words where the regex finds well under one. Trust the reading pass over this number.
- `continuity_facts.py` groups numbers by the nearest preceding noun, which is crude. Expect legitimate flags — different characters, different objects, deliberate change over time. The goal is a set small enough to read, not a set of confirmed errors.
- `names.py` filters sentence openers by testing whether a word also appears lowercase in the same manuscript. Vocatives and interjections that never appear lowercase slip through; add them to `COMMON`.
- Detectors are English-only.

## Output

Written to stdout. Redirect into `bench/reports/` if you want to keep a run — that directory is gitignored, because the output quotes your manuscripts.
