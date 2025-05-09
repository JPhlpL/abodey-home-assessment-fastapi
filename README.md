# 24x7 Home Assessment (FastAPI)

This repository contains the backend service implementation for the 24x7 Home Assessment.

---

## Project Structure

```
.
├── routers          # Endpoint definitions
├── services         # Business logic between routers and repositories
├── repositories     # Database interaction layer
├── utils
│   ├── logger       # Logfire logger integration
│   └── dependencies # Common dependency functions for routers
└── db
    └── config.py    # Database (Supabase PostgreSQL) configuration
```

## Technologies

* **Backend**: [FastAPI](https://fastapi.tiangolo.com/) with [Pydantic](https://docs.pydantic.dev/)
* **Database**: [Supabase (PostgreSQL)](https://supabase.com)
* **Logging**: [Logfire](https://logfire.us.pydantic.dev/)
* **Linting**: [Mypy](https://mypy-lang.org/)
* **Version Control**: Git & GitHub
* **Containerization**: Docker & Docker Compose
* **CORS Support**: Ready for frontend integration

---

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/JPhlpL/abodey-home-assessment-fastapi.git
```

### Setup Supabase Database

1. Sign up at [Supabase](https://supabase.com/).
2. Create a new project.
3. Retrieve connection parameters:

   * Go to your project and click **Connect**.
   * Choose between **Direct Connection** or **Session Pooler**.
   * Store connection details in `.env`.

### Database Migration

1. In your Supabase project, navigate to **SQL Editor**.
2. Copy and paste SQL scripts from the `migrations/` directory.
3. Execute to set up the database.

### Setup Logfire

1. Sign up at [Logfire](https://logfire.us.pydantic.dev/).
2. Create a new project.
3. Generate and store the **Write Token** in `.env`.

---

## Environment Variables (`.env.local`)

```dotenv
LOGFIRE_TOKEN=<your_logfire_token>
POSTGRE_DB_CONNECTION_WITH_PASSWORD=<your_supabase_connection_string>
X_AUTH_API_KEY=<your_auth_api_key>
```

---

## Docker Setup

Ensure Docker and Docker Compose are installed.

### Build and Run

```bash
docker-compose up --build
```

### Run MyPy Linting

```bash
docker exec -it <container_name> mypy src
```

---

## Resource Schema

**Contacts**:

| Field         | Type      | Description                  |
| ------------- | --------- | ---------------------------- |
| id            | UUID      | Primary Key                  |
| name          | String    | User/Owner name              |
| phone\_number | String    | User phone number            |
| email         | String    | User email                   |
| created\_at   | Timestamp | Record creation timestamp    |
| updated\_at   | Timestamp | Record last update timestamp |

---

## Contribution

Contributions are welcome. Fork the repository and submit pull requests for review.

---

© 2025 24x7 Home Assessment by John Philip Lominoque
