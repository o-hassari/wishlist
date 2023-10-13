from sqlalchemy.orm import Session

from ..models import wishlist as wishlist_model
from ..schemas import wishlist as wishlist_schema

def get_wishlists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(wishlist_model.Wishlist).offset(skip).limit(limit).all()

def get_wishlist(db: Session, wishlist_id: int):
    return db.query(wishlist_model.Wishlist).filter(wishlist_model.Wishlist.id == wishlist_id).first()

def create_wishlist(db: Session, wishlist: wishlist_schema.WishlistCreate):
        wishlist_dict = wishlist.model_dump()
        cwishlist = wishlist_model.Wishlist(**wishlist_dict)

        db.add(cwishlist)
        db.commit()
        db.refresh(cwishlist)

        return cwishlist


def delete_wishlist(db: Session, wishlist_id: int):
     dwishlist = db.query(wishlist_model.Wishlist).filter(wishlist_model.Wishlist.id == wishlist_id).delete()
     db.commit()
     return dwishlist