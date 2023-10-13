import logging
from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response, status
from pydantic import ValidationError

from sqlalchemy.orm import Session

from app.database import get_db


from ..schemas import wishlist as wishlist_schema
from ..crud import wishlist as crud_wishlist

router = APIRouter(
    prefix="/wishlists",
    tags=['Wishlist'],
)


@router.get("", response_model=List[wishlist_schema.Wishlist])
def get_wishlists(db: Session = Depends(get_db)):
    return crud_wishlist.get_wishlists(db)


@router.get("/{wishlist_id}", response_model=wishlist_schema.Wishlist)
def get_wishlist( wishlist_id: int, db: Session = Depends(get_db)):
    wishlist = crud_wishlist.get_wishlist(db, wishlist_id)
    if not wishlist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Wishlist with id={wishlist_id} does not exist")
    return   


@router.post("", status_code=status.HTTP_201_CREATED, response_model=wishlist_schema.Wishlist)
def create_wishlist(wishlist: wishlist_schema.WishlistCreate, db: Session = Depends(get_db)):
    try:
        return crud_wishlist.create_wishlist(db, wishlist)

    except ValidationError as e:
        logging.error(f"Validation error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    except Exception as e:
        logging.error(f"Exception error: {str(e)}")
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bad Request")

    finally:
        db.close()

@router.delete("/{wishlist_id}", response_model=None)
def delete_user(wishlist_id: int, db: Session = Depends(get_db)):
    wishlist = crud_wishlist.delete_wishlist(db, wishlist_id)
    if not wishlist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Wishlist with id={wishlist_id} does not exist")
    return Response(status_code=status.HTTP_200_OK)