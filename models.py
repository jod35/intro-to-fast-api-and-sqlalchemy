from database import Base
from sqlalchemy import Column,String,Integer,Boolean
from dataclasses import dataclass


class Item(Base):
    __tablename__ ='items'
    id=Column(Integer,primary_key=True)
    name=Column(String(200),unique=True)
    price=Column(Integer,nullable=False)
    is_offer=Column(Boolean,default=False)


    def __repr__(self):
        return f"<Item name={self.name} price={self.price} is_offer={self.is_offer}>"

