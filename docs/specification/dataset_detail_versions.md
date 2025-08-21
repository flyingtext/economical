# Dataset Detail — Versions & Update Logs (Screen Definition)

## 1. Screen Purpose
The **Versions & Update Logs tab** provides a chronological view of dataset changes.  
It ensures reproducibility by allowing users to track, compare, and reference past versions.

---

## 2. Layout Components

### (A) Header
- Dataset Title (link back to Overview)
- Current Tab: **Versions & Update Logs**
- Action Buttons:
  - [Export Version History] → modal to export metadata (CSV/JSON)
  - [Compare Versions] → modal to select two versions and view diff

---

### (B) Versions List
| Version ID | Date       | Released By | Notes / Changes              | Actions         |
|------------|-----------|-------------|------------------------------|-----------------|
| v1.0       | 2024-12-01| user_123    | Initial release              | [View] [Export] |
| v1.1       | 2025-02-15| user_456    | Added CPI column             | [View] [Export] |
| v1.2       | 2025-05-10| team_admin  | Updated GDP values 2020–2024 | [View] [Export] |

- **Features**:
  - Sortable by date or version ID
  - Filter by contributor

---

### (C) Update Logs Timeline
- **Visual timeline (chronological)**  
  - 2025-05-10: GDP values updated (user: team_admin)  
  - 2025-02-15: CPI column added (user: user_456)  
  - 2024-12-01: Dataset created (user: user_123)  

---

### (D) Version Diff Modal
- **Title**: “Compare Versions”  
- Fields:
  - Select Version A  
  - Select Version B  
- Output:
  - Schema changes (added/removed columns)  
  - Record count changes  
  - Value differences (summary statistics)  
- Actions:
  - [Export Diff Report] (CSV/JSON/HTML)
  - [Close]

---

### (E) Export Version History Modal
- **Title**: “Export Version History”  
- Fields:
  - Format: CSV / JSON  
  - Delivery: Download immediately OR Send to email (logged)  
- Actions:
  - [Confirm Export]  
  - [Cancel]  

---

## 3. Logging Rules
- **If Send to Email**: export job logged in My Account or Team Settings depending on ownership  
- **If Download Immediately**: only download count tracked in Usage & Statistics  

---

## 4. Key Features
1. **Version Tracking**: complete list of dataset versions.  
2. **Transparency**: update logs with who/when/what changed.  
3. **Diff Support**: compare versions to identify schema/data changes.  
4. **Export Options**: download version history or diff reports.  
5. **Integration**: export actions logged for reproducibility.  

---

## 5. Navigation Flow
- Dataset Detail → [Versions & Update Logs tab]  
- User can:
  - View all dataset versions  
  - Inspect update logs (list or timeline)  
  - Compare two versions via modal  
  - Export version history or diff reports  
