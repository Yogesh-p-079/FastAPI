# models.py
from sqlalchemy import Column, Integer, String, Enum, BigInteger, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
import datetime
import enum

Base = declarative_base()

class CategoryEnum(str, enum.Enum):
    FINISHED = "finished"
    SEMI_FINISHED = "semi-finished"
    RAW = "raw"

class UnitEnum(str, enum.Enum):
    METER = "mtr"
    MILLIMETER = "mm"
    LITER = "ltr"
    MILLILITER = "ml"
    CENTIMETER = "cm"
    MILLIGRAM = "mg"
    GRAM = "gm"
    UNIT = "unit"
    PACK = "pack"

class Product(Base):
    __tablename__ = "products"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    category = Column(Enum(CategoryEnum), nullable=False)
    description = Column(String(250))
    product_image = Column(String(255))  # Defined max length
    sku = Column(String(100), unique=True, nullable=False)
    unit_of_measure = Column(Enum(UnitEnum), nullable=False)
    lead_time = Column(Integer)
    created_date = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    updated_date = Column(TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
