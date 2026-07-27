import sys
from pathlib import Path

from fastapi import Depends
from sqlalchemy.orm import Session

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.database import get_db


def get_db_session():
    return get_db()


def get_session(db: Session = Depends(get_db)):
    return db
