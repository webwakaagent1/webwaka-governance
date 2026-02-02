# Governance Escalation Protocol

This protocol defines when work must halt, how escalations are triggered, and how they are resolved.

---

## Escalation Trigger Conditions

Work is immediately escalated (status: BLOCKED-GOVERNANCE) if:

| Trigger | Severity | Action |
|---------|----------|--------|
| Conflicting Founder Decisions | Level 2 | Create FDR, halt work |
| Invariant Violation | Level 2 | Flag in PR, halt work |
| Decision Missing | Level 2 | Create FDR, halt work |
| Ambiguous Authority | Level 2 | Create FDR, halt work |
| Interpretation Disagreement | Level 2 | Create FDR, halt work |
| Security Risk | Level 3 | Immediate Founder notification |
| Critical Blocker | Level 1 | Notify Lead Agent |

---

## Escalation Steps

### Step 1: Detection & Flagging

When a trigger condition is detected:

1. Agent flags the issue in GitHub (issue or PR comment)
2. Clearly state the trigger condition
3. Provide all relevant context and links
4. Propose potential resolutions (if applicable)

**Example comment:**
```
⚠️ GOVERNANCE ESCALATION

**Trigger:** Invariant Violation (INV-010: Offline-First)

**Issue:** This feature requires real-time connectivity, which violates INV-010.

**Affected:** Issue #123, PR #456

**Required:** Founder Decision to either:
1. Redesign feature for offline-first
2. Modify INV-010 (not recommended)
3. Remove feature from scope

**Recommendation:** Redesign for offline-first
```

### Step 2: Status Update

Update the issue/PR status to: `BLOCKED-GOVERNANCE`

Add labels:
- `governance`
- `blocked`
- `escalation`

### Step 3: Create Founder Decision Request

If a Founder decision is needed, create a new issue using the Founder Decision Request template:

**Title:** `FDR: [Escalation Reason]`

**Body:** Use the standard FDR template with:
- Requesting Agent/Team
- Context & Background
- Decision Required
- Options Considered
- Impact of Delay
- Affected Invariants

### Step 4: Halt Work

**No agent may proceed** while an escalation is active.

- Do not commit code
- Do not merge PRs
- Do not make decisions
- Wait for Founder decision

### Step 5: Founder Resolution

The Founder:
1. Reviews the escalation
2. Issues a decision (FD-YYYY-NNN)
3. Decision is logged in the Founder Decision Log
4. Decision is communicated to all agents

### Step 6: Work Resumes

Once the Founder decision is logged:
1. Status changes from `BLOCKED-GOVERNANCE` to `IMPLEMENTING`
2. Work resumes under the new decision
3. All agents are notified
4. Context Handoff Summary provided if needed

---

## Escalation Response Times

| Severity | Response Time | Resolution Time |
|----------|---------------|-----------------|
| Level 1 (Minor) | 4 hours | 24 hours |
| Level 2 (Major) | 2 hours | 8 hours |
| Level 3 (Critical) | 30 minutes | 2 hours |

---

## Escalation Categories

### Category A: Conflicting Decisions

**Trigger:** Two Founder Decisions apply with incompatible outcomes

**Escalation Process:**
1. Flag the conflict
2. Create FDR with both decisions referenced
3. Propose resolution options
4. Halt work
5. Await Founder decision

**Resolution:** New Founder Decision that explicitly supersedes one or both

### Category B: Invariant Violation

**Trigger:** Work violates an enforced invariant

**Escalation Process:**
1. Flag the violation
2. Identify which invariant is violated
3. Propose remediation options
4. Halt work
5. Await Founder decision

**Resolution:** Either fix the work to comply, or modify the invariant (requires FD)

### Category C: Missing Decision

**Trigger:** Work requires a decision that doesn't exist

**Escalation Process:**
1. Flag the missing decision
2. Create FDR with required decision
3. Provide options and recommendations
4. Halt work
5. Await Founder decision

**Resolution:** New Founder Decision issued

### Category D: Authority Ambiguity

**Trigger:** Unclear who has authority to make a decision

**Escalation Process:**
1. Flag the ambiguity
2. Identify which roles claim authority
3. Create FDR requesting authority clarification
4. Halt work
5. Await Founder decision

**Resolution:** New Founder Decision clarifying authority boundaries

### Category E: Interpretation Disagreement

**Trigger:** Agents disagree on interpretation of a decision or invariant

**Escalation Process:**
1. Flag the disagreement
2. Document both interpretations
3. Create FDR requesting clarification
4. Halt work
5. Await Founder decision

**Resolution:** New Founder Decision clarifying interpretation

### Category F: Security Risk

**Trigger:** Security Agent identifies critical security risk

**Escalation Process:**
1. Immediate notification to Founder
2. Work halted immediately
3. Security Agent documents threat and mitigation
4. Await Founder decision

**Resolution:** Either fix the security issue, or accept risk via Founder Decision

---

## Escalation Checklist

Before escalating, verify:

- [ ] Trigger condition is clearly identified
- [ ] All relevant context is provided
- [ ] All links to GitHub artifacts are included
- [ ] Potential resolutions are proposed
- [ ] Status is updated to BLOCKED-GOVERNANCE
- [ ] Founder Decision Request created (if needed)
- [ ] All agents are notified

---

## Escalation Communication Template

**GitHub Issue Comment:**

```
⚠️ GOVERNANCE ESCALATION — [Category]

**Trigger:** [Specific trigger condition]

**Severity:** Level [1/2/3]

**Issue:** [Clear description of the problem]

**Affected Work:**
- Issue: #XXX
- PR: #YYY

**Context:**
[Relevant links and background]

**Required Resolution:**
[What decision or action is needed]

**Proposed Options:**
1. [Option A]
2. [Option B]

**Recommendation:** [Agent recommendation]

**Status:** BLOCKED-GOVERNANCE
**Awaiting:** Founder Decision
```

---

## Escalation Metrics

Track escalations to identify patterns:

- **Escalation Frequency** — How often escalations occur
- **Escalation Duration** — How long escalations take to resolve
- **Escalation Categories** — Which types of escalations are most common
- **Decision Quality** — Are decisions resolving escalations effectively

---

## Prevention

Escalations can be prevented by:

1. **Clear Decisions** — Founder decisions are explicit and unambiguous
2. **Complete Context** — All work includes required context
3. **Role Clarity** — Authority boundaries are explicit
4. **Invariant Compliance** — Work is designed to comply with invariants
5. **Early Review** — Lead Agents review early to catch issues

---

**Last Updated:** 2026-02-01  
**Maintained By:** Chief of Staff (Manus Agent)
