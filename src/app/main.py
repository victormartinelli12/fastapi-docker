from fastapi import FastAPI

from src.app.api.v1 import product, sale
from src.app.core.config import config 
from src.app.core.logging import setup_logging
from src.app.db.models import Base, engine


setup_logging()
Base.metadata.create_all(bind=engine)

app = FastAPI(title=config.app_name)

app.include_router(product.router, prefix="/api/v1", tags=["Products"])
app.include_router(sale.router, prefix="/api/v1", tags=["Sales"])