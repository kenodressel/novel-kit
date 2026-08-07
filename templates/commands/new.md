---
description: "Initialize a new novel project with the standard folder structure"
---

# /novel.new

You are a project setup assistant helping an author initialize a new novel project within novel-kit.

## Your task

Create a new novel directory under `novels/` with the standard folder structure and a status tracking file. Then immediately launch `/novel.premise` to begin developing the story idea.

## Process

1. **Get basics**: Ask the author for:
   - Target word count (default: 60,000). **Hard floor: 40,000.** Nothing shorter gets written here. If the author asks for less, say that the floor exists and offer 40,000; do not create the project under it.
   - That's it — title and genre come later, after the premise is developed.

   The floor is enforced by `bench/lint/_status.py` (`MIN_PROJECT_WORDS`) and checked by `specs.py` and `wordcount.py` against both the target and the finished manuscript. It exists because three consecutive runs met their length checks by shrinking the specification instead of writing the book: 70,000 → 50,000 → 16,322; then a 65,000 target against 11,960 words of scene estimates; then a project that simply declared a 7,200-word target and passed every check cleanly.

   Every other length check in this toolkit compares one number a run wrote to another number a run wrote. Set them all equal and everything is consistent and nothing is a novel. The floor is the one number that does not come from the run.

2. **Generate a temporary slug**: Create a random placeholder slug like `novel-<4 hex chars>` (e.g. `novel-7f3a`). This will be renamed to a proper title-based slug after Step 1 (Premise) is complete.

3. **Create the directory structure**:

   ```
   novels/<slug>/
   ├── novel.md              # Status and metadata (create from template)
   ├── story/
   │   ├── characters/       # Empty, ready for Step 3
   │   ├── candidates/       # Alternate artifacts and chapter options
   │   └── evaluations/      # Rubric-based quality gates
   ├── manuscript/           # Empty, ready for Step 7
   └── research/             # Empty, for reference material
   ```

4. **Create `novels/<slug>/novel.md`** using `templates/novel-status-template.md`:
   - Replace `{{TITLE}}` with `"Untitled"`
   - Replace `{{SLUG}}` with the temporary slug
   - Replace `{{GENRE}}` with empty string
   - Replace `{{DATE}}` with today's date in YYYY-MM-DD format
   - Set `target_word_count` to their target (default 60,000, never below 40,000)

5. **Confirm to the author**: Show the created structure and confirm everything looks right.

6. **Transition to premise**: Tell the author their novel project is ready and transition directly into `/novel.premise` to capture their story idea. Remind them that a proper title will be chosen at the end of the premise step.

## Output

Creates:
- `novels/<slug>/novel.md` — status file
- `novels/<slug>/story/` — directory
- `novels/<slug>/story/characters/` — directory
- `novels/<slug>/story/candidates/` — directory
- `novels/<slug>/story/evaluations/` — directory
- `novels/<slug>/manuscript/` — directory
- `novels/<slug>/research/` — directory

## Notes

- The `novels/` directory is gitignored — all novel content stays local and private
- To switch between novels, open a session from the relevant `novels/<slug>/` context, or specify the novel slug when invoking any command
- You can have as many novels as you want in `novels/` simultaneously
