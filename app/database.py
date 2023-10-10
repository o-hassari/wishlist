from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import settings

# "postgresql://<user>:<password>@<ip-address/hostname>/<database_name>"
#SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{settings.db_username}:{settings.db_password}@{settings.db_hostname}:{settings.db_port}/{settings.db_name}"#f"postgresql://{settings.db_username}:{settings.db_password}@{settings.db_hostname}" \
                          #f":{settings.db_port}/{settings.db_name}"

SQLALCHEMY_DATABASE_URL = f"mariadb+mariadbconnector://{settings.db_username}:{settings.db_password}@{settings.db_hostname}:{settings.db_port}/{settings.db_name}"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

if not database_exists(engine.url):
    create_database(engine.url)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()