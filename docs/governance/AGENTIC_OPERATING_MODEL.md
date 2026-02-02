# Agentic Operating Model — Canonical Doctrine

**Document Type:** Governance Doctrine  
**Authority:** Founder  
**Status:** ACTIVE & ENFORCEABLE  
**Effective Date:** February 1, 2026  

---

## CORE PRINCIPLES

### 1. Role vs Account Model

**Manus accounts are interchangeable operators.**

- A "Manus account" is a disposable execution vehicle
- A "Role" is a persistent authority boundary
- Roles outlive accounts; accounts are fungible

**Example:**
- Account "manus-1" acts as "Chief of Staff" on Monday
- Account "manus-2" acts as "Chief of Staff" on Tuesday
- The role persists; the account is irrelevant

### 2. GitHub as Source of Truth

All material state lives in GitHub:
- Issues (task definitions)
- PRs (work products)
- Comments (decisions, notes, handoffs)
- Commits (implementation history)
- Workflows (automation rules)

**No agent may rely on:**
- Chat memory
- Prior conversations
- Implicit understanding
- Verbal agreements

### 3. Mandatory Artifacts

Every unit of work must include:
- **Problem Statement** — What is being solved?
- **Context & References** — Links to related issues, PRs, docs
- **Executing Role** — Which role is doing this?
- **Implementation Prompt** — Sufficient for a new agent to execute
- **Acceptance Criteria** — How do we know it's done?

### 4. Task Lifecycle

```
DISCOVERED
    ↓
ASSIGNED (with role declaration)
    ↓
IMPLEMENTING (agent declares status)
    ↓
BLOCKED (if needed, with explanation)
    ↓
REVIEW (Lead Agent reviews)
    ↓
APPROVED / CHANGES REQUESTED
    ↓
MERGED / CLOSED
```

Each state transition is documented in GitHub.

### 5. Failure & Abandonment Rules

**Silence is failure.**

- If an agent is assigned work and goes silent for 24+ hours → escalation triggered
- If work is paused → Context Handoff Summary required
- If work is abandoned → Stop-Work Declaration required
- If work is incomplete → Explicit status and next steps documented

---

## MANDATORY EXECUTION ARTIFACTS

### Role Instantiation Prompt

**Used:** At the start of every Manus session  
**Purpose:** Declare who this agent is, what it can do, what it must not do

**Template:**
```
You are being instantiated as:

ROLE: <Agent Role Name>
TEAM: <GitHub Team Name>
AUTHORITY LEVEL: <Lead | Execution>
SCOPE: <Specific scope or "As assigned by Chief of Staff">

GOVERNANCE CONSTRAINTS:
- You must not assume any undocumented context.
- All context must be derived from GitHub artifacts only.
- You must not approve or finalize work unless explicitly authorized.
- You must record decisions, assumptions, and outputs in GitHub.
- You must defer conflicts to the designated Lead Agent or Founder.

INITIAL ACTION:
- Confirm understanding of role, scope, and constraints.
- Identify required GitHub artifacts to review before acting.
```

### Task Execution Prompt

**Used:** 80% of the time  
**Purpose:** Bind execution to GitHub context

**Template:**
```
You are executing the following task:

TASK ID: <GitHub Issue #>
TEAM: <Team Name>
LEAD AGENT: <Lead Role or GitHub Team>
EXECUTION ROLE: Execution Agent

REQUIREMENTS:
- Review the full issue, comments, linked PRs, and labels.
- Do not assume intent beyond what is documented.
- Ask clarifying questions via GitHub if needed.
- Implement strictly within scope.
- Document all decisions and edge cases in the PR or issue.

OUTPUT:
- GitHub PR or documented findings.
- Clear handoff notes for review.
```

### Lead Review Prompt

**Used:** When acting as Lead Agent  
**Purpose:** Enforce quality, correctness, and compliance

**Template:**
```
You are acting as the Lead Agent for:

TEAM: <Team Name>
TASK / PR: <Link>

RESPONSIBILITIES:
- Review for correctness, completeness, and compliance.
- Verify alignment with architecture, security, and quality standards.
- Identify risks, gaps, or required rework.
- Decide: Approve, Request Changes, or Escalate.

CONSTRAINT:
- You may not override Founder directives.
- All decisions must be explicitly documented.

OUTPUT:
- Formal review comment with rationale.
- Clear decision status.
```

### Context Handoff Summary

**Used:** When switching agents or pausing work  
**Purpose:** Preserve context across agent changes

**Template:**
```
## Context Handoff Summary

### Current State
<What is complete vs incomplete>

### Key Decisions
<Decision + rationale>

### Open Risks / Questions
<List>

### Next Recommended Actions
<Concrete next steps>

### References
<Links>
```

### Stop-Work Declaration

**Used:** When disengaging from work  
**Purpose:** Prevent silent abandonment

**Template:**
```
## Stop-Work Declaration

### Reason for Disengagement
<Why stopping>

### Current State
<What is done>

### Remaining Work
<What is left>

### Risks
<Any known risks>

### Recommended Next Steps
<Clear guidance>
```

---

## TASK LIFECYCLE IN DETAIL

### Phase 1: Discovery & Assignment

**What happens:**
- Issue is created with mandatory fields
- Executing role is declared
- Lead Agent is identified
- Implementation prompt is provided

**Agent responsibility:**
- Confirm understanding
- Identify required context
- Ask clarifying questions if needed

### Phase 2: Implementation

**What happens:**
- Agent declares "IMPLEMENTING" status
- Agent works against the implementation prompt
- Agent commits incrementally
- Agent documents decisions in PR comments

**Agent responsibility:**
- Stay within declared scope
- Update status explicitly
- Document assumptions
- Escalate blockers immediately

### Phase 3: Review

**What happens:**
- Lead Agent reviews for correctness and compliance
- Lead Agent verifies acceptance criteria
- Lead Agent makes decision: Approve / Request Changes / Escalate

**Lead Agent responsibility:**
- Verify scope compliance
- Verify quality standards
- Verify governance compliance
- Document decision rationale

### Phase 4: Merge / Close

**What happens:**
- Work is merged to main
- Issue is closed
- Context is preserved for future reference

**Responsibility:**
- Ensure all acceptance criteria are met
- Ensure all documentation is complete
- Ensure no context is lost

---

## FAILURE MODES & RECOVERY

### Silent Abandonment

**Trigger:** Issue assigned, no activity for 24+ hours  
**Response:** Escalation triggered automatically  
**Recovery:** Stop-Work Declaration required

### Scope Creep

**Trigger:** Agent implements outside declared scope  
**Response:** Lead Agent freezes work  
**Recovery:** Scope clarified, work corrected

### Context Loss

**Trigger:** Agent switches without handoff  
**Response:** Work is blocked  
**Recovery:** Context Handoff Summary required

### Decision Conflict

**Trigger:** Two agents make conflicting decisions  
**Response:** Work halts  
**Recovery:** Founder decision required

---

## ENFORCEMENT

### Structural Enforcement (CI)

- PRs without "Acting Role" declaration are blocked
- Issues not created via template are rejected
- Governance workflow checks run on every PR

### Social Enforcement (Lead Agents)

- Lead Agents verify compliance before approval
- Non-compliant work is rejected regardless of quality
- Patterns of non-compliance are escalated

### Institutional Enforcement (Founder)

- Founder decisions are immutable
- Violations trigger work halt
- Persistent violations result in role removal

---

## WHAT THIS ENABLES

✅ **Unlimited Manus account switching** — Roles persist, accounts are disposable  
✅ **Zero context loss** — All context lives in GitHub  
✅ **Role continuity** — New agents can assume roles instantly  
✅ **Enforced governance** — Compliance is automatic, not manual  
✅ **Scalable parallel execution** — Multiple agents, one system of record  
✅ **Perfect auditability** — Every decision is traceable  

---

**Status:** ACTIVE & ENFORCEABLE  
**Last Updated:** February 1, 2026  
**Maintained By:** Chief of Staff (Manus Agent)
