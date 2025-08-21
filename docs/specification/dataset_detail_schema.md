# Dataset Detail — Schema (Screen Definition)

## 1. Screen Purpose
The **Schema tab** provides a structured view of the dataset’s columns.  
It allows users to understand the variables, their types, units, and descriptions, and export schema metadata if needed.

---

## 2. Layout Components

### (A) Header
- Dataset Title (with link back to Overview)
- Current Tab: **Schema**
- Action Buttons:
  - [Export Schema] → modal to export schema as JSON/CSV
  - [Use in Model] → shortcut to link schema to a model (optional)

---

### (B) Schema Table
| Column Name | Data Type | Unit | Description | Example Value |
|-------------|-----------|------|-------------|---------------|
| GDP         | Number    | USD  | Gross Domestic Product | 21,000,000 |
| CPI         | Number    | Index| Consumer Price Index   | 112.5      |
| Country     | String    | -    | ISO country code       | USA        |
| Year        | Integer   | Year | Time reference         | 2024       |

- **Features**:
  - Sortable by column name / data type
  - Filterable (search column names or types)
  - Pagination if many columns

---

### (C) Column Detail Panel (Optional, on click)
- When clicking a column:
  - Column Name
  - Data Type
  - Unit
  - Description (longer text)
  - Example Values (sample rows)
- [Copy Column Info] button

---

### (D) Export Schema Modal
- **Title**: “Export Schema”
- Fields:
  - Format: JSON / CSV / YAML
  - Delivery:  
    - Download immediately  
    - Send to registered email (logs entry to Exports & Backups)
- Actions:
  - [Confirm Export]
  - [Cancel]

---

## 3. Logging Rules
- If user selects **Send to Email**:
  - Export log recorded in My Account (personal) or Team Settings (team), same as dataset export rules
  - Fields logged: Export ID, resource_id, format, requested_by, ownership_type, timestamp, status
- If user selects **Download Immediately**:
  - No email delivery
  - Lightweight log (download count) stored in Usage & Statistics

---

## 4. Key Features
1. **Structured Schema View**: table of columns, types, units, descriptions.
2. **Interactive Exploration**: sort, filter, preview sample values.
3. **Column Detail Drilldown**: extended metadata per column.
4. **Export Options**: export schema metadata in multiple formats.
5. **Logging Integration**: schema export jobs tracked (if delivered by email).

---

## 5. Navigation Flow
- Dataset Detail → [Schema tab]
- User views schema table
- Option 1: Click column → view details in side panel
- Option 2: [Export Schema] → export modal → confirm → export delivered/logged
