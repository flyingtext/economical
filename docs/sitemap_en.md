# 🌐 Economical Full Sitemap

## 1. Account
- Login / Logout
- Sign Up
- Password Reset
- My Account Settings
  - Profile (name, email, password, contact info)
  - Preferences (language, currency, number notation, notifications)
  - API Key Management
  - Backup & Export (models/datasets/showcases → batch → email link delivery)
  - Credit History
- Team Settings
  - Team Profile (name, description, owner)
  - Team Member Management (invite, assign role, remove)
  - Role Policies (CRUD permissions per model/dataset)
  - Team Credit History

---

## 2. Datasets
- Dataset Catalog
  - Search/Filter (domain, source, freshness, quality score)
  - Public vs Private datasets
- Dataset Detail Page
  - Metadata (source, freshness, missing rate, usage count, rating)
  - Preview (sample data viewer)
  - Feedback (likes, comments)
  - Subscribe / Notifications
  - API Access Guide
- Dataset Upload
  - Private dataset upload
  - Public visibility request (requires admin approval)
- Dataset Request
  - Request for new public dataset
  - Admin response/feedback

---

## 3. Models
- Model Catalog
  - Search/Filter (time series, PDE, ODE, agent-based, etc.)
  - Quality metrics (accuracy, citations, verification success rate)
- Model Detail Page
  - Description / Equations / Source code
  - Input/Output variable definitions
  - Showcase results (Validation vs Prediction)
  - Scenario Runner (compare scenario A vs B with different input vars)
  - Feedback (likes, comments, citations)
  - Subscribe / Notifications
  - API Access Guide
- Model Creation
  - Code Editor (Strict Python + restricted libs)
  - Resource limits (time/memory)
  - Dataset linking
- Model Pipeline
  - Graph Editor (connect model outputs → other model inputs)
  - Pipeline preview

---

## 4. Showcases
- Validation Showcase (backtesting results)
- Prediction Showcase (cron-based scheduled results)
  - Prediction Detail Page (history + visual comparisons)
- Scenario Comparison View (multi-panel graphs)
- Share Showcase (with users / add to dashboard)

---

## 5. Dashboards
- Personal Dashboard
  - My models/datasets/showcases as widgets
  - Real-time notifications widget
  - GIS view (geospatial data visualization)
- Team Dashboard
  - Team models/datasets/showcases as widgets
- Shared Dashboards
  - Browse other users’ dashboards
  - Bookmark/favorite dashboards

---

## 6. Community
- Dataset/Model ratings & comments
- Trending models / datasets ranking
- Contribution Ranking (credit-based)
- Discussion Board

---

## 7. Notifications
- Real-time notifications (via WebSocket)
  - Model execution completed
  - Dataset approval status
  - Team invitations
  - Credit changes
- Notification History Page

---

## 8. GIS (Geospatial)
- Map-based Dataset Explorer
  - View datasets by region
  - Filter & search
- GIS Model Visualization
  - Model outputs rendered as geospatial layers
- Internationalization
  - Locale-based unit conversions
  - Regional language display

---

## 9. Admin
- User Management
  - Accounts list / suspension / resource usage
- Team Management
  - Team profiles / members / credit adjustments
- Dataset Management
  - Approve/reject public dataset requests
  - Manage quality indicators
- Model Management
  - Approve/verify models
  - Monitor showcases
- Community Management
  - Moderate comments/feedback reports
- Credit Management
  - Automatic credit assignment policies
  - Manual adjustments
- Logs
  - Execution logs
  - API call logs
  - System alert logs
- DB/System Overview
  - System-wide statistics dashboard
  - Resource monitoring (CPU/GPU/memory)
