# Zenodo Integration: Model Validation to DOI Publication

A platform feature that allows researchers to **upload model validation results directly to Zenodo** and obtain a DOI.  
This enables a seamless workflow from **model experimentation → backtesting → publication**.

---

## Workflow (User Flow)

1. **Model Validation Completed**
   - Perform fitting & solving on selected models (PDE/ODE, time series, agent-based, etc.)
   - Generate a backtesting report (including validation data)

2. **Automatic Template Generation**
   - The following file structure is generated automatically:
     ```
     /export/
       ├─ model_overview.md        # Model overview and mathematical description
       ├─ data.csv                 # Fitting & backtesting dataset
       ├─ fitting_results.json     # Estimated parameters and residual analysis
       ├─ backtesting_report.html  # Report with visualizations
     ```

3. **Click "Publish" Button**
   - Authenticate via Zenodo OAuth → link with the user’s Zenodo account
   - Upload the entire `/export/` directory as a deposition package

4. **Zenodo Upload & DOI Assignment**
   - Choose between Zenodo Sandbox or Production environment
   - Options: Public / Private / Embargo
   - After upload, DOI is immediately assigned → displayed on screen

5. **Result Verification**
   - DOI link can be inserted into the model results page or paper references  
   - Example: `doi:10.5281/zenodo.1234567`

---

## Technical Notes (For Developers)

- **Zenodo API**
  - Endpoint: `https://zenodo.org/api/deposit/depositions`
  - Auth: OAuth2 (Bearer Token)
- **Upload Process**
  - `POST` → create deposition
  - `PUT` → upload files
  - `POST` → publish request
- **Required Metadata**
  ```json
  {
    "metadata": {
      "title": "Backtesting Results of [Model Name]",
      "upload_type": "dataset",
      "description": "Automated model validation and backtesting report.",
      "creators": [{"name": "User Name", "affiliation": "Institution"}]
    }
  }
