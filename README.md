# Student Notes API

This project implements the proposal for a DevOps-focused Student Notes application using Flask, automated testing, GitHub Actions CI/CD, an Azure VM deployment flow, and a browser-based UI for notes management.

## Features

- Create, read, update, and delete student notes through both a web UI and REST API
- JSON-based REST API built with Flask
- SQLite-backed persistence using SQLAlchemy
- Automated testing with `pytest`
- CI/CD with GitHub Actions
- Deployment automation for an Azure Virtual Machine

## Project Structure

```text
.
|-- app/
|   |-- static/styles.css
|   |-- templates/index.html
|   |-- __init__.py
|   |-- models.py
|   |-- routes.py
|   `-- web_routes.py
|-- deploy/azure-vm/
|   |-- deploy.sh
|   |-- setup-server.sh
|   `-- student-notes-api.service
|-- tests/
|-- .github/workflows/ci-cd.yml
|-- requirements.txt
|-- run.py
`-- README.md
```

## Local Setup

1. Create a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python run.py
   ```

4. Open the app in your browser:

   - UI: `http://127.0.0.1:5000/`
   - Health check: `http://127.0.0.1:5000/health`
   - API: `http://127.0.0.1:5000/api/notes`

## UI Routes

- `GET /` - dashboard with create and edit forms
- `POST /notes/create` - create a note from the browser
- `GET /notes/<id>/edit` - open a note in edit mode
- `POST /notes/<id>/edit` - save note updates
- `POST /notes/<id>/delete` - delete a note

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/api/notes` | Retrieve all notes |
| GET | `/api/notes/<id>` | Retrieve a single note |
| POST | `/api/notes` | Create a new note |
| PUT | `/api/notes/<id>` | Update an existing note |
| DELETE | `/api/notes/<id>` | Delete a note |

## Running Tests

```bash
pytest
```

## GitHub Actions Secrets

Add these repository secrets before enabling automatic deployment:

- `AZURE_VM_HOST`
- `AZURE_VM_USER`
- `AZURE_VM_SSH_KEY`
- `AZURE_VM_APP_PATH`

## Azure VM Deployment Flow

1. Run `deploy/azure-vm/setup-server.sh` once on the VM.
2. Make sure `AZURE_VM_APP_PATH` matches your VM deployment directory.
3. Push to `main` to trigger tests and deployment.
4. After deployment, open the app through your VM host and configured port or reverse proxy.

## Suggested Next Steps

- Add Nginx so the UI is reachable on port 80
- Replace SQLite with PostgreSQL for production scale
- Add authentication for multi-user support
- Add monitoring with Prometheus and Grafana
