import enum
import sqlalchemy as sa
from sqlalchemy.orm import relationship
from ..database import Base
from fastapi_utils.guid_type import GUID

class ConfidentialityEnum(enum.Enum): 
    private = "private"
    public = "public"

class Wishlist(Base):
    __tablename__ = 'wishlists'

    id = sa.Column(GUID, primary_key=True, autoincrement=False, nullable=True)

    name = sa.Column(sa.String(100))
    location = sa.Column(sa.String(100))
    description = sa.Column(sa.Text)
    confidentiality = sa.Column(sa.Enum(ConfidentialityEnum))

    user_id = sa.Column(GUID, sa.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)

    user = relationship("User")



class Item(Base):
    __tablename__ = 'items'

    id = sa.Column(GUID, primary_key=True, autoincrement=False, nullable=True)

    link = sa.Column(sa.Text())
    name = sa.Column(sa.String(100), unique=True)
    price = sa.Column(sa.Float())
    image = sa.Column(sa.Text)
    description = sa.Column(sa.String(300))

    wishlist_id = sa.Column(GUID, sa.ForeignKey('wishlists.id', ondelete="CASCADE"), nullable=False)

    wishlist = relationship("Wishlist")



class WishlistShare(Base):
    __tablename__ = 'wishlist_share'

    wishlist_id = sa.Column(GUID, sa.ForeignKey('wishlists.id'), primary_key=True)
    user_id = sa.Column(GUID, sa.ForeignKey('users.id'), primary_key=True)

    share_link = sa.Column(sa.String(100))
    access_expiration = sa.Column(sa.DateTime(timezone=True), server_default=sa.func.now())