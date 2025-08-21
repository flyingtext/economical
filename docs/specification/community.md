# Community Screen Specification

## 1. Screen Name

**Community**

---

## 2. Purpose

* Provide a space for **researchers and teams to share, discuss, and collaborate**.
* Support **global feed**, **discussion threads**, and **personal/team activity tracking**.
* Lightweight alternative to external forums, integrated into the platform.

---

## 3. Layout

### A. Header

* **Title**: `Community`
* **Breadcrumb**: `Community`
* **Global Actions**:

  * \[Create Post]
  * \[Start Discussion]

### B. Tab Navigation

1. Global Feed
2. Discussions
3. My Activity

---

## 4. Tab Specifications

### 1) Global Feed

* **Purpose**: show all public posts and discussions across the platform.
* **Content List** (infinite scroll):

  * Post preview: title, snippet, author, timestamp
  * Metrics: likes, comments, shares
* **Actions**:

  * Like, Comment, Share, Bookmark
  * Click → open full post view

---

### 2) Discussions

* **Topic-based threads** (like forums)
* **Topic list view**:

  * Title, tags, last activity time, # of replies
* **Thread view**:

  * Original post at top
  * Nested replies (indentation)
  * Actions: reply, edit (if author), delete (if owner/admin)

---

### 3) My Activity

* **Personal Activity**

  * Posts created, comments made, likes, shares
* **Team Activity**

  * Posts/comments by team members
  * Visibility based on team membership
* **Filters**: personal / team, date range

---

## 5. States

* **Empty State**

  * Global Feed: “No posts yet.” with \[Create Post] button
  * Discussions: “No topics created yet.” with \[Start Discussion]
  * My Activity: “You haven’t posted anything yet.”
* **Loading State**: spinner with “Loading community activity…”
* **Error State**: “Failed to load content.”

---

## 6. Permissions

* Viewer: can only see **Public posts/discussions**
* Team Member: can see **Team activity** in My Activity tab
* Author: can edit/delete own posts
* Admin: full moderation rights

---

## 7. API Integration

* **Local DB**

  * `posts` (id, author\_id, team\_id, title, content, visibility, created\_at, updated\_at)
  * `discussions` (id, topic, tags, created\_by, created\_at, updated\_at)
  * `comments` (id, post\_id, author\_id, content, parent\_id, created\_at)
  * `likes` (post\_id, user\_id)
  * `shares` (post\_id, user\_id)
* **External**: none (all internal)

---

## 8. Example Wireframe (Text)

```
-------------------------------------------------
[ Community ]

Tabs: [Global Feed] [Discussions] [My Activity]

-------------------------------------------------
[Global Feed]

Post: "New Backtesting Report Template Released"
Author: J. Yoon | 12 likes | 5 comments | Aug 21
-------------------------------------------------
[Start Discussion] [Create Post]
-------------------------------------------------
```

