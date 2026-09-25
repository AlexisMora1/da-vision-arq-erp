from typing import Annotated

from fastapi import APIRouter, Depends

from app.dependencies import get_supplier_items_repository, get_suppliers_repository
from app.domain.suppliers import SupplierItemsRepositoryPort, SuppliersRepositoryPort
from app.workflows.suppliers import (
    CreateSupplierInput,
    CreateSupplierItemInput,
    CreateSupplierItemOutput,
    CreateSupplierOutput,
    GetSupplierInput,
    GetSupplierItemOutput,
    GetSupplierOutput,
    ListSupplierItemsOutput,
    ListSuppliersOutput,
    create_supplier_item_workflow,
    create_supplier_workflow,
    get_supplier_item_workflow,
    get_supplier_workflow,
    list_supplier_items_workflow,
    list_suppliers_workflow,
)

router = APIRouter(tags=["Suppliers"])


@router.get("/suppliers")
async def list_suppliers(
    suppliers_repository: Annotated[
        SuppliersRepositoryPort, Depends(get_suppliers_repository)
    ],
) -> ListSuppliersOutput:
    return await list_suppliers_workflow(suppliers_repository)


@router.get("/suppliers/{supplier_id}")
async def get_supplier(
    supplier_id: str,
    suppliers_repository: Annotated[
        SuppliersRepositoryPort, Depends(get_suppliers_repository)
    ],
) -> GetSupplierOutput:
    input_data = GetSupplierInput(supplier_id=supplier_id)
    return await get_supplier_workflow(input_data, suppliers_repository)


@router.post("/suppliers")
async def create_supplier(
    input_data: CreateSupplierInput,
    suppliers_repository: Annotated[
        SuppliersRepositoryPort, Depends(get_suppliers_repository)
    ],
) -> CreateSupplierOutput:
    return await create_supplier_workflow(input_data, suppliers_repository)


@router.post("/suppliers/{supplier_id}/items")
async def create_supplier_item(
    supplier_id: str,
    input_data: CreateSupplierItemInput,
    suppliers_repository: Annotated[
        SuppliersRepositoryPort, Depends(get_suppliers_repository)
    ],
    items_repository: Annotated[
        SupplierItemsRepositoryPort, Depends(get_supplier_items_repository)
    ],
) -> CreateSupplierItemOutput:
    return await create_supplier_item_workflow(
        supplier_id=supplier_id,
        request=input_data,
        suppliers_repository=suppliers_repository,
        items_repository=items_repository,
    )


@router.get("/suppliers/{supplier_id}/items")
async def list_supplier_items(
    supplier_id: str,
    suppliers_repository: Annotated[
        SuppliersRepositoryPort, Depends(get_suppliers_repository)
    ],
    items_repository: Annotated[
        SupplierItemsRepositoryPort, Depends(get_supplier_items_repository)
    ],
) -> ListSupplierItemsOutput:
    return await list_supplier_items_workflow(
        supplier_id=supplier_id,
        suppliers_repository=suppliers_repository,
        items_repository=items_repository,
    )


@router.get("/suppliers/{supplier_id}/items/{item_id}")
async def get_supplier_item(
    supplier_id: str,
    item_id: str,
    suppliers_repository: Annotated[
        SuppliersRepositoryPort, Depends(get_suppliers_repository)
    ],
    items_repository: Annotated[
        SupplierItemsRepositoryPort, Depends(get_supplier_items_repository)
    ],
) -> GetSupplierItemOutput:
    return await get_supplier_item_workflow(
        supplier_id=supplier_id,
        item_id=item_id,
        suppliers_repository=suppliers_repository,
        items_repository=items_repository,
    )
