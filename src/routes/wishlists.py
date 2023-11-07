import logging
from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response, status
from pydantic import ValidationError

from sqlalchemy.orm import Session

from ..schemas.user import SystemUser

from ..auth.oauth2 import get_current_user

from ..database import get_db

import uuid

from ..schemas import wishlist as wishlist_schema
from ..crud import wishlist as crud_wishlist
from ..crud import item as crud_item

router = APIRouter(
    prefix="/wishlists",
    tags=['Wishlist'],
)


@router.get("", response_model=List[wishlist_schema.Wishlist])
def get_wishlists(db: Session = Depends(get_db), user: SystemUser = Depends(get_current_user)):
    return crud_wishlist.get_user_wishlists(db, user.id)

@router.get("/{wishlist_id}", response_model=wishlist_schema.Wishlist)
def get_wishlist( wishlist_id: uuid.UUID, db: Session = Depends(get_db)):
    wishlist = crud_wishlist.get_wishlist(db, wishlist_id)
    if wishlist.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Wishlist with id={wishlist_id} does not exist")
    return  wishlist.first()


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
        
@router.get("/{wishlist_id}/items", response_model=wishlist_schema.WishlistItem)
def get_wishlist_all( wishlist_id: uuid.UUID, db: Session = Depends(get_db)):
    wishlist = crud_wishlist.get_wishlist(db, wishlist_id)
    if wishlist.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Wishlist with id={wishlist_id} does not exist")
    
    wl = wishlist.first()

    items = crud_item.get_items_of_wishlist(db, wishlist_id)
    
    items_dict = []

    if not items:
        return wishlist_schema.WishlistItem(id=wl.id,name=wl.name, share_link=wl.share_link, description= wl.description, location=wl.location, items=items_dict)
    
    for item in items:
        item_dict = item.__dict__
        items_dict.append(item_dict)

    return wishlist_schema.WishlistItem(id=wl.id,name=wl.name, share_link=wl.share_link, description= wl.description, location=wl.location, items=items_dict)

@router.post("/{wishlist_id}/items", response_model= List[wishlist_schema.ItemWithWishlistId])
def create_wishlist_items(wishlist_id: uuid.UUID, items: List[wishlist_schema.ItemCreate], db: Session = Depends(get_db)):
    wishlist = crud_wishlist.get_wishlist(db, wishlist_id)
    print(wishlist.first())
    if wishlist.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Wishlist with id: {wishlist_id}")
    
    return crud_item.create_items(db, items, wishlist_id)

@router.put("/{wishlist_id}", response_model=wishlist_schema.Wishlist)
def update_wishlist(wishlist_id: int, wishlist: wishlist_schema.WishlistUpdate, db: Session = Depends(get_db)):
    try:
        wishlist_to_update = crud_wishlist.get_wishlist(db, wishlist_id)

        if wishlist_to_update.first() is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Wishlist with id={wishlist_id} does not exist")

        crud_wishlist.update_wishlist(db, wishlist, wishlist_id)
        return crud_wishlist.get_wishlist(db, wishlist_id).first()
    
    except ValidationError as e:
        logging.error(f"Validation error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.delete("/{wishlist_id}", response_model=None)
def delete_user(wishlist_id: int, db: Session = Depends(get_db)):
    wishlist = crud_wishlist.delete_wishlist(db, wishlist_id)
    if not wishlist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Wishlist with id={wishlist_id} does not exist")
    
    return Response(status_code=status.HTTP_200_OK)