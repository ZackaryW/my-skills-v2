# System Patterns

## Architecture Philosophy
Goal-driven, test-validated skills. Everything is a skill. Everything within a skill is a feature.

## Path Resolution
Pure environment variable-based. Both optional, at least one must be set:

| Variable | Purpose |
|----------|---------|
| `MY_SKILLS_REPO` | Direct path to repo root |
| `SKILLS_GROUP_DIR` | Parent directory; repo derived from subdirectory name |

Resolution: `MY_SKILLS_REPO` → `SKILLS_GROUP_DIR/{repo-name}` → fail.

## Directory Structure

```
skills-repo/
├── about.md              # Instruction file
├── memory-bank/          # Built-in memory bank
│   ├── projectbrief.md
│   ├── productContext.md
│   ├── systemPatterns.md
│   ├── techContext.md
│   ├── activeContext.md
│   ├── progress.md
│   └── details/
├── templates/            # Boilerplate for new skills
├── examples/             # Reference implementations
└── skills/               # All skills (flat or nested)
    └── {skill-name}/
        ├── skill.json    # Required: goal, criteria, features
        ├── skill.md      # Optional: concise supplementary docs
        ├── script.*      # Optional: executable
        └── {sub-skill}/  # Optional: nested sub-skill
```

No `scripts/`, `conditions/`, or `conventions/` directories.

## skill.json Schema

```json
{
  "goal": "str",
  "acceptance_criteria": ["str"],
  "features": [
    {
      "name": "str",
      "test_scenario": "Given-When-Then format",
      "expected_result": "str",
      "optional": false,
      "ext": {
        "script": "script.py",
        "skill_md_ref": "#header",
        "subskill": "sub-skill-name"
      }
    }
  ]
}
```

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `goal` | string | ✓ | — | Clear objective |
| `acceptance_criteria` | string[] | ✓ | — | Measurable success conditions |
| `features` | object[] | ✓ | — | Testable components |
| `features[].name` | string | ✓ | — | Feature identifier |
| `features[].test_scenario` | string | ✓ | — | How to validate (Given-When-Then) |
| `features[].expected_result` | string | ✓ | — | Expected outcome |
| `features[].optional` | bool | ✗ | `false` | If `true`, apply only when referenced |
| `features[].ext` | object | ✗ | — | Extensions |
| `features[].ext.script` | string | ✗ | — | Script at same level |
| `features[].ext.skill_md_ref` | string | ✗ | — | Header ref in skill.md |
| `features[].ext.subskill` | string | ✗ | — | Sub-skill directory name (delegates feature) |

## Feature Optionality

Replaces V1 conditions/ and conventions/:

- **`optional: false`** (default) — Always applies. Core to the skill. (= V1 "condition")
- **`optional: true`** — Apply when referenced or contextually relevant. (= V1 "convention")

## skill.md Rules
- Supplementary only — never duplicate skill.json content
- Keep sections 2-5 lines
- Referenced via `ext.skill_md_ref` using `"#header"` or `"#header/sub"`

## Extension System (ext)

Three extension types, with priority: `subskill` > `script` > `skill_md_ref`

| Key | Purpose | Example |
|-----|---------|--------|
| `subskill` | Delegate feature to a sub-skill directory | `"subskill": "list"` |
| `script` | Execute script at same level | `"script": "script.ps1"` or `"script.sh"` or `"script.py"` |
| `skill_md_ref` | Consult section in skill.md | `"skill_md_ref": "#feature"` |

If `subskill` is set, the sub-skill owns the feature's implementation. `script` and `skill_md_ref` may still provide supplementary context.
All three can coexist in the same `ext` object.

**Cross-platform scripts**: For platform-agnostic skills, provide both `script.ps1` (Windows/PowerShell) and `script.sh` (Unix/Linux/Mac/bash). Agents should use the appropriate script for the OS.

## Nested Skills
Sub-skills live as subdirectories with their own `skill.json`. Same structure recursively.

### Reserved Core Skill: `use-skill`
- Provides skill discovery, resolution, and invocation
- Sub-skills: `use-skill/list`, `use-skill/find`
- Handles repo resolution, skill lookup, and invocation routing

## Memory Bank (Built-in)
Every V2 repo includes `memory-bank/` following Cline protocol:
- 6 core files (projectbrief, productContext, systemPatterns, techContext, activeContext, progress)
- `details/` for offloaded content (when core > ~300 words)
- Consult at session start, update after significant changes
- User can narrow scope; agent asks if unclear

## Skill Invocation via `use-skill`

`use-skill` is a **reserved core skill** — the entry point for all skill discovery and invocation.

### Syntax
```
use-skill/{name}
```

### Resolution Order
1. Sub-skill check (`list`, `find`) → route to sub-skill
2. Exact match: `skills/{name}/skill.json`
3. Partial match: single `skills/*{name}*/skill.json`
4. Ambiguous → ask user
5. Not found → fail, suggest `use-skill/list`

Repo path resolved automatically via env vars before lookup.

### Invocation Protocol (after resolution)
1. Read `skill.json` → goal, criteria, features
2. Execute required features (non-optional)
3. Apply optional features if referenced or relevant
4. For each feature, check `ext` (priority: `subskill` > `script` > `skill_md_ref`):
   - `ext.subskill` → delegate to sub-skill (read its skill.json, recurse)
   - `ext.script` → execute script
   - `ext.skill_md_ref` → consult section
5. Validate against `expected_result`

## Feedback Loop
```
Define Goal → Set Criteria → Create Features → Write Tests
     ↑                                              ↓
  Iterate ← Validate ← Run Tests ← Implement ← Expected Results
```
