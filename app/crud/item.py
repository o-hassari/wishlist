from typing import List
from sqlalchemy.orm import Session

from ..models import wishlist as wishlist_model
from ..schemas import wishlist as wishlist_schema

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(wishlist_model.Item).offset(skip).limit(limit).all()

def get_item(db: Session, item_id: int):
    return db.query(wishlist_model.Item).filter(wishlist_model.Item.id == item_id).first()

def get_items_of_wishlist(db: Session, wishlist_id:int):
    return db.query(wishlist_model.Item).filter(wishlist_model.Item.wishlist_id == wishlist_id).all()

def create_items(db: Session, items: List[wishlist_schema.ItemCreate], wishlist_id: int):
    items_dict = [item.model_dump() for item in items]

    citems_obj = [ wishlist_model.Item(**item, wishlist_id=wishlist_id) for item in items_dict]

    for obj in citems_obj :
        db.add(obj)
        db.commit()
        db.refresh(obj)
    
    return citems_obj

def delete_item(db: Session, item_id: int):
     ditem = db.query(wishlist_model.Item).filter(wishlist_model.Item.id == item_id).delete()
     db.commit()
     return ditem