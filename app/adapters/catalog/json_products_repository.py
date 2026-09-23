import json
from dataclasses import asdict
from pathlib import Path
from uuid import uuid4

import aiofiles

from app.domain.catalog import ProductsRepositoryPort
from app.domain.catalog.models import Product


class JSONProductsRepositoryAdapter(ProductsRepositoryPort):
    def __init__(self, path: Path):
        self.path = path
        self.data = {}

        try:
            with open(self.path, "r") as fp:
                content = fp.read()
        except FileNotFoundError:
            content = "{}"

        self.data = json.loads(content)


    async def create_product(self, name: str, description: str, unit_price: float, image_id: str | None = None) -> Product:
        product_id = str(uuid4())

        product = Product(
            product_id=product_id,
            name=name,
            description=description,
            unit_price=unit_price,
            image_id=image_id,
        )

        self.data[product_id] = asdict(product)

        async with aiofiles.open(self.path, "w") as fp:

            await fp.write(json.dumps(self.data))

        return product
    
    
    async def get_product(self, product_id: str) -> Product | None:
        product_data = self.data.get(product_id)
        if not product_data:
            return None
        return Product(**product_data)
    

    async def list_products(self) -> list[Product]:
        return [Product(**product_data) for product_data in self.data.values()]