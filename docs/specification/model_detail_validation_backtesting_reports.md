# Screen Definition: Model Detail – Validation / Backtesting Reports

This page displays the validation and backtesting outputs of a selected model.  
It is designed to help researchers assess model accuracy, reliability, and predictive power with detailed results, visualizations, and export features.

---

## 1. Page Header
- **Model Name** (title, linked to Model Overview)
- **Version Selector** (dropdown to switch between model versions)
- **Action Buttons**:
  - `Re-run Validation`
  - `Export Report (PDF / HTML / CSV)`
  - `Publish to Zenodo (DOI)`

---

## 2. Report Summary
- **Validation Method**: (e.g., k-fold CV, out-of-sample test, rolling window backtest)
- **Dataset Used**: (linked dataset(s))
- **Period / Range**: Training set vs validation set timeline
- **Execution Info**: Runtime, execution environment, compute credits used

---

## 3. Key Metrics
- **Statistical Metrics**
  - RMSE / MAE / MAPE
  - R² (coefficient of determination)
  - Log-likelihood, AIC / BIC
  - Sharpe ratio (for finance models)
- **Custom Metrics**
  - Domain-specific measures (user-defined KPIs)

- **Display**:  
  - Metric cards (highlight key values)  
  - Historical trend line for metrics across versions

---

## 4. Visualizations
- **Residuals Plot**: Actual vs Predicted scatter plot
- **Time-series Chart**: Model predictions vs observed values
- **Distribution Comparison**: Histograms of predicted vs actual
- **Scenario Simulation Results** (if applicable)
- **Error Heatmap**: Error patterns across parameters/time

---

## 5. Backtesting Logs
- **Execution History Table**  
  - Run ID  
  - Timestamp  
  - Dataset version used  
  - Parameters used  
  - Status (`Success`, `Failed`, `In Progress`)  
  - Duration  

- **Clickable Row → Run Detail Page** (expanded view)

---

## 6. Run Detail View (Expandable Section)
- **Parameters Used**: Initial conditions, constraints
- **Execution Environment**: Node / cluster info
- **Detailed Metrics**: Full breakdown
- **Plots & Interactive Charts**
- **Raw Outputs**: JSON export for reproducibility

---

## 7. Community & Collaboration
- **Comment Thread** (discussion on validation results)
- **Ratings / Endorsements**
- **Team Notes** (internal private notes)

---

## 8. Export & Publication
- **Export Options**
  - PDF report (with charts)
  - HTML interactive report
  - Raw CSV of metrics
- **Zenodo Publication Workflow**
  - Auto-generate `backtesting_report.html` package
  - DOI assignment and publication history tracking

---

## 9. Notifications
- Subscribe to:
  - Validation success/failure alerts
  - New backtesting results available
  - Comments/feedback on reports
