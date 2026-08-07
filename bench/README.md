# bench — measurement for the pipeline

Seven linters. They count things a reader notices and an author does not, over a whole manuscript or a whole corpus. They produce pointers, never verdicts: read every flagged passage before changing it, because a script cannot tell a deliberate refrain from a forgotten one.

Python 3, standard library only. Run from the repository root.

```
python3 bench/lint/prose_sanity.py     novels/<slug>            # is it prose at all?
python3 bench/lint/specs.py            novels/<slug>            # BEFORE drafting
python3 bench/lint/wordcount.py        novels/<slug>            # after drafting
python3 bench/lint/fingerprint.py <file-or-novel-dir> [more…]   # any text, side by side
python3 bench/lint/repetition.py       novels/<slug> [--top N] [--budget N]
python3 bench/lint/continuity_facts.py novels/<slug>
python3 bench/lint/names.py           [novels/<slug>]
```

| Script | What it reports |
|---|---|
| `prose_sanity.py` | Asks whether the manuscript is narrative prose at all: unique-sentence ratio, scaffolding phrases (`during beat 8`), verbatim duplicate paragraphs, dialogue share, chapters sharing an opening. Exits 1. Run before every other prose check — the rest all assume prose and measure how good it is. |
| `specs.py` | Validates `scenes.md` **before drafting**: beats per chapter, word estimates, runway targets, prohibitions, whether estimates sum to target, and whether any chapter claims more length than it specifies story for. Exits 1 on failure. |
| `wordcount.py` | Actual words per chapter against the scene estimate, total against target, whether `novel.md`'s count matches reality, and whether the target has been rewritten to match the output. Exits 1 on failure. |
| `fingerprint.py` | Sentence-length distribution and median, paragraph shape, dialogue share, `said` ratio, punctuation rates, simile rate — for a novel or any comparison text, several side by side. This is how you fill the measured table in `style-guide-template.md`. |
| `repetition.py` | Construction signatures per 10,000 words (characterising appositive, negation triad, inanimate volition, filter verbs, crutch words); phrases recurring above budget; near-duplicate sentences; in-chapter frequency outliers. |
| `continuity_facts.py` | Every price, age, span, and clock time grouped by the noun it attaches to, with contradictions flagged; calendar tokens per chapter; numbers in `continuity.md` absent from the prose. |
| `names.py` | Proper nouns shared between novels in this repository, and place names assembled from the two-morpheme nature kit. |

## Where they belong in the pipeline

`specs.py` is the one with the most leverage, because it runs before any prose exists. A chapter comes out the size of its specification: a run whose scene blocks carried a goal, a conflict and an outcome but no beats produced 28 chapters with a median of 497 words against a 2,500-word estimate, and `/novel.realize` added nothing, correctly — it expands toward specified beats and cannot expand toward beats nobody wrote. Checking that before drafting costs milliseconds; discovering it afterwards costs the manuscript.

`wordcount.py` belongs at the step boundary and inside `/novel.realize`, **not after every chapter**. Drafting is allowed to come in short; that is what realize is for, and halting the draft to do the next step's work only stalls the run. Per chapter, log the number and keep going.

Read `wordcount.py` before any other output, though, because length changes how the rest is read. Every shape metric improves as chapters get shorter — a scene sketch has no room for the establishing-shot inventory that produces a long runway or a hollow middle. A chapter under 80% of its estimate has not passed the shape checks; it has not taken them.

`/novel.revise` runs `wordcount`, `repetition`, `continuity_facts`, `names` and `fingerprint` as its required Pass 0, before any reading pass.

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
