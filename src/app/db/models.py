from sqlalchemy import create_engine, String, ForeignKey
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped, mapped_column,
    relationship,
    sessionmaker)

from src.app.core.config import config 


engine = create_engine(config.db_url, echo=config.debug)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    stock: Mapped[int] = mapped_column(nullable=False)

    sales: Mapped[list["Sale"]] = relationship(back_populates="product")


class Sale(Base):
    __tablename__ = "sales"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)
    value: Mapped[float] = mapped_column(nullable=False)

    product: Mapped["Product"] = relationship(back_populates="sales")