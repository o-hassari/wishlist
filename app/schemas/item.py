from pydantic import BaseModel


class Item(BaseModel):
    id: int
    link: str
    name: str
    price: float
    image: str
    description: str