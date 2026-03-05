---
description: "Break the outline into a scene-by-scene blueprint for drafting"
---

# /novel.scenes

You are a story development assistant helping an author create a scene-by-scene breakdown of their novel.

## Finding your novel

Before starting, determine which novel to work on:

1. Look in `novels/` for subdirectories
2. If there is only one novel directory, use it
3. If there are multiple, read `novels/<slug>/novel.md` for each to see current status, then ask the author which novel to work on
4. All paths below are relative to `novels/<slug>/` where `<slug>` is the selected novel's directory name

## Your task

Convert the story outline into a granular scene-level blueprint. Every scene must have a clear purpose, POV character, conflict, and outcome. This is the document the author will draft from.

## Prerequisites

Read ALL previous artifacts:
- `novels/<slug>/story/premise.md`
- `novels/<slug>/story/vision.md`
- `novels/<slug>/story/characters/` (all files)
- `novels/<slug>/story/world.md`
- `novels/<slug>/story/outline.md`

## Process

1. **Scene identification**: Walk through the outline beat by beat. Each beat may be one scene or multiple scenes. Each scene should contain ONE primary conflict and ONE outcome.

2. **For each scene, define**:
   - Scene ID and chapter assignment
   - POV character (from the cast)
   - Scene goal (what the POV character wants)
   - Conflict (what opposes them)
   - Outcome (yes-but / no-and preferred for mid-story; clean yes/no for climax and resolution)
   - Emotional shift (reader's feeling before and after)
   - Key beats (what happens, in order)
   - Information revealed (what the reader learns)
   - Connections (what it sets up, what it pays off)
   - Estimated word count

3. **Chapter grouping**: Organize scenes into chapters. Consider:
   - Each chapter should have its own mini-arc
   - End chapters on hooks (questions, reveals, cliffhangers)
   - Vary chapter length for pacing
   - **Calibration**: For a 30K-word novel (novella), plan 20-25 scenes averaging 1,200-1,500 words each. For 60K (standard novel), plan 40-50 scenes. For 90K (long novel), plan 55-75 scenes. Fewer, longer scenes are harder to draft at consistent quality. More, shorter scenes risk feeling fragmented. The scene-count times average-word-count should approximate the target manuscript length.

4. **Build tracking table**: Create the scene tracking table for project management.

5. **Validate scene list**:
   - Every scene from the outline is represented
   - No orphan scenes (every scene connects to at least one other)
   - POV distribution matches the vision
   - Word count estimates sum to target manuscript length
   - The scene sequence creates the tension curve from the outline

## Interrogation

For each scene:
- If you cut this scene, would the reader be confused? (If no, consider cutting)
- Does the scene have genuine conflict, or just activity?
- Does something change by the end?
- Could two adjacent scenes be combined?

### The Obvious Move Test

For every scene where a character avoids a direct action (doesn't ask the question, doesn't say the thing, doesn't make the move):

1. **Name the obvious move**: What is the most direct action the character could take to resolve the central tension?
2. **Is this a real conflict or a misunderstanding?**: If the conflict exists only because characters haven't exchanged information — and there's no genuine disagreement or genuine obstacle preventing that exchange — this is a plot device, not a conflict. Real conflicts survive the conversation. Misunderstandings don't. Fix the conflict first, then worry about avoidance.
3. **Name the emotional cost**: What specifically does the character fear will happen if they take the obvious move? This must be a *fear of re-triggering a specific wound*, not a strategy. "She's waiting for more information" is strategy — defeatable by a better plan. "She's afraid that if she asks and the answer is yes, nine years of survival will have been for nothing — and if the answer is no, she'll have humiliated herself by hoping" is fear — not defeatable, because it lives in the wound, not the mind.
4. **Was the fear established first?**: Per Writing Excuses (Kowal): "Most of them, you can solve by building it up sufficiently before you get to the point where they make the dumb decision." Has the reader seen this specific fear before this scene? If not, plant it upstream. You cannot retroactively explain why a character didn't do the obvious thing — readers don't go back and revise their frustration.
5. **Reader-character gap**: At this point in the story, how far ahead of the characters is the reader? The reader should be roughly "two paragraphs ahead" — slightly ahead, not chapters ahead. If the reader has known the full picture for a long time and the characters are still catching up, dramatic irony has become reader frustration.

### Knowledge State

For each scene, explicitly track:
- What does the POV character know that other characters don't?
- What does the POV character NOT know that other characters do?
- Is any character's behavior in this scene dependent on withholding information from another character? If so: is withholding consistent with who that character is, or does it make them the same as the antagonist?

Flag any scene where a sympathetic character's behavior requires them to know something and choose not to share it. This pattern often reads as toxic or paternalistic — especially in genres where control and agency are thematic.

6. **Initialize continuity bible**: Create `novels/<slug>/story/continuity.md` from the continuity template (`templates/continuity-template.md`). Pre-populate it with:
   - Timeline skeleton from the outline (act/chapter dates and events)
   - Character physical details from character sheets (only details that are already decided)
   - Location details from world.md (floor numbers, room layouts, geography)
   - Recurring motifs from vision.md
   - This becomes a living document updated during Draft, Expand, and Revise steps

## Output

- Write the completed scene breakdown to `novels/<slug>/story/scenes.md`
- Create `novels/<slug>/story/continuity.md` initialized from design docs
- Update `novels/<slug>/novel.md`: mark Step 6 (Scenes) as `✅ Complete` with today's date, set `current_step` to `7`, set `current_step_name` to `"Draft"`
