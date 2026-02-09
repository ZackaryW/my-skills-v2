# std-dev-impl

Structured 5-phase TDD implementation protocol with user collaboration gates.

## Core Principles

1. **Test-Driven Development (TDD)** — Tests before implementation
2. **Collaborative Clarification** — Ask questions, don't assume
3. **Iterative Alignment** — Continuous requirement comparison
4. **Transparent Decision-Making** — Present options, explain trade-offs

## Process Flow

```
Understand → Clarify → [GATE] → Design → [GATE] → Implement → Validate
```

Two user gates prevent proceeding without confirmation.

---

## Phase 1: Understand

**Goal:** Build comprehensive context about the project and requirements.

**Activities:**
1. Read memory bank files (projectbrief, productContext, systemPatterns, techContext)
2. Understand existing codebase structure and conventions
3. Identify requirements and acceptance criteria
4. Create or update memory bank if missing/outdated

**Outputs:**
- projectbrief.md — Scope, goals, requirements
- productContext.md — Why it exists, how it should work
- techContext.md — Technologies, setup, constraints
- systemPatterns.md — Architecture, patterns, decisions

**When to update:** If files don't exist or are significantly out of date.

---

## Phase 2: Clarify

**Goal:** Resolve all ambiguities before design.

**Activities:**
1. Present questions to user about unclear requirements
2. Confirm understanding of what user wants
3. Verify TDD is appropriate for this task
4. Document clarifications in activeContext.md

**Critical Questions:**
- What is the expected behavior? (happy path)
- What edge cases should be handled?
- What should happen on errors?
- Are there performance/security constraints?
- Should this integrate with existing patterns?

**Outputs:**
- activeContext.md — Current focus, recent decisions, clarified requirements

### Gate: Clarify to Design

**DO NOT PROCEED** until user confirms:
✓ All questions answered
✓ Requirements are clear
✓ TDD approach is confirmed

---

## Phase 3: Design

**Goal:** Present solution approaches and get user approval.

**Activities:**
1. Propose 2-3 different implementation approaches
2. Present trade-offs for each:
   - Complexity vs Maintainability
   - Performance vs Readability
   - Short-term expedience vs Long-term flexibility
3. Recommend one approach with rationale
4. Wait for user feedback

**Output Format:**
```
Approach 1: [Name]
  Pros: ...
  Cons: ...
  Trade-offs: ...

Approach 2: [Name]
  Pros: ...
  Cons: ...
  Trade-offs: ...

Recommendation: Approach [X] because [rationale]
```

### Gate: Design to Implement

**DO NOT PROCEED** until user:
✓ Reviews approaches
✓ Provides feedback or questions
✓ Approves selected approach

---

## Phase 4: Implement

**Goal:** Implement using TDD cycle per component.

### TDD Cycle

For each component:

**1. Write Failing Tests**
- Happy path test
- Edge case tests
- Error condition tests
- Choose test type: Unit (isolated), Integration (interactions), Composite (full workflow)

**2. Implement Minimum Code**
- Write simplest code to pass tests
- Keep it idiomatic and clear
- Avoid over-engineering

**3. Verify Compliance**
- Run tests (all should pass)
- Check against requirements
- Verify adherence to systemPatterns
- Refactor for quality if needed

**4. Update Progress**
- Document what was completed in progress.md
- Note any challenges or decisions

Repeat cycle for each component until feature complete.

### Test Categories

- **Unit Tests** — Isolated component testing
- **Integration Tests** — Component interaction testing
- **Composite Tests** — Complete workflow testing

Choose based on component scope and dependencies.

---

## Phase 5: Validate

**Goal:** Ensure implementation matches initial requirements.

**Activities:**
1. Review initial requirements and acceptance criteria
2. Compare implementation to original goals
3. Identify divergences (if any)
4. Handle based on severity

### Divergence Handling

| Severity | Definition | Action |
|----------|------------|--------|
| **None** | Perfect match | Mark complete, inform user |
| **Minor** | Small deviation, core intact | Discuss with user, accept or adjust |
| **Major** | Significant mismatch | Full discussion, may restart from Phase 1 |

### Validation Checklist

Before marking complete:
- [ ] All tests pass
- [ ] Matches systemPatterns
- [ ] No undocumented deviations from requirements
- [ ] Memory bank updated (progress.md)
- [ ] User confirms implementation meets expectations

---

## Anti-Patterns (Avoid These)

❌ **Coding Before Clarifying** — Implementing with unanswered questions
❌ **Implementation Before Tests** — Writing code before tests
❌ **Gate Jumping** — Proceeding without user confirmation at gates
❌ **Ignoring Divergence** — Not comparing to requirements at end
❌ **Undocumented Assumptions** — Making decisions without asking or documenting
❌ **Over-Engineering** — Adding complexity beyond requirements

---

## Restart Conditions

Restart from Phase 1 if:
- Requirements change fundamentally during implementation
- Major technical blockers emerge that invalidate design
- User requests re-scoping
- Validation reveals irreconcilable divergence

---

## Usage

Invoke when implementing new features:
```
use-skill/std-dev-impl
```

Then provide feature request or requirement description.

Agent will guide through all 5 phases with gates.

---

## Quick Reference

| Phase | Key Activity | Output | Gate |
|-------|--------------|--------|------|
| 1. Understand | Read/create memory bank | Context files | No |
| 2. Clarify | Ask questions | activeContext.md | **✓ User confirms** |
| 3. Design | Propose approaches | Design options | **✓ User approves** |
| 4. Implement | TDD cycle | Code + tests | No |
| 5. Validate | Compare to requirements | Divergence assessment | No |
