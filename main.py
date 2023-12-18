from fastapi import FastAPI, HTTPException, status
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

@app.get('/product/{item_id}', response_model=Product)
def get_product(item_id: int):
    item = db.query(models.Product).filter(models.Product.id == item_id).first()
    return item

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

@app.put('/products/{item_id}')
def update_product(item_id:int, item:Product):
    updated_item = db.query(models.Product).filter(models.Product.id == item_id).first()
    updated_item.name = item.name
    updated_item.price = item.price
    updated_item.url = item.url
    updated_item.on_offer = item.on_offer
    updated_item.category = item.category

    db.commit()

    return updated_item


@app.delete('/products/{item_id}')
def delete_product(item_id: int):
    deleted_item = db.query(models.Product).filter(models.Item.id == item_id).first()

    if deleted_item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
    
    return deleted_item

