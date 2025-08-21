# Economical

**Economical** is an open-source research platform for building, validating, and publishing **economic and financial models**.
It provides an end-to-end workflow from **model fitting & solving → backtesting → publication to Zenodo (DOI issued)**, with dataset management and collaborative features.

[GitHub Repository](https://github.com/flyingtext/economical)
[Zenodo Community](https://zenodo.org/communities/economical)

---

## ✨ Key Features

### 1. Models

* **Model Builder**

  * Create, edit, and manage models (PDE/ODE, time-series, agent-based, etc.)
  * Define parameters, equations, and simulation settings
  * Backtesting with customizable templates
  * Prediction scheduling and validation reports

* **Model Detail Pages**

  * Overview / Equations / Parameters
  * Validation & Backtesting Reports
  * Prediction Schedules
  * Export & Publish (Zenodo integration)

---

### 2. Datasets

* **Dataset Builder**

  * Define schema (columns, types, units)
  * Manage sources & citations (BibTeX, URL, upload log)
  * Import data (CSV, JSON, API binding)
  * Version control & update logs
  * Access permissions & visibility

* **Dataset Detail Pages**

  * Overview
  * Schema
  * Source & Citation

---

### 3. Publication Workflow (Zenodo Integration)

* Directly publish **model results** and **datasets** to [Zenodo](https://zenodo.org/)
* DOI automatically assigned for reproducible research
* Auto-generated export package:

  ```
  /export/
    ├─ model_overview.md        # Model description & equations
    ├─ data.csv                 # Dataset used for fitting/backtesting
    ├─ fitting_results.json     # Parameters & residual analysis
    ├─ backtesting_report.html  # Visualization report
  ```

---

### 4. Team & Collaboration

* Individual and team workspaces
* Role-based permissions (Contributor, Maintainer, Admin)
* Team settings: members, policies, usage & credits
* Export & backup history
* Publication history (personal/team Zenodo uploads)

---

### 5. Community & Wiki

* Public catalog of models and datasets
* Wiki integration: [Spacetime](https://spacetime.click)
* Structured citations & external link monitoring
* Automatic language toggle (EN/KR/JP)
* Document statistics (views, trends)

---

## 🗂 Sitemap (Simplified)

```text
1. Auth / Account
   - Login / Signup / My Account (profile, preferences, Zenodo uploads)

2. Team Settings
   - Members & Roles / Usage & Credits / Publication history

3. Models
   - Model Catalog / Builder / Detail (overview, validation, schedules)

4. Datasets
   - Dataset Catalog / Builder / Detail (schema, sources, versions)

5. Community
   - Public Models & Datasets
   - Wiki & Documentation
```

---

## 🛠 Tech Stack

* **Frontend**: React, Tailwind, shadcn/ui
* **Backend**: Python (Flask/FastAPI), SQLite/PostgreSQL
* **Visualization**: Deck.gl / Leaflet, Recharts, D3.js
* **Integration**: Zenodo API, GitHub Actions for automation
* **Search & Indexing**: Full-text search + citation monitoring

---

## 📦 Installation

```bash
git clone https://github.com/flyingtext/economical.git
cd economical
pip install -r requirements.txt
```

Run local server:

```bash
python run.py
```

---

## 🔗 Zenodo Community

All published models and datasets are curated at:
👉 [https://zenodo.org/communities/economical](https://zenodo.org/communities/economical)

Curation policy: submissions exported via `economical.click` are **reviewed before inclusion**.

---

## 📜 License

MIT License.
See [LICENSE](./LICENSE) for details.

---

## 🤝 Contributing

We welcome contributions! Please check:

* [roles\_matrix.md](./docs/roles_matrix.md) for role definitions
* [model\_builder.md](./docs/model_builder.md) and [dataset\_builder.md](./docs/dataset_builder.md) for specifications

---

## 👤 Maintainer

**JiHyeon Yoon (윤지현)**

* ✉️ Email: [somehowme@gmail.com](mailto:somehowme@gmail.com) / [flyingtext@nate.com](mailto:flyingtext@nate.com) / [flyingtext@hotmail.com](mailto:flyingtext@hotmail.com)
* 🌐 GitHub: [flyingtext](https://github.com/flyingtext)
* 📝 Blog: [j.writings.cloud](https://j.writings.cloud) / [k.writings.cloud](https://k.writings.cloud)
* 🧾 ORCID: [0000-0001-9610-0994](https://orcid.org/0000-0001-9610-0994)

