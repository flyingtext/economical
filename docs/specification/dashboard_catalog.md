# Dashboard Catalog Screen Specification

## 1. Screen Name

**Dashboard Catalog**

---

## 2. Purpose

* Provide a centralized catalog of dashboards.
* Organize dashboards by **My Dashboards**, **Team Dashboards**, and **Public Dashboards**.
* Support creation, browsing, and quick access to dashboard details.

---

## 3. Layout

### A. Header

* **Title**: `Dashboard Catalog`
* **Breadcrumb**: `Dashboards > Catalog`
* **Global Actions**:

  * \[Create Dashboard] → opens `dashboard_builder`

### B. Tabs

* **My Dashboards**: dashboards owned by the user
* **Team Dashboards**: dashboards shared with or created by the team
* **Public Dashboards**: dashboards published by any user/team for public access

---

## 4. Dashboard List View

### List/Table Columns

| Column           | Description                      |
| ---------------- | -------------------------------- |
| Name             | Dashboard name (clickable)       |
| Owner / Team     | Owner or team name               |
| Linked Resources | Models/Datasets bound to widgets |
| Layout Preview   | Thumbnail of dashboard layout    |
| Last Updated     | Date/time of last modification   |
| Status           | Draft / Published                |

### Card View (optional)

* Name + description
* Owner/team info
* Status badge
* Thumbnail preview

---

## 5. Filters & Search

* Search by name, owner, or resource
* Filter by status (Draft, Published)
* Filter by team

---

## 6. States

* **Empty State**: “No dashboards found.” with \[Create Dashboard] button
* **Loading State**: spinner with “Loading dashboards…”
* **Error State**: “Failed to load dashboards. Retry later.”

---

## 7. Permissions

* **Viewer** – access public dashboards only
* **Contributor** – access own and team dashboards
* **Owner** – edit and manage visibility for own dashboards
* **Admin** – manage all dashboards

---

## 8. API Integration

* **Local DB**:

  * `dashboards` (id, name, description, owner\_id, team\_id, status, created\_at, updated\_at, layout JSON)
* **External**: none (internal resource binding only)

---

## 9. Example Wireframe (Text)

```
-------------------------------------------------
[ Dashboard Catalog ]

Tabs: [My Dashboards] [Team Dashboards] [Public Dashboards]

-------------------------------------------------
[My Dashboards]

Name             Owner      Resources   Updated     Status
----------------------------------------------------------------
Macro Overview   J. Yoon    2 models    Aug 20,25   Published
Energy KPIs      Team A     3 datasets  Aug 15,25   Draft
----------------------------------------------------------------

[Create Dashboard]
-------------------------------------------------
```
