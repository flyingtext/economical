# Model Builder Specification

## 1. Screen Name

**Model Builder (Create / Edit)**

---

## 2. Purpose

* Provide a unified environment for **creating and editing models**.
* Use a **visual node-based editor** where datasets (rectangles) and model types (circles) can be connected.
* Support both **preset models** and **Strict Python custom logic**.
* Models can remain **stored internally on the platform** or be optionally **exported to Zenodo (DOI)**.

---

## 3. Layout

### A. Header

* **Title**: `Model Builder`
* **Breadcrumb**: `Models > Model Builder`
* **Global Actions**:

  * \[Save Draft]
  * \[Publish] (to platform)
  * \[Cancel]

### B. Main Editor (Canvas)

* **Canvas (Drag & Drop)**

  * Dataset nodes = rectangles
  * Model nodes = circles
  * Final output node = hexagon
  * Connections = arrows (Dataset → Model → Output)

* **Sidebar Panels**

  * **Inspector Panel**: edit node properties (dataset/model/output)
  * **Validation / Prediction Settings**
  * **Strict Python Editor** for custom transformations or model code

### C. Tab Navigation

1. Overview
2. Editor (Visual Canvas)
3. Parameters
4. Execution Settings
5. Validation & Backtesting
6. Publish

---

## 4. Node Specifications

### Dataset Node (Rectangle)

* **Properties**

  * Dataset name, version
  * Schema preview (columns, type, unit)
* **Actions**

  * \[Select Input Columns]
  * \[Edit in Python] → row-level transform function

    ```python
    def transform(row):
        return {
            "x": row["GDP"],
            "y": row["Inflation"]
        }
    ```
* **Output**: dictionary per row `{col_name: value}`

---

### Model Node (Circle)

* **Properties**

  * Model type: PDE / ODE / Time-series / Agent-based / State-space / Mixed
  * Preset algorithm OR Strict Python
* **Preset Model**: input dict → output dict
* **Strict Python Model**:

  ```python
  def model_fn(row):
      return {
          "forecast": row["x"] * 1.05
      }
  ```
* **Configurable output column names**

---

### Final Output Node (Hexagon)

* **Properties**

  * Output schema (columns, types, units)
  * Row aggregation to build the final result
* **Actions**

  * Export CSV/JSON
  * Link to Dashboard

---

## 5. Extended Features

### Validation

* Sidebar panel: choose metrics (RMSE, MAPE, R², Accuracy)
* Custom metric (Python):

  ```python
  def custom_metric(y_true, y_pred):
      return abs(y_true - y_pred) / y_true
  ```

### Prediction

* Sidebar panel: set forecast horizon, scenario parameters
* Or custom forecasting in Python

### Comparison

* \[Add Comparison] → adds another Final Output node
* Enables multiple model outputs to be compared

---

## 6. Data Types

* SPSS-like classification
* Auto-inferred + editable
* Types: Numeric, Categorical, DateTime, Boolean, Text
* Displayed as icons/tags in schema

---

## 7. Model Lifecycle States

* **New Model**: created, not saved
* **Draft**: stored on the platform server, private
* **Published (Internal)**: visible in platform (Private / Team / Public)
* **Exported to Zenodo (Optional)**: published externally, DOI issued

### Transitions

* New Model → Draft (Save Draft)
* Draft → Published (Publish to Platform)
* Draft → Zenodo (optional export)
* Published → Zenodo (export later)
* Published → Draft (unpublish/edit rollback)

---

## 8. Permissions

* Viewer: read-only
* Editor/Owner: full edit, save, publish, export
* Team Member: restricted based on role

---

## 9. API Integration

* **Local DB**

  * `models`
  * `model_nodes`
  * `model_edges`
  * `model_parameters`
  * `validation_templates`
* **External**

  * Zenodo API (optional export)
  * Execution Engine API (solver/simulation backend)

---

## 10. Example Flow

```
[Dataset: MacroEconomics] --(GDP, Inflation)--> (Time-series Model) --(Forecast)--> [Final Output]

   Save Draft → Stored internally
   Publish → Visible in platform (internal)
   Export to Zenodo → DOI assigned (optional)
```
