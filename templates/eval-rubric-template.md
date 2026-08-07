# Evaluation Rubrics

Use a 1-5 scale for each subjective dimension. Measured dimensions are counts, not scores.

> **A solo 1-5 score by the context that produced the work clusters at 4 and passes everything.** Chapter and prose evaluation must be run blind and comparatively — see "Blind comparative scoring" in `evaluate.md`. A rubric filled in by the drafter, with the story artifacts in view, tests compliance with the style guide. It cannot see the failure mode where the prose has no idiom beyond the style guide's, because matching the style guide is what produces that.

## Premise

| Dimension | What to test |
|-----------|--------------|
| Novelty | Does it feel distinct rather than assembled from stock parts? |
| Collision | Two fails, and only two: a proper noun already used in another novel in `novels/`, or the same arc as an existing novel — the same engine producing the same shape of change. A shared occupation, setting archetype, or relationship shape is recorded as an overlap and passes. |
| Agency | Does the protagonist drive the story through meaningful choices? |
| Opposition | Is there a force outside the protagonist that wants something incompatible, and is its argument good? |
| Sustainability | Is there enough pressure for a full novel? |
| Stakes | Are the stakes concrete and emotionally charged? |
| Market clarity | Can a reader understand what kind of book this is? |

## Vision / Style

| Dimension | What to test |
|-----------|--------------|
| Voice specificity | Would this produce recognizable prose rather than model-default prose? |
| Deliberate configuration | Is this book's POV, tense, register, and prose fingerprint a stated choice? Matching the other novels in `novels/` is allowed; matching them by default is not. If the configuration is the corpus's most common one, there must be a sentence saying why it suits this book. |
| Checkability | Is the style guide measured, or does it still describe the prose in workshop adjectives? An unmeasurable guide cannot be enforced during drafting. |
| Aesthetic coherence | Do the style decisions point in one direction? |
| Thematic tension | Is there a real argument, not just a topic? |

## Outline / Scenes

| Dimension | What to test |
|-----------|--------------|
| Escalation | Does pressure intensify rather than just continue? |
| Clock | Is there a deadline outside the protagonist's feelings, and is it referenced after it is introduced? |
| Opposition quality | Name the character whose argument is better than the protagonist's, and quote it. If none exists, the protagonist is the only force capable of resisting the protagonist. |
| Scene shape variety | Do the scenes open, escalate, and close in *different* shapes? List the closing move of every scene in the act. If three or more share it, fail. |
| Surprise | Are major turns earned but not inertly predictable? |
| Telegraphing | Is any reveal signalled more than once before it lands? A reveal announced three times reveals nothing. |
| Redundancy risk | Are scenes doing distinct work? |
| Draftability | Are the beat positions arithmetically possible inside the target word count? |
| Hook strength | Do chapters/scenes pull the reader forward? |

## Chapter Draft / Realization

**Measured** — counts, recorded per chapter, no scoring:

> **Length changes how these numbers are read, not whether the pipeline may proceed.** Every metric in this table improves as a chapter gets shorter — a scene sketch has no room for the establishing-shot inventory that produces a long runway or a hollow middle. Measured: a run whose chapters averaged 960 words against a 2,500-word spec scored a better mid-band share than any fully drafted novel in the corpus.
>
> So run `bench/lint/wordcount.py` first, and for any chapter under 80% of its scene estimate, mark the rows below `n/a — short` rather than `pass`. A short chapter has not passed these checks; it has not taken them. Length itself is enforced in `/novel.realize`, which is the step that exists to fix it.

| Metric | Fail condition |
|---|---|
| Chapter length | Recorded, not a fail. Under 80% of the scene estimate invalidates the rows below and goes on the realize work-list. |
| Opening runway | Words before the POV character acts with intent (not perceiving, remembering, or being described). **Fail above 250.** Measured basis: published chapter openings average 105-121 words; the weakest unedited chapters ran 430-800. |
| Characterising appositive count | Above the style guide's budget of 1 per 10,000 words. |
| Inanimate volition count | Objects, places, or weather given intentions, beliefs, or opinions. Compare against the style guide's budget. |
| Self-explaining closers | Paragraphs that close by naming their own significance. **Any is a finding.** |
| POV integrity | Any flash-forward, non-POV interior, or second-person address. **Any is a fail.** |
| Repetition | Any distinctive phrase, image, or number over the style guide's budget. |
| Mid-band sentence share | Share of sentences 12-25 words long, from `bench/lint/fingerprint.py`. **Fail below 25%.** Measured basis: 6 published novels span 31-42%; 8 unedited drafts span 14-23%, with no overlap. A hollow middle — fragments alternating with long sentences — is the rhythm signature of an unedited draft. |
| Median sentence length | **Fail below 8 words.** Published: 9-13. Drafts: 5-7. |

**Scored** — 1-5, blind and comparative:

| Dimension | What to test |
|-----------|--------------|
| Voice | Does the prose have an idiom of its own — name the specific markers — or is it model-default prose? Reading like the other novels in `novels/` is not a fail on its own; reading like nothing in particular is. |
| Pressure | Is something being lost or decided in this scene, or is it a competence display? |
| Turn | Is the situation at the end different from the situation at the start? Name what changed. `no` is a fail. |
| Dialogue | With attributions removed, can the speakers be told apart? |
| Dramatic presence | Does the scene feel enacted rather than summarized? |
| Sensory / procedural authority | Are details embodied and, if reality-adjacent, credible? Is competence shown by sustained technical work, or asserted by the narrator? |
| Reader pull | Would a reader want the next page? |
| Predictability risk | Can the reader see the whole beat too early? |

## Decision Rules

- Any measured fail condition fails the chapter. These are counts, not judgments — there is nothing to argue about.
- Any critical scored dimension at `1` fails automatically.
- Any scored average below `3.5` fails.
- **In blind comparative scoring, a chapter that ranks last against its own siblings fails**, regardless of its absolute scores.
- Where two evaluation passes disagree, the worse verdict stands.
- When in doubt, branch before polishing.

## What these rubrics are not

The failure modes above are not artificial-intelligence artifacts. Thesis restatement, one scene shape repeated, an absent antagonist, and continuity contradictions were all measured at comparable or higher rates in an unedited self-published novel by a human author. These are the defects of unedited first drafts. The rubric is an editor, not a detector.
