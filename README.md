# Banking Management API

A simple REST API for managing bank customers and their transactions, built with **FastAPI** and **SQLAlchemy**.

## Features

- Create and list customers
- Create and list transactions (deposits, withdrawals, etc.) linked to customers
- Health check endpoint
- Works with both **MySQL** (default) and **SQLite** (e.g. for testing)

## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) — web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) — ORM
- [Pydantic](https://docs.pydantic.dev/) — data validation
- [PyMySQL](https://pymysql.readthedocs.io/) — MySQL driver
- [pytest](https://docs.pytest.org/) + [httpx](https://www.python-httpx.org/) — testing

## Project Structure

```
app/
├── __init__.py
├── main.py          # FastAPI app instance and router registration
├── database.py       # DB engine/session setup
├── models.py          # SQLAlchemy ORM models (Customer, Transaction)
├── schemas.py          # Pydantic request/response schemas
├── crud.py             # Database access functions
├── dependencies.py     # Shared FastAPI dependencies
└── routers/
    ├── customers.py    # /customers endpoints
    └── transactions.py # /transactions endpoints

test_banking_api.py     # API integration tests
requirements.txt
```

> **Note:** This project expects to live inside an `app/` package (i.e. these files should be placed in a folder named `app/`, alongside a parent directory that contains `test_banking_api.py`).

## Getting Started

### 1. Clone and set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the database

By default, the app connects to MySQL:

```
mysql+pymysql://root:minnie@localhost:3306/bank_management
```

You can override this with the `DATABASE_URL` environment variable. For example, to use SQLite instead:

```bash
export DATABASE_URL="sqlite:///./banking.db"
```

Make sure the target database (e.g. `bank_management` in MySQL) exists before running the app — tables are created automatically on startup via `Base.metadata.create_all`.

### 4. Run the server

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`, with interactive docs at `http://127.0.0.1:8000/docs`.

## API Endpoints

| Method | Endpoint          | Description                    |
|--------|-------------------|---------------------------------|
| GET    | `/health`         | Health check                   |
| POST   | `/customers/`     | Create a new customer          |
| GET    | `/customers/`     | List all customers             |
| POST   | `/transactions/`  | Create a new transaction       |
| GET    | `/transactions/`  | List all transactions          |

### Example: Create a customer

```bash
curl -X POST http://127.0.0.1:8000/customers/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "phone": "555-0101",
    "address": "123 Main St"
  }'
```

### Example: Create a transaction

```bash
curl -X POST http://127.0.0.1:8000/transactions/ \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": 1,
    "transaction_type": "deposit",
    "amount": 250.0,
    "description": "Initial deposit"
  }'
```

## Running Tests

Tests use a local SQLite database (`test_banking.db`) by default, so no MySQL setup is needed:

```bash
pytest test_banking_api.py -v
```

## Environment Variables

| Variable       | Default                                                        | Description               |
|----------------|-----------------------------------------------------------------|----------------------------|
| `DATABASE_URL` | `mysql+pymysql://root:minnie@localhost:3306/bank_management`    | SQLAlchemy database URL   |

## License

This project is currently unlicensed — add a license of your choice (e.g. MIT) if you plan to share or open source it.
