# Dataset Detail — Usage & Statistics (Screen Definition)

## 1. Screen Purpose
The **Usage & Statistics tab** provides visibility into how the dataset is being used across the platform.  
It shows adoption by models, API request volume, and download/view metrics to help users evaluate dataset popularity and reliability.

---

## 2. Layout Components

### (A) Header
- Dataset Title (link back to Overview)
- Current Tab: **Usage & Statistics**
- Action Buttons:
  - [Export Usage Report] → modal to export statistics as CSV/JSON

---

### (B) Linked Models
- **Table / List** of models currently using this dataset:
  | Model Name      | Owner / Team | Linked Since | Last Run | Status |
  |-----------------|--------------|--------------|----------|--------|
  | Forecast-GDP    | user_123     | 2025-01-12   | 2025-08-20 | Active |
  | Inflation-Predict| team_econ   | 2025-03-03   | 2025-08-19 | Active |

- Action: [View Model] → navigates to Model Detail

---

### (C) API Requests
- **Chart**: monthly API calls trend (last 12 months)
- **Stats**:
  - Total requests (lifetime)
  - Average requests per month
  - Peak month usage
- Filter: by time range (30d / 90d / 1y / All)

---

### (D) Downloads & Views
- **Chart**: downloads vs. views (time-series)
- **Stats**:
  - Total views
  - Total downloads
  - Conversion rate (downloads/views)

---

### (E) Export Usage Report Modal
- **Title**: “Export Usage Report”
- Fields:
  - Format: CSV / JSON
  - Range: 30d / 90d / 1y / All
  - Delivery:
    - Download immediately
    - Send to registered email (logs entry)
- Actions:
  - [Confirm Export]
  - [Cancel]

---

## 3. Logging Rules
- **If Send to Email**:  
  - Export job logged under My Account or Team Settings depending on ownership_type  
  - Log fields: Export ID, dataset_id, format, range, requested_by, ownership_type, timestamp, status  
- **If Download Immediately**:  
  - Only aggregated count (download/export usage) stored in statistics  

---

## 4. Key Features
1. **Adoption Visibility**: which models are using the dataset.  
2. **API Monitoring**: request volume trends and peak activity.  
3. **Popularity Metrics**: views and downloads over time.  
4. **Export Options**: usage reports in CSV/JSON for external analysis.  
5. **Transparency**: all exports logged for reproducibility.  

---

## 5. Navigation Flow
- Dataset Detail → [Usage & Statistics tab]  
- User can:
  - View linked models
  - Inspect API request trends
  - Check downloads/views history
  - Export usage reports via modal
