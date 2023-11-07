import uuid
from sqlalchemy import update
from sqlalchemy.orm import Session

from ..models import wishlist as wishlist_model
from ..schemas import wishlist as wishlist_schema

def get_wishlists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(wishlist_model.Wishlist).offset(skip).limit(limit).all()

def get_user_wishlists(db: Session, user_id: uuid.UUID, skip: int = 0, limit: int = 100):
    return db.query(wishlist_model.Wishlist).filter(wishlist_model.Wishlist.user_id == user_id).offset(skip).limit(limit).all()

def get_wishlist(db: Session, wishlist_id: uuid.UUID):
    return db.query(wishlist_model.Wishlist).filter(wishlist_model.Wishlist.id == wishlist_id)

def create_wishlist(db: Session, wishlist: wishlist_schema.WishlistCreate):
    wishlist_dict = wishlist.model_dump()
    wishlist_dict['id']= uuid.uuid4()
    cwishlist = wishlist_model.Wishlist(**wishlist_dict)

    db.add(cwishlist)
    db.commit()
    db.refresh(cwishlist)

    return cwishlist

def create_user_wishlist(db: Session, wishlist: wishlist_schema.WishlistCreate):
    wishlist_dict = wishlist.model_dump()
    wishlist_dict['id']= uuid.uuid4()
    cwishlist = wishlist_model.Wishlist(**wishlist_dict)

    db.add(cwishlist)
    db.commit()
    db.refresh(cwishlist)

    return cwishlist

def update_wishlist(db: Session, wishlist: wishlist_schema.WishlistUpdate, wishlist_id: int):
    wish_dict = wishlist.model_dump(exclude_defaults=True, exclude_none=True)
    query = update(wishlist_model.Wishlist).where(wishlist_model.Wishlist.id == wishlist_id).values(wish_dict)
    db.execute(query)
    db.commit()


def delete_wishlist(db: Session, wishlist_id: uuid.UUID):
    dwishlist = db.query(wishlist_model.Wishlist).filter(wishlist_model.Wishlist.id == wishlist_id).delete()
    db.commit()
    return dwishlist