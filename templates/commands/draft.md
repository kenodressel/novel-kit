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

Write prose for the manuscript, one scene at a time, following the scene specifications in `novels/<slug>/story/scenes.md`. The prose must honor the creative vision, character voices, and structural design established in the story artifacts.

## Prerequisites

Read ALL story artifacts before drafting:
- `novels/<slug>/story/vision.md` -- for voice, tone, style, and non-negotiables
- `novels/<slug>/story/characters/` -- for character voices and psychology
- `novels/<slug>/story/world.md` -- for sensory details and setting
- `novels/<slug>/story/outline.md` -- for structural context
- `novels/<slug>/story/scenes.md` -- for the specific scene being drafted
- `novels/<slug>/story/continuity.md` -- for established details (if it exists)
- Previous chapters in `novels/<slug>/manuscript/` -- for continuity and flow

## Process

1. **Identify the next scene**: Check the scene tracking table in `novels/<slug>/story/scenes.md` for the next scene with status "Planned."

2. **Review the scene spec**: Read the full scene specification. Understand the goal, conflict, outcome, emotional shift, and key beats.

3. **Draft the scene**: Write the prose. Follow these principles:
   - Honor the POV character's voice (from their character sheet)
   - Match the tone and style defined in the vision
   - Hit the key beats from the scene spec
   - Deliver the emotional shift
   - Land the specified outcome
   - Stay within the estimated word count (within 20%)
   - Show, don't tell (unless the vision explicitly calls for a telling style)
   - **Temporal discipline**: Only reference events that have already happened in previously drafted chapters. Do not let a character reflect on a scene that hasn't occurred yet. Check `continuity.md` if unsure.
   - **Earn the emotion**: Emotional beats should match the relationship's current stage. Don't borrow intimacy or vulnerability from later scenes — let each chapter's emotional register be justified by what's come before.

4. **Update continuity**: After drafting, update `novels/<slug>/story/continuity.md` with:
   - New facts established in prose (descriptions, names, places, objects)
   - Timeline: what happened on which day, in what order
   - Emotional milestones: key shifts in relationships (first real conversation, first vulnerability, first conflict, etc.) — note the chapter where each milestone *actually occurs* so later chapters don't reference them prematurely
   - Any motifs or recurring images introduced (note their origin chapter)

5. **Flag deviations**: If the scene naturally wants to go somewhere different from the spec, draft it as written AND note the deviation. The author decides whether to update the spec or revise the draft.

6. **Update status**: Mark the scene as "Drafted" in the tracking table in `novels/<slug>/story/scenes.md`.

7. **Update word count**: After each chapter is complete, update `current_word_count` in `novels/<slug>/novel.md` and recalculate progress percentage.

## Drafting modes

The author may request different levels of AI involvement:
- **Full draft**: Write the complete scene
- **Starter**: Write the opening paragraph, then stop for the author to continue
- **Dialogue draft**: Write only the dialogue, leaving action/description for the author
- **Beat expansion**: Take the key beats and expand each into a paragraph

## Output

- Write scene prose to the appropriate chapter file in `novels/<slug>/manuscript/`
- Update `novels/<slug>/story/continuity.md` with new details
- Update scene status in `novels/<slug>/story/scenes.md`
- When all scenes are drafted: update `novels/<slug>/novel.md` to mark Step 7 (Draft) as `✅ Complete` with today's date, set `current_step` to `8`, set `current_step_name` to `"Revise"`
