# focus-boundary

Control AI autonomy and creative freedom during development tasks.

## Overview

Focus boundary defines how much creative freedom and proactive behavior the AI should use. Three levels control assumptions, file scope, and extras.

## Focus Levels

| Level | Assumptions | File Scope | Extras |
|-------|-------------|------------|--------|
| **0** | Make reasonable assumptions | Unlimited files | Add proactively |
| **1** | Zero assumptions — ask first | Minimal files only | Ask before adding |
| **2** | Zero assumptions — ask first | Create as needed | No unrequested additions |

## Level 0: Full Autonomy

**When to use:** Prototyping, exploration, experienced developer wanting maximum productivity

**Behavior:**
- Make reasonable assumptions when requirements are clear
- Create any files that would improve the solution
- Add helper classes, abstractions, utilities proactively
- Include documentation, examples, tests without asking
- Use standard patterns and best practices automatically

**Example:** "Add authentication" → Agent creates auth service, middleware, guards, types, tests, and updates affected modules

## Level 1: Minimal + File-Constrained

**When to use:** Precise control needed, modifying legacy code, surgical changes only

**Behavior:**
- Make ZERO assumptions — ask about any ambiguity
- Create minimal number of files (preferably single file)
- Do NOT add: helpers, abstractions, extra patterns, documentation
- Stop and ask before deviating from exact request
- Interpret requests literally

**Example:** "Add authentication" → Agent asks: Which file? What type (JWT/session/OAuth)? Which routes? Then modifies only specified file.

## Level 2: Minimal + File-Unrestricted

**When to use:** Well-defined requirements, allow necessary structure, no bells and whistles

**Behavior:**
- Make ZERO assumptions — ask about any ambiguity
- Create necessary files (services, types, tests as required)
- Do NOT add: unrequested abstractions, helper classes, documentation beyond necessities
- Follow standard architecture patterns
- No extras unless requested

**Example:** "Add authentication" → Agent asks: JWT or session? Which routes? Then creates auth service, middleware, types as needed — no example code or advanced patterns.

## Stop and Ask Conditions

For focus levels 1 and 2, agent MUST stop and ask when:
- Destination file/location is not specified or unclear
- Requirements are vague or open-ended
- Would add patterns, abstractions, or utilities not explicitly requested
- Multiple reasonable implementation approaches exist
- Any ambiguity in scope or behavior

## Do Not Add (Levels 1 & 2)

Unless explicitly requested, do NOT create:
- Helper classes or utilities
- Complex abstractions or design patterns
- Registry patterns or factories
- Example files or demo code
- Documentation beyond code comments
- Configuration beyond minimal
- Test utilities or fixtures (tests themselves are OK if requested)

## Default (No Level): Balanced

When no focus level is specified:
- Make reasonable assumptions when requirements are clear
- Use standard patterns appropriate to codebase
- Ask when truly ambiguous
- Add documentation and tests following project conventions
- Balance thoroughness with directness

## Usage

Specify focus level in your request:
```
focus:0 — Add user authentication
focus:1 — Add validateEmail function to utils.ts
focus:2 — Implement shopping cart feature
```

Or invoke skill explicitly:
```
use-skill/focus-boundary
```

Then specify desired level: 0, 1, or 2.
