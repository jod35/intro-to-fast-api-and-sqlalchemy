from typing import Optional,List
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
import models
import database


app=FastAPI()



class Item(BaseModel):
    name:str
    price:float
    is_offer:Optional[bool]=False

    class Config:
        orm_mode=True

db=database.SessionLocal()


@app.get('/items',response_model=List[Item])
def get_all_items():
    items=db.query(models.Item).all()
    return items


@app.post("/items",response_model=Item)
def create_item(item:Item):
    db_user=db.query(models.Item).filter(models.Item.name==item.name).first()

    if db_user:
        raise HTTPException(status_code=400,detail="Item with name exists")

    new_item=models.Item(name=item.name,price=item.price,is_offer=item.is_offer)

    db.add(new_item)
    db.commit()

    return new_item    


@app.get('/item/{item_id}')
def get_item(item_id:int):
    item=db.query(models.Item).filter(models.Item.id==item_id).first()

    if not item:
        raise HTTPException(status_code=404,detail="Resource Not Found")
    return item


@app.put('/item/{item_id}',response_model=Item)
def update_item(item_id:int,item:Item):
    item_to_update=db.query(models.Item).filter(models.Item.id==item_id).first()
    
    if item is None:
        raise HTTPException(status_code=404,detail="Resource not Found")
    
    item_to_update.name=item.name
    item_to_update.price=item.price
    item_to_update.is_offer=item.is_offer

    db.commit()

    return item_to_update

@app.delete('/item/{item_id}')
def delete_item(item_id):
    item_to_delete=db.query(models.Item).filter(models.Item.id == item_id).first()

    if not item_to_delete:
        raise HTTPException(status_code=404,detail="Resource Not Found")

    db.delete(item_to_delete)

    db.commit()

    return item_to_delete