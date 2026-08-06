# Style Guide

> A style guide made of adjectives cannot be checked, and an uncheckable rule does not survive contact with drafting. Every field below is either a number or a named mechanism.
>
> Fill the measured fields by analysing 3-5 comparable novels you want this book to read like. A number without a source is a guess. Record the source.

## Prose Fingerprint (measured)

**Comps analysed**: <!-- title + author for each, and which sections you measured -->

Measure your comps with `python3 bench/lint/fingerprint.py <file-or-novel-dir> …`. It reports every row below. Set each target **inside** the observed comp range, not at the mean of it — the mean of your influences is how a book comes to read like the average of them.

| Metric | This book's target | Comp range observed | Reference: 6 published novels |
|---|---|---|---|
| Mean sentence length (words) | | | 12.3 – 14.7 |
| Median sentence length | | | **9 – 13** |
| Share of sentences 1-3 words | | | **5 – 18%** |
| Share of sentences 4-11 words | | | 31 – 46% |
| Share of sentences 12-25 words | | | **31 – 42%** |
| Share of sentences over 25 words | | | 8 – 14% |
| Longest permitted sentence | | | 65 – 86 |
| Share of paragraphs 8 words or fewer | | | 12 – 24% |
| Share of words inside dialogue | | | 10 – 18% |
| `said` as a share of dialogue attributions | | | 60 – 66% |
| Similes per 1,000 words | | | 2.8 – 4.6 |

Variance is the signal, not the mean. Two books with the same mean sentence length read nothing alike if one clusters at the mean and the other swings between three words and forty.

### The mid-band is the row that separates

The bolded rows are the only sentence-shape metrics that discriminated cleanly when a 349,000-word corpus of unedited drafts was measured against 749,000 words of published fiction:

| | Share 12-25 words | Share 1-3 words | Median |
|---|---|---|---|
| 8 unedited drafts | 14.3 – **22.5%** | **19.8** – 28.3% | 5 – 7 |
| 6 published novels | **30.9** – 41.6% | 5.3 – **17.6%** | 9 – 13 |

Zero overlap. The strongest draft sits below the weakest published book on the mid-band, and no draft reaches a median of 8.

The failure is not "sentences too short". It is **a hollow middle**: fragments alternating with long sentences, and almost nothing in the 12-to-25-word range where published prose spends a third to two-fifths of its time. Three habits push the same way and compound — clipped dialogue, fragments stacked as single-line paragraphs at every emotional spike, and a low paragraph-length floor. Any one of them is fine. All three together evacuate the middle.

**Set a mid-band floor and check it per chapter. Below 25% is a finding.**

### Metrics that do NOT discriminate — do not treat these as tells

Measured and rejected, recorded here so nobody re-derives them:

- **Em-dashes.** Drafts ran a median of 138 per 10,000 words against a published median of 32 — but two Sarah J. Maas novels sit at 129.5 and 136.3, inside the draft range. A rule against em-dashes would have diagnosed a bestselling author as machine-written.
- **Semicolons, colons, ellipses, parentheses.** Published usage spans two orders of magnitude between authors. Personal habits, not quality markers.

The general rule: a metric becomes a constraint only after it has been shown to separate published prose from unedited prose. Counting something is not the same as it mattering.

**If a scene cannot hit a target**, that is information, not failure. The drafter reports the miss with its number and its reason (see the compliance report in `draft.md`). A scene with one speaking character cannot reach a 20% dialogue share; say so rather than inventing conversation.

## Narrative Defaults

- **POV distance**: <!-- close / medium / distant -->
- **Person and tense**: <!-- must match the decision recorded in vision.md, including its stated reason -->
- **POV rule**: <!-- how many POV characters, and whether the narration may ever access a non-POV interior. If the answer is no, say no. -->
- **Rhythm rules**: <!-- where fragments are permitted, where they are forbidden -->

## How characterisation is delivered

This single field decides whether the prose has a voice. Name the **mechanism**, not the aspiration:

- <!-- e.g. assigned physical tic; diction and register; what the character notices and refuses to notice; behaviour under pressure; what they will not say -->

**Not permitted as the primary mechanism — the characterising appositive.** The construction `with the [abstract noun] of [someone] who [does X]` — *with the patience of a man who had waited before*, *with the appraising eye of a woman who* — is capped at **1 per 10,000 words**.

Measured basis: 749,000 words of published fiction across five authors contain **zero** instances of this construction used to describe a person. One unedited 349,000-word corpus contains **218**.

A high count is a symptom, not the disease. The prose reaches for the appositive when the narrator has no idiom of its own, so the simile has to certify the character instead. If the count is high, fix the idiom — do not find and replace, or a substitute tic will take its place.

## Voice Priorities

- **What the prose notices**: <!-- the kinds of detail this narration privileges -->
- **What the prose refuses**: <!-- abstraction, ornamental metaphor, explanation, etc. -->
- **Metaphor domains**: <!-- the image fields the narration draws from -->
- **Metaphor budget**: <!-- how many times a given domain may be used before it stops signifying. A domain used on every feeling is no longer an emphasis. -->

## Dialogue Rules

- **Compression level**: <!-- terse / naturalistic / heightened -->
- **Subtext behavior**: <!-- direct, evasive, status-driven, emotionally masked -->
- **Character voice deltas**: <!-- one line per major character, and it must be a *mechanism*, not an adjective: sentence length, vocabulary register, what they refuse to answer, a syntactic habit -->

**Single-engine test**: write out one line from each major character with the attributions removed. If a reader could not assign them, the characters share one voice and the deltas above are decorative. Common failure: every character speaks in flat-statement-plus-witty-reversal, so the cast is one narrator wearing several names.

## Prohibitions (countable)

- **No paragraph or scene may close by stating its own significance.** If the closing lines name the character's theme, wound, or competence out loud, the scene did not do the work and the gloss is covering for it.
- **No POV break to deliver information.** If the reader needs a fact the POV character cannot have, restructure the scene. Do not flash forward, do not enter a second interior, do not address the reader in the second person. This is the most common way a scene admits it failed.
- **Banned crutch phrases**:
  - <!-- phrase -->
- **Repetition budget**: no distinctive phrase, image, or number may recur more than <!-- N --> times in the manuscript. Set N deliberately. Measured failures in unedited drafts: one phrase 12 times in 5,500 words; a whole closing sentence duplicated near-verbatim 150 lines apart.
- **Thesis budget**: each idea about a character gets **one** statement. If it has been dramatised in a scene, the narrator's later summary of it is deleted — the summary is always the weaker version.

## Reader Effect

- **What a strong page feels like**: <!-- sensory/tonal target -->
- **What a weak page feels like**: <!-- warning signs -->
