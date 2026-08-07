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
- `novels/<slug>/story/style-guide.md` -- voice and prose constraints
- `novels/<slug>/story/motifs.md` -- thematic recurrence and symbolic load
- `novels/<slug>/manuscript/` -- all chapter files
- `novels/<slug>/story/revision-notes.md` -- if it exists (previous revision notes)

## Process

The author may request a specific pass or a full revision. Available passes:

### Pass 0: Mechanical Sweep (REQUIRED — run before any reading pass)

Machines are better than readers at counting, and worse at judging. Run the counters first so the reading passes know where to look.

```
python3 bench/lint/prose_sanity.py     novels/<slug>   # run this FIRST OF ALL
python3 bench/lint/wordcount.py        novels/<slug>
python3 bench/lint/repetition.py       novels/<slug>
python3 bench/lint/continuity_facts.py novels/<slug>
python3 bench/lint/names.py            novels/<slug>   # cross-novel name collisions
python3 bench/lint/fingerprint.py      novels/<slug>   # against style-guide.md targets
```

`prose_sanity.py` comes first because there is no point revising text that is not prose. It asks whether the manuscript is narrative at all: unique-sentence ratio, scaffolding phrases like "during beat 8" that were never replaced with events, verbatim duplicate paragraphs, dialogue share, and chapters that open with the same sentence. A run once met a 50,000-word target by looping a handful of template sentences with the chapter number substituted in — 4.1% of sentences unique, 2,997 scaffolding leaks, 0.6% dialogue — and passed every length and structure check cleanly, because those verify quantities and this was the right quantity.

`wordcount.py` comes next because a manuscript short of its own specification cannot be fixed by revision passes — it needs `/novel.realize`, and every prose metric flatters a chapter that is too thin to contain its own scene.

`repetition.py` reports phrases and distinctive words recurring above the budget in `style-guide.md`, near-duplicate sentences across chapters, and in-chapter word-frequency outliers. `continuity_facts.py` extracts every number, price, date, time, age, and measurement per chapter and reports contradictions between them and against `continuity.md`.

These are pointers, not verdicts. Read every flagged passage before changing it — a script cannot tell a deliberate refrain from a forgotten one. But do not skip the sweep on the grounds that you will notice these while reading. Measured misses from careful human and AI drafts alike: a phrase repeated twelve times in 5,500 words; a whole closing sentence duplicated near-verbatim 150 lines apart; a price stated as eleven dollars, then eighteen, then "$8.50, same as always."

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

**Unedited-draft prose patterns** (check specifically for these — the counts below are measured, not guessed):

- **The characterising appositive**: `with the [abstract noun] of [someone] who [does X]`. The single highest-signal marker. 218 occurrences in one unedited 349,000-word corpus; **zero** in 749,000 words of published fiction by five authors. Count it. If it is over budget, the narrator has no idiom of its own and is using simile to certify characters — fix the idiom rather than the sentences, or a substitute tic replaces it.
- **The negation triad**: "Not a thought. Not a decision. Just —" and `not X but Y`. Present in six of seven measured drafts, and it survives translation into other languages, which is how you know it is a habit rather than a style.
- **Inanimate volition**: objects, buildings, and weather given intentions, beliefs, and opinions. "as if it didn't believe the day was over", "a refrigerator that knew it should have been replaced", "as if the weather had decided to forgive". Published prose does this roughly one-tenth as often, and when it does, the thing is often literally sentient.
- **The self-explaining closer**: a paragraph or scene ending by naming its own significance. In one measured set, every extract closed its opening movement by announcing the protagonist's theme, wound, or competence. And note the correlation: the extracts that explained themselves were the same ones with the longest runways. The gloss is compensating for a scene that did no work — so treat it as a symptom and check the scene, not just the sentence.
- **Thesis restatement**: the same idea about a character delivered three to twelve times in different words. Rule: when a fact has been dramatised, delete the narrator's later summary. The summary is always the weaker version.
- **Section-shape lock**: every scene opening and closing on the same move. List the closing move of all scenes in a chapter group; three or more identical is a finding.
- **POV break to deliver information**: flash-forwards, a second character's interior, second-person address to the reader. This is the scene admitting it could not deliver a fact the reader needs. Restructure the scene.
- **Single-engine dialogue**: every character speaking in the same rhetorical move — commonly flat-statement-plus-witty-reversal. Test: strip the attributions from one line per character and try to reassign them. Measured failure: twelve-year-olds indistinguishable from adults across six characters.
- Crutch words: "particular," "specific," "something about," "a sense of," "the weight of" — count them; "specific" used four times in a chapter is the prose asking to be specific instead of being specific
- Filter phrases: "she felt," "she noticed," "she realized," "she couldn't help but"
- `the way [she/someone] [verb]` as the default simile frame, and `the kind of [noun] that [clause]`
- Consecutive paragraphs opening with "She" or the POV character's name
- Over-explained metaphors (a strong image followed by a sentence explaining it)
- A motif explained aloud by a character — when someone says "that is not comfort, that is a fortification", the image has stopped working and is being narrated
- Heavy em-dash parentheticals that should be their own sentences
- Thought catalogues at chapter endings ("She thought about X. She thought about Y.")

None of these are artifacts of machine generation. Every one of them was also measured, at comparable or higher rates, in an unedited self-published novel written by a human. They are the defects of a first draft that has not met an editor.

### Pass 6: Boredom / Genericity Edit

This pass is reader-facing rather than document-facing:
- Identify scenes that are competent but forgettable
- Flag dialogue that could belong to any character in any book
- Mark predictable beats the reader can see too early
- Find places where the prose sounds assembled, padded, or model-default
- Recommend whether to cut, branch, or fully rewrite the scene

### Pass 7: Read-Aloud (optional)
Flag rhythm and flow issues:
- Sentences that are awkward to read aloud
- Unnatural dialogue
- Monotonous sentence length patterns

## Iterative revision

Revision should be run **at least twice** when significant rewrites have occurred between passes (e.g., after the Realize step). The first pass catches structural and voice issues; the second catches consistency drift and new crutch-word accumulation introduced during rewriting. Each pass should produce its own revision notes; subsequent passes should read previous notes to avoid re-flagging fixed issues.

## Output

- Write revision notes to `novels/<slug>/story/revision-notes.md`
- For each issue, specify: chapter, location, problem, and suggested fix
- Prioritize issues by impact (continuity > structural > character > pacing > line)
- Update `novels/<slug>/story/continuity.md` if revision changes any established facts
- If revision discovers unsupported real-world claims, send them to `/novel.research`
- When all revision passes are complete: update `novels/<slug>/novel.md` to mark Step 9 (Revise) as `✅ Complete` with today's date, set `current_step` to `10`, set `current_step_name` to `"Polish"`
