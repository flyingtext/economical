# Dataset Catalog Specification

## 1. Overview

* **Location**: Datasets → Dataset Catalog
* **Purpose**: Centralized catalog to browse and manage datasets, with options to create, clone, and reuse across models.
* **Primary Users**: Researchers, data managers, analysts, community contributors

---

## 2. Key Features

1. **Tabbed Views**

   * **My Datasets**: Created or cloned by the logged-in user
   * **Team Datasets**: Shared datasets accessible to user’s teams
   * **Public Datasets**: Datasets shared openly across the platform

2. **List/Grid View Toggle**

   * Default: list view with metadata summary
   * Option to switch to grid (card) view

3. **Dataset Summary Card/List Item**

   * Dataset name
   * Version info (latest / multiple versions)
   * Schema preview (columns, types, units)
   * Source & Citation info (DOI, URL, BibTeX availability)
   * Usage statistics (downloads, linked models, views)
   * Community metrics (likes, comments, shares)
   * Last updated timestamp

4. **Dataset Showcase Status (inline indicators)**

   * **Versioning**: current vs total versions
   * **Update frequency**: manual / automated (cron updates)
   * **Data quality indicators**: completeness %, last validation check

5. **Search & Filter**

   * Global search across dataset name, tags, keywords
   * Filters:

     * Dataset type (time series, panel, spatial, text, etc.)
     * Source (uploaded, external URL/API, Zenodo import)
     * Update status (latest only, historical versions)
     * Visibility (My / Team / Public)
     * Tags (discipline: finance, epidemiology, climate, etc.)

6. **Sorting Options**

   * Newest / Recently updated
   * Most used (linked models, downloads)
   * Most popular (likes, shares)

7. **Quick Actions**

   * **View Detail** → opens Dataset Detail page
   * **Link to Model** (if permission)
   * **Export** (CSV/JSON, or publish to Zenodo if available)
   * **Favorite** → bookmark dataset
   * **Clone** → copy dataset into user’s workspace (personal/team)

     * Opens Dataset Builder with schema and metadata pre-filled
     * Actual data files are referenced, not duplicated (user may re-import or replace data)

---

## 3. UI Components

### Header

* Page title: **Dataset Catalog**
* Tabs: `My Datasets | Team Datasets | Public Datasets`
* Global search bar
* Sort dropdown
* Filter button

### Main Content (List/Grid)

* Each row/card includes:

  * Dataset Name
  * Version info
  * Schema preview (sample columns)
  * Source & Citation
  * Usage stats (downloads, linked models, views)
  * Community metrics (likes, comments, shares)
  * Updated timestamp
  * Quick Actions: View, Link, Export, Favorite, Clone

### Sidebar (optional)

* Quick Filters (dataset type, update status, source)
* Recently Viewed Datasets
* Zenodo shortcuts (if user linked Zenodo account)

---

## 4. Data Schema (simplified)

| Field Name         | Type      | Description                            |
| ------------------ | --------- | -------------------------------------- |
| dataset\_id        | string    | Unique dataset ID                      |
| dataset\_name      | string    | Dataset name                           |
| version            | string    | Current version                        |
| schema\_preview    | object\[] | Example of columns/types/units         |
| source\_info       | string    | Source/citation reference              |
| usage\_stats       | object    | {downloads, linked\_models, views}     |
| community\_metrics | object    | {likes, comments, shares}              |
| update\_status     | string    | Manual / Automated (cron)              |
| visibility         | string    | My / Team / Public                     |
| owner\_id          | string    | User who created dataset               |
| team\_id           | string    | Team identifier                        |
| updated\_at        | datetime  | Last update timestamp                  |
| is\_favorited      | boolean   | Whether current user favorited dataset |
| can\_clone         | boolean   | User permission flag for Clone action  |

---

## 5. Permissions

* **Viewer** – can browse public datasets
* **Contributor** – can create, export, and clone datasets; link to models they own
* **Owner** – full control over owned datasets (edit, delete, manage visibility)
* **Admin** – manage all datasets across the platform

---

## 6. Example User Flow

1. User enters **Dataset Catalog** page
2. Chooses tab: *My Datasets / Team Datasets / Public Datasets*
3. Applies filters (e.g., time-series, updated recently, public only)
4. Sees list with version & usage info inline
5. Clicks “View Detail” → goes to Dataset Detail
6. Or clicks “Clone” → opens Dataset Builder with pre-filled metadata/schema
7. Optionally links dataset to a model or exports data

