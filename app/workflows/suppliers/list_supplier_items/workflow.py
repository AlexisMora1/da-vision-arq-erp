from app.domain.suppliers import (
    SupplierItemsRepositoryPort,
    SuppliersRepositoryPort,
    list_supplier_items,
)
from app.workflows.exceptions_handler import exceptions_handler
from app.workflows.suppliers.list_supplier_items.models import (
    ListSupplierItemsOutput,
    SupplierItemSummary,
)


@exceptions_handler
async def list_supplier_items_workflow(
    supplier_id: str,
    suppliers_repository: SuppliersRepositoryPort,
    items_repository: SupplierItemsRepositoryPort,
) -> ListSupplierItemsOutput:
    result = await list_supplier_items(
        supplier_id=supplier_id,
        suppliers_repository=suppliers_repository,
        items_repository=items_repository,
    )
    data = [SupplierItemSummary(**item.__dict__) for item in result.items]
    return ListSupplierItemsOutput(count=len(data), data=data)
