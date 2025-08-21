# Admin Screen Specification

## 1. Screen Name

**Admin Console**

---

## 2. Purpose

* Provide a centralized **administration dashboard** for platform maintainers.
* Enable management of **users, teams, resources (datasets, models, projects, dashboards, community posts)**, and system monitoring.
* Support tracking of **credits, contributions, logs, statistics**, and integration with Zenodo.

---

## 3. Layout

### A. Header

* **Title**: `Admin Console`
* **Breadcrumb**: `Admin`
* **Global Actions**:

  * \[Export Logs]
  * \[Generate Report]

### B. Tab Navigation

1. User Management
2. Team Management
3. Dataset Management
4. Model Management
5. Project Management
6. Dashboard Management
7. Community Management
8. Zenodo Publication Management
9. System Logs
10. Database Status
11. Resource Credits
12. System Statistics
13. Settings

---

## 4. Tab Specifications

### 1) User Management

* **Table View**: user ID, name, email, role, last login, status (active/suspended)
* Actions: \[Promote/Demote Role], \[Suspend], \[Delete]
* Filters: active, suspended, role

---

### 2) Team Management

* **Table View**: team ID, name, owner, # members, # resources
* Actions: \[Edit Info], \[Manage Members], \[Disband Team]

---

### 3) Dataset Management

* List of all datasets (id, name, owner, visibility, last updated)
* Actions: \[Delete], \[Change Visibility], \[Reassign Owner]

---

### 4) Model Management

* List of all models (id, name, type, owner, status, last updated)
* Actions: \[Delete], \[Change Visibility], \[Reassign Owner]

---

### 5) Project Management

* Table: project name, owner/team, # linked models, # linked datasets, last updated
* Actions: \[Delete], \[Change Visibility], \[Reassign Owner]

---

### 6) Dashboard Management

* Table: dashboard name, owner/team, status, last updated
* Actions: \[Delete], \[Change Visibility], \[Reassign Owner]

---

### 7) Community Management

* List of posts, discussions, comments
* Actions: \[Delete Post], \[Suspend User], \[Moderate Content]
* Filters: flagged, reported, team-only

---

### 8) Zenodo Publication Management

* **Table**: DOI, linked resource (dataset/model/project), owner, status, date published
* Actions: \[Sync Metadata], \[Revoke Link]

---

### 9) System Logs

* **Log Viewer**: chronological activity stream
* Fields: timestamp, user/system, action, resource
* Export to CSV/JSON

---

### 10) Database Status

* Metrics: # users, # datasets, # models, # projects, # dashboards, # community posts
* DB health indicators (uptime, replication status)

---

### 11) Resource Credits

* **Credits Management**:

  * Auto Credit Assignment (based on role, activity)
  * Contribution Tracking (uploads, publications)
* Table: user/team, credits available, credits used

---

### 12) System Statistics

* Charts: daily active users, dataset uploads, model runs, Zenodo exports
* KPIs: total credits issued, total publications, API request volume

---

### 13) Settings

* General system configuration
* API keys (Map provider, Zenodo integration)
* Security (password policies, OAuth providers)
* Feature toggles (enable/disable modules)

---

## 5. States

* **Empty State**: “No records available.”
* **Loading State**: spinner + “Loading admin data…”
* **Error State**: “Failed to fetch records.”

---

## 6. Permissions

* **Viewer** – no access
* **Contributor** – no access
* **Owner** – no access
* **Admin** – required; sub-admin roles may be scoped (e.g., Dataset Admin, Community Moderator)

---

## 7. API Integration

* **Local DB**:

  * `users`, `teams`, `datasets`, `models`, `projects`, `dashboards`, `community_posts`, `logs`, `credits`
* **External**:

  * Zenodo API (publication sync)
  * Map provider API keys

---

## 8. Example Wireframe (Text)

```
-------------------------------------------------
[ Admin Console ]

Tabs: [Users] [Teams] [Datasets] [Models] [Projects] 
      [Dashboards] [Community] [Zenodo] [Logs] [DB] 
      [Credits] [Statistics] [Settings]

-------------------------------------------------
[User Management]

User ID   Name     Email             Role     Status     Last Login
-------------------------------------------------------------------
u-102     J. Yoon  jyoon@mail.com    Admin    Active     Aug 20,25
u-214     K. Park  kpark@mail.com    Viewer   Suspended  Aug 10,25
-------------------------------------------------------------------

Actions: [Promote] [Suspend] [Delete]
-------------------------------------------------
```

