# Wave 5: Candidate Phases

**Document Version:** 1.0  
**Date:** January 31, 2026  
**Status:** 🟡 **Draft - Awaiting Founder Approval**  
**Authority:** Manus AI (Planning Agent)

---

## Executive Summary

This document identifies and defines three (3) candidate phases for Wave 5 execution, addressing the three platform concerns specified by the Founder: Automated Testing & CI/CD, API Documentation Standards, and Platform Observability. These phases represent critical infrastructure and quality improvements that will enhance the platform's reliability, maintainability, and operational excellence.

**Proposed Wave 5 Phases:**

1. **PF-4: Automated Testing & CI/CD Infrastructure**
2. **PF-5: API Documentation Standards (OpenAPI/Swagger)**
3. **ID-3: Platform Observability & Monitoring**

All three phases are classified as **Platform Foundation** or **Infrastructure** work, as they provide horizontal capabilities that span all platform layers and deployment modes.

---

## Phase 1: PF-4 - Automated Testing & CI/CD Infrastructure

### Phase Identification

| Attribute | Value |
|-----------|-------|
| **Phase ID** | PF-4 |
| **Phase Name** | Automated Testing & CI/CD Infrastructure |
| **Platform Layer** | Platform Foundation |
| **Deployment Mode** | All (affects all deployment modes) |
| **Actor Scope** | Internal (Development & Operations teams) |
| **Connectivity Mode** | N/A (Infrastructure) |
| **Geographic Assumption** | Global-Ready |
| **Execution Ownership** | Manus (recommended) |
| **Risk Class** | Infrastructure, Security |

### Objective

Implement comprehensive automated testing infrastructure and CI/CD pipelines that enable continuous quality assurance across the multi-repository platform topology. This phase focuses on **test execution automation** and **CI/CD orchestration**, not on rewriting existing tests or business logic.

### Scope

**In Scope:**

1. **Test Execution Automation**
   - Automated unit test execution across all repositories
   - Automated integration test execution with dependency management
   - Automated end-to-end (E2E) test execution with environment provisioning
   - Test result aggregation and reporting

2. **CI/CD Pipeline Infrastructure**
   - GitHub Actions workflows for all repositories
   - Multi-repository coordination and dependency handling
   - Quality gates enforcement (test coverage, linting, security scans)
   - Automated build and artifact generation
   - Branch protection rules and PR validation

3. **Multi-Repository Topology Support**
   - Cross-repository test orchestration
   - Dependency-aware test execution (Foundation → Core Services → Capabilities → Suites)
   - Parallel test execution where dependencies allow
   - Repository-specific and cross-repository test suites

4. **Test Infrastructure**
   - Test database provisioning and teardown
   - Test environment configuration management
   - Mock/stub infrastructure for external dependencies
   - Test data generation and management utilities

**Out of Scope:**

- Rewriting existing test definitions (tests are assumed to exist)
- Modifying business logic or application code
- Creating new test cases (only infrastructure for running existing tests)
- Performance/load testing infrastructure (future phase)
- Security testing tools (future phase, though basic security scans are in scope)

### Dependencies

- **Prerequisites:** All Wave 4 phases complete (✅)
- **Parallel Execution:** Can run in parallel with PF-5 (API Documentation)
- **Sequential Requirement:** Should complete before or alongside ID-3 (Observability) to enable monitoring of CI/CD pipelines

### Execution Readiness

**Status:** ✅ **Fully Specifiable Now**

**Current State Analysis:**

- ✅ Test structures exist in most implementations (`tests/` directories present)
- ✅ Test frameworks configured (Jest for TypeScript/JavaScript, pytest for Python)
- ✅ Test scripts defined in `package.json` files
- ❌ No CI/CD pipelines currently exist (no `.github/workflows/`)
- ❌ No automated test execution on PRs or merges
- ❌ No quality gates or enforcement mechanisms

**Readiness Assessment:**

This phase is fully specifiable and ready for execution. The test infrastructure exists at a basic level, and the requirements are clear. No Founder clarification is required.

### Deliverables

1. **GitHub Actions Workflows**
   - `.github/workflows/test.yml` for each repository
   - `.github/workflows/ci.yml` for continuous integration
   - `.github/workflows/cd.yml` for continuous deployment (staging)

2. **Test Execution Scripts**
   - Cross-repository test orchestration scripts
   - Test environment setup and teardown scripts
   - Test result aggregation and reporting tools

3. **Documentation**
   - CI/CD pipeline architecture document
   - Developer guide for running tests locally and in CI
   - Troubleshooting guide for common CI/CD issues

4. **Quality Gates Configuration**
   - Branch protection rules for all repositories
   - Required status checks configuration
   - Code coverage thresholds and enforcement

### Estimated Complexity

**Medium-High Complexity**

- Multi-repository coordination adds complexity
- Cross-repository dependency management requires careful orchestration
- GitHub Actions expertise required
- Test environment provisioning can be complex

---

## Phase 2: PF-5 - API Documentation Standards (OpenAPI/Swagger)

### Phase Identification

| Attribute | Value |
|-----------|-------|
| **Phase ID** | PF-5 |
| **Phase Name** | API Documentation Standards (OpenAPI/Swagger) |
| **Platform Layer** | Platform Foundation |
| **Deployment Mode** | All (affects all deployment modes) |
| **Actor Scope** | All (documentation serves all actors) |
| **Connectivity Mode** | Fully Online (documentation access) |
| **Geographic Assumption** | Global-Ready |
| **Execution Ownership** | Manus (recommended) |
| **Risk Class** | UX, Infrastructure |

### Objective

Adopt OpenAPI (Swagger) as the canonical API documentation standard for the WebWaka platform and implement tooling to generate interactive, always-up-to-date API documentation directly from code. This phase establishes a platform-wide standard for API documentation, versioning, and exposure.

### Scope

**In Scope:**

1. **OpenAPI Standard Adoption**
   - Define OpenAPI 3.0+ as the canonical API documentation format
   - Establish naming conventions and documentation standards
   - Define schema reuse patterns and best practices

2. **Documentation Generation**
   - Implement code-first OpenAPI generation for TypeScript/JavaScript (using decorators or comments)
   - Implement code-first OpenAPI generation for Python (using FastAPI or similar)
   - Automated OpenAPI spec generation in CI/CD pipelines
   - Validation of generated specs against OpenAPI standards

3. **Documentation Storage and Organization**
   - Define where OpenAPI specs live (e.g., `/docs/api/openapi.yaml` in each repository)
   - Centralized API documentation portal (aggregates all specs)
   - Version-specific documentation (support for multiple API versions)

4. **Interactive Documentation**
   - Swagger UI deployment for interactive API exploration
   - Redoc or similar for polished, read-only documentation
   - API playground/sandbox for testing endpoints

5. **Cross-Layer Compatibility**
   - Ensure consistency across Core Services, Capabilities, and Suites
   - Define how Suites expose Capability APIs
   - Establish API versioning and backward compatibility rules

6. **Exposure and Access Control**
   - Define which APIs are public vs. internal
   - API documentation access control (public, partner-only, internal-only)
   - API key management for documentation access (if needed)

**Out of Scope:**

- Rewriting existing API implementations
- Changing API contracts or breaking changes
- API gateway implementation (future phase)
- API rate limiting implementation (exists but not modified here)
- GraphQL or other API paradigms (OpenAPI/REST only)

### Dependencies

- **Prerequisites:** All Wave 4 phases complete (✅)
- **Parallel Execution:** Can run in parallel with PF-4 (Testing & CI/CD)
- **Sequential Requirement:** None (independent phase)

### Execution Readiness

**Status:** ✅ **Fully Specifiable Now**

**Current State Analysis:**

- ✅ APIs exist across Core Services, Capabilities, and Suites
- ✅ Manual API documentation exists (e.g., `API_DOCUMENTATION.md` in CS-1)
- ❌ No OpenAPI specifications currently exist
- ❌ No automated documentation generation
- ❌ No interactive API documentation (Swagger UI)
- ❌ No centralized API documentation portal

**Readiness Assessment:**

This phase is fully specifiable and ready for execution. The APIs are well-defined, and the requirements are clear. No Founder clarification is required.

### Deliverables

1. **OpenAPI Specifications**
   - OpenAPI 3.0+ spec for each service/suite
   - Validated and linted specs
   - Version-controlled specs in each repository

2. **Documentation Generation Tooling**
   - Code annotation/decorator libraries for TypeScript and Python
   - CI/CD integration for automated spec generation
   - Spec validation and linting tools

3. **Documentation Portal**
   - Centralized API documentation website
   - Swagger UI integration for interactive exploration
   - Redoc or similar for polished documentation
   - Search and navigation across all APIs

4. **Documentation**
   - OpenAPI standards and conventions guide
   - Developer guide for documenting APIs
   - API versioning and backward compatibility policy

5. **Governance Artifacts**
   - API documentation checklist (part of PaA model)
   - API review process for new endpoints
   - Breaking change policy and communication plan

### Estimated Complexity

**Medium Complexity**

- OpenAPI generation is well-supported by existing tools
- Multi-repository aggregation requires coordination
- Centralized portal deployment is straightforward
- Standards definition requires careful thought but is not technically complex

---

## Phase 3: ID-4 - Platform Observability & Monitoring

### Phase Identification

| Attribute | Value |
|-----------|-------|
| **Phase ID** | ID-4 |
| **Phase Name** | Platform Observability & Monitoring |
| **Platform Layer** | Infrastructure |
| **Deployment Mode** | All (with mode-specific configurations) |
| **Actor Scope** | Super Admin, Partner (for partner-deployed), Client (for self-hosted) |
| **Connectivity Mode** | Fully Online (with offline-safe degradation) |
| **Geographic Assumption** | Nigeria-First (cost-aware), Global-Ready |
| **Execution Ownership** | Manus (recommended) |
| **Risk Class** | Infrastructure, Security, Data |

### Objective

Implement comprehensive platform observability infrastructure including centralized logging, metrics collection, distributed tracing, and health checks. This phase enables operational excellence, proactive issue detection, and data-driven decision-making across all deployment modes while respecting Nigeria-first cost realities.

### Scope

**In Scope:**

1. **Centralized Logging**
   - Structured logging standards (JSON format with required fields)
   - Log aggregation infrastructure (e.g., Loki, CloudWatch, or cost-effective alternative)
   - Log retention policies (different retention for different log levels)
   - Log query and search capabilities
   - Multi-deployment mode support (SaaS, Partner-Deployed, Self-Hosted)

2. **Metrics Collection**
   - Application metrics (request rates, response times, error rates)
   - Business metrics (transactions, revenue, user activity)
   - Infrastructure metrics (CPU, memory, disk, network)
   - Metrics storage and visualization (e.g., Prometheus + Grafana, or cost-effective alternative)
   - Custom metrics definition and collection

3. **Distributed Tracing**
   - Request tracing across services (trace ID propagation)
   - Span collection and correlation
   - Trace visualization and analysis
   - Performance bottleneck identification
   - Cross-repository request tracking

4. **Health Checks and SLIs/SLOs**
   - Standardized health check endpoints (`/health`, `/ready`)
   - Service-level indicators (SLIs) definition
   - Service-level objectives (SLOs) definition
   - Uptime monitoring and alerting
   - Dependency health checks

5. **Alerting and Notifications**
   - Alert rule definition and management
   - Multi-channel alerting (email, SMS, Slack, PagerDuty)
   - Alert escalation policies
   - Alert fatigue prevention (intelligent grouping and suppression)

6. **Deployment Mode Considerations**
   - **Shared SaaS:** Centralized observability with WebWaka-managed infrastructure
   - **Partner-Deployed:** Partner-controlled observability with optional WebWaka aggregation
   - **Self-Hosted:** Client-controlled observability with optional telemetry sharing

7. **Cost Awareness (Nigeria-First)**
   - Sampling strategies to reduce data volume
   - Tiered retention policies (hot/warm/cold storage)
   - Cost-effective tooling choices (open-source preferred)
   - Bandwidth-aware telemetry transmission

**Out of Scope:**

- Application Performance Monitoring (APM) agents (future phase)
- Real User Monitoring (RUM) for frontend (future phase)
- Advanced anomaly detection and AI-powered insights (future phase)
- Security Information and Event Management (SIEM) integration (future phase)
- Chaos engineering and resilience testing (future phase)

### Dependencies

- **Prerequisites:** All Wave 4 phases complete (✅)
- **Parallel Execution:** Can run in parallel with PF-4 and PF-5, but benefits from PF-4 (CI/CD) being complete for monitoring pipeline health
- **Sequential Requirement:** None (independent phase)

### Execution Readiness

**Status:** ⚠️ **Mostly Specifiable - Minor Clarifications Needed**

**Current State Analysis:**

- ✅ Basic logging exists (Winston logger in most services)
- ✅ Console-based logging configured
- ❌ No centralized log aggregation
- ❌ No metrics collection infrastructure
- ❌ No distributed tracing
- ❌ No standardized health check endpoints
- ❌ No alerting infrastructure

**Clarifications Needed:**

1. **Tooling Preferences:**
   - **Question:** Does the Founder have preferences for observability tooling?
   - **Options:**
     - **Option A:** Open-source stack (Prometheus + Grafana + Loki + Jaeger)
     - **Option B:** Cloud-native stack (AWS CloudWatch + X-Ray)
     - **Option C:** Hybrid (open-source with cloud backup)
   - **Recommendation:** Option A (open-source) for cost-effectiveness and portability across deployment modes
   - **Blocking?** No - can proceed with Option A as default and adjust if needed

2. **Telemetry Sharing Policy:**
   - **Question:** For partner-deployed and self-hosted instances, should telemetry be shared with WebWaka?
   - **Options:**
     - **Option A:** Opt-in telemetry sharing (privacy-first)
     - **Option B:** Opt-out telemetry sharing (data-first)
     - **Option C:** No telemetry sharing (fully isolated)
   - **Recommendation:** Option A (opt-in) to respect partner/client privacy while enabling platform improvement
   - **Blocking?** No - can implement with opt-in as default

3. **Alert Routing:**
   - **Question:** Who receives alerts in different deployment modes?
   - **Options:**
     - **SaaS:** WebWaka operations team
     - **Partner-Deployed:** Partner operations team (with optional WebWaka escalation)
     - **Self-Hosted:** Client operations team (no WebWaka involvement)
   - **Recommendation:** As described above
   - **Blocking?** No - this is the logical default

**Readiness Assessment:**

This phase is mostly specifiable and can proceed with reasonable defaults. The clarifications above are preferences, not blockers. Recommend proceeding with the recommendations and adjusting based on Founder feedback.

### Deliverables

1. **Observability Infrastructure**
   - Centralized logging infrastructure (deployment manifests, configuration)
   - Metrics collection infrastructure (Prometheus or equivalent)
   - Distributed tracing infrastructure (Jaeger or equivalent)
   - Visualization dashboards (Grafana or equivalent)

2. **Instrumentation Libraries**
   - Logging library with structured logging standards
   - Metrics collection library (Prometheus client or equivalent)
   - Tracing library (OpenTelemetry or equivalent)
   - Health check middleware for all services

3. **Standardized Implementations**
   - Health check endpoints in all services
   - Structured logging in all services
   - Metrics collection in all services
   - Distributed tracing in all services

4. **Dashboards and Visualizations**
   - Platform-wide overview dashboard
   - Service-specific dashboards
   - Business metrics dashboards
   - Infrastructure metrics dashboards

5. **Alerting Configuration**
   - Alert rules for critical issues
   - Alert routing configuration
   - Runbooks for common alerts
   - On-call rotation setup (if applicable)

6. **Documentation**
   - Observability architecture document
   - Runbook for common operational tasks
   - Dashboard user guide
   - Troubleshooting guide for observability infrastructure

7. **Deployment Mode Configurations**
   - SaaS observability deployment
   - Partner-deployed observability template
   - Self-hosted observability template

### Estimated Complexity

**High Complexity**

- Multi-deployment mode support adds significant complexity
- Distributed tracing across services requires careful instrumentation
- Cost-aware design requires thoughtful architecture
- Centralized infrastructure deployment and management is complex
- Telemetry data volume can be large and requires careful management

---

## Summary of Candidate Phases

| Phase ID | Phase Name | Layer | Complexity | Parallel? | Execution Readiness |
|----------|------------|-------|------------|-----------|---------------------|
| **PF-4** | Automated Testing & CI/CD Infrastructure | Foundation | Medium-High | Yes (with PF-5) | ✅ Fully Specifiable |
| **PF-5** | API Documentation Standards (OpenAPI/Swagger) | Foundation | Medium | Yes (with PF-4) | ✅ Fully Specifiable |
| **ID-4** | Platform Observability & Monitoring | Infrastructure | High | Yes (all) | ⚠️ Minor Clarifications |

---

## Dependency Graph

```
Wave 4 (Complete)
       ↓
┌──────┴──────┐
│             │
PF-4          PF-5
(Testing)     (API Docs)
│             │
└──────┬──────┘
       ↓
     ID-4
(Observability)
```

**Notes:**
- PF-4 and PF-5 can run in parallel (no dependencies)
- ID-4 can run in parallel with PF-4 and PF-5, but benefits from PF-4 being complete
- Recommended execution: PF-4 and PF-5 in parallel, then ID-4 (or all three in parallel if resources allow)

---

## Recommended Execution Strategy

### Option A: Sequential (Conservative)

1. **Wave 5a:** PF-4 and PF-5 in parallel (2 phases)
2. **Wave 5b:** ID-4 (1 phase)

**Pros:** Lower risk, easier coordination, allows learning from PF-4/PF-5 before tackling ID-4  
**Cons:** Longer total time to completion

### Option B: Parallel (Aggressive)

1. **Wave 5:** PF-4, PF-5, and ID-4 in parallel (3 phases)

**Pros:** Faster completion, all three concerns addressed simultaneously  
**Cons:** Higher coordination overhead, requires more agent resources

### Recommendation

**Option A (Sequential)** is recommended for the following reasons:

1. **Risk Management:** ID-4 is the most complex phase and benefits from lessons learned in PF-4
2. **Resource Efficiency:** PF-4 and PF-5 can be executed by Manus in parallel, then ID-4 can receive full focus
3. **Testing Benefits:** PF-4 (CI/CD) will enable better testing of ID-4 (Observability) if completed first
4. **Incremental Value:** PF-4 and PF-5 deliver immediate value to developers, while ID-4 is more operational

---

## Next Steps

1. **Founder Review:** Review this candidate phases document and provide approval or feedback
2. **Clarifications:** Address the three minor clarifications for ID-4 (tooling, telemetry, alerting)
3. **Execution Prompts:** Upon approval, create detailed execution prompts for each phase
4. **Platform Assignment:** Finalize platform assignments (Manus vs. Replit) for each phase
5. **MCB Updates:** Update Master Control Board with new phase entries

---

**Document Status:** 🟡 **Draft - Awaiting Founder Approval**  
**Prepared By:** Manus AI  
**Date:** January 31, 2026

---

**End of Candidate Phases Document**
