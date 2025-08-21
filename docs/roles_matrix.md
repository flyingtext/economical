# Role Matrix — Screen Definition

## 1. Roles
- **Owner**: Resource creator (personal or team)  
- **Admin**: Team administrator, has elevated control over team-owned resources  
- **Contributor**: Team member with rights to add/use resources, limited management  
- **Viewer**: Read-only access to resources  

---

## 2. Auth / Account
| Function                  | Owner | Admin | Contributor | Viewer |
|----------------------------|-------|-------|-------------|--------|
| View / Edit Profile        | ✅    | -     | -           | -      |
| Security Settings          | ✅    | -     | -           | -      |
| Preferences                | ✅    | -     | -           | -      |
| View Export Logs (Personal)| ✅    | -     | -           | -      |
| View Export Logs (Team)    | -     | ✅    | ✅ (own)    | ❌     |
| View Publication History   | ✅    | ✅    | ✅          | ❌     |

---

## 3. Team Settings
| Function                           | Owner | Admin | Contributor | Viewer |
|-----------------------------------|-------|-------|-------------|--------|
| Edit General Info                 | ✅    | ✅    | ❌          | ❌     |
| Manage Members & Roles            | ✅    | ✅    | ❌          | ❌     |
| Invite / Remove Members           | ✅    | ✅    | ❌          | ❌     |
| Edit Resource Policies            | ✅    | ✅    | ❌          | ❌     |
| View Usage & Credits              | ✅    | ✅    | ✅          | ✅     |
| Purchase Credits                  | ✅    | ✅    | ❌          | ❌     |
| View Export Logs                  | ✅    | ✅    | ✅ (own)    | ❌     |
| Retry/Cancel Exports              | ✅    | ✅    | ❌          | ❌     |
| View Publication History          | ✅    | ✅    | ✅          | ❌     |
| Retry DOI Sync (Zenodo)           | ✅    | ✅    | ❌          | ❌     |

---

## 4. Datasets
| Function                           | Owner | Admin | Contributor | Viewer |
|-----------------------------------|-------|-------|-------------|--------|
| View Overview / Schema / Source   | ✅    | ✅    | ✅          | ✅     |
| View Versions / Usage / Community | ✅    | ✅    | ✅          | ✅     |
| View API Access / Publications    | ✅    | ✅    | ✅          | ✅     |
| **Use Now (link dataset)**        | ✅    | ✅    | ✅          | ❌     |
| **Export (Personal)**             | ✅    | ❌    | ❌          | ❌     |
| **Export (Team)**                 | ✅    | ✅    | ⭕ (policy) | ❌     |
| Edit Metadata                     | ✅    | ✅    | ❌          | ❌     |
| Delete Dataset                    | ✅    | ✅    | ❌          | ❌     |

---

## 5. Models
| Function                           | Owner | Admin | Contributor | Viewer |
|-----------------------------------|-------|-------|-------------|--------|
| View Overview / Results / Reports | ✅    | ✅    | ✅          | ✅     |
| View Scenarios / Versions         | ✅    | ✅    | ✅          | ✅     |
| Link Dataset                      | ✅    | ✅    | ✅          | ❌     |
| Run Validation / Backtesting      | ✅    | ✅    | ✅          | ❌     |
| Schedule Predictions              | ✅    | ✅    | ✅          | ❌     |
| Export Results                    | ✅    | ✅    | ⭕ (policy) | ❌     |
| Edit Model Metadata               | ✅    | ✅    | ❌          | ❌     |
| Delete Model                      | ✅    | ✅    | ❌          | ❌     |

---

## 6. Projects
| Function                           | Owner | Admin | Contributor | Viewer |
|-----------------------------------|-------|-------|-------------|--------|
| View Project Overview             | ✅    | ✅    | ✅          | ✅     |
| Link Models / Datasets            | ✅    | ✅    | ✅          | ❌     |
| View Activity Logs                | ✅    | ✅    | ✅          | ✅     |
| Export Project Reports            | ✅    | ✅    | ⭕ (policy) | ❌     |
| Edit Project Info                 | ✅    | ✅    | ❌          | ❌     |
| Delete Project                    | ✅    | ✅    | ❌          | ❌     |

---

## 7. Dashboards
| Function                           | Owner | Admin | Contributor | Viewer |
|-----------------------------------|-------|-------|-------------|--------|
| View Dashboard                    | ✅    | ✅    | ✅          | ✅     |
| Edit Layout & Widgets             | ✅    | ✅    | ✅          | ❌     |
| Share Dashboard                   | ✅    | ✅    | ✅          | ❌     |
| Manage Permissions                | ✅    | ✅    | ❌          | ❌     |

---

## 8. Community
| Function                           | Owner | Admin | Contributor | Viewer |
|-----------------------------------|-------|-------|-------------|--------|
| View Global Feed / Discussions    | ✅    | ✅    | ✅          | ✅     |
| Post / Comment / Like             | ✅    | ✅    | ✅          | ❌     |
| Rate Dataset / Model              | ✅    | ✅    | ✅          | ❌     |
| Moderate (delete posts/comments)  | -     | ✅    | ❌          | ❌     |

---

## 9. Admin (Platform-wide)
| Function                           | Owner | Admin | Contributor | Viewer |
|-----------------------------------|-------|-------|-------------|--------|
| User Management                   | -     | ✅    | ❌          | ❌     |
| Team Management                   | -     | ✅    | ❌          | ❌     |
| Dataset Management                | -     | ✅    | ❌          | ❌     |
| Model Management                  | -     | ✅    | ❌          | ❌     |
| Community Management              | -     | ✅    | ❌          | ❌     |
| Zenodo Publication Management     | -     | ✅    | ❌          | ❌     |
| View System Logs                  | -     | ✅    | ❌          | ❌     |
| Database Status                    | -     | ✅    | ❌          | ❌     |
| Manage Resource Credits           | -     | ✅    | ❌          | ❌     |
| View System Statistics            | -     | ✅    | ❌          | ❌     |
| Change System Settings            | -     | ✅    | ❌          | ❌     |

---

## 10. Notifications
| Function                           | Owner | Admin | Contributor | Viewer |
|-----------------------------------|-------|-------|-------------|--------|
| View Real-time Alerts             | ✅    | ✅    | ✅          | ✅     |
| Manage Subscriptions              | ✅    | ✅    | ✅          | ❌     |
| Receive System Messages           | ✅    | ✅    | ✅          | ✅     |
