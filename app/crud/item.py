from sqlalchemy.orm import Session

from ..models import wishlist as item_model




def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(item_model.Item).offset(skip).limit(limit).all()

def get_item(db: Session, item_id: int):
    return db.query(item_model.Item).filter(item_model.Item.id == item_id).first()

#def create_item(db: Session, item: item_model.ItemCreate, wishlist_id: int):
#    pass

def delete_item(db: Session, item_id: int):
     duser = db.query(item_model.Item).filter(item_model.Item.id == item_id).delete()
     db.commit()
     return duser