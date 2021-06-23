from database import engine,Base
from models import Item


print("Creating database ....")
Base.metadata.create_all(engine)