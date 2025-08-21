# Role Matrix (Full, v2)

## Legend
- ✅ Allowed
- ❌ Not allowed
- 🔒 Restricted (context-specific, e.g. own-only)

---

## 1. User & Team
| Action                          | Owner | Admin | Contributor | Viewer | Guest |
|---------------------------------|-------|-------|-------------|--------|-------|
| Create Team                     | ✅    | ❌    | ❌           | ❌     | ❌    |
| Invite / Remove Members         | ✅    | ✅    | ❌           | ❌     | ❌    |
| Assign Roles                    | ✅    | ✅    | ❌           | ❌     | ❌    |
| Edit Team Settings              | ✅    | ✅    | ❌           | ❌     | ❌    |
| View Team Settings              | ✅    | ✅    | ✅           | ✅     | ❌    |
| View Team Usage & Credits       | ✅    | ✅    | ✅           | ✅     | ❌    |
| Request Export / Backup         | ✅    | ✅    | ✅           | ❌     | ❌    |

---

## 2. Datasets
| Action                          | Owner | Admin | Contributor | Viewer | Guest |
|---------------------------------|-------|-------|-------------|--------|-------|
| Upload / Ingest Dataset         | ✅    | ✅    | ✅           | ❌     | ❌    |
| Edit Metadata / Schema          | ✅    | ✅    | ✅           | ❌     | ❌    |
| Delete Dataset                  | ✅    | ✅    | ❌           | ❌     | ❌    |
| View Dataset Catalog            | ✅    | ✅    | ✅           | ✅     | ✅    |
| Download Dataset                | ✅    | ✅    | ✅           | ✅     | ❌    |
| View Source / Citation          | ✅    | ✅    | ✅           | ✅     | ✅    |
| View Usage & Stats              | ✅    | ✅    | ✅           | ✅     | ❌    |
| Comment / Like                  | ✅    | ✅    | ✅           | ✅     | ❌    |
| Zenodo Upload (Dataset Export)  | ✅    | ✅    | ✅           | ❌     | ❌    |
| View Dataset Publication History| ✅    | ✅    | ✅           | ✅     | ❌    |

---

## 3. Models
| Action                          | Owner | Admin | Contributor | Viewer | Guest |
|---------------------------------|-------|-------|-------------|--------|-------|
| Create Model                    | ✅    | ✅    | ✅           | ❌     | ❌    |
| Edit Model Parameters           | ✅    | ✅    | ✅           | ❌     | ❌    |
| Delete Model                    | ✅    | ✅    | ❌           | ❌     | ❌    |
| Run Fitting / Solving           | ✅    | ✅    | ✅           | ❌     | ❌    |
| Run Prediction (cron jobs)      | ✅    | ✅    | ✅           | ❌     | ❌    |
| View Model Catalog              | ✅    | ✅    | ✅           | ✅     | ✅    |
| View Model Results              | ✅    | ✅    | ✅           | ✅     | ✅    |
| Scenario Comparison             | ✅    | ✅    | ✅           | ❌     | ❌    |
| Comment / Like                  | ✅    | ✅    | ✅           | ✅     | ❌    |
| Zenodo Upload (Model Report)    | ✅    | ✅    | ✅           | ❌     | ❌    |
| View Model Publication History  | ✅    | ✅    | ✅           | ✅     | ❌    |

---

## 4. Projects
| Action                          | Owner | Admin | Contributor | Viewer | Guest |
|---------------------------------|-------|-------|-------------|--------|-------|
| Create Project                  | ✅    | ✅    | ✅           | ❌     | ❌    |
| Edit Project                    | ✅    | ✅    | ✅           | ❌     | ❌    |
| Delete Project                  | ✅    | ✅    | ❌           | ❌     | ❌    |
| Link Models / Datasets          | ✅    | ✅    | ✅           | ❌     | ❌    |
| View Project Detail             | ✅    | ✅    | ✅           | ✅     | ❌    |
| Comment / Like                  | ✅    | ✅    | ✅           | ✅     | ❌    |
| Zenodo Upload (Project Export)  | ✅    | ✅    | ✅           | ❌     | ❌    |
| View Project Publication History| ✅    | ✅    | ✅           | ✅     | ❌    |

---

## 5. Dashboards
| Action                          | Owner | Admin | Contributor | Viewer | Guest |
|---------------------------------|-------|-------|-------------|--------|-------|
| Create Dashboard                | ✅    | ✅    | ✅           | ❌     | ❌    |
| Edit Dashboard Widgets          | ✅    | ✅    | ✅           | ❌     | ❌    |
| Delete Dashboard                | ✅    | ✅    | ❌           | ❌     | ❌    |
| Share Dashboard                 | ✅    | ✅    | ✅           | ❌     | ❌    |
| View Dashboards                 | ✅    | ✅    | ✅           | ✅     | ✅    |
| Comment / Like                  | ✅    | ✅    | ✅           | ✅     | ❌    |

---

## 6. Community
| Action                          | Owner | Admin | Contributor | Viewer | Guest |
|---------------------------------|-------|-------|-------------|--------|-------|
| Create Post / Thread            | ✅    | ✅    | ✅           | ❌     | ❌    |
| Comment                         | ✅    | ✅    | ✅           | ✅     | ❌    |
| Like / Upvote                   | ✅    | ✅    | ✅           | ✅     | ❌    |
| Edit Own Post                   | ✅    | ✅    | ✅           | ❌     | ❌    |
| Delete Own Post                 | ✅    | ✅    | ✅           | ❌     | ❌    |
| Moderate Community (delete any) | ✅    | ✅    | ❌           | ❌     | ❌    |
| View Community Feed             | ✅    | ✅    | ✅           | ✅     | ✅    |

---

## 7. Zenodo Publication (All Resources)
| Action                          | Owner | Admin | Contributor | Viewer | Guest |
|---------------------------------|-------|-------|-------------|--------|-------|
| Trigger Upload (Dataset/Model/Project)| ✅ | ✅ | ✅           | ❌     | ❌    |
| View Own Upload History         | ✅    | ✅    | ✅           | ✅     | ❌    |
| View Team Upload History        | ✅    | ✅    | ✅           | ❌     | ❌    |
| Retry Failed Upload             | ✅    | ✅    | 🔒 (own only)| ❌     | ❌    |
| Delete Upload Record (local)    | ✅    | ✅    | ❌           | ❌     | ❌    |
| Manage Zenodo Credentials       | ✅    | ✅    | ❌           | ❌     | ❌    |
| Admin Oversight (all uploads)   | ✅    | ✅    | ❌           | ❌     | ❌    |

---

## 8. Admin
| Action                          | Owner | Admin | Contributor | Viewer | Guest |
|---------------------------------|-------|-------|-------------|--------|-------|
| Manage Users / Teams            | ✅    | ✅    | ❌           | ❌     | ❌    |
| Manage Datasets                 | ✅    | ✅    | ❌           | ❌     | ❌    |
| Manage Models                   | ✅    | ✅    | ❌           | ❌     | ❌    |
| Manage Community                | ✅    | ✅    | ❌           | ❌     | ❌    |
| Manage Zenodo Publications      | ✅    | ✅    | ❌           | ❌     | ❌    |
| View System Logs                | ✅    | ✅    | ❌           | ❌     | ❌    |
| View Database Status            | ✅    | ✅    | ❌           | ❌     | ❌    |
| Manage Credits / Contributions  | ✅    | ✅    | ❌           | ❌     | ❌    |
| View System Statistics          | ✅    | ✅    | ❌           | ❌     | ❌    |
| Configure System Settings       | ✅    | ✅    | ❌           | ❌     | ❌    |
