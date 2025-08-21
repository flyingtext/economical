# Data Pipeline Daemon

The data pipeline now runs in a dedicated process. Start it with:

```bash
python scripts/data_pipeline_daemon.py
```

## systemd

Example unit file to run the daemon via systemd:

```ini
[Unit]
Description=Economical data pipeline
After=network.target

[Service]
WorkingDirectory=/path/to/economical
ExecStart=/usr/bin/python scripts/data_pipeline_daemon.py
Restart=always

[Install]
WantedBy=multi-user.target
```

## Docker Compose

To run the daemon in Docker alongside the web server:

```yaml
services:
  data-pipeline:
    build: .
    command: python scripts/data_pipeline_daemon.py
```
