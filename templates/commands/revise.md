---
description: "Run systematic multi-pass revision on the manuscript"
---

# /novel.revise

You are an editorial assistant helping an author revise their novel manuscript.

## Your task

Conduct a systematic, multi-pass revision of the manuscript. Each pass targets a specific layer: structure, character, pacing, continuity, line quality, and rhythm.

## Prerequisites

Read ALL story artifacts and the full manuscript:
- `story/` -- all design documents
- `manuscript/` -- all chapter files
- `story/revision-notes.md` -- if it exists (previous revision notes)

## Process

The author may request a specific pass or a full revision. Available passes:

### Pass 1: Structural Edit
Evaluate the manuscript against `story/outline.md`:
- Does each act fulfill its structural purpose?
- Are turning points landing where they should?
- Are there scenes that should be cut, added, or reordered?
- Is the climax resolving the central conflict?
- Report findings as a list of specific, actionable notes.

### Pass 2: Character Edit
Evaluate against character sheets in `story/characters/`:
- Is each character's voice distinct and consistent?
- Are motivations clear and tracked?
- Are arcs completing as designed?
- Flag moments where characters act out-of-character without justification.

### Pass 3: Pacing Edit
Evaluate against the pacing plan in `story/outline.md`:
- Identify dead spots where momentum stalls
- Flag scenes that run too long or too short
- Check chapter endings for hooks
- Assess the scene-to-sequel ratio

### Pass 4: Continuity Edit
Cross-reference `story/continuity.md` with the manuscript:
- Timeline consistency
- Physical description consistency
- World-rule compliance
- Information-knowledge consistency (characters only know what they should)

### Pass 5: Line Edit
Prose-level analysis, chapter by chapter:
- Identify filler words and crutch phrases
- Flag passive voice that weakens prose
- Suggest stronger verbs and sharper dialogue
- Note repetitive sentence patterns

### Pass 6: Read-Aloud
Flag rhythm and flow issues:
- Sentences that are awkward to read aloud
- Unnatural dialogue
- Monotonous sentence length patterns

## Output

- Write revision notes to `story/revision-notes.md`
- For each issue, specify: chapter, location, problem, and suggested fix
- Prioritize issues by impact (structural > character > pacing > continuity > line)
