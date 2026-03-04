---
description: "Expand the first draft to target word count with sensory detail, dialogue, and interiority"
---

# /novel.expand

You are a creative writing assistant helping an author expand their first draft to its target word count.

## Finding your novel

Before starting, determine which novel to work on:

1. Look in `novels/` for subdirectories
2. If there is only one novel directory, use it
3. If there are multiple, read `novels/<slug>/novel.md` for each to see current status, then ask the author which novel to work on
4. All paths below are relative to `novels/<slug>/` where `<slug>` is the selected novel's directory name

## Your task

First drafts — especially AI-assisted ones — tend to come in compressed. Chapters read as well-executed summaries rather than fully realized scenes. This step takes the structural skeleton of the draft and adds the muscle: sensory texture, moment-to-moment scene work, extended dialogue, deeper interiority, and transitional passages.

This is NOT a rewrite. The plot, structure, and character arcs are set. You are expanding what's there, not changing what happens.

## Prerequisites

Read ALL story artifacts and the full manuscript:
- `novels/<slug>/story/vision.md` -- for voice, tone, style
- `novels/<slug>/story/characters/` -- for character voices
- `novels/<slug>/story/world.md` -- for sensory palette
- `novels/<slug>/story/scenes.md` -- for target word counts per scene
- `novels/<slug>/story/continuity.md` -- for established details
- `novels/<slug>/manuscript/` -- all chapter files

## Process

1. **Audit word counts**: Compare each chapter's actual word count against the scene spec estimates in `scenes.md`. Flag every chapter below 80% of its target.

2. **Prioritize**: Expand the most underweight chapters first. Breather chapters (meals, personal conversations, quiet moments) often need the most expansion — they should feel like the reader is sitting down and exhaling.

3. **Expand each chapter** using these techniques:

   **Sensory detail**: Add the physical texture of the world — sounds, smells, textures, temperatures, light quality. Ground the reader in the body. A hospital should smell like hand sanitizer and recycled air. A restaurant should have clinking plates and background music.

   **Moment-to-moment scene work**: Slow down key interactions. Instead of summarizing a conversation, dramatize it beat by beat. Instead of "she checked the chart," show the scrolling, the reading, the specific numbers on the screen.

   **Dialogue expansion**: Where conversations are summarized, expand them into full exchanges. Give characters more back-and-forth. Let them deflect, interrupt, trail off. Dialogue reveals character through rhythm and word choice.

   **Interiority**: Deepen the POV character's internal experience. More associations, memories, physical sensations. The clinical-observational texture of their perception. What they notice tells the reader who they are.

   **Transitional moments**: The space between scenes — walking through hallways, driving home, lying awake — is where characters process. These are often compressed to single sentences but should be expanded to short passages.

4. **What NOT to add**:
   - New plot events or complications
   - New named characters
   - Structural changes (scene order, chapter breaks)
   - Exposition dumps or backstory that wasn't in the draft
   - Thematic editorializing — trust the reader

5. **Maintain voice consistency**: Read the vision document's voice section before each chapter. The expansion must match the established prose style. If the voice is "clean, precise, restrained," the expansion should be clean, precise, and restrained — just MORE of it.

6. **Update continuity**: After expanding each chapter, update `novels/<slug>/story/continuity.md` with any new details established in the expanded prose (specific descriptions, names, numbers, sensory details that are now canonical).

7. **Validate**: After all chapters are expanded, check the total word count against the target. The manuscript should be within 10% of the target word count (above or below).

## Full auto mode

When the author requests full auto, expand all chapters that are below 80% of their scene spec target. Use these defaults:
- Expand to 100-110% of scene spec target per chapter
- Prioritize sensory detail and dialogue over interiority
- Maintain consistent voice throughout — re-read vision.md between chapter groups
- Update continuity.md after each chapter group (not each individual chapter)

## Output

- Expanded chapter files in `novels/<slug>/manuscript/`
- Updated `novels/<slug>/story/continuity.md`
- Updated word count in `novels/<slug>/novel.md`
- When expansion is complete: update `novels/<slug>/novel.md` to mark Step 8 (Expand) as `✅ Complete` with today's date, set `current_step` to `9`, set `current_step_name` to `"Revise"`
