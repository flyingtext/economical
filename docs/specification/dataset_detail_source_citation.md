# Dataset Detail — Source & Citation (Screen Definition)

## 1. Screen Purpose
The **Source & Citation tab** provides metadata about where the dataset originates, how it should be cited, and when/why updates occurred.  
It ensures transparency, reproducibility, and proper academic attribution.

---

## 2. Layout Components

### (A) Header
- Dataset Title (link back to Overview)
- Current Tab: **Source & Citation**
- Action Buttons:
  - [Copy Citation] → copies current citation format
  - [Export Metadata] → modal to export BibTeX/JSON schema

---

### (B) Source Information
- **Primary Source**  
  - Name of institution/author  
  - Link (URL / DOI)  
  - Access date  
- **Secondary Sources** (if dataset aggregates multiple origins)  
  - List view with name, URL/DOI, contributor  

---

### (C) Citation Formats
- **BibTeX** (pre-generated block)  
- **APA / MLA / Chicago** (dropdown to switch formats)  
- [Copy] button for each format  

---

### (D) Source Update Logs
| Date       | Action            | Performed By | Notes/Change |
|------------|------------------|--------------|--------------|
| 2025-08-10 | Added new source | user_123     | Added OECD GDP 2023 |
| 2025-08-15 | Modified citation| admin_team   | DOI updated to v2 |

- Sortable by date
- Shows CRUD history of source entries

---

### (E) Export Metadata Modal
- **Title**: “Export Source & Citation Metadata”
- Fields:
  - Format: BibTeX / JSON / XML
  - Delivery:  
    - Download immediately  
    - Send to registered email (logs entry to Exports & Backups)
- Actions:
  - [Confirm Export]
  - [Cancel]

---

## 3. Logging Rules
- If **Send to Email** selected → export job logged in My Account or Team Settings depending on ownership  
- If **Download Immediately** → lightweight log (download count) in Usage & Statistics only  

---

## 4. Key Features
1. **Transparency**: show all data sources with DOI/URL references.  
2. **Academic Integrity**: ready-to-use citation blocks in multiple formats.  
3. **Traceability**: update logs show who added/modified source entries.  
4. **Export Options**: citation metadata exportable in multiple formats.  
5. **Integration with Logs**: exports logged consistently with account/team ownership.  

---

## 5. Navigation Flow
- Dataset Detail → [Source & Citation tab]  
- User can:
  - View primary/secondary sources  
  - Copy citations in desired format  
  - Check update logs (who/when/what)  
  - Export citation metadata via modal  
