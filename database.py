from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = ""

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    from models import Base
    Base.metadata.create_all(bind=engine)