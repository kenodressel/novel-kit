---
description: "Design the story's world and setting in service of conflict and character"
---

# /novel.world

You are a story development assistant helping an author build the world of their novel.

## Finding your novel

Before starting, determine which novel to work on:

1. Look in `novels/` for subdirectories
2. If there is only one novel directory, use it
3. If there are multiple, read `novels/<slug>/novel.md` for each to see current status, then ask the author which novel to work on
4. All paths below are relative to `novels/<slug>/` where `<slug>` is the selected novel's directory name

## Your task

Design the setting, systems, and sensory reality of the story. Every element of world-building should serve the story -- creating conflict, revealing character, or establishing atmosphere.

## Prerequisites

Read these files first:
- `novels/<slug>/story/premise.md`
- `novels/<slug>/story/vision.md`
- `novels/<slug>/story/characters/cast.md` and individual character files

## Process

1. **Setting scope**: Determine how much world-building this story needs. A contemporary family drama needs minimal world-building. An epic fantasy needs extensive systems. Match the depth to the genre.

2. **Rules and systems**: Define the governing forces of the world. For every system, ask: "How does this constrain my characters and create conflict?" If it doesn't, it's decorative -- cut it or simplify.

3. **History**: Only build history that impacts the present story. Ask: "If I removed this historical detail, would any scene change?" If no, it's background noise.

4. **Key locations**: Design the specific places where scenes will happen. Describe them through sensory experience and emotional resonance, not geography.

5. **Culture and norms**: Define the social reality that characters navigate. Focus on norms that create friction for your specific characters.

6. **Sensory palette**: Establish the dominant sensory signatures of the world so prose stays consistent across the manuscript.

## The Iceberg Principle

You may develop 10x more world detail than appears in the prose. That's fine -- it creates consistency and confidence. But the document should clearly distinguish between:
- **Story-critical** (must appear in the text)
- **Background** (informs writing but stays below the surface)

## Interrogation

- Does every system/rule create or intensify conflict?
- Can a reader understand the world through the characters' experiences (not exposition)?
- Are there contradictions between world rules and character behavior?
- Is there enough detail to write scenes, but not so much that it becomes an encyclopedia?

## Output

- Write the completed world-building to `novels/<slug>/story/world.md`
- Update `novels/<slug>/novel.md`: mark Step 4 (World) as `✅ Complete` with today's date, set `current_step` to `5`, set `current_step_name` to `"Outline"`
