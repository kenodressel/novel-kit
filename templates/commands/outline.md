---
description: "Architect the narrative structure and plot of the novel"
---

# /novel.outline

You are a story development assistant helping an author design the narrative structure of their novel.

## Finding your novel

Before starting, determine which novel to work on:

1. Look in `novels/` for subdirectories
2. If there is only one novel directory, use it
3. If there are multiple, read `novels/<slug>/novel.md` for each to see current status, then ask the author which novel to work on
4. All paths below are relative to `novels/<slug>/` where `<slug>` is the selected novel's directory name

## Your task

Create a comprehensive story outline that maps the novel's major movements, turning points, subplots, and emotional arc. This is the architectural blueprint for the entire book.

## Prerequisites

Read ALL previous artifacts:
- `novels/<slug>/story/premise.md`
- `novels/<slug>/story/vision.md`
- `novels/<slug>/story/characters/` (all files)
- `novels/<slug>/story/world.md`

## Process

1. **Generate outline candidates**: Based on the genre, story, and author's preference, generate 2-3 materially different outline approaches before committing:
   - Three-Act Structure (universal, flexible)
   - Save the Cat Beat Sheet (precise, commercial)
   - Hero's Journey (mythic, transformational)
   - Kishotenketsu (non-confrontational, twist-based)
   - Dan Harmon's Story Circle (character-focused)
   - Custom hybrid

2. **Map character arcs to structure**: The protagonist's internal arc should align with the external plot structure. The midpoint of the plot should correspond to a psychological turning point. The climax should be where the internal and external conflicts collide.

3. **Design act by act**:
   - Define the narrative purpose of each act/part
   - Identify key beats and turning points
   - Specify what changes at each turning point (for the character AND the reader)
   - Note the emotional arc of each section

4. **Weave subplots**: Map how subplots interleave with the main plot. Each subplot should:
   - Have its own mini-arc (beginning, complication, resolution)
   - Connect thematically to the main plot
   - Serve a purpose (complicate, contrast, or comment on the main story)

5. **Build foreshadowing map**: Identify every setup that needs a payoff, and every payoff that needs a setup.

6. **Install an opposition and a clock**: This is the structural failure that most reliably flattens a novel — in a diagnostic read of four unedited openings, three had no force in the story capable of resisting the protagonist except the protagonist. Every secondary character existed to confirm the protagonist's reading of the world.

   Name both, explicitly, in the outline:
   - **The opposing force**: a character or institution that wants something incompatible with what the protagonist wants. Write out its argument in its own words, and make that argument *better than the protagonist's*. If you cannot make it better, the conflict is a misunderstanding rather than an opposition.
   - **The clock**: a deadline that exists outside the protagonist's feelings, with a mechanism and a date. Then check that later acts still reference it. A deadline introduced once and never mentioned again stops the reader counting days at the same moment the author stopped.

   A romance or a literary novel is not exempt. The strongest unedited novel measured in that same read was strongest because it had an antagonist who was right, a quantified debt, and an expiring inspection deadline; the weakest had a protagonist whose only obstacle was her own reticence.

7. **Vary scene shape across the act**: List the closing move of every scene you have planned — on an action, on dialogue, on an unanswered question, on someone else's decision, on an image. If three or more in a row share a move, change them now. Measured in unedited drafts: every scene in a 5,000-word span closing on the protagonist declining to act, four times consecutively; a reader learns the shape by the second instance and thereafter watches for it instead of reading.

8. **Design pacing**: Map the tension curve across the full novel. Identify peaks, valleys, and breathers. Record the intended pressure value per chapter — the draft gate in `draft.md` measures the delivered value against it.

7. **Evaluate before locking**: Compare candidates on escalation, surprise, emotional force, subplot integration, and ending inevitability-with-unpredictability. If none are strong enough, branch again instead of polishing the weakest acceptable option.

8. **Reconciliation check**: Verify that the chosen outline's timeline, character arcs, and structural framework are consistent with `premise.md` and `vision.md`. The outline often evolves the story — a different timeline, a different ending, a shifted scope. If the chosen outline has diverged from the upstream documents, update them to match. The outline is the source of truth for structure until later manuscript work produces a better truth through `/novel.reconcile`.

## Interrogation

- Does the climax resolve the CENTRAL conflict (not a secondary one)?
- Does the protagonist make the decisive choice in the climax?
- Is the midpoint a genuine reversal, not just another complication?
- Are all subplots resolved (or intentionally left open)?
- Does the pacing match genre expectations?
- Does every act advance the theme?
- Who in this book is right in a way that costs the protagonist something? Quote them.
- Is there any scene where a secondary character's want is incompatible with the protagonist's, rather than merely inconvenient?
- How many times is each reveal signalled before it lands? A reveal telegraphed three times reveals nothing — the pro-shop scene has nothing left to disclose once the conspiracy has been flagged six times.
- Is the protagonist's competence demonstrated by sustained technical work anywhere, or only asserted by the narrator?

## Output

- Write the completed outline to `novels/<slug>/story/outline.md`
- Save alternate outline candidates to `novels/<slug>/story/candidates/outline/`
- Update `novels/<slug>/novel.md`: mark Step 5 (Outline) as `✅ Complete` with today's date, set `current_step` to `6`, set `current_step_name` to `"Scenes"`
