# Model Catalog Specification

## 1. Overview

* **Location**: Models → Model Catalog
* **Purpose**: Centralized catalog of models, allowing users to browse, search, filter, and clone models (own/team/public) into their workspace.
* **Primary Users**: Researchers, analysts, teams, and community members (contributors & viewers)

---

## 2. Key Features

1. **Tabbed Views**

   * **My Models**: Models created or cloned by the logged-in user
   * **Team Models**: Models shared within the user’s teams
   * **Public Models**: All publicly shared models across the platform

2. **List/Grid View Toggle**

   * Default: list view
   * Option: grid (card) view
   * Each entry displays metadata, execution state, and quick actions

3. **Model Showcase Status (inline on list level)**

   * **Execution State**: Idle / Running / Completed / Failed
   * **Benchmark Level Reached**: Baseline / Advanced / Published
   * **Progress %**: fitting/solving progress bar
   * **Validation Status**: repeated runs, pass/fail metrics
   * **Prediction Status**: next scheduled prediction, last prediction outcome

4. **Model Summary Card/List Item**

   * Model name + version
   * Core algorithm/methodology (ARIMA, PDE Solver, Agent-based, etc.)
   * Linked datasets (count or preview list)
   * Key metrics (R², RMSE, AIC, etc.)
   * Showcase status (execution/validation/prediction info)
   * Creator and team info
   * Community metrics (likes, comments, shares)
   * Updated timestamp (last run / modified)

5. **Search & Filter**

   * Search across model name, tags, algorithms
   * Filters:

     * Model type (PDE, ODE, Time-series, Agent-based, etc.)
     * Execution state (Running, Completed, Failed)
     * Visibility (My / Team / Public)
     * Validation status (Validated, In-progress, Not validated)
     * Tags (finance, epidemiology, climate, etc.)

6. **Sorting Options**

   * Newest / Last updated
   * Most used
   * Most accurate
   * Most popular (likes, shares)

7. **Quick Actions**

   * **View Detail** → opens Model Detail

   * **Run Again** → re-run model (if user has rights)

   * **Export** → download results or publish to Zenodo

   * **Favorite** → bookmark model

   * **Clone** → copy model into user’s workspace (personal/team)

   > ✅ **Clone** opens **Model Builder** with pre-filled values.
   > Datasets are referenced, not duplicated (user may re-import/replace).

---

## 3. UI Components

### Header

* Page title: **Model Catalog**
* Tabs: `My Models | Team Models | Public Models`
* Global Search bar
* Sort dropdown
* Filter button

### Main Content (List/Grid)

* Each row/card includes:

  * Thumbnail (optional snapshot/preview)
  * Model Name + Version
  * Algorithm / Method
  * Showcase status (execution, validation, prediction info)
  * Linked Datasets
  * Metrics overview (quick stats)
  * Community metrics (likes, comments, shares)
  * Quick Actions (View, Run, Export, Favorite, Clone)

### Right Sidebar (optional)

* Quick Filters (execution state, validation, model type)
* Recently Viewed Models
* Zenodo Publication Shortcuts

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
| is\_favorited      | boolean   | Whether user favorited this model                 |
| can\_clone         | boolean   | User permission flag for Clone action             |

---

## 5. Permissions

* **Viewer** – can browse Public Models (no run/export/clone)
* **Contributor** – can create new models and clone public/team models; run/export models they own
* **Owner** – full control over owned models, including visibility & publication
* **Admin** – manage all models across the platform

---

## 6. Example User Flow

1. User enters **Model Catalog** page
2. Chooses tab (My / Team / Public)
3. Applies filters (e.g., Running models, PDE type)
4. Sees list with inline execution/validation/prediction info
5. Clicks “View Detail” → opens Model Detail
6. Or clicks “Clone” → opens Model Builder with pre-filled data
7. Optionally runs model or exports results

