# My Skills

> Goal-driven, test-validated skills for AI agents — inspired by agile user stories.

Define what you want to achieve (goal), how to measure success (acceptance criteria), and what features make it work. AI agents read the structure and execute accordingly.

## Quick Start

**1. Configure AI agent** — Copy [about.md](about.md) to your IDE's custom instructions:
   - **VS Code (GitHub Copilot)**: Settings → GitHub Copilot → Custom Instructions
   - **Cursor**: Settings → Cursor Settings → Rules for AI
   - **Cline/Other**: Add as custom instruction or system prompt

**2. Set environment variable** (choose one):

```powershell
# Windows PowerShell - direct path
$env:MY_SKILLS_REPO = "C:\path\to\my-skills-v2"

# OR - parent directory (repo name auto-resolved)
$env:SKILLS_GROUP_DIR = "C:\path\to\skills"
```

```bash
# macOS/Linux - direct path
export MY_SKILLS_REPO="/path/to/my-skills-v2"

# OR - parent directory
export SKILLS_GROUP_DIR="/path/to/skills"
```

**3. Use a skill** — tell your AI agent:

```
use-skill/list
```

```
use-skill/configure-memory-bank
```

**4. Create your first skill**:

```bash
mkdir skills/my-skill
cp templates/skill.json skills/my-skill/
# Edit skill.json with your goal, criteria, and features
```

## What is a Skill?

A skill is a JSON file that describes:
- **Goal** — what it achieves
- **Acceptance Criteria** — how to measure success
- **Features** — testable components with expected results

Each feature follows the **Given-When-Then** pattern for validation.

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
      "optional": false
    }
  ]
}
```

See [examples/hello-world](examples/hello-world) for a complete working example.

## Built-in Skills

### Core Skills

| Skill | Usage | Description |
|-------|-------|-------------|
| **use-skill/list** | `use-skill/list` | List all available skills with goals |
| **use-skill/find** | `use-skill/find {query}` | Search skills by name or keyword |
| **use-skill/update** | `use-skill/update` | Pull latest changes from git remote |
| **use-skill/create-repo** | `use-skill/create-repo` | Create new skills repository with V2 structure |

### Memory Bank Skills

| Skill | Usage | Description |
|-------|-------|-------------|
| **configure-memory-bank** | `use-skill/configure-memory-bank` | Initialize memory bank structure with all core files |
| **cleanup-memory-bank** | `use-skill/cleanup-memory-bank` | Maintain memory bank quality (keep core files under 300 words) |

### Development Skills

| Skill | Usage | Description |
|-------|-------|-------------|
| **dev/focus-boundary** | `use-skill/dev/focus-boundary` | Control AI autonomy and creative freedom (3 levels) |
| **dev/std-dev-impl** | `use-skill/dev/std-dev-impl` | Structured 5-phase TDD implementation protocol |

## How It Works

**1. Skill Discovery** — AI agent resolves skill path using `use-skill/{name}`:
   - Exact match: `skills/{name}/skill.json`
   - Partial match: `skills/*{name}*/skill.json`
   - Sub-skills: `skills/{parent}/{name}/skill.json`

**2. Skill Invocation** — Agent reads `skill.json`:
   - Understands the **goal** and **acceptance criteria**
   - Executes **required features** (`optional: false`)
   - Applies **optional features** when referenced or contextually relevant
   - Validates against **expected results**

**3. Feature Extensions** — Features can reference:
   - **Scripts** — `ext.script: "script.py"` (execute file)
   - **Documentation** — `ext.skill_md_ref: "#header"` (consult skill.md)
   - **Sub-skills** — `ext.subskill: "sub-skill-name"` (delegate to nested skill)

## Repository Structure

```
my-skills-v2/
├── README.md                   # This file
├── about.md                    # AI agent instructions
├── templates/                  # Boilerplate for new skills
├── examples/                   # Reference implementations
├── memory-bank/                # Project context (optional)
└── skills/                     # Your skills
    ├── use-skill/              # Core: discovery & invocation
    ├── configure-memory-bank/  # Initialize memory bank
    ├── cleanup-memory-bank/    # Maintain memory bank
    └── dev/                    # Development methodology
        ├── focus-boundary/
        └── std-dev-impl/
```

## Advanced: skill.json Reference

### Full Schema

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

### Feature Optionality

| Value | Behavior | Use Case |
|-------|----------|----------|
| `optional: false` | Always applies | Core feature required for skill to work |
| `optional: true` | Applies when referenced or contextually relevant | Conventions, preferences, context-dependent behavior |

### Extension Priority

When multiple extensions are defined, the order of precedence is:
1. **subskill** — Delegates to nested skill (owns feature implementation)
2. **script** — Executes script file
3. **skill_md_ref** — Consults documentation section

## Contributing

1. Create skill directory: `mkdir skills/your-skill`
2. Copy template: `cp templates/skill.json skills/your-skill/`
3. Define goal, criteria, and features
4. Test with AI agent
5. Add documentation in `skill.md` (optional)
6. Add scripts if needed (optional)

## Resources

- [examples/hello-world](examples/hello-world) — Complete working example
- [templates/](templates/) — Boilerplate for new skills
- [about.md](about.md) — Full instruction file for AI agents
- [memory-bank/](memory-bank/) — Project documentation and context
