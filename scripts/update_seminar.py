#!/usr/bin/env python3
"""Sync seminar.html with the Google Doc schedule.

Run from repo root: python scripts/update_seminar.py
"""

import re
import sys
from dataclasses import dataclass, field
from typing import Optional
from urllib.parse import unquote

import requests
from bs4 import BeautifulSoup

GOOGLE_DOC_URL = (
    "https://docs.google.com/document/u/0/d/"
    "19zVZyYweIRvh8Id7rTmP2dpRXY2lF1XOFNkAkQ7geWs/mobilebasic"
)
SEMINAR_HTML = "seminar.html"
PAST_EVENTS_MARKER = (
    '<p style="text-align: left;"><strong>'
    '<font size="6">Past Events:</font></strong></p>'
)

SPRING_MONTHS = {"january", "february", "march", "april", "may"}


@dataclass
class SeminarEntry:
    date: str
    name: str = ""
    affiliation: str = ""
    url: Optional[str] = None
    title: str = ""
    abstract_paras: list = field(default_factory=list)   # one string per paragraph


def is_tba(text: str) -> bool:
    t = text.strip().upper() if text else ""
    return not t or t in ("TBA", "WEBPAGE", "WEBSITE", "[WEBPAGE]", "[WEBSITE]")


def paras_have_content(paras: list) -> bool:
    return bool(paras) and any(not is_tba(p) for p in paras)


def names_match(a: str, b: str) -> bool:
    return a.strip().lower() == b.strip().lower()


def extract_real_url(href: str) -> str:
    """Unwrap Google redirect URLs."""
    if "google.com/url" in href:
        m = re.search(r"[?&]q=([^&]+)", href)
        if m:
            return unquote(m.group(1))
    return href


# ---------------------------------------------------------------------------
# Google Doc parsing
# ---------------------------------------------------------------------------

def fetch_google_doc() -> dict:
    """Fetch and parse the Google Doc. Return dict[date_str -> SeminarEntry]."""
    resp = requests.get(GOOGLE_DOC_URL, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "lxml")

    entries: dict = {}
    current: Optional[SeminarEntry] = None
    state: Optional[str] = None      # None | "abstract"
    seen_spring = False
    past_spring = False
    prev_week_num = 0

    # "Week N Month Day: ..."  — no dash between week number and date
    week_re = re.compile(r"Week\s+(\d+)\s+(\w+)\s+(\d+)\s*:\s*(.*)", re.IGNORECASE)

    for p in soup.find_all("p"):
        raw = p.get_text(separator=" ", strip=True)
        text = re.sub(r"\s+", " ", raw).strip()

        m = week_re.match(text)
        if m:
            week_num = int(m.group(1))
            month_word = m.group(2).lower()
            day = m.group(3)
            rest = m.group(4).strip()
            date_str = f"{m.group(2)} {day}"

            # Detect semester boundary
            if month_word in SPRING_MONTHS:
                if not seen_spring:
                    seen_spring = True
                    prev_week_num = week_num
                elif week_num < prev_week_num:
                    past_spring = True   # week numbers reset → older semester
                else:
                    prev_week_num = week_num
            else:
                if seen_spring:
                    past_spring = True

            if past_spring:
                if current is not None:
                    entries[current.date] = current
                    current = None
                break

            if current is not None:
                entries[current.date] = current

            current = SeminarEntry(date=date_str)
            state = None

            # Skip no-seminar weeks
            if re.match(r"no\s+seminar", rest, re.IGNORECASE):
                current = None
                continue

            # --- URL: first try <a> tag (may be Google-redirected), then bracket text ---
            url: Optional[str] = None
            a_tag = p.find("a")
            if a_tag:
                href = a_tag.get("href", "").strip()
                candidate = extract_real_url(href)
                if candidate.startswith("http"):
                    url = candidate

            bracket_m = re.search(r"\[([^\]]+)\]", rest)
            if bracket_m and url is None:
                bc = bracket_m.group(1).strip()
                if bc.startswith("http"):
                    url = bc

            # Strip bracket from rest before parsing name/affiliation
            rest_clean = re.sub(r"\s*\[[^\]]+\]", "", rest).strip()

            name_candidate = re.sub(r"\([^)]*\)", "", rest_clean).strip()
            if not name_candidate or is_tba(name_candidate):
                current = None
                continue

            # Affiliation in parens: "Name (Affiliation)"
            paren_m = re.search(r"\(([^)]+)\)", rest_clean)
            if paren_m:
                affil = paren_m.group(1).strip()
                name = rest_clean[: paren_m.start()].strip().rstrip(",").strip()
            else:
                parts = rest_clean.split(",", 1)
                name = parts[0].strip()
                affil = parts[1].strip().rstrip(".") if len(parts) > 1 else ""

            current.name = name
            current.affiliation = affil
            current.url = url
            continue

        if current is None:
            continue

        stripped = text.strip()
        if stripped.startswith("Title:"):
            val = stripped[len("Title:"):].strip()
            current.title = val if not is_tba(val) else ""
            state = None
        elif stripped.startswith("Abstract:"):
            val = stripped[len("Abstract:"):].strip()
            if not is_tba(val):
                current.abstract_paras = [val]
                state = "abstract"
            else:
                current.abstract_paras = []
                state = None
        elif state == "abstract":
            if stripped:
                # Non-empty line: continuation paragraph
                current.abstract_paras.append(stripped)
            # Empty line: skip — stay in abstract state so the next non-empty
            # line is still treated as a continuation paragraph
        elif stripped:
            state = None

    if current is not None:
        entries[current.date] = current

    return entries


# ---------------------------------------------------------------------------
# Abstract HTML helpers
# ---------------------------------------------------------------------------

def build_abstract_html(paras: list) -> str:
    """
    Render a list of paragraph strings as HTML.

    First paragraph:  <p><strong>Abstract: </strong>TEXT</p>
    Further paragraphs: <p>TEXT</p>
    """
    if not paras:
        return ""
    lines = [f"<p><strong>Abstract: </strong>{paras[0]}</p>"]
    for p in paras[1:]:
        lines.append(f"<p>{p}</p>")
    return "\n".join(lines)


def parse_existing_abstract_paras(block_html: str) -> list:
    """
    Given the raw HTML of an abstract block (first <p> + any continuation
    <p> tags), return the list of paragraph text strings.
    """
    para_re = re.compile(
        r"<p>(?:<strong>Abstract: </strong>)?(.*?)</p>", re.DOTALL
    )
    paras = []
    for pm in para_re.finditer(block_html):
        text = pm.group(1).strip()
        if text:
            paras.append(text)
    return paras


# Matches the first abstract <p> plus any immediately following plain <p> tags
# (i.e. without <strong> inside them — those belong to Speaker/Title/etc.)
ABS_BLOCK_RE = re.compile(
    r"<p><strong>Abstract: </strong>.*?</p>"   # first paragraph
    r"(?:\s*<p>(?!<strong>).*?</p>)*",          # zero or more continuation paras
    re.DOTALL,
)


# ---------------------------------------------------------------------------
# Speaker helpers
# ---------------------------------------------------------------------------

def parse_existing_speaker(chunk: str):
    """Return (name, url, affiliation) from the Speaker line, or ('', None, '')."""
    speaker_re = re.compile(
        r"<p><strong>Speaker:\s*(.*?)</strong></p>", re.DOTALL
    )
    m = speaker_re.search(chunk)
    if not m:
        return "", None, ""

    content = m.group(1).strip()
    if not content or is_tba(content):
        return "", None, ""

    a_m = re.search(
        r'<a\s+href="([^"]+)"[^>]*>([^<]+)</a>(.*)', content, re.DOTALL
    )
    if a_m:
        url = a_m.group(1).strip()
        name = a_m.group(2).strip()
        after = a_m.group(3).strip().lstrip(",").strip().rstrip(".")
        return name, url, after

    parts = content.rstrip(".").split(",", 1)
    name = parts[0].strip()
    affil = parts[1].strip() if len(parts) > 1 else ""
    return name, None, affil


def build_speaker_tag(
    entry: SeminarEntry,
    existing_url: Optional[str],
    existing_name: str,
    existing_affil: str,
) -> str:
    name = entry.name.strip()

    if entry.url:
        url: Optional[str] = entry.url
    elif existing_url and names_match(existing_name, name):
        url = existing_url
    else:
        url = None

    # Prefer existing (more complete) affiliation; fall back to GD
    affil = (
        existing_affil.strip().rstrip(".")
        if existing_affil
        else entry.affiliation.strip().rstrip(".")
    )

    if url and affil:
        inner = f'<a href="{url}" target="_blank" rel="noopener">{name}</a>, {affil}.'
    elif url:
        inner = f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'
    elif affil:
        inner = f"{name}, {affil}."
    else:
        inner = name

    return f"<p><strong>Speaker: {inner}</strong></p>"


# ---------------------------------------------------------------------------
# Per-week chunk update
# ---------------------------------------------------------------------------

def update_chunk(chunk: str, entry: SeminarEntry, date_str: str):
    """Apply GD updates to a single week's HTML chunk.

    Returns (new_chunk, list_of_change_descriptions).
    """
    changes = []

    # --- Title ---
    if entry.title and not is_tba(entry.title):
        title_re = re.compile(
            r"(<p><strong>Title: </strong>)(.*?)(</p>)", re.DOTALL
        )
        m = title_re.search(chunk)
        if m and m.group(2) != entry.title:
            old_val = m.group(2)
            chunk = title_re.sub(
                lambda x: x.group(1) + entry.title + x.group(3),
                chunk,
                count=1,
            )
            preview = entry.title[:60] + ("..." if len(entry.title) > 60 else "")
            changes.append(
                f"  [{date_str}] Title: '{old_val[:40]}' -> '{preview}'"
            )

    # --- Abstract (multi-paragraph) ---
    if paras_have_content(entry.abstract_paras):
        m = ABS_BLOCK_RE.search(chunk)
        if m:
            existing_paras = parse_existing_abstract_paras(m.group(0))
            new_paras = entry.abstract_paras
            if existing_paras != new_paras:
                new_html = build_abstract_html(new_paras)
                chunk = chunk[: m.start()] + new_html + chunk[m.end():]
                changes.append(f"  [{date_str}] Abstract: updated")

    # --- Speaker ---
    if entry.name and not is_tba(entry.name):
        existing_name, existing_url, existing_affil = parse_existing_speaker(chunk)
        new_speaker_tag = build_speaker_tag(
            entry, existing_url, existing_name, existing_affil
        )
        speaker_re = re.compile(
            r"<p><strong>Speaker:\s*.*?</strong></p>", re.DOTALL
        )
        sm = speaker_re.search(chunk)
        if sm and sm.group(0).strip() != new_speaker_tag.strip():
            chunk = speaker_re.sub(new_speaker_tag, chunk, count=1)
            changes.append(f"  [{date_str}] Speaker: -> '{entry.name}'")

    return chunk, changes


# ---------------------------------------------------------------------------
# Main patch routine
# ---------------------------------------------------------------------------

def patch_seminar_html(gd_entries: dict):
    """Read seminar.html, patch the spring section. Return (new_content, changes)."""
    with open(SEMINAR_HTML, "r", encoding="utf-8") as f:
        content = f.read()

    if PAST_EVENTS_MARKER not in content:
        print("ERROR: Could not find Past Events marker in seminar.html", file=sys.stderr)
        return content, []

    spring_section, past_section = content.split(PAST_EVENTS_MARKER, 1)

    week_header_re = re.compile(
        r"<p><strong>Week\s+\d+&nbsp;\s*(\w+\s+\d+)\s*:.*?</p>",
        re.DOTALL,
    )
    matches = list(week_header_re.finditer(spring_section))
    if not matches:
        return content, []

    changes: list = []
    result_parts = [spring_section[: matches[0].start()]]

    for i, match in enumerate(matches):
        start = match.start()
        end = (
            matches[i + 1].start() if i + 1 < len(matches) else len(spring_section)
        )
        chunk = spring_section[start:end]
        date_str = match.group(1).strip()

        # Detect no-seminar week
        header_html = match.group(0)
        after_strong_m = re.search(r"</strong>(.*?)(?=</p>)", header_html, re.DOTALL)
        if after_strong_m:
            raw_after = after_strong_m.group(1)
            clean = re.sub(r"<[^>]+>", "", raw_after).replace("&nbsp;", "").strip()
            if clean:
                result_parts.append(chunk)
                continue

        entry = gd_entries.get(date_str)
        if entry is None:
            for k, v in gd_entries.items():
                if k.lower() == date_str.lower():
                    entry = v
                    break

        if entry is None:
            result_parts.append(chunk)
            continue

        new_chunk, chunk_changes = update_chunk(chunk, entry, date_str)
        changes.extend(chunk_changes)
        result_parts.append(new_chunk)

    new_spring = "".join(result_parts)
    new_content = new_spring + PAST_EVENTS_MARKER + past_section
    return new_content, changes


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    print("Fetching Google Doc...")
    try:
        gd_entries = fetch_google_doc()
    except Exception as exc:
        print(f"ERROR fetching Google Doc: {exc}", file=sys.stderr)
        sys.exit(0)

    print(f"Found {len(gd_entries)} seminar entries in Google Doc:")
    for date in sorted(gd_entries):
        e = gd_entries[date]
        n_paras = len(e.abstract_paras)
        abstract_status = f"{n_paras} para(s)" if paras_have_content(e.abstract_paras) else "TBA"
        url_marker = f" url={e.url[:30]}..." if e.url else ""
        print(
            f"  {date}: {e.name or 'TBA'}"
            f" — title:{'set' if e.title else 'TBA'}"
            f" abstract:{abstract_status}{url_marker}"
        )

    print("\nPatching seminar.html...")
    new_content, changes = patch_seminar_html(gd_entries)

    if changes:
        print(f"\nChanges ({len(changes)}):")
        for c in changes:
            print(c)
        with open(SEMINAR_HTML, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("\nseminar.html updated.")
    else:
        print("\nNo changes needed.")

    sys.exit(0)


if __name__ == "__main__":
    main()
