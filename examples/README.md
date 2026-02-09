# Skills V2 Examples

This directory contains example skills demonstrating the V2 architecture.

## Available Examples

### hello-world
A simple greeting skill that demonstrates:
- Goal-driven structure
- Acceptance criteria
- Multiple features with test scenarios
- Optional skill.md for detailed documentation
- Script integration via ext.script
- Documentation references via ext.skill_md_ref

**Files:**
- `skill.json` - Core skill definition with goal, criteria, and features
- `skill.md` - Complementary documentation with detailed usage
- `script.py` - Executable Python implementation

**Usage:**
```bash
# Basic greeting
python examples/hello-world/script.py Alice

# Time-based greeting
python examples/hello-world/script.py Bob --time

# Custom message
python examples/hello-world/script.py Charlie --message "Welcome"
```

## Testing Examples

Each example includes test scenarios in skill.json. To validate:

1. Read the `test_scenario` for each feature
2. Execute the scenario as described
3. Verify the `expected_result` matches actual output

## Creating Your Own Skill

Use the templates in `/templates` as a starting point:

```bash
# Copy template
cp templates/skill.json skills/my-new-skill/skill.json
cp templates/skill.md skills/my-new-skill/skill.md

# Edit to define your skill
# - Set clear goal
# - Define acceptance criteria
# - Create features with test scenarios
# - Add optional script if needed
```
