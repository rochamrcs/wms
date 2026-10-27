# WMS

A Warehouse Management System built with Django to manage inbound receipts, outbound shipments, internal transfers, and stock balances by storage location.

The system aims to make materials easier to locate and provide traceability for operations that affect inventory.

## Planned Features

- Authentication and role-based access control.
- Product registration and management.
- Storage location registration and management.
- Inbound receiving.
- Outbound shipping.
- Internal transfers between storage locations.
- Stock balance queries by product and location.
- Movement history for receipts, shipments, and internal transfers.
- Inventory and movement reports.

## Running Locally

### Prerequisites

- Python 3.13.
- Docker with Docker Compose installed and running.

Run the following commands from the project root.

### 1. Create and Activate a Virtual Environment

```bash
python -m venv .venv
```

On Windows using PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

On Linux/macOS:

```bash
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Configure Environment Variables

Copy `.env.example` to `.env` in the project root.

Set `SECRET_KEY` and `POSTGRES_PASSWORD` to your own local values. Keep the remaining settings as provided unless your environment requires changes.

To generate a secret key, run:

```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

Copy the output into `SECRET_KEY` in your `.env` file.

Do not commit `.env` or credentials to the repository.

### 4. Start PostgreSQL

```bash
docker compose up -d db
docker compose ps
```

Wait until the `db` service reports a `healthy` status.

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Start the Development Server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

Press `Ctrl+C` to stop the development server.

To stop PostgreSQL while preserving its data:

```bash
docker compose stop db
```