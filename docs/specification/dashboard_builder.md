# Dashboard Builder Screen Specification

## 1. Screen Name

**Dashboard Builder (Create / Edit)**

---

## 2. Purpose

* Provide an interactive **UI editor** for creating and editing dashboards.
* Allow users to drag & drop **widgets** (charts, tables, maps, KPIs) onto a grid layout.
* Bind widgets to **datasets and model outputs**.
* Configure sharing, permissions, and publication.

---

## 3. Layout

### A. Header

* **Title**: `Dashboard Builder`
* **Breadcrumb**: `Dashboards > Dashboard Builder`
* **Global Actions**:

  * \[Save Draft]
  * \[Publish]
  * \[Cancel]

### B. Main Editor

* **Canvas/Grid Editor**

  * Drag-and-drop interface
  * Snap-to-grid for widgets
  * Resize/move widgets interactively
* **Widget Palette (Sidebar Left)**

  * Chart types: Line, Bar, Pie, Scatter, Area
  * Table (sortable, filterable)
  * Map (Geo heatmap, markers)
  * KPI (single value cards)
  * Text/Markdown block
* **Inspector Panel (Sidebar Right)**

  * Widget properties (title, size, style)
  * Data binding settings
  * Visualization options (axes, colors, legends)

### C. Tab Navigation

1. Basic Info
2. Layout Editor
3. Widgets & Data Binding
4. Sharing & Permissions
5. Publish

---

## 4. Tab Specifications

### 1) Basic Info

* Fields:

  * Dashboard name
  * Description (markdown editor)
  * Tags (multi-select)
  * Visibility (Private / Team / Public)

---

### 2) Layout Editor

* Interactive drag-and-drop grid editor
* Add/remove/move/resize widgets
* Snap alignment guides
* Undo/redo actions

---

### 3) Widgets & Data Binding

* Select a widget → open Inspector panel
* Bind data to widget:

  * Source = dataset or model output
  * Field selection = columns for x/y axes, metrics, categories
* Example:

  * Line Chart bound to GDP (x=Year, y=Value)
  * KPI bound to Inflation Rate (%)

---

### 4) Sharing & Permissions

* Member list with roles (Owner, Editor, Viewer)
* Actions: \[Add Member], \[Change Role], \[Remove]
* Public link toggle (if visibility = Public)

---

### 5) Publish

* Summary of dashboard: layout preview + widgets list
* Options:

  * Save Draft (internal only)
  * Publish to Platform (internal visibility)
  * Export layout JSON (for backup or reuse)

---

## 5. States

* **Draft**: unsaved or stored internally
* **Published**: visible based on permissions (Private / Team / Public)

---

## 6. Permissions

* Viewer: view published dashboards only
* Editor: edit layout, widgets, bindings
* Owner: full control + sharing/publish rights
* Admin: override permissions

---

## 7. API Integration

* **Local DB**

  * `dashboards` (id, name, description, layout JSON, status)
  * `dashboard_widgets` (dashboard\_id, widget\_id, type, config JSON)
  * `dashboard_permissions` (dashboard\_id, user\_id, role)
* **External**

  * Data retrieval API for datasets/models

---

## 8. Example Wireframe (Text)

```
-------------------------------------------------
[ Dashboard Builder ]

Tabs: [Info] [Layout] [Widgets] [Permissions] [Publish]

-------------------------------------------------
[Layout Editor]

+------------------------------------------------+
| [Line Chart: GDP Growth]   [KPI: Inflation %] |
|                                                |
| [Table: Trade Balance]     [Map: Exports]      |
+------------------------------------------------+

Left Sidebar: Widget Palette (Chart, Table, Map, KPI, Text)
Right Sidebar: Inspector (Widget properties + Data binding)
-------------------------------------------------
```
