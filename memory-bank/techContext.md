# Tech Context

## Technologies
- **Documentation**: Markdown
- **Metadata**: JSON (skill.json)
- **Scripts**: PowerShell (.ps1), bash (.sh), Python (.py)
- **Version Control**: Git
- **Memory System**: Cline Memory Bank (built-in)

## Environment Variables

```powershell
# Windows
$env:MY_SKILLS_REPO = "C:\path\to\skills-repo"
$env:SKILLS_GROUP_DIR = "C:\path\to\skills"
```
```bash
# Unix/Mac
export MY_SKILLS_REPO="/path/to/skills-repo"
export SKILLS_GROUP_DIR="/path/to/skills"
```

## Tool Integration
- **Editor**: VS Code
- **AI Assistants**: Claude (Cline), GitHub Copilot
- **Version Control**: Git
- **Testing**: Manual validation against test scenarios

## Conventions
- Skill names: kebab-case (`my-skill-name`)
- All skills must have `skill.json`
- skill.md is always optional and concise
- Features use Given-When-Then for test scenarios
- `optional: true` replaces V1 conditions/conventions
- No separate scripts/, conditions/, or conventions/ directories
- Scripts are integrated into skills via `ext.script`

## File Formats

### skill.json (Required)
```json
{
  "goal": "string",
  "acceptance_criteria": ["string"],
  "features": [
    {
      "name": "string",
      "test_scenario": "string",
      "expected_result": "string",
      "optional": false,
      "ext": { "script": "string", "skill_md_ref": "string" }
    }
  ]
}
```

### skill.md (Optional)
- Referenced via `skill_md_ref` in skill.json
- Concise supplementary content only (2-5 lines per section)

### Scripts (Optional)
- Referenced via `ext.script` in features
- `.ps1` (PowerShell - Windows), `.sh` (bash - Unix/Linux/Mac), `.py` (Python - all platforms) supported
- For cross-platform skills, provide both .ps1 and .sh versions

## Dependencies
- Minimal external dependencies
- Python standard library preferred
- No heavy frameworks unless justified

## Future Considerations
- Automated test execution
- Skill validation tooling
- Cross-referencing between skills
