# Project Builder Screen Specification

## 1. Screen Name

**Project Builder (Create / Edit)**

---

## 2. Purpose

* Provide researchers with an interface to **create or edit projects**.
* Allow linking of models, datasets, and members into a unified project.
* Support configuration of resource settings and publication templates.
* Save as draft, publish internally, or optionally export to Zenodo.

---

## 3. Layout

### A. Header

* **Title**: `Project Builder`
* **Breadcrumb**: `Projects > Project Builder`
* **Global Actions**:

  * \[Save Draft]
  * \[Publish to Platform]
  * \[Cancel]

### B. Tab Navigation

1. Basic Info
2. Linked Models
3. Linked Datasets
4. Team Members & Roles
5. Resource & Execution Settings
6. Validation / Publication Templates
7. Publish

---

## 4. Tab Specifications

### 1) Basic Info

* Fields:

  * Project name
  * Description (markdown editor)
  * Tags (multi-select)
  * Visibility (Private / Team / Public)

---

### 2) Linked Models

* **Model Catalog modal**: search/filter models to add
* **Table of linked models**: model name, type, owner, status
* Actions: \[Add Model], \[Remove]

---

### 3) Linked Datasets

* **Dataset Catalog modal**: search/filter datasets to add
* **Table of linked datasets**: dataset name, schema preview, version
* Actions: \[Add Dataset], \[Remove]

---

### 4) Team Members & Roles

* **Members list**: user name, email, role (Viewer, Contributor, Owner, Admin)
* Actions: \[Add Member], \[Assign Role], \[Remove]
* Visual: member avatars

---

### 5) Resource & Execution Settings

* Resource allocation: CPU/GPU, memory limits
* Execution settings: batch size, iteration limits
* Credit usage forecast (if platform enforces quotas)

---

### 6) Validation / Publication Templates

* **Validation templates**: time-split, k-fold, walk-forward, or custom
* **Publication template selection**: choose predefined structure for exporting reports (overview\.md, results.json, report.html)
* Option to save custom templates

---

### 7) Publish

* **Summary view**: recap of all tabs (info, models, datasets, members, settings)
* Actions:

  * \[Save Draft]
  * \[Publish to Platform]
  * \[Export to Zenodo] (optional)
* Validation check: required fields completed? Show warnings if missing.

---

## 5. States

* **New Project**: unsaved
* **Draft**: saved internally, private
* **Published (Platform)**: visible in platform (Private / Team / Public)
* **Exported to Zenodo (Optional)**: external DOI assigned

---

## 6. Permissions

* **Viewer** – no access
* **Contributor** – can link resources and configure settings for their projects
* **Owner** – full control, including managing members and publication
* **Admin** – manage all projects

---

## 7. API Integration

* **Local DB**

  * `projects` (id, name, description, owner\_id, team\_id, status, created\_at, updated\_at)
  * `project_models` (project\_id, model\_id)
  * `project_datasets` (project\_id, dataset\_id)
  * `project_members` (project\_id, user\_id, role)
  * `project_templates` (validation, publication)
* **External**

  * Zenodo API (optional publication)

---

## 8. Example Wireframe (Text)

```
-------------------------------------------------
[ Project Builder ]

Tabs: [Info] [Models] [Datasets] [Members] [Resources] [Validation] [Publish]

-------------------------------------------------
[Basic Info]
Name: [________________________]
Description: [Markdown Editor]
Tags: [____]   Visibility: (o Private) ( ) Team ( ) Public

[ Save Draft ] [ Cancel ]
-------------------------------------------------
```

