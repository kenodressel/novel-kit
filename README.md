# novel-kit

Design the story first. Generate it under control. AI assists throughout.

> **TL;DR**: A 10-step autonomous novel generation system that takes a book from one-sentence idea to polished manuscript. It generates multiple candidates, evaluates them, selects the strongest path, drafts scene by scene, realizes weak chapters into lived scenes, revises aggressively, and runs research/fact-checking whenever the fiction touches reality. Your writing stays private (`novels/` is gitignored), the toolkit is shareable.
>
> ```
> /novel.new → /novel.premise → /novel.vision → /novel.characters → /novel.world →
> /novel.outline → /novel.scenes → /novel.draft → /novel.realize → /novel.revise → /novel.polish
> ```

---

## Philosophy

Inspired by [spec-kit](https://github.com/github/spec-kit), which inverted software development by making specifications the primary artifact. **novel-kit** applies that logic to fiction, but adapts it for long-form AI generation: the *story design* constrains the prose, while evaluation, selection, research, and reconciliation keep the system from drifting or going generic.

1. **Generate options before committing** -- Key stages should produce multiple candidates. Search beats one-shot generation.
2. **Interrogate and evaluate relentlessly** -- Every assumption gets pressure-tested, then scored against reader-facing criteria.
3. **Preserve emergence, don't just suppress drift** -- If the manuscript finds a better truth, update canon deliberately.
4. **Reality-adjacent fiction requires research** -- Real places, procedures, institutions, and cultures should be researched and fact-checked before they harden into prose.

## The Pipeline

10 steps from idea to manuscript. Each step produces an artifact that feeds the next.

| Step | Command | Produces | What happens |
|------|---------|----------|-------------|
| 1 | `/novel.premise` | `story/premise.md` | Logline, pitch, synopsis, core question |
| 2 | `/novel.vision` | `story/vision.md`, `story/style-guide.md`, `story/motifs.md` | Tone, themes, voice, POV, prose rules, motifs |
| 3 | `/novel.characters` | `story/characters/` | Psychology, arcs, relationships, voice fingerprints |
| 4 | `/novel.world` | `story/world.md` | Systems, locations, sensory palette |
| 5 | `/novel.outline` | `story/outline.md` | Structure, turning points, subplots, pacing curve, alternate paths |
| 6 | `/novel.scenes` | `story/scenes.md` | Scene-by-scene specs + continuity bible initialized |
| 7 | `/novel.draft` | `manuscript/` + chapter candidates | Prose, scene by scene, with branching for key chapters |
| 8 | `/novel.realize` | `manuscript/` (realized) | Turn summary-like draft material into lived scenes |
| 9 | `/novel.revise` | `story/revision-notes.md` | Multi-pass revision including boredom/genericity checks |
| 10 | `/novel.polish` | `story/submission/` | Beta questionnaire, query letter, blurb, synopsis |

Plus cross-cutting commands:
- `/novel.research` -- Gather reference material (optional, any stage)
- `/novel.interrogate` -- Pressure-test any artifact for gaps and contradictions
- `/novel.evaluate` -- Score artifacts and chapters against quality gates
- `/novel.select` -- Choose among candidates
- `/novel.reconcile` -- Propagate approved deviations back into canon

### Why Realize is its own step

First drafts -- especially AI-assisted ones -- often capture the right events without fully dramatizing them. In practice, chapters may land short, generic, or overly summarized. The Realize step fixes that, but it is not mere inflation. It may deepen conflict, sharpen voice, replace summary with enacted scene work, and promote better emergent material back into canon.

### Why Revision is iterative

Each revision pass targets one layer (structure, character, pacing, continuity, line quality, boredom/genericity, rhythm). But after significant rewrites like realization, new issues appear -- consistency drift, reintroduced crutch words, continuity errors, and padded chapters that still do not live. Run at least two full cycles. The revision template includes an AI-specific prose pattern checklist for common failure modes.

---

## Quick Start

```bash
git clone <novel-kit-repo-url>
cd novel-kit

# Open Claude Code in this directory, then:
/novel.new
# Follow the pipeline — each command picks up where the last left off
```

Each command reads artifacts from previous steps, so the AI always has full context. Strong autonomous runs also use `story/candidates/`, `story/evaluations/`, and `research/fact-check-log.md` to keep option search, quality gates, and reality validation visible.

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
│       │   ├── style-guide.md
│       │   ├── motifs.md
│       │   ├── characters/
│       │   ├── world.md
│       │   ├── outline.md
│       │   ├── scenes.md
│       │   ├── continuity.md       # Living fact-tracker, initialized step 6
│       │   ├── candidates/         # Alternate artifacts and chapter variants
│       │   ├── evaluations/        # Rubric-based quality gates
│       │   └── revision-notes.md
│       ├── manuscript/             # Prose (steps 7-8)
│       └── research/               # Reference material + fact-check log
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
| `style-guide-template.md` | Operational prose constraints for autonomous generation |
| `character-template.md` | Wound-based arcs, Enneagram, avoidance patterns |
| `world-template.md` | Sanderson's iceberg principle, sensory-first design |
| `outline-template.md` | Three-act structure, Save the Cat, Story Grid |
| `scenes-template.md` | Scene-sequel pattern, yes-but/no-and outcomes |
| `continuity-template.md` | Living document tracking facts established in prose |
| `motifs-template.md` | Symbolic recurrence tracking |
| `eval-rubric-template.md` | Reader-facing quality gates and pass/fail rules |
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
| Implement | Draft + Realize | Producing the actual output |
| Checklist | Evaluate + Revision Passes | Quality validation |
| Analyze | Continuity Check | Cross-artifact consistency |

## Tested in Practice

This pipeline was refined by writing a complete 72,000-word novel through it -- from blank directory to EPUB. The process revealed the gaps that shaped the toolkit:

- **First drafts run short or thin**: AI chapters came in at ~40% of target or read like competent summaries, leading to the Realize step
- **Parallel realization drifts**: Multiple agents strengthening chapters independently introduced voice and continuity issues, leading to stronger evaluation and revision gates
- **Continuity breaks compound**: Tracking details after drafting is too late, leading to the continuity bible initialized during scene design
- **Research is always needed**: Real-world grounding happened ad hoc at every stage, leading to the cross-cutting research command
- **One-shot generation is too weak**: Candidate search and selection are required for strong openings, turns, and endings

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
