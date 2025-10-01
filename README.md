# Flask + Pydantic + PostgreSQL (Datetime Demo)

A minimal example showing how to handle **datetimes** consistently in a  
**Flask + Pydantic + PostgreSQL** stack using Docker.

✅ Features:
- Flask 2.3 with a custom JSON provider  
- Pydantic models for validation and serialization  
- PostgreSQL (`timestamptz` for proper timezone handling)  
- Docker setup (Postgres + API)  
- Returns datetimes in **ISO 8601** format (RFC-compliant, frontend-friendly)

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/dataLinkGG/flask-pydantic-datetime-demo.git
cd flask-pydantic-datetime-demo
```

### 2. Start services
```
docker compose up --build
```
- PostgreSQL on localhost:5432
- Flask API on localhost:5000


### 3. Test the endpoint

Open Postman, curl, or browser:
```bash
curl http://localhost:5000/task
```

You’ll get a JSON response like:

```
{
  "id": 1,
  "name": "demo",
  "execute_at": "2025-10-01T12:00:00+00:00"
}
```
