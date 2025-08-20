# Economical

This project has evolved into a small **financial model playground** built
with Flask and a minimal HTML front‑end. It demonstrates a complete
workflow for experimenting with economic time series:

1. **Collect real market data** using the Yahoo Finance API.
2. **Transform the raw series** into modelling variables such as
   percentage returns.
3. **Fit a simple autoregressive model** to the processed data.
4. **Validate the model** on recent observations to check how well it
   captures reality.

The original API for serving cached time series is still available and a
new web form at `/model` drives the modelling pipeline.

## Setup

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment**

   Copy the example configuration and adjust as needed:

   ```bash
   cp .env.example .env
   ```

   The application recognises the following variables:

   | Variable | Description | Default |
   | --- | --- | --- |
   | `SERIES_SOURCE` | Base URL of the data source | `https://example.com/api` |
   | `SERIES_SYMBOL` | Identifier for the requested series | `demo` |
   | `SERIES_START` | Start date (`YYYY-MM-DD`) | `2000-01-01` |
   | `SERIES_END` | End date (`YYYY-MM-DD`) | current date |

3. **Run the service**

   ```bash
   python app.py
   ```

   The service exposes a health check at `/`, cached data under
   `/api/data/<series_id>` and an interactive modelling playground at
   `/model`.

## Development

The codebase also contains utilities for applying database migrations and registering per-user MySQL databases. These utilities are not invoked during normal execution but can be used as hooks for a broader application.

## License

This project is licensed under the MIT License.
