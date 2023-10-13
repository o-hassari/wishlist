from sqlalchemy import Column, Integer, String
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(25), nullable=False)
    last_name = Column(String(25), nullable=False)
    birth_date = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)  
    password = Column(String(72), nullable=False)
    
    #created_at = Column(String(50),
    #                    nullable=False, server_default=text('now()'))
    #disabled = Column(Boolean, nullable=False)