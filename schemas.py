from pydantic import BaseModel
from typing import Optional
import datetime

class ProductBase(BaseModel):
    name: str
    category: str
    description: Optional[str] = None
    product_image: Optional[str] = None
    sku: str
    unit_of_measure: str
    lead_time: Optional[int] = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductInDB(ProductBase):
    id: int
    created_date: datetime.datetime
    updated_date: datetime.datetime

    class Config:
        orm_mode = True