from fastapi import FastAPI
import models
from database import engine
from routers import category, product

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="E-commerce API")

app.include_router(category.router)
app.include_router(product.router)


@app.get("/")
def home():
    return {"message": "API is running 🚀"}