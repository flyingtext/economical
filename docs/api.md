# API Reference

This document lists the current HTTP endpoints for the Economical backend. The
endpoints are grouped by feature area and reference the related specification
documents in `docs/specification`.

## Root

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Service status check |

## Authentication

| Method | Path | Description | Spec |
|--------|------|-------------|------|
| GET, POST | `/auth/login` | User login | [login](specification/login.md) |
| GET, POST | `/auth/signup` | Create a new account | [signup](specification/signup.md) |
| GET | `/auth/check-email` | Check if an email is already registered | [signup](specification/signup.md) |
| GET, POST | `/auth/password-reset` | Request password reset email | [password_reset](specification/password_reset.md) |
| GET, POST | `/auth/password-reset/<token>` | Reset password using token | [password_reset](specification/password_reset.md) |
| GET | `/auth/password-reset/success` | Password reset success page | [password_reset](specification/password_reset.md) |

## Data API

| Method | Path | Description | Spec |
|--------|------|-------------|------|
| GET | `/api/data/<series_id>` | Retrieve cached time series data | [dataset_detail_api](specification/dataset_detail_api.md) |
| GET | `https://api.economical.click/v1/datasets/{dataset_id}/records` | Fetch dataset records | [dataset_detail_api](specification/dataset_detail_api.md) |
| GET | `https://api.economical.click/v1/datasets/{dataset_id}/schema` | Fetch dataset schema | [dataset_detail_api](specification/dataset_detail_api.md) |
| GET | `https://api.economical.click/v1/datasets/{dataset_id}/metadata` | Fetch dataset metadata | [dataset_detail_api](specification/dataset_detail_api.md) |

## Datasets

| Method | Path | Description | Spec |
|--------|------|-------------|------|
| GET | `/datasets/` | List available datasets | [dataset_catalog](specification/dataset_catalog.md) |
| GET | `/datasets/<dataset_id>` | Show dataset details | [dataset_detail_overview](specification/dataset_detail_overview.md) |

## Projects

| Method | Path | Description | Spec |
|--------|------|-------------|------|
| GET | `/projects/` | List projects | [project_catalog](specification/project_catalog.md) |
| GET | `/projects/<project_id>` | Project detail view | [project_detail](specification/project_detail.md) |

## Dashboards

| Method | Path | Description | Spec |
|--------|------|-------------|------|
| GET | `/dashboards/` | Dashboard catalog | [dashboard_catalog](specification/dashboard_catalog.md) |
| GET | `/dashboards/<dashboard_id>` | Dashboard detail | [dashboard_detail](specification/dashboard_detail.md) |

## Community

| Method | Path | Description | Spec |
|--------|------|-------------|------|
| GET | `/community/` | Community landing page | [community](specification/community.md) |

## Categories

| Method | Path | Description |
|--------|------|-------------|
| GET | `/categories/` | Root categories listing |
| GET | `/categories/<path:subpath>` | Nested category listing |

## Model Builder

| Method | Path | Description | Spec |
|--------|------|-------------|------|
| GET | `/model/` | Display model building form | [model_builder](specification/model_builder.md) |
| POST | `/model/` | Run model fitting pipeline | [model_builder](specification/model_builder.md) |

## My Account

| Method | Path | Description | Spec |
|--------|------|-------------|------|
| GET, POST | `/my-account` | Personal dashboard and updates | [my_account](specification/my_account.md) |
| GET, POST | `/my-account/` | Personal dashboard (trailing slash) | [my_account](specification/my_account.md) |
| POST | `/my-account/session/<token>/revoke` | Revoke active session | [my_account](specification/my_account.md) |

## Notifications

| Method | Path | Description | Spec |
|--------|------|-------------|------|
| GET | `/notifications/` | Notification center | [notifications](specification/notifications.md) |

## Admin

| Method | Path | Description | Spec |
|--------|------|-------------|------|
| GET | `/admin/` | Admin dashboard | [admin](specification/admin.md) |
