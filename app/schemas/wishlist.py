
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
