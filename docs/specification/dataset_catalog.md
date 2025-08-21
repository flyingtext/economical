# Dataset Catalog Specification

## 1. Overview

* **Location**: Datasets → Dataset Catalog
* **Purpose**: Centralized catalog to browse and manage datasets, separated into personal, team, and public scope.
* **Primary Users**: Researchers, data managers, analysts

---

## 2. Key Features

1. **Tabbed Views**

   * **My Datasets**: Created or owned by the logged-in user
   * **Team Datasets**: Shared datasets accessible to user’s teams
   * **Public Datasets**: Datasets shared openly across the platform

2. **List/Grid View Toggle**

   * Default: list view with metadata summary
   * Option to switch to grid (card) view

3. **Dataset Summary Card/List Item**

   * Dataset name
   * Version info (latest / multiple versions)
   * Schema preview (columns, types, units)
   * Source & Citation info (e.g., DOI, URL, BibTeX availability)
   * Usage statistics (downloads, linked models, views)
   * Community metrics (likes, comments, shares)
   * Last updated timestamp

4. **Dataset Showcase Status (inline indicators)**

   * **Versioning**: current vs total versions
   * **Update frequency**: manual / automated (cron updates)
   * **Data quality indicators** (optional): completeness %, last validation check

5. **Search & Filter**

   * Search by dataset name, tags, keywords
   * Filters:

     * Dataset type (time series, panel, spatial, text, etc.)
     * Source (uploaded, external URL/API, imported from Zenodo)
     * Update status (latest only, historical versions)
     * Visibility (My / Team / Public)
     * Tags (discipline: finance, epidemiology, climate, etc.)

6. **Sorting Options**

   * Newest / Recently updated
   * Most used (linked models, downloads)
   * Most popular (likes, shares)

7. **Quick Actions**

   * “View Detail” → Dataset Detail page
   * “Link to Model” (if permission)
   * “Export” (CSV/JSON, Zenodo publish if available)
   * “Favorite” (bookmarking)

---

## 3. UI Components

### Header

* Page title: **Dataset Catalog**
* Tabs: `My Datasets | Team Datasets | Public Datasets`
* Global search bar
* Sort dropdown
* Filter button

### Main Content (List View)

* Each row/card includes:

  * Dataset Name
  * Version status
  * Schema preview (sample columns)
  * Source & Citation
  * Usage metrics (downloads, linked models, views)
  * Community metrics (likes, comments)
  * Updated timestamp
  * Quick Actions (View, Link, Export, Favorite)

### Sidebar (optional)

* Quick Filters (dataset type, update status, source)
* Recently Viewed Datasets
* Zenodo shortcuts (if user linked Zenodo account)

---

## 4. Data Schema (simplified)

| Field Name         | Type      | Description                        |
| ------------------ | --------- | ---------------------------------- |
| dataset\_id        | string    | Unique dataset ID                  |
| dataset\_name      | string    | Dataset name                       |
| version            | string    | Current version                    |
| schema\_preview    | object\[] | Example of columns/types/units     |
| source\_info       | string    | Source/citation reference          |
| usage\_stats       | object    | {downloads, linked\_models, views} |
| community\_metrics | object    | {likes, comments, shares}          |
| update\_status     | string    | Manual / Automated (cron)          |
| visibility         | string    | My / Team / Public                 |
| owner\_id          | string    | User who created dataset           |
| team\_id           | string    | Team identifier                    |
| updated\_at        | datetime  | Last update timestamp              |

---

## 5. Permissions

* **Read**: based on visibility (My / Team / Public)
* **Export**: dataset owner, team members (if team-owned), or public (if allowed)
* **Link to Model**: dataset owner / team editors
* **Edit/Delete**: dataset owner / team admins

---

## 6. Example User Flow

1. User enters **Dataset Catalog** page
2. Chooses tab: *My Datasets / Team Datasets / Public Datasets*
3. Uses filters (e.g., only time-series datasets, public, updated recently)
4. Sees list with version & usage info inline
5. Clicks a dataset → goes to Dataset Detail page
6. Optionally links dataset to a model or exports data

