from pydantic import BaseModel


class ProductDetails(BaseModel):
    product_id: str
    name: str
    description: str
    price: float
    image_url: str | None = None


class GetProductInput(BaseModel):
    product_id: str


class GetProductOutput(BaseModel):
    data: ProductDetails