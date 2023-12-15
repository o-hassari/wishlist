import logging
from typing import List
from fastapi import Response, status, HTTPException, Depends, APIRouter
from pydantic import ValidationError
from sqlalchemy.orm import Session

from ..database import get_db

from ..schemas import wishlist as item_schema
from ..crud import item as crud_item

router = APIRouter(
    prefix="/items",
    tags=['Items'],
)

@router.get("/{item_id}", response_model=item_schema.Item)
def get_wishlist( item_id: int, db: Session = Depends(get_db)):
    item = crud_item.get_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Wishlist with id={item} does not exist")
    return  item

@router.put("/{item_id}")
def update_item(item_id: int, item: item_schema.ItemUpdate, db: Session = Depends(get_db)):
    try:
        item_to_update = crud_item.get_item(db, item_id)

        if item_to_update is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Wishlist with id={item_id} does not exist")

        crud_item.update_item(db, item, item_id)
        return crud_item.get_item(db, item_id)
    
    except ValidationError as e:
        logging.error(f"Validation error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.delete("/{item_id}", response_model=None)
def delete_item(item_id: int,  db: Session = Depends(get_db)):
    item = crud_item.delete_item(db, item_id)

    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with id={item_id} does not exist") 
    
    return Response(status_code=status.HTTP_200_OK)