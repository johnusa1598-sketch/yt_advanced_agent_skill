#!/usr/bin/env python3
"""publish_check.py - pre-publish checklist for a video or Short.

Usage:
    python3 publish_check.py publish.json
    python3 publish_check.py publish.json --json

Input JSON example:
    {"title": "...", "thumb_text": "...", "description": "...",
     "type": "short", "ai_generated": true, "ai_disclosure": true,
     "playlist": "Skill Challenge", "chapters": false,
     "end_screen": false, "community_poll": false}

Checks: title present and 100 characters or fewer, thumbnail text
present and 3 words or fewer, description first line present, AI
disclosure present when ai_generated is true, playlist named, and for
long videos chapters and an end screen. A missing item is FAIL, not a
guess. This tool does not publish anything and does not touch media.
"""
import argparse
import json
import re
import sys


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
