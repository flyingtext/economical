# My Account — Screen Definition

## 1. Screen Purpose

The **My Account** section centralizes personal account management.
It provides access to user profile, security settings, preferences, export logs, and publication history.

---

## 2. Layout Components

### (A) Navigation Tabs

* Profile
* Security
* Preferences
* Exports & Backups
* Publication History

---

## 3. Sub-Screens

### 3.1 Profile
- **Profile Info**
  - Name
  - Email (primary, verified/unverified)
  - Affiliation / Institution
  - Role (Viewer / Contributor / Owner / Admin)
  - Profile Picture
  - ORCID iD (optional, format: `0000-0002-1825-0097`)
- **Actions**
  - [Edit Profile]  
  - [Change Picture]  
  - [Delete Account] (with warning modal)

---

### 3.2 Security

* **Authentication**

  * Change Password
  * Two-Factor Authentication (2FA) toggle (App/Email)
  * Recent Login History (device, IP, date)
* **Sessions**

  * List of active sessions
  * Option to revoke sessions

---

### 3.3 Preferences

* **UI Settings**

  * Language
  * Timezone
  * Theme (Light / Dark / Auto)
* **Notification Settings**

  * Email alerts
  * In-app notifications (datasets, models, community)
* **Data Preferences**

  * Default export format (CSV/JSON/Parquet)
  * Default chart display options

---

### 3.4 Exports & Backups

* **Purpose**: Track and manage dataset/model export requests.
* **Export History Table**

  * Export ID
  * Dataset / Model Name
  * Format (CSV / JSON / Parquet)
  * Range (full dataset, time window, subset)
  * Requested At (timestamp)
  * Status (Processing / Completed / Failed)
  * Delivery (email sent Y/N)
  * \[Download Link] (if completed, with expiration notice)
* **Backups**

  * Scheduled personal backups (if enabled)
  * Manual backup trigger \[Request Backup]
* **Actions**

  * Retry failed export
  * Cancel export (if still processing)

---

### 3.5 Publication History

* **Purpose**: List of Zenodo publications created by this user.
* **Table Fields**

  * DOI
  * Title
  * Linked Resource (Dataset / Model / Project)
  * Published At (timestamp)
  * Status (Published / Failed / Re-sync Pending)
  * \[View on Zenodo] link
* **Actions**

  * Retry sync (if DOI failed to register)
  * Export citation
* **Flow Integration**

  * On \[Publish to Zenodo] action (from Dataset/Model/Project Detail),
    if ORCID is registered in Profile → user is prompted:

    > “Do you also want to update this record to your ORCID profile?”

    * ✅ Yes → Zenodo metadata includes ORCID, push update to ORCID API
    * ❌ No → Only Zenodo DOI is created

---

## 4. Modals

### Profile Edit Modal

* Update name, affiliation, profile picture, ORCID iD

### Export Detail Modal

* Show full configuration of past export (format, range, delivery info)

### Backup Confirmation Modal

* Trigger manual backup → confirmation before job starts

### ORCID Confirmation Modal (during Publish flow)

* Prompt user if ORCID exists in profile:

  * “Do you also want to update this record to your ORCID profile?”
  * \[Yes] \[No]

---

## 5. Key Features

1. **Unified Account Control** — All personal settings centralized.
2. **Research Identity Integration** — ORCID iD stored in Profile, available for publications.
3. **Security & Transparency** — Passwords, 2FA, session control, login history.
4. **Customization** — Language, timezone, theme, and notification preferences.
5. **Export Management** — Track dataset/model exports, with logs and delivery status.
6. **Publication Tracking** — Personal Zenodo upload history, DOI references, optional ORCID push.

---

## 6. Navigation Flow

* Accessible from global header → \[My Account]
* Within My Account, user navigates via sub-tabs
* Export requests from Dataset/Model pages are logged here automatically
* Publications created through \[Publish to Zenodo] are tracked here automatically
* If ORCID is registered, user is prompted at publish time whether to also push update to ORCID
