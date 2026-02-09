# Active Context

## Current Focus
Completed migration of 3 core skills from V1 to V2 architecture: use-skill/create-repo for repository scaffolding, and dev parent skill with focus-boundary and std-dev-impl sub-skills for development protocols.

## Recent Changes
- **Migrated** 3 V1 skills to V2 architecture
  - `use-skill/create-repo` — scaffolds new skills repositories with V2 structure (about.md, memory-bank/, templates/, examples/, skills/)
  - `dev` parent skill — organizes development methodology skills
  - `dev/focus-boundary` — controls AI autonomy with 3 levels (full, minimal+constrained, minimal+unrestricted)
  - `dev/std-dev-impl` — 5-phase TDD protocol (Understand → Clarify [GATE] → Design [GATE] → Implement → Validate)
- **Updated** documentation to reflect new skills
  - Added `use-skill/create-repo` to resolution examples in use-skill/skill.md
  - Added `dev` section to README Built-in Skills
  - Updated memory bank with completion status
- **Migrated** `cleanup-memory-bank` skill from V1
  - Restructures memory bank files to keep core files under 300 words
  - Offloads detailed content to details/ subdirectory
  - Uses structured naming convention for detail files
  - Applies concise writing style rules
  - Validates cleanup with comprehensive checklist
- **Added** `use-skill/update` sub-skill
  - Resolves repo path via environment variables
  - Detects git repositories
  - Pulls updates for single repo or skills group
  - Detects about.md changes and notifies user to refresh context
  - Cross-platform support: PowerShell (Windows) and bash (Unix/Linux/Mac)
  - Includes both script.ps1 and script.sh implementations
- **Genericized** documentation across all files
  - Changed "my-skills-v2" to "skills repo", "{repo-name}", "skills-repo" in examples
  - Removed V1/V2 comparison language (now "Common Issue" instead of "V1 Limitation")
  - Changed "My Skills V2" header to "Goal-Driven Skills Repository"
  - Updated paths in examples to use generic names
  - Changed "Backward Compatibility" to "AI Integration" (more forward-looking)
  - Made systemPatterns.md note that `use-skill` is available in any repo following this pattern
- **Fixed** about.md ambiguity — clarified that memory bank should be consulted when working **on** the repo (development), not when merely **using** skills
  - Removed "MANDATORY FIRST STEP: Before ANY task" (too broad)
  - Added clear distinction: repo development vs. skill invocation
- **Added** `ext.subskill` key — features can now delegate to sub-skill directories
  - Priority: `subskill` > `script` > `skill_md_ref`
  - Sub-skill owns the feature’s implementation when set
- *Validate new skills through real usage
2. Consider creating scripts for use-skill/create-repo (currently agent-driven)
3. Test dev/focus-boundary with different levels
4. Test dev/std-dev-impl full workflow
5. Continue migrating additional V1 skills as neededal match → ambiguous → not found
- **Created** `configure-memory-bank` — detailed memory bank initialization and maintenance
- **Updated** path resolution to pure env var-based (removed explicit path option)
- **Eliminated** conditions/, conventions/, scripts/ — everything is a skill

## Next Steps
1. Test `cleanup-memory-bank` with actual memory bank files
2. Test `use-skill/update` with actual git repositories
3. Create additional utility skills as needed
4. Validate `use-skill` resolution through real usage

## Active Decisions
- ✅ Everything is a skill (no conditions/conventions/scripts dirs)
- ✅ Features have `optional` flag (replaces conditions/conventions)
- ✅ skill.json is the single source of truth per skill
- ✅ skill.md is supplementary only (concise, never duplicates skill.json)
- ✅ Nested skills for composition
- ✅ Built-in memory bank with scope rules
- ✅ Parent-child arch via env vars ($MY_SKILLS_REPO, $SKILLS_GROUP_DIR)
- ✅ `ext.subskill` key for delegating features to sub-skill directories
- ✅ Extension priority: `subskill` > `script` > `skill_md_ref`
- ✅ `use-skill` is reserved core skill (discovery + invocation)
- ✅ `use-skill/{name}` syntax with resolution order: sub-skill → exact → partial → ambiguous → fail
- ⏳ Automated test execution (manual first)

## Key Patterns
- Goal → Acceptance Criteria → Features (required + optional) → Test Scenarios → Expected Results
- Given-When-Then for test scenarios
- Agent asks for memory bank scope when unclear
- Cross-platform scripts: provide both .ps1 and .sh for OS-agnostic skills

## Context, invocation layer, utilities, and development protocols complete. Core skills: `use-skill` (discovery/resolution/invocation with list/find/update/create-repo sub-skills), `configure-memory-bank`, `cleanup-memory-bank`, and `dev` (focus-boundary for autonomy control, std-dev-impl for TDD protocol). Documentation generic and template-ready. Repository can scaffold new skill repos. Next: validation through real projects and continued V1 migration
Foundation & invocation layer complete. Documentation now generic and template-ready. Core utility skills in place: `use-skill` provides discovery, resolution, and invocation with three sub-skills (list, find, update). `configure-memory-bank` provides detailed memory bank setup instructions. `cleanup-memory-bank` maintains memory bank quality by offloading details and enforcing concise writing. Repo can serve as template for other skill repositories. Next: real-world validation and additional production skills.
