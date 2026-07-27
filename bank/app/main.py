import sys
from pathlib import Path

from fastapi import FastAPI

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.database import Base, engine
from app.routers import customers, transactions

app = FastAPI(title="Banking Management API")

Base.metadata.create_all(bind=engine)

app.include_router(customers.router)
app.include_router(transactions.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
