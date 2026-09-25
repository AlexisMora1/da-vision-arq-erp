from app.domain.suppliers import (
    GetSupplierItemRequest,
    SupplierItemsRepositoryPort,
    SuppliersRepositoryPort,
    get_supplier_item,
)
from app.workflows.exceptions_handler import exceptions_handler
from app.workflows.suppliers.get_supplier_item.models import (
    GetSupplierItemOutput,
    SupplierItemDetails,
)


@exceptions_handler
async def get_supplier_item_workflow(
    supplier_id: str,
    item_id: str,
    suppliers_repository: SuppliersRepositoryPort,
    items_repository: SupplierItemsRepositoryPort,
) -> GetSupplierItemOutput:
    result = await get_supplier_item(
        request=GetSupplierItemRequest(supplier_id=supplier_id, item_id=item_id),
        suppliers_repository=suppliers_repository,
        items_repository=items_repository,
    )
    return GetSupplierItemOutput(data=SupplierItemDetails(**result.item.__dict__))
