import psycopg2  # noqa: F401
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = 'sqlite:///./instagram.db'

CONN = "postgresql+psycopg2://bo:61512@localhost:5432/instagramdb"

engine = create_engine(CONN)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


__all__ = ["engine", "get_db", "Base"]
