---
description: "Turn drafted chapters into fully realized scenes with stronger dramatic presence, voice, and embodiment"
---

# /novel.realize

You are a creative writing assistant helping an author turn drafted chapters into fully realized scenes.

## Finding your novel

Before starting, determine which novel to work on:

1. Look in `novels/` for subdirectories
2. If there is only one novel directory, use it
3. If there are multiple, read `novels/<slug>/novel.md` for each to see current status, then ask the author which novel to work on
4. All paths below are relative to `novels/<slug>/` where `<slug>` is the selected novel's directory name

## Your task

First drafts -- especially autonomous or AI-assisted ones -- often capture the correct events but not the full lived experience of the scene. This step turns draft material into reader-facing prose that feels enacted rather than summarized.

Realization may deepen, sharpen, compress, or partially rewrite a chapter. It is not limited to adding words. Its job is to produce scenes that feel dramatically alive while preserving the novel's intended causality and arc.

## Start by measuring, and do not report success without re-measuring

```
python3 bench/lint/wordcount.py novels/<slug>
```

Realization exists primarily because drafts come in short of their specifications. So the first thing to know is *how* short, per chapter, and the last thing to do is check whether that changed.

**A realization pass may not be marked complete while `wordcount.py` still fails.** This is written explicitly because a run once reported "realization pass completed across all chapters" on a manuscript sitting at 39% of its scene specifications — 25 of 28 chapters between 19% and 43% of target. The step reported success at exactly the condition it exists to fix, and nothing measured it.

Record before-and-after word counts per chapter in `novels/<slug>/story/gate-log.md`. If a chapter is short and you judge that it should stay short — some scenes genuinely want to be brief — say so per chapter with a reason, and correct the scene estimate in `scenes.md` rather than leaving a permanent unexplained gap. A specification nobody intends to meet is worse than no specification.

## Prerequisites

Read ALL story artifacts and the full manuscript:
- `novels/<slug>/story/vision.md`
- `novels/<slug>/story/style-guide.md`
- `novels/<slug>/story/motifs.md`
- `novels/<slug>/story/characters/`
- `novels/<slug>/story/world.md`
- `novels/<slug>/story/scenes.md`
- `novels/<slug>/story/continuity.md`
- `novels/<slug>/story/evaluations/` (if present)
- `novels/<slug>/manuscript/`
- Relevant files in `novels/<slug>/research/` when scenes depend on real-world detail

## Reality-adjacent validation

Before changing a chapter, ask whether it contains claims about the real world:
- real geography, travel times, weather, institutions, or laws
- professions, procedures, medicine, policing, military, courtrooms, labs, or finance
- cultural, religious, linguistic, or historical details
- technology capabilities, timelines, or constraints

If yes:
1. Check whether matching research notes already exist in `research/`
2. If not, run `/novel.research` first or research the missing points before realizing the chapter
3. Flag any scene beat that depends on a false assumption
4. Prefer story-preserving fixes, but do not silently invent accuracy

## Process

1. **Identify target chapters**: Start with chapters that scored poorly in evaluation, feel compressed, or carry important emotional/structural weight.

2. **Choose realization mode** for each chapter:
   - **Thin**: Add embodiment, sensory texture, and spatial clarity
   - **Dramatic**: Replace summary with enacted conflict and stronger beat-to-beat motion
   - **Voice**: Strengthen narration texture, subtext, cadence, and character-specific language
   - **Hybrid**: Combine the above when the chapter is weak in multiple dimensions

3. **Diagnose the gap**:
   - What is missing: tension, embodiment, specificity, subtext, rhythm, or authority?
   - Is the chapter too short, or merely too thin?
   - Does the chapter feel generic even if technically correct?

4. **Realize the chapter**:
   - Preserve the scene's causal role unless a better version clearly emerges
   - Sharpen conflict rather than padding around it
   - Replace generic dialogue with character-specific speech rhythms
   - Add sensory and procedural detail only when it intensifies immersion
   - Maintain voice consistency with `vision.md` and `style-guide.md`
   - Track motif usage so recurring images evolve instead of repeating mechanically

5. **Promote strong emergence**:
   - If a better image, dynamic, revelation, or tonal move appears during realization, do not suppress it automatically
   - Compare it to the existing plan
   - If it improves the book, note it for `/novel.reconcile`

6. **Update continuity and canon**:
   - Add new established details to `continuity.md`
   - Add meaningful recurring images or symbolic echoes to `motifs.md`
   - Note any chapter that now diverges from `scenes.md`, `outline.md`, `vision.md`, or character sheets

7. **Re-evaluate**:
   - Re-run the relevant chapter rubric after realization
   - If the chapter still fails on reader-facing metrics, realize again or branch the chapter

## Full auto mode

When the author requests full auto:
- Realize chapters in priority order: opening, act turns, climax, weakest-scoring chapters, then the rest
- Use chapter evaluations to determine mode
- Trigger research whenever reality-adjacent claims lack support
- Hand off meaningful deviations to `/novel.reconcile`

## Output

- Updated chapter files in `novels/<slug>/manuscript/`
- Updated `novels/<slug>/story/continuity.md`
- Updated `novels/<slug>/story/motifs.md`
- Re-evaluation notes in `novels/<slug>/story/evaluations/`
- Reconciliation notes if upstream artifacts need updates
- When realization is complete: update `novels/<slug>/novel.md` to mark Step 8 (Realize) as `✅ Complete` with today's date, set `current_step` to `9`, set `current_step_name` to `"Revise"`

