# WebWaka Platform - Remediation Wave Plan

**Document Type**: Remediation Planning Artifact  
**Date**: January 31, 2026  
**Source**: WEBWAKA_PLATFORM_VERIFICATION_REPORT.md + ISSUE_CLASSIFICATION_MATRIX.md  
**Status**: Planning Phase

---

## Executive Summary

This document defines the complete remediation strategy for all 29 issues identified in the platform verification report. The remediation is organized into 6 waves with clear dependencies, parallelization opportunities, and platform assignments.

**Total Estimated Timeline**: 16-24 weeks (4-6 months)

**Wave Structure**:
- **Wave R1 (Emergency Stabilization)**: 1-2 weeks - Fix critical blockers
- **Wave R2 (Core Testing Infrastructure)**: 4-6 weeks - Create test suites for all implementations
- **Wave R3 (Platform Capabilities)**: 4-6 weeks - Implement missing platform features
- **Wave R4 (Quality & Governance)**: 2-3 weeks - Establish quality gates and governance processes
- **Wave R5 (Scale Readiness)**: 4-6 weeks - Implement architectural improvements
- **Wave R6 (Operational Excellence)**: 2-4 weeks - Implement observability and monitoring

---

## Remediation Wave Definitions

### Wave R1: Emergency Stabilization

**Duration**: 1-2 weeks  
**Goal**: Fix critical blockers that prevent any meaningful progress  
**Parallelization**: High (all items can run in parallel)  
**Dependencies**: None (can start immediately)

#### Phase R1-A: Fix Broken Tests

**Scope**: Fix CS-1 TypeScript configuration to enable test execution

**Issues Addressed**:
- ISSUE-001: CS-1 Financial Ledger Tests Fail to Compile

**Exit Criteria**:
- CS-1 tests compile successfully
- CS-1 tests execute and pass
- CI/CD pipeline shows green status for CS-1

**Invariants Enforced**: None directly (enables verification of INV-001, INV-002)

**Test Requirements**:
- All 22 existing CS-1 tests must compile
- All tests must pass
- Coverage report must be generated

**Platform Assignment**: Manus  
**Parallelizable**: Yes (independent)  
**Effort**: 1 day  
**Owner**: Core Services Team

**PaA Readiness**: Execution-ready  
**Missing Inputs**: None

---

#### Phase R1-B: Audit Documentation-Code Alignment

**Scope**: Audit all README files against actual codebase and update to reflect reality

**Issues Addressed**:
- ISSUE-005: Severe Documentation-Implementation Mismatch
- ISSUE-022: SC-1 Has Stub Endpoints Returning Empty Data

**Exit Criteria**:
- All READMEs audited against actual code
- All documented features verified as existing or marked as "planned"
- All stub endpoints documented with `"status": "stub"` in responses
- Stakeholders informed of actual vs documented capabilities

**Invariants Enforced**: None directly (restores governance credibility)

**Test Requirements**:
- Automated documentation-code alignment checks (future)

**Platform Assignment**: Manus  
**Parallelizable**: Yes (can audit multiple repositories in parallel)  
**Effort**: 1 week  
**Owner**: All Teams

**PaA Readiness**: Execution-ready  
**Missing Inputs**: None

---

#### Phase R1-C: Execute Unknown Tests

**Scope**: Execute and verify tests for 6 implementations with unknown test status

**Issues Addressed**:
- ISSUE-021: CS-2, CS-4, CB-2, CB-3, CB-4, PF-1 Have Unknown Test Status

**Exit Criteria**:
- Tests executed for all 6 implementations
- Test results documented (pass/fail/coverage)
- Any broken tests fixed
- Coverage reports generated

**Invariants Enforced**: Various (depends on service)

**Test Requirements**:
- All existing tests must execute
- Broken tests must be fixed
- Coverage must be measured

**Platform Assignment**: Manus  
**Parallelizable**: Yes (can test in parallel)  
**Effort**: 1 week  
**Owner**: Respective Teams

**PaA Readiness**: Execution-ready  
**Missing Inputs**: None

---

### Wave R2: Core Testing Infrastructure

**Duration**: 4-6 weeks  
**Goal**: Create comprehensive test suites for all untested implementations  
**Parallelization**: High (most items can run in parallel)  
**Dependencies**: Wave R1 complete (especially R1-A for CI/CD confidence)

#### Phase R2-A: Create CS-3 IAM Test Suite

**Scope**: Create comprehensive test suite for CS-3 (IAM V2) covering tenant isolation, authentication, authorization, and audit logging

**Issues Addressed**:
- ISSUE-002: CS-3 IAM Has Zero Tests

**Exit Criteria**:
- Unit tests for all IAM middleware (tenantContextMiddleware, verifyTenantOwnership, requireSuperAdminWithAudit, scopeToTenant)
- Integration tests for authentication flows
- Integration tests for authorization enforcement
- Integration tests for audit logging
- Integration tests for cross-tenant access attempts (should fail)
- Minimum 70% code coverage
- All tests passing in CI/CD

**Invariants Enforced**:
- INV-001: Multi-Tenant by Design
- INV-002: Strict Tenant Isolation
- INV-003: Audited Super Admin Access

**Test Requirements**:
- Tenant isolation tests (unit + integration)
- Authentication flow tests
- Authorization enforcement tests
- Audit logging tests
- Cross-service tenant isolation tests
- Penetration tests for tenant boundaries

**Platform Assignment**: Manus  
**Parallelizable**: Yes (independent of other test suites)  
**Effort**: 1-2 weeks  
**Owner**: Core Services Team

**PaA Readiness**: Execution-ready  
**Missing Inputs**: None

---

#### Phase R2-B: Create Suite Test Suites

**Scope**: Create test suites for all three business suites (SC-1, SC-2, SC-3)

**Issues Addressed**:
- ISSUE-006: All 3 Suites Have Zero Tests

**Exit Criteria**:
- Unit tests for business logic in SC-1, SC-2, SC-3
- Integration tests with capabilities (CB-*)
- End-to-end tests for critical user flows
- API endpoint tests
- Minimum 70% code coverage per suite
- All tests passing in CI/CD

**Invariants Enforced**:
- INV-006: MLAS as Infrastructure (SC-2)
- INV-007: Nigeria-First, Africa-Ready (all suites)

**Test Requirements**:
- Business logic tests
- API endpoint tests
- Integration tests with capabilities
- End-to-end user flow tests
- Mobile responsiveness tests (ISSUE-010)
- Offline behavior tests (ISSUE-011)

**Platform Assignment**: Mixed (Manus for Python-based, Replit for Node.js-based)  
**Parallelizable**: Yes (can create SC-1, SC-2, SC-3 tests in parallel)  
**Effort**: 2-4 weeks (varies by suite)  
**Owner**: Suites Team

**PaA Readiness**: Execution-ready  
**Missing Inputs**: None

---

#### Phase R2-C: Create Infrastructure Test Suites

**Scope**: Create test suites for all three infrastructure phases (ID-1, ID-2, ID-3)

**Issues Addressed**:
- ISSUE-007: All 3 Infrastructure Phases Have Zero Tests

**Exit Criteria**:
- Deployment automation tests (ID-1)
- Configuration validation tests (ID-1, ID-2, ID-3)
- Multi-tenancy isolation tests (ID-2)
- Partner boundary enforcement tests (ID-2)
- Data residency compliance tests (ID-3)
- Minimum 70% code coverage per phase
- All tests passing in CI/CD

**Invariants Enforced**:
- INV-005: Partner-Led Operating Model (ID-2)
- INV-008: Backward-Compatible Evolution (ID-1, ID-2)
- INV-012: Deployment Flexibility (ID-1, ID-3)

**Test Requirements**:
- Deployment automation tests
- Configuration validation tests
- Multi-tenancy tests
- Partner isolation tests
- Data residency tests
- Rollback tests

**Platform Assignment**: Manus  
**Parallelizable**: Yes (can create ID-1, ID-2, ID-3 tests in parallel)  
**Effort**: 2-3 weeks  
**Owner**: Infrastructure Team

**PaA Readiness**: Execution-ready  
**Missing Inputs**: None

---

#### Phase R2-D: Create MLAS Test Suites

**Scope**: Create test suites for CB-1 (MLAS Capability) and SC-2 (MLAS Suite)

**Issues Addressed**:
- ISSUE-008: CB-1 MLAS and SC-2 MLAS Suite Have Zero Tests

**Exit Criteria**:
- Revenue calculation tests
- Commission distribution tests
- Payout processing tests
- Retry logic tests
- Financial accuracy tests
- Minimum 70% code coverage
- All tests passing in CI/CD

**Invariants Enforced**:
- INV-006: MLAS as Infrastructure

**Test Requirements**:
- Revenue calculation tests
- Commission distribution tests
- Payout processing tests
- Financial accuracy tests
- Edge case tests (zero revenue, negative amounts, etc.)

**Platform Assignment**: Manus  
**Parallelizable**: Yes (can test CB-1 and SC-2 in parallel)  
**Effort**: 1-2 weeks  
**Owner**: Capabilities Team + Suites Team

**PaA Readiness**: Execution-ready  
**Missing Inputs**: None

---

#### Phase R2-E: Create PF-2 and PF-3 Test Suites

**Scope**: Create test suites for PF-2 (Realtime Eventing) and PF-3 (AI & High Complexity)

**Issues Addressed**:
- ISSUE-004: 59% of Implementations Have Zero Tests (PF-2, PF-3 portion)

**Exit Criteria**:
- WebSocket connection tests (PF-2)
- Event delivery tests (PF-2)
- Offline reconciliation tests (PF-2)
- BYOK functionality tests (PF-3)
- Key encryption tests (PF-3)
- Audit logging tests (PF-3)
- Minimum 70% code coverage
- All tests passing in CI/CD

**Invariants Enforced**:
- INV-004: Realtime as Infrastructure (PF-2)
- INV-010: Realtime as Optional Degradable Capability (PF-2)
- INV-011: AI as Opt-In, BYOK-Enabled (PF-3)

**Test Requirements**:
- Realtime connection tests
- Event delivery tests
- Offline reconciliation tests
- BYOK tests
- Key management tests

**Platform Assignment**: Manus  
**Parallelizable**: Yes (can test PF-2 and PF-3 in parallel)  
**Effort**: 2-3 weeks  
**Owner**: Platform Foundation Team

**PaA Readiness**: Execution-ready  
**Missing Inputs**: None

---

#### Phase R2-F: Create CB-1 Test Suite

**Scope**: Create test suite for CB-1 (MLAS Capability) - covered by R2-D

**Issues Addressed**: Covered by Phase R2-D

---

### Wave R3: Platform Capabilities

**Duration**: 4-6 weeks  
**Goal**: Implement missing platform features required for production  
**Parallelization**: Medium (some dependencies between items)  
**Dependencies**: Wave R2 complete (need test infrastructure to verify new features)

#### Phase R3-A: Implement Nigerian Payment Integration

**Scope**: Integrate Paystack or Flutterwave payment gateway with comprehensive tests

**Issues Addressed**:
- ISSUE-012: No Nigerian Payment Integration

**Exit Criteria**:
- Paystack or Flutterwave integration complete
- Payment processing implemented
- Webhook handling implemented
- Reconciliation implemented
- Comprehensive tests (unit + integration + end-to-end)
- Documentation updated
- Minimum 70% code coverage

**Invariants Enforced**:
- INV-007: Nigeria-First, Africa-Ready

**Test Requirements**:
- Payment processing tests
- Webhook handling tests
- Reconciliation tests
- Error handling tests
- Idempotency tests

**Platform Assignment**: Manus  
**Parallelizable**: Yes (independent of other features)  
**Effort**: 2 weeks  
**Owner**: Capabilities Team

**PaA Readiness**: Execution-ready  
**Missing Inputs**: None (but requires Paystack/Flutterwave API credentials from Founder)

---

#### Phase R3-B: Implement Offline-First Patterns

**Scope**: Implement offline-first capabilities across platform with local storage, sync, and reconciliation

**Issues Addressed**:
- ISSUE-011: No Offline-First Implementation

**Exit Criteria**:
- Local data storage implemented (IndexedDB or similar)
- Offline mode detection and indicators implemented
- Queued operations for offline actions implemented
- Sync and reconciliation mechanisms implemented
- Conflict resolution strategies implemented
- Comprehensive tests (offline behavior, sync, reconciliation)
- Documentation updated
- Minimum 70% code coverage

**Invariants Enforced**:
- INV-010: Realtime as Optional Degradable Capability

**Test Requirements**:
- No network behavior tests
- Flaky network handling tests
- Slow network handling tests
- Sync tests
- Reconciliation tests
- Conflict resolution tests
- Failure recovery tests

**Platform Assignment**: Manus  
**Parallelizable**: Partially (PF-2 must be verified first, then suite-level features)  
**Effort**: 4-6 weeks  
**Owner**: Platform Foundation Team + Suites Team

**PaA Readiness**: Partially specifiable (requires PF-2 verification first)  
**Missing Inputs**: PF-2 test results from Wave R2

---

#### Phase R3-C: Implement Mobile-First Validation

**Scope**: Add mobile-specific tests and validation across platform

**Issues Addressed**:
- ISSUE-010: No Mobile-First Validation

**Exit Criteria**:
- Responsive design tests implemented
- Viewport configuration tests implemented
- Memory constraint tests implemented
- Background/foreground transition tests implemented
- Token/session behavior tests implemented
- Graceful degradation tests implemented
- Mobile session management strategy documented (ISSUE-023)
- Documentation updated

**Invariants Enforced**:
- INV-007: Nigeria-First, Africa-Ready

**Test Requirements**:
- Small screen tests
- Low-memory device tests
- Background/foreground transition tests
- Session management tests
- Graceful degradation tests

**Platform Assignment**: Mixed (Manus for test creation, Replit for mobile app testing if needed)  
**Parallelizable**: Yes (can test multiple services in parallel)  
**Effort**: 2-4 weeks  
**Owner**: All Teams

**PaA Readiness**: Execution-ready  
**Missing Inputs**: None

---

#### Phase R3-D: Implement SC-1 Missing Features

**Scope**: Implement documented but missing features in SC-1 Commerce Suite OR remove from documentation

**Issues Addressed**:
- ISSUE-005: Severe Documentation-Implementation Mismatch (SC-1 portion)
- ISSUE-022: SC-1 Has Stub Endpoints Returning Empty Data

**Exit Criteria**:
- Decision made: implement missing features OR remove from documentation
- If implementing: all documented features implemented with tests
- If removing: documentation updated to reflect actual state
- All stub endpoints either implemented or documented as stubs
- Comprehensive tests for all implemented features
- Minimum 70% code coverage

**Invariants Enforced**:
- INV-007: Nigeria-First, Africa-Ready (commerce functionality)

**Test Requirements**:
- Business logic tests for implemented features
- API endpoint tests
- Integration tests

**Platform Assignment**: Manus  
**Parallelizable**: Yes (independent of other features)  
**Effort**: 2-4 weeks (if implementing) or 1 day (if documenting)  
**Owner**: Suites Team

**PaA Readiness**: Blocked (requires Founder decision: implement or document?)  
**Missing Inputs**: Founder decision on SC-1 feature scope

---

### Wave R4: Quality & Governance

**Duration**: 2-3 weeks  
**Goal**: Establish quality gates and governance processes to prevent regression  
**Parallelization**: Medium  
**Dependencies**: Wave R2 complete (need baseline test coverage)

#### Phase R4-A: Remove CI/CD Fallback Flags

**Scope**: Remove `--passWithNoTests` and other fallback flags from CI/CD workflows

**Issues Addressed**:
- ISSUE-003: CI/CD `--passWithNoTests` Flag Masks Test Absence
- ISSUE-020: Coverage Threshold Not Enforced

**Exit Criteria**:
- `--passWithNoTests` flag removed from all repositories
- Coverage threshold fallback removed
- Linting fallback removed
- Build fallback removed
- TypeScript check fallback removed
- CI/CD enforces all quality gates
- All pipelines green after removal

**Invariants Enforced**: None directly (enables verification of all invariants)

**Test Requirements**:
- All quality gates must pass without fallbacks

**Platform Assignment**: Manus  
**Parallelizable**: Yes (can update multiple repositories in parallel)  
**Effort**: 1 day (removal) + ongoing monitoring  
**Owner**: Platform Team

**PaA Readiness**: Execution-ready  
**Missing Inputs**: None (but requires Wave R2 completion)

---

#### Phase R4-B: Re-Verify Wave 4 and Update Verification Report

**Scope**: Re-verify all Wave 4 phases with actual testing and update verification report

**Issues Addressed**:
- ISSUE-009: Wave 4 Verification Report Contains False Assertions

**Exit Criteria**:
- All Wave 4 phases re-verified with actual test execution
- Wave 4 Verification Report retracted or amended
- New verification report published with accurate findings
- Stakeholders informed of actual state
- Verification process updated to include test execution

**Invariants Enforced**: None directly (restores governance credibility)

**Test Requirements**:
- All Wave 4 phase tests must be executed
- Test results must be documented
- Coverage must be measured

**Platform Assignment**: Manus  
**Parallelizable**: No (requires Wave R2 completion)  
**Effort**: 2 weeks  
**Owner**: Governance Team

**PaA Readiness**: Execution-ready  
**Missing Inputs**: None (but requires Wave R2 completion)

---

#### Phase R4-C: Establish Documentation-Code Synchronization Process

**Scope**: Create automated checks and processes to keep documentation aligned with code

**Issues Addressed**:
- ISSUE-005: Severe Documentation-Implementation Mismatch (process portion)

**Exit Criteria**:
- Automated documentation-code alignment checks implemented
- Pre-commit hooks for documentation updates
- CI/CD checks for documentation accuracy
- Documentation update process documented
- Process enforced across all repositories

**Invariants Enforced**: None directly (improves governance)

**Test Requirements**:
- Automated checks must detect misalignment

**Platform Assignment**: Manus  
**Parallelizable**: Yes (independent of other processes)  
**Effort**: 1 week  
**Owner**: Platform Team

**PaA Readiness**: Execution-ready  
**Missing Inputs**: None

---

#### Phase R4-D: Implement Audit Log Retention Policy

**Scope**: Implement audit log retention policy, immutability, and monitoring

**Issues Addressed**:
- ISSUE-024: No Audit Log Retention Policy

**Exit Criteria**:
- Audit log retention policy documented
- Audit log immutability implemented (append-only)
- Audit log completeness tests implemented
- Audit log monitoring implemented
- Policy enforced across all services

**Invariants Enforced**:
- INV-003: Audited Super Admin Access

**Test Requirements**:
- Audit log completeness tests
- Audit log immutability tests
- Audit log retention tests

**Platform Assignment**: Manus  
**Parallelizable**: Yes (independent of other processes)  
**Effort**: 1 week  
**Owner**: Core Services Team

**PaA Readiness**: Execution-ready  
**Missing Inputs**: None

---

### Wave R5: Scale Readiness

**Duration**: 4-6 weeks  
**Goal**: Implement architectural improvements for scale  
**Parallelization**: High  
**Dependencies**: Wave R2 complete (need test infrastructure)

#### Phase R5-A: Create Cross-Service Integration Tests

**Scope**: Create integration tests to verify service boundaries and contracts

**Issues Addressed**:
- ISSUE-013: No Cross-Service Integration Tests

**Exit Criteria**:
- Integration test framework established
- Integration tests for tenant isolation across services
- Integration tests for data consistency
- Integration tests for API contracts
- Integration tests for service dependencies
- All integration tests passing

**Invariants Enforced**:
- INV-001: Multi-Tenant by Design
- INV-002: Strict Tenant Isolation

**Test Requirements**:
- Cross-service tenant isolation tests
- Cross-service data consistency tests
- API contract tests
- Service dependency tests

**Platform Assignment**: Manus  
**Parallelizable**: Partially (requires unit tests to exist first)  
**Effort**: 2-3 weeks  
**Owner**: Platform Team

**PaA Readiness**: Execution-ready  
**Missing Inputs**: None (but requires Wave R2 completion)

---

#### Phase R5-B: Implement Cross-Repository Dependency Tracking

**Scope**: Create tooling to track and validate cross-repository dependencies

**Issues Addressed**:
- ISSUE-014: No Cross-Repository Dependency Tracking

**Exit Criteria**:
- Dependency tracking tooling implemented
- Dependency graph visualization created
- Automated dependency validation implemented
- Dependency versioning strategy documented
- Compatibility matrix created

**Invariants Enforced**:
- INV-009: Extensibility Without Fragmentation

**Test Requirements**:
- Dependency validation tests
- Broken reference detection tests

**Platform Assignment**: Manus  
**Parallelizable**: Yes (independent of other improvements)  
**Effort**: 1-2 weeks  
**Owner**: Platform Team

**PaA Readiness**: Execution-ready  
**Missing Inputs**: None

---

#### Phase R5-C: Create Shared Type Library

**Scope**: Create shared type library repository with common types used across services

**Issues Addressed**:
- ISSUE-015: No Shared Type Library

**Exit Criteria**:
- Shared type library repository created
- Common types extracted (TenantContext, ActorType, etc.)
- Type versioning strategy established
- All implementations updated to use shared types
- Type compatibility verified

**Invariants Enforced**:
- INV-009: Extensibility Without Fragmentation

**Test Requirements**:
- Type compatibility tests
- Type versioning tests

**Platform Assignment**: Manus  
**Parallelizable**: Yes (independent of other improvements)  
**Effort**: 2 weeks  
**Owner**: Platform Team

**PaA Readiness**: Execution-ready  
**Missing Inputs**: None

---

#### Phase R5-D: Implement Database Migration Strategy

**Scope**: Implement database migration tooling and strategy across all services

**Issues Addressed**:
- ISSUE-016: No Database Migration Strategy

**Exit Criteria**:
- Database migration tooling implemented (Alembic for Python, Knex for Node.js)
- Migration strategy documented
- Migration files created for existing schemas
- Rollback strategy implemented
- Zero-downtime migration strategy documented
- Automated migration execution in deployment pipeline

**Invariants Enforced**:
- INV-008: Backward-Compatible Evolution

**Test Requirements**:
- Migration tests
- Rollback tests
- Data integrity tests

**Platform Assignment**: Mixed (depends on database technology per service)  
**Parallelizable**: Yes (can implement per-service in parallel)  
**Effort**: 3 weeks  
**Owner**: All Teams

**PaA Readiness**: Execution-ready  
**Missing Inputs**: None

---

#### Phase R5-E: Standardize Error Handling

**Scope**: Create standardized error format and error handling library

**Issues Addressed**:
- ISSUE-017: Inconsistent Error Handling

**Exit Criteria**:
- Standardized error format defined
- Error handling library created
- All services updated to use standard format
- Error tracing across services verified
- Documentation updated

**Invariants Enforced**: None directly (improves UX/DX)

**Test Requirements**:
- Error format tests
- Error tracing tests

**Platform Assignment**: Manus  
**Parallelizable**: Yes (can update services in parallel after standard is defined)  
**Effort**: 1-2 weeks  
**Owner**: Platform Team

**PaA Readiness**: Execution-ready  
**Missing Inputs**: None

---

#### Phase R5-F: Implement Idempotency Pattern

**Scope**: Implement idempotency keys and duplicate request handling

**Issues Addressed**:
- ISSUE-018: No Idempotency Implementation

**Exit Criteria**:
- Idempotency pattern defined
- Idempotency keys implemented for critical operations
- Duplicate request detection implemented
- Idempotency tests implemented
- Documentation updated

**Invariants Enforced**: None directly (improves financial integrity)

**Test Requirements**:
- Idempotency tests
- Duplicate request tests

**Platform Assignment**: Manus  
**Parallelizable**: Yes (can implement per-service in parallel)  
**Effort**: 2 weeks  
**Owner**: All Teams

**PaA Readiness**: Execution-ready  
**Missing Inputs**: None

---

#### Phase R5-G: Implement Upgrade/Rollback Strategy

**Scope**: Implement blue-green deployment and automated rollback

**Issues Addressed**:
- ISSUE-019: No Upgrade/Rollback Strategy

**Exit Criteria**:
- Blue-green deployment strategy implemented
- Automated rollback mechanism implemented
- Deployment health checks implemented
- Zero-downtime deployment verified
- Deployment procedures documented

**Invariants Enforced**:
- INV-008: Backward-Compatible Evolution
- INV-012: Deployment Flexibility

**Test Requirements**:
- Deployment tests
- Rollback tests
- Health check tests

**Platform Assignment**: Manus  
**Parallelizable**: No (requires infrastructure phases to be complete)  
**Effort**: 2 months  
**Owner**: Infrastructure Team

**PaA Readiness**: Execution-ready  
**Missing Inputs**: None (but requires Wave R2 completion for ID-1, ID-2, ID-3)

---

#### Phase R5-H: Implement Cost Optimization Features

**Scope**: Implement cost optimization features for Nigerian market

**Issues Addressed**:
- ISSUE-025: No Cost Optimization for Nigerian Market

**Exit Criteria**:
- Cost estimation tools implemented
- Budget alerts implemented
- Data usage optimization implemented
- Cost-sensitive feature flags implemented
- Documentation updated

**Invariants Enforced**:
- INV-007: Nigeria-First, Africa-Ready

**Test Requirements**:
- Cost estimation tests
- Budget alert tests
- Data usage tests

**Platform Assignment**: Manus  
**Parallelizable**: Yes (can implement per-service in parallel)  
**Effort**: 2-3 weeks  
**Owner**: All Teams

**PaA Readiness**: Execution-ready  
**Missing Inputs**: None

---

### Wave R6: Operational Excellence

**Duration**: 2-4 weeks  
**Goal**: Implement observability, monitoring, and operational tooling  
**Parallelization**: High  
**Dependencies**: Wave R2 complete (need baseline functionality)

#### Phase R6-A: Implement PF-5 (API Documentation & Contracts)

**Scope**: Implement automated API documentation generation from OpenAPI specs

**Issues Addressed**:
- ISSUE-026: No API Documentation Generation (PF-5 Not Implemented)

**Exit Criteria**:
- OpenAPI spec generation implemented
- API documentation generation implemented
- API contract testing implemented
- Type generation from specs implemented
- Documentation published

**Invariants Enforced**: None directly (improves DX)

**Test Requirements**:
- API contract tests
- Documentation generation tests

**Platform Assignment**: Manus  
**Parallelizable**: Yes (independent of other operational features)  
**Effort**: 1 month  
**Owner**: Platform Team

**PaA Readiness**: Execution-ready (Wave 5 phase)  
**Missing Inputs**: None

---

#### Phase R6-B: Implement ID-4 (Observability & Monitoring)

**Scope**: Implement centralized logging, distributed tracing, metrics, and alerting

**Issues Addressed**:
- ISSUE-027: No Observability & Monitoring (ID-4 Not Implemented)

**Exit Criteria**:
- Centralized logging implemented
- Distributed tracing implemented
- Metrics collection and visualization implemented
- Alerting and incident response implemented
- Operational dashboards created

**Invariants Enforced**: None directly (improves operations)

**Test Requirements**:
- Logging tests
- Tracing tests
- Metrics tests
- Alerting tests

**Platform Assignment**: Manus  
**Parallelizable**: Yes (independent of other operational features)  
**Effort**: 2 months  
**Owner**: Infrastructure Team

**PaA Readiness**: Execution-ready (Wave 5 phase)  
**Missing Inputs**: None

---

#### Phase R6-C: Implement Centralized Error Tracking

**Scope**: Integrate centralized error tracking (e.g., Sentry)

**Issues Addressed**:
- ISSUE-028: No Centralized Error Tracking

**Exit Criteria**:
- Error tracking service integrated (Sentry or similar)
- Error aggregation and deduplication configured
- Error alerting configured
- Error trend analysis dashboards created
- All services sending errors to tracking service

**Invariants Enforced**: None directly (improves operations)

**Test Requirements**:
- Error tracking tests
- Error aggregation tests

**Platform Assignment**: Manus  
**Parallelizable**: Yes (independent of other operational features)  
**Effort**: 1 month  
**Owner**: Platform Team

**PaA Readiness**: Execution-ready  
**Missing Inputs**: None (but requires standardized error format from Wave R5)

---

#### Phase R6-D: Establish Bug Bounty Program

**Scope**: Establish bug bounty program for external security researchers

**Issues Addressed**:
- ISSUE-029: No Bug Bounty Program

**Exit Criteria**:
- Bug bounty program scope defined
- Reward structure established
- Vulnerability disclosure process documented
- Researcher recognition process established
- Program launched

**Invariants Enforced**: None directly (improves security)

**Test Requirements**: None (governance process)

**Platform Assignment**: Governance (not technical)  
**Parallelizable**: Yes (independent of other operational features)  
**Effort**: Ongoing (program management)  
**Owner**: Security Team

**PaA Readiness**: Execution-ready  
**Missing Inputs**: Founder approval for budget and scope

---

## Remediation Wave Summary

| Wave | Duration | Phases | Issues Addressed | Parallelization | Dependencies |
|------|----------|--------|------------------|-----------------|--------------|
| **R1** | 1-2 weeks | 3 | 5 | High | None |
| **R2** | 4-6 weeks | 5 | 6 | High | R1 complete |
| **R3** | 4-6 weeks | 4 | 5 | Medium | R2 complete |
| **R4** | 2-3 weeks | 4 | 4 | Medium | R2 complete |
| **R5** | 4-6 weeks | 8 | 8 | High | R2 complete |
| **R6** | 2-4 weeks | 4 | 4 | High | R2 complete |
| **TOTAL** | **16-24 weeks** | **28** | **29** | - | - |

---

## Critical Path Analysis

The critical path through the remediation waves is:

1. **R1-A** (Fix CS-1 Tests) → 1 day
2. **R2-A** (CS-3 IAM Tests) → 1-2 weeks
3. **R2-B** (Suite Tests) → 2-4 weeks
4. **R3-B** (Offline-First) → 4-6 weeks
5. **R5-G** (Upgrade/Rollback) → 2 months

**Total Critical Path**: ~16-20 weeks

Other waves can run in parallel with the critical path, reducing overall timeline.

---

## Parallelization Opportunities

### Wave R1 (All Parallel)
- R1-A, R1-B, R1-C can all run in parallel
- Estimated completion: 1-2 weeks

### Wave R2 (High Parallelization)
- R2-A, R2-B, R2-C, R2-D, R2-E can all run in parallel
- Estimated completion: 4-6 weeks (longest phase)

### Wave R3 (Medium Parallelization)
- R3-A, R3-C can run in parallel
- R3-B requires PF-2 verification from R2 (partial dependency)
- R3-D blocked on Founder decision
- Estimated completion: 4-6 weeks

### Wave R4 (Medium Parallelization)
- R4-A, R4-C, R4-D can run in parallel
- R4-B requires R2 completion (sequential)
- Estimated completion: 2-3 weeks

### Wave R5 (High Parallelization)
- R5-A, R5-B, R5-C, R5-D, R5-E, R5-F, R5-H can all run in parallel
- R5-G requires infrastructure phases complete (sequential)
- Estimated completion: 4-6 weeks (or 2 months if R5-G is on critical path)

### Wave R6 (High Parallelization)
- R6-A, R6-B, R6-C, R6-D can all run in parallel
- Estimated completion: 2-4 weeks (longest phase)

---

## Platform Assignment Summary

| Platform | Phases | Percentage |
|----------|--------|------------|
| **Manus** | 25 | 89% |
| **Mixed** | 3 | 11% |
| **Governance** | 1 | 4% |

**Recommendation**: Manus is the primary execution platform for 89% of remediation work. Mixed assignments (Manus + Replit) are only for specific cases requiring different technology stacks or mobile app testing.

---

## Dependency Graph

```
R1-A ──┐
R1-B ──┼─→ R2-A ──┐
R1-C ──┘          │
                  ├─→ R3-A
                  ├─→ R3-B (requires PF-2 from R2-E)
                  ├─→ R3-C
                  ├─→ R3-D (blocked on Founder decision)
                  │
       R2-B ──────┤
       R2-C ──────┤
       R2-D ──────┤
       R2-E ──────┘
                  │
                  ├─→ R4-A
                  ├─→ R4-B (requires R2 complete)
                  ├─→ R4-C
                  ├─→ R4-D
                  │
                  ├─→ R5-A (requires R2 complete)
                  ├─→ R5-B
                  ├─→ R5-C
                  ├─→ R5-D
                  ├─→ R5-E
                  ├─→ R5-F
                  ├─→ R5-G (requires R2-C complete)
                  ├─→ R5-H
                  │
                  ├─→ R6-A
                  ├─→ R6-B
                  ├─→ R6-C (requires R5-E complete)
                  └─→ R6-D
```

---

## Founder Decision Points

The following phases are **blocked** and require Founder decisions:

### 1. R3-D: SC-1 Missing Features

**Decision Required**: Should SC-1 documented features be implemented or removed from documentation?

**Options**:
- **Option A**: Implement all documented features (offline-first POS, dashboard, inventory sync, logistics, accounting, engagement)
  - Effort: 2-4 weeks
  - Impact: Delivers full SC-1 functionality
  - Risk: Delays other remediation work
  
- **Option B**: Remove documented features from README and mark as "planned"
  - Effort: 1 day
  - Impact: Aligns documentation with reality
  - Risk: Stakeholder disappointment

**Recommendation**: Option B (document reality) for immediate remediation, then plan implementation as separate feature work

---

### 2. R3-A: Nigerian Payment Integration

**Decision Required**: Which payment gateway should be integrated?

**Options**:
- **Option A**: Paystack
- **Option B**: Flutterwave
- **Option C**: Both

**Recommendation**: Start with Paystack (more established in Nigerian market), add Flutterwave later

**Additional Input Required**: API credentials for chosen payment gateway

---

### 3. R6-D: Bug Bounty Program

**Decision Required**: Approve budget and scope for bug bounty program

**Input Required**:
- Budget allocation
- Reward structure
- Program scope (which services are in scope)

**Recommendation**: Defer until after production deployment (Wave R6 is not blocking production)

---

## PaA Readiness Summary

| Status | Phases | Percentage |
|--------|--------|------------|
| **Execution-Ready** | 26 | 93% |
| **Partially Specifiable** | 1 | 4% |
| **Blocked** | 1 | 4% |

**Execution-Ready**: 26 phases can have v2 PaA execution prompts generated immediately

**Partially Specifiable**: R3-B (Offline-First) requires PF-2 verification results from R2-E

**Blocked**: R3-D (SC-1 Missing Features) requires Founder decision

---

## Success Metrics

### Wave R1 Success Criteria
- CS-1 tests compile and pass
- All READMEs aligned with actual code
- All unknown test statuses resolved

### Wave R2 Success Criteria
- All 10 untested implementations have test suites
- Minimum 70% code coverage across all implementations
- All tests passing in CI/CD

### Wave R3 Success Criteria
- Nigerian payment integration operational
- Offline-first patterns implemented and tested
- Mobile-first validation complete

### Wave R4 Success Criteria
- CI/CD fallback flags removed
- Wave 4 re-verified and documented
- Quality gates enforced

### Wave R5 Success Criteria
- Cross-service integration tests passing
- Architectural improvements complete
- Scale readiness verified

### Wave R6 Success Criteria
- Observability and monitoring operational
- API documentation published
- Operational excellence achieved

---

**Status**: Wave Plan Complete  
**Next Step**: Create Master Control Board update proposals
