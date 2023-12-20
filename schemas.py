from pydantic import BaseModel
from datetime import datetime

class Product(BaseModel):
    id:int
    name:str
    url:str
    price: str
    category: str
    on_offer: bool

    class Config:
        orm_mode = True

class Cart_Item(BaseModel):
    id: int
    session_id: int
    product_id: int
    quantity: int
    created_at:datetime
    modified_at:datetime

    class Config:
        orm_mode = True

class Session(BaseModel):
    id: int
    user_id: int
    total: int
    created_at:datetime
    modified_at:datetime

    class Config:
        orm_mode = True

class OrderDetail(BaseModel):
    id: int
    user_id: int
    total: int
    payment_id: int
    created_at:datetime
    modified_at:datetime

    class Config:
        orm_mode = True

class OrderItem(BaseModel):
    id: int


