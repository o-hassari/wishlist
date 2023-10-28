from sqlalchemy.orm import Session

from ..models import user as user_model
from ..schemas import user as user_schema
from ..utils import passwd_utils


def get_user(db: Session, user_id: int):
    return db.query(user_model.User).filter(user_model.User.id == user_id).first() #db.query(user.User).filter(user.User.id == user_id).first()

#def get_user_by_email(db: Session, email: str):
#    return db.query(user.User).filter(user.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_model.User).offset(skip).limit(limit).all() #db.query(user.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: user_schema.UserCreate):
        # Hash password
        hashed_pwd = passwd_utils.get_password_hash(user.password)
        user_dict = user.model_dump()
        user_dict['password'] = hashed_pwd
        cuser = user_model.User(**user_dict)

        db.add(cuser)
        db.commit()
        db.refresh(cuser)

        return cuser

def delete_user(db: Session, user_id: int):
     duser = db.query(user_model.User).filter(user_model.User.id == user_id).delete()
     db.commit()
     return duser