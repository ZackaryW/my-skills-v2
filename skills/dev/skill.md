# dev

Development methodology and protocol skills.

This parent skill organizes sub-skills that control AI behavior during development tasks.

## Sub-Skills

### focus-boundary
Controls AI autonomy and creative freedom. Three levels:
- **Level 0** — Full autonomy (make assumptions, add extras)
- **Level 1** — Minimal + File-Constrained (zero assumptions, minimal files)
- **Level 2** — Minimal + File-Unrestricted (zero assumptions, unlimited files)

### std-dev-impl
Structured 5-phase TDD implementation protocol:
1. **Understand** — Build context via memory bank
2. **Clarify** — Ask questions, confirm TDD [GATE]
3. **Design** — Propose approaches, get approval [GATE]
4. **Implement** — TDD cycle (tests → code → verify → update)
5. **Validate** — Compare to goals, handle divergence

## Usage

Invoke sub-skills via partial match:
```
use-skill/focus-boundary
use-skill/std-dev-impl
```

Or full path:
```
use-skill/dev/focus-boundary
use-skill/dev/std-dev-impl
```
