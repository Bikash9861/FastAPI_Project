from pydantic import BaseModel

# ✅ Create Category
class CategoryCreate(BaseModel):
    name: str


# ✅ Response Category
class Category(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True   # for SQLAlchemy (important)
# CATEGORY
class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int

    class Config:
        orm_mode = True


# PRODUCT
class ProductBase(BaseModel):
    name: str
    price: int
    category_id: int

class ProductCreate(ProductBase):
    pass


class CategoryNested(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class ProductResponse(BaseModel):
    id: int
    name: str
    price: int
    category: CategoryNested   # 🔥 Nested response

    class Config:
        orm_mode = True