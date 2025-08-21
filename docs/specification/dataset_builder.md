# Dataset Builder — Screen Definition

## 1. Screen Purpose

The **Dataset Builder** provides a guided interface to create or edit datasets.
It supports manual upload, API binding, schema definition, citation management, and importing datasets directly from Zenodo using DOI.
Export to Zenodo is **not supported directly**; datasets are exported only when bundled with models for publication.

---

## 2. Layout Components

### (A) Navigation Tabs (Builder Steps)

* Basic Info
* Schema Definition
* Source & Citation
* Data Upload & Import
* Versions & Update Management
* Access Permissions
* Save Draft / Publish

---

## 3. Sub-Screens

### 3.1 Basic Info

* **Fields**

  * Dataset Name
  * Description (Markdown supported)
  * Tags (comma-separated)
  * Visibility (Private / Team / Public)
* **Actions**

  * \[Save Draft]
  * \[Next → Schema Definition]

---

### 3.2 Schema Definition

* **Schema Table**

  * Column Name
  * Data Type (int, float, string, datetime, boolean)
  * Unit (optional)
  * Description
* **Actions**

  * \[Add Column]
  * \[Import Schema from File] (CSV header or JSON schema)
  * \[Save Schema]

---

### 3.3 Source & Citation

* **Citation Types**

  * BibTeX Entry (text area)
  * URL Reference (string, with fetch metadata option)
  * Zenodo DOI (imported source; auto-filled if dataset imported from Zenodo)
* **Display**

  * List of all citations attached to dataset
  * Show type, value, date added
* **Actions**

  * \[Add Citation]
  * \[Delete Citation]

---

### 3.4 Data Upload & Import

* **Upload Options**

  * Upload CSV (single or multiple files)
  * Upload JSON
  * API Binding (provide endpoint + auth)
* **Import Option**

  * **Import from Zenodo DOI**

    * Input field: DOI string (e.g., `10.5281/zenodo.1234567`)
    * \[Fetch Metadata] → displays dataset title, authors, description, license, and available files
    * Preview table: file names, size, format
    * \[Import Dataset] → downloads and registers dataset version in Economical
* **Actions**

  * \[Validate Data] (schema compliance check)
  * \[Save Draft]

---

### 3.5 Versions & Update Management

* **Version Table**

  * Version Tag
  * Changelog
  * Created At
  * Created By
* **Actions**

  * \[Create New Version] (snapshot current dataset state)
  * \[Restore Version]

---

### 3.6 Access Permissions

* **Permissions Table**

  * User / Team
  * Access Level (Read / Write / Admin)
* **Actions**

  * \[Add Permission]
  * \[Remove Permission]

---

### 3.7 Save Draft / Publish

* **Save Options**

  * \[Save Draft] (keeps dataset private until published)
  * \[Publish Dataset] (makes dataset visible according to chosen visibility)
* **Note**: Export to Zenodo is not available at dataset level. Datasets are exported **only as part of model publication workflows**.

---

## 4. Modals

### Schema Import Modal

* Upload CSV/JSON to auto-generate schema preview before applying

### API Binding Modal

* Configure API endpoint, authentication, refresh frequency

### Zenodo Import Modal

* Input: DOI
* Output: metadata preview (title, authors, license, files)
* Action: \[Import]

---

## 5. Key Features

1. **Flexible Data Input** — Upload from files, APIs, or import directly from Zenodo by DOI.
2. **Schema Control** — Explicit schema definition with units and types.
3. **Citation Management** — Record BibTeX, URL, and Zenodo DOI as data provenance.
4. **Versioning** — Track changes across dataset versions with changelog.
5. **Access Permissions** — Control dataset access at user/team level.
6. **Separation of Concerns** — Export to Zenodo only occurs through model bundling, avoiding license issues with standalone datasets.

---

## 6. Navigation Flow

* Access from Dataset Catalog → \[Create Dataset] or \[Edit Dataset]
* Builder guides user step by step: Basic Info → Schema → Source & Citation → Data Upload & Import → Versions → Permissions → Save/Publish
* Importing from Zenodo DOI populates citation automatically and stores source metadata
* Published datasets appear in Dataset Catalog with proper provenance

