#!/usr/bin/env python3
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


def iter_skill_entries(repo_root):
    for base in ("skills", "examples"):
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


def is_match(query, display, rel_display, goal):
    query = query.strip().lower()
    if not query:
        return False

    query_path = query.replace(".", "/")
    display_lc = display.lower()
    rel_lc = rel_display.lower()

    if "/" in query_path:
        if query_path in display_lc or query_path in rel_lc:
            return True
    else:
        if query in display_lc or query in rel_lc:
            return True

    if goal and query in goal.lower():
        return True

    return False


def main():
    if len(sys.argv) < 2:
        print("Usage: script.py <query>", file=sys.stderr)
        return 2

    query = " ".join(sys.argv[1:]).strip()
    if not query:
        print("Error: query is required.", file=sys.stderr)
        return 2

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

    matches = []
    for display, rel_display, skill_json_path in iter_skill_entries(repo_root):
        goal = load_goal(skill_json_path)
        if is_match(query, display, rel_display, goal):
            matches.append((display, goal))

    if not matches:
        print(f"No matches for '{query}'.")
        return 0

    for display, goal in sorted(matches, key=lambda item: item[0].lower()):
        print(f"{display}\t{goal}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
