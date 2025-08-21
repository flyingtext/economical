# Project Detail Specification

## 1. Screen Name

**Project Detail**

---

## 2. Purpose

* Provide a comprehensive view of a single project.
* Consolidate all sub-sections into **tabs** for a single-page experience.
* Enable collaboration (members, roles), linked models/datasets overview, activity tracking, and publication history.

---

## 3. Layout

### A. Header

* **Title**: Project name (e.g., *Macroeconomic Forecasting*)
* **Breadcrumb**: `Projects > Project Detail`
* **Global Actions**:

  * \[Edit Project] → opens `project_builder`
  * \[Save Draft]
  * \[Publish to Platform]
  * \[Export to Zenodo] (optional)

### B. Tab Navigation

1. Overview
2. Linked Models
3. Linked Datasets
4. Team Members
5. Activity Logs
6. Publication History

---

## 4. Tab Specifications

### 1) Overview

* **Description**: project summary, objectives, scope
* **Properties**: owner/team, visibility (Private / Team / Public)
* **Statistics**: number of linked models, datasets, team members
* **Metadata**: created by, creation date, last updated

---

### 2) Linked Models

* **List of models included in the project**
* Columns: Model name, type, status, last updated
* Actions: \[View Model], \[Add Model], \[Remove]

---

### 3) Linked Datasets

* **List of datasets used in the project**
* Columns: Dataset name, schema preview, version, status
* Actions: \[View Dataset], \[Add Dataset], \[Remove]

---

### 4) Team Members

* **Members list** with role (Owner, Editor, Viewer)
* Columns: User name, role, joined date
* Actions: \[Add Member], \[Change Role], \[Remove]
* Visual: avatars for team members

---

### 5) Activity Logs

* **Timeline of changes** to the project
* Events: model added/removed, dataset linked/unlinked, member joined/left, publication updates
* Columns: Date, User, Action
* Export: CSV/JSON

---

### 6) Publication History

* **List of internal and external publications**
* Columns: Version, DOI (if Zenodo), title, authors, date published
* Actions: \[Export Citation], \[Publish to Zenodo]
* Citation formats: BibTeX, APA, MLA

---

## 5. States

* **Draft** (server-only, private)
* **Published (Platform)** (internal, visible to team/public based on settings)
* **Exported to Zenodo (Optional)** with DOI

---

## 6. Permissions

* Viewer: read-only
* Editor: can edit description, add/remove models/datasets, manage team
* Owner: full access + publication/export rights
* Admin: override permissions

---

## 7. API Integration

* **Local DB**

  * `projects` (id, name, description, owner\_id, team\_id, status, created\_at, updated\_at)
  * `project_models` (project\_id, model\_id)
  * `project_datasets` (project\_id, dataset\_id)
  * `project_members` (project\_id, user\_id, role)
  * `project_logs` (project\_id, action, timestamp, user\_id)
  * `project_publications` (project\_id, doi, metadata)
* **External**

  * Zenodo API (optional publication)

---

## 8. Example Wireframe (Text)

```
-------------------------------------------------
Project: Macro Forecasting Initiative

Tabs: [Overview] [Models] [Datasets] [Team] [Activity] [Publication]

-------------------------------------------------
[Overview]
Description: Forecasting macroeconomic indicators (GDP, inflation, trade).
Owner: J. Yoon
Visibility: Team
Models: 3   Datasets: 2   Members: 4
Last updated: Aug 21, 2025
-------------------------------------------------
```
