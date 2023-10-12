from sqlalchemy.orm import Session

from ..models import item as item_model




def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(item_model.Item).offset(skip).limit(limit).all()