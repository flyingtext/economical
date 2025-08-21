# My Account — Screen Definition

## 1. Screen Purpose
The **My Account** section centralizes personal account management.  
It provides access to user profile, security settings, preferences, export logs, and publication history.  

---

## 2. Layout Components

### (A) Navigation Tabs
- Profile  
- Security  
- Preferences  
- Exports & Backups  
- Publication History  

---

## 3. Sub-Screens

### 3.1 Profile
- **Profile Info**
  - Name
  - Email (primary, verified/unverified)
  - Affiliation / Institution
  - Role (User / Researcher / Admin, etc.)
  - Profile Picture
- **Actions**
  - [Edit Profile]  
  - [Change Picture]  
  - [Delete Account] (with warning modal)

---

### 3.2 Security
- **Authentication**
  - Change Password  
  - Two-Factor Authentication (2FA) toggle (App/Email)  
  - Recent Login History (device, IP, date)  
- **Sessions**
  - List of active sessions  
  - Option to revoke sessions  

---

### 3.3 Preferences
- **UI Settings**
  - Language  
  - Timezone  
  - Theme (Light / Dark / Auto)  
- **Notification Settings**
  - Email alerts  
  - In-app notifications (datasets, models, community)  
- **Data Preferences**
  - Default export format (CSV/JSON/Parquet)  
  - Default chart display options  

---

### 3.4 Exports & Backups
- **Purpose**: Track and manage dataset/model export requests.  
- **Export History Table**
  - Export ID  
  - Dataset / Model Name  
  - Format (CSV / JSON / Parquet)  
  - Range (full dataset, time window, subset)  
  - Requested At (timestamp)  
  - Status (Processing / Completed / Failed)  
  - Delivery (email sent Y/N)  
  - [Download Link] (if completed, with expiration notice)
- **Backups**
  - Scheduled personal backups (if enabled)  
  - Manual backup trigger [Request Backup]  
- **Actions**
  - Retry failed export  
  - Cancel export (if still processing)  

---

### 3.5 Publication History
- **Purpose**: List of Zenodo publications created by this user.  
- **Table Fields**
  - DOI  
  - Title  
  - Linked Resource (Dataset / Model / Project)  
  - Published At (timestamp)  
  - Status (Published / Failed / Re-sync Pending)  
  - [View on Zenodo] link  
- **Actions**
  - Retry sync (if DOI failed to register)  
  - Export citation  

---

## 4. Modals

### Profile Edit Modal
- Update name, affiliation, profile picture  

### Export Detail Modal
- Show full configuration of past export (format, range, delivery info)  

### Backup Confirmation Modal
- Trigger manual backup → confirmation before job starts  

---

## 5. Key Features
1. **Unified Account Control** — All personal settings centralized.  
2. **Security & Transparency** — Passwords, 2FA, session control, login history.  
3. **Customization** — Language, timezone, theme, and notification preferences.  
4. **Export Management** — Track dataset/model exports, with logs and delivery status.  
5. **Publication Tracking** — Personal Zenodo upload history, sync status, DOI references.  

---

## 6. Navigation Flow
- Accessible from global header → [My Account]  
- Within My Account, user navigates via sub-tabs  
- Export requests from Dataset/Model pages are logged here automatically  
- Publications created through [Publish to Zenodo] are tracked here automatically  
