# Model Detail Specification

## 1. Screen Name

**Model Detail**

---

## 2. Purpose

* Provide a unified page for viewing and managing a single model.
* All sub-sections are presented as **tabs** for easier navigation (instead of separate pages).
* Support exploration of model structure, results, validation, schedules, related datasets, and publication history.

---

## 3. Layout

### A. Header

* **Title**: model name
* **Breadcrumb**: `Models > Model Detail`
* **Global Actions**:

  * \[Edit Model] → opens `model_builder`
  * \[Save Draft]
  * \[Publish to Platform]
  * \[Export to Zenodo] (optional)

### B. Tab Navigation

Tabs are top-level navigation within the page:

1. Overview
2. Fitting & Solving Results
3. Validation & Backtesting Reports
4. Prediction Schedules
5. Scenario Comparison
6. Versions & Update Logs
7. Community
8. API Access
9. Related Datasets
10. Publication History

---

## 4. Tab Specifications

### 1) Overview

* **Description**: model name, type, purpose
* **Properties**: model type (PDE, ODE, Time-series, Agent-based …), linked datasets
* **Visualization**: block diagram of model structure
* **Metadata**: created by, creation date, last updated

---

### 2) Fitting & Solving Results

* **Outputs**: parameter estimates, error metrics
* **Visualizations**: residual plots, convergence graphs
* **Raw data**: downloadable JSON/CSV

---

### 3) Validation & Backtesting Reports

* **Metrics**: RMSE, MAPE, R², accuracy
* **Cross-validation results** (time-split, k-fold, walk-forward)
* **Visualization**: charts comparing prediction vs. actuals
* **Export**: PDF/HTML report

---

### 4) Prediction Schedules

* **Forecast horizon settings** (next n steps, date range)
* **Scheduled runs** (auto re-computation)
* **Visualization**: forecast line chart
* **Export**: predicted values (CSV/JSON)

---

### 5) Scenario Comparison

* **Functionality**: run multiple parameter scenarios in parallel
* **Comparison table**: metrics side-by-side
* **Graphs**: overlay plots of scenarios
* **Actions**: \[Add Scenario]

---

### 6) Versions & Update Logs

* **Version list**: v1, v2, v3 …
* **Changelog**: modifications summary
* **Rollback option**: restore previous version
* **Export**: version snapshot as archive

---

### 7) Community

* **Posts/Threads**: discussions about this model
* **Comments & Ratings**
* **Team Activity Feed**

---

### 8) API Access

* **Auto-generated API endpoint** for the model
* **Usage examples** (Python, R, curl)
* **Authentication requirements**
* **Rate limits / quotas**

---

### 9) Related Datasets

* **List of linked datasets**
* **Schema preview**
* **Quick navigation** to dataset detail pages

---

### 10) Publication History

* **List of exports to Zenodo** (if any)
* DOI, version, date, title, authors
* **Citation formats** (BibTeX, APA, MLA)
* \[Publish to Zenodo] button

---

## 5. States

* **Draft** (internal only, private)
* **Published (Platform)** (internal visibility: Private / Team / Public)
* **Exported to Zenodo** (optional, DOI linked)

---

## 6. Permissions

* **Viewer** – read-only
* **Contributor** – edit, publish, and export models they create or team models
* **Owner** – Contributor 권한 + 가시성, 역할, 공개 설정 관리
* **Admin** – manage all models

---

## 7. API Integration

* Local DB: `models`, `model_versions`, `model_results`, `model_scenarios`, `model_publications`
* External: Zenodo API (optional publication), Execution Engine API (results/forecasts)

---

## 8. Example Wireframe (Text)

```
-------------------------------------------------
Model: Economic Forecasting v3

Tabs: [Overview] [Results] [Validation] [Prediction] [Scenarios] 
      [Versions] [Community] [API] [Datasets] [Publication]

-------------------------------------------------
[Overview]
Type: Time-series
Linked Datasets: MacroEconomics v5
Created by: Yoon Jihyeon
Last updated: Aug 2025
-------------------------------------------------
```
