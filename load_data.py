import pandas as pd
from app.database import SessionLocal, engine, Base
from app.models.product import Product

# Create tables
Base.metadata.create_all(bind=engine)

# Start DB session
db = SessionLocal()

# Load CSV
df = pd.read_csv("data/olist_products_dataset.csv")

print("CSV Loaded...")

# Insert data
for _, row in df.iterrows():
    product = Product(
        id=row["product_id"],
        category=row["product_category_name"],
        price=0.0
    )
    db.add(product)

db.commit()
db.close()

print("Data loaded into database!")
