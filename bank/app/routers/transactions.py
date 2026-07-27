import sys
from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app import crud, schemas
from app.dependencies import get_session

router = APIRouter(prefix="/transactions", tags=["transactions"])


@router.post("/", response_model=schemas.TransactionRead)
def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_session)):
    try:
        return crud.create_transaction(db, transaction)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.get("/", response_model=list[schemas.TransactionRead])
def list_transactions(db: Session = Depends(get_session)):
    return crud.list_transactions(db)
