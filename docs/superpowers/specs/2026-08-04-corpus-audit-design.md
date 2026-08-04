# Corpus Audit and Measurement Harness — Design

**Date:** 2026-08-04
**Status:** Approved design, ready for implementation planning

## Problem

novel-kit's instructions and templates have been refined by writing novels through them, but improvements are currently driven by impression rather than measurement. Four recurring complaints about pipeline output:

1. Prose reads as AI-generated
2. Small concepts, images, and explanations repeat
3. Minor logic and continuity errors
4. Tension drops in places

None of these are currently attributable to a specific pipeline step, so fixes are guesswork and there is no way to prove a template change helped.

## Why the corpus, not a comparison benchmark

The original idea was to reverse-engineer premises from published ebooks, write those novels through the pipeline, and compare. That comparison is worth building, but not first: errors compound down the pipeline, so an end-to-end comparison tells you the result is worse without telling you which instruction caused it.

The existing corpus is a stronger starting point. `novels/` holds eight directories: seven substantially complete novels — roughly 350,000 words, each with `outline.md`, `scenes.md`, `continuity.md`, and most with `revision-notes.md` — plus `zirkus`, a single-chapter abandoned start. "All seven" throughout this document means the complete novels; `zirkus` is always named explicitly where it is used.

Preliminary evidence for the approach: the opening paragraphs of four novels spanning Regency romance, science fiction, suburban comedy, and a culinary story all execute the same move — wry ironic distance on a mundane setting, an em-dash parenthetical, a three-item inventory — and three of four use a *not X but Y* construction within the first lines. Each book reads well alone. Together they read as one author. That finding is invisible without cross-novel comparison.

## The corpus is stratified by pipeline generation

This is the central constraint on interpretation. Novel directory mtimes mapped against commit dates show the corpus spans four pipeline versions:

| Gen | Pipeline from | Novels | Words |
|---|---|---|---|
| 1 | Initial commit (2026-03-02) | `the letters` | 56K |
| 2 | 10-step expansion (2026-03-04) | `untitled-scifi`, `untitled-literary` | 72K, 58K |
| 3 | Word-count calibration (2026-03-05) | `regency-easter`, `salt-and-sugar`, `thaw-line` | 30K, 49K, 47K |
| 4 | Autonomous refactor (2026-03-15) | `love-love`, `zirkus` | 36K, 4K (abandoned) |

**The current pipeline has produced exactly one complete novel** (`love-love`, 20 chapters, 36K words). Generation 4 introduced `style-guide.md`, `motifs.md`, and the `evaluate`/`select`/`realize`/`reconcile` commands, which is why those artifacts are absent from the six older novels. `the letters` predates `novel.md` entirely.

The naive recurrence rule — "present in all seven, therefore systemic" — is therefore wrong. A pattern in all seven may already be fixed; a pattern only in `love-love` may be the newest and most important. Two consequences shape the design:

**The corpus is a time series, not a sample.** This is more useful than a flat aggregate: it retroactively validates past template changes. Did the 2026-03-04 change to `draft.md` actually fix thin chapters? Compare Gen 2 against Gen 3 metrics.

**Cross-generation recurrence is depth of evidence, not confounding.** A pattern surviving four pipeline versions is a defect no template revision has touched. The voice-homogeneity observation above happens to span Gen 1, 2, 3, and 4 — which makes it stronger, not weaker.

### Finding liveness

Every finding carries a liveness label, and only LIVE findings become template changes:

- **LIVE** — also present in `love-love`; the current pipeline still produces it
- **LEGACY** — present in Gen 1–3, absent from `love-love`; likely already fixed, leave alone
- **UNKNOWN** — `love-love` at 36K is too short or too genre-specific to judge

The high UNKNOWN rate this will produce is itself the most important structural finding: one novel is insufficient evidence about the current pipeline. Judging it properly requires freshly generated material — which is the strongest argument for Track 2, and a better rationale for it than the original one.

## Scope

This spec covers **Track 1** only: audit the existing corpus and build the measurement harness.

**Track 2** — generate fresh material under the current pipeline and compare against published novels — gets its own spec once Track 1 shows what remains unanswered. Track 1 produces the detectors Track 2 needs anyway, and Track 2 gains a second role beyond finding failures: calibrating target *bands* (how often does published prose actually use these constructions?) and supplying the Gen 4 evidence this corpus lacks.

The ebook set will be well-known bestsellers and classics. Accepted consequence: their plots and phrasing are likely in the model's training data, which makes the pipeline look better than it is. This is acceptable because the goal is finding failures, not certifying quality — any weakness that survives contamination is real. It does mean Track 2 cannot support "the pipeline performs at X% of published quality" claims.

## Architecture

```
bench/
├── lint/
│   ├── prose_lint.py       # one novel in, JSON out
│   ├── aggregate.py        # all JSONs in, per-generation + liveness ranking out
│   └── tests/              # fixtures with known expected counts
├── corpus.json             # gitignored — slug → generation → commit manifest
├── reports/                # gitignored — contains prose excerpts
├── baseline.json           # gitignored — pre-change metric snapshot
└── README.md
```

Python 3, standard library only — no dependency setup for anyone cloning the toolkit.

Scripts belong in the repo: they are part of the toolkit and useful to anyone writing with it. Reports, baseline, and the corpus manifest do not: they name and quote private manuscripts, same reasoning that puts `novels/` in `.gitignore`. Add `bench/reports/`, `bench/baseline.json`, and `bench/corpus.json` to `.gitignore`.

`corpus.json` is hand-authored from the generation table above rather than derived from mtimes at runtime — mtimes are fragile and a re-run must produce the same stratification.

**The deliverable is `bench/findings.md`**, not the reports. Each entry:

| Field | Content |
|---|---|
| Symptom | What is wrong, in reader-facing terms |
| Evidence | Numbers from the lint, plus two or three actual passages |
| Spread | Which generations and how many novels |
| Liveness | LIVE / LEGACY / UNKNOWN |
| Attribution | Which step and which template/command produced it |
| Proposed fix | Concrete edit to that file |

Without attribution the audit produces observations instead of fixes.

## Components

### `prose_lint.py`

One novel directory in, JSON out. Every detector is a named function with its own test, so a broken detector cannot silently produce false findings. All rates normalized per 1000 words — 30K and 72K novels are otherwise not comparable.

**Targeting complaint 1 (AI prose):**

- `punct_tics` — em-dash, semicolon, ellipsis, parenthetical per 1000 words
- `constructions` — regex family: *not X but Y*, *less like X and more like Y*, *something between X and Y*, *wasn't X. It was Y.*, *the kind of X that*, *with the precision of*, three-item inventories
- `sentence_shape` — mean, standard deviation, histogram, share in the 12–25-word band. AI prose clusters mid-length; variance is the signal, not length
- `openers` — participial openers (`-ing,`), *But/And* openers, share of subject-verb openings
- `filter_verbs` — *felt, seemed, noticed, realized, watched as, could tell, found himself*
- `dialogue` — share of words in dialogue, tag variety, tag-to-action-beat ratio

**Targeting complaint 2 (repetition):**

- `repeated_ngrams` — 4–8-word phrases occurring twice or more, reported separately for within-chapter and across-chapter. Requires a stoplist: bare frequency over 350K words surfaces ordinary English ("for the first time", "at the same time"). Rule: an n-gram counts only if it contains at least one content word outside the 2000 most common English words, or is at least 6 tokens long. The stoplist ships as a fixture so results stay reproducible.
- `lexical_recurrence` — uncommon content words with unusually wide chapter spread; catches recurring images and props
- `motif_overuse` — cross-check declared motifs against their occurrence count and chapter spread. Reports raw counts and spread only, no verdict — thresholds are uncalibrated until Track 2. **Runs on `love-love` and `zirkus` only**, since `motifs.md` does not exist in Gen 1–3; it is a single-novel diagnostic, not a systemic measure.

**Targeting complaint 4 (tension), as mechanical proxies:**

- `chapter_shape` — word count per chapter, dialogue-share curve, scene-break frequency. Target comparison requires `novel.md`; skipped for `the letters`, which has none.

### `aggregate.py`

Merges all per-novel JSON using `corpus.json` for stratification, and answers three questions:

1. Which detectors fire across multiple generations? (depth of evidence)
2. Which fire in `love-love`? (liveness)
3. Where do metrics shift between adjacent generations? (retroactive validation of past template changes)

`zirkus` is excluded from all aggregates — one chapter carries no statistics. It remains available as a Gen 4 spot-check.

### LLM reading passes

Four passes, each with a fixed output schema so results are comparable across novels. Run as parallel subagents.

1. **`voice-homogeneity`** — the first 800 words of all seven novels side by side. Seven authors or one? Which specific habits are shared? 5,600 words of input; the strongest signal per token in the project. Because it spans all four generations, it also shows whether voice convergence has worsened or improved over time.
2. **`concept-repetition`** — per novel: the same idea, explanation, or image restated in different words, with chapter references. Scripts find identical phrases, not identical thoughts.
3. **`continuity-diff`** — `continuity.md` plus all chapters: contradictions, logic gaps, timeline errors.
4. **`tension-curve`** — each chapter scored 1–5 on pressure, stakes, and open questions, plotted against the pacing curve in `outline.md`. Where they diverge, `draft` is ignoring its own plan.

**Coverage:** mechanical detectors and pass 1 across all seven novels. Passes 2–4 run on one novel per generation, which is what the time-series reading requires: `love-love` (Gen 4, mandatory — the only current-pipeline evidence), `salt-and-sugar` (Gen 3, 49K), `untitled-scifi` (Gen 2, 72K), `the letters` (Gen 1, 56K). Roughly 215K words of input across three passes. Any narrowing of this coverage must be stated in `findings.md` — silent truncation reads as full coverage.

## Data flow

```
manuscript/ + story/ ──→ prose_lint.py ──→ reports/<slug>.json ──┐
                                                                 │
                                          corpus.json ──→ aggregate.py ──→ reports/systemic.md
                                                                 │
LLM passes ─────────────────→ reports/<slug>-<pass>.md ──────────┤
                                                                 ▼
                                                  findings.md (symptom → evidence → spread
                                                            → liveness → attribution → fix)
                                                                 ▼
                                                  template/command edits (LIVE findings only)
                                                                 ▼
                                                  regression check vs. baseline.json
```

## Validity guards

Four ways this audit can produce nonsense. Each needs a guard, or we build a measuring device that points the wrong way.

**1. A metric is not quality.** A low em-dash rate is not good prose. Guard: no mechanical finding becomes a fix until the flagged passages have been read. The script points; reading judges.

**2. Overfitting to the linter.** The real danger. Tuning templates to satisfy metrics produces prose that games the metrics — published books also use em-dashes and repeat images. Two guards:

- Until Track 2 calibrates target bands, only extreme outliers count as findings. Never "less is better."
- Fixes go into *instructions*, not prohibition lists. A template that says "no em-dashes" just produces a different tic. Voice homogeneity most likely does not come from em-dashes being permitted; it comes from `vision.md` and `style-guide.md` *describing* a voice while nothing in the pipeline forces that voice to *differ* from the last novel's — no step ever asks "how does this book sound different?" That is the level fixes must target.

**3. Generation skew.** Attributing a Gen 1 defect to a current template wastes effort and can undo a fix that worked. Guard: the liveness labels above, and no LEGACY finding produces an edit.

**4. The author is also the judge.** On the prose passes the model evaluates its own habits, which is exactly where it is blind. Guard: subagents are not told the texts are AI-generated or that we are looking for AI tells. The brief is "seven novel extracts — same authorship? On what evidence?" not "find the AI patterns." Otherwise they find what they were pointed at and we mistake suggestion for finding.

## Testing

The scripts are the measuring instrument; a wrong detector produces false findings that become template changes and do real damage. `bench/lint/tests/` holds small fixtures with known expected counts, a handful of assertions per detector, written before any detector runs across 350K words.

## Regression loop

This is what makes the harness worth more than a one-off audit.

`bench/baseline.json` freezes today's metrics. After a template change, a fixed test case: `love-love` keeps its `story/` artifacts unchanged, one mid-book chapter is re-drafted under the new instructions, linted, and compared against the baseline chapter. Same input, different instruction, measurable difference. "Did it help" becomes a measurement rather than a hope.

`love-love` is the test case rather than a longer novel because it is the only one whose `story/` artifacts match the current pipeline's expected inputs — `style-guide.md` and `motifs.md` exist there, and re-drafting a Gen 3 novel would exercise the wrong contract.

## Out of scope

- Track 2, the fresh-run and published-ebook benchmark — separate spec
- Actually rewriting templates and commands — follow-up plan, driven by `findings.md`
- Re-running a complete novel through the pipeline
- Non-English detectors; the corpus is entirely English

## Success criteria

1. `prose_lint.py` and `aggregate.py` run over all seven novels with passing detector tests
2. `reports/systemic.md` ranks patterns by generational spread and reports metric shifts between adjacent generations
3. All four LLM passes complete at the stated coverage
4. `findings.md` contains attributed findings, each labeled LIVE / LEGACY / UNKNOWN and naming the file to change
5. `baseline.json` exists, so the next template change can be measured rather than argued
