import os

import psycopg2  # noqa: F401
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

# SQLALCHEMY_DATABASE_URL = 'sqlite:///./instagram.db'

CONN: str | None = os.getenv("DB_CONNECTION")

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
