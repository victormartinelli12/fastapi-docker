from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    stock: int

class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True)


class SaleBase(BaseModel):
    quantity: int


class SaleCreate(SaleBase):
    product_id: int


class SaleResponse(SaleBase):
    id: int
    value: float
    
    product: ProductResponse 

    model_config = ConfigDict(from_attributes=True)