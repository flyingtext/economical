# Dataset Detail — Overview (Screen Definition)

## 1. Screen Purpose
The **Dataset Detail → Overview** page provides a high-level summary of a dataset.  
It includes workflow integration, usage statistics, and export features managed via modal dialogs.

---

## 2. Layout Components

### (A) Header
- **Dataset Title**
- **Short Description**
- **Tags / Keywords**
- **Access Scope**: Public / Team / Private
- **Owner / Team**: linked to profile
- **Last Updated Date**

**Action Buttons**
- [Use Now] → Modal to select Project/Model  
- [Export / Download] → Modal to configure export & delivery  
- [Favorite] ★  
- [Share]  

---

### (B) Overview Section
- Summary Description (purpose, context, domain)  
- Coverage (time span, geographic scope)  
- Size & Records (rows, columns, file size)  
- Source (short preview + link to Source & Citation tab)  

---

### (C) Usage & Statistics (Preview)
- Linked Models (count + quick list)  
- API Requests Volume (monthly / total, mini chart)  
- Downloads / Views count  

---

### (D) Community (Preview)
- Likes, Ratings, Comments (summary + “View All” → Community tab)  

---

### (E) Related Content
- Related Datasets  
- Related Models  

---

### (F) Footer
- Navigation Tabs → Overview | Schema | Source & Citation | Versions | Usage | Community | API Access | Publication History  

---

## 3. Modals

### (1) Use Now Modal
- **Title**: “Select Target for Dataset”  
- **Content**:  
  - Project List (user/team projects)  
  - Model List (available models)  
  - Search/Filter within modal  
- **Actions**:  
  - [Link Dataset]  
  - [Cancel]  

### (2) Export / Download Modal
- **Title**: “Export Dataset”  
- **Content**:  
  - Export Format: CSV / JSON / Parquet  
  - Range Options: Full dataset / Time window / Columns subset  
  - Delivery: Send to registered email  
- **Actions**:  
  - [Confirm Export] → background job triggered → confirmation toast  
  - [Cancel]  
- **Note**: Export job and status appear in **My Account → Exports & Backups**  

---

## 4. Key Features
1. **Quick Understanding**: dataset context, scope, and metadata  
2. **Workflow Integration**: [Use Now] modal links dataset to Projects/Models  
3. **Usage Transparency**: preview of API calls and model adoption  
4. **Community Preview**: likes, ratings, comments visible at a glance  
5. **Export with Logging**: export requests go through modal → results delivered via email → export history logged  

---

## 5. Navigation Flow
- From Dataset Catalog → [View Details] → lands here (Overview tab).  
- [Use Now] → modal → Project/Model selection.  
- [Export/Download] → modal → select format/range → email delivery.  
- Export history visible in **My Account → Exports & Backups**.  
