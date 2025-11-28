from sqlalchemy.orm import Session
from sqlalchemy import select

from src.app.db.models import Sale, Product


class SaleService:
    def __init__(self, session: Session):
        self._db = session

    def list_sales(self) -> list[Sale]:
        stmt = select(Sale)
        return self._db.scalars(stmt).all()

    def get_sale(self, sale_id: int) -> Sale | None:
        return self._db.get(Sale, sale_id)

    def create_sale(self, product_id: int, quantity: int) -> Sale | None:
        product = self._db.get(Product, product_id)
        if not product:
            return None
        if product.stock < quantity:
            return None

        product.stock -= quantity 
        total_value = product.price * quantity

        sale = Sale(
            product_id=product_id,
            quantity=quantity,
            value=total_value
        )

        self._db.add(sale)
        self._db.commit()
        self._db.refresh(sale)

        return sale