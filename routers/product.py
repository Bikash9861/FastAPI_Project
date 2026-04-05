from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import schemas
import crud
from database import SessionLocal

router = APIRouter(prefix="/api/products", tags=["Products"])  # ✅ IMPORTANT

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def get_products(db: Session = Depends(get_db)):
    return {"message": "Products working"}


@router.get("/", response_model=list[schemas.ProductResponse])
def get_all(page: int = 1, db: Session = Depends(get_db)):
    limit = 5
    skip = (page - 1) * limit
    return crud.get_products(db, skip, limit)


@router.get("/{id}", response_model=schemas.ProductResponse)
def get_one(id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/")
def create(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)


@router.put("/{id}")
def update(id: int, data: schemas.ProductCreate, db: Session = Depends(get_db)):
    product = crud.update_product(db, id, data)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    product = crud.delete_product(db, id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Deleted successfully"}