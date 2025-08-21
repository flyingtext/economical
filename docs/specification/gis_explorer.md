# GIS Explorer Screen Specification

## 1. Screen Name

**GIS Explorer**

---

## 2. Purpose

* Provide an interactive **map-based environment** for visualizing datasets and model outputs.
* Built on **Leaflet.js** with plugins (heatmaps, clustering, time dimension).
* Enable filtering, styling, layer toggling, and **real-time locale visualization**.
* Support saving and sharing map views inside the platform.

---

## 3. Layout

### A. Header

* **Title**: `GIS Explorer`
* **Breadcrumb**: `GIS > Explorer`
* **Global Actions**:

  * \[Add Layer] (Dataset or Model Output)
  * \[Save View]
  * \[Share View]

### B. Main Map View

* **Leaflet Map Canvas**

  * Base map: OpenStreetMap (default)
  * Layers: multiple datasets/models stacked
  * Interactivity: zoom, pan, hover tooltips, marker popups, polygon highlight

### C. Sidebar Panels

* **Layers Panel (Left)**

  * List of active layers
  * Actions: \[Toggle Visibility], \[Change Style], \[Remove]
  * Reorder layers (drag & drop)
* **Inspector Panel (Right)**

  * Layer-specific settings
  * Data binding: choose dataset/model fields for lat/lon, values
  * Style options: marker type, color scale, opacity, clustering
  * Filter options: date range, categories, thresholds

---

## 4. Tab Navigation

1. **Dataset Visualization**
2. **Model Outputs Visualization**
3. **Locale-based Real-time View**

---

## 5. Tab Specifications

### 1) Dataset Visualization

* **Add Dataset Layer**

  * Choose dataset from catalog
  * Select schema fields for latitude & longitude
  * Visualization types: markers, choropleth polygons, heatmaps
* **Inspector options**

  * Marker style (icon, color, size)
  * Choropleth color scale (gradient, categorical palette)
  * Heatmap intensity settings
  * Filters: date/time, category values

---

### 2) Model Outputs Visualization

* **Add Model Output Layer**

  * Select model + output fields with coordinates
  * Bind predictions/forecasts to map
* **Inspector options**

  * Time slider (via Leaflet.TimeDimension plugin)
  * Animation controls (play/pause, speed)
  * Comparison mode: overlay two or more model outputs
  * Style options: color scale, marker size

---

### 3) Locale-based Real-time View

* **Real-time streaming support**

  * Connect via WebSocket or polling API
  * Render new events as markers or heatmap updates
* **Options**

  * Time window: last 5 min, 1h, 24h
  * Auto-expire old points (fade or drop)
  * Clustering toggle for high-density feeds
  * Alert thresholds: highlight markers if values exceed conditions

---

## 6. States

* **Empty State**:

  * “No layers added yet.”
  * Show \[Add Layer] prominently
* **Loading State**:

  * Spinner overlay on map
* **Error State**:

  * “Layer failed to load.” with retry option

---

## 7. Permissions

* Viewer: can see only **public map views**
* Team Member: can add team datasets/models as layers
* Owner: full control, can save/share
* Admin: manage all saved views

---

## 8. API Integration

* **Local DB**

  * `gis_views` (id, name, owner\_id, layers JSON, created\_at, updated\_at)
  * `gis_layers` (view\_id, dataset\_id/model\_id, config JSON)
* **External**

  * Map tiles: OSM / Mapbox
  * Leaflet plugins:

    * `Leaflet.markercluster` for clustering
    * `Leaflet.heat` for heatmaps
    * `Leaflet.TimeDimension` for temporal data
  * Streaming API for real-time updates

---

## 9. Example Wireframe (Text)

```
-------------------------------------------------
[ GIS Explorer ]

Tabs: [Dataset Visualization] [Model Outputs] [Real-time Locale]

-------------------------------------------------
(Map View: Leaflet.js)

Layers Panel (Left):
 - GDP by Region (Choropleth) [visible]
 - Population Density (Heatmap) [visible]
 - Forecast Demand 2030 (Markers) [hidden]

Inspector Panel (Right):
 - Selected Layer: Population Density
 - Style: Heatmap, Opacity=0.7
 - Filters: Year=2025, Category=Urban
 - Cluster: OFF
-------------------------------------------------
```
