from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id:int
    name:str
    url:str
    price: str
    category: str
    created_at: str

@app.get('/')
async def Home():
    return {"Code check one two"}

@app.get('/products')
async def get_all_products():
    return {"Code check one two"}

@app.get('/product/{item_id}')
async def get_product():
    return {"Code check one two"}

@app.post('/products')
async def create_product():
    return {"Code check one two"}

@app.patch('/products/{item_id}')
async def update_product(item_id:int, item:Item):
    return {'name': item.name,
            'price': item.price,
            'category': item.category,
            }

@app.delete('/products/{item_id}')
async def delete_product(item_id):
    return {"Code check one two"}

