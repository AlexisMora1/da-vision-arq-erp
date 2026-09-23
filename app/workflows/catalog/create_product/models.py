from pydantic import BaseModel


class ProductCreated(BaseModel):
    product_id: str
    name: str
    description: str
    price: float
    image_id: str | None = None


class CreateProductInput(BaseModel):
    name: str
    description: str
    unit_price: float
    image_id: str | None = None


class CreateProductOutput(BaseModel):
    message: str
    data: ProductCreated