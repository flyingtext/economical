# Dataset Detail — API Access (Screen Definition)

## 1. Screen Purpose
The **API Access tab** provides programmatic access details for the dataset.  
It includes authentication info, endpoint documentation, example queries, and usage limits to support integration into external workflows.

---

## 2. Layout Components

### (A) Header
- Dataset Title (link back to Overview)
- Current Tab: **API Access**
- Action Buttons:
  - [Copy Endpoint URL]
  - [Generate API Token] → modal (if allowed)

---

### (B) Endpoint Information
- Base URL: `https://api.economical.click/v1/datasets/{dataset_id}`
- Endpoints:
  - `/records` → fetch dataset records
  - `/schema` → fetch dataset schema
  - `/metadata` → fetch metadata (source, versions, etc.)
- Parameters:
  - `limit`, `offset` for pagination
  - `columns` for selecting fields
  - `filters` for conditional queries
- Response format: JSON (default), CSV (optional via header)

---

### (C) Authentication
- API Key / Token required for private/team datasets
- Public datasets may allow unauthenticated access with rate limits
- User-specific tokens generated under My Account → Security
- Team tokens managed under Team Settings → Resource Policies

---

### (D) Example Requests
- **cURL**
  ```bash
  curl -H "Authorization: Bearer <token>" \
       "https://api.economical.click/v1/datasets/ds_123/records?limit=10"
````

* **Python**

  ```python
  import requests
  url = "https://api.economical.click/v1/datasets/ds_123/records?limit=10"
  headers = {"Authorization": "Bearer <token>"}
  data = requests.get(url, headers=headers).json()
  ```
* **R**

  ```R
  library(httr)
  GET("https://api.economical.click/v1/datasets/ds_123/records?limit=10",
      add_headers(Authorization = "Bearer <token>"))
  ```

---

### (E) Rate Limits & Quotas

* Free tier: 1,000 requests / month
* Team tier: 100,000 requests / month (shared across team)
* Admin tier: configurable
* Status panel:

  * Requests used this month
  * Remaining quota
  * Reset date

---

### (F) API Token Modal

* **Title**: “Generate API Token”
* Fields:

  * Token name (optional)
  * Expiry date (optional)
* Actions:

  * \[Generate Token]
  * \[Cancel]
* Generated token shown once with \[Copy] button

---

## 3. Logging Rules

* API requests logged per user/team:

  * dataset\_id
  * endpoint called
  * requestor (user\_id or team\_id)
  * timestamp
* API token generation logged under My Account → Security or Team Settings → Resource Policies
* Usage aggregated and displayed in **Usage & Statistics tab**

---

## 4. Key Features

1. **Clear API Endpoints**: ready-to-use docs with parameters.
2. **Auth Management**: personal & team tokens.
3. **Practical Examples**: cURL, Python, R snippets.
4. **Rate Limit Transparency**: quota usage panel.
5. **Export Integration**: logs and quota linked to Usage & Statistics.

---

## 5. Navigation Flow

* Dataset Detail → \[API Access tab]
* User can:

  * Copy endpoint URL
  * Generate personal/team token (if permitted)
  * Test example queries
  * Monitor quota usage
