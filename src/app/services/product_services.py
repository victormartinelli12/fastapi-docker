from sqlalchemy.orm import Session
from sqlalchemy import select

from src.app.db.models import Product


class ProductService:
    def __init__(self, session: Session):
        self._db = session

    def list_products(self) -> list[Product]:
        stmt = select(Product)
        return self._db.scalars(stmt).all()

    def get_product(self, product_id: int) -> Product | None:
        return self._db.get(Product, product_id)

    def create_product(self, product: Product) -> Product:
        self._db.add(product)
        self._db.commit()
        self._db.refresh(product)
        return product

    def update_product(self, product_id: int,
    name: str, description: str,price: float, stock: int) -> Product | None:
        product = self.get_product(product_id=product_id)
        if not product:
            return None
        product.name = name
        product.description = description
        product.price = price
        product.stock = stock

        self._db.commit()
        self._db.refresh(product)
        return product

    def delete_product(self, product_id: int) -> bool:
        product = self.get_product(product_id=product_id)

        if not product:
            return False

        self._db.delete(product)
        self._db.commit()
        return True