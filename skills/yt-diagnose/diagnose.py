#!/usr/bin/env python3
"""diagnose.py - diagnose videos from a YouTube Studio CSV export.

    python3 diagnose.py studio-export.csv
    python3 diagnose.py studio-export.csv --json

Reads only the CSV you exported from Studio. No API, no login, no
scraping, no invented benchmarks. Every video is judged against the
median of its peers in the same file (same format when the export
says so), never against a global number from a blog post.

Gate logic, in the order Studio itself suggests reading it:
  impressions -> CTR / chose-to-view -> retention -> return viewers
  - low shown-in-feed: the video was never tested, not a hook failure
  - low CTR / chose-to-view + high retention: packaging problem
  - high CTR / chose-to-view + low retention: content or promise problem
  - low returning-viewer share: the video did not bring people back

Column matching is forgiving (Studio export headers vary). Any of
these headers, matched case-insensitively by substring, is used:
  title:            "title"
  format:           "format" (short / long) or duration in seconds
  duration:         "duration"
  shown in feed:    "shown in feed" or "impressions"
  chose to view:    "chose to view" or "viewed"
  swiped away:      "swiped away"
  views:            "views"
  engaged views:    "engaged views"
  average % viewed: "percentage viewed" or "% viewed"
  CTR:              "click-through" or "ctr"
  returning share:  "returning viewers"

Do NOT compare raw public views across 31 Mar 2025 (Shorts view
redefinition) or 24 Aug 2026 (all formats): a "view" before those
dates is not the same unit as a "view" after them. CTR, average
view duration and retention are still calculated on engaged views,
so compare those, not raw views, across the boundary.
"""
import csv
import json
import re
import statistics
import sys


def norm(s):
    return re.sub(r"[^a-z0-9 ]", "", (s or "").lower())


def pick(row, *needles):
    for key, val in row.items():
        n = norm(key)
        if any(ned in n for ned in needles):
            return val
    return None


def num(val):
    if val is None:
        return None
    val = str(val).strip().replace("%", "").replace(",", "")
    if val == "":
        return None
    try:
        return float(val)
    except ValueError:
        return None


def duration_secs(val):
    if val is None:
        return None
    val = str(val).strip()
    if re.match(r"^\d+:\d{2}(:\d{2})?$", val):
        parts = [int(p) for p in val.split(":")]
        if len(parts) == 2:
            return parts[0] * 60 + parts[1]
        return parts[0] * 3600 + parts[1] * 60 + parts[2]
    return num(val)


def load(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    videos = []
    for row in rows:
        fmt = (pick(row, "format") or "").strip().lower()
        dur = duration_secs(pick(row, "duration"))
        if not fmt and dur is not None:
            fmt = "short" if dur <= 180 else "long"
        shown = num(pick(row, "shown in feed", "impressions"))
        chose = num(pick(row, "chose to view", "viewed"))
        swiped = num(pick(row, "swiped away"))
        views = num(pick(row, "views"))
        engaged = num(pick(row, "engaged views"))
        pct = num(pick(row, "percentage viewed", "viewed"))
        ctr = num(pick(row, "click-through", "ctr"))
        returning = num(pick(row, "returning viewers"))
        chose_rate = None
        if shown and chose is not None and shown > 0:
            chose_rate = chose / shown
        swiped_rate = None
        if chose is not None and swiped is not None and (chose + swiped) > 0:
            swiped_rate = swiped / (chose + swiped)
        engaged_ratio = None
        if views and engaged is not None and views > 0:
            engaged_ratio = engaged / views
        videos.append({
            "title": pick(row, "title") or "(untitled)",
            "format": fmt or "unknown",
            "duration_s": dur,
            "shown": shown, "chose": chose, "swiped": swiped,
            "views": views, "engaged": engaged,
            "pct_viewed": pct, "ctr": ctr, "returning": returning,
            "chose_rate": chose_rate, "swiped_rate": swiped_rate,
            "engaged_ratio": engaged_ratio,
        })
    return videos


def peer_median(videos, key, self_idx):
    peers = [v for i, v in enumerate(videos) if i != self_idx
             and v["format"] == videos[self_idx]["format"]
             and v[key] is not None]
    if len(peers) < 2:
        peers = [v for i, v in enumerate(videos) if i != self_idx
                 and v[key] is not None]
    if not peers:
        return None
    return statistics.median([v[key] for v in peers])


def relative(value, median):
    """How far value sits from the peer median, as a ratio. None if unknown."""
    if value is None or median is None or median == 0:
        return None
    return value / median


def diagnose(videos):
    out = []
    for i, v in enumerate(videos):
        gates = {}
        # Reach: was it even tested?
        m_shown = peer_median(videos, "shown", i)
        gates["reach"] = relative(v["shown"], m_shown)
        # Hook: chose-to-view rate (Shorts) or CTR (long-form)
        hook_val = v["chose_rate"] if v["format"] == "short" else v["ctr"]
        hook_key = "chose_rate" if v["format"] == "short" else "ctr"
        m_hook = peer_median(videos, hook_key, i)
        gates["hook"] = relative(hook_val, m_hook)
        # Retention: average % viewed
        m_pct = peer_median(videos, "pct_viewed", i)
        gates["retention"] = relative(v["pct_viewed"], m_pct)
        # Return: returning-viewer share
        m_ret = peer_median(videos, "returning", i)
        gates["return"] = relative(v["returning"], m_ret)

        assessed = {k: r for k, r in gates.items() if r is not None}
        weakest = min(assessed, key=assessed.get) if assessed else None
        findings = []
        if gates["reach"] is not None and gates["reach"] < 1:
            findings.append(
                "low shown-in-feed vs peers: this video was barely tested, "
                "so do not read it as a hook failure yet.")
        if gates["hook"] is not None and gates["hook"] < 1:
            findings.append(
                "hook below peer median: first frame / first seconds did "
                "not win the click or the stay.")
        if gates["retention"] is not None and gates["retention"] < 1:
            findings.append(
                "retention below peer median: viewers left early - check "
                "the retention curve for the cliff, not the average.")
        if gates["return"] is not None and gates["return"] < 1:
            findings.append(
                "returning-viewer share below peer median: the video did "
                "not bring people back.")

        # The classic pairings, stated as comparisons, not thresholds.
        # "Barely tested" is a tool heuristic (shown under half the
        # peer median), not a YouTube rule: with that little reach,
        # hook and retention ratios are noise, so reach is read first.
        if gates["reach"] is not None and gates["reach"] < 0.5:
            verdict = "NOT TESTED: reach is the broken gate. Wait for the " \
                "test audience before judging hook or retention."
        elif (gates["hook"] is not None and gates["hook"] < 1
                and gates["retention"] is not None and gates["retention"] >= 1):
            verdict = "PACKAGING problem: low hook, high retention. " \
                "Repackage (title/thumbnail/first frame) before rewriting."
        elif (gates["hook"] is not None and gates["hook"] >= 1
                and gates["retention"] is not None and gates["retention"] < 1):
            verdict = "CONTENT / PROMISE problem: the hook worked and " \
                "viewers left anyway. The video did not deliver what " \
                "the packaging promised, or the payoff came too late."
        elif weakest == "return":
            verdict = "RETURN problem: the video performed but did not " \
                "convert viewers into returning viewers. Check the " \
                "series pointer, Related Video and pinned comment."
        elif weakest:
            verdict = f"WEAKEST GATE: {weakest}. Fix that one gate on " \
                "the next video, and nothing else, so you learn what worked."
        else:
            verdict = "NOT ENOUGH DATA: the export lacks the columns " \
                "needed to judge any gate. Export shown-in-feed, " \
                "chose-to-view, average % viewed and returning share."
        out.append({
            "title": v["title"], "format": v["format"],
            "shown": v["shown"], "views": v["views"],
            "engaged_views": v["engaged"],
            "engaged_ratio": (round(v["engaged_ratio"], 3)
                              if v["engaged_ratio"] is not None else None),
            "chose_rate": (round(v["chose_rate"], 3)
                           if v["chose_rate"] is not None else None),
            "swiped_rate": (round(v["swiped_rate"], 3)
                            if v["swiped_rate"] is not None else None),
            "pct_viewed": v["pct_viewed"], "ctr": v["ctr"],
            "gates_vs_peer_median": {k: (round(r, 2) if r is not None else None)
                                     for k, r in gates.items()},
            "findings": findings,
            "verdict": verdict,
        })
    return out


def show(results):
    for r in results:
        print(f"\n  {r['title']} [{r['format']}]")
        if r["engaged_ratio"] is not None:
            print(f"    engaged share of public views: {r['engaged_ratio']}")
        if r["chose_rate"] is not None:
            print(f"    chose-to-view rate: {r['chose_rate']}")
        if r["swiped_rate"] is not None:
            print(f"    swiped-away share: {r['swiped_rate']}")
        print("    gates vs peer median: " +
              ", ".join(f"{k}={v}" for k, v in
                        r["gates_vs_peer_median"].items() if v is not None))
        for f in r["findings"]:
            print(f"    - {f}")
        print(f"    VERDICT: {r['verdict']}")
    print("\n  note: medians are from THIS export only. They are your "
          "channel's baseline, not a YouTube rule.")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    as_json = "--json" in sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)
    videos = load(args[0])
    if not videos:
        print("no data rows found in the CSV")
        sys.exit(1)
    results = diagnose(videos)
    if as_json:
        print(json.dumps(results, indent=1))
    else:
        show(results)


if __name__ == "__main__":
    main()
