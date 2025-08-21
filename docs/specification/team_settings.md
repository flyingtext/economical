# 👥 Team Settings Page Specification (with Tabs)

## Purpose
Allow users to manage their team, invite members, assign roles, configure permissions, and monitor team-level resources.

---

## Layout

### Navigation
- **Top Bar**: [Economical Logo] + [Main Navigation]
- **Page Title**: "Team Settings"
- **Tab Navigation (horizontal or sidebar)**:
  - Overview
  - Members & Roles
  - Permissions
  - Usage & Credits
  - Backup & Export
  - Notifications

---

## Tabs

### 1. Overview Tab
- **Info Cards**
  - Team Name
  - Team ID
  - Owner (primary contact)
  - Creation Date
- **Actions**
  - Edit Team Profile (name, description, contact email)
  - Leave Team (for members)
  - Delete Team (for Owner only, with confirmation modal)

---

### 2. Members & Roles Tab
- **Member List Table**
  - Name
  - Email
  - Role (Viewer / Contributor / Owner / Admin)
  - Join Date
  - Status (Active / Pending Invite)
- **Actions**
  - Invite Member (email input → role assignment → send invite)
  - Remove Member
  - Change Role
- **Role Presets**
  - **Viewer** – Read-only, can only access public resources
  - **Contributor** – Regular user, can create and edit own resources, and contribute to team resources
  - **Owner** – Resource or team owner, can manage visibility, roles, and publication
  - **Admin** – Platform-wide privileges, can manage all users, teams, and resources

---

### 3. Permissions Tab
- **Fine-grained Role Matrix**
  - CRUD permissions for:
    - Models
    - Datasets
    - Showcases
    - Dashboards
  - Grid of checkboxes/toggles per role
- **Custom Roles (optional, extension)**
  - Allow creating role variants if needed
  - Assign role variant to members

---

### 4. Usage & Credits Tab
- **Resource Consumption**
  - Monthly usage summary (CPU hours, memory, storage, API calls)
- **Credit Balance**
  - Current team credits
  - Credit earning history (team contributions)
  - Credit spending history (simulations, dataset queries)
- **Charts**
  - Usage over time
  - Credit flow (earned vs spent)

---

### 5. Backup & Export Tab
- **Features**
  - Request full team export (models, datasets, dashboards)
  - Export status list (Pending / Completed)
  - Download links (expire after 24h)
- **Batch Job**
  - Notification sent to team Owner after export ready

---

### 6. Notifications Tab
- **Settings**
  - Email notifications for:
    - Dataset updates
    - Model runs completed
    - New comments/feedback
    - Credit usage alerts
  - In-app/WebSocket notification toggles
- **Delivery Preferences**
  - Per member override (each member chooses what they receive)

---

## Example Wireframe (Text-based)

```

---

| \[Economical Logo]        Team Settings           |                 |                             |          |            |   |
| ------------------------------------------------- | --------------- | --------------------------- | -------- | ---------- | - |
| Tabs: Overview                                    | Members & Roles | Permissions                 |          |            |   |
|                                                   | Usage & Credits | Backup & Export             | Noti     |            |   |
| ------------------------------------------------- |                 |                             |          |            |   |
| \[Active Tab Content]                             |                 |                             |          |            |   |
|                                                   |                 |                             |          |            |   |
| Example: Members & Roles Tab                      |                 |                             |          |            |   |
| -------------------------------------------       |                 |                             |          |            |   |
|                                                   | Name            | Email                       | Role     | Status     |   |
|                                                   | --------        | --------------              | -------- | ---------- |   |
|                                                   | Alice           | [a@ex.com](mailto:a@ex.com) | Admin    | Active     |   |
|                                                   | Bob             | [b@ex.com](mailto:b@ex.com) | Member   | Pending    |   |
| -------------------------------------------       |                 |                             |          |            |   |
| \[ Invite Member ] \[ Remove ] \[ Change Role ]   |                 |                             |          |            |   |

---

```

---

## Accessibility
- Tabs fully keyboard accessible
- ARIA roles for tab panels
- Inline error messages for invalid invites
- High contrast support

---

## Security
- Role changes restricted to Owner/Admin
- Team deletion requires password re-entry + confirmation modal
- Exports secured with time-limited links
- All invite tokens expire after 7 days
