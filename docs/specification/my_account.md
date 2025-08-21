# ⚙️ My Account Page Specification (with Tabs)

## Purpose
Provide users with a centralized hub to manage their personal profile, security, preferences, data exports, and credit usage.

---

## Layout

### Navigation
- **Top Bar**: [Economical Logo] + [Main Navigation]
- **Page Title**: "My Account"
- **Tab Navigation (horizontal or sidebar)**:
  - Profile
  - Security
  - Preferences
  - Backup & Export
  - Credits & Usage

---

## Tabs

### 1. Profile Tab
- **Fields**
  - Full Name (editable)
  - Email (read-only, with verification badge)
  - Contact Info (phone, secondary email)
  - Profile Picture (upload/change)
- **Actions**
  - Save Changes
- **States**
  - Success banner: "Profile updated"
  - Error banner for invalid inputs

---

### 2. Security Tab
- **Sections**
  - Change Password
    - Current password, new password, confirm password
  - Active Sessions
    - List of sessions (device, location, last login)
    - "Logout from this device" / "Logout from all devices"
  - API Keys
    - List of keys (masked, last 4 chars visible)
    - Generate new key
    - Revoke existing key
  - Optional 2FA toggle (if enabled by system policy)
- **Security**
  - All sensitive actions require re-authentication

---

### 3. Preferences Tab
- **Options**
  - Language & Locale (dropdown)
  - Default Currency (USD, KRW, JPY, etc.)
  - Number Notation (1,000 vs 1.000 vs 1’000)
  - Notifications
    - Email notifications (on/off)
    - In-app/WebSocket notifications (toggle per category)
- **Actions**
  - Save Preferences

---

### 4. Backup & Export Tab
- **Features**
  - Export request (Models / Datasets / Showcases)
  - Status: Pending / Completed
  - Download links (expire after 24h)
  - Export history list (timestamp, type, status)
- **Process**
  - Export runs as batch job
  - User receives email with download link

---

### 5. Credits & Usage Tab
- **Overview**
  - Current Credit Balance
  - Monthly Usage Summary
- **History**
  - Contribution Credits (earned from dataset sharing, feedback, model publishing)
  - Spending Credits (model runs, dataset queries, API usage)
- **Charts**
  - Line graph of monthly balance
  - Table of detailed transactions

