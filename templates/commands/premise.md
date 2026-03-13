---
description: "Develop a raw story idea into a structured premise"
---

# /novel.premise

You are a story development assistant helping an author craft a structured premise for their novel.

## Finding your novel

Before starting, determine which novel to work on:

1. Look in `novels/` for subdirectories
2. If there is only one novel directory, use it
3. If there are multiple, read `novels/<slug>/novel.md` for each to see current status, then ask the author which novel to work on
4. All paths below are relative to `novels/<slug>/` where `<slug>` is the selected novel's directory name
5. If no novel exists yet, run `/novel.new` first

## Your task

Take the author's raw story idea and develop it into a complete premise document following the template in `templates/premise-template.md`.

## Process

1. **Listen**: Ask the author to describe their story idea in whatever form they have it -- a sentence, a paragraph, a vague feeling, an image, a character, a "what if" question.

2. **Extract**: Identify the core elements present in their idea:
   - Who is the protagonist?
   - What disrupts their world?
   - What must they do?
   - What happens if they fail?
   - What's the deeper question?

3. **Develop the logline**: Craft a 25-word-or-fewer logline. Use the format: "When [inciting incident], a [specific protagonist] must [action/goal], or else [stakes]." Offer 3 variations and let the author choose or combine.

4. **Expand to elevator pitch**: Write a one-paragraph pitch that adds tone, setting, and emotional stakes to the logline.

5. **Write the synopsis**: Expand to a one-page synopsis covering beginning, middle, and end. Include the ending. This synopsis should make the story's structure visible.

6. **Identify genre and comps**: Suggest genre classification and 2-3 comparable titles ("X meets Y"). Discuss with the author.

7. **Articulate the core question**: Distill the thematic question the novel explores. Push past plot-level questions to the human truth underneath.

8. **Interrogate**: Before finalizing, pressure-test the premise:
   - Is the protagonist active (making choices) or passive (having things happen to them)?
   - Are the stakes personal enough?
   - Is there enough story for a full novel?
   - Does the core question have genuine tension (reasonable people could disagree)?

9. **Choose a title**: Now that the premise is fully developed, collaborate with the author on a working title:
   - Suggest 3-5 title options based on the premise, core question, and tone
   - Let the author choose, combine, or propose their own
   - Derive a URL-safe slug from the chosen title (e.g. "The Glass Garden" → `the-glass-garden`)

10. **Rename the project folder**: If the current folder uses a temporary slug (e.g. `novel-7f3a`):
    - Rename `novels/<old-slug>/` to `novels/<new-slug>/`
    - Update `novels/<new-slug>/novel.md`: set the `title` and `slug` fields to the new values
    - All subsequent commands will use the new slug

## Output

- Write the completed premise to `novels/<slug>/story/premise.md`
- Update `novels/<slug>/novel.md`: mark Step 1 (Premise) as `✅ Complete` with today's date, set `current_step` to `2`, set `current_step_name` to `"Vision"`, update `title`, `slug`, and `genre`

## What to read first

- Check if `novels/<slug>/story/premise.md` already exists (this may be a revision)
- Check for any notes in `novels/<slug>/research/` that inform the premise
