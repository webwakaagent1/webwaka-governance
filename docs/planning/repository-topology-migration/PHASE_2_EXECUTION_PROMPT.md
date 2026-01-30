# EXECUTION PROMPT: Repository Topology Migration - Phase 2

**Phase:** Phase 2 - Foundation & Infrastructure Repository Migration  
**Status:** 🟡 **READY FOR EXECUTION**  
**Version:** 1.0  
**Date:** January 30, 2026  
**Authority:** Founder Approved (Planning Complete)  
**Executor:** Manus

---

## 1. CONTEXT

This is the formal execution prompt for **Phase 2** of the Repository Topology Migration. This phase creates the `webwaka-platform-foundation` and `webwaka-infrastructure` repositories and migrates all corresponding implementation code from the original `webwaka` monorepo while preserving complete Git history.

**Planning Documents:**
- `/docs/planning/repository-topology-migration/`
- `/docs/planning/repository-topology-migration/PHASE_2_MIGRATION_STRATEGY.md`

**Master Control Board Item:** REPO-MIG-1

---

## 2. EXECUTION PROMPT: Phase 2 - Foundation & Infrastructure Migration (v1)

### Objective

Create the `webwaka-platform-foundation` and `webwaka-infrastructure` repositories and migrate all Platform Foundation (PF) and Infrastructure & Deployment (ID) implementation code from the `webwaka` monorepo, preserving full Git history.

### Pre-Execution Checklist

- [ ] Verify Phase 1 is marked as 🟢 Complete in the MCB.
- [ ] Full backup of `webwaka` repository exists (`webwaka-backup-20260130-124825.tar.gz`).
- [ ] GitHub organization `webwakaagent1` has capacity for new repositories.

### Deliverables

1.  **New Repository:** `webwaka-platform-foundation` created.
2.  **Migrated Content (Foundation):** All content from `/implementations/pf-1/`, `/implementations/pf-2/`, and `/implementations/pf-3/` with full Git history.
3.  **New Repository:** `webwaka-infrastructure` created.
4.  **Migrated Content (Infrastructure):** All content from `/implementations/id-1/` and `/implementations/id-3/` with full Git history.
5.  **Updated Migration Status:** `MIGRATION_STATUS.md` updated to reflect Phase 2 completion.

### Execution Steps

#### Step 2.1: Create `webwaka-platform-foundation` Repository

```bash
# Create new repository on GitHub via API
curl -X POST -H "Authorization: token <GITHUB_PAT>" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/user/repos \
  -d '{"name":"webwaka-platform-foundation","description":"WebWaka Platform Foundation Layer (PF Phases)"}'
```

#### Step 2.2: Migrate Foundation Implementations

```bash
# Clone original monorepo
cd /home/ubuntu
git clone https://github.com/webwakaagent1/webwaka.git webwaka-migration-foundation
cd webwaka-migration-foundation

# Extract PF implementations with history
git filter-repo --path implementations/pf-1/ --path implementations/pf-2/ --path implementations/pf-3/ --force

# Push to new foundation repository
git remote add foundation https://github.com/webwakaagent1/webwaka-platform-foundation.git
git push foundation main
```

#### Step 2.3: Create `webwaka-infrastructure` Repository

```bash
# Create new repository on GitHub via API
curl -X POST -H "Authorization: token <GITHUB_PAT>" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/user/repos \
  -d '{"name":"webwaka-infrastructure","description":"WebWaka Infrastructure & Deployment Layer (ID Phases)"}'
```

#### Step 2.4: Migrate Infrastructure Implementations

```bash
# Clone original monorepo again for a clean slate
cd /home/ubuntu
rm -rf webwaka-migration-infra
git clone https://github.com/webwakaagent1/webwaka.git webwaka-migration-infra
cd webwaka-migration-infra

# Extract ID implementations with history
git filter-repo --path implementations/id-1/ --path implementations/id-3/ --force

# Push to new infrastructure repository
git remote add infrastructure https://github.com/webwakaagent1/webwaka-infrastructure.git
git push infrastructure main
```

#### Step 2.5: Update Migration Status

Update `docs/planning/repository-topology-migration/MIGRATION_STATUS.md` in the `webwaka-governance` repository to mark Phase 2 as complete and add the final commit SHAs for both new repositories.

### Completion Criteria

Phase 2 is complete when:

1.  ✅ `webwaka-platform-foundation` repository is operational with all PF implementations and full Git history.
2.  ✅ `webwaka-infrastructure` repository is operational with all ID implementations and full Git history.
3.  ✅ `MIGRATION_STATUS.md` is updated to reflect Phase 2 completion.
4.  ✅ This prompt is updated with backlinks (see Section 3).
5.  ✅ Founder approval is requested for Phase 3.

---

## 3. EXECUTION BACKLINKS (To be updated upon completion)

**Status:** ⚪ **NOT EXECUTED**

- [ ] Foundation repository URL: `https://github.com/webwakaagent1/webwaka-platform-foundation`
- [ ] Foundation final commit SHA: `webwaka-platform-foundation@[SHA]`
- [ ] Infrastructure repository URL: `https://github.com/webwakaagent1/webwaka-infrastructure`
- [ ] Infrastructure final commit SHA: `webwaka-infrastructure@[SHA]`
- [ ] Completion date: `[DATE]`

---

## 4. PROMPT INVARIANT COMPLIANCE

This prompt complies with all platform invariants, including:

- ✅ **INV-011 (PaA Execution)**
- ✅ **INV-012v2 (Multi-Repository Topology)**
- ✅ **Prompt Invariant Checklist**

---

**Status:** 🟡 **READY FOR EXECUTION**  
**Awaiting Founder Approval**
