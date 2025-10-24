from pydantic import BaseModel, condecimal, ConfigDict
from typing import Optional
from decimal import Decimal


class ProductBase(BaseModel):
    name: str
    price: Optional[Decimal] = None
    category: Optional[str] = None


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[Decimal] = None
    category: Optional[str] = None


class ProductOut(ProductBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
