# Use Skill

Reserved core skill for skill discovery, resolution, and invocation.

---

## Skill Resolution

### Invocation Syntax
```
use-skill/{name}
```

### Resolution Order
1. **Repo resolution** — resolve repo root via env vars (`$MY_SKILLS_REPO` or `$SKILLS_GROUP_DIR/{repo-name}`)
2. **Sub-skill check** — if `{name}` matches a use-skill sub-skill (`list`, `find`, `update`, `create-repo`), route there
3. **Skill search** — search `skills/` for a directory matching `{name}`:
   - Exact match: `skills/{name}/` → use directly
   - Partial match: `skills/*{name}*/` → use if single result
   - Multiple matches: present options to user
   - No match: fail with available suggestions

### Examples
| Input | Resolves To |
|-------|-------------|
| `use-skill/list` | Sub-skill: `use-skill/list/` |
| `use-skill/find` | Sub-skill: `use-skill/find/` |
| `use-skill/update` | Sub-skill: `use-skill/update/` |
| `use-skill/create-repo` | Sub-skill: `use-skill/create-repo/` |
| `use-skill/hello-world` | `examples/hello-world/` (exact) |
| `use-skill/memory-bank` | `skills/configure-memory-bank/` (partial match) |

---

## Routing Priority

Order matters. First match wins:, `create-repo`
1. **Sub-skill** — `list`, `find`, `update` (reserved names under use-skill)
2. **Exact skill match** — `skills/{name}/skill.json` exists
3. **Partial skill match** — single `skills/*{name}*/skill.json`
4. **Ambiguous** — multiple matches → ask user to clarify
5. **Not found** — fail, suggest `use-skill/list` or `use-skill/find`

---

## Invocation Protocol

Once a skill is resolved:
1. Read `skill.json` → understand goal, acceptance criteria, features
2. Execute required features (`optional: false` or omitted)
3. Check optional features → apply if user referenced or contextually relevant
4. If `ext.script` → execute the script
5. If `ext.skill_md_ref` → consult that section in skill.md
6. Validate against `expected_result`
