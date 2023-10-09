from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(25), nullable=False)
    last_name = Column(String(25), nullable=False)
    birthdate = Column(Date, nullable=False)
    email = Column(String(50), nullable=False,
                   unique=True)  # unique means that field must be present only one time in the db
    password = Column(String(50), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    disabled = Column(Boolean, nullable=False)