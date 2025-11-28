from fastapi import APIRouter, Depends, HTTPException

from src.app.db.models import SessionLocal
from src.app.models.schemas import SaleCreate, SaleResponse
from src.app.services.sale_services import SaleService

router = APIRouter()


def get_session() -> SessionLocal:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def get_sale_service(session: SessionLocal = Depends(get_session)) -> SaleService:
    return SaleService(session=session)


@router.get("/sales", response_model=list[SaleResponse])
def get_sales(sale_service: SaleService = Depends(get_sale_service)):
    return sale_service.list_sales()


@router.get("/sales/{sale_id}", response_model=SaleResponse)
def get_sale(sale_id: int, sale_service: SaleService = Depends(get_sale_service)):
    return sale_service.get_sale(sale_id)


@router.post("/sales", response_model=SaleResponse)
def create_sale(
    sale_in: SaleCreate,
    service: SaleService = Depends(get_sale_service)
):
    created_sale = service.create_sale(
        product_id=sale_in.product_id, 
        quantity=sale_in.quantity
    )

    if not created_sale:
        raise HTTPException(status_code=400, detail="Product not found or insufficient stock")
    
    return created_sale
