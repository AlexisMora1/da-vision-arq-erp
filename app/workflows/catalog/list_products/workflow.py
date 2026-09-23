from app.domain.catalog import ProductsRepositoryPort
from app.domain.storage import FileRepositoryPort
from app.workflows.catalog.list_products.models import (
    ListProductsOutput,
    ProductSummary,
)
from app.workflows.exceptions_handler import exceptions_handler


@exceptions_handler
async def list_products_workflow(
    products_repository: ProductsRepositoryPort,
    files_repository: FileRepositoryPort,
) -> ListProductsOutput:
    products = await products_repository.list_products()

    summaries = []

    for product in products:
        if product.image_id:
            image = await files_repository.get_download_file_url(file_id=product.image_id)
            url = image.get("url")
        else:
            url = None

        summaries.append(
            ProductSummary(
                product_id=product.product_id,
                name=product.name,
                description=product.description,
                price=product.unit_price,
                image_url=url
            )
        )
    return ListProductsOutput(
        count=len(summaries),
        products=summaries
    )