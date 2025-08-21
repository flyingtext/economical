# Dataset Builder (Create / Edit)

Dataset Builder allows researchers to create, edit, and manage datasets with full versioning, schema definitions, and publication-ready exports.  

---

## 1. Basic Info
- **Name**: Dataset title (required)
- **Description**: Detailed description of dataset contents
- **Tags**: Comma-separated keywords for search/discovery
- **Visibility**: `Private` | `Team` | `Public`

---

## 2. Schema Definition
- **Columns** (add / edit / delete)
  - Column Name
  - Data Type (`string`, `number`, `boolean`, `date`, `geo`, etc.)
  - Units (optional)
  - Notes / Metadata
- **Schema Preview**: Live preview of schema structure

---

## 3. Source & Citation
- **BibTeX Input**: Paste citation in BibTeX format
- **URL Source**: External dataset source link
- **Upload Log**: Record of file sources with timestamps
- **Attribution Metadata**: License, copyright

---

## 4. Data Upload & Import
- **Direct Upload**  
  - Upload CSV / JSON files  
  - Drag & drop interface  
  - File validation & schema check  

- **API Binding**  
  - Connect external API endpoints  
  - Schedule periodic fetch (daily / weekly / monthly)  

- **Email Upload** ✉️  
  - Each dataset has a **unique email address** (auto-generated)  
  - Users can **send files as email attachments** → Automatically ingested  
  - System detects:  
    - **Attachments** (CSV, JSON)  
    - **Large file links** (Google Drive, Dropbox, S3, Zenodo, etc.)  
  - Email log stored in **Upload History**  

---

## 5. Versions & Update Management
- **Version Control**  
  - Create new dataset version on upload/change  
  - Track schema evolution across versions  
- **Update Logs**  
  - Timestamped records of all changes  
  - Diff view (compare versions)

---

## 6. Access Permissions
- **Role-based Access**
  - **Viewer** – read-only
  - **Contributor** – create and edit own datasets, and contribute to team datasets
  - **Owner** – manage visibility, roles, and publication
  - **Admin** – manage all datasets
- **Team Sharing**
  - Assign permissions per member / group
- **Public Access**
  - Enable/disable anonymous read-only API access

---

## 7. Save Draft / Publish
- **Save Draft**: Work-in-progress not visible outside creator/team  
- **Publish**: Finalized dataset visible according to chosen visibility  
- **Export Options**:  
  - JSON schema  
  - Zenodo-ready package (DOI publish workflow)  
