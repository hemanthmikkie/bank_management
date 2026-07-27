import os
os.environ['DATABASE_URL'] = "mysql+pymysql://root:minnie@localhost:3306/bank_management"
from app.main import app
from fastapi.testclient import TestClient

with TestClient(app) as client:
    response = client.post('/customers/', json={
        'name': 'Alice Johnson',
        'email': 'alice@example.com',
        'phone': '555-0101',
        'address': '123 Main St'
    })
    print('status', response.status_code)
    print(response.text)
