from sqlalchemy import Column, String, Float
from app.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True, index=True)
    category = Column(String)
    price = Column(Float)
