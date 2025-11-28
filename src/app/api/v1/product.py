from fastapi import APIRouter, Depends

from src.app.db.models import SessionLocal
from src.app.models.schemas import ProductCreate, ProductResponse
from src.app.services.product_services import ProductService
from src.app.db.models import Product

router = APIRouter()


def get_session() -> SessionLocal:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def get_product_service(session: SessionLocal = Depends(get_session)) -> ProductService:
    return ProductService(session=session)


@router.get("/products", response_model=list[ProductResponse])
def get_products(product_service: ProductService = Depends(get_product_service)):
    return product_service.list_products()


@router.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, product_service: ProductService = Depends(get_product_service)):
    return product_service.get_product(product_id)


@router.post("/products", response_model=ProductResponse)
def create_product(product: ProductCreate, product_service: ProductService = Depends(get_product_service)):
    newProduct = Product(
        name=product.name,
        description=product.description,
        price=product.price,
        stock=product.stock
    )
    return product_service.create_product(newProduct)


@router.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductCreate, product_service: ProductService = Depends(get_product_service)):
    return product_service.update_product(product_id, product.name, product.description, product.price, product.stock)


@router.delete("/products/{product_id}")
def delete_product(product_id: int, product_service: ProductService = Depends(get_product_service)):
    return product_service.delete_product(product_id)
