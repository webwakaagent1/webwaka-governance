# EXECUTION PROMPT: Repository Topology Migration - Phase 4

**Phase:** Phase 4 - Capabilities Repository Migration  
**Status:** 🟡 **READY FOR EXECUTION**  
**Version:** 1.0  
**Date:** January 30, 2026  
**Authority:** Founder Approved (Planning Complete)  
**Executor:** Manus

---

## 1. CONTEXT

This is the formal execution prompt for **Phase 4** of the Repository Topology Migration. This phase creates the `webwaka-capabilities` repository and migrates all corresponding implementation code from the original `webwaka` monorepo while preserving complete Git history.

**Planning Documents:**
- `/docs/planning/repository-topology-migration/`
- `/docs/planning/repository-topology-migration/PHASE_4_MIGRATION_STRATEGY.md`

**Master Control Board Item:** REPO-MIG-1

---

## 2. EXECUTION PROMPT: Phase 4 - Capabilities Migration (v1)

### Objective

Create the `webwaka-capabilities` repository and migrate all Business Capabilities (CB) implementation code from the `webwaka` monorepo, preserving full Git history.

### Pre-Execution Checklist

- [ ] Verify Phase 3 is marked as 🟢 Complete in the MCB.
- [ ] Full backup of `webwaka` repository exists (`webwaka-backup-20260130-124825.tar.gz`).
- [ ] GitHub organization `webwakaagent1` has capacity for new repositories.

### Deliverables

1.  **New Repository:** `webwaka-capabilities` created.
2.  **Migrated Content:** All content from `/implementations/cb1-mlas-capability/`, `/implementations/CB-2_REPORTING_ANALYTICS_CAPABILITY/`, `/implementations/CB-3_CONTENT_MANAGEMENT_CAPABILITY/`, and `/implementations/cb4-inventory-management/` with full Git history.
3.  **Updated Migration Status:** `MIGRATION_STATUS.md` updated to reflect Phase 4 completion.

### Execution Steps

#### Step 4.1: Create `webwaka-capabilities` Repository

```bash
# Create new repository on GitHub via API
curl -X POST -H "Authorization: token <GITHUB_PAT>" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/user/repos \
  -d '{"name":"webwaka-capabilities","description":"WebWaka Business Capabilities Layer (CB Phases)"}'
```

#### Step 4.2: Migrate Capabilities Implementations

```bash
# Clone original monorepo
cd /home/ubuntu
git clone https://github.com/webwakaagent1/webwaka.git webwaka-migration-capabilities
cd webwaka-migration-capabilities

# Extract CB implementations with history
git filter-repo --path implementations/cb1-mlas-capability/ --path implementations/CB-2_REPORTING_ANALYTICS_CAPABILITY/ --path implementations/CB-3_CONTENT_MANAGEMENT_CAPABILITY/ --path implementations/cb4-inventory-management/ --force

# Push to new capabilities repository
git remote add capabilities https://github.com/webwakaagent1/webwaka-capabilities.git
git push capabilities main
```

#### Step 4.3: Update Migration Status

Update `docs/planning/repository-topology-migration/MIGRATION_STATUS.md` in the `webwaka-governance` repository to mark Phase 4 as complete and add the final commit SHA for the new repository.

### Completion Criteria

Phase 4 is complete when:

1.  ✅ `webwaka-capabilities` repository is operational with all CB implementations and full Git history.
2.  ✅ `MIGRATION_STATUS.md` is updated to reflect Phase 4 completion.
3.  ✅ This prompt is updated with backlinks (see Section 3).
4.  ✅ Founder approval is requested for Phase 5.

---

## 3. EXECUTION BACKLINKS

**Status:** ✅ **EXECUTED**

- ✅ **Capabilities repository URL:** https://github.com/webwakaagent1/webwaka-capabilities
- ✅ **Capabilities final commit SHA:** `webwaka-capabilities@bed4b9d`
- ✅ **Capabilities commits migrated:** 9 commits with full Git history
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
