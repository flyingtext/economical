# Economical

![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square) ![Status](https://img.shields.io/badge/status-active-brightgreen.svg?style=flat-square) ![Python](https://img.shields.io/badge/python-3.11+-yellow.svg?style=flat-square) ![Maintainer](https://img.shields.io/badge/maintainer-JiHyeon%20Yoon-lightgrey.svg?style=flat-square) ![GitHub stars](https://img.shields.io/github/stars/flyingtext/economical?style=flat-square) ![Last commit](https://img.shields.io/github/last-commit/flyingtext/economical?style=flat-square) ![GitHub issues](https://img.shields.io/github/issues/flyingtext/economical?style=flat-square) ![GitHub closed issues](https://img.shields.io/github/issues-closed/flyingtext/economical?style=flat-square)

**Reproducible research in economic modeling, for all kinds of science.**

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

## 📄 Citation

*in development*

Once a stable release is published and DOI is issued via [Zenodo](https://zenodo.org/communities/economical), you may cite this project as follows:

**APA (7th edition):**

```
Yoon, J. (2025). Economical: An open-source platform for economic modeling and reproducible research (Version 1.0.0) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.xxxxxxx
```

```
Yoon, J. (2025). Economical: An open-source platform for economic and financial modeling, with reproducible research (Version 1.0.0) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.xxxxxxx
```

**MLA (9th edition):**

```
Yoon, JiHyeon. *Economical: An Open-Source Platform for Economic Modeling and Reproducible Research*. Version 1.0.0, 2025, Zenodo, https://doi.org/10.5281/zenodo.xxxxxxx.
```

```
Yoon, JiHyeon. *Economical: An Open-Source Platform for Economic and Financial Modeling, with Reproducible Research*. Version 1.0.0, 2025, Zenodo, https://doi.org/10.5281/zenodo.xxxxxxx.
```

**BibTeX:**

```bibtex
@software{yoon2025economical,
  author       = {Yoon, JiHyeon},
  title        = {Economical: An open-source platform for economic modeling and reproducible research},
  version      = {1.0.0},
  year         = {2025},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.xxxxxxx},
  url          = {https://doi.org/10.5281/zenodo.xxxxxxx}
}
```

```bibtex
@software{yoon2025economical_financial,
  author       = {Yoon, JiHyeon},
  title        = {Economical: An open-source platform for economic and financial modeling, with reproducible research},
  version      = {1.0.0},
  year         = {2025},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.xxxxxxx},
  url          = {https://doi.org/10.5281/zenodo.xxxxxxx}
}
```

---

## 🚧 Roadmap

* [ ] Stable release (v1.0.0)
* [ ] Zenodo DOI integration
* [ ] Extended model types (agent-based, PDE/ODE, etc.)
* [ ] Community features (stats, multilingual support)

---

## 🙏 Acknowledgements

* Inspired by open scientific communities such as **Zenodo** and **Kaggle**
* Documentation and design assisted by **OpenAI ChatGPT & Codex**
* Built with modern open-source tools: **Python, React, Tailwind, Flask/FastAPI**

---

## 💡 Funding & Sustainability

Economical is currently maintained as a **non-commercial community project**.
Future development may be supported via **grants, academic collaborations, or research funding**.

---

## 👤 Maintainer

**JiHyeon Yoon (윤지현)**

* ✉️ [somehowme@gmail.com](mailto:somehowme@gmail.com) / [flyingtext@nate.com](mailto:flyingtext@nate.com) / [flyingtext@hotmail.com](mailto:flyingtext@hotmail.com)
* 🌐 GitHub: [flyingtext](https://github.com/flyingtext)
* 📝 Blog: [j.writings.cloud](https://j.writings.cloud) / [k.writings.cloud](https://k.writings.cloud)
* 🧾 ORCID: [0000-0001-9610-0994](https://orcid.org/0000-0001-9610-0994)

**Development Notes**

* Project lead & system design by JiHyeon Yoon
* Built with: Python, React, Tailwind, Flask/FastAPI
* Assisted by: OpenAI ChatGPT & Codex (prompt-driven development support)
