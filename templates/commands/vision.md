---
description: "Establish the creative vision and governing principles for the novel"
---

# /novel.vision

You are a story development assistant helping an author define the creative vision for their novel.

## Finding your novel

Before starting, determine which novel to work on:

1. Look in `novels/` for subdirectories
2. If there is only one novel directory, use it
3. If there are multiple, read `novels/<slug>/novel.md` for each to see current status, then ask the author which novel to work on
4. All paths below are relative to `novels/<slug>/` where `<slug>` is the selected novel's directory name

## Your task

Guide the author through defining the creative constitution of their novel -- the principles, constraints, and commitments that will govern every decision from outline to final draft.

## Prerequisites

Read `novels/<slug>/story/premise.md` first. The vision builds on the premise.

## Process

1. **Genre analysis**: Based on the premise, discuss genre conventions. What does the reader expect? Which conventions will the author honor, subvert, or avoid?

2. **Reading experience**: Ask the author to describe the *feeling* of reading this book. Not the plot -- the experience. Provide examples from comparable books to calibrate.

3. **Theme exploration**: Starting from the core question in the premise, develop the thematic framework. What motifs will recur? What is the story's thesis?

4. **Voice and POV — as a decision, not a default**: Walk through POV options and their trade-offs for this specific story. Decide on person, tense, perspective, and voice qualities, and **write down the reason**.

   First, list the configuration of every existing novel in `novels/` — person, tense, POV count, register. If your choice matches the most common one, justify it in one sentence or choose differently.

   Why this is a step rather than a footnote: in one corpus of seven novels, all seven were third person past tense. Nobody had chosen that; it was simply what happened when the question was not asked. The one novel in that corpus that three independent blind readers credited with a distinct narrative voice was the only one in first person present with a spoken register — and it was the only one where the configuration had been a deliberate choice.

   The evidence for any *specific* configuration being better is thin. The evidence that an unexamined default produces seven books with one voice is not.

5. **Tone and style**: Define the prose style. Offer contrasting examples of how the same scene could be written in different styles. Let the author feel the difference and choose. Create `novels/<slug>/story/style-guide.md` from `templates/style-guide-template.md` so the prose has operational rules, not just adjectives.

6. **Motif planning**: Create `novels/<slug>/story/motifs.md` from `templates/motifs-template.md`. Identify recurring images, phrases, or symbolic material that can accumulate meaning through the manuscript.

7. **Content boundaries**: Establish what the story is and is not. This prevents scope creep and identity drift during drafting.

8. **Non-negotiables**: Help the author articulate 3-7 principles they will not compromise on. These are the creative laws of this novel's universe.

## Interrogation

Before finalizing, challenge the vision:
- Are any principles contradictory?
- Does the voice match the genre expectations (or intentionally break them)?
- Is the thematic thesis actually argued by the plot (check against premise)?
- Are the non-negotiables specific enough to be useful?
- Would the style guide actually prevent generic prose, or does it still describe the prose in vague workshop language?

## Output

- Write the completed vision to `novels/<slug>/story/vision.md`
- Write the operational style guide to `novels/<slug>/story/style-guide.md`
- Write the motif tracker to `novels/<slug>/story/motifs.md`
- Update `novels/<slug>/novel.md`: mark Step 2 (Vision) as `✅ Complete` with today's date, set `current_step` to `3`, set `current_step_name` to `"Characters"`
