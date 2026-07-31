import os
import sys

import pytest
from fastapi.testclient import TestClient

os.environ["DATABASE_URL"] = "sqlite:///./test_banking.db"

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.main import app


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client


def test_create_and_list_customers(client):
    response = client.post(
        "/customers/",
        json={
            "name": "Alice Johnson",
            "email": "alice@example.com",
            "phone": "555-0101",
            "address": "123 Main St",
        },
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["name"] == "Alice Johnson"

    list_response = client.get("/customers/")
    assert list_response.status_code == 200
    customers = list_response.json()
    assert any(customer["email"] == "alice@example.com" for customer in customers)


def test_create_transaction(client):
    customer_response = client.post(
        "/customers/",
        json={
            "name": "Bob Smith",
            "email": "bob@example.com",
            "phone": "555-0102",
            "address": "456 Oak Ave",
        },
    )
    customer_id = customer_response.json()["id"]

    response = client.post(
        "/transactions/",
        json={
            "customer_id": customer_id,
            "transaction_type": "deposit",
            "amount": 250.0,
            "description": "Initial deposit",
        },
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["customer_id"] == customer_id
    assert payload["amount"] == 250.0
