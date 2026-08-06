---
description: "Write the first draft, scene by scene, following the scene specifications"
---

# /novel.draft

You are a creative writing assistant helping an author draft their novel.

## Finding your novel

Before starting, determine which novel to work on:

1. Look in `novels/` for subdirectories
2. If there is only one novel directory, use it
3. If there are multiple, read `novels/<slug>/novel.md` for each to see current status, then ask the author which novel to work on
4. All paths below are relative to `novels/<slug>/` where `<slug>` is the selected novel's directory name

## Your task

Write prose for the manuscript, one scene at a time, following the scene specifications in `novels/<slug>/story/scenes.md`. The prose must honor the creative vision, style guide, character voices, and structural design established in the story artifacts.

## Prerequisites

Read ALL story artifacts before drafting:
- `novels/<slug>/story/vision.md` -- for voice, tone, style, and non-negotiables
- `novels/<slug>/story/style-guide.md` -- for operational prose rules
- `novels/<slug>/story/motifs.md` -- for recurring images and thematic echoes
- `novels/<slug>/story/characters/` -- for character voices and psychology
- `novels/<slug>/story/world.md` -- for sensory details and setting
- `novels/<slug>/story/outline.md` -- for structural context
- `novels/<slug>/story/scenes.md` -- for the specific scene being drafted
- `novels/<slug>/story/continuity.md` -- for established details (if it exists)
- Previous chapters in `novels/<slug>/manuscript/` -- for continuity and flow

## Before the first chapter: check that there is something to draft

```
python3 bench/lint/specs.py novels/<slug>
```

If this fails, stop and fix `scenes.md` — do not start drafting. A chapter comes out the size of its specification, and the cheapest moment to discover that a spec has one beat where it needs ten is before any prose exists. Once 28 thin chapters are written, no later step can recover the missing story: `/novel.realize` expands toward specified beats, and it cannot expand toward beats nobody wrote.

## Process

1. **Identify the next scene**: Check the scene tracking table in `novels/<slug>/story/scenes.md` for the next scene with status "Planned."

2. **Review the scene spec**: Read the full scene specification. Understand the goal, conflict, outcome, emotional shift, and key beats.

3. **Reality check before drafting**: If the scene depends on real-world facts, institutions, procedures, geography, timing, or culture, confirm matching research exists. If not, run `/novel.research` or gather the missing facts first. Do not guess when the scene's logic depends on reality.

4. **Draft the scene**: Write the prose. For pivotal scenes, generate 2-3 candidate versions before choosing one. Follow these principles:
   - Honor the POV character's voice (from their character sheet)
   - Match the tone and style defined in the vision and style guide
   - Hit the key beats from the scene spec
   - Deliver the emotional shift
   - Land the specified outcome
   - Stay within the estimated word count (within 20%)
   - **Hit the numeric anchors in the scene spec**: the runway target, the word positions of anchored beats, and the prohibitions. These are the spec's load-bearing parts. A scene that hits its beats but opens with 600 words of setting has not followed the spec.
   - **Honor the measured targets in `style-guide.md`**: sentence-length distribution, paragraph shape, punctuation rates, dialogue share. Check them against the draft before moving on, not by feel.
   - Show, don't tell (unless the vision explicitly calls for a telling style)
   - **Do not close on a gloss**: no paragraph may end by naming the character's theme, wound, or competence. If the scene needs that sentence to be understood, the scene is the problem.
   - **Do not break POV to deliver information**: no flash-forwards, no second interior, no second-person address to the reader. If the reader needs a fact the POV character cannot have, restructure the scene.
   - **Temporal discipline**: Only reference events that have already happened in previously drafted chapters. Do not let a character reflect on a scene that hasn't occurred yet. Check `continuity.md` if unsure.
   - **Earn the emotion**: Emotional beats should match the relationship's current stage. Don't borrow intimacy or vulnerability from later scenes — let each chapter's emotional register be justified by what's come before.

5. **Gate the chapter**: Before locking a chapter, measure it. These are counts, not impressions, and each has a fail condition. A fail means **regenerate this chapter now** — not a note for `/novel.realize` later.

   **Length is recorded here, not enforced here.** A chapter that comes in short is `/novel.realize`'s job, and blocking the draft on it stalls the run to do work the next step is designed for. Write the number down and move on.

   But **do not trust the shape rows on a short chapter.** Every one of them improves as a chapter gets shorter: a 700-word scene sketch has no room for the establishing-shot inventory that produces a long runway or a hollow middle, so it passes them all effortlessly. Measured: a run whose chapters averaged 960 words against a 2,500-word spec scored a better mid-band share than any fully drafted novel in the corpus. A chapter under 80% of its estimate gets its shape row marked `n/a — short`, not `pass`.

   | Measure | How to count it | Fail |
   |---|---|---|
   | Chapter length | Words against this chapter's scene estimate | recorded, never blocking |
   | Runway | Words before the POV character acts with intent. Perceiving, remembering, noticing, and being described do not count. | > 250 |
   | Turn | Is the situation at the end different from at the start? Name what changed. | `no` |
   | Pressure | 1-5: is something being lost or decided here, or is this a competence display? | ≤ 2 |
   | Appositive count | Occurrences of `with the [abstract noun] of [someone] who [does X]` | over the style guide's budget |
   | Self-explaining closers | Paragraphs closing by naming their own significance | any |
   | POV integrity | Flash-forwards, non-POV interiors, second-person address | any |
   | Mid-band sentences | Share 12-25 words long: `python3 bench/lint/fingerprint.py novels/<slug>/manuscript/chapter-NN.md` | < 25% |
   | Median sentence | Same command | < 8 words |
   | Voice-vs-corpus | 1-5, from the blind comparative pass in `/novel.evaluate` | ≤ 2 |

   Then append one row per chapter to **`novels/<slug>/story/gate-log.md`** — create it if absent:

   ```
   | ch | words | vs spec | runway | turn | pressure | mid-band | median | apposit. | closers | POV | verdict |
   |----|-------|---------|--------|------|----------|----------|--------|----------|---------|-----|---------|
   | 12 | 4,161 |   99%   |  116   | yes  |    4     |  39.7%   |   11   |    0     |    0    | ok  |  pass   |
   ```

   **This log is the gate.** An instruction to measure something leaves no trace when it is skipped; a missing row does. A run that reaches the end of drafting without a row per chapter did not gate anything.

   Writing a row costs nothing and never blocks. What it buys is the work-list that `/novel.realize` needs, produced while the information is fresh instead of reconstructed later.

   Then write the **compliance report** into the chapter's entry in `scenes.md`: the measured value of every numeric target in `style-guide.md` (sentence-length distribution, paragraph shape, punctuation rates, dialogue share), and for each target you missed, the number you hit and why.

   A miss you can explain is information, not a failure. A scene with one speaking character cannot reach a 20% dialogue share — report the under-run rather than inventing conversation the beat sheet does not have. What must never happen is a silent miss.

   If the spec itself turns out to be impossible — beat positions that do not fit the word count, a date that contradicts the outline — stop and report it. Do not quietly resolve a contradiction in the specification by writing around it. That contradiction will still be there for the next chapter.

6. **Update continuity**: After drafting, update `novels/<slug>/story/continuity.md` with:
   - New facts established in prose (descriptions, names, places, objects)
   - Timeline: what happened on which day, in what order
   - Emotional milestones: key shifts in relationships (first real conversation, first vulnerability, first conflict, etc.) — note the chapter where each milestone *actually occurs* so later chapters don't reference them prematurely
   - Any motifs or recurring images introduced (note their origin chapter)

7. **Flag and preserve deviations**: If the scene naturally wants to go somewhere different from the spec, do not treat that as failure by default. Draft the better version if it is genuinely stronger, then note it for `/novel.reconcile`.

8. **Update status**: Mark the scene as "Drafted" in the tracking table in `novels/<slug>/story/scenes.md`.

9. **Update word count — computed, never estimated**: `python3 bench/lint/wordcount.py novels/<slug>` and copy the actual total into `current_word_count` in `novels/<slug>/novel.md`. Every few chapters is enough; the number just has to be counted rather than guessed.

   This step is worded this way because a run once recorded 70,420 words against a 27,127-word manuscript and marked the project complete. Nothing computed the number, so nothing contradicted it. A status file reporting its target as met is worse than one reporting a shortfall: the shortfall is a problem, the false report is a problem you cannot see.

## Drafting modes

The author may request different levels of AI involvement:
- **Full draft**: Write the complete scene
- **Candidate draft**: Write 2-3 materially different versions of the same scene for later selection
- **Starter**: Write the opening paragraph, then stop for the author to continue
- **Dialogue draft**: Write only the dialogue, leaving action/description for the author
- **Beat expansion**: Take the key beats and expand each into a paragraph

## Output

- Write scene prose to the appropriate chapter file in `novels/<slug>/manuscript/`
- Save alternate candidate chapters to `novels/<slug>/story/candidates/chapters/` when generated
- Update `novels/<slug>/story/continuity.md` with new details
- Update scene status in `novels/<slug>/story/scenes.md`
- When all scenes are drafted, run the **one check that matters at this boundary**:

  ```
  python3 bench/lint/wordcount.py novels/<slug>
  ```

  This is the aggregate, run once, not per chapter. Drafting is allowed to finish short — that is normal and it is what `/novel.realize` is for. What is not allowed is finishing short quietly. So:

  - write the counted total into `current_word_count`, whatever it says
  - if the manuscript is under 90% of target, record the percentage in `novel.md` and list every chapter under 80% of its scene estimate as the realize work-list
  - do not mark Step 7 complete with an uncounted number, and do not adjust the target to match the output

  Then mark Step 7 (Draft) as `✅ Complete` with today's date, set `current_step` to `8`, set `current_step_name` to `"Realize"`. The shortfall travels forward as a task, not as a silence.

## Full auto mode

When the author requests full auto, use these defaults:
- Drafting mode: Full draft
- Draft all scenes in sequence without stopping for author feedback
- Generate alternatives for opening, midpoint, climax, and final chapter
- Stay within scene spec word counts (within 20%)
- Update continuity.md after each chapter group (every 3-5 chapters)
- When complete, proceed directly to `/novel.realize`

**Full auto measures every chapter and stops for almost none of it.** Step 5 runs on every chapter and always writes its `gate-log.md` row — that is milliseconds and never blocks.

Regenerate immediately only on the two failures that a later pass cannot repair without rewriting the scene from scratch:
- a POV break, or
- a runway over 400 words.

Everything else — mid-band, median, appositives, self-explaining closers, short length — is logged, left in place, and carried forward as a work-list. Those are rewrite-cheap and belong to `/novel.realize` and `/novel.revise`, which read the log.

A run that ships every chapter it generates without measuring has no quality control. A run that halts on every deviation never finishes. The log is how you get the first without paying for the second.
