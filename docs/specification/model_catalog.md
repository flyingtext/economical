# Model Catalog Specification

## 1. Overview

* **Location**: Models → Model Catalog
* **Purpose**: Centralized catalog of models, allowing users to browse their own models, team models, and public models.
* **Primary Users**: Researchers, analysts, teams, and general community members

---

## 2. Key Features

1. **Tabbed Views**

   * **My Models**: Models created or owned by the logged-in user
   * **Team Models**: Models shared within the user’s teams
   * **Public Models**: All publicly shared models across the platform

2. **List/Grid View Toggle**

   * Default list view, with option to switch to grid (card) view
   * Each entry displays both metadata and execution status

3. **Model Showcase Status (inline on list level)**

   * **Execution State**: (Idle, Running, Completed, Failed)
   * **Benchmark Level Reached**: (Baseline, Advanced, Published)
   * **Progress %**: e.g., fitting or solving progress bar
   * **Validation Status**: (Repeated validation runs, Pass/Fail metrics)
   * **Prediction Status**: (Next scheduled prediction, last prediction outcome)

4. **Model Summary Card/List Item**

   * Model name + version
   * Core algorithm/methodology (e.g., ARIMA, PDE Solver, Agent-based model)
   * Linked datasets (count or preview list)
   * Key metrics (R², RMSE, AIC, etc.)
   * Showcase status block (execution/validation/prediction info)
   * Creator and team info
   * Community metrics (likes, comments, shares)
   * Updated timestamp (last run / last modified)

5. **Search & Filter**

   * Global search across model name, tags, algorithms
   * Filters:

     * Model type (PDE, ODE, Time-series, Agent-based, etc.)
     * Execution state (Running, Completed, Failed)
     * Visibility (My / Team / Public)
     * Validation status (Validated, In-progress, Not validated)
     * Tags (e.g., finance, epidemiology, climate)

6. **Sorting Options**

   * Newest / Last updated
   * Most used
   * Most accurate
   * Most popular (likes, shares)

7. **Quick Actions**

   * “View Detail” (go to Model Detail page)
   * “Run Again” (if user has execution rights)
   * “Export” (download or Zenodo publish if available)
   * “Favorite” (bookmarking)

---

## 3. UI Components

### Header

* Page title: **Model Catalog**
* Tabs: `My Models | Team Models | Public Models`
* Global Search bar
* Sort dropdown
* Filter button

### Main Content (List View)

* Each row/card includes:

  * Thumbnail (optional visualization snapshot)
  * **Model Name + Version**
  * Algorithm / Method
  * Showcase Status (execution state, progress bar, validation, prediction)
  * Linked Datasets
  * Metrics overview (quick stats)
  * Community metrics (likes, comments, shares)
  * Quick Actions (buttons: View, Run, Export, Favorite)

### Right Sidebar (optional)

* **Quick Filters** (execution state, validation status, model type)
* **Recently Viewed Models**
* **Zenodo Publication Shortcuts** (if applicable)

---

## 4. Data Schema (simplified)

| Field Name         | Type      | Description                                       |
| ------------------ | --------- | ------------------------------------------------- |
| model\_id          | string    | Unique model ID                                   |
| model\_name        | string    | Model name                                        |
| version            | string    | Version number                                    |
| algorithm          | string    | Algorithm/method                                  |
| datasets\_linked   | string\[] | Linked dataset IDs                                |
| metrics            | object    | Performance metrics                               |
| execution\_state   | string    | Idle / Running / Completed / Failed               |
| benchmark\_level   | string    | Baseline / Advanced / Published                   |
| progress\_percent  | int       | Progress of execution/solving                     |
| validation\_status | string    | Validated / Failed / In-progress                  |
| prediction\_status | object    | {next\_scheduled: datetime, last\_result: string} |
| created\_by        | string    | Author                                            |
| team\_id           | string    | Team identifier                                   |
| visibility         | string    | My / Team / Public                                |
| likes\_count       | int       | Likes                                             |
| comments\_count    | int       | Comments                                          |
| shares\_count      | int       | Shares                                            |
| updated\_at        | datetime  | Last update                                       |

---

## 5. Permissions

* **Viewer** – can browse public models
* **Contributor** – can edit, run, delete, or export models they own and contribute to team models
* **Owner** – full control over owned models, including visibility and publication management
* **Admin** – manage all models across the platform

---

## 6. Example User Flow

1. User enters **Model Catalog** page
2. Chooses tab: *My Models / Team Models / Public Models*
3. Uses filters (e.g., only Running models, PDE type)
4. Sees list with execution/validation/prediction status inline
5. Clicks a model → goes to Model Detail
6. Optionally runs model again or exports results
