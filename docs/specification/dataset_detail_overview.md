# Dataset Detail — Overview (Screen Definition)

## 1. Screen Purpose
The **Overview tab** of Dataset Detail provides a high-level summary of the dataset.  
It helps users quickly understand what the dataset contains, how it is used, and perform key actions such as linking to workflows or exporting.

---

## 2. Layout Components

### (A) Header
- Dataset Title  
- Short Description  
- Tags / Keywords  
- Access Scope: Public / Team / Private  
- Owner / Team (linked to profile)  
- Last Updated Date  

**Action Buttons**
- [Use Now] → opens Use Now Modal  
- [Export / Download] → opens Export Modal  
- [Favorite] ★  
- [Share]  

---

### (B) Overview Section
- **Summary**: purpose, context, research domain  
- **Coverage**: time span (e.g., 1990–2024), geographic coverage  
- **Size & Records**: rows, columns, file size  
- **Source Preview**: citation snippet or DOI (link to Source & Citation tab)

---

### (C) Usage & Statistics (Preview)
- Linked Models: count + quick list (e.g., “Used in 5 Models”)  
- API Requests Volume: recent 30 days / total (mini chart or number)  
- Downloads / Views count  

---

### (D) Community (Preview)
- Likes, Ratings, Comments summary  
- “View All” → links to Community tab  

---

### (E) Related Content
- Related Datasets  
- Related Models  

---

## 3. Modals

### (1) Use Now Modal
- **Title**: “Select Target for Dataset”  
- **Content**:  
  - Project List (user/team projects)  
  - Model List (available models)  
  - Search/Filter inside modal  
- **Actions**:  
  - [Link Dataset]  
  - [Cancel]  

---

### (2) Export / Download Modal
- **Title**: “Export Dataset”  
- **Fields**:  
  - Format: CSV / JSON / Parquet  
  - Range: Full dataset / Time window / Columns subset  
  - Export As:  
    - 🔘 Personal (My Account)  
    - 🔘 Team (Team Settings, if user has permission)  
- **Delivery**:  
  - Send to registered email (optionally secondary email if allowed)  
- **Actions**:  
  - [Confirm Export] → creates export job + logs it  
  - [Cancel]  

---

## 4. Logging Rules
- **If Export As = Personal** → log stored in *My Account → Exports & Backups*  
- **If Export As = Team** → log stored in *Team Settings → Exports & Backups*  
- Log contains: Export ID, resource, ownership_type, requested_by, format, range, status, delivery_email, timestamp  

---

## 5. Key Features
1. High-level dataset context: summary, coverage, size, source.  
2. Quick usage insight: linked models, API requests, downloads/views.  
3. Workflow integration: Use Now modal → link to Project/Model.  
4. Export control: Export modal → select format, range, ownership (personal/team).  
5. Transparency: Export job always logged, status visible in account/team logs.  

---

## 6. Navigation Flow
- Dataset Catalog → [View Details] → lands here (Overview tab).  
- [Use Now] → Use Now Modal → link dataset to workflow.  
- [Export / Download] → Export Modal → confirm → log created in appropriate account.  
