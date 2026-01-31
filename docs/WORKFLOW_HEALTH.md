# Workflow Health Monitoring

**Version:** 1.0  
**Date:** January 31, 2026  
**Status:** Production

---

## Overview

The health of the factory's workflows is critical to its operation. This document outlines how to monitor workflow health and troubleshoot common issues.

---

## Key Workflows

### 1. State Machine Enforcement (`state_machine.yml`)
- **Purpose:** Handles all slash commands and state transitions.
- **Trigger:** `issue_comment` (on new comments), `issues` (on labeling).
- **Criticality:** HIGH - If this fails, the factory stops.

### 2. CI/CD Pipeline (`ci.yml`)
- **Purpose:** Runs tests and quality checks on all pull requests.
- **Trigger:** `pull_request`.
- **Criticality:** HIGH - If this fails, code quality is not guaranteed.

---

## Monitoring

### 1. Automated Monitoring (`workflow_monitor.yml`)
- **What:** A dedicated GitHub Action that runs every hour.
- **Checks for:**
  - **Skipped Runs:** Indicates a workflow was triggered but didn't execute (e.g., missing state transition).
  - **Failed Runs:** Indicates a workflow ran but encountered an error.
  - **Anomalously Long Runs:** Indicates a workflow may be stuck.
- **Alerts:** Sends a notification to the Founder's Chief of Staff if any issues are found.

### 2. Manual Monitoring (Chief of Staff)
- **What:** The Chief of Staff's proactive monitoring loop.
- **Checks for:**
  - Skipped runs
  - State mismatches (agent command vs actual state)
  - Stale issues
- **Alerts:** Proactively notifies the Founder with analysis and recommendations.

### 3. Manual Monitoring (GitHub UI)
- **Where:** https://github.com/webwakaagent1/webwaka-agent-factory/actions
- **What to look for:**
  - **Red X:** Failed runs
  - **Gray Circle:** Skipped runs
  - **Yellow Circle:** In-progress runs
  - **Green Check:** Successful runs

---

## Common Issues & Troubleshooting

### Issue: Workflows are being skipped

**Symptom:** Agent uses a slash command, but the issue state doesn't change. GitHub Actions shows a gray circle (skipped).

**Root Cause:** The workflow was triggered, but the `if` condition in the job was not met. For the state machine, this usually means:
- The command is not defined in the transition matrix.
- The `from` state is incorrect.
- The user doesn't have permission.

**How to Fix:**
1. **Check the workflow file** (`state_machine.yml`) to see if the transition is defined.
2. **Add the missing transition** if needed.
3. **Test the fix** by re-running the command.

### Issue: Workflows are failing

**Symptom:** GitHub Actions shows a red X (failed).

**Root Cause:** A script or command within the workflow encountered an error.

**How to Fix:**
1. **Click on the failed run** in GitHub Actions.
2. **View the logs** for the failing step.
3. **Identify the error message**.
4. **Debug the script** or command.
5. **Push a fix** and re-run the workflow.

### Issue: Workflows are stuck

**Symptom:** GitHub Actions shows a yellow circle (in-progress) for an unusually long time.

**Root Cause:** A step in the workflow is hanging or waiting for input.

**How to Fix:**
1. **View the logs** for the in-progress run.
2. **Identify which step is hanging**.
3. **Cancel the workflow run**.
4. **Debug the hanging step**.
5. **Push a fix** and re-run.

---

## Best Practices

- **Test All Changes:** Never push changes to workflows without testing them in a separate branch first.
- **Use a Test Suite:** The state machine test suite (`test_state_machine.yml`) should be run on every change to the state machine.
- **Monitor Regularly:** The Chief of Staff should provide daily health reports.
- **Document Changes:** All changes to workflows should be documented in the commit message and PR description.

---

## Escalation Path

1. **Automated alert** is sent to Chief of Staff.
2. **Chief of Staff** investigates and reports to Founder with recommendation.
3. **Founder** approves fix.
4. **Chief of Staff** implements and verifies fix.
5. **Post-mortem** is conducted to prevent recurrence.

---

**A healthy workflow system is the backbone of the factory. Monitor it closely.**
