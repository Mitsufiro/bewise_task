import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.util.compat import contextmanager

load_dotenv('.env')

engine = create_engine(url=os.environ['DATABASE_URL'])
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


def get_db_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


db_context = contextmanager(get_db_session)
