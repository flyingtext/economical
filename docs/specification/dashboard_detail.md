# Dashboard Detail Screen Specification

## 1. Screen Name

**Dashboard Detail**

---

## 2. Purpose

* Display a single dashboard with its full layout and widgets.
* Support interactive exploration of bound models/datasets.
* Allow sharing and permission management.

---

## 3. Layout

### A. Header

* **Title**: Dashboard name
* **Breadcrumb**: `Dashboards > Dashboard Detail`
* **Global Actions**:

  * \[Edit Dashboard] → opens `dashboard_builder`
  * \[Save Draft]
  * \[Publish]
  * \[Share / Manage Permissions]

### B. Tab Navigation

1. Overview
2. Layout View
3. Widgets in Action
4. Team & Sharing Permissions
5. Activity Logs

---

## 4. Tab Specifications

### 1) Overview

* Description, owner/team, tags
* Linked models/datasets
* Status (Draft/Published)
* Metadata: created by, last updated

---

### 2) Layout View

* Visual representation of dashboard layout (grid with widgets)
* Preview of widget arrangement
* Read-only in detail view

---

### 3) Widgets in Action

* Interactive widgets (charts, tables, maps, KPIs)
* Bound to live model outputs or datasets
* User interactions: filter, sort, drill-down

---

### 4) Team & Sharing Permissions

* Access list (Viewer, Contributor, Owner, Admin)
* Sharing link (if public)
* Actions: \[Add Member], \[Change Role], \[Remove]

---

### 5) Activity Logs

* Timeline of edits and updates
* Columns: Date, User, Action
* Exportable log

---

## 5. States

* Draft (private/internal)
* Published (visible to team or public)

---

## 6. Permissions

* **Viewer** – read-only widgets
* **Contributor** – edit layout and add/remove widgets for dashboards they contribute to
* **Owner** – full control, including sharing and publication settings
* **Admin** – manage all dashboards

---

## 7. API Integration

* **Local DB**:

  * `dashboards` (id, name, description, layout JSON, status)
  * `dashboard_widgets` (dashboard\_id, widget\_id, type, data\_binding JSON)
  * `dashboard_permissions` (dashboard\_id, user\_id, role)

---

## 8. Example Wireframe (Text)

```
-------------------------------------------------
Dashboard: Macro Overview

Tabs: [Overview] [Layout] [Widgets] [Permissions] [Activity]

-------------------------------------------------
[Layout View]

| GDP Trend (Line Chart) | Inflation Rate (Bar Chart) |
|------------------------|----------------------------|
| Trade Balance (Table)  | World Map (Geo Heatmap)    |

-------------------------------------------------
```

