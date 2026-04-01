from pydantic import BaseModel

class ProductResponse(BaseModel):
    id: str
    category: str
    price: float

    class Config:
        from_attributes = True  # for SQLAlchemy
