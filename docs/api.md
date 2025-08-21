# API Reference (Extended)

This document lists the HTTP endpoints for the Economical backend.
Endpoints are grouped by feature area and reference the related specification
documents in `docs/specification`.

---

## Root

| Method | Path | Description          |
| ------ | ---- | -------------------- |
| GET    | `/`  | Service status check |

---

## Authentication

| Method    | Path                           | Description                  | Spec                                               |
| --------- | ------------------------------ | ---------------------------- | -------------------------------------------------- |
| GET, POST | `/auth/login`                  | User login                   | [login](specification/login.md)                    |
| GET, POST | `/auth/signup`                 | Create a new account         | [signup](specification/signup.md)                  |
| GET       | `/auth/check-email`            | Check if email is registered | [signup](specification/signup.md)                  |
| GET, POST | `/auth/password-reset`         | Request password reset email | [password\_reset](specification/password_reset.md) |
| GET, POST | `/auth/password-reset/<token>` | Reset password with token    | [password\_reset](specification/password_reset.md) |
| GET       | `/auth/password-reset/success` | Password reset success page  | [password\_reset](specification/password_reset.md) |

---

## My Account

| Method    | Path                                       | Description                 | Spec                                       |
| --------- | ------------------------------------------ | --------------------------- | ------------------------------------------ |
| GET, POST | `/my-account`                              | Personal dashboard          | [my\_account](specification/my_account.md) |
| POST      | `/my-account/session/<token>/revoke`       | Revoke active session       | [my\_account](specification/my_account.md) |
| GET, PUT  | `/my-account/preferences`                  | Manage personal preferences | [my\_account](specification/my_account.md) |
| GET       | `/my-account/exports`                      | List export/backup jobs     | [exports](specification/exports.md)        |
| POST      | `/my-account/exports`                      | Request new export/backup   | [exports](specification/exports.md)        |
| GET       | `/my-account/exports/<export_id>/download` | Download export file        | [exports](specification/exports.md)        |

---

## Team Settings

| Method           | Path                                   | Description                    | Spec                                             |
| ---------------- | -------------------------------------- | ------------------------------ | ------------------------------------------------ |
| GET, POST        | `/teams/`                              | Create or list teams           | [team\_settings](specification/team_settings.md) |
| GET, PUT, DELETE | `/teams/<team_id>`                     | Team detail & update           | [team\_settings](specification/team_settings.md) |
| POST             | `/teams/<team_id>/members`             | Add/remove/update team members | [team\_settings](specification/team_settings.md) |
| GET              | `/teams/<team_id>/resources`           | Resource & credits usage       | [team\_settings](specification/team_settings.md) |
| GET              | `/teams/<team_id>/publication-history` | Zenodo upload history          | [team\_settings](specification/team_settings.md) |
| GET              | `/teams/<team_id>/logs`                | Activity logs                  | [team\_settings](specification/team_settings.md) |

---

## Datasets

| Method | Path                             | Description                               | Spec                                                                  |
| ------ | -------------------------------- | ----------------------------------------- | --------------------------------------------------------------------- |
| GET    | `/datasets/`                     | List available datasets                   | [dataset\_catalog](specification/dataset_catalog.md)                  |
| POST   | `/datasets/`                     | Create new dataset                        | [dataset\_builder](specification/dataset_builder.md)                  |
| GET    | `/datasets/<dataset_id>`         | Dataset detail view                       | [dataset\_detail\_overview](specification/dataset_detail_overview.md) |
| PUT    | `/datasets/<dataset_id>`         | Update dataset                            | [dataset\_builder](specification/dataset_builder.md)                  |
| DELETE | `/datasets/<dataset_id>`         | Delete dataset                            | [dataset\_builder](specification/dataset_builder.md)                  |
| POST   | `/datasets/<dataset_id>/import`  | Upload/import data (CSV/JSON/API)         | [dataset\_builder](specification/dataset_builder.md)                  |
| POST   | `/datasets/<dataset_id>/ingest`  | Data ingestion (streaming/batch pipeline) | [dataset\_ingestion](specification/dataset_ingestion.md)              |
| POST   | `/datasets/<dataset_id>/publish` | Publish to Zenodo (DOI)                   | [dataset\_builder](specification/dataset_builder.md)                  |

---

## Data API

| Method | Path                                 | Description                      | Spec                                                        |
| ------ | ------------------------------------ | -------------------------------- | ----------------------------------------------------------- |
| GET    | `/api/data/<series_id>`              | Retrieve cached time series data | [dataset\_detail\_api](specification/dataset_detail_api.md) |
| GET    | `/v1/datasets/{dataset_id}/records`  | Fetch dataset records            | [dataset\_detail\_api](specification/dataset_detail_api.md) |
| GET    | `/v1/datasets/{dataset_id}/schema`   | Fetch dataset schema             | [dataset\_detail\_api](specification/dataset_detail_api.md) |
| GET    | `/v1/datasets/{dataset_id}/metadata` | Fetch dataset metadata           | [dataset\_detail\_api](specification/dataset_detail_api.md) |

---

## Models

| Method | Path                                    | Description                             | Spec                                                                                       |
| ------ | --------------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------ |
| GET    | `/models/`                              | List models (catalog)                   | [model\_catalog](specification/model_catalog.md)                                           |
| POST   | `/models/`                              | Create new model                        | [model\_builder](specification/model_builder.md)                                           |
| GET    | `/models/<model_id>`                    | Model detail view                       | [model\_detail](specification/model_detail.md)                                             |
| PUT    | `/models/<model_id>`                    | Update model                            | [model\_builder](specification/model_builder.md)                                           |
| DELETE | `/models/<model_id>`                    | Delete model                            | [model\_builder](specification/model_builder.md)                                           |
| POST   | `/models/<model_id>/fit`                | Run model fitting/solving               | [model\_builder](specification/model_builder.md)                                           |
| GET    | `/models/<model_id>/validation-reports` | Retrieve validation/backtesting reports | [model\_detail\_validation](specification/model_detail_validation.md)                      |
| POST   | `/models/<model_id>/schedules`          | Create prediction schedule              | [model\_detail\_prediction\_schedules](specification/model_detail_prediction_schedules.md) |
| GET    | `/models/<model_id>/schedules`          | List prediction schedules               | [model\_detail\_prediction\_schedules](specification/model_detail_prediction_schedules.md) |
| POST   | `/models/<model_id>/scenarios/compare`  | Compare scenarios                       | [model\_detail\_scenarios](specification/model_detail_scenarios.md)                        |
| POST   | `/models/<model_id>/publish`            | Publish to Zenodo (DOI)                 | [model\_builder](specification/model_builder.md)                                           |

---

## Projects

| Method | Path                             | Description             | Spec                                                 |
| ------ | -------------------------------- | ----------------------- | ---------------------------------------------------- |
| GET    | `/projects/`                     | List projects           | [project\_catalog](specification/project_catalog.md) |
| POST   | `/projects/`                     | Create new project      | [project\_builder](specification/project_builder.md) |
| GET    | `/projects/<project_id>`         | Project detail view     | [project\_detail](specification/project_detail.md)   |
| PUT    | `/projects/<project_id>`         | Update project          | [project\_builder](specification/project_builder.md) |
| DELETE | `/projects/<project_id>`         | Delete project          | [project\_builder](specification/project_builder.md) |
| GET    | `/projects/<project_id>/logs`    | Activity logs           | [project\_detail](specification/project_detail.md)   |
| POST   | `/projects/<project_id>/publish` | Publish to Zenodo (DOI) | [project\_builder](specification/project_builder.md) |

---

## Dashboards

| Method | Path                              | Description           | Spec                                                     |
| ------ | --------------------------------- | --------------------- | -------------------------------------------------------- |
| GET    | `/dashboards/`                    | List dashboards       | [dashboard\_catalog](specification/dashboard_catalog.md) |
| POST   | `/dashboards/`                    | Create new dashboard  | [dashboard\_builder](specification/dashboard_builder.md) |
| GET    | `/dashboards/<dashboard_id>`      | Dashboard detail view | [dashboard\_detail](specification/dashboard_detail.md)   |
| PUT    | `/dashboards/<dashboard_id>`      | Update dashboard      | [dashboard\_builder](specification/dashboard_builder.md) |
| DELETE | `/dashboards/<dashboard_id>`      | Delete dashboard      | [dashboard\_builder](specification/dashboard_builder.md) |
| GET    | `/dashboards/<dashboard_id>/logs` | Activity logs         | [dashboard\_detail](specification/dashboard_detail.md)   |

---

## GIS

| Method | Path                         | Description                    | Spec                        |
| ------ | ---------------------------- | ------------------------------ | --------------------------- |
| GET    | `/gis/explorer`              | Map explorer                   | [gis](specification/gis.md) |
| GET    | `/gis/datasets/<dataset_id>` | Visualize dataset on map       | [gis](specification/gis.md) |
| GET    | `/gis/models/<model_id>`     | Visualize model outputs on map | [gis](specification/gis.md) |
| GET    | `/gis/realtime/<locale>`     | Locale-based real-time view    | [gis](specification/gis.md) |

---

## Community

| Method | Path                                 | Description      | Spec                                    |
| ------ | ------------------------------------ | ---------------- | --------------------------------------- |
| GET    | `/community/`                        | Community feed   | [community](specification/community.md) |
| POST   | `/community/posts`                   | Create post      | [community](specification/community.md) |
| GET    | `/community/posts/<post_id>`         | View post detail | [community](specification/community.md) |
| DELETE | `/community/posts/<post_id>`         | Delete post      | [community](specification/community.md) |
| POST   | `/community/posts/<post_id>/comment` | Add comment      | [community](specification/community.md) |
| POST   | `/community/posts/<post_id>/like`    | Like a post      | [community](specification/community.md) |
| POST   | `/community/posts/<post_id>/share`   | Share a post     | [community](specification/community.md) |

---

## Notifications

| Method | Path                           | Description         | Spec                                            |
| ------ | ------------------------------ | ------------------- | ----------------------------------------------- |
| GET    | `/notifications/`              | Notification center | [notifications](specification/notifications.md) |
| GET    | `/notifications/alerts`        | Real-time alerts    | [notifications](specification/notifications.md) |
| GET    | `/notifications/subscriptions` | Subscription list   | [notifications](specification/notifications.md) |
| GET    | `/notifications/system`        | System messages     | [notifications](specification/notifications.md) |

---

## Admin

| Method | Path                      | Description                   | Spec                            |
| ------ | ------------------------- | ----------------------------- | ------------------------------- |
| GET    | `/admin/`                 | Admin dashboard               | [admin](specification/admin.md) |
| GET    | `/admin/users`            | User management               | [admin](specification/admin.md) |
| GET    | `/admin/teams`            | Team management               | [admin](specification/admin.md) |
| GET    | `/admin/datasets`         | Dataset management            | [admin](specification/admin.md) |
| GET    | `/admin/models`           | Model management              | [admin](specification/admin.md) |
| GET    | `/admin/projects`         | Project management            | [admin](specification/admin.md) |
| GET    | `/admin/dashboards`       | Dashboard management          | [admin](specification/admin.md) |
| GET    | `/admin/community`        | Community management          | [admin](specification/admin.md) |
| GET    | `/admin/publications`     | Zenodo publication management | [admin](specification/admin.md) |
| GET    | `/admin/system-logs`      | System logs                   | [admin](specification/admin.md) |
| GET    | `/admin/db-status`        | Database status               | [admin](specification/admin.md) |
| GET    | `/admin/resource-credits` | Resource credits management   | [admin](specification/admin.md) |
| GET    | `/admin/statistics`       | System statistics             | [admin](specification/admin.md) |
| GET    | `/admin/settings`         | System settings               | [admin](specification/admin.md) |

---

## Realtime (WebSocket API)

| Protocol | Path                        | Description                                   | Spec                                                   |
| -------- | --------------------------- | --------------------------------------------- | ------------------------------------------------------ |
| WS       | `/ws/notifications`         | Subscribe to real-time notifications          | [notifications](specification/notifications.md)        |
| WS       | `/ws/datasets/<dataset_id>` | Subscribe to dataset updates (record changes) | [dataset\_realtime](specification/dataset_realtime.md) |
| WS       | `/ws/models/<model_id>`     | Subscribe to model run/validation updates     | [model\_realtime](specification/model_realtime.md)     |
| WS       | `/ws/projects/<project_id>` | Subscribe to project activity events          | [project\_realtime](specification/project_realtime.md) |
