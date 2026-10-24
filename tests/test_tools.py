#!/usr/bin/env python3
"""Run every tool in this pack against sample data and check exit codes.

Run from the pack root:
    python3 tests/test_tools.py

No network, no YouTube login, no publishing. A tool that cannot run
its sample is a broken tool, and this test is how you find out
before a creator does.
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run(args, input_file=None):
    result = subprocess.run(
        [sys.executable, *args],
        cwd=ROOT, capture_output=True, text=True, timeout=60,
    )
    return result


def check(name, result, must_contain=""):
    if result.returncode not in (0, 1):
        print(f"FAIL {name}: exit {result.returncode}\n{result.stderr}")
        return False
    if must_contain and must_contain not in result.stdout:
        print(f"FAIL {name}: missing {must_contain!r}\n{result.stdout}")
        return False
    print(f"PASS {name}")
    return True


def main():
    ok = True
    ok &= check("hookscore", run(["skills/yt-script/hookscore.py", "--hook",
        "I tested 3 viral gymnastics hacks, only 1 worked"]), "SPECIFICITY")
    ok &= check("title", run(["skills/yt-package/title.py", "--title",
        "I tested 3 viral gymnastics hacks, only 1 worked",
        "--thumb", "ONLY 1 WORKED"]), "characters")
    ok &= check("analytics", run(["skills/yt-analytics/analytics.py",
        "examples/aria-fit/videos.json", "--subs", "92"]), "One fix")
    ok &= check("shorts_score", run(["skills/yt-shorts-first/shorts_score.py",
        "--title", "I tested 3 viral gymnastics hacks, only 1 worked",
        "--thumb", "ONLY 1 WORKED", "--hook", "Which hack actually works?",
        "--loop", "yes", "--cta", "follow for part 2",
        "--series", "Skill Challenge"]), "Shorts score")
    ok &= check("prompt_builder", run(["skills/yt-ai-prompt/prompt_builder.py",
        "examples/aria-fit/ai-brief.json"]), "CHARACTER LOCK")
    ok &= check("prompt_builder_json", run(["skills/yt-ai-prompt/prompt_builder.py",
        "examples/aria-fit/ai-brief.json", "--json"]), "negative_prompt")
    ok &= check("publish_check_fail", run(["skills/yt-publish/publish_check.py",
        "tests/fixtures/publish-bad.json"]), "NOT READY")
    ok &= check("publish_check_pass", run(["skills/yt-publish/publish_check.py",
        "tests/fixtures/publish-good.json"]), "READY")
    print("ALL PASS" if ok else "SOME TESTS FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
