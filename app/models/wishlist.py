import enum
from sqlalchemy import Column, Enum, Float, Integer, String
from app.database import Base


class confidentialityEnum(enum.Enum): 
    private = "private"
    public = "public"

class Item(Base):
    __tablename__ = "wishlists"

    id: Column(Integer, primary_key=True, nullable=False)
    share_link: Column(String(100))
    name: Column(String(100))
    location: Column(String(100))
    description: Column(String(300))
    confidentiality: Column(Enum(confidentialityEnum))

    