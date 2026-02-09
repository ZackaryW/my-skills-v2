# Goal-Driven Skills Repository

A goal-driven, test-validated skills architecture inspired by Jira user stories.

## Core Concept

```
Goal → Acceptance Criteria → Features (required + optional) → Test Scenarios → Expected Results
```

Everything is a skill. Everything within a skill is a feature. No separate `scripts/`, `conditions/`, or `conventions/` directories.

## Structure

```
skills-repo/
├── about.md              # Instruction file (for AI agents)
├── memory-bank/          # Built-in memory bank
├── templates/            # Boilerplate for new skills
├── examples/             # Reference implementations
└── skills/               # All skills (flat or nested)
    └── {skill-name}/
        ├── skill.json    # Required: goal, criteria, features
        ├── skill.md      # Optional: concise supplementary docs
        ├── script.*      # Optional: executable
        └── {sub-skill}/  # Optional: nested sub-skill
```

## skill.json Schema

```json
{
  "goal": "Clear objective of what this skill achieves",
  "acceptance_criteria": [
    "Measurable success condition 1",
    "Measurable success condition 2"
  ],
  "features": [
    {
      "name": "Feature Name",
      "test_scenario": "Given [condition], When [action], Then [outcome]",
      "expected_result": "Specific, verifiable outcome",
      "optional": false,
      "ext": {
        "script": "script.py",
        "skill_md_ref": "#feature-name"
      }
    }
  ]
}
```

### Feature Optionality

- **`optional: false`** (default) — Always applies. Core to the skill.
- **`optional: true`** — Apply only when referenced or contextually relevant.

This replaces V1's separate `conditions/` (always-apply) and `conventions/` (on-demand) directories.

### Extensions (ext)

- `ext.script` — Script file at same level to execute
- `ext.skill_md_ref` — Header reference in skill.md (e.g. `"#header"` or `"#header/sub"`)

## Quick Start

```bash
mkdir skills/my-new-skill
cp templates/skill.json skills/my-new-skill/
# Edit skill.json with your goal, criteria, and features
```

## Environment Variables

```powershell
$env:MY_SKILLS_REPO = "C:\path\to\skills-repo"
$env:SKILLS_GROUP_DIR = "C:\path\to\skills"
```

## Built-in Skills

### use-skill
Core skill for discovering, resolving, and invoking skills.
- **use-skill/list** — List all available skills with goals
- **use-skill/find** — Search skills by name or keyword
- **use-skill/update** — Pull latest changes from git remote
- **use-skill/create-repo** — Create new skills repository with V2 structure

### configure-memory-bank
Initialize and configure memory bank structure with all core files.

### cleanup-memory-bank
Maintain memory bank quality by keeping core files under 300 words and offloading details to subdirectory.

### dev
Development methodology and protocol skills.
- **dev/focus-boundary** — Control AI autonomy and creative freedom (3 levels: full, minimal+constrained, minimal+unrestricted)
- **dev/std-dev-impl** — Structured 5-phase TDD implementation protocol with user collaboration gates

## Examples

See [examples/hello-world](examples/hello-world) for a complete working example.

## Resources

- [about.md](about.md) — Full instruction file for AI agents
- [memory-bank/](memory-bank/) — Project documentation
- [templates/](templates/) — Boilerplate for new skills
- [examples/](examples/) — Reference implementations
