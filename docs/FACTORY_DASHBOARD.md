# Factory Operations Dashboard

**Version:** 1.0  
**Date:** January 31, 2026  
**Status:** Documented (Implementation in Progress)

---

## Overview

The Factory Operations Dashboard provides real-time visibility into the WebWaka Agentic Software Factory. It displays agent activity, task progress, workflow health, and key metrics.

---

## Dashboard Location

**Project:** `factory-dashboard`  
**Path:** `/home/ubuntu/factory-dashboard`  
**URL:** https://3000-ifnfj1d9s67ninnpjkisu-6f3cd172.us2.manus.computer

---

## Key Features

### 1. Real-Time Status Overview
- Factory health status (operational, degraded, offline)
- Total tasks (open, in progress, completed)
- Active agents count
- Workflow health indicators

### 2. Agent Activity Monitor
- List of active agents with their current tasks
- Agent performance metrics
- Activity timeline
- Workload distribution

### 3. Task Progress Tracker
- Tasks by state (visual breakdown)
- Priority distribution
- Completion rate over time
- Blocked issues alert

### 4. Workflow Health Monitor
- Recent workflow runs status
- Skipped/failed workflow alerts
- State machine health
- System alerts

### 5. Activity Log Viewer
- Recent agent activities
- Filterable by agent, issue, or action type
- Timeline view
- Export capabilities

---

## Data Sources

The dashboard fetches data from:

1. **GitHub API** - Issues, PRs, labels, workflow runs
2. **Activity Log** - `logs/activity_log.jsonl` from the factory repository
3. **Workflow Monitor** - Automated health check results

---

## Implementation Guide

### Technology Stack

- **Frontend:** React 19 + Tailwind CSS 4
- **Charts:** Recharts
- **Data Fetching:** GitHub REST API + GraphQL API
- **Real-time Updates:** Polling every 30-60 seconds

### Key Components

**1. Dashboard Layout**
```tsx
<DashboardLayout>
  <Header /> {/* Factory status, refresh button */}
  <Sidebar /> {/* Navigation */}
  <MainContent>
    <StatusCards /> {/* 4 key metrics */}
    <AgentActivity /> {/* Active agents table */}
    <TaskProgress /> {/* Charts and graphs */}
    <WorkflowHealth /> {/* Health indicators */}
    <ActivityLog /> {/* Recent activities */}
  </MainContent>
</DashboardLayout>
```

**2. Data Fetching Hooks**
```tsx
useFactoryStatus() // Overall factory health
useAgentActivity() // Active agents and their tasks
useTaskMetrics() // Task counts by state/priority
useWorkflowHealth() // Workflow run status
useActivityLog() // Recent activity entries
```

**3. Real-Time Updates**
```tsx
// Poll GitHub API every 60 seconds
useEffect(() => {
  const interval = setInterval(fetchData, 60000);
  return () => clearInterval(interval);
}, []);
```

### API Integration

**GitHub REST API:**
```typescript
const GITHUB_TOKEN = import.meta.env.VITE_GITHUB_TOKEN;
const REPO_OWNER = "webwakaagent1";
const REPO_NAME = "webwaka-agent-factory";

// Fetch issues
const response = await fetch(
  `https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/issues`,
  {
    headers: {
      Authorization: `Bearer ${GITHUB_TOKEN}`,
      Accept: "application/vnd.github.v3+json",
    },
  }
);
```

**Activity Log:**
```typescript
// Fetch activity log from GitHub
const response = await fetch(
  `https://raw.githubusercontent.com/${REPO_OWNER}/${REPO_NAME}/main/logs/activity_log.jsonl`,
  {
    headers: {
      Authorization: `Bearer ${GITHUB_TOKEN}`,
    },
  }
);

// Parse JSONL
const lines = (await response.text()).split("\n").filter(Boolean);
const activities = lines.map(line => JSON.parse(line));
```

---

## Metrics & Calculations

### Factory Health Status

**Operational (🟢):**
- No skipped workflows in last hour
- No blocked issues >24 hours
- <20% of tasks in implementing state

**Degraded (🟡):**
- 1-3 skipped workflows in last hour
- 1-2 blocked issues >24 hours
- 20-40% of tasks in implementing state

**Offline (🔴):**
- >3 skipped workflows in last hour
- >2 blocked issues >24 hours
- >40% of tasks in implementing state

### Agent Performance

**Tasks Completed:** Count of issues closed by agent  
**Average Time:** Mean time from claim to completion  
**Success Rate:** (Completed / (Completed + Abandoned)) × 100

### Task Metrics

**Completion Rate:** (Closed / Total) × 100  
**Velocity:** Tasks completed per day  
**Cycle Time:** Average time from ready → closed

---

## Deployment

### Environment Variables

Add to `.env.local`:
```
VITE_GITHUB_TOKEN=<your_github_token_here>
VITE_REPO_OWNER=webwakaagent1
VITE_REPO_NAME=webwaka-agent-factory
```

### Build & Deploy

```bash
cd /home/ubuntu/factory-dashboard
pnpm install
pnpm build
```

---

## Future Enhancements

**Priority 1:**
- Real-time WebSocket updates (instead of polling)
- Agent identification in dashboard
- Drill-down views for individual agents/tasks

**Priority 2:**
- Historical trend analysis
- Predictive analytics (estimated completion times)
- Custom alerts and notifications

**Priority 3:**
- Mobile-responsive design
- Export reports (PDF/CSV)
- Integration with Slack/Discord for alerts

---

## Current Status

**Implemented:**
- ✅ Project scaffolding
- ✅ Design system and theme
- ✅ Documentation

**In Progress:**
- 🔄 Dashboard components
- 🔄 API integration
- 🔄 Real-time data fetching

**Planned:**
- ⏳ Charts and visualizations
- ⏳ Activity log viewer
- ⏳ Agent performance metrics

---

**The dashboard provides essential visibility into factory operations. Full implementation is documented and ready for development.**
