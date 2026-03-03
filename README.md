# novel-kit

A **specification-driven toolkit for writing novels**, inspired by [spec-kit](https://github.com/github/spec-kit).

Spec-kit inverted software development by making *specifications* the primary artifact instead of code. **novel-kit** applies the same inversion to fiction: the *story design* is the primary artifact, and the prose is its faithful implementation.

Most novels fail not in the writing, but in the planning. novel-kit gives you a structured, AI-assisted workflow that takes a story from a one-sentence premise to a polished manuscript -- with every creative decision documented and traceable.

## Philosophy

> "The first draft is just you telling yourself the story." -- Terry Pratchett

But you shouldn't be *discovering* the story during the first draft. You should be **executing** a design you already trust.

novel-kit follows **Story-Driven Development (StDD)**: a creative methodology where structured story design artifacts drive the writing of prose, not the other way around.

**The Power Inversion**: For centuries, novelists have started with a blank page and "found" the story through drafting. StDD flips this. You design the story first -- its vision, characters, world, structure, and scenes -- and then write prose that serves that design. AI assists at every stage, interrogating your choices, finding plot holes, and generating drafts that stay faithful to your specifications.

### Core Principles

1. **Design Before Drafting** -- Every chapter you write should trace back to a deliberate creative decision
2. **Characters Are Architecture** -- A story's structure emerges from who your characters are, not from imposed plot formulas
3. **World Serves Story** -- World-building exists to create the conditions for conflict, not as an end in itself
4. **Iterative Deepening** -- Start with one sentence, expand to one paragraph, then one page, then full scenes (inspired by the [Snowflake Method](https://www.advancedfictionwriting.com/articles/snowflake-method/))
5. **Interrogate Relentlessly** -- Every assumption gets pressure-tested before you commit it to prose
6. **Drafting Is Implementation** -- The first draft is not exploration; it is the execution of a validated design

## The Workflow

novel-kit prescribes a **9-step pipeline** from spark to polished manuscript. Each step produces a concrete artifact that feeds the next.

```
Premise ──> Vision ──> Characters ──> World ──> Outline ──> Scenes ──> Draft ──> Revise ──> Polish
  (1)        (2)         (3)          (4)        (5)         (6)        (7)       (8)        (9)
```

### Step 1: Premise (`/novel.premise`)

Capture the core story idea in a structured format: a one-sentence logline, a one-paragraph pitch, and a one-page synopsis. This is the seed everything else grows from.

**Produces**: `story/premise.md`

**Key sections**:
- Logline (25 words or fewer)
- Elevator pitch (one paragraph)
- Synopsis (one page)
- Genre and comparable titles
- Core question the novel asks
- Why this story, why now

---

### Step 2: Creative Vision (`/novel.vision`)

Establish the governing creative principles for your novel -- the equivalent of a project constitution. This defines tone, themes, audience, and the rules you will not break.

**Produces**: `story/vision.md`

**Key sections**:
- Genre and subgenre conventions (and which you'll subvert)
- Target audience and reading experience
- Themes and motifs
- Narrative voice and POV strategy
- Tone and style guidelines
- Content boundaries (what this story is and isn't)
- Thematic thesis (what the story argues)

---

### Step 3: Characters (`/novel.characters`)

Design your cast. Each major character gets a full profile: backstory, psychology, desire, flaw, arc, relationships, and voice. Minor characters get abbreviated sheets.

**Produces**: `story/characters/` (one file per major character, plus `cast.md` overview)

**Key sections per character**:
- Role in story (protagonist, antagonist, ally, etc.)
- Background and biography
- Psychological profile (desire, fear, misbelief, need)
- Character arc (who they are at start vs. end)
- Relationships and dynamics with other characters
- Distinctive voice, speech patterns, mannerisms
- Key scenes and turning points

---

### Step 4: World Building (`/novel.world`)

Define the setting -- physical, social, political, magical, technological -- at the level of detail your story requires. World-building is in service of conflict and character, not encyclopedic completeness.

**Produces**: `story/world.md` (plus optional sub-documents for complex worlds)

**Key sections**:
- Setting overview (time, place, scope)
- Rules and systems (magic, technology, social structure)
- History and context (only what affects the story)
- Key locations (described through character experience)
- Culture and daily life
- Constraints and limitations (what characters cannot do)
- Sensory palette (what this world looks, sounds, smells like)

---

### Step 5: Story Outline (`/novel.outline`)

Design the narrative architecture. Map the story's major movements, turning points, and emotional arc using a structure that fits your genre (three-act, hero's journey, Save the Cat, Kishotenketsu, or custom).

**Produces**: `story/outline.md`

**Key sections**:
- Structural framework choice and rationale
- Act/part breakdown with narrative purpose of each
- Major plot points and turning points
- Subplots and how they interweave with the main plot
- Emotional arc (reader experience by act)
- Pacing plan (tension curve)
- Thematic throughline per act
- Foreshadowing and payoff map

---

### Step 6: Scene Breakdown (`/novel.scenes`)

Convert the outline into a scene-by-scene blueprint. Every scene has a purpose, a POV character, a conflict, and a turning point. This is the granular plan you'll draft from.

**Produces**: `story/scenes.md`

**Key sections per scene**:
- Scene ID and chapter assignment
- POV character
- Scene goal (what the POV character wants)
- Conflict (what opposes them)
- Outcome (yes-but / no-and)
- Emotional shift (how the reader should feel before vs. after)
- Key beats and information revealed
- Setup/payoff connections to other scenes
- Estimated word count

---

### Step 7: First Draft (`/novel.draft`)

Write the manuscript, scene by scene, following the scene breakdown. AI assists by generating prose that adheres to your vision, character voices, and scene specifications. You write, rewrite, or direct.

**Produces**: `manuscript/` (chapter files)

**Approach**:
- Draft sequentially or by subplot -- your choice
- Each scene references its specification from Step 6
- Maintain a running `story/continuity.md` log for details established in prose
- Target word count per scene, guided by pacing plan
- Flag deviations from the outline for later reconciliation

---

### Step 8: Revision (`/novel.revise`)

Systematic multi-pass revision. Each pass targets a different layer, from structural coherence down to line-level prose quality.

**Produces**: Updated `manuscript/` + `story/revision-notes.md`

**Revision passes**:
1. **Structural pass** -- Does the plot work? Are arcs complete? Cut/add/reorder scenes
2. **Character pass** -- Is every character's voice distinct? Are arcs earned? Do motivations track?
3. **Pacing pass** -- Does tension build correctly? Are there dead spots? Is the page-turn factor there?
4. **Continuity pass** -- Timeline consistency, factual accuracy, world-rule compliance
5. **Line pass** -- Prose quality, dialogue sharpening, sensory detail, eliminating crutch words
6. **Read-aloud pass** -- Rhythm, flow, and ear

---

### Step 9: Polish (`/novel.polish`)

Incorporate external feedback from beta readers and prepare the manuscript for submission or publication.

**Produces**: Final `manuscript/` + `story/beta-feedback.md`

**Activities**:
- Beta reader recruitment and questionnaire design
- Feedback synthesis (common themes across readers)
- Final revision incorporating feedback
- Line editing and copyediting
- Query letter / blurb / synopsis for submission
- Formatting for target publication path

---

## Project Structure

novel-kit lives in a single repo. Your novels live inside it under `novels/`, which is gitignored — your writing stays private, the toolkit stays shareable.

```
novel-kit/
├── novels/                         # gitignored — your actual novels live here
│   ├── my-thriller/
│   │   ├── novel.md                # Status: current step, word count, pipeline progress
│   │   ├── story/
│   │   │   ├── premise.md          # Step 1: The seed
│   │   │   ├── vision.md           # Step 2: Creative constitution
│   │   │   ├── characters/         # Step 3: Character sheets
│   │   │   │   ├── cast.md         # Cast overview and dynamics
│   │   │   │   ├── protagonist.md  # One file per major character
│   │   │   │   └── ...
│   │   │   ├── world.md            # Step 4: World building
│   │   │   ├── outline.md          # Step 5: Narrative structure
│   │   │   ├── scenes.md           # Step 6: Scene-by-scene blueprint
│   │   │   ├── continuity.md       # Running continuity log
│   │   │   ├── revision-notes.md   # Step 8: Revision tracking
│   │   │   └── beta-feedback.md    # Step 9: External feedback
│   │   ├── manuscript/
│   │   │   ├── chapter-01.md       # Step 7: The actual prose
│   │   │   ├── chapter-02.md
│   │   │   └── ...
│   │   └── research/               # Reference material, inspiration, notes
│   └── my-romance/                 # Work on multiple novels simultaneously
│       ├── novel.md
│       └── ...
├── templates/
│   ├── commands/                   # AI command files
│   ├── novel-status-template.md    # Template for novel.md
│   └── *.md                        # Story artifact templates
└── docs/
```

### The `novel.md` status file

Each novel has a `novel.md` at its root that tracks pipeline progress:

```markdown
---
title: "My Thriller"
slug: "my-thriller"
current_step: 3
current_step_name: "Characters"
target_word_count: 90000
current_word_count: 0
---

| Step | Name       | Status         | Completed  |
|------|------------|----------------|------------|
| 1    | Premise    | ✅ Complete    | 2026-03-01 |
| 2    | Vision     | ✅ Complete    | 2026-03-02 |
| 3    | Characters | ⏳ In Progress | —          |
| 4    | World      | ⬜ Pending     | —          |
...
```

Every command reads and updates this file automatically.

## Templates

novel-kit ships with structured templates for every artifact. Templates encode best practices from established methodologies:

| Template | Inspired By |
|---|---|
| `premise-template.md` | Save the Cat logline formula, Snowflake Method Step 1 |
| `vision-template.md` | spec-kit's Constitution, genre convention analysis |
| `character-template.md` | Snowflake Method character sheets, Enneagram/wound-based arcs |
| `world-template.md` | Sanderson's iceberg principle, sensory-first world design |
| `outline-template.md` | Three-act structure, Save the Cat beat sheet, Story Grid |
| `scenes-template.md` | Scene-sequel pattern, yes-but/no-and outcomes |
| `revision-template.md` | Multi-pass developmental editing, Susan Bell's revision layers |

## AI Commands

Each step has a corresponding AI command that guides an LLM through the process:

| Command | Step | What it does |
|---|---|---|
| `/novel.new` | — | Initializes a new novel directory with status tracking |
| `/novel.premise` | 1 | Develops raw idea into structured premise |
| `/novel.vision` | 2 | Establishes creative principles and constraints |
| `/novel.characters` | 3 | Builds deep character profiles with arcs |
| `/novel.world` | 4 | Designs setting in service of story |
| `/novel.outline` | 5 | Architects narrative structure |
| `/novel.scenes` | 6 | Breaks outline into scene-level specifications |
| `/novel.draft` | 7 | Generates prose following scene specs |
| `/novel.revise` | 8 | Runs multi-pass revision analysis |
| `/novel.polish` | 9 | Prepares manuscript for readers and submission |
| `/novel.interrogate` | Any | Pressure-tests any artifact for gaps and contradictions |

## Quick Start

```bash
# 1. Clone novel-kit
git clone <novel-kit-repo-url>
cd novel-kit

# 2. Open your AI assistant (Claude Code) in this directory
# Then initialize a new novel:
/novel.new

# 3. Follow the pipeline — each command picks up where the last left off
/novel.premise
/novel.vision
/novel.characters
/novel.world
/novel.outline
/novel.scenes
/novel.draft
```

Each command reads the artifacts from previous steps, so the AI always has full context of your creative decisions. When working on multiple novels, every command checks `novels/<slug>/novel.md` to show you the current pipeline status and asks which novel to work on if you have more than one.

## Mapping to spec-kit

For those familiar with [spec-kit](https://github.com/github/spec-kit), here's how the concepts translate:

| spec-kit | novel-kit | Rationale |
|---|---|---|
| Constitution | Creative Vision | Governing principles and constraints |
| Specification | Premise & Synopsis | The "what and why" of the thing being built |
| Clarify | Interrogate | Pressure-testing assumptions and resolving ambiguity |
| Plan | Story Outline | The architectural design |
| Tasks | Scene Breakdown | Granular executable units of work |
| Implement | First Draft | Producing the actual output |
| Checklist | Revision Passes | Quality validation |
| Analyze | Continuity Check | Cross-artifact consistency |

## Why This Works

Structured story design isn't new. Professional screenwriters use beat sheets. TV writers use story bibles. Game designers use narrative design documents. But novelists often resist structure, fearing it kills creativity.

novel-kit's position: **structure liberates creativity**. When you know where you're going, you're free to focus on *how* you get there -- the prose, the voice, the surprising details that make fiction come alive. You're not wasting creative energy on solved problems (where does this plot go?) and can spend it on unsolved ones (how does this character's grief sound in their internal monologue?).

Combined with AI assistance, this approach means:
- **Fewer dead-end drafts** -- you catch structural problems before writing 80,000 words
- **Consistent quality** -- every scene has a clear purpose and specification
- **Faster iteration** -- change the outline, regenerate affected scenes
- **Traceable decisions** -- you can always answer "why does this scene exist?"

## Contributing

This project is in early development. Contributions welcome -- especially:
- Additional templates for specific genres (romance, mystery, sci-fi, literary fiction)
- Alternative structural frameworks (Kishotenketsu, Dan Harmon's Story Circle, etc.)
- Integration with writing tools (Scrivener export, Fountain format, etc.)

## License

MIT

---

*Inspired by [spec-kit](https://github.com/github/spec-kit) and the principle that the best creative work comes from the intersection of structure and imagination.*
