# Screen Definition: Model Detail – Prediction Schedules

This page manages the **scheduling and execution of model predictions**.  
Researchers can configure when and how often a model runs predictions, bind datasets, and monitor outputs.

---

## 1. Page Header
- **Model Name** (title, linked to Model Overview)
- **Version Selector** (switch between model versions)
- **Action Buttons**
  - `New Schedule`
  - `Run Now`
  - `Export Predictions (CSV / JSON / API)`
  - `Publish to Zenodo (DOI)`

---

## 2. Schedule Overview
- **Table of Active Schedules**
  - Schedule Name
  - Frequency (`Once`, `Hourly`, `Daily`, `Weekly`, `Monthly`, `Custom CRON`)
  - Next Run Time
  - Dataset Bound
  - Status (`Active`, `Paused`, `Error`)
  - Last Run Result (`Success`, `Failed`, metrics snapshot)
  - Actions (`View`, `Edit`, `Pause`, `Delete`)

---

## 3. Create / Edit Schedule (Modal or Page)
- **Basic Info**
  - Schedule Name
  - Description / Notes
- **Execution Frequency**
  - One-time run (date/time picker)
  - Recurring run (interval or CRON expression)
- **Dataset Binding**
  - Select dataset (with version selection)
  - Option to auto-update when new dataset version published
- **Execution Settings**
  - Parameters & constraints
  - Compute resource preferences (standard / high-performance node)
- **Output Handling**
  - Save to Dataset (auto-generated output dataset)
  - Export to API endpoint
  - Email notification with results (attachments or download link)
  - Zenodo auto-publication option (DOI each run or per schedule)
- **Permissions**
  - Share with team
  - Restrict to owner only
- **Save / Cancel**

---

## 4. Run Detail (Per Schedule)
- **Execution Log Table**
  - Run ID
  - Timestamp
  - Dataset version used
  - Parameters snapshot
  - Status (`Pending`, `Running`, `Success`, `Failed`)
  - Duration
  - Metrics summary
- **Expandable Row → Detailed Report**
  - Prediction outputs (chart + table)
  - Error logs (if failed)
  - Export options (CSV, JSON, HTML)

---

## 5. Visualization
- **Prediction Timeline**
  - Calendar or timeline view of scheduled runs
  - Indicators for `Upcoming`, `Completed`, `Failed`
- **Charts**
  - Predicted vs Actual overlay (if validation data available)
  - Aggregated forecast trends

---

## 6. Notifications
- **Subscription Options**
  - Run completed successfully
  - Run failed (with error message)
  - Schedule updated by team member
- **Delivery Channels**
  - In-app alerts
  - Email notifications
  - API webhook callbacks

---

## 7. Community & Collaboration
- **Discussion thread per schedule**
- **Team notes & annotations**
- **Ratings / endorsement of schedule reliability**

---

## 8. Export & Publication
- **Exports**
  - CSV / JSON outputs
  - Interactive HTML dashboards
- **Zenodo Publication Workflow**
  - Auto-generate prediction result package
  - Assign DOI per published run or per schedule
