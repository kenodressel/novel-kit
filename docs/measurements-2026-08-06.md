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

### Sentence-shape distribution — the second clean separator

Measured mechanically over full texts with `bench/lint/fingerprint.py`, 8 drafts against 6 published novels:

| | Share 12-25 words | Share 1-3 words | Median sentence |
|---|---|---|---|
| Drafts | 14.3 – **22.5%** | **19.8** – 28.3% | 5 – 7 |
| Published | **30.9** – 41.6% | 5.3 – **17.6%** | 9 – 13 |

No overlap on any of the three. The diagnosis is a hollow middle rather than short sentences as such: the drafts alternate fragments with long sentences and largely skip the 12-to-25-word range where published prose spends a third to two-fifths of its time. This is the basis for the 25% mid-band floor and the 8-word median floor in the draft gate.

Corroborating evidence from the generation test: when drafting against a style guide that specified a 9/18/39/30 distribution, the drafter reported hitting 17/27/28/25 and named the cause — three separate mandates (clipped dialogue, fragment ladders at emotional spikes, a low paragraph floor) all pushing the same direction at once.

### Metrics measured and rejected

Recorded so they are not re-derived as findings:

- **Em-dash rate.** Drafts median 138 per 10,000 words, published median 32 — a large gap that looks conclusive until you see that two Maas novels sit at 129.5 and 136.3, inside the draft range. A "fewer em-dashes" rule would have flagged a bestselling author as machine-written.
- **Semicolons, colons, ellipses, parentheses.** Published usage varies by two orders of magnitude between authors.

This is the validity guard from the 2026-08-04 spec doing its job: *until a reference exists, only extreme outliers count, and never "less is better."* Without it, two of these would have become template rules.

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

## Controlled re-draft — the verification of the 2026-08-06 template changes

The test case: `untitled-scifi` chapter 12, chosen because two blind evaluators had independently ranked it last of thirteen mid-book chapters. Same story, same characters, same events, same outcome. The only variable changed was the specification.

One agent re-specified the existing chapter into the new `scenes-template.md` and `style-guide.md` formats — measured fingerprint from two SF comps, runway target, beats anchored to word positions, prohibitions, closing move. A second agent drafted from that spec alone, with a hard prohibition on opening the existing chapter.

Mechanical result, verified independently rather than taken from the drafter's self-report:

| | old | new | published band |
|---|---|---|---|
| Median sentence length | 7 | **11** | 9 – 13 |
| Share 12-25 words | 24.1% | **39.7%** | 31 – 42% |
| Share 1-3 words | 18.6% | **6.3%** | 5 – 18% |
| Appositive family per 10k | 56.0 | **0.0** | ~0 |
| Em-dashes per 10k | 173.3 | **24.0** | 5 – 136 |

The old chapter sat outside the published band on all three discriminating metrics; the new one is inside all three.

The em-dash row is the instructive one. The drafter was given **no** em-dash target, because the template records that metric as non-discriminating. The rate fell by a factor of seven anyway, as a side effect of writing mid-length sentences instead of dash-spliced fragments. The em-dash flood was a symptom of the hollow middle, not an independent habit — which is exactly why banning em-dashes would have treated the symptom.

Blind evaluation, two evaluators, the two versions mixed with two published SF mid-book chapters, no evaluator told that a matched pair was present:

| | old | new |
|---|---|---|
| Rank of four | 4, 4 | **2, 2** |
| Voice specificity | 2, 2 | **5, 4** |
| Runway as judged | 380, 700 | **0–25** |
| Pressure | 3, 3 | **4, 4** |
| Scene turn | "barely", "no" | **yes, yes** |
| Closes on a gloss | yes, yes | **no, no** |

Both placed the new version above a published Tchaikovsky chapter and both named the old version least finished, at high confidence. Both independently recognised the pair as two drafts of one scene, and both located the difference in the same place: the new version stages an observation and stops; the old version stages it and then explains it.

### What this verification does not prove

- One chapter. The claim is that the specification change moves a chapter, not that it produces a good book.
- Part of the gain came from the re-specification agent discovering nine contradictions already sitting in the artifacts — a one-year date drift across all of Part Two, two hospital names, three mutually exclusive claims about a character's backstory, and three consecutive chapters ending on the same image. The new template's required fields are what surfaced them, but fixing them is a separate effect from the fields themselves.
- The drafter never saw the old version, but it is the same model family, so some improvement may be second-attempt effect rather than specification quality.
- Cost: roughly 320,000 subagent tokens for one chapter, across re-specification and drafting. This is not a cheap procedure, and the specification work amortises across a book while the drafting does not.
- The new draft still missed two style targets and reported seven further spec problems, including an unverified clinical pathway. It passed the gate; it is not finished.

## What this does not establish

- Extracts of 850–5,000 words, and one generated chapter. Nothing here measures whether a book holds over 90,000 words.
- All evaluators were the same model family, so their agreement is correlated. The mechanical counts are not affected; the rankings are.
- The published set is romantasy and science fiction; the drafts are contemporary and Regency romance. For runway and want this is a real confound, partly offset by a Maas opening that begins with a woman vomiting and by one draft that reached a 90-word runway in a suburban comedy. For the construction counts and voice scores it does not apply.
- No claim is supported about machine versus human writing. Every failure mode above was also measured in a human-written self-published novel, at comparable or higher rates.
