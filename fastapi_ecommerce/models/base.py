from typing import Generator

from fastapi_ecommerce.settings import db_settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

_engine = create_engine(db_settings.engine_string, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_engine)


Base = declarative_base()


def get_session() -> Generator:
    try:
        session = SessionLocal()
        yield session
    finally:
        session.close()
