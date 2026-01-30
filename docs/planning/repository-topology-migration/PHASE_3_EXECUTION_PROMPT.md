# EXECUTION PROMPT: Repository Topology Migration - Phase 3

**Phase:** Phase 3 - Core Services Repository Migration  
**Status:** 🟡 **READY FOR EXECUTION**  
**Version:** 1.0  
**Date:** January 30, 2026  
**Authority:** Founder Approved (Planning Complete)  
**Executor:** Manus

---

## 1. CONTEXT

This is the formal execution prompt for **Phase 3** of the Repository Topology Migration. This phase creates the `webwaka-core-services` repository and migrates all corresponding implementation code from the original `webwaka` monorepo while preserving complete Git history.

**Planning Documents:**
- `/docs/planning/repository-topology-migration/`
- `/docs/planning/repository-topology-migration/PHASE_3_MIGRATION_STRATEGY.md`

**Master Control Board Item:** REPO-MIG-1

---

## 2. EXECUTION PROMPT: Phase 3 - Core Services Migration (v1)

### Objective

Create the `webwaka-core-services` repository and migrate all Core Services (CS) implementation code from the `webwaka` monorepo, preserving full Git history.

### Pre-Execution Checklist

- [ ] Verify Phase 2 is marked as 🟢 Complete in the MCB.
- [ ] Full backup of `webwaka` repository exists (`webwaka-backup-20260130-124825.tar.gz`).
- [ ] GitHub organization `webwakaagent1` has capacity for new repositories.

### Deliverables

1.  **New Repository:** `webwaka-core-services` created.
2.  **Migrated Content:** All content from `/implementations/CS-1/`, `/implementations/cs2-notification-service/`, `/implementations/CS-3_IAM_V2/`, and `/implementations/cs4-pricing-billing-service/` with full Git history.
3.  **Updated Migration Status:** `MIGRATION_STATUS.md` updated to reflect Phase 3 completion.

### Execution Steps

#### Step 3.1: Create `webwaka-core-services` Repository

```bash
# Create new repository on GitHub via API
curl -X POST -H "Authorization: token <GITHUB_PAT>" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/user/repos \
  -d '{"name":"webwaka-core-services","description":"WebWaka Core Services Layer (CS Phases)"}'
```

#### Step 3.2: Migrate Core Services Implementations

```bash
# Clone original monorepo
cd /home/ubuntu
git clone https://github.com/webwakaagent1/webwaka.git webwaka-migration-core-services
cd webwaka-migration-core-services

# Extract CS implementations with history
git filter-repo --path implementations/CS-1/ --path implementations/cs2-notification-service/ --path implementations/CS-3_IAM_V2/ --path implementations/cs4-pricing-billing-service/ --force

# Push to new core services repository
git remote add core-services https://github.com/webwakaagent1/webwaka-core-services.git
git push core-services main
```

#### Step 3.3: Update Migration Status

Update `docs/planning/repository-topology-migration/MIGRATION_STATUS.md` in the `webwaka-governance` repository to mark Phase 3 as complete and add the final commit SHA for the new repository.

### Completion Criteria

Phase 3 is complete when:

1.  ✅ `webwaka-core-services` repository is operational with all CS implementations and full Git history.
2.  ✅ `MIGRATION_STATUS.md` is updated to reflect Phase 3 completion.
3.  ✅ This prompt is updated with backlinks (see Section 3).
4.  ✅ Founder approval is requested for Phase 4.

---

## 3. EXECUTION BACKLINKS

**Status:** ✅ **EXECUTED**

- ✅ **Core Services repository URL:** https://github.com/webwakaagent1/webwaka-core-services
- ✅ **Core Services final commit SHA:** `webwaka-core-services@abb6c62`
- ✅ **Core Services commits migrated:** 7 commits with full Git history
- ✅ **Completion date:** January 30, 2026
- 🟡 **Founder approval:** Awaiting verification

---

## 4. PROMPT INVARIANT COMPLIANCE

This prompt complies with all platform invariants, including:

- ✅ **INV-011 (PaA Execution)**
- ✅ **INV-012v2 (Multi-Repository Topology)**
- ✅ **Prompt Invariant Checklist**

---

**Status:** ✅ **EXECUTION COMPLETE**  
**Awaiting Founder Verification**
