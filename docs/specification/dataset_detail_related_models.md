# Dataset Detail Related Models Specification

## 1. Overview

* **Location**: Datasets → Dataset Detail → Related Models
* **Purpose**: Display and manage models that are linked to or use the given dataset.
* **Primary Users**: Researchers, data scientists, team managers

---

## 2. Key Features

1. **Related Model List**

   * Automatically shows models that use the dataset as input
   * Sort by newest, most popular, highest accuracy, favorites
   * Filter by model type (PDE, ODE, time-series, agent-based, etc.)

2. **Model Summary Card**

   * Model name + version
   * Main algorithm/method (e.g., ARIMA, Black-Scholes PDE, Agent-based simulation)
   * Performance metrics (R², RMSE, AIC, etc.)
   * Optional visualization thumbnail
   * Author and team info
   * Community metrics (likes, comments, shares)

3. **Detail Navigation**

   * Clicking a card opens **Model Detail** page
   * Option to open in new tab or same page

4. **Search & Filter**

   * Search bar for model name or keywords
   * Filters:

     * Model type (PDE/ODE/time-series/agent-based, etc.)
     * Simulation tool used (e.g., PyMC, TensorFlow, R)
     * Visibility scope (My projects / Team shared / Public)
     * Version (Latest only / All versions)

5. **Dataset-Model Linking Management**

   * If user has permissions: “Add Related Model” button
   * Unlink existing connections
   * Display Zenodo DOI linkage status

6. **Zenodo Publication**

   * List of Zenodo DOIs published using this dataset
   * DOI entries link directly to Zenodo pages

---

## 3. UI Components

### Header

* Dataset name + “Related Models” tab highlight
* `Search bar`, `Sort dropdown`, `Filter button`

### Main Content

* **Model Card List (grid/list toggle supported)**

  * Thumbnail (optional) + Model name/version
  * Key metrics
  * Author/team name
  * Likes · Comments · Shares
  * “View Detail” button
* Pagination or infinite scroll

### Right Sidebar (optional)

* **Quick Filters**: Model type, visibility, tags
* **Zenodo DOI Box**

  * “Published Reports”
  * DOI list + publication date

---

## 4. Data Schema (simplified)

| Field Name          | Type      | Description                                        |
| ------------------- | --------- | -------------------------------------------------- |
| model\_id           | string    | Unique model ID                                    |
| model\_name         | string    | Model name                                         |
| version             | string    | Model version                                      |
| algorithm           | string    | Algorithm / methodology                            |
| metrics             | object    | Performance metrics (e.g., {r2: 0.92, rmse: 0.15}) |
| thumbnail\_url      | string    | Visualization thumbnail                            |
| created\_by         | string    | Author                                             |
| team\_id            | string    | Team identifier                                    |
| likes\_count        | int       | Number of likes                                    |
| comments\_count     | int       | Number of comments                                 |
| shares\_count       | int       | Number of shares                                   |
| linked\_dataset\_id | string    | Linked dataset ID                                  |
| zenodo\_doi         | string\[] | List of published DOIs                             |

---

## 5. Permissions

* **Read**: Public models visible to all users
* **Team-only models**: Restricted to team members
* **Manage links**: Only dataset owners / team admins can “Add / Unlink” models

---

## 6. Example User Flow

1. User opens a dataset detail page
2. Clicks the **Related Models** tab
3. Sees a list of connected models
4. Clicks a model card → goes to Model Detail page
5. If admin: can add or remove related models

