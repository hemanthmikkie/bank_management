import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:minnie@localhost:3306/bank_management")
DATABASE_URL= mysql+pymysql://avnadmin:AVNS_TNgAshCoHJKnC2GQhHb@mysql-39501748-hemanthkumarthippavathi-b4e3.g.aivencloud.com:16337/defaultdb?ssl-mode=REQUIRED
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
