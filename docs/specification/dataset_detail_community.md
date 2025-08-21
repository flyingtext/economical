# Dataset Detail — Community (Screen Definition)

## 1. Screen Purpose
The **Community tab** provides a space for discussion, feedback, and evaluation of the dataset.  
It encourages collaboration and transparency by letting users comment, rate, and interact with others.

---

## 2. Layout Components

### (A) Header
- Dataset Title (link back to Overview)
- Current Tab: **Community**
- Action Buttons:
  - [Start Discussion] → opens modal to create a new thread
  - [Rate Dataset] → opens rating modal

---

### (B) Discussion Threads
- **Thread List**
  | Title                     | Author     | Replies | Last Activity |
  |---------------------------|------------|---------|---------------|
  | How reliable is CPI data? | user_123   | 4       | 2025-08-20    |
  | Suggestions for metadata  | team_admin | 2       | 2025-08-19    |

- Clicking a thread → expands full discussion view with nested comments

---

### (C) Comments
- Nested comment structure (replies indented)
- Each comment includes:
  - Author (linked to profile)
  - Timestamp
  - Content (text + markdown support)
  - Actions: 👍 Like, 💬 Reply, ⚑ Report
- Sorting: newest / most liked

---

### (D) Ratings & Likes
- **Ratings Panel**
  - Average rating (stars, 0–5)
  - Distribution chart (bar: how many users gave 1–5 stars)
- **Likes Panel**
  - Total likes
  - Recent likers (avatars)

---

### (E) Modals

#### (1) Start Discussion Modal
- Fields:
  - Title
  - Body (markdown supported)
- Actions:
  - [Post Thread]
  - [Cancel]

#### (2) Rating Modal
- Stars (1–5)
- Optional feedback text
- Actions:
  - [Submit Rating]
  - [Cancel]

---

## 3. Logging Rules
- All posts, comments, ratings, likes recorded in **Community Logs**
- Logs store:
  - resource_id (dataset)
  - action_type (post/comment/rating/like)
  - performed_by (user_id)
  - timestamp
- Admin/Owner can delete/flag inappropriate content

---

## 4. Key Features
1. **Discussion Threads**: topic-based conversations around dataset.  
2. **Nested Comments**: collaborative discussion.  
3. **Ratings System**: transparent quality evaluation.  
4. **Likes/Engagement**: quick interaction.  
5. **Moderation Tools**: report & admin deletion.  

---

## 5. Navigation Flow
- Dataset Detail → [Community tab]  
- User can:
  - View discussion threads
  - Post a new discussion
  - Comment and reply to others
  - Rate dataset and see distribution
  - Like or report content
