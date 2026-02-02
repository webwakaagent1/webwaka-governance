# Context Handoff Standard

**Document Type:** Operational Standard  
**Authority:** Founder  
**Status:** ACTIVE & ENFORCEABLE  
**Effective Date:** February 1, 2026  

---

## PURPOSE

This standard defines when context handoffs are mandatory, what they must contain, and what constitutes a valid handoff.

**Goal:** Ensure zero context loss when switching Manus accounts or pausing work.

---

## WHEN HANDOFF IS MANDATORY

A Context Handoff Summary is **required** in these situations:

1. **Account Switching** — Switching from one Manus account to another
2. **Work Pause** — Pausing work for more than 4 hours
3. **Role Change** — Changing roles within the same task
4. **Task Reassignment** — Assigning task to a different agent
5. **Shift Change** — End of a work session
6. **Escalation** — Escalating work to a different team

---

## HANDOFF STRUCTURE (CANONICAL)

All Context Handoff Summaries **must** follow this structure:

```markdown
## Context Handoff Summary

### Current State
[Describe what is complete and what is incomplete]

### Key Decisions
[List all non-trivial decisions made and why]

### Open Risks / Questions
[List any known risks or unanswered questions]

### Next Recommended Actions
[Concrete, actionable next steps]

### References
[Links to all relevant GitHub issues, PRs, docs]
```

---

## DETAILED REQUIREMENTS

### 1. Current State

**Must include:**
- What work is complete
- What work is in progress
- What work is blocked
- What work is remaining
- Current status of all artifacts (code, tests, docs)

**Example:**
```
### Current State
- ✅ Core storage abstraction implemented (OFF-001)
- ✅ IndexedDB backend complete and tested
- ⏳ SQLite backend 60% complete (mobile)
- ❌ Encryption layer not yet started (blocked on OFF-001)
- ❌ Tests for SQLite backend incomplete
- 📝 Documentation draft exists but needs review
```

### 2. Key Decisions

**Must include:**
- Every non-trivial decision made
- Why that decision was made
- What alternatives were considered
- Any trade-offs or risks accepted

**Example:**
```
### Key Decisions
1. **Chose IndexedDB over LocalStorage** — IndexedDB supports larger data volumes and better performance for offline scenarios
2. **Implemented 3-layer architecture** — Abstraction layer allows backend swapping without affecting consumers
3. **Deferred encryption to next phase** — Decided to focus on storage stability first, encryption can be added without breaking changes
```

### 3. Open Risks / Questions

**Must include:**
- Any known issues or risks
- Unanswered questions
- Ambiguities in requirements
- Potential blockers

**Example:**
```
### Open Risks / Questions
- ⚠️ SQLite backend performance on large datasets not yet tested
- ❓ What is the maximum offline data size per user?
- ⚠️ Mobile platform (iOS) SQLite access may require special permissions
- ❓ Should we implement data compression for offline storage?
```

### 4. Next Recommended Actions

**Must include:**
- Concrete, actionable next steps
- Priority order
- Estimated effort (if known)
- Any blockers or dependencies

**Example:**
```
### Next Recommended Actions
1. **Complete SQLite backend** (Priority: HIGH) — Finish remaining 40% of implementation
2. **Add comprehensive tests** (Priority: HIGH) — Both backends need full test coverage
3. **Performance testing** (Priority: MEDIUM) — Test with realistic data volumes
4. **Begin encryption layer** (Priority: MEDIUM) — Can start once OFF-001 is stable
5. **Documentation review** (Priority: LOW) — Polish and finalize docs
```

### 5. References

**Must include:**
- Links to all relevant GitHub issues
- Links to all relevant PRs
- Links to documentation
- Links to related decisions

**Example:**
```
### References
- Issue: #34 OFF-001 — Local Offline Data Store Abstraction
- PR: #54 — Storage Abstraction Implementation
- PR: #55 — IndexedDB Backend
- Doc: docs/architecture/offline-storage.md
- Decision: FD-2026-001 — Offline-First Requirement
```

---

## LOCATION & FORMAT

### Where to Post

Context Handoff Summaries must be posted in one of these locations:

1. **GitHub Issue Comment** — If work is paused on an issue
2. **GitHub PR Comment** — If work is paused on a PR
3. **GitHub Discussion** — If work spans multiple issues
4. **Governance Document** — If work is being formally handed off

### Format

- Use Markdown
- Use the canonical structure above
- Be concise but complete
- Include all links
- No assumptions about context

---

## REJECTION CRITERIA

A Context Handoff Summary is **INVALID** if it:

- ❌ Is missing any of the 5 required sections
- ❌ Contains vague statements like "work is ongoing"
- ❌ Lacks links to relevant GitHub artifacts
- ❌ Assumes context not documented in GitHub
- ❌ Is longer than 1 page (be concise)
- ❌ Contains no actionable next steps
- ❌ Fails to identify risks or blockers

**Invalid handoffs are rejected and must be redone.**

---

## HANDOFF CHECKLIST

Before posting a Context Handoff Summary, verify:

- [ ] All 5 sections are complete
- [ ] Current state is clear (what's done, what's not)
- [ ] All decisions are explained with rationale
- [ ] All risks and questions are listed
- [ ] Next steps are concrete and actionable
- [ ] All references are valid GitHub links
- [ ] No assumptions about prior context
- [ ] Handoff is concise (< 1 page)
- [ ] Handoff is posted in correct location
- [ ] Handoff is in Markdown format

---

## EXAMPLE HANDOFF (COMPLETE)

```markdown
## Context Handoff Summary

### Current State
- ✅ Role Instantiation Prompt Pack completed and tested
- ✅ Chief of Staff prompt verified
- ⏳ Execution Agent prompt 90% complete
- ⏳ QA Agent prompt 80% complete
- ❌ Security Agent prompt not yet started
- ❌ Documentation Agent prompt not yet started
- 📝 Integration tests in progress

### Key Decisions
1. **Prompts are immutable** — Decided to make prompts canonical and unchangeable to ensure consistency across all agents
2. **Separate prompts per role** — Each role gets a dedicated prompt rather than a generic template with role parameters
3. **Master system prompt first** — All agents must load master prompt before role-specific prompt to ensure governance grounding

### Open Risks / Questions
- ⚠️ Need to verify prompts work across different Manus account types
- ❓ Should we add version numbers to prompts for future updates?
- ⚠️ Need to test prompt switching (can agent switch roles mid-session?)

### Next Recommended Actions
1. **Complete remaining prompts** (Priority: HIGH) — Finish Security and Documentation agent prompts
2. **Integration testing** (Priority: HIGH) — Test all prompts in sequence
3. **Documentation** (Priority: MEDIUM) — Add usage guide for Founder
4. **Automation** (Priority: LOW) — Consider auto-validation of prompt structure

### References
- Issue: #80 — Documentation & Knowledge Management Agent Activation
- PR: #5 — Implement Model D + Model E Operational Model
- Doc: docs/roles/ROLE_INSTANTIATION_PROMPT_PACK.md
- Decision: FD-2026-001 — Ratification of Agentic Operating Model
```

---

## ENFORCEMENT

- **Lead Agents verify** handoff completeness before accepting work
- **Invalid handoffs are rejected** and must be redone
- **Missing handoffs block work** — Work cannot proceed without valid handoff
- **Governance Agent audits** handoff quality

---

## WHAT THIS ENABLES

✅ **Zero context loss** — All context is explicit and transferable  
✅ **Instant account switching** — New agent can resume work immediately  
✅ **Perfect continuity** — No rework or duplication  
✅ **Auditability** — All handoffs are documented in GitHub  
✅ **Scalability** — Multiple agents can work on same task seamlessly  

---

**Status:** ACTIVE & ENFORCEABLE  
**Last Updated:** February 1, 2026  
**Maintained By:** Chief of Staff (Manus Agent)
