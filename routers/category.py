from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import SessionLocal

router = APIRouter(prefix="/api/categories", tags=["Categories"])  # ✅ IMPORTANT

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return {"message": "Categories working"}


@router.get("/")
def get_all(page: int = 1, db: Session = Depends(get_db)):
    limit = 5
    skip = (page - 1) * limit
    return crud.get_categories(db, skip, limit)


@router.get("/{id}")
def get_one(id: int, db: Session = Depends(get_db)):
    category = crud.get_category(db, id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.post("/")
def create(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category)


@router.put("/{id}")
def update(id: int, data: schemas.CategoryCreate, db: Session = Depends(get_db)):
    category = crud.update_category(db, id, data)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    category = crud.delete_category(db, id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Deleted successfully"}