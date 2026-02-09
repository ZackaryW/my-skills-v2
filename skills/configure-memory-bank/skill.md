# Configure Memory Bank

Supplementary reference for memory bank configuration. Consult `skill.json` first for goal and acceptance criteria.

---

## Initialization Protocol

### Trigger
- New project with no `memory-bank/` directory
- User requests memory bank setup
- Agent starts work and no memory bank exists

### Steps

1. Create `memory-bank/` at repo root (or at package level for monorepos)
2. Create all 6 core files using seed content from project context
3. Create `memory-bank/details/` directory (empty initially)
4. Populate each file following [Core File Specifications](#core-file-specifications)

### Seed Content Rules
- **Never create empty files** — each must have at least a heading and 2–3 bullets
- Derive content from: project README, package.json, existing docs, conversation context
- If no context available, use structured placeholders with `[TODO]` markers
- Mark the initialization in `progress.md`

---

## Core File Specifications

Each file has a defined purpose, required sections, and size limit (~300 words). Use bullets and tables over prose.

### projectbrief.md
**Purpose**: Foundation document — shapes all other files.

| Section | Content |
|---------|---------|
| Project Name | One-line identifier |
| Goal | What the project achieves (1–2 sentences) |
| Requirements | Bulleted list of core requirements |
| Constraints | Technical/business constraints |
| Success Criteria | How to know it's done |

### productContext.md
**Purpose**: Why the project exists and how it should work.

| Section | Content |
|---------|---------|
| Problem Statement | What problem this solves (1–2 sentences) |
| Target Users | Who uses this |
| User Experience Goals | What the experience should feel like |
| Key Workflows | One-line summaries of main flows |

### systemPatterns.md
**Purpose**: Architecture, technical decisions, and design patterns.

| Section | Content |
|---------|---------|
| Architecture | High-level structure (diagram or bullet list) |
| Key Patterns | Design patterns in use (name + one-line description each) |
| Technical Decisions | Decision + rationale (table format preferred) |
| Component Relationships | How major parts connect |

### techContext.md
**Purpose**: Technologies, setup, and development environment.

| Section | Content |
|---------|---------|
| Tech Stack | Language, framework, runtime versions |
| Dev Setup | Steps to get running (commands, env vars) |
| Dependencies | Key dependencies with purpose |
| Conventions | Naming, file structure, coding style rules |

### activeContext.md
**Purpose**: Current work snapshot — what's happening now.

| Section | Content |
|---------|---------|
| Current Focus | 1–3 items actively being worked on |
| Recent Changes | Last 3–5 changes (one-line each, newest first) |
| Next Steps | Prioritized list of upcoming work |
| Active Decisions | Open questions or choices pending resolution |
| Blockers | Anything preventing progress |

### progress.md
**Purpose**: Status tracking and decision history.

| Section | Content |
|---------|---------|
| Status | Overall project phase (e.g., "Phase 1: Foundation") |
| What Works | Features/components confirmed working |
| What's Left | Remaining work items |
| Known Issues | Bugs or limitations |
| Decision Log | Key decisions as table: Date | Decision | Rationale |

---

## Detail Offloading

### When to Offload
- Core file exceeds ~300 words
- A section contains deep technical detail beyond its one-line summary
- Historical content no longer needs prominence but should be preserved

### Naming Convention
```
details/{prefix}_{category}_{name}.md
```

**Prefixes** (one per core file):
| Core File | Prefix |
|-----------|--------|
| projectbrief.md | `pb_` |
| productContext.md | `pc_` |
| systemPatterns.md | `sp_` |
| techContext.md | `tc_` |
| activeContext.md | `ac_` |
| progress.md | `pr_` |

**Categories** (per file):
| Source | Categories |
|--------|-----------|
| projectbrief | `constraint`, `problem`, `requirement` |
| productContext | `problem`, `workflow`, `goalchange` |
| systemPatterns | `architecture`, `pattern`, `decision` |
| techContext | `setup`, `env`, `dependency` |
| activeContext | `focus`, `change`, `decision` |
| progress | `changelog`, `tasks`, `issues` |

### How to Offload
1. Extract detailed content from core file
2. Create detail file with full content and a `# Title` heading
3. Replace extracted content in core file with one-line summary + relative link:
   ```markdown
   - Auth pattern: JWT with role claims. See [details/sp_pattern_auth.md](details/sp_pattern_auth.md)
   ```

---

## Chained Memory Banks

For monorepos where packages share context but have local specifics.

### Structure
```
my-monorepo/
├── memory-bank/                    # Root: shared patterns
├── packages/
│   ├── api/memory-bank/            # Child: _chain.md → ../../memory-bank
│   └── web/memory-bank/            # Child: _chain.md → ../../memory-bank
```

### _chain.md
```markdown
parent: ../../memory-bank
```

### Resolution Order
1. Scan parent directories for `memory-bank/`
2. If found, create `_chain.md` with relative path
3. Read top-down: root → child
4. Child overrides parent on conflicts

### Scope Rules for Chained Banks
| Scope | Store At |
|-------|----------|
| Shared patterns, standards, cross-package | Root/ancestor |
| Package-specific details, local progress | Current |

When unclear, **ask the user**: "Store globally or locally?"

---

## Update Protocol

### When to Update
- After discovering new project patterns
- After implementing significant changes
- User requests "update memory bank"
- When context becomes stale or misleading

### What to Update
Always update:
- `activeContext.md` — current focus and recent changes
- `progress.md` — status and remaining work

Review and update if relevant:
- `systemPatterns.md` — new patterns or architecture changes
- `techContext.md` — new dependencies or setup changes
- `productContext.md` — goal or scope shifts
- `projectbrief.md` — rarely; only if fundamental requirements change

### How to Update
1. Read all 6 core files to get full picture
2. Update `activeContext.md` with current focus and recent changes
3. Update `progress.md` with current status
4. Review other files for accuracy — remove stale content
5. Check word counts — offload to `details/` if any file exceeds ~300 words
6. Ensure cross-file consistency (no contradictions)
