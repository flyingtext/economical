# Project Catalog Specification

## 1. Screen Name

**Project Catalog**

---

## 2. Purpose

* Provide a centralized catalog of all projects accessible to the user.
* Support browsing of **My Projects**, **Team Projects**, and **Public Projects**.
* Enable quick navigation to project details and project builder (create/edit).

---

## 3. Layout

### A. Header

* **Title**: `Project Catalog`
* **Breadcrumb**: `Projects > Catalog`
* **Global Actions**:

  * \[Create Project] → opens `project_builder`

### B. Tabs

* **My Projects**: projects owned by the user
* **Team Projects**: projects owned by or shared within the user’s team(s)
* **Public Projects**: projects published publicly by any user/team

---

## 4. Project List View

### List/Table Columns

| Column          | Description                                           |
| --------------- | ----------------------------------------------------- |
| Name            | Project name (clickable link to detail page)          |
| Owner / Team    | Project owner or team name                            |
| Linked Models   | Number of linked models (tooltip with preview list)   |
| Linked Datasets | Number of linked datasets (tooltip with preview list) |
| Members         | Count of team members (avatars shown if team project) |
| Last Updated    | Date of last modification                             |
| Status          | Draft / Published (Internal) / Exported to Zenodo     |

### Card View (optional toggle)

* Project name + description
* Badges: Draft/Published/Zenodo
* Linked models & datasets preview
* Owner/team info

---

## 5. Filters & Search

* **Search bar**: keyword (project name, owner, dataset/model names)
* **Filters**:

  * Status (Draft, Published, Zenodo-exported)
  * Owner/Team
  * Last updated (date range)

---

## 6. States

* **Empty State**:

  * “No projects found.”
  * Show \[Create Project] button prominently
* **Loading State**: spinner with message “Loading projects…”
* **Error State**:

  * “Failed to fetch projects. Please retry.”

---

## 7. Permissions

* **Viewer** – can only see **Public Projects**
* **Contributor** – can see and edit **My Projects** and **Team Projects**
* **Owner** – can manage visibility, roles, and publication for owned projects
* **Admin** – full visibility and management

---

## 8. API Integration

* **Local DB**:

  * `projects` (id, name, description, owner\_id, team\_id, status, created\_at, updated\_at)
  * `project_models` (project\_id, model\_id)
  * `project_datasets` (project\_id, dataset\_id)
  * `project_members` (project\_id, user\_id, role)
* **External**:

  * Zenodo API (optional: for export status)

---

## 9. Example Wireframe (Text)

```
-------------------------------------------------
[ Project Catalog ]

Tabs: [My Projects] [Team Projects] [Public Projects]

-------------------------------------------------
[My Projects]

Name              Owner      Models  Datasets  Members  Updated     Status
-------------------------------------------------------------------------------
Macro Forecast    J. Yoon    3       2         1        Aug 21, 25  Published
Energy Simulation Team A     5       4         4        Aug 15, 25  Draft
-------------------------------------------------------------------------------

[Create Project]
-------------------------------------------------
```
