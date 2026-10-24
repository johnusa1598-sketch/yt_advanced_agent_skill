#!/usr/bin/env python3
"""analytics.py - channel analytics from a simple video list.

Usage:
    python3 analytics.py videos.json
    python3 analytics.py videos.json --subs 92 --json

Input JSON: a list of objects, one per video:
    [{"title": "...", "views": 7210, "likes": 88, "date": "2026-10-19",
      "format": "Rating"}, ...]
The format field is optional. When missing, it is inferred from common
title prefixes such as Skill Challenge, Flexibility Test, Slow-Mo, and Fail.

Output: total and average views, median views, like rate, the top 5 and
bottom 3 videos by views, each video's multiple over the channel median,
the best and worst format by average views, subs per 1000 views when
--subs is given, and one recommended fix. This is descriptive arithmetic
on numbers you supply. It does not fetch YouTube data and it does not
predict future views.
"""
import argparse
import json
import statistics
import sys
from collections import defaultdict


def infer_format(title):
    low = title.lower()
    if "vs" in low or "versus" in low or "who won" in low or "duel" in low:
        return "Duel"
    if "rate it" in low or "1-10" in low or "1–10" in low:
        return "Rating"
    if "flexibility" in low:
        return "Flexibility Test"
    if "slow-mo" in low or "slow mo" in low:
        return "Slow-Mo"
    if "fail" in low or "blooper" in low:
        return "Fail"
    if "hack" in low:
        return "Viral Hack Test"
    if "skill challenge" in low:
        return "Skill Challenge"
    return "Other"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    parser.add_argument("--subs", type=int, default=None)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    with open(args.file, encoding="utf-8") as handle:
        videos = json.load(handle)
    if not isinstance(videos, list) or not videos:
        print("analytics.py: input must be a non-empty JSON list", file=sys.stderr)
        return 2

    for video in videos:
        video["format"] = video.get("format") or infer_format(video.get("title", ""))
        views = int(video.get("views", 0))
        likes = int(video.get("likes", 0))
        video["like_rate"] = round(100.0 * likes / views, 2) if views else 0.0

    views_list = [int(v.get("views", 0)) for v in videos]
    total = sum(views_list)
    median = statistics.median(views_list)
    average = total / len(videos)
    for video in videos:
        video["multiple"] = round(int(video.get("views", 0)) / median, 2) if median else 0.0

    by_format = defaultdict(list)
    for video in videos:
        by_format[video["format"]].append(int(video.get("views", 0)))
    format_avg = {
        name: round(sum(values) / len(values), 1)
        for name, values in sorted(by_format.items())
    }
    best_format = max(format_avg, key=format_avg.get)
    worst_format = min(format_avg, key=format_avg.get)

    ranked = sorted(videos, key=lambda v: int(v.get("views", 0)), reverse=True)
    result = {
        "videos": len(videos),
        "total_views": total,
        "average_views": round(average, 1),
        "median_views": median,
        "average_like_rate": round(
            sum(v["like_rate"] for v in videos) / len(videos), 2
        ),
        "format_average_views": format_avg,
        "best_format": best_format,
        "worst_format": worst_format,
        "top_5": [
            {"title": v.get("title", ""), "views": int(v.get("views", 0)),
             "multiple": v["multiple"], "format": v["format"]}
            for v in ranked[:5]
        ],
        "bottom_3": [
            {"title": v.get("title", ""), "views": int(v.get("views", 0)),
             "multiple": v["multiple"], "format": v["format"]}
            for v in ranked[-3:]
        ],
    }
    if args.subs is not None:
        result["subs_per_1000_views"] = round(1000.0 * args.subs / total, 2) if total else 0.0
        result["subs"] = args.subs
    if format_avg[best_format] >= 1.5 * average:
        result["one_fix"] = (
            f"Double down on {best_format}: it averages {format_avg[best_format]} "
            f"views against a channel average of {round(average, 1)}. "
            f"Make the next three uploads in that format before trying a new one."
        )
    else:
        result["one_fix"] = (
            "No format is clearly ahead, so the fix is packaging, not ideas: "
            "rewrite the next three titles with a searchable keyword first, "
            "then a hook, and check them with yt-package before publishing."
        )

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"Videos: {result['videos']}  Total views: {total}  "
              f"Average: {result['average_views']}  Median: {median}")
        if "subs_per_1000_views" in result:
            print(f"Subs per 1000 views: {result['subs_per_1000_views']}")
        print(f"Average like rate: {result['average_like_rate']}%")
        print("Format averages:")
        for name, value in format_avg.items():
            print(f"  {name}: {value}")
        print("Top 5:")
        for item in result["top_5"]:
            print(f"  {item['views']} views ({item['multiple']}x median) - {item['title']}")
        print("One fix:")
        print(f"  {result['one_fix']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
