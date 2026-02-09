---
applyTo: '**'
---
priority: highest

> ⚠️ **When to consult this file**: Read about.md when working **on** this skills repo (developing skills, updating structure). For skill **invocation/usage**, this is NOT required—follow the skill's own instructions.

> **Memory Bank**: Consult `memory-bank/` when developing/maintaining the repo. Not required for skill invocation. See scope rules below.

## Path Resolution

Resolve repo path using environment variables (first match wins):

1. `${MY_SKILLS_REPO}` — if set, use directly as repo root.
2. `${SKILLS_GROUP_DIR}/{repo-name}` — if set, derive repo path from parent directory.
3. **Fail** (never guess a path).

Both variables are optional. At least one must be set.

# Goal-Driven Skills Repository

> **Priority: HIGHEST** — Goal-driven skills with built-in Memory Bank.

## Structure

```
skills-repo/
├── about.md              # This file (instruction)
├── memory-bank/          # Built-in memory bank
├── templates/            # Boilerplate for new skills
├── examples/             # Reference implementations
└── skills/               # All skills (flat or nested)
    └── {skill-name}/
        ├── skill.json    # Required: goal, criteria, features
        ├── skill.md      # Optional: concise supplementary docs
        ├── script.*      # Optional: executable
        └── {sub-skill}/  # Optional: nested sub-skill (same structure)
```

No separate `scripts/`, `conditions/`, or `conventions/` directories. Everything is a skill. Everything within a skill is a feature.

---

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
        "skill_md_ref": "#feature-name",
        "subskill": "sub-skill-name"
      }
    }
  ]
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `goal` | string | ✓ | What the skill achieves |
| `acceptance_criteria` | string[] | ✓ | Measurable success conditions |
| `features` | object[] | ✓ | Testable components |
| `features[].name` | string | ✓ | Feature identifier |
| `features[].test_scenario` | string | ✓ | Given-When-Then validation |
| `features[].expected_result` | string | ✓ | What success looks like |
| `features[].optional` | bool | ✗ | Default `false`. If `true`, apply only when referenced or relevant |
| `features[].ext` | object | ✗ | Extensions (below) |
| `features[].ext.script` | string | ✗ | Script at same level to execute |
| `features[].ext.skill_md_ref` | string | ✗ | Header ref in skill.md (e.g. `"#header"` or `"#header/sub"`) |
| `features[].ext.subskill` | string | ✗ | Sub-skill directory name at same level (delegates feature to nested skill) |

### Feature Optionality (replaces V1 conditions/conventions)

- **`optional: false`** (default) — Always applies. The feature is core to the skill.
- **`optional: true`** — Applies only when the user references it, or when contextually relevant. Agent may skip unless asked.

This eliminates the need for separate condition/convention files. A "condition" is a required feature. A "convention" is an optional feature with a reference.

### Skill Discovery & Resolution (`use-skill`)

`use-skill` is a **reserved core skill** for discovering and invoking skills. Syntax:

```
use-skill/{name}
```

**Resolution order** (first match wins):
1. **Sub-skill** — if `{name}` is `list`, `find`, or `update`, route to that sub-skill
2. **Exact match** — `skills/{name}/skill.json` exists
3. **Partial match** — single `skills/*{name}*/skill.json` found
4. **Ambiguous** — multiple matches → ask user
5. **Not found** — fail, suggest `use-skill/list`

Repo path is resolved automatically via env vars before skill lookup.

| Command | Effect |
|---------|--------|
| `use-skill/list` | List all skills with goals |
| `use-skill/find {query}` | Search skills by name or goal keyword |
| `use-skill/update` | Pull latest changes from git remote |
| `use-skill/memory-bank` | Resolves to `configure-memory-bank` (partial match) |

### Invocation Protocol

Once a skill is resolved:
1. Read `skill.json` → understand goal, criteria, features
2. Execute required features (`optional: false` or omitted)
3. Check optional features → apply if referenced or contextually relevant
4. For each feature, check `ext`:
   - `ext.subskill` → delegate to sub-skill directory (read its `skill.json`, recurse)
   - `ext.script` → execute script
   - `ext.skill_md_ref` → consult that section in skill.md
5. Validate against `expected_result`

**Extension priority within a feature:** `subskill` > `script` > `skill_md_ref`. If `subskill` is set, the sub-skill owns the feature’s implementation. `script` and `skill_md_ref` may still provide supplementary context.

---

## Memory Bank

Built-in `memory-bank/` follows Cline Memory Bank protocol.

**Purpose**: Provides context for **developing and maintaining** this skills repo. Not required for skill invocation—only when working on the repo itself.

### Files
| File | Purpose |
|------|---------|
| `projectbrief.md` | Foundation: scope, goals, requirements |
| `productContext.md` | Why it exists, how it should work |
| `systemPatterns.md` | Architecture, patterns, decisions |
| `techContext.md` | Technologies, setup, constraints |
| `activeContext.md` | Current focus, recent changes, next steps |
| `progress.md` | Status tracking, what works, what's left |
| `details/` | Offloaded content when core files > ~300 words |

### Scope Rules

**When to read**: Only when working **on** this skills repo (developing skills, updating structure, fixing issues). Skip when simply **using** skills.

**Default scope** (when relevant): Read all 6 core files.

**User can narrow scope.** Examples:
- `"Follow memory bank"` → all core files + details
- `"Memory bank: activeContext only"` → just that file
- `"Consult memory bank, ignore references"` → core files, skip detail links
- `"Follow only memory bank in plans/"` → only that subdirectory

**If scope is unclear, ASK:**
```
"Should I consult:
  1) All memory bank files (default)
  2) Specific files: [suggest based on context]
  3) Skip for this task"
```

### Updates
Update memory bank when:
- Discovering new patterns or decisions
- After significant changes
- User requests "update memory bank"

When updating: review all core files, offload to `details/` if any exceed ~300 words, update `activeContext.md` and `progress.md`.

**Detail file naming:** `details/{prefix}_{category}_{name}.md`
Prefixes: `pb_`, `pc_`, `sp_`, `tc_`, `ac_`, `pr_`
