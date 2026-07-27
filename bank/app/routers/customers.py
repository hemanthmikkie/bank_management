import sys
from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app import crud, schemas
from app.dependencies import get_session

router = APIRouter(prefix="/customers", tags=["customers"])


@router.post("/", response_model=schemas.CustomerRead)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_session)):
    try:
        return crud.create_customer(db, customer)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.get("/", response_model=list[schemas.CustomerRead])
def list_customers(db: Session = Depends(get_session)):
    return crud.list_customers(db)
