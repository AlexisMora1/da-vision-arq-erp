from pydantic import BaseModel


class ProductSummary(BaseModel):
    product_id: str
    name: str
    description: str | None = None
    price: float
    image_url: str | None = None


class ListProductsOutput(BaseModel):
    count: int
    products: list[ProductSummary] = []