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
  - Current Role: **Owner / Admin / Member / Viewer** (read-only, inherited from team settings)
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
- **Notes**
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

---

## Example Wireframe (Text-based)

```

---

| \[Economical Logo]        My Account                        |                 |             |        |
| ----------------------------------------------------------- | --------------- | ----------- | ------ |
| Tabs: Profile                                               | Security        | Preferences | Backup |
| & Export                                                    | Credits & Usage |             |        |
| -------------------------------------------------           |                 |             |        |
| \[Active Tab Content]                                       |                 |             |        |
|                                                             |                 |             |        |
| Example: Profile Tab                                        |                 |             |        |
| Name:  \[\_\_\_\_\_\_\_\_\_\_\_]                            |                 |             |        |
| Email: [user@email.com](mailto:user@email.com) (✓ Verified) |                 |             |        |
| Phone: \[\_\_\_\_\_\_\_\_\_\_\_]                            |                 |             |        |
| Picture: \[Upload]                                          |                 |             |        |
| Role: Member (Read-only)                                    |                 |             |        |
| \[ Save Changes ]                                           |                 |             |        |

---

```

---

## Accessibility
- Tabs navigable via keyboard
- Clear ARIA roles for tab panels
- Screen reader announces active tab
- High-contrast friendly design

---

## Security
- All updates via HTTPS
- Password/API key updates require re-authentication
- Export/download links expire after 24h
- Sensitive data never shown in plain text
