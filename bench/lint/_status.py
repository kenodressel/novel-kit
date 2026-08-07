"""Shared reader for novel.md, tolerant of how a run actually formats it.

The template specifies YAML frontmatter (`target_word_count: 60000`). Runs have
been observed to write markdown bullets instead (`- **Target word count**: 65,000`),
which parsed as nothing, so the scale checks in specs.py and wordcount.py silently
skipped and reported PASS on a manuscript at 18% of target.

So: accept both forms, and report which one was found. A tolerant parser stops the
check from being skipped; the format warning stops the deviation from being
permanent, because downstream tooling expects the frontmatter.
"""
import pathlib
import re

FIELDS = {
    "target": ("target_word_count", r"target\s*word\s*count"),
    "current": ("current_word_count", r"current\s*word\s*count"),
}

# ---------------------------------------------------------------------------
# The absolute anchor.
#
# Every other check in bench/lint is relative to a number the run itself writes:
# estimates against target, actual against estimates, actual against target. A run
# that sets all three to 7,200 is perfectly self-consistent and passes everything.
# Observed: 12 chapters, exactly 3 beats each (the declared minimum), 201 words per
# beat (inside the declared band), target_word_count 7,200, every linter green -- a
# 7,066-word text filed as a "Regency Heist Romance".
#
# So one number has to come from outside the run. Publishing length conventions are
# that number: they are not ours to set, and a form has to be *named* to be claimed.
# ---------------------------------------------------------------------------

# The author's standing instruction, 2026-08-07: nothing under 40,000 words.
# This is the anchor. It is not derived from any file the pipeline writes, and a run
# cannot satisfy it by renumbering -- only by writing a novel.
MIN_PROJECT_WORDS = 40_000

FORM_BANDS = {
    "short story": (0, 7_500),
    "novelette": (7_500, 17_500),
    "novella": (17_500, 40_000),
    "novel": (40_000, 250_000),
}

# Where the trade expects a *novel* in that genre to sit. Advisory, not a failure.
GENRE_NOVEL_NORMS = {
    "romantasy": (90_000, 150_000),
    "fantasy": (90_000, 150_000),
    "science fiction": (80_000, 120_000),
    "romance": (70_000, 100_000),
    "thriller": (70_000, 100_000),
    "mystery": (60_000, 90_000),
    "literary": (70_000, 100_000),
    "young adult": (50_000, 80_000),
}


def read_form(status: pathlib.Path):
    """Declared form, normalised. None if absent."""
    if not status.exists():
        return None
    text = status.read_text(encoding="utf-8")
    m = re.search(r"(?im)^[-*\s]*\**\s*form\**\s*[:\-]\s*\**\s*\"?([A-Za-z \-]+)", text)
    if not m:
        return None
    raw = m.group(1).strip().lower().replace("-", " ")
    for key in FORM_BANDS:
        if key in raw or raw in key:
            return key
    return raw or None


def read_genre(status: pathlib.Path):
    if not status.exists():
        return None
    m = re.search(r"(?im)^[-*\s]*\**\s*genre\**\s*[:\-]\s*\**\s*\"?([^\"\n]+)",
                  status.read_text(encoding="utf-8"))
    return m.group(1).strip().lower() if m else None


def genre_norm(genre: str | None):
    """(low, high) for a novel in this genre, or None."""
    if not genre:
        return None
    for key, band in GENRE_NOVEL_NORMS.items():
        if key in genre:
            return band
    return None


def check_scale(status: pathlib.Path, target, actual=None):
    """Absolute checks that no self-consistent run can satisfy by renumbering.

    Returns (fails, notes).
    """
    fails, notes = [], []
    genre = read_genre(status)

    # The hard floor. Checked against the target and against the manuscript, because
    # a run can lower the target and a run can write short, and both have happened.
    if target is not None and target < MIN_PROJECT_WORDS:
        fails.append(
            f"target_word_count is {target:,}, below the project floor of "
            f"{MIN_PROJECT_WORDS:,}. Nothing under {MIN_PROJECT_WORDS // 1000}k gets "
            "written here. This is not negotiable by adjusting the target — the target "
            "is what has to move.")
    if actual is not None and actual < MIN_PROJECT_WORDS:
        fails.append(
            f"the manuscript is {actual:,} words, below the project floor of "
            f"{MIN_PROJECT_WORDS:,}. Do not reclassify it as a novella, a novelette or a "
            "short story to make this pass. The remaining work is "
            f"{MIN_PROJECT_WORDS - actual:,} words of story, and it belongs to "
            "/novel.scenes and /novel.realize.")

    form = read_form(status)
    if form and form in FORM_BANDS and FORM_BANDS[form][1] <= MIN_PROJECT_WORDS:
        fails.append(f"`form: {form}` caps this project at {FORM_BANDS[form][1]:,} words, "
                     f"under the {MIN_PROJECT_WORDS:,} floor. Remove it or set `form: novel`.")

    band = genre_norm(genre)
    if band and target and MIN_PROJECT_WORDS <= target < band[0]:
        notes.append(f"target {target:,} clears the floor but sits below the "
                     f"{band[0]:,}-{band[1]:,} range the trade expects for \"{genre}\". "
                     "Legal, and it will read as under-length to an editor in that category.")
    return fails, notes


def threshold_clustering(values, floor, label):
    """Flag a metric sitting exactly on its own minimum across the board.

    A distribution is evidence of intent. Twelve chapters that each contain exactly
    the minimum permitted number of beats is not a book shaped by its story; it is a
    book shaped by this linter.
    """
    vals = [v for v in values if v is not None]
    if len(vals) < 5:
        return None
    at_floor = sum(1 for v in vals if v == floor)
    if at_floor / len(vals) >= 0.9:
        return (f"{at_floor} of {len(vals)} blocks sit exactly on the minimum "
                f"{label} ({floor}). A threshold is a floor, not a specification. "
                "When every chapter lands precisely on it, the number was chosen to "
                "satisfy this check rather than to fit a scene.")
    return None


def read(status: pathlib.Path, key: str):
    """Return (value, source) where source is 'frontmatter', 'prose', or None."""
    if not status.exists():
        return None, None
    text = status.read_text(encoding="utf-8")
    yaml_key, prose_key = FIELDS[key]

    m = re.search(rf"(?m)^{yaml_key}:\s*\"?([\d,]+)", text)
    if m:
        return int(m.group(1).replace(",", "")), "frontmatter"

    # `- **Target word count**: 65,000` and variants, anywhere in the document
    m = re.search(rf"(?im)^[-*\s]*\**\s*{prose_key}\**\s*[:\-]\s*\**\s*([\d,]+)", text)
    if m:
        return int(m.group(1).replace(",", "")), "prose"

    return None, None


def format_warning(status: pathlib.Path) -> str | None:
    """Non-fatal note if novel.md lacks YAML frontmatter entirely."""
    if not status.exists():
        return f"{status} does not exist"
    head = status.read_text(encoding="utf-8").lstrip()
    if not head.startswith("---"):
        return (f"{status} has no YAML frontmatter. The template specifies it and other "
                "steps read it; prose bullets happen to be parsed here but should be "
                "converted, or the next tool that looks for a field will not find one.")
    return None
