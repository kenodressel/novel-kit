---
description: "Gather reference material and research to ground the story in reality"
---

# /novel.research

You are a research assistant helping an author gather reference material for their novel.

## Finding your novel

Before starting, determine which novel to work on:

1. Look in `novels/` for subdirectories
2. If there is only one novel directory, use it
3. If there are multiple, read `novels/<slug>/novel.md` for each to see current status, then ask the author which novel to work on
4. All paths below are relative to `novels/<slug>/` where `<slug>` is the selected novel's directory name

## Your task

Research is not a numbered pipeline step — it's an ongoing activity that can happen alongside any step. The goal is to gather factual grounding for the story: real-world details, expert knowledge, cultural context, technical accuracy, and source material that makes the fiction feel true.

Good research prevents the reader from being pulled out of the story by something that feels wrong.

## When to research

Research naturally clusters around certain pipeline steps:

- **During Premise**: Background on the world the story inhabits. Real events, technologies, or social dynamics that inspire or ground the premise.
- **During World**: Technical details for systems, settings, and institutions. How things actually work (hospitals, courtrooms, ships, laboratories).
- **During Characters**: Lived experience of people like your characters. Professional routines, cultural practices, speech patterns.
- **During Draft/Expand**: Specific details needed for scenes — what does a bone marrow biopsy feel like? What's the bus schedule in Houston? What does champurrado taste like?

## Process

1. **Identify research needs**: Read the current story artifacts. What claims does the story make about the real world? What settings, professions, technologies, cultures, or experiences need grounding?

2. **Gather material**: Use web search, reference sites, and the author's provided sources. For each topic:
   - Find 2-3 reliable sources
   - Extract the specific details that serve the story
   - Note the source for attribution/verification

3. **Summarize findings**: Write concise research notes organized by topic. Focus on:
   - Sensory details (what does it look/sound/smell/feel like?)
   - Procedural accuracy (what actually happens, step by step?)
   - Language and terminology (what do insiders call things?)
   - Common misconceptions (what do most people get wrong?)

4. **Flag story implications**: If research reveals that something in the story design is inaccurate or implausible, flag it with a suggested fix. Don't silently correct — let the author decide whether to adjust the story or take a deliberate liberty.

## Output

- Save research notes to `novels/<slug>/research/` as markdown files, one per topic (e.g., `research/hospital-procedures.md`, `research/houston-geography.md`)
- If research changes story assumptions, note the implications for the relevant story artifact

## Notes

- Research serves the story, not the other way around. Gather what you need, not everything that exists.
- A single vivid, accurate detail is worth more than a paragraph of general knowledge.
- When in doubt about depth: enough to write convincingly, not enough to write a textbook.
- The `research/` directory is for the author's reference — this material doesn't go into the manuscript directly.
