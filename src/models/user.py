import sqlalchemy as sa

from sqlalchemy import Column, Integer, String
from ..database import Base
from fastapi_utils.guid_type import GUID

class User(Base):
    __tablename__ = "users"

    id = sa.Column(GUID, primary_key=True, autoincrement=False, nullable=True)
    first_name = sa.Column(sa.String(25), nullable=False)
    last_name = sa.Column(sa.String(25), nullable=False)
    birth_date = sa.Column(sa.String(50), nullable=False)
    email = sa.Column(sa.String(50), nullable=False, unique=True)  
    password = Column(sa.String(72), nullable=False)
    
    #created_at = Column(String(50),
    #                    nullable=False, server_default=text('now()'))
    #disabled = Column(Boolean, nullable=False)

class Account(Base):
    # activated_by_gen_pin, account_type, .... user 1,1-1,1 account
    pass