# Founder Decision Conflict Rules

These rules govern how conflicts between decisions are detected, escalated, and resolved.

---

## What Counts as a Conflict

A decision conflict exists if:

1. **Contradictory Decisions** — A new decision contradicts an invariant enforced by an earlier decision
2. **Scope Overlap** — Two decisions apply to the same scope with incompatible outcomes
3. **Invariant Violation** — A PR violates the enforcement rules of an active decision
4. **Ambiguous Authority** — Two roles claim authority over the same decision

---

## Core Conflict Rules

### Rule 1: Decisions Do Not Implicitly Override Each Other

A newer decision does NOT override an older one unless it explicitly references it.

**Example:**
- FD-2026-001 requires offline-first
- FD-2026-002 (hypothetical) cannot silently make online-only features acceptable
- If FD-2026-002 wants to change this, it must explicitly reference FD-2026-001

### Rule 2: Invariants Trump Features

If a feature conflicts with an invariant, the feature is invalid unless the invariant is explicitly modified by a Founder Decision.

**Example:**
- INV-010 requires offline-first
- A feature that requires real-time connectivity violates INV-010
- The feature is blocked until a new Founder Decision modifies INV-010

### Rule 3: Ambiguity Is a Hard Stop

If agents disagree on interpretation of a decision or invariant:
- Work stops immediately
- Escalation is mandatory
- No assumptions are allowed
- Founder clarification is required

### Rule 4: Conflict Resolution Requires a New Decision

Conflicts are resolved ONLY by:
- A new Founder Decision (FD-YYYY-NNN)
- Explicit supersession section that references the conflicting decision
- No workarounds or informal resolutions

---

## Conflict Detection Workflow

### Step 1: Detection

Conflicts are detected by:
- CI governance checks (automated)
- Lead Agent review (manual)
- Security Agent review (manual)
- Quality Agent review (manual)

### Step 2: Classification

Conflicts are classified as:
- **Level 1 (Minor)** — Clarification needed, work can proceed with caution
- **Level 2 (Major)** — Work must halt, Founder decision required
- **Level 3 (Critical)** — Immediate escalation to Founder

### Step 3: Escalation

1. Agent flags conflict in GitHub issue/PR
2. Status set to: `BLOCKED-GOVERNANCE`
3. Founder Decision Request issue created
4. Work halts until decision logged

### Step 4: Resolution

1. Founder issues new decision (FD-YYYY-NNN)
2. Decision explicitly references conflicting decision
3. New decision is logged
4. Work resumes under new decision

---

## Conflict Resolution Template

When a conflict is detected, create a Founder Decision Request with:

**Title:** `FDR: Resolve Conflict Between [Decision 1] and [Decision 2]`

**Body:**
```
## Conflicting Decisions
- FD-YYYY-NNN: [Description]
- FD-ZZZZ-MMM: [Description]

## Nature of Conflict
[Explain how they conflict]

## Affected Work
- Issue: #XXX
- PR: #YYY

## Options
**Option A:** [Modify first decision]
- Pros: ...
- Cons: ...

**Option B:** [Modify second decision]
- Pros: ...
- Cons: ...

## Recommendation
[Agent recommendation, if any]
```

---

## Examples of Conflicts

### Example 1: Offline-First vs Online-Only Feature

**Conflict:**
- INV-010 requires offline-first
- Feature X requires real-time connectivity

**Resolution:**
- Option A: Redesign Feature X to work offline
- Option B: Create Founder Decision to modify INV-010
- Option C: Remove Feature X from scope

### Example 2: Two Decisions on Same Topic

**Conflict:**
- FD-2026-001 requires GitHub-only context
- FD-2026-003 (hypothetical) allows external documentation

**Resolution:**
- FD-2026-003 must explicitly reference FD-2026-001
- FD-2026-003 must explain why external documentation is now acceptable
- If FD-2026-003 doesn't exist, FD-2026-001 remains authoritative

### Example 3: Role Authority Ambiguity

**Conflict:**
- Execution Agent claims authority to approve work
- Quality Agent claims authority to approve work

**Resolution:**
- Founder Decision Request created
- Founder clarifies authority boundaries
- New decision issued (FD-YYYY-NNN)
- Authority is now explicit

---

## Enforcement

**Governance Workflow** automatically detects conflicts:
- Multiple FD-YYYY-NNN references in a single PR
- References to modified invariants
- Contradictory statements in decision text

**Lead Agents** manually verify:
- Scope conflicts
- Authority ambiguities
- Interpretation disagreements

**Founder** resolves:
- All escalated conflicts
- All ambiguities
- All authority disputes

---

## Escalation Triggers

Work is immediately escalated if:

1. **Conflicting Decisions Detected** — Two decisions apply with incompatible outcomes
2. **Invariant Violation** — Work violates an enforced invariant
3. **Decision Missing** — Required decision does not exist
4. **Ambiguous Authority** — Unclear who has authority
5. **Interpretation Disagreement** — Agents disagree on decision meaning

---

**Last Updated:** 2026-02-01  
**Maintained By:** Chief of Staff (Manus Agent)
