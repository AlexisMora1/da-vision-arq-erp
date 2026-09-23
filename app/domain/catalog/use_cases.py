from app.domain.catalog.errors import ProductNotFoundError
from app.domain.catalog.models import (
    CreateProductRequest,
    CreateProductResponse,
    GetProductRequest,
    GetProductResponse,
    ListProductsResponse,
)
from app.domain.catalog.ports import ProductsRepositoryPort


async def create_product(
    request: CreateProductRequest, 
    products_repository: ProductsRepositoryPort
) -> CreateProductResponse:

    product = await products_repository.create_product(
        name=request.name,
        description=request.description,
        unit_price=request.unit_price,
        image_id=request.image_id,
    )

    return CreateProductResponse(
        product_id=product.product_id,
        name=product.name,
        description=product.description,
        unit_price=product.unit_price,
        image_id=product.image_id,
    )


async def get_product(
    request: GetProductRequest,
    products_repository: ProductsRepositoryPort
) -> GetProductResponse:

    product = await products_repository.get_product(
        product_id=request.product_id
    )

    if not product:
        raise ProductNotFoundError(f"Product with ID {request.product_id} not found") 

    return GetProductResponse(
        product_id=product.product_id,
        name=product.name,
        description=product.description,
        unit_price=product.unit_price,
        image_id=product.image_id,
    )


async def list_products(
    products_repository: ProductsRepositoryPort
) -> ListProductsResponse:

    products = await products_repository.list_products()

    return ListProductsResponse(
        products=products
    )