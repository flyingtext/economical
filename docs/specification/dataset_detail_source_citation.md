# Dataset Detail — Source & Citation — Screen Definition

## 1. Screen Purpose

The **Source & Citation** sub-screen provides full provenance information for the dataset.
It enables users to record, view, and manage citations (BibTeX, URLs, Zenodo DOIs) and ensures transparency of dataset origins.
When a dataset is imported from Zenodo, its DOI and associated metadata are displayed here.

---

## 2. Layout Components

### (A) Header

* Title: **Source & Citation**
* Dataset Name (breadcrumb from parent Dataset Detail)

### (B) Citation List Panel

* **Citation Table Columns**

  * Type (BibTeX / URL / Zenodo DOI)
  * Value (string or DOI identifier)
  * Metadata Preview (for Zenodo: title, authors, license; for URL: fetched title if available)
  * Added At (timestamp)
  * Actions (\[View], \[Delete])

* **Examples**

  * BibTeX: `@article{...}` (expandable)
  * URL: `https://example.com/source` (with fetched title: “OECD Economic Outlook 2025”)
  * Zenodo DOI: `10.5281/zenodo.1234567` (with metadata: “Dataset: Global Financial Indicators”, Author: J. Doe, License: CC-BY-4.0)

### (C) Add Citation Panel

* **Input Options**

  * Radio select: \[BibTeX] / \[URL] / \[Zenodo DOI]
* **Fields**

  * If BibTeX → Textarea (paste entry)
  * If URL → URL input field (+ optional fetch metadata button)
  * If Zenodo DOI → DOI input field (`10.xxxx/zenodo.xxxxxxx`)
* **Actions**

  * \[Fetch Metadata] (for URL/DOI)
  * \[Add Citation]

---

## 3. Zenodo DOI Handling

### (A) Import Mode

* If dataset was originally imported from Zenodo Builder:

  * DOI entry is auto-filled and **locked (non-deletable)**
  * Metadata (title, authors, license, description) displayed in detail box

### (B) Manual Citation Mode

* If user adds Zenodo DOI manually (for provenance reference only):

  * DOI shown in table with fetched metadata
  * Can be deleted like other citations

---

## 4. Modals

### (A) View Citation Modal

* Full metadata or BibTeX entry shown in detail view
* Copy-to-clipboard button

### (B) Delete Citation Modal

* Confirmation required
* Message: “Are you sure you want to remove this citation? This does not delete the dataset itself, only its provenance reference.”
* Exception: Zenodo DOI added via Import Mode cannot be deleted

---

## 5. Key Features

1. **Comprehensive Provenance** — Supports BibTeX, URLs, and Zenodo DOIs.
2. **Metadata Integration** — Automatically fetches and displays metadata from URL/DOI sources.
3. **Zenodo Import Lock** — Imported Zenodo DOIs are permanent, ensuring dataset provenance cannot be lost.
4. **Transparency & Reproducibility** — Clear history of when and how citations were added.
5. **User Control** — Citations can be added, previewed, or removed (except locked imports).

---

## 6. Navigation Flow

* From **Dataset Detail** → user clicks “Source & Citation” tab
* User sees all citations listed in a table
* User can add new citation by selecting type and providing input
* If DOI import is used, metadata is auto-fetched and displayed
* Imported Zenodo DOIs remain permanent; additional citations can still be added
