# Student Notes API

This project implements the proposal for a DevOps-focused Student Notes API using Flask, automated testing, GitHub Actions CI/CD, and Azure VM deployment.

## Features

- Create, read, update, and delete student notes
- JSON-based REST API built with Flask
- SQLite-backed persistence using SQLAlchemy
- Automated testing with `pytest`
- CI/CD with GitHub Actions
- Deployment automation for an Azure Virtual Machine

## Project Structure

```text
.
|-- app/
|   |-- __init__.py
|   |-- models.py
|   `-- routes.py
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

3. Run the API:

   ```bash
   python run.py
   ```

4. The application will be available at `http://127.0.0.1:5000`.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/api/notes` | Retrieve all notes |
| GET | `/api/notes/<id>` | Retrieve a single note |
| POST | `/api/notes` | Create a new note |
| PUT | `/api/notes/<id>` | Update an existing note |
| DELETE | `/api/notes/<id>` | Delete a note |

### Example Create Request

```bash
curl -X POST http://127.0.0.1:5000/api/notes \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Exam Prep",
    "content": "Review branching strategies and CI/CD workflow stages.",
    "course": "CSD-4503"
  }'
```

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
2. Copy the repository to the VM path that matches `AZURE_VM_APP_PATH`.
3. Update `deploy/azure-vm/student-notes-api.service` if your VM username or install path differs.
4. Push to `main` to trigger tests and deployment.

## Suggested Next Steps

- Add authentication for multi-user support
- Replace SQLite with PostgreSQL for production scale
- Put Nginx in front of the Flask app
- Add monitoring with Prometheus and Grafana
