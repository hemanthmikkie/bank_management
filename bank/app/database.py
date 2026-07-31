import os
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:minnie@localhost:3306/bank_management")
# DATABASE_URL = os.getenv(
#     "DATABASE_URL",
#     "mysql+pymysql://avnadmin:AVNS_TNgAshCoHJKnC2GQhHb@mysql-39501748-hemanthkumarthippavathi-b4e3.g.aivencloud.com:16337/defaultdb?ssl-mode=REQUIRED",
# )
DATABASE_URL="mysql+pymysql://avnadmin:AVNS_TNgAshCoHJKnC2GQhHb@mysql-39501748-hemanthkumarthippavathi-b4e3.g.aivencloud.com:16337/defaultdb"

def _normalize_mysql_url(url: str) -> tuple[str, dict]:
    connect_args: dict = {}
    if url.startswith("mysql+pymysql://"):
        parsed = urlparse(url)
        query = parse_qs(parsed.query, keep_blank_values=True)
        if "ssl-mode" in query:
            query.pop("ssl-mode")
            connect_args["ssl"] = {}
        if "ssl_mode" in query:
            query.pop("ssl_mode")
            connect_args["ssl"] = {}
        if query:
            url = urlunparse(parsed._replace(query=urlencode({k: v[0] for k, v in query.items()}, doseq=True)))
        else:
            url = urlunparse(parsed._replace(query=""))
    return url, connect_args


DATABASE_URL, connect_args = _normalize_mysql_url(DATABASE_URL)
engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args if connect_args else {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
