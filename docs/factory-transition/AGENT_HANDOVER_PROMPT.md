# Agent Handover Prompt: Agentic Software Factory Finalization

**Date:** January 31, 2026  
**Handover From:** Manus AI (Agentic Software Factory Transition Architect)  
**Handover To:** Next Manus Agent  
**Priority:** HIGH  
**Estimated Duration:** 2-3 hours

---

## Context

You are taking over the finalization of the **WebWaka Agentic Software Factory**, a GitHub-native task coordination system for the WebWaka platform. The previous agent (Transition Architect) has completed Phases A, B, and C of the transition:

- **Phase A:** Exhaustive current-state audit
- **Phase B:** Independent factory verification (simulated)
- **Phase C:** Full task migration (17 issues created)

The factory is **largely complete** but has **two critical outstanding issues** that must be resolved before the system can be ratified by the Founder.

---

## Your Mission

Complete the following tasks to finalize the Agentic Software Factory and prepare it for Founder ratification:

1. **Fix the Kanban Board (Critical)**
2. **Verify the State Machine (High Priority)**
3. **Create Final Ratification Package**
4. **Update Master Control Board**

---

## Task 1: Fix the Kanban Board (Critical)

### Problem

The project board URL (`https://github.com/users/webwakaagent1/projects/1`) returns a 404 error. This prevents the Founder from having real-time visibility into factory operations.

### Root Cause

The project board was created via the GitHub API during the initial implementation, but it is either:
- Not publicly accessible (visibility issue)
- Not properly configured
- Does not exist

### Your Actions

1. **Verify the project exists:**
   - Use the GitHub API to check if a project with ID from `/home/ubuntu/webwaka-agent-factory/project_id.txt` exists
   - If it exists, proceed to step 2
   - If it does not exist, proceed to step 3

2. **If the project exists, fix visibility and configuration:**
   - Set the project to **Public** visibility
   - Ensure it is linked to the `webwaka-agent-factory` repository
   - Configure columns for each state:
     - Discovery
     - Ready
     - Claimed
     - In Progress
     - Review
     - Approved
     - Implementing
     - Complete
   - Set up automation rules to move issues between columns based on their state labels
   - Test that issues appear in the correct columns

3. **If the project does not exist, create it manually:**
   - Navigate to https://github.com/webwakaagent1
   - Create a new Project (Board style)
   - Name it "Agent Factory Kanban"
   - Set visibility to Public
   - Link it to the `webwaka-agent-factory` repository
   - Configure columns as described in step 2
   - Set up automation rules
   - Update the README.md in `webwaka-agent-factory` with the correct project URL

### Success Criteria

- The project board URL is accessible without authentication
- All 17 issues appear on the board
- Issues are organized by their state labels
- Automation rules move issues between columns when labels change

---

## Task 2: Verify the State Machine (High Priority)

### Problem

The core state machine logic (slash commands like `/claim`, `/start`, `/submit`) has not been tested. The workflows exist in `.github/workflows/state_machine.yml`, but their functionality is unverified.

### Your Actions

1. **Create a test issue:**
   - Navigate to https://github.com/webwakaagent1/webwaka-agent-factory/issues
   - Create a new issue titled "[TEST] State Machine Verification"
   - Add labels: `state: discovery`, `priority: low`, `domain: infrastructure`, `type: chore`

2. **Test the full lifecycle:**
   - Comment `/claim` on the issue
     - **Expected:** Issue is assigned to you, label changes to `state: claimed`
   - Comment `/start` on the issue
     - **Expected:** Label changes to `state: in-progress`
   - Comment `/submit` on the issue
     - **Expected:** Label changes to `state: review`
   - Manually add the `approved` label
     - **Expected:** Label changes to `state: approved`
   - Comment `/implement` on the issue
     - **Expected:** Label changes to `state: implementing`
   - Create a dummy PR, link it to the issue, and merge it
     - **Expected:** Label changes to `state: complete`, issue is closed

3. **Document any failures:**
   - If any step fails, document the failure in a file called `STATE_MACHINE_TEST_RESULTS.md`
   - Include the expected behavior, actual behavior, and any error messages
   - Attempt to fix the workflow if possible

4. **Close the test issue:**
   - Once testing is complete, close the test issue (if not already closed)

### Success Criteria

- All slash commands trigger the correct state transitions
- Labels change automatically as expected
- The test issue completes the full lifecycle without errors

---

## Task 3: Create Final Ratification Package

### Problem

The Founder needs a clear, concise package to review before ratifying the factory.

### Your Actions

1. **Create a file called `RATIFICATION_PACKAGE.md` in the `webwaka-governance` repository:**
   - Location: `docs/factory-transition/RATIFICATION_PACKAGE.md`

2. **Include the following sections:**
   - **Executive Summary:** Brief overview of what has been accomplished
   - **System Status:** Current state of the factory (operational, issues resolved, etc.)
   - **Outstanding Risks:** Any remaining risks or limitations
   - **Verification Results:** Summary of Kanban board fix and state machine testing
   - **Recommendation:** Clear recommendation to ratify or delay
   - **Next Steps:** What happens after ratification (agents can begin work)

3. **Commit and push the ratification package to GitHub**

### Success Criteria

- The ratification package is clear, concise, and decision-ready
- All verification results are documented
- The recommendation is explicit

---

## Task 4: Update Master Control Board

### Problem

The Master Control Board needs to reflect the completion of the Agentic Software Factory transition.

### Your Actions

1. **Open the Master Control Board:**
   - File: `/home/ubuntu/phase-a-audit/webwaka-governance/docs/governance/WEBWAKA_MASTER_CONTROL_BOARD.md`

2. **Add a new section at the top (after the status legend):**
   - Title: "Agentic Software Factory Transition"
   - Status: 🟢 **Complete** (January 31, 2026)
   - Summary: Brief description of the transition and its outcomes
   - Link to the ratification package

3. **Update the remediation wave status:**
   - Note that Waves R2-R6 are now tracked as GitHub Issues in the `webwaka-agent-factory` repository
   - Provide a link to the repository

4. **Commit and push the updated Master Control Board**

### Success Criteria

- The Master Control Board reflects the completion of the factory transition
- Links to the factory repository and ratification package are included

---

## Important Context & Files

### Key Repositories

1. **webwaka-agent-factory** (https://github.com/webwakaagent1/webwaka-agent-factory)
   - The operational brain of the factory
   - Contains all 17 issues for current and future work
   - Contains all workflows, templates, and documentation

2. **webwaka-governance** (https://github.com/webwakaagent1/webwaka-governance)
   - Supreme source of truth for governance
   - Contains the Master Control Board
   - Contains all transition reports

### Key Documents

1. **Pre-Migration Task Inventory & Risk Report**
   - Location: `webwaka-governance/docs/factory-transition/Pre_Migration_Task_Inventory_and_Risk_Report.md`
   - Contains the Phase A audit findings

2. **Factory Verification Report**
   - Location: `webwaka-governance/docs/factory-transition/Factory_Verification_Report.md`
   - Contains the Phase B verification findings (including the two outstanding issues)

3. **Factory Task Migration Completion Report**
   - Location: `webwaka-governance/docs/factory-transition/Factory_Task_Migration_Completion_Report.md`
   - Contains the Phase C migration results

4. **Agent Onboarding Guide**
   - Location: `webwaka-agent-factory/docs/onboarding/AGENT_ONBOARDING.md`
   - Complete guide for new agents

5. **Founder Control Guide**
   - Location: `webwaka-agent-factory/docs/onboarding/FOUNDER_GUIDE.md`
   - Complete guide for Founder governance

### GitHub Authentication

- **Username:** `webwakaagent1`
- **Token:** Available via Founder or environment variables

The GitHub Personal Access Token should be provided by the Founder at the start of your session. Use these credentials for all GitHub API calls and git operations.

---

## Constraints & Rules

1. **No Shortcuts:** Do not skip any verification steps. The Founder needs confidence that the system works.
2. **Document Everything:** All actions, results, and decisions must be documented and committed to GitHub.
3. **Stop and Report:** If you encounter any blocking issues, stop and report them to the Founder immediately.
4. **No Assumptions:** If something is unclear, ask the Founder for clarification before proceeding.

---

## Expected Outcome

Upon completion of your tasks, the Agentic Software Factory will be:
- Fully operational with a working Kanban board
- Verified with a tested state machine
- Ready for Founder ratification
- Documented in the Master Control Board

You will deliver a **Ratification Package** to the Founder, who will then decide whether to ratify the system and allow agents to begin work.

---

## How to Begin

1. **Clone the repositories:**
   ```bash
   cd /home/ubuntu
   git clone https://github.com/webwakaagent1/webwaka-agent-factory.git
   git clone https://github.com/webwakaagent1/webwaka-governance.git
   ```

2. **Read the three transition reports** (listed above in Key Documents)

3. **Start with Task 1** (Fix the Kanban Board)

4. **Proceed sequentially** through Tasks 2, 3, and 4

5. **Deliver the Ratification Package** to the Founder

---

**Good luck! The platform is counting on you to complete this critical transition.**

---

**End of Handover Prompt**
