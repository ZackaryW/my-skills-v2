# cleanup-memory-bank

Restructure memory bank files to maintain clarity and efficiency by keeping core files under 300 words.

## File Analysis
Count words in each core memory bank file to identify those exceeding 300 words:
- projectbrief.md, productContext.md, systemPatterns.md
- techContext.md, activeContext.md, progress.md

## Content Identification
For files over 300 words, identify sections suitable for offloading:
- Detailed constraints, workflows, architectures
- Extended explanations, examples, change history
- Setup procedures, completed tasks

## Detail Files
Offload detailed content to `memory-bank/details/` using naming convention:

**Format**: `{prefix}_{category}_{name}.md`

**Prefixes**:
- `pb_` — projectbrief.md
- `pc_` — productContext.md
- `sp_` — systemPatterns.md
- `tc_` — techContext.md
- `ac_` — activeContext.md
- `pg_` — progress.md

**Categories by file**:
- **projectbrief**: constraint, problem
- **productContext**: problem, workflow, goalchange
- **systemPatterns**: architecture, pattern
- **techContext**: envSetup, setupChanges
- **activeContext**: focusChange, recentChange
- **progress**: changelog, tasks

## One-Line Mentions
Replace detailed content with concise one-line mentions linking to detail files:

**Example**:
```markdown
Authentication: JWT-based with user ID and role claims. See [details/sp_pattern_authentication.md](details/sp_pattern_authentication.md) for flow.
```

## Writing Style
Apply concise writing during cleanup:
- Use bullet points over paragraphs
- Remove filler words ("basically", "essentially", "in order to")
- Use active voice
- Tables for structured data
- Combine related points
- Eliminate non-critical examples

## Redundancy
Remove duplicate information across files:
- Consolidate overlapping content
- Maintain single source of truth
- Ensure cross-file consistency
- Link instead of repeating

## Validation
Post-cleanup checklist:
- ✓ All core files ≤ 300 words
- ✓ Essential context preserved
- ✓ Detail files properly organized
- ✓ All links functional
- ✓ No redundancy
- ✓ Concise language throughout
- ✓ Clear hierarchy maintained

## When to Run
Trigger cleanup when:
- Core files approaching or exceeding 300 words
- After major feature implementation
- During project phase transitions
- Context becomes difficult to navigate
