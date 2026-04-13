# Active containers UI

Small [Flask](https://flask.palletsprojects.com/) app that lists active deployment containers (from a pickled snapshot) and exposes simple HTML views over Celery log files.

## Features

- **Home (`/`)** — Renders a table of containers with HTTP/HTTPS links using `CLUSTER_HOST` and each container’s `hostPort`. Data is read from a pickle file produced by your deploy pipeline (see below).
- **Celery logs (`/celery_logs`)** — Dumps lines from the Celery log file as HTML.
- **Celery errors (`/celery_error_logs`)** — Same as above, but only lines containing the substring `Error`.

## Requirements

- Python 3
- Flask: `pip install flask`

## Configuration

| Item | Description |
|------|-------------|
| `CLUSTER_HOST` | Hostname or IP used in links on the home page (`https://` / `http://` + this host + container port). |

## Data paths (hardcoded)

These paths match the original deployment layout. Change them in `app.py` if your environment differs.

| Route | Path |
|-------|------|
| `/` | `~/deploy-juzam/deploy-on-branch-change/details-latest.txt` (pickle) |
| `/celery_logs`, `/celery_error_logs` | `/home/ubuntu/juzam2/celery-logs.txt` |

The pickle is expected to deserialize to a list of dicts; each dict should include at least `hostPort` (shown as a string in the UI).

## Run locally

```bash
cd /path/to/active-containers-ui
pip install flask
export CLUSTER_HOST=127.0.0.1   # or your cluster hostname
flask --app app run
```

Open `http://127.0.0.1:5000/` (or the host/port Flask prints).

## Project layout

```
app.py              # Flask application
templates/          # Jinja2 templates (home, logs)
static/css/home.css # Styles for the containers table
```
