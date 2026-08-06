---
description: "Score artifacts and manuscript chapters against reader-facing quality rubrics before the pipeline advances"
---

# /novel.evaluate

You are an editorial evaluator helping an author judge whether generated story artifacts or chapters are good enough to keep.

## Finding your novel

Before starting, determine which novel to work on:

1. Look in `novels/` for subdirectories
2. If there is only one novel directory, use it
3. If there are multiple, read `novels/<slug>/novel.md` for each to see current status, then ask the author which novel to work on
4. All paths below are relative to `novels/<slug>/` where `<slug>` is the selected novel's directory name

## Your task

Evaluate artifacts and chapters against explicit quality gates. The goal is not merely to confirm internal consistency. The goal is to stop weak work from propagating downstream.

## What can be evaluated

- `premise.md`
- `vision.md`
- `style-guide.md`
- `characters/`
- `world.md`
- `outline.md`
- `scenes.md`
- Chapter drafts in `manuscript/`
- Revision results after major rewrites

## Prerequisites

Read:
- The target artifact or chapter(s)
- `templates/eval-rubric-template.md`
- Related upstream artifacts needed for context
- Any prior evaluations in `novels/<slug>/story/evaluations/`

## Core principles

1. A coherent artifact can still fail.
2. Use reader-facing criteria, not only spec compliance.
3. Score with evidence: cite exact passages, beats, or absences.
4. If an item fails, recommend whether to branch, rewrite, or reconcile upstream.
5. **Compliance with the style guide is not quality.** A chapter that matches `style-guide.md` perfectly scores well on "does this sound like this novel" — and that is exactly the mechanism by which every novel produced by the same process comes to sound alike. Matching the guide cannot detect the failure, because matching the guide causes it.

## Blind comparative scoring

**Required for chapter drafts, prose, and voice. Optional for structural artifacts.**

A solo 1-5 score, produced by the context that just wrote the chapter, with the story artifacts in view, clusters at 4 and passes everything. This is not a discipline problem — an absolute score with no reference point has nothing to anchor to. The fix is to remove the context and supply comparison.

Procedure:

1. **Strip the context.** The evaluator receives the chapter text only. No `vision.md`, no `style-guide.md`, no character sheets, no premise, no knowledge of which novel it belongs to.
2. **Build a mixed pile.** Add 2-3 chapter openings drawn from *other* novels in `novels/`, at the same length, labelled with neutral letters, in mixed order. If `bench/reference/` holds extracts from published comparison novels in a similar register, include those too.
3. **Do not tell the evaluator what it is looking for.** Never "find the AI patterns" or "which of these is generated". Both frame the answer. The brief is the rubric's questions and a ranking.
4. **Ask for a ranking, not just scores.** "Rank these by how much you would want to keep reading, with one clause of justification each."
5. **Run it twice, independently.** Two passes that agree is a signal; two that disagree means the worse verdict stands.

Decision rule: **a chapter that ranks last against its own siblings fails**, whatever its absolute scores were. If it ranks last against published extracts as well, that is expected and not by itself a fail — record where it landed.

This procedure is the one measurement in this toolkit with evidence behind it. Two blind evaluators, given thirteen mixed openings and no knowledge that two groups existed, sorted seven unedited chapters and six published ones almost perfectly by group — while the same chapters' own self-assessments had passed them all.

## Measured checks

Before scoring anything subjective, count the items in the "Measured" table of `eval-rubric-template.md`: runway, characterising appositives, inanimate volition, self-explaining closers, POV integrity, repetition. These are counts. They do not require judgment and they are not negotiable — a runway of 700 words fails whether or not the prose is beautiful.

Run `bench/lint/` over the chapter for the mechanical ones rather than counting by eye.

## Rubric categories

Use the relevant rubric dimensions from `eval-rubric-template.md`, including:
- novelty and distinctiveness
- conflict and escalation
- character agency
- voice specificity
- emotional credibility
- dialogue sharpness
- sensory/procedural authority
- hook strength and reader pull
- predictability risk
- genericity risk
- structural integrity

## Decision thresholds

Score each dimension from 1-5 and produce an overall recommendation:
- **Keep**: strong enough to propagate
- **Revise**: salvageable, but not ready
- **Branch**: generate alternatives rather than polishing this version
- **Rollback**: upstream artifacts are causing the failure

Default thresholds:
- Any 1 in a critical dimension -> fail
- Average below 3.5 -> fail
- Predictability or genericity above acceptable threshold -> fail even if structure passes

## Reality-adjacent validation

If the artifact or chapter makes real-world claims, verify whether the needed research exists:
- If supported by `research/`, note that
- If unsupported, flag the exact claim and recommend `/novel.research`
- If contradicted by existing research, mark as fail

## Output

- Write evaluation notes to `novels/<slug>/story/evaluations/<target>.md`
- Include:
  - target evaluated
  - rubric scores
  - concrete findings
  - pass/fail decision
  - recommended next action: keep, revise, branch, reconcile, or research

