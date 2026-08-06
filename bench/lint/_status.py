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
