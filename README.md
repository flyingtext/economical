# Economical Data Service

This project provides a simple Flask application that fetches a time series from a remote source, caches it on disk and serves the cached data through a small API. A background scheduler refreshes the cache once per day.

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

   The service exposes a health check at `/` and cached data under `/api/data/<series_id>`.

## Development

The codebase also contains utilities for applying database migrations and registering per-user MySQL databases. These utilities are not invoked during normal execution but can be used as hooks for a broader application.

## License

This project is licensed under the MIT License.
