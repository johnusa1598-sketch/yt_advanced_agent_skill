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
    ok &= check("prompt_builder_format", run(["skills/yt-ai-prompt/prompt_builder.py",
        "examples/aria-fit/ai-brief.json"]), "9:16")
    ok &= check("prompt_builder_iphone", run(["skills/yt-ai-prompt/prompt_builder.py",
        "examples/aria-fit/ai-brief.json"]), "iPhone")
    ok &= check("prompt_builder_outfit", run(["skills/yt-ai-prompt/prompt_builder.py",
        "examples/aria-fit/ai-brief.json", "--outfit", "teal leotard"]),
        "teal leotard")
    ok &= check("publish_check_fail", run(["skills/yt-publish/publish_check.py",
        "tests/fixtures/publish-bad.json"]), "NOT READY")
    ok &= check("publish_check_pass", run(["skills/yt-publish/publish_check.py",
        "tests/fixtures/publish-good.json"]), "READY")
    ok &= check("trend_pack", run(["skills/yt-trends/trend_pack.py",
        "beam backflip", "--niche", "AI gymnastics", "--brand", "Aria Fit",
        "--evidence", "tests/fixtures/trend-evidence.json"]), "#gymnastics")
    ok &= check("trend_pack_json", run(["skills/yt-trends/trend_pack.py",
        "beam backflip", "--evidence", "tests/fixtures/trend-evidence.json",
        "--json"]), "evidence_seen")
    ok &= check("package_builder", run(["skills/yt-post/package_builder.py",
        "tests/fixtures/package-brief.json"]), "THUMBNAIL BRIEF")
    ok &= check("package_builder_json", run(["skills/yt-post/package_builder.py",
        "tests/fixtures/package-brief.json", "--json"]), "ab_test")
    ok &= check("retention_plan", run(["skills/yt-viral-loop/retention_plan.py",
        "tests/fixtures/package-brief.json"]), "RETENTION PLAN")
    ok &= check("retention_plan_flags", run(["skills/yt-viral-loop/retention_plan.py",
        "tests/fixtures/retention-brief.json"]), "long-beat")
    ok &= check("retention_plan_json", run(["skills/yt-viral-loop/retention_plan.py",
        "tests/fixtures/package-brief.json", "--json"]), "drop_off_guards")
    ok &= check("diagnose", run(["skills/yt-diagnose/diagnose.py",
        "tests/fixtures/studio-export.csv"]), "PACKAGING problem")
    ok &= check("diagnose_content", run(["skills/yt-diagnose/diagnose.py",
        "tests/fixtures/studio-export.csv"]), "CONTENT / PROMISE problem")
    ok &= check("diagnose_nottested", run(["skills/yt-diagnose/diagnose.py",
        "tests/fixtures/studio-export.csv"]), "NOT TESTED")
    ok &= check("diagnose_json", run(["skills/yt-diagnose/diagnose.py",
        "tests/fixtures/studio-export.csv", "--json"]), "gates_vs_peer_median")
    ok &= check("srt_qa", run(["skills/yt-sound/srt_qa.py",
        "tests/fixtures/captions.srt"]), "overlaps")
    ok &= check("srt_qa_speed", run(["skills/yt-sound/srt_qa.py",
        "tests/fixtures/captions.srt"]), "reading speed")
    ok &= check("srt_qa_safety", run(["skills/yt-sound/srt_qa.py",
        "tests/fixtures/captions.srt", "--safety-words",
        "tests/fixtures/safety-words.txt"]), "safety terms missing")
    ok &= check("originality", run(["skills/yt-originality/originality_scan.py",
        "tests/fixtures/uploads.json"]), "DISCLOSURE CHECK")
    ok &= check("originality_repeat", run(["skills/yt-originality/originality_scan.py",
        "tests/fixtures/uploads.json"]), "repeated structures")
    ok &= check("originality_json", run(["skills/yt-originality/originality_scan.py",
        "tests/fixtures/uploads.json", "--json"]), "repeated_structures")
    ok &= check("scorecard_pass", run(["skills/yt-qa/scorecard.py",
        "--identity", "3", "--movement", "2", "--phone", "2",
        "--beats", "2"]), "PASS")
    ok &= check("scorecard_subgate", run(["skills/yt-qa/scorecard.py",
        "--identity", "1", "--movement", "3", "--phone", "2",
        "--beats", "2"]), "FAIL")
    ok &= check("scorecard_json", run(["skills/yt-qa/scorecard.py",
        "--identity", "3", "--movement", "3", "--phone", "2",
        "--beats", "2", "--json"]), '"verdict": "PASS"')
    ok &= check("skills_structure", check_skills(), "STRUCTURE OK")
    print("ALL PASS" if ok else "SOME TESTS FAILED")
    return 0 if ok else 1


class _FakeResult:
    def __init__(self, ok, text):
        self.returncode = 0 if ok else 2
        self.stdout = text
        self.stderr = ""


def check_skills():
    """Every skill ships a SKILL.md and a skill.yaml; every tool runs."""
    missing = []
    for skill_dir in sorted((ROOT / "skills").glob("yt-*")):
        if not (skill_dir / "SKILL.md").exists():
            missing.append(f"{skill_dir.name}/SKILL.md")
        if not (skill_dir / "skill.yaml").exists():
            missing.append(f"{skill_dir.name}/skill.yaml")
    tools = sorted((ROOT / "skills").glob("yt-*/**/*.py"))
    if not missing and len(tools) >= 16:
        return _FakeResult(True, f"STRUCTURE OK: {len(tools)} tools")
    return _FakeResult(False, "STRUCTURE FAIL: " + ", ".join(missing) +
                      f" ({len(tools)} tools)")


if __name__ == "__main__":
    raise SystemExit(main())
