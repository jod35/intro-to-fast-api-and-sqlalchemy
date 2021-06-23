from sqlalchemy import Session
from . import database,models,main

def get_item(db:Session,item_id:int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def get_all_items(db:Session,skip:int=0,limit:int=10):
    return db.query(models.Item).offset(skip).limit(limit).all()

def create_item(db:Session,user:main.Item):
    new_item =models.Item(name=user.name,price=user.price,is_offer=user.is_offer)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


