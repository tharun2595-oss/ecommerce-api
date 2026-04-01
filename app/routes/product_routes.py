from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.product import Product
from app.utils.auth import get_current_user
from fastapi.security import HTTPBearer
from typing import List
from app.schemas.product_schema import ProductResponse

security = HTTPBearer()

router = APIRouter(prefix="/products", tags=["Products"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[ProductResponse])
def get_products(
    category: str = Query(None),
    limit: int = 10,
    offset: int = 0,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)  # PROTECTED
):
    query = db.query(Product)

    # Filter
    if category:
        query = query.filter(Product.category.ilike(f"%{category}%"))

    products = query.offset(offset).limit(limit).all()

    return products
