from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os

base_dir=os.path.dirname(os.path.realpath(__file__))

conn_str="sqlite:///"+os.path.join(base_dir,"site.db")

engine=create_engine(conn_str,echo=True)

SessionLocal=sessionmaker(bind=engine)

Base=declarative_base()