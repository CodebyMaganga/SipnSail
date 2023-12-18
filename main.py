from fastapi import FastAPI
from pydantic import BaseModel
from db import local_session
from typing import List, Optional
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

@app.get('/products', response_model=List[Product])
def get_all_products():
    items = db.query(models.Product).all()
    return items

@app.get('/product/{item_id}')
def get_product(item_id: int):
    return {"Code check one two"}

@app.post('/products',response_model=Product)
def create_product(product:Product):
    new_item = models.Product(
        name=product.name,
        url=product.url,
        price=product.price,
        category=product.category,
        on_offer=product.on_offer
    )

    db.add(new_item)
    db.commit()
    return new_item

@app.patch('/products/{item_id}')
def update_product(item_id:int, item:Product):
    return {'name': item.name,
            'price': item.price,
            'category': item.category,
            }

@app.delete('/products/{item_id}')
def delete_product(item_id: int):
    return {"Code check one two"}

