# 📂 Dataset Catalog — Screen Definition (v3)

## 1. Purpose

The Dataset Catalog is the entry point for exploring datasets.
It enables users to **search, filter, evaluate usage (models + API calls), and connect datasets** to their workflows.

---

## 2. Layout Components

### (A) Top Bar — Search & Filter

* **Search Box**: full-text across title, description, tags, sources
* **Filters**:

  * Domain: Macroeconomics / Financial Markets / Industry / Demographics / Environment …
  * Data Type: Time-series / Panel / Cross-section / GIS / Other
  * Access Scope: Public / Team-only / Private
  * Source: User Upload / API Integration / Zenodo / Other
  * Last Update: Past 7 days / 30 days / 1 year / All
* **Sorting Options**

  * Most Recent Updates
  * Most Popular (views + downloads)
  * Highest API Usage
  * Alphabetical
  * Highest Rating

---

### (B) Main Content — Dataset List/Grid

* **Toggle**: Card view ↔ List view
* **Dataset Item Components**

  * Thumbnail (preview or icon)
  * Title + Short Description
  * Tags / Keywords
  * Latest Update Date
  * Record Count & Coverage (e.g., “1990–2024, 15k rows”)
  * Access Scope (Public / Team / Private)
  * **Usage Metrics**

    * 🔗 Linked Models Count (e.g., “Used in 5 Models”)
    * 📡 API Requests (e.g., “12.4k calls this month”)
    * 👀 Views / Downloads
  * Community Indicators: 👍 Likes, ⭐ Ratings, 💬 Comments
  * **Action Buttons**

    * **\[View Details]** → navigates to **Dataset Detail page**
    * **\[Use Now]** → opens **modal** (choose Project/Model to link dataset)

---

### (C) \[Use Now] Modal

* **Title**: “Select Target for Dataset”
* **Options**:

  * Project List (user/team projects)
  * Model List (available models)
  * Search/Filter inside modal for quick navigation
* **Confirm Button**: \[Link Dataset]
* **Cancel Button**: \[Close]

---

### (D) Right-side Panel

* Favorites (starred datasets)
* Recently Viewed
* Recommended Datasets (based on popularity/API activity)

---

### (E) Footer

* Pagination or Infinite Scroll
* Export current list (CSV / JSON)

---

## 3. Key Features

1. **Discovery**: search, filter, and sort by update, popularity, API load, etc.
2. **Usage Transparency**: show dataset adoption (linked models) + API traffic.
3. **Workflow Integration**:

   * \[Use Now] opens modal → user selects **Project/Model** to connect dataset.
   * \[View Details] leads to **Dataset Detail page** (Overview, Schema, Source, Versions, Usage, Community…).
4. **Community Engagement**: likes, ratings, comments visible in Catalog.
5. **Export**: save filtered dataset metadata + usage metrics.

---

⚡ With this design, the **Catalog works like a dataset marketplace**, while the **modal ensures direct workflow integration** without losing context.
