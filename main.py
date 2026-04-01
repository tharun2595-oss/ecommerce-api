from fastapi import FastAPI
from app.database import engine, Base
from app.routes import product_routes, auth_routes


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ecommerece API",
              description="Backend API with JWT Auth",
              version="1.0.0")

app.include_router(product_routes.router)
app.include_router(auth_routes.router)

@app.get("/")
def root():
    return {"message": "API running"}
