# novel-kit

Design the story first. Write it second. AI assists throughout.

> **TL;DR**: A 10-step pipeline that takes a novel from one-sentence idea to polished manuscript. You design the story (premise, characters, world, structure, scenes), then draft, expand, revise, and polish. Every creative decision is documented. AI interrogates your choices, generates drafts that follow your specs, and edits against your own design docs. Your writing stays private (`novels/` is gitignored), the toolkit is shareable.
>
> ```
> /novel.new → /novel.premise → /novel.vision → /novel.characters → /novel.world →
> /novel.outline → /novel.scenes → /novel.draft → /novel.expand → /novel.revise → /novel.polish
> ```

---

## Philosophy

Inspired by [spec-kit](https://github.com/github/spec-kit), which inverted software development by making specifications the primary artifact. **novel-kit** applies the same inversion to fiction: the *story design* drives the prose, not the other way around.

1. **Design before drafting** -- Every chapter traces to a deliberate creative decision. Characters, world, structure, and scenes are designed before a word of prose is written.
2. **Interrogate relentlessly** -- Every assumption gets pressure-tested. AI finds the plot holes, flat characters, and structural problems before you write 80,000 words around them.
3. **Drafting is implementation, not exploration** -- The first draft executes a validated design. Discovery happens in the design phase. Expansion, revision, and polish happen after.

## The Pipeline

10 steps from idea to manuscript. Each step produces an artifact that feeds the next.

| Step | Command | Produces | What happens |
|------|---------|----------|-------------|
| 1 | `/novel.premise` | `story/premise.md` | Logline, pitch, synopsis, core question |
| 2 | `/novel.vision` | `story/vision.md` | Tone, themes, voice, POV, non-negotiables |
| 3 | `/novel.characters` | `story/characters/` | Psychology, arcs, relationships, voice fingerprints |
| 4 | `/novel.world` | `story/world.md` | Systems, locations, sensory palette |
| 5 | `/novel.outline` | `story/outline.md` | Structure, turning points, subplots, pacing curve |
| 6 | `/novel.scenes` | `story/scenes.md` | Scene-by-scene specs + continuity bible initialized |
| 7 | `/novel.draft` | `manuscript/` | Prose, scene by scene, following specs |
| 8 | `/novel.expand` | `manuscript/` (expanded) | Sensory detail, dialogue, interiority to target length |
| 9 | `/novel.revise` | `story/revision-notes.md` | 6-pass revision (structural → line → read-aloud), iterative |
| 10 | `/novel.polish` | `story/submission/` | Beta questionnaire, query letter, blurb, synopsis |

Plus two cross-cutting commands:
- `/novel.research` -- Gather reference material (optional, any stage)
- `/novel.interrogate` -- Pressure-test any artifact for gaps and contradictions

### Why Expand is its own step

First drafts -- especially AI-assisted ones -- come in compressed. In practice, chapters land at ~40% of target word count. They read as strong summaries, not realized scenes. The Expand step adds the muscle: sensory texture, moment-to-moment scene work, extended dialogue, deeper interiority. It doesn't change the plot. It fills in what the draft sketched.

### Why Revision is iterative

Each revision pass targets one layer (structure, character, pacing, continuity, line quality, rhythm). But after significant rewrites like expansion, new issues appear -- consistency drift, reintroduced crutch words, continuity errors. Run at least two full cycles. The revision template includes an AI-specific prose pattern checklist for common failure modes.

---

## Quick Start

```bash
git clone <novel-kit-repo-url>
cd novel-kit

# Open Claude Code in this directory, then:
/novel.new
# Follow the pipeline — each command picks up where the last left off
```

Each command reads artifacts from previous steps, so the AI always has full context. When working on multiple novels, commands check `novels/<slug>/novel.md` and ask which novel to work on.

---

## Project Structure

```
novel-kit/
├── novels/                         # gitignored — your novels live here
│   └── my-thriller/
│       ├── novel.md                # Pipeline status and word count
│       ├── story/                  # Design artifacts (steps 1-6)
│       │   ├── premise.md
│       │   ├── vision.md
│       │   ├── characters/
│       │   ├── world.md
│       │   ├── outline.md
│       │   ├── scenes.md
│       │   ├── continuity.md       # Living fact-tracker, initialized step 6
│       │   └── revision-notes.md
│       ├── manuscript/             # Prose (steps 7-8)
│       └── research/               # Reference material
├── templates/
│   ├── commands/                   # AI command files (one per step)
│   └── *.md                        # Artifact templates
└── docs/
    └── story-driven-development.md # Methodology reference
```

### Templates

| Template | Based On |
|---|---|
| `premise-template.md` | Save the Cat logline, Snowflake Method |
| `vision-template.md` | spec-kit Constitution, genre convention analysis |
| `character-template.md` | Wound-based arcs, Enneagram, avoidance patterns |
| `world-template.md` | Sanderson's iceberg principle, sensory-first design |
| `outline-template.md` | Three-act structure, Save the Cat, Story Grid |
| `scenes-template.md` | Scene-sequel pattern, yes-but/no-and outcomes |
| `continuity-template.md` | Living document tracking facts established in prose |
| `revision-template.md` | Multi-pass developmental editing, AI prose pattern checklist |

---

## Mapping to spec-kit

| spec-kit | novel-kit | Rationale |
|---|---|---|
| Constitution | Creative Vision | Governing principles and constraints |
| Specification | Premise & Synopsis | The "what and why" of the thing being built |
| Clarify | Interrogate | Pressure-testing assumptions |
| Plan | Story Outline | Architectural design |
| Tasks | Scene Breakdown | Granular executable units |
| Implement | Draft + Expand | Producing the actual output |
| Checklist | Revision Passes | Quality validation |
| Analyze | Continuity Check | Cross-artifact consistency |

## Tested in Practice

This pipeline was refined by writing a complete 72,000-word novel through it -- from blank directory to EPUB. The process revealed the gaps that shaped the toolkit:

- **First drafts run short**: AI chapters came in at ~40% of target, leading to the Expand step
- **Parallel expansion drifts**: Multiple agents expanding independently introduced voice and continuity issues, leading to the AI-specific revision checklist
- **Continuity breaks compound**: Tracking details after drafting is too late, leading to the continuity bible initialized during scene design
- **Research is always needed**: Real-world grounding happened ad hoc at every stage, leading to the cross-cutting research command

Every template and command exists because its absence caused a specific problem during actual novel writing.

## Contributing

Early development. Contributions welcome:
- Genre-specific templates (romance, mystery, literary fiction)
- Alternative structural frameworks (Kishotenketsu, Dan Harmon's Story Circle)
- Writing tool integrations (Scrivener, Fountain)

## License

MIT

---

*Inspired by [spec-kit](https://github.com/github/spec-kit) and the idea that the best creative work comes from the intersection of structure and imagination.*
