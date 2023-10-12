from sqlalchemy import Column, Float, Integer, String
from app.database import Base


class Item(Base):
    __tablename__ = "items"

    id= Column(Integer, primary_key=True, nullable=False)
    link= Column(String(100))
    name= Column(String(100))
    price= Column(Float)
    image= Column(String(100))
    description= Column(String(300))
