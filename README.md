# 24x7 Home Assessment (FastAPI)

This repository contains the backend service implementation for the **24x7 Home Assessment**.

---

## 📁 Project Structure

```plaintext
.
├── routers          # Endpoint definitions
├── services         # Business logic connecting routers and repositories
├── repositories     # Database interaction layer
├── utils
│   ├── logger       # Logfire integration
│   └── dependencies # Common dependencies for routers
└── db
    └── config.py    # Supabase (PostgreSQL) configuration
```

---

## 🚀 API Endpoints

### 🔎 Get All Contacts

* **Endpoint**: `GET /contact/get-all-contacts`
* **Description**: Retrieve all contacts stored in the database.

### 🔍 Get Specific Contact

* **Endpoint**: `GET /contact/{phone_number}`
* **Description**: Retrieve a specific contact using their phone number.

| Parameter      | Type   | Required | Description             |
| -------------- | ------ | -------- | ----------------------- |
| `phone_number` | String | Yes      | Contact's phone number. |

### ➕ Add Contact

* **Endpoint**: `POST /contact/add`
* **Description**: Add a new contact to the database.
* **Request Body**:

```json
{
  "name": "John Doe",
  "phone_number": "09555298035",
  "email": "johndoe@gmail.com"
}
```

| Field          | Type   | Required | Description             |
| -------------- | ------ | -------- | ----------------------- |
| `name`         | String | Yes      | Name of the contact.    |
| `phone_number` | String | Yes      | Contact's phone number. |
| `email`        | String | Yes      | Email of the contact.   |

---

## 🛠️ Technologies

* **Backend**: [FastAPI](https://fastapi.tiangolo.com/) with [Pydantic](https://docs.pydantic.dev/)
* **Database**: [Supabase (PostgreSQL)](https://supabase.com)
* **Logging**: [Logfire](https://logfire.us.pydantic.dev/)
* **Linting**: [Mypy](https://mypy-lang.org/)
* **Version Control**: Git & GitHub
* **Containerization**: Docker & Docker Compose
* **CORS**: Frontend integration ready

---

## 📌 Getting Started

### 🛎️ Clone Repository

```bash
git clone https://github.com/JPhlpL/abodey-home-assessment-fastapi.git
```

### 📦 Supabase Database Setup

1. Sign up at [Supabase](https://supabase.com/).
2. Create a new project and retrieve connection parameters.
3. Store these parameters in `.env`.

### 📑 Database Migration

1. Navigate to **SQL Editor** in Supabase.
2. Paste and execute SQL scripts from `migrations/`.

### 📈 Logfire Setup

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

## 🐳 Docker Setup

Ensure Docker and Docker Compose are installed.

### 🛠️ Build and Run

```bash
docker-compose up --build
```

### ✅ Run MyPy Linting

```bash
docker exec -it <container_name> mypy src
```

---

## 📋 Resource Schema

**Contacts**:

| Field          | Type      | Description                  |
| -------------- | --------- | ---------------------------- |
| `id`           | UUID      | Primary Key                  |
| `name`         | String    | User/Owner name              |
| `phone_number` | String    | User phone number            |
| `email`        | String    | User email                   |
| `created_at`   | Timestamp | Record creation timestamp    |
| `updated_at`   | Timestamp | Record last update timestamp |

---

## 📦 Postman API Collection

Import the collection API from the `export` directory into your Postman Collection.

---

## 🤝 Contribution

Contributions are welcome! Fork the repository and submit your pull requests.

---

© 2025 24x7 Home Assessment by **John Philip Lominoque**
