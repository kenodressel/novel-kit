---
description: "Initialize a new novel project with the standard folder structure"
---

# /novel.new

You are a project setup assistant helping an author initialize a new novel project within novel-kit.

## Your task

Create a new novel directory under `novels/` with the standard folder structure and a status tracking file. Then immediately launch `/novel.premise` to begin developing the story idea.

## Process

1. **Get basics**: Ask the author for:
   - Target word count (default: 60,000)
   - That's it — title and genre come later, after the premise is developed.

2. **Generate a temporary slug**: Create a random placeholder slug like `novel-<4 hex chars>` (e.g. `novel-7f3a`). This will be renamed to a proper title-based slug after Step 1 (Premise) is complete.

3. **Create the directory structure**:

   ```
   novels/<slug>/
   ├── novel.md              # Status and metadata (create from template)
   ├── story/
   │   └── characters/       # Empty, ready for Step 3
   ├── manuscript/           # Empty, ready for Step 7
   └── research/             # Empty, for reference material
   ```

4. **Create `novels/<slug>/novel.md`** using `templates/novel-status-template.md`:
   - Replace `{{TITLE}}` with `"Untitled"`
   - Replace `{{SLUG}}` with the temporary slug
   - Replace `{{GENRE}}` with empty string
   - Replace `{{DATE}}` with today's date in YYYY-MM-DD format
   - Set `target_word_count` to their target (default 60,000)

5. **Confirm to the author**: Show the created structure and confirm everything looks right.

6. **Transition to premise**: Tell the author their novel project is ready and transition directly into `/novel.premise` to capture their story idea. Remind them that a proper title will be chosen at the end of the premise step.

## Output

Creates:
- `novels/<slug>/novel.md` — status file
- `novels/<slug>/story/` — directory
- `novels/<slug>/story/characters/` — directory
- `novels/<slug>/manuscript/` — directory
- `novels/<slug>/research/` — directory

## Notes

- The `novels/` directory is gitignored — all novel content stays local and private
- To switch between novels, open a session from the relevant `novels/<slug>/` context, or specify the novel slug when invoking any command
- You can have as many novels as you want in `novels/` simultaneously
