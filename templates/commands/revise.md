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

### Pass 1: Structural Edit
Evaluate the manuscript against `novels/<slug>/story/outline.md`:
- Does each act fulfill its structural purpose?
- Are turning points landing where they should?
- Are there scenes that should be cut, added, or reordered?
- Is the climax resolving the central conflict?
- Report findings as a list of specific, actionable notes.

### Pass 2: Character Edit
Evaluate against character sheets in `novels/<slug>/story/characters/`:
- Is each character's voice distinct and consistent?
- Are motivations clear and tracked?
- Are arcs completing as designed?
- Flag moments where characters act out-of-character without justification.

### Pass 3: Pacing Edit
Evaluate against the pacing plan in `novels/<slug>/story/outline.md`:
- Identify dead spots where momentum stalls
- Flag scenes that run too long or too short
- Check chapter endings for hooks
- Assess the scene-to-sequel ratio

### Pass 4: Continuity Edit
Cross-reference `novels/<slug>/story/continuity.md` with the manuscript:
- Timeline consistency
- Physical description consistency
- World-rule compliance
- Information-knowledge consistency (characters only know what they should)
- **Forward references**: Flag any passage where a character reflects on, references, or emotionally processes a scene that hasn't happened yet in the manuscript's chapter order
- **Emotional escalation**: Check that relationship milestones (first vulnerability, first trust, first intimacy) appear in the right order and aren't echoed in earlier chapters before they've been earned

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

### Pass 6: Read-Aloud
Flag rhythm and flow issues:
- Sentences that are awkward to read aloud
- Unnatural dialogue
- Monotonous sentence length patterns

## Iterative revision

Revision should be run **at least twice** when significant rewrites have occurred between passes (e.g., after the Expand step). The first pass catches structural and voice issues; the second catches consistency drift and new crutch-word accumulation introduced during rewriting. Each pass should produce its own revision notes; subsequent passes should read previous notes to avoid re-flagging fixed issues.

## Output

- Write revision notes to `novels/<slug>/story/revision-notes.md`
- For each issue, specify: chapter, location, problem, and suggested fix
- Prioritize issues by impact (structural > character > pacing > continuity > line)
- Update `novels/<slug>/story/continuity.md` if revision changes any established facts
- When all revision passes are complete: update `novels/<slug>/novel.md` to mark Step 9 (Revise) as `✅ Complete` with today's date, set `current_step` to `10`, set `current_step_name` to `"Polish"`
