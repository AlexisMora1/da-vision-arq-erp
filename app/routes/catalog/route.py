from typing import Annotated

from fastapi import APIRouter, Depends

from app.dependencies import get_file_repository, get_products_repository
from app.domain.catalog import ProductsRepositoryPort
from app.domain.storage import FileRepositoryPort
from app.workflows.catalog import (
    CreateProductInput,
    GetProductInput,
    create_product_workflow,
    get_product_workflow,
    list_products_workflow,
)

router = APIRouter(
    tags=["Catalog"]
)


@router.get("/products/{product_id}")
async def get_product(
    product_id: str, 
    products_repository: Annotated[ProductsRepositoryPort, Depends(get_products_repository)], 
    file_repository: Annotated[FileRepositoryPort, Depends(get_file_repository)]
):
    return await get_product_workflow(
        request=GetProductInput(product_id=product_id),
        products_repository=products_repository,
        file_repository=file_repository,
    )


@router.post("/products")
async def create_product(
    request: CreateProductInput,
    products_repository: Annotated[ProductsRepositoryPort, Depends(get_products_repository)],
):
    return await create_product_workflow(
        request=request,
        products_repository=products_repository,
    )


@router.get("/products")
async def list_products(
    products_repository: Annotated[ProductsRepositoryPort, Depends(get_products_repository)],
    file_repository: Annotated[FileRepositoryPort, Depends(get_file_repository)]
):
    return await list_products_workflow(
        products_repository=products_repository,
        files_repository=file_repository,
    )