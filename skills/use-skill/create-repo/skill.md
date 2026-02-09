# create-repo

Create a new goal-driven skills repository with V2 structure.

## Validation
Validates input parameters:
- Repository name (kebab-case format)
- Target path (exists or can be created)
- No existing repository at path

## Structure
Creates complete directory structure:
```
{repo-name}/
├── about.md
├── README.md
├── memory-bank/
│   ├── projectbrief.md
│   ├── productContext.md
│   ├── systemPatterns.md
│   ├── techContext.md
│   ├── activeContext.md
│   └── progress.md
├── templates/
│   ├── skill.json
│   ├── skill.md
│   └── script.ps1 (or .sh, .py)
├── examples/
│   └── hello-world/
└── skills/
```

## about.md File
Generates instruction file with:
- YAML frontmatter (`applyTo`, `priority`)
- Path resolution via environment variables
- Repository structure overview
- skill.json schema documentation
- Skill discovery and invocation protocol
- Memory bank configuration

## README File
Generates user-facing documentation with:
- Repository description
- Core concept explanation
- Quick start guide
- Environment variable setup
- Structure overview

## Memory Bank
Initializes all 6 core memory bank files:
- **projectbrief.md** — Scope, goals, requirements
- **productContext.md** — Why it exists, how it works
- **systemPatterns.md** — Architecture, patterns
- **techContext.md** — Technologies, setup
- **activeContext.md** — Current focus, recent changes
- **progress.md** — Status tracking

## Templates
Creates boilerplate files for new skills:
- skill.json template with full schema
- skill.md template with documentation structure
- Script templates (platform-specific)

## Examples
Optional: Creates hello-world example skill demonstrating V2 pattern.

## Environment Variables
Documents two-variable pattern in generated files:
- `${REPO_NAME_UPPERCASE}_SKILLS_REPO` — Direct path
- `${SKILLS_GROUP_DIR}` — Parent directory

## Usage
```
use-skill/create-repo
```

Agent will prompt for:
- Repository name
- Target path
- Priority level (HIGHEST/HIGH/NORMAL/LOW)
- Whether to include example skill
