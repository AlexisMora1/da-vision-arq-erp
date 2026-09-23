from app.domain.catalog import GetProductRequest, ProductsRepositoryPort, get_product
from app.domain.storage import (
    FileRepositoryPort,
    GetDownloadFileUrlRequest,
    get_download_file_url,
)
from app.workflows.catalog.get_product.models import (
    GetProductInput,
    GetProductOutput,
    ProductDetails,
)
from app.workflows.exceptions_handler import exceptions_handler


@exceptions_handler
async def get_product_workflow(
    request: GetProductInput,
    products_repository: ProductsRepositoryPort,
    file_repository: FileRepositoryPort,
) -> GetProductOutput:
    product = await get_product(
        request=GetProductRequest(product_id=request.product_id),
        products_repository=products_repository,
    )

    if product.image_id:
        image = await get_download_file_url(
            request=GetDownloadFileUrlRequest(file_key=product.image_id),
            file_repository=file_repository,
        )
    else:
        image = None

    return GetProductOutput(
        data=ProductDetails(
            product_id=product.product_id,
            name=product.name,
            description=product.description,
            price=product.unit_price,
            image_url=image.url if image else None,
        )
    )

