from typing import Protocol

from app.domain.catalog.models import Product


class ProductsRepositoryPort(Protocol):
    async def create_product(self, name: str, description: str, unit_price: float, image_id: str | None = None) -> Product:
        ...

    async def get_product(self, product_id: str) -> Product | None:
        ...

    async def list_products(self) -> list[Product]:
        ...