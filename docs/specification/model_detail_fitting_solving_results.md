# Model Detail Fitting & Solving Results Specification (Improved)

## 1. Overview

* **Location**: Models → Model Detail → Fitting & Solving Results
* **Purpose**: Provide a full record of model fitting & solving outcomes, not just one-off runs but also **scheduled or parameterized multiple runs**.
* **Primary Users**: Researchers, analysts, team leads

---

## 2. Enhanced Key Features

1. **Run Overview (Single & Batch)**

   * Supports both **single execution runs** and **batch runs** (multi-parameter fitting/solving jobs)
   * Each run (or batch) assigned a **Run Group ID**
   * Batch runs can be initiated manually or scheduled via cron

2. **Parameter Set Management**

   * Users can define multiple parameter sets in advance
   * Each parameter set tracked separately: initial values, fitted results, confidence intervals
   * Run results can be filtered by parameter set

3. **Residual & Error Analysis (per parameter set)**

   * Residuals shown per run, but also aggregated across parameter sets (e.g. distribution of RMSE across 10 runs)
   * Comparison mode: overlay residual plots of multiple parameter sets

4. **Solving Results (Batch-Aware)**

   * Each run yields solution curves (ODE/PDE/time series forecasts, agent simulation outcomes)
   * Option to **stack/overlay plots** for parameter sets in the same batch
   * Aggregate view: “solution envelope” (e.g. min–max band across multiple parameterizations)

5. **Performance Metrics Panel (Extended)**

   * Per-run metrics (RMSE, R², AIC, etc.)
   * Batch-level summary: best/worst/median metrics
   * Highlight of **“best run”** under chosen metric

6. **Visualization Panel**

   * Multi-run visualization modes:

     * **Overlay** (multiple parameter sets on same chart)
     * **Grid** (each parameter set in separate sub-chart)
     * **Summary band** (aggregate confidence envelope across runs)
   * Progress indicators for ongoing cron jobs

7. **Run History & Scheduling**

   * Timeline view includes both single runs and parameter-batch runs
   * Cron-scheduled jobs shown with recurrence metadata
   * Option to drill down from batch → individual runs

8. **Integration with Scenario Comparison**

   * While “Scenario Comparison” tab compares across **datasets or model configurations**,
     the **Fitting & Solving Results** tab focuses on **parameter-level variations**.
   * Users can export a batch run into Scenario Comparison for higher-level juxtaposition

---

## 3. UI Components (Extended)

### Header

* Title: **Fitting & Solving Results**
* Actions: `Re-run Single`, `Run Batch`, `Schedule via Cron`, `Export`, `Publish to Zenodo`

### Main Sections

1. **Run Summary / Batch Summary Card**

   * Run Group ID, timestamp, dataset, run type (single/batch), execution environment
2. **Parameter Set Panel**

   * Table of parameter sets with status (pending, running, completed)
   * Clickable row → detailed run results
3. **Residual & Error Analysis (Multi-view)**

   * Tabs: *Single run view / Batch overlay / Aggregate*
4. **Solving Results Visualization**

   * Overlay and grid toggle
   * Confidence envelope for batch results
5. **Performance Metrics Dashboard**

   * Best-run highlight + distribution chart across parameter sets
6. **Run History Timeline**

   * Single vs batch runs distinguished
   * Cron jobs labeled with recurrence icons

---

## 4. Extended Data Schema

| Field Name           | Type      | Description                                   |
| -------------------- | --------- | --------------------------------------------- |
| run\_group\_id       | string    | Unique group ID for batch or single run       |
| run\_id              | string    | Individual run ID (within group)              |
| run\_type            | string    | Single / Batch                                |
| dataset\_id          | string    | Dataset used                                  |
| parameters           | object\[] | \[{name, initial, fitted, ci\_low, ci\_high}] |
| batch\_parameters    | object\[] | Array of parameter sets (for batch runs)      |
| execution\_schedule  | object    | {cron\_expression, next\_run\_time}           |
| execution\_env       | string    | CPU/GPU, solver info                          |
| residuals            | float\[]  | Residual values                               |
| metrics              | object    | {rmse, mae, r2, aic, bic}                     |
| metrics\_summary     | object    | {best, worst, median across batch}            |
| solution\_results    | object    | Outputs (time series, PDE solutions, etc.)    |
| visualization\_links | object\[] | Chart metadata per run/parameter set          |
| run\_status          | string    | Success / Failed / In-progress                |
| aggregate\_view      | object    | Min/max/mean envelope data for batch          |
| comparison\_tag      | string    | Reference flag for scenario comparison        |

---

## 5. Permissions

* **Viewer** – read-only access to results
* **Contributor** – can run single or batch jobs and export scenarios
* **Owner** – can schedule jobs via cron and manage runs for owned models
* **Admin** – can delete or manage any batch runs

---

## 6. Example User Flow

1. User opens **Fitting & Solving Results** tab
2. Defines multiple parameter sets → launches a **Batch Run**
3. Cron executes runs overnight, results populated automatically
4. User sees batch summary: envelope plots, best-run highlighted
5. User exports batch to **Scenario Comparison** for cross-model context
6. User publishes selected run(s) to Zenodo
