# ⚙️ My Account Settings Page Specification

## Purpose
Allow individual users to configure their personal profile, preferences, security options, and data exports within Economical.

---

## Layout

### 1. Profile
- Display fields:
  - Full Name (editable text input)
  - Email (read-only, verified status shown)
  - Contact Info (phone number, secondary email, optional)
  - Profile Picture (upload/change)
- Actions:
  - "Save Changes" button

### 2. Security
- Password Management:
  - Change password (current password + new password + confirm)
- Session Management:
  - List of active sessions (device, location, last login time)
  - "Logout from all other sessions" button
- 2FA (optional, toggle if enabled in system settings)
- API Keys:
  - List API keys
  - Generate new API key
  - Revoke key

### 3. Preferences
- Language & Locale:
  - Interface language
  - Default region (for GIS visualization)
- Number & Currency:
  - Currency display unit (USD, KRW, JPY, etc.)
  - Number notation (1,000 vs 1.000 vs 1’000)
- Notifications:
  - Email notification toggle (on/off)
  - In-app/WebSocket notification preferences

### 4. Backup & Export
- Data Export (batch job with email delivery)
  - Models (all created models)
  - Datasets (uploaded or linked datasets)
  - Showcases (validation & prediction reports)
- "Request Export" button → status (Pending / Completed)
- Past Export History with download links

### 5. Credit Usage
- Credit balance overview
- Credit earning history (contribution, feedback, dataset sharing, etc.)
- Credit spending history (model runs, dataset queries, API usage)
- Monthly usage summary

---

## States
- **Default**
  - Editable fields pre-filled with current values
- **Validation Error**
  - Invalid phone number, invalid file format for profile picture, etc.
- **Success**
  - Banner: "Settings updated successfully."
- **Failure**
  - Banner: "Could not update settings. Please try again."

---

## Security
- Password changes require current password
- API keys shown only once at creation (afterwards only last 4 chars)
- Export links expire after 24h
- All settings updated over HTTPS

---

## Accessibility
- Keyboard navigation supported
- Screen reader labels for all fields
- Toggle switches accessible
- High-contrast friendly

