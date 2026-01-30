# Wave 4 Platform Assignment & Parallelization Analysis

**Analysis Date:** January 30, 2026  
**Analyst:** Manus  
**Authority:** Post-Migration Operating Rules, Master Control Board v8.0

---

## Executive Summary

This document provides a detailed analysis of parallelization opportunities and platform assignment recommendations for the five candidate phases identified for Wave 4. The analysis prioritizes continuity, dependency management, and balanced workload distribution between Manus and Replit.

---

## Candidate Phases for Wave 4

1.  **CS-3:** Identity & Access Management V2
2.  **SC-1:** Commerce Suite V1
3.  **SC-2:** MLAS Suite V1
4.  **SC-3:** Transport & Logistics Suite V1
5.  **ID-2:** Partner Whitelabel Deployment

---

## Platform Assignment Analysis & Recommendations

### CS-3: Identity & Access Management V2

*   **Historical Context:** The original IAM implementation (Phase 2A/2B) was executed by **Replit**.
*   **Complexity:** High. This phase involves security-critical features like social login, 2FA, and account recovery.
*   **Dependencies:** None beyond the original IAM implementation.
*   **Recommendation:** **Assign to Replit.** Assigning this to Replit maintains continuity and leverages their existing context on the IAM system. This is the most prudent approach for a security-critical component.

### SC-1: Commerce Suite V1

*   **Historical Context:** This is a new suite, integrating capabilities built by both Manus and Replit.
*   **Complexity:** Very High. This is the largest and most complex suite, integrating four distinct capabilities (CB-1, CB-2, CB-3, CB-4) into a unified user-facing product.
*   **Dependencies:** CB-1 (Manus), CB-2 (Replit), CB-3 (Replit), CB-4 (Replit).
*   **Recommendation:** **Assign to Manus.** Manus has demonstrated superior capability in handling large-scale, multi-dependency integration tasks, most notably the recently completed 6-phase repository topology migration. The complexity of integrating four major capabilities into a single cohesive suite is best handled by Manus.

### SC-2: MLAS Suite V1

*   **Historical Context:** The underlying MLAS Capability (CB-1) was built by **Manus**.
*   **Complexity:** High. This suite will expose the core logic of the MLAS, a complex and critical piece of the platform's business model.
*   **Dependencies:** CB-1 (Manus).
*   **Recommendation:** **Assign to Manus.** The principle of continuity dictates that the platform that built the core capability should also build the suite that exposes it. This ensures deep domain knowledge and a consistent architectural vision.

### SC-3: Transport & Logistics Suite V1

*   **Historical Context:** This is a new suite with significant dependencies on foundational work done by Manus.
*   **Complexity:** High. This suite involves complex requirements, including offline-first functionality, realtime-enhanced operations, and specific Nigeria-first use cases.
*   **Dependencies:** PF-2 (Manus), PF-3 (Manus), CB-1 (Manus), CB-4 (Replit).
*   **Recommendation:** **Assign to Manus.** The heavy dependency on the foundational (PF-2, PF-3) and capability (CB-1) layers built by Manus makes it the logical choice. Manus has the deepest context on the realtime, AI, and MLAS components required for this suite.

### ID-2: Partner Whitelabel Deployment

*   **Historical Context:** The prerequisite, ID-1 (Enterprise Deployment Automation), was built by **Manus**.
*   **Complexity:** Medium. This phase extends an existing infrastructure capability.
*   **Dependencies:** ID-1 (Manus).
*   **Recommendation:** **Assign to Manus.** For infrastructure components, consistency is key. Assigning this to Manus ensures that the entire deployment automation and infrastructure hardening track is managed with a single, consistent approach.

---

## Proposed Wave 4 Parallel Execution Plan

Based on the analysis, the following parallel execution plan is recommended:

| Assigned Platform | Phase(s) | Target Repository(ies) |
| :--- | :--- | :--- |
| **Manus** | SC-1: Commerce Suite V1<br>SC-2: MLAS Suite V1<br>SC-3: Transport & Logistics Suite V1<br>ID-2: Partner Whitelabel Deployment | `webwaka-suites` (new)<br>`webwaka-infrastructure` (existing) |
| **Replit** | CS-3: Identity & Access Management V2 | `webwaka-core-services` (existing) |

### Rationale for Parallelization

*   **No Cross-Dependencies:** The phases assigned to Manus and Replit have no dependencies on each other. CS-3 can be executed independently of the new suites and the infrastructure update.
*   **Balanced Workload:** This plan assigns the single, highly-focused (but complex) IAM task to Replit, while assigning the broader, multi-phase suite and infrastructure work to Manus. This represents a balanced distribution of effort.
*   **Efficient Repository Management:** The three suite phases (SC-1, SC-2, SC-3) can be developed in parallel within the same new `webwaka-suites` repository, which will be created as the first step of their execution.

---

## Conclusion

This plan proposes a clear, parallelizable, and governance-compliant path for Wave 4 execution. It leverages platform strengths, respects historical context, and minimizes execution risk.

**Next Step:** Analyze execution readiness and identify any potential gaps for these five phases.

---

**End of Document**
