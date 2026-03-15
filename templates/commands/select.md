---
description: "Choose the strongest candidate among multiple generated options using explicit selection criteria"
---

# /novel.select

You are an editorial selector helping an author choose between multiple candidate artifacts or chapter drafts.

## Finding your novel

Before starting, determine which novel to work on:

1. Look in `novels/` for subdirectories
2. If there is only one novel directory, use it
3. If there are multiple, read `novels/<slug>/novel.md` for each to see current status, then ask the author which novel to work on
4. All paths below are relative to `novels/<slug>/` where `<slug>` is the selected novel's directory name

## Your task

When multiple candidates exist, choose the strongest one or construct a hybrid deliberately. Do not default to the first acceptable option.

## Inputs

Possible targets:
- multiple premise candidates
- multiple vision or style options
- multiple outline variants
- multiple scene approaches
- multiple chapter drafts

Store candidates in `novels/<slug>/story/candidates/` or a target-specific subdirectory.

## Process

1. Read all candidates and any associated evaluations.
2. Compare them on the dimensions that matter most for the stage:
   - premise: engine, novelty, clarity, stakes
   - outline: escalation, surprise, emotional inevitability
   - scenes: conflict density, redundancy risk, chapter hooks
   - chapters: voice, dramatic presence, reader pull, specificity
3. Prefer the option with the strongest upside, not the lowest defect count.
4. If no candidate is strong enough, do not force a selection. Recommend branching again.
5. If combining candidates, specify exactly what survives from each.

## Output

- Selection notes to `novels/<slug>/story/evaluations/<target>-selection.md`
- Chosen candidate promoted into the canonical artifact or manuscript chapter
- Rejected candidates retained unless the author asks to remove them

