# Notifications Screen Specification

## 1. Screen Name

**Notifications**

---

## 2. Purpose

* Central hub for all platform notifications.
* Provide **real-time alerts**, **subscription updates**, and **system messages**.
* Support filtering, read/unread states, and management of notification preferences.

---

## 3. Layout

### A. Header

* **Title**: `Notifications`
* **Breadcrumb**: `Notifications`
* **Global Actions**:

  * \[Mark All as Read]
  * \[Notification Settings]

### B. Tab Navigation

1. Real-time Alerts
2. Subscriptions
3. System Messages

---

## 4. Tab Specifications

### 1) Real-time Alerts

* **Purpose**: immediate user-specific notifications.
* Examples:

  * Model execution finished
  * Dataset updated by collaborator
  * Team member mentioned you in a post
* **List View**:

  * Icon (type of alert), title, timestamp, status (new/read)
* Actions: \[Mark as Read], \[Open Resource]

---

### 2) Subscriptions

* **Purpose**: notifications from **followed datasets, models, projects, users, or teams**.
* **List View**:

  * Subscription type (Dataset/Model/Project/User)
  * Latest activity (new version, new comment, publication)
  * Timestamp
* Actions: \[Unsubscribe], \[Open Resource]

---

### 3) System Messages

* **Purpose**: platform-wide or admin-originated notifications.
* Examples:

  * Scheduled maintenance
  * Policy updates
  * Credit usage thresholds
* **List View**:

  * Message title, content preview, timestamp
* Actions: \[Acknowledge], \[Open Details]

---

## 5. States

* **Empty State**:

  * “You have no notifications.”
* **Loading State**: spinner with “Fetching notifications…”
* **Error State**: “Failed to load notifications.”

---

## 6. Permissions

* All users can see **their own alerts, subscriptions, and system messages**.
* Admins can broadcast system messages.

---

## 7. API Integration

* **Local DB**:

  * `notifications` (id, user\_id, type, content, resource\_id, status, created\_at)
  * `subscriptions` (id, user\_id, resource\_type, resource\_id, created\_at)
  * `system_messages` (id, title, content, created\_at, priority)
* **External**:

  * WebSocket/Push API for real-time delivery

---

## 8. Example Wireframe (Text)

```
-------------------------------------------------
[ Notifications ]

Tabs: [Real-time Alerts] [Subscriptions] [System Messages]

-------------------------------------------------
[Real-time Alerts]

⚡ Model run completed - "GDP Forecast v2"
   2 minutes ago  [Mark as Read] [Open]

📦 Dataset updated - "Energy Data v5"
   10 minutes ago  [Mark as Read] [Open]
-------------------------------------------------
```

