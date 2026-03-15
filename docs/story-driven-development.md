# Story-Driven Development

A creative methodology where structured story design constrains long-form prose generation, while evaluation, selection, reconciliation, and research keep the output coherent and worth reading.

## The Problem

Most novels fail in one of two ways:

1. **The Wandering Draft**: The author starts writing without a plan, discovers the story through drafting, writes themselves into corners, and abandons the project (or produces a structurally broken manuscript that requires a rewrite from scratch).

2. **The Lifeless Outline**: The author outlines meticulously but produces flat, mechanical prose because the plan was all plot and no soul -- no character psychology, no thematic depth, no voice.

Story-Driven Development solves both problems by making the story design **comprehensive** (covering structure, character, theme, voice, and world), **iterative** (starting simple and deepening layer by layer), and **evaluated** (weak options do not automatically propagate).

## The Methodology

### Design Is Not Outlining

Traditional outlining focuses on plot: what happens, then what happens next. StDD designs the *story*, which includes:

- **Why** events happen (character psychology, thematic necessity)
- **How** they feel (emotional arcs, tone, sensory reality)
- **What they mean** (thematic argument, symbolic resonance)
- **Who** experiences them (POV strategy, voice, internal life)

An outline tells you the plot. A story design tells you the *novel*.

### Iterative Deepening

Borrowed from the Snowflake Method: start with the simplest possible version of the story (one sentence) and expand it through structured stages. At each stage, the story gets more detailed, but every detail traces back to the core premise.

```
One sentence   -->  One paragraph  -->  One page      -->  Full character sheets
(Logline)          (Pitch)            (Synopsis)          (Psychology, arcs, voice)
                                                               |
Full scenes    <--  Chapter outline <-- Act structure  <-- World building
(60-80 specs)      (Chapter arcs)     (Turning points)    (Systems, locations)
    |
First draft    -->  Realization     -->  Revision passes -->  Polish & submit
(candidate set)    (lived scenes)       (iterative)          (beta, query, blurb)
```

### Research And Validation Are Ongoing

Research is not a pipeline step — it's a cross-cutting activity that happens alongside any step. During Premise, you research the world your story inhabits. During World, you research how things actually work. During Draft and Realization, you research specific details for scenes. Save findings to `research/` and let them inform the story without overwhelming it. A single vivid, accurate detail is worth more than a paragraph of general knowledge.

Reality-adjacent fiction should maintain a fact-check log. Not every story needs this. But if the manuscript depends on real places, institutions, laws, medicine, technology, or cultural specifics, unsupported claims should fail evaluation until they are either verified or marked as deliberate liberties.

### Characters Are Architecture

In StDD, characters are not designed after the plot. They are designed *before* the plot, because the best plots emerge from character. When you know what a character wants, fears, and believes, the plot writes itself: put them in situations that test their misbelief, and watch them make decisions that create consequences.

### Every Artifact Has a Job

Each document in the story design exists to prevent a specific category of failure:

| Artifact | Prevents |
|---|---|
| Premise | Stories that can't sustain a full novel |
| Vision | Tonal inconsistency, scope creep, identity drift |
| Characters | Flat characters, unmotivated actions, indistinct voices |
| World | Setting inconsistencies, world-breaking plot conveniences |
| Outline | Structural collapse, saggy middles, unsatisfying climaxes |
| Scenes | Purposeless scenes, pacing problems, missed setups/payoffs |
| Continuity | Contradictions, timeline errors, description drift across chapters |
| Revision checklist | Blind spots, missed layers, superficial editing |

### AI as Collaborator, Generator, And Judge

In StDD, AI serves three roles:

1. **Interrogator**: It pressure-tests your creative decisions, finding holes you can't see because you're too close to the work.
2. **Generator**: It produces draft material that adheres to your specifications, which you then rewrite, refine, or redirect.
3. **Editor**: It analyzes your manuscript against your own design documents, catching deviations and inconsistencies.
4. **Evaluator**: It scores artifacts and chapters against explicit quality gates.
5. **Selector**: It chooses among candidates instead of pretending the first coherent output is best.

The author remains the creative authority. The AI is a highly capable assistant that never forgets the story bible, never gets tired of checking continuity, and can search a wider option space than a one-shot drafting workflow.

## Principles

1. **Generate options before committing**: Search beats one-shot generation.
2. **Characters drive plot**: Build people first, then put them in situations.
3. **World serves story**: Every world detail must create conflict, reveal character, or set atmosphere.
4. **Iterative deepening**: One sentence becomes one paragraph becomes one page becomes sixty scenes.
5. **Interrogate and evaluate relentlessly**: Every assumption gets challenged before it becomes prose, and weak outputs fail forward progress.
6. **Drafting is search, not just implementation**: The first draft should explore multiple options at key moments.
7. **Realization is a distinct step**: First drafts — especially AI-assisted ones — often capture events without fully dramatizing them. Realization turns thin chapters into lived scenes and may surface better canon through controlled reconciliation.
8. **Revision is layered and iterative**: Each pass targets one dimension. Never try to fix everything at once. Run at least two full revision cycles when significant rewrites have occurred between them.
9. **Research protects immersion**: Reality-adjacent claims should be verified or deliberately marked as liberties.
10. **Structure liberates creativity**: Knowing where you're going frees you to focus on how you get there.

### Auto Mode

When the author requests "full auto" or similar, proceed through remaining pipeline steps using opinionated defaults:

- **Structure**: Three-act (or the framework already chosen in the outline)
- **POV**: Whatever was established in the vision document
- **Drafting**: Full draft mode, all chapters in sequence
- **Branching**: Generate alternatives for opening, midpoint, climax, and ending
- **Realization**: Realize all chapters that score below threshold or read as summarized
- **Revision**: Two full passes (structural + line-level, then continuity + boredom/genericity cleanup)
- **Polish**: Generate beta questionnaire, query letter, blurb, synopsis

Even in auto mode, always validate word counts, continuity, reader-facing quality, and reality-adjacent claims. Auto mode is about removing decision fatigue, not removing quality checks.
