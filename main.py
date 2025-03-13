from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Product
from pydantic import BaseModel
from typing import List

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ProductCreate(BaseModel):
    name: str
    category: str
    description: str
    product_image: str
    sku: str
    unit_of_measure: str
    lead_time: int


@app.get("/product/list", response_model=List[ProductCreate])
def list_products(page: int = 1, db: Session = Depends(get_db)):
    per_page = 10
    products = db.query(Product).offset((page - 1) * per_page).limit(per_page).all()
    return products


@app.get("/product/{pid}/info", response_model=ProductCreate)
def get_product_info(pid: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == pid).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.post("/product/add", response_model=ProductCreate)
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@app.put("/product/{pid}/update", response_model=ProductCreate)
def update_product(pid: int, product: ProductCreate, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == pid).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in product.dict().items():
        setattr(db_product, key, value)
    db.commit()
    return db_product