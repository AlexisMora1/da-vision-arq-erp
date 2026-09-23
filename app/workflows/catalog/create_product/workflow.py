from app.domain.catalog import ProductsRepositoryPort
from app.workflows.catalog.create_product.models import (
    CreateProductInput,
    CreateProductOutput,
    ProductCreated,
)
from app.workflows.exceptions_handler import exceptions_handler


@exceptions_handler
async def create_product_workflow(
    request: CreateProductInput,
    products_repository: ProductsRepositoryPort
) -> CreateProductOutput: 
    product = await products_repository.create_product(
        name=request.name,
        description=request.description,
        unit_price=request.unit_price,
        image_id=request.image_id,
    )

    return CreateProductOutput(
        message="Product created successfully",
        data=ProductCreated(
            product_id=product.product_id,
            name=product.name,
            description=product.description,
            price=product.unit_price,
            image_id=product.image_id,
        ),
    )