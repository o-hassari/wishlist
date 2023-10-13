import enum
from sqlalchemy import Column, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


#class confidentialityEnum(enum.Enum): 
#    private = "private"
#    public = "public"

class Wishlist(Base):
    __tablename__ = 'wishlists'

    id = Column(Integer, primary_key=True, nullable=False)
    share_link = Column(String(100))
    name = Column(String(100))
    location = Column(String(100))
    description = Column(String(300))
    #confidentiality = Column(Enum(confidentialityEnum))

    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    user = relationship("User")



class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, nullable=False)
    link = Column(String(100))
    name = Column(String(100))
    price = Column(Float)
    image = Column(String(100))
    description = Column(String(300))

    wishlist_id = Column(Integer,ForeignKey('wishlists.id', ondelete="CASCADE"), nullable=False)

    wishlist = relationship("Wishlist")