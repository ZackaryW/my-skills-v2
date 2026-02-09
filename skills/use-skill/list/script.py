#!/usr/bin/env python3
import argparse
import json
import os
import sys


def resolve_repo_root():
    repo_root = os.environ.get("MY_SKILLS_REPO")
    if repo_root:
        return repo_root

    group_dir = os.environ.get("SKILLS_GROUP_DIR")
    if group_dir:
        return os.path.join(group_dir, "my-skills-v2")

    return None


def iter_skill_entries(repo_root, bases):
    for base in bases:
        base_dir = os.path.join(repo_root, base)
        if not os.path.isdir(base_dir):
            continue

        for dirpath, _dirnames, filenames in os.walk(base_dir):
            if "skill.json" not in filenames:
                continue

            rel_path = os.path.relpath(dirpath, base_dir)
            if rel_path == ".":
                continue

            rel_display = rel_path.replace(os.sep, "/")
            if base == "examples":
                display = f"examples/{rel_display}"
            else:
                display = rel_display

            yield display, rel_display, os.path.join(dirpath, "skill.json")


def load_goal(skill_json_path):
    try:
        with open(skill_json_path, "r", encoding="utf-8") as handle:
            data = json.load(handle)
        goal = data.get("goal", "")
        return goal.strip() if isinstance(goal, str) else ""
    except (OSError, json.JSONDecodeError, ValueError):
        return ""


def normalize_tag(tag):
    return tag.strip().lower().replace(".", "/")


def tag_matches(tag, display, rel_display, goal):
    if not tag:
        return False

    display_lc = display.lower()
    rel_lc = rel_display.lower()
    goal_lc = goal.lower() if goal else ""

    if "/" in tag:
        return tag in display_lc or tag in rel_lc

    return tag in display_lc or tag in rel_lc or (goal_lc and tag in goal_lc)


def is_included(display, rel_display, goal, include_tags, exclude_tags):
    for tag in include_tags:
        if not tag_matches(tag, display, rel_display, goal):
            return False

    for tag in exclude_tags:
        if tag_matches(tag, display, rel_display, goal):
            return False

    return True


def main():
    parser = argparse.ArgumentParser(
        description="List skills with optional filtering.",
    )
    parser.add_argument(
        "--include",
        action="append",
        default=[],
        help="Include tag (can be repeated).",
    )
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="Exclude tag (can be repeated).",
    )
    parser.add_argument(
        "--repo",
        choices=["skills", "examples", "all"],
        default="all",
        help="Filter which repo section to list.",
    )

    args = parser.parse_args()
    include_tags = [normalize_tag(tag) for tag in args.include if tag.strip()]
    exclude_tags = [normalize_tag(tag) for tag in args.exclude if tag.strip()]

    repo_root = resolve_repo_root()
    if not repo_root:
        print(
            "Error: set MY_SKILLS_REPO or SKILLS_GROUP_DIR to resolve the repo.",
            file=sys.stderr,
        )
        return 1

    if not os.path.isdir(repo_root):
        print(f"Error: repo root not found: {repo_root}", file=sys.stderr)
        return 1

    if args.repo == "all":
        bases = ["skills", "examples"]
    else:
        bases = [args.repo]

    matches = []
    for display, rel_display, skill_json_path in iter_skill_entries(repo_root, bases):
        goal = load_goal(skill_json_path)
        if is_included(display, rel_display, goal, include_tags, exclude_tags):
            matches.append((display, goal))

    if not matches:
        print("No matches.")
        return 0

    for display, goal in sorted(matches, key=lambda item: item[0].lower()):
        print(f"{display}\t{goal}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
