#!/usr/bin/env python3
"""publish_check.py - pre-publish checklist for a video or Short.

Usage:
    python3 publish_check.py publish.json
    python3 publish_check.py publish.json --json

Input JSON example:
    {"title": "...", "thumb_text": "...", "description": "...",
     "type": "short", "ai_generated": true, "ai_disclosure": true,
     "playlist": "Skill Challenge", "chapters": false,
     "end_screen": false, "community_poll": false,
     "format": "9:16", "clean": true,
     "comparison_sides": ["beam", "floor"], "pinned_comment": "..."}

Checks (v3.3.6): title present and 100 characters or fewer,
thumbnail text present and 3 words or fewer, thumbnail words do
not repeat the title words, description first line present, AI
disclosure present when ai_generated is true, playlist named,
format is vertical 9:16 (1080x1920 preferred, 720x1280 at the same
ratio acceptable, v3.3.4), output is generated clean with no
watermark (clean = generated clean, never stripped), branded
content disclosed by the creator (never rely on auto-detection,
v3.3.6), the pinned comment is the vote on comparison Shorts
(both sides, v3.3.2), and for long videos chapters and an end
screen. A missing item is FAIL, not a guess. This tool does not
publish anything and does not touch media. It is not a substitute
for yt-qa: scorecard, face gate, audio gate, text-end rule,
parasocial tail cap and leotard slot are checked there, not here.
"""
import argparse
import json
import re
import sys

STOP = {"the", "a", "an", "of", "for", "to", "in", "on", "and", "or",
        "is", "are", "with", "your", "you", "my", "i", "this", "that",
        "it", "how", "what", "why"}
FORMAT_OK = {"9:16", "vertical", "1080x1920", "720x1280", "1080 x 1920",
             "720 x 1280"}


def words(t):
    return re.findall(r"[a-z0-9]+", (t or "").lower())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    with open(args.file, encoding="utf-8") as handle:
        data = json.load(handle)

    checks = []

    def add(name, passed, note):
        checks.append({"check": name, "status": "PASS" if passed else "FAIL", "note": note})

    title = str(data.get("title", "")).strip()
    add("title", bool(title) and len(title) <= 100,
        "Title is present and 100 characters or fewer."
        if title and len(title) <= 100 else "Add a title of 100 characters or fewer.")

    thumb_words = re.findall(r"[A-Za-z0-9]+", str(data.get("thumb_text", "")))
    add("thumbnail_text", 1 <= len(thumb_words) <= 3,
        "Thumbnail text is 1 to 3 words."
        if 1 <= len(thumb_words) <= 3 else "Write 1 to 3 words of thumbnail text.")

    shared = (set(words(title)) - STOP) & (set(words(data.get("thumb_text", ""))) - STOP)
    add("thumbnail_repeat", not shared,
        "Thumbnail words differ from the title words."
        if not shared else
        f"Thumbnail repeats the title on {', '.join(sorted(shared))} - "
        "the pairing should carry twice the information (title.py).")

    fmt = str(data.get("format", "")).strip().lower()
    add("format", fmt in FORMAT_OK,
        "Format is vertical 9:16."
        if fmt in FORMAT_OK else
        "Format must be vertical 9:16 (1080x1920 preferred, 720x1280 "
        "acceptable); 16:9 or landscape fails the format gate.")

    clean = data.get("clean")
    watermark = data.get("watermark")
    clean_ok = clean is True and watermark is not True
    add("clean", clean_ok,
        "Output is generated clean, no watermark."
        if clean_ok else
        "Confirm the render is generated clean (clean: true) with no "
        "watermark; never strip another tool's watermark.")

    if data.get("branded_content"):
        add("branded_disclosure", bool(data.get("branded_disclosure")),
            "Branded content is disclosed by the creator."
            if data.get("branded_disclosure") else
            "Disclose the branded content yourself; do not rely on "
            "YouTube auto-detection.")
    else:
        add("branded_disclosure", True, "No branded content, no disclosure needed.")

    sides = data.get("comparison_sides") or []
    if len(sides) >= 2:
        pinned = str(data.get("pinned_comment", "")).lower()
        missing = [s for s in sides if str(s).lower() not in pinned]
        add("pinned_vote", not missing,
            "Pinned comment is the vote naming both sides."
            if not missing else
            f"Pinned comment must name both sides in video order; "
            f"missing: {', '.join(missing)} (yt-post vote rule).")
    else:
        add("pinned_vote", True, "Not a comparison Short, no vote required.")

    description = str(data.get("description", "")).strip()
    first_line = description.splitlines()[0].strip() if description else ""
    add("description_first_line", bool(first_line),
        "Description opens with a readable first line."
        if first_line else "Write a first description line that states what the video gives.")

    if data.get("ai_generated"):
        add("ai_disclosure", bool(data.get("ai_disclosure")),
            "AI disclosure is marked."
            if data.get("ai_disclosure") else "Mark the AI disclosure before publishing.")
    else:
        add("ai_disclosure", True, "Not AI generated, no disclosure needed.")

    add("playlist", bool(str(data.get("playlist", "")).strip()),
        "Video is assigned to a playlist."
        if data.get("playlist") else "Assign the video to a playlist.")

    if str(data.get("type", "short")).lower() == "long":
        add("chapters", bool(data.get("chapters")),
            "Chapters are included."
            if data.get("chapters") else "Add chapters for a long video.")
        add("end_screen", bool(data.get("end_screen")),
            "End screen is set."
            if data.get("end_screen") else "Set an end screen for a long video.")
    else:
        add("chapters", True, "Shorts do not need chapters.")
        add("end_screen", True, "Shorts do not need an end screen.")

    failed = [c for c in checks if c["status"] == "FAIL"]
    result = {
        "status": "READY" if not failed else "NOT READY",
        "failed": len(failed),
        "checks": checks,
    }
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"Publish check: {result['status']} ({len(failed)} failed)")
        for item in checks:
            print(f"  {item['status']} {item['check']}: {item['note']}")
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
