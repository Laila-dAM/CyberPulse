from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.core.config import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
