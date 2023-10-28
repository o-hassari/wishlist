import logging
from typing import List
from fastapi import Response, status, HTTPException, Depends, APIRouter
from pydantic import ValidationError
from sqlalchemy.orm import Session

from ..database import get_db

from ..schemas import user as user_schema
from ..crud import user as crud_user

router = APIRouter(
    prefix="/users",
    tags=['Users'],
)


@router.get("", response_model=List[user_schema.User])
def get_user(db: Session = Depends(get_db)):
    user = crud_user.get_users(db)
    return user

@router.post("", status_code=status.HTTP_201_CREATED, response_model=user_schema.User)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    try:
        return crud_user.create_user(db, user)

    except ValidationError as e:
        logging.error(f"Validation error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    except Exception as e:
        logging.error(f"Validation error: {str(e)}")
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bad Request")

    finally:
        db.close()

@router.get("/{id}", response_model=user_schema.User)
def get_user(id: int, db: Session = Depends(get_db)):
    user = crud_user.get_user(db, id)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id={id} does not exist")
    
    return user

@router.delete("/{id}", response_model=None)
def delete_user(id: int, db: Session = Depends(get_db)):
    user = crud_user.delete_user(db, id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id={id} does not exist")
    return Response(status_code=status.HTTP_200_OK)