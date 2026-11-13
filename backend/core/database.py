
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

from backend.core.config import settings


database_url = settings.DATABASE_URL

connect_args = (
    {"check_same_thread": False}
    if database_url.startswith("sqlite")
    else {}
)

engine = create_engine(
    database_url,
    connect_args=connect_args,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_db_session():
    db: Session = SessionLocal()

    try:
        yield db
    finally:
        db.close()
