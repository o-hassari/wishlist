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


@router.get("", response_model=List[item_schema.Item])
def get_user(db: Session = Depends(get_db)):
    items = crud_item.get_items(db)

    return items