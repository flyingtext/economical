# Roles Matrix

## 1. Roles Defined

* **Viewer** – Read-only, can only access **public resources**.
* **Contributor** – Regular user, can **create and edit own resources**, and contribute to team resources.
* **Owner** – Resource or team owner, can **manage visibility, roles, and publication**.
* **Admin** – Platform-wide privileges, can manage **all users, teams, and resources**.

---

## 2. Role Permissions by Section

### Auth / Account

| Feature                                     | Viewer | Contributor | Owner        | Admin   |
| ------------------------------------------- | ------ | ----------- | ------------ | ------- |
| Login / Signup / Reset Password             | ✅      | ✅           | ✅            | ✅       |
| My Account (Profile, Security, Preferences) | –      | ✅ (own)     | ✅ (own)      | ✅ (all) |
| Exports & Backups                           | –      | ✅ (own)     | ✅ (own/team) | ✅ (all) |
| Publication History (Zenodo uploads)        | –      | ✅ (own)     | ✅ (own/team) | ✅ (all) |

---

### Team Settings

| Feature                           | Viewer | Contributor   | Owner | Admin |
| --------------------------------- | ------ | ------------- | ----- | ----- |
| View team info                    | –      | ✅             | ✅     | ✅     |
| Edit team settings                | –      | –             | ✅     | ✅     |
| Manage members & roles            | –      | –             | ✅     | ✅     |
| Resource policies, usage, credits | –      | –             | ✅     | ✅     |
| Exports & backups                 | –      | –             | ✅     | ✅     |
| Team publication history          | –      | ✅ (view only) | ✅     | ✅     |

---

### Datasets

| Feature                                                                         | Viewer          | Contributor         | Owner                | Admin   |
| ------------------------------------------------------------------------------- | --------------- | ------------------- | -------------------- | ------- |
| Dataset Catalog                                                                 | ✅ (public only) | ✅ (own/team/public) | ✅ (all owned)        | ✅ (all) |
| Dataset Builder (create/edit)                                                   | –               | ✅ (own/team)        | ✅ (own/team)         | ✅       |
| Dataset Detail (overview, schema, source, versions, usage, API, related models) | ✅ (public only) | ✅ (own/team/public) | ✅ (all owned)        | ✅       |
| Community (comments, posts)                                                     | ✅ (public)      | ✅ (all joined)      | ✅                    | ✅       |
| Publication History (Zenodo DOIs)                                               | –               | ✅ (view/export own) | ✅ (team/publication) | ✅ (all) |

---

### Models

| Feature                                                                                       | Viewer          | Contributor         | Owner                | Admin   |
| --------------------------------------------------------------------------------------------- | --------------- | ------------------- | -------------------- | ------- |
| Model Catalog                                                                                 | ✅ (public only) | ✅ (own/team/public) | ✅ (all owned)        | ✅ (all) |
| Model Builder (create/edit)                                                                   | –               | ✅ (own/team)        | ✅ (own/team)         | ✅       |
| Model Detail (overview, results, validation, predictions, scenarios, versions, API, datasets) | ✅ (public only) | ✅ (own/team/public) | ✅ (all owned)        | ✅       |
| Community (comments, posts)                                                                   | ✅ (public)      | ✅ (all joined)      | ✅                    | ✅       |
| Publication History (Zenodo DOIs)                                                             | –               | ✅ (own export)      | ✅ (team/publication) | ✅ (all) |

---

### Projects

| Feature                                                                        | Viewer          | Contributor         | Owner                | Admin   |
| ------------------------------------------------------------------------------ | --------------- | ------------------- | -------------------- | ------- |
| Project Catalog                                                                | ✅ (public only) | ✅ (own/team/public) | ✅ (all owned)        | ✅ (all) |
| Project Builder (create/edit)                                                  | –               | ✅ (own/team)        | ✅ (own/team)         | ✅       |
| Project Detail (overview, linked models/datasets, members, logs, publications) | ✅ (public only) | ✅ (own/team/public) | ✅ (all owned)        | ✅       |
| Publication History (Zenodo DOIs)                                              | –               | ✅ (own export)      | ✅ (team/publication) | ✅ (all) |

---

### Dashboards

| Feature                                                         | Viewer          | Contributor         | Owner         | Admin   |
| --------------------------------------------------------------- | --------------- | ------------------- | ------------- | ------- |
| Dashboard Catalog                                               | ✅ (public only) | ✅ (own/team/public) | ✅ (all owned) | ✅ (all) |
| Dashboard Builder (create/edit)                                 | –               | ✅ (own/team)        | ✅ (own/team)  | ✅       |
| Dashboard Detail (overview, layout, widgets, permissions, logs) | ✅ (public only) | ✅ (own/team/public) | ✅ (all owned) | ✅       |

---

### GIS

| Feature                     | Viewer                  | Contributor                | Owner                           | Admin   |
| --------------------------- | ----------------------- | -------------------------- | ------------------------------- | ------- |
| GIS Explorer (map view)     | ✅ (public only)         | ✅ (own/team/public layers) | ✅ (own/team layers, save/share) | ✅ (all) |
| Dataset Visualization       | ✅ (public only)         | ✅ (own/team/public)        | ✅ (all owned)                   | ✅       |
| Model Outputs Visualization | ✅ (public only)         | ✅ (own/team/public)        | ✅ (all owned)                   | ✅       |
| Real-time Locale View       | ✅ (public public feeds) | ✅ (own/team/public)        | ✅ (manage feeds)                | ✅       |

---

### Community

| Feature                                          | Viewer   | Contributor         | Owner                 | Admin            |
| ------------------------------------------------ | -------- | ------------------- | --------------------- | ---------------- |
| Global Feed                                      | ✅        | ✅                   | ✅                     | ✅                |
| Discussions (threads, replies)                   | ✅ (read) | ✅ (post/reply)      | ✅ (moderate own/team) | ✅ (moderate all) |
| Posts (create/edit/delete, comment, like, share) | –        | ✅ (own/team/public) | ✅ (manage own/team)   | ✅ (manage all)   |
| My Activity                                      | –        | ✅                   | ✅                     | ✅                |

---

### Admin

| Feature                                                   | Viewer | Contributor | Owner | Admin |
| --------------------------------------------------------- | ------ | ----------- | ----- | ----- |
| User Management                                           | –      | –           | –     | ✅     |
| Team Management                                           | –      | –           | –     | ✅     |
| Dataset/Model/Project/Dashboard Management                | –      | –           | –     | ✅     |
| Community Management                                      | –      | –           | –     | ✅     |
| Zenodo Publication Management                             | –      | –           | –     | ✅     |
| System Logs                                               | –      | –           | –     | ✅     |
| Database Status                                           | –      | –           | –     | ✅     |
| Resource Credits (auto assignment, contribution tracking) | –      | –           | –     | ✅     |
| System Statistics                                         | –      | –           | –     | ✅     |
| Settings (system-wide)                                    | –      | –           | –     | ✅     |

---

### Notifications

| Feature          | Viewer     | Contributor | Owner        | Admin                |
| ---------------- | ---------- | ----------- | ------------ | -------------------- |
| Real-time Alerts | –          | ✅ (own)     | ✅ (own/team) | ✅ (all)              |
| Subscriptions    | –          | ✅ (own)     | ✅ (own/team) | ✅ (all)              |
| System Messages  | ✅ (public) | ✅           | ✅            | ✅ (create/broadcast) |

