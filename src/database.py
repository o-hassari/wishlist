from functools import lru_cache
from typing import Iterator
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import declarative_base, session

from fastapi_utils.session import FastAPISessionMaker

from .config import settings

#SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{settings.db_username}:{settings.db_password}@{settings.db_hostname}:{settings.db_port}/{settings.db_name}"#f"postgresql://{settings.db_username}:{settings.db_password}@{settings.db_hostname}" \
                          #f":{settings.db_port}/{settings.db_name}"

SQLALCHEMY_DATABASE_URL = f"mariadb+mariadbconnector://{settings.db_username}:{settings.db_password}@{settings.db_hostname}:{settings.db_port}/{settings.db_name}"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

if not database_exists(engine.url):
    create_database(engine.url)

def get_db() -> Iterator[session.Session]:
    """FastAPI dependency that provides a sqlalchemy session"""
    yield from _get_fastapi_sessionmaker().get_db()


@lru_cache()
def _get_fastapi_sessionmaker() -> FastAPISessionMaker:
    """This function could be replaced with a global variable if preferred"""
    return FastAPISessionMaker(SQLALCHEMY_DATABASE_URL)