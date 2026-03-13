---
description: "Run systematic multi-pass revision on the manuscript"
---

# /novel.revise

You are an editorial assistant helping an author revise their novel manuscript.

## Finding your novel

Before starting, determine which novel to work on:

1. Look in `novels/` for subdirectories
2. If there is only one novel directory, use it
3. If there are multiple, read `novels/<slug>/novel.md` for each to see current status, then ask the author which novel to work on
4. All paths below are relative to `novels/<slug>/` where `<slug>` is the selected novel's directory name

## Your task

Conduct a systematic, multi-pass revision of the manuscript. Each pass targets a specific layer: structure, character, pacing, continuity, line quality, and rhythm.

## Prerequisites

Read ALL story artifacts and the full manuscript:
- `novels/<slug>/story/` -- all design documents
- `novels/<slug>/story/continuity.md` -- the continuity bible (critical for Pass 4)
- `novels/<slug>/manuscript/` -- all chapter files
- `novels/<slug>/story/revision-notes.md` -- if it exists (previous revision notes)

## Process

The author may request a specific pass or a full revision. Available passes:

### Pass 1: Continuity Edit (SEQUENTIAL — do not parallelize)

This is the most critical pass. It must be done **chapter by chapter in order**, maintaining a running state of what is established in prose. Do NOT read ahead. For each chapter, verify against what has been written so far (not what the outline says will happen later).

**Before starting:** Read `novels/<slug>/story/continuity.md` to load established facts, then verify each one chapter by chapter.

**Per-chapter checklist** (track in a running table as you go):

1. **Timeline**: What day/time is it? Does it follow logically from the previous chapter? Flag any impossible time jumps or contradictions.
2. **Character locations**: Where is each character? Can they physically be where the scene says they are given what happened last?
3. **Object states**: Track key objects (who has them, where are they). If a character uses something, did they acquire it? If something was left somewhere, is it still there?
4. **Physical descriptions**: Any character detail mentioned — hair, scars, tattoos, clothing, body language tics. Flag contradictions with prior chapters or the continuity bible.
5. **Knowledge consistency**: What does each character know at this point? Flag any moment where a character acts on information they haven't received yet.
6. **Emotional state carry-over**: Does each character's emotional state at chapter start match where they ended in their last POV chapter? (Not the previous chapter — their last POV appearance.)
7. **Forward references**: Flag ANY passage where a character reflects on, references, or emotionally processes a scene that hasn't happened yet in chapter order.
8. **Established facts**: If a character states something as fact (a date, a name, a detail), record it. Flag if it contradicts a prior statement.
9. **Sensory consistency**: Weather, time of day, lighting, sounds. If it was raining at the end of chapter 5, is it still raining at the start of chapter 6 (which is the same evening)?
10. **Dialogue callbacks**: When a character quotes or echoes an earlier line, verify the original wording matches.

**Output format for Pass 1:**
For each chapter, produce:
```
## Chapter N
- Timeline: Day X, [time]. ✅ / ⚠️ [issue]
- Locations: [who is where]. ✅ / ⚠️ [issue]
- Objects: [state changes]. ✅ / ⚠️ [issue]
- Knowledge: ✅ / ⚠️ [issue]
- Emotional carry-over: ✅ / ⚠️ [issue]
- New facts established: [list]
- Issues: [numbered list with exact quotes and line references]
```

After completing all chapters, update `novels/<slug>/story/continuity.md` with any new facts or corrections discovered.

### Pass 2: Structural Edit
Evaluate the manuscript against `novels/<slug>/story/outline.md`:
- Does each act fulfill its structural purpose?
- Are turning points landing where they should?
- Are there scenes that should be cut, added, or reordered?
- Is the climax resolving the central conflict?
- Report findings as a list of specific, actionable notes.

### Pass 3: Character Edit
Evaluate against character sheets in `novels/<slug>/story/characters/`:
- Is each character's voice distinct and consistent?
- Are motivations clear and tracked?
- Are arcs completing as designed?
- Flag moments where characters act out-of-character without justification.

### Pass 4: Pacing Edit
Evaluate against the pacing plan in `novels/<slug>/story/outline.md`:
- Identify dead spots where momentum stalls
- Flag scenes that run too long or too short
- Check chapter endings for hooks
- Assess the scene-to-sequel ratio

### Pass 5: Line Edit
Prose-level analysis, chapter by chapter:
- Identify filler words and crutch phrases
- Flag passive voice that weakens prose
- Suggest stronger verbs and sharper dialogue
- Note repetitive sentence patterns

**AI-generated prose patterns** (check specifically for these):
- Crutch words: "particular," "something about," "a sense of," "the weight of"
- Filter phrases: "she felt," "she noticed," "she realized," "she couldn't help but"
- Constructions: "the way [she/someone] [verb]," "the kind of [noun] that [clause]"
- Consecutive paragraphs opening with "She" or the POV character's name
- Over-explained metaphors (a strong image followed by a sentence explaining it)
- Heavy em-dash parentheticals that should be their own sentences
- Thought catalogues at chapter endings ("She thought about X. She thought about Y.")

### Pass 6: Read-Aloud (optional)
Flag rhythm and flow issues:
- Sentences that are awkward to read aloud
- Unnatural dialogue
- Monotonous sentence length patterns

## Iterative revision

Revision should be run **at least twice** when significant rewrites have occurred between passes (e.g., after the Expand step). The first pass catches structural and voice issues; the second catches consistency drift and new crutch-word accumulation introduced during rewriting. Each pass should produce its own revision notes; subsequent passes should read previous notes to avoid re-flagging fixed issues.

## Output

- Write revision notes to `novels/<slug>/story/revision-notes.md`
- For each issue, specify: chapter, location, problem, and suggested fix
- Prioritize issues by impact (continuity > structural > character > pacing > line)
- Update `novels/<slug>/story/continuity.md` if revision changes any established facts
- When all revision passes are complete: update `novels/<slug>/novel.md` to mark Step 9 (Revise) as `✅ Complete` with today's date, set `current_step` to `10`, set `current_step_name` to `"Polish"`
