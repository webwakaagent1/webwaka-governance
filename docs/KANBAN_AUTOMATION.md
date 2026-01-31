# Kanban Board Automation

**Version:** 1.0  
**Date:** January 31, 2026  
**Status:** Configured

---

## Overview

The WebWaka Agentic Software Factory uses a GitHub Project board with 16 state-based columns. This document explains how the board is organized and how automation works.

---

## Board Structure

The Kanban board has 16 columns that correspond to the 16 states in the state machine:

| Column | State Label | Description |
|--------|-------------|-------------|
| Discovered | `state: discovered` | New issues awaiting triage |
| Triaged | `state: triaged` | Issues that have been reviewed |
| Needs Brainstorming | `state: needs-brainstorming` | Complex issues requiring design |
| Brainstorming | `state: brainstorming` | Solution design in progress |
| Needs Clarification | `state: needs-founder-clarification` | Awaiting Founder input |
| Awaiting Decision | `state: awaiting-founder-decision` | Ready for Founder approval |
| Ready for Implementation | `state: ready-for-implementation` | Approved and ready to claim |
| Implementing | `state: implementing` | Agent actively working |
| Blocked | `state: blocked` | Agent is blocked |
| Stopped Working | `state: stopped-working` | Agent abandoned task |
| Testing | `state: testing` | PR created, awaiting review |
| Verification | `state: verification` | Final QA/verification |
| Needs Rework | `state: needs-rework` | Verification failed |
| Failed Testing | `state: failed-testing` | Tests failed |
| Closed | `state: closed` | Complete and verified |
| Duplicate | `state: duplicate` | Duplicate issue |

---

## Automation Rules

### Automatic Column Movement

The board is configured to automatically move issues to the correct column when their state label changes:

**Rule 1: Label-Based Movement**
- When an issue is labeled with `state: *`, it automatically moves to the corresponding column
- Example: Adding `state: implementing` moves the issue to the "Implementing" column

**Rule 2: Closure Movement**
- When an issue is closed, it automatically moves to the "Closed" or "Duplicate" column based on labels

**Rule 3: PR-Linked Movement**
- When a PR is merged, linked issues automatically move to "Closed"

### Manual Configuration

GitHub Projects V2 automation rules must be configured manually in the UI. To configure:

1. Go to: https://github.com/users/webwakaagent1/projects/1/settings/workflows
2. Click "Add workflow"
3. Configure the following workflows:

**Workflow 1: Move to column based on label**
- **Trigger:** Item labeled
- **Condition:** Label starts with "state:"
- **Action:** Set Status to [corresponding column]

**Workflow 2: Move closed issues to Done**
- **Trigger:** Item closed
- **Action:** Set Status to "Closed"

**Workflow 3: Move merged PR issues to Done**
- **Trigger:** Pull request merged
- **Action:** Set Status to "Closed" for linked issues

---

## Benefits

**For Agents:**
- Visual representation of work in progress
- Easy to see what's available to claim
- Clear view of blocked issues

**For Founder:**
- Real-time overview of factory status
- Easy to identify bottlenecks
- Visual progress tracking

**For Everyone:**
- Single source of truth for task status
- Automatic updates reduce manual work
- Clear workflow visualization

---

## Best Practices

**Do:**
- Let the automation handle column movement
- Use state labels to trigger automation
- Check the board for visual overview

**Don't:**
- Manually move issues between columns (use labels instead)
- Create custom columns outside the 16-column structure
- Bypass the state machine

---

## Troubleshooting

**Issue: Card not moving to correct column**
- Check that the correct state label is applied
- Verify automation rules are configured in Project settings
- Manually move the card if automation fails

**Issue: Duplicate cards**
- Remove duplicate cards manually
- Ensure issues are only added to the project once

---

**The Kanban board provides a visual layer on top of the state machine. Use it for overview, rely on labels for truth.**
