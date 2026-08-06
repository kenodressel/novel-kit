# Where the numbers in the templates come from

**Date:** 2026-08-06

Every threshold in `style-guide-template.md`, `eval-rubric-template.md`, `scenes-template.md`, and the gate in `draft.md` was measured. This document records how, so the numbers can be challenged rather than trusted.

## Corpora

- **Drafts**: 7 substantially complete novels produced by this pipeline, 349,215 words. Contemporary romance, Regency romance, literary fiction, near-future science fiction. Note that they span four pipeline generations, so a pattern present in all seven has survived four rounds of template revision.
- **Published**: 6 novels, 748,751 words. Sarah J. Maas (×2), Rebecca Yarros, Martha Wells, Adrian Tchaikovsky — trade — and one self-published 2025 romantasy, included deliberately as the market the drafts actually compete in.

## Method

Blind comparative reading. Extracts were stripped of titles, chapter headings, and epigraphs, labelled with neutral letters, and mixed. Evaluators were never told that two groups existed, that any text was machine-generated, or what to look for. Each pass ran twice with independent evaluators; agreement is reported.

Mechanical counts were run over the full texts, not the extracts.

## Results

### Construction signature — the hardest number here

| | Loose `with the [X] of` | Used to characterise a person (`…of someone who`) |
|---|---|---|
| Published, 748,751 words | 288 (38.5 per 100k) | **0** |
| Drafts, 349,215 words | 508 (145.5 per 100k) | **218** |

Published prose uses the phrase constantly, for ordinary purposes — *with the exception of*, *with the intention of*, *with the heels of my hands*. It never uses it to describe a person. The drafts do so 218 times, roughly once per 1,600 words, and in one novel once per 745.

This is the basis for the 1-per-10,000-word budget in `style-guide-template.md`.

### Chapter openings (850-word extracts, 7 drafts vs 6 published, two evaluators)

| Metric | Published | Drafts |
|---|---|---|
| Words to first intentional act | 84–147 | 426–513 |
| Explicit want on the page | 5 of 6 | 1–2 of 7 |
| Closes by stating its own significance | 1–2 of 6 | 3–4 of 7 |
| Narrative-voice specificity (1–5) | 4.17 / 4.17 | 2.86 / 3.00 |

One evaluator separated the two groups perfectly without knowing they existed; the other placed one draft chapter sixth of thirteen and otherwise matched. This is the basis for the 250-word runway fail condition.

### Mid-book chapters (same method, chapter at ~55% of each book)

The separation collapses. Both evaluators placed a draft chapter in the top three, and both placed a Maas chapter ninth of thirteen. But the bottom four ranks were the same four draft chapters for both evaluators.

| Metric | Published | Drafts |
|---|---|---|
| Words to first intentional act | 105–121 | 206–249 |
| Explicit want | 4 of 6 | 5–6 of 7 |
| Pressure (1–5) | 3.0–3.2 | 3.1–3.9 |
| Scene turns | 4 of 6 | 5–6 of 7 |
| Voice specificity | 3.75 / 3.67 | 2.64 / 2.71 |

Want, pressure, and scene turn are equal or better mid-book. **The competence-display problem is specific to openings, not general to the pipeline.** Voice specificity is the only gap that does not close with book position.

### Developmental read (5,000-word spans, three evaluators)

Ranked against published books on structure rather than prose, the drafts do better than the opening test suggests. One draft was ranked strongest of three against a Maas novel. Another was ranked strongest of four against the self-published title, which was ranked **weakest**, with the note: *"this is a first draft, and the other three are not."*

Defects found at this length that are invisible at 850 words:

- Thesis restatement 3–12 times per novel. Worst: one phrase 12 times in 5,500 words; one whole closing sentence duplicated near-verbatim 150 lines apart.
- One scene shape repeated for every scene in a span, four for four, including in the published Maas novel.
- POV broken to deliver information the POV character cannot have — flash-forwards, second interiors, second-person address.
- Single-engine dialogue: every character using one rhetorical move, twelve-year-olds indistinguishable from adults.
- Causal continuity breaks, not just detail slips: a character reporting a lease signed three days later, and a private conversation nobody witnessed.
- In three of four extracts, no force in the story capable of resisting the protagonist except the protagonist.

### Held-constant generation test

A published novel was reverse-engineered into this pipeline's artifacts — premise, vision, measured style guide, characters, world, outline, and one fully specified opening scene. A separate agent then drafted chapter one from those artifacts alone, with no access to the source.

Blind against the original and two trade-published openings in the same genre and person, both evaluators ranked: **generated first, original last.** Voice specificity 5/5 for the generated chapter, 2/2 for the original. Both evaluators independently recognised the two as the same scene.

Both also qualified it: *"A is the most finished page, but the two most finished books are almost certainly C and D."* One chapter is not a book.

The mechanism matters more than the result. The reverse-engineered specification carried numbers the pipeline's own templates do not: a runway target of 145 words, beat positions anchored to word counts, a measured sentence-length distribution, explicit prohibitions, and a stated POV/tense decision. Same pipeline, same model, better specification.

**The pipeline's weakness is specification, not execution.** That is what the template changes of 2026-08-06 address.

## What this does not establish

- Extracts of 850–5,000 words, and one generated chapter. Nothing here measures whether a book holds over 90,000 words.
- All evaluators were the same model family, so their agreement is correlated. The mechanical counts are not affected; the rankings are.
- The published set is romantasy and science fiction; the drafts are contemporary and Regency romance. For runway and want this is a real confound, partly offset by a Maas opening that begins with a woman vomiting and by one draft that reached a 90-word runway in a suburban comedy. For the construction counts and voice scores it does not apply.
- No claim is supported about machine versus human writing. Every failure mode above was also measured in a human-written self-published novel, at comparable or higher rates.
