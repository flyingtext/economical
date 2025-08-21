# 📋 Sitemap ↔ ERD Column Mapping

## 1. Auth / Account

| Sitemap Item                            | ERD Table            | Columns                                                                          |
| --------------------------------------- | -------------------- | -------------------------------------------------------------------------------- |
| Profile                                 | USER / USER\_PROFILE | `name`, `email`, `affiliation`, `role`, `preferences_json`, `USER_PROFILE.orcid` |
| Security                                | USER                 | `password_hash`, (sessions via token store), `created_at`, `updated_at`          |
| Preferences                             | USER                 | `preferences_json`                                                               |
| Exports & Backups                       | USER\_EXPORT         | `export_type`, `file_path`, `created_at`                                         |
| Publication History (My Zenodo Uploads) | ZENODO\_PUBLICATION  | `doi`, `title`, `published_at`, `owner_id`, `owner_type=user`                    |

---

## 2. Team Settings

| Sitemap Item                              | ERD Table                                | Columns                                                       |
| ----------------------------------------- | ---------------------------------------- | ------------------------------------------------------------- |
| General Info                              | TEAM                                     | `name`, `description`, `created_at`                           |
| Members & Roles                           | TEAM\_MEMBER                             | `user_id`, `role`, `joined_at`                                |
| Resource Policies                         | TEAM\_POLICY                             | `policy_key`, `policy_value`                                  |
| Usage & Credits                           | TEAM\_EXPORT / (future RESOURCE\_CREDIT) | `export_type`, `file_path`, `created_at`                      |
| Exports & Backups                         | TEAM\_EXPORT                             | `export_type`, `file_path`, `created_at`                      |
| Publication History (Team Zenodo Uploads) | ZENODO\_PUBLICATION                      | `doi`, `title`, `published_at`, `owner_id`, `owner_type=team` |

---

## 3. Datasets

| Sitemap Item                      | ERD Table                    | Columns                                                                                   |
| --------------------------------- | ---------------------------- | ----------------------------------------------------------------------------------------- |
| Dataset Catalog                   | DATASET                      | `id`, `name`, `description`, `tags`, `visibility`, `owner_id`, `created_at`, `updated_at` |
| Basic Info                        | DATASET                      | `name`, `description`, `tags`, `visibility`                                               |
| Schema Definition                 | DATASET\_SCHEMA              | `column_name`, `data_type`, `unit`, `description`                                         |
| Source & Citation                 | DATASET\_SOURCE              | `citation_type`, `citation_value`, `metadata`, `added_at`                                 |
| Data Upload & Import              | DATASET\_VERSION             | `origin`, `version_tag`, `changelog`, `created_at`                                        |
| Versions & Update Management      | DATASET\_VERSION             | `version_tag`, `changelog`, `created_at`                                                  |
| Access Permissions                | (future DATASET\_PERMISSION) | (not yet in ERD, extendable)                                                              |
| Overview (Detail)                 | DATASET                      | `name`, `description`, `tags`, `visibility`, `owner_id`                                   |
| Usage & Statistics                | DATASET\_USAGE               | `views`, `downloads`, `api_calls`, `last_accessed`                                        |
| Community                         | POST/COMMENT/LIKE            | `target_type=dataset`                                                                     |
| API Access                        | DATASET (via API layer)      | `id`                                                                                      |
| Related Models                    | MODEL\_DATASET\_LINK         | `model_id`, `dataset_id`                                                                  |
| Publication History (Zenodo DOIs) | ZENODO\_PUBLICATION          | Linked via `owner_type=model` including dataset references                                |

---

## 4. Models

| Sitemap Item                      | ERD Table             | Columns                                                             |
| --------------------------------- | --------------------- | ------------------------------------------------------------------- |
| Model Catalog                     | MODEL                 | `id`, `name`, `description`, `model_type`, `owner_id`, `created_at` |
| Basic Info                        | MODEL                 | `name`, `description`, `model_type`                                 |
| Model Type & Structure            | MODEL                 | `model_type`                                                        |
| Linked Datasets                   | MODEL\_DATASET\_LINK  | `model_id`, `dataset_id`                                            |
| Parameters & Constraints          | MODEL\_PARAM          | `param_name`, `param_value`, `constraint`                           |
| Fitting & Solving Results         | MODEL\_RESULT         | `result_type`, `file_path`, `created_at`                            |
| Validation / Backtesting Reports  | MODEL\_VALIDATION     | `template_id`, `report_path`, `created_at`                          |
| Prediction Schedules              | MODEL\_PREDICTION     | `schedule`, `output_path`, `created_at`                             |
| Versions & Update Logs            | MODEL\_VERSION        | `version_tag`, `changelog`, `created_at`                            |
| Overview (Detail)                 | MODEL                 | `name`, `description`, `owner_id`                                   |
| Community                         | POST/COMMENT/LIKE     | `target_type=model`                                                 |
| API Access                        | MODEL (via API layer) | `id`                                                                |
| Related Datasets                  | MODEL\_DATASET\_LINK  | `dataset_id`                                                        |
| Publication History (Zenodo DOIs) | ZENODO\_PUBLICATION   | `doi`, `title`, `published_at`, `owner_type=model`                  |

---

## 5. Projects

| Sitemap Item                       | ERD Table              | Columns                                               |
| ---------------------------------- | ---------------------- | ----------------------------------------------------- |
| Project Catalog                    | PROJECT                | `id`, `name`, `description`, `owner_id`, `created_at` |
| Basic Info                         | PROJECT                | `name`, `description`, `owner_id`                     |
| Linked Models                      | PROJECT\_MODEL\_LINK   | `project_id`, `model_id`                              |
| Linked Datasets                    | PROJECT\_DATASET\_LINK | `project_id`, `dataset_id`                            |
| Team Members & Roles               | PROJECT\_MEMBER        | `user_id`, `role`                                     |
| Resource & Execution Settings      | PROJECT (extendable)   | `description`                                         |
| Validation / Publication Templates | PROJECT\_LOG           | `activity`                                            |
| Versions & Update Logs             | PROJECT\_LOG           | `activity`, `timestamp`                               |
| Overview (Detail)                  | PROJECT                | `name`, `description`, `owner_id`                     |
| Activity Logs                      | PROJECT\_LOG           | `activity`, `timestamp`                               |
| Publication History (Zenodo DOIs)  | ZENODO\_PUBLICATION    | `doi`, `title`, `owner_type=project`                  |

---

## 6. Dashboards

| Sitemap Item               | ERD Table               | Columns                                               |
| -------------------------- | ----------------------- | ----------------------------------------------------- |
| Dashboard Catalog          | DASHBOARD               | `id`, `name`, `description`, `owner_id`, `created_at` |
| Basic Info                 | DASHBOARD               | `name`, `description`                                 |
| Layout Editor              | DASHBOARD\_WIDGET       | `layout_json`                                         |
| Widgets                    | DASHBOARD\_WIDGET       | `widget_type`, `data_binding`                         |
| Data Binding               | DASHBOARD\_WIDGET       | `data_binding`                                        |
| Sharing & Permissions      | DASHBOARD (extendable)  | `owner_id`, `owner_type`                              |
| Overview (Detail)          | DASHBOARD               | `name`, `description`                                 |
| Layout View                | DASHBOARD\_WIDGET       | `layout_json`                                         |
| Widgets in Action          | DASHBOARD\_WIDGET       | `widget_type`, `data_binding`                         |
| Team & Sharing Permissions | DASHBOARD               | `owner_id`, `owner_type`                              |
| Activity Logs              | (future DASHBOARD\_LOG) | (not yet in ERD)                                      |

---

## 7. GIS

| Sitemap Item                 | ERD Table | Columns                                     |
| ---------------------------- | --------- | ------------------------------------------- |
| Map Explorer                 | MAP\_VIEW | `id`, `name`, `description`, `layer_config` |
| Dataset Visualization on Map | MAP\_VIEW | `layer_config`                              |
| Model Outputs Visualization  | MAP\_VIEW | `layer_config`                              |
| Locale-based Real-time View  | MAP\_VIEW | `layer_config`                              |

---

## 8. Community

| Sitemap Item                  | ERD Table         | Columns                         |
| ----------------------------- | ----------------- | ------------------------------- |
| Global Feed                   | POST              | `id`, `content`, `created_at`   |
| Discussions (threads, topics) | POST              | `type=discussion`, `content`    |
| Posts                         | POST              | `content`, `created_at`         |
| Comments                      | COMMENT           | `content`, `created_at`         |
| Likes                         | LIKE              | `user_id`, `created_at`         |
| My Community Activity         | POST/COMMENT/LIKE | filtered by `author_id=user_id` |

---

## 9. Admin

| Sitemap Item            | ERD Table                           | Columns                        |
| ----------------------- | ----------------------------------- | ------------------------------ |
| User Management         | USER                                | `id`, `name`, `email`, `role`  |
| Team Management         | TEAM                                | `id`, `name`, `description`    |
| Dataset Management      | DATASET                             | `id`, `name`, `visibility`     |
| Model Management        | MODEL                               | `id`, `name`, `model_type`     |
| Project Management      | PROJECT                             | `id`, `name`, `description`    |
| Dashboard Management    | DASHBOARD                           | `id`, `name`                   |
| Community Management    | POST / COMMENT / LIKE               | `content`                      |
| Zenodo Publication Mgmt | ZENODO\_PUBLICATION                 | `doi`, `title`, `published_at` |
| System Logs             | PROJECT\_LOG / (future SYSTEM\_LOG) | `activity`, `timestamp`        |
| Database Status         | (infra only)                        | —                              |
| Resource Credits        | TEAM\_POLICY / TEAM\_EXPORT         | `policy_key`, `policy_value`   |
| Contribution Tracking   | (future)                            | —                              |
| System Statistics       | aggregate over all tables           | —                              |
| Settings                | —                                   | config table                   |

---

## 10. Notifications

| Sitemap Item     | ERD Table    | Columns                                    |
| ---------------- | ------------ | ------------------------------------------ |
| Real-time Alerts | NOTIFICATION | `message`, `type`, `is_read`, `created_at` |
| Subscriptions    | SUBSCRIPTION | `target_type`, `target_id`                 |
| System Messages  | NOTIFICATION | `message`, `type`                          |

