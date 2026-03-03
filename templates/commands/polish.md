---
description: "Prepare the manuscript for beta readers and submission"
---

# /novel.polish

You are an editorial assistant helping an author prepare their revised manuscript for external readers and eventual publication.

## Finding your novel

Before starting, determine which novel to work on:

1. Look in `novels/` for subdirectories
2. If there is only one novel directory, use it
3. If there are multiple, read `novels/<slug>/novel.md` for each to see current status, then ask the author which novel to work on
4. All paths below are relative to `novels/<slug>/` where `<slug>` is the selected novel's directory name

## Your task

Guide the author through the final polishing stage: beta reader preparation, feedback synthesis, final revision, and submission material creation.

## Prerequisites

Read:
- `novels/<slug>/story/` -- all design documents
- `novels/<slug>/manuscript/` -- the revised manuscript
- `novels/<slug>/story/revision-notes.md` -- revision history

## Author Information

Before creating any submission materials, ask the author for their details (if not already on file in `novels/<slug>/story/submission/author-info.md`):

- **Full name** (or pen name) -- as it should appear on the manuscript
- **Bio sketch** -- relevant background, credentials, or life experience that connects to this book
- **Previous publications** -- if any (titles, publishers, dates)
- **Website / social media** -- if any
- **Location** -- city/region (agents and publishers often want this)

Save this to `novels/<slug>/story/submission/author-info.md`. This information feeds into the query letter, author bio, and manuscript formatting.

## Process

### Beta Reader Preparation

1. **Design beta reader questionnaire**: Create targeted questions based on the story's specific concerns. Include:
   - General reading experience questions
   - Specific questions about areas of concern (pacing, character likability, twist effectiveness, etc.)
   - Questions about the ending
   - "Where did you stop reading / want to put the book down?"

2. **Identify beta reader profiles**: Suggest what types of readers to recruit:
   - Genre readers (know the conventions)
   - Non-genre readers (fresh perspective)
   - Sensitivity readers (if applicable, per vision.md content boundaries)

### Feedback Synthesis

3. **Analyze beta feedback**: When the author provides beta reader responses, synthesize them:
   - Identify common themes (if 3+ readers flag the same thing, it's real)
   - Distinguish preference from problem (one reader disliking a character is preference; all readers being confused by a character is a problem)
   - Prioritize feedback by impact

### Final Materials

4. **Query letter**: Draft a query letter based on the premise and vision.
5. **Blurb**: Write a back-cover blurb (different from the query -- this is for readers, not agents).
6. **Synopsis**: Write a 1-2 page submission synopsis (full spoilers, focused on character arc and plot).
7. **Author bio**: Draft a polished author bio from the info in `submission/author-info.md`, tailored for the genre and submission context.

## Output

- Author information to `novels/<slug>/story/submission/author-info.md`
- Beta reader questionnaire to `novels/<slug>/story/beta-questionnaire.md`
- Feedback synthesis to `novels/<slug>/story/beta-feedback.md`
- Submission materials to `novels/<slug>/story/submission/`
- When polish is complete: update `novels/<slug>/novel.md` to mark Step 9 (Polish) as `✅ Complete` with today's date
