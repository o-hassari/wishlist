from typing import List, Optional
from pydantic import BaseModel

class Wishlist(BaseModel):
    id : int
    share_link: str
    name: str
    location: str
    description: str

class WishlistCreate(BaseModel):
    share_link: str
    name: str
    location: str
    description: str
    user_id: int

class WishlistUpdate(BaseModel):
    #share_link: Optional[str] = None
    name: Optional[str] = None
    location: Optional[str] = None
    description: str | None = None   

class Item(BaseModel):
    id: int
    link: str
    name: str
    price: float
    image: str
    description: str

class ItemWithWishlistId(Item):
    wishlist_id: int

class ItemCreate(BaseModel):
    link: str
    name: str
    price: float
    image: str
    description: str

class ItemUpdate(BaseModel):
    link: Optional[str] = None
    name: Optional[str] = None
    price: Optional[float] = None
    image: Optional[str] = None
    description: str | None = None   

class WishlistItem(Wishlist):
    items: List[Item]