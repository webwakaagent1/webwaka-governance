# Decision → Invariant Mapping Registry

This file defines which Founder Decisions enforce or modify which invariants.

**Rule:** If a decision references an invariant, enforcement is mandatory.

---

## INV-001: GitHub Is the Canonical System of Record

**Definition:** All material state, decisions, context, and work products must exist in GitHub artifacts. No external systems are authoritative.

**Enforced By:**
- FD-2026-001 (Agentic Operating Model Ratification)

**Implications:**
- No Manus agent may rely on chat memory
- All context must be derived from GitHub only
- All decisions must be documented in GitHub
- No external documentation is authoritative

**Verification:**
- CI checks verify all work references GitHub artifacts
- Governance workflow enforces GitHub-only context

---

## INV-010: Offline-First Is Non-Negotiable

**Definition:** All features must function without real-time connectivity. Offline storage, queueing, and sync are mandatory.

**Enforced By:**
- FD-2026-001 (Agentic Operating Model Ratification)

**Implications:**
- No feature may require real-time connectivity
- Offline storage and sync mechanisms are mandatory
- Tests must explicitly validate offline behavior
- Sync conflicts must be handled gracefully

**Verification:**
- CI checks for hardcoded online-only dependencies
- Test suite includes offline scenarios
- Architecture review verifies offline-first design

---

## INV-012: Multi-Repository Topology Is Authoritative

**Definition:** The WebWaka platform is organized as a multi-repository topology. Repository boundaries, dependencies, and ownership are explicit and enforced.

**Enforced By:**
- FD-2026-001 (Agentic Operating Model Ratification)

**Implications:**
- No monorepo consolidation without Founder decision
- Repository boundaries are explicit
- Cross-repository dependencies are documented
- Ownership and access control are enforced

**Verification:**
- CODEOWNERS files enforce repository ownership
- GitHub Teams enforce access control
- Architecture review verifies topology compliance

---

## INV-013: Test-First Development Is Mandatory

**Definition:** Tests must exist before implementation. All code changes must have corresponding tests. Minimum coverage thresholds are enforced.

**Enforced By:**
- FD-2026-001 (Agentic Operating Model Ratification)

**Implications:**
- CI must fail if tests are missing
- `--passWithNoTests` flags are forbidden
- Minimum coverage thresholds are enforced
- Tests must fail when feature is removed

**Verification:**
- CI workflow blocks PRs without tests
- Coverage reports are generated and tracked
- Quality Agent verifies test adequacy

---

## INV-014: Founder Decisions Are Explicit, Logged, and Immutable

**Definition:** All decisions affecting scope, architecture, priority, risk, or governance must be explicitly documented in the Founder Decision Log. Decisions are immutable unless explicitly superseded.

**Enforced By:**
- FD-2026-001 (Agentic Operating Model Ratification)

**Implications:**
- All work must reference a valid Founder Decision
- Decisions are append-only (no edits)
- Supersession requires a new decision
- No silent overrides or implicit changes

**Verification:**
- CI checks verify Founder Decision references
- Governance workflow enforces decision compliance
- Conflict detection identifies decision violations

---

## INV-015: Role-Based Authority Is Explicit

**Definition:** Agent authority is derived from explicit role instantiation, not from account identity. Roles are persistent; accounts are disposable.

**Enforced By:**
- FD-2026-001 (Agentic Operating Model Ratification)

**Implications:**
- All work must declare acting role
- Authority is bounded by role definition
- Role instantiation prompts are mandatory
- No agent may exceed role authority

**Verification:**
- GitHub templates require acting role declaration
- Governance workflow enforces role compliance
- Lead Agents verify role authority

---

## INV-016: Context Handoff Is Mandatory on Disengagement

**Definition:** When work is paused, reassigned, or abandoned, a Context Handoff Summary is mandatory. Silence is failure.

**Enforced By:**
- FD-2026-001 (Agentic Operating Model Ratification)

**Implications:**
- Paused work requires handoff documentation
- Reassigned work requires handoff documentation
- Abandoned work requires stop-work declaration
- Silence triggers escalation

**Verification:**
- Lead Agents verify handoff completeness
- Governance workflow flags missing handoffs
- Escalation protocol triggered on silence

---

## Rules

- Invariants are append-only
- Invariants may not be removed without Founder decision
- New invariants require a Founder decision
- Invariant modifications require a Founder decision
- All invariants are enforceable

---

**Last Updated:** 2026-02-01  
**Maintained By:** Chief of Staff (Manus Agent)
