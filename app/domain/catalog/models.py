from dataclasses import dataclass


@dataclass
class Product:
    product_id: str
    name: str
    description: str
    unit_price: float
    image_id: str | None = None


@dataclass 
class CreateProductRequest:
    name: str
    description: str
    unit_price: float
    image_id: str | None = None


@dataclass
class CreateProductResponse:
    product_id: str
    name: str
    description: str
    unit_price: float
    image_id: str | None = None


@dataclass
class GetProductRequest:
    product_id: str


@dataclass
class GetProductResponse:
    product_id: str
    name: str
    description: str
    unit_price: float
    image_id: str | None = None


@dataclass
class ListProductsResponse:
    products: list[Product]