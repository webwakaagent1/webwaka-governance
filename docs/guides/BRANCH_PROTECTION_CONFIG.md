# Branch Protection Configuration Guide

**Phase:** PF-4  
**Date:** January 31, 2026  
**Purpose:** Configuration guide for GitHub branch protection rules

---

## Overview

This document provides the configuration for branch protection rules that have been applied to all WebWaka platform repositories. These rules enforce quality gates and prevent low-quality code from being merged.

---

## Branch Protection Rules for `main` Branch

### Required Configuration (All Repositories)

**Repository Settings → Branches → Branch protection rules → Add rule**

**Branch name pattern:** `main`

#### 1. Protect matching branches
- ✅ **Require a pull request before merging**
  - ✅ Require approvals: 1
  - ✅ Dismiss stale pull request approvals when new commits are pushed
  - ❌ Require review from Code Owners (not configured yet)

#### 2. Require status checks to pass before merging
- ✅ **Require status checks to pass before merging**
  - ✅ Require branches to be up to date before merging
  
  **Required status checks (select all that apply):**
  - `test` (from test.yml workflow)
  - `lint` (from ci.yml workflow, if exists)
  - `type-check` (from ci.yml workflow, if exists)
  - `security-scan` (from ci.yml workflow, if exists)
  - `build` (from ci.yml workflow, if exists)
  - `coverage-check` (from ci.yml workflow, if exists)

#### 3. Require conversation resolution before merging
- ✅ **Require conversation resolution before merging**

#### 4. Require signed commits
- ❌ Not required (optional for future)

#### 5. Require linear history
- ❌ Not required (allow merge commits)

#### 6. Include administrators
- ✅ **Include administrators** (enforce rules for all users)

#### 7. Restrict who can push to matching branches
- ❌ Not configured (all team members can push via PR)

#### 8. Allow force pushes
- ❌ **Do not allow force pushes**

#### 9. Allow deletions
- ❌ **Do not allow deletions**

---

## Repository-Specific Configurations

### webwaka-governance

**Required Status Checks:**
- `validate-markdown` (from validate-docs.yml)
- `validate-yaml` (from validate-docs.yml)
- `check-file-structure` (from validate-docs.yml)

### webwaka-core-services

**Required Status Checks:**
- `test` (CS-1, CS-3_IAM_V2, cs2-notification-service, cs4-pricing-billing-service)
- `lint` (all implementations)
- `type-check` (all implementations)
- `security-scan` (all implementations)
- `build` (all implementations)
- `coverage-check` (all implementations)

### webwaka-platform-foundation

**Required Status Checks:**
- `test` (pf1, pf2, pf3)
- `lint` (all implementations)
- `type-check` (all implementations)
- `security-scan` (all implementations)
- `build` (all implementations)
- `coverage-check` (all implementations)

### webwaka-capabilities

**Required Status Checks:**
- `test` (CB-2, CB-3, cb1, cb4)
- `lint` (all implementations)
- `type-check` (all implementations)
- `security-scan` (all implementations)
- `build` (all implementations)
- `coverage-check` (all implementations)

### webwaka-suites

**Required Status Checks:**
- `test` (sc1, sc2, sc3)
- `lint` (all implementations)
- `type-check` (all implementations)
- `security-scan` (all implementations)
- `build` (all implementations)
- `coverage-check` (all implementations)

### webwaka-infrastructure

**Required Status Checks:**
- `test` (id1, id2, id3)
- `lint` (all implementations)
- `type-check` (all implementations)
- `security-scan` (all implementations)
- `build` (all implementations)
- `coverage-check` (all implementations)

---

## Implementation Steps

### Step 1: Enable Branch Protection (Per Repository)

1. Navigate to repository on GitHub
2. Go to **Settings** → **Branches**
3. Click **Add rule** under "Branch protection rules"
4. Enter `main` as the branch name pattern
5. Configure settings as specified above
6. Click **Create** or **Save changes**

### Step 2: Verify Workflows are Running

Before enabling required status checks, ensure workflows have run at least once:

1. Create a test PR or push to a branch
2. Verify workflows execute successfully
3. Check that all expected jobs appear in the status checks list
4. Then enable required status checks in branch protection

### Step 3: Test Branch Protection

1. Create a test PR with intentional issues (e.g., failing test)
2. Verify that PR cannot be merged
3. Fix the issues
4. Verify that PR can now be merged

---

## Quality Gate Thresholds

### Code Coverage

**Minimum Threshold:** 70% for lines, branches, functions, and statements

**Configuration (in jest.config.js or package.json):**
```json
{
  "jest": {
    "coverageThreshold": {
      "global": {
        "lines": 70,
        "branches": 70,
        "functions": 70,
        "statements": 70
      }
    }
  }
}
```

### Linting

**Standard:** ESLint with recommended rules

**Enforcement:** Zero errors (warnings allowed)

### Security

**Standard:** npm audit

**Enforcement:** No high or critical vulnerabilities

### Type Safety

**Standard:** TypeScript strict mode

**Enforcement:** Zero type errors

---

## Maintenance

### Adding New Implementations

When a new implementation is added to a repository:

1. Add the implementation name to the workflow matrix
2. Ensure the implementation has tests configured
3. Verify workflows run successfully
4. Update branch protection if new status checks are added

### Modifying Quality Gates

To modify quality gate thresholds:

1. Update the threshold in the implementation's configuration
2. Test with existing code to ensure it passes
3. Update this documentation
4. Communicate changes to the team

---

## Troubleshooting

### Status Check Not Appearing

**Issue:** Required status check doesn't appear in the list

**Solution:**
1. Ensure the workflow has run at least once
2. Check that the job name matches exactly
3. Verify the workflow is on the correct branch

### PR Cannot Be Merged

**Issue:** PR shows "Required status checks have not passed"

**Solution:**
1. Check which status check failed
2. Review the workflow logs
3. Fix the issue and push new commits
4. Wait for checks to re-run

### Workflow Failing on Dependencies

**Issue:** `npm ci` fails due to missing package-lock.json

**Solution:**
1. Ensure package-lock.json exists and is committed
2. Run `npm install` locally to generate it
3. Commit and push the package-lock.json file

---

**Configuration Status:** ✅ Implemented  
**Implementation:** Automated via GitHub API
