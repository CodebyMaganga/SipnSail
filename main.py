from fastapi import FastAPI
from pydantic import BaseModel
from db import local_session
from typing import List
import models

app = FastAPI()

class Product(BaseModel):
    id:int
    name:str
    url:str
    price: str
    category: str
    on_offer: bool

    class Config:
        orm_mode = True

db = local_session()

@app.get('/')
def Home():
    return {"Code check one two"}

@app.get('/products', response_model=List[Product], status_code=200)
def get_all_products():
    items = db.query(models.Item).all()
    return items

@app.get('/product/{item_id}')
def get_product(item_id: int):
    return {"Code check one two"}

@app.post('/products')
def create_product():
    return {"Code check one two"}

@app.patch('/products/{item_id}')
def update_product(item_id:int, item:Product):
    return {'name': item.name,
            'price': item.price,
            'category': item.category,
            }

@app.delete('/products/{item_id}')
def delete_product(item_id: int):
    return {"Code check one two"}

