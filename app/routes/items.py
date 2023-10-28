import logging
from typing import List
from fastapi import Response, status, HTTPException, Depends, APIRouter
from pydantic import ValidationError
from sqlalchemy.orm import Session

from ..database import get_db

from ..schemas import item as item_schema
from ..crud import item as crud_item

router = APIRouter(
    prefix="/items",
    tags=['Items'],
)

@router.delete("/{item_id}", response_model=None)
def delete_item(item_id: int,  db: Session = Depends(get_db)):
    item = crud_item.delete_item(db, item_id)

    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with id={item_id} does not exist") 
    
    return Response(status_code=status.HTTP_200_OK)